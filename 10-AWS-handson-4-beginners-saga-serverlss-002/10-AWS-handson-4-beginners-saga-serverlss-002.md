author: Shibao,Tetsuya
summary: サーバレスでindex.html, CSS, images/ ホスティング - AWS CDK, CloudFront, S3, CloudWatch を使ったハンズオン
id: 10-AWS-handson-4-beginners-saga-serverlss-002
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# サーバレスで静的Webサイトをホスティングするハンズオン

## はじめに
Duration: 0:05:00

### ハンズオンの概要

このハンズオンでは、AWS CDKを使って、S3 + CloudFrontで静的Webサイト（HTML/CSS/画像）をホスティングする環境を構築します。  
CloudWatchでアクセスログの監視も設定します。

### 使用するAWSサービス

* **Amazon S3** - 静的ファイル（HTML, CSS, 画像）の保存先
* **Amazon CloudFront** - CDNによるコンテンツ配信
* **AWS CDK** - IaCによるインフラの自動構築
* **Amazon CloudWatch** - アクセスログの監視

### 前提条件

* AWSアカウントを持っていること
* GitHubアカウントを持っていること
* GitHub Codespaces でAWS CLIが利用可能であること（[環境構築ハンズオン](../00-Install-AWS-CLI-to-RPI/web/) を参照）
* Node.jsはCodespaces上にプリインストール済みです
* TypeScriptの基本的な知識があること（なくても実施可能）

Positive
: AWS CDKを使うことで、インフラをコードで管理できます。再現性が高く、環境の複製も容易です。

Negative
: 本ハンズオンで作成するリソースには料金が発生する場合があります。ハンズオン終了後は必ずリソースを削除してください。

## 開発環境の構築
Duration: 0:10:00

### AWS CDKのインストール

AWS CDKをグローバルにインストールします。

```console
npm install -g aws-cdk
cdk --version
```

### CDKプロジェクトの作成

プロジェクトディレクトリを作成し、CDKプロジェクトを初期化します。

```console
mkdir handson-static-hosting
cd handson-static-hosting
cdk init app --language typescript
```

Positive
: `cdk init` コマンドにより、TypeScriptベースのCDKプロジェクトが自動生成されます。

### プロジェクト構成の確認

以下のようなディレクトリ構成が生成されます。

```
handson-static-hosting/
├── bin/
│   └── handson-static-hosting.ts
├── lib/
│   └── handson-static-hosting-stack.ts
├── website/          ← ★ これから作成
│   ├── index.html
│   ├── style.css
│   └── images/
├── cdk.json
├── package.json
└── tsconfig.json
```

## 静的Webサイトの作成
Duration: 0:15:00

### ディレクトリの作成

```console
mkdir -p website/images
```

### index.htmlの作成

`website/index.html` を以下の内容で作成します。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AWS サーバレスハンズオン</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <h1>☁️ AWS Serverless Handson</h1>
        </nav>
    </header>
    <main>
        <section class="hero">
            <h2>サーバレスで始めるWebホスティング</h2>
            <p>S3 + CloudFrontで高速・低コストなWebサイトを構築しよう</p>
        </section>
        <section class="features">
            <div class="feature-card">
                <h3>🚀 高速配信</h3>
                <p>CloudFrontのCDNで世界中に高速配信</p>
            </div>
            <div class="feature-card">
                <h3>💰 低コスト</h3>
                <p>サーバレスだから使った分だけ課金</p>
            </div>
            <div class="feature-card">
                <h3>🔒 セキュア</h3>
                <p>HTTPS対応で安全に配信</p>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 AWS Handson. All rights reserved.</p>
    </footer>
