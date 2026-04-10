author: Shibao,Tetsuya
summary: 生成AI×GAS 業務自動化プロフェッショナル養成講座 〜異なる視点で作り上げる、次世代の業務改善バイブル〜
id: 13-google-apps-script-4-begineers
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/midnight480/handson-manual
analytics account: 196534296

# 生成AI×GAS 業務自動化プロフェッショナル養成講座 〜異なる視点で作り上げる、次世代の業務改善バイブル〜

## 【序章】本プロジェクトの進め方
Duration: 0:05:00

この講座は、単にGAS（Google Apps Script）の構文を暗記するためのものではありません。**「生成AIという強力な相棒と共に、目の前の面倒な業務をどう自動化していくか」**を実践的に学ぶためのバイブルです。

### 3つの役割（視点）
この教科書は、読者のみなさんが以下のいずれかの視点を持って取り組むことで、より生きた知識となります。
* **【学ぶ人（ビギナー）】**: 「どこが難しいか」を言葉にして、業務の課題を見つける。
* **【動かす人（チャレンジャー）】**: AIの力を借りてとにかく「動くコード」を試し、エラーと向き合う。
* **【伝える人（メンター）】**: 学んだ内容を実際の業務プロセスにどう当てはめるかを考え、周囲に広める。

### GitHubを活用したポートフォリオ・履歴管理
学習成果をただの「練習」で終わらせず、あなたの「実績」として形に残すために、プロのエンジニアが利用する「GitHub」というサービスを使用します。

* **GitHubとは？**: エンジニア向けの「ソースコード専用のGoogleドライブ」または「履歴書」のようなプラットフォームです。
* **なぜ使うのか？**: コードの変更履歴がすべて残り、自分がどれだけ学習し、どんなツールを作れるようになったかを、世界中（あるいは転職・評価の場）で客観的に証明できるからです。

初心者の方は、最初は特別なツールを使わずにWebブラウザ上でコードを管理するだけで問題ありません。後半の章では、プロのエンジニアが開発現場で実際に使用している「clasp（クラスプ）」というツールを用いた手元のパソコンでの本格的なソースコード管理や、「TypeScript」を用いた高度な開発手法へのステップアップも用意しています。

Positive
: 非エンジニアの方も安心してください！まずは誰でもできる「画面のクリック」や「コピー＆ペースト」で動く体験を積むことから始めます。焦らず、ご自身のペースで確実に進めていきましょう。

## 第1章 仕事を楽にしたっていい
Duration: 0:15:00

この章では、プログラミングや自動化に対する「マインドセット（心の持ち方）」と、ハンズオンの準備を行います。

### 01-01 無駄な仕事が多いと気づいてしまった
日々の業務で「PDFの内容を手作業でExcelに転記している」「毎日決まった時間に同じ文面のメールを送っている」「複数のシステムに同じ顧客データを二重入力している」といった経験はありませんか？
「これ、毎日同じ作業の繰り返しだな」と感じるその違和感こそが、業務改善の第一歩です。無駄な仕事に気づく目を持つことが、自動化エンジニアとしての最初の才能です。

### 01-02 自分でやる必要のない仕事は、誰かに任せよう
ルーティンワークは人ではなく、コンピューター（プログラム）に任せる時代です。
人間がやるべき仕事は「考えること」「企画すること」「顧客とコミュニケーションを取ること」です。データをコピーして貼り付けるだけの単純作業は、遠慮なく自動化システムに丸投げしてしまいましょう。仕事を楽にすることは、決して「手抜き」ではなく、より価値の高い業務へ時間を投資するための「戦略」です。

### 01-03 目の前の業務を自動化してくれるヒーローはこない
「いつか会社が便利なシステムを導入してくれるだろう」「誰かITに詳しい人がなんとかしてくれるはず」と待っていても、あなたの目の前にある特定の面倒な作業をピンポイントで解決してくれるヒーローは、残念ながら永遠に現れません。
だからこそ、最前線で業務を行う「あなた自身」が課題を解決する手段を持つ必要があるのです。

### 01-04 誰でも仕事を自動化する側になれる
「でも、プログラミングなんてしたことがない」と不安になる必要はありません。
現在はChatGPTやClaudeなどの「生成AI」が強力なコード作成アシスタントとして存在しています。あなたが「どのような業務を」「どう改善したいか」という業務知識を持っていれば、プログラミング言語の細かな文法は生成AIが補ってくれます。誰もが思いつきを形にできる、素晴らしい時代が到来しているのです。

### 01-05 そろばん → 電卓 → Excel の次に進もう
かつて、計算の主流はそろばんでした。それが電卓になり、Excelという表計算ソフトへと進化しました。道具は常に進化しています。Excelのピボットテーブルやマクロ（VBA）に留まることなく、次はWeb上でシームレスに連携する「クラウド」と「GASによる自動化」という新しい道具を使いこなすステップへ進みましょう。

### 01-06 一歩を踏み出すかどうかで、未来は変わる
知識として知っていることと、実際に手を動かして「システムが勝手に動く感動」を味わうことには雲泥の差があります。失敗してもパソコンが壊れることはありません。まずは以下の準備から始めて、未来を変える第一歩を踏み出しましょう。

### 01-07 Googleドライブを準備する
GASを動かす土台となる「Googleドライブ」を開きます。
1. Googleアカウントにログインした状態でブラウザを開きます。
2. 画面右上の点々マーク（Googleアプリ）から「ドライブ」を選択します。
3. 今回の講座用のファイルをまとめるために、左上の「+ 新規」ボタンから「新しいフォルダ」を作成し、名前を `GAS業務改善` としておきましょう。

### 01-08 Google スプレッドシートを準備する
作成したフォルダの中に、作業用のスプレッドシートを用意します。
1. `GAS業務改善` フォルダを開きます。
2. 画面の空白の場所で右クリック（または左上の「+ 新規」ボタン）し、「Google スプレッドシート」>「空白のスプレッドシート」を選択します。
3. シートが新しく開いたら、画面左上の「無題のスプレッドシート」という文字をクリックし、ファイル名を `自動化の第一歩` に変更してください。

### 演習問題 1
作成したGoogleスプレッドシート（`自動化の第一歩`）を開き、シート1の `A1` セルに「私の自動化宣言：〇〇の業務をなくす！」と、あなたの無くしたい業務を一つ書き込んでみてください。

---

### Tips 1: 身の回りの「面倒くさい」をメモする習慣
自動化のネタは日常にたくさん転がっています。「データを探すのが面倒だな」「毎週この報告ウザいな」と心が動いた瞬間に、手元のメモ帳やチャットツールの自分宛の部屋に書き留める習慣をつけましょう。不満の数だけ、あなたが活躍できる自動化のチャンスがあります！

---

## 第2章 Excelを超えるパワフルな世界 - SpreadSheet -
Duration: 0:20:00

GASによるプログラミングに入る前に、Googleスプレッドシート単体が持つ「魔法のような関数」をマスターします。実は、GASを書かなくても関数だけで解決する業務改善は山のようにあります。

### 02-01 「表計算ソフトと言えば Excel」からの脱却
Googleスプレッドシートは単なるWeb版Excelではありません。複数人の同時編集、自動保存、バージョン履歴の復元は当然のこととして、クラウドにあるからこそ可能な「他のファイルやWebサイトとの連携機能」が最大の強みです。

### 02-02 社員一覧・顧客一覧など、いつも同じデータをコピペ。もっと楽な方法はない？
Aというファイルにある名簿を、Bのファイルに手作業でコピペしていませんか？
`IMPORTRANGE` 関数を使えば、別のファイルのデータをリアルタイムに同期できます。元データが更新されれば、あなたのシートも勝手に更新されます。

**構文例**:
```text
=IMPORTRANGE("スプレッドシートのURL", "シート1!A1:D100")
```
※初回の読み込み時に「アクセスを許可」というボタンが出るので、それをクリックするだけで同期が始まります。

### 02-03 データが追加されるたびに、数式をコピーするのがめんどくさい。よい方法は？
行を追加するたびに、上の行から数式をドラッグしてコピーするのは危険で手間な作業です。
`ARRAYFORMULA`（アレイフォーミュラ）関数を使えば、1つのセルに数式を書くだけで、指定した列全体に対して一気に計算を適用できます。

**構文例**（A列とB列を掛け算してC列に表示する場合、C1セルに記入）:
```text
=ARRAYFORMULA(A1:A100 * B1:B100)
```

### 02-04 売上データから条件にあてはまるデータだけとりだすには？
オートフィルタで絞り込んでコピペしていませんか？
`FILTER` 関数を活用すると、条件に合致するデータだけを美しく別の場所に抽出（リアルタイム更新）できます。

**構文例**（A列からC列のデータのうち、B列が「完了」となっている行だけを抜き出す）:
```text
=FILTER(A:C, B:B = "完了")
```
さらに高度なSQLのようなデータ抽出をしたい場合は、 `QUERY`（クエリ）関数が強力な武器になります。

### 02-05 名前から苗字だけ抜き出したい。文字列の一部だけ抜き出すには？
`REGEXEXTRACT` などの関数を使うと、「正規表現」という文字検索のルールを用いて、複雑なテキストから必要な部分だけをピンポイントで抜き出すことができます。

**構文例**（A1セルの「山田 太郎」からスペース前の「山田」だけ抜き出す）:
```text
=REGEXEXTRACT(A1, "^(.+) ")
```

### 02-06 ウェブの情報をスプレッドシートにまとめたい。簡単にデータを集めるには？
手作業でのスクレイピング（情報収集）はもう不要です。
`IMPORTXML` や `IMPORTHTML` 関数を使うと、Webサイトの表データや特定のテキストをダイレクトにシートへ表示させることができます。競合他社の価格調査などに威力を発揮します。

### 演習問題 2
ご自身のスプレッドシートで以下の作業を行ってください。
1. A列の1行目〜5行目に「100, 200, 300, 400, 500」と入力します。
2. B1セルに `=ARRAYFORMULA(A1:A5 * 1.1)` と入力し、B列全体に消費税（10%）込みの金額（110, 220, 330...）が自動的に展開される体験をしてください。

---

### Tips 2: スプレッドシート関数とGASの使い分け
「これって関数でやるべき？GASでやるべき？」と迷うことがあります。
原則として、**「シート内部での計算、データの表示形式の変更、抽出」はシートの関数（ARRAYFORMULAやFILTER）**を使い、**「メールの送信、PDF出力、外部API連携、データの定期的な一括削除処理」など動きを伴う処理はGAS**を使う、という棲み分けがベストプラクティスです。

---

## 第3章 あらゆる業務の効率化を実現する Google Apps Script
Duration: 0:40:00

いよいよGAS（Google Apps Script）を用いて、アプリケーションを自動で動かすプログラミングの世界に入ります。

### 03-01 さあ、可能性を広げよう
スプレッドシート関数の範囲を超え、ここからは「Googleのサービスを自由自在に操る魔法の杖」であるGASを手に入れます。

### 03-02 業務効率化の新常識 Google Apps Script
GASは、Google社が提供しているJavaScriptベースのプログラミング言語です。Gmail、Googleカレンダー、Googleドライブ、Googleドキュメントなど、Workspace上のさまざまなサービスを連携・操作することができます。

### 03-03 革命的なハードルの低さが魅力
プログラミングを始める際、通常は黒い画面（ターミナル）を開き、開発用のソフトをインストールするなど「環境構築」と呼ばれる高い壁があります。
しかしGASは、Webブラウザ（Chromeなど）とGoogleアカウントさえあれば、今すぐ、この10秒後から開発をスタートできます。

### 03-04 じぶんだけのアシスタントを手にいれる
GASのスクリプトはクラウド上（Googleのサーバー上）で実行されます。これはつまり、あなたのパソコンの電源が切れていても、プログラムは文句を言わずに24時間365日働き続けてくれるということです。

### 03-05 はじめの一歩をふみ出そう
実際にエディタ（コードを書く画面）を開いてみましょう。
1. 第1章で作成したスプレッドシートを開きます。
2. 上部のメニューバーから **「拡張機能」** ＞ **「Apps Script」** をクリックします。
3. 新しいタブが開き、`function myFunction() { ... }` と書かれたエディタ画面が表示されたら準備完了です！

### 03-06 スプレッドシート関数と構造は同じ
プログラミング言語といっても恐れることはありません。
シートの関数が `=SUM(A1:A10)` のように「何をするか（SUM）」と「対象（引数: A1:A10）」で構成されるのと同じく、GASも `SpreadsheetApp.getActiveSpreadsheet()` のように「対象を操作する命令をドット（.）で繋いでいく」というルールに基づいています。

### 03-07 実践-1 日次報告メールの下書きを毎日自動で生成しよう
まずはコードをコピー＆ペーストして、実際に動かしてみましょう。
エディタ上に最初から記載されている文字をすべて消して、以下のコードを貼り付けてください。

```javascript
function createDraftEmail() {
  // ① 宛先や件名、本文を変数に用意する
  const recipient = "manager@example.com";
  const subject = "【日次報告】本日の業務進捗";
  const body = "お疲れ様です。\n本日の日報を報告いたします。\n\n・タスクA：完了\n・タスクB：進行中\n\nよろしくお願いいたします。";
  
  // ② Gmailのサービスを呼び出し、下書きを作成する機能(createDraft)を実行する
  GmailApp.createDraft(recipient, subject, body);
}
```

貼り付けたら、フロッピーディスクのアイコン（またはCtrl+S / Cmd+S）で保存し、上部の**「実行」**ボタンをクリックします。

Negative
: 【重要】初回実行時には「承認が必要です」というポップアップが出ます。「権限を確認」→「自身のアカウントを選択」→「詳細」→最下部の「（安全ではないページに）移動」→「許可」をクリックしてください。これは自分自身のプログラムにGmail操作の許可を与える標準的なセキュリティの仕組みです。

実行完了後、ご自身のGmailの「下書き」フォルダを確認してみてください。自動的にメールが作成されているはずです！

### 03-08 実践-2 週次ミーティングの報告シートをコピーしよう
「テンプレートとなるシート」を毎週手でコピーしていませんか？これも自動化できます。
スプレッドシートに「テンプレート」という名前のシートを作成してから、以下のコードを実行してください。

```javascript
function copyWeeklySheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const templateSheet = ss.getSheetByName("テンプレート"); // 対象シートを名前で取得
  
  // Utilitiesを使って今日の日付を 20260410 のような文字列へ変換
  const today = Utilities.formatDate(new Date(), "JST", "yyyyMMdd");
  
  // テンプレートシートをコピーし、名前を変更する
  templateSheet.copyTo(ss).setName(today + "_週次報告");
}
```

### 03-09 実践-3 ストレスフリーなタスク管理を実現しよう
GASを使えば見た目の制御も可能です。たとえば、スプレッドシートのチェックボックスを判定して、終わったタスクの行の背景色をグレーにし、取り消し線を引くこともできます。これらを組み合わせれば、高額なタスク管理ツールを契約しなくても、自社専用の使いやすいツールを自作できます。

```javascript
function formatCompletedTasks() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  // 2行目から100行目までのデータを取得（A列がチェックボックスと仮定）
  const range = sheet.getRange("A2:C100"); 
  const values = range.getValues();
  
  values.forEach((row, index) => {
    const isChecked = row[0]; // A列の値（true / false）
    const targetRow = sheet.getRange(index + 2, 1, 1, 3); // 該当する行のA〜C列
    
    if (isChecked === true) {
      targetRow.setBackground("#f0f0f0"); // 背景をグレーに
      targetRow.setFontLine("line-through"); // 取り消し線を引く
    } else {
      targetRow.setBackground("#ffffff"); // 背景を白に戻す
      targetRow.setFontLine("none"); // 取り消し線を消す
    }
  });
}
```

### 演習問題 3
「実践-1」のコードを修正し、`body`（メール本文）の末尾に、ご自身の「明日の目標：〇〇」という一文が追記された下書きを作成するようにコードを書き換えて実行してください。（文字の繋がりや改行 `\n` に注意しましょう）

---

### Tips 3: 生成AI（ChatGPTなど）をGASの先生にする
「特定のセルの色を変えるGASの書き方がわからない…」と悩んだら、Google検索で何時間も悩むのではなく、生成AIに相談しましょう。
**プロンプトの例**:
「Google Apps Scriptのコードを書いてください。現在のスプレッドシートの、シート名『TODO』の、A列にチェックボックス（TRUE）が入っている行について、その行の背景色をグレー（#f0f0f0）に変更したいです。」
生成AIを横に置きながら、コードを生成してもらい、コピペして微調整していくのが現代の最強の開発スタイルです。

---

## 第4章 自動化でさらなるレベルアップ
Duration: 0:40:00

プログラムの「動かし方」がわかったところで、次は複数のアプリを連携させ、より高度な業務改善システムへと進化させます。

### 04-01 事務職からのピボット
GASの力を身につけたあなたは、もう単なる「手作業をこなす作業者」ではありません。これからは、チーム全体の生産性を飛躍させる「業務プロセスの構築者（Developer）」としてキャリアを広げることができます。

### 04-02 実践-4 フォームとカレンダーの連携でイベント運営の工数削減
「Googleフォームから申し込みが入ったら、カレンダーに自動で予定を登録し、申込者にありがとうメールを自動送信する」。
これはGASの超定番の連携です。フォームの送信という「イベント」をきっかけに動くシステムは、24時間無人受付システムを構築するのと同じ効果を生みます。

```javascript
// Googleフォームの「送信時」トリガーに設定する関数
function onFormSubmitCreateEvent(e) {
  // 送信されたフォームの回答データ（配列）を取得
  const responses = e.values; 
  const title = responses[1] + "様 面談設定"; // 2番目の質問（名前）を利用
  const dateStr = responses[2]; // 3番目の質問（希望日時 例:"2026/04/15 10:00"）を利用
  
  // 文字列の日付をプログラムで扱えるDate型に変換
  const startTime = new Date(dateStr);
  const endTime = new Date(startTime.getTime() + 60 * 60 * 1000); // 1時間後に設定
  
  // デフォルトのカレンダーに予定を追加
  CalendarApp.getDefaultCalendar().createEvent(title, startTime, endTime);
}
```

### 04-03 実践-5 スライド報告資料を自動生成しよう
毎月のプレゼン資料、数字だけ書き換えていませんか？
GASを使えば、スプレッドシートにまとめた売上データを読み取り、Googleスライドの指定したテキスト枠やグラフへ自動的にデータを流し込み、完成した資料（PDF）のURLを関係者にメールすることまでワンクリックで完了します。

```javascript
// スプレッドシートの数値をスライドへ反映する
function updateSlideReport() {
  const ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const salesTotal = ss.getRange("B2").getValue(); // シートのB2セルから売上を取得
  
  // 対象のGoogleスライドをIDで指定して開く
  const presentation = SlidesApp.openById("あなたのスライドIDを指定してください");
  const slide = presentation.getSlides()[0]; // 1枚目のスライドを取得
  
  // スライド内の "{{SALES}}" という文字列を、実際の売上数値に一括置換する
  slide.replaceAllText("{{SALES}}", salesTotal + " 円");
}
```

### 04-04 実践-6 スプレッドシートの更新通知で情報キャッチをスムーズに
シートが誰かによって編集された瞬間に、自動的にSlackやChatwork、Google Chatに「〇〇行目が更新されました」と通知を飛ばすことができます。これにより「シート更新しました」という報告チャットの手間自体を抹殺できます。

```javascript
// スプレッドシートの「編集時」トリガーに設定する関数
function onEditTrigger(e) {
  const sheet = e.source.getActiveSheet();
  const row = e.range.getRow();
  const col = e.range.getColumn();
  const value = e.value;
  
  // A列（カラム番号1）が編集された時だけ通知する条件
  if (col === 1) {
    const message = sheet.getName() + "の " + row + "行目が更新されました。\n入力内容: " + value;
    // 今回は画面右下のポップアップ（トースト通知）で代用します
    // ※ 実際にSlackなどに送る場合は5章で紹介するUrlFetchAppを使います
    SpreadsheetApp.getActiveSpreadsheet().toast(message, "更新通知");
  }
}
```

### 04-05 実践-7 カレンダー連携で勤務報告を効率化 繰り返し処理 forEach
月報を書くときに見ている自分のカレンダー予定を、一瞬でスプレッドシートに書き出すスクリプトです。ここではプログラミングの基本である「繰り返し処理 (`forEach`)」を使用しています。複数のデータを順番に取り出して処理する感覚を掴みましょう。

```javascript
function getCalendarEvents() {
  const now = new Date();
  // 今日から1週間後までの時間を計算
  const oneWeekLater = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000);
  
  // 指定期間のイベント（予定）をすべて取得し、配列(リスト)で保存
  const events = CalendarApp.getDefaultCalendar().getEvents(now, oneWeekLater);
  
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  // eventsの中から1つずつ予定(event)を取り出し、シートの各行へ書き込んでいく
  events.forEach((event, index) => {
    // indexは0から始まる通し番号。2行目から書き込むため index + 2 とする
    sheet.getRange(index + 2, 1).setValue(event.getTitle());     // A列：予定タイトル
    sheet.getRange(index + 2, 2).setValue(event.getStartTime()); // B列：開始時間
  });
}
```

### 04-06 わくわくする未来を実現しよう
単一のアプリ操作から、「アプリ間をつなぐハブ」としてのGASへ。これらを駆使すれば、「名刺をスキャンしたら、ドライブに保存され、シートに情報が整理され、サンクスメールが送信される」など、アイデア次第で思い描いた未来の働き方を実現できます。

### 演習問題 4
「実践-7」のカレンダー予定取得コードに機能を少し追加してください。
`forEach` の処理ブロックの中にコードを1行追加し、スプレッドシートのC列（3列目）に、カレンダーイベントの「終了時間（ `event.getEndTime()` で取得可能）」が書き出されるように変更して実行してください。

---

### Tips 4: トリガーを活用して「完全自動化」を達成しよう
今までのようにエディタを開いて手動で「実行」ボタンを押していては半自動です。
GASエディタ左側にある「時計のマーク」をクリックすると「トリガー（引き金）」の設定画面が開きます。ここで「毎日朝9時に実行する」や「スプレッドシートが編集された時に実行する」と設定するだけで、人間が関与しなくても勝手に動く「完全自動化」を達成できます。

---

## 第5章 さらなるアドバンステクニックの『紹介』
Duration: 0:40:00

ここからは、趣味の効率化を脱却し、より高度で、より壊れにくく、よりチーム・企業に貢献していくためのプロフェッショナルな技術（アドバンステクニック）を紹介します。

### 05-01 業務を変革するようなアイデアを実現するために
複雑なシステムを作る場合、ただ動くだけのコードから、「エラーに強い堅牢な設計」「セキュリティの考慮」「他者との連携開発（バージョン管理）」が必須になってきます。

### 05-02 『WebAPI』を使って、『ChatGPT』『Slack』などの外部ツールと連携する
Googleのサービス内だけでなく、外部のアプリケーションと通信する技術が `UrlFetchApp`（WebAPIの使用）です。
**例**: ChatGPTのAPIをGASから呼び出し、シート上の顧客からの問い合わせテキストを解析させ、自動でAIに返信文面を下書きさせる、といった夢の連携もこの機能で実現します。

```javascript
// UrlFetchAppを使ってSlackにメッセージを投稿する基本コード例
function sendMessageToSlack() {
  const webhookUrl = "https://hooks.slack.com/services/XXXXXX/XXXXXX/XXXXXX";
  
  // 送信するメッセージのデータ部分
  const payload = {
    "text": "GASからSlackへ自動通知のテストです！"
  };
  
  // 通信のルール（POST送信、JSON対応）を定義
  const options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload)
  };
  
  // 外部APIへHTTPリクエストを送信
  UrlFetchApp.fetch(webhookUrl, options);
}
```

