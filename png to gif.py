import sys
import os

files = os.listdir()

for f in files:
    if 'CRR_rainfall' not in f:
        continue
    if 'png' not in f:
        continue
    seps = f.split('.')
    print(len(seps),seps[0])
    print("ffmpeg -i {}.png {}.gif".format(seps[0], seps[1]))
    os.system("ffmpeg -i {}.png {}.gif".format(seps[0], seps[0]))