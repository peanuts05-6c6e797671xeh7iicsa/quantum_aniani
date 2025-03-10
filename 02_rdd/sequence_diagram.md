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

    User->>Web: カスタマイズ選択
    Note over User,Web: ストーリーパターン、キャラクター

    Web->>API: 絵本生成リクエスト

    API->>DB: テンプレート取得
    DB-->>API: テンプレートデータ

    API->>QA: ストーリー構造最適化
    QA-->>API: 最適化されたストーリー構造

    API->>AI: ストーリーテキスト生成
    AI-->>API: 生成されたテキスト

    API->>AI: イラスト生成
    AI-->>API: 生成されたイラスト

    API->>QA: レイアウト最適化
    QA-->>API: 最適化されたレイアウト

    API->>DB: 生成データ保存
    DB-->>API: 保存完了

    API-->>Web: プレビューデータ
    Web-->>User: プレビュー表示

    User->>Web: 確認・編集
    Web->>API: 修正リクエスト
    API-->>Web: 更新されたプレビュー
    Web-->>User: 最終確認

    User->>Web: 注文確定
    Web->>API: 注文処理
    API->>DB: 注文データ保存
    DB-->>API: 保存完了
    API-->>Web: 注文完了
    Web-->>User: 完了通知
