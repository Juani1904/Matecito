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
            cv2.imshow("Original",self.arandela[i].imagenOrig)
            cv2.imshow("FiltroPB",self.arandela[i].imagenfiltroPB)
            cv2.imshow("FiltroPA",self.arandela[i].imagenfiltroPA)
            cv2.imshow("Binarizada",self.arandela[i].imagen)
            cv2.drawContours(arandelaimg[i],self.arandela[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Contornos",arandelaimg[i])
            cv2.waitKey(0)
            fig = plt.figure("Img Dom Frecuencial",figsize=(4, 4))
            plt.imshow(np.log(np.abs(self.arandela[i].domFrec)),cmap='gray')
            plt.show()
            plt.close()
            print(self.arandela[i].caractVector)
            

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
            cv2.imshow("Original",self.clavo[i].imagenOrig)
            cv2.imshow("FiltroPB",self.clavo[i].imagenfiltroPB)
            cv2.imshow("FiltroPA",self.clavo[i].imagenfiltroPA)
            cv2.imshow("Binarizada",self.clavo[i].imagen)
            cv2.drawContours(clavoimg[i],self.clavo[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Contornos",clavoimg[i])
            cv2.waitKey(0)
            fig = plt.figure("Img Dom Frecuencial",figsize=(4, 4))
            plt.imshow(np.log(np.abs(self.arandela[i].domFrec)),cmap='gray')
            plt.show()
            plt.close()
            print(self.clavo[i].caractVector)

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
            cv2.imshow("Original",self.tornillo[i].imagenOrig)
            cv2.imshow("FiltroPB",self.tornillo[i].imagenfiltroPB)
            cv2.imshow("FiltroPA",self.tornillo[i].imagenfiltroPA)
            cv2.imshow("Binarizada",self.tornillo[i].imagen)
            cv2.drawContours(tornilloimg[i],self.tornillo[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Contornos",tornilloimg[i])
            cv2.waitKey(0)
            fig = plt.figure("Img Dom Frecuencial",figsize=(4, 4))
            plt.imshow(np.log(np.abs(self.arandela[i].domFrec)),cmap='gray')
            plt.show()
            plt.close()
            print(self.tornillo[i].caractVector)

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
            cv2.imshow("Original",self.tuerca[i].imagenOrig)
            cv2.imshow("FiltroPB",self.tuerca[i].imagenfiltroPB)
            cv2.imshow("FiltroPA",self.tuerca[i].imagenfiltroPA)
            cv2.imshow("Binarizada",self.tuerca[i].imagen)
            cv2.drawContours(tuercaimg[i],self.tuerca[i].contornos,-1,(0,255,0),2)
            cv2.imshow("Contornos",tuercaimg[i])
            cv2.waitKey(0)
            fig = plt.figure("Img Dom Frecuencial",figsize=(4, 4))
            plt.imshow(np.log(np.abs(self.arandela[i].domFrec)),cmap='gray')
            plt.show()
            plt.close()
            print(self.tuerca[i].caractVector)

        #Finalmente para cerrar todas las imagenes abiertas
        cv2.destroyAllWindows()
        #--------------------------FIN BASE DE DATOS-----------------------------------
