# thread_0133: [内部連絡] Re: 【ALAP】[UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議

- Message count: 5
- Source JSON: `thread_0133.json`

---

## 1. 2025-09-03 02:55

**From:** Itsuo Sakai
**To:** Jun Wang

王さんお疲れさまです。

以下のように回答してください。

酒井ーーーー
Q366226のSubset作成についてですが、「RF 1/1 Power Class 1」はNoにする必要はございませんでしょうか？現在Yesになっています。

⇒再度確認したところQ366226はQ社にしては珍しくRF PHYを含んだ登録でした。

Subsetの依頼ではLLだけではなく「RF 1/15 Power Class 1:YES→NOも併せてご依頼ください。

ーーーー差出人: Shigeyuki Sakai

送信日時: 2025年9月3日 11:43

宛先: Jun Wang

件名: RE: 【ALAP】[UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

すみません、質問を追加させてください。

[ID] の Subset 作成についてですが、「RF
1/1 Power Class 1」は No にする必要はございませんでしょうか？現在 Yes になっています。

お手数ですが、こちらもご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 8:52 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

ご回答どうもありがとうございました。

[ID] の Subset 作成は急ぎ Qualcomm/Volvo へ説明し、対処するようにします。

LE のオプション機能についても理解いたしました。ご解説、大変助かります。

もし、 LE 2M PHY を付ける場合、試験期間と費用はどのくらい変化しますでしょうか？

酒井

From: Jun Wang

Sent: Tuesday, September 2, 2025 10:37 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井さんいつもお世話になります。アリオンの王君です。

標記 Bluetooth 認証登録につき、 Q 社 DN 情報の共有ありがとうございます。

以下いただいたご質問をインラインにて回答させていただきますので、

青字部分ご参照願います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 1, 2025 8:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo から使用する DN の正式情報を入手しましたので、見積依頼書と共にご連絡いたします。

Volvo で Host や X2Core に独自に追加するものは無く、 Qualcomm より提供された DN
[ID] をそのまま使用するとのことです。

なお、 Chip の Component
DN も新しいものが連絡されてきました。 [ID] です。

Consistency check、必要試験の特定に進みたいのですが、その前に、以下の気になる点について確認させてください。

製品は Power Class 2 で認証取得したいのですが、 [ID] の LL
ICS 9/11 が YES です。そうすると、 HM26 のときにあった、 Power
Class の不整合問題に該当しますか？やはり。

回答：

はい、 [ID] を Include し、 RF PHY は SoC を製品基板に直実装のために必要な試験を実施するので

RF PHY 1/15:NO への変更は問題ありませんが、併せて必要な LL 9/11： NO へ変更すると

LL ICS に紐付いた全試験項目が Test Plan
として出力されます。

そこで購入契約者 (V 社あるいは御社 ) から Q 社へ「[ID] の RF PHY 1/15:NO および

LL ICS 9/11:NO の Subset を作成 （SIG への支払は無料） して欲しい」と要求してください。

・見積依頼書内の“ RF PHY の必須機能以外のサポート機能“について、以下、確認させていただきたいです。

どれが必要な機能か、上記 DN から特定可能でしょうか？

回答：

Include する DN の内容で RF PHY の試験範囲が決まるのではなく、製品組込アプリがどこまでサポートしているかにより決定します。

車載器では見かけ上の伝搬速度を下げて遠くへ伝達させる Coded は不要かつ Stable xxx は不要かと思います。

2Mbps は対向相手がサポートしていると自動でネゴシエートされますので使う可能性が高いです。

したがって必須 1M と 2M の試験実施でよろしいかと思います。

最終判断は製品アプリの開発担当部門へご確認ください。

また、今回不要な機能があったとしても、将来 Host 側に更新が入った場合に備え、 Controller 側では予備的に認証を取得しておく考え方はありますでしょうか？

回答：

もし Q 社が Host [ID] のアップデートが予想され、 V 社もそれに追従しそうな場合には、

予備的に Controller 部の部分登録・認証を取得しておけば将来のアップデート登録が楽に済みます。

以上、ご確認をよろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, August 22, 2025 6:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記状況共有させていただきありがとうございます。

Q 社 DN が取得でき次第またご展開いただきますようお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 10:53 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

時間が空いてしまい、申し訳ございません。

Q 社の DN 情報について、現状をご連絡させていただきます。

弊社スウェーデンの現地法人を経由して、正式見積もりおよび認証開始に向けて、

V 社に対して、 Q 社から X2Core 及び Core
complete(Host) の DN 情報を早急に入手するように依頼しております。

入手でき次第に早急に展開させていただきますのでお待ち下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 8, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ICS (Implementation Conformance Statements) は申請製品の機能記述として、

included する Q 社 core complete の DN 及び X2Core の DN 情報がないと、

免除できる試験項目を確定できず、見積のご提示が難しいです。

今回の試験内容的に、 RF/RF PHY 試験は Q 社登録に不含ですので見積依頼書の P2 の記載内容で確定していますが、

プロファイルは X2Core
の登録内容と製品の実装内容の差異が明確にならないと確定見積ができません。

敢えて製品実装プロファイルは X2Core 登録でカバーされ、製品でのプロファイル試験は発生しないという前提条件付の場合、見積は下記となります。

合計
￥ 2,600,000 （税抜）

内訳、

・ RF フル項目試験・・・　￥ 1,200,000

・ RF PHY(1M, 2M, Stable Mod Index-Tx,Stable Mod Index-Rx ) 試験・・・　￥ 1,000,000

・代行登録サポート (Multi-Design) ・・・　￥ 250,000

・コンプライアンスフォルダ作成費・・・・・・　￥ 150,000

Q 社 DN が明確になり次第、必ず費用見積を見直しさせていただきますので、

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 木曜日 , 8 月
7, 2025 8:23:11 午後宛先 : Jun Wang

件名 : RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

DN 提供が出来ておらず、申し訳ございません。

DN が無い場合、 ICS でもお見積りが可能とのお話しを弊社深浦より聞きました。

ICS は V 社経由で今週中に弊社に展開される予定ですが、現時点では展開されておりません。

今週まで V 社、および弊社含めて多くのメンバーが夏休みである為、来週中に展開される可能性が高いです。

弊社のスウェーデン現法メンバーに対して、来週中に途中段階でも良いので ICS を入手できるように依頼をします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, August 6, 2025 9:52 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

Q 社二つの DN とも取得中ということで現時点確定的な DN 情報がない、

という状態になります。

折角見積依頼書をいただきまして大変申し訳ございませんが、

費用見積のご提示がない状況となります。

Q 社 DN 取得でき次第で情報を展開いただきますと、

費用見積りのご提示が可能となりますので、

それまで少しお待ちいただきますようお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 6:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お問い合わせの件、ご回答させていただきます。

まだ Q 社で DN 取得中、との理解でよろしいでしょうか。

はい、ご認識あっております。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

現在、 V 社より、 w36(9/1 ～ 9/5) で利用可能になるとの連絡を受けております。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, August 5, 2025 4:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々すみません。

いただいた Bluetooth 見積依頼書では、 Host Stack に関して

TBD とご記入されていますが、

まだ Q 社で DN 取得中、との理解でよろしいでしょうか。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, August 5, 2025 2:37 PM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth 見積依頼書の更新をいただきありがとうございます。

BQC に試験対象項目を確認し、費用見積をご提示いたしますので、

少々お待ちくださいませ。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 8:30 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

対応が遅くなり、申し訳ございません、

Bluetooth 見積書を更新しました。

補足としては、以下になります。

・ Core-controller の DN を取得したい・以下の DN を include して End product を登録したい取得した Core-controller の DN

Qaulcomm から提供された、 RF/RF PHY が除かれた Core-Complete
DN

Qaulcomm から提供された、 X2Core DN

・ RF PHY の必須機能以外のサポート機能は仮で記入した状態こちらの内容でお見積りをお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, July 30, 2025 12:27 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

お忙しい中ご返信いただきありがとうございます。

RF/RF PHY の再試験を避ける為、 Core-Controller の DN を取得する方向で進めたいと思います。

弊社提案に合意をいただきありがとうございます。

現時点で埋められる部分を埋めて、 ICS 作成を進めるようにします。

ICS は登録内容を確定するためのものとして、

まずは見積書をご用意するにあたり、見積依頼書のご記入（更新）をお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 29, 2025 6:20 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございました。

また、こちらからの返信がかなり遅くなってしまい、申し訳ございません。

アリオン：はい、 Core-Controller の DN を取得のために 1 件の登録費用が発生しますが、

将来的に Q 社登録が更新されても御社名義の DN を Include することで再試験は回避できます。

承知しました。

RF/RF PHY の再試験を避ける為、 Core-Controller の DN を取得する方向で進めたいと思います。

アリオン：はい、登録内容を確定するという目的からは ICS レベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須 (1Mbps) および 2Mbps」という具合に仮入力をお願いします。

承知しました。

現時点で埋められる部分を埋めて、 ICS 作成を進めるようにします。

また、 Bluetooth と Wi-Fi は別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

承知しました。 ( 賛成です )

取り急ぎ、本メールタイトルから「Wi-Fi Alliance」を外しました。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 1:02 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth 認証に関する補足情報、また追加でいただいたご質問について、

下記回答させていただきます。※ 青字ご参照願います。

また、 Bluetooth と Wi-Fi は別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

アリオン：承知いたしました。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

アリオン：原則的には Include する Core-Controller の DN が変われば再度 RF/RF PHY 試験を実施することになります。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

アリオン：はい、 Core-Controller の DN を取得のために 1 件の登録費用が発生しますが、

将来的に Q 社登録が更新されても御社名義の DN を Include することで再試験は回避できます。

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

アリオン：はい、登録内容を確定するという目的からは ICS レベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須 (1Mbps) および 2Mbps」という具合に仮入力をお願いします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:20 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々失礼いたします。

費用見積に関して訂正させていただきます。

7/22 日付の見積には Submission Fee を含めていないため、下記訂正させていただきます。※ 青字ご参照

AP

Staion

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDV を含む )

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$63,640

61

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:11 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

王君の説明不足で混乱させたようで申し訳ございません。

3 ヵ月プランは基本形となっており、 Wi-Fi 6/6e、 Easymesh 等 Wi-Fi
Feature の複雑化に従い、

Wi-Fi 認証試験の L/T も延びている状況となっている中、

3 ヵ月プランも DUT の Wi-Fi Feature の複雑度及び受験サンプル台数を基に調整しております今回の UXC は対象 Wi-Fi Program も多いため、

サンプルを 2 ～ 3 セットのご提供をお願いいたしたいですが、

その場合、 AP と Station を各 1 台で試験を実施し、各 3 ヵ月の有効期限とさせていただきたいと考えます。

いかがでしょうか。

弊社側で記入を進め、 V 社に確認すべき部分は確認の上、提出とさせていただきます。

但し、 V 社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は 8 月下旬になる可能性が高いです。

弊社の Wi-Fi 見積依頼書の内容は概ねいただいている WorkSheet の Step3 Certification、一部 Step4 Capability の内容となりまして、

まずは現時点で確定となっている内容だけの整理で構いませんので、お願いができますと幸いです。

Ｖ社夏休み明けに確認必要な内容整理にもなると思います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 22, 2025 8:56 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お返事をいただき、ありがとうございました。

ü
お見積りをいただいた WFA プログラム (2.4/5GHz) の場合、 1 回の試験でどれくらいの LT 想定になるか、情報を展開いただく・・・ Allion
王様

⇒　試験費用や標準日程を Wi-Fi Program 別に整理いたしました、ご参照願います。

※下記試験費用や日程には、 Mandatory
項目しか含めておりません；

実際 DUT が Optional 項目もサポートし、 CID として登録内容に含めたい場合、試験費用や日程も変わります。

※下記 Test L/T は標準の Lead Time として、再試験は含んでおりません。

Test LT に関して、念のために認識合わせをさせて下さい。

現在、三か月プランでのお見積りをいただいていると思いますが、現在の試験プログラムの合計 Test LT は 61 日になっております。

一月の稼働日を 20 ～ 22 日で計算した場合、三か月は最大でも 66 日程度になる為、基本的には再試験をする日数は無いと認識しました。

こちらの認識はあっているでしょうか？

ü
Android OS
バージョンアップが WFA 試験に影響するかについて、関連する WFA からの公開情報を展開いただく・・・ Allion
王様

⇒　ラボに確認いたしますので少々お待ちください。

お手数ですが、ご確認をお願いします。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi 新規認証（New Certification）

御社フォームの WorkSheet をいただいておりますが、

VCC Comment、 QC Comment も併記されている中、現時点の最終仕様で添付の「Wi-Fi 認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

承知しました。

弊社側で記入を進め、 V 社に確認すべき部分は確認の上、提出とさせていただきます。

但し、 V 社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は 8 月下旬になる可能性が高いです。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 7:48 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

先週の打ち合わせ、お時間ありがとうございました。

製品サンプルを拝見できて、より働く価値を身に感じまして、感謝いたします。

Bluetooth に関して、確認して別途回答いたします。

Wi-Fi に関して下記二点弊社側の宿題事項について下記回答いたします。

ü
お見積りをいただいた WFA プログラム (2.4/5GHz) の場合、 1 回の試験でどれくらいの LT 想定になるか、情報を展開いただく・・・ Allion
王様

⇒ 試験費用や標準日程を W i-Fi Program 別に整理いたしました、ご参照願います。

※下記試験費用や日程には、 Mandatory
項目しか含めておりません；

