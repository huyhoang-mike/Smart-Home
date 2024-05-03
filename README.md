# Automatic garage door opening system
## DESCRIPTION
Imagine the current scenario: You’re driving home after a long day, looking forward to the comfort of your own space. As you approach your garage, you face the inconvenience of having to step out of your car to manually open the garage door. Even with a remote, there’s the need to stop and wait until the door is fully open. This interruption, though seemingly minor, can be a source of frustration.
This is where the automatic garage door project comes into play. It’s not just a project; it’s a solution, a way to streamline your daily routine. By integrating a camera into the system, the garage door will be able to detect the number plate as it approaches. Without any need for you to stop or even slow down, the door will open automatically, ready for you to drive in.
## COMPONENTS
Camera: Webcam Dahua Z2+ will be used to capture images in front of the garage. <br>
ESP32 Microcontroller: ESP32 Wroom Dev Kit Module, a powerful and versatile microcontroller with Wi-Fi capabilities, will handle the task of communicating between the deep learning model and the garage door mechanism. <br>
Micro Servo: Simulation of the door. <br>
LED: Simulation of the light bulb. <br>
## INSTALLATION
Use the package manager [pip](https://pypi.org/project/pip/) to install the software.
``` 
pip install -r requirements.txt
```
## USAGE
Firstly, you need to clone this [repository](https://github.com/huyhoang-mike/Smart-Home/) into your local machine.
```
git clone https://github.com/huyhoang-mike/Smart-Home/
```
Secondly, run the webcam.py file below to start the local server.
```
python webcam.py
```
## DEMO
[Click here](https://drive.google.com/file/d/12HEUDEdb2t5QFlPkG16cHs2a_h_oNBji/view?usp=sharing)

