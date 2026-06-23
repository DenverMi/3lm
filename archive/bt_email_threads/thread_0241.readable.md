# thread_0241: Re: 【内部連絡】FW: [至急：上位製品実装モジュールに内在するICS不整合について]

- Message count: 2
- Source JSON: `thread_0241.json`

---

## 1. 2024-10-08 07:28

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , AJ Bluetooth Group
**Attachments:** ���������������������������.doc, Outlook-z01dicrb.png

望月さんお疲れさまです。
先ほど打合せで、デンソーテン様から今回のProfile試験完了後の手続きについて確認がございましたので以下回答可能でしょうか。

⇒添付資料とともに下記のように答えてください。

酒井ーーーー
１：試験がPassで完了後にデンソーテン側で作業が必要なものを教えてください。

⇒登録完了に合わせてコンプライアンスフォルダ作成用に下記資料をご準備ください。

・製品の操作説明書・製品のブロック図・製品の外形図・アンテナ資料（放射利得特性の記載されたもの）
２：試験が完了してから認証取得終了までどのくらいの時間がかかるでしょうか。

⇒登録費の支払が完了していれば3営業日前後で完了します。試験完了直前に代行登録内容確認書(添付)をご提出願います。

ーーーー差出人: Toshitaka Mochizuki

送信日時: 2024年10月8日 16:18

宛先: AJ Bluetooth Group

件名: 【内部連絡】FW: [至急：上位製品実装モジュールに内在するICS不整合について]

酒井さん望月ですお疲れ様です。

先ほど打合せで、デンソーテン様から今回の Profile 試験完了後の手続きについて確認がございましたので以下回答可能でしょうか。

１：試験が Pass で完了後にデンソーテン側で作業が必要なものを教えてください。

２：試験が完了してから認証取得終了までどのくらいの時間がかかるでしょうか。

以上、ご確認どうぞよろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, September 11, 2024 1:12 PM

To: Hiroshi Majima ( 間嶋宏 ) ; Toshitaka Mochizuki ; Yukihiro Nakano

Subject: Re: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

デンソーテン間嶋様アリオンの酒井です。いつもお世話になっております。
ご指摘のエラーは以前の ICS で存在しなかった項目であり、このケースでは TCW(Test
Coverage Waiver)
: [ID] を適用可能であると BQC から伺っております。
(Consistency Check でご指摘のエラーが出ているままで
ICS Selection 画面下部の TCW 入力 BOX に「ES-
25636」を入力し、登録 )
弊社もこの方法でこれらのエラーを回避して登録できておりますので、一度、当方法で回避できないか、
認証代行機関様へご確認頂けないでしょうか？宜しくお願い致します。

⇒ 「認証依頼先から回答がありました」として下記内容を返信してください。

ーーーー

SIG の [ID] に関する下記 Help&Support ページには下記の説明があります。

すなわち「もし inconsistency がその階層に存在しない ICS 項目 (ICS
item does not exist) を示す場合には

[ID] が適用できる ([ID]
would apply.)」

今回、 [ID] を Include した製品登録では下記 Inconsistency がレポートされます。

2:C.1 | If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

2:C.2 | If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

[BB] (2/4)、
[BB] (2/5) は存在する ICS ですが、 [LMP]
(2b/1-2)、 [LMP] (2b/3) が存在しない ICS のために

[ID] が適用される可能性があります。したがって、まずは [ID] を Include して早めに製品登録を実施して、何か問題があっても認証取得日程をキープできるように注意して進めることを提案します。

ーーーー以上よろしくお願いいたします。

差出人 : Hiroshi
Majima ( 間嶋宏 )

送信日時 : 2024 年 9 月 10 日
22:52

宛先 : Itsuo
Sakai ; Toshitaka Mochizuki ; Yukihiro Nakano

件名 : RE:
[ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMI ソリューション )IVI 技術 1 部 2-4 課間嶋です。

お世話になっております。

