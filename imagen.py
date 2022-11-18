import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import cv2
import math as m

#Definimos la clase Imagen

class Imagen:
    #La idea es tener un solo atributo imagen, y que ese atributo se vaya modificando segun lo que le vayamos
    #haciendo a la imagen
    imagen=None
    contornos=None
    sigmaPB=0.1
    sigmaPA=0.001
    #Creamos el constructor de la clase Imagen
    def __init__(self,miimagen):

        self.imagen=cv2.imread(miimagen)
        #Una vez obtenida la imagen, la redimensionamos a 512x512px
        self.imagen=cv2.resize(self.imagen,(512,512))
        #Pasamos la imagen a escala de grises
        self.imagen=cv2.cvtColor(self.imagen,cv2.COLOR_RGB2GRAY)
        #Establecemos el tipo de dato de intensidad como float
        self.imagen=np.float64(self.imagen)
        #Aplicamos el preprocesamiento
        self.preProcesamiento()
        #Creamos un manejo de excepcion para solucionar el error ZeroDivision
        while(True):
            try:
                #Aplicamos filtro pasa bajo para eliminar el ruido
                self.aplicarFiltro("PB")
                #Luego aplicamos el filtro para alto para resaltar los bordes
                self.aplicarFiltro("PA")
                #Aplicamos la binarizacion a la imagen
                #self.imagen=cv2.Canny(self.imagen,10,150)
                _, self.imagen = cv2.threshold(self.imagen, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
                #Aplicamos el metodo de busqueda de contornos
                self.findContornos()
                #Creamos el vector de caracteristicas
                self.getCaractVector()
                break
            except ZeroDivisionError:
                self.sigmaPB-=0.01
                self.sigmaPA+=0.001
                continue
        
        
    def preProcesamiento(self):
        #Aca vamos a aplicar funciones de dilaracion y erosion para mejorar algunos aspectos de la imagen
        #Estos aspectos a mejorar me van a permitir que el algoritmo identifique bien y cierre los perimetros de las figuras
        #De esta manera me aseguro que las figuran tengan perimetros cerrados y no haya error en la toma de puntos de contorno
        #Aplicamos erode y dilate
        self.imagen=cv2.erode(self.imagen,np.ones((3,3),np.uint8),iterations=1)
        self.imagen=cv2.dilate(self.imagen,np.ones((3,3),np.uint8),iterations=1)

    def aplicarFiltro(self,tipo):
        F1=np.arange(-256,256,1)
        F2=np.arange(-256,256,1)
        [X,Y]=np.meshgrid(F1,F2)
        R=np.sqrt(X**2+Y**2)
        R=R/np.max(R)
        #Aca es donde cambia segun el tipo de filtro que elijamos
        if tipo=="PB":
            FiltroH = np.exp(-(R**2)/(2*self.sigmaPB**2))

        elif tipo=="PA":
            FiltroH = 1-np.exp(-(R**2)/(2*self.sigmaPA**2))

        #Modificamos el origen de coordenadas de la funcion. El cero pasa del centro a los extremos
        FiltroHmod=np.fft.fftshift(FiltroH)
        #Aplicamos transformada de Fourier 2D a la imagen
        Fimg = np.fft.fft2(self.imagen)
        #Generamos producto de filtro con imagen (CONVOLUCION)
        FimgFiltro = Fimg*FiltroHmod
        #Aplicamos la transformada inversa de Fourier 2D
        imgFiltrada = np.fft.ifft2(FimgFiltro)
        #Normalizamos la imagen
        imagenFiltradaN = cv2.normalize(abs(imgFiltrada), None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_8U)
        #Finalmente modificamos el atributo imagen
        self.imagen=imagenFiltradaN
    
    def findContornos(self):
        #Aca se va a implementar el algoritmo de deteccion de contornos

        #Buscamos los puntos de contorno
        self.contornos,_=cv2.findContours(self.imagen,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        #Buscamos los puntos de contorno que me llevan al casco convexo
        self.contornos = sorted(self.contornos,key=cv2.contourArea,reverse=True)[:1]
        # Defectos convexos
        hull = cv2.convexHull(self.contornos[0],returnPoints=False)
        self.defectosConvex = cv2.convexityDefects(self.contornos[0],hull)


    def getCaractVector(self):
        #Creamos el vector de caracteristicas
        self.caractVector=[]
        #Llenamos el vector de caracteristicas con las distintas caract. geometricas
        areafig=cv2.contourArea(self.contornos[0])
        perimetrofig=cv2.arcLength(self.contornos[0],True)
        
        #Calculamos la circularidad
        #Mientras mas cerca de uno la circularidad, mas se parece a un circulo perfecto
        circularidad=(4*(m.pi)*areafig)/(perimetrofig)**2
        self.caractVector.append(circularidad)

        
        #Calculamos la elasticidad
        #La elasticidad es lo mismo que el aspect ratio (width(ancho)/length(altura))
        #Utilizamos boundingRect
        #Si es 1 es un cuadrado perfecto, may a 1 estirado horizontal, menor a 1, estirado vertical
        _,_,ancho,alto=cv2.boundingRect(self.contornos[0])
        elasticidad=float(ancho)/alto
        self.caractVector.append(elasticidad)

        #Realizamos una aprox polinomial que nos servira de parametro
        #Lo que vamos a hacer es sumar al vect. de caracteristicas la cantidad de elementos de approxPoly
        #Este numero de elementos corresponde a los "vertices de la figura"
        #Esto es especialmente util para diferencial la arandela de la tuerca

        epsilon=0.05*cv2.arcLength(self.contornos[0],True)
        approxPoly=cv2.approxPolyDP(self.contornos[0],epsilon,True)
        self.caractVector.append(len(approxPoly))

        #Obtenemos el 3 momento de hu de la imagen
        #huMoments=cv2.HuMoments(cv2.moments(self.contornos[0]))
        #self.caractVector.append(huMoments[2][0])

        


#Fin de deficion de clase















