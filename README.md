# Clipboard-Saver
Windows only sys tray clipboard manager that handles text and images.

Clipboard Saver V1.1 

Freeware by Steve Shambles March 2021 - Updated April 2023 (I took a 2 year break from programming).

![Alt Text](https://github.com/Steve-Shambles/Clipboard-Saver/blob/main/cbsaverV1_1_screenshot.png)

CB Saver (or Clipboard Saver. I still can't decide!) is a little system tray (or taskbar) app that gives you a bit more control over your Windows (7) clipboard.

For example If you want to save the contents of your clipboard at any time simply double-click the CB Saver icon in the taskbar, if  the clipbaord contains text it will be saved in a folder called "clipboard_texts", if it is an image it will be saved in "clipboard_images", you can instantly access these folders by right-clicking the CB Saver icon and selecting the "Open containg folder" item.


Use the right click menu options to click on "Save Clipboard" to save the current contents of the clipboard. Text and images are automatically supported. This can also be achieved by double clicking on the Clipboard Saver icon. If found, either Text or an image will be saved to the relevant folder. A beep will sound if something is saved.

Selecting the "Save current screen" option will take a screenshot of your current screen and save it to the "clipboard_images" folder. A beep will confirm if saved.

If you click "Clear clipboard" a beep will sound to confirm the action.

Selecting "View Clipboard" will display either an image or text using your systems default viewer programs, assuming something is found.

You can view your saved data by clicking on the "Containing folder" menu item and looking in the "clipboard_text" and "clipboard_images" folders.

If you want to create a series of screenshots then select "Burst Save" and from the sub-menu how many screenshots you want to take, from 5 to 60. A screenshot will be snapped of your current screen every second and saved to the "Clipboard Images" folder. You can abort a burst any time by holding down the escape key for 2 seconds.

Python programmers:
---------------------
If you ran my source code without the edited file you would just see ugly dashes as menu seperators. if you want decent seperators then follow these steps:

Navigate to your python folder and then \Lib\site-packages\infi\systray, or do a file search for “win32_adaptor.py” and replace it with this one, 

https://www.mediafire.com/file/wmqtouz04wl1jc0/win32_adapter.py/file

which I have uploaded to MediaFire. I have also put it in on Pastebin, as a backup. https://pastebin.com/i9L6iUwd

They are still there after 2 years so I'm hopeful they will remain for years to come I have also enclosed the file in the github repo.

Steve Shambles April 2023
