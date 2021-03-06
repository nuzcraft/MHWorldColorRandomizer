
from PIL import Image
import numpy as np
import colorsys
from colorthief import ColorThief
import random
import sys
import os
import argparse
import math

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def shift_hue2(arr, new_hues, sat_diff, val_diff, palette, invert):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    for i in range(len(h)):
        for j in range(len(h[i])):
            closest_palette_hue_index = 0
            closest_distance = 1000
            for k in range(len(palette)):
                rp, gp, bp = palette[k]
                # hp, sp, vp = rgb_to_hsv(rp, gp, bp)
                # new_distance = distance_hsv(hp, sp, vp, h[i][j], s[i][j], v[i][j])
                new_distance = distance(rp, gp, bp, r[i][j], g[i][j], b[i][j])
                if new_distance <= 20:
                    break
                if new_distance < closest_distance:
                    closest_palette_hue_index = k
                    closest_distance = new_distance
            h[i][j] = new_hues[closest_palette_hue_index]
            new_s = s[i][j] + sat_diff[closest_palette_hue_index]
            if new_s < 0:
                new_s = 0
            elif new_s > 1:
                new_s = 1
            s[i][j] = new_s
            if v[i][j] >= 255*.2:
                new_v = v[i][j] + val_diff[closest_palette_hue_index]
                if new_v < 0:
                    new_v = 0
                elif new_v > 255:
                    new_v = 255
                v[i][j] = new_v
    r, g, b = hsv_to_rgb(h, s, v)
    if invert:
        r,g,b = 255-r,255-g,255-b
    arr = np.dstack((r, g, b, a))
    return arr

# def invert_hsv(h, s, v):
#     r, g, b = hsv_to_rgb(h, s, v)
#     if (v <= .2 or (v>.8 and s <= .2)):
#         r, g, b = 255-r,255-g,255-b
#     return rgb_to_hsv(r, g, b)

def colorize(image, hues, sats, vals, palette, invert):
    # colorize an image to a new hue
    # hue (0-360)
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue2(arr, hues, sats, vals, palette, invert).astype('uint8'), 'RGBA')
    return new_img

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))

def distance_hsv(h1, s1, v1, h2, s2, v2):
    # hues are 0-1, but they also represent 360 degrees where 360 and 0 are both red
    dh = min(abs(h2-h1), 1-abs(h2-h1)) #this handles the circular nature of hue
    ds = abs(s2-s1)
    dv = abs(v2-v1)/255.0
    return math.sqrt(dh*dh+ds*ds+dv*dv)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description = "Colorize a batch of .pngs with new hues")
    parser.add_argument("-p", "--paletteSize", help = "Example: 4. Higher number means more variations.", required = False, default = "8")
    parser.add_argument("-f", "--file", help = "Example: em/em001/00/mod/em001_00_BML.png. File to colorize. pipe separate for multiple (|)", required = True, default = "")
    # parser.add_argument("-s", "--subDirectory", help = "Example: em01_rathian_002_006/002_image. Secondary directory to colorize. Not used to create the palette. Comma separate for multiple directories.", required = False, default = "")
    
    argument = parser.parse_args()

    colorCount = int(argument.paletteSize)
    files = argument.file
    ls_files = files.split('|')
    # directories = argument.directory
    # subdirectories = argument.subDirectory
    # ls_directories = directories.split(',')
    # ls_subdirectories = subdirectories.split(',')
    imgs_for_palette = []
    imgs = []
    files = []

    # we create 2 lists of images because we only want to create a palette based on the
    # primary folder. This way we create a palette based on velocidrome, then apply the 
    # same hue changes to velociprey 
    for i_file in ls_files:
        imgs_for_palette.append(Image.open(i_file))
        imgs.append(Image.open(i_file))
        files.append(i_file)
    
    # if argument.subDirectory:
    #     for subdirectory in ls_subdirectories:
    #         for file in os.listdir(subdirectory):
    #             if file.endswith('.png'):
    #                 filename = subdirectory + '/' + file
    #                 imgs.append(Image.open(filename))
    #                 files.append(filename)

    # take all the images in the folder and merge them into a super image that we 
    # can pull a full palette from. This new image will be deleted later
    img_size = imgs_for_palette[0].size
    merged_image = Image.new('RGBA', (len(imgs)*img_size[0], img_size[1]))
    for idx, png in enumerate(imgs_for_palette):
        resized_img = imgs_for_palette[idx].resize(img_size)
        merged_image.paste(resized_img, (idx*img_size[0], 0))
    merged_filename = ls_files[0].replace(".png", "_merged.png")
    merged_image.save(merged_filename)

    #color thief generates the palette
    color_thief = ColorThief(merged_filename)
    palette = color_thief.get_palette(color_count=colorCount, quality=3) #8 maybe too busy?

    # once the palette is generated, remove the merged image
    os.remove(merged_filename)

    # take the palette and get the hues for that palette
    # we'll use these to create a range of hues randomize to the same destination hue
    hue_arr = []
    for idx, val in enumerate(palette):
        r, g, b = val
        h, s, v = rgb_to_hsv(r, g, b)
        # print(int(h*360))
        hue_arr.append(h)
    hue_arr.sort()

    # use the hues from the palette (a single point each) to create a new array
    # that represents ranges of hues from 0 to 1 with break point that match the midway
    # point of the hue array.
    hue_diff_arr = [0]
    for idx, val in enumerate(hue_arr):
        if idx + 1 < len(hue_arr):
            hue_diff_arr.append((hue_arr[idx] + hue_arr[idx+1]) / 2)
        else:
            hue_diff_arr.append((hue_arr[idx] + 1.0) / 2)
    hue_diff_arr.append(1.0)

    # create the random hues we're going to shift to
    hues = []
    for x in range(1, len(hue_diff_arr)):
        hues.append(random.random())

    # create random saturation changes - we'll only shift the saturation
    # up just a bit
    sats = []
    for x in range(1, len(hue_diff_arr)):
        sats.append(random.random() * 1.2 - .2)

    # create random value changes - we'll only shift the value
    # down a little bit
    vals = []
    for x in range(1, len(hue_diff_arr)):
        vals.append(-1*(random.random()*255*.3) - (.1*255))

    # base 10% chance to fully invert the colors
    invert = False
    # if random.random() <= .1:
    #     invert = True

    # run through all the images and colorize them based on the new h, s, v info
    for idx, texture in enumerate(imgs):
        new_img = colorize(texture, hues, sats, vals, palette, invert)
        new_img.save(files[idx])