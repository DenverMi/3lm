# thread_0183: [HM23登録方法変更のお願い] Re: [ALAP] HM23 Bluetooth SIG認証について

- Message count: 3
- Source JSON: `thread_0183.json`

---

## 1. 2025-01-22 13:08

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura
**Attachments:** [ID]xlsx

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
Core階層ICSのチェックを修正することでConsistency Checkの結果がご提示いただいた3項目となり、
進めることができました。
その次のStepのテストレポートのアップロードが何度試しても処理中から進まないため完了はできておりませんが、明日改めて試してみます。

⇒私がアドバイスした「LE AUdio Profile」を削除する方法では、これまで経験のない添付の86項目ものIOPT試験要求が発生するシステムに改変さています。IOPT試験はSDPで対向機器のサポートプロファイルを確認するBR/EDRプロファイルだけが対象ですのでLE Profileの改変は関係ないはずです。テストレポートのアップロードが何度試しても処理中から進まないのは、おそらくこの試験要求のテストレポートを待っているからかと推測します。

そこで何とか&quot;Combine unmodified Designs&quot;で進む方法はないか色々調べて試した結果、BAPに関するTCW:ES-25802が使えそうです。

下記手順で登録を進めてください。

(1) [URL] Productsを開いてください。

(2) Product Detailページが開きますので右下の[Save and got to Specify the Design]をクリック

(3) Q328538の右のＸで削除後、再度Q328538を入力し、[I'm finished entering DNs]をクリックし、

[Combine unmodefied Designs]をクリックし、[Perform consistency Check]をクリック。

(4) 下図が表示されるので[Apply TCW]をクリックし開いた入力欄に [ID] を入力後、右下の

[Save and goto Test Plan and Documentation]をクリック

(5) 下図のように No test plan is generated - - と表示される。

右下の[Save and goto Qulification Fee]をクリック後、Recipt Numberを選択して右下の

[Save and go to Submission]をクリックし、&quot;ICS Form&quot;が黄色である以外はStatus欄が緑の□表示出ることを確認して下方の確認欄にチェックし、Listing Ownerの英文名を署名欄に入力後[Complete the Submission]をクリックしてSubmissionを行ってください。

(6) TCWによる登録のためSIG管理者の確認んのめ2-3営業日後に登録が承認されます。却下の場合はその旨Emailが届き、Recipt NumberとともにDrft Pridcut一覧へ差し戻されます。この場合にはそのメールを私に転送してご連絡ください。

以上よろしくお願いいたします。

差出人: Hiroaki Fukaura

送信日時: 2025年1月22日 17:07

宛先: Itsuo Sakai

件名: RE: [HM26登録懸念点は解消] Re: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

Core 階層 ICS のチェックを修正することで Consistency Check の結果がご提示いただいた 3 項目となり、進めることができました。

その次の Step のテストレポートのアップロードが何度試しても処理中から進まないため完了はできておりませんが、明日改めて試してみます。

ありがとうございました。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, January 22, 2025 1:22 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

「(4) Core 階層の ICS
10/1 のチェックを外し、」が記載ミスで正しくは「Core 階層の ICS
12/1 のチェックを外し」です。申し訳ありませんでした。

対応方法としては、 ICS Selection で
Core 10/1 をチェックし、 Core 12/1 のチェックを外して再度

Consistency Check を行ってください。

以上よろしくお願いいたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2025 年 1 月 22 日
13:10

宛先 :
Itsuo Sakai

件名 :
RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

特別サポートのご提案、並びに詳細な登録方法のアドバイスをいただきありがとうございます。

ご連絡いただいた手順で進めましたが、 (4) の Consistency Check 後に表示される結果が 3 項目であるべきところ 5 項目表示されました。

酒井様ご提示の３項目に加え、以下の 2 項目が表示されています。

―――

CORE

12:C.1 | If [CORE] (12/1) is Supported then it is Mandatory to Support at least one of [CORE] (12/2-3)

SEC

SEC > CORE | If [CORE] (10/1) is Not Supported then [SEC] is Excluded Go to Layer Selection.

―――

お手数おかけしますが、記入内容が正しいかチェックしていただけないでしょうか？

画面キャプチャしましたので添付ファイルをご参照願います。

追加サポートについて有償となる場合は弊社内で承認を得るため、お見積書の発行をお願いいたします。

また以降同様の案件については代行登録を発注しての対応となることを承知いたしました。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, January 21, 2025 5:18 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

お問い合わせの内容は、 Include 先の登録内容や登録製品のサポート機能によって個々に異なる対応が必要で代行登録と同じ手間が発生するため、本来は「代行登録をご依頼ください」という対応となります。しかし、御社からは MH26 や新田様案件などをご依頼いただいていますので特別にサポートさせていただきます。以下の手順で登録できることを確認しました。

(1) [ID]
と [ID]
を Include 後、 [Modefy
or Add to this set of Design] をクリック ( 下図 )。

(2)
右下の [Save and go to Layer Selection] をクリック。

(3) Layer Selection ページで Core
Layers から HCI
と UHCI
のチェックをはずし、 LE Audio Spec からすべてのプロトコル・プロファイルのチェックを外して右下の [Save and go to ICS Selection] をクリック

(4) Core 階層の ICS
10/1 のチェックを外し、右上の [Consistency Check] をクリック。結果が下記

3 項目であることを確認後、下部の [Test
Coverage Waiver(s)] に [ID]( 下図 ) を入力後右下の

[Save and go to Test Plan and Documentation] をクリック。その後のページは記載内容に従って所定の入力などを行い、最後のページまで進む。 .

ーーー

BB

If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

GAP

4b:Prerequisite | If [GATT] (1a/4) is Supported then [GAP] (4b/1-2) are Mandatory

ーーー以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2025 年 1 月 21 日
16:08

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

下記、間が空いてしまいましたが弊社 HM23 の Android14 登録についてアドバイスいただけないでしょうか。

弊社大平より、
この後、 Host subsystem、 Profile subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

と説明いたしましたが、 Qualcomm 社から Host と Profile を統合した「QDID/DN : [ID]」の登録完了連絡を受けました。

そこで、 Core_Host and Profiles Qualification: [ID] と Controller Subsystem: [ID] (HM23 A13 から変更なし ) で登録を試みたところ

Consistency Check で添付画像のエラーが出てしまいました。

これは酒井様のご説明にある“ QDID:[ID] から RF/RF PHY 階層を選択する”事により回避可能でしょうか？

試しに「Modify Layers of your Disign manually」を選択して進めてみたところ、エラーにある BAP は LE で選択されていましたが

BASS は選択されていないようでした。

またそのいずれも変更を加えようとすると新しい Ver が適用されるというような警告が表示されました。

もし階層選択によりエラーを無くせるようなら、手順を教えていただけないでしょうか？

大変お手数おかけしますがよろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, October 31, 2024 9:51 AM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
この後、 Host subsystem、 Profile
subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

⇒ 承知しました。
また、ご指摘頂いております RF 試験 1 項目の追加実施につきまして、
先日王君様より概算見積をご提示頂いております。

⇒ 試験項目の不足に関して再度精査しました。当該不足項目は [ID] で追加されて発効が 2022/12/28 でした。従って御社の QDID:[ID](Controller
Subsystem / Listing Date

:[ID]) および展開いただいた SGS 台湾での RF/RF
PHY レポートに含まれていなくても

QDID:[ID] の登録に関しては認証規定上の問題はありません。

しかし、 新規に「当該 RF/RF PHY レポートをエビデンスとした登録を行と不足項目が問題」となります。 ( 以前問題ありと連絡を差し上げた内容です。 )

そこで提案ですが、 QDID:[ID] は Controller
Subsystem 登録ですので現在も引き続き有効なため、これと Q 社の Subset
DN [ID] を Include して、 QDID:[ID] から RF/RF
PHY 階層を選択するとともに DN [ID] から残りの階層を選択すると「認証規定に準拠して」 2022/04/20 当時に有効であった RF/RF PHY およびそのエビデンスを引き継ぐことが可能です。この部分組み合わせ登録手順は 7/1 の新登録サイトで可能となったもので、こうすることで不足項目試験を実施すること無く「認証規定に準拠した」 HM23 登録を進めることが可能です。

以上ご検討ください。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 10 月 30 日 13:49

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早々にご確認頂きありがとうございます。

作成頂いた「Subset DN [ID]」にて問題にないとのこと、承知致しました。

この後、 Host subsystem、 Profile subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

また、ご指摘頂いております RF 試験 1 項目の追加実施につきまして、

先日王君様より概算見積をご提示頂いております。

参考にさせて頂き対応方法等決定しましたら改めてご連絡させて頂きます。

/eom

From: Itsuo Sakai

Sent: Wednesday, October 30, 2024 12:10 PM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
HM23 にて使用している [ID](QDID
[ID]) につきまして、
先日追加にて AoA/AoD 機能削除必要とのことでアドバイス頂いておりました件、
Qualcomm より本件対応完了とのことで連絡がされております。

⇒ ご連絡ありがとうございます。
酒井様よりご教示頂きました通り、 SIG にて以下について削除となっている旨確認はしておりますが、本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

⇒ 私の Workspace で仮 Project を作成して「N
[ID]」で問題解消したことを確認できました。

引き続きよろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 10 月 30 日 11:36

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To.
アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。度々申し訳ありません。

削除追加にて連絡されている subset DN は以下の通りとなります。

先のメールにて記載漏れており申し訳ありません。

ご確認の程よろしくお願い致します。
Subset DN [ID] was created from QDID [ID], [ID] Controller listing.

/eom

From:
大平ひとみ Hitomi Ohira

Sent: Wednesday, October 30, 2024 11:32 AM

To: Itsuo Sakai

Subject: RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To.
アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23 にて使用している [ID](QDID [ID]) につきまして、

先日追加にて AoA/AoD 機能削除必要とのことでアドバイス頂いておりました件、

Qualcomm より本件対応完了とのことで連絡がされております。

Update the subset DN [ID] for [ID] (delete AoA/AoD capabilities from LL)

酒井様よりご教示頂きました通り、 SIG にて以下について削除となっている旨確認はしておりますが、

本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

お忙しいところお手数おかけし申し訳ありません。

ご協力の程よろしくお願い致します。

→ [LL] (9/17):NO

→ [LL] (9/20):NO

→ [LL] (9/21):NO

→ [LL] (9/23):NO

→ [LL] (9/24):NO

/eom

From: Itsuo Sakai

Sent: Monday, September 30, 2024 7:49 PM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
HM23 にして使用している [ID](QDID
[ID]) につきましても
Power Class1 サポート削除にて Subset
DN [ID] が登録されたとのことで連絡がされました。

お忙しいところ大変恐縮ではございますが、こちらにつきましても先日の HM26 と同様に懸念点解消となっているかご確認頂くことは可能でしょうか？

⇒ Qualification Warkspace で仮 Project を作って確認しました結果、 DN:[ID] は確かに LL
9/11 LE

Power Class 1: NO と修正されて RF
PHY 1/15:NO との階層間不整合は消えました。しかし先日ご送付いただいたベースモデルの RF PHY テストレポート記載の RF
PHY ICS と、 DN [ID] の

LL 階層間に以下の 5 件の不整合 (AoA/AoD の関連 ) が発生します。

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/17) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/20) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/13) is Not Supported then [LL] (9/23) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/14) is Not Supported then [LL] (9/24) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/12) is Not Supported then [LL] (9/21) is Excluded

