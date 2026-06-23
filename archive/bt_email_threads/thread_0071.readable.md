# thread_0071: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について

- Message count: 10
- Source JSON: `thread_0071.json`

---

## 1. 2025-10-10 07:31

**From:** Itsuo Sakai
**To:** Kousuke Nakayama , Toshitaka Mochizuki
**Attachments:** Report_IOPT.zip

望月さんお疲れさまです。

添付ファイルとともに下記文面をALAP酒井様に送って非Pass

項目の解析およびFW改修を依頼してください。

酒井ーーーー

ALAP(UXC10)のIOPT試験で18項目中14項目はPassしました。

残る下記項目がFail、またはINDCSVとなっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

上記のPTSレポート(ログ付)を添付しますので、ご確認および解析をお願いします。特に製品のSDPレコード内容を重点的にご確認ください。

PTSのIXITの設定で対処できるものはその旨お知しらせください。FW改修が必要な場合は改修FWをご準備ください。

ーーーー差出人: Kousuke Nakayama

送信日時: 2025年10月10日 14:47

宛先: Itsuo Sakai

件名: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さんお疲れ様です。中山です。

AlpsAlpine 様の UXC10 の Profile 試験について、

下記項目で Fail、または [ID] となっております。

別の PTS バージョン (8.8.1) で確認しましたが、同様の結果となっております。

・ IOPT/MAP/MCE/CGSIT/SFC/[ID]

・ IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らく DUT 側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Log を添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験では PTS バージョン 8.8.1 で PASS となりました。

念のためご報告いたします。

・ IOPT/SR/COD/[ID]

[ID]/FAIL 8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 2. 2025-10-16 00:30

**From:** Itsuo Sakai
**To:** Kousuke Nakayama , Kenichi Ushiroebisu
**Attachments:** UXC10_ICS_Pass-Report.zip

中山さん、後夷さんお疲れさまです。

先日のIOPT試験でPassしなかった4項目について客先からPassレポートが届きました。

客先レポートを見ると「Releases [ID]」でPassしていて、AJ実施非Passレポートとの違いはICSです。先日のAJレポートで作成した

Export ICSを生成した仮ProjectのICSと客先レポートのICSは一致しており、AJの非PassレポートのICSは大きく異なっています。

再度仮ProjectからExport ICSファイルと客先レポートを添付します。

まずは客先PassレポートのICSをアリオンv8.10.2の方で客先レポートのICSに修正してMAP, PBAP, SPPの再試験を行ってください。

酒井差出人: Kousuke Nakayama

送信日時: 2025年10月10日 14:47

宛先: Itsuo Sakai

件名: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さんお疲れ様です。中山です。

AlpsAlpine 様の UXC10 の Profile 試験について、

下記項目で Fail、または [ID] となっております。

別の PTS バージョン (8.8.1) で確認しましたが、同様の結果となっております。

・ IOPT/MAP/MCE/CGSIT/SFC/[ID]

・ IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らく DUT 側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Log を添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験では PTS バージョン 8.8.1 で PASS となりました。

念のためご報告いたします。

・ IOPT/SR/COD/[ID]

[ID]/FAIL 8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 3. 2025-10-16 05:52

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , Kousuke Nakayama , Kenichi Ushiroebisu

望月さんお疲れさまです。

優先順位はアルプスアルパインのプロファイル試験→コイズミ照明→SONY

の順番でお願いします。

酒井差出人: Toshitaka Mochizuki

送信日時: 2025年10月16日 14:47

宛先: Itsuo Sakai ; Kousuke Nakayama ; Kenichi Ushiroebisu

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん望月です本日Bluetooth担当者が全員Bletoothイベント参加のため不在となっておりますので、明日、確認となる予定ですが、

コイズミ照明、アルプスアルパイン、SONYと同時に入っておりますので、

プロファイル試験はSONYより先にこちらを確認したほうがよさそうでしょうか。

コイズミはRFになります。

なお中山さんはFeliCaの方へ基本戻られました。

どうぞよろしくお願い申し上げます。

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ; Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 4. 2025-10-17 02:28

**From:** Itsuo Sakai
**To:** Yu Hong

喩さんお疲れさです。

当初Fail/Inconclusveの4件を客先に連絡した際、MAP, PBAP, SPPの

ICSを変更するとそれらプロファイルの全試験が発生して試験費用がか加算されると望月さんから連絡した返信で、そのように客先から返信がありました。

