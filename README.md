# 🕰️ Vintage Analog Clock – Computer Graphics Project

A classic analog clock built using Python + Pygame, featuring vintage Roman numerals, old-style colors, smooth clock-hand animation, and real-time date & time display right below the clock hands.


📸 Preview

![Analog Clock Screenshot](screenshot.png)

✨ Features

✔️ Real-time analog clock with hour, minute, and second hands
✔️ Vintage look: Roman numerals, wooden border, parchment-style face
✔️ Smooth second-hand movement
✔️ Date & Time displayed neatly below the hands
✔️ Fully customizable colors, fonts, styles
✔️ Built using Python + Pygame
✔️ Clean and readable source code

🛠️ Technologies Used

Python 3

Pygame (graphics and rendering)

Math & geometry for clock hand rotation

Real-time system clock reading using datetime

📦 Installation
1️⃣ Install Python

Download Python from:
https://www.python.org/downloads/

2️⃣ Install Pygame

Open terminal / CMD:

pip install pygame

3️⃣ Clone the repository
git clone https://github.com/pandey-sundaram/Vintage-Analog-Clock.git
cd Vintage-Analog-Clock

▶️ Running the Clock

Simply run:

python analog_clock.py


The clock window will open automatically.

📂 Project Structure
Vintage-Analog-Clock/
│
├── analog_clock.py       # Main clock program
├── README.md             # Project documentation
└── screenshot.png        # clock preview image

🎨 Customization

You can easily modify:

Clock background colors

Roman numeral fonts

Hand sizes & colors

Date/time formatting

Clock radius & style

Inside the code, look for the CONFIG section:

# CONFIG (OLD VINTAGE STYLE)
WIDTH, HEIGHT = 600, 600
CLOCK_RADIUS = 250
BG_COLOR = (45, 30, 20)
CLOCK_FACE_COLOR = (235, 220, 190)


Change these values to match your desired look.

🧠 How The Clock Works

The clock uses trigonometry (sin, cos) to calculate the hand endpoints

datetime.now() provides real-time system time

Pygame renders shapes at 60 FPS for smooth movement

Roman numerals and tick marks are drawn using loops and calculated angles

📘 Topics Covered

This project demonstrates the following concepts:

Computer Graphics fundamentals

2D rendering

Coordinate geometry

Polar → Cartesian conversion

Animation & frame refresh

Event loops

Real-time applications

🙋 Author

Sundaram Pandey (1/23/SET/BCS/290)
Satyam Mishra (1/23/SET/BCS/285)
Kartik Sharma (1/23/SET/BCS/279)

⭐ Show Your Support

If you found this project useful:
⭐ Give the repository a star on GitHub!
