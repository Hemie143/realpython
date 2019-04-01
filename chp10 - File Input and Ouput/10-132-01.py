import os
import glob

folder = './images'

print('-- Step 1 --')

files_and_folders = os.listdir(folder)
for f in files_and_folders:
    print(os.path.join(folder, f))

print('-- Step 2 --')

png_files = os.path.join(folder, '*/*.png')
for f in glob.glob(png_files):
    print(f)

print('-- Step 3 --')

for currenfolder, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.lower().endswith('.png'):
            full_filename = os.path.join(currenfolder, filename)
            new_filename = full_filename[:-4] + '.jpg'
            os.rename(full_filename, new_filename)
            if os.path.exists(new_filename):
                print(f'{new_filename} is OK')
            else:
                print(f'{new_filename} does not exist!')
