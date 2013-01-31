# coding: utf8
# intente algo como
def index(): 
	facturas = dbRosan().select(dbRosan.factura.ALL, orderby=dbRosan.factura.fecha)
	return dict(facturas=facturas)


# Funcion nuevaFactura: INicio del creación de nueva factura.
def nuevaFactura():
	return dict()
