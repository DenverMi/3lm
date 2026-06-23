# thread_0036: [内部連絡] Re: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

- Message count: 20
- Source JSON: `thread_0036.json`

---

## 1. 2025-09-24 12:31

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように返信してください。

酒井ーーーーラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒ありがとうございます。諸々承知しました。

ーーーー差出人:

送信日時: 2025年9月24日 20:04

宛先: Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 11/9 までに登録完了で考えております。

（DN 購入の支払日は 10/31 予定です）

この日程感で、 11/9 までに登録完了可能そうでしょうか？

大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ >
今回ホストは [ID] を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 >
となっております。 > 3 年前の QDID [ID] のときは > A2DP 1. 3. 2 > AVRCP 1. 5 >
としていました。 ⇒ プロファイル (X2core) 部を QDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストは [ID] を参照で
A2DP 1.4
AVRCP 1.6.2
となっております。
3 年前の QDID [ID] のときは
A2DP 1.3.2
AVRCP 1.5
としていました。

⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP 1.4、

AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。

A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

11 月 9 までの登録では以下の見積です。

・プロファイル試験 (A2DP,AVRCP) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (A2DP,AVRCP,IOPT) ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストは [ID] を参照で

A2DP 1.4

AVRCP 1.6.2

となっております。

3 年前の QDID [ID] のときは

A2DP 1.3.2

AVRCP 1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を >
使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録で [ID]、 [ID] および FY23 の QDID: [ID] を Include して A2DP などのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらに QPRDv4 から IOPT 試験が追加されて、 2025 年 11 月 10 発効で以下の試験が発生します。

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

公開日が 180 日先まで指定可能になったこともあり、サーバーへの登録を 11 月 9 日までに行えば、 RF/RF PHY およびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (IOPT) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様しばらくぶりのメール、失礼致します。

ソニーの宮川です。

FY26 モデルの Bluetooth SIG 認証試験について、業務委託の見積もりをお願いしたく。

テレビ本体とリモコン、それぞれで見積もりをお願いしたいと考えているのですが、 Bluetooth については見積もり作成用のフォーマットがあったと記憶しております。

お手数ですが、最新のフォーマットを送付頂けないでしょうか？

以上、ご確認よろしくお願い致します。

---

## 2. 2025-10-07 23:47

**From:** Itsuo Sakai
**To:** "" , Masaya Iida

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。

Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムがExport projectファイル形式を配信しませんのでzipファイル化して添付してください。

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月7日 21:04

宛先: Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度 Qualification Workspece 操作について教えてください。

Specified the Design で、それぞれ参照する DN を選択後、 ICS Selection まで進むと、 CORE におきまして

Controller は Core v5.3 と v5.4

Host は Core v5.3 と v6.0

のふたつチェックが入っており、 Consistency Check が通らない状態になっています。

ここで CORE のチェックをさわると、色々な Layer が Unlock されてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
・ Option 2b でよかったでしょうか？ ⇒ はい、 Option 2b で結構です。 >
・ TCRL Package version は TCRK pkg100
でよかったでしょうか？ ⇒ はい、 pkg100 で結構です。 >
・ [ID]、 [ID]、 QDID: [ID] を include しましたが、下記設定画面で > Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて
[ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は
[ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1) プロファイル試験用の ICS を提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるための Qualification Workspece 操作をサポート頂きたく。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP
1.4、
AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。
A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

・ Option 2b でよかったでしょうか？

・ TCRL Package version は TCRK pkg100 でよかったでしょうか？

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で

Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを ICS 修正画面で修正する）

上記以外の Host 関連は [ID] を選ぶ

Controller 以下はすべて [ID] を選ぶ → RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 >
サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspace を作成して実装された各プロファイルの ICS を入力して Export ISC ファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの ( 無改造 ) で結構です。

(2) RF および RF PHY 試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3) 登録時の WorkSpace への入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

[ID] へのご記入・ご提出をお願いします。

(4)
添付の「Invoice 取得手順 _ 自社送金」を参照して SIG へ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = =
= = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUT の送付は以下までお願いいたします。 〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUT の送付は以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行して DUT の準備を進めたく思っております。

DUT の送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計 2 課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 >
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 > 11/9 までに登録完了で考えております。 >
（DN 購入の支払日は 10/31 予定です） >
この日程感で、 11/9 までに登録完了可能そうでしょうか？ ⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、 これまでの経験では Fail 項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、
11/9 までに登録完了で考えております。
（DN 購入の支払日は 10/31 予定です）
この日程感で、 11/9 までに登録完了可能そうでしょうか？

⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、

これまでの経験では Fail 項目の再試験、再々試験を加味しても約

3 週間で完了するのが一般的です。

この経験則からは 11/9 までに登録完了可能です。
大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 11/9 までに登録完了で考えております。

（DN 購入の支払日は 10/31 予定です）

この日程感で、 11/9 までに登録完了可能そうでしょうか？

大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ >
今回ホストは [ID] を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 >
となっております。 > 3 年前の QDID [ID] のときは > A2DP 1. 3. 2 > AVRCP 1. 5 >
としていました。 ⇒プロファイル (X2core) 部を QDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストは [ID] を参照で
A2DP 1.4
AVRCP 1.6.2
となっております。
3 年前の QDID [ID] のときは
A2DP 1.3.2
AVRCP 1.5
としていました。

⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP 1.4、

AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。

A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

11 月 9 までの登録では以下の見積です。

・プロファイル試験 (A2DP,AVRCP) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (A2DP,AVRCP,IOPT) ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストは [ID] を参照で

A2DP 1.4

AVRCP 1.6.2

となっております。

3 年前の QDID [ID] のときは

A2DP 1.3.2

AVRCP 1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を >
使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録で [ID]、 [ID] および FY23 の QDID: [ID] を Include して A2DP などのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらに QPRDv4 から IOPT 試験が追加されて、 2025 年 11 月 10 発効で以下の試験が発生します。

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

公開日が 180 日先まで指定可能になったこともあり、サーバーへの登録を 11 月 9 日までに行えば、 RF/RF PHY およびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (IOPT) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様しばらくぶりのメール、失礼致します。

ソニーの宮川です。

FY26 モデルの Bluetooth SIG 認証試験について、業務委託の見積もりをお願いしたく。

テレビ本体とリモコン、それぞれで見積もりをお願いしたいと考えているのですが、 Bluetooth については見積もり作成用のフォーマットがあったと記憶しております。

お手数ですが、最新のフォーマットを送付頂けないでしょうか？

以上、ご確認よろしくお願い致します。

---

## 3. 2025-10-08 05:32

**From:** Itsuo Sakai
**To:** "" , Masaya Iida

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selectionで、COREを変更する前の状態でExportしてあります。

⇒ありがとうございます。

この状態から(1)Layer SelectionでHCIとUHCIを削除してください。

次に(2)ICS SelectionでCore階層を選択し、12/1, 1/53, 2/53を削除してください。

これでAll ICS inconsistencies are resolved状態になりますので

A2DP, AVRCPのICSを変更してConcyctency CheckでNo Invalidを確認後にTest Plan and Declarationページに進んで[Download Test Plan]

アイコンをクリックしてTest Planを取得してください。

なお、QDID:199247からRF, RF PHY階層を踏襲してもTest Planには試験項目が出力されますのでQDID:199247登録時のRF/RF PHYレポートをご準備ください。

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月8日 10:11

宛先: Itsuo Sakai ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selection で、 CORE を変更する前の状態で Export してあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。 Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 7 日
21:04

宛先 :
Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度 Qualification Workspece 操作について教えてください。

Specified the Design で、それぞれ参照する DN を選択後、 ICS Selection まで進むと、 CORE におきまして

Controller は Core v5.3 と v5.4

Host は Core v5.3 と v6.0

のふたつチェックが入っており、 Consistency Check が通らない状態になっています。

ここで CORE のチェックをさわると、色々な Layer が Unlock されてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
・ Option 2b でよかったでしょうか？ ⇒はい、 Option 2b で結構です。 >
・ TCRL Package version は TCRK pkg100
でよかったでしょうか？ ⇒はい、 pkg100 で結構です。 >
・ [ID]、 [ID]、 QDID: [ID] を include しましたが、下記設定画面で > Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて
[ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は
[ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1) プロファイル試験用の ICS を提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるための Qualification Workspece 操作をサポート頂きたく。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP
1.4、
AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。
A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

・ Option 2b でよかったでしょうか？

・ TCRL Package version は TCRK pkg100 でよかったでしょうか？

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で

Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを ICS 修正画面で修正する）

上記以外の Host 関連は [ID] を選ぶ

Controller 以下はすべて [ID] を選ぶ → RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 >
サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspace を作成して実装された各プロファイルの ICS を入力して Export ISC ファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの ( 無改造 ) で結構です。

(2) RF および RF PHY 試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3) 登録時の WorkSpace への入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

[ID] へのご記入・ご提出をお願いします。

(4)
添付の「Invoice 取得手順 _ 自社送金」を参照して SIG へ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUT の送付は以下までお願いいたします。 〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUT の送付は以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行して DUT の準備を進めたく思っております。

DUT の送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計 2 課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 >
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 > 11/9 までに登録完了で考えております。 >
（DN 購入の支払日は 10/31 予定です） >
この日程感で、 11/9 までに登録完了可能そうでしょうか？ ⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、 これまでの経験では Fail 項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、
11/9 までに登録完了で考えております。
（DN 購入の支払日は 10/31 予定です）
この日程感で、 11/9 までに登録完了可能そうでしょうか？

⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、

これまでの経験では Fail 項目の再試験、再々試験を加味しても約

3 週間で完了するのが一般的です。

この経験則からは 11/9 までに登録完了可能です。
大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 11/9 までに登録完了で考えております。

（DN 購入の支払日は 10/31 予定です）

この日程感で、 11/9 までに登録完了可能そうでしょうか？

大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ >
今回ホストは [ID] を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 >
となっております。 > 3 年前の QDID [ID] のときは > A2DP 1. 3. 2 > AVRCP 1. 5 >
としていました。 ⇒プロファイル (X2core) 部を QDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストは [ID] を参照で
A2DP 1.4
AVRCP 1.6.2
となっております。
3 年前の QDID [ID] のときは
A2DP 1.3.2
AVRCP 1.5
としていました。

⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP 1.4、

AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。

A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

11 月 9 までの登録では以下の見積です。

・プロファイル試験 (A2DP,AVRCP) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (A2DP,AVRCP,IOPT) ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストは [ID] を参照で

A2DP 1.4

AVRCP 1.6.2

となっております。

3 年前の QDID [ID] のときは

A2DP 1.3.2

AVRCP 1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を >
使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録で [ID]、 [ID] および FY23 の QDID: [ID] を Include して A2DP などのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらに QPRDv4 から IOPT 試験が追加されて、 2025 年 11 月 10 発効で以下の試験が発生します。

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

公開日が 180 日先まで指定可能になったこともあり、サーバーへの登録を 11 月 9 日までに行えば、 RF/RF PHY およびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (IOPT) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG 認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = =
= = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
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

## 4. 2025-10-08 09:22

**From:** Itsuo Sakai
**To:** "" , Masaya Iida

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。
TVの開発キットを送付しますが、映像出力がHDMIとなっております。
HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月8日 18:18

宛先: Itsuo Sakai ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。

TV の開発キットを送付しますが、映像出力が HDMI となっております。

HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
添付ご確認ください。 > ICS Selection で、 CORE を変更する前の状態で Export してあります。 ⇒ ありがとうございます。 この状態から (1)Layer Selection で HCI と UHCI を削除してください。
次に (2)ICS Selection で Core 階層を選択し、 12/1, 1/53, 2/53 を削除してください。 これで All ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 8 日
10:11

宛先 :
Itsuo Sakai ; Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selection で、 CORE を変更する前の状態で Export してあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。 Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 7 日
21:04

宛先 :
Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度 Qualification Workspece 操作について教えてください。

Specified the Design で、それぞれ参照する DN を選択後、 ICS Selection まで進むと、 CORE におきまして

Controller は Core v5.3 と v5.4

Host は Core v5.3 と v6.0

のふたつチェックが入っており、 Consistency Check が通らない状態になっています。

ここで CORE のチェックをさわると、色々な Layer が Unlock されてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
・ Option 2b でよかったでしょうか？ ⇒はい、 Option 2b で結構です。 >
・ TCRL Package version は TCRK pkg100
でよかったでしょうか？ ⇒はい、 pkg100 で結構です。 >
・ [ID]、 [ID]、 QDID: [ID] を include しましたが、下記設定画面で > Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて
[ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は
[ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1) プロファイル試験用の ICS を提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるための Qualification Workspece 操作をサポート頂きたく。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP
1.4、
AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。
A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

・ Option 2b でよかったでしょうか？

・ TCRL Package version は TCRK pkg100 でよかったでしょうか？

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で

Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを ICS 修正画面で修正する）

上記以外の Host 関連は [ID] を選ぶ

Controller 以下はすべて [ID] を選ぶ → RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 >
サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspace を作成して実装された各プロファイルの ICS を入力して Export ISC ファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの ( 無改造 ) で結構です。

(2) RF および RF PHY 試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3) 登録時の WorkSpace への入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

[ID] へのご記入・ご提出をお願いします。

(4)
添付の「Invoice 取得手順 _ 自社送金」を参照して SIG へ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUT の送付は以下までお願いいたします。 〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUT の送付は以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行して DUT の準備を進めたく思っております。

DUT の送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計 2 課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 >
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 > 11/9 までに登録完了で考えております。 >
（DN 購入の支払日は 10/31 予定です） >
この日程感で、 11/9 までに登録完了可能そうでしょうか？ ⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、 これまでの経験では Fail 項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、
11/9 までに登録完了で考えております。
（DN 購入の支払日は 10/31 予定です）
この日程感で、 11/9 までに登録完了可能そうでしょうか？

⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、

これまでの経験では Fail 項目の再試験、再々試験を加味しても約

3 週間で完了するのが一般的です。

この経験則からは 11/9 までに登録完了可能です。
大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 11/9 までに登録完了で考えております。

（DN 購入の支払日は 10/31 予定です）

この日程感で、 11/9 までに登録完了可能そうでしょうか？

大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ >
今回ホストは [ID] を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 >
となっております。 > 3 年前の QDID [ID] のときは > A2DP 1. 3. 2 > AVRCP 1. 5 >
としていました。 ⇒プロファイル (X2core) 部を QDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストは [ID] を参照で
A2DP 1.4
AVRCP 1.6.2
となっております。
3 年前の QDID [ID] のときは
A2DP 1.3.2
AVRCP 1.5
としていました。

⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP 1.4、

AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。

A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

11 月 9 までの登録では以下の見積です。

・プロファイル試験 (A2DP,AVRCP) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (A2DP,AVRCP,IOPT) ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストは [ID] を参照で

A2DP 1.4

AVRCP 1.6.2

となっております。

3 年前の QDID [ID] のときは

A2DP 1.3.2

AVRCP 1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を >
使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録で [ID]、 [ID] および FY23 の QDID: [ID] を Include して A2DP などのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらに QPRDv4 から IOPT 試験が追加されて、 2025 年 11 月 10 発効で以下の試験が発生します。

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

公開日が 180 日先まで指定可能になったこともあり、サーバーへの登録を 11 月 9 日までに行えば、 RF/RF PHY およびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (IOPT) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG 認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = =
= = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
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

## 5. 2025-10-09 10:29

**From:** Itsuo Sakai
**To:** "" , Masaya Iida

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、ICSとテストプラン作成しました。
3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge（adb） | Android Studio | Android Developers
Android SDK Platform-Toolsをインストール頂く形になります。

⇒Bluetoothラボ備え付けのPCがありますのでダウンロードURLなどをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験でADBインストールPCが必要でしょうか。(今回はRF/RF PHY試験は対象外です。)

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月9日 19:12

宛先: Itsuo Sakai ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、 ICS とテストプラン作成しました。

3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？

Android Debug Bridge （adb）
| Android Studio | Android Developers

Android SDK Platform-Tools をインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。 > TV の開発キットを送付しますが、映像出力が HDMI となっております。 > HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒ はい、当方で準備いたします。
以上よろしくお願いいたします。 差出人 : Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 8 日
18:18

宛先 :
Itsuo Sakai ; Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。

TV の開発キットを送付しますが、映像出力が HDMI となっております。

HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
添付ご確認ください。 > ICS Selection で、 CORE を変更する前の状態で Export してあります。 ⇒ありがとうございます。 この状態から (1)Layer Selection で HCI と UHCI を削除してください。
次に (2)ICS Selection で Core 階層を選択し、 12/1, 1/53, 2/53 を削除してください。 これで All ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 8 日
10:11

宛先 :
Itsuo Sakai ; Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selection で、 CORE を変更する前の状態で Export してあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。 Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 7 日
21:04

宛先 :
Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度 Qualification Workspece 操作について教えてください。

Specified the Design で、それぞれ参照する DN を選択後、 ICS Selection まで進むと、 CORE におきまして

Controller は Core v5.3 と v5.4

Host は Core v5.3 と v6.0

のふたつチェックが入っており、 Consistency Check が通らない状態になっています。

ここで CORE のチェックをさわると、色々な Layer が Unlock されてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
・ Option 2b でよかったでしょうか？ ⇒はい、 Option 2b で結構です。 >
・ TCRL Package version は TCRK pkg100
でよかったでしょうか？ ⇒はい、 pkg100 で結構です。 >
・ [ID]、 [ID]、 QDID: [ID] を include しましたが、下記設定画面で > Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて
[ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は
[ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1) プロファイル試験用の ICS を提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるための Qualification Workspece 操作をサポート頂きたく。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP
1.4、
AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。
A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

・ Option 2b でよかったでしょうか？

・ TCRL Package version は TCRK pkg100 でよかったでしょうか？

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で

Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを ICS 修正画面で修正する）

上記以外の Host 関連は [ID] を選ぶ

Controller 以下はすべて [ID] を選ぶ → RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 >
サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspace を作成して実装された各プロファイルの ICS を入力して Export ISC ファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの ( 無改造 ) で結構です。

(2) RF および RF PHY 試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3) 登録時の WorkSpace への入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

[ID] へのご記入・ご提出をお願いします。

(4)
添付の「Invoice 取得手順 _ 自社送金」を参照して SIG へ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUT の送付は以下までお願いいたします。 〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUT の送付は以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行して DUT の準備を進めたく思っております。

DUT の送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。
= = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID]
東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計 2 課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 >
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 > 11/9 までに登録完了で考えております。 >
（DN 購入の支払日は 10/31 予定です） >
この日程感で、 11/9 までに登録完了可能そうでしょうか？ ⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、 これまでの経験では Fail 項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、
11/9 までに登録完了で考えております。
（DN 購入の支払日は 10/31 予定です）
この日程感で、 11/9 までに登録完了可能そうでしょうか？

⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、

これまでの経験では Fail 項目の再試験、再々試験を加味しても約

3 週間で完了するのが一般的です。

この経験則からは 11/9 までに登録完了可能です。
大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 11/9 までに登録完了で考えております。

（DN 購入の支払日は 10/31 予定です）

この日程感で、 11/9 までに登録完了可能そうでしょうか？

大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ >
今回ホストは [ID] を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 >
となっております。 > 3 年前の QDID [ID] のときは > A2DP 1. 3. 2 > AVRCP 1. 5 >
としていました。 ⇒プロファイル (X2core) 部を QDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストは [ID] を参照で
A2DP 1.4
AVRCP 1.6.2
となっております。
3 年前の QDID [ID] のときは
A2DP 1.3.2
AVRCP 1.5
としていました。

⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP 1.4、

AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。

A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

11 月 9 までの登録では以下の見積です。

・プロファイル試験 (A2DP,AVRCP) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (A2DP,AVRCP,IOPT) ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストは [ID] を参照で

A2DP 1.4

AVRCP 1.6.2

となっております。

3 年前の QDID [ID] のときは

A2DP 1.3.2

AVRCP 1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を >
使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録で [ID]、 [ID] および FY23 の QDID: [ID] を Include して A2DP などのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらに QPRDv4 から IOPT 試験が追加されて、 2025 年 11 月 10 発効で以下の試験が発生します。

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

公開日が 180 日先まで指定可能になったこともあり、サーバーへの登録を 11 月 9 日までに行えば、 RF/RF PHY およびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (IOPT) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG 認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = =
= = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
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

## 6. 2025-10-10 03:55

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki
**Attachments:** Test Plan_ICS-FY26.zip

望月さんお疲れさまです。

ソニー宮川さん案件のProfile Test PlanおよびExport ICSファイルを添付します。QUESTONAIRSは望月さんから提出依頼してください。

登録希望は2026年1月です。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年10月10日 10:57

宛先: Itsuo Sakai

件名: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん望月です本件ですが、プロファイル試験のA2DPとAVRCPの実施かと存じますが、

ICS、テストプランの方は既にございましたでしょうか。

11/4-7のエンジニアのアサインが難しいのでFail発生時に備えてなるべく早く試験を開始できるようにしたいと思います。

ご確認どうぞよろしくお願い申し上げます。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。
以上よろしくお願いいたします。 差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。
次に(2)ICS SelectionでCore階層を選択し、12/1, 1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 >
・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で > Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 =
= = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel
[ID] 以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 >
3年前のQDID 199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

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

---

## 7. 2025-10-10 04:02

**From:** Itsuo Sakai
**To:** "" , Masaya Iida

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。
参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ADBインストールPCの使途が理解できました。設定変更であれば

PTS試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Toolsは下記サイトからダウンロードできます。
SDK Platform-Tools リリースノート | Android Studio | Android Developers
なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windowsでadb環境を構築する

⇒ADBのダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月10日 11:33

宛先: Itsuo Sakai ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。

参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Tools は下記サイトからダウンロードできます。

SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windows でadb 環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。 > 3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。 ⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。 > テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb）
| Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 9 日
19:12

宛先 :
Itsuo Sakai ; Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、 ICS とテストプラン作成しました。

3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge （adb） | Android Studio | Android Developers

Android SDK Platform-Tools をインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。 > TV の開発キットを送付しますが、映像出力が HDMI となっております。 > HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。 差出人 :
Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 8 日
18:18

宛先 :
Itsuo Sakai ; Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。

TV の開発キットを送付しますが、映像出力が HDMI となっております。

HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
添付ご確認ください。 > ICS Selection で、 CORE を変更する前の状態で Export してあります。 ⇒ありがとうございます。 この状態から (1)Layer Selection で HCI と UHCI を削除してください。
次に (2)ICS Selection で Core 階層を選択し、 12/1, 1/53, 2/53 を削除してください。 これで All ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 8 日
10:11

宛先 :
Itsuo Sakai ; Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selection で、 CORE を変更する前の状態で Export してあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。 Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 :
2025 年 10 月 7 日
21:04

宛先 :
Masaya Iida

件名 :
RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度 Qualification Workspece 操作について教えてください。

Specified the Design で、それぞれ参照する DN を選択後、 ICS Selection まで進むと、 CORE におきまして

Controller は Core v5.3 と v5.4

Host は Core v5.3 と v6.0

のふたつチェックが入っており、 Consistency Check が通らない状態になっています。

