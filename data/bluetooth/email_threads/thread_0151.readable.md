# thread_0151: Re: BT-SIG認証依頼

- Message count: 5
- Source JSON: `thread_0151.json`

---

## 1. 2026-03-09 07:22

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?S3VkbyBBdHN1c2hpGyRCIUo5KUYjGyhCIBskQj1fO0shSxsoQg==?= , Masaya Iida

株式会社ソアー工藤様アリオンでBluetooth認証を担当しています酒井です。よろしくお願いします。

飯田に代わりご質問にお答えします。
＞(1)認証登録済で、ICS不整合のない登録であること、
⇒こちら添付ファイルを確認していただくことは可能でしょうか？

送付頂いたICSを読み込んでCnsistency Checkを行うと以下のInvalid(不整合)が発生します。このままでは登録サイトの「Specify the Design」ページでHost Subsystem

とともにQDID/DNをInclude後に[Use This Design Without Modifications]をチェックして登録を進めるしか方法がありません。

しかし、Invalidが登録サイトの判断の許容範囲でないとコア階層に試験要求が発生することがあります。コア階層の試験は試験機関および費用的に天文学的費用になりますので他の「Invalidが発生しない」SoC/モジュール/ホストスタックを選択して、

試験免除登録を行うことをお勧めします。

また見積確定に必要なのは、見積依頼書にTBD（Realtekに確認中）と書かれたQDID/DN

ですが、「ICS不整合のある登録」でも[Use This Design Without Modifications]で試験要求も発生せずに新規登録できることもありますのでRealtekから参照先登録候補が示されたら確認しますのでご連絡ください。

HCI

4:C.157 | If [HCI] (1a/1 and 4/13) are Supported then [HCI] (4/10) is Mandatory

5:Prerequisite | If [CORE] (1a/54) is Not Supported then [HCI] (5/34a, 5/35a and 5/67-69) are Excluded

IAL

2:C.1 | If [IAL] (1/3) is Supported then it is Mandatory to Support at least one of [IAL] (2/1-2)

2:C.2 | If [IAL] (1/4) is Supported then [IAL] (2/3) is Mandatory

2:C.3 | If [IAL] (1/5) is Supported then [IAL] (2/4) is Mandatory

LL

9:C.44 | If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/48) is Excluded

4a:C.1 | If [LL] (1/2 and 4/8) are Supported then [LL] (4a/1) is Mandatory

4a:C.3 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/3) is Mandatory

4a:C.5 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/5) is Mandatory

4a:C.7 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/7) is Mandatory

4a:C.7 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/7) is Mandatory

9:C.55 | If [LL] (9/31) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/32) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/48) is Supported then [LL] (9/60) is Mandatory

9:C.57 | If [LL] (9/15) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/16) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/19) is Supported then [LL] (9/62) is Mandatory

LMP

2a:C.56 | If [HCI] (13/7) is Supported then [LMP] (2a/56) is Mandatory

2b:C.1 | If [LMP] (2/17) is Supported then [LMP] (2b/1) is Mandatory

2b:C.3 | If [LMP] (2/18) is Supported then [LMP] (2b/3) is Mandatory

30:C.0 | If [LMP] (2/1) is Supported then [LMP] (30/0a and 30/0b) are Mandatory

30:C.1 | If [LMP] (2/2) is Supported then [LMP] (30/1a and 30/1b) are Mandatory

30:C.11 | If [LMP] (2/12) is Supported then [LMP] (30/11) is Mandatory

30:C.25 | If [LMP] (2/17) is Supported then [LMP] (30/25) is Mandatory

30:C.26 | If [LMP] (2/17a) is Supported then [LMP] (30/26) is Mandatory

30:C.31 | If [LMP] (2/15) is Supported then [LMP] (30/31) is Mandatory

30:C.45 | If [LMP] (2/18) is Supported then [LMP] (30/45) is Mandatory

30:C.46 | If [LMP] (2/18a) is Supported then [LMP] (30/46) is Mandatory

31:C.1 | If [RF] (1/1) is Supported then [LMP] (31/1) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/12) are Supported then [LMP] (2a/53) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/15) are Supported then [LMP] (2a/53) is Mandatory

以上回答いたします。

差出人: Kudo Atsushi（工藤淳史）

送信日時: 2026年3月9日 15:01

宛先: Masaya Iida

件名: RE: BT-SIG認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

下記ご確認していただく事は可能でしょうか？

問題なければいただいた内容で進めさせていただきたいので、ご確認よろしくお願い致します。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Kudo Atsushi （工藤淳史）

Sent: Thursday, March 5, 2026 11:05 AM

To: 'Masaya Iida'

Subject: RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

返信が遅くなり申し訳ありません。

お見積りありがとうございます。

下記前提の件ご確認をお願い致します。

＞ (1) 認証登録済で、 ICS 不整合のない登録であること、

⇒こちら添付ファイルを確認していただくことは可能でしょうか？

＞ (2) ホストスタックに AVCTP,
AVDTP, GADTP を含むこと

⇒こちら対応しております。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Masaya Iida

Sent: Wednesday, February 25, 2026 5:32 PM

To: Kudo Atsushi （工藤淳史）

Subject: RE: [ID] 認証依頼ソアー工藤様アリオンの飯田です。

見積依頼書のご提出ありがとうございました。

当社サポート費用は以下の通りです。

確認中の実装モジュールおよびホストスタックが

(1) 認証登録済で、 ICS 不整合のない登録であること、

(2) ホストスタックに AVCTP,
AVDTP, GADTP を含むことを前提にした見積は以下の通りです。

・ PTS 試験（A2DP,
AVRCP, IOPT） ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発酵前月末日 TTS レート換算円貨

($6,000 は NTT
sonority, Inc 名義登録の場合 )

※上記は税抜き表示です。

※ US ドルは円換算して正式見積書を発行いたします。

※御社とは取引実績がまだございませんので、費用は「前払い」でお願いいたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 2. 2026-03-10 03:22

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?TWl6dW1hdGEgU2hpbmppGyRCIUo/ZUtzGyhCIBskQj84RnMhSxsoQg==?= , =?iso-2022-jp?B?S3VkbyBBdHN1c2hpGyRCIUo5KUYjGyhCIBskQj1fO0shSxsoQg==?= , Masaya Iida

株式会社ソアー水俣様、工藤様アリオンの酒井です。いつも世話になっております。

RealtekからのDID情報展開ありがとうございます。

ご連絡いただいた「Bluetooth IC DID : [ID]」はController Stack DID : [ID]

およびHost Stack DID :188777を一部組み合わせた「BLEオンリーのEnd Product登録」

です。

先日いただた見積依頼書にはBR/EDRにチェックが入っていますので、BLEオンリー登録の「Bluetooth IC DID : [ID]」は適しないものと思われますが、参照している

「Controller Stack DID : 207390およびHost Stack DID :[ID]」を直接参照すれば

BR/EDRの新規製品登録が可能です。ただし、2024/07/01以降の現行登録制度では、参照先のQDID/DNがBR/EDR/LEの場合にはそのまま踏襲しないでCore階層を削除するとInvalid

が発生しますので、今回もBR/EDR/LE登録の「Controller Stack DID : 207390および

Host Stack DID :[ID]」もそのまま踏襲してBR/EDR/LE登録し、製品実装でBR/EDRのペアリングのみを実装して実質的にBR/EDR製品として製品化する方法となりますのでご了承ください。

「Controller Stack DID : 207390およびHost Stack DID :[ID]」を参照した登録を仮

Projectで確認した結果、GAPに56件のInvalidが発生します。当然、参照先の188777を登録した時点ではNo Invalidでしか登録できないため、登録後に追加あるいは変更されたチェックルールに起因するもので、このケースでは[Combine Unmodified Design]という登録手順が準備されています。この手順は参照先のサポート階層、各階層のICS機能および包含するInvalidをそのまま踏襲する(取捨選択できない)登録となりますがSIGが特定で許容した有効な登録が可能です。

