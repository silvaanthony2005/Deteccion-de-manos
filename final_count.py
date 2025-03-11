import cv2
import mediapipe as mp
import pygame

mp_hands = mp.solutions.hands               #trabajar con las manos con la libreria de mediapipe
mp_drawing = mp.solutions.drawing_utils     #Graficacion los puntos de las manos

pygame.mixer.init()                         #iniciar pygame

#sonidos para cada dedo
sonunds = [
    pygame.mixer.Sound('sonidos/#fa.WAV'),  #indice izquierdo 0
    pygame.mixer.Sound('sonidos/la.WAV'),   #medio izquierdo 1
    pygame.mixer.Sound('sonidos/re.WAV'),   #anular izquierdo 2
    pygame.mixer.Sound('sonidos/#do.WAV'),  #indice derecho 3
    pygame.mixer.Sound('sonidos/#sol.WAV'), #indice derecho 4
    pygame.mixer.Sound('sonidos/si.WAV'),   #indice derecho 5
]

# se pasan de la libreria los puntos de la mano y en especial el de las punta de los dedos y el nudillo para hacer comparativas de posicion
def is_finger__down(landmarks, finger_tip, finger_mcp):
    return landmarks[finger_tip].y > landmarks[finger_mcp].y #obtiene la posicion en el eje y de la punta del dedo y la compara con el nudillo

cap = cv2.VideoCapture(0)   #trabajar con la camara conectada a la pc

with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5, 
                    max_num_hands = 2) as hands:
    finger_state = [False]*6

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame,1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for h, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
                finger_tips = [8,12,16]
                finger_mcp = [5,9,13]

                for i in range(3):
                    finger_index = i + h*3
                    if is_finger__down(hand_landmarks.landmark, finger_tips[i], finger_mcp[i]):
                        if not finger_state[finger_index]:
                            sonunds[finger_index].play()
                            finger_state[finger_index] = True
                    else:
                            finger_state[finger_index] = False

        cv2.imshow('hand detection', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()