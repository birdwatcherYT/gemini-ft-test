from dotenv import load_dotenv
load_dotenv()

import argparse
parser = argparse.ArgumentParser(description="モデルの削除スクリプト")
parser.add_argument("model_name", nargs="?", help="削除するモデル名")
parser.add_argument("-a", "--all", action="store_true", help="全てのモデルを削除する")
args = parser.parse_args()

import google.generativeai as genai
if args.all:
    # 全てのモデルを削除
    models = genai.list_tuned_models()
    for model in models:
        genai.delete_tuned_model(model.name)
        print(f"モデル '{model.name}' を削除しました。")
elif args.model_name:
    # 指定されたモデルを削除
    genai.delete_tuned_model(args.model_name)
    print(f"モデル '{args.model_name}' を削除しました。")
else:
    print("モデル名を指定するか、-a または --all オプションを指定してください。")