実際 DUT が Optional 項目もサポートし、 CID として登録内容に含めたい場合、試験費用や日程も変わります。

※下記 Test L/T は標準の Lead Time として、再試験は含んでおりません。

AP

Station

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDV を含む )

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$58,640

61

ü
Android OS
バージョンアップが WFA 試験に影響するかについて、関連する WFA からの公開情報を展開いただく・・・ Allion
王様

⇒　ラボに確認いたしますので少々お待ちください。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi 新規認証（New Certification）

御社フォームの WorkSheet をいただいておりますが、

VCC Comment、 QC Comment も併記されている中、現時点の最終仕様で添付の「Wi-Fi 認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, July 18, 2025 3:40 PM

To: Jun Wang

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

昨日は遠い中、弊社までお越しいただき、ありがとうございました。

Bluetooth 認証登録書、 Wi-Fi 新規認証（New Certification）につきましては、弊社側で最新内容に更新します。

Bluetooth 認証登録書の更新にあたり、何点かご確認した内容があります。以下の質問に対して、ご回答をお願いできますでしょうか？

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

Wi-Fi 認証の事前試験については、アリオン様でお見積り済みの LT 情報も踏まえて、判断したいと考えています。

以下は昨日の議事メモ内になります。 ( 黄色塗りつぶしは宿題事項となっております )

その中でも依頼事項として記載しておりますのでご展開をお願いします。

【[ID]】

ü
試験拠点は以下の通り。

Ø
PTS IOPT :
日本

Ø
Controller(PHY) :
日本 or
中国 or 台湾　※ [ID] 見積依頼書の内容を基に Allion 様側で判断予定。

ü
想定される試験期間は以下の通り。 (= 現状、それぞれ三か月を見込んでいる為、計画内で完了する見通し )

Ø
PTS IOPT : 2~3 回の不具合修正 / 再テスト含めて、 8 週間。 (IOPT だけなので更に短い LT で完了できる見通し )

Ø
Controller(PHY) :
一か月 (MAX)

ü
見積依頼書を更新して Allion 様に提出する・・・ ALAP
水野

【WFA】

ü
WFA 認証プランは三か月プランが一般的であり、先日頂いたお見積りも三か月プランの費用になる。

Ø
1 回目の試験は、 NG が出ても試験できる項目を全て通して実施する。 (NG により試験出来ない項目は Skip)

Ø
2 回目の試験は、基本的に NG 項目を再試験するが、 NG 項目に関連する項目は再試験する場合もあり。

ü
お見積りをいただいた WFA プログラム (2.4/5GHz) の場合、 1 回の試験でどれくらいの LT 想定になるか、情報を展開いただく・・・ Allion
王様

ü
試験場所は、中国 or
台湾になる。 ( 基本的には台湾が多くの試験設備を保持している為、台湾になる見込み )

ü
事前検証を Allion 様に依頼する場合、全ての項目を依頼するか、 V 社と協議の上、心配項目を依頼するか、判断する・・・ ALAP
水野

ü
Android OS
バージョンアップが WFA 試験に影響するかについて、関連する WFA からの公開情報を展開いただく・・・ Allion
王様

Ø
Volvo に Android OS のバージョンアップが WFA 認証に影響することを説明するために利用したい以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, July 18, 2025 10:29 AM

To: 水野淳也 Junya Mizuno ;
酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様、酒井様いつもお世話になります、アリオンの王君です。

昨日はお忙しい中お時間をいただきありがとうございました。

UXC の開発及び Bluetooth ＆ Wi-Fi 認証に向けた最新日程の共有、ありがとうございます。

·
Bluetooth 認証登録

24 年 9 月にいただきました見積依頼書を添付いたします。

ご更新いただき、弊社より試験対象項目及び見積をご提示いたしますので、よろしくお願いいたします。

·
Wi-Fi 新規認証（New Certification）

御社フォームの WorkSheet をいただいておりますが、

VCC Comment、 QC Comment も併記されている中、現時点の最終仕様で添付の「Wi-Fi 認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

·
Wi-Fi 認証の事前試験に関して、御社別部隊からもよく「事前試験＋本番試験」でご依頼をいただいております。

本番試験をスムーズに進められるように、事前に一通り試験を回しておく、

もしくは一部気になる Program/ 項目を確認しておくことをお勧めいたします。

·
CSD に関して、いろいろご調整いただき誠にありがとうございます。

CSD を除いた DUT 本体やケーブル類は本社日本から、 CSD は御社中国から、

ご提供される予定との旨、承知いたしました。

試験に向けて引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

-----Original Appointment-----

From: Jun Wang On Behalf Of Junya Mizuno

Sent: Thursday, July 17, 2025 12:59 PM

To: Doyen

Subject: FW: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議

When: 2025 年 7 月 17 日木曜日 13:00-14:00
(UTC+09:00) 大阪、札幌、東京

Where: 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議差出人 : Junya Mizuno

送信日時 : 2025 年 7 月 8 日 16:55:10
(UTC+09:00) Osaka, Sapporo, Tokyo

宛先 : Junya Mizuno ;
Jun Wang ;
Itsuo Sakai ;
Shigeyuki Sakai ;
Hiroaki Fukaura

件名 : [UXC] VCC UXC モデル向け Bluetooth
SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議開催日 : 2025 年 7 月 17 日 13:00
- 14:00。

場所 : 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議アリオン王様、酒井様いつもお世話になっております。アルプスアルパインの水野です。

大変遅くなってしまい申し訳ございません。

V 社ソフトリリース日程、 Display(CSD) 入手見込みが固まってきましたので、

最新状況を反映した Bluetooth SIG/Wi-Fi Alliance 認証計画を作成中です。

最新認証計画を基に、認証計画の共有、認証に向けた段取りの協議をさせて下さい。

※最新認証計画は 7/11( 金 ) までに送付させていただきます。

以上です。

宜しくお願いします。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
460 795 130 830 7

パスコード :
db6Xf3X4

開催者向け :
会議オプション

________________________________________________________________________________

---

## 2. 2025-09-03 05:16

**From:** Itsuo Sakai
**To:** Jun Wang

王さんお疲れさまです。

質問には以下のように回答してください。

酒井ーーーー
IOPT試験は不要でよろしいですか？

⇒製品がサポートするプロファイルがQ370647（Qualcomm Android V Auto Core Host）

によりICSレベルで包含されている場合、IOPT試験はQPRDv4(7/21発効)の規定で不要になりました。
お見積りには、RF試験は含まれておりますでしょうか？（RF PHY試験だけでなく）

⇒失礼しました。RF試験が抜けておりました。

・RFフル項目試験・・・・・・・・・・・　￥1,200,000

・RF PHY試験(1M, 2M)　・・・・・・・・・・　￥700,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・　￥150,000
RF PHY試験の、1M＆2M両方を試験する場合と 1Mだけを試験する場合の2つのお見積りを頂くことできますでしょうか。

⇒RF PHY試験(1M)の場合の見積は以下の通りです。なお、製品がQ370647（Qualcomm

Android V Auto Core Host）のサポートプロファイルを実装する前提では、[ID]

にBLEのGATT Base Profileはないため2Mの試験は必須ではありません。もし独自

BLEプロファイル(128bit UUID)をサポートする場合に上記1M, 2Mの試験となります。

・RFフル項目試験・・・・・・・・・・・　￥1,200,000

・RF PHY試験(1M)　・・・・・・・・・・・・　￥400,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・　￥150,000

ーーーー差出人: Shigeyuki Sakai

送信日時: 2025年9月3日 13:45

宛先: Jun Wang

件名: RE: 【ALAP】[UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

費用のお見積り、ありがとうございます。 Power Class1 の問題は対処するとして、以下を確認させてください。

IOPT 試験は不要でよろしいですか？ DUT やマニュアルの準備に関わることから、念のため確認したいです。
お見積りには、 RF 試験は含まれておりますでしょうか？（RF
PHY 試験だけでなく）
RF PHY 試験の、 1M ＆ 2M 両方を試験する場合と
1M だけを試験する場合の 2 つのお見積りを頂くことできますでしょうか。先述しました“予備的に 2M を試験するか？”の判断材料にしたいためです。

Power Class1 の件、ご確認ありがとうございます。 [ID] を以下のように変更した Subset を作ってもらうよう Qualcomm へ依頼します。

LL 9/11 LE Power Class 1 : YES→NO

RF 1/1 Power Class 1 : YES→NO

RF PHY 1/15 Power Class 1 : YES→NO

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:22 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

費用について、いただいた Q 社 DN を基に、見積を下記更新いたします。

合計：￥ 1,100,000 （税抜）

内、

・ RF PHY 試験 (1M, 2M) ・・・・・・　￥ 700,000

・代行登録サポート (Multi-Design 参照 ) ・・・　￥ 250,000

・コンプライアンスフォルダ作成費・・・・・・　￥ 150,000

下記追加でいただいたご質問ですが、

再度確認いたしまして、 [ID] は Q 社にしては珍しく RF PHY を含んだ登録でした。

Subset の依頼では LL だけではなく RF 1/15 Power
Class 1:YES → NO も併せてご依頼ください。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 11:43 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

すみません、質問を追加させてください。

[ID] の Subset 作成についてですが、「RF
1/1 Power Class 1」は No にする必要はございませんでしょうか？現在 Yes になっています。

お手数ですが、こちらもご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 8:52 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

ご回答どうもありがとうございました。

[ID] の Subset 作成は急ぎ Qualcomm/Volvo へ説明し、対処するようにします。

LE のオプション機能についても理解いたしました。ご解説、大変助かります。

もし、 LE 2M PHY を付ける場合、試験期間と費用はどのくらい変化しますでしょうか？

酒井

From: Jun Wang

Sent: Tuesday, September 2, 2025 10:37 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井さんいつもお世話になります。アリオンの王君です。

標記 Bluetooth 認証登録につき、 Q 社 DN 情報の共有ありがとうございます。

以下いただいたご質問をインラインにて回答させていただきますので、

青字部分ご参照願います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 1, 2025 8:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo から使用する DN の正式情報を入手しましたので、見積依頼書と共にご連絡いたします。

Volvo で Host や X2Core に独自に追加するものは無く、 Qualcomm より提供された DN
[ID] をそのまま使用するとのことです。

なお、 Chip の Component
DN も新しいものが連絡されてきました。 [ID] です。

Consistency check、必要試験の特定に進みたいのですが、その前に、以下の気になる点について確認させてください。

製品は Power Class 2 で認証取得したいのですが、 [ID] の LL
ICS 9/11 が YES です。そうすると、 HM26 のときにあった、 Power
Class の不整合問題に該当しますか？やはり。

回答：

はい、 [ID] を Include し、 RF PHY は SoC を製品基板に直実装のために必要な試験を実施するので

RF PHY 1/15:NO への変更は問題ありませんが、併せて必要な LL 9/11： NO へ変更すると

LL ICS に紐付いた全試験項目が Test Plan
として出力されます。

そこで購入契約者 (V 社あるいは御社 ) から Q 社へ「[ID] の RF PHY 1/15:NO および

LL ICS 9/11:NO の Subset を作成 （SIG への支払は無料） して欲しい」と要求してください。

・見積依頼書内の“ RF PHY の必須機能以外のサポート機能“について、以下、確認させていただきたいです。

どれが必要な機能か、上記 DN から特定可能でしょうか？

回答：

Include する DN の内容で RF PHY の試験範囲が決まるのではなく、製品組込アプリがどこまでサポートしているかにより決定します。

車載器では見かけ上の伝搬速度を下げて遠くへ伝達させる Coded は不要かつ Stable xxx は不要かと思います。

2Mbps は対向相手がサポートしていると自動でネゴシエートされますので使う可能性が高いです。

したがって必須 1M と 2M の試験実施でよろしいかと思います。

最終判断は製品アプリの開発担当部門へご確認ください。

また、今回不要な機能があったとしても、将来 Host 側に更新が入った場合に備え、 Controller 側では予備的に認証を取得しておく考え方はありますでしょうか？

回答：

もし Q 社が Host [ID] のアップデートが予想され、 V 社もそれに追従しそうな場合には、

予備的に Controller 部の部分登録・認証を取得しておけば将来のアップデート登録が楽に済みます。

以上、ご確認をよろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, August 22, 2025 6:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記状況共有させていただきありがとうございます。

Q 社 DN が取得でき次第またご展開いただきますようお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 10:53 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

時間が空いてしまい、申し訳ございません。

Q 社の DN 情報について、現状をご連絡させていただきます。

弊社スウェーデンの現地法人を経由して、正式見積もりおよび認証開始に向けて、

V 社に対して、 Q 社から X2Core 及び Core
complete(Host) の DN 情報を早急に入手するように依頼しております。

入手でき次第に早急に展開させていただきますのでお待ち下さい。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 8, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ICS (Implementation Conformance Statements) は申請製品の機能記述として、

included する Q 社 core complete の DN 及び X2Core の DN 情報がないと、

免除できる試験項目を確定できず、見積のご提示が難しいです。

今回の試験内容的に、 RF/RF PHY 試験は Q 社登録に不含ですので見積依頼書の P2 の記載内容で確定していますが、

プロファイルは X2Core
の登録内容と製品の実装内容の差異が明確にならないと確定見積ができません。

敢えて製品実装プロファイルは X2Core 登録でカバーされ、製品でのプロファイル試験は発生しないという前提条件付の場合、見積は下記となります。

合計
￥ 2,600,000 （税抜）

内訳、

・ RF フル項目試験・・・　￥ 1,200,000

・ RF PHY(1M, 2M, Stable Mod Index-Tx,Stable Mod Index-Rx ) 試験・・・　￥ 1,000,000

・代行登録サポート (Multi-Design) ・・・　￥ 250,000

・コンプライアンスフォルダ作成費・・・・・・　￥ 150,000

Q 社 DN が明確になり次第、必ず費用見積を見直しさせていただきますので、

よろしくお願いいたします。

Outlook for Android を取得差出人 : Junya Mizuno

送信日時 : 木曜日 , 8 月 7, 2025 8:23:11
午後宛先 : Jun Wang

件名 : RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

DN 提供が出来ておらず、申し訳ございません。

DN が無い場合、 ICS でもお見積りが可能とのお話しを弊社深浦より聞きました。

ICS は V 社経由で今週中に弊社に展開される予定ですが、現時点では展開されておりません。

今週まで V 社、および弊社含めて多くのメンバーが夏休みである為、来週中に展開される可能性が高いです。

弊社のスウェーデン現法メンバーに対して、来週中に途中段階でも良いので ICS を入手できるように依頼をします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, August 6, 2025 9:52 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

Q 社二つの DN とも取得中ということで現時点確定的な DN 情報がない、

という状態になります。

折角見積依頼書をいただきまして大変申し訳ございませんが、

費用見積のご提示がない状況となります。

Q 社 DN 取得でき次第で情報を展開いただきますと、

費用見積りのご提示が可能となりますので、

それまで少しお待ちいただきますようお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 6:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お問い合わせの件、ご回答させていただきます。

まだ Q 社で DN 取得中、との理解でよろしいでしょうか。

はい、ご認識あっております。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

現在、 V 社より、 w36(9/1 ～ 9/5) で利用可能になるとの連絡を受けております。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, August 5, 2025 4:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々すみません。

いただいた Bluetooth 見積依頼書では、 Host Stack に関して

TBD とご記入されていますが、

まだ Q 社で DN 取得中、との理解でよろしいでしょうか。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, August 5, 2025 2:37 PM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth 見積依頼書の更新をいただきありがとうございます。

BQC に試験対象項目を確認し、費用見積をご提示いたしますので、

少々お待ちくださいませ。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 8:30 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

対応が遅くなり、申し訳ございません、

Bluetooth 見積書を更新しました。

補足としては、以下になります。

・ Core-controller の DN を取得したい・以下の DN を include して End product を登録したい取得した Core-controller の DN

Qaulcomm から提供された、 RF/RF PHY が除かれた Core-Complete
DN

Qaulcomm から提供された、 X2Core DN

・ RF PHY の必須機能以外のサポート機能は仮で記入した状態こちらの内容でお見積りをお願いします。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, July 30, 2025 12:27 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

お忙しい中ご返信いただきありがとうございます。

RF/RF PHY の再試験を避ける為、 Core-Controller の DN を取得する方向で進めたいと思います。

弊社提案に合意をいただきありがとうございます。

現時点で埋められる部分を埋めて、 ICS 作成を進めるようにします。

ICS は登録内容を確定するためのものとして、

まずは見積書をご用意するにあたり、見積依頼書のご記入（更新）をお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 29, 2025 6:20 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございました。

また、こちらからの返信がかなり遅くなってしまい、申し訳ございません。

アリオン：はい、 Core-Controller の DN を取得のために 1 件の登録費用が発生しますが、

将来的に Q 社登録が更新されても御社名義の DN を Include することで再試験は回避できます。

承知しました。

RF/RF PHY の再試験を避ける為、 Core-Controller の DN を取得する方向で進めたいと思います。

アリオン：はい、登録内容を確定するという目的からは ICS レベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須 (1Mbps) および 2Mbps」という具合に仮入力をお願いします。

承知しました。

現時点で埋められる部分を埋めて、 ICS 作成を進めるようにします。

また、 Bluetooth と Wi-Fi は別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

承知しました。 ( 賛成です )

取り急ぎ、本メールタイトルから「Wi-Fi Alliance」を外しました。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 1:02 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth 認証に関する補足情報、また追加でいただいたご質問について、

下記回答させていただきます。※ 青字ご参照願います。

また、 Bluetooth と Wi-Fi は別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

アリオン：承知いたしました。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

アリオン：原則的には Include する Core-Controller の DN が変われば再度 RF/RF PHY 試験を実施することになります。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

アリオン：はい、 Core-Controller の DN を取得のために 1 件の登録費用が発生しますが、

将来的に Q 社登録が更新されても御社名義の DN を Include することで再試験は回避できます。

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

アリオン：はい、登録内容を確定するという目的からは ICS レベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須 (1Mbps) および 2Mbps」という具合に仮入力をお願いします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:20 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々失礼いたします。

費用見積に関して訂正させていただきます。

7/22 日付の見積には Submission Fee を含めていないため、下記訂正させていただきます。※ 青字ご参照

AP

Staion

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDV を含む )

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$63,640

