# AWS Environment Policies (SCP/RCP) & IAM Setup

このディレクトリ (`99-policy/`) には、本リポジトリで提供している各種AWSハンズオン（06〜14章）を安全に実行するために組織全体に適用する **Service Control Policy (SCP)** および **Resource Control Policy (RCP)**、そして作業用IAMユーザーを払い出すための仕組みが格納されています。

## 目次・ディレクトリ構成

```text
99-policy/
├── 06-CloudWatch-Logs-Metrics/         ... (各章ごとのSCP.json/RCP.json)
├── 07-SITCD-Initial-Setup/
├── 08-SITCD-Resource-Setup/
├── 09-AWS-handson-4-beginners-saga-serverlss-001/
├── 10-AWS-handson-4-beginners-saga-serverlss-002/
├── 11-AWS-handson-4-beginners-saga-serverlss-003/
├── 12-AWS-handson-4-beginners-saga-serverlss-004/
├── 13-Google-Apps-Script-4-Begineers/
├── 14-AWS-handson-4-beginners-saga-o11y/
└── iam-admin-user.yaml                 ... (AdministratorAccessユーザーの自動作成テンプレート)
```

## ポリシーの設計方針 (SCP / RCP)

すべてのハンズオン環境に対して共通で、以下の強固なガードレールが適用されるよう設計されています。

1. **原則全サービス拒否 ＆ 必要サービスのみ許可 (ホワイトリスト制)**
   - `Effect: Deny` および `NotAction` を用いることで、指定のサービス以外を強力に拒否します。
   - ハンズオンの対象章で使用するサービス（例えば S3, API Gateway, Lambda など）および共通で必要なベースサービス (IAM, STS, CloudFormation 等) のみ例外的に許可されます。

2. **許可リージョンの制限**
   - 以下のリージョン以外での操作はすべて拒否されます。
     - バージニア北部 (`us-east-1`)
     - オレゴン (`us-west-2`)
     - 東京 (`ap-northeast-1`)
     - 大阪 (`ap-northeast-3`)
   - ※ IAM や CloudFront などのグローバルサービスについては、このリージョン制限から除外（許可）する設定を含んでいます。

3. **EC2 インスタンスタイプの制限 (※ SCPのみ適用)**
   - EC2を利用してコンピューティング環境を立ち上げる場合の不正利用や高額請求を防ぐため、以下の少額・検証用インスタンスタイプ以外での起動(`ec2:RunInstances`)を禁止しています。
     - **t3系**: `t3.nano` 〜 `t3.2xlarge`
     - **t4g系**: `t4g.micro` 〜 `t4g.2xlarge`

## 各章ごとの追加許可サービス一覧

全章共通で許可されるベースサービス (`iam`, `sts`, `tag`, `cloudformation`, `s3`) に加えて、それぞれの章ごとに以下の該当サービスが追加で利用可能になっています。

| 章番号 | ハンズオンタイトル | 必要な追加サービス等 |
| :---: | :--- | :--- |
| **06** | CloudWatch Logs & Metrics | CloudWatch, Logs, EC2 |
| **07** | SITCD Initial Setup | EC2, SSM, Lambda |
| **08** | SITCD Resource Setup | DynamoDB, Lambda, API Gateway |
| **09** | saga-serverlss-001 | CloudWatch, DynamoDB, EventBridge, Lambda, Logs, SNS |
| **10** | saga-serverlss-002 | CloudFront, CloudWatch, WAFv2 |
| **11** | saga-serverlss-003 | API Gateway, Amplify, AppSync, CloudFront, CloudWatch, DynamoDB, Lambda, WAFv2 |
| **12** | saga-serverlss-004 | API Gateway, Amplify, CloudFront, CloudWatch, Cognito, DynamoDB, Lambda, Logs, WAFv2 |
| **13** | Google Apps Script 4 Begineers | (AWSへの直接アクセスは想定されないためベースのみ) |
| **14** | saga-o11y | CloudWatch, EC2, SNS, SSM, Logs, EventBridge, AWS X-Ray |

## ハンズオン用 IAM ユーザーの自動作成 (StackSets利用)

本環境では、ルートユーザーの操作・共有を行いません。受講者に対する IAM ユーザーの払い出しは、**CloudFormation StackSets** を用いて自動化されています。

具体的には、上記の SCP および RCP が適用されている AWS Organizations の該当 OU（Organizational Unit）に所属する各ハンズオン用アカウントに向けて、`iam-admin-user.yaml` テンプレートを StackSets で一括展開（デプロイ）します。

> **💡 AdministratorAccess について**
> 払い出されたIAMユーザーには `AdministratorAccess` が直接アタッチされています。しかし、親となる OU に SCP や RCP が被さって評価されるため、事実上アカウント内では**「ハンズオン用に許可されたサービス、指定された4リージョン、特定サイズのインスタンスタイプ」でしか行動できない**ように安全に隔離（サンドボックス化）されています。
