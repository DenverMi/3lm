# thread_0074: Re: [Report Review] ALPS [ID] CO. LTD.; [ID]

- Message count: 5
- Source JSON: `thread_0074.json`

---

## 1. 2025-10-14 12:46

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu

Dear Ushiroebisu-san,

Thank you for testing and making a RF report for ALAP UXC10.

There are two items that don't refer to the Test Plan correctly.

(1) Company Address

(2) Power Class: Class 1 → Class 2　(Test setup is Class 2 as far as the log)

(3) Test Voltage:　14V→13.2V (Test setup is 13.2V as far as the log)

After correcting (1) to (3), pleas ask Yu-san to approve.

Thanks

Best Regard,

Itsuo sakai

差出人: Kenichi Ushiroebisu

送信日時: 2025年10月14日 19:01

宛先: Itsuo Sakai

件名: [Report Review] ALPS [ID] CO. LTD.; [ID]

Dear Sakai-san,

Could you review the following test report?

Project ID: [ID]

Vender Name: ALPS [ID] CO. LTD

Model Name: UXC10 (RF)

Schedule:

Test Result: PASS

Comment: 在宅勤務対応としてTeams上に「Bluetoothデータ共有」というデータ共有用のチームを作成し、そちらにもファイルを保存しました。

​ ​ RF ​ ​

Regards,

Kenichi Ushiroebisu

---

## 2. 2025-10-15 01:26

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , AJ Bluetooth Group
**Attachments:** ALPS_ALPINE_UXC10_RF_PASS_Report_Rev1.[ID]doc

望月さんお疲れさまです。

修正版ドラフトレポートを添付します。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年10月15日 10:04

宛先: AJ Bluetooth Group

件名: 【内部連絡】FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

喩さん望月です本日後夷さんお休みですが、こちら修正・田中さんレビュー依頼代行可能でしょうか。

難しいようでしたら金曜修正してもらいます。

どうぞよろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 14, 2025 9:46 PM

To: Kenichi Ushiroebisu

Subject: Re: [Report Review] ALPS [ID] CO. LTD.; [ID]

Dear Ushiroebisu-san,

Thank you for testing and making a RF report for ALAP UXC10.

There are two items that don't refer to the Test Plan correctly.

(1) Company Address

(2) Power Class: Class 1 → Class 2 (Test
setup is Class 2 as far as the log)

(3) Test Voltage: 14V→13.2V
(Test setup is 13.2V as far as the log)

After correcting (1) to (3), pleas ask Yu-san to approve.

Thanks

Best Regard,

Itsuo sakai

差出人 : Kenichi
Ushiroebisu

送信日時 : 2025 年 10 月 14 日
19:01

宛先 : Itsuo
Sakai

件名 : [Report
Review] ALPS [ID] CO. LTD.; [ID]

Dear Sakai-san,

Could you review the following test report?

Project ID: [ID]

Vender Name: ALPS [ID] CO. LTD

Model Name: UXC10 (RF)

Schedule:

Test Result: PASS

Comment: 在宅勤務対応として Teams 上に「Bluetooth データ共有」というデータ共有用のチームを作成し、そちらにもファイルを保存しました。

​ ​ RF ​ ​

Regards,

Kenichi Ushiroebisu

---

## 3. 2025-10-15 05:04

**From:** Itsuo Sakai
**To:** Yu Hong , Kousuke Nakayama

喩さんお疲れさまです。

RF試験ではテスターに入力したICSに対応した試験項目を実施した差異、

サポートしていない項目には「サポートしていない」という旨の応答がり、このテスター設定が他の試験項目の試験結果には何の影響も与えません。

ICSとテスターの設定が一致していないのは事実ですが、試験スケジュールがタイトなためこれで目をつむってください。

酒井差出人: Yu Hong

送信日時: 2025年10月15日 13:54

宛先: Kousuke Nakayama ; Itsuo Sakai

件名: RE: 【内部連絡】FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

酒井さん、中山さんお疲れ様です。

TX 側のログを確認したところ、 OUT Parameters において「Enhanced Power Control」が True に設定されていました。

しかし、 Test Plan の ICS では「Enhanced Power Control」が「No」と記載されているため、測定時の DUT の設定が ICS の仕様と一致していないことになります。

その場合、試験結果に影響が出る可能性はありますでしょうか？

