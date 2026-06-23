# thread_0025: Re: [ID]/認証見積のお願い

- Message count: 9
- Source JSON: `thread_0025.json`

---

## 1. 2024-09-05 10:32

**From:** Itsuo Sakai
**To:** =?utf-8?B?Tm9tdXJhIFl1c3VrZSAvIOmHjuadkSDoo5Xku4s=?=

ホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように7/1に新登録サイトに更新されました。新登録サイトでは従来Controller Subsystemと

Host Subsystemの組み合わせ登録では一律チェックが除外されていたDeclaration登録相当の登録でデザイン番号(DN)が付与されない登録と、階層間不整合チェックを行ってデザイン番号(DN)が付与されない登録が可能です。前者は御社が製品を発売する場合ならばDNが付与されなくても問題ありませんが、

御社がOEM供給する場合にはDNがあれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方DNが付与される登録のために、今回見積依頼書に記載いただいたD065101 (QDID：[ID])とD043119

(QDID：[ID])の組み合わせで私のWorkspaceで仮Projectを作成してConsystency Checkを実施すると後述の(1)の階層間不整合が検出されました。これらの不整合はGAPあるいはLLのどちらかのICSを修正することで解消可能ですが、新サイトではICSを修正した階層のICSに対応した試験要求が発生します。

GAPはExcuded(YES→NOにせよ)ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory項目が山のように出だしたので途中で止めました。DNが付与される登録をご希望の場合は

SoCのLLが(3)をサポートしているものに変更するか、ホストスタックのGAPが(2)をサポートしていないものを選択し直してください。

結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID

の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

その場合の見積は下記の通りです。

・RF PHY試験（1M, 2M） ￥700,000

・代行登録サポート費(Multi-Design参照) ￥250,000

・コンプライアンスフォルダ作成費 ￥150,000

旧Declaration登録相当の登録（DNは付与されない）で支障がないかご検討ください。

(1) <階層間不整合一覧>

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAPの関連ICSの機能は下記の通りです。>

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LLの関連ICS機能は以下の通りです。>

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人: Nomura Yusuke / 野村裕介

送信日時: 2024年9月5日 17:05

宛先: Itsuo Sakai

件名: RE: [ID]/認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

---

## 2. 2024-09-19 10:11

**From:** Itsuo Sakai
**To:** =?utf-8?B?Tm9tdXJhIFl1c3VrZSAvIOmHjuadkSDoo5Xku4s=?= , =?utf-8?B?SG9yaSBNYXNha2kgLyDloIAg6ZuF5qi5?=
**Attachments:** Outlook-ce4sfrfd.png, Outlook-5l4mff0y.png, Outlook-24godgqu.png, Outlook-31cvqnfq.png, Outlook-2svrxkjz.png, Outlook-hymiomcv.png, Outlook-2sdpm1o5.png, Outlook-3yrip5cy.png

ホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な”見積書”を書面で送付お願いします。

⇒承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・RF PHY試験（1M） ￥400,000

・代行登録サポート費( Single -Design参照 ) ￥150,000

・コンプライアンスフォルダ作成費 ￥150,000

以上よろしくお願いいたします。

差出人: Nomura Yusuke / 野村裕介

送信日時: 2024年9月19日 18:57

宛先: Itsuo Sakai ; Hori Masaki / 堀雅樹

