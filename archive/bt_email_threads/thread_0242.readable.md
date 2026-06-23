# thread_0242: [内部連絡] Re: 問合せ】Bluetooth 認証に必要な資料と試験について

- Message count: 1
- Source JSON: `thread_0242.json`

---

## 1. 2024-12-26 00:29

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

12/11に飯田さん宛に返信したとおり、客先から連絡のあった参照先で問題は解消しました。

見積額に変更はありません。

酒井差出人: 米澤智

送信日時: 2024年12月25日 20:45

宛先: Masaya Iida

件名: Re: 【問合せ】Bluetooth 認証に必要な資料と試験についてアリオン株式会社飯田様お世話になっております。

GO株式会社の米澤です。

こちらの件、状況はいかがでしょうか？

ご返信いただけると助かります。

お手数をおかけしますが、よろしくお願いします。

2024年12月10日(火) 23:30 米澤智 :

アリオン株式会社飯田様お世話になっております。

GO株式会社の米澤です。

連絡に間が空いてしまい、大変申し訳ありません。

Silicon Labへの確認に時間がかかっていました。

結論としては、下記を使用すると、不一致が解消されるようです。

QDID [ID] (for [ID] part) and DN [ID] (for LL , HCI and Host layers )

お手数をおかけしますが、ご確認をよろしくお願いします。

2024年10月21日(月) 12:57 Masaya Iida :

Go 株式会社米澤様いつもお世話になっております。

アリオンの飯田です。

先ほどお送りした内容は Silicon Laboratories あるいはその代理店と確認してほしい内容でした。

以下改めてご案内いたします。

見積金額は下記の通りです。

・代行登録サポート (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

・ドル送金代行手数料 ￥ 100,000

・ Declaration Fee($11,040) 正式見積書発行前月末日 TTS レート換算円貨ただ見積依頼書記載の Component 登録を Include すると階層間不整合が発生してそのままでは登録できません。そこで客先に後述の内容で Silicon Laboratories あるいはその代理店に階層間不整合を回避した Sub setting DN を作成・提供依頼するメール送信を依頼してください。

ーーーここからーーー

QDID:[ID]([ID] /Component /v5.1) と、 QDID:[ID](Wireless
Gecko Link Layer and Host

based on Core Specification 5.4 /Component /v5.4) を Include した製品登録を行うと、 LL と RFPHY

階層間で下記 13 項目の不整合 (AoA/AoD 機能および Isochronous 機能 ) が発生します。

[LL]

If [RFPHY] is Supported and [RFPHY] (1/15) is Not Supported then [LL] (9/11) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/17) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/9) is Not Supported then [LL] (9/18) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/19) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/20) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/10) is Not Supported then [LL] (9/22) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/13) is Not Supported then [LL] (9/23) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/14) is Not Supported then [LL] (9/24) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/12) is Not Supported then [LL] (9/21) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/16) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/15) is Excluded

If [CORE] is Supported and [CORE] (1a/52) is Not Supported then [LL] (9/37 and 9/39) are Excluded

If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/49) is Excluded

If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/50) is Excluded

製品登録過程で LL の ICS を修正すると LL 階層のテスト要求 ( 数百項目 ) が発生します。御社の QDID:[ID]

の Listing Owner が上記 [LL]ICS
15 項目を Support YES→NO に変更した Subset を作成 ( 無料 ) すれば解決すると思いますのでご対応をお願いします。もしすでに QDID:[ID] あるいは同等機能のデザイン登録の [LL] から AoA/AoD 機能および Isochronous 機能を Support
NO とした Subset のご準備があればその DN をお知らせください。

ーーーここまでーーー以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階内線 220

FAX [ID]

From: Masaya Iida

Sent: Monday, October 21, 2024 12:31 PM

To: 米澤智

Subject: RE: 【問合せ】 Bluetooth
認証に必要な資料と試験について

Go 株式会社米澤様いつもお世話になっております。

アリオンの飯田です。

Bluetooth SIG 認証について見積もりを確認をしております。

QDID:[ID]([ID] /Component /v5.1) と、 QDID:[ID](Wireless Gecko Link Layer and Host

based on Core Specification 5.4 /Component /v5.4) を Include した製品登録を行うと、 LL と RFPHY

階層間で下記 13 項目の不整合 (AoA/AoD 機能および Isochronous 機能 ) が発生します。

[LL]

If [RFPHY] is Supported and [RFPHY] (1/15) is Not Supported then [LL] (9/11) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/17) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/9) is Not Supported then [LL] (9/18) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/19) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/20) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/10) is Not Supported then [LL] (9/22) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/13) is Not Supported then [LL] (9/23) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/14) is Not Supported then [LL] (9/24) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/12) is Not Supported then [LL] (9/21) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/16) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/15) is Excluded

If [CORE] is Supported and [CORE] (1a/52) is Not Supported then [LL] (9/37 and 9/39) are Excluded

If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/49) is Excluded

If [CORE] is Supported and [CORE] (1a/54) is Not Supported then [LL] (9/50) is Excluded

