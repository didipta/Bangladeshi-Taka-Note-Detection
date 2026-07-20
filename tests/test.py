from ultralytics import YOLO

model = YOLO("models/best.pt")

results = model("sample_images/test (1).jpg")

for result in results:
    for box in result.boxes:
        print("Class:", model.names[int(box.cls)])
        print("Confidence:", float(box.conf))
        print("Bounding Box:", box.xyxy.tolist())