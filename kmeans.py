import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import cv2
import math as m
import os
from imagen import Imagen
from random import randint
import time


class Kmeans:

    #Definimos el constructor
    def __init__(self,miarandela,mituerca,miclavo,mitornillo,K=4):
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
        #Definimos el numero de clusters
        self.K=K
        #Definimos el numero de iteraciones
        self.iteraciones=10
        #Definimos los centroides
        self.randomSelectCentroide()
        #Definimos el vector de etiquetas
        self.etiquetas=[]
        #Definimos el vector de distancias
        self.distancias=[]
        #Llenamos el vector de etiquetas con 24 elementos que digan "desconocido", el de distancias con 0
        #El vector distancia tendra como elemento una lista de 4 elementos porque esas son las distancias de cada elemento a cada uno de los 4 centroides
        for i in range(24):
            self.etiquetas.append("Desconocido")
            self.distancias.append([0,0,0,0])
    
    def randomSelectCentroide(self):
        #Los parametros no son mas que vectores o listas de objetos Imagen
        i1=randint(0,4)
        i2=randint(0,4)
        i3=randint(0,4)
        i4=randint(0,4)
        self.centroide=[self.arandelas[i1].caractVector,self.tuercas[i2].caractVector,self.clavos[i3].caractVector,self.tornillos[i4].caractVector]

        
    def catalogador(self):

        #Calculamos la distancia euclideana de las imagenes a los centroides
        #Primero para las arandelas
        for i in range(5):
            for j in range(4):
                self.distancias[i][j]=m.sqrt((self.arandelas[i].caractVector[0]-self.centroide[j][0])**2+(self.arandelas[i].caractVector[1]-self.centroide[j][1])**2+(self.arandelas[i].caractVector[2]-self.centroide[j][2])**2)
        #Ahora para las tuercas
        for i in range(5):
            for j in range(4):
                self.distancias[i+5][j]=m.sqrt((self.tuercas[i].caractVector[0]-self.centroide[j][0])**2+(self.tuercas[i].caractVector[1]-self.centroide[j][1])**2+(self.tuercas[i].caractVector[2]-self.centroide[j][2])**2)
        #Ahora para los clavos
        for i in range(5):
            for j in range(4):
                self.distancias[i+10][j]=m.sqrt((self.clavos[i].caractVector[0]-self.centroide[j][0])**2+(self.clavos[i].caractVector[1]-self.centroide[j][1])**2+(self.clavos[i].caractVector[2]-self.centroide[j][2])**2)
        #Ahora para los tornillos
        for i in range(5):
            for j in range(4):
                self.distancias[i+15][j]=m.sqrt((self.tornillos[i].caractVector[0]-self.centroide[j][0])**2+(self.tornillos[i].caractVector[1]-self.centroide[j][1])**2+(self.tornillos[i].caractVector[2]-self.centroide[j][2])**2)
        #Ahora para las imagenes desconocidas
        for i in range(4):
            for j in range(4):
                self.distancias[i+20][j]=m.sqrt((self.imagenes[i].caractVector[0]-self.centroide[j][0])**2+(self.imagenes[i].caractVector[1]-self.centroide[j][1])**2+(self.imagenes[i].caractVector[2]-self.centroide[j][2])**2)

        #Ahora asignamos las etiquetas
        for distancias in self.distancias:
            for numero in distancias:
                minimo=distancias.index(min(distancias))
                if minimo==0:
                    self.etiquetas[self.distancias.index(distancias)]="Arandela"
                elif minimo==1:
                    self.etiquetas[self.distancias.index(distancias)]="Tuerca"
                elif minimo==2:
                    self.etiquetas[self.distancias.index(distancias)]="Clavo"
                elif minimo==3:
                    self.etiquetas[self.distancias.index(distancias)]="Tornillo"
    
    #Ahora definimos el metodo para recalcular el centroide mediante la media de los puntos de los clusters formados
    def recalcularCentroide(self):
        #Primero armamos una lista con todos los puntos de todas las imagenes, en el mismo orden que antes
        puntos=[]
        for i in range(5):
            puntos.append(self.arandelas[i].caractVector)
        for i in range(5):
            puntos.append(self.tuercas[i].caractVector)
        for i in range(5):
            puntos.append(self.clavos[i].caractVector)
        for i in range(5):
            puntos.append(self.tornillos[i].caractVector)
        for i in range(4):
            puntos.append(self.imagenes[i].caractVector)
        
        #Ahora calculamos la media aritmetica a lo largo de cada eje
        ejeX=[]
        ejeY=[]
        ejeZ=[]
        for coordenada in puntos:
            X,Y,Z=coordenada
            ejeX.append(X)
            ejeY.append(Y)
            ejeZ.append(Z)

        #Ahora vamos a calcular la media de los datos, segun su clasificacion
        ejeXArandela=[]
        ejeYArandela=[]
        ejeZArandela=[]
        ejeXTuerca=[]
        ejeYTuerca=[]
        ejeZTuerca=[]
        ejeXClavo=[]
        ejeYClavo=[]
        ejeZClavo=[]
        ejeXTornillo=[]
        ejeYTornillo=[]
        ejeZTornillo=[]
        
        for item in self.etiquetas:
            if item=="Arandela":
                ejeXArandela.append(ejeX[self.etiquetas.index(item)])
                ejeYArandela.append(ejeY[self.etiquetas.index(item)])
                ejeZArandela.append(ejeZ[self.etiquetas.index(item)])
            elif item=="Tuerca":
                ejeXTuerca.append(ejeX[self.etiquetas.index(item)])
                ejeYTuerca.append(ejeY[self.etiquetas.index(item)])
                ejeZTuerca.append(ejeZ[self.etiquetas.index(item)])
            elif item=="Clavo":
                ejeXClavo.append(ejeX[self.etiquetas.index(item)])
                ejeYClavo.append(ejeY[self.etiquetas.index(item)])
                ejeZClavo.append(ejeZ[self.etiquetas.index(item)])
            elif item=="Tornillo":
                ejeXTornillo.append(ejeX[self.etiquetas.index(item)])
                ejeYTornillo.append(ejeY[self.etiquetas.index(item)])
                ejeZTornillo.append(ejeZ[self.etiquetas.index(item)])

        #Finalmente, recalculamos el centroide
        self.centroide[0][0]=sum(ejeXArandela)/len(ejeXArandela)
        self.centroide[0][1]=sum(ejeYArandela)/len(ejeYArandela)
        self.centroide[0][2]=sum(ejeZArandela)/len(ejeZArandela)
        self.centroide[1][0]=sum(ejeXTuerca)/len(ejeXTuerca)
        self.centroide[1][1]=sum(ejeYTuerca)/len(ejeYTuerca)
        self.centroide[1][2]=sum(ejeZTuerca)/len(ejeZTuerca)
        self.centroide[2][0]=sum(ejeXClavo)/len(ejeXClavo)
        self.centroide[2][1]=sum(ejeYClavo)/len(ejeYClavo)
        self.centroide[2][2]=sum(ejeZClavo)/len(ejeZClavo)
        self.centroide[3][0]=sum(ejeXTornillo)/len(ejeXTornillo)
        self.centroide[3][1]=sum(ejeYTornillo)/len(ejeYTornillo)
        self.centroide[3][2]=sum(ejeZTornillo)/len(ejeZTornillo)

    
    #Definimos el metodo para guardar las 4 imagenes ahora catalogadas segun su etiqueta, en la carpeta Output, con su nombre particular
    def guardarImagenes(self):
        for imagen in self.imagenes:
            time.sleep(1)
            i=self.imagenes.index(imagen)
            if self.etiquetas[20+i]=="Arandela":
                cv2.imwrite("Output/Kmeans/"+str(i+1)+".Arandela.jpg",imagen.imagen)
            elif self.etiquetas[20+i]=="Tuerca":
                cv2.imwrite("Output/Kmeans/"+str(i+1)+".Tuerca.jpg",imagen.imagen)
            elif self.etiquetas[20+i]=="Clavo":
                cv2.imwrite("Output/Kmeans/"+str(i+1)+".Clavo.jpg",imagen.imagen)
            elif self.etiquetas[20+i]=="Tornillo":
                cv2.imwrite("Output/Kmeans/"+str(i+1)+".Tornillo.jpg",imagen.imagen)
        




        



    



    