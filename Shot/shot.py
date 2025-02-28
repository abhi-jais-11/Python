import pyautogui

def take_screenshot(output_filename="screenshot.png"):
    """
    Takes a screenshot of the entire screen and saves it to a file.
    
    Parameters:
        output_filename (str): The name of the file to save the screenshot.
                              Default is "screenshot.png".
    """
    # Capture the screenshot
    screenshot = pyautogui.screenshot()
    # Save the screenshot to a file
    screenshot.save(output_filename)
    print(f"Screenshot saved as '{output_filename}'")

# Example usage

take_screenshot("main.png")



'''
How It Works:
pyautogui.screenshot():
Captures the entire screen as an image.

screenshot.save(output_filename):
Saves the captured image to the specified file (e.g., my_screenshot.png).

Default Filename:
If no filename is provided, it defaults to screenshot.png.

'''