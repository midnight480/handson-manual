author: Shibao,Tetsuya
summary: AWSを使った簡単なObservability（O11y）と脆弱性管理のハンズオン
id: 14-AWS-handson-4-beginners-saga-o11y
categories: codelab,markdown,aws,o11y,security
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# AWS Hands-on for Beginners: Saga O11y & Security

## はじめに
Duration: 0:05:00

### ハンズオンの目的
このハンズオンでは、「アプリのログを収集し、可視化・通知する」という Observability (O11y / 可観測性) の基本を学びます。
また、意図的に脆弱性を含んだパッケージを導入し、セキュリティツール（Snyk または Aikido）を使って検知・修復する DevSecOps の基本的な流れを体験します。

### アーキテクチャと使用技術
* **インフラ**: AWS EC2 (CloudFormation で構築)
* **アプリケーション**: Python (Flask または Django) / TypeScript 等で作成した簡単な ToDo アプリ (DBは SQLite)
* **開発環境**: **Kiro-IDE Remote** を使用して、ブラウザ上で簡単にコーディング・操作を行います。
* **O11yツール**: Amazon CloudWatch, Mackerel (または Datadog / Sentry)
* **セキュリティツール**: Snyk または Aikido

---

## 開発環境 (Kiro-IDE Remote) の準備
Duration: 0:10:00

本ハンズオンでは、AWS 上に簡単に Web 開発環境を構築できる **Kiro-IDE Remote** を使用します。これにより、ローカル PC に環境を構築することなくハンズオンを進めることができます。

### Kiro-IDE の起動
以下のリンク先に用意されている「Deploy」ボタンから、ワンクリックでデプロイが可能です。

[Kiro IDE Remote のマニュアルページ](https://aws-samples.github.io/sample-one-click-generative-ai-solutions/solutions/kiro-ide/)

1. サインイン済みの AWS アカウントがある状態で、マニュアルページ内の **[Deploy]** ボタンをクリックします。
2. AWS CloudFormation の「スタックのクイック作成」画面が開きます。
3. デプロイに必要な以下のパラメータを確認・入力します：
   - **UserEmail**: 構築完了メールや通知を受け取るご自身のメールアドレスを入力します。
   - **Language**: OS の言語設定です。`JP`（日本語）を選択しておくことを推奨します。
   - **EnableAdministratorAccess**: 本ハンズオンでは CloudFormation などの AWS リソースを作成・操作するため、`true` に設定してください。
4. 画面最下部の「AWS CloudFormation が IAM リソースを作成する場合があることを承認します。」にチェックを入れます。
5. **[スタックの作成]** をクリックし、作成プロセスが完了（ステータスが `CREATE_COMPLETE` になる）するまで約5〜10分程度待ちます。
   * ※デプロイが開始されると、入力したメールアドレス宛に通知のサブスクリプション確認メールが届きます。「Confirm subscription」をクリックして承認を行ってください。
6. デプロイが完了すると、「[One Click Gen AI Solutions] Kiro IDE - Deployment completed」というメールが届きます。本文（または CloudFormation の「出力(Outputs)」タブ）から以下の情報を確認します：
   - `KiroIDEURL`: アクセス用URL
   - `Username`: ログインユーザー名
   - `Password`: 初期パスワード
7. 指定された URL にアクセスし、ユーザー名とパスワードでログインしてください。
8. ログイン後、ブラウザ上で VS Code ライクなエディタとターミナルが使用できることを確認してください。以降の作業はこのエディタ内のターミナルで行います。
   * ※デスクトップ上の Kiro アイコンは最初無効化されています。右クリックで起動を許可（Allow Launching）してから実行してください。

---

## インフラとアプリのデプロイ
Duration: 0:15:00

### CloudFormationテンプレートの作成と実行
ToDoアプリを動かすためのEC2インスタンスを、CloudFormationを利用して構築します。

1. Kiro-IDE のエディタを開き、新規ファイル `todo-app-template.yaml` を作成します。
2. 以下の内容をコピーして、作成したファイルに貼り付けて保存します。
   （※このテンプレートは EC2 の構築、Python・Flask のセットアップ、および脆弱性のあるパッケージの導入を自動で行います）

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'ToDo App EC2 Instance for Observability Hands-on'
Resources:
  InstanceRole:
    Type: 'AWS::IAM::Role'
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
            Action: 'sts:AssumeRole'
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'
        - 'arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy'

  InstanceProfile:
    Type: 'AWS::IAM::InstanceProfile'
    Properties:
      Roles:
        - !Ref InstanceRole

  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: 'Allow HTTP traffic for ToDo App'
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 8080
          ToPort: 8080
          CidrIp: 0.0.0.0/0

  ToDoAppInstance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: t3.micro
      ImageId: 'resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'
      IamInstanceProfile: !Ref InstanceProfile
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          dnf update -y
          dnf install -y python3-pip
          mkdir -p /opt/todo-app /var/log/todo-app
          cd /opt/todo-app
          # 意図的に古い脆弱性のあるパッケージを導入（ハンズオン用）
          pip3 install Flask==2.0.1 Jinja2==3.0.1 Werkzeug==2.0.1
          cat << 'EOF' > app.py
          import logging
          from flask import Flask, request, jsonify
          app = Flask(__name__)
          logging.basicConfig(filename='/var/log/todo-app/app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
          todos = []
          @app.route('/', methods=['GET'])
          def get_todos():
              app.logger.info("Fetched ToDos")
              return jsonify(todos)
          @app.route('/', methods=['POST'])
          def add_todo():
              data = request.json
              if not data or 'task' not in data:
                  app.logger.error("Invalid request to add ToDo")
                  return "Invalid data", 400
              todos.append(data['task'])
              app.logger.info(f"Added ToDo: {data['task']}")
              return jsonify({'status': 'added'}), 201
          @app.route('/error', methods=['GET'])
          def trigger_error():
              app.logger.error("Intentionally triggered error log for testing!")
              return "Error logged", 500
          if __name__ == '__main__':
              app.run(host='0.0.0.0', port=8080)
          EOF
          nohup python3 app.py > /dev/null 2>&1 &

Outputs:
  AppURL:
    Value: !Sub 'http://${ToDoAppInstance.PublicDnsName}:8080'
    Description: ToDo App Access URL
  InstanceId:
    Value: !Ref ToDoAppInstance
    Description: EC2 Instance ID
```

3. Kiro-IDE のターミナルで以下のコマンドを実行し、ファイルからCloudFormationスタックを作成します。

```console
aws cloudformation create-stack \
  --stack-name saga-o11y-handson \
  --template-body file://todo-app-template.yaml \
  --capabilities CAPABILITY_IAM
```

3. スマホやブラウザから構築された ToDo アプリ（例: EC2のパブリックIP:8080）にアクセスし、タスクの追加・完了ができることを確認します。
4. このToDoアプリは背景でログファイル（例: `/var/log/todo-app/app.log`）にアクセスログやエラーを出力していることを確認しておきましょう。

---

## CloudWatchによるログ取集と通知
Duration: 0:15:00

まずはAWSのネイティブサービスである CloudWatch を利用してアプリのログを収集・可視化します。

### CloudWatch Agent のインストールと設定
EC2 インスタンスにログイン（またはSSMセッションマネージャー経由で接続）し、CloudWatch Agentをインストールします。

```console
sudo yum install amazon-cloudwatch-agent -y
```

ログを転送するための設定ファイル（`config.json`）を作成し、起動します。

```json
{
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/todo-app/app.log",
            "log_group_name": "todo-app-logs",
            "log_stream_name": "{instance_id}"
          }
        ]
      }
    }
  }
}
```

```console
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:config.json
```

### 通知用 SNS トピックの作成とメール購読 (CLI)
まずは、アラーム発生時にメールを通知するための SNS トピックを作成します。Kiro-IDE のターミナルから以下のコマンドを入力します。
（最後に設定する自分のメールアドレス `your_email@example.com` は、受信可能なものに変更して実行してください）

```console
# SNS トピックの作成
TOPIC_ARN=$(aws sns create-topic --name todo-app-alerts --query 'TopicArn' --output text)

