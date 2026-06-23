# thread_0203: [内部連絡] Re: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

- Message count: 7
- Source JSON: `thread_0203.json`

---

## 1. 2025-10-31 01:51

**From:** Itsuo Sakai
**To:** Hsiaoting Huang

王さんお疲れさまです。

ALAP社HM26の試験の際に王さんがQ社アカウントを取得したと記憶していますがいかがでしょうか？

酒井差出人: Shuhei Umeda

送信日時: 2025年10月31日 10:44

宛先: Hsiaoting Huang ; Shigeyuki Sakai

件名: RE: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

アリオンジェシー様/望月様お世話になっております。アルプスアルパインの梅田です。

ご確認いただきましてありがとうございました。
Step 7: Run QUTS Status App」と記載されていますが、ラボにQUTS Status Appがないため、貴社に確認したところ、QRCTでもQUTSの確認が可能とのことでした。
そのため、本日はQRCTを使用してBLE DTMモードへの移行を試しました。

誤解を招いてしまったかもしれません。

QRCTでQUTSの確認はできません。

QRCTがインストールされているのであれば、QUTSも一緒にインストールされているのではないか、との推測になります。

Qualcomm社のダウンローダー上、QUTSがQRCTにも含まれるような構成になっているためです。

お手数でございますが、再度、以下のPathにQUTSStatusApp.exeがあるかどうかご確認いただけますでしょうか？

C:\Program Files (x86)\Qualcomm\QUTSStatusApp\QUTSStatusApp.exe

もし存在しない場合、QUTSStatusAppの御社への提供方法を検討いたします。

ただ、QRCTをお持ちであるということは、何らかの方法でQRCTをインストールされたと思いますが、

御社がQualcomm IDをお持ちでないのは確かでしょうか？

基本的にQualcommのツールは起動時にネットワークを経由して、Qualcommサーバーと何らかの認証を行っていると思います。

QRCTが使えているので、その認証はPassしていることになります。

使用中のQRCTのバージョンについて教えていただけますでしょうか。

また、御社とQualcommとの間に契約関係はございますでしょうか？

以上、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 5:14 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様お世話になっております。

アリオンのジェシーです。

ご返信ありがとうございます。

＞現在実施しようとしている試験は、Bluetooth Measurementでしょうか、それともBLE Measurementでしょうか？

現在実施しようとしている試験はBLE Measurement ([ID])です。

また、ラボに確認したところ、Bluetooth Measurement (RF)試験は既に実施完了しまして、テストレポートも先日提出させていただきました。

＞手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

BLE Measurementについては、Step ６マクロの実施（uxc_BLE_FTM_Mode.ttl）まで成功しました。

Step 7: Run QUTS Status App」と記載されていますが、ラボにQUTS Status Appがないため、貴社に確認したところ、QRCTでもQUTSの確認が可能とのことでした。

そのため、本日はQRCTを使用してBLE DTMモードへの移行を試しました。

但し、BLE Measurementの測定手順ではQUTS Status Appでの設定方法が指定されているため、QRCTの画面上でどのように設定してBLE DTMモードへ移行すればよいのかが分かりませんでした。そのため、本日再度お問い合わせさせていただきました。

大変恐縮ですが、現状（QUTS Status App無し）でBLE DTMモードへの移行方法があればお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shuhei Umeda

Sent: Thursday, October 30, 2025 4:28 PM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオンジェシー様お世話になっております。アルプスアルパインの梅田です。

望月様の代理でのご確認ありがとうございます。

Qualcomm IDはお持ちでは無いが、QRCTのインストールはできた、またはQRCTは既にお持ちだったということでしょうか。

QRCTの画面を添付いただきましたので、QRCTが動いている前提でお話しますが、

添付しました資料は既に展開させていただいているQRCTの動作手順書です。

現在実施しようとしている試験は、Bluetooth Measurementでしょうか、それともBLE Measurementでしょうか？

手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

お手数ですが、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 4:09 PM

To: 酒井重之 Shigeyuki Sakai ;
梅田修平 Shuhei Umeda

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様、酒井様、

お世話になっております。

アリオンのジェシーです。

ご不便をお掛けして申し訳ございません。

本日望月が社内不在のため、代理にてラボのフィードバックをご連絡いたします。

＞【BLE】

＞御社にて Qualcomm からツールを直接入手することは可能でしょうか？

申し訳ございません。内部で確認したところ、弊社はQualcomm IDを持っていないため、Qualcommからツールを直接入手できないです。

メールでご提示いただいた方法（QRCTの利用）を試しましたが、接続に失敗しました。添付のScreenshotをご参照ください。

確認したところ、USBケーブルで制御用PCに接続していますが、PC側でUSBデバイスとして認識されていません。

また、USB Driver.exeはQRCTフォルダ内に存在しないようです。

念のため、「Select USB Driver.exe」ボタンをクリックし、QC.BluetoothLE_DirectMode.exeを選択して接続を試みましたが、Failed device connectionと表示されました。

ご確認いただき、QRCTでDTMモードへ移行する手順をお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shigeyuki Sakai

Sent: Monday, October 27, 2025 1:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

本日、梅田が不在ですので、私からご回答します。

【IOPT】

添付のファイルが過去に Volvo から提供されていたのですが、御社へ提出していなかったと思います。申し訳ありません。

“adb install BlueSPP.apk”

については、 PDF の 3 ページ目に記載されております。

一度ご確認いただけますでしょうか。

【BLE】

御社にて Qualcomm からツールを直接入手することは可能でしょうか？

通常ですと QPM(Qualcomm Package Manager) というツール経由で PC にインストールします。

（そのためツールインストーラーをお渡しすることができないことも背景です）

QUTS は下記 QRCT をインストールすることで一緒に導入されます。

QRCT は Classic の試験でご使用いただいたと思いますので、 QUTS もご確認可能ではと思います。

一度ご確認いただけますでしょうか。

なお、 BLE 試験用にご提供しました手順書の &quot;Notes
on QRCT tools&quot; シートに QRCT のインストールの説明を記載しておりますので、合わせてご確認をお願いいたします。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:31 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

RF-PHY試験に関して、メールでいただいているQUTS Status Appと Run Bluetooth LE Direct Modeテストツールがまだご提供いただいていないようです。

ご確認の上、ご提供お願いできますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:07 AM

To: Shuhei Umeda ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

10月21日19:42の梅田様からのメールでは、「IOPTTestguide.pdfに記載されているBlueSPP.apkをインストール」という記述がありますが、

こちらで探しておりますが、これら資料をいただいていないようです。

もしお送りいただいているようでしたら、そのメールご送付の日時をお知らせいただけますでしょうか。

またIOPTTestguide.pdf以外にも関連する試験で必要なファイルがございましたら併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 7:29 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

まずはadbが正常に動作できるようになったとのこと承知いたしました。

こちらかの情報に誤りがありまして申し訳ございませんでした。

また、SPPの再試験ありがとうございました。

結果を再度V社と共有いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 7:02 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

&quot;USB-A 2.0&quot;というラベルの付いたケーブルを使用したところ、adb install はできましたが、

再度SPPのプロファイル試験を実行しましたが、結果は以前と同じでした。

logのファイルを添付いたしますので、ご確認いただけないでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 10:39 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様ご確認いただきありがとうございました。

こちらのケーブルになります。

このケーブル経由でadb関連のコマンド操作を試してみていただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 9:51 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

添付のケーブルがございましたが、こちらのことでよろしいでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 7:08 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

何度もご確認いただきましてありがとうございます。

再度、PCとDUTの接続方法を確認させてください。

弊社から送付したDUTですが、USBケーブルが4本あったと思います。

DEBUG SAIL

DEBUG HKP

DEBUG MD

以外のもう1本のケーブルはございますでしょうか？もしよろしければ写真を撮って送っていただけると助かります。

DEBUG MDとご案内いたしましたが、残りの1本がDUT側のUSB機能として使うもので、

こちらのケーブルでないとadbが動作しない可能性がございます。

お手数をおかけいたしますが、4本目のケーブルのご確認をお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

お送りいただきました資料を確認し、adb shell settings put global development_settings_enabled 1&quot;コマンドを送りましたが、以下のエラーが表示されます。

• error: no devices/emulators found

DUTやPCなどで、他に確認すべき点や、設定すべき点がございましたら、ご教示いただけますでしょうか。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 1:19 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

添付ファイルのP.2にBasic DUT operationsが記載されておりますが、

Developer ModeはEnableになっていますでしょうか？

adb shell settings put global development_settings_enabled 1

を実行してから

adb install bluespp.apk

を試してみていただけますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 12:55 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡いただきました&quot;DEBUG MD&quot;のUSBケーブルをPCに接続し、&quot;adb install bluespp.apk&quot;を実行したところ、下記のエラーが表示されました。

• adb: connect error for write: no devices/emulator found

また、&quot;adb devices&quot;コマンドを実行いたしましたが、&quot;List of attached devices&quot;の下に何も表示されず、認識されていないようです。

PCやDUTで、他に設定する所などがございましたら、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 11:53 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご確認ありがとうございます。

DEBUG MDとPCを接続してください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 11:51 AM

To: Itsuo Sakai ;
梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は不在といたしまして申し訳ございません。

以下確認事項がございますので、

ご回答いただけますでしょうか。

BlueSPP.apk をインストールするには、 DUT の下記の 3 本の USB ケーブルのどれを PC に接続すればよいかご教示ください。

DEBUG SAIL
DEBUG HKP
DEBUG MD

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 5:25 PM

To: Shuhei Umeda ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
Connection Diagram ですが、 RF
PHY Test System を追記したものを準備いたしました。
こちらを参照いただけたらと思います。

⇒ 何度もお手数をお掛けしました。これで RF
PHY 試験の接続系統図が明確になりました。ありがとうございました。

引き続きよろしくお願いいたします。

酒井差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 16:00

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様

Connection Diagramですが、RF PHY Test Systemを追記したものを準備いたしました。

こちらを参照いただけたらと思います。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, October 21, 2025 2:33 PM

To: 'Itsuo Sakai' ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

Operation ManualですがPDFに変換しました。

こちらをご参照ください。
RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。

使用いたします。

添付のBluetooth measurement procedure.pdf、BLE measurement procedure.pdf を参照ください。

操作手順の中にEthernetに関する操作がございます。
ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の
USB 接続部分は反映されていないという理解で間違いないでしょうか。

おっしゃるとおりです。Bluetooth Connection Diagramに反映されておりません。
そうあれば私の最初からの質問であるテストシステムの Serial
over USB
の接続先ですが、それは PC
running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

はい。その理解で合っています。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 1:43 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
RF PHY Test System との接続は以下の図をご参照ください。
DUT と PC
running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。
RF PHY Test System と DUT は RF のみ接続します。

⇒ RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。
そして PC running QDART と RF
PHY Test System は直接 RS232、 GPIB での接続となります。

⇒ HM26 でも同じ図の Q 社マニュアルを使いました。しかし、 DTM モードでは GPIB 経由のコマンドの定義はなく、 Serial
over USB を含む Serial

(UART) 経由でのコマンドが定義されそれに従って DUT を制御しています。

このため DUT と PC および RF
PHY テストシステムは下図のような接続系統図となります。

ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の

USB 接続部分は反映されていないという理解で間違いないでしょうか。

そうあれば私の最初からの質問であるテストシステムの Serial over USB

の接続先ですが、それは PC running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

以上ご確認をお願いします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 12:55

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

RF PHY Test Systemとの接続は以下の図をご参照ください。

DUTとPC running QDART間はUSB conversion harnessを使ってUSB Serialで接続いたします。

RF PHY Test SystemとDUTはRFのみ接続します。

そしてPC running QDARTとRF PHY Test Systemは直接RS232、GPIBでの接続となります。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 12:01 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

ご返信ありがとうございます。
制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。
ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

⇒ 図では黄色マーカー部分の一端が PC,
他端が DUT ですが、文面から推測すると下図かと思われますが、正しいでしょうか ?

以上よろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 11:40

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。
以上のようにご送付いただいた Connection
Diagram では RF PHY の
DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。

制御結線についてですが、RFテストシステム-DUT間の結線は以下の画像の黄色マーカー部分になります。

ちょうどご質問をいただいたUSB conversion harness-USB Type-Aケーブルの部分です。

DUT – USB conversion harness – USB Type-Aケーブル – PC で結線され、USB SerialとしてPCとDUT間の通信が可能となります。

後ほど、Operation ManualをPDF化して送付するようにいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, October 20, 2025 7:19 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

先程の質問は私の Excel のバージョンが古いせいか以下の図が表示されたためで、「薄緑線の分岐」とか「薄緑線の上方の接続先」が何のことやらと思われたと思います。お詫びします。

しかし、 RF PHY 試験は認証テストシステム及び簡易なアンリツ

BT テスタでも RF 測定系とは別に、 UART/COM ポート接続が必須で、

HM26 でも下図のように外部 PC ＋ Q 社テストアプリを Bridge にして

DUT<->(Eternet)<->PC<->(Serial over USB)<->RF PHY テスターという接続を行いました。その際の DTM モードマニュアルを添付します。

以上のようにご送付いただいた Connection Diagram では RF
PHY の

DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。ご送付の Connection Diagram はおそらく電波法 /FCC 試験時のオープンループ試験用のものと推測されます。再度 DTM モードのセットアップ方法をご確認ください。

以上よろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 20 日 18:35

宛先 : Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様

SPPのレポートの送付ありがとうございました。

内容確認して返信いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 6:17 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

SPPのレポートをお送りいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Monday, October 20, 2025 5:16 PM

To: Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPTの再試験の実施ありがとうございました。

SPPについてですが、再試験結果のレポートを送付いただくこと可能でしょうか。

V社側に連絡して事前条件やSWの差分の有無について確認を依頼したいと思います。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 5:12 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

IOPT試験について連絡です。

御社からご送付いただいたSPPのPTSレポートと同じICS設定であることを確認してv8.10.2で再試験を実施しましたところ、MAPとPBAPはPass

しましたがSPPはPassしませんでした。

SPPのPTS試験では、スタート前にDUTの接続済機器一覧からPTSを削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいたPassレポートを得られたDUTのSWが当社のDUT

のSWから更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいたSPPのPTSレポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 20, 2025 1:36 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご返却、どうもありがとうございました。

弊社側での内部データ更新が完了しまして、先ほど望月様宛での発送手続きが完了したところです。

ヤマトお問合せ No : [ID]

併せて、 RF PHY 試験の手順書もお送りします。

ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 1:40 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

承知いたしました。

更新いただいた後、RF PHY試験の日本分実施後、台湾での試験向けに発送予定です。

その際に該否判定書と製品仕様書が必要になります。

今回はRF試験についてはモニタ部分については輸出は必要なかったとおもいます。

また、先日お伝えいたしました、プロファイル（IOPT）試験についてのご修正についてもそちらのサンプルの返送が必要でしたらおしらせください。

以下RF試験機の返送になります。

運送会社：佐川急便お問い合わせ送り状No.[ID]

酒井様宛て一個口引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, October 15, 2025 12:56 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

＞ 御社へ一旦サンプルをお返しするという事だったと存じます。

はい、お手数おかけしまして申し訳ありませんが、そのように進めさせてください。

RF 試験用のサンプルは以下の写真が示す DUT のみで大丈夫です。

ご返却の宛先は私でお願いいたします。

福島県いわき市好間工業団地 20-1

アルプスアルパイン株式会社 DC1 設計部酒井重之あと、 BLE
オプション機能の試験のため DUT を台湾に発送されると思いますが、弊社から該非見解書をお出しするということでよろしいでしょうか。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 6:28 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

RF試験が完了いたしましたが、RF PHY試験実施のため御社へ一旦サンプルをお返しするという事だったと存じます。

RF試験用のサンプルですが、Fullセットでお返ししたほうがよろしいでしょうか。

必要な物のみでよろしければご指定いただければそちらのみお返しいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, October 14, 2025 9:52 AM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきありがとうございました。

RF試験が合格完了とのこと承知いたしました。

引き続き、RF PHYの実施、よろしくお願いいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Friday, October 10, 2025 7:35 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様、酒井様アリオンの酒井です。いつもお世話になっております。

望月に変わり私からお知らせします。

先程 RF 試験が合格完了しましたのでお知らせします。来週 RF
PHY(1M)

を実施し、 Pass 後に台湾ラボへ送って (2M,
Coded) を実施する予定です。

引き続きよろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 10 日 17:38

宛先 : Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

酒井に代わりまして本件返信させていただきます。

まず試験日程のイメージの共有ありがとうございました。

おおよそこれぐらいの日程感で試験が進むこと承知いたしました。

次に、Bluetooth IOPT試験の結果のご連絡ありがとうございました。

Fail、INDCSVとなった項目についてレポート内容を確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 4:49 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

今回のケースで問題なく試験が進んだ場合は以下の様な時間的イメージとなります。（日本分のみ）

RF：4日程度

[ID]：3日程度

Profile：2日程度状況により途中中断、問題箇所再確認などで時間は大きく変化する場合があります。

ご了承ください。

Bluetooth IOPT試験について以下エンジニアから報告がございます。

★ALAP(UXC10)のIOPT試験で18項目中14項目はPassしました。

残る下記項目がFail、またはINDCSVとなっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

上記のPTSレポート(ログ付)を添付しますので、ご確認および解析をお願いします。特に製品のSDPレコード内容を重点的にご確認ください。

PTSのIXITの設定で対処できるものはその旨お知しらせください。FW改修が必要な場合は改修FWをご準備ください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 2:20 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご確認どうもありがとうございました。

各試験の想定日数を教えていただく事は可能でしょうか。

問題発生により変化することも承知しておりますので、特に問題無く進んだ場合の日程感で構わないです。

RF ・・・

RF PHY ・・・

IOPT ・・・

RF PHY 試験前の DUT 更新時期や、 IOPT 試験後ディスプレイご返却のタイミングを知っておきたいためです。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 2:08 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

QUESTIONNAIRSの方、受け取っております。

RF PHY試験の方のテストプランも作成いたしました。

DUTサンプルの運用につきましてはご希望通り対応予定です。

何かございましたら改めて連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 1:57 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご確認、どうもありがとうございました。

試験のご対応を引き続きよろしくお願いいたします。

別メールにしてしまいすみませんでしたが、

Questionnaire の更新と DUT 更新対応のご相談をご連絡しておりますので、

そちらもご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 1:10 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

お待たせしております。

その後こちらで試行いたしまして、RF試験開始の段階まで進めることができたようです。

ＲＦ試験実施の上何かございましたら随時連絡いたしますのでしばらくお待ちください。

また、ＩＯＰＴ試験の方も動作確認いたしました。

特にこちらも問題ないようです。

取り急ぎ連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, October 9, 2025 6:58 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご指示有難うございます。

昨日連絡いたしましたDUTの通信接続ができない問題について、

電流の制限を調整したところその部分につきましては正常に動作することが確認できました。

ただ、その先で確認を要する状況となっておりますので、もう少しはっきりしましたら改めて連絡いたしますので、もうしばらくお待ちいただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Thursday, October 9, 2025 3:18 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

弊社での似た過去事例にもとづき、少しご確認お願いしたい点がございます。

·
Wake_up 端子の GND 接続確認

DUT の Wake_up ラインが電源の GND に接続されていることをご確認お願いします。

接続が外れると DUT が Sleep 動作に入る動きをしますため。

·
電源投入後、 30 秒待機電源投入後、ソフト起動に 30 秒程度時間がかかりますので、それを待ったのち、操作を開始してみていただけますでしょうか。

以上、２点のご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 6:01 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

RF 試験のDUT Settingで以下の現象が起きております。

・「(UXC)AT operation manual_for_BT_rev001.xlsx」内の手順５実施後、「root@lemans:~#」が表示されず、通信接続ができません。

TeraTermは最新バージョン(5.5.0)を使用しております。

TeraTermを別のバージョン(5.4.1)で確認しましたが、同様の現象が起こります。

手順5実施中にも切断されることがあります。

こちら対策をご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 5:54 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

★ RF PHY は確認中で未記入項目があって Test
Plan は作成できません。

QUESTIONNAIREの未記入（TBD）の項目のご確認状況はいかがでしょうか。

★サンプルは本日到着し、セッティング、動作確認を行っております。

確認結果わかりましたら連絡しますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 9:11 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様立て続けて申し訳ございません。

RF 試験の DUT 操作マニュアルおよび TeraTerm 用マクロを提出します。

ご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 2:54 PM

To: 'Toshitaka Mochizuki'

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

以下、トピックごとにご連絡いたします。

■ DUT list について間違い修正や写真追加等で更新しました。

添付しました 2025/10/07 のもので差し替えをお願いいたします。

■ DUT 機材発送について

RF 試験用と IOPT 試験用の DUT 機材を別々に発送しました。

以下、ヤマトの送り状番号です。

■ [ID] について別メールですが質問事項へのご回答、ありがとうございました。

（現在の記述で問題無いと理解いたしました）

■ IOPT 試験用の DUT 操作マニュアルについて添付の AOSP_Bluetooth_User_Manual_1_0_0.pdf が試験用の DUT 操作マニュアルです。

不明点などありましたら、ご連絡お願いいたします。

■ RF 試験用の DUT 操作マニュアルについて明日を目標に、現在準備中です。

整い次第、お送りいたします。

以上、ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 7, 2025 11:06 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ドキュメントのご送付ありがとうございます。

試験サンプルの接続、操作マニュアルのご提供もお待ちしております。

（可能であれば英文、もしくは中文併記でいただけますと助かります。）

引き続きどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 9:24 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご回答ありがとうございます。

送信データ量が大きくなりすみません。

■機材提出票および DUT list

機材提出票を作成いたしました。

RF DUT 一式の方はのちのち台湾に行く予定のため、 IOPT DUT とは別で扱えた方が好ましいと思いましたため、そのようにしました。

また、 WFA メールスレッドの方でありました税関対策の意味も込めて DUT
list を作成しました。 RF DUT の接続写真はのちほど載せるようにします。

お気づきの点等ございましたらご連絡ください。

■ [ID]

こちらも作成いたしました。

下記のご確認をよろしくお願いいたします。

Antenna だけの値を持っていないことから、 Cable Loss も含めた値となります。こちらで構いませんでしょうか？

このケーブルは、製品のアンテナケーブル or 測定用ケーブルどちらになりますでしょうか？添付ファイルには、一旦、測定用ケーブルのロスを書いています。

BLE の試験モード検討中のため、今時点 TBD とさせてください。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 6:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

＞・ RF試験とIOPT試験用に、DUT一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

★管理を共通にしてよいのであれば、最終的なご提供物を１冊にまとめていただいても問題ございません。必ず数量、それぞれの識別が出来るようにサンプル本体や付属品にラベルなどを貼ってください。

＞・ IOPT試験はQuestionnaireはございますか？

★こちらICSを既にいただいているので特にQuestionnaireは必要ございません。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 4:54 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご指示ありがとうございます。

以下、確認させてください。

·
RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

·
IOPT 試験は Questionnaire はございますか？

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 11:47 AM

To: Misumi Sato ;
酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

先週はお打ち合わせありがとうございました。

Wi-Fiと一旦メールを分けさせていただきます。

Bluetoothサンプルの送り先ですが、当社日本ラボは本メールのフッタにございます望月宛にお送りください。

また、その際には添付の機材提出票をお送りください。

またRF テストプラン作成のため、添付のQUESTIONNAIRSにご記入の上、ご返送いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Misumi Sato

Sent: Friday, October 3, 2025 4:06 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

こちらこそ早速発送手続き着手していただきありがとうございます。

ご発送準備整いましたら、追跡番号とインボイスをご提供いただけますと幸いです。

尚、以前貴社の別部隊のWFA認証試験をご担当させていただいた際台湾から日本へのDUT返送時に、税関から再輸入免税措置を求められた経験がございます。

その際、製品個々のシリアルナンバーが必要だったため、念のため、DUT本体や

Wi-Fiアンテナ等にシリアルナンバーをご設定いただくことをお勧めいたします。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 3:51 PM

To: Misumi Sato ;
Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について佐藤様お世話になります。

アルプスアルパイン酒井です。

早速のご回答、どうもありがとうございます。

来週早々に発送手続き着手する予定です。

よろしくお願いいたします。

酒井

From: Misumi Sato

Sent: Friday, October 3, 2025 3:05 PM

To: 酒井重之 Shigeyuki Sakai ;
Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

午前中の会議ではありがとうございました。

横から失礼いたします。

WFA試験のDUTの送付先ですが、下記の表に記載させていただきましたので、ご参照お願いいたします。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

追跡番号、インボイスをご連絡その他、何かWFA試験に関すること、および輸送に関するご質問等ございましたら、お気軽にお問い合わせくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 2:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

PCAT のご確認ありがとうございました。

この内容を踏まえまして、弊社側でどう対応するか確認いたします。

機材の発送について、

·
下記の通り、弊社から送る際の送付先を教えていただけますでしょうか。（間違い等ありましたら修正をお願いいたします）

·
該非判定見解書等の時間かかるものは着手開始したいと思いますので、対応必要事項欄に追記していただけますでしょうか。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

追跡番号、インボイスをご連絡よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, October 3, 2025 12:16 PM

To: 酒井重之 Shigeyuki Sakai ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

Subject: Re: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

会議資料の更新＆共有させていただき、ありがとうございます。

PCATに関して台湾ラボがHM26のWi-Fi認証試験で利用実績がございます。

ただ、御社別部隊から異なる案件への対応として、

今回V社様案件で使用してよいか、バージョンの指定がないか、

使用できない場合、御社からご提供いただけるか、

ご確認いただきますよう、お願いいたします。

※ HM26の案件で使用したPCATのバージョン：[ID]

よろしくお願いいたします。

Outlook
for Android を取得差出人: Shigeyuki Sakai

送信日時: 金曜日, 10月 3, 2025 10:59:20 午前宛先: Jun Wang ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

件名: RE: 【ALAP】[UXC] Wi-Fi Alliance認証計画について各位本日は、打合せをどうもありがとうございました。

更新した資料をお送りします。

‘QA’ シートに、★マーク付きで確認必要事項を書いております。

試験のご対応、引き続きどうぞよろしくお願いいたします。

酒井

-----Original Appointment-----

From: Jun Wang

Sent: Thursday, October 2, 2025 1:10 PM

To: Jun Wang; 酒井重之 Shigeyuki Sakai; Toshitaka Mochizuki; Itsuo Sakai

Subject: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について

When: 2025 年 10 月 3 日金曜日 9:30-10:30
(UTC+09:00) 大阪、札幌、東京

Where: Microsoft Teams 会議アルプスアルパイン酒井様こちらから設定して申し訳ございません。

明日の打ち合わせは少し早めに開始して、09:30からでお願いいたします。

時間帯を09:30～10:30に修正し、会議案内を再送いたします。

宜しくお願いいたします。

アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

弊社側関係者に確認いたしまして、下記時間帯でお願いいたします。

10/3（金）　10:00～11:00

会議リンクは下記ご参照願います。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
489 106 497 201 8

パスコード :
sR6yD26r

開催者向け :
会議オプション

________________________________________________________________________________

_____________________________________________

From: Jun Wang

Sent: Thursday, October 2, 2025 10:06 AM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

空き時間帯の共有ありがとうございます。

本日は酒井様のお時間が概ね埋まっているようで、

弊社関係者と一旦明日で調整させていただきます。

調整つき次第ご連絡いたしますので少しお待ちください。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Thursday, October 2, 2025 8:42 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご承諾ありがとうございます。

以下に私のカレンダーを貼りました。この白い時間帯でお願いできましたら助かります。

また、時間は 30 分を見込みますが、延長用に 1 時間スロットを頂けたら助かります。

ご確認をよろしくお願いいたします。

＜１０月＞

酒井

From: Jun Wang

Sent: Thursday, October 2, 2025 7:26 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi認証のPre-testの正式見積書について、

承知いたしました、ご用意いたします。

機材送付の段取りについての打ち合わせですが、

弊社側関係者に確認いたしますが、

予め酒井様のご都合をお伺いしてもよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, October 1, 2025 6:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご提案どうもありがとうございました。

【アルプスアルパイン様】 V 社 UXC10 の Wi-Fi 認証につきプリテストのご提案 _Update_1001.pdf の内容でお見積書をいただけますでしょうか。

あと、 BT SIG 試験と WFA 試験の DUT 機材発送段取りを考えておりますが、

機材の保管場所がいわきと中国大連に分かれている背景や、少し悩んでいる点があります。（添付ファイル）

この内容を一度打合せさせていただけませんでしょうか。

可能でしたら、打合せの候補日をいただきたいです。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, October 1, 2025 10:59 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10のWi-Fi Pre-testの部分試験に関して、

提案資料のP5に追加いたしました。

基本は本番試験の各対象Programに関して、WFAのTest Planより一部抽出して試験を行う考えです。

ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, September 30, 2025 9:40 AM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

早速ご確認いただきありがとうございます。

部分試験のブレークダウン、

なるべく早めにご報告するように調整してまいりますので、

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Tuesday, September 30, 2025 9:11 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

内容確認しまして、とても良い内容だと考えております。

ご提案どうもありがとうございます。

試験項目ブレークダウンお待ちしております。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Tuesday, September 30, 2025 6:46 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

お待たせいたしました。

UXC10のWi-Fi認証試験をスムーズに進めることができ、

そして目標時期までに認証取得できるように、

プレテストのご提案をいたします。※添付ご参照願います。

部分試験に関して、もう少し試験項目のブレークダウンについてラボと相談しておりまして、もう少しお待ちいただきますと幸いです。

ご検討賜りますようお願いいいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Monday, September 29, 2025 4:38 PM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi認証に向けてのPre-testに関して、酒井様のご要望を基に、

ラボと提案内容について相談しております。

本日は台湾がお休みをいただいておりまして、先週末時点の概案を展開いたします。

本日の遅い時間帯になりますが、もう暫くお待ちいただきますようお願いいたします。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 29, 2025 10:34 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

Pre-test のご検討の状況はいかがでしょうか。

状況を教えていただけると助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 24, 2025 4:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10のWi-Fi認証試験につき、Pre-testのご相談ありがとうございます。

酒井様のお考えをラボに展開いたしまして、

Pre-testへの期待や目的は理解いたしました。

いただいた資料を基に、Pre-test向けのTest Planをご用意いたします。

目標として、9/26（金）までにお送りいたしますので、

少々お待ちいただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 24, 2025 11:39 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

打合せありがとうございました。

私が考えております Pre check の進め方のメモ書きを添付します。

なるべく無駄なく効果的に check を行っていきたいと思っています。

御社でのご経験踏まえて、、 check 実施項目のご提案等いただけますと、大変助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Saturday, September 20, 2025 9:25 AM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

補足説明ありがとうございます。

Wi-Fi認証試験はユーザー立場で、WFAが決めたGoldenSampleとの接続性の確認が多く、

御社でWFAが定めた試験環境でなくても、ユーザー視点で

Wi-Fiの機能確認はできるのではと考えます。

最新の日程表から、御社でSWの確認も行っているようですが、

その状況を参考に、弊社ラボでの事前確認プランを立てようと考えますが、

いかがでしょうか。

宜しくお願いいたしますアリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 6:45 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

私の言葉の選び方が良くなかったです。

「UXC10のSWが不安定」ではなく、「UXC10のSWの品質レベルが不明なので不安」が正しいです。

弊社もV社もWFAテストをする環境を保持しておらず、どの程度 WFAテストできる品質レベルなのか分かっておりません。

従いまして、Pre Testでは、WFAテストできるレベルなのか確認したいです。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 19, 2025 5:32 PM

To: 水野淳也 Junya Mizuno

Subject: Re: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC10のSWが不安定との事ですが、

Labから具体的な症状を確認されております。

例、〇〇操作する時に〇〇不安定の症状がある、〇〇の際に良くリブートかかったりする、等差支えの無い程度でお願いできますと助かります。

よろしくお願い致します。

Outlook
for Android を取得差出人: Jun Wang

送信日時: 金曜日, 9月 19, 2025 2:38:00 午後宛先: Junya Mizuno

件名: RE: 【ALAP】[UXC] Wi-Fi Alliance認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

承知いたしました。

9/22（月）にLabとの相談状況をご報告いたします。

具体的な提案ができるように調整してまいります。

最新日程を踏まえた進め方のすり合わせですが、

9/24（水）09:00～10:00、 でお願いいたします。

弊社の酒井と王君、2名で参加させていただきます。

よろしければこちらでTeams会議を設定いたしますが、

御社の参加者をお伺いしてよろしいでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 11:01 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

もしも可能であれば、9/22(月)までにご回答もしくは状況のご連絡をいただくことは可能でしょうか？

V社側のSWリリース遅延およびソフト品塾度が問題ではありますが、弊社からV社に具体的なプランを早急に提示、説明していく必要がある状況です。

また、今日中に提示予定の新しい開発日程を基に、一度 BT-SIGとWFAの進め方のすり合わせを再度させていただくことは可能でしょうか？(最大で1時間程度を想定しています)

来週の火曜日は御社はお休みと思いますので(弊社は勤務日です)、来週の月曜日もしくは水曜日の以下どれかの日程でお打ち合わせが可能かご確認をお願いしたいです。

ü
9/22(月) 14:00-15:00

ü
9/24(水) 9:00-10:00

ü
9/24(水) 13:00-15:00

お時間に限りがあれば、V社の次期モデルのBT-SIGとWFA認証についてもお話しさせていただければと考えております。

ご確認をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 11:20 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

相談なので、話してみないとわかりかねますので。

急ぎであれば回答希望納期をいただければそれまでに回答するように調整いたしますが、いかがでしょうか。

SWに関して情報共有させていただきありがとうございます。

今後試験においてFailが出た際のデバッグ作業もV社自力（外部委託？）

で行う予定、承知いたしました。

他社様案件での経験ですが、ソフト完成度が低いと安定的な試験結果を得られず、

トラブルシュートも難航になったり、結果試験期間が倍半年かかった案件もございました。

ということで、弊社としても完成度の高い（量産品同等レベル）製品のご提供をお願いいたしたいです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 7:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

申し訳ございませんが、御社Labにご相談をお願いします。

御社Labより、いつ頃にご回答をいただける予定か、分かっておりましたら教えていただけますか？

今回のV社からリリースされているSWは、WFAテストに対応した素性として受け取っています。

但し、実態を聞くと、V社側でもWFA認証の経験が乏しく、実際にどれだけの品質になっているか(=WFAテストできる状態か)分かっておりません。

V社のSWのバグ修正等は、全てV社で実施します。

弊社側でV社のSWに手を加えることはありません。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 3:26 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記ご相談いただきありがとうございます。

現行SWが不安定な状況にあること、承知いたしました。

ご要望を一度Labに相談いたしますので、

少々お待ちいただきますと幸いです。

参考にさせていただければと存じますが、

今回V社からリリースされるSWは受験用SWでしょうか。

もしくは、Ver0.8（例）として御社にリリースし、その後のバグ修正、完成度アップは御社で行われる、との予定でしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 1:00 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

追加でご相談したいことがあります。

現在、V社よりWFA向けソフトウェアを受領したのですが、完成度に不安がある状況です。

この状態でWFA本試験を開始し、結果として、殆ど何も試験できずに三か月を過ぎてしまうことを恐れています。

従いまして、“WFA本試験を開始できる状態であること”を確認する目的で、事前試験をお願いしたいと考えております。

以下の条件にて、事前試験項目のご提案とお見積りをお願いできないでしょうか？

ü
期間 : 3日～5日

ü
確認したいこと : WFAの基本となるTest ProgramのGeneral部分がPassできること

Ø
Wi-Fi 4 11n、Wi-Fi 5 11ac、Wi-Fi 6 11axの初期に実行されると想定するコマンド受付確認、接続確認、動作確認等が該当すると考えています。

確認したい内容が具体的ではなく、申し訳ございません。

お手数ですが、一度依頼をご確認いただき、不明点等ありましたらご連絡をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Wednesday, September 17, 2025 4:17 PM

To: 'Jun Wang'

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

再提出は必要ですが、現行CIDの内容をLabに確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

承知しました。

その他の問題点含めて、ご確認、整理をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Model Nameは、製品に張り付けされているラベル等に印字されているNameと一致している必要がある、との理解で合っているでしょうか？

上記ご理解があっています。

合っている場合、Model NameはUXC10になります。

同じModel Nameで電波認証等も取得しています。

承知いたしました。確かにBluetoothの見積依頼書でも「UXC10」とご記載されています。

再度Model Nameを変えてV社からSubmitが必要になる認識で合っているでしょうか？

再提出は必要ですが、現行CIDの内容をLabに確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 3:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご指摘ありがとうございます。

Model Nameは、製品に張り付けされているラベル等に印字されているNameと一致している必要がある、との理解で合っているでしょうか？

合っている場合、Model NameはUXC10になります。

同じModel Nameで電波認証等も取得しています。

この場合、再度Model Nameを変えてV社からSubmitが必要になる認識で合っているでしょうか？

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 12:30 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V社UXCのWi-Fi見積依頼書の更新、ありがとうございます。

Model Nameについて確認させていただきます。

SubmitいただいたCID（[ID]）では、 UXC 1.0、となっていますが、

見積依頼書では UXC10 とご記入されています。

正しくは UXC 1.0 でよろしいでしょうか。

※ WFA Certification Systemの画面よりキャプチャ宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 10:58 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

既にメール等でやりとりしており、ご存じの内容と思いますが、

見積書に以下未記載の箇所がありましたので追記しました。

ü
Submission Category(Flex/Quick/Derivative)

ü
CID number

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 3:08 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

見積依頼書の再送、ありがとうございます。

内容を確認させていただきます。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:58 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

本メールに添付しましたのでご確認をお願いします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 1:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V社より見直しした依頼書も入手しましたので送付させていただきます。

添付はついていないようですが、ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:11 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

CID（[ID]）を基にお見積りを進めていただき、ありがとうございます。

後追いですが、V社より見直しした依頼書も入手しましたので送付させていただきます。

前回、依頼書から変更が入っているSupport Function部分を黄色セルにしました。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:11 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

下記ご連絡をいただきありがとうございます。

V社が本日改めてCID（[ID]）をSubmitされたようです、

Submitされた内容から、Certified b/gが入っていなく、

Certified a/ac/N、Certified 6が対応されることを確認できました。

下記ご連絡いただいた内容で御見積書をご用意いたしますので、

更新でき次第の送付で構いません。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Friday, September 12, 2025 7:38 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

申し訳ありません、今しがた、 Volvo からリストの更新に関する情報がありました。

b
と g
が少し古い規格ですので、申請を削除することを考えているそうです。

急ぎ再提出できるよう推進しますので、お見積りはもう少しお待ちいただけますでしょうか。

よろしくお願いいたします。

酒井

From:
水野淳也 Junya Mizuno

Sent: Friday, September 12, 2025 5:52 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご連絡ありがとうございます。

Test Toolにつきましては、スウェーデン現地法人を介してV社より回答を入手できました。

お見積りに影響は無いのかもしれませんが、取り急ぎTest Tool欄を記入したお見積書を送付させていただきます。

週明けのお見積りをお待ちしております。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 4:58 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

来週中の日程更新、お手数かけますが、よろしくお願いいたします。

見積依頼書に関して、test toolは継続してご確認お願いいたします。

いただいた内容を基に見積書をご用意いたしますので、

週明けにお送りいたします。

よろしくお願いいたします。

Outlook
for Android を取得差出人: Junya Mizuno

送信日時: 金曜日, 9月 12, 2025 2:15:31 午後宛先: Jun Wang

件名: RE: [UXC] Wi-Fi Alliance認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お待たせしてしまっており、申し訳ございません。

昨日、V社より弊社のスウェーデン現地法人を介して、SWがリリースされてきました。

従いまして、現時点でのOpen項目は以下の認識です。

1.
V社SWの動作チェック

2.
V社操作マニュアルの内容チェック

3.
V社からのTest toolの回答入手および見積書の再送

3については、V社にPUSHしつつ、残りのOpen項目については確認を進めます。

来週中に現在の状況を基に、新たに認証計画を更新し、ご提出させていただきます。

何がご不明点、お気づきの点等ありましたらご連絡をお願いします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:45 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Ｖ社UXC1.0のWi-Fi認証について、

8/21にV社からSWのリリースが遅れるとご連絡をいただきましたが、

現時点の状況はいかがでしょうか。

ザックリで構いませんので、共有させていただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Monday, September 8, 2025 9:32 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

Test ToolはV社で記入したSupport Functionによって決まる認識の為、

V社にどのTest Toolを使うのか確認を依頼しております。

少々お待ち下さい。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 5, 2025 11:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Wi-Fi認証御見積依頼書のご記入、ありがとうございます。

Test Toolに関して記入されていないようですが、ご確認いただいてよろしいでしょうか。

Row#67～72

For testing

WTS(Wi-Fi Test Suite)

Quick Track Tool

Manual

For throuput

WTS(Wi-Fi Test Suite)

IxChariot

iPerf

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 5, 2025 9:10 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi認証見積依頼確認書」の[Support Function Information]欄に対して、V社から回答を入手しました。

お手数ですが、一度ご確認いただき、何か気になる点等ありましたらご指摘をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:24 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご理解いただきありがとうございます。

お手数かけますが、よろしくお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 2, 2025 1:18 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

ご指摘の点は仰る通りと思います。

改めて、認証する試験は何か、仕様するテストツールは何か、それらをどのように接続し、動作させるのか、を段階的に整理するように依頼します。

その上で不明点がある場合には質問を明確にするように依頼します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 2, 2025 9:09 AM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記打ち合わせのご要望ですが、弊社が認証ラボとして、

UXCの設計開発に携わったことがなく、マニュアル作成の支援や相談はご対応できかねますので、打ち合わせに参加してもあまり意味が無いと存じますが、いかが思いますでしょうか。

WTSやQuickTrackをセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程をStep by Stepで記述すればOK、とは伝えてはいます。

弊社からも同じ説明になりますが、それでも分からない、と言われると困りますね。

実際車のユーザーマニュアルなどの作成経験があるのではと思いますが…

Wi-Fiだけでなく、Bluetooth、USB、CarplayやAndroidAutoの認証につき、

内容やレベルは違いはあれども、「マニュアル」作成もあるでしょう。

どうしてもマニュアルの作成が困難な場合、1つご提案ですが、

接続過程をビデオ撮影してご提供いただくことでいかがでしょうか。

よろしくお願いいたします。

Outlook
for Android を取得差出人: Junya Mizuno

送信日時: 月曜日, 9月 1, 2025 10:09:16 午後宛先: Jun Wang

件名: RE: [UXC] Wi-Fi Alliance認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

WFA試験を受けるために、V社にソフトウェアの操作マニュアルの作成を依頼しております。

ALAPからは以下のような目次を目安に作成依頼をしておりますが、V社側でマニュアル作成経験が無く難航しているそうです。

(WTSやQuickTrackをセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程をStep by Stepで記述すればOK、とは伝えてはいます)

- Connection diagram

- How to bring up DUT and Android

- Wi-Fi Test Suite

Configuration

AP test procedure

STA test procedure

- QuickTrack

Configuration

AP test procedure

STA test procedure

- Also, some shell scripts or supplemental information so that test operator doesn’t have any confusion about set up.

※WTSやQuickTrackのどれを使うのかは並行してVolvoへ確認中ですそのような状況の中、V社からマニュアルの内容についてアリオン様とも打合せをさせて教えてほしい、とリクエストを受けました。

打合せは、何を書けばよいか？のQAになると予想します。

お手数ですが打合せのご対応は可能でしょうか？

可能な場合、9/4(木)もしくは9/8(月)の16:00以降でご都合が良い時間を教えていただけないでしょうか？

※両日共にご都合が悪い場合には、ご都合が良い日時を教えていただけますと幸いです。

弊社もHM26のモデル等で経験はあるものの、UXC担当の私などは実経験がある訳では無い為、

御社から未経験のV社を適切にガイドしていただけると助かります。

ご検討をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 29, 2025 1:59 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご確認ありがとうございます。

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

はい、Powerとは送信パワーのことです。

V社ソフトで試験するにあたり、送信パワーを確認する場合には、何を基準に確認をされるのか把握し、

事前にV社に基準を満たすことを確認する必要があると考えて、質問をさせていただきました。

また、Volvo様よりCID（[ID]）を既にご提出されていますが、

6GHz対応となっているため、修正が必要かと思いますので、

一旦弊社よりReturnしてよろしいでしょうか。

はい、6GHzは未対応になる為、Returnで問題ないと考えています。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 29, 2025 1:22 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

「Wi-Fi認証見積依頼確認書」のご返送はもう少し時間かかる状況、

承知いたしました。

試験項目の中で、Powerの強さを確認する試験項目はあるでしょうか？

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

また、Volvo様よりCID（[ID]）を既にご提出されていますが、

6GHz対応となっているため、修正が必要かと思いますので、

一旦弊社よりReturnしてよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, August 29, 2025 1:07 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi認証見積依頼確認書」の提出が遅れており、申し訳ございません。

V社に[Support Function Information]欄の記入を依頼し、受け取りましたが複数確認事項があり、時間を要しています。

申し訳ございませんがもう少々お待ち下さい。

また、Wi-Fi Alliance認証の試験項目に関して、ご確認したいことがあります。

試験項目の中で、Powerの強さを確認する試験項目はあるでしょうか？

試験準備の際に考慮する必要があるか把握する為、ご確認させて下さい。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 22, 2025 1:55 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

「Wi-Fi認証見積依頼確認書」の提出が遅れており、申し訳ございません。

弊社スウェーデン現法を介してV社に[Support Function Information]欄の記入を依頼しております。

記入が完了できましたら直ぐにご送付させていただきます。

またPre-testのアドバイスについても承知しました。

V社のSWリリース状況を確認する中で、Criticalな部分および Pre-test要否についてもV社含めて確認していくようにします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 22, 2025 10:31 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXCのWi-Fi認証試験用SWのリリースが遅れている状況、承知いたしました。

リリース予定について引き続き更新の方よろしくお願いいたします。

先日のメールでお願いいたしました弊社フォームの「Wi-Fi認証見積依頼確認書」へのご記入ですが、

いつ頃ご送付いただけますでしょうか。

御社フォームのWorkSheetをいただいておりますが、VCC Comment、QC Commentも併記されている中、

最終仕様（認証取得のターゲット仕様）が不明確となっているため、

仕様情報の整理としても、見積依頼書へのご記入をお願いいたします。

Per-testに関して、SWリリース時期が不明となっている中、予定が立てられない状況をよく理解いたしました。

3ヵ月プランの中で試験、問題解析/原因究明、デバッグ、再試験、をやり切るのかなりの負荷となります。

打合せでご説明いたしましたようにPre-testは部分試験の実施も対応可能なので、

Criticalな項目のみの事前試験があればフロントローディングができ、本番試験が効率アップし、

L/O日程の確保に繋がりますので、時間的に全く無理でない限り事前試験をお勧めいたします。

またSWのリリース状況を踏まえてご相談いただければと存じますので、

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 11:07 PM

To: Jun Wang

Subject: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

Wi-Fi Alliance向けSoftwareに関して、V社より最新情報が入りました。

残念なことに、Android V適用に向けた対応が難航しており、弊社へのリリース遅延が発生し、現時点ではいつリリースできるか不明との情報を受けております。

弊社としては、遅くても9月中にV社からSoftwareを受け取れるようにPUSHしている状況です。

上記の状況を踏まえまして、Pre-testを実施する時間が確保できない為、

Pre-testは無しで、三か月パックの中で最初の1.5カ月は試験1回目、後半の1.5カ月でNG修正と試験2回目(NG+関連する試験項目)、といった形で進めたいと考えております。

取り急ぎ、現状と弊社の考えをご連絡させていただきました。

また、Wi-Fi Alliance向けSoftwareリリース日程に関し、進展がありましたら直ぐにご連絡させていただきます。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

---

## 2. 2025-10-31 02:39

**From:** Itsuo Sakai
**To:** Jun Wang , Toshitaka Mochizuki

望月さんお疲れさまです。

昨日の梅田さんメールに以下のように回答してください。

酒井ーーーーもし存在しない場合、QUTSStatusAppの御社への提供方法を検討いたします。
ただ、QRCTをお持ちであるということは、何らかの方法でQRCTをインストールされたと思いますが、御社がQualcomm IDをお持ちでないのは確かでしょうか？
基本的にQualcommのツールは起動時にネットワークを経由して、Qualcommサーバーと何らかの認証を行っていると思います。
QRCTが使えているので、その認証はPassしていることになります。

⇒先のメールでアリオンはQualcomm IDを取得していないとお伝えしましたが御社HM26案件で営業の王がQualcomm IDを取得しておりました。大変失礼しました。
使用中のQRCTのバージョンについて教えていただけますでしょうか。

⇒別途調べてお答えします。

ーーーー差出人: Jun Wang

送信日時: 2025年10月31日 11:06

宛先: Itsuo Sakai ; Hsiaoting Huang

件名: RE: [内部連絡] Re: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

酒井さん

HM26のBluetooth認証試験で、ALAPのSubcontractorとして、

王君名義で申請してQから承認済みです。

メールに追い付いていなくて恐縮ですが、何をすればよろしいでしょうか。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Itsuo Sakai

Sent: Friday, October 31, 2025 10:52 AM

To: Hsiaoting Huang

Subject: [ 内部連絡 ] Re: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

王さんお疲れさまです。

ALAP 社 HM26 の試験の際に王さんが Q 社アカウントを取得したと記憶していますがいかがでしょうか？

酒井差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 31 日 10:44

宛先 : Hsiaoting Huang ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様/望月様お世話になっております。アルプスアルパインの梅田です。

ご確認いただきましてありがとうございました。
Step 7: Run QUTS Status App」と記載されていますが、ラボにQUTS Status Appがないため、貴社に確認したところ、QRCTでもQUTSの確認が可能とのことでした。
そのため、本日はQRCTを使用してBLE DTMモードへの移行を試しました。

誤解を招いてしまったかもしれません。

QRCTでQUTSの確認はできません。

QRCTがインストールされているのであれば、QUTSも一緒にインストールされているのではないか、との推測になります。

Qualcomm社のダウンローダー上、QUTSがQRCTにも含まれるような構成になっているためです。

お手数でございますが、再度、以下のPathにQUTSStatusApp.exeがあるかどうかご確認いただけますでしょうか？

C:\Program Files (x86)\Qualcomm\QUTSStatusApp\QUTSStatusApp.exe

もし存在しない場合、QUTSStatusAppの御社への提供方法を検討いたします。

ただ、QRCTをお持ちであるということは、何らかの方法でQRCTをインストールされたと思いますが、

御社がQualcomm IDをお持ちでないのは確かでしょうか？

基本的にQualcommのツールは起動時にネットワークを経由して、Qualcommサーバーと何らかの認証を行っていると思います。

QRCTが使えているので、その認証はPassしていることになります。

使用中のQRCTのバージョンについて教えていただけますでしょうか。

また、御社とQualcommとの間に契約関係はございますでしょうか？

以上、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 5:14 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様お世話になっております。

アリオンのジェシーです。

ご返信ありがとうございます。

＞現在実施しようとしている試験は、Bluetooth Measurementでしょうか、それともBLE Measurementでしょうか？

現在実施しようとしている試験はBLE Measurement ([ID])です。

また、ラボに確認したところ、Bluetooth Measurement (RF)試験は既に実施完了しまして、テストレポートも先日提出させていただきました。

＞手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

BLE Measurementについては、Step ６マクロの実施（uxc_BLE_FTM_Mode.ttl）まで成功しました。

Step 7: Run QUTS Status App」と記載されていますが、ラボにQUTS Status Appがないため、貴社に確認したところ、QRCTでもQUTSの確認が可能とのことでした。

そのため、本日はQRCTを使用してBLE DTMモードへの移行を試しました。

但し、BLE Measurementの測定手順ではQUTS Status Appでの設定方法が指定されているため、QRCTの画面上でどのように設定してBLE DTMモードへ移行すればよいのかが分かりませんでした。そのため、本日再度お問い合わせさせていただきました。

大変恐縮ですが、現状（QUTS Status App無し）でBLE DTMモードへの移行方法があればお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shuhei Umeda

Sent: Thursday, October 30, 2025 4:28 PM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオンジェシー様お世話になっております。アルプスアルパインの梅田です。

望月様の代理でのご確認ありがとうございます。

Qualcomm IDはお持ちでは無いが、QRCTのインストールはできた、またはQRCTは既にお持ちだったということでしょうか。

QRCTの画面を添付いただきましたので、QRCTが動いている前提でお話しますが、

添付しました資料は既に展開させていただいているQRCTの動作手順書です。

現在実施しようとしている試験は、Bluetooth Measurementでしょうか、それともBLE Measurementでしょうか？

手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

お手数ですが、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 4:09 PM

To: 酒井重之 Shigeyuki Sakai ;
梅田修平 Shuhei Umeda

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様、酒井様、

お世話になっております。

アリオンのジェシーです。

ご不便をお掛けして申し訳ございません。

本日望月が社内不在のため、代理にてラボのフィードバックをご連絡いたします。

＞【BLE】

＞御社にて Qualcomm からツールを直接入手することは可能でしょうか？

申し訳ございません。内部で確認したところ、弊社はQualcomm IDを持っていないため、Qualcommからツールを直接入手できないです。

メールでご提示いただいた方法（QRCTの利用）を試しましたが、接続に失敗しました。添付のScreenshotをご参照ください。

確認したところ、USBケーブルで制御用PCに接続していますが、PC側でUSBデバイスとして認識されていません。

また、USB Driver.exeはQRCTフォルダ内に存在しないようです。

念のため、「Select USB Driver.exe」ボタンをクリックし、QC.BluetoothLE_DirectMode.exeを選択して接続を試みましたが、Failed device connectionと表示されました。

ご確認いただき、QRCTでDTMモードへ移行する手順をお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shigeyuki Sakai

Sent: Monday, October 27, 2025 1:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

本日、梅田が不在ですので、私からご回答します。

【IOPT】

添付のファイルが過去に Volvo から提供されていたのですが、御社へ提出していなかったと思います。申し訳ありません。

“adb install BlueSPP.apk”

については、 PDF の 3 ページ目に記載されております。

一度ご確認いただけますでしょうか。

【BLE】

御社にて Qualcomm からツールを直接入手することは可能でしょうか？

通常ですと QPM(Qualcomm Package Manager) というツール経由で PC にインストールします。

（そのためツールインストーラーをお渡しすることができないことも背景です）

QUTS は下記 QRCT をインストールすることで一緒に導入されます。

QRCT は Classic の試験でご使用いただいたと思いますので、 QUTS もご確認可能ではと思います。

一度ご確認いただけますでしょうか。

なお、 BLE 試験用にご提供しました手順書の &quot;Notes
on QRCT tools&quot; シートに QRCT のインストールの説明を記載しておりますので、合わせてご確認をお願いいたします。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:31 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

RF-PHY試験に関して、メールでいただいているQUTS Status Appと Run Bluetooth LE Direct Modeテストツールがまだご提供いただいていないようです。

ご確認の上、ご提供お願いできますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:07 AM

To: Shuhei Umeda ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

10月21日19:42の梅田様からのメールでは、「IOPTTestguide.pdfに記載されているBlueSPP.apkをインストール」という記述がありますが、

こちらで探しておりますが、これら資料をいただいていないようです。

もしお送りいただいているようでしたら、そのメールご送付の日時をお知らせいただけますでしょうか。

またIOPTTestguide.pdf以外にも関連する試験で必要なファイルがございましたら併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 7:29 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

まずはadbが正常に動作できるようになったとのこと承知いたしました。

こちらかの情報に誤りがありまして申し訳ございませんでした。

また、SPPの再試験ありがとうございました。

結果を再度V社と共有いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 7:02 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

&quot;USB-A 2.0&quot;というラベルの付いたケーブルを使用したところ、adb install はできましたが、

再度SPPのプロファイル試験を実行しましたが、結果は以前と同じでした。

logのファイルを添付いたしますので、ご確認いただけないでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 10:39 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様ご確認いただきありがとうございました。

こちらのケーブルになります。

このケーブル経由でadb関連のコマンド操作を試してみていただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 9:51 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

添付のケーブルがございましたが、こちらのことでよろしいでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 7:08 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

何度もご確認いただきましてありがとうございます。

再度、PCとDUTの接続方法を確認させてください。

弊社から送付したDUTですが、USBケーブルが4本あったと思います。

DEBUG SAIL

DEBUG HKP

DEBUG MD

以外のもう1本のケーブルはございますでしょうか？もしよろしければ写真を撮って送っていただけると助かります。

DEBUG MDとご案内いたしましたが、残りの1本がDUT側のUSB機能として使うもので、

こちらのケーブルでないとadbが動作しない可能性がございます。

お手数をおかけいたしますが、4本目のケーブルのご確認をお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

お送りいただきました資料を確認し、adb shell settings put global development_settings_enabled 1&quot;コマンドを送りましたが、以下のエラーが表示されます。

• error: no devices/emulators found

DUTやPCなどで、他に確認すべき点や、設定すべき点がございましたら、ご教示いただけますでしょうか。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 1:19 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

添付ファイルのP.2にBasic DUT operationsが記載されておりますが、

Developer ModeはEnableになっていますでしょうか？

adb shell settings put global development_settings_enabled 1

を実行してから

adb install bluespp.apk

を試してみていただけますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 12:55 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡いただきました&quot;DEBUG MD&quot;のUSBケーブルをPCに接続し、&quot;adb install bluespp.apk&quot;を実行したところ、下記のエラーが表示されました。

• adb: connect error for write: no devices/emulator found

また、&quot;adb devices&quot;コマンドを実行いたしましたが、&quot;List of attached devices&quot;の下に何も表示されず、認識されていないようです。

PCやDUTで、他に設定する所などがございましたら、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 11:53 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご確認ありがとうございます。

DEBUG MDとPCを接続してください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 11:51 AM

To: Itsuo Sakai ;
梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は不在といたしまして申し訳ございません。

以下確認事項がございますので、

ご回答いただけますでしょうか。

BlueSPP.apk をインストールするには、 DUT の下記の 3 本の USB ケーブルのどれを PC に接続すればよいかご教示ください。

DEBUG SAIL

DEBUG HKP

DEBUG MD

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 5:25 PM

To: Shuhei Umeda ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
Connection Diagram ですが、 RF
PHY Test System を追記したものを準備いたしました。
こちらを参照いただけたらと思います。

⇒ 何度もお手数をお掛けしました。これで RF
PHY 試験の接続系統図が明確になりました。ありがとうございました。

引き続きよろしくお願いいたします。

酒井差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 16:00

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様

Connection Diagramですが、RF PHY Test Systemを追記したものを準備いたしました。

こちらを参照いただけたらと思います。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, October 21, 2025 2:33 PM

To: 'Itsuo Sakai' ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

Operation ManualですがPDFに変換しました。

こちらをご参照ください。
RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。

使用いたします。

添付のBluetooth measurement procedure.pdf、BLE measurement procedure.pdf を参照ください。

操作手順の中にEthernetに関する操作がございます。
ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の
USB 接続部分は反映されていないという理解で間違いないでしょうか。

おっしゃるとおりです。Bluetooth Connection Diagramに反映されておりません。
そうあれば私の最初からの質問であるテストシステムの Serial
over USB
の接続先ですが、それは PC
running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

はい。その理解で合っています。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 1:43 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
RF PHY Test System との接続は以下の図をご参照ください。
DUT と PC
running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。
RF PHY Test System と DUT は RF のみ接続します。

⇒ RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。
そして PC running QDART と RF
PHY Test System は直接 RS232、 GPIB での接続となります。

⇒ HM26 でも同じ図の Q 社マニュアルを使いました。しかし、 DTM モードでは GPIB 経由のコマンドの定義はなく、 Serial
over USB を含む Serial

(UART) 経由でのコマンドが定義されそれに従って DUT を制御しています。

このため DUT と PC および RF
PHY テストシステムは下図のような接続系統図となります。

ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の

USB 接続部分は反映されていないという理解で間違いないでしょうか。

そうあれば私の最初からの質問であるテストシステムの Serial over USB

の接続先ですが、それは PC running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

以上ご確認をお願いします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 12:55

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

RF PHY Test Systemとの接続は以下の図をご参照ください。

DUTとPC running QDART間はUSB conversion harnessを使ってUSB Serialで接続いたします。

RF PHY Test SystemとDUTはRFのみ接続します。

そしてPC running QDARTとRF PHY Test Systemは直接RS232、GPIBでの接続となります。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 12:01 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

ご返信ありがとうございます。
制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。
ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

⇒ 図では黄色マーカー部分の一端が PC,
他端が DUT ですが、文面から推測すると下図かと思われますが、正しいでしょうか ?

以上よろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 11:40

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。
以上のようにご送付いただいた Connection
Diagram では RF PHY の
DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。

制御結線についてですが、RFテストシステム-DUT間の結線は以下の画像の黄色マーカー部分になります。

ちょうどご質問をいただいたUSB conversion harness-USB Type-Aケーブルの部分です。

DUT – USB conversion harness – USB Type-Aケーブル – PC で結線され、USB SerialとしてPCとDUT間の通信が可能となります。

後ほど、Operation ManualをPDF化して送付するようにいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, October 20, 2025 7:19 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

先程の質問は私の Excel のバージョンが古いせいか以下の図が表示されたためで、「薄緑線の分岐」とか「薄緑線の上方の接続先」が何のことやらと思われたと思います。お詫びします。

しかし、 RF PHY 試験は認証テストシステム及び簡易なアンリツ

BT テスタでも RF 測定系とは別に、 UART/COM ポート接続が必須で、

HM26 でも下図のように外部 PC ＋ Q 社テストアプリを Bridge にして

DUT<->(Eternet)<->PC<->(Serial over USB)<->RF PHY テスターという接続を行いました。その際の DTM モードマニュアルを添付します。

以上のようにご送付いただいた Connection Diagram では RF
PHY の

DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。ご送付の Connection Diagram はおそらく電波法 /FCC 試験時のオープンループ試験用のものと推測されます。再度 DTM モードのセットアップ方法をご確認ください。

以上よろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 20 日 18:35

宛先 : Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様

SPPのレポートの送付ありがとうございました。

内容確認して返信いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 6:17 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

SPPのレポートをお送りいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Monday, October 20, 2025 5:16 PM

To: Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPTの再試験の実施ありがとうございました。

SPPについてですが、再試験結果のレポートを送付いただくこと可能でしょうか。

V社側に連絡して事前条件やSWの差分の有無について確認を依頼したいと思います。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 5:12 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

IOPT試験について連絡です。

御社からご送付いただいたSPPのPTSレポートと同じICS設定であることを確認してv8.10.2で再試験を実施しましたところ、MAPとPBAPはPass

しましたがSPPはPassしませんでした。

SPPのPTS試験では、スタート前にDUTの接続済機器一覧からPTSを削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいたPassレポートを得られたDUTのSWが当社のDUT

のSWから更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいたSPPのPTSレポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 20, 2025 1:36 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご返却、どうもありがとうございました。

弊社側での内部データ更新が完了しまして、先ほど望月様宛での発送手続きが完了したところです。

ヤマトお問合せ No : [ID]

併せて、 RF PHY 試験の手順書もお送りします。

ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 1:40 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

承知いたしました。

更新いただいた後、RF PHY試験の日本分実施後、台湾での試験向けに発送予定です。

その際に該否判定書と製品仕様書が必要になります。

今回はRF試験についてはモニタ部分については輸出は必要なかったとおもいます。

また、先日お伝えいたしました、プロファイル（IOPT）試験についてのご修正についてもそちらのサンプルの返送が必要でしたらおしらせください。

以下RF試験機の返送になります。

運送会社：佐川急便お問い合わせ送り状No.[ID]

酒井様宛て一個口引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, October 15, 2025 12:56 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

＞ 御社へ一旦サンプルをお返しするという事だったと存じます。

はい、お手数おかけしまして申し訳ありませんが、そのように進めさせてください。

RF 試験用のサンプルは以下の写真が示す DUT のみで大丈夫です。

ご返却の宛先は私でお願いいたします。

福島県いわき市好間工業団地 20-1

アルプスアルパイン株式会社 DC1 設計部酒井重之あと、 BLE
オプション機能の試験のため DUT を台湾に発送されると思いますが、弊社から該非見解書をお出しするということでよろしいでしょうか。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 6:28 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

RF試験が完了いたしましたが、RF PHY試験実施のため御社へ一旦サンプルをお返しするという事だったと存じます。

RF試験用のサンプルですが、Fullセットでお返ししたほうがよろしいでしょうか。

必要な物のみでよろしければご指定いただければそちらのみお返しいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, October 14, 2025 9:52 AM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきありがとうございました。

RF試験が合格完了とのこと承知いたしました。

引き続き、RF PHYの実施、よろしくお願いいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Friday, October 10, 2025 7:35 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様、酒井様アリオンの酒井です。いつもお世話になっております。

望月に変わり私からお知らせします。

先程 RF 試験が合格完了しましたのでお知らせします。来週 RF
PHY(1M)

を実施し、 Pass 後に台湾ラボへ送って (2M,
Coded) を実施する予定です。

引き続きよろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 10 日 17:38

宛先 : Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

酒井に代わりまして本件返信させていただきます。

まず試験日程のイメージの共有ありがとうございました。

おおよそこれぐらいの日程感で試験が進むこと承知いたしました。

次に、Bluetooth IOPT試験の結果のご連絡ありがとうございました。

Fail、INDCSVとなった項目についてレポート内容を確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 4:49 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

今回のケースで問題なく試験が進んだ場合は以下の様な時間的イメージとなります。（日本分のみ）

RF：4日程度

[ID]：3日程度

Profile：2日程度状況により途中中断、問題箇所再確認などで時間は大きく変化する場合があります。

ご了承ください。

Bluetooth IOPT試験について以下エンジニアから報告がございます。

★ALAP(UXC10)のIOPT試験で18項目中14項目はPassしました。

残る下記項目がFail、またはINDCSVとなっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

上記のPTSレポート(ログ付)を添付しますので、ご確認および解析をお願いします。特に製品のSDPレコード内容を重点的にご確認ください。

PTSのIXITの設定で対処できるものはその旨お知しらせください。FW改修が必要な場合は改修FWをご準備ください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 2:20 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご確認どうもありがとうございました。

各試験の想定日数を教えていただく事は可能でしょうか。

問題発生により変化することも承知しておりますので、特に問題無く進んだ場合の日程感で構わないです。

RF ・・・

RF PHY ・・・

IOPT ・・・

RF PHY 試験前の DUT 更新時期や、 IOPT 試験後ディスプレイご返却のタイミングを知っておきたいためです。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 2:08 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

QUESTIONNAIRSの方、受け取っております。

RF PHY試験の方のテストプランも作成いたしました。

DUTサンプルの運用につきましてはご希望通り対応予定です。

何かございましたら改めて連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 1:57 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご確認、どうもありがとうございました。

試験のご対応を引き続きよろしくお願いいたします。

別メールにしてしまいすみませんでしたが、

Questionnaire の更新と DUT 更新対応のご相談をご連絡しておりますので、

そちらもご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 1:10 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

お待たせしております。

その後こちらで試行いたしまして、RF試験開始の段階まで進めることができたようです。

ＲＦ試験実施の上何かございましたら随時連絡いたしますのでしばらくお待ちください。

また、ＩＯＰＴ試験の方も動作確認いたしました。

特にこちらも問題ないようです。

取り急ぎ連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, October 9, 2025 6:58 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご指示有難うございます。

昨日連絡いたしましたDUTの通信接続ができない問題について、

電流の制限を調整したところその部分につきましては正常に動作することが確認できました。

ただ、その先で確認を要する状況となっておりますので、もう少しはっきりしましたら改めて連絡いたしますので、もうしばらくお待ちいただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Thursday, October 9, 2025 3:18 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

弊社での似た過去事例にもとづき、少しご確認お願いしたい点がございます。

·
Wake_up 端子の GND 接続確認

DUT の Wake_up ラインが電源の GND に接続されていることをご確認お願いします。

接続が外れると DUT が Sleep 動作に入る動きをしますため。

·
電源投入後、 30 秒待機電源投入後、ソフト起動に 30 秒程度時間がかかりますので、それを待ったのち、操作を開始してみていただけますでしょうか。

以上、２点のご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 6:01 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

RF 試験のDUT Settingで以下の現象が起きております。

・「(UXC)AT operation manual_for_BT_rev001.xlsx」内の手順５実施後、「root@lemans:~#」が表示されず、通信接続ができません。

TeraTermは最新バージョン(5.5.0)を使用しております。

TeraTermを別のバージョン(5.4.1)で確認しましたが、同様の現象が起こります。

手順5実施中にも切断されることがあります。

こちら対策をご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 5:54 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

★ RF PHY は確認中で未記入項目があって Test
Plan は作成できません。

QUESTIONNAIREの未記入（TBD）の項目のご確認状況はいかがでしょうか。

★サンプルは本日到着し、セッティング、動作確認を行っております。

確認結果わかりましたら連絡しますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 9:11 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様立て続けて申し訳ございません。

RF 試験の DUT 操作マニュアルおよび TeraTerm 用マクロを提出します。

ご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 2:54 PM

To: 'Toshitaka Mochizuki'

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

以下、トピックごとにご連絡いたします。

■ DUT list について間違い修正や写真追加等で更新しました。

添付しました 2025/10/07 のもので差し替えをお願いいたします。

■ DUT 機材発送について

RF 試験用と IOPT 試験用の DUT 機材を別々に発送しました。

以下、ヤマトの送り状番号です。

■ [ID] について別メールですが質問事項へのご回答、ありがとうございました。

（現在の記述で問題無いと理解いたしました）

■ IOPT 試験用の DUT 操作マニュアルについて添付の AOSP_Bluetooth_User_Manual_1_0_0.pdf が試験用の DUT 操作マニュアルです。

不明点などありましたら、ご連絡お願いいたします。

■ RF 試験用の DUT 操作マニュアルについて明日を目標に、現在準備中です。

整い次第、お送りいたします。

以上、ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 7, 2025 11:06 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ドキュメントのご送付ありがとうございます。

試験サンプルの接続、操作マニュアルのご提供もお待ちしております。

（可能であれば英文、もしくは中文併記でいただけますと助かります。）

引き続きどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 9:24 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご回答ありがとうございます。

送信データ量が大きくなりすみません。

■機材提出票および DUT list

機材提出票を作成いたしました。

RF DUT 一式の方はのちのち台湾に行く予定のため、 IOPT
DUT とは別で扱えた方が好ましいと思いましたため、そのようにしました。

また、 WFA メールスレッドの方でありました税関対策の意味も込めて DUT
list を作成しました。 RF DUT の接続写真はのちほど載せるようにします。

お気づきの点等ございましたらご連絡ください。

■ [ID]

こちらも作成いたしました。

下記のご確認をよろしくお願いいたします。

Antenna だけの値を持っていないことから、 Cable
Loss も含めた値となります。こちらで構いませんでしょうか？

このケーブルは、製品のアンテナケーブル or 測定用ケーブルどちらになりますでしょうか？添付ファイルには、一旦、測定用ケーブルのロスを書いています。

BLE の試験モード検討中のため、今時点 TBD とさせてください。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 6:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

＞・ RF試験とIOPT試験用に、DUT一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

★管理を共通にしてよいのであれば、最終的なご提供物を１冊にまとめていただいても問題ございません。必ず数量、それぞれの識別が出来るようにサンプル本体や付属品にラベルなどを貼ってください。

＞・ IOPT試験はQuestionnaireはございますか？

★こちらICSを既にいただいているので特にQuestionnaireは必要ございません。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 4:54 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご指示ありがとうございます。

以下、確認させてください。

·
RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

·
IOPT 試験は Questionnaire はございますか？

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 11:47 AM

To: Misumi Sato ;
酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

先週はお打ち合わせありがとうございました。

Wi-Fiと一旦メールを分けさせていただきます。

Bluetoothサンプルの送り先ですが、当社日本ラボは本メールのフッタにございます望月宛にお送りください。

また、その際には添付の機材提出票をお送りください。

またRF テストプラン作成のため、添付のQUESTIONNAIRSにご記入の上、ご返送いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Misumi Sato

Sent: Friday, October 3, 2025 4:06 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

こちらこそ早速発送手続き着手していただきありがとうございます。

ご発送準備整いましたら、追跡番号とインボイスをご提供いただけますと幸いです。

尚、以前貴社の別部隊のWFA認証試験をご担当させていただいた際台湾から日本へのDUT返送時に、税関から再輸入免税措置を求められた経験がございます。

その際、製品個々のシリアルナンバーが必要だったため、念のため、DUT本体や

Wi-Fiアンテナ等にシリアルナンバーをご設定いただくことをお勧めいたします。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 3:51 PM

To: Misumi Sato ;
Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について佐藤様お世話になります。

アルプスアルパイン酒井です。

早速のご回答、どうもありがとうございます。

来週早々に発送手続き着手する予定です。

よろしくお願いいたします。

酒井

From: Misumi Sato

Sent: Friday, October 3, 2025 3:05 PM

To: 酒井重之 Shigeyuki Sakai ;
Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

午前中の会議ではありがとうございました。

横から失礼いたします。

WFA試験のDUTの送付先ですが、下記の表に記載させていただきましたので、ご参照お願いいたします。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

追跡番号、インボイスをご連絡その他、何かWFA試験に関すること、および輸送に関するご質問等ございましたら、お気軽にお問い合わせくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 2:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

PCAT のご確認ありがとうございました。

この内容を踏まえまして、弊社側でどう対応するか確認いたします。

機材の発送について、

·
下記の通り、弊社から送る際の送付先を教えていただけますでしょうか。（間違い等ありましたら修正をお願いいたします）

·
該非判定見解書等の時間かかるものは着手開始したいと思いますので、対応必要事項欄に追記していただけますでしょうか。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

追跡番号、インボイスをご連絡よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, October 3, 2025 12:16 PM

To: 酒井重之 Shigeyuki Sakai ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

Subject: Re: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

会議資料の更新＆共有させていただき、ありがとうございます。

PCATに関して台湾ラボがHM26のWi-Fi認証試験で利用実績がございます。

ただ、御社別部隊から異なる案件への対応として、

今回V社様案件で使用してよいか、バージョンの指定がないか、

使用できない場合、御社からご提供いただけるか、

ご確認いただきますよう、お願いいたします。

※ HM26の案件で使用したPCATのバージョン：[ID]

よろしくお願いいたします。

Outlook
for Android を取得

---

## 3. 2025-11-13 12:41

**From:** Itsuo Sakai
**To:** Shigeyuki Sakai , Toshitaka Mochizuki

アリオンの酒井です。いつもお世話になっております。

望月に代わって私から回答いたします。
ログのご提供、ありがとうございました。
一つ確認させてください。
Command: LEReceiverTestv1

Expected: 0x040EXXXXXXXX00
Received: 0x040E04011D200C
上記のような期待値と異なる値は、PC上のLE Direct Modeのログにも現れておりましたか？
DUTからは正常に返したのにLE Direct Modeで何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

⇒InterLabテストシステムでコマンドおよびコマンド応答の上記ログが表示されるのは試験冒頭の「Set DUT in Direct Test Mode」という表題に続くLEReceiverTestv1コマンド部分で受信したコマンド応答が期待値と異なる場合のみです。このためQ社アプリでは自動試験で全てのコマンドとコマンド応答をログ表示するものの試験項目の情報がなく、InterLab

ログは各試験項目の2402, 2440, 2480MHログに分散し、期待値と異なる場合のみて格納されるため対比するのが困難です。

自動試験に入る前に手動でLEReceiverTestv1コマンドに対する応答を確認する段階では以下のように期待値の最終Octedが00→0Cとなる事例はありませんでした。さらにTRM試験では自動試験で期待値と異なるコマンド応答は発生しないため、おそらくQ社アプリで変換されることはないものと思います。

<InterLab>

15:16:03

Running Serial - HCI LE Receiver Test v1: 1

15:16:04 Sent: 0x011D200100

15:16:04 Expected: 0x040EXXXXXXXX00

15:16:04 Received: 0x040E04011D2000

15:16:04

LE Receiver Test v1: Completed. Result: Success

15:16:07

Running Serial - HCI LE Test End: 1

15:16:14 Sent: 0x011F2000

15:16:14 Expected: 0x040EXXXXXXXX00

15:16:14 Received: 0x040E06011F200C0000

15:16:14 Packets: 0x0000

15:16:14

LE Test End: Completed. Result: Success

<Q社アプリのログ>

9: 15:12:[ID] HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x00

10 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e , 0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

11 15:12:[ID] HCI_Command:0x01 , 0x1f , 0x20 , 0x00 ,

12 15:12:[ID] HCI_Event(1366):0x04 , 0x0e , 0x12 , 0x01 , 0x00 , 0xfc , 0x00 , 0x19 , 0x0c , 0x13 , 0x00 , 0x00 , 0x00 , 0xe6 , 0x38 , 0x01 , 0x02 , 0x10 , 0x02 , 0x0c , 0x40 ,

13 15:12:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00

14 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e , 0x06 , 0x01 , 0x1f , 0x20 , 0x0c , 0x00 , 0x00 ,

酒井さんの懸念を確かめるには、PC-InterLab間にRS232ロガーを設置して送出データを逐一記録後、Q社ツールのログと比較することが必要ですが当社ではすでにシリアル通信ロガーあるいはRS232プロトコルアナライザを持ち合わせておりません。

以上回答いたします。

差出人: Shigeyuki Sakai

送信日時: 2025年11月13日 20:26

宛先: Toshitaka Mochizuki

件名: RE: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ログのご提供、ありがとうございました。

一つ確認させてください。

Command: LEReceiverTestv1

Sent: 0x011D20010C

Expected: 0x040EXXXXXXXX00

Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？

DUT からは正常に返したのに LE
Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

（この Logging にも現れていたかどうか）

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 6:58 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

お待たせいたしました。

RCVログをお送りいたしますので、こちらの内容の確認、解析をいただけますでしょうか。

Passwordは追ってお知らせいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 5:01 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

以下連絡いたします。

FTMモード投入後にTeraTarmでuxc_enable_synergy.ttlというマクロスクリプトを発行後、Q社アプリのHandshake=DTRに合わせてInterlabの

DTR=Trueに設定した結果、送信TRM系試験項目は実施でき、1Mモードの全4項目がPassしました。

残る受信RCV系は不思議なことにDUTが試験セットアップ時のInterLabからのDTMコマンドに正常応答しないために試験Passに至りません。

TRM試験がPass完了したということは、 DUT <-> PC <-> InterLb 間の電気的・論理的接続は正常ということになります。しかしRCVコマンドに対するDUTの応答がInterLabに届くものの、期待値通りの正しい応答ではないという症状です。考えられるのは、「DUT内蔵のテストFWの不具合で、

InterlaboからのDTMコマンドに正常応答していない」と推測されます。

現在下記RCV試験項目を実施中で、明日Failログをまとめて送付いたしますので、お手数ですがそのログとともにV社経由Q社にテストサンプル内のDTM

FWの解析依頼をお願いいたします。

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

以上ご確認どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 6:53 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

種々のご確認、こちらこそ大変恐れ入ります。

PC側との兼ね合いがあるとのこと承知いたしました。

明日改めてこちらの方法でも確認させていただきます。

台湾作業の前にクリアできればと思います。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, November 12, 2025 6:48 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

（メインで担当中の梅田が今週末まで不在のため、私から回答いたします。窓口がしばしば変わりご迷惑をおかけします。）

色々とご確認ありがとうございます。

解決に至るかどうか分からないのですが、過去遭遇した接続不良時の対応を共有いたします。

そのときは、 Windows PC 側の Port 設定が重複していたようで、異なる IP
Address を DUT に設定し直すことで接続が回復しました。

そのためのマニュアル、マクロ、 bat ファイルをお送りいたします。

マニュアルの BLE measurement procedure (2)
シートをご覧ください。

下記ケーブルが同梱されていたかと思いますが、最初にこのケーブルを使用して DUT の IP
Address を [ID] に変更します。その上で BLE 試験用の接続を行う、というものです。

また、現地確認のご提案もありがとうございます。

上記でも解決が見られなければ御社へ伺うことも検討中です。

お手数おかけしますが、接続の確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 2:55 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

いただいたログからは一旦Bluetooth-FTMモードに入るとノーマル操作ができなくなり、

TeraTarmでuxc_enable_synergy.ttlというマクロスクリプトを発行してDUTのテストFWを通常FWに戻さないと。電源再投入後に通常動作しないと読み取れる可能性があるようだということが判ってきましたので、

こちらではこの点を引き続き確認するよう進めます。

他になにか必要な操作などございましたらご教示お願い申し上げます。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 11:40 AM

To: Shuhei Umeda ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

DUTとの接続を一旦すべて外してやり直したり、システムやPCの電源を入れ直したりを何回かやってみましたが、

HCI_Eventの受信はできませんでした。

何か他に考えられる状況はございますでしょうか。

状況に応じ、ご来訪でのご確認も可能です。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

HCI_Eventが表示されていないということは、PCからUXCに対してHCI_Commandが送信できていないか、

UXCからPCへのHCI_Eventが受信できていないかになるかと思います。

一度HCI_Eventは受信できていましたので、接続状態を再確認いただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 11, 2025 1:38 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご教示ありがとうございます。

現在確認作業をしておりますが、

本日朝から手順に従い&quot;Bluetooth Test Mode&quot;を再度実行しましたが、昨日はあった&quot;HCI_Event&quot;の行が表示されなくなりました。

どのような原因、確認、復旧手段があるかご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 8:59 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

弊社ではInterLabシステムを使用したことがないのですが、

LE Direct Mode（Qualcomm Tool）のLog上は、送信/受信ともに正常に動作しているように見えます。

それに対してInterLabシステムの画面上は“Received”に何も表示が無いので、InterLabシステムは受信ができていないように見えます。

よって、PCとInterLab間のケーブルの接続状態を再度ご確認いただけますでしょうか？

また、過去HM26モデルでは同じテストシステムで送受信は問題なかったでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, November 10, 2025 5:04 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

下記のDUTとの接続で、InterLabシステムとの通信を行おうとしていますがfailとなります。

何か確認すべき点や修正すべき点などございましたらご教示いただけますでしょうか。。

InterLabシステムとの接続いただきました&quot;Bluetooth Connection Diagram&quot; (添付)の真ん中の下側のPCのUSBポートとInterLabシステムのUSBポートを接続。

使用ケーブル：

[ID]232C変換ケーブル⇔ RS-232Cメス-メスケーブル (クロス) ⇔ [ID]USB変換ケーブル

InterLabシステムから&quot;LE Reset&quot;を実行。

QUTS Status Appの画面

InterLabシステムの画面ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:48 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

情報いただきありがとうございます。

接続できるようになったとのこと承知いたしました。

引き続きよろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:13 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

RF PHYの方ですが、 ご連絡いただいた内容を実行したところ、下記の通り接続できましたのでお知らせします。引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:02 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様承知いたしました。

早速のご対応感謝いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:00 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

本日サンプル発送いたします。

運送会社：佐川急便お問い合わせ送り状No.[ID]

酒井様宛て一個口どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 11:01 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様はい。ディスプレイ部、付属品含めてとなります。

お手数ですが、ご対応よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 10:58 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様ご連絡有難うございます。

一式ということはディスプレイ部、付属品も含めてという認識でよろしいですね。

発送は可能と思いますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 10:53 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT試験用に弊社から送付しましたDUT一式ですが、

返却いただくこと可能でしょうか？

お手数ですが、ご確認をお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Wednesday, November 5, 2025 8:58 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

QUTSのバージョンは最新になっていますでしょうか？

Qualcomm Package Managerを起動して、”Updates Available”タブを選択し、

もし最新のバージョンが存在する場合は、最新版をインストールしてみてください。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, November 4, 2025 7:12 PM

To: 'Toshitaka Mochizuki' ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきましてありがとうございます。

QUTSが動作するところまで進んだようで良かったです。

Step7までは手順書の通り進んでいるのにStep8でIPアドレスが表示されないということですね。

即答できないのでこちらでも調査してみます。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 6:27 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

現在再確認作業を行っております。

UXC10のRF-PHYのセットアップを、いただきました手順書で行っておりますが、

ステップ8で、COM PortのところでIPアドレスを選択するように書いてあるのですが、

下記の通り、IPアドレスが表示ず選択できません。

どうすれば、IPアドレスを選択できるようになるかを、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

Qualcomm Package Managerの検索WindowにQUTSを入力すると、該当するツールが絞り込まれると思います。

お試しいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 1:35 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

QUTSStatusApp ですが、 Qualcomm 社のサイトの Software のダウンロードを探しておりますが、複数のパッケージが表示されますが、そのものズバリのものが出てきません。

こちらは何のパッケージに入っているかご教示いただけますでしょうか。

お忙しいところお手数ですが、ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Shuhei Umeda

送信 : 2025
年 10
月 31
日 ( 金曜日 ) 13:18

宛先 : Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再度ご確認いただきましてありがとうございます。

Qualcomm IDを取得されていること承知いたしました。

ということは、Qualcomm Package Managerを使用してQUTSのインストールはできそうでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 11:43 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は終日不在としてご迷惑をお掛けいたしました。

以下回答となります。

ご確認どうぞよろしくお願い申し上げます。
もし存在しない場合、QUTSStatusAppの御社への提供方法を検討いたします。
ただ、QRCTをお持ちであるということは、何らかの方法でQRCTをインストールされたと思いますが、御社がQualcomm IDをお持ちでないのは確かでしょうか？
基本的にQualcommのツールは起動時にネットワークを経由して、Qualcommサーバーと何らかの認証を行っていると思います。
QRCTが使えているので、その認証はPassしていることになります。

⇒先のメールでアリオンはQualcomm IDを取得していないとお伝えしましたが御社HM26案件で営業の王がQualcomm IDを取得しておりました。大変失礼しました。
使用中のQRCTのバージョンについて教えていただけますでしょうか。

⇒別途調べてお答えします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 10:45 AM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオンジェシー様/望月様お世話になっております。アルプスアルパインの梅田です。

ご確認いただきましてありがとうございました。
Step 7: Run QUTS Status App」と記載されていますが、ラボにQUTS Status Appがないため、貴社に確認したところ、QRCTでもQUTSの確認が可能とのことでした。
そのため、本日はQRCTを使用してBLE DTMモードへの移行を試しました。

誤解を招いてしまったかもしれません。

QRCTでQUTSの確認はできません。

QRCTがインストールされているのであれば、QUTSも一緒にインストールされているのではないか、との推測になります。

Qualcomm社のダウンローダー上、QUTSがQRCTにも含まれるような構成になっているためです。

お手数でございますが、再度、以下のPathにQUTSStatusApp.exeがあるかどうかご確認いただけますでしょうか？

C:\Program Files (x86)\Qualcomm\QUTSStatusApp\QUTSStatusApp.exe

もし存在しない場合、QUTSStatusAppの御社への提供方法を検討いたします。

ただ、QRCTをお持ちであるということは、何らかの方法でQRCTをインストールされたと思いますが、

御社がQualcomm IDをお持ちでないのは確かでしょうか？

基本的にQualcommのツールは起動時にネットワークを経由して、Qualcommサーバーと何らかの認証を行っていると思います。

QRCTが使えているので、その認証はPassしていることになります。

使用中のQRCTのバージョンについて教えていただけますでしょうか。

また、御社とQualcommとの間に契約関係はございますでしょうか？

以上、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 5:14 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様お世話になっております。

アリオンのジェシーです。

ご返信ありがとうございます。

＞現在実施しようとしている試験は、Bluetooth Measurementでしょうか、それともBLE Measurementでしょうか？

現在実施しようとしている試験はBLE Measurement ([ID])です。

また、ラボに確認したところ、Bluetooth Measurement (RF)試験は既に実施完了しまして、テストレポートも先日提出させていただきました。

＞手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

BLE Measurementについては、Step ６マクロの実施（uxc_BLE_FTM_Mode.ttl）まで成功しました。

Step 7: Run QUTS Status App」と記載されていますが、ラボにQUTS Status Appがないため、貴社に確認したところ、QRCTでもQUTSの確認が可能とのことでした。

そのため、本日はQRCTを使用してBLE DTMモードへの移行を試しました。

但し、BLE Measurementの測定手順ではQUTS Status Appでの設定方法が指定されているため、QRCTの画面上でどのように設定してBLE DTMモードへ移行すればよいのかが分かりませんでした。そのため、本日再度お問い合わせさせていただきました。

大変恐縮ですが、現状（QUTS Status App無し）でBLE DTMモードへの移行方法があればお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shuhei Umeda

Sent: Thursday, October 30, 2025 4:28 PM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオンジェシー様お世話になっております。アルプスアルパインの梅田です。

望月様の代理でのご確認ありがとうございます。

Qualcomm IDはお持ちでは無いが、QRCTのインストールはできた、またはQRCTは既にお持ちだったということでしょうか。

QRCTの画面を添付いただきましたので、QRCTが動いている前提でお話しますが、

添付しました資料は既に展開させていただいているQRCTの動作手順書です。

現在実施しようとしている試験は、Bluetooth Measurementでしょうか、それともBLE Measurementでしょうか？

手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

お手数ですが、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 4:09 PM

To: 酒井重之 Shigeyuki Sakai ;
梅田修平 Shuhei Umeda

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様、酒井様、

お世話になっております。

アリオンのジェシーです。

ご不便をお掛けして申し訳ございません。

本日望月が社内不在のため、代理にてラボのフィードバックをご連絡いたします。

＞【BLE】

＞御社にて Qualcomm からツールを直接入手することは可能でしょうか？

申し訳ございません。内部で確認したところ、弊社はQualcomm IDを持っていないため、Qualcommからツールを直接入手できないです。

メールでご提示いただいた方法（QRCTの利用）を試しましたが、接続に失敗しました。添付のScreenshotをご参照ください。

確認したところ、USBケーブルで制御用PCに接続していますが、PC側でUSBデバイスとして認識されていません。

また、USB Driver.exeはQRCTフォルダ内に存在しないようです。

念のため、「Select USB Driver.exe」ボタンをクリックし、QC.BluetoothLE_DirectMode.exeを選択して接続を試みましたが、Failed device connectionと表示されました。

ご確認いただき、QRCTでDTMモードへ移行する手順をお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shigeyuki Sakai

Sent: Monday, October 27, 2025 1:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

本日、梅田が不在ですので、私からご回答します。

【IOPT】

添付のファイルが過去に Volvo から提供されていたのですが、御社へ提出していなかったと思います。申し訳ありません。

“adb install BlueSPP.apk”

については、 PDF の 3 ページ目に記載されております。

一度ご確認いただけますでしょうか。

【BLE】

御社にて Qualcomm からツールを直接入手することは可能でしょうか？

通常ですと QPM(Qualcomm Package Manager) というツール経由で PC にインストールします。

（そのためツールインストーラーをお渡しすることができないことも背景です）

QUTS は下記 QRCT をインストールすることで一緒に導入されます。

QRCT は Classic の試験でご使用いただいたと思いますので、 QUTS もご確認可能ではと思います。

一度ご確認いただけますでしょうか。

なお、 BLE 試験用にご提供しました手順書の &quot;Notes
on QRCT tools&quot; シートに QRCT のインストールの説明を記載しておりますので、合わせてご確認をお願いいたします。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:31 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

RF-PHY試験に関して、メールでいただいているQUTS Status Appと Run Bluetooth LE Direct Modeテストツールがまだご提供いただいていないようです。

ご確認の上、ご提供お願いできますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:07 AM

To: Shuhei Umeda ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

10月21日19:42の梅田様からのメールでは、「IOPTTestguide.pdfに記載されているBlueSPP.apkをインストール」という記述がありますが、

こちらで探しておりますが、これら資料をいただいていないようです。

もしお送りいただいているようでしたら、そのメールご送付の日時をお知らせいただけますでしょうか。

またIOPTTestguide.pdf以外にも関連する試験で必要なファイルがございましたら併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 7:29 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

まずはadbが正常に動作できるようになったとのこと承知いたしました。

こちらかの情報に誤りがありまして申し訳ございませんでした。

また、SPPの再試験ありがとうございました。

結果を再度V社と共有いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 7:02 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

&quot;USB-A 2.0&quot;というラベルの付いたケーブルを使用したところ、adb install はできましたが、

再度SPPのプロファイル試験を実行しましたが、結果は以前と同じでした。

logのファイルを添付いたしますので、ご確認いただけないでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 10:39 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様ご確認いただきありがとうございました。

こちらのケーブルになります。

このケーブル経由でadb関連のコマンド操作を試してみていただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 9:51 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

添付のケーブルがございましたが、こちらのことでよろしいでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 7:08 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

何度もご確認いただきましてありがとうございます。

再度、PCとDUTの接続方法を確認させてください。

弊社から送付したDUTですが、USBケーブルが4本あったと思います。

DEBUG SAIL

DEBUG HKP

DEBUG MD

以外のもう1本のケーブルはございますでしょうか？もしよろしければ写真を撮って送っていただけると助かります。

DEBUG MDとご案内いたしましたが、残りの1本がDUT側のUSB機能として使うもので、

こちらのケーブルでないとadbが動作しない可能性がございます。

お手数をおかけいたしますが、4本目のケーブルのご確認をお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

お送りいただきました資料を確認し、adb shell settings put global development_settings_enabled 1&quot;コマンドを送りましたが、以下のエラーが表示されます。

&#8226; error: no devices/emulators found

DUTやPCなどで、他に確認すべき点や、設定すべき点がございましたら、ご教示いただけますでしょうか。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 1:19 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

添付ファイルのP.2にBasic DUT operationsが記載されておりますが、

Developer ModeはEnableになっていますでしょうか？

adb shell settings put global development_settings_enabled 1

を実行してから

adb install bluespp.apk

を試してみていただけますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 12:55 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡いただきました&quot;DEBUG MD&quot;のUSBケーブルをPCに接続し、&quot;adb install bluespp.apk&quot;を実行したところ、下記のエラーが表示されました。

&#8226; adb: connect error for write: no devices/emulator found

また、&quot;adb devices&quot;コマンドを実行いたしましたが、&quot;List of attached devices&quot;の下に何も表示されず、認識されていないようです。

PCやDUTで、他に設定する所などがございましたら、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 11:53 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご確認ありがとうございます。

DEBUG MDとPCを接続してください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 11:51 AM

To: Itsuo Sakai ;
梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は不在といたしまして申し訳ございません。

以下確認事項がございますので、

ご回答いただけますでしょうか。

BlueSPP.apk をインストールするには、 DUT の下記の 3 本の USB ケーブルのどれを PC に接続すればよいかご教示ください。

DEBUG SAIL

DEBUG HKP

DEBUG MD

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 5:25 PM

To: Shuhei Umeda ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
Connection Diagram ですが、 RF
PHY Test System を追記したものを準備いたしました。
こちらを参照いただけたらと思います。

⇒ 何度もお手数をお掛けしました。これで RF
PHY 試験の接続系統図が明確になりました。ありがとうございました。

引き続きよろしくお願いいたします。

酒井差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 16:00

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様

Connection Diagramですが、RF PHY Test Systemを追記したものを準備いたしました。

こちらを参照いただけたらと思います。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, October 21, 2025 2:33 PM

To: 'Itsuo Sakai' ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

Operation ManualですがPDFに変換しました。

こちらをご参照ください。
RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。

使用いたします。

添付のBluetooth measurement procedure.pdf、BLE measurement procedure.pdf を参照ください。

操作手順の中にEthernetに関する操作がございます。
ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の
USB 接続部分は反映されていないという理解で間違いないでしょうか。

おっしゃるとおりです。Bluetooth Connection Diagramに反映されておりません。
そうあれば私の最初からの質問であるテストシステムの Serial
over USB
の接続先ですが、それは PC
running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

はい。その理解で合っています。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 1:43 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
RF PHY Test System との接続は以下の図をご参照ください。
DUT と PC
running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。
RF PHY Test System と DUT は RF のみ接続します。

⇒ RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。
そして PC running QDART と RF
PHY Test System は直接 RS232、 GPIB での接続となります。

⇒ HM26 でも同じ図の Q 社マニュアルを使いました。しかし、 DTM モードでは GPIB 経由のコマンドの定義はなく、 Serial
over USB を含む Serial

(UART) 経由でのコマンドが定義されそれに従って DUT を制御しています。

このため DUT と PC および RF
PHY テストシステムは下図のような接続系統図となります。

ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の

USB 接続部分は反映されていないという理解で間違いないでしょうか。

そうあれば私の最初からの質問であるテストシステムの Serial over USB

の接続先ですが、それは PC running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

以上ご確認をお願いします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 12:55

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

RF PHY Test Systemとの接続は以下の図をご参照ください。

DUTとPC running QDART間はUSB conversion harnessを使ってUSB Serialで接続いたします。

RF PHY Test SystemとDUTはRFのみ接続します。

そしてPC running QDARTとRF PHY Test Systemは直接RS232、GPIBでの接続となります。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 12:01 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

ご返信ありがとうございます。
制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。
ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

⇒ 図では黄色マーカー部分の一端が PC,
他端が DUT ですが、文面から推測すると下図かと思われますが、正しいでしょうか ?

以上よろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 21 日 11:40

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。
以上のようにご送付いただいた Connection
Diagram では RF PHY の
DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。

制御結線についてですが、RFテストシステム-DUT間の結線は以下の画像の黄色マーカー部分になります。

ちょうどご質問をいただいたUSB conversion harness-USB Type-Aケーブルの部分です。

DUT &#8211; USB conversion harness &#8211; USB Type-Aケーブル &#8211; PC で結線され、USB SerialとしてPCとDUT間の通信が可能となります。

後ほど、Operation ManualをPDF化して送付するようにいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, October 20, 2025 7:19 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

先程の質問は私の Excel のバージョンが古いせいか以下の図が表示されたためで、「薄緑線の分岐」とか「薄緑線の上方の接続先」が何のことやらと思われたと思います。お詫びします。

しかし、 RF PHY 試験は認証テストシステム及び簡易なアンリツ

BT テスタでも RF 測定系とは別に、 UART/COM ポート接続が必須で、

HM26 でも下図のように外部 PC ＋ Q 社テストアプリを Bridge にして

DUT<->(Eternet)<->PC<->(Serial over USB)<->RF PHY テスターという接続を行いました。その際の DTM モードマニュアルを添付します。

以上のようにご送付いただいた Connection Diagram では RF
PHY の

DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。ご送付の Connection Diagram はおそらく電波法 /FCC 試験時のオープンループ試験用のものと推測されます。再度 DTM モードのセットアップ方法をご確認ください。

以上よろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 20 日 18:35

宛先 : Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様

SPPのレポートの送付ありがとうございました。

内容確認して返信いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 6:17 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

SPPのレポートをお送りいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Monday, October 20, 2025 5:16 PM

To: Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPTの再試験の実施ありがとうございました。

SPPについてですが、再試験結果のレポートを送付いただくこと可能でしょうか。

V社側に連絡して事前条件やSWの差分の有無について確認を依頼したいと思います。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 5:12 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

IOPT試験について連絡です。

御社からご送付いただいたSPPのPTSレポートと同じICS設定であることを確認してv8.10.2で再試験を実施しましたところ、MAPとPBAPはPass

しましたがSPPはPassしませんでした。

SPPのPTS試験では、スタート前にDUTの接続済機器一覧からPTSを削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいたPassレポートを得られたDUTのSWが当社のDUT

のSWから更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいたSPPのPTSレポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 20, 2025 1:36 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご返却、どうもありがとうございました。

弊社側での内部データ更新が完了しまして、先ほど望月様宛での発送手続きが完了したところです。

ヤマトお問合せ No : [ID]

併せて、 RF PHY 試験の手順書もお送りします。

ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 1:40 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

承知いたしました。

更新いただいた後、RF PHY試験の日本分実施後、台湾での試験向けに発送予定です。

その際に該否判定書と製品仕様書が必要になります。

今回はRF試験についてはモニタ部分については輸出は必要なかったとおもいます。

また、先日お伝えいたしました、プロファイル（IOPT）試験についてのご修正についてもそちらのサンプルの返送が必要でしたらおしらせください。

以下RF試験機の返送になります。

運送会社：佐川急便お問い合わせ送り状No.[ID]

酒井様宛て一個口引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, October 15, 2025 12:56 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

＞ 御社へ一旦サンプルをお返しするという事だったと存じます。

はい、お手数おかけしまして申し訳ありませんが、そのように進めさせてください。

RF 試験用のサンプルは以下の写真が示す DUT のみで大丈夫です。

ご返却の宛先は私でお願いいたします。

福島県いわき市好間工業団地 20-1

アルプスアルパイン株式会社 DC1 設計部酒井重之あと、 BLE
オプション機能の試験のため DUT を台湾に発送されると思いますが、弊社から該非見解書をお出しするということでよろしいでしょうか。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 6:28 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

RF試験が完了いたしましたが、RF PHY試験実施のため御社へ一旦サンプルをお返しするという事だったと存じます。

RF試験用のサンプルですが、Fullセットでお返ししたほうがよろしいでしょうか。

必要な物のみでよろしければご指定いただければそちらのみお返しいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, October 14, 2025 9:52 AM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきありがとうございました。

RF試験が合格完了とのこと承知いたしました。

引き続き、RF PHYの実施、よろしくお願いいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Friday, October 10, 2025 7:35 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: [RF 試験合格完了 ] Re:
【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン梅田様、酒井様アリオンの酒井です。いつもお世話になっております。

望月に変わり私からお知らせします。

先程 RF 試験が合格完了しましたのでお知らせします。来週 RF
PHY(1M)

を実施し、 Pass 後に台湾ラボへ送って (2M,
Coded) を実施する予定です。

引き続きよろしくお願いいたします。

差出人 : Shuhei Umeda

送信日時 : 2025 年 10 月 10 日 17:38

宛先 : Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

酒井に代わりまして本件返信させていただきます。

まず試験日程のイメージの共有ありがとうございました。

おおよそこれぐらいの日程感で試験が進むこと承知いたしました。

次に、Bluetooth IOPT試験の結果のご連絡ありがとうございました。

Fail、INDCSVとなった項目についてレポート内容を確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 4:49 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

今回のケースで問題なく試験が進んだ場合は以下の様な時間的イメージとなります。（日本分のみ）

RF：4日程度

[ID]：3日程度

Profile：2日程度状況により途中中断、問題箇所再確認などで時間は大きく変化する場合があります。

ご了承ください。

Bluetooth IOPT試験について以下エンジニアから報告がございます。

★ALAP(UXC10)のIOPT試験で18項目中14項目はPassしました。

残る下記項目がFail、またはINDCSVとなっております。

・IOPT/MAP/MCE/CGSIT/SFC/[ID]

・IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・IOPT/SPP/DEVB/SDPR/[ID]

上記のPTSレポート(ログ付)を添付しますので、ご確認および解析をお願いします。特に製品のSDPレコード内容を重点的にご確認ください。

PTSのIXITの設定で対処できるものはその旨お知しらせください。FW改修が必要な場合は改修FWをご準備ください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 2:20 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご確認どうもありがとうございました。

各試験の想定日数を教えていただく事は可能でしょうか。

問題発生により変化することも承知しておりますので、特に問題無く進んだ場合の日程感で構わないです。

RF ・・・

RF PHY ・・・

IOPT ・・・

RF PHY 試験前の DUT 更新時期や、 IOPT 試験後ディスプレイご返却のタイミングを知っておきたいためです。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 2:08 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

QUESTIONNAIRSの方、受け取っております。

RF PHY試験の方のテストプランも作成いたしました。

DUTサンプルの運用につきましてはご希望通り対応予定です。

何かございましたら改めて連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 1:57 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご確認、どうもありがとうございました。

試験のご対応を引き続きよろしくお願いいたします。

別メールにしてしまいすみませんでしたが、

Questionnaire の更新と DUT 更新対応のご相談をご連絡しておりますので、

そちらもご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 1:10 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

お待たせしております。

その後こちらで試行いたしまして、RF試験開始の段階まで進めることができたようです。

ＲＦ試験実施の上何かございましたら随時連絡いたしますのでしばらくお待ちください。

また、ＩＯＰＴ試験の方も動作確認いたしました。

特にこちらも問題ないようです。

取り急ぎ連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, October 9, 2025 6:58 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご指示有難うございます。

昨日連絡いたしましたDUTの通信接続ができない問題について、

電流の制限を調整したところその部分につきましては正常に動作することが確認できました。

ただ、その先で確認を要する状況となっておりますので、もう少しはっきりしましたら改めて連絡いたしますので、もうしばらくお待ちいただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Thursday, October 9, 2025 3:18 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

弊社での似た過去事例にもとづき、少しご確認お願いしたい点がございます。

&middot;
Wake_up 端子の GND 接続確認

DUT の Wake_up ラインが電源の GND に接続されていることをご確認お願いします。

接続が外れると DUT が Sleep 動作に入る動きをしますため。

&middot;
電源投入後、 30 秒待機電源投入後、ソフト起動に 30 秒程度時間がかかりますので、それを待ったのち、操作を開始してみていただけますでしょうか。

以上、２点のご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 6:01 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

RF 試験のDUT Settingで以下の現象が起きております。

・「(UXC)AT operation manual_for_BT_rev001.xlsx」内の手順５実施後、「root@lemans:~#」が表示されず、通信接続ができません。

TeraTermは最新バージョン(5.5.0)を使用しております。

TeraTermを別のバージョン(5.4.1)で確認しましたが、同様の現象が起こります。

手順5実施中にも切断されることがあります。

こちら対策をご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 5:54 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

★ RF PHY は確認中で未記入項目があって Test
Plan は作成できません。

QUESTIONNAIREの未記入（TBD）の項目のご確認状況はいかがでしょうか。

★サンプルは本日到着し、セッティング、動作確認を行っております。

確認結果わかりましたら連絡しますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 9:11 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様立て続けて申し訳ございません。

RF 試験の DUT 操作マニュアルおよび TeraTerm 用マクロを提出します。

ご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 2:54 PM

To: 'Toshitaka Mochizuki'

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

以下、トピックごとにご連絡いたします。

■ DUT list について間違い修正や写真追加等で更新しました。

添付しました 2025/10/07 のもので差し替えをお願いいたします。

■ DUT 機材発送について

RF 試験用と IOPT 試験用の DUT 機材を別々に発送しました。

以下、ヤマトの送り状番号です。

■ [ID] について別メールですが質問事項へのご回答、ありがとうございました。

（現在の記述で問題無いと理解いたしました）

■ IOPT 試験用の DUT 操作マニュアルについて添付の AOSP_Bluetooth_User_Manual_1_0_0.pdf が試験用の DUT 操作マニュアルです。

不明点などありましたら、ご連絡お願いいたします。

■ RF 試験用の DUT 操作マニュアルについて明日を目標に、現在準備中です。

整い次第、お送りいたします。

以上、ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 7, 2025 11:06 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ドキュメントのご送付ありがとうございます。

試験サンプルの接続、操作マニュアルのご提供もお待ちしております。

（可能であれば英文、もしくは中文併記でいただけますと助かります。）

引き続きどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 9:24 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご回答ありがとうございます。

送信データ量が大きくなりすみません。

■機材提出票および DUT list

機材提出票を作成いたしました。

RF DUT 一式の方はのちのち台湾に行く予定のため、 IOPT
DUT とは別で扱えた方が好ましいと思いましたため、そのようにしました。

また、 WFA メールスレッドの方でありました税関対策の意味も込めて DUT
list を作成しました。 RF DUT の接続写真はのちほど載せるようにします。

お気づきの点等ございましたらご連絡ください。

■ [ID]

こちらも作成いたしました。

下記のご確認をよろしくお願いいたします。

Antenna だけの値を持っていないことから、 Cable
Loss も含めた値となります。こちらで構いませんでしょうか？

このケーブルは、製品のアンテナケーブル or 測定用ケーブルどちらになりますでしょうか？添付ファイルには、一旦、測定用ケーブルのロスを書いています。

BLE の試験モード検討中のため、今時点 TBD とさせてください。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 6:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

＞・ RF試験とIOPT試験用に、DUT一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

★管理を共通にしてよいのであれば、最終的なご提供物を１冊にまとめていただいても問題ございません。必ず数量、それぞれの識別が出来るようにサンプル本体や付属品にラベルなどを貼ってください。

＞・ IOPT試験はQuestionnaireはございますか？

★こちらICSを既にいただいているので特にQuestionnaireは必要ございません。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 4:54 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご指示ありがとうございます。

以下、確認させてください。

&middot;
RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

&middot;
IOPT 試験は Questionnaire はございますか？

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 11:47 AM

To: Misumi Sato ;
酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

先週はお打ち合わせありがとうございました。

Wi-Fiと一旦メールを分けさせていただきます。

Bluetoothサンプルの送り先ですが、当社日本ラボは本メールのフッタにございます望月宛にお送りください。

また、その際には添付の機材提出票をお送りください。

またRF テストプラン作成のため、添付のQUESTIONNAIRSにご記入の上、ご返送いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Misumi Sato

Sent: Friday, October 3, 2025 4:06 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

こちらこそ早速発送手続き着手していただきありがとうございます。

ご発送準備整いましたら、追跡番号とインボイスをご提供いただけますと幸いです。

尚、以前貴社の別部隊のWFA認証試験をご担当させていただいた際台湾から日本へのDUT返送時に、税関から再輸入免税措置を求められた経験がございます。

その際、製品個々のシリアルナンバーが必要だったため、念のため、DUT本体や

Wi-Fiアンテナ等にシリアルナンバーをご設定いただくことをお勧めいたします。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 3:51 PM

To: Misumi Sato ;
Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について佐藤様お世話になります。

アルプスアルパイン酒井です。

早速のご回答、どうもありがとうございます。

来週早々に発送手続き着手する予定です。

よろしくお願いいたします。

酒井

From: Misumi Sato

Sent: Friday, October 3, 2025 3:05 PM

To: 酒井重之 Shigeyuki Sakai ;
Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

午前中の会議ではありがとうございました。

横から失礼いたします。

WFA試験のDUTの送付先ですが、下記の表に記載させていただきましたので、ご参照お願いいたします。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

追跡番号、インボイスをご連絡その他、何かWFA試験に関すること、および輸送に関するご質問等ございましたら、お気軽にお問い合わせくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 2:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

PCAT のご確認ありがとうございました。

この内容を踏まえまして、弊社側でどう対応するか確認いたします。

機材の発送について、

&middot;
下記の通り、弊社から送る際の送付先を教えていただけますでしょうか。（間違い等ありましたら修正をお願いいたします）

&middot;
該非判定見解書等の時間かかるものは着手開始したいと思いますので、対応必要事項欄に追記していただけますでしょうか。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

追跡番号、インボイスをご連絡よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, October 3, 2025 12:16 PM

To: 酒井重之 Shigeyuki Sakai ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

Subject: Re: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

会議資料の更新＆共有させていただき、ありがとうございます。

PCATに関して台湾ラボがHM26のWi-Fi認証試験で利用実績がございます。

ただ、御社別部隊から異なる案件への対応として、

今回V社様案件で使用してよいか、バージョンの指定がないか、

使用できない場合、御社からご提供いただけるか、

ご確認いただきますよう、お願いいたします。

※ HM26の案件で使用したPCATのバージョン：[ID]

よろしくお願いいたします。

Outlook
for Android を取得差出人: Shigeyuki Sakai

送信日時: 金曜日, 10月 3, 2025 10:59:20 午前宛先: Jun Wang ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

件名: RE: 【ALAP】[UXC] Wi-Fi Alliance認証計画について各位本日は、打合せをどうもありがとうございました。

更新した資料をお送りします。

‘QA’ シートに、★マーク付きで確認必要事項を書いております。

試験のご対応、引き続きどうぞよろしくお願いいたします。

酒井

-----Original Appointment-----

From: Jun Wang

Sent: Thursday, October 2, 2025 1:10 PM

To: Jun Wang; 酒井重之 Shigeyuki Sakai; Toshitaka Mochizuki; Itsuo Sakai

Subject: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について

When: 2025 年 10 月 3 日金曜日 9:30-10:30
(UTC+09:00) 大阪、札幌、東京

Where: Microsoft Teams 会議アルプスアルパイン酒井様こちらから設定して申し訳ございません。

明日の打ち合わせは少し早めに開始して、09:30からでお願いいたします。

時間帯を09:30〜10:30に修正し、会議案内を再送いたします。

宜しくお願いいたします。

アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

弊社側関係者に確認いたしまして、下記時間帯でお願いいたします。

10/3（金）　10:00〜11:00

会議リンクは下記ご参照願います。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
489 106 497 201 8

パスコード :
sR6yD26r

開催者向け :
会議オプション

________________________________________________________________________________

_____________________________________________

From: Jun Wang

Sent: Thursday, October 2, 2025 10:06 AM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

空き時間帯の共有ありがとうございます。

本日は酒井様のお時間が概ね埋まっているようで、

弊社関係者と一旦明日で調整させていただきます。

調整つき次第ご連絡いたしますので少しお待ちください。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Thursday, October 2, 2025 8:42 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご承諾ありがとうございます。

以下に私のカレンダーを貼りました。この白い時間帯でお願いできましたら助かります。

また、時間は 30 分を見込みますが、延長用に 1 時間スロットを頂けたら助かります。

ご確認をよろしくお願いいたします。

＜１０月＞

酒井

From: Jun Wang

Sent: Thursday, October 2, 2025 7:26 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi認証のPre-testの正式見積書について、

承知いたしました、ご用意いたします。

機材送付の段取りについての打ち合わせですが、

弊社側関係者に確認いたしますが、

予め酒井様のご都合をお伺いしてもよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, October 1, 2025 6:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご提案どうもありがとうございました。

【アルプスアルパイン様】 V 社 UXC10 の Wi-Fi 認証につきプリテストのご提案 _Update_1001.pdf の内容でお見積書をいただけますでしょうか。

あと、 BT SIG 試験と WFA 試験の DUT 機材発送段取りを考えておりますが、

機材の保管場所がいわきと中国大連に分かれている背景や、少し悩んでいる点があります。（添付ファイル）

この内容を一度打合せさせていただけませんでしょうか。

可能でしたら、打合せの候補日をいただきたいです。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, October 1, 2025 10:59 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10のWi-Fi Pre-testの部分試験に関して、

提案資料のP5に追加いたしました。

基本は本番試験の各対象Programに関して、WFAのTest Planより一部抽出して試験を行う考えです。

ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, September 30, 2025 9:40 AM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

早速ご確認いただきありがとうございます。

部分試験のブレークダウン、

なるべく早めにご報告するように調整してまいりますので、

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Tuesday, September 30, 2025 9:11 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

内容確認しまして、とても良い内容だと考えております。

ご提案どうもありがとうございます。

試験項目ブレークダウンお待ちしております。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Tuesday, September 30, 2025 6:46 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

お待たせいたしました。

UXC10のWi-Fi認証試験をスムーズに進めることができ、

そして目標時期までに認証取得できるように、

プレテストのご提案をいたします。※添付ご参照願います。

部分試験に関して、もう少し試験項目のブレークダウンについてラボと相談しておりまして、もう少しお待ちいただきますと幸いです。

ご検討賜りますようお願いいいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Monday, September 29, 2025 4:38 PM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi認証に向けてのPre-testに関して、酒井様のご要望を基に、

ラボと提案内容について相談しております。

本日は台湾がお休みをいただいておりまして、先週末時点の概案を展開いたします。

本日の遅い時間帯になりますが、もう暫くお待ちいただきますようお願いいたします。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 29, 2025 10:34 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

Pre-test のご検討の状況はいかがでしょうか。

状況を教えていただけると助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 24, 2025 4:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10のWi-Fi認証試験につき、Pre-testのご相談ありがとうございます。

酒井様のお考えをラボに展開いたしまして、

Pre-testへの期待や目的は理解いたしました。

いただいた資料を基に、Pre-test向けのTest Planをご用意いたします。

目標として、9/26（金）までにお送りいたしますので、

少々お待ちいただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 24, 2025 11:39 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

打合せありがとうございました。

私が考えております Pre check の進め方のメモ書きを添付します。

なるべく無駄なく効果的に check を行っていきたいと思っています。

御社でのご経験踏まえて、、 check 実施項目のご提案等いただけますと、大変助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Saturday, September 20, 2025 9:25 AM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

補足説明ありがとうございます。

Wi-Fi認証試験はユーザー立場で、WFAが決めたGoldenSampleとの接続性の確認が多く、

御社でWFAが定めた試験環境でなくても、ユーザー視点で

Wi-Fiの機能確認はできるのではと考えます。

最新の日程表から、御社でSWの確認も行っているようですが、

その状況を参考に、弊社ラボでの事前確認プランを立てようと考えますが、

いかがでしょうか。

宜しくお願いいたしますアリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 6:45 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

私の言葉の選び方が良くなかったです。

「UXC10のSWが不安定」ではなく、「UXC10のSWの品質レベルが不明なので不安」が正しいです。

弊社もV社もWFAテストをする環境を保持しておらず、どの程度 WFAテストできる品質レベルなのか分かっておりません。

従いまして、Pre Testでは、WFAテストできるレベルなのか確認したいです。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 19, 2025 5:32 PM

To: 水野淳也 Junya Mizuno

Subject: Re: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC10のSWが不安定との事ですが、

Labから具体的な症状を確認されております。

例、〇〇操作する時に〇〇不安定の症状がある、〇〇の際に良くリブートかかったりする、等差支えの無い程度でお願いできますと助かります。

よろしくお願い致します。

Outlook
for Android を取得差出人: Jun Wang

送信日時: 金曜日, 9月 19, 2025 2:38:00 午後宛先: Junya Mizuno

件名: RE: 【ALAP】[UXC] Wi-Fi Alliance認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

承知いたしました。

9/22（月）にLabとの相談状況をご報告いたします。

具体的な提案ができるように調整してまいります。

最新日程を踏まえた進め方のすり合わせですが、

9/24（水）09:00〜10:00、 でお願いいたします。

弊社の酒井と王君、2名で参加させていただきます。

よろしければこちらでTeams会議を設定いたしますが、

御社の参加者をお伺いしてよろしいでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 11:01 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

もしも可能であれば、9/22(月)までにご回答もしくは状況のご連絡をいただくことは可能でしょうか？

V社側のSWリリース遅延およびソフト品塾度が問題ではありますが、弊社からV社に具体的なプランを早急に提示、説明していく必要がある状況です。

また、今日中に提示予定の新しい開発日程を基に、一度 BT-SIGとWFAの進め方のすり合わせを再度させていただくことは可能でしょうか？(最大で1時間程度を想定しています)

来週の火曜日は御社はお休みと思いますので(弊社は勤務日です)、来週の月曜日もしくは水曜日の以下どれかの日程でお打ち合わせが可能かご確認をお願いしたいです。

&uuml;
9/22(月) 14:00-15:00

&uuml;
9/24(水) 9:00-10:00

&uuml;
9/24(水) 13:00-15:00

お時間に限りがあれば、V社の次期モデルのBT-SIGとWFA認証についてもお話しさせていただければと考えております。

ご確認をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 11:20 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

相談なので、話してみないとわかりかねますので。

急ぎであれば回答希望納期をいただければそれまでに回答するように調整いたしますが、いかがでしょうか。

SWに関して情報共有させていただきありがとうございます。

今後試験においてFailが出た際のデバッグ作業もV社自力（外部委託？）

で行う予定、承知いたしました。

他社様案件での経験ですが、ソフト完成度が低いと安定的な試験結果を得られず、

トラブルシュートも難航になったり、結果試験期間が倍半年かかった案件もございました。

ということで、弊社としても完成度の高い（量産品同等レベル）製品のご提供をお願いいたしたいです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 7:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

申し訳ございませんが、御社Labにご相談をお願いします。

御社Labより、いつ頃にご回答をいただける予定か、分かっておりましたら教えていただけますか？

今回のV社からリリースされているSWは、WFAテストに対応した素性として受け取っています。

但し、実態を聞くと、V社側でもWFA認証の経験が乏しく、実際にどれだけの品質になっているか(=WFAテストできる状態か)分かっておりません。

V社のSWのバグ修正等は、全てV社で実施します。

弊社側でV社のSWに手を加えることはありません。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 3:26 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記ご相談いただきありがとうございます。

現行SWが不安定な状況にあること、承知いたしました。

ご要望を一度Labに相談いたしますので、

少々お待ちいただきますと幸いです。

参考にさせていただければと存じますが、

今回V社からリリースされるSWは受験用SWでしょうか。

もしくは、Ver0.8（例）として御社にリリースし、その後のバグ修正、完成度アップは御社で行われる、との予定でしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 1:00 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

追加でご相談したいことがあります。

現在、V社よりWFA向けソフトウェアを受領したのですが、完成度に不安がある状況です。

この状態でWFA本試験を開始し、結果として、殆ど何も試験できずに三か月を過ぎてしまうことを恐れています。

従いまして、“WFA本試験を開始できる状態であること”を確認する目的で、事前試験をお願いしたいと考えております。

以下の条件にて、事前試験項目のご提案とお見積りをお願いできないでしょうか？

&uuml;
期間 : 3日〜5日

&uuml;
確認したいこと : WFAの基本となるTest ProgramのGeneral部分がPassできること

&Oslash;
Wi-Fi 4 11n、Wi-Fi 5 11ac、Wi-Fi 6 11axの初期に実行されると想定するコマンド受付確認、接続確認、動作確認等が該当すると考えています。

確認したい内容が具体的ではなく、申し訳ございません。

お手数ですが、一度依頼をご確認いただき、不明点等ありましたらご連絡をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Wednesday, September 17, 2025 4:17 PM

To: 'Jun Wang'

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

再提出は必要ですが、現行CIDの内容をLabに確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

承知しました。

その他の問題点含めて、ご確認、整理をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Model Nameは、製品に張り付けされているラベル等に印字されているNameと一致している必要がある、との理解で合っているでしょうか？

上記ご理解があっています。

合っている場合、Model NameはUXC10になります。

同じModel Nameで電波認証等も取得しています。

承知いたしました。確かにBluetoothの見積依頼書でも「UXC10」とご記載されています。

再度Model Nameを変えてV社からSubmitが必要になる認識で合っているでしょうか？

再提出は必要ですが、現行CIDの内容をLabに確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 3:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご指摘ありがとうございます。

Model Nameは、製品に張り付けされているラベル等に印字されているNameと一致している必要がある、との理解で合っているでしょうか？

合っている場合、Model NameはUXC10になります。

同じModel Nameで電波認証等も取得しています。

この場合、再度Model Nameを変えてV社からSubmitが必要になる認識で合っているでしょうか？

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 12:30 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC] Wi-Fi
Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V社UXCのWi-Fi見積依頼書の更新、ありがとうございます。

Model Nameについて確認させていただきます。

SubmitいただいたCID（[ID]）では、 UXC 1.0、となっていますが、

見積依頼書では UXC10 とご記入されています。

正しくは UXC 1.0 でよろしいでしょうか。

※ WFA Certification Systemの画面よりキャプチャ宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 10:58 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

既にメール等でやりとりしており、ご存じの内容と思いますが、

見積書に以下未記載の箇所がありましたので追記しました。

&uuml;
Submission Category(Flex/Quick/Derivative)

&uuml;
CID number

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 3:08 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

見積依頼書の再送、ありがとうございます。

内容を確認させていただきます。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:58 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

本メールに添付しましたのでご確認をお願いします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 1:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V社より見直しした依頼書も入手しましたので送付させていただきます。

添付はついていないようですが、ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:11 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

CID（[ID]）を基にお見積りを進めていただき、ありがとうございます。

後追いですが、V社より見直しした依頼書も入手しましたので送付させていただきます。

前回、依頼書から変更が入っているSupport Function部分を黄色セルにしました。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:11 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

下記ご連絡をいただきありがとうございます。

V社が本日改めてCID（[ID]）をSubmitされたようです、

Submitされた内容から、Certified b/gが入っていなく、

Certified a/ac/N、Certified 6が対応されることを確認できました。

下記ご連絡いただいた内容で御見積書をご用意いたしますので、

更新でき次第の送付で構いません。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Friday, September 12, 2025 7:38 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

申し訳ありません、今しがた、 Volvo からリストの更新に関する情報がありました。

b
と g
が少し古い規格ですので、申請を削除することを考えているそうです。

急ぎ再提出できるよう推進しますので、お見積りはもう少しお待ちいただけますでしょうか。

よろしくお願いいたします。

酒井

From:
水野淳也 Junya Mizuno

Sent: Friday, September 12, 2025 5:52 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご連絡ありがとうございます。

Test Toolにつきましては、スウェーデン現地法人を介してV社より回答を入手できました。

お見積りに影響は無いのかもしれませんが、取り急ぎTest Tool欄を記入したお見積書を送付させていただきます。

週明けのお見積りをお待ちしております。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 4:58 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

来週中の日程更新、お手数かけますが、よろしくお願いいたします。

見積依頼書に関して、test toolは継続してご確認お願いいたします。

いただいた内容を基に見積書をご用意いたしますので、

週明けにお送りいたします。

よろしくお願いいたします。

Outlook
for Android を取得差出人: Junya Mizuno

送信日時: 金曜日, 9月 12, 2025 2:15:31 午後宛先: Jun Wang

件名: RE: [UXC] Wi-Fi Alliance認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お待たせしてしまっており、申し訳ございません。

昨日、V社より弊社のスウェーデン現地法人を介して、SWがリリースされてきました。

従いまして、現時点でのOpen項目は以下の認識です。

1.
V社SWの動作チェック

2.
V社操作マニュアルの内容チェック

3.
V社からのTest toolの回答入手および見積書の再送

3については、V社にPUSHしつつ、残りのOpen項目については確認を進めます。

来週中に現在の状況を基に、新たに認証計画を更新し、ご提出させていただきます。

何がご不明点、お気づきの点等ありましたらご連絡をお願いします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:45 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Ｖ社UXC1.0のWi-Fi認証について、

8/21にV社からSWのリリースが遅れるとご連絡をいただきましたが、

現時点の状況はいかがでしょうか。

ザックリで構いませんので、共有させていただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Monday, September 8, 2025 9:32 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

Test ToolはV社で記入したSupport Functionによって決まる認識の為、

V社にどのTest Toolを使うのか確認を依頼しております。

少々お待ち下さい。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 5, 2025 11:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Wi-Fi認証御見積依頼書のご記入、ありがとうございます。

Test Toolに関して記入されていないようですが、ご確認いただいてよろしいでしょうか。

Row#67〜72

For testing

WTS(Wi-Fi Test Suite)

Quick Track Tool

Manual

For throuput

WTS(Wi-Fi Test Suite)

IxChariot

iPerf

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 5, 2025 9:10 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi認証見積依頼確認書」の[Support Function Information]欄に対して、V社から回答を入手しました。

お手数ですが、一度ご確認いただき、何か気になる点等ありましたらご指摘をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:24 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご理解いただきありがとうございます。

お手数かけますが、よろしくお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 2, 2025 1:18 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

ご指摘の点は仰る通りと思います。

改めて、認証する試験は何か、仕様するテストツールは何か、それらをどのように接続し、動作させるのか、を段階的に整理するように依頼します。

その上で不明点がある場合には質問を明確にするように依頼します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 2, 2025 9:09 AM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記打ち合わせのご要望ですが、弊社が認証ラボとして、

UXCの設計開発に携わったことがなく、マニュアル作成の支援や相談はご対応できかねますので、打ち合わせに参加してもあまり意味が無いと存じますが、いかが思いますでしょうか。

WTSやQuickTrackをセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程をStep by Stepで記述すればOK、とは伝えてはいます。

弊社からも同じ説明になりますが、それでも分からない、と言われると困りますね。

実際車のユーザーマニュアルなどの作成経験があるのではと思いますが…

Wi-Fiだけでなく、Bluetooth、USB、CarplayやAndroidAutoの認証につき、

内容やレベルは違いはあれども、「マニュアル」作成もあるでしょう。

どうしてもマニュアルの作成が困難な場合、1つご提案ですが、

接続過程をビデオ撮影してご提供いただくことでいかがでしょうか。

よろしくお願いいたします。

Outlook
for Android を取得差出人: Junya Mizuno

送信日時: 月曜日, 9月 1, 2025 10:09:16 午後宛先: Jun Wang

件名: RE: [UXC] Wi-Fi Alliance認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

WFA試験を受けるために、V社にソフトウェアの操作マニュアルの作成を依頼しております。

ALAPからは以下のような目次を目安に作成依頼をしておりますが、V社側でマニュアル作成経験が無く難航しているそうです。

(WTSやQuickTrackをセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程をStep by Stepで記述すればOK、とは伝えてはいます)

- Connection diagram

- How to bring up DUT and Android

- Wi-Fi Test Suite

Configuration

AP test procedure

STA test procedure

- QuickTrack

Configuration

AP test procedure

STA test procedure

- Also, some shell scripts or supplemental information so that test operator doesn’t have any confusion about set up.

※WTSやQuickTrackのどれを使うのかは並行してVolvoへ確認中ですそのような状況の中、V社からマニュアルの内容についてアリオン様とも打合せをさせて教えてほしい、とリクエストを受けました。

打合せは、何を書けばよいか？のQAになると予想します。

お手数ですが打合せのご対応は可能でしょうか？

可能な場合、9/4(木)もしくは9/8(月)の16:00以降でご都合が良い時間を教えていただけないでしょうか？

※両日共にご都合が悪い場合には、ご都合が良い日時を教えていただけますと幸いです。

弊社もHM26のモデル等で経験はあるものの、UXC担当の私などは実経験がある訳では無い為、

御社から未経験のV社を適切にガイドしていただけると助かります。

ご検討をお願い致します。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 29, 2025 1:59 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご確認ありがとうございます。

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

はい、Powerとは送信パワーのことです。

V社ソフトで試験するにあたり、送信パワーを確認する場合には、何を基準に確認をされるのか把握し、

事前にV社に基準を満たすことを確認する必要があると考えて、質問をさせていただきました。

また、Volvo様よりCID（[ID]）を既にご提出されていますが、

6GHz対応となっているため、修正が必要かと思いますので、

一旦弊社よりReturnしてよろしいでしょうか。

はい、6GHzは未対応になる為、Returnで問題ないと考えています。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 29, 2025 1:22 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

「Wi-Fi認証見積依頼確認書」のご返送はもう少し時間かかる状況、

承知いたしました。

試験項目の中で、Powerの強さを確認する試験項目はあるでしょうか？

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

また、Volvo様よりCID（[ID]）を既にご提出されていますが、

6GHz対応となっているため、修正が必要かと思いますので、

一旦弊社よりReturnしてよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, August 29, 2025 1:07 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi認証見積依頼確認書」の提出が遅れており、申し訳ございません。

V社に[Support Function Information]欄の記入を依頼し、受け取りましたが複数確認事項があり、時間を要しています。

申し訳ございませんがもう少々お待ち下さい。

また、Wi-Fi Alliance認証の試験項目に関して、ご確認したいことがあります。

試験項目の中で、Powerの強さを確認する試験項目はあるでしょうか？

試験準備の際に考慮する必要があるか把握する為、ご確認させて下さい。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 22, 2025 1:55 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

「Wi-Fi認証見積依頼確認書」の提出が遅れており、申し訳ございません。

弊社スウェーデン現法を介してV社に[Support Function Information]欄の記入を依頼しております。

記入が完了できましたら直ぐにご送付させていただきます。

またPre-testのアドバイスについても承知しました。

V社のSWリリース状況を確認する中で、Criticalな部分および Pre-test要否についてもV社含めて確認していくようにします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 22, 2025 10:31 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXCのWi-Fi認証試験用SWのリリースが遅れている状況、承知いたしました。

リリース予定について引き続き更新の方よろしくお願いいたします。

先日のメールでお願いいたしました弊社フォームの「Wi-Fi認証見積依頼確認書」へのご記入ですが、

いつ頃ご送付いただけますでしょうか。

御社フォームのWorkSheetをいただいておりますが、VCC Comment、QC Commentも併記されている中、

最終仕様（認証取得のターゲット仕様）が不明確となっているため、

仕様情報の整理としても、見積依頼書へのご記入をお願いいたします。

Per-testに関して、SWリリース時期が不明となっている中、予定が立てられない状況をよく理解いたしました。

3ヵ月プランの中で試験、問題解析/原因究明、デバッグ、再試験、をやり切るのかなりの負荷となります。

打合せでご説明いたしましたようにPre-testは部分試験の実施も対応可能なので、

Criticalな項目のみの事前試験があればフロントローディングができ、本番試験が効率アップし、

L/O日程の確保に繋がりますので、時間的に全く無理でない限り事前試験をお勧めいたします。

またSWのリリース状況を踏まえてご相談いただければと存じますので、

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 11:07 PM

To: Jun Wang

Subject: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

Wi-Fi Alliance向けSoftwareに関して、V社より最新情報が入りました。

残念なことに、Android V適用に向けた対応が難航しており、弊社へのリリース遅延が発生し、現時点ではいつリリースできるか不明との情報を受けております。

弊社としては、遅くても9月中にV社からSoftwareを受け取れるようにPUSHしている状況です。

上記の状況を踏まえまして、Pre-testを実施する時間が確保できない為、

Pre-testは無しで、三か月パックの中で最初の1.5カ月は試験1回目、後半の1.5カ月でNG修正と試験2回目(NG+関連する試験項目)、といった形で進めたいと考えております。

取り急ぎ、現状と弊社の考えをご連絡させていただきました。

また、Wi-Fi Alliance向けSoftwareリリース日程に関し、進展がありましたら直ぐにご連絡させていただきます。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

---

## 4. 2025-11-17 04:52

**From:** Itsuo Sakai
**To:** Shigeyuki Sakai , Toshitaka Mochizuki

アルプスアルパイン酒井様アリオンの酒井です。いつもお世話になっております代わりに、以下2点をご確認していただきたいのですがよろしいでしょうか。
添付資料に従ってDUT筐体を開けて、RFケーブルの接続不良が無いかどうか見ていただけませんでしょうか。
再度、BT Classicの方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

⇒承知しました。再試験は現在スケジュールされている案件の合間の実施となりますことをご理解願います。スケジュールが決まりましたら望月からお知らせします。

以上よろしくお願いいたします。

差出人: Shigeyuki Sakai

送信日時: 2025年11月17日 12:58

宛先: Itsuo Sakai ; Toshitaka Mochizuki

件名: RE: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

酒井様、望月様お世話になります。

アルプスアルパイン酒井です。

詳細のご説明、どうもありがとうございます。

PC – InterLab 間の通信不具合の可能性は低そうであること、分かりました。

代わりに、以下 2 点をご確認していただきたいのですがよろしいでしょうか。

添付資料に従って DUT 筐体を開けて、 RF ケーブルの接続不良が無いかどうか見ていただけませんでしょうか。
再度、 BT Classic の方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

よろしくお願いいたします。

酒井

From: Itsuo Sakai

Sent: Thursday, November 13, 2025 9:42 PM

To: 酒井重之 Shigeyuki Sakai ; Toshitaka Mochizuki

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンの酒井です。いつもお世話になっております。

望月に代わって私から回答いたします。
ログのご提供、ありがとうございました。
一つ確認させてください。

Command: LEReceiverTestv1

Expected: 0x040EXXXXXXXX00
Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？
DUT からは正常に返したのに LE
Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

⇒ InterLab テストシステムでコマンドおよびコマンド応答の上記ログが表示されるのは試験冒頭の「Set DUT in Direct Test Mode」という表題に続く LEReceiverTestv1 コマンド部分で受信したコマンド応答が期待値と異なる場合のみです。このため Q 社アプリでは自動試験で全てのコマンドとコマンド応答をログ表示するものの試験項目の情報がなく、 InterLab

ログは各試験項目の 2402, 2440, [ID] ログに分散し、期待値と異なる場合のみて格納されるため対比するのが困難です。

自動試験に入る前に手動で LEReceiverTestv1 コマンドに対する応答を確認する段階では以下のように期待値の最終 Octed が 00→0C となる事例はありませんでした。さらに TRM 試験では自動試験で期待値と異なるコマンド応答は発生しないため、おそらく Q 社アプリで変換されることはないものと思います。

<InterLab>

15:16:03

Running Serial - HCI LE Receiver Test v1: 1

15:16:04 Sent: 0x011D200100

15:16:04 Expected: 0x040EXXXXXXXX00

15:16:04
Received: 0x040E04011D2000

15:16:04

LE Receiver Test v1: Completed. Result: Success

15:16:07

Running Serial - HCI LE Test End: 1

15:16:14 Sent: 0x011F2000

15:16:14 Expected: 0x040EXXXXXXXX00

15:16:14 Received:
0x040E06011F200C0000

15:16:14 Packets: 0x0000

15:16:14

LE Test End: Completed. Result: Success

<Q 社アプリのログ >

9: 15:12:[ID]
HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x00

10 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

11 15:12:[ID] HCI_Command:0x01 , 0x1f , 0x20 , 0x00 ,

12 15:12:[ID] HCI_Event(1366):0x04 , 0x0e , 0x12 , 0x01 , 0x00 , 0xfc , 0x00 , 0x19 , 0x0c , 0x13 , 0x00 , 0x00 , 0x00 , 0xe6 , 0x38 , 0x01
, 0x02 , 0x10 , 0x02 , 0x0c , 0x40 ,

13 15:12:[ID] HCI_Command: 0x01 , 0x1f , 0x20
, 0x00 ,

14 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x06 , 0x01 , 0x1f , 0x20 , 0x0c , 0x00 , 0x00 ,

酒井さんの懸念を確かめるには、 PC-InterLab 間に RS232 ロガーを設置して送出データを逐一記録後、 Q 社ツールのログと比較することが必要ですが当社ではすでにシリアル通信ロガーあるいは RS232 プロトコルアナライザを持ち合わせておりません。

以上回答いたします。

差出人 : Shigeyuki
Sakai

送信日時 : 2025 年 11 月 13 日
20:26

宛先 : Toshitaka
Mochizuki

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ログのご提供、ありがとうございました。

一つ確認させてください。

Command: LEReceiverTestv1

Sent: 0x011D20010C

Expected: 0x040EXXXXXXXX00

Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？

DUT からは正常に返したのに LE Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

（この Logging にも現れていたかどうか）

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 6:58 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

お待たせいたしました。

RCV ログをお送りいたしますので、こちらの内容の確認、解析をいただけますでしょうか。

Password は追ってお知らせいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 5:01 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

以下連絡いたします。

FTM モード投入後に TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行後、 Q 社アプリの Handshake=DTR に合わせて Interlab の

DTR=True に設定した結果、送信 TRM 系試験項目は実施でき、 1M モードの全 4 項目が Pass しました。

残る受信 RCV 系は不思議なことに DUT が試験セットアップ時の InterLab からの DTM コマンドに正常応答しないために試験 Pass に至りません。

TRM 試験が Pass 完了したということは、 DUT <-> PC <-> InterLb
間の電気的・論理的接続は正常ということになります。しかし RCV コマンドに対する DUT の応答が InterLab に届くものの、期待値通りの正しい応答ではないという症状です。考えられるのは、「DUT 内蔵のテスト FW の不具合で、

Interlabo からの DTM コマンドに正常応答していない」と推測されます。

現在下記 RCV 試験項目を実施中で、明日 Fail ログをまとめて送付いたしますので、お手数ですがそのログとともに V 社経由 Q 社にテストサンプル内の DTM

FW の解析依頼をお願いいたします。

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

以上ご確認どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 6:53 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

種々のご確認、こちらこそ大変恐れ入ります。

PC 側との兼ね合いがあるとのこと承知いたしました。

明日改めてこちらの方法でも確認させていただきます。

台湾作業の前にクリアできればと思います。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, November 12, 2025 6:48 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

（メインで担当中の梅田が今週末まで不在のため、私から回答いたします。窓口がしばしば変わりご迷惑をおかけします。）

色々とご確認ありがとうございます。

解決に至るかどうか分からないのですが、過去遭遇した接続不良時の対応を共有いたします。

そのときは、 Windows PC 側の Port 設定が重複していたようで、異なる IP
Address を DUT に設定し直すことで接続が回復しました。

そのためのマニュアル、マクロ、 bat ファイルをお送りいたします。

マニュアルの BLE measurement procedure (2)
シートをご覧ください。

下記ケーブルが同梱されていたかと思いますが、最初にこのケーブルを使用して DUT の IP
Address を [ID] に変更します。その上で BLE 試験用の接続を行う、というものです。

また、現地確認のご提案もありがとうございます。

上記でも解決が見られなければ御社へ伺うことも検討中です。

お手数おかけしますが、接続の確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 2:55 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

いただいたログからは一旦 Bluetooth-FTM モードに入るとノーマル操作ができなくなり、

TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行して DUT のテスト FW を通常 FW に戻さないと。電源再投入後に通常動作しないと読み取れる可能性があるようだということが判ってきましたので、

こちらではこの点を引き続き確認するよう進めます。

他になにか必要な操作などございましたらご教示お願い申し上げます。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 11:40 AM

To: Shuhei Umeda ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

DUT との接続を一旦すべて外してやり直したり、システムや PC の電源を入れ直したりを何回かやってみましたが、

HCI_Event の受信はできませんでした。

何か他に考えられる状況はございますでしょうか。

状況に応じ、ご来訪でのご確認も可能です。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

HCI_Event が表示されていないということは、 PC から UXC に対して HCI_Command が送信できていないか、

UXC から PC への HCI_Event が受信できていないかになるかと思います。

一度 HCI_Event は受信できていましたので、接続状態を再確認いただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 11, 2025 1:38 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご教示ありがとうございます。

現在確認作業をしておりますが、

本日朝から手順に従い &quot;Bluetooth Test Mode&quot; を再度実行しましたが、昨日はあった &quot;HCI_Event&quot; の行が表示されなくなりました。

どのような原因、確認、復旧手段があるかご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 8:59 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

弊社では InterLab システムを使用したことがないのですが、

LE Direct Mode （Qualcomm Tool）の Log 上は、送信 / 受信ともに正常に動作しているように見えます。

それに対して InterLab システムの画面上は“ Received ”に何も表示が無いので、 InterLab システムは受信ができていないように見えます。

よって、 PC と InterLab 間のケーブルの接続状態を再度ご確認いただけますでしょうか？

また、過去 HM26 モデルでは同じテストシステムで送受信は問題なかったでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, November 10, 2025 5:04 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

下記の DUT との接続で、 InterLab システムとの通信を行おうとしていますが fail となります。

何か確認すべき点や修正すべき点などございましたらご教示いただけますでしょうか。。

InterLab システムとの接続いただきました &quot;Bluetooth Connection Diagram&quot; ( 添付 ) の真ん中の下側の PC の USB ポートと InterLab システムの USB ポートを接続。

使用ケーブル：

[ID] 変換ケーブル⇔ [ID] メス - メスケーブル ( クロス )
⇔ [ID] 変換ケーブル

InterLab システムから &quot;LE Reset&quot; を実行。

QUTS Status App の画面

InterLab システムの画面ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:48 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

情報いただきありがとうございます。

接続できるようになったとのこと承知いたしました。

引き続きよろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:13 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

RF PHY の方ですが、 ご連絡いただいた内容を実行したところ、下記の通り接続できましたのでお知らせします。引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:02 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様承知いたしました。

早速のご対応感謝いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:00 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

本日サンプル発送いたします。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 11:01 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様はい。ディスプレイ部、付属品含めてとなります。

お手数ですが、ご対応よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 10:58 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様ご連絡有難うございます。

一式ということはディスプレイ部、付属品も含めてという認識でよろしいですね。

発送は可能と思いますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 10:53 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT 試験用に弊社から送付しました DUT 一式ですが、

返却いただくこと可能でしょうか？

お手数ですが、ご確認をお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Wednesday, November 5, 2025 8:58 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

QUTS のバージョンは最新になっていますでしょうか？

Qualcomm Package Manager を起動して、” Updates Available ”タブを選択し、

もし最新のバージョンが存在する場合は、最新版をインストールしてみてください。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, November 4, 2025 7:12 PM

To: 'Toshitaka Mochizuki' ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきましてありがとうございます。

QUTS が動作するところまで進んだようで良かったです。

Step7 までは手順書の通り進んでいるのに Step8 で IP アドレスが表示されないということですね。

即答できないのでこちらでも調査してみます。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 6:27 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

現在再確認作業を行っております。

UXC10 の [ID] のセットアップを、いただきました手順書で行っておりますが、

ステップ 8 で、 COM Port のところで IP アドレスを選択するように書いてあるのですが、

下記の通り、 IP アドレスが表示ず選択できません。

どうすれば、 IP アドレスを選択できるようになるかを、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

Qualcomm Package Manager の検索 Window に QUTS を入力すると、該当するツールが絞り込まれると思います。

お試しいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 1:35 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

QUTSStatusApp ですが、 Qualcomm 社のサイトの Software のダウンロードを探しておりますが、複数のパッケージが表示されますが、そのものズバリのものが出てきません。

こちらは何のパッケージに入っているかご教示いただけますでしょうか。

お忙しいところお手数ですが、ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Shuhei
Umeda

送信 : 2025
年 10
月 31
日 ( 金曜日 ) 13:18

宛先 : Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再度ご確認いただきましてありがとうございます。

Qualcomm ID を取得されていること承知いたしました。

ということは、 Qualcomm Package Manager を使用して QUTS のインストールはできそうでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 11:43 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は終日不在としてご迷惑をお掛けいたしました。

以下回答となります。

ご確認どうぞよろしくお願い申し上げます。
もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。
ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、御社が Qualcomm ID をお持ちでないのは確かでしょうか？
基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。
QRCT が使えているので、その認証は Pass していることになります。

⇒先のメールでアリオンは Qualcomm ID を取得していないとお伝えしましたが御社 HM26 案件で営業の王が Qualcomm ID を取得しておりました。大変失礼しました。
使用中の QRCT のバージョンについて教えていただけますでしょうか。

⇒別途調べてお答えします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 10:45 AM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様 / 望月様お世話になっております。アルプスアルパインの梅田です。

ご確認いただきましてありがとうございました。
Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS
Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。
そのため、本日は QRCT を使用して BLE
DTM モードへの移行を試しました。

誤解を招いてしまったかもしれません。

QRCT で QUTS の確認はできません。

QRCT がインストールされているのであれば、 QUTS も一緒にインストールされているのではないか、との推測になります。

Qualcomm 社のダウンローダー上、 QUTS が QRCT にも含まれるような構成になっているためです。

お手数でございますが、再度、以下の Path に QUTSStatusApp.exe があるかどうかご確認いただけますでしょうか？

C:\Program Files (x86)\Qualcomm\QUTSStatusApp\QUTSStatusApp.exe

もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。

ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、

御社が Qualcomm ID をお持ちでないのは確かでしょうか？

基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。

QRCT が使えているので、その認証は Pass していることになります。

使用中の QRCT のバージョンについて教えていただけますでしょうか。

また、御社と Qualcomm との間に契約関係はございますでしょうか？

以上、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 5:14 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様お世話になっております。

アリオンのジェシーです。

ご返信ありがとうございます。

＞現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

現在実施しようとしている試験は BLE Measurement ([ID]) です。

また、ラボに確認したところ、 Bluetooth Measurement (RF) 試験は既に実施完了しまして、テストレポートも先日提出させていただきました。

＞手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

BLE Measurement については、 Step
６マクロの実施（uxc_BLE_FTM_Mode.ttl）まで成功しました。

Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS
Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。

そのため、本日は QRCT を使用して BLE DTM モードへの移行を試しました。

但し、 BLE Measurement の測定手順では QUTS Status App での設定方法が指定されているため、 QRCT の画面上でどのように設定して BLE
DTM モードへ移行すればよいのかが分かりませんでした。そのため、本日再度お問い合わせさせていただきました。

大変恐縮ですが、現状（QUTS Status App 無し）で BLE DTM モードへの移行方法があればお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shuhei Umeda

Sent: Thursday, October 30, 2025 4:28 PM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様お世話になっております。アルプスアルパインの梅田です。

望月様の代理でのご確認ありがとうございます。

Qualcomm ID はお持ちでは無いが、 QRCT のインストールはできた、または QRCT は既にお持ちだったということでしょうか。

QRCT の画面を添付いただきましたので、 QRCT が動いている前提でお話しますが、

添付しました資料は既に展開させていただいている QRCT の動作手順書です。

現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

お手数ですが、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 4:09 PM

To: 酒井重之 Shigeyuki Sakai ;
梅田修平 Shuhei Umeda

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様、

お世話になっております。

アリオンのジェシーです。

ご不便をお掛けして申し訳ございません。

本日望月が社内不在のため、代理にてラボのフィードバックをご連絡いたします。

＞【BLE】

＞御社にて Qualcomm からツールを直接入手することは可能でしょうか？

申し訳ございません。内部で確認したところ、弊社は Qualcomm ID を持っていないため、 Qualcomm からツールを直接入手できないです。

メールでご提示いただいた方法（QRCT の利用）を試しましたが、接続に失敗しました。添付の Screenshot をご参照ください。

確認したところ、 USB ケーブルで制御用 PC に接続していますが、 PC 側で USB デバイスとして認識されていません。

また、 USB Driver.exe は QRCT フォルダ内に存在しないようです。

念のため、「Select USB Driver.exe」ボタンをクリックし、 QC.BluetoothLE_DirectMode.exe を選択して接続を試みましたが、 Failed
device connection と表示されました。

ご確認いただき、 QRCT で DTM モードへ移行する手順をお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shigeyuki Sakai

Sent: Monday, October 27, 2025 1:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

本日、梅田が不在ですので、私からご回答します。

【IOPT】

添付のファイルが過去に Volvo から提供されていたのですが、御社へ提出していなかったと思います。申し訳ありません。

“adb install BlueSPP.apk”

については、 PDF の 3 ページ目に記載されております。

一度ご確認いただけますでしょうか。

【BLE】

御社にて Qualcomm からツールを直接入手することは可能でしょうか？

通常ですと QPM(Qualcomm Package Manager) というツール経由で PC にインストールします。

（そのためツールインストーラーをお渡しすることができないことも背景です）

QUTS は下記 QRCT をインストールすることで一緒に導入されます。

QRCT は Classic の試験でご使用いただいたと思いますので、 QUTS もご確認可能ではと思います。

一度ご確認いただけますでしょうか。

なお、 BLE 試験用にご提供しました手順書の &quot;Notes
on QRCT tools&quot; シートに QRCT のインストールの説明を記載しておりますので、合わせてご確認をお願いいたします。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:31 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

[ID] 試験に関して、メールでいただいている QUTS Status App と Run
Bluetooth LE Direct Mode テストツールがまだご提供いただいていないようです。

ご確認の上、ご提供お願いできますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:07 AM

To: Shuhei Umeda ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

10 月 21 日 19:42 の梅田様からのメールでは、「IOPTTestguide.pdf に記載されている BlueSPP.apk をインストール」という記述がありますが、

こちらで探しておりますが、これら資料をいただいていないようです。

もしお送りいただいているようでしたら、そのメールご送付の日時をお知らせいただけますでしょうか。

また IOPTTestguide.pdf 以外にも関連する試験で必要なファイルがございましたら併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 7:29 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

まずは adb が正常に動作できるようになったとのこと承知いたしました。

こちらかの情報に誤りがありまして申し訳ございませんでした。

また、 SPP の再試験ありがとうございました。

結果を再度 V 社と共有いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 7:02 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

&quot;USB-A 2.0&quot; というラベルの付いたケーブルを使用したところ、 adb
install はできましたが、

再度 SPP のプロファイル試験を実行しましたが、結果は以前と同じでした。

log のファイルを添付いたしますので、ご確認いただけないでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 10:39 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様ご確認いただきありがとうございました。

こちらのケーブルになります。

このケーブル経由で adb 関連のコマンド操作を試してみていただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 9:51 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

添付のケーブルがございましたが、こちらのことでよろしいでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 7:08 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

何度もご確認いただきましてありがとうございます。

再度、 PC と DUT の接続方法を確認させてください。

弊社から送付した DUT ですが、 USB ケーブルが 4 本あったと思います。

DEBUG SAIL

DEBUG HKP

DEBUG MD

以外のもう 1 本のケーブルはございますでしょうか？もしよろしければ写真を撮って送っていただけると助かります。

DEBUG MD とご案内いたしましたが、残りの 1 本が DUT 側の USB 機能として使うもので、

こちらのケーブルでないと adb が動作しない可能性がございます。

お手数をおかけいたしますが、 4 本目のケーブルのご確認をお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

お送りいただきました資料を確認し、 adb shell settings put global development_settings_enabled 1&quot; コマンドを送りましたが、以下のエラーが表示されます。

• error: no devices/emulators found

DUT や PC などで、他に確認すべき点や、設定すべき点がございましたら、ご教示いただけますでしょうか。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 1:19 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

添付ファイルの P.2 に Basic DUT operations が記載されておりますが、

Developer Mode は Enable になっていますでしょうか？

adb shell settings put global development_settings_enabled 1

を実行してから

adb install bluespp.apk

を試してみていただけますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 12:55 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡いただきました &quot;DEBUG MD&quot; の USB ケーブルを PC に接続し、 &quot;adb install
bluespp.apk&quot; を実行したところ、下記のエラーが表示されました。

• adb: connect error for write: no devices/emulator found

また、 &quot;adb devices&quot; コマンドを実行いたしましたが、 &quot;List of attached devices&quot; の下に何も表示されず、認識されていないようです。

PC や DUT で、他に設定する所などがございましたら、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 11:53 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご確認ありがとうございます。

DEBUG MD と PC を接続してください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 11:51 AM

To: Itsuo Sakai ;
梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は不在といたしまして申し訳ございません。

以下確認事項がございますので、

ご回答いただけますでしょうか。

BlueSPP.apk をインストールするには、 DUT の下記の 3 本の USB ケーブルのどれを PC に接続すればよいかご教示ください。

DEBUG SAIL
DEBUG HKP
DEBUG MD

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 5:25 PM

To: Shuhei Umeda ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
Connection Diagram ですが、 RF
PHY Test System を追記したものを準備いたしました。
こちらを参照いただけたらと思います。

⇒ 何度もお手数をお掛けしました。これで RF
PHY 試験の接続系統図が明確になりました。ありがとうございました。

引き続きよろしくお願いいたします。

酒井差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 16:00

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様

Connection Diagram ですが、 RF PHY Test System を追記したものを準備いたしました。

こちらを参照いただけたらと思います。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, October 21, 2025 2:33 PM

To: 'Itsuo Sakai' ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

Operation Manual ですが PDF に変換しました。

こちらをご参照ください。
RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。

使用いたします。

添付の Bluetooth measurement procedure.pdf、 BLE measurement procedure.pdf
を参照ください。

操作手順の中に Ethernet に関する操作がございます。
ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の
USB 接続部分は反映されていないという理解で間違いないでしょうか。

おっしゃるとおりです。 Bluetooth Connection Diagram に反映されておりません。
そうあれば私の最初からの質問であるテストシステムの Serial
over USB
の接続先ですが、それは PC
running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

はい。その理解で合っています。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 1:43 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
RF PHY Test System との接続は以下の図をご参照ください。
DUT と PC
running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。
RF PHY Test System と DUT は RF のみ接続します。

⇒ RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。
そして PC running QDART と RF
PHY Test System は直接 RS232、 GPIB での接続となります。

⇒ HM26 でも同じ図の Q 社マニュアルを使いました。しかし、 DTM モードでは GPIB 経由のコマンドの定義はなく、 Serial
over USB を含む Serial

(UART) 経由でのコマンドが定義されそれに従って DUT を制御しています。

このため DUT と PC および RF
PHY テストシステムは下図のような接続系統図となります。

ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の

USB 接続部分は反映されていないという理解で間違いないでしょうか。

そうあれば私の最初からの質問であるテストシステムの Serial over USB

の接続先ですが、それは PC running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

以上ご確認をお願いします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 12:55

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

RF PHY Test System との接続は以下の図をご参照ください。

DUT と PC running QDART 間は USB
conversion harness を使って USB Serial で接続いたします。

RF PHY Test System と DUT は RF のみ接続します。

そして PC running QDART と RF PHY Test System は直接 RS232、 GPIB での接続となります。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 12:01 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

ご返信ありがとうございます。
制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。
ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

⇒ 図では黄色マーカー部分の一端が PC,
他端が DUT ですが、文面から推測すると下図かと思われますが、正しいでしょうか ?

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 11:40

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。
以上のようにご送付いただいた Connection
Diagram では RF PHY の
DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。

制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。

ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

DUT
– USB conversion harness
– USB Type-A ケーブル – PC
で結線され、 USB Serial として PC と DUT 間の通信が可能となります。

後ほど、 Operation Manual を PDF 化して送付するようにいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, October 20, 2025 7:19 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

先程の質問は私の Excel のバージョンが古いせいか以下の図が表示されたためで、「薄緑線の分岐」とか「薄緑線の上方の接続先」が何のことやらと思われたと思います。お詫びします。

しかし、 RF PHY 試験は認証テストシステム及び簡易なアンリツ

BT テスタでも RF 測定系とは別に、 UART/COM ポート接続が必須で、

HM26 でも下図のように外部 PC ＋ Q 社テストアプリを Bridge にして

DUT<->(Eternet)<->PC<->(Serial over USB)<->RF PHY テスターという接続を行いました。その際の DTM モードマニュアルを添付します。

以上のようにご送付いただいた Connection Diagram では RF
PHY の

DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。ご送付の Connection Diagram はおそらく電波法 /FCC 試験時のオープンループ試験用のものと推測されます。再度 DTM モードのセットアップ方法をご確認ください。

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 20 日 18:35

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様

SPP のレポートの送付ありがとうございました。

内容確認して返信いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 6:17 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

SPP のレポートをお送りいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Monday, October 20, 2025 5:16 PM

To: Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT の再試験の実施ありがとうございました。

SPP についてですが、再試験結果のレポートを送付いただくこと可能でしょうか。

V 社側に連絡して事前条件や SW の差分の有無について確認を依頼したいと思います。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 5:12 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

IOPT 試験について連絡です。

御社からご送付いただいた SPP の PTS レポートと同じ ICS 設定であることを確認して v8.10.2 で再試験を実施しましたところ、 MAP と PBAP は Pass

しましたが SPP は Pass しませんでした。

SPP の PTS 試験では、スタート前に DUT の接続済機器一覧から PTS を削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいた Pass レポートを得られた DUT の SW が当社の DUT

の SW から更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいた SPP の PTS レポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki
Sakai

Sent: Monday, October 20, 2025 1:36 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご返却、どうもありがとうございました。

弊社側での内部データ更新が完了しまして、先ほど望月様宛での発送手続きが完了したところです。

ヤマトお問合せ No : [ID]

併せて、 RF PHY 試験の手順書もお送りします。

ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 1:40 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

承知いたしました。

更新いただいた後、 RF PHY 試験の日本分実施後、台湾での試験向けに発送予定です。

その際に該否判定書と製品仕様書が必要になります。

今回は RF 試験についてはモニタ部分については輸出は必要なかったとおもいます。

また、先日お伝えいたしました、プロファイル（IOPT）試験についてのご修正についてもそちらのサンプルの返送が必要でしたらおしらせください。

以下 RF 試験機の返送になります。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, October 15, 2025 12:56 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

＞ 御社へ一旦サンプルをお返しするという事だったと存じます。

はい、お手数おかけしまして申し訳ありませんが、そのように進めさせてください。

RF 試験用のサンプルは以下の写真が示す DUT のみで大丈夫です。

ご返却の宛先は私でお願いいたします。

福島県いわき市好間工業団地 20-1

アルプスアルパイン株式会社 DC1 設計部酒井重之あと、 BLE
オプション機能の試験のため DUT を台湾に発送されると思いますが、弊社から該非見解書をお出しするということでよろしいでしょうか。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 6:28 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

RF 試験が完了いたしましたが、 RF PHY 試験実施のため御社へ一旦サンプルをお返しするという事だったと存じます。

RF 試験用のサンプルですが、 Full セットでお返ししたほうがよろしいでしょうか。

必要な物のみでよろしければご指定いただければそちらのみお返しいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, October 14, 2025 9:52 AM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきありがとうございました。

RF 試験が合格完了とのこと承知いたしました。

引き続き、 RF PHY の実施、よろしくお願いいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Friday, October 10, 2025 7:35 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様アリオンの酒井です。いつもお世話になっております。

望月に変わり私からお知らせします。

先程 RF 試験が合格完了しましたのでお知らせします。来週 RF
PHY(1M)

を実施し、 Pass 後に台湾ラボへ送って (2M,
Coded) を実施する予定です。

引き続きよろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 10 日 17:38

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

酒井に代わりまして本件返信させていただきます。

まず試験日程のイメージの共有ありがとうございました。

おおよそこれぐらいの日程感で試験が進むこと承知いたしました。

次に、 Bluetooth IOPT 試験の結果のご連絡ありがとうございました。

Fail、 [ID] となった項目についてレポート内容を確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 4:49 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

今回のケースで問題なく試験が進んだ場合は以下の様な時間的イメージとなります。（日本分のみ）

RF： 4 日程度

[ID]： 3 日程度

Profile： 2 日程度状況により途中中断、問題箇所再確認などで時間は大きく変化する場合があります。

ご了承ください。

Bluetooth IOPT 試験について以下エンジニアから報告がございます。

★ ALAP(UXC10) の IOPT 試験で 18 項目中 14 項目は Pass しました。

残る下記項目が Fail、または [ID] となっております。

・ IOPT/MAP/MCE/CGSIT/SFC/[ID]

・ IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVB/SDPR/[ID]

上記の PTS レポート ( ログ付 ) を添付しますので、ご確認および解析をお願いします。特に製品の SDP レコード内容を重点的にご確認ください。

PTS の IXIT の設定で対処できるものはその旨お知しらせください。 FW 改修が必要な場合は改修 FW をご準備ください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 2:20 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご確認どうもありがとうございました。

各試験の想定日数を教えていただく事は可能でしょうか。

問題発生により変化することも承知しておりますので、特に問題無く進んだ場合の日程感で構わないです。

RF ・・・

RF PHY ・・・

IOPT ・・・

RF PHY 試験前の DUT 更新時期や、 IOPT 試験後ディスプレイご返却のタイミングを知っておきたいためです。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 2:08 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

[ID] の方、受け取っております。

RF PHY 試験の方のテストプランも作成いたしました。

DUT サンプルの運用につきましてはご希望通り対応予定です。

何かございましたら改めて連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 1:57 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご確認、どうもありがとうございました。

試験のご対応を引き続きよろしくお願いいたします。

別メールにしてしまいすみませんでしたが、

Questionnaire の更新と DUT 更新対応のご相談をご連絡しておりますので、

そちらもご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 1:10 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

お待たせしております。

その後こちらで試行いたしまして、 RF 試験開始の段階まで進めることができたようです。

ＲＦ試験実施の上何かございましたら随時連絡いたしますのでしばらくお待ちください。

また、ＩＯＰＴ試験の方も動作確認いたしました。

特にこちらも問題ないようです。

取り急ぎ連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, October 9, 2025 6:58 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご指示有難うございます。

昨日連絡いたしました DUT の通信接続ができない問題について、

電流の制限を調整したところその部分につきましては正常に動作することが確認できました。

ただ、その先で確認を要する状況となっておりますので、もう少しはっきりしましたら改めて連絡いたしますので、もうしばらくお待ちいただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Thursday, October 9, 2025 3:18 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

弊社での似た過去事例にもとづき、少しご確認お願いしたい点がございます。

·
Wake_up 端子の GND 接続確認

DUT の Wake_up ラインが電源の GND に接続されていることをご確認お願いします。

接続が外れると DUT が Sleep 動作に入る動きをしますため。

·
電源投入後、 30 秒待機電源投入後、ソフト起動に 30 秒程度時間がかかりますので、それを待ったのち、操作を開始してみていただけますでしょうか。

以上、２点のご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 6:01 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

RF
試験の DUT Setting で以下の現象が起きております。

・「(UXC)AT operation manual_for_BT_rev001.xlsx」内の手順５実施後、「root@lemans:~#」が表示されず、通信接続ができません。

TeraTerm は最新バージョン (5.5.0) を使用しております。

TeraTerm を別のバージョン (5.4.1) で確認しましたが、同様の現象が起こります。

手順 5 実施中にも切断されることがあります。

こちら対策をご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 5:54 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

★ RF PHY は確認中で未記入項目があって Test
Plan は作成できません。

[ID] の未記入（TBD）の項目のご確認状況はいかがでしょうか。

★サンプルは本日到着し、セッティング、動作確認を行っております。

確認結果わかりましたら連絡しますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 9:11 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様立て続けて申し訳ございません。

RF 試験の DUT 操作マニュアルおよび TeraTerm 用マクロを提出します。

ご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 2:54 PM

To: 'Toshitaka Mochizuki'

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

以下、トピックごとにご連絡いたします。

■ DUT list について間違い修正や写真追加等で更新しました。

添付しました 2025/10/07 のもので差し替えをお願いいたします。

■ DUT 機材発送について

RF 試験用と IOPT 試験用の DUT 機材を別々に発送しました。

以下、ヤマトの送り状番号です。

■ [ID] について別メールですが質問事項へのご回答、ありがとうございました。

（現在の記述で問題無いと理解いたしました）

■ IOPT 試験用の DUT 操作マニュアルについて添付の AOSP_Bluetooth_User_Manual_1_0_0.pdf が試験用の DUT 操作マニュアルです。

不明点などありましたら、ご連絡お願いいたします。

■ RF 試験用の DUT 操作マニュアルについて明日を目標に、現在準備中です。

整い次第、お送りいたします。

以上、ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 7, 2025 11:06 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ドキュメントのご送付ありがとうございます。

試験サンプルの接続、操作マニュアルのご提供もお待ちしております。

（可能であれば英文、もしくは中文併記でいただけますと助かります。）

引き続きどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 9:24 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご回答ありがとうございます。

送信データ量が大きくなりすみません。

■機材提出票および DUT list

機材提出票を作成いたしました。

RF DUT 一式の方はのちのち台湾に行く予定のため、 IOPT
DUT とは別で扱えた方が好ましいと思いましたため、そのようにしました。

また、 WFA メールスレッドの方でありました税関対策の意味も込めて DUT
list を作成しました。 RF DUT の接続写真はのちほど載せるようにします。

お気づきの点等ございましたらご連絡ください。

■ [ID]

こちらも作成いたしました。

下記のご確認をよろしくお願いいたします。

Antenna だけの値を持っていないことから、 Cable
Loss も含めた値となります。こちらで構いませんでしょうか？

このケーブルは、製品のアンテナケーブル or 測定用ケーブルどちらになりますでしょうか？添付ファイルには、一旦、測定用ケーブルのロスを書いています。

BLE の試験モード検討中のため、今時点 TBD とさせてください。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 6:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

＞・ RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

★管理を共通にしてよいのであれば、最終的なご提供物を１冊にまとめていただいても問題ございません。必ず数量、それぞれの識別が出来るようにサンプル本体や付属品にラベルなどを貼ってください。

＞・ IOPT 試験は Questionnaire はございますか？

★こちら ICS を既にいただいているので特に Questionnaire は必要ございません。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 4:54 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご指示ありがとうございます。

以下、確認させてください。

·
RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

·
IOPT 試験は Questionnaire はございますか？

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 11:47 AM

To: Misumi Sato ;
酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

先週はお打ち合わせありがとうございました。

Wi-Fi と一旦メールを分けさせていただきます。

Bluetooth サンプルの送り先ですが、当社日本ラボは本メールのフッタにございます望月宛にお送りください。

また、その際には添付の機材提出票をお送りください。

また RF
テストプラン作成のため、添付の [ID] にご記入の上、ご返送いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Misumi Sato

Sent: Friday, October 3, 2025 4:06 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

こちらこそ早速発送手続き着手していただきありがとうございます。

ご発送準備整いましたら、追跡番号とインボイスをご提供いただけますと幸いです。

尚、以前貴社の別部隊の WFA 認証試験をご担当させていただいた際台湾から日本への DUT 返送時に、税関から再輸入免税措置を求められた経験がございます。

その際、製品個々のシリアルナンバーが必要だったため、念のため、 DUT 本体や

Wi-Fi アンテナ等にシリアルナンバーをご設定いただくことをお勧めいたします。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 3:51 PM

To: Misumi Sato ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について佐藤様お世話になります。

アルプスアルパイン酒井です。

早速のご回答、どうもありがとうございます。

来週早々に発送手続き着手する予定です。

よろしくお願いいたします。

酒井

From: Misumi Sato

Sent: Friday, October 3, 2025 3:05 PM

To: 酒井重之 Shigeyuki Sakai ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

午前中の会議ではありがとうございました。

横から失礼いたします。

WFA 試験の DUT の送付先ですが、下記の表に記載させていただきましたので、ご参照お願いいたします。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

追跡番号、インボイスをご連絡その他、何か WFA 試験に関すること、および輸送に関するご質問等ございましたら、お気軽にお問い合わせくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 2:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

PCAT のご確認ありがとうございました。

この内容を踏まえまして、弊社側でどう対応するか確認いたします。

機材の発送について、

·
下記の通り、弊社から送る際の送付先を教えていただけますでしょうか。（間違い等ありましたら修正をお願いいたします）

·
該非判定見解書等の時間かかるものは着手開始したいと思いますので、対応必要事項欄に追記していただけますでしょうか。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

追跡番号、インボイスをご連絡よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, October 3, 2025 12:16 PM

To: 酒井重之 Shigeyuki Sakai ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

会議資料の更新＆共有させていただき、ありがとうございます。

PCAT に関して台湾ラボが HM26 の Wi-Fi 認証試験で利用実績がございます。

ただ、御社別部隊から異なる案件への対応として、

今回 V 社様案件で使用してよいか、バージョンの指定がないか、

使用できない場合、御社からご提供いただけるか、

ご確認いただきますよう、お願いいたします。

※ HM26 の案件で使用した PCAT のバージョン： [ID]

よろしくお願いいたします。

Outlook for Android を取得差出人 : Shigeyuki Sakai

送信日時 : 金曜日 , 10 月 3, 2025 10:59:20
午前宛先 : Jun Wang ;
Toshitaka Mochizuki ; Itsuo Sakai ;
Misumi Sato ; Zakk Shih

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画について各位本日は、打合せをどうもありがとうございました。

更新した資料をお送りします。

‘QA’ シートに、★マーク付きで確認必要事項を書いております。

試験のご対応、引き続きどうぞよろしくお願いいたします。

酒井

-----Original Appointment-----

From: Jun Wang

Sent: Thursday, October 2, 2025 1:10 PM

To: Jun Wang; 酒井重之 Shigeyuki Sakai; Toshitaka Mochizuki; Itsuo Sakai

Subject: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について

When: 2025 年 10 月 3 日金曜日 9:30-10:30
(UTC+09:00) 大阪、札幌、東京

Where: Microsoft Teams 会議アルプスアルパイン酒井様こちらから設定して申し訳ございません。

明日の打ち合わせは少し早めに開始して、 09:30 からでお願いいたします。

時間帯を 09:30 ～ 10:30 に修正し、会議案内を再送いたします。

宜しくお願いいたします。

アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

弊社側関係者に確認いたしまして、下記時間帯でお願いいたします。

10/3 （金） 10:00 ～ 11:00

会議リンクは下記ご参照願います。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
489 106 497 201 8

パスコード :
sR6yD26r

開催者向け :
会議オプション

________________________________________________________________________________

_____________________________________________

From: Jun Wang

Sent: Thursday, October 2, 2025 10:06 AM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

空き時間帯の共有ありがとうございます。

本日は酒井様のお時間が概ね埋まっているようで、

弊社関係者と一旦明日で調整させていただきます。

調整つき次第ご連絡いたしますので少しお待ちください。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Thursday, October 2, 2025 8:42 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご承諾ありがとうございます。

以下に私のカレンダーを貼りました。この白い時間帯でお願いできましたら助かります。

また、時間は 30 分を見込みますが、延長用に 1 時間スロットを頂けたら助かります。

ご確認をよろしくお願いいたします。

＜１０月＞

酒井

From: Jun Wang

Sent: Thursday, October 2, 2025 7:26 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証の Pre-test の正式見積書について、

承知いたしました、ご用意いたします。

機材送付の段取りについての打ち合わせですが、

弊社側関係者に確認いたしますが、

予め酒井様のご都合をお伺いしてもよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, October 1, 2025 6:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご提案どうもありがとうございました。

【アルプスアルパイン様】 V 社 UXC10 の Wi-Fi 認証につきプリテストのご提案 _Update_1001.pdf の内容でお見積書をいただけますでしょうか。

あと、 BT SIG 試験と WFA 試験の DUT 機材発送段取りを考えておりますが、

機材の保管場所がいわきと中国大連に分かれている背景や、少し悩んでいる点があります。（添付ファイル）

この内容を一度打合せさせていただけませんでしょうか。

可能でしたら、打合せの候補日をいただきたいです。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, October 1, 2025 10:59 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi Pre-test の部分試験に関して、

提案資料の P5 に追加いたしました。

基本は本番試験の各対象 Program に関して、 WFA の Test Plan より一部抽出して試験を行う考えです。

ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, September 30, 2025 9:40 AM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

早速ご確認いただきありがとうございます。

部分試験のブレークダウン、

なるべく早めにご報告するように調整してまいりますので、

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Tuesday, September 30, 2025 9:11 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

内容確認しまして、とても良い内容だと考えております。

ご提案どうもありがとうございます。

試験項目ブレークダウンお待ちしております。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Tuesday, September 30, 2025 6:46 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

お待たせいたしました。

UXC10 の Wi-Fi 認証試験をスムーズに進めることができ、

そして目標時期までに認証取得できるように、

プレテストのご提案をいたします。※添付ご参照願います。

部分試験に関して、もう少し試験項目のブレークダウンについてラボと相談しておりまして、もう少しお待ちいただきますと幸いです。

ご検討賜りますようお願いいいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Monday, September 29, 2025 4:38 PM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証に向けての Pre-test に関して、酒井様のご要望を基に、

ラボと提案内容について相談しております。

本日は台湾がお休みをいただいておりまして、先週末時点の概案を展開いたします。

本日の遅い時間帯になりますが、もう暫くお待ちいただきますようお願いいたします。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 29, 2025 10:34 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

Pre-test のご検討の状況はいかがでしょうか。

状況を教えていただけると助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 24, 2025 4:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi 認証試験につき、 Pre-test のご相談ありがとうございます。

酒井様のお考えをラボに展開いたしまして、

Pre-test への期待や目的は理解いたしました。

いただいた資料を基に、 Pre-test 向けの Test Plan をご用意いたします。

目標として、 9/26 （金）までにお送りいたしますので、

少々お待ちいただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 24, 2025 11:39 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

打合せありがとうございました。

私が考えております Pre check の進め方のメモ書きを添付します。

なるべく無駄なく効果的に check を行っていきたいと思っています。

御社でのご経験踏まえて、、 check 実施項目のご提案等いただけますと、大変助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Saturday, September 20, 2025 9:25 AM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

補足説明ありがとうございます。

Wi-Fi 認証試験はユーザー立場で、 WFA が決めた GoldenSample との接続性の確認が多く、

御社で WFA が定めた試験環境でなくても、ユーザー視点で

Wi-Fi の機能確認はできるのではと考えます。

最新の日程表から、御社で SW の確認も行っているようですが、

その状況を参考に、弊社ラボでの事前確認プランを立てようと考えますが、

いかがでしょうか。

宜しくお願いいたしますアリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 6:45 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

私の言葉の選び方が良くなかったです。

「UXC10 の SW が不安定」ではなく、「UXC10 の SW の品質レベルが不明なので不安」が正しいです。

弊社も V 社も WFA テストをする環境を保持しておらず、どの程度 WFA テストできる品質レベルなのか分かっておりません。

従いまして、 Pre Test では、 WFA テストできるレベルなのか確認したいです。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 19, 2025 5:32 PM

To: 水野淳也 Junya Mizuno

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC10 の SW が不安定との事ですが、

Lab から具体的な症状を確認されております。

例、〇〇操作する時に〇〇不安定の症状がある、〇〇の際に良くリブートかかったりする、等差支えの無い程度でお願いできますと助かります。

よろしくお願い致します。

Outlook for Android を取得差出人 : Jun Wang

送信日時 : 金曜日 , 9 月 19, 2025 2:38:00
午後宛先 : Junya Mizuno

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

承知いたしました。

9/22 （月）に Lab との相談状況をご報告いたします。

具体的な提案ができるように調整してまいります。

最新日程を踏まえた進め方のすり合わせですが、

9/24 （水） 09:00 ～ 10:00、 でお願いいたします。

弊社の酒井と王君、 2 名で参加させていただきます。

よろしければこちらで Teams 会議を設定いたしますが、

御社の参加者をお伺いしてよろしいでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 11:01 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

もしも可能であれば、 9/22( 月 ) までにご回答もしくは状況のご連絡をいただくことは可能でしょうか？

V 社側の SW リリース遅延およびソフト品塾度が問題ではありますが、弊社から V 社に具体的なプランを早急に提示、説明していく必要がある状況です。

また、今日中に提示予定の新しい開発日程を基に、一度 [ID] と WFA の進め方のすり合わせを再度させていただくことは可能でしょうか？ ( 最大で 1 時間程度を想定しています )

来週の火曜日は御社はお休みと思いますので ( 弊社は勤務日です )、来週の月曜日もしくは水曜日の以下どれかの日程でお打ち合わせが可能かご確認をお願いしたいです。

ü
9/22( 月 ) 14:00-15:00

ü
9/24( 水 ) 9:00-10:00

ü
9/24( 水 ) 13:00-15:00

お時間に限りがあれば、 V 社の次期モデルの [ID] と WFA 認証についてもお話しさせていただければと考えております。

ご確認をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 11:20 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

相談なので、話してみないとわかりかねますので。

急ぎであれば回答希望納期をいただければそれまでに回答するように調整いたしますが、いかがでしょうか。

SW に関して情報共有させていただきありがとうございます。

今後試験において Fail が出た際のデバッグ作業も V 社自力（外部委託？）

で行う予定、承知いたしました。

他社様案件での経験ですが、ソフト完成度が低いと安定的な試験結果を得られず、

トラブルシュートも難航になったり、結果試験期間が倍半年かかった案件もございました。

ということで、弊社としても完成度の高い（量産品同等レベル）製品のご提供をお願いいたしたいです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 7:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

申し訳ございませんが、御社 Lab にご相談をお願いします。

御社 Lab より、いつ頃にご回答をいただける予定か、分かっておりましたら教えていただけますか？

今回の V 社からリリースされている SW は、 WFA テストに対応した素性として受け取っています。

但し、実態を聞くと、 V 社側でも WFA 認証の経験が乏しく、実際にどれだけの品質になっているか (=WFA テストできる状態か ) 分かっておりません。

V 社の SW のバグ修正等は、全て V 社で実施します。

弊社側で V 社の SW に手を加えることはありません。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 3:26 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記ご相談いただきありがとうございます。

現行 SW が不安定な状況にあること、承知いたしました。

ご要望を一度 Lab に相談いたしますので、

少々お待ちいただきますと幸いです。

参考にさせていただければと存じますが、

今回 V 社からリリースされる SW は受験用 SW でしょうか。

もしくは、 Ver0.8 （例）として御社にリリースし、その後のバグ修正、完成度アップは御社で行われる、との予定でしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 1:00 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

追加でご相談したいことがあります。

現在、 V 社より WFA 向けソフトウェアを受領したのですが、完成度に不安がある状況です。

この状態で WFA 本試験を開始し、結果として、殆ど何も試験できずに三か月を過ぎてしまうことを恐れています。

従いまして、“ WFA 本試験を開始できる状態であること”を確認する目的で、事前試験をお願いしたいと考えております。

以下の条件にて、事前試験項目のご提案とお見積りをお願いできないでしょうか？

ü
期間 : 3 日～ 5 日

ü
確認したいこと : WFA の基本となる Test Program の General 部分が Pass できること

Ø
Wi-Fi 4 11n、 Wi-Fi 5 11ac、 Wi-Fi 6 11ax の初期に実行されると想定するコマンド受付確認、接続確認、動作確認等が該当すると考えています。

確認したい内容が具体的ではなく、申し訳ございません。

お手数ですが、一度依頼をご確認いただき、不明点等ありましたらご連絡をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Wednesday, September 17, 2025 4:17 PM

To: 'Jun Wang'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

承知しました。

その他の問題点含めて、ご確認、整理をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

上記ご理解があっています。

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

承知いたしました。確かに Bluetooth の見積依頼書でも「UXC10」とご記載されています。

再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 3:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご指摘ありがとうございます。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

この場合、再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 12:30 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社 UXC の Wi-Fi 見積依頼書の更新、ありがとうございます。

Model Name について確認させていただきます。

Submit いただいた CID （[ID]）では、 UXC
1.0、となっていますが、

見積依頼書では UXC10 とご記入されています。

正しくは UXC 1.0 でよろしいでしょうか。

※ WFA Certification System の画面よりキャプチャ宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 10:58 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

既にメール等でやりとりしており、ご存じの内容と思いますが、

見積書に以下未記載の箇所がありましたので追記しました。

ü
Submission Category(Flex/Quick/Derivative)

ü
CID number

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 3:08 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

見積依頼書の再送、ありがとうございます。

内容を確認させていただきます。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:58 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

本メールに添付しましたのでご確認をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 1:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社より見直しした依頼書も入手しましたので送付させていただきます。

添付はついていないようですが、ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:11 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

CID （[ID]）を基にお見積りを進めていただき、ありがとうございます。

後追いですが、 V 社より見直しした依頼書も入手しましたので送付させていただきます。

前回、依頼書から変更が入っている Support Function 部分を黄色セルにしました。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:11 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

下記ご連絡をいただきありがとうございます。

V 社が本日改めて CID （[ID]）を Submit されたようです、

Submit された内容から、 Certified b/g が入っていなく、

Certified a/ac/N、 Certified 6 が対応されることを確認できました。

下記ご連絡いただいた内容で御見積書をご用意いたしますので、

更新でき次第の送付で構いません。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Friday, September 12, 2025 7:38 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

申し訳ありません、今しがた、 Volvo からリストの更新に関する情報がありました。

b
と g
が少し古い規格ですので、申請を削除することを考えているそうです。

急ぎ再提出できるよう推進しますので、お見積りはもう少しお待ちいただけますでしょうか。

よろしくお願いいたします。

酒井

From:
水野淳也 Junya Mizuno

Sent: Friday, September 12, 2025 5:52 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご連絡ありがとうございます。

Test Tool につきましては、スウェーデン現地法人を介して V 社より回答を入手できました。

お見積りに影響は無いのかもしれませんが、取り急ぎ Test Tool 欄を記入したお見積書を送付させていただきます。

週明けのお見積りをお待ちしております。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 4:58 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

来週中の日程更新、お手数かけますが、よろしくお願いいたします。

見積依頼書に関して、 test tool は継続してご確認お願いいたします。

いただいた内容を基に見積書をご用意いたしますので、

週明けにお送りいたします。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 金曜日 , 9 月 12, 2025 2:15:31
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お待たせしてしまっており、申し訳ございません。

昨日、 V 社より弊社のスウェーデン現地法人を介して、 SW がリリースされてきました。

従いまして、現時点での Open 項目は以下の認識です。

1.
V 社 SW の動作チェック

2.
V 社操作マニュアルの内容チェック

3.
V 社からの Test tool の回答入手および見積書の再送

3 については、 V 社に PUSH しつつ、残りの Open 項目については確認を進めます。

来週中に現在の状況を基に、新たに認証計画を更新し、ご提出させていただきます。

何がご不明点、お気づきの点等ありましたらご連絡をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:45 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Ｖ社 [ID] の Wi-Fi 認証について、

8/21 に V 社から SW のリリースが遅れるとご連絡をいただきましたが、

現時点の状況はいかがでしょうか。

ザックリで構いませんので、共有させていただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Monday, September 8, 2025 9:32 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

Test Tool は V 社で記入した Support
Function によって決まる認識の為、

V 社にどの Test Tool を使うのか確認を依頼しております。

少々お待ち下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 5, 2025 11:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証御見積依頼書のご記入、ありがとうございます。

Test Tool に関して記入されていないようですが、ご確認いただいてよろしいでしょうか。

Row#67 ～ 72

For testing

WTS(Wi-Fi Test Suite)

Quick Track Tool

Manual

For throuput

WTS(Wi-Fi Test Suite)

IxChariot

iPerf

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 5, 2025 9:10 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の [Support Function Information] 欄に対して、 V 社から回答を入手しました。

お手数ですが、一度ご確認いただき、何か気になる点等ありましたらご指摘をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:24 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご理解いただきありがとうございます。

お手数かけますが、よろしくお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 2, 2025 1:18 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

ご指摘の点は仰る通りと思います。

改めて、認証する試験は何か、仕様するテストツールは何か、それらをどのように接続し、動作させるのか、を段階的に整理するように依頼します。

その上で不明点がある場合には質問を明確にするように依頼します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 2, 2025 9:09 AM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記打ち合わせのご要望ですが、弊社が認証ラボとして、

UXC の設計開発に携わったことがなく、マニュアル作成の支援や相談はご対応できかねますので、打ち合わせに参加してもあまり意味が無いと存じますが、いかが思いますでしょうか。

WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます。

弊社からも同じ説明になりますが、それでも分からない、と言われると困りますね。

実際車のユーザーマニュアルなどの作成経験があるのではと思いますが…

Wi-Fi だけでなく、 Bluetooth、 USB、 Carplay や AndroidAuto の認証につき、

内容やレベルは違いはあれども、「マニュアル」作成もあるでしょう。

どうしてもマニュアルの作成が困難な場合、 1 つご提案ですが、

接続過程をビデオ撮影してご提供いただくことでいかがでしょうか。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 月曜日 , 9 月 1, 2025 10:09:16
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

WFA 試験を受けるために、 V 社にソフトウェアの操作マニュアルの作成を依頼しております。

ALAP からは以下のような目次を目安に作成依頼をしておりますが、 V 社側でマニュアル作成経験が無く難航しているそうです。

(WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます )

- Connection diagram

- How to bring up DUT and Android

- Wi-Fi Test Suite

Configuration

AP test procedure

STA test procedure

- QuickTrack

Configuration

AP test procedure

STA test procedure

- Also, some shell scripts or supplemental information so that test operator doesn ’ t
have any confusion about set up.

※ WTS や QuickTrack のどれを使うのかは並行して Volvo へ確認中ですそのような状況の中、 V 社からマニュアルの内容についてアリオン様とも打合せをさせて教えてほしい、とリクエストを受けました。

打合せは、何を書けばよいか？の QA になると予想します。

お手数ですが打合せのご対応は可能でしょうか？

可能な場合、 9/4( 木 ) もしくは 9/8( 月 ) の 16:00 以降でご都合が良い時間を教えていただけないでしょうか？

※両日共にご都合が悪い場合には、ご都合が良い日時を教えていただけますと幸いです。

弊社も HM26 のモデル等で経験はあるものの、 UXC 担当の私などは実経験がある訳では無い為、

御社から未経験の V 社を適切にガイドしていただけると助かります。

ご検討をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 29, 2025 1:59 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご確認ありがとうございます。

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

はい、 Power とは送信パワーのことです。

V 社ソフトで試験するにあたり、送信パワーを確認する場合には、何を基準に確認をされるのか把握し、

事前に V 社に基準を満たすことを確認する必要があると考えて、質問をさせていただきました。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

はい、 6GHz は未対応になる為、 Return で問題ないと考えています。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 29, 2025 1:22 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

「Wi-Fi 認証見積依頼確認書」のご返送はもう少し時間かかる状況、

承知いたしました。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, August 29, 2025 1:07 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

V 社に [Support Function
Information] 欄の記入を依頼し、受け取りましたが複数確認事項があり、時間を要しています。

申し訳ございませんがもう少々お待ち下さい。

また、 Wi-Fi Alliance 認証の試験項目に関して、ご確認したいことがあります。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

試験準備の際に考慮する必要があるか把握する為、ご確認させて下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 22, 2025 1:55 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

弊社スウェーデン現法を介して V 社に [Support Function Information] 欄の記入を依頼しております。

記入が完了できましたら直ぐにご送付させていただきます。

また Pre-test のアドバイスについても承知しました。

V 社の SW リリース状況を確認する中で、 Critical な部分および Pre-test 要否についても V 社含めて確認していくようにします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 22, 2025 10:31 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC の Wi-Fi 認証試験用 SW のリリースが遅れている状況、承知いたしました。

リリース予定について引き続き更新の方よろしくお願いいたします。

先日のメールでお願いいたしました弊社フォームの「Wi-Fi 認証見積依頼確認書」へのご記入ですが、

いつ頃ご送付いただけますでしょうか。

御社フォームの WorkSheet をいただいておりますが、 VCC Comment、 QC Comment も併記されている中、

最終仕様（認証取得のターゲット仕様）が不明確となっているため、

仕様情報の整理としても、見積依頼書へのご記入をお願いいたします。

Per-test に関して、 SW リリース時期が不明となっている中、予定が立てられない状況をよく理解いたしました。

3 ヵ月プランの中で試験、問題解析 / 原因究明、デバッグ、再試験、をやり切るのかなりの負荷となります。

打合せでご説明いたしましたように Pre-test は部分試験の実施も対応可能なので、

Critical な項目のみの事前試験があればフロントローディングができ、本番試験が効率アップし、

L/O 日程の確保に繋がりますので、時間的に全く無理でない限り事前試験をお勧めいたします。

また SW のリリース状況を踏まえてご相談いただければと存じますので、

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 11:07 PM

To: Jun Wang

Subject: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

Wi-Fi Alliance 向け Software に関して、 V 社より最新情報が入りました。

残念なことに、 Android V 適用に向けた対応が難航しており、弊社へのリリース遅延が発生し、現時点ではいつリリースできるか不明との情報を受けております。

弊社としては、遅くても 9 月中に V 社から Software を受け取れるように PUSH している状況です。

上記の状況を踏まえまして、 Pre-test を実施する時間が確保できない為、

Pre-test は無しで、三か月パックの中で最初の 1.5 カ月は試験 1 回目、後半の 1.5 カ月で NG 修正と試験 2 回目 (NG+ 関連する試験項目 )、といった形で進めたいと考えております。

取り急ぎ、現状と弊社の考えをご連絡させていただきました。

また、 Wi-Fi Alliance 向け Software リリース日程に関し、進展がありましたら直ぐにご連絡させていただきます。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

---

## 5. 2025-12-08 10:53

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki
**Attachments:** Log_RFPHY_RCV_BV-07-C_test1.zip

望月さんお疲れさまです。

コメントを加えましたので以下のように梅田様、酒井様に送信してください。

酒井ーーーーやっと先々週金曜日の状況に戻りました。酒井様の懸念であるQ社ツールと

InterLabテスタ間でデータが化けていないかの試験を行いました。

（今回のRF PHYの試験では、RF系統での受信レベルに関連するFAIL/ERRまで到達する以前のトラブルのため、uPFコネクタ抜挿後のRF再試験は割愛させていただきました。）

RF PHYの受信試験で1周波数のみを実施する「RF PHY/RCV/[ID]」を3回実施して、InterLabのFailログとQ社のログを比較しました結果、3回ともFal/ERR

箇所は異なるものの、InterLabのFailログとQ社のログの内容とは一致しておりました。

以下の1回目のトライアルで、明確にテストサンプルのおかしな挙動が捉えられています。それは＜Q社ツールのログ＞の「6: 18:24:[ID]」の直後にDUT

から応答がなく、約6秒後にInterLabから「7: 18:24:[ID]」に、6と同じコマンドが再送されています。するとDUTは即座に「8: 18:24:59」に「0x04 ,

0x0e , 0x04 , 0x01 , 0x1d , 0x20 , 0x0c」をコマンド応答し、InterLabも同じ値を受信して、コマンド応答の最終バイトが00以外はDUTからのエラー応答を意味しているため、Fail判定しています。

＜Inter LabのFailログ＞

Command: LEReceiverTestv1

Sent: 0x011D200113 → 6, 7 (6のコマンドにDUTが不応答で7が再送された）

Expected: 0x040EXXXXXXXX00

Received: 0x040E04011D200C　→ 8 (一致)

＜Q社ツールのログ＞

0: 18:23:[ID] HCI_Command:0x01 , 0x03 , 0x0c , 0x00 ,

1 18:23:[ID] HCI_Event(1366):0x04 , 0x0e , 0x04 , 0x01 , 0x03 , 0x0c , 0x00 ,

2: 18:23:[ID] HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x00 ,

3 18:23:[ID] HCI_Event(1366):0x04 , 0x0e , 0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

4: 18:24:[ID] HCI_Command:0x01 , 0x03 , 0x0c , 0x00 ,

5 18:24:[ID] HCI_Event(1366):0x04 , 0x0e , 0x5f , 0x01 , 0x0b , 0xfc , 0x00 , 0x00 , 0x26 , 0x58 , 0x00 , 0x00 , 0x30 , 0x00 , 0x68 , 0x09 , 0x70 , 0x00 , 0x01 , 0x1f , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x02 , 0x08 , 0x00 , 0x01 , 0x0f , 0x0f
, 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x60
, 0xea , 0x2c , 0x01 , 0x05 , 0x0f , 0x03 , 0x00 , 0xff , 0x00 , 0x40 , 0x06 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x01 , 0xe8 , 0x03 , 0x14 , 0x14 , 0x00 , 0x00 ,

6: 18:24:[ID] HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

7: 18:24:[ID] HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

8 18:24:[ID] HCI_Event(1366):0x04 , 0x0e , 0x04 , 0x01 , 0x1d , 0x20 , 0x0c ,

当方では上記状況および他の2回のトライアルでFail/ERRがランダムに発生していることから、「DUTは試験中に動作速度が低下する」のではないかと推測しています。御社からV社経由Q社に添付のログと前述の当社コメントを送付してアドバイスを求めてください。

ーーーー差出人: Toshitaka Mochizuki

送信日時: 2025年12月8日 19:09

宛先: Shuhei Umeda ; Shigeyuki Sakai ; Itsuo Sakai

件名: RE: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

試験の方大変お待たせしております。

本日 DUT は DTM モードへの移行に成功し、 RF PHY/RCV/[ID] を 3 回実施いたしました。

しかしながら毎回の Fail の状況が異なっています。

Interlab Solution と Qualcomm tool
のログファイル ( ３回分 ) を別途お送りいたしますので以下の Password にてダウンロードください。

[ パスワード ]

VpUC8+RF

[ パスワード有効期限 ]

[ID] 19:05
まで

[ 送信 ID]

内容ご確認いただき、何かご対策ございましたらお知らせください。

どうぞよろしくお願い申し上げます。

※【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, December 4, 2025 7:08 PM

To: Shuhei Umeda ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

こちらお待たせしており大変申し訳ございません。

使用している PC 環境に問題があるか確認するため、別の

PC に新しく Qualcomm ソフトウェアをインストールし直して接続を試みておりますが、 RF PHY
手順書にある IP アドレスが表示されず、先に進めない状況のようです。

取り急ぎ状況をお知らせいたします。

どうぞよろしくお願い申し上げます。

【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, December 4, 2025 6:19 PM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

RF PHY 試験の状況いかがでしょうか？

ご不明な点などございましたら、ご連絡いただけたらと思います。

引き続き、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Friday, November 28, 2025 6:30 PM

To: Toshitaka Mochizuki ; 酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

試験状況のご連絡ありがとうございます。

状況理解いたしました。

来週も引き続きよろしくお願いいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, November 28, 2025 6:25 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

試験の方お待たせいたしまして申し訳ございません。

RF PHY 実施の手順が複雑で、先週末に全送信系および受信系 1 項目が Pass した状況に現状到達していない状況です。このためまだ酒井様からの追加確認ご依頼の対応着手に至っておりません。

来週引き続きご依頼内容を試行いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Wednesday, November 26, 2025 7:06 PM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

返信いただきましてありがとうございました。

本日作業いただいていること承知いたしました。

ご連絡お待ちしております。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, November 26, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

試験の方お待たせしております。

本日作業しておりまして、 QUTS Status APP の挙動など確認実施中ですが、

まだうまく動作していないようです。

何かお伺いすることございましたら連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Wednesday, November 26, 2025 3:16 PM

To: Shigeyuki Sakai ; Itsuo Sakai ; Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再試験のスケジュールが決まっていましたらご連絡をいただけますでしょうか？

以上、よろしくお願いいたします。

From:
酒井重之 Shigeyuki Sakai

Sent: Monday, November 17, 2025 3:22 PM

To: Itsuo Sakai ; Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

酒井様お世話になります。

アルプスアルパイン酒井です。

＞ 再試験は現在スケジュールされている案件の合間の実施となりますことをご理解願います。スケジュールが決まりましたら望月からお知らせします。

承知いたしました。お手数おかけし恐縮ですが、よろしくお願いいたします。

酒井

From: Itsuo Sakai

Sent: Monday, November 17, 2025 1:53 PM

To: 酒井重之 Shigeyuki Sakai ; Toshitaka Mochizuki

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様アリオンの酒井です。いつもお世話になっております代わりに、以下 2 点をご確認していただきたいのですがよろしいでしょうか。
添付資料に従って DUT 筐体を開けて、 RF ケーブルの接続不良が無いかどうか見ていただけませんでしょうか。
再度、 BT
Classic の方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

⇒ 承知しました。再試験は現在スケジュールされている案件の合間の実施となりますことをご理解願います。スケジュールが決まりましたら望月からお知らせします。

以上よろしくお願いいたします。

差出人 :
Shigeyuki Sakai

送信日時 :
2025 年 11 月 17 日
12:58

宛先 :
Itsuo Sakai ; Toshitaka Mochizuki

件名 :
RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

酒井様、望月様お世話になります。

アルプスアルパイン酒井です。

詳細のご説明、どうもありがとうございます。

PC – InterLab 間の通信不具合の可能性は低そうであること、分かりました。

代わりに、以下 2 点をご確認していただきたいのですがよろしいでしょうか。

·
添付資料に従って DUT 筐体を開けて、 RF ケーブルの接続不良が無いかどうか見ていただけませんでしょうか。

·
再度、 BT Classic の方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

よろしくお願いいたします。

酒井

From: Itsuo Sakai

Sent: Thursday, November 13, 2025 9:42 PM

To: 酒井重之 Shigeyuki Sakai ; Toshitaka Mochizuki

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンの酒井です。いつもお世話になっております。

望月に代わって私から回答いたします。
ログのご提供、ありがとうございました。
一つ確認させてください。

Command: LEReceiverTestv1

Expected: 0x040EXXXXXXXX00
Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？
DUT からは正常に返したのに LE
Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

⇒ InterLab テストシステムでコマンドおよびコマンド応答の上記ログが表示されるのは試験冒頭の「Set DUT in Direct Test Mode」という表題に続く LEReceiverTestv1 コマンド部分で受信したコマンド応答が期待値と異なる場合のみです。このため Q 社アプリでは自動試験で全てのコマンドとコマンド応答をログ表示するものの試験項目の情報がなく、 InterLab

ログは各試験項目の 2402, 2440, [ID] ログに分散し、期待値と異なる場合のみて格納されるため対比するのが困難です。

自動試験に入る前に手動で LEReceiverTestv1 コマンドに対する応答を確認する段階では以下のように期待値の最終 Octed が 00→0C となる事例はありませんでした。さらに TRM 試験では自動試験で期待値と異なるコマンド応答は発生しないため、おそらく Q 社アプリで変換されることはないものと思います。

<InterLab>

15:16:03

Running Serial - HCI LE Receiver Test v1: 1

15:16:04 Sent: 0x011D200100

15:16:04 Expected: 0x040EXXXXXXXX00

15:16:04
Received: 0x040E04011D2000

15:16:04

LE Receiver Test v1: Completed. Result: Success

15:16:07

Running Serial - HCI LE Test End: 1

15:16:14 Sent: 0x011F2000

15:16:14 Expected: 0x040EXXXXXXXX00

15:16:14 Received:
0x040E06011F200C0000

15:16:14 Packets: 0x0000

15:16:14

LE Test End: Completed. Result: Success

<Q 社アプリのログ >

9: 15:12:[ID]
HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x00

10 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

11 15:12:[ID] HCI_Command:0x01 , 0x1f , 0x20 , 0x00 ,

12 15:12:[ID] HCI_Event(1366):0x04 , 0x0e , 0x12 , 0x01 , 0x00 , 0xfc , 0x00 , 0x19 , 0x0c , 0x13 , 0x00 , 0x00 , 0x00 , 0xe6 , 0x38 , 0x01
, 0x02 , 0x10 , 0x02 , 0x0c , 0x40 ,

13 15:12:[ID] HCI_Command: 0x01 , 0x1f ,
0x20 , 0x00 ,

14 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x06 , 0x01 , 0x1f , 0x20 , 0x0c , 0x00 , 0x00 ,

酒井さんの懸念を確かめるには、 PC-InterLab 間に RS232 ロガーを設置して送出データを逐一記録後、 Q 社ツールのログと比較することが必要ですが当社ではすでにシリアル通信ロガーあるいは RS232 プロトコルアナライザを持ち合わせておりません。

以上回答いたします。

差出人 : Shigeyuki
Sakai

送信日時 : 2025 年 11 月 13 日
20:26

宛先 : Toshitaka
Mochizuki

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ログのご提供、ありがとうございました。

一つ確認させてください。

Command: LEReceiverTestv1

Sent: 0x011D20010C

Expected: 0x040EXXXXXXXX00

Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？

DUT からは正常に返したのに LE Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

（この Logging にも現れていたかどうか）

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 6:58 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

お待たせいたしました。

RCV ログをお送りいたしますので、こちらの内容の確認、解析をいただけますでしょうか。

Password は追ってお知らせいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 5:01 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

以下連絡いたします。

FTM モード投入後に TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行後、 Q 社アプリの Handshake=DTR に合わせて Interlab の

DTR=True に設定した結果、送信 TRM 系試験項目は実施でき、 1M モードの全 4 項目が Pass しました。

残る受信 RCV 系は不思議なことに DUT が試験セットアップ時の InterLab からの DTM コマンドに正常応答しないために試験 Pass に至りません。

TRM 試験が Pass 完了したということは、 DUT <-> PC <-> InterLb
間の電気的・論理的接続は正常ということになります。しかし RCV コマンドに対する DUT の応答が InterLab に届くものの、期待値通りの正しい応答ではないという症状です。考えられるのは、「DUT 内蔵のテスト FW の不具合で、

Interlabo からの DTM コマンドに正常応答していない」と推測されます。

現在下記 RCV 試験項目を実施中で、明日 Fail ログをまとめて送付いたしますので、お手数ですがそのログとともに V 社経由 Q 社にテストサンプル内の DTM

FW の解析依頼をお願いいたします。

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

以上ご確認どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 6:53 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

種々のご確認、こちらこそ大変恐れ入ります。

PC 側との兼ね合いがあるとのこと承知いたしました。

明日改めてこちらの方法でも確認させていただきます。

台湾作業の前にクリアできればと思います。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, November 12, 2025 6:48 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

（メインで担当中の梅田が今週末まで不在のため、私から回答いたします。窓口がしばしば変わりご迷惑をおかけします。）

色々とご確認ありがとうございます。

解決に至るかどうか分からないのですが、過去遭遇した接続不良時の対応を共有いたします。

そのときは、 Windows PC 側の Port 設定が重複していたようで、異なる IP
Address を DUT に設定し直すことで接続が回復しました。

そのためのマニュアル、マクロ、 bat ファイルをお送りいたします。

マニュアルの BLE measurement procedure (2)
シートをご覧ください。

下記ケーブルが同梱されていたかと思いますが、最初にこのケーブルを使用して DUT の IP
Address を [ID] に変更します。その上で BLE 試験用の接続を行う、というものです。

また、現地確認のご提案もありがとうございます。

上記でも解決が見られなければ御社へ伺うことも検討中です。

お手数おかけしますが、接続の確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 2:55 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

いただいたログからは一旦 Bluetooth-FTM モードに入るとノーマル操作ができなくなり、

TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行して DUT のテスト FW を通常 FW に戻さないと。電源再投入後に通常動作しないと読み取れる可能性があるようだということが判ってきましたので、

こちらではこの点を引き続き確認するよう進めます。

他になにか必要な操作などございましたらご教示お願い申し上げます。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 11:40 AM

To: Shuhei Umeda ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

DUT との接続を一旦すべて外してやり直したり、システムや PC の電源を入れ直したりを何回かやってみましたが、

HCI_Event の受信はできませんでした。

何か他に考えられる状況はございますでしょうか。

状況に応じ、ご来訪でのご確認も可能です。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

HCI_Event が表示されていないということは、 PC から UXC に対して HCI_Command が送信できていないか、

UXC から PC への HCI_Event が受信できていないかになるかと思います。

一度 HCI_Event は受信できていましたので、接続状態を再確認いただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 11, 2025 1:38 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご教示ありがとうございます。

現在確認作業をしておりますが、

本日朝から手順に従い &quot;Bluetooth Test Mode&quot; を再度実行しましたが、昨日はあった &quot;HCI_Event&quot; の行が表示されなくなりました。

どのような原因、確認、復旧手段があるかご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 8:59 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

弊社では InterLab システムを使用したことがないのですが、

LE Direct Mode （Qualcomm Tool）の Log 上は、送信 / 受信ともに正常に動作しているように見えます。

それに対して InterLab システムの画面上は“ Received ”に何も表示が無いので、 InterLab システムは受信ができていないように見えます。

よって、 PC と InterLab 間のケーブルの接続状態を再度ご確認いただけますでしょうか？

また、過去 HM26 モデルでは同じテストシステムで送受信は問題なかったでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, November 10, 2025 5:04 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

下記の DUT との接続で、 InterLab システムとの通信を行おうとしていますが fail となります。

何か確認すべき点や修正すべき点などございましたらご教示いただけますでしょうか。。

InterLab システムとの接続いただきました &quot;Bluetooth Connection Diagram&quot; ( 添付 ) の真ん中の下側の PC の USB ポートと InterLab システムの USB ポートを接続。

使用ケーブル：

[ID] 変換ケーブル⇔ [ID] メス - メスケーブル ( クロス )
⇔ [ID] 変換ケーブル

InterLab システムから &quot;LE Reset&quot; を実行。

QUTS Status App の画面

InterLab システムの画面ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:48 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

情報いただきありがとうございます。

接続できるようになったとのこと承知いたしました。

引き続きよろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:13 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

RF PHY の方ですが、 ご連絡いただいた内容を実行したところ、下記の通り接続できましたのでお知らせします。引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:02 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様承知いたしました。

早速のご対応感謝いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:00 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

本日サンプル発送いたします。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 11:01 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様はい。ディスプレイ部、付属品含めてとなります。

お手数ですが、ご対応よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 10:58 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様ご連絡有難うございます。

一式ということはディスプレイ部、付属品も含めてという認識でよろしいですね。

発送は可能と思いますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 10:53 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT 試験用に弊社から送付しました DUT 一式ですが、

返却いただくこと可能でしょうか？

お手数ですが、ご確認をお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Wednesday, November 5, 2025 8:58 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

QUTS のバージョンは最新になっていますでしょうか？

Qualcomm Package Manager を起動して、” Updates Available ”タブを選択し、

もし最新のバージョンが存在する場合は、最新版をインストールしてみてください。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, November 4, 2025 7:12 PM

To: 'Toshitaka Mochizuki' ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきましてありがとうございます。

QUTS が動作するところまで進んだようで良かったです。

Step7 までは手順書の通り進んでいるのに Step8 で IP アドレスが表示されないということですね。

即答できないのでこちらでも調査してみます。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 6:27 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

現在再確認作業を行っております。

UXC10 の [ID] のセットアップを、いただきました手順書で行っておりますが、

ステップ 8 で、 COM Port のところで IP アドレスを選択するように書いてあるのですが、

下記の通り、 IP アドレスが表示ず選択できません。

どうすれば、 IP アドレスを選択できるようになるかを、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

Qualcomm Package Manager の検索 Window に QUTS を入力すると、該当するツールが絞り込まれると思います。

お試しいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 1:35 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

QUTSStatusApp ですが、 Qualcomm 社のサイトの Software のダウンロードを探しておりますが、複数のパッケージが表示されますが、そのものズバリのものが出てきません。

こちらは何のパッケージに入っているかご教示いただけますでしょうか。

お忙しいところお手数ですが、ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Shuhei
Umeda

送信 : 2025
年 10
月 31
日 ( 金曜日 ) 13:18

宛先 : Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再度ご確認いただきましてありがとうございます。

Qualcomm ID を取得されていること承知いたしました。

ということは、 Qualcomm Package Manager を使用して QUTS のインストールはできそうでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 11:43 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は終日不在としてご迷惑をお掛けいたしました。

以下回答となります。

ご確認どうぞよろしくお願い申し上げます。
もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。
ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、御社が Qualcomm ID をお持ちでないのは確かでしょうか？
基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。
QRCT が使えているので、その認証は Pass していることになります。

⇒先のメールでアリオンは Qualcomm ID を取得していないとお伝えしましたが御社 HM26 案件で営業の王が Qualcomm ID を取得しておりました。大変失礼しました。
使用中の QRCT のバージョンについて教えていただけますでしょうか。

⇒別途調べてお答えします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 10:45 AM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様 / 望月様お世話になっております。アルプスアルパインの梅田です。

ご確認いただきましてありがとうございました。
Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。
そのため、本日は QRCT を使用して BLE DTM モードへの移行を試しました。

誤解を招いてしまったかもしれません。

QRCT で QUTS の確認はできません。

QRCT がインストールされているのであれば、 QUTS も一緒にインストールされているのではないか、との推測になります。

Qualcomm 社のダウンローダー上、 QUTS が QRCT にも含まれるような構成になっているためです。

お手数でございますが、再度、以下の Path に QUTSStatusApp.exe があるかどうかご確認いただけますでしょうか？

C:\Program Files (x86)\Qualcomm\QUTSStatusApp\QUTSStatusApp.exe

もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。

ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、

御社が Qualcomm ID をお持ちでないのは確かでしょうか？

基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。

QRCT が使えているので、その認証は Pass していることになります。

使用中の QRCT のバージョンについて教えていただけますでしょうか。

また、御社と Qualcomm との間に契約関係はございますでしょうか？

以上、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 5:14 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様お世話になっております。

アリオンのジェシーです。

ご返信ありがとうございます。

＞現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

現在実施しようとしている試験は BLE Measurement ([ID]) です。

また、ラボに確認したところ、 Bluetooth Measurement (RF) 試験は既に実施完了しまして、テストレポートも先日提出させていただきました。

＞手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

BLE Measurement については、 Step
６マクロの実施（uxc_BLE_FTM_Mode.ttl）まで成功しました。

Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。

そのため、本日は QRCT を使用して BLE DTM モードへの移行を試しました。

但し、 BLE Measurement の測定手順では QUTS Status App での設定方法が指定されているため、 QRCT の画面上でどのように設定して BLE
DTM モードへ移行すればよいのかが分かりませんでした。そのため、本日再度お問い合わせさせていただきました。

大変恐縮ですが、現状（QUTS Status App 無し）で BLE DTM モードへの移行方法があればお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shuhei Umeda

Sent: Thursday, October 30, 2025 4:28 PM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様お世話になっております。アルプスアルパインの梅田です。

望月様の代理でのご確認ありがとうございます。

Qualcomm ID はお持ちでは無いが、 QRCT のインストールはできた、または QRCT は既にお持ちだったということでしょうか。

QRCT の画面を添付いただきましたので、 QRCT が動いている前提でお話しますが、

添付しました資料は既に展開させていただいている QRCT の動作手順書です。

現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

お手数ですが、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 4:09 PM

To: 酒井重之 Shigeyuki Sakai ;
梅田修平 Shuhei Umeda

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様、

お世話になっております。

アリオンのジェシーです。

ご不便をお掛けして申し訳ございません。

本日望月が社内不在のため、代理にてラボのフィードバックをご連絡いたします。

＞【BLE】

＞御社にて Qualcomm からツールを直接入手することは可能でしょうか？

申し訳ございません。内部で確認したところ、弊社は Qualcomm ID を持っていないため、 Qualcomm からツールを直接入手できないです。

メールでご提示いただいた方法（QRCT の利用）を試しましたが、接続に失敗しました。添付の Screenshot をご参照ください。

確認したところ、 USB ケーブルで制御用 PC に接続していますが、 PC 側で USB デバイスとして認識されていません。

また、 USB Driver.exe は QRCT フォルダ内に存在しないようです。

念のため、「Select USB Driver.exe」ボタンをクリックし、 QC.BluetoothLE_DirectMode.exe を選択して接続を試みましたが、 Failed device connection と表示されました。

ご確認いただき、 QRCT で DTM モードへ移行する手順をお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shigeyuki Sakai

Sent: Monday, October 27, 2025 1:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

本日、梅田が不在ですので、私からご回答します。

【IOPT】

添付のファイルが過去に Volvo から提供されていたのですが、御社へ提出していなかったと思います。申し訳ありません。

“adb install BlueSPP.apk”

については、 PDF の 3 ページ目に記載されております。

一度ご確認いただけますでしょうか。

【BLE】

御社にて Qualcomm からツールを直接入手することは可能でしょうか？

通常ですと QPM(Qualcomm Package Manager) というツール経由で PC にインストールします。

（そのためツールインストーラーをお渡しすることができないことも背景です）

QUTS は下記 QRCT をインストールすることで一緒に導入されます。

QRCT は Classic の試験でご使用いただいたと思いますので、 QUTS もご確認可能ではと思います。

一度ご確認いただけますでしょうか。

なお、 BLE 試験用にご提供しました手順書の &quot;Notes
on QRCT tools&quot; シートに QRCT のインストールの説明を記載しておりますので、合わせてご確認をお願いいたします。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:31 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

[ID] 試験に関して、メールでいただいている QUTS Status App と Run Bluetooth LE Direct
Mode テストツールがまだご提供いただいていないようです。

ご確認の上、ご提供お願いできますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:07 AM

To: Shuhei Umeda ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

10 月 21 日 19:42 の梅田様からのメールでは、「IOPTTestguide.pdf に記載されている BlueSPP.apk をインストール」という記述がありますが、

こちらで探しておりますが、これら資料をいただいていないようです。

もしお送りいただいているようでしたら、そのメールご送付の日時をお知らせいただけますでしょうか。

また IOPTTestguide.pdf 以外にも関連する試験で必要なファイルがございましたら併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 7:29 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

まずは adb が正常に動作できるようになったとのこと承知いたしました。

こちらかの情報に誤りがありまして申し訳ございませんでした。

また、 SPP の再試験ありがとうございました。

結果を再度 V 社と共有いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 7:02 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

&quot;USB-A 2.0&quot; というラベルの付いたケーブルを使用したところ、 adb install
はできましたが、

再度 SPP のプロファイル試験を実行しましたが、結果は以前と同じでした。

log のファイルを添付いたしますので、ご確認いただけないでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 10:39 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様ご確認いただきありがとうございました。

こちらのケーブルになります。

このケーブル経由で adb 関連のコマンド操作を試してみていただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 9:51 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

添付のケーブルがございましたが、こちらのことでよろしいでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 7:08 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

何度もご確認いただきましてありがとうございます。

再度、 PC と DUT の接続方法を確認させてください。

弊社から送付した DUT ですが、 USB ケーブルが 4 本あったと思います。

DEBUG SAIL

DEBUG HKP

DEBUG MD

以外のもう 1 本のケーブルはございますでしょうか？もしよろしければ写真を撮って送っていただけると助かります。

DEBUG MD とご案内いたしましたが、残りの 1 本が DUT 側の USB 機能として使うもので、

こちらのケーブルでないと adb が動作しない可能性がございます。

お手数をおかけいたしますが、 4 本目のケーブルのご確認をお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

お送りいただきました資料を確認し、 adb shell settings put global development_settings_enabled 1&quot; コマンドを送りましたが、以下のエラーが表示されます。

• error: no devices/emulators found

DUT や PC などで、他に確認すべき点や、設定すべき点がございましたら、ご教示いただけますでしょうか。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 1:19 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

添付ファイルの P.2 に Basic DUT operations が記載されておりますが、

Developer Mode は Enable になっていますでしょうか？

adb shell settings put global development_settings_enabled 1

を実行してから

adb install bluespp.apk

を試してみていただけますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 12:55 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡いただきました &quot;DEBUG MD&quot; の USB ケーブルを PC に接続し、 &quot;adb install bluespp.apk&quot; を実行したところ、下記のエラーが表示されました。

• adb: connect error for write: no devices/emulator found

また、 &quot;adb devices&quot; コマンドを実行いたしましたが、 &quot;List of attached devices&quot; の下に何も表示されず、認識されていないようです。

PC や DUT で、他に設定する所などがございましたら、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 11:53 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご確認ありがとうございます。

DEBUG MD と PC を接続してください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 11:51 AM

To: Itsuo Sakai ;
梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は不在といたしまして申し訳ございません。

以下確認事項がございますので、

ご回答いただけますでしょうか。

BlueSPP.apk をインストールするには、 DUT の下記の 3 本の USB ケーブルのどれを PC に接続すればよいかご教示ください。

DEBUG SAIL
DEBUG HKP
DEBUG MD

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 5:25 PM

To: Shuhei Umeda ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
Connection Diagram ですが、 RF
PHY Test System を追記したものを準備いたしました。
こちらを参照いただけたらと思います。

⇒ 何度もお手数をお掛けしました。これで RF
PHY 試験の接続系統図が明確になりました。ありがとうございました。

引き続きよろしくお願いいたします。

酒井差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 16:00

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様

Connection Diagram ですが、 RF PHY Test System を追記したものを準備いたしました。

こちらを参照いただけたらと思います。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, October 21, 2025 2:33 PM

To: 'Itsuo Sakai' ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

Operation Manual ですが PDF に変換しました。

こちらをご参照ください。
RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。

使用いたします。

添付の Bluetooth measurement procedure.pdf、 BLE measurement procedure.pdf
を参照ください。

操作手順の中に Ethernet に関する操作がございます。
ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の
USB 接続部分は反映されていないという理解で間違いないでしょうか。

おっしゃるとおりです。 Bluetooth Connection Diagram に反映されておりません。
そうあれば私の最初からの質問であるテストシステムの Serial
over USB
の接続先ですが、それは PC
running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

はい。その理解で合っています。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 1:43 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
RF PHY Test System との接続は以下の図をご参照ください。
DUT と PC
running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。
RF PHY Test System と DUT は RF のみ接続します。

⇒ RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。
そして PC running QDART と RF
PHY Test System は直接 RS232、 GPIB での接続となります。

⇒ HM26 でも同じ図の Q 社マニュアルを使いました。しかし、 DTM モードでは GPIB 経由のコマンドの定義はなく、 Serial
over USB を含む Serial

(UART) 経由でのコマンドが定義されそれに従って DUT を制御しています。

このため DUT と PC および RF
PHY テストシステムは下図のような接続系統図となります。

ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の

USB 接続部分は反映されていないという理解で間違いないでしょうか。

そうあれば私の最初からの質問であるテストシステムの Serial over USB

の接続先ですが、それは PC running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

以上ご確認をお願いします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 12:55

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

RF PHY Test System との接続は以下の図をご参照ください。

DUT と PC running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。

RF PHY Test System と DUT は RF のみ接続します。

そして PC running QDART と RF PHY Test System は直接 RS232、 GPIB での接続となります。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 12:01 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

ご返信ありがとうございます。
制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。
ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

⇒ 図では黄色マーカー部分の一端が PC,
他端が DUT ですが、文面から推測すると下図かと思われますが、正しいでしょうか ?

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 11:40

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。
以上のようにご送付いただいた Connection
Diagram では RF PHY の
DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。

制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。

ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

DUT
– USB conversion harness
– USB Type-A ケーブル – PC
で結線され、 USB Serial として PC と DUT 間の通信が可能となります。

後ほど、 Operation Manual を PDF 化して送付するようにいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, October 20, 2025 7:19 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

先程の質問は私の Excel のバージョンが古いせいか以下の図が表示されたためで、「薄緑線の分岐」とか「薄緑線の上方の接続先」が何のことやらと思われたと思います。お詫びします。

しかし、 RF PHY 試験は認証テストシステム及び簡易なアンリツ

BT テスタでも RF 測定系とは別に、 UART/COM ポート接続が必須で、

HM26 でも下図のように外部 PC ＋ Q 社テストアプリを Bridge にして

DUT<->(Eternet)<->PC<->(Serial over USB)<->RF PHY テスターという接続を行いました。その際の DTM モードマニュアルを添付します。

以上のようにご送付いただいた Connection Diagram では RF
PHY の

DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。ご送付の Connection Diagram はおそらく電波法 /FCC 試験時のオープンループ試験用のものと推測されます。再度 DTM モードのセットアップ方法をご確認ください。

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 20 日 18:35

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様

SPP のレポートの送付ありがとうございました。

内容確認して返信いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 6:17 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

SPP のレポートをお送りいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Monday, October 20, 2025 5:16 PM

To: Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT の再試験の実施ありがとうございました。

SPP についてですが、再試験結果のレポートを送付いただくこと可能でしょうか。

V 社側に連絡して事前条件や SW の差分の有無について確認を依頼したいと思います。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 5:12 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

IOPT 試験について連絡です。

御社からご送付いただいた SPP の PTS レポートと同じ ICS 設定であることを確認して v8.10.2 で再試験を実施しましたところ、 MAP と PBAP は Pass

しましたが SPP は Pass しませんでした。

SPP の PTS 試験では、スタート前に DUT の接続済機器一覧から PTS を削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいた Pass レポートを得られた DUT の SW が当社の DUT

の SW から更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいた SPP の PTS レポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki
Sakai

Sent: Monday, October 20, 2025 1:36 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご返却、どうもありがとうございました。

弊社側での内部データ更新が完了しまして、先ほど望月様宛での発送手続きが完了したところです。

ヤマトお問合せ No : [ID]

併せて、 RF PHY 試験の手順書もお送りします。

ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 1:40 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

承知いたしました。

更新いただいた後、 RF PHY 試験の日本分実施後、台湾での試験向けに発送予定です。

その際に該否判定書と製品仕様書が必要になります。

今回は RF 試験についてはモニタ部分については輸出は必要なかったとおもいます。

また、先日お伝えいたしました、プロファイル（IOPT）試験についてのご修正についてもそちらのサンプルの返送が必要でしたらおしらせください。

以下 RF 試験機の返送になります。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, October 15, 2025 12:56 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

＞ 御社へ一旦サンプルをお返しするという事だったと存じます。

はい、お手数おかけしまして申し訳ありませんが、そのように進めさせてください。

RF 試験用のサンプルは以下の写真が示す DUT のみで大丈夫です。

ご返却の宛先は私でお願いいたします。

福島県いわき市好間工業団地 20-1

アルプスアルパイン株式会社 DC1 設計部酒井重之あと、 BLE
オプション機能の試験のため DUT を台湾に発送されると思いますが、弊社から該非見解書をお出しするということでよろしいでしょうか。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 6:28 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

RF 試験が完了いたしましたが、 RF PHY 試験実施のため御社へ一旦サンプルをお返しするという事だったと存じます。

RF 試験用のサンプルですが、 Full セットでお返ししたほうがよろしいでしょうか。

必要な物のみでよろしければご指定いただければそちらのみお返しいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, October 14, 2025 9:52 AM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきありがとうございました。

RF 試験が合格完了とのこと承知いたしました。

引き続き、 RF PHY の実施、よろしくお願いいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Friday, October 10, 2025 7:35 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様アリオンの酒井です。いつもお世話になっております。

望月に変わり私からお知らせします。

先程 RF 試験が合格完了しましたのでお知らせします。来週 RF
PHY(1M)

を実施し、 Pass 後に台湾ラボへ送って (2M,
Coded) を実施する予定です。

引き続きよろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 10 日 17:38

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

酒井に代わりまして本件返信させていただきます。

まず試験日程のイメージの共有ありがとうございました。

おおよそこれぐらいの日程感で試験が進むこと承知いたしました。

次に、 Bluetooth IOPT 試験の結果のご連絡ありがとうございました。

Fail、 [ID] となった項目についてレポート内容を確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 4:49 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

今回のケースで問題なく試験が進んだ場合は以下の様な時間的イメージとなります。（日本分のみ）

RF： 4 日程度

[ID]： 3 日程度

Profile： 2 日程度状況により途中中断、問題箇所再確認などで時間は大きく変化する場合があります。

ご了承ください。

Bluetooth IOPT 試験について以下エンジニアから報告がございます。

★ ALAP(UXC10) の IOPT 試験で 18 項目中 14 項目は Pass しました。

残る下記項目が Fail、または [ID] となっております。

・ IOPT/MAP/MCE/CGSIT/SFC/[ID]

・ IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVB/SDPR/[ID]

上記の PTS レポート ( ログ付 ) を添付しますので、ご確認および解析をお願いします。特に製品の SDP レコード内容を重点的にご確認ください。

PTS の IXIT の設定で対処できるものはその旨お知しらせください。 FW 改修が必要な場合は改修 FW をご準備ください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 2:20 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご確認どうもありがとうございました。

各試験の想定日数を教えていただく事は可能でしょうか。

問題発生により変化することも承知しておりますので、特に問題無く進んだ場合の日程感で構わないです。

RF ・・・

RF PHY ・・・

IOPT ・・・

RF PHY 試験前の DUT 更新時期や、 IOPT 試験後ディスプレイご返却のタイミングを知っておきたいためです。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 2:08 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

[ID] の方、受け取っております。

RF PHY 試験の方のテストプランも作成いたしました。

DUT サンプルの運用につきましてはご希望通り対応予定です。

何かございましたら改めて連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 1:57 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご確認、どうもありがとうございました。

試験のご対応を引き続きよろしくお願いいたします。

別メールにしてしまいすみませんでしたが、

Questionnaire の更新と DUT 更新対応のご相談をご連絡しておりますので、

そちらもご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 1:10 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

お待たせしております。

その後こちらで試行いたしまして、 RF 試験開始の段階まで進めることができたようです。

ＲＦ試験実施の上何かございましたら随時連絡いたしますのでしばらくお待ちください。

また、ＩＯＰＴ試験の方も動作確認いたしました。

特にこちらも問題ないようです。

取り急ぎ連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, October 9, 2025 6:58 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご指示有難うございます。

昨日連絡いたしました DUT の通信接続ができない問題について、

電流の制限を調整したところその部分につきましては正常に動作することが確認できました。

ただ、その先で確認を要する状況となっておりますので、もう少しはっきりしましたら改めて連絡いたしますので、もうしばらくお待ちいただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Thursday, October 9, 2025 3:18 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

弊社での似た過去事例にもとづき、少しご確認お願いしたい点がございます。

·
Wake_up 端子の GND 接続確認

DUT の Wake_up ラインが電源の GND に接続されていることをご確認お願いします。

接続が外れると DUT が Sleep 動作に入る動きをしますため。

·
電源投入後、 30 秒待機電源投入後、ソフト起動に 30 秒程度時間がかかりますので、それを待ったのち、操作を開始してみていただけますでしょうか。

以上、２点のご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 6:01 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

RF
試験の DUT Setting で以下の現象が起きております。

・「(UXC)AT operation manual_for_BT_rev001.xlsx」内の手順５実施後、「root@lemans:~#」が表示されず、通信接続ができません。

TeraTerm は最新バージョン (5.5.0) を使用しております。

TeraTerm を別のバージョン (5.4.1) で確認しましたが、同様の現象が起こります。

手順 5 実施中にも切断されることがあります。

こちら対策をご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 5:54 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

★ RF PHY は確認中で未記入項目があって Test
Plan は作成できません。

[ID] の未記入（TBD）の項目のご確認状況はいかがでしょうか。

★サンプルは本日到着し、セッティング、動作確認を行っております。

確認結果わかりましたら連絡しますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 9:11 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様立て続けて申し訳ございません。

RF 試験の DUT 操作マニュアルおよび TeraTerm 用マクロを提出します。

ご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 2:54 PM

To: 'Toshitaka Mochizuki'

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

以下、トピックごとにご連絡いたします。

■ DUT list について間違い修正や写真追加等で更新しました。

添付しました 2025/10/07 のもので差し替えをお願いいたします。

■ DUT 機材発送について

RF 試験用と IOPT 試験用の DUT 機材を別々に発送しました。

以下、ヤマトの送り状番号です。

■ [ID] について別メールですが質問事項へのご回答、ありがとうございました。

（現在の記述で問題無いと理解いたしました）

■ IOPT 試験用の DUT 操作マニュアルについて添付の AOSP_Bluetooth_User_Manual_1_0_0.pdf が試験用の DUT 操作マニュアルです。

不明点などありましたら、ご連絡お願いいたします。

■ RF 試験用の DUT 操作マニュアルについて明日を目標に、現在準備中です。

整い次第、お送りいたします。

以上、ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 7, 2025 11:06 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ドキュメントのご送付ありがとうございます。

試験サンプルの接続、操作マニュアルのご提供もお待ちしております。

（可能であれば英文、もしくは中文併記でいただけますと助かります。）

引き続きどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 9:24 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご回答ありがとうございます。

送信データ量が大きくなりすみません。

■機材提出票および DUT list

機材提出票を作成いたしました。

RF DUT 一式の方はのちのち台湾に行く予定のため、 IOPT
DUT とは別で扱えた方が好ましいと思いましたため、そのようにしました。

また、 WFA メールスレッドの方でありました税関対策の意味も込めて DUT
list を作成しました。 RF DUT の接続写真はのちほど載せるようにします。

お気づきの点等ございましたらご連絡ください。

■ [ID]

こちらも作成いたしました。

下記のご確認をよろしくお願いいたします。

Antenna だけの値を持っていないことから、 Cable
Loss も含めた値となります。こちらで構いませんでしょうか？

このケーブルは、製品のアンテナケーブル or 測定用ケーブルどちらになりますでしょうか？添付ファイルには、一旦、測定用ケーブルのロスを書いています。

BLE の試験モード検討中のため、今時点 TBD とさせてください。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 6:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

＞・ RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

★管理を共通にしてよいのであれば、最終的なご提供物を１冊にまとめていただいても問題ございません。必ず数量、それぞれの識別が出来るようにサンプル本体や付属品にラベルなどを貼ってください。

＞・ IOPT 試験は Questionnaire はございますか？

★こちら ICS を既にいただいているので特に Questionnaire は必要ございません。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 4:54 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご指示ありがとうございます。

以下、確認させてください。

·
RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

·
IOPT 試験は Questionnaire はございますか？

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 11:47 AM

To: Misumi Sato ;
酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

先週はお打ち合わせありがとうございました。

Wi-Fi と一旦メールを分けさせていただきます。

Bluetooth サンプルの送り先ですが、当社日本ラボは本メールのフッタにございます望月宛にお送りください。

また、その際には添付の機材提出票をお送りください。

また RF
テストプラン作成のため、添付の [ID] にご記入の上、ご返送いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Misumi Sato

Sent: Friday, October 3, 2025 4:06 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

こちらこそ早速発送手続き着手していただきありがとうございます。

ご発送準備整いましたら、追跡番号とインボイスをご提供いただけますと幸いです。

尚、以前貴社の別部隊の WFA 認証試験をご担当させていただいた際台湾から日本への DUT 返送時に、税関から再輸入免税措置を求められた経験がございます。

その際、製品個々のシリアルナンバーが必要だったため、念のため、 DUT 本体や

Wi-Fi アンテナ等にシリアルナンバーをご設定いただくことをお勧めいたします。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 3:51 PM

To: Misumi Sato ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について佐藤様お世話になります。

アルプスアルパイン酒井です。

早速のご回答、どうもありがとうございます。

来週早々に発送手続き着手する予定です。

よろしくお願いいたします。

酒井

From: Misumi Sato

Sent: Friday, October 3, 2025 3:05 PM

To: 酒井重之 Shigeyuki Sakai ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

午前中の会議ではありがとうございました。

横から失礼いたします。

WFA 試験の DUT の送付先ですが、下記の表に記載させていただきましたので、ご参照お願いいたします。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

追跡番号、インボイスをご連絡その他、何か WFA 試験に関すること、および輸送に関するご質問等ございましたら、お気軽にお問い合わせくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 2:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

PCAT のご確認ありがとうございました。

この内容を踏まえまして、弊社側でどう対応するか確認いたします。

機材の発送について、

·
下記の通り、弊社から送る際の送付先を教えていただけますでしょうか。（間違い等ありましたら修正をお願いいたします）

·
該非判定見解書等の時間かかるものは着手開始したいと思いますので、対応必要事項欄に追記していただけますでしょうか。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

追跡番号、インボイスをご連絡よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, October 3, 2025 12:16 PM

To: 酒井重之 Shigeyuki Sakai ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

会議資料の更新＆共有させていただき、ありがとうございます。

PCAT に関して台湾ラボが HM26 の Wi-Fi 認証試験で利用実績がございます。

ただ、御社別部隊から異なる案件への対応として、

今回 V 社様案件で使用してよいか、バージョンの指定がないか、

使用できない場合、御社からご提供いただけるか、

ご確認いただきますよう、お願いいたします。

※ HM26 の案件で使用した PCAT のバージョン： [ID]

よろしくお願いいたします。

Outlook for Android を取得差出人 : Shigeyuki Sakai

送信日時 : 金曜日 , 10 月 3, 2025 10:59:20
午前宛先 : Jun Wang ;
Toshitaka Mochizuki ; Itsuo Sakai ;
Misumi Sato ; Zakk Shih

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画について各位本日は、打合せをどうもありがとうございました。

更新した資料をお送りします。

‘QA’ シートに、★マーク付きで確認必要事項を書いております。

試験のご対応、引き続きどうぞよろしくお願いいたします。

酒井

-----Original Appointment-----

From: Jun Wang

Sent: Thursday, October 2, 2025 1:10 PM

To: Jun Wang; 酒井重之 Shigeyuki Sakai; Toshitaka Mochizuki; Itsuo Sakai

Subject: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について

When: 2025 年 10 月 3 日金曜日 9:30-10:30
(UTC+09:00) 大阪、札幌、東京

Where: Microsoft Teams 会議アルプスアルパイン酒井様こちらから設定して申し訳ございません。

明日の打ち合わせは少し早めに開始して、 09:30 からでお願いいたします。

時間帯を 09:30 ～ 10:30 に修正し、会議案内を再送いたします。

宜しくお願いいたします。

アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

弊社側関係者に確認いたしまして、下記時間帯でお願いいたします。

10/3 （金） 10:00 ～ 11:00

会議リンクは下記ご参照願います。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
489 106 497 201 8

パスコード :
sR6yD26r

開催者向け :
会議オプション

________________________________________________________________________________

_____________________________________________

From: Jun Wang

Sent: Thursday, October 2, 2025 10:06 AM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

空き時間帯の共有ありがとうございます。

本日は酒井様のお時間が概ね埋まっているようで、

弊社関係者と一旦明日で調整させていただきます。

調整つき次第ご連絡いたしますので少しお待ちください。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Thursday, October 2, 2025 8:42 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご承諾ありがとうございます。

以下に私のカレンダーを貼りました。この白い時間帯でお願いできましたら助かります。

また、時間は 30 分を見込みますが、延長用に 1 時間スロットを頂けたら助かります。

ご確認をよろしくお願いいたします。

＜１０月＞

酒井

From: Jun Wang

Sent: Thursday, October 2, 2025 7:26 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証の Pre-test の正式見積書について、

承知いたしました、ご用意いたします。

機材送付の段取りについての打ち合わせですが、

弊社側関係者に確認いたしますが、

予め酒井様のご都合をお伺いしてもよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, October 1, 2025 6:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご提案どうもありがとうございました。

【アルプスアルパイン様】 V 社 UXC10 の Wi-Fi 認証につきプリテストのご提案 _Update_1001.pdf の内容でお見積書をいただけますでしょうか。

あと、 BT SIG 試験と WFA 試験の DUT 機材発送段取りを考えておりますが、

機材の保管場所がいわきと中国大連に分かれている背景や、少し悩んでいる点があります。（添付ファイル）

この内容を一度打合せさせていただけませんでしょうか。

可能でしたら、打合せの候補日をいただきたいです。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, October 1, 2025 10:59 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi Pre-test の部分試験に関して、

提案資料の P5 に追加いたしました。

基本は本番試験の各対象 Program に関して、 WFA の Test Plan より一部抽出して試験を行う考えです。

ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, September 30, 2025 9:40 AM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

早速ご確認いただきありがとうございます。

部分試験のブレークダウン、

なるべく早めにご報告するように調整してまいりますので、

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Tuesday, September 30, 2025 9:11 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

内容確認しまして、とても良い内容だと考えております。

ご提案どうもありがとうございます。

試験項目ブレークダウンお待ちしております。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Tuesday, September 30, 2025 6:46 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

お待たせいたしました。

UXC10 の Wi-Fi 認証試験をスムーズに進めることができ、

そして目標時期までに認証取得できるように、

プレテストのご提案をいたします。※添付ご参照願います。

部分試験に関して、もう少し試験項目のブレークダウンについてラボと相談しておりまして、もう少しお待ちいただきますと幸いです。

ご検討賜りますようお願いいいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Monday, September 29, 2025 4:38 PM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証に向けての Pre-test に関して、酒井様のご要望を基に、

ラボと提案内容について相談しております。

本日は台湾がお休みをいただいておりまして、先週末時点の概案を展開いたします。

本日の遅い時間帯になりますが、もう暫くお待ちいただきますようお願いいたします。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 29, 2025 10:34 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

Pre-test のご検討の状況はいかがでしょうか。

状況を教えていただけると助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 24, 2025 4:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi 認証試験につき、 Pre-test のご相談ありがとうございます。

酒井様のお考えをラボに展開いたしまして、

Pre-test への期待や目的は理解いたしました。

いただいた資料を基に、 Pre-test 向けの Test Plan をご用意いたします。

目標として、 9/26 （金）までにお送りいたしますので、

少々お待ちいただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 24, 2025 11:39 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

打合せありがとうございました。

私が考えております Pre check の進め方のメモ書きを添付します。

なるべく無駄なく効果的に check を行っていきたいと思っています。

御社でのご経験踏まえて、、 check 実施項目のご提案等いただけますと、大変助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Saturday, September 20, 2025 9:25 AM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

補足説明ありがとうございます。

Wi-Fi 認証試験はユーザー立場で、 WFA が決めた GoldenSample との接続性の確認が多く、

御社で WFA が定めた試験環境でなくても、ユーザー視点で

Wi-Fi の機能確認はできるのではと考えます。

最新の日程表から、御社で SW の確認も行っているようですが、

その状況を参考に、弊社ラボでの事前確認プランを立てようと考えますが、

いかがでしょうか。

宜しくお願いいたしますアリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 6:45 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

私の言葉の選び方が良くなかったです。

「UXC10 の SW が不安定」ではなく、「UXC10 の SW の品質レベルが不明なので不安」が正しいです。

弊社も V 社も WFA テストをする環境を保持しておらず、どの程度 WFA テストできる品質レベルなのか分かっておりません。

従いまして、 Pre Test では、 WFA テストできるレベルなのか確認したいです。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 19, 2025 5:32 PM

To: 水野淳也 Junya Mizuno

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC10 の SW が不安定との事ですが、

Lab から具体的な症状を確認されております。

例、〇〇操作する時に〇〇不安定の症状がある、〇〇の際に良くリブートかかったりする、等差支えの無い程度でお願いできますと助かります。

よろしくお願い致します。

Outlook for Android を取得差出人 : Jun Wang

送信日時 : 金曜日 , 9 月 19, 2025 2:38:00
午後宛先 : Junya Mizuno

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

承知いたしました。

9/22 （月）に Lab との相談状況をご報告いたします。

具体的な提案ができるように調整してまいります。

最新日程を踏まえた進め方のすり合わせですが、

9/24 （水） 09:00 ～ 10:00、 でお願いいたします。

弊社の酒井と王君、 2 名で参加させていただきます。

よろしければこちらで Teams 会議を設定いたしますが、

御社の参加者をお伺いしてよろしいでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 11:01 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

もしも可能であれば、 9/22( 月 ) までにご回答もしくは状況のご連絡をいただくことは可能でしょうか？

V 社側の SW リリース遅延およびソフト品塾度が問題ではありますが、弊社から V 社に具体的なプランを早急に提示、説明していく必要がある状況です。

また、今日中に提示予定の新しい開発日程を基に、一度 [ID] と WFA の進め方のすり合わせを再度させていただくことは可能でしょうか？ ( 最大で 1 時間程度を想定しています )

来週の火曜日は御社はお休みと思いますので ( 弊社は勤務日です )、来週の月曜日もしくは水曜日の以下どれかの日程でお打ち合わせが可能かご確認をお願いしたいです。

ü
9/22( 月 ) 14:00-15:00

ü
9/24( 水 ) 9:00-10:00

ü
9/24( 水 ) 13:00-15:00

お時間に限りがあれば、 V 社の次期モデルの [ID] と WFA 認証についてもお話しさせていただければと考えております。

ご確認をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 11:20 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

相談なので、話してみないとわかりかねますので。

急ぎであれば回答希望納期をいただければそれまでに回答するように調整いたしますが、いかがでしょうか。

SW に関して情報共有させていただきありがとうございます。

今後試験において Fail が出た際のデバッグ作業も V 社自力（外部委託？）

で行う予定、承知いたしました。

他社様案件での経験ですが、ソフト完成度が低いと安定的な試験結果を得られず、

トラブルシュートも難航になったり、結果試験期間が倍半年かかった案件もございました。

ということで、弊社としても完成度の高い（量産品同等レベル）製品のご提供をお願いいたしたいです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 7:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

申し訳ございませんが、御社 Lab にご相談をお願いします。

御社 Lab より、いつ頃にご回答をいただける予定か、分かっておりましたら教えていただけますか？

今回の V 社からリリースされている SW は、 WFA テストに対応した素性として受け取っています。

但し、実態を聞くと、 V 社側でも WFA 認証の経験が乏しく、実際にどれだけの品質になっているか (=WFA テストできる状態か ) 分かっておりません。

V 社の SW のバグ修正等は、全て V 社で実施します。

弊社側で V 社の SW に手を加えることはありません。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 3:26 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記ご相談いただきありがとうございます。

現行 SW が不安定な状況にあること、承知いたしました。

ご要望を一度 Lab に相談いたしますので、

少々お待ちいただきますと幸いです。

参考にさせていただければと存じますが、

今回 V 社からリリースされる SW は受験用 SW でしょうか。

もしくは、 Ver0.8 （例）として御社にリリースし、その後のバグ修正、完成度アップは御社で行われる、との予定でしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 1:00 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

追加でご相談したいことがあります。

現在、 V 社より WFA 向けソフトウェアを受領したのですが、完成度に不安がある状況です。

この状態で WFA 本試験を開始し、結果として、殆ど何も試験できずに三か月を過ぎてしまうことを恐れています。

従いまして、“ WFA 本試験を開始できる状態であること”を確認する目的で、事前試験をお願いしたいと考えております。

以下の条件にて、事前試験項目のご提案とお見積りをお願いできないでしょうか？

ü
期間 : 3 日～ 5 日

ü
確認したいこと : WFA の基本となる Test Program の General 部分が Pass できること

Ø
Wi-Fi 4 11n、 Wi-Fi 5 11ac、 Wi-Fi 6 11ax の初期に実行されると想定するコマンド受付確認、接続確認、動作確認等が該当すると考えています。

確認したい内容が具体的ではなく、申し訳ございません。

お手数ですが、一度依頼をご確認いただき、不明点等ありましたらご連絡をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Wednesday, September 17, 2025 4:17 PM

To: 'Jun Wang'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

承知しました。

その他の問題点含めて、ご確認、整理をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

上記ご理解があっています。

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

承知いたしました。確かに Bluetooth の見積依頼書でも「UXC10」とご記載されています。

再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 3:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご指摘ありがとうございます。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

この場合、再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 12:30 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社 UXC の Wi-Fi 見積依頼書の更新、ありがとうございます。

Model Name について確認させていただきます。

Submit いただいた CID （[ID]）では、 UXC
1.0、となっていますが、

見積依頼書では UXC10 とご記入されています。

正しくは UXC 1.0 でよろしいでしょうか。

※ WFA Certification System の画面よりキャプチャ宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 10:58 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

既にメール等でやりとりしており、ご存じの内容と思いますが、

見積書に以下未記載の箇所がありましたので追記しました。

ü
Submission Category(Flex/Quick/Derivative)

ü
CID number

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 3:08 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

見積依頼書の再送、ありがとうございます。

内容を確認させていただきます。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:58 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

本メールに添付しましたのでご確認をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 1:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社より見直しした依頼書も入手しましたので送付させていただきます。

添付はついていないようですが、ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:11 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

CID （[ID]）を基にお見積りを進めていただき、ありがとうございます。

後追いですが、 V 社より見直しした依頼書も入手しましたので送付させていただきます。

前回、依頼書から変更が入っている Support Function 部分を黄色セルにしました。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:11 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

下記ご連絡をいただきありがとうございます。

V 社が本日改めて CID （[ID]）を Submit されたようです、

Submit された内容から、 Certified b/g が入っていなく、

Certified a/ac/N、 Certified 6 が対応されることを確認できました。

下記ご連絡いただいた内容で御見積書をご用意いたしますので、

更新でき次第の送付で構いません。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Friday, September 12, 2025 7:38 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

申し訳ありません、今しがた、 Volvo からリストの更新に関する情報がありました。

b
と g
が少し古い規格ですので、申請を削除することを考えているそうです。

急ぎ再提出できるよう推進しますので、お見積りはもう少しお待ちいただけますでしょうか。

よろしくお願いいたします。

酒井

From:
水野淳也 Junya Mizuno

Sent: Friday, September 12, 2025 5:52 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご連絡ありがとうございます。

Test Tool につきましては、スウェーデン現地法人を介して V 社より回答を入手できました。

お見積りに影響は無いのかもしれませんが、取り急ぎ Test Tool 欄を記入したお見積書を送付させていただきます。

週明けのお見積りをお待ちしております。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 4:58 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

来週中の日程更新、お手数かけますが、よろしくお願いいたします。

見積依頼書に関して、 test tool は継続してご確認お願いいたします。

いただいた内容を基に見積書をご用意いたしますので、

週明けにお送りいたします。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 金曜日 , 9 月 12, 2025 2:15:31
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お待たせしてしまっており、申し訳ございません。

昨日、 V 社より弊社のスウェーデン現地法人を介して、 SW がリリースされてきました。

従いまして、現時点での Open 項目は以下の認識です。

1.
V 社 SW の動作チェック

2.
V 社操作マニュアルの内容チェック

3.
V 社からの Test tool の回答入手および見積書の再送

3 については、 V 社に PUSH しつつ、残りの Open 項目については確認を進めます。

来週中に現在の状況を基に、新たに認証計画を更新し、ご提出させていただきます。

何がご不明点、お気づきの点等ありましたらご連絡をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:45 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Ｖ社 [ID] の Wi-Fi 認証について、

8/21 に V 社から SW のリリースが遅れるとご連絡をいただきましたが、

現時点の状況はいかがでしょうか。

ザックリで構いませんので、共有させていただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Monday, September 8, 2025 9:32 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

Test Tool は V 社で記入した Support
Function によって決まる認識の為、

V 社にどの Test Tool を使うのか確認を依頼しております。

少々お待ち下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 5, 2025 11:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証御見積依頼書のご記入、ありがとうございます。

Test Tool に関して記入されていないようですが、ご確認いただいてよろしいでしょうか。

Row#67 ～ 72

For testing

WTS(Wi-Fi Test Suite)

Quick Track Tool

Manual

For throuput

WTS(Wi-Fi Test Suite)

IxChariot

iPerf

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 5, 2025 9:10 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の [Support Function Information] 欄に対して、 V 社から回答を入手しました。

お手数ですが、一度ご確認いただき、何か気になる点等ありましたらご指摘をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:24 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご理解いただきありがとうございます。

お手数かけますが、よろしくお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 2, 2025 1:18 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

ご指摘の点は仰る通りと思います。

改めて、認証する試験は何か、仕様するテストツールは何か、それらをどのように接続し、動作させるのか、を段階的に整理するように依頼します。

その上で不明点がある場合には質問を明確にするように依頼します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 2, 2025 9:09 AM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記打ち合わせのご要望ですが、弊社が認証ラボとして、

UXC の設計開発に携わったことがなく、マニュアル作成の支援や相談はご対応できかねますので、打ち合わせに参加してもあまり意味が無いと存じますが、いかが思いますでしょうか。

WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます。

弊社からも同じ説明になりますが、それでも分からない、と言われると困りますね。

実際車のユーザーマニュアルなどの作成経験があるのではと思いますが…

Wi-Fi だけでなく、 Bluetooth、 USB、 Carplay や AndroidAuto の認証につき、

内容やレベルは違いはあれども、「マニュアル」作成もあるでしょう。

どうしてもマニュアルの作成が困難な場合、 1 つご提案ですが、

接続過程をビデオ撮影してご提供いただくことでいかがでしょうか。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 月曜日 , 9 月 1, 2025 10:09:16
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

WFA 試験を受けるために、 V 社にソフトウェアの操作マニュアルの作成を依頼しております。

ALAP からは以下のような目次を目安に作成依頼をしておりますが、 V 社側でマニュアル作成経験が無く難航しているそうです。

(WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます )

- Connection diagram

- How to bring up DUT and Android

- Wi-Fi Test Suite

Configuration

AP test procedure

STA test procedure

- QuickTrack

Configuration

AP test procedure

STA test procedure

- Also, some shell scripts or supplemental information so that test operator doesn ’ t
have any confusion about set up.

※ WTS や QuickTrack のどれを使うのかは並行して Volvo へ確認中ですそのような状況の中、 V 社からマニュアルの内容についてアリオン様とも打合せをさせて教えてほしい、とリクエストを受けました。

打合せは、何を書けばよいか？の QA になると予想します。

お手数ですが打合せのご対応は可能でしょうか？

可能な場合、 9/4( 木 ) もしくは 9/8( 月 ) の 16:00 以降でご都合が良い時間を教えていただけないでしょうか？

※両日共にご都合が悪い場合には、ご都合が良い日時を教えていただけますと幸いです。

弊社も HM26 のモデル等で経験はあるものの、 UXC 担当の私などは実経験がある訳では無い為、

御社から未経験の V 社を適切にガイドしていただけると助かります。

ご検討をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 29, 2025 1:59 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご確認ありがとうございます。

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

はい、 Power とは送信パワーのことです。

V 社ソフトで試験するにあたり、送信パワーを確認する場合には、何を基準に確認をされるのか把握し、

事前に V 社に基準を満たすことを確認する必要があると考えて、質問をさせていただきました。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

はい、 6GHz は未対応になる為、 Return で問題ないと考えています。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 29, 2025 1:22 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

「Wi-Fi 認証見積依頼確認書」のご返送はもう少し時間かかる状況、

承知いたしました。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, August 29, 2025 1:07 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

V 社に [Support Function Information] 欄の記入を依頼し、受け取りましたが複数確認事項があり、時間を要しています。

申し訳ございませんがもう少々お待ち下さい。

また、 Wi-Fi Alliance 認証の試験項目に関して、ご確認したいことがあります。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

試験準備の際に考慮する必要があるか把握する為、ご確認させて下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 22, 2025 1:55 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

弊社スウェーデン現法を介して V 社に [Support Function Information] 欄の記入を依頼しております。

記入が完了できましたら直ぐにご送付させていただきます。

また Pre-test のアドバイスについても承知しました。

V 社の SW リリース状況を確認する中で、 Critical な部分および Pre-test 要否についても V 社含めて確認していくようにします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 22, 2025 10:31 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC の Wi-Fi 認証試験用 SW のリリースが遅れている状況、承知いたしました。

リリース予定について引き続き更新の方よろしくお願いいたします。

先日のメールでお願いいたしました弊社フォームの「Wi-Fi 認証見積依頼確認書」へのご記入ですが、

いつ頃ご送付いただけますでしょうか。

御社フォームの WorkSheet をいただいておりますが、 VCC Comment、 QC Comment も併記されている中、

最終仕様（認証取得のターゲット仕様）が不明確となっているため、

仕様情報の整理としても、見積依頼書へのご記入をお願いいたします。

Per-test に関して、 SW リリース時期が不明となっている中、予定が立てられない状況をよく理解いたしました。

3 ヵ月プランの中で試験、問題解析 / 原因究明、デバッグ、再試験、をやり切るのかなりの負荷となります。

打合せでご説明いたしましたように Pre-test は部分試験の実施も対応可能なので、

Critical な項目のみの事前試験があればフロントローディングができ、本番試験が効率アップし、

L/O 日程の確保に繋がりますので、時間的に全く無理でない限り事前試験をお勧めいたします。

また SW のリリース状況を踏まえてご相談いただければと存じますので、

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 11:07 PM

To: Jun Wang

Subject: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

Wi-Fi Alliance 向け Software に関して、 V 社より最新情報が入りました。

残念なことに、 Android V 適用に向けた対応が難航しており、弊社へのリリース遅延が発生し、現時点ではいつリリースできるか不明との情報を受けております。

弊社としては、遅くても 9 月中に V 社から Software を受け取れるように PUSH している状況です。

上記の状況を踏まえまして、 Pre-test を実施する時間が確保できない為、

Pre-test は無しで、三か月パックの中で最初の 1.5 カ月は試験 1 回目、後半の 1.5 カ月で NG 修正と試験 2 回目 (NG+ 関連する試験項目 )、といった形で進めたいと考えております。

取り急ぎ、現状と弊社の考えをご連絡させていただきました。

また、 Wi-Fi Alliance 向け Software リリース日程に関し、進展がありましたら直ぐにご連絡させていただきます。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

---

## 6. 2025-12-11 02:54

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki

望月さんお疲れさまです。

客先から「弊社所有の測定器はInterLabではなくアンリツのMT8852Bになりますが、RF?PHY/RCV/BV?07?Cを再度実施してみましたが、結果はPassでした。」

ということですのでRf PHYの1Mの受信受信試験項目と2Mに試験項目を台湾ラボで実施する提案を行ってはいかがでしょうか。

以下の文面案を望月さんの立場で修正しただいて客先へ返信してください。

ーーーー確認結果について現在Qualcommに問い合わせをしております。

⇒お手数をお掛けしますがよろしくお願いします。
また、弊社所有の測定器はInterLabではなくアンリツのMT8852Bになりますが、
RF/PHY/RCV/[ID]Cを再度実施してみましたが、結果はPassでした。

⇒これまでRF PHYのDTMモードFW開発あるいは動作確認をアンリツのMT8852B

おこなったテストサンプルで、InterLabでは正常にコマンド応答しないもののアンリツのMT8852Bでは試験にPassすることが複数回ありました。

幸い、台湾ラボのSIG認定テストシステムはシグナリングユニットにMT8852B

を用いいているため、過去の類似事例では台湾ラボでRF PHY試験を実施して

Pass結果を得ております。今回御社でMT8852BでのPassを確認頂いているとのことですのでおそらく問題なくPassすることと思います。

御社の同意を頂けましたら早速台湾ラボへの発送を進めますのでご検討の上、ご指示をお願いします。

ーーーー差出人: Shuhei Umeda

送信日時: 2025年12月11日 09:52

宛先: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

件名: RE: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

確認結果について現在 Qualcomm に問い合わせをしております。

また、弊社所有の測定器は InterLab ではなくアンリツの [ID] になりますが、

RF‑PHY/RCV/BV‑07‑C を再度実施してみましたが、結果は Pass でした。

Qualcomm から何か情報などございましたら共有させていただきます。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, December 9, 2025 11:18 AM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご解析有難うございます。

入れ違いで申し訳ございませんんが、

こちらでの確認結果について別途メールをお送りいたしましたので、

そちらもご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

※【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, December 9, 2025 11:11 AM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

試験結果を共有いただきありがとうございました。

Test1 と 2/3 は送信コマンドに差異がありますが、どの試験も最終的に HCI Command に対して

NG(Unsupported Feature or Parameter Value) が返っています。

また、途中で応答が無かったり、意図しないコマンドが DUT から返っていたりするのが気になります。

[Test1]

HCI Reset

0: 18:23:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

OK

1 18:23:[ID] HCI_Event(1366):0x04 , 0x0e , 0x04 , 0x01 ,
0x03 , 0x0c , 0x00 ,

LE Set Default PHY

2: 18:23:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x00 ,

OK

3 18:23:[ID] HCI_Event(1366):0x04 , 0x0e , 0x04 , 0x01 , 0x1d , 0x20 ,
0x00 ,

HCI Reset

4: 18:24:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

Vendor Specific Command(Read Extended Features/Capabilities)

5 18:24:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x5f , 0x01 , 0x0b , 0xfc ,
0x00 , 0x00 , 0x26 , 0x58 , 0x00 , 0x00 , 0x30 , 0x00 , 0x68 , 0x09 , 0x70
, 0x00 , 0x01 , 0x1f , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x02 , 0x08 , 0x00 , 0x01 , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00
, 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x60 , 0xea , 0x2c , 0x01 , 0x05 , 0x0f , 0x03 , 0x00 , 0xff , 0x00 , 0x40 , 0x06 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00
, 0x01 , 0xe8 , 0x03 , 0x14 , 0x14 , 0x00 , 0x00 ,

LE Set Default PHY Command

6: 18:24:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

No Response?

LE Set Default PHY Command

7: 18:24:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

Unsupported Feature or Parameter Value

8 18:24:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x0c ,

[Test2]

HCI Reset

0: 18:28:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

OK

1 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x03 , 0x0c , 0x00 ,

LE Set Default PHY Command

2: 18:28:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

OK

3 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

LE Read Transmit Power Command

4: 18:28:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

OK

5 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x06 , 0x01 , 0x1f , 0x20 , 0x00 , 0xd3 , 0x00 ,

LE Set Default PHY Command

6: 18:28:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

No Response?

LE Set Default PHY Command

7: 18:28:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

Unsupported Feature or Parameter Value

8 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x0c ,

[Test3]

HCI Reset

0: 18:31:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

OK

1 18:31:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x03 , 0x0c , 0x00 ,

LE Set Default PHY Command

2: 18:32:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

OK

3 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

LE Read Transmit Power Command

4: 18:32:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

OK

5 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x06 , 0x01 , 0x1f , 0x20 , 0x00 , 0xa9 ,
0x01 ,

LE Set Default PHY Command

6: 18:32:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

OK

7 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

LE Read Transmit Power Command

8: 18:32:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

Vendor Specific Command(Read Version Info)

9 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x12 , 0x01 , 0x00 , 0xfc ,
0x00 , 0x19 , 0x0c , 0x13 , 0x00 , 0x00 , 0x00 , 0xe6 , 0x38 , 0x01 , 0x02
, 0x10 , 0x02 , 0x0c ,
0x40 ,

LE Read Transmit Power Command

10: 18:32:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

Unsupported Feature or Parameter Value

11 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x06 , 0x01 , 0x1f , 0x20 ,
0x0c , 0x00 , 0x00 ,

Test 手順ですが、以下のコマンドを順に送信する理解で合っていますでしょうか？

1. HCI Reset

2. LE Set Default PHY Command

3. LE Read Transmit Power Command

4. LE Set Default PHY Command

5. LE Read Transmit Power Command

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, December 8, 2025 7:09 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

試験の方大変お待たせしております。

本日 DUT は DTM モードへの移行に成功し、 RF PHY/RCV/[ID] を 3 回実施いたしました。

しかしながら毎回の Fail の状況が異なっています。

Interlab Solution と Qualcomm tool
のログファイル ( ３回分 ) を別途お送りいたしますので以下の Password にてダウンロードください。

[ パスワード ]

VpUC8+RF

[ パスワード有効期限 ]

[ID] 19:05
まで

[ 送信 ID]

内容ご確認いただき、何かご対策ございましたらお知らせください。

どうぞよろしくお願い申し上げます。

※【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, December 4, 2025 7:08 PM

To: Shuhei Umeda ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

こちらお待たせしており大変申し訳ございません。

使用している PC 環境に問題があるか確認するため、別の

PC に新しく Qualcomm ソフトウェアをインストールし直して接続を試みておりますが、 RF PHY
手順書にある IP アドレスが表示されず、先に進めない状況のようです。

取り急ぎ状況をお知らせいたします。

どうぞよろしくお願い申し上げます。

【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, December 4, 2025 6:19 PM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

RF PHY 試験の状況いかがでしょうか？

ご不明な点などございましたら、ご連絡いただけたらと思います。

引き続き、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Friday, November 28, 2025 6:30 PM

To: Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

試験状況のご連絡ありがとうございます。

状況理解いたしました。

来週も引き続きよろしくお願いいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, November 28, 2025 6:25 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

試験の方お待たせいたしまして申し訳ございません。

RF PHY 実施の手順が複雑で、先週末に全送信系および受信系 1 項目が Pass した状況に現状到達していない状況です。このためまだ酒井様からの追加確認ご依頼の対応着手に至っておりません。

来週引き続きご依頼内容を試行いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Wednesday, November 26, 2025 7:06 PM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

返信いただきましてありがとうございました。

本日作業いただいていること承知いたしました。

ご連絡お待ちしております。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, November 26, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

試験の方お待たせしております。

本日作業しておりまして、 QUTS Status APP の挙動など確認実施中ですが、

まだうまく動作していないようです。

何かお伺いすることございましたら連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Wednesday, November 26, 2025 3:16 PM

To: Shigeyuki Sakai ; Itsuo Sakai ; Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再試験のスケジュールが決まっていましたらご連絡をいただけますでしょうか？

以上、よろしくお願いいたします。

From:
酒井重之 Shigeyuki Sakai

Sent: Monday, November 17, 2025 3:22 PM

To: Itsuo Sakai ; Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

酒井様お世話になります。

アルプスアルパイン酒井です。

＞ 再試験は現在スケジュールされている案件の合間の実施となりますことをご理解願います。スケジュールが決まりましたら望月からお知らせします。

承知いたしました。お手数おかけし恐縮ですが、よろしくお願いいたします。

酒井

From: Itsuo Sakai

Sent: Monday, November 17, 2025 1:53 PM

To: 酒井重之 Shigeyuki Sakai ; Toshitaka Mochizuki

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様アリオンの酒井です。いつもお世話になっております代わりに、以下 2 点をご確認していただきたいのですがよろしいでしょうか。
添付資料に従って DUT 筐体を開けて、 RF ケーブルの接続不良が無いかどうか見ていただけませんでしょうか。
再度、 BT
Classic の方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

⇒ 承知しました。再試験は現在スケジュールされている案件の合間の実施となりますことをご理解願います。スケジュールが決まりましたら望月からお知らせします。

以上よろしくお願いいたします。

差出人 :
Shigeyuki Sakai

送信日時 :
2025 年 11 月 17 日
12:58

宛先 :
Itsuo Sakai ; Toshitaka Mochizuki

件名 :
RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

酒井様、望月様お世話になります。

アルプスアルパイン酒井です。

詳細のご説明、どうもありがとうございます。

PC – InterLab 間の通信不具合の可能性は低そうであること、分かりました。

代わりに、以下 2 点をご確認していただきたいのですがよろしいでしょうか。

·
添付資料に従って DUT 筐体を開けて、 RF ケーブルの接続不良が無いかどうか見ていただけませんでしょうか。

·
再度、 BT Classic の方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

よろしくお願いいたします。

酒井

From: Itsuo Sakai

Sent: Thursday, November 13, 2025 9:42 PM

To: 酒井重之 Shigeyuki Sakai ; Toshitaka Mochizuki

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンの酒井です。いつもお世話になっております。

望月に代わって私から回答いたします。
ログのご提供、ありがとうございました。
一つ確認させてください。

Command: LEReceiverTestv1

Expected: 0x040EXXXXXXXX00
Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？
DUT からは正常に返したのに LE
Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

⇒ InterLab テストシステムでコマンドおよびコマンド応答の上記ログが表示されるのは試験冒頭の「Set DUT in Direct Test Mode」という表題に続く LEReceiverTestv1 コマンド部分で受信したコマンド応答が期待値と異なる場合のみです。このため Q 社アプリでは自動試験で全てのコマンドとコマンド応答をログ表示するものの試験項目の情報がなく、 InterLab

ログは各試験項目の 2402, 2440, [ID] ログに分散し、期待値と異なる場合のみて格納されるため対比するのが困難です。

自動試験に入る前に手動で LEReceiverTestv1 コマンドに対する応答を確認する段階では以下のように期待値の最終 Octed が 00→0C となる事例はありませんでした。さらに TRM 試験では自動試験で期待値と異なるコマンド応答は発生しないため、おそらく Q 社アプリで変換されることはないものと思います。

<InterLab>

15:16:03

Running Serial - HCI LE Receiver Test v1: 1

15:16:04 Sent: 0x011D200100

15:16:04 Expected: 0x040EXXXXXXXX00

15:16:04
Received: 0x040E04011D2000

15:16:04

LE Receiver Test v1: Completed. Result: Success

15:16:07

Running Serial - HCI LE Test End: 1

15:16:14 Sent: 0x011F2000

15:16:14 Expected: 0x040EXXXXXXXX00

15:16:14 Received:
0x040E06011F200C0000

15:16:14 Packets: 0x0000

15:16:14

LE Test End: Completed. Result: Success

<Q 社アプリのログ >

9: 15:12:[ID]
HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x00

10 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

11 15:12:[ID] HCI_Command:0x01 , 0x1f , 0x20 , 0x00 ,

12 15:12:[ID] HCI_Event(1366):0x04 , 0x0e , 0x12 , 0x01 , 0x00 , 0xfc , 0x00 , 0x19 , 0x0c , 0x13 , 0x00 , 0x00 , 0x00 , 0xe6 , 0x38 , 0x01
, 0x02 , 0x10 , 0x02 , 0x0c , 0x40 ,

13 15:12:[ID] HCI_Command: 0x01 , 0x1f ,
0x20 , 0x00 ,

14 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x06 , 0x01 , 0x1f , 0x20 , 0x0c , 0x00 , 0x00 ,

酒井さんの懸念を確かめるには、 PC-InterLab 間に RS232 ロガーを設置して送出データを逐一記録後、 Q 社ツールのログと比較することが必要ですが当社ではすでにシリアル通信ロガーあるいは RS232 プロトコルアナライザを持ち合わせておりません。

以上回答いたします。

差出人 : Shigeyuki
Sakai

送信日時 : 2025 年 11 月 13 日
20:26

宛先 : Toshitaka
Mochizuki

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ログのご提供、ありがとうございました。

一つ確認させてください。

Command: LEReceiverTestv1

Sent: 0x011D20010C

Expected: 0x040EXXXXXXXX00

Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？

DUT からは正常に返したのに LE Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

（この Logging にも現れていたかどうか）

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 6:58 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

お待たせいたしました。

RCV ログをお送りいたしますので、こちらの内容の確認、解析をいただけますでしょうか。

Password は追ってお知らせいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 5:01 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

以下連絡いたします。

FTM モード投入後に TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行後、 Q 社アプリの Handshake=DTR に合わせて Interlab の

DTR=True に設定した結果、送信 TRM 系試験項目は実施でき、 1M モードの全 4 項目が Pass しました。

残る受信 RCV 系は不思議なことに DUT が試験セットアップ時の InterLab からの DTM コマンドに正常応答しないために試験 Pass に至りません。

TRM 試験が Pass 完了したということは、 DUT <-> PC <-> InterLb
間の電気的・論理的接続は正常ということになります。しかし RCV コマンドに対する DUT の応答が InterLab に届くものの、期待値通りの正しい応答ではないという症状です。考えられるのは、「DUT 内蔵のテスト FW の不具合で、

Interlabo からの DTM コマンドに正常応答していない」と推測されます。

現在下記 RCV 試験項目を実施中で、明日 Fail ログをまとめて送付いたしますので、お手数ですがそのログとともに V 社経由 Q 社にテストサンプル内の DTM

FW の解析依頼をお願いいたします。

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

以上ご確認どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 6:53 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

種々のご確認、こちらこそ大変恐れ入ります。

PC 側との兼ね合いがあるとのこと承知いたしました。

明日改めてこちらの方法でも確認させていただきます。

台湾作業の前にクリアできればと思います。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, November 12, 2025 6:48 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

（メインで担当中の梅田が今週末まで不在のため、私から回答いたします。窓口がしばしば変わりご迷惑をおかけします。）

色々とご確認ありがとうございます。

解決に至るかどうか分からないのですが、過去遭遇した接続不良時の対応を共有いたします。

そのときは、 Windows PC 側の Port 設定が重複していたようで、異なる IP
Address を DUT に設定し直すことで接続が回復しました。

そのためのマニュアル、マクロ、 bat ファイルをお送りいたします。

マニュアルの BLE measurement procedure (2)
シートをご覧ください。

下記ケーブルが同梱されていたかと思いますが、最初にこのケーブルを使用して DUT の IP
Address を [ID] に変更します。その上で BLE 試験用の接続を行う、というものです。

また、現地確認のご提案もありがとうございます。

上記でも解決が見られなければ御社へ伺うことも検討中です。

お手数おかけしますが、接続の確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 2:55 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

いただいたログからは一旦 Bluetooth-FTM モードに入るとノーマル操作ができなくなり、

TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行して DUT のテスト FW を通常 FW に戻さないと。電源再投入後に通常動作しないと読み取れる可能性があるようだということが判ってきましたので、

こちらではこの点を引き続き確認するよう進めます。

他になにか必要な操作などございましたらご教示お願い申し上げます。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 11:40 AM

To: Shuhei Umeda ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

DUT との接続を一旦すべて外してやり直したり、システムや PC の電源を入れ直したりを何回かやってみましたが、

HCI_Event の受信はできませんでした。

何か他に考えられる状況はございますでしょうか。

状況に応じ、ご来訪でのご確認も可能です。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

HCI_Event が表示されていないということは、 PC から UXC に対して HCI_Command が送信できていないか、

UXC から PC への HCI_Event が受信できていないかになるかと思います。

一度 HCI_Event は受信できていましたので、接続状態を再確認いただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 11, 2025 1:38 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご教示ありがとうございます。

現在確認作業をしておりますが、

本日朝から手順に従い &quot;Bluetooth Test Mode&quot; を再度実行しましたが、昨日はあった &quot;HCI_Event&quot; の行が表示されなくなりました。

どのような原因、確認、復旧手段があるかご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 8:59 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

弊社では InterLab システムを使用したことがないのですが、

LE Direct Mode （Qualcomm Tool）の Log 上は、送信 / 受信ともに正常に動作しているように見えます。

それに対して InterLab システムの画面上は“ Received ”に何も表示が無いので、 InterLab システムは受信ができていないように見えます。

よって、 PC と InterLab 間のケーブルの接続状態を再度ご確認いただけますでしょうか？

また、過去 HM26 モデルでは同じテストシステムで送受信は問題なかったでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, November 10, 2025 5:04 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

下記の DUT との接続で、 InterLab システムとの通信を行おうとしていますが fail となります。

何か確認すべき点や修正すべき点などございましたらご教示いただけますでしょうか。。

InterLab システムとの接続いただきました &quot;Bluetooth Connection Diagram&quot; ( 添付 ) の真ん中の下側の PC の USB ポートと InterLab システムの USB ポートを接続。

使用ケーブル：

[ID] 変換ケーブル⇔ [ID] メス - メスケーブル ( クロス )
⇔ [ID] 変換ケーブル

InterLab システムから &quot;LE Reset&quot; を実行。

QUTS Status App の画面

InterLab システムの画面ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:48 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

情報いただきありがとうございます。

接続できるようになったとのこと承知いたしました。

引き続きよろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:13 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

RF PHY の方ですが、 ご連絡いただいた内容を実行したところ、下記の通り接続できましたのでお知らせします。引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:02 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様承知いたしました。

早速のご対応感謝いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:00 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

本日サンプル発送いたします。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 11:01 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様はい。ディスプレイ部、付属品含めてとなります。

お手数ですが、ご対応よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 10:58 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様ご連絡有難うございます。

一式ということはディスプレイ部、付属品も含めてという認識でよろしいですね。

発送は可能と思いますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 10:53 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT 試験用に弊社から送付しました DUT 一式ですが、

返却いただくこと可能でしょうか？

お手数ですが、ご確認をお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Wednesday, November 5, 2025 8:58 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

QUTS のバージョンは最新になっていますでしょうか？

Qualcomm Package Manager を起動して、” Updates Available ”タブを選択し、

もし最新のバージョンが存在する場合は、最新版をインストールしてみてください。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, November 4, 2025 7:12 PM

To: 'Toshitaka Mochizuki' ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきましてありがとうございます。

QUTS が動作するところまで進んだようで良かったです。

Step7 までは手順書の通り進んでいるのに Step8 で IP アドレスが表示されないということですね。

即答できないのでこちらでも調査してみます。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 6:27 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

現在再確認作業を行っております。

UXC10 の [ID] のセットアップを、いただきました手順書で行っておりますが、

ステップ 8 で、 COM Port のところで IP アドレスを選択するように書いてあるのですが、

下記の通り、 IP アドレスが表示ず選択できません。

どうすれば、 IP アドレスを選択できるようになるかを、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

Qualcomm Package Manager の検索 Window に QUTS を入力すると、該当するツールが絞り込まれると思います。

お試しいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 1:35 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

QUTSStatusApp ですが、 Qualcomm 社のサイトの Software のダウンロードを探しておりますが、複数のパッケージが表示されますが、そのものズバリのものが出てきません。

こちらは何のパッケージに入っているかご教示いただけますでしょうか。

お忙しいところお手数ですが、ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Shuhei
Umeda

送信 : 2025
年 10
月 31
日 ( 金曜日 ) 13:18

宛先 : Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再度ご確認いただきましてありがとうございます。

Qualcomm ID を取得されていること承知いたしました。

ということは、 Qualcomm Package Manager を使用して QUTS のインストールはできそうでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 11:43 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は終日不在としてご迷惑をお掛けいたしました。

以下回答となります。

ご確認どうぞよろしくお願い申し上げます。
もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。
ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、御社が Qualcomm ID をお持ちでないのは確かでしょうか？
基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。
QRCT が使えているので、その認証は Pass していることになります。

⇒先のメールでアリオンは Qualcomm ID を取得していないとお伝えしましたが御社 HM26 案件で営業の王が Qualcomm ID を取得しておりました。大変失礼しました。
使用中の QRCT のバージョンについて教えていただけますでしょうか。

⇒別途調べてお答えします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 10:45 AM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様 / 望月様お世話になっております。アルプスアルパインの梅田です。

ご確認いただきましてありがとうございました。
Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。
そのため、本日は QRCT を使用して BLE DTM モードへの移行を試しました。

誤解を招いてしまったかもしれません。

QRCT で QUTS の確認はできません。

QRCT がインストールされているのであれば、 QUTS も一緒にインストールされているのではないか、との推測になります。

Qualcomm 社のダウンローダー上、 QUTS が QRCT にも含まれるような構成になっているためです。

お手数でございますが、再度、以下の Path に QUTSStatusApp.exe があるかどうかご確認いただけますでしょうか？

C:\Program Files (x86)\Qualcomm\QUTSStatusApp\QUTSStatusApp.exe

もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。

ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、

御社が Qualcomm ID をお持ちでないのは確かでしょうか？

基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。

QRCT が使えているので、その認証は Pass していることになります。

使用中の QRCT のバージョンについて教えていただけますでしょうか。

また、御社と Qualcomm との間に契約関係はございますでしょうか？

以上、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 5:14 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様お世話になっております。

アリオンのジェシーです。

ご返信ありがとうございます。

＞現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

現在実施しようとしている試験は BLE Measurement ([ID]) です。

また、ラボに確認したところ、 Bluetooth Measurement (RF) 試験は既に実施完了しまして、テストレポートも先日提出させていただきました。

＞手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

BLE Measurement については、 Step
６マクロの実施（uxc_BLE_FTM_Mode.ttl）まで成功しました。

Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。

そのため、本日は QRCT を使用して BLE DTM モードへの移行を試しました。

但し、 BLE Measurement の測定手順では QUTS Status App での設定方法が指定されているため、 QRCT の画面上でどのように設定して BLE
DTM モードへ移行すればよいのかが分かりませんでした。そのため、本日再度お問い合わせさせていただきました。

大変恐縮ですが、現状（QUTS Status App 無し）で BLE DTM モードへの移行方法があればお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shuhei Umeda

Sent: Thursday, October 30, 2025 4:28 PM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様お世話になっております。アルプスアルパインの梅田です。

望月様の代理でのご確認ありがとうございます。

Qualcomm ID はお持ちでは無いが、 QRCT のインストールはできた、または QRCT は既にお持ちだったということでしょうか。

QRCT の画面を添付いただきましたので、 QRCT が動いている前提でお話しますが、

添付しました資料は既に展開させていただいている QRCT の動作手順書です。

現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

お手数ですが、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 4:09 PM

To: 酒井重之 Shigeyuki Sakai ;
梅田修平 Shuhei Umeda

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様、

お世話になっております。

アリオンのジェシーです。

ご不便をお掛けして申し訳ございません。

本日望月が社内不在のため、代理にてラボのフィードバックをご連絡いたします。

＞【BLE】

＞御社にて Qualcomm からツールを直接入手することは可能でしょうか？

申し訳ございません。内部で確認したところ、弊社は Qualcomm ID を持っていないため、 Qualcomm からツールを直接入手できないです。

メールでご提示いただいた方法（QRCT の利用）を試しましたが、接続に失敗しました。添付の Screenshot をご参照ください。

確認したところ、 USB ケーブルで制御用 PC に接続していますが、 PC 側で USB デバイスとして認識されていません。

また、 USB Driver.exe は QRCT フォルダ内に存在しないようです。

念のため、「Select USB Driver.exe」ボタンをクリックし、 QC.BluetoothLE_DirectMode.exe を選択して接続を試みましたが、 Failed device connection と表示されました。

ご確認いただき、 QRCT で DTM モードへ移行する手順をお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shigeyuki Sakai

Sent: Monday, October 27, 2025 1:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

本日、梅田が不在ですので、私からご回答します。

【IOPT】

添付のファイルが過去に Volvo から提供されていたのですが、御社へ提出していなかったと思います。申し訳ありません。

“adb install BlueSPP.apk”

については、 PDF の 3 ページ目に記載されております。

一度ご確認いただけますでしょうか。

【BLE】

御社にて Qualcomm からツールを直接入手することは可能でしょうか？

通常ですと QPM(Qualcomm Package Manager) というツール経由で PC にインストールします。

（そのためツールインストーラーをお渡しすることができないことも背景です）

QUTS は下記 QRCT をインストールすることで一緒に導入されます。

QRCT は Classic の試験でご使用いただいたと思いますので、 QUTS もご確認可能ではと思います。

一度ご確認いただけますでしょうか。

なお、 BLE 試験用にご提供しました手順書の &quot;Notes
on QRCT tools&quot; シートに QRCT のインストールの説明を記載しておりますので、合わせてご確認をお願いいたします。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:31 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

[ID] 試験に関して、メールでいただいている QUTS Status App と Run Bluetooth LE Direct
Mode テストツールがまだご提供いただいていないようです。

ご確認の上、ご提供お願いできますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:07 AM

To: Shuhei Umeda ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

10 月 21 日 19:42 の梅田様からのメールでは、「IOPTTestguide.pdf に記載されている BlueSPP.apk をインストール」という記述がありますが、

こちらで探しておりますが、これら資料をいただいていないようです。

もしお送りいただいているようでしたら、そのメールご送付の日時をお知らせいただけますでしょうか。

また IOPTTestguide.pdf 以外にも関連する試験で必要なファイルがございましたら併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 7:29 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

まずは adb が正常に動作できるようになったとのこと承知いたしました。

こちらかの情報に誤りがありまして申し訳ございませんでした。

また、 SPP の再試験ありがとうございました。

結果を再度 V 社と共有いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 7:02 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

&quot;USB-A 2.0&quot; というラベルの付いたケーブルを使用したところ、 adb install
はできましたが、

再度 SPP のプロファイル試験を実行しましたが、結果は以前と同じでした。

log のファイルを添付いたしますので、ご確認いただけないでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 10:39 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様ご確認いただきありがとうございました。

こちらのケーブルになります。

このケーブル経由で adb 関連のコマンド操作を試してみていただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 9:51 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

添付のケーブルがございましたが、こちらのことでよろしいでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 7:08 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

何度もご確認いただきましてありがとうございます。

再度、 PC と DUT の接続方法を確認させてください。

弊社から送付した DUT ですが、 USB ケーブルが 4 本あったと思います。

DEBUG SAIL

DEBUG HKP

DEBUG MD

以外のもう 1 本のケーブルはございますでしょうか？もしよろしければ写真を撮って送っていただけると助かります。

DEBUG MD とご案内いたしましたが、残りの 1 本が DUT 側の USB 機能として使うもので、

こちらのケーブルでないと adb が動作しない可能性がございます。

お手数をおかけいたしますが、 4 本目のケーブルのご確認をお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

お送りいただきました資料を確認し、 adb shell settings put global development_settings_enabled 1&quot; コマンドを送りましたが、以下のエラーが表示されます。

• error: no devices/emulators found

DUT や PC などで、他に確認すべき点や、設定すべき点がございましたら、ご教示いただけますでしょうか。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 1:19 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

添付ファイルの P.2 に Basic DUT operations が記載されておりますが、

Developer Mode は Enable になっていますでしょうか？

adb shell settings put global development_settings_enabled 1

を実行してから

adb install bluespp.apk

を試してみていただけますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 12:55 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡いただきました &quot;DEBUG MD&quot; の USB ケーブルを PC に接続し、 &quot;adb install bluespp.apk&quot; を実行したところ、下記のエラーが表示されました。

• adb: connect error for write: no devices/emulator found

また、 &quot;adb devices&quot; コマンドを実行いたしましたが、 &quot;List of attached devices&quot; の下に何も表示されず、認識されていないようです。

PC や DUT で、他に設定する所などがございましたら、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 11:53 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご確認ありがとうございます。

DEBUG MD と PC を接続してください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 11:51 AM

To: Itsuo Sakai ;
梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は不在といたしまして申し訳ございません。

以下確認事項がございますので、

ご回答いただけますでしょうか。

BlueSPP.apk をインストールするには、 DUT の下記の 3 本の USB ケーブルのどれを PC に接続すればよいかご教示ください。

DEBUG SAIL
DEBUG HKP
DEBUG MD

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 5:25 PM

To: Shuhei Umeda ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
Connection Diagram ですが、 RF
PHY Test System を追記したものを準備いたしました。
こちらを参照いただけたらと思います。

⇒ 何度もお手数をお掛けしました。これで RF
PHY 試験の接続系統図が明確になりました。ありがとうございました。

引き続きよろしくお願いいたします。

酒井差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 16:00

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様

Connection Diagram ですが、 RF PHY Test System を追記したものを準備いたしました。

こちらを参照いただけたらと思います。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, October 21, 2025 2:33 PM

To: 'Itsuo Sakai' ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

Operation Manual ですが PDF に変換しました。

こちらをご参照ください。
RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。

使用いたします。

添付の Bluetooth measurement procedure.pdf、 BLE measurement procedure.pdf
を参照ください。

操作手順の中に Ethernet に関する操作がございます。
ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の
USB 接続部分は反映されていないという理解で間違いないでしょうか。

おっしゃるとおりです。 Bluetooth Connection Diagram に反映されておりません。
そうあれば私の最初からの質問であるテストシステムの Serial
over USB
の接続先ですが、それは PC
running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

はい。その理解で合っています。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 1:43 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
RF PHY Test System との接続は以下の図をご参照ください。
DUT と PC
running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。
RF PHY Test System と DUT は RF のみ接続します。

⇒ RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。
そして PC running QDART と RF
PHY Test System は直接 RS232、 GPIB での接続となります。

⇒ HM26 でも同じ図の Q 社マニュアルを使いました。しかし、 DTM モードでは GPIB 経由のコマンドの定義はなく、 Serial
over USB を含む Serial

(UART) 経由でのコマンドが定義されそれに従って DUT を制御しています。

このため DUT と PC および RF
PHY テストシステムは下図のような接続系統図となります。

ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の

USB 接続部分は反映されていないという理解で間違いないでしょうか。

そうあれば私の最初からの質問であるテストシステムの Serial over USB

の接続先ですが、それは PC running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

以上ご確認をお願いします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 12:55

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

RF PHY Test System との接続は以下の図をご参照ください。

DUT と PC running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。

RF PHY Test System と DUT は RF のみ接続します。

そして PC running QDART と RF PHY Test System は直接 RS232、 GPIB での接続となります。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 12:01 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

ご返信ありがとうございます。
制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。
ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

⇒ 図では黄色マーカー部分の一端が PC,
他端が DUT ですが、文面から推測すると下図かと思われますが、正しいでしょうか ?

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 11:40

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。
以上のようにご送付いただいた Connection
Diagram では RF PHY の
DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。

制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。

ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

DUT
– USB conversion harness
– USB Type-A ケーブル – PC
で結線され、 USB Serial として PC と DUT 間の通信が可能となります。

後ほど、 Operation Manual を PDF 化して送付するようにいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, October 20, 2025 7:19 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

先程の質問は私の Excel のバージョンが古いせいか以下の図が表示されたためで、「薄緑線の分岐」とか「薄緑線の上方の接続先」が何のことやらと思われたと思います。お詫びします。

しかし、 RF PHY 試験は認証テストシステム及び簡易なアンリツ

BT テスタでも RF 測定系とは別に、 UART/COM ポート接続が必須で、

HM26 でも下図のように外部 PC ＋ Q 社テストアプリを Bridge にして

DUT<->(Eternet)<->PC<->(Serial over USB)<->RF PHY テスターという接続を行いました。その際の DTM モードマニュアルを添付します。

以上のようにご送付いただいた Connection Diagram では RF
PHY の

DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。ご送付の Connection Diagram はおそらく電波法 /FCC 試験時のオープンループ試験用のものと推測されます。再度 DTM モードのセットアップ方法をご確認ください。

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 20 日 18:35

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様

SPP のレポートの送付ありがとうございました。

内容確認して返信いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 6:17 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

SPP のレポートをお送りいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Monday, October 20, 2025 5:16 PM

To: Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT の再試験の実施ありがとうございました。

SPP についてですが、再試験結果のレポートを送付いただくこと可能でしょうか。

V 社側に連絡して事前条件や SW の差分の有無について確認を依頼したいと思います。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 5:12 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

IOPT 試験について連絡です。

御社からご送付いただいた SPP の PTS レポートと同じ ICS 設定であることを確認して v8.10.2 で再試験を実施しましたところ、 MAP と PBAP は Pass

しましたが SPP は Pass しませんでした。

SPP の PTS 試験では、スタート前に DUT の接続済機器一覧から PTS を削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいた Pass レポートを得られた DUT の SW が当社の DUT

の SW から更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいた SPP の PTS レポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki
Sakai

Sent: Monday, October 20, 2025 1:36 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご返却、どうもありがとうございました。

弊社側での内部データ更新が完了しまして、先ほど望月様宛での発送手続きが完了したところです。

ヤマトお問合せ No : [ID]

併せて、 RF PHY 試験の手順書もお送りします。

ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 1:40 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

承知いたしました。

更新いただいた後、 RF PHY 試験の日本分実施後、台湾での試験向けに発送予定です。

その際に該否判定書と製品仕様書が必要になります。

今回は RF 試験についてはモニタ部分については輸出は必要なかったとおもいます。

また、先日お伝えいたしました、プロファイル（IOPT）試験についてのご修正についてもそちらのサンプルの返送が必要でしたらおしらせください。

以下 RF 試験機の返送になります。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, October 15, 2025 12:56 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

＞ 御社へ一旦サンプルをお返しするという事だったと存じます。

はい、お手数おかけしまして申し訳ありませんが、そのように進めさせてください。

RF 試験用のサンプルは以下の写真が示す DUT のみで大丈夫です。

ご返却の宛先は私でお願いいたします。

福島県いわき市好間工業団地 20-1

アルプスアルパイン株式会社 DC1 設計部酒井重之あと、 BLE
オプション機能の試験のため DUT を台湾に発送されると思いますが、弊社から該非見解書をお出しするということでよろしいでしょうか。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 6:28 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

RF 試験が完了いたしましたが、 RF PHY 試験実施のため御社へ一旦サンプルをお返しするという事だったと存じます。

RF 試験用のサンプルですが、 Full セットでお返ししたほうがよろしいでしょうか。

必要な物のみでよろしければご指定いただければそちらのみお返しいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, October 14, 2025 9:52 AM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきありがとうございました。

RF 試験が合格完了とのこと承知いたしました。

引き続き、 RF PHY の実施、よろしくお願いいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Friday, October 10, 2025 7:35 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様アリオンの酒井です。いつもお世話になっております。

望月に変わり私からお知らせします。

先程 RF 試験が合格完了しましたのでお知らせします。来週 RF
PHY(1M)

を実施し、 Pass 後に台湾ラボへ送って (2M,
Coded) を実施する予定です。

引き続きよろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 10 日 17:38

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

酒井に代わりまして本件返信させていただきます。

まず試験日程のイメージの共有ありがとうございました。

おおよそこれぐらいの日程感で試験が進むこと承知いたしました。

次に、 Bluetooth IOPT 試験の結果のご連絡ありがとうございました。

Fail、 [ID] となった項目についてレポート内容を確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 4:49 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

今回のケースで問題なく試験が進んだ場合は以下の様な時間的イメージとなります。（日本分のみ）

RF： 4 日程度

[ID]： 3 日程度

Profile： 2 日程度状況により途中中断、問題箇所再確認などで時間は大きく変化する場合があります。

ご了承ください。

Bluetooth IOPT 試験について以下エンジニアから報告がございます。

★ ALAP(UXC10) の IOPT 試験で 18 項目中 14 項目は Pass しました。

残る下記項目が Fail、または [ID] となっております。

・ IOPT/MAP/MCE/CGSIT/SFC/[ID]

・ IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVB/SDPR/[ID]

上記の PTS レポート ( ログ付 ) を添付しますので、ご確認および解析をお願いします。特に製品の SDP レコード内容を重点的にご確認ください。

PTS の IXIT の設定で対処できるものはその旨お知しらせください。 FW 改修が必要な場合は改修 FW をご準備ください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 2:20 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご確認どうもありがとうございました。

各試験の想定日数を教えていただく事は可能でしょうか。

問題発生により変化することも承知しておりますので、特に問題無く進んだ場合の日程感で構わないです。

RF ・・・

RF PHY ・・・

IOPT ・・・

RF PHY 試験前の DUT 更新時期や、 IOPT 試験後ディスプレイご返却のタイミングを知っておきたいためです。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 2:08 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

[ID] の方、受け取っております。

RF PHY 試験の方のテストプランも作成いたしました。

DUT サンプルの運用につきましてはご希望通り対応予定です。

何かございましたら改めて連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 1:57 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご確認、どうもありがとうございました。

試験のご対応を引き続きよろしくお願いいたします。

別メールにしてしまいすみませんでしたが、

Questionnaire の更新と DUT 更新対応のご相談をご連絡しておりますので、

そちらもご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 1:10 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

お待たせしております。

その後こちらで試行いたしまして、 RF 試験開始の段階まで進めることができたようです。

ＲＦ試験実施の上何かございましたら随時連絡いたしますのでしばらくお待ちください。

また、ＩＯＰＴ試験の方も動作確認いたしました。

特にこちらも問題ないようです。

取り急ぎ連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, October 9, 2025 6:58 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご指示有難うございます。

昨日連絡いたしました DUT の通信接続ができない問題について、

電流の制限を調整したところその部分につきましては正常に動作することが確認できました。

ただ、その先で確認を要する状況となっておりますので、もう少しはっきりしましたら改めて連絡いたしますので、もうしばらくお待ちいただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Thursday, October 9, 2025 3:18 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

弊社での似た過去事例にもとづき、少しご確認お願いしたい点がございます。

·
Wake_up 端子の GND 接続確認

DUT の Wake_up ラインが電源の GND に接続されていることをご確認お願いします。

接続が外れると DUT が Sleep 動作に入る動きをしますため。

·
電源投入後、 30 秒待機電源投入後、ソフト起動に 30 秒程度時間がかかりますので、それを待ったのち、操作を開始してみていただけますでしょうか。

以上、２点のご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 6:01 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

RF
試験の DUT Setting で以下の現象が起きております。

・「(UXC)AT operation manual_for_BT_rev001.xlsx」内の手順５実施後、「root@lemans:~#」が表示されず、通信接続ができません。

TeraTerm は最新バージョン (5.5.0) を使用しております。

TeraTerm を別のバージョン (5.4.1) で確認しましたが、同様の現象が起こります。

手順 5 実施中にも切断されることがあります。

こちら対策をご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 5:54 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

★ RF PHY は確認中で未記入項目があって Test
Plan は作成できません。

[ID] の未記入（TBD）の項目のご確認状況はいかがでしょうか。

★サンプルは本日到着し、セッティング、動作確認を行っております。

確認結果わかりましたら連絡しますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 9:11 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様立て続けて申し訳ございません。

RF 試験の DUT 操作マニュアルおよび TeraTerm 用マクロを提出します。

ご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 2:54 PM

To: 'Toshitaka Mochizuki'

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

以下、トピックごとにご連絡いたします。

■ DUT list について間違い修正や写真追加等で更新しました。

添付しました 2025/10/07 のもので差し替えをお願いいたします。

■ DUT 機材発送について

RF 試験用と IOPT 試験用の DUT 機材を別々に発送しました。

以下、ヤマトの送り状番号です。

■ [ID] について別メールですが質問事項へのご回答、ありがとうございました。

（現在の記述で問題無いと理解いたしました）

■ IOPT 試験用の DUT 操作マニュアルについて添付の AOSP_Bluetooth_User_Manual_1_0_0.pdf が試験用の DUT 操作マニュアルです。

不明点などありましたら、ご連絡お願いいたします。

■ RF 試験用の DUT 操作マニュアルについて明日を目標に、現在準備中です。

整い次第、お送りいたします。

以上、ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 7, 2025 11:06 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ドキュメントのご送付ありがとうございます。

試験サンプルの接続、操作マニュアルのご提供もお待ちしております。

（可能であれば英文、もしくは中文併記でいただけますと助かります。）

引き続きどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 9:24 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご回答ありがとうございます。

送信データ量が大きくなりすみません。

■機材提出票および DUT list

機材提出票を作成いたしました。

RF DUT 一式の方はのちのち台湾に行く予定のため、 IOPT
DUT とは別で扱えた方が好ましいと思いましたため、そのようにしました。

また、 WFA メールスレッドの方でありました税関対策の意味も込めて DUT
list を作成しました。 RF DUT の接続写真はのちほど載せるようにします。

お気づきの点等ございましたらご連絡ください。

■ [ID]

こちらも作成いたしました。

下記のご確認をよろしくお願いいたします。

Antenna だけの値を持っていないことから、 Cable
Loss も含めた値となります。こちらで構いませんでしょうか？

このケーブルは、製品のアンテナケーブル or 測定用ケーブルどちらになりますでしょうか？添付ファイルには、一旦、測定用ケーブルのロスを書いています。

BLE の試験モード検討中のため、今時点 TBD とさせてください。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 6:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

＞・ RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

★管理を共通にしてよいのであれば、最終的なご提供物を１冊にまとめていただいても問題ございません。必ず数量、それぞれの識別が出来るようにサンプル本体や付属品にラベルなどを貼ってください。

＞・ IOPT 試験は Questionnaire はございますか？

★こちら ICS を既にいただいているので特に Questionnaire は必要ございません。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 4:54 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご指示ありがとうございます。

以下、確認させてください。

·
RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

·
IOPT 試験は Questionnaire はございますか？

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 11:47 AM

To: Misumi Sato ;
酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

先週はお打ち合わせありがとうございました。

Wi-Fi と一旦メールを分けさせていただきます。

Bluetooth サンプルの送り先ですが、当社日本ラボは本メールのフッタにございます望月宛にお送りください。

また、その際には添付の機材提出票をお送りください。

また RF
テストプラン作成のため、添付の [ID] にご記入の上、ご返送いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Misumi Sato

Sent: Friday, October 3, 2025 4:06 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

こちらこそ早速発送手続き着手していただきありがとうございます。

ご発送準備整いましたら、追跡番号とインボイスをご提供いただけますと幸いです。

尚、以前貴社の別部隊の WFA 認証試験をご担当させていただいた際台湾から日本への DUT 返送時に、税関から再輸入免税措置を求められた経験がございます。

その際、製品個々のシリアルナンバーが必要だったため、念のため、 DUT 本体や

Wi-Fi アンテナ等にシリアルナンバーをご設定いただくことをお勧めいたします。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 3:51 PM

To: Misumi Sato ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について佐藤様お世話になります。

アルプスアルパイン酒井です。

早速のご回答、どうもありがとうございます。

来週早々に発送手続き着手する予定です。

よろしくお願いいたします。

酒井

From: Misumi Sato

Sent: Friday, October 3, 2025 3:05 PM

To: 酒井重之 Shigeyuki Sakai ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

午前中の会議ではありがとうございました。

横から失礼いたします。

WFA 試験の DUT の送付先ですが、下記の表に記載させていただきましたので、ご参照お願いいたします。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

追跡番号、インボイスをご連絡その他、何か WFA 試験に関すること、および輸送に関するご質問等ございましたら、お気軽にお問い合わせくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 2:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

PCAT のご確認ありがとうございました。

この内容を踏まえまして、弊社側でどう対応するか確認いたします。

機材の発送について、

·
下記の通り、弊社から送る際の送付先を教えていただけますでしょうか。（間違い等ありましたら修正をお願いいたします）

·
該非判定見解書等の時間かかるものは着手開始したいと思いますので、対応必要事項欄に追記していただけますでしょうか。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

追跡番号、インボイスをご連絡よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, October 3, 2025 12:16 PM

To: 酒井重之 Shigeyuki Sakai ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

会議資料の更新＆共有させていただき、ありがとうございます。

PCAT に関して台湾ラボが HM26 の Wi-Fi 認証試験で利用実績がございます。

ただ、御社別部隊から異なる案件への対応として、

今回 V 社様案件で使用してよいか、バージョンの指定がないか、

使用できない場合、御社からご提供いただけるか、

ご確認いただきますよう、お願いいたします。

※ HM26 の案件で使用した PCAT のバージョン： [ID]

よろしくお願いいたします。

Outlook for Android を取得差出人 : Shigeyuki Sakai

送信日時 : 金曜日 , 10 月 3, 2025 10:59:20
午前宛先 : Jun Wang ;
Toshitaka Mochizuki ; Itsuo Sakai ;
Misumi Sato ; Zakk Shih

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画について各位本日は、打合せをどうもありがとうございました。

更新した資料をお送りします。

‘QA’ シートに、★マーク付きで確認必要事項を書いております。

試験のご対応、引き続きどうぞよろしくお願いいたします。

酒井

-----Original Appointment-----

From: Jun Wang

Sent: Thursday, October 2, 2025 1:10 PM

To: Jun Wang; 酒井重之 Shigeyuki Sakai; Toshitaka Mochizuki; Itsuo Sakai

Subject: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について

When: 2025 年 10 月 3 日金曜日 9:30-10:30
(UTC+09:00) 大阪、札幌、東京

Where: Microsoft Teams 会議アルプスアルパイン酒井様こちらから設定して申し訳ございません。

明日の打ち合わせは少し早めに開始して、 09:30 からでお願いいたします。

時間帯を 09:30 ～ 10:30 に修正し、会議案内を再送いたします。

宜しくお願いいたします。

アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

弊社側関係者に確認いたしまして、下記時間帯でお願いいたします。

10/3 （金） 10:00 ～ 11:00

会議リンクは下記ご参照願います。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
489 106 497 201 8

パスコード :
sR6yD26r

開催者向け :
会議オプション

________________________________________________________________________________

_____________________________________________

From: Jun Wang

Sent: Thursday, October 2, 2025 10:06 AM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

空き時間帯の共有ありがとうございます。

本日は酒井様のお時間が概ね埋まっているようで、

弊社関係者と一旦明日で調整させていただきます。

調整つき次第ご連絡いたしますので少しお待ちください。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Thursday, October 2, 2025 8:42 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご承諾ありがとうございます。

以下に私のカレンダーを貼りました。この白い時間帯でお願いできましたら助かります。

また、時間は 30 分を見込みますが、延長用に 1 時間スロットを頂けたら助かります。

ご確認をよろしくお願いいたします。

＜１０月＞

酒井

From: Jun Wang

Sent: Thursday, October 2, 2025 7:26 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証の Pre-test の正式見積書について、

承知いたしました、ご用意いたします。

機材送付の段取りについての打ち合わせですが、

弊社側関係者に確認いたしますが、

予め酒井様のご都合をお伺いしてもよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, October 1, 2025 6:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご提案どうもありがとうございました。

【アルプスアルパイン様】 V 社 UXC10 の Wi-Fi 認証につきプリテストのご提案 _Update_1001.pdf の内容でお見積書をいただけますでしょうか。

あと、 BT SIG 試験と WFA 試験の DUT 機材発送段取りを考えておりますが、

機材の保管場所がいわきと中国大連に分かれている背景や、少し悩んでいる点があります。（添付ファイル）

この内容を一度打合せさせていただけませんでしょうか。

可能でしたら、打合せの候補日をいただきたいです。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, October 1, 2025 10:59 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi Pre-test の部分試験に関して、

提案資料の P5 に追加いたしました。

基本は本番試験の各対象 Program に関して、 WFA の Test Plan より一部抽出して試験を行う考えです。

ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, September 30, 2025 9:40 AM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

早速ご確認いただきありがとうございます。

部分試験のブレークダウン、

なるべく早めにご報告するように調整してまいりますので、

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Tuesday, September 30, 2025 9:11 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

内容確認しまして、とても良い内容だと考えております。

ご提案どうもありがとうございます。

試験項目ブレークダウンお待ちしております。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Tuesday, September 30, 2025 6:46 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

お待たせいたしました。

UXC10 の Wi-Fi 認証試験をスムーズに進めることができ、

そして目標時期までに認証取得できるように、

プレテストのご提案をいたします。※添付ご参照願います。

部分試験に関して、もう少し試験項目のブレークダウンについてラボと相談しておりまして、もう少しお待ちいただきますと幸いです。

ご検討賜りますようお願いいいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Monday, September 29, 2025 4:38 PM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証に向けての Pre-test に関して、酒井様のご要望を基に、

ラボと提案内容について相談しております。

本日は台湾がお休みをいただいておりまして、先週末時点の概案を展開いたします。

本日の遅い時間帯になりますが、もう暫くお待ちいただきますようお願いいたします。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 29, 2025 10:34 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

Pre-test のご検討の状況はいかがでしょうか。

状況を教えていただけると助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 24, 2025 4:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi 認証試験につき、 Pre-test のご相談ありがとうございます。

酒井様のお考えをラボに展開いたしまして、

Pre-test への期待や目的は理解いたしました。

いただいた資料を基に、 Pre-test 向けの Test Plan をご用意いたします。

目標として、 9/26 （金）までにお送りいたしますので、

少々お待ちいただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 24, 2025 11:39 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

打合せありがとうございました。

私が考えております Pre check の進め方のメモ書きを添付します。

なるべく無駄なく効果的に check を行っていきたいと思っています。

御社でのご経験踏まえて、、 check 実施項目のご提案等いただけますと、大変助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Saturday, September 20, 2025 9:25 AM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

補足説明ありがとうございます。

Wi-Fi 認証試験はユーザー立場で、 WFA が決めた GoldenSample との接続性の確認が多く、

御社で WFA が定めた試験環境でなくても、ユーザー視点で

Wi-Fi の機能確認はできるのではと考えます。

最新の日程表から、御社で SW の確認も行っているようですが、

その状況を参考に、弊社ラボでの事前確認プランを立てようと考えますが、

いかがでしょうか。

宜しくお願いいたしますアリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 6:45 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

私の言葉の選び方が良くなかったです。

「UXC10 の SW が不安定」ではなく、「UXC10 の SW の品質レベルが不明なので不安」が正しいです。

弊社も V 社も WFA テストをする環境を保持しておらず、どの程度 WFA テストできる品質レベルなのか分かっておりません。

従いまして、 Pre Test では、 WFA テストできるレベルなのか確認したいです。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 19, 2025 5:32 PM

To: 水野淳也 Junya Mizuno

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC10 の SW が不安定との事ですが、

Lab から具体的な症状を確認されております。

例、〇〇操作する時に〇〇不安定の症状がある、〇〇の際に良くリブートかかったりする、等差支えの無い程度でお願いできますと助かります。

よろしくお願い致します。

Outlook for Android を取得差出人 : Jun Wang

送信日時 : 金曜日 , 9 月 19, 2025 2:38:00
午後宛先 : Junya Mizuno

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

承知いたしました。

9/22 （月）に Lab との相談状況をご報告いたします。

具体的な提案ができるように調整してまいります。

最新日程を踏まえた進め方のすり合わせですが、

9/24 （水） 09:00 ～ 10:00、 でお願いいたします。

弊社の酒井と王君、 2 名で参加させていただきます。

よろしければこちらで Teams 会議を設定いたしますが、

御社の参加者をお伺いしてよろしいでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 11:01 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

もしも可能であれば、 9/22( 月 ) までにご回答もしくは状況のご連絡をいただくことは可能でしょうか？

V 社側の SW リリース遅延およびソフト品塾度が問題ではありますが、弊社から V 社に具体的なプランを早急に提示、説明していく必要がある状況です。

また、今日中に提示予定の新しい開発日程を基に、一度 [ID] と WFA の進め方のすり合わせを再度させていただくことは可能でしょうか？ ( 最大で 1 時間程度を想定しています )

来週の火曜日は御社はお休みと思いますので ( 弊社は勤務日です )、来週の月曜日もしくは水曜日の以下どれかの日程でお打ち合わせが可能かご確認をお願いしたいです。

ü
9/22( 月 ) 14:00-15:00

ü
9/24( 水 ) 9:00-10:00

ü
9/24( 水 ) 13:00-15:00

お時間に限りがあれば、 V 社の次期モデルの [ID] と WFA 認証についてもお話しさせていただければと考えております。

ご確認をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 11:20 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

相談なので、話してみないとわかりかねますので。

急ぎであれば回答希望納期をいただければそれまでに回答するように調整いたしますが、いかがでしょうか。

SW に関して情報共有させていただきありがとうございます。

今後試験において Fail が出た際のデバッグ作業も V 社自力（外部委託？）

で行う予定、承知いたしました。

他社様案件での経験ですが、ソフト完成度が低いと安定的な試験結果を得られず、

トラブルシュートも難航になったり、結果試験期間が倍半年かかった案件もございました。

ということで、弊社としても完成度の高い（量産品同等レベル）製品のご提供をお願いいたしたいです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 7:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

申し訳ございませんが、御社 Lab にご相談をお願いします。

御社 Lab より、いつ頃にご回答をいただける予定か、分かっておりましたら教えていただけますか？

今回の V 社からリリースされている SW は、 WFA テストに対応した素性として受け取っています。

但し、実態を聞くと、 V 社側でも WFA 認証の経験が乏しく、実際にどれだけの品質になっているか (=WFA テストできる状態か ) 分かっておりません。

V 社の SW のバグ修正等は、全て V 社で実施します。

弊社側で V 社の SW に手を加えることはありません。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 3:26 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記ご相談いただきありがとうございます。

現行 SW が不安定な状況にあること、承知いたしました。

ご要望を一度 Lab に相談いたしますので、

少々お待ちいただきますと幸いです。

参考にさせていただければと存じますが、

今回 V 社からリリースされる SW は受験用 SW でしょうか。

もしくは、 Ver0.8 （例）として御社にリリースし、その後のバグ修正、完成度アップは御社で行われる、との予定でしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 1:00 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

追加でご相談したいことがあります。

現在、 V 社より WFA 向けソフトウェアを受領したのですが、完成度に不安がある状況です。

この状態で WFA 本試験を開始し、結果として、殆ど何も試験できずに三か月を過ぎてしまうことを恐れています。

従いまして、“ WFA 本試験を開始できる状態であること”を確認する目的で、事前試験をお願いしたいと考えております。

以下の条件にて、事前試験項目のご提案とお見積りをお願いできないでしょうか？

ü
期間 : 3 日～ 5 日

ü
確認したいこと : WFA の基本となる Test Program の General 部分が Pass できること

Ø
Wi-Fi 4 11n、 Wi-Fi 5 11ac、 Wi-Fi 6 11ax の初期に実行されると想定するコマンド受付確認、接続確認、動作確認等が該当すると考えています。

確認したい内容が具体的ではなく、申し訳ございません。

お手数ですが、一度依頼をご確認いただき、不明点等ありましたらご連絡をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Wednesday, September 17, 2025 4:17 PM

To: 'Jun Wang'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

承知しました。

その他の問題点含めて、ご確認、整理をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

上記ご理解があっています。

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

承知いたしました。確かに Bluetooth の見積依頼書でも「UXC10」とご記載されています。

再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 3:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご指摘ありがとうございます。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

この場合、再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 12:30 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社 UXC の Wi-Fi 見積依頼書の更新、ありがとうございます。

Model Name について確認させていただきます。

Submit いただいた CID （[ID]）では、 UXC
1.0、となっていますが、

見積依頼書では UXC10 とご記入されています。

正しくは UXC 1.0 でよろしいでしょうか。

※ WFA Certification System の画面よりキャプチャ宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 10:58 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

既にメール等でやりとりしており、ご存じの内容と思いますが、

見積書に以下未記載の箇所がありましたので追記しました。

ü
Submission Category(Flex/Quick/Derivative)

ü
CID number

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 3:08 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

見積依頼書の再送、ありがとうございます。

内容を確認させていただきます。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:58 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

本メールに添付しましたのでご確認をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 1:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社より見直しした依頼書も入手しましたので送付させていただきます。

添付はついていないようですが、ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:11 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

CID （[ID]）を基にお見積りを進めていただき、ありがとうございます。

後追いですが、 V 社より見直しした依頼書も入手しましたので送付させていただきます。

前回、依頼書から変更が入っている Support Function 部分を黄色セルにしました。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:11 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

下記ご連絡をいただきありがとうございます。

V 社が本日改めて CID （[ID]）を Submit されたようです、

Submit された内容から、 Certified b/g が入っていなく、

Certified a/ac/N、 Certified 6 が対応されることを確認できました。

下記ご連絡いただいた内容で御見積書をご用意いたしますので、

更新でき次第の送付で構いません。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Friday, September 12, 2025 7:38 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

申し訳ありません、今しがた、 Volvo からリストの更新に関する情報がありました。

b
と g
が少し古い規格ですので、申請を削除することを考えているそうです。

急ぎ再提出できるよう推進しますので、お見積りはもう少しお待ちいただけますでしょうか。

よろしくお願いいたします。

酒井

From:
水野淳也 Junya Mizuno

Sent: Friday, September 12, 2025 5:52 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご連絡ありがとうございます。

Test Tool につきましては、スウェーデン現地法人を介して V 社より回答を入手できました。

お見積りに影響は無いのかもしれませんが、取り急ぎ Test Tool 欄を記入したお見積書を送付させていただきます。

週明けのお見積りをお待ちしております。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 4:58 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

来週中の日程更新、お手数かけますが、よろしくお願いいたします。

見積依頼書に関して、 test tool は継続してご確認お願いいたします。

いただいた内容を基に見積書をご用意いたしますので、

週明けにお送りいたします。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 金曜日 , 9 月 12, 2025 2:15:31
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お待たせしてしまっており、申し訳ございません。

昨日、 V 社より弊社のスウェーデン現地法人を介して、 SW がリリースされてきました。

従いまして、現時点での Open 項目は以下の認識です。

1.
V 社 SW の動作チェック

2.
V 社操作マニュアルの内容チェック

3.
V 社からの Test tool の回答入手および見積書の再送

3 については、 V 社に PUSH しつつ、残りの Open 項目については確認を進めます。

来週中に現在の状況を基に、新たに認証計画を更新し、ご提出させていただきます。

何がご不明点、お気づきの点等ありましたらご連絡をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:45 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Ｖ社 [ID] の Wi-Fi 認証について、

8/21 に V 社から SW のリリースが遅れるとご連絡をいただきましたが、

現時点の状況はいかがでしょうか。

ザックリで構いませんので、共有させていただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Monday, September 8, 2025 9:32 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

Test Tool は V 社で記入した Support
Function によって決まる認識の為、

V 社にどの Test Tool を使うのか確認を依頼しております。

少々お待ち下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 5, 2025 11:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証御見積依頼書のご記入、ありがとうございます。

Test Tool に関して記入されていないようですが、ご確認いただいてよろしいでしょうか。

Row#67 ～ 72

For testing

WTS(Wi-Fi Test Suite)

Quick Track Tool

Manual

For throuput

WTS(Wi-Fi Test Suite)

IxChariot

iPerf

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 5, 2025 9:10 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の [Support Function Information] 欄に対して、 V 社から回答を入手しました。

お手数ですが、一度ご確認いただき、何か気になる点等ありましたらご指摘をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:24 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご理解いただきありがとうございます。

お手数かけますが、よろしくお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 2, 2025 1:18 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

ご指摘の点は仰る通りと思います。

改めて、認証する試験は何か、仕様するテストツールは何か、それらをどのように接続し、動作させるのか、を段階的に整理するように依頼します。

その上で不明点がある場合には質問を明確にするように依頼します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 2, 2025 9:09 AM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記打ち合わせのご要望ですが、弊社が認証ラボとして、

UXC の設計開発に携わったことがなく、マニュアル作成の支援や相談はご対応できかねますので、打ち合わせに参加してもあまり意味が無いと存じますが、いかが思いますでしょうか。

WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます。

弊社からも同じ説明になりますが、それでも分からない、と言われると困りますね。

実際車のユーザーマニュアルなどの作成経験があるのではと思いますが…

Wi-Fi だけでなく、 Bluetooth、 USB、 Carplay や AndroidAuto の認証につき、

内容やレベルは違いはあれども、「マニュアル」作成もあるでしょう。

どうしてもマニュアルの作成が困難な場合、 1 つご提案ですが、

接続過程をビデオ撮影してご提供いただくことでいかがでしょうか。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 月曜日 , 9 月 1, 2025 10:09:16
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

WFA 試験を受けるために、 V 社にソフトウェアの操作マニュアルの作成を依頼しております。

ALAP からは以下のような目次を目安に作成依頼をしておりますが、 V 社側でマニュアル作成経験が無く難航しているそうです。

(WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます )

- Connection diagram

- How to bring up DUT and Android

- Wi-Fi Test Suite

Configuration

AP test procedure

STA test procedure

- QuickTrack

Configuration

AP test procedure

STA test procedure

- Also, some shell scripts or supplemental information so that test operator doesn ’ t
have any confusion about set up.

※ WTS や QuickTrack のどれを使うのかは並行して Volvo へ確認中ですそのような状況の中、 V 社からマニュアルの内容についてアリオン様とも打合せをさせて教えてほしい、とリクエストを受けました。

打合せは、何を書けばよいか？の QA になると予想します。

お手数ですが打合せのご対応は可能でしょうか？

可能な場合、 9/4( 木 ) もしくは 9/8( 月 ) の 16:00 以降でご都合が良い時間を教えていただけないでしょうか？

※両日共にご都合が悪い場合には、ご都合が良い日時を教えていただけますと幸いです。

弊社も HM26 のモデル等で経験はあるものの、 UXC 担当の私などは実経験がある訳では無い為、

御社から未経験の V 社を適切にガイドしていただけると助かります。

ご検討をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 29, 2025 1:59 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご確認ありがとうございます。

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

はい、 Power とは送信パワーのことです。

V 社ソフトで試験するにあたり、送信パワーを確認する場合には、何を基準に確認をされるのか把握し、

事前に V 社に基準を満たすことを確認する必要があると考えて、質問をさせていただきました。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

はい、 6GHz は未対応になる為、 Return で問題ないと考えています。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 29, 2025 1:22 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

「Wi-Fi 認証見積依頼確認書」のご返送はもう少し時間かかる状況、

承知いたしました。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, August 29, 2025 1:07 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

V 社に [Support Function Information] 欄の記入を依頼し、受け取りましたが複数確認事項があり、時間を要しています。

申し訳ございませんがもう少々お待ち下さい。

また、 Wi-Fi Alliance 認証の試験項目に関して、ご確認したいことがあります。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

試験準備の際に考慮する必要があるか把握する為、ご確認させて下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 22, 2025 1:55 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

弊社スウェーデン現法を介して V 社に [Support Function Information] 欄の記入を依頼しております。

記入が完了できましたら直ぐにご送付させていただきます。

また Pre-test のアドバイスについても承知しました。

V 社の SW リリース状況を確認する中で、 Critical な部分および Pre-test 要否についても V 社含めて確認していくようにします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 22, 2025 10:31 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC の Wi-Fi 認証試験用 SW のリリースが遅れている状況、承知いたしました。

リリース予定について引き続き更新の方よろしくお願いいたします。

先日のメールでお願いいたしました弊社フォームの「Wi-Fi 認証見積依頼確認書」へのご記入ですが、

いつ頃ご送付いただけますでしょうか。

御社フォームの WorkSheet をいただいておりますが、 VCC Comment、 QC Comment も併記されている中、

最終仕様（認証取得のターゲット仕様）が不明確となっているため、

仕様情報の整理としても、見積依頼書へのご記入をお願いいたします。

Per-test に関して、 SW リリース時期が不明となっている中、予定が立てられない状況をよく理解いたしました。

3 ヵ月プランの中で試験、問題解析 / 原因究明、デバッグ、再試験、をやり切るのかなりの負荷となります。

打合せでご説明いたしましたように Pre-test は部分試験の実施も対応可能なので、

Critical な項目のみの事前試験があればフロントローディングができ、本番試験が効率アップし、

L/O 日程の確保に繋がりますので、時間的に全く無理でない限り事前試験をお勧めいたします。

また SW のリリース状況を踏まえてご相談いただければと存じますので、

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 11:07 PM

To: Jun Wang

Subject: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

Wi-Fi Alliance 向け Software に関して、 V 社より最新情報が入りました。

残念なことに、 Android V 適用に向けた対応が難航しており、弊社へのリリース遅延が発生し、現時点ではいつリリースできるか不明との情報を受けております。

弊社としては、遅くても 9 月中に V 社から Software を受け取れるように PUSH している状況です。

上記の状況を踏まえまして、 Pre-test を実施する時間が確保できない為、

Pre-test は無しで、三か月パックの中で最初の 1.5 カ月は試験 1 回目、後半の 1.5 カ月で NG 修正と試験 2 回目 (NG+ 関連する試験項目 )、といった形で進めたいと考えております。

取り急ぎ、現状と弊社の考えをご連絡させていただきました。

また、 Wi-Fi Alliance 向け Software リリース日程に関し、進展がありましたら直ぐにご連絡させていただきます。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

---

## 7. 2025-12-11 06:41

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki
**Attachments:** Revised_RF-PHY_TestPlan_IXIT_ICS(AT).xls

望月さんお疲れさまです。

台湾ラボ用RF PHY全項目のテストプランを添付します。

酒井差出人: Itsuo Sakai

送信日時: 2025年12月11日 11:54

宛先: Toshitaka Mochizuki

件名: [内部連絡] Re: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

望月さんお疲れさまです。

客先から「弊社所有の測定器はInterLabではなくアンリツのMT8852Bになりますが、RF?PHY/RCV/BV?07?Cを再度実施してみましたが、結果はPassでした。」

ということですのでRf PHYの1Mの受信受信試験項目と2Mに試験項目を台湾ラボで実施する提案を行ってはいかがでしょうか。

以下の文面案を望月さんの立場で修正しただいて客先へ返信してください。

ーーーー確認結果について現在Qualcommに問い合わせをしております。

⇒お手数をお掛けしますがよろしくお願いします。
また、弊社所有の測定器はInterLabではなくアンリツのMT8852Bになりますが、
RF/PHY/RCV/[ID]Cを再度実施してみましたが、結果はPassでした。

⇒これまでRF PHYのDTMモードFW開発あるいは動作確認をアンリツのMT8852B

おこなったテストサンプルで、InterLabでは正常にコマンド応答しないもののアンリツのMT8852Bでは試験にPassすることが複数回ありました。

幸い、台湾ラボのSIG認定テストシステムはシグナリングユニットにMT8852B

を用いいているため、過去の類似事例では台湾ラボでRF PHY試験を実施して

Pass結果を得ております。今回御社でMT8852BでのPassを確認頂いているとのことですのでおそらく問題なくPassすることと思います。

御社の同意を頂けましたら早速台湾ラボへの発送を進めますのでご検討の上、ご指示をお願いします。

ーーーー差出人: Shuhei Umeda

送信日時: 2025年12月11日 09:52

宛先: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

件名: RE: [RF試験合格完了] Re: 【ALAP】[UXC] Bluetooth 認証計画について(10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

確認結果について現在 Qualcomm に問い合わせをしております。

また、弊社所有の測定器は InterLab ではなくアンリツの [ID] になりますが、

RF‑PHY/RCV/BV‑07‑C を再度実施してみましたが、結果は Pass でした。

Qualcomm から何か情報などございましたら共有させていただきます。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, December 9, 2025 11:18 AM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご解析有難うございます。

入れ違いで申し訳ございませんんが、

こちらでの確認結果について別途メールをお送りいたしましたので、

そちらもご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

※【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, December 9, 2025 11:11 AM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

試験結果を共有いただきありがとうございました。

Test1 と 2/3 は送信コマンドに差異がありますが、どの試験も最終的に HCI Command に対して

NG(Unsupported Feature or Parameter Value) が返っています。

また、途中で応答が無かったり、意図しないコマンドが DUT から返っていたりするのが気になります。

[Test1]

HCI Reset

0: 18:23:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

OK

1 18:23:[ID] HCI_Event(1366):0x04 , 0x0e , 0x04 , 0x01 ,
0x03 , 0x0c , 0x00 ,

LE Set Default PHY

2: 18:23:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x00 ,

OK

3 18:23:[ID] HCI_Event(1366):0x04 , 0x0e , 0x04 , 0x01 , 0x1d , 0x20 ,
0x00 ,

HCI Reset

4: 18:24:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

Vendor Specific Command(Read Extended Features/Capabilities)

5 18:24:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x5f , 0x01 , 0x0b , 0xfc ,
0x00 , 0x00 , 0x26 , 0x58 , 0x00 , 0x00 , 0x30 , 0x00 , 0x68 , 0x09 , 0x70
, 0x00 , 0x01 , 0x1f , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x02 , 0x08 , 0x00 , 0x01 , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x0f , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00
, 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x60 , 0xea , 0x2c , 0x01 , 0x05 , 0x0f , 0x03 , 0x00 , 0xff , 0x00 , 0x40 , 0x06 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00 , 0x00
, 0x01 , 0xe8 , 0x03 , 0x14 , 0x14 , 0x00 , 0x00 ,

LE Set Default PHY Command

6: 18:24:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

No Response?

LE Set Default PHY Command

7: 18:24:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

Unsupported Feature or Parameter Value

8 18:24:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x0c ,

[Test2]

HCI Reset

0: 18:28:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

OK

1 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x03 , 0x0c , 0x00 ,

LE Set Default PHY Command

2: 18:28:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

OK

3 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

LE Read Transmit Power Command

4: 18:28:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

OK

5 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x06 , 0x01 , 0x1f , 0x20 , 0x00 , 0xd3 , 0x00 ,

LE Set Default PHY Command

6: 18:28:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

No Response?

LE Set Default PHY Command

7: 18:28:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

Unsupported Feature or Parameter Value

8 18:28:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x0c ,

[Test3]

HCI Reset

0: 18:31:[ID] HCI_Command: 0x01 , 0x03 , 0x0c , 0x00 ,

OK

1 18:31:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x03 , 0x0c , 0x00 ,

LE Set Default PHY Command

2: 18:32:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

OK

3 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

LE Read Transmit Power Command

4: 18:32:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

OK

5 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x06 , 0x01 , 0x1f , 0x20 , 0x00 , 0xa9 ,
0x01 ,

LE Set Default PHY Command

6: 18:32:[ID] HCI_Command: 0x01 , 0x1d , 0x20 , 0x01 , 0x13 ,

OK

7 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

LE Read Transmit Power Command

8: 18:32:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

Vendor Specific Command(Read Version Info)

9 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x12 , 0x01 , 0x00 , 0xfc ,
0x00 , 0x19 , 0x0c , 0x13 , 0x00 , 0x00 , 0x00 , 0xe6 , 0x38 , 0x01 , 0x02
, 0x10 , 0x02 , 0x0c ,
0x40 ,

LE Read Transmit Power Command

10: 18:32:[ID] HCI_Command: 0x01 , 0x1f , 0x20 , 0x00 ,

Unsupported Feature or Parameter Value

11 18:32:[ID] HCI_Event(1366):0x04 , 0x0e ,
0x06 , 0x01 , 0x1f , 0x20 ,
0x0c , 0x00 , 0x00 ,

Test 手順ですが、以下のコマンドを順に送信する理解で合っていますでしょうか？

1. HCI Reset

2. LE Set Default PHY Command

3. LE Read Transmit Power Command

4. LE Set Default PHY Command

5. LE Read Transmit Power Command

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, December 8, 2025 7:09 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

試験の方大変お待たせしております。

本日 DUT は DTM モードへの移行に成功し、 RF PHY/RCV/[ID] を 3 回実施いたしました。

しかしながら毎回の Fail の状況が異なっています。

Interlab Solution と Qualcomm tool
のログファイル ( ３回分 ) を別途お送りいたしますので以下の Password にてダウンロードください。

[ パスワード ]

VpUC8+RF

[ パスワード有効期限 ]

[ID] 19:05
まで

[ 送信 ID]

内容ご確認いただき、何かご対策ございましたらお知らせください。

どうぞよろしくお願い申し上げます。

※【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, December 4, 2025 7:08 PM

To: Shuhei Umeda ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

こちらお待たせしており大変申し訳ございません。

使用している PC 環境に問題があるか確認するため、別の

PC に新しく Qualcomm ソフトウェアをインストールし直して接続を試みておりますが、 RF PHY
手順書にある IP アドレスが表示されず、先に進めない状況のようです。

取り急ぎ状況をお知らせいたします。

どうぞよろしくお願い申し上げます。

【アリオン年末年始休業のお知らせ】

アリオン株式会社の [ID] 年末年始の休業は、 2025/12/27( 土）～ 2026/1/4( 日）となります。

2026 年新年の営業は 1/5 （月）からの営業となりますのでどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, December 4, 2025 6:19 PM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

RF PHY 試験の状況いかがでしょうか？

ご不明な点などございましたら、ご連絡いただけたらと思います。

引き続き、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Friday, November 28, 2025 6:30 PM

To: Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

試験状況のご連絡ありがとうございます。

状況理解いたしました。

来週も引き続きよろしくお願いいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, November 28, 2025 6:25 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

試験の方お待たせいたしまして申し訳ございません。

RF PHY 実施の手順が複雑で、先週末に全送信系および受信系 1 項目が Pass した状況に現状到達していない状況です。このためまだ酒井様からの追加確認ご依頼の対応着手に至っておりません。

来週引き続きご依頼内容を試行いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Wednesday, November 26, 2025 7:06 PM

To: Toshitaka Mochizuki ; Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

返信いただきましてありがとうございました。

本日作業いただいていること承知いたしました。

ご連絡お待ちしております。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, November 26, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai ; Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

試験の方お待たせしております。

本日作業しておりまして、 QUTS Status APP の挙動など確認実施中ですが、

まだうまく動作していないようです。

何かお伺いすることございましたら連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Wednesday, November 26, 2025 3:16 PM

To: Shigeyuki Sakai ; Itsuo Sakai ; Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再試験のスケジュールが決まっていましたらご連絡をいただけますでしょうか？

以上、よろしくお願いいたします。

From:
酒井重之 Shigeyuki Sakai

Sent: Monday, November 17, 2025 3:22 PM

To: Itsuo Sakai ; Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

酒井様お世話になります。

アルプスアルパイン酒井です。

＞ 再試験は現在スケジュールされている案件の合間の実施となりますことをご理解願います。スケジュールが決まりましたら望月からお知らせします。

承知いたしました。お手数おかけし恐縮ですが、よろしくお願いいたします。

酒井

From: Itsuo Sakai

Sent: Monday, November 17, 2025 1:53 PM

To: 酒井重之 Shigeyuki Sakai ; Toshitaka Mochizuki

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様アリオンの酒井です。いつもお世話になっております代わりに、以下 2 点をご確認していただきたいのですがよろしいでしょうか。
添付資料に従って DUT 筐体を開けて、 RF ケーブルの接続不良が無いかどうか見ていただけませんでしょうか。
再度、 BT
Classic の方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

⇒ 承知しました。再試験は現在スケジュールされている案件の合間の実施となりますことをご理解願います。スケジュールが決まりましたら望月からお知らせします。

以上よろしくお願いいたします。

差出人 :
Shigeyuki Sakai

送信日時 :
2025 年 11 月 17 日
12:58

宛先 :
Itsuo Sakai ; Toshitaka Mochizuki

件名 :
RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

酒井様、望月様お世話になります。

アルプスアルパイン酒井です。

詳細のご説明、どうもありがとうございます。

PC – InterLab 間の通信不具合の可能性は低そうであること、分かりました。

代わりに、以下 2 点をご確認していただきたいのですがよろしいでしょうか。

·
添付資料に従って DUT 筐体を開けて、 RF ケーブルの接続不良が無いかどうか見ていただけませんでしょうか。

·
再度、 BT Classic の方の受信系試験項目を少し試していただいて、問題無く実施できるか見ていただけませんでしょうか。

よろしくお願いいたします。

酒井

From: Itsuo Sakai

Sent: Thursday, November 13, 2025 9:42 PM

To: 酒井重之 Shigeyuki Sakai ; Toshitaka Mochizuki

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンの酒井です。いつもお世話になっております。

望月に代わって私から回答いたします。
ログのご提供、ありがとうございました。
一つ確認させてください。

Command: LEReceiverTestv1

Expected: 0x040EXXXXXXXX00
Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？
DUT からは正常に返したのに LE
Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

⇒ InterLab テストシステムでコマンドおよびコマンド応答の上記ログが表示されるのは試験冒頭の「Set DUT in Direct Test Mode」という表題に続く LEReceiverTestv1 コマンド部分で受信したコマンド応答が期待値と異なる場合のみです。このため Q 社アプリでは自動試験で全てのコマンドとコマンド応答をログ表示するものの試験項目の情報がなく、 InterLab

ログは各試験項目の 2402, 2440, [ID] ログに分散し、期待値と異なる場合のみて格納されるため対比するのが困難です。

自動試験に入る前に手動で LEReceiverTestv1 コマンドに対する応答を確認する段階では以下のように期待値の最終 Octed が 00→0C となる事例はありませんでした。さらに TRM 試験では自動試験で期待値と異なるコマンド応答は発生しないため、おそらく Q 社アプリで変換されることはないものと思います。

<InterLab>

15:16:03

Running Serial - HCI LE Receiver Test v1: 1

15:16:04 Sent: 0x011D200100

15:16:04 Expected: 0x040EXXXXXXXX00

15:16:04
Received: 0x040E04011D2000

15:16:04

LE Receiver Test v1: Completed. Result: Success

15:16:07

Running Serial - HCI LE Test End: 1

15:16:14 Sent: 0x011F2000

15:16:14 Expected: 0x040EXXXXXXXX00

15:16:14 Received:
0x040E06011F200C0000

15:16:14 Packets: 0x0000

15:16:14

LE Test End: Completed. Result: Success

<Q 社アプリのログ >

9: 15:12:[ID]
HCI_Command:0x01 , 0x1d , 0x20 , 0x01 , 0x00

10 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x04 , 0x01 , 0x1d , 0x20 , 0x00 ,

11 15:12:[ID] HCI_Command:0x01 , 0x1f , 0x20 , 0x00 ,

12 15:12:[ID] HCI_Event(1366):0x04 , 0x0e , 0x12 , 0x01 , 0x00 , 0xfc , 0x00 , 0x19 , 0x0c , 0x13 , 0x00 , 0x00 , 0x00 , 0xe6 , 0x38 , 0x01
, 0x02 , 0x10 , 0x02 , 0x0c , 0x40 ,

13 15:12:[ID] HCI_Command: 0x01 , 0x1f
, 0x20 , 0x00 ,

14 15:12:[ID] HCI_Event(1366): 0x04 , 0x0e
, 0x06 , 0x01 , 0x1f , 0x20 , 0x0c , 0x00 , 0x00 ,

酒井さんの懸念を確かめるには、 PC-InterLab 間に RS232 ロガーを設置して送出データを逐一記録後、 Q 社ツールのログと比較することが必要ですが当社ではすでにシリアル通信ロガーあるいは RS232 プロトコルアナライザを持ち合わせておりません。

以上回答いたします。

差出人 : Shigeyuki
Sakai

送信日時 : 2025 年 11 月 13 日
20:26

宛先 : Toshitaka
Mochizuki

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ログのご提供、ありがとうございました。

一つ確認させてください。

Command: LEReceiverTestv1

Sent: 0x011D20010C

Expected: 0x040EXXXXXXXX00

Received: 0x040E04011D200C

上記のような期待値と異なる値は、 PC 上の LE
Direct Mode のログにも現れておりましたか？

DUT からは正常に返したのに LE Direct Mode で何か変換されてしまってないか？を、無いとは思いますが、確認しておきたいです。

（この Logging にも現れていたかどうか）

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 6:58 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

お待たせいたしました。

RCV ログをお送りいたしますので、こちらの内容の確認、解析をいただけますでしょうか。

Password は追ってお知らせいたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, November 13, 2025 5:01 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様梅田様いつもお世話になっております。

アリオンの望月です。

以下連絡いたします。

FTM モード投入後に TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行後、 Q 社アプリの Handshake=DTR に合わせて Interlab の

DTR=True に設定した結果、送信 TRM 系試験項目は実施でき、 1M モードの全 4 項目が Pass しました。

残る受信 RCV 系は不思議なことに DUT が試験セットアップ時の InterLab からの DTM コマンドに正常応答しないために試験 Pass に至りません。

TRM 試験が Pass 完了したということは、 DUT <-> PC <-> InterLb
間の電気的・論理的接続は正常ということになります。しかし RCV コマンドに対する DUT の応答が InterLab に届くものの、期待値通りの正しい応答ではないという症状です。考えられるのは、「DUT 内蔵のテスト FW の不具合で、

Interlabo からの DTM コマンドに正常応答していない」と推測されます。

現在下記 RCV 試験項目を実施中で、明日 Fail ログをまとめて送付いたしますので、お手数ですがそのログとともに V 社経由 Q 社にテストサンプル内の DTM

FW の解析依頼をお願いいたします。

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

RFPHY/RCV/[ID]

以上ご確認どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 6:53 PM

To: Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

種々のご確認、こちらこそ大変恐れ入ります。

PC 側との兼ね合いがあるとのこと承知いたしました。

明日改めてこちらの方法でも確認させていただきます。

台湾作業の前にクリアできればと思います。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, November 12, 2025 6:48 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

（メインで担当中の梅田が今週末まで不在のため、私から回答いたします。窓口がしばしば変わりご迷惑をおかけします。）

色々とご確認ありがとうございます。

解決に至るかどうか分からないのですが、過去遭遇した接続不良時の対応を共有いたします。

そのときは、 Windows PC 側の Port 設定が重複していたようで、異なる IP
Address を DUT に設定し直すことで接続が回復しました。

そのためのマニュアル、マクロ、 bat ファイルをお送りいたします。

マニュアルの BLE measurement procedure (2)
シートをご覧ください。

下記ケーブルが同梱されていたかと思いますが、最初にこのケーブルを使用して DUT の IP
Address を [ID] に変更します。その上で BLE 試験用の接続を行う、というものです。

また、現地確認のご提案もありがとうございます。

上記でも解決が見られなければ御社へ伺うことも検討中です。

お手数おかけしますが、接続の確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 2:55 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

いただいたログからは一旦 Bluetooth-FTM モードに入るとノーマル操作ができなくなり、

TeraTarm で uxc_enable_synergy.ttl というマクロスクリプトを発行して DUT のテスト FW を通常 FW に戻さないと。電源再投入後に通常動作しないと読み取れる可能性があるようだということが判ってきましたので、

こちらではこの点を引き続き確認するよう進めます。

他になにか必要な操作などございましたらご教示お願い申し上げます。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, November 12, 2025 11:40 AM

To: Shuhei Umeda ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

DUT との接続を一旦すべて外してやり直したり、システムや PC の電源を入れ直したりを何回かやってみましたが、

HCI_Event の受信はできませんでした。

何か他に考えられる状況はございますでしょうか。

状況に応じ、ご来訪でのご確認も可能です。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

HCI_Event が表示されていないということは、 PC から UXC に対して HCI_Command が送信できていないか、

UXC から PC への HCI_Event が受信できていないかになるかと思います。

一度 HCI_Event は受信できていましたので、接続状態を再確認いただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 11, 2025 1:38 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご教示ありがとうございます。

現在確認作業をしておりますが、

本日朝から手順に従い &quot;Bluetooth Test Mode&quot; を再度実行しましたが、昨日はあった &quot;HCI_Event&quot; の行が表示されなくなりました。

どのような原因、確認、復旧手段があるかご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, November 11, 2025 8:59 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

弊社では InterLab システムを使用したことがないのですが、

LE Direct Mode （Qualcomm Tool）の Log 上は、送信 / 受信ともに正常に動作しているように見えます。

それに対して InterLab システムの画面上は“ Received ”に何も表示が無いので、 InterLab システムは受信ができていないように見えます。

よって、 PC と InterLab 間のケーブルの接続状態を再度ご確認いただけますでしょうか？

また、過去 HM26 モデルでは同じテストシステムで送受信は問題なかったでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, November 10, 2025 5:04 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

下記の DUT との接続で、 InterLab システムとの通信を行おうとしていますが fail となります。

何か確認すべき点や修正すべき点などございましたらご教示いただけますでしょうか。。

InterLab システムとの接続いただきました &quot;Bluetooth Connection Diagram&quot; ( 添付 ) の真ん中の下側の PC の USB ポートと InterLab システムの USB ポートを接続。

使用ケーブル：

[ID] 変換ケーブル⇔ [ID] メス - メスケーブル ( クロス )
⇔ [ID] 変換ケーブル

InterLab システムから &quot;LE Reset&quot; を実行。

QUTS Status App の画面

InterLab システムの画面ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:48 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

情報いただきありがとうございます。

接続できるようになったとのこと承知いたしました。

引き続きよろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:13 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

RF PHY の方ですが、 ご連絡いただいた内容を実行したところ、下記の通り接続できましたのでお知らせします。引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 5:02 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様承知いたしました。

早速のご対応感謝いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 5:00 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

本日サンプル発送いたします。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 11:01 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様はい。ディスプレイ部、付属品含めてとなります。

お手数ですが、ご対応よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, November 6, 2025 10:58 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様ご連絡有難うございます。

一式ということはディスプレイ部、付属品も含めてという認識でよろしいですね。

発送は可能と思いますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, November 6, 2025 10:53 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT 試験用に弊社から送付しました DUT 一式ですが、

返却いただくこと可能でしょうか？

お手数ですが、ご確認をお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Wednesday, November 5, 2025 8:58 AM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

QUTS のバージョンは最新になっていますでしょうか？

Qualcomm Package Manager を起動して、” Updates Available ”タブを選択し、

もし最新のバージョンが存在する場合は、最新版をインストールしてみてください。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, November 4, 2025 7:12 PM

To: 'Toshitaka Mochizuki' ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきましてありがとうございます。

QUTS が動作するところまで進んだようで良かったです。

Step7 までは手順書の通り進んでいるのに Step8 で IP アドレスが表示されないということですね。

即答できないのでこちらでも調査してみます。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, November 4, 2025 6:27 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

現在再確認作業を行っております。

UXC10 の [ID] のセットアップを、いただきました手順書で行っておりますが、

ステップ 8 で、 COM Port のところで IP アドレスを選択するように書いてあるのですが、

下記の通り、 IP アドレスが表示ず選択できません。

どうすれば、 IP アドレスを選択できるようになるかを、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 1:49 PM

To: Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

Qualcomm Package Manager の検索 Window に QUTS を入力すると、該当するツールが絞り込まれると思います。

お試しいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 1:35 PM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

QUTSStatusApp ですが、 Qualcomm 社のサイトの Software のダウンロードを探しておりますが、複数のパッケージが表示されますが、そのものズバリのものが出てきません。

こちらは何のパッケージに入っているかご教示いただけますでしょうか。

お忙しいところお手数ですが、ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Shuhei
Umeda

送信 : 2025
年 10
月 31
日 ( 金曜日 ) 13:18

宛先 : Toshitaka Mochizuki ;
Hsiaoting Huang ;
Shigeyuki Sakai

件名 : RE: [RF 試験合格完了 ]
Re: 【ALAP】 [UXC] Bluetooth
認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

再度ご確認いただきましてありがとうございます。

Qualcomm ID を取得されていること承知いたしました。

ということは、 Qualcomm Package Manager を使用して QUTS のインストールはできそうでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 31, 2025 11:43 AM

To: 梅田修平 Shuhei Umeda ;
Hsiaoting Huang ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は終日不在としてご迷惑をお掛けいたしました。

以下回答となります。

ご確認どうぞよろしくお願い申し上げます。
もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。
ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、御社が Qualcomm ID をお持ちでないのは確かでしょうか？
基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。
QRCT が使えているので、その認証は Pass していることになります。

⇒先のメールでアリオンは Qualcomm ID を取得していないとお伝えしましたが御社 HM26 案件で営業の王が Qualcomm ID を取得しておりました。大変失礼しました。
使用中の QRCT のバージョンについて教えていただけますでしょうか。

⇒別途調べてお答えします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 31, 2025 10:45 AM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様 / 望月様お世話になっております。アルプスアルパインの梅田です。

ご確認いただきましてありがとうございました。
Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。
そのため、本日は QRCT を使用して BLE DTM モードへの移行を試しました。

誤解を招いてしまったかもしれません。

QRCT で QUTS の確認はできません。

QRCT がインストールされているのであれば、 QUTS も一緒にインストールされているのではないか、との推測になります。

Qualcomm 社のダウンローダー上、 QUTS が QRCT にも含まれるような構成になっているためです。

お手数でございますが、再度、以下の Path に QUTSStatusApp.exe があるかどうかご確認いただけますでしょうか？

C:\Program Files (x86)\Qualcomm\QUTSStatusApp\QUTSStatusApp.exe

もし存在しない場合、 QUTSStatusApp の御社への提供方法を検討いたします。

ただ、 QRCT をお持ちであるということは、何らかの方法で QRCT をインストールされたと思いますが、

御社が Qualcomm ID をお持ちでないのは確かでしょうか？

基本的に Qualcomm のツールは起動時にネットワークを経由して、 Qualcomm サーバーと何らかの認証を行っていると思います。

QRCT が使えているので、その認証は Pass していることになります。

使用中の QRCT のバージョンについて教えていただけますでしょうか。

また、御社と Qualcomm との間に契約関係はございますでしょうか？

以上、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 5:14 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様お世話になっております。

アリオンのジェシーです。

ご返信ありがとうございます。

＞現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

現在実施しようとしている試験は BLE Measurement ([ID]) です。

また、ラボに確認したところ、 Bluetooth Measurement (RF) 試験は既に実施完了しまして、テストレポートも先日提出させていただきました。

＞手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

BLE Measurement については、 Step
６マクロの実施（uxc_BLE_FTM_Mode.ttl）まで成功しました。

Step 7: Run QUTS Status App」と記載されていますが、ラボに QUTS Status App がないため、貴社に確認したところ、 QRCT でも QUTS の確認が可能とのことでした。

そのため、本日は QRCT を使用して BLE DTM モードへの移行を試しました。

但し、 BLE Measurement の測定手順では QUTS Status App での設定方法が指定されているため、 QRCT の画面上でどのように設定して BLE
DTM モードへ移行すればよいのかが分かりませんでした。そのため、本日再度お問い合わせさせていただきました。

大変恐縮ですが、現状（QUTS Status App 無し）で BLE DTM モードへの移行方法があればお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shuhei Umeda

Sent: Thursday, October 30, 2025 4:28 PM

To: Hsiaoting Huang ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオンジェシー様お世話になっております。アルプスアルパインの梅田です。

望月様の代理でのご確認ありがとうございます。

Qualcomm ID はお持ちでは無いが、 QRCT のインストールはできた、または QRCT は既にお持ちだったということでしょうか。

QRCT の画面を添付いただきましたので、 QRCT が動いている前提でお話しますが、

添付しました資料は既に展開させていただいている QRCT の動作手順書です。

現在実施しようとしている試験は、 Bluetooth Measurement でしょうか、それとも BLE Measurement でしょうか？

手順書に記載の手順において、どこまでが成功していて、どこで失敗しているのかの情報をいただけますでしょうか。

お手数ですが、よろしくお願いいたします。

From: Hsiaoting Huang

Sent: Thursday, October 30, 2025 4:09 PM

To: 酒井重之 Shigeyuki Sakai ;
梅田修平 Shuhei Umeda

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様、

お世話になっております。

アリオンのジェシーです。

ご不便をお掛けして申し訳ございません。

本日望月が社内不在のため、代理にてラボのフィードバックをご連絡いたします。

＞【BLE】

＞御社にて Qualcomm からツールを直接入手することは可能でしょうか？

申し訳ございません。内部で確認したところ、弊社は Qualcomm ID を持っていないため、 Qualcomm からツールを直接入手できないです。

メールでご提示いただいた方法（QRCT の利用）を試しましたが、接続に失敗しました。添付の Screenshot をご参照ください。

確認したところ、 USB ケーブルで制御用 PC に接続していますが、 PC 側で USB デバイスとして認識されていません。

また、 USB Driver.exe は QRCT フォルダ内に存在しないようです。

念のため、「Select USB Driver.exe」ボタンをクリックし、 QC.BluetoothLE_DirectMode.exe を選択して接続を試みましたが、 Failed device connection と表示されました。

ご確認いただき、 QRCT で DTM モードへ移行する手順をお教えいただくことは可能でしょうか。

よろしくお願いいたします

From: Shigeyuki Sakai

Sent: Monday, October 27, 2025 1:59 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

本日、梅田が不在ですので、私からご回答します。

【IOPT】

添付のファイルが過去に Volvo から提供されていたのですが、御社へ提出していなかったと思います。申し訳ありません。

“adb install BlueSPP.apk”

については、 PDF の 3 ページ目に記載されております。

一度ご確認いただけますでしょうか。

【BLE】

御社にて Qualcomm からツールを直接入手することは可能でしょうか？

通常ですと QPM(Qualcomm Package Manager) というツール経由で PC にインストールします。

（そのためツールインストーラーをお渡しすることができないことも背景です）

QUTS は下記 QRCT をインストールすることで一緒に導入されます。

QRCT は Classic の試験でご使用いただいたと思いますので、 QUTS もご確認可能ではと思います。

一度ご確認いただけますでしょうか。

なお、 BLE 試験用にご提供しました手順書の &quot;Notes
on QRCT tools&quot; シートに QRCT のインストールの説明を記載しておりますので、合わせてご確認をお願いいたします。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:31 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

立て続けで申し訳ございません。

[ID] 試験に関して、メールでいただいている QUTS Status App と Run Bluetooth LE Direct
Mode テストツールがまだご提供いただいていないようです。

ご確認の上、ご提供お願いできますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Monday, October 27, 2025 10:07 AM

To: Shuhei Umeda ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

10 月 21 日 19:42 の梅田様からのメールでは、「IOPTTestguide.pdf に記載されている BlueSPP.apk をインストール」という記述がありますが、

こちらで探しておりますが、これら資料をいただいていないようです。

もしお送りいただいているようでしたら、そのメールご送付の日時をお知らせいただけますでしょうか。

また IOPTTestguide.pdf 以外にも関連する試験で必要なファイルがございましたら併せてご提供いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 7:29 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

まずは adb が正常に動作できるようになったとのこと承知いたしました。

こちらかの情報に誤りがありまして申し訳ございませんでした。

また、 SPP の再試験ありがとうございました。

結果を再度 V 社と共有いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 7:02 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

&quot;USB-A 2.0&quot; というラベルの付いたケーブルを使用したところ、 adb install
はできましたが、

再度 SPP のプロファイル試験を実行しましたが、結果は以前と同じでした。

log のファイルを添付いたしますので、ご確認いただけないでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Friday, October 24, 2025 10:39 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様ご確認いただきありがとうございました。

こちらのケーブルになります。

このケーブル経由で adb 関連のコマンド操作を試してみていただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 24, 2025 9:51 AM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

添付のケーブルがございましたが、こちらのことでよろしいでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 7:08 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

何度もご確認いただきましてありがとうございます。

再度、 PC と DUT の接続方法を確認させてください。

弊社から送付した DUT ですが、 USB ケーブルが 4 本あったと思います。

DEBUG SAIL

DEBUG HKP

DEBUG MD

以外のもう 1 本のケーブルはございますでしょうか？もしよろしければ写真を撮って送っていただけると助かります。

DEBUG MD とご案内いたしましたが、残りの 1 本が DUT 側の USB 機能として使うもので、

こちらのケーブルでないと adb が動作しない可能性がございます。

お手数をおかけいたしますが、 4 本目のケーブルのご確認をお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 6:51 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

お送りいただきました資料を確認し、 adb shell settings put global development_settings_enabled 1&quot; コマンドを送りましたが、以下のエラーが表示されます。

• error: no devices/emulators found

DUT や PC などで、他に確認すべき点や、設定すべき点がございましたら、ご教示いただけますでしょうか。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 1:19 PM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

添付ファイルの P.2 に Basic DUT operations が記載されておりますが、

Developer Mode は Enable になっていますでしょうか？

adb shell settings put global development_settings_enabled 1

を実行してから

adb install bluespp.apk

を試してみていただけますでしょうか？

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 12:55 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

ご連絡いただきました &quot;DEBUG MD&quot; の USB ケーブルを PC に接続し、 &quot;adb install bluespp.apk&quot; を実行したところ、下記のエラーが表示されました。

• adb: connect error for write: no devices/emulator found

また、 &quot;adb devices&quot; コマンドを実行いたしましたが、 &quot;List of attached devices&quot; の下に何も表示されず、認識されていないようです。

PC や DUT で、他に設定する所などがございましたら、ご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Thursday, October 23, 2025 11:53 AM

To: Toshitaka Mochizuki ;
Itsuo Sakai ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

ご確認ありがとうございます。

DEBUG MD と PC を接続してください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, October 23, 2025 11:51 AM

To: Itsuo Sakai ;
梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

昨日は不在といたしまして申し訳ございません。

以下確認事項がございますので、

ご回答いただけますでしょうか。

BlueSPP.apk をインストールするには、 DUT の下記の 3 本の USB ケーブルのどれを PC に接続すればよいかご教示ください。

DEBUG SAIL
DEBUG HKP
DEBUG MD

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 5:25 PM

To: Shuhei Umeda ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
Connection Diagram ですが、 RF
PHY Test System を追記したものを準備いたしました。
こちらを参照いただけたらと思います。

⇒ 何度もお手数をお掛けしました。これで RF
PHY 試験の接続系統図が明確になりました。ありがとうございました。

引き続きよろしくお願いいたします。

酒井差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 16:00

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様

Connection Diagram ですが、 RF PHY Test System を追記したものを準備いたしました。

こちらを参照いただけたらと思います。

以上、よろしくお願いいたします。

From:
梅田修平 Shuhei Umeda

Sent: Tuesday, October 21, 2025 2:33 PM

To: 'Itsuo Sakai' ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

Operation Manual ですが PDF に変換しました。

こちらをご参照ください。
RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。

使用いたします。

添付の Bluetooth measurement procedure.pdf、 BLE measurement procedure.pdf
を参照ください。

操作手順の中に Ethernet に関する操作がございます。
ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の
USB 接続部分は反映されていないという理解で間違いないでしょうか。

おっしゃるとおりです。 Bluetooth Connection Diagram に反映されておりません。
そうあれば私の最初からの質問であるテストシステムの Serial
over USB
の接続先ですが、それは PC
running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

はい。その理解で合っています。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 1:43 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。
RF PHY Test System との接続は以下の図をご参照ください。
DUT と PC
running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。
RF PHY Test System と DUT は RF のみ接続します。

⇒ RF 試験では QDART と DUT は Ethernet 接続でしたが、 RF
PHY 試験ではさらに USB 接続するということになりますが、 Ethernet 接続は接続しているだけで使わないということでしょうか。
そして PC running QDART と RF
PHY Test System は直接 RS232、 GPIB での接続となります。

⇒ HM26 でも同じ図の Q 社マニュアルを使いました。しかし、 DTM モードでは GPIB 経由のコマンドの定義はなく、 Serial
over USB を含む Serial

(UART) 経由でのコマンドが定義されそれに従って DUT を制御しています。

このため DUT と PC および RF
PHY テストシステムは下図のような接続系統図となります。

ここで確認ですが 11:40AM のメールの接続ブロック図には、上図の青色の

USB 接続部分は反映されていないという理解で間違いないでしょうか。

そうあれば私の最初からの質問であるテストシステムの Serial over USB

の接続先ですが、それは PC running QDART の空いている USB 端子に接続すれば良い ( もちろん QDART の DTM 試験モードで Serial ポートを設定 ) との理解でよろしいでしょうか。

以上ご確認をお願いします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 12:55

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

RF PHY Test System との接続は以下の図をご参照ください。

DUT と PC running QDART 間は USB conversion harness を使って USB
Serial で接続いたします。

RF PHY Test System と DUT は RF のみ接続します。

そして PC running QDART と RF PHY Test System は直接 RS232、 GPIB での接続となります。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Tuesday, October 21, 2025 12:01 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

ご返信ありがとうございます。
制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。
ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

⇒ 図では黄色マーカー部分の一端が PC,
他端が DUT ですが、文面から推測すると下図かと思われますが、正しいでしょうか ?

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 21 日 11:40

宛先 : Itsuo
Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。
以上のようにご送付いただいた Connection
Diagram では RF PHY の
DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。

制御結線についてですが、 RF テストシステム -DUT 間の結線は以下の画像の黄色マーカー部分になります。

ちょうどご質問をいただいた USB conversion harness-USB Type-A ケーブルの部分です。

DUT
– USB conversion harness
– USB Type-A ケーブル – PC
で結線され、 USB Serial として PC と DUT 間の通信が可能となります。

後ほど、 Operation Manual を PDF 化して送付するようにいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Monday, October 20, 2025 7:19 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: Re: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様アリオンの酒井です。いつもお世話になっております。

先程の質問は私の Excel のバージョンが古いせいか以下の図が表示されたためで、「薄緑線の分岐」とか「薄緑線の上方の接続先」が何のことやらと思われたと思います。お詫びします。

しかし、 RF PHY 試験は認証テストシステム及び簡易なアンリツ

BT テスタでも RF 測定系とは別に、 UART/COM ポート接続が必須で、

HM26 でも下図のように外部 PC ＋ Q 社テストアプリを Bridge にして

DUT<->(Eternet)<->PC<->(Serial over USB)<->RF PHY テスターという接続を行いました。その際の DTM モードマニュアルを添付します。

以上のようにご送付いただいた Connection Diagram では RF
PHY の

DTM(Direct Test Mode) 試験に必須の RF テストシステム -DUT 間の制御結線が不足しています。ご送付の Connection Diagram はおそらく電波法 /FCC 試験時のオープンループ試験用のものと推測されます。再度 DTM モードのセットアップ方法をご確認ください。

以上よろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 20 日 18:35

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
[RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様

SPP のレポートの送付ありがとうございました。

内容確認して返信いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 6:17 PM

To: 梅田修平 Shuhei Umeda ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様いつもお世話になっております。

アリオンの望月です。

SPP のレポートをお送りいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Monday, October 20, 2025 5:16 PM

To: Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

IOPT の再試験の実施ありがとうございました。

SPP についてですが、再試験結果のレポートを送付いただくこと可能でしょうか。

V 社側に連絡して事前条件や SW の差分の有無について確認を依頼したいと思います。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, October 20, 2025 5:12 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

IOPT 試験について連絡です。

御社からご送付いただいた SPP の PTS レポートと同じ ICS 設定であることを確認して v8.10.2 で再試験を実施しましたところ、 MAP と PBAP は Pass

しましたが SPP は Pass しませんでした。

SPP の PTS 試験では、スタート前に DUT の接続済機器一覧から PTS を削除するなど、試験に先立って何か操作が必要なのでしょうか？

また、ご送付いただいた Pass レポートを得られた DUT の SW が当社の DUT

の SW から更新されているようなことはありませんでしょうか。

もし原因が追求できない場合にはご提供いただいた SPP の PTS レポートを認証登録のエビデンスに使うとともに、それをログにしてアリオンレポートを発行させていただきたいと存じます。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki
Sakai

Sent: Monday, October 20, 2025 1:36 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご返却、どうもありがとうございました。

弊社側での内部データ更新が完了しまして、先ほど望月様宛での発送手続きが完了したところです。

ヤマトお問合せ No : [ID]

併せて、 RF PHY 試験の手順書もお送りします。

ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 15, 2025 1:40 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご確認ありがとうございます。

承知いたしました。

更新いただいた後、 RF PHY 試験の日本分実施後、台湾での試験向けに発送予定です。

その際に該否判定書と製品仕様書が必要になります。

今回は RF 試験についてはモニタ部分については輸出は必要なかったとおもいます。

また、先日お伝えいたしました、プロファイル（IOPT）試験についてのご修正についてもそちらのサンプルの返送が必要でしたらおしらせください。

以下 RF 試験機の返送になります。

運送会社：佐川急便お問い合わせ送り状 No.[ID]

酒井様宛て一個口引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Wednesday, October 15, 2025 12:56 PM

To: Toshitaka Mochizuki

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

＞ 御社へ一旦サンプルをお返しするという事だったと存じます。

はい、お手数おかけしまして申し訳ありませんが、そのように進めさせてください。

RF 試験用のサンプルは以下の写真が示す DUT のみで大丈夫です。

ご返却の宛先は私でお願いいたします。

福島県いわき市好間工業団地 20-1

アルプスアルパイン株式会社 DC1 設計部酒井重之あと、 BLE
オプション機能の試験のため DUT を台湾に発送されると思いますが、弊社から該非見解書をお出しするということでよろしいでしょうか。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 14, 2025 6:28 PM

To: 梅田修平 Shuhei Umeda ;
Itsuo Sakai ;
酒井重之 Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様酒井様いつもお世話になっております。

アリオンの望月です。

RF 試験が完了いたしましたが、 RF PHY 試験実施のため御社へ一旦サンプルをお返しするという事だったと存じます。

RF 試験用のサンプルですが、 Full セットでお返ししたほうがよろしいでしょうか。

必要な物のみでよろしければご指定いただければそちらのみお返しいたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shuhei Umeda

Sent: Tuesday, October 14, 2025 9:52 AM

To: Itsuo Sakai ;
Toshitaka Mochizuki ;
Shigeyuki Sakai

Subject: RE: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン酒井様お世話になっております。アルプスアルパインの梅田です。

ご連絡いただきありがとうございました。

RF 試験が合格完了とのこと承知いたしました。

引き続き、 RF PHY の実施、よろしくお願いいたします。

以上、よろしくお願いいたします。

From: Itsuo Sakai

Sent: Friday, October 10, 2025 7:35 PM

To: 梅田修平 Shuhei Umeda ;
Toshitaka Mochizuki ;
酒井重之 Shigeyuki Sakai

Subject: [RF 試験合格完了 ] Re:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン梅田様、酒井様アリオンの酒井です。いつもお世話になっております。

望月に変わり私からお知らせします。

先程 RF 試験が合格完了しましたのでお知らせします。来週 RF
PHY(1M)

を実施し、 Pass 後に台湾ラボへ送って (2M,
Coded) を実施する予定です。

引き続きよろしくお願いいたします。

差出人 : Shuhei
Umeda

送信日時 : 2025 年 10 月 10 日 17:38

宛先 : Toshitaka
Mochizuki ;
Shigeyuki Sakai

件名 : RE:
【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アリオン望月様お世話になっております。アルプスアルパインの梅田です。

酒井に代わりまして本件返信させていただきます。

まず試験日程のイメージの共有ありがとうございました。

おおよそこれぐらいの日程感で試験が進むこと承知いたしました。

次に、 Bluetooth IOPT 試験の結果のご連絡ありがとうございました。

Fail、 [ID] となった項目についてレポート内容を確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 4:49 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

今回のケースで問題なく試験が進んだ場合は以下の様な時間的イメージとなります。（日本分のみ）

RF： 4 日程度

[ID]： 3 日程度

Profile： 2 日程度状況により途中中断、問題箇所再確認などで時間は大きく変化する場合があります。

ご了承ください。

Bluetooth IOPT 試験について以下エンジニアから報告がございます。

★ ALAP(UXC10) の IOPT 試験で 18 項目中 14 項目は Pass しました。

残る下記項目が Fail、または [ID] となっております。

・ IOPT/MAP/MCE/CGSIT/SFC/[ID]

・ IOPT/PBAP/PCE/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVA/CGSIT/SFC/[ID]

・ IOPT/SPP/DEVB/SDPR/[ID]

上記の PTS レポート ( ログ付 ) を添付しますので、ご確認および解析をお願いします。特に製品の SDP レコード内容を重点的にご確認ください。

PTS の IXIT の設定で対処できるものはその旨お知しらせください。 FW 改修が必要な場合は改修 FW をご準備ください。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 2:20 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご確認どうもありがとうございました。

各試験の想定日数を教えていただく事は可能でしょうか。

問題発生により変化することも承知しておりますので、特に問題無く進んだ場合の日程感で構わないです。

RF ・・・

RF PHY ・・・

IOPT ・・・

RF PHY 試験前の DUT 更新時期や、 IOPT 試験後ディスプレイご返却のタイミングを知っておきたいためです。

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 2:08 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご連絡有難うございます。

[ID] の方、受け取っております。

RF PHY 試験の方のテストプランも作成いたしました。

DUT サンプルの運用につきましてはご希望通り対応予定です。

何かございましたら改めて連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Friday, October 10, 2025 1:57 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

DUT のご確認、どうもありがとうございました。

試験のご対応を引き続きよろしくお願いいたします。

別メールにしてしまいすみませんでしたが、

Questionnaire の更新と DUT 更新対応のご相談をご連絡しておりますので、

そちらもご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Friday, October 10, 2025 1:10 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

お待たせしております。

その後こちらで試行いたしまして、 RF 試験開始の段階まで進めることができたようです。

ＲＦ試験実施の上何かございましたら随時連絡いたしますのでしばらくお待ちください。

また、ＩＯＰＴ試験の方も動作確認いたしました。

特にこちらも問題ないようです。

取り急ぎ連絡いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Thursday, October 9, 2025 6:58 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ご指示有難うございます。

昨日連絡いたしました DUT の通信接続ができない問題について、

電流の制限を調整したところその部分につきましては正常に動作することが確認できました。

ただ、その先で確認を要する状況となっておりますので、もう少しはっきりしましたら改めて連絡いたしますので、もうしばらくお待ちいただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Thursday, October 9, 2025 3:18 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

弊社での似た過去事例にもとづき、少しご確認お願いしたい点がございます。

·
Wake_up 端子の GND 接続確認

DUT の Wake_up ラインが電源の GND に接続されていることをご確認お願いします。

接続が外れると DUT が Sleep 動作に入る動きをしますため。

·
電源投入後、 30 秒待機電源投入後、ソフト起動に 30 秒程度時間がかかりますので、それを待ったのち、操作を開始してみていただけますでしょうか。

以上、２点のご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 6:01 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

RF
試験の DUT Setting で以下の現象が起きております。

・「(UXC)AT operation manual_for_BT_rev001.xlsx」内の手順５実施後、「root@lemans:~#」が表示されず、通信接続ができません。

TeraTerm は最新バージョン (5.5.0) を使用しております。

TeraTerm を別のバージョン (5.4.1) で確認しましたが、同様の現象が起こります。

手順 5 実施中にも切断されることがあります。

こちら対策をご教示いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Wednesday, October 8, 2025 5:54 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

★ RF PHY は確認中で未記入項目があって Test
Plan は作成できません。

[ID] の未記入（TBD）の項目のご確認状況はいかがでしょうか。

★サンプルは本日到着し、セッティング、動作確認を行っております。

確認結果わかりましたら連絡しますのでお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 9:11 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様立て続けて申し訳ございません。

RF 試験の DUT 操作マニュアルおよび TeraTerm 用マクロを提出します。

ご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Tuesday, October 7, 2025 2:54 PM

To: 'Toshitaka Mochizuki'

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

以下、トピックごとにご連絡いたします。

■ DUT list について間違い修正や写真追加等で更新しました。

添付しました 2025/10/07 のもので差し替えをお願いいたします。

■ DUT 機材発送について

RF 試験用と IOPT 試験用の DUT 機材を別々に発送しました。

以下、ヤマトの送り状番号です。

■ [ID] について別メールですが質問事項へのご回答、ありがとうございました。

（現在の記述で問題無いと理解いたしました）

■ IOPT 試験用の DUT 操作マニュアルについて添付の AOSP_Bluetooth_User_Manual_1_0_0.pdf が試験用の DUT 操作マニュアルです。

不明点などありましたら、ご連絡お願いいたします。

■ RF 試験用の DUT 操作マニュアルについて明日を目標に、現在準備中です。

整い次第、お送りいたします。

以上、ご確認をよろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Tuesday, October 7, 2025 11:06 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

ドキュメントのご送付ありがとうございます。

試験サンプルの接続、操作マニュアルのご提供もお待ちしております。

（可能であれば英文、もしくは中文併記でいただけますと助かります。）

引き続きどうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 9:24 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご回答ありがとうございます。

送信データ量が大きくなりすみません。

■機材提出票および DUT list

機材提出票を作成いたしました。

RF DUT 一式の方はのちのち台湾に行く予定のため、 IOPT
DUT とは別で扱えた方が好ましいと思いましたため、そのようにしました。

また、 WFA メールスレッドの方でありました税関対策の意味も込めて DUT
list を作成しました。 RF DUT の接続写真はのちほど載せるようにします。

お気づきの点等ございましたらご連絡ください。

■ [ID]

こちらも作成いたしました。

下記のご確認をよろしくお願いいたします。

Antenna だけの値を持っていないことから、 Cable
Loss も含めた値となります。こちらで構いませんでしょうか？

このケーブルは、製品のアンテナケーブル or 測定用ケーブルどちらになりますでしょうか？添付ファイルには、一旦、測定用ケーブルのロスを書いています。

BLE の試験モード検討中のため、今時点 TBD とさせてください。

以上、よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 6:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

＞・ RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

★管理を共通にしてよいのであれば、最終的なご提供物を１冊にまとめていただいても問題ございません。必ず数量、それぞれの識別が出来るようにサンプル本体や付属品にラベルなどを貼ってください。

＞・ IOPT 試験は Questionnaire はございますか？

★こちら ICS を既にいただいているので特に Questionnaire は必要ございません。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Shigeyuki Sakai

Sent: Monday, October 6, 2025 4:54 PM

To: Toshitaka Mochizuki

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

望月様お世話になります。

アルプスアルパイン酒井です。

ご指示ありがとうございます。

以下、確認させてください。

·
RF 試験と IOPT 試験用に、 DUT 一式を別々に提出する予定です。

評価機材提出票も別々に作成する、でよいでしょうか？

·
IOPT 試験は Questionnaire はございますか？

よろしくお願いいたします。

酒井

From: Toshitaka Mochizuki

Sent: Monday, October 6, 2025 11:47 AM

To: Misumi Sato ;
酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Bluetooth 認証計画について (10/6)

アルプスアルパイン酒井様いつもお世話になっております。

アリオンの望月です。

先週はお打ち合わせありがとうございました。

Wi-Fi と一旦メールを分けさせていただきます。

Bluetooth サンプルの送り先ですが、当社日本ラボは本メールのフッタにございます望月宛にお送りください。

また、その際には添付の機材提出票をお送りください。

また RF
テストプラン作成のため、添付の [ID] にご記入の上、ご返送いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社品川テストセンター営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Misumi Sato

Sent: Friday, October 3, 2025 4:06 PM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

こちらこそ早速発送手続き着手していただきありがとうございます。

ご発送準備整いましたら、追跡番号とインボイスをご提供いただけますと幸いです。

尚、以前貴社の別部隊の WFA 認証試験をご担当させていただいた際台湾から日本への DUT 返送時に、税関から再輸入免税措置を求められた経験がございます。

その際、製品個々のシリアルナンバーが必要だったため、念のため、 DUT 本体や

Wi-Fi アンテナ等にシリアルナンバーをご設定いただくことをお勧めいたします。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 3:51 PM

To: Misumi Sato ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について佐藤様お世話になります。

アルプスアルパイン酒井です。

早速のご回答、どうもありがとうございます。

来週早々に発送手続き着手する予定です。

よろしくお願いいたします。

酒井

From: Misumi Sato

Sent: Friday, October 3, 2025 3:05 PM

To: 酒井重之 Shigeyuki Sakai ;
Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様お世話になっております。アリオンの佐藤です。

午前中の会議ではありがとうございました。

横から失礼いたします。

WFA 試験の DUT の送付先ですが、下記の表に記載させていただきましたので、ご参照お願いいたします。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

Allion Labs, Inc. CTSP Branch

No.9, Zhongxing Rd., Nantou City, Nantou County, Taiwan 540R R.O.C

Bonnie Ke( 柯宥汝 )

追跡番号、インボイスをご連絡その他、何か WFA 試験に関すること、および輸送に関するご質問等ございましたら、お気軽にお問い合わせくださいませ。

以上、よろしくお願いいたします。

アリオン株式会社東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階営業統括部プロジェクトマネジメント佐藤美純

From: Shigeyuki Sakai

Sent: Friday, October 3, 2025 2:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

PCAT のご確認ありがとうございました。

この内容を踏まえまして、弊社側でどう対応するか確認いたします。

機材の発送について、

·
下記の通り、弊社から送る際の送付先を教えていただけますでしょうか。（間違い等ありましたら修正をお願いいたします）

·
該非判定見解書等の時間かかるものは着手開始したいと思いますので、対応必要事項欄に追記していただけますでしょうか。

No

試験機材送付対応必要事項

1

BT RF/RF PHY

ALAP いわき
⇒
アリオン日本 < 送付先 1>

2

BT RF PHY オプション機能アリオン日本
⇒
アリオン台湾

DUT 該非判定書 ( アリオン様にお出しするもの )

3

BT IOPT

ALAP いわき
⇒
アリオン日本 < 送付先 2>

4

WFA

ALAP いわき
⇒
アリオン台湾 < 送付先 3>

DUT 該非判定追跡番号、インボイスをご連絡

ALAP 大連
⇒
アリオン台湾 < 送付先 4>

追跡番号、インボイスをご連絡よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, October 3, 2025 12:16 PM

To: 酒井重之 Shigeyuki Sakai ;
Toshitaka Mochizuki ;
Itsuo Sakai ;
Misumi Sato ;
Zakk Shih

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

会議資料の更新＆共有させていただき、ありがとうございます。

PCAT に関して台湾ラボが HM26 の Wi-Fi 認証試験で利用実績がございます。

ただ、御社別部隊から異なる案件への対応として、

今回 V 社様案件で使用してよいか、バージョンの指定がないか、

使用できない場合、御社からご提供いただけるか、

ご確認いただきますよう、お願いいたします。

※ HM26 の案件で使用した PCAT のバージョン： [ID]

よろしくお願いいたします。

Outlook for Android を取得差出人 : Shigeyuki Sakai

送信日時 : 金曜日 , 10 月 3, 2025 10:59:20
午前宛先 : Jun Wang ;
Toshitaka Mochizuki ; Itsuo Sakai ;
Misumi Sato ; Zakk Shih

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画について各位本日は、打合せをどうもありがとうございました。

更新した資料をお送りします。

‘QA’ シートに、★マーク付きで確認必要事項を書いております。

試験のご対応、引き続きどうぞよろしくお願いいたします。

酒井

-----Original Appointment-----

From: Jun Wang

Sent: Thursday, October 2, 2025 1:10 PM

To: Jun Wang; 酒井重之 Shigeyuki Sakai; Toshitaka Mochizuki; Itsuo Sakai

Subject: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について

When: 2025 年 10 月 3 日金曜日 9:30-10:30
(UTC+09:00) 大阪、札幌、東京

Where: Microsoft Teams 会議アルプスアルパイン酒井様こちらから設定して申し訳ございません。

明日の打ち合わせは少し早めに開始して、 09:30 からでお願いいたします。

時間帯を 09:30 ～ 10:30 に修正し、会議案内を再送いたします。

宜しくお願いいたします。

アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

弊社側関係者に確認いたしまして、下記時間帯でお願いいたします。

10/3 （金） 10:00 ～ 11:00

会議リンクは下記ご参照願います。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
489 106 497 201 8

パスコード :
sR6yD26r

開催者向け :
会議オプション

________________________________________________________________________________

_____________________________________________

From: Jun Wang

Sent: Thursday, October 2, 2025 10:06 AM

To: Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

空き時間帯の共有ありがとうございます。

本日は酒井様のお時間が概ね埋まっているようで、

弊社関係者と一旦明日で調整させていただきます。

調整つき次第ご連絡いたしますので少しお待ちください。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Thursday, October 2, 2025 8:42 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご承諾ありがとうございます。

以下に私のカレンダーを貼りました。この白い時間帯でお願いできましたら助かります。

また、時間は 30 分を見込みますが、延長用に 1 時間スロットを頂けたら助かります。

ご確認をよろしくお願いいたします。

＜１０月＞

酒井

From: Jun Wang

Sent: Thursday, October 2, 2025 7:26 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証の Pre-test の正式見積書について、

承知いたしました、ご用意いたします。

機材送付の段取りについての打ち合わせですが、

弊社側関係者に確認いたしますが、

予め酒井様のご都合をお伺いしてもよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, October 1, 2025 6:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

ご提案どうもありがとうございました。

【アルプスアルパイン様】 V 社 UXC10 の Wi-Fi 認証につきプリテストのご提案 _Update_1001.pdf の内容でお見積書をいただけますでしょうか。

あと、 BT SIG 試験と WFA 試験の DUT 機材発送段取りを考えておりますが、

機材の保管場所がいわきと中国大連に分かれている背景や、少し悩んでいる点があります。（添付ファイル）

この内容を一度打合せさせていただけませんでしょうか。

可能でしたら、打合せの候補日をいただきたいです。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, October 1, 2025 10:59 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi Pre-test の部分試験に関して、

提案資料の P5 に追加いたしました。

基本は本番試験の各対象 Program に関して、 WFA の Test Plan より一部抽出して試験を行う考えです。

ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, September 30, 2025 9:40 AM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

早速ご確認いただきありがとうございます。

部分試験のブレークダウン、

なるべく早めにご報告するように調整してまいりますので、

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Tuesday, September 30, 2025 9:11 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

内容確認しまして、とても良い内容だと考えております。

ご提案どうもありがとうございます。

試験項目ブレークダウンお待ちしております。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Tuesday, September 30, 2025 6:46 AM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

お待たせいたしました。

UXC10 の Wi-Fi 認証試験をスムーズに進めることができ、

そして目標時期までに認証取得できるように、

プレテストのご提案をいたします。※添付ご参照願います。

部分試験に関して、もう少し試験項目のブレークダウンについてラボと相談しておりまして、もう少しお待ちいただきますと幸いです。

ご検討賜りますようお願いいいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Monday, September 29, 2025 4:38 PM

To: 'Shigeyuki Sakai'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証に向けての Pre-test に関して、酒井様のご要望を基に、

ラボと提案内容について相談しております。

本日は台湾がお休みをいただいておりまして、先週末時点の概案を展開いたします。

本日の遅い時間帯になりますが、もう暫くお待ちいただきますようお願いいたします。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 29, 2025 10:34 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

Pre-test のご検討の状況はいかがでしょうか。

状況を教えていただけると助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 24, 2025 4:04 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

UXC10 の Wi-Fi 認証試験につき、 Pre-test のご相談ありがとうございます。

酒井様のお考えをラボに展開いたしまして、

Pre-test への期待や目的は理解いたしました。

いただいた資料を基に、 Pre-test 向けの Test Plan をご用意いたします。

目標として、 9/26 （金）までにお送りいたしますので、

少々お待ちいただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 24, 2025 11:39 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

打合せありがとうございました。

私が考えております Pre check の進め方のメモ書きを添付します。

なるべく無駄なく効果的に check を行っていきたいと思っています。

御社でのご経験踏まえて、、 check 実施項目のご提案等いただけますと、大変助かります。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Saturday, September 20, 2025 9:25 AM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

補足説明ありがとうございます。

Wi-Fi 認証試験はユーザー立場で、 WFA が決めた GoldenSample との接続性の確認が多く、

御社で WFA が定めた試験環境でなくても、ユーザー視点で

Wi-Fi の機能確認はできるのではと考えます。

最新の日程表から、御社で SW の確認も行っているようですが、

その状況を参考に、弊社ラボでの事前確認プランを立てようと考えますが、

いかがでしょうか。

宜しくお願いいたしますアリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 6:45 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

私の言葉の選び方が良くなかったです。

「UXC10 の SW が不安定」ではなく、「UXC10 の SW の品質レベルが不明なので不安」が正しいです。

弊社も V 社も WFA テストをする環境を保持しておらず、どの程度 WFA テストできる品質レベルなのか分かっておりません。

従いまして、 Pre Test では、 WFA テストできるレベルなのか確認したいです。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 19, 2025 5:32 PM

To: 水野淳也 Junya Mizuno

Subject: Re: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC10 の SW が不安定との事ですが、

Lab から具体的な症状を確認されております。

例、〇〇操作する時に〇〇不安定の症状がある、〇〇の際に良くリブートかかったりする、等差支えの無い程度でお願いできますと助かります。

よろしくお願い致します。

Outlook for Android を取得差出人 : Jun Wang

送信日時 : 金曜日 , 9 月 19, 2025 2:38:00
午後宛先 : Junya Mizuno

件名 : RE:
【ALAP】 [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

承知いたしました。

9/22 （月）に Lab との相談状況をご報告いたします。

具体的な提案ができるように調整してまいります。

最新日程を踏まえた進め方のすり合わせですが、

9/24 （水） 09:00 ～ 10:00、 でお願いいたします。

弊社の酒井と王君、 2 名で参加させていただきます。

よろしければこちらで Teams 会議を設定いたしますが、

御社の参加者をお伺いしてよろしいでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 19, 2025 11:01 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

もしも可能であれば、 9/22( 月 ) までにご回答もしくは状況のご連絡をいただくことは可能でしょうか？

V 社側の SW リリース遅延およびソフト品塾度が問題ではありますが、弊社から V 社に具体的なプランを早急に提示、説明していく必要がある状況です。

また、今日中に提示予定の新しい開発日程を基に、一度 [ID] と WFA の進め方のすり合わせを再度させていただくことは可能でしょうか？ ( 最大で 1 時間程度を想定しています )

来週の火曜日は御社はお休みと思いますので ( 弊社は勤務日です )、来週の月曜日もしくは水曜日の以下どれかの日程でお打ち合わせが可能かご確認をお願いしたいです。

ü
9/22( 月 ) 14:00-15:00

ü
9/24( 水 ) 9:00-10:00

ü
9/24( 水 ) 13:00-15:00

お時間に限りがあれば、 V 社の次期モデルの [ID] と WFA 認証についてもお話しさせていただければと考えております。

ご確認をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 11:20 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

相談なので、話してみないとわかりかねますので。

急ぎであれば回答希望納期をいただければそれまでに回答するように調整いたしますが、いかがでしょうか。

SW に関して情報共有させていただきありがとうございます。

今後試験において Fail が出た際のデバッグ作業も V 社自力（外部委託？）

で行う予定、承知いたしました。

他社様案件での経験ですが、ソフト完成度が低いと安定的な試験結果を得られず、

トラブルシュートも難航になったり、結果試験期間が倍半年かかった案件もございました。

ということで、弊社としても完成度の高い（量産品同等レベル）製品のご提供をお願いいたしたいです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 7:54 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

申し訳ございませんが、御社 Lab にご相談をお願いします。

御社 Lab より、いつ頃にご回答をいただける予定か、分かっておりましたら教えていただけますか？

今回の V 社からリリースされている SW は、 WFA テストに対応した素性として受け取っています。

但し、実態を聞くと、 V 社側でも WFA 認証の経験が乏しく、実際にどれだけの品質になっているか (=WFA テストできる状態か ) 分かっておりません。

V 社の SW のバグ修正等は、全て V 社で実施します。

弊社側で V 社の SW に手を加えることはありません。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Thursday, September 18, 2025 3:26 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記ご相談いただきありがとうございます。

現行 SW が不安定な状況にあること、承知いたしました。

ご要望を一度 Lab に相談いたしますので、

少々お待ちいただきますと幸いです。

参考にさせていただければと存じますが、

今回 V 社からリリースされる SW は受験用 SW でしょうか。

もしくは、 Ver0.8 （例）として御社にリリースし、その後のバグ修正、完成度アップは御社で行われる、との予定でしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, September 18, 2025 1:00 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

追加でご相談したいことがあります。

現在、 V 社より WFA 向けソフトウェアを受領したのですが、完成度に不安がある状況です。

この状態で WFA 本試験を開始し、結果として、殆ど何も試験できずに三か月を過ぎてしまうことを恐れています。

従いまして、“ WFA 本試験を開始できる状態であること”を確認する目的で、事前試験をお願いしたいと考えております。

以下の条件にて、事前試験項目のご提案とお見積りをお願いできないでしょうか？

ü
期間 : 3 日～ 5 日

ü
確認したいこと : WFA の基本となる Test Program の General 部分が Pass できること

Ø
Wi-Fi 4 11n、 Wi-Fi 5 11ac、 Wi-Fi 6 11ax の初期に実行されると想定するコマンド受付確認、接続確認、動作確認等が該当すると考えています。

確認したい内容が具体的ではなく、申し訳ございません。

お手数ですが、一度依頼をご確認いただき、不明点等ありましたらご連絡をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Wednesday, September 17, 2025 4:17 PM

To: 'Jun Wang'

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

承知しました。

その他の問題点含めて、ご確認、整理をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

上記ご理解があっています。

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

承知いたしました。確かに Bluetooth の見積依頼書でも「UXC10」とご記載されています。

再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

再提出は必要ですが、現行 CID の内容を Lab に確認してもらっておりまして、

問題点をまとめておきますので、少々お待ちください。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 3:31 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご指摘ありがとうございます。

Model Name は、製品に張り付けされているラベル等に印字されている Name と一致している必要がある、との理解で合っているでしょうか？

合っている場合、 Model Name は UXC10 になります。

同じ Model Name で電波認証等も取得しています。

この場合、再度 Model Name を変えて V 社から Submit が必要になる認識で合っているでしょうか？

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 17, 2025 12:30 PM

To: 水野淳也 Junya Mizuno

Subject: RE: 【ALAP】 [UXC]
Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社 UXC の Wi-Fi 見積依頼書の更新、ありがとうございます。

Model Name について確認させていただきます。

Submit いただいた CID （[ID]）では、 UXC
1.0、となっていますが、

見積依頼書では UXC10 とご記入されています。

正しくは UXC 1.0 でよろしいでしょうか。

※ WFA Certification System の画面よりキャプチャ宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Wednesday, September 17, 2025 10:58 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

申し訳ございません。

既にメール等でやりとりしており、ご存じの内容と思いますが、

見積書に以下未記載の箇所がありましたので追記しました。

ü
Submission Category(Flex/Quick/Derivative)

ü
CID number

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 3:08 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

見積依頼書の再送、ありがとうございます。

内容を確認させていただきます。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:58 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

本メールに添付しましたのでご確認をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 16, 2025 1:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

V 社より見直しした依頼書も入手しましたので送付させていただきます。

添付はついていないようですが、ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 16, 2025 1:11 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

CID （[ID]）を基にお見積りを進めていただき、ありがとうございます。

後追いですが、 V 社より見直しした依頼書も入手しましたので送付させていただきます。

前回、依頼書から変更が入っている Support Function 部分を黄色セルにしました。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:11 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

下記ご連絡をいただきありがとうございます。

V 社が本日改めて CID （[ID]）を Submit されたようです、

Submit された内容から、 Certified b/g が入っていなく、

Certified a/ac/N、 Certified 6 が対応されることを確認できました。

下記ご連絡いただいた内容で御見積書をご用意いたしますので、

更新でき次第の送付で構いません。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Friday, September 12, 2025 7:38 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画について王様お世話になります。

アルプスアルパイン酒井です。

申し訳ありません、今しがた、 Volvo からリストの更新に関する情報がありました。

b
と g
が少し古い規格ですので、申請を削除することを考えているそうです。

急ぎ再提出できるよう推進しますので、お見積りはもう少しお待ちいただけますでしょうか。

よろしくお願いいたします。

酒井

From:
水野淳也 Junya Mizuno

Sent: Friday, September 12, 2025 5:52 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご連絡ありがとうございます。

Test Tool につきましては、スウェーデン現地法人を介して V 社より回答を入手できました。

お見積りに影響は無いのかもしれませんが、取り急ぎ Test Tool 欄を記入したお見積書を送付させていただきます。

週明けのお見積りをお待ちしております。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 4:58 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

来週中の日程更新、お手数かけますが、よろしくお願いいたします。

見積依頼書に関して、 test tool は継続してご確認お願いいたします。

いただいた内容を基に見積書をご用意いたしますので、

週明けにお送りいたします。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 金曜日 , 9 月 12, 2025 2:15:31
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お待たせしてしまっており、申し訳ございません。

昨日、 V 社より弊社のスウェーデン現地法人を介して、 SW がリリースされてきました。

従いまして、現時点での Open 項目は以下の認識です。

1.
V 社 SW の動作チェック

2.
V 社操作マニュアルの内容チェック

3.
V 社からの Test tool の回答入手および見積書の再送

3 については、 V 社に PUSH しつつ、残りの Open 項目については確認を進めます。

来週中に現在の状況を基に、新たに認証計画を更新し、ご提出させていただきます。

何がご不明点、お気づきの点等ありましたらご連絡をお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 12, 2025 10:45 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Ｖ社 [ID] の Wi-Fi 認証について、

8/21 に V 社から SW のリリースが遅れるとご連絡をいただきましたが、

現時点の状況はいかがでしょうか。

ザックリで構いませんので、共有させていただきますと幸いです。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Monday, September 8, 2025 9:32 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

失礼しました。

Test Tool は V 社で記入した Support
Function によって決まる認識の為、

V 社にどの Test Tool を使うのか確認を依頼しております。

少々お待ち下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, September 5, 2025 11:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Wi-Fi 認証御見積依頼書のご記入、ありがとうございます。

Test Tool に関して記入されていないようですが、ご確認いただいてよろしいでしょうか。

Row#67 ～ 72

For testing

WTS(Wi-Fi Test Suite)

Quick Track Tool

Manual

For throuput

WTS(Wi-Fi Test Suite)

IxChariot

iPerf

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, September 5, 2025 9:10 AM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の [Support Function Information] 欄に対して、 V 社から回答を入手しました。

お手数ですが、一度ご確認いただき、何か気になる点等ありましたらご指摘をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:24 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご理解いただきありがとうございます。

お手数かけますが、よろしくお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, September 2, 2025 1:18 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

ご指摘の点は仰る通りと思います。

改めて、認証する試験は何か、仕様するテストツールは何か、それらをどのように接続し、動作させるのか、を段階的に整理するように依頼します。

その上で不明点がある場合には質問を明確にするように依頼します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, September 2, 2025 9:09 AM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記打ち合わせのご要望ですが、弊社が認証ラボとして、

UXC の設計開発に携わったことがなく、マニュアル作成の支援や相談はご対応できかねますので、打ち合わせに参加してもあまり意味が無いと存じますが、いかが思いますでしょうか。

WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます。

弊社からも同じ説明になりますが、それでも分からない、と言われると困りますね。

実際車のユーザーマニュアルなどの作成経験があるのではと思いますが…

Wi-Fi だけでなく、 Bluetooth、 USB、 Carplay や AndroidAuto の認証につき、

内容やレベルは違いはあれども、「マニュアル」作成もあるでしょう。

どうしてもマニュアルの作成が困難な場合、 1 つご提案ですが、

接続過程をビデオ撮影してご提供いただくことでいかがでしょうか。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 月曜日 , 9 月 1, 2025 10:09:16
午後宛先 : Jun Wang

件名 : RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

WFA 試験を受けるために、 V 社にソフトウェアの操作マニュアルの作成を依頼しております。

ALAP からは以下のような目次を目安に作成依頼をしておりますが、 V 社側でマニュアル作成経験が無く難航しているそうです。

(WTS や QuickTrack をセットアップし、幾つかコマンドを実際に実行してみて、そこに至る過程を Step
by Step で記述すれば OK、とは伝えてはいます )

- Connection diagram

- How to bring up DUT and Android

- Wi-Fi Test Suite

Configuration

AP test procedure

STA test procedure

- QuickTrack

Configuration

AP test procedure

STA test procedure

- Also, some shell scripts or supplemental information so that test operator doesn ’ t
have any confusion about set up.

※ WTS や QuickTrack のどれを使うのかは並行して Volvo へ確認中ですそのような状況の中、 V 社からマニュアルの内容についてアリオン様とも打合せをさせて教えてほしい、とリクエストを受けました。

打合せは、何を書けばよいか？の QA になると予想します。

お手数ですが打合せのご対応は可能でしょうか？

可能な場合、 9/4( 木 ) もしくは 9/8( 月 ) の 16:00 以降でご都合が良い時間を教えていただけないでしょうか？

※両日共にご都合が悪い場合には、ご都合が良い日時を教えていただけますと幸いです。

弊社も HM26 のモデル等で経験はあるものの、 UXC 担当の私などは実経験がある訳では無い為、

御社から未経験の V 社を適切にガイドしていただけると助かります。

ご検討をお願い致します。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 29, 2025 1:59 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご確認ありがとうございます。

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

はい、 Power とは送信パワーのことです。

V 社ソフトで試験するにあたり、送信パワーを確認する場合には、何を基準に確認をされるのか把握し、

事前に V 社に基準を満たすことを確認する必要があると考えて、質問をさせていただきました。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

はい、 6GHz は未対応になる為、 Return で問題ないと考えています。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 29, 2025 1:22 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

「Wi-Fi 認証見積依頼確認書」のご返送はもう少し時間かかる状況、

承知いたしました。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

「Power」とは送信パワーのことなのか、もう少し具体的にご説明をお願いしてよろしいでしょうか。

もしくはご確認されている背景、何か懸念や気になる点、があれば、

共有させていただきますと幸いです。

また、 Volvo 様より CID （[ID]）を既にご提出されていますが、

6GHz 対応となっているため、修正が必要かと思いますので、

一旦弊社より Return してよろしいでしょうか。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, August 29, 2025 1:07 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

V 社に [Support Function Information] 欄の記入を依頼し、受け取りましたが複数確認事項があり、時間を要しています。

申し訳ございませんがもう少々お待ち下さい。

また、 Wi-Fi Alliance 認証の試験項目に関して、ご確認したいことがあります。

試験項目の中で、 Power の強さを確認する試験項目はあるでしょうか？

試験準備の際に考慮する必要があるか把握する為、ご確認させて下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From:
水野淳也 Junya Mizuno

Sent: Friday, August 22, 2025 1:55 PM

To: Jun Wang

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございます。

「Wi-Fi 認証見積依頼確認書」の提出が遅れており、申し訳ございません。

弊社スウェーデン現法を介して V 社に [Support Function Information] 欄の記入を依頼しております。

記入が完了できましたら直ぐにご送付させていただきます。

また Pre-test のアドバイスについても承知しました。

V 社の SW リリース状況を確認する中で、 Critical な部分および Pre-test 要否についても V 社含めて確認していくようにします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 22, 2025 10:31 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] Wi-Fi Alliance 認証計画についてアルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

UXC の Wi-Fi 認証試験用 SW のリリースが遅れている状況、承知いたしました。

リリース予定について引き続き更新の方よろしくお願いいたします。

先日のメールでお願いいたしました弊社フォームの「Wi-Fi 認証見積依頼確認書」へのご記入ですが、

いつ頃ご送付いただけますでしょうか。

御社フォームの WorkSheet をいただいておりますが、 VCC Comment、 QC Comment も併記されている中、

最終仕様（認証取得のターゲット仕様）が不明確となっているため、

仕様情報の整理としても、見積依頼書へのご記入をお願いいたします。

Per-test に関して、 SW リリース時期が不明となっている中、予定が立てられない状況をよく理解いたしました。

3 ヵ月プランの中で試験、問題解析 / 原因究明、デバッグ、再試験、をやり切るのかなりの負荷となります。

打合せでご説明いたしましたように Pre-test は部分試験の実施も対応可能なので、

Critical な項目のみの事前試験があればフロントローディングができ、本番試験が効率アップし、

L/O 日程の確保に繋がりますので、時間的に全く無理でない限り事前試験をお勧めいたします。

また SW のリリース状況を踏まえてご相談いただければと存じますので、

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 11:07 PM

To: Jun Wang

Subject: [UXC] Wi-Fi Alliance 認証計画についてアリオン王様いつもお世話になっております。アルプスアルパインの水野です。

Wi-Fi Alliance 向け Software に関して、 V 社より最新情報が入りました。

残念なことに、 Android V 適用に向けた対応が難航しており、弊社へのリリース遅延が発生し、現時点ではいつリリースできるか不明との情報を受けております。

弊社としては、遅くても 9 月中に V 社から Software を受け取れるように PUSH している状況です。

上記の状況を踏まえまして、 Pre-test を実施する時間が確保できない為、

Pre-test は無しで、三か月パックの中で最初の 1.5 カ月は試験 1 回目、後半の 1.5 カ月で NG 修正と試験 2 回目 (NG+ 関連する試験項目 )、といった形で進めたいと考えております。

取り急ぎ、現状と弊社の考えをご連絡させていただきました。

また、 Wi-Fi Alliance 向け Software リリース日程に関し、進展がありましたら直ぐにご連絡させていただきます。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :
