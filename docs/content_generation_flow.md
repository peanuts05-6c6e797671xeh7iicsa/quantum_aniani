# コンテンツ生成フロー

```mermaid
flowchart TB
    subgraph Input["ユーザー入力"]
        A1[子供の基本情報]
        A2[名前の由来情報]
        A3[アバター選択]
    end

    subgraph MasterData["マスターデータ"]
        B1[キャラクター候補]
        B2[ステージ候補]
        B3[メッセージ候補]
        B4[大枠ストーリー]
    end

    subgraph QA["量子アニーリング処理"]
        C1[QUBO作成]
        C2[最適化計算]
        C3[舞台・設定決定]
    end

    subgraph LLM["LLM処理"]
        D1[セグメントストーリー生成]
        D2[各ページセンテンス生成]
    end

    subgraph AI["生成AI処理"]
        E1[各ページ絵生成]
    end

    %% 入力からの流れ
    A1 --> C1
    A2 --> C1
    A3 --> C1

    %% マスターデータからの流れ
    B1 --> C1
    B2 --> C1
    B3 --> C1
    B4 --> D1

    %% QA処理の流れ
    C1 --> C2
    C2 --> C3
    C3 --> D1

    %% LLM処理の流れ
    D1 --> D2
    D2 --> E1

    %% スタイル定義
    classDef input fill:#e1f5fe,stroke:#01579b
    classDef master fill:#fff3e0,stroke:#ff6f00
    classDef qa fill:#f3e5f5,stroke:#7b1fa2
    classDef llm fill:#e8f5e9,stroke:#2e7d32
    classDef ai fill:#fbe9e7,stroke:#d84315

    %% スタイル適用
    class A1,A2,A3 input
    class B1,B2,B3,B4 master
    class C1,C2,C3 qa
    class D1,D2 llm
    class E1 ai

```

## フロー説明

1. **ユーザー入力**
   - 子供の基本情報（名前、性別、生年月日）
   - 名前の由来情報（命名理由、願い、エピソード）
   - アバター選択

2. **マスターデータ参照**
   - キャラクター候補（干支、自然現象、日本の象徴的な植物など）
   - ステージ候補（海、森など）
   - メッセージ候補
   - 事前定義された大枠ストーリー

3. **量子アニーリング処理**
   - ユーザー入力とマスターデータに基づきQUBO作成
   - 最適化計算実行
   - 各セグメントの舞台・設定を決定

4. **LLM処理**
   - 量子アニーリングの結果と大枠ストーリーを基に詳細なストーリーを生成
   - ストーリーから各ページのセンテンスを生成

5. **生成AI処理**
   - セグメントストーリーとセンテンスに基づき、各ページの絵を生成
   - 絵柄の統一性を保持
