from ultralytics import YOLO

def classifier(file_path):
    model = YOLO("yolo_clf.pt")
    classification_result = model(file_path)
   
    
    return classification_result