# thread_0061: Re: [ALAP] HM23 Bluetooth SIG認証について

- Message count: 10
- Source JSON: `thread_0061.json`

---

## 1. 2024-09-10 05:10

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura , Jun Wang

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23の登録(予定)情報ご連絡ありがとうございます。
HM23はAH00ICBというモデルで、D066499で登録済みです。
End Product登録で参照しているQDIDは以下です。
[ID] (Controller Subsystem)　- [ID] (Component (Tested))
[ID] (Host Subsystem)
[ID] (Profile Subsystem)
Android OSのUpdateに伴い217713 (Host Subsystem)と226611 (Profile Subsystem)が変更となり、
弊社では今後取得される新しいA Host-Core ConfigurationとX2Core Layer(Profile Subsystem)を参照してEnd Product登録を行う予定です。

⇒ここまで理解しました。
AH00ICBは他社で試験をして登録したモデルではありますが、
Host SubsystemとProfile Subsystem変更後の登録においてはHM26と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

⇒ありがとうございます。
そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。
本件、他社のテストレポートになってしまいますがそれを参照したSIG登録のサポート業務を御社にお願いすることは可能でしょうか？
(A Host-Core Configuration(新規取得)＋X2Core Layer(新規取得)＋Component(従来登録済み)＋前回登録時の他社テストレポート)

⇒はい、他社レポートで問題ございません。
なお認証取得完了はHM23/HM26共に2025年4月がMUSTとなっております。
他に必要な情報がございましたらお申し付けください。

⇒MH26と同様、参照(Include)予定の新規登録のA Host-Core ConfigurationとX2Core Layer(Profile

Subsystem)のDN(Design Number)が判明しましたら階層間不整合を確認いたしますのでお知らせください。

テストレポートに関してですが、2024/12/28から有効になるプロファイルの試験項目がTCRL2024-1で予告されています。可能であければ早めにテストレポートをご提出いただければ2024/12/28以降に当該レポートがそのまま使えるかどうかを事前確認いたします。

以上よろしくお願いいたします。

差出人: Hiroaki Fukaura

送信日時: 2024年9月10日 13:43

宛先: Jun Wang ; Itsuo Sakai

件名: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れましたHM23のBluetooth SIG認証について相談させてください。

HM23はAH00ICBというモデルで、D066499で登録済みです。

End Product登録で参照しているQDIDは以下です。

[ID] (Controller Subsystem)　-
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OSのUpdateに伴い217713 (Host Subsystem)と226611 (Profile Subsystem)が変更となり、

弊社では今後取得される新しいA Host-Core ConfigurationとX2Core Layer(Profile Subsystem)を参照して

End Product登録を行う予定です。

AH00ICBは他社で試験をして登録したモデルではありますが、

Host SubsystemとProfile Subsystem変更後の登録においてはHM26と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照したSIG登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration(新規取得)＋X2Core Layer(新規取得)＋Component(従来登録済み)＋前回登録時の他社テストレポート)

なお認証取得完了はHM23/HM26共に2025年4月がMUSTとなっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

---

## 2. 2024-09-19 02:29

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID])の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、2024/12/28以降にそのまま使用可能であるかご確認いただけますか？⇒RFおよびRF PHYレポートおよびログを受領しました。

私のWarkspaceでRFとRF PHYだけの仮Projectを作成し、D066499のRFとRF PHYのICSを入力して

[ID](2024/12/02から必須)でTest Planを出力して受領したRFおよびRF PHYレポートと逐次比較しました。

その結果RFはレポートと一致するとともに、[ID]1およびTCRL2024-2で追加される試験項目はありませんでした。

RF PHYはTCRL2024-1およびTCRL2024-2で追加される試験項目はないものの、「RFPHY/TRM/[ID]」

がレポートに不足していました。この項目はTCRL2022-1で新設されたもので、D066499が登録された2024-06-04の1年以上前に必須項目でしたので、BQTFの確認ミスと思われます。

しかし6/30以前の登録制度ではデザイン登録部分(D066499ではController Subsystem)にQDID:

186292がSIGから付与されて形式的にSIGの確認済になっています。したがってご依頼の「[ID]

(Host Subsystem)と226611 (Profile Subsystem)を更新した登録」ではQDID:186292をInclude

し、全階層に対してICSの変更・追加を行わなければ新たにRF PHYの試験要求は発生しません。

言い換えれば敢えてRF PHYの「RFPHY/TRM/[ID]」を追加試験しなくても新登録サイトの登録過程で「形式上」は不都合が生じません。

立場上「RFPHY/TRM/[ID]Cの追加試験は不要」と断定的にアドバイスできないのですが、既に

D066499は承認された登録ですのでSIGからこの試験項目の不足を指摘される可能性は無いものと思います。

以上回答いたします。

差出人: Itsuo Sakai

送信日時: 2024年9月18日 18:13

宛先: Hiroaki Fukaura