また、再試験の実施は必要となりますでしょうか？

ご確認ください。

よろしくお願いします。

喩

From: Kousuke Nakayama

Sent: Wednesday, October 15, 2025 12:00 PM

To: Yu Hong

Subject: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

Dear
Yu -san,

Since Ushiroebisu-san is off today, I am contacting you on their behalf.

Could you review the following test report?

Project ID: [ID]

Vender Name: ALPS [ID] CO. LTD

Model Name: UXC10 (RF)

Schedule:

Test Result: PASS

Report File Path:
\\dataserver\LOGO\Bluetooth\Project\[ID]\2025\251007_UXC10_Sakai\RF\Report

Comment: 在宅勤務対応として Teams 上に「Bluetooth データ共有」というデータ共有用のチームを作成し、そちらにもファイルを保存しました。

​ ​

Regards

Kousuke Nakayama

---

## 4. 2025-10-15 05:16

**From:** Itsuo Sakai
**To:** Yu Hong

喩さんお疲れさまです。

ありがとうございます。

「客先がICSを認識していないため、念のため全項目を試験するために

ICSは全サポートを入力し、製品がサポート応答した項目にはすべて

Passしていることを確認してレポートを発行した」という運用とお考えください。

酒井差出人: Yu Hong

送信日時: 2025年10月15日 14:14

宛先: Itsuo Sakai

件名: RE: 【内部連絡】FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

酒井さん了解しました。

では続けてレポート内容を確認します。（DUT の返送を止める可能性があったため、先に酒井さんに確認メールを送りました）

よろしくお願いします。

喩

From: Itsuo Sakai

Sent: Wednesday, October 15, 2025 2:04 PM

To: Yu Hong ; Kousuke Nakayama

Subject: Re: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

喩さんお疲れさまです。

RF 試験ではテスターに入力した ICS に対応した試験項目を実施した差異、

サポートしていない項目には「サポートしていない」という旨の応答がり、このテスター設定が他の試験項目の試験結果には何の影響も与えません。

ICS とテスターの設定が一致していないのは事実ですが、試験スケジュールがタイトなためこれで目をつむってください。

酒井差出人 :
Yu Hong

送信日時 :
2025 年 10 月 15 日
13:54

宛先 :
Kousuke Nakayama ; Itsuo Sakai

件名 :
RE: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

酒井さん、中山さんお疲れ様です。

TX 側のログを確認したところ、 OUT Parameters において「Enhanced Power Control」が True に設定されていました。

しかし、 Test Plan の ICS では「Enhanced Power Control」が「No」と記載されているため、測定時の DUT の設定が ICS の仕様と一致していないことになります。

その場合、試験結果に影響が出る可能性はありますでしょうか？

また、再試験の実施は必要となりますでしょうか？

ご確認ください。

よろしくお願いします。

喩

From: Kousuke Nakayama

Sent: Wednesday, October 15, 2025 12:00 PM

To: Yu Hong

Subject: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

Dear
Yu -san,

Since Ushiroebisu-san is off today, I am contacting you on their behalf.

Could you review the following test report?

Project ID: [ID]

Vender Name: ALPS [ID] CO. LTD

Model Name: UXC10 (RF)

Schedule:

Test Result: PASS

Report File Path:
\\dataserver\LOGO\Bluetooth\Project\[ID]\2025\251007_UXC10_Sakai\RF\Report

Comment: 在宅勤務対応として Teams 上に「Bluetooth データ共有」というデータ共有用のチームを作成し、そちらにもファイルを保存しました。

​ ​

Regards

Kousuke Nakayama

---

## 5. 2025-10-15 06:58

**From:** Itsuo Sakai
**To:** Yu Hong , Kousuke Nakayama

喩さんお疲れさまです。
ICSで「Yes」と記載されている仕様に対して、DUTが非対応だった場合は
Failとなるのでしょうか？

⇒ログはInconclusiveとなります。
もしFailになる場合、ログ上でDUTがその機能に対して反応しないことを確認できた場合、製品がこの機能に非対応であると判断してよいのでしょうか？

⇒ALAP社は今年はじめの別モデルでEnhanced Power Cintrolを確認した際、

Qualcomm社に問い合わせて「SoCとしてはサポートしている」という回答でしたが同じくテスターログには「DUT indicates that it does not