61

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:11 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

王君の説明不足で混乱させたようで申し訳ございません。

3 ヵ月プランは基本形となっており、 Wi-Fi 6/6e、 Easymesh 等 Wi-Fi
Feature の複雑化に従い、

Wi-Fi 認証試験の L/T も延びている状況となっている中、

3 ヵ月プランも DUT の Wi-Fi Feature の複雑度及び受験サンプル台数を基に調整しております今回の UXC は対象 Wi-Fi Program も多いため、

サンプルを 2 ～ 3 セットのご提供をお願いいたしたいですが、

その場合、 AP と Station を各 1 台で試験を実施し、各 3 ヵ月の有効期限とさせていただきたいと考えます。

いかがでしょうか。

弊社側で記入を進め、 V 社に確認すべき部分は確認の上、提出とさせていただきます。

但し、 V 社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は 8 月下旬になる可能性が高いです。

弊社の Wi-Fi 見積依頼書の内容は概ねいただいている WorkSheet の Step3 Certification、一部 Step4 Capability の内容となりまして、

まずは現時点で確定となっている内容だけの整理で構いませんので、お願いができますと幸いです。

Ｖ社夏休み明けに確認必要な内容整理にもなると思います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 22, 2025 8:56 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お返事をいただき、ありがとうございました。

ü
お見積りをいただいた WFA プログラム (2.4/5GHz) の場合、 1 回の試験でどれくらいの LT 想定になるか、情報を展開いただく・・・ Allion
王様

⇒　試験費用や標準日程を Wi-Fi Program 別に整理いたしました、ご参照願います。

※下記試験費用や日程には、 Mandatory
項目しか含めておりません；

実際 DUT が Optional 項目もサポートし、 CID として登録内容に含めたい場合、試験費用や日程も変わります。

※下記 Test L/T は標準の Lead Time として、再試験は含んでおりません。

Test LT に関して、念のために認識合わせをさせて下さい。

現在、三か月プランでのお見積りをいただいていると思いますが、現在の試験プログラムの合計 Test LT は 61 日になっております。

一月の稼働日を 20 ～ 22 日で計算した場合、三か月は最大でも 66 日程度になる為、基本的には再試験をする日数は無いと認識しました。

こちらの認識はあっているでしょうか？

ü
Android OS
バージョンアップが WFA 試験に影響するかについて、関連する WFA からの公開情報を展開いただく・・・ Allion
王様

⇒　ラボに確認いたしますので少々お待ちください。

お手数ですが、ご確認をお願いします。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi 新規認証（New Certification）

御社フォームの WorkSheet をいただいておりますが、

VCC Comment、 QC Comment も併記されている中、現時点の最終仕様で添付の「Wi-Fi 認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

承知しました。

弊社側で記入を進め、 V 社に確認すべき部分は確認の上、提出とさせていただきます。

但し、 V 社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は 8 月下旬になる可能性が高いです。

以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 7:48 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

先週の打ち合わせ、お時間ありがとうございました。

製品サンプルを拝見できて、より働く価値を身に感じまして、感謝いたします。

Bluetooth に関して、確認して別途回答いたします。

Wi-Fi に関して下記二点弊社側の宿題事項について下記回答いたします。

ü
お見積りをいただいた WFA プログラム (2.4/5GHz) の場合、 1 回の試験でどれくらいの LT 想定になるか、情報を展開いただく・・・ Allion
王様

⇒ 試験費用や標準日程を W i-Fi Program 別に整理いたしました、ご参照願います。

※下記試験費用や日程には、 Mandatory
項目しか含めておりません；

実際 DUT が Optional 項目もサポートし、 CID として登録内容に含めたい場合、試験費用や日程も変わります。

※下記 Test L/T は標準の Lead Time として、再試験は含んでおりません。

AP

Station

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDV を含む )

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$58,640

61

ü
Android OS
バージョンアップが WFA 試験に影響するかについて、関連する WFA からの公開情報を展開いただく・・・ Allion
王様

⇒　ラボに確認いたしますので少々お待ちください。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi 新規認証（New Certification）

御社フォームの WorkSheet をいただいておりますが、

VCC Comment、 QC Comment も併記されている中、現時点の最終仕様で添付の「Wi-Fi 認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, July 18, 2025 3:40 PM

To: Jun Wang

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

昨日は遠い中、弊社までお越しいただき、ありがとうございました。

Bluetooth 認証登録書、 Wi-Fi 新規認証（New Certification）につきましては、弊社側で最新内容に更新します。

Bluetooth 認証登録書の更新にあたり、何点かご確認した内容があります。以下の質問に対して、ご回答をお願いできますでしょうか？

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

Wi-Fi 認証の事前試験については、アリオン様でお見積り済みの LT 情報も踏まえて、判断したいと考えています。

以下は昨日の議事メモ内になります。 ( 黄色塗りつぶしは宿題事項となっております )

その中でも依頼事項として記載しておりますのでご展開をお願いします。

【[ID]】

ü
試験拠点は以下の通り。

Ø
PTS IOPT :
日本

Ø
Controller(PHY) :
日本 or
中国 or 台湾　※ [ID] 見積依頼書の内容を基に Allion 様側で判断予定。

ü
想定される試験期間は以下の通り。 (= 現状、それぞれ三か月を見込んでいる為、計画内で完了する見通し )

Ø
PTS IOPT : 2~3 回の不具合修正 / 再テスト含めて、 8 週間。 (IOPT だけなので更に短い LT で完了できる見通し )

Ø
Controller(PHY) :
一か月 (MAX)

ü
見積依頼書を更新して Allion 様に提出する・・・ ALAP
水野

【WFA】

ü
WFA 認証プランは三か月プランが一般的であり、先日頂いたお見積りも三か月プランの費用になる。

Ø
1 回目の試験は、 NG が出ても試験できる項目を全て通して実施する。 (NG により試験出来ない項目は Skip)

Ø
2 回目の試験は、基本的に NG 項目を再試験するが、 NG 項目に関連する項目は再試験する場合もあり。

ü
お見積りをいただいた WFA プログラム (2.4/5GHz) の場合、 1 回の試験でどれくらいの LT 想定になるか、情報を展開いただく・・・ Allion
王様

ü
試験場所は、中国 or
台湾になる。 ( 基本的には台湾が多くの試験設備を保持している為、台湾になる見込み )

ü
事前検証を Allion 様に依頼する場合、全ての項目を依頼するか、 V 社と協議の上、心配項目を依頼するか、判断する・・・ ALAP
水野

ü
Android OS
バージョンアップが WFA 試験に影響するかについて、関連する WFA からの公開情報を展開いただく・・・ Allion
王様

Ø
Volvo に Android OS のバージョンアップが WFA 認証に影響することを説明するために利用したい以上です。

宜しくお願いします。

+
アルプスアルパイン株式会社 DC1 設計部開発 2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, July 18, 2025 10:29 AM

To: 水野淳也 Junya Mizuno ;
酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様、酒井様いつもお世話になります、アリオンの王君です。

昨日はお忙しい中お時間をいただきありがとうございました。

UXC の開発及び Bluetooth ＆ Wi-Fi 認証に向けた最新日程の共有、ありがとうございます。

·
Bluetooth 認証登録

24 年 9 月にいただきました見積依頼書を添付いたします。

ご更新いただき、弊社より試験対象項目及び見積をご提示いたしますので、よろしくお願いいたします。

·
Wi-Fi 新規認証（New Certification）

御社フォームの WorkSheet をいただいておりますが、

VCC Comment、 QC Comment も併記されている中、現時点の最終仕様で添付の「Wi-Fi 認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

·
Wi-Fi 認証の事前試験に関して、御社別部隊からもよく「事前試験＋本番試験」でご依頼をいただいております。

本番試験をスムーズに進められるように、事前に一通り試験を回しておく、

もしくは一部気になる Program/ 項目を確認しておくことをお勧めいたします。

·
CSD に関して、いろいろご調整いただき誠にありがとうございます。

CSD を除いた DUT 本体やケーブル類は本社日本から、 CSD は御社中国から、

ご提供される予定との旨、承知いたしました。

試験に向けて引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

-----Original Appointment-----

From: Jun Wang On Behalf Of Junya Mizuno

Sent: Thursday, July 17, 2025 12:59 PM

To: Doyen

Subject: FW: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議

When: 2025 年 7 月 17 日木曜日 13:00-14:00
(UTC+09:00) 大阪、札幌、東京

Where: 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議差出人 : Junya Mizuno

送信日時 : 2025 年 7 月 8 日 16:55:10
(UTC+09:00) Osaka, Sapporo, Tokyo

