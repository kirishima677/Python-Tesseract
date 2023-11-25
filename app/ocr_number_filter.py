#!/usr/bin/python3
 
from PIL import Image
import sys
import json
import os
 
import pyocr
import pyocr.builders
 
#OCRが利用可能か
arr_ocr_tool = pyocr.get_available_tools()
if len(arr_ocr_tool) == 0:
    print("OCR is not available with the pyocr library.")
    sys.exit(1)
ocr_tool = arr_ocr_tool[0]
 
#OCR設定（数字と-.のみ認識）
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
builder.tesseract_configs.append("digits")
 
#OCR実行 数字だけを認識
ocr_txt = ocr_tool.image_to_string(
    Image.open("./targetImage/digits.png"),
    lang="eng",
    builder=builder
)
 
#実行結果をJSONで表示
arr_ocr = {}
arr_ocr['digits'] = ocr_txt
ocr_json = json.dumps(arr_ocr)
print ("Content-type: application/json\n")
print (ocr_json)