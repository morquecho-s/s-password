from bdst.conexion import *

DB_NAME = "psword"
__DB_PASSWORD = 'sergiomolla160'
DB_TABLES = (
    'ix105',##inventario 0
)

torres = Database(
    'root',
    __DB_PASSWORD,
    'localhost'
)

torres.createDataBase(DB_NAME)
torres.setDB(DB_NAME)
torres.createTable(DB_TABLES[0],(
                   ("mail",str,NOT_NULL),
                   ("passw",str,f"{NOT_NULL} {KEY}"),
                   ("last modified",str,NOT_NULL)))