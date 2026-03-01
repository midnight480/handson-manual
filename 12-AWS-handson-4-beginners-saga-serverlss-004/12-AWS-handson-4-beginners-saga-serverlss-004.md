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
* GitHub Codespaces でAWS CLIが利用可能であること（[環境構築ハンズオン](../00-Install-AWS-CLI-to-RPI/web/) を参照）

Positive
: 本ハンズオンは初心者向けの内容です。GAS、Lambda、API Gateway、WAF を段階的に学んでいきます。

Negative
: 本ハンズオンで作成するリソースには料金が発生する場合があります。ハンズオン終了後は必ずリソースを削除してください。

## GASでWebアプリAPIを作成する
Duration: 0:15:00

### Google Apps Script プロジェクトの作成

1. ブラウザで [Google Apps Script](https://script.google.com/) にアクセスします
2. **新しいプロジェクト** をクリックします
3. プロジェクト名を `handson-text-api` に変更します

### コードの入力

デフォルトの `コード.gs` を以下の内容に書き換えます。

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

### Webアプリとしてデプロイ

1. **デプロイ** → **新しいデプロイ** をクリックします
2. 種類の選択で **ウェブアプリ** を選択します

| 項目 | 値 |
|------|-----|
| 説明 | テキスト要約API |
| 次のユーザーとして実行 | 自分 |
| アクセスできるユーザー | 全員 |

3. **デプロイ** をクリックします
4. 表示されたURLをメモします

### 動作確認

```console
# GETリクエスト
curl -L "https://script.google.com/macros/s/{デプロイID}/exec"

# POSTリクエスト
curl -L -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。", "max_sentences": 2}' \
  "https://script.google.com/macros/s/{デプロイID}/exec"
```

Negative
: GASのWebアプリURLは、URLを知っている人なら誰でもアクセスできます。また、無料版では実行時間が最大6分に制限されています。

## Lambda Function URLで同等のAPIを作成する
Duration: 0:20:00

### IAMロールの作成

1. AWSマネジメントコンソールから **IAM** を選択します
2. **ロール** → **ロールを作成** をクリックします

| 項目 | 値 |
|------|-----|
| 信頼されたエンティティ | AWS のサービス |
| ユースケース | Lambda |
| ロール名 | `handson-furl-lambda-role` |

以下のポリシーをアタッチします。

```
CloudWatchLogsFullAccess
```

### Lambda関数の作成

1. **Lambda** コンソールから **関数の作成** をクリックします

| 項目 | 値 |
|------|-----|
| 関数名 | `handson-text-summarizer` |
| ランタイム | Python 3.12 |
| アーキテクチャ | x86_64 |
| 実行ロール | `handson-furl-lambda-role`（既存のロールを使用） |

### コードの入力

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
```

3. **Deploy** をクリックして関数をデプロイします

### Function URLの有効化

1. **設定** タブ → **関数URL** → **関数URLの作成** をクリックします

| 項目 | 値 |
|------|-----|
| 認証タイプ | `NONE` |
| CORS - オリジンを許可 | `*` |
| CORS - メソッドを許可 | `GET`, `POST` |
| CORS - ヘッダーを許可 | `Content-Type` |

2. **保存** をクリックし、発行されたURLをメモします

### 動作確認

```console
# GETリクエスト
curl https://{Function URL}/

# POSTリクエスト
curl -X POST https://{Function URL}/ \
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

`コード.gs` を以下に更新し、再デプロイします。

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
```

Negative
: GASでは `doPost` の引数 `e` にリクエストヘッダーを直接取得する方法が限定的なため、ここではリクエストボディの `api_key` フィールドで照合しています。

#### GASの再デプロイ

1. **デプロイ** → **デプロイの管理** をクリック
2. 鉛筆アイコンをクリックして **バージョン** を「新しいバージョン」に変更
3. **デプロイ** をクリック

#### テスト

```console
# APIキーなし → エラー
curl -L -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "テストです。要約します。"}' \
  "https://script.google.com/macros/s/{デプロイID}/exec"

# APIキーあり → 成功
curl -L -X POST \
  -H "Content-Type: application/json" \
  -d '{"api_key": "handson-demo-key-2026", "text": "テストです。要約します。", "max_sentences": 1}' \
  "https://script.google.com/macros/s/{デプロイID}/exec"
```

### Lambda側: DynamoDBでのキー照合

#### DynamoDBテーブルの作成

1. AWSマネジメントコンソールから **DynamoDB** を選択します
2. **テーブルの作成** をクリックします

| 項目 | 値 |
|------|-----|
| テーブル名 | `handson-api-keys` |
| パーティションキー | `api_key`（文字列） |
| テーブルクラス | DynamoDB Standard |
| キャパシティモード | オンデマンド |

3. **テーブルの作成** をクリックします

#### APIキーの登録

1. 作成した `handson-api-keys` テーブルを開きます
2. **項目を探索** → **項目を作成** をクリック
3. 以下のアイテムを追加します

| 属性 | 値 |
|------|-----|
| api_key | `handson-demo-key-2026` |

#### IAMロールの更新

Lambda関数がDynamoDBにアクセスできるよう、ポリシーを追加します。

1. IAMコンソールで `handson-furl-lambda-role` を開きます
2. **ポリシーをアタッチ** をクリック
3. `AmazonDynamoDBReadOnlyAccess` を追加します

#### Lambda関数コードの更新

Lambda関数のコードを以下に更新します。

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

**Deploy** をクリックして関数を更新します。

#### テスト

```console
# APIキーなし → 403
curl -X POST https://{Function URL}/ \
  -H "Content-Type: application/json" \
  -d '{"text": "テストです。"}'

