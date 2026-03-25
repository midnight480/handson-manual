author: Shibao,Tetsuya
summary: ローカルテキストファイルの翻訳・音声化・文字起こし - Lambda, Step Functions, S3, Translate, Polly, Transcribe を使ったサーバレスハンズオン
id: 09-AWS-handson-4-beginners-saga-serverlss-001
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# ローカルテキストファイルの翻訳・音声化・文字起こしハンズオン

## はじめに
Duration: 0:05:00

### ハンズオンの概要

このハンズオンでは、AWSのサーバレスサービスを活用して、ローカルのテキストファイルをアップロードし、翻訳・音声化・文字起こしを行うシステムを構築します。テキストから音声への変換（Polly）と、音声からテキストへの変換（Transcribe）の双方向変換を体験できます。

### 構成図

以下のAWSサービスを使用します。

* **Amazon S3** - テキストファイルのアップロード先・出力先ストレージ
* **AWS Lambda** - 各処理のビジネスロジック実行
* **AWS Step Functions** - ワークフローのオーケストレーション
* **Amazon Translate** - テキストの翻訳処理
* **Amazon Polly** - テキストの音声化処理（Text-to-Speech）
* **Amazon Transcribe** - 音声の文字起こし処理（Speech-to-Text）

### 処理フロー

**フェーズ1: テキスト → 音声（Text-to-Speech）**

1. ユーザーがテキストファイルをS3にアップロード
2. S3イベントがStep Functionsのワークフローを起動
3. Lambda関数がテキストファイルを読み取り
4. Amazon Translateで翻訳
5. Amazon Pollyで音声ファイルに変換
6. 結果をS3に保存

**フェーズ2: 音声 → テキスト（Speech-to-Text）**

7. Pollyで生成した音声ファイルに対してAmazon Transcribeで文字起こし
8. 文字起こし結果をS3に保存
9. 元のテキストと文字起こし結果を比較

### 前提条件

* AWSアカウントを持っていること
* GitHubアカウントを持っていること
* AWS マネジメントコンソールにログインできること

Positive
: 本ハンズオンは初心者向けの内容です。AWSの基本的な操作ができれば問題ありません。

Negative
: 本ハンズオンで作成するリソースには料金が発生する場合があります。ハンズオン終了後は必ずリソースを削除してください。

## GitHub Codespaces で開発環境を準備する
Duration: 0:10:00

### テンプレートからリポジトリを作成

