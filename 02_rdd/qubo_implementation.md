# QUBO実装設計書

## 1. 最適化の目的
子供の名前の由来とメッセージを活かした、整合性の取れた絵本ストーリーの生成

## 2. QUBO行列の構造

### 2.1 基本構造
```python
Q[i,j] = Σ(w_k * coherence_k(i,j))
```

### 2.2 重み付けパラメータ
- w1: 導き手×ステージ整合性の重み
- w2: メッセージ分散度の重み
- w3: ストーリー展開整合性の重み
- w4: ページ間連続性の重み

## 3. 整合性評価関数

### 3.1 導き手×ステージ整合性 (w1)
```python
def character_stage_coherence(character, stage):
    score = 0
    # 季節との適合性
    score += season_compatibility(character.season, stage.season)
    # 場所との相性
    score += location_compatibility(character.type, stage.location)
    # メッセージとの調和
    score += message_compatibility(character.traits, stage.theme)
    return score
```

### 3.2 メッセージ分散度 (w2)
```python
def message_distribution_coherence(messages):
    score = 0
    # メッセージの重複チェック
    score += check_message_uniqueness(messages)
    # テーマの一貫性
    score += evaluate_theme_consistency(messages)
    # メッセージの分散度
    score += calculate_message_distribution(messages)
    return score
```

### 3.3 ストーリー展開整合性 (w3)
```python
def story_coherence(story_progression, stage):
    score = 0
    # 展開強度と環境のマッチング
    score += match_progression_environment(story_progression, stage)
    # 感情表現と季節感の整合性
    score += evaluate_emotional_seasonal_match(story_progression, stage)
    return score
```

### 3.4 ページ間連続性 (w4)
```python
def page_continuity(current_page, next_page):
    score = 0
    # 場面転換の自然さ
    score += evaluate_transition_smoothness(current_page, next_page)
    # キャラクターの一貫性
    score += check_character_consistency(current_page, next_page)
    # メッセージの流れ
    score += evaluate_message_flow(current_page, next_page)
    return score
```

## 4. 制約条件

### 4.1 ハード制約
- 同一キャラクターの連続登場を制限
- 極端な季節の変化を防止
- 必須メッセージの包含を保証

### 4.2 ソフト制約
- キャラクターの多様性を推奨
- メッセージの均等な分散を推奨
- 場面展開の自然な流れを推奨

## 5. 最適化プロセス

### 5.1 初期化
1. ユーザー入力の解析
   - 名前の分解
   - メッセージの抽出
   - 希望する要素の特定

2. 候補プールの生成
   - 適切なキャラクターの選定
   - 可能なステージの列挙
   - メッセージのバリエーション作成

### 5.2 QUBO行列の構築
1. 変数の定義
   - キャラクター選択変数
   - ステージ設定変数
   - メッセージ配置変数

2. 制約の実装
   - ハード制約の重み付け
   - ソフト制約の係数設定

### 5.3 最適化実行
1. 量子アニーリングによる解の探索
2. 結果の後処理
3. 整合性スコアの確認

## 6. 品質評価

### 6.1 評価指標
- 整合性スコア（0-1の範囲）
- メッセージカバレッジ率
- キャラクター分散度
- ストーリー展開の自然さ

### 6.2 閾値設定
- 最小許容整合性スコア: 0.7
- 最小メッセージカバレッジ: 80%
- 最小キャラクター分散度: 0.6

### 6.3 再生成トリガー
- 整合性スコアが閾値未満
- メッセージカバレッジ不足
- キャラクター分散度不足

## 7. 実装例

### 7.1 キャラクター×季節の整合性マトリクス
```python
season_compatibility = {
    'ネズミ': {'冬': 1.0, '春': 0.7, '夏': 0.3, '秋': 0.5},
    'ウサギ': {'春': 1.0, '夏': 0.7, '秋': 0.5, '冬': 0.3},
    'トラ': {'夏': 1.0, '春': 0.7, '秋': 0.5, '冬': 0.3},
    # ... 他のキャラクター
}
```

### 7.2 メッセージ分散評価
```python
def evaluate_message_distribution(messages):
    # メッセージの種類をカウント
    message_types = Counter([msg.type for msg in messages])
    # 分散度を計算
    distribution_score = 1 - (std(message_types.values()) / mean(message_types.values()))
    return distribution_score
```

### 7.3 ストーリー展開評価
```python
def evaluate_story_progression(current, next):
    # 展開の強度変化を計算
    intensity_change = abs(current.intensity - next.intensity)
    # 場面転換の自然さを評価
    transition_score = 1 - (intensity_change / max_intensity)
    return transition_score
```

## 8. 最適化の実行フロー

1. ユーザー入力の受け取り
   - 名前（ひらがな）
   - 名前の由来
   - メッセージ

2. 初期候補の生成
   - キャラクター候補プール作成
   - ステージ候補プール作成
   - メッセージ変換候補作成

3. QUBO行列の構築
   - 変数エンコーディング
   - 制約条件の実装
   - 目的関数の設定

4. 量子アニーリング実行
   - 最適解の探索
   - 結果のデコード
   - 品質評価

5. 結果の後処理
   - 整合性チェック
   - 必要に応じて再最適化
   - 最終結果の出力
