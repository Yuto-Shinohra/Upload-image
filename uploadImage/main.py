from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from firebase_admin import credentials,initialize_app,storage
import urllib.request
from urllib.parse import urlencode
from PIL import Image
import sys
sys.path.append('/path/to/dir')
import os
import cv2
import numpy as np
from PIL import Image
import pyocr
from urllib import response
import requests 
#カレンダーAPIスコープ
SCOPES = ['https://www.googleapis.com/auth/calendar']
gotimage = 0

#Firebase認証
  cred = credentials.Certificate("loadimage-9bac0-firebase-adminsdk-abrf6-698df0bf5f.json")
  initialize_app(cred,{'storageBucket': 'gs://loadimage-9bac0.appspot.com'})
  
  bucket = storage.bucket('loadimage-9bac0.appspot.com')
  #アップロード用
  filenameup = 'hanba-gu6321.png'
  path = '/Users/yuto_shinohara/Documents/Programming/python/textdata/カメンダー/completeversion'
  #ダウンロード用
  filenamedown = "post"
  
  #urlクエリパラメータ
  q_data = {
      'q': 'Pythonでクエリパラメータを作成',
      'option': [1, 3, 5],
      'lang': 'jp',
  }
  
  
  #OCR
  tools = pyocr.get_available_tools()
  tool = tools[0]
  
  #Firebaseダウンロード
  def download_blob(filenamedown, path):
      global gotimage
      blob = bucket.blob(filenamedown)
      blob.download_to_filename(path + filenamedown)
      blob.make_public()
      print(blob.public_url)
      gotimage = blob.public_url
      print("ダウンロード完了")
      #urlから画像を保存する
      url = gotimage
      file_name = "sample.png"
      response = requests.get(url)
      image = response.content


