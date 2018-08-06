# coding: utf-8
import re, os.path, sys

# 変数の初期化
lonStart = lonEnd = latStart = latEnd = i = 0
fileName = "typhoon.txt"

# 参照するファイルが存在するかどうか確認
if not os.path.exists(fileName):
    print "参照するファイルがありません！"
    sys.exit(1)

# ファイルを読み込み、その中から緯度と経度の場所を調べる
f = open(fileName, "r")
line = f.read()
matchLine = re.finditer("[+-]?[0-9]+[\.]?[0-9]*[eE]?[+-]?[0-9]*", line)
for match in matchLine:
    if i == 9:
        latStart = match.start()
        latEnd = match.end()
    elif i == 12:
        lonStart = match.start()
        lonEnd = match.end()
    i += 1

# 座標の出力
print "緯度：" + line[latStart:latEnd]
print "経度：" + line[lonStart:lonEnd]

# ファイルを閉じる
f.close()