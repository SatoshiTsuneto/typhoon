# coding: utf-8
import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://www.jma.go.jp/jp/typh/"

# URLにアクセスする htmlが帰ってくる
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
typhoon = BeautifulSoup(html, "html.parser")

# 台風情報が記載されている要素を出力
print typhoon.find("div", class_="forecast")
