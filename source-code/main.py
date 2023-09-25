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
    pass

print(f"Files will be copied to {dest} directory.")

print()
#print(dest)

print('Please wait...')

print()

for dirs, subdirs, files in os.walk(src):
    for file in files:
        if file.endswith(ext):
            filename = os.path.join(src, dirs, file)
            if os.path.exists(filename):
                #print(filename)
                try:
                    shutil.copy(filename, dest)
                except:
                    pass

print(f'Copied.\n\nOpen {dest} directory to see the files')

