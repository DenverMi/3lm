# thread_0169: Re: [Internal]FW: [ご相談][アリオン] BT SIG認証試験について

- Message count: 3
- Source JSON: `thread_0169.json`

---

## 1. 2025-12-04 01:50

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。
正式な見積り提示をしたいのですが、可能でしょうか。

⇒アリオン台湾に「Open Source (fluoride)スタックのPTS試験

(L2CAP, GAP, SDP, GATT, ATT, SM, [ID], SPP)のパスまでコース試験費用見積を依頼してください。
なお、試験部分の見積条件としては
3か月のパッケージとしようと思います。（試験合格とならない場合も、試験開始から3か月で終了）

⇒賛成です。

酒井差出人: Masaya Iida

送信日時: 2025年12月4日 10:24

宛先: Itsuo Sakai

件名: [Internal]FW: [ご相談][アリオン] BT SIG認証試験について酒井さん、お疲れ様です。

以下NECPF様のメールですが、台湾ラボでのHost STACKの試験を含めて進めるとの結論をだされました。

正式な見積り提示をしたいのですが、

可能でしょうか。

なお、試験部分の見積条件としては

3か月のパッケージとしようと思います。（試験合格とならない場合も、試験開始から3か月で終了）

飯田

From: [ID] [ID]( 橋本秀昌 )

Sent: Wednesday, December 3, 2025 5:32 PM

To: Masaya Iida

Subject: RE: [ ご相談 ][ アリオン ] BT
SIG 認証試験について

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様二転三転して申し訳ございません。

NXP様へ問い合わさせて頂いた結果現在実装しているBT HOST STACKは、

Google QDID取得BT HOST STACKと同一でない回答を得られました。

ということで、

台湾で新規BT HOST STACK認証が必要となりました。

誠にお手数ですが同上におけるお見積りを正式にご提示を頂きますようお願いいたします。

因みに御社国内では

BT HOST STACK認証試験はできないものなのでしょうか？

【弊社結論】

・Google BT HOST STACK

→QDID取得済・弊社i.mx8MP BSP BT HOST STACK

→ Google BT HOST STACKを一部改修して実装

→ 上記によりQDID取得とは見なされないものを実装・以上より、

Google HOST STACK QDID + IW416 QDID

＝＞弊社製品QDID登録の流れは不可と判断・台湾での新規BT HOST STACK　QDID取得作業を予定

From: [ID] [ID](橋本秀昌)

Sent: Wednesday, December 3, 2025 1:30 PM

To: 'Masaya Iida'

Subject: RE: [ご相談][アリオン] BT SIG認証試験について

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様ご連絡ありがとうございます。

先程お電話で会話させて頂いた内容ご連絡いたします。

【お見積りに関して】

合計：50万→150万円であること認識いたしました。

【製品認証と試験環境方針】

・製品登録作業に関して

Google HOST STACK QDID + IW416 QDID

→弊社製品QDID登録となる・Google HOST STACK QDID：169365はあくまでの製品登録の際の紐付け処理の位置付けとなる。

その結果下記具体的作業と想定される。

その１、プロトコル試験は未実施でよいその２、プロファイル試験のみとなるその３、弊社、元々実装のBTスタックを改修する必要なし上記認識間違いや他具体的追加作業がある場合はご指摘の程お願い致します。

From: Masaya Iida

Sent: Wednesday, December 3, 2025 12:36 PM

To: [ID] [ID](橋本秀昌)

Subject: RE: [ご相談][アリオン] BT SIG認証試験について

NECPF　橋本様いつもお世話になっております。

アリオンの飯田です。

以下にご案内いたします。
下記QDID 169365が
HOST STACKとして流用可能と推定しています。
現在、NXP様へは問い合わせ中です。

問題は、コントローラがNXP製NW416で
HOST STACK GOOGLE製とベンダーが違うのですが製品認証としてはこのような組み合わせは可能でしょうか？

