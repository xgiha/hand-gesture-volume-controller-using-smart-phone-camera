# AI Hand Gesture Volume Controller using Smart Phone Camera

This project uses AI and computer vision to control the system volume based on hand gestures. The program captures hand movements using a smartphone camera and recognizes specific gestures to increase or decrease the volume on your PC.

## Features

- Real-time hand gesture detection using the MediaPipe library.
- Volume control based on the distance between the thumb and index finger.
- Works with a smartphone camera as the input device.

## Requirements

- Python 3.7 or higher
- OpenCV
- MediaPipe
- PyAutoGUI
- PyCaw (for volume control)
- DroidCam app + client (for using phone camera)
- ADB (Android Debug Bridge) for USB connection

## Installation

Follow these steps to set up and run the AI Hand Gesture Volume Controller project:

1. **Clone the Repository**
    ```sh
    git clone https://github.com/your-username/hand-gesture-volume-controller.git
    cd hand-gesture-volume-controller
    ```
   
2. **Install Python and Libraries**
    - Ensure Python 3.7 or higher is installed. You can download it from [Python.org](https://www.python.org/downloads/).
    - Create a virtual environment and activate it (OPTIONAL): 
        ```sh
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```
    - Install the required libraries:
        ```sh
        pip install opencv-python mediapipe pyautogui pycaw
        ```

3. **Set Up ADB (Android Debug Bridge)**
    - Download the Android SDK Platform Tools from the [official site](https://developer.android.com/tools/releases/platform-tools).
    - Extract the downloaded file and note the directory path.
    - Open the Extracted folder then run cmd in the folder path.

4. **Connect Your Phone**
    - Enable Developer Options and USB Debugging on your Android device.
    - Connect your phone to your computer via USB.
    - Then run "adb devices" command and it will show a popup message (if it's your first time) to allow from both pc and your phone. You will see your device if it successfully connected:
        ```sh
        adb devices
        ```
        
5. **Install Droid Cam**
   - Download and install DroidCam on both PC and your Android phone.
   - [official site](https://droidcam.app/).
   - Forward the camera feed port if necessary as it shown in your DroidCam:
        ```sh
        adb forward tcp:4747 localabstract:droidcam
        ```

6. **Run the Project**
    - Ensure your phone is connected and DroidCam is running.
    - Run the Python script:
        ```sh
        main.py
        ```

Now, the AI Hand Gesture Volume Controller should be up and running, allowing you to control the volume using hand gestures detected by your phone's camera.
