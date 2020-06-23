# file-organizer

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Built With](#built_with)

## About <a name = "about"></a>

Python program that organizes your Anime or TV Shows into organized folders.

Will organize .mkv files that are in the following format: [Group] Show Name - Episode # [Resolution].mkv

Example: [HorribleSubs] Hunter X Hunter - 126 [1080p]

The file above would be moved into a new or pre-existing folder named Hunter X Hunter, along with the rest of the Hunter X Hunter episodes in that directory.

## Getting Started <a name = "getting_started"></a>

### Prerequisites
```
    Python 3.8.2
    Visual C++ Redistributable
```


To create an .exe file, use pyinstaller. (Instructions: https://datatofish.com/executable-pyinstaller/)

1. Open Command Prompt
2. Enter the following into the command prompt: pip install pyinstaller
3. Change directory to where the Python script is stored. (Ex: cd C:\Users\HalfLife7\Desktop\file-organizer)
4. Enter the following into the command prompt: pyinstaller --onefile file-organizer.py
5. Run the .exe file located in the newly created dist folder (if you get an error message, you may need to install Visual C++ Redistributable).

Alternatively, you can download the .zip folder and launch the .exe from there. (if it does not work, try creating the .exe using the instructions above)

## Built With <a name = "built_with"></a>

- Python
- Regex
