# thread_0081: [今後の進め方のご提案 ] Re: Bluetooth SIG認証 送金を進めるためのInvoice取得のお願い

- Message count: 8
- Source JSON: `thread_0081.json`

---

## 1. 2026-02-05 12:38

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?SEFZQVNISSBLRU5TVUtFKBskQk5TISE3ekplGyhCKQ==?= , =?iso-2022-jp?B?SEFTSElNT1RPIEhJREVNQVNBKBskQjY2S1whIT0oPjsbKEIp?= , Masaya Iida , =?iso-2022-jp?B?VFNVUlVUQSBEQUlTVUtFKBskQkRhRUQhIUJnMnAbKEIp?= , =?iso-2022-jp?B?bXVyYXlhbWEgdGVydW1hc2EoGyRCQjw7MyEhNTE+OxsoQik=?= , =?iso-2022-jp?B?SE9TSEkgTUFTQVNISSgbJEJAMSEhPGM7VhsoQik=?= , Kei Tanaka
**Attachments:** [ID]zip

NECプラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、(2)のプロファイルのICSの割り切りをお願いします。

(1)既存登録をIncludeして発生するコア階層のInvalidの除外申請制度

Bluetooth SIGのHelp & Supportページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類のConsistensy

Check発生の例外申請(Test Case Waiver)の一つに、今回のHost Stack

のInvlidに使えそうな「TCW [ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW ES-26007は既存のController Subsystem登録と既存のHost Subsystem

登録をIncludeし、X2Core(=プロフィル)を追加定義する際にコア階層ので発生したInvalidを例外申請するためのコードです。

(2)IncludeするQDIDとPTS試験内容の決定手順

MAYA-W1モジュール(QDID:[ID])とFluoride 1.5(QDID:[ID])をIncude

すると、HID, SPP, PAN, BNEP, HOGP, ScPPは包含されていてほとんどご送付いただいたICS項目と一致しているのですが、一部不足しているものもあります。ICS Exportファイルを添付しますので、どなたかの

Qualification WorkspceにInportしてHID, PAN, HOGPのICSを御社希望のICSと比較して「ICS項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID])から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポートYESでもNOでも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11だけはFluoride 1.5(QDID:[ID])に包含されてないのでPTS試験レポートをエビデンスとしてアップロードする必要があります。

(3)御社テストサンプルでPTS試験を実施上記(2)でご確認いただく包含されたICS項目では不足していて試験対象とするプロファイルが決まらないとPTS試験のテストプランが確定できませんが、仮にHID11以外はFluoride 1.5(QDID:[ID])に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4)テストレポート取得後の作業当方でTCW:ES-26007申請および必要なプロファイルレポートによる代行登録を実施します。TCWによる申請はSIG管理者の内容確認後の登録確定(あるいは

Listing OwnerへのReject通知)ですので、2-5営業日の登録遅延が発生します。

(5)その他：ご送付いただいたICSで見つけた問題点

HID11のTbale 1は 1/1と1/2が互いに排他YESとなっています。

1/1 →C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2 →C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付したExport ICSのHID11は1/1:YES, 1/2:NO としています。

以上よろしくお願いいたします。

差出人: Itsuo Sakai

送信日時: 2026年2月5日 18:16

宛先: [ID] [ID](林建輔) ; [ID] [ID](橋本秀昌) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志)
; Kei Tanaka

件名: [再送] [Google Fluoride 1.4/1.5は使えませんでした ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECプラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールでInvalidの説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、Google Fluoride 1.6 197197との適合性も調べていただけますか？

⇒仮ProjectでConsistency Checkを掛けたところ、Google Fluoride 1.5 [ID]

と同じ以下のInvalidが発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:192202とFluoride 1.4の組み合わせでは、GAPとGATT 7/5をサポートする際に必要なGAP機能（25/5 または 35/5）が不足している。

⇒ 「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」、 「[GATT] (7/6)をサポートしているが、 [GAP]（25/6 または

35/6）サポート条件が満たされていない」、 「[GATT] (1/2 and 4/15) をサポートしているが、[GATT] (4/25)サポート条件が満たされていない」、 「[GATT] (1/2

and 4/16) をサポートしているが、[GATT] (4/25)サポート条件が満たされていない」

および 「[GATT] (1/2 and 4/22) をサポートしているが、[GATT] (4/25)サポート条件が満たされていない」 というInvalid表示です。
QDID:192202とFluoride 1.5の組み合わせでも、同様にGAPとGATT 7/6をサポートする際に必要なGAP機能（25/6 または 35/6）が不足している

⇒ 「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」 および 「[GATT] (7/6)をサポートしているが、 [GAP]（25/6 または 35/6）サポート条件が満たされていない」 に減少しています。
使用しているモジュール（QDID:[ID]）が、GAPの要件（25/5, 35/5 または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒GAP, GATTはHost Subsystemの階層で、モジュール（QDID:[ID]）は無関係です。

単にFluoride 1.4/1.5/1.6自身が包含する内部不整合で、登録時点ではInvalid=0

でないと登録できませんので、登録以降にBluetooth SIGがGAPとGATTのICSチェックルールを追加したものと推測します。このようなInvalidはFluoride 1.4/1.5/1.6に代わるInvalidの出ないHost Stackと組み合わせる必要があります。

以上回答いたします。

差出人: Itsuo Sakai

送信日時: 2026年2月5日 18:01

宛先: [ID] [ID](林建輔) ; [ID] [ID](橋本秀昌) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志)
; Kei Tanaka

件名: Re: [Google Fluoride 1.4/1.5は使えませんでした ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECプラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、Google Fluoride 1.6 197197との適合性も調べていただけますか？

⇒仮ProjectでConsistency Checkを掛けたところ、Google Fluoride 1.5 [ID]

と同じ以下のInvalidが発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:192202とFluoride 1.4の組み合わせでは、GAPとGATT 7/5をサポートする際に必要なGAP機能（25/5 または 35/5）が不足している。

⇒「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15) をサポートしているが、[GATT]

(4/25)サポート条件が満たされていない」というInvalidが表示されています。
QDID:192202とFluoride 1.5の組み合わせでも、同様にGAPとGATT 7/6をサポートする際に必要なGAP機能（25/6 または 35/6）が不足している

⇒「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、GAPの要件（25/5, 35/5 または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒GAP, GATTはHost Subsystemの階層で、モジュール（QDID:[ID]）は無関係です。

単にFluoride 1.4/1.5/1.6自身が包含する内部不整合で、登録時点ではInvalid=0

でないと登録できませんので、登録以降にBluetooth SIGがGAPとGATTのICSチェックルールを追加したものと推測します。このようなInvalidはFluoride 1.4/1.5/1.6に代わるInvalidの出ないHost Stackと組合わせる必要があります。

以上回答いたします。

差出人: [ID] [ID](林建輔)

送信日時: 2026年2月5日 15:49

宛先: Itsuo Sakai ; [ID] [ID](橋本秀昌) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [Google Fluoride 1.4/1.5は使えませんでした ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NECプラットフォームズの林です。

お世話になっております。

お手数ですが、Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

エラーの見方をよく知りませんが、要約すると

QDID:192202とFluoride 1.4の組み合わせでは、GAPとGATT 7/5をサポートする際に必要なGAP機能（25/5 または 35/5）が不足している。

QDID:192202とFluoride 1.5の組み合わせでも、同様にGAPとGATT 7/6をサポートする際に必要なGAP機能（25/6 または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、GAPの要件（25/5, 35/5 または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NECプラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; [ID] [ID]( 林建輔 ) ; murayama terumasa( 村山輝昌 )
; HOSHI [ID]( 星若志 ) ; Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride
1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride
1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty
Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya Iida ;
Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ;
[ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件におけるINVOICEお送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID](橋本秀昌) ;
Itsuo Sakai ;
[ID] [ID](鶴田大介) ;
[ID] [ID](林建輔) ;
murayama terumasa(村山輝昌) ;
HOSHI [ID](星若志) ;
Kei Tanaka

Subject: RE: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECPF　橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から2番目の My

account をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

---

## 2. 2026-02-05 23:45

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?SEFZQVNISSBLRU5TVUtFKBskQk5TISE3ekplGyhCKQ==?= , =?iso-2022-jp?B?SEFTSElNT1RPIEhJREVNQVNBKBskQjY2S1whIT0oPjsbKEIp?= , Masaya Iida , =?iso-2022-jp?B?VFNVUlVUQSBEQUlTVUtFKBskQkRhRUQhIUJnMnAbKEIp?= , =?iso-2022-jp?B?bXVyYXlhbWEgdGVydW1hc2EoGyRCQjw7MyEhNTE+OxsoQik=?= , =?iso-2022-jp?B?SE9TSEkgTUFTQVNISSgbJEJAMSEhPGM7VhsoQik=?= , Kei Tanaka

NECプラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

前のメールで「ICS Exportファイルを添付しますので、どなたかの

Qualification WorkspceにInportして踏襲したICSを確認」とお伝えしましたが手間がかかる方法です。[URL]

以下のURL参照で直接Fluoride 1.5(QDID:[ID])の登録詳細ページのサポートプロファイルとそのICSを確認できますのでこの方法をお勧めします。

以上よろしくお願いいたします。

差出人: Itsuo Sakai

送信日時: 2026年2月5日 21:38

宛先: [ID] [ID](林建輔) ; [ID] [ID](橋本秀昌) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志)
; Kei Tanaka

