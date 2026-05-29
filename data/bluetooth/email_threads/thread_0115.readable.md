# thread_0115: Re: 【内部連絡】ALPSALPINE様_19AVNJ._Profile試験

- Message count: 4
- Source JSON: `thread_0115.json`

---

## 1. 2025-12-03 11:47

**From:** Itsuo Sakai
**To:** Kousuke Nakayama , Toshitaka Mochizuki

中山さんお疲れさまです。

ご報告ありがとうございます。

明日のFail項目の再試験の件、よろしくお願いします。

酒井差出人: Kousuke Nakayama

送信日時: 2025年12月3日 18:58

宛先: Itsuo Sakai ; Toshitaka Mochizuki

件名: 【内部連絡】ALPSALPINE様_19AVNJ._Profile試験酒井さん、望月さん

CC. 喩さんお疲れ様です。中山です。

[ID] 様の [ID]. の Profile 試験の進捗をご連絡いたします。

一度すべての試験項目を実施し、 9 割ほどは PASS となっております。

いくつか FAIL になっている項目があるため、そちらは明日確認いたします。

よろしくお願いいたします。

中山光祐

---

## 2. 2025-12-04 06:35

**From:** Itsuo Sakai
**To:** Kousuke Nakayama
**Attachments:** yuandeyixinren.zip

中山さんお疲れさまです。
A2DP/SNK/SYN/[ID]Cの実施についてこちらのテスト項目がPTSに無く、実施ができません。
Test Case CategoryがDの項目となりますので、未実施で問題ないとの認識で間違いないでしょうか

⇒はい、試験実施は必須でないのでPTSで試験できなければ対象外です。
Fail項目についてお客様から送付いただいた手順書に従って実施を行いましたが、下記項目でFailとなっております。
・A2DP
AVRCP/CT/MCN/CB/[ID]
・OPP
OPP/SR/GOEP/SRM/[ID]
OPP/SR/GOEP/SRM/[ID]
OPP/SR/GOEP/SRMP/[ID]
OPP/SR/BCE/[ID]
OPP/SR/BCE/[ID]
OPP/SR/BCP/[ID]
OPP/SR/GOEP/BC/[ID]
Logを添付いたしますので、お手数ですがご確認いただき、改善方法などご存じでしたらご教示いただけないでしょうか。
念のため、テスト実行中のTeraTerm画面も添付いたします。

⇒AVRCP/CT/MCN/CB/[ID]Cは512kB以上のメタデータを含む音楽ファイルを使わないと分割(Fragment)が発生しないので試験できません。

添付の音楽ファイルを使ってください。

OPPに関しては望月さんから客先へ問い合わせてもらいます。

酒井差出人: Kousuke Nakayama

送信日時: 2025年12月4日 15:00

宛先: Itsuo Sakai

件名: RE: 【内部連絡】ALPSALPINE様_19AVNJ._Profile試験酒井さんお疲れ様です。中山です。

お忙しいところ恐れ入りますが、以下の点をご確認いただけますでしょうか。

A2DP/SNK/SYN/[ID]Cの実施についてこちらのテスト項目がPTSに無く、実施ができません。

Test Case CategoryがDの項目となりますので、未実施で問題ないとの認識で間違いないでしょうか

Fail項目についてお客様から送付いただいた手順書に従って実施を行いましたが、下記項目でFailとなっております。

・A2DP

AVRCP/CT/MCN/CB/[ID]

・OPP

OPP/SR/GOEP/SRM/[ID]

OPP/SR/GOEP/SRM/[ID]

OPP/SR/GOEP/SRMP/[ID]

OPP/SR/BCE/[ID]

OPP/SR/BCE/[ID]

OPP/SR/BCP/[ID]

OPP/SR/GOEP/BC/[ID]

Logを添付いたしますので、お手数ですがご確認いただき、改善方法などご存じでしたらご教示いただけないでしょうか。

念のため、テスト実行中のTeraTerm画面も添付いたします。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Wednesday, December 3, 2025 8:47 PM

To: Kousuke Nakayama ; Toshitaka Mochizuki

Subject: Re: 【内部連絡】 [ID] 様 _19AVNJ._Profile 試験中山さんお疲れさまです。

ご報告ありがとうございます。

明日の Fail 項目の再試験の件、よろしくお願いします。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 12 月 3 日 18:58

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki

件名 :
【内部連絡】 [ID] 様 _19AVNJ._Profile 試験酒井さん、望月さん

