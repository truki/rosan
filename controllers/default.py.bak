# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    response.flash = "Bienvenido a Rosan!"
    return dict()
        
def frontend():
    return dict()

def clientes():
    return dict()  
    
def facturas():
    return dict()

def presupuestos():
    return dict()  
    
def articulos():
    return dict()
    
def contabilidad():
    return dict()
    
def login():
    return dict()

def error():
    return dict()
    
def nuevoCliente():
    response.flash = 'Sección Clientes'
    form = SQLFORM(dbRosan.cliente)
    
    grid = SQLFORM.grid(dbRosan.cliente)
    if form.process().accepted:
        response.flash = 'Insertado'
        grid = SQLFORM.grid(dbRosan.cliente)
    elif form.errors:
        response.flash = 'Ha habido errores'
    else:
        response.flash = 'Rellene el formulario para insertar un cliente'
    return dict(form=form, grid=grid)

def nuevaFactura():
    # se introduce el cliente, fecha, descuento, retencion y cualquier otro valor global de la factura
    # se podría marcar como pagada.
    response.flash = "Introduce los datos de la nueva factura"

    return dict()


def nuevoPresupuesto():

    response.flash = "Introduce los datos del nuevo presupuesto"
    return dict()
