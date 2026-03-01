author: Shibao,Tetsuya
summary: AWS CloudShell / GitHub Codespaces で AWS CLI を使い始める環境構築ハンズオン
id: 00-Install-AWS-CLI-to-RPI
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# AWS CLI 環境構築ハンズオン — CloudShell & GitHub Codespaces

## はじめに
Duration: 0:03:00

### ハンズオンの概要

このハンズオンでは、AWS CLI を使い始めるための環境を構築します。  
ローカルPCへのインストールは不要で、以下の2つの方法を紹介します。

| 方法 | 特徴 |
|------|------|
| **AWS CloudShell** | AWSマネジメントコンソールからすぐに使えるブラウザベースのシェル。AWS CLI v2がプリインストール済み |
| **GitHub Codespaces** | GitHubリポジトリと連携したクラウド開発環境。AWS CLIを手動インストール |

### 前提条件

* AWSアカウントを持っていること
* GitHubアカウントを持っていること（Codespaces利用時）
* Webブラウザが利用できること

Positive
: どちらの方法もブラウザだけで完結します。ローカルPCの環境を汚さずにAWS CLIを試せます。

## 方法1: AWS CloudShell を使う
Duration: 0:05:00

### CloudShell とは

AWS CloudShell は、AWSマネジメントコンソール内で利用できるブラウザベースのシェル環境です。  
AWS CLI v2がプリインストールされており、追加のインストール作業は不要です。

### CloudShell の起動