しかしその後、客先から送付されたPassレポートを精査した結果、MAP,

PBAP, SPPのICSを修正しない状態で試験が行われていて、アリオンでの試験にミスがあったと思われ再試験を行う予定で。また、望月さんからは客先レポートと同じPTSバージョンで再試験を行う旨のメールを客先へ送っています。

客先からのPassレポート送付時のメールには「当初のICSのままPassしている。追加費用云々以前にやるべきことをアリオンはやっていない」

のお叱りまでは明示されていませんが、暗示的に「ICS変更をしなくてもPassする」ことを添付Passレポートで主張しています。したがってアリオンはICS変更の判断を待たずにICS変更なしで即座に再試験を行うべきです。

関連メールはすべてを読んで現状判断してください。

酒井差出人: Yu Hong

送信日時: 2025年10月17日 11:07

宛先: Itsuo Sakai

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さんお疲れ様です。

アルプスアルパインのプロファイル試験ですが、お客さんとのやり取りメールによりますと、

MAP, PBAP, SPP の ICS を修正して IOPT 試験に対応するかどうか、社内検討となっているようです。

アルプスアルパインから社内方針を決めていたから、Profile試験を再開していかかでしょうか？

なお、PTS [ID] でのIOPT試験（ICS更新されていないもの）は中山さんは当時実施したと認識しています。

結果は 8.8.1と変わっていません。

ご確認よろしくお願いします。

喩

From: Kousuke Nakayama

Sent: Friday, October 17, 2025 10:58 AM

To: Toshitaka Mochizuki

Subject: RE: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について望月さんお疲れ様です。中山です。

下記、承知しました。

タイミング見てProfile試験対応いたします。

よろしくお願いいたします。

中山光祐

From: Toshitaka Mochizuki

Sent: Friday, October 17, 2025 10:40 AM

To: Kousuke Nakayama

Subject: FW: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん望月です。

お忙しいところ申し訳ありません。

本日FeliCaトレーニング中だとおもいますが、後夷さんが急遽お休みになってしまいました。

可能であればFeliCaトレーニングの合間、もしくは数時間トレーニング時間調整、または残業いただき、

AlpsAlpineのプロファイル再試験を添付の酒井さんの指示の内容で走らせていただくことは可能でしょうか。

対応できるようでしたら進捗状況を喩さんにも共有しておいていただけると助かります。

負荷かけてしまい申し訳ありませんが、ご検討お願いいたします。

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 2:52 PM

To: Toshitaka Mochizuki ;
Kousuke Nakayama ;
Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について望月さんお疲れさまです。

優先順位はアルプスアルパインのプロファイル試験 → コイズミ照明 →SONY

の順番でお願いします。

酒井差出人 : Toshitaka Mochizuki

送信日時 : 2025 年 10 月 16 日 14:47

宛先 : Itsuo Sakai ;
Kousuke Nakayama ;
Kenichi Ushiroebisu

件名 : RE:
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さん望月です本日Bluetooth担当者が全員Bletoothイベント参加のため不在となっておりますので、明日、確認となる予定ですが、

コイズミ照明、アルプスアルパイン、SONYと同時に入っておりますので、

プロファイル試験はSONYより先にこちらを確認したほうがよさそうでしょうか。

コイズミはRFになります。

なお中山さんはFeliCaの方へ基本戻られました。

どうぞよろしくお願い申し上げます。

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ;
Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 5. 2025-10-18 09:52

**From:** Itsuo Sakai
**To:** Kousuke Nakayama

中山さんお疲れさまです。

遅くまでALAP社のIOPT試験実施ありがとうございます。

.xmlファイルはOutlookサーバーが配信しない形式のためzip圧縮して再送してください。
送付されたICSをインポートして確認しました。
MAP、PBAPはPASSとなりましたが、SPPでINDCSV・FAILとなってしまいます。

⇒前回もICSファイルをインポートしたと思いますがインポート元のProjectと大きく異なっています。(それで私は客先のレポートのICSを設定するようお願いしましたが、今回インポート後のPTS

のICSは客先レポートのICSに一致していましたか？。)

以上ご対応ください。

酒井差出人: Kousuke Nakayama

送信日時: 2025年10月17日 18:49

宛先: Itsuo Sakai

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さんお疲れ様です。中山です。

送付されたICSをインポートして確認しました。