CC.喩さんお疲れ様です。中山です。

ALPSALPINE様の19AVNJ.のProfile試験の進捗をご連絡いたします。

一度すべての試験項目を実施し、9割ほどはPASSとなっております。

いくつかFAILになっている項目があるため、そちらは明日確認いたします。

よろしくお願いいたします。

中山光祐

---

## 3. 2025-12-04 07:13

**From:** Itsuo Sakai
**To:** Kousuke Nakayama , Toshitaka Mochizuki
**Attachments:** TeraTerm-Log_OPP_Fail.zip, PTS_Report_OPP.zip

望月さんお疲れさまです。

添付ファイルとともに以下のメールを客先へ送ってください。

酒井ーーーーご依頼いただきました19AVNのプロファイル試験のOPPでFailが残りました。

お手数ですがFail項目のPTSログ付きレポートおよびTeraTermログをご参照の上、テストサンプルの操作方法などのアドバイスを頂ければ幸いです。

ーーーー差出人: Kousuke Nakayama

送信日時: 2025年12月4日 15:00

宛先: Itsuo Sakai

件名: RE: 【内部連絡】ALPSALPINE様_19AVNJ._Profile試験酒井さんお疲れ様です。中山です。

お忙しいところ恐れ入りますが、以下の点をご確認いただけますでしょうか。

A2DP/SNK/SYN/[ID] の実施についてこちらのテスト項目が PTS に無く、実施ができません。

Test Case Category が D の項目となりますので、未実施で問題ないとの認識で間違いないでしょうか

Fail 項目についてお客様から送付いただいた手順書に従って実施を行いましたが、下記項目で Fail となっております。

・ A2DP

AVRCP/CT/MCN/CB/[ID]

・ OPP

OPP/SR/GOEP/SRM/[ID]

OPP/SR/GOEP/SRM/[ID]

OPP/SR/GOEP/SRMP/[ID]

OPP/SR/BCE/[ID]

OPP/SR/BCE/[ID]

OPP/SR/BCP/[ID]

OPP/SR/GOEP/BC/[ID]

Log を添付いたしますので、お手数ですがご確認いただき、改善方法などご存じでしたらご教示いただけないでしょうか。

念のため、テスト実行中の TeraTerm 画面も添付いたします。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Wednesday, December 3, 2025 8:47 PM

To: Kousuke Nakayama ; Toshitaka Mochizuki

Subject: Re: 【内部連絡】 [ID] 様 _19AVNJ._Profile 試験中山さんお疲れさまです。

ご報告ありがとうございます。

明日の Fail 項目の再試験の件、よろしくお願いします。

酒井差出人 :
Kousuke Nakayama

送信日時 :
2025 年 12 月 3 日
18:58

宛先 :
Itsuo Sakai ;
Toshitaka Mochizuki

件名 :
【内部連絡】 [ID] 様 _19AVNJ._Profile 試験酒井さん、望月さん

CC. 喩さんお疲れ様です。中山です。

[ID] 様の [ID]. の Profile 試験の進捗をご連絡いたします。

一度すべての試験項目を実施し、 9 割ほどは PASS となっております。

いくつか FAIL になっている項目があるため、そちらは明日確認いたします。

よろしくお願いいたします。

中山光祐

---

## 4. 2025-12-08 09:18

**From:** Itsuo Sakai
**To:** Kenichi Ushiroebisu , "Toshitaka Mochizuki"

望月さんお疲れさまです。

BQTFが一般的な試験実施方法なんて恥ずかしいことを聞かないでください。

PTSの以下のように対応してください。

TSPX_no_cover_art_folder Path a folder in the virtual file system that has media elements, none of which have cover art(only used by cover art test cases). Example: &quot;\Playlists\NoCoverArt&quot; (Default: &quot;&quot;)

酒井差出人: Kenichi Ushiroebisu

送信日時: 2025年12月8日 18:01

宛先: Toshitaka Mochizuki

件名: Re: 【内部連絡】ALPSALPINE様_19AVNJ._Profile試験望月さん、

お疲れ様です。

ALPSALPINE様の19AVNJ._Profile試験ですが、&quot; AVRCP/CT/MCN/CB/[ID]&quot;以外はすべてPASSいたしました。

&quot; AVRCP/CT/MCN/CB/[ID]&quot;について、お客様に下記の問い合わせをしていただけますでしょうか。

