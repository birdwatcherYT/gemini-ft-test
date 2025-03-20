from dotenv import load_dotenv
load_dotenv()


import argparse
parser = argparse.ArgumentParser(description="モデルの推論スクリプト")
parser.add_argument("model_name", help="使用するモデル名")
args = parser.parse_args()

import json
with open("test.json", encoding='utf-8') as f:
    test_data=json.load(f)

import time
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
model = genai.GenerativeModel(model_name=args.model_name)

delay = 10
for text in test_data:
    retries = 0
    while True:
        try:
            output = model.generate_content(text)
            print(text, "=>", output.text)
            break  # 成功したらループを抜ける
        except ResourceExhausted as e:
            print(f"リソース制限に達しました。{delay}秒待機してリトライします... (リトライ回数: {retries + 1})")
            retries += 1
            time.sleep(delay)
        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")
            raise
