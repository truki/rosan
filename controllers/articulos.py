# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
	articulos = dbRosan().select(dbRosan.articulo.ALL, orderby=dbRosan.articulo.titulo)
	return dict(articulos=articulos)

def eliminar():
	id = request.args[0]
	articuloEliminado = dbRosan.articulo(id)
	nombre = articuloEliminado.titulo
	dbRosan(dbRosan.articulo.id==id).delete()
	return dict(id=id, nombre=nombre)

def nuevoArticulo():
    info = ""
    errores = ""

    form = SQLFORM(dbRosan.articulo)
    
    if form.process().accepted:
        info = "El artículo ha sido insertado"
    elif form.errors:
        errores = "Ha habido errores compruebe los campos"
    else:
        info = "Rellene el formulario para introducir un nuevo artículo en la base de datos."
    return dict(form=form, info=info, errores=errores)