from backend.bdst.conexion import Database,INCREMENT,KEY,NOT_NULL

class AdminDatabase(Database):
    def __init__(self, _user: str, _password: str, _host: str,nameDB:str="STR-16",nameTable:str = 'TSS') -> None:
        super().__init__(_user, _password, _host)
        self.__name_db =  nameDB
        self.__name_table = nameTable
        self.EMAIL_PROPERTY = "000"
        self.PASSWORD_PROPERTY = "111"
        self.GROUP_PROPERTY = "222"

        db_ok = self.__init_database()
        if not db_ok:
            raise Exception("Could not initialize database")
        tb_ok = self.__init_table()
        
        if not tb_ok:
            raise Exception("Could not initialize table")
        
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
                self.__name_table,
                (("id",int,f"{KEY} {INCREMENT}"),
                (self.EMAIL_PROPERTY,str,""),
                 (self.PASSWORD_PROPERTY,str,""),
                 (self.GROUP_PROPERTY,str,""),),
                 50
            )
            return True
        except:
            return False
        

    def add_frame(self,email:str,password:str)->None|Exception:
        """
        Add a new frame in the database...
        """
        try:
            result = self.insertV(email,password)
            if not result == True:
                raise Exception("No se pudo hacer la inserción del Frame en la base de datos.")
            
        except Exception as e:
            return e

    def get_frames(self)->list:
        return self.selectC((self.EMAIL_PROPERTY,self.PASSWORD_PROPERTY,self.GROUP_PROPERTY))
    
    def remove_frame(self,email:str,password:str,group:str)->bool:
        return self.delete({self.EMAIL_PROPERTY:email,self.PASSWORD_PROPERTY:password,self.GROUP_PROPERTY:group})
    
torres = AdminDatabase(
    "root",
    "sergiomolla160",
    "localhost"
)

#! relleno para llegar a la linea 60 :]