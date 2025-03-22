"""
テキストのベクトル化ユーティリティ
OpenAI APIを使用してテキストをベクトル化する機能を提供します。
"""
import os
from typing import List, Union
import openai
from pathlib import Path

class TextEmbedder:
    def __init__(self, api_key: str = None):
        """
        TextEmbedderの初期化
        
        Args:
            api_key (str, optional): OpenAI APIキー。
                未指定の場合は環境変数OPENAI_API_KEYから読み込み
        """
        if api_key:
            openai.api_key = api_key
        elif os.getenv("OPENAI_API_KEY"):
            openai.api_key = os.getenv("OPENAI_API_KEY")
        else:
            raise ValueError("OpenAI APIキーが必要です。引数で指定するか環境変数OPENAI_API_KEYを設定してください。")

    def embed_text(self, text: str) -> List[float]:
        """
        単一のテキストをベクトル化

        Args:
            text (str): ベクトル化するテキスト

        Returns:
            List[float]: ベクトル化されたテキスト（1536次元）
        """
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        複数のテキストをベクトル化

        Args:
            texts (List[str]): ベクトル化するテキストのリスト

        Returns:
            List[List[float]]: ベクトル化されたテキストのリスト
        """
        response = openai.Embedding.create(
            input=texts,
            model="text-embedding-ada-002"
        )
        return [data['embedding'] for data in response['data']]

    def embed_file(self, file_path: Union[str, Path], split_char: str = "\n") -> List[List[float]]:
        """
        テキストファイルの内容をベクトル化

        Args:
            file_path (Union[str, Path]): テキストファイルのパス
            split_char (str, optional): テキストの分割文字。デフォルトは改行

        Returns:
            List[List[float]]: ベクトル化されたテキストのリスト
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"ファイルが見つかりません: {file_path}")
        
        with path.open('r', encoding='utf-8') as f:
            content = f.read()
            texts = [text.strip() for text in content.split(split_char) if text.strip()]
            return self.embed_texts(texts)
