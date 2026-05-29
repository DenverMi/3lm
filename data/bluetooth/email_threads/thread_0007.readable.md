# thread_0007: [内部連絡] Re: GAP-LL間で階層間不整合の件

- Message count: 1
- Source JSON: `thread_0007.json`

---

## 1. 2025-11-19 06:40

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように回答してください。

酒井ーーーー開発会社からBLEモジュールを扱う商社に問い合わせしましたところ、
下記の回答でした。
＜商社の回答＞
下記URLにnRF52805として使用できるDesign Numberが記載されており、
もともとChannel Soundingに対応していないnRF52805として使用できる
NCS v3.1.0のDesign Numberは「CSなし：[ID]」のみとなります。
したがって下記の組み合わせで新規登録できるという認識で良いでしょうか？
[ID](Core-Host)　←CS非対応のQDID
[ID](Core-Controller)　※こちらは変更無し

⇒上記組み合わせをIncludeした登録では階層間エラーが発生します。

しかし、最後の手段としては上記を組み合わせ指定後にICSを修正しない

[Combine Unmodified Designs]という選択で登録を進めると、たまたまですが今回の組み合わせでは追加試験要求なしでの登録が可能です。

したがって御社登録のICSには階層間エラーがそのまま踏襲されるものの新規登録が可能です。

認証の有効性は参照先に起因した階層間不整合を踏襲した登録と、階層間不整合のない参照先を組み合わせた登録とは同等ですのでご安心ください。

ーーーー差出人: シブタニ森朋之

送信日時: 2025年11月19日 15:10

宛先: Masaya Iida

件名: RE: GAP-LL間で階層間不整合の件

To：アリオン株式会社飯田様いつもお世話になります。

シブタニ技術開発部の森です。

開発会社からBLEモジュールを扱う商社に問い合わせしましたところ、下記の回答でした。

＜商社の回答＞

下記URLにnRF52805として使用できるDesign Numberが記載されており、もともとChannel Soundingに対応していないnRF52805として使用できるNCS v3.1.0のDesign Numberは「CSなし：[ID]」のみとなります。

したがって下記の組み合わせで新規登録できるという認識で良いでしょうか？

[ID](Core-Host)　←CS非対応のQDID

[ID](Core-Controller)　※こちらは変更無し以上株式会社シブタニ森朋之

From:
シブタニ森朋之

Sent: Wednesday, November 12, 2025 5:41 AM

To: 'Masaya Iida'

Subject: RE: [ID] 間で階層間不整合の件

To：アリオン株式会社飯田様いつもお世話になります。

シブタニ技術開発部の森です。

ご説明いただきありがとうございます。

開発会社に展開いたします。

以上株式会社シブタニ森朋之

From: Masaya Iida

Sent: Tuesday, November 11, 2025 5:51 PM

To: シブタニ森朋之

Subject: RE: [ID] 間で階層間不整合の件シブタニ森様いつもお世話になっております。

アリオンの飯田です。

以下回答いたします。

＜質問＞

製品はCS非対応のため（2）[ID]→Q358851で対応したいと考えております。

NordicのHPを参考に選んでいます。（Bluetooth DNs）

nrf connect SDKを3.1.0を使用すれば

[ID]→[ID]

ということはできますか？

Q358851ですとSDKのバージョン3.0.0と古いので、

できれば新しいSDKを採用したいです。

回答）

Q370938はQ370860から一部機能を削除して作成されたSubset DNですが、

CSに関するGAP 33a/1, 33a/2がどちらもYESです。このためQ370860でも

Q370938と同様、[ID](Core-Controller)とは階層間不整合が発生しますので新規登録で参照できません。

SIGの登録サイトの詳細検索でCompany: Nordic Semiconductor ASAおよび検索キーにConnect SDK Hostで検索してもQ370860しか表示されません。

したがって認証登録されたConnect SDK Host 3.1.XとそのSubsetでは、

CS非対応のものは無いように見受けられます。

Nordicへ「Connect SDK Host 3.1.XでCS非サポートの登録」の有無を確認いただけますでしょうか。

以上、よろしくお願いいたします。
