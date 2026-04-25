author: Shibao,Tetsuya
summary: SITCD Initial Setup - SCP, RCP, and IAM Setup via AWS CLI
id: initial-setup
categories: codelab,markdown,aws,security
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual

# SITCD Initial Setup: AWS CLI 設定手順書

## はじめに
Duration: 0:02:00

この手順書では、AWS CLI を使用してハンズオン環境向けの初期設定（SCP、RCP、および IAM ユーザーの自動払い出し）を行う方法を解説します。
管理アカウント（Management Account）の権限を持つユーザー、または AWS CloudShell 等から実行してください。

### 前提条件
* AWS CLI がインストール・設定されていること。
* AWS Organizations の管理権限を有していること。
* ハンズオン対象のアカウントが所属する「対象の OU (Organizational Unit) ID」を確認しておくこと。（例: `ou-xxxx-yyyyyy`）

---

## 1. Organizations ポリシーの有効化
Duration: 0:03:00

Organizations で SCP および RCP を利用するためには、まず組織のルートで各ポリシータイプを有効化する必要があります。すでに有効化済みの場合はスキップして構いません。

### ルートIDの確認
```console
ROOT_ID=$(aws organizations list-roots --query 'Roots[0].Id' --output text)
echo $ROOT_ID
```

### SCP と RCP の有効化
```console
# SCP (Service Control Policy) の有効化
aws organizations enable-policy-type \
    --root-id $ROOT_ID \
    --policy-type SERVICE_CONTROL_POLICY

# RCP (Resource Control Policy) の有効化
aws organizations enable-policy-type \
    --root-id $ROOT_ID \
    --policy-type RESOURCE_CONTROL_POLICY
```

---

## 2. SCP の作成とアタッチ
Duration: 0:05:00

`SCP.json` を読み込み、AWS Organizations にポリシーを作成し、対象の OU にアタッチします。

### ポリシーの作成
※カレントディレクトリを `99-Setup/` に移動してから実行してください。

```console
SCP_POLICY_ID=$(aws organizations create-policy \
    --content file://07-SITCD-Initial-Setup/07-SCP.json \
    --description "SITCD Hands-on SCP" \
    --name "SITCD-HandsOn-SCP" \
    --type SERVICE_CONTROL_POLICY \
    --query 'Policy.PolicySummary.Id' \
    --output text)

echo "作成された SCP ID: $SCP_POLICY_ID"
```

### 対象 OU へのアタッチ
`TARGET_OU_ID` の値はご自身の環境の OU ID に変更して実行してください。

```console
TARGET_OU_ID="ou-xxxx-yyyyyy"

aws organizations attach-policy \
    --policy-id $SCP_POLICY_ID \
    --target-id $TARGET_OU_ID
```

---

## 3. RCP の作成とアタッチ
Duration: 0:05:00

同様に、`RCP.json` を読み込み、ポリシーを作成して対象 OU にアタッチします。

### ポリシーの作成
```console
RCP_POLICY_ID=$(aws organizations create-policy \
    --content file://07-SITCD-Initial-Setup/07-RCP.json \
    --description "SITCD Hands-on RCP" \
    --name "SITCD-HandsOn-RCP" \
    --type RESOURCE_CONTROL_POLICY \
    --query 'Policy.PolicySummary.Id' \
    --output text)

echo "作成された RCP ID: $RCP_POLICY_ID"
```

### 対象 OU へのアタッチ
```console
aws organizations attach-policy \
    --policy-id $RCP_POLICY_ID \
    --target-id $TARGET_OU_ID
```

---

## 4. StackSets による IAM ユーザーの展開
Duration: 0:05:00

最後に、CloudFormation StackSets を利用して、ハンズオン用の IAM ユーザー (`AdministratorAccess` 権限付き) を対象 OU 内の全アカウントに一括作成します。

### StackSet の作成
テンプレートファイル `iam-admin-user.yaml` は同じディレクトリ (`99-Setup/`) に配置されている前提です。

```console
aws cloudformation create-stack-set \
    --stack-set-name SITCD-HandsOn-IAM \
    --template-body file://iam-admin-user.yaml \
    --capabilities CAPABILITY_NAMED_IAM \
    --permission-model SERVICE_MANAGED \
    --auto-deployment Enabled=true,RetainStacksOnAccountRemoval=false \
    --parameters ParameterKey=Password,ParameterValue="TempPassword123!" \
    --description "Create hands-on IAM users via StackSets"
```

Positive
: **パスワードについて**
: `--parameters ParameterKey=Password,ParameterValue="TempPassword123!"` の箇所で初期パスワードを指定しています。必要に応じて安全な値に変更して実行してください。初回のログイン時にパスワードの再設定が要求されます。

### Stack Instance のデプロイ
対象 OU に向けてインスタンスを展開（実際の IAM ユーザーのデプロイ）を実行します。

```console
aws cloudformation create-stack-instances \
    --stack-set-name SITCD-HandsOn-IAM \
    --deployment-targets OrganizationalUnitIds=$TARGET_OU_ID \
    --regions ap-northeast-1 \
    --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=1
```

### 展開状況の確認
StackSets の展開は非同期で行われるため、以下のコマンドでステータスを確認します。

```console
# 直近のオペレーションIDを取得
OPERATION_ID=$(aws cloudformation list-stack-set-operations \
    --stack-set-name SITCD-HandsOn-IAM \
    --query 'Summaries[0].OperationId' \
    --output text)

# ステータスの確認
aws cloudformation describe-stack-set-operation \
    --stack-set-name SITCD-HandsOn-IAM \
    --operation-id $OPERATION_ID \
    --query 'StackSetOperation.Status' \
    --output text
```

`SUCCEEDED` と表示されれば、OU 配下の各アカウントでの IAM ユーザー作成は完了です！

---

## おわりに
Duration: 0:01:00

以上で、SCP・RCP によるアカウントの安全なガードレール設定と、ハンズオン用ユーザーの払い出しがすべて完了しました。

受講者は各アカウントにログインし、作成された `handson-admin` ユーザー（および初期パスワード）を用いてコンソールに入り、ハンズオンを開始できます。隔離された安全な環境で学習を進めてください！
