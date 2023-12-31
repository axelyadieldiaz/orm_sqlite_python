import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuarios

db=orm.SQLiteORM("db_biblioteca")
db.crear_tabla(Autores)
db.crear_tabla(Libros)
db.crear_tabla(Usuarios)

# autor_uno={
#     "dni":78945612,"nombre":"quevedo","apellidos":"escoja de los rios"
# }
# db.insertarUno("Autores",autor_uno)
usuarios_varios=[
    {
        "dni":745896,
        "nombre":"nadine",
        "apellidos":"atoccsa",
        "f_nacimiento":"06/04/2005",
        "estado":"activo"
    },
    {
       "dni":78965432,
        "nombre":"feli",
        "apellidos":"ccaccahua",
        "f_nacimiento":"07/11/1997",
        "estado":"activo" 
    },
    {
        "dni":74123658,
        "nombre":"bichota",
        "apellidos":"de taype",
        "f_nacimiento":"28/11/2023",
        "estado":"inactivo"
    },
    {
        "dni":75369842,
        "nombre":"chamo",
        "apellidos":"no jodas",
        "f_nacimiento":"30/11/2023",
        "estado":"activo"
    },
    {
        "dni":67392023,
        "nombre":"yadira",
        "apellidos":"quiero mani",
        "f_nacimiento":"509 a.c",
        "estado":"momia"
    }]
# db.insertarVarios("Usuarios",usuarios_varios)

#muestra una lista de tuplas
# print(db.mostrar("Usuarios"))
#muestra un objeto con sus campos y sus valores
# print(db.mostrar("Usuarios",type="objeto"))
#tambien puedo filtrar informacion
#print(db.mostrar("Usuarios",where="nombre LIKE 'cha%'",type="objeto"))
#print(db.mostrar("Usuarios",where="dni =78965432",type="objeto"))

#db.actualizar("Usuarios",{"estado":"activo"},where="nombre= 'yadira'")
#db.actualizar("Usuarios",{"f_nacimiento":"11/08/2005"},where="74123698")
#dato_actualizar=("nombre":"chamos","apellidos":"ya es salida")
#db.actualizar("Usuarios",dato_actualizar,where="dni=75369842")

db.eliminar("Usuarios",where="nombre='bichota'")
db.eliminar("Usuarios",where="dni=75369842")

print(db.mostrar("Usuarios",type="objeto"))