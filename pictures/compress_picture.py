#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Feb-25-21 00:12
# @Update  : Mar-12-21 21:05
# @Author  : Kelly Hwong (dianhuangkan@gmail.com)
# @RefLink : https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html

from PIL import Image
# import cv2
import os
import glob
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
    stat_origin = os.stat(src)
    # Set atime and mtime
    os.utime(dest, (stat_origin.st_atime, stat_origin.st_mtime))

    # Set ctime
    import platform
    sys = platform.system()
    if sys == "Windows":
        from win32_setctime import setctime
        setctime(dest, stat_origin.st_ctime)
    elif sys == "Darwin":
        # Still cannot set ctime on Mac platform
        # See: https://stackoverflow.com/questions/56008797/how-to-change-the-creation-date-of-file-using-python-on-a-mac
        pass


def main():
    # Prepare directories
    png_dir = "/Users/HuangKan/Downloads/原神截图Mac"
    out_dir = "/Users/HuangKan/Downloads/原神截图Mac_out"
    exif_dir = "/Users/HuangKan/Downloads/原神截图Mac_exif"
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(exif_dir, exist_ok=True)

    # Set quality
    quality = 95

    png_paths = glob.glob(os.path.join(png_dir, "*.png"))\
        + glob.glob(os.path.join(png_dir, "*.PNG"))
    print(f"Number of PNG files: {len(png_paths)}.")

    # Run here firstly, to split png files with and without EXIF info
    for png_file in tqdm(png_paths):
        image = Image.open(png_file)
        # Try to load EXIF info
        exif_dict = None
        try:
            exif_dict = piexif.load(image.info["exif"])
            # print("got exif_dict!")
        except:
            # print("KeyError: 'exif', no EXIF info found.")
            pass
        if exif_dict:
            image.close()

            def move_exif_file(src, dest_dir):
                dest = os.path.join(dest_dir, os.path.split(png_file)[1])
                print(f"Moving file from {src} to {dest}")
                shutil.move(src, dest)
                return dest

            move_exif_file(png_file, exif_dir)

    # Compress png files without EXIF to jpg
    png_paths = glob.glob(os.path.join(png_dir, "*.png"))\
        + glob.glob(os.path.join(png_dir, "*.PNG"))
    # png_paths = [f for f in png_paths if os.path.splitext(f)[-1] == ".png"]
    print(f"Number of PNG files without EXIF: {len(png_paths)}.")

    for png_path in tqdm(png_paths):
        jpg_path = f"{os.path.splitext(png_path)[0]}-quality-{quality}.jpg"
        jpg_path = os.path.join(out_dir, os.path.split(jpg_path)[1])
        jpg_path = png2jpg(png_path, jpg_path, quality=quality)
        copy_stat(png_path, jpg_path)
        os.remove(png_path)  # Warning! 警告！这里会删除原文件。

    # Compress png files with EXIF to jpg
    png_paths = glob.glob(os.path.join(exif_dir, "*.png"))\
        + glob.glob(os.path.join(exif_dir, "*.PNG"))
    # png_paths = [f for f in png_paths if os.path.splitext(f)[-1] == ".png"]
    print(f"Number of PNG files with EXIF: {len(png_paths)}.")

    for png_path in tqdm(png_paths):
        jpg_path = f"{os.path.splitext(png_path)[0]}-quality-{quality}.jpg"
        jpg_path = os.path.join(out_dir, os.path.split(jpg_path)[1])
        jpg_path = png2jpg(png_path, jpg_path, quality=quality)
        copy_stat(png_path, jpg_path)

        image = Image.open(png_path)  # copy png file's EXIF info to jpg file
        exif_dict = piexif.load(image.info["exif"])
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, jpg_path)
        os.remove(png_path)  # Warning! 警告！这里会删除原文件。


if __name__ == "__main__":
    main()
