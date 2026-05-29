# thread_0027: Re: 【内部連絡】トイテック様 RF-PHY試験について

- Message count: 5
- Source JSON: `thread_0027.json`

---

## 1. 2024-10-21 07:23

**From:** Itsuo Sakai
**To:** Kousuke Nakayama

中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY試験〜準備〜」だけを行ってInterLabから

Automation ExploreでDUTからのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wireに設定して試験を行うとERROR

⇒QUESTIONAIRSでは2-Wiredにチェックが入っていますのでまずはその設定でAutomation Exploreで

DUTからのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM & LPT)] that the OUT.」

COM8ポートが正しくないようで、InterLab内蔵PCのdevice managerでCOMポートの割当を確認してください。このポートがアサインされていないとAutomation ExploreでのDUTコマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommandに設定するとFail

⇒SkipCommandでの試験実施ではなく、Automation ExploreでDUTのコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようでERROR 100%でfail判定されています。ログではERROR 100%の原因は不明です。

Outputpower試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人: Kousuke Nakayama

送信日時: 2024年10月21日 15:49

宛先: Itsuo Sakai

件名: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐

---

## 2. 2024-10-21 08:48

**From:** Itsuo Sakai
**To:** Kousuke Nakayama

望月さんお疲れさまです。

客先に以下の内容の質問をしてください。

(1) QUSTINAIRS記載の2wire-UART、115200bpsの設定では、試験開始前に行うDUTから正常なコマンド応答の確認段階で正常と判定されません。テストモードがHCI、あるいはボーレートが他の値ではないか、

再度モジュール（あるいはSoC）ベンダにご確認ください。

(2) 【[ID]】BluetoothSIG認証取得サンプル説明資料記載の内容は「準備」と「試験操作方法」

の2段階で説明されていますが、「試験操作方法」は明らかに電波法やFCCなどの法的認証試験での

DUTが自発的に電波を発射する操作方法が書かれています。

今一度Bluetooth SIG認証試験のRF PHYテストの操作説明をモジュール（あるいはSoC）ベンダにご確認ください。

酒井差出人: Kousuke Nakayama

送信日時: 2024年10月21日 17:14

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM
& LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐差出人: Kousuke Nakayama

送信日時: 2024年10月21日 17:14

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM
& LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐

---

## 3. 2024-10-21 08:53

**From:** Itsuo Sakai
**To:** Kousuke Nakayama

中山さんお疲れさまです。

望月さんからは客先へ質問をお願いしていますが、回答を待たずに以下の確認をお願いします。

【[ID]】BluetoothSIG認証取得サンプル説明資料記載の内容は電波法などの試験ツールの操作方法が記載されています。「準備」のを飛ばしての段階でInterLabからAutomation Exploreで

DUTコマンド応答確認を行ってみてください。

酒井差出人: Kousuke Nakayama

送信日時: 2024年10月21日 17:14

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM
& LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐差出人: Kousuke Nakayama

送信日時: 2024年10月21日 17:14

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM
& LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐

---

## 4. 2024-10-21 09:20

**From:** Itsuo Sakai
**To:** Kousuke Nakayama

中山さんお疲れさまです。

まだAutomation ExploreでERRORですか。HCIモードあるいはボーレートの値が違っているかも知れません。この次は望月さんの問い合わせに対する客先からの回答を待って対応してください。

酒井差出人: Kousuke Nakayama

送信日時: 2024年10月21日 18:15

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

「FCC_assist1.0.4.exe」を起動させずにAutomation Exploreのコマンド確認を行ったところ、

結果はERRORとなりましたが、LogのSendの値が変わりました。

また、結果が表示されるまでの読み込み時間が長くなりました。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 5:54 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

望月さんからは客先へ質問をお願いしていますが、回答を待たずに以下の確認をお願いします。

【[ID]】 BluetoothSIG 認証取得サンプル説明資料記載の内容は電波法などの試験ツールの操作方法が記載されています。「準備」のを飛ばしての段階で InterLab から Automation
Explore で

DUT コマンド応答確認を行ってみてください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 17:14

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM & LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 17:14

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM & LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐差出人: Kousuke Nakayama

送信日時: 2024年10月21日 18:15

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

「FCC_assist1.0.4.exe」を起動させずにAutomation Exploreのコマンド確認を行ったところ、

結果はERRORとなりましたが、LogのSendの値が変わりました。

また、結果が表示されるまでの読み込み時間が長くなりました。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 5:54 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

望月さんからは客先へ質問をお願いしていますが、回答を待たずに以下の確認をお願いします。

【[ID]】 BluetoothSIG 認証取得サンプル説明資料記載の内容は電波法などの試験ツールの操作方法が記載されています。「準備」のを飛ばしての段階で InterLab から Automation
Explore で

