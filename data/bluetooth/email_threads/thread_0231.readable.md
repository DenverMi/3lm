# thread_0231: [内部連絡] Re: 【Bluetooth Test Request】[Internal]Alinco [ID] Bluetooth logo test RF PHY at HQ

- Message count: 1
- Source JSON: `thread_0231.json`

---

## 1. 2026-01-30 03:47

**From:** Itsuo Sakai
**To:** Toshitaka Mochizuki

望月さんお疲れさまです。

レポートをチェックし、問題ありませんでしたのでこれで試験完了です。

酒井差出人: Toshitaka Mochizuki

送信日時: 2026年1月30日 11:32

宛先: Leo Chou(周展弘) ; Itsuo Sakai ; Ning Lin(林芷寧)

件名: RE: 【Bluetooth Test Request】[Internal]Alinco [ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

Thank you very much for your testing support!

We will check this.

Thank you very much for your hard work!

Best Regards.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

From: Leo Chou( 周展弘 )

Sent: Friday, January 30, 2026 11:16 AM

To: Itsuo Sakai ; Toshitaka Mochizuki ; Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Sakai-san and Mochizuki-san

This testing is complete, please refer the attached file for report and logs

Thank you

Leo Chou

From: Leo Chou( 周展弘 )

Sent: Wednesday, January 28, 2026 3:44 PM

To: JP_Itsuo Sakai; JP_Toshitaka Mochizuki; Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Sakai-san

OK, I will set to Non-power class 1 and re-test it

Thank you

Leo Chou

From: Itsuo Sakai [ mailto: ]

Sent: Wednesday, January 28, 2026 2:59 PM

To: Leo Chou( 周展弘 ); JP_Toshitaka Mochizuki; Ning Lin( 林芷寧 )

Subject: Re: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Leo-san,

This is Sakai sending Email by proxy of Mochizuki-san,

I'm sorry that the SoC([ID]) isn't Class 1 bacause it was qulified

under Core Spec. v5.2 that didn't define Class 1.

Please re-start the RF PHY testing under attached Test plan.

Thanks.

Best regard,

Itsuo Sakai

差出人 : Leo
Chou( 周展弘 )

送信日時 : 2026 年 1 月 27 日
14:24

宛先 : Toshitaka
Mochizuki ; Ning Lin( 林芷寧 )

件名 : RE:
【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

OK, I will suspend this testing

Thank you

Leo Chou

From: Toshitaka Mochizuki [ mailto: ]

Sent: Tuesday, January 27, 2026 9:43 AM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

Thank you very much for your testing.

We ’ re sorry that the Outpot power isn't meet the RF
PHY test requirement.

I just requested Alinco to update the DUT's output power setting more than 10dBm.

Please stop RF PHY test until the new FW or DUT is provided.

Thank you.

Best Regards.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

From: Leo Chou( 周展弘 )

Sent: Tuesday, January 27, 2026 10:32 AM

To: Toshitaka Mochizuki ; Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

We also measured it is within this range. But it is under 10 dBm so this DUT should not be LE power class 1 device.

[ID]:10:1

Maximum TX mode output power

10 to 20

dBm

Please check it

Thank you

Leo Chou

From: Toshitaka Mochizuki [ mailto: ]

Sent: Monday, January 26, 2026 5:29 PM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

Thank you very much for your confirmation.

For RFPHY/TRM/[ID], it was as follows.

• 2402MHz: Pavg=8.61dBm

• 2440MHz: Pavg=8.91dBm

• 2480MHz: Pavg=9.23dBm

Could you check with the values above？

Thank you.

Best Regards.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

From: Leo Chou( 周展弘 )

Sent: Monday, January 26, 2026 6:03 PM

To: Toshitaka Mochizuki ; Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

After changes the USB 3.0 cable , DUT can load properly， I
seem it is power class 1 support check on IXIT file. Could you provide how many the PAVG is with 1MBLE Measurement.

Thank you

Leo Chou

From: Toshitaka Mochizuki [ mailto: ]

Sent: Monday, January 26, 2026 3:42 PM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

We received the following comment from Alinco. Is it possible?

★ If the error occurs, try changing the PC or changing the USB cable.

It may be resolved.

I'm not sure which combination is best, but

Errors are less likely to occur on Windows 10 PCs.

Instead of the USB cable included with [ID],

If you use a [ID] cable, the error will not occur.

(Cable with B terminal [[ID] side] shaped like the attached photo)

Could you please confirm the above?

Thank you.

Best Regards.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

From: Leo Chou( 周展弘 )

Sent: Wednesday, January 21, 2026 11:44 AM

To: Toshitaka Mochizuki ; Ning Lin( 林芷寧 )

Subject: RE: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

Due to I
will be taking leave this Friday. If [ID] is not executed, it is expected to be completed next Monday (1/26)

Thank you

Leo Chou

From: Toshitaka Mochizuki [ mailto: ]

Sent: Wednesday, January 21, 2026 10:01 AM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: Re: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Leo-san, thank you for your flexible response.

An AlpsAlpine customer has contacted us asking for an estimated completion date. Please let us know your current estimated completion date.

Thank you very much for your support.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

差出人 : Leo Chou( 周展弘 )

送信 : 2026
年 1
月 21
日 ( 水曜日 )
10:52

宛先 : Toshitaka Mochizuki ;
Ning Lin( 林芷寧 )

件名 : RE:
【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

I will execute the UXC10 project first.

Thank you

Leo Chou

From: Toshitaka Mochizuki [ mailto: ]

Sent: Wednesday, January 21, 2026 9:35 AM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: Re: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

Thank you very much for your confirmation.

I am aware that there is no need to update the FW this time.

The person in charge is off today, so I will have to confirm tomorrow.

If possible, could you please move forward with AlpseAlpine testing?

Thank you.

Best Regards.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

差出人 : Leo Chou( 周展弘 )

送信 : 2026
年 1
月 21
日 ( 水曜日 )
10:21

宛先 : Toshitaka Mochizuki ;
Ning Lin( 林芷寧 )

件名 : RE:
【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

The DUT log seems different with document, DUT does not return the firmware version information:

Opening USB TRB ([ID]).

Transport active.

Chip Family [ID] (aup) (Family ID 0x114B).

Failed call to teGetBuildId

Is it need to up
firmware ? Please provide the firmware file if needed.

Thank you

Leo Chou

From: Toshitaka Mochizuki [ mailto: ]

Sent: Tuesday, January 20, 2026 6:10 PM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: Re: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

Thank you very much for your testing.

I have attached the test memo from when I took the test at AJ. Could you please check it?

Please let us know if you continue to have problems.

Thank you very much for your support.

Best Regards.

Mochizuki

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

差出人 : Leo Chou( 周展弘 )

送信 : 2026
年 1
月 20
日 ( 火曜日 )
18:30

宛先 : Toshitaka Mochizuki ;
Ning Lin( 林芷寧 )

件名 : RE:
【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

I have install the [ID] driver and fallow the settings to set up (after install the [ID] driver LED is light
on when connect DUT)， but DUT still not working and shows error message when running LE HCI commands:

Please refer the 1020 log files, it seems “Failed call to teGetBuildId” and failed to running tester HCI commands:

[ID]: Read [ID] command received

Read [ID] : failed

Read [ID] unsupported, ignoring request.

[ID]: LETE command received

[ID]: LEETT command received (Channel 0, Length 37, Payload Type 0, PHY 1)

BLE TEST TX failed

Could you provide any suggest

Thank you

From: Toshitaka Mochizuki [ mailto: ]

Sent: Tuesday, January 20, 2026 1:59 PM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: Re: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

Thank you very much for your confirmation.

We remember that this DUT was still operating internally even though the LED was off.

Please refer to the attached document for [ID] setup.

thank you.

Best Regards.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250

差出人 : Leo Chou( 周展弘 )

送信 : 2026
年 1
月 20
日 ( 火曜日 )
12:47

宛先 : Toshitaka Mochizuki ;
Ning Lin( 林芷寧 )

件名 : RE:
【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Mochizuki-san

I have received the [ID] DUT, But the DUT cannot power on propyl , according to the [ID] test sample information,
to hold power switch for 3 seconds to start the device, but once the button is released then the DUT is auto power off:

And it need the driver for the USB connect:

Please confirm it

Thank you

From: Toshitaka Mochizuki [ mailto: ]

Sent: Wednesday, January 7, 2026 3:27 PM

To: Leo Chou( 周展弘 ); Ning Lin( 林芷寧 )

Subject: 【Bluetooth Test Request】 [Internal]Alinco
[ID] Bluetooth logo test RF PHY at HQ

Hi Leo-san

We would like to request Bluetooth RF PHY test for Alinco [ID] in HQ.

Could you arrange the test slot for this project?

DUT has been shipped today via CTSP.

The test plan is attached. Could you refer it?

Could you arrange the test slot when you will receive the DUT later?

Please let me know if you have any problems and questions.

Project ID is below:

Thank you.

Best Regards.

Mochizuki.

Toshitaka Mochizuki

Allion Japan Inc.

Sales Division

4F, Building B
TokyoSRC 1-1-1 Katsushima
Shinagawa-ku

Tokyo Japan

+[ID]

Ext 52250