MAP、PBAPはPASSとなりましたが、SPPでINDCSV・FAILとなってしまいます。

レポート添付いたしますので確認いただけますでしょうか。

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

ペアリング設定後、接続と切断を何度か自動で繰り返し、INDCSVとなってしまいます。

・IOPT/SPP/DEVB/SDPR/[ID]

ペアリング設定後にFailとなってしまいます。

対応策、もしくは確認すべきことがあればご教示いただけますでしょうか。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ; Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 6. 2025-10-20 02:38

**From:** Itsuo Sakai
**To:** Kousuke Nakayama , Toshitaka Mochizuki , Kenichi Ushiroebisu

中山さんお疲れさまです。

UVC10のICSは客先から直接受け取っておらず、IOPTではTSPC_ALLで

Test Planの試験項目を選択すれば試験可能と思っていました。

しかし客先に8.10.2および8.8.1のどちらでもPassしなかった旨を知らせると返信メールで8.10.2でPassしたMAP,PBAP, SPPの客先実施レポートが返信されました。アリオンレポートと比較するとICS設定が異なるだけのようです。(試験前にDUT側で対向機器リストからPTS

を削除するなどの何らかの操作が必要なのかもしれません。)

このため、参照先のHost Subsysem(下記URL)そのままという指示で

ICSファイルは提供されていないため、2回目のIOPT試験では仮Project

でそれをInckudeしてExport ICSを生成して添付しました。

客先レポートのICSは上記Host SubsystemのView ICSページで表示される内容および仮ProjectのICSと一致していることは確認済です。

酒井差出人: Kousuke Nakayama

送信日時: 2025年10月20日 11:05

宛先: Itsuo Sakai ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、望月さん、後夷さんお疲れ様です。中山です。

酒井さん最初に実施する際、サーバー上にICSが保存されておりませんでした。

その際、手動で試験する方法(試験項目を選択し、ICSにチェックが必要な項目にチェックを入れることで実施可能)を教わっていましたので、今回はそちらで対応いたしました。

本来であればサーバー上にICSが見つからない時点で望月さんに確認すべきでしたが、ICSが無いものと思い込み、確認を致しませんでした。大変申し訳ありません。

ですので、ICSをインポートして試験を行ったのは客先から送られてきたICSファイルのみになります。

現在、FeliCa業務のスケジュールが詰まっていて、早急な対応が難しいため、ICSの確認については後夷さんにお任せいたしました。

望月さんお手数ですが、酒井さんから送られているUXC10のICSファイルの保存先を後夷さんに共有いただけますでしょうか。

後夷さん病み上がりで申し訳ありませんが、こちらの対応お願い致します。

ＤＵＴの操作方法などでわからないことあればご連絡ください。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Saturday, October 18, 2025 6:52 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さんお疲れさまです。

遅くまで ALAP 社の IOPT 試験実施ありがとうございます。

.xml ファイルは Outlook サーバーが配信しない形式のため zip 圧縮して再送してください。
送付された ICS をインポートして確認しました。
MAP、 PBAP は PASS となりましたが、 SPP で [ID] ・ FAIL となってしまいます。

⇒ 前回も ICS ファイルをインポートしたと思いますがインポート元の Project と大きく異なっています。 ( それで私は客先のレポートの ICS を設定するようお願いしましたが、今回インポート後の PTS

の ICS は客先レポートの ICS に一致していましたか？。 )

以上ご対応ください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 17 日 18:49

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

送付されたICSをインポートして確認しました。

MAP、PBAPはPASSとなりましたが、SPPでINDCSV・FAILとなってしまいます。

レポート添付いたしますので確認いただけますでしょうか。

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

ペアリング設定後、接続と切断を何度か自動で繰り返し、INDCSVとなってしまいます。

・IOPT/SPP/DEVB/SDPR/[ID]

ペアリング設定後にFailとなってしまいます。

対応策、もしくは確認すべきことがあればご教示いただけますでしょうか。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ;
Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 7. 2025-10-20 03:25

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu , Kousuke Nakayama , Toshitaka Mochizuki

後夷さんお疲れさまです。

まずは客先レポートのICSを参照してください。

SIGサイトでICSを確認するには下記を試してください。

(1) [URL] でログインが必要です。

(2) Qualification Workspacehのトップへ飛んだら再度URLを入力酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 12:09

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

本件は、中山光祐さんから、後夷が引き継ぎました。

