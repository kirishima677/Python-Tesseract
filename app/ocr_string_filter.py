#!/usr/bin/python3

from PIL import Image, ImageEnhance
import sys
import json
import os

import pyocr
import pyocr.builders
import pytesseract

# 画像ファイルの絶対パスを取得
image_path = os.path.abspath("./targetImage/string.png")

# 解析画像読み込み TODO: 画像のパスを引数で受け取るようにする
print("Image Path:", image_path)
img = Image.open(image_path) 
img_g = img.convert('L') # Gray変換
enhancer = ImageEnhance.Contrast(img_g) # コントラストを上げる
img_con = enhancer.enhance(2.0) # コントラストを上げる

# 画像サイズを表示（デバッグ用）
print("Original Image Size:", img.size)
print("Enhanced Image Size:", img_con.size)

# OCR実行 全ての文字列を認識
ocr_txt = pytesseract.image_to_string(img_con, lang='eng+jpn')

# 実行結果をJSONで表示（半角スペースと改行を削除）
arr_ocr = {"text": ocr_txt.replace(" ", "").replace("\n", "")}
ocr_json = json.dumps(arr_ocr, ensure_ascii=False)
print("Content-type: application/json\n")
print(ocr_json)