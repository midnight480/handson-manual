author: Shibao,Tetsuya
summary: GAS vs Lambda Function URL 比較から API Gateway + WAF + Lambda まで - サーバレスAPI構築の一気通貫ハンズオン
id: 12-AWS-handson-4-beginners-saga-serverlss-004
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# サーバレスAPIの構築と保護 - GASからAPI Gateway + WAFまで

## はじめに
Duration: 0:05:00

### ハンズオンの概要

このハンズオンでは、サーバレスでHTTP APIを公開する方法を段階的に学びます。

1. **Google Apps Script（GAS）** で手軽にAPIを作る
2. **AWS Lambda Function URL** で同等のAPIを作り、GASとの違いを比較する
3. セキュリティ上の課題を認識し、暫定的な対策を実装する
4. **API Gateway + WAF + Lambda** でより本格的・セキュアな構成を構築する

### サーバレスAPIの実行時間制限

サーバレスAPIを選ぶ際、実行時間制限は重要な判断材料です。

| サービス | プラン | 実行時間の上限 |
|----------|--------|--------------|
| Google Apps Script | 無料版 | **6分** |
| Google Apps Script | Google Workspace（有料版） | **30分** |
| AWS Lambda | — | **15分** |

### 構成の進化

このハンズオンでは、以下のように段階的に構成を発展させます。

```
Step 1: GAS → Webアプリとして公開（手軽だが制約あり）
  ↓
Step 2: Lambda Function URL（AWSでの同等構成、制約も同様）
  ↓
Step 3: セキュリティ暫定対策（GAS: スプレッドシート照合 / Lambda: DynamoDB照合）
  ↓
Step 4: API Gateway + WAF + Lambda（本格的・セキュアな構成）
```

### 前提条件

* AWSアカウントを持っていること
* Googleアカウントを持っていること
* GitHubアカウントを持っていること

### ターミナルとディレクトリの前提

本ハンズオンでは、特記ない限り**プロジェクトのルートディレクトリ**（`12-AWS-handson...` フォルダ）でコマンドを実行することを前提としています。

また、Windows のコマンドプロンプトを使用する場合、ターミナルを閉じると `set` コマンドで設定した環境変数（`API_ID` や `API_KEY` 等）が消えてしまいます。ターミナルを再起動した場合は、必要に応じて変数を再設定してください。

Positive
: 本ハンズオンは初心者向けの内容です。GAS、Lambda、API Gateway、WAF を段階的に学んでいきます。

Negative
: 本ハンズオンで作成するリソースには料金が発生する場合があります。ハンズオン終了後は必ずリソースを削除してください。

## AWSアカウントの準備
Duration: 0:10:00

本ハンズオンを実行するためにはAWSアカウントが必要です。
すでにAWSから直接払い出されたアカウント、ハンズオンイベント等で払い出されているAWSアカウントをご利用の場合は、このステップをスキップしてかまいません。

新しく個人で作成する場合、2026年5月6日現在、アカウント作成時には**クレジットカードの登録が必要**となりますが、登録から半年間は**200 USD 分の無料クレジット**枠が付与されるキャンペーンや、常時無料枠が用意されています。