下記ご指摘の件、村田の方に確認しましたところ以下とのことなのですが、下記方法で回避可能でしょうか？

＜村田からの回答＞

ご指摘のエラーは以前の ICS で存在しなかった項目であり、このケースでは TCW(Test Coverage Waiver): [ID] を適用可能であると BQC から伺っております。

(Consistency Check でご指摘のエラーが出ているままで ICS Selection 画面下部の TCW 入力 BOX に「[ID]」を入力し、登録 )

弊社もこの方法でこれらのエラーを回避して登録できておりますので、一度、当方法で回避できないか、認証代行機関様へご確認頂けないでしょうか？宜しくお願い致します。

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMI ソリューション事業本部 IVI 技術一部第二技術室第四技術課間嶋宏

〒 [ID]

神戸市兵庫区御所通 [ID]

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 10:59 AM

To: Hiroshi Majima ( 間嶋宏 ) ; Toshitaka Mochizuki ;
Yukihiro Nakano

Subject: Re: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

デンソーテン間嶋様アリオンの酒井です。いつもお世話になっております。
村田の方から、
『[LL] (9/11)
を No
とした登録』について SIG 審査が完了したとの連絡がありました。
DN(Design Number) が [ID] とのことなのですが、
アリオン様の方で確認可能でしょうか？

⇒ SIG の登録検索で [ID] を検索し、詳細ページの [View
ICS Details] アイコンで開いた ICS 詳細ページの [Consistency Check] をクリックして ICS 不整合を確認しました。その結果 [ID] 間に 2 件の階層間不整合が検出されました。（どうしてこんな中途半端な更新登録をしたのでしょうか不思議です。）

2:C.1 | If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

2:C.2 | If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

上記の階層間不整合は [ID] を Include した御社製品登録でもそのまま引き継がれ、 [BB]2/4,
2/5 を製品登録の過程で変更すると製品登録付帯の Test Plan に BB 階層の試験要求が発生します。

M 社に [ID] に内在する下記不整合を解消するよう至急申しいれてください。

2:C.1 | If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

2:C.2 | If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

以上回答いたします。

差出人 : Hiroshi
Majima ( 間嶋宏 )

送信日時 : 2024 年 9 月 10 日 10:24

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Yukihiro Nakano

件名 : RE:
[ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMI ソリューション )IVI 技術 1 部 2-4 課間嶋です。

お世話になっております。

村田の方から、

『[LL] (9/11)
を No とした登録』について SIG 審査が完了したとの連絡がありました。

DN(Design Number) が [ID] とのことなのですが、

アリオン様の方で確認可能でしょうか？

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMI ソリューション事業本部 IVI 技術一部第二技術室第四技術課間嶋宏

〒 [ID]

神戸市兵庫区御所通 [ID]

From: Hiroshi Majima ( 間嶋宏 )

Sent: Friday, September 6, 2024 8:49 PM

To: Itsuo Sakai ; Toshitaka Mochizuki ;
Yukihiro Nakano

Subject: RE: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMI ソリューション )IVI 技術 1 部 2-4 課間嶋です。

お世話になっております。

下記ご回答頂きありがとうございます。

問題ないとのこと承知いたしました。

引き続きよろしくお願いいたします。

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMI ソリューション事業本部 IVI 技術一部第二技術室第四技術課間嶋宏

〒 [ID]

神戸市兵庫区御所通 [ID]

From: Itsuo Sakai

Sent: Friday, September 6, 2024 7:54 PM

To: Hiroshi Majima ( 間嶋宏 ) ;
Toshitaka Mochizuki ; Yukihiro Nakano

Subject: Re: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

