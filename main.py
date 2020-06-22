def main():
    # TODO: create GUI or .exe to run from command line
    # TODO: refactor main() to split up into smaller functions

    # set directory
    my_path = "E:\Downloads\TV Shows"

    # imports
    import os
    from os import listdir
    from os.path import isfile, isdir, join
    import re
    import shutil

    # TODO: ask for user to set the directory
    while True:
        print("What would you like to organize today?")
        print("1: Anime")
        print("2: TV Shows")
        user_input = input("Enter a number between 1-2: ")

        if user_input == "1":
            # only_files = [f for f in listdir(my_path)] - to return all items in directory
            # get list of ONLY files in directory
            only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

            # regex to return files with extension .mkv (video files)
            r = re.compile('.*\\.mkv$')

            # use regex expression to return only .mkv files
            file_list = list(filter(r.match, only_files))

            show_list = []

            # print out list 1 item at a time by running in for loop (individual lines)
            for item in file_list:
                result = re.search('^\\[.*\\] +(.*) +- +.*\\.mkv$', item)
                # add file to list of names if not duplicate
                try:
                    show_name = result.group(1)
                    if show_name not in show_list:
                        show_list.append(show_name)
                except Exception:
                    print(Exception)

            # create directories using list of directory names
            for show in show_list:
                try:
                    directory_name = str(my_path) + '\\' + str(show)
                    os.makedirs(directory_name)
                except OSError as err:
                    print(err)

            # move files into corresponding directories
            for file in listdir(my_path):
                if isfile(join(my_path, file)):
                    try:
                        # move the file to the correct directory
                        source = str(my_path) + '\\' + str(file)
                        result = re.search('^\\[.*\\] +(.*) +- +.*\\.mkv$', file)
                        file_name = result.group(1)
                        destination = str(my_path) + '\\' + file_name + '\\' + str(file)
                        shutil.move(source, destination)
                    except shutil.Error as err:
                        print(err)
        elif user_input == "2":
            # only_directories = [f for f in listdir(my_path)] - to return all items in directory
            # get list of ONLY directories in directory
            only_directories = [f for f in listdir(my_path) if isdir(join(my_path, f))]

            # regex to directories containing SXXEXX
            # example (South.Park.S23E01.Mexican.Joker.UNCENSORED.1080p.WEB-DL.AAC2.0.H264-LAZY[rarbg])
            r = re.compile('^.*\.S\d\dE\d\d.*')

            directory_list = list(filter(r.match, only_directories))
            print(directory_list)

            show_list = []

            # print out list 1 item at a time by running in for loop (individual lines)
            for item in directory_list:
                result = re.search('^(.*)\.S\d\dE\d\d.*', item)
                # add file to list of names if not duplicate
                try:
                    show_name = result.group(1)
                    if show_name not in show_list:
                        show_list.append(show_name)
                except Exception:
                    print(Exception)

            # create directories using list of directory names
            for show in show_list:
                try:
                    directory_name = str(my_path) + '\\' + str(show)
                    os.makedirs(directory_name)
                except OSError as err:
                    print(err)

            # move files into corresponding directories
            for folder in directory_list:
                try:
                    # move the folder to the correct directory
                    source = str(my_path) + '\\' + str(folder)
                    result = re.search('^(.*)\.S\d\dE\d\d.*', folder)
                    folder_name = result.group(1)
                    destination = str(my_path) + '\\' + folder_name + '\\' + str(folder)
                    shutil.move(source, destination)
                except shutil.Error as err:
                    print(err)

        else:
            print("invalid input")


if __name__ == '__main__':
    main()