「Controller Stack DID : 207390およびHost Stack DID :[ID]」を参照し、[Combine

Unmodified Design]の登録手順ならば登録可能で、見積は以下の通りです。（見積依頼書のBR/EDRのチェックを前提としています。もしBLEもサポートした製品ではRF PHY試験が追加実施が発生します。)

・RFフル項目試験 ￥1,200,000

・プロファアイル試験(A2DP, AVRCP, IOPT) ￥300,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

・ドル送金代行手数料 ￥100,000

・Qualification Fee($6,000) 正式見積書発行前月末日TTSレート換算円貨以上回答いたします。

差出人: Mizumata Shinji（水俣晋二）

送信日時: 2026年3月10日 09:56

宛先: Itsuo Sakai ; Kudo Atsushi（工藤淳史） ; Masaya Iida

件名: RE: BT-SIG認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

工藤の代わりにご連絡致します。

Realtek より下記の DID で確認頂きたいと連絡がありました。

Bluetooth IC DID : [ID]

Controller Stack DID : [ID]

Host Stack DID :[ID]

お忙しいところお手数お掛けしますが、

ご確認のほど、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, March 9, 2026 4:23 PM

To: Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー工藤様アリオンで Bluetooth 認証を担当しています酒井です。よろしくお願いします。

飯田に代わりご質問にお答えします。
＞ (1) 認証登録済で、 ICS 不整合のない登録であること、
⇒ こちら添付ファイルを確認していただくことは可能でしょうか？

送付頂いた ICS を読み込んで Cnsistency
Check を行うと以下の Invalid( 不整合 ) が発生します。このままでは登録サイトの「Specify the Design」ページで Host
Subsystem

とともに QDID/DN を Include 後に [Use
This Design Without Modifications] をチェックして登録を進めるしか方法がありません。

しかし、 Invalid が登録サイトの判断の許容範囲でないとコア階層に試験要求が発生することがあります。コア階層の試験は試験機関および費用的に天文学的費用になりますので他の「Invalid が発生しない」 SoC/ モジュール / ホストスタックを選択して、

試験免除登録を行うことをお勧めします。

また見積確定に必要なのは、見積依頼書に TBD （Realtek に確認中）と書かれた QDID/DN

ですが、「ICS 不整合のある登録」でも [Use
This Design Without Modifications] で試験要求も発生せずに新規登録できることもありますので Realtek から参照先登録候補が示されたら確認しますのでご連絡ください。

HCI

4:C.157 | If [HCI] (1a/1 and 4/13) are Supported then [HCI] (4/10) is Mandatory

5:Prerequisite | If [CORE] (1a/54) is Not Supported then [HCI] (5/34a, 5/35a and 5/67-69) are Excluded

IAL

2:C.1 | If [IAL] (1/3) is Supported then it is Mandatory to Support at least one of [IAL] (2/1-2)

2:C.2 | If [IAL] (1/4) is Supported then [IAL] (2/3) is Mandatory

2:C.3 | If [IAL] (1/5) is Supported then [IAL] (2/4) is Mandatory

LL

9:C.44 | If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/48) is Excluded

4a:C.1 | If [LL] (1/2 and 4/8) are Supported then [LL] (4a/1) is Mandatory

4a:C.3 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/3) is Mandatory

4a:C.5 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/5) is Mandatory

4a:C.7 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/7) is Mandatory

4a:C.7 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/7) is Mandatory

9:C.55 | If [LL] (9/31) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/32) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/48) is Supported then [LL] (9/60) is Mandatory

9:C.57 | If [LL] (9/15) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/16) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/19) is Supported then [LL] (9/62) is Mandatory

LMP

2a:C.56 | If [HCI] (13/7) is Supported then [LMP] (2a/56) is Mandatory

2b:C.1 | If [LMP] (2/17) is Supported then [LMP] (2b/1) is Mandatory

2b:C.3 | If [LMP] (2/18) is Supported then [LMP] (2b/3) is Mandatory

30:C.0 | If [LMP] (2/1) is Supported then [LMP] (30/0a and 30/0b) are Mandatory

30:C.1 | If [LMP] (2/2) is Supported then [LMP] (30/1a and 30/1b) are Mandatory

30:C.11 | If [LMP] (2/12) is Supported then [LMP] (30/11) is Mandatory

30:C.25 | If [LMP] (2/17) is Supported then [LMP] (30/25) is Mandatory

30:C.26 | If [LMP] (2/17a) is Supported then [LMP] (30/26) is Mandatory

30:C.31 | If [LMP] (2/15) is Supported then [LMP] (30/31) is Mandatory

30:C.45 | If [LMP] (2/18) is Supported then [LMP] (30/45) is Mandatory

30:C.46 | If [LMP] (2/18a) is Supported then [LMP] (30/46) is Mandatory

31:C.1 | If [RF] (1/1) is Supported then [LMP] (31/1) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/12) are Supported then [LMP] (2a/53) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/15) are Supported then [LMP] (2a/53) is Mandatory

以上回答いたします。

差出人 :
Kudo Atsushi （工藤淳史）

送信日時 :
2026 年 3 月 9 日
15:01

宛先 :
Masaya Iida

件名 :
RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

下記ご確認していただく事は可能でしょうか？

問題なければいただいた内容で進めさせていただきたいので、ご確認よろしくお願い致します。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Kudo Atsushi （工藤淳史）

Sent: Thursday, March 5, 2026 11:05 AM

To: 'Masaya Iida'

Subject: RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

返信が遅くなり申し訳ありません。

お見積りありがとうございます。

下記前提の件ご確認をお願い致します。

＞ (1) 認証登録済で、 ICS 不整合のない登録であること、

⇒こちら添付ファイルを確認していただくことは可能でしょうか？

＞ (2) ホストスタックに AVCTP,
AVDTP, GADTP を含むこと

⇒こちら対応しております。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Masaya Iida

Sent: Wednesday, February 25, 2026 5:32 PM

To: Kudo Atsushi （工藤淳史）

Subject: RE: [ID] 認証依頼ソアー工藤様アリオンの飯田です。

見積依頼書のご提出ありがとうございました。

当社サポート費用は以下の通りです。

確認中の実装モジュールおよびホストスタックが

(1) 認証登録済で、 ICS 不整合のない登録であること、

(2) ホストスタックに AVCTP,
AVDTP, GADTP を含むことを前提にした見積は以下の通りです。

・ PTS 試験（A2DP,
AVRCP, IOPT） ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発酵前月末日 TTS レート換算円貨

($6,000 は NTT
sonority, Inc 名義登録の場合 )

※上記は税抜き表示です。

※ US ドルは円換算して正式見積書を発行いたします。

※御社とは取引実績がまだございませんので、費用は「前払い」でお願いいたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 3. 2026-03-10 07:56

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?TWl6dW1hdGEgU2hpbmppGyRCIUo/ZUtzGyhCIBskQj84RnMhSxsoQg==?= , =?iso-2022-jp?B?S3VkbyBBdHN1c2hpGyRCIUo5KUYjGyhCIBskQj1fO0shSxsoQg==?= , Masaya Iida

株式会社ソアー水俣様アリオンの酒井です。いつも世話になっております。
1. 当社製品では BLE を使用せず BR/EDR のペアリングのみを実装していますが、
このような製品に対して、SIG 認証を BR/EDR のみを対象として行うことは一般的でしょうか。

⇒2024年7月1日に登録制度が現在のQualifiction Workspaceに更新されて以降、

セットメーカーが登録済BR/EDR/LE対応S0C/モジュールと登録済BR/EDR/LE対応

Host Stackを参照した登録BR/EDRのみ、あるいはBLEのみサポートであっても登録はBR/EDR/LE対応としてしか登録できなくなりました。理由は階層間不整合確認が強化されたため、BR/EDR/LE共用上位階層のGAP, L2CAPが下位階層のLL,LMP

のどちらかが存在しないとConsystency CheckでInvalidが発生します。このため、

