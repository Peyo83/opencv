import cv2

captura = cv2.VideoCapture(0)

ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Grabación en MAC
codigo = cv2.VideoWriter_fourcc(*'MJPG')
grabador = cv2.VideoWriter('video.avi', codigo, 20, (ancho, altura))

#Grabación en Windows
#codigo = cv2.VideoWriter_fourcc(*'DIVX')
#grabador = cv2.VideoWriter('video.mp4', codigo, 20, (ancho, altura))
                               

while True:
    
    resultado, video = captura.read()
    
    # Grabar
    grabador.write(video)
    
    cv2.imshow('Nuestro video', video)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
captura.release()
grabador.release()
cv2.destroyAllWindows()