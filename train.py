from dotenv import load_dotenv
load_dotenv()

import time
import google.generativeai as genai

import json

with open("train.json", encoding='utf-8') as f:
    training_data=json.load(f)

operation = genai.create_tuned_model(
    display_name="extract_hobby",
    source_model="models/gemini-1.5-flash-001-tuning",
    epoch_count=3,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,
)

for status in operation.wait_bar():
    time.sleep(10)

for model_info in genai.list_tuned_models():
    print(model_info.name)