### 05-03 ミスなく安心安全に自動化するために
外部サービスが落ちている時など、予期せぬエラーは必ず起きます。
プログラムに `try...catch` 文を記述することで、「もしエラーが起きてもプログラム全体をクラッシュさせずに、管理者へメールでエラー内容を通知する」といった安全なエラーハンドリング（代替処理）が可能となります。

```javascript
// エラーでシステムが止まらないためのフェイルセーフ設計
function safeExecution() {
  try {
    // 成功させたいメイン処理
    const calculation = 100 * 50; 
    
    // エラーを起こすテスト（存在しないメソッドを呼び出す）
    SpreadsheetApp.getNonExistentMethod();
    
  } catch (error) {
    // 上のtryブロック内でエラーが起きた場合、プログラムがクラッシュせずにここへ避難してくる
    console.error("エラーが発生しました: " + error.message);
    
    // 【ベストプラクティス】エラー内容を管理者のGmailへひっそりと通知する
    // GmailApp.sendEmail("admin@example.com", "GASエラー通知", "エラー内容: " + error.stack);
  } finally {
    // 成功・失敗に関わらず、最後に必ず実行したい処理を書く
    console.log("一連の処理を安全に終了しました。");
  }
}
```

### 05-04 組織にとって価値ある資産にするために
あなたが異動・退職した後にそのプログラムが動かなくなる「属人化」を防ぐ必要があります。
「変数名にわかりやすい英語（名詞や動詞）を使う」「複雑なロジックの上には日本語でコメントを残す」など、後継者（未来の自分や同僚）が読み解ける『ドキュメント（コードとしての運用保守性）』を常に意識しましょう。

### 05-05 よくあるエラーと解消方法
* **"Exceeded maximum execution time"（実行時間超過）**: GASは1回の処理につき原則「6分間」しか実行できないというルールがあります。大量のデータ処理は、数回に分けて処理するバッチ設計など工夫が必要です。
* **"Permission denied"（権限不足）**: スクリプトが触ろうとしているシートやAPIの権限付与に不備があります。もう一度承認プロセス（OAuth）を確認してください。

### 05-06 データをわかりやすく表現するなら『Looker Studio』
GASで自動収集・整理したデータをより活かすため、Googleが提供するBIツール「Looker Studio」と連携しましょう。スプレッドシートをデータ元（データベース）とし、経営層やチームがパッと見て直感で理解できる美しいダッシュボードが一瞬で作成可能です。

### 05-07 未経験独学の壁を乗り越えて：clasp と TypeScript の扉
さらなる高みを目指す方は「clasp（クラスプ）」と「TypeScript」の導入をおすすめします。
* **clasp**: PCのローカル環境（手元のパソコン）からGoogleのクラウド上のGASプロジェクトへコードを直接アップロード・ダウンロードするツールです。Webエディタから脱却し、VSCodeなどの強力なエディタを使えるほか、本プロジェクトの目的でもある**「GitHubへのソースコード連携」が圧倒的に容易**になります。
* **TypeScript**: Googleや世界のトップ企業が採用している強力なプログラミング言語です。最大のメリットは「型」の存在により、実行する前にエディタ上で「ここのコード、文字じゃなくて数字が入る場所ですよ！」とミスを教えてくれることです。claspを使うと、手元で書いたTypeScriptファイル（.ts）は、クラウドに自動でGAS用のJavaScriptに変換（トランスパイル）されてアップロードされます。