件名: [今後の進め方のご提案 ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECプラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、(2)のプロファイルのICSの割り切りをお願いします。

(1)既存登録をIncludeして発生するコア階層のInvalidの除外申請制度

Bluetooth SIGのHelp & Supportページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類のConsistensy

Check発生の例外申請(Test Case Waiver)の一つに、今回のHost Stack

のInvlidに使えそうな「TCW [ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW ES-26007は既存のController Subsystem登録と既存のHost Subsystem

登録をIncludeし、X2Core(=プロフィル)を追加定義する際にコア階層ので発生したInvalidを例外申請するためのコードです。

(2)IncludeするQDIDとPTS試験内容の決定手順

MAYA-W1モジュール(QDID:[ID])とFluoride 1.5(QDID:[ID])をIncude

すると、HID, SPP, PAN, BNEP, HOGP, ScPPは包含されていてほとんどご送付いただいたICS項目と一致しているのですが、一部不足しているものもあります。ICS Exportファイルを添付しますので、どなたかの

Qualification WorkspceにInportしてHID, PAN, HOGPのICSを御社希望のICSと比較して「ICS項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID])から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポートYESでもNOでも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11だけはFluoride 1.5(QDID:[ID])に包含されてないのでPTS試験レポートをエビデンスとしてアップロードする必要があります。

(3)御社テストサンプルでPTS試験を実施上記(2)でご確認いただく包含されたICS項目では不足していて試験対象とするプロファイルが決まらないとPTS試験のテストプランが確定できませんが、仮にHID11以外はFluoride 1.5(QDID:[ID])に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4)テストレポート取得後の作業当方でTCW:ES-26007申請および必要なプロファイルレポートによる代行登録を実施します。TCWによる申請はSIG管理者の内容確認後の登録確定(あるいは

Listing OwnerへのReject通知)ですので、2-5営業日の登録遅延が発生します。

(5)その他：ご送付いただいたICSで見つけた問題点

HID11のTbale 1は 1/1と1/2が互いに排他YESとなっています。

1/1 →C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2 →C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付したExport ICSのHID11は1/1:YES, 1/2:NO としています。

以上よろしくお願いいたします。

差出人: Itsuo Sakai

送信日時: 2026年2月5日 18:16

宛先: [ID] [ID](林建輔) ; [ID] [ID](橋本秀昌) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志)
; Kei Tanaka

件名: [再送] [Google Fluoride 1.4/1.5は使えませんでした ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECプラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールでInvalidの説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、Google Fluoride 1.6 197197との適合性も調べていただけますか？

⇒仮ProjectでConsistency Checkを掛けたところ、Google Fluoride 1.5 [ID]

と同じ以下のInvalidが発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:192202とFluoride 1.4の組み合わせでは、GAPとGATT 7/5をサポートする際に必要なGAP機能（25/5 または 35/5）が不足している。

⇒ 「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」、 「[GATT] (7/6)をサポートしているが、 [GAP]（25/6 または

35/6）サポート条件が満たされていない」、 「[GATT] (1/2 and 4/15) をサポートしているが、[GATT] (4/25)サポート条件が満たされていない」、 「[GATT] (1/2

and 4/16) をサポートしているが、[GATT] (4/25)サポート条件が満たされていない」

および 「[GATT] (1/2 and 4/22) をサポートしているが、[GATT] (4/25)サポート条件が満たされていない」 というInvalid表示です。
QDID:192202とFluoride 1.5の組み合わせでも、同様にGAPとGATT 7/6をサポートする際に必要なGAP機能（25/6 または 35/6）が不足している

⇒ 「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」 および 「[GATT] (7/6)をサポートしているが、 [GAP]（25/6 または 35/6）サポート条件が満たされていない」 に減少しています。
使用しているモジュール（QDID:[ID]）が、GAPの要件（25/5, 35/5 または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒GAP, GATTはHost Subsystemの階層で、モジュール（QDID:[ID]）は無関係です。

単にFluoride 1.4/1.5/1.6自身が包含する内部不整合で、登録時点ではInvalid=0

でないと登録できませんので、登録以降にBluetooth SIGがGAPとGATTのICSチェックルールを追加したものと推測します。このようなInvalidはFluoride 1.4/1.5/1.6に代わるInvalidの出ないHost Stackと組み合わせる必要があります。

以上回答いたします。

差出人: Itsuo Sakai

送信日時: 2026年2月5日 18:01

宛先: [ID] [ID](林建輔) ; [ID] [ID](橋本秀昌) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志)
; Kei Tanaka

件名: Re: [Google Fluoride 1.4/1.5は使えませんでした ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECプラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、Google Fluoride 1.6 197197との適合性も調べていただけますか？

⇒仮ProjectでConsistency Checkを掛けたところ、Google Fluoride 1.5 [ID]

と同じ以下のInvalidが発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:192202とFluoride 1.4の組み合わせでは、GAPとGATT 7/5をサポートする際に必要なGAP機能（25/5 または 35/5）が不足している。

⇒「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15) をサポートしているが、[GATT]

(4/25)サポート条件が満たされていない」というInvalidが表示されています。
QDID:192202とFluoride 1.5の組み合わせでも、同様にGAPとGATT 7/6をサポートする際に必要なGAP機能（25/6 または 35/6）が不足している

⇒「[GATT] (7/5)をサポートしているが、 [GAP]（25/5 または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、GAPの要件（25/5, 35/5 または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒GAP, GATTはHost Subsystemの階層で、モジュール（QDID:[ID]）は無関係です。

単にFluoride 1.4/1.5/1.6自身が包含する内部不整合で、登録時点ではInvalid=0

でないと登録できませんので、登録以降にBluetooth SIGがGAPとGATTのICSチェックルールを追加したものと推測します。このようなInvalidはFluoride 1.4/1.5/1.6に代わるInvalidの出ないHost Stackと組合わせる必要があります。

以上回答いたします。

差出人: [ID] [ID](林建輔)

送信日時: 2026年2月5日 15:49

