# Python-Tesseract

## docker-compose up
% docker-compose up --build tesseract-service

## attach shell
% docker-compose exec tesseract-service bash

## OCR実行 数字の抽出 数字以外は抽出されない
/app# python3 ocr_number_filter.py
>Content-type: application/json
>
>{"digits": "012345\n6789"}
テスト用の画像の数字が入っている

## OCR実行 文字の抽出 日本語の抽出の精度は悪くないが英単語混じりだと少々精度が落ちる
/app# python3 ocr_string_filter.py 

>{"text": "オランダとスペインの行く未を決める「ブレダ攻囲戦」で大きな働きをしたイサック。備兵としての戦いを終え、いよいよロレンツォを討つ、という使命を果た>す時が来た。小悪党ヨナスの話によると、フランスの港町サン・マロに銃を持った百人の女達と共にロレンツォが潜伏しているという。フランスで虐げられているユグノー
>(改革派教会)信徒の少年アンリ、ゼッタ、ヨナスと共にイサックはサン・マロへ向かう。ヨナスの口利きで密輸船に乗り出港した一行。だが船に異常事態が発生!イサックの
>仙討ちの行方は!?第16巻(全16巻)Dillnula)付箋メモ出版社発売日"}
