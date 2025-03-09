# Quantum Picture Book システム設計書

## 1. システムアーキテクチャ

### 1.1 全体構成
```
[クライアント]
    │
    ├── [Webアプリケーション]
    │   ├── 入力フォーム
    │   ├── プレビューシステム
    │   └── 編集インターフェース
    │
    ├── [APIサーバー]
    │   ├── ストーリー生成エンジン
    │   ├── 画像生成エンジン
    │   └── データ管理システム
    │
    └── [データストア]
        ├── ユーザーDB
        ├── コンテンツDB
        └── 素材ストレージ
```

### 1.2 コンポーネント詳細
1. Webアプリケーション
   - React.js + TypeScript
   - Next.js（SSR対応）
   - Tailwind CSS（UIフレームワーク）
   - Three.js（3Dプレビュー用）

2. APIサーバー
   - Node.js + Express
   - Python（AI/ML処理用）
   - GraphQL API

3. データストア
   - PostgreSQL（メインDB）
   - Redis（キャッシュ）
   - Amazon S3（画像ストレージ）

## 2. データベース設計

### 2.1 ユーザーDB
```sql
-- users テーブル
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- profiles テーブル
CREATE TABLE profiles (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    child_name VARCHAR(100) NOT NULL,
    child_name_kana VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    gender VARCHAR(10),
    avatar_id UUID,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- name_stories テーブル
CREATE TABLE name_stories (
    id UUID PRIMARY KEY,
    profile_id UUID REFERENCES profiles(id),
    name_origin TEXT NOT NULL,
    wishes TEXT,
    special_episode TEXT,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);
```

### 2.2 コンテンツDB
```sql
-- characters テーブル
CREATE TABLE characters (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL, -- 干支/自然/気象/植物
    description TEXT,
    image_path VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- story_templates テーブル
CREATE TABLE story_templates (
    id UUID PRIMARY KEY,
    category VARCHAR(50) NOT NULL, -- 起/承/転/結
    content_template TEXT NOT NULL,
    variables JSONB,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- scenes テーブル
CREATE TABLE scenes (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    background_path VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);
```

### 2.3 生成物DB
```sql
-- books テーブル
CREATE TABLE books (
    id UUID PRIMARY KEY,
    profile_id UUID REFERENCES profiles(id),
    status VARCHAR(50) NOT NULL, -- draft/preview/published
    content JSONB NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- pages テーブル
CREATE TABLE pages (
    id UUID PRIMARY KEY,
    book_id UUID REFERENCES books(id),
    page_number INTEGER NOT NULL,
    content JSONB NOT NULL,
    scene_id UUID REFERENCES scenes(id),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);
```

## 3. APIエンドポイント設計

### 3.1 ユーザー管理API
```graphql
type User {
    id: ID!
    email: String!
    profile: Profile
    books: [Book]
}

type Profile {
    id: ID!
    childName: String!
    childNameKana: String!
    birthDate: Date!
    gender: String
    avatar: Avatar
    nameStory: NameStory
}

type Mutation {
    createUser(input: CreateUserInput!): User
    updateProfile(input: UpdateProfileInput!): Profile
    createNameStory(input: CreateNameStoryInput!): NameStory
}
```

### 3.2 ストーリー生成API
```graphql
type Book {
    id: ID!
    profile: Profile!
    status: BookStatus!
    pages: [Page]!
}

type Page {
    id: ID!
    pageNumber: Int!
    content: PageContent!
    scene: Scene!
}

type Mutation {
    generateStory(input: GenerateStoryInput!): Book
    updatePage(input: UpdatePageInput!): Page
    publishBook(bookId: ID!): Book
}
```

### 3.3 画像生成API
```graphql
type Scene {
    id: ID!
    name: String!
    background: String!
    characters: [Character]!
}

type Character {
    id: ID!
    name: String!
    category: CharacterCategory!
    image: String!
}

type Mutation {
    generatePageImage(input: GeneratePageImageInput!): String
    updateSceneLayout(input: UpdateSceneLayoutInput!): Scene
}
```

## 4. セキュリティ設計

### 4.1 認証・認可
- JWT（JSON Web Token）による認証
- Role-based Access Control（RBAC）
- OAuth2.0によるソーシャルログイン

### 4.2 データ保護
- AES-256による個人情報の暗号化
- HTTPS通信の強制
- CSRFトークンの実装

### 4.3 監視・ロギング
- AWS CloudWatchによるログ管理
- Sentryによるエラー監視
- Datadogによるパフォーマンス監視

## 5. デプロイメント設計

### 5.1 インフラストラクチャ
- AWS ECS（コンテナオーケストレーション）
- AWS RDS（データベース）
- AWS ElastiCache（Redisキャッシュ）
- AWS S3（静的アセット）
- CloudFront（CDN）

### 5.2 CI/CD
- GitHub Actions
- Docker
- Terraform（IaC）

### 5.3 環境構成
- 開発環境（Development）
- ステージング環境（Staging）
- 本番環境（Production）

## 6. パフォーマンス最適化

### 6.1 フロントエンド
- コード分割（Code Splitting）
- 画像の最適化
- キャッシュ戦略
- プログレッシブローディング

### 6.2 バックエンド
- クエリ最適化
- キャッシュ層の実装
- 非同期処理
- バッチ処理

### 6.3 インフラストラクチャ
- オートスケーリング
- ロードバランシング
- CDNの活用
- データベースレプリケーション