宛先: Itsuo Sakai ; [ID] [ID](橋本秀昌) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [Google Fluoride 1.4/1.5は使えませんでした ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NECプラットフォームズの林です。

お世話になっております。

お手数ですが、Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5
or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of
[GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6
or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of
[GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or
35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or
35/6)

エラーの見方をよく知りませんが、要約すると

QDID:192202とFluoride 1.4の組み合わせでは、GAPとGATT 7/5をサポートする際に必要なGAP機能（25/5 または 35/5）が不足している。

QDID:192202とFluoride 1.5の組み合わせでも、同様にGAPとGATT 7/6をサポートする際に必要なGAP機能（25/6 または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、GAPの要件（25/5, 35/5 または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NECプラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; [ID] [ID]( 林建輔 ) ; murayama terumasa( 村山輝昌 )
; HOSHI [ID]( 星若志 ) ; Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride
1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP]
(25/5 or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one
of [GAP] (25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP]
(25/6 or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one
of [GAP] (25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride
1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty
Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5
or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6
or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya Iida ;
Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ;
[ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件におけるINVOICEお送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID](橋本秀昌) ;
Itsuo Sakai ;
[ID] [ID](鶴田大介) ;
[ID] [ID](林建輔) ;
murayama terumasa(村山輝昌) ;
HOSHI [ID](星若志) ;
Kei Tanaka

Subject: RE: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECPF　橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から2番目の My

account をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

---

## 3. 2026-02-10 04:17

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?SEFTSElNT1RPIEhJREVNQVNBKBskQjY2S1whIT0oPjsbKEIp?= , =?iso-2022-jp?B?SEFZQVNISSBLRU5TVUtFKBskQk5TISE3ekplGyhCKQ==?= , Masaya Iida , =?iso-2022-jp?B?VFNVUlVUQSBEQUlTVUtFKBskQkRhRUQhIUJnMnAbKEIp?= , =?iso-2022-jp?B?bXVyYXlhbWEgdGVydW1hc2EoGyRCQjw7MyEhNTE+OxsoQik=?= , =?iso-2022-jp?B?SE9TSEkgTUFTQVNISSgbJEJAMSEhPGM7VhsoQik=?= , Kei Tanaka

NECプラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
下記２点ご連絡いたします。

【HID11未採用の件】
弊社で検討した結果、HID11未採用という結論に至りました。
お手数ですがHID11試験は不要でお願いいたします。

⇒HID11未採用とのこと承知しました。
【Fluoride 1.5と弊社提示ICS差分の確認】
現在、差分を確認中です。
結果がでましたら連絡させて頂きます。

⇒SPP、ScPPおよびBNEPは必要最低限のICSサポートであれば問題ありません。

(既存登録は登録条件として必要最低限のICSがサポートされています。)

Fluoride 1.5のHID、PAN、HOGPが御社が必要とするICS機能をサポートしているかをご確認ください。

以上よろしくお願いいたします。

差出人: [ID] [ID](橋本秀昌)

送信日時: 2026年2月10日 12:24

宛先: Itsuo Sakai ; [ID] [ID](林建輔) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [今後の進め方のご提案 ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】

FROM：NECPF橋本です

TO：アリオン酒井様ご連絡遅くなり申し訳ございません。

先程はお電話ありがとうございました。

下記２点ご連絡いたします。

【HID11未採用の件】

弊社で検討した結果、HID11未採用という結論に至りました。

お手数ですがHID11試験は不要でお願いいたします。

【Fluoride 1.5と弊社提示ICS差分の確認】

現在、差分を確認中です。

結果がでましたら連絡させて頂きます。

From: Itsuo Sakai

Sent: Friday, February 6, 2026 8:45 AM

To: [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 ) ; murayama terumasa( 村山輝昌 )
; HOSHI [ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

前のメールで「ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して踏襲した ICS を確認」とお伝えしましたが手間がかかる方法です。 [URL] でログイン後、

以下の URL 参照で直接 Fluoride
1.5(QDID:[ID]) の登録詳細ページのサポートプロファイルとその ICS を確認できますのでこの方法をお勧めします。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 21:38

宛先 : [ID] [ID]( 林建輔 )
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : [ 今後の進め方のご提案 ]
Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、 (2) のプロファイルの ICS の割り切りをお願いします。

(1) 既存登録を Include して発生するコア階層の Invalid の除外申請制度

Bluetooth SIG の Help
& Support ページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類の Consistensy

Check 発生の例外申請 (Test
Case Waiver) の一つに、今回の Host Stack

の Invlid に使えそうな「TCW
[ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW [ID] は既存の Controller
Subsystem 登録と既存の Host Subsystem

登録を Include し、 X2Core(= プロフィル ) を追加定義する際にコア階層ので発生した Invalid を例外申請するためのコードです。

(2)Include する QDID と PTS 試験内容の決定手順

[ID] モジュール (QDID:[ID]) と Fluoride
1.5(QDID:[ID]) を Incude

すると、 HID, SPP, PAN, BNEP, HOGP, ScPP は包含されていてほとんどご送付いただいた ICS 項目と一致しているのですが、一部不足しているものもあります。 ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して HID,
PAN, HOGP の ICS を御社希望の ICS と比較して「ICS 項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID]) から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポート YES でも NO でも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11 だけは Fluoride
1.5(QDID:[ID]) に包含されてないので PTS 試験レポートをエビデンスとしてアップロードする必要があります。

(3) 御社テストサンプルで PTS 試験を実施上記 (2) でご確認いただく包含された ICS 項目では不足していて試験対象とするプロファイルが決まらないと PTS 試験のテストプランが確定できませんが、仮に HID11 以外は Fluoride
1.5(QDID:[ID]) に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4) テストレポート取得後の作業当方で TCW:[ID] 申請および必要なプロファイルレポートによる代行登録を実施します。 TCW による申請は SIG 管理者の内容確認後の登録確定 ( あるいは

Listing Owner への Reject 通知 ) ですので、 2-5 営業日の登録遅延が発生します。

(5) その他：ご送付いただいた ICS で見つけた問題点

HID11 の Tbale
1 は 1/1 と 1/2 が互いに排他 YES となっています。

1/1 →C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2 →C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付した Export ICS の HID11 は 1/1:YES,
1/2:NO としています。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:16

宛先 : [ID] [ID]( 林建輔 )
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : [ 再送 ]
[Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールで Invalid の説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒ 仮 Project で Consistency
Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒ 「[GATT]
(7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」、 「[GATT]
(7/6) をサポートしているが、 [GAP] （25/6
または

35/6）サポート条件が満たされていない」、 「[GATT]
(1/2 and 4/15) をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」、 「[GATT]
(1/2

and 4/16)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」

および 「[GATT]
(1/2 and 4/22) をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」 という Invalid 表示です。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒ 「[GATT]
(7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」 および 「[GATT]
(7/6) をサポートしているが、 [GAP] （25/6
または 35/6）サポート条件が満たされていない」 に減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5,
35/5 または 25/6,
35/6）を満たすバージョンであるか？
→ デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host
Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride
1.4/1.5/1.6 に代わる Invalid の出ない Host
Stack と組み合わせる必要があります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:01

宛先 : [ID] [ID]( 林建輔 )
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : Re: [Google Fluoride 1.4/1.5 は使えませんでした ]
Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒ 仮 Project で Consistency
Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒ 「[GATT]
(7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT]

(4/25) サポート条件が満たされていない」という Invalid が表示されています。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒ 「[GATT]
(7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5,
35/5 または 25/6,
35/6）を満たすバージョンであるか？
→ デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host
Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride
1.4/1.5/1.6 に代わる Invalid の出ない Host
Stack と組合わせる必要があります。

以上回答いたします。

差出人 : [ID] [ID]( 林建輔 )

送信日時 : 2026 年 2 月 5 日 15:49

宛先 : Itsuo Sakai ;
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [Google Fluoride 1.4/1.5 は使えませんでした ]
Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NECプラットフォームズの林です。

お世話になっております。

お手数ですが、Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

エラーの見方をよく知りませんが、要約すると

QDID:192202とFluoride 1.4の組み合わせでは、GAPとGATT 7/5をサポートする際に必要なGAP機能（25/5 または 35/5）が不足している。

QDID:192202とFluoride 1.5の組み合わせでも、同様にGAPとGATT 7/6をサポートする際に必要なGAP機能（25/6 または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、GAPの要件（25/5, 35/5 または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NECプラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
[ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride
1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride
1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty
Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya Iida ;
Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ;
[ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件におけるINVOICEお送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID](橋本秀昌) ;
Itsuo Sakai ;
[ID] [ID](鶴田大介) ;
[ID] [ID](林建輔) ;
murayama terumasa(村山輝昌) ;
HOSHI [ID](星若志) ;
Kei Tanaka

Subject: RE: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

NECPF　橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から2番目の My

account をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

---

## 4. 2026-02-12 05:21

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?SEFTSElNT1RPIEhJREVNQVNBKBskQjY2S1whIT0oPjsbKEIp?= , =?iso-2022-jp?B?SEFZQVNISSBLRU5TVUtFKBskQk5TISE3ekplGyhCKQ==?= , Masaya Iida , =?iso-2022-jp?B?VFNVUlVUQSBEQUlTVUtFKBskQkRhRUQhIUJnMnAbKEIp?= , =?iso-2022-jp?B?bXVyYXlhbWEgdGVydW1hc2EoGyRCQjw7MyEhNTE+OxsoQik=?= , =?iso-2022-jp?B?SE9TSEkgTUFTQVNISSgbJEJAMSEhPGM7VhsoQik=?= , Kei Tanaka
**Attachments:** ���������������������������.doc

NECプラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
本日、弊社内部で議論した結果、
全てのPROFILEの ICSは、Fluoride 1.5に合わせるという結論となりました。
誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

⇒承知しました。プロファイル試験免除で認証登録を進めます。

つきましては添付の代行登録内容確認書にご記入の上、ご返送ください。

以上よろしくお願いいたします。

差出人: [ID] [ID](橋本秀昌)

送信日時: 2026年2月12日 14:05

宛先: Itsuo Sakai ; [ID] [ID](林建輔) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [今後の進め方のご提案 ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様本日、弊社内部で議論した結果、

全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。

誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

HID、 PAN、 HOGP における現行機と Fluoride 1.5 の ICS 差分抽出いたしました。

T.B.D. 部が現在、必要性判断検討中でおります。

休み明けに弊社にて議論実施し最終回答させて頂きます。

背景として今回プロジェクトは現行機踏襲いうのが前提条件であり

T.B.D. → N.A とする最終判断を慎重に進めさせて頂きたい所存でおります。

From: Itsuo Sakai

Sent: Tuesday, February 10, 2026 1:17 PM

To: [ID] [ID]( 橋本秀昌 ) ;
[ID] [ID]( 林建輔 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
下記２点ご連絡いたします。

【HID11 未採用の件】
弊社で検討した結果、 HID11 未採用という結論に至りました。
お手数ですが HID11 試験は不要でお願いいたします。

⇒ HID11 未採用とのこと承知しました。
【Fluoride 1.5 と弊社提示 ICS 差分の確認】
現在、差分を確認中です。
結果がでましたら連絡させて頂きます。

⇒ SPP、 ScPP および BNEP は必要最低限の ICS サポートであれば問題ありません。

( 既存登録は登録条件として必要最低限の ICS がサポートされています。 )

Fluoride 1.5 の HID、 PAN、 HOGP が御社が必要とする ICS 機能をサポートしているかをご確認ください。

以上よろしくお願いいたします。

差出人 : [ID]
[ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 10 日
12:24

宛先 : Itsuo
Sakai ;
[ID] [ID]( 林建輔 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE:
[ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡遅くなり申し訳ございません。

先程はお電話ありがとうございました。

下記２点ご連絡いたします。

【HID11 未採用の件】

弊社で検討した結果、 HID11 未採用という結論に至りました。

お手数ですが HID11 試験は不要でお願いいたします。

【Fluoride 1.5 と弊社提示 ICS 差分の確認】

現在、差分を確認中です。

結果がでましたら連絡させて頂きます。

From: Itsuo Sakai

Sent: Friday, February 6, 2026 8:45 AM

To: [ID] [ID]( 林建輔 ) ;
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

前のメールで「ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して踏襲した ICS を確認」とお伝えしましたが手間がかかる方法です。 [URL] でログイン後、

以下の URL 参照で直接 Fluoride
1.5(QDID:[ID]) の登録詳細ページのサポートプロファイルとその ICS を確認できますのでこの方法をお勧めします。

以上よろしくお願いいたします。

差出人 : Itsuo
Sakai

送信日時 : 2026 年 2 月 5 日 21:38

宛先 : [ID]
[ID]( 林建輔 ) ;
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : [ 今後の進め方のご提案 ]
Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、 (2) のプロファイルの ICS の割り切りをお願いします。

(1) 既存登録を Include して発生するコア階層の Invalid の除外申請制度

Bluetooth SIG の Help
& Support ページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類の Consistensy

Check 発生の例外申請 (Test Case
Waiver) の一つに、今回の Host Stack

の Invlid に使えそうな「TCW
[ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW [ID] は既存の Controller
Subsystem 登録と既存の Host Subsystem

登録を Include し、 X2Core(= プロフィル ) を追加定義する際にコア階層ので発生した Invalid を例外申請するためのコードです。

(2)Include する QDID と PTS 試験内容の決定手順

[ID] モジュール (QDID:[ID]) と Fluoride
1.5(QDID:[ID]) を Incude

すると、 HID, SPP, PAN, BNEP, HOGP, ScPP は包含されていてほとんどご送付いただいた ICS 項目と一致しているのですが、一部不足しているものもあります。 ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して HID,
PAN, HOGP の ICS を御社希望の ICS と比較して「ICS 項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID]) から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポート YES でも NO でも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11 だけは Fluoride 1.5(QDID:[ID]) に包含されてないので PTS 試験レポートをエビデンスとしてアップロードする必要があります。

(3) 御社テストサンプルで PTS 試験を実施上記 (2) でご確認いただく包含された ICS 項目では不足していて試験対象とするプロファイルが決まらないと PTS 試験のテストプランが確定できませんが、仮に HID11 以外は Fluoride
1.5(QDID:[ID]) に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4) テストレポート取得後の作業当方で TCW:[ID] 申請および必要なプロファイルレポートによる代行登録を実施します。 TCW による申請は SIG 管理者の内容確認後の登録確定 ( あるいは

Listing Owner への Reject 通知 ) ですので、 2-5 営業日の登録遅延が発生します。

(5) その他：ご送付いただいた ICS で見つけた問題点

HID11 の Tbale 1 は 1/1 と 1/2 が互いに排他 YES となっています。

1/1 →C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2 →C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付した Export ICS の HID11 は 1/1:YES,
1/2:NO としています。

以上よろしくお願いいたします。

差出人 : Itsuo
Sakai

送信日時 : 2026 年 2 月 5 日 18:16

宛先 : [ID]
[ID]( 林建輔 ) ;
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : [ 再送 ]
[Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールで Invalid の説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒ 仮 Project で Consistency
Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒ 「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」、「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または

35/6）サポート条件が満たされていない」、「[GATT]
(1/2 and 4/15) をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」、「[GATT]
(1/2

and 4/16)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」

および「[GATT] (1/2 and 4/22)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」という Invalid 表示です。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒ 「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または 35/6）サポート条件が満たされていない」に減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5,
35/5 または 25/6,
35/6）を満たすバージョンであるか？
→ デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host
Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride
1.4/1.5/1.6 に代わる Invalid の出ない Host
Stack と組み合わせる必要があります。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2026 年 2 月 5 日 18:01

宛先 : [ID]
[ID]( 林建輔 ) ;
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : Re:
[Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒ 仮 Project で Consistency
Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒ 「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT]

(4/25) サポート条件が満たされていない」という Invalid が表示されています。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒ 「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5,
35/5 または 25/6,
35/6）を満たすバージョンであるか？
→ デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host
Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride
1.4/1.5/1.6 に代わる Invalid の出ない Host
Stack と組合わせる必要があります。

以上回答いたします。

差出人 : [ID]
[ID]( 林建輔 )

送信日時 : 2026 年 2 月 5 日 15:49

宛先 : Itsuo
Sakai ;
[ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE:
[Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NEC プラットフォームズの林です。

お世話になっております。

お手数ですが、 Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5
or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of
[GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6
or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of
[GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5
or 35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6
or 35/6)

エラーの見方をよく知りませんが、要約すると

QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT 7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT 7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NEC プラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
[ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride
1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5
or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP]
(25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6
or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP]
(25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride
1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty
Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID]
[ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya
Iida ;
Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ;
[ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE:
Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件における [ID] お送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID]( 橋本秀昌 ) ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] でログイン後、ページ左上の My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から 2 番目の My

account
をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 5. 2026-02-12 10:22

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?SEFTSElNT1RPIEhJREVNQVNBKBskQjY2S1whIT0oPjsbKEIp?= , =?iso-2022-jp?B?SEFZQVNISSBLRU5TVUtFKBskQk5TISE3ekplGyhCKQ==?= , Masaya Iida , =?iso-2022-jp?B?VFNVUlVUQSBEQUlTVUtFKBskQkRhRUQhIUJnMnAbKEIp?= , =?iso-2022-jp?B?bXVyYXlhbWEgdGVydW1hc2EoGyRCQjw7MyEhNTE+OxsoQik=?= , =?iso-2022-jp?B?SE9TSEkgTUFTQVNISSgbJEJAMSEhPGM7VhsoQik=?= , Kei Tanaka

NECプラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

⇒承知しました。お手数をお掛けしますがよろしくお願いします。
登録したい製品は３種類ございますが
３機種明記すればよろしいでしょうか？
いずれも同じBT MODULEとHOST STACKが実装されております。
・製品１：[ID]
・製品２：[ID]
・製品３：[ID]

⇒はい、「5&#8194;最初に販売予定の機器の型式（モデル）名」に3機種を列記してください。

以上よろしくお願いいたします。

差出人: [ID] [ID](橋本秀昌)

送信日時: 2026年2月12日 19:17

宛先: Itsuo Sakai ; [ID] [ID](林建輔) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [今後の進め方のご提案 ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡ありがとうございます。

パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

登録したい製品は３種類ございますが

３機種明記すればよろしいでしょうか？

いずれも同じ BT [ID] と HOST STACK が実装されております。

・製品１： [ID]

・製品２： [ID]

・製品３： [ID]

From: Itsuo Sakai

Sent: Thursday, February 12, 2026 2:22 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
本日、弊社内部で議論した結果、
全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。
誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

⇒ 承知しました。プロファイル試験免除で認証登録を進めます。

つきましては添付の代行登録内容確認書にご記入の上、ご返送ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 12 日
14:05

宛先 : Itsuo Sakai ;
[ID] [ID]( 林建輔 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案
] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様本日、弊社内部で議論した結果、

全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。

誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

HID、 PAN、 HOGP における現行機と Fluoride 1.5 の ICS 差分抽出いたしました。

T.B.D. 部が現在、必要性判断検討中でおります。

休み明けに弊社にて議論実施し最終回答させて頂きます。

背景として今回プロジェクトは現行機踏襲いうのが前提条件であり

T.B.D. → N.A とする最終判断を慎重に進めさせて頂きたい所存でおります。

From: Itsuo Sakai

Sent: Tuesday, February 10, 2026 1:17 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
下記２点ご連絡いたします。

【HID11 未採用の件】
弊社で検討した結果、 HID11 未採用という結論に至りました。
お手数ですが HID11 試験は不要でお願いいたします。

⇒ HID11 未採用とのこと承知しました。
【Fluoride 1.5 と弊社提示 ICS 差分の確認】
現在、差分を確認中です。
結果がでましたら連絡させて頂きます。

⇒ SPP、 ScPP および BNEP は必要最低限の ICS サポートであれば問題ありません。

( 既存登録は登録条件として必要最低限の ICS がサポートされています。 )

Fluoride 1.5 の HID、 PAN、 HOGP が御社が必要とする ICS 機能をサポートしているかをご確認ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 10 日 12:24

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡遅くなり申し訳ございません。

先程はお電話ありがとうございました。

下記２点ご連絡いたします。

【HID11 未採用の件】

弊社で検討した結果、 HID11 未採用という結論に至りました。

お手数ですが HID11 試験は不要でお願いいたします。

【Fluoride 1.5 と弊社提示 ICS 差分の確認】

現在、差分を確認中です。

結果がでましたら連絡させて頂きます。

From: Itsuo Sakai

Sent: Friday, February 6, 2026 8:45 AM

To: [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

前のメールで「ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して踏襲した ICS を確認」とお伝えしましたが手間がかかる方法です。 [URL] でログイン後、

以下の URL 参照で直接 Fluoride 1.5(QDID:[ID]) の登録詳細ページのサポートプロファイルとその ICS を確認できますのでこの方法をお勧めします。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 21:38

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、 (2) のプロファイルの ICS の割り切りをお願いします。

(1) 既存登録を Include して発生するコア階層の Invalid の除外申請制度

Bluetooth SIG の Help & Support ページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類の Consistensy

Check 発生の例外申請 (Test Case Waiver) の一つに、今回の Host Stack

の Invlid に使えそうな「TCW [ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW [ID] は既存の Controller Subsystem 登録と既存の Host Subsystem

登録を Include し、 X2Core(= プロフィル ) を追加定義する際にコア階層ので発生した Invalid を例外申請するためのコードです。

(2)Include する QDID と PTS 試験内容の決定手順

[ID] モジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) を Incude

すると、 HID, SPP, PAN, BNEP, HOGP, ScPP は包含されていてほとんどご送付いただいた ICS 項目と一致しているのですが、一部不足しているものもあります。 ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して HID, PAN, HOGP の ICS を御社希望の ICS と比較して「ICS 項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID]) から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポート YES でも NO でも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11 だけは Fluoride 1.5(QDID:[ID]) に包含されてないので PTS 試験レポートをエビデンスとしてアップロードする必要があります。

(3) 御社テストサンプルで PTS 試験を実施上記 (2) でご確認いただく包含された ICS 項目では不足していて試験対象とするプロファイルが決まらないと PTS 試験のテストプランが確定できませんが、仮に HID11 以外は Fluoride 1.5(QDID:[ID]) に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4) テストレポート取得後の作業当方で TCW:[ID] 申請および必要なプロファイルレポートによる代行登録を実施します。 TCW による申請は SIG 管理者の内容確認後の登録確定 ( あるいは

Listing Owner への Reject 通知 ) ですので、 2-5 営業日の登録遅延が発生します。

(5) その他：ご送付いただいた ICS で見つけた問題点

HID11 の Tbale 1 は 1/1 と 1/2 が互いに排他 YES となっています。

1/1
→ C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2
→ C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付した Export ICS の HID11 は 1/1:YES, 1/2:NO
としています。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:16

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 再送 ] [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールで Invalid の説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」、「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または

35/6）サポート条件が満たされていない」、「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」、「[GATT] (1/2

and 4/16)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」

および「[GATT] (1/2 and 4/22)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」という Invalid 表示です。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または 35/6）サポート条件が満たされていない」に減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組み合わせる必要があります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:01

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : Re: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT]

(4/25) サポート条件が満たされていない」という Invalid が表示されています。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組合わせる必要があります。

以上回答いたします。

差出人 : [ID] [ID]( 林建輔 )

送信日時 : 2026 年 2 月 5 日 15:49

宛先 : Itsuo Sakai ; [ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NEC プラットフォームズの林です。

お世話になっております。

お手数ですが、 Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

エラーの見方をよく知りませんが、要約すると

QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT 7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT 7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NEC プラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride 1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya Iida ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件における [ID] お送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID]( 橋本秀昌 ) ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] でログイン後、ページ左上の My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から 2 番目の My

account
をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 6. 2026-02-13 01:24

**From:** Itsuo Sakai
**To:** =?utf-8?B?SEFTSElNT1RPIEhJREVNQVNBKOapi+acrOOAgOengOaYjCk=?= , =?utf-8?B?SEFZQVNISSBLRU5TVUtFKOael+OAgOW7uui8lCk=?= , Masaya Iida , =?utf-8?B?VFNVUlVUQSBEQUlTVUtFKOm2tOeUsOOAgOWkp+S7iyk=?= , =?utf-8?B?bXVyYXlhbWEgdGVydW1hc2Eo5p2R5bGx44CA6Lyd5piMKQ==?= , =?utf-8?B?SE9TSEkgTUFTQVNISSjmmJ/jgIDoi6Xlv5cp?= , Kei Tanaka

NECプラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。

代行登録内容確認書ご送付ありがとうございます。

登録サイトの仕組み上、最初にProduct Listへ登録したProduct Nameが登録の

「Design Name」として扱われます。しかし、今回3種類個別のProduct Nameですので、例えば「[ID]」や「[ID]/HERO3」のような統一的な呼称を

Design Nameとして修正入力しますのでご検討の上、ご連絡ください。

その他の内容は問題ございません。

以上よろしくお願いいたします。

差出人: [ID] [ID](橋本秀昌)

送信日時: 2026年2月13日 08:38

宛先: Itsuo Sakai ; [ID] [ID](林建輔) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [今後の進め方のご提案 ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様

[ID] なし代行登録内容確認書お送りいたします。

齟齬ないかご確認お願いいたします。

このあとのメールにてローカルで酒井様のみに

[ID] あり代行登録内容確認書お送りいたします。

From: Itsuo Sakai

Sent: Thursday, February 12, 2026 7:22 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

⇒ 承知しました。お手数をお掛けしますがよろしくお願いします。
登録したい製品は３種類ございますが
３機種明記すればよろしいでしょうか？

いずれも同じ BT [ID] と HOST STACK が実装されております。
・製品１： [ID]
・製品２： [ID]
・製品３： [ID]

⇒ はい、「5 最初に販売予定の機器の型式（モデル）名」に 3 機種を列記してください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 12 日
19:17

宛先 : Itsuo Sakai ;
[ID] [ID]( 林建輔 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案
] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡ありがとうございます。

パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

登録したい製品は３種類ございますが

３機種明記すればよろしいでしょうか？

いずれも同じ BT [ID] と HOST STACK が実装されております。

・製品１： [ID]

・製品２： [ID]

・製品３： [ID]

From: Itsuo Sakai

Sent: Thursday, February 12, 2026 2:22 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
本日、弊社内部で議論した結果、
全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。
誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

⇒承知しました。プロファイル試験免除で認証登録を進めます。

つきましては添付の代行登録内容確認書にご記入の上、ご返送ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 12 日 14:05

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様本日、弊社内部で議論した結果、

全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。

誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

HID、 PAN、 HOGP における現行機と Fluoride 1.5 の ICS 差分抽出いたしました。

T.B.D. 部が現在、必要性判断検討中でおります。

休み明けに弊社にて議論実施し最終回答させて頂きます。

背景として今回プロジェクトは現行機踏襲いうのが前提条件であり

T.B.D. → N.A とする最終判断を慎重に進めさせて頂きたい所存でおります。

From: Itsuo Sakai

Sent: Tuesday, February 10, 2026 1:17 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
下記２点ご連絡いたします。

【HID11 未採用の件】
弊社で検討した結果、 HID11 未採用という結論に至りました。
お手数ですが HID11 試験は不要でお願いいたします。

⇒ HID11 未採用とのこと承知しました。
【Fluoride 1.5 と弊社提示 ICS 差分の確認】
現在、差分を確認中です。
結果がでましたら連絡させて頂きます。

⇒ SPP、 ScPP および BNEP は必要最低限の ICS サポートであれば問題ありません。

( 既存登録は登録条件として必要最低限の ICS がサポートされています。 )

Fluoride 1.5 の HID、 PAN、 HOGP が御社が必要とする ICS 機能をサポートしているかをご確認ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 10 日 12:24

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡遅くなり申し訳ございません。

先程はお電話ありがとうございました。

下記２点ご連絡いたします。

【HID11 未採用の件】

弊社で検討した結果、 HID11 未採用という結論に至りました。

お手数ですが HID11 試験は不要でお願いいたします。

【Fluoride 1.5 と弊社提示 ICS 差分の確認】

現在、差分を確認中です。

結果がでましたら連絡させて頂きます。

From: Itsuo Sakai

Sent: Friday, February 6, 2026 8:45 AM

To: [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

前のメールで「ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して踏襲した ICS を確認」とお伝えしましたが手間がかかる方法です。 [URL] でログイン後、

以下の URL 参照で直接 Fluoride 1.5(QDID:[ID]) の登録詳細ページのサポートプロファイルとその ICS を確認できますのでこの方法をお勧めします。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 21:38

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、 (2) のプロファイルの ICS の割り切りをお願いします。

(1) 既存登録を Include して発生するコア階層の Invalid の除外申請制度

Bluetooth SIG の Help & Support ページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類の Consistensy

Check 発生の例外申請 (Test Case Waiver) の一つに、今回の Host Stack

の Invlid に使えそうな「TCW [ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW [ID] は既存の Controller Subsystem 登録と既存の Host Subsystem

登録を Include し、 X2Core(= プロフィル ) を追加定義する際にコア階層ので発生した Invalid を例外申請するためのコードです。

(2)Include する QDID と PTS 試験内容の決定手順

[ID] モジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) を Incude

すると、 HID, SPP, PAN, BNEP, HOGP, ScPP は包含されていてほとんどご送付いただいた ICS 項目と一致しているのですが、一部不足しているものもあります。 ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して HID, PAN, HOGP の ICS を御社希望の ICS と比較して「ICS 項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID]) から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポート YES でも NO でも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11 だけは Fluoride 1.5(QDID:[ID]) に包含されてないので PTS 試験レポートをエビデンスとしてアップロードする必要があります。

(3) 御社テストサンプルで PTS 試験を実施上記 (2) でご確認いただく包含された ICS 項目では不足していて試験対象とするプロファイルが決まらないと PTS 試験のテストプランが確定できませんが、仮に HID11 以外は Fluoride 1.5(QDID:[ID]) に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4) テストレポート取得後の作業当方で TCW:[ID] 申請および必要なプロファイルレポートによる代行登録を実施します。 TCW による申請は SIG 管理者の内容確認後の登録確定 ( あるいは

Listing Owner への Reject 通知 ) ですので、 2-5 営業日の登録遅延が発生します。

(5) その他：ご送付いただいた ICS で見つけた問題点

HID11 の Tbale 1 は 1/1 と 1/2 が互いに排他 YES となっています。

1/1
→ C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2
→ C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付した Export ICS の HID11 は 1/1:YES, 1/2:NO
としています。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:16

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 再送 ] [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールで Invalid の説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」、「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または

35/6）サポート条件が満たされていない」、「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」、「[GATT] (1/2

and 4/16)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」

および「[GATT] (1/2 and 4/22)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」という Invalid 表示です。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または 35/6）サポート条件が満たされていない」に減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組み合わせる必要があります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:01

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : Re: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT]

(4/25) サポート条件が満たされていない」という Invalid が表示されています。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組合わせる必要があります。

以上回答いたします。

差出人 : [ID] [ID]( 林建輔 )

送信日時 : 2026 年 2 月 5 日 15:49

宛先 : Itsuo Sakai ; [ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NEC プラットフォームズの林です。

お世話になっております。

お手数ですが、 Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

エラーの見方をよく知りませんが、要約すると

QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT 7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT 7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NEC プラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride 1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya Iida ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件における [ID] お送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID]( 橋本秀昌 ) ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] でログイン後、ページ左上の My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から 2 番目の My

account
をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 7. 2026-02-13 02:14

**From:** Itsuo Sakai
**To:** =?utf-8?B?SEFTSElNT1RPIEhJREVNQVNBKOapi+acrOOAgOengOaYjCk=?= , =?utf-8?B?SEFZQVNISSBLRU5TVUtFKOael+OAgOW7uui8lCk=?= , Masaya Iida , =?utf-8?B?VFNVUlVUQSBEQUlTVUtFKOm2tOeUsOOAgOWkp+S7iyk=?= , =?utf-8?B?bXVyYXlhbWEgdGVydW1hc2Eo5p2R5bGx44CA6Lyd5piMKQ==?= , =?utf-8?B?SE9TSEkgTUFTQVNISSjmmJ/jgIDoi6Xlv5cp?= , Kei Tanaka

NECプラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
現行機が「Communications Terminal」となっておりますので
Product Name(Design Name)：Communications Terminal
に変更いたします。

⇒承知しました。早速のご連絡ありがとうございます。

以上よろしくお願いいたします。

差出人: [ID] [ID](橋本秀昌)

送信日時: 2026年2月13日 11:07

宛先: Itsuo Sakai ; [ID] [ID](林建輔) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [今後の進め方のご提案 ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様現行機が「Communications Terminal」となっておりますので

Product Name(Design Name)： Communications Terminal

に変更いたします。

Pass あり版をこのあと酒井様のみにお送りいたします。

From: Itsuo Sakai

Sent: Friday, February 13, 2026 10:25 AM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。

代行登録内容確認書ご送付ありがとうございます。

登録サイトの仕組み上、最初に Product List へ登録した Product Name が登録の

「Design Name」として扱われます。しかし、今回 3 種類個別の Product Name ですので、例えば「[ID]」や「[ID]/HERO3」のような統一的な呼称を

Design Name として修正入力しますのでご検討の上、ご連絡ください。

その他の内容は問題ございません。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 13 日
08:38

宛先 : Itsuo Sakai ;
[ID] [ID]( 林建輔 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案
] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様

[ID] なし代行登録内容確認書お送りいたします。

齟齬ないかご確認お願いいたします。

このあとのメールにてローカルで酒井様のみに

[ID] あり代行登録内容確認書お送りいたします。

From: Itsuo Sakai

Sent: Thursday, February 12, 2026 7:22 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

⇒承知しました。お手数をお掛けしますがよろしくお願いします。
登録したい製品は３種類ございますが
３機種明記すればよろしいでしょうか？

いずれも同じ BT [ID] と HOST STACK が実装されております。
・製品１： [ID]
・製品２： [ID]
・製品３： [ID]

⇒はい、「5 最初に販売予定の機器の型式（モデル）名」に 3 機種を列記してください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 12 日 19:17

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡ありがとうございます。

パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

登録したい製品は３種類ございますが

３機種明記すればよろしいでしょうか？

いずれも同じ BT [ID] と HOST STACK が実装されております。

・製品１： [ID]

・製品２： [ID]

・製品３： [ID]

From: Itsuo Sakai

Sent: Thursday, February 12, 2026 2:22 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
本日、弊社内部で議論した結果、
全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。
誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

⇒承知しました。プロファイル試験免除で認証登録を進めます。

つきましては添付の代行登録内容確認書にご記入の上、ご返送ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 12 日 14:05

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様本日、弊社内部で議論した結果、

全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。

誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

HID、 PAN、 HOGP における現行機と Fluoride 1.5 の ICS 差分抽出いたしました。

T.B.D. 部が現在、必要性判断検討中でおります。

休み明けに弊社にて議論実施し最終回答させて頂きます。

背景として今回プロジェクトは現行機踏襲いうのが前提条件であり

T.B.D. → N.A とする最終判断を慎重に進めさせて頂きたい所存でおります。

From: Itsuo Sakai

Sent: Tuesday, February 10, 2026 1:17 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
下記２点ご連絡いたします。

【HID11 未採用の件】
弊社で検討した結果、 HID11 未採用という結論に至りました。
お手数ですが HID11 試験は不要でお願いいたします。

⇒ HID11 未採用とのこと承知しました。
【Fluoride 1.5 と弊社提示 ICS 差分の確認】
現在、差分を確認中です。
結果がでましたら連絡させて頂きます。

⇒ SPP、 ScPP および BNEP は必要最低限の ICS サポートであれば問題ありません。

( 既存登録は登録条件として必要最低限の ICS がサポートされています。 )

Fluoride 1.5 の HID、 PAN、 HOGP が御社が必要とする ICS 機能をサポートしているかをご確認ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 10 日 12:24

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡遅くなり申し訳ございません。

先程はお電話ありがとうございました。

下記２点ご連絡いたします。

【HID11 未採用の件】

弊社で検討した結果、 HID11 未採用という結論に至りました。

お手数ですが HID11 試験は不要でお願いいたします。

【Fluoride 1.5 と弊社提示 ICS 差分の確認】

現在、差分を確認中です。

結果がでましたら連絡させて頂きます。

From: Itsuo Sakai

Sent: Friday, February 6, 2026 8:45 AM

To: [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

前のメールで「ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して踏襲した ICS を確認」とお伝えしましたが手間がかかる方法です。 [URL] でログイン後、

以下の URL 参照で直接 Fluoride 1.5(QDID:[ID]) の登録詳細ページのサポートプロファイルとその ICS を確認できますのでこの方法をお勧めします。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 21:38

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、 (2) のプロファイルの ICS の割り切りをお願いします。

(1) 既存登録を Include して発生するコア階層の Invalid の除外申請制度

Bluetooth SIG の Help & Support ページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類の Consistensy

Check 発生の例外申請 (Test Case Waiver) の一つに、今回の Host Stack

の Invlid に使えそうな「TCW [ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW [ID] は既存の Controller Subsystem 登録と既存の Host Subsystem

登録を Include し、 X2Core(= プロフィル ) を追加定義する際にコア階層ので発生した Invalid を例外申請するためのコードです。

(2)Include する QDID と PTS 試験内容の決定手順

[ID] モジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) を Incude

すると、 HID, SPP, PAN, BNEP, HOGP, ScPP は包含されていてほとんどご送付いただいた ICS 項目と一致しているのですが、一部不足しているものもあります。 ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して HID, PAN, HOGP の ICS を御社希望の ICS と比較して「ICS 項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID]) から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポート YES でも NO でも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11 だけは Fluoride 1.5(QDID:[ID]) に包含されてないので PTS 試験レポートをエビデンスとしてアップロードする必要があります。

(3) 御社テストサンプルで PTS 試験を実施上記 (2) でご確認いただく包含された ICS 項目では不足していて試験対象とするプロファイルが決まらないと PTS 試験のテストプランが確定できませんが、仮に HID11 以外は Fluoride 1.5(QDID:[ID]) に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4) テストレポート取得後の作業当方で TCW:[ID] 申請および必要なプロファイルレポートによる代行登録を実施します。 TCW による申請は SIG 管理者の内容確認後の登録確定 ( あるいは

Listing Owner への Reject 通知 ) ですので、 2-5 営業日の登録遅延が発生します。

(5) その他：ご送付いただいた ICS で見つけた問題点

HID11 の Tbale 1 は 1/1 と 1/2 が互いに排他 YES となっています。

1/1
→ C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2
→ C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付した Export ICS の HID11 は 1/1:YES, 1/2:NO
としています。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:16

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 再送 ] [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールで Invalid の説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」、「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または

35/6）サポート条件が満たされていない」、「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」、「[GATT] (1/2

and 4/16)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」

および「[GATT] (1/2 and 4/22)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」という Invalid 表示です。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または 35/6）サポート条件が満たされていない」に減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組み合わせる必要があります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:01

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : Re: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT]

(4/25) サポート条件が満たされていない」という Invalid が表示されています。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組合わせる必要があります。

以上回答いたします。

差出人 : [ID] [ID]( 林建輔 )

送信日時 : 2026 年 2 月 5 日 15:49

宛先 : Itsuo Sakai ; [ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NEC プラットフォームズの林です。

お世話になっております。

お手数ですが、 Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

エラーの見方をよく知りませんが、要約すると

QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT 7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT 7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NEC プラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride 1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya Iida ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件における [ID] お送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID]( 橋本秀昌 ) ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] でログイン後、ページ左上の My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から 2 番目の My

account
をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

---

## 8. 2026-02-20 03:47

**From:** Itsuo Sakai
**To:** =?utf-8?B?SEFTSElNT1RPIEhJREVNQVNBKOapi+acrOOAgOengOaYjCk=?= , =?utf-8?B?SEFZQVNISSBLRU5TVUtFKOael+OAgOW7uui8lCk=?= , Masaya Iida , =?utf-8?B?VFNVUlVUQSBEQUlTVUtFKOm2tOeUsOOAgOWkp+S7iyk=?= , =?utf-8?B?bXVyYXlhbWEgdGVydW1hc2Eo5p2R5bGx44CA6Lyd5piMKQ==?= , =?utf-8?B?SE9TSEkgTUFTQVNISSjmmJ/jgIDoi6Xlv5cp?= , Kei Tanaka

NECプラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
その後、認証手続きのご進捗いかがでしょうか。
簡単で結構ですのでご進捗ご連絡頂けたらと思っております。

⇒すでに登録準備は完了しています。しかし現在当社HQ(台湾)への稟議中で、

あいにく2/22まで旧正月休暇のために来週のSIG送金を予定しております。

具体的なReciption Number発番見込日(登録確定操作可能日)が決まりましたらお知らせします。

以上よろしくお願いいたします。

差出人: [ID] [ID](橋本秀昌)

送信日時: 2026年2月20日 12:31

宛先: Itsuo Sakai ; [ID] [ID](林建輔) ; Masaya Iida ; [ID] [ID](鶴田大介) ; murayama terumasa(村山輝昌) ; HOSHI [ID](星若志) ;
Kei Tanaka

件名: RE: [今後の進め方のご提案 ] Re: Bluetooth SIG認証送金を進めるためのInvoice取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様その後、認証手続きのご進捗いかがでしょうか。

簡単で結構ですのでご進捗ご連絡頂けたらと思っております。

From: Itsuo Sakai

Sent: Friday, February 13, 2026 11:15 AM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
現行機が「Communications Terminal」となっておりますので
Product Name(Design Name)： Communications
Terminal
に変更いたします。

⇒ 承知しました。早速のご連絡ありがとうございます。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 13 日
11:07

宛先 : Itsuo Sakai ;
[ID] [ID]( 林建輔 ) ;
Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ;
HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案
] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様現行機が「Communications Terminal」となっておりますので

Product Name(Design Name)： Communications Terminal

に変更いたします。

Pass あり版をこのあと酒井様のみにお送りいたします。

From: Itsuo Sakai

Sent: Friday, February 13, 2026 10:25 AM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。

代行登録内容確認書ご送付ありがとうございます。

登録サイトの仕組み上、最初に Product List へ登録した Product Name が登録の

「Design Name」として扱われます。しかし、今回 3 種類個別の Product Name ですので、例えば「[ID]」や「[ID]/HERO3」のような統一的な呼称を

Design Name として修正入力しますのでご検討の上、ご連絡ください。

その他の内容は問題ございません。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 13 日 08:38

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様

[ID] なし代行登録内容確認書お送りいたします。

齟齬ないかご確認お願いいたします。

このあとのメールにてローカルで酒井様のみに

[ID] あり代行登録内容確認書お送りいたします。

From: Itsuo Sakai

Sent: Thursday, February 12, 2026 7:22 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

⇒承知しました。お手数をお掛けしますがよろしくお願いします。
登録したい製品は３種類ございますが
３機種明記すればよろしいでしょうか？

いずれも同じ BT [ID] と HOST STACK が実装されております。
・製品１： [ID]
・製品２： [ID]
・製品３： [ID]

⇒はい、「5 最初に販売予定の機器の型式（モデル）名」に 3 機種を列記してください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 12 日 19:17

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡ありがとうございます。

パスワード等含まれる内容の為別途ローカルで酒井様のみお送りさせて頂きます。

登録したい製品は３種類ございますが

３機種明記すればよろしいでしょうか？

いずれも同じ BT [ID] と HOST STACK が実装されております。

・製品１： [ID]

・製品２： [ID]

・製品３： [ID]

From: Itsuo Sakai

Sent: Thursday, February 12, 2026 2:22 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
本日、弊社内部で議論した結果、
全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。
誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

⇒承知しました。プロファイル試験免除で認証登録を進めます。

つきましては添付の代行登録内容確認書にご記入の上、ご返送ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 12 日 14:05

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様本日、弊社内部で議論した結果、

全ての [ID] の ICS は、 Fluoride 1.5 に合わせるという結論となりました。

誠にお手数ですが上記方針で作業進めて頂くようお願いいたします。

HID、 PAN、 HOGP における現行機と Fluoride 1.5 の ICS 差分抽出いたしました。

T.B.D. 部が現在、必要性判断検討中でおります。

休み明けに弊社にて議論実施し最終回答させて頂きます。

背景として今回プロジェクトは現行機踏襲いうのが前提条件であり

T.B.D. → N.A とする最終判断を慎重に進めさせて頂きたい所存でおります。

From: Itsuo Sakai

Sent: Tuesday, February 10, 2026 1:17 PM

To: [ID] [ID]( 橋本秀昌 ) ; [ID] [ID]( 林建輔 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ橋本様アリオンの酒井です。いつもお世話になっております。
下記２点ご連絡いたします。

【HID11 未採用の件】
弊社で検討した結果、 HID11 未採用という結論に至りました。
お手数ですが HID11 試験は不要でお願いいたします。

⇒ HID11 未採用とのこと承知しました。
【Fluoride 1.5 と弊社提示 ICS 差分の確認】
現在、差分を確認中です。
結果がでましたら連絡させて頂きます。

⇒ SPP、 ScPP および BNEP は必要最低限の ICS サポートであれば問題ありません。

( 既存登録は登録条件として必要最低限の ICS がサポートされています。 )

Fluoride 1.5 の HID、 PAN、 HOGP が御社が必要とする ICS 機能をサポートしているかをご確認ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 10 日 12:24

宛先 : Itsuo Sakai ; [ID] [ID]( 林建輔 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン酒井様ご連絡遅くなり申し訳ございません。

先程はお電話ありがとうございました。

下記２点ご連絡いたします。

【HID11 未採用の件】

弊社で検討した結果、 HID11 未採用という結論に至りました。

お手数ですが HID11 試験は不要でお願いいたします。

【Fluoride 1.5 と弊社提示 ICS 差分の確認】

現在、差分を確認中です。

結果がでましたら連絡させて頂きます。

From: Itsuo Sakai

Sent: Friday, February 6, 2026 8:45 AM

To: [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

Subject: Re: [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

前のメールで「ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して踏襲した ICS を確認」とお伝えしましたが手間がかかる方法です。 [URL] でログイン後、

以下の URL 参照で直接 Fluoride 1.5(QDID:[ID]) の登録詳細ページのサポートプロファイルとその ICS を確認できますのでこの方法をお勧めします。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 21:38

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 今後の進め方のご提案 ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様、橋本様アリオンの酒井です。いつもお世話になっております。

今後の進め方を検討しましたので順を追って説明いたします。

御社にはこの進め方へのご同意と、 (2) のプロファイルの ICS の割り切りをお願いします。

(1) 既存登録を Include して発生するコア階層の Invalid の除外申請制度

Bluetooth SIG の Help & Support ページの「ICS Form Inconsistencies

for Inter-Layer Dependencies」という項目に、数種類の Consistensy

Check 発生の例外申請 (Test Case Waiver) の一つに、今回の Host Stack

の Invlid に使えそうな「TCW [ID]」を見つけました。

TCW [ID] - TCW for X2Core only modification/addition to waive

Core invalids where no changes were made to referenced QDIDs/DNs

of Core Host Configuration plus Core Controller Configuration

TCW [ID] は既存の Controller Subsystem 登録と既存の Host Subsystem

登録を Include し、 X2Core(= プロフィル ) を追加定義する際にコア階層ので発生した Invalid を例外申請するためのコードです。

(2)Include する QDID と PTS 試験内容の決定手順

[ID] モジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) を Incude

すると、 HID, SPP, PAN, BNEP, HOGP, ScPP は包含されていてほとんどご送付いただいた ICS 項目と一致しているのですが、一部不足しているものもあります。 ICS Export ファイルを添付しますので、どなたかの

Qualification Workspce に Inport して HID, PAN, HOGP の ICS を御社希望の ICS と比較して「ICS 項目不足が譲れない」プロファイルに関しては

Fluoride 1.5(QDID:[ID]) から引き継いた内容を削除して新たに試験レポートエビデンスとして登録する必要があります。試験レポートを取得するプロファイルが洗い出せましたらお知らせください。差分がサポート YES でも NO でも良いものは、割り切って引き継ぎプロファイルの活用をお勧めします。

HID11 だけは Fluoride 1.5(QDID:[ID]) に包含されてないので PTS 試験レポートをエビデンスとしてアップロードする必要があります。

(3) 御社テストサンプルで PTS 試験を実施上記 (2) でご確認いただく包含された ICS 項目では不足していて試験対象とするプロファイルが決まらないと PTS 試験のテストプランが確定できませんが、仮に HID11 以外は Fluoride 1.5(QDID:[ID]) に包含されたプロファイルをそのまま踏襲する場合の試験項目は以下の通りです。

<HID11>

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HGR/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HCT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/HIT/[ID]

HID11/HOS/CGSIT/SFC/[ID]

HID11/HOS/CDD/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCE/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HCR/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

HID11/HOS/HRE/[ID]

<IOPT>

IOPT/SR/COD/[ID]

IOPT/HID11/HOS/CGSIT/SFC/[ID]

(4) テストレポート取得後の作業当方で TCW:[ID] 申請および必要なプロファイルレポートによる代行登録を実施します。 TCW による申請は SIG 管理者の内容確認後の登録確定 ( あるいは

Listing Owner への Reject 通知 ) ですので、 2-5 営業日の登録遅延が発生します。

(5) その他：ご送付いただいた ICS で見つけた問題点

HID11 の Tbale 1 は 1/1 と 1/2 が互いに排他 YES となっています。

1/1
→ C.1: Excluded IF HID11 1/2 &quot;Limited HID Host, Report protocol&quot;

1/2
→ C.3: Excluded IF HID11 1/1 &quot;General HID Host, Report protocol&quot;

添付した Export ICS の HID11 は 1/1:YES, 1/2:NO
としています。

以上よろしくお願いいたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:16

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : [ 再送 ] [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。

先程のメールで Invalid の説明が略式でわかりにくいので当該部分を書き直して再送します。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」、「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または

35/6）サポート条件が満たされていない」、「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」、「[GATT] (1/2

and 4/16)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」

および「[GATT] (1/2 and 4/22)
をサポートしているが、 [GATT] (4/25) サポート条件が満たされていない」という Invalid 表示です。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (7/6) をサポートしているが、 [GAP] （25/6
または 35/6）サポート条件が満たされていない」に減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組み合わせる必要があります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2026 年 2 月 5 日 18:01

宛先 : [ID] [ID]( 林建輔 ) ; [ID] [ID]( 橋本秀昌 )
; Masaya Iida ; [ID] [ID]( 鶴田大介 )
; murayama terumasa( 村山輝昌 ) ; HOSHI
[ID]( 星若志 ) ; Kei Tanaka

件名 : Re: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NEC プラットフォームズ林様アリオンの酒井です。いつもお世話になっております。
お手数ですが、 Google Fluoride 1.6 [ID] との適合性も調べていただけますか？

⇒仮 Project で Consistency Check を掛けたところ、 Google Fluoride 1.5 [ID]

と同じ以下の Invalid が発生しました。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
エラーの見方をよく知りませんが、要約すると
QDID:[ID] と Fluoride 1.4 の組み合わせでは、 GAP と GATT
7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」および「[GATT] (1/2 and 4/15)
をサポートしているが、 [GATT]

(4/25) サポート条件が満たされていない」という Invalid が表示されています。
QDID:[ID] と Fluoride 1.5 の組み合わせでも、同様に GAP と GATT
7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している

⇒「[GATT] (7/5) をサポートしているが、 [GAP] （25/5
または 35/5）サポート条件が満たされていない」だけに減少しています。
使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6,
35/6）を満たすバージョンであるか？
→デバイスメーカに確認する必要がありますか？

⇒ GAP, GATT は Host Subsystem の階層で、モジュール（QDID:[ID]）は無関係です。

単に Fluoride 1.4/1.5/1.6 自身が包含する内部不整合で、登録時点では Invalid=0

でないと登録できませんので、登録以降に Bluetooth SIG が GAP と GATT の ICS チェックルールを追加したものと推測します。このような Invalid は Fluoride 1.4/1.5/1.6 に代わる Invalid の出ない Host Stack と組合わせる必要があります。

以上回答いたします。

差出人 : [ID] [ID]( 林建輔 )

送信日時 : 2026 年 2 月 5 日 15:49

宛先 : Itsuo Sakai ; [ID] [ID]( 橋本秀昌 ) ;
Masaya Iida ; [ID] [ID]( 鶴田大介 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】指定した範囲（必要範囲）以外への情報開示を禁止

To：アリオン酒井様

NEC プラットフォームズの林です。

お世話になっております。

お手数ですが、 Google Fluoride 1.6
[ID] との適合性も調べていただけますか？
GAP
GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
GATT
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory
4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator
GAP
If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)
If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)
If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

エラーの見方をよく知りませんが、要約すると

QDID:[ID] と Fluoride
1.4 の組み合わせでは、 GAP と GATT 7/5 をサポートする際に必要な GAP 機能（25/5
または 35/5）が不足している。
QDID:[ID] と Fluoride
1.5 の組み合わせでも、同様に GAP と GATT 7/6 をサポートする際に必要な GAP 機能（25/6
または 35/6）が不足している使用しているモジュール（QDID:[ID]）が、 GAP の要件（25/5, 35/5
または 25/6, 35/6）を満たすバージョンであるか？

→デバイスメーカに確認する必要がありますか？

以上、よろしくお願いいたします。

---

林建輔 (Hayashi Kensuke)

NEC プラットフォームズパブリックプロダクツ統括部先進技術開発グループ

--Separator@

From: Itsuo Sakai

Sent: Thursday, February 5, 2026 2:29 PM

To: [ID] [ID]( 橋本秀昌 ) ; Masaya Iida ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: [Google Fluoride 1.4/1.5 は使えませんでした ] Re: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様アリオンの酒井です。いつもお世話になっております。

私の仮 Project でモジュール (QDID:[ID]) と本日ご指示いただいた Fluoride 1.4

(QDID:[ID]) の組み合わせた段階 ( プロファイル追加前 ) で、 Contensisty
Check

を掛けたところ、以下の致命的な Invalid が発生するためこの組み合わせは不可という結論となります。試しに Fluoride 1.3 でも試しましたが同じ結果でした。

GAP

GAP > GATT | If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

GAP > GATT | If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GAP > GATT | If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

GATT

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/15) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/16) are Supported then [GATT] (4/25) is Mandatory

4:C.7 | If [CORE] (2a/50) and [GATT] (1/2 and 4/22) are Supported then [GATT] (4/25) is Mandator

次にモジュール (QDID:[ID]) と Fluoride 1.5(QDID:[ID]) の組み合わせた段階

( プロファイル追加前 ) で、 Contensisty Check を掛けるとこちらも以下の致命的な

Invalid が発生します。このためこの組み合わせは不可という結論となります。

GAP

If [GAP] and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [CORE] (40/3) and [GATT] (7/5) are Supported then it is Mandatory to Support at least one of [GAP] (25/5 or 35/5)

If [GAP] and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

If [CORE] (40/3) and [GATT] (7/6) are Supported then it is Mandatory to Support at least one of [GAP] (25/6 or 35/6)

従ってご指示いただいた Goole LLC の Fluoride シリーズは現在の登録サイトでは

Include できないことという結論になりまますので代替可能な登録済 Fluoride あるいは BlueZ を選定いただくようお願いします。

PS:
一旦登録費送金代行を止めたほうがよろしければ、至急営業の飯田にご指示ください。

以上よろしくお願いいたします。

差出人 : [ID] [ID]( 橋本秀昌 )

送信日時 : 2026 年 2 月 5 日 14:00

宛先 : Masaya Iida ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

件名 : RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

【秘密】

FROM： NECPF 橋本です

TO：アリオン飯田様遅くなり申し訳ございません。

本件における [ID] お送りいたします。

ご確認お願いいたします。

From: Masaya Iida

Sent: Wednesday, February 4, 2026 5:23 PM

To: [ID] [ID]( 橋本秀昌 ) ; Itsuo Sakai ;
[ID] [ID]( 鶴田大介 ) ; [ID] [ID]( 林建輔 ) ;
murayama terumasa( 村山輝昌 ) ; HOSHI [ID]( 星若志 ) ;
Kei Tanaka

Subject: RE: Bluetooth SIG 認証送金を進めるための Invoice 取得のお願い

NECPF 橋本様いつもお世話になっております。

アリオンの飯田です。

先ほどはお電話ありがとうございました。

[URL] でログイン後、ページ左上の My
blue アイコンをクリックすると下図のダイヤログが開きますので、下から 2 番目の My

account
をクリックするとログインしているアカウントの登録内容が表示されます。

以上、よろしくお願いいたします。

アリオン株式会社ビジネスソリューション事業部営業統括部飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階
