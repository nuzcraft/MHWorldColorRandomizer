
from PIL import Image
import numpy as np
import colorsys
import argparse

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def greyscale(arr):
    r,g,b,a = np.rollaxis(arr, axis=-1)
    for i in range(len(r)):
        for j in range(len(r[i])):
            grey = max(min(0.299*r[i][j] + 0.587*g[i][j] + 0.144*b[i][j], 255.0), 0.0)
            r[i][j] = grey
            g[i][j] = grey
            b[i][j] = grey
    arr = np.dstack((r,g,b,a))
    return arr

def saturate(arr):
    r,g,b,a = np.rollaxis(arr, axis=-1)
    h,s,v = rgb_to_hsv(r,g,b)
    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j] += 0.2
            if s[i][j] > 1.0:
                s[i][j] = 1.0
    r,g,b = hsv_to_rgb(h,s,v)
    arr = np.dstack((r,g,b,a))
    return arr

if __name__=='__main__':
    parser = argparse.ArgumentParser(description = "Colorize a batch of .pngs with new hues")
    parser.add_argument("-f", "--file", help = "Example: em/em001/00/mod/em001_00_BML.png. File to colorize. pipe separate for multiple (|)", required = True, default = "")
   
    argument = parser.parse_args()

    files = argument.file
    ls_files = files.split('|')
    imgs = []
    files = []

    for i_file in ls_files:
        imgs.append(Image.open(i_file))
        files.append(i_file)

    for idx, texture in enumerate(imgs):
        tex = texture.convert('RGBA')
        arr = np.array(np.asarray(tex).astype('float'))
        if "eye" in files[idx]:
            new_img = Image.fromarray(saturate(arr).astype('uint8'), 'RGBA')
        else:
            new_img = Image.fromarray(greyscale(arr).astype('uint8'), 'RGBA')
        new_img.save(files[idx])