■Google HOST STACK
Bluetooth Certification - Google LLC
Google Fluoride 1.4 Bluetooth Core Host solution, Fluoride 1.4
Bluetooth Core Host solution for Android and Bluetooth 5.2 core specification.

■ AOSP Bluetoothスタック（Fluoride）
ソースコード場所
android.googlesource.com/platform/packages/modules/Bluetooth
→ Fluoride BluetoothスタックはAOSPに標準で含まれています。

⇒認証登録にHost StackとController部のベンダー違いは全く問題ありません。

問題なく新規登録可能です。

QDID:169365を参照したとして、ICSレベルでサポートプロファイルの情報がないとHOGPに紐付けられるBAS, DIS, HIDS, ScPPの要否が決まりませんが、

HOGP両ロールとすると以下が当社見積です。(以前と同じです。)

・プロファイル試験(HID, PAN, BNEP, HOGP, BAS, DIS, HIDS, ScPP, IOPT) ￥1,000,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

・ドル送金代行手数料 ￥100,000

・Qualification Fee($11,040または$12,000)

合計: 500,000円とQualification Fee

以上、よろしくお願いいたします。

---

## 2. 2025-12-04 05:57

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。
LCCAPとGAPが2つあるのが良くわからないのですが、
黄色で網掛けしたやつを足せば良さそうですかね。

⇒ LCCAPとGAPは階層としては一つで試験内容としてBR/EDRとBLEに分けているものと思います。今回はデュアルモードですので足してください。

酒井差出人: Masaya Iida

送信日時: 2025年12月4日 12:46

宛先: Itsuo Sakai

件名: RE: [Internal]FW: [ご相談][アリオン] BT SIG認証試験について酒井さん、お疲れ様です。

台湾ラボの標準費用のリストを見ると以下がありました。

単位はUSDで、パスまでパッケージです。

LCCAPとGAPが2つあるのが良くわからないのですが、

黄色で網掛けしたやつを足せば良さそうですかね。

台湾ラボと確認しますが、確認を簡単にするために確認をさせてくださいませ。

BQTF_Protocols Testing

Protocols' Conformance Test

a. BB/LM/HCI (TUV)

43670

BQTF_Protocols Testing

Protocols' Conformance Test

b. LL/HCI 4.0 (Allion)

25300

BQTF_Protocols Testing

Protocols' Conformance Test

