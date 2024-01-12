# Face Recognition with Alert System

## Project Overview

This project focuses on creating a face recognition system with an alert mechanism using Python, OpenCV, and Machine Learning. The system continuously monitors its surroundings through a camera, emphasizing the detection of unenrolled faces. Upon identification of an unauthorized face, the system promptly captures an image and records the timestamp for future reference.

## Features

- **Real-time Face Detection:** The system employs advanced face detection techniques to identify unenrolled faces in real-time.

- **Image Capture:** Once an unauthorized face is detected, the system captures an image swiftly, ensuring a visual record of the incident.

- **Secure Storage:** Captured images and timestamps are securely stored in a database, providing a reliable repository for monitoring and analysis.

- **Proactive Monitoring and Alert Generation:** The system actively monitors for unauthorized access attempts. If a breach is detected, it generates alerts to notify relevant authorities or security personnel.

- **Resource for Analysis and Investigation:** The stored data serves as a valuable resource for in-depth analysis and investigation in the event of security breaches, enabling a proactive response.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vidyasagar1793/Face-recognition-with-warning-system.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. run the training.py:
   - camera starts to capture the images

## Usage

1. Run the main application:
   ```bash
   python main.py

<img src="https://github.com/vidyasagar1793/Face-recognition-with-warning-system/blob/main/image/Screenshot%202023-11-27%20195820.png" height ="400px" width="600px" >
<img src="https://github.com/vidyasagar1793/Face-recognition-with-warning-system/blob/main/image/photo_2023-11-27_19-20-57.jpg" height="400px"  width="600px">
   
   ```

2. Monitor the system through the camera.

3. Receive alerts and review captured images in the database in case of unauthorized access attempts.