宛先 : Junya Mizuno ;
Jun Wang ;
Itsuo Sakai ;
Shigeyuki Sakai ;
Hiroaki Fukaura

件名 : [UXC] VCC UXC モデル向け Bluetooth
SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議開催日 : 2025 年 7 月 17 日 13:00
- 14:00。

場所 : 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議アリオン王様、酒井様いつもお世話になっております。アルプスアルパインの水野です。

大変遅くなってしまい申し訳ございません。

V 社ソフトリリース日程、 Display(CSD) 入手見込みが固まってきましたので、

最新状況を反映した Bluetooth SIG/Wi-Fi Alliance 認証計画を作成中です。

最新認証計画を基に、認証計画の共有、認証に向けた段取りの協議をさせて下さい。

※最新認証計画は 7/11( 金 ) までに送付させていただきます。

以上です。

宜しくお願いします。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
460 795 130 830 7

パスコード :
db6Xf3X4

開催者向け :
会議オプション

________________________________________________________________________________

---

## 3. 2025-09-08 05:31

**From:** Itsuo Sakai
**To:** Jun Wang

王さんお疲れさまです。

費用は変わりませんが、見積確定は客先のRF PHYの試験範囲の連絡待ちです。

客先質問には以下のように返信してください。

酒井ーーーー
Volvo/Qualcommから、Chipの新しいDNのご連絡を頂きました。
再度、
Host & X2Core : [ID]
Component : [ID] (←新)
この組み合わせにて、ご確認していただけますでしょうか。

⇒私のWorkspaceの仮Projectでチェックした結果、[ID] (←新)はこれまでの

Q366226と比較して(1)LL 9/11:NO、(2)RF階層不含、(3)RF PHY階層不含となっています。また、新たな階層間エラーも発生していません。

このため製品でRF/RF PHY試験を実施してエビデンスにする今回の登録では問題なくClass 2としての登録実施が可能です。

ーーーー差出人: Jun Wang

送信日時: 2025年9月8日 14:01

宛先: Itsuo Sakai

件名: FW:【Internal】 【ALAP】[UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議酒井さんお疲れ様です。

AlpsAlpine様V社向けUXCのBluetooth認証登録の件、

Bluetooth IC/Moduleに関してIncludeするDNの更新がありました。

下記内容で費用見積りの更新があるか、ご確認をお願いしてよろしいでしょうか。

※LE 2M PHYなどのOption機能は以前確認中となります。

Bluetooth Component：[ID]　→ [ID]

Host & X2Core : [ID] →　更新無

n
9/3にいただいた費用見積：

・RFフル項目試験・・・・・・・・・・・　￥1,200,000

・RF PHY試験(1M, 2M)　・・・・・・・・・・　￥700,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・　￥150,000

宜しくお願い致します。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 8, 2025 1:33 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo/Qualcomm から、 Chip の新しい DN のご連絡を頂きました。

再度、

Host & X2Core : [ID]

Component : [ID] ( ←新 )

この組み合わせにて、ご確認していただけますでしょうか。

LE 2M PHY 等、オプション機能について試験するかどうかは依然確認中です。

引き続き、急ぎ確認するようにします。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:22 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

費用について、いただいたQ社DNを基に、見積を下記更新いたします。

合計：￥1,100,000（税抜）

内、

・RF PHY試験(1M, 2M) ・・・・・・　￥700,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・・・・　￥150,000

下記追加でいただいたご質問ですが、

再度確認いたしまして、Q366226はQ社にしては珍しくRF PHYを含んだ登録でした。

Subsetの依頼ではLLだけではなくRF 1/15 Power Class 1:YES→NOも併せてご依頼ください。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 11:43 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

すみません、質問を追加させてください。

[ID] の Subset 作成についてですが、「RF
1/1 Power Class 1」はNoにする必要はございませんでしょうか？現在Yesになっています。

お手数ですが、こちらもご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 8:52 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

ご回答どうもありがとうございました。

[ID] の Subset 作成は急ぎ Qualcomm/Volvo へ説明し、対処するようにします。

LE のオプション機能についても理解いたしました。ご解説、大変助かります。

もし、 LE 2M PHY を付ける場合、試験期間と費用はどのくらい変化しますでしょうか？

酒井

From: Jun Wang

Sent: Tuesday, September 2, 2025 10:37 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井さんいつもお世話になります。アリオンの王君です。

標記Bluetooth認証登録につき、Q社DN情報の共有ありがとうございます。

以下いただいたご質問をインラインにて回答させていただきますので、

青字部分ご参照願います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 1, 2025 8:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo から使用する DN の正式情報を入手しましたので、見積依頼書と共にご連絡いたします。

Volvo で Host や X2Core に独自に追加するものは無く、 Qualcomm より提供された DN
[ID] をそのまま使用するとのことです。

なお、 Chip の Component
DN も新しいものが連絡されてきました。 [ID] です。

Consistency check、必要試験の特定に進みたいのですが、その前に、以下の気になる点について確認させてください。

製品は Power Class 2 で認証取得したいのですが、 [ID] の LL
ICS 9/11 が YES です。そうすると、 HM26 のときにあった、 Power
Class の不整合問題に該当しますか？やはり。

回答：

はい、Q366226をIncludeし、RF PHYはSoCを製品基板に直実装のために必要な試験を実施するので

RF PHY 1/15:NOへの変更は問題ありませんが、併せて必要なLL　9/11：NOへ変更すると

LL ICSに紐付いた全試験項目が Test Plan として出力されます。

そこで購入契約者(V社あるいは御社)からQ社へ「Q366226のRF PHY 1/15:NOおよび

LL ICS 9/11:NOのSubsetを作成 （SIGへの支払は無料） して欲しい」と要求してください。

・見積依頼書内の“ RF PHY の必須機能以外のサポート機能“について、以下、確認させていただきたいです。

どれが必要な機能か、上記 DN から特定可能でしょうか？

回答：

IncludeするDNの内容でRF PHYの試験範囲が決まるのではなく、製品組込アプリがどこまでサポートしているかにより決定します。

車載器では見かけ上の伝搬速度を下げて遠くへ伝達させるCodedは不要かつStable xxxは不要かと思います。

2Mbpsは対向相手がサポートしていると自動でネゴシエートされますので使う可能性が高いです。

したがって必須1Mと2Mの試験実施でよろしいかと思います。

最終判断は製品アプリの開発担当部門へご確認ください。

また、今回不要な機能があったとしても、将来 Host 側に更新が入った場合に備え、 Controller 側では予備的に認証を取得しておく考え方はありますでしょうか？

回答：

もしQ社がHost Q370647のアップデートが予想され、V社もそれに追従しそうな場合には、

予備的にController部の部分登録・認証を取得しておけば将来のアップデート登録が楽に済みます。

以上、ご確認をよろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, August 22, 2025 6:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記状況共有させていただきありがとうございます。

Q社DNが取得でき次第またご展開いただきますようお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 10:53 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

時間が空いてしまい、申し訳ございません。

Q社のDN情報について、現状をご連絡させていただきます。

弊社スウェーデンの現地法人を経由して、正式見積もりおよび認証開始に向けて、

V社に対して、Q社からX2Core及びCore complete(Host)のDN情報を早急に入手するように依頼しております。

入手でき次第に早急に展開させていただきますのでお待ち下さい。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 8, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ICS (Implementation Conformance Statements)は申請製品の機能記述として、

includedするQ社core completeのDN及びX2CoreのDN情報がないと、

免除できる試験項目を確定できず、見積のご提示が難しいです。

今回の試験内容的に、RF/RF PHY試験はQ社登録に不含ですので見積依頼書のP2の記載内容で確定していますが、

プロファイルはX2Core の登録内容と製品の実装内容の差異が明確にならないと確定見積ができません。

敢えて製品実装プロファイルは X2Core登録でカバーされ、製品でのプロファイル試験は発生しないという前提条件付の場合、見積は下記となります。

合計 ￥2,600,000（税抜）

内訳、

・RFフル項目試験・・・　￥1,200,000

・RF PHY(1M, 2M, Stable Mod Index-Tx,Stable Mod Index-Rx )試験・・・　￥1,000,000

・代行登録サポート(Multi-Design) ・・・　￥250,000

・コンプライアンスフォルダ作成費・・・・・・　￥150,000

Q社DNが明確になり次第、必ず費用見積を見直しさせていただきますので、

よろしくお願いいたします。

Outlook
for Android を取得差出人: Junya Mizuno

送信日時: 木曜日, 8月 7, 2025 8:23:11 午後宛先: Jun Wang

件名: RE: [UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

DN提供が出来ておらず、申し訳ございません。

DNが無い場合、ICSでもお見積りが可能とのお話しを弊社深浦より聞きました。

ICSはV社経由で今週中に弊社に展開される予定ですが、現時点では展開されておりません。

今週までV社、および弊社含めて多くのメンバーが夏休みである為、来週中に展開される可能性が高いです。

弊社のスウェーデン現法メンバーに対して、来週中に途中段階でも良いのでICSを入手できるように依頼をします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, August 6, 2025 9:52 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

Q社二つのDNとも取得中ということで現時点確定的なDN情報がない、

という状態になります。

折角見積依頼書をいただきまして大変申し訳ございませんが、

費用見積のご提示がない状況となります。

Q社DN取得でき次第で情報を展開いただきますと、

費用見積りのご提示が可能となりますので、

それまで少しお待ちいただきますようお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 6:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お問い合わせの件、ご回答させていただきます。

まだQ社でDN取得中、との理解でよろしいでしょうか。

はい、ご認識あっております。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

現在、V社より、w36(9/1～9/5)で利用可能になるとの連絡を受けております。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, August 5, 2025 4:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々すみません。

いただいたBluetooth見積依頼書では、Host Stackに関して

TBDとご記入されていますが、

まだQ社でDN取得中、との理解でよろしいでしょうか。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, August 5, 2025 2:37 PM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth見積依頼書の更新をいただきありがとうございます。

BQCに試験対象項目を確認し、費用見積をご提示いたしますので、

少々お待ちくださいませ。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 8:30 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

対応が遅くなり、申し訳ございません、

Bluetooth見積書を更新しました。

補足としては、以下になります。

・ Core-controllerのDNを取得したい・以下のDNをincludeしてEnd productを登録したい取得したCore-controllerのDN

Qaulcommから提供された、RF/RF PHYが除かれたCore-Complete DN

Qaulcommから提供された、X2Core DN

・ RF PHYの必須機能以外のサポート機能は仮で記入した状態こちらの内容でお見積りをお願いします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, July 30, 2025 12:27 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

お忙しい中ご返信いただきありがとうございます。

RF/RF PHYの再試験を避ける為、Core-ControllerのDNを取得する方向で進めたいと思います。

弊社提案に合意をいただきありがとうございます。

現時点で埋められる部分を埋めて、ICS作成を進めるようにします。

ICSは登録内容を確定するためのものとして、

まずは見積書をご用意するにあたり、見積依頼書のご記入（更新）をお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 29, 2025 6:20 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございました。

また、こちらからの返信がかなり遅くなってしまい、申し訳ございません。

アリオン：はい、Core-ControllerのDNを取得のために1件の登録費用が発生しますが、

将来的にQ社登録が更新されても御社名義のDNをIncludeすることで再試験は回避できます。

承知しました。

RF/RF PHYの再試験を避ける為、Core-ControllerのDNを取得する方向で進めたいと思います。

アリオン：はい、登録内容を確定するという目的からはICSレベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須(1Mbps)および2Mbps」という具合に仮入力をお願いします。

承知しました。

現時点で埋められる部分を埋めて、ICS作成を進めるようにします。

また、BluetoothとWi-Fiは別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

承知しました。(賛成です)

取り急ぎ、本メールタイトルから「Wi-Fi Alliance」を外しました。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 1:02 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth認証に関する補足情報、また追加でいただいたご質問について、

下記回答させていただきます。※ 青字ご参照願います。

また、BluetoothとWi-Fiは別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

アリオン：承知いたしました。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

アリオン：原則的にはIncludeするCore-ControllerのDNが変われば再度RF/RF PHY試験を実施することになります。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

アリオン：はい、Core-ControllerのDNを取得のために1件の登録費用が発生しますが、

将来的にQ社登録が更新されても御社名義のDNをIncludeすることで再試験は回避できます。

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

アリオン：はい、登録内容を確定するという目的からはICSレベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須(1Mbps)および2Mbps」という具合に仮入力をお願いします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:20 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々失礼いたします。

費用見積に関して訂正させていただきます。

7/22日付の見積にはSubmission Feeを含めていないため、下記訂正させていただきます。※ 青字ご参照

AP

Staion

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDVを含む)

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$63,640

61

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:11 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

王君の説明不足で混乱させたようで申し訳ございません。

3ヵ月プランは基本形となっており、Wi-Fi 6/6e、Easymesh等Wi-Fi Featureの複雑化に従い、

Wi-Fi認証試験のL/Tも延びている状況となっている中、

3ヵ月プランもDUTのWi-Fi Featureの複雑度及び受験サンプル台数を基に調整しております今回のUXCは対象Wi-Fi Programも多いため、

サンプルを2～3セットのご提供をお願いいたしたいですが、

その場合、APとStationを各1台で試験を実施し、各3ヵ月の有効期限とさせていただきたいと考えます。

いかがでしょうか。

弊社側で記入を進め、V社に確認すべき部分は確認の上、提出とさせていただきます。

但し、V社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は8月下旬になる可能性が高いです。

弊社のWi-Fi見積依頼書の内容は概ねいただいているWorkSheetのStep3 Certification、一部Step4 Capabilityの内容となりまして、

まずは現時点で確定となっている内容だけの整理で構いませんので、お願いができますと幸いです。

Ｖ社夏休み明けに確認必要な内容整理にもなると思います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 22, 2025 8:56 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お返事をいただき、ありがとうございました。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

⇒　試験費用や標準日程をWi-Fi Program別に整理いたしました、ご参照願います。

※下記試験費用や日程には、Mandatory 項目しか含めておりません；

実際DUTがOptional項目もサポートし、CIDとして登録内容に含めたい場合、試験費用や日程も変わります。

※下記Test L/Tは標準のLead Timeとして、再試験は含んでおりません。

Test LTに関して、念のために認識合わせをさせて下さい。

現在、三か月プランでのお見積りをいただいていると思いますが、現在の試験プログラムの合計Test LTは61日になっております。

一月の稼働日を20～22日で計算した場合、三か月は最大でも66日程度になる為、基本的には再試験をする日数は無いと認識しました。

こちらの認識はあっているでしょうか？

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

⇒　ラボに確認いたしますので少々お待ちください。

お手数ですが、ご確認をお願いします。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

承知しました。

弊社側で記入を進め、V社に確認すべき部分は確認の上、提出とさせていただきます。

但し、V社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は8月下旬になる可能性が高いです。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 7:48 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

先週の打ち合わせ、お時間ありがとうございました。

製品サンプルを拝見できて、より働く価値を身に感じまして、感謝いたします。

Bluetoothに関して、確認して別途回答いたします。

Wi-Fiに関して下記二点弊社側の宿題事項について下記回答いたします。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

⇒ 試験費用や標準日程を W i-Fi
Program別に整理いたしました、ご参照願います。

※下記試験費用や日程には、Mandatory 項目しか含めておりません；

実際DUTがOptional項目もサポートし、CIDとして登録内容に含めたい場合、試験費用や日程も変わります。

※下記Test L/Tは標準のLead Timeとして、再試験は含んでおりません。

AP

Station

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDVを含む)

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$58,640