下位階層もBR/EDR/LEサポートが必須となります。GAPとL2CAPをBR/EDRのみ、あるいはBLEのみサポートとして製品で新たにプロトコル試験を実施してPassレポートをエビデンスとしてアップロードして下位階層もBR/EDRだけのRF, BB, LMPまたは

BLEだけのRF PHY, LLだけ残して他を削除することも「理屈の上では可能」ですが、製品上では中間階層の試験ができずソースコードもないためにスタックベンダへの依頼となります。これが期間的にも費用的(200-300万円)にも非現実的なためセットメーカーは実装では不要なモードのスキャニングあるいはペアリング手段を実装しないで実質的にBR/EDRのみ、あるいはBLEのみサポート製品として販売していて、当社でも10件ほどの実績があります。(この方法は一般的というより手間と費用が納得できるレベルで実現できる登録手段が欠落しているためにそうぜさるを得ないというのが実態です。）
2. ご提示いただいたお見積りでは、BLE をサポートする場合には RF PHY 試験が追加実施される旨の記載がありました。
これは現在の見積金額に加算されるという理解でよろしいでしょうか。
また、追加費用の目安があればご教示いただけますでしょうか。

⇒「BLEをサポート」というのは製品としてBLEのAdvertizingあるはScanningが可能な実装となっている場合で、それが実装されていなければ（製品としてBLEの電波発射ができなければ）RF PHY 試験は不要です。
3. 「RFフル項目試験」について、BR/EDR のみの場合と BR/EDR + BLE をサポートする場合では試験内容（内訳）がどのように異なるのか、分かる範囲で教えていただくことは可能でしょうか。

⇒RFとRF PHYは独立階層で依存関係は一切ないため、どちらの場合でも試験内容は

26項目で同じです。
4. BR/EDR 試験、BLE 試験、プロファイル試験、登録手続きなど、それぞれの試験・認証プロセスにおいて、認証申請から認証取得完了までのおおよその期間（リードタイム）を教えていただけますでしょうか。

⇒(1) RF試験：テストモードに正常応答するテストサンプルでは所要3営業日

(2) RF PHY試験：オプションモードが多く、正常応答するテストサンプルでは所要最低1営業日〜15営業日程度

(3) プロファイル試験：前メールでプロファイル試験の項目を参入しましたが、

これは先日のICSファイルから算出したもので、今回の「Controller Stack

DID : 207390およびHost Stack DID :[ID]」を参照[Combine Unmodified

Design]の登録手順では免除されて実施不要です。

(4) 登録手続：RF試験完了後3営業日程度

(5) BLEモードを使えない実装で、プロファイル試験免除の場合の見積金額・RFフル項目試験 ￥1,200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

・ドル送金代行手数料 ￥100,000

・Qualification Fee($6,000) 正式見積書発行前月末日TTSレート換算円貨以上回答いたします。

差出人: Mizumata Shinji（水俣晋二）

送信日時: 2026年3月10日 16:06

宛先: Itsuo Sakai ; Kudo Atsushi（工藤淳史） ; Masaya Iida

件名: RE: BT-SIG認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

お見積りおよび詳細なご説明ありがとうございました。

内容を確認し、以下の点について追加で確認させて下さい。

1. 当社製品では BLE
を使用せず BR/EDR のペアリングのみを実装していますが、

このような製品に対して、 SIG
認証を BR/EDR のみを対象として行うことは一般的でしょうか。

2. ご提示いただいたお見積りでは、 BLE
をサポートする場合には RF PHY 試験が追加実施される旨の記載がありました。

これは現在の見積金額に加算されるという理解でよろしいでしょうか。

また、追加費用の目安があればご教示いただけますでしょうか。

3. 「RF フル項目試験」について、 BR/EDR
のみの場合と BR/EDR + BLE をサポートする場合では試験内容（内訳）がどのように異なるのか、分かる範囲で教えていただくことは可能でしょうか。

4. BR/EDR
試験、 BLE 試験、プロファイル試験、登録手続きなど、

それぞれの試験・認証プロセスにおいて、

認証申請から認証取得完了までのおおよその期間（リードタイム）を教えていただけますでしょうか。

お忙しいところお手数をおかけいたしますが、

ご確認のほど、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, March 10, 2026 12:22 PM

To: Mizumata Shinji （水俣晋二） ; Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー水俣様、工藤様アリオンの酒井です。いつも世話になっております。

Realtek からの DID 情報展開ありがとうございます。

ご連絡いただいた「Bluetooth IC DID : [ID]」は Controller
Stack DID : [ID]

および Host Stack DID :[ID] を一部組み合わせた「BLE オンリーの End
Product 登録」

です。

先日いただた見積依頼書には BR/EDR にチェックが入っていますので、 BLE オンリー登録の「Bluetooth IC DID : [ID]」は適しないものと思われますが、参照している

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を直接参照すれば

BR/EDR の新規製品登録が可能です。ただし、 2024/07/01 以降の現行登録制度では、参照先の QDID/DN が BR/EDR/LE の場合にはそのまま踏襲しないで Core 階層を削除すると Invalid

が発生しますので、今回も BR/EDR/LE 登録の「Controller
Stack DID : [ID] および

Host Stack DID :[ID]」もそのまま踏襲して BR/EDR/LE 登録し、製品実装で BR/EDR のペアリングのみを実装して実質的に BR/EDR 製品として製品化する方法となりますのでご了承ください。

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を参照した登録を仮

Project で確認した結果、 GAP に 56 件の Invalid が発生します。当然、参照先の [ID] を登録した時点では No Invalid でしか登録できないため、登録後に追加あるいは変更されたチェックルールに起因するもので、このケースでは [Combine Unmodified Design] という登録手順が準備されています。この手順は参照先のサポート階層、各階層の ICS 機能および包含する Invalid をそのまま踏襲する ( 取捨選択できない ) 登録となりますが SIG が特定で許容した有効な登録が可能です。

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を参照し、 [Combine

Unmodified Design] の登録手順ならば登録可能で、見積は以下の通りです。（見積依頼書の BR/EDR のチェックを前提としています。もし BLE もサポートした製品では RF
PHY 試験が追加実施が発生します。 )

・ RF フル項目試験 ￥ 1,200,000

・プロファアイル試験 (A2DP, AVRCP, IOPT) ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発行前月末日 TTS レート換算円貨以上回答いたします。

差出人 :
Mizumata Shinji （水俣晋二）

送信日時 :
2026 年 3 月 10 日
09:56

宛先 :
Itsuo Sakai ; Kudo Atsushi （工藤淳史） ; Masaya Iida

件名 :
RE: [ID] 認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

工藤の代わりにご連絡致します。

Realtek より下記の DID で確認頂きたいと連絡がありました。

Bluetooth IC DID : [ID]

Controller Stack DID : [ID]

Host Stack DID :[ID]

お忙しいところお手数お掛けしますが、

ご確認のほど、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, March 9, 2026 4:23 PM

To: Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー工藤様アリオンで Bluetooth 認証を担当しています酒井です。よろしくお願いします。

飯田に代わりご質問にお答えします。
＞ (1) 認証登録済で、 ICS 不整合のない登録であること、
⇒ こちら添付ファイルを確認していただくことは可能でしょうか？

送付頂いた ICS を読み込んで Cnsistency
Check を行うと以下の Invalid( 不整合 ) が発生します。このままでは登録サイトの「Specify the Design」ページで Host
Subsystem

とともに QDID/DN を Include 後に [Use
This Design Without Modifications] をチェックして登録を進めるしか方法がありません。

しかし、 Invalid が登録サイトの判断の許容範囲でないとコア階層に試験要求が発生することがあります。コア階層の試験は試験機関および費用的に天文学的費用になりますので他の「Invalid が発生しない」 SoC/ モジュール / ホストスタックを選択して、

試験免除登録を行うことをお勧めします。

また見積確定に必要なのは、見積依頼書に TBD （Realtek に確認中）と書かれた QDID/DN

