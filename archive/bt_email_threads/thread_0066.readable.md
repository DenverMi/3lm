# thread_0066: Re: 【内部連絡】FW: 【ALAP】Q社テストツールインストールの件

- Message count: 6
- Source JSON: `thread_0066.json`

---

## 1. 2025-02-04 06:57

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu , "Toshitaka Mochizuki"

後夷さんお疲れさまです。

客先の「DUT(実機)はどのCOM Portに接続されているのでしょうか。」に対しては「COM3」だけでよろしいと思います。

以下私からの質問ですが、テスター接続仮想COMポートのUSB-Serialケーブル(RS232C側開放状態)は外部PCに接続しましか？このケーブル接続がないと外部PCは当該(仮想)COMポートを認識しません。

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年2月4日 15:02

宛先: Toshitaka Mochizuki ; Itsuo Sakai

件名: RE: 【内部連絡】FW: 【ALAP】Q社テストツールインストールの件望月さん、

お疲れ様です。

現状では、 COM3 が DUT に接続されています。

Tester と接続するための [ID] ( クロス )
メス / メス - ケーブルがないため手配しています。

届き次第、 Tester と DUT に接続して確認します。

酒井さん、

DTM モードについて、私はまだ理解が足りていないかもしれないと思いますので、お客様へ上記の回答でよいか、ご確認いただけますでしょうか。

よろしくお願いいたします。

後夷

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 2:39 PM

To: Kenichi Ushiroebisu

Subject: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さん望月です以下回答が参りましたのでご確認ください。

どうぞよろしくお願いいたします。

From: Yuya Kitayama

Sent: Tuesday, February 4, 2025 2:33 PM

To: Toshitaka Mochizuki ; Hitomi Ohira ; Makoto Chida ;
Jun Wang ; Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

PC と機材の接続状況がつかめず ( また、こちらで Tester を持ち合わせていない為 )

詳細な原因がつかめませんが、文面から Tester は COM3 に接続されていると読み取りました。

その場合、 DUT( 実機 ) はどの COM Port に接続されているのでしょうか。

DUT( 実機 ) と Tester の COM Port を同じ番号に指定し

Enable を押下すると同じエラーが表示されました。

DUT( 実機 ) と Tester の COM Port は別の番号になっておりますでしょうか。

QUTS Status App の画面キャプチャでもよいので展開いただけると何かわかるかもしれませんのでご教示ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 12:25 PM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ; Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在 QC.BluetoothLE_DirectMode.exe 起動の最終段階で ERROR が発生して DTM モードに投入できない状態となってしまいました。

解決策を何かご教示いただけますでしょうか。

“ QC.BluetoothLE_DirectMode.exe ”の起動ですが、 dll ファイルを” C:\[ID]\WCN\ProdTests\BIN ”から、” C:\Program
Files (x86)\[ID]\QDART\BIN ”にコピーしたところ、下記の設定画面が開きました。

なお、「[ID]19_REV_A_Bluetooth_Low_Energy_Direct_Test_Mode」の 14 ページの図とは少し違い、真ん中より少し上に” COM Port
‘ AUTO ’”と表示されています。

同文書の 14 ページの手順 2. の Step A. と Step B. は以下のようになっていますが、そのように設定はできないので、 QRCT での設定に合わせて A. の Target
Type は” APQ ”、 B. の ConnectionMode (QRCT では、 Library Mode) は” QUTS ”としました。

Step C. の Tester Port Settings で COM Port に、実際に接続されている” COM3 ”を選択すると、真ん中の少し上の” COM
Port ”に” Qualcomm ～”と表示されるので、それを選択しました。

Step D. で Enable をクリックしたところ、下記のようなエラーが表示されました。

Baurate が初期値で [ID] となっており、デバイスマネージャーで COM3 のプロパティで表示される 9600 にも設定してみましたが、同じエラーが表示されました。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 10:43 AM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

ご返信頂きありがとうございます。

RF 試験においては開始頂けているとのこと承知致しました。

また DTM モード遷移についても確認頂いている最中とのこと併せて承知致しました。

ご対応頂きありがとうございます。

上記確認結果次第になるかとは思いますが、試験日程につきまして目処が立っておりましたらご連絡お願いしたく、

お手数おかけし申し訳ありませんが、よろしくお願い致します。

/eom

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 10:22 AM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

試験の方お待たせしております。

現在 RF 試験については、 QRCT ソフトウェアで DUT モードに設定できるようになりましたので、測定を開始しています。こちらは結果出次第お知らせできると存じます。

RF PHY 試験については、 DTM モードへの遷移について確認中で、 DTM モードに遷移できるようになりましたら、測定が可能になります。

RF 試験後対応予定です。

なお、 RF PHY 試験につきましては台湾でも実施予定ですのでこの後発送書類の再確認いたします。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 9:18 AM

To: Yuya Kitayama ;
Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

BT 試験の件、色々とご迷惑おかけしており申し訳ありません。

先週末に北山より状況確認のお願いをさせて頂いておりますが、こちら如何でしょうか？

また、別メールにてお問合せ頂いておりました「DTM モードへの遷移について」についても Qualcomm からの資料を展開させて頂いておりますが、

こちらにつきましても併せて状況ご連絡頂けますと幸いです。

お手数おかけし申し訳ありません。

ご確認の程よろしくお願い致します。

/eom

From:
北山優哉 Yuya Kitayama

Sent: Friday, January 31, 2025 9:41 AM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

状況をお伺いしたく存じます。

下記でご連絡いただいておりましたが測定は開始出来ておりますでしょうか。

最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。
なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 5:25 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご対応、ご連絡ありがとうございました。

アップデートいただいたツールのバージョンに関して BT 試験に関係ありそうな箇所は、

想定通りでしたので問題ありません。

QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。

確認しました。無事動作したとのことで安心しました。

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

承知しました。引き続きご対応よろしくお願いいたします。

上記よりサンプルの回収は一旦なしにいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 5:15 PM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

Qualcomm Package Manager で、” Updates available ”にあったツールをすべてアップデートしました。

現在、こちらの PC にインストールされているツールバージョンのスクリーンショットを添付します。

(QPM_Installed_1.jpg, QPM_Installed_2.jpg)

なお、インストールされているツールが、御社から送られてきたスクリーンショットよりも多いですが、

これは昨年、こちらからも Qualcomm に直接問い合わせをして、インストールを指示されたためです。

( “ Qualcomm Software Center ”も Qualcomm の指示で入れたもので、これも今回アップデートしようとしたのですが、

全然進まなかったので、これだけアップデートできていません。 )

QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。 (QRCT_HCI_DUT_Mode.jpg)

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

HCI DUT Mode が成功した各ツールバージョンのスクリーンショットを添付しますので、

参考になさってください。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:04 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ログの取得、動作確認ありがとうございます。

ftmdaemon -ndd → QRCT にて HCI
Reset、 HCI DUT Mode クリック時のログが明らかに差異があるため、ツールの動作もしくは実機の反応に違いがあると考えます。

HCI DUT Mode クリック時のログが数回出ていましたので、

繰り返しでも接続できなかったと判断しました。

なお本日同事象を発生させることが出来ましたので、

サンプル返却までに以下の★を試していただけますでしょうか。

これで解消しない場合はサンプルの返却をお願いいたします。

・ツールの動作の原因として考えられること

→ QRCT、関連ツールのバージョンが最新ではない ( バージョン差によるツール同士の互換性含む )

添付の png を参考に QPM の「Updates Available」タブを開いていただき、

「Qualcomm USB Drivers Products」、 Qualcomm® Development Acceleration Resource Toolkit (QDART)」配下のアップデート可能なツールを最新にアップデートをお願いいたします。★

このリストに表示されるツールが最新ではないツールになります。

なお、 Qualcomm USB Drivers Products が古い状態で、 QRCT を最新にすると同事象が発生することを確認しております。

→ライセンスグループの差異

→送付いただいたキャプチャのツールのバージョンは同じですが、ライセンスグループ名には差異がありました。

もし上記で解消しない場合、同じ内容であるかは Qualcomm
しか分かりませんので問い合わせをお願いしたく存じます。

・実機の反応の違いとして考えられることハード面で差異があるかもしれませんので回収し確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 11:53 AM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

入れ違いで申し訳ございません。

先ほど確認結果をお送りいたしましたのでご確認ください。

ご確認の結果、必要でしたらサンプルをお返しいたしますのでお知らせください。

なお、大変恐縮ですが、本日体調不良のため在宅となっております。

サンプルお返しには少々お時間をいただく場合がございますのでご了承ください。

どうぞよろしくお願い致します。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 11:44 AM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

昨日の今日で申し訳ございませんが、ご連絡した方法で改善していますでしょうか。

もし改善しないようであれば、問題の切り分けを行うため、

一度実機 2 台を弊社に送り返していただくことは可能でしょうか。

送り先は以下でお願いいたします。

〒 [ID]

栃木県宇都宮市東宿郷 3-1-7

メットライフビル宇都宮ビル 8F

アルプスアルパイン ( 株 )

北山宛以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Monday, January 27, 2025 3:08 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

お忙し中ログの取得いただきありがとうございます。

取得いただいたログは確認を進めております。

ところで有識者から聞いた情報をもとに今一度、確認をお願いできないしょうか。

これで解消しない場合は実機の回収、差し替えも視野に入れております。

＝＝＝＝＝＝＝＝＝＝＝＝＝

・下記までは手順書通り

8.1.2. PC setting

4) Execute the following command to start FTM daemon.

gen4_gvm:/ #
ftmdaemon -ndd

を入力

↓

・ QRCT にて HCI Reset、 HCI DUT Mode をクリック

HCI DUT Mode で Error が出ても HCI DUT Mode を何回かクリックしてみてください。

( クリックのタイミングによって Error になることもあるようです )

その際のコマンドプロンプトのログを貼り付けて展開してください。

下記イメージでは見切れていますが HCI Reset
クリック時は Send Response = 14 が表示され、

HCI DUT Mode クリック時は Send Response = 15、 Send Response = 17 のログが表示されるはずです。

＝＝＝＝＝＝＝＝＝＝＝＝＝

Bluetooth and ANT QRCT Module をリフレッシュする。

QPM で QRCT → Bluetooth and ANT QRCT Module を検索し、

最新の v4.[ID] を Refresh インストールを実行する

＝＝＝＝＝＝＝＝＝＝＝＝＝

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, January 27, 2025 12:14 PM

To: 千田誠 Makoto Chida ;
北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン千田様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示いただきました手順を実行し、” logcat.log ”ファイルができましたので添付いたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Makoto Chida

Sent: Friday, January 24, 2025 8:15 PM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております、アルプスアルパイン千田誠です。

ご展開して頂いた“ bluetooth_bt_firmware.txt ” に出力されております、

gen4_gvm:/ # ls -l /vendor/bt_firmware/image の

BT 関連ファイル一覧について、不足ファイルなく弊社想定ファイルと一致していることを先ずはご連絡いたします。

次に本日の TeamsMTG の席でお伝えしておりました Logcat ログ取得について、以下にコマンド手順を記載します。

(Logcat ログについて、 DUT 側 Android システム上のアプリケーション / システム動作のログメッセージとなります。 )

このコマンド手順例 ) の場合、

Step6. で C:\Users\[ID]\logcat.log というファイル名が作成されおりますので、

この logcat.log ファイルを弊社にご展開の程、宜しくお願い致します。

Step1.

“ ftmdaemon -d ”を入力するコマンド・プロントとは別に新規コマンド・プロンプトを Open する

Step2.

新規コマンド・プロンプト上で以下の太字コマンド実行し、 Logcat バッファ内容を一旦クリア ( 消去 ) する。

C:\Users\[ID]> adb root

C:\Users\[ID]> adb logcat -c

Step3.

以下のコマンドを実行して Logcat 出力を” logcat.log ”というファイルに保存状態する。

C:\Users\[ID]> adb logcat > logcat.log

Step4.

“ ftmdaemon -d ”を入力するコマンド・プロントに戻り、

手順書 8.1 から QRCT 上で ” HCI DUT Mode ”で Error となる事象のところまで実行

Step5.

Step3. のコマンド・プロンプトに移り、“ Ctrl+C ”キー押下による Logcat ログ取得状態を強制終了する。

^C <- “ Ctrl+C ”キー押下

C:\Users\[ID]>

以上、お手数をおかけしますが本件不具合事象についてのログ取得ご協力の程、宜しくお願い致します。

千田誠

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 5:50 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

先ほどはお打ち合わせありがとうございました。

ご依頼の一覧をお送りいたします。

Ls コマンドの結果は一番下の方をご確認ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 11:28 AM

To: Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡有難うございます。

ご検討いただきありがとうございます。

本日私の方が午後はミーティングなどのため、

16:30 もしく 17:00 頃からの Teams ミーティングでいかがでしょうか。

当社からは、

中山：

後夷：

酒井（任意）：

王（任意）：

望月：

が参加の予定です。

御社側の参加者様をお知らせいただけましたらミーティング設定いたします。

ログにつきましては確認いたしますのでお待ちください。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Friday, January 24, 2025 11:14 AM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

BT OFF 状態でも” HCI DUT Mode ”で Error 出る旨承知しました。

一度お送りしている実機の動きを確認させていただきたいので、本日午後に WebMTG は可能でしょうか。

( カメラで状況を共有しつつできるとありがたいです )

可能であれば、ご都合の良いお時間を教えていただければと存じます。

(15:00-16:00 は外していただけると助かります )

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

ところで、下記を試していただきコマンドプロンプトに表示されるログを送付頂きたいです。

一度、 QRCT と実機を Disconnect し、実機を再起動後、手順書の 8.1 から実行し、 [ID]. で以下コマンドを実行。

[ID]. Start FTM daemon

4) Execute the following command to start FTM daemon.

gen4_gvm:/ # ftmdaemon -nd

その後、 QRCT にて HCI Reset、 HCI DUT Mode を実行した際にコマンドプロンプトに下記のようなログが表示されるはずです。

その画面キャプチャを展開いただきたく存じます。

Error が表示される時 (BT ON 時 )

問題ない時 (BT OFF 時 )

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 10:29 AM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示の件確認いたしました。

BT の設定については、今までも” OFF ”にしていたつもりでしたが、今回、改めて手順書の 8.1 から実行し、 [ID] では BT の設定の” OFF ”を確認して進めましたが、

やはり” HCI Reset ”は正常に実行できますが、” HCI DUT Mode ”では下記のエラーが表示されます。

もし、このまま解決できないようでしたら、可能でしたら来週以降でどなたか当社ご訪問いただき、実機でご確認いただくことなど調整いただくことは可能でしょうか。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, January 23, 2025 5:41 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

バージョン情報画面の取得ありがとうございました。

こちらで確認したバージョンと一致していること確認できました。

こちらで再現確認をおこなったところ BT の設定が ON の場合、

ご連絡いただいた症状になることが確認できました。

手順書 [ID]. Turn off Bluetooth を実施されていますでしょうか？

下記状態が Bluetooth OFF の状態です。

なお、手順書の 8.Bluetooth Test の操作は実機の電源を OFF/ON する度に必ず毎回実施してください。

電源 ON 時のすべての設定をを覚えているわけではない為です。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, January 23, 2025 3:45 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

ご指示いただきました画面の画像をお送りいたしますのでご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Wednesday, January 22, 2025 7:04 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

ご確認ありがとうございます。

こちらでも同じバージョンのソフトに書き換え、手順通りに動作確認を行いましたが、

“ HCI Reset ”も” HCI DUT Mode ”も Error なく実行できております。

現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、
DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。
( この表示は数秒で消えます。 )

“ USB Debugging connected ”
Tag to turn off USB debugging

こちらは DUT 側が接続先の PC を認識しているということになります。

この状態にならなければ、 [ID] ～ [ID] の設定はできないはずです。

また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

” HCI DUT Mode ”のみが Error になるということですよね。

こちらでは同様の事象が発生しておらず、手順書通りに実施していただいているのであれば、対処方法が見つかりません。

Qualcomm に念のため、下記方法でバージョン情報の画面キャプチャをいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, January 22, 2025 1:38 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、

DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。

( この表示は数秒で消えます。 )

“ USB Debugging connected ”

Tag to turn off USB debugging

また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

他に何か確認するべきところや方法はございますでしょうか。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Monday, January 20, 2025 7:12 PM

To: Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡、ご確認ありがとうございます。

手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

ありがとうございます。承知しました。

8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

8.1. Initial Setting

5)Execute the following command to start
【Normal Running】 mode.

こちらの実施結果は以下のようになっていますでしょうか？

以上、ご確認よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 6:24 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

“ HCI Reset ”は正常に実行できていますが、” HCI DUT Mode ”でエラーが発生しているようです。

（念のため、 8.1.2 から再実行してみましたが、” HCI Reset ”は正常で、” HCI DUT Mode ”でエラーが発生しました。 )

8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 20 日
17:52

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

早速のご確認ありがとうございます。

ラボにお伝えいたします。

取り急ぎお礼まで。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Yuya
Kitayama

送信日時 : 2025 年 1 月 20 日
17:42

宛先 : Jun
Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

手順書の 8.1.2. PC setting ( 下記 ) は実行されていますでしょうか？

こちらを実行しないと HCI Reset や HCI DUT Mode 押下時にエラーが出る症状がこちらでも確認出来ております。

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 5:26 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

標記テストツールの件先週末の続きですが、

現在ラボでは手順書に従って 21 ページの” 2) ”までは手順書通りに進められました。

21 ページの” 3) ”で、” HCI DUT Mode ”をクリックしたとき、下の図のようになるはずなのですが、

その下に記載した error が表示されています。

考えられる原因や対応策等ご教示いただけますと幸いです。

Error SEND: QLIB_FTM_BT_Enable_Bluetooth()

Error Failed: QLIB_FTM_BT_Enable_Bluetooth

お手数かけますが、何卒よろしくお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 17:40

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオン王君です。

標記の件早速ご確認いただきありがとうございます。

ソフトウェアは最新版の使用で問題がないこと承知いたしました。

では QPST を QUTS に読みかえてこのまま進めさせていただきます。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Yuya Kitayama

送信日時 : 金曜日 , 1 月 17, 2025 5:32:45
午後宛先 : Jun Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

お問い合わせいただいている件ですが、

動作手順書のツールのバージョンが少し古かったようで、

