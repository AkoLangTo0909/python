"""
Module 2 — Activity: File Sorting with os and shutil
Student: Pereda,Chris Euki     
Date: Sept 27 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================

WHAT DID YOU BUILD?
This script sorts files in a folder into subfolders based on their
file extensions. For example, .pdf files go into a PDF folder and
.jpg files go into a JPG folder. 
explain these like im your friend you not coding
I made a script that cleans up a messy folder by putting similar files together.
It looks at the ending of each filename—like “.pdf” or “.jpg”—and moves each file into a folder for that type.
So PDFs go in one folder, pictures in another, and so on.
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


============================================
KEY VOCABULARY
============================================
- os module: is helping Python to work on with files and folder of your computer 
- shutil module: is helping python in a way where this one is copy and moving the files and folder
- file path: is the address of a file where you can locate it
- directory: this is just like a folder that store your files
- extension: is the part of the file name after the final dot for example is sample.docx or sample.pdf 
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""
import os
import shutil

source_folder = "myfiles"

for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file)

    if file.endswith((".jpg", ".png", ".jpeg")):
        folder = os.path.join(source_folder, "Images")

    elif file.endswith((".pdf", ".docx", ".txt")):
        folder = os.path.join(source_folder, "Documents")

    elif file.endswith((".mp3", ".wav")):
        folder = os.path.join(source_folder, "Music")

    else:
        continue

    if not os.path.exists(folder):
        os.makedirs(folder)

    shutil.move(file_path, folder)

print("Files sorted successfully!")

# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
I need to make the right call for the folder i assign to not have some errors or change the file i called for.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