### 05-08 新たな潮流：Google Workspace CLI
さらなる最新動向として、Google公式から提供されている**Google Workspace CLI**（[https://github.com/googleworkspace/cli](https://github.com/googleworkspace/cli)）にも注目です。
GASのコード管理に特化した「clasp」とは異なり、こちらはターミナル（コマンドライン）から直接Gmailの送信やカレンダーの検索、Googleドライブのファイル管理など、あらゆるWorkspaceの機能をスクリプトを書かずとも直接操作することができます。
今後エンジニアリングを深めていく中で、自動化の引き出しの一つとして知っておくと非常に強力な武器となるはずです。

### 演習問題 5（中・上級者向けの高度な演習）
1. Node.jsがインストールされているローカルパソコンのターミナル（黒い画面）を開き、`npm install -g @google/clasp` を実行しclaspをインストールしてください。
2. `clasp login` を実行してGoogleアカウントとPCを連携します。
3. 既存のGASプロジェクトのスクリプトIDを確認し、`clasp clone [スクリプトID]` を実行してプロジェクトを手元（ローカル）にダウンロードしてください。
4. ダウンロードされた `.js` ファイルの拡張子を `.ts` に変更し、TypeScriptの構文（型定義など）を少し追加して編集した後、`clasp push` を実行し、クラウド上のGASへ反映される動作確認を完了させてください。

Positive
: TypeScriptの導入やターミナルの操作は、初学者にとって最初は魔法の呪文のようで壁に感じるかもしれません。しかし、今は生成AIという強力な24時間対応の家庭教師がプロンプト一つで教えてくれます。エラーのない安全でプロフェッショナルなシステムを目指し、ぜひ勇気を持って一歩踏み出してみてください！

## おわりに
Duration: 0:02:00

お疲れ様でした！このバイブルは、皆さんが業務課題にぶつかり、「わからない」と悩み、「こうしたら動いた！」という現場の発見の数だけ、皆さんと共にどんどん進化し分厚い教科書になっていくことでしょう。
ここで学んだ知識と、GitHubに一つ一つ積み上げたコードは「実績（自動化ポートフォリオ）」として、あなたの今後のキャリアを強力に支える武器となるはずです。

さあ、AIを相棒に、よりラクで、よりクリエイティブな「未来の働き方」を手に入れに行きましょう！

## 補講：演習問題の解答例

### 演習問題 1 の解答例
A1セルを選択し、「私の自動化宣言：〇〇の業務をなくす！」と入力できていれば正解です。
（※GASのコードではなく、あくまでスプレッドシートの操作と自動化への意識づけとなります）

### 演習問題 2 の解答例
B1セルに以下を入力します。
```text
=ARRAYFORMULA(A1:A5 * 1.1)
```

### 演習問題 3 の解答例
`body`（メール本文）の変数定義部分を以下のように修正できていれば正解です。（改行文字 `\n` が適切に入っているかがポイントです）

```javascript
function createDraftEmail() {
  const recipient = "manager@example.com";
  const subject = "【日次報告】本日の業務進捗";
  
  // 本文の最後に改行(\n)と明日の目標を追加
  const body = "お疲れ様です。\n本日の日報を報告いたします。\n\n・タスクA：完了\n・タスクB：進行中\n\n明日の目標：〇〇\n\nよろしくお願いいたします。";
  
  GmailApp.createDraft(recipient, subject, body);
}
```

### 演習問題 4 の解答例
`sheet.getRange(index + 2, 3).setValue(event.getEndTime());` という1行が、`forEach` ブロックの中に追加されていれば正解です。

```javascript
function getCalendarEvents() {
  const now = new Date();
  const oneWeekLater = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000);
  
  const events = CalendarApp.getDefaultCalendar().getEvents(now, oneWeekLater);
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  events.forEach((event, index) => {
    sheet.getRange(index + 2, 1).setValue(event.getTitle());     // A列：予定タイトル
    sheet.getRange(index + 2, 2).setValue(event.getStartTime()); // B列：開始時間
    // 以下の1行を追加：C列（3列目）に終了時間をセット
    sheet.getRange(index + 2, 3).setValue(event.getEndTime());   
  });
}
```

### 演習問題 5 の解答例
こちらはGASではなく、手元のパソコン（ターミナル）で実行するコマンド群です。以下のように順番に打てていれば正解です。

```bash
# 1. claspのインストール
npm install -g @google/clasp

# 2. Googleアカウントでのログイン（ブラウザが開きます）
clasp login

# 3. プロジェクトのクローン（実際のスクリプトIDに置き換えます）
clasp clone 1a2B3c4D5e...（実際のID）...VwXyZ

# 4. TypeScriptなどに拡張子を変更・編集後、クラウドへプッシュ
clasp push
```

---

## 補講：実践コードの全量まとめ

各章で登場した実践コードの全体版です。コピー＆ペーストしてそのまま使えます。

### 実践-1 の全体コード：日次報告メールの下書き自動生成

```javascript
function createDraftEmail() {
  // 宛先・件名・本文を定義する
  const recipient = "manager@example.com";
  const subject = "【日次報告】本日の業務進捗";
  const body =
    "お疲れ様です。\n" +
    "本日の日報を報告いたします。\n\n" +
    "・タスクA：完了\n" +
    "・タスクB：進行中\n\n" +
    "よろしくお願いいたします。";

  // Gmailに下書きとして保存する
  GmailApp.createDraft(recipient, subject, body);
}
```

### 実践-2 の全体コード：週次ミーティングの報告シートをコピー

```javascript
function copyWeeklySheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // 「テンプレート」という名前のシートを取得する（事前に作成が必要）
  const templateSheet = ss.getSheetByName("テンプレート");
  if (!templateSheet) {
    SpreadsheetApp.getUi().alert("「テンプレート」シートが見つかりません。先に作成してください。");
    return;
  }

  // 今日の日付を「20260410」形式の文字列に変換する
  const today = Utilities.formatDate(new Date(), "JST", "yyyyMMdd");

  // テンプレートをコピーして、新しいシート名を設定する
  templateSheet.copyTo(ss).setName(today + "_週次報告");
  SpreadsheetApp.getActiveSpreadsheet().toast("シートをコピーしました：" + today + "_週次報告");
}
```

### 実践-3 の全体コード：チェックボックスで完了タスクを自動フォーマット

```javascript
function formatCompletedTasks() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // A列（チェックボックス）・B列（タスク名）・C列（担当者）が入っている前提
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return; // データが2行目以降にない場合は何もしない

  const values = sheet.getRange(2, 1, lastRow - 1, 3).getValues();

  values.forEach((row, index) => {
    const isChecked = row[0]; // A列：チェックボックスの値（true / false）
    const targetRow = sheet.getRange(index + 2, 1, 1, 3); // 該当する行のA〜C列

    if (isChecked === true) {
      targetRow.setBackground("#f0f0f0"); // 背景をグレーに
      targetRow.setFontLine("line-through"); // 取り消し線を引く
    } else {
      targetRow.setBackground("#ffffff"); // 背景を白に戻す
      targetRow.setFontLine("none"); // 取り消し線を消す
    }
  });
}
```

### 実践-4 の全体コード：Googleフォーム送信時にカレンダーへ予定を自動登録

```javascript
// ※この関数は、Googleフォームに紐づくスプレッドシートの「送信時」トリガーに設定して使います
function onFormSubmitCreateEvent(e) {
  // フォームの回答値を配列で取得（e.valuesはフォームに並んでいる質問の順番通り）
  const responses = e.values;
  // responses[0] はタイムスタンプ（自動）
  const applicantName = responses[1]; // 質問1：申込者名
  const dateStr = responses[2];       // 質問2：希望日時（例: "2026/04/15 10:00"）

  // 日時文字列をDate型オブジェクトに変換する
  const startTime = new Date(dateStr);
  const endTime = new Date(startTime.getTime() + 60 * 60 * 1000); // 開始から1時間後

  // カレンダーに予定を追加する
  const title = applicantName + " 様 面談";
  CalendarApp.getDefaultCalendar().createEvent(title, startTime, endTime);

  // 申込者へ確認メールを送信する
  GmailApp.sendEmail(
    e.namedValues["メールアドレス"][0], // フォームの「メールアドレス」質問の回答
    "【受付完了】面談のご予約ありがとうございます",
    applicantName + " 様\n\nご予約を受け付けました。\n日時：" + dateStr + "\nよろしくお願いいたします。"
  );
}
```

### 実践-5 の全体コード：スプレッドシートの数値をGoogleスライドへ自動反映

```javascript
function updateSlideReport() {
  // スプレッドシートからデータを取得する
  const ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const salesTotal = ss.getRange("B2").getValue(); // B2セルの売上合計
  const reportMonth = ss.getRange("A1").getValue(); // A1セルの対象月（例：2026年4月）

  // 対象のGoogleスライドをIDで指定して取得する（URLの /d/ 以降の文字列がID）
  const SLIDE_ID = "ここにスライドのIDを入力してください";
  const presentation = SlidesApp.openById(SLIDE_ID);
  const slide = presentation.getSlides()[0]; // 1枚目のスライドを操作

  // スライド内のプレースホルダーテキストを実データで置換する
  slide.replaceAllText("{{MONTH}}", reportMonth + " 実績");
  slide.replaceAllText("{{SALES}}", salesTotal.toLocaleString() + " 円");

  SpreadsheetApp.getActiveSpreadsheet().toast("スライドへの反映が完了しました。");
}
```

### 実践-6 の全体コード：シート編集時にトースト＆Slack通知

```javascript
// ※この関数は「編集時」トリガーに設定して使います
function onEditTrigger(e) {
  const sheet = e.source.getActiveSheet();
  const row = e.range.getRow();
  const col = e.range.getColumn();
  const newValue = e.value;

  // 1行目（ヘッダー行）の編集は無視する
  if (row === 1) return;

  // A列（カラム番号1）が編集された時だけ処理する
  if (col === 1) {
    const message =
      "シート「" + sheet.getName() + "」の " + row + " 行目が更新されました。\n" +
      "入力内容: " + newValue;

    // ① トースト通知（画面右下にポップアップ）
    SpreadsheetApp.getActiveSpreadsheet().toast(message, "編集通知", 5);

    // ② Slack Incoming Webhookへ通知する場合はコメントを外してください
    // const webhookUrl = "https://hooks.slack.com/services/XXXXXX/XXXXXX/XXXXXX";
    // UrlFetchApp.fetch(webhookUrl, {
    //   method: "post",
    //   contentType: "application/json",
    //   payload: JSON.stringify({ text: message })
    // });
  }
}
```

### 実践-7 の全体コード（演習問題 4 解答版）：カレンダー予定をシートへ書き出し

```javascript
function getCalendarEvents() {
  const now = new Date();
  // 今日から1週間分の予定を取得する範囲を設定
  const oneWeekLater = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000);

  // デフォルトのカレンダーから指定期間のイベントを全件取得
  const events = CalendarApp.getDefaultCalendar().getEvents(now, oneWeekLater);

  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // 既存データのクリア（2行目以降のA〜C列）
  if (sheet.getLastRow() >= 2) {
    sheet.getRange(2, 1, sheet.getLastRow() - 1, 3).clearContent();
  }

  // 1行目にヘッダーを設定
  sheet.getRange("A1").setValue("予定タイトル");
  sheet.getRange("B1").setValue("開始日時");
  sheet.getRange("C1").setValue("終了日時");

  // カレンダーイベントを1件ずつ行へ書き込む
  events.forEach((event, index) => {
    sheet.getRange(index + 2, 1).setValue(event.getTitle());     // A列：タイトル
    sheet.getRange(index + 2, 2).setValue(event.getStartTime()); // B列：開始時間
    sheet.getRange(index + 2, 3).setValue(event.getEndTime());   // C列：終了時間（演習4の追加分）
  });

  SpreadsheetApp.getActiveSpreadsheet().toast(events.length + " 件の予定を書き出しました。");
}
```


---

## 技術リファレンス編 第1章 Google Apps Scriptの基礎知識
Duration: 0:20:00

### 01-01 Google Apps Scriptとは
Google Apps Script（GAS）は、Googleが提供するクラウドベースのスクリプト環境です。JavaScriptをベースとした言語で記述し、GoogleのサーバーでホストされているためローカルのPCにインストールする必要がありません。

GASは「Google Apps Script IDE」（統合開発環境）をWebブラウザ上で提供しており、コードの記述・デバッグ・実行がすべてブラウザ内で完結します。また、作成したスクリプトはGoogleのクラウドサーバー上で実行されるため、自分のPCがオフラインでも動作し続けます。

```javascript
// 最初のGASコード：ログにメッセージを出力する
function helloGAS() {
  Logger.log("Hello, Google Apps Script!");
  console.log("コンソールにも出力できます");
}
```

### 01-02 Google AppsとGoogle Workspace
Google Workspace（旧G Suite）は、Googleが提供するクラウドベースの業務用アプリケーション群です。GASはこれらすべてのアプリケーションとネイティブに連携できます。

| サービス | GASでの操作例 |
|---|---|
| Gmail | メール送受信・下書き作成 |
| Googleスプレッドシート | データ読み書き・書式設定 |
| Googleドライブ | ファイル・フォルダ操作 |
| Googleカレンダー | 予定の作成・取得 |
| Googleドキュメント | 文書の作成・編集 |
| Googleフォーム | フォーム作成・回答取得 |
| Googleスライド | プレゼン資料の自動生成 |

```javascript
// 各サービスの起点となるAppクラスを確認するコード
function checkServices() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  Logger.log("スプレッドシート名: " + ss.getName());

  const user = Session.getActiveUser();
  Logger.log("実行ユーザー: " + user.getEmail());
}
```

### 01-03 GASで操作できるアプリケーション
GASから操作できる主なGoogleサービスと、それぞれの「Appクラス（サービスのエントリーポイント）」を確認しましょう。

```javascript
function listAvailableServices() {
  // スプレッドシート
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();

  // Gmail
  const threads = GmailApp.getInboxThreads(0, 5);

  // ドライブ
  const rootFolder = DriveApp.getRootFolder();

  // カレンダー
  const calendar = CalendarApp.getDefaultCalendar();

  // ドキュメント（スタンドアロンプロジェクトから）
  // const doc = DocumentApp.create("新しいドキュメント");

  Logger.log("スプレッドシート: " + spreadsheet.getName());
  Logger.log("受信トレイのスレッド数: " + threads.length);
  Logger.log("ドライブのルートフォルダ: " + rootFolder.getName());
  Logger.log("カレンダー名: " + calendar.getName());
}
```

### 01-04 GASを学ぶ上で知っておくべき注意点
GASには通常のJavaScript環境とは異なるいくつかの制限があります。開発前に把握しておきましょう。

| 制限事項 | 内容 |
|---|---|
| 実行時間 | 1回の実行につき最大6分（無料）/ 30分（Workspace） |
| 同時実行 | 同一スクリプトの並列実行不可 |
| URL Fetch | 1日あたり最大20,000回（無料） |
| メール送信 | 1日あたり最大100通（無料） |
| スプレッドシートのセル | 最大1,000万セル |

```javascript
// 実行時間制限への対処例：キャッシュ（続きの位置）を保存して再実行
function batchProcessWithResume() {
  const startTime = new Date().getTime();
  const LIMIT_MS = 5 * 60 * 1000; // 5分でセーフに切り上げ

  const props = PropertiesService.getScriptProperties();
  let startRow = Number(props.getProperty("lastRow") || 2);

  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();

  for (let row = startRow; row <= lastRow; row++) {
    // 5分経過したら位置を保存して終了
    if (new Date().getTime() - startTime > LIMIT_MS) {
      props.setProperty("lastRow", row.toString());
      Logger.log(row + "行目で一時停止。次回はここから再開します。");
      return;
    }
    // 実際の処理
    const value = sheet.getRange(row, 1).getValue();
    sheet.getRange(row, 2).setValue(value + "_処理済");
  }
  // すべて完了したらキャッシュを削除
  props.deleteProperty("lastRow");
  Logger.log("全行の処理が完了しました");
}
```

### 演習問題 第1章
`helloGAS()` 関数を参考に、自分の名前とメールアドレスを `Logger.log()` で出力する `myInfo()` という関数を作成してください。実行後、エディタ左上の「実行ログ」で出力を確認してみましょう。

---

## 技術リファレンス編 第2章 スクリプトエディタとダッシュボード
Duration: 0:25:00

### 02-01 はじめてのGAS
スクリプトエディタを初めて開く手順と、各UIパーツの役割を確認しましょう。

1. Googleスプレッドシートまたはドライブを開きます。
2. **「拡張機能」→「Apps Script」** または **「新規」→「その他」→「Google Apps Script」** を選択します。
3. エディタが開くと `function myFunction() {}` というデフォルトコードが表示されます。

```javascript
// エディタを確認するための基本コード
function editorCheck() {
  // Loggerはクラシック実行ログに出力される
  Logger.log("Logger による出力です");

  // console.logはV8エンジン以降で使用可能（実行ログに出力）
  console.log("console.log による出力です");

  // ユーザーに向けたダイアログ表示
  SpreadsheetApp.getUi().alert("スクリプトが実行されました！");
}
```

### 02-02 プロジェクトとスクリプト
GASのコードは「プロジェクト」単位で管理されます。1つのプロジェクトは複数の `.gs` ファイル（スクリプトファイル）を持てます。

```javascript
// 複数ファイルを活用する例
// --- utils.gs ---
function formatCurrency(value) {
  return "¥" + value.toLocaleString();
}

// --- main.gs ---
function showSalesReport() {
  const sales = 1250000;
  // 別ファイルの関数を呼び出せる
  const formatted = formatCurrency(sales);
  Logger.log("今月の売上: " + formatted);
}
```

### 02-03 スクリプトエディタの編集機能
エディタには補完・検索・整形などの機能があります。

| 操作 | ショートカット |
|---|---|
| 保存 | Ctrl/Cmd + S |
| 実行 | Ctrl/Cmd + Enter |
| コメントアウト | Ctrl/Cmd + / |
| 検索 | Ctrl/Cmd + F |
| 検索＆置換 | Ctrl/Cmd + H |
| 自動整形 | Shift + Alt + F |

```javascript
// オートコンプリートを体験するためのコード
// SpreadsheetApp. と入力すると候補が出ることを確認
function autoCompleteDemo() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  // ss. と入力してみてください → メソッド一覧が表示されます
  const sheet = ss.getActiveSheet();
  const range = sheet.getRange("A1");
  range.setValue("オートコンプリート成功！");
}
```

### 02-04 ログとデバッグ
GASでは `Logger.log()` / `console.log()` のほか、ブレークポイントを使ったデバッグが可能です。

```javascript
function debugDemo() {
  const data = [10, 20, "hello", null, undefined, true];

  data.forEach((item, index) => {
    // typeof で型を確認しながらデバッグ
    Logger.log("index=" + index + " value=" + item + " type=" + typeof item);
  });

  // console.error / console.warn も使える
  console.warn("これは警告メッセージです");
  console.error("これはエラーメッセージです（実行は止まりません）");
}

// スタックトレースを含む詳細ログ
function detailedLog() {
  try {
    const result = riskyOperation();
    Logger.log("成功: " + result);
  } catch (e) {
    // error.stackでスタックトレースを取得
    Logger.log("エラー発生: " + e.message);
    Logger.log("スタック: " + e.stack);
  }
}

function riskyOperation() {
  throw new Error("意図的なエラーです");
}
```

### 02-05 権限と許可
GASはGoogleのサービスにアクセスするため、初回実行時に「OAuthスコープ」の認可が必要です。

```javascript
// appsscript.json に記載が必要なスコープ例（自動設定も可能）
// {
//   "oauthScopes": [
//     "https://www.googleapis.com/auth/spreadsheets",
//     "https://www.googleapis.com/auth/gmail.send",
//     "https://www.googleapis.com/auth/drive"
//   ]
// }

// 現在の実行ユーザーとスコープを確認
function checkAuth() {
  const user = Session.getActiveUser();
  Logger.log("実行ユーザー: " + user.getEmail());

  const effectiveUser = Session.getEffectiveUser();
  Logger.log("有効ユーザー: " + effectiveUser.getEmail());
}
```

### 02-06 サポートメニューとリファレンス
GASのリファレンスはエディタの「？」メニューまたは以下のURLから参照できます。

```javascript
// 公式リファレンスで確認すべき主なドキュメント
// https://developers.google.com/apps-script/reference

function openReferenceLinks() {
  // エディタのヘルプメニューから「Apps Script リファレンス」をクリック
  // またはコード中のクラス名にカーソルを当ててF1キーを押せばリファレンスへ
  Logger.log("SpreadsheetAppの詳細は Reference > Spreadsheet Service を参照");
}
```

### 演習問題 第2章
`debugDemo()` を参考に、A1〜A5セルのデータを読み込み、各セルの値と型を `Logger.log()` で出力する `inspectCells()` 関数を作成してください。スプレッドシートのA列に数字・文字・空白を混在させてからテストしてみましょう。

---

## 技術リファレンス編 第3章 基本構文
Duration: 0:30:00

### 03-01 JavaScriptの基本
GASはJavaScript（ECMAScript 2019 以降）をベースにしています。JavaScriptの基本的な特徴を押さえましょう。

```javascript
function jsBasics() {
  // セミコロンは省略可能だが、つける方がより安全
  Logger.log("文字列リテラル");

  // テンプレートリテラル（バッククォート）
  const name = "田中";
  Logger.log(`こんにちは、${name}さん！`);

  // 複数行文字列もテンプレートリテラルで
  const multiLine = `1行目
2行目
3行目`;
  Logger.log(multiLine);
}
```

### 03-02 変数・定数
GASでは `var`（非推奨）・`let`（変数）・`const`（定数）の3種類の宣言があります。

```javascript
function variableDemo() {
  // const: 再代入不可（推奨。オブジェクトや配列の中身は変更可能）
  const PI = 3.14159;
  const config = { env: "production", maxRetry: 3 };
  config.env = "staging"; // ← オブジェクトの中身は変更できる
  // PI = 3; // ← これはエラーになる

  // let: ブロックスコープ変数（ループカウンタ等に使用）
  let count = 0;
  count++;
  Logger.log("count: " + count);

  // var: 関数スコープ（旧来の書き方。現在は非推奨）
  var oldStyle = "使わない方がよい";
  Logger.log(oldStyle);

  Logger.log("PI=" + PI + " env=" + config.env);
}
```

### 03-03 データ型
JavaScriptには7種類のプリミティブ型があります。

```javascript
function dataTypeDemo() {
  // プリミティブ型
  const num = 42;           // Number
  const str = "テキスト";   // String
  const bool = true;        // Boolean
  const nothing = null;     // Null
  let undef;                // Undefined
  const big = 9007199254740993n; // BigInt（GASでは稀）
  const sym = Symbol("id"); // Symbol（GASでは稀）

  Logger.log(typeof num);   // "number"
  Logger.log(typeof str);   // "string"
  Logger.log(typeof bool);  // "boolean"
  Logger.log(typeof nothing); // "object"（JavaScript の歴史的バグ）
  Logger.log(typeof undef); // "undefined"

  // 型変換
  Logger.log(String(123));      // "123"
  Logger.log(Number("456"));    // 456
  Logger.log(Number("abc"));    // NaN
  Logger.log(Boolean(0));       // false
  Logger.log(Boolean(""));      // false
  Logger.log(Boolean("a"));     // true
  Logger.log(Boolean(null));    // false

  // NaN のチェック
  Logger.log(isNaN(NaN));       // true
  Logger.log(Number.isNaN(NaN)); // true（より厳密）
}
```

### 03-04 配列
配列は複数の値を順序付きで格納するデータ構造です。

```javascript
function arrayDemo() {
  // 配列の宣言
  const fruits = ["りんご", "みかん", "ぶどう"];

  Logger.log(fruits[0]);          // "りんご"（0始まり）
  Logger.log(fruits.length);      // 3

  // 追加・削除
  fruits.push("バナナ");          // 末尾に追加
  fruits.unshift("いちご");       // 先頭に追加
  fruits.pop();                    // 末尾を削除
  fruits.shift();                  // 先頭を削除

  // スプレッド演算子
  const moreFruits = [...fruits, "メロン", "スイカ"];

  // 分割代入
  const [first, second, ...rest] = fruits;
  Logger.log("first=" + first + " second=" + second);
  Logger.log("rest=" + rest.join(", "));

  // よく使うメソッド
  Logger.log(fruits.indexOf("みかん")); // 0（見つからなければ-1）
  Logger.log(fruits.includes("ぶどう")); // true
  Logger.log(fruits.join(" / "));
  Logger.log(fruits.slice(0, 2));       // 部分配列
  Logger.log(fruits.reverse());         // 逆順（元の配列も変更される）
}
```

### 03-05 オブジェクト
オブジェクトは「キーと値」のペアでデータを管理する構造体です。

```javascript
function objectDemo() {
  // オブジェクトリテラル
  const user = {
    name: "山田太郎",
    age: 30,
    email: "yamada@example.com",
    address: {
      city: "東京",
      zip: "100-0001"
    }
  };

  // プロパティのアクセス
  Logger.log(user.name);           // ドット記法
  Logger.log(user["email"]);       // ブラケット記法（動的キーに便利）
  Logger.log(user.address.city);   // ネストされたオブジェクト

  // 分割代入
  const { name, age, address: { city } } = user;
  Logger.log(`${name}(${age})は${city}在住`);

  // スプレッド演算子でコピー・マージ
  const updatedUser = { ...user, age: 31, phone: "000-0000-0000" };
  Logger.log(updatedUser.age + " " + updatedUser.phone);

  // オブジェクトのキー・値・エントリを取得
  Logger.log(Object.keys(user));
  Logger.log(Object.values(user));
  Object.entries(user).forEach(([key, val]) => {
    if (typeof val !== "object") Logger.log(key + ": " + val);
  });
}
```

### 03-06 算術演算子と代入演算子
数値計算と変数への代入で使う演算子一覧です。

```javascript
function operatorDemo() {
  // 算術演算子
  Logger.log(10 + 3);   // 13（加算）
  Logger.log(10 - 3);   // 7（減算）
  Logger.log(10 * 3);   // 30（乗算）
  Logger.log(10 / 3);   // 3.333...（除算）
  Logger.log(10 % 3);   // 1（剰余：割り算の余り）
  Logger.log(2 ** 8);   // 256（べき乗）

  // 代入演算子の省略形
  let x = 10;
  x += 5;   // x = x + 5 → 15
  x -= 3;   // x = x - 3 → 12
  x *= 2;   // x = x * 2 → 24
  x /= 4;   // x = x / 4 → 6
  x %= 4;   // x = x % 4 → 2
  Logger.log("x = " + x);

  // 文字列と数値の演算（型強制）
  Logger.log("5" + 3);     // "53"（文字列連結が優先）
  Logger.log("5" - 3);     // 2（減算は数値変換される）
  Logger.log(+"5" + 3);    // 8（+演算子で数値変換）
  Logger.log(parseInt("5px")); // 5（先頭の数字部分だけ取得）
}
```

### 演習問題 第3章
スプレッドシートのA1〜A10セルに金額（数値）を入力し、合計・平均・最大値・最小値を計算してB1〜B4セルにそれぞれ書き出す `calcStats()` 関数を作成してください。配列操作（`reduce`, `Math.max`, `Math.min`）を使って計算してみましょう。

---

## 技術リファレンス編 第4章 制御構文
Duration: 0:30:00

### 04-01 if文による条件分岐
条件の真偽によって処理を分岐させます。

```javascript
function ifDemo() {
  const score = 75;

  if (score >= 90) {
    Logger.log("評価: S");
  } else if (score >= 70) {
    Logger.log("評価: A");
  } else if (score >= 50) {
    Logger.log("評価: B");
  } else {
    Logger.log("評価: C");
  }

  // 三項演算子（短い条件式に便利）
  const result = score >= 60 ? "合格" : "不合格";
  Logger.log(result);

  // Nullish合体演算子（??）：null/undefinedの場合だけデフォルト値を使う
  const userInput = null;
  const displayName = userInput ?? "名前未設定";
  Logger.log(displayName); // "名前未設定"

  // オプショナルチェイン（?.）：ネストされたプロパティが存在しない場合にエラーを防ぐ
  const config = null;
  Logger.log(config?.apiKey ?? "APIキー未設定"); // エラーにならない
}
```

### 04-02 条件式と比較演算子・論理演算子

```javascript
function comparisonDemo() {
  // 比較演算子
  Logger.log(5 == "5");   // true（型変換あり：非推奨）
  Logger.log(5 === "5");  // false（型変換なし：推奨）
  Logger.log(5 != "5");   // false
  Logger.log(5 !== "5");  // true
  Logger.log(5 > 3);      // true
  Logger.log(5 >= 5);     // true

  // 論理演算子
  Logger.log(true && false); // false（AND：両方trueのとき）
  Logger.log(true || false); // true（OR：どちらかtrueのとき）
  Logger.log(!true);         // false（NOT）

  // 短絡評価（&&/||の特性を活用）
  const value = null;
  const safe = value && value.toString(); // valueがnullなら&&以降は評価されない
  Logger.log(safe); // null

  const fallback = value || "デフォルト値";
  Logger.log(fallback); // "デフォルト値"

  // 偽値（falsy）一覧：これらはすべてif文でfalseとして扱われる
  // false, 0, "", null, undefined, NaN
  const falsyValues = [false, 0, "", null, undefined, NaN];
  falsyValues.forEach(v => {
    if (!v) Logger.log(String(v) + " は偽値です");
  });
}
```

### 04-03 switch文による多岐分岐
複数の条件に対して明確に処理を振り分けるときに使います。

```javascript
function switchDemo() {
  const dayOfWeek = new Date().getDay(); // 0=日, 1=月, ..., 6=土

  switch (dayOfWeek) {
    case 0:
      Logger.log("今日は日曜日");
      break;
    case 1:
      Logger.log("今日は月曜日");
      break;
    case 2:
    case 3:
    case 4:
      Logger.log("今日は火/水/木曜日");
      break;
    case 5:
      Logger.log("今日は金曜日 🎉");
      break;
    case 6:
      Logger.log("今日は土曜日");
      break;
    default:
      Logger.log("不明な曜日");
  }
}
```

### 04-04 while文による繰り返し
条件が真である間、処理を繰り返します。

```javascript
function whileDemo() {
  // while: 条件をチェックしてからループ
  let n = 1;
  let sum = 0;
  while (n <= 10) {
    sum += n;
    n++;
  }
  Logger.log("1〜10の合計: " + sum); // 55

  // do...while: 最低1回は実行してから条件チェック
  let count = 0;
  do {
    count++;
    Logger.log("do-while実行回数: " + count);
  } while (count < 3);
}
```

### 04-05 for文による繰り返し
カウンタを使った繰り返し処理の基本形です。

```javascript
function forDemo() {
  // 基本のfor文
  for (let i = 0; i < 5; i++) {
    Logger.log("i = " + i);
  }

  // スプレッドシートの行を走査する実践例
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();

  for (let row = 2; row <= lastRow; row++) { // 2行目（ヘッダー除外）から最終行まで
    const name = sheet.getRange(row, 1).getValue();
    const score = sheet.getRange(row, 2).getValue();
    if (score >= 80) {
      Logger.log(name + " さんは高得点（" + score + "点）です！");
    }
  }
}
```

### 04-06 for...of文による繰り返し
配列や文字列などの「反復可能なオブジェクト」の要素を順番に処理します。

```javascript
function forOfDemo() {
  const members = ["Alice", "Bob", "Charlie", "Diana"];

  // 配列の要素を順番に取り出す
  for (const name of members) {
    Logger.log("メンバー: " + name);
  }

  // 文字列の1文字ずつを処理
  for (const char of "GAS") {
    Logger.log("文字: " + char);
  }

  // entries()でindexも取得
  for (const [index, name] of members.entries()) {
    Logger.log(index + ": " + name);
  }
}
```

### 04-07 for...in文による繰り返し
オブジェクトのすべてのキーを列挙します。

```javascript
function forInDemo() {
  const userInfo = {
    name: "山田太郎",
    department: "営業部",
    years: 5,
    role: "マネージャー"
  };

  // オブジェクトのキーを列挙
  for (const key in userInfo) {
    Logger.log(key + ": " + userInfo[key]);
  }

  // 注意：配列への for...in は非推奨（for-of または forEach を使うこと）
}
```

### 04-08 繰り返し処理の中断とスキップ
`break` で繰り返しを中断し、`continue` で次のイテレーションへスキップします。

```javascript
function breakContinueDemo() {
  const data = [10, 25, -5, 40, 0, 15, -3, 100];

  Logger.log("--- break: 最初の負の値で処理を中断 ---");
  for (const val of data) {
    if (val < 0) {
      Logger.log("負の値 " + val + " が見つかりました。処理を中断します。");
      break;
    }
    Logger.log("処理中: " + val);
  }

  Logger.log("--- continue: 0以下はスキップして合計を計算 ---");
  let positiveSum = 0;
  for (const val of data) {
    if (val <= 0) continue; // 0以下はスキップ
    positiveSum += val;
  }
  Logger.log("正の値の合計: " + positiveSum);
}
```

### 04-09 try...catch文と例外処理
エラーが発生しても処理を安全に続けるための構文です。

```javascript
function tryCatchDemo() {
  // 基本のtry-catch-finally
  try {
    const data = JSON.parse('{"name": "田中"}'); // 正常なJSON
    Logger.log("パース成功: " + data.name);

    const invalid = JSON.parse("これはJSONではない"); // エラーが発生
    Logger.log("この行は実行されない");

  } catch (e) {
    // Errorオブジェクトのプロパティ
    Logger.log("エラー名: " + e.name);        // "SyntaxError"など
    Logger.log("メッセージ: " + e.message);
    Logger.log("スタック: " + e.stack);

    // エラーをメールで通知する実践的な例
    // GmailApp.sendEmail("admin@example.com", "GASエラー: " + e.name, e.stack);

  } finally {
    // エラーの有無に関わらず必ず実行
    Logger.log("処理終了（finally）");
  }

  // カスタムエラーをthrowする
  function divide(a, b) {
    if (b === 0) throw new Error("ゼロ除算は禁止です");
    return a / b;
  }

  try {
    Logger.log(divide(10, 2)); // 5
    Logger.log(divide(10, 0)); // エラー
  } catch (e) {
    Logger.log("捕捉: " + e.message);
  }
}
```

### 演習問題 第4章
スプレッドシートのA列に「100, 0, 50, -20, 80, null, 60」が入っているとして、以下の条件で処理する `filterAndSum()` 関数を書いてください。
- null や空のセルはスキップ（`continue`）
- 0以下の値が見つかったらそのセルを赤色に塗る
- 正の値のみを合計してB1セルに出力



---

## 技術リファレンス編 第5章 関数
Duration: 0:20:00

### 05-01 関数とは
関数は処理をひとまとめにして名前をつけ、繰り返し呼び出せるようにしたものです。GASのすべてのコードは関数の中に書きます。

```javascript
// 関数宣言
function greet(name) {
  return "こんにちは、" + name + "さん！";
}
Logger.log(greet("田中")); // "こんにちは、田中さん！"

// デフォルト引数（引数が渡されなかった場合の初期値）
function greetWithDefault(name = "ゲスト", greeting = "こんにちは") {
  return greeting + "、" + name + "さん！";
}
Logger.log(greetWithDefault());          // "こんにちは、ゲストさん！"
Logger.log(greetWithDefault("山田"));    // "こんにちは、山田さん！"
Logger.log(greetWithDefault("田中", "やあ")); // "やあ、田中さん！"

// 残余引数（可変長引数）
function sumAll(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}
Logger.log(sumAll(1, 2, 3, 4, 5)); // 15

// 複数の値を返す（分割代入を活用）
function getMinMax(arr) {
  return [Math.min(...arr), Math.max(...arr)];
}
const [min, max] = getMinMax([3, 1, 4, 1, 5, 9, 2, 6]);
Logger.log("min=" + min + " max=" + max); // min=1 max=9
```

### 05-02 関数リテラル
関数を値として変数に代入したり、引数として渡したりできます。

```javascript
function functionLiteralDemo() {
  // 関数式（変数に代入）
  const double = function(n) { return n * 2; };
  Logger.log(double(5)); // 10

  // アロー関数（省略形）
  const triple = (n) => n * 3;
  const add = (a, b) => a + b;
  Logger.log(triple(4)); // 12
  Logger.log(add(3, 7)); // 10

  // 複数行のアロー関数
  const processData = (data) => {
    const filtered = data.filter(n => n > 0);
    const total = filtered.reduce((sum, n) => sum + n, 0);
    return total / filtered.length;
  };
  Logger.log(processData([-1, 5, 3, -2, 8])); // 5.333...

  // 高階関数（関数を引数に取る関数）
  const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const evens = numbers.filter(n => n % 2 === 0);   // [2,4,6,8,10]
  const doubled = evens.map(n => n * 2);             // [4,8,12,16,20]
  const total = doubled.reduce((sum, n) => sum + n, 0); // 60
  Logger.log("偶数の2倍の合計: " + total);

  // GASでの実践例：スプレッドシートのデータを処理
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getRange("A2:B10").getValues();
  const highScorers = data
    .filter(row => row[1] >= 80)         // B列が80以上
    .map(row => row[0] + "(" + row[1] + "点)"); // A列に点数付きで整形
  Logger.log("高得点者: " + highScorers.join(", "));
}
```

### 05-03 スコープ
変数は宣言した場所によってアクセスできる範囲（スコープ）が決まります。

```javascript
// グローバルスコープ（トップレベル）
const GLOBAL_CONFIG = {
  sheetName: "データ",
  emailTo: "admin@example.com"
};

function scopeDemo() {
  // 関数スコープ（この関数内でのみ有効）
  const localVar = "ローカル変数";
  Logger.log(localVar);
  Logger.log(GLOBAL_CONFIG.sheetName); // グローバル変数にはアクセスできる

  // ブロックスコープ（let/const はブロック内でのみ有効）
  if (true) {
    const blockVar = "ブロック変数";
    let blockLet = "ブロックlet";
    Logger.log(blockVar); // OK（ブロック内）
  }
  // Logger.log(blockVar); // ← エラー！ブロック外からはアクセス不可

  // クロージャ（関数が外側のスコープを記憶する）
  function makeCounter() {
    let count = 0;
    return function() {
      count++;
      return count;
    };
  }
  const counter = makeCounter();
  Logger.log(counter()); // 1
  Logger.log(counter()); // 2
  Logger.log(counter()); // 3
}
```

### 演習問題 第5章
スプレッドシートのA列に商品名、B列に価格、C列に数量が入っているとき、各行の「小計（価格×数量）」を計算してD列に書き込み、最後にE1セルに消費税（10%）込みの合計を書き出す `calcInvoice()` 関数を作成してください。小計の計算は関数（`calcSubtotal(price, qty)`）に切り出して実装してみましょう。

---

## 技術リファレンス編 第6章 クラスとオブジェクト
Duration: 0:25:00

### 06-01 オブジェクト・プロパティ・メソッド
オブジェクトはプロパティ（データ）とメソッド（処理）をひとまとめにした設計図の「実体」です。

```javascript
function objectMethodDemo() {
  // メソッドを持つオブジェクト
  const calculator = {
    // プロパティ
    history: [],
    // メソッド（短縮記法）
    add(a, b) {
      const result = a + b;
      this.history.push(`${a}+${b}=${result}`); // thisで自身を参照
      return result;
    },
    getHistory() {
      return this.history.join(" / ");
    }
  };

  Logger.log(calculator.add(3, 5));  // 8
  Logger.log(calculator.add(10, 7)); // 17
  Logger.log(calculator.getHistory()); // "3+5=8 / 10+7=17"
}
```

### 06-02 クラスとインスタンス化
`class` キーワードを使ってオブジェクトの設計図（クラス）を定義し、`new` でインスタンスを生成します。

```javascript
// GASでの実践的なクラス例：Slackメッセージ送信クラス
class SlackNotifier {
  constructor(webhookUrl, channel = "#general") {
    this.webhookUrl = webhookUrl;
    this.channel = channel;
    this.messageCount = 0;
  }

  send(text, emoji = ":memo:") {
    const payload = {
      channel: this.channel,
      text: emoji + " " + text
    };
    // 実際に送信する場合は以下を有効化
    // UrlFetchApp.fetch(this.webhookUrl, {
    //   method: "post",
    //   contentType: "application/json",
    //   payload: JSON.stringify(payload)
    // });
    this.messageCount++;
    Logger.log(`[Slack送信 ${this.messageCount}件目] ${payload.text} → ${this.channel}`);
    return this;  // メソッドチェーン用にthisを返す
  }

  sendError(message) {
    return this.send(message, ":red_circle:");
  }
}

function classDemo() {
  const notifier = new SlackNotifier("https://hooks.slack.com/....", "#alerts");
  notifier
    .send("日次バッチ処理を開始します")
    .send("データ取込み完了: 150件")
    .sendError("一部データに不備がありました");
  Logger.log("送信件数: " + notifier.messageCount);
}
```

### 06-03 メソッドとプロトタイプ
JavaScriptのクラスはプロトタイプチェーンに基づいており、継承が可能です。

```javascript
// 基底クラス
class Report {
  constructor(title, date) {
    this.title = title;
    this.date = date || new Date();
  }

  getHeader() {
    return `=== ${this.title} (${Utilities.formatDate(this.date, "JST", "yyyy/MM/dd")}) ===`;
  }

  generate() {
    return this.getHeader() + "\n（基底クラスの内容）";
  }
}

// 派生クラス（継承）
class SalesReport extends Report {
  constructor(date, salesData) {
    super("月次売上レポート", date); // 親クラスのコンストラクタを呼ぶ
    this.salesData = salesData;
  }

  // オーバーライド
  generate() {
    const header = this.getHeader(); // 親のメソッドを呼ぶ
    const total = this.salesData.reduce((sum, item) => sum + item.amount, 0);
    const lines = this.salesData.map(item => `  ${item.name}: ¥${item.amount.toLocaleString()}`);
    return [header, ...lines, `  合計: ¥${total.toLocaleString()}`].join("\n");
  }
}

function inheritanceDemo() {
  const report = new SalesReport(new Date(), [
    { name: "商品A", amount: 120000 },
    { name: "商品B", amount: 85000 },
    { name: "商品C", amount: 230000 }
  ]);
  Logger.log(report.generate());
  Logger.log(report instanceof Report);       // true
  Logger.log(report instanceof SalesReport);  // true
}
```

### 06-04 静的メンバー
インスタンスを作らずに呼び出せるクラスメソッド（`static`）です。

```javascript
class DateUtils {
  // 静的メソッド（インスタンス不要で呼び出せる）
  static getToday() {
    return Utilities.formatDate(new Date(), "JST", "yyyy/MM/dd");
  }

  static isWeekend(date) {
    const day = date.getDay();
    return day === 0 || day === 6;
  }

  static addDays(date, days) {
    const result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
  }

  // 静的プロパティ
  static get HOLIDAYS() {
    return ["2026-01-01", "2026-01-02"]; // 祝日リスト（簡易版）
  }
}

function staticDemo() {
  Logger.log(DateUtils.getToday());
  Logger.log("今日は週末？: " + DateUtils.isWeekend(new Date()));
  Logger.log("1週間後: " + Utilities.formatDate(DateUtils.addDays(new Date(), 7), "JST", "yyyy/MM/dd"));
  Logger.log("祝日: " + DateUtils.HOLIDAYS.join(", "));
}
```

### 演習問題 第6章
`Employee`（従業員）クラスを作成してください。コンストラクタで `name`・`department`・`salary` を受け取り、`getAnnualSalary()`（年収を返す）と `toString()`（「田中 / 営業部 / 月給¥xx」形式の文字列を返す）メソッドを実装してください。複数の従業員を配列に格納し、一番高い年収の人の情報をログに出力してみましょう。

---

## 技術リファレンス編 第7章 JavaScriptの組み込みオブジェクト
Duration: 0:35:00

### 07-01 組み込みオブジェクト
JavaScriptには最初から使えるビルトインオブジェクトが多数存在します。

```javascript
function builtinOverview() {
  Logger.log(typeof Number);   // "function"（コンストラクタ）
  Logger.log(typeof String);   // "function"
  Logger.log(typeof Array);    // "function"
  Logger.log(typeof Math);     // "object"（コンストラクタなし）
  Logger.log(typeof JSON);     // "object"
  Logger.log(typeof Date);     // "function"
}
```

### 07-02 数値を取り扱う - Numberオブジェクト

```javascript
function numberDemo() {
  Logger.log(Number.MAX_SAFE_INTEGER); // 9007199254740991
  Logger.log(Number.MIN_SAFE_INTEGER); // -9007199254740991
  Logger.log(Number.EPSILON);          // 2.220446049250313e-16
  Logger.log(Number.isInteger(3.0));   // true
  Logger.log(Number.isFinite(Infinity)); // false
  Logger.log(Number.isNaN(NaN));       // true
  Logger.log(Number.parseInt("42px")); // 42
  Logger.log(Number.parseFloat("3.14cm")); // 3.14

  const price = 1234567.89;
  Logger.log(price.toFixed(0));        // "1234568"（小数点以下0桁）
  Logger.log(price.toFixed(2));        // "1234567.89"
  Logger.log(price.toLocaleString("ja-JP", { style: "currency", currency: "JPY" })); // "¥1,234,568"
  Logger.log((0.1 + 0.2).toFixed(1)); // "0.3"（浮動小数点誤差を回避）
}
```

### 07-03 文字列を取り扱う - Stringオブジェクト

```javascript
function stringDemo() {
  const s = "Hello, Google Apps Script!";

  Logger.log(s.length);                   // 26
  Logger.log(s.toUpperCase());            // "HELLO, GOOGLE APPS SCRIPT!"
  Logger.log(s.toLowerCase());            // "hello, google apps script!"
  Logger.log(s.includes("Google"));       // true
  Logger.log(s.startsWith("Hello"));      // true
  Logger.log(s.endsWith("!"));            // true
  Logger.log(s.indexOf("Google"));        // 7
  Logger.log(s.slice(7, 13));            // "Google"
  Logger.log(s.replace("Google", "GAS")); // "Hello, GAS Apps Script!"
  Logger.log(s.split(", "));             // ["Hello", "Google Apps Script!"]
  Logger.log("  trim me  ".trim());      // "trim me"
  Logger.log("abc".repeat(3));           // "abcabcabc"
  Logger.log("5".padStart(3, "0"));      // "005"（ゼロパディング）

  // テンプレートリテラル（実践例）
  const name = "田中", score = 92;
  const message = `${name}さん、今月のスコアは${score}点です（${score >= 90 ? "優秀" : "良好"}）`;
  Logger.log(message);
}
```

### 07-04 配列を取り扱う - Arrayオブジェクト

```javascript
function arrayMethodDemo() {
  const nums = [5, 2, 8, 1, 9, 3, 7, 4, 6];

  // 変換・フィルタ・集計
  const doubled = nums.map(n => n * 2);           // すべて2倍
  const evens = nums.filter(n => n % 2 === 0);     // 偶数のみ
  const total = nums.reduce((s, n) => s + n, 0);   // 合計
  const sorted = [...nums].sort((a, b) => a - b);  // 昇順ソート

  Logger.log("doubled: " + doubled);
  Logger.log("evens: " + evens);
  Logger.log("total: " + total);
  Logger.log("sorted: " + sorted);

  // 検索
  Logger.log(nums.find(n => n > 7));         // 8（最初に7より大きい数）
  Logger.log(nums.findIndex(n => n > 7));    // 2（そのインデックス）
  Logger.log(nums.some(n => n > 8));         // true
  Logger.log(nums.every(n => n > 0));        // true

  // 変形
  const matrix = [[1, 2], [3, 4], [5, 6]];
  const flat = matrix.flat();               // [1,2,3,4,5,6]
  Logger.log("flat: " + flat);

  // GASでスプレッドシートデータを2次元配列で処理
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getRange("A2:C10").getValues();
  const processed = data
    .filter(row => row[0] !== "")  // 空行を除外
    .map(row => ({
      name: row[0],
      score: row[1],
      grade: row[1] >= 80 ? "A" : row[1] >= 60 ? "B" : "C"
    }));
  Logger.log(JSON.stringify(processed.slice(0, 3)));
}
```

### 07-05 関数を取り扱う - Functionオブジェクト

```javascript
function functionObjectDemo() {
  // bind: thisと引数を固定した新しい関数を作る
  function multiply(a, b) { return a * b; }
  const double = multiply.bind(null, 2); // 第1引数を2に固定
  const triple = multiply.bind(null, 3);
  Logger.log(double(5));  // 10
  Logger.log(triple(5));  // 15

  // call/apply: thisを指定して関数を即時実行
  function introduce() {
    return `私は${this.name}（${this.role}）です`;
  }
  const person = { name: "田中", role: "エンジニア" };
  Logger.log(introduce.call(person)); // "私は田中（エンジニア）です"

  // 関数の引数の数
  Logger.log(multiply.length); // 2（引数の数）
}
```

### 07-06 日付・時刻を取り扱う - Dateオブジェクト

```javascript
function dateDemo() {
  const now = new Date();
  Logger.log("現在日時: " + now);
  Logger.log("年: " + now.getFullYear());
  Logger.log("月: " + (now.getMonth() + 1)); // 月は0始まりなので+1
  Logger.log("日: " + now.getDate());
  Logger.log("曜日: " + now.getDay()); // 0=日...6=土
  Logger.log("時: " + now.getHours());
  Logger.log("分: " + now.getMinutes());
  Logger.log("ミリ秒タイムスタンプ: " + now.getTime());

  // Utilitiesと組み合わせた日付フォーマット（GAS推奨）
  Logger.log(Utilities.formatDate(now, "JST", "yyyy/MM/dd HH:mm:ss"));
  Logger.log(Utilities.formatDate(now, "JST", "yyyyMMdd"));

  // 日付の計算
  const twoWeeksLater = new Date(now.getTime() + 14 * 24 * 60 * 60 * 1000);
  Logger.log("2週間後: " + Utilities.formatDate(twoWeeksLater, "JST", "yyyy/MM/dd"));

  // 月初め・月末の計算
  const firstDay = new Date(now.getFullYear(), now.getMonth(), 1);
  const lastDay  = new Date(now.getFullYear(), now.getMonth() + 1, 0);
  Logger.log("月初め: " + Utilities.formatDate(firstDay, "JST", "yyyy/MM/dd"));
  Logger.log("月末: " + Utilities.formatDate(lastDay, "JST", "yyyy/MM/dd"));
}
```

### 07-07 正規表現を取り扱う - RegExpオブジェクト

```javascript
function regexDemo() {
  // メールアドレスの検証
  const emailRe = /^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$/;
  Logger.log(emailRe.test("user@example.com")); // true
  Logger.log(emailRe.test("invalid-email"));    // false

  // 電話番号の抽出
  const text = "連絡先：090-1234-5678 または 03-1234-5678 まで";
  const phoneRe = /\d{2,4}-\d{2,4}-\d{4}/g;
  const phones = text.match(phoneRe);
  Logger.log("電話番号: " + phones.join(", "));

  // 置換（replace）
  const csv = "田中, 山田, 佐藤 ,鈴木";
  const cleaned = csv.replace(/\s*,\s*/g, ","); // カンマ周りの空白を除去
  Logger.log(cleaned); // "田中,山田,佐藤,鈴木"

  // グループキャプチャ
  const dateStr = "2026-04-10";
  const match = dateStr.match(/^(\d{4})-(\d{2})-(\d{2})$/);
  if (match) {
    Logger.log(`年:${match[1]} 月:${match[2]} 日:${match[3]}`);
  }
}
```

### 07-08 例外情報を取得する - Errorオブジェクト

```javascript
function errorObjectDemo() {
  // Errorの種類
  const errorTypes = [
    new Error("一般エラー"),
    new TypeError("型エラー"),
    new RangeError("範囲エラー"),
    new ReferenceError("参照エラー"),
    new SyntaxError("構文エラー")
  ];

  errorTypes.forEach(err => {
    Logger.log(`[${err.name}] ${err.message}`);
  });

  // カスタムエラークラス
  class ApiError extends Error {
    constructor(message, statusCode) {
      super(message);
      this.name = "ApiError";
      this.statusCode = statusCode;
    }
  }

  try {
    throw new ApiError("レート制限を超えました", 429);
  } catch (e) {
    Logger.log(`${e.name} (${e.statusCode}): ${e.message}`);
  }
}
```

### 07-09 数学演算を実行する - Mathオブジェクト

```javascript
function mathDemo() {
  Logger.log(Math.PI);              // 3.141592653589793
  Logger.log(Math.E);               // 2.718281828459045
  Logger.log(Math.abs(-42));        // 42（絶対値）
  Logger.log(Math.round(4.5));      // 5（四捨五入）
  Logger.log(Math.floor(4.9));      // 4（切り捨て）
  Logger.log(Math.ceil(4.1));       // 5（切り上げ）
  Logger.log(Math.max(1, 5, 3));    // 5
  Logger.log(Math.min(1, 5, 3));    // 1
  Logger.log(Math.pow(2, 10));      // 1024
  Logger.log(Math.sqrt(144));       // 12
  Logger.log(Math.log2(1024));      // 10
  Logger.log(Math.random());        // 0〜1未満のランダムな数

  // 指定範囲内のランダム整数
  function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  Logger.log("1〜100のランダム: " + randomInt(1, 100));

  // 配列の最大・最小（スプレッド演算子でMathに渡す）
  const scores = [78, 92, 55, 88, 73];
  Logger.log("最高点: " + Math.max(...scores));
  Logger.log("最低点: " + Math.min(...scores));
}
```

### 07-10 JSONデータを取り扱う - JSONオブジェクト

```javascript
function jsonDemo() {
  // オブジェクト → JSON文字列
  const user = { name: "田中", age: 30, tags: ["GAS", "自動化"] };
  const json = JSON.stringify(user);
  Logger.log(json); // {"name":"田中","age":30,"tags":["GAS","自動化"]}

  // インデント付きで整形
  Logger.log(JSON.stringify(user, null, 2));

  // JSON文字列 → オブジェクト
  const parsed = JSON.parse(json);
  Logger.log(parsed.name + " / " + parsed.tags.join(", "));

  // replacer（特定キーのみシリアライズ）
  const partial = JSON.stringify(user, ["name", "age"]);
  Logger.log(partial); // {"name":"田中","age":30}

  // GASでの実践：PropertiesServiceにオブジェクトを保存
  const props = PropertiesService.getScriptProperties();
  props.setProperty("config", JSON.stringify({ maxRow: 1000, debug: false }));
  const config = JSON.parse(props.getProperty("config"));
  Logger.log("maxRow: " + config.maxRow);
}
```

### 07-11 オブジェクトを取り扱う - Objectオブジェクト

```javascript
function objectUtilDemo() {
  const src = { a: 1, b: 2 };
  const ext = { b: 99, c: 3 };

  // Object.assign: オブジェクトのマージ（浅いコピー）
  const merged = Object.assign({}, src, ext);
  Logger.log(JSON.stringify(merged)); // {"a":1,"b":99,"c":3}

  // Object.keys / values / entries
  Logger.log(Object.keys(merged));   // ["a","b","c"]
  Logger.log(Object.values(merged)); // [1,99,3]
  Logger.log(JSON.stringify(Object.entries(merged))); // [["a",1],["b",99],["c",3]]

  // Object.freeze: オブジェクトを変更不可にする
  const CONSTANTS = Object.freeze({ MAX: 100, MIN: 0 });
  // CONSTANTS.MAX = 999; // strictモードではエラー、通常は無視される
  Logger.log(CONSTANTS.MAX); // 100

  // Object.fromEntries: entries → オブジェクトに変換
  const pairs = [["x", 10], ["y", 20], ["z", 30]];
  const obj = Object.fromEntries(pairs);
  Logger.log(JSON.stringify(obj)); // {"x":10,"y":20,"z":30}

  // Object.hasOwn: プロパティの存在チェック（推奨）
  Logger.log(Object.hasOwn(merged, "a")); // true
  Logger.log(Object.hasOwn(merged, "d")); // false
}
```

### 07-12 グローバル関数

```javascript
function globalFunctionsDemo() {
  // 数値変換
  Logger.log(parseInt("10", 10));   // 10（10進数として解析）
  Logger.log(parseInt("0xff", 16)); // 255（16進数）
  Logger.log(parseFloat("3.14pi")); // 3.14
  Logger.log(isNaN("hello"));       // true
  Logger.log(isFinite(1e308));      // true（Infinityでなければtrue）

  // エンコード・デコード
  const url = "https://example.com/search?q=Google スプレッドシート";
  const encoded = encodeURIComponent("Google スプレッドシート");
  Logger.log(encoded); // "Google%20%E3%82%B9%E3%83%97%E3%83%AC..."
  Logger.log(decodeURIComponent(encoded));

  // eval（使用は非推奨・セキュリティリスクあり）
  // Logger.log(eval("2 + 2")); // 4（動的コード実行）
}
```

### 演習問題 第7章
スプレッドシートのA列に以下の電話番号が混在して入っているとします（スペースあり・ハイフン形式混在）。正規表現を使って統一形式（`xxx-xxxx-xxxx`）に変換してB列に書き出す `normalizePhones()` 関数を作成してください。
- `090 1234 5678`
- `09012345678`
- `090-1234-5678`



---

## 技術リファレンス編 第8章 スプレッドシート
Duration: 0:45:00

### 08-01 Spreadsheetサービス
`SpreadsheetApp` はスプレッドシート操作のエントリーポイントです。ここからすべての操作が始まります。

```javascript
function spreadsheetServiceOverview() {
  // 現在アクティブなスプレッドシートを取得
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // IDで特定のスプレッドシートを取得（別のファイルにアクセス）
  // const ss = SpreadsheetApp.openById("スプレッドシートID");

  // URLで取得
  // const ss = SpreadsheetApp.openByUrl("https://docs.google.com/...");

  Logger.log("スプレッドシート名: " + ss.getName());
  Logger.log("スプレッドシートID: " + ss.getId());
  Logger.log("URL: " + ss.getUrl());
}
```

### 08-02 SpreadsheetAppクラス

```javascript
function spreadsheetAppDemo() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // ファイル全体の情報
  Logger.log("スプレッドシート名: " + ss.getName());
  Logger.log("オーナー: " + ss.getOwner().getEmail());
  Logger.log("最終更新日: " + ss.getLastUpdated());

  // スプレッドシートのロケール設定
  Logger.log("ロケール: " + ss.getSpreadsheetLocale());
  Logger.log("タイムゾーン: " + ss.getSpreadsheetTimeZone());

  // すべてのシートの一覧
  const sheets = ss.getSheets();
  sheets.forEach(sheet => Logger.log("シート: " + sheet.getName()));

  // 通知（ユーザーへのフィードバック）
  ss.toast("処理中です...", "自動化スクリプト", 5); // 5秒間表示
}
```

### 08-03 スプレッドシートを操作する - Spreadsheetクラス

```javascript
function spreadsheetClassDemo() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // シートの作成・取得・削除
  const newSheet = ss.insertSheet("新しいシート");
  const sheet1 = ss.getSheetByName("シート1");
  const activeSheet = ss.getActiveSheet();

  // シートのコピー
  const copied = sheet1.copyTo(ss);
  copied.setName("シート1のコピー");

  // シートの移動（インデックスで管理）
  ss.setActiveSheet(newSheet);

  // 名前付き範囲の設定
  ss.setNamedRange("データ範囲", sheet1.getRange("A1:D100"));
  const namedRange = ss.getRangeByName("データ範囲");
  Logger.log("名前付き範囲: " + namedRange.getA1Notation());

  // 後始末（作成したシートを削除）
  ss.deleteSheet(newSheet);
  ss.deleteSheet(copied);
}
```

### 08-04 シートを操作する - Sheetクラス

```javascript
function sheetClassDemo() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // シートの情報
  Logger.log("シート名: " + sheet.getName());
  Logger.log("最終行: " + sheet.getLastRow());
  Logger.log("最終列: " + sheet.getLastColumn());
  Logger.log("最大行数: " + sheet.getMaxRows());

  // 行・列の操作
  sheet.insertRowBefore(2);          // 2行目の前に行を挿入
  sheet.insertColumnAfter(3);        // 3列目の後に列を挿入
  sheet.deleteRow(10);               // 10行目を削除
  sheet.deleteColumn(5);             // 5列目を削除
  sheet.hideRow(sheet.getRange("5:5"));  // 5行目を非表示
  sheet.showRows(5, 1);             // 5行目から1行を表示

  // 行・列の高さ/幅
  sheet.setRowHeight(1, 40);        // 1行目の高さを40に
  sheet.setColumnWidth(1, 150);     // A列の幅を150に

  // シートの保護
  const protection = sheet.protect().setDescription("管理者のみ編集可");
  // protection.addEditor("admin@example.com");

  // データのソート（A列昇順）
  const dataRange = sheet.getRange("A2:D" + sheet.getLastRow());
  dataRange.sort({ column: 1, ascending: true });

  // シートのクリア
  // sheet.clearContents(); // コンテンツのみ
  // sheet.clearFormats();  // 書式のみ
  // sheet.clear();         // すべてクリア
}
```

### 08-05 セル範囲を操作する - Rangeクラス

```javascript
function rangeClassDemo() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // 範囲の取得（様々な方法）
  const singleCell = sheet.getRange("B3");
  const byRowCol  = sheet.getRange(3, 2);           // 行番号, 列番号
  const multiCell = sheet.getRange("A1:C5");
  const bySize    = sheet.getRange(1, 1, 5, 3);     // 行, 列, 行数, 列数

  // 値の読み書き
  singleCell.setValue("こんにちは");
  const val = singleCell.getValue();
  Logger.log("値: " + val);

  // 複数セルを一括で読み書き（配列で高速化）
  const data = [
    ["商品A", 100, 50],
    ["商品B", 200, 30],
    ["商品C", 150, 80]
  ];
  sheet.getRange(2, 1, data.length, data[0].length).setValues(data);
  const readData = sheet.getRange(2, 1, 3, 3).getValues();
  Logger.log(JSON.stringify(readData));

  // 書式設定
  const headerRange = sheet.getRange("A1:C1");
  headerRange.setBackground("#1a237e");     // 背景色
  headerRange.setFontColor("#ffffff");       // 文字色
  headerRange.setFontWeight("bold");         // 太字
  headerRange.setFontSize(12);              // フォントサイズ
  headerRange.setHorizontalAlignment("center"); // 中央揃え

  // 数式の設定
  sheet.getRange("D2").setFormula("=B2*C2");
  sheet.getRange("D2:D" + (data.length + 1)).setFormulaR1C1("=RC[-2]*RC[-1]");

  // 範囲の情報
  Logger.log("行数: " + multiCell.getNumRows());
  Logger.log("列数: " + multiCell.getNumColumns());
  Logger.log("A1表記: " + multiCell.getA1Notation());
}
```

### 08-06 配列を使ったデータ処理

```javascript
function batchProcessDemo() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // ❌ 遅い方法（ループの中でgetValue/setValueを繰り返す）
  // for (let r = 2; r <= 100; r++) {
  //   const val = sheet.getRange(r, 1).getValue();
  //   sheet.getRange(r, 2).setValue(val * 1.1);
  // }

  // ✅ 速い方法（一括取得 → 処理 → 一括書き込み）
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  // 1回のAPIコールでA列全体を取得
  const values = sheet.getRange(2, 1, lastRow - 1, 1).getValues();

  // 処理（配列の操作はメモリ上なので高速）
  const results = values.map(([val]) => {
    if (!val || isNaN(val)) return [""];
    return [Math.round(val * 1.1)]; // 10%増しにして整数化
  });

  // 1回のAPIコールでB列全体に書き込む
  sheet.getRange(2, 2, results.length, 1).setValues(results);
  Logger.log(results.length + "行を処理しました");
}
```

### 08-07 カスタム関数

```javascript
/**
 * 税込み金額を計算します（スプレッドシート関数として使用可能）
 * @param {number} price 税抜き価格
 * @param {number} [taxRate=0.1] 税率（デフォルト10%）
 * @return {number} 税込み価格
 * @customfunction
 */
function TAX(price, taxRate) {
  taxRate = taxRate || 0.1;
  if (typeof price !== "number") return "ERROR: 数値を入力してください";
  return Math.ceil(price * (1 + taxRate));
}

/**
 * 名前をフルネームに変換します
 * @param {string} lastName 姓
 * @param {string} firstName 名
 * @return {string} フルネーム（姓 名）
 * @customfunction
 */
function FULLNAME(lastName, firstName) {
  return (lastName + " " + firstName).trim();
}

// スプレッドシート上で =TAX(1000) → 1100
// スプレッドシート上で =FULLNAME("田中","太郎") → "田中 太郎"
```

### 演習問題 第8章
スプレッドシートの「売上データ」シートに A列:日付 B列:担当者名 C列:売上金額 が100行あるとします。以下の処理を一括処理（配列）で実装してください。
1. C列の売上金額の合計・平均をD1・D2セルに表示
2. B列の担当者ごとに合計売上を集計し、「集計」シートのA列:担当者名、B列:合計売上 に書き出す
3. 集計シートのデータを金額の降順にソートする

---

## 技術リファレンス編 第9章 Gmail
Duration: 0:30:00

### 09-01 Gmailサービス
`GmailApp` は Gmailの操作全般を担うサービスです。メールの送受信、下書き、ラベル、スレッドを操作できます。

```javascript
function gmailServiceOverview() {
  // 受信トレイのスレッド数を確認
  const threads = GmailApp.getInboxThreads();
  Logger.log("受信トレイのスレッド数: " + threads.length);

  // 未読メールの件数
  const unreadThreads = GmailApp.search("is:unread");
  Logger.log("未読スレッド数: " + unreadThreads.length);
}
```

### 09-02 GmailAppクラス

```javascript
function gmailAppDemo() {
  // メールを送信
  GmailApp.sendEmail(
    "recipient@example.com",
    "テストメール",
    "これはGASから送信したメールです。",
    {
      name: "GAS自動送信",          // 送信者表示名
      cc: "cc@example.com",          // CC
      bcc: "bcc@example.com",        // BCC
      replyTo: "reply@example.com",  // 返信先
      htmlBody: "<b>HTML形式</b>のメールです。<br>GASから送信しました。"
    }
  );

  // 下書きを作成
  const draft = GmailApp.createDraft(
    "manager@example.com",
    "【週次報告】" + Utilities.formatDate(new Date(), "JST", "M月d日"),
    "報告内容をここに記述します。"
  );
  Logger.log("下書き作成: " + draft.getId());

  // メールを検索
  const searchResults = GmailApp.search("label:重要 after:2026/01/01", 0, 10);
  Logger.log("検索結果: " + searchResults.length + "件");
}
```

### 09-03 スレッドを取得する

```javascript
function getThreadsDemo() {
  // 受信トレイから10件取得
  const threads = GmailApp.getInboxThreads(0, 10);

  threads.forEach(thread => {
    Logger.log("---");
    Logger.log("件名: " + thread.getFirstMessageSubject());
    Logger.log("メッセージ数: " + thread.getMessageCount());
    Logger.log("未読: " + thread.isUnread());
    Logger.log("最終更新: " + thread.getLastMessageDate());
  });

  // 特定の検索クエリでスレッドを取得
  const importantThreads = GmailApp.search("is:important is:unread");
  Logger.log("重要・未読: " + importantThreads.length + " スレッド");
}
```

### 09-04 スレッドを取り扱う - GmailThreadクラス

```javascript
function threadClassDemo() {
  const threads = GmailApp.getInboxThreads(0, 5);
  if (threads.length === 0) return;

  const thread = threads[0];

  // スレッドの操作
  Logger.log("件名: " + thread.getFirstMessageSubject());
  Logger.log("ラベル: " + thread.getLabels().map(l => l.getName()).join(", "));

  // スレッドにスターを付ける
  // thread.markImportant();
  // thread.addLabel(GmailApp.getUserLabelByName("処理済み"));

  // スレッドをゴミ箱へ
  // thread.moveToTrash();

  // スレッドをアーカイブ
  // thread.moveToArchive();
}
```

### 09-05 メッセージを取得する

```javascript
function getMessagesDemo() {
  const threads = GmailApp.getInboxThreads(0, 3);
  threads.forEach(thread => {
    const messages = thread.getMessages();
    Logger.log("=== スレッド: " + thread.getFirstMessageSubject() + " ===");
    messages.forEach(msg => {
      Logger.log("  差出人: " + msg.getFrom());
      Logger.log("  本文（先頭100文字）: " + msg.getPlainBody().slice(0, 100));
    });
  });
}
```

### 09-06 メッセージを取り扱う - GmailMessageクラス

```javascript
function messageClassDemo() {
  const threads = GmailApp.getInboxThreads(0, 1);
  if (!threads.length) return;

  const message = threads[0].getMessages()[0];

  // メッセージ情報の取得
  Logger.log("差出人: " + message.getFrom());
  Logger.log("宛先: " + message.getTo());
  Logger.log("件名: " + message.getSubject());
  Logger.log("日時: " + message.getDate());
  Logger.log("未読: " + message.isUnread());
  Logger.log("スター: " + message.isStarred());

  // 本文の取得
  const plainBody = message.getPlainBody();
  const htmlBody = message.getBody();
  Logger.log("プレーンテキスト: " + plainBody.slice(0, 200));

  // 添付ファイルの処理
  const attachments = message.getAttachments();
  attachments.forEach(att => {
    Logger.log("添付: " + att.getName() + " (" + att.getSize() + " bytes)");
    // Driveに保存する場合
    // DriveApp.getRootFolder().createFile(att);
  });

  // 返信する
  // message.reply("承知しました。確認します。");

  // 既読にする
  // message.markRead();
}
```

### 演習問題 第9章
GmailApp.search() を使って「subject:請求書」で検索し、見つかったスレッドのメッセージについて、差出人・件名・日付・添付ファイル名をスプレッドシートの「Gmailログ」シートに書き出す `logInvoiceEmails()` 関数を作成してください。

---

## 技術リファレンス編 第10章 ドライブ
Duration: 0:30:00

### 10-01 Driveサービス
`DriveApp` はGoogleドライブのファイル・フォルダを操作するサービスです。

```javascript
function driveServiceOverview() {
  const root = DriveApp.getRootFolder();
  Logger.log("ルートフォルダ名: " + root.getName());
  Logger.log("ルートフォルダID: " + root.getId());

  // 使用中のストレージ（バイト）
  Logger.log("使用ストレージ: " + DriveApp.getStorageUsed() + " bytes");
  Logger.log("合計ストレージ: " + DriveApp.getStorageLimit() + " bytes");
}
```

### 10-02 DriveAppクラス

```javascript
function driveAppDemo() {
  // ファイル・フォルダをIDで取得
  // const file = DriveApp.getFileById("ファイルID");
  // const folder = DriveApp.getFolderById("フォルダID");

  // 名前で検索
  const files = DriveApp.getFilesByName("報告書.pdf");
  while (files.hasNext()) {
    const f = files.next();
    Logger.log("ファイル名: " + f.getName() + " URL: " + f.getUrl());
  }

  // テキストファイルをドライブに作成
  const newFile = DriveApp.createFile("テスト.txt", "GASで作成したファイルです", MimeType.PLAIN_TEXT);
  Logger.log("作成: " + newFile.getName() + " / " + newFile.getUrl());

  // 後始末
  newFile.setTrashed(true);
}
```

### 10-03 フォルダを操作する - Folderクラス

```javascript
function folderClassDemo() {
  const root = DriveApp.getRootFolder();

  // フォルダの作成
  const folder = root.createFolder("GAS_作業フォルダ");
  Logger.log("フォルダ作成: " + folder.getName());

  // サブフォルダの作成
  const subFolder = folder.createFolder("2026年");
  subFolder.createFolder("04月");

  // フォルダ内のファイル一覧
  folder.createFile("sample.txt", "サンプル内容", MimeType.PLAIN_TEXT);
  const files = folder.getFiles();
  while (files.hasNext()) {
    Logger.log("ファイル: " + files.next().getName());
  }

  // フォルダの移動・コピー
  Logger.log("フォルダURL: " + folder.getUrl());

  // 後始末
  folder.setTrashed(true);
}
```

### 10-04 ファイルを操作する - Fileクラス

```javascript
function fileClassDemo() {
  // テキストファイルを作成
  const file = DriveApp.createFile(
    "gas_report.txt",
    "GASで生成したレポートです。\n作成日時: " + new Date().toString(),
    MimeType.PLAIN_TEXT
  );

  // ファイルの情報
  Logger.log("名前: " + file.getName());
  Logger.log("ID: " + file.getId());
  Logger.log("URL: " + file.getUrl());
  Logger.log("サイズ: " + file.getSize() + " bytes");
  Logger.log("MIMEタイプ: " + file.getMimeType());
  Logger.log("作成日: " + file.getDateCreated());
  Logger.log("更新日: " + file.getLastUpdated());
  Logger.log("オーナー: " + file.getOwner().getEmail());

  // ファイルの操作
  file.setName("gas_report_renamed.txt");
  file.setDescription("GASで自動生成されたレポート");
  const newFile = file.makeCopy("gas_report_copy.txt");

  // コンテンツの読み込み
  const content = file.getBlob().getDataAsString();
  Logger.log("内容: " + content);

  // 後始末
  file.setTrashed(true);
  newFile.setTrashed(true);
}
```

### 10-05 フォルダ・ファイルのコレクションを操作する

```javascript
function collectionDemo() {
  const root = DriveApp.getRootFolder();

  // ファイルのイテレーション
  const allFiles = root.getFiles();
  const fileList = [];
  while (allFiles.hasNext()) {
    const f = allFiles.next();
    fileList.push({ name: f.getName(), size: f.getSize(), url: f.getUrl() });
  }
  Logger.log("ルートのファイル数: " + fileList.length);

  // フォルダのイテレーション
  const allFolders = root.getFolders();
  while (allFolders.hasNext()) {
    const folder = allFolders.next();
    Logger.log("フォルダ: " + folder.getName());
  }

  // 検索でファイルを取得
  const query = "mimeType='application/pdf' and modifiedTime > '2026-01-01'";
  const pdfFiles = DriveApp.searchFiles(query);
  while (pdfFiles.hasNext()) {
    const pdf = pdfFiles.next();
    Logger.log("PDF: " + pdf.getName());
  }
}
```

### 10-06 フォルダ・ファイルの共有と権限を操作する

```javascript
function sharingDemo() {
  const file = DriveApp.createFile("共有テスト.txt", "共有のテスト", MimeType.PLAIN_TEXT);

  // 特定ユーザーに編集権限を付与
  file.addEditor("editor@example.com");

  // 特定ユーザーに閲覧権限を付与
  file.addViewer("viewer@example.com");

  // リンクを知っている全員が閲覧可能にする
  file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
  Logger.log("共有URL: " + file.getUrl());

  // 権限の確認
  Logger.log("アクセスタイプ: " + file.getSharingAccess());
  Logger.log("権限: " + file.getSharingPermission());

  // エディター・ビューワーの一覧
  file.getEditors().forEach(e => Logger.log("編集者: " + e.getEmail()));
  file.getViewers().forEach(v => Logger.log("閲覧者: " + v.getEmail()));

  // 権限を削除
  file.removeEditor("editor@example.com");

  // 後始末
  file.setTrashed(true);
}
```

### 演習問題 第10章
スプレッドシートのA列にファイル名のリストがある状態で、Googleドライブの「レポート置き場」というフォルダ内で各ファイルを検索し、見つかった場合はB列にそのファイルのURL、C列にファイルサイズ（KB）を書き出す `findFilesFromSheet()` 関数を作成してください。



---

## 技術リファレンス編 第11章 カレンダー
Duration: 0:25:00

### 11-01 Calendarサービス
`CalendarApp` はGoogleカレンダーの操作サービスです。予定の作成・取得・更新・削除が可能です。

```javascript
function calendarServiceOverview() {
  // デフォルトカレンダー（メインカレンダー）を取得
  const defaultCal = CalendarApp.getDefaultCalendar();
  Logger.log("デフォルトカレンダー: " + defaultCal.getName());

  // すべてのカレンダーを取得
  const allCals = CalendarApp.getAllCalendars();
  allCals.forEach(cal => Logger.log("カレンダー: " + cal.getName() + " / " + cal.getId()));

  // IDで特定のカレンダーを取得
  // const calendar = CalendarApp.getCalendarById("カレンダーID");
}
```

### 11-02 CalendarAppクラス

```javascript
function calendarAppDemo() {
  const app = CalendarApp;

  // カレンダーを名前で検索
  const cals = app.getCalendarsByName("仕事");
  if (cals.length > 0) {
    Logger.log("仕事カレンダー: " + cals[0].getId());
  }

  // 新しいカレンダーを作成
  // const newCal = app.createCalendar("プロジェクトX", { timeZone: "Asia/Tokyo" });
  // Logger.log("新規カレンダー: " + newCal.getName());
}
```

### 11-03 カレンダーを操作する - Calendarクラス

```javascript
function calendarClassDemo() {
  const cal = CalendarApp.getDefaultCalendar();

  // カレンダーの情報
  Logger.log("名前: " + cal.getName());
  Logger.log("ID: " + cal.getId());
  Logger.log("タイムゾーン: " + cal.getTimeZone());
  Logger.log("色: " + cal.getColor());

  // イベントの作成
  const now = new Date();
  const oneHourLater = new Date(now.getTime() + 60 * 60 * 1000);

  const event = cal.createEvent(
    "GAS学習ミーティング",
    now,
    oneHourLater,
    {
      description: "GASの学習進捗を共有するミーティングです。",
      location: "会議室A",
      guests: "colleague@example.com",
      sendInvites: false
    }
  );
  Logger.log("作成したイベントID: " + event.getId());

  // 終日イベントの作成
  const allDayEvent = cal.createAllDayEvent(
    "プロジェクト締め切り",
    new Date(2026, 3, 30) // 2026年4月30日（月は0始まり）
  );
  Logger.log("終日イベント: " + allDayEvent.getTitle());

  // 定期イベント（毎週月曜日）
  // cal.createEventSeries("週次MTG", start, end, {
  //   frequency: CalendarApp.EventFrequency.WEEKLY,
  //   daysOfWeek: [CalendarApp.Weekday.MONDAY]
  // });

  // 指定期間のイベントを取得
  const weekEvents = cal.getEvents(now, new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000));
  Logger.log("今週のイベント数: " + weekEvents.length);

  // 後始末
  event.deleteEvent();
  allDayEvent.deleteEvent();
}
```

### 11-04 イベントを操作する - CalendarEventクラス

```javascript
function calendarEventDemo() {
  const cal = CalendarApp.getDefaultCalendar();
  const now = new Date();
  const end = new Date(now.getTime() + 60 * 60 * 1000);

  const event = cal.createEvent("テストイベント", now, end);

  // イベントの情報取得
  Logger.log("タイトル: " + event.getTitle());
  Logger.log("説明: " + event.getDescription());
  Logger.log("場所: " + event.getLocation());
  Logger.log("開始: " + event.getStartTime());
  Logger.log("終了: " + event.getEndTime());
  Logger.log("作成者: " + event.getCreators().join(", "));
  Logger.log("終日イベント: " + event.isAllDayEvent());

  // イベントの更新
  event.setTitle("更新されたイベント");
  event.setDescription("GASで自動作成・更新しました");
  event.setLocation("オンライン（Google Meet）");
  event.setColor(CalendarApp.EventColor.CYAN);

  // ゲストの追加・確認
  // event.addGuest("guest@example.com");
  const guests = event.getGuestList();
  Logger.log("ゲスト数: " + guests.length);

  // リマインダーの設定
  event.addEmailReminder(60);    // 1時間前にメールリマインダー
  event.addPopupReminder(30);    // 30分前にポップアップ
  Logger.log("リマインダー: " + JSON.stringify(event.getPopupReminders()));

  // イベントの削除
  event.deleteEvent();
}
```

### 演習問題 第11章
「今月の予定」をカレンダーから取得してスプレッドシートに書き出す機能を拡張してください。
- A列: 予定タイトル
- B列: 開始日時
- C列: 終了日時
- D列: 場所
- E列: 終日イベントかどうか（TRUE/FALSE）

なお、取得後に「終日イベントのみ表示」と「期間でフィルタ」をシート上で切り替えられるよう、フィルタを設定するコードも追加してください。

---

## 技術リファレンス編 第12章 ドキュメント
Duration: 0:30:00

### 12-01 Documentサービス
`DocumentApp` はGoogleドキュメントを操作するサービスです。

```javascript
function documentServiceOverview() {
  // 新規ドキュメントを作成
  const doc = DocumentApp.create("GAS生成ドキュメント");
  Logger.log("ドキュメントID: " + doc.getId());
  Logger.log("URL: " + doc.getUrl());

  // 後始末
  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 12-02 DocumentAppクラス

```javascript
function documentAppDemo() {
  // IDでドキュメントを開く
  // const doc = DocumentApp.openById("ドキュメントID");

  // アクティブなドキュメント（ドキュメントにバインドされたスクリプトの場合）
  // const doc = DocumentApp.getActiveDocument();

  // 新規作成
  const doc = DocumentApp.create("テストドキュメント");
  Logger.log("名前: " + doc.getName());
  Logger.log("ID: " + doc.getId());

  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 12-03 ドキュメントを操作する - Documentクラス

```javascript
function documentClassDemo() {
  const doc = DocumentApp.create("議事録テンプレート");
  const body = doc.getBody();

  // タイトル・見出しの追加
  body.appendParagraph("2026年4月 定例ミーティング議事録")
    .setHeading(DocumentApp.ParagraphHeading.TITLE);
  body.appendParagraph("開催日時：2026年4月10日（木）14:00〜15:00")
    .setHeading(DocumentApp.ParagraphHeading.HEADING2);

  // 本文段落の追加
  body.appendParagraph("参加者：田中、山田、佐藤");
  body.appendParagraph(""); // 空行

  // リスト（箇条書き）
  body.appendParagraph("議題").setHeading(DocumentApp.ParagraphHeading.HEADING2);
  const item1 = body.appendListItem("Q1売上報告");
  item1.setGlyphType(DocumentApp.GlyphType.BULLET);
  const item2 = body.appendListItem("来月の計画について");
  item2.setGlyphType(DocumentApp.GlyphType.BULLET);

  // 水平線を追加
  body.appendHorizontalRule();

  // ドキュメント全体を保存
  doc.saveAndClose();

  Logger.log("議事録を作成しました: " + doc.getUrl());
  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 12-04 セクションを操作する

```javascript
function sectionDemo() {
  const doc = DocumentApp.create("セクションテスト");
  const body = doc.getBody();

  // 段落の取得と操作
  body.appendParagraph("第1段落：はじめに");
  body.appendParagraph("第2段落：概要説明");
  body.appendParagraph("第3段落：まとめ");

  // 要素の数
  Logger.log("要素数: " + body.getNumChildren());

  // インデックスで要素を取得
  const firstChild = body.getChild(0);
  Logger.log("最初の要素タイプ: " + firstChild.getType());

  // 要素の削除
  // body.removeChild(firstChild);

  doc.saveAndClose();
  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 12-05 段落・リストアイテムを操作する

```javascript
function paragraphDemo() {
  const doc = DocumentApp.create("段落テスト");
  const body = doc.getBody();

  // 段落の書式設定
  const para = body.appendParagraph("重要なお知らせ");
  para.setHeading(DocumentApp.ParagraphHeading.HEADING1);
  para.setAlignment(DocumentApp.HorizontalAlignment.CENTER);
  para.setSpacingBefore(12);
  para.setSpacingAfter(6);
  para.setIndentFirstLine(0);

  // 番号付きリスト
  const listItems = ["手順1: ログインする", "手順2: ファイルを開く", "手順3: 編集する"];
  listItems.forEach(text => {
    const item = body.appendListItem(text);
    item.setGlyphType(DocumentApp.GlyphType.NUMBER);
    item.setNestingLevel(0);
  });

  doc.saveAndClose();
  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 12-06 テキストオブジェクトを操作する

```javascript
function textObjectDemo() {
  const doc = DocumentApp.create("テキスト書式テスト");
  const body = doc.getBody();

  const para = body.appendParagraph("このテキストには様々な書式が適用されています。");
  const text = para.editAsText();

  // 部分的な書式設定（文字オフセット指定）
  text.setBold(0, 5, true);             // 0〜5文字目を太字
  text.setItalic(7, 12, true);          // 7〜12文字目をイタリック
  text.setUnderline(14, 20, true);      // 14〜20文字目に下線
  text.setForegroundColor(22, 28, "#e53935"); // 赤色
  text.setFontSize(0, 5, 16);           // 最初の6文字をフォントサイズ16に

  doc.saveAndClose();
  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 12-07 文字列の編集と書式設定

```javascript
function textEditDemo() {
  const doc = DocumentApp.create("文字列編集テスト");
  const body = doc.getBody();

  const para = body.appendParagraph("初期テキストです。");

  // テキストの追加・挿入
  para.appendText("\n追記されたテキストです。");

  // 段落のテキスト全体に書式を適用
  const text = para.editAsText();
  text.setFontFamily("Noto Sans JP");
  text.setFontSize(11);

  doc.saveAndClose();
  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 12-08 文字列の置換と検索

```javascript
function findReplaceDemo() {
  const doc = DocumentApp.create("置換テスト");
  const body = doc.getBody();

  body.appendParagraph("こんにちは、{{NAME}}さん。");
  body.appendParagraph("本日の日付は {{DATE}} です。");
  body.appendParagraph("プロジェクト: {{PROJECT}}");

  // プレースホルダーを実際の値で置換
  const replacements = {
    "{{NAME}}": "田中太郎",
    "{{DATE}}": Utilities.formatDate(new Date(), "JST", "yyyy年MM月dd日"),
    "{{PROJECT}}": "GAS自動化プロジェクト"
  };

  Object.entries(replacements).forEach(([placeholder, value]) => {
    body.replaceText(placeholder, value);
  });

  // 検索して書式を適用
  const search = body.findText("GAS自動化");
  if (search) {
    search.getElement().editAsText()
      .setBold(search.getStartOffset(), search.getEndOffsetInclusive(), true)
      .setForegroundColor(search.getStartOffset(), search.getEndOffsetInclusive(), "#1565c0");
  }

  doc.saveAndClose();
  DriveApp.getFileById(doc.getId()).setTrashed(true);
}
```

### 演習問題 第12章
スプレッドシートの「社員情報」シート（A列:氏名 B列:部署 C列:入社年）のデータを読み込み、各社員ごとに「社員証明書テンプレート」ドキュメントのコピーを作成して `{{NAME}}`, `{{DEPT}}`, `{{YEAR}}` をプレースホルダーとして置換し、指定のドライブフォルダに保存する `generateCertificates()` 関数を作成してください。

---

## 技術リファレンス編 第13章 スライド
Duration: 0:25:00

### 13-01 Slidesサービス

```javascript
function slidesServiceOverview() {
  // 新規プレゼンテーション作成
  const pres = SlidesApp.create("GASプレゼン");
  Logger.log("プレゼンID: " + pres.getId());
  Logger.log("URL: " + pres.getUrl());

  DriveApp.getFileById(pres.getId()).setTrashed(true);
}
```

### 13-02 SlidesAppクラス

```javascript
function slidesAppDemo() {
  // IDで既存のプレゼンを開く
  // const pres = SlidesApp.openById("プレゼンID");

  const pres = SlidesApp.create("テストプレゼン");
  Logger.log("名前: " + pres.getName());
  Logger.log("スライド数: " + pres.getSlides().length);

  DriveApp.getFileById(pres.getId()).setTrashed(true);
}
```

### 13-03 プレゼンテーションを操作する - Presentationクラス

```javascript
function presentationClassDemo() {
  const pres = SlidesApp.create("月次レポート");

  // スライドの追加
  const slide1 = pres.getSlides()[0]; // 最初のスライド
  const slide2 = pres.appendSlide(SlidesApp.PredefinedLayout.TITLE_AND_BODY);
  const slide3 = pres.appendSlide(SlidesApp.PredefinedLayout.BLANK);

  Logger.log("スライド数: " + pres.getSlides().length);
  Logger.log("スライドの幅: " + pres.getPageWidth() + " EMU");

  // スライドに一括テキスト置換
  pres.replaceAllText("{{MONTH}}", "4月");
  pres.replaceAllText("{{YEAR}}", "2026");

  // 保存
  pres.saveAndClose();

  DriveApp.getFileById(pres.getId()).setTrashed(true);
}
```

### 13-04 スライドを操作する - Slideクラス

```javascript
function slideClassDemo() {
  const pres = SlidesApp.create("スライド操作テスト");
  const slide = pres.getSlides()[0];

  // スライドのレイアウトを変更
  // slide.applyLayout(pres.getLayouts()[0]);

  // スライドにテキストボックスを追加
  const textBox = slide.insertTextBox("Hello, Slides API!", 100, 100, 400, 100);
  textBox.getText().getTextStyle().setBold(true).setFontSize(24);

  // スライドに図形を追加
  const shape = slide.insertShape(SlidesApp.ShapeType.RECTANGLE, 50, 50, 200, 100);
  shape.getFill().setSolidFill("#1a237e");
  shape.getText().appendText("GAS").getTextStyle()
    .setForegroundColor("#ffffff")
    .setFontSize(32)
    .setBold(true);

  // スプレッドシートのチャートを埋め込む（事前にチャートが必要）
  // const ss = SpreadsheetApp.openById("スプレッドシートID");
  // const chart = ss.getSheets()[0].getCharts()[0];
  // slide.insertSheetsChart(chart);

  pres.saveAndClose();
  DriveApp.getFileById(pres.getId()).setTrashed(true);
}
```

### 13-05 ページ要素を操作する

```javascript
function pageElementDemo() {
  const pres = SlidesApp.create("ページ要素テスト");
  const slide = pres.getSlides()[0];

  // テキストボックスを追加
  slide.insertTextBox("要素1", 50, 50, 200, 50);
  slide.insertTextBox("要素2", 300, 50, 200, 50);

  // ページ要素の一覧
  const elements = slide.getPageElements();
  elements.forEach((el, i) => {
    Logger.log("要素 " + i + ": タイプ=" + el.getPageElementType());
    Logger.log("  位置: left=" + el.getLeft() + " top=" + el.getTop());
    Logger.log("  サイズ: w=" + el.getWidth() + " h=" + el.getHeight());
  });

  // 要素を選択・変換
  const firstEl = elements[0];
  firstEl.setLeft(100);
  firstEl.setTop(200);

  pres.saveAndClose();
  DriveApp.getFileById(pres.getId()).setTrashed(true);
}
```

### 13-06 テキスト範囲と文字列の操作

```javascript
function slideTextDemo() {
  const pres = SlidesApp.create("テキスト操作テスト");
  const slide = pres.getSlides()[0];

  const box = slide.insertTextBox("", 50, 50, 600, 300);
  const textRange = box.getText();

  // テキストの追加と書式設定
  const para1 = textRange.appendParagraph("2026年4月 月次報告");
  para1.getRange().getTextStyle()
    .setBold(true)
    .setFontSize(20)
    .setForegroundColor("#1a237e");

  textRange.appendParagraph(""); // 空行
  textRange.appendParagraph("売上: ¥1,250,000（前月比 +8.3%）")
    .getRange().getTextStyle().setFontSize(14);

  pres.saveAndClose();
  DriveApp.getFileById(pres.getId()).setTrashed(true);
}
```

### 演習問題 第13章
スプレッドシートの「月次KPI」シート（A列:指標名 B列:目標値 C列:実績値 D列:達成率）を読み込み、Googleスライドのテンプレートの各スライドへデータを流し込む `generateKPISlides()` 関数を作成してください。達成率が100%以上の場合は緑色、未達の場合は赤色でテキストを表示してください。



---

## 技術リファレンス編 第14章 フォーム
Duration: 0:25:00

### 14-01 Formsサービス

```javascript
function formsServiceOverview() {
  // 新規フォームを作成
  const form = FormApp.create("アンケートフォーム");
  Logger.log("フォームURL: " + form.getPublishedUrl());
  Logger.log("フォームID: " + form.getId());

  // 後始末
  DriveApp.getFileById(form.getId()).setTrashed(true);
}
```

### 14-02 FormAppクラス

```javascript
function formAppDemo() {
  // IDでフォームを開く
  // const form = FormApp.openById("フォームID");

  // 新規作成して設定
  const form = FormApp.create("参加申込フォーム");
  form.setTitle("GAS勉強会 参加申込");
  form.setDescription("参加希望の方は以下のフォームにご記入ください。");
  form.setConfirmationMessage("ご応募ありがとうございます。後日ご連絡いたします。");
  form.setAllowResponseEdits(true);    // 回答の編集を許可
  form.setLimitOneResponsePerUser(true); // 1ユーザー1回

  Logger.log("フォームURL: " + form.getPublishedUrl());
  Logger.log("編集URL: " + form.getEditUrl());

  DriveApp.getFileById(form.getId()).setTrashed(true);
}
```

### 14-03 フォームを操作する - Formクラス

```javascript
function formClassDemo() {
  const form = FormApp.create("イベント申込");

  // テキスト入力（短文）
  const nameItem = form.addTextItem();
  nameItem.setTitle("お名前").setRequired(true);

  // テキスト入力（長文）
  const commentItem = form.addParagraphTextItem();
  commentItem.setTitle("ご要望・コメント").setRequired(false);

  // ラジオボタン（単一選択）
  const roleItem = form.addMultipleChoiceItem();
  roleItem.setTitle("ご所属")
    .setChoiceValues(["会社員", "学生", "フリーランス", "その他"])
    .setRequired(true);

  // チェックボックス（複数選択）
  const topicItem = form.addCheckboxItem();
  topicItem.setTitle("興味のあるトピック（複数可）")
    .setChoiceValues(["GAS基礎", "スプレッドシート自動化", "Gmail連携", "API連携"]);

  // ドロップダウン
  const timeItem = form.addListItem();
  timeItem.setTitle("希望参加時間")
    .setChoices([
      timeItem.createChoice("午前の部（10:00〜12:00）"),
      timeItem.createChoice("午後の部（14:00〜16:00）"),
      timeItem.createChoice("どちらでも可")
    ]);

  // 日付入力
  const dateItem = form.addDateItem();
  dateItem.setTitle("都合の良い日程").setRequired(true);

  // セクション区切り
  form.addSectionHeaderItem().setTitle("確認事項");

  // 線形尺度
  const satisfactionItem = form.addScaleItem();
  satisfactionItem.setTitle("過去のイベントへの満足度")
    .setBounds(1, 5)
    .setLabels("とても不満", "とても満足");

  Logger.log("フォーム作成完了: " + form.getPublishedUrl());
  Logger.log("アイテム数: " + form.getItems().length);

  DriveApp.getFileById(form.getId()).setTrashed(true);
}
```

### 14-04 アイテムを操作する

```javascript
function formItemDemo() {
  const form = FormApp.create("アイテム操作テスト");

  // アイテムを追加
  form.addTextItem().setTitle("名前");
  form.addMultipleChoiceItem().setTitle("性別")
    .setChoiceValues(["男性", "女性", "回答しない"]);

  // 既存アイテムの取得と操作
  const items = form.getItems();
  items.forEach(item => {
    Logger.log("アイテム: " + item.getTitle() + " タイプ: " + item.getType());
  });

  // フォームの回答を取得
  const responses = form.getResponses();
  Logger.log("回答数: " + responses.length);

  // 送信後の回答シートを設定
  // form.setDestination(FormApp.DestinationType.SPREADSHEET, "スプレッドシートID");

  DriveApp.getFileById(form.getId()).setTrashed(true);
}
```

### 演習問題 第14章
「社内研修申込フォーム」をGASで作成してください。フォームには以下のアイテムを含めてください。
- 氏名（テキスト、必須）
- 所属部署（ドロップダウン：総務、営業、開発、その他）
- 希望研修日（日付）
- 参加動機（段落テキスト）
- 事前スキル（チェックボックス：GAS初心者、JavaScript経験あり、GASスクリプト経験あり）
- 満足度評価（線形尺度 1〜5）
フォームを作成したあと、フォームIDとURLをスプレッドシートのA1・B1セルに書き出してください。

---

## 技術リファレンス編 第15章 翻訳
Duration: 0:10:00

### 15-01 LanguageサービスとLanguageAppクラス

```javascript
function languageDemo() {
  // テキストを翻訳
  const english = LanguageApp.translate("こんにちは、世界！", "ja", "en");
  Logger.log("英訳: " + english); // "Hello, World!"

  const french = LanguageApp.translate("I love Google Apps Script", "en", "fr");
  Logger.log("仏訳: " + french);

  const detected = LanguageApp.translate("GAS は素晴らしい", "auto", "en");
  Logger.log("自動検出→英語: " + detected);

  // スプレッドシートのデータを一括翻訳
  function translateSheet() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const lastRow = sheet.getLastRow();
    if (lastRow < 2) return;

    const sourceData = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
    const translated = sourceData.map(([text]) => {
      if (!text) return [""];
      const result = LanguageApp.translate(String(text), "ja", "en");
      Utilities.sleep(200); // APIレート制限対策
      return [result];
    });

    sheet.getRange(2, 2, translated.length, 1).setValues(translated);
    Logger.log("翻訳完了: " + translated.length + "件");
  }
  translateSheet();
}
```

### 演習問題 第15章
スプレッドシートのA列に日本語テキストが入っているとき、B列に英語翻訳・C列に中国語翻訳（簡体字）・D列にフランス語翻訳を一括で書き出す `multiTranslate()` 関数を作成してください。APIコール過多によるエラーを防ぐため `Utilities.sleep()` を適切に挿入してください。

---

## 技術リファレンス編 第16章 Baseサービス
Duration: 0:15:00

### 16-01 Baseサービスとは
BaseサービスはGASのコア機能（ログ・セッション・ユーザー情報など）を提供します。

```javascript
function baseServiceOverview() {
  // Loggerクラス（クラシックログ）
  Logger.log("Logger is part of Base Service");

  // consoleオブジェクト（V8エンジン以降）
  console.log("console.log");
  console.info("console.info");
  console.warn("console.warn");
  console.error("console.error");

  // ログの取得（実行後に取得できる）
  const logs = Logger.getLog();
  Logger.log("ログ内容の長さ: " + logs.length);
}
```

### 16-02 ログ

```javascript
function loggingDemo() {
  // 構造化ログ（JSON形式で出力すると読みやすい）
  const user = { name: "田中", role: "admin" };
  console.log("ユーザー情報:", JSON.stringify(user));

  // タイムスタンプ付きログ
  function logWithTime(message) {
    const ts = Utilities.formatDate(new Date(), "JST", "HH:mm:ss.SSS");
    Logger.log("[" + ts + "] " + message);
  }
  logWithTime("バッチ処理開始");
  Utilities.sleep(500);
  logWithTime("データ取得完了");
  logWithTime("バッチ処理終了");

  // エラーログをGmailで通知（本番環境向け）
  function sendErrorLog(funcName, error) {
    const subject = "【GASエラー】" + funcName;
    const body = [
      "エラー名: " + error.name,
      "メッセージ: " + error.message,
      "スタック: " + error.stack,
      "発生時刻: " + new Date().toString()
    ].join("\n");
    // GmailApp.sendEmail("admin@example.com", subject, body);
    Logger.log(body);
  }
  try {
    throw new Error("テストエラー");
  } catch(e) {
    sendErrorLog("loggingDemo", e);
  }
}
```

### 16-03 セッションとユーザー

```javascript
function sessionAndUserDemo() {
  // 実行ユーザー（スクリプトを実行している人）
  const activeUser = Session.getActiveUser();
  Logger.log("実行ユーザー: " + activeUser.getEmail());

  // 有効ユーザー（トリガー実行時は所有者になる場合がある）
  const effectiveUser = Session.getEffectiveUser();
  Logger.log("有効ユーザー: " + effectiveUser.getEmail());

  // スクリプトの一時キー（セッション内でユニーク）
  const tempKey = Session.getTemporaryActiveUserKey();
  Logger.log("一時キー: " + tempKey);

  // タイムゾーン
  Logger.log("スクリプトタイムゾーン: " + Session.getScriptTimeZone());
}
```

### 演習問題 第16章
GASのトリガーで毎日1回実行するバッチ処理を設計してください。実行開始・終了のログを記録し、エラーが発生した場合は管理者メール（`admin@example.com`）にエラー内容を送信するラッパー関数 `runDailyBatch()` を作成してください。内部で呼び出す処理は `processDailyData()` という別関数として定義してください。

---

## 技術リファレンス編 第17章 ユーザーインターフェース
Duration: 0:25:00

### 17-01 UIの操作とUiクラス
スプレッドシートやドキュメントのメニュー・ダイアログを操作するクラスです。

```javascript
function uiOverview() {
  const ui = SpreadsheetApp.getUi();
  // または DocumentApp.getUi() / SlidesApp.getUi()
  Logger.log("UIクラス取得完了");
}
```

### 17-02 ダイアログ

```javascript
function dialogDemo() {
  const ui = SpreadsheetApp.getUi();

  // 情報ダイアログ（OKボタンのみ）
  ui.alert("処理が完了しました！", ui.ButtonSet.OK);

  // 確認ダイアログ（YES/NOボタン）
  const response = ui.alert(
    "確認",
    "このシートのデータをすべてクリアしますか？",
    ui.ButtonSet.YES_NO
  );
  if (response === ui.Button.YES) {
    Logger.log("YES が押されました");
    // SpreadsheetApp.getActiveSheet().clearContents();
  } else {
    Logger.log("NO または キャンセル が押されました");
  }

  // 入力ダイアログ
  const result = ui.prompt(
    "担当者名を入力してください",
    ui.ButtonSet.OK_CANCEL
  );
  if (result.getSelectedButton() === ui.Button.OK) {
    const name = result.getResponseText();
    Logger.log("入力された名前: " + name);
    SpreadsheetApp.getActiveSheet().getRange("A1").setValue(name);
  }
}
```

### 17-03 メニュー

```javascript
// スプレッドシートが開いたときに自動実行（シンプルトリガー）
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu("🚀 自動化メニュー")
    .addItem("📧 日報メールを下書き作成", "createDraftEmail")
    .addItem("📅 シートをコピー", "copyWeeklySheet")
    .addSeparator()
    .addSubMenu(
      ui.createMenu("📊 レポート")
        .addItem("月次レポートを生成", "generateMonthlyReport")
        .addItem("Slackへ通知", "sendMessageToSlack")
    )
    .addSeparator()
    .addItem("⚙️ 設定", "openSettingsDialog")
    .addToUi();
}

function openSettingsDialog() {
  SpreadsheetApp.getUi().alert("設定画面（今後実装予定）");
}
```

### 17-04 スプレッドシートのUIを拡張する

```javascript
function advancedUiDemo() {
  const ui = SpreadsheetApp.getUi();

  // HTMLダイアログ（リッチなUIを表示）
  const htmlContent = HtmlService.createHtmlOutput(`
    <html>
      <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2>📊 データ設定</h2>
        <p>処理するシート名を入力してください：</p>
        <input type="text" id="sheetName" placeholder="例: 売上データ" style="width:100%;padding:8px;">
        <br><br>
        <button onclick="google.script.host.close()" style="padding:8px 16px;">閉じる</button>
      </body>
    </html>
  `).setWidth(400).setHeight(200);

  ui.showModalDialog(htmlContent, "データ設定");

  // サイドバーを表示
  const sideBar = HtmlService.createHtmlOutput(`
    <html><body>
      <h3>ヘルプ</h3>
      <ul>
        <li>A列に名前を入力</li>
        <li>B列に点数を入力</li>
        <li>メニューから実行</li>
      </ul>
    </body></html>
  `).setTitle("使い方ガイド");
  // ui.showSidebar(sideBar);
}
```

### 演習問題 第17章
スプレッドシートに「自動化ツール」カスタムメニューを追加してください。メニューには「データ集計」「PDFとして書き出し」「管理者に報告」の3つのサブメニューを用意し、それぞれクリックしたときに何の処理が実行されるかを `alert()` で説明するダミー関数を作成してください。「PDFとして書き出し」押下時はシート名を入力するプロンプトを表示し、入力された名前を使って書き出し予定のファイル名を `alert()` で確認してください。

---

## 技術リファレンス編 第18章 ファイルとデータの操作
Duration: 0:20:00

### 18-01 Blobオブジェクト
Blobはバイナリデータ（画像・PDF・CSVなど）を扱うためのオブジェクトです。

```javascript
function blobDemo() {
  // 文字列からBlobを作成
  const text = "GASで生成したCSVデータ\n名前,点数\n田中,85\n山田,72";
  const blob = Utilities.newBlob(text, "text/csv", "results.csv");

  Logger.log("名前: " + blob.getName());
  Logger.log("MIMEタイプ: " + blob.getContentType());
  Logger.log("サイズ: " + blob.getBytes().length + " bytes");
  Logger.log("内容: " + blob.getDataAsString());

  // BlobをGoogleドライブに保存
  const file = DriveApp.createFile(blob);
  Logger.log("保存完了: " + file.getUrl());

  // スプレッドシートをPDFとして取得（Blob形式）
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const url = ss.getUrl().replace("/edit", "/export?format=pdf&portrait=true&size=A4");
  // const pdfBlob = UrlFetchApp.fetch(url, { headers: { Authorization: "Bearer " + ScriptApp.getOAuthToken() } }).getBlob();
  // pdfBlob.setName("report.pdf");
  // DriveApp.createFile(pdfBlob);

  file.setTrashed(true);
}
```

### 18-02 添付ファイルを操作する

```javascript
function attachmentDemo() {
  // Gmailの添付ファイルをドライブに保存する
  function saveAttachmentsToDrive() {
    const threads = GmailApp.search("has:attachment subject:報告書 newer_than:7d");
    const folder = DriveApp.createFolder("添付ファイル_" +
      Utilities.formatDate(new Date(), "JST", "yyyyMMdd"));

    threads.forEach(thread => {
      thread.getMessages().forEach(msg => {
        msg.getAttachments().forEach(att => {
          const file = folder.createFile(att);
          Logger.log("保存: " + file.getName() + " (" + file.getSize() + " bytes)");
        });
      });
    });
    Logger.log("フォルダ: " + folder.getUrl());
  }
  saveAttachmentsToDrive();

  // メール送信時の添付ファイル
  function sendWithAttachment() {
    // Blobからファイルを作成してメールに添付
    const data = [["名前","スコア"],["田中",90],["山田",75]];
    const csvContent = data.map(row => row.join(",")).join("\n");
    const csvBlob = Utilities.newBlob(csvContent, "text/csv", "scores.csv");

    GmailApp.sendEmail(
      "recipient@example.com",
      "スコア一覧をお送りします",
      "添付ファイルをご確認ください。",
      { attachments: [csvBlob] }
    );
  }
}
```

### 演習問題 第18章
スプレッドシートの「請求書データ」シート（A:顧客名 B:金額 C:品目）を読み込み、以下を実行する `generateAndSendInvoice()` 関数を作成してください。
1. データをCSV形式のBlobとして生成
2. Googleドライブの「請求書」フォルダに保存
3. 保存したファイルを添付して顧客にメール送信（`customer@example.com` 宛）

---

## 技術リファレンス編 第19章 Utilitiesサービス
Duration: 0:20:00

### 19-01 Utilitiesサービス
Utilitiesサービスは、日付フォーマット・ZIP圧縮・エンコード・ランダム生成などのユーティリティ機能を提供します。

```javascript
function utilitiesOverview() {
  // スリープ（ミリ秒単位）
  Logger.log("処理開始");
  Utilities.sleep(1000); // 1秒待機
  Logger.log("1秒後");

  // ランダムバイト列を生成（セキュアなトークン生成に利用）
  const randomBytes = Utilities.getUuid();
  Logger.log("UUID: " + randomBytes);

  // Base64エンコード・デコード
  const text = "Hello, GAS!";
  const encoded = Utilities.base64Encode(text);
  const decoded = Utilities.base64DecodeWebSafe(encoded);
  Logger.log("エンコード: " + encoded);
  Logger.log("デコード: " + Utilities.newBlob(decoded).getDataAsString());
}
```

### 19-02 ZIPファイルとCSVファイル

```javascript
function zipAndCsvDemo() {
  // 複数ファイルをZIP圧縮
  const file1 = Utilities.newBlob("ファイル1の内容", "text/plain", "file1.txt");
  const file2 = Utilities.newBlob("ファイル2の内容", "text/plain", "file2.txt");
  const zipBlob = Utilities.zip([file1, file2], "archive.zip");

  const zipFile = DriveApp.createFile(zipBlob);
  Logger.log("ZIP作成: " + zipFile.getName() + " / " + zipFile.getUrl());

  // ZIPを展開
  const unzipped = Utilities.unzip(zipBlob);
  unzipped.forEach(b => Logger.log("展開: " + b.getName()));

  // CSVデータを2次元配列に変換
  const csvData = "名前,年齢,部署\n田中,30,営業\n山田,25,開発\n佐藤,35,総務";
  const parsed = Utilities.parseCsv(csvData);
  Logger.log("CSV行数: " + parsed.length);
  parsed.forEach(row => Logger.log(row.join(" | ")));

  // 区切り文字を指定してパース（タブ区切り）
  const tsvData = "田中\t30\t営業";
  const tsvParsed = Utilities.parseCsv(tsvData, "\t");
  Logger.log(JSON.stringify(tsvParsed));

  zipFile.setTrashed(true);
}
```

### 19-03 日時を文字列化する

```javascript
function dateFormattingDemo() {
  const now = new Date();

  // よく使うフォーマットパターン
  const formats = [
    "yyyy/MM/dd",
    "yyyy年MM月dd日",
    "yyyyMMdd",
    "HH:mm:ss",
    "yyyy/MM/dd HH:mm:ss",
    "EEE, MMM d, yyyy",   // "Thu, Apr 10, 2026"
    "M月d日（E）"          // "4月10日（木）"
  ];

  formats.forEach(fmt => {
    Logger.log(fmt + " → " + Utilities.formatDate(now, "JST", fmt));
  });

  // UTCとJSTの使い分け
  Logger.log("JST: " + Utilities.formatDate(now, "Asia/Tokyo", "yyyy/MM/dd HH:mm:ss"));
  Logger.log("UTC: " + Utilities.formatDate(now, "UTC", "yyyy/MM/dd HH:mm:ss"));
  Logger.log("PST: " + Utilities.formatDate(now, "America/Los_Angeles", "yyyy/MM/dd HH:mm:ss"));
}
```

### 演習問題 第19章
スプレッドシートの「月次データ」シート全体を以下の処理で加工してください。
1. シートのデータをCSV文字列に変換する
2. CSV文字列を `text/csv` BlobとしてZIPに圧縮する
3. ZIPファイルを「バックアップ_YYYYMMDD.zip」という名前でドライブに保存する
4. 処理完了をトースト通知で表示する

---

## 技術リファレンス編 第20章 プロパティサービス
Duration: 0:20:00

### 20-01 プロパティストア
プロパティサービスは、スクリプト・ドキュメント・ユーザーの設定値（APIキーや設定情報）をクラウド上に永続保存するためのKVSです。

| ストア | スコープ | 用途 |
|---|---|---|
| ScriptProperties | スクリプト単位・全ユーザー共有 | APIキー・共通設定 |
| UserProperties | スクリプト単位・ユーザー別 | ユーザーの個人設定 |
| DocumentProperties | ドキュメント単位・全ユーザー | ドキュメント固有の設定 |

### 20-02 PropertiesサービスとPropertiesServiceクラス

```javascript
function propertiesServiceDemo() {
  // スクリプトプロパティ（最も多く使われる）
  const scriptProps = PropertiesService.getScriptProperties();

  // ユーザープロパティ
  const userProps = PropertiesService.getUserProperties();

  // ドキュメントプロパティ（ドキュメントバインドスクリプトのみ）
  // const docProps = PropertiesService.getDocumentProperties();

  Logger.log("ScriptProps keys: " + JSON.stringify(scriptProps.getKeys()));
  Logger.log("UserProps keys: " + JSON.stringify(userProps.getKeys()));
}
```

### 20-03 Propertiesクラス - プロパティストアの読み書き

```javascript
function propertiesReadWriteDemo() {
  const props = PropertiesService.getScriptProperties();

  // 値の書き込み
  props.setProperty("SLACK_WEBHOOK_URL", "https://hooks.slack.com/...");
  props.setProperty("MAX_ROWS", "1000");
  props.setProperty("LAST_RUN", new Date().toString());

  // 複数のプロパティを一括設定
  props.setProperties({
    "API_KEY": "sk-xxxxxx",
    "DEBUG_MODE": "false",
    "VERSION": "1.2.0"
  });

  // 値の読み込み
  const slackUrl = props.getProperty("SLACK_WEBHOOK_URL");
  const maxRows = Number(props.getProperty("MAX_ROWS"));
  const allProps = props.getProperties(); // すべてのプロパティをオブジェクトで取得
  Logger.log("SLACK_URL: " + slackUrl);
  Logger.log("MAX_ROWS: " + maxRows);
  Logger.log("全プロパティ: " + JSON.stringify(allProps));

  // プロパティの削除
  props.deleteProperty("LAST_RUN");
  props.deleteAllProperties(); // 全削除（注意！）
}

// 実践：APIキーを安全に管理する
function safeApiKeyUsage() {
  // ❌ コードに直接書くのは絶対にNG（GitHubに上がると危険）
  // const apiKey = "sk-xxxxxxxxxxxxxxxx";

  // ✅ PropertiesServiceから取得する（安全）
  const apiKey = PropertiesService.getScriptProperties().getProperty("OPENAI_API_KEY");
  if (!apiKey) {
    throw new Error("APIキーが設定されていません。スクリプトプロパティにOPENAI_API_KEYを追加してください。");
  }
  Logger.log("APIキー取得成功（先頭5文字）: " + apiKey.substring(0, 5) + "...");
}
```

### 演習問題 第20章
バッチ処理のレジューム（再開）機能をプロパティサービスを使って実装してください。
- `startBatchProcess()`: 処理を開始する（スクリプトプロパティに現在行を保存しながら処理）
- `resetBatchProcess()`: スクリプトプロパティをクリアして処理をリセットする
- A列のデータを1行ずつ処理し、処理完了した行番号を `LAST_PROCESSED_ROW` というキーで保存する



---

## 技術リファレンス編 第21章 イベントとトリガー
Duration: 0:30:00

### 21-01 シンプルトリガー
シンプルトリガーは、決まった名前の関数をGASが自動的に呼び出す仕組みです。設定不要でそのまま動作します。

| 関数名 | 発動タイミング |
|---|---|
| `onOpen(e)` | ファイルが開かれた時 |
| `onEdit(e)` | セルが編集された時（スプレッドシートのみ） |
| `onSelectionChange(e)` | セルの選択が変わった時 |
| `onFormSubmit(e)` | フォームが送信された時（フォームバインド） |
| `doGet(e)` | GASウェブアプリへGETリクエストが来た時 |
| `doPost(e)` | GASウェブアプリへPOSTリクエストが来た時 |

```javascript
// シンプルトリガーの例

// ファイルを開いた時のトリガー
function onOpen(e) {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu("🤖 自動化")
    .addItem("日報を作成", "createDailyReport")
    .addToUi();
  Logger.log("スプレッドシートが開かれました");
}

// セルが編集された時のトリガー（軽い処理のみ推奨）
function onEdit(e) {
  const range = e.range;
  const sheet = range.getSheet();
  const row = range.getRow();
  const col = range.getColumn();
  const value = e.value;
  const oldValue = e.oldValue;

  // B列のステータスが「完了」に変更されたら行を緑色に
  if (sheet.getName() === "タスク管理" && col === 2 && value === "完了") {
    sheet.getRange(row, 1, 1, sheet.getLastColumn())
      .setBackground("#c8e6c9");
    Logger.log("行 " + row + " を完了済みとしてマーク");
  }
}

// セル選択変更のトリガー
function onSelectionChange(e) {
  const range = e.range;
  // 選択中のセルの値をA1に表示する（デモ用）
  if (range.getSheet().getName() === "データ") {
    SpreadsheetApp.getActiveSpreadsheet()
      .toast("選択中: " + range.getA1Notation() + " = " + range.getValue(), "セル情報", 2);
  }
}
```

### 21-02 インストーラブルトリガー
インストーラブルトリガーは、ユーザーが明示的に設定するトリガーです。時刻指定や他のファイルのフォーム送信イベントにも対応できます。

```javascript
// トリガーをコードで管理する（推奨：ソースコードとして管理できる）

// 既存のトリガーを削除してから再設定する
function setupTriggers() {
  // 既存のすべてのトリガーを削除
  ScriptApp.getProjectTriggers().forEach(trigger => {
    ScriptApp.deleteTrigger(trigger);
  });

  // 毎日9時に実行するトリガー
  ScriptApp.newTrigger("dailyMorningTask")
    .timeBased()
    .everyDays(1)
    .atHour(9)
    .create();

  // 毎週月曜日8時半に実行するトリガー
  ScriptApp.newTrigger("weeklyReport")
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.MONDAY)
    .atHour(8)
    .nearestMinute(30)
    .create();

  // 毎月1日に実行するトリガー
  ScriptApp.newTrigger("monthlyReport")
    .timeBased()
    .onMonthDay(1)
    .atHour(10)
    .create();

  // 隔30分でポーリングするトリガー
  ScriptApp.newTrigger("pollForUpdates")
    .timeBased()
    .everyMinutes(30)
    .create();

  // スプレッドシートが開かれた時のインストーラブルトリガー
  const ss = SpreadsheetApp.getActive();
  ScriptApp.newTrigger("onOpenInstallable")
    .forSpreadsheet(ss)
    .onOpen()
    .create();

  // フォーム送信時のインストーラブルトリガー
  // const form = FormApp.openById("フォームID");
  // ScriptApp.newTrigger("onFormSubmitInstallable")
  //   .forForm(form)
  //   .onFormSubmit()
  //   .create();

  Logger.log("トリガーの設定が完了しました");
  listTriggers();
}

// トリガーの一覧を表示
function listTriggers() {
  const triggers = ScriptApp.getProjectTriggers();
  triggers.forEach(t => {
    Logger.log("トリガー: " + t.getHandlerFunction() +
      " / タイプ: " + t.getEventType() +
      " / ソース: " + t.getTriggerSource());
  });
}

// 特定のトリガーを削除
function deleteTriggerByFunction(funcName) {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === funcName)
    .forEach(t => ScriptApp.deleteTrigger(t));
  Logger.log(funcName + " のトリガーを削除しました");
}

