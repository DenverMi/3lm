# thread_0132: [内部連絡] Re: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（リモコン）

- Message count: 1
- Source JSON: `thread_0132.json`

---

## 1. 2025-09-12 06:26

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように返信してください。

酒井ーーーー遅くなりましたが、リモコンの見積もり依頼書を添付します。
御確認の上、御見積をお願いします。

⇒見積依頼書ご送付ありがとうございます。この内容で製品登録しますと

Core仕様バージョンは参照先のより低いD049426のコア仕様v5.2となります。見積依頼書記載のv5.4ではありませんのでご了承ください。

見積は以下の通りです。

・RF PHY試験(1M, 2M) ￥700,000

・プロファイル試験(BAS,DIS, HIDS, HOGP) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

ーーーー差出人:

送信日時: 2025年9月12日 14:46

宛先: Masaya Iida ;

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（リモコン）

※メールを分かりやすくするため、件名に（リモコン）を付け加え再送しましたアリオン飯田様、

ソニー佐藤(善)です。

お世話になっております。

Bluetoothリモコンを担当しております。
リモコンの見積もり依頼書は別途担当から送付させて頂きます、依頼書作成中につきもう少々お時間ください。

遅くなりましたが、リモコンの見積もり依頼書を添付します。

御確認の上、御見積をお願いします。

なお御見積を頂いた後に、弊社内でリモコンのBluetooth SIG認証試験とEPL作業を御社に依頼するかを判断させて頂きます。

御社に依頼する場合の費用処理ですが、従来と異なりTVとリモコンは分けて、別々に費用処理をお願いすることとなりますが問題ありませんでしょうか。

以上、御確認の程よろしくお願いいたします。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらにQPRDv4からIOPT試験が追加されて、2025年11月10発効で以下の試験が発生します。

この試験は日本ラボで実施予定です。

IOPT/SR/COD/[ID] Class-of-Device

IOPT/A2DP/SRC/SDPR/[ID] SDP Record ? Source role

IOPT/A2DP/SRC/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is A2DP Source

IOPT/AVRCP/TG/SDPR/[ID] SDP Record ? Target role

IOPT/DID/SR/SDPR/[ID] SDP Record ? Device ID

IOPT/HFP/AG/SDPR/[ID] SDP Record ? Audio Gateway role

IOPT/HFP/AG/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is HFP AG

IOPT/HFP/HF/SDPR/[ID] SDP Record ? Hands-Free role

IOPT/HFP/HF/CGSIT/SFC/[ID] SDP Future Compatibility - IUT is HFP HF

IOPT/HID11/HOS/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is HID11 Host

IOPT/HSP/AG/SDPR/[ID] SDP Record ? HSP AG role

IOPT/HSP/AG/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is HSP AG role

IOPT/HSP/HS/SDPR/[ID] SDP Record ? HSP HS role

IOPT/HSP/HS/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is HSP HS role

IOPT/MAP/MCE/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is MAP MCE

IOPT/MAP/MSE/SDPR/[ID] SDP Record ? MSE role

IOPT/OPP/CL/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is OPP Push Client

IOPT/OPP/SR/SDPR/[ID] SDP Record ? Object Push

IOPT/PAN/NAP/SDPR/[ID] SDP Record ? NAP role

IOPT/PAN/PANU/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is PANU

IOPT/PBAP/PCE/SDPR/[ID] SDP Record ? PCE role

IOPT/PBAP/PCE/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is PBAP PCE

IOPT/PBAP/PSE/SDPR/[ID] SDP Record ? PSE role

IOPT/SPP/DEVA/CGSIT/SFC/[ID] SDP Future Compatibility ? IUT is SPP DevA

IOPT/SPP/DEVB/SDPR/[ID] SDP Record ? Serial Port

公開日が180日先まで指定可能になったこともあり、サーバーへの登録を11月9日までに行えば、RF/RF PHYおよびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(IOPT) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 > なお本件、3年前に御社に依頼したD062233の、OSバージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールやRF仕様の変更はないため、D062233の際作成したRF/RFPHYのテストレポートはソニー宮川様いつもお世話になっております。

アリオンの飯田です。

見積依頼書をご送付いただきありがとうございます。
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。

無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートは流用できると考えておりますが、こちら認識正しいかもご確認頂けると幸いです。
念のため、テストレポートも添付させて頂きます。

⇒ はい、無線モジュールや RF 仕様の変更がなければ、 [ID] の際に作成した RF/RFPHY のテストレポートは流用可能です。

念のため [ID] 登録と見積依頼書記載の Controller
Subsystem:[ID] の RF/RF PHY を比較した結果、 LL 9/15 (Power Class 1) と RF
1/1 (Power Clas 1) が [ID] は NO、 [ID] は YES

という違いがありました。 [ID] を Include した登録で LL の ICS 変更による対応は可能ですが、

2024 年 7 月 1 日以降の新登録制度では LL の試験要求が Test
Plan として出力されて 300 項目程度の試験レポートのアップロードが必要となりますので試験費用と所要期間が現実的ではありません。さらに [ID] 登録自体に階層間不整合が存在し、仮 Project で [ID] と組み合わせた登録過程で ICS 修正で階層間不整合を取り除くと新たな階層の試験要求が発生します。

そこで提案ですが、 [ID] には 4 種の Subset が準備されていて、そのうちの [ID] が既存の

[ID] と RF/RF
PHY が同じ Class 2 で、 [ID] と組み合わせた登録で階層間不整合が発生しません。このため [ID] は [ID] に変更いて登録を進めたいと思いますのでご検討ください。

見積は以下の通りです。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )
リモコンの見積もり依頼書は別途担当から送付させて頂きます、依頼書作成中につきもう少々お時間ください。

⇒ ありがとうございます。承知しました。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Tuesday, September 9, 2025 5:43 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

時間があいてしまい申し訳ありません。

TV本体側の見積もり依頼書を送付しますのでご確認ください。

なお本件、3年前に御社に依頼したD062233の、OSバージョンアップによるリスティングとなります。

無線モジュールやRF仕様の変更はないため、D062233の際作成したRF/RFPHYのテストレポートは流用できると考えておりますが、こちら認識正しいかもご確認頂けると幸いです。

念のため、テストレポートも添付させて頂きます。

リモコンの見積もり依頼書は別途担当から送付させて頂きます、依頼書作成中につきもう少々お時間ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, August 20, 2025 1:58 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = =
= = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

Bluetooth SIG認証のご相談をいただきまして、

誠にありがとうございます。

添付が見積依頼書です。

お手数ですが記載の上、ご提出をお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, August 20, 2025 1:54 PM

To: Masaya Iida

Subject: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様しばらくぶりのメール、失礼致します。

ソニーの宮川です。

FY26モデルのBluetooth SIG認証試験について、業務委託の見積もりをお願いしたく。

テレビ本体とリモコン、それぞれで見積もりをお願いしたいと考えているのですが、Bluetoothについては見積もり作成用のフォーマットがあったと記憶しております。

お手数ですが、最新のフォーマットを送付頂けないでしょうか？

以上、ご確認よろしくお願い致します。
