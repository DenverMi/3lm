# thread_0135: [内部連絡] Re: SIG申請について

- Message count: 4
- Source JSON: `thread_0135.json`

---

## 1. 2025-04-16 12:44

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

[ID]1モジュールはDatasheetにアンテナ内蔵またはアンテナコネクタ付と明記されていますのでRF/RF PHY試験は免除されます。また、QDID:[ID]([ID]-

[ID] Host)はQDID:[ID] ([ID]

/Controller Subsystem)と組み合せて参照する必要がありますが、QDID:199354はBLEオンリーモジュールのため、両者を組み合せた登録は見積依頼書記載のBR/EDR/BLEではなく、BLE

オンリー製品の登録となります。

見積金額は以下の通りです。

・代行登録サポート費(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

酒井差出人: Hideaki Haraguchi/原口秀明

送信日時: 2025年4月16日 20:25

宛先: Masaya Iida

件名: SIG申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

SIG 認証についてですが、申請したい案件がございます。

下記 Bluetooth モジュールを搭載した、弊社の基板にて SIG 認証の取得を予定しております。

Bluetooth モジュール

Espressif 製 [ID]

QDID： [ID]

基板サイズ： 79x50mm

弊社搭載基板分かる範囲にて見積依頼書を添付いたしましたので、申請内容のご確認をお願いできればと思います。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯 :[ID] FAX:[ID]

申請製品は、

---

## 2. 2025-04-22 09:26

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

質問へは以下のように回答してください。

酒井ーーーー私の理解としては、今回使用するBTモジュールがSIG上、Component登録になっていないからと理解しており、その旨をお伝えした所、モジュールメーカーからDeclaration IF D059143にて
Componentになっている旨の連絡がございました。

ただ、SIG上で見る限りComponent登録になっていないように見受けられますが、
私の理解で合っていますでしょうか？（今回のBTモジュールはComponentではない）

⇒はい、D059143はQDID:[ID] (Host Subsystem)ystem: QDID:[ID](Controller Subsystem)

の組み合わせ登録です。したがってこのモジュール実装製品は単一のComponentあるいはEnd

Product登録が参照できませんので、QDID:[ID] (Host Subsystem)とQDID:[ID]

(Controller Subsystem)の2件を参照する必要があります。

2024年7月1日以降の新登録制度ではController-Host間の階層間不整合チェックが強化されて複数のQDID/DNを参照する場合はICS修正などの検証作業が増えるため、当社のサポート費用ももSigle Design参照：￥150,000、Multi-Design参照：￥250,000と設定させて頂いております。

ーーーー差出人: Hideaki Haraguchi/原口秀明

送信日時: 2025年4月22日 17:58

宛先: Masaya Iida

件名: RE: SIG申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

１つご質問がございます。

依頼部署の方から前々回と比べて費用が高くなっている理由について聞かれております。

下記の金額となります。

・代行登録サポート費 (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

私の理解としては、今回使用する BT モジュールが SIG 上、 Component 登録になっていないからと理解しており、その旨をお伝えした所、モジュールメーカーから Declaration IF [ID] にて

Component になっている旨の連絡がございました。

ただ、 SIG 上で見る限り Component 登録になっていないように見受けられますが、

私の理解で合っていますでしょうか？（今回の BT モジュールは Component ではない）

以上、よろしくお願い致します。

寺岡精工原口

From: Hideaki Haraguchi/ 原口秀明

Sent: Thursday, April 17, 2025 10:41 AM

To: Masaya Iida

Subject: RE: SIG 申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

ご連絡頂きありがとうございます。

申請内容及び費用について承知いたしました。

Bluetooth SIG への送金（DID 取得）が完了しましたら改めてご連絡いたします。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯 :[ID] FAX:[ID]

From: Masaya Iida

Sent: Thursday, April 17, 2025 9:49 AM

To: Hideaki Haraguchi/ 原口秀明

Subject: RE: SIG 申請について寺岡精工原口様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。

内容を確認いたしました。

[ID] モジュールは Datasheet にアンテナ内蔵またはアンテナコネクタ付と明記されていますので Bluetooth SIG 認証に RF/RF PHY 試験は不要です。

また、 QDID:[ID]([ID] Host) は

QDID:[ID] ([ID]/Controller Subsystem) と組み合せて参照する必要がありますが、

QDID:[ID] は BLE オンリーモジュールのため、

両者を組み合せた登録は見積依頼書記載の BR/EDR/BLE ではなく、 BLE

オンリー製品の登録となります。

当社の登録サポート費用の見積りを以下にご案内いたします。

見積金額は以下の通りです。

・代行登録サポート費 (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

合計 :
￥ 400,000 ( 税別 )

※ Bluetooth SIG 認証取得には本費用とは別途でお客様より

Bluetooth SIG への送金（DID 取得費用）が必要です。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From: Hideaki Haraguchi/ 原口秀明

Sent: Wednesday, April 16, 2025 8:25 PM

To: Masaya Iida

Subject: SIG 申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

SIG 認証についてですが、申請したい案件がございます。

下記 Bluetooth モジュールを搭載した、弊社の基板にて SIG 認証の取得を予定しております。

Bluetooth モジュール

Espressif 製 [ID]

QDID： [ID]

基板サイズ： 79x50mm

弊社搭載基板分かる範囲にて見積依頼書を添付いたしましたので、申請内容のご確認をお願いできればと思います。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯 :[ID] FAX:[ID]

申請製品は、

---

## 3. 2025-05-13 09:50

**From:** Itsuo Sakai
**To:** Masaya Iida
**Attachments:** ���������������������������.doc

飯田さんお疲れさまです。

本件は見積書未発行で未受注ですが、客先は登録のためにDIDを取得中です。

まだ連絡がないのですが客先のメールから4週間経過していますのでDID取得完了かと思います。

正式見積書発行と添付の代行登録内容確認書（下記内容でBluetoothロゴ認証代行登録を依頼します。 を冒頭等に追加）を送付してください。これが返送されたら業務発注とみなせます。

酒井差出人: Hideaki Haraguchi/原口秀明

送信日時: 2025年4月17日 10:41

宛先: Masaya Iida

件名: RE: SIG申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

ご連絡頂きありがとうございます。

申請内容及び費用について承知いたしました。

Bluetooth SIGへの送金（DID取得）が完了しましたら改めてご連絡いたします。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯:[ID] FAX:[ID]

From: Masaya Iida

Sent: Thursday, April 17, 2025 9:49 AM

To: Hideaki Haraguchi/ 原口秀明

Subject: RE: SIG 申請について寺岡精工原口様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。

内容を確認いたしました。

[ID]1モジュールはDatasheetにアンテナ内蔵またはアンテナコネクタ付と明記されていますのでBluetooth SIG認証にRF/RF PHY試験は不要です。

また、QDID:[ID]([ID] Host)は

QDID:[ID] ([ID]/Controller Subsystem)と組み合せて参照する必要がありますが、

QDID:199354はBLEオンリーモジュールのため、

両者を組み合せた登録は見積依頼書記載のBR/EDR/BLEではなく、BLE

オンリー製品の登録となります。

当社の登録サポート費用の見積りを以下にご案内いたします。

見積金額は以下の通りです。

・代行登録サポート費(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

合計: ￥400,000 (税別)

※Bluetooth SIG認証取得には本費用とは別途でお客様より

Bluetooth SIGへの送金（DID取得費用）が必要です。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Hideaki Haraguchi/ 原口秀明

Sent: Wednesday, April 16, 2025 8:25 PM

To: Masaya Iida

Subject: SIG 申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

SIG認証についてですが、申請したい案件がございます。

下記Bluetoothモジュールを搭載した、弊社の基板にてSIG認証の取得を予定しております。

Bluetoothモジュール

Espressif製ESP32-[ID]

QDID：[ID]

基板サイズ：79x50mm

弊社搭載基板分かる範囲にて見積依頼書を添付いたしましたので、申請内容のご確認をお願いできればと思います。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯:[ID] FAX:[ID]

申請製品は、

---

## 4. 2025-05-20 09:32

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?SGlkZWFraSBIYXJhZ3VjaGkvGyRCODY4fSEhPShMQBsoQg==?= , Masaya Iida
**Attachments:** Review_Page.png

寺岡精工原口様アリオンの酒井です。いつもお世話になっております。

代行登録内容確認書をご送付いただきありがとうございます。

登録s業を勧めて登録確定直前のReview Pageの画像イメージを取得しましたので念のため御社でもご確認ください。

内容をご確認いただきよろしければ確定操作のご指示をお願いします。

なお、今回の参照先の登録内容ではConsysytency CheckでのInvalidが解消できずにReviewページのSubmission Requirementのび第3項目に黄色警告マークがありますが、SIGが許容しているTCW

(テストケース免除)のES-25636対象となるSIG起因のものです。Submission後にSIG担当者が確認して承認するため、1-5営業日に原口様の登録メールに承認通知が届いた段階で正式登録となります。

また、コンプライアンスフォルダ作成のため、登録確定後の登録サーバーから取得する情報以外に必要な下記製品情報をご準備の上、ご提出願います。

(1) 操作説明書（Bluetooth部分）

(2) 製品のブロック図

(3) 製品の外形寸法図

(4) アンテナ資料(放射利得特性図を含むもの)

以上よろしくお願いいたします。

差出人: Hideaki Haraguchi/原口秀明

送信日時: 2025年5月19日 16:02

宛先: Masaya Iida

件名: RE: SIG申請についてアリオン飯田様いつもお世話になっております、　寺岡精工の原口です。

ご連絡が遅くなりましたが、代行登録内容確認書を添付いたしましたのでこの内容にて登録作業を進めて頂きます様お願い致します。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯 :[ID] FAX:[ID]

From: Masaya Iida

Sent: Wednesday, May 14, 2025 4:46 PM

To: Hideaki Haraguchi/ 原口秀明

Subject: RE: SIG 申請について寺岡精工原口様いつもお世話になっております。

アリオンの飯田です。

SIG への送金が完了されているとのこと承知いたしました。

先ほどの見積書に対してご注文をいただけますでしょうか。

また、添付は代行登録内容確認書です。

こちらを記載いただきましてご提出いただけましたら当社での登録代行を進めます。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From: Hideaki Haraguchi/ 原口秀明

Sent: Wednesday, May 14, 2025 3:53 PM

To: Masaya Iida

Subject: RE: SIG 申請についてアリオン飯田様いつもお世話になっております。

SIG への入金ですが、弊社の振込タイミングや GW などで遅くなってしまいましたが

5/12 振込で処理されており、先ほど SIG の HP で確認しましたが、下記の [ID] でよろしかったでしょうか？

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯 :[ID] FAX:[ID]

From: Masaya Iida

Sent: Wednesday, May 14, 2025 2:56 PM

To: Hideaki Haraguchi/ 原口秀明

Subject: RE: SIG 申請について寺岡精工原口様いつもお世話になっております。

アリオンの飯田です。

Bluetooth SIG への送金についてですが、

状況はいかがでしょうか。

当社見積書がまだ提出できておりませんでしたので、

添付にて提出いたします。

ご注文のご検討のほどよろしくお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From: Hideaki Haraguchi/ 原口秀明

Sent: Tuesday, April 22, 2025 6:41 PM

To: Masaya Iida

Subject: RE: SIG 申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

早急なご連絡ありがとうございます。

また、詳細にご回答頂きありがとうございました。

引き続きよろしくお願い致します。

寺岡精工原口

From: Masaya Iida

Sent: Tuesday, April 22, 2025 6:28 PM

To: Hideaki Haraguchi/ 原口秀明

Subject: RE: SIG 申請について寺岡精工原口様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。

以下回答いたします。
私の理解としては、今回使用する BT モジュールが SIG 上、 Component 登録になっていないからと理解しており、その旨をお伝えした所、モジュールメーカーから Declaration IF [ID] にて
Component になっている旨の連絡がございました。

ただ、 SIG 上で見る限り Component 登録になっていないように見受けられますが、
私の理解で合っていますでしょうか？（今回の BT モジュールは Component ではない）

⇒ はい、 [ID] は QDID:[ID]
(Host Subsystem)ystem: QDID:[ID](Controller Subsystem)

の組み合わせ登録です。したがってこのモジュール実装製品は単一の Component あるいは End

Product 登録が参照できませんので、 QDID:[ID]
(Host Subsystem) と QDID:[ID]

(Controller Subsystem) の 2 件を参照する必要があります。

2024 年 7 月 1 日以降の新登録制度では Controller-Host 間の階層間不整合チェックが強化されて複数の QDID/DN を参照する場合は ICS 修正などの検証作業が増えるため、当社のサポート費用もも Sigle Design 参照：￥ 150,000、 Multi-Design 参照：￥ 250,000 と設定させて頂いております。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From: Hideaki Haraguchi/ 原口秀明

Sent: Tuesday, April 22, 2025 5:59 PM

To: Masaya Iida

Subject: RE: SIG 申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

１つご質問がございます。

依頼部署の方から前々回と比べて費用が高くなっている理由について聞かれております。

下記の金額となります。

・代行登録サポート費 (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

私の理解としては、今回使用する BT モジュールが SIG 上、 Component 登録になっていないからと理解しており、その旨をお伝えした所、モジュールメーカーから Declaration IF [ID] にて

Component になっている旨の連絡がございました。

ただ、 SIG 上で見る限り Component 登録になっていないように見受けられますが、

私の理解で合っていますでしょうか？（今回の BT モジュールは Component ではない）

以上、よろしくお願い致します。

寺岡精工原口

From: Hideaki Haraguchi/ 原口秀明

Sent: Thursday, April 17, 2025 10:41 AM

To: Masaya Iida

Subject: RE: SIG 申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

ご連絡頂きありがとうございます。

申請内容及び費用について承知いたしました。

Bluetooth SIG への送金（DID 取得）が完了しましたら改めてご連絡いたします。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯 :[ID] FAX:[ID]

From: Masaya Iida

Sent: Thursday, April 17, 2025 9:49 AM

To: Hideaki Haraguchi/ 原口秀明

Subject: RE: SIG 申請について寺岡精工原口様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。

内容を確認いたしました。

[ID] モジュールは Datasheet にアンテナ内蔵またはアンテナコネクタ付と明記されていますので Bluetooth SIG 認証に RF/RF PHY 試験は不要です。

また、 QDID:[ID]([ID] Host) は

QDID:[ID] ([ID]/Controller Subsystem) と組み合せて参照する必要がありますが、

QDID:[ID] は BLE オンリーモジュールのため、

両者を組み合せた登録は見積依頼書記載の BR/EDR/BLE ではなく、 BLE

オンリー製品の登録となります。

当社の登録サポート費用の見積りを以下にご案内いたします。

見積金額は以下の通りです。

・代行登録サポート費 (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

合計 :
￥ 400,000 ( 税別 )

※ Bluetooth SIG 認証取得には本費用とは別途でお客様より

Bluetooth SIG への送金（DID 取得費用）が必要です。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From: Hideaki Haraguchi/ 原口秀明

Sent: Wednesday, April 16, 2025 8:25 PM

To: Masaya Iida

Subject: SIG 申請についてアリオン飯田様いつもお世話になっております。　寺岡精工の原口です。

SIG 認証についてですが、申請したい案件がございます。

下記 Bluetooth モジュールを搭載した、弊社の基板にて SIG 認証の取得を予定しております。

Bluetooth モジュール

Espressif 製 [ID]

QDID： [ID]

基板サイズ： 79x50mm

弊社搭載基板分かる範囲にて見積依頼書を添付いたしましたので、申請内容のご確認をお願いできればと思います。

以上、よろしくお願い致します。

−−−−−−−−−−−−−−−−−−−−−

株式会社寺岡精工知的財産規格部原口秀明携帯 :[ID] FAX:[ID]

申請製品は、

* The information contained in this message is intended for the use of the individuals to whom it is addressed and may contain information
that is privileged and confidential. If you have received this email by mistake, please discard this email immediately. Do not disclose, forward or copy.

* このメッセージは宛名人に差し出されたもので、特定の機密情報が含まれている可能性があります。したがって、宛名人以外の方がこのメッセージを受信された場合、お手数ですが送信者までその旨メールにてご連絡いただきますとともに、直ちに本メールを破棄頂き公表・転用・複写等なきようお願い致します。

* The information contained in this message is intended for the use of the individuals to whom it is addressed and may contain information that is privileged and confidential. If you have received this email by mistake, please discard this email immediately.
Do not disclose, forward or copy.

* このメッセージは宛名人に差し出されたもので、特定の機密情報が含まれている可能性があります。したがって、宛名人以外の方がこのメッセージを受信された場合、お手数ですが送信者までその旨メールにてご連絡いただきますとともに、直ちに本メールを破棄頂き公表・転用・複写等なきようお願い致します。
