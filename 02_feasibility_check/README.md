# テキストベクトル化ユーティリティ

OpenAI APIを使用してテキストをベクトル化するユーティリティです。キャラクター情報やメッセージなどのテキストデータを数値ベクトルに変換し、類似度計算や機械学習での利用を可能にします。

## 必要条件

- Python 3.7以上
- OpenAI APIキー
- openaiパッケージ

```bash
pip install openai
```

## 使用方法と具体例

### 1. 初期化

```python
from embedding_utils import TextEmbedder

# APIキーを直接指定
embedder = TextEmbedder(api_key="your-api-key")

# または環境変数から読み込み
# export OPENAI_API_KEY="your-api-key"
embedder = TextEmbedder()
```

### 2. 単一のキャラクター情報をベクトル化

```python
# キャラクター情報の例
character_info = """
名前：量子くん
性格：好奇心旺盛で明るい
特徴：量子力学を愛する小学生。いつも不思議な実験に夢中。
"""

vector = embedder.embed_text(character_info)
print(f"ベクトルの次元数: {len(vector)}")  # 1536
print(f"最初の5次元: {vector[:5]}")  # 例: [-0.023, 0.015, -0.007, 0.028, 0.011]
```

### 3. 複数のキャラクター情報をベクトル化

```python
characters = [
    "量子くん：好奇心旺盛で明るい性格の小学生。量子力学を愛する。",
    "波動ちゃん：おっとりした性格で、波動方程式が得意。量子くんの親友。",
    "エントロピー先生：物理学者で量子くんたちの指導者。いつも熱力学の話で盛り上がる。"
]

vectors = embedder.embed_texts(characters)
print(f"キャラクター数: {len(vectors)}")  # 3
print(f"各ベクトルの次元数: {len(vectors[0])}")  # 1536
```

### 4. キャラクターファイルの内容をベクトル化

例えば、以下のような形式のテキストファイルがある場合：

```text
# docs/data/characters.txt の例
量子くん：好奇心旺盛で明るい性格の小学生。量子力学を愛する。
波動ちゃん：おっとりした性格で、波動方程式が得意。量子くんの親友。
エントロピー先生：物理学者で量子くんたちの指導者。いつも熱力学の話で盛り上がる。
```

このファイルを読み込んでベクトル化：

```python
# 改行で区切られたテキストファイルを読み込む
vectors = embedder.embed_file("docs/data/characters.txt")

# または、カスタム区切り文字（|など）で区切られたファイルを読み込む
vectors = embedder.embed_file("docs/data/messages.txt", split_char="|")

# 出力されるデータ形式
print(f"ベクトル数: {len(vectors)}")  # ファイル内の行数（この例では3）
print(f"各ベクトルの形式: {len(vectors[0])}次元の浮動小数点数配列")  # 1536次元
```

## ベクトルの活用例

生成されたベクトルは以下のような用途に活用できます：

1. キャラクター間の類似度計算
```python
from numpy import dot
from numpy.linalg import norm

def cosine_similarity(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))

# 量子くんと波動ちゃんの類似度を計算
similarity = cosine_similarity(vectors[0], vectors[1])
print(f"類似度: {similarity}")  # 0.0～1.0の値
```

2. キャラクターの検索
```python
# 「物理学に詳しい」キャラクターを検索
query = "物理学に詳しい先生"
query_vector = embedder.embed_text(query)

# 各キャラクターとの類似度を計算
similarities = [cosine_similarity(query_vector, v) for v in vectors]
most_similar_idx = similarities.index(max(similarities))
print(f"最も近いキャラクター: {characters[most_similar_idx]}")
```

## 注意事項

- OpenAI APIの利用には課金が発生します
- 大量のテキストを処理する場合はAPIの利用制限に注意してください
- ベクトル化されたテキストは1536次元の浮動小数点数配列として返されます
- 返されるベクトルの各次元の値は通常-1.0から1.0の範囲に正規化されています
