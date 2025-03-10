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

    subgraph "レイアウト最適化"
        ImageFix --> QA2[量子アニーリング処理]
        QA2 --> LayoutOpt[レイアウト最適化]
        LayoutOpt --> FinalCheck{最終確認}
        FinalCheck --> |OK| Complete
        FinalCheck --> |修正必要| Revise[修正指示]
        Revise --> |テキスト修正| AI1
        Revise --> |イラスト修正| AI2
        Revise --> |構造修正| QA1
    end

    Complete([完了])

    style Start fill:#9f9,stroke:#6e6
    style Complete fill:#9f9,stroke:#6e6
    
    subgraph "凡例"
        direction LR
        L1[処理] --> L2{判断}
        L2 --> L3[/入力データ/]
    end