# APIキーあり → 200
curl -X POST https://{Function URL}/ \
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
```

**Deploy** をクリックして更新します。

Positive
: API Gatewayの「Lambdaプロキシ統合」を使用する場合、イベント形式が Function URL とは異なります。`httpMethod` でHTTPメソッドを判定する点に注意してください。

### Function URLの削除

API Gateway経由に切り替えるため、既存のFunction URLを削除します。

1. Lambda関数の **設定** → **関数URL** → **削除**

### REST APIの作成

1. AWSマネジメントコンソールから **API Gateway** を選択します
2. **APIを作成** → **REST API** の **構築** をクリックします

| 項目 | 値 |
|------|-----|
| API名 | `handson-text-summarizer-api` |
| 説明 | テキスト要約REST API |
| エンドポイントタイプ | リージョン |

3. **APIの作成** をクリックします

### リソースとメソッドの作成

1. **リソースの作成** をクリックします

| 項目 | 値 |
|------|-----|
| リソース名 | `summarize` |
| CORS | 有効にする |

2. `/summarize` を選択 → **メソッドの作成** をクリック（GETとPOSTの2つ作成）

| 項目 | 値 |
|------|-----|
| 統合タイプ | Lambda関数 |
| Lambdaプロキシ統合 | 有効 |
| Lambda関数 | `handson-text-summarizer` |

### APIのデプロイ

1. **APIのデプロイ** をクリックします

| 項目 | 値 |
|------|-----|
| ステージ | *新しいステージ* |
| ステージ名 | `dev` |

2. **デプロイ** をクリックし、エンドポイントURLをメモします

```
https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize
```

### 動作確認

```console
curl https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize

curl -X POST https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "AWSは包括的なクラウドプラットフォームです。200以上のサービスを提供しています。多くの企業がAWSを利用しています。", "max_sentences": 2}'
```

## APIキー認証の追加
Duration: 0:15:00

### 使用量プランの作成

1. API Gatewayコンソールの **使用量プラン** → **作成** をクリックします

| 項目 | 値 |
|------|-----|
| プラン名 | `handson-basic-plan` |
| スロットリング - レート | 10（リクエスト/秒） |
| スロットリング - バースト | 5 |
| クォータ | 1000リクエスト/日 |

2. APIステージ `handson-text-summarizer-api` / `dev` を関連付けます

### APIキーの作成

1. **APIキーの作成と使用量プランへの追加** をクリックします

| 項目 | 値 |
|------|-----|
| 名前 | `handson-test-key` |
| 自動生成 | 有効 |

2. 作成されたキーの値をメモします

### メソッドにAPIキー要求を設定

1. `/summarize` の **GET** と **POST** 両方のメソッドで、**APIキーが必須** を `true` に設定します
2. **APIのデプロイ** で `dev` ステージに再デプロイします

### テスト

```console
# APIキーなし → 403 Forbidden
curl https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize

# APIキーあり → 200 OK
curl -H "x-api-key: {あなたのAPIキー}" \
  https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize

# POSTリクエスト + APIキー
curl -X POST \
  -H "x-api-key: {あなたのAPIキー}" \
  -H "Content-Type: application/json" \
  -d '{"text": "テストです。要約します。", "max_sentences": 1}' \
  https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize
```

Positive
: API Gatewayの`x-api-key`ヘッダーによる認証は、DynamoDBによる暫定対策と比べて、レートリミット・使用量制御・キー管理が組み込みで提供されます。

## AWS WAFの構築と連携
Duration: 0:20:00

### AWS WAFとは

AWS WAF（Web Application Firewall）は、Webアプリケーションを一般的な攻撃から保護するサービスです。  
API Gatewayと連携することで、APIに対する不正アクセスを自動的にブロックできます。

### Web ACLの作成

1. AWSマネジメントコンソールから **WAF & Shield** を選択します
2. **Web ACLs** → **Create web ACL** をクリックします

| 項目 | 値 |
|------|-----|
| Name | `handson-api-waf` |
| Description | ハンズオンAPI用WAF |
| Resource type | Regional resources |
| Region | Asia Pacific (Tokyo) |

3. **Associated AWS resources** の **Add AWS resources** をクリックします
4. リソースタイプ **Amazon API Gateway REST API** を選択し、`handson-text-summarizer-api` の `dev` ステージを追加します
5. **Next** をクリックします

### マネージドルールの追加

1. **Add managed rule groups** をクリックします
2. **AWS managed rule groups** を展開します
3. 以下のルールグループを **Add to web ACL** でオンにします

| ルールグループ | 説明 |
|--------------|------|
| AWSManagedRulesCommonRuleSet | 一般的なWebアプリケーション攻撃を防御 |
| AWSManagedRulesKnownBadInputsRuleSet | 既知の悪意のある入力パターンを検出 |

4. **Add rules** をクリックします

### レートベースルールの追加

大量リクエストによるDDoS攻撃を防ぐため、レートベースのルールを追加します。

1. **Add my own rules and rule groups** → **Rule builder** を選択します

| 項目 | 値 |
|------|-----|
| Name | `handson-rate-limit` |
| Type | Rate-based rule |
| Rate limit | 100（5分あたり） |
| Action | Block |

2. **Add rule** をクリックします

### デフォルトアクションの設定

| 項目 | 値 |
|------|-----|
| Default web ACL action for requests that don't match any rules | Allow |

3. **Next** → **Next** → **Create web ACL** をクリックします

Positive
: マネージドルールはAWSが管理・更新するため、最新のセキュリティ脅威に自動的に対応できます。

## WAFの動作確認
Duration: 0:10:00

### 正常アクセスの確認

APIキーを使って正常にアクセスできることを確認します。

```console
curl -H "x-api-key: {あなたのAPIキー}" \
  https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize
```

正常なレスポンスが返れば、WAFが正常なリクエストを通過させていることを確認できます。

### WAFの監視ダッシュボード

1. **WAF & Shield** コンソールで `handson-api-waf` を選択します
2. **Overview** タブでリクエスト数とブロック数を確認します

### SQLインジェクション攻撃のテスト

WAFが悪意のあるリクエストをブロックすることを確認します。

```console
# SQLインジェクション風のリクエスト → WAFがブロック
curl -X POST \
  -H "x-api-key: {あなたのAPIキー}" \
  -H "Content-Type: application/json" \
  -d '{"text": "SELECT * FROM users; DROP TABLE users;--"}' \
  https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize
```

WAFがブロックした場合、`403 Forbidden` が返ります。

### レートリミットのテスト

短時間に大量のリクエストを送信して、レートリミットが機能することを確認します。

```console
# 連続リクエストでレートリミットをテスト
for i in $(seq 1 120); do
  echo "Request $i: $(curl -s -o /dev/null -w '%{http_code}' \
    -H 'x-api-key: {あなたのAPIキー}' \
    https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/summarize)"
done
```

100リクエストを超えた辺りから `403` レスポンスが返り始めれば、レートリミットが機能しています。

Negative
: レートベースのルールは5分間隔で評価されるため、即座にブロックされるわけではありません。テスト時はこの点を考慮してください。

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

ハンズオンが完了したら、以下のリソースを削除して料金の発生を防ぎましょう。

削除順序は以下の通りです。

1. **AWS WAF** Web ACL `handson-api-waf` の削除
   * WAF & Shield → Web ACLs → `handson-api-waf` → Delete
2. **APIキー** `handson-test-key` の削除
3. **使用量プラン** `handson-basic-plan` の削除
4. **API Gateway** `handson-text-summarizer-api` の削除
5. **DynamoDBテーブル** `handson-api-keys` の削除
6. **Lambda関数** `handson-text-summarizer` の削除
7. **IAMロール** `handson-furl-lambda-role` の削除
8. **GASプロジェクト** `handson-text-api` の削除（任意）
9. **スプレッドシート** `APIKeys` の削除（任意）

### AWS CLIでの一括削除

```console
# WAF Web ACLの削除
WAF_ACL_ID=$(aws wafv2 list-web-acls --scope REGIONAL --region ap-northeast-1 \
  --query "WebACLs[?Name=='handson-api-waf'].Id" --output text)
WAF_ACL_LOCK=$(aws wafv2 get-web-acl --name handson-api-waf --scope REGIONAL \
  --id $WAF_ACL_ID --region ap-northeast-1 --query "LockToken" --output text)
aws wafv2 delete-web-acl --name handson-api-waf --scope REGIONAL \
  --id $WAF_ACL_ID --lock-token $WAF_ACL_LOCK --region ap-northeast-1

# API Gateway関連の削除
API_ID=$(aws apigateway get-rest-apis \
  --query "items[?name=='handson-text-summarizer-api'].id" --output text)
KEY_ID=$(aws apigateway get-api-keys \
  --query "items[?name=='handson-test-key'].id" --output text)
PLAN_ID=$(aws apigateway get-usage-plans \
  --query "items[?name=='handson-basic-plan'].id" --output text)

aws apigateway delete-api-key --api-key $KEY_ID
aws apigateway delete-usage-plan --usage-plan-id $PLAN_ID
aws apigateway delete-rest-api --rest-api-id $API_ID

# DynamoDBテーブルの削除
aws dynamodb delete-table --table-name handson-api-keys

# Lambda関数の削除
aws lambda delete-function --function-name handson-text-summarizer

# IAMロールの削除
aws iam detach-role-policy --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
aws iam detach-role-policy --role-name handson-furl-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess
aws iam delete-role --role-name handson-furl-lambda-role
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
