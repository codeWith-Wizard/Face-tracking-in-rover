# 🎯 **Hand Tracking Movement Control using OpenCV & MediaPipe**

## 🌟 **Overview**
This project uses **OpenCV** 🖼️ and **MediaPipe** ✋ to track hand movements and generate movement commands in real-time. The system detects the position of the hand and sends corresponding movement commands (`🅻`, `🆁`, `🅵`, `🅱`, `🆂`) to control a robotic buggy.

## 🚀 **Features**
✅ **Real-time hand tracking** using **MediaPipe** 🎥
✅ **Movement detection** based on hand position:
   - 🏁 **Left (🅻)**: Move left
   - 🏁 **Right (🆁)**: Move right
   - 🏁 **Forward (🅵)**: Move forward
   - 🏁 **Backward (🅱)**: Move backward
   - 🛑 **Stop (🆂)**: Default state
✅ **Serial communication support** (for sending commands to an ESP32) 📡
✅ **Live video feed** with hand landmark visualization 👀

## 🔧 **Dependencies**
Ensure you have the following Python libraries installed:
```sh
pip install opencv-python mediapipe pyserial
```

## 🎥 **How It Works**
1️⃣ Captures live video from the **desktop camera** 📷.
2️⃣ Detects the hand using **MediaPipe Hand Tracking** ✋.
3️⃣ Determines the hand's **wrist position** 🎯.
4️⃣ Compares the hand's position with predefined regions:
   - 📍 **Left of the screen** → Move **Left (🅻)**
   - 📍 **Right of the screen** → Move **Right (🆁)**
   - 📍 **Top of the screen** → Move **Forward (🅵)**
   - 📍 **Bottom of the screen** → Move **Backward (🅱)**
   - 📍 **Center** → **Stop (🆂)**
5️⃣ Displays the movement command on the screen 📺.
6️⃣ Optionally sends movement commands via **Serial** to an ESP32 🛰️.

## ▶️ **Usage**
### 1️⃣ Run the Script
```sh
python hand_tracking.py
```
### 2️⃣ Quit the Program
- Press **'q'** to exit the program ❌.

## 🔗 **Serial Communication (Optional)**
If you want to send movement commands to an **ESP32**:
1️⃣ Connect the ESP32 to your computer via USB 🔌.
2️⃣ Uncomment and modify the following line in the script:
   ```python
   ser = serial.Serial("COM5", 9600)  # Replace COM5 with your port
   ```
3️⃣ Uncomment the command sending line:
   ```python
   ser.write(movement_command.encode())
   ```

## 🎨 **Customization**
🎯 **Adjust Sensitivity**: Modify the threshold values for movement detection.
⚙️ **Modify Commands**: Change the mapping of hand positions to movement commands.
✋ **Use Different Gestures**: Implement gesture-based controls instead of position-based.

## 🔮 **Future Enhancements**
🚀 Implement **gesture recognition** for more advanced controls.
⚡ Improve accuracy with **dynamic hand tracking**.
📡 Integrate with the **ESP-NOW protocol** for wireless buggy control.

## 📜 **License**
This project is **open-source** and free to use for learning and experimentation. 🎓

---
💡 Developed as part of a **6-hour challenge** ⏳ to build an AI-powered face-following buggy. 🚗💨

