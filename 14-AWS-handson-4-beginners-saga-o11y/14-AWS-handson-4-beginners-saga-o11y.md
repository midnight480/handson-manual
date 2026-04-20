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
また、意図的に脆弱性を含んだパッケージを導入し、セキュリティツール（Snyk）を使って検知・修復する DevSecOps の基本的な流れを体験します。

Positive
: **用語解説: O11y (Observability / 可観測性) とは？**
: 「Observability」は「O」と「y」の間に11文字あるため「O11y」と略されます。システムの内部状態を「ログ」「メトリクス（数値データ）」「トレース（処理の流れ）」の3つの柱で外部から把握できるようにする考え方です。「サーバーが今どんな状態か」「エラーが起きていないか」を素早く知るための仕組みづくりと考えてください。

Positive
: **用語解説: DevSecOps とは？**
: 「Development（開発）」「Security（セキュリティ）」「Operations（運用）」を組み合わせた言葉です。従来はアプリを作った後にセキュリティチェックを行っていましたが、DevSecOps では開発の早い段階からセキュリティを組み込むことで、脆弱性（セキュリティ上の弱点）を早期に発見・修正します。

Positive
: **用語解説: 脆弱性（ぜいじゃくせい）とは？**
: ソフトウェアに存在するセキュリティ上の欠陥や弱点のことです。悪意のある攻撃者に悪用されると、データの漏洩やシステムの乗っ取りなどの被害につながる可能性があります。ライブラリ（他の人が作った便利なプログラム部品）の古いバージョンには、既知の脆弱性が含まれていることがあります。

### アーキテクチャと使用技術
* **インフラ**: AWS EC2 (CloudFormation で構築)
* **アプリケーション**: Python (Flask または Django) / TypeScript 等で作成した簡単な ToDo アプリ (DBは SQLite)
* **開発環境**: **Kiro-IDE Remote** を使用して、ブラウザ上で簡単にコーディング・操作を行います。
* **O11yツール**: Amazon CloudWatch, Mackerel
* **セキュリティツール**: Snyk

Positive
: **用語解説: 上記の技術用語について**
: * **EC2 (Elastic Compute Cloud)**: AWS が提供する仮想サーバーです。自分の PC の代わりにクラウド上にサーバーを借りるイメージです。
: * **CloudFormation**: AWS のリソースをコード（設計図）で自動作成するサービスです。詳しくは後のセクションで説明します。
: * **Flask**: Python で Web アプリケーションを簡単に作るためのフレームワーク（ひな形）です。
: * **SQLite**: ファイル1つで動く軽量なデータベースです。サーバーの設定が不要なため、学習用途に最適です。
: * **CloudWatch**: AWS が提供するログ収集・監視・アラーム通知のサービスです。
: * **Mackerel**: AWS 以外の会社が提供する監視・エラー管理の SaaS ツールです。

Positive
: **SaaS とは？**
: 「Software as a Service」の略で、自分でサーバーを用意してインストールすることなく、ブラウザ経由で利用できるサービスのことです。Mackerel や Snyk などは、クラウド上で提供されているサービスをそのまま利用します。

### 2つの環境の使い分けに注意！
本ハンズオンでは、2つの異なる Linux 環境を使い分けます。
1. **Kiro-IDE Remote**: あなたの「作業用 PC」のような環境です。ここで設計図（CloudFormation）を書いたり、セキュリティスキャンを実行したりします。
2. **ToDo アプリの EC2**: CloudFormation で作成される「サーバー」環境です。アプリが実際に動き、ログが保存される場所です。

Positive
: ターミナルで操作しているのが「どちらの環境か」を常に意識するのが上達の近道です。

---

## 事前準備: AWS Builder ID の作成
Duration: 0:05:00

Kiro-IDE Remoteなどのツールを利用・連携するために、「**AWS Builder ID**」が必要となります。
AWS Builder ID は AWS や Amazon.co.jp アカウントとは異なる、個人のための無料アカウントです（クレジットカードの登録なども不要です）。

