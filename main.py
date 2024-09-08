import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

# Function to get click coordinates
def get_click_coordinates(root):
    messagebox.showinfo("Instructions", "Click OK, then move the cursor to the desired position within 2 seconds.")
    root.withdraw()  # Hide the root window
    time.sleep(2)  # Give user 2 seconds to move the mouse
    x, y = pyautogui.position()  # Get current mouse position
    root.deiconify()  # Show the root window again
    return x, y

# Function to process clicks
def click_button(number_of_press, sleep_time, x, y):
    try:
        for _ in range(number_of_press):
            pyautogui.moveTo(x, y)  # Move the cursor to the button's coordinates
            pyautogui.click()  # Click the button
            time.sleep(sleep_time)  # Wait for the specified interval
    except pyautogui.FailSafeException:
        messagebox.showerror("Error", "Mouse moved to a corner of the screen (Failsafe triggered).")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to handle the first button click to get coordinates
def on_get_coordinates_click():
    global coordinates
    coordinates = get_click_coordinates(root)
    messagebox.showinfo("Coordinates", f"Coordinates captured: {coordinates}")

# Function to handle the second button click to start clicking
def on_button_click():
    try:
        # Get the integer values from the input fields
        number_of_press = int(entry1.get())
        sleep_time = float(entry2.get())

        if coordinates is None:
            messagebox.showerror("Error", "Please capture the coordinates first.")
        else:
            x, y = coordinates  # Use captured coordinates
            click_button(number_of_press, sleep_time, x, y)

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create the main application window
root = tk.Tk()
root.minsize(400, 250)
root.title("PyClicker")

# Set a custom background color
root.configure(bg="#f0f0f0")

# Define custom fonts and padding
font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)
padding = {'padx': 10, 'pady': 5}

coordinates = None  # Variable to store coordinates

# Create and place the title label
title_label = tk.Label(root, text="PyClicker Automation Tool", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Create and place labels for inputs
label1 = tk.Label(root, text="Number of Clicks:", font=font_label, bg="#f0f0f0")
label1.pack(**padding)

# Create and place input fields
entry1 = tk.Entry(root, font=font_entry)
entry1.pack(**padding)

label2 = tk.Label(root, text="Interval Between Each Click (in seconds):", font=font_label, bg="#f0f0f0")
label2.pack(**padding)

entry2 = tk.Entry(root, font=font_entry)
entry2.pack(**padding)

# Create and place the first button for getting coordinates
button1 = tk.Button(root, text="Get Coordinates", font=font_label, command=on_get_coordinates_click, bg="#4CAF50", fg="white")
button1.pack(**padding)

# Create and place the second button for performing clicks
button2 = tk.Button(root, text="Start Clicking", font=font_label, command=on_button_click, bg="#2196F3", fg="white")
button2.pack(**padding)

# Handle closing the application properly
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the application
root.mainloop()