件名: RE: [再送：ご提案] Re: [ID]/認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID]
(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように｢ Combine
unmodified Designs ｣を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は｢ Details ｣という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように｢ Combine
unmodified Designs ｣を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は｢ Details ｣という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。
結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID
の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

→上記の内容についてですが、これは下記のように｢Combine unmodified Designs｣を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。(添付参照)

ただ、DNが付与されない登録になり、DNは｢Details｣という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
｢ [ID] ｣をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
｢ [ID] ｣をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

｢[ID]｣をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Numberが！表記なのは登録費 (旧Declaration ID)を設定していないためです。

[質問事項]

・DN (Design Number)が「Default」表記になることのデメリット、問題点はないのか？

・Q30から始まるQDIDのみで再ブランド化した場合、Bluetooth認証上は問題ないのか？

単にDNがDefault表示になるだけ、QDIDが「Q30～」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先にHRM5141として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードはBLE1Mのみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

---

## 3. 2024-09-19 10:16

**From:** Itsuo Sakai
**To:** Masaya Iida
**Attachments:** Outlook-rzt2jfsi.png, Outlook-fzpzzia2.png, Outlook-stljpppr.png, Outlook-ep0hdys4.png, Outlook-vsrgb3qo.png, Outlook-agfvf2b2.png, Outlook-ozmlumod.png, Outlook-hrtz2rfb.png

飯田さんお疲れさまです。

下記内容でホシデン野村様へ見積書を発行・送付してください。

・RF PHY試験（1M） ￥400,000

・代行登録サポート費(Single -Design参照) ￥150,000

・コンプライアンスフォルダ作成費 ￥150,000

ーーーー

<宛先>

野村裕介ホシデン株式会社技術本部第二技術部技術三課

---

## 4. 2024-09-26 04:44

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?Tm9tdXJhIFl1c3VrZSAvIBskQkxuQjwbKEIgGyRCTTUycBsoQg==?= , =?iso-2022-jp?B?SG9yaSBNYXNha2kgLyAbJEJLWRsoQiAbJEIybTx5GyhC?=
**Attachments:** Outlook-kirfpflo.png, Outlook-2xul5vyn.png, Outlook-kmbksnwc.png, Outlook-ts2xfcol.png, Outlook-ezlx14eb.png, Outlook-yagj44ec.png, Outlook-sw2pjpgw.png, Outlook-4illq4pu.png

ホシデン野村様アリオンの酒井です。いつもお世話になっております。
見積書はまだ掛かりそうでしょうか？
いつ提出できるのかを回答お願いします。

⇒見積が遅延しており失礼しました。本日中にメール添付で送付予定です。
御社で使用されるBTテスタのメーカー名と品番を参考に教えて頂けないでしょうか？
弊社ではRohde & Schwarz製のものを使用しています。

⇒SIG認定RFテストシステムとしてInterLab RF Test Solutionを設置しています。シグナリングユニットにR&S社CMW270が組み込まれていますが合否判定は統制制御ユニット(Windows Board PC)

上の管理アプリによってRF/RF PHYテスト仕様書に忠実に準拠しています。(RFテスタ単体は試験内容が一部テスト仕様書と異なっています。)

以上回答いたします。

差出人: Nomura Yusuke / 野村裕介

送信日時: 2024年9月26日 12:33

宛先: Itsuo Sakai ; Hori Masaki / 堀雅樹

件名: RE: [再送：ご提案] Re: [ID]/認証見積のお願いアリオン酒井様いつもお世話になっております。

見積書はまだ掛かりそうでしょうか？

いつ提出できるのかを回答お願いします。

御社で使用されるBTテスタのメーカー名と品番を参考に教えて頂けないでしょうか？

弊社ではRohde & Schwarz製のものを使用しています。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 7:12 PM

To: Nomura Yusuke / 野村裕介 ; Hori Masaki /
堀雅樹

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

⇒ 承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・ RF PHY 試験（1M）

￥ 400,000

・代行登録サポート費 ( Single
-Design 参照 ) ￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上よろしくお願いいたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 19 日 18:57

宛先 : Itsuo Sakai ;
Hori Masaki / 堀雅樹

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように Combine unmodified
Designs #を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は Details #という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように Combine unmodified
Designs #を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は Details #という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。
結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID
の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

→上記の内容についてですが、これは下記のようにCombine unmodified Designs#を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。(添付参照)

ただ、DNが付与されない登録になり、DNはDetails#という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
" [ID] #をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
" [ID] #をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

"[ID]#をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Numberが！表記なのは登録費 (旧Declaration ID)を設定していないためです。

[質問事項]

・DN (Design Number)が「Default」表記になることのデメリット、問題点はないのか？

・Q30から始まるQDIDのみで再ブランド化した場合、Bluetooth認証上は問題ないのか？

単にDNがDefault表示になるだけ、QDIDが「Q30〜」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先にHRM5141として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードはBLE1Mのみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

---

## 5. 2024-11-04 03:42

**From:** Itsuo Sakai
**To:** =?utf-8?B?SG9yaSBNYXNha2kgLyDloIAg6ZuF5qi5?= , =?utf-8?B?Tm9tdXJhIFl1c3VrZSAvIOmHjuadkSDoo5Xku4s=?=

ホシデン野村様、堀様アリオンの酒井です。いつもお世話になっております。

RF PHY試験がPass完了しましたので早速ですが今後の進め方をご案内します。

(1) 添付の代行登録内容確認書にご記入の上、ご返送ください。ログイン情報はInvoiceを取得された方と同一アカウントをご記入ください。

(2) 当方で認証登録に必要な作業を行い、Reviewページの内容を添付して確認依頼メールを送ります。

(3) 内容ご確認いただき登録指示メール受信後、登録確定操作を行います。1-2営業日以内にSIGの承認が完了して認証登録が有効になります。表示開始日指定登録ではその日から一般公開されます。

(4) コンプライアンスフォルダ作成のために、RF PHYレポートおよび登録過程で取得したドキュメントとともに以下の資料をご提出ください。

① モジュールの仕様書

② モジュールのブロック図

③ モジュールの外形図

④ 実装されたアンテナデータシート(放射利得特性を含むもの)

以上よろしくお願いいたします。

差出人: Toshitaka Mochizuki

送信日時: 2024年11月1日 19:12

宛先: Hori Masaki / 堀雅樹 ; Nomura Yusuke / 野村裕介 ; Masaya Iida

件名: Re: [再送：ご提案] Re: [ID]/認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

大変お待たせいたしました。

予定より早くRF試験が完了いたしましたのでレポートをお送りいたします。

以下のPasswordにてダウンロードください。

[パスワード]

z2kzM&quot;*M

[パスワード有効期限]

[ID] 19:10 まで

[送信ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人: Toshitaka Mochizuki

送信日時: 2024年11月1日 16:14

宛先: Hori Masaki / 堀雅樹 ; Nomura Yusuke / 野村裕介 ; Masaya Iida

件名: Re: [再送：ご提案] Re: [ID]/認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントありがとうございます。

本日試験を日本で開始できました。

そのため、ご準備いただきましたが、今回台湾への発送は行う必要がなくなりました。

週明けまでには結果をお知らせできる予定です。

もうしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人: Hori Masaki / 堀雅樹

送信日時: 2024年10月31日 18:32

宛先: Toshitaka Mochizuki ; Nomura Yusuke / 野村裕介 ; Masaya Iida

件名: RE: [再送：ご提案] Re: [ID]/認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

機材提出票を添付致しますので、ご確認お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 5:02 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントご送付ありがとうございます。

確認いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Thursday, October 31, 2024 3:40 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

ご連絡ありがとうございます。日本での試験実施をお願い致します。

[ID]docと試験手順書を提出致しますので、ご確認お願い致します。

機材提出票は、別途提出致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 11:55 AM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡ありがとうございます。

先ほどサンプルが到着いたしました。

[ID]docのご提出をいただき、

テストプラン作成後試験開始となります。

出来るだけお早目のご提供お願いいたします。

こちらのサンプルですが、テストモードに入るための手順などはございますでしょうか。

ある場合はその手順もお知らせください。

また、後程で良いですので添付の機材提出票のファイルにご記入の上ご返送ください。

試験なのですが、キャンセルが発生したため、

今日、明日であれば日本で実施いたします。

もし遅くなるようでしたら台湾実施の検討となります。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Wednesday, October 30, 2024 5:03 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

試験サンプルを望月様宛てに、10/31午前着で発送致しました。

[ID]docについては、明日提出致します。

【便名】 ヤマト運輸

【送り状No.】 [ID]

【お届け予定日】 10/31 AM着指定

【その他】ヤマト運輸の箱での発送です。

【発送物】[ID]/Bluetooth SIG認証サンプル以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Tuesday, October 29, 2024 3:50 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

種々ご準備いただきありがとうございます。

試験サンプルと [ID]doc ですが、

明日もしくは３１日の当社日本側到着は可能でしょうか。

サンプルは以下の私のフッタの私宛てへのご発送となります。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 10 月 25 日 17:18

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

以下となります。

[ID] LABS, INC.

９F, No.3-1, Yuan Ku Street

[ID] [ID] PARK BLD.G

Taipei, [ID] CITY 11503

Add: 11503台北市南港區園區街3-1號9樓(南港軟體園區G棟)

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Friday, October 25, 2024 5:10 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

下記承知致しました。

サンプルの送付先(台湾ラボ)の名前と住所をご教授お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Friday, October 25, 2024 11:29 AM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン野村様堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

日本側でキャンセル等発生した場合は対応可能ですが、不確定ですので、

台湾でも実施できるよう進めてまいります。

台湾輸出に当たり、該否判定書など御社書式でご準備いただけますでしょうか。

また、添付の税関等で使用する製品の画像入りの仕様書のご記入と、お預かりサンプル一覧のご記入もお願い申し上げます。

また、製品の接続、操作説明（英文もしくは中文）もいただけますでしょうか。

大変お手数おかけいたしますが、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Nomura Yusuke /
野村裕介

Sent: Friday, October 25, 2024 8:13 AM

To: Toshitaka Mochizuki ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン㈱ 望月様いつもお世話になっております。

台湾のラボでの試験でもOKです。

日程優先で進めてください。

⇒堀さん添付資料をしあげて提出お願いします。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Toshitaka Mochizuki

Sent: Thursday, October 24, 2024 6:53 PM

To: Hori Masaki / 堀雅 Γ 彊児 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認 Γ 恐孜見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

Bluetooth 試験の方ですが実際の試験につきましては

PM の望月よりご案内いたします。

試験日程なのですが、 10 月 29 日以降ですと、空いている日程が

11 月下旬となってしまうため、調整しておりますが、

例えば当社台湾でのご受験は可能でしょうか。

ご検討お願いいたします。

また、添付の [ID]doc にご記入の上、

ご返送いただけますでしょうか。

テストプランを作成いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 23 日 14:28

宛先 : Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

返信が遅くなり申し訳ありません。

サンプルの準備に時間を要しておりましたが、10/29頃にサンプルの発送を予定しております。

試験開始日は、サンプルが届き次第、なるべく早い日で実施をお願いしたく、

お手数をおかけしますが、日程調整をお願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Tuesday, October 1, 2024 4:24 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン堀様いつもお世話になっております。

アリオンの飯田です。

注文書のご提出ありがとうございます。

ご注文を承ります。
サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？

問題ございません。
サンプルは何台必要でしょうか？

1台で結構です。

サンプル準備については添付内容をご参照くださいませ。

ご希望の試験開始日はございますでしょうか。

サンプルはいつ頃提出可能な見込みでしょうか。

日程調整いたしますので、ご回答のほどよろしくお願いいたします。

また、サンプル提出先については以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社 KSTC 営業部 PM 望月宛以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Hori Masaki /
堀雅樹

Sent: Tuesday, October 1, 2024 2:49 PM

To: Masaya Iida ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

注文書を発行致しましたので、添付をご確認お願い致します。

また、提出するサンプルに関して、お手数をおかけしますが、以下の質問にご回答をお願い致します。

・サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？(セミリジットケーブル付き)

・サンプルは何台必要でしょうか？

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Thursday, September 26, 2024 1:46 PM

To: Nomura Yusuke / 野村裕介 ;
Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様いつもお世話になっております。

アリオンの飯田です。

お待たせをして申し訳ございません。

見積書を発行いたしました。

添付致します。ご検討のほどよろしくお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Nomura Yusuke /
野村裕介

Sent: Thursday, September 26, 2024 12:34 PM

To: Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

見積書はまだ掛かりそうでしょうか？

いつ提出できるのかを回答お願いします。

御社で使用されるBTテスタのメーカー名と品番を参考に教えて頂けないでしょうか？

弊社ではRohde & Schwarz製のものを使用しています。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 7:12 PM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

⇒ 承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・ RF PHY 試験（1M）

￥ 400,000

・代行登録サポート費 ( Single
-Design 参照 ) ￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上よろしくお願いいたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 19 日 18:57

宛先 : Itsuo Sakai ;
Hori Masaki / 堀雅樹

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID]
(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine
unmodified Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine
unmodified Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。
結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID
の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

→上記の内容についてですが、これは下記のように「Combine unmodified Designs」を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。(添付参照)

ただ、DNが付与されない登録になり、DNは「Details」という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

「[ID]」をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Numberが！表記なのは登録費 (旧Declaration ID)を設定していないためです。

[質問事項]

・DN (Design Number)が「Default」表記になることのデメリット、問題点はないのか？

・Q30から始まるQDIDのみで再ブランド化した場合、Bluetooth認証上は問題ないのか？

単にDNがDefault表示になるだけ、QDIDが「Q30～」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先にHRM5141として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードはBLE1Mのみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

---

## 6. 2024-11-04 03:56

**From:** Itsuo Sakai
**To:** =?utf-8?B?SG9yaSBNYXNha2kgLyDloIAg6ZuF5qi5?= , =?utf-8?B?Tm9tdXJhIFl1c3VrZSAvIOmHjuadkSDoo5Xku4s=?=
**Attachments:** ���������������������������.doc

ホシデン野村様、堀様アリオンの酒井です。いつもお世話になっております。

(先のメールで添付ファイルを失念したため再送します。)

RF PHY試験がPass完了しましたので早速ですが今後の進め方をご案内します。

(1) 添付の代行登録内容確認書にご記入の上、ご返送ください。ログイン情報はInvoiceを取得された方と同一アカウントをご記入ください。

(2) 当方で認証登録に必要な作業を行い、Reviewページの内容を添付して確認依頼メールを送ります。

(3) 内容ご確認いただき登録指示メール受信後、登録確定操作を行います。1-2営業日以内にSIGの承認が完了して認証登録が有効になります。表示開始日指定登録ではその日から一般公開されます。

(4) コンプライアンスフォルダ作成のために、RF PHYレポートおよび登録過程で取得したドキュメントとともに以下の資料をご提出ください。

① モジュールの仕様書

② モジュールのブロック図

③ モジュールの外形図

④ 実装されたアンテナデータシート(放射利得特性を含むもの)

以上よろしくお願いいたします。

差出人: Toshitaka Mochizuki

送信日時: 2024年11月1日 19:12

宛先: Hori Masaki / 堀雅樹 ; Nomura Yusuke / 野村裕介 ; Masaya Iida

件名: Re: [再送：ご提案] Re: [ID]/認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

大変お待たせいたしました。

予定より早くRF試験が完了いたしましたのでレポートをお送りいたします。

以下のPasswordにてダウンロードください。

[パスワード]

z2kzM&quot;*M

[パスワード有効期限]

[ID] 19:10 まで

[送信ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人: Toshitaka Mochizuki

送信日時: 2024年11月1日 16:14

宛先: Hori Masaki / 堀雅樹 ; Nomura Yusuke / 野村裕介 ; Masaya Iida

件名: Re: [再送：ご提案] Re: [ID]/認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントありがとうございます。

本日試験を日本で開始できました。

そのため、ご準備いただきましたが、今回台湾への発送は行う必要がなくなりました。

週明けまでには結果をお知らせできる予定です。

もうしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人: Hori Masaki / 堀雅樹

送信日時: 2024年10月31日 18:32

宛先: Toshitaka Mochizuki ; Nomura Yusuke / 野村裕介 ; Masaya Iida

件名: RE: [再送：ご提案] Re: [ID]/認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

機材提出票を添付致しますので、ご確認お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 5:02 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントご送付ありがとうございます。

確認いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Thursday, October 31, 2024 3:40 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

ご連絡ありがとうございます。日本での試験実施をお願い致します。

[ID]docと試験手順書を提出致しますので、ご確認お願い致します。

機材提出票は、別途提出致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 11:55 AM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡ありがとうございます。

先ほどサンプルが到着いたしました。

[ID]docのご提出をいただき、

テストプラン作成後試験開始となります。

出来るだけお早目のご提供お願いいたします。

こちらのサンプルですが、テストモードに入るための手順などはございますでしょうか。

ある場合はその手順もお知らせください。

また、後程で良いですので添付の機材提出票のファイルにご記入の上ご返送ください。

試験なのですが、キャンセルが発生したため、

今日、明日であれば日本で実施いたします。

もし遅くなるようでしたら台湾実施の検討となります。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Wednesday, October 30, 2024 5:03 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

試験サンプルを望月様宛てに、10/31午前着で発送致しました。

[ID]docについては、明日提出致します。

【便名】 ヤマト運輸

【送り状No.】 [ID]

【お届け予定日】 10/31 AM着指定

【その他】ヤマト運輸の箱での発送です。

【発送物】[ID]/Bluetooth SIG認証サンプル以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Tuesday, October 29, 2024 3:50 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

種々ご準備いただきありがとうございます。

試験サンプルと [ID]doc ですが、

明日もしくは３１日の当社日本側到着は可能でしょうか。

サンプルは以下の私のフッタの私宛てへのご発送となります。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 10 月 25 日 17:18

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

以下となります。

[ID] LABS, INC.

９F, No.3-1, Yuan Ku Street

[ID] [ID] PARK BLD.G

Taipei, [ID] CITY 11503

Add: 11503台北市南港區園區街3-1號9樓(南港軟體園區G棟)

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Friday, October 25, 2024 5:10 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

下記承知致しました。

サンプルの送付先(台湾ラボ)の名前と住所をご教授お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Friday, October 25, 2024 11:29 AM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン野村様堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

日本側でキャンセル等発生した場合は対応可能ですが、不確定ですので、

台湾でも実施できるよう進めてまいります。

台湾輸出に当たり、該否判定書など御社書式でご準備いただけますでしょうか。

また、添付の税関等で使用する製品の画像入りの仕様書のご記入と、お預かりサンプル一覧のご記入もお願い申し上げます。

また、製品の接続、操作説明（英文もしくは中文）もいただけますでしょうか。

大変お手数おかけいたしますが、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Nomura Yusuke /
野村裕介

Sent: Friday, October 25, 2024 8:13 AM

To: Toshitaka Mochizuki ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン㈱ 望月様いつもお世話になっております。

台湾のラボでの試験でもOKです。

日程優先で進めてください。

⇒堀さん添付資料をしあげて提出お願いします。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Toshitaka Mochizuki

Sent: Thursday, October 24, 2024 6:53 PM

To: Hori Masaki / 堀雅 Γ 彊児 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認 Γ 恐孜見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

Bluetooth 試験の方ですが実際の試験につきましては

PM の望月よりご案内いたします。

試験日程なのですが、 10 月 29 日以降ですと、空いている日程が

11 月下旬となってしまうため、調整しておりますが、

例えば当社台湾でのご受験は可能でしょうか。

ご検討お願いいたします。

また、添付の [ID]doc にご記入の上、

ご返送いただけますでしょうか。

テストプランを作成いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 23 日 14:28

宛先 : Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

返信が遅くなり申し訳ありません。

サンプルの準備に時間を要しておりましたが、10/29頃にサンプルの発送を予定しております。

試験開始日は、サンプルが届き次第、なるべく早い日で実施をお願いしたく、

お手数をおかけしますが、日程調整をお願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Tuesday, October 1, 2024 4:24 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン堀様いつもお世話になっております。

アリオンの飯田です。

注文書のご提出ありがとうございます。

ご注文を承ります。
サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？

問題ございません。
サンプルは何台必要でしょうか？

1台で結構です。

サンプル準備については添付内容をご参照くださいませ。

ご希望の試験開始日はございますでしょうか。

サンプルはいつ頃提出可能な見込みでしょうか。

日程調整いたしますので、ご回答のほどよろしくお願いいたします。

また、サンプル提出先については以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社 KSTC 営業部 PM 望月宛以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Hori Masaki /
堀雅樹

Sent: Tuesday, October 1, 2024 2:49 PM

To: Masaya Iida ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

注文書を発行致しましたので、添付をご確認お願い致します。

また、提出するサンプルに関して、お手数をおかけしますが、以下の質問にご回答をお願い致します。

・サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？(セミリジットケーブル付き)

・サンプルは何台必要でしょうか？

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Thursday, September 26, 2024 1:46 PM

To: Nomura Yusuke / 野村裕介 ;
Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様いつもお世話になっております。

アリオンの飯田です。

お待たせをして申し訳ございません。

見積書を発行いたしました。

添付致します。ご検討のほどよろしくお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Nomura Yusuke /
野村裕介

Sent: Thursday, September 26, 2024 12:34 PM

To: Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

見積書はまだ掛かりそうでしょうか？

いつ提出できるのかを回答お願いします。

御社で使用されるBTテスタのメーカー名と品番を参考に教えて頂けないでしょうか？

弊社ではRohde & Schwarz製のものを使用しています。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 7:12 PM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

⇒ 承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・ RF PHY 試験（1M）

￥ 400,000

・代行登録サポート費 ( Single
-Design 参照 ) ￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上よろしくお願いいたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 19 日 18:57

宛先 : Itsuo Sakai ;
Hori Masaki / 堀雅樹

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID]
(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine
unmodified Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine
unmodified Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。
結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID
の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

→上記の内容についてですが、これは下記のように「Combine unmodified Designs」を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。(添付参照)

ただ、DNが付与されない登録になり、DNは「Details」という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

「[ID]」をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Numberが！表記なのは登録費 (旧Declaration ID)を設定していないためです。

[質問事項]

・DN (Design Number)が「Default」表記になることのデメリット、問題点はないのか？

・Q30から始まるQDIDのみで再ブランド化した場合、Bluetooth認証上は問題ないのか？

単にDNがDefault表示になるだけ、QDIDが「Q30～」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先にHRM5141として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードはBLE1Mのみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee™W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

---

## 7. 2024-11-05 02:27

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki , Masaya Iida

望月さんお疲れさまです。

HOSIDEN様RF PHYレポート記載内容に変更依頼がありました。
また、先日頂いたテストレポートに関して、
お手数をおかけしますが、製品名(英文)をWristband activity trackerに変更お願い致します。

客先へ展開後ですのでレビュジョン管理を行って製品名変更レポートを発行してください。

酒井差出人: Hori Masaki / 堀雅樹

送信日時: 2024年11月5日 11:05

宛先: Nomura Yusuke / 野村裕介 ; Itsuo Sakai

件名: RE: [再送:今後の進め方のご案内] [再送：ご提案] Re: [ID]/認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀です。

資料を提出致しますので、ご確認お願い致します。

仕様書と外形図はBluetooth ICのデータシートをご確認お願い致します。

ブロック図は無線部を中心に記載しております。Bluetooth ICのブロック図はデータシートから抜粋したものとなります。

また、先日頂いたテストレポートに関して、

お手数をおかけしますが、製品名(英文)をWristband activity trackerに変更お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Nomura Yusuke /
野村裕介

Sent: Tuesday, November 5, 2024 9:56 AM

To: Itsuo Sakai ; Hori Masaki / 堀雅樹

Subject: RE: [ 再送 : 今後の進め方のご案内 ]
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

RF-PHYの試験およびレポートの送付ありがとうございました。

代行登録内容確認書を添付の通り提出致します。

下記資料に関しては、別途堀より送付します。

モジュールの仕様書モジュールのブロック図モジュールの外形図実装されたアンテナデータシート ( 放射利得特性を含むもの )

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Monday, November 4, 2024 12:56 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介

Subject: [ 再送 : 今後の進め方のご案内 ] [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いホシデン野村様、堀様アリオンの酒井です。いつもお世話になっております。

( 先のメールで添付ファイルを失念したため再送します。 )

RF PHY 試験が Pass 完了しましたので早速ですが今後の進め方をご案内します。

(1)
添付の代行登録内容確認書にご記入の上、ご返送ください。ログイン情報は Invoice を取得された方と同一アカウントをご記入ください。

(2)
当方で認証登録に必要な作業を行い、 Review ページの内容を添付して確認依頼メールを送ります。

(3)
内容ご確認いただき登録指示メール受信後、登録確定操作を行います。 1-2 営業日以内に SIG の承認が完了して認証登録が有効になります。表示開始日指定登録ではその日から一般公開されます。

(4)
コンプライアンスフォルダ作成のために、 RF PHY レポートおよび登録過程で取得したドキュメントとともに以下の資料をご提出ください。

モジュールの仕様書モジュールのブロック図モジュールの外形図実装されたアンテナデータシート ( 放射利得特性を含むもの )

以上よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 11 月 1 日 19:12

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : Re: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

大変お待たせいたしました。

予定より早く RF 試験が完了いたしましたのでレポートをお送りいたします。

以下の Password にてダウンロードください。

[ パスワード ]

z2kzM&quot;*M

[ パスワード有効期限 ]

[ID] 19:10 まで

[ 送信 ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 11 月 1 日 16:14

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : Re: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントありがとうございます。

本日試験を日本で開始できました。

そのため、ご準備いただきましたが、今回台湾への発送は行う必要がなくなりました。

週明けまでには結果をお知らせできる予定です。

もうしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 31 日 18:32

宛先 : Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

機材提出票を添付致しますので、ご確認お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 5:02 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントご送付ありがとうございます。

確認いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Thursday, October 31, 2024 3:40 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

ご連絡ありがとうございます。日本での試験実施をお願い致します。

[ID]docと試験手順書を提出致しますので、ご確認お願い致します。

機材提出票は、別途提出致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 11:55 AM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡ありがとうございます。

先ほどサンプルが到着いたしました。

[ID]docのご提出をいただき、

テストプラン作成後試験開始となります。

出来るだけお早目のご提供お願いいたします。

こちらのサンプルですが、テストモードに入るための手順などはございますでしょうか。

ある場合はその手順もお知らせください。

また、後程で良いですので添付の機材提出票のファイルにご記入の上ご返送ください。

試験なのですが、キャンセルが発生したため、

今日、明日であれば日本で実施いたします。

もし遅くなるようでしたら台湾実施の検討となります。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Wednesday, October 30, 2024 5:03 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

試験サンプルを望月様宛てに、10/31午前着で発送致しました。

[ID]docについては、明日提出致します。

【便名】 ヤマト運輸

【送り状No.】 [ID]

【お届け予定日】 10/31 AM着指定

【その他】ヤマト運輸の箱での発送です。

【発送物】[ID]/Bluetooth SIG認証サンプル以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Tuesday, October 29, 2024 3:50 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

種々ご準備いただきありがとうございます。

試験サンプルと [ID]doc ですが、

明日もしくは３１日の当社日本側到着は可能でしょうか。

サンプルは以下の私のフッタの私宛てへのご発送となります。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 10 月 25 日 17:18

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

以下となります。

[ID] LABS, INC.

９F, No.3-1, Yuan Ku Street

[ID] [ID] PARK BLD.G

Taipei, [ID] CITY 11503

Add: 11503台北市南港區園區街3-1號9樓(南港軟體園區G棟)

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Friday, October 25, 2024 5:10 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

下記承知致しました。

サンプルの送付先(台湾ラボ)の名前と住所をご教授お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Friday, October 25, 2024 11:29 AM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン野村様堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

日本側でキャンセル等発生した場合は対応可能ですが、不確定ですので、

台湾でも実施できるよう進めてまいります。

台湾輸出に当たり、該否判定書など御社書式でご準備いただけますでしょうか。

また、添付の税関等で使用する製品の画像入りの仕様書のご記入と、お預かりサンプル一覧のご記入もお願い申し上げます。

また、製品の接続、操作説明（英文もしくは中文）もいただけますでしょうか。

大変お手数おかけいたしますが、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Nomura Yusuke /
野村裕介

Sent: Friday, October 25, 2024 8:13 AM

To: Toshitaka Mochizuki ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

台湾のラボでの試験でもOKです。

日程優先で進めてください。

⇒堀さん添付資料をしあげて提出お願いします。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Toshitaka Mochizuki

Sent: Thursday, October 24, 2024 6:53 PM

To: Hori Masaki / 堀雅 Γ 彊児 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認 Γ 恐孜見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

Bluetooth 試験の方ですが実際の試験につきましては

PM の望月よりご案内いたします。

試験日程なのですが、 10 月 29 日以降ですと、空いている日程が

11 月下旬となってしまうため、調整しておりますが、

例えば当社台湾でのご受験は可能でしょうか。

ご検討お願いいたします。

また、添付の [ID]doc にご記入の上、

ご返送いただけますでしょうか。

テストプランを作成いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 23 日 14:28

宛先 : Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

返信が遅くなり申し訳ありません。

サンプルの準備に時間を要しておりましたが、10/29頃にサンプルの発送を予定しております。

試験開始日は、サンプルが届き次第、なるべく早い日で実施をお願いしたく、

お手数をおかけしますが、日程調整をお願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Tuesday, October 1, 2024 4:24 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン堀様いつもお世話になっております。

アリオンの飯田です。

注文書のご提出ありがとうございます。

ご注文を承ります。
サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？

問題ございません。
サンプルは何台必要でしょうか？

1台で結構です。

サンプル準備については添付内容をご参照くださいませ。

ご希望の試験開始日はございますでしょうか。

サンプルはいつ頃提出可能な見込みでしょうか。

日程調整いたしますので、ご回答のほどよろしくお願いいたします。

また、サンプル提出先については以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社 KSTC 営業部 PM 望月宛以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Hori Masaki /
堀雅樹

Sent: Tuesday, October 1, 2024 2:49 PM

To: Masaya Iida ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

注文書を発行致しましたので、添付をご確認お願い致します。

また、提出するサンプルに関して、お手数をおかけしますが、以下の質問にご回答をお願い致します。

・サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？(セミリジットケーブル付き)

・サンプルは何台必要でしょうか？

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Thursday, September 26, 2024 1:46 PM

To: Nomura Yusuke / 野村裕介 ;
Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様いつもお世話になっております。

アリオンの飯田です。

お待たせをして申し訳ございません。

見積書を発行いたしました。

添付致します。ご検討のほどよろしくお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Nomura Yusuke /
野村裕介

Sent: Thursday, September 26, 2024 12:34 PM

To: Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

見積書はまだ掛かりそうでしょうか？

いつ提出できるのかを回答お願いします。

御社で使用されるBTテスタのメーカー名と品番を参考に教えて頂けないでしょうか？

弊社ではRohde & Schwarz製のものを使用しています。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 7:12 PM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

⇒ 承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・ RF PHY 試験（1M）

￥ 400,000

・代行登録サポート費 ( Single -Design 参照 )
￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上よろしくお願いいたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 19 日 18:57

宛先 : Itsuo Sakai ;
Hori Masaki / 堀雅樹

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine unmodified
Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine unmodified
Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。
結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID
の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

→上記の内容についてですが、これは下記のように「Combine unmodified Designs」を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。(添付参照)

ただ、DNが付与されない登録になり、DNは「Details」という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

「[ID]」をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Numberが！表記なのは登録費 (旧Declaration ID)を設定していないためです。

[質問事項]

・DN (Design Number)が「Default」表記になることのデメリット、問題点はないのか？

・Q30から始まるQDIDのみで再ブランド化した場合、Bluetooth認証上は問題ないのか？

単にDNがDefault表示になるだけ、QDIDが「Q30〜」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先にHRM5141として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードはBLE1Mのみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

---

## 8. 2024-11-05 02:43

**From:** Itsuo Sakai
**To:** =?utf-8?B?SG9yaSBNYXNha2kgLyDloIAg6ZuF5qi5?= , =?utf-8?B?Tm9tdXJhIFl1c3VrZSAvIOmHjuadkSDoo5Xku4s=?=

ホシデン堀様アリオンの酒井です。いつもお世話になっております。

製品資料をご提出あいがとうございます。

外形図ですが、モジュールとしての外形図あるいは実物にものさしを添えた写真をご提供いただけないでしょうか。他の資料は問題ございません。

RF PHYテストレポートの製品名(英文)をWristband activity trackerに変更した更新版は別途試験部門の望月より送付させていただきます。

以上よろしくお願いいたします。

差出人: Hori Masaki / 堀雅樹

送信日時: 2024年11月5日 11:05

宛先: Nomura Yusuke / 野村裕介 ; Itsuo Sakai

件名: RE: [再送:今後の進め方のご案内] [再送：ご提案] Re: [ID]/認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀です。

資料を提出致しますので、ご確認お願い致します。

仕様書と外形図は Bluetooth IC のデータシートをご確認お願い致します。

ブロック図は無線部を中心に記載しております。 Bluetooth IC のブロック図はデータシートから抜粋したものとなります。

また、先日頂いたテストレポートに関して、

お手数をおかけしますが、製品名 ( 英文 ) を Wristband activity tracker に変更お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Nomura Yusuke /
野村裕介

Sent: Tuesday, November 5, 2024 9:56 AM

To: Itsuo Sakai ; Hori Masaki / 堀雅樹

Subject: RE: [ 再送 : 今後の進め方のご案内 ]
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

[ID] の試験およびレポートの送付ありがとうございました。

代行登録内容確認書を添付の通り提出致します。

下記資料に関しては、別途堀より送付します。

①
モジュールの仕様書

②
モジュールのブロック図

③
モジュールの外形図

④
実装されたアンテナデータシート ( 放射利得特性を含むもの )

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Monday, November 4, 2024 12:56 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介

Subject: [ 再送 : 今後の進め方のご案内 ]
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様、堀様アリオンの酒井です。いつもお世話になっております。

( 先のメールで添付ファイルを失念したため再送します。 )

RF PHY 試験が Pass 完了しましたので早速ですが今後の進め方をご案内します。

(1)
添付の代行登録内容確認書にご記入の上、ご返送ください。ログイン情報は Invoice を取得された方と同一アカウントをご記入ください。

(2)
当方で認証登録に必要な作業を行い、 Review ページの内容を添付して確認依頼メールを送ります。

(3)
内容ご確認いただき登録指示メール受信後、登録確定操作を行います。 1-2 営業日以内に SIG の承認が完了して認証登録が有効になります。表示開始日指定登録ではその日から一般公開されます。

(4)
コンプライアンスフォルダ作成のために、 RF PHY レポートおよび登録過程で取得したドキュメントとともに以下の資料をご提出ください。

①
モジュールの仕様書

②
モジュールのブロック図

③
モジュールの外形図

④
実装されたアンテナデータシート ( 放射利得特性を含むもの )

以上よろしくお願いいたします。

差出人 :
Toshitaka Mochizuki

送信日時 :
2024 年 11 月 1 日
19:12

宛先 :
Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Masaya Iida

件名 :
Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

大変お待たせいたしました。

予定より早く RF 試験が完了いたしましたのでレポートをお送りいたします。

以下の Password にてダウンロードください。

[ パスワード ]

z2kzM&quot;*M

[ パスワード有効期限 ]

[ID] 19:10 まで

[ 送信 ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka
Mochizuki

送信日時 : 2024 年 11 月 1 日
16:14

宛先 : Hori
Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Masaya Iida

件名 : Re:
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントありがとうございます。

本日試験を日本で開始できました。

そのため、ご準備いただきましたが、今回台湾への発送は行う必要がなくなりました。

週明けまでには結果をお知らせできる予定です。

もうしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori
Masaki / 堀雅樹

送信日時 : 2024 年 10 月 31 日
18:32

宛先 : Toshitaka
Mochizuki ; Nomura Yusuke /
野村裕介 ; Masaya Iida

件名 : RE:
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

機材提出票を添付致しますので、ご確認お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 5:02 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントご送付ありがとうございます。

確認いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Thursday, October 31, 2024 3:40 PM

To: Toshitaka Mochizuki ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

ご連絡ありがとうございます。日本での試験実施をお願い致します。

[ID]doc と試験手順書を提出致しますので、ご確認お願い致します。

機材提出票は、別途提出致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 11:55 AM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡ありがとうございます。

先ほどサンプルが到着いたしました。

[ID]doc のご提出をいただき、

テストプラン作成後試験開始となります。

出来るだけお早目のご提供お願いいたします。

こちらのサンプルですが、テストモードに入るための手順などはございますでしょうか。

ある場合はその手順もお知らせください。

また、後程で良いですので添付の機材提出票のファイルにご記入の上ご返送ください。

試験なのですが、キャンセルが発生したため、

今日、明日であれば日本で実施いたします。

もし遅くなるようでしたら台湾実施の検討となります。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Wednesday, October 30, 2024 5:03 PM

To: Toshitaka Mochizuki ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

試験サンプルを望月様宛てに、 10/31 午前着で発送致しました。

[ID]doc については、明日提出致します。

【便名】 ヤマト運輸

【送り状 No.】 [ID]

【お届け予定日】 10/31 AM 着指定

【その他】ヤマト運輸の箱での発送です。

【発送物】 [ID]/Bluetooth SIG 認証サンプル以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Tuesday, October 29, 2024 3:50 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

種々ご準備いただきありがとうございます。

試験サンプルと [ID]doc ですが、

明日もしくは３１日の当社日本側到着は可能でしょうか。

サンプルは以下の私のフッタの私宛てへのご発送となります。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka
Mochizuki

送信日時 : 2024 年 10 月 25 日 17:18

宛先 : Hori
Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE:
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

以下となります。

[ID] LABS, INC.

９ F, No.3-1, Yuan Ku Street

[ID] [ID] PARK BLD.G

Taipei, [ID] CITY 11503

Add: 11503 台北市南港區園區街 3-1 號 9 樓 ( 南港軟體園區 G 棟 )

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Friday, October 25, 2024 5:10 PM

To: Toshitaka Mochizuki ; Nomura Yusuke /
野村裕介 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

下記承知致しました。

サンプルの送付先 ( 台湾ラボ ) の名前と住所をご教授お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Friday, October 25, 2024 11:29 AM

To: Nomura Yusuke / 野村裕介 ; Hori Masaki /
堀雅樹 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン野村様堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

日本側でキャンセル等発生した場合は対応可能ですが、不確定ですので、

台湾でも実施できるよう進めてまいります。

台湾輸出に当たり、該否判定書など御社書式でご準備いただけますでしょうか。

また、添付の税関等で使用する製品の画像入りの仕様書のご記入と、お預かりサンプル一覧のご記入もお願い申し上げます。

また、製品の接続、操作説明（英文もしくは中文）もいただけますでしょうか。

大変お手数おかけいたしますが、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Nomura Yusuke /
野村裕介

Sent: Friday, October 25, 2024 8:13 AM

To: Toshitaka Mochizuki ; Hori Masaki /
堀雅樹 ; Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン㈱ 望月様いつもお世話になっております。

台湾のラボでの試験でも OK です。

日程優先で進めてください。

⇒堀さん添付資料をしあげて提出お願いします。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Toshitaka Mochizuki

Sent: Thursday, October 24, 2024 6:53 PM

To: Hori Masaki / 堀雅 Γ 彊児 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認 Γ 恐孜見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

Bluetooth 試験の方ですが実際の試験につきましては

PM の望月よりご案内いたします。

試験日程なのですが、 10 月 29 日以降ですと、空いている日程が

11 月下旬となってしまうため、調整しておりますが、

例えば当社台湾でのご受験は可能でしょうか。

ご検討お願いいたします。

また、添付の [ID]doc にご記入の上、

ご返送いただけますでしょうか。

テストプランを作成いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori
Masaki / 堀雅樹

送信日時 : 2024 年 10 月 23 日 14:28

宛先 : Masaya
Iida

件名 : RE:
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

返信が遅くなり申し訳ありません。

サンプルの準備に時間を要しておりましたが、 10/29 頃にサンプルの発送を予定しております。

試験開始日は、サンプルが届き次第、なるべく早い日で実施をお願いしたく、

お手数をおかけしますが、日程調整をお願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Tuesday, October 1, 2024 4:24 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介 ; Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン堀様いつもお世話になっております。

アリオンの飯田です。

注文書のご提出ありがとうございます。

ご注文を承ります。
サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？

問題ございません。
サンプルは何台必要でしょうか？

1 台で結構です。

サンプル準備については添付内容をご参照くださいませ。

ご希望の試験開始日はございますでしょうか。

サンプルはいつ頃提出可能な見込みでしょうか。

日程調整いたしますので、ご回答のほどよろしくお願いいたします。

また、サンプル提出先については以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社 KSTC 営業部 PM 望月宛以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From: Hori Masaki /
堀雅樹

Sent: Tuesday, October 1, 2024 2:49 PM

To: Masaya Iida ; Nomura Yusuke /
野村裕介 ; Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

注文書を発行致しましたので、添付をご確認お願い致します。

また、提出するサンプルに関して、お手数をおかけしますが、以下の質問にご回答をお願い致します。

・サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？ ( セミリジットケーブル付き )

・サンプルは何台必要でしょうか？

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Thursday, September 26, 2024 1:46 PM

To: Nomura Yusuke / 野村裕介 ; Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様いつもお世話になっております。

アリオンの飯田です。

お待たせをして申し訳ございません。

見積書を発行いたしました。

添付致します。ご検討のほどよろしくお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒 [ID]

東京都品川区大井一丁目 28 番 1 号住友不動産大井町駅前ビル 4 階

FAX [ID]

From: Nomura Yusuke /
野村裕介

Sent: Thursday, September 26, 2024 12:34 PM

To: Itsuo Sakai ; Hori Masaki /
堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

見積書はまだ掛かりそうでしょうか？

いつ提出できるのかを回答お願いします。

御社で使用される BT テスタのメーカー名と品番を参考に教えて頂けないでしょうか？

弊社では Rohde & Schwarz 製のものを使用しています。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 7:12 PM

To: Nomura Yusuke / 野村裕介 ; Hori Masaki /
堀雅樹

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

⇒ 承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・ RF PHY 試験（1M）

￥ 400,000

・代行登録サポート費 ( Single
-Design 参照 ) ￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上よろしくお願いいたします。

差出人 : Nomura
Yusuke / 野村裕介

送信日時 : 2024 年 9 月 19 日 18:57

宛先 : Itsuo
Sakai ;
Hori Masaki / 堀雅樹

件名 : RE:
[ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀 c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID]
(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine
unmodified Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura
Yusuke / 野村裕介

件名 : Re:
[ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine
unmodified Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura
Yusuke / 野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo
Sakai

件名 : RE:
[ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

結論は今回の [ID] (QDID： [ID]) と [ID] (QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→上記の内容についてですが、これは下記のように「Combine unmodified Designs」を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )

ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo
Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura
Yusuke / 野村裕介

件名 : Re:
[ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura
Yusuke / 野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo
Sakai

件名 : RE:
[ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG 登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

「[ID]」をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Number が！表記なのは登録費 ( 旧 Declaration ID) を設定していないためです。

[ 質問事項 ]

・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

単に DN が Default 表示になるだけ、 QDID が「Q30 ～」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura
Yusuke / 野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo
Sakai

件名 : RE:
[ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードは BLE1M のみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura
Yusuke / 野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo
Sakai

件名 : RE:
[ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

( 堀さんが休みのため、代わってメールします )

添付の見積依頼書を記入しました。

なお、 Profiles for Test に関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori
Masaki / 堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo
Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee ™W22 ｜生体センサ｜TDK プロダクトセンター
| 製品情報 | TDK プロダクトセンター対象規格：

Blueooth SIG 認証無線モード：

BLE1M モードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori
Masaki / 堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo
Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee ™W22 ｜生体センサ｜TDK プロダクトセンター
| 製品情報 | TDK プロダクトセンター対象規格：

Blueooth SIG 認証無線モード：

BLE1M モードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

---

## 9. 2024-11-05 06:54

**From:** Itsuo Sakai
**To:** =?iso-2022-jp?B?Tm9tdXJhIFl1c3VrZSAvIBskQkxuQjwbKEIgGyRCTTUycBsoQg==?= , =?iso-2022-jp?B?SG9yaSBNYXNha2kgLyAbJEJLWRsoQiAbJEIybTx5GyhC?=
**Attachments:** Review_Page.png

ホシデン野村様アリオンの酒井です。いつもお世話になっております。

代行登録内容確認書をご送付いただきありがとうございます。

QDID：125464をIncludeした具体的な登録手順とICSの階層間整合性については予め私の仮Projectで確認済でしたので、スムースに登録確定直前のレビューページまで進めることができました。

添付のレビューページの内容を念のため御社でもご確認ください。問題なければ登録確定のご指示をお願いします。

以上よろしくお願いいたします。

差出人: Nomura Yusuke / 野村裕介

送信日時: 2024年11月5日 9:55

宛先: Itsuo Sakai ; Hori Masaki / 堀雅樹

件名: RE: [再送:今後の進め方のご案内] [再送：ご提案] Re: [ID]/認証見積のお願いアリオン酒井様いつもお世話になっております。

RF-PHYの試験およびレポートの送付ありがとうございました。

代行登録内容確認書を添付の通り提出致します。

下記資料に関しては、別途堀より送付します。

モジュールの仕様書モジュールのブロック図モジュールの外形図実装されたアンテナデータシート ( 放射利得特性を含むもの )

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Monday, November 4, 2024 12:56 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介

Subject: [ 再送 : 今後の進め方のご案内 ] [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いホシデン野村様、堀様アリオンの酒井です。いつもお世話になっております。

( 先のメールで添付ファイルを失念したため再送します。 )

RF PHY 試験が Pass 完了しましたので早速ですが今後の進め方をご案内します。

(1)
添付の代行登録内容確認書にご記入の上、ご返送ください。ログイン情報は Invoice を取得された方と同一アカウントをご記入ください。

(2)
当方で認証登録に必要な作業を行い、 Review ページの内容を添付して確認依頼メールを送ります。

(3)
内容ご確認いただき登録指示メール受信後、登録確定操作を行います。 1-2 営業日以内に SIG の承認が完了して認証登録が有効になります。表示開始日指定登録ではその日から一般公開されます。

(4)
コンプライアンスフォルダ作成のために、 RF PHY レポートおよび登録過程で取得したドキュメントとともに以下の資料をご提出ください。

モジュールの仕様書モジュールのブロック図モジュールの外形図実装されたアンテナデータシート ( 放射利得特性を含むもの )

以上よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 11 月 1 日 19:12

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : Re: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

大変お待たせいたしました。

予定より早く RF 試験が完了いたしましたのでレポートをお送りいたします。

以下の Password にてダウンロードください。

[ パスワード ]

z2kzM&quot;*M

[ パスワード有効期限 ]

[ID] 19:10 まで

[ 送信 ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 11 月 1 日 16:14

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : Re: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントありがとうございます。

本日試験を日本で開始できました。

そのため、ご準備いただきましたが、今回台湾への発送は行う必要がなくなりました。

週明けまでには結果をお知らせできる予定です。

もうしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 31 日 18:32

宛先 : Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

機材提出票を添付致しますので、ご確認お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 5:02 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントご送付ありがとうございます。

確認いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Thursday, October 31, 2024 3:40 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

ご連絡ありがとうございます。日本での試験実施をお願い致します。

[ID]docと試験手順書を提出致しますので、ご確認お願い致します。

機材提出票は、別途提出致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 11:55 AM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡ありがとうございます。

先ほどサンプルが到着いたしました。

[ID]docのご提出をいただき、

テストプラン作成後試験開始となります。

出来るだけお早目のご提供お願いいたします。

こちらのサンプルですが、テストモードに入るための手順などはございますでしょうか。

ある場合はその手順もお知らせください。

また、後程で良いですので添付の機材提出票のファイルにご記入の上ご返送ください。

試験なのですが、キャンセルが発生したため、

今日、明日であれば日本で実施いたします。

もし遅くなるようでしたら台湾実施の検討となります。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Wednesday, October 30, 2024 5:03 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

試験サンプルを望月様宛てに、10/31午前着で発送致しました。

[ID]docについては、明日提出致します。

【便名】 ヤマト運輸

【送り状No.】 [ID]

【お届け予定日】 10/31 AM着指定

【その他】ヤマト運輸の箱での発送です。

【発送物】[ID]/Bluetooth SIG認証サンプル以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Tuesday, October 29, 2024 3:50 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

種々ご準備いただきありがとうございます。

試験サンプルと [ID]doc ですが、

明日もしくは３１日の当社日本側到着は可能でしょうか。

サンプルは以下の私のフッタの私宛てへのご発送となります。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 10 月 25 日 17:18

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

以下となります。

[ID] LABS, INC.

９F, No.3-1, Yuan Ku Street

[ID] [ID] PARK BLD.G

Taipei, [ID] CITY 11503

Add: 11503台北市南港區園區街3-1號9樓(南港軟體園區G棟)

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Friday, October 25, 2024 5:10 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

下記承知致しました。

サンプルの送付先(台湾ラボ)の名前と住所をご教授お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Friday, October 25, 2024 11:29 AM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン野村様堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

日本側でキャンセル等発生した場合は対応可能ですが、不確定ですので、

台湾でも実施できるよう進めてまいります。

台湾輸出に当たり、該否判定書など御社書式でご準備いただけますでしょうか。

また、添付の税関等で使用する製品の画像入りの仕様書のご記入と、お預かりサンプル一覧のご記入もお願い申し上げます。

また、製品の接続、操作説明（英文もしくは中文）もいただけますでしょうか。

大変お手数おかけいたしますが、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Nomura Yusuke /
野村裕介

Sent: Friday, October 25, 2024 8:13 AM

To: Toshitaka Mochizuki ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

台湾のラボでの試験でもOKです。

日程優先で進めてください。

⇒堀さん添付資料をしあげて提出お願いします。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Toshitaka Mochizuki

Sent: Thursday, October 24, 2024 6:53 PM

To: Hori Masaki / 堀雅 Γ 彊児 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認 Γ 恐孜見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

Bluetooth 試験の方ですが実際の試験につきましては

PM の望月よりご案内いたします。

試験日程なのですが、 10 月 29 日以降ですと、空いている日程が

11 月下旬となってしまうため、調整しておりますが、

例えば当社台湾でのご受験は可能でしょうか。

ご検討お願いいたします。

また、添付の [ID]doc にご記入の上、

ご返送いただけますでしょうか。

テストプランを作成いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 23 日 14:28

宛先 : Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

返信が遅くなり申し訳ありません。

サンプルの準備に時間を要しておりましたが、10/29頃にサンプルの発送を予定しております。

試験開始日は、サンプルが届き次第、なるべく早い日で実施をお願いしたく、

お手数をおかけしますが、日程調整をお願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Tuesday, October 1, 2024 4:24 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン堀様いつもお世話になっております。

アリオンの飯田です。

注文書のご提出ありがとうございます。

ご注文を承ります。
サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？

問題ございません。
サンプルは何台必要でしょうか？

1台で結構です。

サンプル準備については添付内容をご参照くださいませ。

ご希望の試験開始日はございますでしょうか。

サンプルはいつ頃提出可能な見込みでしょうか。

日程調整いたしますので、ご回答のほどよろしくお願いいたします。

また、サンプル提出先については以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社 KSTC 営業部 PM 望月宛以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Hori Masaki /
堀雅樹

Sent: Tuesday, October 1, 2024 2:49 PM

To: Masaya Iida ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

注文書を発行致しましたので、添付をご確認お願い致します。

また、提出するサンプルに関して、お手数をおかけしますが、以下の質問にご回答をお願い致します。

・サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？(セミリジットケーブル付き)

・サンプルは何台必要でしょうか？

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Thursday, September 26, 2024 1:46 PM

To: Nomura Yusuke / 野村裕介 ;
Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様いつもお世話になっております。

アリオンの飯田です。

お待たせをして申し訳ございません。

見積書を発行いたしました。

添付致します。ご検討のほどよろしくお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Nomura Yusuke /
野村裕介

Sent: Thursday, September 26, 2024 12:34 PM

To: Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

見積書はまだ掛かりそうでしょうか？

いつ提出できるのかを回答お願いします。

御社で使用されるBTテスタのメーカー名と品番を参考に教えて頂けないでしょうか？

弊社ではRohde & Schwarz製のものを使用しています。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 7:12 PM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

⇒ 承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・ RF PHY 試験（1M）

￥ 400,000

・代行登録サポート費 ( Single -Design 参照 )
￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上よろしくお願いいたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 19 日 18:57

宛先 : Itsuo Sakai ;
Hori Masaki / 堀雅樹

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine unmodified
Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine unmodified
Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。
結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID
の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

→上記の内容についてですが、これは下記のように「Combine unmodified Designs」を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。(添付参照)

ただ、DNが付与されない登録になり、DNは「Details」という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

「[ID]」をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Numberが！表記なのは登録費 (旧Declaration ID)を設定していないためです。

[質問事項]

・DN (Design Number)が「Default」表記になることのデメリット、問題点はないのか？

・Q30から始まるQDIDのみで再ブランド化した場合、Bluetooth認証上は問題ないのか？

単にDNがDefault表示になるだけ、QDIDが「Q30〜」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先にHRM5141として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードはBLE1Mのみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人: Nomura Yusuke / 野村裕介

送信日時: 2024年11月5日 9:55

宛先: Itsuo Sakai ; Hori Masaki / 堀雅樹

件名: RE: [再送:今後の進め方のご案内] [再送：ご提案] Re: [ID]/認証見積のお願いアリオン酒井様いつもお世話になっております。

RF-PHYの試験およびレポートの送付ありがとうございました。

代行登録内容確認書を添付の通り提出致します。

下記資料に関しては、別途堀より送付します。

モジュールの仕様書モジュールのブロック図モジュールの外形図実装されたアンテナデータシート ( 放射利得特性を含むもの )

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Monday, November 4, 2024 12:56 PM

To: Hori Masaki / 堀雅樹 ; Nomura Yusuke /
野村裕介

Subject: [ 再送 : 今後の進め方のご案内 ] [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いホシデン野村様、堀様アリオンの酒井です。いつもお世話になっております。

( 先のメールで添付ファイルを失念したため再送します。 )

RF PHY 試験が Pass 完了しましたので早速ですが今後の進め方をご案内します。

(1)
添付の代行登録内容確認書にご記入の上、ご返送ください。ログイン情報は Invoice を取得された方と同一アカウントをご記入ください。

(2)
当方で認証登録に必要な作業を行い、 Review ページの内容を添付して確認依頼メールを送ります。

(3)
内容ご確認いただき登録指示メール受信後、登録確定操作を行います。 1-2 営業日以内に SIG の承認が完了して認証登録が有効になります。表示開始日指定登録ではその日から一般公開されます。

(4)
コンプライアンスフォルダ作成のために、 RF PHY レポートおよび登録過程で取得したドキュメントとともに以下の資料をご提出ください。

モジュールの仕様書モジュールのブロック図モジュールの外形図実装されたアンテナデータシート ( 放射利得特性を含むもの )

以上よろしくお願いいたします。

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 11 月 1 日 19:12

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : Re: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

大変お待たせいたしました。

予定より早く RF 試験が完了いたしましたのでレポートをお送りいたします。

以下の Password にてダウンロードください。

[ パスワード ]

z2kzM&quot;*M

[ パスワード有効期限 ]

[ID] 19:10 まで

[ 送信 ID]

ご確認どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 11 月 1 日 16:14

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : Re: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントありがとうございます。

本日試験を日本で開始できました。

そのため、ご準備いただきましたが、今回台湾への発送は行う必要がなくなりました。

週明けまでには結果をお知らせできる予定です。

もうしばらくお待ちください。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 31 日 18:32

宛先 : Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

機材提出票を添付致しますので、ご確認お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 5:02 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ドキュメントご送付ありがとうございます。

確認いたします。

引き続きどうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Thursday, October 31, 2024 3:40 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

ご連絡ありがとうございます。日本での試験実施をお願い致します。

[ID]docと試験手順書を提出致しますので、ご確認お願い致します。

機材提出票は、別途提出致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Thursday, October 31, 2024 11:55 AM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご連絡ありがとうございます。

先ほどサンプルが到着いたしました。

[ID]docのご提出をいただき、

テストプラン作成後試験開始となります。

出来るだけお早目のご提供お願いいたします。

こちらのサンプルですが、テストモードに入るための手順などはございますでしょうか。

ある場合はその手順もお知らせください。

また、後程で良いですので添付の機材提出票のファイルにご記入の上ご返送ください。

試験なのですが、キャンセルが発生したため、

今日、明日であれば日本で実施いたします。

もし遅くなるようでしたら台湾実施の検討となります。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Wednesday, October 30, 2024 5:03 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

試験サンプルを望月様宛てに、10/31午前着で発送致しました。

[ID]docについては、明日提出致します。

【便名】 ヤマト運輸

【送り状No.】 [ID]

【お届け予定日】 10/31 AM着指定

【その他】ヤマト運輸の箱での発送です。

【発送物】[ID]/Bluetooth SIG認証サンプル以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Tuesday, October 29, 2024 3:50 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

種々ご準備いただきありがとうございます。

試験サンプルと [ID]doc ですが、

明日もしくは３１日の当社日本側到着は可能でしょうか。

サンプルは以下の私のフッタの私宛てへのご発送となります。

どうぞよろしくお願いいたします。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Toshitaka Mochizuki

送信日時 : 2024 年 10 月 25 日 17:18

宛先 : Hori Masaki /
堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

以下となります。

[ID] LABS, INC.

９F, No.3-1, Yuan Ku Street

[ID] [ID] PARK BLD.G

Taipei, [ID] CITY 11503

Add: 11503台北市南港區園區街3-1號9樓(南港軟體園區G棟)

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Hori Masaki /
堀雅樹

Sent: Friday, October 25, 2024 5:10 PM

To: Toshitaka Mochizuki ;
Nomura Yusuke / 野村裕介 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

ホシデンの堀です。

下記承知致しました。

サンプルの送付先(台湾ラボ)の名前と住所をご教授お願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Toshitaka Mochizuki

Sent: Friday, October 25, 2024 11:29 AM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願い

[confidential]

ホシデン野村様堀様いつもお世話になっております。

アリオン株式会社の望月です。

ご回答ありがとうございます。

日本側でキャンセル等発生した場合は対応可能ですが、不確定ですので、

台湾でも実施できるよう進めてまいります。

台湾輸出に当たり、該否判定書など御社書式でご準備いただけますでしょうか。

また、添付の税関等で使用する製品の画像入りの仕様書のご記入と、お預かりサンプル一覧のご記入もお願い申し上げます。

また、製品の接続、操作説明（英文もしくは中文）もいただけますでしょうか。

大変お手数おかけいたしますが、どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

From: Nomura Yusuke /
野村裕介

Sent: Friday, October 25, 2024 8:13 AM

To: Toshitaka Mochizuki ;
Hori Masaki / 堀雅樹 ;
Masaya Iida

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン望月様いつもお世話になっております。

台湾のラボでの試験でもOKです。

日程優先で進めてください。

⇒堀さん添付資料をしあげて提出お願いします。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Toshitaka Mochizuki

Sent: Thursday, October 24, 2024 6:53 PM

To: Hori Masaki / 堀雅 Γ 彊児 ;
Masaya Iida

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認 Γ 恐孜見積のお願い

[confidential]

ホシデン堀様いつもお世話になっております。

アリオン株式会社の望月です。

Bluetooth 試験の方ですが実際の試験につきましては

PM の望月よりご案内いたします。

試験日程なのですが、 10 月 29 日以降ですと、空いている日程が

11 月下旬となってしまうため、調整しておりますが、

例えば当社台湾でのご受験は可能でしょうか。

ご検討お願いいたします。

また、添付の [ID]doc にご記入の上、

ご返送いただけますでしょうか。

テストプランを作成いたします。

どうぞよろしくお願い申し上げます。

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

アリオン株式会社 KSTC 営業部 PM 望月俊孝所在地：〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階

ωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωωω

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 10 月 23 日 14:28

宛先 : Masaya Iida

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

返信が遅くなり申し訳ありません。

サンプルの準備に時間を要しておりましたが、10/29頃にサンプルの発送を予定しております。

試験開始日は、サンプルが届き次第、なるべく早い日で実施をお願いしたく、

お手数をおかけしますが、日程調整をお願い致します。

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Tuesday, October 1, 2024 4:24 PM

To: Hori Masaki / 堀雅樹 ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン堀様いつもお世話になっております。

アリオンの飯田です。

注文書のご提出ありがとうございます。

ご注文を承ります。
サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？

問題ございません。
サンプルは何台必要でしょうか？

1台で結構です。

サンプル準備については添付内容をご参照くださいませ。

ご希望の試験開始日はございますでしょうか。

サンプルはいつ頃提出可能な見込みでしょうか。

日程調整いたしますので、ご回答のほどよろしくお願いいたします。

また、サンプル提出先については以下までお願いいたします。

〒 [ID] 東京都品川区勝島 1-1-1
東京 SRC B 館 4 階アリオン株式会社 KSTC 営業部 PM 望月宛以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Hori Masaki /
堀雅樹

Sent: Tuesday, October 1, 2024 2:49 PM

To: Masaya Iida ;
Nomura Yusuke / 野村裕介 ;
Itsuo Sakai

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン飯田様いつもお世話になっております。

ホシデンの堀です。

注文書を発行致しましたので、添付をご確認お願い致します。

また、提出するサンプルに関して、お手数をおかけしますが、以下の質問にご回答をお願い致します。

・サンプルの状態は、ケース無し・基板剥き出し状態で問題ないでしょうか？(セミリジットケーブル付き)

・サンプルは何台必要でしょうか？

以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係

From: Masaya Iida

Sent: Thursday, September 26, 2024 1:46 PM

To: Nomura Yusuke / 野村裕介 ;
Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様いつもお世話になっております。

アリオンの飯田です。

お待たせをして申し訳ございません。

見積書を発行いたしました。

添付致します。ご検討のほどよろしくお願いいたします。

以上、よろしくお願いいたします。

アリオン株式会社営業統括部営業担当飯田雅也

〒[ID]

東京都品川区大井一丁目28番1号住友不動産大井町駅前ビル4階

FAX [ID]

From: Nomura Yusuke /
野村裕介

Sent: Thursday, September 26, 2024 12:34 PM

To: Itsuo Sakai ;
Hori Masaki / 堀雅樹

Subject: RE: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

見積書はまだ掛かりそうでしょうか？

いつ提出できるのかを回答お願いします。

御社で使用されるBTテスタのメーカー名と品番を参考に教えて頂けないでしょうか？

弊社ではRohde & Schwarz製のものを使用しています。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 19, 2024 7:12 PM

To: Nomura Yusuke / 野村裕介 ;
Hori Masaki / 堀雅樹

Subject: Re: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
対策案の提示、ありがとうございます。
下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

⇒ ご対応ありがとうございます。
ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

⇒ 承知しました。営業の飯田より下記内容の正式見積書を野村様あてに発行させていただきます。

・ RF PHY 試験（1M）

￥ 400,000

・代行登録サポート費 ( Single -Design 参照 )
￥ 150,000

・コンプライアンスフォルダ作成費 ￥ 150,000

以上よろしくお願いいたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 19 日 18:57

宛先 : Itsuo Sakai ;
Hori Masaki / 堀雅樹

件名 : RE: [ 再送：ご提案 ]
Re: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

対策案の提示、ありがとうございます。

下記対策案をユーザーへ提示し、これで進める最終確認を取っている状況です。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

ユーザー承認後に手配しますので、正式な ” 見積書 ” を書面で送付お願いします。

・ RF PHY 試験（1M）
￥ 400,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

⇒堀c

注文書を準備願います。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Saturday, September 14, 2024 2:07 PM

To: Nomura Yusuke / 野村裕介

Subject: [ 再送：ご提案 ] Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

赤字文言に訂正して再送します。

9/5 の返信メールのとおり、 [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、

組み合わせ QDID の階層間不整合チェックのために御社モジュール登録の過程で Contensystency
Check

結果を Invalid=0 とんなよう ICS を修正すると GAP 階層の試験要求が発生し、プロトコル階層の試験は中間階層のために SW 開発環境でデバッガーを GAP の上位 ([ID] 階層）に組み込んで試験を行い、 Fail

が発生したらソースコードを解析・修正してコンパイラで実行ファイル化して再試験という工程を行う必要があります。これまでの経験ではプロトコル階層の認証試験はスタックベンダでないと困難です。

一方「[ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能」ですが、

モジュールとしての DN が付与されないため、当該モジュールを実装したセットの登録では結局 [ID]

(QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせ登録を行うことになるために「DN を取得できないモジュールの登録の必要性」が疑わしくなります。可能ならば Host と controller 間の階層間不整合が発生しない Host Stack への変更をご検討ください。 [ID]
(QDID： [ID]) は下図のように Listing

企業が退会していますので ARM Ltd への GAP 機能を削減した更新登録依頼は困難かと思います。

そこで提案ですが上記の「Host と controller 間の階層間不整合が発生しない Host
Stack への変更」は現実的には困難かと思いますので下記代替策を提案します。

今回の [ID] (QDID： [ID]) は SoC ですのでそれを実装したモジュールや製品基板での RF
PHY 試験が必須です。 ( 本来 [ID] は Component 登録されるべきものです。）御社モジュールを [ID]
(QDID：

[ID]) だけを Include すれば Consystency
Check で Invlid=0 で、 RF
PHY 試験レポートをアップロードすることで DN を取得した Core
Controller( 旧 controller Subsystem) 登録が可能です。そしてセットメーカーはそのモジュール登録の DN と Host
Controller 登録の [ID] (QDID： [ID]) を Include した登録で「このデザインを変更せずに使用」で先に進めば階層間不整合問題は回避した Core Complete の製品登録が可能です。

この代替案でモジュールとして実施する RF PHY を SIG 登録サイトにアップロードでき、このモジュール登録で DN が取得できて「モジュールとしてデザイン登録済」をアッピールできるメリットがあります。

( 見積額は以前と同額です。 )

以上、この代替案をご検討ください。

をしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能で
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine unmodified
Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 13 日 19:47

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 上記の内容についてですが、これは下記のように「Combine unmodified
Designs」を選択して申請をあげることを指していますか？

⇒ そのご理解通りです。
この場合だとレポート登録も不要になり、登録できることが確認できました。 ( 添付参照 )
ただ、 DN が付与されない登録になり、 DN は「Details」という表示になるのでしょうか？

⇒ はい、 DID/DN 欄に Details と表示される登録になります。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 13 日 18:45

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。
結論は今回のD065101 (QDID：[ID])とD043119 (QDID：[ID])の組み合わせでは、組み合わせQDID
の階層間不整合チェックをしない旧Declaration登録相当の登録(DNは付与されない)でしたら可能です。

→上記の内容についてですが、これは下記のように「Combine unmodified Designs」を選択して申請をあげることを指していますか？

この場合だとレポート登録も不要になり、登録できることが確認できました。(添付参照)

ただ、DNが付与されない登録になり、DNは「Details」という表示になるのでしょうか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 1:19 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

先程のメールの文中画像が Details の例ではなかったので、訂正再送します。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Itsuo Sakai

送信日時 : 2024 年 9 月 12 日 13:01

宛先 : Nomura Yusuke /
野村裕介

件名 : Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
「[ID]」をそのままデザイン流用して製品登録を試してみたところ、
登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。
Receipt Number が！表記なのは登録費 ( 旧 Declaration
ID) を設定していないためです。

[ 質問事項 ]
・ DN (Design Number) が「Default」表記になることのデメリット、問題点はないのか？

⇒ 新登録サイトがスタートした 7/1 から暫くは、旧 Declaration 登録に相当する Include した既存

QDID/DN を編集しない登録には一律 DN 欄に Details、その隣の欄に Include した QDID/DN だけが表示されていました。最近だと思いますが、 Include した QDID/DN が 1 件の場合はそのままで、

2 件以上の場合には当該 QDID/DN を組み合わせた全体の ICS に対して Q30 から始まる DN が付与され、 Include した QDID/DN とともに表示されるようになりました。

この奇妙な DN の扱いは新登録サイトのルールですのでどうにもなりませんので御社顧客に DN

があり、顧客の製品登録ではそれを Include することで試験免除での登録が可能と説明してください。

なお、現在でも QDID/DN が 1 件の場合は DN は付与されず、御社登録の DN を Include した顧客登録も下記表示になります。
・ Q30 から始まる QDID のみで再ブランド化した場合、 Bluetooth 認証上は問題ないのか？

⇒ Q30 は QPRDv3.0 の意味で、 7/1 以降付与された DN が全てその番号から始まります、旧登録の QDID

とまったく同じ効力ですので問題ありません。
単に DN が Default 表示になるだけ、 QDID が「Q30 〜」になるだけであり、
特にデメリットや問題点が無ければ、ホシデンで先に [ID] として製品登録は進められます。

⇒ そのご理解通り「DN が Default 表示になるだけ、 QDID に替わる DN が付与される」で間違いありません。補足ですが、たまたま Controller Subsystem と Host
Subsystem を Include したために新登録サイトでも DN が付与されたもので、もし SoC が End
Product だったら、 DN は付与されません。御社のようにセットメーカーへモジュールを販売する場合には、顧客の製品登録のために DN が付与される登録が可能な SoC ＋ Host
Stack の選択を今後もお勧めします。

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 12:36

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

SIG登録の件ですが、社内で詳しい梅田に相談しました。

下記のように情報入手できたので、ご確認頂けないでしょうか。

「[ID]」をそのままデザイン流用して製品登録を試してみたところ、

登録一歩手前までは進められたので従来の再ブランド化と同じやり方で対応できそうです。

Receipt Numberが！表記なのは登録費 (旧Declaration ID)を設定していないためです。

[質問事項]

・DN (Design Number)が「Default」表記になることのデメリット、問題点はないのか？

・Q30から始まるQDIDのみで再ブランド化した場合、Bluetooth認証上は問題ないのか？

単にDNがDefault表示になるだけ、QDIDが「Q30〜」になるだけであり、

特にデメリットや問題点が無ければ、ホシデンで先にHRM5141として製品登録は進められます。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 12, 2024 10:07 AM

To: Nomura Yusuke /
野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。
弊社でも実施してみて同様の内容を確認しました。
今後の方針はユーザーと相談した上で決めたいと思います。

⇒ 承知しました。
>
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
>
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。
→ 取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？
データベースにどう表示されるのか、ご教示お願いします。

⇒ 同じ条件で登録された実例は下記のように検索結果の DN 欄に「Details」と表示される ( 見かけ上は DN が付与されない ) ものの、この組み合わせにでも実は Design
Number(DN) が 2 番目の欄に ( この例では [ID])

が表示されます。そして他社の製品登録でこの 2 番目の欄の Q30 から始まる DN を Include することが可能です。

詳細ページの表示内容は下記 URL( ＝上図の Details アイコンが示す URL) を参照してください。

>
・ RF PHY 試験（1M,
2M）
￥ 700,000
→ 無線モードは BLE1M のみですので、減額できますか？

⇒ 階層間不整合チェックをしない旧 Declaration 登録相当の登録では、 Include した既存登録の ICS を踏襲しますので御社名義の登録で [RF PHY] (1/4) 2M PHY :NO と変更した登録ができません。

しかし [ID] (QDID： [ID]) は SoC であるため、モジュールまたは製品基板に実装した状態での

RF PHY 試験が必須です。このような SoC は本来 Component 登録するべきですが、 Controller
Subsystem

登録されてされているため新登録サイトでもアップロードは要求されず、 RF PHY 試験は確認レポートの扱いになります。

このため、今回のモジュールが 1M PHY の仕様でしたら RF
PHY 試験も 1M PHY のみとすることが可能です。

・ RF PHY 試験（1M）
￥ 400,000

以上回答いたします。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 12 日 8:52

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ご指摘ありがとうございます。

弊社でも実施してみて同様の内容を確認しました。

今後の方針はユーザーと相談した上で決めたいと思います。
結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID
の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

→取得は可能とのことですが、この場合どのような登録結果になるのでしょうか？

データベースにどう表示されるのか、ご教示お願いします。
・ RF PHY 試験（1M,
2M）
￥ 700,000

→無線モードはBLE1Mのみですので、減額できますか？

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Thursday, September 5, 2024 7:33 PM

To: Nomura Yusuke / 野村裕介

Subject: Re: [ID]/ 認証見積のお願いホシデン野村様アリオンの酒井です。いつもお世話になっております。

見積ご依頼ありがとうございます。

ご存知のように 7/1 に新登録サイトに更新されました。新登録サイトでは従来 Controller
Subsystem と

Host Subsystem の組み合わせ登録では一律チェックが除外されていた Declaration 登録相当の登録でデザイン番号 (DN) が付与されない登録と、階層間不整合チェックを行ってデザイン番号 (DN) が付与されない登録が可能です。前者は御社が製品を発売する場合ならば DN が付与されなくても問題ありませんが、

御社が OEM 供給する場合には DN があれば販売企業がそれに紐つけた製品登録を行うことができて、認証の流れが綺麗です。

一方 DN が付与される登録のために、今回見積依頼書に記載いただいた [ID]
(QDID： [ID]) と [ID]

(QDID： [ID]) の組み合わせで私の Workspace で仮 Project を作成して Consystency
Check を実施すると後述の (1) の階層間不整合が検出されました。これらの不整合は GAP あるいは LL のどちらかの ICS を修正することで解消可能ですが、新サイトでは ICS を修正した階層の ICS に対応した試験要求が発生します。

GAP は Excuded(YES→NO にせよ ) ですので簡単だと試しに修正を始めたところモグラたたきのように

Mandatory 項目が山のように出だしたので途中で止めました。 DN が付与される登録をご希望の場合は

SoC の LL が (3) をサポートしているものに変更するか、ホストスタックの GAP が (2) をサポートしていないものを選択し直してください。

結論は今回の [ID] (QDID： [ID]) と [ID]
(QDID： [ID]) の組み合わせでは、組み合わせ QDID

の階層間不整合チェックをしない旧 Declaration 登録相当の登録 (DN は付与されない ) でしたら可能です。

その場合の見積は下記の通りです。

・ RF PHY 試験（1M,
2M）
￥ 700,000

・代行登録サポート費 (Multi-Design 参照 )
￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

旧 Declaration 登録相当の登録（DN は付与されない）で支障がないかご検討ください。

(1) < 階層間不整合一覧 >

11a:C.1 | If [LL] is Supported and [LL] (3/10) is Not Supported then [GAP] (11a/1) is Excluded

17a:C.1 | If [LL] is Supported and [LL] (4/8) is Not Supported then [GAP] (17a/2) is Excluded

17a:C.2 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (17a/1) is Excluded

27a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (27a/1) is Excluded

27a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/2) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (27a/3) is Excluded

27a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (27a/3) is Excluded

37a:C.1 | If [LL] is Supported and [LL] (9/26) is Not Supported then [GAP] (37a/1) is Excluded

37a:C.2 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/2) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (11/1) is Not Supported then [GAP] (37a/3) is Excluded

37a:C.3 | If [LL] is Supported and [LL] (9/27) is Not Supported then [GAP] (37a/3) is Excluded

(2) <GAP の関連 ICS の機能は下記の通りです。 >

11a/1:Periodic Advertising Synchronizability mode

17a/1:Periodic Advertising Synch Establishment procedure without listening for periodic advertising

17a/2:Periodic Advertising Synch Establishment procedure with listening for periodic advertising

27a/1:Periodic Advertising Synch Transfer procedure

27a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

27a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

37a/1:Periodic Advertising Synch Transfer procedure

37a/2:Periodic Advertising Synch Establishment procedure over an LE connection without listening for periodic advertising

37a/3:Periodic Advertising Synch Establishment procedure over an LE connection with listening for periodic advertising

(3) <LL の関連 ICS 機能は以下の通りです。 >

3/10:Periodic Advertising

4/8 :Scanning for Periodic Advertising

9/26:Periodic Advertising Sync Transfer ? Sender

9/27:Periodic Advertising Sync Transfer ? Recipient

11/1:Synchronizing to Periodic Advertising

以上ご検討ください。

差出人 : Nomura Yusuke /
野村裕介

送信日時 : 2024 年 9 月 5 日 17:05

宛先 : Itsuo Sakai

件名 : RE: [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

(堀さんが休みのため、代わってメールします)

添付の見積依頼書を記入しました。

なお、Profiles for Testに関しては、独自プロファイル前提で見積りをお願いします。

ユーザーに問い合わせ中ですが、入手までに時間が掛かりそうであるため。

よろしくお願い致します。

野村裕介ホシデン株式会社技術本部第二技術部技術三課

From: Itsuo Sakai

Sent: Friday, August 30, 2024 6:00 PM

To: Hori Masaki / 堀雅樹

Subject: Re: [ID]/ 認証見積のお願いホシデン堀様アリオンの酒井です。いつもお世話になっております。

ご連絡ありがとうございます。
早速ですが、リストバンド型ウェアラブルデバイス (= スマートウォッチ ) について、認証を取得したく、
下記情報にて試験費・申請費の御見積もりをお願いします。 ( 見積もりに不足する情報がありましたら御連絡ください。 )

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：
類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。 ⇒ TDK の「Silmee
W22」を検索しますと下記の既存登録を参照しています。

QDID:56907 （Profile
Subsystem）

QDID:83565 （Host
Subsystem）

QDID:83573 （Controller
Subsystem）

QDID:56907 （Profile
Subsystem）は多くのプロファイルが登録されているため、「Silmee W22」が実際にサポートしている SIG 制定プロファイルは不明です。前提条件を設けて概算見積額をお答えします。

(1) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、モジュールがアンテナ内蔵型の場合は・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(2) TDK の「Silmee
W22」同様すべての階層が既存の Host Subsystem ＋ Controller
Subsystem ＋ Profile

Subsystem
あるいは End Product ＋ Profile
Subsystem を実装し、 SoC を製品基盤に直実装する場合は・ RF PHY 試験（1M 必須項目） ￥ 400,000

・代行登録サポート (Multi-Design 参照 ) ￥ 250,000

・コンプライアンスフォルダ作成費 ￥ 150,000

（この他に申請者から SIG へ $11,040 のドル送金が必要）

(3)
参照する Profile Subsystem が存在しない場合には、上記見積額に加えて製品でのプロフィル試験費用が発生します。

・プロファイル試験 ￥ 100,000/1 プロフィル設計が進みましたら添付の見積依頼書にご記入・ご送付いただければ営業担当より確定見積書を発行させていただきます。

以上よろしくお願いいたします。

差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係差出人 : Hori Masaki /
堀雅樹

送信日時 : 2024 年 8 月 30 日 17:23

宛先 : Itsuo Sakai

件名 : [ID]/ 認証見積のお願いアリオン酒井様いつもお世話になっております。

ホシデンの堀と申します。

早速ですが、 リストバンド型ウェアラブルデバイス(=スマートウォッチ) について、認証を取得したく、

下記情報にて試験費・申請費の御見積もりをお願いします。(見積もりに不足する情報がありましたら御連絡ください。)

また、サンプル改造が必要か、試験サンプルは何台必要かに関しても、ご教授お願い致します。

製品概要：

類似製品として、下記製品がございます。お手数をおかけしますが、下記リンクをご確認お願い致します。

Silmee&#8482;W22｜生体センサ｜TDKプロダクトセンター
| 製品情報 | TDKプロダクトセンター対象規格：

Blueooth SIG認証無線モード：

BLE1Mモードのみ以上、よろしくお願いいたします。

堀雅樹 / Masaki Hori

ホシデン株式会社技術本部第二技術部技術三課技術一係