// トリガーで呼び出される関数
function dailyMorningTask() {
  Logger.log("朝9時の自動処理: " + new Date());
}
function weeklyReport() {
  Logger.log("週次レポート処理: " + new Date());
}
function monthlyReport() {
  Logger.log("月次レポート処理: " + new Date());
}
function pollForUpdates() {
  Logger.log("30分ポーリング: " + new Date());
}
```

### 21-03 イベントオブジェクト
トリガーが発火した際に渡されるイベントオブジェクト `e` の内容を確認します。

```javascript
// onEdit トリガーのイベントオブジェクト詳細
function onEditDetailed(e) {
  Logger.log("=== onEdit イベントオブジェクト ===");
  Logger.log("変更後の値: " + e.value);
  Logger.log("変更前の値: " + e.oldValue);
  Logger.log("セル範囲: " + e.range.getA1Notation());
  Logger.log("シート名: " + e.range.getSheet().getName());
  Logger.log("ユーザー: " + e.user.getEmail());
  Logger.log("スプレッドシート名: " + e.source.getName());
}

// onFormSubmit トリガーのイベントオブジェクト詳細
function onFormSubmitDetailed(e) {
  Logger.log("=== onFormSubmit イベントオブジェクト ===");
  Logger.log("タイムスタンプ: " + e.values[0]);
  Logger.log("全回答（配列）: " + JSON.stringify(e.values));

  // namedValues: 質問名をキーにした回答
  const namedVals = e.namedValues;
  Object.entries(namedVals).forEach(([question, answers]) => {
    Logger.log("質問[" + question + "] → " + answers[0]);
  });

  // レスポンスオブジェクト
  const response = e.response;
  Logger.log("回答ID: " + response.getId());
  Logger.log("回答時刻: " + response.getTimestamp());
}
```

### 21-04 Scriptサービス

```javascript
function scriptServiceDemo() {
  // OAuthトークンの取得（UrlFetchAppでAPIを呼ぶ際に必要）
  const token = ScriptApp.getOAuthToken();
  Logger.log("OAuthトークン（先頭20文字）: " + token.substring(0, 20) + "...");

  // スクリプトのサービスURL（ウェブアプリとして公開した場合のURL）
  const serviceUrl = ScriptApp.getService().getUrl();
  Logger.log("サービスURL: " + serviceUrl);

  // 残り実行時間の確認（6分制限のうち残り何秒か）
  // ヒント：タイムアウト直前に処理を安全に中断するために使う
  // Logger.log("残り実行時間: " + ScriptApp.getRemainingTime() + "ms");
}
```

### 演習問題 第21章
以下の要件を満たすトリガー管理システムを実装してください。
1. `setupAllTriggers()`: 毎朝9時 + 毎週月曜8時 + フォーム送信時 の3種類のトリガーを設定（既存削除後に再設定）
2. `listTriggers()`: 設定済みのトリガーを一覧表示してスプレッドシートのA列に書き出す
3. `onEdit(e)`: A列が「完了」に変更されたら自動でB列に完了日時を記録する
4. フォーム送信時のイベントで `e.namedValues` から「氏名」と「メールアドレス」を取り出して送信確認メールを送信する

---

## 技術リファレンス編 第22章 外部サイトへのアクセス
Duration: 0:25:00

### 22-01 Url Fetchサービス
`UrlFetchApp` はHTTPリクエストを送信して外部APIと通信するためのサービスです。

```javascript
function urlFetchOverview() {
  // 最もシンプルなGETリクエスト
  const response = UrlFetchApp.fetch("https://api.github.com/users/octocat");
  Logger.log("ステータスコード: " + response.getResponseCode());
  Logger.log("レスポンス（先頭200文字）: " + response.getContentText().substring(0, 200));
}
```

### 22-02 HTTPリクエストとHTTPレスポンス

```javascript
function httpRequestDemo() {
  // GETリクエスト（シンプル）
  const getResponse = UrlFetchApp.fetch("https://httpbin.org/get");
  Logger.log("GET Status: " + getResponse.getResponseCode());

  // POSTリクエスト（JSONボディ）
  const postOptions = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify({ name: "田中", score: 95 }),
    headers: {
      "Authorization": "Bearer " + PropertiesService.getScriptProperties().getProperty("API_KEY"),
      "X-Custom-Header": "GAS-Client"
    },
    muteHttpExceptions: true  // エラーステータスでも例外を投げない（推奨）
  };
  const postResponse = UrlFetchApp.fetch("https://httpbin.org/post", postOptions);
  Logger.log("POST Status: " + postResponse.getResponseCode());

  // レスポンスオブジェクトの操作
  const res = UrlFetchApp.fetch("https://httpbin.org/get");
  Logger.log("ステータス: " + res.getResponseCode());      // 200
  Logger.log("Content-Type: " + res.getHeaders()["Content-Type"]);
  const json = JSON.parse(res.getContentText());
  Logger.log("URL: " + json.url);

  // 複数URLへの並列リクエスト（高速）
  const urls = [
    "https://api.github.com/repos/google/clasp",
    "https://api.github.com/repos/googleworkspace/cli"
  ];
  const requests = urls.map(url => ({ url, muteHttpExceptions: true }));
  const responses = UrlFetchApp.fetchAll(requests);
  responses.forEach((r, i) => {
    const data = JSON.parse(r.getContentText());
    Logger.log(urls[i] + " → ⭐ " + (data.stargazers_count || "N/A"));
  });
}
```

### 22-03 HTML・JSONからデータを取り出す

```javascript
function parseResponseDemo() {
  // JSONレスポンスの解析
  function fetchAndParseJson(url) {
    const response = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
    if (response.getResponseCode() !== 200) {
      throw new Error("HTTPエラー: " + response.getResponseCode());
    }
    return JSON.parse(response.getContentText());
  }

  // 天気APIの例（OpenWeatherMap）
  // const apiKey = PropertiesService.getScriptProperties().getProperty("WEATHER_API_KEY");
  // const weather = fetchAndParseJson(`https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=${apiKey}&lang=ja&units=metric`);
  // Logger.log("東京の天気: " + weather.weather[0].description + " " + weather.main.temp + "℃");

  // ChatGPT API呼び出しの例
  function callChatGPT(prompt) {
    const apiKey = PropertiesService.getScriptProperties().getProperty("OPENAI_API_KEY");
    const response = UrlFetchApp.fetch("https://api.openai.com/v1/chat/completions", {
      method: "post",
      contentType: "application/json",
      headers: { "Authorization": "Bearer " + apiKey },
      payload: JSON.stringify({
        model: "gpt-4o",
        messages: [{ role: "user", content: prompt }],
        max_tokens: 500
      }),
      muteHttpExceptions: true
    });
    const result = JSON.parse(response.getContentText());
    return result.choices[0].message.content;
  }
  // Logger.log(callChatGPT("GASで業務自動化するメリットを3つ教えてください"));

  // Slack通知の完全版
  function notifySlack(message, channel = "#general") {
    const webhookUrl = PropertiesService.getScriptProperties().getProperty("SLACK_WEBHOOK_URL");
    if (!webhookUrl) throw new Error("SLACK_WEBHOOK_URLが設定されていません");

    const payload = { text: message, channel };
    const response = UrlFetchApp.fetch(webhookUrl, {
      method: "post",
      contentType: "application/json",
      payload: JSON.stringify(payload),
      muteHttpExceptions: true
    });
    Logger.log("Slack通知: " + response.getResponseCode());
  }
  // notifySlack("GASバッチ処理が完了しました :white_check_mark:");

  // GitHub APIでissueを作成する
  function createGitHubIssue(owner, repo, title, body) {
    const token = PropertiesService.getScriptProperties().getProperty("GITHUB_TOKEN");
    const response = UrlFetchApp.fetch(
      `https://api.github.com/repos/${owner}/${repo}/issues`,
      {
        method: "post",
        contentType: "application/json",
        headers: { "Authorization": "token " + token },
        payload: JSON.stringify({ title, body }),
        muteHttpExceptions: true
      }
    );
    const issue = JSON.parse(response.getContentText());
    Logger.log("Issue作成: #" + issue.number + " " + issue.html_url);
    return issue;
  }
  // createGitHubIssue("midnight480", "handson-manual", "バグ報告", "詳細をここに...");
}
```

### 演習問題 第22章
GitHubのPublic APIを使って、自分のリポジトリ一覧を取得しスプレッドシートに書き出す `fetchMyRepos()` 関数を作成してください。
- `GET https://api.github.com/users/{username}/repos` を使用
- A列:リポジトリ名 B列:説明 C列:スター数 D列:最終更新日をスプレッドシートに書き出す
- スター数の降順でソートする
- エラーが発生した場合は `muteHttpExceptions: true` でハンドリングし、エラーメッセージをログに出力する

