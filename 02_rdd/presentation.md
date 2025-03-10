---
marp: true
theme: default
paginate: true
header: "Quantum Picture Book Service"
footer: "© 2024 Quantum Ani"
style: |
  section {
    font-family: 'Arial', sans-serif;
  }
  h1 {
    color: #2c3e50;
  }
  h2 {
    color: #34495e;
  }
---

# Quantum Picture Book
## パーソナライズ絵本生成サービス

---

# サービス概要 🎨

- 子供の**名前の由来**をストーリーの中心に据えた新しい形の絵本制作サービス
- **量子アニーリング**と**AI**を活用し、質の高い絵本を数分で生成
- 家族の想いを次世代に伝える新しいコミュニケーションツール

---

# 背景と課題 🤔

## 既存サービスの限界

- 名前の文字を物語に組み込む**表面的なカスタマイズ**
- 名前に込められた**本当の物語**が活かされていない
- 家族の想いを伝える機会が限られている

---

# 目的 🎯

## 名前に込められた想いを次世代に伝える

1. 親から子への想いをストーリー化
2. 名前を付けた際のエピソードの視覚化
3. 家族の歴史や願いの継承

## 日本の文化要素を活かした独自の世界観

- ひらがなベースのストーリー展開
- 日本的な象徴やモチーフの活用

---

# システムアーキテクチャ 🏗

```mermaid
graph TB
    subgraph "フロントエンド"
        UI[Webアプリケーション]
        UI --> |ユーザー入力| Forms[入力フォーム]
        UI --> |プレビュー| Preview[プレビュー画面]
        UI --> |編集| Editor[編集画面]
    end

    subgraph "バックエンド"
        API[APIサーバー]
        Auth[認証サービス]
        Cache[キャッシュ]
    end

    subgraph "生成エンジン"
        QA[量子アニーリング]
        AI_Text[テキスト生成AI]
        AI_Image[イラスト生成AI]
    end

    subgraph "データストア"
        DB[(メインDB)]
        Assets[(アセットDB)]
    end

    Forms --> |API呼び出し| API
    Preview --> |データ取得| API
    Editor --> |更新リクエスト| API

    API --> |認証| Auth
    API --> |データ取得/保存| Cache
    API --> |永続化| DB
    API --> |テンプレート取得| Assets

    API --> |構造最適化| QA
    API --> |テキスト生成| AI_Text
    API --> |イラスト生成| AI_Image

    QA --> |最適化結果| API
    AI_Text --> |生成テキスト| API
    AI_Image --> |生成イラスト| API

    Cache --> |キャッシュヒット| API
    DB --> |データ読み取り| API
    Assets --> |テンプレート| API
```

---

# 生成プロセス 🔄

```mermaid
flowchart TB
    Start([開始]) --> Input[/ユーザー入力データ/]
    
    subgraph "ストーリー構造決定"
        Input --> TemplateSelect{テンプレート選択}
        TemplateSelect --> |基本テンプレート| QA1[量子アニーリング処理]
        QA1 --> |最適化| Structure[ストーリー構造確定]
    end

    subgraph "テキスト生成"
        Structure --> CharacterMap[キャラクターマッピング]
        CharacterMap --> SceneDiv[シーン分割]
        SceneDiv --> AI1[AI文章生成]
        AI1 --> TextReview{テキスト確認}
        TextReview --> |OK| TextFix[テキスト確定]
        TextReview --> |NG| AI1
    end

    subgraph "イラスト生成"
        TextFix --> StyleSelect[スタイル選択]
        StyleSelect --> AI2[AIイラスト生成]
        AI2 --> ImageReview{イラスト確認}
        ImageReview --> |OK| ImageFix[イラスト確定]
        ImageReview --> |NG| AI2
    end

    Complete([完了])

    style Start fill:#9f9,stroke:#6e6
    style Complete fill:#9f9,stroke:#6e6
```

---

# 実装フロー 🔍

```mermaid
sequenceDiagram
    actor User as ユーザー
    participant Web as Webアプリ
    participant API as APIサーバー
    participant QA as 量子アニーリング
    participant AI as AI生成エンジン
    participant DB as データベース

    User->>Web: 基本情報入力
    Note over User,Web: 子供の名前、性別、生年月日

    User->>Web: 名前の由来情報入力
    Note over User,Web: 由来、願い、エピソード

    Web->>API: 絵本生成リクエスト
    API->>QA: ストーリー構造最適化
    QA-->>API: 最適化されたストーリー構造
    API->>AI: コンテンツ生成
    AI-->>API: 生成結果
    API-->>Web: プレビューデータ
    Web-->>User: プレビュー表示
```

---

# 主な特徴 ✨

## 1. 量子アニーリングによる最適化
- ストーリー構造の最適化
- レイアウトの最適化
- パフォーマンス要件：生成時間3秒以内

## 2. AIによる高品質コンテンツ生成
- 自然な文章生成
- クオリティの高いイラスト生成
- 日本語・日本文化への適応

## 3. カスタマイズ性
- 複数のストーリーパターン
- キャラクター選択
- 背景シーンのカスタマイズ

---

# 今後の展開 🚀

## 短期目標
- β版リリース（2024年第2四半期）
- ユーザーフィードバックの収集
- 生成エンジンの改善

## 中長期目標
- 多言語対応
- 実店舗との連携
- プラットフォームの拡張

---

# ご清聴ありがとうございました 🙏

お問い合わせ：
contact@quantum-ani.com
