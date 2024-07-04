# AI Hand Gesture Volume Controller

This project is an AI-based volume controller that uses hand gestures to increase or decrease the system volume. It utilizes the phone's camera to capture hand gestures and processes them using OpenCV and MediaPipe libraries.

## Features

- Recognizes hand gestures using the phone's camera
- Increases volume when thumb and index finger are apart
- Decreases volume when thumb and index finger are close

## Requirements

- Python 3.7 or higher
- OpenCV
- MediaPipe
- PyAutoGUI
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
    - Ensure Python 3.7 or higher is installed. You can download it from [Python.org](https://www.python.org/).
    - Create a virtual environment and activate it:
        ```sh
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```
    - Install the required libraries:
        ```sh
        pip install opencv-python mediapipe pyautogui
        ```

3. **Set Up ADB (Android Debug Bridge)**
    - Download the Android SDK Platform Tools from the [official site](https://developer.android.com/studio/releases/platform-tools).
    - Extract the downloaded file and note the directory path.
    - Add the path to the Platform Tools to your system's environment variables:
        - On Windows, search for "Environment Variables" in the start menu, then add the path to the `Path` variable.
        - On Mac or Linux, add the following line to your `~/.bashrc` or `~/.zshrc` file:
            ```sh
            export PATH=$PATH:/path/to/platform-tools
            ```

4. **Connect Your Phone**
    - Enable Developer Options and USB Debugging on your Android device.
    - Connect your phone to your computer via USB.
    - Verify the connection by running:
        ```sh
        adb devices
        ```
    - Forward the camera feed port:
        ```sh
        adb forward tcp:4747 localabstract:droidcam
        ```

5. **Run the Project**
    - Ensure your phone is connected and DroidCam is running.
    - Run the Python script:
        ```sh
        main.py
        ```

Now, the AI Hand Gesture Volume Controller should be up and running, allowing you to control the volume using hand gestures detected by your phone's camera.
