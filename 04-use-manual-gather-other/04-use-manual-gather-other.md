author: Shibao,Tetsuya
summary: Desc
id: 04-use-manual-gather-other
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# Gatherを使ってみよう

## はじめに
Duration: 0:05:00

### Gatherとは

Negative
: このページは紹介しているのみなのでアカウント登録は実施しないでください！

* 機能概要 - オンラインコミュニケーションスペース
  * 2次元をアバターを移動させる
  * 音声・テキストチャット
  * 画面共有
  * カスタムマップ
  * カスタムオブジェクト（環境音,Google Meet/ZoomなどのURL）

* サイトURL
  * [公式](https://gather.town/)
  * [本社所在地](https://pitchbook.com/profiles/company/454511-26#overview)  
    547 Elm Avenue, San Bruno, CA, United States
  * [料金体系](https://gather.town/pricing)  
  ※ Free Tier Accommodates 25 Online Users!

* 通信仕様
  * [ネットワークについて](https://support.gather.town/help/data-protection-and-encryption#data-encryption)  
  一般的なWebRTCを用いて E2E(P2P)でのTCP/443によるHTTPS通信

* 適用される法律
  * [利用規約](https://gather.town/terms-of-use)  
    > United States Legal Compliance  
    ※ EUはGDPR、USのCalifornia州は独自の個人情報取得に関する法律が適用される

### 実績

* [高エネルギー加速器研究機構 - 研究会「放射線検出器とその応用」](https://www-conf.kek.jp/rdetconf/index.html)
  * [ポスター会場](https://www-conf.kek.jp/rdetconf/GatherTown.pdf)

* [株式会社アニマ](https://www.studioanima.co.jp/company/)
  * [2021.01.21 - バーチャルオフィスサービスの導入について](https://www.studioanima.co.jp/Anigon-chat/2021/01/21/post-5326/)

* [放課後モノづくり倶楽部](https://monodukuri.club/)
  * [チームでオフィスを持ちました！(Gatherにね)](https://note.com/hiroki_hachisuka/n/neeada2121807)

* [クラスメソッド株式会社](https://classmethod.jp/company/overview/)
  * [レトロRPG風デザインのオンラインビデオ通話スペース『 Gather.Town 』で”出社して仕事＆気軽に雑談”を楽しく仮想体験！](https://dev.classmethod.jp/articles/gather-town-as-a-virtual-office/)
  * [Gather.Town 有料プランの費用感について](https://dev.classmethod.jp/articles/gather-town-pricing/)
  * [Gather.Town でビデオ会議サービス(Zoom, Google Meet等)との連携を行う](https://dev.classmethod.jp/articles/gather-town-integration-with-external-call-and-zoom-call/)

## 使い方の動画
Duration: 0:10:00

### 使い方紹介動画

* Gather公式

<button>
  [YouTube - Intro to Gather](https://www.youtube.com/watch?v=89at5EvCEvk)
</button>

* 【ダナン在住エンジニア】KZY

<button>
  [YouTube - 【Gather Town】How to start Gather Town, which is the RPG like virtual office!](https://www.youtube.com/watch?v=G2tBlLADZ2A)
</button>

## 実際につかってみよう
Duration: 0:10:00

### ログインURL

* 主催者から通知されるURLを利用してください

<button>
  [今回利用するGather Space](https://gather.town/app/8KYOxHXpjMTelpx1/DINER)
</button>

Positive
: このあとログイン名を入力いただきますが、このスペースのみ有効なため、アカウント作成されるわけではないです

Negative
: ログイン時にパスワードが必要になるので主催者から通知された情報にあるパスワードを事前に確認してください

Negative
: 以降の画面はmacOS BigSur 11.3.1, Mozilla Firefox 88.0.1 (64 ビット)で取得した画面となりますが、各自の操作へ影響はないと思います。

### （共通操作）プライベートルームのパスワード

* 主催者から通知されるパスワードを入力

![privateroom](./images/0401.jpg)

### （Gatherアプリがインストールされている人のみ）拡張機能の有効

* アプリケーションとの関連付けはキャンセル

![relative](./images/0401-a.jpg)

* ブラウザで続ける

![browser](./images/0402.jpg)

### （共通操作）部屋に入るために必要な設定

* マイクとカメラの設定

![settings](./images/0403.jpg)

* （Edit Character）名前とアバターの設定

![avator](./images/0404.jpg)

変更可能な要素は次のとおりです。
  * Body
    * Skin（肌）
    * Hair（髪型）
    * Facial Hair（ひげ）
  * Clothing
    * Top（上）
    * Bottom（下）
    * Shoes（靴）
  * Accessories
    * Hat（帽子）
    * Glasses（眼鏡）
    * Other（他[マスク、松葉杖、車椅子？]）

Negative
: 予め選択可能な組み合わせの範囲内でのみ選択可能なため、オリジナルのアイテムを作成・選択することはできません

### （任意）チュートリアルのスキップ

* 接続後に表示されるチュートリアルはスキップ可能

実際にMAPに入る前にキーボードなどでの動作について説明がありますが、
スキップしてください

![tutorial](./images/0405.jpg)

## 簡単な機能説明
Duration: 0:05:00

### 入室後の画面

表示されている相手を直接呼び出すことも可能です

画面下部のバー表示が自身の名前およびツールとなります。  
左からマップ（全体のどの位置にいるか）、画面共有、アクションとなっています。

![firsttime](./images/0406.jpg)

### チャット

１：１、近く、全体にチャットを送ることが可能です

![chat](./images/0407.jpg)

### アクション

アイコンで反応を示すことが可能です（アバターの上に数秒表示されます）

![action](./images/0408.jpg)

### その他

迷子になったら初期位置に戻ることが可能です

![action](./images/0413.jpg)

## ゾーンについて

### 初期位置

右下が初期位置になります

![init](./images/0410.jpg)

### パブリックゾーン

初期はパブリックゾーンとなり、  
ここでのマイクによる発言は、  
パブリックゾーンにいる全員が聞き取れます

![public](./images/0411.jpg)

### プライベートゾーン

特定の位置に移動すると周囲が暗くなり、  
特定のゾーンのみ明るい状態になります。  
これはプライベートゾーンとなるので、  
会話はそのゾーンにいるメンバに留まります。  

![private](./images/0412.jpg)

### （おまけ）管理者から強制退出

![block](./images/0409.jpg)

Positive
: ダイレクトリンクでログインした人はブラウザタブを閉じるだけで退出扱いとなります。

Negative
: 誤ってタブを閉じたあともCookieが有効な間はユーザ名、アバターは維持されますが、DuckDuckGoのようなCookieを保存しないブラウザを使っている場合は再度登録からやり直しとなります
