# thread_0185: [内部連絡] Re: お見積りのお願い：Bluetooth認証

- Message count: 1
- Source JSON: `thread_0185.json`

---

## 1. 2025-09-17 10:31

**From:** Itsuo Sakai
**To:** Masaya Iida

飯田さんお疲れさまです。

ざっくりとした内容ですので前提条件付の概略見積となりますが以下のように回答してください。

酒井ーーーー製品：ケーブルテレビ用セットトップボックス仕向け地：国内のみ試験依頼予定：2026年12月ごろ量産開始予定：2027年10月
Wi-Fi/Bluetoothコンボモジュール（買い入れ）
アンテナ：外付け。Wi-Fi2本、Bluetooth１本（買い入れ）
Bluetoothバージョン：5.3
使用チップ：[ID]VTまたはRTL8852BE-VTR （どちらを選ぶか検討中）
Bluetooth SIGサイトで検索したところRTL8852はComponentとなっていました。
Bluetoothモジュール認証に関して (Bluetooth5.0モジュールは全て同じ?) - 半導体事業 - マクニカ以前Component/Controller subsystem/End productのどれかで費用が変わる？
と伺った記憶のため記載しました。

⇒2024年7月1日以降の新制度ではComponentが廃止されてController subsystem

との認証面での扱いが同じになった関係で、同じ階層をサポートしたどちらの登録カテゴリのQDIDを参照しても費用面での差異はなくなりました。
仕様（仮）：
・Classic、BLE両対応・LE Audio対応・HFP対応・HSP非対応（最近あまり使われないと以前伺ったため）
・A2DP対応・AVRCP対応・Device ID対応（何の話か分かりませんがとりあえず）
・LE 2M PHY対応・LE Coded PHY対応・LE Link Layer Privacy対応・拡張アドバタイジング対応・定期アドバタイジング対応・位置スキャン非対応

⇒後述の概算見積は次の一般的な条件が満たされる前提ですのでご注意ください。

(1) Core-Host(Host Subsystem)登録されたHost階層を実装する前提とします。

(2) LE Audioに関してはGeneric Frame Workと呼ばれる下記内容のプロトコルおよびプロファイルを含むX2Core登録あるいはCore Host登録を実装する前提の見積となります。

<概算見積>

・RFフル項目試験 ￥1,200,000

・RF PHY(1M, 2M, Coded)試験 ￥900,000

・PTS試験(A2DP、AVRCP、AVCTP、AVDTP、GAVDP、HFP、DID、IOPT) ￥1,000,000

（もしHost階層が各プロファイルをサポートしていればIOPT試験のみ￥200,000）

・代行登録サポート(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

ーーーー差出人: Takada Taku (高田琢)

送信日時: 2025年9月17日 17:52

宛先: Masaya Iida

件名: お見積りのお願い：Bluetooth認証アリオン飯田様パナソニックコネクト GSOL の高田です。

いつもお世話になっております。

１点お願いがございます。

Bluetooth 認証試験をお願いした場合のお見積りを頂きたくお願いします。

■ご回答希望日：９／１９（金）

製品：ケーブルテレビ用セットトップボックス仕向け地：国内のみ試験依頼予定： 2026 年 12 月ごろ量産開始予定： 2027 年 10 月

Wi-Fi/Bluetooth コンボモジュール（買い入れ）

アンテナ：外付け。 Wi-Fi2 本、 Bluetooth １本（買い入れ）

Bluetooth バージョン： 5.3

使用チップ： [ID] または [ID]

（どちらを選ぶか検討中）

Bluetooth SIG サイトで検索したところ [ID] は Component となっていました。

Bluetooth モジュール認証に関して
(Bluetooth5.0 モジュールは全て同じ?) -
半導体事業 - マクニカ以前 Component/Controller subsystem/End product のどれかで費用が変わる？

と伺った記憶のため記載しました。

仕様（仮）：

・ Classic、 BLE 両対応・ LE Audio 対応・ HFP 対応・ HSP 非対応（最近あまり使われないと以前伺ったため）

・ A2DP 対応・ AVRCP 対応・ Device ID 対応（何の話か分かりませんがとりあえず）

・ LE 2M PHY 対応・ LE Coded PHY 対応・ LE Link Layer Privacy 対応・拡張アドバタイジング対応・定期アドバタイジング対応・位置スキャン非対応不足の情報などございましたらお知らせください。

よろしくお願いいたします。

高田琢 （）

パナソニックコネクト株式会社現場ソリューションカンパニー映像メディアサービス本部ソリューション総括部開発部開発１課

〒 [ID] 大阪府門真市大字門真 1006 番地 16 棟 3 階
