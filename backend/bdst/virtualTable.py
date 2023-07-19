# DATE: 16/01/22
# V = 1.0


# DATE: 4/4/23
# V = 1.5
class Table:
    def __init__(self,columns:tuple|list=[None,None,None]) -> None:
        ## se declara la matriz que simula una tabla de una BD.
        self._table:list = [columns]
        self.atributos:tuple = ()


    def setColumns(self,columns:list|tuple)->None:
        ## se establece el nombre de las propiedades de la tabla simulada.
        self._table[0] = columns

    def getTable(self)->list:
        ## se retorna la tabla simulada.
        return self._table
        
    def getPropertys(self)->tuple:
        ## retorna las propiedades de la tabla simulada.
        return self._table[0]

    def addRegister(self,register:list|tuple)->None:
        """
        Este método agrega registros a la tabla simulada.
        ! si hay mas de un elemento en la lista o tupla se intuye \n que cada elemento es un registro a insertar en la tabla simulada.
        """ 
        if len(register) == 1:
            self._table.append(register)
        else:
            for row in register:
                self._table.append(row)
    
    def clearRegisters(self,columns:tuple)->list:
        ## este método limpia la tabla simulada y la retorna.
        del self._table
        self._table:list = [columns]
        return self._table

    def updateTable(self)->None:
        # ! este es un método abstracto pero sin serlo, sera implementado en la clase de base de datos.
        pass

    def getTable(self)->list:
        #Retorna la tabla te lo juro:>
        return self._table

    def printTable(self)->None:
        ## imprime toda la tabla registro por registro.
        for row in self._table:
            print(row)

    def _printTable(self,typeSelect:callable = None)->list:
        """
        Imprime la matriz que representa la tabla, para tener la matriz
        actualizaba se hace una petición select a la tabla, el tipo de petición
        se puede especificar pasando su método en el parámetro TypeSelect()
        """
        if typeSelect != None:
            print(self.atributos)
            try:
                rows = typeSelect()
            except:
                rows = typeSelect
        else:
            rows = self._table

        for row in rows:
            print(row)

    def _prepareValues(self,values:list|tuple=None)->str:
        """
        Este método recibe una lista o tuple la cual se convertirá en
        la misma lista pero dentro de un String, en resultado es el sig.

        ! return "'texto',18,18.50,False,'otroTexto'"
        """
        tempValues = values
        values = ''
        for word in tempValues:
            if word != "False" and word != "True":
                if not (isinstance(word,int) or isinstance(word,float)):
                    values += f'"{word}"'+','
                else:
                    values+= f'{word}'+','
                values += '\n'

        return values.removesuffix(',\n').removesuffix("'")
    
    def _prepareColumns(self,values:tuple|list)->str:
        finalColumns = str()
        for value in values:
            finalColumns += f'`{value}`,'

        return finalColumns.removesuffix(',')

    def _prepareWhere(self,values:dict = None,concatenator:str = 'or',asing:str = ' = ',isLike:bool = False)->str:
        newWhere = ""
        for key in values:
            if values[key] != "False" and values[key] != "True":
                if isLike:
                    pre = '%'
                    suff = '%'
                else:
                    pre = ''
                    suff = ''

                if not (isinstance(values[key],int) or isinstance(values[key],float)):
                    newWhere += f' `{key}` {asing} "{pre}{values[key]}{suff}" '+f' {concatenator} ' 
                else:
                    newWhere += f' `{key}` {asing} {pre}{values[key]}{suff} '+f' {concatenator} '

        return newWhere.removesuffix(f' {concatenator} ')