こちらでも最新版をインストールしたところ Library Mode は“ QUTS ”だけしか表示されませんでした。

その為、 QPST
を QUTS と読み替えて使用してください。

基本的には最新バージョンを使用していただいて問題ありません。

( 大幅な UI の変更はないと考えますが、こればかりは Qualcomm 社次第となりますので、

手順書と乖離する場合があることは許容いただけますと幸いです。 )

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Friday, January 17, 2025 5:22 PM

To: 金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様アリオンの王君です。五月雨式となり失礼いたしました。

下記確認させていただいております Library Mode の変更に関して、

ソフトウェアバージョンとは関係ありますでしょうか。

弊社ラボでは Qualcomm のソフトウェアは最新版をインストールしています。

手順書では、インストールの画面でソフトウェアのバージョンが見えていまして、

どうも古いバージョンのようです。

弊社でのインストールでは特定バージョンでのダウンロードが必要な場合、

ご連絡いただけますと幸いです。

ご確認いただきますようお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 16:50

宛先 : Masafumi
Kaneko

件名 : 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様大平様いつもお世話になります、アリオンの王君です。

標記の件、いただきました動作手順書に従ってテストツールのインストールして、

進めている中、問題が発生しており、ご確認をお願いしてもよろしいでしょうか。

インストール手順：

Sub Contractor として Accept する。

Package Manager 3 を起動し、 1. で登録したメールアドレスでログインする。

試験の手順書 (Radio Law Test / BluetoothSIG Qualification Test Operation Manual (Android14))

の 11 ページに記載されている手順でインストールする。

その後、手順書を続けて実行してみたところ、 17 ページの 2) のところで ( 下記参照 )、 Target に” APQ ”に変更できましたが、

Library Mode は“ QUTS ”だけしか表示されず、” QPST ”への変更はできませんでした。

お忙しいところ恐縮ですが、ご確認いただけますと幸いです。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

---

## 2. 2025-02-04 07:16

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu

後夷さんお疲れさまです。

クロスケーブルがないのでその先を繋げないのは理解しています。外部PCのUSBポートにUSB-Serial

変換ケーブルを繋いでいるかという質問です。

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年2月4日 16:12

宛先: Itsuo Sakai

件名: RE: 【内部連絡】FW: 【ALAP】Q社テストツールインストールの件酒井さん、

お疲れ様です。

お客様への回答についてご確認いただき、ありがとうございます。

後半のご質問についてですが、ケーブルが手配中でまだ届いておりませんので、テスターは制御用 PC に接続していません。

ケーブルは明日届く予定ですが、私が休みの日ですので、明後日、接続して確認いたします。

よろしくお願いいたします。

後夷

From: Itsuo Sakai

Sent: Tuesday, February 4, 2025 3:58 PM

To: Kenichi Ushiroebisu ; Toshitaka Mochizuki

Subject: Re: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さんお疲れさまです。

客先の「DUT( 実機 ) はどの COM
Port に接続されているのでしょうか。」に対しては「COM3」だけでよろしいと思います。

以下私からの質問ですが、テスター接続仮想 COM ポートの USB-Serial ケーブル ([ID] 側開放状態 ) は外部 PC に接続しましか？このケーブル接続がないと外部 PC は当該 ( 仮想 )COM ポートを認識しません。

酒井差出人 :
Kenichi Ushiroebisu

送信日時 :
2025 年 2 月 4 日
15:02

宛先 :
Toshitaka Mochizuki ; Itsuo Sakai

件名 :
RE: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件望月さん、

お疲れ様です。

現状では、 COM3 が DUT に接続されています。

Tester と接続するための [ID] ( クロス )
メス / メス - ケーブルがないため手配しています。

届き次第、 Tester と DUT に接続して確認します。

酒井さん、

DTM モードについて、私はまだ理解が足りていないかもしれないと思いますので、お客様へ上記の回答でよいか、ご確認いただけますでしょうか。

よろしくお願いいたします。

後夷

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 2:39 PM

To: Kenichi Ushiroebisu

Subject: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さん望月です以下回答が参りましたのでご確認ください。

どうぞよろしくお願いいたします。

From: Yuya Kitayama

Sent: Tuesday, February 4, 2025 2:33 PM

To: Toshitaka Mochizuki ; Hitomi Ohira ; Makoto Chida ;
Jun Wang ; Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

PC と機材の接続状況がつかめず ( また、こちらで Tester を持ち合わせていない為 )

詳細な原因がつかめませんが、文面から Tester は COM3 に接続されていると読み取りました。

その場合、 DUT( 実機 ) はどの COM Port に接続されているのでしょうか。

DUT( 実機 ) と Tester の COM Port を同じ番号に指定し

Enable を押下すると同じエラーが表示されました。

DUT( 実機 ) と Tester の COM Port は別の番号になっておりますでしょうか。

QUTS Status App の画面キャプチャでもよいので展開いただけると何かわかるかもしれませんのでご教示ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 12:25 PM

To: 大平ひとみ Hitomi Ohira ;
北山優哉
Yuya Kitayama ;
千田誠 Makoto Chida ; Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在 QC.BluetoothLE_DirectMode.exe 起動の最終段階で ERROR が発生して DTM モードに投入できない状態となってしまいました。

解決策を何かご教示いただけますでしょうか。

“ QC.BluetoothLE_DirectMode.exe ”の起動ですが、 dll ファイルを” C:\[ID]\WCN\ProdTests\BIN ”から、” C:\Program
Files (x86)\[ID]\QDART\BIN ”にコピーしたところ、下記の設定画面が開きました。

なお、「[ID]19_REV_A_Bluetooth_Low_Energy_Direct_Test_Mode」の 14 ページの図とは少し違い、真ん中より少し上に” COM Port
‘ AUTO ’”と表示されています。

同文書の 14 ページの手順 2. の Step A. と Step B. は以下のようになっていますが、そのように設定はできないので、 QRCT での設定に合わせて A. の Target
Type は” APQ ”、 B. の ConnectionMode (QRCT では、 Library Mode) は” QUTS ”としました。

Step C. の Tester Port Settings で COM Port に、実際に接続されている” COM3 ”を選択すると、真ん中の少し上の” COM
Port ”に” Qualcomm ～”と表示されるので、それを選択しました。

Step D. で Enable をクリックしたところ、下記のようなエラーが表示されました。

Baurate が初期値で [ID] となっており、デバイスマネージャーで COM3 のプロパティで表示される 9600 にも設定してみましたが、同じエラーが表示されました。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 10:43 AM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

ご返信頂きありがとうございます。

RF 試験においては開始頂けているとのこと承知致しました。

また DTM モード遷移についても確認頂いている最中とのこと併せて承知致しました。

ご対応頂きありがとうございます。

上記確認結果次第になるかとは思いますが、試験日程につきまして目処が立っておりましたらご連絡お願いしたく、

お手数おかけし申し訳ありませんが、よろしくお願い致します。

/eom

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 10:22 AM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

試験の方お待たせしております。

現在 RF 試験については、 QRCT ソフトウェアで DUT モードに設定できるようになりましたので、測定を開始しています。こちらは結果出次第お知らせできると存じます。

RF PHY 試験については、 DTM モードへの遷移について確認中で、 DTM モードに遷移できるようになりましたら、測定が可能になります。

RF 試験後対応予定です。

なお、 RF PHY 試験につきましては台湾でも実施予定ですのでこの後発送書類の再確認いたします。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 9:18 AM

To: Yuya Kitayama ;
Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

BT 試験の件、色々とご迷惑おかけしており申し訳ありません。

先週末に北山より状況確認のお願いをさせて頂いておりますが、こちら如何でしょうか？

また、別メールにてお問合せ頂いておりました「DTM モードへの遷移について」についても Qualcomm からの資料を展開させて頂いておりますが、

こちらにつきましても併せて状況ご連絡頂けますと幸いです。

お手数おかけし申し訳ありません。

ご確認の程よろしくお願い致します。

/eom

From:
北山優哉 Yuya Kitayama

Sent: Friday, January 31, 2025 9:41 AM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

状況をお伺いしたく存じます。

下記でご連絡いただいておりましたが測定は開始出来ておりますでしょうか。

·
最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

·
なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に

·
実施いたします。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 5:25 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご対応、ご連絡ありがとうございました。

アップデートいただいたツールのバージョンに関して BT 試験に関係ありそうな箇所は、

想定通りでしたので問題ありません。

·
QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。

確認しました。無事動作したとのことで安心しました。

·
今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御が

·
できるということになりますので、それから測定が可能になると思います。

承知しました。引き続きご対応よろしくお願いいたします。

上記よりサンプルの回収は一旦なしにいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 5:15 PM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

Qualcomm Package Manager で、” Updates available ”にあったツールをすべてアップデートしました。

現在、こちらの PC にインストールされているツールバージョンのスクリーンショットを添付します。

(QPM_Installed_1.jpg, QPM_Installed_2.jpg)

なお、インストールされているツールが、御社から送られてきたスクリーンショットよりも多いですが、

これは昨年、こちらからも Qualcomm に直接問い合わせをして、インストールを指示されたためです。

( “ Qualcomm Software Center ”も Qualcomm の指示で入れたもので、これも今回アップデートしようとしたのですが、

全然進まなかったので、これだけアップデートできていません。 )

QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。 (QRCT_HCI_DUT_Mode.jpg)

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

HCI DUT Mode が成功した各ツールバージョンのスクリーンショットを添付しますので、

参考になさってください。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:04 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ログの取得、動作確認ありがとうございます。

ftmdaemon -ndd → QRCT にて HCI
Reset、 HCI DUT Mode クリック時のログが明らかに差異があるため、ツールの動作もしくは実機の反応に違いがあると考えます。

HCI DUT Mode クリック時のログが数回出ていましたので、

繰り返しでも接続できなかったと判断しました。

なお本日同事象を発生させることが出来ましたので、

サンプル返却までに以下の★を試していただけますでしょうか。

これで解消しない場合はサンプルの返却をお願いいたします。

・ツールの動作の原因として考えられること

→ QRCT、関連ツールのバージョンが最新ではない ( バージョン差によるツール同士の互換性含む )

添付の png を参考に QPM の「Updates Available」タブを開いていただき、

「Qualcomm USB Drivers Products」、 Qualcomm® Development Acceleration Resource Toolkit (QDART)」配下のアップデート可能なツールを最新にアップデートをお願いいたします。★

このリストに表示されるツールが最新ではないツールになります。

なお、 Qualcomm USB Drivers Products が古い状態で、 QRCT を最新にすると同事象が発生することを確認しております。

→ライセンスグループの差異

→送付いただいたキャプチャのツールのバージョンは同じですが、ライセンスグループ名には差異がありました。

もし上記で解消しない場合、同じ内容であるかは Qualcomm
しか分かりませんので問い合わせをお願いしたく存じます。

・実機の反応の違いとして考えられることハード面で差異があるかもしれませんので回収し確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 11:53 AM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

入れ違いで申し訳ございません。

先ほど確認結果をお送りいたしましたのでご確認ください。

ご確認の結果、必要でしたらサンプルをお返しいたしますのでお知らせください。

なお、大変恐縮ですが、本日体調不良のため在宅となっております。

サンプルお返しには少々お時間をいただく場合がございますのでご了承ください。

どうぞよろしくお願い致します。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 11:44 AM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

昨日の今日で申し訳ございませんが、ご連絡した方法で改善していますでしょうか。

もし改善しないようであれば、問題の切り分けを行うため、

一度実機 2 台を弊社に送り返していただくことは可能でしょうか。

送り先は以下でお願いいたします。

〒 [ID]

栃木県宇都宮市東宿郷 3-1-7

メットライフビル宇都宮ビル 8F

アルプスアルパイン ( 株 )

北山宛以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Monday, January 27, 2025 3:08 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

お忙し中ログの取得いただきありがとうございます。

取得いただいたログは確認を進めております。

ところで有識者から聞いた情報をもとに今一度、確認をお願いできないしょうか。

これで解消しない場合は実機の回収、差し替えも視野に入れております。

＝＝＝＝＝＝＝＝＝＝＝＝＝

・下記までは手順書通り

8.1.2. PC setting

4) Execute the following command to start FTM daemon.

gen4_gvm:/ #
ftmdaemon -ndd

を入力

↓

・ QRCT にて HCI Reset、 HCI DUT Mode をクリック

HCI DUT Mode で Error が出ても HCI DUT Mode を何回かクリックしてみてください。

( クリックのタイミングによって Error になることもあるようです )

その際のコマンドプロンプトのログを貼り付けて展開してください。

下記イメージでは見切れていますが HCI Reset
クリック時は Send Response = 14 が表示され、

HCI DUT Mode クリック時は Send Response = 15、 Send Response = 17 のログが表示されるはずです。

＝＝＝＝＝＝＝＝＝＝＝＝＝

Bluetooth and ANT QRCT Module をリフレッシュする。

QPM で QRCT → Bluetooth and ANT QRCT Module を検索し、

最新の v4.[ID] を Refresh インストールを実行する

＝＝＝＝＝＝＝＝＝＝＝＝＝

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, January 27, 2025 12:14 PM

To: 千田誠 Makoto Chida ;
北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン千田様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示いただきました手順を実行し、” logcat.log ”ファイルができましたので添付いたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Makoto Chida

Sent: Friday, January 24, 2025 8:15 PM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております、アルプスアルパイン千田誠です。

ご展開して頂いた“ bluetooth_bt_firmware.txt ” に出力されております、

gen4_gvm:/ # ls -l /vendor/bt_firmware/image の

BT 関連ファイル一覧について、不足ファイルなく弊社想定ファイルと一致していることを先ずはご連絡いたします。

次に本日の TeamsMTG の席でお伝えしておりました Logcat ログ取得について、以下にコマンド手順を記載します。

(Logcat ログについて、 DUT 側 Android システム上のアプリケーション / システム動作のログメッセージとなります。 )

このコマンド手順例 ) の場合、

Step6. で C:\Users\[ID]\logcat.log というファイル名が作成されおりますので、

この logcat.log ファイルを弊社にご展開の程、宜しくお願い致します。

Step1.

“ ftmdaemon -d ”を入力するコマンド・プロントとは別に新規コマンド・プロンプトを Open する

Step2.

新規コマンド・プロンプト上で以下の太字コマンド実行し、 Logcat バッファ内容を一旦クリア ( 消去 ) する。

C:\Users\[ID]> adb root

C:\Users\[ID]> adb logcat -c

Step3.

以下のコマンドを実行して Logcat 出力を” logcat.log ”というファイルに保存状態する。

C:\Users\[ID]> adb logcat > logcat.log

Step4.

“ ftmdaemon -d ”を入力するコマンド・プロントに戻り、

手順書 8.1 から QRCT 上で ” HCI DUT Mode ”で Error となる事象のところまで実行

Step5.

Step3. のコマンド・プロンプトに移り、“ Ctrl+C ”キー押下による Logcat ログ取得状態を強制終了する。

^C <- “ Ctrl+C ”キー押下

C:\Users\[ID]>

以上、お手数をおかけしますが本件不具合事象についてのログ取得ご協力の程、宜しくお願い致します。

千田誠

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 5:50 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

先ほどはお打ち合わせありがとうございました。

ご依頼の一覧をお送りいたします。

Ls コマンドの結果は一番下の方をご確認ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 11:28 AM

To: Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡有難うございます。

ご検討いただきありがとうございます。

本日私の方が午後はミーティングなどのため、

16:30 もしく 17:00 頃からの Teams ミーティングでいかがでしょうか。

当社からは、

中山：

後夷：

酒井（任意）：

王（任意）：

望月：

が参加の予定です。

御社側の参加者様をお知らせいただけましたらミーティング設定いたします。

ログにつきましては確認いたしますのでお待ちください。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Friday, January 24, 2025 11:14 AM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

BT OFF 状態でも” HCI DUT Mode ”で Error 出る旨承知しました。

一度お送りしている実機の動きを確認させていただきたいので、本日午後に WebMTG は可能でしょうか。

( カメラで状況を共有しつつできるとありがたいです )

可能であれば、ご都合の良いお時間を教えていただければと存じます。

(15:00-16:00 は外していただけると助かります )

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

ところで、下記を試していただきコマンドプロンプトに表示されるログを送付頂きたいです。

一度、 QRCT と実機を Disconnect し、実機を再起動後、手順書の 8.1 から実行し、 [ID]. で以下コマンドを実行。

[ID]. Start FTM daemon

4) Execute the following command to start FTM daemon.

gen4_gvm:/ # ftmdaemon -nd

その後、 QRCT にて HCI Reset、 HCI DUT Mode を実行した際にコマンドプロンプトに下記のようなログが表示されるはずです。

その画面キャプチャを展開いただきたく存じます。

Error が表示される時 (BT ON 時 )

問題ない時 (BT OFF 時 )

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 10:29 AM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示の件確認いたしました。

BT の設定については、今までも” OFF ”にしていたつもりでしたが、今回、改めて手順書の 8.1 から実行し、 [ID] では BT の設定の” OFF ”を確認して進めましたが、

やはり” HCI Reset ”は正常に実行できますが、” HCI DUT Mode ”では下記のエラーが表示されます。

もし、このまま解決できないようでしたら、可能でしたら来週以降でどなたか当社ご訪問いただき、実機でご確認いただくことなど調整いただくことは可能でしょうか。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, January 23, 2025 5:41 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

バージョン情報画面の取得ありがとうございました。

こちらで確認したバージョンと一致していること確認できました。

こちらで再現確認をおこなったところ BT の設定が ON の場合、

ご連絡いただいた症状になることが確認できました。

手順書 [ID]. Turn off Bluetooth を実施されていますでしょうか？

下記状態が Bluetooth OFF の状態です。

なお、手順書の 8.Bluetooth Test の操作は実機の電源を OFF/ON する度に必ず毎回実施してください。

電源 ON 時のすべての設定をを覚えているわけではない為です。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, January 23, 2025 3:45 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

ご指示いただきました画面の画像をお送りいたしますのでご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Wednesday, January 22, 2025 7:04 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

ご確認ありがとうございます。

こちらでも同じバージョンのソフトに書き換え、手順通りに動作確認を行いましたが、

“ HCI Reset ”も” HCI DUT Mode ”も Error なく実行できております。

·
現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、

