#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time     :2022/8/28 12:11
# @Author   :root
# @FileName :example
import pytesseract

img_path = "./Demo.PNG"
result = pytesseract.image_to_string(image=img_path,lang="eng",config="--psm 1")   #路径；语言；配置
print(result)
