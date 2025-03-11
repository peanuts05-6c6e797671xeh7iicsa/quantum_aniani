# LLMプロンプト設計書

## 1. プロンプトの種類

### 1.1 ストーリーテキスト生成
```
あなたは子供向け絵本作家です。以下の要素に基づいて、[age]歳の子供向けの
物語を生成してください：

シーン情報：
- 場所：[location]
- 季節：[season]
- 導き手：[guide_name]（[guide_type]）
- テーマ：[theme]

制約条件：
- 40文字程度/ページ
- ひらがな主体
- [age]歳向けの語彙
- 明確な情景描写

出力形式：
{
  "text": "ストーリーテキスト",
  "emotions": ["感情1", "感情2"],
  "keywords": ["キーワード1", "キーワード2"]
}
```

### 1.2 イラスト生成プロンプト
```
以下の要素を含む子供向け絵本のイラストを生成するためのプロンプトを
作成してください：

シーン要素：
- 主人公：[age]歳の[gender]の子供
- 導き手：[guide_description]
- 場所：[location_description]
- 季節：[season_description]
- 感情：[emotion_list]

スタイル指定：
- 明るく温かみのある色調
- やわらかいタッチ
- 子供向けの親しみやすいデザイン
- 日本的な要素の自然な組み込み

出力形式：
{
  "prompt": "生成AI用プロンプト",
  "style_params": {
    "color_tone": "色調指定",
    "art_style": "画風指定",
    "composition": "構図指定"
  }
}
```

### 1.3 感情表現調整
```
以下のテキストを、指定された感情とトーンに調整してください：

原文：[original_text]

調整パラメータ：
- 感情強度：[1-5]
- 主要感情：[emotion]
- 年齢：[age]歳向け

制約条件：
- 原文の意味を保持
- 年齢に適した表現
- 自然な日本語

出力形式：
{
  "adjusted_text": "調整後テキスト",
  "emotion_level": "感情強度",
  "key_phrases": ["重要フレーズ1", "重要フレーズ2"]
}
```

## 2. プロンプトパラメータ

### 2.1 共通パラメータ
- age: 対象年齢（数値）
- gender: 性別（"男の子"/"女の子"）
- emotion_level: 感情強度（1-5）
- style_tone: 文体トーン（"やわらかい"/"元気"/"静か"等）

### 2.2 シーン固有パラメータ
- location: 場所情報
- season: 季節情報
- guide: 導き手情報
- theme: シーンテーマ
- weather: 天候情報

### 2.3 スタイルパラメータ
- color_scheme: 配色指定
- art_style: 画風指定
- composition: 構図指定
- mood: 雰囲気指定

## 3. 条件分岐ロジック

### 3.1 年齢による調整
```python
def adjust_for_age(age):
    if age <= 3:
        return {
            "vocabulary_level": "基本的な単語のみ",
            "sentence_length": "5-7語",
            "hiragana_only": True
        }
    elif age <= 6:
        return {
            "vocabulary_level": "基本+一部の漢字",
            "sentence_length": "10-15語",
            "hiragana_only": False
        }
    else:
        return {
            "vocabulary_level": "標準的",
            "sentence_length": "15-20語",
            "hiragana_only": False
        }
```

### 3.2 感情強度による調整
```python
def adjust_emotion_level(level):
    return {
        1: {"intensity": "とても穏やか", "expressions": ["そっと", "やさしく"]},
        2: {"intensity": "穏やか", "expressions": ["ゆっくり", "のんびり"]},
        3: {"intensity": "標準", "expressions": ["元気に", "楽しく"]},
        4: {"intensity": "活発", "expressions": ["わくわく", "どきどき"]},
        5: {"intensity": "とても活発", "expressions": ["すごく", "とても"]}
    }[level]
```

## 4. プロンプト生成関数

### 4.1 ストーリープロンプト生成
```python
def generate_story_prompt(scene_info, age, emotion_level):
    age_params = adjust_for_age(age)
    emotion_params = adjust_emotion_level(emotion_level)
    
    return {
        "base_prompt": "子供向け絵本のストーリー",
        "scene": scene_info,
        "constraints": {
            **age_params,
            **emotion_params,
            "max_length": 40
        }
    }
```

### 4.2 イラストプロンプト生成
```python
def generate_illustration_prompt(scene_info, style_params):
    return {
        "base_prompt": "子供向け絵本のイラスト",
        "scene": scene_info,
        "style": style_params,
        "constraints": {
            "style": "日本的",
            "tone": "明るい",
            "complexity": "simple"
        }
    }
```

## 5. 品質チェック

### 5.1 テキスト品質評価
- 文字数制限の遵守
- 年齢適合性
- 感情表現の適切さ
- 物語の一貫性

### 5.2 イラスト品質評価
- 年齢適合性
- 色使いの適切さ
- 構図の明確さ
- キャラクターの表現

## 6. エラー処理

### 6.1 再生成条件
- 文字数超過
- 不適切な表現
- 感情強度ミスマッチ
- スタイル逸脱

### 6.2 調整アプローチ
- パラメータの微調整
- 制約の緩和/強化
- 代替表現の使用

## 7. 統合例

### 7.1 シーン生成の完全な例
```python
def generate_complete_scene(scene_info, age, style_params):
    # ストーリーの生成
    story_prompt = generate_story_prompt(scene_info, age, 3)
    story = generate_story(story_prompt)
    
    # 感情の調整
    adjusted_story = adjust_emotions(story, scene_info["emotion"])
    
    # イラストプロンプトの生成
    illustration_prompt = generate_illustration_prompt(
        scene_info,
        style_params
    )
    
    return {
        "story": adjusted_story,
        "illustration_prompt": illustration_prompt
    }
```

### 7.2 品質チェック統合
```python
def quality_check_scene(scene):
    text_quality = check_text_quality(scene["story"])
    illustration_quality = check_illustration_prompt(
        scene["illustration_prompt"]
    )
    
    if text_quality["score"] < 0.7 or illustration_quality["score"] < 0.7:
        return generate_complete_scene(
            scene["info"],
            scene["age"],
            scene["style"]
        )
    
    return scene
