import os
import shutil

# list all files
files = os.listdir('.')

# identify screenshots
screenshots = []
for file in files:
    if 'Screenshot' in file and 'png' in file:
        screenshots.append(file)
print(screenshots)

# move screenshots to Screenshots_folder
destination = '/Users/tanyabalwani/Desktop/Screenshots'
for file in screenshots:
    shutil.move(file, destination)
