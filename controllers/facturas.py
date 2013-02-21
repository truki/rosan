# coding: utf8
# intente algo como
def index(): 
	facturas = dbRosan().select(dbRosan.factura.ALL, orderby=dbRosan.factura.fecha)
	return dict(facturas=facturas)


# Funcion nuevaFactura: INicio del creación de nueva factura.
def nuevaFactura():
	#buscamos el ultimo id de fcatura_temp

	#creamos la variable sesión
	session.facturaId = 1
	return dict()

# Funcion detalleFactura: donde se insertan las lineas de cada factura
def detalleFactura():
	info=""
	
	#recuperamos los datos de la factura temporal a partir de la variable de sesion que hemos pasado
	datosFacturaTemp = dbRosan.factura_temp(session.facturaId)
	neto = datosFacturaTemp.neto 									#neto de la factura (sin IVA)
	descuento = datosFacturaTemp.descuento							#descuento de la factura (cantidad descontada)
	retencion = datosFacturaTemp.retencion 							#cantidad retenida deppendiendo del tipo_retencion
	totalIVA = datosFacturaTemp.total_iva        					#suma del IVA dependiendo del tipo_iva
	totalBruto = datosFacturaTemp.total_bruto						#suma de todo

	formConcepto = FORM((FIELDSET(DIV(LABEL("Descripción", _class="control-label"), 
									  DIV(TEXTAREA(_class="span7", _rows="5", _placeholder="Introduce la descripción", _name="descripcion", requires=IS_NOT_EMPTY(error_message="Introduce una descripción en el concepto")), _class="controls"), 
								   _class="control-group")),
								  DIV(LABEL("Cantidad", _class="control-label"), 
									  DIV(INPUT(_name="cantidad", _type="text", _class="input-large", _id="cantidad", _value="1", requires=IS_INT_IN_RANGE(1,999999, error_message="Introduce un valor entre 1 y 999999")), _class="controls"), 
								   _class="control-group"),
								  DIV(LABEL("Precio", _class="control-label"),
								  	  DIV(INPUT(_name="precio", _type="text", _class="input-large", _id="precio", requires=IS_FLOAT_IN_RANGE(0,9999999, dot=".", error_message="Introduce un valor entre 0 y 9999999, el signo de los decimales es el .")), _class="controls"),
								   _class="control-group"),
								  DIV(DIV(INPUT(_name="insertarConcepto", _type="submit", _class="btn btn-primary", _id="insertarConcepto", _value="Insertar"), _class="controls"), 
								   _class="control-group")), 
						_class="form-horizontal", _name="nuevoConcepto", _action=URL('/detalleFactura'))
	if formConcepto.accepts(request, session):
		info="Concepto insertado"
		#Se inserta la lineaa en factura_detalle_temp
		dbRosan.factura_detalle_temp.insert(id_factura=1, id_articulo=0, 
											articulo=formConcepto.vars.descripcion, precio=formConcepto.vars.precio, cantidad=formConcepto.vars.cantidad, 
											total_articulo=formConcepto.vars.precio * formConcepto.vars.cantidad)
		#se actualizan los totales en factura_temp
		totalArticulo = formConcepto.vars.precio * formConcepto.vars.cantidad
		neto = (dbRosan.factura_temp.neto + totalArticulo)
		retencion = (dbRosan.factura_temp.tipo_retencion/100) * neto
		totalIVA = ((dbRosan.factura_temp.tipo_iva/100) * neto)
		totalBruto = ((neto - retencion) + totalIVA)

		dbRosan(dbRosan.factura_temp.id == session.facturaId).update(neto = neto, descuento=0, retencion = retencion, total_iva = totalIVA, total_bruto = totalBruto)

	elif formConcepto.errors:
		info="Concepto erróneo"
	else:
		info="Rellena el formulario"

	formArticulo = FORM()

	lineas = dbRosan().select(dbRosan.factura_detalle_temp.ALL)	
	return dict(info=info, formConcepto=formConcepto, lineas=lineas, formArticulo=formArticulo, neto=dbRosan.factura_temp(session.facturaId).neto, descuento=dbRosan.factura_temp(session.facturaId).descuento, retencion=dbRosan.factura_temp(session.facturaId).retencion, totalIVA = dbRosan.factura_temp(session.facturaId).total_iva, totalBruto = dbRosan.factura_temp(session.facturaId).total_bruto)

#eliminación de la linea del detalle de la factura desde botón elimanar de la tabla con el detalle temporal.
def eliminarLineaTemp():
    #query para encontrar la linea se pasa como argumento el idLinea
    lineaEliminada = dbRosan.factura_detalle_temp(request.args[0]) or redirect(URL('error'))
    
    #borramos la linea
    dbRosan(dbRosan.factura_detalle_temp.id==lineaEliminada.id).delete()
    
    #Actualizamos los valores Neto, Retención,...
    datosFacturaTemp = dbRosan.factura_temp(session.facturaId)
    neto = datosFacturaTemp.neto - lineaEliminada.total_articulo
    descuento = datosFacturaTemp.descuento
    retencion = datosFacturaTemp.retencion - (lineaEliminada.total_articulo*(datosFacturaTemp.tipo_retencion/100))
    totalIVA = datosFacturaTemp.total_iva  - (lineaEliminada.total_articulo*(datosFacturaTemp.tipo_iva/100))
    totalBruto = datosFacturaTemp.total_bruto - (lineaEliminada.total_articulo*(datosFacturaTemp.tipo_iva/100)) - lineaEliminada.total_articulo
    dbRosan(dbRosan.factura_temp.id == session.facturaId).update(neto = neto, descuento=0, retencion = retencion, total_iva = totalIVA, total_bruto = totalBruto)

    redirect(URL('/detalleFactura'))

