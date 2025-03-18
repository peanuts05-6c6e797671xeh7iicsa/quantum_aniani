# 量子アニーリングプロジェクト

## 1. 全体概要
- 量子アニーリングのアプリケーション開発を目指すプロジェクト
- **企画段階～実装段階まで** 一貫して GitHub でドキュメント・コードを管理
- チーム全員が **VSCode** or **Cursor** と **GitHub** を使って作業
- 将来的なDocker利用を見据え、Windows環境ではWSL2を使用

## 2. 準備（インストール・アカウント作成）

### 2.1 Windows環境のセットアップ（Windows ユーザーのみ）
1. WSL2のインストール
   ```powershell
   # PowerShellを管理者として実行
   wsl --install
   ```
   - インストール後、PCの再起動が必要です
   - 再起動後、Ubuntuの初期設定が自動的に開始します
   - ユーザー名とパスワードを設定してください

2. Ubuntuのセットアップ
   - パッケージの更新
     ```bash
     sudo apt update
     sudo apt upgrade
     ```
   - 開発に必要なパッケージのインストール
     ```bash
     sudo apt install build-essential curl wget
     ```

3. WSLの基本的な使い方
   - Windowsのファイルは `/mnt/c/` などでアクセス可能
   - ホームディレクトリは `~` または `/home/ユーザー名/`
   - 開発作業は基本的にWSL内のディレクトリで行う

### 2.2 エディタのセットアップ
1. VSCode または Cursor のインストール
   - VSCode: https://code.visualstudio.com/
   - Cursor: https://cursor.sh/

2. WSL用の拡張機能（Windows環境）
   - Remote Development
     - WSL内のファイルをVSCodeで直接編集可能
     - ターミナルもWSL環境を使用可能
     - インストール後、左下の緑のボタンからWSLに接続

3. 一般的な推奨拡張機能
   - GitHub Pull Requests and Issues
     - GitHubとの連携が便利に
     - PRのレビューやIssueの確認が可能
   - markdownlint
     - Markdownの文法チェック
     - 一貫性のある文書作成を支援
   - GitLens
     - Gitの履歴を詳細に確認可能
     - 変更箇所の追跡が容易に

### 2.3 GitHubアカウントの準備
1. アカウント作成
   - [GitHub公式](https://github.com/) にアクセス
   - 「Sign up」からメールアドレスで登録
   - ユーザー名は実名である必要はないが、チーム内で誰か分かるものを推奨

2. 二要素認証の設定（推奨）
   - Settings → Security → Two-factor authentication
   - スマートフォンアプリまたはSMSで設定可能

3. チームリポジトリへのアクセス権取得
   - リポジトリ管理者に GitHub アカウント名を連絡
   - Collaborator として招待されるのを待つ
   - メールまたはGitHub通知から招待を承認

### 2.4 Gitのセットアップ
1. Gitのインストール
   - Windows (WSL): `sudo apt install git`
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

### 2.5 リポジトリのクローン
1. SSHでクローン（推奨）
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

### 2.6 動作確認
1. リポジトリに移動
   ```bash
   cd リポジトリ名
   ```

2. ブランチの確認
   ```bash
   # 現在のブランチを確認
   git branch
   
   # リモートブランチも含めて確認
   git branch -a
   ```

3. 簡単な変更を試してみる
   ```bash
   # テストブランチを作成
   git checkout -b test-名前-setup
   
   # 変更を加えてコミット
   git add .
   git commit -m "テスト: 初期セットアップの確認"
   
   # GitHubにプッシュ
   git push origin test-名前-setup
   ```

### 補足：WSLでの開発について
- WSLを使用することで、WindowsでもLinux環境での開発が可能
- 将来的なDocker利用も見据えた環境構築 (コード開発の時に環境を揃えます。この辺は.devcontainerファイルを私の方で用意して配布する予定です)
