import cv2
import numpy as np

# Variables globale
dibujando = False
valorx = 0
valory = 0

# Definir función para dibujar
def dibujar(event, x, y, etiquetas, parametros):
    
    global dibujando, valorx, valory
    
    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando == True
        valorx = x
        valory = y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando == True:
            cv2.rectangle(imagen, (valorx, valory), (x,y), (255,255,0), -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(imagen, (valorx, valory), (x,y), (255,255,0), -1)
        
# Conectarfunción con imagen
cv2.namedWindow(winname='mi_imagen')
cv2.setMouseCallback('mi_imagen', dibujar)

# Mostrar la imagen donde dibujar
imagen = np.zeros(shape=(500,500,3), dtype=np.int8)
    
while True:
    
    cv2.imshow('mi_imagen', imagen)
    
    if cv2.waiyKey(10) & 0xFF ==27:
        break
        
cv2.destroyAllWindows()