ですが、「ICS 不整合のある登録」でも [Use
This Design Without Modifications] で試験要求も発生せずに新規登録できることもありますので Realtek から参照先登録候補が示されたら確認しますのでご連絡ください。

HCI

4:C.157 | If [HCI] (1a/1 and 4/13) are Supported then [HCI] (4/10) is Mandatory

5:Prerequisite | If [CORE] (1a/54) is Not Supported then [HCI] (5/34a, 5/35a and 5/67-69) are Excluded

IAL

2:C.1 | If [IAL] (1/3) is Supported then it is Mandatory to Support at least one of [IAL] (2/1-2)

2:C.2 | If [IAL] (1/4) is Supported then [IAL] (2/3) is Mandatory

2:C.3 | If [IAL] (1/5) is Supported then [IAL] (2/4) is Mandatory

LL

9:C.44 | If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/48) is Excluded

4a:C.1 | If [LL] (1/2 and 4/8) are Supported then [LL] (4a/1) is Mandatory

4a:C.3 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/3) is Mandatory

4a:C.5 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/5) is Mandatory

4a:C.7 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/7) is Mandatory

4a:C.7 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/7) is Mandatory

9:C.55 | If [LL] (9/31) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/32) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/48) is Supported then [LL] (9/60) is Mandatory

9:C.57 | If [LL] (9/15) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/16) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/19) is Supported then [LL] (9/62) is Mandatory

LMP

2a:C.56 | If [HCI] (13/7) is Supported then [LMP] (2a/56) is Mandatory

2b:C.1 | If [LMP] (2/17) is Supported then [LMP] (2b/1) is Mandatory

2b:C.3 | If [LMP] (2/18) is Supported then [LMP] (2b/3) is Mandatory

30:C.0 | If [LMP] (2/1) is Supported then [LMP] (30/0a and 30/0b) are Mandatory

30:C.1 | If [LMP] (2/2) is Supported then [LMP] (30/1a and 30/1b) are Mandatory

30:C.11 | If [LMP] (2/12) is Supported then [LMP] (30/11) is Mandatory

30:C.25 | If [LMP] (2/17) is Supported then [LMP] (30/25) is Mandatory

30:C.26 | If [LMP] (2/17a) is Supported then [LMP] (30/26) is Mandatory

30:C.31 | If [LMP] (2/15) is Supported then [LMP] (30/31) is Mandatory

30:C.45 | If [LMP] (2/18) is Supported then [LMP] (30/45) is Mandatory

30:C.46 | If [LMP] (2/18a) is Supported then [LMP] (30/46) is Mandatory

31:C.1 | If [RF] (1/1) is Supported then [LMP] (31/1) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/12) are Supported then [LMP] (2a/53) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/15) are Supported then [LMP] (2a/53) is Mandatory

以上回答いたします。

差出人 :
Kudo Atsushi （工藤淳史）

送信日時 :
2026 年 3 月 9 日
15:01

宛先 :
Masaya Iida

件名 :
RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

下記ご確認していただく事は可能でしょうか？

問題なければいただいた内容で進めさせていただきたいので、ご確認よろしくお願い致します。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Kudo Atsushi （工藤淳史）

Sent: Thursday, March 5, 2026 11:05 AM

To: 'Masaya Iida'

Subject: RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

返信が遅くなり申し訳ありません。

お見積りありがとうございます。

下記前提の件ご確認をお願い致します。

＞ (1) 認証登録済で、 ICS 不整合のない登録であること、

⇒こちら添付ファイルを確認していただくことは可能でしょうか？

＞ (2) ホストスタックに AVCTP,
AVDTP, GADTP を含むこと

⇒こちら対応しております。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Masaya Iida

Sent: Wednesday, February 25, 2026 5:32 PM

To: Kudo Atsushi （工藤淳史）

Subject: RE: [ID] 認証依頼ソアー工藤様アリオンの飯田です。

見積依頼書のご提出ありがとうございました。

当社サポート費用は以下の通りです。

確認中の実装モジュールおよびホストスタックが

(1) 認証登録済で、 ICS 不整合のない登録であること、

(2) ホストスタックに AVCTP,
AVDTP, GADTP を含むことを前提にした見積は以下の通りです。

・ PTS 試験（A2DP,
AVRCP, IOPT） ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発酵前月末日 TTS レート換算円貨

($6,000 は NTT
sonority, Inc 名義登録の場合 )

※上記は税抜き表示です。

※ US ドルは円換算して正式見積書を発行いたします。

※御社とは取引実績がまだございませんので、費用は「前払い」でお願いいたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 4. 2026-03-11 05:25

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?TWl6dW1hdGEgU2hpbmppGyRCIUo/ZUtzGyhCIBskQj84RnMhSxsoQg==?= , =?iso-2022-jp?B?S3VkbyBBdHN1c2hpGyRCIUo5KUYjGyhCIBskQj1fO0shSxsoQg==?= , Masaya Iida
**Attachments:** ���������������������������.doc, [ID]doc, Bluetooth���������RF������������������������������.pdf

株式会社ソアー水俣様アリオンの酒井です。いつもお世話になっております。
以下内容でお見積りをお願いできますでしょうか。
(5) BLEモードを使えない実装で、プロファイル試験免除の場合の見積金額
RFフル項目試験 ￥1,200,000
代行登録サポート（Multi-Design参照） ￥250,000
コンプライアンスフォルダ作成費 ￥150,000
ドル送金代行手数料 ￥100,000
Qualification Fee（$6,000）　正式見積書発行前月末日の TTS レート換算円貨

⇒承知しました。別途営業の飯田から送付させていただきます。
また、試験および認証にあたり、弊社で準備が必要な内容についてご教示いただけますと幸いです。

⇒以下の通りです。

・試験に必要な製品の台数：1台（別紙の改造が必要です。）

・試験に必要な環境や付帯設備：もしあれば、SoCメーカー提供の試験用DUTモード投入用PCアプリ・申請書類や技術資料として弊社が事前に提出すべきもの：別紙のQUESTIONAIRSのご提出および試験完了後に代行登録内容確認書のご提出・登録完了後までに必要なコンプライアンスフォルダ用技術資料：(1)操作マニュアル(Bluetooth部分)

(2)製品のブロック図 （3)製品の外形図 (4)アンテナデータシート(放射利得特性図を含むもの)

・その他、事前に準備すべき事項や注意点：上記内容で全てです。

以上よろしくお願いいたします。

差出人: Mizumata Shinji（水俣晋二）

送信日時: 2026年3月11日 14:04

宛先: Itsuo Sakai ; Kudo Atsushi（工藤淳史） ; Masaya Iida

件名: RE: BT-SIG認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

以下内容でお見積りをお願いできますでしょうか。

(5) BLE モードを使えない実装で、プロファイル試験免除の場合の見積金額

RF フル項目試験 ￥ 1,200,000

代行登録サポート（Multi-Design 参照） ￥ 250,000

コンプライアンスフォルダ作成費 ￥ 150,000

ドル送金代行手数料 ￥ 100,000

Qualification Fee （$6,000）　正式見積書発行前月末日の TTS
レート換算円貨また、試験および認証にあたり、弊社で準備が必要な内容についてご教示いただけますと幸いです。

・試験に必要な製品の台数

（例：動作品、予備品、限定モード設定品など）

・試験に必要な環境や付帯設備

（例：評価用ソフト、治具、電源、通信ログ取得環境等）

・申請書類や技術資料として弊社が事前に提出すべきもの

（回路図、ブロック図、無線仕様書、ユーザーマニュアルなど）

・その他、事前に準備すべき事項や注意点お忙しいところお手数をおかけいたしますが、

ご確認のほどよろしくお願いいたします。

From: Mizumata Shinji （水俣晋二）

Sent: Tuesday, March 10, 2026 5:38 PM

To: 'Itsuo Sakai' ; Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: RE: [ID] 認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

ご確認ありがとうございます。

いただいた内容について社内で確認いたしますので、

少しお時間をいただければ幸いです。

