# Face Detection using YOLOv8

This repository contains a simple Python script for real-time face detection using the YOLOv8 model from the Ultralytics library. The script utilizes OpenCV for video capture and display.

## Prerequisites

Make sure you have the following dependencies installed:

- [Ultralytics](https://github.com/ultralytics/yolov5): `pip install -U git+https://github.com/ultralytics/yolov5.git`
- [OpenCV](https://pypi.org/project/opencv-python/): `pip install opencv-python`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Run the script:

   ```bash
   python face_detection.py
   ```

   Press 'q' to exit the video feed.

## Explanation

The script does the following:

1. Imports the necessary libraries: `ultralytics`, `cv2`, and `time`.
2. Loads the YOLOv8 face detection model from Ultralytics.
3. Captures video from the default camera (change `cv2.VideoCapture(0)` to use a different camera or video file).
4. Performs face detection on each video frame and calculates the inference time.
5. Draws bounding boxes around detected faces and displays the video feed.
6. If a face is detected, it displays "MATCH!" along with the elapsed time since the first detection.
7. If no face is detected, it resets the timer and displays "NOT FOUND!"

Feel free to modify the code to suit your needs or integrate it into your projects.

## Acknowledgments

- Ultralytics for providing the YOLOv8 model.
- OpenCV for the video capture and display functionalities.