Q 社には「Subset
DN [ID] から LL の AoA/AoD 機能を削除 ([LL]
(9/17):NO、 [LL] (9/20):NO、

[LL] (9/21):NO、 [LL]
(9/23):NO、 [LL] (9/24):NO) した Subset
DN を作成してほしい。」と再度依頼してください。

以上回答いたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 30 日 11:56

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23 にして使用している [ID](QDID [ID]) につきましても

Power Class1 サポート削除にて Subset DN [ID]
が登録されたとのことで連絡がされました。

お忙しいところ大変恐縮ではございますが、こちらにつきましても先日の HM26 と同様に懸念点解消となっているかご確認頂くことは可能でしょうか？

上記ご協力頂けますと幸いです。

よろしくお願い致します。

/eom

From: Itsuo Sakai

Sent: Wednesday, September 25, 2024 4:08 PM

To: 大平ひとみ Hitomi Ohira

Subject: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
早速ですが、 HM26 にて使用している [ID](QDID
[ID]) にて DN [ID] が作成され、
Subset DN [ID]
も作成頂けた旨連絡頂いております。
Subset DN にて「9/11
LE Power Class 1」のサポートが削除されている旨も確認致しましたが、
取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

⇒ [ID](QDID [ID]) の Subset
DN: [ID] での HM26 の登録可能性を私の Quaification
Workspace

の仮 Project を作成して「LL-RF
PHY 間の Class 1 に関する階層間不整合が出ず、他の階層間不整合も

QDID [ID] と同じ TCW(Test
Case Waiver 対象項目 )」であることを確認しました。

この結果、もし御社が RF/RF PHY 試験レポートをエビデンスとして Core-Controller( 旧 Controller

Subsystem) の登録を希望される場合でも、 Subset
DN: [ID] で問題なく登録できることが確認できました。

以上よろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、 HM26 にて使用している [ID](QDID [ID]) にて DN [ID] が作成され、

Subset DN [ID]
も作成頂けた旨連絡頂いております。

Subset DN にて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

お忙しいところ何度もお手数おかけしてしまい申し訳ありません。

ご協力頂けますと幸いです。

/eom

From: Itsuo Sakai

Sent: Tuesday, September 24, 2024 5:21 PM

To: 大平ひとみ Hitomi Ohira ;
深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。
HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。
弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