·
DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。

·
( この表示は数秒で消えます。 )

·

“ USB Debugging connected ”

·
Tag to turn off USB debugging

こちらは DUT 側が接続先の PC を認識しているということになります。

この状態にならなければ、 [ID] ～ [ID] の設定はできないはずです。

·
また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

” HCI DUT Mode ”のみが Error になるということですよね。

こちらでは同様の事象が発生しておらず、手順書通りに実施していただいているのであれば、対処方法が見つかりません。

Qualcomm に念のため、下記方法でバージョン情報の画面キャプチャをいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, January 22, 2025 1:38 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、

DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。

( この表示は数秒で消えます。 )

“ USB Debugging connected ”

Tag to turn off USB debugging

また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

他に何か確認するべきところや方法はございますでしょうか。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Monday, January 20, 2025 7:12 PM

To: Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡、ご確認ありがとうございます。

·
手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

ありがとうございます。承知しました。

·
8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

8.1. Initial Setting

5)Execute the following command to start
【Normal Running】 mode.

こちらの実施結果は以下のようになっていますでしょうか？

以上、ご確認よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 6:24 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

“ HCI Reset ”は正常に実行できていますが、” HCI DUT Mode ”でエラーが発生しているようです。

（念のため、 8.1.2 から再実行してみましたが、” HCI Reset ”は正常で、” HCI DUT Mode ”でエラーが発生しました。 )

8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 20 日
17:52

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

早速のご確認ありがとうございます。

ラボにお伝えいたします。

取り急ぎお礼まで。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Yuya
Kitayama

送信日時 : 2025 年 1 月 20 日
17:42

宛先 : Jun
Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

手順書の 8.1.2. PC setting ( 下記 ) は実行されていますでしょうか？

こちらを実行しないと HCI Reset や HCI DUT Mode 押下時にエラーが出る症状がこちらでも確認出来ております。

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 5:26 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

標記テストツールの件先週末の続きですが、

現在ラボでは手順書に従って 21 ページの” 2) ”までは手順書通りに進められました。

21 ページの” 3) ”で、” HCI DUT Mode ”をクリックしたとき、下の図のようになるはずなのですが、

その下に記載した error が表示されています。

考えられる原因や対応策等ご教示いただけますと幸いです。

Error SEND: QLIB_FTM_BT_Enable_Bluetooth()

Error Failed: QLIB_FTM_BT_Enable_Bluetooth

お手数かけますが、何卒よろしくお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 17:40

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオン王君です。

標記の件早速ご確認いただきありがとうございます。

ソフトウェアは最新版の使用で問題がないこと承知いたしました。

では QPST を QUTS に読みかえてこのまま進めさせていただきます。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Yuya Kitayama

送信日時 : 金曜日 , 1 月 17, 2025 5:32:45
午後宛先 : Jun Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

お問い合わせいただいている件ですが、

動作手順書のツールのバージョンが少し古かったようで、

こちらでも最新版をインストールしたところ Library Mode は“ QUTS ”だけしか表示されませんでした。

その為、 QPST
を QUTS と読み替えて使用してください。

基本的には最新バージョンを使用していただいて問題ありません。

( 大幅な UI の変更はないと考えますが、こればかりは Qualcomm 社次第となりますので、

手順書と乖離する場合があることは許容いただけますと幸いです。 )

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Friday, January 17, 2025 5:22 PM

To: 金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様アリオンの王君です。五月雨式となり失礼いたしました。

下記確認させていただいております Library Mode の変更に関して、

ソフトウェアバージョンとは関係ありますでしょうか。

弊社ラボでは Qualcomm のソフトウェアは最新版をインストールしています。

手順書では、インストールの画面でソフトウェアのバージョンが見えていまして、

どうも古いバージョンのようです。

弊社でのインストールでは特定バージョンでのダウンロードが必要な場合、

ご連絡いただけますと幸いです。

ご確認いただきますようお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 16:50

宛先 : Masafumi
Kaneko

件名 : 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様大平様いつもお世話になります、アリオンの王君です。

標記の件、いただきました動作手順書に従ってテストツールのインストールして、

進めている中、問題が発生しており、ご確認をお願いしてもよろしいでしょうか。

インストール手順：

Sub Contractor として Accept する。

Package Manager 3 を起動し、 1. で登録したメールアドレスでログインする。

試験の手順書 (Radio Law Test / BluetoothSIG Qualification Test Operation Manual (Android14))

の 11 ページに記載されている手順でインストールする。

その後、手順書を続けて実行してみたところ、 17 ページの 2) のところで ( 下記参照 )、 Target に” APQ ”に変更できましたが、

Library Mode は“ QUTS ”だけしか表示されず、” QPST ”への変更はできませんでした。

お忙しいところ恐縮ですが、ご確認いただけますと幸いです。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

---

## 3. 2025-02-04 07:31

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu

後夷さんお疲れさまです。

USB-Serial変換ケーブルを外部PCのUSBポートに接続していないなら下記ERROR(COM4 Open ERROR

およびCOM4アクセス拒否)は当然出ます。

クロスケーブルが入手でき,RFテストが終了したらうべて接続して再度試してください。

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年2月4日 16:21

宛先: Itsuo Sakai

件名: RE: 【内部連絡】FW: 【ALAP】Q社テストツールインストールの件酒井さん、

お疲れ様です。

外部PCには、DUTからのUSBケーブルのみ接続しており、[ID]232C変換ケーブルは接続しておりません。

現在、RF試験実施中ですので、こちらも明後日確認いたします。

よろしくお願いいたします。

後夷

From: Itsuo Sakai

Sent: Tuesday, February 4, 2025 4:17 PM

To: Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さんお疲れさまです。

クロスケーブルがないのでその先を繋げないのは理解しています。外部 PC の USB ポートに USB-Serial

変換ケーブルを繋いでいるかという質問です。

酒井差出人 : Kenichi Ushiroebisu

送信日時 : 2025 年 2 月 4 日 16:12

宛先 : Itsuo Sakai

件名 : RE:
【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件酒井さん、

お疲れ様です。

お客様への回答についてご確認いただき、ありがとうございます。

後半のご質問についてですが、ケーブルが手配中でまだ届いておりませんので、テスターは制御用PCに接続していません。

ケーブルは明日届く予定ですが、私が休みの日ですので、明後日、接続して確認いたします。

よろしくお願いいたします。

後夷

From: Itsuo Sakai

Sent: Tuesday, February 4, 2025 3:58 PM

To: Kenichi Ushiroebisu ;
Toshitaka Mochizuki

Subject: Re: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さんお疲れさまです。

客先の「DUT( 実機 ) はどの COM
Port に接続されているのでしょうか。」に対しては「COM3」だけでよろしいと思います。

以下私からの質問ですが、テスター接続仮想 COM ポートの USB-Serial ケーブル ([ID] 側開放状態 ) は外部 PC に接続しましか？このケーブル接続がないと外部 PC は当該 ( 仮想 )COM ポートを認識しません。

酒井差出人 : Kenichi Ushiroebisu

送信日時 : 2025 年 2 月 4 日 15:02

宛先 : Toshitaka Mochizuki ;
Itsuo Sakai

件名 : RE:
【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件望月さん、

お疲れ様です。

現状では、COM3がDUTに接続されています。

Testerと接続するためのRS-232C (クロス) メス/メス-ケーブルがないため手配しています。

届き次第、TesterとDUTに接続して確認します。

酒井さん、

DTMモードについて、私はまだ理解が足りていないかもしれないと思いますので、お客様へ上記の回答でよいか、ご確認いただけますでしょうか。

よろしくお願いいたします。

後夷

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 2:39 PM

To: Kenichi Ushiroebisu

Subject: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さん望月です以下回答が参りましたのでご確認ください。

どうぞよろしくお願いいたします。

From: Yuya Kitayama

Sent: Tuesday, February 4, 2025 2:33 PM

To: Toshitaka Mochizuki ;
Hitomi Ohira ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

PCと機材の接続状況がつかめず(また、こちらでTesterを持ち合わせていない為)

詳細な原因がつかめませんが、文面からTesterはCOM3に接続されていると読み取りました。

その場合、DUT(実機)はどのCOM Portに接続されているのでしょうか。

DUT(実機)とTesterのCOM Portを同じ番号に指定し

Enableを押下すると同じエラーが表示されました。

DUT(実機)とTesterのCOM Portは別の番号になっておりますでしょうか。

QUTS Status Appの画面キャプチャでもよいので展開いただけると何かわかるかもしれませんのでご教示ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 12:25 PM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在QC.BluetoothLE_DirectMode.exe起動の最終段階でERRORが発生してDTMモードに投入できない状態となってしまいました。

解決策を何かご教示いただけますでしょうか。

“QC.BluetoothLE_DirectMode.exe”の起動ですが、dllファイルを”C:\[ID]\WCN\ProdTests\BIN”から、”C:\Program Files (x86)\[ID]\QDART\BIN”にコピーしたところ、下記の設定画面が開きました。

なお、「[ID]19_REV_A_Bluetooth_Low_Energy_Direct_Test_Mode」の14ページの図とは少し違い、真ん中より少し上に”COM Port ‘AUTO’”と表示されています。

同文書の14ページの手順2.のStep A.とStep B.は以下のようになっていますが、そのように設定はできないので、QRCTでの設定に合わせてA.のTarget Typeは”APQ”、B.のConnectionMode (QRCTでは、Library Mode)は”QUTS”としました。

Step C.のTester Port SettingsでCOM Portに、実際に接続されている”COM3”を選択すると、真ん中の少し上の”COM Port”に”Qualcomm～”と表示されるので、それを選択しました。

Step D.でEnableをクリックしたところ、下記のようなエラーが表示されました。

Baurateが初期値で115200となっており、デバイスマネージャーでCOM3のプロパティで表示される9600にも設定してみましたが、同じエラーが表示されました。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 10:43 AM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To.　アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

ご返信頂きありがとうございます。

RF試験においては開始頂けているとのこと承知致しました。

またDTMモード遷移についても確認頂いている最中とのこと併せて承知致しました。

ご対応頂きありがとうございます。

上記確認結果次第になるかとは思いますが、試験日程につきまして目処が立っておりましたらご連絡お願いしたく、

お手数おかけし申し訳ありませんが、よろしくお願い致します。

/eom

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 10:22 AM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

試験の方お待たせしております。

現在RF試験については、QRCTソフトウェアでDUTモードに設定できるようになりましたので、測定を開始しています。こちらは結果出次第お知らせできると存じます。

RF PHY試験については、DTMモードへの遷移について確認中で、DTMモードに遷移できるようになりましたら、測定が可能になります。

RF試験後対応予定です。

なお、RF PHY試験につきましては台湾でも実施予定ですのでこの後発送書類の再確認いたします。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 9:18 AM

To: Yuya Kitayama ;
Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To.　アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

BT試験の件、色々とご迷惑おかけしており申し訳ありません。

先週末に北山より状況確認のお願いをさせて頂いておりますが、こちら如何でしょうか？

また、別メールにてお問合せ頂いておりました「DTMモードへの遷移について」についてもQualcommからの資料を展開させて頂いておりますが、

こちらにつきましても併せて状況ご連絡頂けますと幸いです。

お手数おかけし申し訳ありません。

ご確認の程よろしくお願い致します。

/eom

From:
北山優哉 Yuya Kitayama

Sent: Friday, January 31, 2025 9:41 AM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

状況をお伺いしたく存じます。

下記でご連絡いただいておりましたが測定は開始出来ておりますでしょうか。

·
最後まで行ければ、DUTの制御ができるということになりますので、それから測定が可能になると思います。

·
なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に

·
実施いたします。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 5:25 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご対応、ご連絡ありがとうございました。

アップデートいただいたツールのバージョンに関してBT試験に関係ありそうな箇所は、

想定通りでしたので問題ありません。

·
QRCTで”HCI DUT Mode”が正常に実行できたところのスクリーンショットも添付いたします。

確認しました。無事動作したとのことで安心しました。

·
今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、DUTの制御が

·
できるということになりますので、それから測定が可能になると思います。

承知しました。引き続きご対応よろしくお願いいたします。

上記よりサンプルの回収は一旦なしにいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 5:15 PM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

Qualcomm Package Managerで、”Updates available”にあったツールをすべてアップデートしました。

現在、こちらのPCにインストールされているツールバージョンのスクリーンショットを添付します。

(QPM_Installed_1.jpg, QPM_Installed_2.jpg)

なお、インストールされているツールが、御社から送られてきたスクリーンショットよりも多いですが、

これは昨年、こちらからもQualcommに直接問い合わせをして、インストールを指示されたためです。

(“Qualcomm Software Center”もQualcommの指示で入れたもので、これも今回アップデートしようとしたのですが、

全然進まなかったので、これだけアップデートできていません。)

QRCTで”HCI DUT Mode”が正常に実行できたところのスクリーンショットも添付いたします。(QRCT_HCI_DUT_Mode.jpg)

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、DUTの制御ができるということになりますので、それから測定が可能になると思います。

なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

HCI DUT Modeが成功した各ツールバージョンのスクリーンショットを添付しますので、

参考になさってください。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:04 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ログの取得、動作確認ありがとうございます。

ftmdaemon -ndd　→ QRCTにてHCI Reset、HCI DUT Modeクリック時のログが明らかに差異があるため、ツールの動作もしくは実機の反応に違いがあると考えます。

HCI DUT Modeクリック時のログが数回出ていましたので、

繰り返しでも接続できなかったと判断しました。

なお本日同事象を発生させることが出来ましたので、

サンプル返却までに以下の★を試していただけますでしょうか。

これで解消しない場合はサンプルの返却をお願いいたします。

・ツールの動作の原因として考えられること

→QRCT、関連ツールのバージョンが最新ではない (バージョン差によるツール同士の互換性含む)

添付のpngを参考にQPMの「Updates Available」タブを開いていただき、

「Qualcomm USB Drivers Products」、Qualcomm® Development Acceleration Resource Toolkit (QDART)」配下のアップデート可能なツールを最新にアップデートをお願いいたします。★

このリストに表示されるツールが最新ではないツールになります。

なお、Qualcomm USB Drivers Productsが古い状態で、QRCTを最新にすると同事象が発生することを確認しております。

→ライセンスグループの差異

→送付いただいたキャプチャのツールのバージョンは同じですが、ライセンスグループ名には差異がありました。

もし上記で解消しない場合、同じ内容であるかはQualcomm しか分かりませんので問い合わせをお願いしたく存じます。

・実機の反応の違いとして考えられることハード面で差異があるかもしれませんので回収し確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 11:53 AM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

入れ違いで申し訳ございません。

先ほど確認結果をお送りいたしましたのでご確認ください。

ご確認の結果、必要でしたらサンプルをお返しいたしますのでお知らせください。

なお、大変恐縮ですが、本日体調不良のため在宅となっております。

サンプルお返しには少々お時間をいただく場合がございますのでご了承ください。

どうぞよろしくお願い致します。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 11:44 AM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

昨日の今日で申し訳ございませんが、ご連絡した方法で改善していますでしょうか。

もし改善しないようであれば、問題の切り分けを行うため、

一度実機2台を弊社に送り返していただくことは可能でしょうか。

送り先は以下でお願いいたします。

〒[ID]

栃木県宇都宮市東宿郷3-1-7

メットライフビル宇都宮ビル8F

アルプスアルパイン(株)

北山宛以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Monday, January 27, 2025 3:08 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

お忙し中ログの取得いただきありがとうございます。

取得いただいたログは確認を進めております。

ところで有識者から聞いた情報をもとに今一度、確認をお願いできないしょうか。

これで解消しない場合は実機の回収、差し替えも視野に入れております。

＝＝＝＝＝＝＝＝＝＝＝＝＝

・下記までは手順書通り

8.1.2. PC setting

4) Execute the following command to start FTM daemon.

gen4_gvm:/ #
ftmdaemon -ndd

を入力

↓

・QRCTにてHCI Reset、HCI DUT Modeをクリック

HCI DUT ModeでErrorが出ても HCI DUT Modeを何回かクリックしてみてください。

(クリックのタイミングによってErrorになることもあるようです)

その際のコマンドプロンプトのログを貼り付けて展開してください。

下記イメージでは見切れていますがHCI Reset クリック時はSend Response = 14が表示され、

HCI DUT Modeクリック時はSend Response = 15、Send Response = 17　のログが表示されるはずです。

＝＝＝＝＝＝＝＝＝＝＝＝＝

Bluetooth and ANT QRCT Module　をリフレッシュする。

QPMでQRCT→Bluetooth and ANT QRCT Moduleを検索し、

最新のv4.[ID]2をRefreshインストールを実行する

＝＝＝＝＝＝＝＝＝＝＝＝＝

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, January 27, 2025 12:14 PM

To: 千田誠 Makoto Chida ;
北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン千田様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示いただきました手順を実行し、”logcat.log”ファイルができましたので添付いたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Makoto Chida

Sent: Friday, January 24, 2025 8:15 PM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To.　アリオン株式会社望月様お世話になっております、アルプスアルパイン千田誠です。

ご展開して頂いた“bluetooth_bt_firmware.txt” に出力されております、

gen4_gvm:/ # ls -l /vendor/bt_firmware/image の

BT関連ファイル一覧について、不足ファイルなく弊社想定ファイルと一致していることを先ずはご連絡いたします。

次に本日のTeamsMTGの席でお伝えしておりましたLogcatログ取得について、以下にコマンド手順を記載します。

(Logcatログについて、DUT側Androidシステム上のアプリケーション/システム動作のログメッセージとなります。)

このコマンド手順例) の場合、

Step6.でC:\Users\[ID]\logcat.log というファイル名が作成されおりますので、

このlogcat.logファイルを弊社にご展開の程、宜しくお願い致します。

Step1.

“ftmdaemon -d”を入力するコマンド・プロントとは別に新規コマンド・プロンプトをOpenする

Step2.

新規コマンド・プロンプト上で以下の太字コマンド実行し、Logcatバッファ内容を一旦クリア(消去)する。

C:\Users\[ID]> adb root

C:\Users\[ID]> adb logcat -c

Step3.

以下のコマンドを実行して Logcat出力を”logcat.log”というファイルに保存状態する。

C:\Users\[ID]> adb logcat > logcat.log

Step4.

“ftmdaemon -d”を入力するコマンド・プロントに戻り、

