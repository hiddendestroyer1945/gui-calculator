# gui-calculator

gui-calculator is a tactile, hardware-inspired GUI calculator designed for Linux environments. Built with Python 3, it focuses on providing a professional "device-like" user experience with industrial gray-black aesthetics and full keyboard integration.

🚀 Features

* **Tactile UI Design:** Features an embossed (raised) button layout and a sunken data display.
* **Keyboard Synchronized:** Fully controllable via physical keyboard; maps "Enter" to results and "Backspace" to data correction.
* **Linux Native:** Uses the Tkinter engine, ensuring a lightweight footprint without heavy dependencies.
* **Industrial Theme:** Professional gray and black color palette for low-strain usage.

📋 Prerequisites

Before you begin, ensure you have the following installed on your Linux system:

* Python 3
* Git
* python3-tk (The GUI toolkit for Python)

🛠️ Installation & Setup

Follow these steps to get your environment ready and run the program:

1. Update System & Install Dependencies
Open your terminal and run:
```bash
sudo apt update
sudo apt install python3 git python3-tk

    Clone the Repository Clone the project to your local machine:

Bash

git clone <your-repository-link-here>
cd gui-calculator/

    Run the Program Once the environment is ready, execute the script:

Bash

chmod +x calculator.py
python3 calculator.py

💻 Usage & Controls

The program is designed to behave like a physical calculator device. You can use the mouse or your computer keyboard:

    Numbers: Use 0-9 or the Numpad.

    Operators: Use +, -, *, /, and % keys.

    Calculate: Press = or the Enter key to process the expression.

    Delete: Press Backspace to remove the last entered digit.

    Clear: Press the C button or Escape key to wipe all data.

Supported Operations:

    Standard Addition/Subtraction

    Multiplication/Division

    Floating point (decimal) math

    Percentage calculations

    Error handling for invalid math expressions

⚠️ Disclaimer

This tool is a standard mathematical utility. It performs calculations locally on your machine. It does not require internet access and does not collect or transmit any user data, ensuring complete privacy for your financial or technical calculations.