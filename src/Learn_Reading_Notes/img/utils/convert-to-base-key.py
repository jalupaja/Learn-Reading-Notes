#!/usr/bin/env python3

from pathlib import Path
from PIL import Image

path = "../b/"
save_path = "../"
file_extension = ".png"
remove_widht = 630  # px

bass_key = Image.open("base-lines-short.png")


for p in Path(path).glob(f"*{file_extension}"):
    img = Image.open(p.absolute())
    img.paste(bass_key)
    img.save(save_path + p.name)