手順書8.1 から QRCT 上で ”HCI DUT Mode”でErrorとなる事象のところまで実行

Step5.

Step3. のコマンド・プロンプトに移り、“Ctrl+C”キー押下によるLogcatログ取得状態を強制終了する。

^C <-“Ctrl+C”キー押下

C:\Users\[ID]>

以上、お手数をおかけしますが本件不具合事象についてのログ取得ご協力の程、宜しくお願い致します。

千田誠

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 5:50 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

先ほどはお打ち合わせありがとうございました。

ご依頼の一覧をお送りいたします。

Lsコマンドの結果は一番下の方をご確認ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 11:28 AM

To: Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡有難うございます。

ご検討いただきありがとうございます。

本日私の方が午後はミーティングなどのため、

16:30もしく17:00頃からのTeamsミーティングでいかがでしょうか。

当社からは、

中山：

後夷：

酒井（任意）：

王（任意）：

望月：

が参加の予定です。

御社側の参加者様をお知らせいただけましたらミーティング設定いたします。

ログにつきましては確認いたしますのでお待ちください。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Friday, January 24, 2025 11:14 AM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

BT OFF状態でも”HCI DUT Mode”でError出る旨承知しました。

一度お送りしている実機の動きを確認させていただきたいので、本日午後にWebMTGは可能でしょうか。

(カメラで状況を共有しつつできるとありがたいです)

可能であれば、ご都合の良いお時間を教えていただければと存じます。

(15:00-16:00は外していただけると助かります)

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

ところで、下記を試していただきコマンドプロンプトに表示されるログを送付頂きたいです。

一度、QRCTと実機をDisconnectし、実機を再起動後、手順書の8.1から実行し、[ID]で以下コマンドを実行。

[ID]. Start FTM daemon

4) Execute the following command to start FTM daemon.

gen4_gvm:/ # ftmdaemon -nd

その後、QRCTにてHCI Reset、HCI DUT Mode　を実行した際にコマンドプロンプトに下記のようなログが表示されるはずです。

その画面キャプチャを展開いただきたく存じます。

Errorが表示される時(BT ON時)

問題ない時(BT OFF時)

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 10:29 AM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示の件確認いたしました。

BTの設定については、今までも”OFF”にしていたつもりでしたが、今回、改めて手順書の8.1から実行し、[ID]3ではBTの設定の”OFF”を確認して進めましたが、

やはり”HCI Reset”は正常に実行できますが、”HCI DUT Mode”では下記のエラーが表示されます。

もし、このまま解決できないようでしたら、可能でしたら来週以降でどなたか当社ご訪問いただき、実機でご確認いただくことなど調整いただくことは可能でしょうか。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, January 23, 2025 5:41 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

バージョン情報画面の取得ありがとうございました。

こちらで確認したバージョンと一致していること確認できました。

こちらで再現確認をおこなったところ BTの設定がONの場合、

ご連絡いただいた症状になることが確認できました。

手順書8.1.1.3.　Turn off Bluetooth　を実施されていますでしょうか？

下記状態がBluetooth OFFの状態です。

なお、手順書の 8.Bluetooth Test の操作は実機の電源をOFF/ONする度に必ず毎回実施してください。

電源ON時のすべての設定をを覚えているわけではない為です。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, January 23, 2025 3:45 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

ご指示いただきました画面の画像をお送りいたしますのでご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Wednesday, January 22, 2025 7:04 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

ご確認ありがとうございます。

こちらでも同じバージョンのソフトに書き換え、手順通りに動作確認を行いましたが、

“HCI Reset”も”HCI DUT Mode”もErrorなく実行できております。

·
現在確認作業はいただきました手順書に従って実行しており、12ページの”[ID]”の”1)”で、USBケーブルを接続すると、

·
DUTのディスプレイ上に下記のように表示され、DUT側でUSBケーブルを認識していることが確認できます。

·
(この表示は数秒で消えます。)

·
“USB Debugging connected”

·
Tag to turn off USB debugging

こちらはDUT側が接続先のPCを認識しているということになります。

この状態にならなければ、[ID]～[ID]1の設定はできないはずです。

·
また、お知らせしたとおり、21ページの”[ID]”の”2)”で、”HCI Reset”は正常に動作していることが確認できます。

”HCI DUT Mode”のみがErrorになるということですよね。

こちらでは同様の事象が発生しておらず、手順書通りに実施していただいているのであれば、対処方法が見つかりません。

Qualcommに念のため、下記方法でバージョン情報の画面キャプチャをいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, January 22, 2025 1:38 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在確認作業はいただきました手順書に従って実行しており、12ページの”[ID]”の”1)”で、USBケーブルを接続すると、

DUTのディスプレイ上に下記のように表示され、DUT側でUSBケーブルを認識していることが確認できます。

(この表示は数秒で消えます。)

“USB Debugging connected”

Tag to turn off USB debugging

また、お知らせしたとおり、21ページの”[ID]”の”2)”で、”HCI Reset”は正常に動作していることが確認できます。

他に何か確認するべきところや方法はございますでしょうか。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Monday, January 20, 2025 7:12 PM

To: Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡、ご確認ありがとうございます。

·
手順書8.1.2のPC Settingについて、実行していることをラボに確認できました。

ありがとうございます。承知しました。

·
8.1.2　PC Setting以外、考えられることは何かありませんでしょうか。

8.1. Initial Setting

5)Execute the following command to start
【Normal Running】 mode.

こちらの実施結果は以下のようになっていますでしょうか？

以上、ご確認よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 6:24 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

手順書8.1.2のPC Settingについて、実行していることをラボに確認できました。

“HCI Reset”は正常に実行できていますが、”HCI DUT Mode”でエラーが発生しているようです。

（念のため、8.1.2から再実行してみましたが、”HCI Reset”は正常で、”HCI DUT Mode”でエラーが発生しました。)

8.1.2　PC Setting以外、考えられることは何かありませんでしょうか。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun Wang

送信日時 : 2025 年 1 月 20 日 17:52

宛先 : Yuya Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

早速のご確認ありがとうございます。

ラボにお伝えいたします。

取り急ぎお礼まで。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Yuya Kitayama

送信日時 : 2025 年 1 月 20 日 17:42

宛先 : Jun Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

手順書の 8.1.2. PC setting (下記)は実行されていますでしょうか？

こちらを実行しないとHCI ResetやHCI DUT Mode押下時にエラーが出る症状がこちらでも確認出来ております。

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 5:26 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

標記テストツールの件先週末の続きですが、

現在ラボでは手順書に従って21ページの”2)”までは手順書通りに進められました。

21ページの”3)”で、”HCI DUT Mode”をクリックしたとき、下の図のようになるはずなのですが、

その下に記載したerrorが表示されています。

考えられる原因や対応策等ご教示いただけますと幸いです。

Error　SEND: QLIB_FTM_BT_Enable_Bluetooth()

Error　Failed: QLIB_FTM_BT_Enable_Bluetooth

お手数かけますが、何卒よろしくお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun Wang

送信日時 : 2025 年 1 月 17 日 17:40

宛先 : Yuya Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオン王君です。

標記の件早速ご確認いただきありがとうございます。

ソフトウェアは最新版の使用で問題がないこと承知いたしました。

ではQPSTをQUTSに読みかえてこのまま進めさせていただきます。

よろしくお願いいたします。

Outlook for Android を取得差出人: Yuya Kitayama

送信日時: 金曜日, 1月 17, 2025 5:32:45 午後宛先: Jun Wang ;
Masafumi Kaneko

件名: RE: 【ALAP】Q社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

お問い合わせいただいている件ですが、

動作手順書のツールのバージョンが少し古かったようで、

こちらでも最新版をインストールしたところ Library Modeは“QUTS”だけしか表示されませんでした。

その為、 QPST をQUTSと読み替えて使用してください。

基本的には最新バージョンを使用していただいて問題ありません。

(大幅なUIの変更はないと考えますが、こればかりはQualcomm社次第となりますので、

手順書と乖離する場合があることは許容いただけますと幸いです。)

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Friday, January 17, 2025 5:22 PM

To: 金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様アリオンの王君です。五月雨式となり失礼いたしました。

下記確認させていただいておりますLibrary Modeの変更に関して、

ソフトウェアバージョンとは関係ありますでしょうか。

弊社ラボではQualcommのソフトウェアは最新版をインストールしています。

手順書では、インストールの画面でソフトウェアのバージョンが見えていまして、

どうも古いバージョンのようです。

弊社でのインストールでは特定バージョンでのダウンロードが必要な場合、

ご連絡いただけますと幸いです。

ご確認いただきますようお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun Wang

送信日時 : 2025 年 1 月 17 日 16:50

宛先 : Masafumi Kaneko

件名 : 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様大平様いつもお世話になります、アリオンの王君です。

標記の件、いただきました動作手順書に従ってテストツールのインストールして、

進めている中、問題が発生しており、ご確認をお願いしてもよろしいでしょうか。

インストール手順：

Sub ContractorとしてAcceptする。

Package Manager 3を起動し、1.で登録したメールアドレスでログインする。

試験の手順書(Radio Law Test / BluetoothSIG Qualification Test Operation Manual (Android14))

の11ページに記載されている手順でインストールする。

その後、手順書を続けて実行してみたところ、17ページの2)のところで(下記参照)、Targetに”APQ”に変更できましたが、

Library Modeは“QUTS”だけしか表示されず、”QPST”への変更はできませんでした。

お忙しいところ恐縮ですが、ご確認いただけますと幸いです。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

---

## 4. 2025-02-06 04:10

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu

後夷さんお疲れさまです。

DTMモード投入アプリの動作報告ありがとうございます。

あとはInterLab側のAutomation Exploreで外部PCとのUSB-Aerial変換ケーブルのCOM#設定、9.600bps

設定、まずはHCI-Serialを選択してRF PHYコマンド確認で緑表示されるか試してください。

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年2月6日 13:00

宛先: Itsuo Sakai

件名: RE: 【内部連絡】FW: 【ALAP】Q社テストツールインストールの件酒井さん、

お疲れ様です。

手配していた [ID] メス / メス ( クロス ) ケーブルが届きましたので、接続したところ下記の様に ”connected” となり接続することができましたのでお知らせいたします。

その後、 InterLab のコントローラーの ”Command Definition” で、 ”LE Reset” 等を Test すると Error で赤くなり、

上記で ”Connected” だったところが ”not connected” となり、 ”Failed ～ ” と表示されました。

ご確認いただけますでしょうか。

よろしくお願いいたします。

後夷

From: Kenichi Ushiroebisu

Sent: Tuesday, February 4, 2025 4:22 PM

To: Itsuo Sakai

Subject: RE: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件酒井さん、

お疲れ様です。

外部 PC には、 DUT からの USB ケーブルのみ接続しており、 [ID] 変換ケーブルは接続しておりません。

現在、 RF 試験実施中ですので、こちらも明後日確認いたします。

よろしくお願いいたします。

後夷

From: Itsuo Sakai

Sent: Tuesday, February 4, 2025 4:17 PM

To: Kenichi Ushiroebisu

Subject: Re: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さんお疲れさまです。

クロスケーブルがないのでその先を繋げないのは理解しています。外部 PC の USB ポートに USB-Serial

変換ケーブルを繋いでいるかという質問です。

酒井差出人 :
Kenichi Ushiroebisu

送信日時 :
2025 年 2 月 4 日
16:12

宛先 :
Itsuo Sakai

件名 :
RE: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件酒井さん、

お疲れ様です。

お客様への回答についてご確認いただき、ありがとうございます。

後半のご質問についてですが、ケーブルが手配中でまだ届いておりませんので、テスターは制御用 PC に接続していません。

ケーブルは明日届く予定ですが、私が休みの日ですので、明後日、接続して確認いたします。

よろしくお願いいたします。

後夷

From: Itsuo Sakai

Sent: Tuesday, February 4, 2025 3:58 PM

To: Kenichi Ushiroebisu ; Toshitaka Mochizuki

Subject: Re: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さんお疲れさまです。

客先の「DUT( 実機 ) はどの COM
Port に接続されているのでしょうか。」に対しては「COM3」だけでよろしいと思います。

以下私からの質問ですが、テスター接続仮想 COM ポートの USB-Serial ケーブル ([ID] 側開放状態 ) は外部 PC に接続しましか？このケーブル接続がないと外部 PC は当該 ( 仮想 )COM ポートを認識しません。

酒井差出人 :
Kenichi Ushiroebisu

送信日時 :
2025 年 2 月 4 日
15:02

宛先 :
Toshitaka Mochizuki ; Itsuo Sakai

件名 :
RE: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件望月さん、

お疲れ様です。

現状では、 COM3 が DUT に接続されています。

Tester と接続するための [ID] ( クロス )
メス / メス - ケーブルがないため手配しています。

届き次第、 Tester と DUT に接続して確認します。

酒井さん、

DTM モードについて、私はまだ理解が足りていないかもしれないと思いますので、お客様へ上記の回答でよいか、ご確認いただけますでしょうか。

よろしくお願いいたします。

後夷

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 2:39 PM

To: Kenichi Ushiroebisu

Subject: 【内部連絡】 FW:
【ALAP】 Q 社テストツールインストールの件後夷さん望月です以下回答が参りましたのでご確認ください。

どうぞよろしくお願いいたします。

From: Yuya Kitayama

Sent: Tuesday, February 4, 2025 2:33 PM

To: Toshitaka Mochizuki ; Hitomi Ohira ; Makoto Chida ;
Jun Wang ; Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

PC と機材の接続状況がつかめず ( また、こちらで Tester を持ち合わせていない為 )

詳細な原因がつかめませんが、文面から Tester は COM3 に接続されていると読み取りました。

その場合、 DUT( 実機 ) はどの COM Port に接続されているのでしょうか。

DUT( 実機 ) と Tester の COM Port を同じ番号に指定し

Enable を押下すると同じエラーが表示されました。

DUT( 実機 ) と Tester の COM Port は別の番号になっておりますでしょうか。

QUTS Status App の画面キャプチャでもよいので展開いただけると何かわかるかもしれませんのでご教示ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 12:25 PM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ; Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在 QC.BluetoothLE_DirectMode.exe 起動の最終段階で ERROR が発生して DTM モードに投入できない状態となってしまいました。

解決策を何かご教示いただけますでしょうか。

“ QC.BluetoothLE_DirectMode.exe ”の起動ですが、 dll ファイルを” C:\[ID]\WCN\ProdTests\BIN ”から、” C:\Program
Files (x86)\[ID]\QDART\BIN ”にコピーしたところ、下記の設定画面が開きました。

なお、「[ID]19_REV_A_Bluetooth_Low_Energy_Direct_Test_Mode」の 14 ページの図とは少し違い、真ん中より少し上に” COM Port
‘ AUTO ’”と表示されています。

同文書の 14 ページの手順 2. の Step A. と Step B. は以下のようになっていますが、そのように設定はできないので、 QRCT での設定に合わせて A. の Target
Type は” APQ ”、 B. の ConnectionMode (QRCT では、 Library Mode) は” QUTS ”としました。

Step C. の Tester Port Settings で COM Port に、実際に接続されている” COM3 ”を選択すると、真ん中の少し上の” COM
Port ”に” Qualcomm ～”と表示されるので、それを選択しました。

Step D. で Enable をクリックしたところ、下記のようなエラーが表示されました。

Baurate が初期値で [ID] となっており、デバイスマネージャーで COM3 のプロパティで表示される 9600 にも設定してみましたが、同じエラーが表示されました。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 10:43 AM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

ご返信頂きありがとうございます。

RF 試験においては開始頂けているとのこと承知致しました。

また DTM モード遷移についても確認頂いている最中とのこと併せて承知致しました。

ご対応頂きありがとうございます。

上記確認結果次第になるかとは思いますが、試験日程につきまして目処が立っておりましたらご連絡お願いしたく、

お手数おかけし申し訳ありませんが、よろしくお願い致します。

/eom

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 10:22 AM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

試験の方お待たせしております。

現在 RF 試験については、 QRCT ソフトウェアで DUT モードに設定できるようになりましたので、測定を開始しています。こちらは結果出次第お知らせできると存じます。

RF PHY 試験については、 DTM モードへの遷移について確認中で、 DTM モードに遷移できるようになりましたら、測定が可能になります。

RF 試験後対応予定です。

なお、 RF PHY 試験につきましては台湾でも実施予定ですのでこの後発送書類の再確認いたします。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 9:18 AM

To: Yuya Kitayama ;
Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

BT 試験の件、色々とご迷惑おかけしており申し訳ありません。

先週末に北山より状況確認のお願いをさせて頂いておりますが、こちら如何でしょうか？

また、別メールにてお問合せ頂いておりました「DTM モードへの遷移について」についても Qualcomm からの資料を展開させて頂いておりますが、

こちらにつきましても併せて状況ご連絡頂けますと幸いです。

お手数おかけし申し訳ありません。

ご確認の程よろしくお願い致します。

/eom

From:
北山優哉 Yuya Kitayama

Sent: Friday, January 31, 2025 9:41 AM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

状況をお伺いしたく存じます。

下記でご連絡いただいておりましたが測定は開始出来ておりますでしょうか。

·
最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

·
なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に

·
実施いたします。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 5:25 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご対応、ご連絡ありがとうございました。

アップデートいただいたツールのバージョンに関して BT 試験に関係ありそうな箇所は、

想定通りでしたので問題ありません。

·
QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。

確認しました。無事動作したとのことで安心しました。

·
今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御が

·
できるということになりますので、それから測定が可能になると思います。

承知しました。引き続きご対応よろしくお願いいたします。

上記よりサンプルの回収は一旦なしにいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 5:15 PM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

Qualcomm Package Manager で、” Updates available ”にあったツールをすべてアップデートしました。

現在、こちらの PC にインストールされているツールバージョンのスクリーンショットを添付します。

(QPM_Installed_1.jpg, QPM_Installed_2.jpg)

なお、インストールされているツールが、御社から送られてきたスクリーンショットよりも多いですが、

これは昨年、こちらからも Qualcomm に直接問い合わせをして、インストールを指示されたためです。

( “ Qualcomm Software Center ”も Qualcomm の指示で入れたもので、これも今回アップデートしようとしたのですが、

全然進まなかったので、これだけアップデートできていません。 )

QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。 (QRCT_HCI_DUT_Mode.jpg)

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

HCI DUT Mode が成功した各ツールバージョンのスクリーンショットを添付しますので、

参考になさってください。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:04 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ログの取得、動作確認ありがとうございます。

ftmdaemon -ndd → QRCT にて HCI
Reset、 HCI DUT Mode クリック時のログが明らかに差異があるため、ツールの動作もしくは実機の反応に違いがあると考えます。

HCI DUT Mode クリック時のログが数回出ていましたので、

繰り返しでも接続できなかったと判断しました。

なお本日同事象を発生させることが出来ましたので、

サンプル返却までに以下の★を試していただけますでしょうか。

これで解消しない場合はサンプルの返却をお願いいたします。

・ツールの動作の原因として考えられること

→ QRCT、関連ツールのバージョンが最新ではない ( バージョン差によるツール同士の互換性含む )

添付の png を参考に QPM の「Updates Available」タブを開いていただき、

「Qualcomm USB Drivers Products」、 Qualcomm® Development Acceleration Resource Toolkit (QDART)」配下のアップデート可能なツールを最新にアップデートをお願いいたします。★

このリストに表示されるツールが最新ではないツールになります。

なお、 Qualcomm USB Drivers Products が古い状態で、 QRCT を最新にすると同事象が発生することを確認しております。

→ライセンスグループの差異

→送付いただいたキャプチャのツールのバージョンは同じですが、ライセンスグループ名には差異がありました。

もし上記で解消しない場合、同じ内容であるかは Qualcomm
しか分かりませんので問い合わせをお願いしたく存じます。

・実機の反応の違いとして考えられることハード面で差異があるかもしれませんので回収し確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 11:53 AM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

入れ違いで申し訳ございません。

先ほど確認結果をお送りいたしましたのでご確認ください。

ご確認の結果、必要でしたらサンプルをお返しいたしますのでお知らせください。

なお、大変恐縮ですが、本日体調不良のため在宅となっております。

サンプルお返しには少々お時間をいただく場合がございますのでご了承ください。

どうぞよろしくお願い致します。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 11:44 AM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

昨日の今日で申し訳ございませんが、ご連絡した方法で改善していますでしょうか。

もし改善しないようであれば、問題の切り分けを行うため、

一度実機 2 台を弊社に送り返していただくことは可能でしょうか。

送り先は以下でお願いいたします。

〒 [ID]

栃木県宇都宮市東宿郷 3-1-7

メットライフビル宇都宮ビル 8F

アルプスアルパイン ( 株 )

北山宛以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Monday, January 27, 2025 3:08 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

お忙し中ログの取得いただきありがとうございます。

取得いただいたログは確認を進めております。

ところで有識者から聞いた情報をもとに今一度、確認をお願いできないしょうか。

これで解消しない場合は実機の回収、差し替えも視野に入れております。

＝＝＝＝＝＝＝＝＝＝＝＝＝

・下記までは手順書通り

8.1.2. PC setting

4) Execute the following command to start FTM daemon.

gen4_gvm:/ #
ftmdaemon -ndd

を入力

↓

・ QRCT にて HCI Reset、 HCI DUT Mode をクリック

HCI DUT Mode で Error が出ても HCI DUT Mode を何回かクリックしてみてください。

( クリックのタイミングによって Error になることもあるようです )

その際のコマンドプロンプトのログを貼り付けて展開してください。

下記イメージでは見切れていますが HCI Reset
クリック時は Send Response = 14 が表示され、

HCI DUT Mode クリック時は Send Response = 15、 Send Response = 17 のログが表示されるはずです。

＝＝＝＝＝＝＝＝＝＝＝＝＝

Bluetooth and ANT QRCT Module をリフレッシュする。

QPM で QRCT → Bluetooth and ANT QRCT Module を検索し、

最新の v4.[ID] を Refresh インストールを実行する

＝＝＝＝＝＝＝＝＝＝＝＝＝

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, January 27, 2025 12:14 PM

To: 千田誠 Makoto Chida ;
北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン千田様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示いただきました手順を実行し、” logcat.log ”ファイルができましたので添付いたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Makoto Chida

Sent: Friday, January 24, 2025 8:15 PM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております、アルプスアルパイン千田誠です。

ご展開して頂いた“ bluetooth_bt_firmware.txt ” に出力されております、

gen4_gvm:/ # ls -l /vendor/bt_firmware/image の

BT 関連ファイル一覧について、不足ファイルなく弊社想定ファイルと一致していることを先ずはご連絡いたします。

次に本日の TeamsMTG の席でお伝えしておりました Logcat ログ取得について、以下にコマンド手順を記載します。

(Logcat ログについて、 DUT 側 Android システム上のアプリケーション / システム動作のログメッセージとなります。 )

このコマンド手順例 ) の場合、

Step6. で C:\Users\[ID]\logcat.log というファイル名が作成されおりますので、

この logcat.log ファイルを弊社にご展開の程、宜しくお願い致します。

Step1.

“ ftmdaemon -d ”を入力するコマンド・プロントとは別に新規コマンド・プロンプトを Open する

Step2.

新規コマンド・プロンプト上で以下の太字コマンド実行し、 Logcat バッファ内容を一旦クリア ( 消去 ) する。

C:\Users\[ID]> adb root

C:\Users\[ID]> adb logcat -c

Step3.

以下のコマンドを実行して Logcat 出力を” logcat.log ”というファイルに保存状態する。

C:\Users\[ID]> adb logcat > logcat.log

Step4.

“ ftmdaemon -d ”を入力するコマンド・プロントに戻り、

手順書 8.1 から QRCT 上で ” HCI DUT Mode ”で Error となる事象のところまで実行

Step5.

Step3. のコマンド・プロンプトに移り、“ Ctrl+C ”キー押下による Logcat ログ取得状態を強制終了する。

^C <- “ Ctrl+C ”キー押下

C:\Users\[ID]>

以上、お手数をおかけしますが本件不具合事象についてのログ取得ご協力の程、宜しくお願い致します。

千田誠

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 5:50 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

先ほどはお打ち合わせありがとうございました。

ご依頼の一覧をお送りいたします。

Ls コマンドの結果は一番下の方をご確認ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 11:28 AM

To: Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡有難うございます。

ご検討いただきありがとうございます。

本日私の方が午後はミーティングなどのため、

16:30 もしく 17:00 頃からの Teams ミーティングでいかがでしょうか。

当社からは、

中山：

後夷：

酒井（任意）：

王（任意）：

望月：

が参加の予定です。

御社側の参加者様をお知らせいただけましたらミーティング設定いたします。

ログにつきましては確認いたしますのでお待ちください。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Friday, January 24, 2025 11:14 AM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

BT OFF 状態でも” HCI DUT Mode ”で Error 出る旨承知しました。

一度お送りしている実機の動きを確認させていただきたいので、本日午後に WebMTG は可能でしょうか。

( カメラで状況を共有しつつできるとありがたいです )

可能であれば、ご都合の良いお時間を教えていただければと存じます。

(15:00-16:00 は外していただけると助かります )

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

ところで、下記を試していただきコマンドプロンプトに表示されるログを送付頂きたいです。

一度、 QRCT と実機を Disconnect し、実機を再起動後、手順書の 8.1 から実行し、 [ID]. で以下コマンドを実行。

[ID]. Start FTM daemon

4) Execute the following command to start FTM daemon.

gen4_gvm:/ # ftmdaemon -nd

その後、 QRCT にて HCI Reset、 HCI DUT Mode を実行した際にコマンドプロンプトに下記のようなログが表示されるはずです。

その画面キャプチャを展開いただきたく存じます。

Error が表示される時 (BT ON 時 )

問題ない時 (BT OFF 時 )

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 10:29 AM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示の件確認いたしました。

BT の設定については、今までも” OFF ”にしていたつもりでしたが、今回、改めて手順書の 8.1 から実行し、 [ID] では BT の設定の” OFF ”を確認して進めましたが、

やはり” HCI Reset ”は正常に実行できますが、” HCI DUT Mode ”では下記のエラーが表示されます。

もし、このまま解決できないようでしたら、可能でしたら来週以降でどなたか当社ご訪問いただき、実機でご確認いただくことなど調整いただくことは可能でしょうか。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, January 23, 2025 5:41 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

バージョン情報画面の取得ありがとうございました。

こちらで確認したバージョンと一致していること確認できました。

こちらで再現確認をおこなったところ BT の設定が ON の場合、

ご連絡いただいた症状になることが確認できました。

手順書 [ID]. Turn off Bluetooth を実施されていますでしょうか？

下記状態が Bluetooth OFF の状態です。

なお、手順書の 8.Bluetooth Test の操作は実機の電源を OFF/ON する度に必ず毎回実施してください。

電源 ON 時のすべての設定をを覚えているわけではない為です。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, January 23, 2025 3:45 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

ご指示いただきました画面の画像をお送りいたしますのでご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Wednesday, January 22, 2025 7:04 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

ご確認ありがとうございます。

こちらでも同じバージョンのソフトに書き換え、手順通りに動作確認を行いましたが、

“ HCI Reset ”も” HCI DUT Mode ”も Error なく実行できております。

·
現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、

·
DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。

·
( この表示は数秒で消えます。 )

·

“ USB Debugging connected ”

·
Tag to turn off USB debugging

こちらは DUT 側が接続先の PC を認識しているということになります。

この状態にならなければ、 [ID] ～ [ID] の設定はできないはずです。

·
また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

” HCI DUT Mode ”のみが Error になるということですよね。

こちらでは同様の事象が発生しておらず、手順書通りに実施していただいているのであれば、対処方法が見つかりません。

Qualcomm に念のため、下記方法でバージョン情報の画面キャプチャをいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, January 22, 2025 1:38 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、

DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。

( この表示は数秒で消えます。 )

“ USB Debugging connected ”

Tag to turn off USB debugging

また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

他に何か確認するべきところや方法はございますでしょうか。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Monday, January 20, 2025 7:12 PM

To: Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡、ご確認ありがとうございます。

·
手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

ありがとうございます。承知しました。

·
8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

8.1. Initial Setting

5)Execute the following command to start
【Normal Running】 mode.

こちらの実施結果は以下のようになっていますでしょうか？

以上、ご確認よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 6:24 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

“ HCI Reset ”は正常に実行できていますが、” HCI DUT Mode ”でエラーが発生しているようです。

（念のため、 8.1.2 から再実行してみましたが、” HCI Reset ”は正常で、” HCI DUT Mode ”でエラーが発生しました。 )

8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 20 日
17:52

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

早速のご確認ありがとうございます。

ラボにお伝えいたします。

取り急ぎお礼まで。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Yuya
Kitayama

送信日時 : 2025 年 1 月 20 日
17:42

宛先 : Jun
Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

手順書の 8.1.2. PC setting ( 下記 ) は実行されていますでしょうか？

こちらを実行しないと HCI Reset や HCI DUT Mode 押下時にエラーが出る症状がこちらでも確認出来ております。

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 5:26 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

標記テストツールの件先週末の続きですが、

現在ラボでは手順書に従って 21 ページの” 2) ”までは手順書通りに進められました。

21 ページの” 3) ”で、” HCI DUT Mode ”をクリックしたとき、下の図のようになるはずなのですが、

その下に記載した error が表示されています。

考えられる原因や対応策等ご教示いただけますと幸いです。

Error SEND: QLIB_FTM_BT_Enable_Bluetooth()

Error Failed: QLIB_FTM_BT_Enable_Bluetooth

お手数かけますが、何卒よろしくお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 17:40

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオン王君です。

標記の件早速ご確認いただきありがとうございます。

ソフトウェアは最新版の使用で問題がないこと承知いたしました。

では QPST を QUTS に読みかえてこのまま進めさせていただきます。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Yuya Kitayama

送信日時 : 金曜日 , 1 月 17, 2025 5:32:45
午後宛先 : Jun Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

お問い合わせいただいている件ですが、

動作手順書のツールのバージョンが少し古かったようで、

こちらでも最新版をインストールしたところ Library Mode は“ QUTS ”だけしか表示されませんでした。

その為、 QPST
を QUTS と読み替えて使用してください。

基本的には最新バージョンを使用していただいて問題ありません。

( 大幅な UI の変更はないと考えますが、こればかりは Qualcomm 社次第となりますので、

手順書と乖離する場合があることは許容いただけますと幸いです。 )

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Friday, January 17, 2025 5:22 PM

To: 金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様アリオンの王君です。五月雨式となり失礼いたしました。

下記確認させていただいております Library Mode の変更に関して、

ソフトウェアバージョンとは関係ありますでしょうか。

弊社ラボでは Qualcomm のソフトウェアは最新版をインストールしています。

手順書では、インストールの画面でソフトウェアのバージョンが見えていまして、

どうも古いバージョンのようです。

弊社でのインストールでは特定バージョンでのダウンロードが必要な場合、

ご連絡いただけますと幸いです。

ご確認いただきますようお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 16:50

宛先 : Masafumi
Kaneko

件名 : 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様大平様いつもお世話になります、アリオンの王君です。

標記の件、いただきました動作手順書に従ってテストツールのインストールして、

進めている中、問題が発生しており、ご確認をお願いしてもよろしいでしょうか。

インストール手順：

Sub Contractor として Accept する。

Package Manager 3 を起動し、 1. で登録したメールアドレスでログインする。

試験の手順書 (Radio Law Test / BluetoothSIG Qualification Test Operation Manual (Android14))

の 11 ページに記載されている手順でインストールする。

その後、手順書を続けて実行してみたところ、 17 ページの 2) のところで ( 下記参照 )、 Target に” APQ ”に変更できましたが、

Library Mode は“ QUTS ”だけしか表示されず、” QPST ”への変更はできませんでした。

お忙しいところ恐縮ですが、ご確認いただけますと幸いです。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

---

## 5. 2025-02-07 11:28

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki

望月さんお疲れさまです。

以下のように返信してください。

酒井ーーーー
HCIコマンドでのサポート有無の確認であれば、サポート有の判定となるはずですが、
認証試験ではEnhanced Power Controlが有効になったかどうかをどのように確認されていますでしょうか。

⇒Enhanced Power Controlサポート有無に関してご確認いただきありがとうございます。

認証試験としてのRF試験は、SIG認定テストシステム（当社所有はInterLab RF Test System）が自動試験を行います。試験項目は事前に試験項目メニューから選択してテストシステムは順にの試験制御コマンドをアンテナ信号測定端子経由でDUTに送信して各試験項目のテスト仕様書規定の試験内容を実行します。試験項目毎の冒頭のコマンドでサポート確認を行っているようで添付の2402MHzのログ

(2441MHz,2480MHzも同内容のため未添付)のログファイルの赤字部分に記載されているように、DUT

からRFテストシステムにはアンテナ信号測定端子経由でNot Supportと応答しています。

BT: ERROR: OUT indicates that it does not support Enhanced Power Control (EPC).

Final Verdict: [ID]

こんなことを申し上げるのは釈迦に説法とは存じますが
Enhanced Power Controlが有効となるためには、
両方の機器がEnhanced Power Controlに対応している必要があるようです。
もしEnhanced Power Controlが有効となったかの確認を行われているのであれば、
対向機側もEnhanced Power Controlをサポートするものでご確認をいただければと存じます。

⇒実機対向ではそのとおりでRF階層のネゴシエーションで双方の機器がサポートしている共通機能で通信が開始されます。

認証テスターはもちろん「RF/TRM/CA/[ID] (Enhanced Power Control)」試験に対応していて事前の試験項目選択でEnhanced Power Controlを選択すれば実際の試験段階ではEnhanced Power

Controlの規定に従ってPower UP / Power DownのコマンドをDUTに投げて当該試験を実施します。

今回はDUTモード下でDUTが「Not support Enhanced Power Control」と応答するためにRFテストシステムは当該項目の試験をその時点で打ち切っています。

お手数ですがQ社に「HCIコマンドではEnhanced Power Control：YESだが、InterLab RFテストシステムの試験では「ERROR: OUT indicates that it does not support Enhanced Power Control」

のためRF/TRM/CA/[ID] (Enhanced Power Control)にPassしない。対処方法をアドバイスして欲しい」と依頼してください。

ーーーー差出人: Yuya Kitayama

送信日時: 2025年2月7日 19:51

宛先: Toshitaka Mochizuki ; Hitomi Ohira ; Makoto Chida ; Jun Wang ; Masafumi Kaneko

件名: RE: 【ALAP】Q社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

Enhanced Power Control をサポート状況について調査結果をご報告いたします。

Blutooth オンした時の HCI ログ（添付画像）を確認したところ、自身のサポートする機能を Read していますが、

「Enhanced Power Control: True」となっており、 Enhanced Power Control をサポートしている結果となっております。

恐れ入りますが、再度ご確認をいただくことは可能でしょうか。

HCI コマンドでのサポート有無の確認であれば、サポート有の判定となるはずですが、

認証試験では Enhanced Power Control が有効になったかどうかをどのように確認されていますでしょうか。

こんなことを申し上げるのは釈迦に説法とは存じますが

Enhanced Power Control が有効となるためには、

両方の機器が Enhanced Power Control に対応している必要があるようです。

もし Enhanced Power Control が有効となったかの確認を行われているのであれば、

対向機側も Enhanced Power Control をサポートするものでご確認をいただければと存じます。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Friday, February 7, 2025 4:09 PM

To: Toshitaka Mochizuki ; 大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ; Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認、キャプチャありがとうございます。

Tester と DUT がまずは接続できたようで安心しました。

ところでご質問いただいている件ですが、

Tester port Settings の Baudrate の値が [ID] であったとしても同じ結果になりますでしょうか。

ご確認をお願いいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, February 7, 2025 3:10 PM

To: 北山優哉 Yuya Kitayama ;
大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご教示ありがとうございます。

確認させていただきたいのですが、新しい手順書の「手順 4 から」ということですと、

前提条件に記載されている「デバッグボードの Soc 端子」への接続や、

接続手順の「1. ADB 接続」の「USB debugging」の設定は行わなくてもよいという理解でよろしいでしょうか。

上記の前提で、「手順 4」から進めました。

下記の通り、 PC には、 COM3 に DUT が、 COM5 にテスターが接続されております。

下記が QUTS の表示になります。

COM3 (DUT)

COM5 ( テスター )