件名: Re: [ALAP] HM23 Bluetooth SIG認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID])の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、2024/12/28以降にそのまま使用可能であるかご確認いただけますか？ ⇒承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人: Hiroaki Fukaura

送信日時: 2024年9月18日 16:21

宛先: Itsuo Sakai

件名: RE: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ; Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) -
[ID] (Component (Tested))
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

送信日時 : 2024 年 9 月 10 日
13:43

宛先 : Jun
Wang ; Itsuo Sakai

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

## 3. 2024-09-19 07:03

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートはRFPHY/TRM/[ID]Cが不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。
そこでRFPHY/TRM/[ID]Cの試験について教えてください。
・RFPHY/TRM/[ID]Cは(可能かどうかで言えば)差分試験として実施できるものでしょうか？

⇒差分(追加)試験は可能です。しかし、本来その項目が必要な D066499へは反映できません。
・仮にRFPHY/TRM/[ID]Cを差分試験として実施してなおかつ登録に反映させる場合には、
ICS変更に相当しRF PHYの試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ご依頼の「[ID]([ID]/Controller Subsystem)＋[ID](Host Subsystem)と226611 (Profile

Subsystem)を更新した登録」では、[ID]([ID])をIncludeした取得したICSそのものにRFPHY

/TRM/[ID]C試験が含まれますが、形式的に186292([ID])の登録時点で当該試験項目はクリアしたものとして扱われます。

敢えて更新登録でRF PHYのICSの任意の項目を修正→元に戻すとTest PlanにRF PHY階層の試験要求が出力されますのでRFPHY/TRM/[ID]Cを差分試験を反映させることは可能ですが、[ID](Host

Subsystem)と226611(Profile Subsystem)を更新した登録と186292([ID])との階層間不整合のチェック対象となって217713(Host Subsystem)と226611 (Profile Subsystem)を更新した登録の機能次第ではリスクが発生します。（例えば更新したHost Subsystem相当の登録がIsochronous

モードをサポート、あるいはAoA/AoDをサポートした場合です。）

ちなみに186292([ID])に現状の217713(Host Subsystem)と226611(Profile Subsystem)をInclude

した登録で、RF PHYを修正→元に戻すと階層間チェックが実施されて下記のようにScPPが不足という結果になります。(Layer/ICSに一切手をいれなければ階層間不整合チェックは行われない)

<SCPP>

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported then [SCPP] (7/1) is Mandatoryn
・もしRFPHY/TRM/[ID]Cのみを追加で行える場合、試験費用はどれ程でしょうか？

⇒当社では1項目の試験実績がないため費用設定も無いのですが、2項目試験ならば￥200,000です。

しかし、今回の事例は明らかにD066499/Controller SubsystemをサポートしたBQTFのミスですので、

担当したSGS台湾にRFPHY/TRM/[ID]Cの無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人: Hiroaki Fukaura

送信日時: 2024年9月19日 14:58

宛先: Itsuo Sakai

件名: RE: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

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

差出人 :
Itsuo Sakai

送信日時 :
2024 年 9 月 18 日
18:13

宛先 :
Hiroaki Fukaura

件名 :
Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2024 年 9 月 18 日
16:21

宛先 :
Itsuo Sakai

件名 :
RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ; Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) -
[ID] (Component (Tested))
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

送信日時 : 2024 年 9 月 10 日
13:43

宛先 : Jun
Wang ; Itsuo Sakai

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

## 4. 2024-09-24 08:20

**From:** Itsuo Sakai
**To:** Hitomi Ohira , Hiroaki Fukaura

アルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。
HM23、HM26とそれぞれにおける対応方法について改めてMTGにて相談させて頂きたいと思っております。
弊社都合にて大変恐縮ではございますが、次週以降にてMTG開催させて頂ければと思っておりますので引き続きご協力頂きたく、開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

⇒承知しました。ご連絡をお待ちしております。
尚、以前に懸念事項としてご連絡頂いていたPower Classにつきましては
HM23/26共にQualcommにてClass1のサポートを削除したsubset DNを対応頂けるとのことで連絡頂いております。
また、A14として10/31を目処に旧QDID取得予定となっているHost subsystem/Profile subsystemのICS
Detailsですが、こちらについてもHM23/26共に A13 Profile Subsystem([ID])、Host Subsystem
([ID])参照にて問題ない旨 Qualcommより連絡頂いております。

⇒Q社の対応が確認でき、安心しました。

引き続きよろしくお願いいたいます。

差出人: Hitomi Ohira

送信日時: 2024年9月24日 16:54

宛先: Itsuo Sakai ; Hiroaki Fukaura

件名: RE: [ALAP] HM23 Bluetooth SIG認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、 HM26 とそれぞれにおける対応方法について改めて MTG にて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にて MTG 開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていた Power Class につきましては

HM23/26 共に Qualcomm にて Class1 のサポートを削除した subset
DN を対応頂けるとのことで連絡頂いております。