ここで CORE のチェックをさわると、色々な Layer が Unlock されてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
・ Option 2b でよかったでしょうか？ ⇒はい、 Option 2b で結構です。 >
・ TCRL Package version は TCRK pkg100
でよかったでしょうか？ ⇒はい、 pkg100 で結構です。 >
・ [ID]、 [ID]、 QDID: [ID] を include しましたが、下記設定画面で > Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて
[ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は
[ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1) プロファイル試験用の ICS を提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるための Qualification Workspece 操作をサポート頂きたく。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP
1.4、
AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。
A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

・ Option 2b でよかったでしょうか？

・ TCRL Package version は TCRK pkg100 でよかったでしょうか？

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で

Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを ICS 修正画面で修正する）

上記以外の Host 関連は [ID] を選ぶ

Controller 以下はすべて [ID] を選ぶ → RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 >
サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspace を作成して実装された各プロファイルの ICS を入力して Export ISC ファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの ( 無改造 ) で結構です。

(2) RF および RF PHY 試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3) 登録時の WorkSpace への入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

[ID] へのご記入・ご提出をお願いします。

(4)
添付の「Invoice 取得手順 _ 自社送金」を参照して SIG へ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = = =
= アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUT の送付は以下までお願いいたします。 〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUT の送付は以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行して DUT の準備を進めたく思っております。

DUT の送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計 2 課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 >
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 > 11/9 までに登録完了で考えております。 >
（DN 購入の支払日は 10/31 予定です） >
この日程感で、 11/9 までに登録完了可能そうでしょうか？ ⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、 これまでの経験では Fail 項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、
11/9 までに登録完了で考えております。
（DN 購入の支払日は 10/31 予定です）
この日程感で、 11/9 までに登録完了可能そうでしょうか？

⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、

これまでの経験では Fail 項目の再試験、再々試験を加味しても約

3 週間で完了するのが一般的です。

この経験則からは 11/9 までに登録完了可能です。
大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 11/9 までに登録完了で考えております。

（DN 購入の支払日は 10/31 予定です）

この日程感で、 11/9 までに登録完了可能そうでしょうか？

大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ >
今回ホストは [ID] を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 >
となっております。 > 3 年前の QDID [ID] のときは > A2DP 1. 3. 2 > AVRCP 1. 5 >
としていました。 ⇒プロファイル (X2core) 部を QDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストは [ID] を参照で
A2DP 1.4
AVRCP 1.6.2
となっております。
3 年前の QDID [ID] のときは
A2DP 1.3.2
AVRCP 1.5
としていました。

⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP 1.4、

AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。

A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

11 月 9 までの登録では以下の見積です。

・プロファイル試験 (A2DP,AVRCP) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (A2DP,AVRCP,IOPT) ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストは [ID] を参照で

A2DP 1.4

AVRCP 1.6.2

となっております。

3 年前の QDID [ID] のときは

A2DP 1.3.2

AVRCP 1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を >
使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録で [ID]、 [ID] および FY23 の QDID: [ID] を Include して A2DP などのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらに QPRDv4 から IOPT 試験が追加されて、 2025 年 11 月 10 発効で以下の試験が発生します。

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

公開日が 180 日先まで指定可能になったこともあり、サーバーへの登録を 11 月 9 日までに行えば、 RF/RF PHY およびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (IOPT) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG 認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = =
= = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
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

## 8. 2025-10-10 04:51

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki
**Attachments:** Revised_est Plan_ICS-FY26.zip

望月さんお疲れさまです。

先程送付したソニー宮川さん案件は当初の予定から「IOPT

が必須になる以前の2025/10/09までの登録」に変更されていましたのでTest Planを訂正して再送します。

なお、QUESTONAIRSは望月さんから提出依頼してください。

酒井差出人: Itsuo Sakai

送信日時: 2025年10月10日 12:55

宛先: Toshitaka Mochizuki

件名: Re: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

望月さんお疲れさまです。

ソニー宮川さん案件のProfile Test PlanおよびExport ICSファイルを添付します。QUESTONAIRSは望月さんから提出依頼してください。

登録希望は2026年1月です。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年10月10日 10:57

宛先: Itsuo Sakai

件名: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん望月です本件ですが、プロファイル試験のA2DPとAVRCPの実施かと存じますが、

ICS、テストプランの方は既にございましたでしょうか。

11/4-7のエンジニアのアサインが難しいのでFail発生時に備えてなるべく早く試験を開始できるようにしたいと思います。

ご確認どうぞよろしくお願い申し上げます。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。 差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1, 1/53, 2/53を削除してください。 これでAll
ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport projectファイル形式を配信しませんのでzipファイル化して添付してください。
以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で > Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。

・ Option 2b でよかったでしょうか？

⇒ はい、 Option 2b で結構です。

・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。

上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID] 以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com
<Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220 Mobile: [ID] FAX
[ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？ ⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID 199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。
⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 > なお本件、3年前に御社に依頼したD062233の、OSバージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID] > > 無線モジュールやRF仕様の変更はないため、D062233の際作成したRF/RFPHYのテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel
[ID] 内線220

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

---

## 9. 2025-10-15 07:59

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , Yu Hong

望月さんお疲れさまです。

以下のように返信してください。

酒井ーーーー
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。

ーーーー差出人: Toshitaka Mochizuki

送信日時: 2025年10月15日 16:34

宛先: Itsuo Sakai ; Yu Hong

件名: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん望月です

SONY BRAVIA様から質問ですご回答いただけますでしょうか。

どうぞよろしくお願いいたします。

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ; ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。
もしサイズが大きい物でしたらあらかじめお知らせください。 また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 >
なお、テスト環境でもう一点確認があります。 > テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。
以上よろしくお願いいたします。 差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。
次に(2)ICS SelectionでCore階層を選択し、12/1, 1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 >
・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で > Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 =
= = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel
[ID] 以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 >
3年前のQDID 199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

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

---

## 10. 2025-10-30 09:52

**From:** Itsuo Sakai
**To:** "" , "" , Toshitaka Mochizuki , Masaya Iida

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。
A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ご連絡ありがとうございます。

A2DP ICS 1/8:NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、11/9申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ご推察の通り11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。非Pass項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社でのPTS試験実施をお願いします。

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月30日 17:55

宛先: ; Toshitaka Mochizuki ; Itsuo Sakai ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ; Miyagawa, Yoichi (SEC) ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ; Miyagawa, Yoichi (SEC) ; Itsuo Sakai
; Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player
list does not contain a browsable player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ; ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l
A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。
もしサイズが大きい物でしたらあらかじめお知らせください。 また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 >
なお、テスト環境でもう一点確認があります。 > テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。
以上よろしくお願いいたします。 差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。
次に(2)ICS SelectionでCore階層を選択し、12/1, 1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 >
・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で > Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 =
= = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel
[ID] 以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 >
3年前のQDID 199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

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

---

## 11. 2025-10-30 10:12

**From:** Itsuo Sakai
**To:** "" , "" , Toshitaka Mochizuki , Masaya Iida

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
>11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。
エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、
そういうわけではない感じでしょうか？

⇒望月から、Bluetooth専任エンジニアが試験できない間は別規格の認証試験担当にアサインされたProfile試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

したがって全く試験できない訳ではありませんが、残件を分担させていただけると心強いです。

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月30日 18:56

宛先: Itsuo Sakai ; ; Toshitaka Mochizuki ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

一点確認をさせてください。
11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、そういうわけではない感じでしょうか？

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 6:52 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ; Toshitaka Mochizuki ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 本日望月が不在のため代わって返信させていただきます。 > A2DP/SRC/SUS/[ID] ですが、今のテレビソフトはSuspendを発行しない > ことが分かりました。 > A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付 >
にテストケース差し替えをお願いできますでしょうか？ ⇒ご連絡ありがとうございます。 A2DP ICS 1/8: NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player list does not
contain a browsable player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]：Suspend
the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。
また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 > なお、テスト環境でもう一点確認があります。 >
テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。
差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1,
1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport
projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で >
Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = =
= = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel
[ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID
199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ >
前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220

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

---

## 12. 2025-10-31 01:05

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki

望月さんお疲れさまです。

A2DP/SRC/SUS/[ID]Cは客先から取り下げられ、もう1件Passしない

A2DP/SRC/SUS/[ID]CはCtegory Dで試験必須ではありません。

したがってこれでA2DPは試験完了です。

AVRCPはおそらく「The media player list does not contain a

browsable player」でPassしない項目はDUTが送ってくるMedia

Player Listの問題と思われ、客先解析で約30項目が解決しそうです。残る4件もDUT側の応答内容が正しくないというログ内容ですので客先回答待ちです。

以上の状況ですので客先回答を待たないとSony様Profile試験は先に進めない状況ですのでALAPのRF/RF PHY/Profile案件を先に実施し、回答があればすぐSony様案件に戻してください。

酒井差出人: Itsuo Sakai

送信日時: 2025年10月30日 18:52

宛先: ; ; Toshitaka Mochizuki ; Masaya Iida

件名: Re: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。
A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ご連絡ありがとうございます。

A2DP ICS 1/8:NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、11/9申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ご推察の通り11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。非Pass項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社でのPTS試験実施をお願いします。

以上よろしくお願いいたします。

差出人:

送信日時: 2025年10月30日 17:55

宛先: ; Toshitaka Mochizuki ; Itsuo Sakai ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ; Miyagawa, Yoichi (SEC) ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ; Miyagawa, Yoichi (SEC) ; Itsuo Sakai
; Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player list does not contain a browsable player” と表示されています。 DUT本体上で media
player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ; ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1
東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming
channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1
東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC
B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。
こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC
B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1
東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM
望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。 また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。

参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 > なお、テスト環境でもう一点確認があります。 > テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。 差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1, 1/53, 2/53を削除してください。 これでAll
ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport projectファイル形式を配信しませんのでzipファイル化して添付してください。
以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で > Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。

・ Option 2b でよかったでしょうか？

⇒ はい、 Option 2b で結構です。

・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。

上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID] 以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com
<Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220 Mobile: [ID] FAX
[ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？ ⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID 199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。
⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 > なお本件、3年前に御社に依頼したD062233の、OSバージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID] > > 無線モジュールやRF仕様の変更はないため、D062233の際作成したRF/RFPHYのテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel
[ID] 内線220

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

---

## 13. 2025-10-31 01:34

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , AJ Bluetooth Group

喩さん、後夷さん、中山さんお疲れさまです。

Sony様案件のTest Plan記載のAVRCPの非Pass項目のコメントは「The media

player list does not contain a browsable player」ですが、PTSレポートのログINDCSV項目は「PreAmble, Failed to init stack. Controller doesn't

respond to command, please unplug and plug back the dongle.」（Dongle

のController Stackが正しく応答しないのでDongleを抜いて再度挿入せよ）

となっています。（Report_AVRCP_2025_10_27_17_39_24.xml）

おそらくTest PlanのコメントはそのようなUSB Dongleの問題がない段階でメモしたものと思いますが、今後のPTS試験でUSB Dongleの抜挿指示が出たらすぐそれを行って、その後に次の項目を実施してください。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年10月31日 10:14

宛先: AJ Bluetooth Group

件名: [内部連絡] Re: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

喩さん望月です。

本日ですが、来週のWSのご準備もあるかと思いますが、

以下の酒井さんのご指示もありますので、Alps AlpineのRF PHY試験の試験を優先して実施お願いできますでしょうか。

また、次のAlpsAlpineのサンプルの動作確認も可能でしたらお願いいたします。

どうぞよろしくお願い申し上げます。

From: Itsuo Sakai

Sent: Friday, October 31, 2025 10:06 AM

To: Toshitaka Mochizuki

Subject: [ 内部連絡 ] Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

望月さんお疲れさまです。

A2DP/SRC/SUS/[ID] は客先から取り下げられ、もう 1 件 Pass しない

A2DP/SRC/SUS/[ID] は Ctegory
D で試験必須ではありません。

したがってこれで A2DP は試験完了です。

AVRCP はおそらく「The
media player list does not contain a

browsable player」で Pass しない項目は DUT が送ってくる Media

Player List の問題と思われ、客先解析で約 30 項目が解決しそうです。残る 4 件も DUT 側の応答内容が正しくないというログ内容ですので客先回答待ちです。

以上の状況ですので客先回答を待たないと Sony 様 Profile 試験は先に進めない状況ですので ALAP の RF/RF
PHY/Profile 案件を先に実施し、回答があればすぐ Sony 様案件に戻してください。

酒井差出人 : Itsuo Sakai

送信日時 : 2025 年 10 月 30 日 18:52

