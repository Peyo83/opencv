import cv2

captura = cv2.VideoCapture('video.avi')

if captura.isOpened() == False:
    print('Error al abrir el fichero')
    
while captura.isOpened():
    
    resultado, video = captura.read()
    
    if resultado == True:
        
        cv2.imshow('Mi video', video)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    else:
        break
        
captura.release()
cv2.destroyAllWindows()