</body>
</html>
```

### style.cssの作成

`website/style.css` を以下の内容で作成します。

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #0a0a2e 0%, #1a1a4e 100%);
    color: #ffffff;
    min-height: 100vh;
}

header nav {
    display: flex;
    justify-content: center;
    padding: 1.5rem 2rem;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
}

.hero {
    text-align: center;
    padding: 4rem 2rem;
}

.hero h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    background: linear-gradient(90deg, #00d2ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 1.2rem;
    color: #aaa;
}

.features {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 2rem;
    flex-wrap: wrap;
}

.feature-card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 2rem;
    width: 280px;
    text-align: center;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
}

.feature-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.8rem;
}

.feature-card p {
    color: #bbb;
}

footer {
    text-align: center;
    padding: 2rem;
    color: #666;
    margin-top: 3rem;
}
```

## CDKスタックの実装
Duration: 0:20:00

### 必要なパッケージのインストール

```console
npm install aws-cdk-lib constructs
```

### スタックファイルの編集

`lib/handson-static-hosting-stack.ts` を以下の内容に書き換えます。

```typescript
import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import { Construct } from 'constructs';

export class HandsonStaticHostingStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3バケット（WebサイトホスティングはCloudFront経由のため不要）
    const websiteBucket = new s3.Bucket(this, 'WebsiteBucket', {
      bucketName: `handson-website-${this.account}`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
    });

    // CloudFrontディストリビューション
    const distribution = new cloudfront.Distribution(this, 'Distribution', {
      defaultBehavior: {
        origin: origins.S3BucketOrigin.withOriginAccessControl(websiteBucket),
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        cachePolicy: cloudfront.CachePolicy.CACHING_OPTIMIZED,
      },
      defaultRootObject: 'index.html',
      enableLogging: true,
    });

    // S3へのデプロイ
    new s3deploy.BucketDeployment(this, 'DeployWebsite', {
      sources: [s3deploy.Source.asset('./website')],
      destinationBucket: websiteBucket,
      distribution,
      distributionPaths: ['/*'],
    });

    // CloudWatchダッシュボード
    const dashboard = new cloudwatch.Dashboard(this, 'WebsiteDashboard', {
      dashboardName: 'handson-website-dashboard',
    });

    dashboard.addWidgets(
      new cloudwatch.GraphWidget({
        title: 'CloudFront Requests',
        left: [
          new cloudwatch.Metric({
            namespace: 'AWS/CloudFront',
            metricName: 'Requests',
            dimensionsMap: {
              DistributionId: distribution.distributionId,
              Region: 'Global',
            },
            statistic: 'Sum',
            period: cdk.Duration.minutes(5),
          }),
        ],
      }),
      new cloudwatch.GraphWidget({
        title: 'CloudFront Error Rate',
        left: [
          new cloudwatch.Metric({
            namespace: 'AWS/CloudFront',
            metricName: '4xxErrorRate',
            dimensionsMap: {
              DistributionId: distribution.distributionId,
              Region: 'Global',
            },
            statistic: 'Average',
            period: cdk.Duration.minutes(5),
          }),
          new cloudwatch.Metric({
            namespace: 'AWS/CloudFront',
            metricName: '5xxErrorRate',
            dimensionsMap: {
              DistributionId: distribution.distributionId,
              Region: 'Global',
            },
            statistic: 'Average',
            period: cdk.Duration.minutes(5),
          }),
        ],
      }),
    );

    // 出力
    new cdk.CfnOutput(this, 'DistributionDomainName', {
      value: distribution.distributionDomainName,
      description: 'CloudFrontのURL',
    });

    new cdk.CfnOutput(this, 'BucketName', {
      value: websiteBucket.bucketName,
      description: 'S3バケット名',
    });
  }
}
```

Positive
: OAC（Origin Access Control）を使用することで、S3バケットへの直接アクセスをブロックし、CloudFront経由のみでアクセスを許可できます。

## CDKデプロイ
Duration: 0:15:00

### CDKブートストラップ

初めてCDKを利用する場合は、ブートストラップを実行します。

```console
cdk bootstrap aws://{アカウントID}/ap-northeast-1
```

Negative
: `{アカウントID}` は自分のAWSアカウントIDに置き換えてください。

