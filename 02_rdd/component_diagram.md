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
