import cv2
import numpy as np
import os

# Загрузка предобученной модели для детекции лиц и модели для вычисления дескрипторов лиц
face_detector_model = "deploy.prototxt"
face_detector_weights = "res10_300x300_ssd_iter_140000_fp16.caffemodel"
face_recognizer_model = "openface.nn4.small2.v1.t7"


# Функция для загрузки известных лиц
def load_known_faces(known_faces_dir):
    known_faces = []
    known_names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = cv2.imread(os.path.join(known_faces_dir, filename))
            face_encoding = get_face_encoding(image)
            if face_encoding is not None:
                known_faces.append(face_encoding)
                known_names.append(os.path.splitext(filename)[0])
    return known_faces, known_names


# Функция для вычисления дескриптора лица
def get_face_encoding(image):
    # Преобразуем изображение в BLOB
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
    face_detector.setInput(blob)
    detections = face_detector.forward()

    if len(detections) > 0:
        # Предполагаем, что на изображении одно лицо (берем первое обнаруженное)
        i = np.argmax(detections[0, 0, :, 2])
        box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
        (startX, startY, endX, endY) = box.astype("int")

        # Извлекаем лицо
        face = image[startY:endY, startX:endX]
        blob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0), swapRB=True, crop=False)
        face_recognizer.setInput(blob)
        return face_recognizer.forward()

    return None


# Загрузка моделей
face_detector = cv2.dnn.readNetFromCaffe(face_detector_model, face_detector_weights)
face_recognizer = cv2.dnn.readNetFromTorch(face_recognizer_model)


def main():
    # Загрузка известных лиц
    known_faces_dir = 'photo'  # Укажите путь к каталогу с фотографиями
    known_faces, known_names = load_known_faces(known_faces_dir)

    # Открываем подключение к вебкамере (0 - стандартная вебкамера)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Не удалось открыть вебкамеру")
        return

    while True:
        # Читаем кадр с вебкамеры
        ret, frame = cap.read()

        if not ret:
            print("Не удалось получить кадр")
            break

        # Преобразуем кадр в BLOB
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))
        face_detector.setInput(blob)
        detections = face_detector.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                # Координаты рамки лица
                box = detections[0, 0, i, 3:7] * np.array(
                    [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (startX, startY, endX, endY) = box.astype("int")

                # Извлекаем лицо и вычисляем дескриптор
                face = frame[startY:endY, startX:endX]
                face_encoding = get_face_encoding(face)

                if face_encoding is not None:
                    # Сравниваем каждое лицо с известными лицами
                    matches = []
                    for known_face in known_faces:
                        matches.append(np.linalg.norm(known_face - face_encoding))

                    name = "Unknown"
                    if matches:
                        min_distance = min(matches)
                        if min_distance < 0.6:  # Порог для распознавания
                            name = known_names[matches.index(min_distance)]

                    # Обводим обнаруженные лица зелеными квадратами
                    cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                    # Подписываем имя под квадратом
                    cv2.putText(frame, name, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Отображаем кадр в окне
        cv2.imshow('Webcam', frame)

        # Проверяем, была ли нажата клавиша 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Освобождаем захват видео и закрываем окна
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
