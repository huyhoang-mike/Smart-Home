from ultralytics import YOLO
import os

model_path = os.path.join('.', 'runs', 'detect', 'train7', 'weights', 'best.pt')

# Load a model
model = YOLO(model_path)  # load a pretrained model (recommended for training)

# Use the model
results = model.train(data="config.yaml", epochs=30)  # train the model
