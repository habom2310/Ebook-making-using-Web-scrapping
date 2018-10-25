import os
import glob


zfile = glob.glob('*.zip')

print(zfile)

for file in zfile:
    
    base = os.path.splitext(file)[0]
    
    if not os.path.isfile(base + ".epub"):
        os.rename(file, base + ".epub")