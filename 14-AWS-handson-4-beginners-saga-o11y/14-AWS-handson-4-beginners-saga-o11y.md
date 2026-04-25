author: Shibao,Tetsuya
summary: AWSを使った簡単なObservability（O11y）と脆弱性管理のハンズオン
id: 14-AWS-handson-4-beginners-saga-o11y
categories: codelab,markdown,aws,o11y,security
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# AWS Hands-on for Beginners: Saga Edition (O11y & Security)

## はじめに
Duration: 0:05:00

### ハンズオンの目的
このハンズオンは、**佐賀の皆さんにAWSの楽しさを知ってもらうための特別編**です！
「アプリのログを収集し、可視化・通知する」という Observability (O11y / 可観測性) の基本を学びます。
また、意図的に脆弱性を含んだパッケージを導入し、セキュリティツール（Snyk）を使って検知・修復する DevSecOps の基本的な流れを体験します。

Positive
: **タイトルの「Saga」について**
: このハンズオンの「Saga」は、マイクロサービスの難しい用語（Sagaパターン）ではなく、**私たちの「佐賀」**を指しています！佐賀のエンジニアや学習者の皆さんが、クラウドの運用とセキュリティの一歩を踏み出すためのガイドです。

Positive
: **用語解説: O11y (Observability / 可観測性) とは？**
: システムの内部状態を「ログ」「メトリクス」「トレース」で把握できるようにする考え方です。
: お医者さんの診察に例えると、**「熱がある（異常）」と気づくのが「監視」**なら、**「なぜ熱が出たのか（原因）」を調べるのが「O11y」**です。複雑なシステムで「どこが悪いか」を素早く突き止めるための地図を作る作業だと考えてください。

Positive
: **用語解説: DevSecOps とは？**
: 「Development（開発）」「Security（セキュリティ）」「Operations（運用）」を組み合わせた言葉です。従来はアプリを作った後にセキュリティチェックを行っていましたが、DevSecOps では開発の早い段階からセキュリティを組み込むことで、弱点を早期に発見・修正します。

Positive
: **用語解説: 脆弱性（ぜいじゃくせい）とは？**
: ソフトウェアに存在するセキュリティ上の欠陥や弱点のことです。お店の鍵が壊れていたり、壁に穴が開いていたりするイメージです。放置するとデータの漏洩などの被害につながるため、定期的な点検が必要です。

### アーキテクチャと使用技術
* **インフラ**: AWS EC2 (CloudFormation で構築)
* **アプリケーション**: Python (Flask または Django) / TypeScript 等で作成した簡単な ToDo アプリ (DBは SQLite)
* **開発環境**: Kiro-IDE Remote、GitHub Codespaces、または自身のローカルPCなどを利用してコーディング・操作を行います。
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
1. **開発環境 (Kiro-IDE / Codespaces / ローカルPC)**: あなたの「作業用 PC」です。ここで設計図（CloudFormation）を書いたり、セキュリティスキャンを実行したりします。
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

## IAMユーザーのアクセスキーの発行と設定 (Kiro-IDE 以外の場合)
Duration: 0:10:00

Kiro-IDE 以外（オプション2〜4）の環境を利用する場合は、AWS リソースを操作するためのアクセスキー（認証情報）が必要です。以下の手順で IAM ユーザーのアクセスキーを発行し、設定してください。

