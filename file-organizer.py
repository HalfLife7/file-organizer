def main():
    # TODO: create GUI
    # TODO: refactor main() to split up into smaller functions

    # imports
    import os
    from os import listdir, path
    from os.path import isfile, isdir, join
    import re
    import shutil

    while True:
        # ask user for what directory to organize
        sorting_directory = input("Enter the directory you want to organize (default: D:\Downloads): ")

        # set default if user input was empty
        if sorting_directory == "":
            sorting_directory = "D:\Downloads"
            break
        # if valid path, move on to options
        elif path.isdir(sorting_directory) == True:
            break
        # if invalid, ask for input again
        else:
            print("Invalid directory, please try again.")

    while True:
        print("Available Options for", sorting_directory)
        print("1: Sort Anime")
        print("2: Sort TV Shows")
        print("3: Change Directory")
        user_input = input("Enter a number between 1-3: ")

        if user_input == "1":
            # only_files = [f for f in listdir(sorting_directory)] - to return all items in directory
            # get list of ONLY files in directory
            only_files = [f for f in listdir(sorting_directory) if isfile(join(sorting_directory, f))]

            # regex to return files with extension .mkv (video files)
            r = re.compile('.*\\.mkv$')

            # use regex expression to return only .mkv files
            file_list = list(filter(r.match, only_files))

            show_list = []

            # will go through all .mkv files and find ones in the format [Group] Show Name - Episode # [Resolution].mkv
            # Example: [HorribleSubs] Hunter X Hunter - 126 [1080p]
            # TODO: add regex rules for these exceptions
            # will bug out and now work for episodes that do not have an episode # or do not follow that format
            # Example: [MTBB] Psycho-Pass the Movie (2015) v2 [C5A5F12D].mkv
            for item in file_list:
                result = re.search('^\\[.*\\] +(.*) +- +.*\\.mkv$', item)
                # add file to list of names if not duplicate
                try:
                    show_name = result.group(1)
                    if show_name not in show_list:
                        show_list.append(show_name)
                except Exception:
                    print("The following file is not in the right format: ", item)

            # if there are no suitable files to be organized, go back to main menu
            if len(show_list) == 0:
                print("There is no valid Anime shows to be organized, returning to Main Menu.", end="\n\n")
                continue

            # create directories using list of directory names
            for show in show_list:
                try:
                    directory_name = str(sorting_directory) + '\\' + str(show)
                    os.makedirs(directory_name)
                except OSError as err:
                    print(err)

            # move files into corresponding directories
            for file in listdir(sorting_directory):
                if file.endswith('.mkv'):
                    try:
                        # move the file to the correct directory
                        source = str(sorting_directory) + '\\' + str(file)
                        result = re.search('^\\[.*\\] +(.*) +- +.*\\.mkv$', file)
                        if result is None:
                            continue
                        else:
                            file_name = result.group(1)
                            destination = str(sorting_directory) + '\\' + file_name + '\\' + str(file)
                            shutil.move(source, destination)
                    except shutil.Error as err:
                        print(err)
            print("The following shows were organized: ", show_list, end="\n\n")
        elif user_input == "2":
            # only_directories = [f for f in listdir(sorting_directory)] - to return all items in directory
            # get list of ONLY directories in directory
            only_directories = [f for f in listdir(sorting_directory) if isdir(join(sorting_directory, f))]

            # regex to directories containing SddEdd
            # example (South.Park.S23E01.Mexican.Joker.UNCENSORED.1080p.WEB-DL.AAC2.0.H264-LAZY[rarbg])
            r = re.compile('^.*\.S\d\dE\d\d.*')

            directory_list = list(filter(r.match, only_directories))
            # print(directory_list)

            show_list = []

            # if there are no suitable files to be organized, go back to main menu
            if len(show_list) == 0:
                print("There is no valid TV Shows to be organized, returning to Main Menu.", end="\n\n")
                continue

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
                    directory_name = str(sorting_directory) + '\\' + str(show)
                    os.makedirs(directory_name)
                except OSError as err:
                    print(err)

            # move files into corresponding directories
            for folder in directory_list:
                try:
                    # move the folder to the correct directory
                    source = str(sorting_directory) + '\\' + str(folder)
                    result = re.search('^(.*)\.S\d\dE\d\d.*', folder)
                    if result is None:
                        continue
                    else:
                        folder_name = result.group(1)
                        destination = str(sorting_directory) + '\\' + folder_name + '\\' + str(folder)
                        shutil.move(source, destination)
                except shutil.Error as err:
                    print(err)
            print("The following shows were organized: ", show_list, end="\n\n")
        elif user_input == "3":
            sorting_directory=input("Enter the new directory you want to sort: ")
        else:
            print("invalid input")


if __name__ == '__main__':
    main()