1. [AWSマネジメントコンソール](https://console.aws.amazon.com/) にログインします
2. 画面上部のナビゲーションバーにある **CloudShell アイコン**（`>_` マーク）をクリックします
3. 初回起動時はシェル環境の準備に1〜2分かかります

### AWS CLI のバージョン確認

CloudShell が起動したら、AWS CLI がインストール済みであることを確認します。

```console
aws --version
```

以下のような出力が表示されます。

```
aws-cli/2.x.x Python/3.x.x Linux/x.x.x source/x86_64.amzn.2023
```

Positive
: CloudShell では AWS CLI v2 がプリインストールされています。ログイン中のIAMユーザー/ロールの権限で自動的に認証されるため、`aws configure` も不要です。

### CloudShell の特徴

| 項目 | 内容 |
|------|------|
| AWS CLI | v2 プリインストール済み |
| 認証 | ログイン中のIAMユーザー/ロールで自動認証 |
| ストレージ | ホームディレクトリに1GBの永続ストレージ |
| タイムアウト | 20〜30分間操作がないと自動切断 |
| リージョン | コンソールで選択中のリージョンが適用 |
| コスト | 無料 |

### 動作確認

いくつかのコマンドを実行して、正常に動作することを確認します。

```console
# 現在のIAMユーザー/ロールを確認
aws sts get-caller-identity

# S3バケットの一覧を表示
aws s3 ls

# 現在のリージョンを確認
aws configure get region
```

Negative
: CloudShell はAWSマネジメントコンソールのセッションに依存します。コンソールからログアウトするとシェルも終了します。また、一部のリージョンではCloudShellが利用できない場合があります。

## 方法2: GitHub Codespaces を使う
Duration: 0:10:00

### GitHub Codespaces とは

GitHub Codespaces は、GitHub上でクラウドベースの開発環境を提供するサービスです。  
VS Codeベースのエディタがブラウザ上で動作し、ターミナルも利用できます。

### Codespace の作成

1. [GitHub](https://github.com/) にログインします
2. 任意のリポジトリを開きます（新規作成でも可）
3. **Code** ボタン → **Codespaces** タブ → **Create codespace on main** をクリックします
4. Codespace の起動を待ちます（1〜2分程度）

Positive
: GitHub Free プランでは、毎月120コア時間のCodespaces無料枠が提供されています。2コアマシンの場合、月60時間利用可能です。

### AWS CLI v2 のインストール

Codespace のターミナルで以下のコマンドを実行して、AWS CLI v2 をインストールします。

```console
# インストーラーのダウンロード
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# 解凍
unzip awscliv2.zip

# インストール
sudo ./aws/install

# インストール確認
aws --version
```

以下のような出力が表示されればインストール完了です。

```
aws-cli/2.x.x Python/3.x.x Linux/x.x.x source/x86_64.ubuntu
```

### 不要ファイルの削除

インストール後、不要なファイルを削除します。

```console
rm -rf awscliv2.zip aws/
```

Positive
: Codespace を停止・再起動してもインストール済みの AWS CLI は保持されます。ただし、Codespace を削除した場合は再インストールが必要です。

## AWS CLI の初期設定
Duration: 0:05:00

### 認証方法の選択

AWS CLI で AWS リソースを操作するには、認証情報の設定が必要です。

| 方法 | 対象環境 | 説明 |
|------|---------|------|
| CloudShell 自動認証 | CloudShell | 設定不要。ログイン中の権限で自動認証 |
| `aws configure` | Codespaces 等 | アクセスキーとシークレットキーを設定 |
| 環境変数 | Codespaces 等 | 環境変数にアクセスキーを設定（一時利用向き） |

### aws configure による設定（Codespaces 向け）

GitHub Codespaces では `aws configure` コマンドで認証情報を設定します。

```console
aws configure
```

以下の情報を入力します。

| 項目 | 値 |
|------|-----|
| AWS Access Key ID | `AKIAXXXXXXXXXXXXXXXX`（管理者から払い出されたもの） |
| AWS Secret Access Key | `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` |
| Default region name | `ap-northeast-1` |
| Default output format | `json` |

### 設定の確認

```console
# 設定ファイルの確認
cat ~/.aws/config

# 認証情報ファイルの確認（中身は表示しない）
ls -la ~/.aws/credentials

# 現在のIAMユーザーを確認
aws sts get-caller-identity
```

Negative
: アクセスキーとシークレットキーは管理者から払い出されたものを設定してください。キーをGitリポジトリにコミットしないよう注意してください。

### 環境変数による設定（一時利用向け）

一時的に利用する場合は、環境変数で認証情報を設定することもできます。

```console
export AWS_ACCESS_KEY_ID="AKIAXXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
export AWS_DEFAULT_REGION="ap-northeast-1"
```

Positive
: 環境変数による設定はターミナルを閉じると消えるため、一時的な利用に適しています。Codespace の Secrets 機能を使えば、安全に環境変数を永続化することもできます。

## Codespace Secrets の活用（推奨）
Duration: 0:05:00

### Codespace Secrets とは

GitHub Codespace Secrets を使うと、AWS の認証情報を安全にCodespace に設定できます。  
Secrets はCodespace 起動時に環境変数として自動的に読み込まれます。

### Secrets の設定方法

1. GitHubの **Settings** → **Codespaces** を開きます
2. **Codespace secrets** セクションの **New secret** をクリックします
3. 以下の3つの Secret を追加します

| Name | Value |
|------|-------|
| `AWS_ACCESS_KEY_ID` | `AKIAXXXXXXXXXXXXXXXX` |
| `AWS_SECRET_ACCESS_KEY` | `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` |
| `AWS_DEFAULT_REGION` | `ap-northeast-1` |

4. それぞれの Secret で、利用するリポジトリを選択して **Add secret** をクリックします

### 設定の確認

Codespace を再起動（または新規作成）した後、環境変数が設定されていることを確認します。

```console
# 環境変数の確認（キーの先頭数文字のみ表示）
echo "Region: $AWS_DEFAULT_REGION"
echo "Key ID: ${AWS_ACCESS_KEY_ID:0:8}..."

# AWS CLI での確認
aws sts get-caller-identity
```

Positive
: Codespace Secrets を使えば、`aws configure` を毎回実行する必要がなく、認証情報がGitリポジトリに漏洩するリスクもありません。

Negative
: Codespace Secrets に保存したアクセスキーが漏洩した場合に備え、IAMユーザーには最小権限のポリシーを設定しましょう。また、定期的なキーローテーションも推奨されます。

## 動作確認テスト
Duration: 0:05:00

### CloudShell / Codespaces の共通テスト

どちらの環境でも以下のコマンドが正常に実行できることを確認します。

### IAM情報の確認

```console
aws sts get-caller-identity
```

```json
{
    "UserId": "AIDAXXXXXXXXXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/your-username"
}
```

### S3操作の確認

```console
# バケット一覧
aws s3 ls

# テスト用バケットの作成（任意）
aws s3 mb s3://handson-test-{あなたのアカウントID}

# ファイルのアップロード
echo "Hello AWS CLI" > test.txt
aws s3 cp test.txt s3://handson-test-{あなたのアカウントID}/

# ファイルの確認
aws s3 ls s3://handson-test-{あなたのアカウントID}/

# テスト用バケットの削除
aws s3 rm s3://handson-test-{あなたのアカウントID}/ --recursive
aws s3 rb s3://handson-test-{あなたのアカウントID}
```

### リージョンの確認

```console
aws ec2 describe-regions --query "Regions[].RegionName" --output table
```

Positive
: ここまでの操作がすべて成功すれば、AWS CLI の環境構築は完了です。他のハンズオン（09〜12）を進める準備が整いました。

## 2つの方法の比較とまとめ
Duration: 0:02:00

### CloudShell vs GitHub Codespaces

| 比較項目 | CloudShell | GitHub Codespaces |
|----------|-----------|-------------------|
| 起動方法 | AWSコンソールからワンクリック | GitHubリポジトリから作成 |
| AWS CLI | プリインストール済み | 手動インストール |
| 認証設定 | 自動（設定不要） | `aws configure` または Secrets |
| エディタ | なし（CLIのみ） | VS Code（フルエディタ） |
| ストレージ | 1GB（永続） | 最大32GB（Codespace 単位） |
| コスト | 無料 | 月120コア時間まで無料 |
| 向いている用途 | AWS CLI の実行のみ | コード開発 + AWS CLI |

### 使い分けの指針

* **AWS CLI でサクッとコマンドを実行したい** → CloudShell
* **コードの開発・編集も一緒に行いたい** → GitHub Codespaces

Positive
: AWS CLI はGUIと比較して、再現性の高い作業が可能です。ここで構築した環境を使って、他のハンズオンに進みましょう。

### 参考リンク

<button>
  [AWS CloudShell ドキュメント](https://docs.aws.amazon.com/ja_jp/cloudshell/)
</button>

<button>
  [AWS CLI v2 インストールガイド](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html)
</button>

<button>
  [GitHub Codespaces ドキュメント](https://docs.github.com/ja/codespaces)
</button>