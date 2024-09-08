

# PyClicker Automation Tool

## Overview

The **PyClicker Automation Tool** is a Python application that automates mouse clicks at user-specified coordinates. This tool is useful for repetitive tasks where you need to click a button or an area on the screen multiple times with a specified interval.

## Features

- **Capture Coordinates:** Click a button to capture the coordinates where the mouse is currently positioned.
- **Automate Clicking:** Specify the number of clicks and the interval between each click.
- **User-friendly Interface:** Simple and intuitive interface using Tkinter.

## Installation

### Prerequisites

1. **Python 3.x**: Ensure that Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
2. **Required Libraries**: Install the necessary Python libraries using pip:

   ```bash
   pip install pyautogui tkinter
   ```

### Downloading Files

1. **Clone the Repository or Download Files**

   Clone the repository using Git:

   ```bash
   git clone https://github.com/fahadarefin/PyClicker
   ```

   Alternatively, download the repository as a ZIP file from GitHub and extract it.

2. **Locate the Files**

   Ensure you have the following files:

   - `main.py`
   - `pyclicker.exe` (partially tested for Windows 11)

### Running the Application

1. **Using the Python Script**

   Navigate to the directory containing `main.py` and run:

   ```bash
   python main.py
   ```

   This will start the PyClicker GUI.

2. **Using the Executable**

   You can also use the `pyclicker.exe` file. Note that this executable is only partially tested for Windows 11. If you encounter issues, it is recommended to run the Python script instead.

## Usage

1. **Capture Coordinates**

   - Click the "Get Coordinates" button.
   - Move the cursor to the desired position within 2 seconds.
   - Click "OK" in the popup message box to capture the coordinates.

2. **Start Clicking**

   - Enter the number of clicks you want to perform in the "Number of Clicks" field.
   - Enter the interval between each click (in seconds) in the "Interval Between Each Click" field.
   - Click the "Start Clicking" button to begin the automation.

## Error Handling

- If the mouse moves to a corner of the screen, a failsafe exception is triggered.
- Input errors will display an appropriate error message.

## Closing the Application

- Click the close button on the window to exit the application.
- A confirmation dialog will appear asking if you really want to quit.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or fixes. 

## Contact

For any issues or questions, please contact the repository owner via GitHub issues.

