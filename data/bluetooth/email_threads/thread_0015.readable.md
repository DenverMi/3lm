# thread_0015: Re: [Internal]FW: 【依頼】 Bluetooth SIG 認証取得見積 ([ID] GEN2)

- Message count: 3
- Source JSON: `thread_0015.json`

---

## 1. 2025-02-25 10:34

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように返信してください。

酒井ーーーー質問
１．認証取得完了までの見積費用を頂けますでしょうか。
（評価サンプルの提供は８月初旬を予定しております。）

⇒見積は以下の通りです。

・RF-PHY試験(1M+2M+Coded) ￥900,000

・登録代行サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

他に申請者からSIGへ$11,040のドル送金あるいは下記の当社代行送金依頼費用・ドル送金手数料 ￥100,000

・Qualification Fee($11,040)

２．認証試験の実施期間はどのくらいかかるでしょうか。

・RF PHY試験は試験サンプル受領後2-3週間程度・RF PHY試験にPass後レポート作成と代行登録で5営業日程度ーーーー差出人: Masaya Iida

送信日時: 2025年2月25日 18:56

宛先: Itsuo Sakai

件名: [Internal]FW: 【依頼】 Bluetooth SIG 認証取得見積 ([ID] GEN2)

酒井さん、お疲れ様です。

アライドテレシスからのbluetoothの問い合わせですが、

以下内容で見積可能でしょうか。

飯田

---

## 2. 2025-03-24 09:58

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように返信してください。

酒井ーーーー他認証機関からの指摘で以前お伝えしたQDID の組み合わせでは、
下記理由により「認証不可」という回答をもらっています。
お手数ですが、今一度Bluetooth 5.1 にてお伝えしたQDID で認証可能を確認頂けますでしょうか。
理由・Consistency Check でError が発生している・Error の解消にはICベンダーのICS変更作業が必要・シリコンラボ社は古いデバイスはサポートの対象外

⇒ご連絡いただいたQDID: [ID]([ID])、QDID: [ID]（Link Layer, 5.1）、QDID: [ID](Host

Layer, 5.1)の組み合わせでは下記の階層間不整合(IDL)が発生します。

[GAP]

If [GAP] (5/2 and 17a/2) and [CORE] (2a/50) are Supported then [GAP] (17a/5) is Mandatory

[LL]

If [LL] and [GAP] (20/5) are Supported then [LL] (3/4b) is Mandatory

If [LL] and [GAP] (11a/2) are Supported then [LL] (3/10) is Mandatory

If [CORE] (40/3) and [GAP] (11a/2) are Supported then [LL] (3/10) is Mandatory

If [CORE] (40/3) and [GAP] (20/5) are Supported then [LL] (3/4b) is Mandatory

他の認証機関にも相談されているとのことですので詳細内容は申し上げられませんが、PRD2.3登録の

QDIDを参照してIDL(Consistency Check Error)が残っても、今回のご依頼内容は特定条件を満すので新規登録可能です。

ーーーー差出人: 小川政之(Masayuki OGAWA)

送信日時: 2025年3月24日 16:25

宛先: Masaya Iida

件名: Re: 【依頼】 Bluetooth SIG 認証取得見積 ([ID] GEN2)

アリオン株式会社飯田様お世話になっております。

アライドテレシス株式会社小川です認証について一つ確認したいことがあります。

他認証機関からの指摘で以前お伝えしたQDID の組み合わせでは、

下記理由により「認証不可」という回答をもらっています。

お手数ですが、今一度Bluetooth 5.1 にてお伝えしたQDID で認証可能を確認頂けますでしょうか。

理由・Consistency Check でError が発生している・Error の解消にはICベンダーのICS変更作業が必要・シリコンラボ社は古いデバイスはサポートの対象外以上

Allied Telesis K.K.

Software Development Dept.

OGAWA Masayuki

---

## 3. 2025-04-07 10:50

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように返信してください。

酒井ーーーー下記QDID として認証取得しようと思っています。
その場合の費用および試験期間は以前お知らせいただいた内容でよろしいでしょうか。
QDID: [ID] : ([ID] and [ID])
[ID] : Wireless Gecko Link Layer and Host based on Core Specification 5.4

⇒Q301597のLink LayerはAoA/AoD対応ですがQDID: [ID] : ([ID] and [ID])の

RF PHYはAoA/AoD非対応です。このためTCW(Test Case Waiver)申請では許容対象とならない下記IDL(階層間不整合)が発生するためこの参照先では登録不可能です。

[RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/17) is Excluded

[RFPHY] is Supported and [RFPHY] (1/9) is Not Supported then [LL] (9/18) is Excluded

[RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/19) is Excluded

[RFPHY] is Supported and [RFPHY] (1/11) is Not Supported then [LL] (9/20) is Excluded

[RFPHY] is Supported and [RFPHY] (1/10) is Not Supported then [LL] (9/22) is Excluded

[RFPHY] is Supported and [RFPHY] (1/13) is Not Supported then [LL] (9/23) is Excluded

[RFPHY] is Supported and [RFPHY] (1/14) is Not Supported then [LL] (9/24) is Excluded

[RFPHY] is Supported and [RFPHY] (1/12) is Not Supported then [LL] (9/21) is Excluded

[RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/16) is Excluded

[RFPHY] is Supported and [RFPHY] (1/8) is Not Supported then [LL] (9/15) is Excluded

回避策としては「Wireless Gecko Link Layer and Host based on Core Specification 5.4」には下図のように多くのSubset DNが準備されています。

その中のAoA/AoD非対応、Class 1非対応のSubset DN:Q304831とQDID: [ID]([ID]

and [ID])とをIncludeすれば、上記の致命的な階層間不整合は発生せず、TCW(Test

Case Waiver)申請で認証登録が可能です。この場合の見積額は以前と同じです。
なお、RF PHY 試験の一部も前回と同様に台湾で実施するという認識で正しいですか。

⇒はい、RF PHY必須項目は日本ラボで実施し、2MbpsとCodedの試験項目は台湾ラボで実施します。

この際のテストサンサンプルの輸送手続は当方で行います。

ーーーー差出人: 小川政之(Masayuki OGAWA)

送信日時: 2025年4月7日 17:56

宛先: Masaya Iida

件名: Re: 【依頼】 Bluetooth SIG 認証取得見積 ([ID] GEN2)

アリオン株式会社飯田様お世話になっております。

アライドテレシス株式会社小川です改めて確認させてください。

下記QDID として認証取得しようと思っています。

その場合の費用および試験期間は以前お知らせいただいた内容でよろしいでしょうか。

[ID] : Wireless Gecko Link Layer and Host based on Core Specification 5.4

[ID] : [ID] and [ID]

なお、RF PHY 試験の一部も前回と同様に台湾で実施するという認識で正しいですか。

Allied Telesis K.K.

Software Development Dept.

OGAWA Masayuki
