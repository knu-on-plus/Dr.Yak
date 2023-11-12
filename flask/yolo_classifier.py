from ultralytics import YOLO
import torch
def classifier(file_path):
    model = YOLO("yolo_clf.pt")
    classification_result = model(file_path)

    rounded_probabilities = (classification_result[0].probs.data.numpy()).round(2)
    # return classification_result[0].probs.data.round(2)
    return rounded_probabilities
if __name__ == "__main__":
    a = classifier("static/uploads/uploaded_image.png")
    print(a)