&quot; AVRCP/CT/MCN/CB/[ID]&quot;について、手順書(PTS_Guide_AVRCP.pdf)に従ってテストを行いましたが&quot;FAIL&quot;となりました。

この試験は、512kB以上のメタデータを含む音楽ファイルを使わないと分割(Fragment)が発生しないので試験できないと理解しております。

音楽ファイルはこちらで用意したものがありますので、このファイルをどこに置いて、どのように指定すればよいかをご教示いただけますでしょうか。

よろしくお願いいたします。

後夷差出人: Itsuo Sakai

送信: 2025 年 12 月 4 日 (木曜日) 15:35

宛先: Kousuke Nakayama

件名: Re: 【内部連絡】ALPSALPINE様_19AVNJ._Profile試験中山さんお疲れさまです。
A2DP/SNK/SYN/[ID]Cの実施についてこちらのテスト項目がPTSに無く、実施ができません。
Test Case CategoryがDの項目となりますので、未実施で問題ないとの認識で間違いないでしょうか

⇒はい、試験実施は必須でないのでPTSで試験できなければ対象外です。
Fail項目についてお客様から送付いただいた手順書に従って実施を行いましたが、下記項目でFailとなっております。
・A2DP
AVRCP/CT/MCN/CB/[ID]
・OPP
OPP/SR/GOEP/SRM/[ID]
OPP/SR/GOEP/SRM/[ID]
OPP/SR/GOEP/SRMP/[ID]
OPP/SR/BCE/[ID]
OPP/SR/BCE/[ID]
OPP/SR/BCP/[ID]
OPP/SR/GOEP/BC/[ID]
Logを添付いたしますので、お手数ですがご確認いただき、改善方法などご存じでしたらご教示いただけないでしょうか。
念のため、テスト実行中のTeraTerm画面も添付いたします。

⇒AVRCP/CT/MCN/CB/[ID]Cは512kB以上のメタデータを含む音楽ファイルを使わないと分割(Fragment)が発生しないので試験できません。

添付の音楽ファイルを使ってください。

OPPに関しては望月さんから客先へ問い合わせてもらいます。

酒井差出人: Kousuke Nakayama

送信日時: 2025年12月4日 15:00

宛先: Itsuo Sakai

件名: RE: 【内部連絡】ALPSALPINE様_19AVNJ._Profile試験酒井さんお疲れ様です。中山です。

お忙しいところ恐れ入りますが、以下の点をご確認いただけますでしょうか。

A2DP/SNK/SYN/[ID]Cの実施についてこちらのテスト項目がPTSに無く、実施ができません。

Test Case CategoryがDの項目となりますので、未実施で問題ないとの認識で間違いないでしょうか

Fail項目についてお客様から送付いただいた手順書に従って実施を行いましたが、下記項目でFailとなっております。

・A2DP

AVRCP/CT/MCN/CB/[ID]

・OPP

OPP/SR/GOEP/SRM/[ID]

OPP/SR/GOEP/SRM/[ID]

OPP/SR/GOEP/SRMP/[ID]

OPP/SR/BCE/[ID]

OPP/SR/BCE/[ID]

OPP/SR/BCP/[ID]

OPP/SR/GOEP/BC/[ID]

Logを添付いたしますので、お手数ですがご確認いただき、改善方法などご存じでしたらご教示いただけないでしょうか。

念のため、テスト実行中のTeraTerm画面も添付いたします。

よろしくお願いいたします。

中山光祐

From: Itsuo Sakai

Sent: Wednesday, December 3, 2025 8:47 PM

To: Kousuke Nakayama ; Toshitaka Mochizuki

Subject: Re: 【内部連絡】 [ID] 様 _19AVNJ._Profile 試験中山さんお疲れさまです。

ご報告ありがとうございます。

明日の Fail 項目の再試験の件、よろしくお願いします。

酒井差出人 : Kousuke Nakayama

送信日時 : 2025 年 12 月 3 日 18:58

宛先 : Itsuo Sakai ;
Toshitaka Mochizuki

件名 :
【内部連絡】 [ID] 様 _19AVNJ._Profile 試験酒井さん、望月さん

CC.喩さんお疲れ様です。中山です。

ALPSALPINE様の19AVNJ.のProfile試験の進捗をご連絡いたします。

一度すべての試験項目を実施し、9割ほどはPASSとなっております。

いくつかFAILになっている項目があるため、そちらは明日確認いたします。

よろしくお願いいたします。

中山光祐