ICSファイルが添付されていないようですので、ご確認の上、再送いただけますでしょうか。

(リンク先を見ましたが、見当たりませんでした。)

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 11:38

宛先: Kousuke Nakayama ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について中山さんお疲れさまです。

UVC10のICSは客先から直接受け取っておらず、IOPTではTSPC_ALLで

Test Planの試験項目を選択すれば試験可能と思っていました。

しかし客先に8.10.2および8.8.1のどちらでもPassしなかった旨を知らせると返信メールで8.10.2でPassしたMAP,PBAP, SPPの客先実施レポートが返信されました。アリオンレポートと比較するとICS設定が異なるだけのようです。(試験前にDUT側で対向機器リストからPTS

を削除するなどの何らかの操作が必要なのかもしれません。)

このため、参照先のHost Subsysem(下記URL)そのままという指示で

ICSファイルは提供されていないため、2回目のIOPT試験では仮Project

でそれをInckudeしてExport ICSを生成して添付しました。

客先レポートのICSは上記Host SubsystemのView ICSページで表示される内容および仮ProjectのICSと一致していることは確認済です。

酒井差出人: Kousuke Nakayama

送信日時: 2025年10月20日 11:05

宛先: Itsuo Sakai ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、望月さん、後夷さんお疲れ様です。中山です。

酒井さん最初に実施する際、サーバー上にICSが保存されておりませんでした。

その際、手動で試験する方法(試験項目を選択し、ICSにチェックが必要な項目にチェックを入れることで実施可能)を教わっていましたので、今回はそちらで対応いたしました。

本来であればサーバー上にICSが見つからない時点で望月さんに確認すべきでしたが、ICSが無いものと思い込み、確認を致しませんでした。大変申し訳ありません。

ですので、ICSをインポートして試験を行ったのは客先から送られてきたICSファイルのみになります。

現在、FeliCa業務のスケジュールが詰まっていて、早急な対応が難しいため、ICSの確認については後夷さんにお任せいたしました。

望月さんお手数ですが、酒井さんから送られているUXC10のICSファイルの保存先を後夷さんに共有いただけますでしょうか。

後夷さん病み上がりで申し訳ありませんが、こちらの対応お願い致します。

ＤＵＴの操作方法などでわからないことあればご連絡ください。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Saturday, October 18, 2025 6:52 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さんお疲れさまです。

遅くまで ALAP 社の IOPT 試験実施ありがとうございます。

.xml ファイルは Outlook サーバーが配信しない形式のため zip 圧縮して再送してください。
送付された ICS をインポートして確認しました。
MAP、 PBAP は PASS となりましたが、 SPP で [ID] ・ FAIL となってしまいます。

⇒ 前回も ICS ファイルをインポートしたと思いますがインポート元の Project と大きく異なっています。 ( それで私は客先のレポートの ICS を設定するようお願いしましたが、今回インポート後の PTS

の ICS は客先レポートの ICS に一致していましたか？。 )

以上ご対応ください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 17 日 18:49

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

送付されたICSをインポートして確認しました。

MAP、PBAPはPASSとなりましたが、SPPでINDCSV・FAILとなってしまいます。

レポート添付いたしますので確認いただけますでしょうか。

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

ペアリング設定後、接続と切断を何度か自動で繰り返し、INDCSVとなってしまいます。

・IOPT/SPP/DEVB/SDPR/[ID]

ペアリング設定後にFailとなってしまいます。

対応策、もしくは確認すべきことがあればご教示いただけますでしょうか。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ;
Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 8. 2025-10-20 07:01

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu , Kousuke Nakayama , Toshitaka Mochizuki

後夷さんお疲れさまです。

SPP試験実施ありがとうございます。

MAP, PBAPも実施願います。

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 16:00

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

ICSについて、下記の3つのものが同じであることを確認いたしました。

客先レポート酒井さんからご連絡いただいたもの現在、試験で使用しているPTSソフトウェア

PASSしていない2項目を、再度実行いたしましたが、PASSしませんでした。

IOPT/SPP/DEVA/CGSIT/SFC/[ID] ([ID])

IOPT/SPP/DEVB/SDPR/[ID] (FAIL)

他に確認すべき点などございましたら、ご連絡いただけますでしょうか。

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 12:25

宛先: Kenichi Ushiroebisu ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について後夷さんお疲れさまです。

まずは客先レポートのICSを参照してください。

