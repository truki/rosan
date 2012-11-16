# coding: utf8
"""
just copy paste this code into your model and replace dbRosan to something
you prefer or what is used in your code, another thing that should be known is that
this code still cannot distinguish what exactly should be in reference title - name
when you use generic appadmin so please remove all fiealds you don't need not require 
"""
"""
database class object creation
"""
dbRosan = SQLDB("sqlite://dbRosan.db")

"""
Tabla de clientes
"""
dbRosan.define_table("cliente",
      SQLField("cif", "string", length=9, notnull=True, default=None),
      SQLField("nombre", "string", length=200, notnull=True, default=None),
      SQLField("direccion", "string", length=200, notnull=True, default=None),
      SQLField("localidad", "string", length=100, notnull=True, default=None),
      SQLField("cod_postal", "string", length=5, notnull=True, default=None),
      SQLField("email", "string", length=100, notnull=True, default=None),
      SQLField("www","string", length=200, notnull=True, default=None)
      ) 

"""
Tabla facturas
"""
dbRosan.define_table("factura",
      SQLField("fecha", "date", notnull=True, default=None),
      SQLField("id_cliente", dbRosan.cliente),
      SQLField("tipo_iva", "double", notnull=True, default=None),
      SQLField("neto", "double", notnull=True, default=None),
      SQLField("retencion", "double", notnull=True, default=None),
      SQLField("descuento", "integer", notnull=True, default=None),
      SQLField("total_iva", "double", notnull=True, default=None),
      SQLField("total_bruto", "double", notnull=True, default=None),
      SQLField("pagada", "boolean", notnull=True, default=False)) 



"""
Table con el detalle de las facturas
"""
dbRosan.define_table("factura_detalle",
      SQLField("id_factura", dbRosan.factura),
      SQLField("articulo", "text", notnull=True, default=None),
      SQLField("precio", "double", notnull=True, default=None),
      SQLField("cantidad", "integer", notnull=True, default=None),
      SQLField("total_articulo", "double", notnull=True, default=None))  
           
"""
Tabla articulos
"""
dbRosan.define_table("articulo",
      SQLField("descripcion", "text", notnull=True, default=None),
      SQLField("precio", "double", notnull=True, default=None)) 
      
"""
Tabla almacen, contiene los stocks de los articulos
"""
dbRosan.define_table("almacen", 
      SQLField("id_articulo", dbRosan.articulo),
      SQLField("cantidad", "integer", notnull=True, default=0),
      SQLField("max", "integer", notnull=True, default=0),
      SQLField("min", "integer", notnull=True, default=0))
      
      

"""
Relations between tables (remove fields you don't need from requires)
"""
dbRosan.factura.id_cliente.requires=IS_IN_DB(dbRosan, 'cliente.id', '%(nombre)s')

dbRosan.factura_detalle.id_factura.requires=IS_IN_DB(dbRosan, 'factura.id')

dbRosan.almacen.id_articulo.requires=IS_IN_DB(dbRosan, 'articulo.id' '%(nombre)s')