1. [GitHub](https://github.com/) にログインします
2. テンプレートリポジトリ [midnight480/aws-handson-template](https://github.com/midnight480/aws-handson-template) を開きます
3. **Use this template** → **Create a new repository** をクリックします
4. リポジトリ名に任意の名前を入力し、**Create repository** をクリックします

### Codespace の起動

1. 作成したリポジトリの画面で **Code** ボタンをクリックします
2. **Codespaces** タブ → **Create codespace on main** をクリックします
3. Codespace の起動を待ちます（初回は3〜5分程度）

Positive
: テンプレートリポジトリには開発環境の設定（devcontainer）が含まれており、AWS CLI や Python 3.12 が自動的にインストールされます。

### AWS CLI の動作確認

Codespace が起動したら、ターミナルで AWS CLI がインストールされていることを確認します。

```console
aws --version
```

`aws-cli/2.x.x` のようにバージョンが表示されればOKです。

## IAMユーザーの作成
Duration: 0:10:00

### IAMユーザーの作成手順

AWS CLI から AWS リソースを操作するために、IAM ユーザーを作成してアクセスキーを発行します。

1. AWS マネジメントコンソールにログインします
2. サービス一覧から **IAM** を選択します
3. 左メニューの **ユーザー** をクリックします
4. **ユーザーを作成** をクリックします

| 項目 | 値 |
|------|-----|
| ユーザー名 | `handson-user`（任意の名前） |
| AWS マネジメントコンソールへのアクセスを提供 | チェック不要 |

5. **次へ** をクリックします

### 許可の設定

1. **ポリシーを直接アタッチする** を選択します
2. 検索ボックスに `AdministratorAccess` と入力します
3. **AdministratorAccess** にチェックを入れます
4. **次へ** をクリックします
5. 内容を確認し、**ユーザーの作成** をクリックします

Positive
: 本ハンズオンでは簡易化のため AdministratorAccess を付与しますが、AWS Organizations のSCP（サービスコントロールポリシー）により、実際に利用できるサービスは制限されています。本番環境では最小権限の原則に基づいた権限設定を行ってください。

### アクセスキーの発行

1. 作成したユーザーの詳細画面を開きます
2. **セキュリティ認証情報** タブをクリックします
3. **アクセスキー** セクションの **アクセスキーを作成** をクリックします
4. ユースケースで **コマンドラインインターフェイス (CLI)** を選択します
5. 確認のチェックボックスにチェックを入れ、**次へ** をクリックします
6. **アクセスキーを作成** をクリックします
7. **アクセスキー** と **シークレットアクセスキー** をメモします

Negative
: シークレットアクセスキーはこの画面でしか確認できません。必ずメモしてください。紛失した場合は、アクセスキーを削除して新しく作成し直す必要があります。

## AWS CLI の認証設定
Duration: 0:05:00

### 認証情報の設定

Codespace のターミナルで以下のコマンドを実行し、先ほど発行したアクセスキーを設定します。

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

正しく設定されていれば、アカウントIDやユーザーARNが表示されます。

Negative
: アクセスキーをGitリポジトリにコミットしないよう注意してください。`.gitignore` にAWS認証情報ファイルの除外設定が含まれていますが、環境変数やコード内にハードコードしないよう気をつけましょう。

## S3バケットの作成
Duration: 0:10:00

### 入力用バケットの作成

テキストファイルをアップロードするためのS3バケットを作成します。

1. AWSマネジメントコンソールにログインします
2. サービス一覧から **S3** を選択します
3. **バケットを作成** をクリックします

以下の設定でバケットを作成します。

| 項目 | 値 |
|------|-----|
| バケット名 | `handson-input-{あなたのアカウントID}` |
| AWSリージョン | `ap-northeast-1（東京）` |
| その他設定 | デフォルトのまま |

4. **バケットを作成** をクリックして完了します

### 出力用バケットの作成

翻訳結果と音声ファイルを格納するS3バケットを作成します。

同様の手順で以下の設定のバケットを作成します。

| 項目 | 値 |
|------|-----|
| バケット名 | `handson-output-{あなたのアカウントID}` |
| AWSリージョン | `ap-northeast-1（東京）` |
| その他設定 | デフォルトのまま |

Positive
: S3バケット名はグローバルで一意である必要があります。アカウントIDを含めることで重複を避けましょう。

## IAMロールの作成
Duration: 0:10:00

### Lambda用IAMロール

Lambda関数がS3、Translate、Polly、Transcribeにアクセスするためのロールを作成します。

1. AWSマネジメントコンソールから **IAM** を選択します
2. 左メニューの **ロール** をクリックします
3. **ロールを作成** をクリックします

以下の設定でロールを作成します。

| 項目 | 値 |
|------|-----|
| 信頼されたエンティティ | AWS のサービス |
| ユースケース | Lambda |
| ロール名 | `handson-lambda-role` |

以下のポリシーをアタッチします。

```
AmazonS3FullAccess
AmazonTranslateFullAccess
AmazonPollyFullAccess
AmazonTranscribeFullAccess
CloudWatchLogsFullAccess
```

Negative
: 本ハンズオンでは簡易化のためFullAccessポリシーを使用しますが、本番環境では最小権限の原則に基づいたポリシーを設定してください。

### Step Functions用IAMロール

同様の手順で、Step Functions用のロールを作成します。

| 項目 | 値 |
|------|-----|
| 信頼されたエンティティ | AWS のサービス |
| ユースケース | Step Functions |
| ロール名 | `handson-stepfunctions-role` |

以下のポリシーをアタッチします。

```
AWSLambda_FullAccess
CloudWatchLogsFullAccess
```

## Lambda関数の作成（テキスト読み取り）
Duration: 0:15:00

### 関数の作成

1. AWSマネジメントコンソールから **Lambda** を選択します
2. **関数の作成** をクリックします

| 項目 | 値 |
|------|-----|
| 関数名 | `handson-read-text` |
| ランタイム | Python 3.12 |
| 実行ロール | `handson-lambda-role`（既存のロールを使用） |

### コードの入力

以下のコードを入力します。

```python
import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """S3からテキストファイルを読み取る"""

    bucket = event['bucket']
    key = event['key']

    # S3からファイルを取得
    response = s3.get_object(Bucket=bucket, Key=key)
    text = response['Body'].read().decode('utf-8')

    return {
        'statusCode': 200,
        'bucket': bucket,
        'key': key,
        'text': text,
        'source_language': 'ja'
    }
```

3. **Deploy** をクリックして関数をデプロイします

## Lambda関数の作成（翻訳処理）
Duration: 0:15:00

### 関数の作成

新しいLambda関数を作成します。

| 項目 | 値 |
|------|-----|
| 関数名 | `handson-translate-text` |
| ランタイム | Python 3.12 |
| 実行ロール | `handson-lambda-role`（既存のロールを使用） |

### コードの入力

以下のコードを入力します。

```python
import json
import boto3

translate = boto3.client('translate')

def lambda_handler(event, context):
    """テキストを英語に翻訳する"""

    text = event['text']
    source_language = event.get('source_language', 'ja')
    target_language = 'en'

    # Amazon Translateで翻訳
    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_language,
        TargetLanguageCode=target_language
    )

    translated_text = response['TranslatedText']

    return {
        'statusCode': 200,
        'bucket': event['bucket'],
        'key': event['key'],
        'original_text': text,
        'translated_text': translated_text,
        'source_language': source_language,
        'target_language': target_language
    }
```

3. **Deploy** をクリックして関数をデプロイします

Positive
: Amazon Translateは多くの言語ペアに対応しています。`source_language`と`target_language`を変更することで、様々な言語間の翻訳が可能です。

## Lambda関数の作成（音声化処理）
Duration: 0:15:00

### 関数の作成

新しいLambda関数を作成します。

| 項目 | 値 |
|------|-----|
| 関数名 | `handson-text-to-speech` |
| ランタイム | Python 3.12 |
| 実行ロール | `handson-lambda-role`（既存のロールを使用） |
| タイムアウト | 60秒（デフォルトの3秒から変更） |

### タイムアウトの変更

1. **設定** タブをクリック
2. **一般設定** の **編集** をクリック
3. タイムアウトを **1分** に変更
4. **保存** をクリック

### コードの入力

以下のコードを入力します。

```python
import json
import boto3
from datetime import datetime

polly = boto3.client('polly')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """翻訳されたテキストを音声に変換してS3に保存する"""

    translated_text = event['translated_text']
    output_bucket = event['bucket'].replace('input', 'output')
    original_key = event['key']

    # ファイル名を生成
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_key_text = f"translated/{timestamp}_{original_key}"
    output_key_audio = f"audio/{timestamp}_{original_key.replace('.txt', '.mp3')}"

    # 翻訳テキストをS3に保存
    s3.put_object(
        Bucket=output_bucket,
        Key=output_key_text,
        Body=translated_text.encode('utf-8'),
        ContentType='text/plain'
    )

    # Amazon Pollyで音声合成
    response = polly.synthesize_speech(
        Text=translated_text,
        OutputFormat='mp3',
        VoiceId='Joanna',
        Engine='neural'
    )

    # 音声ファイルをS3に保存
    audio_stream = response['AudioStream'].read()
    s3.put_object(
        Bucket=output_bucket,
        Key=output_key_audio,
        Body=audio_stream,
        ContentType='audio/mpeg'
    )

    return {
        'statusCode': 200,
        'output_bucket': output_bucket,
        'translated_text_key': output_key_text,
        'audio_key': output_key_audio,
        'message': '翻訳テキストと音声ファイルの保存が完了しました'
    }
```

3. **Deploy** をクリックして関数をデプロイします

## Lambda関数の作成（Transcribe起動）
Duration: 0:15:00

### 関数の作成

Pollyで生成した音声をTranscribeで文字起こしするためのLambda関数を作成します。

新しいLambda関数を作成します。

| 項目 | 値 |
|------|-----|
| 関数名 | `handson-start-transcribe` |
| ランタイム | Python 3.12 |
| 実行ロール | `handson-lambda-role`（既存のロールを使用） |

### コードの入力

以下のコードを入力します。

```python
import json
import boto3
from datetime import datetime

transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    """Pollyで生成した音声ファイルのTranscribeジョブを開始する"""

    output_bucket = event['output_bucket']
    audio_key = event['audio_key']

    # ジョブ名を生成（一意にするためタイムスタンプを使用）
    job_name = f"handson-transcribe-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    media_uri = f"s3://{output_bucket}/{audio_key}"

    # Amazon Transcribeのジョブを開始
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': media_uri},
        MediaFormat='mp3',
        LanguageCode='en-US',
        OutputBucketName=output_bucket,
        OutputKey=f"transcription/{job_name}.json"
    )

    return {
        'statusCode': 200,
        'output_bucket': output_bucket,
        'audio_key': audio_key,
        'transcription_job_name': job_name,
        'translated_text_key': event.get('translated_text_key', ''),
        'message': 'Transcribeジョブを開始しました'
    }
```

3. **Deploy** をクリックして関数をデプロイします

Positive
: Amazon Transcribeは非同期処理です。ジョブの開始後、完了まで数十秒〜数分かかる場合があります。Step Functions のWaitステートで自動的に待機します。

## Lambda関数の作成（Transcribe結果取得）
Duration: 0:15:00

### 関数の作成

Transcribeジョブの結果を取得するLambda関数を作成します。

新しいLambda関数を作成します。

| 項目 | 値 |
|------|-----|
| 関数名 | `handson-get-transcription` |
| ランタイム | Python 3.12 |
| 実行ロール | `handson-lambda-role`（既存のロールを使用） |

### コードの入力

以下のコードを入力します。

```python
import json
import boto3

transcribe = boto3.client('transcribe')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """Transcribeジョブの結果を確認し、文字起こしテキストを取得する"""

    job_name = event['transcription_job_name']

    # ジョブのステータスを取得
    response = transcribe.get_transcription_job(
        TranscriptionJobName=job_name
    )

    status = response['TranscriptionJob']['TranscriptionJobStatus']

    if status == 'COMPLETED':
        # 結果をS3から取得
        output_bucket = event['output_bucket']
        result_key = f"transcription/{job_name}.json"

        result_obj = s3.get_object(Bucket=output_bucket, Key=result_key)
        result_data = json.loads(result_obj['Body'].read().decode('utf-8'))

        # 文字起こしテキストを抽出
        transcript_text = result_data['results']['transcripts'][0]['transcript']

        # テキストファイルとしてS3に保存
        summary_key = f"transcription/{job_name}_text.txt"
        s3.put_object(
            Bucket=output_bucket,
            Key=summary_key,
            Body=transcript_text.encode('utf-8'),
            ContentType='text/plain'
        )

        return {
            'statusCode': 200,
            'transcription_status': 'COMPLETED',
            'transcript_text': transcript_text,
            'summary_key': summary_key,
            'output_bucket': output_bucket,
            'message': '文字起こしが完了しました'
        }
    elif status == 'FAILED':
        raise Exception(f"Transcribeジョブが失敗しました: {response['TranscriptionJob'].get('FailureReason', '不明')}")
    else:
        # IN_PROGRESS の場合は再試行のためステータスを返す
        return {
            'statusCode': 200,
            'transcription_status': status,
            'transcription_job_name': job_name,
            'output_bucket': event['output_bucket'],
            'audio_key': event.get('audio_key', ''),
            'translated_text_key': event.get('translated_text_key', ''),
            'message': f'ジョブは {status} です。処理中...'
        }
```

3. **Deploy** をクリックして関数をデプロイします

Positive
: `transcription_status` の値によってStep Functionsが処理を分岐します。`COMPLETED` なら完了、それ以外なら待機→再確認のループになります。

## Step Functionsの作成
Duration: 0:20:00

### ステートマシンの作成

1. AWSマネジメントコンソールから **Step Functions** を選択します
2. **ステートマシンの作成** をクリックします
3. **コードでワークフローを作成** を選択します

### ワークフロー定義

以下のASL（Amazon States Language）を入力します。フェーズ1（テキスト→音声）とフェーズ2（音声→テキスト）の両方を含むワークフローです。

```json
{
  "Comment": "テキストファイルの翻訳・音声化・文字起こしワークフロー",
  "StartAt": "ReadText",
  "States": {
    "ReadText": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-northeast-1:{アカウントID}:function:handson-read-text",
      "Next": "TranslateText",
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "HandleError"
        }
      ]
    },
    "TranslateText": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-northeast-1:{アカウントID}:function:handson-translate-text",
      "Next": "TextToSpeech",
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "HandleError"
        }
      ]
    },
    "TextToSpeech": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-northeast-1:{アカウントID}:function:handson-text-to-speech",
      "Next": "StartTranscribe",
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "HandleError"
        }
      ]
    },
    "StartTranscribe": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-northeast-1:{アカウントID}:function:handson-start-transcribe",
      "Next": "WaitForTranscription",
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "HandleError"
        }
      ]
    },
    "WaitForTranscription": {
      "Type": "Wait",
      "Seconds": 30,
      "Next": "GetTranscription"
    },
    "GetTranscription": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:ap-northeast-1:{アカウントID}:function:handson-get-transcription",
      "Next": "CheckTranscriptionStatus",
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "HandleError"
        }
      ]
    },
    "CheckTranscriptionStatus": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.transcription_status",
          "StringEquals": "COMPLETED",
          "Next": "SuccessState"
        }
      ],
      "Default": "WaitForTranscription"
    },
    "SuccessState": {
      "Type": "Succeed"
    },
    "HandleError": {
      "Type": "Fail",
      "Error": "ProcessingError",
      "Cause": "ワークフローの実行中にエラーが発生しました"
    }
  }
}
```

Negative
: `{アカウントID}` は自分のAWSアカウントIDに置き換えてください。

### ステートマシンの設定

| 項目 | 値 |
|------|-----|
| ステートマシン名 | `handson-translate-workflow` |
| 実行ロール | `handson-stepfunctions-role`（既存のロールを使用） |
| ログ記録 | すべてのログ |

4. **ステートマシンの作成** をクリックします

## S3イベント通知の設定
Duration: 0:10:00

### イベント通知の設定

S3にテキストファイルがアップロードされた際に、自動的にStep Functionsを実行するよう設定します。

1. S3コンソールから **入力用バケット** を選択します
2. **プロパティ** タブを選択します
3. **イベント通知** セクションの **イベント通知を作成** をクリックします

Positive
: S3イベント通知からStep Functionsを直接起動するには、Amazon EventBridge経由で設定することもできます。

### EventBridge経由での設定

1. 入力用S3バケットの **プロパティ** タブを開きます
2. **Amazon EventBridge** セクションで **編集** をクリック
3. **通知をEventBridgeに送信** を **オン** にします

次に、EventBridgeでルールを作成します。

1. **Amazon EventBridge** コンソールを開きます
2. **ルール** → **ルールを作成** をクリック

| 項目 | 値 |
|------|-----|
| ルール名 | `handson-s3-to-stepfunctions` |
| イベントバス | default |
| ルールタイプ | イベントパターンを持つルール |

3. イベントパターンを以下のように設定します

```json
{
  "source": ["aws.s3"],
  "detail-type": ["Object Created"],
  "detail": {
    "bucket": {
      "name": ["handson-input-{アカウントID}"]
    },
    "object": {
      "key": [{
        "suffix": ".txt"
      }]
    }
  }
}
```

4. ターゲットに **Step Functions ステートマシン** を選択し、`handson-translate-workflow` を指定します

## 動作確認
Duration: 0:15:00

### テストファイルの確認

テンプレートリポジトリに含まれている `test.txt` を使用します。内容を確認してみましょう。

```console
cat test.txt
```

別のテキストで試したい場合は、以下のように新しいファイルを作成できます。

```console
echo "こんにちは。今日はAWSのサーバレスサービスを使ったハンズオンを行います。楽しんでいきましょう。" > test.txt
```

### S3へのアップロード

AWS CLIを使ってファイルをアップロードします。

```console
aws s3 cp test.txt s3://handson-input-{アカウントID}/test.txt
```

### 結果の確認

1. **Step Functions** コンソールでワークフローの実行を確認します
2. 各ステップが **Succeeded** になっていることを確認します（Transcribeジョブの完了待ちで `WaitForTranscription` → `GetTranscription` のループが発生します）
3. **出力用S3バケット** に以下のファイルが生成されていることを確認します

* `translated/` フォルダ - 翻訳されたテキストファイル
* `audio/` フォルダ - 音声ファイル（.mp3）
* `transcription/` フォルダ - 文字起こし結果（JSONとテキスト）

### 音声ファイルの確認（Polly）

```console
aws s3 ls s3://handson-output-{アカウントID}/audio/
aws s3 cp s3://handson-output-{アカウントID}/audio/{生成されたファイル名}.mp3 ./output.mp3
```

ダウンロードしたMP3ファイルを再生して、英語の音声が出力されることを確認します。

### 文字起こし結果の確認（Transcribe）

```console
aws s3 ls s3://handson-output-{アカウントID}/transcription/
aws s3 cp s3://handson-output-{アカウントID}/transcription/{ジョブ名}_text.txt ./transcription_result.txt
cat transcription_result.txt
```

文字起こしされた英語テキストが表示されます。翻訳されたテキストと比較して、Polly→Transcribeの変換精度を確認してみましょう。

Positive
: 元の日本語テキスト → 英語翻訳テキスト → 英語音声 → 英語文字起こしテキスト の変換結果を比較することで、各サービスの変換精度を体感できます。

Positive
: ワークフローがエラーになった場合は、Step Functionsの実行履歴からエラーの詳細を確認してください。Lambda関数のCloudWatch Logsも参考になります。

## リソースの削除
Duration: 0:10:00

### 作成したリソースの削除

ハンズオンが完了したら、以下のリソースを削除して料金の発生を防ぎましょう。

削除順序は以下の通りです。

1. **EventBridge ルール** `handson-s3-to-stepfunctions` を削除
2. **Step Functions** ステートマシン `handson-translate-workflow` を削除
3. **Lambda関数** 以下の5つの関数を削除
   * `handson-read-text`
   * `handson-translate-text`
   * `handson-text-to-speech`
   * `handson-start-transcribe`
   * `handson-get-transcription`
4. **S3バケット** 以下の2つのバケットを空にしてから削除
   * `handson-input-{アカウントID}`
   * `handson-output-{アカウントID}`
5. **IAMロール** 以下の2つのロールを削除
   * `handson-lambda-role`
   * `handson-stepfunctions-role`
6. **IAMユーザー** `handson-user` を削除（アクセスキーも自動的に削除されます）
7. **GitHub Codespace** 不要であれば Codespace を削除（GitHub の Codespaces 管理画面から）

### S3バケットの空にする方法

```console
aws s3 rm s3://handson-input-{アカウントID} --recursive
aws s3 rm s3://handson-output-{アカウントID} --recursive
aws s3 rb s3://handson-input-{アカウントID}
aws s3 rb s3://handson-output-{アカウントID}
```

Negative
: リソースの削除を忘れると、意図しない料金が発生する可能性があります。必ず全てのリソースを削除してください。

## まとめ
Duration: 0:05:00

### 学んだこと

このハンズオンでは以下のことを学びました。

* **Amazon S3** を使ったファイルの保存とイベント通知
* **AWS Lambda** を使ったサーバレスアプリケーションの構築
* **AWS Step Functions** を使ったワークフローのオーケストレーション（Choiceステートによるループ処理を含む）
* **Amazon Translate** を使ったテキスト翻訳
* **Amazon Polly** を使ったテキスト音声変換（Text-to-Speech）
* **Amazon Transcribe** を使った音声の文字起こし（Speech-to-Text）
* **Amazon EventBridge** を使ったイベント駆動アーキテクチャ

### 発展課題

* 翻訳先の言語を複数言語に対応させてみましょう
* 音声のVoiceIdを変更して異なる声質を試してみましょう（例: `Matthew`, `Amy`, `Takumi`）
* Transcribeの `LanguageCode` を変更して日本語音声の文字起こしを試してみましょう
* 文字起こし結果をさらに別の言語に翻訳してみましょう（多段翻訳パイプライン）
* エラーハンドリングを強化してSNS通知を追加してみましょう
* DynamoDBを追加して翻訳・文字起こし履歴を保存してみましょう

### 参考リンク

<button>
  [AWS Lambda ドキュメント](https://docs.aws.amazon.com/ja_jp/lambda/)
</button>

<button>
  [AWS Step Functions ドキュメント](https://docs.aws.amazon.com/ja_jp/step-functions/)
</button>

<button>
  [Amazon Translate ドキュメント](https://docs.aws.amazon.com/ja_jp/translate/)
</button>

<button>
  [Amazon Polly ドキュメント](https://docs.aws.amazon.com/ja_jp/polly/)
</button>

<button>
  [Amazon Transcribe ドキュメント](https://docs.aws.amazon.com/ja_jp/transcribe/)
</button>
