# Key-Logger
The implementation of a keylogger using Python. A keylogger is a type of software or hardware device that is designed to monitor and record all the keystrokes made on a computer or a device. But it can get a lot more than just the keys. **Next version will be self healing and self replicating.**

The code uses the pynput library to capture key presses and releases, and the requests library to upload the collected data to a server. The keylogger has the following functionalities:

**Key Capture:** The code uses the pynput.keyboard.Listener class to listen to the key presses and releases made on the computer. Whenever a key is pressed, the press() function is called, and whenever a key is released, the release() function is called. The press() function appends the pressed key to a list of keys and writes the contents of the list to a text file after 10 keys have been captured.

**System Information Capture:** The code also captures system information, such as the hostname, IP address, operating system, processor, and machine type, and writes it to a text file. It uses the socket and platform libraries to obtain the information.

**Clipboard Information Capture:** The code captures the data stored in the clipboard and writes it to a text file. It uses the win32clipboard library to access the contents of the clipboard.

**Screenshot Capture:** The code takes a screenshot of the computer screen and saves it as a PNG file. It uses the PIL library to capture the screenshot.

**File Upload:** The code uploads the collected data (keylogs, system information, clipboard data, and screenshot) to a server using the requests library. The uploaded files are sent to the URL specified in the URL variable in the upload_files() function. **SEE INDEX.PHP FILE FOR SERVER SIDE CONFIGURATIONS.**

**File Deletion:** Finally, the code deletes the files created by the keylogger after they have been uploaded to the server. This is done to hide the presence of the keylogger and avoid detection.

It's worth noting that keyloggers can be used for malicious purposes, such as stealing sensitive information or spying on users. Therefore, it is important to use keyloggers only for legitimate purposes and with proper authorization.
  
**Server side config**
In index.php it checks for file extension, file size and upload it to the destination.

Contact me on linkedin: https://www.linkedin.com/in/mtabarikasif/

Upcoming Updates:
 1. Work around windows defender.
 2. An app for both android and ios.
 3. A steganographic file to execute the logger on a victim device.
 4. Test features to check organizatinal security.
 5. You can always recommend any other feature that's helpful in reviewing organizational security.

**This project is only for educational purposes and test cases. I do not recommend any activity without the organizational consent**  