SIGサイトでICSを確認するには下記を試してください。

(1) [URL] でログインが必要です。

(2) Qualification Workspacehのトップへ飛んだら再度URLを入力酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 12:09

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

本件は、中山光祐さんから、後夷が引き継ぎました。

ICSファイルが添付されていないようですので、ご確認の上、再送いただけますでしょうか。

(リンク先を見ましたが、見当たりませんでした。)

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 11:38

宛先: Kousuke Nakayama ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について中山さんお疲れさまです。

UVC10のICSは客先から直接受け取っておらず、IOPTではTSPC_ALLで

Test Planの試験項目を選択すれば試験可能と思っていました。

しかし客先に8.10.2および8.8.1のどちらでもPassしなかった旨を知らせると返信メールで8.10.2でPassしたMAP,PBAP, SPPの客先実施レポートが返信されました。アリオンレポートと比較するとICS設定が異なるだけのようです。(試験前にDUT側で対向機器リストからPTS

を削除するなどの何らかの操作が必要なのかもしれません。)

このため、参照先のHost Subsysem(下記URL)そのままという指示で

ICSファイルは提供されていないため、2回目のIOPT試験では仮Project

でそれをInckudeしてExport ICSを生成して添付しました。

客先レポートのICSは上記Host SubsystemのView ICSページで表示される内容および仮ProjectのICSと一致していることは確認済です。

酒井差出人: Kousuke Nakayama

送信日時: 2025年10月20日 11:05

宛先: Itsuo Sakai ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、望月さん、後夷さんお疲れ様です。中山です。

酒井さん最初に実施する際、サーバー上にICSが保存されておりませんでした。

その際、手動で試験する方法(試験項目を選択し、ICSにチェックが必要な項目にチェックを入れることで実施可能)を教わっていましたので、今回はそちらで対応いたしました。

本来であればサーバー上にICSが見つからない時点で望月さんに確認すべきでしたが、ICSが無いものと思い込み、確認を致しませんでした。大変申し訳ありません。

ですので、ICSをインポートして試験を行ったのは客先から送られてきたICSファイルのみになります。

現在、FeliCa業務のスケジュールが詰まっていて、早急な対応が難しいため、ICSの確認については後夷さんにお任せいたしました。

望月さんお手数ですが、酒井さんから送られているUXC10のICSファイルの保存先を後夷さんに共有いただけますでしょうか。

後夷さん病み上がりで申し訳ありませんが、こちらの対応お願い致します。

ＤＵＴの操作方法などでわからないことあればご連絡ください。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Saturday, October 18, 2025 6:52 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さんお疲れさまです。

遅くまで ALAP 社の IOPT 試験実施ありがとうございます。

.xml ファイルは Outlook サーバーが配信しない形式のため zip 圧縮して再送してください。
送付された ICS をインポートして確認しました。
MAP、 PBAP は PASS となりましたが、 SPP で [ID] ・ FAIL となってしまいます。

⇒ 前回も ICS ファイルをインポートしたと思いますがインポート元の Project と大きく異なっています。 ( それで私は客先のレポートの ICS を設定するようお願いしましたが、今回インポート後の PTS

の ICS は客先レポートの ICS に一致していましたか？。 )

以上ご対応ください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 17 日 18:49

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

送付されたICSをインポートして確認しました。

MAP、PBAPはPASSとなりましたが、SPPでINDCSV・FAILとなってしまいます。

レポート添付いたしますので確認いただけますでしょうか。

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

ペアリング設定後、接続と切断を何度か自動で繰り返し、INDCSVとなってしまいます。

・IOPT/SPP/DEVB/SDPR/[ID]

ペアリング設定後にFailとなってしまいます。

対応策、もしくは確認すべきことがあればご教示いただけますでしょうか。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ;
Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 9. 2025-10-20 07:30

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu , Kousuke Nakayama , Toshitaka Mochizuki

望月さんお疲れさまです。

後夷さんのMAP,PBAP試験結果を待って、Passしない場合には以下のメールを客先へ送ってください。

酒井ーーーー御社からご送付いただいたSPP, MAP, PBAPのPTSレポートと同じICS

設定であることを確認してv8.10.2で再試験を実施しましたが結果は以前と同じくPassしません。

SPP, MAP, PBAPのPTS試験では、スタート前にDUTの接続済機器一覧から

PTSを削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいたPassレポートを得られたDUTのSWが当社のDUT