c. L2CAP (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

d. GAP (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

e. SM (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

f. ATT (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

g. GATT (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

h. [ID] (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

i. L2CAP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

j. SDP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

k. GAP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

l. SPP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

m. [ID] (classic core host protocols) (Allion)

5500

飯田

From: Itsuo Sakai

Sent: Thursday, December 4, 2025 10:51 AM

To: Masaya Iida

Subject: Re: [Internal]FW: [ ご相談 ][ アリオン ]
BT SIG 認証試験について飯田さんお疲れさまです。
正式な見積り提示をしたいのですが、可能でしょうか。

⇒ アリオン台湾に「Open
Source (fluoride) スタックの PTS 試験

(L2CAP, GAP, SDP, GATT, ATT, SM, [ID], SPP) のパスまでコース試験費用見積を依頼してください。
なお、試験部分の見積条件としては
3 か月のパッケージとしようと思います。（試験合格とならない場合も、試験開始から 3 か月で終了）

⇒ 賛成です。

酒井差出人 : Masaya Iida

送信日時 : 2025 年 12 月 4 日 10:24

宛先 : Itsuo Sakai

件名 : [Internal]FW: [ ご相談 ][ アリオン ]
BT SIG 認証試験について酒井さん、お疲れ様です。

以下NECPF様のメールですが、台湾ラボでのHost STACKの試験を含めて進めるとの結論をだされました。

正式な見積り提示をしたいのですが、

可能でしょうか。

なお、試験部分の見積条件としては

3か月のパッケージとしようと思います。（試験合格とならない場合も、試験開始から3か月で終了）

飯田

From: [ID] [ID]( 橋本秀昌 )

Sent: Wednesday, December 3, 2025 5:32 PM

To: Masaya Iida

Subject: RE: [ ご相談 ][ アリオン ] BT
SIG 認証試験について

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様二転三転して申し訳ございません。

NXP様へ問い合わさせて頂いた結果現在実装しているBT HOST STACKは、

Google QDID取得BT HOST STACKと同一でない回答を得られました。

ということで、

台湾で新規BT HOST STACK認証が必要となりました。

誠にお手数ですが同上におけるお見積りを正式にご提示を頂きますようお願いいたします。

因みに御社国内では

BT HOST STACK認証試験はできないものなのでしょうか？

【弊社結論】

・Google BT HOST STACK

→QDID取得済・弊社i.mx8MP BSP BT HOST STACK

→ Google BT HOST STACKを一部改修して実装

→ 上記によりQDID取得とは見なされないものを実装・以上より、

Google HOST STACK QDID + IW416 QDID

＝＞弊社製品QDID登録の流れは不可と判断・台湾での新規BT HOST STACK　QDID取得作業を予定

From: [ID] [ID](橋本秀昌)

Sent: Wednesday, December 3, 2025 1:30 PM

To: 'Masaya Iida'

Subject: RE: [ご相談][アリオン] BT SIG認証試験について

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様ご連絡ありがとうございます。

先程お電話で会話させて頂いた内容ご連絡いたします。

【お見積りに関して】

合計：50万→150万円であること認識いたしました。

【製品認証と試験環境方針】

・製品登録作業に関して

Google HOST STACK QDID + IW416 QDID

→弊社製品QDID登録となる・Google HOST STACK QDID：169365はあくまでの製品登録の際の紐付け処理の位置付けとなる。

その結果下記具体的作業と想定される。

その１、プロトコル試験は未実施でよいその２、プロファイル試験のみとなるその３、弊社、元々実装のBTスタックを改修する必要なし上記認識間違いや他具体的追加作業がある場合はご指摘の程お願い致します。

From: Masaya Iida

Sent: Wednesday, December 3, 2025 12:36 PM

To: [ID] [ID](橋本秀昌)

Subject: RE: [ご相談][アリオン] BT SIG認証試験について

NECPF　橋本様いつもお世話になっております。

アリオンの飯田です。

以下にご案内いたします。
下記QDID 169365が
HOST STACKとして流用可能と推定しています。
現在、NXP様へは問い合わせ中です。

問題は、コントローラがNXP製NW416で
HOST STACK GOOGLE製とベンダーが違うのですが製品認証としてはこのような組み合わせは可能でしょうか？

■Google HOST STACK
Bluetooth Certification - Google LLC
Google Fluoride 1.4 Bluetooth Core Host solution, Fluoride 1.4
Bluetooth Core Host solution for Android and Bluetooth 5.2 core specification.

■ AOSP Bluetoothスタック（Fluoride）
ソースコード場所
android.googlesource.com/platform/packages/modules/Bluetooth
→ Fluoride BluetoothスタックはAOSPに標準で含まれています。

⇒認証登録にHost StackとController部のベンダー違いは全く問題ありません。

問題なく新規登録可能です。

QDID:169365を参照したとして、ICSレベルでサポートプロファイルの情報がないとHOGPに紐付けられるBAS, DIS, HIDS, ScPPの要否が決まりませんが、

HOGP両ロールとすると以下が当社見積です。(以前と同じです。)

・プロファイル試験(HID, PAN, BNEP, HOGP, BAS, DIS, HIDS, ScPP, IOPT) ￥1,000,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

・ドル送金代行手数料 ￥100,000

・Qualification Fee($11,040または$12,000)

合計: 500,000円とQualification Fee

以上、よろしくお願いいたします。

---

## 3. 2025-12-04 06:22

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。
台湾ラボでのプロトコルテストに追加で、
以下が発生するという認識でよいでしょうか。
・プロファイル試験(HID, PAN, BNEP, HOGP, BAS, DIS, HIDS, ScPP, IOPT) ￥1,000,000
・代行登録サポート(Multi-Design参照) ￥250,000
・コンプライアンスフォルダ作成費 ￥150,000
・ドル送金代行手数料 ￥100,000

⇒はい、上記はプロトコル試験とは別に日本ラボで発生する費用です。

酒井差出人: Masaya Iida

送信日時: 2025年12月4日 15:07

宛先: Itsuo Sakai

件名: RE: [Internal]FW: [ご相談][アリオン] BT SIG認証試験について酒井さん、

台湾ラボでのプロトコルテストに追加で、

以下が発生するという認識でよいでしょうか。

・プロファイル試験(HID, PAN, BNEP, HOGP, BAS, DIS, HIDS, ScPP, IOPT) ￥1,000,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

・ドル送金代行手数料 ￥100,000

・Qualification Fee($11,040または$12,000)

合計: 1, 500,000円とQualification Fee

飯田

From: Itsuo Sakai

Sent: Thursday, December 4, 2025 2:57 PM

To: Masaya Iida

Subject: Re: [Internal]FW: [ ご相談 ][ アリオン ]
BT SIG 認証試験について飯田さんお疲れさまです。
LCCAP と GAP が 2 つあるのが良くわからないのですが、
黄色で網掛けしたやつを足せば良さそうですかね。

⇒ LCCAP と GAP は階層としては一つで試験内容として BR/EDR と BLE に分けているものと思います。今回はデュアルモードですので足してください。

酒井差出人 : Masaya Iida

送信日時 : 2025 年 12 月 4 日 12:46

宛先 : Itsuo Sakai

件名 : RE: [Internal]FW: [ ご相談 ][ アリオン ]
BT SIG 認証試験について酒井さん、お疲れ様です。

台湾ラボの標準費用のリストを見ると以下がありました。

単位はUSDで、パスまでパッケージです。

LCCAPとGAPが2つあるのが良くわからないのですが、

黄色で網掛けしたやつを足せば良さそうですかね。

台湾ラボと確認しますが、確認を簡単にするために確認をさせてくださいませ。

BQTF_Protocols Testing

Protocols' Conformance Test

a. BB/LM/HCI (TUV)

43670

BQTF_Protocols Testing

Protocols' Conformance Test

b. LL/HCI 4.0 (Allion)

25300

BQTF_Protocols Testing

Protocols' Conformance Test

c. L2CAP (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

d. GAP (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

e. SM (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

f. ATT (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

g. GATT (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

h. [ID] (LE core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

i. L2CAP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

j. SDP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

k. GAP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

l. SPP (classic core host protocols) (Allion)

5500

BQTF_Protocols Testing

Protocols' Conformance Test

m. [ID] (classic core host protocols) (Allion)

5500

飯田

From: Itsuo Sakai

Sent: Thursday, December 4, 2025 10:51 AM

To: Masaya Iida

Subject: Re: [Internal]FW: [ ご相談 ][ アリオン ]
BT SIG 認証試験について飯田さんお疲れさまです。
正式な見積り提示をしたいのですが、可能でしょうか。

⇒ アリオン台湾に「Open
Source (fluoride) スタックの PTS 試験

(L2CAP, GAP, SDP, GATT, ATT, SM, [ID], SPP) のパスまでコース試験費用見積を依頼してください。
なお、試験部分の見積条件としては
3 か月のパッケージとしようと思います。（試験合格とならない場合も、試験開始から 3 か月で終了）

⇒ 賛成です。

酒井差出人 : Masaya Iida

送信日時 : 2025 年 12 月 4 日 10:24

宛先 : Itsuo Sakai

件名 : [Internal]FW: [ ご相談 ][ アリオン ]
BT SIG 認証試験について酒井さん、お疲れ様です。

以下NECPF様のメールですが、台湾ラボでのHost STACKの試験を含めて進めるとの結論をだされました。

正式な見積り提示をしたいのですが、

可能でしょうか。

なお、試験部分の見積条件としては

3か月のパッケージとしようと思います。（試験合格とならない場合も、試験開始から3か月で終了）

飯田

From: [ID] [ID]( 橋本秀昌 )

Sent: Wednesday, December 3, 2025 5:32 PM

To: Masaya Iida

Subject: RE: [ ご相談 ][ アリオン ] BT
SIG 認証試験について

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様二転三転して申し訳ございません。

NXP様へ問い合わさせて頂いた結果現在実装しているBT HOST STACKは、

Google QDID取得BT HOST STACKと同一でない回答を得られました。

ということで、

台湾で新規BT HOST STACK認証が必要となりました。

誠にお手数ですが同上におけるお見積りを正式にご提示を頂きますようお願いいたします。

因みに御社国内では

BT HOST STACK認証試験はできないものなのでしょうか？

【弊社結論】

・Google BT HOST STACK

→QDID取得済・弊社i.mx8MP BSP BT HOST STACK

→ Google BT HOST STACKを一部改修して実装

→ 上記によりQDID取得とは見なされないものを実装・以上より、

Google HOST STACK QDID + IW416 QDID

＝＞弊社製品QDID登録の流れは不可と判断・台湾での新規BT HOST STACK　QDID取得作業を予定

From: [ID] [ID](橋本秀昌)

Sent: Wednesday, December 3, 2025 1:30 PM

To: 'Masaya Iida'

Subject: RE: [ご相談][アリオン] BT SIG認証試験について

【秘密】

FROM：NECPF橋本です

TO：アリオン飯田様ご連絡ありがとうございます。

先程お電話で会話させて頂いた内容ご連絡いたします。

【お見積りに関して】

合計：50万→150万円であること認識いたしました。

【製品認証と試験環境方針】

・製品登録作業に関して

Google HOST STACK QDID + IW416 QDID

→弊社製品QDID登録となる・Google HOST STACK QDID：169365はあくまでの製品登録の際の紐付け処理の位置付けとなる。

その結果下記具体的作業と想定される。

その１、プロトコル試験は未実施でよいその２、プロファイル試験のみとなるその３、弊社、元々実装のBTスタックを改修する必要なし上記認識間違いや他具体的追加作業がある場合はご指摘の程お願い致します。

From: Masaya Iida

Sent: Wednesday, December 3, 2025 12:36 PM

To: [ID] [ID](橋本秀昌)

Subject: RE: [ご相談][アリオン] BT SIG認証試験について

NECPF　橋本様いつもお世話になっております。

アリオンの飯田です。

以下にご案内いたします。
下記QDID 169365が
HOST STACKとして流用可能と推定しています。
現在、NXP様へは問い合わせ中です。

問題は、コントローラがNXP製NW416で
HOST STACK GOOGLE製とベンダーが違うのですが製品認証としてはこのような組み合わせは可能でしょうか？

■Google HOST STACK
Bluetooth Certification - Google LLC
Google Fluoride 1.4 Bluetooth Core Host solution, Fluoride 1.4
Bluetooth Core Host solution for Android and Bluetooth 5.2 core specification.

■ AOSP Bluetoothスタック（Fluoride）
ソースコード場所
android.googlesource.com/platform/packages/modules/Bluetooth
→ Fluoride BluetoothスタックはAOSPに標準で含まれています。

⇒認証登録にHost StackとController部のベンダー違いは全く問題ありません。

問題なく新規登録可能です。

QDID:169365を参照したとして、ICSレベルでサポートプロファイルの情報がないとHOGPに紐付けられるBAS, DIS, HIDS, ScPPの要否が決まりませんが、

HOGP両ロールとすると以下が当社見積です。(以前と同じです。)

・プロファイル試験(HID, PAN, BNEP, HOGP, BAS, DIS, HIDS, ScPP, IOPT) ￥1,000,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

・ドル送金代行手数料 ￥100,000

・Qualification Fee($11,040または$12,000)

合計: 500,000円とQualification Fee

以上、よろしくお願いいたします。
