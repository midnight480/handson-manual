author: Shibao,Tetsuya
summary: 動的ページのホスティング - AWS Amplify を使ったサーバレスハンズオン
id: 11-AWS-handson-4-beginners-saga-serverlss-003
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# Amplifyで動的Webアプリケーションをホスティングするハンズオン

## はじめに
Duration: 0:05:00

### ハンズオンの概要

このハンズオンでは、AWS Amplifyを使って動的なWebアプリケーションを構築・デプロイします。  
フォーム送信やAPIとの連携など、サーバサイドの処理を含むWebアプリケーションをサーバレスで実現します。

### 使用するAWSサービス

* **AWS Amplify** - Webアプリケーションのホスティング・バックエンドサービス
  * Amplify Hosting - フロントエンドアプリのデプロイとCDN配信
  * Amplify Functions - サーバレスAPI
  * Amplify Data - データの永続化

### 前提条件

* AWSアカウントを持っていること
* GitHubアカウントを持っていること
* GitHub Codespaces でAWS CLIが利用可能であること（[環境構築ハンズオン](../00-Install-AWS-CLI-to-RPI/web/) を参照）
* Node.js / Git はCodespaces上にプリインストール済みです

Positive
: AWS Amplifyは、フロントエンドからバックエンドまで一貫して構築できるフルスタックのサービスです。

Negative
: 本ハンズオンで作成するリソースには料金が発生する場合があります。ハンズオン終了後は必ずアプリを削除してください。

## アプリケーションの作成
Duration: 0:10:00

### Amplifyプロジェクトの初期化

新しいAmplifyプロジェクトを作成します。

```console
npm create amplify@latest -- --yes
cd my-amplify-app
```

Positive
: `npm create amplify@latest` コマンドにより、Next.jsベースのAmplifyプロジェクトが自動生成されます。

### プロジェクト構成の確認

```
my-amplify-app/
├── amplify/
│   ├── auth/
│   │   └── resource.ts
│   ├── data/
│   │   └── resource.ts
│   ├── backend.ts
│   └── tsconfig.json
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── globals.css
├── package.json
└── tsconfig.json
```

主な構造は以下の通りです。

* `amplify/` - バックエンドリソースの定義
* `app/` - フロントエンドアプリケーション
* `amplify/data/resource.ts` - データモデルの定義
* `amplify/auth/resource.ts` - 認証の設定

## データモデルの定義
Duration: 0:10:00

### スキーマの設定

`amplify/data/resource.ts` を編集して、メッセージを管理するデータモデルを定義します。

```typescript
import { type ClientSchema, a, defineData } from '@aws-amplify/backend';

const schema = a.schema({
  // メッセージボードのデータモデル
  Message: a.model({
    content: a.string().required(),
    author: a.string().required(),
    createdAt: a.datetime(),
  }).authorization(allow => [
    allow.publicApiKey(),
  ]),
});

export type Schema = ClientSchema<typeof schema>;

export const data = defineData({
  schema,
  authorizationModes: {
    defaultAuthorizationMode: 'apiKey',
    apiKeyAuthorizationMode: {
      expiresInDays: 7,
    },
  },
});
```

Positive
: `a.model()` で定義したモデルは自動的にDynamoDBテーブルとGraphQL APIが作成されます。CRUD操作も自動生成されます。

## フロントエンドの実装
Duration: 0:20:00

### メインページの編集

`app/page.tsx` を以下の内容に書き換えて、メッセージボードアプリを実装します。

```tsx
"use client";

import { useState, useEffect } from "react";
import { generateClient } from "aws-amplify/data";
import type { Schema } from "@/amplify/data/resource";
import { Amplify } from "aws-amplify";
import outputs from "@/amplify_outputs.json";

Amplify.configure(outputs);
const client = generateClient<Schema>();

export default function Home() {
  const [messages, setMessages] = useState<Schema["Message"]["type"][]>([]);
  const [content, setContent] = useState("");
  const [author, setAuthor] = useState("");

  // メッセージの一覧取得
  useEffect(() => {
    const sub = client.models.Message.observeQuery().subscribe({
      next: ({ items }) => {
        setMessages([...items].sort((a, b) =>
          (b.createdAt ?? "").localeCompare(a.createdAt ?? "")
        ));
      },
    });
    return () => sub.unsubscribe();
  }, []);

  // メッセージの送信
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!content.trim() || !author.trim()) return;

    await client.models.Message.create({
      content: content.trim(),
      author: author.trim(),
      createdAt: new Date().toISOString(),
    });

    setContent("");
  };

  // メッセージの削除
  const handleDelete = async (id: string) => {
    await client.models.Message.delete({ id });
  };

  return (
    <main className="container">
      <h1>📝 メッセージボード</h1>
      <p className="subtitle">AWS Amplify で構築した動的Webアプリ</p>

      <form onSubmit={handleSubmit} className="form">
        <input
          type="text"
          placeholder="名前を入力"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          className="input"
          required
        />
        <textarea
          placeholder="メッセージを入力"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          className="textarea"
          required
        />
        <button type="submit" className="button">
          送信
        </button>
      </form>

      <div className="messages">
        <h2>メッセージ一覧 ({messages.length}件)</h2>
        {messages.length === 0 ? (
          <p className="empty">まだメッセージがありません</p>
        ) : (
          messages.map((msg) => (
            <div key={msg.id} className="message-card">
              <div className="message-header">
                <span className="message-author">👤 {msg.author}</span>
                <span className="message-date">
                  {msg.createdAt
                    ? new Date(msg.createdAt).toLocaleString("ja-JP")
                    : ""}
                </span>
              </div>
              <p className="message-content">{msg.content}</p>
              <button
                onClick={() => handleDelete(msg.id)}
                className="delete-button"
              >
                🗑 削除
              </button>
            </div>
          ))
        )}
      </div>
    </main>
  );
}
```

