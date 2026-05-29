# thread_0284: Re: [Internal]FW: [Allion]Bluetooth SIG認証 （キーシステム様)

- Message count: 1
- Source JSON: `thread_0284.json`

---

## 1. 2026-04-01 04:43

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

以下のように返信してください。

酒井ーーーー

【製品1（スマート縄跳び）】

1. Bluetoothの仕様（BLE / Classic / Dual）

→BLE

2. コア仕様バージョン (Core Spec)

→4.2

3. 使用コンポーネントのQDID

→すでに認証済みのチップ（QDID取得済み）は使っていない。

4. 実装プロファイル

→・DIS ・BAS ・CustomGATT

5. RF物理層 (PHY)

→LE 1M

6. 送信出力 (Power Class)

→Class2

7. アンテナ

→PCB antenna

【アリオン見積】

Link Layer, L2CAP, GAP, GATT, ATT,SMは認証登録済SoCおよびHost Stackを実装しない製品はこれらの階層の試験を実施してレポートを認証登録時にアップロードする必要があります。しかし最下層のRF PHYおよび上位のプロフィル階層は製品の試験が可能ですが、前述の中間階層は製品実装状態では試験ができません。

Host Stackは認証登録済のSoC＋LL StackおよびHost Syackの実装をご検討ください。

【製品2（スマートバンド）】

1. Bluetoothの仕様（BLE / Classic / Dual）

→BLE

2. コア仕様バージョン (Core Spec)

→6

3. 使用コンポーネントのQDID

→Nordic nRF54L15。

4. 実装プロファイル

→・DIS ・BAS ・CustomGATT

5. RF物理層 (PHY)

→1M

6. 送信出力 (Power Class)

→Class3

7. アンテナ

→外付けモノポールアンテナ

【アリオン見積】　実装するnRF54L15およびHost Stackは認証登録済を前提とした見積です。

・RF PHY試験（1M） ￥400,000

・プロファイル試験(DIS, BAS) ￥200,000

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

(他に申請者からSIGへ$12,000のドル送金)

ーーーー差出人: Masaya Iida

送信日時: 2026年4月1日 13:13

宛先: Itsuo Sakai

件名: [Internal]FW: [Allion]Bluetooth SIG認証 （キーシステム様)

酒井さん、お疲れ様です。

以下メール内容でBluetooth SIG認証の見積りは可能でしょうか。

2製品あります。

飯田