support Enhanced Power Control (EPC)」と表示されました。その旨ALAP

担当者に伝え、非サポートが正しいのか確認してもらった結果、製品の電源投入後の初期化ルーティンでEPC機能をDisableしていることが判明しました。

結論としてはDisableしているからEPC非サポートでOkということになった過去があります。
それとも、その製品は設計上で当該機能に対応する予定でありながら、
まだ実装が不完全である可能性も考えられるでしょうか？

⇒設計検証サービスではそこまでの可能性を含めて対処しますが、認証試験では提出されたDUTが事実として非サポートと応答したのですからレポートもそれに基づいて発行すれば良いと判断できます。

酒井差出人: Yu Hong

送信日時: 2025年10月15日 15:39

宛先: Itsuo Sakai ; Kousuke Nakayama

件名: RE: 【内部連絡】FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

酒井さん、中山さんお疲れ様です。

レポート内容を確認しました。

問題ないです。

ありがとうございました。

酒井さんへ

ICS に関して、念のため下記を確認させてください。

ICS で「Yes」と記載されている仕様に対して、 DUT が非対応だった場合は Fail となるのでしょうか？

もし Fail になる場合、ログ上で DUT がその機能に対して反応しないことを確認できた場合、

製品がこの機能に非対応であると判断してよいのでしょうか？

それとも、その製品は設計上で当該機能に対応する予定でありながら、まだ実装が不完全である可能性も考えられるでしょうか？

ご確認よろしくお願いします。

喩

From: Itsuo Sakai

Sent: Wednesday, October 15, 2025 2:16 PM

To: Yu Hong

Subject: Re: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

喩さんお疲れさまです。

ありがとうございます。

「客先が ICS を認識していないため、念のため全項目を試験するために

ICS は全サポートを入力し、製品がサポート応答した項目にはすべて

Pass していることを確認してレポートを発行した」という運用とお考えください。

酒井差出人 :
Yu Hong

送信日時 :
2025 年 10 月 15 日
14:14

宛先 :
Itsuo Sakai

件名 :
RE: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

酒井さん了解しました。

では続けてレポート内容を確認します。（DUT の返送を止める可能性があったため、先に酒井さんに確認メールを送りました）

よろしくお願いします。

喩

From: Itsuo Sakai

Sent: Wednesday, October 15, 2025 2:04 PM

To: Yu Hong ; Kousuke Nakayama

Subject: Re: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

喩さんお疲れさまです。

RF 試験ではテスターに入力した ICS に対応した試験項目を実施した差異、

サポートしていない項目には「サポートしていない」という旨の応答がり、このテスター設定が他の試験項目の試験結果には何の影響も与えません。

ICS とテスターの設定が一致していないのは事実ですが、試験スケジュールがタイトなためこれで目をつむってください。

酒井差出人 :
Yu Hong

送信日時 :
2025 年 10 月 15 日
13:54

宛先 :
Kousuke Nakayama ; Itsuo Sakai

件名 :
RE: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

酒井さん、中山さんお疲れ様です。

TX 側のログを確認したところ、 OUT Parameters において「Enhanced Power Control」が True に設定されていました。

しかし、 Test Plan の ICS では「Enhanced Power Control」が「No」と記載されているため、測定時の DUT の設定が ICS の仕様と一致していないことになります。

その場合、試験結果に影響が出る可能性はありますでしょうか？

また、再試験の実施は必要となりますでしょうか？

ご確認ください。

よろしくお願いします。

喩

From: Kousuke Nakayama

Sent: Wednesday, October 15, 2025 12:00 PM

To: Yu Hong

Subject: 【内部連絡】 FW: [Report Review] ALPS [ID] CO. LTD.; [ID]

Dear
Yu -san,

Since Ushiroebisu-san is off today, I am contacting you on their behalf.

Could you review the following test report?

Project ID: [ID]

Vender Name: ALPS [ID] CO. LTD

Model Name: UXC10 (RF)

Schedule:

Test Result: PASS

Report File Path:
\\dataserver\LOGO\Bluetooth\Project\[ID]\2025\251007_UXC10_Sakai\RF\Report

Comment: 在宅勤務対応として Teams 上に「Bluetooth データ共有」というデータ共有用のチームを作成し、そちらにもファイルを保存しました。

​ ​

Regards

Kousuke Nakayama