61

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

⇒　ラボに確認いたしますので少々お待ちください。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, July 18, 2025 3:40 PM

To: Jun Wang

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

昨日は遠い中、弊社までお越しいただき、ありがとうございました。

Bluetooth認証登録書、Wi-Fi　新規認証（New Certification）につきましては、弊社側で最新内容に更新します。

Bluetooth認証登録書の更新にあたり、何点かご確認した内容があります。以下の質問に対して、ご回答をお願いできますでしょうか？

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

Wi-Fi認証の事前試験については、アリオン様でお見積り済みのLT情報も踏まえて、判断したいと考えています。

以下は昨日の議事メモ内になります。( 黄色塗りつぶしは宿題事項となっております)

その中でも依頼事項として記載しておりますのでご展開をお願いします。

【[ID]】

ü
試験拠点は以下の通り。

Ø
PTS IOPT : 日本

Ø
Controller(PHY) : 日本 or 中国 or 台湾　※[ID] 見積依頼書の内容を基にAllion様側で判断予定。

ü
想定される試験期間は以下の通り。(=現状、それぞれ三か月を見込んでいる為、計画内で完了する見通し)

Ø
PTS IOPT : 2~3回の不具合修正/再テスト含めて、8週間。(IOPTだけなので更に短いLTで完了できる見通し)

Ø
Controller(PHY) : 一か月(MAX)

ü
[ID] 見積依頼書を更新してAllion様に提出する・・・ALAP 水野

【WFA】

ü
WFA認証プランは三か月プランが一般的であり、先日頂いたお見積りも三か月プランの費用になる。

Ø
1回目の試験は、NGが出ても試験できる項目を全て通して実施する。(NGにより試験出来ない項目はSkip)

Ø
2回目の試験は、基本的にNG項目を再試験するが、NG項目に関連する項目は再試験する場合もあり。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

ü
試験場所は、中国 or 台湾になる。(基本的には台湾が多くの試験設備を保持している為、台湾になる見込み)

ü
事前検証をAllion様に依頼する場合、全ての項目を依頼するか、V社と協議の上、心配項目を依頼するか、判断する・・・ALAP 水野

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

Ø
VolvoにAndroid OSのバージョンアップがWFA認証に影響することを説明するために利用したい以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, July 18, 2025 10:29 AM

To: 水野淳也 Junya Mizuno ;
酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様、酒井様いつもお世話になります、アリオンの王君です。

昨日はお忙しい中お時間をいただきありがとうございました。

UXCの開発及びBluetooth＆Wi-Fi認証に向けた最新日程の共有、ありがとうございます。

·
Bluetooth認証登録

24年9月にいただきました見積依頼書を添付いたします。

ご更新いただき、弊社より試験対象項目及び見積をご提示いたしますので、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

·
Wi-Fi認証の事前試験に関して、御社別部隊からもよく「事前試験＋本番試験」でご依頼をいただいております。

本番試験をスムーズに進められるように、事前に一通り試験を回しておく、

もしくは一部気になるProgram/項目を確認しておくことをお勧めいたします。

·
CSDに関して、いろいろご調整いただき誠にありがとうございます。

CSDを除いたDUT本体やケーブル類は本社日本から、CSDは御社中国から、

ご提供される予定との旨、承知いたしました。

試験に向けて引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

-----Original Appointment-----

From: Jun Wang On Behalf Of Junya Mizuno

Sent: Thursday, July 17, 2025 12:59 PM

To: Doyen

Subject: FW: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議

When: 2025 年 7 月 17 日木曜日 13:00-14:00
(UTC+09:00) 大阪、札幌、東京

Where: 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議差出人 : Junya Mizuno

送信日時 : 2025 年 7 月 8 日 16:55:10
(UTC+09:00) Osaka, Sapporo, Tokyo

宛先 : Junya Mizuno ;
Jun Wang ;
Itsuo Sakai ;
Shigeyuki Sakai ;
Hiroaki Fukaura

件名 : [UXC] VCC UXC モデル向け Bluetooth
SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議開催日 : 2025 年 7 月 17 日 13:00
- 14:00。

場所 : 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議アリオン王様、酒井様いつもお世話になっております。アルプスアルパインの水野です。

大変遅くなってしまい申し訳ございません。

V社ソフトリリース日程、Display(CSD)入手見込みが固まってきましたので、

最新状況を反映したBluetooth SIG/Wi-Fi Alliance認証計画を作成中です。

最新認証計画を基に、認証計画の共有、認証に向けた段取りの協議をさせて下さい。

※最新認証計画は7/11(金)までに送付させていただきます。

以上です。

宜しくお願いします。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
460 795 130 830 7

パスコード :
db6Xf3X4

開催者向け :
会議オプション

________________________________________________________________________________

---

## 4. 2025-09-08 05:53

**From:** Itsuo Sakai
**To:** Jun Wang

王さんお疲れさまです。

AJではRF PHYは必須(1M)項目のみ実施可能で他の項目はATでの実施となります。

酒井差出人: Jun Wang

送信日時: 2025年9月8日 14:51

宛先: Itsuo Sakai