デンソーテン間嶋様アリオンの酒井です。いつもお世話になっております。
下記メール頂きました件、村田に確認しましたところ・ [LL](9/11) を No とした登録を作成中・登録は、現行の [ID](QDID:[ID]）とは別の ID となりそうとの回答を得ました。
この対応で問題なかったでしょうか？

⇒ 早速のご対応ありがとうございます。 [LL](9/11) を No とした新規登録が完了すればそれを参照することで御社の製品登録は問題なく進められます。

以上回答いたします。

差出人 : Hiroshi
Majima ( 間嶋宏 )

送信日時 : 2024 年 9 月 6 日 19:47

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Yukihiro Nakano

件名 : RE:
[ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMI ソリューション )IVI 技術 1 部 2-4 課間嶋です。

お世話になっております。

下記メール頂きました件、村田に確認しましたところ・ [LL](9/11) を No とした登録を作成中・登録は、現行の [ID](QDID:[ID]）とは別の ID となりそうとの回答を得ました。

この対応で問題なかったでしょうか？

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMI ソリューション事業本部 IVI 技術一部第二技術室第四技術課間嶋宏

〒 [ID]

神戸市兵庫区御所通 [ID]

From: Itsuo Sakai

Sent: Tuesday, September 3, 2024 2:47 PM

To: Hiroshi Majima ( 間嶋宏 ) ;
Toshitaka Mochizuki ; Yukihiro Nakano

Subject: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

このメッセージを受信した人は、
からのメールを受け取る頻度が高くありません。 このことが重要である理由デンソーテン、間嶋様アリオンの酒井です。いつもお世話になっております。

先行して私の Qualification Workspace で見積依頼書記載内容で仮 Project を作成して ICS の確認を実施しました。その結果、上位モデルでモジュール登録の ICS 内容そのものに含まれる不整合がネックになり、製品登録で ICS 修正を強行すると LL 試験要求が発生することが判明しました。

至急下記内容を M 社へ送付して対処をご依頼ください。

村田製モジュール「[ID] /[ID](QDID:[ID]）」は SIG の登録サイトで ICS を確認すると LL 階層で下記 Invalid （階層間不整合）が含まれています。

If [RFPHY] is Supported and [RFPHY] (1/15) is Not Supported then [LL] (9/11) is Excluded

これは [RFPHY] (1/15) Class 1： NO に対して [LL]
(9/11) Class 1: YES という登録内容に起因するもので、このまま製品登録を進めると、 (1)
製品登録の ICS で [LL]
(9/11): YES→NO への変更を行うと LL 階層の追加試験要求が発生します。

この LL 試験要求を回避しつつ製品登録を完了するためには、 M 社のオリジナル登録に含まれる上記

Invalid を取り除いてもらうしか方法がありません。選択肢は (1)M 社「[ID]
/[ID]

(QDID:[ID]）」の Listing
Owner から SIG へ ICS
Error Correction Request を出して [LL] (9/11)

Class 1: YES→NO に修正依頼する、 (2) すでに [LL]
(9/11) Class 1: YES として参照した製品登録が存在すると ICS 修正は拒絶されますので、その場合には M 社が当該 Invalid を含まない更新登録を実施する、の 2 通りです。

以上よろしくお願いいたします。

---

## 2. 2024-10-15 09:12

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , AJ Bluetooth Group
**Attachments:** Outlook-z01dicrb.png

望月さんお疲れさまです。

以下のように回答してください。

酒井ーーーー
１：製品のブロック図は添付の内容で良いか確認を依頼されました。
ご確認お願いいたします。

⇒これはBluetoothモジュール部分のみが記載されています。ブロック図は電波法工事設計認証で提出するものと同様の製品全体が対象のブロック図をご準備ください。
２：製品の操作説明書ですが、どの程度の記載の物が必要か問われました。
製品起動から一通りの機能の操作が書かれた総合的なユーザーマニュアルのようなものか、
Bluetoothの操作部分のみに特化したものか等。

⇒コンプライアンスダ用としてわざわざBluetoothの操作部分のみに特化したすさ説明書を作成いただく必要はございません。既存のユーザーマニュアルのBluetooth操作部分だけを抜き出したものをご準備ください。
３：INVOICEは添付のもので問題ないでしょうか。

⇒今回は上位モデルと下位モデルの2件が登録対象です。1件分としては添付のInvoiceで問題ありませんが、同じ操作でもう1件分を取得してください。

ーーーー差出人: Toshitaka Mochizuki

送信日時: 2024年10月15日 17:38

宛先: Itsuo Sakai ; AJ Bluetooth Group

件名: Re: 【内部連絡】FW: [至急：上位製品実装モジュールに内在するICS不整合について]

酒井さん望月ですお疲れ様です。

デンソーテン様から質問です。

コンプライアンスフォルダ用の資料について以下質問です

１：製品のブロック図は添付の内容で良いか確認を依頼されました。

ご確認お願いいたします。

２：製品の操作説明書ですが、どの程度の記載の物が必要か問われました。

製品起動から一通りの機能の操作が書かれた総合的なユーザーマニュアルのようなものか、

Bluetoothの操作部分のみに特化したものか等。

３：INVOICEは添付のもので問題ないでしょうか。

以上、ご確認どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人: Itsuo Sakai

送信日時: 2024年10月8日 16:28

宛先: Toshitaka Mochizuki ; AJ Bluetooth Group

件名: Re: 【内部連絡】FW: [至急：上位製品実装モジュールに内在するICS不整合について]

望月さんお疲れさまです。
先ほど打合せで、デンソーテン様から今回のProfile試験完了後の手続きについて確認がございましたので以下回答可能でしょうか。

⇒添付資料とともに下記のように答えてください。

酒井ーーーー
１：試験がPassで完了後にデンソーテン側で作業が必要なものを教えてください。

⇒登録完了に合わせてコンプライアンスフォルダ作成用に下記資料をご準備ください。

・製品の操作説明書・製品のブロック図・製品の外形図・アンテナ資料（放射利得特性の記載されたもの）
２：試験が完了してから認証取得終了までどのくらいの時間がかかるでしょうか。

⇒登録費の支払が完了していれば3営業日前後で完了します。試験完了直前に代行登録内容確認書(添付)をご提出願います。

ーーーー差出人: Toshitaka Mochizuki

送信日時: 2024年10月8日 16:18

宛先: AJ Bluetooth Group

件名: 【内部連絡】FW: [至急：上位製品実装モジュールに内在するICS不整合について]

酒井さん望月ですお疲れ様です。

先ほど打合せで、デンソーテン様から今回のProfile試験完了後の手続きについて確認がございましたので以下回答可能でしょうか。

１：試験がPassで完了後にデンソーテン側で作業が必要なものを教えてください。

２：試験が完了してから認証取得終了までどのくらいの時間がかかるでしょうか。

以上、ご確認どうぞよろしくお願い致します。

From: Itsuo Sakai

Sent: Wednesday, September 11, 2024 1:12 PM

To: Hiroshi Majima ( 間嶋宏 ) ; Toshitaka Mochizuki ; Yukihiro Nakano

Subject: Re: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

デンソーテン間嶋様アリオンの酒井です。いつもお世話になっております。

ご指摘のエラーは以前の ICS で存在しなかった項目であり、このケースでは TCW(Test
Coverage Waiver)
: [ID] を適用可能であると BQC から伺っております。
(Consistency Check でご指摘のエラーが出ているままで ICS Selection 画面下部の TCW 入力 BOX に「ES-
25636」を入力し、登録 )

弊社もこの方法でこれらのエラーを回避して登録できておりますので、一度、当方法で回避できないか、

認証代行機関様へご確認頂けないでしょうか？宜しくお願い致します。

⇒ 「認証依頼先から回答がありました」として下記内容を返信してください。

ーーーー

SIG の [ID] に関する下記 Help&Support ページには下記の説明があります。

すなわち「もし inconsistency がその階層に存在しない ICS 項目 (ICS
item does not exist) を示す場合には

[ID] が適用できる ([ID]
would apply.)」

今回、 [ID] を Include した製品登録では下記 Inconsistency がレポートされます。

2:C.1 | If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

2:C.2 | If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

[BB] (2/4)、 [BB]
(2/5) は存在する ICS ですが、 [LMP]
(2b/1-2)、 [LMP] (2b/3) が存在しない ICS のために

[ID] が適用される可能性があります。したがって、まずは [ID] を Include して早めに製品登録を実施して、何か問題があっても認証取得日程をキープできるように注意して進めることを提案します。

ーーーー以上よろしくお願いいたします。

差出人 : Hiroshi Majima ( 間嶋宏 )

送信日時 : 2024 年 9 月 10 日 22:52

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Yukihiro Nakano

件名 : RE: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMIソリューション)IVI技術1部 2-4課間嶋です。

お世話になっております。

下記ご指摘の件、村田の方に確認しましたところ以下とのことなのですが、下記方法で回避可能でしょうか？

＜村田からの回答＞

ご指摘のエラーは以前のICSで存在しなかった項目であり、このケースではTCW(Test Coverage Waiver): ES-25636を適用可能であるとBQCから伺っております。

(Consistency Checkでご指摘のエラーが出ているままで ICS Selection画面下部のTCW入力BOXに「[ID]」を入力し、登録)

弊社もこの方法でこれらのエラーを回避して登録できておりますので、一度、当方法で回避できないか、認証代行機関様へご確認頂けないでしょうか？宜しくお願い致します。

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMIソリューション事業本部 IVI技術一部第二技術室第四技術課間嶋宏

〒[ID]

神戸市兵庫区御所通1-2-28

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 10:59 AM

To: Hiroshi Majima ( 間嶋宏 ) ;
Toshitaka Mochizuki ;
Yukihiro Nakano

Subject: Re: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

デンソーテン間嶋様アリオンの酒井です。いつもお世話になっております。
村田の方から、
『[LL] (9/11)
を No
とした登録』について SIG 審査が完了したとの連絡がありました。
DN(Design Number) が [ID] とのことなのですが、
アリオン様の方で確認可能でしょうか？

⇒ SIG の登録検索で [ID] を検索し、詳細ページの [View
ICS Details] アイコンで開いた ICS 詳細ページの [Consistency Check] をクリックして ICS 不整合を確認しました。その結果 [ID] 間に 2 件の階層間不整合が検出されました。（どうしてこんな中途半端な更新登録をしたのでしょうか不思議です。）

2:C.1 | If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

2:C.2 | If [LMP] is Supported and [LMP] (2b/3) is Not Supported
then [BB] (2/5) is Excluded

上記の階層間不整合は [ID] を Include した御社製品登録でもそのまま引き継がれ、 [BB]2/4,
2/5 を製品登録の過程で変更すると製品登録付帯の Test Plan に BB 階層の試験要求が発生します。

M 社に [ID] に内在する下記不整合を解消するよう至急申しいれてください。

2:C.1 | If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported
then [BB] (2/4) is Excluded

2:C.2 | If [LMP] is Supported and [LMP] (2b/3) is Not Supported
then [BB] (2/5) is Excluded

以上回答いたします。

差出人 : Hiroshi Majima ( 間嶋宏 )

送信日時 : 2024 年 9 月 10 日 10:24

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Yukihiro Nakano

件名 : RE: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMIソリューション)IVI技術1部 2-4課間嶋です。

お世話になっております。

村田の方から、

『[LL] (9/11) を No とした登録』についてSIG審査が完了したとの連絡がありました。

DN(Design Number)がQ307172とのことなのですが、

アリオン様の方で確認可能でしょうか？

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMIソリューション事業本部 IVI技術一部第二技術室第四技術課間嶋宏

〒[ID]

神戸市兵庫区御所通1-2-28

From: Hiroshi Majima ( 間嶋宏 )

Sent: Friday, September 6, 2024 8:49 PM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Yukihiro Nakano

Subject: RE: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMIソリューション)IVI技術1部 2-4課間嶋です。

お世話になっております。

下記ご回答頂きありがとうございます。

問題ないとのこと承知いたしました。

引き続きよろしくお願いいたします。

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMIソリューション事業本部 IVI技術一部第二技術室第四技術課間嶋宏

〒[ID]

神戸市兵庫区御所通1-2-28

From: Itsuo Sakai

Sent: Friday, September 6, 2024 7:54 PM

To: Hiroshi Majima ( 間嶋宏 ) ;
Toshitaka Mochizuki ;
Yukihiro Nakano

Subject: Re: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

デンソーテン間嶋様アリオンの酒井です。いつもお世話になっております。
下記メール頂きました件、村田に確認しましたところ・ [LL](9/11) を No とした登録を作成中・登録は、現行の [ID](QDID:[ID]）とは別の ID となりそうとの回答を得ました。
この対応で問題なかったでしょうか？

⇒ 早速のご対応ありがとうございます。 [LL](9/11) を No とした新規登録が完了すればそれを参照することで御社の製品登録は問題なく進められます。

以上回答いたします。

差出人 : Hiroshi Majima ( 間嶋宏 )

送信日時 : 2024 年 9 月 6 日 19:47

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Yukihiro Nakano

件名 : RE: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

アリオン酒井様デンソーテン

HMIソリューション)IVI技術1部 2-4課間嶋です。

お世話になっております。

下記メール頂きました件、村田に確認しましたところ・[LL](9/11)をNoとした登録を作成中・登録は、現行のD064454(QDID:[ID]）とは別のIDとなりそうとの回答を得ました。

この対応で問題なかったでしょうか？

以上、よろしくお願いいたします。

私の交通安全宣言： 「常にゆとりを持って運転し安全運転を心がけます」

株式会社デンソーテン

HMIソリューション事業本部 IVI技術一部第二技術室第四技術課間嶋宏

〒[ID]

神戸市兵庫区御所通1-2-28

From: Itsuo Sakai

Sent: Tuesday, September 3, 2024 2:47 PM

To: Hiroshi Majima ( 間嶋宏 ) ;
Toshitaka Mochizuki ;
Yukihiro Nakano

Subject: [ 至急：上位製品実装モジュールに内在する ICS 不整合について ]

このメッセージを受信した人は、
からのメールを受け取る頻度が高くありません。 このことが重要である理由デンソーテン、間嶋様アリオンの酒井です。いつもお世話になっております。

先行して私の Qualification Workspace で見積依頼書記載内容で仮 Project を作成して ICS の確認を実施しました。その結果、上位モデルでモジュール登録の ICS 内容そのものに含まれる不整合がネックになり、製品登録で ICS 修正を強行すると LL 試験要求が発生することが判明しました。

至急下記内容を M 社へ送付して対処をご依頼ください。

村田製モジュール「[ID] /[ID](QDID:[ID]）」は SIG の登録サイトで ICS を確認すると LL 階層で下記 Invalid （階層間不整合）が含まれています。

If [RFPHY] is Supported and [RFPHY] (1/15) is Not Supported then [LL] (9/11) is Excluded

これは [RFPHY] (1/15) Class 1： NO に対して [LL]
(9/11) Class 1: YES という登録内容に起因するもので、このまま製品登録を進めると、 (1)
製品登録の ICS で [LL]
(9/11): YES→NO への変更を行うと LL 階層の追加試験要求が発生します。

この LL 試験要求を回避しつつ製品登録を完了するためには、 M 社のオリジナル登録に含まれる上記

Invalid を取り除いてもらうしか方法がありません。選択肢は (1)M 社「[ID]
/[ID]

(QDID:[ID]）」の Listing
Owner から SIG へ ICS
Error Correction Request を出して [LL] (9/11)

Class 1: YES→NO に修正依頼する、 (2) すでに [LL]
(9/11) Class 1: YES として参照した製品登録が存在すると ICS 修正は拒絶されますので、その場合には M 社が当該 Invalid を含まない更新登録を実施する、の 2 通りです。

以上よろしくお願いいたします。