### スタイルの編集

`app/globals.css` を以下の内容に書き換えます。

```css
:root {
  --bg-primary: #0f0f23;
  --bg-secondary: #1a1a3e;
  --text-primary: #e0e0ff;
  --text-secondary: #9999cc;
  --accent: #6c63ff;
  --accent-hover: #5a52d5;
  --card-bg: rgba(255, 255, 255, 0.06);
  --border: rgba(255, 255, 255, 0.1);
  --danger: #ff6b6b;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

.container {
  max-width: 720px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}

h1 {
  font-size: 2.2rem;
  text-align: center;
  margin-bottom: 0.3rem;
}

.subtitle {
  text-align: center;
  color: var(--text-secondary);
  margin-bottom: 2.5rem;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  margin-bottom: 2.5rem;
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid var(--border);
}

.input, .textarea {
  width: 100%;
  padding: 0.8rem 1rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
}

.input:focus, .textarea:focus {
  border-color: var(--accent);
}

.textarea {
  min-height: 80px;
  resize: vertical;
}

.button {
  padding: 0.8rem;
  background: var(--accent);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.button:hover {
  background: var(--accent-hover);
}

.messages h2 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
  color: var(--text-secondary);
}

.empty {
  text-align: center;
  color: var(--text-secondary);
  padding: 2rem;
}

.message-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.2rem;
  margin-bottom: 1rem;
  transition: transform 0.2s;
}

.message-card:hover {
  transform: translateY(-2px);
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.6rem;
}

.message-author {
  font-weight: 600;
  color: var(--accent);
}

.message-date {
  font-size: 0.8rem;
  color: var(--text-secondary);
}

.message-content {
  line-height: 1.6;
  margin-bottom: 0.8rem;
}

.delete-button {
  background: none;
  border: 1px solid var(--danger);
  color: var(--danger);
  padding: 0.3rem 0.8rem;
  border-radius: 6px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
}

.delete-button:hover {
  background: var(--danger);
  color: white;
}
```

## ローカルでの動作確認
Duration: 0:10:00

### Amplifyサンドボックスの起動

ローカル開発用のサンドボックス環境を起動します。

```console
npx ampx sandbox
```

Positive
: サンドボックスモードでは、バックエンドのリソースが自動的にAWS上に作成されます。コードを変更するとホットリロードされます。

別のターミナルでフロントエンドの開発サーバーを起動します。

```console
npm run dev
```

### ブラウザで確認

`http://localhost:3000` にアクセスして以下を確認します。

1. メッセージボードが表示される
2. 名前とメッセージを入力して「送信」ボタンをクリック
3. メッセージ一覧にリアルタイムで反映される
4. 「削除」ボタンでメッセージを削除できる

### サンドボックスの停止

確認が終わったら、サンドボックスを停止します。  
ターミナルで `Ctrl + C` を押して停止し、リソース削除の確認に `y` と回答します。

## GitHubリポジトリの作成とプッシュ
Duration: 0:10:00

### リポジトリの作成

