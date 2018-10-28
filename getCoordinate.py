# coding: utf-8
import os.path, sys

# 読み込むファイル名
fileName = "typhoon.txt"

# 参照するファイルが存在するかどうか確認
if not os.path.exists(fileName):
    print "参照するファイルがありません！"
    sys.exit(1)

f = open(fileName, "r") # ファイルの読み込み
line = f.read()         # 内容を変数に保存
f.close()               # ファイルを閉じる

lat = line.find("北緯") # ファイルの中から緯度の場所を調べる
lon = line.find("東経") # ファイルの中から経度の場所を調べる

# 緯度と経度が存在すれば出力
if lat > -1 and lon > -1:  
    latStart = lat + 6
    latEnd = latStart + 6
    print "緯度：" + line[latStart:latEnd]   
    lonStart = lon + 6
    lonEnd = lonStart + 7
    print "経度：" + line[lonStart:lonEnd]