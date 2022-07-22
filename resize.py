import PIL
import os
import os.path
from PIL import Image
"""
f = r'c://Users/xx/Desktop/imagetest'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((2296,1724))
    img.save(f_img)
"""

obj  = os.walk('D:\\indoorCVPR_09')
images = []
for path, dirs, files in obj:
    if not len(files) > 0:
        continue
    for img in files:
        if not img:
            continue
        image_path = '%s\\%s' % (path, img)
        images.append(image_path)

import random
print(len(images))
while len(images) > 1000:
    int = random.randint(0, len(images) - 1)
    images.pop(int)

print(len(images))

for file in images:
    #f_img = f+"/"+file
    img = Image.open(file)
    img = img.resize((2296,1724))
    img.save("D:\\no_note_detected\image_%s.jpg" % random.randint(0, 100000))
