# Background Remeover App

A real-time background removal tool using OpenCV and SelfiSegmentation from the cvzone library. This application captures video from the webcam and allows users to remove the background and replace it with custom images.

## Features

* Real-time video capture and background removal.
* Switch between multiple background images with keyboard input.
* Displays FPS (Frames Per Second) on the video feed.
* Simple controls for navigating through background images.

## Requirements

* Python 3.x
* OpenCV (opencv-python)
* NumPy
* cvzone (SelfiSegmentation module)

You can install the required dependencies using the following command:

```bash
pip install opencv-python numpy cvzone
```

## How to Use

1. Clone this repository:

```python
git clone https://github.com/your-username/your-repo-name.git
```
2. Nevigate to the project directory:
```bash
cd your-repo-name
```
3. Run the background_remover.py file:
```bash
python background_remover.py
```

4. Controls:
* Press (**d**) to switch to the next background image.
* Press (**a**) to switch to the previous background image.
* Press (**p**) to quit the application.

## Example Usage

* **Real-time Background Removal:** The app captures live video from your webcam, detects the subject, and replaces the background with a selected image.


## Contributing

Real-time Background Removal: The app captures live video from your webcam, detects the subject, and replaces the background with a selected image.
