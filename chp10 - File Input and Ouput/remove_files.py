import os

folder = './little pics'

for currenfolder, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.lower().endswith('.jpg'):
            full_filename = os.path.join(currenfolder, filename)
            filesize = os.path.getsize(full_filename)
            if filesize < 2000:
                os.remove(full_filename)
                print(f'Deleted {full_filename}')
