def main():
    import shutil
    import os

    src = input('Enter proper parent folder location: ').strip()

    print()
    #print(src)

    ext = input('Write the file extention that you want to seperate (eg .ttf): ').strip()


    print()

    dest = src

    try:
        os.mkdir(src + '\\00_Copied\\')
        dest = src + '\\00_Copied\\'

    except FileExistsError:
        dest = src + '\\00_Copied\\'

    print(f"Files will be copied to {dest} directory if available.")

    print()
    #print(dest)

    print('Please wait...')

    print()

    file_exist_flag = False

    for dirs, subdirs, files in os.walk(src):
        for file in files:
            if file.endswith(ext):
                file_exist_flag = True
                filename = os.path.join(src, dirs, file)
                if os.path.exists(filename):
                    #print(filename)
                    try:
                        shutil.copy(filename, dest)
                    except:
                        pass
    if file_exist_flag:            
        print(f'Copied.\n\nOpen {dest} directory to see the files')
    else:
        print('No files found with the given extention')
    
    print()

main()

while True:
    print('Do you want to copy more files? (y/n): ', end='')
    choice = input().strip().lower()
    if choice == 'y':
        main()
    else:
        break