製品登録過程で LL の ICS を修正すると LL 階層のテスト要求 ( 数百項目 ) が発生します。御社の QDID:[ID]

の Listing Owner が上記 [LL]ICS 15 項目を Support YES → NO に変更した Subset を作成 ( 無料 ) すれば解決すると思いますのでご対応をお願いします。もしすでに QDID:[ID] あるいは同等機能のデザイン登録の [LL] から AoA/AoD 機能および Isochronous 機能を Support NO とした Subset のご準備があればその DN をお知らせください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階内線 220

FAX [ID]

From:
米澤智

Sent: Friday, October 18, 2024 1:17 PM

To: Masaya Iida

Subject: Re: 【問合せ】 Bluetooth
認証に必要な資料と試験についてアリオン株式会社飯田様お世話になっております。

GO 株式会社の米澤です。

ご返信ありがとうございます。

支払い条件については、承知しました。

また、見積についても承知しました。

以上、よろしくお願いします。

2024 年 10 月 18 日 ( 金 ) 13:15 Masaya Iida :

GO 株式会社米澤様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。

支払い条件についてご認識の通りです。

ただし、 7 月に SIG の登録システムに変更がありましたため、

見積り内容、金額が変わる可能性がございます。

社内確認して別途見積書を提出いたします。

当方都合により月曜日以降となりますがお待ちくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階内線 220

FAX [ID]

From:
米澤智

Sent: Thursday, October 17, 2024 11:17 PM

To: Masaya Iida

Subject: Re: 【問合せ】 Bluetooth
認証に必要な資料と試験についてアリオン株式会社飯田様お世話になっております。

GO 株式会社の米澤です。

ご返信ができておらず、大変申し訳ありません。

改めての確認ですが、

支払い条件は月末締め翌月末支払いという理解で正しいでしょうか？

（見積書に記載がありましたが、念のため）

また、社内処理を進められる状況になったため、見積書を再送いただけないでしょうか？

お手数をおかけしますが、ご確認をよろしくお願いします。

2024 年 9 月 26 日 ( 木 ) 14:27 Masaya Iida :

GO
株式会社米澤様いつもお世話になっております。

アリオンの飯田です。

先日、 Bluetooth SIG 認証についての見積りをいたしましたが、

その後ご検討状況はいかがでしょうか。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階内線 220

FAX [ID]

From:
米澤智

Sent: Friday, June 21, 2024 7:58 PM

To: Masaya Iida

Subject: Re: 【問合せ】 Bluetooth
認証に必要な資料と試験についてアリオン株式会社飯田様お世話になります。

GO 株式会社の米澤です。

見積の送付ありがとうございます。

社内で協議させていただきます。

以上、よろしくお願いします。

2024 年 6 月 21 日 ( 金 ) 18:13 Masaya Iida :

GO 株式会社米澤様いつもお世話になっております。

アリオン営業担当の飯田です。

よろしくお願いいたします。

添付にて見積書を提出いたします。

ご検討のほどよろしくお願いいたします。

ご不明な点がございましたらご連絡のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階内線 220

FAX [ID]

From: Itsuo Sakai

Sent: Thursday, June 20, 2024 11:59 AM

To: 米澤智

Subject: Re: 【問合せ】 Bluetooth
認証に必要な資料と試験について

GO 株式会社米澤様アリオンの酒井です。いつもお世話になっております。

見積依頼書ご送付ありがとうございます。記載内容および念のため SIG 登録サイトを参照して試験不要であることが確認できました。

見積金額は下記の通りです。

・ Declaration 登録代行費 ￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

・ドル送金代行手数料 ￥ 100,000

・ Declaration Fee($11,040) 正式見積書発行前月末日 TTS レート換算円貨

7 月 31 日登録完了ご希望ですと 6 月末までにご発注いただきますと、当社内の Declaration
Fee 支払手続を進めて 7 月下旬に御社に Declaration
ID が発番されて代行登録が完了できるという日程感となります。

まずは上記内容の正式見積書 (pdf 版 ) を正式見積書を営業の飯田より送付させていただきます。

以上よろしくお願いいたします。

差出人 :
米澤智

送信日時 :
2024 年 6 月 20 日
11:34

宛先 : Itsuo
Sakai

件名 : Re:
【問合せ】 Bluetooth
認証に必要な資料と試験についてアリオン株式会社酒井様お世話になります。

GO 株式会社の米澤です。

ご返信とご説明ありがとうございます。

見積依頼書に記入しましたので、ご確認下さい。

以下の URL からダウンロードしてください :

< [URL] >

ダウンロードパスワード : QmYM&h3muRA4

URL の有効期限 : 2024 年 6 月 27 日
11:32 (UTC+09:00)

＞＞もしモジュール内蔵アンテナを使って製品に実装する場合には RF PHY 試験は免除されます。

内蔵アンテナ利用予定のため、 RF PHY 試験は免除と理解しました。

