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
### 環境構築
```sh
uv sync
```
`.env`を用意
```
GOOGLE_API_KEY="GOOGLE AI STUDIOから入手したAPIキー"
```

### 学習
ファインチューニング
```sh
uv run python train.py
```

結果:
>100%|██████████████████████████████████████████████████████████████████████████████████| 53/53 [02:46<00:00,  3.14s/it]

3分もかかりませんでした。

### 推論
学習済みモデルを使ったテスト
```sh
uv run python infer.py --model_name 使用するモデル名
```
- 使用するモデル名は**モデルの確認**で確認できます
- リソース使い果たしたら待機するようにしてます

結果:
```
休日はカフェで読書をして過ごします => 読書
ジムに通って筋トレをするのが日課です => 筋トレ
映画館で最新のアクション映画を観るのが楽しみです => 映画鑑賞
休日は家庭菜園で野菜を育てています => 家庭菜園
登山をして自然の景色を楽しんでいます => 登山
旅行先で写真を撮るのが好きです => 写真撮影
ギターを弾いてオリジナル曲を作っています => ギター
競馬のレースを観戦するのが趣味です => 競馬観戦
夜に天体観測をして星座を探しています => 天体観測
釣りをして、のんびり過ごすのが好きです => 釣り
バイクでツーリングをして遠くまで出かけます => ツーリング
スケートボードの技を練習しています => スケートボード
クラシック音楽を聴いてリラックスしています => クラシック音楽
休日は料理をして新しいレシピに挑戦しています => 料理
美術館を巡ってアート作品を鑑賞しています => 美術館鑑賞
家庭用3Dプリンターでフィギュアを作っています => 3Dプリンター
リソース制限に達しました。10秒待機してリトライします... (リトライ回数: 1)
ランニングをして体を鍛えています => ランニング
和菓子作りに挑戦しています => 和菓子作り
ボルダリングのジムに通っています => ボルダリング
フラワーアレンジメントを学んでいます => フラワーアレンジメント
ボードゲームカフェで友人と遊んでいます => ボードゲーム
ゲーム実況動画を作って投稿しています => ゲーム実況
カメラを持って動物の写真を撮っています => 写真撮影
プラモデルを組み立てるのが楽しいです => プラモデル作り
合唱団に入って歌を練習しています => 合唱団
ドライブをしながら好きな音楽を聴いています => ドライブ
電子工作でラジオを自作しています => 電子工作
サバイバルゲームに参加しています => サバイバルゲーム
```

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

