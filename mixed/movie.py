#!/usr/bin/python3
import os

for i in range(201):
    os.system("../../utils-gp/bitmap_field -u 8 spinodal.odr/u.%d spinodal.odr/fr_%04d.png -1 1 > /dev/null" %(i,i))

os.system("ffmpeg -r 30 -y -i spinodal.odr/fr_%4d.png -preset veryslow -c:v libx265 -crf 17 -pix_fmt yuv420p -tag:v hvc1 -movflags faststart spinodal.mov")