“ QC.BluetoothLE_DirectMode.exe ”を実行し、 Enable をクリックすると” DUT Connected ”と表示されました。

テスター機器から、“ Reset ”コマンドシークエンスを送ったのですが、下記のような表示がでました。

テスター機器側では、” Reset ”のエラーが表示されました。

上記の内容をご確認いただき、直すべきところや、確認するところがございましたら、ご連絡いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, February 6, 2025 7:28 PM

To: Toshitaka Mochizuki ;
Hitomi Ohira ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

手順 3 までは以前お送りした手順書と重複する内容ですので、手順 4 からご確認ください。

前述の通りですが、ご質問いただいている件は、認証試験を行っていただくうえで実施、ご確認は頂かなくてよい内容となります。

やむを得ずソフトの書き換え等により設定が解除されてしまった場合に実施、ご確認いただく内容となります。

「1.ADB 接続」で、下記の通り“ USB debugging ”の項目が有効になっていることは確認できましたが、
“ USB debugging ”を抜けて通常モードに戻すにはどうすればよいでしょうか。

通常モードに戻す必要はありません。

設定を変更して通常モードにしてしまうと、 DUT の制御に制約が加えられるためです。

「1.ADB 接続」で、下記の「デバッグボードの Soc 端子」とはどこのことでしょうか。
DUT の外部に出ている基板の上の USB 端子でしょうか。

ご認識の通りデバッグボード上の端子のことですが、こちらもご確認いただく必要はありません。

Peripheral モードであるが故に ADB 接続が出来ております。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, February 6, 2025 4:57 PM

To: 北山優哉 Yuya Kitayama ;
大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

書類の更新ありがとうございます。

新しい手順書「[ID] 設定手順 ( 仮 ).xlsx」を実施していますが、分からないことがありますので以下ご教示いただけますでしょうか。

「1.ADB 接続」で、下記の通り“ USB debugging ”の項目が有効になっていることは確認できましたが、

“ USB debugging ”を抜けて通常モードに戻すにはどうすればよいでしょうか。

( 電源の再投入はしましたが、戻りませんでした。 )

「1.ADB 接続」で、下記の「デバッグボードの Soc 端子」とはどこのことでしょうか。

DUT の外部に出ている基板の上の USB 端子でしょうか。

以上、ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, February 6, 2025 2:39 PM

To: Toshitaka Mochizuki ;
Hitomi Ohira ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

2 点ご報告いたします。

・ Enhanced Power Control については現在確認中です。

・ RF PHY 試験における DTM へのモード遷移について突貫で作成した資料を添付いたします。

手順 3 までは以前お送りした手順書と重複する内容ですので、手順 4 からご確認ください。

想定する試験環境の構成も載せてありますのでご確認ください。

Qcom から展開されている手順書で RF PHY 試験が実施できるのかの見極めを行いと考えております。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, February 5, 2025 10:43 AM

To: 北山優哉 Yuya Kitayama ;
大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

大変お待たせいたしました。

RF 試験が一通り完了し、「RF/TRM/CA/[ID]」以外は Pass しました。「RF/TRM/CA/[ID]」は 12 月中旬に Q 社に問い合わせていただき、下記のように Support YES との回答を頂きましたので実施しました。
(3) Enhanced Power Control (Yes or No)
→ Yes

しかし下記試験ログの引用部のようにテストサンプルは Enhanced Power Control をサポートしていないしていないと RF テストシステムに応答しています。

Tx Freq | Step | Packet | Measur. | Avg. P. | P. Diff. | P. Limit | Result | Test Status

(MHz) | | Type | | (dBm) | (dB) | (dB) | |

--BT: ERROR: OUT indicates that it does not support Enhanced Power Control (EPC).

Final Verdict: [ID]

今一度 Q 社に Enhanced Power Control はサポート NO ではないかご確認ください。

Enhanced Power Control はサポート NO の回答があれば RF 試験は Pass 完了となりますが、もし YES

ですとテストサンプルの SoC の設定を Enhanced Power Control:YES に変更していただき再試験の必要があります。

先ずは上記ご確認いただけますでしょうか。

また、本日エンジニアが不在となっておりますので、実機での確認事項等は明日の対応となる場合がございますのでご了承ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, February 4, 2025 2:33 PM

To: Toshitaka Mochizuki ;
Hitomi Ohira ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

PC と機材の接続状況がつかめず ( また、こちらで Tester を持ち合わせていない為 )

詳細な原因がつかめませんが、文面から Tester は COM3 に接続されていると読み取りました。

その場合、 DUT( 実機 ) はどの COM Port に接続されているのでしょうか。

DUT( 実機 ) と Tester の COM Port を同じ番号に指定し

Enable を押下すると同じエラーが表示されました。

DUT( 実機 ) と Tester の COM Port は別の番号になっておりますでしょうか。

QUTS Status App の画面キャプチャでもよいので展開いただけると何かわかるかもしれませんのでご教示ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 12:25 PM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在 QC.BluetoothLE_DirectMode.exe 起動の最終段階で ERROR が発生して DTM モードに投入できない状態となってしまいました。

解決策を何かご教示いただけますでしょうか。

“ QC.BluetoothLE_DirectMode.exe ”の起動ですが、 dll ファイルを” C:\[ID]\WCN\ProdTests\BIN ”から、” C:\Program
Files (x86)\[ID]\QDART\BIN ”にコピーしたところ、下記の設定画面が開きました。

なお、「[ID]19_REV_A_Bluetooth_Low_Energy_Direct_Test_Mode」の 14 ページの図とは少し違い、真ん中より少し上に” COM Port
‘ AUTO ’”と表示されています。

同文書の 14 ページの手順 2. の Step A. と Step B. は以下のようになっていますが、そのように設定はできないので、 QRCT での設定に合わせて A. の Target
Type は” APQ ”、 B. の ConnectionMode (QRCT では、 Library Mode) は” QUTS ”としました。

Step C. の Tester Port Settings で COM Port に、実際に接続されている” COM3 ”を選択すると、真ん中の少し上の” COM
Port ”に” Qualcomm ～”と表示されるので、それを選択しました。

Step D. で Enable をクリックしたところ、下記のようなエラーが表示されました。

Baurate が初期値で [ID] となっており、デバイスマネージャーで COM3 のプロパティで表示される 9600 にも設定してみましたが、同じエラーが表示されました。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 10:43 AM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

ご返信頂きありがとうございます。

RF 試験においては開始頂けているとのこと承知致しました。

また DTM モード遷移についても確認頂いている最中とのこと併せて承知致しました。

ご対応頂きありがとうございます。

上記確認結果次第になるかとは思いますが、試験日程につきまして目処が立っておりましたらご連絡お願いしたく、

お手数おかけし申し訳ありませんが、よろしくお願い致します。

/eom

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 10:22 AM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

試験の方お待たせしております。

現在 RF 試験については、 QRCT ソフトウェアで DUT モードに設定できるようになりましたので、測定を開始しています。こちらは結果出次第お知らせできると存じます。

RF PHY 試験については、 DTM モードへの遷移について確認中で、 DTM モードに遷移できるようになりましたら、測定が可能になります。

RF 試験後対応予定です。

なお、 RF PHY 試験につきましては台湾でも実施予定ですのでこの後発送書類の再確認いたします。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 9:18 AM

To: Yuya Kitayama ;
Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

BT 試験の件、色々とご迷惑おかけしており申し訳ありません。

先週末に北山より状況確認のお願いをさせて頂いておりますが、こちら如何でしょうか？

また、別メールにてお問合せ頂いておりました「DTM モードへの遷移について」についても Qualcomm からの資料を展開させて頂いておりますが、

こちらにつきましても併せて状況ご連絡頂けますと幸いです。

お手数おかけし申し訳ありません。

ご確認の程よろしくお願い致します。

/eom

From:
北山優哉 Yuya Kitayama

Sent: Friday, January 31, 2025 9:41 AM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

状況をお伺いしたく存じます。

下記でご連絡いただいておりましたが測定は開始出来ておりますでしょうか。

最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。
なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 5:25 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご対応、ご連絡ありがとうございました。

アップデートいただいたツールのバージョンに関して BT 試験に関係ありそうな箇所は、

想定通りでしたので問題ありません。

QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。

確認しました。無事動作したとのことで安心しました。

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

承知しました。引き続きご対応よろしくお願いいたします。

上記よりサンプルの回収は一旦なしにいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 5:15 PM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

Qualcomm Package Manager で、” Updates available ”にあったツールをすべてアップデートしました。

現在、こちらの PC にインストールされているツールバージョンのスクリーンショットを添付します。

(QPM_Installed_1.jpg, QPM_Installed_2.jpg)

なお、インストールされているツールが、御社から送られてきたスクリーンショットよりも多いですが、

これは昨年、こちらからも Qualcomm に直接問い合わせをして、インストールを指示されたためです。

( “ Qualcomm Software Center ”も Qualcomm の指示で入れたもので、これも今回アップデートしようとしたのですが、

全然進まなかったので、これだけアップデートできていません。 )

QRCT で” HCI DUT Mode ”が正常に実行できたところのスクリーンショットも添付いたします。 (QRCT_HCI_DUT_Mode.jpg)

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、 DUT の制御ができるということになりますので、それから測定が可能になると思います。

なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

HCI DUT Mode が成功した各ツールバージョンのスクリーンショットを添付しますので、

参考になさってください。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:04 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ログの取得、動作確認ありがとうございます。

ftmdaemon -ndd → QRCT にて HCI
Reset、 HCI DUT Mode クリック時のログが明らかに差異があるため、ツールの動作もしくは実機の反応に違いがあると考えます。

HCI DUT Mode クリック時のログが数回出ていましたので、

繰り返しでも接続できなかったと判断しました。

なお本日同事象を発生させることが出来ましたので、

サンプル返却までに以下の★を試していただけますでしょうか。

これで解消しない場合はサンプルの返却をお願いいたします。

・ツールの動作の原因として考えられること

→ QRCT、関連ツールのバージョンが最新ではない ( バージョン差によるツール同士の互換性含む )

添付の png を参考に QPM の「Updates Available」タブを開いていただき、

「Qualcomm USB Drivers Products」、 Qualcomm® Development Acceleration Resource Toolkit (QDART)」配下のアップデート可能なツールを最新にアップデートをお願いいたします。★

このリストに表示されるツールが最新ではないツールになります。

なお、 Qualcomm USB Drivers Products が古い状態で、 QRCT を最新にすると同事象が発生することを確認しております。

→ライセンスグループの差異

→送付いただいたキャプチャのツールのバージョンは同じですが、ライセンスグループ名には差異がありました。

もし上記で解消しない場合、同じ内容であるかは Qualcomm
しか分かりませんので問い合わせをお願いしたく存じます。

・実機の反応の違いとして考えられることハード面で差異があるかもしれませんので回収し確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 11:53 AM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

入れ違いで申し訳ございません。

先ほど確認結果をお送りいたしましたのでご確認ください。

ご確認の結果、必要でしたらサンプルをお返しいたしますのでお知らせください。

なお、大変恐縮ですが、本日体調不良のため在宅となっております。

サンプルお返しには少々お時間をいただく場合がございますのでご了承ください。

どうぞよろしくお願い致します。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 11:44 AM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

昨日の今日で申し訳ございませんが、ご連絡した方法で改善していますでしょうか。

もし改善しないようであれば、問題の切り分けを行うため、

一度実機 2 台を弊社に送り返していただくことは可能でしょうか。

送り先は以下でお願いいたします。

〒 [ID]

栃木県宇都宮市東宿郷 3-1-7

メットライフビル宇都宮ビル 8F

アルプスアルパイン ( 株 )

北山宛以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Monday, January 27, 2025 3:08 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

お忙し中ログの取得いただきありがとうございます。

取得いただいたログは確認を進めております。

ところで有識者から聞いた情報をもとに今一度、確認をお願いできないしょうか。

これで解消しない場合は実機の回収、差し替えも視野に入れております。

＝＝＝＝＝＝＝＝＝＝＝＝＝

・下記までは手順書通り

8.1.2. PC setting

4) Execute the following command to start FTM daemon.

gen4_gvm:/ #
ftmdaemon -ndd

を入力

↓

・ QRCT にて HCI Reset、 HCI DUT Mode をクリック

HCI DUT Mode で Error が出ても HCI DUT Mode を何回かクリックしてみてください。

( クリックのタイミングによって Error になることもあるようです )

その際のコマンドプロンプトのログを貼り付けて展開してください。

下記イメージでは見切れていますが HCI Reset
クリック時は Send Response = 14 が表示され、

HCI DUT Mode クリック時は Send Response = 15、 Send Response = 17 のログが表示されるはずです。

＝＝＝＝＝＝＝＝＝＝＝＝＝

Bluetooth and ANT QRCT Module をリフレッシュする。

QPM で QRCT → Bluetooth and ANT QRCT Module を検索し、

最新の v4.[ID] を Refresh インストールを実行する

＝＝＝＝＝＝＝＝＝＝＝＝＝

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, January 27, 2025 12:14 PM

To: 千田誠 Makoto Chida ;
北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン千田様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示いただきました手順を実行し、” logcat.log ”ファイルができましたので添付いたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Makoto Chida

Sent: Friday, January 24, 2025 8:15 PM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To. アリオン株式会社望月様お世話になっております、アルプスアルパイン千田誠です。

ご展開して頂いた“ bluetooth_bt_firmware.txt ” に出力されております、

gen4_gvm:/ # ls -l /vendor/bt_firmware/image の

BT 関連ファイル一覧について、不足ファイルなく弊社想定ファイルと一致していることを先ずはご連絡いたします。

次に本日の TeamsMTG の席でお伝えしておりました Logcat ログ取得について、以下にコマンド手順を記載します。

(Logcat ログについて、 DUT 側 Android システム上のアプリケーション / システム動作のログメッセージとなります。 )

このコマンド手順例 ) の場合、

Step6. で C:\Users\[ID]\logcat.log というファイル名が作成されおりますので、

この logcat.log ファイルを弊社にご展開の程、宜しくお願い致します。

Step1.

“ ftmdaemon -d ”を入力するコマンド・プロントとは別に新規コマンド・プロンプトを Open する

Step2.

新規コマンド・プロンプト上で以下の太字コマンド実行し、 Logcat バッファ内容を一旦クリア ( 消去 ) する。

C:\Users\[ID]> adb root

C:\Users\[ID]> adb logcat -c

Step3.

以下のコマンドを実行して Logcat 出力を” logcat.log ”というファイルに保存状態する。

C:\Users\[ID]> adb logcat > logcat.log

Step4.

“ ftmdaemon -d ”を入力するコマンド・プロントに戻り、

手順書 8.1 から QRCT 上で ” HCI DUT Mode ”で Error となる事象のところまで実行

Step5.

Step3. のコマンド・プロンプトに移り、“ Ctrl+C ”キー押下による Logcat ログ取得状態を強制終了する。

^C <- “ Ctrl+C ”キー押下

C:\Users\[ID]>

以上、お手数をおかけしますが本件不具合事象についてのログ取得ご協力の程、宜しくお願い致します。

千田誠

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 5:50 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

先ほどはお打ち合わせありがとうございました。

ご依頼の一覧をお送りいたします。

Ls コマンドの結果は一番下の方をご確認ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 11:28 AM

To: Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡有難うございます。

ご検討いただきありがとうございます。

本日私の方が午後はミーティングなどのため、

16:30 もしく 17:00 頃からの Teams ミーティングでいかがでしょうか。

当社からは、

中山：

後夷：

酒井（任意）：

王（任意）：

望月：

が参加の予定です。

御社側の参加者様をお知らせいただけましたらミーティング設定いたします。

ログにつきましては確認いたしますのでお待ちください。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Friday, January 24, 2025 11:14 AM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

BT OFF 状態でも” HCI DUT Mode ”で Error 出る旨承知しました。

一度お送りしている実機の動きを確認させていただきたいので、本日午後に WebMTG は可能でしょうか。

( カメラで状況を共有しつつできるとありがたいです )

可能であれば、ご都合の良いお時間を教えていただければと存じます。

(15:00-16:00 は外していただけると助かります )

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

ところで、下記を試していただきコマンドプロンプトに表示されるログを送付頂きたいです。

一度、 QRCT と実機を Disconnect し、実機を再起動後、手順書の 8.1 から実行し、 [ID]. で以下コマンドを実行。

[ID]. Start FTM daemon

4) Execute the following command to start FTM daemon.

gen4_gvm:/ # ftmdaemon -nd

その後、 QRCT にて HCI Reset、 HCI DUT Mode を実行した際にコマンドプロンプトに下記のようなログが表示されるはずです。

その画面キャプチャを展開いただきたく存じます。

Error が表示される時 (BT ON 時 )

問題ない時 (BT OFF 時 )

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 10:29 AM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示の件確認いたしました。

BT の設定については、今までも” OFF ”にしていたつもりでしたが、今回、改めて手順書の 8.1 から実行し、 [ID] では BT の設定の” OFF ”を確認して進めましたが、

やはり” HCI Reset ”は正常に実行できますが、” HCI DUT Mode ”では下記のエラーが表示されます。

もし、このまま解決できないようでしたら、可能でしたら来週以降でどなたか当社ご訪問いただき、実機でご確認いただくことなど調整いただくことは可能でしょうか。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, January 23, 2025 5:41 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

バージョン情報画面の取得ありがとうございました。

こちらで確認したバージョンと一致していること確認できました。

こちらで再現確認をおこなったところ BT の設定が ON の場合、

ご連絡いただいた症状になることが確認できました。

手順書 [ID]. Turn off Bluetooth を実施されていますでしょうか？

下記状態が Bluetooth OFF の状態です。

なお、手順書の 8.Bluetooth Test の操作は実機の電源を OFF/ON する度に必ず毎回実施してください。

電源 ON 時のすべての設定をを覚えているわけではない為です。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, January 23, 2025 3:45 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

ご指示いただきました画面の画像をお送りいたしますのでご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Wednesday, January 22, 2025 7:04 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

ご確認ありがとうございます。

こちらでも同じバージョンのソフトに書き換え、手順通りに動作確認を行いましたが、

“ HCI Reset ”も” HCI DUT Mode ”も Error なく実行できております。

現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、
DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。
( この表示は数秒で消えます。 )

“ USB Debugging connected ”
Tag to turn off USB debugging

