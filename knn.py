import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import cv2
import math as m
import os
from imagen import Imagen
from random import randint
from mpl_toolkits.mplot3d import Axes3D

#Ahora vamos a definir la clase Knn

class Knn:


    #Definimos el constructor
    def __init__(self,miarandela,mituerca,miclavo,mitornillo):
        #Incluimos los objetos creados en el main, para poder comunicarnos con ellos
        self.arandelas=miarandela
        self.tuercas=mituerca
        self.clavos=miclavo
        self.tornillos=mitornillo
        #Ahora instanciamos las imagenes desconocidas de la carpeta input
        #Inicializamos el vector de imagenes
        self.imagenes=[]
        for filename in os.listdir("Input"):
            self.imagenes.append(Imagen("Input/"+filename))
            ind=os.listdir("Input").index(filename)
            mostrarimg=self.imagenes[ind].imagenOrig
            cv2.drawContours(mostrarimg,self.imagenes[ind].contornos,-1,(0,255,0),2)
            cv2.imshow(filename,mostrarimg)
            cv2.waitKey(0)
            cv2.imshow("Trazo "+str(filename),self.imagenes[ind].imagen)
            cv2.waitKey(0)
            print("Imagen "+str(ind+1))
            print(self.imagenes[ind].caractVector)
            cv2.destroyAllWindows()
        
        #Definimos el vector de etiquetas. Como este algoritmo es supervisado, el prellenado
        #de los valores de etiqueta no sera "Desconocido", si no con el nombre de la pieza de la base de datos
        self.etiquetas=[]

        for i in range(5):
            self.etiquetas.append("Arandela")
        for i in range(5):
            self.etiquetas.append("Tuerca")
        for i in range(5):
            self.etiquetas.append("Clavo")
        for i in range(5):
            self.etiquetas.append("Tornillo")
        

    def clasificador(self,K):
        #Definimos el numero de vecinos
        self.K=K
        #Definimos los vectores de distancias
        #Los definimos como variables locales y no como atributos porque solo los usaremos aca
        distimg1=[]
        distimg2=[]
        distimg3=[]
        distimg4=[]
        #Definimos los vectores respuesta donde se almacenara el resultado del contraste entre el vector de distancias
        #y el vector de etiquetas.
        respimg1=[]
        respimg2=[]
        respimg3=[]
        respimg4=[]
        #Ahora calculamos las distancias de cada imagen a cada una de las imagenes de la base de datos
        #Primero para la imagen 1
        for i in range(5):
            distimg1.append(m.sqrt((self.imagenes[0].caractVector[0]-self.arandelas[i].caractVector[0])**2+(self.imagenes[0].caractVector[1]-self.arandelas[i].caractVector[1])**2+(self.imagenes[0].caractVector[2]-self.arandelas[i].caractVector[2])**2))
        for i in range(5):
            distimg1.append(m.sqrt((self.imagenes[0].caractVector[0]-self.tuercas[i].caractVector[0])**2+(self.imagenes[0].caractVector[1]-self.tuercas[i].caractVector[1])**2+(self.imagenes[0].caractVector[2]-self.tuercas[i].caractVector[2])**2))
        for i in range(5):
            distimg1.append(m.sqrt((self.imagenes[0].caractVector[0]-self.clavos[i].caractVector[0])**2+(self.imagenes[0].caractVector[1]-self.clavos[i].caractVector[1])**2+(self.imagenes[0].caractVector[2]-self.clavos[i].caractVector[2])**2))
        for i in range(5):
            distimg1.append(m.sqrt((self.imagenes[0].caractVector[0]-self.tornillos[i].caractVector[0])**2+(self.imagenes[0].caractVector[1]-self.tornillos[i].caractVector[1])**2+(self.imagenes[0].caractVector[2]-self.tornillos[i].caractVector[2])**2))
        #Ahora para la imagen 2
        for i in range(5):
            distimg2.append(m.sqrt((self.imagenes[1].caractVector[0]-self.arandelas[i].caractVector[0])**2+(self.imagenes[1].caractVector[1]-self.arandelas[i].caractVector[1])**2+(self.imagenes[1].caractVector[2]-self.arandelas[i].caractVector[2])**2))
        for i in range(5):
            distimg2.append(m.sqrt((self.imagenes[1].caractVector[0]-self.tuercas[i].caractVector[0])**2+(self.imagenes[1].caractVector[1]-self.tuercas[i].caractVector[1])**2+(self.imagenes[1].caractVector[2]-self.tuercas[i].caractVector[2])**2))
        for i in range(5):
            distimg2.append(m.sqrt((self.imagenes[1].caractVector[0]-self.clavos[i].caractVector[0])**2+(self.imagenes[1].caractVector[1]-self.clavos[i].caractVector[1])**2+(self.imagenes[1].caractVector[2]-self.clavos[i].caractVector[2])**2))
        for i in range(5):
            distimg2.append(m.sqrt((self.imagenes[1].caractVector[0]-self.tornillos[i].caractVector[0])**2+(self.imagenes[1].caractVector[1]-self.tornillos[i].caractVector[1])**2+(self.imagenes[1].caractVector[2]-self.tornillos[i].caractVector[2])**2))
        #Ahora para la imagen 3
        for i in range(5):
            distimg3.append(m.sqrt((self.imagenes[2].caractVector[0]-self.arandelas[i].caractVector[0])**2+(self.imagenes[2].caractVector[1]-self.arandelas[i].caractVector[1])**2+(self.imagenes[2].caractVector[2]-self.arandelas[i].caractVector[2])**2))
        for i in range(5):
            distimg3.append(m.sqrt((self.imagenes[2].caractVector[0]-self.tuercas[i].caractVector[0])**2+(self.imagenes[2].caractVector[1]-self.tuercas[i].caractVector[1])**2+(self.imagenes[2].caractVector[2]-self.tuercas[i].caractVector[2])**2))
        for i in range(5):
            distimg3.append(m.sqrt((self.imagenes[2].caractVector[0]-self.clavos[i].caractVector[0])**2+(self.imagenes[2].caractVector[1]-self.clavos[i].caractVector[1])**2+(self.imagenes[2].caractVector[2]-self.clavos[i].caractVector[2])**2))
        for i in range(5):
            distimg3.append(m.sqrt((self.imagenes[2].caractVector[0]-self.tornillos[i].caractVector[0])**2+(self.imagenes[2].caractVector[1]-self.tornillos[i].caractVector[1])**2+(self.imagenes[2].caractVector[2]-self.tornillos[i].caractVector[2])**2))
        #Ahora para la imagen 4
        for i in range(5):
            distimg4.append(m.sqrt((self.imagenes[3].caractVector[0]-self.arandelas[i].caractVector[0])**2+(self.imagenes[3].caractVector[1]-self.arandelas[i].caractVector[1])**2+(self.imagenes[3].caractVector[2]-self.arandelas[i].caractVector[2])**2))
        for i in range(5):
            distimg4.append(m.sqrt((self.imagenes[3].caractVector[0]-self.tuercas[i].caractVector[0])**2+(self.imagenes[3].caractVector[1]-self.tuercas[i].caractVector[1])**2+(self.imagenes[3].caractVector[2]-self.tuercas[i].caractVector[2])**2))
        for i in range(5):
            distimg4.append(m.sqrt((self.imagenes[3].caractVector[0]-self.clavos[i].caractVector[0])**2+(self.imagenes[3].caractVector[1]-self.clavos[i].caractVector[1])**2+(self.imagenes[3].caractVector[2]-self.clavos[i].caractVector[2])**2))
        for i in range(5):
            distimg4.append(m.sqrt((self.imagenes[3].caractVector[0]-self.tornillos[i].caractVector[0])**2+(self.imagenes[3].caractVector[1]-self.tornillos[i].caractVector[1])**2+(self.imagenes[3].caractVector[2]-self.tornillos[i].caractVector[2])**2))

        #Ahora vemos el index de las K minimas distancias y las comparamos con las
        #los elementos con ese mismo index en el vector de etiquetas
        
        for contador in range(K):
            #Para la imagen 1
            for distancia in distimg1:
                if distancia == min(distimg1):
                    index = distimg1.index(distancia)
                    respimg1.append(self.etiquetas[index])
            #Para la imagen 2
            for distancia in distimg2:
                if distancia == min(distimg2):
                    index = distimg2.index(distancia)
                    respimg2.append(self.etiquetas[index])
            #Para la imagen 3
            for distancia in distimg3:
                if distancia == min(distimg3):
                    index = distimg3.index(distancia)
                    respimg3.append(self.etiquetas[index])
            #Para la imagen 4
            for distancia in distimg4:
                if distancia == min(distimg4):
                    index = distimg4.index(distancia)
                    respimg4.append(self.etiquetas[index])

            #Ahora actualizamos en minimo de cada imagen por 1000 (numero grande), para, en el caso que
            #K>1 podamos tomar los K-1 valores minimos restantes
            distimg1[distimg1.index(min(distimg1))] = 1000
            distimg2[distimg2.index(min(distimg2))] = 1000
            distimg3[distimg3.index(min(distimg3))] = 1000
            distimg4[distimg4.index(min(distimg4))] = 1000

        #Para graficar las esferas creamos el siguiente vector
        #Cuando salgamos de la funcion clasificador, los valores del vector corresponderan
        #a los radios de las esferas, que seran las distancias al vecino mas lejano de los K considerados
        self.distEsferas=[min(distimg1),min(distimg2),min(distimg3),min(distimg4)]

        #Ahora vemos cuantas veces aparece cada elemento en las respuestas
        #Las cantidades las almacenamos en diccionarios cuyo nombre clave es el de cada pieza
        #Y el valor es la cantidad de veces que aparece
        piezas1 = {"Arandela":0,"Tuerca":0,"Clavo":0,"Tornillo":0}
        piezas2 = {"Arandela":0,"Tuerca":0,"Clavo":0,"Tornillo":0}
        piezas3 = {"Arandela":0,"Tuerca":0,"Clavo":0,"Tornillo":0}
        piezas4 = {"Arandela":0,"Tuerca":0,"Clavo":0,"Tornillo":0}
        for pieza in respimg1:
            if pieza == "Arandela":
                piezas1["Arandela"] += 1
            elif pieza == "Tuerca":
                piezas1["Tuerca"] += 1
            elif pieza == "Clavo":
                piezas1["Clavo"] += 1
            elif pieza == "Tornillo":
                piezas1["Tornillo"] += 1
        for pieza in respimg2:
            if pieza == "Arandela":
                piezas2["Arandela"] += 1
            elif pieza == "Tuerca":
                piezas2["Tuerca"] += 1
            elif pieza == "Clavo":
                piezas2["Clavo"] += 1
            elif pieza == "Tornillo":
                piezas2["Tornillo"] += 1
        for pieza in respimg3:
            if pieza == "Arandela":
                piezas3["Arandela"] += 1
            elif pieza == "Tuerca":
                piezas3["Tuerca"] += 1
            elif pieza == "Clavo":
                piezas3["Clavo"] += 1
            elif pieza == "Tornillo":
                piezas3["Tornillo"] += 1
        for pieza in respimg4:
            if pieza == "Arandela":
                piezas4["Arandela"] += 1
            elif pieza == "Tuerca":
                piezas4["Tuerca"] += 1
            elif pieza == "Clavo":
                piezas4["Clavo"] += 1
            elif pieza == "Tornillo":
                piezas4["Tornillo"] += 1
        
        self.piezas=[]
        self.piezas.append(piezas1)
        self.piezas.append(piezas2)
        self.piezas.append(piezas3)
        self.piezas.append(piezas4)
        

    def guardarImagenes(self):
        #Ahora vemos para cada imagen cual es el valor que mas se repite en el diccionario
        #y guardamos la imagen en la carpeta output con el nombre de la clave que mas se repite

        #Primero borramos los archivos que pudieran haber en la carpeta output
        for archivo in os.listdir("Output/Knn/"):
            os.remove("Output/Knn/"+archivo)
        #Ahora guardamos las imagenes
        for imagen in self.imagenes:
            i=self.imagenes.index(imagen)
            if self.piezas[i]["Arandela"] > self.piezas[i]["Tuerca"] and self.piezas[i]["Arandela"] > self.piezas[i]["Clavo"] and self.piezas[i]["Arandela"] > self.piezas[i]["Tornillo"]:
                cv2.imwrite("Output/Knn/"+str(i+1)+".Arandela.jpg",imagen.imagenOrig)
            
            elif self.piezas[i]["Tuerca"] > self.piezas[i]["Arandela"] and self.piezas[i]["Tuerca"] > self.piezas[i]["Clavo"] and self.piezas[i]["Tuerca"] > self.piezas[i]["Tornillo"]:
                cv2.imwrite("Output/Knn/"+str(i+1)+".Tuerca.jpg",imagen.imagenOrig)
            
            elif self.piezas[i]["Clavo"] > self.piezas[i]["Arandela"] and self.piezas[i]["Clavo"] > self.piezas[i]["Tuerca"] and self.piezas[i]["Clavo"] > self.piezas[i]["Tornillo"]:
                cv2.imwrite("Output/Knn/"+str(i+1)+".Clavo.jpg",imagen.imagenOrig)
            
            elif self.piezas[i]["Tornillo"] > self.piezas[i]["Arandela"] and self.piezas[i]["Tornillo"] > self.piezas[i]["Tuerca"] and self.piezas[i]["Tornillo"] > self.piezas[i]["Clavo"]:
                cv2.imwrite("Output/Knn/"+str(i+1)+".Tornillo.jpg",imagen.imagenOrig)
            
            else:
                print("Imagen "+str(i+1)+": Clasificacion indefinida para este numero de vecinos")
                print("Intentando nuevamente con K="+str(self.K+1))
                self.clasificador(self.K+1)
                self.guardarImagenes()
                #cv2.imwrite("Output/Knn/"+str(i+1)+".Desconocido.jpg",imagen.imagenOrig)
        
        print("Imagenes guardadas en la carpeta Output/Knn")
    
    def Graficador(self):
        #En este metodo graficaremos los puntos de cada pieza con distintos colores
        #Tambien graficaremos los puntos que queremos conocer
        #Y finalmente una esfera desde el punto que queremos conocer, con radio igual la distancia a los K vecinos
        #Para esto usaremos la libreria matplotlib
        #Primero graficaremos los puntos de cada pieza
        fig = plt.figure("Grafica Knn")
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('Elasticidad')
        ax.set_ylabel('AproxPoly')
        ax.set_zlabel('1er Momento Hu')
        ax.set_title("Grafica Knn")
        for i in range(len(self.arandelas)):
            ax.scatter(self.arandelas[i].caractVector[0],self.arandelas[i].caractVector[1],self.arandelas[i].caractVector[2],c='red',marker='o')
        #Graficamos los clavos
        for i in range(len(self.clavos)):
            ax.scatter(self.clavos[i].caractVector[0],self.clavos[i].caractVector[1],self.clavos[i].caractVector[2],c='blue',marker='o')
        #Graficamos los tornillos
        for i in range(len(self.tornillos)):
            ax.scatter(self.tornillos[i].caractVector[0],self.tornillos[i].caractVector[1],self.tornillos[i].caractVector[2],c='green',marker='o')
        #Graficamos las tuercas
        for i in range(len(self.tuercas)):
            ax.scatter(self.tuercas[i].caractVector[0],self.tuercas[i].caractVector[1],self.tuercas[i].caractVector[2],c='yellow',marker='o')

        #Graficamos las imagenes desconocidas
        for i in range(len(self.imagenes)):
            ax.scatter(self.imagenes[i].caractVector[0],self.imagenes[i].caractVector[1],self.imagenes[i].caractVector[2],c='k',marker='o')

        #Colocamos una leyenda para clasificar las piezas por su color
        ax.scatter(0,0,0,c='red',marker='o',label='Arandela')
        ax.scatter(0,0,0,c='blue',marker='o',label='Clavo')
        ax.scatter(0,0,0,c='green',marker='o',label='Tornillo')
        ax.scatter(0,0,0,c='yellow',marker='o',label='Tuerca')
        ax.scatter(0,0,0,c='k',marker='o',label='Desconocido')
        ax.legend()
        #Graficamos las esferas (No se nota mucho porque van a ser muy chicas. Hacerle zoom)
        
        for i in range(len(self.piezas)):

            u,v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
            x=np.cos(u)*np.sin(v)
            y=np.sin(u)*np.sin(v)
            z=np.cos(v)
            r=self.distEsferas[i]
            ax.plot_wireframe(x*r+self.imagenes[i].caractVector[0], y*r+self.imagenes[i].caractVector[1], z*r+self.imagenes[i].caractVector[2], color="black")
        plt.show()

        

        
            

                
                            
                        