また、 A14 として 10/31 を目処に旧 QDID 取得予定となっている Host subsystem/Profile subsystem の ICS
Details ですが、

こちらについても HM23/26 共に
A13 Profile Subsystem([ID])、 Host Subsystem([ID]) 参照にて問題ない旨
Qualcomm より連絡頂いております。

取り急ぎご連絡まで。

/eom

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 4:04 PM

To: 深浦裕章 Hiroaki Fukaura

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
前回テストレポートは RFPHY/TRM/[ID] が不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこで RFPHY/TRM/[ID] の試験について教えてください。

・ RFPHY/TRM/[ID] は ( 可能かどうかで言えば ) 差分試験として実施できるものでしょうか？

⇒ 差分 ( 追加 ) 試験は可能です。しかし、本来その項目が必要な
[ID] へは反映できません。
・仮に RFPHY/TRM/[ID] を差分試験として実施してなおかつ登録に反映させる場合には、
ICS 変更に相当し RF
PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller
Subsystem) ＋ [ID](Host Subsystem) と [ID]
(Profile

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

差出人 :
Hiroaki Fukaura

送信日時 :
2024 年 9 月 19 日
14:58

宛先 :
Itsuo Sakai

件名 :
RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

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

差出人 :
Itsuo Sakai

送信日時 :
2024 年 9 月 18 日
18:13

宛先 :
Hiroaki Fukaura

件名 :
Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 :
Hiroaki Fukaura

送信日時 :
2024 年 9 月 18 日
16:21

宛先 :
Itsuo Sakai

件名 :
RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？

お手数おかけしますが、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, September 10, 2024 2:10 PM

To: 深浦裕章 Hiroaki Fukaura ; Jun Wang

Subject: Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

HM23 の登録 ( 予定 ) 情報ご連絡ありがとうございます。
HM23 は [ID] というモデルで、 [ID] で登録済みです。
End Product 登録で参照している QDID は以下です。
[ID] (Controller Subsystem) -
[ID] (Component (Tested))
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

送信日時 : 2024 年 9 月 10 日
13:43

宛先 : Jun
Wang ; Itsuo Sakai

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

## 5. 2024-09-25 07:07

**From:** Itsuo Sakai
**To:** Hitomi Ohira

アルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
早速ですが、HM26にて使用しているQCA66988(QDID [ID])にてDN Q307964が作成され、
Subset DN [ID] も作成頂けた旨連絡頂いております。
Subset DNにて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、
取り急ぎ本対応にて先に懸念事項として連絡頂いた点につきましてクリアとなるか確認頂けますでしょうか？

⇒[ID](QDID [ID])のSubset DN: Q307964でのHM26の登録可能性を私のQuaification Workspace

の仮Projectを作成して「LL-RF PHY間のClass 1に関する階層間不整合が出ず、他の階層間不整合も

QDID 179073と同じTCW(Test Case Waiver対象項目)」であることを確認しました。

この結果、もし御社がRF/RF PHY試験レポートをエビデンスとしてCore-Controller(旧Controller

Subsystem)の登録を希望される場合でも、Subset DN: Q307964で問題なく登録できることが確認できました。

以上よろしくお願いいたします。

差出人: Hitomi Ohira

送信日時: 2024年9月25日 13:16

宛先: Itsuo Sakai

件名: RE: [ALAP] HM23 Bluetooth SIG認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、HM26にて使用しているQCA66988(QDID [ID])にてDN Q307964が作成され、

Subset DN [ID] も作成頂けた旨連絡頂いております。

Subset DNにて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

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

差出人 : Hitomi Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo Sakai ;
Hiroaki Fukaura

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、HM26とそれぞれにおける対応方法について改めてMTGにて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にてMTG開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていたPower Classにつきましては

HM23/26共にQualcommにてClass1のサポートを削除したsubset DNを対応頂けるとのことで連絡頂いております。

また、A14として10/31を目処に旧QDID取得予定となっているHost subsystem/Profile subsystemのICS Detailsですが、

こちらについてもHM23/26共に A13 Profile Subsystem([ID])、Host Subsystem([ID])参照にて問題ない旨 Qualcommより連絡頂いております。

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
ICS 変更に相当し RF
PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller
Subsystem) ＋ [ID](Host Subsystem) と [ID]
(Profile

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

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported
then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported
then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートはRFPHY/TRM/[ID]Cが不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこでRFPHY/TRM/[ID]Cの試験について教えてください。

・RFPHY/TRM/[ID]Cは(可能かどうかで言えば)差分試験として実施できるものでしょうか？

・仮にRFPHY/TRM/[ID]Cを差分試験として実施してなおかつ登録に反映させる場合には、

ICS変更に相当しRF PHYの試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もしRFPHY/TRM/[ID]Cのみを追加で行える場合、試験費用はどれ程でしょうか？

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

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki Fukaura

件名 : Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID])の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、2024/12/28以降にそのまま使用可能であるかご確認いただけますか？

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

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun Wang ;
Itsuo Sakai

