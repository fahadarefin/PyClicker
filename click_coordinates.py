from pynput import mouse

def get_click_coordinates():
    # This function will store the coordinates
    coordinates = []

    def on_click(x, y, button, pressed):
        if pressed:
            coordinates.append((x, y))  # Store the coordinates
            return False  # Stop the listener after getting the coordinates

    # Start the mouse listener
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # Return the coordinates captured
    return coordinates[0] if coordinates else None