1. [AWS Builder ID の作成画面](https://builder.aws.com/start) にアクセスします。
2. 個人のメールアドレスを入力し [次へ] をクリックします。
3. 表示される「名前」を入力して [次へ] をクリックします。
4. 入力したメールアドレス宛に届いた認証コードを入力して [認証] します。
5. パスワードの条件（8〜64文字・大文字と小文字・数値・英数字以外の文字）を満たすパスワードを設定し、[AWS Builder IDを作成] をクリックします。

Positive
: 詳しい画面遷移や Community.aws でのプロファイル作成方法については、[こちらの記事 (AWS Builder ID の利用とその作成方法)](https://note.com/s_numaguchi/n/nd5126833389b) もあわせてご参照ください。

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
   - **EnableAdministratorAccess**: **重要**。本ハンズオンでは CloudFormation などの AWS リソースを作成・操作するため、必ず `true` に設定してください。これにより、Kiro-IDE のターミナルから AWS コマンドを実行するための権限（IAM ロール）が自動的に付与されます。
4. 画面最下部の「AWS CloudFormation が IAM リソースを作成する場合があることを承認します。」にチェックを入れます。
5. **[スタックの作成]** をクリックし、作成プロセスが完了（ステータスが `CREATE_COMPLETE` になる）するまで約5〜10分程度待ちます。
   * ※デプロイが開始されると、入力したメールアドレス宛に通知のサブスクリプション確認メールが届きます。「Confirm subscription」をクリックして承認を行ってください。
6. デプロイが完了すると、「[One Click Gen AI Solutions] Kiro IDE - Deployment completed」というメールが届きます。本文（または CloudFormation の「出力(Outputs)」タブ）から以下の情報を確認します：
   - `KiroIDEURL`: アクセス用URL
   - `Username`: ログインユーザー名
   - `Password`: 初期パスワード
7. 指定された URL にアクセスし、ユーザー名とパスワードでログインしてください。
8. ログイン後、ブラウザ上で VS Code ライクなエディタとターミナルが使用できることを確認してください。
   * **エディタ**: 左側のファイルツリーからファイルを管理し、右側の画面で編集します。
   * **ターミナル**: 画面下部（またはメニューの Terminal > New Terminal）に表示される Linux シェルです。以降のコマンド操作はここで行います。
   * ※デスクトップ上の Kiro アイコンは最初無効化されています。右クリックで起動を許可（Allow Launching）してから実行してください。

---

## インフラとアプリのデプロイ
Duration: 0:15:00

### CloudFormationテンプレートの作成と実行
ToDoアプリを動かすためのEC2インスタンスを、CloudFormationを利用して構築します。

Positive
: **CloudFormationとは？**
: AWS上のインフラ環境（サーバーやネットワークなど）を、設計図（テンプレート）としてコード化して自動構築するサービスです。「スタック」とは、その設計図をもとに作られたAWSリソースのグループのことです。手動で一つずつ設定するよりも、早く・正確にインフラを用意できます。

1. Kiro-IDE のエディタを開き、新規ファイル `todo-app-template.yaml` を作成します。
   * **作成方法**: 左側のファイルエクスプローラーで右クリックし「New File」を選択するか、上部メニューの File > New Text File から作成し、名前を付けて保存します。

Positive
: **■日本語入力**
: もしかしたら、デフォルトで英語になっているかもしれません。
: `Ctrl + Space` で直接／日本語を切り替えられますが、半角・全角キーでの切り替えを行いたい場合一度設定を再起動してください。

Positive
: **■その他**
: * Kiro CLI で認証がなかなか進まない場合、`kiro-cli login --use-device-flow` を試してみてください。
: * ターミナルへの Copy & Paste は `Ctrl + Shift + V` になります。これは Linux の仕様です。

2. 以下の内容をコピーして、作成したファイルに貼り付けて保存します。
   （※このテンプレートは EC2 の構築、Python・Flask のセットアップ、および脆弱性のあるパッケージの導入を自動で行います）

Negative
: **YAML (ヤムル) ファイルの注意点**
: YAML はインデント（行頭の空白の数）で設定の階層構造を表現します。コピー＆ペーストする際に空白がズレてしまうとエラーになるため、そのままの形で貼り付いているか必ず確認してください。

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'ToDo App EC2 Instance for Observability Hands-on'
Resources:
  # --- ① IAMロール: EC2がAWSサービス(SSM, CloudWatch)と連携するための「許可証」---
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

  # --- ② インスタンスプロファイル: IAMロールをEC2に紐づけるための「入れ物」---
  InstanceProfile:
    Type: 'AWS::IAM::InstanceProfile'
    Properties:
      Roles:
        - !Ref InstanceRole

  # --- ③ セキュリティグループ: EC2への通信を制御する「ファイアウォール」---
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: 'Allow HTTP traffic for ToDo App'
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 8080
          ToPort: 8080
          CidrIp: 0.0.0.0/0

  # --- ④ EC2インスタンス本体: アプリが動くサーバー ---
  ToDoAppInstance:
    Type: 'AWS::EC2::Instance'
    Properties:
      InstanceType: t3.micro
      ImageId: 'resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'
      IamInstanceProfile: !Ref InstanceProfile
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      # --- ⑤ UserData: EC2起動時に自動実行されるセットアップスクリプト ---
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

# --- ⑥ Outputs: スタック作成後に表示される情報 ---
Outputs:
  AppURL:
    Value: !Sub 'http://${ToDoAppInstance.PublicDnsName}:8080'
    Description: ToDo App Access URL
  InstanceId:
    Value: !Ref ToDoAppInstance
    Description: EC2 Instance ID
```

Positive
: **テンプレートの各パーツ解説**
: 上記のテンプレートは、以下の6つのパーツで構成されています。
: 1. **InstanceRole (IAMロール)**: EC2 が SSM（リモート接続）や CloudWatch（ログ送信）を使うための「許可証」です。人間でいう「社員証」のようなもので、これがないと EC2 は他の AWS サービスと連携できません。
: 2. **InstanceProfile**: IAM ロールを EC2 に渡すための「入れ物」です。EC2 にロールを直接付けることはできないため、この仲介役が必要です。
: 3. **InstanceSecurityGroup**: EC2 への通信を制御する「ファイアウォール（防火壁）」です。ここでは TCP ポート 8080 番への通信を全 IP アドレス（`0.0.0.0/0`）から許可しています。
: 4. **ToDoAppInstance**: 実際の EC2 サーバー本体です。`t3.micro` は無料利用枠対象の小さなサーバーサイズです。`ImageId` は OS のテンプレート（Amazon Linux 2023）を指定しています。
: 5. **UserData**: EC2 が初めて起動した時に自動実行されるスクリプトです。Python や Flask のインストール、アプリのコード配置、アプリの起動までを自動で行います。
: 6. **Outputs**: スタック作成完了後に表示される情報です。アプリの URL やインスタンス ID を確認できます。

Positive
: **YAML の特殊な記法について**
: * `!Ref InstanceRole`: 同じテンプレート内の別リソースを「参照」する関数です。「上で定義した InstanceRole を使う」という意味です。
: * `!Sub`: 文字列の中に変数を埋め込む関数です。`${ToDoAppInstance.PublicDnsName}` の部分が、実際の EC2 の DNS 名に置き換わります。
: * `Fn::Base64`: テキストを Base64 形式にエンコード（変換）します。UserData に渡すスクリプトは Base64 形式である必要があるため使用しています。

3. Kiro-IDE のターミナルで以下のコマンドを実行し、ファイルからCloudFormationスタックを作成します。

```console
aws cloudformation create-stack \
  --stack-name saga-o11y-handson \
  --template-body file://todo-app-template.yaml \
  --capabilities CAPABILITY_IAM
```

Positive
: **コマンドの解説**
: * `--stack-name`: この構築セットに付ける名前です。
: * `--template-body`: 先ほど作成したファイルのパスを指定します。
: * `--capabilities CAPABILITY_IAM`: このテンプレートが、AWS内での権限設定（IAMロールなど）を作成することを許可するためのフラグです。

4. 構築完了を確認します。
   * AWS マネジメントコンソールの **CloudFormation** 画面を開き、`saga-o11y-handson` のステータスが `CREATE_COMPLETE` になるのを待ちます。
   * 完了したら、スタックの詳細画面にある「**出力 (Outputs)**」タブを開きます。
   * そこに表示されている `AppURL` をクリック（またはコピーしてブラウザで開く）して、ToDo アプリが表示されるか確認してください。

5. このToDoアプリは背景でログファイル（例: `/var/log/todo-app/app.log`）にアクセスログやエラーを出力していることを確認しておきましょう。

---

## CloudWatchによるログ取集と通知
Duration: 0:15:00

まずはAWSのネイティブサービスである CloudWatch を利用してアプリのログを収集・可視化します。

### CloudWatch Agent のインストールと設定
EC2 インスタンスにログイン（※マネジメントコンソールから「SSMセッションマネージャー」を使用すると、ブラウザだけで安全・簡単にLinuxサーバへ接続できます）し、CloudWatch Agentをインストールします。

Positive
: **SSM セッションマネージャーでの EC2 接続手順**
: SSH キーの設定なしに、ブラウザだけで EC2 に接続できる便利な方法です。
: 1. AWS マネジメントコンソールにログインし、上部の検索バーで「**EC2**」と入力して EC2 ダッシュボードを開きます。
: 2. 左メニューの「**インスタンス**」をクリックし、`saga-o11y-handson` で作成されたインスタンスを見つけます。
: 3. インスタンスのチェックボックスを選択し、画面上部の「**接続**」ボタンをクリックします。
: 4. 「セッションマネージャー」タブを選択し、「**接続**」をクリックします。
: 5. ブラウザ上に黒い画面（ターミナル）が開けば接続成功です。
:
: ※ 接続できない場合は、EC2 インスタンスのステータスが「実行中 (running)」であること、および CloudFormation テンプレートで IAM ロール（`AmazonSSMManagedInstanceCore` ポリシー）が正しく設定されていることを確認してください。

Positive
: **セッションマネージャーで接続した直後の注意点**
: 接続直後は `sh-5.2$` のようなプロンプト（入力待ち表示）になっています。`bash` と入力して Enter を押すと、より使いやすいシェルに切り替わります。また、`sudo su -` と入力すると管理者（root）ユーザーに切り替わり、`sudo` を毎回付ける必要がなくなります。

Positive
: **Linux コマンドの補足: `sudo` とパッケージ管理**
: 以下のコマンドの先頭にある `sudo` は、「管理者（スーパーユーザー）権限で実行する」という意味です。ソフトウェアのインストールなどシステム全体に関わる操作を行う際に必要になります。また、`yum` や `dnf` は、ソフトウェアをダウンロード・インストールするためのパッケージ管理ツールです。

```console
sudo yum install amazon-cloudwatch-agent -y
```

ログを転送するための設定ファイル（`config.json`）を作成し、起動します。

Positive
: **GUI エディタを使って編集したい場合**
: 1. まず、**Kiro-IDE のエディタ**で `config.json` という名前の新規ファイルを作成し、以下の JSON 内容を貼り付けて保存します。
: 2. 保存した内容をコピーします。
: 3. EC2 インスタンスのターミナル（セッションマネージャー）で `sudo nano config.json` を実行します。
: 4. コピーした内容をターミナルに貼り付け（Ctrl + Shift + V）て保存します。
: これが、GUI を活用しつつサーバー上のファイルを書き換える最も確実な方法です！

EC2 のターミナルで以下の設定を作成します。

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

Positive
: **用語解説**
: * **ロググループ**: ログをまとめる器の名前です（例: アプリ名など）。
: * **ログストリーム**: その器の中の、個別のログファイルの流れです。ここではインスタンスIDを名前にしています。

```console
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:config.json
```

Positive
: **コマンドの解説**
: このコマンドは CloudWatch Agent を設定ファイルを読み込んで起動するものです。
: * `-a fetch-config`: 「設定を取得して適用する」というアクション指定です。
: * `-m ec2`: 実行環境が EC2 であることを指定しています。
: * `-s`: エージェントを起動（start）します。
: * `-c file:config.json`: 先ほど作成した設定ファイルを指定しています。

### 通知用 SNS トピックの作成とメール購読 (CLI)
まずは、アラーム発生時にメールを通知するための SNS トピックを作成します。Kiro-IDE のターミナルから以下のコマンドを入力します。
（最後に設定する自分のメールアドレス `your_email@example.com` は、受信可能なものに変更して実行してください）

Positive
: **用語解説: SNS (Simple Notification Service) とは？**
: AWS が提供する通知サービスです。「トピック」という通知チャンネルを作り、そこにメールアドレスなどの「購読者（サブスクライバー）」を登録しておくと、トピックにメッセージが送られた時に自動で通知が届きます。LINEグループのようなイメージです。

```console
# SNS トピックの作成
TOPIC_ARN=$(aws sns create-topic --name todo-app-alerts --query 'TopicArn' --output text)

# メールアドレスの登録（★各自のメールアドレスに変更）
aws sns subscribe \
  --topic-arn $TOPIC_ARN \
  --protocol email \
  --notification-endpoint "your_email@example.com"
```

Positive
: **コマンドの解説**
: * `aws sns create-topic --name todo-app-alerts`: 「todo-app-alerts」という名前の通知チャンネル（トピック）を作成します。
: * `--query 'TopicArn' --output text`: コマンドの出力結果から ARN（識別子）だけをテキスト形式で取り出します。
: * `TOPIC_ARN=$(...)`: `$(...)` の中のコマンドを実行し、その結果を `TOPIC_ARN` という変数に保存します。
: * `aws sns subscribe`: トピックにメールアドレスを購読者として登録します。
: * `--protocol email`: 通知方法として「メール」を指定しています（他に SMS や HTTPS なども選べます）。
: * `--notification-endpoint`: 通知先のメールアドレスを指定します。

Positive
: **用語解説: ARN とは？**
: 「Amazon Resource Name」の略で、AWS 上のあらゆるリソースを一意に識別するための住所のようなものです。`arn:aws:sns:ap-northeast-1:123456789012:todo-app-alerts` のような形式をしています。

Positive
: **Linux コマンドの補足: 変数の利用と `\` による改行**
: 上記のコマンドでは、SNS トピック作成時に出力される識別子 (ARN) を `TOPIC_ARN` という「変数」に一時保存し、直後のメール登録コマンドで `$TOPIC_ARN` として再利用しています。また、行末の `\` (バックスラッシュまたは円記号) は、「次の行も同じコマンドとして続く」ことを意味しています。長いコマンドを見やすく改行するための工夫です。

※ コマンド実行後、入力したメールアドレス宛に「**AWS Notification - Subscription Confirmation**」というメールが届きます。本文中の `Confirm subscription` を必ずクリックして承認してください。

### メトリクスフィルターとアラームの作成 (CLI)
アプリのログログループ（`todo-app-logs`）の中から、`ERROR` という文字列を含んだ行をカウントし、1分間に1回でも発生したら先ほどの SNS（メール）経由で通知する設定を行います。

Positive
: **用語解説: メトリクスフィルターとアラームとは？**
: * **メトリクスフィルター**: ログの中から特定の文字列（パターン）を検索し、見つかった回数を「メトリクス（数値データ）」として記録する仕組みです。
: * **アラーム**: メトリクスの値が設定した条件（しきい値）を超えた時に、通知などのアクションを実行する仕組みです。
: この2つを組み合わせることで、「ログに ERROR が出たらメールで知らせる」という自動通知が実現できます。

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

Positive
: **メトリクスフィルターのコマンド解説**
: * `--log-group-name "todo-app-logs"`: 監視対象のロググループ名です。
: * `--filter-name "ErrorFilter"`: このフィルターに付ける名前です。
: * `--filter-pattern "ERROR"`: ログの中から検索する文字列です。「ERROR」を含む行が見つかるたびにカウントされます。
: * `--metric-transformations`: フィルターが一致した時にどんな数値データを記録するかの設定です。
:   * `metricName=ErrorCount`: 記録するメトリクスの名前（エラー回数）。
:   * `metricNamespace=ToDoAppMetrics`: メトリクスを分類するグループ名。
:   * `metricValue=1`: パターンが一致するたびに「1」を記録します。
:   * `defaultValue=0`: パターンが一致しない場合は「0」を記録します。

Positive
: **アラームのコマンド解説**
: * `--alarm-name`: アラームの名前です。
: * `--metric-name` / `--namespace`: 上で作成したメトリクスフィルターの名前とグループを指定します。
: * `--statistic Sum`: 集計方法として「合計」を使います（期間内のエラー回数の合計）。
: * `--period 60`: 60秒（1分間）ごとに集計します。
: * `--evaluation-periods 1`: 1回の集計期間で判定します（つまり直近1分間）。
: * `--threshold 1`: しきい値（基準値）を「1」に設定。エラーが1回以上でアラーム発動です。
: * `--comparison-operator GreaterThanOrEqualToThreshold`: 「しきい値以上」で発動する条件です。
: * `--alarm-actions $TOPIC_ARN`: アラーム発動時に通知を送る SNS トピックを指定します。
: * `--treat-missing-data notBreaching`: データがない期間は「問題なし」として扱います。

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

## 外部ツールによる監視 (Mackerel)
Duration: 0:20:00

さらに、外部の SaaS 型監視ツール（Mackerel など）を利用してみましょう。
※本シナリオでは Mackerel の例を記載します。

### Mackerel エージェントの導入
1. [Mackerel](https://mackerel.io/) にサインアップし、オーガニゼーションを作成します。
2. 「新規ホストの登録」画面から、インストールコマンド（APIキーが含まれています）をコピーします。
3. **EC2 インスタンスのターミナル（セッションマネージャー）** にて、コピーしたコマンドを実行します。

```console
# Mackerelのインストールと起動（ダミー例。実際のコマンドを使用）
curl -fsSL https://mackerel.io/file/script/setup-all-yum-v2.sh | MACKEREL_APIKEY='YOUR_API_KEY' sh
```

Positive
: **コマンドの解説**
: * `curl -fsSL <URL>`: 指定した URL からスクリプト（プログラム）をダウンロードするコマンドです。`-fsSL` はエラー時に静かに失敗し、リダイレクトに追従するオプションです。
: * `| sh`: ダウンロードしたスクリプトをそのまま実行します。`|`（パイプ）は前のコマンドの出力を次のコマンドに渡す Linux の機能です。
: * `MACKEREL_APIKEY='YOUR_API_KEY'`: Mackerel のアカウントに紐づく API キー（認証用の文字列）を環境変数として渡しています。Mackerel の画面からコピーした実際のキーに置き換えてください。

### アプリケーション監視の設定（ログ監視）
ダッシュボードへのリソース表示とあわせて、アプリケションログの監視（チェック監視）を追加してみましょう。

1. Mackerel のダッシュボードに EC2 の CPU やメモリのリソースが表示されていることを確認します。
2. ログ監視を行うために、Mackerel公式のチェックプラグイン集をインストールします。**EC2 のターミナル**で以下のコマンドを実行します。

```console
sudo dnf install -y mackerel-check-plugins
```

3. Mackerel エージェントの設定ファイルを開きます。

```console
sudo nano /etc/mackerel-agent/mackerel-agent.conf
```

Positive
: **nano エディタの基本操作**
: `nano` は Linux で使えるシンプルなテキストエディタです。画面下部にショートカットキーの一覧が表示されます（`^` は Ctrl キーを意味します）。
: * **カーソル移動**: 矢印キーで移動します。
: * **文字の入力**: そのままキーボードで入力できます。
: * **保存**: `Ctrl + O` を押し、ファイル名を確認して `Enter` を押します。
: * **終了**: `Ctrl + X` で nano を閉じます。
: * **貼り付け**: ブラウザからコピーした内容は `Ctrl + Shift + V` で貼り付けます。
: * **行末へ移動**: `Ctrl + E`、**行頭へ移動**: `Ctrl + A` が便利です。

4. 先ほどのアプリのログ (`/var/log/todo-app/app.log`) から、特定のエラー文字列（`ERROR`）を検知してアラートを発火させるため、ファイルの末尾に以下の設定を追記し、保存して閉じます。（※ nano エディタの場合は `Ctrl+O` -> `Enter` で保存し、`Ctrl+X` で終了します）

```toml
[plugin.checks.todo-app-log]
command = ["check-log", "--file", "/var/log/todo-app/app.log", "--pattern", "ERROR"]
```

Positive
: **設定ファイル (TOML形式) の解説**
: * `[plugin.checks.todo-app-log]`: チェック監視プラグインの設定セクションです。`todo-app-log` は監視項目の名前で、Mackerel のダッシュボードに表示されます。
: * `command`: 実行するチェックコマンドです。`check-log` プラグインが `/var/log/todo-app/app.log` ファイルを監視し、`ERROR` という文字列が見つかるとアラートを発報します。

5. 設定を反映させるために Mackerel エージェントを再起動します。

```console
sudo systemctl restart mackerel-agent
```

Positive
: **Linux コマンドの補足: systemctl とは？**
: `systemctl` は Linux のサービス（バックグラウンドで動くプログラム）を管理するコマンドです。
: * `sudo systemctl restart <サービス名>`: サービスを再起動します（設定変更を反映させたい時に使います）。
: * `sudo systemctl status <サービス名>`: サービスの現在の状態（動作中か停止中か）を確認できます。
: * `sudo systemctl start <サービス名>`: サービスを開始します。
: * `sudo systemctl stop <サービス名>`: サービスを停止します。
:
: 設定ファイルを変更した後は `restart` で再起動しないと変更が反映されません。

6. アプリの **エラー発生用 URL**（`http://<EC2のIPまたはパブリックDNS>:8080/error`）へ何度かアクセスし、意図的にエラーログを発生させます。
7. Mackerel のダッシュボードの左メニュー「**Alerts (アラート)**」から、指定したログ監視アラート（`todo-app-log`）が CRITICAL として検知・発報していることを確認します。


---

## 脆弱性の検知と修復 (Snyk)
Duration: 0:20:00

開発と運用（DevSecOps）において、使用しているライブラリ（パッケージ）に脆弱性がないかチェックすることは重要です。
ここでは意図的に古い脆弱なパッケージを入れ、ツールで検知し、安全なバージョンに修復します。

### 脆弱なパッケージの導入
Kiro-IDE または EC2 のターミナル上で、作業用のソースコードディレクトリ（フォルダ）に移動し、わざと古いパッケージを指定してインストールします。（例：Python の requests や Jinja2 の古いバージョン）

Positive
: **Linux コマンドの補足: ディレクトリの移動**
: Linux 環境で特定のフォルダ（ディレクトリ）に移動する場合は、`cd` (change directory) コマンドを使用します。今回の EC2 の例では、アプリの配置場所である `/opt/todo-app` に移動する必要があります（例: `cd /opt/todo-app` を実行）。

```console
# Pythonの例
pip install requests==2.19.1
pip freeze > requirements.txt
```

Positive
: **用語解説**
: * **pip**: Python のライブラリをインストールするためのツールです。
: * **pip freeze**: 現在インストールされているライブラリとそのバージョンを一覧表示します。
: * **requirements.txt**: プロジェクトに必要なライブラリを書き出したファイルです。これがあることで、他の環境でも同じ構成を再現できます。 `>` は「コマンドの結果をファイルに書き出す」という Linux の機能（リダイレクト）です。

### セキュリティスキャンの実行（例: Snyk）
1. [Snyk](https://snyk.io/) のアカウントを作成し、CLI メニューの手順に従って Kiro-IDE 環境に Snyk CLI をインストールします。
2. 認証を行います。

Positive
: **用語解説: npm とは？**
: 「Node Package Manager」の略で、JavaScript / TypeScript のライブラリ（パッケージ）を管理するツールです。Python における `pip` と同じ役割です。`npm install -g snyk` の `-g` は「グローバル（システム全体）にインストールする」という意味で、どのディレクトリからでも `snyk` コマンドが使えるようになります。

Positive
: **Snyk CLI を使うための前提条件**
: Snyk CLI を動かすには **Node.js** が必要です。Kiro-IDE 環境には通常プリインストールされていますが、`node --version` を実行してバージョンが表示されない場合は、以下のコマンドで Node.js をインストールしてください。
: ```console
: # Amazon Linux 2023 の場合
: sudo dnf install -y nodejs
: ```

```console
npm install -g snyk
snyk auth
```

Positive
: **コマンドの解説**
: * `npm install -g snyk`: Snyk の CLI ツールをグローバルにインストールします。
: * `snyk auth`: ブラウザが開き、Snyk アカウントとの認証（ログイン連携）を行います。ブラウザが開かない環境の場合は、`snyk auth --token <YOUR_TOKEN>` のように Snyk の Web 画面から取得したトークンを直接指定することもできます。

3. プロジェクトディレクトリでスキャンを実行します。

```console
snyk test
```

Positive
: **コマンドの解説**
: `snyk test` は、カレントディレクトリ（現在いるフォルダ）にある `requirements.txt` や `package.json` などの依存関係ファイルを読み取り、使用しているライブラリに既知の脆弱性がないかをチェックします。結果には脆弱性の深刻度（Low / Medium / High / Critical）、影響を受けるパッケージ名、推奨される修正バージョンなどが表示されます。

4. 古い `requests` パッケージに「High」や「Critical」な脆弱性が複数見つかることを確認してください。

### 修復 (Remediation) 作業
出力されたアドバイスに従い、安全なバージョンにアップデートします。

```console
# 提案された安全なバージョンや最新バージョンへアップデート
pip install requests --upgrade
pip freeze > requirements.txt
```

Positive
: **コマンドの解説**
: * `pip install requests --upgrade`: `requests` ライブラリを最新の安全なバージョンにアップデートします。`--upgrade` を付けないと、既にインストール済みの場合は何もしません。
: * `pip freeze > requirements.txt`: アップデート後のライブラリ一覧を `requirements.txt` に上書き保存します。これにより、修正後の安全な状態が記録されます。

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

Positive
: **コマンドの解説**
: `delete-stack` は、指定したスタック名に紐づくすべての AWS リソース（EC2、セキュリティグループ、IAM ロールなど）をまとめて削除します。手動で一つずつ消す必要がないのが CloudFormation の大きなメリットです。

Positive
: **削除が完了したか確認する方法**
: `delete-stack` コマンドは即座に完了しますが、実際のリソース削除には数分かかります。以下のいずれかの方法で削除完了を確認してください。
: * **CLI で確認**: 以下のコマンドを実行し、ステータスが `DELETE_COMPLETE` になるか、スタックが見つからない（エラーになる）ことを確認します。
:   ```console
:   aws cloudformation describe-stacks --stack-name saga-o11y-handson
:   ```
: * **マネジメントコンソールで確認**: CloudFormation の画面を開き、フィルターで「削除済み」を含めて表示すると、`DELETE_COMPLETE` のステータスを確認できます。スタック一覧から消えていれば削除完了です。

Negative
: **削除に失敗した場合**
: ステータスが `DELETE_FAILED` になった場合は、CloudFormation の「イベント」タブでエラー原因を確認してください。手動で追加したリソース（例: セキュリティグループのルールなど）が原因で削除できないことがあります。その場合は、該当リソースを手動で削除してから再度 `delete-stack` を実行してください。

### 手動で作成したリソースの削除
CloudFormation で管理されていない、CLI で手動作成したリソースも忘れずに削除しましょう。

```console
# SNS トピックの削除（TOPIC_ARN 変数が残っている場合）
aws sns delete-topic --topic-arn $TOPIC_ARN

# CloudWatch アラームの削除
aws cloudwatch delete-alarms --alarm-names "ToDoAppErrorAlarm"

# メトリクスフィルターの削除
aws logs delete-metric-filter --log-group-name "todo-app-logs" --filter-name "ErrorFilter"

# ロググループの削除
aws logs delete-log-group --log-group-name "todo-app-logs"
```

Positive
: **TOPIC_ARN 変数が消えてしまった場合**
: ターミナルを閉じると変数は消えてしまいます。その場合は以下のコマンドで ARN を確認できます。
: ```console
: aws sns list-topics
: ```
: 表示された一覧から `todo-app-alerts` を含む ARN をコピーして使用してください。

### Kiro-IDE 環境の削除
用済みになった場合は、手順に従って Kiro-IDE 自体の CloudFormation スタックも削除してください。

### 外部サービスの後処理
* **Mackerel**: 作成したオーガニゼーション、ホスト設定などを必要に応じて退会・削除してください。
* **Snyk**: 連携したプロジェクト情報などを削除してください。

以上で本ハンズオンは終了です。お疲れ様でした！

