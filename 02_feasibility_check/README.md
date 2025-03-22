# Embedding
OpenAI APIを使用してテキストをベクトル化するやり方です。テキストファイルや文字列をベクトル化し、数学的な処理が可能な形式に変換します。

## 必要条件

- Python 3.7以上
- OpenAI APIキー
- openaiパッケージ

```bash
pip install openai
```

## 使用方法

### 1. 初期化

```python
from embedding_utils import TextEmbedder

# APIキーを直接指定
embedder = TextEmbedder(api_key="your-api-key")

# または環境変数から読み込み
# export OPENAI_API_KEY="your-api-key"
embedder = TextEmbedder()
```

### 2. 単一のテキストをベクトル化

```python
text = "こんにちは、世界！"
vector = embedder.embed_text(text)
# 1536次元のベクトルが返されます
```

### 3. 複数のテキストをベクトル化

```python
texts = [
    "こんにちは、世界！",
    "AIの世界へようこそ",
    "量子コンピュータについて学びましょう"
]
vectors = embedder.embed_texts(texts)
# テキストごとに1536次元のベクトルが返されます
```

### 4. テキストファイルの内容をベクトル化

```python
# デフォルトでは改行で分割
vectors = embedder.embed_file("docs/data/characters.txt")

# カスタム区切り文字を指定
vectors = embedder.embed_file("docs/data/messages.txt", split_char="|")
```

## 注意事項

- OpenAI APIの利用には課金が発生します
- 大量のテキストを処理する場合はAPIの利用制限に注意してください
