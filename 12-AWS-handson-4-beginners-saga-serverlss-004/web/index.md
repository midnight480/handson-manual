---
id: 12-AWS-handson-4-beginners-saga-serverlss-004
summary: GAS vs Lambda Function URL 比較から API Gateway + WAF + Lambda まで - サーバレスAPI構築の一気通貫ハンズオン
status: [published]
categories: codelab,markdown
tags: web
feedback_link: https://github.com/midnight480/handson-manual
analytics_account: 196534296
source: 12-AWS-handson-4-beginners-saga-serverlss-004.md
duration: 175

---

# サーバレスAPIの構築と保護 - GASからAPI Gateway + WAFまで

[Codelab Feedback](https://github.com/midnight480/handson-manual)


## はじめに
Duration: 05:00


### ハンズオンの概要

このハンズオンでは、サーバレスでHTTP APIを公開する方法を段階的に学びます。

* **Google Apps Script（GAS）** で手軽にAPIを作る
* **AWS Lambda Function URL** で同等のAPIを作り、GASとの違いを比較する
* セキュリティ上の課題を認識し、暫定的な対策を実装する
* **API Gateway + WAF + Lambda** でより本格的・セキュアな構成を構築する

### サーバレスAPIの実行時間制限

サーバレスAPIを選ぶ際、実行時間制限は重要な判断材料です。

| サービス | プラン | 実行時間の上限 |
| --- | --- | --- |
| Google Apps Script | 無料版 | <strong>6分</strong> |
| Google Apps Script | Google Workspace（有料版） | <strong>30分</strong> |
| AWS Lambda | — | <strong>15分</strong> |

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

> aside positive
> 
> 本ハンズオンは初心者向けの内容です。GAS、Lambda、API Gateway、WAF を段階的に学んでいきます。

> aside negative
> 
> 本ハンズオンで作成するリソースには料金が発生する場合があります。ハンズオン終了後は必ずリソースを削除してください。


## 事前準備: AWS Builder ID の作成
Duration: 05:00


Kiro-IDE Remoteなどのツールを利用・連携するために、「**AWS Builder ID**」が必要となります。 AWS Builder ID は AWS や Amazon.co.jp アカウントとは異なる、個人のための無料アカウントです（クレジットカードの登録なども不要です）。

*  [AWS Builder ID の作成画面](https://builder.aws.com/start) にアクセスします。
* 個人のメールアドレスを入力し [次へ] をクリックします。
* 表示される「名前」を入力して [次へ] をクリックします。
* 入力したメールアドレス宛に届いた認証コードを入力して [認証] します。
* パスワードの条件（8〜64文字・大文字と小文字・数値・英数字以外の文字）を満たすパスワードを設定し、[AWS Builder IDを作成] をクリックします。

> aside positive
> 
> 詳しい画面遷移や Community.aws でのプロファイル作成方法については、 [こちらの記事 (AWS Builder ID の利用とその作成方法)](https://note.com/s_numaguchi/n/nd5126833389b) もあわせてご参照ください。


## 開発環境を準備する
Duration: 15:00


開発環境は以下の2つから選択できます。

### オプション1: GitHub Codespaces を使う場合

#### 新規リポジトリの作成

*  [GitHub](https://github.com/) にログインします
* 右上の **+** → **New repository** をクリックします
* 以下の内容で設定します

| 項目 | 値 |
| --- | --- |
| Repository name | 任意の名前（例: <code>aws-handson</code>） |
| Public / Private | どちらでもOK |
| Add a README file | <strong>✅ チェックを入れる</strong> |

4. **Create repository** をクリックします

#### Codespace の起動

* 作成したリポジトリの画面で **Code** ボタンをクリックします
* **Codespaces** タブ → **Create codespace on main** をクリックします
* Codespace の起動を待ちます（初回は2〜3分程度）

#### 開発ツールのインストール

Codespace が起動したら、ターミナルで以下のコマンドを実行し、必要なツールをインストールします。

```console
# AWS CLI のインストール
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip

# Python3 の最新化とエイリアス設定
sudo apt-get update && sudo apt-get install -y python3 python3-pip
echo 'alias python=python3' >> ~/.bashrc
echo 'alias pip=pip3' >> ~/.bashrc
source ~/.bashrc

# Node.js のインストール
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# npm の最新化
sudo npm install -g npm@latest

# clasp（Google Apps Script CLI）のインストール
sudo npm install -g @google/clasp
```

#### 動作確認

```console
aws --version; python -V; node -v; npm -v; clasp --version
```

それぞれバージョンが表示されればOKです。

#### clasp で Google アカウントにログイン

Codespace はリモート環境のため、ブラウザが直接開けません。`--no-localhost` オプションを使って認証します。

* Apps Script API を有効化します。ブラウザで以下のURLにアクセスし、トグルを **オン** にしますhttps://script.google.com/home/usersettings
* Codespace のターミナルで以下を実行します

```console
clasp login --no-localhost
```

3. 認証用のURLが表示されるので、そのURLをコピーしてブラウザで開きます
4. Google アカウントでログインし、アクセスを許可します
5. 表示された認証コードをコピーします
6. Codespace のターミナルに戻り、認証コードを貼り付けて Enter を押します

`Authorization successful.` と表示されればログイン完了です。

### オプション2: Kiro-IDE Remote を使う場合

AWS 上に簡単に Web 開発環境を構築できる **Kiro-IDE Remote** を使用します。ローカル PC に環境を構築することなく、また IAM の設定なども自動で行われるため、推奨される手順です。

#### Kiro-IDE の起動

以下のリンク先に用意されている「Deploy」ボタンから、ワンクリックでデプロイが可能です。

[Kiro IDE Remote のマニュアルページ](https://aws-samples.github.io/sample-one-click-generative-ai-solutions/solutions/kiro-ide/)

* サインイン済みの AWS アカウントがある状態で、マニュアルページ内の **[Deploy]** ボタンをクリックします。
* AWS CloudFormation の「スタックのクイック作成」画面が開きます。
* デプロイに必要な以下のパラメータを確認・入力します： 

* **UserEmail**: 構築完了メールや通知を受け取るご自身のメールアドレスを入力します。
* **Language**: OS の言語設定です。`JP`（日本語）を選択しておくことを推奨します。
* **EnableAdministratorAccess**: **重要**。本ハンズオンでは CloudFormation などの AWS リソースを作成・操作するため、必ず `true` に設定してください。これにより、Kiro-IDE のターミナルから AWS コマンドを実行するための権限（IAM ロール）が自動的に付与されます。
* 画面最下部の「AWS CloudFormation が IAM リソースを作成する場合があることを承認します。」にチェックを入れます。
* **[スタックの作成]** をクリックし、作成プロセスが完了（ステータスが `CREATE_COMPLETE` になる）するまで約5〜10分程度待ちます。 

* ※デプロイが開始されると、入力したメールアドレス宛に通知のサブスクリプション確認メールが届きます。「Confirm subscription」をクリックして承認を行ってください。
* デプロイが完了すると、「[One Click Gen AI Solutions] Kiro IDE - Deployment completed」というメールが届きます。本文（または CloudFormation の「出力(Outputs)」タブ）から以下の情報を確認します： 

* `KiroIDEURL`: アクセス用URL
* `Username`: ログインユーザー名
* `Password`: 初期パスワード
* 指定された URL にアクセスし、ユーザー名とパスワードでログインしてください。
* ログイン後、ブラウザ上で VS Code ライクなエディタとターミナルが使用できることを確認してください。 

* **エディタ**: 左側のファイルツリーからファイルを管理し、右側の画面で編集します。
* **ターミナル**: 画面下部（またはメニューの Terminal &gt; New Terminal）に表示される Linux シェルです。以降のコマンド操作はここで行います。
* **Session Manager プラグインのインストール**: Kiro 上の AI チャット機能（**Vibe**）を開き、「`Session Manager プラグインをインストールする`」と入力して送信します。AI が提示した手順やコマンドに従って、Session Manager プラグインをインストールしてください。

#### Kiro-IDE Remote の操作Tips

* **デスクトップの Kiro アイコン**: 最初は無効化されています。右クリックで起動を許可（Allow Launching）してから実行してください。
* **日本語入力**: `Ctrl + Space` で直接入力 / 日本語入力を切り替えられます。半角・全角キーでの切り替えを行いたい場合は、一度設定を再起動してください。
* **ターミナルへの貼り付け**: `Ctrl + Shift + V` を使用します（Linux の仕様です）。
* **Kiro CLI の認証**: 認証がなかなか進まない場合は `kiro-cli login --use-device-flow` を試してみてください。

> aside positive
> 
> Kiro-IDE Remote を使う場合、IAM ユーザーの作成やアクセスキーの発行は不要です。`EnableAdministratorAccess` を `true` にすることで、ターミナルから直接 AWS CLI を使用できます。次の「IAMユーザーの作成」と「AWS CLI の認証設定」のセクションはスキップしてください。

#### 開発ツールのインストール（Kiro-IDE Remote）

ターミナルで以下のコマンドを実行し、必要なツールをインストールします。

```console
# Python3 の最新化とエイリアス設定
sudo apt-get update && sudo apt-get install -y python3 python3-pip
echo 'alias python=python3' >> ~/.bashrc
echo 'alias pip=pip3' >> ~/.bashrc
source ~/.bashrc

# Node.js のインストール
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# npm の最新化
sudo npm install -g npm@latest

# clasp（Google Apps Script CLI）のインストール
sudo npm install -g @google/clasp
```

#### 動作確認

```console
aws --version; python -V; node -v; npm -v; clasp --version
```

それぞれバージョンが表示されればOKです。

#### clasp で Google アカウントにログイン

リモート環境のため、ブラウザが直接開けません。`--no-localhost` オプションを使って認証します。

* Apps Script API を有効化します。ブラウザで以下のURLにアクセスし、トグルを **オン** にしますhttps://script.google.com/home/usersettings
* ターミナルで以下を実行します

```console
clasp login --no-localhost
```

3. 認証用のURLが表示されるので、そのURLをコピーしてブラウザで開きます
4. Google アカウントでログインし、アクセスを許可します
5. 表示された認証コードをコピーします
6. ターミナルに戻り、認証コードを貼り付けて Enter を押します

`Authorization successful.` と表示されればログイン完了です。


## IAMユーザーの作成
Duration: 10:00


> aside negative
> 
> **Kiro-IDE Remote を使用している場合、このセクションと次の「AWS CLI の認証設定」はスキップしてください。** IAM ロールが自動的に付与されているため、アクセスキーの発行は不要です。

### IAMユーザーの作成手順

AWS CLI から AWS リソースを操作するために、IAM ユーザーを作成してアクセスキーを発行します。

```console
# IAMユーザーの作成
aws iam create-user --user-name handson-user

# AdministratorAccess ポリシーをアタッチ
aws iam attach-user-policy --user-name handson-user \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess

# アクセスキーの発行
aws iam create-access-key --user-name handson-user
```

出力される `AccessKeyId` と `SecretAccessKey` をメモします。

> aside positive
> 
> 本ハンズオンでは簡易化のため AdministratorAccess を付与しますが、AWS Organizations のSCP（サービスコントロールポリシー）により、実際に利用できるサービスは制限されています。本番環境では最小権限の原則に基づいた権限設定を行ってください。

> aside negative
> 
> シークレットアクセスキーはこのコマンド実行時にしか表示されません。必ずメモしてください。紛失した場合は、アクセスキーを削除して新しく作成し直す必要があります。


## AWS CLI の認証設定
Duration: 05:00


> aside negative
> 
> **Kiro-IDE Remote を使用している場合、このセクションはスキップしてください。**

### 認証情報の設定

Codespace のターミナルで以下のコマンドを実行し、先ほど発行したアクセスキーを設定します。

```console
aws configure
```

| 項目 | 値 |
| --- | --- |
| AWS Access Key ID | 発行したアクセスキー |
| AWS Secret Access Key | 発行したシークレットアクセスキー |
| Default region name | <code>ap-northeast-1</code> |
| Default output format | <code>json</code> |

### 設定の確認

```console
aws sts get-caller-identity
```

正しく設定されていれば、アカウントIDやユーザーARNが表示されます。

> aside negative
> 
> アクセスキーをGitリポジトリにコミットしないよう注意してください。`.gitignore` にAWS認証情報ファイルの除外設定が含まれていますが、環境変数やコード内にハードコードしないよう気をつけましょう。


## GASでWebアプリAPIを作成する
Duration: 15:00


### Google Apps Script プロジェクトの作成

Codespace のターミナルで clasp を使ってプロジェクトを作成します。

```console
mkdir -p ~/gas/04 && cd ~/gas/04
clasp create --title "handson-text-api" --type webapp
```

### コードの入力

作成された `Code.js` を以下の内容で上書きします。

```console
cat > Code.js << 'EOF'
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
EOF
```

### コードのアップロードとデプロイ

```console
# コードを Apps Script にアップロード
clasp push

# バージョンを作成
clasp version "初回デプロイ"

# Webアプリとしてデプロイ
clasp deploy --description "テキスト要約API"
```

デプロイIDが表示されます。WebアプリのURLは以下の形式です。

```
https://script.google.com/macros/s/{デプロイID}/exec
```

> aside positive
> 
> `clasp deployments` コマンドでデプロイ一覧を確認できます。

### 動作確認

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

> aside negative
> 
> GASのWebアプリURLは、URLを知っている人なら誰でもアクセスできます。また、無料版では実行時間が最大6分に制限されています。


## Lambda Function URLで同等のAPIを作成する
Duration: 20:00


### IAMロールの作成

Lambda関数用の実行ロールを作成します。

```console
mkdir -p ~/lambda/05 && cd ~/lambda/05

# 信頼ポリシーの作成
cat > trust-policy.json << 'EOF'
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
EOF

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

```console
# 作業ディレクトリの作成
cd ~/lambda/05

# コードファイルの作成
cat > lambda_function.py << 'EOF'
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
            body = event.get('body', '{}')
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
EOF

# zipファイルの作成
zip function.zip lambda_function.py

# アカウントIDの取得
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Lambda関数の作成
aws lambda create-function \
  --function-name handson-text-summarizer \
  --runtime python3.12 \
  --handler lambda_function.lambda_handler \
  --role arn:aws:iam::${ACCOUNT_ID}:role/handson-furl-lambda-role \
  --zip-file fileb://function.zip
```

### Function URLの有効化

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

> aside negative
> 
> 今回は GAS との比較のため `--auth-type NONE`（全ユーザーアクセス可能）で作成しています。本来は `--auth-type AWS_IAM` を指定することで、IAM認証済みのユーザー・ロールのみにアクセスを限定できます。IAM認証を使う場合、呼び出し側は SigV4 署名付きリクエストを送信する必要があります。詳細は  [Lambda Function URL のアクセス制御](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html) を参照してください。

Function URLを取得します。

```console
FUNCTION_URL=$(aws lambda get-function-url-config \
  --function-name handson-text-summarizer \
  --query FunctionUrl --output text)
echo $FUNCTION_URL
```

### 動作確認

```console
# GETリクエスト
curl $FUNCTION_URL

# POSTリクエスト
curl -X POST $FUNCTION_URL \
  -H "Content-Type: application/json" \
  -d '{"text": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。", "max_sentences": 2}'
```

> aside positive
> 
> GASとLambda、どちらも同じテキスト要約処理を実装しています。URLにアクセスするだけで動く手軽さは同じですが、実行時間制限やインフラの制御度に差があります。


## GAS vs Lambda Function URL の比較
Duration: 05:00


### 両者の比較

ここまでの実装を踏まえて、GASとLambda Function URLを比較します。

| 比較項目 | GAS（無料版） | GAS（有料版） | Lambda Function URL |
| --- | --- | --- | --- |
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

> aside negative
> 
> GASもLambda Function URLも、単体ではAPIキー認証やレートリミットなどのセキュリティ機能を持ちません。次のセクションで暫定的な対策を、その後に本格的な対策を学びます。


## セキュリティの暫定対策
Duration: 20:00


### 考え方

API GatewayやWAFを使わなくても、アプリケーションレベルでの認証チェックを導入することで、ある程度のアクセス制御が可能です。

* **GAS**: スプレッドシートにAPIキーを保存し、リクエストのキーと照合
* **Lambda**: DynamoDBにAPIキーを保存し、リクエストのキーと照合

### GAS側: スプレッドシートでのキー照合

#### スプレッドシートの準備

* Google スプレッドシートを新規作成します
* シート名を `APIKeys` に変更します
* A1セルに `key`、B1セルに `description` と入力します
* A2セルにAPIキー（例: `handson-demo-key-2026`）を入力します
* スプレッドシートのIDをメモします（URLの `/d/` と `/edit` の間の文字列）

#### GASコードの更新

`~/gas/06/Code.js` を以下に更新します。

```console
mkdir -p ~/gas/06 && cd ~/gas/06
clasp create --title "handson-text-api-v2" --type webapp
cat > Code.js << 'EOF'
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
  var keys = sheet.getRange("A2:A" + sheet.getLastRow()).getValues();

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
EOF
```

> aside negative
> 
> GASでは `doPost` の引数 `e` にリクエストヘッダーを直接取得する方法が限定的なため、ここではリクエストボディの `api_key` フィールドで照合しています。

#### GASの再デプロイ

```console
clasp push
clasp version "APIキー認証追加"
clasp deploy --description "APIキー認証付きテキスト要約API"
```

#### テスト

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

```console
aws dynamodb create-table \
  --table-name handson-api-keys \
  --attribute-definitions AttributeName=api_key,AttributeType=S \
  --key-schema AttributeName=api_key,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

#### APIキーの登録

```console
aws dynamodb put-item \
  --table-name handson-api-keys \
  --item '{"api_key": {"S": "handson-demo-key-2026"}}'
```

#### IAMロールの更新

Lambda関数がDynamoDBにアクセスできるよう、ポリシーを追加します。

```console
aws iam attach-role-policy \
  --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
```

#### Lambda関数コードの更新

Lambda関数のコードを以下に更新します。

```console
mkdir -p ~/lambda/06 && cd ~/lambda/06
cat > lambda_function.py << 'EOF'
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
EOF

# zipファイルの作成とデプロイ
zip function.zip lambda_function.py
aws lambda update-function-code \
  --function-name handson-text-summarizer \
  --zip-file fileb://function.zip
```

#### テスト

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
| --- | --- |
| レートリミットなし | 大量リクエストを防げない |
| DDoS対策なし | エンドポイントへの攻撃を防げない |
| キー管理の煩雑さ | キーのローテーションや失効管理が手動 |
| ログ・監査 | APIの利用状況を体系的に把握しづらい |

> aside positive
> 
> 暫定対策は小規模なプロトタイプやデモでは有効ですが、本格運用には次に学ぶAPI Gateway + WAFの構成が推奨されます。


## API Gatewayの構築
Duration: 15:00


### 本格的なAPI構成へ

ここからは、Lambda Function URLの代わりにAPI Gatewayを使った本格的な構成を構築します。

### Lambda関数の準備

API Gateway用にLambda関数を更新します。既存の `handson-text-summarizer` のコードを以下に更新します。
 （DynamoDBのAPIキー認証は、API Gateway側のAPIキー認証に置き換えるため削除します）

```console
mkdir -p ~/lambda/07 && cd ~/lambda/07
cat > lambda_function.py << 'EOF'
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
            body = event.get('body', '{}')
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
EOF

zip function.zip lambda_function.py
aws lambda update-function-code \
  --function-name handson-text-summarizer \
  --zip-file fileb://function.zip
```

> aside positive
> 
> API Gatewayの「Lambdaプロキシ統合」を使用する場合、イベント形式が Function URL とは異なります。`httpMethod` でHTTPメソッドを判定する点に注意してください。

### Function URLの削除

API Gateway経由に切り替えるため、既存のFunction URLを削除します。

```console
aws lambda delete-function-url-config --function-name handson-text-summarizer
aws lambda remove-permission --function-name handson-text-summarizer \
  --statement-id FunctionURLAllowPublicAccess
```

### REST APIの作成

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

### メソッドの作成（GET・POST）

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

```console
aws lambda add-permission \
  --function-name handson-text-summarizer \
  --statement-id apigateway-invoke \
  --action lambda:InvokeFunction \
  --principal apigateway.amazonaws.com \
  --source-arn "arn:aws:execute-api:${REGION}:${ACCOUNT_ID}:${API_ID}/*"
```

### APIのデプロイ

```console
aws apigateway create-deployment \
  --rest-api-id $API_ID \
  --stage-name dev

echo "Endpoint: https://${API_ID}.execute-api.${REGION}.amazonaws.com/dev/summarize"
```

### 動作確認

```console
API_URL="https://${API_ID}.execute-api.${REGION}.amazonaws.com/dev/summarize"

curl $API_URL

curl -X POST $API_URL \
  -H "Content-Type: application/json" \
  -d '{"text": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。", "max_sentences": 2}'
```


## APIキー認証の追加
Duration: 15:00


### 使用量プランの作成

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

### メソッドにAPIキー要求を設定

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

> aside positive
> 
> API Gatewayの`x-api-key`ヘッダーによる認証は、DynamoDBによる暫定対策と比べて、レートリミット・使用量制御・キー管理が組み込みで提供されます。


## AWS WAFの構築と連携
Duration: 20:00


### AWS WAFとは

AWS WAF（Web Application Firewall）は、Webアプリケーションを一般的な攻撃から保護するサービスです。
 API Gatewayと連携することで、APIに対する不正アクセスを自動的にブロックできます。

### Web ACLの作成

```console
# API GatewayのARNを取得
API_GW_ARN="arn:aws:apigateway:${REGION}::/restapis/${API_ID}/stages/dev"

# Web ACLの作成（マネージドルール + レートベースルール付き）
WAF_ACL_ARN=$(aws wafv2 create-web-acl \
  --name handson-api-waf \
  --scope REGIONAL \
  --region $REGION \
  --default-action Allow={} \
  --description "ハンズオンAPI用WAF" \
  --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=handson-api-waf \
  --rules '[
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
  ]' \
  --query Summary.ARN --output text)
echo "WAF ACL ARN: $WAF_ACL_ARN"
```

| ルールグループ | 説明 |
| --- | --- |
| AWSManagedRulesCommonRuleSet | 一般的なWebアプリケーション攻撃を防御 |
| AWSManagedRulesKnownBadInputsRuleSet | 既知の悪意のある入力パターンを検出 |
| handson-rate-limit | 5分あたり100リクエストを超えるとブロック |

### API Gatewayとの関連付け

```console
aws wafv2 associate-web-acl \
  --web-acl-arn $WAF_ACL_ARN \
  --resource-arn $API_GW_ARN \
  --region $REGION
```

> aside positive
> 
> マネージドルールはAWSが管理・更新するため、最新のセキュリティ脅威に自動的に対応できます。


## WAFの動作確認
Duration: 10:00


### 正常アクセスの確認

APIキーを使って正常にアクセスできることを確認します。

```console
curl -H "x-api-key: $API_KEY" $API_URL
```

正常なレスポンスが返れば、WAFが正常なリクエストを通過させていることを確認できます。

### SQLインジェクション攻撃のテスト

WAFが悪意のあるリクエストをブロックすることを確認します。

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

```console
# 連続リクエストでレートリミットをテスト
for i in $(seq 1 120); do
  echo "Request $i: $(curl -s -o /dev/null -w '%{http_code}' \
    -H "x-api-key: $API_KEY" \
    $API_URL)"
done
```

100リクエストを超えた辺りから `403` レスポンスが返り始めれば、レートリミットが機能しています。

> aside negative
> 
> レートベースのルールは5分間隔で評価されるため、即座にブロックされるわけではありません。テスト時はこの点を考慮してください。

### 構成の進化を振り返る

| 構成 | 認証 | レートリミット | 攻撃防御 | 運用負荷 |
| --- | --- | --- | --- | --- |
| GAS（単体） | なし | GAS制限のみ | なし | 低 |
| GAS + スプレッドシート照合 | 簡易キー | なし | なし | 中 |
| Lambda Function URL（単体） | なし | なし | なし | 低 |
| Lambda + DynamoDB照合 | 簡易キー | なし | なし | 中 |
| <strong>API Gateway + APIキー</strong> | <strong>APIキー</strong> | <strong>✅</strong> | なし | 中 |
| <strong>API Gateway + WAF + Lambda</strong> | <strong>APIキー</strong> | <strong>✅</strong> | <strong>✅</strong> | 中〜高 |


## リソースの削除
Duration: 10:00


### 作成したリソースの削除

ハンズオンが完了したら、以下のコマンドでリソースを削除して料金の発生を防ぎましょう。

#### WAF Web ACLの削除

```console
WAF_ACL_ID=$(aws wafv2 list-web-acls --scope REGIONAL --region ap-northeast-1 \
  --query "WebACLs[?Name=='handson-api-waf'].Id" --output text)
WAF_ACL_LOCK=$(aws wafv2 get-web-acl --name handson-api-waf --scope REGIONAL \
  --id $WAF_ACL_ID --region ap-northeast-1 --query "LockToken" --output text)
aws wafv2 delete-web-acl --name handson-api-waf --scope REGIONAL \
  --id $WAF_ACL_ID --lock-token $WAF_ACL_LOCK --region ap-northeast-1
```

#### API Gateway関連の削除

```console
API_ID=$(aws apigateway get-rest-apis \
  --query "items[?name=='handson-text-summarizer-api'].id" --output text)
KEY_ID=$(aws apigateway get-api-keys \
  --query "items[?name=='handson-test-key'].id" --output text)
PLAN_ID=$(aws apigateway get-usage-plans \
  --query "items[?name=='handson-basic-plan'].id" --output text)

aws apigateway delete-api-key --api-key $KEY_ID
aws apigateway delete-usage-plan --usage-plan-id $PLAN_ID
aws apigateway delete-rest-api --rest-api-id $API_ID
```

#### DynamoDBテーブルの削除

```console
aws dynamodb delete-table --table-name handson-api-keys
```

#### Lambda関数の削除

```console
aws lambda delete-function --function-name handson-text-summarizer
```

#### IAMロールの削除

```console
aws iam detach-role-policy --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
aws iam detach-role-policy --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
aws iam delete-role --role-name handson-furl-lambda-role
```

#### IAMユーザーの削除

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

```console
cd ~/gas/04 && clasp undeploy --all
cd ~/gas/06 && clasp undeploy --all
```

#### 作業ディレクトリの削除

```console
rm -rf ~/gas ~/lambda
```

#### GitHub Codespace の削除

不要であれば GitHub の  [Codespaces 管理画面](https://github.com/codespaces) から Codespace を削除します。

> aside negative
> 
> リソースの削除を忘れると、特にWAFとAPI Gatewayで意図しない料金が発生する可能性があります。必ず全てのリソースを削除してください。


## まとめ
Duration: 05:00


### 学んだこと

このハンズオンでは、サーバレスAPIの構築と保護について段階的に学びました。

| ステップ | 内容 |
| --- | --- |
| GAS Webアプリ | 最も手軽なAPI公開方法を体験 |
| Lambda Function URL | AWS上での同等構成を体験 |
| GAS vs Lambda 比較 | 実行時間制限・コスト・制約の違い |
| 暫定セキュリティ対策 | スプレッドシート/DynamoDBでのキー照合 |
| API Gateway | 本格的なAPI管理基盤 |
| APIキー認証 | アクセス制御とレートリミット |
| AWS WAF | Web攻撃からの保護 |

### ハンズオンシリーズの振り返り

| # | テーマ | 使用サービス |
| --- | --- | --- |
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


  [AWS Lambda Function URL ドキュメント](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-urls.html)

  [Amazon API Gateway ドキュメント](https://docs.aws.amazon.com/ja_jp/apigateway/)

  [AWS WAF ドキュメント](https://docs.aws.amazon.com/ja_jp/waf/)

  [Google Apps Script ドキュメント](https://developers.google.com/apps-script)