---

## 技術リファレンス編 第23章 ライブラリ
Duration: 0:20:00

### 23-01 ライブラリを使用する
GASのライブラリとは、他のプロジェクトから再利用できるスクリプト群です。頻繁に使う処理をライブラリ化することで、複数のプロジェクト間でコードを共有できます。

```javascript
// ライブラリの追加手順：
// エディタ左サイドバーの「ライブラリ（＋）」→ スクリプトIDを入力 → バージョンを選択

// よく使われるサードパーティライブラリ
// ① moment.gs（日付操作）
//   スクリプトID: 15hgNOjKHUG4UtyZl9clqBbl23sDvWMS8pfDJOyIapZk5RBqwL3i-rlCo
// ② GASMailer（HTMLメール送信の簡略化）

// ライブラリ使用例（Momentを使った日付操作）
// function momentDemo() {
//   const today = Moment.moment(); // ライブラリのオブジェクトを呼び出す
//   Logger.log(today.format("YYYY年MM月DD日"));
//   Logger.log(today.add(7, "days").format("YYYY/MM/DD"));
//   Logger.log(today.startOf("month").format("YYYY/MM/DD")); // 月初め
// }
```

### 23-02 ライブラリを作成する

```javascript
// ライブラリとして公開するコードの例

/**
 * スプレッドシートのデータを2次元配列で取得するユーティリティ
 * @param {string} spreadsheetId スプレッドシートID
 * @param {string} sheetName シート名
 * @param {boolean} hasHeader ヘッダー行があるか否か
 * @return {Object[]} ヘッダーをキーとしたオブジェクトの配列
 */
function getSheetAsObjects(spreadsheetId, sheetName, hasHeader = true) {
  const ss = SpreadsheetApp.openById(spreadsheetId);
  const sheet = ss.getSheetByName(sheetName);
  if (!sheet) throw new Error("シート「" + sheetName + "」が見つかりません");

  const data = sheet.getDataRange().getValues();
  if (!hasHeader || data.length <= 1) return data;

  const headers = data[0];
  return data.slice(1)
    .filter(row => row.some(cell => cell !== "")) // 空行除外
    .map(row =>
      Object.fromEntries(headers.map((h, i) => [h, row[i]]))
    );
}

/**
 * 配列データをスプレッドシートに書き出すユーティリティ
 * @param {Object[]} records 書き出すデータ（オブジェクトの配列）
 * @param {string} spreadsheetId スプレッドシートID
 * @param {string} sheetName シート名（存在しない場合は作成）
 */
function writeObjectsToSheet(records, spreadsheetId, sheetName) {
  if (!records || records.length === 0) {
    Logger.log("書き出すデータがありません");
    return;
  }
  const ss = SpreadsheetApp.openById(spreadsheetId);
  let sheet = ss.getSheetByName(sheetName);
  if (!sheet) sheet = ss.insertSheet(sheetName);
  sheet.clearContents();

  const headers = Object.keys(records[0]);
  const rows = records.map(rec => headers.map(h => rec[h] !== undefined ? rec[h] : ""));

  sheet.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight("bold");
  if (rows.length > 0) {
    sheet.getRange(2, 1, rows.length, headers.length).setValues(rows);
  }
  Logger.log(rows.length + "件を「" + sheetName + "」シートに書き出しました");
}

// ライブラリ化の手順：
// 1. エディタの「プロジェクト設定」→ スクリプトIDをコピー
// 2. 使いたいプロジェクトで「ライブラリ（＋）」に貼り付け
// 3. バージョンを「HEAD（開発モード）」または特定バージョンで固定
// 4. 識別子（例: MyLib）を設定 → MyLib.getSheetAsObjects(...) で呼び出せる
```

