#!/usr/bin/env python
import platform
import math
from datetime import datetime
import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import ctypes
#########Local_Variables##########
removed=0
added=0
current = datetime.now()
megic = "MeGiCaLlY"
flag=1
##################################
def init():
    print("Welcome to "+platform.system()+" ransomware version.")
    time.sleep(2)
    print("System now is watching for changes...")
    time.sleep(2)
    print("For exit please ptress cntrl+c for interrupt signal.")
    time.sleep(2)
#Signing each file in dir with megic sign
def Signing_All():
    print("Signing megic sign in each file for encryption detection.")
    global megic
    directory = "."
    for filename in os.listdir(directory):
        if ".txt" in filename:
            file = open(filename, "r+")
            for line in file:
                if megic in line:
                        return
            file.write(" "+megic)
            file.close()

#Signing new file in dir in megic sign
def Signing_Specific(path):
    print("Signing new file.")
    global megic
    global flag
    flag=0
    file = open(path[2:], "a+")
    #print(path[2:])
    for line in file:
        if megic in line:
            file.close()
            return
    file.write(" "+megic)
    file.close()
    time.sleep(3)
    flag=1

if __name__ == "__main__":
    init()
    Signing_All()
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

#created file handler
def on_created(event):
    time.sleep(2)
    if event.src_path[2:]!="test.py~" and flag:
        global added
        added = added + 1
        print("File "+event.src_path[2:]+" has been created!")
        Wrong_Chars_Checker(event.src_path)
        Valid_Word_Checker(event.src_path)
        Valid_Extention(event.src_path)
        Signing_Specific(event.src_path)
        if added >= 10:
            # raise Exception("Added.")
            if platform.system()=="Windows":
                ctypes.windll.user32.MessageBoxW(0, "There is too many added files.\nCheck for ransomware.", "ALERT", 1)
            else:
                print('ERR: There is too many added files.\nCheck for ransomware.')
            # messagebox.showinfo('Ransomware Alert', 'There is to many added files.\nCheck for ransomware.')
#deleted file handler
def on_deleted(event):

    print("File "+event.src_path[2:]+" removed!")
    global removed
    removed = removed + 1
    if removed>=3:
        if platform.system() == "Windows":
            ctypes.windll.user32.MessageBoxW(0, "There is too many removed files.\nCheck for ransomware.", "ALERT", 1)
        else:
            print('ERR: There is too many removed files.\nCheck for ransomware.')
        #messagebox.showinfo('Ransomware Alert', 'There is to many removed files.\nCheck for ransomware.')
#modified file handler
def on_modified(event):
    global flag
    if event.src_path[2:]!="test.py" and event.src_path[2:]!="test.py~" and flag:

                print("File "+event.src_path[2:]+" has been modified...")
                Wrong_Chars_Checker(event.src_path)
                Valid_Word_Checker(event.src_path)
                Valid_Extention(event.src_path)
                Signing_Check(event.src_path)
                If_Encrypted_Frequency(event.src_path)

                # print("The file is already opened...")
#on moved file handled
def on_moved(event):
    if platform.system() == "Windows":
        ctypes.windll.user32.MessageBoxW(0, "Detetcting file moving...\nFile "+event.src_path[2:]+" have moved to "+event.dest_path[2:]+".\nCheck for ransomware.", "ALERT", 1)
    else:
        print("ERR: Detetcting unexpected file moving...\nFile "+event.src_path[2:]+" have moved to "+event.dest_path[2:]+".\nCheck for ransomware.")
#Filter number: checking sum suspecious chars
def Wrong_Chars_Checker(path):
        file = open(path[2:], "r")
        list = ["|", "./", "$", "#", "@", ">", "&", "~", ]
        for line in file:
            for word in line.split():
                for x in list:
                    if x in word:
                        if platform.system() == "Windows":
                            ctypes.windll.user32.MessageBoxW(0, "There is Suspecious chars in "+path[2:]+"!\nCheck for ransomware.","ALERT", 1)
                        #messagebox.showinfo('Ransomware Alert','There is Suspecious chars in this file!\nCheck for ransomware.')
                        else:
                            print("ERR: There is Suspecious chars in "+path[2:]+"!\nCheck for ransomware.")
                        file.close()
                        return
        file.close()
#Checking if the given words contain string or numbers only
def Valid_Word_Checker(path):
        file = open(path[2:], "r")
        for line in file:
            for word in line.split():
                word = word.replace(',', '')
                word = word.replace('.', '')
                if not word.isdigit() and not word.isalpha():
                    #print(word)
                    #raise Exception("Valid_Word_Checker.")
                    if platform.system() == "Windows":
                        ctypes.windll.user32.MessageBoxW(0, "There is unvalid words in "+path[2:]+"!\nCheck for ransomware.","ALERT", 1)
                    else:
                        print("ERR: There is unvalid words in "+path[2:]+"!\nCheck for ransomware.")
                    file.close()
                    return
                    #messagebox.showinfo('Ransomware Alert','There is unvalid words in this file!\nCheck for ransomware.')
        file.close()
#Alert if happend unexpected creation of non txt file
def Valid_Extention(path):
    if not ".txt" in str(path):
        #raise Exception("Valid_Extention.")
        if platform.system() == "Windows":
            ctypes.windll.user32.MessageBoxW(0, "There is unvalid file extention in "+path[2:]+"!\nCheck for ransomware.","ALERT", 1)
        else:
            print("ERR: There is unvalid file extention in "+path[2:]+"!\nCheck for ransomware.")
        #messagebox.showinfo('Ransomware Alert','There is unvalid file extention in this file!\nCheck for ransomware.')
#Check the magic sign we input the first time.
def Signing_Check(path):
        global megic
        file = open(path[2:], "r")
        for line in file:
            for word in line.split():
                if word == megic:
                    file.close()
                    return
            #raise Exception("Encrypted.")
            #messagebox.showinfo('Ransomware Alert','The megic sign alert for encryption in this file!\nCheck for ransomware.')
        if platform.system() == "Windows":
            ctypes.windll.user32.MessageBoxW(0, "The megic sign alert for encryption in "+path[2:]+"!\nCheck for ransomware.","ALERT", 1)
        else:
            print("ERR: The megic sign alert for encryption in "+path[2:]+"!\nCheck for ransomware.")
        file.close()
        Signing_Specific(path)
#Checking avarage appearence
def If_Encrypted_Frequency(path):
    file = open(path[2:], "r")
    text=""
    for line in file:
        for word in line.split():
            text+=" "+word
    file.close()
    scores = {}
    for letter in text:
        if letter in scores:
             scores[letter] += 1
        else:
            scores[letter]=0
    largest = max(scores.values())
    average = len(text) / 256.0
    if largest < average + 5 * math.sqrt(average):
        if platform.system() == "Windows":
            ctypes.windll.user32.MessageBoxW(0, "Encryption equation detection at: "+ path[2:],"ALERT", 1)
        else:
            print("Encryption equation detection at: "+ path[2:])
def on_pause(event):
    time.sleep(2)
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:

    while True:
        time.sleep(1)
        after = datetime.now()
        if(flag==0):
            my_event_handler.on_modified=on_pause
        else:
            my_event_handler.on_modified=on_modified
        if((after-current).seconds>=2):
            removed=0
            added=0
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()