＞＞ LL, L2CAP, GAP, GATT, ATT, SM のプロトコル階層は Silicon Laboratories の Component(Tested) に

＞＞を参照した製品登録を行うことによって、試験免除されます。

こちらについても試験時に参照した SDK をそのまま使用予定のため、試験免除で理解しました。

＞＞残るプロファイル階層ですが、 Bluetooth SIG 制定プロファイルを実装する場合には、プロファイル

＞＞試験を実施してテストレポートを製品登録のエビデンスとしてアップロードする必要がありますが、

＞＞独自プロファイルを実装あるいはプロトコル階層のみ ( プロファイルレス ) の製品の場合には不要です一般的な GATT と独自プロファイルのみのため、追加試験は不要と理解しました。

お手数をおかけしますが、ご確認をよろしくお願いします。

2024 年 6 月 19 日 ( 水 ) 22:24 Itsuo Sakai :

GO 株式会社米澤様

Bluetooth ロゴ認証を担当しております酒井と申します。お問い合わせいただきありがとうございます。
現在、 Silicon Lab から販売されている [ID] シリーズという BLE
モジュールを使用した製品を開発しようとしています。
Bluetooth
の EPL 登録に必要な資料と貴社で実施が必要な試験について確認させて下さい。

⇒ 2014 年に EPL 登録という呼称は廃止されたため、下記回答では製品登録と表現させていただきます。
１．該当の BLE モジュールを Bluetooth
SIG のサイトで検索すると
Product
Type が Component （Tested）となっているため、

別途 Soft Device や Application のソフトを含めた試験が必要という認識ですが、正しいでしょうか？

また、試験を行う際は貴社施設での試験が必須という理解で正しいですか？

⇒ 以下はご質問内の情報から Bluetooth SIG 登録および [ID] シリーズの Datasheet を参照して一般論でお答えします。念のため添付の見積依頼書に分かる範囲でご記入の上ご返送ください。具体的に必要な試験を特定して費用を算出いたします。

[ID] モジュールは datasheet によると内蔵アンテナまたは RF ピン経由で外部アンテナを接続できます。

もしモジュール内蔵アンテナを使って製品に実装する場合には RF PHY 試験は免除されます。

LL, L2CAP, GAP, GATT, ATT, SM のプロトコル階層は Silicon
Laboratories の Component(Tested) にを参照した製品登録を行うことによって、試験免除されます。

残るプロファイル階層ですが、 Bluetooth SIG 制定プロファイルを実装する場合には、プロファイル試験を実施してテストレポートを製品登録のエビデンスとしてアップロードする必要がありますが、

独自プロファイルを実装あるいはプロトコル階層のみ ( プロファイルレス ) の製品の場合には不要です。
２．必要な資料は下記かと認識していますが、
過不足あるでしょうか？
また、下記資料は製品全体ではなく、
Bluetooth
モジュール部分に関する部分のみという理解で正しいでしょうか？
・ Bluetooth モジュール回路図・ Bluetooth モジュール PCB レイアウト・ Bluetooth モジュールの部品配置図・ Bluetooth モジュールの部品リスト・機能ブロック図・使用 IC のデータシート・ RF テストレポート

⇒ Bluetooth ロゴ認証では無料のメンバー登録と製品全体を対象とした下記資料が必要です。

・製品の操作マニュアル・製品のブロック図・製品の外形図・アンテナ外形図・利得特性図以上よろしくお願いいたします。

差出人 :
米澤智

送信日時 :
2024 年 6 月 19 日
21:31

宛先 : AJ
Sales/PM Department (SPD)

件名 :
【問合せ】 Bluetooth
認証に必要な資料と試験についてアリオン株式会社窓口担当者様お世話になります。

GO 株式会社の米澤と申します。

現在、 Silicon Lab から販売されている [ID] シリーズという BLE
モジュールを使用した製品を開発しようとしています。

Bluetooth の EPL 登録に必要な資料と貴社で実施が必要な試験について確認させて下さい。

１．該当の BLE モジュールを Bluetooth SIG のサイトで検索すると

Product Type が Component （Tested）となっているため、

別途 Soft Device や Application のソフトを含めた試験が必要という認識ですが、正しいでしょうか？

また、試験を行う際は貴社施設での試験が必須という理解で正しいですか？

２．必要な資料は下記かと認識していますが、

過不足あるでしょうか？

また、下記資料は製品全体ではなく、

Bluetooth モジュール部分に関する部分のみという理解で正しいでしょうか？

・ Bluetooth モジュール回路図・ Bluetooth モジュール PCB レイアウト・ Bluetooth モジュールの部品配置図・ Bluetooth モジュールの部品リスト・機能ブロック図・使用 IC のデータシート・ RF テストレポートお手数をおかけしますが、ご返信をよろしくお願いします。

--

GO 株式会社

IoT 本部 IoT 開発部ハードウェア開発グループ米澤智（Satoshi Yonezawa）

〒 [ID]

東京都港区麻布台 1 丁目 3-1 麻布台ヒルズ森 JP タワー 23F

FAX： [ID]
