# thread_0251: Re: [登録内容に関するご相談] Re: HSP再テストについて

- Message count: 1
- Source JSON: `thread_0251.json`

---

## 1. 2024-09-02 01:00

**From:** Itsuo Sakai
**To:** "" , Masaya Iida , Toshitaka Mochizuki , AJ Bluetooth Group

JVCケンウッド菅沼様アリオンの酒井です。いつもお世話になっております。
「BR/EDR/LE」「Class 1」で登録した場合、
弊社ホームページの製品紹介または取扱説明書には「BR/EDR」「Class ２」の文言が入るかもしれませんが、その場合でも何らかのルール違反が生じなければ問題ありません。
BT SIGのルール等、ご教示頂けると助かります。

⇒(1) LEはAdvertizingパケットを出すUIがなければスマホなどのScanner機器からBluetooth LE機器として検出できません。従ってBR/EDR/LE機能で登録しても、LE機器としてAdvertizingパケットを出すUIを実装しなければその機器は使用者にLE機能は使うことはできないため取り扱い説明書に

「BR/EDR」と記載可能です。この件に言及したSIGのドキュメント等は見当たりません。

(2) 出力に関して、SIGの仕様は下記の通り 0dBmから4dBm が重複しています。

Class 1: 0dBm(1mW) < Output <20dBm(100mW)

Class 2: -6dBm(0.25mW) < Output <4dBm(2.5mW)

また、一般的に無線規格認証では最大出力での測定値で公示されますがそれ以下のレベルでの実使用は合法です。

従って今回のケースでは出力を 0dBmから4dBm で管理するとともに、取扱説明書に「Class 2相当」と

「相当」を入れることで問題回避できます。

以上ご検討ください。

差出人:

送信日時: 2024年9月2日 9:31

宛先: Itsuo Sakai ; Masaya Iida ; Toshitaka Mochizuki ; AJ Bluetooth Group

件名: Re: [登録内容に関するご相談] Re: HSP再テストについて