Negative
: **【重要】アクセスキーの利用に関する注意喚起**
: IAM ユーザーの永続的なアクセスキーを発行する本手順は、**あくまでも今回のハンズオンを簡単に進めるための限定的な手段**です。
: 実際の開発現場や本番運用においては、セキュリティの観点から永続的なアクセスキーの利用は推奨されていません。現在は `aws login`（AWS IAM Identity Center との統合）や `aws sso login` などを利用し、一時的な（有効期限のある）認証トークンを取得して利用することが前提・ベストプラクティスとされています。
: 
: * 参考: [AWS CLI での認証の簡素化 – 新しいコマンド「aws login」を一般公開](https://aws.amazon.com/jp/blogs/news/simplified-developer-access-to-aws-with-aws-login/)

### アクセスキーの発行手順

1. **AWS マネジメントコンソール**にログインし、**IAM** (Identity and Access Management) サービスを開きます。
2. 左側のメニューから「**ユーザー**」を選択し、本ハンズオン用のユーザー（例: AdministratorAccess 権限を持つユーザー）をクリックします。
3. 「**セキュリティ認証情報**」タブを選択します。
4. 「**アクセスキーを作成**」ボタンをクリックします。
5. ユースケースとして「**コマンドラインインターフェイス (CLI)**」を選択し、確認のチェックを入れて「次へ」をクリックします。
6. (任意) 説明タグを入力し、「**アクセスキーを作成**」をクリックします。
7. 発行された「**アクセスキー**」と「**シークレットアクセスキー**」をメモするか、CSVファイルをダウンロードします（※この画面を閉じるとシークレットアクセスキーは二度と確認できません）。

Positive
: 画面の詳しい操作手順については、こちらの記事も参考にしてください。
: * [2023年版：IAMユーザーのアクセスキーを作成してみる (DevelopersIO)](https://dev.classmethod.jp/articles/iam_user_create_access_keys_2023/)

### アクセスキーの設定 (aws configure)

ご自身の開発環境のターミナルで以下のコマンドを実行し、先ほど発行したキーを設定します。

```console
aws configure
```

対話形式で以下のように入力してください。
* **AWS Access Key ID**: (取得したアクセスキー)
* **AWS Secret Access Key**: (取得したシークレットアクセスキー)
* **Default region name**: `ap-northeast-1` (東京リージョンの場合)
* **Default output format**: `json`

設定後、以下のコマンドでエラーが出ず、ご自身のアカウント情報が表示されれば設定は完了です。

```console
aws sts get-caller-identity
```

---

## 開発環境の準備
Duration: 0:10:00

本ハンズオンでは、以下の4つの方法からお好きな開発環境を選択して進めることができます。

1. **Kiro-IDE Remote を使う場合** (推奨: AWS上に環境を自動構築)
2. **GitHub Codespaces を使う場合** (ブラウザ上で完結)
3. **ローカルの VSCode を使う場合** (自身の端末)
4. **自身の端末を利用する場合** (ローカル環境)

---

### オプション1: Kiro-IDE Remote を使う場合

AWS 上に簡単に Web 開発環境を構築できる **Kiro-IDE Remote** を使用します。ローカル PC に環境を構築することなく、また IAM の設定なども自動で行われるため、最も推奨される手順です。

#### Kiro-IDE の起動
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
9. **Session Manager プラグインのインストール**: Kiro 上の AI チャット機能（**Vibe**）を開き、「`Session Manager プラグインをインストールする`」と入力して送信します。AI が提示した手順やコマンドに従って、Session Manager プラグインをインストールしてください。

---

### オプション2: GitHub Codespaces を使う場合

ブラウザ上で完結する開発環境である GitHub Codespaces を利用することもできます。

#### Codespace の起動とツールのインストール

[GitHub Codespaces](https://github.com/codespaces) にアクセスし、任意のテンプレート（Blank template など）から新しい Codespace を作成して起動します。
Codespace が起動したら、ターミナルで以下のコマンドを順番に実行し、必要なツールをインストール・更新します。

1. **AWS CLI (v2) のインストール**
   ```console
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   ```

2. **AWS SSM Plugin のインストール**
   ```console
   curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb"
   sudo dpkg -i session-manager-plugin.deb
   ```

3. **Python を最新にする**
   ```console
   sudo apt-get update
   sudo apt-get install -y python3 python3-pip
   ```

4. **Node (npm) を最新にする**
   Codespaces には `nvm` (Node Version Manager) がプリインストールされているため、それを利用して最新の Node.js をインストールします。
   ```console
   nvm install node
   nvm use node
   npm install -g npm@latest
   ```

Negative
: **IAMユーザーの作成と認証設定について**
: GitHub Codespaces を使用する場合は、別途 IAM ユーザー（AdministratorAccess 等の権限を持つもの）を作成し、ターミナルで `aws configure` コマンドを使用してアクセスキーとシークレットアクセスキーを設定する必要があります。

---

### オプション3: ローカルの VSCode を使う場合

ご自身の PC のローカル環境で VSCode を使って進めることも可能です。必要な開発環境が自動で揃うテンプレートリポジトリを活用します。

#### テンプレートからリポジトリを作成

1. [GitHub](https://github.com/) にログインします
2. テンプレートリポジトリ [midnight480/aws-handson-template](https://github.com/midnight480/aws-handson-template) を開きます
3. **Use this template** → **Create a new repository** をクリックします
4. リポジトリ名に任意の名前を入力し、**Create repository** をクリックします

#### リポジトリのクローンと VSCode での起動

作成したリポジトリをご自身の PC にクローン（ダウンロード）し、VSCode で開きます。

Positive
: テンプレートリポジトリには開発環境の設定（devcontainer）が含まれており、VSCode の Dev Containers 拡張機能を使用することで、AWS CLI、Python、Node.js などが自動的にインストールされた環境を利用できます。

#### AWS CLI の動作確認

VSCode のターミナルを開き、AWS CLI が利用可能になっていることを確認します。

```console
aws --version
```

`aws-cli/2.x.x` のようにバージョンが表示されればOKです。

---

### オプション4: 自身の端末を利用する場合

ご自身の PC (Windows, Mac, Linux など) のローカル環境で進めることも可能です。その場合は、以下のツールがあらかじめインストールされている必要があります。

1. **AWS CLI (v2)**
   - AWS リソースをコマンドラインから操作するために必要です。
   - [AWS CLI のインストールと更新 (公式ドキュメント)](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html) を参照してインストールしてください。
2. **Session Manager プラグイン (SSM Plugin)**
   - EC2 インスタンスにコマンドラインから安全に接続するために必要です（本ハンズオンではマネジメントコンソールのブラウザ経由で接続することも可能ですが、CLIから接続する場合に必須となります）。
   - [Session Manager プラグインをインストールする (公式ドキュメント)](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) を参照してインストールしてください。
3. **Node.js (npm)**
   - 後半の Snyk CLI インストールや動作のために必要になります。
   - [Node.js 公式サイト](https://nodejs.org/ja/) などからインストールしてください。
4. **AWS 認証情報の設定**
   - ターミナルで `aws configure` を実行し、AWS へのアクセス権限を持つ IAM ユーザーのアクセスキーを設定してください。
   ```console
   $ aws configure

   Tip: You can deliver temporary credentials to the AWS CLI using your AWS Console session by running the command 'aws login'.

   AWS Access Key ID [None]: AK***
   AWS Secret Access Key [None]: ***
   Default region name [None]: ap-northeast-1
   Default output format [None]: json

   $ aws sts get-caller-identity
   {
       "UserId": "***",
       "Account": "***",
       "Arn": "arn:aws:iam::***:user/handson-admin"
   }
   ```

Positive
: 各ツールのインストール後、ターミナルで `aws --version` や `session-manager-plugin`、`npm --version` を実行し、正しくインストールされているか確認しましょう。

---

## インフラとアプリのデプロイ
Duration: 0:15:00

### CloudFormationテンプレートの作成と実行
ToDoアプリを動かすためのEC2インスタンスを、CloudFormationを利用して構築します。

Positive
: **CloudFormationとは？**
: AWS上のインフラ環境（サーバーやネットワークなど）を、設計図（テンプレート）としてコード化して自動構築するサービスです。「スタック」とは、その設計図をもとに作られたAWSリソースのグループのことです。手動で一つずつ設定するよりも、早く・正確にインフラを用意できます。

1. 開発環境のエディタを開き、新規ファイル `todo-app-template.yaml` を作成します。
   * **作成方法**: 左側のファイルエクスプローラーで右クリックし「New File」を選択するか、上部メニューの File > New Text File から作成し、名前を付けて保存します。

Positive
: **■日本語入力**
: もしかしたら、デフォルトで英語になっているかもしれません。
: Windowsの場合は `Ctrl + Space`、Macの場合は `Control + Space` や `Cmd + Space` などで直接／日本語入力を切り替えられる場合があります。半角・全角キーでの切り替えを行いたい場合一度設定を再起動してください。

Positive
: **■その他 (Kiro-IDE 利用時のヒント)**
: * Kiro CLI で認証がなかなか進まない場合、`kiro-cli login --use-device-flow` を試してみてください。
: * ターミナルへの貼り付け（Paste）は、Windows の場合は `Ctrl + Shift + V`、Mac の場合は `Cmd + V` をお試しください。

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
      InstanceType: t4g.small
      ImageId: 'resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64'
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
          cat << 'PYEOF' > app.py
          import logging, time, random
          from flask import Flask, request, render_template_string, redirect, jsonify

          app = Flask(__name__)
          logging.basicConfig(filename='/var/log/todo-app/app.log', level=logging.INFO,
                              format='%(asctime)s %(levelname)s: %(message)s')

          todos = [
              {"task": "AWS CloudWatchを学ぶ", "done": False},
              {"task": "X-Rayのセットアップ", "done": False},
              {"task": "ToDoアプリをデプロイする", "done": True},
          ]

          HTML = """
          <!DOCTYPE html>
          <html lang="ja">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>ToDo App - O11y Hands-on</title>
            <style>
              * { box-sizing: border-box; margin: 0; padding: 0; }
              body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                     background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
                     color: #f8fafc; min-height: 100vh; padding: 2rem; }
              .container { max-width: 640px; margin: 0 auto; }
              h1 { font-size: 1.8rem; margin-bottom: 0.3rem;
                   background: linear-gradient(to right, #a78bfa, #38bdf8);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
              .subtitle { color: #94a3b8; margin-bottom: 1.5rem; font-size: 0.9rem; }
              .card { background: rgba(30,41,59,0.7); backdrop-filter: blur(12px);
                      border: 1px solid rgba(255,255,255,0.1); border-radius: 16px;
                      padding: 1.5rem; margin-bottom: 1.5rem; }
              .stats { display: flex; gap: 1rem; margin-bottom: 1rem; }
              .stat { flex: 1; text-align: center; padding: 0.8rem; border-radius: 10px;
                      background: rgba(255,255,255,0.05); }
              .stat-num { font-size: 1.5rem; font-weight: 700; }
              .stat-label { font-size: 0.75rem; color: #94a3b8; }
              .stat-num.total { color: #38bdf8; }
              .stat-num.done { color: #4ade80; }
              .stat-num.pending { color: #fbbf24; }
              form { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
              input[type="text"] { flex: 1; padding: 0.7rem 1rem; border-radius: 8px;
                     border: 1px solid rgba(255,255,255,0.15); background: rgba(15,23,42,0.6);
                     color: white; font-size: 1rem; outline: none; }
              input:focus { border-color: #8b5cf6; box-shadow: 0 0 0 2px rgba(139,92,246,0.3); }
              button, .btn { padding: 0.7rem 1.2rem; border-radius: 8px; border: none;
                     font-size: 0.9rem; font-weight: 600; cursor: pointer; color: white;
                     text-decoration: none; display: inline-block; transition: 0.2s; }
              .btn-add { background: #8b5cf6; }
              .btn-add:hover { background: #7c3aed; }
              .btn-sm { padding: 0.3rem 0.6rem; font-size: 0.75rem; border-radius: 6px; }
              .btn-done { background: #4ade80; color: #0f172a; }
              .btn-undo { background: #fbbf24; color: #0f172a; }
              .btn-del { background: #ef4444; }
              ul { list-style: none; }
              li { display: flex; align-items: center; justify-content: space-between;
                   padding: 0.7rem 0; border-bottom: 1px solid rgba(255,255,255,0.06); }
              li:last-child { border-bottom: none; }
              .task-text { flex: 1; margin: 0 0.8rem; }
              .task-done { text-decoration: line-through; color: #64748b; }
              .actions { display: flex; gap: 0.3rem; }
              .test-section { margin-top: 1rem; padding-top: 1rem;
                              border-top: 1px solid rgba(255,255,255,0.1); }
              .test-section h3 { font-size: 0.85rem; color: #94a3b8; margin-bottom: 0.5rem; }
              .test-btns { display: flex; gap: 0.5rem; flex-wrap: wrap; }
              .btn-warn { background: #f97316; }
              .btn-err { background: #ef4444; }
              .btn-slow { background: #6366f1; }
              .badge { display: inline-block; width: 8px; height: 8px; border-radius: 50%;
                       margin-right: 0.3rem; }
              .badge-done { background: #4ade80; }
              .badge-pending { background: #fbbf24; }
              .flash { background: rgba(139,92,246,0.15); border: 1px solid #8b5cf6;
                       border-radius: 8px; padding: 0.6rem 1rem; margin-bottom: 1rem;
                       font-size: 0.85rem; }
            </style>
          </head>
          <body>
            <div class="container">
              <h1>📝 ToDo App</h1>
              <p class="subtitle">AWS Observability ハンズオン用アプリケーション</p>
              {% if message %}<div class="flash">{{ message }}</div>{% endif %}
              <div class="card">
                <div class="stats">
                  <div class="stat"><div class="stat-num total">{{ total }}</div><div class="stat-label">Total</div></div>
                  <div class="stat"><div class="stat-num done">{{ done_count }}</div><div class="stat-label">Done</div></div>
                  <div class="stat"><div class="stat-num pending">{{ pending }}</div><div class="stat-label">Pending</div></div>
                </div>
                <form action="/" method="POST">
                  <input type="text" name="task" placeholder="新しいタスクを入力..." required>
                  <button type="submit" class="btn btn-add">追加</button>
                </form>
                <ul>
                {% for i, todo in todos %}
                  <li>
                    <span class="badge {{ 'badge-done' if todo.done else 'badge-pending' }}"></span>
                    <span class="task-text {{ 'task-done' if todo.done }}">{{ todo.task }}</span>
                    <div class="actions">
                      {% if todo.done %}
                        <a href="/undo/{{ i }}" class="btn btn-sm btn-undo">↩</a>
                      {% else %}
                        <a href="/done/{{ i }}" class="btn btn-sm btn-done">✓</a>
                      {% endif %}
                      <a href="/delete/{{ i }}" class="btn btn-sm btn-del">✕</a>
                    </div>
                  </li>
                {% endfor %}
                </ul>
              </div>
              <div class="card">
                <div class="test-section">
                  <h3>🔧 Observability テスト（ハンズオン用）</h3>
                  <div class="test-btns">
                    <a href="/error" class="btn btn-sm btn-err">500 Error</a>
                    <a href="/warn" class="btn btn-sm btn-warn">Warning Log</a>
                    <a href="/slow" class="btn btn-sm btn-slow">Slow Response</a>
                    <a href="/health" class="btn btn-sm btn-done" style="color:white">Health Check</a>
                  </div>
                </div>
              </div>
            </div>
          </body>
          </html>
          """

          def render(message=None):
              done_count = sum(1 for t in todos if t["done"])
              return render_template_string(HTML, todos=list(enumerate(todos)),
                  total=len(todos), done_count=done_count, pending=len(todos)-done_count,
                  message=message)

          @app.route('/', methods=['GET'])
          def get_todos():
              app.logger.info("GET / - Fetched ToDos")
              return render()

          @app.route('/', methods=['POST'])
          def add_todo():
              task = request.form.get('task', '').strip()
              if not task:
                  app.logger.error("POST / - Empty task submitted")
                  return render("タスクを入力してください"), 400
              todos.append({"task": task, "done": False})
              app.logger.info(f"POST / - Added ToDo: {task}")
              return redirect('/')

          @app.route('/done/<int:idx>')
          def mark_done(idx):
              if 0 <= idx < len(todos):
                  todos[idx]["done"] = True
                  app.logger.info(f"GET /done/{idx} - Marked done: {todos[idx]['task']}")
              return redirect('/')

          @app.route('/undo/<int:idx>')
          def mark_undo(idx):
              if 0 <= idx < len(todos):
                  todos[idx]["done"] = False
                  app.logger.info(f"GET /undo/{idx} - Marked undone: {todos[idx]['task']}")
              return redirect('/')

          @app.route('/delete/<int:idx>')
          def delete_todo(idx):
              if 0 <= idx < len(todos):
                  removed = todos.pop(idx)
                  app.logger.info(f"GET /delete/{idx} - Deleted: {removed['task']}")
              return redirect('/')

          @app.route('/error')
          def trigger_error():
              app.logger.error("GET /error - Intentional 500 error triggered!")
              return render("⚠️ 500 Internal Server Error をログに記録しました"), 500

          @app.route('/warn')
          def trigger_warn():
              app.logger.warning("GET /warn - Intentional warning triggered!")
              return render("⚠️ Warning をログに記録しました")

          @app.route('/slow')
          def trigger_slow():
              delay = random.uniform(2.0, 5.0)
              app.logger.warning(f"GET /slow - Slow response: {delay:.1f}s")
              time.sleep(delay)
              return render(f"🐢 {delay:.1f}秒の遅延レスポンスを返しました")

          @app.route('/health')
          def health():
              app.logger.info("GET /health - Health check OK")
              return jsonify({"status": "healthy", "todos": len(todos)}), 200

          if __name__ == '__main__':
              app.run(host='0.0.0.0', port=8080)
          PYEOF
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
: 4. **ToDoAppInstance**: 実際の EC2 サーバー本体です。`t4g.small` は Graviton プロセッサを搭載したコストパフォーマンスに優れた小さなサーバーサイズです。`ImageId` は OS のテンプレート（Amazon Linux 2023）を指定しています。
: 5. **UserData**: EC2 が初めて起動した時に自動実行されるスクリプトです。Python や Flask のインストール、アプリのコード配置、アプリの起動までを自動で行います。
: 6. **Outputs**: スタック作成完了後に表示される情報です。アプリの URL やインスタンス ID を確認できます。

Positive
: **YAML の特殊な記法について**
: * `!Ref InstanceRole`: 同じテンプレート内の別リソースを「参照」する関数です。「上で定義した InstanceRole を使う」という意味です。
: * `!Sub`: 文字列の中に変数を埋め込む関数です。`${ToDoAppInstance.PublicDnsName}` の部分が、実際の EC2 の DNS 名に置き換わります。
: * `Fn::Base64`: テキストを Base64 形式にエンコード（変換）します。UserData に渡すスクリプトは Base64 形式である必要があるため使用しています。

3. 開発環境のターミナルで以下のコマンドを実行し、ファイルからCloudFormationスタックを作成します。

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

4. スタックの構築完了と出力結果を確認します。

   AWS マネジメントコンソールの **CloudFormation** 画面から `saga-o11y-handson` のステータス（`CREATE_COMPLETE`）と「**出力 (Outputs)**」タブを確認することもできますが、ターミナルから以下のコマンドで確認することも可能です。

   **進行状況を待機するコマンド**（構築が完了するまで待機します。数分後にプロンプトが戻れば完了です）:
   ```console
   aws cloudformation wait stack-create-complete --stack-name saga-o11y-handson
   ```

   **出力結果を確認するコマンド**（完了後に実行します）:
   ```console
   aws cloudformation describe-stacks \
     --stack-name saga-o11y-handson \
     --query 'Stacks[0].Outputs'
   ```

   * 出力結果に表示された `AppURL` の値（`http://ec2-...`）をコピーしてブラウザで開き、ToDo アプリの画面が表示されるか確認してください。

5. 表示された ToDo アプリの画面にある入力フォームから、新しいタスク（例: `CloudWatchのログを確認する`）を入力し、「追加」ボタンを押して登録できるかテストしてみましょう。

6. この ToDo アプリは背景でログファイル（例: `/var/log/todo-app/app.log`）にアクセスログやエラーを出力していることを確認しておきましょう。

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
: 1. まず、**開発環境のエディタ**で `config.json` という名前の新規ファイルを作成し、以下の JSON 内容を貼り付けて保存します。
: 2. 保存した内容をコピーします。
: 3. EC2 インスタンスのターミナル（セッションマネージャー）で `sudo nano config.json` を実行します。
: 4. コピーした内容をターミナルに貼り付け（Windows: `Ctrl + Shift + V` / Mac: `Cmd + V`）て保存します。
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
: **nanoエディタが苦手な方へ（ワンライナーでのファイル作成）**
: エディタを使わずに、以下のワンライナーコマンドをターミナルにコピー＆ペーストして実行するだけで、一発でファイルを作成することもできます。

```console
echo '{"logs": {"logs_collected": {"files": {"collect_list": [{"file_path": "/var/log/todo-app/app.log", "log_group_name": "todo-app-logs", "log_stream_name": "{instance_id}"}]}}}}' > config.json
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
まずは、アラーム発生時にメールを通知するための SNS トピックを作成します。開発環境のターミナルから以下のコマンドを入力します。
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
4. 開発環境のブラウザまたは別タブから、ToDo アプリの **エラー発生用 URL** にアクセスし、意図的にエラーログを書き込みます。
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
: **なぜ vim ではなく nano なのか？**
: Linuxのテキストエディタといえば `vi` や `vim` が定番ですが、今回使用している環境（Ubuntuベースのブラウザターミナルなど）では、キーボードの特殊な操作がうまく受け付けられないケースがあるため、本ハンズオンではより確実に操作できる `nano` を採用しています。

Positive
: **nano エディタの基本操作**
: `nano` は Linux で使えるシンプルなテキストエディタです。画面下部にショートカットキーの一覧が表示されます（`^` は Windows/Mac ともに `Ctrl` キーを意味します。Mac の `Cmd` ではない点に注意してください）。
: * **カーソル移動**: 矢印キーで移動します。
: * **文字の入力**: そのままキーボードで入力できます。
: * **保存**: `Ctrl + O` を押し、ファイル名を確認して `Enter` を押します。
: * **終了**: `Ctrl + X` で nano を閉じます。
: * **貼り付け**: ブラウザからコピーした内容は Windowsの場合は `Ctrl + Shift + V`、Macの場合は `Cmd + V` で貼り付けます。
: * **行末へ移動**: `Ctrl + E`、**行頭へ移動**: `Ctrl + A` が便利です。

4. 先ほどのアプリのログ (`/var/log/todo-app/app.log`) から、特定のエラー文字列（`ERROR`）を検知してアラートを発火させるため、ファイルの末尾に以下の設定を追記し、保存して閉じます。（※ nano エディタの場合は `Ctrl+O` -> `Enter` で保存し、`Ctrl+X` で終了します。Macでも `Cmd` ではなく `Ctrl` キーを使用します）

```toml
[plugin.checks.todo-app-log]
command = ["check-log", "--file", "/var/log/todo-app/app.log", "--pattern", "ERROR"]
```

Positive
: **nanoエディタが苦手な方へ（ワンライナーでの追記）**
: エディタの操作に自信がない、またはキーボードがうまく反応しない場合は、以下の `echo` を使ったワンライナーコマンド（1行のコマンド）を貼り付けて実行するだけで、ファイルの末尾に設定を追記できます。

```console
echo -e '\n[plugin.checks.todo-app-log]\ncommand = ["check-log", "--file", "/var/log/todo-app/app.log", "--pattern", "ERROR"]' | sudo tee -a /etc/mackerel-agent/mackerel-agent.conf
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
ここでは**あえて脆弱な古いパッケージ**を導入し、セキュリティツールで検知・修復する流れを体験します。

Negative
: **【重要】わざと古い（悪い）お手本を作ります**
: このセクションでは、学習のために意図的に古い脆弱なバージョンをインストールします。**実際の開発現場では、常に最新の安定版を使用し、古いバージョンをそのまま使い続けることは絶対に避けてください！**

### 脆弱なパッケージの導入
開発環境 または EC2 のターミナル上で、作業用のソースコードディレクトリ（フォルダ）に移動し、わざと古いパッケージを指定してインストールします。

Positive
: **Linux コマンドの補足: ディレクトリの移動**
: Linux 環境で特定のフォルダ（ディレクトリ）に移動する場合は、`cd` (change directory) コマンドを使用します。今回の EC2 の例では、アプリの配置場所である `/opt/todo-app` に移動する必要があります（例: `cd /opt/todo-app` を実行）。

```console
# Pythonの例
# あえて脆弱性がある古いバージョン(2.19.1)を指定します
pip install requests==2.19.1
pip freeze > requirements.txt
```

Positive
: **用語解説**
: * **pip**: Python のライブラリをインストールするためのツールです。
: * **pip freeze**: 現在インストールされているライブラリとそのバージョンを一覧表示します。
: * **requirements.txt**: プロジェクトに必要なライブラリを書き出したファイルです。これがあることで、他の環境でも同じ構成を再現できます。 `>` は「コマンドの結果をファイルに書き出す」という Linux の機能（リダイレクト）です。

### セキュリティスキャンの実行（例: Snyk）
「Snyk（スニーク）」は、開発中にセキュリティ上の問題を自動で見つけてくれる便利なツールです。佐賀の現場でも、こういったツールを導入して安全な開発を行うことが推奨されます。

1. [Snyk](https://snyk.io/) のアカウントを作成し、CLI メニューの手順に従って開発環境に Snyk CLI をインストールします。
2. 認証を行います。

Positive
: **用語解説: npm とは？**
: 「Node Package Manager」の略で、JavaScript / TypeScript のライブラリ（パッケージ）を管理するツールです。Python における `pip` と同じ役割です。`npm install -g snyk` の `-g` は「グローバル（システム全体）にインストールする」という意味で、どのディレクトリからでも `snyk` コマンドが使えるようになります。

Positive
: **Snyk CLI を使うための前提条件**
: Snyk CLI を動かすには **Node.js** が必要です。Kiro-IDE や Codespaces 環境には通常プリインストールされていますが、`node --version` を実行してバージョンが表示されない場合は、以下のコマンド等で Node.js をインストールしてください。

```console
# Amazon Linux 2023 の場合
sudo dnf install -y nodejs
```

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
開発環境 または AWS マネジメントコンソールから、最初に作成した CloudFormation スタックを削除します。

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

```console
aws cloudformation describe-stacks --stack-name saga-o11y-handson
```

Positive
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

```console
aws sns list-topics
```

Positive
: 表示された一覧から `todo-app-alerts` を含む ARN をコピーして使用してください。

### 環境のお片付け

ハンズオン用に構築した EC2 インスタンス等の CloudFormation スタックを削除します。ターミナルで以下のコマンドを実行してください。

```console
aws cloudformation delete-stack --stack-name saga-o11y-handson

# 削除が完了するまで待機する場合（数分かかります）
aws cloudformation wait stack-delete-complete --stack-name saga-o11y-handson
```

* **Kiro-IDE の場合**: 用済みになった場合は、手順に従って Kiro-IDE 自体の CloudFormation スタックも削除してください。
* **Codespaces の場合**: 不要になった Codespace インスタンスを GitHub 上から削除（Delete）してください。

### 外部サービスの後処理
* **Mackerel**: 作成したオーガニゼーション、ホスト設定などを必要に応じて退会・削除してください。
* **Snyk**: 連携したプロジェクト情報などを削除してください。

以上で本ハンズオンは終了です。お疲れ様でした！

