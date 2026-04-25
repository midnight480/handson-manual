# handson-manual

## descprition

This page is my hands-on Manual Docs Site.

## How to Create Docs

Use Claat by [CodeLabs - tools](https://github.com/googlecodelabs/tools).

### Install

```
> go version
go version go1.23.x darwin/amd64
>
> go install github.com/googlecodelabs/tools/claat@latest
...
export GOPATH=$HOME/Go
export PATH=$PATH:$GOPATH/bin
claat -h
claat export *.md
...
> 
```

> [!NOTE]
> Go 1.17 以降、ツールのインストールには `go get` ではなく `go install パッケージ@latest` を使用してください。

```
export GOPATH=$HOME/Go
export PATH=$PATH:$GOPATH/bin
claat -h
claat export *.md
```
## Available Manuals

- [AWS CLI 環境構築ハンズオン — CloudShell & GitHub Codespaces](00-Install-AWS-CLI-to-RPI/web/index.html)
- [oViceを使ってみよう](01-use-manual-oVice/web/index.html)
- [Gatherを使ってみよう](02-use-manual-gather/web/index.html)
- [AWS CLIを使ってEC2からAMIを作成する](03-AWS-CLI-CreateAMI/web/index.html)
- [Gatherを使ってみよう](04-use-manual-gather-other/web/index.html)
- [Cloudflare Zero Trust Client](05-Cloudflare-ZeroTrust-Client/web/index.html)
- [CloudWatch Logs Metrics](06-CloudWatch-Logs-Metrics/web/index.html)
- [SITCD Initial Setup](07-SITCD-Initial-Setup/web/index.html)
- [SITCD Resource Setup](08-SITCD-Resource-Setup/web/index.html)
- [ローカルテキストファイルの翻訳・音声化・文字起こしハンズオン](09-AWS-handson-4-beginners-saga-serverlss-001/web/index.html)
- [サーバレスで静的Webサイトをホスティングするハンズオン](10-AWS-handson-4-beginners-saga-serverlss-002/web/index.html)
- [Amplifyで動的Webアプリケーションをホスティングするハンズオン](11-AWS-handson-4-beginners-saga-serverlss-003/web/index.html)
- [サーバレスAPIの構築と保護 - GASからAPI Gateway + WAFまで](12-AWS-handson-4-beginners-saga-serverlss-004/web/index.html)
- [生成AI×GAS 業務自動化プロフェッショナル養成講座 〜異なる視点で作り上げる、次世代の業務改善バイブル〜](13-Google-Apps-Script-4-Begineers/web/index.html)
- [AWS Hands-on for Beginners: Saga O11y & Security](14-AWS-handson-4-beginners-saga-o11y/web/index.html)
- [SITCD Initial Setup - SCP, RCP, and IAM Setup via AWS CLI](99-Setup/web/index.html)
- [AWS環境構築・ポリシー設定CLIジェネレーター](99-Setup/cli-generator.html)
