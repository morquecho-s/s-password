from backend.bdst.conexion import Database,INCREMENT,KEY

class AdminDatabase(Database):
    def __init__(self, _user: str, _password: str, _host: str,nameDB:str="str-16",nameTable:str = 'tss') -> None:
        super().__init__(_user, _password, _host)
        self.__name_db =  nameDB
        self.tableName = nameTable
        self.ID_PROPERTY = "id"
        self.EMAIL_PROPERTY = "mail"
        self.PASSWORD_PROPERTY = "pass"
        self.GROUP_PROPERTY = "group"

        db_ok = self.__init_database()
        if not db_ok:
            raise Exception("Could not initialize database")
        tb_ok = self.__init_table()
        
        if not tb_ok == True:
            raise Exception(f"Could not initialize table:")
        
    def __init_database(self):
        try:
            self.createDataBase(self.__name_db)
            self.setDB(self.__name_db)
            return True
        except:
            return False
        
    def __init_table(self):
        try:
            self.createTable(
                self.tableName,
                ((self.ID_PROPERTY,int,f"{KEY} {INCREMENT}"),
                (self.EMAIL_PROPERTY,str,""),
                 (self.PASSWORD_PROPERTY,str,""),
                 (self.GROUP_PROPERTY,str,""),),
                 50
            )
            self.setTable(self.tableName)
            return True
        except Exception as e:
            print(e)
            return False
        

    def add_frame(self,email:str,password:str,group:str)->None|Exception:
        """
        Add a new frame in the database...
        """
        try:
            self.setTable(self.tableName)
            columns = (self.EMAIL_PROPERTY,self.PASSWORD_PROPERTY,self.GROUP_PROPERTY)
            result = self.insertVForC(columns,email,password,group)
            if not result == True:
                raise Exception("No se pudo hacer la inserción del Frame en la base de datos.")
            
        except Exception as e:
            return e

    def get_frames(self)->list:
        self.setTable(self.tableName)
        return self.selectC((self.EMAIL_PROPERTY,self.PASSWORD_PROPERTY,self.GROUP_PROPERTY,self.ID_PROPERTY))
    
    def delete_frame(self,email:str,password:str,group:str,id:int = None)->bool:
        self.setTable(self.tableName)
        delete = {self.EMAIL_PROPERTY:email,self.PASSWORD_PROPERTY:password,self.GROUP_PROPERTY:group}
        if not id == None:
            delete[self.ID_PROPERTY] = id
        return self.delete(delete)
    
torres = AdminDatabase(
    "root",
    "sergiomolla160",
    "localhost"
)




#! relleno para llegar a la linea 80 :]