件名 : [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れましたHM23のBluetooth SIG認証について相談させてください。

HM23はAH00ICBというモデルで、D066499で登録済みです。

End Product登録で参照しているQDIDは以下です。

[ID] (Controller Subsystem)　-
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OSのUpdateに伴い217713 (Host Subsystem)と226611 (Profile Subsystem)が変更となり、

弊社では今後取得される新しいA Host-Core ConfigurationとX2Core Layer(Profile Subsystem)を参照して

End Product登録を行う予定です。

AH00ICBは他社で試験をして登録したモデルではありますが、

Host SubsystemとProfile Subsystem変更後の登録においてはHM26と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照したSIG登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration(新規取得)＋X2Core Layer(新規取得)＋Component(従来登録済み)＋前回登録時の他社テストレポート)

なお認証取得完了はHM23/HM26共に2025年4月がMUSTとなっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

差出人: Hitomi Ohira

送信日時: 2024年9月25日 13:16

宛先: Itsuo Sakai

件名: RE: [ALAP] HM23 Bluetooth SIG認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、HM26にて使用しているQCA66988(QDID [ID])にてDN Q307964が作成され、

Subset DN [ID] も作成頂けた旨連絡頂いております。

Subset DNにて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

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

差出人 : Hitomi Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo Sakai ;
Hiroaki Fukaura

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、HM26とそれぞれにおける対応方法について改めてMTGにて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にてMTG開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていたPower Classにつきましては

HM23/26共にQualcommにてClass1のサポートを削除したsubset DNを対応頂けるとのことで連絡頂いております。

また、A14として10/31を目処に旧QDID取得予定となっているHost subsystem/Profile subsystemのICS Detailsですが、

こちらについてもHM23/26共に A13 Profile Subsystem([ID])、Host Subsystem([ID])参照にて問題ない旨 Qualcommより連絡頂いております。

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
ICS 変更に相当し RF
PHY の試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

⇒ ご依頼の「[ID]([ID]/Controller
Subsystem) ＋ [ID](Host Subsystem) と [ID]
(Profile

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

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (7a/1) are Supported
then [SCPP] (1/2) is Mandatory

SCPP > HOGP| If [CORE] (40/3) and [HOGP] (9/4) are Supported
then [SCPP] (7/1) is Mandatoryn
・もし RFPHY/TRM/[ID] のみを追加で行える場合、試験費用はどれ程でしょうか？

⇒ 当社では 1 項目の試験実績がないため費用設定も無いのですが、 2 項目試験ならば￥ 200,000 です。

しかし、今回の事例は明らかに [ID]/Controller Subsystem をサポートした BQTF のミスですので、

担当した SGS 台湾に RFPHY/TRM/[ID] の無償追加試験を求める権利がありますのでご検討ください。

以上回答いたします。

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートはRFPHY/TRM/[ID]Cが不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこでRFPHY/TRM/[ID]Cの試験について教えてください。

・RFPHY/TRM/[ID]Cは(可能かどうかで言えば)差分試験として実施できるものでしょうか？

・仮にRFPHY/TRM/[ID]Cを差分試験として実施してなおかつ登録に反映させる場合には、

ICS変更に相当しRF PHYの試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もしRFPHY/TRM/[ID]Cのみを追加で行える場合、試験費用はどれ程でしょうか？

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

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki Fukaura

件名 : Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID])の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、2024/12/28以降にそのまま使用可能であるかご確認いただけますか？

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

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun Wang ;
Itsuo Sakai

件名 : [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れましたHM23のBluetooth SIG認証について相談させてください。

HM23はAH00ICBというモデルで、D066499で登録済みです。

End Product登録で参照しているQDIDは以下です。

[ID] (Controller Subsystem)　-
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OSのUpdateに伴い217713 (Host Subsystem)と226611 (Profile Subsystem)が変更となり、

弊社では今後取得される新しいA Host-Core ConfigurationとX2Core Layer(Profile Subsystem)を参照して

End Product登録を行う予定です。

AH00ICBは他社で試験をして登録したモデルではありますが、

Host SubsystemとProfile Subsystem変更後の登録においてはHM26と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照したSIG登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration(新規取得)＋X2Core Layer(新規取得)＋Component(従来登録済み)＋前回登録時の他社テストレポート)

なお認証取得完了はHM23/HM26共に2025年4月がMUSTとなっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

---

## 6. 2024-10-04 08:29

**From:** Itsuo Sakai
**To:** Hitomi Ohira

アルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
先日ご相談させて頂きましたHM23/HM26 Bluetooth認証試験についてのMTG開催につきまして、
弊社側都合にて大変恐縮なのですが、以下の通りにてMTG開催日時案を提示させて頂きますので、
酒井様のご都合のよい日時をご連絡頂けます様よろしくお願い致します。

