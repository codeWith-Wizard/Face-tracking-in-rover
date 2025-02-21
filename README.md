# 🚀 **Face-Tracking Buggy**
### ⏳ 12-Hour Challenge: AI-Powered Face-Following Robot

## 🎯 **Project Overview**
This project aims to build an AI-powered **face-tracking buggy** using **OpenCV, ESP32, and ESP-NOW**. The buggy follows a user’s face in real-time by processing video from a **desktop camera**, generating movement commands, and wirelessly sending them to the buggy via **ESP-NOW**.

## 🛠️ **Core Components**

### 1️⃣ **Face Tracking (OpenCV & Python)** 🎥
- Captures live video from a **desktop webcam**.
- Uses **OpenCV** for **face detection & tracking**.
- Determines face position to generate movement commands (`Left`, `Right`, `Forward`, `Backward`, `Stop`).
- Sends movement commands to **ESP32 via Serial**.

### 2️⃣ **Wireless Command Transmission (ESP-NOW & ESP32)** 📡
- ESP32 (Connected to PC) receives serial commands.
- Transmits commands wirelessly using **ESP-NOW** to the ESP32 on the buggy.

### 3️⃣ **Buggy Control (ESP32 & Motor Driver)** 🚗💨
- ESP32 on the buggy receives movement commands.
- Controls the **motor driver (L298N)** to drive the motors accordingly.

## 🚀 **Features**
✅ **AI-powered real-time face tracking** 🎭
✅ **Wireless command transmission using ESP-NOW** 📡
✅ **Smooth motor control for fluid movement** ⚙️
✅ **Scalable for hand tracking, gesture control, and object following** 🤖
✅ **Low-latency control & response** ⏳

---

## 🏗️ **Project Architecture**
```
[Webcam (PC)] 🎥 → (Face Detection) → [Movement Command] → (Serial) → [ESP32 (PC)] → (ESP-NOW) → [ESP32 (Buggy)] → (Motor Driver) → [Motors] 🚗
```

## 📦 **Required Hardware**
- 🎥 **Desktop/Laptop Camera** (for face tracking)
- 📡 **ESP32 (x2)** (for wireless control)
- ⚡ **L298N Motor Driver**
- 🔋 **Battery Pack (Li-Ion or LiPo)**
- 🛞 **2 or 4-Wheel Drive Buggy Chassis**
- 🎮 **Additional: Ultrasonic sensor for obstacle avoidance** (optional)

## 🔧 **Software Requirements**
- 🐍 **Python** (for OpenCV face tracking)
- 🔧 **Arduino IDE** (for ESP32 programming)
- 📦 **Libraries:**
  - `opencv-python`
  - `mediapipe`
  - `pyserial`
  - `espnow` (for ESP32)

## 📜 **How It Works**
1️⃣ **Face Tracking with OpenCV** 📷
   - Detects the face and determines its position.
   - Generates a movement command (`L`, `R`, `F`, `B`, `S`).
   
2️⃣ **Sending Commands to ESP32** 🔄
   - Transmits the command via **Serial Communication**.
   
3️⃣ **Wireless Transmission with ESP-NOW** 📡
   - ESP32 (PC) sends movement command to ESP32 (Buggy).
   
4️⃣ **Buggy Movement Control** 🚗
   - ESP32 (Buggy) receives the command and controls **L298N Motor Driver**.

---

## 🏎️ **Running the Project**
### **1️⃣ Set Up Face Tracking on PC**
```sh
python face_tracking.py
```
### **2️⃣ Upload ESP32 Code**
- Flash `esp32_transmitter.ino` to ESP32 (PC side).
- Flash `esp32_receiver.ino` to ESP32 (Buggy side).

### **3️⃣ Power Up the Buggy & Start Moving!**
🚀 Your buggy should now follow your face in real-time! 🎥🔄🚗

## 🔮 **Future Enhancements**
✨ Implement **gesture recognition** for advanced controls ✋
✨ Add **obstacle avoidance** using **ultrasonic sensors** 🚧
✨ Use **Raspberry Pi with a camera** for onboard tracking 🎭
✨ Improve **motion smoothness with PID control** ⚙️

---

## 📜 **License**
🔓 This project is open-source under the **MIT License**.

📌 **12-HOUR CHALLENGE** 🏆 LET'S BUILD IT! 🚀🔥

