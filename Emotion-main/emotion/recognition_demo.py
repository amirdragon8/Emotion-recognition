import cv2
import glob
from deepface import DeepFace

images = [cv2.imread(file) for file in glob.glob("./faces/*.jpg")]

result = []

for img in images:
    result.append(DeepFace.analyze(img, actions=['emotion'], enforce_detection=False))

for i in range(len(result)):
    print(result[i])