#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-25-21 00:12
# @Update  : Mar-12-21 21:05
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)
# @RefLink : https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html

from PIL import Image
import cv2
import os
import piexif
import shutil
from tqdm import tqdm


def png2jpg(png_path, out_path, quality=75):
    """png2jpg
    Compress a png iamge file by converting it to jpg
    """
    # img = cv2.imread(png_path, 0)
    # w, h = img.shape[::-1]

    img = Image.open(png_path)
    # img = img.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)

    if len(img.split()) == 4:  # RGBA channel
        # prevent IOError: cannot write mode RGBA as BMP
        r, g, b, a = img.split()
        img = Image.merge("RGB", (r, g, b))

    img.convert('RGB').save(out_path, quality=quality)
    img.close()

    return out_path


def different_qualities(png_path):
    for quality in [70, 75, 80, 90, 95, 100]:
        out_path = f"{os.path.splitext(png_path)[0]}-quality-{quality}.jpg"
        png2jpg(png_path, out_path, quality=quality)


def copy_stat(src, dest):
    from win32_setctime import setctime
    stat_origin = os.stat(src)
    # Set atime and mtime
    os.utime(dest, (stat_origin.st_atime, stat_origin.st_mtime))
    # Set ctime
    setctime(dest, stat_origin.st_ctime)


def main():
    png_dir = "D:\\原神截图"
    out_dir = "D:\\原神截图_out"
    exif_dir = "D:\\原神截图_exif"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(exif_dir, exist_ok=True)

    quality = 95

    png_files = os.listdir(png_dir)
    png_files = [f for f in png_files if os.path.splitext(f)[-1] == ".png"]
    print(f"Number of PNG files: {len(png_files)}.")
    # png_path = "AI_2021-02-24-10-18-13-646.png"
    for png_file in png_files:
        image = Image.open(os.path.join(png_dir, png_file))
        # Try to load EXIF info
        exif_dict = None
        try:
            exif_dict = piexif.load(image.info["exif"])
            # print(exif_dict)
        except:
            # KeyError: 'exif'
            # print("KeyError: 'exif', no EXIF info found.")
            pass
        if exif_dict:
            image.close()
            shutil.move(os.path.join(png_dir, png_file),
                        os.path.join(exif_dir, png_file))
            png_files.remove(png_file)

    for png_file in tqdm(png_files):
        jpg_file = f"{os.path.splitext(png_file)[0]}-quality-{quality}.jpg"
        png2jpg(os.path.join(png_dir, png_file),
                os.path.join(out_dir, jpg_file), quality=quality)
        copy_stat(os.path.join(png_dir, png_file),
                  os.path.join(out_dir, jpg_file))
        # Warning! 警告！这里会删除原文件。
        os.remove(os.path.join(png_dir, png_file))


if __name__ == "__main__":
    main()