### 演習問題 第23章
自分用のユーティリティライブラリ「GASUtils」を設計してください。以下の関数を実装し、別のスプレッドシートプロジェクトからライブラリとして呼び出せるか確認してください。
1. `sendSlackNotification(message)`: Slack通知を送る（WebhookURLはScriptPropertiesから取得）
2. `appendLogToSheet(sheetName, message)`: ログ用シートに日時とメッセージを追記する
3. `getLastRowOf(sheet, column)`: 指定列の最終行番号を返す（空白セルを除いた実質的な最終行）



---

## 補講：技術リファレンス編 演習問題の解答例
Duration: 0:10:00

各章の演習問題の模範解答コードです。コピー＆ペーストしてそのまま動かせます。

---

### 技術リファレンス編 第1章の解答：myInfo()

```javascript
function myInfo() {
  const name = "田中太郎"; // ← ご自身の名前に変更してください
  const email = Session.getActiveUser().getEmail(); // 実行ユーザーのメールアドレスを自動取得

  Logger.log("名前: " + name);
  Logger.log("メールアドレス: " + email);
}
```

---

### 技術リファレンス編 第2章の解答：inspectCells()

```javascript
function inspectCells() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  // A1〜A5セルの値を一括取得
  const values = sheet.getRange("A1:A5").getValues();

  values.forEach((row, index) => {
    const val = row[0];
    const cellName = "A" + (index + 1);
    Logger.log(cellName + ": 値=[" + val + "] 型=" + typeof val
      + (val === "" ? " (空白)" : ""));
  });
}
```