こちらは DUT 側が接続先の PC を認識しているということになります。

この状態にならなければ、 [ID] ～ [ID] の設定はできないはずです。

また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

” HCI DUT Mode ”のみが Error になるということですよね。

こちらでは同様の事象が発生しておらず、手順書通りに実施していただいているのであれば、対処方法が見つかりません。

Qualcomm に念のため、下記方法でバージョン情報の画面キャプチャをいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, January 22, 2025 1:38 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在確認作業はいただきました手順書に従って実行しており、 12 ページの” [ID] ”の” 1) ”で、 USB ケーブルを接続すると、

DUT のディスプレイ上に下記のように表示され、 DUT 側で USB ケーブルを認識していることが確認できます。

( この表示は数秒で消えます。 )

“ USB Debugging connected ”

Tag to turn off USB debugging

また、お知らせしたとおり、 21 ページの” [ID] ”の” 2) ”で、” HCI Reset ”は正常に動作していることが確認できます。

他に何か確認するべきところや方法はございますでしょうか。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Monday, January 20, 2025 7:12 PM

To: Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡、ご確認ありがとうございます。

手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

ありがとうございます。承知しました。

8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

8.1. Initial Setting

5)Execute the following command to start
【Normal Running】 mode.

こちらの実施結果は以下のようになっていますでしょうか？

以上、ご確認よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 6:24 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

手順書 8.1.2 の PC Setting について、実行していることをラボに確認できました。

“ HCI Reset ”は正常に実行できていますが、” HCI DUT Mode ”でエラーが発生しているようです。

（念のため、 8.1.2 から再実行してみましたが、” HCI Reset ”は正常で、” HCI DUT Mode ”でエラーが発生しました。 )

8.1.2 PC Setting 以外、考えられることは何かありませんでしょうか。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 20 日
17:52

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

早速のご確認ありがとうございます。

ラボにお伝えいたします。

取り急ぎお礼まで。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Yuya
Kitayama

送信日時 : 2025 年 1 月 20 日
17:42

宛先 : Jun
Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

手順書の 8.1.2. PC setting ( 下記 ) は実行されていますでしょうか？

こちらを実行しないと HCI Reset や HCI DUT Mode 押下時にエラーが出る症状がこちらでも確認出来ております。

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 5:26 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

標記テストツールの件先週末の続きですが、

現在ラボでは手順書に従って 21 ページの” 2) ”までは手順書通りに進められました。

21 ページの” 3) ”で、” HCI DUT Mode ”をクリックしたとき、下の図のようになるはずなのですが、

その下に記載した error が表示されています。

考えられる原因や対応策等ご教示いただけますと幸いです。

Error SEND: QLIB_FTM_BT_Enable_Bluetooth()

Error Failed: QLIB_FTM_BT_Enable_Bluetooth

お手数かけますが、何卒よろしくお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 17:40

宛先 : Yuya
Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオン王君です。

標記の件早速ご確認いただきありがとうございます。

ソフトウェアは最新版の使用で問題がないこと承知いたしました。

では QPST を QUTS に読みかえてこのまま進めさせていただきます。

よろしくお願いいたします。

Outlook for Android を取得差出人 : Yuya Kitayama

送信日時 : 金曜日 , 1 月 17, 2025 5:32:45
午後宛先 : Jun Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

お問い合わせいただいている件ですが、

動作手順書のツールのバージョンが少し古かったようで、

こちらでも最新版をインストールしたところ Library Mode は“ QUTS ”だけしか表示されませんでした。

その為、 QPST
を QUTS と読み替えて使用してください。

基本的には最新バージョンを使用していただいて問題ありません。

( 大幅な UI の変更はないと考えますが、こればかりは Qualcomm 社次第となりますので、

手順書と乖離する場合があることは許容いただけますと幸いです。 )

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Friday, January 17, 2025 5:22 PM

To: 金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様アリオンの王君です。五月雨式となり失礼いたしました。

下記確認させていただいております Library Mode の変更に関して、

ソフトウェアバージョンとは関係ありますでしょうか。

弊社ラボでは Qualcomm のソフトウェアは最新版をインストールしています。

手順書では、インストールの画面でソフトウェアのバージョンが見えていまして、

どうも古いバージョンのようです。

弊社でのインストールでは特定バージョンでのダウンロードが必要な場合、

ご連絡いただけますと幸いです。

ご確認いただきますようお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun
Wang

送信日時 : 2025 年 1 月 17 日 16:50

宛先 : Masafumi
Kaneko

件名 : 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様大平様いつもお世話になります、アリオンの王君です。

標記の件、いただきました動作手順書に従ってテストツールのインストールして、

進めている中、問題が発生しており、ご確認をお願いしてもよろしいでしょうか。

インストール手順：

Sub Contractor として Accept する。

Package Manager 3 を起動し、 1. で登録したメールアドレスでログインする。

試験の手順書 (Radio Law Test / BluetoothSIG Qualification Test Operation Manual (Android14))

の 11 ページに記載されている手順でインストールする。

その後、手順書を続けて実行してみたところ、 17 ページの 2) のところで ( 下記参照 )、 Target に” APQ ”に変更できましたが、

Library Mode は“ QUTS ”だけしか表示されず、” QPST ”への変更はできませんでした。

お忙しいところ恐縮ですが、ご確認いただけますと幸いです。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

---

## 6. 2025-02-07 11:47

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki
**Attachments:** TRM14_VN_TN_2402_Max_EPC_C_2025-[ID]rtf

望月さんお疲れさまです。

2402MHzのログを添付して再送します。

望月さんお疲れさまです。

以下のように返信してください。

酒井ーーーー
HCIコマンドでのサポート有無の確認であれば、サポート有の判定となるはずですが、
認証試験ではEnhanced Power Controlが有効になったかどうかをどのように確認されていますでしょうか。

⇒Enhanced Power Controlサポート有無に関してご確認いただきありがとうございます。

認証試験としてのRF試験は、SIG認定テストシステム（当社所有はInterLab RF Test System）が自動試験を行います。試験項目は事前に試験項目メニューから選択してテストシステムは順にの試験制御コマンドをアンテナ信号測定端子経由でDUTに送信して各試験項目のテスト仕様書規定の試験内容を実行します。試験項目毎の冒頭のコマンドでサポート確認を行っているようで添付の2402MHzのログ

(2441MHz,2480MHzも同内容のため未添付)のログファイルの赤字部分に記載されているように、DUT

からRFテストシステムにはアンテナ信号測定端子経由でNot Supportと応答しています。

BT: ERROR: OUT indicates that it does not support Enhanced Power Control (EPC).

Final Verdict: [ID]

こんなことを申し上げるのは釈迦に説法とは存じますが
Enhanced Power Controlが有効となるためには、
両方の機器がEnhanced Power Controlに対応している必要があるようです。
もしEnhanced Power Controlが有効となったかの確認を行われているのであれば、
対向機側もEnhanced Power Controlをサポートするものでご確認をいただければと存じます。

⇒実機対向ではそのとおりでRF階層のネゴシエーションで双方の機器がサポートしている共通機能で通信が開始されます。

認証テスターはもちろん「RF/TRM/CA/[ID] (Enhanced Power Control)」試験に対応していて事前の試験項目選択でEnhanced Power Controlを選択すれば実際の試験段階ではEnhanced Power

Controlの規定に従ってPower UP / Power DownのコマンドをDUTに投げて当該試験を実施します。

今回はDUTモード下でDUTが「Not support Enhanced Power Control」と応答するためにRFテストシステムは当該項目の試験をその時点で打ち切っています。

お手数ですがQ社に「HCIコマンドではEnhanced Power Control：YESだが、InterLab RFテストシステムの試験では「ERROR: OUT indicates that it does not support Enhanced Power Control」

のためRF/TRM/CA/[ID] (Enhanced Power Control)にPassしない。対処方法をアドバイスして欲しい」と依頼してください。

ーーーー差出人: Yuya Kitayama

送信日時: 2025年2月7日 19:51

宛先: Toshitaka Mochizuki ; Hitomi Ohira ; Makoto Chida ; Jun Wang ; Masafumi Kaneko

件名: RE: 【ALAP】Q社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

Enhanced Power Controlをサポート状況について調査結果をご報告いたします。

Blutoothオンした時のHCIログ（添付画像）を確認したところ、自身のサポートする機能をReadしていますが、

「Enhanced Power Control: True」となっており、Enhanced Power Controlをサポートしている結果となっております。

恐れ入りますが、再度ご確認をいただくことは可能でしょうか。

HCIコマンドでのサポート有無の確認であれば、サポート有の判定となるはずですが、

認証試験ではEnhanced Power Controlが有効になったかどうかをどのように確認されていますでしょうか。

こんなことを申し上げるのは釈迦に説法とは存じますが

Enhanced Power Controlが有効となるためには、

両方の機器がEnhanced Power Controlに対応している必要があるようです。

もしEnhanced Power Controlが有効となったかの確認を行われているのであれば、

対向機側もEnhanced Power Controlをサポートするものでご確認をいただければと存じます。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Friday, February 7, 2025 4:09 PM

To: Toshitaka Mochizuki ; 大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ; Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認、キャプチャありがとうございます。

TesterとDUTがまずは接続できたようで安心しました。

ところでご質問いただいている件ですが、

Tester port SettingsのBaudrateの値が [ID] であったとしても同じ結果になりますでしょうか。

ご確認をお願いいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, February 7, 2025 3:10 PM

To: 北山優哉 Yuya Kitayama ;
大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご教示ありがとうございます。

確認させていただきたいのですが、新しい手順書の「手順4から」ということですと、

前提条件に記載されている「デバッグボードのSoc端子」への接続や、

接続手順の「1. ADB接続」の「USB debugging」の設定は行わなくてもよいという理解でよろしいでしょうか。

上記の前提で、「手順4」から進めました。

下記の通り、PCには、COM3にDUTが、COM5にテスターが接続されております。

下記がQUTSの表示になります。

COM3 (DUT)

COM5 (テスター)

“QC.BluetoothLE_DirectMode.exe”を実行し、Enableをクリックすると”DUT Connected”と表示されました。

テスター機器から、“Reset”コマンドシークエンスを送ったのですが、下記のような表示がでました。

テスター機器側では、”Reset”のエラーが表示されました。

上記の内容をご確認いただき、直すべきところや、確認するところがございましたら、ご連絡いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, February 6, 2025 7:28 PM

To: Toshitaka Mochizuki ;
Hitomi Ohira ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

手順3までは以前お送りした手順書と重複する内容ですので、手順4からご確認ください。

前述の通りですが、ご質問いただいている件は、認証試験を行っていただくうえで実施、ご確認は頂かなくてよい内容となります。

やむを得ずソフトの書き換え等により設定が解除されてしまった場合に実施、ご確認いただく内容となります。

「1.ADB接続」で、下記の通り“USB debugging”の項目が有効になっていることは確認できましたが、

“USB debugging”を抜けて通常モードに戻すにはどうすればよいでしょうか。

通常モードに戻す必要はありません。

設定を変更して通常モードにしてしまうと、DUTの制御に制約が加えられるためです。

「1.ADB接続」で、下記の「デバッグボードのSoc端子」とはどこのことでしょうか。

DUTの外部に出ている基板の上のUSB端子でしょうか。

ご認識の通りデバッグボード上の端子のことですが、こちらもご確認いただく必要はありません。

Peripheralモードであるが故にADB接続が出来ております。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, February 6, 2025 4:57 PM

To: 北山優哉 Yuya Kitayama ;
大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

書類の更新ありがとうございます。

新しい手順書「BLE_DTM設定手順(仮).xlsx」を実施していますが、分からないことがありますので以下ご教示いただけますでしょうか。

「1.ADB接続」で、下記の通り“USB debugging”の項目が有効になっていることは確認できましたが、

“USB debugging”を抜けて通常モードに戻すにはどうすればよいでしょうか。

(電源の再投入はしましたが、戻りませんでした。)

「1.ADB接続」で、下記の「デバッグボードのSoc端子」とはどこのことでしょうか。

DUTの外部に出ている基板の上のUSB端子でしょうか。

以上、ご回答どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, February 6, 2025 2:39 PM

To: Toshitaka Mochizuki ;
Hitomi Ohira ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

2点ご報告いたします。

・ Enhanced Power Controlについては現在確認中です。

・RF PHY試験におけるDTMへのモード遷移について突貫で作成した資料を添付いたします。

手順3までは以前お送りした手順書と重複する内容ですので、手順4からご確認ください。

想定する試験環境の構成も載せてありますのでご確認ください。

Qcomから展開されている手順書でRF PHY試験が実施できるのかの見極めを行いと考えております。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, February 5, 2025 10:43 AM

To: 北山優哉 Yuya Kitayama ;
大平ひとみ Hitomi Ohira ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

大変お待たせいたしました。

RF試験が一通り完了し、「RF/TRM/CA/[ID]」以外はPassしました。「RF/TRM/CA/[ID]」は12月中旬にQ社に問い合わせていただき、下記のようにSupport YESとの回答を頂きましたので実施しました。
(3) Enhanced Power Control (Yes or No) → Yes

しかし下記試験ログの引用部のようにテストサンプルはEnhanced Power ControlをサポートしていないしていないとRFテストシステムに応答しています。

Tx Freq | Step | Packet | Measur. | Avg. P. | P. Diff. | P. Limit | Result | Test Status

(MHz) | | Type | | (dBm) | (dB) | (dB) | |

--BT: ERROR: OUT indicates that it does not support Enhanced Power Control (EPC).

Final Verdict: [ID]

今一度Q社にEnhanced Power ControlはサポートNOではないかご確認ください。

Enhanced Power ControlはサポートNOの回答があればRF試験はPass完了となりますが、もしYES

ですとテストサンプルのSoCの設定をEnhanced Power Control:YESに変更していただき再試験の必要があります。

先ずは上記ご確認いただけますでしょうか。

また、本日エンジニアが不在となっておりますので、実機での確認事項等は明日の対応となる場合がございますのでご了承ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, February 4, 2025 2:33 PM

To: Toshitaka Mochizuki ;
Hitomi Ohira ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

PCと機材の接続状況がつかめず(また、こちらでTesterを持ち合わせていない為)

詳細な原因がつかめませんが、文面からTesterはCOM3に接続されていると読み取りました。

その場合、DUT(実機)はどのCOM Portに接続されているのでしょうか。

DUT(実機)とTesterのCOM Portを同じ番号に指定し

Enableを押下すると同じエラーが表示されました。

DUT(実機)とTesterのCOM Portは別の番号になっておりますでしょうか。

QUTS Status Appの画面キャプチャでもよいので展開いただけると何かわかるかもしれませんのでご教示ください。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 12:25 PM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在QC.BluetoothLE_DirectMode.exe起動の最終段階でERRORが発生してDTMモードに投入できない状態となってしまいました。

解決策を何かご教示いただけますでしょうか。

“QC.BluetoothLE_DirectMode.exe”の起動ですが、dllファイルを”C:\[ID]\WCN\ProdTests\BIN”から、”C:\Program Files (x86)\[ID]\QDART\BIN”にコピーしたところ、下記の設定画面が開きました。

なお、「[ID]19_REV_A_Bluetooth_Low_Energy_Direct_Test_Mode」の14ページの図とは少し違い、真ん中より少し上に”COM Port ‘AUTO’”と表示されています。

同文書の14ページの手順2.のStep A.とStep B.は以下のようになっていますが、そのように設定はできないので、QRCTでの設定に合わせてA.のTarget Typeは”APQ”、B.のConnectionMode (QRCTでは、Library Mode)は”QUTS”としました。

Step C.のTester Port SettingsでCOM Portに、実際に接続されている”COM3”を選択すると、真ん中の少し上の”COM Port”に”Qualcomm〜”と表示されるので、それを選択しました。

Step D.でEnableをクリックしたところ、下記のようなエラーが表示されました。

Baurateが初期値で115200となっており、デバイスマネージャーでCOM3のプロパティで表示される9600にも設定してみましたが、同じエラーが表示されました。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 10:43 AM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To.　アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

ご返信頂きありがとうございます。

RF試験においては開始頂けているとのこと承知致しました。

またDTMモード遷移についても確認頂いている最中とのこと併せて承知致しました。

ご対応頂きありがとうございます。

上記確認結果次第になるかとは思いますが、試験日程につきまして目処が立っておりましたらご連絡お願いしたく、

お手数おかけし申し訳ありませんが、よろしくお願い致します。

/eom

From: Toshitaka Mochizuki

Sent: Tuesday, February 4, 2025 10:22 AM

To: 大平ひとみ Hitomi Ohira ;
北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン大平様北山様いつもお世話になっております。

アリオン株式会社の望月です。

試験の方お待たせしております。

現在RF試験については、QRCTソフトウェアでDUTモードに設定できるようになりましたので、測定を開始しています。こちらは結果出次第お知らせできると存じます。

RF PHY試験については、DTMモードへの遷移について確認中で、DTMモードに遷移できるようになりましたら、測定が可能になります。

RF試験後対応予定です。

なお、RF PHY試験につきましては台湾でも実施予定ですのでこの後発送書類の再確認いたします。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hitomi Ohira

Sent: Tuesday, February 4, 2025 9:18 AM

To: Yuya Kitayama ;
Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To.　アリオン株式会社望月様お世話になっております。

アルプスアルパイン大平です。

BT試験の件、色々とご迷惑おかけしており申し訳ありません。

先週末に北山より状況確認のお願いをさせて頂いておりますが、こちら如何でしょうか？

また、別メールにてお問合せ頂いておりました「DTMモードへの遷移について」についてもQualcommからの資料を展開させて頂いておりますが、

こちらにつきましても併せて状況ご連絡頂けますと幸いです。

お手数おかけし申し訳ありません。

ご確認の程よろしくお願い致します。

/eom

From:
北山優哉 Yuya Kitayama

Sent: Friday, January 31, 2025 9:41 AM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

状況をお伺いしたく存じます。

下記でご連絡いただいておりましたが測定は開始出来ておりますでしょうか。

最後まで行ければ、DUTの制御ができるということになりますので、それから測定が可能になると思います。

なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 5:25 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご対応、ご連絡ありがとうございました。

アップデートいただいたツールのバージョンに関してBT試験に関係ありそうな箇所は、

