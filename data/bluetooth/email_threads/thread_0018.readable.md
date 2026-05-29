# thread_0018: Re: [内部連絡]RE: [Report Review] Denso ten Limited, [ID], Profile Test

- Message count: 1
- Source JSON: `thread_0018.json`

---

## 1. 2025-01-24 01:47

**From:** Itsuo Sakai
**To:** Kousuke Nakayama , Kei Tanaka

中山さんお疲れさまです。

責任が持てるとともに再Generate不要なアリオン実施分を記載してください。

酒井差出人: Kousuke Nakayama

送信日時: 2025年1月24日 10:30

宛先: Itsuo Sakai ; Kei Tanaka

件名: [内部連絡]RE: [Report Review] Denso ten Limited, [ID], Profile Test

酒井さんお疲れ様です。中山です。

田中さんに二次レビューを依頼したのですが、以下の修正依頼がありました。

以下の点についてご教示いただけますでしょうか。

・アリオン実施分とお客様実施分で重複している項目がございました。

こちらレポート上にはどちらを優先して記載するべきでしょうか。

HFP/HF/ACC/[ID] （アリオン実施 ver [ID] /
お客様実施 ver [ID]）

また、レポートに記載しない方については該当項目を削除し再 Generate が必要でしょうか。

お手数おかけしますがよろしくお願い致します中山光祐

From: Kei Tanaka

Sent: Thursday, January 23, 2025 10:44 PM

To: Kousuke Nakayama

Subject: RE: [Report Review] Denso ten Limited, [ID], Profile Test

中山さんレポートを確認しました。

以下の点の確認をお願いします。

・複数の DUT が使用されているがレポートに記載されているのは 1 つのみ。以下、テストログに記載されている BD アドレス。

[ID]( レポートに記載されているアドレス。アリオンで試験された DUT のアドレス。デンソーテンのテストログもこの DUT が多い )

[ID](A2DP、 AVRCP、 PBAP)

[ID]、 [ID](DIS)

[ID](MAP)

[ID]、 [ID](MPS)

・ MAP バージョンはテストログでは 1.4.2 が True となっているが、レポートでは 1.4 となっている・ PBAP バージョンはテストログでは 1.2.3 が True となっているが、レポートでは 1.2 となっている・ PTS software version の項に 8.5.4/8.6.0/8.7.0/8.7.1/8.7.2/8.7.3/8.7.4 とあるが、 8.7.4 が使用されたテストログが見当たらない・顧客実施分のテストログ関連・試験実施日がテストログでは 12 月 17 日になっている。レポートでは 11 月 17 日になっている。

DIS/SR/SGGIT/CHA/[ID]

DIS/SR/SGGIT/CHA/[ID]

・試験実施日がテストログでは 12 月 4 日になっている。レポートでは 11 月 4 日になっている。

A2DP/SNK/AS/[ID]

・試験実施日がテストログでは 12 月 4 日になっている。レポートでは 11 月 4 日になっている。

AVRCP/CT/MCN/NP/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/CA/[ID]

・試験実施日がテストログでは 12 月 16 日になっている。レポートでは 11 月 16 日になっている。

AVRCP/CT/RCR/[ID]

DIS/SR/SGGIT/CHA/[ID]

DIS/SR/SGGIT/CHA/[ID]

DIS/SR/SGGIT/SER/[ID]

MPS/[ID]/HFAV/CLH/MD/[ID]

MPS/[ID]/HFAV/CLH/MD/[ID]

MPS/[ID]/HFAV/CLH/MD/[ID]

MPS/[ID]/HFAV/CLH/MD/[ID]

MPS/[ID]/HFAV/CLH/MD/[ID]

MPS/[ID]/HFAV/CLH/MD/[ID]

・試験実施日がテストログでは 12 月 9 日になっている。レポートでは 11 月 9 日になっている。

AVRCP/TG/VLH/[ID]

AVRCP/CT/MPS/[ID]

AVRCP/CT/CA/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/MCN/CB/[ID]

AVRCP/CT/CA/[ID]

AVRCP/CT/CA/[ID]

・試験実施日がテストログでは 12 月 5 日になっている。レポートでは 11 月 5 日になっている。

AVRCP/CT/MCN/NP/[ID]

・試験実施日がテストログでは 12 月 18 日になっている。レポートでは 11 月 18 日になっている。

AVRCP/CT/PTH/[ID]

AVRCP/CT/PTT/[ID]

AVRCP/CT/MPS/[ID]

・ツールバージョンがテストログでは [ID] になっている。レポートでは [ID] になっている。

MPS/[ID]/HFAV/CLH/MD/[ID]

・レポートには記載なし。デンソーテンが作成した PDF レポートをそのまま使うのであればこのままでよい。

MPS/[ID]/AVO/ACT/SD/[ID]

・アリオン実施分のテストログ関連・顧客実施分と重複している。バージョンは顧客実施が [ID]、アリオン実施が [ID]。レポートには [ID] が記載されている。

HFP/HF/ACC/[ID]

田中

From: Kousuke Nakayama

Sent: Thursday, January 23, 2025 10:54 AM

To: Kei Tanaka

Subject: [Report Review] Denso ten Limited, [ID], Profile Test

Dear Tanaka-san,

Could you review the following test report?

Project ID: [ID]

Vender Name: Denso ten Limited

Model Name: [ID]

Schedule:

Test Result: Pass

Report File Path:
\\dataserver\LOGO\Bluetooth\Project\Denso-Ten\240523_Majima\(6696)[ID]( 上位）\Report\Profile

Comment: 在宅勤務対応として Teams 上に「Bluetooth データ共有」というデータ共有用のチームを作成し、そちらにもファイルを保存しました。

Regards,

Kousuke Nakayama
