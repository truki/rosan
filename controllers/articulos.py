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