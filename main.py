
#Importamos el modulo donde se encuentra la clase Database, que crea la base de datos
from database import Database
#Importamos el modulo donde se encuentra la clase consola
from consola import Consola

if __name__ == "__main__":


    #Instanciamos el objeto consola, donde manejaremos todo
    consola=Consola()

    #Llamamos al cmdloop
    consola.cmdloop()