件名: RE: 【Internal】 【ALAP】[UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議酒井さん早速ご確認いただきありがとうございます。

いただいた内容でお客様に返信いたします。

アリオン内部の確認ですが、

AlpsAlpine様HM26 A14のBluetooth認証登録同様、

LE 2M PHYはAJでは対応できず、ATでの実施になる状況は変わりがないとの認識で合っていますでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Itsuo Sakai

Sent: Monday, September 8, 2025 2:32 PM

To: Jun Wang

Subject: Re: 【Internal】
【ALAP】 [UXC] VCC UC モデル向け Bluetooth
SIG 認証計画の共有 / 段取りの協議王さんお疲れさまです。

費用は変わりませんが、見積確定は客先の RF PHY の試験範囲の連絡待ちです。

客先質問には以下のように返信してください。

酒井ーーーー
Volvo/Qualcomm から、 Chip の新しい DN のご連絡を頂きました。
再度、
Host & X2Core : [ID]
Component : [ID] (← 新 )
この組み合わせにて、ご確認していただけますでしょうか。

⇒ 私の Workspace の仮 Project でチェックした結果、 [ID]
(← 新 ) はこれまでの

[ID] と比較して (1)LL
9/11:NO、 (2)RF 階層不含、 (3)RF
PHY 階層不含となっています。また、新たな階層間エラーも発生していません。

このため製品で RF/RF PHY 試験を実施してエビデンスにする今回の登録では問題なく Class 2 としての登録実施が可能です。

ーーーー差出人 : Jun Wang

送信日時 : 2025 年 9 月 8 日 14:01

宛先 : Itsuo Sakai

件名 : FW: 【Internal】
【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議酒井さんお疲れ様です。

AlpsAlpine様V社向けUXCのBluetooth認証登録の件、

Bluetooth IC/Moduleに関してIncludeするDNの更新がありました。

下記内容で費用見積りの更新があるか、ご確認をお願いしてよろしいでしょうか。

※LE 2M PHYなどのOption機能は以前確認中となります。

Bluetooth Component：[ID]　→ [ID]

Host & X2Core : [ID] →　更新無

n
9/3にいただいた費用見積：

・RFフル項目試験・・・・・・・・・・・　￥1,200,000

・RF PHY試験(1M, 2M)　・・・・・・・・・・　￥700,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・　￥150,000

宜しくお願い致します。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 8, 2025 1:33 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo/Qualcomm から、 Chip の新しい DN のご連絡を頂きました。

再度、

Host & X2Core : [ID]

Component : [ID] ( ←新 )

この組み合わせにて、ご確認していただけますでしょうか。

LE 2M PHY 等、オプション機能について試験するかどうかは依然確認中です。

引き続き、急ぎ確認するようにします。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:22 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

費用について、いただいたQ社DNを基に、見積を下記更新いたします。

合計：￥1,100,000（税抜）

内、

・RF PHY試験(1M, 2M) ・・・・・・　￥700,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・・・・　￥150,000

下記追加でいただいたご質問ですが、

再度確認いたしまして、Q366226はQ社にしては珍しくRF PHYを含んだ登録でした。

Subsetの依頼ではLLだけではなくRF 1/15 Power Class 1:YES→NOも併せてご依頼ください。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 11:43 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

すみません、質問を追加させてください。

[ID] の Subset 作成についてですが、「RF
1/1 Power Class 1」はNoにする必要はございませんでしょうか？現在Yesになっています。

お手数ですが、こちらもご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 8:52 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

ご回答どうもありがとうございました。

[ID] の Subset 作成は急ぎ Qualcomm/Volvo へ説明し、対処するようにします。

LE のオプション機能についても理解いたしました。ご解説、大変助かります。

もし、 LE 2M PHY を付ける場合、試験期間と費用はどのくらい変化しますでしょうか？

酒井

From: Jun Wang

Sent: Tuesday, September 2, 2025 10:37 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井さんいつもお世話になります。アリオンの王君です。

標記Bluetooth認証登録につき、Q社DN情報の共有ありがとうございます。

以下いただいたご質問をインラインにて回答させていただきますので、

青字部分ご参照願います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 1, 2025 8:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo から使用する DN の正式情報を入手しましたので、見積依頼書と共にご連絡いたします。

Volvo で Host や X2Core に独自に追加するものは無く、 Qualcomm より提供された DN
[ID] をそのまま使用するとのことです。

なお、 Chip の Component
DN も新しいものが連絡されてきました。 [ID] です。

Consistency check、必要試験の特定に進みたいのですが、その前に、以下の気になる点について確認させてください。

製品は Power Class 2 で認証取得したいのですが、 [ID] の LL
ICS 9/11 が YES です。そうすると、 HM26 のときにあった、 Power
Class の不整合問題に該当しますか？やはり。

回答：

はい、Q366226をIncludeし、RF PHYはSoCを製品基板に直実装のために必要な試験を実施するので

RF PHY 1/15:NOへの変更は問題ありませんが、併せて必要なLL　9/11：NOへ変更すると

LL ICSに紐付いた全試験項目が Test Plan として出力されます。

そこで購入契約者(V社あるいは御社)からQ社へ「Q366226のRF PHY 1/15:NOおよび

LL ICS 9/11:NOのSubsetを作成 （SIGへの支払は無料） して欲しい」と要求してください。

・見積依頼書内の“ RF PHY の必須機能以外のサポート機能“について、以下、確認させていただきたいです。

どれが必要な機能か、上記 DN から特定可能でしょうか？

回答：

IncludeするDNの内容でRF PHYの試験範囲が決まるのではなく、製品組込アプリがどこまでサポートしているかにより決定します。

車載器では見かけ上の伝搬速度を下げて遠くへ伝達させるCodedは不要かつStable xxxは不要かと思います。

2Mbpsは対向相手がサポートしていると自動でネゴシエートされますので使う可能性が高いです。

したがって必須1Mと2Mの試験実施でよろしいかと思います。

最終判断は製品アプリの開発担当部門へご確認ください。

また、今回不要な機能があったとしても、将来 Host 側に更新が入った場合に備え、 Controller 側では予備的に認証を取得しておく考え方はありますでしょうか？

回答：

もしQ社がHost Q370647のアップデートが予想され、V社もそれに追従しそうな場合には、

予備的にController部の部分登録・認証を取得しておけば将来のアップデート登録が楽に済みます。

以上、ご確認をよろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, August 22, 2025 6:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記状況共有させていただきありがとうございます。

Q社DNが取得でき次第またご展開いただきますようお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 10:53 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

時間が空いてしまい、申し訳ございません。

Q社のDN情報について、現状をご連絡させていただきます。

弊社スウェーデンの現地法人を経由して、正式見積もりおよび認証開始に向けて、

V社に対して、Q社からX2Core及びCore complete(Host)のDN情報を早急に入手するように依頼しております。

入手でき次第に早急に展開させていただきますのでお待ち下さい。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 8, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ICS (Implementation Conformance Statements)は申請製品の機能記述として、

includedするQ社core completeのDN及びX2CoreのDN情報がないと、

免除できる試験項目を確定できず、見積のご提示が難しいです。

今回の試験内容的に、RF/RF PHY試験はQ社登録に不含ですので見積依頼書のP2の記載内容で確定していますが、

プロファイルはX2Core の登録内容と製品の実装内容の差異が明確にならないと確定見積ができません。

敢えて製品実装プロファイルは X2Core登録でカバーされ、製品でのプロファイル試験は発生しないという前提条件付の場合、見積は下記となります。

合計 ￥2,600,000（税抜）

内訳、

・RFフル項目試験・・・　￥1,200,000

・RF PHY(1M, 2M, Stable Mod Index-Tx,Stable Mod Index-Rx )試験・・・　￥1,000,000

・代行登録サポート(Multi-Design) ・・・　￥250,000

・コンプライアンスフォルダ作成費・・・・・・　￥150,000

Q社DNが明確になり次第、必ず費用見積を見直しさせていただきますので、

よろしくお願いいたします。

Outlook
for Android を取得差出人: Junya Mizuno

送信日時: 木曜日, 8月 7, 2025 8:23:11 午後宛先: Jun Wang

件名: RE: [UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

DN提供が出来ておらず、申し訳ございません。

DNが無い場合、ICSでもお見積りが可能とのお話しを弊社深浦より聞きました。

ICSはV社経由で今週中に弊社に展開される予定ですが、現時点では展開されておりません。

今週までV社、および弊社含めて多くのメンバーが夏休みである為、来週中に展開される可能性が高いです。

弊社のスウェーデン現法メンバーに対して、来週中に途中段階でも良いのでICSを入手できるように依頼をします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, August 6, 2025 9:52 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

Q社二つのDNとも取得中ということで現時点確定的なDN情報がない、

という状態になります。

折角見積依頼書をいただきまして大変申し訳ございませんが、

費用見積のご提示がない状況となります。

Q社DN取得でき次第で情報を展開いただきますと、

費用見積りのご提示が可能となりますので、

それまで少しお待ちいただきますようお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 6:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お問い合わせの件、ご回答させていただきます。

まだQ社でDN取得中、との理解でよろしいでしょうか。

はい、ご認識あっております。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

現在、V社より、w36(9/1～9/5)で利用可能になるとの連絡を受けております。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, August 5, 2025 4:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々すみません。

いただいたBluetooth見積依頼書では、Host Stackに関して

TBDとご記入されていますが、

まだQ社でDN取得中、との理解でよろしいでしょうか。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, August 5, 2025 2:37 PM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth見積依頼書の更新をいただきありがとうございます。

BQCに試験対象項目を確認し、費用見積をご提示いたしますので、

少々お待ちくださいませ。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 8:30 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

対応が遅くなり、申し訳ございません、

Bluetooth見積書を更新しました。

補足としては、以下になります。

・ Core-controllerのDNを取得したい・以下のDNをincludeしてEnd productを登録したい取得したCore-controllerのDN

Qaulcommから提供された、RF/RF PHYが除かれたCore-Complete DN

Qaulcommから提供された、X2Core DN

・ RF PHYの必須機能以外のサポート機能は仮で記入した状態こちらの内容でお見積りをお願いします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, July 30, 2025 12:27 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

お忙しい中ご返信いただきありがとうございます。

RF/RF PHYの再試験を避ける為、Core-ControllerのDNを取得する方向で進めたいと思います。

弊社提案に合意をいただきありがとうございます。

現時点で埋められる部分を埋めて、ICS作成を進めるようにします。

ICSは登録内容を確定するためのものとして、

まずは見積書をご用意するにあたり、見積依頼書のご記入（更新）をお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 29, 2025 6:20 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございました。

また、こちらからの返信がかなり遅くなってしまい、申し訳ございません。

アリオン：はい、Core-ControllerのDNを取得のために1件の登録費用が発生しますが、

将来的にQ社登録が更新されても御社名義のDNをIncludeすることで再試験は回避できます。

承知しました。

RF/RF PHYの再試験を避ける為、Core-ControllerのDNを取得する方向で進めたいと思います。

アリオン：はい、登録内容を確定するという目的からはICSレベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須(1Mbps)および2Mbps」という具合に仮入力をお願いします。

承知しました。

現時点で埋められる部分を埋めて、ICS作成を進めるようにします。

また、BluetoothとWi-Fiは別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

承知しました。(賛成です)

取り急ぎ、本メールタイトルから「Wi-Fi Alliance」を外しました。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 1:02 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth認証に関する補足情報、また追加でいただいたご質問について、

下記回答させていただきます。※ 青字ご参照願います。

また、BluetoothとWi-Fiは別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

アリオン：承知いたしました。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

アリオン：原則的にはIncludeするCore-ControllerのDNが変われば再度RF/RF PHY試験を実施することになります。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

アリオン：はい、Core-ControllerのDNを取得のために1件の登録費用が発生しますが、

将来的にQ社登録が更新されても御社名義のDNをIncludeすることで再試験は回避できます。

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

アリオン：はい、登録内容を確定するという目的からはICSレベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須(1Mbps)および2Mbps」という具合に仮入力をお願いします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:20 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々失礼いたします。

費用見積に関して訂正させていただきます。

7/22日付の見積にはSubmission Feeを含めていないため、下記訂正させていただきます。※ 青字ご参照

AP

Staion

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDVを含む)

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$63,640

61

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:11 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

王君の説明不足で混乱させたようで申し訳ございません。

3ヵ月プランは基本形となっており、Wi-Fi 6/6e、Easymesh等Wi-Fi Featureの複雑化に従い、

Wi-Fi認証試験のL/Tも延びている状況となっている中、

3ヵ月プランもDUTのWi-Fi Featureの複雑度及び受験サンプル台数を基に調整しております今回のUXCは対象Wi-Fi Programも多いため、

サンプルを2～3セットのご提供をお願いいたしたいですが、

その場合、APとStationを各1台で試験を実施し、各3ヵ月の有効期限とさせていただきたいと考えます。

いかがでしょうか。

弊社側で記入を進め、V社に確認すべき部分は確認の上、提出とさせていただきます。

但し、V社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は8月下旬になる可能性が高いです。

弊社のWi-Fi見積依頼書の内容は概ねいただいているWorkSheetのStep3 Certification、一部Step4 Capabilityの内容となりまして、

まずは現時点で確定となっている内容だけの整理で構いませんので、お願いができますと幸いです。

Ｖ社夏休み明けに確認必要な内容整理にもなると思います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 22, 2025 8:56 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お返事をいただき、ありがとうございました。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

⇒　試験費用や標準日程をWi-Fi Program別に整理いたしました、ご参照願います。

※下記試験費用や日程には、Mandatory 項目しか含めておりません；

実際DUTがOptional項目もサポートし、CIDとして登録内容に含めたい場合、試験費用や日程も変わります。

※下記Test L/Tは標準のLead Timeとして、再試験は含んでおりません。

Test LTに関して、念のために認識合わせをさせて下さい。

現在、三か月プランでのお見積りをいただいていると思いますが、現在の試験プログラムの合計Test LTは61日になっております。

一月の稼働日を20～22日で計算した場合、三か月は最大でも66日程度になる為、基本的には再試験をする日数は無いと認識しました。

こちらの認識はあっているでしょうか？

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

⇒　ラボに確認いたしますので少々お待ちください。

お手数ですが、ご確認をお願いします。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

承知しました。

弊社側で記入を進め、V社に確認すべき部分は確認の上、提出とさせていただきます。

但し、V社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は8月下旬になる可能性が高いです。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 7:48 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

先週の打ち合わせ、お時間ありがとうございました。

製品サンプルを拝見できて、より働く価値を身に感じまして、感謝いたします。

Bluetoothに関して、確認して別途回答いたします。

Wi-Fiに関して下記二点弊社側の宿題事項について下記回答いたします。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

⇒ 試験費用や標準日程を W i-Fi
Program別に整理いたしました、ご参照願います。

※下記試験費用や日程には、Mandatory 項目しか含めておりません；

実際DUTがOptional項目もサポートし、CIDとして登録内容に含めたい場合、試験費用や日程も変わります。

※下記Test L/Tは標準のLead Timeとして、再試験は含んでおりません。

AP

Station

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDVを含む)

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$58,640

61

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

⇒　ラボに確認いたしますので少々お待ちください。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, July 18, 2025 3:40 PM

To: Jun Wang

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

昨日は遠い中、弊社までお越しいただき、ありがとうございました。

Bluetooth認証登録書、Wi-Fi　新規認証（New Certification）につきましては、弊社側で最新内容に更新します。

Bluetooth認証登録書の更新にあたり、何点かご確認した内容があります。以下の質問に対して、ご回答をお願いできますでしょうか？

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

Wi-Fi認証の事前試験については、アリオン様でお見積り済みのLT情報も踏まえて、判断したいと考えています。

以下は昨日の議事メモ内になります。( 黄色塗りつぶしは宿題事項となっております)

その中でも依頼事項として記載しておりますのでご展開をお願いします。

【[ID]】

ü
試験拠点は以下の通り。

Ø
PTS IOPT : 日本

Ø
Controller(PHY) : 日本 or 中国 or 台湾　※[ID] 見積依頼書の内容を基にAllion様側で判断予定。

ü
想定される試験期間は以下の通り。(=現状、それぞれ三か月を見込んでいる為、計画内で完了する見通し)

Ø
PTS IOPT : 2~3回の不具合修正/再テスト含めて、8週間。(IOPTだけなので更に短いLTで完了できる見通し)

Ø
Controller(PHY) : 一か月(MAX)

ü
[ID] 見積依頼書を更新してAllion様に提出する・・・ALAP 水野

【WFA】

ü
WFA認証プランは三か月プランが一般的であり、先日頂いたお見積りも三か月プランの費用になる。

Ø
1回目の試験は、NGが出ても試験できる項目を全て通して実施する。(NGにより試験出来ない項目はSkip)

Ø
2回目の試験は、基本的にNG項目を再試験するが、NG項目に関連する項目は再試験する場合もあり。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

ü
試験場所は、中国 or 台湾になる。(基本的には台湾が多くの試験設備を保持している為、台湾になる見込み)

ü
事前検証をAllion様に依頼する場合、全ての項目を依頼するか、V社と協議の上、心配項目を依頼するか、判断する・・・ALAP 水野

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

Ø
VolvoにAndroid OSのバージョンアップがWFA認証に影響することを説明するために利用したい以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, July 18, 2025 10:29 AM

To: 水野淳也 Junya Mizuno ;
酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様、酒井様いつもお世話になります、アリオンの王君です。

昨日はお忙しい中お時間をいただきありがとうございました。

UXCの開発及びBluetooth＆Wi-Fi認証に向けた最新日程の共有、ありがとうございます。

·
Bluetooth認証登録

24年9月にいただきました見積依頼書を添付いたします。

ご更新いただき、弊社より試験対象項目及び見積をご提示いたしますので、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

·
Wi-Fi認証の事前試験に関して、御社別部隊からもよく「事前試験＋本番試験」でご依頼をいただいております。

本番試験をスムーズに進められるように、事前に一通り試験を回しておく、

もしくは一部気になるProgram/項目を確認しておくことをお勧めいたします。

·
CSDに関して、いろいろご調整いただき誠にありがとうございます。

CSDを除いたDUT本体やケーブル類は本社日本から、CSDは御社中国から、

ご提供される予定との旨、承知いたしました。

試験に向けて引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

-----Original Appointment-----

From: Jun Wang On Behalf Of Junya Mizuno

Sent: Thursday, July 17, 2025 12:59 PM

To: Doyen

Subject: FW: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議

When: 2025 年 7 月 17 日木曜日 13:00-14:00
(UTC+09:00) 大阪、札幌、東京

Where: 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議差出人 : Junya Mizuno

送信日時 : 2025 年 7 月 8 日 16:55:10
(UTC+09:00) Osaka, Sapporo, Tokyo

宛先 : Junya Mizuno ;
Jun Wang ;
Itsuo Sakai ;
Shigeyuki Sakai ;
Hiroaki Fukaura

件名 : [UXC] VCC UXC モデル向け Bluetooth
SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議開催日 : 2025 年 7 月 17 日 13:00
- 14:00。

場所 : 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議アリオン王様、酒井様いつもお世話になっております。アルプスアルパインの水野です。

大変遅くなってしまい申し訳ございません。

V社ソフトリリース日程、Display(CSD)入手見込みが固まってきましたので、

最新状況を反映したBluetooth SIG/Wi-Fi Alliance認証計画を作成中です。

最新認証計画を基に、認証計画の共有、認証に向けた段取りの協議をさせて下さい。

※最新認証計画は7/11(金)までに送付させていただきます。

以上です。

宜しくお願いします。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
460 795 130 830 7

パスコード :
db6Xf3X4

開催者向け :
会議オプション

________________________________________________________________________________

---

## 5. 2025-09-18 07:55

**From:** Itsuo Sakai
**To:** Jun Wang

