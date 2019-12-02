#!/usr/bin/env python
#coding: utf-8

from PIL import Image

imageSrc = Image.open("./target/page-10.jpg")
logo = Image.open("./water_logo/water_mark_test.png")

logo_mask = logo.convert("L").point(lambda x: min(x, 35))
logo.putalpha(logo_mask)

# 循环遍历水印
for i in range(0, 3):
    for j in range(0, 3):
        x = 33 + (374*j)
        y = 250 + (374*i)
        imageSrc.paste(logo, (x, y), mask=logo)


imageSrc.save('./test.jpg', optimize=True)
