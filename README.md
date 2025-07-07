# 🎨 RGB At Mouse Coordinates

A lightweight Python utility that prints your mouse’s X/Y position and the pixel’s RGB color in real time. Press **C** to save the current value and **Esc** to exit.

---

## 🧠 About

I needed a quick way to grab exact RGB values at specific screen coordinates for an automation script. Since I couldn’t find an existing tool, I built this with Python, PyAutoGUI, and Keyboard.

---

## 🚀 Features

- Continuously displays mouse **X, Y** coordinates and pixel **RGB** color.  
- Press **C** to “save” (print) the current values.  
- Press **Esc** to quit the script.

---

## 🛠️ Technologies

- **Python 3.x**  
- **PyAutoGUI** (for mouse position & pixel color)  
- **keyboard** (for hotkeys)  
- **threading** (for non‑blocking loop)

---

## ⚙️ Installation

1. Clone the repo:  
   ```bash
   git clone https://github.com/MarcusK00/RGBAtMouseCords.git
   cd RGBAtMouseCords
   ```
2. Install Pyautogui
   ```bash
   pip install pyautogui keyboard
   ```
3. Run the script
   ```python
   python rgb_at_mouse.py
   ```
