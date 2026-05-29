# thread_0051: [内部連絡] Re: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験

- Message count: 2
- Source JSON: `thread_0051.json`

---

## 1. 2025-09-09 22:50

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように回答してください。

酒井ーーーー見積依頼書をご送付いただきありがとうございます。
なお本件、3年前に御社に依頼したD062233の、OSバージョンアップによるリスティングとなります。
無線モジュールやRF仕様の変更はないため、D062233の際作成したRF/RFPHYのテストレポートは流用できると考えておりますが、こちら認識正しいかもご確認頂けると幸いです。
念のため、テストレポートも添付させて頂きます。

⇒はい、無線モジュールやRF仕様の変更がなければ、D062233の際に作成したRF/RFPHYのテストレポートは流用可能です。

念のためD062233登録と見積依頼書記載のController Subsystem:Q325703のRF/RF PHYを比較した結果、LL 9/15 (Power Class 1)とRF 1/1 (Power Clas 1)がD06223はNO、Q325703はYES

という違いがありました。Q325703をIncudeした登録でLLのICS変更による対応は可能ですが、

2024年7月1日以降の新登録制度ではLLの試験要求がTest Planとして出力されて300項目程度の試験レポートのアップロードが必要となりますので試験費用と所要期間が現実的ではありません。さらにQ325703登録自体に階層間不整合が存在し、仮ProjectでQ346069と組み合わせた登録過程でICS修正で階層間不整合を取り除くと新たな階層の試験要求が発生します。

そこで提案ですが、Q325703には4種のSubsetが準備されていて、そのうちのQ333791が既存の

D06223とRF/RF PHYが同じClass 2で、Q346069と組み合わせた登録で階層間不整合が発生しません。このためQ325703はQ333791に変更いて登録を進めたいと思いますのでご検討ください。

見積は以下の通りです。

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)
リモコンの見積もり依頼書は別途担当から送付させて頂きます、依頼書作成中につきもう少々お時間ください。

⇒ありがとうございます。承知しました。

ーーーー差出人:

送信日時: 2025年9月9日 17:43

宛先: Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

時間があいてしまい申し訳ありません。

TV 本体側の見積もり依頼書を送付しますのでご確認ください。

なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。

無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートは流用できると考えておりますが、こちら認識正しいかもご確認頂けると幸いです。

念のため、テストレポートも添付させて頂きます。

リモコンの見積もり依頼書は別途担当から送付させて頂きます、依頼書作成中につきもう少々お時間ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, August 20, 2025 1:58 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG 認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = =
= = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID]
東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

Bluetooth SIG 認証のご相談をいただきまして、

誠にありがとうございます。

添付が見積依頼書です。

お手数ですが記載の上、ご提出をお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, August 20, 2025 1:54 PM

To: Masaya Iida

Subject: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様しばらくぶりのメール、失礼致します。

ソニーの宮川です。

FY26 モデルの Bluetooth SIG 認証試験について、業務委託の見積もりをお願いしたく。

テレビ本体とリモコン、それぞれで見積もりをお願いしたいと考えているのですが、 Bluetooth については見積もり作成用のフォーマットがあったと記憶しております。

お手数ですが、最新のフォーマットを送付頂けないでしょうか？

以上、ご確認よろしくお願い致します。

---

## 2. 2025-09-12 01:08

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下の用に返信してください。

酒井ーーーーご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を使った方がいい件、理解しました。

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

公開日が180日先まで指定可能になったこともあり、サーバーへの登録を11月9日までに行えば、RF/RF PHYおよびプロファイル試験全てが免除されます。その場合の見積は以下の先メールの内容となります。

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(IOPT) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

ーーーー差出人:

送信日時: 2025年9月11日 20:32

宛先: Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID] > >
無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Tuesday, September 9, 2025 5:43 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

時間があいてしまい申し訳ありません。

TV 本体側の見積もり依頼書を送付しますのでご確認ください。

なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。

無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートは流用できると考えておりますが、こちら認識正しいかもご確認頂けると幸いです。

念のため、テストレポートも添付させて頂きます。

リモコンの見積もり依頼書は別途担当から送付させて頂きます、依頼書作成中につきもう少々お時間ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, August 20, 2025 1:58 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG 認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = =
= = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID]
東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

Bluetooth SIG 認証のご相談をいただきまして、

誠にありがとうございます。

添付が見積依頼書です。

お手数ですが記載の上、ご提出をお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, August 20, 2025 1:54 PM

To: Masaya Iida
