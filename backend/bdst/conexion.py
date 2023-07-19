from mysql import connector
try:
    from virtualTable import Table
except:
    from backend.bdst.virtualTable import Table
# DATE: 16/01/23
# V = 1.0

# DATE: 4/4/23
# V = 1.5

AND = ' and '
OR = ' or '
## yya...
class Database(Table):
    def __init__(self,_user:str,_password:str,_host:str)-> None:
        super().__init__()
        self.__connection = connector.connect(
            user = _user,
            password = _password,
            host = _host,
            )
        self.__cursor = self.__connection.cursor()
        self.tableName:str = ""
        self.name:str = ""

    def exportActualTable(self,dir:str)->None:
        tabla_html = """
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <style>
    table {
        width: 100%;
        border-collapse: collapse;
        background-color: #f8f8f8;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    
    .header-row {
        background-color: #333;
        color: #fff;
        text-align: left;
        padding: 10px;
    }
    
    td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    
    tr:hover {
        background-color: #e0e0e0;
    }
</style>

</head>
<body>

"""
        data =  self.selectAll()
        data.insert(0,self.getPropertys())
        tabla_html += "<table>\n"

        for i, fila in enumerate(data):
            if i == 0:
                tabla_html += "<tr class='header-row'>\n"
                for elemento in fila:
                    tabla_html += f"<th>{elemento}</th>\n"
                tabla_html += "</tr>\n"
            else:
                tabla_html += "<tr>\n"
                for elemento in fila:
                    tabla_html += f"<td>{elemento}</td>\n"
                tabla_html += "</tr>\n"

        tabla_html += "</table></body></html>"
        with open(f"{dir}/{self.tableName}.html",'w') as file:
            file.write(tabla_html)

            
        return tabla_html
    
    def setTable(self,tableName:str)->None:
        """
        Este método establece que tabla se usara en la base de datos.
        ! también agrega los registros en la tabla simulada.
        @tableName : es el nombre de la tabla \n la tabla actual.
        """
        self.tableName = tableName #! actualiza la propiedad de __table a el nombre de la tabla.
        self.selectPropertys() ## selecciona y actualiza los atributos de la tabla actual.
        self.addRegister(self.selectAll()) ## agrega todos los registros de la tabla a la simulación de la tabla.
    
    def setDB(self,name:str)->None:
        self.__execute(f'use `{name}`')
        self.name = name

    # INSERT KEYWORD (mucha palabra en ingles poca documentación no??)....
    def insertV(self,*values)->bool:
        """
            El parámetro values recibe una tuple del
            registro que se agregara a la BD
            ! RECUERDA RESPETAR EL ORDEN Y TIPO DE DATOS!
        """
        try:
            values:str = self._prepareValues(values)
            # print(f"INSERT INTO {self.tableName} VALUES ({values})")
            self.__execute(f"INSERT INTO `{self.tableName}` VALUES ({values})")
            return True
        except Exception as e:
            print(e)
            return (False,e)
    
    def insertVForC(self,columns:tuple|str,*values)->bool:
        """
        Este método inserta datos en la base de datos.\n
        estos datos se insertan en las columnas que se le indique.\n
        @columns son las columnas donde insertaras los datos.\n
        @values son los datos que se insertaran en las columnas. \n
        """
        try:
            values = self._prepareValues(values)
            columns = self._prepareColumns(columns)
            self._execute(
                f"INSERT INTO {self.tableName}({columns}) VALUES ({values})")
            return True
        except Exception as e:
            print(e)
            return False

    # SELECT KEYWORD....
    def selectPropertys(self)->tuple:
        #!hace una petición a la tabla para saber sus propiedades.
        self._execute(f"select * from {self.tableName}")
        self.atributos = self.__cursor.column_names
        self.setColumns(self.atributos)
        return self.atributos

    
    def selectAll(self) -> list:
        #selecciona toda la tabla y la retorna.
        resultConsole:list = self._execute(f"select * from `{self.tableName}`")
        return resultConsole
    
    def selectC(self,columns:tuple)-> list:
        """
        Este método selecciona todos los registros de \n
        las columnas que le indiquemos por medio del \n
        parámetro @columns.

        @param columns debe seguir este formato.
            ! columns = 'nombre','apellido','edad'
        """
        newColumns = self._prepareColumns(columns)
        resultConsole:list = self._execute(f"select {newColumns} from `{self.tableName}`")
        return resultConsole
    
    def selectAllW(self,where:dict,concatenator:str = 'or')->list:
        """
        Este método selecciona todo en la tabla \n delimitando por la keyword WHERE.

        @param where recibe los delimitadores de la seleccion\n
            !El parámetro where debe entregarse en el siguiente formato...\n
            !where = {"id":'22',"nombre":'Juan'}.\n
            !La clave es el nombre de la propiedad y el valor es el dato que deberá tener. 
        """
        newWhere:str = self._prepareWhere(where,concatenator)
        #? print(newWhere)
        resultConsole:list = self._execute(f"select * from `{self.tableName}` where {newWhere}")
        return resultConsole
    
    def selectAllWLike(self,where:dict,concatenator:str = 'or')->list:
        """
        Este método selecciona todo en la tabla \n delimitando por la keyword WHERE.

        @param where recibe los delimitadores de la seleccion\n
            !El parámetro where debe entregarse en el siguiente formato...\n
            !where = {"id":'22',"nombre":'Juan'}.\n
            !La clave es el nombre de la propiedad y el valor es el dato que deberá tener. 
        """
        newWhere:str = self._prepareWhere(where,concatenator,asing=' LIKE ',isLike = True)
        #? print(newWhere)
        resultConsole:list = self._execute(f"select * from `{self.tableName}` where {newWhere};")
        return resultConsole

    
    def selectCW(self,columns:tuple,where:dict,concatenator:str='or',asing = '=')->list:
        newColumns = self._prepareColumns(columns)
        newWhere = self._prepareWhere(where,concatenator,asing=asing)
        resultConsole:list = self._execute(f"select {newColumns} from `{self.tableName}` where {newWhere}")
        return resultConsole
    
    def selectCWLike(self,columns:tuple,where:dict,concatenator:str='or')->list:
        newColumns = self._prepareColumns(columns)
        newWhere = self._prepareWhere(where,concatenator,asing=' LIKE ',isLike = True)
        resultConsole:list = self._execute(f"select {newColumns} from `{self.tableName}` where {newWhere}")
        return resultConsole
    
    #TODO TERMINA ESTO DESPUÉS.
        #TODO si eres alguien que esta leyendo eso y no se termino terminalo y te querré mas <3
    def selectCS(self,columns:tuple|list,sqlCode:str)->list:
        newColumns = self._prepareColumns(columns)
        resultConsole:list = self._execute(f'select {newColumns} from {self.tableName} {sqlCode}')
        return resultConsole
    
    def update(self,set:dict,where:dict,concatenator:str ='or')->bool:
        try:
            new_set = self._prepareWhere(set,concatenator)
            new_where = self._prepareWhere(where)
            # print(f'update {self.tableName} set {new_set} where {new_where};')
            self.__execute(f'update {self.tableName} set {new_set} where {new_where};')

            return True
        except Exception as e:
            return (False,e)
        
    def delete(self,where:dict,concatenator:str = "and")->bool:
        try:
            new_where = self._prepareWhere(where,concatenator)
            self._execute(f'delete from `{self.tableName}` where {new_where};')
            return True
        
        except Exception as e:
            print(e)
            return False

    # Métodos database
    def _execute(self,sqlCode:str=None)->list:
        #! ejecuta consultas SQL y retorna el resultado.
        self.__cursor.execute(sqlCode)
        fetchall:list = self.__cursor.fetchall()
        self.__connection.commit()
        return fetchall
    
    def __execute(self,sqlCode:str = None)->None:
        #! ejecuta consultas SQL y NO retorna el resultado.
        if not sqlCode == None:
            self.__cursor.execute(sqlCode)

    def _close(self)->None:
        self.__connection.close()
    
    # Métodos de la clase Table(relacionado, no son abstractos).
    def updateTable(self) -> None:
        # actualiza la tabla actual (Matriz representativa) la tabla simulada.
        self.clearRegisters(self.atributos)
        self.addRegister(self.selectAll())

    def createDataBase(self,name:str)->None:
        self.__execute(f'create database if not exists `{name}`;')
        
    def createTable(self,tableName:str,propertys:tuple|list,len_str:int = 500)->None:
        """
        @param tableName: name of the table \n
        @param propertys: ('name property',type,modificador)\n
        @param len_str: length of the strings in the table.
        """
        self.tableName = tableName
        sqlCode = f"create table if not exists `{self.tableName}` (\n"

        for property in propertys:
            sqlCode += f"`{property[0]}` "

            #! arregla esto, usa un diccionario...
            if property[1] == int:
                sqlCode += f" int "
            elif property[1] == str:

                if 'comentario' in property[0]:
                    sqlCode += f' varchar(5500) CHARACTER SET utf8 '
                else:
                    sqlCode += f' varchar({len_str}) CHARACTER SET utf8 '

            elif property[1] == float:
                sqlCode += ' float '

            sqlCode += f"{property[2]},\n"

        sqlCode = sqlCode.removesuffix(',\n')
        sqlCode += "\n);"
        self.__execute(sqlCode)