王さんお疲れさまです。
下記内容でよろしいでしょうか。
合計 ￥2,000,000（税抜）
・RFフル項目試験・・・・・・・・・・・　￥1,200,000
・RF PHY試験(必須機能のみ)　・・・・・・・・・　￥400,000
・代行登録サポート(Multi-Design参照)　・・・　￥250,000
・コンプライアンスフォルダ作成費・・・　￥150,000

⇒これで結構です。
Core-ControllerのDN取得について
7/22のメールで下記のようなやり取りがありましたが、Core-Controllerの
DN取得も今回のBluetooth認証登録に含まれるとの認識でよろしいでしょうか。

⇒申請者が2件分のQualificarion Feeを払っていただければ、Core-complete

（旧End Prduct）登録の試験及び見積費用と同額で(1) Core-Controller登録とそのDNを参照した(2)Core-complete登録に対応します。

酒井差出人: Jun Wang

送信日時: 2025年9月18日 16:09

宛先: Itsuo Sakai

件名: RE: 【Internal】 【ALAP】[UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議酒井さん

AlpsAlpine様V社UXC10のBluetooth認証登録の件、

下記メールはご確認いただきましたでしょうか。

宜しくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Wednesday, September 17, 2025 11:49 AM

To: Itsuo Sakai

Subject: RE: 【Internal】
【ALAP】 [UXC] VCC UC モデル向け Bluetooth
SIG 認証計画の共有 / 段取りの協議酒井さんお疲れ様です。

AlpsAlpine様Volvo社向けUXC1.0のBluetooth認証登録の件ですが、

お客様よりご連絡をいただきまして、RF-PHYのOption機能は「全て不要」とのことです。

※最新版見積依頼書を添付いたします。

n
見積内容の確認下記内容でよろしいでしょうか。

合計 ￥2,000,000（税抜）

・RFフル項目試験・・・・・・・・・・・　￥1,200,000

・RF PHY試験(必須機能のみ)　・・・・・・・・・・　￥400,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・　￥150,000

n
Core-ControllerのDN取得について

7/22のメールで下記のようなやり取りがありましたが、Core-ControllerのDN取得も今回のBluetooth認証登録に含まれるとの認識でよろしいでしょうか。

（質問） ALAP:上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

--> アリオン様：はい、Core-ControllerのDNを取得のために1件の登録費用が発生しますが、

--> 将来的にQ社登録が更新されても御社名義のDNをIncludeすることで再試験は回避できます。

ご確認いただきますようお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Itsuo Sakai

Sent: Monday, September 8, 2025 2:32 PM

To: Jun Wang

Subject: Re: 【Internal】
【ALAP】 [UXC] VCC UC モデル向け Bluetooth
SIG 認証計画の共有 / 段取りの協議王さんお疲れさまです。

費用は変わりませんが、見積確定は客先の RF PHY の試験範囲の連絡待ちです。

客先質問には以下のように返信してください。

酒井ーーーー
Volvo/Qualcomm から、 Chip の新しい DN のご連絡を頂きました。
再度、
Host & X2Core : [ID]
Component : [ID] (← 新 )
この組み合わせにて、ご確認していただけますでしょうか。

⇒ 私の Workspace の仮 Project でチェックした結果、 [ID]
(← 新 ) はこれまでの

[ID] と比較して (1)LL
9/11:NO、 (2)RF 階層不含、 (3)RF
PHY 階層不含となっています。また、新たな階層間エラーも発生していません。

このため製品で RF/RF PHY 試験を実施してエビデンスにする今回の登録では問題なく Class 2 としての登録実施が可能です。

ーーーー差出人 : Jun Wang

送信日時 : 2025 年 9 月 8 日 14:01

宛先 : Itsuo Sakai

件名 : FW: 【Internal】
【ALAP】 [UXC]
VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議酒井さんお疲れ様です。

AlpsAlpine様V社向けUXCのBluetooth認証登録の件、

Bluetooth IC/Moduleに関してIncludeするDNの更新がありました。

下記内容で費用見積りの更新があるか、ご確認をお願いしてよろしいでしょうか。

※LE 2M PHYなどのOption機能は以前確認中となります。

Bluetooth Component：[ID]　→ [ID]

Host & X2Core : [ID] →　更新無

n
9/3にいただいた費用見積：

・RFフル項目試験・・・・・・・・・・・　￥1,200,000

・RF PHY試験(1M, 2M)　・・・・・・・・・・　￥700,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・　￥150,000

宜しくお願い致します。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 8, 2025 1:33 PM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo/Qualcomm から、 Chip の新しい DN のご連絡を頂きました。

再度、

Host & X2Core : [ID]

Component : [ID] ( ←新 )

この組み合わせにて、ご確認していただけますでしょうか。

LE 2M PHY 等、オプション機能について試験するかどうかは依然確認中です。

引き続き、急ぎ確認するようにします。

よろしくお願いいたします。

酒井

From: Jun Wang

Sent: Wednesday, September 3, 2025 1:22 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井様いつもお世話になります、アリオンの王君です。

費用について、いただいたQ社DNを基に、見積を下記更新いたします。

合計：￥1,100,000（税抜）

内、

・RF PHY試験(1M, 2M) ・・・・・・　￥700,000

・代行登録サポート(Multi-Design参照)　・・・　￥250,000

・コンプライアンスフォルダ作成費・・・・・・　￥150,000

下記追加でいただいたご質問ですが、

再度確認いたしまして、Q366226はQ社にしては珍しくRF PHYを含んだ登録でした。

Subsetの依頼ではLLだけではなくRF 1/15 Power Class 1:YES→NOも併せてご依頼ください。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 11:43 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

すみません、質問を追加させてください。

[ID] の Subset 作成についてですが、「RF
1/1 Power Class 1」はNoにする必要はございませんでしょうか？現在Yesになっています。

お手数ですが、こちらもご確認をよろしくお願いいたします。

酒井

From:
酒井重之 Shigeyuki Sakai

Sent: Wednesday, September 3, 2025 8:52 AM

To: Jun Wang

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

ご回答どうもありがとうございました。

[ID] の Subset 作成は急ぎ Qualcomm/Volvo へ説明し、対処するようにします。

LE のオプション機能についても理解いたしました。ご解説、大変助かります。

もし、 LE 2M PHY を付ける場合、試験期間と費用はどのくらい変化しますでしょうか？

酒井

From: Jun Wang

Sent: Tuesday, September 2, 2025 10:37 PM

To: 酒井重之 Shigeyuki Sakai

Subject: RE: 【ALAP】 [UXC] VCC
UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン酒井さんいつもお世話になります。アリオンの王君です。

標記Bluetooth認証登録につき、Q社DN情報の共有ありがとうございます。

以下いただいたご質問をインラインにて回答させていただきますので、

青字部分ご参照願います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Shigeyuki Sakai

Sent: Monday, September 1, 2025 8:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議王様お世話になります。

アルプスアルパイン酒井です。

Volvo から使用する DN の正式情報を入手しましたので、見積依頼書と共にご連絡いたします。

Volvo で Host や X2Core に独自に追加するものは無く、 Qualcomm より提供された DN
[ID] をそのまま使用するとのことです。

なお、 Chip の Component
DN も新しいものが連絡されてきました。 [ID] です。

Consistency check、必要試験の特定に進みたいのですが、その前に、以下の気になる点について確認させてください。

製品は Power Class 2 で認証取得したいのですが、 [ID] の LL
ICS 9/11 が YES です。そうすると、 HM26 のときにあった、 Power
Class の不整合問題に該当しますか？やはり。

回答：

はい、Q366226をIncludeし、RF PHYはSoCを製品基板に直実装のために必要な試験を実施するので

RF PHY 1/15:NOへの変更は問題ありませんが、併せて必要なLL　9/11：NOへ変更すると

LL ICSに紐付いた全試験項目が Test Plan として出力されます。

そこで購入契約者(V社あるいは御社)からQ社へ「Q366226のRF PHY 1/15:NOおよび

LL ICS 9/11:NOのSubsetを作成 （SIGへの支払は無料） して欲しい」と要求してください。

・見積依頼書内の“ RF PHY の必須機能以外のサポート機能“について、以下、確認させていただきたいです。

どれが必要な機能か、上記 DN から特定可能でしょうか？

回答：

IncludeするDNの内容でRF PHYの試験範囲が決まるのではなく、製品組込アプリがどこまでサポートしているかにより決定します。

車載器では見かけ上の伝搬速度を下げて遠くへ伝達させるCodedは不要かつStable xxxは不要かと思います。

2Mbpsは対向相手がサポートしていると自動でネゴシエートされますので使う可能性が高いです。

したがって必須1Mと2Mの試験実施でよろしいかと思います。

最終判断は製品アプリの開発担当部門へご確認ください。

また、今回不要な機能があったとしても、将来 Host 側に更新が入った場合に備え、 Controller 側では予備的に認証を取得しておく考え方はありますでしょうか？

回答：

もしQ社がHost Q370647のアップデートが予想され、V社もそれに追従しそうな場合には、

予備的にController部の部分登録・認証を取得しておけば将来のアップデート登録が楽に済みます。

以上、ご確認をよろしくお願いいたします。

酒井

From: Jun Wang

Sent: Friday, August 22, 2025 6:54 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

下記状況共有させていただきありがとうございます。

Q社DNが取得でき次第またご展開いただきますようお願いいたします。

引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Thursday, August 21, 2025 10:53 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

時間が空いてしまい、申し訳ございません。

Q社のDN情報について、現状をご連絡させていただきます。

弊社スウェーデンの現地法人を経由して、正式見積もりおよび認証開始に向けて、

V社に対して、Q社からX2Core及びCore complete(Host)のDN情報を早急に入手するように依頼しております。

入手でき次第に早急に展開させていただきますのでお待ち下さい。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, August 8, 2025 3:50 PM

To: 水野淳也 Junya Mizuno

Subject: Re: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ICS (Implementation Conformance Statements)は申請製品の機能記述として、

includedするQ社core completeのDN及びX2CoreのDN情報がないと、

免除できる試験項目を確定できず、見積のご提示が難しいです。

今回の試験内容的に、RF/RF PHY試験はQ社登録に不含ですので見積依頼書のP2の記載内容で確定していますが、

プロファイルはX2Core の登録内容と製品の実装内容の差異が明確にならないと確定見積ができません。

敢えて製品実装プロファイルは X2Core登録でカバーされ、製品でのプロファイル試験は発生しないという前提条件付の場合、見積は下記となります。

合計 ￥2,600,000（税抜）

内訳、

・RFフル項目試験・・・　￥1,200,000

・RF PHY(1M, 2M, Stable Mod Index-Tx,Stable Mod Index-Rx )試験・・・　￥1,000,000

・代行登録サポート(Multi-Design) ・・・　￥250,000

・コンプライアンスフォルダ作成費・・・・・・　￥150,000

Q社DNが明確になり次第、必ず費用見積を見直しさせていただきますので、

よろしくお願いいたします。

Outlook
for Android を取得差出人: Junya Mizuno

送信日時: 木曜日, 8月 7, 2025 8:23:11 午後宛先: Jun Wang

件名: RE: [UXC] VCC UCモデル向け Bluetooth SIG認証計画の共有/段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

DN提供が出来ておらず、申し訳ございません。

DNが無い場合、ICSでもお見積りが可能とのお話しを弊社深浦より聞きました。

ICSはV社経由で今週中に弊社に展開される予定ですが、現時点では展開されておりません。

今週までV社、および弊社含めて多くのメンバーが夏休みである為、来週中に展開される可能性が高いです。

弊社のスウェーデン現法メンバーに対して、来週中に途中段階でも良いのでICSを入手できるように依頼をします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, August 6, 2025 9:52 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

ご返信いただきありがとうございます。

Q社二つのDNとも取得中ということで現時点確定的なDN情報がない、

という状態になります。

折角見積依頼書をいただきまして大変申し訳ございませんが、

費用見積のご提示がない状況となります。

Q社DN取得でき次第で情報を展開いただきますと、

費用見積りのご提示が可能となりますので、

それまで少しお待ちいただきますようお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 6:04 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お問い合わせの件、ご回答させていただきます。

まだQ社でDN取得中、との理解でよろしいでしょうか。

はい、ご認識あっております。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

現在、V社より、w36(9/1～9/5)で利用可能になるとの連絡を受けております。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, August 5, 2025 4:29 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々すみません。

いただいたBluetooth見積依頼書では、Host Stackに関して

TBDとご記入されていますが、

まだQ社でDN取得中、との理解でよろしいでしょうか。

理解があっている場合、予定の取得時期について共有させていただきますと助かります。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, August 5, 2025 2:37 PM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth見積依頼書の更新をいただきありがとうございます。

BQCに試験対象項目を確認し、費用見積をご提示いたしますので、

少々お待ちくださいませ。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, August 5, 2025 8:30 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

対応が遅くなり、申し訳ございません、

Bluetooth見積書を更新しました。

補足としては、以下になります。

・ Core-controllerのDNを取得したい・以下のDNをincludeしてEnd productを登録したい取得したCore-controllerのDN

Qaulcommから提供された、RF/RF PHYが除かれたCore-Complete DN

Qaulcommから提供された、X2Core DN

・ RF PHYの必須機能以外のサポート機能は仮で記入した状態こちらの内容でお見積りをお願いします。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Wednesday, July 30, 2025 12:27 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

お忙しい中ご返信いただきありがとうございます。

RF/RF PHYの再試験を避ける為、Core-ControllerのDNを取得する方向で進めたいと思います。

弊社提案に合意をいただきありがとうございます。

現時点で埋められる部分を埋めて、ICS作成を進めるようにします。

ICSは登録内容を確定するためのものとして、

まずは見積書をご用意するにあたり、見積依頼書のご記入（更新）をお願いいたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 29, 2025 6:20 PM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

ご回答ありがとうございました。

また、こちらからの返信がかなり遅くなってしまい、申し訳ございません。

アリオン：はい、Core-ControllerのDNを取得のために1件の登録費用が発生しますが、

将来的にQ社登録が更新されても御社名義のDNをIncludeすることで再試験は回避できます。

承知しました。

RF/RF PHYの再試験を避ける為、Core-ControllerのDNを取得する方向で進めたいと思います。

アリオン：はい、登録内容を確定するという目的からはICSレベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須(1Mbps)および2Mbps」という具合に仮入力をお願いします。

承知しました。

現時点で埋められる部分を埋めて、ICS作成を進めるようにします。

また、BluetoothとWi-Fiは別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

承知しました。(賛成です)

取り急ぎ、本メールタイトルから「Wi-Fi Alliance」を外しました。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 1:02 PM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

Bluetooth認証に関する補足情報、また追加でいただいたご質問について、

下記回答させていただきます。※ 青字ご参照願います。

また、BluetoothとWi-Fiは別件名として、メールを分けて進めていきたいと考えますが、いかがでしょうか。

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

アリオン：承知いたしました。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

アリオン：原則的にはIncludeするCore-ControllerのDNが変われば再度RF/RF PHY試験を実施することになります。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

アリオン：はい、Core-ControllerのDNを取得のために1件の登録費用が発生しますが、

将来的にQ社登録が更新されても御社名義のDNをIncludeすることで再試験は回避できます。

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

アリオン：はい、登録内容を確定するという目的からはICSレベルの情報が不可欠です。

同時に見積金額確定には試験費用の確定が必要なため、当面「必須(1Mbps)および2Mbps」という具合に仮入力をお願いします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:20 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

度々失礼いたします。

費用見積に関して訂正させていただきます。

7/22日付の見積にはSubmission Feeを含めていないため、下記訂正させていただきます。※ 青字ご参照

AP

Staion

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDVを含む)

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$63,640

