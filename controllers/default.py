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
    form = SQLFORM(dbRosan.cliente)
    if form.process().accepted:
        response.flash = 'cliente insertado'
    return dict(form=form)  
    
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
