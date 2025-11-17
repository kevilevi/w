import win32api
import win32con
import time

def unlock_pc(password):
    # Wait for the lock screen to appear
    time.sleep(5)

    # Send keystrokes to the lock screen
    for char in password:
        vk_code = ord(char)
        win32api.keybd_event(vk_code, 0, 0, 0)
        time.sleep(0.1)
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)  # Send Enter key

# Call the function to unlock the PC
unlock_pc('5555')