のSWから更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいたPTSレポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。ご検討をお願いします。

ーーーー差出人: Itsuo Sakai

送信日時: 2025年10月20日 16:01

宛先: Kenichi Ushiroebisu ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について後夷さんお疲れさまです。

SPP試験実施ありがとうございます。

MAP, PBAPも実施願います。

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 16:00

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

ICSについて、下記の3つのものが同じであることを確認いたしました。

客先レポート酒井さんからご連絡いただいたもの現在、試験で使用しているPTSソフトウェア

PASSしていない2項目を、再度実行いたしましたが、PASSしませんでした。

IOPT/SPP/DEVA/CGSIT/SFC/[ID] ([ID])

IOPT/SPP/DEVB/SDPR/[ID] (FAIL)

他に確認すべき点などございましたら、ご連絡いただけますでしょうか。

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 12:25

宛先: Kenichi Ushiroebisu ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について後夷さんお疲れさまです。

まずは客先レポートのICSを参照してください。

SIGサイトでICSを確認するには下記を試してください。

(1) [URL] でログインが必要です。

(2) Qualification Workspacehのトップへ飛んだら再度URLを入力酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 12:09

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

本件は、中山光祐さんから、後夷が引き継ぎました。

ICSファイルが添付されていないようですので、ご確認の上、再送いただけますでしょうか。

(リンク先を見ましたが、見当たりませんでした。)

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 11:38

宛先: Kousuke Nakayama ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について中山さんお疲れさまです。

UVC10のICSは客先から直接受け取っておらず、IOPTではTSPC_ALLで

Test Planの試験項目を選択すれば試験可能と思っていました。

しかし客先に8.10.2および8.8.1のどちらでもPassしなかった旨を知らせると返信メールで8.10.2でPassしたMAP,PBAP, SPPの客先実施レポートが返信されました。アリオンレポートと比較するとICS設定が異なるだけのようです。(試験前にDUT側で対向機器リストからPTS

を削除するなどの何らかの操作が必要なのかもしれません。)

このため、参照先のHost Subsysem(下記URL)そのままという指示で

ICSファイルは提供されていないため、2回目のIOPT試験では仮Project

でそれをInckudeしてExport ICSを生成して添付しました。

客先レポートのICSは上記Host SubsystemのView ICSページで表示される内容および仮ProjectのICSと一致していることは確認済です。

酒井差出人: Kousuke Nakayama

送信日時: 2025年10月20日 11:05

宛先: Itsuo Sakai ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、望月さん、後夷さんお疲れ様です。中山です。

酒井さん最初に実施する際、サーバー上にICSが保存されておりませんでした。

その際、手動で試験する方法(試験項目を選択し、ICSにチェックが必要な項目にチェックを入れることで実施可能)を教わっていましたので、今回はそちらで対応いたしました。

本来であればサーバー上にICSが見つからない時点で望月さんに確認すべきでしたが、ICSが無いものと思い込み、確認を致しませんでした。大変申し訳ありません。

ですので、ICSをインポートして試験を行ったのは客先から送られてきたICSファイルのみになります。

現在、FeliCa業務のスケジュールが詰まっていて、早急な対応が難しいため、ICSの確認については後夷さんにお任せいたしました。

望月さんお手数ですが、酒井さんから送られているUXC10のICSファイルの保存先を後夷さんに共有いただけますでしょうか。

後夷さん病み上がりで申し訳ありませんが、こちらの対応お願い致します。

ＤＵＴの操作方法などでわからないことあればご連絡ください。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Saturday, October 18, 2025 6:52 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さんお疲れさまです。

遅くまで ALAP 社の IOPT 試験実施ありがとうございます。

.xml ファイルは Outlook サーバーが配信しない形式のため zip 圧縮して再送してください。
送付された ICS をインポートして確認しました。
MAP、 PBAP は PASS となりましたが、 SPP で [ID] ・ FAIL となってしまいます。

⇒ 前回も ICS ファイルをインポートしたと思いますがインポート元の Project と大きく異なっています。 ( それで私は客先のレポートの ICS を設定するようお願いしましたが、今回インポート後の PTS

の ICS は客先レポートの ICS に一致していましたか？。 )

以上ご対応ください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 17 日 18:49

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

送付されたICSをインポートして確認しました。

MAP、PBAPはPASSとなりましたが、SPPでINDCSV・FAILとなってしまいます。

