import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import cv2
import math as m

#Importamos el modulo donde hacemos la definicion de clase Imagen
from imagen import Imagen
#Importamos el modulo donde hacemos la definicion de la clase Kmeans
from kmeans import Kmeans
#Importamos el modulo donde hacemos la definicion de la clase Knn
from knn import Knn
#Cargamos las imagenes de la base de datos
#--------------------------BASE DE DATOS-----------------------------------
print("ARANDELAS")
#ARANDELAS
cargaArandelas=["base_de_datos/arandela1.jpg","base_de_datos/arandela2.jpg","base_de_datos/arandela3.jpg","base_de_datos/arandela4.jpg","base_de_datos/arandela5.jpg"]
arandelaimg=[]
arandela=[]
for nombre in cargaArandelas:
    i=cargaArandelas.index(nombre)
    arandelaimg.append(cv2.imread(nombre))
    arandela.append(Imagen(nombre))
    arandelaimg[i]=(cv2.resize(arandelaimg[i],(512,512)))
    #cv2.drawContours(arandelaimg[i],arandela[i].contornos,-1,(0,255,0),2)
    #cv2.imshow("Arandela",arandelaimg[i])
    #cv2.waitKey(0)
    #cv2.imshow("ArandelaTrazo",arandela[i].imagen)
    #cv2.waitKey(0)
    print(arandela[i].caractVector)
    #cv2.destroyAllWindows()

print("CLAVOS")
#CLAVOS
cargaClavos=["base_de_datos/clavo1.jpg","base_de_datos/clavo2.jpg","base_de_datos/clavo3.jpg","base_de_datos/clavo4.jpg","base_de_datos/clavo5.jpg"]
clavoimg=[]
clavo=[]
for nombre in cargaClavos:
    i=cargaClavos.index(nombre)
    clavoimg.append(cv2.imread(nombre))
    clavo.append(Imagen(nombre))
    clavoimg[i]=(cv2.resize(clavoimg[i],(512,512)))
    #cv2.drawContours(clavoimg[i],clavo[i].contornos,-1,(0,255,0),2)
    #cv2.imshow("Clavo",clavoimg[i])
    #cv2.waitKey(0)
    #cv2.imshow("ClavoTrazo",clavo[i].imagen)
    #cv2.waitKey(0)
    print(clavo[i].caractVector)
    #cv2.destroyAllWindows()

print("TORNILLOS")
#TORNILLOS
cargaTornillos=["base_de_datos/tornillo1.jpg","base_de_datos/tornillo2.jpg","base_de_datos/tornillo3.jpg","base_de_datos/tornillo4.jpg","base_de_datos/tornillo5.jpg"]
tornilloimg=[]
tornillo=[]
for nombre in cargaTornillos:
    i=cargaTornillos.index(nombre)
    tornilloimg.append(cv2.imread(nombre))
    tornillo.append(Imagen(nombre))
    tornilloimg[i]=(cv2.resize(tornilloimg[i],(512,512)))
    #cv2.drawContours(tornilloimg[i],tornillo[i].contornos,-1,(0,255,0),2)
    #cv2.imshow("Tornillo",tornilloimg[i])
    #cv2.waitKey(0)
    #cv2.imshow("TornilloTrazo",tornillo[i].imagen)
    #cv2.waitKey(0)
    print(tornillo[i].caractVector)
    #cv2.destroyAllWindows()

print("TUERCAS")
#TUERCAS
cargaTuercas=["base_de_datos/tuerca1.jpg","base_de_datos/tuerca2.jpg","base_de_datos/tuerca3.jpg","base_de_datos/tuerca4.jpg","base_de_datos/tuerca5.jpg"]
tuercaimg=[]
tuerca=[]
for nombre in cargaTuercas:
    i=cargaTuercas.index(nombre)
    tuercaimg.append(cv2.imread(nombre))
    tuerca.append(Imagen(nombre))
    tuercaimg[i]=(cv2.resize(tuercaimg[i],(512,512)))
    #cv2.drawContours(tuercaimg[i],tuerca[i].contornos,-1,(0,255,0),2)
    #cv2.imshow("Tuerca",tuercaimg[i])
    #cv2.waitKey(0)
    #cv2.imshow("TuercaTrazo",tuerca[i].imagen)
    #cv2.waitKey(0)
    print(tuerca[i].caractVector)
    #cv2.destroyAllWindows()

#--------------------------FIN BASE DE DATOS-----------------------------------

#Implementamos el algoritmo Kmeans para realizar la segmentacion de la imagen
catalog1=Kmeans(arandela,tuerca,clavo,tornillo)
for i in range(20):
    catalog1.catalogador()
    catalog1.recalcularCentroide()
    
catalog1.guardarImagenes()
#Graficamos los puntos de la DB y los de las imagenes desconocidas
catalog1.Graficador()

#Implementamos el algoritmo Knn para realizar la clasificacion de la imagen
catalog2=Knn(arandela,tuerca,clavo,tornillo)
catalog2.clasificador(2) #Utilizamos el clasificador con un numero de vecinos igual a K=2
catalog2.guardarImagenes()



"""
#Ahora graficamos los valores en 3D, a un costado figuran los nombres y color de las piezas
#--------------------------GRAFICACION-----------------------------------
#Graficamos las arandelas
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(arandela)):
    ax.scatter(arandela[i].caractVector[0],arandela[i].caractVector[1],arandela[i].caractVector[2],c='r',marker='o')
    ax.text(arandela[i].caractVector[0],arandela[i].caractVector[1],arandela[i].caractVector[2],  '%s' % (str(cargaArandelas[i])), size=5, zorder=1, color='k')
#Graficamos los clavos
for i in range(len(clavo)):
    ax.scatter(clavo[i].caractVector[0],clavo[i].caractVector[1],clavo[i].caractVector[2],c='b',marker='o')
    ax.text(clavo[i].caractVector[0],clavo[i].caractVector[1],clavo[i].caractVector[2],  '%s' % (str(cargaClavos[i])), size=5, zorder=1, color='k')
#Graficamos los tornillos
for i in range(len(tornillo)):
    ax.scatter(tornillo[i].caractVector[0],tornillo[i].caractVector[1],tornillo[i].caractVector[2],c='g',marker='o')
    ax.text(tornillo[i].caractVector[0],tornillo[i].caractVector[1],tornillo[i].caractVector[2],  '%s' % (str(cargaTornillos[i])), size=5, zorder=1, color='k')
#Graficamos las tuercas
for i in range(len(tuerca)):
    ax.scatter(tuerca[i].caractVector[0],tuerca[i].caractVector[1],tuerca[i].caractVector[2],c='y',marker='o')
    ax.text(tuerca[i].caractVector[0],tuerca[i].caractVector[1],tuerca[i].caractVector[2],  '%s' % (str(cargaTuercas[i])), size=5, zorder=1, color='k')

#Graficamos las imagenes desconocidas
for i in range(len(catalog.imagenes)):
    ax.scatter(catalog.imagenes[i].caractVector[0],catalog.imagenes[i].caractVector[1],catalog.imagenes[i].caractVector[2],c='k',marker='o')
    ax.text(catalog.imagenes[i].caractVector[0],catalog.imagenes[i].caractVector[1],catalog.imagenes[i].caractVector[2],  '%s' % (str("imagen")), size=5, zorder=1, color='k')

ax.set_xlabel('Elasticidad')
ax.set_ylabel('AproxPoly')
ax.set_zlabel('1er Momento Hu')
plt.show()
#--------------------------FIN GRAFICACION-----------------------------------

"""