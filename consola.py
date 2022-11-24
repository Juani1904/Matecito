#En este espacio vamos a programar una consola donde el usuario podra interactuar
#con el programa y aplicar los distintos metodos de segmentacion
from cmd import Cmd
#Importamos el modulo donde hacemos la definicion de la clase Kmeans
from kmeans import Kmeans
#Importamos el modulo donde hacemos la definicion de la clase Knn
from knn import Knn
#Importamos la clase donde se encuentra la base de datos
from database import Database
#Importamos el modulo donde se encuentra la clase Nodo y las funciones para aplicar algoritmo A estrella
#import A_estrella
#Definimos la clase hija Consola, heredada de la clase padre Cmd
class Consola(Cmd):

    intro="Bienvenido a M.A.T.E.C.I.T.O ® by Juani. Tipee help o ? para listar los comandos disponibles"
    prompt="Matecito>>"
    doc_header="Lista de comandos disponibles:"
    Cmd.ruler

    #Definimos el constructor, para instanciar los objetos que utilizaremos en la consola
    def __init__(self):
        Cmd.__init__(self)

    #Definimos los distintos metodos a los cuales podremos accesar desde la consola

    def do_carga_db(self,arg):
        'Carga la base de datos de imagenes al Robot.Tipee CARGA_DB'
        db=Database()
        self.arandela=db.arandela
        self.tuerca=db.tuerca
        self.clavo=db.clavo
        self.tornillo=db.tornillo

    def do_kmeans(self,iteraciones):
        'Aplica el algortimo de segmentacion no supervisada Kmeans, para identificar las imagenes de la carpeta Input. Tipee KMEANS <N de interaciones>'
        #Agregamos una excepcion. Si no se carga la DB no se puede acceder al metodo
        try:
            self.catalog1=Kmeans(self.arandela,self.tuerca,self.clavo,self.tornillo)
            for i in range(int(iteraciones)):
                self.catalog1.Graficador(i)
                self.catalog1.catalogador()
                self.catalog1.recalcularCentroide()
            self.catalog1.guardarImagenes()
        except AttributeError:
            print ("No se ha cargado la base de datos. Intente con CARGA_DB")
        except ValueError:
            print ("No se ha cargado la base de datos. Intente con CARGA_DB")

    def do_knn(self,K):
        'Aplica el algortimo de clasificacion supervisada Knn, para identificar las imagenes de la carpeta Input. Tipee KNN <N de vecinos>'
        try:
            self.catalog2=Knn(self.arandela,self.tuerca,self.clavo,self.tornillo)
            self.catalog2.clasificador(int(K)) #Utilizamos el clasificador con un numero de vecinos igual a K
            self.catalog2.Graficador()
            self.catalog2.guardarImagenes()
        except AttributeError:
            print ("No se ha cargado la base de datos. Intente con CARGA_DB")
        except ValueError:
            print ("No se ha cargado la base de datos. Intente con CARGA_DB")
    """
    def do_a_estrella(self,arg):
        'Aplica el algortimo de busqueda A*. Tipee A_ESTRELLA'
        print("\n#############################################")
        print("Instrucciones:")
        print("1. Ingrese el punto de inicio con click izquierdo")
        print("2. Ingrese el punto de destino con click izquierdo")
        print("3. Ingrese obstaculos con click izquierdo")
        print("4. Si se equivoca, puede borrar con click derecho")
        print("5. Presione ESPACIO para comenzar busqueda")
        print("6. Presione C para restaurar ventana a default")
        print("#############################################\n")
        A_estrella.ejecutaAlgoritmo()
    """    
    def do_exit(self,line):
        'Salir del programa (Apagar Robot)'
        return True
    
    #Metemos un precmd para que las palabras escritas en mayuscula se conviertan en minuscula
    def precmd(self,line):
        return line.lower()
    #Mensaje por defecto cuando ponemos un comando incorrecto
    def default(self):
        print("Comando no reconocido. Ingrese help <comando> para ver su sintaxis")
    #Mensaje por defecto cuando le damos enter sin escribir nada primero
    def emptyline(self):
        pass
    
        
            