DUT コマンド応答確認を行ってみてください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 17:14

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM & LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 17:14

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM & LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐

---

## 5. 2024-10-22 09:18

**From:** Itsuo Sakai
**To:** Kousuke Nakayama
**Attachments:** RF_ICS_TestPlan_IXIT.xlsx

望月さんお疲れさまです。

トイテック様のRFのTest Planを失念しておりました。添付しますのでサーバーに保管するとともに中山さんに試験依頼願います。

酒井差出人: Itsuo Sakai

送信日時: 2024年10月21日 17:48

宛先: Kousuke Nakayama

件名: Re: 【内部連絡】トイテック様 RF-PHY試験について望月さんお疲れさまです。

客先に以下の内容の質問をしてください。

(1) QUSTINAIRS記載の2wire-UART、115200bpsの設定では、試験開始前に行うDUTから正常なコマンド応答の確認段階で正常と判定されません。テストモードがHCI、あるいはボーレートが他の値ではないか、

再度モジュール（あるいはSoC）ベンダにご確認ください。

(2) 【[ID]】BluetoothSIG認証取得サンプル説明資料記載の内容は「準備」と「試験操作方法」

の2段階で説明されていますが、「試験操作方法」は明らかに電波法やFCCなどの法的認証試験での

DUTが自発的に電波を発射する操作方法が書かれています。

今一度Bluetooth SIG認証試験のRF PHYテストの操作説明をモジュール（あるいはSoC）ベンダにご確認ください。

酒井差出人: Kousuke Nakayama

送信日時: 2024年10月21日 17:14

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM & LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐差出人: Kousuke Nakayama

送信日時: 2024年10月21日 17:14

宛先: Itsuo Sakai

件名: RE: 【内部連絡】トイテック様 RF-PHY試験について酒井さんお疲れ様です。中山です。

COMポートが合っていることを確認しAutomation Exploreのコマンドを確認しましたが、すべてERROR(赤表示)となってしまいます。

ポートを変更して確認しましたがそちらでもERRORとなっています。

また、リファレンスDUTでは正常(緑表示)となることを確認済みです。

よろしくお願い致します中山光祐

From: Itsuo Sakai

Sent: Monday, October 21, 2024 4:23 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】トイテック様 [ID] 試験について中山さんお疲れさまです。

最初に説明資料の「2-2-2. BLE RF PHY 試験〜試験操作方法〜」は電波法の試験の際に使うモードで、認証テスターでの試験では「2-2-1. BLE RF PHY 試験〜準備〜」だけを行って InterLab から

Automation Explore で DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

この機能を使ったことがなければ田中さんに使い方を尋ねてください。
2 wire に設定して試験を行うと ERROR

⇒ [ID] では 2-Wired にチェックが入っていますのでまずはその設定で Automation
Explore で

DUT からのコマンドが正常（緑の表示）の確認後に実試験を行ってください。

ログを見ると以下の警告がでていて、試験以前の接続段階で失敗しています。

「Unable to open COM8. Check in the device manager [Ports (COM & LPT)] that the OUT.」

COM8 ポートが正しくないようで、 InterLab 内蔵 PC の device
manager で COM ポートの割当を確認してください。このポートがアサインされていないと Automation Explore での DUT コマンド応答チェックで正常（緑の表示）とはなりません。
SkipCommand に設定すると Fail

⇒ SkipCommand での試験実施ではなく、 Automation
Explore で DUT のコマンド応答が正常出ることを確認して試験実施してください。。

試験は実施されてようで ERROR 100% で fail 判定されています。ログでは ERROR
100% の原因は不明です。

Outputpower 試験で極端に出力が低い結果がでればアンテナ信号引出に問題がありと推定されます。

酒井差出人 : Kousuke Nakayama

送信日時 : 2024 年 10 月 21 日 15:49

宛先 : Itsuo Sakai

件名 : 【内部連絡】トイテック様 [ID] 試験について酒井さんお疲れ様です。中山光祐です。

トイテック様のRF-PHY試験にて、Failとなってしまいます。

お手数ですがFailの原因についてご教示いただけますでしょうか。

以下疑問点になります。

・テストモードへの移行についてお客様資料に従い、テストモードの設定をしましたが、SystemSoftwareではエラーとなっています。

資料：[【[ID]】BluetoothSIG認証取得サンプル説明資料.xlsx]　[ID] RF PHY試験 〜準備〜

・Logについて

2 wireに設定して試験を行うとERRORとなってしまい、SkipCommandに設定するとFailとなってしまいます。

Logを添付いたしますのでご確認いただけますでしょうか。

お手数おかけしますがよろしくお願い致します中山光祐