レポート添付いたしますので確認いただけますでしょうか。

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

ペアリング設定後、接続と切断を何度か自動で繰り返し、INDCSVとなってしまいます。

・IOPT/SPP/DEVB/SDPR/[ID]

ペアリング設定後にFailとなってしまいます。

対応策、もしくは確認すべきことがあればご教示いただけますでしょうか。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ;
Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐

---

## 10. 2025-10-20 08:01

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu , Kousuke Nakayama , Toshitaka Mochizuki

望月さんお疲れさまです。

以下のメールをALAP IXC10ソフト担当の客先へ送ってください。

酒井ーーーー御社からご送付いただいたSPPのPTSレポートと同じICS設定であることを確認してv8.10.2で再試験を実施しましたところ、MAPとPBAPはPass

しましたがSPPはPassしませんでした。

SPPのPTS試験では、スタート前にDUTの接続済機器一覧からPTSを削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいたPassレポートを得られたDUTのSWが当社のDUT

のSWから更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいたSPPのPTSレポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討をお願いします。

ーーーー差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 16:57

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

MAP, PBAPはPASSいたしました。

お送りいただいた文案を修正して、お客様に問い合わせいたします。

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 16:30

宛先: Kenichi Ushiroebisu ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について望月さんお疲れさまです。

後夷さんのMAP,PBAP試験結果を待って、Passしない場合には以下のメールを客先へ送ってください。

酒井ーーーー御社からご送付いただいたSPP, MAP, PBAPのPTSレポートと同じICS

設定であることを確認してv8.10.2で再試験を実施しましたが結果は以前と同じくPassしません。

SPP, MAP, PBAPのPTS試験では、スタート前にDUTの接続済機器一覧から

PTSを削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいたPassレポートを得られたDUTのSWが当社のDUT

のSWから更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいたPTSレポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。ご検討をお願いします。

ーーーー差出人: Itsuo Sakai

送信日時: 2025年10月20日 16:01

宛先: Kenichi Ushiroebisu ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について後夷さんお疲れさまです。

SPP試験実施ありがとうございます。

MAP, PBAPも実施願います。

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 16:00

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

ICSについて、下記の3つのものが同じであることを確認いたしました。

客先レポート酒井さんからご連絡いただいたもの現在、試験で使用しているPTSソフトウェア

PASSしていない2項目を、再度実行いたしましたが、PASSしませんでした。

IOPT/SPP/DEVA/CGSIT/SFC/[ID] ([ID])

IOPT/SPP/DEVB/SDPR/[ID] (FAIL)

他に確認すべき点などございましたら、ご連絡いただけますでしょうか。

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 12:25

宛先: Kenichi Ushiroebisu ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について後夷さんお疲れさまです。

まずは客先レポートのICSを参照してください。

SIGサイトでICSを確認するには下記を試してください。

(1) [URL] でログインが必要です。

(2) Qualification Workspacehのトップへ飛んだら再度URLを入力酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年10月20日 12:09

宛先: Itsuo Sakai ; Kousuke Nakayama ; Toshitaka Mochizuki

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、

お疲れ様です。

本件は、中山光祐さんから、後夷が引き継ぎました。

ICSファイルが添付されていないようですので、ご確認の上、再送いただけますでしょうか。

(リンク先を見ましたが、見当たりませんでした。)

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 10 月 20 日 (月曜日) 11:38

宛先: Kousuke Nakayama ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: Re: 【内部連絡】AlpsAlpine_UXC10_Profile試験について中山さんお疲れさまです。

UVC10のICSは客先から直接受け取っておらず、IOPTではTSPC_ALLで

Test Planの試験項目を選択すれば試験可能と思っていました。

しかし客先に8.10.2および8.8.1のどちらでもPassしなかった旨を知らせると返信メールで8.10.2でPassしたMAP,PBAP, SPPの客先実施レポートが返信されました。アリオンレポートと比較するとICS設定が異なるだけのようです。(試験前にDUT側で対向機器リストからPTS

を削除するなどの何らかの操作が必要なのかもしれません。)

このため、参照先のHost Subsysem(下記URL)そのままという指示で

ICSファイルは提供されていないため、2回目のIOPT試験では仮Project

でそれをInckudeしてExport ICSを生成して添付しました。

客先レポートのICSは上記Host SubsystemのView ICSページで表示される内容および仮ProjectのICSと一致していることは確認済です。