⇒それでは下記日時でお願いします。

10/8(火) 14:00～15:00

以上よろしくお願いいたします。

差出人: Hitomi Ohira

送信日時: 2024年10月4日 17:24

宛先: Itsuo Sakai

件名: RE: [HM26登録懸念点は解消] Re: [ALAP] HM23 Bluetooth SIG認証について

To.
アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

先日ご相談させて頂きました HM23/HM26 Bluetooth 認証試験についての MTG 開催につきまして、

弊社側都合にて大変恐縮なのですが、以下の通りにて MTG 開催日時案を提示させて頂きますので、

酒井様のご都合のよい日時をご連絡頂けます様よろしくお願い致します。

お忙しいところお時間頂くこととなってしまい申し訳ありませんが、

ご検討の程よろしくお願い致します。

【MTG 開催日時案】

10/8( 火 ) 13:00 ～ 15:00 の内 1 時間

10/9( 水 ) 9:00 ～ 11:00 の内 1 時間

10/9( 水 ) 15:00 ～ 16:00

10/10( 木 ) 9:00 ～ 11:00 の内 1 時間

/eom

From:
大平ひとみ Hitomi Ohira

Sent: Tuesday, October 1, 2024 8:58 AM

To: Itsuo Sakai

Subject: RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

毎度早々にご確認頂きありがとうございます。助かります。

HM23 のテストレポートとの不整合発生とのこと、承知致しました。

ご連絡頂いた追加でのサポート削除につきまして早速対応検討を依頼致しました。

結果頂き次第にて再度確認協力のお願いをさせて頂きます。

ご面倒をおかけし大変申し訳ありません。

引き続きご協力頂けます様よろしくお願い致します。

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

送信日時 : 2024 年 9 月 30 日
11:56

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

## 7. 2024-10-30 03:09

**From:** Itsuo Sakai
**To:** Hitomi Ohira

アルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
HM23にて使用しているQCA6595(QDID [ID])につきまして、
先日追加にてAoA/AoD機能削除必要とのことでアドバイス頂いておりました件、
Qualcommより本件対応完了とのことで連絡がされております。

⇒ご連絡ありがとうございます。
酒井様よりご教示頂きました通り、SIGにて以下について削除となっている旨確認はしておりますが、本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

⇒私のWorkspaceで仮Projectを作成して「N [ID]」で問題解消したことを確認できました。

引き続きよろしくお願いいたします。

差出人: Hitomi Ohira

送信日時: 2024年10月30日 11:36

宛先: Itsuo Sakai

件名: RE: [HM26登録懸念点は解消] Re: [ALAP] HM23 Bluetooth SIG認証について

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

送信日時 : 2024 年 9 月 30 日
11:56

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

## 8. 2024-10-31 00:50

**From:** Itsuo Sakai
**To:** Hitomi Ohira

アルプスアルパイン大平様アリオンの酒井です。いつもお世話になっております。
この後、Host subsystem、Profile subsystemが提示され次第にて製品登録を進めるようにしたいと思います。
その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

⇒承知しました。
また、ご指摘頂いておりますRF試験1項目の追加実施につきまして、
先日王君様より概算見積をご提示頂いております。

⇒試験項目の不足に関して再度精査しました。当該不足項目はTCRL2022-1で追加されて発効が2022/12/28でした。従って御社のQDID:[ID](Controller Subsystem / Listing Date

:[ID])および展開いただいたSGS台湾でのRF/RF PHYレポートに含まれていなくても

QDID:186292の登録に関しては認証規定上の問題はありません。

しかし、 新規に「当該RF/RF PHYレポートをエビデンスとした登録を行と不足項目が問題」となります。(以前問題ありと連絡を差し上げた内容です。)

そこで提案ですが、 QDID:186292はController Subsystem登録ですので現在も引き続き有効なため、これとQ社のSubset DN Q320680をIncludeして、QDID:186292からRF/RF PHY階層を選択するとともにDN Q320680から残りの階層を選択すると「認証規定に準拠して」2022/04/20当時に有効であったRF/RF PHYおよびそのエビデンスを引き継ぐことが可能です。この部分組み合わせ登録手順は7/1の新登録サイトで可能となったもので、こうすることで不足項目試験を実施すること無く「認証規定に準拠した」HM23登録を進めることが可能です。

以上ご検討ください。

差出人: Hitomi Ohira

送信日時: 2024年10月30日 13:49

宛先: Itsuo Sakai

件名: RE: [HM26登録懸念点は解消] Re: [ALAP] HM23 Bluetooth SIG認証について

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

差出人 :
Hitomi Ohira

送信日時 :
2024 年 10 月 30 日
11:36

宛先 :
Itsuo Sakai

件名 :
RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

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

送信日時 : 2024 年 9 月 30 日
11:56

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

## 9. 2025-01-21 08:18

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

