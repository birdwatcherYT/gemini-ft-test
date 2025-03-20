# gemini-ft-test
Geminiのファインチューニングをやってみる

## toy-problem
与えられた文章から趣味を抽出する

例: 
```json
  {"text_input": "休日に散歩して鳥の写真を撮ります", "output": "バードウォッチング"}
```

- [train.json](train.json): ファインチューニング用データ
- [test.json](test.json): テスト用データ


## コード
`.env`
```
GOOGLE_API_KEY="GOOGLE AI STUDIOから入手したAPIキー"
```

### 学習
ファインチューニング
```sh
uv run python train.py
```

### 推論
学習済みモデルを使ったテスト
```sh
uv run python infer.py --model_name
```
リソース使い果たしたら待機するようにしてます

### モデルの確認
```sh
uv run python check.py
```

### モデルの削除
特定のモデル削除
```sh
uv run python delete.py --model_name
```
全部削除
```sh
uv run python delete.py --all
```

