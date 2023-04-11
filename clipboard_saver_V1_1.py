"""
Clipboard Saver V1.1
By Steve Shambles, Upadated April 2023
Windows only. Tested on Windows 7, 64bit.

Requirements:
cs2.ico (supplied) in current dir.
If not found then default sytem icon is used.

pip3 install infi.systray
pip3 install keyboard
pip3 install Pillow
pip3 install pyautogui
pip3 install pyperclip

* Menu seperator bar fix:
copy the supplied file 'win32_adapter.py' and overwrite the old one
in you python directory + \Lib\site-packages\infi\systray.
If you don'y you will just see some dashes in the systray menu rather
than proper seperator bars, its up to you I guess.
"""
from datetime import datetime
import os
import time
import tkinter as tk
from tkinter import messagebox
import webbrowser as web
import winsound

from infi.systray import SysTrayIcon as stray
import keyboard
from PIL import ImageGrab
import pyautogui
import pyperclip


root = tk.Tk()
root.withdraw()

#  Check required folders exist in current dir If not then create them.
img_folder = 'clipboard_images'
check_img_folder = os.path.isdir(img_folder)
if not check_img_folder:
    os.makedirs(img_folder)

txt_folder = 'clipboard_texts'
check_txt_folder = os.path.isdir(txt_folder)
if not check_txt_folder:
    os.makedirs(txt_folder)

# Put copy of screen on clipboard. This solves a small bug
# where if the first thing you do is click save screen an error occurs.
pyautogui.press('printscreen')


def beep_sound(stray):
    """Beep sound. frequency, duration."""
    winsound.Beep(840, 100)


def clear_cb(stray):
    """Clear the clipboard and then make a beep sound to alert the user."""
    pyperclip.copy('')
    beep_sound(stray)


def save_cb_txt(stray):
    """If text found on clipboard, Save to uniquely named text file."""
    # Grab clipboard contents.
    cb_txt = pyperclip.paste()

    if cb_txt:
        undr_ln = '-' * 43 + '\n'
        # Properly readable date and time as a unique file name.
        time_stamp = (datetime.now().strftime
                      (r'%d' + ('-') + '%b' + ('-') +
                      '%Y' + ('-') + '%H' + ('.')
                       + '%M' + ('-') + '%S' + 's'))
        file_name = time_stamp+'.txt'
        folder = r'clipboard_texts/'

        with open(folder+str(file_name), 'w') as contents:
            contents.write('Clipboard text found: '+str(time_stamp)+'\n')
            contents.write(undr_ln)
            contents.write(cb_txt)
            beep_sound(stray)


def save_cb_img(stray):
    """If image found, Save to uniquely named jpg file."""
    img = ImageGrab.grabclipboard()

    if img:
        img_file_name = (datetime.now().strftime
                         (r'%d' + ('-') + '%b' + ('-') + '%Y' +
                         ('-') + '%H' + ('.') +
                         '%M' + ('-') + '%S' + 's')) + '.jpg'

        cb_img_folder = r'clipboard_images/'
        img.save(cb_img_folder+img_file_name)
        beep_sound(stray)


def save_curr_screen(stray):
    """Save current screen by auto pressing PrtScn key."""
    pyautogui.press('printscreen')
    save_cb_img(stray)


def burst_save(x):
    """Saves x amount of screenshots with 1 second gap.
       Hold down Esc key for 2 secs to cancel burst if required."""
    for _burst in range(x):
        pyautogui.press('printscreen')
        save_cb_img(stray)

        if keyboard.is_pressed('Escape'):
            return
        time.sleep(1)


def save_clipb(stray):
    """When Save clipboard is selected call the two check
       and save functions."""
    save_cb_img(stray)
    save_cb_txt(stray)
    # Pause is to make sure cannot save more than once a second
    # or might interfere with unique filenames.
    time.sleep(1)


def view_clipb(stray):
    """View either text or image from clipboard using
       systems default viewers."""
    # Check for image on cb.
    img = ImageGrab.grabclipboard()

    if img:
        img.save('temp.jpg')
        web.open('temp.jpg')
        return

    # Is it text on cb?
    cb_txt = ''
    cb_txt = pyperclip.paste()
    if cb_txt:
        with open('temp.txt', 'w') as contents:
            contents.write(cb_txt)
        web.open('temp.txt')


def exit_prg(stray):
    """When quit is clicked,
       thread should close and icon in systray destroyed."""
    pass


def open_folder(stray):
    """Get current dir and open systems file browser to view contents."""
    cwd = os.getcwd()
    web.open(cwd)


def donate_me(stray):
    """Open PayPal donation page -expectantly, LOL."""
    web.open('https://paypal.me/photocolourizer')


def github(stray):
    """Visit my GitHub page for lots of source code."""
    web.open('https://github.com/Steve-Shambles?tab=repositories')


def cb_help(stray):
    """Popup box describing how to use the program."""
    web.open('cb_help.txt')


def about_cbsaver(stray):
    """About program pop up."""
    messagebox.showinfo('About This Program',
                        '\nCB Saver V1.1\n'
                        'Freeware by Steve Shambles April 2023.\n\n'
                        'CB Saver is a clipboard manager\n'
                        'written in Python.\n\n'
                        'Source code available on GitHub.\n\n'
                        'If you find this program useful\n'
                        'please consider making a small donation.\n\n')


def fake(stray):
    """Required for seperator bars in systray menu."""
    pass


hover_text = 'Clipboard Saver V1.1'

# Replace None with "your.ico" to use icons in the menus if you want.
# Although they will look pretty bad.
menu_options = (('Save clipboard', None, save_clipb),
                ('-----', None, fake),
                ('Burst Save', None, (('Burst Save  5x1secs', None, lambda x: burst_save(5)),
                                      ('Burst Save 10x1secs', None, lambda x: burst_save(10)),
                                      ('Burst Save 30x1secs', None, lambda x: burst_save(30)),
                                      ('Burst Save 60x1secs', None, lambda x: burst_save(60)),)),
                ('-----', None, fake),
                ('Clear clipboard', None, clear_cb),
                ('View Clipboard', None, view_clipb),
                ('-----', None, fake),
                ('Save current screen', None, save_curr_screen),
                ('-----', None, fake),
                ('Open containing folder', None, open_folder),
                ('-----', None, fake),
                ('Options', None, (('Help', None, cb_help),
                                   ('About', None, about_cbsaver),
                                   ('Make a small donation to author', None, donate_me),
                                   ('Source code on GitHub', None, github),))
                )

# Main program icon that will appear in systray.
# If not found system default icon used.
stray = stray('cs2.ico',
              hover_text, menu_options, on_quit=exit_prg,
              default_menu_index=0)

stray.start()

root.mainloop()
