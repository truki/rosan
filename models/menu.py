response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Clientes'),URL('default','nuevoCliente')==URL(),URL('default','nuevoCliente'),[]),
(T('Facturas'),URL('default','nuevaFactura')==URL(),URL('default','nuevaFactura'),[]),
(T('Presupuestos'),URL('default','nuevoPresupuesto')==URL(),URL('default','nuevoPresupuesto'),[])
]