お問い合わせの内容は、Include先の登録内容や登録製品のサポート機能によって個々に異なる対応が必要で代行登録と同じ手間が発生するため、本来は「代行登録をご依頼ください」という対応となります。しかし、御社からはMH26や新田様案件などをご依頼いただいていますので特別にサポートさせていただきます。以下の手順で登録できることを確認しました。

(1) [ID] と [ID] をInclude後、[Modefy or Add to this set of Design]をクリック(下図)。

(2) 右下の[Save and go to Layer Selection]をクリック。

(3) Layer SelectionページでCore Layersから HCI と UHCI のチェックをはずし、LE Audio Specからすべてのプロトコル・プロファイルのチェックを外して右下の[Save and go to ICS Selection]をクリック

(4) Core階層のICS 10/1 のチェックを外し、右上の[Consistency Check]をクリック。結果が下記

3項目であることを確認後、下部の[Test Coverage Waiver(s)]に [ID](下図)を入力後右下の

[Save and go to Test Plan and Documentation]をクリック。その後のページは記載内容に従って所定の入力などを行い、最後のページまで進む。 .

ーーー

BB

If [LMP] is Supported and [LMP] (2b/1-2) are Not Supported then [BB] (2/4) is Excluded

If [LMP] is Supported and [LMP] (2b/3) is Not Supported then [BB] (2/5) is Excluded

GAP

4b:Prerequisite | If [GATT] (1a/4) is Supported then [GAP] (4b/1-2) are Mandatory

ーーー以上よろしくお願いいたします。

差出人: Hiroaki Fukaura

送信日時: 2025年1月21日 16:08

宛先: Itsuo Sakai

件名: RE: [HM26登録懸念点は解消] Re: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

下記、間が空いてしまいましたが弊社HM23のAndroid14登録についてアドバイスいただけないでしょうか。

弊社大平より、
この後、Host subsystem、Profile subsystemが提示され次第にて製品登録を進めるようにしたいと思います。

と説明いたしましたが、Qualcomm社からHostとProfileを統合した「QDID/DN : [ID]」の登録完了連絡を受けました。

そこで、Core_Host and Profiles Qualification: Q328538とController Subsystem: [ID] (HM23 A13から変更なし)で登録を試みたところ

Consistency Checkで添付画像のエラーが出てしまいました。

これは酒井様のご説明にある“QDID:186292からRF/RF PHY階層を選択する”事により回避可能でしょうか？

試しに「Modify Layers of your Disign manually」を選択して進めてみたところ、エラーにあるBAPはLEで選択されていましたが

BASSは選択されていないようでした。

またそのいずれも変更を加えようとすると新しいVerが適用されるというような警告が表示されました。

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

しかし、 新規に「当該 RF/RF
PHY レポートをエビデンスとした登録を行と不足項目が問題」となります。 ( 以前問題ありと連絡を差し上げた内容です。 )

そこで提案ですが、 QDID:[ID] は Controller
Subsystem 登録ですので現在も引き続き有効なため、これと Q 社の Subset
DN [ID] を Include して、 QDID:[ID] から RF/RF
PHY 階層を選択するとともに DN [ID] から残りの階層を選択すると「認証規定に準拠して」 2022/04/20 当時に有効であった RF/RF PHY およびそのエビデンスを引き継ぐことが可能です。この部分組み合わせ登録手順は 7/1 の新登録サイトで可能となったもので、こうすることで不足項目試験を実施すること無く「認証規定に準拠した」 HM23 登録を進めることが可能です。

以上ご検討ください。

差出人 : Hitomi Ohira

送信日時 : 2024 年 10 月 30 日 13:49

宛先 : Itsuo Sakai

件名 : RE: [HM26 登録懸念点は解消 ]
Re: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早々にご確認頂きありがとうございます。

作成頂いた「Subset DN [ID]」にて問題にないとのこと、承知致しました。

この後、Host subsystem、Profile subsystemが提示され次第にて製品登録を進めるようにしたいと思います。

その際には再度対応ご相談させて頂くことがあるかと思いますが、引き続きご協力頂けますと幸いです。

また、ご指摘頂いておりますRF試験1項目の追加実施につきまして、

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

差出人 : Hitomi Ohira

送信日時 : 2024 年 10 月 30 日 11:36

宛先 : Itsuo Sakai

件名 : RE: [HM26 登録懸念点は解消 ]
Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。度々申し訳ありません。

削除追加にて連絡されているsubset DNは以下の通りとなります。

先のメールにて記載漏れており申し訳ありません。

ご確認の程よろしくお願い致します。
Subset DN [ID] was created from QDID [ID],
[ID] Controller listing.

/eom

From:
大平ひとみ Hitomi Ohira

Sent: Wednesday, October 30, 2024 11:32 AM

To: Itsuo Sakai

Subject: RE: [HM26 登録懸念点は解消 ] Re: [ALAP] HM23 Bluetooth SIG 認証について

To. アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23にて使用しているQCA6595(QDID [ID])につきまして、

先日追加にてAoA/AoD機能削除必要とのことでアドバイス頂いておりました件、

Qualcommより本件対応完了とのことで連絡がされております。

Update the subset DN [ID] for [ID] (delete AoA/AoD capabilities from LL)

酒井様よりご教示頂きました通り、SIGにて以下について削除となっている旨確認はしておりますが、

本内容にて先にご提示したテストレポート流用での製品登録が可能か再度ご確認頂けます様お願い致します。

お忙しいところお手数おかけし申し訳ありません。

ご協力の程よろしくお願い致します。

→[LL] (9/17):NO

→[LL] (9/20):NO

→[LL] (9/21):NO

→[LL] (9/23):NO

→[LL] (9/24):NO

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

差出人 : Hitomi Ohira

送信日時 : 2024 年 9 月 30 日 11:56

宛先 : Itsuo Sakai

件名 : RE: [HM26 登録懸念点は解消 ]
Re: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

HM23にして使用しているQCA6595(QDID [ID])につきましても

Power Class1サポート削除にてSubset DN [ID] が登録されたとのことで連絡がされました。

お忙しいところ大変恐縮ではございますが、こちらにつきましても先日のHM26と同様に懸念点解消となっているかご確認頂くことは可能でしょうか？

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
Subset DN にて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、
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

差出人 : Hitomi Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、HM26にて使用しているQCA66988(QDID [ID])にてDN Q307964が作成され、

Subset DN [ID] も作成頂けた旨連絡頂いております。

Subset DNにて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

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

差出人 : Hitomi Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo Sakai ;
Hiroaki Fukaura

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、HM26とそれぞれにおける対応方法について改めてMTGにて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にてMTG開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていたPower Classにつきましては

HM23/26共にQualcommにてClass1のサポートを削除したsubset DNを対応頂けるとのことで連絡頂いております。

また、A14として10/31を目処に旧QDID取得予定となっているHost subsystem/Profile subsystemのICS Detailsですが、

こちらについてもHM23/26共に A13 Profile Subsystem([ID])、Host Subsystem([ID])参照にて問題ない旨 Qualcommより連絡頂いております。

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

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートはRFPHY/TRM/[ID]Cが不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこでRFPHY/TRM/[ID]Cの試験について教えてください。

・RFPHY/TRM/[ID]Cは(可能かどうかで言えば)差分試験として実施できるものでしょうか？

・仮にRFPHY/TRM/[ID]Cを差分試験として実施してなおかつ登録に反映させる場合には、

ICS変更に相当しRF PHYの試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もしRFPHY/TRM/[ID]Cのみを追加で行える場合、試験費用はどれ程でしょうか？

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

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki Fukaura

件名 : Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ &#8194;&#8194; ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID])の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、2024/12/28以降にそのまま使用可能であるかご確認いただけますか？

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
Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

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

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun Wang ;
Itsuo Sakai

件名 : [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れましたHM23のBluetooth SIG認証について相談させてください。

HM23はAH00ICBというモデルで、D066499で登録済みです。

End Product登録で参照しているQDIDは以下です。

[ID] (Controller Subsystem)　-
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OSのUpdateに伴い217713 (Host Subsystem)と226611 (Profile Subsystem)が変更となり、

弊社では今後取得される新しいA Host-Core ConfigurationとX2Core Layer(Profile Subsystem)を参照して

End Product登録を行う予定です。

AH00ICBは他社で試験をして登録したモデルではありますが、

Host SubsystemとProfile Subsystem変更後の登録においてはHM26と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照したSIG登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration(新規取得)＋X2Core Layer(新規取得)＋Component(従来登録済み)＋前回登録時の他社テストレポート)

なお認証取得完了はHM23/HM26共に2025年4月がMUSTとなっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

差出人 : Hitomi Ohira

送信日時 : 2024 年 9 月 25 日 13:16

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

早速ですが、HM26にて使用しているQCA66988(QDID [ID])にてDN Q307964が作成され、

Subset DN [ID] も作成頂けた旨連絡頂いております。

Subset DNにて「9/11 LE Power Class 1」のサポートが削除されている旨も確認致しましたが、

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

差出人 : Hitomi Ohira

送信日時 : 2024 年 9 月 24 日 16:54

宛先 : Itsuo Sakai ;
Hiroaki Fukaura

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証について

To.　アリオン株式会社酒井様お世話になっております。

アルプスアルパイン大平です。

以下、深浦よりメールにてご相談させて頂いている件、色々とアドバイス頂きありがとうございます。

HM23、HM26とそれぞれにおける対応方法について改めてMTGにて相談させて頂きたいと思っております。

弊社都合にて大変恐縮ではございますが、次週以降にてMTG開催させて頂ければと思っておりますので引き続きご協力頂きたく、

開催日程につきましては関係者調整の上、後日ご連絡とさせて頂きますのでよろしくお願い致します。