引き続きよろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, March 10, 2026 4:56 PM

To: Mizumata Shinji （水俣晋二） ; Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー水俣様アリオンの酒井です。いつも世話になっております。
1.
当社製品では BLE
を使用せず BR/EDR
のペアリングのみを実装していますが、
このような製品に対して、 SIG
認証を BR/EDR
のみを対象として行うことは一般的でしょうか。

⇒ 2024 年 7 月 1 日に登録制度が現在の Qualifiction
Workspace に更新されて以降、

セットメーカーが登録済 BR/EDR/LE 対応 S0C/ モジュールと登録済 BR/EDR/LE 対応

Host Stack を参照した登録 BR/EDR のみ、あるいは BLE のみサポートであっても登録は BR/EDR/LE 対応としてしか登録できなくなりました。理由は階層間不整合確認が強化されたため、 BR/EDR/LE 共用上位階層の GAP,
L2CAP が下位階層の LL,LMP

のどちらかが存在しないと Consystency Check で Invalid が発生します。このため、

下位階層も BR/EDR/LE サポートが必須となります。 GAP と L2CAP を BR/EDR のみ、あるいは BLE のみサポートとして製品で新たにプロトコル試験を実施して Pass レポートをエビデンスとしてアップロードして下位階層も BR/EDR だけの RF,
BB, LMP または

BLE だけの RF
PHY, LL だけ残して他を削除することも「理屈の上では可能」ですが、製品上では中間階層の試験ができずソースコードもないためにスタックベンダへの依頼となります。これが期間的にも費用的 ([ID] 万円 ) にも非現実的なためセットメーカーは実装では不要なモードのスキャニングあるいはペアリング手段を実装しないで実質的に BR/EDR のみ、あるいは BLE のみサポート製品として販売していて、当社でも 10 件ほどの実績があります。 ( この方法は一般的というより手間と費用が納得できるレベルで実現できる登録手段が欠落しているためにそうぜさるを得ないというのが実態です。）
2.
ご提示いただいたお見積りでは、 BLE
をサポートする場合には RF PHY
試験が追加実施される旨の記載がありました。
これは現在の見積金額に加算されるという理解でよろしいでしょうか。
また、追加費用の目安があればご教示いただけますでしょうか。

⇒ 「BLE をサポート」というのは製品として BLE の Advertizing あるは Scanning が可能な実装となっている場合で、それが実装されていなければ（製品として BLE の電波発射ができなければ） RF PHY
試験は不要です。
3.
「RF フル項目試験」について、 BR/EDR
のみの場合と BR/EDR + BLE
をサポートする場合では試験内容（内訳）がどのように異なるのか、分かる範囲で教えていただくことは可能でしょうか。

⇒ RF と RF
PHY は独立階層で依存関係は一切ないため、どちらの場合でも試験内容は

26 項目で同じです。
4. BR/EDR
試験、 BLE
試験、プロファイル試験、登録手続きなど、それぞれの試験・認証プロセスにおいて、認証申請から認証取得完了までのおおよその期間（リードタイム）を教えていただけますでしょうか。

⇒ (1) RF 試験：テストモードに正常応答するテストサンプルでは所要 3 営業日

(2) RF PHY 試験：オプションモードが多く、正常応答するテストサンプルでは所要最低 1 営業日〜 15 営業日程度

(3)
プロファイル試験：前メールでプロファイル試験の項目を参入しましたが、

これは先日の ICS ファイルから算出したもので、今回の「Controller
Stack

DID : [ID] および Host
Stack DID :[ID]」を参照 [Combine Unmodified

Design] の登録手順では免除されて実施不要です。

(4)
登録手続： RF 試験完了後 3 営業日程度

(5) BLE モードを使えない実装で、プロファイル試験免除の場合の見積金額・ RF フル項目試験 ￥ 1,200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発行前月末日 TTS レート換算円貨以上回答いたします。

差出人 :
Mizumata Shinji （水俣晋二）

送信日時 :
2026 年 3 月 10 日
16:06

宛先 :
Itsuo Sakai ; Kudo Atsushi （工藤淳史） ; Masaya Iida

件名 :
RE: [ID] 認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

お見積りおよび詳細なご説明ありがとうございました。

内容を確認し、以下の点について追加で確認させて下さい。

1. 当社製品では BLE
を使用せず BR/EDR のペアリングのみを実装していますが、

このような製品に対して、 SIG
認証を BR/EDR のみを対象として行うことは一般的でしょうか。

2. ご提示いただいたお見積りでは、 BLE
をサポートする場合には RF PHY 試験が追加実施される旨の記載がありました。

これは現在の見積金額に加算されるという理解でよろしいでしょうか。

また、追加費用の目安があればご教示いただけますでしょうか。

3. 「RF フル項目試験」について、 BR/EDR
のみの場合と BR/EDR + BLE をサポートする場合では試験内容（内訳）がどのように異なるのか、分かる範囲で教えていただくことは可能でしょうか。

4. BR/EDR
試験、 BLE 試験、プロファイル試験、登録手続きなど、

それぞれの試験・認証プロセスにおいて、

認証申請から認証取得完了までのおおよその期間（リードタイム）を教えていただけますでしょうか。

お忙しいところお手数をおかけいたしますが、

ご確認のほど、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, March 10, 2026 12:22 PM

To: Mizumata Shinji （水俣晋二） ; Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー水俣様、工藤様アリオンの酒井です。いつも世話になっております。

Realtek からの DID 情報展開ありがとうございます。

ご連絡いただいた「Bluetooth IC DID : [ID]」は Controller
Stack DID : [ID]

および Host Stack DID :[ID] を一部組み合わせた「BLE オンリーの End
Product 登録」

です。

先日いただた見積依頼書には BR/EDR にチェックが入っていますので、 BLE オンリー登録の「Bluetooth IC DID : [ID]」は適しないものと思われますが、参照している

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を直接参照すれば

BR/EDR の新規製品登録が可能です。ただし、 2024/07/01 以降の現行登録制度では、参照先の QDID/DN が BR/EDR/LE の場合にはそのまま踏襲しないで Core 階層を削除すると Invalid

が発生しますので、今回も BR/EDR/LE 登録の「Controller
Stack DID : [ID] および

Host Stack DID :[ID]」もそのまま踏襲して BR/EDR/LE 登録し、製品実装で BR/EDR のペアリングのみを実装して実質的に BR/EDR 製品として製品化する方法となりますのでご了承ください。

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を参照した登録を仮

Project で確認した結果、 GAP に 56 件の Invalid が発生します。当然、参照先の [ID] を登録した時点では No Invalid でしか登録できないため、登録後に追加あるいは変更されたチェックルールに起因するもので、このケースでは [Combine Unmodified Design] という登録手順が準備されています。この手順は参照先のサポート階層、各階層の ICS 機能および包含する Invalid をそのまま踏襲する ( 取捨選択できない ) 登録となりますが SIG が特定で許容した有効な登録が可能です。

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を参照し、 [Combine

Unmodified Design] の登録手順ならば登録可能で、見積は以下の通りです。（見積依頼書の BR/EDR のチェックを前提としています。もし BLE もサポートした製品では RF
PHY 試験が追加実施が発生します。 )

・ RF フル項目試験 ￥ 1,200,000

・プロファアイル試験 (A2DP, AVRCP, IOPT) ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発行前月末日 TTS レート換算円貨以上回答いたします。

差出人 :
Mizumata Shinji （水俣晋二）

送信日時 :
2026 年 3 月 10 日
09:56

宛先 :
Itsuo Sakai ; Kudo Atsushi （工藤淳史） ; Masaya Iida

件名 :
RE: [ID] 認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

工藤の代わりにご連絡致します。

Realtek より下記の DID で確認頂きたいと連絡がありました。

Bluetooth IC DID : [ID]

Controller Stack DID : [ID]

Host Stack DID :[ID]

お忙しいところお手数お掛けしますが、

ご確認のほど、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, March 9, 2026 4:23 PM

