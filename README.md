# 量子アニーリングプロジェクト 初期セットアップ (ここまではnosionに書くか)



## 1. 全体概要
- 量子アニーリングのアプリケーション開発を目指すプロジェクト
- **企画段階～実装段階まで** 一貫して GitHub でドキュメント・コードを管理
- チーム全員が **VSCode** or **Cursor** と **GitHub** を使って作業

## 2. 準備（インストール・アカウント作成）

### 2.1 エディタのセットアップ
#### VSCode または Cursor のインストール
1. 公式サイトからダウンロード
   - VSCode: https://code.visualstudio.com/
   - Cursor: https://cursor.sh/


### 2.2 GitHubアカウントの準備
1. アカウント作成
   - [GitHub公式](https://github.com/) にアクセス
   - 「Sign up」からメールアドレスで登録
   - ユーザー名は実名である必要はないが、チーム内で誰か分かるものを推奨

2. 二要素認証の設定（推奨）
   - Settings → Security → Two-factor authentication
   - スマートフォンアプリまたはSMSで設定可能

3. チームリポジトリへのアクセス権取得
   - リポジトリ管理者に GitHub アカウント名を連絡 (discordを活用してください！)
   - Collaborator として招待されるのを待つ
   - メールまたはGitHub通知から招待を承認

### 2.3 Gitのセットアップ
1. Gitのインストール
   - Windows: https://git-scm.com/download/win
   - Mac: `brew install git`
   - Linux: `sudo apt install git`

2. 初期設定
   ```bash
   # ユーザー名とメールアドレスの設定
   git config --global user.name "あなたの名前"
   git config --global user.email "あなたのメールアドレス"

   # 日本語ファイル名の文字化け防止
   git config --global core.quotepath false
   ```

### 2.4 リポジトリのクローン
 SSHでクローン
   - SSH鍵の生成
     ```bash
     # SSH鍵を生成
     ssh-keygen -t ed25519 -C "あなたのメールアドレス"
     ```
   - 公開鍵をGitHubに登録
     - Settings → SSH and GPG keys → New SSH key
   - クローン
     ```bash
     git clone git@github.com:組織名/リポジトリ名.git
     ```


これで基本的な開発環境のセットアップは完了です。
実際の開発手順については、`01_planning/README.md`を参照してください。
