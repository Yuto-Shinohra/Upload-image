Last login: Fri Jul 22 20:48:49 on ttys001
yuto_shinohara@shinoharayuujinnoMacBook-Pro ~ % cd Documents 
yuto_shinohara@shinoharayuujinnoMacBook-Pro Documents % cd Programming 
yuto_shinohara@shinoharayuujinnoMacBook-Pro Programming % cd python/textdata/カメンダー 
yuto_shinohara@shinoharayuujinnoMacBook-Pro カメンダー % ls
calendar app		completeversion		completeversionItem	completeversionpost	python firebase		python ocr		python ocr 2
yuto_shinohara@shinoharayuujinnoMacBook-Pro カメンダー % cd completeversion
yuto_shinohara@shinoharayuujinnoMacBook-Pro completeversion % ls
credentials.json					main.py							token.pickle
loadimage-9bac0-firebase-adminsdk-abrf6-698df0bf5f.json	sample.png
yuto_shinohara@shinoharayuujinnoMacBook-Pro completeversion % ls
credentials.json					main.py							token.pickle
loadimage-9bac0-firebase-adminsdk-abrf6-698df0bf5f.json	sample.png
yuto_shinohara@shinoharayuujinnoMacBook-Pro completeversion % git add main.py
fatal: not a git repository (or any of the parent directories): .git
yuto_shinohara@shinoharayuujinnoMacBook-Pro completeversion % ls
credentials.json					main.py							token.pickle
loadimage-9bac0-firebase-adminsdk-abrf6-698df0bf5f.json	sample.png
yuto_shinohara@shinoharayuujinnoMacBook-Pro completeversion % fish
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
yuto_shinohara@shinoharayuujinnoMacBook-Pro ~/D/P/p/t/カ/completeversion> git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint: 	git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint: 	git branch -m <name>
Initialized empty Git repository in /Users/yuto_shinohara/Documents/Programming/python/textdata/カメンダー/completeversion/.git/
yuto_shinohara@shinoharayuujinnoMacBook-Pro ~/D/P/p/t/カ/completeversion (master)> ;s
fish: Unknown command: s
fish: 
;s
 ^
yuto_shinohara@shinoharayuujinnoMacBook-Pro ~/D/P/p/t/カ/completeversion (master) [127]> ls
credentials.json					main.py							token.pickle
loadimage-9bac0-firebase-adminsdk-abrf6-698df0bf5f.json	sample.png
yuto_shinohara@shinoharayuujinnoMacBook-Pro ~/D/P/p/t/カ/completeversion (master)> vim main.py 

























  1 from __future__ import print_function
  2 import datetime
  3 import pickle
  4 import os.path
  5 from googleapiclient.discovery import build
  6 from google_auth_oauthlib.flow import InstalledAppFlow
  7 from google.auth.transport.requests import Request
  8 from firebase_admin import credentials,initialize_app,storage
  9 import urllib.request
 10 from urllib.parse import urlencode
 11 from PIL import Image
 12 import sys
 13 sys.path.append('/path/to/dir')
 14 import os
 15 import cv2
 16 import numpy as np
 17 from PIL import Image
 18 import pyocr
 19 from urllib import response
 20 import requests
 21 
 22 
 23 #カレンダーAPIスコープ
 24 SCOPES = ['https://www.googleapis.com/auth/calendar']
 25 
 26 
 27 #Firebase
 28 #取得した画像
 29 gotimage = 0
 30 #Firebase認証
 31 cred = credentials.Certificate("loadimage-9bac0-firebase-adminsdk-abrf6-698df0bf5f.json")
 32 initialize_app(cred,{'storageBucket': 'gs://loadimage-9bac0.appspot.com'})
 33 
 34 bucket = storage.bucket('loadimage-9bac0.appspot.com')
 35 #アップロード用
 36 filenameup = 'hanba-gu6321.png'
 37 path = '/Users/yuto_shinohara/Documents/Programming/python/textdata/カメンダー/completeversion'
 38 #ダウンロード用
 39 filenamedown = "post"
 40 
 41 #urlクエリパラメータ
 42 q_data = {
 43     'q': 'Pythonでクエリパラメータを作成',
 44     'option': [1, 3, 5],
 45     'lang': 'jp',
 46 }
 47 
 48 
 49 #OCR
 50 tools = pyocr.get_available_tools()
 51 tool = tools[0]
 52 
 53 #Firebaseダウンロード
 54 def download_blob(filenamedown, path):
 55     global gotimage
 56     blob = bucket.blob(filenamedown)
 57     blob.download_to_filename(path + filenamedown)
 58     blob.make_public()
 59     print(blob.public_url)
 60     gotimage = blob.public_url
 61     print("ダウンロード完了")
 62     #urlから画像を保存する
 63     url = gotimage
 64     file_name = "sample.png"
 65     response = requests.get(url)
 66     image = response.content
"main.py" 122L, 3396B