To: Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー工藤様アリオンで Bluetooth 認証を担当しています酒井です。よろしくお願いします。

飯田に代わりご質問にお答えします。
＞ (1) 認証登録済で、 ICS 不整合のない登録であること、
⇒ こちら添付ファイルを確認していただくことは可能でしょうか？

送付頂いた ICS を読み込んで Cnsistency
Check を行うと以下の Invalid( 不整合 ) が発生します。このままでは登録サイトの「Specify the Design」ページで Host
Subsystem

とともに QDID/DN を Include 後に [Use
This Design Without Modifications] をチェックして登録を進めるしか方法がありません。

しかし、 Invalid が登録サイトの判断の許容範囲でないとコア階層に試験要求が発生することがあります。コア階層の試験は試験機関および費用的に天文学的費用になりますので他の「Invalid が発生しない」 SoC/ モジュール / ホストスタックを選択して、

試験免除登録を行うことをお勧めします。

また見積確定に必要なのは、見積依頼書に TBD （Realtek に確認中）と書かれた QDID/DN

ですが、「ICS 不整合のある登録」でも [Use
This Design Without Modifications] で試験要求も発生せずに新規登録できることもありますので Realtek から参照先登録候補が示されたら確認しますのでご連絡ください。

HCI

4:C.157 | If [HCI] (1a/1 and 4/13) are Supported then [HCI] (4/10) is Mandatory

5:Prerequisite | If [CORE] (1a/54) is Not Supported then [HCI] (5/34a, 5/35a and 5/67-69) are Excluded

IAL

2:C.1 | If [IAL] (1/3) is Supported then it is Mandatory to Support at least one of [IAL] (2/1-2)

2:C.2 | If [IAL] (1/4) is Supported then [IAL] (2/3) is Mandatory

2:C.3 | If [IAL] (1/5) is Supported then [IAL] (2/4) is Mandatory

LL

9:C.44 | If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/48) is Excluded

4a:C.1 | If [LL] (1/2 and 4/8) are Supported then [LL] (4a/1) is Mandatory

4a:C.3 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/3) is Mandatory

4a:C.5 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/5) is Mandatory

4a:C.7 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/7) is Mandatory

4a:C.7 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/7) is Mandatory

9:C.55 | If [LL] (9/31) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/32) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/48) is Supported then [LL] (9/60) is Mandatory

9:C.57 | If [LL] (9/15) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/16) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/19) is Supported then [LL] (9/62) is Mandatory

LMP

2a:C.56 | If [HCI] (13/7) is Supported then [LMP] (2a/56) is Mandatory

2b:C.1 | If [LMP] (2/17) is Supported then [LMP] (2b/1) is Mandatory

2b:C.3 | If [LMP] (2/18) is Supported then [LMP] (2b/3) is Mandatory

30:C.0 | If [LMP] (2/1) is Supported then [LMP] (30/0a and 30/0b) are Mandatory

30:C.1 | If [LMP] (2/2) is Supported then [LMP] (30/1a and 30/1b) are Mandatory

30:C.11 | If [LMP] (2/12) is Supported then [LMP] (30/11) is Mandatory

30:C.25 | If [LMP] (2/17) is Supported then [LMP] (30/25) is Mandatory

30:C.26 | If [LMP] (2/17a) is Supported then [LMP] (30/26) is Mandatory

30:C.31 | If [LMP] (2/15) is Supported then [LMP] (30/31) is Mandatory

30:C.45 | If [LMP] (2/18) is Supported then [LMP] (30/45) is Mandatory

30:C.46 | If [LMP] (2/18a) is Supported then [LMP] (30/46) is Mandatory

31:C.1 | If [RF] (1/1) is Supported then [LMP] (31/1) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/12) are Supported then [LMP] (2a/53) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/15) are Supported then [LMP] (2a/53) is Mandatory

以上回答いたします。

差出人 :
Kudo Atsushi （工藤淳史）

送信日時 :
2026 年 3 月 9 日
15:01

宛先 :
Masaya Iida

件名 :
RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

下記ご確認していただく事は可能でしょうか？

問題なければいただいた内容で進めさせていただきたいので、ご確認よろしくお願い致します。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Kudo Atsushi （工藤淳史）

Sent: Thursday, March 5, 2026 11:05 AM

To: 'Masaya Iida'

Subject: RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

返信が遅くなり申し訳ありません。

お見積りありがとうございます。

下記前提の件ご確認をお願い致します。

＞ (1) 認証登録済で、 ICS 不整合のない登録であること、

⇒こちら添付ファイルを確認していただくことは可能でしょうか？

＞ (2) ホストスタックに AVCTP,
AVDTP, GADTP を含むこと

⇒こちら対応しております。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Masaya Iida

Sent: Wednesday, February 25, 2026 5:32 PM

To: Kudo Atsushi （工藤淳史）

Subject: RE: [ID] 認証依頼ソアー工藤様アリオンの飯田です。

見積依頼書のご提出ありがとうございました。

当社サポート費用は以下の通りです。

確認中の実装モジュールおよびホストスタックが

(1) 認証登録済で、 ICS 不整合のない登録であること、

(2) ホストスタックに AVCTP,
AVDTP, GADTP を含むことを前提にした見積は以下の通りです。

・ PTS 試験（A2DP,
AVRCP, IOPT） ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発酵前月末日 TTS レート換算円貨

($6,000 は NTT
sonority, Inc 名義登録の場合 )

※上記は税抜き表示です。

※ US ドルは円換算して正式見積書を発行いたします。

※御社とは取引実績がまだございませんので、費用は「前払い」でお願いいたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 5. 2026-03-11 05:28

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

ソアー、水俣様に正式見積書を発行してください。
RFフル項目試験 ￥1,200,000
代行登録サポート（Multi-Design参照） ￥250,000
コンプライアンスフォルダ作成費 ￥150,000
ドル送金代行手数料 ￥100,000
Qualification Fee（$6,000）　正式見積書発行前月末日の TTS レート換算円貨酒井差出人: Itsuo Sakai

送信日時: 2026年3月11日 14:25

宛先: Mizumata Shinji（水俣晋二） ; Kudo Atsushi（工藤淳史） ; Masaya Iida

件名: Re: BT-SIG認証依頼株式会社ソアー水俣様アリオンの酒井です。いつもお世話になっております。
以下内容でお見積りをお願いできますでしょうか。
(5) BLEモードを使えない実装で、プロファイル試験免除の場合の見積金額
RFフル項目試験 ￥1,200,000
代行登録サポート（Multi-Design参照） ￥250,000
コンプライアンスフォルダ作成費 ￥150,000
ドル送金代行手数料 ￥100,000
Qualification Fee（$6,000）　正式見積書発行前月末日の TTS レート換算円貨

⇒承知しました。別途営業の飯田から送付させていただきます。
また、試験および認証にあたり、弊社で準備が必要な内容についてご教示いただけますと幸いです。

⇒以下の通りです。

・試験に必要な製品の台数：1台（別紙の改造が必要です。）

・試験に必要な環境や付帯設備：もしあれば、SoCメーカー提供の試験用DUTモード投入用PCアプリ・申請書類や技術資料として弊社が事前に提出すべきもの：別紙のQUESTIONAIRSのご提出および試験完了後に代行登録内容確認書のご提出・登録完了後までに必要なコンプライアンスフォルダ用技術資料：(1)操作マニュアル(Bluetooth部分)

(2)製品のブロック図 （3)製品の外形図 (4)アンテナデータシート(放射利得特性図を含むもの)

・その他、事前に準備すべき事項や注意点：上記内容で全てです。

以上よろしくお願いいたします。

差出人: Mizumata Shinji（水俣晋二）

送信日時: 2026年3月11日 14:04

宛先: Itsuo Sakai ; Kudo Atsushi（工藤淳史） ; Masaya Iida

件名: RE: BT-SIG認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

以下内容でお見積りをお願いできますでしょうか。

(5) BLEモードを使えない実装で、プロファイル試験免除の場合の見積金額

