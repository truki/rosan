# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    clientes = dbRosan().select(dbRosan.cliente.ALL, orderby=dbRosan.cliente.nombre)
    return dict(clientes=clientes)


def eliminar():
    id = request.args[0]
    clienteEliminado = dbRosan.articulo(id)
    nombre = articuloEliminado.nombre
    dbRosan(dbRosan.articulo.id==id).delete()
    return dict(id=id, nombre=nombre)

    

def clientes():
    form = SQLFORM(dbRosan.cliente)
    if form.process().accepted:
        response.flash = 'cliente insertado'
    return dict(form=form)  
  

def nuevoCliente():
    info = ""
    errores = ""

    form = SQLFORM(dbRosan.cliente, submit_button = 'Insertar')
    
    if form.process().accepted:
        info = "El cliente ha sido insertado"
    elif form.errors:
        errores = "Ha habido errores compruebe los campos"
    else:
        info = "Rellene el formulario para introducir un cliente en la base de datos."
    return dict(form=form, info=info, errores=errores)

def verCliente():
    info = ""
    errores = ""

    id = dbRosan.cliente(request.args[0]) or redirect(URL('error'))
    form = SQLFORM(dbRosan.cliente, id, submit_button = 'Guardar')
    if form.process().accepted:
        info = "El cliente ha sido modificado"
    elif form.errors:
        errores = "Ha habido un error"
    else:
        info = "Si lo deseas puedes modificar el artículo, después pulsa sobre guardar"
    return dict(form=form, info=info, errores=errores)
