# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()
    

def clientes():
    form = SQLFORM(dbRosan.cliente)
    if form.process().accepted:
        response.flash = 'cliente insertado'
    return dict(form=form)  
  