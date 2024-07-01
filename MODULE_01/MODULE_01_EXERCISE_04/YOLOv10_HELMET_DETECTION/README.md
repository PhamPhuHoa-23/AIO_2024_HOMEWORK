# YOLOv10_HELMET_DETECTION

This repository contains a project for detecting helmets using the YOLOv10 model as part of Module 01 Exercise 04 for the AIO 2024 Homework series.

## What is YOLOv10?

YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system. YOLOv10 is an advanced version designed for better accuracy and efficiency.

## Project Structure

- **yolo/**
  - Contains YOLO code and my trained-model

- **Yolov10_Helmet_Detection.ipynb**
  - This file contain the training process for my last model

## Features

- **Helmet Detection**: Detects helmets in images and videos using the YOLOv10 neural network.
- **Model Training**: Provides scripts to train the YOLOv10 model on custom datasets.
- **Model Evaluation**: Scripts to evaluate the performance of the trained model.

## Installation

To install the required packages, you can use:

```bash
cd yolov10
pip install -r requirements.txt
```

## Usage

To train the model, use the following command

```python
EPOCHS = 50
IMG_SIZE = 640 # 640
BATCH_SIZE = 64 # 256

model.train(data=YAML_PATH,
            epochs=EPOCHS,
            batch=BATCH_SIZE,
            imgsz=IMG_SIZE)
```

To evaluate the model, use the following command:

```python
TRAINED_MODEL_PATH = './best.pt'
model = YOLOv10(TRAINED_MODEL_PATH)

model.val(data=YAML_PATH,
          imgsz=IMG_SIZE,
          split='test')
```

To run helmet-detection, use the following command

```python
IMG_PATH = 'Your_image_path'
model(source=IMG_PATH)[0].save('./images/img.png')
```