---

### 技術リファレンス編 第3章の解答：calcStats()

```javascript
function calcStats() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const values = sheet.getRange("A1:A10").getValues()
    .map(r => r[0])
    .filter(v => typeof v === "number" && !isNaN(v));

  if (values.length === 0) {
    SpreadsheetApp.getActiveSpreadsheet().toast("A列に数値データがありません");
    return;
  }

  const sum = values.reduce((s, n) => s + n, 0);
  const avg = sum / values.length;
  const max = Math.max(...values);
  const min = Math.min(...values);

  // B1〜B4に結果を書き出す
  const results = [["合計", sum], ["平均", avg], ["最大値", max], ["最小値", min]];
  results.forEach(([label, value], i) => {
    sheet.getRange(i + 1, 2).setValue(value);
    sheet.getRange(i + 1, 3).setValue(label);
  });

  Logger.log("合計=" + sum + " 平均=" + avg.toFixed(2) + " 最大=" + max + " 最小=" + min);
}
```

---

### 技術リファレンス編 第4章の解答：filterAndSum()

```javascript
function filterAndSum() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 1) return;

  const values = sheet.getRange(1, 1, lastRow, 1).getValues();
  let positiveSum = 0;

  values.forEach(([val], index) => {
    const row = index + 1;
    const cell = sheet.getRange(row, 1);

    // null・空・非数値はスキップ
    if (val === null || val === "" || typeof val !== "number") return;

    if (val <= 0) {
      // 0以下は赤色に塗る
      cell.setBackground("#ef9a9a");
    } else {
      // 正の値のみ合計
      positiveSum += val;
      cell.setBackground(null); // 背景色をリセット
    }
  });

  // B1セルに正の値の合計を出力
  sheet.getRange("B1").setValue(positiveSum);
  Logger.log("正の値の合計: " + positiveSum);
}
```

---

### 技術リファレンス編 第5章の解答：calcInvoice()

```javascript
// 小計計算を別関数に切り出す
function calcSubtotal(price, qty) {
  return price * qty;
}

function calcInvoice() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return;

  // B列(価格)・C列(数量)を一括取得
  const data = sheet.getRange(2, 2, lastRow - 1, 2).getValues();
  let totalBeforeTax = 0;

  const subtotals = data.map(([price, qty]) => {
    if (!price || !qty) return [0];
    const subtotal = calcSubtotal(price, qty);
    totalBeforeTax += subtotal;
    return [subtotal];
  });

  // D列に小計を一括書き込み
  sheet.getRange(2, 4, subtotals.length, 1).setValues(subtotals);

  // E1セルに消費税込み合計
  const totalWithTax = Math.ceil(totalBeforeTax * 1.1);
  sheet.getRange("E1").setValue(totalWithTax);

  Logger.log("税抜き合計: " + totalBeforeTax + "円 / 税込み合計: " + totalWithTax + "円");
}
```

---

### 技術リファレンス編 第6章の解答：Employeeクラス

```javascript
class Employee {
  constructor(name, department, salary) {
    this.name = name;
    this.department = department;
    this.salary = salary; // 月給
  }

  getAnnualSalary() {
    return this.salary * 12;
  }

  toString() {
    return `${this.name} / ${this.department} / 月給¥${this.salary.toLocaleString()}`;
  }
}

function highlightTopEarner() {
  const employees = [
    new Employee("田中", "営業部", 350000),
    new Employee("山田", "開発部", 480000),
    new Employee("佐藤", "総務部", 310000),
    new Employee("鈴木", "マーケ部", 420000)
  ];

  // 年収が最も高い社員を抽出
  const topEarner = employees.reduce((best, emp) =>
    emp.getAnnualSalary() > best.getAnnualSalary() ? emp : best
  );

  Logger.log("最高年収者: " + topEarner.toString());
  Logger.log("年収: ¥" + topEarner.getAnnualSalary().toLocaleString());

  // 全員をログ出力
  employees.forEach(emp => Logger.log(emp.toString() + " 年収¥" + emp.getAnnualSalary().toLocaleString()));
}
```

---

### 技術リファレンス編 第7章の解答：normalizePhones()

```javascript
function normalizePhones() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 1) return;

  const values = sheet.getRange(1, 1, lastRow, 1).getValues();

  const normalized = values.map(([phone]) => {
    if (!phone) return [""];
    // 数字のみ抽出（スペース・ハイフン・その他を除去）
    const digits = String(phone).replace(/[^\d]/g, "");
    // 11桁の携帯番号を xxx-xxxx-xxxx 形式に整形
    if (digits.length === 11) {
      return [digits.slice(0, 3) + "-" + digits.slice(3, 7) + "-" + digits.slice(7)];
    }
    // 10桁の市外局番付き番号を xx-xxxx-xxxx 形式に
    if (digits.length === 10) {
      return [digits.slice(0, 2) + "-" + digits.slice(2, 6) + "-" + digits.slice(6)];
    }
    return [phone + "（形式不明）"];
  });

  // B列に一括書き込み
  sheet.getRange(1, 2, normalized.length, 1).setValues(normalized);
  Logger.log("電話番号の正規化が完了しました（" + normalized.length + "件）");
}
```

---

### 技術リファレンス編 第8章の解答：スプレッドシート売上集計

```javascript
function aggregateSalesData() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const dataSheet = ss.getSheetByName("売上データ") || ss.getActiveSheet();
  const lastRow = dataSheet.getLastRow();
  if (lastRow < 2) return;

  // A:日付 B:担当者 C:売上金額 を一括取得
  const data = dataSheet.getRange(2, 1, lastRow - 1, 3).getValues()
    .filter(row => row[2] !== "" && !isNaN(row[2]));

  // 合計・平均の計算
  const amounts = data.map(r => Number(r[2]));
  const total = amounts.reduce((s, n) => s + n, 0);
  const average = total / amounts.length;

  dataSheet.getRange("D1").setValue(total);
  dataSheet.getRange("D2").setValue(Math.round(average));
  Logger.log("合計: " + total + " / 平均: " + Math.round(average));

  // 担当者別集計（Map を使用）
  const salesByPerson = new Map();
  data.forEach(([, name, amount]) => {
    salesByPerson.set(name, (salesByPerson.get(name) || 0) + Number(amount));
  });

  // 集計シートへ書き出し
  let summarySheet = ss.getSheetByName("集計");
  if (!summarySheet) summarySheet = ss.insertSheet("集計");
  summarySheet.clearContents();
  summarySheet.getRange("A1:B1").setValues([["担当者", "合計売上"]]).setFontWeight("bold");

  const summaryData = [...salesByPerson.entries()]
    .sort((a, b) => b[1] - a[1]); // 金額の降順でソート

  summarySheet.getRange(2, 1, summaryData.length, 2).setValues(summaryData);
  Logger.log("集計シートに " + summaryData.length + "人分を書き出しました");
}
```