KEY = ' PRIMARY KEY '
NOT_NULL = ' not null '
INCREMENT = " auto_increment "

if __name__ == "__main__":
    db = Database(_user = "root",
    _password = "sergiomolla160",_host="localhost")
    columnas = (
        ('ID',int,KEY),
        ('precio',str,NOT_NULL),
        ('fecha',str,NOT_NULL)
    )
    # db.setDB('usuarios')
    # db.setTable("datos_usuario")

    # print(db.insertVForC(("Nombre" , "Puntos"),'sergio el bailador2',102))

    # //print(db.select())
    
    # //print(db.insert("Morquecho2",105,"morq0il@.com"))
    # //db.select()
    # //print(db.select())
    # //db._printTable(db.select())
    # //db.insertCV("Nombre,Puntos","Juan",480)
    # //db.printTable()
    #// print(db.updateTable())
    # db.updateTable()
    # db._printTable()
    

    
    # where = {
    #     'puntos':22,
    #     'nombre':'Ernesto'
    # }
    # set0 = {
    #     "correo":'cambios extraños que hay en mi'
    # }
    # uwu = (db.selectAllW(where,OR))
    # for i in uwu:
    #     print(i)

    # a = db.update(set0,where)
    # print(a)
    # db.updateTable()
    # db._printTable()

    # e = db.delete(where)
    # print(e)
    # db.updateTable()
    # db._printTable()

    db.createDataBase('prueba juanito')
    db.setDB('prueba juanito')
    db.createTable("tabla juenito",columnas)

    db._close()