### 差分確認

デプロイ前に変更内容を確認します。

```console
cdk diff
```

### デプロイ

```console
cdk deploy
```

デプロイ中に確認が求められた場合は `y` を入力します。

Positive
: デプロイには数分かかる場合があります。CloudFrontディストリビューションの作成に特に時間がかかります。

### デプロイ完了

デプロイが完了すると、以下のような出力が表示されます。

```
Outputs:
HandsonStaticHostingStack.DistributionDomainName = d1234567890.cloudfront.net
HandsonStaticHostingStack.BucketName = handson-website-{アカウントID}
```

## 動作確認
Duration: 0:10:00

### Webサイトの確認

出力されたCloudFrontのURLにブラウザでアクセスします。

```
https://d1234567890.cloudfront.net
```

以下を確認しましょう。

* HTMLページが正しく表示される
* CSSスタイルが適用されている
* HTTPSでアクセスできる

### CloudWatchダッシュボードの確認

1. AWSマネジメントコンソールから **CloudWatch** を選択
2. 左メニューの **ダッシュボード** をクリック
3. `handson-website-dashboard` を選択
4. リクエスト数とエラー率のグラフを確認

Positive
: CloudFrontのメトリクスはリアルタイムではなく、数分の遅延がある場合があります。

### コンテンツの更新

Webサイトの内容を更新したい場合は、`website/` ディレクトリのファイルを編集し、再デプロイします。

```console
cdk deploy
```

CDKが自動的にS3のファイルを更新し、CloudFrontのキャッシュを無効化します。

## リソースの削除
Duration: 0:05:00

### CDKで作成したリソースの削除

CDKで作成したリソースは、以下のコマンドで一括削除できます。

```console
cdk destroy
```

確認が求められた場合は `y` を入力します。

Positive
: CDKの `RemovalPolicy.DESTROY` と `autoDeleteObjects: true` を設定済みのため、S3バケットも含めて全て自動削除されます。

### CDKブートストラップリソースの削除（任意）

CDKブートストラップで作成されたS3バケットとCloudFormationスタックが残ります。  
完全にクリーンアップしたい場合は以下を実行してください。

1. S3コンソールで `cdk-hnb659fds-assets-{アカウントID}-ap-northeast-1` バケットを空にして削除
2. CloudFormationコンソールで `CDKToolkit` スタックを削除

Negative
: CDKブートストラップを削除すると、次回CDKを使用する際に再度ブートストラップが必要になります。他のCDKプロジェクトにも影響するため、削除は慎重に行ってください。

## まとめ
Duration: 0:05:00

### 学んだこと

このハンズオンでは以下のことを学びました。

* **AWS CDK** を使ったIaC（Infrastructure as Code）によるインフラ構築
* **Amazon S3** を使った静的ファイルのホスティング
* **Amazon CloudFront** を使ったCDN配信とHTTPS対応
* **Amazon CloudWatch** を使ったアクセスログの監視とダッシュボード作成
* OAC（Origin Access Control）によるセキュアなS3アクセス制御

### 発展課題

* 独自ドメイン（Route 53 + ACM）を設定してみましょう
* WAF（Web Application Firewall）を追加してセキュリティを強化してみましょう
* CloudFrontのキャッシュポリシーをカスタマイズしてみましょう
* CloudWatch Alarmを設定してエラー率の閾値超過を通知してみましょう

### 参考リンク

<button>
  [AWS CDK ドキュメント](https://docs.aws.amazon.com/ja_jp/cdk/)
</button>

<button>
  [Amazon CloudFront ドキュメント](https://docs.aws.amazon.com/ja_jp/cloudfront/)
</button>

<button>
  [Amazon S3 ドキュメント](https://docs.aws.amazon.com/ja_jp/s3/)
</button>

<button>
  [Amazon CloudWatch ドキュメント](https://docs.aws.amazon.com/ja_jp/cloudwatch/)
</button>
