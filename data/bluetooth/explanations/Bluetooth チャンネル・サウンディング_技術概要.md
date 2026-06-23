[目次][]

- 1.はじめに
- 2.背景
- [2.1 デバイスの位置決めとBluetooth
LE](#21-device-positioning-and-bluetooth-le)
- [2.1.1ブルートゥース®
ファインド・ミー](#211-bluetooth-find-me)
- [2.1.2
ビーコンと第一世代の距離推定](#212-beacons-and-firstgeneration-distance-estimation)
- [2.1.3ブルートゥース® 方向検知 とAoA
そしてAoD](#213-bluetooth-direction-finding-with-aoa-and-aod)
- [2.1.4ブルートゥース® Channel
Sounding](#214-bluetooth-channel-sounding)
- [2.2ブルートゥース® Channel
Sounding入門](#22-an-introduction-to-bluetooth-channel-sounding)
- [2.2.1
電波の基本的性質](#221-the-fundamental-properties-of-radio-waves)
- [2.2.1.1
振幅と波の周期](#2211-amplitude-and-wave-cycles)
- 2.2.1.2 波長
- 2.2.1.3 周波数
- 2.2.1.4 段階
- [2.2.1.5
周波数と波長の数学的関係](#2215-the-mathematical-relationship-between-frequency-and-wavelength)
- [2.2.2
距離測定方法](#222-distance-measurement-methods)
- [2.2.2.1位相ベース測距
PBR](#2221-phasebased-ranging-pbr)
- 2.2.2.1.1 理論編
- [2.2.2.1.2
動作例](#22212-worked-example)
- [2.2.2.2
往復タイミングRTT](#2222-roundtrip-timing-rtt)
- 2.2.2.2.1 理論編
- [2.2.2.3
現実世界の課題](#2223-realworld-challenges)
- [3.ブルートゥース®Channel
Sounding](#3-bluetooth-channel-sounding)
- 3.1 概要
- 3.2 アーキテクチャ
- [3.2.1
デバイスの役割](#321-device-roles)
- 3.2.2 トポロジー
- [3.2.3
アンテナ・アレイ](#323-antenna-arrays)
- 3.2.4 用途
- [3.2.5
データ・トランスポート・アーキテクチャ](#325-data-transport-architecture)
- [3.2.6Bluetooth LE スタックにおけるChannel
Sounding](#326-channel-sounding-in-the-bluetooth-le-stack)
- [3.3ブルートゥース® Channel Sounding
制御手順](#33-bluetooth-channel-sounding-control-procedures)
- [3.3.1ブルートゥース® Channel Sounding
セキュリティスタート](#331-bluetooth-channel-sounding-security-start)
- [3.3.2ブルートゥース® Channel Sounding
機能交換](#332-bluetooth-channel-sounding-capabilities-exchange)
- [3.3.3ブルートゥース® Channel Sounding
設定](#333-bluetooth-channel-sounding-configuration)
- [3.3.4 Mode-0 FAE
テーブル・リクエスト](#334-mode0-fae-table-request)
- [3.3.5ブルートゥース® Channel
Sounding](#335-bluetooth-channel-sounding-start)
- [3.3.6ブルートゥース® Channel
Sounding](#336-bluetooth-channel-sounding)
- [3.4
イベント、サブイベント、ステップ](#34-events-subevents-and-steps)
- [3.4.1
LE-ACL接続と時分割](#341-leacl-connections-and-time-division)
- [3.4.2
タイムディビジョン](#342-time-division)
- 3.4.2.1 構造
- 3.4.2.2 タイミング
- [3.5ブルートゥース® Channel
Sounding](#35-bluetooth-channel-sounding-steps)
- [3.5.1
ステップについて](#351-about-steps)
- [3.5.2
パケットとトーン](#352-packets-and-tones)
- [3.5.3
ステップ・モード](#353-step-modes)
- 3.5.3.1 モード0
- 3.5.3.2 モード-1
- 3.5.3.3 モード2
- 3.5.3.4 モード-3
- [3.6
位相差の確立](#36-establishing-phase-differences)
- [3.7
アンテナ切り替え](#37-antenna-switching)
- [3.8
モード・シーケンス](#38-mode-sequencing)
- [3.8.1
モード・シーケンスの概要](#381-mode-sequencing-overview)
- [3.8.2
モードの組み合わせ](#382-mode-combinations)
- [3.8.3
モードシーケンス構成とサブモード挿入](#383-mode-sequence-configuration-and-submode-insertion)
- [3.8.4
メイン・モードの繰り返し](#384-main-mode-repetition)
- [3.8.5
アプリケーションとモードシーケンスに関する考察](#385-applications-and-mode-sequencing-considerations)
- [3.9
RFチャンネルとチャンネル選択](#39-rf-channels-and-channel-selection)
- [3.9.1ブルートゥース® Channel
Sounding](#391-the-bluetooth-channel-sounding-channel-map)
- [3.9.2
チャンネル・フィルタリング](#392-channel-filtering)
- [3.9.3
周波数ホッピング](#393-frequency-hopping)
- [3.9.4
チャンネルの選択](#394-channel-selection)
- 3.9.4.1 概要
- [3.9.4.2
チャンネルインデックスシャッフリング](#3942-channel-index-shuffling)
- 3.9.4.3 CSA #3a
- 3.9.4.4 CSA #3b
- 3.9.4.5 CSA #3c
- [3.10RTT
オプションと精度](#310-rtt-options-and-accuracy)
- [3.10.1
アクセスアドレス基づくタイミング](#3101-timing-based-on-an-access-address)
- 3.10.2部分的タイミング推定
- [3.10.3RTT
法の比較](#3103-a-comparison-of-rtt-methods)
- [3.11LE 2M 2BT
PHY](#311-the-le-2m-2bt-phy)
- [3.11.1
変調方式](#3111-modulation-schemes)
- [3.11.2
帯域幅-ビット周期製品](#3112-bandwidthbit-period-product)
- 3.11.3LE 2M 2bt
- [3.12ブルートゥース® Channel Sounding SNR
コントロール](#312-snr-control-for-bluetooth-channel-sounding-steps)
- 3.13 セキュリティ
- 3.13.1 概要
- [3.13.2PBR RTT
クロスチェック](#3132-pbr-and-rtt-cross-checking)
- [3.13.3ブルートゥース® Channel Sounding
初期化](#3133-initializing-bluetooth-channel-sounding-security)
- [3.13.4
決定論的乱数ビット生成器（DRBG）](#3134-deterministic-random-bit-generator-drbg)
- [3.13.4.1
セキュアアクセスアドレス](#31341-secure-access-addresses)
- [3.13.4.2RTT
フラクショナルタイミングのランダムシーケンス](#31342-random-sequence-for-rtt-fractional-timing)
- [3.13.4.3
発音シーケンスマーカー信号](#31343-sounding-sequence-marker-signals)
- [3.13.4.4
トーン拡張スロットランダム送信](#31344-tone-extension-slot-random-transmissions)
- [3.13.4.5
アンテナ経路のランダム選択](#31345-random-selection-of-antenna-paths)
- [3.13.5
サウンディング・シークエンス](#3135-sounding-sequences)
- [3.13.6
攻撃の検知と報告](#3136-attack-detection-and-reporting)
- 3.13.7LE 2M 2bt
- [3.13.8 SNR制御とRTT
セキュリティ](#3138-snr-control-and-rtt-security)
- [3.13.9 CS
セキュリティ・レベル](#3139-cs-security-levels)
- [3.13.10
ベンダー固有の実装と追加セキュリティ](#31310-vendorspecific-implementations-and-additional-security)
- [3.13.11Channel Sounding
基づく攻撃耐性](#31311-channel-sounding-amplitudebased-attack-resilience)
- [3.14Host
アプリケーション](#314-host-applications)
- [3.14.1
距離測定アルゴリズム](#3141-the-distance-measurement-algorithm)
- [3.14.2ブルートゥース® Channel Sounding コントローラ-Host
間通信](#3142-controller-to-host-communication-of-bluetooth-channel-sounding-data)
- [3.14.2.1
HCIイベントタイプ](#31421-hci-event-types)
- [3.14.2.2
HCIイベントのタイミング](#31422-hci-event-timing)
- [3.14.2.3
HCIイベントの内容](#31423-hci-event-content)
- [3.14.3
モードの組み合わせとモードシーケンス](#3143-mode-combinations-and-mode-sequencing)
- 3.14.4アプリケーション
- [3.15
Bluetoothチャネル・サウンディング機能の強化](#315-bluetooth-channel-sounding-enhancements)
- [3.15.1
振幅ベースの攻撃に対する耐性  ](#3151-resilience-against-amplitudebasedattacks)
- [3.15.2
インラインPCT転送のサポート ](#3152inline-pct-transfersupport)
- [3.15.3 PHY固有のRTT
サポート ](#3153-physpecific-rtt-accuracysupport)
- [4.ブルートゥースコア仕様
変更の概要](#4-a-summary-of-bluetooth-core-specification-changes)
- 4.1 アーキテクチャ
- 4.2Host
- [4.2.1
汎用アクセス・プロファイル](#421-generic-access-profile)
- 4.2.2Host
- 4.3 コントローラー
- 4.3.1 物理層
- 4.3.2リンクレイヤー
- [4.3.3ブルートゥース® Channel
Sounding](#433-bluetooth-channel-sounding)
- 5.結論
- 6.参考文献

**バージョン：** 1.0
**改定日** 9 2024年7月
**著者** マーティン・ウーリー、BluetoothSIG

ブルートゥース®・ローエナジー（LE）は、ユーザーにワイヤレスデータ転送
オーディオ機能を提供することで世界的に知られています。このテクノロジーは、よりスマートな携帯電話に搭載されているため、私たちのポケットの中にあります。スマートウォッチやフィットネストラッカーとして手首に装着されている。車の中ではハンズフリーで操作やコミュニケーションができる。そして、Bluetooth
LE Audioの新しい機能である[オーラキャスト®

しかし長年にわたり、Bluetooth
LEを利用すれば、近傍にある他のデバイスの存在を検知・報告したり、デバイス間の距離を推定したり、他のデバイスの位置方向を算出したりすることが可能です。こうしたデバイスの位置特定機能は、デジタルキーや資産追跡、
*紛失防止*、および屋内ナビゲーションなど、幅広いアプリケーションの実現に活用されています。

ブルートゥース・テクノロジーは、25年の歴史の中で絶えず改良を続けてきました。積極的な進化の道を歩んできたことで、Bluetoothは目覚ましい新機能を次々と生み出し、製品にもたらす成果も向上してきました。

Bluetoothコア仕様の更新により、機能 Bluetooth® Channel Sounding機能
追加されました。この機能は、2つのBluetoothデバイス間で安全な高精度測距を可能にするものであり、本稿の主題となっています。なお、本稿はBluetoothコア仕様に代わるものではなく、またその代替となるものでもありません。

Bluetooth LE は 2010
年に初めて仕様化された。この時点から、位置情報サービス技術としてのBluetooth
LE の進化における多くの重要な出来事を特定することができる。

Bluetooth LE
ブルートゥースコア仕様初めて含まれたのと同じ年に、位置情報に関連する最初の正式なBluetooth
LE プロファイル仕様が発表された。これがFind Meプロファイルである。

「Find Me
Profile」は、個人所有物の捜索に関する標準的なアプローチを定義したもので、別名
*紛失防止*とも呼ばれます。1台のデバイスが「Find
Meロケーター」の役割を担います。これは通常、スマートフォンです。ユーザーが紛失しがちな他のデバイス（Bluetoothキーホルダー付きの鍵などが代表的です）は、「Find
Meロケーター」とペアリングされ、それぞれ「Find
Meターゲット」の役割を担います。

ターゲットデバイスはGATTを実装している^1^
「即時アラートサービス」と呼ばれるGATTサービスを実装しています。

紛失したデバイスを探す手助けが必要な場合、ユーザーはスマートフォンでアプリケーション
実行する。アプリケーション
、紛失したデバイスからブロードキャストされる広告パケットをスキャンすることで、デバイス発見手順を実行する。ターゲットデバイスを発見すると、ロケータはそのデバイスに接続する。アプリケーションユーザーインターフェース（UI）は、接続が完了したことを示す。ユーザーは通常、UI上のボタンを押す。これにより、アプリケーション
即時アラートサービスに属するアラートレベル特徴
書き込まれる。ターゲットデバイスは、何らかの適切な方法でアラートレベル値の変化に応答し、おそらく大きなビープ音を発したり、LEDを点滅させたり、あるいはその両方を行ったりします。この時点でユーザーは、鍵がずっと上着のポケットに入っていたことに気づくか、ソファの背もたれに落ちていたことに気づくか、あるいは予測しにくい場所にあることに気づく。いずれにせよ、ブルートゥース技術がその日とユーザーを救い、紛失物は再会する。

ブルートゥース® Find Me は存在アプリケーション一例である。Bluetooth LE
、紛失したデバイスが近くにあることを判断するために使用されるが、Locatorからの方向や距離の表示は提供しない。

ブルートゥース・ビーコンは、Bluetooth
LE広告機能を活用している。アドバタイジングは、範囲内のデバイスがスキャンすることで受信できる小さなデータパケットをブロードキャストすることです。

2013年、アップルはiBeaconフォーマットの仕様を発表した。これは、ビーコン・デバイスがブロードキャストするペイロードの内容として一般的なフォーマットとなった。iBeaconメッセージのデータにはTX
Powerと呼ばれるフィールドがあり、ビーコンから1メートルの距離で測定した場合に予想される信号強度を表す値が含まれている。iBeaconメッセージやGoogleのEddystoneのような他の同等のビーコン・データ・フォーマットにおけるTX
Powerフィールドの存在は、Bluetooth LE
距離推定の第一世代の到来を告げるものでした。

このブルートゥース距離推定の初期バージョンは、2つのデータ値といくつかの簡単な物理学を使用し、次のように動作する：

- ビーコン・メッセージのTXパワー・フィールドは、1メートルのような既知の距離における基準パワー・レベルを提供する。
- 各受信ビーコン・メッセージに関連付けられた受信信号強度インジケータ（RSSI）は、受信デバイスにおける信号強度を定量化する。
- 物理学では、トランスミッター
離れるほど信号強度が低下する割合が理論的に定義されている。具体的には、レシーバー
信号強度はトランスミッター距離の二乗に反比例する。
- トランスミッター
遠ざかるにつれて、測定された信号強度が低下することをパスロスまたは減衰と呼ぶ。iBeacon送信の場合、パスロス＝TXパワー-RSSI。
- このように、一定距離での基準電力レベル、受信したビーコン送信の測定RSSI、距離とパスロスの逆2乗関係、減衰を知ることで、ビーコンとレシーバー間の距離を推定することができる。

[{.aligncenter
.wp-image-234481 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1.png 758w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-600x331.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-300x165.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-450x248.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1-660x364.png 660w"
sizes="auto, (max-width: 758px) 100vw, 758px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_1.png)

*図1 - 経路損失と距離*

このように距離を推定できることは非常に画期的なことで、ビーコンは小売店、旅行、博物館など、あらゆる用途で普及した。

ビーコンはいくつかの要件には非常に適していたが、RSSIとパスロスに基づく距離測定は、他のアプリケーションには十分な精度を備えていない。また、トランスミッター
方向が分からないことも、近さだけでなく位置情報が必要な場合の制約となる。さらに、iBeaconのような様々な独自のビーコン・タイプには、明示的なセキュリティ保護機能が組み込まれていない。

2019年、ブルートゥースコア仕様
バージョン5.1には、主要な機能であるブルートゥース方向検知機能が搭載された。

Bluetooth の方向検知 機能 、Bluetooth LE
コントローラーによる位相測定を使用して、受信信号の方向
をアプリケーションで正確に計算することを可能にします。2つの方法が定義されています。

AoA of
ArrivalAoA方式では、受信装置はアンテナアレイを持ち、異なるアンテナで測定された受信信号は、送信装置の単一アンテナに対する各アンテナの距離がわずかに異なるため、位相差が生じる。

AoD of
Departure）方式では、送信装置はアンテナアレイを持つ。受信デバイスは1つのアンテナを持つが、遠隔の送信デバイスのアンテナアレイの詳細を持っている。このため、受信装置は、その単一のアンテナで行われた位相測定から同様の計算を行うことができます。

[{.aligncenter
.wp-image-234482 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2.png 1440w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-600x300.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-300x150.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-768x384.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-450x225.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-660x330.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-800x400.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-1000x500.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2-1200x600.png 1200w"
sizes="auto, (max-width: 1440px) 100vw, 1440px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_2.png)

*図2 --方向検知 使用してAoA そしてAoD*

同相および直交（IQ）サンプル形式の位相測定値は、Bluetoothコントローラからアプリケーション渡されます。IQサンプルは位相と振幅の値の組で構成され、アプリケーション
これを使用してトランスミッター
見つけることができる方向を計算することができます。

[{.aligncenter
.wp-image-234483 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3.png 2320w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-600x600.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-2000x2000.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-300x300.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-768x768.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1536x1536.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-2048x2048.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-200x200.png 200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-450x450.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-660x660.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-800x800.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1000x1000.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1200x1200.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-1600x1600.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3-50x50.png 50w"
sizes="auto, (max-width: 2320px) 100vw, 2320px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_3.png)

*図3 - IQサンプル*

新しいBluetooth® Channel機能
、RSSIと伝送損失を用いた第一世代の手法では到底実現できなかった精度で、2つのBluetoothデバイス間の距離を算出できる製品の開発が可能機能
。この機能は全く異なる仕組みで動作し、様々なリスクを軽減するための多様なセキュリティ対策が組み込まれています。

ブルートゥース® Channel Sounding 、紛失防止
ソリューション、デジタルキー製品、その他多くのブルートゥース接続機器に恩恵をもたらすと期待されている。

Bluetooth LE のブルートゥース® Channel Sounding 説明する前に、このセ
クションではまず、機能基本的な理論を説明します。ブルートゥース® Channel
Sounding既にご存知の方は、セクション 3「ブルートゥース® Channel
Sounding」へお進みください。

ラジオは電磁波の一種であり、物理学者はしばしばそれを波という言葉で表現する。電波には様々な基本的性質があり、それを理解することが重要である。

電波の振幅は、その電波が伝えるエネルギーに対応し、より一般的な用語では信号強度に対応する。振幅は、ある基準値の上下で振動する。この上下振動は、規則的かつ周期的に繰り返される。ピーク振幅まで上昇し、谷まで下降し、再び開始基準値まで上昇する1回の遷移を波周期と呼びます。図4は、2つの完全な波のサイクルを示しており、振幅は縦軸の目盛りで示されている。最初の波のサイクルの範囲が強調されている。

[{.aligncenter
.wp-image-234484 .size-1200w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4-1600x556.png 1600w"
sizes="auto, (max-width: 1200px) 100vw, 1200px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_4.png)

*図4 - 振幅を縦軸にとった波の周期*

波の周期には物理的な長さがある。波長は周波数に関係し、ブルートゥース・テクノロジーの場合、約12.0cmから約12.5cmの間である。

[{.aligncenter
.wp-image-234485 .size-1200w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5-1600x556.png 1600w"
sizes="auto, (max-width: 1200px) 100vw, 1200px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_5.png)

*図5 - 波長*

電波は真空中で光速で進む^2^。1秒間に空間内の固定された一点を通過する波の完全な周期の数を周波数と呼ぶ。周波数はヘルツ（Hz）で表され、1
Hzは1秒間に1回の波の周期に相当する。Bluetooth信号は、ギガヘルツ（GHz）単位で測定される、はるかに高い周波数で動作する。

[{.aligncenter
.wp-image-234438 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6-1600x556.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_6.png)

*図6 - 周波数*

1つの波周期内のどこかに位置する点は、位相として知られる角度測定値で表されます。位相値の範囲は0～360度、または0～2πラジアンです。図7は、波周期上の適切なポイントにマークされた多数の位相値（ラジアン表示）による位相の概念を示しています。

[{.aligncenter
.wp-image-234439 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7-1600x556.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_7.png)

*図7 - フェーズ*

周波数（f）と波長（λ）は互いに反比例の関係にある。波長が短いほど周波数は高くなり、逆もまた然りである。さらに、これら2つの変数と光速（c）の関係は、一連の簡単な公式によって定義されており、他の2つの既知の値から3つの量のいずれかを計算することができる。光速は299792458m/sの定数である。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">数式</th>
<th class="has-text-align-left" data-align="left">使用</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left"><img
src="https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_1.svg"
height="100" alt="2405 水路測量計算式 1" /></td>
<td class="has-text-align-left"
data-align="left">既知の周波数と光の定数から、未知の波長を求めなさい。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left"><img
src="https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_2.svg"
height="100" alt="2405 水路測量計算式 2" /></td>
<td class="has-text-align-left"
data-align="left">既知の波長と光速から、未知の周波数を求めなさい。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left"><img
src="https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_3.svg"
height="216" alt="2405 水路測量式集 3" /></td>
<td class="has-text-align-left"
data-align="left">周波数の値とそれに対応する波長を用いて、光速を計算してください。</td>
</tr>
</tbody>
</table>

*表1 - 周波数と波長の公式*

無線距離測定技術で最もよく使われる2つの方法は、位相ベース測距
PBR）とラウンドトリップタイミングRTT）である。このセクションでは、両手法の背景にある理論について概説する。

トランスミッター
レシーバー信号が伸びるのに必要な波のサイクル数という観点から、信号の波長の関数として距離を視覚化するのは簡単だ。

[{.aligncenter
.wp-image-234440 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1000x348.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-600x209.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-2000x695.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-768x267.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1536x534.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-2048x712.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-800x278.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1200x417.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_8-1600x556.png 1600w"

*図8 - 波長と波の周期からの距離*

図8では、図の左側で送信された信号が、レシーバー10.5波長離れた位置にあることがはっきりとわかります。信号の周波数がわかれば、波長もわかります。また、波長がわかれば、波の周期数から、掛け算を用いて2つの装置間の距離を求めることができます。

例えば、送信周波数が2402 MHzの場合、波長は12.48095162
cmとなります。この値は、光速を周波数で割ることで求められました。

しかし、送信装置は、自分のアンテナとレシーバーアンテナの間の波のサイクル数を知る方法がない。そこでPBR
法では、トランスミッター レシーバー
間の距離を他のデータから推測する技術を用いる。その方法はこうだ。

ここでは、距離測定を計算したいデバイスをデバイスA、もう一方のデバイスをデバイスBと呼ぶことにする。

1. デバイスAは、既知の周波数f1で信号を送信する。この信号の初期位相はデバイスAにとって既知であり、説明のために、この信号がゼロラジアンの位相で送信されると仮定しよう。
2. デバイスBは、そのアンテナでf1信号を受信し、その位相（ここでは受信位相と呼ぶ）を記録する。
3. 次に、デバイスBは、同じ周波数f1で送信し、この送信の初期位相がデバイスAから受信した信号の受信位相と完全に同じであることを保証することによって、受信した信号をデバイスAにエコーバックします。
4. デバイスAは、デバイスBから到着した信号の受信位相を測定する。

[{.aligncenter
.wp-image-234441 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9.png)

*図9 - 周波数f1による双方向測距*

次にデバイスAは新しい周波数f2を選択し、4つのステップが繰り返されます。この4ステップの2回目の実行結果は、デバイスBから受信した信号のデバイスAによる新しい位相測定で、これをPf2と呼ぶことにします。

[{.aligncenter
.wp-image-234442 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10.png)

*図10 - 周波数f2による双方向測距*

装置Aはここで、f1とf2のそれぞれについて測定された位相値の差を計算する、すなわちPf2-Pf1を計算する。この位相差と周波数f1とf2の差を用いて、以下の式で距離を計算することができます：

![2405Channel Sounding 公式
4](https://www.bluetooth.com/wp-content/uploads/2024/05/2405_Channel_Sounding_Formulas_4.svg){.aligncenter
.size-full .wp-image-208116 loading="lazy" decoding="async" width="937"

ここで、c は光速、(Pf2 -- Pf1) は位相差、(f2 -- f1)
は周波数差、*r*は2つのデバイス間の往復距離である。

2番目のデバイスが信号を発信デバイスに送り返し、そのデバイスが位相測定を行えるようにするこのアプローチは、双方向レンジングと呼ばれる。

現実の世界では、この基本理論の説明には反映されないような課題が生じることもある。このセクションの後半で、そのような課題に遭遇することになる。

簡単な例で、この式を実際に見てみよう。ここでは、2つのデバイス間の距離をすでに知っているという、かなり人為的なケースを使用し、式がどのように正しく同じ結果を導き出すかを見てみましょう。

図11は、互いに正確に1.248095162メートル離れている2つのデバイス、デバイスAとデバイスBを示している。デバイスAは、周波数2.402
MHz、波長12.48095162
cmの信号を送信した。実に驚くべき偶然だが、この2つのデバイスは、互いにこの波長のちょうど10倍の距離にあることになる。

[{.aligncenter
.wp-image-234441 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_9.png)

*図11 - f1波の周期がちょうど10回離れているデバイス*

デバイスAはこの信号を初期位相ゼロで送信し、デバイスBは波長の正確な倍数離れているので、デバイスBでの受信位相もゼロである。図に示すように、デバイスBはデバイスAに信号を送り返し、初期位相を元々受信した信号と同じ受信位相の値に設定することで、実質的に継続が可能になります。

図12は、デバイスAが周波数f2で送信した2番目の信号を示している。今回選択された周波数はf1よりも高く、f2
= 2.432 MHzである。デバイスAにおける初期位相は、今回もゼロである。

[{.aligncenter
.wp-image-234442 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1000x157.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-600x94.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2000x314.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-300x47.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-768x120.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1536x241.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-2048x321.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-450x71.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-660x103.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-800x125.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1200x188.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10-1600x251.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_10.png)

*図12-10回強のf2波のサイクルを隔てたデバイス*

f2の方が周波数が高いため、f1の波長よりもf2の波長の方が短い。この結果、デバイスBでの受信位相はゼロではなくなる。実際には0.784744210ラジアンである。信号が同じ初期位相で機器Bによって再送され、機器Aによって受信される頃には、その位相は1.56948842ラジアンになっている。

周波数差は30MHz、位相差は1.56948842である。これらの値をrの式に代入すると、計算された距離は小数点以下2桁までで2.49メートルとなる。しかし、これはデバイスAからデバイスBへの往復分であるため、2つのデバイス間の実際の距離はこの数値の半分、すなわち1.24メートルとなる。これは予想された結果であり、光速と2つの送信信号の既知の位相と周波数の分離に基づくrの公式が、いかに2つの装置間の距離を正確に計算するために使用できるかを示している。

しかし、複雑な点があり、これは位相の公式と（2 \*
π）のモジュール分割にヒントがあります。位相値は距離が長くなるにつれて変化しますが、周期的であるため、位相値が（2
\*
π）ラジアンに達するとゼロにリセットされ、同じ値が繰り返されるようになります。このため、2つのデバイス間の距離を決定する際に、同じ位相差の値によって複数の距離が暗示される可能性があるため、あいまいさが生じることがあります。これは距離の曖昧性として知られています。

距離の曖昧性がいつ発生するかは、周波数間隔によって異なります。一般に、周波数差が大きいほど、距離の曖昧性はより早く発生します。幸いなことに、この問題は、PBR
第2の距離測定手法である往復時間測定（Round-Trip Timing）PBR
使用することで解決できます。

ラウンドトリップ・タイミングを使って2つのデバイス間の距離を計算する理屈はとても簡単だ。無線（RF）通信は、既知の定数である光速で移動する。つまり、2つのデバイス間を伝送するのにかかる時間を計算できれば、距離を計算することができる。あとは往復時間
時間に光速をかけるだけである。

例えば、RF信号がデバイスAからデバイスBへ、そしてデバイスAへ戻るのに20ナノ秒かかるとすると、単純に光速に20ナノ秒を掛けると、双方向の合計距離は6メートル弱となり、2つのデバイス間の距離は3メートル弱となる。

*双方向距離 2r = c \* 0.00000002*

ここで、cは光速（299792458m/s）、0.00000002は秒単位の双方向飛行時間（ToF）である。この結果、次のようになる：

*2r = 299792458 × 0.00000002\
= 5.99584916*

従って、デバイスAとデバイスBの間の距離は

*2.99792458 メートル*

しかし、この基本公式は正しいが、ブルートゥース・デバイスの文脈でこれを使うのは少し複雑であり、これまで紹介した理論は不完全である。

RF信号を策定して送信する行為には、往復応答を受信、処理、送信する行為と同様に時間がかかる。電波が1マイクロ秒で300メートル弱移動できることを考慮すると、この一見短い時間は、距離測定の文脈では非常に重要な意味を持つ可能性がある。

[![2405Channel Sounding
図13](https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13.png "Figure 13"){.aligncenter
.wp-image-218307 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-600x176.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-300x88.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-768x225.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1536x451.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-450x132.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-660x194.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-800x235.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1000x294.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1200x352.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13-1600x470.png 1600w"
sizes="auto, (max-width: 2000px) 100vw, 2000px"}](https://www.bluetooth.com/wp-content/uploads/2024/07/2405_Channel_Sounding_Figure_13.png)

*図13 -RTT 内訳（縮尺なし - 信号の内容は代表的なものではない）*

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left"
data-align="left">インスタント・イン・タイム</th>
<th class="has-text-align-left" data-align="left">説明</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left"
data-align="left"><strong><sub>ToDA</sub></strong></td>
<td class="has-text-align-left"
data-align="left">デバイスAからの送信時刻。これは、デバイスAが信号を無線で送信した時刻である。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left"><strong><sub>ToAB</sub></strong></td>
<td class="has-text-align-left"
data-align="left">デバイスBへの到着時刻。これは、信号がデバイスBのアンテナに到達した時刻です。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left"><strong><sub>ToDB</sub></strong></td>
<td class="has-text-align-left"
data-align="left">デバイスBからの送信時刻。これは、デバイスBが無線で送信を行った時刻です。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left"><strong><sub>ToAA</sub></strong></td>
<td class="has-text-align-left"
data-align="left">デバイスAへの到着時刻。これは、デバイスBからの信号がデバイスAのアンテナで受信された時刻である。</td>
</tr>
</tbody>
</table>

緑色の点線は、2つの信号のいずれも*電波として*送信されていない経過時間を表しています。

往復時間
RTT）は、図13に示された時刻の時点を用いて、次のように表すことができる：

*RTT 2 \* ToF = (~ToAA~--~ToDA~) -- (~ToDB~--~ToAB~)*

デバイスRTT計算するには、デバイスBでの処理所要時間（~すなわちToDB~---~ToAB~）を知る必要があります。理論上、これを実現する方法はいくつか考えられます。
実際には、最も簡単な解決策は、デバイスAとデバイスBが事前に固定の処理所要時間を合意しておくことです。デバイスBは、その処理所要時間が満了するまさにその瞬間に、処理を完了し、応答を送信することを保証しなければなりません。その後、デバイスAは、その事前に合意された値を（~ToDB~---~ToAB~）として使用します。

距離測定のPBR RTT
両手法について提示された理論は、このトピックに対する最初の洞察を得るには十分であり、純粋に理論的な文脈においては、それは完全なものである。しかし、現実の世界では、正確な距離測定はより複雑である。実世界で使用される実デバイスで満足のいく結果を出すには、いくつかの課題に対処しなければならない。

ワイヤレス距離測定技術がアドレス
すべき課題の種類には、次のようなものがある：

- 無線信号のマルチパス伝搬から生じる複雑さ
- 発生する信号の周波数の精度と安定性
- 内部時計の安定性、タイムスタンプの精度と分解能
- 位相ベース測距距離の曖昧さ
- セキュリティ

本稿の残りの部分では、Bluetooth技術における高精度距離測定について学び、このような現実世界の問題に直面したときに、この技術がどのように効果的に機能するように設計されているかを理解する。

ブルートゥース®Channel Sounding
、従来よりもはるかに高精度の距離測定が可能です。測定の精度は、環境条件や、ブルートゥース®
Channel Sounding アプリケーション
層がどのように利用するかによって決まります。また、ブルートゥースコア仕様
範囲外ではありますが、計算に使用する生データの品質を向上させることができる実装の選択にも依存します。

ブルートゥース®Channel Sounding
、様々な構成が可能な距離測定のための柔軟なツールキットをアプリケーションに提供します。この仕様では、位相ベース測距
PBR）とラウンドトリップタイミングRTT）の両方の距離測定法がサポートされています。ほとんどの場合、PBR
主要かつ最も正確な距離測定方法として使用され、RTT
それと並行して追加のセキュリティを提供するために使用されることが予想されます。

ブルートゥース® Channel
Sounding使用されているPBR、距離のあいまいさが生じる前に約150メートルまでの距離を測定することができます。PBR
RTT
使用することで、アプリケーションは距離のあいまいさを識別し、取り除くことができるため、より長い距離を測定することができる。

アプリケーションは、精度、セキュリティ、レイテンシ、消費電力などの問題に対して、さまざまなレベルの優先順位を置くことができます。ブルートゥース®
Channel Sounding 機能
設定可能性により、アプリケーションはシステムの主要な機能や動作の多くを制御したり、影響を与えたりすることができます。

このセクションでは、ブルートゥース® Channel Sounding 機能
、それが依存するBluetoothスタックのコア機能を検証します。

ブルートゥース® Channel Sounding 機能
、2つのデバイスの役割が定義されている。1つ目はイニシエータ、2つ目はリフレクタです。

イニシエータ
、自分から他の装置までの距離を計算したい装置である。もう一方の装置はリフレクタである。

イニシエータ またはリフレクタ いずれかが、ブルートゥース® Channel
Sounding 手順を開始することができる。

[{.aligncenter
.wp-image-234444 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14.png 7566w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-600x115.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-2000x383.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-300x57.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-768x147.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1536x294.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-2048x392.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-450x86.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-660x126.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-800x153.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1000x192.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1200x230.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14-1600x307.png 1600w"
sizes="auto, (max-width: 7566px) 100vw, 7566px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_14.png)

*図14 - 役割*

ブルートゥース®Channel Sounding 、1対1のトポロジーで行われ、イニシエータ
役割を持つ1つのデバイスとリフレクタ
役割を持つ1つのデバイスの間で通信が行われ ます。

ブルートゥース® イニシエータ 役割は、リンクレイヤー LE
セントラルの役割を果たすデバイス又は LE
ペリフェラルの役割を果たすデバイスのいずれかが担うことができることに留意されたい。同じことがブルートゥース®
リフレクタ 役割にも適用される。

ブルートゥース® Channel Sounding
使用する機器には、アンテナアレイが含まれることがあります。これにより、位相ベース測距
使用されるブルートゥース® Channel Sounding
伝送の一連の代替経路が提供され、マルチパス伝搬の影響を軽減することで距離測定の精度を向上させることができます。

ブルートゥース®Channel Sounding 、Bluetooth
コントローラが提供するデータを使用して、アプリケーション
距離を計算する必要があります。このデータは、ブルートゥース® Channel
Sounding
手順の実行中にコントローラによって取得され、各デバイスで行われた信号交換と低レベル測定の結果です。データはHCIイベントでアプリケーション
層に渡されます。

またアプリケーション 、Bluetooth
コントローラーにコンフィギュレーションの選択肢や設定を提供する役割も担っており、この選択肢や設定は、2つのデバイス上のアプリケーションでサポートされ、アプリケーションに適したブルートゥース®
Channel Sounding 確立に使用されます。

台のデバイスがイニシエータ 、もう1台がリフレクタ
役割を持つシステムに参加するためには、両方のデバイスがブルートゥース®
Channel Sounding 機能サポートするBluetooth LE
コントローラーを持っている必要があります。

[{.aligncenter
.wp-image-234445 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1000x648.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-600x389.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-2000x1295.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-300x194.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-768x497.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1536x995.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-2048x1326.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-450x291.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-660x427.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-800x518.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1200x777.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New-1600x1036.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_15_New.png)

*図 15 -ブルートゥース® Channel Sounding Bluetooth スタック*

Bluetoothコア仕様書は、Bluetooth技術のアーキテクチャをいくつかの観点から定義している。最初の観点では、汎用的なデータ転送アーキテクチャが定義されている。

ブルートゥースコア仕様定義を参照し、図16の用語を以下に説明する：

- **L2CAPは**、論理リンク制御および適応プロトコル（Logical Link Control
and Adaptation
Protocol）の略称です。L2CAPチャネルとは、単一のアプリケーションまたは上位層プロトコルにサービスを提供する、2つのデバイス間のL2CAPレベルにおける論理的な接続のことです。
- 「**論理リンク**」とは、「Bluetoothシステムのクライアントに対して独立したデータ転送サービスを提供するために使用される、アーキテクチャ上の最下位レベル」である。
- **論理トランスポート**は、送受信ルーチン、フロー制御メカニズム、確認応答プロトコル、リンク識別などの課題を扱います。論理トランスポートには、同期型、非同期型、および等時型があります。
- **物理リンクとは**、リンクレイヤー確立されるデバイス間の接続のことです。リンクレイヤー
はリンクレイヤー プロトコルスタック構成する層リンクレイヤー 。
- **物理チャネルとは**、1つまたは複数の通信機器による無線周波数（RF）搬送波の占有パターンを定義するものである。
- **物理層の伝送方式は**、無線信号を搬送波としてデジタルデータを符号化し伝送するために用いられる、無線パケットの構造や変調方式など、一般的に適用される事項を規定する。

汎用データ転送アーキテクチャは、Bluetooth LE と Bluetooth Basic
Rate/Enhanced Data Rate（BR/EDR）の両方に適用されます。

図 17 にデータ・トランスポート・アーキテクチャのサブセット
示す。青くハイライトされているのは、Channel
Sounding用に定義された新しい物理チャネル・タイプと新しい物理リンク・タイプである。

[{.aligncenter
.wp-image-234447 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17.png 1341w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-600x271.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-300x136.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-768x347.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-450x203.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-660x298.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-800x362.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-1000x452.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17-1200x542.png 1200w"
sizes="auto, (max-width: 1341px) 100vw, 1341px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_17.png)

*図17 - CSとデータ・トランスポート・アーキテクチャ*

論理トランスポート・タイプまたは論理リンク・タイプは、LEChannel Sounding
物理リンクに関連付けられていない。

Bluetooth LE より包括的に定義する方法は、完全なプロトコルスタック
そのレイヤーの観点からである。ブルートゥースコア仕様
大部分は各レイヤーの定義に費やされている。図 18 にBluetooth LE
スタックを示す。

[{.aligncenter
.wp-image-234449 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18.png 654w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18-509x600.png 509w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18-254x300.png 254w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18-450x531.png 450w"
sizes="auto, (max-width: 654px) 100vw, 654px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_18.png)

*図18 -Bluetooth LE スタック*

Bluetooth LE スタックの各層の責務の概要は表 2 に記載されている。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">レイヤー</th>
<th class="has-text-align-left" data-align="left">主な責任</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left"
data-align="left">汎用アクセスプロファイル（GAP）</td>
<td class="has-text-align-left"
data-align="left">状態使用される可能性のある動作モードや手順（接続不要な通信やデバイス検出におけるアドバタイジングの使用方法など）を定義する。また、セキュリティレベルや一部のユーザーインターフェースの標準についても定義する。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">汎用属性プロファイル（GATT）</td>
<td class="has-text-align-left"
data-align="left">属性テーブル内の基礎となる属性に基づいて、「サービス」、「特性」、「記述子」と呼ばれる高レベルなデータ型を定義します。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">アトリビュート・プロトコル（ATT）</td>
<td class="has-text-align-left"
data-align="left">サーバーが保持するデータを、属性テーブルと呼ばれる論理データ構造内で検索および利用するために使用されるプロトコル。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">セキュリティマネージャープロトコル（SMP）</td>
<td class="has-text-align-left"
data-align="left">ペアリングなどのセキュリティ手順の実行時に使用されるプロトコル。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">論理リンク制御および適応プロトコル（L2CAP）</td>
<td class="has-text-align-left"
data-align="left">RF接続を介したデータチャネルの多重化サービス、大規模なSDUの分割および再構成、ならびに強化されたエラー検出および再送信機能を提供します。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">ホスト・コントローラ・インターフェース（HCI）</td>
<td class="has-text-align-left"
data-align="left">ホストコンポーネントとコントローラ間のコマンドおよびデータの双方向通信を行うためのインターフェースを提供します。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">アイソクロナス・アダプテーション・レイヤー（ISOAL）</td>
<td class="has-text-align-left"
data-align="left">アイソクロナスチャネルを使用するデバイスで、異なるフレーム期間を使用できるようにします。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">リンクレイヤー</td>
<td class="has-text-align-left"
data-align="left">無線インターフェースのパケット形式、エラーチェックなどのビットストリーム処理手順、状態
、無線通信プロトコル、およびリンク制御を定義する。また、論理トランスポートと呼ばれる、接続非依存型、接続指向型、および等時性通信のための、基盤となる無線通信装置の利用方法についても、いくつかの異なる方式を定義する。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">物理層</td>
<td class="has-text-align-left"
data-align="left">変調方式、周波数帯域、チャネルの使用、レシーバー
など、無線（RF）の使用に関連するBluetooth技術のあらゆる側面を定義する。物理層パラメータの3つの組み合わせが定義されており、これらはLE
1M、LE 2M、LE 2M PHYと呼ばれる。LE 2M
、Bluetoothコア仕様のバージョン6.0で初めて定義され、Bluetooth®チャネルサウンディングと組み合わせてのみ使用可能です。さらに、LE
Coded別のPHYも定義されています。名称とは異なり、LE Coded LE
1Mと同じ物理層パラメータLE Coded
、リンクレイヤーで前方誤り訂正符号化とパターンマッピングを適用します。</td>
</tr>
</tbody>
</table>

*表 2 -Bluetooth LE スタックの各層の主な責務と機能の概要*

Bluetoothコア仕様の「物理層」、「リンクレイヤー」、「ホストコントローラインターフェース」、および「汎用アクセスプロファイル」の各セクションは、Bluetooth®チャネルサウンディングの導入により影響を受けています。詳細については第4節で説明します。

ブルートゥース® Channel Sounding 開始される前に、リンクレイヤー LE
セントラルの役割を担うデバイスは、リンクレイヤー LE
ペリフェラルの役割を担うデバイスに接続しなければならない。Channel
Sounding準備と開始に関係するいくつかの手順の間、様々なリンクレイヤー
伝送データ・ユニット（PDU）の交換のために安全な伝送を提供できるよう
に、確立された LE-ACL 接続上でセキュリティが開始される。

ブルートゥース® Channel Sounding 準備と開始の主な手順は以下の通り：

1. セキュリティ・スタート
2. 能力交換
3. 構成
4. スタート

これらの手順のすべてが必須というわけではありません。これは、2つのデバイスが以前に情報を交換しており、その情報がキャッシュされているかどうかといった要因によって異なります。手順の例と関連するPDUを図19に示します。

[{.aligncenter
.wp-image-234450 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19.png 462w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19-319x600.png 319w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19-159x300.png 159w"
sizes="auto, (max-width: 924px) 100vw, 924px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_19.png)

*図 19 - CS 開始手順のシーケンス*

ブルートゥース®Channel Sounding 、初期化手順が実行される LE-ACL
接続に関連するも
のとは異なる独自のセキュリティ機能を有する。ブルートゥース® Channel
Sounding 開始手順は、後にブルートゥース® Channel Sounding
機能で使用されるパラメータを、2 つのデバイスが安全に交換す
ることを可能にする。

ブルートゥース® Channel Sounding 開始手順は、LE セントラル・デバイスが 3
つの乱数を生成し、LL_CS_SEC_REQ PDU で LE
周辺デバイスに送信することから始まる。LE
周辺機器は、セントラルの乱数と同じ規則に従った独自の 3
つの乱数を生成し、LL_CS_SEC_RSP PDU でセントラルに送り返す。

各デバイスで生成される乱数には名前が付けられており、表3に説明されている。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">名前</th>
<th class="has-text-align-left" data-align="left">項目</th>
<th class="has-text-align-left" data-align="left">長さ（ビット）</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">CS_IV_C</td>
<td class="has-text-align-left"
data-align="left">中央局によって生成された初期化ベクトル。</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_IN_C</td>
<td class="has-text-align-left" data-align="left">Centralによってノンス
インスタンス化ノンス 。</td>
<td class="has-text-align-left" data-align="left">32</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_PV_C</td>
<td class="has-text-align-left"
data-align="left">セントラルによって生成されたパーソナライゼーションベクトル。</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_IV_P</td>
<td class="has-text-align-left"
data-align="left">周辺機器によって生成された初期化ベクトル。</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_IN_P</td>
<td class="has-text-align-left" data-align="left">周辺機器によってノンス
インスタンス化ノンス 。</td>
<td class="has-text-align-left" data-align="left">32</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">CS_PV_P</td>
<td class="has-text-align-left"
data-align="left">Peripheralによって生成されたパーソナライゼーションベクトル。</td>
<td class="has-text-align-left" data-align="left">64</td>
</tr>
</tbody>
</table>

*表 3 - CS セキュリティ・パラメータ*

両方のデバイスがブルートゥース® Channel Sounding
タの両方のセットを所有している場合、セントラル/ペリフェラルの各ペアの値は、
それぞれのリンク層によって連結されます。この結果、3 つのブルートゥース®
Channel Sounding タ CS_IV、CS_IN、CS_PV
に対して、両方のデバイスが同じ値を持つことになります。

ブルートゥース® Channel Sounding
能力は、2つのデバイスで大きく異なる場合があり、開始前に相互にサポートされるコンフィギュレーションに到達するためには、2つのデバイスがそれぞれ、もう一方のデバイスの能力に関する情報を所有している必要があります。

ケイパビリティの交換は、一方のデバイスがLL_CS_CAPABILITIES_REQ
PDUでその詳細を送信し、他方のデバイスがLL_CS_CAPABILITIES_RSP
PDUでその詳細を応答することによって達成される。デバイスは、以前に受信したケイパビリティデータをキャッシュすることができ、そのため相手デバイスとケイパビリティを交換しないことを選択することができる。しかし、どちらのデバイスがこの手順を開始してもよい。

機能の違いの例としては、PHYのサポート、RTT
、Bluetooth®チャネル・サウンディングモードなどが挙げられます^3^
、攻撃検知のサポート、およびサポートされるアンテナパスの最大数などが挙げられます。

この手順は、LL_CS_CONFIG_REQ と LL_CS_CONFIG_RSP PDU
の交換を含む。要するに、以前に交換された能力を使用して、この手順により、デバイスは使用される特定の構成を選択することができる。

複数のパラメータ
保持してもよい。このような各コンフィグレーションには、Host識別子が割り当てられる。この識別子は、このデバイスのペアで使用される識別子の中で一意でなければならず、リンクレイヤー
手順中に所定のパラメータ セットを参照するために使用することができる。

LL_CS_CONFIG_REQ PDUを送信した機器のアプリケーション 、イニシエータ
またはリフレクタ
どちらの役割を引き受けるかを選択することができる。もう一方のデバイスはLL_CS_CONFIG_RSPで応答し、もう一方の役割を引き受けなければならない。

FAE（Fractional Frequency Offset Actuation
Error）とは、生成された周波数と期待または要求された周波数との差をppm（Parts
Per
Million）で表したものである。すべてのデバイスはこの点である程度の不正確さを持ち、通常、その大きさは使用するRFチャネルによって異なります。

可能な限り正確な距離測定結果を得るために、Bluetooth®チャネル・サウンディングに対応したデバイスには、「モード0
FAEテーブル」と呼ばれるデータテーブルが搭載されている場合があります。このテーブルには各チャネルのFAE値が格納されており、製造工程で設定されます。

モード0 FAEテーブル要求手順は、イニシエータ リフレクタモード0
FAEテーブルを要求することを可能にする。これには、イニシエータ
LL_CS_FAE_REQ PDUを送信し、リフレクタ そのFAEテーブルを含むLL_CS_FAE_RSP
PDUで返信することが含まれる。

一度取得されたFAEテーブルは、同じリフレクタ
将来使用するために保存することができ、この手順は、与えられたデバイスペアに対して一度だけ実行すればよい。

ブルートゥース® Channel Sounding
開始されたとき、デバイスは互いの能力に関する情報を所有している、イニシエータ
リフレクタmode-0
FAEテーブルを持っており（持っている場合）、デバイスが適切なコンフィギュレーションに合意している場合、Channel
Sounding 開始手順を開始することができる。これは
LL_CS_REQ、LL_CS_RSP、LL_CS_IND PDU を介して達成される。

LL_CS_REQ と LL_CS_RSP PDU
には、各デバイスから提案されたタイミングと構造パラメータが含まれる。これらのパラメータは、ブルートゥース®
Channel Sounding中の時間の分割方法とその利用方法を規定します。LL_CS_IND
PDUは、ペリフェラルからLL_CS_REQまたはLL_CS_RSP
PDUを受信した後、セントラル役割のデバイスによって送信される。LL_CS_INDは、ブルートゥース®
Channel Sounding
開始されるべきことを示し、前のPDUの交換に含まれるプロポーザルに基づいて、両方のデバイスが許容できるパラメータ
値を含む。

Bluetooth®チャネルサウンディング手順は、Bluetooth®チャネルサウンディング開始手順が完了した後に開始されます。これは、アプリケーションが距離の計算に使用できる測定値を取得するために、2つのデバイスがRF信号を交換する仕組みです。

ACL
接続では、接続イベント中にパケットを送信できる。接続イベントのタイミングは、その
ACL 接続の接続間隔パラメータ
値に基づいている。接続イベント中、セントラルとペリフェラルはそれぞれ順番にパケットを送信し、セントラルが最初に送信し、ペリフェラルが応答します。他の接続パラメータによっては、ペリフェラルはパケットのサブセット
応答することが許可され、セントラルはイベントのサブセット
間のみ送信することが許可される。

3.3「Bluetooth®チャネル・サウンディング制御手順」に記載されているとおり、Bluetooth®チャネル・サウンディングの開始手順では、LE-ACL接続が使用されます。

[{.aligncenter
.wp-image-234451 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20.png 1369w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-600x208.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-300x104.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-768x266.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-450x156.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-660x229.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-800x277.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-1000x346.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20-1200x415.png 1200w"
sizes="auto, (max-width: 1369px) 100vw, 1369px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_20.png)

*図 20 - LE-ACL 接続における接続イベントと間隔*

ブルートゥース®Channel Sounding
、一連の手順で行われる。各手順は複数のCSイベントから構成され、各CSイベントはさらにCSサブイベントに分割されます。この階層スキームにおける最終的な時間の区分がCSステップです。ステップ内で、パケットまたはトーンが送受信されます。図
21 に、時間の分割に関するこの構造スキームを例として示します。

[{.aligncenter
.wp-image-234452 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21.png 1824w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-600x302.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-300x151.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-768x386.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1536x772.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-450x226.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-660x332.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-800x402.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1000x503.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1200x603.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21-1600x804.png 1600w"
sizes="auto, (max-width: 1824px) 100vw, 1824px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_21.png)

*図 21 -ブルートゥース® Channel Sounding 構成例*

Bluetooth®チャネル・サウンディング手順の構造的な側面を制御するためのパラメータがいくつかあります。設定可能な主な変数の一部を表4に示します。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">設定可能な変数</th>
<th class="has-text-align-left" data-align="left">範囲／値</th>
<th class="has-text-align-left" data-align="left">項目</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">CS処置の実施回数</td>
<td class="has-text-align-left" data-align="left">0 ～ 65535</td>
<td class="has-text-align-left"
data-align="left">Bluetooth®チャネル・サウンディングが終了するまでに実行するCSプロシージャの繰り返し回数。値が0の場合、CSプロシージャは「Bluetooth®チャネル・サウンディング・プロシージャの繰り返し終了」プロシージャによって終了されるまで実行され続けることを示します。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">イベントごとのサブイベント数</td>
<td class="has-text-align-left" data-align="left">1～16</td>
<td class="has-text-align-left"
data-align="left">同じACLイベントに紐付けられたサブイベントの数。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">サブイベント間隔</td>
<td class="has-text-align-left"
data-align="left">0、または625マイクロ秒から40959.375ミリ秒の範囲。</td>
<td class="has-text-align-left"
data-align="left">同じCSイベント内で、あるCSサブイベントの開始から次のCSサブイベントの開始までの時間間隔。0は、サブイベントに分割されないことを意味する。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">各サブイベントの所要時間</td>
<td class="has-text-align-left" data-align="left">変数</td>
<td class="has-text-align-left"
data-align="left">各サブイベントの所要時間。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">サブイベントごとのステップ数</td>
<td class="has-text-align-left" data-align="left">2～160</td>
<td class="has-text-align-left"
data-align="left">設定された範囲からランダムに選択されます。1回の処理につき、最大256ステップまで可能です。</td>
</tr>
</tbody>
</table>

*表 4 -ブルートゥース® Channel Sounding 設定パラメータ例*

手順、イベント、サブイベント、ステップのタイミング、期間、スケジューリングは、ブルートゥース®
Channel Sounding ブルートゥース® Channel Sounding
手順で設定される多くのパラメータによって制御されます。

すべての手順、イベント、サブイベント、およびステップの開始時刻は、基盤となるLE
ACL接続で選択された接続イベントに直接的または間接的に紐付けられています。最初のBluetooth®チャネルサウンディング手順のインスタンスでは、その最初のイベントとサブイベントはすべて同時に開始され、選択された接続イベントのアンカーポイントからオフセットされた時刻に発生するようにスケジュールされます。
最初のステップは、T_FCSと呼ばれる最初のサブイベントの開始時刻からオフセットされた時点で発生します。T_FCSの値は15
μsから150
μsの範囲にあり、この期間を利用してホッピングにより周波数を変更します。

プロシージャとイベントはどちらも、ACL接続間隔の数で表される間隔で発生します。図22は、プロシージャ間隔の値が4、イベント間隔の値が2である例を示しています。

[{.aligncenter
.wp-image-234453 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22.png 1713w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-600x243.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-300x121.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-768x311.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1536x621.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-450x182.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-660x267.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-800x324.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1000x405.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1200x485.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22-1600x647.png 1600w"
sizes="auto, (max-width: 1713px) 100vw, 1713px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_22.png)

*図22 -
手続きとイベントのスケジューリング（手続き間隔＝4、イベント間隔＝2*

各イベントの最初のサブイベントは、関連する ACL
接続イベントからオフセットして、イベントと同時に開始する。イベントごとのサブイベント数はパラメータ
であり、図 23 に示すように、サブイベントはサブイベント間隔ごとに 1
回発生する。

[{.aligncenter
.wp-image-234454 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23.png 1713w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-600x243.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-300x121.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-768x311.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1536x621.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-450x182.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-660x267.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-800x324.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1000x405.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1200x485.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23-1600x647.png 1600w"
sizes="auto, (max-width: 1713px) 100vw, 1713px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_23.png)

*図 23 - CS イベント・スケジューリング内の CS サブイベントの例*

各サブイベントには、少なくとも2つのステップが含まれる。これは、アプリケーション
channel sounding
どのように使用されているかによって、サブイベントごとに異なる可能性がある。ステップの継続時間は、やはり構成によって異なる。ステップのスケジューリングと、それらに割り当てられるRF送受信スロットは、綿密なタイミングルールに従うブルートゥースコア仕様

イニシエータ レシーバー RF信号の交換は、ほんの数歩のレシーバー
。アプリケーション層が選択したチャネル探査方式（PBR
RTT）によって、詳細は異なります。

一般的に、ステップは校正に関係するか、距離測定アルゴリズムでアプリケーション
層が使用できる低レベル測定値の取得に関係する。

RTT 使用されているとき、CS_Syncと呼ばれるタイプのパケットがイニシエータ
リフレクタ交換される。

[{.aligncenter
.wp-image-234455 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24.png 1937w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-600x125.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-300x62.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-768x159.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1536x319.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-450x93.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-660x137.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-800x166.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1000x208.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1200x249.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24-1600x332.png 1600w"
sizes="auto, (max-width: 1937px) 100vw, 1937px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_24.png)

*図 24 - CS_Sync パケット*

CS_Syncパケットの末尾にSounding SequenceまたはRandom
Sequenceを含めるかどうかは任意です。CS_Syncパケットは、LE 1M、LE 2M LE
2M PHYのいずれかを使用して送信できます。GFSK^4^
変調方式が使用されます。

PBR 使用時には、CSトーンと呼ばれる信号がイニシエータ
リフレクタ交換される。これらの信号は、ASK（Amplitude Shift
Keying：振幅シフト・キーイング）を使用して、周波数が一定時間固定されたシンボルを生成する。

ステップには関連するモードがあり、ステップのゴールとその中で行われるアクティビティのタイプを決定する。つのモードが定義されており、モード-0、モード-1、モード-2、モード-3と指定されている。

Mode-0は較正に関するものである。すべてのデバイスは、ある程度のクロック・ドリフトと周波数生成の不正確さを示す。これは、RTT
PBR 両方の距離測定方法にとって問題である。

モード0ステップの目的は、トランスミッター生成された信号と、リフレクタ
送信された信号の周波数が異なる量を測定できるようにすることである。

イニシエータ 、選択したチャネルと周波数で CS_Sync
パケットを送信する。リフレクタ
CS_SyncパケットとCSトーンで応答する。どちらも、イニシエータ受信した信号と同じ周波数で送信する必要があります。

イニシエータ 、リフレクタ応答信号を受信すると、Fractional Frequency
Offset（FFO）と呼ばれる値をイニシエータ 。FFOの算出にはリフレクタ
受信したトーンの周波数リフレクタ リフレクタモード0
FAEテーブルが用いられます。FFOは、その後、2つのデバイス間の差異を補正し、結果の精度を向上させるための計算に使用されます。

図 25 は、イニシエータ CS_Sync
パケットの送信と、それに続いてリフレクタ応答として送信する CS_Sync
および CS Tone
を示している。様々なタイム・スロットの時間は、以下の意味を持つ記号名で示される：

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">記号</th>
<th class="has-text-align-left" data-align="left">意味</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">T_SY</td>
<td class="has-text-align-left"
data-align="left">同期シーケンスの実行時間です。所要時間は、CS_Syncパケットの長さと使用されるPHYによって異なります。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_RD</td>
<td class="has-text-align-left"
data-align="left">送信ランプダウンの時間。これは5μsで、トランスミッター
RFチャネルからエネルギーを除去するために使用される。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_IP1</td>
<td class="has-text-align-left"
data-align="left">イニシエータ送信終了からリフレクタ送信開始までの間奏時間。持続時間は10μs～145μsの間で変化し、能力交換手順で決定される。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_GD</td>
<td class="has-text-align-left"
data-align="left">ガード時間。常に10μ秒。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_FM</td>
<td class="has-text-align-left"
data-align="left">周波数測定時間。ステップモード0では常に80μs。</td>
</tr>
</tbody>
</table>

*表5 -- タイムスロットのパラメータ*

[{.aligncenter
.wp-image-234456 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25.png 1713w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-600x163.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-300x82.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-768x209.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1536x418.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-450x122.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-660x180.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-800x218.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1000x272.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1200x326.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25-1600x435.png 1600w"
sizes="auto, (max-width: 1713px) 100vw, 1713px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_25.png)

*図25 - Mode-0の送信とタイムスロット*

モード0ステップのサポートは必須である。

mode-1ステップでは、イニシエータ リフレクタ
送信されたCS_Syncパケットの往復タイミングRTT）が計算される。

タイムスタンプは、最初のCS_Syncパケットを送信するときにイニシエータ 記録
され、Time of Departure（ToD）と呼ばれる。イニシエータ
リフレクタ送り返されたCS_Syncパケットを受信する際に2つ目のタイムスタ
ンプを記録する。これは到着時刻（ToA）と呼ばれる。

[{.aligncenter
.wp-image-234457 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1000x248.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-600x149.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-300x74.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-768x191.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1536x381.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-450x112.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-660x164.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-800x199.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1200x298.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26-1600x397.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26.png 1878w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_26.png)

*図26 - モード1送信とタイムスロット*

インタールード期間T_IP1は、リフレクタ
パケットを準備し送信するのに十分な、既知の
固定長である。交換のこの部分で事前に合意された固定期間を使用することは、イニシエータ
レシーバー ターンアラウンド時間を知っており、RTT 計算にこれを使用でき
ることを意味する。

モード1ステップのサポートは必須である。

モード2ステップの目的は、位相ベース測距 PBRサポートすることである。

モード2のステップは、イニシエータ
選択されたチャネルおよび利用可能な各アンテナ経路を介してCSトーンイニシエータ
から始まる。減衰時間と間隔期間の後、リフレクタ は、イニシエータ
から受信したトーンと同じ周波数を選択しイニシエータ
自身の各アンテナ経路イニシエータ 介してCSトーンでリフレクタ
。図27はこの通信の流れを示している。
タイムスロットの持続時間には、表5に記載された用語に加え、表6で定義された追加の用語が含まれる。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">記号</th>
<th class="has-text-align-left" data-align="left">意味</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">T_SW</td>
<td class="has-text-align-left"
data-align="left">アンテナ切り替えのための予約時間。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_PM</td>
<td class="has-text-align-left"
data-align="left">位相測定トーンの送信時間。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">T_IP2</td>
<td class="has-text-align-left"
data-align="left">CSトーン間の間奏時間。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">N_AP</td>
<td class="has-text-align-left"
data-align="left">アンテナ経路の数。</td>
</tr>
</tbody>
</table>

*表6 - 追加のステップ・モード2タイミング・パラメーター*

[{.aligncenter
.wp-image-234458 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1000x268.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-600x161.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-300x81.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-768x206.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1536x412.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-450x121.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-660x177.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-800x215.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1200x322.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27-1600x429.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27.png 1878w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27.png)

*図27-モード2の送信とタイムスロット*

イニシエータ 、期間T_PMの間にリフレクタ 受信したCS
Toneの位相を、各アンテナ経路について1回ずつ測定する。調整は、mode-0
ステップで計算された補正値を使用して行われます。位相測定値は、IQサンプルの配列の形でHCIイベントのアプリケーション
層に渡されます。

なお、CSトーンの送信総時間の式には、**N_AP + 1**
という項が含まれていることに留意すべきである。これは、各アンテナパスに割り当てられたT_PM期間のタイムスロットの後に、CSトーン延長スロットと呼ばれる追加の期間が続くためである。
セキュリティ上の理由から、このタイムスロットの使用はランダム化されているが、使用される場合、直前の
T_PM タイムスロットで使用されたのと同じアンテナを用いて CS
トーンが送信される。

モード2ステップのサポートは必須である。

mode-3ステップは、CS_SyncパケットとCS
Toneを組み合わせた交換を使用して、RTT 計算とPBR 両方をサポートする。

[{.aligncenter
.wp-image-234459 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1000x260.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-600x156.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-300x78.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-768x200.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1536x400.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-450x117.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-660x172.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-800x208.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1200x312.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B-1600x417.png 1600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B.png 1878w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_27_B.png)

*図28-モード3の送信とタイムスロット*

モード3のサポートは必須ではありません。RTT 組み合わせRTT
機能交換手順を通じてイニシエータ リフレクタ
双方がモード3をサポートしていないことが判明したアプリケーションは、代わりにモード2とモード1のステップを組み合わせたモードシーケンスを使用リフレクタ
。

モード3ステップには、モード2ステップで説明したようなエクステンションスロットがある。

モード-0、モード-1、モード-2、モード-3の各ステップに関するこれまでのセクションでは、それぞれのタイプの1つのステップにおいて、時間がどのように分割され、使用されるかという詳細に焦点が当てられていた。しかし、距離の計算では、計算された距離の精度を高めるため、あるいは使用される手法がそれを要求するため、複数の交換が必要となる。PBR
定義では、少なくとも2回の交換が必要となる。

位相差を測定可能にするためには、複数の送信信号が存在し、かつ複数の周波数が関与している必要があります。1つのステップでは、選択された単一のチャネルおよび周波数上で、1つのCSトーンの交換が行われます。したがって、PBR
、PBR
をサポートするモードのステップを少なくとも2つ実行する必要があることは明らかです。
一般的に、より多くのRFチャネルセットを使用してCSトーンの交換回数を増やすほど、アプリケーションはより多くのデータを得ることができ、より正確な距離測定が可能になることに留意すべきである。ただし、交換回数が増えると、実行に要する時間も長くなる。

3.2.3 アンテナ・アレイで述べたように、デバイスは位相ベース測距
交換中に使用するために複数のアンテナを含むことができる。PBR
交換（すなわち、モード 2 またはモード 3
ステップ）中に使用するためにデバイスが持つことができるアンテナの最大数は
4 です。あるアンテナ構成のペア（1つはイニシエータ
属し、1つはリフレクタ属する）は、2つのデバイス間に多数のアンテナ経路を提供します。

Bluetoothコア仕様では、合計8種類のアンテナ構成が定義されています。表7にこれらの構成を示します。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left"
data-align="left">アンテナ構成指数（ACI）</th>
<th class="has-text-align-left" data-align="left">装置 アンテナの数</th>
<th class="has-text-align-left"
data-align="left">デバイスBのアンテナ数</th>
<th class="has-text-align-left" data-align="left">アンテナパス数
(N_AP)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0</td>
<td class="has-text-align-left" data-align="left">1</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">3</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">3</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">3</td>
<td class="has-text-align-left" data-align="left">4</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">4</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">4</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">5</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">3</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">6</td>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">4</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">7</td>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">4</td>
</tr>
</tbody>
</table>

*表7 - アンテナ構成*

アンテナの切り替えは、モード 2 ステップPBR）中および各モード 3
ステップのPBR部分で行われる。具体的には、送信デバイスのアンテナ構成に応じて、CSトーンの送信時にアンテナ切り替えが適用される。mode-2およびmode-3ステップにおけるCSトーン送信タイムスロットの持続時間の計算は、アンテナ切り替えと複数のアンテナ経路に対応する：

*(T_SW+T_PM)\*(N_AP+1)*

- T_SWはアンテナ切り替えが行われるまでの時間を指定するパラメータであり、その値は0、2、4、または10マイクロ秒のいずれかです。
- T_PMは、CSトーンの送信にかかる時間です。
- N_AP はアンテナパスの数です。+1
の項は、拡張スロットを考慮するためのものです。

ブルートゥース® Channel Sounding
手順では、常に複数のステップと少なくとも2つのモ
ードをミックスしたシーケンスが実行されます。ブルートゥースコア仕様
、モードの組み合わせとシーケンスルールを定義しています。

ブルートゥース®Channel Sounding 、Bluetooth
コントローラーから、より多くのパケットとトーンの交換から得られたデータを提供された場合、より高品質で正確な距離測定を行います。

Bluetooth®チャネル・サウンディング手順には、常に少なくとも2種類の異なるモードのステップが含まれます。1つ目は周波数オフセット測定を行うモード0のステップであり、2つ目は他のモードのいずれかである必要があります。モード0以外の主要なモードは
Main_Mode
と呼ばれます。モード0以外の副次的なモードがある場合は、Sub_Mode
と呼ばれます。表8には、許可されている6つのモード0以外のモードの組み合わせが示されています。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">メインモード</th>
<th class="has-text-align-left" data-align="left">サブモード</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">モード1</td>
<td class="has-text-align-left" data-align="left">なし</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">モード2</td>
<td class="has-text-align-left" data-align="left">なし</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">モード3</td>
<td class="has-text-align-left" data-align="left">なし</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">モード2</td>
<td class="has-text-align-left" data-align="left">モード1</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">モード2</td>
<td class="has-text-align-left" data-align="left">モード3</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">モード3</td>
<td class="has-text-align-left" data-align="left">モード2</td>
</tr>
</tbody>
</table>

*表8 - 許容されるモード0以外のモードの組み合わせ*

アプリケーションは、HCIコマンドを使用してステップモードのシーケンスを設定することができます。デバイス間で要求および合意される可能性のある主要なパラメータには、表9に示すものがあります。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">HCIパラメータ</th>
<th class="has-text-align-left" data-align="left">目的</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left"
data-align="left">モード_0_ステップ数</td>
<td class="has-text-align-left"
data-align="left">各CSサブイベントの開始時に実行されるモード0ステップの連続回数を指定します。指定可能な値は1、2、または3です。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">メインモードタイプ</td>
<td class="has-text-align-left"
data-align="left">メインモードとなるモード（1、2、または3）を示します。</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">サブモードタイプ</td>
<td class="has-text-align-left"
data-align="left">サブモードとなるモード（1、2、または3）を示します。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">Min_Main_Mode_Steps</td>
<td class="has-text-align-left"
data-align="left">サブモードのステップを実行する前に、必ず実行しなければならないメインモードのステップの最小数を指定します。</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">Max_Main_Mode_Steps</td>
<td class="has-text-align-left"
data-align="left">サブモードのステップを実行する前に、必ず実行しなければならないメインモードのステップの最大数を指定します。</td>
</tr>
</tbody>
</table>

*表 9 - モード・シーケンス制御パラメータ*

一般的に、ステップモードのシーケンスはこのパターンに従う：

1. 1つ以上のmode-0ステップがサブイベントを開始する。
2. ここでnはランダムに選択され、Min_Main_Mode_StepsからMax_Main_Mode_Stepsの範囲に含まれる。
3. ブルートゥースコア仕様
サブモード挿入と呼ぶプロセスにより、1つのサブモードステップがn個のメインモードステップのシーケンスに続く。

ステップ・モード・シーケンスは、サブイベントが常に1つ以上のモード0ステップで始まらなければならないという一般的なルール以外には、サブイベントの境界に縛られることはない。フルシーケンスは複数のサブイベントにまたがることができる。

[{.aligncenter
.wp-image-234464 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1000x334.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-600x200.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-2000x667.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-300x100.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-768x256.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1536x513.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-2048x683.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-450x150.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-660x220.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-800x267.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1200x400.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32-1600x534.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_32.png)

*図33 - ステップ・モードのシーケンス例*

もう1つ、アプリケーションで使用できるモードシーケンスのパラメータ
ある。Main_Mode_Repetitionは、現在のサブイベントで繰り返される、最後のサブイベントからの最新のメインモードステップの数を指定します。

メインモードの繰り返し機能が適用される場合、現在のサブイベントで繰り返されるステップは、前のサブイベントにおける対応するステップで使用されたものと同じチャネルインデックスを使用します。これにより、繰り返されるステップの送信が意図した周波数で行われることが保証されます。なお、メインモードのステップを同じ周波数で繰り返す目的は、周波数ドリフトやドップラーシフトの影響に対処することにあります。

メインモードの繰り返しは、アプリケーションに交流の特性のいくつかを相関させる機会を与え、移動するデバイスの速度を追跡することを容易にするかもしれない。

メインモードの繰り返しによってモードシーケンスに組み込まれるステップは、サブモードの挿入処理ではカウントされません。

サブモードの挿入やメインモードの繰り返しを活用してモードの組み合わせを設定し、ステップモードのシーケンスを制御できるため、アプリケーションはBluetooth®チャネルサウンディングのプロセスを詳細に制御できます。PBR
2つの距離測定手法のうち最も精度PBR 、RTT
システムのセキュリティが大幅に向PBR 。また、PBR
の使用時に生じうる距離の曖昧性に対処することも可能になります。

ステップ・モード-3は1つのモードタイプで両方の方式をサポートするが、モード-3のサ
ポートはオプションである。したがって、能力交換手順の間に mode-3
が利用できないことを発見したデバイスは、mode-1RTT）と
mode-2PBR）ステップを混在させなければならない。これは、mode-2をメイン・モード、mode-1をサブ・モードとして選択することで実現できる。

アプリケーションにおいてさらに考慮すべき点は、遅延です。信号のやり取りには毎回時間がかかります。アンテナ経路の数によっては、モード1RTT
モード2PBR
よりも時間がかかる場合があります。遅延を一定の閾値以下に抑える必要があるアプリケーションでは、Bluetooth®チャネルサウンディング手順におけるRTT
割合を低く設定する傾向があります。

[{.aligncenter
.wp-image-234464 .size-1000w loading="lazy" decoding="async"
height="334"}](https://www.bluetooth.com/wp-content/uploads/2025/01/Figure_34.png)

*図34-モード2とモード1を使用した3:1のPBR 対RTT 比*

[{.aligncenter
.wp-image-234464 .size-1000w loading="lazy" decoding="async"
height="334"}](https://www.bluetooth.com/wp-content/uploads/2025/01/Figure_35-1.png)

*図35-モード2とモード3を使用した3:1のPBR 対RTT 比*

通常、Bluetooth LE
2.4GHzのISMバンドを2MHz幅の40チャンネルに分割します。しかし、ブルートゥース®
Channel Sounding使用する場合はそうではありません。

ブルートゥース® Channel Sounding目的のため、72
チャンネルが定義され、各チャンネルは 1MHz
の幅と固有のチャンネル・インデックス値を持つ。これらのチャンネルの配置は、LEの主要な広告チャンネルを避けることを保証します。

チャンネル幅を通常の2MHzではなく1MHzにすることで、隣接するチャンネルを使用するPBR
信号間の周波数分離を確保し、150m付近まで距離の曖昧さが生じないようにしている。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">CSチャンネル指数</th>
<th class="has-text-align-left" data-align="left">RF中心周波数</th>
<th class="has-text-align-left" data-align="left">可</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0</td>
<td class="has-text-align-left" data-align="left">2402MHz</td>
<td class="has-text-align-left" data-align="left">いいえ</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">2403 MHz</td>
<td class="has-text-align-left" data-align="left">いいえ</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">2404MHz</td>
<td class="has-text-align-left" data-align="left">はい</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">...</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">22</td>
<td class="has-text-align-left" data-align="left">2424MHz</td>
<td class="has-text-align-left" data-align="left">はい</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">23</td>
<td class="has-text-align-left" data-align="left">2425MHz</td>
<td class="has-text-align-left" data-align="left">いいえ</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">24</td>
<td class="has-text-align-left" data-align="left">2426MHz</td>
<td class="has-text-align-left" data-align="left">いいえ</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">25</td>
<td class="has-text-align-left" data-align="left">2427MHz</td>
<td class="has-text-align-left" data-align="left">いいえ</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">26</td>
<td class="has-text-align-left" data-align="left">2428 MHz</td>
<td class="has-text-align-left" data-align="left">はい</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">...</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">76</td>
<td class="has-text-align-left" data-align="left">2478MHz</td>
<td class="has-text-align-left" data-align="left">はい</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">77</td>
<td class="has-text-align-left" data-align="left">2479 MHz</td>
<td class="has-text-align-left" data-align="left">いいえ</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">78</td>
<td class="has-text-align-left" data-align="left">2480 MHz</td>
<td class="has-text-align-left" data-align="left">いいえ</td>
</tr>
</tbody>
</table>

*表10 -ブルートゥース® Channel Sounding RF物理チャンネル*

チャネルインデックスフィルタビットマップが管理されています。これは、Bluetooth®チャネルサウンディング用に定義されたチャネルインデックスのリストであり、各チャネルが「包含」または「除外」のいずれかとしてマークされています。
Bluetooth®チャネルサウンディングのチャネルインデックスフィルタマップは、「チャネルサウンディング・チャネルマップ更新」と呼ばれるリンクレイヤー
によって管理されます。このプロシージャにより、リフレクタ
、ローカルチャネルの状態を評価した上で、使用するチャネルや回避すべきチャネルを相手デバイスに通知リフレクタ
。除外されたチャネルは、どのチャネル選択アルゴリズムによっても選択されることはありません。

周波数ホッピングは一般に、図36に描かれているように、ステップ実行の直前に行われる。

[{.aligncenter
.wp-image-234467 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1000x81.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-600x49.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-2000x162.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-300x24.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-768x62.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1536x124.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-2048x166.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-450x36.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-660x53.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-800x65.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1200x97.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35-1600x129.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_35.png)

*図36 -- ステップ実行前の周波数ホッピング*

このルールの例外は、Main_Mode_Repetitionパラメータゼロ以外の値が割り当てられてモード反復が設定されている場合に適用されます。モード繰り返しによって繰り返されるステップは、繰り返される前のサブイベントのステップと同じチャンネル・インデックスを使用します。

ブルートゥース® Channel
Sounding使用する3つのチャンネル選択アルゴリズム（CSA）の新しいセットが定義されました。これらは総称してCSA
#3、個別にCSA #3a、CSA #3b、CSA #3cと呼ばれています。

CSA #3a は、モード 0
のステップで使用するチャネルを選択するためにのみ使用されます。CSA #3b
および CSA #3c は、いずれもモード 0
以外のステップで使用されるように設計されていますが、Bluetooth®
チャネル・サウンディング手順の実行中には、この 2 つのうち 1
つしか使用できません。その結果、いつでも 2
つの異なるチャネル選択アルゴリズムが Bluetooth®
チャネル・サウンディングにアクティブに関連付けられています。

チャンネル選択には、2つの異なるチャンネルインデックスリストが含まれる。最初のものは
CSA #3a とモード 0 ステップのチャンネル選択で使用される。もう1つは、CSA
#3bまたはCSA #3cでモード0以外のステップに使用される。

チャンネルインデックスリストは、チャンネルマップに含まれているとマークされたチャンネルの順番をランダムにして、シャッフルされたチャンネルリストを作成する。CSA#3aとCSA#3bはまったく同じ方法でこれを行う。CSA#3cは異なるアプローチをとるが、ブルートゥースコア仕様cr1として知られる、同じ原始的なシャッフル関数に依存している。

モード0のチャネル選択アルゴリズムCSA
#3aでは、シャッフルされたチャネルリストが使用される。モード0のステップ周波数ホッピングに使用されるシャッフルされたチャネルリストは、モード0以外のチャネルホッピングに使用される対応するチャネルリストとは異なる。シャッフルされたチャネルリストの各エントリは一意であり、一度しか使用されない。シャッフルされたチャネルリストのすべてのエントリが使用されると、リストは再生成され、新しいランダム化されたチャネルリストが生成される。

非モード0チャネル選択アルゴリズムCSA
#3bは、モード0チャネルホッピングに使用される対応するチャネルリストとは異なる、シャッフルされたチャネルリストを使用する。CSA
#3b
では、チャネルインデックスリストが再生成される前に複数回繰り返されることが許されており、これは
CSNumRepetitions と呼ばれるパラメータ 制御される。

アルゴリズムCSA #3cは、CSA
#3bとは大きく異なります。チャネルマップに含まれるチャネルのサブセットがグループに整理され、形状を形成するチャネルパターンが生成されます。2種類のパターンがサポートされており、「hat」および「X」と名付けられています。CSA
#3cは、状況によっては反射信号経路の検出において一定の利点をもたらす可能性があります。CSA
#3cのサポートはオプションです。

RTT
、モード1および／またはモード3の手順に従ってCS_Syncパケットの交換が行われます。往復時間の計算に必要な到着時刻（ToA）タイムスタンプを設定するためのいくつかの方法が定義されています。アプリケーションは、HCIパラメータを使用して、Bluetooth®チャネルサウンディングの設定手順中に使用する方法を指定することができます。

アクセス・アドレス
フィールドに基づくタイミング測定、32ビットまたは96ビットの長さのサウンディング・シーケンスの使用、または32、64、96、128ビットの長さのランダム・シーケンスの使用のオプションがある。時間推定の精度は、使用する方法とタイミング目的で使用するフィールドの長さによって異なる。サウンディング・シーケンスの使用とランダム・シーケンスの使用の両方により、分数タイミング推定として知られるより正確な推定を行うことができる。

CS_Syncパケットには、32ビットのAccessアドレス
フィールドが含まれる。ToA値を確立するために使用できる最も単純な方法は、コントローラがクロックを使用して、CS_SyncパケットのAccessアドレス
フィールドを受信した時点のタイムスタンプを取得することである。

アクセスアドレスはリンクレイヤー 32ビットの2進値リンクレイヤー
送信時には、それらのデジタルビットにGFSK変調を適用することで形成された一連のアナログシンボルによってその値が表現される。1つのシンボルは、0または1のビット値を表す周波数での無線送信からなり、シンボルレートに応じて、その持続時間は1マイクロ秒または0.5マイクロ秒となる。

トランスミッター発振器とレシーバー発振器の位相が一致する可能性は低く、これがこのプロセスの不正確さの原因となる可能性がある。結果を改善するために、一連のステップで交換される一連のパケットを測定し、値の分布を計算することが提案されている。この分布を利用して、ToAタイムスタンプの精度を向上させることができる。

ToAタイムスタンプの精度を向上させる2つのオプション手法が、リンクレイヤー
（Part
H）の3.3節および3.4節に記載されている。いずれも部分的タイミング推定を提供する。

CS_Sync
パケットには、パケットの最後に追加のオプション・データを追加することができる。このオプションが使用される場合、CS_Sync
パケットには、ランダム・シーケンスまたはサウンディング・シーケンスの 2
つのフィールドのいずれかが追加される。

分数のタイミング誤差を算出する手法の1つ目は、CS_Syncパケット内のオプションである「ランダムシーケンス」フィールドを解析し、分数のタイミング誤差を特定するものです。ランダムシーケンスから算出された分数のタイミング誤差は、アクセスアドレスのタイムスタンプを最適化するために使用されます。

2つ目の小数点以下のタイミング測定法は、CS_Syncパケットに付加されたサウンディングシーケンスフィールドの解析に基づいています。サウンディングシーケンスリンクレイヤー
における0と1が交互に並ぶパターンでありリンクレイヤー
GFSKを用いて変調するとリンクレイヤー
周波数と位相が異なる2つの明確な無線トーンリンクレイヤー
生成されますリンクレイヤー
これら2つのトーンが示す位相差を解析することで、小数点以下のタイミング誤差を算出し、ToAタイムスタンプの最適化に活用することができます。

ブルートゥース®アプリケーション
開発者は、3つの異なる方法の1つによって生成された測定値に基づいて、ラウンドトリップタイムを導出することができます。選択肢は、アクセス・アドレス
ToAを使用するか、CS_Syncパケット内のランダム・シーケンスまたはサウンディング・シーケンスのいずれかに基づく2つの分数メソッドのいずれかを使用するかです。

3つのRTT 方式は、距離測定の精度、安全性、そしてアプリケーション
開発者にとっての待ち時間が異なる。一般的に、分数メソッドは最も正確な結果と最高のセキュリティを提供する可能性があります。

変調方式とは、信号の1つ以上の物理的特性を利用して、デジタル情報を信号に符号化する方法のことです。周波数変調（FSK）は、変調方式の簡単な例です。この方式では、搬送波の周波数を一定量（周波数偏移）だけ上昇させることで2進数の「1」を表し、同様に下降させることで「0」を表すシンボルを生成します。

[ encoded bit stream"){.aligncenter
.wp-image-234468 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1000x256.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-600x154.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-2000x513.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-300x77.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-768x197.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1536x394.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-2048x525.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-450x115.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-660x169.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-800x205.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1200x308.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36-1600x410.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_36.png)

*図 37 - 周波数シフト・キーイング（FSK）符号化ビット・ストリーム
01010101010*

機能
である周波数の急激な切り替えは、望ましい範囲よりも広い周波数帯域にノイズが広がる原因となります。これに対処するため、Bluetooth技術では、ガウス周波数変調（GFSK）と呼ばれるFSKの特殊な変種を採用しています。GFSKは、周波数間の遷移が曲線を描くようにするフィルタを用いる点で、基本的なFSKとは異なります。
この曲線の形状や周波数遷移の速度は、帯域幅-ビット周期製品 BT製品
を含む様々なパラメータによって決定されます。

製品 BT）製品
信号の帯域幅とシンボルの持続時間との関係に関する情報を提供する信号の属性です。BTは、シンボルを構成する無線パルスの形状と幅に影響を与えます。BTの値が高いほど、パルスは狭く角張った形状になり、値が低いほど、パルスは広く丸みを帯びた形状になります。

Bluetoothコア仕様では、LE 2M と呼ばれる新しいPHYが導入されています。LE
2M
、現時点ではBluetooth®チャネル・サウンディングでのみ使用可能です。表11には、LE
2M 主な特徴を強調したPHYの比較が示されています。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left"></th>
<th class="has-text-align-left" data-align="left">LE 1M</th>
<th class="has-text-align-left" data-align="left">LE Coded</th>
<th class="has-text-align-left" data-align="left">LE 2M</th>
<th class="has-text-align-left" data-align="left">LE 2M 2BT</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">シンボル・レート</td>
<td class="has-text-align-left" data-align="left">1 メガシンボル/秒</td>
<td class="has-text-align-left" data-align="left">2 Msym/s</td>
</tr>
<tr>
<td class="has-text-align-left"
data-align="left">ブリティッシュ・テレコム</td>
<td class="has-text-align-left" data-align="left">0.5</td>
<td class="has-text-align-left" data-align="left">2.0</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">最小周波数偏差</td>
<td class="has-text-align-left" data-align="left">185 kHz</td>
<td class="has-text-align-left" data-align="left">370 kHz</td>
<td class="has-text-align-left" data-align="left">420 kHz</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">エラー検出</td>
<td class="has-text-align-left" data-align="left">CRC</td>
<td class="has-text-align-left" data-align="left">該当なし</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">エラー訂正</td>
<td class="has-text-align-left" data-align="left">なし</td>
<td class="has-text-align-left" data-align="left">FEC</td>
<td class="has-text-align-left" data-align="left">なし</td>
<td class="has-text-align-left" data-align="left">該当なし</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">必要条件</td>
<td class="has-text-align-left" data-align="left">必須</td>
<td class="has-text-align-left" data-align="left">オプション</td>
<td class="has-text-align-left"
data-align="left">任意。チャンネル測深時のみ使用してください。</td>
</tr>
</tbody>
</table>

*表 11 -Bluetooth LE PHY の比較*

[{.aligncenter
.wp-image-234469 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37.png 778w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-600x471.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-300x236.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-768x603.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-450x353.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37-660x518.png 660w"
sizes="auto, (max-width: 778px) 100vw, 778px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_37.png)

*図38 - パルス形状*

一部の無線送信機には、信号対雑音比（SNR）を特定の範囲内に収めるように調整する機能があります。この機能は、イニシエータ
リフレクタ の両方のリフレクタ 対応している場合、RTT
測定法に関連するBluetooth®チャネルサウンディングの手順、すなわちモード1およびモード3の手順のセキュリティを向上させるために利用できます。

ブルートゥースコア仕様 、dB で測定される関連 SNR
出力レベルに対応するいくつかの SNR 出力指数（SOI）値を定義している。表
12 にこれらの定義を示す。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left"
data-align="left">SNR出力指数（SOI）</th>
<th class="has-text-align-left"
data-align="left">SNR出力レベル（dB）</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0</td>
<td class="has-text-align-left" data-align="left">18</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">1</td>
<td class="has-text-align-left" data-align="left">21</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">2</td>
<td class="has-text-align-left" data-align="left">24</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">3</td>
<td class="has-text-align-left" data-align="left">27</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">4</td>
<td class="has-text-align-left" data-align="left">30</td>
</tr>
</tbody>
</table>

*表12 - SNR出力指標とレベル*

距離測定ソリューションに特有のセキュリティ上の課題は、一般的に、信頼できないデバイスが何らかの手段を用いて、ある信頼できるデバイスに対し、別の信頼できるデバイスが特定のアクションを許可または実行するのに十分な距離にあると誤認させるという脅威を伴う。

ブルートゥース®Channel Sounding
、距離測定のセキュリティ上の脅威に対する対策として機能する機能が搭載されています。これらの機能は4つのカテゴリーに分類されます：

1. PBR RTT 併用
2. ビットストリームと送信パターンのランダム化
3. シンボル操作に対する防御
4. 攻撃検知を含むRF信号解析技術

Bluetooth® Channel Soundingは、位相ベース測距
PBR）と往復伝播時間（RTT）の2つの距離測定方式をサポートしています。これら2つの方式はPBR
その動作原理が全く異なります。アプリケーションでは、PBR
メインモードとしてモード2をPBR
RTTサブモードとしてモード1を選択するなど、適切なモードの組み合わせを設定することで、両方の方式を併用することができます。

ブルートゥース® Channel Sounding
信号の位相と計算された往復時間の両方を操作して、誤解を招くような一貫性のある結果を出すために、両方の方法を同時に攻撃することの複雑さは、セキュリティの専門家によって非常に高いとみなされている。

まず、デバイス同士がペアリングされている必要があります。これは、暗号化されたLE-ACLリンクを確立するために不可欠です。その後、暗号化されたLE-ACLリンクを介してCS
Security Startが実行されるため、Bluetooth® Channelセキュリティキー
やり取りが盗聴から保護されます。

最後に、セントラル・デバイスとペリフェラル・デバイスの両方が、ブルートゥース®
Channel Sounding 部分値の安全な交換を実行します。これにより、CS
初期化ベクトル（CS_IV）、CS インスタンス化ノンス （CS_IN）、CS
パーソナライゼーション・ベク
トル（CS_PV）のそれぞれについて、完全な共通値を構
築するための同じデータが両デバイスに提供されます。

Bluetoothコア仕様では、NIST特別刊行物800-90Ar1で定義された推奨事項に準拠した乱数ビット生成器が規定されています。これは、決定論的乱数ビット生成器（DRBG）として知られています。

DRBGをインスタンス化するには、CS_IV、CS_IN、CS_PVの3つのブルートゥース®
Channel Sounding 入力として指定する必要があります。ブルートゥース®
Channel Sounding 手順を実行すると、イニシエータ リフレクタ
両方のデバイスが、これらのパラメータに同じ値を持つようになります。同じパラメータ値で初期化された場合、DRBGの2つのインスタンスは一連の呼び出しでまったく同じビット・シーケンスを生成します。

Bluetooth®チャネル・サウンディングの場合、各デバイスは、モード0、モード1、およびモード3の各CSステップごとに、CS_Syncパケット内のアクセスアドレスフィールドを変更します。新しいアクセスアドレスの値は、DRBGを用いた選択ルールに基づいて生成され、両デバイスは相手側が使用するアクセスアドレスを把握しています。受信側はアクセスアドレスの値を確認し、問題がある場合はホストに報告します。

Accessアドレス フィールドは 32 ビット長で、4,294,967,296
個の異なる値を持つことができます。したがって、CS_Syncパケットを偽装しようとする悪意のあるデバイスが、交換される複数のCS_Syncパケットの各1つで正しいAccessアドレス
値を推測できる確率は、4,294,967,296分の1となります。

CS_Syncパケットには、オプションのランダムシーケンスフィールドを含めることができます。このフィールドは、RTT
サポートします。ランダムシーケンスフィールドの内容は、送信される各CS_Syncパケットごとに、CS
DRBGを使用して再生成されます。ランダムシーケンスフィールドの長さは、32ビット、64ビット、96ビット、または128ビットのいずれかです。

サウンディング・シーケンスは、32ビットまたは96ビットの予測可能な交互パターンで構成され、RTT
に使用されます。この既知のビットパターンが悪用されるリスクを軽減するため、DRBGを使用してシーケンス内の位置を選択し、マーカー信号と呼ばれる2つのランダムに選択された4ビット値のいずれかを挿入します。
DRBGによって選択されるマーカー信号の値は、0b1100または0b0011のいずれかである。ソーニングシーケンス内にランダムなビットパターンをランダムに挿入することで、ソーニングシーケンスのなりすましを防止する。

モード2およびモード3のステップには、トーン拡張スロットが含まれます。トーン拡張スロットは常に予約されていますが、そのタイムスロットで送信が行われるかどうかはランダム化されており、DRBGによって制御されます。受信端末は、トーン拡張スロットで送信が行われるタイミングと行われないタイミングを把握していますが、攻撃端末はそれを把握していません。

位相ベース測距中は、2つのデバイス間に存在するすべての利用可能なアンテナ経路を介してトーンが送信されます。使用される経路の順序は、Bluetooth®チャネルサウンディングの各ステップにおいてDRBGを用いてランダム化されます。

ソーンディング・シーケンスは、0と1のビット値が交互に並ぶシーケンスで構成されます。これに対応するRF信号は、周波数が異なり、位相も異なる2つのトーンから成るものと見なすことができます。
したがって、単一のCS_SyncパケットのSounding
Sequenceフィールドにエンコードされた2つのトーンの位相差を用いてPBR
を行うと同時に、そのCS_Syncパケットを用いて往復時間計算することができる。単一のパケットに基づいてRTT
PBR RTT PBR
同時に計算することで、この通信の解読を極めて困難にしようとするものである。

Bluetooth®チャネル・サウンディングリンクレイヤー
セクションには、攻撃検知システムの説明が含まれています。BluetoothコントローラにおけるBluetooth®チャネル・サウンディング攻撃の検知は、受信信号を基準信号の定義と照合して評価すること、および予期しないビット遷移や位相調整など、攻撃の可能性を示す兆候がないか受信信号を精査することに基づいています。

攻撃が進行中である確率を報告するための標準化された指標は、Bluetoothコア仕様書で定義されており、「正規化攻撃検知指標（Normalized
Attack Detector
Metric、NADM）」と呼ばれています。表13には、NADMの値の定義が記載されています。

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">NADM値</th>
<th class="has-text-align-left" data-align="left">項目</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">0x00</td>
<td class="has-text-align-left"
data-align="left">攻撃の可能性は極めて低い</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x01</td>
<td class="has-text-align-left"
data-align="left">攻撃の可能性は極めて低い</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x02</td>
<td class="has-text-align-left"
data-align="left">攻撃の可能性は低い</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x03</td>
<td class="has-text-align-left" data-align="left">攻撃は可能</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x04</td>
<td class="has-text-align-left"
data-align="left">攻撃の可能性が高い</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x05</td>
<td class="has-text-align-left"
data-align="left">攻撃の可能性は非常に高い</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0x06</td>
<td class="has-text-align-left"
data-align="left">攻撃の可能性は極めて高い</td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">0xFF</td>
<td class="has-text-align-left"
data-align="left">不明なNADM。ランダムシーケンスまたはサウンディングシーケンスを持たないRTT
デフォルト値。</td>
</tr>
</tbody>
</table>

*表13 - NADM値*

[{.aligncenter
.wp-image-234470 .size-1000w loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1000x693.png 1000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-600x416.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-2000x1386.png 2000w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-300x208.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-768x532.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1536x1065.png 1536w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-2048x1419.png 2048w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-450x312.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-660x457.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-800x554.png 800w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1200x832.png 1200w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38-1600x1109.png 1600w"
sizes="auto, (max-width: 1000px) 100vw, 1000px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_38.png)

*図39 - 攻撃検知システムの概要*

中間者（MITM）攻撃者が、正当な送信デバイスから部分的に受信したシンボルの値を予測し、正当な受信者が往復時間誤算するようにタイミングを操作した、生成済みの完全なバージョンのシンボルを中継するという、既知の物理層攻撃が数多く存在します。
帯域幅ビット製品 2.製品 LE 2M PHY では、シンボルパルスの持続時間が他の
PHY に関連するパルスよりも短いため、この種の攻撃のリスクが低減されます。

SNR機能 、イニシエータ レシーバー
、事前に合意した量のランダムノイズを信号に混入レシーバー
。これは、モード1（RTT）およびモード3（PBR）のステップ中に送信されるCS_Syncパケットにのみ適用されます。信号にノイズを混入させることで、攻撃者による解析の完了が困難かつ遅延し、その結果、そのような攻撃が成功する可能性が低くなります。
一方、SNRを事前に合意しているイニシエータ リフレクタ
、人為的に追加されたノイズを容易に除去することができます。

ブルートゥースコア仕様 GAP（Generic Access
Profile）セクションでは、セキュリティ・モードとセキュリティ・レベルを定義している。ブルートゥース®
Channel Sounding
4つのセキュリティレベルの正式な定義が含まれています。将来のBluetoothプロファイル仕様では、これらの定義が参照される可能性があります。

コントローラの実装者は、ベンダー固有のセキュリティ対策をさらに導入
することを選択できる。

ブルートゥース® Channel
Sounding、振幅ベースの攻撃耐性により、セキュリティ機能を強化します。正確な攻撃モデル、堅牢なDFTベースの検出指標、徹底した多段階テストレジメンを定義することで、認証されたデバイスが距離測定を操作する巧妙な試みを確実に検出できることを保証します。

HCIおよびリンクレイヤー 必要なアップデートと相まって、Channel Sounding
Amplitude-based Attack Resilience機能
、進化する脅威を軽減するための包括的なフレームワークを提供します。これは、Bluetoothのセキュリティに対するコミットメントを反映したものであり、新たな課題に直面しても高精度測距技術の正確性と信頼性を維持できるよう支援するものです。

ブルートゥース® Channel Sounding 機能 コントローラのブルートゥース®
Channel Sounding 機能を活用し、カスタム
のアプリケーション組み合わせることで、ブルートゥースの様々なアプリ
ケーションや製品を作成することができます。ソリューションのアプリケーション
コンポーネントの開発者は、このセクションで取り上げる様々な問題に注意する必要があります。

Bluetooth スタックは距離測定を直接生成しません。その代わり、Bluetooth
コントローラによる CS
ステップの実行中に、位相および/またはタイミングの低レベル測定が行われ、このデータからアプリケーションが距離測定を計算できます。

アプリケーションが距離計算に使用するアルゴリズムは、ブルートゥースコア仕様指定されていない。したがって、これはベンダーが差別化できる分野の1つです。優れたアルゴリズムは優れた結果を生む。

「ホスト・コントローラ・インターフェース機能仕様書」では、コントローラがBluetooth®チャネル・サウンディングデータをホストに渡す際に使用する2つのイベントを定義しています。これら2つのイベントは、「LE
CSサブイベント結果」および「LE CSサブイベント結果継続」と呼ばれます。

コントローラは、ブルートゥース® Channel Sounding 内で実行されたス
テップ中に生成された測定値を集約します。結果の完全なセットまたは部分的なセットは、LE
CS Subevent Result HCI
イベントを使用して報告されます。不完全なセットが報告される場合、結果の残りは、後で送信される
1 つ以上の LE CS
サブイベント結果コンティニュー・イベントで報告されます。HCI
イベント・フィールド Subevent_Done_Status と Procedure_Done_Status
は、レイヤに
対し、サブイベントまたはプロシージャーに関する全てのデータが報告されたのか、まだ続きが
あるのかをアプリケーション 。

[{.aligncenter
.wp-image-234471 .size-full loading="lazy" decoding="async"
srcset="https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39.png 924w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-600x394.png 600w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-300x197.png 300w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-768x504.png 768w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-450x295.png 450w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-660x433.png 660w, https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39-800x525.png 800w"
sizes="auto, (max-width: 924px) 100vw, 924px"}](https://www.bluetooth.com/wp-content/uploads/2024/10/Figure_39.png)

*図 40 -ブルートゥース® Channel Sounding HCI データ・レポートの例*

Bluetooth®チャネル・サウンディングHCIイベントは、コントローラからホストへ、さまざまな種類のデータを伝送します。ここでは、主要なフィールドとデータ構造の一部について説明します。

**周波数補正**---
モード0のステップの目的は、リフレクタ生成される目標周波数と実際の周波数の差を特定することです。これにより、周波数オフセット（FFO）が算出され、この値を用いて、周波数およびタイミング値に生じる影響を補正し、最終的に距離測定の精度を向上させることができます。

**Num_Steps_Reported**---
このフィールドは、このHCIイベントで報告されているステップ数を示します。また、ステップに関連する4つのデータ配列（Step_Mode、Step_Channel、Step_Data_Length、およびStep_Data）のサイズも示します。

**Step_Mode \[ \]**---
この配列には、各ステップのモードが、ステップ番号順に、0 ～ 3
の範囲の値として格納されています。

**Step_Channel \[ \]**---
この配列には、対応するステップの実行に使用されたRFチャネルのインデックスが含まれます。

**Step_Data_Length \[ \]**---
各ステップについて報告されるデータは、内容や構造が異なります。この配列には、関連する
Step_Dataエレメント 各エレメント の長さが格納されています。

**Step_Data \[ \]**---
各ステップで報告されるデータは、ステップモード、デバイスの役割（リフレクタ）、およびサウンディングシーケンスが使用されるかどうかに依存します。関連するデータを含む構造体は
Mode_Role_Specific_Info オブジェクトと呼ばれ、この構造体には 11
種類のバリエーションが定義されています。
含まれる可能性のあるデータの例としては、Packet_Quality、Tone_Quality、受信信号強度インジケータ（RSSI）、測定された周波数オフセット、NADM値、アンテナ識別子、位相補正項、およびパケットの送信から到着までの経過時間の測定値などが挙げられます。時間値は、0.5ナノ秒単位の倍数として表されます。

アプリケーション層は、どのステップモードを使用するかを決定する役割を担っており、プライマリモードとサブモードの両方が使用される場合、選択された各モードのステップ数の比率をどのように設定すべきかを決定します。アプリケーション製品
、結論を導き出すにあたり、距離測定の精度要件、セキュリティ、遅延に加え、ローカルコントローラがサポートする機能についても考慮する必要があります。

アプリケーション層は、モードの組み合わせやRTT
選択を通じて、ソリューション全体のセキュリティをある程度制御することができます。開発者は、採用すべきセキュリティオプションを決定する際の出発点として、まずGeneric
Access
Profile（GAP）で定義されているセキュリティレベルを理解し、評価するよう努めるべきです。

RTT 常に組み合わせてRTT
推奨します。これにより、これら2つの手法に基づく距離計算の相互検証が可能になります。PBR
Bluetooth®チャネル測深機能によってPBR
、最も正確な距離測定を実現します。一方、RTT
もサポートされている主な理由は、セキュリティ対策RTT 。

NADM値は、Bluetoothコントローラ内のNADMアルゴリズムによって作成され、これらの値に対して標準化された形容詞の形の意味が定義される。しかし、可能性のあるNADM値のそれぞれに対して（もしあれば）どのようなアクションを取るかを決定しなければならないのは、アプリケーション
である。

Bluetooth® チャネル・サウンディングは、コア仕様の更新に伴う段階的な機能
を通じて継続的に進化する、拡張可能なフレームワークとして設計されています。コアアーキテクチャと手順は共通の基盤を確立していますが、新たに特定された要件、運用上の考慮事項、または実装の改良に対応するため、将来的に追加機能が導入される可能性があります。
本節では、Core Specification v6.0 に含まれるバージョン 1
の機能の特定の側面を拡張する、Bluetooth®
チャネル・サウンディングの機能強化について要約します。チャネル・サウンディングは進化し続けるため、本節は将来の機能強化を盛り込むべく拡張される予定です。

Bluetooth Core Specification
バージョン6.2では、チャネル・サウンディングにおける距離測定に影響を与えるために振幅操作を利用する一連の測距攻撃に対する耐性が強化されています。これらの攻撃は、チャネル・サウンディング・パケットのシンボルタイミングに同期した周期的な増幅パターンを適用し、アナログ・フロントエンドにおける振幅から位相への変換レシーバー
予測可能な位相歪みを引き起こします。
このような挙動を検出するため、本仕様では、既存の正規化攻撃検出指標（NADM）フレームワークを、離散フーリエ変換（DFT）に基づく検出手法で拡張しています。このアプローチでは、周期的な振幅操作に特徴的なシンボル周波数およびその高調波におけるエネルギー成分を分析し、その結果得られた指標を既存のNADMレポートに組み込みます。
この機能強化により、特定のレシーバー
規定することなく、高度な早期コミット測距攻撃を検出するChannel
Soundingの能力が強化され、新たに特定された脅威ベクトルに対処しつつ、柔軟性を維持することが可能となる。

Bluetooth Core Specification バージョン 6.3
では、チャネル・サウンディングの位相ベースの測距手順の機能強化として、インライン位相補正項（inline
PCT）のサポートが導入されました。インライン PCT により、リフレクタ
再送信前に無線処理チェーン内で位相補正項を適用することが可能となり、イニシエータ側ですべての位相補正をデジタル処理する必要なく、位相整合された信号の転送を実現します。
位相補正をインラインで組み込むことで、このメカニズムは、基本的な双方向チャネル・サウンディング測定モデルを維持しつつ、位相誤差補正に伴う制御および報告のオーバーヘッドを削減できます。インラインPCTのサポートはオプションであり、デバイス間でネゴシエーションされるため、イニシエータデジタル位相補正に依存する実装との相互運用性が維持されます。詳細については、[Bluetooth®
Core Specification
rel="noreferrer noopener"}を参照してください。

Bluetooth Core Specification バージョン6.3では、RTT
宣言を導入することで、チャネル・サウンディングによる往復伝送時間（RTT）の測定機能が強化されました。この機能強化以前は、シンボルレートやタイミング特性が異なるにもかかわらず、デバイスはサポートするすべてのPHYに一律に適用される単一RTT
値を報告していました。 更新されたメカニズムにより、デバイスはLELE
2Mオプションの高レートPHYを含め、各PHYごとに個別にRTT
要件を宣言できるようになります。これにより、RTT
と各PHYで達成可能なタイミング精度との整合性がより正確になり、マルチPHY環境における効率性と一貫性が向上します。
この機能強化は、リンクレイヤー
およびバージョン管理されたホストコントローラインターフェース（HCI）コマンドを通じてサポートされ、従来の実装との相互運用性を維持しています。詳細については、[『Bluetooth®
Core Specification
rel="noreferrer noopener"}参照してください。

ブルートゥース® Channel Sounding
機能導入にあたり、ブルートゥースコア仕様いくつかのレイヤーに変更が加えられました。この章では、主要な変更点を要約し、章ごとのハイレベルなリファレンスを提供することで、オリエンテーションのみを目的としています。詳細についてはブルートゥースコア仕様
参照されたい。

ブルートゥースコア仕様
第1巻パートAには、この技術のアーキテクチャが記述されている。

- 第3節「トランスポートアーキテクチャ」では、Bluetooth®チャネルサウンディング向けの新しいパケット構造とシグナリング形式について説明します。また、新しいLEチャネルサウンディング物理チャネルおよびLEチャネルサウンディング物理リンクについても定義しています。
- 第9章「Bluetooth Low Energy を使用した Bluetooth®
チャネル・サウンディング」では、Bluetooth®
チャネル機能について簡単にまとめています。

第3巻パートCでは、Generic Access Profileを定義している。

- 第9節では、GAP
Bluetooth®チャネル・サウンディングの手順と、イニシエータ
リフレクタの役割について解説します。
- 第10節では、Bluetooth®チャネル・サウンディングの4つのセキュリティレベルを定義しています。

第4巻パートEには、Host 機能仕様が含まれる。

- セクション7.7.6.5「LE Metaイベント」が更新され、LE
CSサブイベント結果イベントやLE
CSサブイベント結果継続イベントなど、Bluetooth®チャネルサウンディングに関連するさまざまな新しいイベントタイプが追加されました。
- セクション7.8「LEコントローラコマンド」には、チャンネル・サウンディングで使用するための追加コマンドが追加されました。これには、「LE
CS Read Remote FAE Table」コマンド、「LE CS Create
Config」コマンド、「LE CS Security Enable」コマンド、および「LE CS
Procedure Enable」コマンドが含まれます。

第6巻パートAには物理層仕様が含まれている。

- 第 1 章では、新しいLE 2M 2BT PHY を紹介する。
- セクション2では、ブルートゥース® Channel
Sounding新しいチャンネル配置を紹介する。
- セクション3では、新しいSNRコントロール機能定義する。
- セクション3.4は、ブルートゥース® Channel
Soundingサポートする機器に対する安定位相要件を追加する。
- セクション 3.5 では、ブルートゥース® Channel
Sounding周波数測定と生成の要件について説
明する。これには、分数周波数オフセット（FFO）測定要件の仕様が含まれる。
- セクション5.3は、ブルートゥース® Channel
Soundingためのアンテナ切り替えについて説明する新しいセクションである。
- 第 6 章では、位相測定の要件について説明し、基準レシーバー
定義、位相測定の精度要件、周波数作動誤差補正要件、および位相測定のタ
イミング規則について説明します。
- 付録Bは、ブルートゥース® Channel
Soundingための試験装置のセットアップ例を示しています。

第6巻パートBには、リンクレイヤー 仕様書が収録されている。

- セクション2.4.2では、ブルートゥース® Channel Sounding 機能
関連する新しいリンクレイヤー
PDUタイプと、そのオペコードを定義している。
- 第4節には、Bluetooth®チャネル・サウンディングリンクレイヤー
更新内容が記載されている。これには、第4.2節におけるスリープクロックの精度要件の更新、および第4.5.18節におけるBluetooth®チャネル・サウンディングの手順、イベント、サブイベント、およびステップに関する仕様が含まれる。Bluetooth®チャネル・サウンディングに関連するACLリンクおよびそれが伝送する可能性のある制御PDUに対するセキュリティ要件は、第4.5.18.2節に規定されている。
- セクション5.1では、リンクレイヤー
コントロールについて説明している。ブルートゥース® Channel Sounding
開始手順、ブルートゥース® Channel Sounding
能力交換手順、ブルートゥース®Channel Sounding
設定手順など、ブルートゥース® Channel
Sounding関連する新しい制御手順を含むように更新された、ブルートゥース®
ブルートゥース® Channel Sounding 開始手順、ブルートゥース® Channel
Sounding 能力交換手順、ブルートゥース® Channel Sounding
設定手順、ブルートゥース® Channel Sounding
開始手順など、ブルートゥース® Channel Sounding
関連する新しい制御手順が含まれています。

第6巻パートHは、新しいブルートゥース® Channel Sounding
機能特化した新しいセクションです。ブルートゥース® Channel
Sounding使用される物理RFチャネルの定義、新しいCS_Syncパケット・フォーマット、RTT測定、到着時刻または出発時刻のタイムスタンプを取得するさまざまな方法について説明しています。このセクションでは、ブルートゥース®
Channel Sounding 新しいチャネル選択アルゴリズ
ム、ステップ・モード、ステップの組み合わせとシーケンス・ルール、位相測定ルール、DRBG
を使用したランダム・ビット生成について定義します。

ブルートゥース® Channel
Sounding使えば、開発者は、機能安全なファイン・レンジング機能を活用したエキサイティングな製品やアプリケーションを開発することができます。

世界で最もユビキタスな低消費電力無線技術をベースとする紛失防止
およびデジタル・キー・ソリューションのエンドユーザーは、ブルートゥース®
Channel Sounding
機能使用するデバイスで達成できる結果の品質により、パフォーマンスの向上を享受できます。また、製品
開発者には、関連する問題にアドレス
するための包括的なセキュリティ機能が提供されているため、安心してお使いいただけます。

ブルートゥース® Channel Sounding
技術的な柔軟性は、開発者がセキュリティ、精度、レイテンシなど、最も重要な測距の側面を優先できることを意味します。ブルートゥース®
機能、すべてのアプリケーションに同じ機能があるわけではありません。開発者には、自社製品の実装において、開発者とユーザーにとって何が最も重要かを決定する自由が与えられています。

毎年50億台以上のBluetooth対応機器が出荷されている。その結果、大規模なスケールメリットが生まれ、製品
メーカーや部品メーカー、ひいてはその顧客に利益をもたらしています。

ブルートゥース® Channel Sounding
安全な高精度測距機能により、多くのBluetooth接続デバイスの利便性、安全性、セキュリティを向上させることができます。プレゼンス検出、方向検知そして今channel
sounding それぞれを個別に、または組み合わせて使用することで、エンド
ユーザーや企業がメリットを享受できる空間認識型製品やアプリケーションを作成できます。

Bluetooth技術はすでに広く普及しており、広く採用され、綿密に規定された技術規格に基づいています。Bluetooth®
Channel
Soundingを採用することは、Bluetooth製品に高精度測距機能を追加したいと考えている開発者にとって、簡単かつ確実な選択肢となります。Bluetooth技術の豊富な機能群に加わったこの画期的な新機能の詳細については、Bluetoothコア仕様書をダウンロードしてご確認ください！

<table class="has-fixed-layout">
<thead>
<tr>
<th class="has-text-align-left" data-align="left">項目</th>
<th class="has-text-align-left" data-align="left">所在地</th>
</tr>
</thead>
<tbody>
<tr>
<td class="has-text-align-left" data-align="left">Bluetooth® コア仕様
v6.0</td>
<td class="has-text-align-left" data-align="left"><a
href="https://www.bluetooth.com/specifications/specs/core60-html/">https://www.bluetooth.com/specifications/specs/core60-html/</a></td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">プロフィール</td>
<td class="has-text-align-left" data-align="left"><a
href="https://www.bluetooth.com/specifications/specs/find-me-profile-1-0/">https://www.bluetooth.com/specifications/specs/find-me-profile-1-0/</a></td>
</tr>
<tr>
<td class="has-text-align-left" data-align="left">即時警報サービス</td>
<td class="has-text-align-left" data-align="left"><a
href="https://www.bluetooth.com/specifications/specs/immediate-alert-service-1-0/">https://www.bluetooth.com/specifications/specs/immediate-alert-service-1-0/</a></td>
</tr>
</tbody>
</table>

**脚注**

*1.汎用属性プロファイル\
2.速度は、信号が通過する物質によって異なります。ただし、理論計算では光速を用いるのが一般的です。\
3.CSモードについては、セクション3.5で説明されています\
4.ガウス周波数変調*