酒井差出人: Kousuke Nakayama

送信日時: 2025年10月20日 11:05

宛先: Itsuo Sakai ; Toshitaka Mochizuki ; Kenichi Ushiroebisu

件名: RE: 【内部連絡】AlpsAlpine_UXC10_Profile試験について酒井さん、望月さん、後夷さんお疲れ様です。中山です。

酒井さん最初に実施する際、サーバー上にICSが保存されておりませんでした。

その際、手動で試験する方法(試験項目を選択し、ICSにチェックが必要な項目にチェックを入れることで実施可能)を教わっていましたので、今回はそちらで対応いたしました。

本来であればサーバー上にICSが見つからない時点で望月さんに確認すべきでしたが、ICSが無いものと思い込み、確認を致しませんでした。大変申し訳ありません。

ですので、ICSをインポートして試験を行ったのは客先から送られてきたICSファイルのみになります。

現在、FeliCa業務のスケジュールが詰まっていて、早急な対応が難しいため、ICSの確認については後夷さんにお任せいたしました。

望月さんお手数ですが、酒井さんから送られているUXC10のICSファイルの保存先を後夷さんに共有いただけますでしょうか。

後夷さん病み上がりで申し訳ありませんが、こちらの対応お願い致します。

ＤＵＴの操作方法などでわからないことあればご連絡ください。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Saturday, October 18, 2025 6:52 PM

To: Kousuke Nakayama

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さんお疲れさまです。

遅くまで ALAP 社の IOPT 試験実施ありがとうございます。

.xml ファイルは Outlook サーバーが配信しない形式のため zip 圧縮して再送してください。

送付された ICS をインポートして確認しました。
MAP、 PBAP は PASS となりましたが、 SPP で [ID] ・ FAIL となってしまいます。

⇒ 前回も ICS ファイルをインポートしたと思いますがインポート元の Project と大きく異なっています。 ( それで私は客先のレポートの ICS を設定するようお願いしましたが、今回インポート後の PTS

の ICS は客先レポートの ICS に一致していましたか？。 )

以上ご対応ください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 17 日 18:49

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

送付されたICSをインポートして確認しました。

MAP、PBAPはPASSとなりましたが、SPPでINDCSV・FAILとなってしまいます。

レポート添付いたしますので確認いただけますでしょうか。

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

ペアリング設定後、接続と切断を何度か自動で繰り返し、INDCSVとなってしまいます。

・IOPT/SPP/DEVB/SDPR/[ID]

ペアリング設定後にFailとなってしまいます。

対応策、もしくは確認すべきことがあればご教示いただけますでしょうか。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Thursday, October 16, 2025 9:30 AM

To: Kousuke Nakayama ;
Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 AlpsAlpine_UXC10_Profile 試験について中山さん、後夷さんお疲れさまです。

先日の IOPT 試験で Pass しなかった 4 項目について客先から Pass レポートが届きました。

客先レポートを見ると「Releases [ID]」で Pass していて、 AJ 実施非 Pass レポートとの違いは ICS です。先日の AJ レポートで作成した

Export ICS を生成した仮 Project の ICS と客先レポートの ICS は一致しており、 AJ の非 Pass レポートの ICS は大きく異なっています。

再度仮 Project から Export
ICS ファイルと客先レポートを添付します。

まずは客先 Pass レポートの ICS をアリオン v8.10.2 の方で客先レポートの ICS に修正して MAP,
PBAP, SPP の再試験を行ってください。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 10 月 10 日 14:47

宛先 : Itsuo Sakai

件名 :
【内部連絡】 AlpsAlpine_UXC10_Profile 試験について酒井さんお疲れ様です。中山です。

AlpsAlpine様のUXC10のProfile試験について、

下記項目でFail、またはINDCSVとなっております。

別のPTSバージョン(8.8.1)で確認しましたが、同様の結果となっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

喩さんにも確認いただきましたが、恐らくDUT側の信号が正しくないと予想しており、デバック依頼が必要かと思います。

Logを添付いたしますので、お手数ですが酒井さんにもご確認いただき、ご意見いただけないでしょうか。

ALAP_Profile.zip

また、以下の試験ではPTSバージョン8.8.1でPASSとなりました。

念のためご報告いたします。

・IOPT/SR/COD/[ID]

[ID]/FAIL　8.8.1/PASS

よろしくお願いいたします。

中山光祐
