from datetime import date
from datetime import datetime
import random 
class Alumno:
    
    def __init__(self,Nombre,ApellidoP,ApellidoM,AnioNac,Carrera):
        self.__Nombre = Nombre
        self.__ApellidoPaterno = ApellidoP
        self.__ApellidoMaterno = ApellidoM
        self.__AnioNacimiento = AnioNac
        self.__Carrera = Carrera
        self.__Matricula = ""
     
    def getSiglasNac(self):
        SiglasNAc = ""
        for i in range(2,4):
            SiglasNAc = SiglasNAc+self.__AnioNacimiento[i]
        return SiglasNAc    
         
    def getSiglasCarrera(self):
        SiglasCarrera = ""
        for i in range(0,3):
            SiglasCarrera =SiglasCarrera+ self.__Carrera[i] 
        return SiglasCarrera    
     
    def getAnioAct(self):                
        #AnioEncurso = datetime.year()
        #AnioCurso = date().year()
        AnioCurso = "23"
        return AnioCurso
    
    def getSiglasApellidos(self):
        SiglasApellidos = ""
        for i in range(0,3):
            SiglasApellidos = SiglasApellidos + self.__ApellidoPaterno[i]
        
        for j in range(0,3):
            SiglasApellidos = SiglasApellidos+ self.__ApellidoMaterno[j]    
         
        return SiglasApellidos        
     
    def getNumRandom(self):
        NumAzar = ""
        for i in range(0,3):
            NumAzar=NumAzar+str(random.randint(0,9))        
        return NumAzar    
   
    def getMatricula(self):
        return self.__Matricula                
        
    def generaMatricula(self):    
        SiglasCarrera =self.getSiglasCarrera()
        AnioAct = self.getAnioAct()
        AnioNacimiento = self.getSiglasNac()
        LetraName = self.__Nombre[0]
        LetrasApellidos = self.getSiglasApellidos()
        NumerosAzar = self.getNumRandom()
        Matricula = SiglasCarrera + str(AnioAct)+str(AnioNacimiento)+LetraName+LetrasApellidos+NumerosAzar
        self.__Matricula = Matricula
        

            
            
            
            
        