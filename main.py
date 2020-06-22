def main():
    # set directory
    myPath = "D:\Downloads\Anime"

    # imports
    import os
    from os import listdir
    from os.path import isfile, isdir, join
    import re
    import shutil

    while True:
        print("What would you like to organize today?")
        print("1: Anime")
        print("2: TV Shows")
        userInput = input("Enter a number between 1-2: ")

        if userInput == "1":
            # onlyFiles = [f for f in listdir(myPath)] - to return all items in directory
            # get list of ONLY files in directory
            onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
            onlyDirectories = [f for f in listdir(myPath) if isdir(join(myPath, f))]

            # regex to return files with extension .mkv (video files)
            r = re.compile('.*\\.mkv$')

            # use regex expression to return only .mkv files
            fileList = list(filter(r.match, onlyFiles))

            # regex to directories containing SXXEXX
            # example (South.Park.S23E01.Mexican.Joker.UNCENSORED.1080p.WEB-DL.AAC2.0.H264-LAZY[rarbg])
            r = re.compile('^.*\.S\d\dE\d\d.*')

            directoryList = list(filter(r.match, onlyDirectories))

            showList = []

            # print out list 1 item at a time by running in for loop (individual lines)
            for item in fileList:
                result = re.search('^\\[.*\\] +(.*) +- +.*\\.mkv$', item)
                # add file to list of names if not duplicate
                try:
                    showName = result.group(1)
                    if showName not in showList:
                        showList.append(showName)
                except Exception:
                    print(Exception)

            # create directories using list of directory names
            for show in showList:
                try:
                    dirName = str(myPath) + '\\' + str(show)
                    os.makedirs(dirName)
                except OSError as err:
                    print(err)

            # move files into corresponding directories
            for file in listdir(myPath):
                if isfile(join(myPath, file)):
                    try:
                        # move the file to the correct directory
                        originalPathway = str(myPath) + '\\' + str(file)
                        result = re.search('^\\[.*\\] +(.*) +- +.*\\.mkv$', file)
                        fileName = result.group(1)
                        targetPathway = str(myPath) + '\\' + fileName + '\\' + str(file)
                        shutil.move(originalPathway, targetPathway)
                    except shutil.Error as err:
                        print(err)
        elif userInput == "2":
            print("working")
        else:
            print("invalid input")


if __name__ == '__main__':
    main()