1. [GitHub](https://github.com/) にログインします
2. **New repository** をクリックします

| 項目 | 値 |
|------|-----|
| Repository name | `handson-amplify-app` |
| Visibility | Private |

3. **Create repository** をクリックします

### コードのプッシュ

```console
git init
git add .
git commit -m "Initial commit: Amplify message board app"
git branch -M main
git remote add origin https://github.com/{あなたのGitHubユーザー名}/handson-amplify-app.git
git push -u origin main
```

Negative
: `{あなたのGitHubユーザー名}` は自分のGitHubユーザー名に置き換えてください。

## Amplify Hostingへのデプロイ
Duration: 0:15:00

### Amplifyコンソールでの設定

1. AWSマネジメントコンソールから **AWS Amplify** を選択します
2. **新しいアプリを作成** をクリックします
3. **GitHub** を選択して **続行** をクリックします

### GitHubとの連携

1. GitHubの認証画面が表示されるので、**Authorize** をクリックします
2. リポジトリの一覧から `handson-amplify-app` を選択します
3. ブランチとして `main` を選択します

### ビルド設定

アプリ名を確認して、ビルド設定はデフォルトのまま進めます。

| 項目 | 値 |
|------|-----|
| アプリ名 | handson-amplify-app |
| ブランチ | main |
| ビルド設定 | 自動検出（Next.js） |

4. **保存してデプロイ** をクリックします

Positive
: Amplifyがnext.jsアプリを自動検出して適切なビルド設定を構成してくれます。

### デプロイの完了を待つ

以下のステップが順番に実行されます。

1. **Provision** - インフラのプロビジョニング
2. **Build** - アプリケーションのビルド
3. **Deploy** - デプロイ
4. **Verify** - 動作確認

全てのステップが ✅ になるまで待ちます（5〜10分程度）。

## 動作確認
Duration: 0:10:00

### デプロイされたアプリの確認

デプロイ完了後、Amplifyコンソールに表示されるURLにアクセスします。

```
https://main.{ランダム文字列}.amplifyapp.com
```

以下を確認しましょう。

1. メッセージボードが正しく表示される
2. メッセージの投稿ができる
3. メッセージの削除ができる
4. リアルタイムでメッセージが反映される
5. HTTPSでアクセスできる

### CI/CDの確認

コードを変更してGitHubにプッシュすると、自動的にAmplifyでリビルド・再デプロイが行われます。

```console
# 例：ページのタイトルを変更
# app/page.tsx を任意の内容に編集
git add .
git commit -m "Update page title"
git push
```

Amplifyコンソールで自動ビルドが開始されることを確認します。

Positive
: AmplifyはGitベースのCI/CDを標準で提供しています。プッシュするだけで自動デプロイが実行されます。

## リソースの削除
Duration: 0:05:00

### Amplifyアプリの削除

1. AWSマネジメントコンソールから **AWS Amplify** を選択します
2. 作成したアプリ（`handson-amplify-app`）を選択します
3. **アプリの設定** → **全般** を選択します
4. **アプリを削除** をクリックします
5. 確認画面で「削除」と入力して **削除** をクリックします

Positive
: Amplifyアプリを削除すると、関連するバックエンドリソース（DynamoDB、AppSync、S3など）も自動的に削除されます。

### GitHubリポジトリの削除（任意）

不要であればGitHubリポジトリも削除します。

1. GitHubのリポジトリページを開きます
2. **Settings** → ページ最下部の **Delete this repository** をクリック

Negative
: リソースの削除を忘れると、意図しない料金が発生する可能性があります。必ずアプリを削除してください。

## まとめ
Duration: 0:05:00

### 学んだこと

このハンズオンでは以下のことを学びました。

* **AWS Amplify** を使ったフルスタックアプリケーションの構築
* **Amplify Data** を使ったデータモデルの定義とGraphQL APIの自動生成
* **Amplify Hosting** を使ったアプリケーションのデプロイ
* **GitHubとの連携** によるCI/CD自動化
* **サンドボックスモード** でのローカル開発
* **リアルタイムデータ同期** の実装

### 4つのハンズオンの振り返り

| # | テーマ | 使用サービス |
|---|--------|------------|
| 09 | テキストの翻訳・音声化 | Lambda, Step Functions, S3, Translate, Polly |
| 10 | 静的Webサイトホスティング | CDK, CloudFront, S3, CloudWatch |
| 11 | 動的Webアプリホスティング | Amplify |
| 12 | サーバレスAPIの構築と保護 | GAS, Lambda, API Gateway, WAF, DynamoDB |

それぞれのハンズオンで、サーバレスのユースケースと構築方法を学びました。

### 発展課題

* Amplify Authを使ってユーザー認証を追加してみましょう
* Amplify Storageを使って画像のアップロード機能を追加してみましょう
* カスタムドメインを設定してみましょう
* Amplify Functionsでカスタムバックエンドロジックを追加してみましょう

### 参考リンク

<button>
  [AWS Amplify ドキュメント](https://docs.amplify.aws/)
</button>

<button>
  [Amplify Gen 2 ガイド](https://docs.amplify.aws/gen2/)
</button>

<button>
  [Next.js ドキュメント](https://nextjs.org/docs)
</button>
