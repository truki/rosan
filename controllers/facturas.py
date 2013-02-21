# coding: utf8
# intente algo como
def index(): 
	facturas = dbRosan().select(dbRosan.factura.ALL, orderby=dbRosan.factura.fecha)
	return dict(facturas=facturas)


# Funcion nuevaFactura: INicio del creación de nueva factura.
def nuevaFactura():

	return dict()

# Funcion detalleFactura: donde se insertan las lineas de cada factura
def detalleFactura():
	info=""
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
		dbRosan.factura_detalle_temp.insert(id_factura=1, id_articulo=0, 
											articulo=formConcepto.vars.descripcion, precio=formConcepto.vars.precio, cantidad=formConcepto.vars.cantidad, 
											total_articulo=formConcepto.vars.precio * formConcepto.vars.cantidad)

	elif formConcepto.errors:
		info="Concepto erróneo"
	else:
		info="Rellena el formulario"

	formArticulo = FORM()

	lineas = dbRosan().select(dbRosan.factura_detalle_temp.ALL)	
	return dict(info=info, formConcepto=formConcepto, lineas=lineas, formArticulo=formArticulo)

