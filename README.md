# Detección de Manos y Reproducción de Sonidos

Este proyecto utiliza la cámara web para detectar las manos y reproducir sonidos diferentes según los dedos que se levanten. Está desarrollado en Python utilizando las librerías OpenCV, MediaPipe y Pygame.

## Requisitos
- Python 3.x
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- Pygame (`pip install pygame`)

## Funcionamiento

1. **Detección de Manos**:
   - Utiliza MediaPipe para detectar las manos a través de la cámara web.
   - Dibuja los puntos de referencia y las conexiones entre ellos en la imagen capturada.

2. **Detección de Dedos**:
   - Compara la posición vertical (eje Y) de las puntas de los dedos con sus nudillos correspondientes.
   - Si la punta del dedo está por debajo del nudillo, se considera que el dedo está "levantado".

3. **Reproducción de Sonidos**:
   - Cada dedo levantado reproduce un sonido diferente.
   - Los sonidos están mapeados de la siguiente manera:
     - Índice izquierdo: fa.WAV
     - Medio izquierdo: la.WAV
     - Anular izquierdo: re.WAV
     - Índice derecho: do.WAV
     - Medio derecho: sol.WAV
     - Anular derecho: si.WAV

4. **Control de la Aplicación**:
   - Presiona la tecla `ESC` para salir del programa.

## Ejecución

1. Coloca los archivos de audio en la carpeta `sonidos`.
2. Ejecuta el script principal:
   ```bash
   python final_count.py
   ```
3. Coloca tus manos frente a la cámara y flexiona los dedos para escuchar los sonidos.

## Notas
- Asegúrate de que la cámara web esté conectada y funcione correctamente.
- Los archivos de audio deben estar en formato WAV y tener los nombres correctos.
- El programa está configurado para detectar hasta dos manos simultáneamente.