RFフル項目試験 ￥1,200,000

代行登録サポート（Multi-Design参照） ￥250,000

コンプライアンスフォルダ作成費 ￥150,000

ドル送金代行手数料 ￥100,000

Qualification Fee（$6,000）　正式見積書発行前月末日の TTS レート換算円貨また、試験および認証にあたり、弊社で準備が必要な内容についてご教示いただけますと幸いです。

・試験に必要な製品の台数

（例：動作品、予備品、限定モード設定品など）

・試験に必要な環境や付帯設備

（例：評価用ソフト、治具、電源、通信ログ取得環境等）

・申請書類や技術資料として弊社が事前に提出すべきもの

（回路図、ブロック図、無線仕様書、ユーザーマニュアルなど）

・その他、事前に準備すべき事項や注意点お忙しいところお手数をおかけいたしますが、

ご確認のほどよろしくお願いいたします。

From: Mizumata Shinji （水俣晋二）

Sent: Tuesday, March 10, 2026 5:38 PM

To: 'Itsuo Sakai' ; Kudo Atsushi （工藤淳史） ; Masaya Iida

Subject: RE: [ID] 認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

ご確認ありがとうございます。

いただいた内容について社内で確認いたしますので、

少しお時間をいただければ幸いです。

引き続きよろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, March 10, 2026 4:56 PM

To: Mizumata Shinji （水俣晋二） ;
Kudo Atsushi （工藤淳史） ;
Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー水俣様アリオンの酒井です。いつも世話になっております。
1.
当社製品では BLE
を使用せず BR/EDR
のペアリングのみを実装していますが、

このような製品に対して、 SIG
認証を BR/EDR
のみを対象として行うことは一般的でしょうか。

⇒ 2024 年 7 月 1 日に登録制度が現在の Qualifiction
Workspace に更新されて以降、

セットメーカーが登録済 BR/EDR/LE 対応 S0C/ モジュールと登録済 BR/EDR/LE 対応

Host Stack を参照した登録 BR/EDR のみ、あるいは BLE のみサポートであっても登録は BR/EDR/LE 対応としてしか登録できなくなりました。理由は階層間不整合確認が強化されたため、 BR/EDR/LE 共用上位階層の GAP,
L2CAP が下位階層の LL,LMP

のどちらかが存在しないと Consystency Check で Invalid が発生します。このため、

下位階層も BR/EDR/LE サポートが必須となります。 GAP と L2CAP を BR/EDR のみ、あるいは BLE のみサポートとして製品で新たにプロトコル試験を実施して Pass レポートをエビデンスとしてアップロードして下位階層も BR/EDR だけの RF,
BB, LMP または

BLE だけの RF
PHY, LL だけ残して他を削除することも「理屈の上では可能」ですが、製品上では中間階層の試験ができずソースコードもないためにスタックベンダへの依頼となります。これが期間的にも費用的 ([ID] 万円 ) にも非現実的なためセットメーカーは実装では不要なモードのスキャニングあるいはペアリング手段を実装しないで実質的に BR/EDR のみ、あるいは BLE のみサポート製品として販売していて、当社でも 10 件ほどの実績があります。 ( この方法は一般的というより手間と費用が納得できるレベルで実現できる登録手段が欠落しているためにそうぜさるを得ないというのが実態です。）
2.
ご提示いただいたお見積りでは、 BLE
をサポートする場合には RF PHY
試験が追加実施される旨の記載がありました。

これは現在の見積金額に加算されるという理解でよろしいでしょうか。

また、追加費用の目安があればご教示いただけますでしょうか。

⇒ 「BLE をサポート」というのは製品として BLE の Advertizing あるは Scanning が可能な実装となっている場合で、それが実装されていなければ（製品として BLE の電波発射ができなければ） RF PHY
試験は不要です。
3.
「RF フル項目試験」について、 BR/EDR
のみの場合と BR/EDR + BLE
をサポートする場合では試験内容（内訳）がどのように異なるのか、分かる範囲で教えていただくことは可能でしょうか。

⇒ RF と RF
PHY は独立階層で依存関係は一切ないため、どちらの場合でも試験内容は

26 項目で同じです。
4. BR/EDR
試験、 BLE
試験、プロファイル試験、登録手続きなど、それぞれの試験・認証プロセスにおいて、認証申請から認証取得完了までのおおよその期間（リードタイム）を教えていただけますでしょうか。

⇒ (1) RF 試験：テストモードに正常応答するテストサンプルでは所要 3 営業日

(2) RF PHY 試験：オプションモードが多く、正常応答するテストサンプルでは所要最低 1 営業日〜 15 営業日程度

(3)
プロファイル試験：前メールでプロファイル試験の項目を参入しましたが、

これは先日の ICS ファイルから算出したもので、今回の「Controller
Stack

DID : [ID] および Host
Stack DID :[ID]」を参照 [Combine Unmodified

Design] の登録手順では免除されて実施不要です。

(4)
登録手続： RF 試験完了後 3 営業日程度

(5) BLE モードを使えない実装で、プロファイル試験免除の場合の見積金額・ RF フル項目試験 ￥ 1,200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発行前月末日 TTS レート換算円貨以上回答いたします。

差出人 : Mizumata Shinji （水俣晋二）

送信日時 : 2026 年 3 月 10 日 16:06

宛先 : Itsuo Sakai ;
Kudo Atsushi （工藤淳史） ;
Masaya Iida

件名 : RE: [ID] 認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

お見積りおよび詳細なご説明ありがとうございました。

内容を確認し、以下の点について追加で確認させて下さい。

1. 当社製品では BLE を使用せず BR/EDR のペアリングのみを実装していますが、

このような製品に対して、SIG 認証を BR/EDR のみを対象として行うことは一般的でしょうか。

2. ご提示いただいたお見積りでは、BLE をサポートする場合には RF PHY 試験が追加実施される旨の記載がありました。

これは現在の見積金額に加算されるという理解でよろしいでしょうか。

また、追加費用の目安があればご教示いただけますでしょうか。

3. 「RFフル項目試験」について、BR/EDR のみの場合と BR/EDR + BLE をサポートする場合では試験内容（内訳）がどのように異なるのか、分かる範囲で教えていただくことは可能でしょうか。

4. BR/EDR 試験、BLE 試験、プロファイル試験、登録手続きなど、

それぞれの試験・認証プロセスにおいて、

認証申請から認証取得完了までのおおよその期間（リードタイム）を教えていただけますでしょうか。

お忙しいところお手数をおかけいたしますが、

ご確認のほど、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, March 10, 2026 12:22 PM

To: Mizumata Shinji （水俣晋二） ;
Kudo Atsushi （工藤淳史） ;
Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー水俣様、工藤様アリオンの酒井です。いつも世話になっております。

Realtek からの DID 情報展開ありがとうございます。

ご連絡いただいた「Bluetooth IC DID : [ID]」は Controller
Stack DID : [ID]

および Host Stack DID :[ID] を一部組み合わせた「BLE オンリーの End
Product 登録」

です。

先日いただた見積依頼書には BR/EDR にチェックが入っていますので、 BLE オンリー登録の「Bluetooth IC DID : [ID]」は適しないものと思われますが、参照している

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を直接参照すれば

BR/EDR の新規製品登録が可能です。ただし、 2024/07/01 以降の現行登録制度では、参照先の QDID/DN が BR/EDR/LE の場合にはそのまま踏襲しないで Core 階層を削除すると Invalid

が発生しますので、今回も BR/EDR/LE 登録の「Controller
Stack DID : [ID] および

Host Stack DID :[ID]」もそのまま踏襲して BR/EDR/LE 登録し、製品実装で BR/EDR のペアリングのみを実装して実質的に BR/EDR 製品として製品化する方法となりますのでご了承ください。

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を参照した登録を仮

Project で確認した結果、 GAP に 56 件の Invalid が発生します。当然、参照先の [ID] を登録した時点では No Invalid でしか登録できないため、登録後に追加あるいは変更されたチェックルールに起因するもので、このケースでは [Combine Unmodified Design] という登録手順が準備されています。この手順は参照先のサポート階層、各階層の ICS 機能および包含する Invalid をそのまま踏襲する ( 取捨選択できない ) 登録となりますが SIG が特定で許容した有効な登録が可能です。

「Controller Stack DID : [ID] および Host
Stack DID :[ID]」を参照し、 [Combine

Unmodified Design] の登録手順ならば登録可能で、見積は以下の通りです。（見積依頼書の BR/EDR のチェックを前提としています。もし BLE もサポートした製品では RF
PHY 試験が追加実施が発生します。 )