宛先 : ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player list does not
contain a browsable player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]：Suspend
the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。
また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 > なお、テスト環境でもう一点確認があります。 >
テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。
差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1,
1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport
projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で >
Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = =
= = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel
[ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID
199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ >
前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220

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

---

## 14. 2025-11-04 06:50

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , AJ Bluetooth Group

望月さんお疲れさまです。

客先には以下のように返信してください。

酒井ーーーー
A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case Category
がDなので、不問ということで理解正しいでしょうか？
（A2DPはパスしたと考えてよいでしょうか？）

⇒そのご認識通りです。A2DPが認証登録に必要な試験項目を完了したことを明確にお知らせしてませんでした。申し訳ございません。
AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、
引き続き残った1件を進めています。

⇒ありがとうございます。AVRCPのPTSレポートを添付いただきましたが当方のメールサーバーがxml拡張子のファイルを配信しないため、お手数ですがzip

圧縮後添付して再送をお願いします。
すべてパスしましたら、Evidence logを提出します。

⇒ありがとうございます。お手数をお掛けしますがよろしくお願いいたします。

ーーーー差出人: Toshitaka Mochizuki

送信日時: 2025年11月4日 15:44

宛先: AJ Bluetooth Group

件名: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん中山さん

SONY様から以下の連絡がございました。

以下のご質問回答いただけますでしょうか。

添付もご確認ください。

どうぞよろしくお願いいたします。

望月

From:

Sent: Tuesday, November 4, 2025 3:36 PM

To: Toshitaka Mochizuki ; ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

すみません、一点確認させてください。

A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case CategoryがDなので、不問ということで理解正しいでしょうか？（A2DPはパスしたと考えてよいでしょうか？）

AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、引き続き残った1件を進めています。

すべてパスしましたら、Evidence logを提出します。

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Friday, October 31, 2025 7:29 PM

To: 'Toshitaka Mochizuki' ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

ファイルありがとうございました、ダウンロードできました。

チップベンダーと相談します、火曜日に進め方再度相談させてください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 7:22 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 大変お待たせいたしました。 ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。 以下のPasswordにてダウンロードください。 ----------------------------------------
[パスワード] nn<VVk~5 [パスワード有効期限] [ID] 19: 19 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

大変お待たせいたしました。

ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。

以下のPasswordにてダウンロードください。

[パスワード]

nn<VVk~5

[パスワード有効期限]

[ID] 19:19 まで

[送信ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 6:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

ファイルダウンロードできました、ありがとうございます。

本日終了時点でのリストの方もよろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 6:10 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 Failログなどをオフィス宅ふぁいる便で再送いたしましたので、 お送りしたリンクで以下のPasswordにてダウンロードください。 ---------------------------------------- [パスワード]
RWG. 7r{y [パスワード有効期限] [ID] 18: 07 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

Failログなどをオフィス宅ふぁいる便で再送いたしましたので、

お送りしたリンクで以下のPasswordにてダウンロードください。

[パスワード]

RWG.7r{y

[パスワード有効期限]

[ID] 18:07 まで

[送信ID]

ダウンロードできないようでしたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 5:14 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

申し訳ありません、添付ファイルが削除されてしまったようです。

下記拡張子のファイルが含まれると、削除されるとのこと。

&quot;386, &quot;3gr&quot;, &quot;add&quot;, &quot;ade&quot;, &quot;asp&quot;, &quot;bas&quot;, &quot;bat&quot;, &quot;chm&quot;, &quot;cmd&quot;, &quot;com&quot;, &quot;cpl&quot;, &quot;crt&quot;, &quot;dbx&quot;, &quot;dll&quot;, &quot;exe&quot;,

&quot;fon, &quot;hlp&quot;, &quot;hta&quot;, &quot;inf&quot;, &quot;ins&quot;, &quot;isp&quot;, &quot;js&quot;, &quot;jse&quot;, &quot;lnk&quot;, &quot;mdb&quot;, &quot;mde&quot;, &quot;msc&quot;, &quot;msi&quot;, &quot;msp&quot;, &quot;mst&quot;,

&quot;ocx, &quot;pcd&quot;, &quot;pif&quot;, &quot;reg&quot;, &quot;scr&quot;, &quot;sct&quot;, &quot;shs&quot;, &quot;shb&quot;, &quot;url&quot;, &quot;vb&quot;, &quot;vbe&quot;, &quot;vbs&quot;, &quot;vxd&quot;, &quot;wsc&quot;, &quot;wsf&quot;,

&quot;wsh,&quot;adp&quot;, &quot;ani&quot;, &quot;ht&quot;, &quot;job&quot;, &quot;mda&quot;, &quot;mdz&quot;, &quot;ws&quot;, &quot;ps1&quot;, &quot;ps1xml&quot;, &quot;ps2&quot;, &quot;ps2xml&quot;, &quot;psc1&quot;, &quot;psc2&quot;,

&quot;msh, &quot;msh1&quot;, &quot;msh2&quot;, &quot;mshxml&quot;, &quot;msh1xml&quot;, &quot;msh2xml&quot;, &quot;scf&quot;, &quot;class&quot;, &quot;jar&quot;, &quot;iqy&quot;, &quot;psm1&quot;, &quot;pssc&quot;

&quot;apk, &quot;app&quot;, &quot;appcontent-ms&quot;, &quot;appref-ms&quot;, &quot;appx&quot;, &quot;aspx&quot;, &quot;asx&quot;, &quot;cdxml&quot;, &quot;cer&quot;, &quot;cnt&quot;

&quot;csh, &quot;der&quot;, &quot;diagcab&quot;, &quot;fxp&quot;, &quot;gadget&quot;, &quot;grp&quot;, &quot;hpj&quot;, &quot;htc&quot;, &quot;its&quot;, &quot;jnlp&quot;, &quot;ksh&quot;, &quot;mad&quot;

&quot;maf, &quot;mag&quot;, &quot;mam&quot;, &quot;maq&quot;, &quot;mar&quot;, &quot;mas&quot;, &quot;mat&quot;, &quot;mau&quot;, &quot;mav&quot;, &quot;maw&quot;, &quot;mcf&quot;, &quot;mdt&quot;, &quot;mdw&quot;, &quot;mht&quot;

&quot;mhtml, &quot;msu&quot;, &quot;ops&quot;, &quot;pl&quot;, &quot;plg&quot;, &quot;prf&quot;, &quot;prg&quot;, &quot;printerexport&quot;, &quot;psd1&quot;, &quot;psdm1&quot;, &quot;pst&quot;, &quot;py&quot;, &quot;pyc&quot;

&quot;pyo, &quot;pyw&quot;, &quot;pyz&quot;, &quot;pyzw&quot;, &quot;settingcontent-ms&quot;, &quot;theme&quot;, &quot;tmp&quot;, &quot;udl&quot;, &quot;vbp&quot;, &quot;vhd&quot;, &quot;vhdx&quot;, &quot;vsmacros&quot;

&quot;vss, &quot;vst&quot;, &quot;vsw&quot;, &quot;webpnp&quot;, &quot;website&quot;, &quot;wsb&quot;, &quot;xbap&quot;, &quot;xll&quot;, &quot;xnk&quot;

ひとまず、本日の確認終わりましたら、エクセルでリスト頂けますでしょうか？

Evidence log取得が終わっていないテストケースについて色付けしてリスト頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 4:24 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、 Fail となっていた項目は依然として Pass にはなっていません。 すべての Fail 項目への再確認はまた完了していないですが、
「The media player list does not contain a browsable player」または 「Failed to retrieve

An email has been sent to you which contained one or more attachments, some of which are not permitted for security reasons. Please contact your local helpdesk for advice on how to securely share
files with external parties.

Attachment(s) deleted: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

Sender:

Date: [ID]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proofpointにより添付ファイルが削除されました。セキュリティ上の理由から許可されていない添付ファイルが1つ以上含まれている電子メールが送信されたためです。

削除された添付ファイル名: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

送信者:

日付: [ID]

外部の顧客と安全にファイルを共有する方法については、以下のURLをご参照ください。

< [URL] >

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、

Fail となっていた項目は依然として Pass にはなっていません。

すべての Fail 項目への再確認はまた完了していないですが、

「The media player list does not contain a browsable player」または

「Failed to retrieve Media Player List」

というエラーが発生したことにより、試験結果は [ID] または Fail となっております。

取り急ぎ、再試験した項目のテストログ、スクリーンショット、および写真を添付いたしますので、ご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 4:18 PM

To: ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

本日安井より情報を入れさせて頂きましたが、これで少し評価進みましたでしょうか？

Failなど残りましたら、チップベンダーにEvidence log取得の依頼をかけることも考えておりますので、本日終了時点で進捗状況お知らせ頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Friday, October 31, 2025 12:32 PM

To: Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、チップベンダー様からの情報によると、テストでは Google Play Music を使用することが大事なように思われます。

以下、そちらの情報です。

I have shared the User Manuals for these failed test items with you via MTK FEX.

It also includes the required Google Music and MP3 files.

Please follow the SOP for each test item in the User Manual to conduct the tests.

Because most of these test items require the use of Google Music.

If you encounter any difficulties installing Google Music, please let me know.

I will check it tomorrow night. (As you know, I am currently attending military reservist training...)

Additionally, regarding AVRCP/TG/MPS/[ID], we do not have experience testing this item.

However, based on the information provided by the lab, it also requires the use of Google Music.

You can try the following steps to see if you can pass this test item:

1.
Install the Google Play Music app

2.
Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

3.
Play then pause the music in Google Play Music

4.
Make sure PTS and IUT are paired

5.
Run PTS to start the test case AVRCP/TG/MPS/[ID]

6.
PTS will pop up a message (&quot;Received Play Command, press Yes&quot;)

7.
If Google Play Music starts playing music, click &quot;Yes&quot;; if it does not start playing, click &quot;No&quot;.

弊社でもこちらのやり方を調査しておりまして、以下の部分を補足させていただきます。

・ Google Play Music のインストール方法

PC とテレビを adb
接続していただき、以前お送りした GoogleMusic.apk が入っているフォルダからコマンドプロンプトで

adb root

adb install GoogleMusic.apk

adb reboot

と打っていただくとインストールできます。

・ Google Play Music の開き方設定 → アプリ → アプリをすべて表示 → システムアプリの表示 →Google
Play Musuic

から開いていただくと、開けますその際サーバーエラーのような画面が出ますが、 OK を何度か押していただくとプレイリストの画面まで進むことができると思います。

その後、リモコンで上ボタンを押すと、画像左上の 3 本の線がある部分にカーソルが表示されますので、その状態であれば Google
Play Music を操作することが可能になるように思われます。

・ Goole Play Music に mp3 ファイルを入れる方法

Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

との記載がありますが、こちらでうまくいかない場合は

mp3 ファイルを USB メモリに入れていただき、テレビのもう一つの USB ポート (addb 接続している USB ポートの隣 ) に接続していただくと Google
Play Music 上でもプレイリストが表示されるように思われます。

弊社の方でも、こちらのやり方引き続き調査しますので、ひとまず「AVRCP_fail_case_UserManual.docx」をご参照の上、テストを進めていただけますでしょうか。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。 引き続きどうぞよろしくお願い申し上げます。

差出人 : Miyagawa, Yoichi (SEC)

送信日時 : 2025 年 10 月 30 日 19:39

宛先 : Itsuo Sakai ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

宮川です。

来週の御社側の状況理解しました。

状況に応じて対応方法検討します。

以上、よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 7:12 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > >11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。 > エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、 > そういうわけではない感じでしょうか？ ⇒望月から、Bluetooth専任エンジニアが試験できない間は別規格の認証試験担当にアサインされたProfile試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
>11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。
エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、
そういうわけではない感じでしょうか？

⇒ 望月から、 Bluetooth 専任エンジニアが試験できない間は別規格の認証試験担当にアサインされた Profile 試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

したがって全く試験できない訳ではありませんが、残件を分担させていただけると心強いです。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 18:56

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

一点確認をさせてください。
11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、そういうわけではない感じでしょうか？

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 6:52 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 本日望月が不在のため代わって返信させていただきます。 > A2DP/SRC/SUS/[ID] ですが、今のテレビソフトはSuspendを発行しない > ことが分かりました。 > A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付 >
にテストケース差し替えをお願いできますでしょうか？ ⇒ご連絡ありがとうございます。 A2DP ICS 1/8: NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player list does not
contain a browsable player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]：Suspend
the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。
また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 > なお、テスト環境でもう一点確認があります。 >
テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。
差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1,
1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport
projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で >
Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = =
= = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel
[ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID
199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ >
前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220

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

---

## 15. 2025-11-04 07:07

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , AJ Bluetooth Group

望月さんお疲れさまです。

客先に以下の内容のメールを送信してください。

添付いただいたTestReporから始まる.xml形式のAVRCPログは認証エビデンスに使えません。

お手数ですが認証用PTSレポートは、単なるログではなくPTSでGenerate Report

機能により生成した「Report_AVRCP_2025」から始まる.xml Reportファイルをご提供ください。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年11月4日 15:53

宛先: Itsuo Sakai ; AJ Bluetooth Group

件名: RE: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん望月ですご確認ありがとうございます私の方でzip化しましたが、こちらで確認可能でしょうか。

可能でしたらお客様へはこの部分については要求しないで連絡いたします。

どうぞよろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, November 4, 2025 3:50 PM

To: Toshitaka Mochizuki ; AJ Bluetooth Group

Subject: Re: 【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

望月さんお疲れさまです。

客先には以下のように返信してください。

酒井ーーーー
A2DP/SRC/SYN/[ID] が [ID] になっていますが、 Test
Case Category
が D なので、不問ということで理解正しいでしょうか？
（A2DP はパスしたと考えてよいでしょうか？）

⇒ そのご認識通りです。 A2DP が認証登録に必要な試験項目を完了したことを明確にお知らせしてませんでした。申し訳ございません。
AVRCP の方は、 AVRCP/TG/MCN/CB/[ID] を残しすべて Pass したとのことです、
引き続き残った 1 件を進めています。

⇒ ありがとうございます。 AVRCP の PTS レポートを添付いただきましたが当方のメールサーバーが xml 拡張子のファイルを配信しないため、お手数ですが zip

圧縮後添付して再送をお願いします。
すべてパスしましたら、 Evidence log を提出します。

⇒ ありがとうございます。お手数をお掛けしますがよろしくお願いいたします。

ーーーー差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 11 月 4 日 15:44

宛先 : AJ Bluetooth Group

件名 : 【内部連絡】 FW:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

酒井さん中山さん

SONY様から以下の連絡がございました。

以下のご質問回答いただけますでしょうか。

添付もご確認ください。

どうぞよろしくお願いいたします。

望月

From:

Sent: Tuesday, November 4, 2025 3:36 PM

To: Toshitaka Mochizuki ; ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

すみません、一点確認させてください。

A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case CategoryがDなので、不問ということで理解正しいでしょうか？（A2DPはパスしたと考えてよいでしょうか？）

AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、引き続き残った1件を進めています。

すべてパスしましたら、Evidence logを提出します。

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Friday, October 31, 2025 7:29 PM

To: 'Toshitaka Mochizuki' ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

ファイルありがとうございました、ダウンロードできました。

チップベンダーと相談します、火曜日に進め方再度相談させてください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 7:22 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 大変お待たせいたしました。 ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。 以下のPasswordにてダウンロードください。 ----------------------------------------
[パスワード] nn<VVk~5 [パスワード有効期限] [ID] 19: 19 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

大変お待たせいたしました。

ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。

以下のPasswordにてダウンロードください。

[パスワード]

nn<VVk~5

[パスワード有効期限]

[ID] 19:19 まで

[送信ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 6:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

ファイルダウンロードできました、ありがとうございます。

本日終了時点でのリストの方もよろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 6:10 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 Failログなどをオフィス宅ふぁいる便で再送いたしましたので、 お送りしたリンクで以下のPasswordにてダウンロードください。 ---------------------------------------- [パスワード] RWG. 7r{y [パスワード有効期限]
[ID] 18: 07 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

Failログなどをオフィス宅ふぁいる便で再送いたしましたので、

お送りしたリンクで以下のPasswordにてダウンロードください。

[パスワード]

RWG.7r{y

[パスワード有効期限]

[ID] 18:07 まで

[送信ID]

ダウンロードできないようでしたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 5:14 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

申し訳ありません、添付ファイルが削除されてしまったようです。

下記拡張子のファイルが含まれると、削除されるとのこと。

&quot;386, &quot;3gr&quot;, &quot;add&quot;, &quot;ade&quot;, &quot;asp&quot;, &quot;bas&quot;, &quot;bat&quot;, &quot;chm&quot;, &quot;cmd&quot;, &quot;com&quot;, &quot;cpl&quot;, &quot;crt&quot;, &quot;dbx&quot;, &quot;dll&quot;, &quot;exe&quot;,

&quot;fon, &quot;hlp&quot;, &quot;hta&quot;, &quot;inf&quot;, &quot;ins&quot;, &quot;isp&quot;, &quot;js&quot;, &quot;jse&quot;, &quot;lnk&quot;, &quot;mdb&quot;, &quot;mde&quot;, &quot;msc&quot;, &quot;msi&quot;, &quot;msp&quot;, &quot;mst&quot;,

&quot;ocx, &quot;pcd&quot;, &quot;pif&quot;, &quot;reg&quot;, &quot;scr&quot;, &quot;sct&quot;, &quot;shs&quot;, &quot;shb&quot;, &quot;url&quot;, &quot;vb&quot;, &quot;vbe&quot;, &quot;vbs&quot;, &quot;vxd&quot;, &quot;wsc&quot;, &quot;wsf&quot;,

&quot;wsh,&quot;adp&quot;, &quot;ani&quot;, &quot;ht&quot;, &quot;job&quot;, &quot;mda&quot;, &quot;mdz&quot;, &quot;ws&quot;, &quot;ps1&quot;, &quot;ps1xml&quot;, &quot;ps2&quot;, &quot;ps2xml&quot;, &quot;psc1&quot;, &quot;psc2&quot;,

&quot;msh, &quot;msh1&quot;, &quot;msh2&quot;, &quot;mshxml&quot;, &quot;msh1xml&quot;, &quot;msh2xml&quot;, &quot;scf&quot;, &quot;class&quot;, &quot;jar&quot;, &quot;iqy&quot;, &quot;psm1&quot;, &quot;pssc&quot;

&quot;apk, &quot;app&quot;, &quot;appcontent-ms&quot;, &quot;appref-ms&quot;, &quot;appx&quot;, &quot;aspx&quot;, &quot;asx&quot;, &quot;cdxml&quot;, &quot;cer&quot;, &quot;cnt&quot;

&quot;csh, &quot;der&quot;, &quot;diagcab&quot;, &quot;fxp&quot;, &quot;gadget&quot;, &quot;grp&quot;, &quot;hpj&quot;, &quot;htc&quot;, &quot;its&quot;, &quot;jnlp&quot;, &quot;ksh&quot;, &quot;mad&quot;

&quot;maf, &quot;mag&quot;, &quot;mam&quot;, &quot;maq&quot;, &quot;mar&quot;, &quot;mas&quot;, &quot;mat&quot;, &quot;mau&quot;, &quot;mav&quot;, &quot;maw&quot;, &quot;mcf&quot;, &quot;mdt&quot;, &quot;mdw&quot;, &quot;mht&quot;

&quot;mhtml, &quot;msu&quot;, &quot;ops&quot;, &quot;pl&quot;, &quot;plg&quot;, &quot;prf&quot;, &quot;prg&quot;, &quot;printerexport&quot;, &quot;psd1&quot;, &quot;psdm1&quot;, &quot;pst&quot;, &quot;py&quot;, &quot;pyc&quot;

&quot;pyo, &quot;pyw&quot;, &quot;pyz&quot;, &quot;pyzw&quot;, &quot;settingcontent-ms&quot;, &quot;theme&quot;, &quot;tmp&quot;, &quot;udl&quot;, &quot;vbp&quot;, &quot;vhd&quot;, &quot;vhdx&quot;, &quot;vsmacros&quot;

&quot;vss, &quot;vst&quot;, &quot;vsw&quot;, &quot;webpnp&quot;, &quot;website&quot;, &quot;wsb&quot;, &quot;xbap&quot;, &quot;xll&quot;, &quot;xnk&quot;

ひとまず、本日の確認終わりましたら、エクセルでリスト頂けますでしょうか？

Evidence log取得が終わっていないテストケースについて色付けしてリスト頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 4:24 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、 Fail となっていた項目は依然として Pass にはなっていません。 すべての Fail 項目への再確認はまた完了していないですが、 「The
media player list does not contain a browsable player」または 「Failed to retrieve

An email has been sent to you which contained one or more attachments, some of which are not permitted for security reasons. Please contact your local helpdesk for advice on how to securely share files with external
parties.

Attachment(s) deleted: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

Sender:

Date: [ID]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proofpointにより添付ファイルが削除されました。セキュリティ上の理由から許可されていない添付ファイルが1つ以上含まれている電子メールが送信されたためです。

削除された添付ファイル名: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

送信者:

日付: [ID]

外部の顧客と安全にファイルを共有する方法については、以下のURLをご参照ください。

< [URL] >

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、

Fail となっていた項目は依然として Pass にはなっていません。

すべての Fail 項目への再確認はまた完了していないですが、

「The media player list does not contain a browsable player」または

「Failed to retrieve Media Player List」

というエラーが発生したことにより、試験結果は [ID] または Fail となっております。

取り急ぎ、再試験した項目のテストログ、スクリーンショット、および写真を添付いたしますので、ご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 4:18 PM

To: ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

本日安井より情報を入れさせて頂きましたが、これで少し評価進みましたでしょうか？

Failなど残りましたら、チップベンダーにEvidence log取得の依頼をかけることも考えておりますので、本日終了時点で進捗状況お知らせ頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Friday, October 31, 2025 12:32 PM

To: Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、チップベンダー様からの情報によると、テストでは Google Play Music を使用することが大事なように思われます。

以下、そちらの情報です。

I have shared the User Manuals for these failed test items with you via MTK FEX.

It also includes the required Google Music and MP3 files.

Please follow the SOP for each test item in the User Manual to conduct the tests.

Because most of these test items require the use of Google Music.

If you encounter any difficulties installing Google Music, please let me know.

I will check it tomorrow night. (As you know, I am currently attending military reservist training...)

Additionally, regarding AVRCP/TG/MPS/[ID], we do not have experience testing this item.

However, based on the information provided by the lab, it also requires the use of Google Music.

You can try the following steps to see if you can pass this test item:

1.
Install the Google Play Music app

2.
Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

3.
Play then pause the music in Google Play Music

4.
Make sure PTS and IUT are paired

5.
Run PTS to start the test case AVRCP/TG/MPS/[ID]

6.
PTS will pop up a message (&quot;Received Play Command, press Yes&quot;)

7.
If Google Play Music starts playing music, click &quot;Yes&quot;; if it does not start playing, click &quot;No&quot;.

弊社でもこちらのやり方を調査しておりまして、以下の部分を補足させていただきます。

・ Google Play Music のインストール方法

PC とテレビを adb
接続していただき、以前お送りした GoogleMusic.apk が入っているフォルダからコマンドプロンプトで

adb root

adb install GoogleMusic.apk

adb reboot

と打っていただくとインストールできます。

・ Google Play Music の開き方設定 → アプリ → アプリをすべて表示 → システムアプリの表示 →Google
Play Musuic

から開いていただくと、開けますその際サーバーエラーのような画面が出ますが、 OK を何度か押していただくとプレイリストの画面まで進むことができると思います。

その後、リモコンで上ボタンを押すと、画像左上の 3 本の線がある部分にカーソルが表示されますので、その状態であれば Google
Play Music を操作することが可能になるように思われます。

・ Goole Play Music に mp3 ファイルを入れる方法

Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

との記載がありますが、こちらでうまくいかない場合は

mp3 ファイルを USB メモリに入れていただき、テレビのもう一つの USB ポート (addb 接続している USB ポートの隣 ) に接続していただくと Google
Play Music 上でもプレイリストが表示されるように思われます。

弊社の方でも、こちらのやり方引き続き調査しますので、ひとまず「AVRCP_fail_case_UserManual.docx」をご参照の上、テストを進めていただけますでしょうか。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。 引き続きどうぞよろしくお願い申し上げます。

差出人 : Miyagawa, Yoichi (SEC)

送信日時 : 2025 年 10 月 30 日 19:39

宛先 : Itsuo Sakai ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

宮川です。

来週の御社側の状況理解しました。

状況に応じて対応方法検討します。

以上、よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 7:12 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > >11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。 > エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、 > そういうわけではない感じでしょうか？ ⇒望月から、Bluetooth専任エンジニアが試験できない間は別規格の認証試験担当にアサインされたProfile試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
>11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。
エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、
そういうわけではない感じでしょうか？

⇒ 望月から、 Bluetooth 専任エンジニアが試験できない間は別規格の認証試験担当にアサインされた Profile 試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

したがって全く試験できない訳ではありませんが、残件を分担させていただけると心強いです。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 18:56

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

一点確認をさせてください。
11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、そういうわけではない感じでしょうか？

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 6:52 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 本日望月が不在のため代わって返信させていただきます。 > A2DP/SRC/SUS/[ID] ですが、今のテレビソフトはSuspendを発行しない > ことが分かりました。 > A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付 > にテストケース差し替えをお願いできますでしょうか？ ⇒ご連絡ありがとうございます。 A2DP
ICS 1/8: NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player list does not contain a browsable
player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]：Suspend
the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。
また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 > なお、テスト環境でもう一点確認があります。 >
テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。 差出人:
Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1,
1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport
projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で >
Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID] 以上、よろしくお願いいたします。
アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID]
内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？ ⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、
これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID 199247のときは > A2DP
1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ >
前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 > なお本件、3年前に御社に依頼したD062233の、OSバージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID] > >
無線モジュールやRF仕様の変更はないため、D062233の際作成したRF/RFPHYのテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID]
東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220

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

---

## 16. 2025-11-05 01:06

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki
**Attachments:** ���������������������������.doc

望月さんお疲れさまです。
ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、
ご確認いただけますでしょうか。

⇒最新バージョンが問題であるかどうかはログでは分かりませんが、

これまで、PTSの更新で前のバージョンでPassしていた試験項目が

Passしなくなることは頻発しています。

客先の質問は「PTSバージョンが異なるレポートの混在は可能か？」

ですので以下の回答を返信してください。

酒井ーーーー
AVRCP/TG/MCN/CB/[ID]
本件ですが、古いバージョンのPTS（ETS version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

⇒古いバージョンでのPassのご確認ありがとうございます。

PTSはこれまでも更新バージョンでそれまでPassしていた試験項目が

Passしなくなることは少なからず発生していました。
TestReport_AVRCP_2025_11_04_20_57_51.zip：AVRCP/TG/MCN/CB/[ID]
のEvidence Log (ETS version [ID])
TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外のEvidence Log
(ETS version [ID])
このようにテストレポート分割してQualificationを進めることは可能でしょうか？

⇒はい、試験対象プロファイルが最新のPTSバージョンでPassしない場合に一部試験項目を異なるPTSバージョンで実施してPTSレポートが複数ファイルになってもエビデンスとして有効で問題ございません。

代行登録作業を進ますのでお手数ですが添付の代行登録内容確認書にご記入の上ご提出をお願いします。

ーーーー差出人: Toshitaka Mochizuki

送信日時: 2025年11月5日 09:44

宛先: Itsuo Sakai

件名: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん望月です

ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、

ご確認いただけますでしょうか。

どうぞよろしくお願いいたします。

From:

Sent: Wednesday, November 5, 2025 9:40 AM

To: Toshitaka Mochizuki ; ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

AVRCP/TG/MCN/CB/[ID]

本件ですが、古いバージョンの PTS （ETS version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

TestReport_AVRCP_2025_11_04_20_57_51.zip： AVRCP/TG/MCN/CB/[ID] の Evidence
Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外の Evidence Log (ETS version
[ID])

このようにテストレポート分割して Qualification を進めることは可能でしょうか？

それともすべてのテストを ETS version [ID] でパスさせる必要ありますか？

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 4:11 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ; Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 続けて失礼いたします。 添付いただいた TestRepor から始まる . xml 形式の AVRCP ログは認証エビデンスに使えません。 お手数ですが認証用 PTS レポートは、単なるログではなく PTS で Generate Report
機能により生成した「Report_AVRCP_2025」から始まる . xml Report ファイルをご提供ください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

続けて失礼いたします。

添付いただいた TestRepor から始まる .xml 形式の AVRCP ログは認証エビデンスに使えません。

お手数ですが認証用 PTS レポートは、単なるログではなく PTS で Generate Report

機能により生成した「Report_AVRCP_2025」から始まる .xml Report ファイルをご提供ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 3:55 PM

To: ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。
A2DP/SRC/SYN/[ID] が [ID] になっていますが、 Test
Case Category
が D なので、不問ということで理解正しいでしょうか？
（A2DP はパスしたと考えてよいでしょうか？）

⇒そのご認識通りです。 A2DP が認証登録に必要な試験項目を完了したことを明確にお知らせしておりませんでした。申し訳ございません。
AVRCP の方は、 AVRCP/TG/MCN/CB/[ID] を残しすべて Pass したとのことです、
引き続き残った 1 件を進めています。
すべてパスしましたら、 Evidence log を提出します。

⇒ありがとうございます。お手数をお掛けしますが引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, November 4, 2025 3:36 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

すみません、一点確認させてください。

A2DP/SRC/SYN/[ID] が [ID] になっていますが、 Test Case Category が D なので、不問ということで理解正しいでしょうか？（A2DP はパスしたと考えてよいでしょうか？）

AVRCP の方は、 AVRCP/TG/MCN/CB/[ID] を残しすべて Pass したとのことです、引き続き残った 1 件を進めています。

すべてパスしましたら、 Evidence log を提出します。

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Friday, October 31, 2025 7:29 PM

To: 'Toshitaka Mochizuki' ; Yasui, Jun (SEC) ; Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

ファイルありがとうございました、ダウンロードできました。

チップベンダーと相談します、火曜日に進め方再度相談させてください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 7:22 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ; Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 大変お待たせいたしました。 ACRCP
全 Fail 項目の再試験した、テストログと測定結果纏め Excel 表をお送りいたします。 以下の Password にてダウンロードください。 ---------------------------------------- [ パスワード ] nn<VVk~5
[ パスワード有効期限 ] [ID] 19: 19
まで [ 送信 ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

大変お待たせいたしました。

ACRCP
全 Fail 項目の再試験した、テストログと測定結果纏め Excel 表をお送りいたします。

以下の Password にてダウンロードください。

[ パスワード ]

nn<VVk~5

[ パスワード有効期限 ]

[ID] 19:19
まで

[ 送信 ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 6:59 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

ファイルダウンロードできました、ありがとうございます。

本日終了時点でのリストの方もよろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 6:10 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 Fail ログなどをオフィス宅ふぁいる便で再送いたしましたので、 お送りしたリンクで以下の Password にてダウンロードください。 ----------------------------------------
[ パスワード ] RWG. 7r{y [ パスワード有効期限 ] [ID] 18: 07
まで [ 送信 ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

Fail ログなどをオフィス宅ふぁいる便で再送いたしましたので、

お送りしたリンクで以下の Password にてダウンロードください。

[ パスワード ]

RWG.7r{y

[ パスワード有効期限 ]

[ID] 18:07
まで

[ 送信 ID]

ダウンロードできないようでしたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 5:14 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

申し訳ありません、添付ファイルが削除されてしまったようです。

下記拡張子のファイルが含まれると、削除されるとのこと。

&quot;386, &quot;3gr&quot;, &quot;add&quot;, &quot;ade&quot;, &quot;asp&quot;, &quot;bas&quot;, &quot;bat&quot;, &quot;chm&quot;, &quot;cmd&quot;, &quot;com&quot;, &quot;cpl&quot;, &quot;crt&quot;, &quot;dbx&quot;, &quot;dll&quot;, &quot;exe&quot;,

&quot;fon, &quot;hlp&quot;, &quot;hta&quot;, &quot;inf&quot;, &quot;ins&quot;, &quot;isp&quot;, &quot;js&quot;, &quot;jse&quot;, &quot;lnk&quot;, &quot;mdb&quot;, &quot;mde&quot;, &quot;msc&quot;, &quot;msi&quot;, &quot;msp&quot;, &quot;mst&quot;,

&quot;ocx, &quot;pcd&quot;, &quot;pif&quot;, &quot;reg&quot;, &quot;scr&quot;, &quot;sct&quot;, &quot;shs&quot;, &quot;shb&quot;, &quot;url&quot;, &quot;vb&quot;, &quot;vbe&quot;, &quot;vbs&quot;, &quot;vxd&quot;, &quot;wsc&quot;, &quot;wsf&quot;,

&quot;wsh,&quot;adp&quot;, &quot;ani&quot;, &quot;ht&quot;, &quot;job&quot;, &quot;mda&quot;, &quot;mdz&quot;, &quot;ws&quot;, &quot;ps1&quot;, &quot;ps1xml&quot;, &quot;ps2&quot;, &quot;ps2xml&quot;, &quot;psc1&quot;, &quot;psc2&quot;,

&quot;msh, &quot;msh1&quot;, &quot;msh2&quot;, &quot;mshxml&quot;, &quot;msh1xml&quot;, &quot;msh2xml&quot;, &quot;scf&quot;, &quot;class&quot;, &quot;jar&quot;, &quot;iqy&quot;, &quot;psm1&quot;, &quot;pssc&quot;

&quot;apk, &quot;app&quot;, &quot;appcontent-ms&quot;, &quot;appref-ms&quot;, &quot;appx&quot;, &quot;aspx&quot;, &quot;asx&quot;, &quot;cdxml&quot;, &quot;cer&quot;, &quot;cnt&quot;

&quot;csh, &quot;der&quot;, &quot;diagcab&quot;, &quot;fxp&quot;, &quot;gadget&quot;, &quot;grp&quot;, &quot;hpj&quot;, &quot;htc&quot;, &quot;its&quot;, &quot;jnlp&quot;, &quot;ksh&quot;, &quot;mad&quot;

&quot;maf, &quot;mag&quot;, &quot;mam&quot;, &quot;maq&quot;, &quot;mar&quot;, &quot;mas&quot;, &quot;mat&quot;, &quot;mau&quot;, &quot;mav&quot;, &quot;maw&quot;, &quot;mcf&quot;, &quot;mdt&quot;, &quot;mdw&quot;, &quot;mht&quot;

&quot;mhtml, &quot;msu&quot;, &quot;ops&quot;, &quot;pl&quot;, &quot;plg&quot;, &quot;prf&quot;, &quot;prg&quot;, &quot;printerexport&quot;, &quot;psd1&quot;, &quot;psdm1&quot;, &quot;pst&quot;, &quot;py&quot;, &quot;pyc&quot;

&quot;pyo, &quot;pyw&quot;, &quot;pyz&quot;, &quot;pyzw&quot;, &quot;settingcontent-ms&quot;, &quot;theme&quot;, &quot;tmp&quot;, &quot;udl&quot;, &quot;vbp&quot;, &quot;vhd&quot;, &quot;vhdx&quot;, &quot;vsmacros&quot;

&quot;vss, &quot;vst&quot;, &quot;vsw&quot;, &quot;webpnp&quot;, &quot;website&quot;, &quot;wsb&quot;, &quot;xbap&quot;, &quot;xll&quot;, &quot;xnk&quot;

ひとまず、本日の確認終わりましたら、エクセルでリスト頂けますでしょうか？

Evidence log 取得が終わっていないテストケースについて色付けしてリスト頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 4:24 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 ご指定の方法で Google Play Music
にて音楽ファイルを再生できましたが、 Fail となっていた項目は依然として Pass
にはなっていません。 すべての Fail 項目への再確認はまた完了していないですが、 「The media player list does not contain a browsable player」または 「Failed to retrieve

An email has been sent to you which contained one or more attachments, some of which are not permitted for security reasons. Please contact your local helpdesk for advice on how to securely share files with external
parties.

Attachment(s) deleted: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

Sender:

Date: [ID]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proofpoint により添付ファイルが削除されました。セキュリティ上の理由から許可されていない添付ファイルが 1 つ以上含まれている電子メールが送信されたためです。

削除された添付ファイル名 : 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

送信者 :

---

## 17. 2025-11-05 01:27

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki

望月さんお疲れさまです。
Fail部分に関してはアリオンでFail項目部分の再試験を旧バージョンで行う必要はございますか？

⇒手順書が更新されていないのでアリオンがこれまでどおりの手順で試験しても客先(依頼先)で最新バージョンでPassした30項目はPass

しないと思います。旧バージョンでPassした1項目はアリオンでも

Passするかも知れませんが、時間もないのでアリオン発行レポートは客先のPassレポートを参照して作成を進めてください。これらの試験項目のレポートの試験場所記載欄はCustomerとしてください。
客先からのログをそのまま使用されますでしょうか。

⇒そのようにします。念のため客先に「ご送付いただいたPTSレポートで認証登録を進めるとともにアリオン発行プロファルレポートのPass

ログとして参照させていただきますのでよろしくお願いします」と事前申し入れをお願いします。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年11月5日 10:13

宛先: Itsuo Sakai

件名: RE: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん承知しました。

Fail部分に関してはアリオンでFail項目部分の再試験を旧バージョンで行う必要はございますか？

客先からのログをそのまま使用されますでしょうか。

本日中山さんが少々空きが生じておりますので確認作業、レポート作成は可能かと思います。

ご確認どうぞよろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, November 5, 2025 10:06 AM

To: Toshitaka Mochizuki

Subject: Re: 【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

望月さんお疲れさまです。
ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、
ご確認いただけますでしょうか。

⇒ 最新バージョンが問題であるかどうかはログでは分かりませんが、

これまで、 PTS の更新で前のバージョンで Pass していた試験項目が

Pass しなくなることは頻発しています。

客先の質問は「PTS バージョンが異なるレポートの混在は可能か？」

ですので以下の回答を返信してください。

酒井ーーーー
AVRCP/TG/MCN/CB/[ID]
本件ですが、古いバージョンの PTS （ETS
version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

⇒ 古いバージョンでの Pass のご確認ありがとうございます。

PTS はこれまでも更新バージョンでそれまで Pass していた試験項目が

Pass しなくなることは少なからず発生していました。
TestReport_AVRCP_2025_11_04_20_57_51.zip： AVRCP/TG/MCN/CB/[ID]
の Evidence Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外の Evidence
Log
(ETS version [ID])

このようにテストレポート分割して Qualification を進めることは可能でしょうか？

⇒ はい、試験対象プロファイルが最新の PTS バージョンで Pass しない場合に一部試験項目を異なる PTS バージョンで実施して PTS レポートが複数ファイルになってもエビデンスとして有効で問題ございません。

代行登録作業を進ますのでお手数ですが添付の代行登録内容確認書にご記入の上ご提出をお願いします。

ーーーー差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 11 月 5 日 09:44

宛先 : Itsuo Sakai

件名 :
【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

酒井さん望月です

ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、

ご確認いただけますでしょうか。

どうぞよろしくお願いいたします。

From:

Sent: Wednesday, November 5, 2025 9:40 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

AVRCP/TG/MCN/CB/[ID]

本件ですが、古いバージョンのPTS（ETS version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

TestReport_AVRCP_2025_11_04_20_57_51.zip：AVRCP/TG/MCN/CB/[ID]CのEvidence Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外のEvidence Log (ETS version [ID])

このようにテストレポート分割してQualificationを進めることは可能でしょうか？

それともすべてのテストを ETS version [ID]3でパスさせる必要ありますか？

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 4:11 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 続けて失礼いたします。 添付いただいたTestReporから始まる. xml形式のAVRCPログは認証エビデンスに使えません。 お手数ですが認証用PTSレポートは、単なるログではなくPTSでGenerate Report
機能により生成した「Report_AVRCP_2025」から始まる. xml Reportファイルをご提供ください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

続けて失礼いたします。

添付いただいたTestReporから始まる.xml形式のAVRCPログは認証エビデンスに使えません。

お手数ですが認証用PTSレポートは、単なるログではなくPTSでGenerate Report

機能により生成した「Report_AVRCP_2025」から始まる.xml Reportファイルをご提供ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 3:55 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。
A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case Category
がDなので、不問ということで理解正しいでしょうか？
（A2DPはパスしたと考えてよいでしょうか？）

⇒そのご認識通りです。A2DPが認証登録に必要な試験項目を完了したことを明確にお知らせしておりませんでした。申し訳ございません。
AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、
引き続き残った1件を進めています。
すべてパスしましたら、Evidence logを提出します。

⇒ありがとうございます。お手数をお掛けしますが引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, November 4, 2025 3:36 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

すみません、一点確認させてください。

A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case CategoryがDなので、不問ということで理解正しいでしょうか？（A2DPはパスしたと考えてよいでしょうか？）

AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、引き続き残った1件を進めています。

すべてパスしましたら、Evidence logを提出します。

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Friday, October 31, 2025 7:29 PM

To: 'Toshitaka Mochizuki' ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

ファイルありがとうございました、ダウンロードできました。

チップベンダーと相談します、火曜日に進め方再度相談させてください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 7:22 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 大変お待たせいたしました。 ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。 以下のPasswordにてダウンロードください。 ----------------------------------------
[パスワード] nn<VVk~5 [パスワード有効期限] [ID] 19: 19 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

大変お待たせいたしました。

ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。

以下のPasswordにてダウンロードください。

[パスワード]

nn<VVk~5

[パスワード有効期限]

[ID] 19:19 まで

[送信ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 6:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

ファイルダウンロードできました、ありがとうございます。

本日終了時点でのリストの方もよろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 6:10 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 Failログなどをオフィス宅ふぁいる便で再送いたしましたので、 お送りしたリンクで以下のPasswordにてダウンロードください。 ---------------------------------------- [パスワード]
RWG. 7r{y [パスワード有効期限] [ID] 18: 07 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

Failログなどをオフィス宅ふぁいる便で再送いたしましたので、

お送りしたリンクで以下のPasswordにてダウンロードください。

[パスワード]

RWG.7r{y

[パスワード有効期限]

[ID] 18:07 まで

[送信ID]

ダウンロードできないようでしたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 5:14 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

申し訳ありません、添付ファイルが削除されてしまったようです。

下記拡張子のファイルが含まれると、削除されるとのこと。

&quot;386, &quot;3gr&quot;, &quot;add&quot;, &quot;ade&quot;, &quot;asp&quot;, &quot;bas&quot;, &quot;bat&quot;, &quot;chm&quot;, &quot;cmd&quot;, &quot;com&quot;, &quot;cpl&quot;, &quot;crt&quot;, &quot;dbx&quot;, &quot;dll&quot;, &quot;exe&quot;,

&quot;fon, &quot;hlp&quot;, &quot;hta&quot;, &quot;inf&quot;, &quot;ins&quot;, &quot;isp&quot;, &quot;js&quot;, &quot;jse&quot;, &quot;lnk&quot;, &quot;mdb&quot;, &quot;mde&quot;, &quot;msc&quot;, &quot;msi&quot;, &quot;msp&quot;, &quot;mst&quot;,

&quot;ocx, &quot;pcd&quot;, &quot;pif&quot;, &quot;reg&quot;, &quot;scr&quot;, &quot;sct&quot;, &quot;shs&quot;, &quot;shb&quot;, &quot;url&quot;, &quot;vb&quot;, &quot;vbe&quot;, &quot;vbs&quot;, &quot;vxd&quot;, &quot;wsc&quot;, &quot;wsf&quot;,

&quot;wsh,&quot;adp&quot;, &quot;ani&quot;, &quot;ht&quot;, &quot;job&quot;, &quot;mda&quot;, &quot;mdz&quot;, &quot;ws&quot;, &quot;ps1&quot;, &quot;ps1xml&quot;, &quot;ps2&quot;, &quot;ps2xml&quot;, &quot;psc1&quot;, &quot;psc2&quot;,

&quot;msh, &quot;msh1&quot;, &quot;msh2&quot;, &quot;mshxml&quot;, &quot;msh1xml&quot;, &quot;msh2xml&quot;, &quot;scf&quot;, &quot;class&quot;, &quot;jar&quot;, &quot;iqy&quot;, &quot;psm1&quot;, &quot;pssc&quot;

&quot;apk, &quot;app&quot;, &quot;appcontent-ms&quot;, &quot;appref-ms&quot;, &quot;appx&quot;, &quot;aspx&quot;, &quot;asx&quot;, &quot;cdxml&quot;, &quot;cer&quot;, &quot;cnt&quot;

&quot;csh, &quot;der&quot;, &quot;diagcab&quot;, &quot;fxp&quot;, &quot;gadget&quot;, &quot;grp&quot;, &quot;hpj&quot;, &quot;htc&quot;, &quot;its&quot;, &quot;jnlp&quot;, &quot;ksh&quot;, &quot;mad&quot;

&quot;maf, &quot;mag&quot;, &quot;mam&quot;, &quot;maq&quot;, &quot;mar&quot;, &quot;mas&quot;, &quot;mat&quot;, &quot;mau&quot;, &quot;mav&quot;, &quot;maw&quot;, &quot;mcf&quot;, &quot;mdt&quot;, &quot;mdw&quot;, &quot;mht&quot;

&quot;mhtml, &quot;msu&quot;, &quot;ops&quot;, &quot;pl&quot;, &quot;plg&quot;, &quot;prf&quot;, &quot;prg&quot;, &quot;printerexport&quot;, &quot;psd1&quot;, &quot;psdm1&quot;, &quot;pst&quot;, &quot;py&quot;, &quot;pyc&quot;

&quot;pyo, &quot;pyw&quot;, &quot;pyz&quot;, &quot;pyzw&quot;, &quot;settingcontent-ms&quot;, &quot;theme&quot;, &quot;tmp&quot;, &quot;udl&quot;, &quot;vbp&quot;, &quot;vhd&quot;, &quot;vhdx&quot;, &quot;vsmacros&quot;

&quot;vss, &quot;vst&quot;, &quot;vsw&quot;, &quot;webpnp&quot;, &quot;website&quot;, &quot;wsb&quot;, &quot;xbap&quot;, &quot;xll&quot;, &quot;xnk&quot;

ひとまず、本日の確認終わりましたら、エクセルでリスト頂けますでしょうか？

Evidence log取得が終わっていないテストケースについて色付けしてリスト頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 4:24 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、 Fail となっていた項目は依然として Pass にはなっていません。 すべての Fail 項目への再確認はまた完了していないですが、
「The media player list does not contain a browsable player」または 「Failed to retrieve

An email has been sent to you which contained one or more attachments, some of which are not permitted for security reasons. Please contact your local helpdesk for advice on how to securely share
files with external parties.

Attachment(s) deleted: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

Sender:

Date: [ID]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proofpointにより添付ファイルが削除されました。セキュリティ上の理由から許可されていない添付ファイルが1つ以上含まれている電子メールが送信されたためです。

削除された添付ファイル名: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

送信者:

日付: [ID]

外部の顧客と安全にファイルを共有する方法については、以下のURLをご参照ください。

< [URL] >

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、

Fail となっていた項目は依然として Pass にはなっていません。

すべての Fail 項目への再確認はまた完了していないですが、

「The media player list does not contain a browsable player」または

「Failed to retrieve Media Player List」

というエラーが発生したことにより、試験結果は [ID] または Fail となっております。

取り急ぎ、再試験した項目のテストログ、スクリーンショット、および写真を添付いたしますので、ご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 4:18 PM

To: ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

本日安井より情報を入れさせて頂きましたが、これで少し評価進みましたでしょうか？

Failなど残りましたら、チップベンダーにEvidence log取得の依頼をかけることも考えておりますので、本日終了時点で進捗状況お知らせ頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Friday, October 31, 2025 12:32 PM

To: Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、チップベンダー様からの情報によると、テストでは Google Play Music を使用することが大事なように思われます。

以下、そちらの情報です。

I have shared the User Manuals for these failed test items with you via MTK FEX.

It also includes the required Google Music and MP3 files.

Please follow the SOP for each test item in the User Manual to conduct the tests.

Because most of these test items require the use of Google Music.

If you encounter any difficulties installing Google Music, please let me know.

I will check it tomorrow night. (As you know, I am currently attending military reservist training...)

Additionally, regarding AVRCP/TG/MPS/[ID], we do not have experience testing this item.

However, based on the information provided by the lab, it also requires the use of Google Music.

You can try the following steps to see if you can pass this test item:

1.
Install the Google Play Music app

2.
Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

3.
Play then pause the music in Google Play Music

4.
Make sure PTS and IUT are paired

5.
Run PTS to start the test case AVRCP/TG/MPS/[ID]

6.
PTS will pop up a message (&quot;Received Play Command, press Yes&quot;)

7.
If Google Play Music starts playing music, click &quot;Yes&quot;; if it does not start playing, click &quot;No&quot;.

弊社でもこちらのやり方を調査しておりまして、以下の部分を補足させていただきます。

・ Google Play Music のインストール方法

PC とテレビを adb
接続していただき、以前お送りした GoogleMusic.apk が入っているフォルダからコマンドプロンプトで

adb root

adb install GoogleMusic.apk

adb reboot

と打っていただくとインストールできます。

・ Google Play Music の開き方設定 → アプリ → アプリをすべて表示 → システムアプリの表示 →Google
Play Musuic

から開いていただくと、開けますその際サーバーエラーのような画面が出ますが、 OK を何度か押していただくとプレイリストの画面まで進むことができると思います。

その後、リモコンで上ボタンを押すと、画像左上の 3 本の線がある部分にカーソルが表示されますので、その状態であれば Google
Play Music を操作することが可能になるように思われます。

・ Goole Play Music に mp3 ファイルを入れる方法

Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

との記載がありますが、こちらでうまくいかない場合は

mp3 ファイルを USB メモリに入れていただき、テレビのもう一つの USB ポート (addb 接続している USB ポートの隣 ) に接続していただくと Google
Play Music 上でもプレイリストが表示されるように思われます。

弊社の方でも、こちらのやり方引き続き調査しますので、ひとまず「AVRCP_fail_case_UserManual.docx」をご参照の上、テストを進めていただけますでしょうか。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。 引き続きどうぞよろしくお願い申し上げます。

差出人 : Miyagawa, Yoichi (SEC)

送信日時 : 2025 年 10 月 30 日 19:39

宛先 : Itsuo Sakai ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

宮川です。

来週の御社側の状況理解しました。

状況に応じて対応方法検討します。

以上、よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 7:12 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > >11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。 > エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、 > そういうわけではない感じでしょうか？ ⇒望月から、Bluetooth専任エンジニアが試験できない間は別規格の認証試験担当にアサインされたProfile試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
>11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。
エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、
そういうわけではない感じでしょうか？

⇒ 望月から、 Bluetooth 専任エンジニアが試験できない間は別規格の認証試験担当にアサインされた Profile 試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

したがって全く試験できない訳ではありませんが、残件を分担させていただけると心強いです。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 18:56

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

一点確認をさせてください。
11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、そういうわけではない感じでしょうか？

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 6:52 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 本日望月が不在のため代わって返信させていただきます。 > A2DP/SRC/SUS/[ID] ですが、今のテレビソフトはSuspendを発行しない > ことが分かりました。 > A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付 >
にテストケース差し替えをお願いできますでしょうか？ ⇒ご連絡ありがとうございます。 A2DP ICS 1/8: NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player list does not
contain a browsable player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]：Suspend
the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。
また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 > なお、テスト環境でもう一点確認があります。 >
テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。
差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1,
1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport
projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で >
Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = =
= = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel
[ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID
199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ >
前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220

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

---

## 18. 2025-11-05 02:25

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki

中山さんお疲れさまです。

Sony様向レポート作成の最初の段階で、アリオン実施A2DPおよびAVRCPの

Pass項目だけ選んでPTSレポートを再生成するとともにTeams共有フォルダにアップロードしてください。

酒井差出人: Itsuo Sakai

送信日時: 2025年11月5日 10:27

宛先: Toshitaka Mochizuki

件名: Re: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

望月さんお疲れさまです。
Fail部分に関してはアリオンでFail項目部分の再試験を旧バージョンで行う必要はございますか？

⇒手順書が更新されていないのでアリオンがこれまでどおりの手順で試験しても客先(依頼先)で最新バージョンでPassした30項目はPass

しないと思います。旧バージョンでPassした1項目はアリオンでも

Passするかも知れませんが、時間もないのでアリオン発行レポートは客先のPassレポートを参照して作成を進めてください。これらの試験項目のレポートの試験場所記載欄はCustomerとしてください。
客先からのログをそのまま使用されますでしょうか。

⇒そのようにします。念のため客先に「ご送付いただいたPTSレポートで認証登録を進めるとともにアリオン発行プロファルレポートのPass

ログとして参照させていただきますのでよろしくお願いします」と事前申し入れをお願いします。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年11月5日 10:13

宛先: Itsuo Sakai

件名: RE: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さん承知しました。

Fail部分に関してはアリオンでFail項目部分の再試験を旧バージョンで行う必要はございますか？

客先からのログをそのまま使用されますでしょうか。

本日中山さんが少々空きが生じておりますので確認作業、レポート作成は可能かと思います。

ご確認どうぞよろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, November 5, 2025 10:06 AM

To: Toshitaka Mochizuki

Subject: Re: 【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

望月さんお疲れさまです。

ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、

ご確認いただけますでしょうか。

⇒ 最新バージョンが問題であるかどうかはログでは分かりませんが、

これまで、 PTS の更新で前のバージョンで Pass していた試験項目が

Pass しなくなることは頻発しています。

客先の質問は「PTS バージョンが異なるレポートの混在は可能か？」

ですので以下の回答を返信してください。

酒井ーーーー
AVRCP/TG/MCN/CB/[ID]

本件ですが、古いバージョンの PTS （ETS
version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

⇒ 古いバージョンでの Pass のご確認ありがとうございます。

PTS はこれまでも更新バージョンでそれまで Pass していた試験項目が

Pass しなくなることは少なからず発生していました。
TestReport_AVRCP_2025_11_04_20_57_51.zip： AVRCP/TG/MCN/CB/[ID]

の Evidence Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外の Evidence
Log
(ETS version [ID])

このようにテストレポート分割して Qualification を進めることは可能でしょうか？

⇒ はい、試験対象プロファイルが最新の PTS バージョンで Pass しない場合に一部試験項目を異なる PTS バージョンで実施して PTS レポートが複数ファイルになってもエビデンスとして有効で問題ございません。

代行登録作業を進ますのでお手数ですが添付の代行登録内容確認書にご記入の上ご提出をお願いします。

ーーーー差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 11 月 5 日 09:44

宛先 : Itsuo Sakai

件名 :
【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

酒井さん望月です

ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、

ご確認いただけますでしょうか。

どうぞよろしくお願いいたします。

From:

Sent: Wednesday, November 5, 2025 9:40 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

AVRCP/TG/MCN/CB/[ID]

本件ですが、古いバージョンのPTS（ETS version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

TestReport_AVRCP_2025_11_04_20_57_51.zip：AVRCP/TG/MCN/CB/[ID]CのEvidence Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外のEvidence Log (ETS version [ID])

このようにテストレポート分割してQualificationを進めることは可能でしょうか？

それともすべてのテストを ETS version [ID]3でパスさせる必要ありますか？

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 4:11 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 続けて失礼いたします。 添付いただいたTestReporから始まる. xml形式のAVRCPログは認証エビデンスに使えません。 お手数ですが認証用PTSレポートは、単なるログではなくPTSでGenerate Report 機能により生成した「Report_AVRCP_2025」から始まる. xml Reportファイルをご提供ください。 どうぞよろしくお願い申し上げます。
ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

続けて失礼いたします。

添付いただいたTestReporから始まる.xml形式のAVRCPログは認証エビデンスに使えません。

お手数ですが認証用PTSレポートは、単なるログではなくPTSでGenerate Report

機能により生成した「Report_AVRCP_2025」から始まる.xml Reportファイルをご提供ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 3:55 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。
A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case Category
がDなので、不問ということで理解正しいでしょうか？
（A2DPはパスしたと考えてよいでしょうか？）

⇒そのご認識通りです。A2DPが認証登録に必要な試験項目を完了したことを明確にお知らせしておりませんでした。申し訳ございません。
AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、
引き続き残った1件を進めています。
すべてパスしましたら、Evidence logを提出します。

⇒ありがとうございます。お手数をお掛けしますが引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, November 4, 2025 3:36 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

すみません、一点確認させてください。

A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case CategoryがDなので、不問ということで理解正しいでしょうか？（A2DPはパスしたと考えてよいでしょうか？）

AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、引き続き残った1件を進めています。

すべてパスしましたら、Evidence logを提出します。

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Friday, October 31, 2025 7:29 PM

To: 'Toshitaka Mochizuki' ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

ファイルありがとうございました、ダウンロードできました。

チップベンダーと相談します、火曜日に進め方再度相談させてください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 7:22 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 大変お待たせいたしました。 ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。 以下のPasswordにてダウンロードください。 ---------------------------------------- [パスワード] nn<VVk~5 [パスワード有効期限] [ID] 19: 19 まで [送信ID]
[ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

大変お待たせいたしました。

ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。

以下のPasswordにてダウンロードください。

[パスワード]

nn<VVk~5

[パスワード有効期限]

[ID] 19:19 まで

[送信ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 6:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

ファイルダウンロードできました、ありがとうございます。

本日終了時点でのリストの方もよろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 6:10 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 Failログなどをオフィス宅ふぁいる便で再送いたしましたので、 お送りしたリンクで以下のPasswordにてダウンロードください。 ---------------------------------------- [パスワード] RWG. 7r{y [パスワード有効期限] [ID] 18: 07 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

Failログなどをオフィス宅ふぁいる便で再送いたしましたので、

お送りしたリンクで以下のPasswordにてダウンロードください。

[パスワード]

RWG.7r{y

[パスワード有効期限]

[ID] 18:07 まで

[送信ID]

ダウンロードできないようでしたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 5:14 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

申し訳ありません、添付ファイルが削除されてしまったようです。

下記拡張子のファイルが含まれると、削除されるとのこと。

&quot;386, &quot;3gr&quot;, &quot;add&quot;, &quot;ade&quot;, &quot;asp&quot;, &quot;bas&quot;, &quot;bat&quot;, &quot;chm&quot;, &quot;cmd&quot;, &quot;com&quot;, &quot;cpl&quot;, &quot;crt&quot;, &quot;dbx&quot;, &quot;dll&quot;, &quot;exe&quot;,

&quot;fon, &quot;hlp&quot;, &quot;hta&quot;, &quot;inf&quot;, &quot;ins&quot;, &quot;isp&quot;, &quot;js&quot;, &quot;jse&quot;, &quot;lnk&quot;, &quot;mdb&quot;, &quot;mde&quot;, &quot;msc&quot;, &quot;msi&quot;, &quot;msp&quot;, &quot;mst&quot;,

&quot;ocx, &quot;pcd&quot;, &quot;pif&quot;, &quot;reg&quot;, &quot;scr&quot;, &quot;sct&quot;, &quot;shs&quot;, &quot;shb&quot;, &quot;url&quot;, &quot;vb&quot;, &quot;vbe&quot;, &quot;vbs&quot;, &quot;vxd&quot;, &quot;wsc&quot;, &quot;wsf&quot;,

&quot;wsh,&quot;adp&quot;, &quot;ani&quot;, &quot;ht&quot;, &quot;job&quot;, &quot;mda&quot;, &quot;mdz&quot;, &quot;ws&quot;, &quot;ps1&quot;, &quot;ps1xml&quot;, &quot;ps2&quot;, &quot;ps2xml&quot;, &quot;psc1&quot;, &quot;psc2&quot;,

&quot;msh, &quot;msh1&quot;, &quot;msh2&quot;, &quot;mshxml&quot;, &quot;msh1xml&quot;, &quot;msh2xml&quot;, &quot;scf&quot;, &quot;class&quot;, &quot;jar&quot;, &quot;iqy&quot;, &quot;psm1&quot;, &quot;pssc&quot;

&quot;apk, &quot;app&quot;, &quot;appcontent-ms&quot;, &quot;appref-ms&quot;, &quot;appx&quot;, &quot;aspx&quot;, &quot;asx&quot;, &quot;cdxml&quot;, &quot;cer&quot;, &quot;cnt&quot;

&quot;csh, &quot;der&quot;, &quot;diagcab&quot;, &quot;fxp&quot;, &quot;gadget&quot;, &quot;grp&quot;, &quot;hpj&quot;, &quot;htc&quot;, &quot;its&quot;, &quot;jnlp&quot;, &quot;ksh&quot;, &quot;mad&quot;

&quot;maf, &quot;mag&quot;, &quot;mam&quot;, &quot;maq&quot;, &quot;mar&quot;, &quot;mas&quot;, &quot;mat&quot;, &quot;mau&quot;, &quot;mav&quot;, &quot;maw&quot;, &quot;mcf&quot;, &quot;mdt&quot;, &quot;mdw&quot;, &quot;mht&quot;

&quot;mhtml, &quot;msu&quot;, &quot;ops&quot;, &quot;pl&quot;, &quot;plg&quot;, &quot;prf&quot;, &quot;prg&quot;, &quot;printerexport&quot;, &quot;psd1&quot;, &quot;psdm1&quot;, &quot;pst&quot;, &quot;py&quot;, &quot;pyc&quot;

&quot;pyo, &quot;pyw&quot;, &quot;pyz&quot;, &quot;pyzw&quot;, &quot;settingcontent-ms&quot;, &quot;theme&quot;, &quot;tmp&quot;, &quot;udl&quot;, &quot;vbp&quot;, &quot;vhd&quot;, &quot;vhdx&quot;, &quot;vsmacros&quot;

&quot;vss, &quot;vst&quot;, &quot;vsw&quot;, &quot;webpnp&quot;, &quot;website&quot;, &quot;wsb&quot;, &quot;xbap&quot;, &quot;xll&quot;, &quot;xnk&quot;

ひとまず、本日の確認終わりましたら、エクセルでリスト頂けますでしょうか？

Evidence log取得が終わっていないテストケースについて色付けしてリスト頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 4:24 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、 Fail となっていた項目は依然として Pass にはなっていません。 すべての Fail 項目への再確認はまた完了していないですが、 「The media player list does not contain a browsable
player」または 「Failed to retrieve

An email has been sent to you which contained one or more attachments, some of which are not permitted for security reasons. Please contact your local helpdesk for advice on how to securely share files with external parties.

Attachment(s) deleted: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

Sender:

Date: [ID]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proofpointにより添付ファイルが削除されました。セキュリティ上の理由から許可されていない添付ファイルが1つ以上含まれている電子メールが送信されたためです。

削除された添付ファイル名: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

送信者:

日付: [ID]

外部の顧客と安全にファイルを共有する方法については、以下のURLをご参照ください。

< [URL] >

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、

Fail となっていた項目は依然として Pass にはなっていません。

すべての Fail 項目への再確認はまた完了していないですが、

「The media player list does not contain a browsable player」または

「Failed to retrieve Media Player List」

というエラーが発生したことにより、試験結果は [ID] または Fail となっております。

取り急ぎ、再試験した項目のテストログ、スクリーンショット、および写真を添付いたしますので、ご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 4:18 PM

To: ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

本日安井より情報を入れさせて頂きましたが、これで少し評価進みましたでしょうか？

Failなど残りましたら、チップベンダーにEvidence log取得の依頼をかけることも考えておりますので、本日終了時点で進捗状況お知らせ頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Friday, October 31, 2025 12:32 PM

To: Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、チップベンダー様からの情報によると、テストでは Google Play Music を使用することが大事なように思われます。

以下、そちらの情報です。

I have shared the User Manuals for these failed test items with you via MTK FEX.

It also includes the required Google Music and MP3 files.

Please follow the SOP for each test item in the User Manual to conduct the tests.

Because most of these test items require the use of Google Music.

If you encounter any difficulties installing Google Music, please let me know.

I will check it tomorrow night. (As you know, I am currently attending military reservist training...)

Additionally, regarding AVRCP/TG/MPS/[ID], we do not have experience testing this item.

However, based on the information provided by the lab, it also requires the use of Google Music.

You can try the following steps to see if you can pass this test item:

1.
Install the Google Play Music app

2.
Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

3.
Play then pause the music in Google Play Music

4.
Make sure PTS and IUT are paired

5.
Run PTS to start the test case AVRCP/TG/MPS/[ID]

6.
PTS will pop up a message (&quot;Received Play Command, press Yes&quot;)

7.
If Google Play Music starts playing music, click &quot;Yes&quot;; if it does not start playing, click &quot;No&quot;.

弊社でもこちらのやり方を調査しておりまして、以下の部分を補足させていただきます。

・ Google Play Music のインストール方法

PC とテレビを adb
接続していただき、以前お送りした GoogleMusic.apk が入っているフォルダからコマンドプロンプトで

adb root

adb install GoogleMusic.apk

adb reboot

と打っていただくとインストールできます。

・ Google Play Music の開き方設定 → アプリ → アプリをすべて表示 → システムアプリの表示 →Google
Play Musuic

から開いていただくと、開けますその際サーバーエラーのような画面が出ますが、 OK を何度か押していただくとプレイリストの画面まで進むことができると思います。

その後、リモコンで上ボタンを押すと、画像左上の 3 本の線がある部分にカーソルが表示されますので、その状態であれば Google
Play Music を操作することが可能になるように思われます。

・ Goole Play Music に mp3 ファイルを入れる方法

Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

との記載がありますが、こちらでうまくいかない場合は

mp3 ファイルを USB メモリに入れていただき、テレビのもう一つの USB ポート (addb 接続している USB ポートの隣 ) に接続していただくと Google
Play Music 上でもプレイリストが表示されるように思われます。

弊社の方でも、こちらのやり方引き続き調査しますので、ひとまず「AVRCP_fail_case_UserManual.docx」をご参照の上、テストを進めていただけますでしょうか。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。 引き続きどうぞよろしくお願い申し上げます。

差出人 : Miyagawa, Yoichi (SEC)

送信日時 : 2025 年 10 月 30 日 19:39

宛先 : Itsuo Sakai ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

宮川です。

来週の御社側の状況理解しました。

状況に応じて対応方法検討します。

以上、よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 7:12 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > >11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。 > エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、 > そういうわけではない感じでしょうか？ ⇒望月から、Bluetooth専任エンジニアが試験できない間は別規格の認証試験担当にアサインされたProfile試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
>11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、

そういうわけではない感じでしょうか？

⇒ 望月から、 Bluetooth 専任エンジニアが試験できない間は別規格の認証試験担当にアサインされた Profile 試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

したがって全く試験できない訳ではありませんが、残件を分担させていただけると心強いです。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 18:56

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

一点確認をさせてください。
11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、そういうわけではない感じでしょうか？

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 6:52 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 本日望月が不在のため代わって返信させていただきます。 > A2DP/SRC/SUS/[ID] ですが、今のテレビソフトはSuspendを発行しない > ことが分かりました。 > A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付 >
にテストケース差し替えをお願いできますでしょうか？ ⇒ご連絡ありがとうございます。 A2DP ICS 1/8: NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player
list does not contain a browsable player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l
A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。
もしサイズが大きい物でしたらあらかじめお知らせください。 また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 >
なお、テスト環境でもう一点確認があります。 > テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。
以上よろしくお願いいたします。 差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。
次に(2)ICS SelectionでCore階層を選択し、12/1, 1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。
なお、当方のメールシステムがExport projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 >
・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で > Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 =
= = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel
[ID] 以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 >
3年前のQDID 199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

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

---

## 19. 2025-11-05 05:35

**From:** Itsuo Sakai
**To:** Kousuke Nakayama

中山さんお疲れさまです。
先程アップロードしたPTSレポートですが、テストプランにないもの
(IOPT)が含まれていました。

⇒IOPT項目を削除したReportの再Generateありがとうございます。

今後はPsssであれば不要な試験項目が含まれていても問題ないため、

Reportを再Generateしなくても結構です。

酒井差出人: Kousuke Nakayama

送信日時: 2025年11月5日 14:25

宛先: Itsuo Sakai

件名: RE: 【内部連絡】FW: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

酒井さんお疲れ様です。中山です。

先程アップロードした PTS レポートですが、テストプランにないもの (IOPT) が含まれていました。

大変失礼いたしました。

IOPT 項目を削除したものをアップロードいたしましたのでお手数ですが確認いただけますでしょうか。

Sony TV

よろしくお願いいたします。

中山光祐

From: Kousuke Nakayama

Sent: Wednesday, November 5, 2025 12:26 PM

To: Itsuo Sakai

Subject: RE: 【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

酒井さんお疲れ様です。中山です。

以下に Log をアップロードしました。

お手数ですが確認お願い致します。

Log.zip

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Wednesday, November 5, 2025 11:25 AM

To: Toshitaka Mochizuki

Subject: Re: 【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

中山さんお疲れさまです。

Sony 様向レポート作成の最初の段階で、アリオン実施 A2DP および AVRCP の

Pass 項目だけ選んで PTS レポートを再生成するとともに Teams 共有フォルダにアップロードしてください。

酒井差出人 : Itsuo
Sakai

送信日時 : 2025 年 11 月 5 日
10:27

宛先 : Toshitaka
Mochizuki

件名 : Re:
【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

望月さんお疲れさまです。
Fail 部分に関してはアリオンで Fail 項目部分の再試験を旧バージョンで行う必要はございますか？

⇒ 手順書が更新されていないのでアリオンがこれまでどおりの手順で試験しても客先 ( 依頼先 ) で最新バージョンで Pass した 30 項目は Pass

しないと思います。旧バージョンで Pass した 1 項目はアリオンでも

Pass するかも知れませんが、時間もないのでアリオン発行レポートは客先の Pass レポートを参照して作成を進めてください。これらの試験項目のレポートの試験場所記載欄は Customer としてください。
客先からのログをそのまま使用されますでしょうか。

⇒ そのようにします。念のため客先に「ご送付いただいた PTS レポートで認証登録を進めるとともにアリオン発行プロファルレポートの Pass

ログとして参照させていただきますのでよろしくお願いします」と事前申し入れをお願いします。

酒井差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 11 月 5 日
10:13

宛先 : Itsuo
Sakai

件名 : RE:
【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

酒井さん承知しました。

Fail 部分に関してはアリオンで Fail 項目部分の再試験を旧バージョンで行う必要はございますか？

客先からのログをそのまま使用されますでしょうか。

本日中山さんが少々空きが生じておりますので確認作業、レポート作成は可能かと思います。

ご確認どうぞよろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, November 5, 2025 10:06 AM

To: Toshitaka Mochizuki

Subject: Re: 【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

望月さんお疲れさまです。
ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、
ご確認いただけますでしょうか。

⇒ 最新バージョンが問題であるかどうかはログでは分かりませんが、

これまで、 PTS の更新で前のバージョンで Pass していた試験項目が

Pass しなくなることは頻発しています。

客先の質問は「PTS バージョンが異なるレポートの混在は可能か？」

ですので以下の回答を返信してください。

酒井ーーーー
AVRCP/TG/MCN/CB/[ID]
本件ですが、古いバージョンの PTS （ETS
version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

⇒ 古いバージョンでの Pass のご確認ありがとうございます。

PTS はこれまでも更新バージョンでそれまで Pass していた試験項目が

Pass しなくなることは少なからず発生していました。
TestReport_AVRCP_2025_11_04_20_57_51.zip： AVRCP/TG/MCN/CB/[ID]
の Evidence Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外の Evidence
Log
(ETS version [ID])

このようにテストレポート分割して Qualification を進めることは可能でしょうか？

⇒ はい、試験対象プロファイルが最新の PTS バージョンで Pass しない場合に一部試験項目を異なる PTS バージョンで実施して PTS レポートが複数ファイルになってもエビデンスとして有効で問題ございません。

代行登録作業を進ますのでお手数ですが添付の代行登録内容確認書にご記入の上ご提出をお願いします。

ーーーー差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 11 月 5 日 09:44

宛先 : Itsuo
Sakai

件名 :
【内部連絡】 FW: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

酒井さん望月です

ＳＯＮＹ様からツールの問題ではないかと質問がきておりますので、

ご確認いただけますでしょうか。

どうぞよろしくお願いいたします。

From:

Sent: Wednesday, November 5, 2025 9:40 AM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

AVRCP/TG/MCN/CB/[ID]

本件ですが、古いバージョンの PTS （ETS version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

TestReport_AVRCP_2025_11_04_20_57_51.zip： AVRCP/TG/MCN/CB/[ID] の Evidence
Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外の Evidence Log (ETS version [ID])

このようにテストレポート分割して Qualification を進めることは可能でしょうか？

それともすべてのテストを ETS version [ID] でパスさせる必要ありますか？

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 4:11 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ;
Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 続けて失礼いたします。 添付いただいた TestRepor から始まる . xml 形式の AVRCP ログは認証エビデンスに使えません。 お手数ですが認証用 PTS レポートは、単なるログではなく PTS で Generate
Report 機能により生成した「Report_AVRCP_2025」から始まる . xml Report ファイルをご提供ください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

続けて失礼いたします。

添付いただいた TestRepor から始まる .xml 形式の AVRCP ログは認証エビデンスに使えません。

お手数ですが認証用 PTS レポートは、単なるログではなく PTS で Generate Report

機能により生成した「Report_AVRCP_2025」から始まる .xml Report ファイルをご提供ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 3:55 PM

To: ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。
A2DP/SRC/SYN/[ID] が [ID] になっていますが、 Test Case Category

が D なので、不問ということで理解正しいでしょうか？
（A2DP はパスしたと考えてよいでしょうか？）

⇒そのご認識通りです。 A2DP が認証登録に必要な試験項目を完了したことを明確にお知らせしておりませんでした。申し訳ございません。
AVRCP の方は、 AVRCP/TG/MCN/CB/[ID] を残しすべて Pass したとのことです、

引き続き残った 1 件を進めています。

すべてパスしましたら、 Evidence log を提出します。

⇒ありがとうございます。お手数をお掛けしますが引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, November 4, 2025 3:36 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

すみません、一点確認させてください。

A2DP/SRC/SYN/[ID] が [ID] になっていますが、 Test Case Category が D なので、不問ということで理解正しいでしょうか？（A2DP はパスしたと考えてよいでしょうか？）

AVRCP の方は、 AVRCP/TG/MCN/CB/[ID] を残しすべて Pass したとのことです、引き続き残った 1 件を進めています。

すべてパスしましたら、 Evidence log を提出します。

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Friday, October 31, 2025 7:29 PM

To: 'Toshitaka Mochizuki' ; Yasui, Jun (SEC) ;
Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

ファイルありがとうございました、ダウンロードできました。

チップベンダーと相談します、火曜日に進め方再度相談させてください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 7:22 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ;
Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 大変お待たせいたしました。 ACRCP
全 Fail 項目の再試験した、テストログと測定結果纏め Excel 表をお送りいたします。 以下の Password にてダウンロードください。 ---------------------------------------- [ パスワード ] nn<VVk~5
[ パスワード有効期限 ] [ID] 19: 19
まで [ 送信 ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

大変お待たせいたしました。

ACRCP 全 Fail 項目の再試験した、テストログと測定結果纏め Excel 表をお送りいたします。

以下の Password にてダウンロードください。

[ パスワード ]

nn<VVk~5

[ パスワード有効期限 ]

[ID] 19:19
まで

[ 送信 ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 6:59 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

ファイルダウンロードできました、ありがとうございます。

本日終了時点でのリストの方もよろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 6:10 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ;
Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 Fail ログなどをオフィス宅ふぁいる便で再送いたしましたので、 お送りしたリンクで以下の Password にてダウンロードください。 ----------------------------------------
[ パスワード ] RWG. 7r{y [ パスワード有効期限 ] [ID] 18: 07
まで [ 送信 ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

Fail ログなどをオフィス宅ふぁいる便で再送いたしましたので、

お送りしたリンクで以下の Password にてダウンロードください。

[ パスワード ]

RWG.7r{y

[ パスワード有効期限 ]

[ID] 18:07
まで

[ 送信 ID]

ダウンロードできないようでしたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 5:14 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

申し訳ありません、添付ファイルが削除されてしまったようです。

下記拡張子のファイルが含まれると、削除されるとのこと。

&quot;386, &quot;3gr&quot;, &quot;add&quot;, &quot;ade&quot;, &quot;asp&quot;, &quot;bas&quot;, &quot;bat&quot;, &quot;chm&quot;, &quot;cmd&quot;, &quot;com&quot;, &quot;cpl&quot;, &quot;crt&quot;, &quot;dbx&quot;, &quot;dll&quot;, &quot;exe&quot;,

&quot;fon, &quot;hlp&quot;, &quot;hta&quot;, &quot;inf&quot;, &quot;ins&quot;, &quot;isp&quot;, &quot;js&quot;, &quot;jse&quot;, &quot;lnk&quot;, &quot;mdb&quot;, &quot;mde&quot;, &quot;msc&quot;, &quot;msi&quot;, &quot;msp&quot;, &quot;mst&quot;,

&quot;ocx, &quot;pcd&quot;, &quot;pif&quot;, &quot;reg&quot;, &quot;scr&quot;, &quot;sct&quot;, &quot;shs&quot;, &quot;shb&quot;, &quot;url&quot;, &quot;vb&quot;, &quot;vbe&quot;, &quot;vbs&quot;, &quot;vxd&quot;, &quot;wsc&quot;, &quot;wsf&quot;,

&quot;wsh,&quot;adp&quot;, &quot;ani&quot;, &quot;ht&quot;, &quot;job&quot;, &quot;mda&quot;, &quot;mdz&quot;, &quot;ws&quot;, &quot;ps1&quot;, &quot;ps1xml&quot;, &quot;ps2&quot;, &quot;ps2xml&quot;, &quot;psc1&quot;, &quot;psc2&quot;,

&quot;msh, &quot;msh1&quot;, &quot;msh2&quot;, &quot;mshxml&quot;, &quot;msh1xml&quot;, &quot;msh2xml&quot;, &quot;scf&quot;, &quot;class&quot;, &quot;jar&quot;, &quot;iqy&quot;, &quot;psm1&quot;, &quot;pssc&quot;

&quot;apk, &quot;app&quot;, &quot;appcontent-ms&quot;, &quot;appref-ms&quot;, &quot;appx&quot;, &quot;aspx&quot;, &quot;asx&quot;, &quot;cdxml&quot;, &quot;cer&quot;, &quot;cnt&quot;

&quot;csh, &quot;der&quot;, &quot;diagcab&quot;, &quot;fxp&quot;, &quot;gadget&quot;, &quot;grp&quot;, &quot;hpj&quot;, &quot;htc&quot;, &quot;its&quot;, &quot;jnlp&quot;, &quot;ksh&quot;, &quot;mad&quot;

&quot;maf, &quot;mag&quot;, &quot;mam&quot;, &quot;maq&quot;, &quot;mar&quot;, &quot;mas&quot;, &quot;mat&quot;, &quot;mau&quot;, &quot;mav&quot;, &quot;maw&quot;, &quot;mcf&quot;, &quot;mdt&quot;, &quot;mdw&quot;, &quot;mht&quot;

&quot;mhtml, &quot;msu&quot;, &quot;ops&quot;, &quot;pl&quot;, &quot;plg&quot;, &quot;prf&quot;, &quot;prg&quot;, &quot;printerexport&quot;, &quot;psd1&quot;, &quot;psdm1&quot;, &quot;pst&quot;, &quot;py&quot;, &quot;pyc&quot;

&quot;pyo, &quot;pyw&quot;, &quot;pyz&quot;, &quot;pyzw&quot;, &quot;settingcontent-ms&quot;, &quot;theme&quot;, &quot;tmp&quot;, &quot;udl&quot;, &quot;vbp&quot;, &quot;vhd&quot;, &quot;vhdx&quot;, &quot;vsmacros&quot;

&quot;vss, &quot;vst&quot;, &quot;vsw&quot;, &quot;webpnp&quot;, &quot;website&quot;, &quot;wsb&quot;, &quot;xbap&quot;, &quot;xll&quot;, &quot;xnk&quot;

ひとまず、本日の確認終わりましたら、エクセルでリスト頂けますでしょうか？

Evidence log 取得が終わっていないテストケースについて色付けしてリスト頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 4:24 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ;
Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 ご指定の方法で Google Play Music
にて音楽ファイルを再生できましたが、 Fail となっていた項目は依然として Pass
にはなっていません。 すべての Fail 項目への再確認はまた完了していないですが、 「The media player list does not contain a browsable player」または 「Failed to retrieve

An email has been sent to you which contained one or more attachments, some of which are not permitted for security reasons. Please contact your local helpdesk for advice on how to securely share files with external parties.

Attachment(s) deleted: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

Sender:

Date: [ID]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proofpoint により添付ファイルが削除されました。セキュリティ上の理由から許可されていない添付ファイルが 1 つ以上含まれている電子メールが送信されたためです。

削除された添付ファイル名 : 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

送信者 :

日付 : [ID]

外部の顧客と安全にファイルを共有する方法については、以下の URL をご参照ください。

< [URL] >

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

ご指定の方法で Google Play Music
にて音楽ファイルを再生できましたが、

Fail となっていた項目は依然として Pass にはなっていません。

すべての Fail
項目への再確認はまた完了していないですが、

「The media player list does not contain a browsable player」または

「Failed to retrieve Media Player List」

というエラーが発生したことにより、試験結果は [ID] または Fail
となっております。

取り急ぎ、再試験した項目のテストログ、スクリーンショット、および写真を添付いたしますので、ご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 4:18 PM

To: ; Itsuo Sakai ; Toshitaka Mochizuki
; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

本日安井より情報を入れさせて頂きましたが、これで少し評価進みましたでしょうか？

Fail など残りましたら、チップベンダーに Evidence log 取得の依頼をかけることも考えておりますので、本日終了時点で進捗状況お知らせ頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Friday, October 31, 2025 12:32 PM

To: Miyagawa, Yoichi (SEC) ; Itsuo Sakai ;
Toshitaka Mochizuki ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、チップベンダー様からの情報によると、テストでは Google Play Music を使用することが大事なように思われます。

以下、そちらの情報です。

I have shared the User Manuals for these failed test items with you via MTK FEX.

It also includes the required Google Music and MP3 files.

Please follow the SOP for each test item in the User Manual to conduct the tests.

Because most of these test items require the use of Google Music.

If you encounter any difficulties installing Google Music, please let me know.

I will check it tomorrow night. (As you know, I am currently attending military reservist training...)

Additionally, regarding AVRCP/TG/MPS/[ID], we do not have experience testing this item.

However, based on the information provided by the lab, it also requires the use of Google Music.

You can try the following steps to see if you can pass this test item:

1.
Install the Google Play Music app

2.
Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

3.
Play then pause the music in Google Play Music

4.
Make sure PTS and IUT are paired

5.
Run PTS to start the test case AVRCP/TG/MPS/[ID]

6.
PTS will pop up a message (&quot;Received Play Command, press Yes&quot;)

7.
If Google Play Music starts playing music, click &quot;Yes&quot;; if it does not start playing, click &quot;No&quot;.

弊社でもこちらのやり方を調査しておりまして、以下の部分を補足させていただきます。

・ Google Play Music のインストール方法

PC とテレビを adb
接続していただき、以前お送りした GoogleMusic.apk が入っているフォルダからコマンドプロンプトで

adb root

adb install GoogleMusic.apk

adb reboot

と打っていただくとインストールできます。

・ Google Play Music の開き方設定 → アプリ → アプリをすべて表示 → システムアプリの表示 →Google
Play Musuic

から開いていただくと、開けますその際サーバーエラーのような画面が出ますが、 OK を何度か押していただくとプレイリストの画面まで進むことができると思います。

その後、リモコンで上ボタンを押すと、画像左上の 3 本の線がある部分にカーソルが表示されますので、その状態であれば Google
Play Music を操作することが可能になるように思われます。

・ Goole Play Music に mp3 ファイルを入れる方法

Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

との記載がありますが、こちらでうまくいかない場合は

mp3 ファイルを USB メモリに入れていただき、テレビのもう一つの USB ポート (addb 接続している USB ポートの隣 ) に接続していただくと Google
Play Music 上でもプレイリストが表示されるように思われます。

弊社の方でも、こちらのやり方引き続き調査しますので、ひとまず「AVRCP_fail_case_UserManual.docx」をご参照の上、テストを進めていただけますでしょうか。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。 引き続きどうぞよろしくお願い申し上げます。

差出人 : Miyagawa,
Yoichi (SEC)

送信日時 : 2025 年 10 月 30 日 19:39

宛先 : Itsuo
Sakai ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

宮川です。

来週の御社側の状況理解しました。

状況に応じて対応方法検討します。

以上、よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 7:12 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ;
Toshitaka Mochizuki ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > >11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。 >
エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、 > そういうわけではない感じでしょうか？ ⇒望月から、 Bluetooth 専任エンジニアが試験できない間は別規格の認証試験担当にアサインされた Profile 試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
>11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。
エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、
そういうわけではない感じでしょうか？

⇒ 望月から、 Bluetooth 専任エンジニアが試験できない間は別規格の認証試験担当にアサインされた Profile 試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

したがって全く試験できない訳ではありませんが、残件を分担させていただけると心強いです。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 18:56

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

一点確認をさせてください。
11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、そういうわけではない感じでしょうか？

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 6:52 PM

To: Miyagawa, Yoichi (SEC) ; Yasui, Jun (SEC) ;
Toshitaka Mochizuki ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 本日望月が不在のため代わって返信させていただきます。 > A2DP/SRC/SUS/[ID]
ですが、今のテレビソフトは Suspend を発行しない >
ことが分かりました。 > A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付 >
にテストケース差し替えをお願いできますでしょうか？ ⇒ご連絡ありがとうございます。 A2DP ICS 1/8: NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。

A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ; Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １． AVRCP/TG/MCN/CB、 AVRCP/TG/MCN/NP など試験は、 [ID] または Fail となっています。
ログには “ The media player list does not contain a browsable player ” と表示されています。 DUT 本体上で media player list
が確認できず、 browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、 AVRCP/TG/MCN/NP など試験は、 [ID] または Fail となっています。

ログには “ The media player list does not contain a browsable player ” と表示されています。

DUT 本体上で media player list が確認できず、 browsable player
がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、 Step 7 「Open Google Play Music （YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS 画面に「Suspend the streaming channel」と表示され、 YouTube
Music を起動することができませんでした。

そのため、試験結果は [ID]
となりました。

なお、 Google Play Music はすでに YouTube Music
に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “ yuandeyixinren.mp3 ” を USB
メモリから再生した

➁ adb コマンドで persist.bluetooth.pts を True にした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、 MP3 音楽ファイルを再生してみましたが、結果は Fail
のままでした。添付の Screenshot をご参照ください。

Playing Changed 情報を PTS に伝える方法を教えてください。

５． AVRCP/TG/MPS/[ID]

試験中に“ Play Command をいただきましたが、 Yes を押す”とのメッセージが表示されますが、 Play Command への確認方法が不明です。

一応 Yes と押しても、 [ID] になりました。添付の Screenshot をご参照ください。

Play Command への確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらで Zip ファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便の URL をお送りいたしましたので、 前回同様、ファイルアップロード後、 Password をお送りください。
どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM
望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便の URL をお送りいたしましたので、

前回同様、ファイルアップロード後、 Password をお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui,
Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka
Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下 DUT の操作方法が分からない部分があり、 Pass にできませんでした。
まずは、以下の項目について DUT の操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]： Suspend the streaming channel (streaming channel をサスペンドする方法が不明 ) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下 DUT の操作方法が分からない部分があり、 Pass にできませんでした。

まずは、以下の項目について DUT の操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]： Suspend the streaming channel (streaming channel をサスペンドする方法が不明 )

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes 以上 media を再生方法がわからない )

添付の Screenshot をご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階 TEL: [ID]( 平日 18: 00 以降、または直通の場合は必ず内線番号 52250 を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階 TEL: [ID]( 平日 18: 00 以降、または直通の場合は必ず内線番号 52250 を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用 URL をお送りいたしましたので、
可能であればそちらにファイルをアップロードの上、 Password がオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用 URL をお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、 Password がオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３ G 程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui,
Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka
Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui,
Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka
Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階 TEL: [ID]( 平日 18: 00 以降、または直通の場合は必ず内線番号 52250 を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui,
Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験で ADB コマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。
ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM
望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験で ADB コマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
 ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
[ID] の方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。 * あるいは ** のついた項目は RF/RF PHY 試験のパラメータですので Profile 試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
 ; Itsuo Sakai ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka
Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa,
Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしました [ID] のご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。
どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM
望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしました [ID] のご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ; Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ; Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth 試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。 また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回 ADB などの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth 試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回 ADB などの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付の [ID] にも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、 11/4 ～ 11/7 にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9 申請の場合は 10/31 までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一の Fail 発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo
Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。

参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Tools は下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windows でadb 環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。 > 3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。 >
なお、テスト環境でもう一点確認があります。 > テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo
Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、 ICS とテストプラン作成しました。

3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge （adb） | Android Studio | Android Developers

Android SDK Platform-Tools をインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。 > TV の開発キットを送付しますが、映像出力が HDMI となっております。 > HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。 差出人 :
Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo
Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。

TV の開発キットを送付しますが、映像出力が HDMI となっております。

HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 >
添付ご確認ください。 > ICS Selection で、 CORE を変更する前の状態で Export してあります。 ⇒ありがとうございます。 この状態から (1)Layer Selection で HCI と UHCI を削除してください。
次に (2)ICS Selection で Core 階層を選択し、 12/1, 1/53, 2/53 を削除してください。 これで All ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo
Sakai ;
Masaya Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selection で、 CORE を変更する前の状態で Export してあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ; Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。 Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export
project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya
Iida

件名 : RE:
[RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度 Qualification Workspece 操作について教えてください。

Specified the Design で、それぞれ参照する DN を選択後、 ICS
Selection まで進むと、 CORE におきまして

Controller は Core v5.3 と v5.4

Host は Core v5.3 と v6.0

のふたつチェックが入っており、 Consistency Check が通らない状態になっています。

ここで CORE のチェックをさわると、色々な Layer が Unlock されてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
・ Option 2b でよかったでしょうか？ ⇒はい、 Option 2b で結構です。 >
・ TCRL Package version は TCRK pkg100
でよかったでしょうか？ ⇒はい、 pkg100 で結構です。 >
・ [ID]、 [ID]、 QDID: [ID] を include しましたが、下記設定画面で > Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1) プロファイル試験用の ICS を提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるための Qualification Workspece 操作をサポート頂きたく。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP
1.4、
AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。
A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

・ Option 2b でよかったでしょうか？

・ TCRL Package version は TCRK pkg100 でよかったでしょうか？

・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で

Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを ICS 修正画面で修正する）

上記以外の Host 関連は [ID] を選ぶ

Controller 以下はすべて [ID] を選ぶ → RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 >
サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒ (1) プロファイル試験用の ICS を提出いただくにあったって SIG ページの Specification サイトから実装された各プロファイルの ICS ファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspace を作成して実装された各プロファイルの ICS を入力して Export ISC ファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの ( 無改造 ) で結構です。

(2) RF および RF PHY 試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3) 登録時の WorkSpace への入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

[ID] へのご記入・ご提出をお願いします。

(4)
添付の「Invoice 取得手順 _ 自社送金」を参照して SIG へ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspace でのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 =
= = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID]
東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUT の送付は以下までお願いいたします。 〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUT の送付は以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行して DUT の準備を進めたく思っております。

DUT の送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = =
アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID] 東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階 Tel [ID]
内線 220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計 2 課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 >
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 > 11/9 までに登録完了で考えております。 >
（DN 購入の支払日は 10/31 予定です） >
この日程感で、 11/9 までに登録完了可能そうでしょうか？ ⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、 これまでの経験では Fail 項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、
11/9 までに登録完了で考えております。
（DN 購入の支払日は 10/31 予定です）
この日程感で、 11/9 までに登録完了可能そうでしょうか？

⇒ A2DP および AVRCP のプロファイル試験の結果次第ではありますが、

これまでの経験では Fail 項目の再試験、再々試験を加味しても約

3 週間で完了するのが一般的です。

この経験則からは 11/9 までに登録完了可能です。
大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、 10 月上旬に契約を締結、 10 月末までにテスト完了、 11/9 までに登録完了で考えております。

（DN 購入の支払日は 10/31 予定です）

この日程感で、 11/9 までに登録完了可能そうでしょうか？

大丈夫そうでしたら、 2025/11/9 までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ >
今回ホストは [ID] を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 >
となっております。 > 3 年前の QDID [ID] のときは > A2DP 1. 3. 2 > AVRCP 1. 5 >
としていました。 ⇒プロファイル (X2core) 部を QDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストは [ID] を参照で
A2DP 1.4
AVRCP 1.6.2
となっております。
3 年前の QDID [ID] のときは
A2DP 1.3.2
AVRCP 1.5
としていました。

⇒プロファイル (X2core) 部を QDID [ID] を参照した後、 ICS 修正で A2DP
1.4、

AVRCP 1.6.2 に変更すると、 ICS 更新に伴って A2DP と AVRCP のテスト要求が出力されます。

A2DP と AVRCP を PTS 試験を実施してテストレポートを取得し、アップロードすることで ICS 更新が可能かつ試験を最小限に抑えることが可能です。

11 月 9 までの登録では以下の見積です。

・プロファイル試験 (A2DP,AVRCP) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (A2DP,AVRCP,IOPT) ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストは [ID] を参照で

A2DP 1.4

AVRCP 1.6.2

となっております。

3 年前の QDID [ID] のときは

A2DP 1.3.2

AVRCP 1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 >
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を >
使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 >
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ > 前回と同じく台湾ですか？ ⇒今回の登録で [ID]、 [ID] および FY23 の QDID: [ID] を Include して A2DP などのソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

⇒ご理解いただきありがとうございます。
一点確認させてください。
今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？
前回と同じく台湾ですか？

⇒今回の登録で [ID]、 [ID] および FY23 の QDID:[ID] を Include して A2DP などのプロファイルを QDID:[ID] から ICS レベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。

もしプロファイルの ICS が FY23 の QDID:[ID] から追加サポート項目があるとこの方法は使えませんが FY26 で FY23 のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

さらに QPRDv4 から IOPT 試験が追加されて、 2025 年 11 月 10 発効で以下の試験が発生します。

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

公開日が 180 日先まで指定可能になったこともあり、サーバーへの登録を 11 月 9 日までに行えば、 RF/RF PHY およびプロファイル試験全てが免除されます。その場合の見積は以下の内容となります。

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

11 月 10 以降の登録では以下の見積となります。

・プロファイル試験 (IOPT) ￥ 200,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

( 他に申請者から SIG へ登録費のドル送金 )

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From:

Sent: Thursday, September 11, 2025 8:33 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験アリオン飯田様お世話になっております。

ソニー宮川です。

ご確認ありがとうございます、 [ID] 参照は色々問題があり、 Subset の [ID] を使った方がいい件、理解しました。

一点確認させてください。

今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？前回と同じく台湾ですか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Wednesday, September 10, 2025 9:43 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 見積依頼書をご送付いただきありがとうございます。 >
なお本件、 3 年前に御社に依頼した [ID] の、 OS バージョンアップによるリスティングとなります。 > https: //qualification. bluetooth. com/ListingDetails/[ID]
> 無線モジュールや RF 仕様の変更はないため、 [ID] の際作成した RF/RFPHY のテストレポートはソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG 認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 =
= = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒 [ID]
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

## 20. 2025-11-06 06:41

**From:** Itsuo Sakai
**To:** "" , Toshitaka Mochizuki , "" , Masaya Iida
**Attachments:** Review_Page.png

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

ご送付いただいたAVRCPレポート(ETS [ID])で問題ございません。

ご協力ありがとうございました。

9月30日にご送付いただきました SIG_Ama3.0_02.zip 内のExport Project

ファイルを読み込ませ、Consistency CheckでNo IDLを確認後、Test Plan

にPTSレポート結果を記入してUploadするとともに関連したTest Peportも

Upload後、Recipt Numberを選択してReviewページまで進んでSubmission

Statusの全項目が緑となることを確認しました。

代行登録内容確認書の内容と対比を行って合致していることを確認しましたが、念のため御社でも最終確認のうえ登録確定のご指示をお願いいたします。

並行してコンプライアンスフォルダ作成資料として登録過程で得られるドキュメント以外に下記製品資料が必要ですのでご準備をお願いします。

(1)製品の操作マニュアル(Bluetooth部分のみで結構です)

(2)製品のブロック図

(3)製品の外形図

(4)アンテナデータシート(放射利得特性図を含むもの)

以上、よろしくお願いいたします差出人:

送信日時: 2025年11月6日 15:35

宛先: Toshitaka Mochizuki ; ; Itsuo Sakai ; Masaya Iida

件名: RE: [RFQ][Allion様] FY26 [ID] Bluetooth SIG認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの宮川です。

昨晩お送りしたEvidence logでQualification進められそうでしょうか？

以上、よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Wednesday, November 5, 2025 9:47 PM

To: Toshitaka Mochizuki ; Yasui, Jun (SEC) ; Itsuo Sakai ; Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの宮川です。

添付ご確認頂けますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, November 5, 2025 6:18 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 以下補足となります。 Reportから始まる. xmlレポートファイルのみの更新で結構です。 したがって再試験でのlog取得は不要です。 ご説明が後になりまして申し訳ございません。 引き続きご対応どうぞよろしくお願い申し上げます。
ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

以下補足となります。

Reportから始まる.xmlレポートファイルのみの更新で結構です。

したがって再試験でのlog取得は不要です。

ご説明が後になりまして申し訳ございません。

引き続きご対応どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, November 5, 2025 5:54 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

至急確認します。
TestReport_AVRCP_2025_11_04_20_57_51.zip：AVRCP/TG/MCN/CB/[ID]CのEvidence
Log (ETS version [ID])

こちらの差し替えが必要と理解しましたが、間違っていましたらお知らせください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Wednesday, November 5, 2025 5:47 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 以下につきまして、明日までに至急ご対応いただけますでしょうか。 ★1項目実施のAVRCPレポートのICSで AVRCP Versionが1. 5となっています。PTSのICSを以下のようにVersion 1. 6. 2に変更してGenerate
Repoertしたレポートファイルの再送をお願いします。」 大変恐れ入りますが、ご対応どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

以下につきまして、明日までに至急ご対応いただけますでしょうか。

★1項目実施のAVRCPレポートのICSで　AVRCP Versionが1.5となっています。PTSのICSを以下のようにVersion 1.6.2に変更してGenerate

Repoertしたレポートファイルの再送をお願いします。」

大変恐れ入りますが、ご対応どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 5, 2025 12:23 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

今回の試験レポートについて補足ですが、

ご送付いただいたPTSレポートで認証登録を進めるとともにアリオン発行プロファルレポートのPass　ログとして参照させていただきますのでどうぞよろしくお願いします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 5, 2025 11:35 AM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

確認させていただきます。

試験レポートはでき次第お送りしますのでもうしばらくお待ちください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, November 5, 2025 11:23 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

添付ご確認ください。

基本、以前お送りしたbqwファイルで記載した情報と同じですが、公開日だけ5/1に変更しています。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Wednesday, November 5, 2025 10:15 AM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご確認いただきましてありがとうございます。 > AVRCP/TG/MCN/CB/[ID] > 本件ですが、古いバージョンのPTS（ETS version 11. 5. 0. 5）では > パスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。
⇒古いバージョンでのPassのご確認ありがとうございます。 PTSはこれまでも更新バージョンでそれまでPassしていた試験項目がソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご確認いただきましてありがとうございます。
AVRCP/TG/MCN/CB/[ID]
本件ですが、古いバージョンのPTS（ETS version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

⇒古いバージョンでのPassのご確認ありがとうございます。

PTSはこれまでも更新バージョンでそれまでPassしていた試験項目が

Passしなくなることは少なからず発生していました。
TestReport_AVRCP_2025_11_04_20_57_51.zip：AVRCP/TG/MCN/CB/[ID]
のEvidence Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外のEvidence Log
(ETS version [ID])

このようにテストレポート分割してQualificationを進めることは可能でしょうか？

⇒はい、試験対象プロファイルが最新のPTSバージョンでPassしない場合に一部試験項目を異なるPTSバージョンで実施してPTSレポートが複数ファイルになってもエビデンスとして有効で問題ございません。

代行登録作業を進めますのでお手数ですが添付の代行登録内容確認書にご記入の上ご提出をお願いします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, November 5, 2025 9:40 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

AVRCP/TG/MCN/CB/[ID]

本件ですが、古いバージョンのPTS（ETS version [ID]）ではパスしたため、ツールの問題ではないか？とチップベンダーから連絡が来ています。

TestReport_AVRCP_2025_11_04_20_57_51.zip：AVRCP/TG/MCN/CB/[ID]CのEvidence Log (ETS version [ID])

TestReport_AVRCP_2025_11_04_18_52_38.zip：上記以外のEvidence Log (ETS version [ID])

このようにテストレポート分割してQualificationを進めることは可能でしょうか？

それともすべてのテストを ETS version [ID]3でパスさせる必要ありますか？

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 4:11 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 続けて失礼いたします。 添付いただいたTestReporから始まる. xml形式のAVRCPログは認証エビデンスに使えません。 お手数ですが認証用PTSレポートは、単なるログではなくPTSでGenerate Report
機能により生成した「Report_AVRCP_2025」から始まる. xml Reportファイルをご提供ください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

続けて失礼いたします。

添付いただいたTestReporから始まる.xml形式のAVRCPログは認証エビデンスに使えません。

お手数ですが認証用PTSレポートは、単なるログではなくPTSでGenerate Report

機能により生成した「Report_AVRCP_2025」から始まる.xml Reportファイルをご提供ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 3:55 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。
A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case Category
がDなので、不問ということで理解正しいでしょうか？
（A2DPはパスしたと考えてよいでしょうか？）

⇒そのご認識通りです。A2DPが認証登録に必要な試験項目を完了したことを明確にお知らせしておりませんでした。申し訳ございません。
AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、
引き続き残った1件を進めています。
すべてパスしましたら、Evidence logを提出します。

⇒ありがとうございます。お手数をお掛けしますが引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, November 4, 2025 3:36 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

すみません、一点確認させてください。

A2DP/SRC/SYN/[ID]　が　[ID]　になっていますが、Test Case CategoryがDなので、不問ということで理解正しいでしょうか？（A2DPはパスしたと考えてよいでしょうか？）

AVRCPの方は、AVRCP/TG/MCN/CB/[ID]　を残しすべてPassしたとのことです、引き続き残った1件を進めています。

すべてパスしましたら、Evidence logを提出します。

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Friday, October 31, 2025 7:29 PM

To: 'Toshitaka Mochizuki' ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

宮川です。

ファイルありがとうございました、ダウンロードできました。

チップベンダーと相談します、火曜日に進め方再度相談させてください。

以上、よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 7:22 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 大変お待たせいたしました。 ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。 以下のPasswordにてダウンロードください。 ----------------------------------------
[パスワード] nn<VVk~5 [パスワード有効期限] [ID] 19: 19 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

大変お待たせいたしました。

ACRCP 全Fail項目の再試験した、テストログと測定結果纏めExcel表をお送りいたします。

以下のPasswordにてダウンロードください。

[パスワード]

nn<VVk~5

[パスワード有効期限]

[ID] 19:19 まで

[送信ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 6:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

ファイルダウンロードできました、ありがとうございます。

本日終了時点でのリストの方もよろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 6:10 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 Failログなどをオフィス宅ふぁいる便で再送いたしましたので、 お送りしたリンクで以下のPasswordにてダウンロードください。 ---------------------------------------- [パスワード]
RWG. 7r{y [パスワード有効期限] [ID] 18: 07 まで [送信ID] [ID] ----------------------------------------------------------

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

Failログなどをオフィス宅ふぁいる便で再送いたしましたので、

お送りしたリンクで以下のPasswordにてダウンロードください。

[パスワード]

RWG.7r{y

[パスワード有効期限]

[ID] 18:07 まで

[送信ID]

ダウンロードできないようでしたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 5:14 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

申し訳ありません、添付ファイルが削除されてしまったようです。

下記拡張子のファイルが含まれると、削除されるとのこと。

&quot;386, &quot;3gr&quot;, &quot;add&quot;, &quot;ade&quot;, &quot;asp&quot;, &quot;bas&quot;, &quot;bat&quot;, &quot;chm&quot;, &quot;cmd&quot;, &quot;com&quot;, &quot;cpl&quot;, &quot;crt&quot;, &quot;dbx&quot;, &quot;dll&quot;, &quot;exe&quot;,

&quot;fon, &quot;hlp&quot;, &quot;hta&quot;, &quot;inf&quot;, &quot;ins&quot;, &quot;isp&quot;, &quot;js&quot;, &quot;jse&quot;, &quot;lnk&quot;, &quot;mdb&quot;, &quot;mde&quot;, &quot;msc&quot;, &quot;msi&quot;, &quot;msp&quot;, &quot;mst&quot;,

&quot;ocx, &quot;pcd&quot;, &quot;pif&quot;, &quot;reg&quot;, &quot;scr&quot;, &quot;sct&quot;, &quot;shs&quot;, &quot;shb&quot;, &quot;url&quot;, &quot;vb&quot;, &quot;vbe&quot;, &quot;vbs&quot;, &quot;vxd&quot;, &quot;wsc&quot;, &quot;wsf&quot;,

&quot;wsh,&quot;adp&quot;, &quot;ani&quot;, &quot;ht&quot;, &quot;job&quot;, &quot;mda&quot;, &quot;mdz&quot;, &quot;ws&quot;, &quot;ps1&quot;, &quot;ps1xml&quot;, &quot;ps2&quot;, &quot;ps2xml&quot;, &quot;psc1&quot;, &quot;psc2&quot;,

&quot;msh, &quot;msh1&quot;, &quot;msh2&quot;, &quot;mshxml&quot;, &quot;msh1xml&quot;, &quot;msh2xml&quot;, &quot;scf&quot;, &quot;class&quot;, &quot;jar&quot;, &quot;iqy&quot;, &quot;psm1&quot;, &quot;pssc&quot;

&quot;apk, &quot;app&quot;, &quot;appcontent-ms&quot;, &quot;appref-ms&quot;, &quot;appx&quot;, &quot;aspx&quot;, &quot;asx&quot;, &quot;cdxml&quot;, &quot;cer&quot;, &quot;cnt&quot;

&quot;csh, &quot;der&quot;, &quot;diagcab&quot;, &quot;fxp&quot;, &quot;gadget&quot;, &quot;grp&quot;, &quot;hpj&quot;, &quot;htc&quot;, &quot;its&quot;, &quot;jnlp&quot;, &quot;ksh&quot;, &quot;mad&quot;

&quot;maf, &quot;mag&quot;, &quot;mam&quot;, &quot;maq&quot;, &quot;mar&quot;, &quot;mas&quot;, &quot;mat&quot;, &quot;mau&quot;, &quot;mav&quot;, &quot;maw&quot;, &quot;mcf&quot;, &quot;mdt&quot;, &quot;mdw&quot;, &quot;mht&quot;

&quot;mhtml, &quot;msu&quot;, &quot;ops&quot;, &quot;pl&quot;, &quot;plg&quot;, &quot;prf&quot;, &quot;prg&quot;, &quot;printerexport&quot;, &quot;psd1&quot;, &quot;psdm1&quot;, &quot;pst&quot;, &quot;py&quot;, &quot;pyc&quot;

&quot;pyo, &quot;pyw&quot;, &quot;pyz&quot;, &quot;pyzw&quot;, &quot;settingcontent-ms&quot;, &quot;theme&quot;, &quot;tmp&quot;, &quot;udl&quot;, &quot;vbp&quot;, &quot;vhd&quot;, &quot;vhdx&quot;, &quot;vsmacros&quot;

&quot;vss, &quot;vst&quot;, &quot;vsw&quot;, &quot;webpnp&quot;, &quot;website&quot;, &quot;wsb&quot;, &quot;xbap&quot;, &quot;xll&quot;, &quot;xnk&quot;

ひとまず、本日の確認終わりましたら、エクセルでリスト頂けますでしょうか？

Evidence log取得が終わっていないテストケースについて色付けしてリスト頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 4:24 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、 Fail となっていた項目は依然として Pass にはなっていません。 すべての Fail 項目への再確認はまた完了していないですが、
「The media player list does not contain a browsable player」または 「Failed to retrieve

An email has been sent to you which contained one or more attachments, some of which are not permitted for security reasons. Please contact your local helpdesk for advice on how to securely share
files with external parties.

Attachment(s) deleted: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

Sender:

Date: [ID]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proofpointにより添付ファイルが削除されました。セキュリティ上の理由から許可されていない添付ファイルが1つ以上含まれている電子メールが送信されたためです。

削除された添付ファイル名: 251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip,251031_avrcp_fail test items.zip

送信者:

日付: [ID]

外部の顧客と安全にファイルを共有する方法については、以下のURLをご参照ください。

< [URL] >

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

ご指定の方法で Google Play Music にて音楽ファイルを再生できましたが、

Fail となっていた項目は依然として Pass にはなっていません。

すべての Fail 項目への再確認はまた完了していないですが、

「The media player list does not contain a browsable player」または

「Failed to retrieve Media Player List」

というエラーが発生したことにより、試験結果は [ID] または Fail となっております。

取り急ぎ、再試験した項目のテストログ、スクリーンショット、および写真を添付いたしますので、ご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Friday, October 31, 2025 4:18 PM

To: ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

本日安井より情報を入れさせて頂きましたが、これで少し評価進みましたでしょうか？

Failなど残りましたら、チップベンダーにEvidence log取得の依頼をかけることも考えておりますので、本日終了時点で進捗状況お知らせ頂けると助かります。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Friday, October 31, 2025 12:32 PM

To: Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、チップベンダー様からの情報によると、テストでは Google Play Music を使用することが大事なように思われます。

以下、そちらの情報です。

I have shared the User Manuals for these failed test items with you via MTK FEX.

It also includes the required Google Music and MP3 files.

Please follow the SOP for each test item in the User Manual to conduct the tests.

Because most of these test items require the use of Google Music.

If you encounter any difficulties installing Google Music, please let me know.

I will check it tomorrow night. (As you know, I am currently attending military reservist training...)

Additionally, regarding AVRCP/TG/MPS/[ID], we do not have experience testing this item.

However, based on the information provided by the lab, it also requires the use of Google Music.

You can try the following steps to see if you can pass this test item:

1.
Install the Google Play Music app

2.
Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

3.
Play then pause the music in Google Play Music

4.
Make sure PTS and IUT are paired

5.
Run PTS to start the test case AVRCP/TG/MPS/[ID]

6.
PTS will pop up a message (&quot;Received Play Command, press Yes&quot;)

7.
If Google Play Music starts playing music, click &quot;Yes&quot;; if it does not start playing, click &quot;No&quot;.

弊社でもこちらのやり方を調査しておりまして、以下の部分を補足させていただきます。

・ Google Play Music のインストール方法

PC とテレビを adb
接続していただき、以前お送りした GoogleMusic.apk が入っているフォルダからコマンドプロンプトで

adb root

adb install GoogleMusic.apk

adb reboot

と打っていただくとインストールできます。

・ Google Play Music の開き方設定 → アプリ → アプリをすべて表示 → システムアプリの表示 →Google
Play Musuic

から開いていただくと、開けますその際サーバーエラーのような画面が出ますが、 OK を何度か押していただくとプレイリストの画面まで進むことができると思います。

その後、リモコンで上ボタンを押すと、画像左上の 3 本の線がある部分にカーソルが表示されますので、その状態であれば Google
Play Music を操作することが可能になるように思われます。

・ Goole Play Music に mp3 ファイルを入れる方法

Push some mp3 files to the sdcard/Music/ folder and then reboot the DUT

adb reboot

との記載がありますが、こちらでうまくいかない場合は

mp3 ファイルを USB メモリに入れていただき、テレビのもう一つの USB ポート (addb 接続している USB ポートの隣 ) に接続していただくと Google
Play Music 上でもプレイリストが表示されるように思われます。

弊社の方でも、こちらのやり方引き続き調査しますので、ひとまず「AVRCP_fail_case_UserManual.docx」をご参照の上、テストを進めていただけますでしょうか。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。 引き続きどうぞよろしくお願い申し上げます。

差出人 : Miyagawa, Yoichi (SEC)

送信日時 : 2025 年 10 月 30 日 19:39

宛先 : Itsuo Sakai ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

宮川です。

来週の御社側の状況理解しました。

状況に応じて対応方法検討します。

以上、よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 7:12 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > >11/9登録のためには11/5までにPassあるいはその目処が立たないと実現が困難です。 > エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、 > そういうわけではない感じでしょうか？ ⇒望月から、Bluetooth専任エンジニアが試験できない間は別規格の認証試験担当にアサインされたProfile試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
>11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。
エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、
そういうわけではない感じでしょうか？

⇒ 望月から、 Bluetooth 専任エンジニアが試験できない間は別規格の認証試験担当にアサインされた Profile 試験を経験したエンジニアをその本業の空いた時間にアサインする予定と聞いております。

したがって全く試験できない訳ではありませんが、残件を分担させていただけると心強いです。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 18:56

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

一点確認をさせてください。
11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。

エンジニア不在で来週御社でのテストが一切実施出来ないと思ったのですが、そういうわけではない感じでしょうか？

From: Itsuo Sakai

Sent: Thursday, October 30, 2025 6:52 PM

To: Miyagawa, Yoichi (SEC) ;
Yasui, Jun (SEC) ;
Toshitaka Mochizuki ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 本日望月が不在のため代わって返信させていただきます。 > A2DP/SRC/SUS/[ID] ですが、今のテレビソフトはSuspendを発行しない > ことが分かりました。 > A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付 >
にテストケース差し替えをお願いできますでしょうか？ ⇒ご連絡ありがとうございます。 A2DP ICS 1/8: NOに変更してA2DP/SRC/SUS/[ID]Cを試験対象外にいたします。

ソニー宮川様アリオンの酒井です。いつもお世話になっております。

本日望月が不在のため代わって返信させていただきます。
A2DP/SRC/SUS/[ID] ですが、今のテレビソフトは Suspend を発行しないことが分かりました。
A2DP 2/8 Initiate Suspend のチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

⇒ ご連絡ありがとうございます。

A2DP ICS 1/8:NO に変更して A2DP/SRC/SUS/[ID] を試験対象外にいたします。
他の案件につきましては、無線チップベンダーと確認中ですのでもう少々
お時間ください。

⇒ 承知しました。よろしくお願いいたします。
なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、
今週中にテストパスできない場合、 11/9 申請は厳しいでしょうか？
御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

⇒ ご推察の通り 11/9 登録のためには 11/5 までに Pass あるいはその目処が立たないと実現が困難です。非 Pass 項目の解析とともに再試験を御社で実施していただけると情報交換の時間ロスがなくなり、大変助かりますので是非御社での PTS 試験実施をお願いします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 30 日 17:55

宛先 : ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

A2DP/SRC/SUS/[ID]　ですが、今のテレビソフトはSuspendを発行しないことが分かりました。

A2DP 2/8 Initiate Suspendのチェックを外しましたので、お手数ですが添付にテストケース差し替えをお願いできますでしょうか？

他の案件につきましては、無線チップベンダーと確認中ですのでもう少々お時間ください。

なお、来週海外イベントなどのため御社エンジニアが不在とのことですが、今週中にテストパスできない場合、11/9申請は厳しいでしょうか？

御社が動けない場合、最悪来週こちらでエビデンスログを取得することも考えています。

以上、ご確認よろしくお願い致します。

From: Yasui, Jun (SEC)

Sent: Wednesday, October 29, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

ご連絡いただき、誠にありがとうございます。
また、プロファイル試験の測定結果に関しまして、詳細なご確認をいただき感謝申し上げます。

お問い合わせいただいた 5 つの確認事項につきまして、
内部で内容を確認いたしますので、恐れ入りますが今しばらくお待ちください。

試験の実施にあたり多大なお手数をお掛けしておりますこと、
また、「A2DP_AVRCP_fail_case_UserManual.docx」に関しまして分かりにくい点があり、ご不便をおかけいたしましたこと、深くお詫び申し上げます。
こちらでもう少し丁寧に内容をまとめてお送りするべきであったと反省しております。

大変恐縮ではございますが、取り急ぎご連絡とさせていただきます。
引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 29 日 14:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 プロファイル試験の測定結果について、いくつかの確認事項があります。 １．AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。 ログには “The media player list does not
contain a browsable player” と表示されています。 DUT本体上で media player list が確認できず、browsable

ソニー安井様いつもお世話になっております。

アリオンの望月です。

プロファイル試験の測定結果について、いくつかの確認事項があります。

AVRCP/TG/MCN/CB、AVRCP/TG/MCN/NPなど試験は、INDCSVまたはFailとなっています。

ログには “The media player list does not contain a browsable player” と表示されています。

DUT本体上で media player list が確認できず、browsable player がどのように media player list に含まれるのかも分かりません。

2. A2DP/SRC/SUS/[ID]

頂いた測定手順に従い、Step 7「Open Google Play Music（YouTube Music）」を実施しようとしました。

しかし、リモコンのホームボタンを押して「設定 → APP → YouTube Music」を選択しようとすると、

PTS画面に「Suspend the streaming channel」と表示され、YouTube Musicを起動することができませんでした。

そのため、試験結果は [ID] となりました。

なお、Google Play Music はすでに YouTube Music に引き継がれているため、頂いた測定手順は古い内容となっています。

3. AVRCP/TG/RCR/[ID], AVRCP/TG/RCR/[ID]

下記の測定手順に従って試験を実施した結果、「Received incorrect Packet Type」 または 「Received incorrect PDU ID」 が発生しました。

① 指定のメタデータ “yuandeyixinren.mp3” を USB メモリから再生した

➁ adbコマンドでpersist.bluetooth.ptsをTrueにした

4. AVRCP/TG/MCN/NP/[ID]

試験中に「Update database by sending a valid Now Playing Changed Notification to the PTS」というメッセージが表示されましたが、

実施方法が不明でした。

念のため、MP3音楽ファイルを再生してみましたが、結果は Fail のままでした。添付のScreenshotをご参照ください。

Playing Changed情報をPTSに伝える方法を教えてください。

５．AVRCP/TG/MPS/[ID]

試験中に“Play Commandをいただきましたが、Yesを押す”とのメッセージが表示されますが、Play Commandへの確認方法が不明です。

一応Yesと押しても、INDCSVになりました。添付のScreenshotをご参照ください。

Play Commandへの確認方法を教えていただけますでしょうか。

以上取り急ぎご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 28, 2025 2:31 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

こちらでZipファイルを受け取りました。

確認いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 2:15 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「オフィス宅ふぁいる便」をご準備いただき、誠にありがとうございました。

ご案内いただいた「オフィス宅ふぁいる便」にて、下記のデータをお送りしました。

・ A2DP_AVRCP_fail_case_UserManual.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

dQ5eB5((

[ パスワード有効期限 ]

[ID] 14:11
まで

[ アップロード ID]

4d5b61bb-fdfa-4221-855c-58b174aed569

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 28 日 14:05

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 早速のご対応ありがとうございます。 オフィス宅ふぁいる便のURLをお送りいたしましたので、 前回同様、ファイルアップロード後、Passwordをお送りください。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC

ソニー安井様いつもお世話になっております。

アリオンの望月です。

早速のご対応ありがとうございます。

オフィス宅ふぁいる便のURLをお送りいたしましたので、

前回同様、ファイルアップロード後、Passwordをお送りください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 28, 2025 1:53 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

お待たせいたしまして、大変申し訳ございません。

ご依頼いただいておりました下記 2 項目のテストにつきまして、手順書「A2DP_AVRCP_fail_case_UserManual.docx」を本メールに添付いたしました。

・ A2DP/SRC/SUS/[ID] ・ AVRCP/TG/RCR/[ID]

お手数をおかけいたしますが、添付の手順書をご参照の上、テストを進めていただけますでしょうか。

なお、上記テストの実施に必要となります下記ファイルにつきましては、別途送付させていただきたく存じます。

・ Google Play Music
アプリ・音声ファイル「yuandeyixinren.mp3」

上記 2 点は「A2DP_AVRCP_fail_case_UserManual.zip」という Zip ファイルに格納しておりますが、以前お送りした「PTS_AvrcpTest_true.zip」等と同様にファイル容量が大きく、メールに添付することができません。

弊社都合で大変恐縮ではございますが、以前と同様に「オフィス宅ファイル便」にて「A2DP_AVRCP_fail_case_UserManual.zip」をアップロードさせていただきたく、ご準備いただくことは可能でしょうか。

ご多忙のところお手数をおかけいたしますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 28 日 10:16

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

ご連絡、大変誠にありがとうございます。

現在、内部で確認中でございますので、恐れ入りますが今しばらくお待ちください。

大変恐縮ですが、よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 27 日 18:24

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様宮川様いつもお世話になっております。 アリオンの望月です。 試験についていくつか不明点がございますのでご回答いただけますでしょうか。 以下DUTの操作方法が分からない部分があり、Passにできませんでした。 まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。 l A2DP/SRC/SUS/[ID]：Suspend
the streaming channel (streaming channelをサスペンドする方法が不明) l AVRCP/TG/RCR/[ID]:

ソニー安井様宮川様いつもお世話になっております。

アリオンの望月です。

試験についていくつか不明点がございますのでご回答いただけますでしょうか。

以下DUTの操作方法が分からない部分があり、Passにできませんでした。

まずは、以下の項目についてDUTの操作方法をご教示いただけますでしょうか。

A2DP/SRC/SUS/[ID]：Suspend the streaming channel (streaming channelをサスペンドする方法が不明)

AVRCP/TG/RCR/[ID]: Play with 512 bytes worth of metadata (512 bytes以上 mediaを再生方法がわからない)

添付のScreenshotをご参照ください。

ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 2:06 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニーの安井です。

状況のご連絡、大変誠にありがとうございます。

また、試験を開始したところのこと、感謝申し上げます。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 23 日 13:33

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご連絡有難うございます。 サンプルの動作確認ができましたので、現在試験を開始したところです。 試験中何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

サンプルの動作確認ができましたので、現在試験を開始したところです。

試験中何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 23, 2025 1:09 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。
ソニーの安井です。

ファイルご確認のご連絡、誠にありがとうございます。

ファイルを送付した直後で大変恐縮ではございますが、認証テストはすでに開始されておりますでしょうか？

アリオン様のご状況を、ご確認させていただきたかった次第です。

お忙しいところ申し訳ございませんが、引き続きどうぞよろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 21 日 11:27

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 ファイル受け取りました。 引き続き何かございましたら連絡いたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

ファイル受け取りました。

引き続き何かございましたら連絡いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 8:13 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

現在試験は開始可能な状態とのこと、承知いたしました。

また、この度は「オフィス宅ファイル便」をご準備いただき、誠にありがとうございました。

データの送付方法について苦慮しておりましたので、大変助かりました。

ご案内いただいた「オフィス宅ファイル便」にて、下記 2 点のデータをお送りしました。

・ PTS_AvrcpTest_true.zip

・ PTS_AvrcpTest_false.zip

ダウンロード用の URL は別途、望月様宛にメールが届いているかと存じます。私の方からファイルを開くためのパスワードなど送付します。

[ パスワード ]

F8U;mB_n

[ パスワード有効期限 ]

[ID] 20:02
まで

[ アップロード ID]

[ID]c63f-4f53-9104-ef50eec0465e

[ 送信 ID]

大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 20 日 18:04

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、 到着待ちとなっております。 当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、 可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。 こちらでダウンロードいたします。

ソニー安井様いつもお世話になっております。

アリオンの望月です。

現在試験は開始可能な状態となりましたが、試験用のファイルがまだいただけていないようですので、

到着待ちとなっております。

当社で使用しているオフィス宅ファイル便のファイルアップロード用URLをお送りいたしましたので、

可能であればそちらにファイルをアップロードの上、Passwordがオフィス宅ファイル便から送られてきますのでそちらを私までメールでお知らせいただけますでしょうか。

こちらでダウンロードいたします。

サイズは３G程度まで送ることが可能です。

ご検討どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 2:15 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

手順書のご送付ありがとうございます。

試験開始日程についてエンジニアと確認の上お返事いたしますのでしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Monday, October 20, 2025 2:11 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

本日の 12 時 55 分にこちらと同じ内容のメールをお送りいたしましたが、「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」の添付が原因で、望月様含め、すべての方に届いていない可能性が非常に高い状況です。 13 時 05 分にお送りしましたメールは、上記のメールが送達されているものと思い、お送りしておりました。混乱を招いておりましたら申し訳ございません。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 AVRCP/TG/NFY/[ID] のテストの際に必要となるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」につきましては、前述の通り、メールに添付すると送達できない問題がございました。現在、別途共有方法を検討中ですので、恐れ入りますが今しばらくお待ちください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

メールの送受信トラブルによりご迷惑をおかけし、大変恐縮ではございますが、何卒よろしくお願い申し上げます。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 13:05

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」が容量が大きいため、正しく添付できておりませんでした。

大変申し訳ございません。

送付の仕方、確認の上再送しますので、今しばらくお待ちいただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Yasui, Jun (SEC)

送信日時 : 2025 年 10 月 20 日 12:55

宛先 : Toshitaka Mochizuki ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : Re: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

お待たせして大変申し訳ございません。

ADB コマンドでの操作手順に関する資料を準備いたしました。こちら操作方法に関する資料「adb 操作方法 _ アリオン様向け .pdf」を添付にて送付いたします。

また、 adb 操作の際に必要になるファイル「PTS_AvrcpTest_true.zip」と「PTS_AvrcpTest_false.zip」を添付にて送付いたします。

もしご不明な点がございましたら、お気軽にお問い合わせください。

また一点、ご確認させていただきたいのですが、テスト開始日は、いつ頃をご予定されておりますでしょうか。差し支えなければ、目安をご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 18:49

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 ご対応ありがとうございます。 内容確認させていただきます。 試験サンプルは本日到着しております。 引き続きどうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階 TEL: [ID](平日18: 00以降、または直通の場合は必ず内線番号52250を入れてください。）

ソニー安井様いつもお世話になっております。

アリオンの望月です。

ご対応ありがとうございます。

内容確認させていただきます。

試験サンプルは本日到着しております。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Thursday, October 16, 2025 6:39 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井です。

[ID] の記入方法につきまして、ご丁寧にご教授いただき大変誠にありがとうございます。ご案内に沿って作成いたしました「[ID]( ソニー TV).doc」を添付にてお送りいたします。
ご査収のほど、よろしくお願い申し上げます。

あわせて、パネルレステレビのセットアップ方法に関する資料「テレビセットアップ方法 _ アリオン様向け .pdf」も添付いたしました。
セットアップの際に、もしご不明な点がございましたら、お気軽にお問い合わせください。

なお、 ADB コマンドでの操作手順につきましては、現在資料を準備しております。
完成次第、改めてお送りいたしますので、今しばらくお待ちいただけますと幸いです。

私どもの認識では、 AVRCP 以外のテスト項目につきましては、 ADB コマンドでの操作は不要で、リモコン操作にて実施可能かと存じます。
つきましては、大変恐縮ではございますが、先行してリモコン操作で可能な項目からテストを進めていただくことは可能でしょうか。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 11:29

宛先 : Yasui, Jun (SEC) ;
Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。 アリオンの望月です。 今回試験でADBコマンドでの操作が必要とのことでしたが、 製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階ソニー安井様いつもお世話になっております。

アリオンの望月です。

今回試験でADBコマンドでの操作が必要とのことでしたが、

製品操作のための接続、コマンドの入力、操作手順書を併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 5:16 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー安井様いつもお世話になっております。

アリオンの望月です。
QUESTIONNAIRSの方もご案内ありがとうございます。ご提出に先立ち、
一点確認させてください。
「Test Parameter of Device Under Test」の項目について、今回は
RF関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

⇒ご認識の通りです。*あるいは**のついた項目はRF/RF PHY試験のパラメータですのでProfile試験ではご記入不要です。それ以外の部分にご記入ください。

以上、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Wednesday, October 15, 2025 4:16 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっておりますソニーの安井と申します。

本日、望月様宛に DUT および関連機材一式を発送いたしました。

明日のご到着予定です。

送付いたしました機材の詳細は、添付の「[ID]
評価機材提出票及びチェックリスト _( ソニー TV).xlsx」にてご確認いただけますと幸いです。

また先日、飯田様よりご案内いただきました代行登録内容確認書につきましても、必要事項を記入した「代行登録内容確認書 _( ソニー TV).doc」を添付にてお送りいたします。

なお、公開日が 180 日先まで指定可能となったとの認識ですので、登録の表示開始日は 2026 年 4 月 1 日とさせていただいております。

[ID] の方もご案内ありがとうございます。ご提出に先立ち、一点確認させてください。

「Test Parameter of Device Under Test」の項目について、今回は RF 関連の試験は実施しないと認識しておりますが、本項目の記載は必要でしょうか。

お手数ではございますが、ご教示いただけますと幸いです。

大変恐縮ですがよろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 14 日 16:55

宛先 : Miyagawa, Yoichi (SEC) ;
Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月です。 立て続けで申し訳ございません。 先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。 こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。 どうぞよろしくお願い申し上げます。 ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω
アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

先週末にお送りいたしましたQUESTIONNAIRSのご記入の方いかがでしょうか。

こちら試験レポートに使用いたしますので、ご送付の方お願いいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 3:17 PM

To: ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

承知いたしました。

ご確定いただきましたらお知らせください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From:

Sent: Tuesday, October 14, 2025 2:34 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン望月様お世話になっております。

ソニー宮川です。

サンプル発送につきましては、弊社安井より準備出来次第連絡させて頂きます。

予定通り、明日には送り出せると思います、もう少々お時間ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 6:27 PM

To: Itsuo Sakai ;
Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの望月と申します。 横から失礼いたします。 Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。 ★サンプルのご発送準備有難うございます。 ご発送先は本メールの下にございますフッタの私望月宛にお送りください。 もしサイズが大きい物でしたらあらかじめお知らせください。
また、添付の評価機材提出票へのご記入、送付をお願いいたします。 ★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

ソニー宮川様いつもお世話になっております。

アリオンの望月と申します。

横から失礼いたします。

Bluetooth試験の実際の試験につきましては私の方からご案内させていただきます。

★サンプルのご発送準備有難うございます。

ご発送先は本メールの下にございますフッタの私望月宛にお送りください。

もしサイズが大きい物でしたらあらかじめお知らせください。

また、添付の評価機材提出票へのご記入、送付をお願いいたします。

★今回ADBなどの使用が必要とでしたら試験に必要な操作説明書もご提供お願いいたします。

★ドキュメント作成にも使用いたしますので添付のQUESTIONNAIRSにも必要事項ご記入の上ご返送ください。

★試験日程なのですが、こちらの都合で大変申し訳ございませんが、11/4～11/7にかけて、

海外イベントなどのためエンジニアが不在となってしまいます。

11/9申請の場合は10/31までにはレポートが出来ている必要があるかと存じます。

試験項目は少なめですが、万が一のFail発生時に備え、早めにサンプルの方お送りいただけますと助かります。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Friday, October 10, 2025 1:02 PM

To: ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのに ADB インストール PC が必要となります。
参考までに、添付メールの通り、 3 年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

⇒ ADB インストール PC の使途が理解できました。設定変更であれば

PTS 試験に対して問題ございません。

試験実施時には設定変更の手順書と必要であれば設定ファイルもご準備ください。
Android SDK Platform-Tools は下記サイトからダウンロードできます。
SDK Platform-Tools
リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。
Windows で adb 環境を構築する

⇒ ADB のダウンロードおよび構築情報ご提供ありがとうございます。

問題なく対応できると思います。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 10 日 11:33

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。
確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

はい、製品そのもので実施ですが、一部テストで製品の設定を変更するのにADBインストールPCが必要となります。

参考までに、添付メールの通り、3年前台湾でプロファイル試験を実施頂いた際も同じお願いをさせて頂いております。

Android SDK Platform-Toolsは下記サイトからダウンロードできます。

SDK
Platform-Tools リリースノート | Android Studio | Android Developers

なお、一般のサイトではありますが、環境構築にあたりこちら参考にしてみてください。

Windowsでadb環境を構築する以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Thursday, October 9, 2025 7:29 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > ご教示頂いた操作方法で、ICSとテストプラン作成しました。 > 3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。 ⇒ご対応ありがとうございます。これで当方でのプロファイル試験のTest Planが作成できます。 > なお、テスト環境でもう一点確認があります。 >
テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
ご教示頂いた操作方法で、 ICS とテストプラン作成しました。
3 年前の RF/RFPHY のレポート含めて一式送付しますのでご確認ください。

⇒ ご対応ありがとうございます。これで当方でのプロファイル試験の Test Plan が作成できます。
なお、テスト環境でもう一点確認があります。
テストを進めるにあたり、 DUT を制御するのに ADB 環境が必要なのですが、準備可能でしょうか？
Android Debug Bridge （adb） |
Android Studio | Android Developers
Android SDK Platform-Tools をインストール頂く形になります。

⇒ Bluetooth ラボ備え付けの PC がありますのでダウンロード URL などをご教示いただければインストールは可能です。

確認ですが、原則プロファイル試験は製品そのものので実施する規定となっておりますが、プロファイル試験で ADB インストール PC が必要でしょうか。 ( 今回は RF/RF
PHY 試験は対象外です。 )

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 9 日 19:12

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

ご教示頂いた操作方法で、ICSとテストプラン作成しました。

3年前のRF/RFPHYのレポート含めて一式送付しますのでご確認ください。

なお、テスト環境でもう一点確認があります。

テストを進めるにあたり、DUTを制御するのにADB環境が必要なのですが、準備可能でしょうか？

Android
Debug Bridge（adb） | Android Studio | Android Developers

Android SDK Platform-Toolsをインストール頂く形になります。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 6:22 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。 > TVの開発キットを送付しますが、映像出力がHDMIとなっております。 > HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？ ⇒はい、当方で準備いたします。 以上よろしくお願いいたします。
差出人: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
なお、 DUT ですが、来週火曜か水曜には発送できるよう準備を進めています。
TV の開発キットを送付しますが、映像出力が HDMI となっております。
HDMI ケーブルとモニターは御社でご準備頂くことは可能ですか？

⇒ はい、当方で準備いたします。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 18:18

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

操作方法ご教示頂きありがとうございます、試してみます。

なお、DUTですが、来週火曜か水曜には発送できるよう準備を進めています。

TVの開発キットを送付しますが、映像出力がHDMIとなっております。

HDMIケーブルとモニターは御社でご準備頂くことは可能ですか？

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 2:33 PM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンの酒井です。いつもお世話になっております。 > 添付ご確認ください。 > ICS Selectionで、COREを変更する前の状態でExportしてあります。 ⇒ありがとうございます。 この状態から(1)Layer SelectionでHCIとUHCIを削除してください。 次に(2)ICS SelectionでCore階層を選択し、12/1,
1/53, 2/53を削除してください。 これでAll ICS inconsistencies are

ソニー宮川様アリオンの酒井です。いつもお世話になっております。
添付ご確認ください。
ICS Selection で、 CORE を変更する前の状態で Export してあります。

⇒ ありがとうございます。

この状態から (1)Layer Selection で HCI と UHCI を削除してください。

次に (2)ICS Selection で Core 階層を選択し、 12/1,
1/53, 2/53 を削除してください。

これで All ICS inconsistencies are resolved 状態になりますので

A2DP, AVRCP の ICS を変更して Concyctency
Check で No Invalid を確認後に Test Plan and Declaration ページに進んで [Download
Test Plan]

アイコンをクリックして Test Plan を取得してください。

なお、 QDID:[ID] から RF,
RF PHY 階層を踏襲しても Test Plan には試験項目が出力されますので QDID:[ID] 登録時の RF/RF
PHY レポートをご準備ください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 8 日 10:11

宛先 : Itsuo Sakai ;
Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン酒井様お世話になっております。

ソニー宮川です。

添付ご確認ください。

ICS Selectionで、COREを変更する前の状態でExportしてあります。

こちらでも色々試してみます。

以上、ご確認よろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, October 8, 2025 8:47 AM

To: Miyagawa, Yoichi (SEC) ;
Masaya Iida

Subject: Re: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様アリオンのBTロゴ認証担当の酒井です。いつもお世話になっております。 Invalidの解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点でExport projectファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。 なお、当方のメールシステムがExport
projectファイル形式を配信しませんのでzipファイル化して添付してください。 以上よろしくお願いいたします。

ソニー宮川様アリオンの BT ロゴ認証担当の酒井です。いつもお世話になっております。

Invalid の解消はケースバイケースでメールでのやり取りでは時間が掛かってしまいますので、現時点で Export project ファイルを取得して私に送付てください。トライアンドエラーで解決策を見つけて解消手順をお知らせします。

なお、当方のメールシステムが Export project ファイル形式を配信しませんので zip ファイル化して添付してください。

以上よろしくお願いいたします。

差出人 :

送信日時 : 2025 年 10 月 7 日 21:04

宛先 : Masaya Iida

件名 : RE: [RFQ][Allion 様 ]
FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

情報ありがとうございます。

ご教示頂いた通り進めたのですが、再度Qualification Workspece操作について教えてください。

Specified the Designで、それぞれ参照するDNを選択後、ICS Selectionまで進むと、COREにおきまして

ControllerはCore v5.3とv5.4

HostはCore v5.3とv6.0

のふたつチェックが入っており、Consistency Checkが通らない状態になっています。

ここでCOREのチェックをさわると、色々なLayerがUnlockされてしまうのですが、何か回避方法ご存じないでしょうか？

From: Masaya Iida

Sent: Tuesday, October 7, 2025 5:44 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ・Option 2b でよかったでしょうか？ ⇒はい、Option 2bで結構です。 > ・TCRL Package versionはTCRK pkg100 でよかったでしょうか？ ⇒はい、pkg100で結構です。 > ・[ID]、[ID]、QDID: 199247をincludeしましたが、下記設定画面で >
Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
・ Option 2b でよかったでしょうか？

⇒ はい、 Option
2b で結構です。
・ TCRL Package version は TCRK
pkg100 でよかったでしょうか？

⇒ はい、 pkg100 で結構です。
・ [ID]、 [ID]、 QDID:[ID] を include しましたが、下記設定画面で
Profile 関連はすべて [ID] を選ぶ（その後 A2DP と AVRCP はバージョンを
ICS 修正画面で修正する）

⇒ そのとおりです。
上記以外の Host 関連は [ID] を選ぶ

⇒ そのとおりです。
Controller 以下はすべて [ID] を選ぶ
→RF/[ID] レポート流用のため、 RF/[ID] は [ID] 参照の方がいいなどありましたらご教示ください

⇒ RF/[ID] は [ID] を選択し、他の階層は [ID] を選択してください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 8:10 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
(1)プロファイル試験用のICSを提出にあたり質問をさせてください。

以前、下記ご提案を頂きましたが、具体的にご提案通り進めるためのQualification Workspece操作をサポート頂きたく。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、
AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。
A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

・Option 2b　でよかったでしょうか？

・TCRL Package versionはTCRK pkg100　でよかったでしょうか？

・[ID]、[ID]、QDID:199247をincludeしましたが、下記設定画面で

Profile関連はすべて 199247を選ぶ（その後A2DPとAVRCPはバージョンをICS修正画面で修正する）

上記以外のHost関連は Q346069を選ぶ

Controller以下はすべてQ333791を選ぶ →RF/RF_PHYレポート流用のため、RF/RF_PHYは199247参照の方がいいなどありましたらご教示くださいでご提案の通りの設定にできますでしょうか？

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Monday, October 6, 2025 1:53 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご案内いたします。 > サンプル提出は確認中ですが、並行して確認させてください。 > Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？ ⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご案内いたします。
サンプル提出は確認中ですが、並行して確認させてください。
Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

⇒(1)プロファイル試験用のICSを提出いただくにあったってSIGページのSpecificationサイトから実装された各プロファイルのICSファイルにサポート項目をチェックマークや○を追記して提出するか、

Qualification Workspaceを作成して実装された各プロファイルのICSを入力してExport ISCファイルを取得してご提出願います。なおプロファイル試験用サンプルは製品そのもの(無改造)で結構です。

(2) RFおよびRF PHY試験サンプルは添付の改造メモおよびチップセットベンダの認証テストサンプルに関する参考資料に従って試験用改造サンプルをご準備ください。

(3)登録時のWorkSpaceへの入力は見積依頼書および代行登録内容確認書の内容に従って当方で入力します。本体およびリモコンの代行登録内容確認書および

QUESTIONAIRSへのご記入・ご提出をお願いします。

(4) 添付の「Invoice取得手順_自社送金」を参照してSIGへ登録費のドル送金を登録完了ご希望日までに進めてください。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Monday, October 6, 2025 12:15 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

サンプル提出は確認中ですが、並行して確認させてください。

Qualification Workspaceでのテストケース作成はどのような段取りで進めればよいでしょうか？

From: Miyagawa, Yoichi (SEC)

Sent: Monday, October 6, 2025 9:47 AM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。
試験のスロット調整を行いますので、
サンプル提出予定日をご提示いただけますと幸いです。

内部で確認しますので、少々お時間下さい。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Friday, October 3, 2025 5:13 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご注文をいただきまして誠にありがとうございました。 クラウドサインが完了いたしました。 ご注文を承ります。 試験のスロット調整を行いますので、 サンプル提出予定日をご提示いただけますと幸いです。 以上、よろしくお願いいたします。 = = = = = = =
= = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご注文をいただきまして誠にありがとうございました。

クラウドサインが完了いたしました。

ご注文を承ります。

試験のスロット調整を行いますので、

サンプル提出予定日をご提示いただけますと幸いです。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, October 2, 2025 1:55 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

体制表送付ありがとうございます。

弊社側「タスクを依頼する発注者」の記載が間違っていたので添付のようにリバイスしました、ご確認ください。

別で進めている注文書ドラフトの確認が終わりましたら決裁進めます、引き続きよろしくお願い致します。

From: Masaya Iida

Sent: Thursday, October 2, 2025 11:15 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 体制表ですが、当社部分を更新いたしました。 添付いたします。 DUTの送付は以下までお願いいたします。 〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月 Tel [ID]
以上、よろしくお願いいたします。 アリオン株式会社飯田 From: Yoichi. Miyagawa@ sony. com <Yoichi. Miyagawa@ sony. com>

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

体制表ですが、当社部分を更新いたしました。

添付いたします。

DUTの送付は以下までお願いいたします。

〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階アリオン株式会社品川テストセンター営業統括部望月以上、よろしくお願いいたします。

アリオン株式会社飯田

From:

Sent: Wednesday, October 1, 2025 11:58 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

決裁前の事前承認通りました。

契約締結に進めさせて頂きたく、まずは添付体制表の御社の部分の更新をお願いできますでしょうか？

また、スムーズなテスト開始に向け、並行してDUTの準備を進めたく思っております。

DUTの送付先をご教示頂けますでしょうか？

以上、ご確認よろしくお願い致します。

From: Miyagawa, Yoichi (SEC)

Sent: Thursday, September 25, 2025 8:08 PM

To: 'Masaya Iida'

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

見積書修正ありがとうございました。

来週水曜に審議予定です、少々お時間ください。

以上、よろしくお願い致します。

From: Masaya Iida

Sent: Thursday, September 25, 2025 1:39 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 部門名の件、修正いたしました。 添付いたします。 ご検討のほどよろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel
[ID] 内線220 Mobile: [ID] FAX [ID] = = = = = =

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

部門名の件、修正いたしました。

添付いたします。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Thursday, September 25, 2025 11:42 AM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

宮川です。

情報足らずで大変申し訳ありません。

見積書へ記載の“部門”なのですが、下記で再度見積書作成お願いしても大丈夫でしょうか？

技術センター無線通信システム技術部門無線設計部無線設計2課

From: Masaya Iida

Sent: Thursday, September 25, 2025 11:34 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 ご連絡ありがとうございます。 > ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、 > 11/9までに登録完了で考えております。 > （DN購入の支払日は10/31予定です） > この日程感で、11/9までに登録完了可能そうでしょうか？
⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、 これまでの経験ではFail項目の再試験、再々試験を加味しても約ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

ご連絡ありがとうございます。
ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、
11/9までに登録完了で考えております。
（DN購入の支払日は10/31予定です）
この日程感で、11/9までに登録完了可能そうでしょうか？

⇒A2DPおよびAVRCPのプロファイル試験の結果次第ではありますが、

これまでの経験ではFail項目の再試験、再々試験を加味しても約

3週間で完了するのが一般的です。

この経験則からは11/9までに登録完了可能です。
大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。
なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

⇒添付にて見積書を提出いたします。

労務費、原材料費、エネルギーコスト等を含めた適正な価格で見積りしております。

ご検討のほどよろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Wednesday, September 24, 2025 8:04 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

アリオン飯田様お世話になっております。

ソニー宮川です。

間をあけてしまい申し訳ございません。

ラフな日程感ですが、10月上旬に契約を締結、10月末までにテスト完了、11/9までに登録完了で考えております。

（DN購入の支払日は10/31予定です）

この日程感で、11/9までに登録完了可能そうでしょうか？

大丈夫そうでしたら、2025/11/9までに登録前提で、正式見積もり書の発行をお願いしたいです。

なお見積もりですが、労務費、原材料費、エネルギーコスト等を含めた適正な価格をご連絡ください。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 7:24 PM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > 一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？ > 今回ホストはQ346069を参照で > A2DP 1. 4 > AVRCP 1. 6. 2 > となっております。 > 3年前のQDID
199247のときは > A2DP 1. 3. 2 > AVRCP 1. 5 > としていました。 ⇒プロファイル(X2core)部をQDID

ソニー宮川様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。
一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？
今回ホストはQ346069を参照で
A2DP　1.4
AVRCP 1.6.2
となっております。
3年前のQDID 199247のときは
A2DP 1.3.2
AVRCP　1.5
としていました。

⇒プロファイル(X2core)部をQDID 199247を参照した後、ICS修正でA2DP 1.4、

AVRCP 1.6.2に変更すると、ICS更新に伴ってA2DPとAVRCPのテスト要求が出力されます。

A2DPとAVRCPをPTS試験を実施してテストレポートを取得し、アップロードすることでICS更新が可能かつ試験を最小限に抑えることが可能です。

11月9までの登録では以下の見積です。

・プロファイル試験(A2DP,AVRCP) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ登録費のドル送金)

11月10以降の登録では以下の見積となります。

・プロファイル試験(A2DP,AVRCP,IOPT) ￥400,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From:

Sent: Friday, September 12, 2025 2:36 PM

To: Masaya Iida

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験（テレビ）

※メールを分かりやすくするため、件名に（テレビ）を付け加えておりますアリオン飯田様お世話になっております。

ソニー宮川です。
⇒今回の登録でQ333791、Q346069およびFY23のQDID:199247をIncludeしてA2DPなどのプロファイルをQDID:199247からICSレベルで踏襲することで各プロファイルの試験実施とレポートアップロードは回避できます。
もしプロファイルのICSがFY23のQDID:199247から追加サポート項目があるとこの方法は使えませんがFY26でFY23のプロファイル機能と同一で支障なければこの方法でのプロファイル試験回避をおすすめします。

一部プロファイルのバージョンが異なるのですが、この場合でもプロファイル試験回避できますか？

今回ホストはQ346069を参照で

A2DP　1.4

AVRCP 1.6.2

となっております。

3年前のQDID 199247のときは

A2DP 1.3.2

AVRCP　1.5

としていました。

以上、ご確認よろしくお願い致します。

From: Masaya Iida

Sent: Friday, September 12, 2025 11:04 AM

To: Miyagawa, Yoichi (SEC)

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 以下回答いたします。 > ご確認ありがとうございます、Q325703参照は色々問題があり、SubsetのQ333791を > 使った方がいい件、理解しました。 ⇒ご理解いただきありがとうございます。 > 一点確認させてください。 > 今回の見積もりですが、プロファイル試験の実施場所はどちらになりますでしょうか？ >
前回と同じく台湾ですか？ ⇒今回の登録でQ333791、Q346069およびFY23のQDID: 199247をIncludeしてA2DPなどのソニー宮川様いつもお世話になっております。

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

Subject: RE: [RFQ][Allion 様 ] FY26 [ID] Bluetooth SIG 認証試験ソニー宮川様いつもお世話になっております。 アリオンの飯田です。 Bluetooth SIG認証のご相談をいただきまして、 誠にありがとうございます。 添付が見積依頼書です。 お手数ですが記載の上、ご提出をお願いいたします。 以上、よろしくお願いいたします。 = = = = = = = = = = アリオン株式会社営業統括部営業担当飯田雅也 〒[ID] 東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階 Tel [ID] 内線220

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