想定通りでしたので問題ありません。

QRCTで”HCI DUT Mode”が正常に実行できたところのスクリーンショットも添付いたします。

確認しました。無事動作したとのことで安心しました。

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、DUTの制御ができるということになりますので、それから測定が可能になると思います。

承知しました。引き続きご対応よろしくお願いいたします。

上記よりサンプルの回収は一旦なしにいたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 5:15 PM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

Qualcomm Package Managerで、”Updates available”にあったツールをすべてアップデートしました。

現在、こちらのPCにインストールされているツールバージョンのスクリーンショットを添付します。

(QPM_Installed_1.jpg, QPM_Installed_2.jpg)

なお、インストールされているツールが、御社から送られてきたスクリーンショットよりも多いですが、

これは昨年、こちらからもQualcommに直接問い合わせをして、インストールを指示されたためです。

(“Qualcomm Software Center”もQualcommの指示で入れたもので、これも今回アップデートしようとしたのですが、

全然進まなかったので、これだけアップデートできていません。)

QRCTで”HCI DUT Mode”が正常に実行できたところのスクリーンショットも添付いたします。(QRCT_HCI_DUT_Mode.jpg)

今までは手順書の途中で進めない状態だったので、これからその先を実行していき、最後まで行ければ、DUTの制御ができるということになりますので、それから測定が可能になると思います。

なお、明日ですが、エンジニアが不在となりますので、この後できる部分まで進め、終わらない場合は続きは明後日に実施いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:13 PM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

HCI DUT Modeが成功した各ツールバージョンのスクリーンショットを添付しますので、

参考になさってください。

以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Tuesday, January 28, 2025 3:04 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ログの取得、動作確認ありがとうございます。

ftmdaemon -ndd　→ QRCTにてHCI Reset、HCI DUT Modeクリック時のログが明らかに差異があるため、ツールの動作もしくは実機の反応に違いがあると考えます。

HCI DUT Modeクリック時のログが数回出ていましたので、

繰り返しでも接続できなかったと判断しました。

なお本日同事象を発生させることが出来ましたので、

サンプル返却までに以下の★を試していただけますでしょうか。

これで解消しない場合はサンプルの返却をお願いいたします。

・ツールの動作の原因として考えられること

→QRCT、関連ツールのバージョンが最新ではない (バージョン差によるツール同士の互換性含む)

添付のpngを参考にQPMの「Updates Available」タブを開いていただき、

「Qualcomm USB Drivers Products」、Qualcomm&reg; Development Acceleration Resource Toolkit (QDART)」配下のアップデート可能なツールを最新にアップデートをお願いいたします。★

このリストに表示されるツールが最新ではないツールになります。

なお、Qualcomm USB Drivers Productsが古い状態で、QRCTを最新にすると同事象が発生することを確認しております。

→ライセンスグループの差異

→送付いただいたキャプチャのツールのバージョンは同じですが、ライセンスグループ名には差異がありました。

もし上記で解消しない場合、同じ内容であるかはQualcomm しか分かりませんので問い合わせをお願いしたく存じます。

・実機の反応の違いとして考えられることハード面で差異があるかもしれませんので回収し確認いたします。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Tuesday, January 28, 2025 11:53 AM

To: 北山優哉 Yuya Kitayama ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

入れ違いで申し訳ございません。

先ほど確認結果をお送りいたしましたのでご確認ください。

ご確認の結果、必要でしたらサンプルをお返しいたしますのでお知らせください。

なお、大変恐縮ですが、本日体調不良のため在宅となっております。

サンプルお返しには少々お時間をいただく場合がございますのでご了承ください。

どうぞよろしくお願い致します。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Tuesday, January 28, 2025 11:44 AM

To: Toshitaka Mochizuki ;
Makoto Chida ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

昨日の今日で申し訳ございませんが、ご連絡した方法で改善していますでしょうか。

もし改善しないようであれば、問題の切り分けを行うため、

一度実機2台を弊社に送り返していただくことは可能でしょうか。

送り先は以下でお願いいたします。

〒[ID]

栃木県宇都宮市東宿郷3-1-7

メットライフビル宇都宮ビル8F

アルプスアルパイン(株)

北山宛以上、よろしくお願いいたします。

From:
北山優哉 Yuya Kitayama

Sent: Monday, January 27, 2025 3:08 PM

To: Toshitaka Mochizuki ;
千田誠 Makoto Chida ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

お忙し中ログの取得いただきありがとうございます。

取得いただいたログは確認を進めております。

ところで有識者から聞いた情報をもとに今一度、確認をお願いできないしょうか。

これで解消しない場合は実機の回収、差し替えも視野に入れております。

＝＝＝＝＝＝＝＝＝＝＝＝＝

・下記までは手順書通り

8.1.2. PC setting

4) Execute the following command to start FTM daemon.

gen4_gvm:/ # ftmdaemon -ndd

を入力

↓

・QRCTにてHCI Reset、HCI DUT Modeをクリック

HCI DUT ModeでErrorが出ても HCI DUT Modeを何回かクリックしてみてください。

(クリックのタイミングによってErrorになることもあるようです)

その際のコマンドプロンプトのログを貼り付けて展開してください。

下記イメージでは見切れていますがHCI Reset クリック時はSend Response = 14が表示され、

HCI DUT Modeクリック時はSend Response = 15、Send Response = 17　のログが表示されるはずです。

＝＝＝＝＝＝＝＝＝＝＝＝＝

Bluetooth and ANT QRCT Module　をリフレッシュする。

QPMでQRCT→Bluetooth and ANT QRCT Moduleを検索し、

最新のv4.[ID]2をRefreshインストールを実行する

＝＝＝＝＝＝＝＝＝＝＝＝＝

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Monday, January 27, 2025 12:14 PM

To: 千田誠 Makoto Chida ;
北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン千田様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示いただきました手順を実行し、”logcat.log”ファイルができましたので添付いたします。

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Makoto Chida

Sent: Friday, January 24, 2025 8:15 PM

To: Toshitaka Mochizuki ;
Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件

To.　アリオン株式会社望月様お世話になっております、アルプスアルパイン千田誠です。

ご展開して頂いた“bluetooth_bt_firmware.txt” に出力されております、

gen4_gvm:/ # ls -l /vendor/bt_firmware/image の

BT関連ファイル一覧について、不足ファイルなく弊社想定ファイルと一致していることを先ずはご連絡いたします。

次に本日のTeamsMTGの席でお伝えしておりましたLogcatログ取得について、以下にコマンド手順を記載します。

(Logcatログについて、DUT側Androidシステム上のアプリケーション/システム動作のログメッセージとなります。)

このコマンド手順例) の場合、

Step6.でC:\Users\[ID]\logcat.log というファイル名が作成されおりますので、

このlogcat.logファイルを弊社にご展開の程、宜しくお願い致します。

Step1.

“ftmdaemon -d”を入力するコマンド・プロントとは別に新規コマンド・プロンプトをOpenする

Step2.

新規コマンド・プロンプト上で以下の太字コマンド実行し、Logcatバッファ内容を一旦クリア(消去)する。

C:\Users\[ID]> adb root

C:\Users\[ID]> adb logcat -c

Step3.

以下のコマンドを実行して Logcat出力を”logcat.log”というファイルに保存状態する。

C:\Users\[ID]> adb logcat > logcat.log

Step4.

“ftmdaemon -d”を入力するコマンド・プロントに戻り、

手順書8.1 から QRCT 上で ”HCI DUT Mode”でErrorとなる事象のところまで実行

Step5.

Step3. のコマンド・プロンプトに移り、“Ctrl+C”キー押下によるLogcatログ取得状態を強制終了する。

^C <-“Ctrl+C”キー押下

C:\Users\[ID]>

以上、お手数をおかけしますが本件不具合事象についてのログ取得ご協力の程、宜しくお願い致します。

千田誠

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 5:50 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

先ほどはお打ち合わせありがとうございました。

ご依頼の一覧をお送りいたします。

Lsコマンドの結果は一番下の方をご確認ください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 11:28 AM

To: Yuya Kitayama ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡有難うございます。

ご検討いただきありがとうございます。

本日私の方が午後はミーティングなどのため、

16:30もしく17:00頃からのTeamsミーティングでいかがでしょうか。

当社からは、

中山：

後夷：

酒井（任意）：

王（任意）：

望月：

が参加の予定です。

御社側の参加者様をお知らせいただけましたらミーティング設定いたします。

ログにつきましては確認いたしますのでお待ちください。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Friday, January 24, 2025 11:14 AM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。

アルプスアルパイン北山です。

ご確認ありがとうございます。

BT OFF状態でも”HCI DUT Mode”でError出る旨承知しました。

一度お送りしている実機の動きを確認させていただきたいので、本日午後にWebMTGは可能でしょうか。

(カメラで状況を共有しつつできるとありがたいです)

可能であれば、ご都合の良いお時間を教えていただければと存じます。

(15:00-16:00は外していただけると助かります)

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

ところで、下記を試していただきコマンドプロンプトに表示されるログを送付頂きたいです。

一度、QRCTと実機をDisconnectし、実機を再起動後、手順書の8.1から実行し、[ID]で以下コマンドを実行。

[ID]. Start FTM daemon

4) Execute the following command to start FTM daemon.

gen4_gvm:/ # ftmdaemon -nd

その後、QRCTにてHCI Reset、HCI DUT Mode　を実行した際にコマンドプロンプトに下記のようなログが表示されるはずです。

その画面キャプチャを展開いただきたく存じます。

Errorが表示される時(BT ON時)

問題ない時(BT OFF時)

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Friday, January 24, 2025 10:29 AM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご指示の件確認いたしました。

BTの設定については、今までも”OFF”にしていたつもりでしたが、今回、改めて手順書の8.1から実行し、[ID]3ではBTの設定の”OFF”を確認して進めましたが、

やはり”HCI Reset”は正常に実行できますが、”HCI DUT Mode”では下記のエラーが表示されます。

もし、このまま解決できないようでしたら、可能でしたら来週以降でどなたか当社ご訪問いただき、実機でご確認いただくことなど調整いただくことは可能でしょうか。

ご検討どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Thursday, January 23, 2025 5:41 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

バージョン情報画面の取得ありがとうございました。

こちらで確認したバージョンと一致していること確認できました。

こちらで再現確認をおこなったところ BTの設定がONの場合、

ご連絡いただいた症状になることが確認できました。

手順書8.1.1.3.　Turn off Bluetooth　を実施されていますでしょうか？

下記状態がBluetooth OFFの状態です。

なお、手順書の 8.Bluetooth Test の操作は実機の電源をOFF/ONする度に必ず毎回実施してください。

電源ON時のすべての設定をを覚えているわけではない為です。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Thursday, January 23, 2025 3:45 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

ご指示いただきました画面の画像をお送りいたしますのでご確認いただけますでしょうか。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Wednesday, January 22, 2025 7:04 PM

To: Toshitaka Mochizuki ;
Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社望月様いつもお世話になっております。アルプスアルパイン北山です。

ご確認ありがとうございます。

こちらでも同じバージョンのソフトに書き換え、手順通りに動作確認を行いましたが、

“HCI Reset”も”HCI DUT Mode”もErrorなく実行できております。

現在確認作業はいただきました手順書に従って実行しており、12ページの”[ID]”の”1)”で、USBケーブルを接続すると、

DUTのディスプレイ上に下記のように表示され、DUT側でUSBケーブルを認識していることが確認できます。

(この表示は数秒で消えます。)

“USB Debugging connected”

Tag to turn off USB debugging

こちらはDUT側が接続先のPCを認識しているということになります。

この状態にならなければ、[ID]〜[ID]1の設定はできないはずです。

また、お知らせしたとおり、21ページの”[ID]”の”2)”で、”HCI Reset”は正常に動作していることが確認できます。

”HCI DUT Mode”のみがErrorになるということですよね。

こちらでは同様の事象が発生しておらず、手順書通りに実施していただいているのであれば、対処方法が見つかりません。

Qualcommに念のため、下記方法でバージョン情報の画面キャプチャをいただけますでしょうか。

以上、よろしくお願いいたします。

From: Toshitaka Mochizuki

Sent: Wednesday, January 22, 2025 1:38 PM

To: 北山優哉 Yuya Kitayama ;
Jun Wang ;
金子征史 Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になっております。

アリオン株式会社の望月です。

現在確認作業はいただきました手順書に従って実行しており、12ページの”[ID]”の”1)”で、USBケーブルを接続すると、

DUTのディスプレイ上に下記のように表示され、DUT側でUSBケーブルを認識していることが確認できます。

(この表示は数秒で消えます。)

“USB Debugging connected”

Tag to turn off USB debugging

また、お知らせしたとおり、21ページの”[ID]”の”2)”で、”HCI Reset”は正常に動作していることが確認できます。

他に何か確認するべきところや方法はございますでしょうか。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社　KSTC　営業部　PM　望月俊孝所在地：〒140-0012東京都品川区勝島1-1-1 東京SRC B館4階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Yuya Kitayama

Sent: Monday, January 20, 2025 7:12 PM

To: Jun Wang ;
Masafumi Kaneko

Subject: RE: 【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡、ご確認ありがとうございます。

手順書8.1.2のPC Settingについて、実行していることをラボに確認できました。

ありがとうございます。承知しました。

8.1.2　PC Setting以外、考えられることは何かありませんでしょうか。

8.1. Initial Setting

5)Execute the following command to start
【Normal Running】 mode.

こちらの実施結果は以下のようになっていますでしょうか？

以上、ご確認よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 6:24 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

手順書8.1.2のPC Settingについて、実行していることをラボに確認できました。

“HCI Reset”は正常に実行できていますが、”HCI DUT Mode”でエラーが発生しているようです。

（念のため、8.1.2から再実行してみましたが、”HCI Reset”は正常で、”HCI DUT Mode”でエラーが発生しました。)

8.1.2　PC Setting以外、考えられることは何かありませんでしょうか。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun Wang

送信日時 : 2025 年 1 月 20 日 17:52

宛先 : Yuya Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

早速のご確認ありがとうございます。

ラボにお伝えいたします。

取り急ぎお礼まで。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Yuya Kitayama

送信日時 : 2025 年 1 月 20 日 17:42

宛先 : Jun Wang ;
Masafumi Kaneko

件名 : RE:
【ALAP】 Q 社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

手順書の 8.1.2. PC setting (下記)は実行されていますでしょうか？

こちらを実行しないとHCI ResetやHCI DUT Mode押下時にエラーが出る症状がこちらでも確認出来ております。

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Monday, January 20, 2025 5:26 PM

To: 北山優哉 Yuya Kitayama ;
金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオンの王君です。

標記テストツールの件先週末の続きですが、

現在ラボでは手順書に従って21ページの”2)”までは手順書通りに進められました。

21ページの”3)”で、”HCI DUT Mode”をクリックしたとき、下の図のようになるはずなのですが、

その下に記載したerrorが表示されています。

考えられる原因や対応策等ご教示いただけますと幸いです。

Error　SEND: QLIB_FTM_BT_Enable_Bluetooth()

Error　Failed: QLIB_FTM_BT_Enable_Bluetooth

お手数かけますが、何卒よろしくお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun Wang

送信日時 : 2025 年 1 月 17 日 17:40

宛先 : Yuya Kitayama ;
Masafumi Kaneko

件名 : Re:
【ALAP】 Q 社テストツールインストールの件アルプスアルパイン北山様いつもお世話になります、アリオン王君です。

標記の件早速ご確認いただきありがとうございます。

ソフトウェアは最新版の使用で問題がないこと承知いたしました。

ではQPSTをQUTSに読みかえてこのまま進めさせていただきます。

よろしくお願いいたします。

Outlook
for Android を取得差出人: Yuya Kitayama

送信日時: 金曜日, 1月 17, 2025 5:32:45 午後宛先: Jun Wang ;
Masafumi Kaneko

件名: RE: 【ALAP】Q社テストツールインストールの件アリオン株式会社王君様いつもお世話になっております。

アルプスアルパイン北山です。

ご連絡ありがとうございます。

お問い合わせいただいている件ですが、

動作手順書のツールのバージョンが少し古かったようで、

こちらでも最新版をインストールしたところ Library Modeは“QUTS”だけしか表示されませんでした。

その為、 QPST をQUTSと読み替えて使用してください。

基本的には最新バージョンを使用していただいて問題ありません。

(大幅なUIの変更はないと考えますが、こればかりはQualcomm社次第となりますので、

手順書と乖離する場合があることは許容いただけますと幸いです。)

以上、よろしくお願いいたします。

From: Jun Wang

Sent: Friday, January 17, 2025 5:22 PM

To: 金子征史 Masafumi Kaneko

Subject: Re: 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様アリオンの王君です。五月雨式となり失礼いたしました。

下記確認させていただいておりますLibrary Modeの変更に関して、

ソフトウェアバージョンとは関係ありますでしょうか。

弊社ラボではQualcommのソフトウェアは最新版をインストールしています。

手順書では、インストールの画面でソフトウェアのバージョンが見えていまして、

どうも古いバージョンのようです。

弊社でのインストールでは特定バージョンでのダウンロードが必要な場合、

ご連絡いただけますと幸いです。

ご確認いただきますようお願いいたします。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

差出人 : Jun Wang

送信日時 : 2025 年 1 月 17 日 16:50

宛先 : Masafumi Kaneko

件名 : 【ALAP】 Q 社テストツールインストールの件アルプスアルパイン金子様大平様いつもお世話になります、アリオンの王君です。

標記の件、いただきました動作手順書に従ってテストツールのインストールして、

進めている中、問題が発生しており、ご確認をお願いしてもよろしいでしょうか。

インストール手順：

Sub ContractorとしてAcceptする。

Package Manager 3を起動し、1.で登録したメールアドレスでログインする。

試験の手順書(Radio Law Test / BluetoothSIG Qualification Test Operation Manual (Android14))

の11ページに記載されている手順でインストールする。

その後、手順書を続けて実行してみたところ、17ページの2)のところで(下記参照)、Targetに”APQ”に変更できましたが、

Library Modeは“QUTS”だけしか表示されず、”QPST”への変更はできませんでした。

お忙しいところ恐縮ですが、ご確認いただけますと幸いです。

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)

アリオン株式会社営業統括部営業王君（ワン・ジュン）

(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)(*^_^*)