# メールアドレスの登録（★各自のメールアドレスに変更）
aws sns subscribe \
  --topic-arn $TOPIC_ARN \
  --protocol email \
  --notification-endpoint "your_email@example.com"
```

※ コマンド実行後、入力したメールアドレス宛に「**AWS Notification - Subscription Confirmation**」というメールが届きます。本文中の `Confirm subscription` を必ずクリックして承認してください。

### メトリクスフィルターとアラームの作成 (CLI)
アプリのログログループ（`todo-app-logs`）の中から、`ERROR` という文字列を含んだ行をカウントし、1分間に1回でも発生したら先ほどの SNS（メール）経由で通知する設定を行います。

```console
# ロググループが存在することを保証するために作成（既に存在する場合は作成済みのエラーが出ますが無視して構いません）
aws logs create-log-group --log-group-name todo-app-logs || true

# メトリクスフィルター（ERROR の検知）を作成
aws logs put-metric-filter \
  --log-group-name "todo-app-logs" \
  --filter-name "ErrorFilter" \
  --filter-pattern "ERROR" \
  --metric-transformations \
      metricName=ErrorCount,metricNamespace=ToDoAppMetrics,metricValue=1,defaultValue=0

# アラーム（1分間に1回以上 ERROR が出たら通知）の作成
aws cloudwatch put-metric-alarm \
  --alarm-name "ToDoAppErrorAlarm" \
  --metric-name "ErrorCount" \
  --namespace "ToDoAppMetrics" \
  --statistic Sum \
  --period 60 \
  --evaluation-periods 1 \
  --threshold 1 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --alarm-actions $TOPIC_ARN \
  --treat-missing-data notBreaching
```

### マネジメントコンソールでの確認とエラー発生テスト
CLI で一気に立ち上げた設定を、実際に画面から確認＆テストしてみましょう。

1. **AWSマネジメントコンソール** にログインし、**CloudWatch** の画面を開きます。
2. 左メニューの **ログ > ロググループ** から `todo-app-logs` を開くと、EC2 が送信したアプリのログ（ログストリーム）を見ることができます。
3. 左メニューの **アラーム > すべてのアラーム** を開くと、「`ToDoAppErrorAlarm`」が作成されていることを確認できます（最初は「データ不足」や「OK」になっています）。
4. Kiro-IDEまたは別ブラウザのタブから、ToDo アプリの **エラー発生用 URL** にアクセスし、意図的にエラーログを書き込みます。
   * アクセス先例: `http://<EC2のIPまたはパブリックDNS>:8080/error`
5. 1〜2分後、CloudWatchアラームの画面をリロードし、状態が「**アラーム (In alarm)**」という赤い状態に変わったことを確認してください。
6. 同時に、ご自身のメールアドレス宛に CloudWatch からの警告通知メールが届いていれば、一連のログの検知＆通知フローは成功です！

---

## 外部ツールによる監視 (Mackerel / Sentry)
Duration: 0:20:00

さらに、外部の SaaS 型監視・エラー管理ツール（Mackerel や Sentry など）を利用してみましょう。
※本シナリオでは Mackerel の例を記載します。

### Mackerel エージェントの導入
1. [Mackerel](https://mackerel.io/) にサインアップし、オーガニゼーションを作成します。
2. 「新規ホストの登録」画面から、インストールコマンド（APIキーが含まれています）をコピーします。
3. Kiro-IDE などのターミナルから、EC2 にログインしコマンドを実行します。

```console
# Mackerelのインストールと起動（ダミー例。実際のコマンドを使用）
curl -fsSL https://mackerel.io/file/script/setup-all-yum-v2.sh | MACKEREL_APIKEY='YOUR_API_KEY' sh
```

### アプリケーション監視の設定
* Mackerel のダッシュボードに EC2 の CPU やメモリのリソースが表示されることを確認します。
* `mackerel-agent.conf` を編集し、先ほどのアプリのログ (`/var/log/todo-app/app.log`) を監視し、特定のエラー文字列でアラートを発火させる設定（チェック監視）を追加します。

> [!TIP]
> アプリによっては、コード内に Sentry SDK を組み込むことで、より詳細なスタックトレース付きのエラー収集を体験するのもおすすめです。導入後はわざとアプリで例外(Exception)を発生させて、Sentryのダッシュボードで確認してみましょう。

---

## 脆弱性の検知と修復 (Snyk / Aikido)
Duration: 0:20:00

開発と運用（DevSecOps）において、使用しているライブラリ（パッケージ）に脆弱性がないかチェックすることは重要です。
ここでは意図的に古い脆弱なパッケージを入れ、ツールで検知し、安全なバージョンに修復します。

### 脆弱なパッケージの導入
Kiro-IDE 上で、ToDo アプリのソースコードディレクトリに移動し、わざと古いパッケージを指定してインストールします。（例：Python の requests や Jinja2 の古いバージョン）

```console
# Pythonの例
pip install requests==2.19.1
pip freeze > requirements.txt
```

### セキュリティスキャンの実行（例: Snyk）
1. [Snyk](https://snyk.io/) のアカウントを作成し、CLI メニューの手順に従って Kiro-IDE 環境に Snyk CLI をインストールします。
2. 認証を行います。

```console
npm install -g snyk
snyk auth
```

3. プロジェクトディレクトリでスキャンを実行します。

```console
snyk test
```

4. 古い `requests` パッケージに「High」や「Critical」な脆弱性が複数見つかることを確認してください。

### 修復 (Remediation) 作業
出力されたアドバイスに従い、安全なバージョンにアップデートします。

```console
# 提案された安全なバージョンや最新バージョンへアップデート
pip install requests --upgrade
pip freeze > requirements.txt
```

再度 `snyk test` を実行し、脆弱性が「0」になったことを確認します。

Positive
: このように、定期的にチェックすることで、本番環境に脆弱性が混入するのを未然に防ぐことができます。

---

## お片付け (Clean up)
Duration: 0:05:00

ハンズオンで使用した AWS リソースや、外部サービスのデータは、課金や不要なアラートの原因になるため忘れずに削除しましょう。

### CloudFormationスタックの削除
Kiro-IDE または AWS マネジメントコンソールから、最初に作成した CloudFormation スタックを削除します。

```console
aws cloudformation delete-stack --stack-name saga-o11y-handson
```

### Kiro-IDE 環境の削除
用済みになった場合は、手順に従って Kiro-IDE 自体の CloudFormation スタックも削除してください。

### 外部サービスの後処理
* **Mackerel / Datadog / Sentry**: 作成したオーガニゼーション、プロジェクト、ホスト設定などを必要に応じて退会・削除してください。
* **Snyk / Aikido**: 連携したプロジェクト情報などを削除してください。

以上で本ハンズオンは終了です。お疲れ様でした！