・ RF フル項目試験 ￥ 1,200,000

・プロファアイル試験 (A2DP, AVRCP, IOPT) ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発行前月末日 TTS レート換算円貨以上回答いたします。

差出人 : Mizumata Shinji （水俣晋二）

送信日時 : 2026 年 3 月 10 日 09:56

宛先 : Itsuo Sakai ;
Kudo Atsushi （工藤淳史） ;
Masaya Iida

件名 : RE: [ID] 認証依頼アリオン酒井様お世話になっております。

株式会社ソアー水俣です。

工藤の代わりにご連絡致します。

Realtekより下記のDIDで確認頂きたいと連絡がありました。

Bluetooth IC DID : [ID]

Controller Stack DID : [ID]

Host Stack DID :[ID]

お忙しいところお手数お掛けしますが、

ご確認のほど、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, March 9, 2026 4:23 PM

To: Kudo Atsushi （工藤淳史） ;
Masaya Iida

Subject: Re: [ID] 認証依頼株式会社ソアー工藤様アリオンで Bluetooth 認証を担当しています酒井です。よろしくお願いします。

飯田に代わりご質問にお答えします。

＞ (1) 認証登録済で、 ICS 不整合のない登録であること、

⇒ こちら添付ファイルを確認していただくことは可能でしょうか？

送付頂いた ICS を読み込んで Cnsistency
Check を行うと以下の Invalid( 不整合 ) が発生します。このままでは登録サイトの「Specify the Design」ページで Host
Subsystem

とともに QDID/DN を Include 後に [Use
This Design Without Modifications] をチェックして登録を進めるしか方法がありません。

しかし、 Invalid が登録サイトの判断の許容範囲でないとコア階層に試験要求が発生することがあります。コア階層の試験は試験機関および費用的に天文学的費用になりますので他の「Invalid が発生しない」 SoC/ モジュール / ホストスタックを選択して、

試験免除登録を行うことをお勧めします。

また見積確定に必要なのは、見積依頼書に TBD （Realtek に確認中）と書かれた QDID/DN

ですが、「ICS 不整合のある登録」でも [Use
This Design Without Modifications] で試験要求も発生せずに新規登録できることもありますので Realtek から参照先登録候補が示されたら確認しますのでご連絡ください。

HCI

4:C.157 | If [HCI] (1a/1 and 4/13) are Supported then [HCI] (4/10) is Mandatory

5:Prerequisite | If [CORE] (1a/54) is Not Supported then [HCI] (5/34a, 5/35a and 5/67-69) are Excluded

IAL

2:C.1 | If [IAL] (1/3) is Supported then it is Mandatory to Support at least one of [IAL] (2/1-2)

2:C.2 | If [IAL] (1/4) is Supported then [IAL] (2/3) is Mandatory

2:C.3 | If [IAL] (1/5) is Supported then [IAL] (2/4) is Mandatory

LL

9:C.44 | If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/48) is Excluded

4a:C.1 | If [LL] (1/2 and 4/8) are Supported then [LL] (4a/1) is Mandatory

4a:C.3 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/3) is Mandatory

4a:C.5 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/5) is Mandatory

4a:C.7 | If [LL] (1/2 and 1/5) are Supported then [LL] (4a/7) is Mandatory

4a:C.7 | If [LL] (1/2 and 4/3) are Supported then [LL] (4a/7) is Mandatory

9:C.55 | If [LL] (9/31) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/32) is Supported then [LL] (9/60) is Mandatory

9:C.55 | If [LL] (9/48) is Supported then [LL] (9/60) is Mandatory

9:C.57 | If [LL] (9/15) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/16) is Supported then [LL] (9/62) is Mandatory

9:C.57 | If [LL] (9/19) is Supported then [LL] (9/62) is Mandatory

LMP

2a:C.56 | If [HCI] (13/7) is Supported then [LMP] (2a/56) is Mandatory

2b:C.1 | If [LMP] (2/17) is Supported then [LMP] (2b/1) is Mandatory

2b:C.3 | If [LMP] (2/18) is Supported then [LMP] (2b/3) is Mandatory

30:C.0 | If [LMP] (2/1) is Supported then [LMP] (30/0a and 30/0b) are Mandatory

30:C.1 | If [LMP] (2/2) is Supported then [LMP] (30/1a and 30/1b) are Mandatory

30:C.11 | If [LMP] (2/12) is Supported then [LMP] (30/11) is Mandatory

30:C.25 | If [LMP] (2/17) is Supported then [LMP] (30/25) is Mandatory

30:C.26 | If [LMP] (2/17a) is Supported then [LMP] (30/26) is Mandatory

30:C.31 | If [LMP] (2/15) is Supported then [LMP] (30/31) is Mandatory

30:C.45 | If [LMP] (2/18) is Supported then [LMP] (30/45) is Mandatory

30:C.46 | If [LMP] (2/18a) is Supported then [LMP] (30/46) is Mandatory

31:C.1 | If [RF] (1/1) is Supported then [LMP] (31/1) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/12) are Supported then [LMP] (2a/53) is Mandatory

2a:C.53 | If [HCI] (9/8) and [LMP] (2/15) are Supported then [LMP] (2a/53) is Mandatory

以上回答いたします。

差出人 : Kudo Atsushi （工藤淳史）

送信日時 : 2026 年 3 月 9 日 15:01

宛先 : Masaya Iida

件名 : RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

下記ご確認していただく事は可能でしょうか？

問題なければいただいた内容で進めさせていただきたいので、ご確認よろしくお願い致します。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Kudo Atsushi （工藤淳史）

Sent: Thursday, March 5, 2026 11:05 AM

To: 'Masaya Iida'

Subject: RE: [ID] 認証依頼アリオン飯田様お世話になっております。

株式会社ソアー工藤です。

返信が遅くなり申し訳ありません。

お見積りありがとうございます。

下記前提の件ご確認をお願い致します。

＞ (1) 認証登録済で、 ICS 不整合のない登録であること、

⇒こちら添付ファイルを確認していただくことは可能でしょうか？

＞ (2) ホストスタックに AVCTP,
AVDTP, GADTP を含むこと

⇒こちら対応しております。

以上よろしくお願い致します。

株式会社ソアー技術開発本部　ＭＳ技術開発部技術二課工藤淳史

From: Masaya Iida

Sent: Wednesday, February 25, 2026 5:32 PM

To: Kudo Atsushi （工藤淳史）

Subject: RE: [ID] 認証依頼ソアー工藤様アリオンの飯田です。

見積依頼書のご提出ありがとうございました。

当社サポート費用は以下の通りです。

確認中の実装モジュールおよびホストスタックが

(1) 認証登録済で、 ICS 不整合のない登録であること、

(2) ホストスタックに AVCTP, AVDTP, GADTP を含むことを前提にした見積は以下の通りです。

・ PTS 試験（A2DP,
AVRCP, IOPT） ￥ 300,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・ドル送金代行手数料 ￥ 100,000

・ Qualification Fee($6,000) 正式見積書発酵前月末日 TTS レート換算円貨

($6,000 は NTT sonority, Inc 名義登録の場合 )

※上記は税抜き表示です。

※ US ドルは円換算して正式見積書を発行いたします。

※御社とは取引実績がまだございませんので、費用は「前払い」でお願いいたします。

ご検討のほどよろしくお願いいたします。