61

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Jun Wang

Sent: Tuesday, July 22, 2025 10:11 AM

To: Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

王君の説明不足で混乱させたようで申し訳ございません。

3ヵ月プランは基本形となっており、Wi-Fi 6/6e、Easymesh等Wi-Fi Featureの複雑化に従い、

Wi-Fi認証試験のL/Tも延びている状況となっている中、

3ヵ月プランもDUTのWi-Fi Featureの複雑度及び受験サンプル台数を基に調整しております今回のUXCは対象Wi-Fi Programも多いため、

サンプルを2～3セットのご提供をお願いいたしたいですが、

その場合、APとStationを各1台で試験を実施し、各3ヵ月の有効期限とさせていただきたいと考えます。

いかがでしょうか。

弊社側で記入を進め、V社に確認すべき部分は確認の上、提出とさせていただきます。

但し、V社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は8月下旬になる可能性が高いです。

弊社のWi-Fi見積依頼書の内容は概ねいただいているWorkSheetのStep3 Certification、一部Step4 Capabilityの内容となりまして、

まずは現時点で確定となっている内容だけの整理で構いませんので、お願いができますと幸いです。

Ｖ社夏休み明けに確認必要な内容整理にもなると思います。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Tuesday, July 22, 2025 8:56 AM

To: Jun Wang

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

お返事をいただき、ありがとうございました。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

⇒　試験費用や標準日程をWi-Fi Program別に整理いたしました、ご参照願います。

※下記試験費用や日程には、Mandatory 項目しか含めておりません；

実際DUTがOptional項目もサポートし、CIDとして登録内容に含めたい場合、試験費用や日程も変わります。

※下記Test L/Tは標準のLead Timeとして、再試験は含んでおりません。

Test LTに関して、念のために認識合わせをさせて下さい。

現在、三か月プランでのお見積りをいただいていると思いますが、現在の試験プログラムの合計Test LTは61日になっております。

一月の稼働日を20～22日で計算した場合、三か月は最大でも66日程度になる為、基本的には再試験をする日数は無いと認識しました。

こちらの認識はあっているでしょうか？

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

⇒　ラボに確認いたしますので少々お待ちください。

お手数ですが、ご確認をお願いします。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

承知しました。

弊社側で記入を進め、V社に確認すべき部分は確認の上、提出とさせていただきます。

但し、V社含むスウェーデンは夏休み中であり、我々のお盆休み期間に戻ってくる為、ご提出は8月下旬になる可能性が高いです。

以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Tuesday, July 22, 2025 7:48 AM

To: 水野淳也 Junya Mizuno

Subject: RE: [UXC] VCC UC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様いつもお世話になります、アリオンの王君です。

先週の打ち合わせ、お時間ありがとうございました。

製品サンプルを拝見できて、より働く価値を身に感じまして、感謝いたします。

Bluetoothに関して、確認して別途回答いたします。

Wi-Fiに関して下記二点弊社側の宿題事項について下記回答いたします。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

⇒ 試験費用や標準日程を W i-Fi
Program別に整理いたしました、ご参照願います。

※下記試験費用や日程には、Mandatory 項目しか含めておりません；

実際DUTがOptional項目もサポートし、CIDとして登録内容に含めたい場合、試験費用や日程も変わります。

※下記Test L/Tは標準のLead Timeとして、再試験は含んでおりません。

AP

Station

Test Fee

Test L/T

Test Fee

Test L/T

Certified 6 R2

$13,200

12

$13,200

12

Certified N(WPA2, WMM, SDVを含む)

$3,300

5

$3,300

5

Certified ac

$3,850

4

$3,850

4

PMF

$720

2

$720

2

FFD

$2,200

2

$2,200

2

WPA3 R3 Personal

$2,200

2

$3,300

3

Agile Multiband

×

-

$3,300

3

Forward Compatibility

$1,100

1

$2,200

2

Sub Total

$26,570

28

$32,070

33

Submission Fee

$5,000

TTL

$58,640

61

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

⇒　ラボに確認いたしますので少々お待ちください。

また、下記王君からのお願いも、ご面倒をおかけいたしますが、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

よろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

From: Junya Mizuno

Sent: Friday, July 18, 2025 3:40 PM

To: Jun Wang

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アリオン王様いつもお世話になっております。アルプスアルパインの水野です。

昨日は遠い中、弊社までお越しいただき、ありがとうございました。

Bluetooth認証登録書、Wi-Fi　新規認証（New Certification）につきましては、弊社側で最新内容に更新します。

Bluetooth認証登録書の更新にあたり、何点かご確認した内容があります。以下の質問に対して、ご回答をお願いできますでしょうか？

·
（補足） Include する [ID] は H 社向け CDC と同じ DN です。

·
（補足） アリオン酒井さんに以前教えていただいた以下の理解のもと、記入しています。

Qualcomm の登録は特殊で、 Core-Complete から RF/RF
PHY を除いた階層を登録と Profile を X2Core として登録するのが通例で、製品登録では製品で RF/RF
PHY

試験を実施してそれをエビデンスに Q 社登録を Include して RF/RF
PHY 階層を加えるとともに

Q 社の X2Core(Profile) 登録も Include します。

·
（質問） 上記の製品登録の仕方では Core-Controller の DN を取得せず RF/RF
PHY 試験レポートだけをエビデンスに使用しますが、

将来 Qualcomm 社の RF/RF
PHY 無し Core-Complete 側が更新された場合に、 RF/RF
PHY もまた試験することになりますか？

そうである場合に、今のうちに Core-Controller の DN を取得しておけば、 RF/RF
PHY の再試験は避けられますか？

·
（質問） “ RF PHY の必須機能以外のサポート“ですが、まだ埋められていません。ここは、 ICS が揃ってから判断できるものかと思っていますが、合っていますでしょうか？

Wi-Fi認証の事前試験については、アリオン様でお見積り済みのLT情報も踏まえて、判断したいと考えています。

以下は昨日の議事メモ内になります。( 黄色塗りつぶしは宿題事項となっております)

その中でも依頼事項として記載しておりますのでご展開をお願いします。

【[ID]】

ü
試験拠点は以下の通り。

Ø
PTS IOPT : 日本

Ø
Controller(PHY) : 日本 or 中国 or 台湾　※[ID] 見積依頼書の内容を基にAllion様側で判断予定。

ü
想定される試験期間は以下の通り。(=現状、それぞれ三か月を見込んでいる為、計画内で完了する見通し)

Ø
PTS IOPT : 2~3回の不具合修正/再テスト含めて、8週間。(IOPTだけなので更に短いLTで完了できる見通し)

Ø
Controller(PHY) : 一か月(MAX)

ü
[ID] 見積依頼書を更新してAllion様に提出する・・・ALAP 水野

【WFA】

ü
WFA認証プランは三か月プランが一般的であり、先日頂いたお見積りも三か月プランの費用になる。

Ø
1回目の試験は、NGが出ても試験できる項目を全て通して実施する。(NGにより試験出来ない項目はSkip)

Ø
2回目の試験は、基本的にNG項目を再試験するが、NG項目に関連する項目は再試験する場合もあり。

ü
お見積りをいただいたWFAプログラム(2.4/5GHz)の場合、1回の試験でどれくらいのLT想定になるか、情報を展開いただく・・・Allion 王様

ü
試験場所は、中国 or 台湾になる。(基本的には台湾が多くの試験設備を保持している為、台湾になる見込み)

ü
事前検証をAllion様に依頼する場合、全ての項目を依頼するか、V社と協議の上、心配項目を依頼するか、判断する・・・ALAP 水野

ü
Android OS バージョンアップがWFA試験に影響するかについて、関連するWFAからの公開情報を展開いただく・・・Allion 王様

Ø
VolvoにAndroid OSのバージョンアップがWFA認証に影響することを説明するために利用したい以上です。

宜しくお願いします。

+ アルプスアルパイン株式会社 DC1設計部開発2G 22T(INF OEM PM) 水野淳也

+ E-mail :

From: Jun Wang

Sent: Friday, July 18, 2025 10:29 AM

To: 水野淳也 Junya Mizuno ;
酒井重之 Shigeyuki Sakai

Subject: RE: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議アルプスアルパイン水野様、酒井様いつもお世話になります、アリオンの王君です。

昨日はお忙しい中お時間をいただきありがとうございました。

UXCの開発及びBluetooth＆Wi-Fi認証に向けた最新日程の共有、ありがとうございます。

·
Bluetooth認証登録

24年9月にいただきました見積依頼書を添付いたします。

ご更新いただき、弊社より試験対象項目及び見積をご提示いたしますので、よろしくお願いいたします。

·
Wi-Fi　新規認証（New Certification）

御社フォームのWorkSheetをいただいておりますが、

VCC Comment、QC Commentも併記されている中、現時点の最終仕様で添付の「Wi-Fi認証見積依頼確認書」にご記入いただきたいですが、お願いができますと助かります。

ご記入いただいた内容で正式見積書をご用意いたします。

·
Wi-Fi認証の事前試験に関して、御社別部隊からもよく「事前試験＋本番試験」でご依頼をいただいております。

本番試験をスムーズに進められるように、事前に一通り試験を回しておく、

もしくは一部気になるProgram/項目を確認しておくことをお勧めいたします。

·
CSDに関して、いろいろご調整いただき誠にありがとうございます。

CSDを除いたDUT本体やケーブル類は本社日本から、CSDは御社中国から、

ご提供される予定との旨、承知いたしました。

試験に向けて引き続きよろしくお願いいたします。

アリオン株式会社営業統括部営業王君（ワン・ジュン）

-----Original Appointment-----

From: Jun Wang On Behalf Of Junya Mizuno

Sent: Thursday, July 17, 2025 12:59 PM

To: Doyen

Subject: FW: [UXC] VCC UXC モデル向け Bluetooth SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議

When: 2025 年 7 月 17 日木曜日 13:00-14:00
(UTC+09:00) 大阪、札幌、東京

Where: 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議差出人 : Junya Mizuno

送信日時 : 2025 年 7 月 8 日 16:55:10
(UTC+09:00) Osaka, Sapporo, Tokyo

宛先 : Junya Mizuno ;
Jun Wang ;
Itsuo Sakai ;
Shigeyuki Sakai ;
Hiroaki Fukaura

件名 : [UXC] VCC UXC モデル向け Bluetooth
SIG/Wi-Fi Alliance 認証計画の共有 / 段取りの協議開催日 : 2025 年 7 月 17 日 13:00
- 14:00。

場所 : 5 号棟 2F-R2 会議室 (52-R2),;
Microsoft Teams 会議アリオン王様、酒井様いつもお世話になっております。アルプスアルパインの水野です。

大変遅くなってしまい申し訳ございません。

V社ソフトリリース日程、Display(CSD)入手見込みが固まってきましたので、

最新状況を反映したBluetooth SIG/Wi-Fi Alliance認証計画を作成中です。

最新認証計画を基に、認証計画の共有、認証に向けた段取りの協議をさせて下さい。

※最新認証計画は7/11(金)までに送付させていただきます。

以上です。

宜しくお願いします。

________________________________________________________________________________

Microsoft Teams
ヘルプが必要ですか ?

今すぐ会議に参加する会議 ID:
460 795 130 830 7

パスコード :
db6Xf3X4

開催者向け :
会議オプション

________________________________________________________________________________