詳細な作成手順については、以下の公式ページや参考記事をご覧ください。
* [AWS 無料枠（公式）](https://aws.amazon.com/jp/free/)
* [参考記事: AWSアカウントの作成手順](https://zenn.dev/tamago701/articles/ce15bf5f0cce09)

### AWSの主要サービスの無料枠について

AWSには、クレジットを消費せずに利用できる**「常に無料」のサービス**と、クレジットを利用して評価・検証が可能なサービスがあります。

#### 常に無料のサービス（毎月の限度枠）
* **AWS Lambda**: 100万リクエスト/月、最大40万GB秒（または320万秒）のコンピューティング時間
* **Amazon DynamoDB**: 25 GBのストレージ、25 WCU（書き込み）、25 RCU（読み込み）
* **Amazon CloudFront**: 1 TBのアウトバウンドデータ転送、1,000万リクエスト/月
* **Amazon Q Developer**: IDE/CLIでのコード補完、月間50回のチャット、月間25回の自然言語クエリなど
* **AWS WAF Bot Control**: 月間1,000万リクエストまでの処理
* **Amazon CodeCatalyst**: 2,000ビルド分、60時間の開発環境、10GBのソースストレージ
* **Amazon SNS**: 100万件のパブリッシュ、10万件のHTTP/S配信、1,000件のEメール配信
* **AWS Certificate Manager (ACM)**: 最初の10,000APIコール
* **AWS Systems Manager**: Explorer, Session Manager, Parameter Store などの主要機能
* **AWS CloudFormation**: 月間1,000回のハンドラー操作
* **Amazon EventBridge**: Schedulerの月間1,400万回呼び出し など
* **AWS Key Management Service (KMS)**: 月間20,000リクエスト

#### 無料枠・クレジット対象のサービス
以下のサービスは、無料プラン対象のインスタンスを選択したり、付与されたクレジットを消費することで無料で評価・利用が可能です。
* **Amazon EC2**: T3.micro, T3.small, T4g.micro などの対象インスタンス
* **Amazon RDS**: db.t3.micro, db.t4g.micro（MySQL, PostgreSQL 等）
* **Amazon S3**: 高い耐久性を持ったデータ保存とアクセス制御
* **その他**: Elastic Load Balancing (ALB/NLB等), AWS WAF, AWS CloudShell, Amazon SES, Amazon Polly, AWS SecretsManager

## 事前準備: AWS Builder ID の作成
Duration: 0:05:00

AWS Kiro-IDE などのツールを利用・連携するために、「**AWS Builder ID**」が必要となります。
AWS Builder ID は AWS や Amazon.co.jp アカウントとは異なる、個人のための無料アカウントです（クレジットカードの登録なども不要です）。

1. [AWS Builder ID の作成画面](https://builder.aws.com/start) にアクセスします。
2. 個人のメールアドレスを入力し [次へ] をクリックします。
3. 表示される「名前」を入力して [次へ] をクリックします。
4. 入力したメールアドレス宛に届いた認証コードを入力して [認証] します。
5. パスワードの条件（8〜64文字・大文字と小文字・数値・英数字以外の文字）を満たすパスワードを設定し、[AWS Builder IDを作成] をクリックします。

Positive
: 詳しい画面遷移や Community.aws でのプロファイル作成方法については、[こちらの記事 (AWS Builder ID の利用とその作成方法)](https://note.com/s_numaguchi/n/nd5126833389b) もあわせてご参照ください。

## 開発環境を準備する
Duration: 0:15:00

本ハンズオンは、ご自身のローカルPC（Windows または macOS/Linux）または **AWS Kiro-IDE** などのクラウドIDEで実行することを前提としています。
以下のツールがインストールされているか確認し、インストールされていない場合はセットアップを行ってください。

### 1. エディタ (AWS Kiro-IDE) のインストール

本ハンズオンでは、デスクトップIDEである **AWS Kiro-IDE** を使用します。
[https://kiro.dev/](https://kiro.dev/) にアクセスし、サイトの手順に従ってダウンロード・インストールを行ってください。

以降のファイル編集などの操作は、このエディタ環境内で行うものとします。

### 2. Node.js と npm のインストール

GASのコマンドラインツール（clasp）を使用するために必要です。

**Windows の場合**
[Node.js 公式サイト](https://nodejs.org/) から Windows Installer (.msi) をダウンロードしてインストールしてください（LTS版を推奨）。

**macOS の場合**
Homebrew を使用してインストールします。
```console
brew install node
```

**Linux (Ubuntu/Debian) の場合**
```console
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 3. Python 3 のインストール

AWS Lambda のコードを作成・パッケージングするために使用します。

**Windows の場合**
[Python 公式サイト](https://www.python.org/downloads/windows/) からインストーラをダウンロードしてインストールしてください。
※ インストール時に「Add Python to PATH」にチェックを入れるのを忘れないでください。

**macOS の場合**
```console
brew install python
```

**Linux (Ubuntu/Debian) の場合**
```console
sudo apt-get update && sudo apt-get install -y python3 python3-pip
```

### 4. AWS CLI のインストール

AWS リソースをコマンドラインから操作するために必要です。

**Windows の場合**
[AWS CLI MSI インストーラ](https://awscli.amazonaws.com/AWSCLIV2.msi) をダウンロードして実行してください。

**macOS の場合**
```console
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

**Linux の場合**
```console
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

### 5. clasp のインストールとログイン

Google Apps Script のプロジェクトをローカルで管理するためのツールです。

コマンドプロンプト（Windows）またはターミナル（macOS/Linux）を開き、以下のコマンドを実行します。

```console
npm install -g @google/clasp
```

インストールが完了したら、Google アカウントにログインします。

1. Apps Script API を有効化します。ブラウザで以下のURLにアクセスし、トグルを **オン** にします。
   https://script.google.com/home/usersettings

2. ターミナルまたはコマンドプロンプトで以下を実行します。

```console
clasp login
```

3. ブラウザが自動的に開き、Google アカウントの選択画面が表示されます。
4. 使用するアカウントを選択し、アクセスを許可してください。
5. ブラウザに「Logged in! You may close this page.」と表示されれば成功です。

### 動作確認

ターミナル（またはコマンドプロンプト）で以下のコマンドを実行し、バージョンが表示されれば準備完了です。

**Windows (コマンドプロンプト) の場合**
```console
aws --version
python -V
node -v
npm -v
clasp --version
```

**macOS/Linux (ターミナル) の場合**
```console
aws --version; python3 -V; node -v; npm -v; clasp --version
```

**実行結果の例**
```text
aws-cli/2.15.0 Python/3.11.6 ...
Python 3.12.1
v20.10.0
10.2.3
2.4.2
```

## IAMユーザーの作成
Duration: 0:10:00

### IAMユーザーの作成手順 (マネジメントコンソール)

AWS CLI から AWS リソースを操作するための専用ユーザーを作成し、アクセスキーを発行します。最初のユーザー作成は、AWS マネジメントコンソール（ブラウザ）から行います。

1. [AWS マネジメントコンソール](https://console.aws.amazon.com/) に、**ルートユーザー** または **ハンズオン用に払い出された（IAM操作権限を持つ）IAMユーザー** でログインします。
2. 検索バーに「IAM」と入力し、IAM サービス画面に移動します。
3. 左メニューの [ユーザー] をクリックし、[ユーザーの作成] をクリックします。
4. **ユーザーの詳細**:
   *   ユーザー名: `handson-user`
   *   [次へ] をクリックします。
5. **許可の設定**:
   *   [ポリシーを直接アタッチする] を選択します。
   *   許可ポリシーの検索窓に `AdministratorAccess` と入力し、チェックボックスをオンにします。
   *   [次へ] をクリックします。
6. **確認と作成**:
   *   内容を確認し、[ユーザーの作成] をクリックします。
7. **アクセスキーの発行**:
   *   作成された `handson-user` の名前をクリックして詳細画面を開きます。
   *   [セキュリティ認証情報] タブをクリックします。
   *   「アクセスキー」セクションで [アクセスキーを作成] をクリックします。
   *   ユースケースで [コマンドラインインターフェイス (CLI)] を選択し、チェックボックスをオンにして [次へ] をクリックします。
   *   [アクセスキーを作成] をクリックします。

8. 表示される **アクセスキー ID** と **シークレットアクセスキー** を必ずメモ（またはCSVをダウンロード）してください。

Positive
: 本ハンズオンでは簡易化のため AdministratorAccess を付与しますが、AWS Organizations のSCP（サービスコントロールポリシー）により、実際に利用できるサービスは制限されています。本番環境では最小権限の原則に基づいた権限設定を行ってください。

Negative
: シークレットアクセスキーはこのタイミングでしか確認できません。必ずメモしてください。

## AWS CLI の認証設定
Duration: 0:05:00

### 認証情報の設定

ターミナル（またはコマンドプロンプト）で以下のコマンドを実行し、先ほど発行したアクセスキーを設定します。

```console
aws configure
```

| 項目 | 値 |
|------|-----|
| AWS Access Key ID | 発行したアクセスキー |
| AWS Secret Access Key | 発行したシークレットアクセスキー |
| Default region name | `ap-northeast-1` |
| Default output format | `json` |

### 設定の確認

```console
aws sts get-caller-identity
```

**実行結果の例**
```json
{
    "UserId": "AIDASAMPLEUSERID",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/handson-user"
}
```

正しく設定されていれば、アカウントIDやユーザーARNが表示されます。

Negative
: アクセスキーをGitリポジトリにコミットしないよう注意してください。`.gitignore` にAWS認証情報ファイルの除外設定が含まれていますが、環境変数やコード内にハードコードしないよう気をつけましょう。

## GASでWebアプリAPIを作成する
Duration: 0:15:00

### Google Apps Script プロジェクトの作成

ターミナル（またはコマンドプロンプト）で clasp を使ってプロジェクトを作成します。

**Windows (コマンドプロンプト) の場合**
```console
mkdir gas\04
cd gas\04
clasp create --title "handson-text-api" --type standalone
```

**macOS/Linux (ターミナル) の場合**
```console
mkdir -p gas/04 && cd gas/04
clasp create --title "handson-text-api" --type standalone
```

**実行結果の例**
```text
Created new standalone script: handson-text-api
...
```

### コードの入力

Kiro を使用して作成されたディレクトリ内の `Code.js` を開き、以下の内容で上書き保存してください。

```javascript
/**
 * GETリクエストのハンドラー
 * @param {Object} e - イベントオブジェクト
 * @return {TextOutput} JSON形式のレスポンス
 */
function doGet(e) {
  var output = {
    service: "テキスト要約API（GAS版）",
    version: "1.0",
    usage: "POSTリクエストで {text: '要約したいテキスト', max_sentences: 3} を送信してください"
  };

  return ContentService
    .createTextOutput(JSON.stringify(output))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * POSTリクエストのハンドラー - テキスト要約処理
 * @param {Object} e - イベントオブジェクト
 * @return {TextOutput} JSON形式のレスポンス
 */
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var text = data.text || "";
    var maxSentences = data.max_sentences || 3;

    if (!text) {
      return ContentService
        .createTextOutput(JSON.stringify({
          error: "テキストが指定されていません"
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    // 簡易要約処理: 文を分割して先頭N文を抽出
    var sentences;
    if (text.indexOf("。") !== -1) {
      sentences = text.split("。").filter(function(s) { return s.trim(); });
      sentences = sentences.map(function(s) { return s.trim() + "。"; });
    } else {
      sentences = text.split(".").filter(function(s) { return s.trim(); });
      sentences = sentences.map(function(s) { return s.trim() + "."; });
    }

    var summarySentences = sentences.slice(0, maxSentences);
    var summary = summarySentences.join("");

    var result = {
      original_length: text.length,
      summary: summary,
      sentence_count: sentences.length,
      summary_sentence_count: summarySentences.length
    };

    return ContentService
      .createTextOutput(JSON.stringify(result))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({
        error: "リクエストの処理中にエラーが発生しました: " + error.message
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

### コードのアップロードとデプロイ

**Windows (コマンドプロンプト) の場合**
```console
:: コードを Apps Script にアップロード
clasp push

:: バージョンを作成
clasp version "初回デプロイ"

:: Webアプリとしてデプロイ
clasp deploy --description "テキスト要約API"
```

**macOS/Linux (ターミナル) の場合**
```console
clasp push
clasp version "初回デプロイ"
clasp deploy --description "テキスト要約API"
```

**実行結果の例**
```text
Created version 1.
- AKfycbwEXAMPLE_DEPLOY_ID @1.
```

デプロイIDが表示されます。WebアプリのURLは以下の形式です。

```
https://script.google.com/macros/s/{デプロイID}/exec
```

Positive
: `clasp deployments` コマンドでデプロイ一覧を確認できます。

### 動作確認

デプロイID（`AKfy...`のような文字列）をコピーしておきます。

**Windows (コマンドプロンプト) の場合**
```console
:: デプロイIDを変数に設定（表示されたIDに置き換え）
set DEPLOY_ID=ここにデプロイIDを貼り付け

:: GETリクエスト
curl -L "https://script.google.com/macros/s/%DEPLOY_ID%/exec"

:: POSTリクエスト（WindowsコマンドプロンプトではJSONのエスケープが必要です）
curl -L -X POST -H "Content-Type: application/json" -d "{\"text\": \"AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。\", \"max_sentences\": 2}" "https://script.google.com/macros/s/%DEPLOY_ID%/exec"
```

**macOS/Linux (ターミナル) の場合**
```console
# デプロイIDを変数に設定（表示されたIDに置き換え）
DEPLOY_ID="ここにデプロイIDを貼り付け"

# GETリクエスト
curl -L "https://script.google.com/macros/s/${DEPLOY_ID}/exec"

# POSTリクエスト
curl -L -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。", "max_sentences": 2}' \
  "https://script.google.com/macros/s/${DEPLOY_ID}/exec"
```

**実行結果の例**
```json
{
  "original_length": 68,
  "summary": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。",
  "sentence_count": 3,
  "summary_sentence_count": 2
}
```

Negative
: GASのWebアプリURLは、URLを知っている人なら誰でもアクセスできます。また、無料版では実行時間が最大6分に制限されています。

## Lambda Function URLで同等のAPIを作成する
Duration: 0:20:00

### IAMロールの作成

Lambda関数用の実行ロールを作成します。

**Windows (コマンドプロンプト) の場合**
```console
mkdir lambda\05
cd lambda\05
```

**macOS/Linux (ターミナル) の場合**
```console
mkdir -p lambda/05 && cd lambda/05
```

Kiro を使用して同ディレクトリ内に `trust-policy.json` を作成し、以下の内容を保存します。

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Windows (コマンドプロンプト) の場合**
```console
:: IAMロールの作成
aws iam create-role ^
  --role-name handson-furl-lambda-role ^
  --assume-role-policy-document file://trust-policy.json

:: CloudWatchLogsFullAccess ポリシーをアタッチ
aws iam attach-role-policy ^
  --role-name handson-furl-lambda-role ^
  --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
```

**macOS/Linux (ターミナル) の場合**
```console
# IAMロールの作成
aws iam create-role \
  --role-name handson-furl-lambda-role \
  --assume-role-policy-document file://trust-policy.json

# CloudWatchLogsFullAccess ポリシーをアタッチ
aws iam attach-role-policy \
  --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
```

### Lambda関数の作成

Kiro を使用して同ディレクトリ内（`lambda/05`）に `lambda_function.py` を作成し、以下の内容を保存します。

```python
import json


def lambda_handler(event, context):
    """Lambda Function URL用のテキスト要約API"""

    # リクエストメソッドの取得
    http_method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')

    # GETリクエスト: API情報を返す
    if http_method == 'GET':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json; charset=utf-8'
            },
            'body': json.dumps({
                'service': 'テキスト要約API（Lambda版）',
                'version': '1.0',
                'usage': 'POSTリクエストで {"text": "要約したいテキスト", "max_sentences": 3} を送信してください'
            }, ensure_ascii=False)
        }

    # POSTリクエスト: テキスト要約処理
    if http_method == 'POST':
        try:
            body = event.get('body') or '{}'
            if event.get('isBase64Encoded', False):
                import base64
                body = base64.b64decode(body).decode('utf-8')

            data = json.loads(body)
            text = data.get('text', '')
            max_sentences = data.get('max_sentences', 3)

            if not text:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json; charset=utf-8'},
                    'body': json.dumps({
                        'error': 'テキストが指定されていません'
                    }, ensure_ascii=False)
                }

            # 簡易要約処理
            if '。' in text:
                sentences = [s.strip() + '。' for s in text.split('。') if s.strip()]
            else:
                sentences = [s.strip() + '.' for s in text.split('.') if s.strip()]

            summary_sentences = sentences[:max_sentences]
            summary = ''.join(summary_sentences) if '。' in text else ' '.join(summary_sentences)

            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json; charset=utf-8'},
                'body': json.dumps({
                    'original_length': len(text),
                    'summary': summary,
                    'sentence_count': len(sentences),
                    'summary_sentence_count': len(summary_sentences)
                }, ensure_ascii=False)
            }
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json; charset=utf-8'},
                'body': json.dumps({'error': 'JSONの形式が不正です'}, ensure_ascii=False)
            }

    return {
        'statusCode': 405,
        'headers': {'Content-Type': 'application/json; charset=utf-8'},
        'body': json.dumps({'error': f'{http_method}はサポートされていません'}, ensure_ascii=False)
    }
```

コードを保存したら、ZIPファイルに圧縮し、Lambda関数を作成します。

**Windows (コマンドプロンプト) の場合**
```console
:: zipファイルの作成 (Windows 10/11 以降で利用可能な tar コマンドを使用)
tar -a -c -f function.zip lambda_function.py

:: アカウントIDの取得と関数の作成
for /f "delims=" %i in ('aws sts get-caller-identity --query Account --output text') do set ACCOUNT_ID=%i

aws lambda create-function ^
  --function-name handson-text-summarizer ^
  --runtime python3.12 ^
  --handler lambda_function.lambda_handler ^
  --role arn:aws:iam::%ACCOUNT_ID%:role/handson-furl-lambda-role ^
  --zip-file fileb://function.zip
```

**macOS/Linux (ターミナル) の場合**
```console
# zipファイルの作成
zip function.zip lambda_function.py

# アカウントIDの取得と関数の作成
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

aws lambda create-function \
  --function-name handson-text-summarizer \
  --runtime python3.12 \
  --handler lambda_function.lambda_handler \
  --role arn:aws:iam::${ACCOUNT_ID}:role/handson-furl-lambda-role \
  --zip-file fileb://function.zip
```

**実行結果の例**
```json
{
    "FunctionName": "handson-text-summarizer",
    "FunctionArn": "arn:aws:lambda:ap-northeast-1:123456789012:function:handson-text-summarizer",
    "Runtime": "python3.12",
    ...
}
```


### Function URLの有効化

**Windows (コマンドプロンプト) の場合**
```console
:: Function URLの作成
aws lambda create-function-url-config ^
  --function-name handson-text-summarizer ^
  --auth-type NONE ^
  --cors "{\"AllowOrigins\":[\"*\"],\"AllowMethods\":[\"GET\",\"POST\"],\"AllowHeaders\":[\"Content-Type\"]}"

:: 公開アクセス許可の付与
aws lambda add-permission ^
  --function-name handson-text-summarizer ^
  --statement-id FunctionURLAllowPublicAccess ^
  --action lambda:InvokeFunctionUrl ^
  --principal "*" ^
  --function-url-auth-type NONE
```

**macOS/Linux (ターミナル) の場合**
```console
# Function URLの作成
aws lambda create-function-url-config \
  --function-name handson-text-summarizer \
  --auth-type NONE \
  --cors '{"AllowOrigins":["*"],"AllowMethods":["GET","POST"],"AllowHeaders":["Content-Type"]}'

# 公開アクセス許可の付与
aws lambda add-permission \
  --function-name handson-text-summarizer \
  --statement-id FunctionURLAllowPublicAccess \
  --action lambda:InvokeFunctionUrl \
  --principal "*" \
  --function-url-auth-type NONE
```

Negative
: 今回は GAS との比較のため `--auth-type NONE`（全ユーザーアクセス可能）で作成しています。本来は `--auth-type AWS_IAM` を指定することで、IAM認証済みのユーザー・ロールのみにアクセスを限定できます。IAM認証を使う場合、呼び出し側は SigV4 署名付きリクエストを送信する必要があります。詳細は [Lambda Function URL のアクセス制御](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html) を参照してください。

Function URLを取得します。

**Windows (コマンドプロンプト) の場合**
```console
for /f "delims=" %i in ('aws lambda get-function-url-config --function-name handson-text-summarizer --query FunctionUrl --output text') do set FUNCTION_URL=%i
echo %FUNCTION_URL%
```

**macOS/Linux (ターミナル) の場合**
```console
FUNCTION_URL=$(aws lambda get-function-url-config \
  --function-name handson-text-summarizer \
  --query FunctionUrl --output text)
echo $FUNCTION_URL
```

### 動作確認

**Windows (コマンドプロンプト) の場合**
```console
:: GETリクエスト
curl %FUNCTION_URL%

:: POSTリクエスト
curl -X POST %FUNCTION_URL% -H "Content-Type: application/json" -d "{\"text\": \"AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。\", \"max_sentences\": 2}"
```

**macOS/Linux (ターミナル) の場合**
```console
# GETリクエスト
curl $FUNCTION_URL

# POSTリクエスト
curl -X POST $FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{"text": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。", "max_sentences": 2}'
```

Positive
: GASとLambda、どちらも同じテキスト要約処理を実装しています。URLにアクセスするだけで動く手軽さは同じですが、実行時間制限やインフラの制御度に差があります。

## GAS vs Lambda Function URL の比較
Duration: 0:05:00

### 両者の比較

ここまでの実装を踏まえて、GASとLambda Function URLを比較します。

| 比較項目 | GAS（無料版） | GAS（有料版） | Lambda Function URL |
|----------|-------------|-------------|-------------------|
| 実行時間上限 | 6分 | 30分 | 15分 |
| デプロイ | ワンクリック | ワンクリック | Deploy+URL設定 |
| 言語 | JavaScript | JavaScript | Python, Node.js 等 |
| コスト | 無料 | Workspace料金 | 従量課金 |
| 認証 | Googleアカウント or なし | 同左 | NONE or IAM |
| カスタムドメイン | 不可 | 不可 | 不可 |
| WAF連携 | 不可 | 不可 | 不可 |
| レートリミット | GAS側の制限のみ | 同左 | なし（課金増大リスク） |

### 共通の課題

どちらの方式も、**URLを知っていれば誰でもアクセスできる**というセキュリティ上の課題があります。

* 不正アクセスによるコスト増大（Lambda）
* APIの不正利用
* DDoS攻撃のリスク

Negative
: GASもLambda Function URLも、単体ではAPIキー認証やレートリミットなどのセキュリティ機能を持ちません。次のセクションで暫定的な対策を、その後に本格的な対策を学びます。

## セキュリティの暫定対策
Duration: 0:20:00

### 考え方

API GatewayやWAFを使わなくても、アプリケーションレベルでの認証チェックを導入することで、ある程度のアクセス制御が可能です。

* **GAS**: スプレッドシートにAPIキーを保存し、リクエストのキーと照合
* **Lambda**: DynamoDBにAPIキーを保存し、リクエストのキーと照合

### GAS側: スプレッドシートでのキー照合

#### スプレッドシートの準備

1. Google スプレッドシートを新規作成します
2. シート名を `APIKeys` に変更します
3. A1セルに `key`、B1セルに `description` と入力します
4. A2セルにAPIキー（例: `handson-demo-key-2026`）を入力します
5. スプレッドシートのIDをメモします（URLの `/d/` と `/edit` の間の文字列）

#### GASコードの更新

新しいディレクトリを作成し、プロジェクトを初期化します。

**Windows (コマンドプロンプト) の場合**
```console
mkdir gas\06
cd gas\06
clasp create --title "handson-text-api-v2" --type standalone
```

**macOS/Linux (ターミナル) の場合**
```console
mkdir -p gas/06 && cd gas/06
clasp create --title "handson-text-api-v2" --type standalone
```

Kiro を使用してディレクトリ内に生成された `Code.js` を開き、以下の内容で上書き保存してください。

```javascript
// スプレッドシートID（自分のスプレッドシートIDに置き換え）
var SPREADSHEET_ID = "{あなたのスプレッドシートID}";

/**
 * APIキーを検証する
 * @param {string} apiKey - 検証するAPIキー
 * @return {boolean} 有効なキーならtrue
 */
function validateApiKey(apiKey) {
  if (!apiKey) return false;

  var sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName("APIKeys");
  var lastRow = sheet.getLastRow();
  if (lastRow < 2) return false;

  var keys = sheet.getRange(2, 1, lastRow - 1, 1).getValues();

  for (var i = 0; i < keys.length; i++) {
    if (keys[i][0] === apiKey) return true;
  }
  return false;
}

/**
 * GETリクエストのハンドラー
 */
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({
      service: "テキスト要約API（GAS版・認証あり）",
      version: "2.0",
      usage: "x-api-keyパラメータにAPIキーを指定してください"
    }))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * POSTリクエストのハンドラー - APIキー認証付き
 */
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);

    // APIキーの検証
    var apiKey = data.api_key || e.parameter.api_key || "";
    if (!validateApiKey(apiKey)) {
      return ContentService
        .createTextOutput(JSON.stringify({
          error: "無効なAPIキーです。正しいAPIキーを指定してください。"
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    var text = data.text || "";
    var maxSentences = data.max_sentences || 3;

    if (!text) {
      return ContentService
        .createTextOutput(JSON.stringify({ error: "テキストが指定されていません" }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    // 簡易要約処理
    var sentences;
    if (text.indexOf("。") !== -1) {
      sentences = text.split("。").filter(function(s) { return s.trim(); });
      sentences = sentences.map(function(s) { return s.trim() + "。"; });
    } else {
      sentences = text.split(".").filter(function(s) { return s.trim(); });
      sentences = sentences.map(function(s) { return s.trim() + "."; });
    }

    var summarySentences = sentences.slice(0, maxSentences);

    return ContentService
      .createTextOutput(JSON.stringify({
        original_length: text.length,
        summary: summarySentences.join(""),
        sentence_count: sentences.length,
        summary_sentence_count: summarySentences.length
      }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ error: "エラー: " + error.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

Negative
: GASでは `doPost` の引数 `e` にリクエストヘッダーを直接取得する方法が限定的なため、ここではリクエストボディの `api_key` フィールドで照合しています。

#### GASの再デプロイ

**Windows (コマンドプロンプト) の場合**
```console
clasp push
clasp version "APIキー認証追加"
clasp deploy --description "APIキー認証付きテキスト要約API"
```

**macOS/Linux (ターミナル) の場合**
```console
clasp push
clasp version "APIキー認証追加"
clasp deploy --description "APIキー認証付きテキスト要約API"
```

#### テスト

**Windows (コマンドプロンプト) の場合**
```console
set DEPLOY_ID=ここにデプロイIDを貼り付け

:: APIキーなし → エラー
curl -L -X POST -H "Content-Type: application/json" -d "{\"text\": \"テストです。要約します。\"}" "https://script.google.com/macros/s/%DEPLOY_ID%/exec"

:: APIキーあり → 成功
curl -L -X POST -H "Content-Type: application/json" -d "{\"api_key\": \"handson-demo-key-2026\", \"text\": \"テストです。要約します。\", \"max_sentences\": 1}" "https://script.google.com/macros/s/%DEPLOY_ID%/exec"
```

**macOS/Linux (ターミナル) の場合**
```console
# 新しいデプロイIDを変数に設定（表示されたIDに置き換え）
DEPLOY_ID="ここにデプロイIDを貼り付け"

# APIキーなし → エラー
curl -L -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "テストです。要約します。"}' \
  "https://script.google.com/macros/s/${DEPLOY_ID}/exec"

# APIキーあり → 成功
curl -L -X POST \
  -H "Content-Type: application/json" \
  -d '{"api_key": "handson-demo-key-2026", "text": "テストです。要約します。", "max_sentences": 1}' \
  "https://script.google.com/macros/s/${DEPLOY_ID}/exec"
```

### Lambda側: DynamoDBでのキー照合

#### DynamoDBテーブルの作成

**Windows (コマンドプロンプト) の場合**
```console
aws dynamodb create-table ^
  --table-name handson-api-keys ^
  --attribute-definitions AttributeName=api_key,AttributeType=S ^
  --key-schema AttributeName=api_key,KeyType=HASH ^
  --billing-mode PAY_PER_REQUEST
```

**macOS/Linux (ターミナル) の場合**
```console
aws dynamodb create-table \
  --table-name handson-api-keys \
  --attribute-definitions AttributeName=api_key,AttributeType=S \
  --key-schema AttributeName=api_key,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

**実行結果の例**
```json
{
    "TableDescription": {
        "TableName": "handson-api-keys",
        "TableStatus": "CREATING",
        ...
    }
}
```

#### APIキーの登録

**Windows (コマンドプロンプト) の場合**
```console
aws dynamodb put-item ^
  --table-name handson-api-keys ^
  --item "{\"api_key\": {\"S\": \"handson-demo-key-2026\"}}"
```

**macOS/Linux (ターミナル) の場合**
```console
aws dynamodb put-item \
  --table-name handson-api-keys \
  --item '{"api_key": {"S": "handson-demo-key-2026"}}'
```

#### IAMロールの更新

Lambda関数がDynamoDBにアクセスできるよう、ポリシーを追加します。

**Windows (コマンドプロンプト) の場合**
```console
aws iam attach-role-policy ^
  --role-name handson-furl-lambda-role ^
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
```

**macOS/Linux (ターミナル) の場合**
```console
aws iam attach-role-policy \
  --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
```

#### Lambda関数コードの更新

Lambda関数のコードを以下に更新します。

**Windows (コマンドプロンプト) の場合**
```console
mkdir lambda\06
cd lambda\06
```

**macOS/Linux (ターミナル) の場合**
```console
mkdir -p lambda/06 && cd lambda/06
```

Kiro を使用してディレクトリ内に `lambda_function.py` を作成し、以下の内容を保存します。

```python
import json
import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('handson-api-keys')


def validate_api_key(api_key):
    """DynamoDBでAPIキーを検証する"""
    if not api_key:
        return False
    try:
        response = table.get_item(Key={'api_key': api_key})
        return 'Item' in response
    except Exception:
        return False


def lambda_handler(event, context):
    """Lambda Function URL用のテキスト要約API（APIキー認証付き）"""

    http_method = event.get('requestContext', {}).get('http', {}).get('method', 'GET')

    # GETリクエスト: API情報を返す
    if http_method == 'GET':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json; charset=utf-8'},
            'body': json.dumps({
                'service': 'テキスト要約API（Lambda版・認証あり）',
                'version': '2.0',
                'usage': 'POSTリクエストで {"api_key": "...", "text": "...", "max_sentences": 3} を送信'
            }, ensure_ascii=False)
        }

    # POSTリクエスト: APIキー認証 + テキスト要約
    if http_method == 'POST':
        try:
            body = event.get('body', '{}')
            if event.get('isBase64Encoded', False):
                import base64
                body = base64.b64decode(body).decode('utf-8')
            data = json.loads(body)

            # APIキーの検証
            api_key = data.get('api_key', '')
            if not validate_api_key(api_key):
                return {
                    'statusCode': 403,
                    'headers': {'Content-Type': 'application/json; charset=utf-8'},
                    'body': json.dumps({
                        'error': '無効なAPIキーです'
                    }, ensure_ascii=False)
                }

            text = data.get('text', '')
            max_sentences = data.get('max_sentences', 3)

            if not text:
                return {
                    'statusCode': 400,
                    'headers': {'Content-Type': 'application/json; charset=utf-8'},
                    'body': json.dumps({'error': 'テキストが指定されていません'}, ensure_ascii=False)
                }

            # 簡易要約処理
            if '。' in text:
                sentences = [s.strip() + '。' for s in text.split('。') if s.strip()]
            else:
                sentences = [s.strip() + '.' for s in text.split('.') if s.strip()]

            summary_sentences = sentences[:max_sentences]
            summary = ''.join(summary_sentences) if '。' in text else ' '.join(summary_sentences)

            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json; charset=utf-8'},
                'body': json.dumps({
                    'original_length': len(text),
                    'summary': summary,
                    'sentence_count': len(sentences),
                    'summary_sentence_count': len(summary_sentences)
                }, ensure_ascii=False)
            }
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json; charset=utf-8'},
                'body': json.dumps({'error': 'JSONの形式が不正です'}, ensure_ascii=False)
            }

    return {
        'statusCode': 405,
        'headers': {'Content-Type': 'application/json; charset=utf-8'},
        'body': json.dumps({'error': f'{http_method}はサポートされていません'}, ensure_ascii=False)
    }
```

ファイルを保存したら、圧縮して更新します。

**Windows (コマンドプロンプト) の場合**
```console
tar -a -c -f function.zip lambda_function.py
aws lambda update-function-code ^
  --function-name handson-text-summarizer ^
  --zip-file fileb://function.zip
```

**macOS/Linux (ターミナル) の場合**
```console
zip function.zip lambda_function.py
aws lambda update-function-code \
  --function-name handson-text-summarizer \
  --zip-file fileb://function.zip
```

#### テスト

**Windows (コマンドプロンプト) の場合**
```console
:: APIキーなし → 403
curl -X POST %FUNCTION_URL% -H "Content-Type: application/json" -d "{\"text\": \"テストです。\"}"

:: APIキーあり → 200
curl -X POST %FUNCTION_URL% -H "Content-Type: application/json" -d "{\"api_key\": \"handson-demo-key-2026\", \"text\": \"テストです。要約します。\", \"max_sentences\": 1}"
```

**macOS/Linux (ターミナル) の場合**
```console
# APIキーなし → 403
curl -X POST $FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{"text": "テストです。"}'

# APIキーあり → 200
curl -X POST $FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{"api_key": "handson-demo-key-2026", "text": "テストです。要約します。", "max_sentences": 1}'
```

### 暫定対策の限界

スプレッドシートやDynamoDBでのキー照合は暫定対策であり、以下の課題が残ります。

| 課題 | 説明 |
|------|------|
| レートリミットなし | 大量リクエストを防げない |
| DDoS対策なし | エンドポイントへの攻撃を防げない |
| キー管理の煩雑さ | キーのローテーションや失効管理が手動 |
| ログ・監査 | APIの利用状況を体系的に把握しづらい |

Positive
: 暫定対策は小規模なプロトタイプやデモでは有効ですが、本格運用には次に学ぶAPI Gateway + WAFの構成が推奨されます。

## API Gatewayの構築
Duration: 0:15:00

### 本格的なAPI構成へ

ここからは、Lambda Function URLの代わりにAPI Gatewayを使った本格的な構成を構築します。

### Lambda関数の準備

API Gateway用にLambda関数を更新します。既存の `handson-text-summarizer` のコードを以下に更新します。  
（DynamoDBのAPIキー認証は、API Gateway側のAPIキー認証に置き換えるため削除します）

**Windows (コマンドプロンプト) の場合**
```console
mkdir lambda\07
cd lambda\07
```

**macOS/Linux (ターミナル) の場合**
```console
mkdir -p lambda/07 && cd lambda/07
```

Kiro を使用してディレクトリ内に `lambda_function.py` を作成し、以下の内容を保存します。

```python
import json


def lambda_handler(event, context):
    """API Gateway用のテキスト要約API"""

    http_method = event.get('httpMethod', 'GET')

    if http_method == 'GET':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json; charset=utf-8',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'service': 'テキスト要約API',
                'version': '3.0',
                'description': 'API Gateway + WAF経由のセキュアなAPI'
            }, ensure_ascii=False)
        }

    if http_method == 'POST':
        try:
            body = event.get('body') or '{}'
            data = json.loads(body) if isinstance(body, str) else body

            text = data.get('text', '')
            max_sentences = data.get('max_sentences', 3)

            if not text:
                return {
                    'statusCode': 400,
                    'headers': {
                        'Content-Type': 'application/json; charset=utf-8',
                        'Access-Control-Allow-Origin': '*'
                    },
                    'body': json.dumps({'error': 'テキストが指定されていません'}, ensure_ascii=False)
                }

            if '。' in text:
                sentences = [s.strip() + '。' for s in text.split('。') if s.strip()]
            else:
                sentences = [s.strip() + '.' for s in text.split('.') if s.strip()]

            summary_sentences = sentences[:max_sentences]
            summary = ''.join(summary_sentences) if '。' in text else ' '.join(summary_sentences)

            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json; charset=utf-8',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'original_length': len(text),
                    'summary': summary,
                    'sentence_count': len(sentences),
                    'summary_sentence_count': len(summary_sentences)
                }, ensure_ascii=False)
            }
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json; charset=utf-8',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'JSONの形式が不正です'}, ensure_ascii=False)
            }

    return {
        'statusCode': 405,
        'headers': {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'error': f'{http_method}はサポートされていません'}, ensure_ascii=False)
    }
```

**Windows (コマンドプロンプト) の場合**
```console
tar -a -c -f function.zip lambda_function.py
aws lambda update-function-code ^
  --function-name handson-text-summarizer ^
  --zip-file fileb://function.zip
```

**macOS/Linux (ターミナル) の場合**
```console
zip function.zip lambda_function.py
aws lambda update-function-code \
  --function-name handson-text-summarizer \
  --zip-file fileb://function.zip
```

Positive
: API Gatewayの「Lambdaプロキシ統合」を使用する場合、イベント形式が Function URL とは異なります。`httpMethod` でHTTPメソッドを判定する点に注意してください。

### Function URLの削除

API Gateway経由に切り替えるため、既存のFunction URLを削除します。

**Windows (コマンドプロンプト) の場合**
```console
aws lambda delete-function-url-config --function-name handson-text-summarizer
aws lambda remove-permission --function-name handson-text-summarizer ^
  --statement-id FunctionURLAllowPublicAccess
```

**macOS/Linux (ターミナル) の場合**
```console
aws lambda delete-function-url-config --function-name handson-text-summarizer
aws lambda remove-permission --function-name handson-text-summarizer \
  --statement-id FunctionURLAllowPublicAccess
```

### REST APIの作成

以降の手順では、コマンドの出力を変数に格納して利用します。

**Windows (コマンドプロンプト) の場合**
```console
:: REST APIの作成
for /f "delims=" %i in ('aws apigateway create-rest-api --name handson-text-summarizer-api --description "テキスト要約REST API" --endpoint-configuration types=REGIONAL --query id --output text') do set API_ID=%i
echo API ID: %API_ID%

:: ルートリソースIDの取得
for /f "delims=" %i in ('aws apigateway get-resources --rest-api-id %API_ID% --query "items[?path=='/'].id" --output text') do set ROOT_ID=%i

:: /summarize リソースの作成
for /f "delims=" %i in ('aws apigateway create-resource --rest-api-id %API_ID% --parent-id %ROOT_ID% --path-part summarize --query id --output text') do set RESOURCE_ID=%i
echo Resource ID: %RESOURCE_ID%
```

**macOS/Linux (ターミナル) の場合**
```console
# REST APIの作成
API_ID=$(aws apigateway create-rest-api \
  --name handson-text-summarizer-api \
  --description "テキスト要約REST API" \
  --endpoint-configuration types=REGIONAL \
  --query id --output text)
echo "API ID: $API_ID"

# ルートリソースIDの取得
ROOT_ID=$(aws apigateway get-resources --rest-api-id $API_ID \
  --query "items[?path=='/'].id" --output text)

# /summarize リソースの作成
RESOURCE_ID=$(aws apigateway create-resource \
  --rest-api-id $API_ID \
  --parent-id $ROOT_ID \
  --path-part summarize \
  --query id --output text)
echo "Resource ID: $RESOURCE_ID"
```

**実行結果の例**
```text
API ID: abcdef1234
Resource ID: ghijk5678
```

### メソッドの作成（GET・POST）

**Windows (コマンドプロンプト) の場合**
```console
for /f "delims=" %i in ('aws sts get-caller-identity --query Account --output text') do set ACCOUNT_ID=%i
set REGION=ap-northeast-1

aws apigateway put-method --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method GET --authorization-type NONE
aws apigateway put-integration --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method GET --type AWS_PROXY --integration-http-method POST --uri "arn:aws:apigateway:%REGION%:lambda:path/2015-03-31/functions/arn:aws:lambda:%REGION%:%ACCOUNT_ID%:function:handson-text-summarizer/invocations"

aws apigateway put-method --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method POST --authorization-type NONE
aws apigateway put-integration --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method POST --type AWS_PROXY --integration-http-method POST --uri "arn:aws:apigateway:%REGION%:lambda:path/2015-03-31/functions/arn:aws:lambda:%REGION%:%ACCOUNT_ID%:function:handson-text-summarizer/invocations"

aws apigateway put-method --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method OPTIONS --authorization-type NONE
aws apigateway put-integration --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method OPTIONS --type MOCK --request-templates "{\"application/json\": \"{\\\"statusCode\\\": 200}\"}"

aws apigateway put-method-response --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method OPTIONS --status-code 200 --response-parameters "{\"method.response.header.Access-Control-Allow-Headers\":false,\"method.response.header.Access-Control-Allow-Methods\":false,\"method.response.header.Access-Control-Allow-Origin\":false}"
aws apigateway put-integration-response --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method OPTIONS --status-code 200 --response-parameters "{\"method.response.header.Access-Control-Allow-Headers\":\"'Content-Type,X-Amz-Date,Authorization,X-Api-Key'\",\"method.response.header.Access-Control-Allow-Methods\":\"'GET,POST,OPTIONS'\",\"method.response.header.Access-Control-Allow-Origin\":\"'*'\"}"
```

**macOS/Linux (ターミナル) の場合**
```console
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=ap-northeast-1

# GETメソッドの作成
aws apigateway put-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method GET \
  --authorization-type NONE

aws apigateway put-integration \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method GET \
  --type AWS_PROXY \
  --integration-http-method POST \
  --uri "arn:aws:apigateway:${REGION}:lambda:path/2015-03-31/functions/arn:aws:lambda:${REGION}:${ACCOUNT_ID}:function:handson-text-summarizer/invocations"

# POSTメソッドの作成
aws apigateway put-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method POST \
  --authorization-type NONE

aws apigateway put-integration \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method POST \
  --type AWS_PROXY \
  --integration-http-method POST \
  --uri "arn:aws:apigateway:${REGION}:lambda:path/2015-03-31/functions/arn:aws:lambda:${REGION}:${ACCOUNT_ID}:function:handson-text-summarizer/invocations"

# OPTIONSメソッドの作成（CORS用）
aws apigateway put-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method OPTIONS \
  --authorization-type NONE

aws apigateway put-integration \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method OPTIONS \
  --type MOCK \
  --request-templates '{"application/json": "{\"statusCode\": 200}"}'

aws apigateway put-method-response \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method OPTIONS \
  --status-code 200 \
  --response-parameters '{"method.response.header.Access-Control-Allow-Headers":false,"method.response.header.Access-Control-Allow-Methods":false,"method.response.header.Access-Control-Allow-Origin":false}'

aws apigateway put-integration-response \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method OPTIONS \
  --status-code 200 \
  --response-parameters '{"method.response.header.Access-Control-Allow-Headers":"'"'"'Content-Type,X-Amz-Date,Authorization,X-Api-Key'"'"'","method.response.header.Access-Control-Allow-Methods":"'"'"'GET,POST,OPTIONS'"'"'","method.response.header.Access-Control-Allow-Origin":"'"'"'*'"'"'"}'
```

### Lambda実行権限の付与

API GatewayがLambda関数を呼び出せるよう権限を付与します。

**Windows (コマンドプロンプト) の場合**
```console
aws lambda add-permission --function-name handson-text-summarizer --statement-id apigateway-invoke --action lambda:InvokeFunction --principal apigateway.amazonaws.com --source-arn "arn:aws:execute-api:%REGION%:%ACCOUNT_ID%:%API_ID%/*"
```

**macOS/Linux (ターミナル) の場合**
```console
aws lambda add-permission \
  --function-name handson-text-summarizer \
  --statement-id apigateway-invoke \
  --action lambda:InvokeFunction \
  --principal apigateway.amazonaws.com \
  --source-arn "arn:aws:execute-api:${REGION}:${ACCOUNT_ID}:${API_ID}/*"
```

### APIのデプロイ

**Windows (コマンドプロンプト) の場合**
```console
aws apigateway create-deployment --rest-api-id %API_ID% --stage-name dev
set API_URL=https://%API_ID%.execute-api.%REGION%.amazonaws.com/dev/summarize
echo Endpoint: %API_URL%
```

**macOS/Linux (ターミナル) の場合**
```console
aws apigateway create-deployment \
  --rest-api-id $API_ID \
  --stage-name dev
API_URL="https://${API_ID}.execute-api.${REGION}.amazonaws.com/dev/summarize"
echo "Endpoint: $API_URL"
```

### 動作確認

**Windows (コマンドプロンプト) の場合**
```console
curl %API_URL%

curl -X POST %API_URL% -H "Content-Type: application/json" -d "{\"text\": \"AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。\", \"max_sentences\": 2}"
```

**macOS/Linux (ターミナル) の場合**
```console
curl $API_URL

curl -X POST $API_URL \
  -H "Content-Type: application/json" \
  -d '{"text": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。", "max_sentences": 2}'
```

## APIキー認証の追加
Duration: 0:15:00

### 使用量プランの作成

**Windows (コマンドプロンプト) の場合**
```console
for /f "delims=" %i in ('aws apigateway create-usage-plan --name handson-basic-plan --throttle burstLimit^=5^,rateLimit^=10 --quota limit^=1000^,period^=DAY --api-stages apiId^=%API_ID%^,stage^=dev --query id --output text') do set PLAN_ID=%i
echo Usage Plan ID: %PLAN_ID%
```

**macOS/Linux (ターミナル) の場合**
```console
# 使用量プランの作成
PLAN_ID=$(aws apigateway create-usage-plan \
  --name handson-basic-plan \
  --throttle burstLimit=5,rateLimit=10 \
  --quota limit=1000,period=DAY \
  --api-stages apiId=${API_ID},stage=dev \
  --query id --output text)
echo "Usage Plan ID: $PLAN_ID"
```

### APIキーの作成

**Windows (コマンドプロンプト) の場合**
```console
for /f "delims=" %i in ('aws apigateway create-api-key --name handson-test-key --enabled --query id --output text') do set KEY_ID=%i
aws apigateway create-usage-plan-key --usage-plan-id %PLAN_ID% --key-id %KEY_ID% --key-type API_KEY
for /f "delims=" %i in ('aws apigateway get-api-key --api-key %KEY_ID% --include-value --query value --output text') do set API_KEY=%i
echo API Key: %API_KEY%
```

**macOS/Linux (ターミナル) の場合**
```console
# APIキーの作成
KEY_ID=$(aws apigateway create-api-key \
  --name handson-test-key \
  --enabled \
  --query id --output text)

# APIキーを使用量プランに紐付け
aws apigateway create-usage-plan-key \
  --usage-plan-id $PLAN_ID \
  --key-id $KEY_ID \
  --key-type API_KEY

# APIキーの値を取得
API_KEY=$(aws apigateway get-api-key --api-key $KEY_ID --include-value \
  --query value --output text)
echo "API Key: $API_KEY"
```

**実行結果の例**
```text
Usage Plan ID: lmno9012
API Key: ABCDEFGHIJKLMNOPQRSTUVWXYZ123456
```

### メソッドにAPIキー要求を設定

**Windows (コマンドプロンプト) の場合**
```console
aws apigateway update-method --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method GET --patch-operations op=replace,path=/apiKeyRequired,value=true
aws apigateway update-method --rest-api-id %API_ID% --resource-id %RESOURCE_ID% --http-method POST --patch-operations op=replace,path=/apiKeyRequired,value=true
aws apigateway create-deployment --rest-api-id %API_ID% --stage-name dev
```

**macOS/Linux (ターミナル) の場合**
```console
# GETメソッドにAPIキー必須を設定
aws apigateway update-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method GET \
  --patch-operations op=replace,path=/apiKeyRequired,value=true

# POSTメソッドにAPIキー必須を設定
aws apigateway update-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method POST \
  --patch-operations op=replace,path=/apiKeyRequired,value=true

# 再デプロイ
aws apigateway create-deployment \
  --rest-api-id $API_ID \
  --stage-name dev
```

### テスト

**Windows (コマンドプロンプト) の場合**
```console
:: APIキーなし → 403 Forbidden
curl %API_URL%

:: APIキーあり → 200 OK
curl -H "x-api-key: %API_KEY%" %API_URL%

:: POSTリクエスト + APIキー
curl -X POST -H "x-api-key: %API_KEY%" -H "Content-Type: application/json" -d "{\"text\": \"テストです。要約します。\", \"max_sentences\": 1}" %API_URL%
```

**macOS/Linux (ターミナル) の場合**
```console
# APIキーなし → 403 Forbidden
curl $API_URL

# APIキーあり → 200 OK
curl -H "x-api-key: $API_KEY" $API_URL

# POSTリクエスト + APIキー
curl -X POST \
  -H "x-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "テストです。要約します。", "max_sentences": 1}' \
  $API_URL
```

Positive
: API Gatewayの`x-api-key`ヘッダーによる認証は、DynamoDBによる暫定対策と比べて、レートリミット・使用量制御・キー管理が組み込みで提供されます。

## AWS WAFの構築と連携
Duration: 0:20:00

### AWS WAFとは

AWS WAF（Web Application Firewall）は、Webアプリケーションを一般的な攻撃から保護するサービスです。  
API Gatewayと連携することで、APIに対する不正アクセスを自動的にブロックできます。

### Web ACLの作成

まず、WAFのルールを定義したJSONファイルを作成します。  
Kiro を使用してコマンドを実行しているディレクトリに `waf-rules.json` を作成し、以下の内容を保存してください。

```json
[
  {
    "Name": "AWSManagedRulesCommonRuleSet",
    "Priority": 1,
    "Statement": {
      "ManagedRuleGroupStatement": {
        "VendorName": "AWS",
        "Name": "AWSManagedRulesCommonRuleSet"
      }
    },
    "OverrideAction": {"None": {}},
    "VisibilityConfig": {
      "SampledRequestsEnabled": true,
      "CloudWatchMetricsEnabled": true,
      "MetricName": "AWSManagedRulesCommonRuleSet"
    }
  },
  {
    "Name": "AWSManagedRulesKnownBadInputsRuleSet",
    "Priority": 2,
    "Statement": {
      "ManagedRuleGroupStatement": {
        "VendorName": "AWS",
        "Name": "AWSManagedRulesKnownBadInputsRuleSet"
      }
    },
    "OverrideAction": {"None": {}},
    "VisibilityConfig": {
      "SampledRequestsEnabled": true,
      "CloudWatchMetricsEnabled": true,
      "MetricName": "AWSManagedRulesKnownBadInputsRuleSet"
    }
  },
  {
    "Name": "handson-rate-limit",
    "Priority": 3,
    "Statement": {
      "RateBasedStatement": {
        "Limit": 100,
        "AggregateKeyType": "IP"
      }
    },
    "Action": {"Block": {}},
    "VisibilityConfig": {
      "SampledRequestsEnabled": true,
      "CloudWatchMetricsEnabled": true,
      "MetricName": "handson-rate-limit"
    }
  }
]
```

次に、Web ACLを作成します。

**Windows (コマンドプロンプト) の場合**
```console
set API_GW_ARN=arn:aws:apigateway:%REGION%::/restapis/%API_ID%/stages/dev

:: Web ACLの作成
aws wafv2 create-web-acl ^
  --name handson-api-waf ^
  --scope REGIONAL ^
  --region %REGION% ^
  --default-action Allow={} ^
  --description "ハンズオンAPI用WAF" ^
  --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=handson-api-waf ^
  --rules file://waf-rules.json

:: ARNの取得
for /f "delims=" %i in ('aws wafv2 list-web-acls --scope REGIONAL --region %REGION% --query "WebACLs[?Name=='handson-api-waf'].ARN" --output text') do set WAF_ACL_ARN=%i
echo WAF ACL ARN: %WAF_ACL_ARN%
```

**macOS/Linux (ターミナル) の場合**
```console
# API GatewayのARNを取得
API_GW_ARN="arn:aws:apigateway:${REGION}::/restapis/${API_ID}/stages/dev"

# Web ACLの作成
WAF_ACL_ARN=$(aws wafv2 create-web-acl \
  --name handson-api-waf \
  --scope REGIONAL \
  --region $REGION \
  --default-action Allow={} \
  --description "ハンズオンAPI用WAF" \
  --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=handson-api-waf \
  --rules file://waf-rules.json \
  --query Summary.ARN --output text)
echo "WAF ACL ARN: $WAF_ACL_ARN"
```

**実行結果の例**
```text
WAF ACL ARN: arn:aws:wafv2:ap-northeast-1:123456789012:regional/webacl/handson-api-waf/...
```

| ルールグループ | 説明 |
|--------------|------|
| AWSManagedRulesCommonRuleSet | 一般的なWebアプリケーション攻撃を防御 |
| AWSManagedRulesKnownBadInputsRuleSet | 既知の悪意のある入力パターンを検出 |
| handson-rate-limit | 5分あたり100リクエストを超えるとブロック |

### API Gatewayとの関連付け

**Windows (コマンドプロンプト) の場合**
```console
aws wafv2 associate-web-acl --web-acl-arn %WAF_ACL_ARN% --resource-arn %API_GW_ARN% --region %REGION%
```

**macOS/Linux (ターミナル) の場合**
```console
aws wafv2 associate-web-acl \
  --web-acl-arn $WAF_ACL_ARN \
  --resource-arn $API_GW_ARN \
  --region $REGION
```

Positive
: マネージドルールはAWSが管理・更新するため、最新のセキュリティ脅威に自動的に対応できます。

## WAFの動作確認
Duration: 0:10:00

### 正常アクセスの確認

APIキーを使って正常にアクセスできることを確認します。

**Windows (コマンドプロンプト) の場合**
```console
curl -H "x-api-key: %API_KEY%" %API_URL%
```

**macOS/Linux (ターミナル) の場合**
```console
curl -H "x-api-key: $API_KEY" $API_URL
```

正常なレスポンスが返れば、WAFが正常なリクエストを通過させていることを確認できます。

### SQLインジェクション攻撃のテスト

WAFが悪意のあるリクエストをブロックすることを確認します。

**Windows (コマンドプロンプト) の場合**
```console
curl -X POST -H "x-api-key: %API_KEY%" -H "Content-Type: application/json" -d "{\"text\": \"SELECT * FROM users; DROP TABLE users;--\"}" %API_URL%
```

**macOS/Linux (ターミナル) の場合**
```console
# SQLインジェクション風のリクエスト → WAFがブロック
curl -X POST \
  -H "x-api-key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "SELECT * FROM users; DROP TABLE users;--"}' \
  $API_URL
```

WAFがブロックした場合、`403 Forbidden` が返ります。

### レートリミットのテスト

短時間に大量のリクエストを送信して、レートリミットが機能することを確認します。

**Windows (コマンドプロンプト) の場合**
```console
for /l %i in (1,1,120) do @curl -s -o nul -w "Request %i: %%{http_code}\n" -H "x-api-key: %API_KEY%" %API_URL%
```

**macOS/Linux (ターミナル) の場合**
```console
# 連続リクエストでレートリミットをテスト
for i in $(seq 1 120); do
  echo "Request $i: $(curl -s -o /dev/null -w '%{http_code}' \
    -H "x-api-key: $API_KEY" \
    $API_URL)"
done
```

100リクエストを超えた辺りから `403` レスポンスが返り始めれば、レートリミットが機能しています。

Positive
: **テスト結果の解釈について**
WAF のレートベースルールは「5分間の継続的な集計」に基づいています。そのため、120回連続でリクエストを投げても、評価タイミングによっては**すべて `200 OK` で終わる場合がありますが、これは正常な動作です。** その場合は数分待ってから再度 1 回リクエストを投げると、集計が完了して `403 Forbidden` が返るようになります。

Negative
: レートベースのルールは5分間隔の集計に基づいて評価されるため、しきい値を超えてから実際にブロックが開始されるまでに数分のタイムラグが発生する場合があります。テストで即座に `403` にならない場合は、少し待ってから再度試してください。


### 構成の進化を振り返る

| 構成 | 認証 | レートリミット | 攻撃防御 | 運用負荷 |
|------|------|-------------|---------|---------|
| GAS（単体） | なし | GAS制限のみ | なし | 低 |
| GAS + スプレッドシート照合 | 簡易キー | なし | なし | 中 |
| Lambda Function URL（単体） | なし | なし | なし | 低 |
| Lambda + DynamoDB照合 | 簡易キー | なし | なし | 中 |
| **API Gateway + APIキー** | **APIキー** | **✅** | なし | 中 |
| **API Gateway + WAF + Lambda** | **APIキー** | **✅** | **✅** | 中〜高 |

## リソースの削除
Duration: 0:10:00

### 作成したリソースの削除

ハンズオンが完了したら、以下のコマンドでリソースを削除して料金の発生を防ぎましょう。

Windowsのコマンドプロンプトでは変数の動的取得が複雑になるため、ここではマネジメントコンソールからの削除を推奨しますが、コマンドで削除する場合は以下のようになります。

#### WAF Web ACLの削除

**Windows (コマンドプロンプト) の場合**
```console
:: 関連付けの解除
aws wafv2 disassociate-web-acl --resource-arn %API_GW_ARN% --region %REGION%

:: Web ACLの削除
for /f "delims=" %i in ('aws wafv2 list-web-acls --scope REGIONAL --region %REGION% --query "WebACLs[?Name=='handson-api-waf'].Id" --output text') do set WAF_ACL_ID=%i
for /f "delims=" %i in ('aws wafv2 get-web-acl --name handson-api-waf --scope REGIONAL --id %WAF_ACL_ID% --region %REGION% --query "LockToken" --output text') do set WAF_ACL_LOCK=%i
aws wafv2 delete-web-acl --name handson-api-waf --scope REGIONAL --id %WAF_ACL_ID% --lock-token %WAF_ACL_LOCK% --region %REGION%
```

**macOS/Linux (ターミナル) の場合**
```console
# 関連付けの解除
aws wafv2 disassociate-web-acl --resource-arn $API_GW_ARN --region $REGION

# Web ACLの削除
WAF_ACL_ID=$(aws wafv2 list-web-acls --scope REGIONAL --region $REGION \
  --query "WebACLs[?Name=='handson-api-waf'].Id" --output text)
WAF_ACL_LOCK=$(aws wafv2 get-web-acl --name handson-api-waf --scope REGIONAL \
  --id $WAF_ACL_ID --region $REGION --query "LockToken" --output text)
aws wafv2 delete-web-acl --name handson-api-waf --scope REGIONAL \
  --id $WAF_ACL_ID --lock-token $WAF_ACL_LOCK --region $REGION
```

#### API Gateway関連の削除

**Windows (コマンドプロンプト) の場合**
```console
:: 変数が残っていない場合は再取得が必要です
for /f "delims=" %i in ('aws apigateway get-rest-apis --query "items[?name=='handson-text-summarizer-api'].id" --output text') do set API_ID=%i
for /f "delims=" %i in ('aws apigateway get-api-keys --query "items[?name=='handson-test-key'].id" --output text') do set KEY_ID=%i
for /f "delims=" %i in ('aws apigateway get-usage-plans --query "items[?name=='handson-basic-plan'].id" --output text') do set PLAN_ID=%i

:: 削除実行（REST API -> 使用量プラン -> APIキー の順）
aws apigateway delete-rest-api --rest-api-id %API_ID%
aws apigateway delete-usage-plan --usage-plan-id %PLAN_ID%
aws apigateway delete-api-key --api-key %KEY_ID%
```

**macOS/Linux (ターミナル) の場合**
```console
API_ID=$(aws apigateway get-rest-apis \
  --query "items[?name=='handson-text-summarizer-api'].id" --output text)
KEY_ID=$(aws apigateway get-api-keys \
  --query "items[?name=='handson-test-key'].id" --output text)
PLAN_ID=$(aws apigateway get-usage-plans \
  --query "items[?name=='handson-basic-plan'].id" --output text)

# 削除実行（REST API -> 使用量プラン -> APIキー の順）
aws apigateway delete-rest-api --rest-api-id $API_ID
aws apigateway delete-usage-plan --usage-plan-id $PLAN_ID
aws apigateway delete-api-key --api-key $KEY_ID
```

Windows環境の場合は、AWSマネジメントコンソールから手動で「WAF Web ACL」「API Gateway」を削除することをおすすめします（変数が維持されていれば、作成時と同様のコマンドで削除可能です）。

#### DynamoDBテーブルの削除

```console
aws dynamodb delete-table --table-name handson-api-keys
```

#### Lambda関数の削除

```console
aws lambda delete-function --function-name handson-text-summarizer
```

#### IAMロールの削除

**Windows (コマンドプロンプト) の場合**
```console
aws iam detach-role-policy --role-name handson-furl-lambda-role ^
  --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
aws iam detach-role-policy --role-name handson-furl-lambda-role ^
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
aws iam delete-role --role-name handson-furl-lambda-role
```

**macOS/Linux (ターミナル) の場合**
```console
aws iam detach-role-policy --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
aws iam detach-role-policy --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
aws iam delete-role --role-name handson-furl-lambda-role
```

#### IAMユーザーの削除

**Windows (コマンドプロンプト) の場合**
```console
:: アクセキーの削除
for /f "delims=" %i in ('aws iam list-access-keys --user-name handson-user --query "AccessKeyMetadata[0].AccessKeyId" --output text') do set ACCESS_KEY_ID=%i
aws iam delete-access-key --user-name handson-user --access-key-id %ACCESS_KEY_ID%

:: ポリシーのデタッチとユーザー削除
aws iam detach-user-policy --user-name handson-user ^
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam delete-user --user-name handson-user
```

**macOS/Linux (ターミナル) の場合**
```console
# アクセスキーの削除
ACCESS_KEY_ID=$(aws iam list-access-keys --user-name handson-user \
  --query "AccessKeyMetadata[0].AccessKeyId" --output text)
aws iam delete-access-key --user-name handson-user --access-key-id $ACCESS_KEY_ID

# ポリシーのデタッチとユーザー削除
aws iam detach-user-policy --user-name handson-user \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws iam delete-user --user-name handson-user
```

#### GASプロジェクトの削除

**Windows (コマンドプロンプト) の場合**
```console
cd gas\04 && clasp undeploy --all
cd gas\06 && clasp undeploy --all
```

**macOS/Linux (ターミナル) の場合**
```console
cd gas/04 && clasp undeploy --all
cd gas/06 && clasp undeploy --all
```

#### 作業ディレクトリの削除

**Windows (コマンドプロンプト) の場合**
```console
rmdir /S /Q gas lambda
```

**macOS/Linux (ターミナル) の場合**
```console
rm -rf gas lambda
```

Negative
: リソースの削除を忘れると、特にWAFとAPI Gatewayで意図しない料金が発生する可能性があります。必ず全てのリソースを削除してください。

## まとめ
Duration: 0:05:00

### 学んだこと

このハンズオンでは、サーバレスAPIの構築と保護について段階的に学びました。

| ステップ | 内容 |
|---------|------|
| GAS Webアプリ | 最も手軽なAPI公開方法を体験 |
| Lambda Function URL | AWS上での同等構成を体験 |
| GAS vs Lambda 比較 | 実行時間制限・コスト・制約の違い |
| 暫定セキュリティ対策 | スプレッドシート/DynamoDBでのキー照合 |
| API Gateway | 本格的なAPI管理基盤 |
| APIキー認証 | アクセス制御とレートリミット |
| AWS WAF | Web攻撃からの保護 |

### ハンズオンシリーズの振り返り

| # | テーマ | 使用サービス |
|---|--------|------------|
| 09 | テキストの翻訳・音声化 | Lambda, Step Functions, S3, Translate, Polly |
| 10 | 静的Webサイトホスティング | CDK, CloudFront, S3, CloudWatch |
| 11 | 動的Webアプリ | Amplify |
| 12 | サーバレスAPIの構築と保護 | GAS, Lambda, API Gateway, WAF, DynamoDB |

### 発展課題

* GASで作成したテキスト要約APIを、自力でLambda（Python）に書き換えてみましょう（イベント形式の違いに注目）
* Lambdaで作成したテキスト要約APIを、自力でGAS（JavaScript）に書き換えてみましょう（レスポンス形式の違いに注目）
* API GatewayにCognitoユーザープールを連携して、ユーザー認証を追加してみましょう
* カスタムドメインを設定してAPIのURLを独自ドメインにしてみましょう
* Lambda関数でAmazon Bedrockと連携し、AI要約を実装してみましょう
* WAFのルールをカスタマイズして、特定のIPアドレスのみ許可してみましょう
* CloudWatch Logsでアクセスログを分析してみましょう

### 参考リンク

<button>
  [AWS Lambda Function URL ドキュメント](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-urls.html)
</button>

<button>
  [Amazon API Gateway ドキュメント](https://docs.aws.amazon.com/ja_jp/apigateway/)
</button>

<button>
  [AWS WAF ドキュメント](https://docs.aws.amazon.com/ja_jp/waf/)
</button>

<button>
  [Google Apps Script ドキュメント](https://developers.google.com/apps-script)
</button>