尚、以前に懸念事項としてご連絡頂いていたPower Classにつきましては

HM23/26共にQualcommにてClass1のサポートを削除したsubset DNを対応頂けるとのことで連絡頂いております。

また、A14として10/31を目処に旧QDID取得予定となっているHost subsystem/Profile subsystemのICS Detailsですが、

こちらについてもHM23/26共に A13 Profile Subsystem([ID])、Host Subsystem([ID])参照にて問題ない旨 Qualcommより連絡頂いております。

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

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 19 日 14:58

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

いつも早急にご回答いただきありがとうございます。

前回テストレポートはRFPHY/TRM/[ID]Cが不足しているものの、登録にあたり形式上は不整合を起こさないという事は事実として理解いたしました。

そこでRFPHY/TRM/[ID]Cの試験について教えてください。

・RFPHY/TRM/[ID]Cは(可能かどうかで言えば)差分試験として実施できるものでしょうか？

・仮にRFPHY/TRM/[ID]Cを差分試験として実施してなおかつ登録に反映させる場合には、

ICS変更に相当しRF PHYの試験要求、および階層間チェックの対象となるリスクを負う事になりますか？

・もしRFPHY/TRM/[ID]Cのみを追加で行える場合、試験費用はどれ程でしょうか？

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

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 18 日 18:13

宛先 : Hiroaki Fukaura

件名 : Re: [ALAP] HM23 Bluetooth SIG 認証についてアルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。
HM23 ([ID]) の更新の際に参照したい他社テストレポートを添付いたします。
ご提案いただきましたとおり、 2024/12/28 以降にそのまま使用可能であるかご確認いただけますか？ &#8194;&#8194; ⇒ 承知しました。結果は明日昼までに返信いたします。

引き続きよろしくお願いいたします。

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 18 日 16:21

宛先 : Itsuo Sakai

件名 : RE: [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

HM23 ([ID])の更新の際に参照したい他社テストレポートを添付いたします。

ご提案いただきましたとおり、2024/12/28以降にそのまま使用可能であるかご確認いただけますか？

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
Host Subsystem と Profile Subsystem 変更後の登録においては HM26 と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

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

差出人 : Hiroaki Fukaura

送信日時 : 2024 年 9 月 10 日 13:43

宛先 : Jun Wang ;
Itsuo Sakai

件名 : [ALAP] HM23 Bluetooth SIG 認証についてアリオン株式会社王君様、酒井様お世話になっております。アルプスアルパインの深浦です。

先のメールの末尾で触れましたHM23のBluetooth SIG認証について相談させてください。

HM23はAH00ICBというモデルで、D066499で登録済みです。

End Product登録で参照しているQDIDは以下です。

[ID] (Controller Subsystem)　-
[ID] (Component (Tested))

[ID] (Host Subsystem)

[ID] (Profile Subsystem)

Android OSのUpdateに伴い217713 (Host Subsystem)と226611 (Profile Subsystem)が変更となり、

弊社では今後取得される新しいA Host-Core ConfigurationとX2Core Layer(Profile Subsystem)を参照して

End Product登録を行う予定です。

AH00ICBは他社で試験をして登録したモデルではありますが、

Host SubsystemとProfile Subsystem変更後の登録においてはHM26と同様の問題に直面するため更新登録は御社に依頼したいと考えております。

そこで質問なのですが、昨日の打ち合わせで酒井様が上記のような登録ケースの場合には前回テストから年数がたっていなければ前回テストレポートを参照しての登録で問題ないとの見解を示されたと思います。

本件、他社のテストレポートになってしまいますがそれを参照したSIG登録のサポート業務を御社にお願いすることは可能でしょうか？

(A Host-Core Configuration(新規取得)＋X2Core Layer(新規取得)＋Component(従来登録済み)＋前回登録時の他社テストレポート)

なお認証取得完了はHM23/HM26共に2025年4月がMUSTとなっております。

他に必要な情報がございましたらお申し付けください。

以上、よろしくお願いいたします。

---

## 10. 2025-01-22 04:21

**From:** Itsuo Sakai
**To:** Hiroaki Fukaura

アルプスアルパイン深浦様アリオンの酒井です。いつもお世話になっております。

「(4) Core階層のICS 10/1 のチェックを外し、」が記載ミスで正しくは「Core階層のICS 12/1 のチェックを外し」です。申し訳ありませんでした。

対応方法としては、ICS Selectionで Core 10/1をチェックし、Core 12/1のチェックを外して再度

Consistency Checkを行ってください。

以上よろしくお願いいたします。

差出人: Hiroaki Fukaura

送信日時: 2025年1月22日 13:10

宛先: Itsuo Sakai

件名: RE: [HM26登録懸念点は解消] Re: [ALAP] HM23 Bluetooth SIG認証についてアリオン株式会社酒井様お世話になっております。アルプスアルパインの深浦です。

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