⇒ 承知しました。ご連絡をお待ちしております。
尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては
HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset
DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host
subsystem/Profile subsystem の ICS
Details ですが、こちらについても HM23/26 共に A13
Profile Subsystem([ID])、 Host Subsystem
([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

⇒ Q 社の対応が確認でき、安心しました。

引き続きよろしくお願いいたいます。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo
Sakai ;
Hiroaki Fukaura

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては

HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host subsystem/Profile subsystem の ICS Details ですが、

こちらについても HM23/26 共に A13 Profile Subsystem([ID])、 Host Subsystem([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

取り急ぎご連絡まで。

/eom

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 4:04 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

⇒ 差分 ( 追加 ) 試験は可能です。しかし、本来その項目が必要な [ID] へは反映できません。
・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、
ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller Subsystem) ＋ [ID](Host
Subsystem) と [ID] (Profile

Subsystem) を更新した登録」では、 [ID]([ID]) を Include した取得した ICS そのものに RFPHY

/TRM/[ID] 試験が含まれますが、形式的に [ID]([ID]) の登録時点で当該試験項目はクリアしたものとして扱われます。

敢えて更新登録で RF PHY の ICS の任意の項目を修正 → 元に戻すと Test
Plan に RF PHY 階層の試験要求が出力されますので RFPHY/TRM/[ID] を差分試験を反映させることは可能ですが、 [ID](Host

Subsystem) と [ID](Profile
Subsystem) を更新した登録と [ID]([ID]) との階層間不整合のチェック対象となって [ID](Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録の機能次第ではリスクが発生します。（例えば更新した Host Subsystem 相当の登録が Isochronous

モードをサポート、あるいは AoA/AoD をサポートした場合です。）

ちなみに [ID]([ID]) に現状の [ID](Host
Subsystem) と [ID](Profile Subsystem) を Include

した登録で、 RF PHY を修正 → 元に戻すと階層間チェックが実施されて下記のように ScPP が不足という結果になります。 (Layer/ICS に一切手をいれなければ階層間不整合チェックは行われない )

<SCPP>

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、

ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 11:29 AM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ RF および RF
PHY レポートおよびログを受領しました。

私の Warkspace で RF と RF
PHY だけの仮 Project を作成し、 [ID] の RF と RF
PHY の ICS を入力して

[ID](2024/12/02 から必須 ) で Test
Plan を出力して受領した RF および RF
PHY レポートと逐次比較しました。

その結果 RF はレポートと一致するとともに、 [ID] および [ID] で追加される試験項目はありませんでした。

RF PHY は [ID] および [ID] で追加される試験項目はないものの、「RFPHY/TRM/[ID]」

がレポートに不足していました。この項目は [ID] で新設されたもので、 [ID] が登録された [ID] の 1 年以上前に必須項目でしたので、 BQTF の確認ミスと思われます。

しかし 6/30 以前の登録制度ではデザイン登録部分 ([ID] では Controller
Subsystem) に QDID:

[ID] が SIG から付与されて形式的に SIG の確認済になっています。したがってご依頼の「[ID]

(Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録」では QDID:[ID] を Include

し、全階層に対して ICS の変更・追加を行わなければ新たに RF
PHY の試験要求は発生しません。

言い換えれば敢えて RF PHY の「RFPHY/TRM/[ID]」を追加試験しなくても新登録サイトの登録過程で「形式上」は不都合が生じません。

立場上「RFPHY/TRM/[ID] の追加試験は不要」と断定的にアドバイスできないのですが、既に

[ID] は承認された登録ですので SIG からこの試験項目の不足を指摘される可能性は無いものと思います。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki
Fukaura

件名 : Re:
[ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ;
Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) - [ID]
(Component (Tested))
[ID] (Host Subsystem)
[ID] (Profile Subsystem)

Android OS の Update に伴い [ID]
(Host Subsystem) と [ID] (Profile Subsystem) が変更となり、
弊社では今後取得される新しい A Host-Core Configuration と X2Core
Layer(Profile Subsystem) を参照して End Product 登録を行う予定です。

⇒ ここまで理解しました。
[ID] は他社で試験をして登録したモデルではありますが、
Host Subsystem と Profile
Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

⇒ ありがとうございます。
そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。
本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？
(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

⇒ はい、他社レポートで問題ございません。
なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。
他に必要な情報がございましたらお申し付けください。

⇒ MH26 と同様、参照 (Include) 予定の新規登録の A
Host-Core Configuration と X2Core Layer(Profile

Subsystem) の DN(Design
Number) が判明しましたら階層間不整合を確認いたしますのでお知らせください。

テストレポートに関してですが、 2024/12/28 から有効になるプロファイルの試験項目が [ID] で予告されています。可能であければ早めにテストレポートをご提出いただければ 2024/12/28 以降に当該レポートがそのまま使えるかどうかを事前確認いたします。

以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun
Wang ;
Itsuo Sakai

件名 : [ALAP]
HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れました HM23 の Bluetooth SIG 認証について相談させてください。

HM23 は [ID] というモデルで、 [ID] で登録済みです。

End Product 登録で参照している QDID は以下です。

[ID] (Controller Subsystem) -
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OS の Update に伴い [ID] (Host
Subsystem) と [ID] (Profile Subsystem) が変更となり、

弊社では今後取得される新しい A Host-Core Configuration と X2Core Layer(Profile Subsystem) を参照して

End Product 登録を行う予定です。

[ID] は他社で試験をして登録したモデルではありますが、

Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、 HM26 にて使用している [ID](QDID [ID]) にて DN [ID] が作成され、

Subset DN [ID]
も作成頂けた旨連絡頂いております。

Subset DN にて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

お忙しいところ何度もお手数おかけしてしまい申し訳ありません。

ご協力頂けますと幸いです。

/eom

From: Itsuo Sakai

Sent: Tuesday, September 24, 2024 5:21 PM

To: 大平ひとみ Hitomi Ohira ;
深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。
HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。
弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

⇒ 承知しました。ご連絡をお待ちしております。
尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては
HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset
DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host
subsystem/Profile subsystem の ICS
Details ですが、こちらについても HM23/26 共に A13
Profile Subsystem([ID])、 Host Subsystem
([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

⇒ Q 社の対応が確認でき、安心しました。

引き続きよろしくお願いいたいます。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo
Sakai ;
Hiroaki Fukaura

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては

HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host subsystem/Profile subsystem の ICS Details ですが、

こちらについても HM23/26 共に A13 Profile Subsystem([ID])、 Host Subsystem([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

取り急ぎご連絡まで。

/eom

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 4:04 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

⇒ 差分 ( 追加 ) 試験は可能です。しかし、本来その項目が必要な [ID] へは反映できません。
・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、
ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller Subsystem) ＋ [ID](Host
Subsystem) と [ID] (Profile

Subsystem) を更新した登録」では、 [ID]([ID]) を Include した取得した ICS そのものに RFPHY

/TRM/[ID] 試験が含まれますが、形式的に [ID]([ID]) の登録時点で当該試験項目はクリアしたものとして扱われます。

敢えて更新登録で RF PHY の ICS の任意の項目を修正 → 元に戻すと Test
Plan に RF PHY 階層の試験要求が出力されますので RFPHY/TRM/[ID] を差分試験を反映させることは可能ですが、 [ID](Host

Subsystem) と [ID](Profile
Subsystem) を更新した登録と [ID]([ID]) との階層間不整合のチェック対象となって [ID](Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録の機能次第ではリスクが発生します。（例えば更新した Host Subsystem 相当の登録が Isochronous

モードをサポート、あるいは AoA/AoD をサポートした場合です。）

ちなみに [ID]([ID]) に現状の [ID](Host
Subsystem) と [ID](Profile Subsystem) を Include

した登録で、 RF PHY を修正 → 元に戻すと階層間チェックが実施されて下記のように ScPP が不足という結果になります。 (Layer/ICS に一切手をいれなければ階層間不整合チェックは行われない )

<SCPP>

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、

ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 11:29 AM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ RF および RF
PHY レポートおよびログを受領しました。

私の Warkspace で RF と RF
PHY だけの仮 Project を作成し、 [ID] の RF と RF
PHY の ICS を入力して

[ID](2024/12/02 から必須 ) で Test
Plan を出力して受領した RF および RF
PHY レポートと逐次比較しました。

その結果 RF はレポートと一致するとともに、 [ID] および [ID] で追加される試験項目はありませんでした。

RF PHY は [ID] および [ID] で追加される試験項目はないものの、「RFPHY/TRM/[ID]」

がレポートに不足していました。この項目は [ID] で新設されたもので、 [ID] が登録された [ID] の 1 年以上前に必須項目でしたので、 BQTF の確認ミスと思われます。

しかし 6/30 以前の登録制度ではデザイン登録部分 ([ID] では Controller
Subsystem) に QDID:

[ID] が SIG から付与されて形式的に SIG の確認済になっています。したがってご依頼の「[ID]

(Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録」では QDID:[ID] を Include

し、全階層に対して ICS の変更・追加を行わなければ新たに RF
PHY の試験要求は発生しません。

言い換えれば敢えて RF PHY の「RFPHY/TRM/[ID]」を追加試験しなくても新登録サイトの登録過程で「形式上」は不都合が生じません。

立場上「RFPHY/TRM/[ID] の追加試験は不要」と断定的にアドバイスできないのですが、既に

[ID] は承認された登録ですので SIG からこの試験項目の不足を指摘される可能性は無いものと思います。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki
Fukaura

件名 : Re:
[ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ;
Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) - [ID]
(Component (Tested))
[ID] (Host Subsystem)
[ID] (Profile Subsystem)

Android OS の Update に伴い [ID]
(Host Subsystem) と [ID] (Profile Subsystem) が変更となり、
弊社では今後取得される新しい A Host-Core Configuration と X2Core
Layer(Profile Subsystem) を参照して End Product 登録を行う予定です。

⇒ ここまで理解しました。
[ID] は他社で試験をして登録したモデルではありますが、
Host Subsystem と Profile
Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

⇒ ありがとうございます。
そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。
本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？
(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

⇒ はい、他社レポートで問題ございません。
なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。
他に必要な情報がございましたらお申し付けください。

⇒ MH26 と同様、参照 (Include) 予定の新規登録の A
Host-Core Configuration と X2Core Layer(Profile

Subsystem) の DN(Design
Number) が判明しましたら階層間不整合を確認いたしますのでお知らせください。

テストレポートに関してですが、 2024/12/28 から有効になるプロファイルの試験項目が [ID] で予告されています。可能であければ早めにテストレポートをご提出いただければ 2024/12/28 以降に当該レポートがそのまま使えるかどうかを事前確認いたします。

以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun
Wang ;
Itsuo Sakai

件名 : [ALAP]
HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れました HM23 の Bluetooth SIG 認証について相談させてください。

HM23 は [ID] というモデルで、 [ID] で登録済みです。

End Product 登録で参照している QDID は以下です。

[ID] (Controller Subsystem) -
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OS の Update に伴い [ID] (Host
Subsystem) と [ID] (Profile Subsystem) が変更となり、

弊社では今後取得される新しい A Host-Core Configuration と X2Core Layer(Profile Subsystem) を参照して

End Product 登録を行う予定です。

[ID] は他社で試験をして登録したモデルではありますが、

Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

---

## 2. 2025-01-23 06:28

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
先程Submitを完了しました。
SIGから連絡が入り次第、登録完了or Rejectいずれの場合も酒井様にご連絡いたします。

⇒問題ないとは思いますが念のため結果をご連絡ください。
ところで新システムの概念について私はまだよく理解できていないのですが、
当初行おうとしていたES-25636を参照してテストレポートを提出する登録方法に対して、
後から行ったES-25802を参照したTCWによる登録というものは、どのような違いがあるのでしょうか？
(先の方法ではSIG管理者の確認ではなくシステムによる自動判定なのでしょうか？)

⇒TCWはConsistency CheckでInvalid結果が出た場合に、SIGが定める内容であれば新規登録を許容するという運用で、最初のアドバイスの登録手順では3項目のInvalid内容がES-25636適用対象でしたが、

BLEプロファイル削除が予期していないWR/BERのIOPT試験要求発生となりました。ES-25636適用自体は登録に支障ないのですが試験要求発生の際にはそのレポートをアップロードしないと登録できないため、試験要求が発生しない&quot;Combine Unmodefied Design&quot;によるInvalidに適用されるICWがないか探して、BAPのInvalidに関するTCW:[ID](昨年秋にはなかった)を見つけてその適用による登録手順をアドバイスしました。通常InvalidはICS変更で解消しないと登録できませんが「ICSを変更したプロトコル・プロファイルのPTS試験要求」が発生しますのでこの方法でInvalidを解消することは大事になります。前回のURLに数種類のTCWの適用範囲が簡単に説明されていますが、Invalidaが発生しても、いずれかのTCWに合致すれば対応するICW番号を入力することで登録が許容されます。

7/1以降、代行登録も追加試験を発生させないために様々な手順を試す模索の繰り返しです。今回の御社のケースが特段登録内容に問題があるとか特殊であるという事例ではありません。

以上回答いたします。

差出人: Hiroaki Fukaura

送信日時: 2025年1月23日 15:01

宛先: Itsuo Sakai

件名: RE: [HM23登録方法変更のお願い] Re: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

再度のご確認ならびに詳細な手続き方法をご説明いただきありがとうございます。

先程 Submit を完了しました。

SIG から連絡が入り次第、登録完了 or Reject いずれの場合も酒井様にご連絡いたします。

ところで新システムの概念について私はまだよく理解できていないのですが、

当初行おうとしていた [ID] を参照してテストレポートを提出する登録方法に対して、

後から行った [ID] を参照した TCW による登録というものは、どのような違いがあるのでしょうか？

( 先の方法では SIG 管理者の確認ではなくシステムによる自動判定なのでしょうか？ )

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, January 22, 2025 10:08 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: [HM23 登録方法変更のお願い ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
Core 階層 ICS のチェックを修正することで Consistency
Check の結果がご提示いただいた 3 項目となり、
進めることができました。

その次の Step のテストレポートのアップロードが何度試しても処理中から進まないため完了はできておりませんが、明日改めて試してみます。

⇒ 私がアドバイスした「LE AUdio
Profile」を削除する方法では、これまで経験のない添付の 86 項目もの IOPT 試験要求が発生するシステムに改変さています。 IOPT 試験は SDP で対向機器のサポートプロファイルを確認する BR/EDR プロファイルだけが対象ですので LE
Profile の改変は関係ないはずです。テストレポートのアップロードが何度試しても処理中から進まないのは、おそらくこの試験要求のテストレポートを待っているからかと推測します。

そこで何とか &quot;Combine unmodified Designs&quot; で進む方法はないか色々調べて試した結果、 BAP に関する TCW:[ID] が使えそうです。

下記手順で登録を進めてください。

(1)
[URL] でログインし、下記 URL で登録操作中の Draft
Products を開いてください。

(2) Product Detail ページが開きますので右下の [Save
and got to Specify the Design] をクリック

(3) [ID] の右のＸで削除後、再度 [ID] を入力し、 [I'm
finished entering DNs] をクリックし、

[Combine unmodefied Designs] をクリックし、 [Perform
consistency Check] をクリック。

(4)
下図が表示されるので [Apply TCW] をクリックし開いた入力欄に
[ID] を入力後、右下の

[Save and goto Test Plan and Documentation] をクリック

(5)
下図のように No test plan is generated - -
と表示される。

右下の [Save and goto Qulification Fee] をクリック後、 Recipt
Number を選択して右下の

[Save and go to Submission] をクリックし、 &quot;ICS
Form&quot; が黄色である以外は Status 欄が緑の □ 表示出ることを確認して下方の確認欄にチェックし、 Listing
Owner の英文名を署名欄に入力後 [Complete the Submission] をクリックして Submission を行ってください。

(6) TCW による登録のため SIG 管理者の確認んのめ 2-3 営業日後に登録が承認されます。却下の場合はその旨 Email が届き、 Recipt
Number とともに Drft Pridcut 一覧へ差し戻されます。この場合にはそのメールを私に転送してご連絡ください。

以上よろしくお願いいたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2025 年 1 月 22 日
17:07

宛先 :
Itsuo Sakai

件名 :
RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

Core 階層 ICS のチェックを修正することで Consistency Check の結果がご提示いただいた 3 項目となり、進めることができました。

その次の Step のテストレポートのアップロードが何度試しても処理中から進まないため完了はできておりませんが、明日改めて試してみます。

ありがとうございました。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, January 22, 2025 1:22 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

「(4) Core 階層の ICS
10/1 のチェックを外し、」が記載ミスで正しくは「Core 階層の ICS
12/1 のチェックを外し」です。申し訳ありませんでした。

対応方法としては、 ICS Selection で
Core 10/1 をチェックし、 Core 12/1 のチェックを外して再度

Consistency Check を行ってください。

以上よろしくお願いいたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2025 年 1 月 22 日
13:10

宛先 :
Itsuo Sakai

件名 :
RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

特別サポートのご提案、並びに詳細な登録方法のアドバイスをいただきありがとうございます。

ご連絡いただいた手順で進めましたが、 (4) の Consistency Check 後に表示される結果が 3 項目であるべきところ 5 項目表示されました。

酒井様ご提示の３項目に加え、以下の 2 項目が表示されています。

―――

CORE

12:C.1 | If [CORE] (12/1) is Supported then it is Mandatory to Support at least one of [CORE] (12/2-3)

SEC

SEC > CORE | If [CORE] (10/1) is Not Supported then [SEC] is Excluded Go to Layer Selection.

―――

お手数おかけしますが、記入内容が正しいかチェックしていただけないでしょうか？

画面キャプチャしましたので添付ファイルをご参照願います。

追加サポートについて有償となる場合は弊社内で承認を得るため、お見積書の発行をお願いいたします。

また以降同様の案件については代行登録を発注しての対応となることを承知いたしました。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, January 21, 2025 5:18 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

お問い合わせの内容は、 Include 先の登録内容や登録製品のサポート機能によって個々に異なる対応が必要で代行登録と同じ手間が発生するため、本来は「代行登録をご依頼ください」という対応となります。しかし、御社からは MH26 や新田様案件などをご依頼いただいていますので特別にサポートさせていただきます。以下の手順で登録できることを確認しました。

(1) [ID]
と [ID]
を Include 後、 [Modefy
or Add to this set of Design] をクリック ( 下図 )。

(2)
右下の [Save and go to Layer Selection] をクリック。

(3) Layer Selection ページで Core
Layers から HCI
と UHCI
のチェックをはずし、 LE Audio Spec からすべてのプロトコル・プロファイルのチェックを外して右下の [Save and go to ICS Selection] をクリック

(4) Core 階層の ICS
10/1 のチェックを外し、右上の [Consistency Check] をクリック。結果が下記

3 項目であることを確認後、下部の [Test
Coverage Waiver(s)] に [ID]( 下図 ) を入力後右下の

[Save and go to Test Plan and Documentation] をクリック。その後のページは記載内容に従って所定の入力などを行い、最後のページまで進む。 .

ーーー

BB

If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

GAP

4b:Prerequisite | If [GATT] (1a/4) is Supported then [GAP] (4b/1-2) are Mandatory

ーーー以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2025 年 1 月 21 日
16:08

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

下記、間が空いてしまいましたが弊社 HM23 の Android14 登録についてアドバイスいただけないでしょうか。

弊社大平より、
この後、 Host subsystem、 Profile subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

と説明いたしましたが、 Qualcomm 社から Host と Profile を統合した「QDID/DN : [ID]」の登録完了連絡を受けました。

そこで、 Core_Host and Profiles Qualification: [ID] と Controller Subsystem: [ID] (HM23 A13 から変更なし ) で登録を試みたところ

Consistency Check で添付画像のエラーが出てしまいました。

これは酒井様のご説明にある“ QDID:[ID] から RF/RF PHY 階層を選択する”事により回避可能でしょうか？

試しに「Modify Layers of your Disign manually」を選択して進めてみたところ、エラーにある BAP は LE で選択されていましたが

BASS は選択されていないようでした。

またそのいずれも変更を加えようとすると新しい Ver が適用されるというような警告が表示されました。

もし階層選択によりエラーを無くせるようなら、手順を教えていただけないでしょうか？

大変お手数おかけしますがよろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, October 31, 2024 9:51 AM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
この後、 Host subsystem、 Profile
subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

⇒ 承知しました。
また、ご指摘頂いております RF 試験 1 項目の追加実施につきまして、
先日王君様より概算見積をご提示頂いております。

⇒ 試験項目の不足に関して再度精査しました。当該不足項目は [ID] で追加されて発効が 2022/12/28 でした。従って御社の QDID:[ID](Controller
Subsystem / Listing Date

:[ID]) および展開いただいた SGS 台湾での RF/RF
PHY レポートに含まれていなくても

QDID:[ID] の登録に関しては認証規定上の問題はありません。

しかし、 新規に「当該 RF/RF PHY レポートをエビデンスとした登録を行と不足項目が問題」となります。 ( 以前問題ありと連絡を差し上げた内容です。 )

そこで提案ですが、 QDID:[ID] は Controller
Subsystem 登録ですので現在も引き続き有効なため、これと Q 社の Subset
DN [ID] を Include して、 QDID:[ID] から RF/RF
PHY 階層を選択するとともに DN [ID] から残りの階層を選択すると「認証規定に準拠して」 2022/04/20 当時に有効であった RF/RF PHY およびそのエビデンスを引き継ぐことが可能です。この部分組み合わせ登録手順は 7/1 の新登録サイトで可能となったもので、こうすることで不足項目試験を実施すること無く「認証規定に準拠した」 HM23 登録を進めることが可能です。

以上ご検討ください。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 10 月 30 日 13:49

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早々にご確認頂きありがとうございます。

作成頂いた「Subset DN [ID]」にて問題にないとのこと、承知致しました。

この後、 Host subsystem、 Profile subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

また、ご指摘頂いております RF 試験 1 項目の追加実施につきまして、

先日王君様より概算見積をご提示頂いております。

参考にさせて頂き対応方法等決定しましたら改めてご連絡させて頂きます。

/eom

From: Itsuo Sakai

Sent: Wednesday, October 30, 2024 12:10 PM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
HM23 にて使用している [ID](QDID
[ID]) につきまして、
先日追加にて AoA/AoD 機能削除必要とのことでアドバイス頂いておりました件、
Qualcomm より本件対応完了とのことで連絡がされております。

⇒ ご連絡ありがとうございます。
酒井様よりご教示頂きました通り、 SIG にて以下について削除となっている旨確認はしておりますが、本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

⇒ 私の Workspace で仮 Project を作成して「N
[ID]」で問題解消したことを確認できました。

引き続きよろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 10 月 30 日 11:36

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To.
アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。度々申し訳ありません。

削除追加にて連絡されている subset DN は以下の通りとなります。

先のメールにて記載漏れており申し訳ありません。

ご確認の程よろしくお願い致します。
Subset DN [ID] was created from QDID [ID], [ID] Controller listing.

/eom

From:
大平ひとみ Hitomi Ohira

Sent: Wednesday, October 30, 2024 11:32 AM

To: Itsuo Sakai

Subject: RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To.
アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23 にて使用している [ID](QDID [ID]) につきまして、

先日追加にて AoA/AoD 機能削除必要とのことでアドバイス頂いておりました件、

Qualcomm より本件対応完了とのことで連絡がされております。

Update the subset DN [ID] for [ID] (delete AoA/AoD capabilities from LL)

酒井様よりご教示頂きました通り、 SIG にて以下について削除となっている旨確認はしておりますが、

本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

お忙しいところお手数おかけし申し訳ありません。

ご協力の程よろしくお願い致します。

→ [LL] (9/17):NO

→ [LL] (9/20):NO

→ [LL] (9/21):NO

→ [LL] (9/23):NO

→ [LL] (9/24):NO

/eom

From: Itsuo Sakai

Sent: Monday, September 30, 2024 7:49 PM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
HM23 にして使用している [ID](QDID
[ID]) につきましても
Power Class1 サポート削除にて Subset
DN [ID] が登録されたとのことで連絡がされました。

お忙しいところ大変恐縮ではございますが、こちらにつきましても先日の HM26 と同様に懸念点解消となっているかご確認頂くことは可能でしょうか？

⇒ Qualification Warkspace で仮 Project を作って確認しました結果、 DN:[ID] は確かに LL
9/11 LE

Power Class 1: NO と修正されて RF
PHY 1/15:NO との階層間不整合は消えました。しかし先日ご送付いただいたベースモデルの RF PHY テストレポート記載の RF
PHY ICS と、 DN [ID] の

LL 階層間に以下の 5 件の不整合 (AoA/AoD の関連 ) が発生します。

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/17) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/20) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/13) is Not Supported then [LL] (9/23) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/14) is Not Supported then [LL] (9/24) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/12) is Not Supported then [LL] (9/21) is Excluded

Q 社には「Subset
DN [ID] から LL の AoA/AoD 機能を削除 ([LL]
(9/17):NO、 [LL] (9/20):NO、

[LL] (9/21):NO、 [LL]
(9/23):NO、 [LL] (9/24):NO) した Subset
DN を作成してほしい。」と再度依頼してください。

以上回答いたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 30 日 11:56

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23 にして使用している [ID](QDID [ID]) につきましても

Power Class1 サポート削除にて Subset DN [ID]
が登録されたとのことで連絡がされました。

お忙しいところ大変恐縮ではございますが、こちらにつきましても先日の HM26 と同様に懸念点解消となっているかご確認頂くことは可能でしょうか？

上記ご協力頂けますと幸いです。

よろしくお願い致します。

/eom

From: Itsuo Sakai

Sent: Wednesday, September 25, 2024 4:08 PM

To: 大平ひとみ Hitomi Ohira

Subject: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
早速ですが、 HM26 にて使用している [ID](QDID
[ID]) にて DN [ID] が作成され、
Subset DN [ID]
も作成頂けた旨連絡頂いております。
Subset DN にて「9/11
LE Power Class 1」のサポートが削除されている旨も確認致しましたが、
取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

⇒ [ID](QDID [ID]) の Subset
DN: [ID] での HM26 の登録可能性を私の Quaification
Workspace

の仮 Project を作成して「LL-RF
PHY 間の Class 1 に関する階層間不整合が出ず、他の階層間不整合も

QDID [ID] と同じ TCW(Test
Case Waiver 対象項目 )」であることを確認しました。

この結果、もし御社が RF/RF PHY 試験レポートをエビデンスとして Core-Controller( 旧 Controller

Subsystem) の登録を希望される場合でも、 Subset
DN: [ID] で問題なく登録できることが確認できました。

以上よろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、 HM26 にて使用している [ID](QDID [ID]) にて DN [ID] が作成され、

Subset DN [ID]
も作成頂けた旨連絡頂いております。

Subset DN にて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

お忙しいところ何度もお手数おかけしてしまい申し訳ありません。

ご協力頂けますと幸いです。

/eom

From: Itsuo Sakai

Sent: Tuesday, September 24, 2024 5:21 PM

To: 大平ひとみ Hitomi Ohira ;
深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。
HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。
弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

⇒ 承知しました。ご連絡をお待ちしております。
尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては
HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset
DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host
subsystem/Profile subsystem の ICS
Details ですが、こちらについても HM23/26 共に A13
Profile Subsystem([ID])、 Host Subsystem
([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

⇒ Q 社の対応が確認でき、安心しました。

引き続きよろしくお願いいたいます。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo
Sakai ;
Hiroaki Fukaura

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては

HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host subsystem/Profile subsystem の ICS Details ですが、

こちらについても HM23/26 共に A13 Profile Subsystem([ID])、 Host Subsystem([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

取り急ぎご連絡まで。

/eom

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 4:04 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

⇒ 差分 ( 追加 ) 試験は可能です。しかし、本来その項目が必要な [ID] へは反映できません。
・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、
ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller Subsystem) ＋ [ID](Host
Subsystem) と [ID] (Profile

Subsystem) を更新した登録」では、 [ID]([ID]) を Include した取得した ICS そのものに RFPHY

/TRM/[ID] 試験が含まれますが、形式的に [ID]([ID]) の登録時点で当該試験項目はクリアしたものとして扱われます。

敢えて更新登録で RF PHY の ICS の任意の項目を修正 → 元に戻すと Test
Plan に RF PHY 階層の試験要求が出力されますので RFPHY/TRM/[ID] を差分試験を反映させることは可能ですが、 [ID](Host

Subsystem) と [ID](Profile
Subsystem) を更新した登録と [ID]([ID]) との階層間不整合のチェック対象となって [ID](Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録の機能次第ではリスクが発生します。（例えば更新した Host Subsystem 相当の登録が Isochronous

モードをサポート、あるいは AoA/AoD をサポートした場合です。）

ちなみに [ID]([ID]) に現状の [ID](Host
Subsystem) と [ID](Profile Subsystem) を Include

した登録で、 RF PHY を修正 → 元に戻すと階層間チェックが実施されて下記のように ScPP が不足という結果になります。 (Layer/ICS に一切手をいれなければ階層間不整合チェックは行われない )

<SCPP>

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、

ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 11:29 AM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ RF および RF
PHY レポートおよびログを受領しました。

私の Warkspace で RF と RF
PHY だけの仮 Project を作成し、 [ID] の RF と RF
PHY の ICS を入力して

[ID](2024/12/02 から必須 ) で Test
Plan を出力して受領した RF および RF
PHY レポートと逐次比較しました。

その結果 RF はレポートと一致するとともに、 [ID] および [ID] で追加される試験項目はありませんでした。

RF PHY は [ID] および [ID] で追加される試験項目はないものの、「RFPHY/TRM/[ID]」

がレポートに不足していました。この項目は [ID] で新設されたもので、 [ID] が登録された [ID] の 1 年以上前に必須項目でしたので、 BQTF の確認ミスと思われます。

しかし 6/30 以前の登録制度ではデザイン登録部分 ([ID] では Controller
Subsystem) に QDID:

[ID] が SIG から付与されて形式的に SIG の確認済になっています。したがってご依頼の「[ID]

(Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録」では QDID:[ID] を Include

し、全階層に対して ICS の変更・追加を行わなければ新たに RF
PHY の試験要求は発生しません。

言い換えれば敢えて RF PHY の「RFPHY/TRM/[ID]」を追加試験しなくても新登録サイトの登録過程で「形式上」は不都合が生じません。

立場上「RFPHY/TRM/[ID] の追加試験は不要」と断定的にアドバイスできないのですが、既に

[ID] は承認された登録ですので SIG からこの試験項目の不足を指摘される可能性は無いものと思います。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki
Fukaura

件名 : Re:
[ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ;
Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) - [ID]
(Component (Tested))
[ID] (Host Subsystem)
[ID] (Profile Subsystem)

Android OS の Update に伴い [ID]
(Host Subsystem) と [ID] (Profile Subsystem) が変更となり、
弊社では今後取得される新しい A Host-Core Configuration と X2Core
Layer(Profile Subsystem) を参照して End Product 登録を行う予定です。

⇒ ここまで理解しました。
[ID] は他社で試験をして登録したモデルではありますが、
Host Subsystem と Profile
Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

⇒ ありがとうございます。
そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。
本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？
(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

⇒ はい、他社レポートで問題ございません。
なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。
他に必要な情報がございましたらお申し付けください。

⇒ MH26 と同様、参照 (Include) 予定の新規登録の A
Host-Core Configuration と X2Core Layer(Profile

Subsystem) の DN(Design
Number) が判明しましたら階層間不整合を確認いたしますのでお知らせください。

テストレポートに関してですが、 2024/12/28 から有効になるプロファイルの試験項目が [ID] で予告されています。可能であければ早めにテストレポートをご提出いただければ 2024/12/28 以降に当該レポートがそのまま使えるかどうかを事前確認いたします。

以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun
Wang ;
Itsuo Sakai

件名 : [ALAP]
HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れました HM23 の Bluetooth SIG 認証について相談させてください。

HM23 は [ID] というモデルで、 [ID] で登録済みです。

End Product 登録で参照している QDID は以下です。

[ID] (Controller Subsystem) -
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OS の Update に伴い [ID] (Host
Subsystem) と [ID] (Profile Subsystem) が変更となり、

弊社では今後取得される新しい A Host-Core Configuration と X2Core Layer(Profile Subsystem) を参照して

End Product 登録を行う予定です。

[ID] は他社で試験をして登録したモデルではありますが、

Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、 HM26 にて使用している [ID](QDID [ID]) にて DN [ID] が作成され、

Subset DN [ID]
も作成頂けた旨連絡頂いております。

Subset DN にて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

お忙しいところ何度もお手数おかけしてしまい申し訳ありません。

ご協力頂けますと幸いです。

/eom

From: Itsuo Sakai

Sent: Tuesday, September 24, 2024 5:21 PM

To: 大平ひとみ Hitomi Ohira ;
深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。
HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。
弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

⇒ 承知しました。ご連絡をお待ちしております。
尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては
HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset
DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host
subsystem/Profile subsystem の ICS
Details ですが、こちらについても HM23/26 共に A13
Profile Subsystem([ID])、 Host Subsystem
([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

⇒ Q 社の対応が確認でき、安心しました。

引き続きよろしくお願いいたいます。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo
Sakai ;
Hiroaki Fukaura

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては

HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host subsystem/Profile subsystem の ICS Details ですが、

こちらについても HM23/26 共に A13 Profile Subsystem([ID])、 Host Subsystem([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

取り急ぎご連絡まで。

/eom

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 4:04 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

⇒ 差分 ( 追加 ) 試験は可能です。しかし、本来その項目が必要な [ID] へは反映できません。
・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、
ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller Subsystem) ＋ [ID](Host
Subsystem) と [ID] (Profile

Subsystem) を更新した登録」では、 [ID]([ID]) を Include した取得した ICS そのものに RFPHY

/TRM/[ID] 試験が含まれますが、形式的に [ID]([ID]) の登録時点で当該試験項目はクリアしたものとして扱われます。

敢えて更新登録で RF PHY の ICS の任意の項目を修正 → 元に戻すと Test
Plan に RF PHY 階層の試験要求が出力されますので RFPHY/TRM/[ID] を差分試験を反映させることは可能ですが、 [ID](Host

Subsystem) と [ID](Profile
Subsystem) を更新した登録と [ID]([ID]) との階層間不整合のチェック対象となって [ID](Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録の機能次第ではリスクが発生します。（例えば更新した Host Subsystem 相当の登録が Isochronous

モードをサポート、あるいは AoA/AoD をサポートした場合です。）

ちなみに [ID]([ID]) に現状の [ID](Host
Subsystem) と [ID](Profile Subsystem) を Include

した登録で、 RF PHY を修正 → 元に戻すと階層間チェックが実施されて下記のように ScPP が不足という結果になります。 (Layer/ICS に一切手をいれなければ階層間不整合チェックは行われない )

<SCPP>

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、

ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 11:29 AM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ RF および RF
PHY レポートおよびログを受領しました。

私の Warkspace で RF と RF
PHY だけの仮 Project を作成し、 [ID] の RF と RF
PHY の ICS を入力して

[ID](2024/12/02 から必須 ) で Test
Plan を出力して受領した RF および RF
PHY レポートと逐次比較しました。

その結果 RF はレポートと一致するとともに、 [ID] および [ID] で追加される試験項目はありませんでした。

RF PHY は [ID] および [ID] で追加される試験項目はないものの、「RFPHY/TRM/[ID]」

がレポートに不足していました。この項目は [ID] で新設されたもので、 [ID] が登録された [ID] の 1 年以上前に必須項目でしたので、 BQTF の確認ミスと思われます。

しかし 6/30 以前の登録制度ではデザイン登録部分 ([ID] では Controller
Subsystem) に QDID:

[ID] が SIG から付与されて形式的に SIG の確認済になっています。したがってご依頼の「[ID]

(Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録」では QDID:[ID] を Include

し、全階層に対して ICS の変更・追加を行わなければ新たに RF
PHY の試験要求は発生しません。

言い換えれば敢えて RF PHY の「RFPHY/TRM/[ID]」を追加試験しなくても新登録サイトの登録過程で「形式上」は不都合が生じません。

立場上「RFPHY/TRM/[ID] の追加試験は不要」と断定的にアドバイスできないのですが、既に

[ID] は承認された登録ですので SIG からこの試験項目の不足を指摘される可能性は無いものと思います。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki
Fukaura

件名 : Re:
[ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ;
Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) - [ID]
(Component (Tested))
[ID] (Host Subsystem)
[ID] (Profile Subsystem)

Android OS の Update に伴い [ID]
(Host Subsystem) と [ID] (Profile Subsystem) が変更となり、
弊社では今後取得される新しい A Host-Core Configuration と X2Core
Layer(Profile Subsystem) を参照して End Product 登録を行う予定です。

⇒ ここまで理解しました。
[ID] は他社で試験をして登録したモデルではありますが、
Host Subsystem と Profile
Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

⇒ ありがとうございます。
そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。
本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？
(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

⇒ はい、他社レポートで問題ございません。
なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。
他に必要な情報がございましたらお申し付けください。

⇒ MH26 と同様、参照 (Include) 予定の新規登録の A
Host-Core Configuration と X2Core Layer(Profile

Subsystem) の DN(Design
Number) が判明しましたら階層間不整合を確認いたしますのでお知らせください。

テストレポートに関してですが、 2024/12/28 から有効になるプロファイルの試験項目が [ID] で予告されています。可能であければ早めにテストレポートをご提出いただければ 2024/12/28 以降に当該レポートがそのまま使えるかどうかを事前確認いたします。

以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun
Wang ;
Itsuo Sakai

件名 : [ALAP]
HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れました HM23 の Bluetooth SIG 認証について相談させてください。

HM23 は [ID] というモデルで、 [ID] で登録済みです。

End Product 登録で参照している QDID は以下です。

[ID] (Controller Subsystem) -
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OS の Update に伴い [ID] (Host
Subsystem) と [ID] (Profile Subsystem) が変更となり、

弊社では今後取得される新しい A Host-Core Configuration と X2Core Layer(Profile Subsystem) を参照して

End Product 登録を行う予定です。

[ID] は他社で試験をして登録したモデルではありますが、

Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

---

## 3. 2025-01-23 09:15

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
SIGから早速登録完了の通知が届きました。サポートいただきありがとうございました。

⇒登録完了通知受取とのことで安心しました。(それにしても早いですね。)
また今回行った対応についてのご説明、ありがとうございます。
どのような申請を行ったのかという概要についてはなんとか理解できました。
新システムでの製品登録には今まで以上にBluetoothの構成(規格仕様と製品仕様)への理解が必要と感じました。
旧システムにおける登録済みQDIDを参照する製品登録であれば(表現は適切ではないかもしれませんが)
ある意味事務手続きのような感覚で登録出来てしまっていたものが、今後は実態に即した正確な登録が求められて格段に難易度が上がった印象を抱いています。

⇒理解すべき要点を一言で言えば旧制度ではConsisitency Check対象外の扱いでController Subsystem,

Host Subsytem, Profie Subsystem, End Productの組み合わせ指定(全体でも,Compnent参照との組み合わせでも)による登録が可能でした。それが「登録済みQDIDを参照する製品登録は事務手続のような感覚で登録出来てしまっていた」理由です。

一方、新制度では全階層を網羅したConsistency Checkに通らないと登録が完結しないように変更されたことに起因して階層間不整合が多発し、最も安易なICS変更によるInvalid解消を行うと当該階層の全試験項目の試験要求が出力されてそのレポートアップロードを行わないと登録できなくなりました。

ご印象どおり、新制度で追加試験を避けて旧制度と同じ内容の登録を行うことの難易度は飛躍的に増大しました。
従来自社対応していた製品登録のうち単純なモデル追加を除くものについては、登録代行を依頼する機会も出てきそうです。

⇒自社対応でも問題が発生しないのは、既存End Product/Core Complete登録1件をIncludeした登録で、

参照登録自体にInvalidを含まない限り旧制度と同じ感覚で製品登録が可能です。既存登録を2件以上

Includeする登録はまずご自身のQualification Workspaceで試してみて、手に負えなさそうな場合には代行登録をご検討ください。
関連して色々と質問させていただく事があると思いますが、今後ともよろしくお願いいたします。

⇒承知しました。お気軽にお尋ねください。

以上回答いたします。

差出人: Hiroaki Fukaura

送信日時: 2025年1月23日 16:28

宛先: Itsuo Sakai

件名: RE: [HM23登録方法変更のお願い] Re: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

SIG から早速登録完了の通知が届きました。サポートいただきありがとうございました。

また今回行った対応についてのご説明、ありがとうございます。

どのような申請を行ったのかという概要についてはなんとか理解できました。

新システムでの製品登録には今まで以上に Bluetooth の構成 ( 規格仕様と製品仕様 ) への理解が必要と感じました。

旧システムにおける登録済み QDID を参照する製品登録であれば ( 表現は適切ではないかもしれませんが ) ある意味事務手続きのような感覚で登録出来てしまっていたものが、今後は実態に即した正確な登録が求められて格段に難易度が上がった印象を抱いています。

従来自社対応していた製品登録のうち単純なモデル追加を除くものについては、登録代行を依頼する機会も出てきそうです。

関連して色々と質問させていただく事があると思いますが、今後ともよろしくお願いいたします。

以上です。

From: Itsuo Sakai

Sent: Thursday, January 23, 2025 3:28 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [HM23 登録方法変更のお願い ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
先程 Submit を完了しました。
SIG から連絡が入り次第、登録完了 or
Reject いずれの場合も酒井様にご連絡いたします。

⇒ 問題ないとは思いますが念のため結果をご連絡ください。
ところで新システムの概念について私はまだよく理解できていないのですが、
当初行おうとしていた [ID] を参照してテストレポートを提出する登録方法に対して、
後から行った [ID] を参照した TCW による登録というものは、どのような違いがあるのでしょうか？
( 先の方法では SIG 管理者の確認ではなくシステムによる自動判定なのでしょうか？ )

⇒ TCW は Consistency
Check で Invalid 結果が出た場合に、 SIG が定める内容であれば新規登録を許容するという運用で、最初のアドバイスの登録手順では 3 項目の Invalid 内容が [ID] 適用対象でしたが、

BLE プロファイル削除が予期していない WR/BER の IOPT 試験要求発生となりました。 [ID] 適用自体は登録に支障ないのですが試験要求発生の際にはそのレポートをアップロードしないと登録できないため、試験要求が発生しない &quot;Combine Unmodefied Design&quot; による Invalid に適用される ICW がないか探して、 BAP の Invalid に関する TCW:[ID]( 昨年秋にはなかった ) を見つけてその適用による登録手順をアドバイスしました。通常 Invalid は ICS 変更で解消しないと登録できませんが「ICS を変更したプロトコル・プロファイルの PTS 試験要求」が発生しますのでこの方法で Invalid を解消することは大事になります。前回の URL に数種類の TCW の適用範囲が簡単に説明されていますが、 Invalida が発生しても、いずれかの TCW に合致すれば対応する ICW 番号を入力することで登録が許容されます。

7/1 以降、代行登録も追加試験を発生させないために様々な手順を試す模索の繰り返しです。今回の御社のケースが特段登録内容に問題があるとか特殊であるという事例ではありません。

以上回答いたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2025 年 1 月 23 日
15:01

宛先 :
Itsuo Sakai

件名 :
RE: [HM23 登録方法変更のお願い ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

再度のご確認ならびに詳細な手続き方法をご説明いただきありがとうございます。

先程 Submit を完了しました。

SIG から連絡が入り次第、登録完了 or Reject いずれの場合も酒井様にご連絡いたします。

ところで新システムの概念について私はまだよく理解できていないのですが、

当初行おうとしていた [ID] を参照してテストレポートを提出する登録方法に対して、

後から行った [ID] を参照した TCW による登録というものは、どのような違いがあるのでしょうか？

( 先の方法では SIG 管理者の確認ではなくシステムによる自動判定なのでしょうか？ )

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, January 22, 2025 10:08 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: [HM23 登録方法変更のお願い ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
Core 階層 ICS のチェックを修正することで Consistency
Check の結果がご提示いただいた 3 項目となり、
進めることができました。

その次の Step のテストレポートのアップロードが何度試しても処理中から進まないため完了はできておりませんが、明日改めて試してみます。

⇒ 私がアドバイスした「LE AUdio
Profile」を削除する方法では、これまで経験のない添付の 86 項目もの IOPT 試験要求が発生するシステムに改変さています。 IOPT 試験は SDP で対向機器のサポートプロファイルを確認する BR/EDR プロファイルだけが対象ですので LE
Profile の改変は関係ないはずです。テストレポートのアップロードが何度試しても処理中から進まないのは、おそらくこの試験要求のテストレポートを待っているからかと推測します。

そこで何とか &quot;Combine unmodified Designs&quot; で進む方法はないか色々調べて試した結果、 BAP に関する TCW:[ID] が使えそうです。

下記手順で登録を進めてください。

(1)
[URL] でログインし、下記 URL で登録操作中の Draft
Products を開いてください。

(2) Product Detail ページが開きますので右下の [Save
and got to Specify the Design] をクリック

(3) [ID] の右のＸで削除後、再度 [ID] を入力し、 [I'm
finished entering DNs] をクリックし、

[Combine unmodefied Designs] をクリックし、 [Perform
consistency Check] をクリック。

(4)
下図が表示されるので [Apply TCW] をクリックし開いた入力欄に
[ID] を入力後、右下の

[Save and goto Test Plan and Documentation] をクリック

(5)
下図のように No test plan is generated - -
と表示される。

右下の [Save and goto Qulification Fee] をクリック後、 Recipt
Number を選択して右下の

[Save and go to Submission] をクリックし、 &quot;ICS
Form&quot; が黄色である以外は Status 欄が緑の □ 表示出ることを確認して下方の確認欄にチェックし、 Listing
Owner の英文名を署名欄に入力後 [Complete the Submission] をクリックして Submission を行ってください。

(6) TCW による登録のため SIG 管理者の確認んのめ 2-3 営業日後に登録が承認されます。却下の場合はその旨 Email が届き、 Recipt
Number とともに Drft Pridcut 一覧へ差し戻されます。この場合にはそのメールを私に転送してご連絡ください。

以上よろしくお願いいたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2025 年 1 月 22 日
17:07

宛先 :
Itsuo Sakai

件名 :
RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

Core 階層 ICS のチェックを修正することで Consistency Check の結果がご提示いただいた 3 項目となり、進めることができました。

その次の Step のテストレポートのアップロードが何度試しても処理中から進まないため完了はできておりませんが、明日改めて試してみます。

ありがとうございました。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Wednesday, January 22, 2025 1:22 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

「(4) Core 階層の ICS
10/1 のチェックを外し、」が記載ミスで正しくは「Core 階層の ICS
12/1 のチェックを外し」です。申し訳ありませんでした。

対応方法としては、 ICS Selection で
Core 10/1 をチェックし、 Core 12/1 のチェックを外して再度

Consistency Check を行ってください。

以上よろしくお願いいたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2025 年 1 月 22 日
13:10

宛先 :
Itsuo Sakai

件名 :
RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

特別サポートのご提案、並びに詳細な登録方法のアドバイスをいただきありがとうございます。

ご連絡いただいた手順で進めましたが、 (4) の Consistency Check 後に表示される結果が 3 項目であるべきところ 5 項目表示されました。

酒井様ご提示の３項目に加え、以下の 2 項目が表示されています。

―――

CORE

12:C.1 | If [CORE] (12/1) is Supported then it is Mandatory to Support at least one of [CORE] (12/2-3)

SEC

SEC > CORE | If [CORE] (10/1) is Not Supported then [SEC] is Excluded Go to Layer Selection.

―――

お手数おかけしますが、記入内容が正しいかチェックしていただけないでしょうか？

画面キャプチャしましたので添付ファイルをご参照願います。

追加サポートについて有償となる場合は弊社内で承認を得るため、お見積書の発行をお願いいたします。

また以降同様の案件については代行登録を発注しての対応となることを承知いたしました。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, January 21, 2025 5:18 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

お問い合わせの内容は、 Include 先の登録内容や登録製品のサポート機能によって個々に異なる対応が必要で代行登録と同じ手間が発生するため、本来は「代行登録をご依頼ください」という対応となります。しかし、御社からは MH26 や新田様案件などをご依頼いただいていますので特別にサポートさせていただきます。以下の手順で登録できることを確認しました。

(1) [ID]
と [ID]
を Include 後、 [Modefy
or Add to this set of Design] をクリック ( 下図 )。

(2)
右下の [Save and go to Layer Selection] をクリック。

(3) Layer Selection ページで Core
Layers から HCI
と UHCI
のチェックをはずし、 LE Audio Spec からすべてのプロトコル・プロファイルのチェックを外して右下の [Save and go to ICS Selection] をクリック

(4) Core 階層の ICS
10/1 のチェックを外し、右上の [Consistency Check] をクリック。結果が下記

3 項目であることを確認後、下部の [Test
Coverage Waiver(s)] に [ID]( 下図 ) を入力後右下の

[Save and go to Test Plan and Documentation] をクリック。その後のページは記載内容に従って所定の入力などを行い、最後のページまで進む。 .

ーーー

BB

If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

GAP

4b:Prerequisite | If [GATT] (1a/4) is Supported then [GAP] (4b/1-2) are Mandatory

ーーー以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2025 年 1 月 21 日
16:08

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

下記、間が空いてしまいましたが弊社 HM23 の Android14 登録についてアドバイスいただけないでしょうか。

弊社大平より、
この後、 Host subsystem、 Profile subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

と説明いたしましたが、 Qualcomm 社から Host と Profile を統合した「QDID/DN : [ID]」の登録完了連絡を受けました。

そこで、 Core_Host and Profiles Qualification: [ID] と Controller Subsystem: [ID] (HM23 A13 から変更なし ) で登録を試みたところ

Consistency Check で添付画像のエラーが出てしまいました。

これは酒井様のご説明にある“ QDID:[ID] から RF/RF PHY 階層を選択する”事により回避可能でしょうか？

試しに「Modify Layers of your Disign manually」を選択して進めてみたところ、エラーにある BAP は LE で選択されていましたが

BASS は選択されていないようでした。

またそのいずれも変更を加えようとすると新しい Ver が適用されるというような警告が表示されました。

もし階層選択によりエラーを無くせるようなら、手順を教えていただけないでしょうか？

大変お手数おかけしますがよろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, October 31, 2024 9:51 AM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
この後、 Host subsystem、 Profile
subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

⇒ 承知しました。
また、ご指摘頂いております RF 試験 1 項目の追加実施につきまして、
先日王君様より概算見積をご提示頂いております。

⇒ 試験項目の不足に関して再度精査しました。当該不足項目は [ID] で追加されて発効が 2022/12/28 でした。従って御社の QDID:[ID](Controller
Subsystem / Listing Date

:[ID]) および展開いただいた SGS 台湾での RF/RF
PHY レポートに含まれていなくても

QDID:[ID] の登録に関しては認証規定上の問題はありません。

しかし、 新規に「当該 RF/RF PHY レポートをエビデンスとした登録を行と不足項目が問題」となります。 ( 以前問題ありと連絡を差し上げた内容です。 )

そこで提案ですが、 QDID:[ID] は Controller
Subsystem 登録ですので現在も引き続き有効なため、これと Q 社の Subset
DN [ID] を Include して、 QDID:[ID] から RF/RF
PHY 階層を選択するとともに DN [ID] から残りの階層を選択すると「認証規定に準拠して」 2022/04/20 当時に有効であった RF/RF PHY およびそのエビデンスを引き継ぐことが可能です。この部分組み合わせ登録手順は 7/1 の新登録サイトで可能となったもので、こうすることで不足項目試験を実施すること無く「認証規定に準拠した」 HM23 登録を進めることが可能です。

以上ご検討ください。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 10 月 30 日 13:49

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早々にご確認頂きありがとうございます。

作成頂いた「Subset DN [ID]」にて問題にないとのこと、承知致しました。

この後、 Host subsystem、 Profile subsystem が提示され次第にて製品登録を進めるようにしたいと思います。

その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

また、ご指摘頂いております RF 試験 1 項目の追加実施につきまして、

先日王君様より概算見積をご提示頂いております。

参考にさせて頂き対応方法等決定しましたら改めてご連絡させて頂きます。

/eom

From: Itsuo Sakai

Sent: Wednesday, October 30, 2024 12:10 PM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
HM23 にて使用している [ID](QDID
[ID]) につきまして、
先日追加にて AoA/AoD 機能削除必要とのことでアドバイス頂いておりました件、
Qualcomm より本件対応完了とのことで連絡がされております。

⇒ ご連絡ありがとうございます。
酒井様よりご教示頂きました通り、 SIG にて以下について削除となっている旨確認はしておりますが、本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

⇒ 私の Workspace で仮 Project を作成して「N
[ID]」で問題解消したことを確認できました。

引き続きよろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 10 月 30 日 11:36

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To.
アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。度々申し訳ありません。

削除追加にて連絡されている subset DN は以下の通りとなります。

先のメールにて記載漏れており申し訳ありません。

ご確認の程よろしくお願い致します。
Subset DN [ID] was created from QDID [ID], [ID] Controller listing.

/eom

From:
大平ひとみ Hitomi Ohira

Sent: Wednesday, October 30, 2024 11:32 AM

To: Itsuo Sakai

Subject: RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To.
アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23 にて使用している [ID](QDID [ID]) につきまして、

先日追加にて AoA/AoD 機能削除必要とのことでアドバイス頂いておりました件、

Qualcomm より本件対応完了とのことで連絡がされております。

Update the subset DN [ID] for [ID] (delete AoA/AoD capabilities from LL)

酒井様よりご教示頂きました通り、 SIG にて以下について削除となっている旨確認はしておりますが、

本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

お忙しいところお手数おかけし申し訳ありません。

ご協力の程よろしくお願い致します。

→ [LL] (9/17):NO

→ [LL] (9/20):NO

→ [LL] (9/21):NO

→ [LL] (9/23):NO

→ [LL] (9/24):NO

/eom

From: Itsuo Sakai

Sent: Monday, September 30, 2024 7:49 PM

To: 大平ひとみ Hitomi Ohira

Subject: Re: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
HM23 にして使用している [ID](QDID
[ID]) につきましても
Power Class1 サポート削除にて Subset
DN [ID] が登録されたとのことで連絡がされました。

お忙しいところ大変恐縮ではございますが、こちらにつきましても先日の HM26 と同様に懸念点解消となっているかご確認頂くことは可能でしょうか？

⇒ Qualification Warkspace で仮 Project を作って確認しました結果、 DN:[ID] は確かに LL
9/11 LE

Power Class 1: NO と修正されて RF
PHY 1/15:NO との階層間不整合は消えました。しかし先日ご送付いただいたベースモデルの RF PHY テストレポート記載の RF
PHY ICS と、 DN [ID] の

LL 階層間に以下の 5 件の不整合 (AoA/AoD の関連 ) が発生します。

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/17) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/20) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/13) is Not Supported then [LL] (9/23) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/14) is Not Supported then [LL] (9/24) is Excluded

If [RFPHY] is Supported and [RFPHY] (1/12) is Not Supported then [LL] (9/21) is Excluded

Q 社には「Subset
DN [ID] から LL の AoA/AoD 機能を削除 ([LL]
(9/17):NO、 [LL] (9/20):NO、

[LL] (9/21):NO、 [LL]
(9/23):NO、 [LL] (9/24):NO) した Subset
DN を作成してほしい。」と再度依頼してください。

以上回答いたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 30 日 11:56

宛先 : Itsuo
Sakai

件名 : RE:
[HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23 にして使用している [ID](QDID [ID]) につきましても

Power Class1 サポート削除にて Subset DN [ID]
が登録されたとのことで連絡がされました。

お忙しいところ大変恐縮ではございますが、こちらにつきましても先日の HM26 と同様に懸念点解消となっているかご確認頂くことは可能でしょうか？

上記ご協力頂けますと幸いです。

よろしくお願い致します。

/eom

From: Itsuo Sakai

Sent: Wednesday, September 25, 2024 4:08 PM

To: 大平ひとみ Hitomi Ohira

Subject: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
早速ですが、 HM26 にて使用している [ID](QDID
[ID]) にて DN [ID] が作成され、
Subset DN [ID]
も作成頂けた旨連絡頂いております。
Subset DN にて「9/11
LE Power Class 1」のサポートが削除されている旨も確認致しましたが、
取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

⇒ [ID](QDID [ID]) の Subset
DN: [ID] での HM26 の登録可能性を私の Quaification
Workspace

の仮 Project を作成して「LL-RF
PHY 間の Class 1 に関する階層間不整合が出ず、他の階層間不整合も

QDID [ID] と同じ TCW(Test
Case Waiver 対象項目 )」であることを確認しました。

この結果、もし御社が RF/RF PHY 試験レポートをエビデンスとして Core-Controller( 旧 Controller

Subsystem) の登録を希望される場合でも、 Subset
DN: [ID] で問題なく登録できることが確認できました。

以上よろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、 HM26 にて使用している [ID](QDID [ID]) にて DN [ID] が作成され、

Subset DN [ID]
も作成頂けた旨連絡頂いております。

Subset DN にて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

お忙しいところ何度もお手数おかけしてしまい申し訳ありません。

ご協力頂けますと幸いです。

/eom

From: Itsuo Sakai

Sent: Tuesday, September 24, 2024 5:21 PM

To: 大平ひとみ Hitomi Ohira ;
深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。
HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。
弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

⇒ 承知しました。ご連絡をお待ちしております。
尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては
HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset
DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host
subsystem/Profile subsystem の ICS
Details ですが、こちらについても HM23/26 共に A13
Profile Subsystem([ID])、 Host Subsystem
([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

⇒ Q 社の対応が確認でき、安心しました。

引き続きよろしくお願いいたいます。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo
Sakai ;
Hiroaki Fukaura

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては

HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host subsystem/Profile subsystem の ICS Details ですが、

こちらについても HM23/26 共に A13 Profile Subsystem([ID])、 Host Subsystem([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

取り急ぎご連絡まで。

/eom

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 4:04 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

⇒ 差分 ( 追加 ) 試験は可能です。しかし、本来その項目が必要な [ID] へは反映できません。
・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、
ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller Subsystem) ＋ [ID](Host
Subsystem) と [ID] (Profile

Subsystem) を更新した登録」では、 [ID]([ID]) を Include した取得した ICS そのものに RFPHY

/TRM/[ID] 試験が含まれますが、形式的に [ID]([ID]) の登録時点で当該試験項目はクリアしたものとして扱われます。

敢えて更新登録で RF PHY の ICS の任意の項目を修正 → 元に戻すと Test
Plan に RF PHY 階層の試験要求が出力されますので RFPHY/TRM/[ID] を差分試験を反映させることは可能ですが、 [ID](Host

Subsystem) と [ID](Profile
Subsystem) を更新した登録と [ID]([ID]) との階層間不整合のチェック対象となって [ID](Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録の機能次第ではリスクが発生します。（例えば更新した Host Subsystem 相当の登録が Isochronous

モードをサポート、あるいは AoA/AoD をサポートした場合です。）

ちなみに [ID]([ID]) に現状の [ID](Host
Subsystem) と [ID](Profile Subsystem) を Include

した登録で、 RF PHY を修正 → 元に戻すと階層間チェックが実施されて下記のように ScPP が不足という結果になります。 (Layer/ICS に一切手をいれなければ階層間不整合チェックは行われない )

<SCPP>

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、

ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 11:29 AM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ RF および RF
PHY レポートおよびログを受領しました。

私の Warkspace で RF と RF
PHY だけの仮 Project を作成し、 [ID] の RF と RF
PHY の ICS を入力して

[ID](2024/12/02 から必須 ) で Test
Plan を出力して受領した RF および RF
PHY レポートと逐次比較しました。

その結果 RF はレポートと一致するとともに、 [ID] および [ID] で追加される試験項目はありませんでした。

RF PHY は [ID] および [ID] で追加される試験項目はないものの、「RFPHY/TRM/[ID]」

がレポートに不足していました。この項目は [ID] で新設されたもので、 [ID] が登録された [ID] の 1 年以上前に必須項目でしたので、 BQTF の確認ミスと思われます。

しかし 6/30 以前の登録制度ではデザイン登録部分 ([ID] では Controller
Subsystem) に QDID:

[ID] が SIG から付与されて形式的に SIG の確認済になっています。したがってご依頼の「[ID]

(Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録」では QDID:[ID] を Include

し、全階層に対して ICS の変更・追加を行わなければ新たに RF
PHY の試験要求は発生しません。

言い換えれば敢えて RF PHY の「RFPHY/TRM/[ID]」を追加試験しなくても新登録サイトの登録過程で「形式上」は不都合が生じません。

立場上「RFPHY/TRM/[ID] の追加試験は不要」と断定的にアドバイスできないのですが、既に

[ID] は承認された登録ですので SIG からこの試験項目の不足を指摘される可能性は無いものと思います。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki
Fukaura

件名 : Re:
[ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ;
Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) - [ID]
(Component (Tested))
[ID] (Host Subsystem)
[ID] (Profile Subsystem)

Android OS の Update に伴い [ID]
(Host Subsystem) と [ID] (Profile Subsystem) が変更となり、
弊社では今後取得される新しい A Host-Core Configuration と X2Core
Layer(Profile Subsystem) を参照して End Product 登録を行う予定です。

⇒ ここまで理解しました。
[ID] は他社で試験をして登録したモデルではありますが、
Host Subsystem と Profile
Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

⇒ ありがとうございます。
そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。
本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？
(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

⇒ はい、他社レポートで問題ございません。
なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。
他に必要な情報がございましたらお申し付けください。

⇒ MH26 と同様、参照 (Include) 予定の新規登録の A
Host-Core Configuration と X2Core Layer(Profile

Subsystem) の DN(Design
Number) が判明しましたら階層間不整合を確認いたしますのでお知らせください。

テストレポートに関してですが、 2024/12/28 から有効になるプロファイルの試験項目が [ID] で予告されています。可能であければ早めにテストレポートをご提出いただければ 2024/12/28 以降に当該レポートがそのまま使えるかどうかを事前確認いたします。

以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun
Wang ;
Itsuo Sakai

件名 : [ALAP]
HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れました HM23 の Bluetooth SIG 認証について相談させてください。

HM23 は [ID] というモデルで、 [ID] で登録済みです。

End Product 登録で参照している QDID は以下です。

[ID] (Controller Subsystem) -
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OS の Update に伴い [ID] (Host
Subsystem) と [ID] (Profile Subsystem) が変更となり、

弊社では今後取得される新しい A Host-Core Configuration と X2Core Layer(Profile Subsystem) を参照して

End Product 登録を行う予定です。

[ID] は他社で試験をして登録したモデルではありますが、

Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、 HM26 にて使用している [ID](QDID [ID]) にて DN [ID] が作成され、

Subset DN [ID]
も作成頂けた旨連絡頂いております。

Subset DN にて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

お忙しいところ何度もお手数おかけしてしまい申し訳ありません。

ご協力頂けますと幸いです。

/eom

From: Itsuo Sakai

Sent: Tuesday, September 24, 2024 5:21 PM

To: 大平ひとみ Hitomi Ohira ;
深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。
HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。
弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

⇒ 承知しました。ご連絡をお待ちしております。
尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては
HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset
DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host
subsystem/Profile subsystem の ICS
Details ですが、こちらについても HM23/26 共に A13
Profile Subsystem([ID])、 Host Subsystem
([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

⇒ Q 社の対応が確認でき、安心しました。

引き続きよろしくお願いいたいます。

差出人 : Hitomi
Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo
Sakai ;
Hiroaki Fukaura

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては

HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host subsystem/Profile subsystem の ICS Details ですが、

こちらについても HM23/26 共に A13 Profile Subsystem([ID])、 Host Subsystem([ID]) 参照にて問題ない旨 Qualcomm より連絡頂いております。

取り急ぎご連絡まで。

/eom

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 4:04 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

⇒ 差分 ( 追加 ) 試験は可能です。しかし、本来その項目が必要な [ID] へは反映できません。
・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、
ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller Subsystem) ＋ [ID](Host
Subsystem) と [ID] (Profile

Subsystem) を更新した登録」では、 [ID]([ID]) を Include した取得した ICS そのものに RFPHY

/TRM/[ID] 試験が含まれますが、形式的に [ID]([ID]) の登録時点で当該試験項目はクリアしたものとして扱われます。

敢えて更新登録で RF PHY の ICS の任意の項目を修正 → 元に戻すと Test
Plan に RF PHY 階層の試験要求が出力されますので RFPHY/TRM/[ID] を差分試験を反映させることは可能ですが、 [ID](Host

Subsystem) と [ID](Profile
Subsystem) を更新した登録と [ID]([ID]) との階層間不整合のチェック対象となって [ID](Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録の機能次第ではリスクが発生します。（例えば更新した Host Subsystem 相当の登録が Isochronous

モードをサポート、あるいは AoA/AoD をサポートした場合です。）

ちなみに [ID]([ID]) に現状の [ID](Host
Subsystem) と [ID](Profile Subsystem) を Include

した登録で、 RF PHY を修正 → 元に戻すと階層間チェックが実施されて下記のように ScPP が不足という結果になります。 (Layer/ICS に一切手をいれなければ階層間不整合チェックは行われない )

<SCPP>

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、

ICS 変更に相当し RF PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 11:29 AM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ RF および RF
PHY レポートおよびログを受領しました。

私の Warkspace で RF と RF
PHY だけの仮 Project を作成し、 [ID] の RF と RF
PHY の ICS を入力して

[ID](2024/12/02 から必須 ) で Test
Plan を出力して受領した RF および RF
PHY レポートと逐次比較しました。

その結果 RF はレポートと一致するとともに、 [ID] および [ID] で追加される試験項目はありませんでした。

RF PHY は [ID] および [ID] で追加される試験項目はないものの、「RFPHY/TRM/[ID]」

がレポートに不足していました。この項目は [ID] で新設されたもので、 [ID] が登録された [ID] の 1 年以上前に必須項目でしたので、 BQTF の確認ミスと思われます。

しかし 6/30 以前の登録制度ではデザイン登録部分 ([ID] では Controller
Subsystem) に QDID:

[ID] が SIG から付与されて形式的に SIG の確認済になっています。したがってご依頼の「[ID]

(Host Subsystem) と [ID]
(Profile Subsystem) を更新した登録」では QDID:[ID] を Include

し、全階層に対して ICS の変更・追加を行わなければ新たに RF
PHY の試験要求は発生しません。

言い換えれば敢えて RF PHY の「RFPHY/TRM/[ID]」を追加試験しなくても新登録サイトの登録過程で「形式上」は不都合が生じません。

立場上「RFPHY/TRM/[ID] の追加試験は不要」と断定的にアドバイスできないのですが、既に

[ID] は承認された登録ですので SIG からこの試験項目の不足を指摘される可能性は無いものと思います。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki
Fukaura

件名 : Re:
[ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo
Sakai

件名 : RE:
[ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ;
Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) - [ID]
(Component (Tested))
[ID] (Host Subsystem)
[ID] (Profile Subsystem)

Android OS の Update に伴い [ID]
(Host Subsystem) と [ID] (Profile Subsystem) が変更となり、
弊社では今後取得される新しい A Host-Core Configuration と X2Core
Layer(Profile Subsystem) を参照して End Product 登録を行う予定です。

⇒ ここまで理解しました。
[ID] は他社で試験をして登録したモデルではありますが、
Host Subsystem と Profile
Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

⇒ ありがとうございます。
そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。
本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？
(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

⇒ はい、他社レポートで問題ございません。
なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。
他に必要な情報がございましたらお申し付けください。

⇒ MH26 と同様、参照 (Include) 予定の新規登録の A
Host-Core Configuration と X2Core Layer(Profile

Subsystem) の DN(Design
Number) が判明しましたら階層間不整合を確認いたしますのでお知らせください。

テストレポートに関してですが、 2024/12/28 から有効になるプロファイルの試験項目が [ID] で予告されています。可能であければ早めにテストレポートをご提出いただければ 2024/12/28 以降に当該レポートがそのまま使えるかどうかを事前確認いたします。

以上よろしくお願いいたします。

差出人 : Hiroaki
Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun
Wang ;
Itsuo Sakai

件名 : [ALAP]
HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れました HM23 の Bluetooth SIG 認証について相談させてください。

HM23 は [ID] というモデルで、 [ID] で登録済みです。

End Product 登録で参照している QDID は以下です。

[ID] (Controller Subsystem) -
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OS の Update に伴い [ID] (Host
Subsystem) と [ID] (Profile Subsystem) が変更となり、

弊社では今後取得される新しい A Host-Core Configuration と X2Core Layer(Profile Subsystem) を参照して

End Product 登録を行う予定です。

[ID] は他社で試験をして登録したモデルではありますが、

Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照した SIG 登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration( 新規取得 ) ＋ X2Core
Layer( 新規取得 ) ＋ Component( 従来登録済み ) ＋前回登録時の他社テストレポート )

なお認証取得完了は HM23/HM26 共に 2025 年 4 月が MUST となっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。
