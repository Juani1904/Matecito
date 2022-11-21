import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import cv2
import math as m

#Importamos el modulo donde hacemos la definicion de clase Imagen
from imagen import Imagen


class Database():


    #Definimos constructor
    
    def __init__(self):

        #--------------------------BASE DE DATOS-----------------------------------
        print("ARANDELAS")
        #ARANDELAS
        cargaArandelas=["base_de_datos/arandela1.jpg","base_de_datos/arandela2.jpg","base_de_datos/arandela3.jpg","base_de_datos/arandela4.jpg","base_de_datos/arandela5.jpg"]
        arandelaimg=[]
        self.arandela=[]
        for nombre in cargaArandelas:
            i=cargaArandelas.index(nombre)
            arandelaimg.append(cv2.imread(nombre))
            self.arandela.append(Imagen(nombre))
            arandelaimg[i]=(cv2.resize(arandelaimg[i],(512,512)))
            cv2.drawContours(arandelaimg[i],self.arandela[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Arandela",arandelaimg[i])
            cv2.waitKey(0)
            cv2.imshow("ArandelaTrazo",self.arandela[i].imagen)
            cv2.waitKey(0)
            print(self.arandela[i].caractVector)
            cv2.destroyAllWindows()

        print("CLAVOS")
        #CLAVOS
        cargaClavos=["base_de_datos/clavo1.jpg","base_de_datos/clavo2.jpg","base_de_datos/clavo3.jpg","base_de_datos/clavo4.jpg","base_de_datos/clavo5.jpg"]
        clavoimg=[]
        self.clavo=[]
        for nombre in cargaClavos:
            i=cargaClavos.index(nombre)
            clavoimg.append(cv2.imread(nombre))
            self.clavo.append(Imagen(nombre))
            clavoimg[i]=(cv2.resize(clavoimg[i],(512,512)))
            cv2.drawContours(clavoimg[i],self.clavo[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Clavo",clavoimg[i])
            cv2.waitKey(0)
            cv2.imshow("ClavoTrazo",self.clavo[i].imagen)
            cv2.waitKey(0)
            print(self.clavo[i].caractVector)
            cv2.destroyAllWindows()

        print("TORNILLOS")
        #TORNILLOS
        cargaTornillos=["base_de_datos/tornillo1.jpg","base_de_datos/tornillo2.jpg","base_de_datos/tornillo3.jpg","base_de_datos/tornillo4.jpg","base_de_datos/tornillo5.jpg"]
        tornilloimg=[]
        self.tornillo=[]
        for nombre in cargaTornillos:
            i=cargaTornillos.index(nombre)
            tornilloimg.append(cv2.imread(nombre))
            self.tornillo.append(Imagen(nombre))
            tornilloimg[i]=(cv2.resize(tornilloimg[i],(512,512)))
            cv2.drawContours(tornilloimg[i],self.tornillo[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Tornillo",tornilloimg[i])
            cv2.waitKey(0)
            cv2.imshow("TornilloTrazo",self.tornillo[i].imagen)
            cv2.waitKey(0)
            print(self.tornillo[i].caractVector)
            cv2.destroyAllWindows()

        print("TUERCAS")
        #TUERCAS
        cargaTuercas=["base_de_datos/tuerca1.jpg","base_de_datos/tuerca2.jpg","base_de_datos/tuerca3.jpg","base_de_datos/tuerca4.jpg","base_de_datos/tuerca5.jpg"]
        tuercaimg=[]
        self.tuerca=[]
        for nombre in cargaTuercas:
            i=cargaTuercas.index(nombre)
            tuercaimg.append(cv2.imread(nombre))
            self.tuerca.append(Imagen(nombre))
            tuercaimg[i]=(cv2.resize(tuercaimg[i],(512,512)))
            cv2.drawContours(tuercaimg[i],self.tuerca[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Tuerca",tuercaimg[i])
            cv2.waitKey(0)
            cv2.imshow("TuercaTrazo",self.tuerca[i].imagen)
            cv2.waitKey(0)
            print(self.tuerca[i].caractVector)
            cv2.destroyAllWindows()

        #--------------------------FIN BASE DE DATOS-----------------------------------