---

### 技術リファレンス編 第9章の解答：logInvoiceEmails()

```javascript
function logInvoiceEmails() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let logSheet = ss.getSheetByName("Gmailログ");
  if (!logSheet) logSheet = ss.insertSheet("Gmailログ");
  logSheet.clearContents();

  // ヘッダー行
  logSheet.getRange("A1:E1").setValues([["差出人", "件名", "日付", "添付ファイル名", "スレッドID"]])
    .setFontWeight("bold");

  const threads = GmailApp.search("subject:請求書", 0, 20);
  const rows = [];

  threads.forEach(thread => {
    thread.getMessages().forEach(msg => {
      const attachments = msg.getAttachments();
      const attNames = attachments.length > 0
        ? attachments.map(a => a.getName()).join(", ")
        : "（なし）";
      rows.push([
        msg.getFrom(),
        msg.getSubject(),
        Utilities.formatDate(msg.getDate(), "JST", "yyyy/MM/dd HH:mm"),
        attNames,
        thread.getId()
      ]);
    });
  });

  if (rows.length > 0) {
    logSheet.getRange(2, 1, rows.length, 5).setValues(rows);
  }
  Logger.log("Gmailログに " + rows.length + "件を書き出しました");
}
```

---

### 技術リファレンス編 第10章の解答：findFilesFromSheet()

```javascript
function findFilesFromSheet() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 1) return;

  // 「レポート置き場」フォルダを検索
  const folderIterator = DriveApp.getFoldersByName("レポート置き場");
  const targetFolder = folderIterator.hasNext() ? folderIterator.next() : null;

  const fileNames = sheet.getRange(1, 1, lastRow, 1).getValues();

  const results = fileNames.map(([fileName]) => {
    if (!fileName) return ["", ""];
    let url = "見つかりません";
    let sizeKB = "";

    const iterator = targetFolder
      ? targetFolder.getFilesByName(String(fileName))
      : DriveApp.getFilesByName(String(fileName));

    if (iterator.hasNext()) {
      const file = iterator.next();
      url = file.getUrl();
      sizeKB = Math.round(file.getSize() / 1024 * 10) / 10; // KB単位（小数1桁）
    }
    return [url, sizeKB];
  });

  sheet.getRange(1, 2, results.length, 2).setValues(results);
  Logger.log(results.length + "件のファイル検索が完了しました");
}
```

---

### 技術リファレンス編 第11章の解答：getThisMonthCalendar()

```javascript
function getThisMonthCalendar() {
  const now = new Date();
  const firstDay = new Date(now.getFullYear(), now.getMonth(), 1);
  const lastDay = new Date(now.getFullYear(), now.getMonth() + 1, 0, 23, 59, 59);

  const events = CalendarApp.getDefaultCalendar().getEvents(firstDay, lastDay);

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("今月の予定");
  if (!sheet) sheet = ss.insertSheet("今月の予定");
  sheet.clearContents();

  // ヘッダー
  sheet.getRange("A1:E1").setValues([["タイトル", "開始日時", "終了日時", "場所", "終日イベント"]])
    .setFontWeight("bold");

  const rows = events.map(event => [
    event.getTitle(),
    event.isAllDayEvent() ? "" : Utilities.formatDate(event.getStartTime(), "JST", "yyyy/MM/dd HH:mm"),
    event.isAllDayEvent() ? "" : Utilities.formatDate(event.getEndTime(), "JST", "yyyy/MM/dd HH:mm"),
    event.getLocation(),
    event.isAllDayEvent()
  ]);

  if (rows.length > 0) {
    sheet.getRange(2, 1, rows.length, 5).setValues(rows);
  }

  // E列（終日フラグ）でフィルタ設定
  const range = sheet.getRange(1, 1, rows.length + 1, 5);
  range.createFilter();

  Logger.log("今月の予定を " + rows.length + "件書き出しました");
}
```

---

### 技術リファレンス編 第12章の解答：generateCertificates()

```javascript
function generateCertificates() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const dataSheet = ss.getSheetByName("社員情報");
  if (!dataSheet) throw new Error("「社員情報」シートが見つかりません");

  const TEMPLATE_ID = PropertiesService.getScriptProperties().getProperty("CERT_TEMPLATE_ID");
  if (!TEMPLATE_ID) throw new Error("CERT_TEMPLATE_IDをスクリプトプロパティに設定してください");

  // 保存先フォルダ
  const folderName = "社員証明書_" + Utilities.formatDate(new Date(), "JST", "yyyyMMdd");
  const folder = DriveApp.createFolder(folderName);

  const data = dataSheet.getRange(2, 1, dataSheet.getLastRow() - 1, 3).getValues()
    .filter(row => row[0] !== "");

  data.forEach(([name, dept, year]) => {
    // テンプレートをコピー
    const templateFile = DriveApp.getFileById(TEMPLATE_ID);
    const copy = templateFile.makeCopy(name + "_証明書", folder);
    const doc = DocumentApp.openById(copy.getId());
    const body = doc.getBody();

    // プレースホルダーを置換
    body.replaceText("\{\{NAME\}\}", name);
    body.replaceText("\{\{DEPT\}\}", dept);
    body.replaceText("\{\{YEAR\}\}", String(year));

    doc.saveAndClose();
    Logger.log("作成: " + name + " → " + copy.getUrl());
  });

  SpreadsheetApp.getActiveSpreadsheet().toast(
    data.length + "件の証明書を「" + folderName + "」フォルダに作成しました"
  );
}
```

---

### 技術リファレンス編 第13章の解答：generateKPISlides()

```javascript
function generateKPISlides() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName("月次KPI");
  if (!sheet) throw new Error("「月次KPI」シートが見つかりません");

  const SLIDE_ID = PropertiesService.getScriptProperties().getProperty("KPI_SLIDE_ID");
  if (!SLIDE_ID) throw new Error("KPI_SLIDE_IDをスクリプトプロパティに設定してください");

  const data = sheet.getRange(2, 1, sheet.getLastRow() - 1, 4).getValues()
    .filter(row => row[0] !== "");
  // A:指標名 B:目標値 C:実績値 D:達成率

  const pres = SlidesApp.openById(SLIDE_ID);
  const slides = pres.getSlides();

  data.forEach((row, index) => {
    const [metricName, target, actual, rate] = row;
    if (index >= slides.length) return;

    const slide = slides[index];
    slide.replaceAllText("{{METRIC}}", String(metricName));
    slide.replaceAllText("{{TARGET}}", String(target));
    slide.replaceAllText("{{ACTUAL}}", String(actual));
    slide.replaceAllText("{{RATE}}", (Number(rate) * 100).toFixed(1) + "%");

    // 達成率に応じて色分け（テキストボックスを検索して色を変える）
    const color = Number(rate) >= 1 ? "#2e7d32" : "#c62828"; // 達成:緑 未達:赤
    slide.getPageElements().forEach(el => {
      if (el.getPageElementType() === SlidesApp.PageElementType.SHAPE) {
        const text = el.asShape().getText().asString();
        if (text.includes("%")) {
          el.asShape().getText().getTextStyle().setForegroundColor(color);
        }
      }
    });
  });

  pres.saveAndClose();
  Logger.log("KPIスライドを更新しました（" + data.length + "指標）");
}
```

---

### 技術リファレンス編 第14章の解答：createTrainingForm()

```javascript
function createTrainingForm() {
  const form = FormApp.create("社内研修申込フォーム");
  form.setTitle("社内研修 参加申込");
  form.setDescription("研修参加を希望される方はご記入ください。");

  // 氏名（必須）
  form.addTextItem().setTitle("氏名").setRequired(true);

  // 所属部署（ドロップダウン）
  form.addListItem().setTitle("所属部署")
    .setChoiceValues(["総務", "営業", "開発", "その他"])
    .setRequired(true);

  // 希望研修日（日付）
  form.addDateItem().setTitle("希望研修日").setRequired(true);

  // 参加動機（段落テキスト）
  form.addParagraphTextItem().setTitle("参加動機");

  // 事前スキル（チェックボックス）
  form.addCheckboxItem().setTitle("事前スキル（当てはまるものすべて）")
    .setChoiceValues(["GAS初心者", "JavaScript経験あり", "GASスクリプト経験あり"]);

  // 満足度評価（線形尺度）
  form.addScaleItem().setTitle("過去の研修への満足度（初参加は回答不要）")
    .setBounds(1, 5)
    .setLabels("とても不満", "とても満足");

  // フォームID・URLをスプレッドシートに保存
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.getRange("A1").setValue(form.getId());
  sheet.getRange("B1").setValue(form.getPublishedUrl());

  Logger.log("フォーム作成完了");
  Logger.log("URL: " + form.getPublishedUrl());
}
```

---

### 技術リファレンス編 第15章の解答：multiTranslate()

```javascript
function multiTranslate() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  if (lastRow < 1) return;

  const sourceData = sheet.getRange(1, 1, lastRow, 1).getValues();
  const targets = [
    { col: 2, lang: "en", label: "英語" },
    { col: 3, lang: "zh-CN", label: "中国語（簡体字）" },
    { col: 4, lang: "fr", label: "フランス語" }
  ];

  targets.forEach(({ col, lang, label }) => {
    const translated = sourceData.map(([text]) => {
      if (!text) return [""];
      try {
        const result = LanguageApp.translate(String(text), "ja", lang);
        Utilities.sleep(300); // API制限対策
        return [result];
      } catch (e) {
        return ["翻訳エラー: " + e.message];
      }
    });
    sheet.getRange(1, col, translated.length, 1).setValues(translated);
    Logger.log(label + "への翻訳完了");
  });

  SpreadsheetApp.getActiveSpreadsheet().toast("全言語への翻訳が完了しました");
}
```

---

### 技術リファレンス編 第16章の解答：runDailyBatch()

```javascript
function processDailyData() {
  // メインのバッチ処理の内容（省略可）
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  Logger.log("processDailyData: " + sheet.getLastRow() + "行を処理中...");
  Utilities.sleep(500); // 処理の模倣
}

function runDailyBatch() {
  const start = new Date();
  const ts = () => Utilities.formatDate(new Date(), "JST", "HH:mm:ss");

  try {
    Logger.log("[" + ts() + "] 日次バッチ処理を開始します");
    processDailyData();
    Logger.log("[" + ts() + "] 日次バッチ処理が正常に完了しました");

  } catch (e) {
    const errorMsg = [
      "エラー名: " + e.name,
      "メッセージ: " + e.message,
      "スタック: " + e.stack,
      "発生時刻: " + new Date().toString()
    ].join("\n");

    Logger.log("[" + ts() + "] エラーが発生しました:\n" + errorMsg);
    GmailApp.sendEmail(
      "admin@example.com",
      "【GASエラー】日次バッチ処理でエラーが発生しました",
      errorMsg
    );

  } finally {
    const elapsed = ((new Date() - start) / 1000).toFixed(1);
    Logger.log("[" + ts() + "] 処理終了（所要時間: " + elapsed + "秒）");
  }
}
```

---

### 技術リファレンス編 第17章の解答：カスタムメニューと確認ダイアログ

```javascript
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("🔧 自動化ツール")
    .addItem("📊 データ集計", "showAggregateInfo")
    .addItem("📄 PDFとして書き出し", "promptPdfExport")
    .addItem("📧 管理者に報告", "showReportInfo")
    .addToUi();
}

function showAggregateInfo() {
  SpreadsheetApp.getUi().alert(
    "データ集計",
    "アクティブシートのデータを集計します。\nA列: 担当者名、B列: 金額が必要です。",
    SpreadsheetApp.getUi().ButtonSet.OK
  );
}

function promptPdfExport() {
  const ui = SpreadsheetApp.getUi();
  const result = ui.prompt(
    "PDFとして書き出し",
    "出力ファイル名を入力してください（例: 月次レポート_2026年4月）",
    ui.ButtonSet.OK_CANCEL
  );
  if (result.getSelectedButton() === ui.Button.OK) {
    const fileName = result.getResponseText() || "出力ファイル";
    ui.alert("確認", '「' + fileName + '.pdf」として書き出します。', ui.ButtonSet.OK);
    // 実際のPDF書き出し処理をここに追加
  }
}

function showReportInfo() {
  SpreadsheetApp.getUi().alert(
    "管理者に報告",
    "admin@example.com に集計結果レポートを送信します。",
    SpreadsheetApp.getUi().ButtonSet.OK
  );
}
```

---

### 技術リファレンス編 第18章の解答：generateAndSendInvoice()

```javascript
function generateAndSendInvoice() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("請求書データ");
  if (!sheet) throw new Error("「請求書データ」シートが見つかりません");

  // A:顧客名 B:金額 C:品目 を読み込む
  const data = sheet.getRange(2, 1, sheet.getLastRow() - 1, 3).getValues()
    .filter(row => row[0] !== "");

  // CSV文字列を生成
  const header = "顧客名,金額,品目";
  const csvRows = data.map(row => row.join(","));
  const csvContent = [header, ...csvRows].join("\n");

  // Blobを作成
  const csvBlob = Utilities.newBlob(csvContent, "text/csv; charset=utf-8", "invoice.csv");

  // Googleドライブの「請求書」フォルダに保存
  let folder;
  const folderIterator = DriveApp.getFoldersByName("請求書");
  folder = folderIterator.hasNext() ? folderIterator.next() : DriveApp.createFolder("請求書");
  const savedFile = folder.createFile(csvBlob);
  Logger.log("保存: " + savedFile.getUrl());

  // 顧客にメール送信
  GmailApp.sendEmail(
    "customer@example.com",
    "【請求書】ご請求金額のご案内",
    "いつもお世話になっております。\n請求書データをCSFにてお送りします。\nご確認のほど、よろしくお願いいたします。",
    {
      attachments: [csvBlob],
      name: "GAS自動送信システム"
    }
  );

  SpreadsheetApp.getActiveSpreadsheet()
    .toast("請求書を送信しました。ファイル: " + savedFile.getName());
}
```

---

### 技術リファレンス編 第19章の解答：backupSheetAsZip()

```javascript
function backupSheetAsZip() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("月次データ");
  if (!sheet) throw new Error("「月次データ」シートが見つかりません");

  // シートデータを2次元配列で取得してCSV文字列に変換
  const data = sheet.getDataRange().getValues();
  const csvContent = data.map(row =>
    row.map(cell => {
      // セルにカンマや改行が含まれる場合はダブルクォートで囲む
      const str = String(cell);
      return str.includes(",") || str.includes("\n") ? '"' + str + '"' : str;
    }).join(",")
  ).join("\n");

  // CSV → Blob
  const csvBlob = Utilities.newBlob(csvContent, "text/csv; charset=utf-8", "monthly_data.csv");

  // ZIP圧縮
  const zipBlob = Utilities.zip([csvBlob],
    "バックアップ_" + Utilities.formatDate(new Date(), "JST", "yyyyMMdd") + ".zip"
  );

  // Googleドライブに保存
  const file = DriveApp.createFile(zipBlob);

  SpreadsheetApp.getActiveSpreadsheet()
    .toast("バックアップ完了: " + file.getName(), "ZIP作成", 5);
  Logger.log("ZIPバックアップ保存: " + file.getUrl());
}
```

---

### 技術リファレンス編 第20章の解答：バッチ処理のレジューム機能

```javascript
const PROP_KEY = "LAST_PROCESSED_ROW";

function startBatchProcess() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const props = PropertiesService.getScriptProperties();
  const startRow = Number(props.getProperty(PROP_KEY) || 2);
  const lastRow = sheet.getLastRow();
  const START_TIME = new Date().getTime();
  const LIMIT_MS = 5 * 60 * 1000; // 5分でセーフストップ

  Logger.log("バッチ開始: " + startRow + "行目から再開");

  for (let row = startRow; row <= lastRow; row++) {
    // 5分経過でセーフストップ
    if (new Date().getTime() - START_TIME > LIMIT_MS) {
      props.setProperty(PROP_KEY, String(row));
      Logger.log("タイムアウト: " + row + "行目で中断。次回はここから再開します。");
      return;
    }

    const value = sheet.getRange(row, 1).getValue();
    if (!value) continue;

    // 実際の処理（ここでは処理済みマークをB列に付ける）
    sheet.getRange(row, 2).setValue("✅ 処理済み");
    props.setProperty(PROP_KEY, String(row + 1)); // 次回の開始行を保存
  }

  // 全行完了
  props.deleteProperty(PROP_KEY);
  Logger.log("全行の処理が完了しました（" + (lastRow - 1) + "行）");
}

function resetBatchProcess() {
  PropertiesService.getScriptProperties().deleteProperty(PROP_KEY);
  Logger.log("バッチ処理プロパティをリセットしました");
}
```

---

### 技術リファレンス編 第21章の解答：トリガー管理システム

```javascript
function setupAllTriggers() {
  // 既存のトリガーをすべて削除
  ScriptApp.getProjectTriggers().forEach(t => ScriptApp.deleteTrigger(t));

  // 毎朝9時
  ScriptApp.newTrigger("dailyMorningTask").timeBased().everyDays(1).atHour(9).create();

  // 毎週月曜8時
  ScriptApp.newTrigger("weeklyMondayTask")
    .timeBased().onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(8).nearestMinute(0).create();

  Logger.log("トリガーを設定しました");
  listTriggersToSheet();
}

function listTriggersToSheet() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const triggers = ScriptApp.getProjectTriggers();

  const headers = [["関数名", "イベントタイプ", "ソース", "ID"]];
  const rows = triggers.map(t => [
    t.getHandlerFunction(),
    t.getEventType(),
    t.getTriggerSource(),
    t.getUniqueId()
  ]);

  sheet.clearContents();
  sheet.getRange(1, 1, 1, 4).setValues(headers).setFontWeight("bold");
  if (rows.length > 0) sheet.getRange(2, 1, rows.length, 4).setValues(rows);

  Logger.log(triggers.length + "個のトリガーを書き出しました");
}

function onEdit(e) {
  const col = e.range.getColumn();
  const row = e.range.getRow();
  if (col !== 1 || row === 1) return; // A列でなければスキップ、ヘッダーも除外

  if (e.value === "完了") {
    const sheet = e.range.getSheet();
    const now = Utilities.formatDate(new Date(), "JST", "yyyy/MM/dd HH:mm:ss");
    sheet.getRange(row, 2).setValue(now); // B列に完了日時を記録
  }
}

function onFormSubmitForTrigger(e) {
  const namedVals = e.namedValues;
  const name = (namedVals["氏名"] || ["（不明）"])[0];
  const email = (namedVals["メールアドレス"] || [""])[0];

  if (email) {
    GmailApp.sendEmail(
      email,
      "【受付完了】研修申込を受け付けました",
      name + " 様\n\nご応募ありがとうございます。\n内容を確認の上、折り返しご連絡いたします。"
    );
    Logger.log("確認メール送信: " + name + " <" + email + ">");
  }
}

function dailyMorningTask() { Logger.log("朝9時バッチ実行: " + new Date()); }
function weeklyMondayTask() { Logger.log("月曜朝バッチ実行: " + new Date()); }
```

---

### 技術リファレンス編 第22章の解答：fetchMyRepos()

```javascript
function fetchMyRepos() {
  const USERNAME = PropertiesService.getScriptProperties().getProperty("GITHUB_USERNAME");
  if (!USERNAME) throw new Error("GITHUB_USERNAMEをスクリプトプロパティに設定してください");

  const TOKEN = PropertiesService.getScriptProperties().getProperty("GITHUB_TOKEN");

  const response = UrlFetchApp.fetch(
    "https://api.github.com/users/" + USERNAME + "/repos?per_page=100&sort=updated",
    {
      headers: TOKEN ? { "Authorization": "token " + TOKEN } : {},
      muteHttpExceptions: true
    }
  );

  if (response.getResponseCode() !== 200) {
    Logger.log("エラー: " + response.getResponseCode() + " " + response.getContentText());
    return;
  }

  const repos = JSON.parse(response.getContentText());

  // スター数の降順でソート
  repos.sort((a, b) => b.stargazers_count - a.stargazers_count);

  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.clearContents();
  sheet.getRange("A1:D1")
    .setValues([["リポジトリ名", "説明", "スター数", "最終更新日"]])
    .setFontWeight("bold");

  const rows = repos.map(repo => [
    repo.name,
    repo.description || "",
    repo.stargazers_count,
    Utilities.formatDate(new Date(repo.updated_at), "JST", "yyyy/MM/dd")
  ]);

  if (rows.length > 0) {
    sheet.getRange(2, 1, rows.length, 4).setValues(rows);
  }
  Logger.log(rows.length + "件のリポジトリを書き出しました");
}
```

---

### 技術リファレンス編 第23章の解答：GASUtilsライブラリ

```javascript
// ===== GASUtils ライブラリ =====
// このスクリプトを単独のGASプロジェクトとして保存し、
// ライブラリとして他のプロジェクトから呼び出す

/**
 * Slack Incoming Webhookにメッセージを送信する
 * @param {string} message 送信するメッセージ
 * @param {string} [channel] 送信チャンネル（省略可）
 */
function sendSlackNotification(message, channel) {
  const webhookUrl = PropertiesService.getScriptProperties().getProperty("SLACK_WEBHOOK_URL");
  if (!webhookUrl) throw new Error("SLACK_WEBHOOK_URLをスクリプトプロパティに設定してください");

  const payload = { text: message };
  if (channel) payload.channel = channel;

  const response = UrlFetchApp.fetch(webhookUrl, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  });
  Logger.log("Slack通知送信: " + response.getResponseCode() + " / " + message.substring(0, 50));
  return response.getResponseCode() === 200;
}

/**
 * ログ用シートに日時とメッセージを追記する
 * @param {string} sheetName ログを追記するシート名
 * @param {string} message ログメッセージ
 * @param {string} [level="INFO"] ログレベル（INFO/WARN/ERROR）
 */
function appendLogToSheet(sheetName, message, level) {
  level = level || "INFO";
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(sheetName);
  if (!sheet) {
    sheet = ss.insertSheet(sheetName);
    sheet.getRange("A1:C1").setValues([["日時", "レベル", "メッセージ"]]).setFontWeight("bold");
  }

  const timestamp = Utilities.formatDate(new Date(), "JST", "yyyy/MM/dd HH:mm:ss");
  sheet.appendRow([timestamp, level, message]);
  Logger.log("[" + level + "] " + message);
}

/**
 * 指定列の最終行番号を返す（空白セルを除いた実質的な最終行）
 * @param {GoogleAppsScript.Spreadsheet.Sheet} sheet 対象シート
 * @param {number} column 列番号（1始まり）
 * @return {number} 最終行番号
 */
function getLastRowOf(sheet, column) {
  const colData = sheet.getRange(1, column, sheet.getMaxRows(), 1).getValues();
  for (let i = colData.length - 1; i >= 0; i--) {
    if (colData[i][0] !== "") return i + 1;
  }
  return 0;
}

// ===== 呼び出し元プロジェクトでの使用例 =====
// 前提: ライブラリの識別子を "GASUtils" に設定

// function useSample() {
//   GASUtils.sendSlackNotification("バッチ処理が完了しました");
//   GASUtils.appendLogToSheet("実行ログ", "バッチ処理完了", "INFO");
//   const sheet = SpreadsheetApp.getActiveSheet();
//   const lastRow = GASUtils.getLastRowOf(sheet, 1);
//   Logger.log("A列の最終行: " + lastRow);
// }
```
