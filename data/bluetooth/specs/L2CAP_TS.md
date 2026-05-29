## **Logical Link Control and Adaptation Protocol (L2CAP)**

## _**Bluetooth[®]**_ **Test Suite**

- **Revision:** L2CAP.TS _._ p41

- **Revision Date:** 2025-11-04

- **Prepared By:** BTI

- **Published during TCRL:** TCRL.pkg101

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.**

**THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.**

**TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.**

**This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.**

## **This document is subject to change without notice.**

**Copyright © 2003–2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.**

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **2 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **Contents**

|**1**|**Scope ................................................................................................................................................... 12**|
|**2**|**References, definitions, and abbreviations ..................................................................................... 13**|
||2.1<br>References .................................................................................................................................. 13|
||2.2<br>Definitions ................................................................................................................................... 13|
||2.3<br>Acronyms and abbreviations ...................................................................................................... 13|
|**3**|**Test Suite Structure (TSS) ................................................................................................................. 14**|
||3.1<br>Test Strategy ............................................................................................................................... 14|
||3.2<br>Test groups ................................................................................................................................. 14|
||3.2.1<br>Protocol service groups ........................................................................................................................ 14|
||3.2.2<br>Main test groups ................................................................................................................................... 16|
||3.2.3<br>Behavior testing groups ........................................................................................................................ 16|
|**4**|**Test cases (TC) ................................................................................................................................... 17**|
||4.1<br>Test case identification conventions ........................................................................................... 17|
||4.2<br>MSC abbreviations...................................................................................................................... 18|
||4.3<br>Conformance .............................................................................................................................. 18|
||4.4<br>Lower layer assumptions ............................................................................................................ 19|
||4.5<br>Upper Tester ............................................................................................................................... 19|
||4.6<br>General information about MSC ................................................................................................. 19|
||4.7<br>Pass/Fail verdict conventions ..................................................................................................... 19|
||4.8<br>Preamble IXITs ........................................................................................................................... 19|
||4.9<br>Common Packet Contents .......................................................................................................... 20|
||4.9.1<br>Fields and Bits Reserved for Future Use .............................................................................................. 20|
||4.10 Connection-Oriented Basic L2CAP mode .................................................................................. 20|
||4.10.1<br>Basic Operation Data Channel CED ..................................................................................................... 20|
||L2CAP/COS/CED/BV-01-C [Request Connection] ............................................................................................... 20|
||L2CAP/COS/CED/BV-03-C [Send Data] ............................................................................................................... 21|
||L2CAP/COS/CED/BV-04-C [Disconnect] .............................................................................................................. 22|
||L2CAP/COS/CED/BV-07-C [Accept Disconnect] .................................................................................................. 23|
||L2CAP/COS/CED/BV-08-C [Disconnect on Timeout] ........................................................................................... 23|
||L2CAP/COS/CED/BV-09-C [Receive Multi-Command Packet] ............................................................................. 25|
||L2CAP/COS/CED/BV-10-C [Transmit I-frames] .................................................................................................... 26|
||L2CAP/COS/CED/BV-11-C [Configure MTU Size] ............................................................................................... 27|
||L2CAP/COS/CED/BV-12-C [Recombination of Signaling Packets] ...................................................................... 27|
||L2CAP/COS/CED/BI-03-C [Incorrect PDU Length, Received Data Packet, Basic] ............................................... 28|
||L2CAP/COS/CED/BI-04-C [Incorrect PDU Length, C-Frame, BR/EDR] ............................................................... 30|
||L2CAP/COS/CED/BI-05-C [Incorrect PDU Length, C-Frame, LE Credit Based Connection Request] ................. 30|
||L2CAP/COS/CED/BI-18-C [Incorrect PDU Length, C-Frame, LE Enhanced Credit Based Connection|
||Request]................................................................................................................................................................ 30|
||L2CAP/COS/CED/BI-19-C [Incorrect PDU Length, C-Frame, LE Credit Based Connection Request|
||Rejected] ............................................................................................................................................................... 30|
||L2CAP/COS/CED/BI-06-C [Incorrect PDU Length, Received Data Packets with Continuation, Basic] ................ 31|
||L2CAP/COS/CED/BI-07-C [Incorrect PDU Length, Received Data Packets with Multiple Continuation] .............. 32|
||L2CAP/COS/CED/BI-08-C [Valid Signaling Command, Data Length > PDU Space, BR/EDR] ............................ 33|
||L2CAP/COS/CED/BI-09-C [Valid Signaling Command, Data Length > PDU Space, LE Credit Based|
||Connection Request] ............................................................................................................................................ 33|
||L2CAP/COS/CED/BI-20-C [Valid Signaling Command, Data Length > PDU Space, LE Enhanced Credit|
||Based Connection Request] ................................................................................................................................. 34|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **3 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|L2CAP/COS/CED/BI-21-C [Valid Signaling Command, Data Length > PDU Space, LE Credit Based|
|---|
|Connection Request Rejected] ............................................................................................................................. 34|
|L2CAP/COS/CED/BI-10-C [Incorrect Signaling Command Packets, Invalid Data Length for Command,|
|BR/EDR] ............................................................................................................................................................... 35|
|L2CAP/COS/CED/BI-11-C [Incorrect Signaling Command Packets, Invalid Data Length for Command,|
|LE] ........................................................................................................................................................................ 35|
|L2CAP/COS/CED/BI-12-C [Valid Signaling Command, Shorter Data Length, Extra Zero Octet, BR/EDR] .......... 36|
|L2CAP/COS/CED/BI-13-C [Valid Signaling Command, Shorter Data Length, Extra Zero Octet, LE Credit|
|Based Connection Request] ................................................................................................................................. 38|
|L2CAP/COS/CED/BI-22-C [Valid Signaling Command, Data Length > PDU Space, LE Enhanced Credit|
|Based Connection Request] ................................................................................................................................. 38|
|L2CAP/COS/CED/BI-23-C [Valid Signaling Command, Data Length > PDU Space, LE Enhanced Credit|
|Based Connection Request Rejected] .................................................................................................................. 38|
|L2CAP/COS/CED/BI-14-C [Multiple Signaling Command in one PDU, Data Truncated, BR/EDR, Echo|
|Request]................................................................................................................................................................ 40|
|L2CAP/COS/CED/BI-15-C [Multiple Signaling Command in one PDU, Data Truncated, BR/EDR,|
|Disconnection Request] ........................................................................................................................................ 40|
|L2CAP/COS/CED/BI-16-C [Multiple Signaling Command in one PDU, Data Truncated, LE Credit Based|
|Flow Control Mode, LE Credit Based Connection Request] ................................................................................. 42|
|L2CAP/COS/CED/BI-17-C [Multiple Signaling Command in one PDU, Data Truncated, LE Credit Based|
|Flow Control Mode, Disconnection Request] ........................................................................................................ 42|
|L2CAP/COS/CED/BI-24-C [Multiple Signaling Command in one PDU, LE, Data Truncated, Enhanced|
|Credit Based Flow Control Mode, Enhanced Credit Based Connection Request] ................................................ 42|
|L2CAP/COS/CED/BI-25-C [Multiple Signaling Command in one PDU, LE, Data Truncated, Enhanced|
|Credit Based Flow Control Mode, Disconnection Request]................................................................................... 42|
|L2CAP/COS/CED/BI-28-C [Ignore Command Response with Invalid ID or Duplicate Response,|
|BR/EDR] ............................................................................................................................................................... 44|
|L2CAP/COS/CED/BI-29-C [Ignore Command Response with Invalid ID or Duplicate Response, LE] .................. 44|
|4.10.2<br>Encryption Key Size .............................................................................................................................. 45|
|4.10.3<br>Configuration of Data Channel CFD ..................................................................................................... 45|
|L2CAP/COS/CFD/BV-01-C [Continuation Flag] .................................................................................................... 45|
|L2CAP/COS/CFD/BV-02-C [Negotiation with Reject] ........................................................................................... 47|
|L2CAP/COS/CFD/BV-03-C [Send Requested Options] ........................................................................................ 48|
|L2CAP/COS/CFD/BV-08-C [Non-blocking Config Response]............................................................................... 48|
|L2CAP/COS/CFD/BV-09-C [Mandatory 48 Byte MTU] ......................................................................................... 49|
|L2CAP/COS/CFD/BV-10-C [Retransmission Mode Negotiation] .......................................................................... 51|
|L2CAP/COS/CFD/BV-11-C [Negotiation of Unsupported Parameter] ................................................................... 51|
|L2CAP/COS/CFD/BV-12-C [Unknown Option Response] .................................................................................... 52|
|L2CAP/COS/CFD/BV-13-C [Flow Control Mode Negotiation] ............................................................................... 53|
|L2CAP/COS/CFD/BV-14-C [Unknown Mandatory Options Request] ................................................................... 54|
|4.10.4<br>Implementation-Specific Information Exchange IEX ............................................................................. 55|
|L2CAP/COS/IEX/BV-01-C [Query for 1.2 Features] ............................................................................................. 55|
|L2CAP/COS/IEX/BV-02-C [Respond with 1.2 Features] ....................................................................................... 56|
|4.10.5<br>Echo Handling ECH .............................................................................................................................. 57|
|L2CAP/COS/ECH/BV-01-C [Respond to Echo Request] ...................................................................................... 57|
|L2CAP/COS/ECH/BV-02-C [Send Echo Request] ................................................................................................ 58|
|4.10.6<br>LE Credit Based Flow Control Mode ..................................................................................................... 58|
|L2CAP/COS/CFC/BV-01-C [Segmentation] .......................................................................................................... 58|
|L2CAP/COS/CFC/BV-02-C [No Segmentation] .................................................................................................... 59|
|L2CAP/COS/CFC/BV-03-C [Reassembling] ......................................................................................................... 60|
|L2CAP/COS/CFC/BV-04-C [Data Receiving] ........................................................................................................ 61|
|L2CAP/COS/CFC/BV-05-C [Multiple Channels with Interleaved Data Streams]................................................... 62|
|L2CAP/LE/CFC/BV-30-C [Recombination of Signaling Packets] .......................................................................... 65|
|L2CAP/ECFC/BV-39-C [Recombination of Signaling Packets - LE] ..................................................................... 65|
|L2CAP/ECFC/BV-40-C [Recombination of Signaling Packets – BR/EDR] ........................................................... 65|
|L2CAP/LE/CFC/BV-31-C [Recombination of Data Packets] ................................................................................. 67|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **4 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|L2CAP/ECFC/BV-41-C [Recombination of Data Packets] .................................................................................... 67|
|---|
|L2CAP/ECFC/BV-42-C [Recombination of Data Packets] .................................................................................... 67|
|L2CAP/ECFC/BI-09-C [Incorrect Size Signaling Packets, BR/EDR] ..................................................................... 68|
|4.10.7<br>Enhanced Credit Based Flow Control Mode ......................................................................................... 70|
|L2CAP/COS/ECFC/BV-01-C [Segmentation, LE] ................................................................................................. 70|
|L2CAP/COS/ECFC/BV-05-C [Segmentation, BR/EDR] ........................................................................................ 70|
|L2CAP/COS/ECFC/BV-02-C [Reassembling, LE] ................................................................................................ 71|
|L2CAP/COS/ECFC/BV-06-C [Reassembling, BR/EDR] ....................................................................................... 71|
|L2CAP/COS/ECFC/BV-03-C [Multiple Channels with Interleaved Data Streams, LE] .......................................... 72|
|L2CAP/COS/ECFC/BV-07-C [Multiple Channels with Interleaved Data Streams, BR/EDR] ................................. 72|
|L2CAP/COS/ECFC/BV-04-C [Reassembling, LE] ................................................................................................ 73|
|L2CAP/COS/ECFC/BV-08-C [Reassembling, BR/EDR] ....................................................................................... 73|
|4.11 Connection-Oriented Retransmission/Flow Control/Streaming modes ...................................... 74|
|4.11.1<br>Flow Control .......................................................................................................................................... 74|
|L2CAP/COS/FLC/BV-01-C [Flow Control without Acks] ....................................................................................... 74|
|L2CAP/COS/FLC/BV-02-C [Resume Flow on RR Frame Ack] ............................................................................. 75|
|L2CAP/COS/FLC/BV-03-C [Resume Flow on I-frame Ack] .................................................................................. 76|
|L2CAP/COS/FLC/BV-04-C [Transmit RR Frame on Monitor Timeout] ................................................................. 77|
|4.11.2<br>Retransmission ..................................................................................................................................... 77|
|L2CAP/COS/RTX/BV-01-C [No Retransmission with R=1] ................................................................................... 77|
|L2CAP/COS/RTX/BV-02-C [Retransmission with R=0 in RR frame] .................................................................... 78|
|L2CAP/COS/RTX/BV-03-C [Retransmission with R=0 in I-frame] ........................................................................ 79|
|4.11.3<br>Extended Features (EXF) ..................................................................................................................... 80|
|L2CAP/EXF/BV-07-C [Extended Features Information Response] ....................................................................... 80|
|L2CAP/EXF/BV-08-C [Information Request, Extended Features] ......................................................................... 81|
|4.11.4<br>Channel Mode Configuration (CMC) ..................................................................................................... 82|
|L2CAP/CMC/BV-01-C [IUT Initiated Configuration of Enhanced Retransmission Mode] ...................................... 82|
|L2CAP/CMC/BV-02-C [Lower Tester Initiated Configuration of Enhanced Retransmission Mode] ....................... 83|
|L2CAP/CMC/BV-03-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode|
|is Optional] ............................................................................................................................................................ 84|
|L2CAP/CMC/BV-04-C [IUT Initiated Configuration of Streaming Mode] ............................................................... 85|
|L2CAP/CMC/BV-05-C [Lower Tester Initiated Configuration of Streaming Mode] ................................................ 86|
|L2CAP/CMC/BV-06-C [Failed Configuration of Streaming Mode when use of the Mode is Optional] ................... 87|
|L2CAP/CMC/BV-07-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is|
|Optional]................................................................................................................................................................ 88|
|L2CAP/CMC/BV-08-C [Configuration Mode Mismatch when use of Streaming Mode is Optional] ....................... 89|
|L2CAP/CMC/BV-09-C [Configuration to Basic Mode by the IUT] ......................................................................... 90|
|L2CAP/CMC/BI-01-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is|
|Mandatory] ............................................................................................................................................................ 92|
|L2CAP/CMC/BI-02-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is|
|Mandatory] ............................................................................................................................................................ 93|
|L2CAP/CMC/BI-03-C [Failed Configuration of Streaming Mode when use of the Mode is Mandatory] ................ 93|
|L2CAP/CMC/BI-04-C [Configuration Mode mismatch when use of Streaming Mode is Mandatory] ..................... 94|
|L2CAP/CMC/BI-05-C [Failed Configuration to Basic Mode by the IUT] ................................................................ 95|
|L2CAP/CMC/BI-06-C [Configuration to Basic Mode Rejected by the Lower Tester] ............................................. 96|
|L2CAP/CMC/BV-10-C [ERTM Not Supported by Lower Tester for Optional ERTM Channel] .............................. 97|
|L2CAP/CMC/BV-11-C [Streaming Mode not supported by Lower Tester for Optional Streaming Mode|
|Channel]................................................................................................................................................................ 98|
|L2CAP/CMC/BV-12-C [ERTM Not Supported by Lower Tester for Mandatory ERTM channel] ........................... 99|
|L2CAP/CMC/BV-13-C [Streaming Mode not supported by Lower Tester for Mandatory Streaming Mode|
|Channel].............................................................................................................................................................. 100|
|L2CAP/CMC/BV-14-C [Failed Configuration of Streaming Mode when use of the mode is optional and|
|ERTM is proposed by the Lower Tester] ............................................................................................................. 101|
|L2CAP/CMC/BV-15-C [Configuration Mode Mismatch when use of Streaming Mode is Optional and|
|ERTM is proposed by the Lower Tester] ............................................................................................................. 102|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **5 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|4.11.5<br>Frame Check Sequence (FCS) Option Configuration (FOC) .............................................................. 104|
|---|
|L2CAP/FOC/BV-01-C [IUT Initiated Configuration of the FCS Option, IUT No FCS Option, Lower Tester|
|No FCS Option] ................................................................................................................................................... 104|
|L2CAP/FOC/BV-02-C [IUT Initiated Configuration of the FCS Option, IUT No FCS Option, Lower Tester|
|Yes FCS Option] ................................................................................................................................................. 104|
|L2CAP/FOC/BV-03-C [IUT Initiated Configuration of the FCS Option, IUT No FCS Option, Lower Tester|
|Omitted FCS Option] ........................................................................................................................................... 104|
|L2CAP/FOC/BV-04-C [IUT Initiated Configuration of the FCS Option, IUT FCS 0x01] ....................................... 106|
|L2CAP/FOC/BV-06-C [IUT Initiated Configuration of the FCS Option, IUT FCS Omitted] .................................. 106|
|L2CAP/FOC/BV-05-C [IUT Responder, Configuration of the FCS Option, IUT FCS 0x00] ................................. 108|
|L2CAP/FOC/BV-07-C [IUT Responder, Configuration of the FCS Option, IUT FCS 0x01] ................................. 108|
|L2CAP/FOC/BV-08-C [IUT Responder, Configuration of the FCS Option, IUT FCS Omitted] ............................ 108|
|4.11.6<br>Optional FCS (OFS) ............................................................................................................................ 110|
|L2CAP/OFS/BV-01-C [Sending I-Frames without FCS for ERTM] ..................................................................... 110|
|L2CAP/OFS/BV-02-C [Receiving Frames without FCS for ERTM] ..................................................................... 110|
|L2CAP/OFS/BV-03-C [Sending I-Frames without FCS for Streaming Mode] ..................................................... 111|
|L2CAP/OFS/BV-04-C [Receiving Frames without FCS for Streaming Mode] ..................................................... 112|
|L2CAP/OFS/BV-05-C [Sending I-Frames with FCS for ERTM] .......................................................................... 112|
|L2CAP/OFS/BV-06-C [Receiving Frames with FCS for ERTM] .......................................................................... 113|
|L2CAP/OFS/BV-07-C [Sending I-Frames with FCS for Streaming Mode] .......................................................... 114|
|L2CAP/OFS/BV-08-C [Receiving Frames with FCS for Streaming Mode] .......................................................... 114|
|4.11.7<br>Enhanced Retransmission Mode (ERM) ............................................................................................. 115|
|L2CAP/ERM/BV-01-C [Transmit I-frames] .......................................................................................................... 115|
|L2CAP/ERM/BV-02-C [Receive I-Frames] .......................................................................................................... 116|
|L2CAP/ERM/BV-03-C [Acknowledging Received I-Frames] ............................................................................... 118|
|L2CAP/ERM/BV-05-C [Resume Transmitting I-Frames when an S-Frame [RR] is Received] ............................ 118|
|L2CAP/ERM/BV-06-C [Resume Transmitting I-Frames when an I-Frame is Received] ..................................... 119|
|L2CAP/ERM/BV-07-C [Send S-Frame [RNR]] .................................................................................................... 120|
|L2CAP/ERM/BV-08-C [Send S-Frame [RR] with Poll Bit Set] ............................................................................. 121|
|L2CAP/ERM/BV-09-C [Send S-frame [RR] with Final Bit Set] ............................................................................ 122|
|L2CAP/ERM/BV-10-C [Retransmit S-Frame [RR] with Poll Bit Set] .................................................................... 123|
|L2CAP/ERM/BV-11-C [S-Frame Transmissions Exceed MaxTransmit] ............................................................. 124|
|L2CAP/ERM/BV-12-C [I-Frame Transmissions Exceed MaxTransmit] ............................................................... 125|
|L2CAP/ERM/BV-13-C [Respond to S-Frame [REJ]] ........................................................................................... 126|
|L2CAP/ERM/BV-14-C [Respond to S-Frame [SREJ] POLL Bit Set] ................................................................... 127|
|L2CAP/ERM/BV-15-C [Respond to S-Frame [SREJ] POLL bit clear] ................................................................. 128|
|L2CAP/ERM/BV-16-C [Send S-Frame [REJ]] ..................................................................................................... 129|
|L2CAP/ERM/BV-17-C [Send S-Frame [SREJ]] ................................................................................................... 130|
|L2CAP/ERM/BV-18-C [Receive S-Frame [RR] Final Bit = 1] .............................................................................. 131|
|L2CAP/ERM/BV-19-C [Receive I-Frame Final Bit = 1] ........................................................................................ 132|
|L2CAP/ERM/BV-20-C [Enter Remote Busy Condition] ....................................................................................... 133|
|L2CAP/ERM/BV-22-C [Exit Local Busy Condition] ............................................................................................. 134|
|L2CAP/ERM/BV-23-C [Transmit I-Frames using SAR] ....................................................................................... 135|
|L2CAP/ERM/BI-01-C [S-Frame [REJ] Lost or Corrupted] ................................................................................... 136|
|L2CAP/ERM/BI-02-C [S-Frame [SREJ] Lost or Corrupted] ................................................................................ 137|
|L2CAP/ERM/BI-03-C [Handle Duplicate S-Frame [SREJ]] ................................................................................. 138|
|L2CAP/ERM/BI-04-C [Handle Receipt of S-Frame [REJ] and S-Frame [RR, F=1] that Both Require|
|Retransmission of the Same I-Frames] ............................................................................................................... 139|
|L2CAP/ERM/BI-05-C [Handle receipt of S-Frame [REJ] and I-Frame [F=1] that Both Require|
|Retransmission of the Same I-Frames] ............................................................................................................... 140|
|4.11.8<br>Streaming Mode (STM) ....................................................................................................................... 142|
|L2CAP/STM/BV-01-C [Streaming Mode Source] ................................................................................................ 142|
|L2CAP/STM/BV-02-C [Streaming Mode Sink] .................................................................................................... 142|
|L2CAP/STM/BV-03-C [Streaming Mode Source using SAR] .............................................................................. 143|
|4.11.9<br>Fixed Channel Support (FIX) .............................................................................................................. 144|
|L2CAP/FIX/BV-01-C [Fixed Channels Supported Information Request] ............................................................. 144|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **6 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

L2CAP/FIX/BV-02-C [AMP Manager Channel Supported] .................................................................................. 145 L2CAP/FIX/BV-03-C [Information Request, Fixed Channels Supported] ............................................................ 146 4.11.10 Extended Window Size Configuration (EWC) ..................................................................................... 147 L2CAP/EWC/BV-01-C [IUT Initiated Extended Window Size Option] ................................................................. 147 L2CAP/EWC/BV-02-C [Lower Tester Requests Extended Window Size] ........................................................... 148 L2CAP/EWC/BV-03-C [Extended Window Size Option Not Supported by Lower Tester] ................................... 149 4.11.11 Lock Step Configuration (LSC) ........................................................................................................... 150 L2CAP/LSC/BV-01-C [Normal Lock Step Configuration Process for Best Effort, BR/EDR ERTM Channel].............................................................................................................................................................. 150 L2CAP/LSC/BV-02-C [Normal Lock Step Configuration Process for Guaranteed, BR/EDR ERTM Channel].............................................................................................................................................................. 151 L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel] .................... 153 L2CAP/LSC/BI-04-C [Mismatched Service Type, Best Effort, BR/EDR ERTM Channel] .................................... 154 L2CAP/LSC/BI-05-C [Mismatched Service Type, Guaranteed, BR/EDR ERTM Channel] ................................. 155 L2CAP/LSC/BV-06-C [Remote Failed on Guaranteed, BR/EDR ERTM Channel] .............................................. 156 L2CAP/LSC/BV-07-C [Normal Lock Step Configuration Process for Best Effort, AMP Channel]........................ 157 L2CAP/LSC/BV-08-C [Normal Lock Step Configuration Process for Guaranteed, AMP Channel] ..................... 158 L2CAP/LSC/BV-09-C [Premature Success in Configuration Response, AMP Channel] ..................................... 159 L2CAP/LSC/BI-10-C [Mismatched Service Type, Best Effort, AMP Channel]..................................................... 160 L2CAP/LSC/BI-11-C [Mismatched Service Type, Guaranteed, AMP Channel] .................................................. 161 L2CAP/LSC/BV-12-C [Remote Failed on Guaranteed, AMP Channel] ............................................................... 162 4.11.12 Create Channel (CCH) ........................................................................................................................ 163 L2CAP/CCH/BV-01-C [Create Channel Request for an AMP Physical Link] ...................................................... 163 L2CAP/CCH/BV-02-C [Create Channel Request for an AMP Physical Link – Refused] ..................................... 164 L2CAP/CCH/BV-03-C [Create Channel Request for an AMP Physical Link – Failed] ........................................ 165 L2CAP/CCH/BV-04-C [Create Channel Response for an AMP Physical Link] ................................................... 166 4.11.13 Move Channel (MCH) ......................................................................................................................... 167 L2CAP/MCH/BV-01-C [Move ERTM Channel Request for BR/EDR to AMP – Success] ................................... 167 L2CAP/MCH/BV-02-C [Move ERTM Channel Request for BR/EDR to AMP – Refused] .................................... 169 L2CAP/MCH/BV-03-C [Move ERTM Channel Request for BR/EDR to AMP – AMP Fail] .................................. 170 L2CAP/MCH/BV-04-C [Move ERTM Channel Request for AMP to BR/EDR – Success] ................................... 171 L2CAP/MCH/BV-05-C [Move ERTM Channel Request for AMP to BR/EDR – Refused] .................................... 173 L2CAP/MCH/BV-06-C [Move ERTM Channel Response for BR/EDR to AMP – Success] ................................. 174 L2CAP/MCH/BV-07-C [Move ERTM Channel Response for BR/EDR to AMP – Failure] ................................... 175 L2CAP/MCH/BV-08-C [Move ERTM Channel Response for AMP to BR/EDR – Success] ................................. 176 L2CAP/MCH/BV-09-C [Move ERTM Channel Response for AMP to BR/EDR – Failure] ................................... 177 L2CAP/MCH/BV-10-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP] ............................. 179 L2CAP/MCH/BV-11-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP – Unacknowledged Data] ....................................................................................................................................... 180 L2CAP/MCH/BV-12-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR] ............................. 181 L2CAP/MCH/BV-13-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR – Unacknowledged Data] ....................................................................................................................................... 183 L2CAP/MCH/BV-14-C [Move Collision – ERTM] ................................................................................................ 185 L2CAP/MCH/BV-15-C [Move Channel Request for BR/EDR to AMP (STM Source) – Success] ....................... 187 L2CAP/MCH/BV-16-C [Move Channel Request for BR/EDR to AMP (STM Sink) – Success] ............................ 188 L2CAP/MCH/BV-17-C [Move Channel Request for BR/EDR to AMP (STM Source) – Refused] ........................ 190 L2CAP/MCH/BV-18-C [Move Channel Request for BR/EDR to AMP (STM Sink) – Refused] ............................ 191 L2CAP/MCH/BV-19-C [Move Channel Request for BR/EDR to AMP (STM Source) – AMP Fail] ...................... 192 L2CAP/MCH/BV-20-C [Move Channel Request for BR/EDR to AMP (STM Sink) – AMP Failed] ....................... 193 L2CAP/MCH/BV-21-C [Move Channel Request for AMP to BR/EDR (STM Source) – Success] ....................... 195 L2CAP/MCH/BV-22-C [Move Channel Request for AMP to BR/EDR (STM Sink) – Success] ............................ 196 L2CAP/MCH/BV-23-C [Move Channel Request for AMP to BR/EDR (STM Source) – Refused]........................ 197 L2CAP/MCH/BV-24-C [Move Channel Request for AMP to BR/EDR (STM Sink) – Refused] ............................ 199 L2CAP/MCH/BV-25-C [Move Channel Request for AMP to BR/EDR (STM Source) – AMP Fail] ...................... 200 L2CAP/MCH/BV-26-C [Move Channel Request for AMP to BR/EDR (STM Sink) – AMP Failed] ....................... 201 L2CAP/MCH/BV-27-C [Move Channel Response for BR/EDR to AMP (STM Source) – Success] ..................... 202

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **7 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|L2CAP/MCH/BV-28-C [Move Channel Response for BR/EDR to AMP (STM Sink) – Success] ......................... 204|
|---|
|L2CAP/MCH/BV-29-C [Move Channel Response for AMP to BR/EDR (STM Source) – Success] ..................... 205|
|L2CAP/MCH/BV-30-C [Move Channel Response for AMP to BR/EDR (STM Sink) – Success] ......................... 207|
|L2CAP/MCH/BV-31-C [Move Channel Response for BR/EDR to AMP (STM Source) – Failed] ........................ 208|
|L2CAP/MCH/BV-32-C [Move Channel Response for BR/EDR to AMP (STM Sink) – Failed] ............................. 209|
|L2CAP/MCH/BV-33-C [Move Channel Response for AMP to BR/EDR (STM Source) – Failed] ........................ 210|
|L2CAP/MCH/BV-34-C [Move Channel Response for AMP to BR/EDR (STM Sink) – Failed] ............................. 212|
|L2CAP/MCH/BV-35-C [Move Collision – STM Source] ....................................................................................... 214|
|L2CAP/MCH/BV-36-C [Move Collision – STM Sink] ........................................................................................... 216|
|4.11.14 Enhanced Retransmission Mode with Extended Control Field (ECF) ................................................. 218|
|L2CAP/ECF/BV-01-C [Receive I-Frames with Extended Control Field] .............................................................. 218|
|L2CAP/ECF/BV-02-C [Transmit I-Frames with Extended Control Field] ............................................................. 219|
|L2CAP/ECF/BV-03-C [Acknowledging Received I-Frames with Extended Control Field] ................................... 220|
|L2CAP/ECF/BV-04-C [Send S-Frame [RR] with Extended Control Field and Poll Bit Set] ................................. 221|
|L2CAP/ECF/BV-05-C [Respond to S-Frame [REJ] with Extended Control Field] ............................................... 222|
|L2CAP/ECF/BV-06-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL bit Set] ................. 223|
|L2CAP/ECF/BV-07-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL Bit Clear] ............. 224|
|L2CAP/ECF/BV-08-C [Transmit I-Frames using Extended Control Field and SAR] ........................................... 225|
|4.11.15 Streaming Mode with Extended Control Field (STM) .......................................................................... 227|
|L2CAP/STM/BV-11-C [Streaming Mode Source with Extended Control Field] ................................................... 227|
|L2CAP/STM/BV-12-C [Streaming Mode Sink with Extended Control Field]........................................................ 228|
|L2CAP/STM/BV-13-C [Streaming Mode Source using Extended Control Field and SAR] .................................. 228|
|4.12 Low Energy System tests ......................................................................................................... 229|
|4.12.1<br>Connection Parameter Update ........................................................................................................... 229|
|L2CAP/LE/CPU/BV-01-C [Send Connection Parameter Update Request] ......................................................... 229|
|L2CAP/LE/CPU/BV-02-C [Accept Connection Parameter Update Request] ...................................................... 230|
|L2CAP/LE/CPU/BI-01-C [Reject Connection Parameter Update Parameters].................................................... 231|
|L2CAP/LE/CPU/BI-02-C [Reject Connection Parameter Update Request] ......................................................... 232|
|4.12.2<br>Command Reject ................................................................................................................................ 233|
|L2CAP/COS/CED/BI-01-C [Reject Unknown Command, BR/EDR] .................................................................... 234|
|L2CAP/LE/REJ/BI-02-C [Reject Unknown Command – LE] ............................................................................... 234|
|4.13 Connectionless Basic L2CAP Mode ......................................................................................... 235|
|4.13.1<br>Connectionless Reception Channel CLR ............................................................................................ 235|
|L2CAP/CLS/CLR/BV-01-C [Data Over Connectionless Channel] ....................................................................... 235|
|L2CAP/CLS/UCD/BV-01-C [Data Reception over Unicast Connectionless Channel] ......................................... 236|
|L2CAP/CLS/UCD/BV-02-C [Unencrypted data transmission over unicast connectionless channel] ................... 236|
|L2CAP/CLS/UCD/BV-03-C [Encrypted Data Transmission over Unicast Connectionless Channel] ................... 237|
|4.14 Channel Identifiers (CID) .......................................................................................................... 238|
|L2CAP/LE/CID/BV-01-C [Receiving DCID over BR/EDR and LE] ...................................................................... 238|
|L2CAP/LE/CID/BV-02-C [Receiving SCID over BR/EDR and LE] ...................................................................... 239|
|L2CAP/LE/CID/BV-03-C [Receiving same DCID over BR/EDR and LE] ............................................................ 240|
|L2CAP/LE/CID/BV-04-C [Receiving same SCID over BR/EDR and LE] ............................................................. 241|
|4.14.1<br>Ignore Unsupported CIDs ................................................................................................................... 241|
|L2CAP/COS/CID/BI-01-C [Ignore Unsupported CIDs, ACL] ............................................................................... 242|
|L2CAP/LE/CID/BI-01-C [Ignore Unsupported CIDs, LE] ..................................................................................... 242|
|L2CAP/CLS/CID/BV-01-C [Ignore Unsupported CIDs, APB] .............................................................................. 242|
|4.15 Credit Based Flow Control Mode .............................................................................................. 244|
|4.15.1<br>Enhanced Credit Based Flow Control Mode ....................................................................................... 244|
|L2CAP/ECFC/BV-01-C [L2CAP Credit Based Connection Request – Legacy Peer, LE] ................................... 245|
|L2CAP/ECFC/BV-45-C [L2CAP Credit Based Connection Request – Legacy Peer, BR/EDR] .......................... 245|
|L2CAP/ECFC/BV-02-C [L2CAP Credit Based Connection Request on Supported PSM, LE] ............................ 246|
|L2CAP/ECFC/BV-46-C [L2CAP Credit Based Connection Request on Supported PSM, BR/EDR] ................... 246|
|L2CAP/ECFC/BV-03-C [L2CAP Credit Based Connection Response on Supported PSM, LE] ......................... 247|
|L2CAP/ECFC/BV-47-C [L2CAP Credit Based Connection Response on Supported PSM, BR/EDR] ................ 247|
|L2CAP/ECFC/BV-04-C [L2CAP Credit Based Connection Request on an Unsupported PSM, LE] ................... 248|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **8 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

L2CAP/ECFC/BV-48-C [L2CAP Credit Based Connection Request on an Unsupported PSM, BR/EDR] .......... 248 L2CAP/ECFC/BV-06-C [Credit Exchange – Receiving Incremental Credits, LE] ................................................ 249 L2CAP/ECFC/BV-49-C [Credit Exchange – Receiving Incremental Credits, BR/EDR] ....................................... 249 L2CAP/ECFC/BV-07-C [Credit Exchange – Sending Credits, LE] ...................................................................... 251 L2CAP/ECFC/BV-50-C [Credit Exchange – Sending Credits, BR/EDR] ............................................................. 251 L2CAP/ECFC/BI-01-C [Credit Exchange – Zero Credits and Exceed Maximum Credits, LE] ............................ 252 L2CAP/ECFC/BI-10-C [Credit Exchange – Zero Credits and Exceed Maximum Credits, BR/EDR] ................... 252 L2CAP/ECFC/BI-02-C [Credit Exchange – No Credits, LE] ................................................................................ 253 L2CAP/ECFC/BI-11-C [Credit Exchange – No Credits, BR/EDR] ....................................................................... 253 L2CAP/ECFC/BV-11-C [Security – Insufficient Authentication – Responder, LE] ............................................... 255 L2CAP/ECFC/BV-14-C [Security – Insufficient Encryption Key Size – Initiator, LE] ........................................... 256 L2CAP/ECFC/BV-52-C [Security – Insufficient Encryption Key Size – Initiator, BR/EDR] .................................. 256 L2CAP/ECFC/BV-17-C [L2CAP Credit Based Connection Response – refused due to insufficient resources, LE] ..................................................................................................................................................... 257 L2CAP/ECFC/BV-53-C [L2CAP Credit Based Connection Response – refused due to insufficient resources, BR/EDR] ............................................................................................................................................ 257 L2CAP/ECFC/BV-18-C [L2CAP Credit Based Connection Request – refused due to Invalid Source CID, LE] ...................................................................................................................................................................... 258 L2CAP/ECFC/BV-54-C [L2CAP Credit Based Connection Request – refused due to Invalid Source CID, BR/EDR] ............................................................................................................................................................. 258 L2CAP/ECFC/BV-19-C [L2CAP Credit Based Connection Request – refused due to Source CID already allocated, LE] ...................................................................................................................................................... 260 L2CAP/ECFC/BV-55-C [L2CAP Credit Based Connection Request – refused due to Source CID already allocated, BR/EDR] ............................................................................................................................................. 260 L2CAP/ECFC/BV-20-C [L2CAP Credit Based Connection Response – refused due to Source CID already allocated, LE] ......................................................................................................................................... 261 L2CAP/ECFC/BV-56-C [L2CAP Credit Based Connection Response – refused due to Source CID already allocated, BR/EDR] ................................................................................................................................ 261 L2CAP/ECFC/BV-21-C [L2CAP Credit Based Connection Request – refused due to Unacceptable Parameters, LE] .................................................................................................................................................. 262 L2CAP/ECFC/BV-57-C [L2CAP Credit Based Connection Request – refused due to Unacceptable Parameters, BR/EDR] ......................................................................................................................................... 262 L2CAP/ECFC/BV-22-C [Renegotiate MTU – Initiator, LE] .................................................................................. 264 L2CAP/ECFC/BV-58-C [Renegotiate MTU – Initiator, BR/EDR] ......................................................................... 264 L2CAP/ECFC/BV-23-C [Renegotiate MTU – Responder, LE] ............................................................................ 265 L2CAP/ECFC/BV-59-C [Renegotiate MTU – Responder, BR/EDR] ................................................................... 265 L2CAP/ECFC/BI-03-C [Renegotiate MTU – MTU value is decreased, LE] ......................................................... 267 L2CAP/ECFC/BI-12-C [Renegotiate MTU – MTU value is decreased, BR/EDR] ................................................ 267 L2CAP/ECFC/BV-24-C [Renegotiate MPS – Initiator, LE] .................................................................................. 268 L2CAP/ECFC/BV-60-C [Renegotiate MPS – Initiator, BR/EDR] ......................................................................... 268 L2CAP/ECFC/BV-25-C [Renegotiate MPS – Responder, LE] ............................................................................ 271 L2CAP/ECFC/BV-61-C [Renegotiate MPS – Responder, BR/EDR] ................................................................... 271 L2CAP/ECFC/BI-04-C [Renegotiate MPS – MPS value is decreased, LE] ......................................................... 273 L2CAP/ECFC/BI-13-C [Renegotiate MPS – MPS value is decreased, BR/EDR] ................................................ 273 L2CAP/ECFC/BV-26-C [L2CAP Credit Based Connection Response – refused due to Invalid Parameters, LE] .................................................................................................................................................. 274 L2CAP/ECFC/BV-62-C [L2CAP Credit Based Connection Response – refused due to Invalid Parameters, BR/EDR] ......................................................................................................................................... 274 L2CAP/ECFC/BV-27-C [L2CAP Credit Based Connection Response – refused due to Unacceptable Parameters, LE] .................................................................................................................................................. 275 L2CAP/ECFC/BV-63-C [L2CAP Credit Based Connection Response – refused due to Unacceptable Parameters, BR/EDR] ......................................................................................................................................... 275 L2CAP/ECFC/BI-05-C [Reconfigure – refused due to invalid Destination CID, LE] ............................................ 276 L2CAP/ECFC/BI-14-C [Reconfigure – refused due to invalid Destination CID, BR/EDR] ................................... 276 L2CAP/ECFC/BI-06-C [Reconfigure – other unacceptable parameters, LE] ...................................................... 277 L2CAP/ECFC/BI-15-C [Reconfigure – other unacceptable parameters, BR/EDR] ............................................. 277

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **9 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|L2CAP/ECFC/BV-29-C [L2CAP Credit Based Connection Response – Duplicate DCID, LE] ............................ 278|
|---|
|L2CAP/ECFC/BV-64-C [L2CAP Credit Based Connection Response – Duplicate DCID, BR/EDR] ................... 278|
|L2CAP/ECFC/BI-07-C [L2CAP Credit Based Connection Response – Duplicate DCID, LE] ............................. 280|
|L2CAP/ECFC/BI-16-C [L2CAP Credit Based Connection Response – Duplicate DCID, BR/EDR] .................... 280|
|4.15.2<br>LE Credit Based Flow Control Mode ................................................................................................... 280|
|L2CAP/LE/CFC/BV-01-C [LE Credit Based Connection Request - Legacy Peer] ............................................... 280|
|L2CAP/LE/CFC/BV-02-C [LE Credit Based Connection Request on Supported SPSM] .................................... 281|
|L2CAP/LE/CFC/BV-03-C [LE Credit Based Connection Response on Supported SPSM] ................................. 282|
|L2CAP/LE/CFC/BV-04-C [LE Credit Based Connection Request on an unsupported SPSM] ............................ 283|
|L2CAP/LE/CFC/BV-05-C [LE Credit Based Connection Request - unsupported SPSM] .................................... 284|
|L2CAP/LE/CFC/BV-06-C [Credit Exchange – Receiving Incremental Credits] ................................................... 285|
|L2CAP/LE/CFC/BV-07-C [Credit Exchange – Sending Credits] ......................................................................... 287|
|L2CAP/LE/CFC/BI-01-C [Credit Exchange – Exceed Initial Credits] ................................................................... 288|
|L2CAP/LE/CFC/BV-11-C [Security - Insufficient Authentication – Responder] ................................................... 289|
|L2CAP/LE/CFC/BV-14-C [Security - Insufficient Encryption Key Size – Initiator] ............................................... 289|
|L2CAP/LE/CFC/BV-17-C [LE Credit Based Connection Response - refused due to insufficient|
|resources - Responder] ...................................................................................................................................... 290|
|L2CAP/LE/CFC/BV-18-C [LE Credit Based Connection Request - refused due to Invalid Source CID -|
|Initiator] ............................................................................................................................................................... 291|
|L2CAP/LE/CFC/BV-19-C [LE Credit Based Connection Request - refused due to source CID already|
|allocated - Initiator] .............................................................................................................................................. 292|
|L2CAP/LE/CFC/BV-20-C [LE Credit Based Connection Response - refused due to Source CID already|
|allocated - Responder] ........................................................................................................................................ 293|
|L2CAP/LE/CFC/BV-21-C [LE Credit Based Connection Request - refused due to Unacceptable|
|Parameters - Initiator] ......................................................................................................................................... 294|
|L2CAP/ECFC/BV-38-C [Credit Based Connection Request Dynamically Allocated Source CID – LE] .............. 296|
|L2CAP/LE/CFC/BV-29-C [Credit Based Connection Request Dynamically Allocated Source CID] .................... 296|
|L2CAP/ECFC/BV-79-C [Credit Based Connection Request Dynamically Allocated Source CID –|
|BR/EDR] ............................................................................................................................................................. 296|
|4.15.3<br>All Credit Based Flow Control Mode ................................................................................................... 297|
|L2CAP/LE/CFC/BV-08-C [Disconnection Request] ............................................................................................ 298|
|L2CAP/ECFC/BV-08-C [Disconnection Request, LE] ......................................................................................... 298|
|L2CAP/ECFC/BV-65-C [Disconnection Request, BR/EDR] ................................................................................ 298|
|L2CAP/LE/CFC/BV-09-C [Disconnection Response] .......................................................................................... 300|
|L2CAP/ECFC/BV-09-C [Disconnection Response, LE] ...................................................................................... 300|
|L2CAP/ECFC/BV-66-C [Disconnection Response, BR/EDR] ............................................................................. 300|
|L2CAP/LE/CFC/BV-10-C [Security – Insufficient Authentication – Initiator] ........................................................ 302|
|L2CAP/ECFC/BV-10-C [Security – Insufficient Authentication – Initiator, LE] .................................................... 302|
|L2CAP/ECFC/BV-67-C [Security – Insufficient Authentication – Initiator, BR/EDR] ........................................... 302|
|L2CAP/LE/CFC/BV-12-C [Security – Insufficient Authorization – Initiator] .......................................................... 304|
|L2CAP/ECFC/BV-12-C [Security – Insufficient Authorization – Initiator, LE] ...................................................... 304|
|L2CAP/ECFC/BV-68-C [Security – Insufficient Authorization – Initiator, BR/EDR] ............................................. 304|
|L2CAP/LE/CFC/BV-13-C [Security – Insufficient Authorization – Responder] .................................................... 306|
|L2CAP/ECFC/BV-13-C [Security – Insufficient Authorization – Responder, LE] ................................................. 306|
|L2CAP/LE/CFC/BV-15-C [Security – Insufficient Encryption Key Size – Responder] ......................................... 308|
|L2CAP/ECFC/BV-15-C [Security – Insufficient Encryption Key Size – Responder, LE] ..................................... 308|
|L2CAP/ECFC/BV-70-C [Security – Insufficient Encryption Key Size – Responder, BR/EDR] ............................ 308|
|L2CAP/LE/CFC/BV-16-C [L2CAP LE Credit Based Connection Request – refused due to insufficient|
|resources] ........................................................................................................................................................... 311|
|L2CAP/ECFC/BV-16-C [L2CAP Credit Based Connection Request – refused due to insufficient|
|resources, LE] ..................................................................................................................................................... 311|
|L2CAP/ECFC/BV-71-C [L2CAP Credit Based Connection Request – refused due to insufficient|
|resources, BR/EDR] ............................................................................................................................................ 311|
|L2CAP/LE/CFC/BV-22-C [L2CAP LE Credit Based Connection Response on Unsupported SPSM] ................. 313|
|L2CAP/ECFC/BV-28-C [L2CAP Credit Based Connection Response on Unsupported SPSM, LE] ................... 313|
|L2CAP/ECFC/BV-72-C [L2CAP Credit Based Connection Response on Unsupported SPSM, BR/EDR] .......... 313|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **10 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

||L2CAP/LE/CFC/BV-23-C [Disconnect Request – DCID not recognized] ............................................................ 315|
||L2CAP/ECFC/BV-30-C [Disconnection Response, LE] ...................................................................................... 315|
||L2CAP/ECFC/BV-73-C [Disconnection Response, BR/EDR] ............................................................................. 315|
||L2CAP/LE/CFC/BV-24-C [Security – Insufficient Encryption – Initiator] .............................................................. 317|
||L2CAP/ECFC/BV-31-C [Security – Insufficient Encryption – Initiator, LE] .......................................................... 317|
||L2CAP/LE/CFC/BV-25-C [Security – Insufficient Encryption – Responder] ........................................................ 319|
||L2CAP/ECFC/BV-32-C [Security – Insufficient Encryption – Responder, LE] .................................................... 319|
||L2CAP/LE/CFC/BV-26-C [K-frame – SDU length greater than MTU of IUT] ...................................................... 321|
||L2CAP/ECFC/BV-33-C [K-frame – SDU length greater than MTU of IUT, LE] ................................................... 321|
||L2CAP/ECFC/BV-76-C [K-frame – SDU length greater than MTU of IUT, BR/EDR] .......................................... 321|
||L2CAP/LE/CFC/BV-27-C [K-frame – Information Payload length greater than MPS of IUT] .............................. 323|
||L2CAP/ECFC/BV-34-C [K-frame – Information Payload length greater than MPS of IUT, LE] ........................... 323|
||L2CAP/ECFC/BV-77-C [K-frame – Information Payload length greater than MPS of IUT, BR/EDR] .................. 323|
||L2CAP/LE/CFC/BV-28-C [Total length of segments greater than SDU length specified in first K-frame] ........... 325|
||L2CAP/ECFC/BV-35-C [Total length of segments greater than SDU length specified in first K-frame, LE] ........ 325|
||L2CAP/ECFC/BV-78-C [Total length of segments greater than SDU length specified in first K-frame,|
||BR/EDR] ............................................................................................................................................................. 325|
||L2CAP/LE/CFC/BV-32-C [K-frame – SDU length = MPS] .................................................................................. 327|
||L2CAP/ECFC/BV-80-C [K-frame – SDU length = MPS, LE] ............................................................................... 327|
||L2CAP/ECFC/BV-81-C [K-frame – SDU length = MPS, BR/EDR] ...................................................................... 327|
||4.16 Generic Attribute Timing tests .................................................................................................. 329|
||4.16.1<br>Back-off on Connection Request Collision .......................................................................................... 329|
||L2CAP/TIM/BV-01-C [Back-off on Connection Request Collision, BR/EDR, Dynamic] ...................................... 330|
||L2CAP/TIM/BV-02-C [Back-off on Connection Request Collision, BR/EDR, EATT] ........................................... 330|
||L2CAP/TIM/BV-03-C [Back-off on Connection Request Collision, LE, EATT] .................................................... 330|
|**5**|**Test case mapping ........................................................................................................................... 333**|
|**6**|**Revision history and acknowledgments ........................................................................................ 344**|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **11 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **1 Sco e p**

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Logical Link Control and Adaptation Protocol (L2CAP) layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers’ Bluetooth devices.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **12 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **2 References, definitions, and abbreviations**

## **2.1 References**

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereafter. Additional definitions and abbreviations can be found in [9] and [10].

- [1] Specification of the Bluetooth System, Version 1.2 or later, Volume 3, Part A

- [2] ISO/IEC 9646-1 "Conformance Testing Methodology and Framework"

- [3] Core IXIT Proforma for Bluetooth Conformance Test Suites

- [4] Specification of the Bluetooth System, Version 2.0 / 2.0+EDR / 2.1 / 2.1+EDR

- [5] ICS Proforma for Logical Link Control and Adaption Protocol (L2CAP)

- [6] ITU-T Recommendation Z.120, Message Sequence Chart (MSC)

- [7] Core Specification Addendum 1 (CSA1)

- [8] Specification of the Bluetooth System, Version 3.0 +HS or later, Volume 3, Part A

- [9] Specification of the Bluetooth System, Volume 2, Part C

- [10] Volume 1, Part A, Test Strategy and Terminology Overview

- [11] Specification of the Bluetooth System, Version 4.0 or later, Volume 3, Part A (L2CAP)

- [12] Specification of the Bluetooth System, Version 4.1 or later, Volume 3, Part A (L2CAP)

- [13] Specification of the Bluetooth System, Volume 3, Part A (Logical Link Control and Adaptation Protocol Specification), Version 5.2 or later

- [14] Specification of the Bluetooth System, Volume 3, Part G (Generic Attribute Profile Specification), Version 5.2 or later

- [15] Specification of the Bluetooth System, Volume 3, Part A (Logical Link Control and Adaptation Protocol Specification), Version 5.3 or later

- [16] Security Manager Test Suite, SM.TS

- [17] Link Manager Protocol Test Suite, LMP.TS

- [18] Appropriate Language Mapping Tables document

## **2.2 Definitions**

In this Bluetooth document, the definitions from [9] and [10] apply.

Certain terms that were identified as inappropriate have been replaced. For a list of the original terms and their replacement terms, see the Appropriate Language Mapping Tables document [18].

## **2.3 Acronyms and abbreviations**

In this Bluetooth document, the definitions, acronyms, and abbreviations from [9] and [10] apply.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **13 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **3 Test Suite Structure (TSS)**

## **3.1 Test Strategy**

The test objectives are to verify the functionality of the L2CAP layer within a Bluetooth Host and enable interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory and optional requirements in the specification and matches these to the support of the IUT as described in the ICS. At the same time, unless specifically prohibited by a test procedure, it is acceptable for IUTs to send redundant PDUs not described by the test procedure. When observed, such PDUs do not result in a test case failure. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test Case Mapping Table (TCMT) evaluates to true.

The test equipment provides an implementation of the Radio Controller and the parts of the Host needed to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT’s peer device and interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement similar capabilities to communicate with the test equipment. For some test cases, it is necessary to stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface, a Man Machine Interface (MMI), or another interface supported by the IUT.

This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with catalogued specification requirements that were logically grouped and assessed for testability enabling coverage in defined test purposes.

The L2CAP layer specifies three groups of services:

- CONNECTION ORIENTED basic L2CAP mode

- CONNECTION ORIENTED retransmission/flow control/streaming modes

- CONNECTIONLESS basic L2CAP mode

The Test Suite Structure is a tree with the first level defined as L2CAP representing the protocol services. From these services, the test groups and functional modules are derived.

## **3.2 Test groups**

Tests are defined in terms of a sequence of L2CAP and AMP Manager operations in the Implementation Under Test (IUT) and over-the-air interface operations.

The test groups are organized in three levels. The first level defines the protocol groups representing the protocol services. The second level separates the protocol services in functional modules. The last level in each branch contains the standard ISO subgroups BV and BI.

## **3.2.1 Protocol service groups**

The protocol groups identify the Bluetooth L2CAP Layer services Connection-Oriented Services and the Connectionless Service.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **14 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **3.2.1.1 Connection-Oriented Service – Basic L2CAP Mode**

With the functional modules:

- Basic operation data channel

- Configuration of data channel

- Implementation-specific information exchange

- Echo handling

- **3.2.1.2 Connection-Oriented Service – Retransmission/Flow Control/Streaming Modes**

- Flow control mode

- Retransmission mode

- Extended features

- Channel mode configuration

- Frame check sequence (FCS) option configuration

- Optional FCS

- Enhanced retransmission mode

- Streaming mode

- Extended features

- Fixed channel support

- Extended window size configuration

- Lock step configuration

- LE credit based flow control mode

- Enhanced credit based flow control mode

- Create channel

- Move channel

- Enhanced retransmission mode with extended control field

- Streaming mode with extended control field

## **3.2.1.3 Low Energy System tests**

- Connection parameter update

- Command reject

## **3.2.1.4 Connectionless Service**

- Connectionless reception channel

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **15 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **3.2.2 Main test groups**

## **3.2.2.1 Fixed Channel Support**

The Generic AMP defines a method to determine if a device supports fixed channels beyond the two currently defined. A fixed channel is present as soon as the ACL link is created. These fixed channels can be used for the AMP Manager protocol and other protocols in the future.

Refer to [8] Section 2.1 for a list of the characteristics of each fixed channel (e.g., reliability, MTU size, QoS). Table 2.1 in Section 2.1 lists the defined fixed channels and provides a reference to where the associated channel characteristics are defined.

## **3.2.2.2 AMP Manager Channel Support**

The AMP Manager protocol uses L2CAP fixed channel 3 for communication between individual device AMP Managers. These tests relate to the creation of AMP channels and moving data channels between AMPs and the BR/EDR controllers.

## **3.2.2.3 AMP Manager Protocol**

The AMP Manager provides information on available AMPs and their characteristics to other AMP capable Bluetooth devices. These tests relate to AMP Discovery, info exchange and change in available AMP status.

## **3.2.2.4 AMP Manager Physical Channel Interface**

The AMP Manager must be able to acquire AMP info from the local available AMPs. These tests relate to AMP Manager / AMP HCI / AMP PAL interface and control. The interface and exchange of information is defined in terms of AMP HCI command packets and events. Note that a specific instance of a Bluetooth stack and AMP PAL may not necessarily need to exchange an AMP HCI Packet if the interaction between the layers “acts” as if an AMP HCI packet was exchanged.

## **3.2.2.5 Low Energy Signaling Channel Support**

The Low Energy Signaling channel uses L2CAP fixed channel 5 for communication between Low energy capable devices.

## **3.2.3 Behavior testing groups**

## **3.2.3.1 Valid Behavior (BV) tests**

This sub group provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt or exchange of a valid Protocol Data Units (PDUs). Valid PDUs means that the exchange of messages and the content of the exchanged messages are considered as valid.

## **3.2.3.2 Invalid Behavior (BI) tests**

This sub group provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt of a syntactically or semantically invalid PDU.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **16 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4 Test cases (TC)**

## **4.1 Test case identification conventions**

Test cases are assigned unique identifiers per the conventions in [10]. The convention used here is: **<spec abbreviation>/<IUT role>/** <class>/ **<feat>** /<func>/<subfunc>/<cap>/ **<xx>-<nn>-<y>** .

|**Identifier Abbreviation**|**Spec Identifier <spec abbreviation>**|
|L2CAP|Logical Link Control and Adaptation Protocol|
|**Identifier Abbreviation**|**Function Identifier <func>**|
|CLS|Connectionless services|
|COS|Connection-oriented services|
|LE|Low Energysignalingchannel|
|**Identifier Abbreviation**|**Subfunction Identifier <subfunc>**|
|CCH|Create Channel|
|CED|Basic operation data channel|
|CFC|LE Credit Based Flow Control Mode|
|CFD|Configuration of data channel|
|CID|Channel Identifiers|
|CLR|Connectionless reception channel|
|CMC|Channel Mode configuration|
|CPU|Connection Parameter Update|
|ECF|Enhanced Retransmission Mode usingExtended Control Field|
|ECH|Echo handling|
|ERM|Use of Enhanced Retransmission Mode|
|EWC|Extended Window Size Configuration|
|EXF|Extended Features|
|FIX|Fixed Channel Support|
|FLC|Flow control mode|
|FOC|Optional FCS configuration|
|IEX|Implementation-specific information exchange|
|LSC|Lock StepConfiguration|
|MCH|Move Channel|
|OFS|Use of Optional FCS|
|REJ|Command reject|
|RTX|Retransmission mode|
|STM|StreamingMode|
|UCD|Unicast Connectionless Data|
|**Identifier Abbreviation**|**Class Identifier <class>**|
|TIM|Generic Attribute TimingTests|
|**Item**|**Support**|
|ECFC|Enhanced Credit Based Flow Control Mode|

_Table 4.1: L2CAP TC feature naming conventions_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **17 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.2 MSC abbreviations**

Table 4.2 provides the definitions of abbreviations used in the test case MSCs.

|**MSC Abbr**|**Use in**<br>**Frame**|**Description**|**Reference**|
|N(S)|I-Frame|Send sequence number. N(S) is equivalent to TxSeq<br>use in[1].|[1]3.3.2|
|SAR|I-Frame|I-Frame Segmentation And Reassembly indicator (i.e.,<br>Un-segmented SDU / Start, Continuation, End of<br>SDU)|[1]3.3.2|
|N(R)|I/S-Frame|Receive sequence number. N(R) is equivalent to<br>ReqSequse in[1].|[1]3.3.2|
|F|I/S-Frame|Final Bit|[1]3.3.2|
|P|S-Frame|Poll Bit|[1]3.3.2|
|RR|S-Frame|S-Frame SupervisoryFunction = Receiver Ready|[1]3.3.2|
|RNR|S-Frame|S-Frame SupervisoryFunction = Receiver Not Ready|[1]3.3.2|
|REJ|S-Frame|S-Frame SupervisoryFunction = Reject|[1]3.3.2|
|SREJ|S-Frame|S-Frame SupervisoryFunction = Selective Reject|[1]3.3.2|

_Table 4.2: MSC abbreviations_

## **4.3 Conformance**

When conformance is claimed for a particular specification, all capabilities are to be supported in the specified manner. The mandated tests from this Test Suite depend on the capabilities to which conformance is claimed.

The Bluetooth Qualification Program may employ tests to verify implementation robustness. The level of implementation robustness that is verified varies from one specification to another and may be revised for cause based on interoperability issues found in the market.

Such tests may verify:

- That claimed capabilities may be used in any order and any number of repetitions not excluded by the specification

- That capabilities enabled by the implementations are sustained over durations expected by the use case

- That the implementation gracefully handles any quantity of data expected by the use case

- That in cases where more than one valid interpretation of the specification exists, the implementation complies with at least one interpretation and gracefully handles other interpretations

- That the implementation is immune to attempted security exploits

A single execution of each of the required tests is required to constitute a Pass verdict. However, it is noted that to provide a foundation for interoperability, it is necessary that a qualified implementation consistently and repeatedly pass any of the applicable tests.

In any case, where a member finds an issue with the test plan generated by the Bluetooth SIG qualification tool, with the test case as described in the Test Suite, or with the test system utilized, the member is required to notify the responsible party via an erratum request such that the issue may be addressed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **18 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.4 Lower layer assumptions**

For conformance testing L2CAP and enhanced L2CAP layers it is necessary to have working lower layers in conformance with lower layer specifications.

For testing it is necessary to have an ACL link between the Lower Tester and IUT set up.

For connection-oriented operation no more than one ACL link exists between an IUT and the Lower Tester.

In the L2CAP test cases the IUT may act either as L2CAP initiator or as L2CAP acceptor. In each test case is defined which of these roles apply. The L2CAP initiator is assumed to be the Central of the piconet when executing these tests.

## **4.5 Upper Tester**

For some test cases, it is necesary to stimulate the IUT from an Upper Tester. In practice, this could be special test interface, an MMI, or other interface as supported by the IUT.

## **4.6 General information about MSC**

The reception of L2CAP_Config PDUs from the IUT by the Lower Tester is described in more detail in [6] Section 5.2. The MSC diagrams for each Test Case only reflect the case where these PDUs are not segmented by IUT. If segmentation occurs, the MSC diagrams for each Test Case can be seen as the final outcome of the configuration procedure.

## **4.7 Pass/Fail verdict conventions**

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met.

The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict.

## **4.8 Preamble IXITs**

The following IXIT items are defined to assist with general establishment of initial conditions. As such they are noted here rather than in specific tests.

|TSPX_iut_device_name_in_adv_packet_for_random_address|Device Name. IUT advertising this<br>local name for the Lower Tester to<br>make connection to.<br>The default is that this not using it with<br>emptystring.|
|TSPX_time_guard|The time in ms, for the Lower Tester<br>to wait for a specific event.|
|TSPX_security_enabled|Indicates if security is required, to<br>establish connections, bythe IUT.|
|TSPX_delete_ltk|Indicates whether to delete Long Term<br>Keyor not.|
|TSPX_delete_link_key|Determine whether the Lower Tester<br>has to delete the stored link key in the<br>beginningof each test case.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **19 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|TSPX_use_dynamic_pin|Determines whether a dynamic PIN<br>MMI edit box will be used for Dynamic<br>Lower Tester Pin.|
|TSPX_secure_simple_pairing_pass_key_confirmation|Determines whether manual<br>confirmation on generated key is<br>required duringsecure simplepairing.|

## _Table 4.3: Preamble IXITs_

## **4.9 Common Packet Contents**

## **4.9.1 Fields and Bits Reserved for Future Use**

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers.

## **4.10 Connection-Oriented Basic L2CAP mode**

Verify the correct implementation of the connection-oriented services of the L2CAP layer.

## **4.10.1 Basic Operation Data Channel CED**

Verify the basic procedures for connection establishment of a data channel. That describes the setup phases, the data exchange and the release.

## **L2CAP/COS/CED/BV-01-C [Request Connection]**

- Test Purpose

Verify that the IUT can request the connection establishment for an L2CAP data channel and initiate the configuration procedure.

- Reference

[1] Table 2.1, Table 6.1, 2.2, 4.2, 4.3

- Initial Condition

- The IUT is in CLOSED state for data channel. No ACL link is established.

- It must be possible to send a connection request from the Upper Tester to create a L2CAP channel.

- Test Procedure

ACL link establishment is part of the test case. The Lower Tester imposes 48 byte MTU for both configuration directions.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **20 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**==> picture [372 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upp er Tester<br>Connect Request<br>ACL link establishment from IUT.<br>L2CAP_CONNECTION_REQ<br>(ID, length, PSM, SCID)<br>(ID, length, DCID, SCID, result, status)<br>L2CAP_ConfigReq<br>(ID, length, DCID, flags, IUT, options)<br>**----- End of picture text -----**<br>

_Figure 4.1: L2CAP/COS/CED/BV-01-C [Request Connection] MSC_

- Test Condition

The Lower Tester utilizes version L2CAP Basic Mode.

The Lower Tester’s Bluetooth device address BD_ADDR is defined. For parameters to send and receive, see [5].

The IUT acts as L2CAP initiator.

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_CONNECTION_REQ over the signaling channel and dynamically allocates an SCID.

The IUT initiates the configuration process as indicated by the generation of an L2CAP_ConfigReq.

The IUT accepts configuration of the MTU=48 bytes.

## **L2CAP/COS/CED/BV-03-C [Send Data]**

- Test Purpose

Verify that the IUT can send DATA.

- Reference

- [1] Table 6.1, Section 4

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in the OPEN state for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **21 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [368 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state for channel with CID.<br>Cause data to be sent<br>Use destination channel end<br>L2CAP_Data point DCID.<br>(length, DCID, data)<br>**----- End of picture text -----**<br>

_Figure 4.2: L2CAP/COS/CED/BV-03-C [Send Data] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_Data over the assigned channel with correct DCID assigned by the Lower Tester.

## **L2CAP/COS/CED/BV-04-C [Disconnect]**

- Test Purpose

Verify that the IUT can disconnect the data channel.

- Reference

- [1] Table 2.2, Table 6.1, 2.2, 4, 4.6

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in the OPEN state for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

**==> picture [373 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN state for channel with CID.<br>Cause L2CAP disconnect<br>L2CAP_DisconnectReq<br>(ID, length, DCID, SCID)<br>L2CAP_DisconnectRsp<br>(ID, length, DCID, SCID)<br>**----- End of picture text -----**<br>

_Figure 4.3: L2CAP/COS/CED/BV-04-C [Disconnect] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **22 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT transmits a correct L2CAP_DisconnectReq.

## **L2CAP/COS/CED/BV-07-C [Accept Disconnect]**

- Test Purpose

Verify that the IUT can respond to the request to disconnect the data channel.

- Reference

- [1] Table 2.2, Table 6.1, 2.2, 4, 4.4, 4.5

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in OPEN state for a data channel with assigned CID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

**==> picture [376 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN state for channel with CID.<br>L2CAP_DisconnectReq<br>(ID, length, DCID, SCID)<br>L2CAP_DisconnectRsp<br>RTX_TIMER<br>(ID, length, DCID, SCID)<br>**----- End of picture text -----**<br>

_Figure 4.4: L2CAP/COS/CED/BV-07-C [Accept Disconnect] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP_DisconnectRsp before the RTX timer expires.

-

- Notes

The Lower Tester’s RTX timer is set to TSPX_timer_rtx_max.

## **L2CAP/COS/CED/BV-08-C [Disconnect on Timeout]**

- Test Purpose

Verify that the IUT disconnects the data channel and shuts down this channel if no response occurs.

- Reference

- [1] 4.6, 4.7, 6.2.1

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **23 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in WAIT CONFIG state for a data channel with assigned CID.

- The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

**==> picture [299 x 337] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>IUT Is in WAIT_CONFIG state for channel with CID<br>L2CAP_ConfigReq Wait(RTX_TIME)RTX_TIMER:<br>L2CAP_ConfigReq Wait(2*RTX_TIME)RTX_TIMER: NOTE: IUT might<br>not retransmit<br>L2CAP_ConfigReq Wait(4*RTX_TIME)RTX_TIMER: L2CAP_ConfigReq<br>L2CAP_ConfigReq Wait(8*RTX_TIME)RTX_TIMER:<br>OPTIONAL – depends on ICS<br>RTX_TIMER:<br>L2CAP_DisconnectReq Wait(RTX_TIME)<br>L2CAP_DisconnectReq Wait(2*RTX_TIME)RTX_TIMER:<br>NOTE: IUT might<br>L2CAP_DisconnectReq Wait(4*RTX_TIME)RTX_TIMER: not retransmit<br>L2CAP_DIsconnectReq<br>RTX_TIMER:<br>L2CAP_DisconnectReq Wait(8*RTX_TIME)<br>Wait 65s from receipt of 1st<br>L2CAP_ConfigReq or 5s from<br>receipt of last<br>L2CAP_DisconnectReq<br>L2CAP_ConfigReq<br>5 sec L2CAP_Reject<br>(Reason = 0x0002)<br>**----- End of picture text -----**<br>

_Figure 4.5: L2CAP/COS/CED/BV-08-C [Disconnect on Timeout] MSC_

The Lower Tester transmits L2CAP_ConfigReq 5 seconds after receiving the last L2CAP_DisconnectReq or 65 seconds after receiving the first L2CAP ConfigReq.

The IUT sends an L2CAP_Reject with reason 0x0002 “Invalid CID in request” in response to the L2CAP_ConfigReq received.

The supplier may be required to state the number of L2CAP_DisconnectReq retransmissions that the IUT performs.

Following the expiration of TSPX_timer_rtx, it is possible that the IUT terminates the ACL – in this case the test stops.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **24 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP_ConfigReq to the Lower Tester.

If the IUT retransmits the L2CAP_ConfigReq more than once, each subsequent delay is at least twice the previous delay, and the identifier used for the original transmission is also used for each retransmission.

If the IUT sends an L2CAP_DisconnectReq, it is correctly formatted.

If the IUT retransmits the L2CAP_DisconnectReq more than once, each subsequent delay is at least twice the previous delay, and the identifier used for the original transmission is also used for each retransmission.

The IUT may terminate the ACL at the expiration of the RTX timer.

If the IUT does not terminate the ACL:

- The IUT does not transmit an L2CAP_ConfigRsp to the Lower Tester within 5 seconds of the L2CAP_ConfigReq sent by the Lower Tester.

- The IUT sends an L2CAP_Reject with reason 0x0002 “Invalid CID in request” in response to the L2CAP_ConfigReq received.

## **L2CAP/COS/CED/BV-09-C [Receive Multi-Command Packet]**

- Test Purpose

Verify that the IUT can receive more than one signaling command in one L2CAP packet.

- Reference

## 1 4

- Initial Condition

- Either the IUT initiated the connection or the Lower Tester initiated the connection and the IUT is in CONFIG state for a data channel with assigned CID. The IUT may act as either L2CAP initiator or L2CAP acceptor. Either the initiator or responder can send the first L2CAP_ConfigReq.

- Test Procedure

**==> picture [337 x 178] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, IUT options)<br>L2CAP_ConfigRsp, L2CAP_ConfigReq<br>(ID, length, SCID, Flags, result, options1, ID, length, DCID, Flags, options2)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, Flags, result, IUT options)<br>**----- End of picture text -----**<br>

_Figure 4.6: L2CAP/COS/CED/BV-09-C [Receive Multi-Command Packet] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **25 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

ALT1:

The IUT sends a correctly formatted L2CAP_ConfigReq to the Lower Tester, the first on the CID, and, having received an L2CAP_ConfigRsp and an L2CAP_ConfigReq in a single L2CAP packet from the Lower Tester, sends a correctly formatted L2CAP_ConfigRsp to the Lower Tester within 60s.

ALT2:

The IUT, having received the first L2CAP_ConfigReq from the Lower Tester and having sent a correctly formatted L2CAP_ConfigRsp to the Lower Tester, sends a correctly formatted L2CAP_ConfigReq to the Lower Tester and, upon reception of an L2CAP_ConfigRsp and an L2CAP_EchoReq in a single L2CAP packet from the Lower Tester, sends an L2CAP_EchoRsp to the Lower Tester within 60s.

## **L2CAP/COS/CED/BV-10-C [Transmit I-frames]**

- Test Purpose

Verify that IUT can transmit I-frames including correct CRC.

- Reference

- [1] 5.4, 7.4

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.

- Test Procedure

**==> picture [335 x 233] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Flow Control mode.<br>Command the IUT to send data<br>I frame<br>N(S)=0 N(R)=0<br>RetransmissionTimer of the IUT<br>I frame<br>N(S)=1 N(R)=0<br>I frame<br>N(S)=n-1 N(R)=0<br>RR frame<br>N(R)=n R=1<br>**----- End of picture text -----**<br>

_Figure 4.7: L2CAP/COS/CED/BV-10-C [Transmit I-frames] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **26 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT sends I-frames until TxWindow is full.

Data in the I-frames matches that provided by the Upper Tester. CRC value is set per the specification.

## **L2CAP/COS/CED/BV-11-C [Configure MTU Size]**

- Test Purpose

Verify that the IUT can configure the supported MTU size.

- Reference

[1] 5

- Initial Condition

- Maximum supported MTU size set in TSPX_l2ca_inmtu.

- The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

**==> picture [361 x 157] intentionally omitted <==**

_Figure 4.8: L2CAP/COS/CED/BV-11-C [Configure MTU Size] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP_ConfigRsp to the Lower Tester accepting the MTU.

The IUT sends a correct L2CAP_ConfigReq to the Lower Tester indicating maximum supported MTU.

## **L2CAP/COS/CED/BV-12-C [Recombination of Signaling Packets]**

- Test Purpose

Verify that the IUT correctly handles fragmented L2CAP signaling PDUs.

- Reference

- [1] 3.1, 4.2, 4.3, 7.2.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **27 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in CLOSED state. No ACL link is established. The IUT acts as L2CAP acceptor.

- Test Procedure

The IUT waits for all the fragments of each C-frame before interpreting the latter, i.e., until the received size of the C-frame equals the value of the PDU Length field of the C-frame + length of the L2CAP header (4 octets).

**==> picture [341 x 238] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An ACL link is established between the IUT and the Lower Tester<br>L2CAP_CONNECTION_REQ (first fragment)<br>RTX_TIMER L2CAP_CONNECTION_REQ (last fragment)<br>L2CAP_CONNECTION_RSP<br>(ID, Data length, PSM, DCID, result, status)<br>L2CAP_CONFIGURATION_REQ (first fragment)<br>RTX_TIMER L2CAP_CONFIGURATION_REQ (last fragment)<br>L2CAP_CONFIGURATION_RSP<br>(ID, Data length, PSM, SCID, Result = Success,<br>IUT, options)<br>L2CAP_CONFIGURATION_REQ<br>(ID, Data length, DCID, flags, MTU)<br>L2CAP_CONFIGURATION_REQ (first fragment)<br>L2CAP_CONFIGURATION_RSP (last fragment)<br>An L2CAP channel on the relevant PSM is established between the IUT and the Lower Tester<br>**----- End of picture text -----**<br>

_Figure 4.9: L2CAP/COS/CED/BV-12-C [Recombination of Signaling Packets] MSC_

- Expected Outcome

## Pass verdict

The IUT sends correct L2CAP signaling PDUs before the RTX timer expires in response to the correctly recombined L2CAP PDUs sent by the Lower Tester.

-

- Notes

The Lower Tester’s RTX timer is set to maximum allowed initial value.

It is allowed for the IUT to fragment its signaling packets, as well.

## **L2CAP/COS/CED/BI-03-C [Incorrect PDU Length, Received Data Packet, Basic]**

- Test Purpose

Verify that the IUT properly handles L2CAP Data PDUs that have an invalid PDU length.

- Reference

- [1] 3.1, 4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **28 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The IUT is in the OPEN state with the BR/EDR transport for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

1. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 3, and 4 octets of Information Payload Data.

2. Perform alternative 2A, 2B, or 2C depending on the IUT’s response.

- Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.

- 2A.2 The test ends with a Pass verdict.

- Alternative 2B (IUT discards the frame):

- 2B.1 The IUT discards the frame.

- 2B.2 The IUT does not send data to the Upper Tester.

- Alternative 2C (Any other IUT response):

- 2C.1 The Upper Tester issues a warning and the test ends.

3. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 4, and 4 octets of Information Payload Data.

4. The IUT sends the data received in Step 3 to the Upper Tester.

- Test Condition

Reliability for the basic mode channel is not needed, so the first PDU in Step 1 can be silently discarded. The IUT can use a finite flush timeout or an ERTM channel.

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.2, the IUT does not send the data from Step 1 to the Upper Tester.

In Step 2C.1, the IUT sends any valid response.

In Step 4, the IUT sends the data received in Step 3 to the Upper Tester.

- **4.10.1.1 Incorrect PDU Length, C-Frame**

- Test Purpose

Verify that the IUT properly handles L2CAP C-Frame PDUs that have an invalid PDU length.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The L2CAP signaling channel specified in Table 4.4 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **29 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case**|**Transport**|**Signaling**<br>**Channel**|**L2CAP payload/**<br>**PDU_Length/**<br>**Payload Length**|
|L2CAP/COS/CED/BI-04-C<br>[Incorrect PDU Length, C-Frame,<br>BR/EDR]|BR/EDR|0x0001|L2CAP_ECHO_REQ/RSP<br>4<br>5|
|L2CAP/COS/CED/BI-05-C<br>[Incorrect PDU Length, C-Frame,<br>LE Credit Based Connection<br>Request]|LE|0x0005|L2CAP_LE_CREDIT_<br>BASED_CONNECTION_<br>REQ/RSP<br>13<br>14|
|L2CAP/COS/CED/BI-18-C<br>[Incorrect PDU Length, C-Frame,<br>LE Enhanced Credit Based<br>Connection Request]|LE|0x0005|L2CAP_CREDIT_<br>BASED_CONNECTION_<br>REQ/RSP<br>13<br>14|
|L2CAP/COS/CED/BI-19-C<br>[Incorrect PDU Length, C-Frame,<br>LE Credit Based Connection<br>Request Rejected]|LE|0x0005|L2CAP_LE_CREDIT_<br>BASED_CONNECTION_<br>REQ<br>L2CAP_COMMAND_<br>REJECT_RSP<br>7<br>8|

_Table 4.4: Incorrect PDU Length, C-Frame test cases_

- Test Procedure

1. The Lower Tester sends a C-frame to the IUT with LLID set to 0b10, PDU Length specified in Table 4.4, and Channel ID set to the correct signaling channel for the logical link. The Information payload contains the packet payload request specified in Table 4.4. For the ECHO request, the payload contains 1 octet of ECHO data.

2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT’s response. Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link. 2A.2 The test ends with a Pass verdict.

- Alternative 2B (IUT discards the frame):

- 2B.1 The IUT does not send a reply to the Lower Tester.

- Alternative 2C (IUT rejects PDU):

- 2C.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP PDU to the Lower Tester.

- Alternative 2D (Any other IUT response): 2D.1 The Upper Tester issues a warning and the test ends.

3. The Lower Tester sends a C-frame to the IUT with LLID set to 0b10 and PDU Length set to the payload length specified in Table 4.4. The Information payload contains the payload length specified in Table 4.4 octets of data containing the L2CAP payload. For the ECHO request, the payload contains 1 octet of ECHO data.

4. The IUT sends the L2CAP response PDU specified in Table 4.4 to the Lower Tester.

-

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **30 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the Upper Tester.

## **L2CAP/COS/CED/BI-06-C [Incorrect PDU Length, Received Data Packets with Continuation, Basic]**

- Test Purpose

Verify that the IUT properly handles L2CAP Data PDUs that contain continuation packets that have an invalid PDU length.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The IUT is in the OPEN state with the BR/EDR transport for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

1. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 11, and 4 octets of Information Payload Data that contains 4 octets of data.

2. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b01 that contains 8 octets of data.

3. Perform alternative 3A, 3B, or 3C depending on the IUT’s response.

- Alternative 3A (IUT terminates the link):

- 3A.1 The IUT terminates the link.

- 3A.2 The test ends with a Pass verdict.

- Alternative 3B (IUT discards the frame):

- 3B.1 The IUT discards the frame.

- 3B.2 The IUT does not send data to the Upper Tester.

- Alternative 3C (Any other IUT response):

- 3C.1 The Upper Tester issues a warning and the test ends.

4. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b01, PDU Length set to 12, and 8 octets of Information Payload Data that contains 8 octets of data.

5. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 that contains 4 octets of data.

6. The IUT sends the data received in Steps 4 and 5 as one PDU to the Upper Tester.

- Test Condition

Reliability for the basic mode channel is not needed, so the first PDU in Step 1 can be silently discarded. The IUT can use a finite flush timeout or an ERTM channel.

- Expected Outcome

## Pass verdict

In Step 3A.1, the IUT terminates the link.

In Step 3B.2, the IUT does not send the data from Step 1 to the Upper Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **31 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

In Step 3C.1, the IUT sends any valid response.

In Step 6, the IUT sends the data received in Steps 4 and 5 as one PDU to the Upper Tester.

## **L2CAP/COS/CED/BI-07-C [Incorrect PDU Length, Received Data Packets with Multiple Continuation]**

- Test Purpose

Verify that the IUT properly handles L2CAP Data PDUs that contain multiple continuation packets that have an invalid PDU length.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The IUT is in the OPEN state with the BR/EDR transport for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

1. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 4, and 4 octets of Information Payload Data that contains 4 octets of data.

2. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 and 8 octets of Information Payload Data that contains 8 octets of data.

3. The IUT sends the data in Step 1 to the Upper Tester as one PDU.

4. Perform alternative 4A, 4B, or 4C depending on the IUT’s response. Alternative 4A (IUT terminates the link):

- 4A.1 The IUT terminates the link.

- 4A.2 The test ends with a Pass verdict.

- Alternative 4B (IUT discards the frame):

- 4B.1 The IUT discards the frame from Step 2.

- 4B.2 The IUT does not send data to the Upper Tester.

- Alternative 4C (Any other IUT response):

- 4C.1 The Upper Tester issues a warning and the test ends.

5. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 12, and 4 octets of Information Payload Data that contains 4 octets of data.

6. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 and 8 octets of Information Payload Data that contains 8 octets of data.

7. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 and 8 octets of Information Payload Data that contains 8 octets of data.

8. The IUT sends the data in Steps 5 and 6 as one PDU to the Upper Tester.

9. Perform alternative 9A, 9B, or 9C depending on the IUT’s response. Alternative 9A (IUT terminates the link):

- 9A.1 The IUT terminates the link.

- 9A.2 The test ends with a Pass verdict.

- Alternative 9B (IUT discards the frame):

- 9B.1 The IUT discards the frame from Step 7.

- 9B.2 The IUT does not send data to the Upper Tester.

- Alternative 9C (Any other IUT response):

- 9C.1 The Upper Tester issues a warning and the test ends.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **32 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

10. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 4, and 4 octets of Information Payload Data that contains 4 octets of data.

11. The IUT sends the data in Step 10 to the Upper Tester as one PDU.

- Test Condition

Reliability for the basic mode channel is not needed, so the first PDU in Step 1 can be silently discarded. The IUT can use a finite flush timeout or an ERTM channel.

- Expected Outcome

## Pass verdict

In Step 3, the IUT sends the data in Step 1 to the Upper Tester.

In Step 4A.1 or 9A.1, the IUT terminates the link.

In Step 4B.2 or 9B.2, the IUT does not send the data from Step 1 to the Upper Tester.

In Step 4C.1 or 9C.1, the IUT sends any valid response.

In Step 8, the IUT sends the data received in Steps 5 and 6 as one PDU to the Upper Tester.

In Step 11, the IUT sends the data in Step 10 to the Upper Tester.

- **4.10.1.2 Valid Signaling Command, Data Length > PDU Space**

- Test Purpose

Verify that the IUT properly handles incorrect L2CAP signaling command packets with invalid Data length.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The L2CAP signaling channel specified in Table 4.5 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

- Test Case Configuration

|**Test Case**|**Transport**|**Signaling**<br>**Channel**|**L2CAP payload/**<br>**PDU_Length/**<br>**Data Length**|
|L2CAP/COS/CED/BI-08-C [Valid<br>Signaling Command, Data Length<br>> PDU Space, BR/EDR]|BR/EDR|0x0001|L2CAP_ECHO_REQ/RSP<br>7<br>4|
|L2CAP/COS/CED/BI-09-C [Valid<br>Signaling Command, Data Length<br>> PDU Space, LE Credit Based<br>Connection Request]|LE|0x0005|L2CAP_LE_CREDIT_<br>BASED_CONNECTION_<br>REQ/RSP<br>14<br>11|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **33 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Test Case**|**Transport**|**Signaling**<br>**Channel**|**L2CAP payload/**<br>**PDU_Length/**<br>**Data Length**|
|L2CAP/COS/CED/BI-20-C [Valid<br>Signaling Command, Data Length<br>> PDU Space, LE Enhanced<br>Credit Based Connection<br>Request]|LE|0x0005|L2CAP_CREDIT_<br>BASED_CONNECTION_<br>REQ/RSP<br>14<br>11|
|L2CAP/COS/CED/BI-21-C [Valid<br>Signaling Command, Data Length<br>> PDU Space, LE Credit Based<br>Connection Request Rejected]|LE|0x0005|L2CAP_LE_CREDIT_<br>BASED_CONNECTION_<br>REQ<br>L2CAP_COMMAND_<br>REJECT_RSP<br>8<br>5|

_Table 4.5: Valid Signaling Command, Data Length > PDU Space test cases_

- Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.5 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length and L2CAP payload set as specified in Table 4.5. For the ECHO request, the payload contains 3 octets of ECHO data.

2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT’s response. Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.

- 2A.2 The test ends with a Pass verdict.

- Alternative 2B (IUT discards the frame): 2B.1 The IUT does not send a reply to the Lower Tester.

- Alternative 2C (IUT rejects PDU):

- 2C.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP PDU to the Lower Tester.

- Alternative 2D (Any other IUT response): 2D.1 The Upper Tester issues a warning and the test ends.

3. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.5 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains the correct data length for the L2CAP payload specified in Table 4.5. For the ECHO request, the payload contains 3 octets of ECHO data.

4. The IUT sends the L2CAP response PDU specified in Table 4.5 to the Lower Tester.

-

## Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **34 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.10.1.3 Incorrect Signaling Command Packets, Invalid Data Length for Command**

- Test Purpose

Verify that the IUT properly handles incorrect L2CAP signaling command packets with invalid Data length.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The L2CAP signaling channel specified in Table 4.6 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

- Test Case Configuration

|**Test Case**|**Transport**|**Signaling**<br>**Channel**|**Execute**<br>**Steps 3**<br>**and 4**|
|L2CAP/COS/CED/BI-10-C [Incorrect Signaling<br>Command Packets, Invalid Data Length for<br>Command, BR/EDR]|BR/EDR|0x0001|Yes|
|L2CAP/COS/CED/BI-11-C [Incorrect Signaling<br>Command Packets, Invalid Data Length for<br>Command, LE]|LE|0x0005|No|

_Table 4.6: Incorrect Signaling Command Packets, Invalid Data Length for Command test cases_

- Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length set to 9 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 5 with an L2CAP_DISCONNECTION_REQ packet followed by an octet with value 0x00.

2. Perform alternatives 2A, 2B, 2C, or 2D depending on the IUT’s response. Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.

- 2A.2 The test ends with a Pass verdict.

- Alternative 2B (IUT discards the frame): 2B.1 The IUT does not send a reply to the Lower Tester.

- Alternative 2C (IUT rejects PDU):

- 2C.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP PDU to the Lower Tester.

- Alternative 2D (Any other IUT response): 2D.1 The Upper Tester issues a warning and the test ends.

- Execute Steps 3 and 4 if indicated in Table 4.6.

3. The Lower Tester sends a C-frame to the IUT with PDU Length set to 7 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 3 with an L2CAP_ECHO_REQ packet with 3 octets of echo data.

4. The IUT sends an L2CAP_ECHO_RSP PDU to the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **35 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the Lower Tester.

## **L2CAP/COS/CED/BI-12-C [Valid Signaling Command, Shorter Data Length, Extra Zero Octet, BR/EDR]**

- Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with extra data in the Information Payload.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The BR/EDR L2CAP signaling channel 0x0001 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

- Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length set to 9 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 4 with an L2CAP_ECHO_REQ packet with 4 octets of echo data followed by a 0 octet.

2. Perform alternative 2A or 2B depending on the IUT’s response. Alternative 2A (Send the echo response):

- 2A.1 The IUT sends an L2CAP_ECHO_RSP PDU to the Lower Tester.

- Alternative 2B (Disconnect):

- 2B.1 The IUT terminates the link.

- 2B.2 The test ends with a Pass verdict.

3. Perform alternative 3A, 3B, or 3C depending on the IUT’s response. Alternative 3A (Reject the signaling command):

- 3A.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP to the Lower Tester with Reason set to 0x0000.

- Alternative 3B (Disconnect):

- 3B.1 The IUT terminates the link.

Alternative 3C (Ignore the invalid command):

- 3C.1 The IUT does not send a response to the Lower Tester.

- 3C.2 The Lower Tester sends a C-frame to the IUT with PDU Length set to 8 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 4 with an L2CAP_ECHO_REQ packet with 4 octets of echo data.

- 3C.3 The IUT sends an L2CAP_ECHO_RSP PDU to the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **36 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

In Step 2, the IUT responds to the L2CAP_ECHO_REQ from Step 1.

In Step 3A, the IUT rejects the command from Step 1.

In Step 2B or 3B, the IUT disconnects the link.

In Step 3C, the IUT ignores the invalid command and responds to the ECHO request.

## **4.10.1.4 Valid Signaling Command, Data Length > PDU Space**

- Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with extra data in the Information Payload.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The LE L2CAP signaling channel 0x0005 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **37 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case**|**Transport**|**Signaling**<br>**Channel**|**L2CAP payload**|**Step 1 PDU Length /**<br>**Data Length**|**Step 3 PDU Length /**<br>**Data Length**|
|L2CAP/COS/CED/BI-13-C [Valid<br>Signaling Command, Shorter<br>Data Length, Extra Zero Octet, LE<br>Credit Based Connection<br>Request]|LE|0x0005|L2CAP_LE_CREDIT_<br>BASED_CONNECTION_<br>REQ/RSP|15<br>10|14<br>10|
|L2CAP/COS/CED/BI-22-C [Valid<br>Signaling Command, Data Length<br>> PDU Space, LE Enhanced<br>Credit Based Connection<br>Request]|LE|0x0005|L2CAP_CREDIT_<br>BASED_CONNECTION_<br>REQ/RSP|15<br>10|14<br>10|
|L2CAP/COS/CED/BI-23-C [Valid<br>Signaling Command, Data Length<br>> PDU Space, LE Enhanced<br>Credit Based Connection<br>Request Rejected]|LE|0x0005|L2CAP_CREDIT_<br>BASED_CONNECTION_<br>REQ<br>L2CAP_COMMAND_<br>REJECT_RSP|9<br>4|8<br>4|

_Table 4.7: Valid Signaling Command, Data Length > PDU Space test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **38 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.7 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set as specified in Table 4.7 with an L2CAP packet payload request as specified in Table 4.7 with data length octets of connection data followed by a 0 octet.

2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT’s response. Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.

- 2A.2 The test ends with a Pass verdict.

- Alternative 2B (IUT discards the frame):

- 2B.1 The IUT does not send a reply to the Lower Tester.

- Alternative 2C (IUT rejects PDU):

- 2C.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP PDU to the Lower Tester.

- Alternative 2D (Any other IUT response): 2D.1 The Upper Tester issues a warning and the test ends.

3. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.7 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains an L2CAP packet payload request as specified in Table 4.7 with Data Length set as specified in Table 4.7 and with data length octets of connection request data.

4. The IUT sends the L2CAP response PDU specified in Table 4.7 to the Lower Tester. If that response is L2CAP_COMMAND_REJECT_RSP, the test ends with a Pass verdict.

5. The Lower Tester sends an L2CAP_DISCONNECTION_REQ PDU to the IUT.

6. The IUT sends an L2CAP_DISCONNECTION_RSP PDU to the Lower Tester.

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the connection request in Step 3.

- **4.10.1.5 Multiple Signaling Command in one PDU, Data Truncated, BR/EDR**

- Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with a Data Length of 0 in the Information Payload.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The BR/EDR L2CAP signaling channel 0x0001 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **39 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case**|**Second**<br>**Command/Response**|**Second**<br>**Command Data**<br>**Length**|**PDU Length**|
|L2CAP/COS/CED/BI-14-C<br>[Multiple Signaling<br>Command in one PDU,<br>Data Truncated, BR/EDR,<br>Echo Request]|L2CAP_ECHO_REQ<br>L2CAP_ECHO_RSP|1|8|
|L2CAP/COS/CED/BI-15-C<br>[Multiple Signaling<br>Command in one PDU,<br>Data Truncated, BR/EDR,<br>Disconnection Request]|L2CAP_DISCONNECTION_<br>REQ<br>L2CAP_DISCONNECTION_<br>RSP|0|8|

_Table 4.8: Multiple Signaling Command in one PDU, Data Truncated, BR/EDR test cases_

- Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length as specified in Table 4.8 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains one L2CAP_ECHO_REQ packet with Data Length set to 0 with 0 octets of echo data and one command packet and Data Length set as specified in Table 4.8.

2. The IUT sends an L2CAP_ECHO_RSP PDU to the Lower Tester.

3. Perform alternative 3A, 3B, 3C, or 3D depending on the IUT’s response. Alternative 3A (IUT terminates the link): 3A.1 The IUT terminates the link. 3A.2 The test ends with a Pass verdict.

Alternative 3B (IUT discards the frame): 3B.1 The IUT does not send a reply to the Lower Tester.

Alternative 3C (IUT rejects PDU):

- 3C.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP PDU to the Lower Tester.

- Alternative 3D (Any other IUT response): 3D.1 The Upper Tester issues a warning and the test ends.

4. The Lower Tester sends a C-frame to the IUT with PDU Length set to 4 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 0 with an L2CAP_ECHO_REQ packet with 0 octets of echo data.

5. The IUT sends an L2CAP_ECHO_RSP PDU to the Lower Tester.

-

- Expected Outcome

## Pass verdict

In Steps 2 and 5, the IUT responds with an L2CAP_ECHO_RSP.

In Step 3A.1, the IUT terminates the link.

In Step 3B.1, the IUT does not send a reply to the Lower Tester.

In Step 3C.1, the IUT rejects the PDU.

In Step 3D.1, the IUT sends any valid response.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **40 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.10.1.6 Multiple Signaling Command in one PDU, Data Truncated, LE**

- Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with an incorrect PDU length in the Information Payload.

- Reference

- [1] 3.1, 4

- Initial Condition

- The Lower Tester uses version L2CAP Basic Mode.

- No security is used in this test case.

- The LE L2CAP signaling channel 0x0005 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **41 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case**|**PDU Length**|**First Command/Response**|**First**<br>**Command**<br>**Data Length**|**Second Command/Response**|**Second**<br>**Command**<br>**Data Length**|
|L2CAP/COS/CED/BI-16-C<br>[Multiple Signaling Command in<br>one PDU, Data Truncated, LE<br>Credit Based Flow Control Mode,<br>LE Credit Based Connection<br>Request]|28|L2CAP_LE_CREDIT_BASED_<br>CONNECTION_REQ<br>L2CAP_LE_CREDIT_BASED_<br>CONNECTION_RSP|10|L2CAP_LE_CREDIT_BASED_<br>CONNECTION_REQ<br>L2CAP_LE_CREDIT_BASED_<br>CONNECTION_RSP|11|
|L2CAP/COS/CED/BI-17-C<br>[Multiple Signaling Command in<br>one PDU, Data Truncated, LE<br>Credit Based Flow Control Mode,<br>Disconnection Request]|22|L2CAP_LE_CREDIT_BASED_<br>CONNECTION_REQ<br>L2CAP_LE_CREDIT_BASED_<br>CONNECTION_RSP|10|L2CAP_DISCONNECTION_<br>REQ<br>L2CAP_DISCONNECTION_<br>RSP|5|
|L2CAP/COS/CED/BI-24-C<br>[Multiple Signaling Command in<br>one PDU, LE, Data Truncated,<br>Enhanced Credit Based Flow<br>Control Mode, Enhanced Credit<br>Based Connection Request]|28|L2CAP_CREDIT_BASED_<br>CONNECTION_REQ<br>L2CAP_CREDIT_BASED_<br>CONNECTION_RSP|10|L2CAP_CREDIT_BASED_<br>CONNECTION_REQ<br>L2CAP_CREDIT_BASED_<br>CONNECTION_RSP|11|
|L2CAP/COS/CED/BI-25-C<br>[Multiple Signaling Command in<br>one PDU, LE, Data Truncated,<br>Enhanced Credit Based Flow<br>Control Mode, Disconnection<br>Request]|22|L2CAP_CREDIT_BASED_<br>CONNECTION_REQ<br>L2CAP_CREDIT_BASED_<br>CONNECTION_RSP|10|L2CAP_DISCONNECTION_<br>REQ<br>L2CAP_DISCONNECTION_<br>RSP|5|

_Table 4.9: Multiple Signaling Command in one PDU, Data Truncated, LE test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **42 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.9 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains one first L2CAP command request packet, Data Length, and connection request data size as specified in Table 4.9 and one second command request packet and Data Length set as specified in Table 4.9 and the correct command data.

2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT’s response.

- Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.

- 2A.2 The test ends with a Pass verdict.

- Alternative 2B (IUT discards the frame):

- 2B.1 The IUT does not send a reply to the Lower Tester.

- Alternative 2C (IUT rejects PDU):

- 2C.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP PDU to the Lower Tester.

- Alternative 2D (Any other IUT response): 2D.1 The Upper Tester issues a warning and the test ends.

3. The Lower Tester sends a C-frame to the IUT with PDU Length set to 14 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains a first L2CAP command request packet, Data Length, and connection request data size as specified in Table 4.9.

4. The IUT sends the first L2CAP response PDU to the Lower Tester.

5. The Lower Tester sends an L2CAP_DISCONNECTION_REQ PDU to the IUT.

6. The IUT sends an L2CAP_DISCONNECTION_RSP PDU to the Lower Tester.

- Expected Outcome

## Pass verdictA

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the connection request in Step 4.

- **4.10.1.7 Ignore Command Response with Invalid ID or Duplicate Response**

- Test Purpose

Verify that the IUT ignores a Command Response with an Invalid ID and a duplicate response. The Invalid ID can be an ID of 0. The test also verifies that identifiers are not duplicated until all valid identifiers have been used.

- Reference

- [1] 4

-

- Initial Condition

- The IUT is in CLOSED state for data channel. No ACL link is established.

- No security is used in this test case.

- The L2CAP signaling channel specified in Table 4.10 is established between the IUT and the Lower Tester.

- The IUT is in CLOSED state and acts as an L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **43 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case**|**Transport**|**Signaling**<br>**Channel**|**L2CAP Signaling Packet**|
|L2CAP/COS/CED/BI-28-C<br>[Ignore Command Response with<br>Invalid ID or Duplicate Response,<br>BR/EDR]|BR/EDR|0x0001|L2CAP_CONNECTION_<br>REQ/RSP|
|L2CAP/COS/CED/BI-29-C<br>[Ignore Command Response with<br>Invalid ID or Duplicate Response,<br>LE]|LE|0x0005|L2CAP_LE_CREDIT_<br>BASED_CONNECTION_<br>REQ/RSP|

_Table 4.10: Ignore Command Response with Invalid ID or Duplicate Response test cases_

- Test Procedure

**==> picture [332 x 346] intentionally omitted <==**

_Figure 4.10: Ignore Command Response with Invalid ID or Duplicate Response MSC_

1. The Upper Tester commands the IUT to start the procedure that initiates the connection request specified in Table 4.10.

2. The IUT sends an L2CAP request PDU specified in Table 4.10 to the Lower Tester with an Identifier. The Lower Tester saves the Identifier.

3. The Lower Tester sends a successful L2CAP response PDU specified in Table 4.10 to the IUT with the Identifier set to 0.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **44 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

4. The IUT and the Lower Tester do not make a connection.

5. Repeat Steps 1–4 with the Identifier in Step 3 set to any non-zero value other than the two values saved in Step 2.

6. Repeat Steps 1–4 253 times with the Identifier in Step 3 set to 0x00. The test fails if the IUT reuses an Identifier that already was used.

7. The Upper Tester commands the IUT to start the procedure that initiates the connection request specified in Table 4.10.

8. The IUT sends an L2CAP request PDU specified in Table 4.10 to the Lower Tester with an Identifier.

9. The Lower Tester sends a successful L2CAP response PDU specified in Table 4.10 to the IUT with the Identifier set to the value in Step 8.

10. If the Transport is BR/EDR, the Lower Tester and the IUT may execute the L2CAP Configuration Process.

11. The IUT sends a connection complete event to the Upper Tester.

12. The Lower Tester sends the same L2CAP response PDU as was sent in Step 9.

13. If the IUT sends a connection complete event to the Upper Tester, the test ends with a Fail verdict.

14. The Lower Tester sends an L2CAP_DISCONNECTION_REQ PDU to the IUT.

15. The IUT sends an L2CAP_DISCONNECTION_RSP PDU to the Lower Tester.

- Expected Outcome

## Pass verdict

In Step 4, the IUT and the Lower Tester do not make a connection.

In Step 15, the IUT sends an L2CAP_DISCONNECTION_RSP PDU.

## Fail verdict

The IUT reuses an Identifier in Step 2 in the first 255 repeats.

In Step 13, the IUT sends a connection complete event.

## **4.10.2 Encryption Key Size**

Tests for insufficient encryption key size require an encrypted link with a key size less than the size required by an L2CAP channel. The encryption key size requirements of attributes are determined by the associated profile.

## Preamble procedure:

Establish an encrypted link over the LE transport between the IUT and the Lower Tester. For example, see test SM/CEN/EKS/BV-01-C or SM/PER/EKS/BV-02-C in [16] for LE transport, or LMP/ENC/BV-01-C or LMP/ENC/BV-05-C in [17] for BR/EDR transport. The key size is less than the size required by the security requirements of the L2CAP channel.

## **4.10.3 Configuration of Data Channel CFD**

Verify the procedures for configuration of a data channel.

## **L2CAP/COS/CFD/BV-01-C [Continuation Flag]**

- Test Purpose

Verify that the IUT can receive configuration requests that have the continuation flag set.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **45 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

[1] Table 6.1, 4.4, 4.5, 5

- Initial Condition

- The IUT is in CONFIG state for a data channel with assigned CID. The IUT’s request path is already configured. The connection was initiated from the Lower Tester.

- Test Procedure

**==> picture [337 x 261] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.The IUT´s request path is configured.<br>L2CAP_ConfigReq<br>(ID, length, DCID, C-flag=1, InMTU)<br>ALT 1 L2CAP_ConfigRsp<br>(ID, length, SCID, C-flag=1, Result, InMTU)<br>L2CAP_ConfigReq<br>(ID, length, DCID, C-flag=0, OutFlow,<br>OutFlushTO)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, C-flag=0, Result,<br>OutFlow, OutFlushTO)<br>ALT 2 L2CAP_ConfigRsp<br>(ID, length, SCID, C-flag=1,<br>Result=Success, no options)<br>L2CAP_ConfigReq<br>(ID, length, DCID, C-flag=0, OutFlow,<br>OutFlushTO)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, C-flag=0, Result,<br>IUT options)<br>**----- End of picture text -----**<br>

_Figure 4.11: L2CAP/COS/CFD/BV-01-C [Continuation Flag] MSC_

- Test Condition

Acceptable configuration parameter values are supplied by the manufacturer.

-

- Expected Outcome

## Pass verdict

The IUT responds to each L2CAP_ConfigReq message with an L2CAP_ConfigRsp message indicating "success". The response to the first message has the continuation flag set. The final response has the continuation flag cleared. One of the two responses indicates an MTU size equal to that in the request.

-

## Notes

The Lower Tester sets the most significant bit of the type parameter to '1', indicating a "hint", for the optional parameters Quality of Service, and Retransmission and Flow Control. If the IUT supports the optional parameter, it accepts the default value; if it does not support an optional parameter, it should ignore the hint and take no additional action.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **46 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/COS/CFD/BV-02-C [Negotiation with Reject]**

- Test Purpose

Verify that the IUT can perform negotiation while the Lower Tester rejects the proposed configuration parameter values.

- Reference

- [1] Table 6.1, 4.4, 4.5

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in CONFIG state for a data channel with assigned CID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

**==> picture [338 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, IUT options)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, Flags, Result=0x0001,<br>acceptable OutMTU, acceptable InFlow,<br>acceptable InFlushTO)<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, IUT options)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, Flags, Result=success)<br>**----- End of picture text -----**<br>

_Figure 4.12: L2CAP/COS/CFD/BV-02-C [Negotiation with Reject] MSC_

- Test Condition

Acceptable configuration parameter values have to be stated by the manufacturer.

-

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigReq with acceptable values received in the L2CAP_ConfigRsp with Result= Failure – unacceptable parameters or the L2CAP_ConfigReq contains no options.

or

The IUT closes the channel.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **47 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/COS/CFD/BV-03-C [Send Requested Options]**

- Test Purpose

Verify that the IUT can receive a configuration request with no options and send the requested options to the Lower Tester.

- Reference

- [1] Table 6.1, 4.4, 4.5

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in CONFIG state for data channel with assigned CID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

**==> picture [341 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, no options)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, Flags, result, local options)<br>**----- End of picture text -----**<br>

_Figure 4.13: L2CAP/COS/CFD/BV-03-C [Send Requested Options] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigRsp before expiration of RTX timer.

-

- Notes

The Lower Tester uses TSPX_timer_rtx_max for RTX timer.

## **L2CAP/COS/CFD/BV-08-C [Non-blocking Config Response]**

- Test Purpose

Verify that the IUT does not block transmitting L2CAP_ConfigRsp while waiting for L2CAP_ConfigRsp from the Lower Tester.

- Reference

- [1] 4.4, 4.5

-

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in CONFIG state for a channel with CID. The IUT acts as L2CAP initiator.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **48 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [335 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT has transmitted L2CAP_CONNECTION_REQ.<br>L2CAP_ConfigReq<br>(Code, ID, Length, DCID, Flags,<br>IUT options)<br>L2CAP_ConfigReq<br>(Code, ID, Length, DCID, Flags, MTU)<br>L2CAP_ConfigRsp<br>(Code, ID, Length, SCID, Flags, Result, IUT<br>options)<br>L2CAP_ConfigRsp<br>(Code, ID, Length, SCID, Flags, Result)<br>**----- End of picture text -----**<br>

_Figure 4.14: L2CAP/COS/CFD/BV-08-C [Non-blocking Config Response] MSC_

- Expected Outcome

## Pass verdict

After receiving L2CAP_ConfigReq from the Lower Tester, the IUT transmits L2CAP_ConfigRsp to the Lower Tester.

- Notes

The Lower Tester uses an MTU value not exceeding what is transmitted from the IUT in the L2CAP_ConfigReq. Other options have default or accepted values, and hence, need not be transmitted. It is implementation dependent which options are transmitted by the IUT.

## **L2CAP/COS/CFD/BV-09-C [Mandatory 48 Byte MTU]**

- Test Purpose

Verify that the IUT can support mandatory 48 byte MTU.

- Reference

- [1] 5.1, 7.1

- Initial Condition

- The IUT is in CONFIG state for a channel with CID.

- The IUT acts as L2CAP initiator.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **49 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [229 x 479] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>IUT in CONFIG state for channel with CID<br>L2CAP_ConfigReq<br>ID,length,DCID,Flags,<br>[InMTU]<br>L2CAP_ConfigRes<br>Result=success<br>ID,length, SCID, Flags<br>InMTU=48<br>L2CAP_ConfigReq<br>ID,length,DCID,Flags<br>InMTU = 48<br>L2CAP_ConfigRes Optional<br>Result=success<br>ID,length, SCID, Flags<br>InMTU=48(inMTU is optional)<br>L2CAP_PDU First L2CAP PDU has<br>Payload size 48 Bytes<br>length=48,DCID, Payload<br>(size = 48 Bytes)<br>Optional<br>L2CAP_PDU Additional L2CAP PDUs<br>length=48,DCID, Payload with Payload size 48 Bytes<br>(size = 48 Bytes)<br>Optional<br>L2CAP_PDU Last L2CAP PDU has<br>Length=< 48,DCID,Payload Payload size <48 Bytes<br>(size = Length)<br>InMTU<br>**----- End of picture text -----**<br>

_Figure 4.15: L2CAP/COS/CFD/BV-09-C [Mandatory 48 Byte MTU] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits a configuration request containing InMTU or omit the InMTU. Regardless of indicated MTU, when the Lower Tester responds with MTU=48 the configuration completes successfully without further negotiation.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **50 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

The IUT responds with MTU=48 or omit the MTU in its configuration response. The configuration completes successfully without further negotiation.

- Notes

In part 1, the IUT may request any MTU > 48.

## **L2CAP/COS/CFD/BV-10-C [Retransmission Mode Negotiation]**

- Test Purpose

Verify that the IUT can negotiate L2CAP F+E for Retransmission mode.

- Reference

- [1] 5.3, 7.4

- Initial Condition

- The IUT is in CONFIG state for a data channel with assigned CID.

- Test Procedure

**==> picture [341 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, InMTU, OutFlow,<br>OutFlushTO, Flow & Error Control<br>(flag=0x01))<br>L2CAP_ConfigRsp<br>(result=success, InMTU, OutFlow,<br>OutFlushTO, Flow & Error Control<br>(flag=0x01))<br>**----- End of picture text -----**<br>

_Figure 4.16: L2CAP/COS/CFD/BV-10-C [Retransmission Mode Negotiation] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigReq with L2CAP Flow and Error control option for Retransmission mode.

## **L2CAP/COS/CFD/BV-11-C [Negotiation of Unsupported Parameter]**

- Test Purpose

Verify that the IUT can negotiate when the Lower Tester proposes an unsupported configuration parameter value.

- Reference

- [1] 4.4, 4.5

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **51 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The Lower Tester performs an Information Request/Response command to read the supported mode of the IUT.

- The Lower Tester then sends a Configuration Request with unsupported configuration parameters to the IUT.

- Test Procedure

The Lower Tester proposes configuration parameter values the IUT does not support.

The IUT acts either as L2CAP initiator or as L2CAP acceptor.

**==> picture [341 x 220] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags,<br>unacceptable option)<br>L2CAP_ConfigRsp ALT 1<br>(ID, length, SCID, Flags,<br>Result=0x0001, adjusted option)<br>L2CAP_ConfigRsp ALT 2<br>(ID, length, SCID, Flags,<br>Result=0x0000)<br>**----- End of picture text -----**<br>

_Figure 4.17: L2CAP/COS/CFD/BV-11-C [Negotiation of Unsupported Parameter] MSC_

- Expected Outcome

## Pass verdict

The IUT negotiates the configuration parameters to supported values (ALT 1). If NO unacceptable options are possible, the IUT may respond as shown in ALT 2.

## **L2CAP/COS/CFD/BV-12-C [Unknown Option Response]**

- Test Purpose

Verify that the IUT can give the appropriate error code when the Lower Tester proposes any number of unknown options that are optional.

- Reference

- [1] 4.4, 4.5

- Initial Condition

- The IUT is in CONFIG state. Supported configuration option types are given as the TSPX_supported_config_options IXIT value.

- The IUT either acts as L2CAP initiator or as L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **52 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Repeat the steps for each round in Table 4.11.

The Lower Tester transmits a configuration request with a number of options as specified in Table 4.11 where the option types are not supported by the IUT and all have the MSB set to 1.

**==> picture [199 x 199] intentionally omitted <==**

**----- Start of picture text -----**<br>
Round Number of Options<br>1 1<br>2 2<br>3 3<br>4 4<br>5 5<br>6 6<br>7 7<br>8 8<br>9 9<br>10 10<br>**----- End of picture text -----**<br>

_Table 4.11: L2CAP/COS/CFD/BV-12-C [Unknown Option Response] rounds_

**==> picture [374 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.<br>Repeat for Rounds 1-10<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, unknown options: msb:1)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, Flags, result, local options)<br>**----- End of picture text -----**<br>

_Figure 4.18: L2CAP/COS/CFD/BV-12-C [Unknown Option Response] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_ConfigRsp before expiration of RTX timer.

## **L2CAP/COS/CFD/BV-13-C [Flow Control Mode Negotiation]**

- Test Purpose

Verify that the IUT can negotiate L2CAP F+E for Flow Control only mode.

- Reference

- [1] 5.4, 7.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **53 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT is in CONFIG state for a data channel with assigned CID.

- Test Procedure

**==> picture [335 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, IUT options)<br>L2CAP_ConfigRsp, L2CAP_ConfigReq<br>(ID, length, SCID, Flags, result,<br>options1, ID, length, DCID, Flags,<br>options2)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, Flags, result, IUT options)<br>**----- End of picture text -----**<br>

_Figure 4.19: L2CAP/COS/CFD/BV-13-C [Flow Control Mode Negotiation] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigReq with L2CAP Flow and Error control option for Flow Control only mode.

## **L2CAP/COS/CFD/BV-14-C [Unknown Mandatory Options Request]**

- Test Purpose

Verify that the IUT can give the appropriate error code when the Lower Tester proposes any number of unknown options where at least one is mandatory.

- Reference

[1] 4.4, 4.5

- Initial Condition

- The IUT is in CONFIG state. Supported configuration option types are given as the TSPX_supported_config_options IXIT value.

- The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure

The Lower Tester transmits a configuration request with a number of options as specified in Table 4.12 where the option types are not supported by the IUT and have the MSBs set as specified in Table 4.12.

|**Round**|**Number of Options**|**MSB value**|
|1|1|All set to 0|
|2|2|All set to 1, except the last one set to 0|
|3|3|All set to 0|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **54 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Round**|**Number of Options**|**MSB value**|
|4|4|Two at random set to 0, the rest set to 1|
|5|5|All set to 1, except the last one set to 0|
|6|6|Two at random set to 0, the rest set to 1|
|7|7|All set to 0|
|8|8|All set to 1, except the last one set to 0|
|9|9|Two at random set to 0, the rest set to 1|
|10|10|All set to 1, except the last one set to 0|

_Table 4.12: L2CAP/COS/CFD/BV-14-C [Unknown Mandatory Options Request] rounds_

**==> picture [374 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in CONFIG state for channel with CID.<br>Repeat for Rounds 1-10<br>L2CAP_ConfigReq<br>(ID, length, DCID, Flags, unknown options: msb)<br>L2CAP_ConfigRsp<br>(ID, length, SCID, Flags, Result=0x0003,<br>unknown option)<br>**----- End of picture text -----**<br>

_Figure 4.20: L2CAP/COS/CFD/BV-14-C [Unknown Mandatory Options Request] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_ConfigRsp with Result=0x0003 and specifying one of the unsupported options that has the MSB set to 0.

## **4.10.4 Implementation-Specific Information Exchange IEX**

Verify the implementation-specific information exchange feature.

## **L2CAP/COS/IEX/BV-01-C [Query for 1.2 Features]**

- Test Purpose

Verify that the IUT transmits an information request command to solicit if the remote device supports Specification 1.2 features.

- Reference

- [1] 4.10, 4.11

- Initial Condition

- The IUT is in any state.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **55 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [336 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in any state.<br>L2CAP_InfoReq<br>(ID, length, InfoType=0x0002)<br>L2CAP_InfoRsp<br>(ID, length, InfoType=0x0002, Result=0x0000, Data=0x00000002)<br>**----- End of picture text -----**<br>

_Figure 4.21: L2CAP/COS/IEX/BV-01-C [Query for 1.2 Features] MSC_

- Expected Outcome

Pass verdict

The IUT transmits L2CAP_InfoReq with InfoType=0x0002.

## **L2CAP/COS/IEX/BV-02-C [Respond with 1.2 Features]**

- Test Purpose

Verify that the IUT responds to an information request command soliciting for Specification 1.2 features.

- Reference

[1] 4.10, 4.11, 4.12

- Initial Condition

- The IUT is in any state.

- Test Procedure

**==> picture [341 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in any state.<br>L2CAP_InfoReq<br>(ID, length, InfoType=0x0002)<br>L2CAP_InfoRsp<br>(ID, length, InfoType=0x0002, Result, [Data])<br>**----- End of picture text -----**<br>

_Figure 4.22: L2CAP/COS/IEX/BV-02-C [Respond with 1.2 Features] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **56 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_InfoRsp with InfoType=0x0002.

If the IUT supports any extended features:

The Result=Success and Data is formatted correctly for an Extended Feature Mask.

Otherwise:

The Result=Success, and Data is set to 0x0000 0000, OR

The Result=Not Supported, and Data is not present.

## **4.10.5 Echo Handling ECH**

Verify the procedures for echo handling, which means link testing and passing of vendor-specific information with the ECHO_REQUEST and ECHO_RESPONSE signaling command.

## **L2CAP/COS/ECH/BV-01-C [Respond to Echo Request]**

- Test Purpose

Verify that the IUT responds to an echo request.

- Reference

- [1] Table 6.1, 4.8, 4.9

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in CLOSED state for data channel. No ACL link is established. The IUT acts as L2CAP acceptor.

- Test Procedure

**==> picture [375 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL link establishment tester.<br>L2CAP_EchoReq<br>(ID, length, data)<br>L2CAP_EchoRsp<br>(ID, length, data)<br>**----- End of picture text -----**<br>

_Figure 4.23: L2CAP/COS/ECH/BV-01-C [Respond to Echo Request] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_EchoRsp before expiration of RTX timer.

- Notes

The Lower Tester uses maximum value for RTX timer.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **57 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/COS/ECH/BV-02-C [Send Echo Request]**

- Test Purpose

Verify that the IUT sends an echo request.

- Reference

- [1] Table 6.1, 4.8, 4.9

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT is in CLOSED state for data channel. No ACL link is established. The IUT acts as L2CAP initiator.

- Test Procedure

ACL link establishment is part of the test case.

|Lower|Tester|Tester|Tester|Tester|Tester|Upper Tester|Upper Tester|
||(ID, length, data)<br>L2CAP_EchoRsp|||||||
||(ID, length, data)|||||||

_Figure 4.24: L2CAP/COS/ECH/BV-02-C [Send Echo Request] MSC_

- Test Condition

It must be possible to send an echo request from the Upper Tester to the Lower Tester.

-

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_EchoReq.

## **4.10.6 LE Credit Based Flow Control Mode**

Verify the correct implementation of the data channel in LE Credit Based Flow Control mode.

## **L2CAP/COS/CFC/BV-01-C [Segmentation]**

- Test Purpose

Verify that the IUT can send data segments that are larger than the K-frame payload size.

- Reference

## 12 3.4

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An LE Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value with credits returned to the IUT by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **58 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- The role of the IUT is indicated via TSPX_iut_role_initiator.

- The MTU and MPS of the Lower Tester are indicated in the TSPX_tester_mtu and TSPX_tester_mps IXIT values.

- The Upper Tester can command the IUT to send data.

- Test Procedure

**==> picture [302 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel is established between the Lower Tester<br>and IUT<br>LE Credit Based Flow Control Channel established<br>Data Packet<br>K-frame 0<br>K-frame 1<br>K-frame 2<br>K-frame N<br>**----- End of picture text -----**<br>

_Figure 4.25: L2CAP/COS/CFC/BV-01-C [Segmentation] MSC_

The Upper Tester sends a data packet to the IUT which is larger than or equal to the Lower Tester’s MPS and smaller than or equal to the Lower Tester’s MTU.

-

- Expected Outcome

## Pass verdict

The IUT sends at least one K-frame containing data to the Lower Tester.

If the Upper Test sends a data packet to the IUT which is larger than the Lower Tester’s MPS and smaller than the Lower Tester’s MTU, the IUT segments the K-frames correctly.

The data sent by the IUT to the Lower Tester matches the data sent to the IUT by the Upper Tester.

## **L2CAP/COS/CFC/BV-02-C [No Segmentation]**

- Test Purpose

Verify that the IUT can send data segments that do not require segmentation.

- Reference

- [12] 3.4

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An LE Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value with credits returned to the IUT by the Lower Tester.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **59 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [302 x 205] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel is established between the Lower Tester<br>and IUT<br>LE Credit Based Flow Control Channel established<br>Data Packet<br>K-frame 0<br>**----- End of picture text -----**<br>

_Figure 4.26: L2CAP/COS/CFC/BV-02-C [No Segmentation] MSC_

The Upper Tester sends a data packet of one octet to the IUT.

-

- Expected Outcome

## Pass verdict

The IUT send a K-frame containing the data to the Lower Tester.

The data sent by the IUT to the Lower Tester matches the data sent to the IUT by the Upper Tester.

## **L2CAP/COS/CFC/BV-03-C [Reassembling]**

- Test Purpose

Verify that the IUT can correctly reassemble data received from the Lower Tester where the L2CAP SDU Length is greater than the IUT K-frame payload size.

- Reference

- [12] 3.4

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An LE Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **60 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [302 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel is established between the Lower Tester<br>and IUT<br>LE Credit Based Flow Control Channel established<br>LE_Flow_Control_Credit<br>K-frame 0<br>LE_Flow_Control_Credit<br>K-frame N<br>LE_Flow_Control_Credit<br>Data Packet<br>**----- End of picture text -----**<br>

_Figure 4.27: L2CAP/COS/CFC/BV-03-C [Reassembling] MSC_

(Optional) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data in a series of K-frames to the IUT with the L2CAP SDU Length smaller than the IUT MTU.

- Expected Outcome

## Pass verdict

The IUT correctly reassembles the data received from the Lower Tester and sends it to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## **L2CAP/COS/CFC/BV-04-C [Data Receiving]**

- Test Purpose

Verify that the IUT can receive unsegmented data correctly.

- Reference

- [12] 3.4

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An LE Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **61 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [302 x 222] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel is established between the Lower Tester<br>and IUT<br>LE Credit Based Flow Control Channel established<br>LE_Flow_Control_Credit<br>K-frame<br>LE_Flow_Control_Credit<br>Data Packet<br>**----- End of picture text -----**<br>

_Figure 4.28: L2CAP/COS/CFC/BV-04-C [Data Receiving] MSC_

(Optional) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data in a single K-frame to the IUT. The SDU length is less than or equal to the length of the K-frame - 2.

-

- Expected Outcome

## Pass verdict

The IUT sends the received data to the Upper Tester

The data sent to the Upper Tester by the IUT matches the data sent by the Lower Tester to the IUT

## **L2CAP/COS/CFC/BV-05-C [Multiple Channels with Interleaved Data Streams]**

- Test Purpose

Verify that an IUT can create multiple channels and receives data streams on the channels when the streams are interleaved.

- Reference

[12] 4.22

-

- Initial Condition

- The appropriate signaling channel for the transport is used.

- The LE Data Channel is established using the SPSM declared via the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **62 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [296 x 456] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel is established between the Lower Tester<br>and IUT<br>LE_Credit_Based_Connection_<br>Req<br>(PSM = X)<br>LE_Credit_Based_Connection_<br>Rsp<br>LE Credit Based Flow Control Channel established (CID = Y)<br>LE_Credit_Based_Connection_<br>Req<br>(PSM = X)<br>LE_Credit_Based_Connection_<br>Rsp<br>LE Credit Based Flow Control Channel established (CID = Z)<br>LE_Flow_Control_Credit<br>K-frame (CID = Y)<br>K-frame (CID = Z)<br>K-frame (CID = Y)<br>K-frame (CID = Z)<br>K-frame (CID = Y)<br>Data from CID Y<br>K-frame (CID = Z)<br>Data from CID Z<br>**----- End of picture text -----**<br>

_Figure 4.29: L2CAP/COS/CFC/BV-05-C [Multiple Channels with Interleaved Data Streams] MSC_

(Optional) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data on the different channels interleaved.

- Expected Outcome

## Pass verdict

The IUT sends the received data to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **63 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.10.6.1 Recombination of Signaling Packets**

- Test Purpose

Verify that the IUT correctly handles fragmented L2CAP signaling PDUs.

- Initial Condition

- The signaling channel specified in Table 4.13 is used.

- An SPSM for the desired Credit Based or Enhanced Credit Based Flow Control based channel is declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **64 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-30-C [Recombination of<br>SignalingPackets]|[1]4.22, 4.23|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-39-C [Recombination of<br>SignalingPackets - LE]|[1]4.25, 4.26|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-40-C [Recombination of<br>SignalingPackets – BR/EDR]|[1]4.25, 4.26|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.13: Recombination of Signaling Packets test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **65 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 167] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between the IUT and the Lower Tester<br>L2CAP_[LE_]CREDIT_BASED_CONNECTION_REQ (first fragment)<br>L2CAP_[LE_]CREDIT_BASED_CONNECTION_REQ (last fragment)<br>RTX_TIMER L2CAP_[LE_]CREDIT_BASED_CONNECTION(Result = 0)_RSP<br>An L2CAP channel on the relevant SPSM is established between the IUT and the Lower Tester<br>**----- End of picture text -----**<br>

_Figure 4.30: Recombination of Signaling Packets MSC_

The L2CAP Credit Based Connection Request/Response commands are specified in Table 4.13.

The Lower Tester sends a valid connection request command, with nonzero credits to the IUT on the SPSM specified in the initial condition, fragmented into two fragments.

The IUT responds with a connection request response and establishes the credit-based channel.

-

- Expected Outcome

## Pass verdict

The IUT sends a correct connection request response in response to the connection request command received in the recombined C-frame.

- Note

It is allowed for the IUT to fragment its signaling packets, as well.

## **4.10.6.2 Recombination of Data Packets**

- Test Purpose

Verify that the IUT correctly handles fragmented L2CAP data PDUs.

- Reference

[12] 3.4

- Initial Condition

- The signaling channel specified in Table 4.14 is used.

- A Data Channel over the relevant bearer is established on the SPSM declared via the TSPX_spsm IXIT value using the commands specified in Table 4.14.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **66 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-31-C[Recombination of Data Packets]|[1]3.4, 7.2.2|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-41-C[Recombination of Data Packets]|[1]3.4, 7.2.2|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-42-C[Recombination of Data Packets]|[1]3.4, 7.2.2|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.14: Recombination of Data Packets test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **67 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

(Optional, for LE Credit-based) If the channel has been created with zero credits, the Upper Tester issues a command to the IUT to send credits to the Lower Tester.

The Lower Tester sends Credit-based frames (K-frame) on the established CID, with PDU Length equal to 10 bytes, fragmented into two fragments.

The IUT recombines the fragments and sends the received data to the Upper Tester.

**==> picture [340 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>An L2CAP fixed channel is established between the IUT and the Lower Tester<br>An L2CAP channel on the relevant SPSM is established between the IUT and the Lower Tester<br>L2CAP_FLOW_CONTROL_CREDIT_IND<br>(Credit Increment)<br>L2CAP Data (K-frame) (first fragment)<br>L2CAP Data (last fragment)<br>data<br>**----- End of picture text -----**<br>

_Figure 4.31: Recombination of Data Packets MSC_

- Expected Outcome

## Pass verdict

The IUT receives the fragments and recombines them into correctly formatted K-frames and sends the data to the Upper Tester. The data sent to the Upper Tester matches the data sent by the Lower Tester.

## **L2CAP/ECFC/BI-09-C [Incorrect Size Signaling Packets, BR/EDR]**

- Test Purpose

Verify that the IUT properly handles L2CAP signaling PDUs that have invalid length over BR/EDR.

- Initial Condition

- The appropriate signaling channel for the transport is used.

- No security is used in this test case.

- An SPSM for the desired Credit Based Flow Control based channel is declared via the TSPX_spsm IXIT value.

- An ACL connection is established between the Lower Tester and the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **68 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [328 x 351] intentionally omitted <==**

_Figure 4.32: L2CAP/ECFC/BI-09-C [Incorrect Size Signaling Packets] MSC_

1. The Lower Tester sends a C-frame to the IUT with PDU Length smaller than the signaling packet’s actual size, Channel ID set to the correct signaling channel for the logical link, and the Information payload containing a correct L2CAP_CREDIT_BASED_CONNECTION_REQ packet. The L2CAP_CREDIT_BASED_CONNECTION_REQ packet contains only one SCID.

2. Perform either alternative 2A, 2B, or 2C depending on the IUT’s response. Alternative 2A (IUT disconnects the connection):

- 2A.1 The IUT disconnects the ACL connection. 2A.2 The IUT and the Lower Tester create an ACL connection.

- Alternative 2B (IUT ignores the C-frame):

- 2B.1 The IUT discards the frame.

- Alternative 2C (IUT rejects the C-frame): 2C.1 The IUT sends an L2CAP_COMMAND_REJECT_RSP to the Lower Tester with a valid Reason code.

3. The Lower Tester sends a C-frame to the IUT with PDU Length = 18, Channel ID set to the correct signaling channel for the logical link, and the Information payload containing a correct L2CAP_CREDIT_BASED_CONNECTION_REQ packet (of length 14 bytes), padded with “0”s. The L2CAP_CREDIT_BASED_CONNECTION_REQ packet contains only one SCID.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **69 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

4. The IUT sends a correctly formatted L2CAP_CREDIT_BASED_CONNECTION_RSP to the Lower Tester and an L2CAP_COMMAND_REJECT_RSP rejecting the partial packet, with Reason = 0x0000 (“Command not understood”).

5. The Lower Tester sends a correctly formatted C-frame to the IUT with valid PDU Length and Channel ID set to the correct signaling channel for the logical link.

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_CREDIT_BASED_CONNECTION_RSP only in response to the second C-frame.

In Step 5, the IUT correctly handles the received C-frame.

## **4.10.7 Enhanced Credit Based Flow Control Mode**

Verify the correct implementation of the data channel in Enhanced Credit Based Flow Control mode.

## **4.10.7.1 Segmentation**

- Test Purpose

Verify that the IUT can send data segments that are larger than the K-frame payload size.

- Reference

- [13] 3.4

- Initial Condition

- The signaling channel specified in Table 4.15 is used.

- An SPSM for the desired Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- A Data Channel as specified in Table 4.15 is established on the SPSM declared via the TSPX_spsm IXIT value with credits returned to the IUT by the Lower Tester.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The Upper Tester can command the IUT to send data.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/COS/ECFC/BV-01-C[Segmentation, LE]|0x0005|
|L2CAP/COS/ECFC/BV-05-C[Segmentation, BR/EDR]|0x0001|

_Table 4.15: Segmentation test cases_

- Test Procedure

Same as for L2CAP/COS/CFC/BV-01-C [Segmentation].

-

- Expected Outcome

## Pass verdict

The IUT sends at least one K-frame containing data to the Lower Tester.

If the Upper Test sends a data packet to the IUT larger than the Lower Tester’s MPS and smaller than the Lower Tester’s MTU, the IUT segments the K-frames correctly.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **70 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.10.7.2 Reassembling**

- Test Purpose

Verify that the IUT can correctly reassemble data received from the Lower Tester where the L2CAP SDU Length is greater than the IUT K-frame payload size.

- Reference

- [13] 3.4

- Initial Condition

- The signaling channel specified in Table 4.16 is used.

- An SPSM for the desired Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- A Data Channel as specified in Table 4.16 is established on the SPSM declared via the TSPX_spsm IXIT value with credits returned to the IUT by the Lower Tester.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/COS/ECFC/BV-02-C[Reassembling, LE]|0x0005|
|L2CAP/COS/ECFC/BV-06-C[Reassembling, BR/EDR]|0x0001|

## _Table 4.16: Reassembling test cases_

- Test Procedure

Same as for L2CAP/COS/CFC/BV-03-C [Reassembling].

-

- Expected Outcome

## Pass verdict

The IUT correctly reassembles the data received from the Lower Tester and sends it to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## **4.10.7.3 Multiple Channels with Interleaved Data Streams**

- Test Purpose

Verify that an IUT can create multiple channels and receives data streams on the channels when the streams are interleaved.

- Reference

[13] 4.25

-

- Initial Condition

- The signaling channel specified in Table 4.17 is used.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **71 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- An SPSM for the desired Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value, send data and credits.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/COS/ECFC/BV-03-C [Multiple Channels with Interleaved Data<br>Streams, LE]|0x0005|
|L2CAP/COS/ECFC/BV-07-C [Multiple Channels with Interleaved Data<br>Streams, BR/EDR]|0x0001|

_Table 4.17: Multiple Channels with Interleaved Data Streams test cases_

- Test Procedure

**==> picture [342 x 306] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>L2CAP_Credit_Based_Connection_Req (two channels)<br>(Code = 0x17, SPSM, SCID = [X, Y],<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, DCID = [A, B], Initial Credits,<br>Result = 0)<br>Two L2CAP channels on relevant SPSM have been established between IUT and Lower Tester<br>L2CAP_Flow_ControlCredit Increment_Credit_Ind<br>K Frame (CID = XA)<br>K Frame (CID = YB)<br>K Frame (CID = XA)<br>K Frame (CID = YB)<br>Data from CID XA<br>K Frame (CID = XA)<br>Data from CID YB<br>**----- End of picture text -----**<br>

_Figure 4.33: Multiple Channels with Interleaved Data Streams MSC_

1. The Upper Tester commands the IUT to send a connection request on the SPSM, with two channels.

2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) to the Lower Tester, with two valid CIDs, on the SPSM.

3. The Lower Tester responds with an L2CAP Credit Based Connection Response (Code = 0x18), establishing all channels.

4. The Lower Tester sends K-Frames to the IUT, alternatively on the two established channels.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **72 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT sends the received data to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## **4.10.7.4 Reassembling**

- Test Purpose

Verify that the IUT can correctly report data received from the Lower Tester when MTU = MPS in the direction from the Lower Tester to the IUT and the data received length = MTU.

- Reference

- [13] 3.4

- Initial Condition

- The signaling channel specified in Table 4.18 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- A Data Channel as specified in Table 4.18 is established on SPSM declared via the TSPX_spsm IXIT value with credits returned to the IUT by the Lower Tester.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/COS/ECFC/BV-04-C[Reassembling, LE]|0x0005|
|L2CAP/COS/ECFC/BV-08-C[Reassembling, BR/EDR]|0x0001|

_Table 4.18: Reassembling test cases_

- Test Procedure

Same as for L2CAP/COS/CFC/BV-04-C [Data Receiving]. The Credit Based Connection Request includes the MTU and MPS parameters set to the same value that is between the minimum and the IUT’s MTU read by the Lower Tester. The length of the data sent by the Lower Tester is the same size as the MTU/MPS parameters in the Credit Based Connection Request.

-

- Expected Outcome

## Pass verdict

The IUT correctly reports the data received from the Lower Tester to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **73 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.11 Connection-Oriented Retransmission/Flow Control/Streaming modes**

Verify the correct implementation of the features of the Retransmission, Flow Control, and Streaming modes of the connection-oriented L2CAP service.

## **4.11.1 Flow Control**

Verify the correct implementation of the Flow Control feature.

## **L2CAP/COS/FLC/BV-01-C [Flow Control without Acks]**

- Test Purpose

Verify that the IUT does not transmit packets with sequence numbers higher than flow control window when no acknowledgment is received.

- Reference

- [1] 5.4, 7.4

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.

- Test Procedure

**==> picture [340 x 267] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Flow Control mode.<br>Command the IUT to send data<br>I-frame<br>N(S)=0 N(R)=0<br>RetransmissionTimer of the IUT<br>I-frame<br>N(S)=1 N(R)=0<br>I-frame<br>N(S)=n-1 N(R)=0<br>Tester to verify that the IUT does<br>not transmit packets with N(S)<br>higher than flow control<br>transmission window (n).<br>I-frame<br>N(S)=n N(R)=0<br>**----- End of picture text -----**<br>

_Figure 4.34: L2CAP/COS/FLC/BV-01-C [Flow Control without Acks] MSC_

- Expected Outcome

## Pass verdict

The IUT does not send any I-frames when the TxWindow is full until the RetransmissionTimer, which has been started with the sending of the first I-frame (N(S)=0), expires.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **74 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/COS/FLC/BV-02-C [Resume Flow on RR Frame Ack]**

- Test Purpose

Verify that the IUT resumes transmission on reception of acknowledgment in an RR frame.

- Reference

[1] 5.4, 7.4

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.

- Test Procedure

**==> picture [340 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Flow Control mode.<br>Command the IUT to send data<br>I-frame<br>N(S)=0 N(R)=0<br>RetransmissionTimer of the IUT<br>I-frame<br>N(S)=1 N(R)=0<br>I-frame<br>N(S)=n-1 N(R)=0<br>Tester to verify that the IUT does<br>not transmit packets with N(S)<br>higher than flow control<br>transmission window (n).<br>RR frame<br>N(R)=1<br>I-frame<br>N(S)=n N(R)=0<br>**----- End of picture text -----**<br>

_Figure 4.35: L2CAP/COS/FLC/BV-02-C [Resume Flow on RR Frame Ack] MSC_

- Expected Outcome

## Pass verdict

The IUT does not send any I-frames when the TxWindow is full and the IUT RetransmissionTimer, which has been started with the sending of the first I-frame (N(S)=0), has not expired yet.

The IUT resumes transmission when it receives acknowledgment for the first I-frame in a RR frame before IUT Retransmission time-out.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **75 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/COS/FLC/BV-03-C [Resume Flow on I-frame Ack]**

- Test Purpose

Verify that the IUT resumes transmission on the reception of acknowledgment in an I-frame.

- Reference

- [1] 5.4, 7.4

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.

- Test Procedure

**==> picture [340 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Flow Control mode.<br>Command the IUT to send data<br>I-frame<br>N(S)=0 N(R)=0<br>RetransmissionTimer of the IUT<br>I-frame<br>N(S)=1 N(R)=0<br>I-frame<br>N(S)=n-1 N(R)=0<br>Tester to verify that the IUT<br>does not transmit packets with<br>N(S) higher than flow control<br>transmission window (n).<br>I-frame<br>N(S)=0 N(R)=1<br>I-frame<br>N(S)=n N(R)=0 or 1<br>**----- End of picture text -----**<br>

_Figure 4.36: L2CAP/COS/FLC/BV-03-C [Resume Flow on I-frame Ack] MSC_

- Expected Outcome

## Pass verdict

The IUT does not send any I-frames when the TxWindow is full and the RetransmissionTimer, which has been started with the sending of the first I-frame (N(S)=0), has not expired yet.

The IUT resumes transmission when it receives an acknowledgment for the first I-frame in an I-frame sent by the Lower Tester before IUT Retransmission time-out.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **76 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/COS/FLC/BV-04-C [Transmit RR Frame on Monitor Timeout]**

- Test Purpose

Verify that the IUT transmits an RR frame after Monitor time-out.

- Reference

- [1] 5.4, 7.4

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.

- Test Procedure

**==> picture [340 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Flow Control mode.<br>Command the IUT to send 1 I-frame<br>I-frame<br>N(S)=0 N(R)=0<br>RR frame<br>N(R)=1<br>Monitor<br>Time-out<br>RR frame<br>N(R)=0<br>**----- End of picture text -----**<br>

_Figure 4.37: L2CAP/COS/FLC/BV-04-C [Transmit RR Frame on Monitor Timeout] MSC_

- Expected Outcome

## Pass verdict

The Lower Tester receives the IUT’s RR frame within the timing window, [Monitor Time-out (+/- 10%)], after transmission of its own RR frame.

-

- Notes

The 10 percent timing window is to account for timing differences between IUT and Lower Tester, as well as minor measurement error.

## **4.11.2 Retransmission**

Verify the correct implementation of the retransmission feature.

## **L2CAP/COS/RTX/BV-01-C [No Retransmission with R=1]**

- Test Purpose

Verify that the IUT does not retransmit packets when the retransmission flag is set to R=1.

- Reference

- [1] 5.3, 7.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **77 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Retransmission mode.

- Test Procedure

**==> picture [341 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Retransmission mode.<br>Tester Retransmission Command the IUT to send data<br>Timer =IUT Retransmission<br>Time-out<br>I-frame<br>After receiving RR frame with<br>N(S)=0 N(R)=0 R=1, IUT's Retransmission<br>Monitor timer Timer should be stopped.<br>of the Tester RR frame<br>N(R)=0 R=1<br>Optional<br>Repeat RR frame<br>N(R)=0 R=1<br>To be transmitted every<br>Tester Monitor time-out until<br>Delay = Tester to verify that the IUT Tester Retransmission Timer<br>Monitor Time-out does not retransmit I-frame expires.<br>with N(S)=0.<br>RR frame<br>N(R)=1 R=0<br>**----- End of picture text -----**<br>

_Figure 4.38: L2CAP/COS/RTX/BV-01-C [No Retransmission with R=1] MSC_

- Expected Outcome

## Pass verdict

The IUT does not retransmit an I-frame with sequence number N(S)=0 after IUT Retransmission timeout when the latest received R bit in a RR frame is 1.

## **L2CAP/COS/RTX/BV-02-C [Retransmission with R=0 in RR frame]**

- Test Purpose

Verify that the IUT retransmits packets after retransmission time-out when the retransmission flag is set to R=0 received in a RR frame.

- Reference

- [1] 5.3, 7.4

-

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Retransmission mode.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **78 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [299 x 290] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Retransmission mode.<br>Command the IUT to send data<br>I-frame<br>N(S)=0 N(R)=0<br>RR frame RetransmissionTimer of<br>Monitor N(R)=0 R=0 the IUT<br>timer of the<br>Tester<br>Optional<br>Repeat RR frame<br>N(R)=0 R=0<br>I-frame<br>N(S)=0 N(R)=0<br>RR frame<br>To be transmitted every<br>N(R)=1 R=1 Tester Monitor time-out until<br>IUT Retransmission time-out<br>expires.<br>**----- End of picture text -----**<br>

_Figure 4.39: L2CAP/COS/RTX/BV-02-C [Retransmission with R=0 in RR frame] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits an I-frame with sequence number N(S)=0 after IUT Retransmission time-out when the latest received R bit in a RR frame is 0.

## **L2CAP/COS/RTX/BV-03-C [Retransmission with R=0 in I-frame]**

- Test Purpose

Verify that the IUT retransmits packets after retransmission time-out when retransmission flag is set to R=0 received in an I-frame.

- Reference

- [1] 5.3, 7.4

-

- Initial Condition

- The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Retransmission mode.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **79 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [297 x 239] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in OPEN state. Retransmission mode.<br>Command the IUT to send data<br>I-frame<br>N(S)=0 N(R)=0<br>I-frame RetransmissionTimer<br>N(S)=0 N(R)=0 R=0 of the IUT<br>I-frame<br>N(S)=0<br>RR frame<br>N(R)=1 R=1<br>**----- End of picture text -----**<br>

_Figure 4.40: L2CAP/COS/RTX/BV-03-C [Retransmission with R=0 in I-frame] MSC_

- Expected Outcome

Pass verdict

The IUT retransmits I-frame with sequence number N(S)=0 after IUT Retransmission time-out when latest received R bit in a I-frame is 0.

## **4.11.3 Extended Features (EXF)**

Verify the correct implementation of the extended features information requests and responses of the L2CAP layer.

## **L2CAP/EXF/BV-07-C [Extended Features Information Response]**

- Test Purpose

Verify that the IUT can format an Information Response for the information type of Extended Features.

- Reference

[1] 4.10, 4.11, 4.12

-

- Initial Condition

- An ACL connection has been established by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **80 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [248 x 102] intentionally omitted <==**

_Figure 4.41: L2CAP/EXF/BV-07-C [Extended Features Information Response] MSC_

- Expected Outcome

## Pass verdict

The IUT sends Information Response [InfoType = Extended Features] and with a result code of Success and containing extended features supported defined by the ICS as mapped by Table 3.1 in [5].

## **L2CAP/EXF/BV-08-C [Information Request, Extended Features]**

- Test Purpose

Verify that the IUT returns the proper L2CAP Extended Features in response to the Information Request from the Lower Tester.

- Reference

- [11] 4.10

- Initial Condition

- The IUT is in the CLOSED state.

- No ACL link exists.

- The IUT acts as an L2CAP acceptor.

- Test Procedure

The Lower Tester sends an information request to the IUT.

**==> picture [355 x 95] intentionally omitted <==**

_Figure 4.42: L2CAP/EXF/BV-08-C [Information Request, Extended Features] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **81 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_INFORMATION_RSP PDU to the Lower Tester with the Info parameter containing 4 octets that match the ICS entries as shown in Table 4.19 and all bits not listed are set to 0b0.

|**Feature**|**Octet**|**Bit**|**ICS**|
|Flow Control mode|0|0|L2CAP 2/11|
|Retransmission mode|0|1|L2CAP 2/10|
|Bi-directional QoS|0|2|L2CAP 3/7|
|Enhanced Retransmission mode|0|3|L2CAP 2/12|
|Streamingmode|0|4|L2CAP 2/13|
|FCS Option|0|5|L2CAP 2/14|
|Extended Flow Specification for BR/EDR|0|6|L2CAP 2/38|
|Fixed Channels supported over BR/EDR|0|7|L2CAP 2/30|
|Extended Window Size|1|0|L2CAP 2/39|
|Unicast Connectionless Data Reception|1|1|L2CAP 2/35|
|Enhanced Credit Based Flow Control mode over BR/EDR|1|2|L2CAP 2/48a|

_Table 4.19: Extended Feature Mask bits_

- Notes

The Lower Tester’s RTX timer is set to maximum allowed initial value.

## **4.11.4 Channel Mode Configuration (CMC)**

Verify the configuration of L2CAP channels using the various L2CAP supported modes.

## **L2CAP/CMC/BV-01-C [IUT Initiated Configuration of Enhanced Retransmission Mode]**

- Test Purpose

Verify that the IUT can send a Configuration Request command containing the F&EC option that specifies Enhanced Retransmission Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has been established by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **82 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [342 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in CONFIG State. Tester has not sent L2CAP_ConfigReq<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>Mode = Enhanced Retransmission Mode<br>Configuration Timer<br>(120 Seconds)<br>L2CAP_ConfigRsp<br>Result = Success<br>**----- End of picture text -----**<br>

_Figure 4.43: L2CAP/CMC/BV-01-C [IUT Initiated Configuration of Enhanced Retransmission Mode] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP Configure Request for Enhanced Retransmission Mode before the Lower Tester configuration timer (120 seconds) expires.

**L2CAP/CMC/BV-02-C [Lower Tester Initiated Configuration of Enhanced Retransmission Mode]**

- Test Purpose

Verify that the IUT can accept a Configuration Request from the Lower Tester containing an F&EC option that specifies Enhanced Retransmission Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- Test L2CAP/CMC/BV-01-C [IUT Initiated Configuration of Enhanced Retransmission Mode] has been performed successfully.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **83 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 195] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in WAIT_CONFIG_REQ CONFIG sub-state.<br>L2CAP_ConfigReq<br>Mode = Enhanced Retransmission Mode<br>RTX Timer<br>(5 Seconds)<br>L2CAP_ConfigRsp<br>Result = Success<br>**----- End of picture text -----**<br>

_Figure 4.44: L2CAP/CMC/BV-02-C [Lower Tester Initiated Configuration of Enhanced Retransmission Mode] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigRsp before the Lower Tester TSPX_timer_rtx timer expires with a result code of “Success.”

**L2CAP/CMC/BV-03-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Optional]**

- Test Purpose

When configuring a PSM that can optionally support ERTM, verify that the IUT can handle receipt (renegotiate the channel mode in accordance with the specification) of a Configure Response indicating the peer L2CAP entity doesn’t wish to use Enhanced Retransmission Mode (Configure Response Result = Reject Unacceptable Parameters).

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **84 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

|Configuration<br>(120 Seco<br>Configuration<br>(120 Seco|Lower|Tester||IUT|IUT||Upper Tester|Upper Tester|
|||IUT is not yet in CONFIG State. Tester ha|||s not sent L2CAP_ConfigReq||||
|||L2CAP_CONNECTION_RSP|||<br> <br>||||
|||L2CAP_ConfigReq|||||||
||Timer<br>nds)|L2CAPConfigRsp<br><br>(F&EC Option [<br>Channel Mode = ERTM<br>Other Option fields = ANY])|||||||
|||_<br>(Result = 0x0001 (Unacceptable Params)<br>F&EC Option<br>- Channel Mode = Basic Mode<br>- Other Option fields = Basic Mode values)<br>L2CAP_ConfigReq|||||||
||Timer<br>nds)|(F&EC Option [<br>Channel mode = Basic mode OR omitted<br>Other Option fields = Basic mode values OR omitted])<br>L2CAP_ConfigRsp|||||||
|||(Result = Success)<br>L2CAP_ConfigReq|||||||
|||(F&EC Option<br>- Channel Mode = Basic Mode<br>- Other Option fields = Basic Mode values)<br>L2CAP_ConfigRsp|||||||
|||(Result = Success)|||||||

_Figure 4.45: L2CAP/CMC/BV-03-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Optional] MSC_

- Expected Outcome

Pass verdict

The channel is successfully configured to Basic Mode.

## **L2CAP/CMC/BV-04-C [IUT Initiated Configuration of Streaming Mode]**

- Test Purpose

Verify that the IUT can send a Configuration Request command containing the F&EC option that specifies Streaming Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports the Streaming Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has been established by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **85 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 183] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG State. Tester has not sent L2CAP_ConfigReq<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>Mode = Streaming Mode<br>Configuration Timer<br>(120 Seconds)<br>L2CAP_ConfigRsp<br>Result = Success<br>**----- End of picture text -----**<br>

_Figure 4.46: L2CAP/CMC/BV-04-C [IUT Initiated Configuration of Streaming Mode] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP Configure Request for Streaming Mode before the Lower Tester Configuration Timer (120 seconds) expires.

## **L2CAP/CMC/BV-05-C [Lower Tester Initiated Configuration of Streaming Mode]**

- Test Purpose

Verify that the IUT can accept a Configuration Request from the Lower Tester containing an F&EC option that specifies Streaming Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- Test L2CAP/CMC/BV-04-C [IUT Initiated Configuration of Streaming Mode] has been performed successfully.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **86 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 195] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in WAIT_CONFIG_REQ CONFIG sub-state.<br>L2CAP_ConfigReq<br>Mode = Streaming Mode<br>RTX Timer<br>(5 Seconds)<br>L2CAP_ConfigRsp<br>Result = Success<br>**----- End of picture text -----**<br>

_Figure 4.47: L2CAP/CMC/BV-05-C [Lower Tester Initiated Configuration of Streaming Mode] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigRsp before the Lower Tester RTX timer expires with a result code of “Success.”

**L2CAP/CMC/BV-06-C [Failed Configuration of Streaming Mode when use of the Mode is Optional]**

- Test Purpose

When configuring a PSM that can optionally support Streaming Mode, verify that the IUT can handle receipt (renegotiate the channel mode in accordance with the specification) of a Configure Response indicating the peer L2CAP entity does not wish to use the tested mode (Configure Response Result = Reject Unacceptable Parameters).

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **87 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

**==> picture [340 x 385] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Streaming Mode<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigRsp<br>(Result = 0x0001 (Unacceptable Params)<br>F&EC Option<br> - Channel Mode = Basic Mode<br> - Other Option fields = Basic Mode values)<br>L2CAP _Confi gRe q<br>(F&EC Option [<br>Configuration Timer Channel mode = Basic mode OR omitted<br>(120 Seconds) Other Option fields = Basic mode values OR omitted] )<br>L2CAP_ConfigRsp<br>(Result = Success)<br>L2CAP_ConfigReq<br>(F&EC Option<br> - Channel Mode = Basic Mode<br> - Other Option fields = Basic Mode values)<br>L2CAP_ConfigRsp<br>(Result = Success)<br>**----- End of picture text -----**<br>

_Figure 4.48: L2CAP/CMC/BV-06-C [Failed Configuration of Streaming Mode when use of the Mode is Optional] MSC_

- Expected Outcome

## Pass verdict

The channel is successfully configured to Basic Mode.

**L2CAP/CMC/BV-07-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Optional]**

- Test Purpose

When configuring a PSM that can optionally support the use of ERTM, verify that the IUT renegotiates the channel mode to Basic Mode if the Lower Tester attempts to configure Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **88 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

- Test Procedure

**==> picture [341 x 335] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.IUT is in CONFIG State. Tester has not sent L2CAP_ConfigReq<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = ERTM<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = Basic Mode<br>(5 Seconds) - Other Option fields = Basic Mode values)<br>L2CAP_ConfigRsp<br>(Result = Success)<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params<br>F&EC Option<br> - Channel Mode = Basic Mode<br> - Other Option fields = Basic Mode values)<br>L2CAP _Confi gRe q<br>(F&EC Option [<br>Channel mode = Basic mode OR omitted<br>Other Option fields = Basic mode values OR omitted] )<br>Configuration Timer<br>(120 Seconds) L2CAP_ConfigRsp<br>(Result = Success)<br>**----- End of picture text -----**<br>

_Figure 4.49: L2CAP/CMC/BV-07-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Optional] MSC_

- Expected Outcome

## Pass verdict

The channel is successfully configured to Basic Mode.

**L2CAP/CMC/BV-08-C [Configuration Mode Mismatch when use of Streaming Mode is Optional]**

- Test Purpose

When configuring a PSM that can optionally support the use of Streaming Mode, verify that the IUT renegotiates the channel mode to Basic Mode if the Lower Tester attempts to configure Basic Mode.

- Reference

- [1] 4.4, 4.5, 5.4, 6.1.4, 7.1

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **89 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

- Test Procedure

**==> picture [341 x 337] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Streaming Mode<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = Basic Mode<br>(5 Seconds) - Other Option fields = Basic Mode values)<br>L2CAP_ConfigRsp<br>(Result = Success)<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params<br>F&EC Option<br> - Channel Mode = Basic Mode<br> - Other Option fields = Basic Mode values)<br>L2CAP _Confi gRe q<br>(F&EC Option [<br>Channel mode = Basic mode OR omitted<br>Other Option fields = Basic mode values OR omitted] )<br>Configuration Timer<br>(120 Seconds) L2CAP_ConfigRsp<br>(Result = Success)<br>**----- End of picture text -----**<br>

_Figure 4.50: L2CAP/CMC/BV-08-C [Configuration Mode Mismatch when use of Streaming Mode is Optional] MSC_

- Expected Outcome

## Pass verdict

The channel is successfully configured to Basic Mode.

## **L2CAP/CMC/BV-09-C [Configuration to Basic Mode by the IUT]**

- Test Purpose

The IUT wishes to use Basic Mode when configuring a PSM that can optionally support the use of ERTM or Streaming Mode. Verify that the IUT correctly rejects the request for ERTM or Streaming Mode from the Lower Tester.

- Reference

- [1] 4.4, 4.5, 5.4, 6.1.4, 7.1

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **90 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The Lower Tester has determined which Enhanced L2CAP Mode the IUT supports (using the Information Request/Response [Extended Features] mechanism). If the IUT supports both, the Lower Tester attempts to configure ERTM.

- The channel connection has completed.

- Test Procedure

**==> picture [342 x 341] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Basic Mode OR Omitted<br>(120 Seconds) Other Option fields = Basic mode values OR<br>Omitted])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = ERTM or STM<br>(5 Seconds) - Other Option fields = ANY)<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params<br>(F&EC Option [<br> Channel Mode = Basic Mode<br>Other Option fields = Basic Mode values])<br>L2CAP_ConfigRsp<br>(Result = Success)<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = Basic Mode<br>(5 Seconds) - Other Option fields = Basic Mode Values)<br>L2CAP_ConfigRsp<br>(Result = Success)<br>**----- End of picture text -----**<br>

_Figure 4.51: L2CAP/CMC/BV-09-C [Configuration to Basic Mode by the IUT] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a Configure Response with result code of Unacceptable Parameters to the request from the Lower Tester for ERTM or STM.

The channel is successfully configured for Basic Mode.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **91 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/CMC/BI-01-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Mandatory]**

- Test Purpose

When creating a connection for a PSM that mandates the use of ERTM, verify that the IUT can handle receipt (close the channel in accordance with the specification) of a Configure Response indicating the peer L2CAP entity does not wish to use Enhanced Retransmission Mode (Configure Response Result = Reject Unacceptable Parameters).

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

- Test Procedure

**==> picture [341 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = ERTM<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params<br>F&EC Option<br> - Channel Mode = Basic Mode<br> - Other Option fields = Basic Mode values)<br>L2CAP_DisconnectReq<br>Configuration Timer<br>(120 Seconds)<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.52: L2CAP/CMC/BI-01-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Mandatory] MSC_

- Expected Outcome

## Pass verdict

The IUT initiates closure of the channel.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **92 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/CMC/BI-02-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Mandatory]**

- Test Purpose

When creating a connection for a PSM that mandates the use of ERTM, verify that the IUT closes the channel if the Lower Tester attempts to configure Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

- Test Procedure

**==> picture [341 x 246] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = ERTM<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = Basic Mode<br>(5 Seconds) - Other Option fields = Basic Mode values)<br>L2CAP_DisconnectReq<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.53: L2CAP/CMC/BI-02-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Mandatory] MSC_

- Expected Outcome

## Pass verdict

The IUT initiates closure of the channel.

**L2CAP/CMC/BI-03-C [Failed Configuration of Streaming Mode when use of the Mode is Mandatory]**

- Test Purpose

When creating a connection for a PSM that mandates the use of Streaming Mode, verify that the IUT can handle receipt (close the channel in accordance with the specification) of a Configure Response indicating the peer L2CAP entity does not wish to use Streaming Mode (Configure Response Result = Reject Unacceptable Parameters).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **93 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

- Test Procedure

**==> picture [340 x 291] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Streaming Mode<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params<br>F&EC Option<br> - Channel Mode = Basic Mode<br> - Other Option fields = Basic Mode values)<br>L2CAP_DisconnectReq<br>Configuration Timer<br>(120 Seconds)<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.54: L2CAP/CMC/BI-03-C [Failed Configuration of Streaming Mode when use of the Mode is Mandatory] MSC_

- Expected Outcome

## Pass verdict

The IUT initiates closure of the channel.

## **L2CAP/CMC/BI-04-C [Configuration Mode mismatch when use of Streaming Mode is Mandatory]**

- Test Purpose

When creating a connection for a PSM that mandates the use of Streaming Mode, verify that the IUT closes the channel if the Lower Tester attempts to configure Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **94 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

- Test Procedure

**==> picture [341 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Streaming Mode<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = Basic Mode<br>(5 Seconds) - Other Option fields = Basic Mode values)<br>L2CAP_DisconnectReq<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.55: L2CAP/CMC/BI-04-C [Configuration Mode mismatch when use of Streaming Mode is Mandatory] MSC_

- Expected Outcome

## Pass verdict

The IUT initiates closure of the channel.

## **L2CAP/CMC/BI-05-C [Failed Configuration to Basic Mode by the IUT]**

- Test Purpose

The IUT wishes to use Basic Mode when configuring a PSM that can optionally support the use of ERTM or Streaming Mode. Verify that the IUT initiates channel closure if the Lower Tester refuses to negotiate the channel to Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The Lower Tester has determined which Enhanced L2CAP Mode the IUT supports (using the Information Request/Response [Extended Features] mechanism). If the IUT supports both, the Lower Tester attempts to configure ERTM.

- The channel connection has completed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **95 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 336] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Basic Mode OR Omitted<br>(120 Seconds) Other Option fields = Basic mode values OR<br>Omitted])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = ERTM or STM<br>(5 Seconds) - Other Option fields = ANY)<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params<br>(F&EC Option [<br> Channel Mode = Basic Mode<br>Other Option fields = Basic Mode values])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = ERTM or STM<br>(5 Seconds) - Other Option fields = ANY)<br>L2CAP_DisconnectReq<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.56: L2CAP/CMC/BI-05-C [Failed Configuration to Basic Mode by the IUT] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a Configure Response with result code of Unacceptable Parameters to the request from the Lower Tester for ERTM.

The IUT initiates closure of the channel when it receives the second Configure Request for ERTM from the Lower Tester.

## **L2CAP/CMC/BI-06-C [Configuration to Basic Mode Rejected by the Lower Tester]**

- Test Purpose

The IUT wishes to use Basic Mode when configuring a PSM that can optionally support the use of ERTM or Streaming Mode. Verify that the IUT initiates channel closure if the Lower Tester rejects the IUT configure request for Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **96 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The Lower Tester has determined which Enhanced L2CAP Mode the IUT supports (using the Information Request/Response [Extended Features] mechanism). If the IUT supports both, the Lower Tester attempts to configure ERTM.

- The channel connection has completed.

- Test Procedure

**==> picture [342 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel mode = Basic mode OR omitted<br>(120 Seconds) Other Option fields = Basic mode values OR<br>omitted] )<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params,<br>RTX Timer F&EC Option<br>(5 Seconds) - Channel Mode = ERTM OR STM<br> - Other Option fields = ANY)<br>L2CAP_DisconnectReq<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.57: L2CAP/CMC/BI-06-C [Configuration to Basic Mode Rejected by the Lower Tester] MSC_

- Expected Outcome

## Pass verdict

The IUT initiates closure of the channel when it receives the Configure Response rejecting Basic Mode from the Lower Tester.

## **L2CAP/CMC/BV-10-C [ERTM Not Supported by Lower Tester for Optional ERTM Channel]**

- Test Purpose

The IUT is initiating connection of a L2CAP channel that can optionally support use of ERTM. Verify that the IUT attempts to configure Basic Mode if the Lower Tester does not indicate support for ERTM in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 4.10, 4.11, 4.12, 5.4, 6.1.4, 7.1

- Initial Condition

- An ACL connection has been established by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **97 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [339 x 271] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established<br>Create Connection<br>(ERTM Optional)<br>L2CAP_InfoReq<br>(InfoType = Extended Features)<br>RTX Timer<br>L2CAP_InfoRsp<br>(InfoType = Extended Features<br>Extended Feature Mask ERTM bit = 0)<br>L2CAP_CONNECTION_REQ<br>RTX Timer<br>L2CAP_CONNECTION_RSP<br>(Result = Success)<br>L2CAP _Confi gReq<br>(F&EC Option [<br>Configuration Timer Channel mode = Basic mode OR omitted<br>(120 Seconds) Other Option fields = Basic mode values OR omitted] )<br>**----- End of picture text -----**<br>

_Figure 4.58: L2CAP/CMC/BV-10-C [ERTM Not Supported by Lower Tester for Optional ERTM Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT opens the L2CAP channel to the Lower Tester.

The IUT attempts to configure the channel to Basic Mode.

**L2CAP/CMC/BV-11-C [Streaming Mode not supported by Lower Tester for Optional Streaming Mode Channel]**

- Test Purpose

The IUT is initiating connection of an L2CAP channel that can optionally support use of STM. Verify that the IUT attempts to configure Basic Mode if the Lower Tester does not indicate support for STM in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 4.10, 4.11, 4.12, 5.4, 6.1.4, 7.1

- Initial Condition

- An ACL connection has been established by the Lower Tester

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **98 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [343 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established<br>Create Connection<br>(STM Optional)<br>L2CAP_InfoReq<br>(InfoType = Extended Features)<br>RTX Timer<br>L2CAP_InfoRsp<br>(InfoType = Extended Features<br>Extended Feature Mask STM bit = 0)<br>L2CAP_CONNECTION_REQ<br>RTX Timer<br>L2CAP_CONNECTION_RSP<br>(Result = Success)<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel mode = Basic mode OR omitted<br>(120 Seconds) Other Option fields = Basic mode values OR<br>omitted] )<br>**----- End of picture text -----**<br>

_Figure 4.59: L2CAP/CMC/BV-11-C [Streaming Mode not supported by Lower Tester for Optional Streaming Mode Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT opens the L2CAP channel to the Lower Tester.

The IUT attempts to configure the channel to Basic Mode.

## **L2CAP/CMC/BV-12-C [ERTM Not Supported by Lower Tester for Mandatory ERTM channel]**

- Test Purpose

The IUT is initiating connection of an L2CAP channel that mandates use of ERTM. Verify that the IUT does not attempt to configure the connection to ERTM if the Lower Tester has not indicated support for ERTM in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 4.10, 4.11, 4.12, 5.4, 6.1.4, 7.1

- Initial Condition

- An ACL connection has been established by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **99 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [306 x 202] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established<br>Create Connection<br>(ERTM Mandatory)<br>L2CAP_CONNECTION_REQ (optional)<br>L2CAP_CONNECTION_RSP (success)<br>L2CAP_InfoReq<br>(InfoType = Extended Features) RTX Timer<br>L2CAP_InfoRsp<br>(InfoType = Extended Features<br>Extended Feature Mask ERTM bit = 0)<br>Create Connection<br>(Failure – ERTM not<br>supported by peer)<br>**----- End of picture text -----**<br>

_Figure 4.60: L2CAP/CMC/BV-12-C [ERTM Not Supported by Lower Tester for Mandatory ERTM channel] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT does not attempt to configure the connection to the unsupported mode of the Lower Tester and informs the Upper Tester that the connection has failed.

**L2CAP/CMC/BV-13-C [Streaming Mode not supported by Lower Tester for Mandatory Streaming Mode Channel]**

- Test Purpose

The IUT is initiating connection of an L2CAP channel that mandates use of STM. Verify that the IUT does not attempt to configure the connection to STM if the Lower Tester has not indicated support for STM in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 4.10, 4.11, 4.12, 5.4, 6.1.4, 7.1

- Initial Condition

- An ACL connection has been established by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **100 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [306 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established<br>Create Connection<br>(STM Mandatory)<br>L2CAP_CONNECTION_REQ (optional)<br>L2CAP_CONNECTION_RSP (success)<br>L2CAP_InfoReq<br>(InfoType = Extended Features) RTX Timer<br>L2CAP_InfoRsp<br>(InfoType = Extended Features<br>Extended Feature Mask STM bit = 0)<br>Create Connection<br>(Failure – STM not<br>supported by peer)<br>**----- End of picture text -----**<br>

_Figure 4.61: L2CAP/CMC/BV-13-C [Streaming Mode not supported by Lower Tester for Mandatory Streaming Mode Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT does not attempt to configure the connection to the unsupported mode of the Lower Tester and informs the Upper Tester that the connection has failed.

**L2CAP/CMC/BV-14-C [Failed Configuration of Streaming Mode when use of the mode is optional and ERTM is proposed by the Lower Tester]**

- Test Purpose

When configuring a PSM that can optionally support Streaming Mode, verify that the IUT can handle receipt (renegotiate the channel mode in accordance with the specification) of a Configure Response indicating the peer L2CAP entity wishes to use ERTM (Configure Response Result = Reject Unacceptable Parameters).

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **101 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [340 x 372] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Streaming Mode<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigRsp<br>(Result = 0x0001 (Unacceptable Params)<br>F&EC Option<br> - Channel Mode = ERTM<br> - Other Option fields = ANY)<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = ERTM<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigRsp<br>(Result = Success)<br>L2CAP_ConfigReq<br>(F&EC Option<br> - Channel Mode = ERTM<br> - Other Option fields = ANY)<br>L2CAP_ConfigRsp<br>(Result = Success)<br>**----- End of picture text -----**<br>

_Figure 4.62: L2CAP/CMC/BV-14-C [Failed Configuration of Streaming Mode when use of the mode is optional and ERTM is proposed by the Lower Tester] MSC_

- Expected Outcome

## Pass verdict

The channel is successfully configured to Enhanced Retransmission Mode.

**L2CAP/CMC/BV-15-C [Configuration Mode Mismatch when use of Streaming Mode is Optional and ERTM is proposed by the Lower Tester]**

- Test Purpose

When configuring a PSM that can optionally support the use of Streaming Mode, verify that the IUT renegotiates the channel mode to ERTM if the Lower Tester attempts to configure ERTM.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **102 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).

- The channel connection has completed.

- Test Procedure

**==> picture [341 x 335] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is not yet in CONFIG state. Tester has not sent L2CAP_ConfigReq.<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(F&EC Option [<br>Configuration Timer Channel Mode = Streaming Mode<br>(120 Seconds) Other Option fields = ANY])<br>L2CAP_ConfigReq<br>(F&EC Option<br>RTX Timer - Channel Mode = ERTM<br>(5 Seconds) - Other Option fields = ANY)<br>L2CAP_ConfigRsp<br>(Result = Success)<br>L2CAP_ConfigRsp<br>(Result = Unacceptable Params<br>F&EC Option<br> - Channel Mode = ERTM<br> - Other Option fields = ANY)<br>L2CAP_ConfigReq<br>(F&EC Option [<br> Channel Mode = ERTM<br>Other Option fields = ANY])<br>Configuration Timer<br>(120 Seconds) L2CAP_ConfigRsp<br>(Result = Success)<br>**----- End of picture text -----**<br>

_Figure 4.63: L2CAP/CMC/BV-15-C [Configuration Mode Mismatch when use of Streaming Mode is Optional and ERTM is proposed by the Lower Tester] MSC_

- Expected Outcome

## Pass verdict

The channel is successfully configured to Enhanced Retransmission Mode.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **103 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.11.5 Frame Check Sequence (FCS) Option Configuration (FOC)**

Verify the configuration of the FCS option of the L2CAP layer.

## **4.11.5.1 IUT Initiated Configuration of the FCS Option, IUT No FCS**

- Test Purpose

Verify that an IUT that does not support FCS sends S-frame or I-frame PDUs with or without FCS depending on the Lower Tester FCS support.

- Reference

- [1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition

- The initiator IUT has established that the peer L2CAP entity supports configuration of the Optional FCS option (using the Information Request/Response [Extended Features] mechanism).

- Test Case Configuration

|**Test Case**|**FCS Type**<br>**(Lower Tester)**|**IUT**<br>**S/I-Frame FCS**|
|L2CAP/FOC/BV-01-C [IUT Initiated Configuration of the FCS<br>Option, IUT No FCS Option, Lower Tester No FCS Option]|0x00: No FCS|No|
|L2CAP/FOC/BV-02-C [IUT Initiated Configuration of the FCS<br>Option, IUT No FCS Option, Lower Tester Yes FCS Option]|0x01: 16-bit<br>FCS|Yes|
|L2CAP/FOC/BV-03-C [IUT Initiated Configuration of the FCS<br>Option, IUT No FCS Option, Lower Tester Omitted FCS<br>Option]|Omitted|Yes|

_Table 4.20: IUT Initiated Configuration of the FCS Option, IUT No FCS test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **104 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [388 x 398] intentionally omitted <==**

_Figure 4.64: IUT Initiated Configuration of the FCS Option, IUT No FCS MSC_

- Expected Outcome

## Pass verdict

The channel is established.

The IUT sends an S-frame (in response to the S-frame [POLL] from the sender) or an I-frame with or without the FCS field as specified in Table 4.20.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **105 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.11.5.2 IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted**

- Test Purpose

Verify that the IUT sends I/S-frames with the FCS field present when the IUT either supports or omits the FCS type and the Lower Tester supports, does not support, or omits the FCS Type.

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition

- The initiator IUT has established that the peer L2CAP entity supports configuration of the Optional FCS option (using the Information Request/Response [Extended Features] mechanism).

- Test Case Configuration

|**Test Case**|**FCS Type (IUT)**|
|L2CAP/FOC/BV-04-C [IUT Initiated Configuration of the FCS Option,<br>IUT FCS 0x01]|0x01: 16-bit FCS|
|L2CAP/FOC/BV-06-C [IUT Initiated Configuration of the FCS Option,<br>IUT FCS Omitted]|Omitted|

_Table 4.21: IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **106 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [384 x 525] intentionally omitted <==**

_Figure 4.65: IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted MSC_

|**Rounds**|**FCS Type (Lower Tester)**|
|1|0x00: No FCS|
|2|0x01: 16-bit FCS|
|3|Omitted|

_Table 4.22: IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted rounds_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **107 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

Pass verdict

The channel is established.

The IUT sends an S-frame (in response to the S-frame [POLL] from the sender) or an I-frame with the FCS field present.

## **4.11.5.3 IUT Responder, Configuration of the FCS Option**

- Test Purpose

Verify that the IUT can respond to a channel configuration. The IUT is configured to support, not support, or omit the FCS type as specified in Table 4.24 in I/S-frames and will send I/S-frames with the FCS field as specified in Table 4.24.

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition

- The responder IUT has established that the peer L2CAP entity supports configuration of the Optional FCS option (using the Information Request/Response [Extended Features] mechanism).

- Test Case Configuration

|**Test Case**|**FCS Type (IUT)**|**IUT S/I-Frame FCS**|**IUT S/I-Frame FCS**|
|||**Round 1**|**Rounds 2 & 3**|
|L2CAP/FOC/BV-05-C [IUT Responder,<br>Configuration of the FCS Option, IUT FCS<br>0x00]|0x00: No FCS|No|Yes|
|L2CAP/FOC/BV-07-C [IUT Responder,<br>Configuration of the FCS Option, IUT FCS<br>0x01]|0x01: 16-bit FCS|Yes|Yes|
|L2CAP/FOC/BV-08-C [IUT Responder,<br>Configuration of the FCS Option, IUT FCS<br>Omitted]|Omitted|Yes|Yes|

_Table 4.23: IUT Responder, Configuration of the FCS Option test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **108 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [342 x 427] intentionally omitted <==**

_Figure 4.66: IUT Responder, Configuration of the FCS Option MSC_

|**Rounds**|**FCS Type (Lower Tes**|
|1|0x00: No FCS|
|2|0x01: 16-bit FCS|
|3|Omitted|

_Table 4.24: IUT Responder, Configuration of the FCS Option rounds_

- Expected Outcome

Pass verdict

The channel is established.

The IUT sends an S-frame (in response to the S-frame [POLL] from the sender) or an I-frame with the FCS field as specified in Table 4.24.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **109 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.11.6 Optional FCS (OFS)**

Verify the correct implementation of the Optional FCS feature.

## **L2CAP/OFS/BV-01-C [Sending I-Frames without FCS for ERTM]**

- Test Purpose

Verify that the IUT does not include the FCS in I-frames.

- Reference

- [1] 3.3.5, 8.6

- Initial Condition

- The channel is configured to not include FCS in I/S-frames.

- The channel is configured to use ERTM.

- Test Procedure

**==> picture [376 x 150] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM and to not use FCS<br>Test Guard<br>Timer L2CAP_Config_Rsp<br>(30 seconds) Command the IUT to send data<br>I-Frame<br>(N(S) = 0, No FCS)<br>Retransmission<br>S-Frame Timer<br>(RR, N(R) = 1, Poll = 0, No FCS)<br>**----- End of picture text -----**<br>

_Figure 4.67: L2CAP/OFS/BV-01-C [Sending I-Frames without FCS for ERTM] MSC_

- Expected Outcome

Pass verdict

The IUT sends an I-frame without the FCS field.

## **L2CAP/OFS/BV-02-C [Receiving Frames without FCS for ERTM]**

- Test Purpose

Verify that the IUT can handle I-frames that do not contain the FCS.

- Reference

[1] 3.3.5, 8.6

- Initial Condition

- The channel is configured to not include FCS in I/S-frames.

- The channel is configured to use ERTM.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **110 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [377 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM and to not use FCS<br>I-Frame<br>Retransmission (N(S) = 0, No FCS) Received Data passed to Upper Tester<br>Timer<br>S-Frame<br>(RR, N(R) = 1, No FCS)<br>**----- End of picture text -----**<br>

_Figure 4.68: L2CAP/OFS/BV-02-C [Receiving Frames without FCS for ERTM] MSC_

- Expected Outcome

## Pass verdict

The IUT passes the received data to the Upper Tester.

The IUT acknowledges the received I-frame before the Retransmission timer of the Lower Tester expires.

## **L2CAP/OFS/BV-03-C [Sending I-Frames without FCS for Streaming Mode]**

- Test Purpose

Verify that the IUT does not include the FCS in I-frames.

- Reference [1] 3.3.5, 8.7

- Initial Condition

- The channel is configured to not include FCS in I/S-frames.

- The channel is configured to use Streaming Mode.

- Test Procedure

**==> picture [376 x 135] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode and to not use FCS<br>Test Guard<br>Timer L2CAP_Config_Rsp<br>(30 seconds) Command the IUT to send data<br>I-Frame<br>(N(S) = 0, No FCS)<br>**----- End of picture text -----**<br>

_Figure 4.69: L2CAP/OFS/BV-03-C [Sending I-Frames without FCS for Streaming Mode] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **111 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT sends an I-frame without the FCS field.

## **L2CAP/OFS/BV-04-C [Receiving Frames without FCS for Streaming Mode]**

- Test Purpose

Verify that the IUT can handle I-frames that do not contain the FCS.

- Reference

- [1] 3.3.5, 8.7

- Initial Condition

- The channel is configured to not include FCS in I/S-frames.

- The channel is configured to use Streaming Mode.

- Test Procedure

**==> picture [341 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode and to not use FCS<br>I-Frame<br>(N(S) = 0, No FCS) Received Data passed to Upper<br>Tester<br>**----- End of picture text -----**<br>

_Figure 4.70: L2CAP/OFS/BV-04-C [Receiving Frames without FCS for Streaming Mode] MSC_

- Expected Outcome

## Pass verdict

The IUT passes the received data to the Upper Tester.

## **L2CAP/OFS/BV-05-C [Sending I-Frames with FCS for ERTM]**

- Test Purpose

Verify that the IUT does include the FCS in I-frames.

- Reference

- [1] 3.3.5, 8.6

- Initial Condition

- The channel is configured to include FCS in I/S-frames.

- The channel is configured to use ERTM.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **112 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [376 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM and to use FCS<br>Test Guard<br>Timer L2CAP_Config_Rsp<br>(30 seconds) Command the IUT to send data<br>I-Frame<br>(N(S) = 0, FCS)<br>Retransmission<br>S-Frame Timer<br>(RR, N(R) = 1, Poll = 0, FCS)<br>**----- End of picture text -----**<br>

_Figure 4.71: L2CAP/OFS/BV-05-C [Sending I-Frames with FCS for ERTM] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an I-frame with the correct FCS included.

## **L2CAP/OFS/BV-06-C [Receiving Frames with FCS for ERTM]**

- Test Purpose

Verify that the IUT can handle I-frames that do contain the FCS.

- Reference

- [1] 3.3.5, 8.6

- Initial Condition

- The channel is configured to include FCS in I/S-frames.

- The channel is configured to use ERTM.

- Test Procedure

**==> picture [377 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM and to use FCS<br>I-Frame<br>Retransmission (N(S) = 0, FCS) Received Data passed to Upper Tester<br>Timer<br>S-Frame<br>(RR, N(R) = 1, FCS)<br>**----- End of picture text -----**<br>

_Figure 4.72: L2CAP/OFS/BV-06-C [Receiving Frames with FCS for ERTM] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **113 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT passes the received data to the Upper Tester.

The IUT acknowledges the received I-frame before the Retransmission timer of the Lower Tester expires.

## **L2CAP/OFS/BV-07-C [Sending I-Frames with FCS for Streaming Mode]**

- Test Purpose

Verify that the IUT does include the FCS in I-frames.

- Reference

- [1] 3.3.5, 8.7

- Initial Condition

- The channel is configured to include FCS in I/S-frames.

- The channel is configured to use Streaming Mode.

- Test Procedure

**==> picture [376 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode and to use FCS<br>Test Guard<br>Timer L2CAP_Config_Rsp<br>(30 seconds) Command the IUT to send data<br>I-Frame<br>(N(S) = 0, FCS)<br>**----- End of picture text -----**<br>

_Figure 4.73: L2CAP/OFS/BV-07-C [Sending I-Frames with FCS for Streaming Mode] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an I-frame with the FCS field.

## **L2CAP/OFS/BV-08-C [Receiving Frames with FCS for Streaming Mode]**

- Test Purpose

Verify that the IUT can handle I-frames that do contain the FCS.

- Reference

- [1] 3.3.5, 8.7

- Initial Condition

- The channel is configured to include FCS in I/S-frames.

- The channel is configured to use Streaming Mode.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **114 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode and to use FCS<br>I-Frame<br>(N(S) = 0, FCS) Received Data passed to Upper<br>Tester<br>**----- End of picture text -----**<br>

_Figure 4.74: L2CAP/OFS/BV-08-C [Receiving Frames with FCS for Streaming Mode] MSC_

- Expected Outcome

## Pass verdict

The IUT passes the received data to the Upper Tester.

## **4.11.7 Enhanced Retransmission Mode (ERM)**

Verify the correct implementation of the Enhanced Retransmission Mode of L2CAP.

## **L2CAP/ERM/BV-01-C [Transmit I-frames]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the enhanced control fields (SAR, F-bit, ReqSeq, TxSeq).

- Reference

- [1] 3.3.2, 8.6

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID.

- The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **115 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.75 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 0)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 3, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.75: L2CAP/ERM/BV-01-C [Transmit I-frames] MSC_

- Expected Outcome

Pass verdict

The IUT sends I-frame(s) to the Lower Tester.

Data in the I-frame(s) match that provided by the Upper Tester.

SAR bits are set per the Specification in [8].

F-bit is set to 0.

## **L2CAP/ERM/BV-02-C [Receive I-Frames]**

- Test Purpose

Verify that the IUT can receive in-sequence valid I-frames and deliver L2CAP SDUs to the Upper Tester.

- Reference

[1] 3.3.2, 8.6

-

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID.

- The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The IUT has configured an MPS size that is equal to 48 bytes.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **116 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.76 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 355] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional (RR, 0 <= N(R) <= 1, P=0, F=0)<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 2, P=0, F=0)<br>I-Frame – Payload Length 48 Bytes<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 3, P=0, F=0)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01)<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 4, P=0, F=0)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11)<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 5, P=0, F=0)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 6, P=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.76: L2CAP/ERM/BV-02-C [Receive I-Frames] MSC_

- Expected Outcome

## Pass verdict

Data in the received I-frame(s) match that sent by the Lower Tester.

SAR bits are set per specification.

F-bit is set to 0.

Complete SDU is sent to the Upper Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **117 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/ERM/BV-03-C [Acknowledging Received I-Frames]**

- Test Purpose

Verify that the IUT sends S-frame [RR] with the Poll bit not set to acknowledge data received from the Lower Tester.

- Reference

[1] 3.3.2, 8.6.1.1

-

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.77 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [375 x 199] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 1, P=0, F=0)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0)<br>Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 2, P=0, F=0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0)<br>Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 3, P=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.77: L2CAP/ERM/BV-03-C [Acknowledging Received I-Frames] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a Supervisory Frame with S=RR, LastAckedReqSeq < ReqSeq <= last received I- frame’s TxSeq+1, F=0, P=0, Reserved bits = 0.

## **L2CAP/ERM/BV-05-C [Resume Transmitting I-Frames when an S-Frame [RR] is Received]**

- Test Purpose

Verify that the IUT ceases transmission of I-frames when the negotiated TxWindow is full. Verify that the IUT resumes transmission of I-frames when an S-frame [RR] is received that acknowledges previously sent I-frames.

- Reference

[1] 3.3.2, 8.6.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **118 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The Lower Tester specifies a TxWindow size of 1 in the Configuration Request it sends to the IUT.

- Test Procedure

Figure 4.78 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>S-Frame<br>Timer<br>(RR, N(R) = 1, P = 0, F = 0)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.78: L2CAP/ERM/BV-05-C [Resume Transmitting I-Frames when an S-Frame [RR] is Received] MSC_

- Expected Outcome

## Pass verdict

The IUT sends I-frames until TxWindow is full.

The IUT does not send any I-frame when the TxWindow is full.

The IUT sends the outstanding I-frame when it receives the acknowledgment of the first I-frame from the Lower Tester.

## **L2CAP/ERM/BV-06-C [Resume Transmitting I-Frames when an I-Frame is Received]**

- Test Purpose

Verify that the IUT ceases transmission of I-frames when the negotiated TxWindow is full. Verify that the IUT resumes transmission of I-frames when an I-frame is received that acknowledges previously sent I-frames.

- Reference

[1] 3.3.2, 8.6.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **119 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The Lower Tester specifies a TxWindow size of 1 in the Configuration Request it sends to the IUT.

- Test Procedure

Figure 4.79 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>I-Frame<br>Timer<br>(N(S) = 0, N(R) = 1, F = 0)<br>I-Frame<br>(N(S) = 1, N(R) = 0 or 1, F = 0) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.79: L2CAP/ERM/BV-06-C [Resume Transmitting I-Frames when an I-Frame is Received] MSC_

- Expected Outcome

## Pass verdict

The IUT sends I-frames until TxWindow is full.

The IUT does not send any I-frame when the TxWindow is full.

The IUT sends the outstanding I-frame when it receives the acknowledgment of the first I-frame from the Lower Tester.

## **L2CAP/ERM/BV-07-C [Send S-Frame [RNR]]**

- Test Purpose

Verify that the IUT sends an S-frame [RNR] when it detects a Local Busy condition.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **120 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Whether the IUT has the capability to set the Local Busy condition from the Upper Tester is specified in the L2CAP TSPX_generate_local_busy IXIT value.

- Test Procedure

Figure 4.80 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The Lower Tester sends as many I-frames as are permitted by the IUT TxWindow to trigger the Local Busy condition at the IUT. Once the Lower Tester receives the RNR from the IUT it will stop sending I-frames.

**==> picture [375 x 219] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Upper Tester sets Local Busy<br>condition<br>ALT 1<br>S-Frame<br>(RNR, N(R) =0, P=0, F=0)<br>I-Frame ALT 2<br>(N(S) = 0, N(R) = 0, F = 0)<br>I-Frame<br>Retrans- (N(S) = 1, N(R) = 0, F = 0)<br>mission<br>Timer I-Frame ...<br>(N(S) = n, N(R) = 0, F = 0<br> n < IUT TxWin)<br>S-Frame<br>(RNR, 0 <= N(R) <= n + 1, P=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.80: L2CAP/ERM/BV-07-C [Send S-Frame [RNR]] MSC_

- Expected Outcome

## Pass verdict

ALT 1: The IUT immediately sends an S-frame with function RNR after the Local Busy condition is set by the Upper Tester.

ALT 2: The IUT sends an S-frame with function RNR after receiving I-frame(s) from the Lower Tester when the Local Busy condition is reached.

## **L2CAP/ERM/BV-08-C [Send S-Frame [RR] with Poll Bit Set]**

- Test Purpose

Verify that the IUT sends an S-frame [RR] with the Poll bit set when its retransmission timer expires.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **121 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.81 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [377 x 169] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 1)<br>Retransmission<br>Timer of the IUT<br>**----- End of picture text -----**<br>

_Figure 4.81: L2CAP/ERM/BV-08-C [Send S-Frame [RR] with Poll Bit Set] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an S-frame with the POLL bit set after the IUT Retransmission Timer (as specified by Lower Tester during configuration) expires.

The IUT does not retransmit the I-frame after receiving an S-frame from the Lower Tester that acknowledges the previously sent I-frame.

## **L2CAP/ERM/BV-09-C [Send S-frame [RR] with Final Bit Set]**

- Test Purpose

Verify that the IUT responds with an S-frame [RR] with the Final bit set after receiving an S-frame [RR] with the Poll bit set.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **122 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.82 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [376 x 177] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer of<br>the Tester<br>S-Frame<br>(RR, N(R) = 0, P = 0, F = 1)<br>**----- End of picture text -----**<br>

_Figure 4.82: L2CAP/ERM/BV-09-C [Send S-frame [RR] with Final Bit Set] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an S-frame with the Final bit set before the Monitor Timer of the Lower Tester expires.

## **L2CAP/ERM/BV-10-C [Retransmit S-Frame [RR] with Poll Bit Set]**

- Test Purpose

Verify that the IUT will retransmit the S-frame [RR] with the Poll bit set when the Monitor Timer expires.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **123 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.83 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [376 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 1)<br>Monitor Timer of<br>the IUT<br>**----- End of picture text -----**<br>

_Figure 4.83: L2CAP/ERM/BV-10-C [Retransmit S-Frame [RR] with Poll Bit Set] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the S-frame with the POLL bit set after the Monitor Timer expires.

The IUT does not retransmit the S-frame with the POLL bit set after receiving the S-frame acknowledgment of the previously sent I-frame.

## **L2CAP/ERM/BV-11-C [S-Frame Transmissions Exceed MaxTransmit]**

- Test Purpose

Verify that the IUT closes the channel when the Monitor Timer expires.

- Reference

[1] 3.3.2, 5.4, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **124 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.84 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>L2CAP_DisconnectReq<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.84: L2CAP/ERM/BV-11-C [S-Frame Transmissions Exceed MaxTransmit] MSC_

- Expected Outcome

Pass verdict

The IUT initiates closure of the L2CAP channel when the Monitor Timer expires.

## **L2CAP/ERM/BV-12-C [I-Frame Transmissions Exceed MaxTransmit]**

- Test Purpose

Verify that the IUT closes the channel when it receives an S-frame [RR] with the final bit set that does not acknowledge the previous I-frame sent by the IUT.

- Reference

[1] 3.3.2, 5.4, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **125 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.85 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 202] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(RR, N(R) = 0, P = 0, F = 1)<br>L2CAP_DisconnectReq<br>L2CAP_DisconnectRsp<br>**----- End of picture text -----**<br>

_Figure 4.85: L2CAP/ERM/BV-12-C [I-Frame Transmissions Exceed MaxTransmit] MSC_

- Expected Outcome

## Pass verdict

The IUT initiates closure of the L2CAP channel when it receives the S-frame from the Lower Tester that does not acknowledge the previously sent I-frame.

## **L2CAP/ERM/BV-13-C [Respond to S-Frame [REJ]]**

- Test Purpose

Verify that the IUT retransmits I-frames starting from the sequence number specified in the S-frame [REJ].

- Reference

[1] 3.3.2, 8.6.1.2, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin that is greater than 1 in the Configure Request sent to the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **126 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.86 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [375 x 218] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>I-Frame<br>Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>S-Frame<br>(REJ, N(R) = 0, P = 0, F = 0)<br>Monitor Timer of<br>the Tester I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission Retransmission<br>Timer of the IUT I-Frame Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.86: L2CAP/ERM/BV-13-C [Respond to S-Frame [REJ]] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the first I-frame requested in the REJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The IUT retransmits the second I-frame requested in the REJ from the Lower Tester before the IUT Retransmission Timer expires.

## **L2CAP/ERM/BV-14-C [Respond to S-Frame [SREJ] POLL Bit Set]**

- Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame. Verify that the IUT processes the acknowledgment of previously unacknowledged I-frames.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **127 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.87 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [376 x 269] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>I-Frame<br>Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0)<br>S-Frame<br>(SREJ, N(R) = 1, P = 1, F = 0)<br>Monitor Timer of<br>the Tester I-Frame<br>(N(S) = 1, N(R) = 0, F = 1)<br>I-Frame Retransmission<br>(N(S) = 3, N(R) = 0, F = 0) Timer<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.87: L2CAP/ERM/BV-14-C [Respond to S-Frame [SREJ] POLL Bit Set] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The I-frame retransmitted by the IUT has the Final bit = 1.

The IUT processes the acknowledgment of the first I-frame (N(S) = 0) from the SREJ received and consequently send the pending I-frame (N(S) = 3).

## **L2CAP/ERM/BV-15-C [Respond to S-Frame [SREJ] POLL bit clear]**

- Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **128 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.

- Test Procedure

Figure 4.88 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [375 x 258] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>I-Frame<br>Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0)<br>S-Frame<br>(SREJ, N(R) = 1, P = 0, F = 0)<br>Monitor Timer of<br>the Tester I-Frame<br>(N(S) = 1, N(R) = 0, F = 0) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 3, P = 0, F = 0)<br>I-Frame<br>(N(S) = 3, N(R) = 0, F = 0) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 4, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.88: L2CAP/ERM/BV-15-C [Respond to S-Frame [SREJ] POLL bit clear] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The IUT does not transmit I-frame (N(S) = 3) as a result of receiving the SREJ from the Lower Tester.

## **L2CAP/ERM/BV-16-C [Send S-Frame [REJ]]**

- Test Purpose

Verify that the IUT can send an S-frame [REJ] after receiving out of sequence I-frames.

- Reference

[1] 3.3.2, 8.6.1.2, 8.6.4

- Initial Condition

- The TxWindow size of the Lower Tester must be greater than 2 and should be the largest value that can be supported by the IUT.

- The channel is in the OPEN state and configured to use ERTM.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **129 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.89 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [413 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>I-Frame<br>N(S) = 0, N(R) =0, F=0<br>Retransmission Timer of the I-Frame (RR, N(R) =1, P=0, F=0)S-Frame (Optional)<br>Tester N(S) = (IUT TxWin -1), N(R) =0, F=0<br>S-Frame<br>(REJ, N(R) =1, P=0, F=0)<br>Tester sends all I-Frames<br>I-Frame from N(S) =1 to<br>N(S) = 1, N(R) =0, F=0 N(S) = IUT TxWin -1<br>S-Frame<br>(Optional)<br>Retransmission (RR, N(R) =2, P=0, F=0)<br>Timer of the<br>Tester ...<br>I-Frame<br>N(S) = IUT TxWin -1, N(R) =0, F=0<br>S-Frame<br>(RR, N(R) = IUT TxWin, P=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.89: L2CAP/ERM/BV-16-C [Send S-Frame [REJ]] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an S-frame REJ requesting I-frames with N(S) >= 1 prior to the Retransmission timer of the Lower Tester expiring.

The IUT acknowledges all the I-frames that are sent by the Lower Tester after the S-frame REJ is sent.

## **L2CAP/ERM/BV-17-C [Send S-Frame [SREJ]]**

- Test Purpose

Verify that the IUT can send an S-frame [SREJ] after receiving out of sequence I-frames.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition

- The TxWindow size of the Lower Tester must be greater than 2.

- The channel is in the OPEN state and configured to use ERTM.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **130 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.90 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [357 x 212] intentionally omitted <==**

_Figure 4.90: L2CAP/ERM/BV-17-C [Send S-Frame [SREJ]] MSC_

- Expected Outcome

Pass verdict

The IUT sends an S-frame SREJ requesting I-frame with N(S) = 1 prior to the Retransmission timer of the Lower Tester expiring.

The IUT acknowledges all the I-frames that are sent by the Lower Tester.

## **L2CAP/ERM/BV-18-C [Receive S-Frame [RR] Final Bit = 1]**

- Test Purpose

Verify that the IUT retransmits any previously sent I-frames unacknowledged by receipt of an S- Frame [RR] with the Final Bit set.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- MaxTransmit for the IUT is set to a value greater than 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **131 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.91 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [375 x 205] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Retransmission<br>Timer<br>Timer of the IUT<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(RR, N(R) = 0, P = 0, F = 1)<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.91: L2CAP/ERM/BV-18-C [Receive S-Frame [RR] Final Bit = 1] MSC_

- Expected Outcome

Pass verdict

The IUT retransmits the I-frame when it receives the S-frame from the Lower Tester that indicates that the previous transmission failed.

## **L2CAP/ERM/BV-19-C [Receive I-Frame Final Bit = 1]**

- Test Purpose

Verify that the IUT retransmits any previously sent I-frames unacknowledged by receipt of an I-frame with the final bit set.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

-

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- MaxTransmit for the IUT is set to a value greater than 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **132 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.92 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [368 x 197] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Retransmission S-Frame Timer<br>Timer of the IUT (RR, N(R) = 0, P = 1, F = 0)<br>I-Frame<br>Monitor Timer<br>(N(S) = 0, N(R) = 0, F = 1)<br>I-Frame<br>(N(S) = 0, N(R) = 0 OR 1, F = 0)<br>S-Frame Retransmission<br>(Optional) (RR, N(R) = 1, P = 0, F = 0) Timer<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.92: L2CAP/ERM/BV-19-C [Receive I-Frame Final Bit = 1] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame when it receives the I-frame from the Lower Tester that indicates that the previous transmission failed.

## **L2CAP/ERM/BV-20-C [Enter Remote Busy Condition]**

- Test Purpose

Verify that the IUT does not retransmit any I-frames when it receives a remote busy indication from the Lower Tester (S-frame [RNR]).

- Reference

- [1] 3.3.2, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- MaxTransmit for the IUT is set to a value greater than 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **133 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.93 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [370 x 197] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Retransmission<br>Timer<br>Timer of the IUT<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(RNR, N(R) = 0, P = 0, F = 1)<br>Retransmission<br>Timer of the IUT<br>**----- End of picture text -----**<br>

_Figure 4.93: L2CAP/ERM/BV-20-C [Enter Remote Busy Condition] MSC_

- Expected Outcome

## Pass verdict

The IUT does not retransmit the unacknowledged I-frame.

## **L2CAP/ERM/BV-22-C [Exit Local Busy Condition]**

- Test Purpose

Verify that the IUT sends an S-frame [RR] Poll = 1 when the local busy condition is cleared.

- Reference

[1] 3.3.2, 8.6.4

- Initial Condition

- Run test L2CAP/ERM/BV-07-C [Send S-Frame [RNR]].

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **134 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [369 x 173] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Upper Tester clears Local Busy<br>condition<br>S-Frame<br>Retransmission (RR, N(R) = n, P = 1, F = 0)<br>Timer Monitor Timer<br>S-Frame<br>(RR, N(R) = 0, P = 0, F = 1)<br>**----- End of picture text -----**<br>

_Figure 4.94: L2CAP/ERM/BV-22-C [Exit Local Busy Condition] MSC_

- Expected Outcome

Pass verdict

The IUT sends an S-frame RR with the POLL bit set.

## **L2CAP/ERM/BV-23-C [Transmit I-Frames using SAR]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the enhanced control fields (SAR, F-bit, ReqSeq, TxSeq) when performing SAR.

- Reference

[1] 3.3.2

- Initial Condition

- The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The Lower Tester has configured a value for the MPS that ensures that the IUT performs SAR. The Lower Tester uses "TSPX_iut_SDU_size_in_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.

- The Lower Tester has configured a TxWindow size of 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **135 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.95 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [338 x 346] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 01) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 1, P = 0, F = 0)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 11) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 2, P = 0, F = 0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 10) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 3, P = 0, F = 0)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 4, P = 0, F = 0)<br>I-Frame<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 5, P = 0, F = 0)<br>I-Frame<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 6, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.95: L2CAP/ERM/BV-23-C [Transmit I-Frames using SAR] MSC_

- Expected Outcome

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT.

## **L2CAP/ERM/BI-01-C [S-Frame [REJ] Lost or Corrupted]**

- Test Purpose

Verify that the IUT can handle receipt of an S-frame [RR] Poll = 1 if the S-frame [REJ] sent from the IUT is lost.

- Reference

[1] 3.3.2, 8.6.1.2, 8.6.4

-

## Initial Condition

- The TxWindow size of the Lower Tester must be greater than 2 and should be the largest value that can be supported by the IUT.

- The channel is in the OPEN state and configured to use ERTM.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **136 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.96 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [378 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission S-Frame (Optional<br>Timer of the (RR, N(R) = 1, P = 0 , F = 0) )<br>I-Frame<br>Tester<br>(N(S) = (IUT TxWin – 1), N(R) = 0, F = 0)<br>S-Frame<br>(REJ, N(R) = 1, P = 0, F = 0)<br>S-Frame<br>Monitor Timer (RR, N(R) = 0, P = 1, F = 0)<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 1) Tester sends all I-<br>I-Frame Frames from N(S) = 1 to<br>(N(S) = 1, N(R) = 0, F = 0) N(S) = IUT TxWin - 1<br>S-Frame<br>(RR, N(R) = 2, P = 0 , F = 0) (Optional. Each subsequent in-sequence<br>I-Frame may be acknowledged in the<br>same manner until N(S) = (IUT TxWin - 1))<br>I-Frame<br>(N(S) = (IUT TxWin – 1), N(R) = 0, F = 0)<br>S-Frame<br>(RR, N(R) = IUT TxWin, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.96: L2CAP/ERM/BI-01-C [S-Frame [REJ] Lost or Corrupted] MSC_

- Expected Outcome

## Pass verdict

The IUT responds to the S-frame [RR] Poll = 1 with an S-frame [RR] Final = 1 that includes the TxSeq of the last received in sequence I-frame.

The IUT acknowledges all the I-frames that are sent by the Lower Tester after the S-frame REJ is sent.

## **L2CAP/ERM/BI-02-C [S-Frame [SREJ] Lost or Corrupted]**

- Test Purpose

Verify that the IUT can handle receipt of an S-frame [RR] Poll = 1 if the S-frame [SREJ] sent from the IUT is lost.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

-

- Initial Condition

- The TxWindow size of the Lower Tester must be greater than 2.

- The channel is in the OPEN state and configured to use ERTM.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **137 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.97 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [389 x 293] intentionally omitted <==**

_Figure 4.97: L2CAP/ERM/BI-02-C [S-Frame [SREJ] Lost or Corrupted] MSC_

- Expected Outcome

## Pass verdict

The IUT responds to the S-frame [RR] Poll = 1 with an S-frame [SREJ] Final = 1 that includes the TxSeq of the missing I-frame (N(S) = 1).

The IUT acknowledges all the I-frames that are sent by the Lower Tester after the S-frame SREJ is sent.

## **L2CAP/ERM/BI-03-C [Handle Duplicate S-Frame [SREJ]]**

- Test Purpose

Verify that the IUT only retransmits the requested I-frame once after receiving a duplicate SREJ.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **138 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin > 1 in the Configure Request sent to the IUT.

- Test Procedure

Figure 4.98 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>I-Frame<br>Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(SREJ, N(R) = 0, P = 0, F = 0)<br>S-Frame<br>(SREJ, N(R) = 0, P = 0, F = 1)<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.98: L2CAP/ERM/BI-03-C [Handle Duplicate S-Frame [SREJ]] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester only once.

**L2CAP/ERM/BI-04-C [Handle Receipt of S-Frame [REJ] and S-Frame [RR, F=1] that Both Require Retransmission of the Same I-Frames]**

- Test Purpose

Verify that the IUT only retransmits the requested I-frames once after receiving an S-frame [REJ] followed by an S-frame [RR] with the Final bit set that indicates the same I-frames should be retransmitted.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **139 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin > 1 in the Configure Request sent to the IUT.

- Test Procedure

Figure 4.99 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(REJ, N(R) = 0, P = 0, F = 0)<br>S-Frame<br>(RR, N(R) = 0, P = 0, F = 1)<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>I-Frame Retransmission<br>(N(S) = 1, N(R) = 0, F = 0) Timer<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.99: L2CAP/ERM/BI-04-C [Handle Receipt of S-Frame [REJ] and S-Frame [RR, F=1] that Both Require Retransmission of the Same I-Frames] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frames requested in the REJ from the Lower Tester only once.

**L2CAP/ERM/BI-05-C [Handle receipt of S-Frame [REJ] and I-Frame [F=1] that Both Require Retransmission of the Same I-Frames]**

- Test Purpose

Verify that the IUT only retransmits the requested I-frames once after receiving an S-frame [REJ] followed by an I-frame with the Final bit set that indicates the same I-frames should be retransmitted.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **140 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin > 1 in the Configure Request sent to the IUT.

- Test Procedure

Figure 4.100 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 293] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>I-Frame Retransmission Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>S-Frame<br>S-Frame (RR, N(R) = 0, P=1, F = 0) Monitor Timer<br>(REJ, N(R) = 0, P = 0, F = 0)<br>I-Frame<br>(N(S)= 0, N(R) = 0, F = 1)<br>I-Frame ALT1<br>(N(S) = 0, N(R) = 0, F = 0)<br>I-Frame Retransmission Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>I-Frame ALT2<br>(N(S) = 0, N(R) = 1, F = 0)<br>I-Frame Retransmission Timer<br>(N(S) = 1, N(R) = 1, F = 0)<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>I-Frame ALT3<br>(N(S) = 0, N(R) = 0, F = 0)<br>I-Frame Retransmission Timer<br>(N(S) = 1, N(R) = 1, F = 0)<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.100: L2CAP/ERM/BI-05-C [Handle receipt of S-Frame [REJ] and I-Frame [F=1] that Both Require Retransmission of the Same I-Frames] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frames requested in the REJ from the Lower Tester only once.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **141 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.11.8 Streaming Mode (STM)**

Verify the correct implementation of Streaming Mode in the IUT.

## **L2CAP/STM/BV-01-C [Streaming Mode Source]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Control fields (SAR, F-bit, ReqSeq, and TxSeq).

- Reference

- [1] 3.3.2, 8.7

- Initial Condition

- The channel is in the OPEN state and configured to use Streaming Mode.

- No I-frames have been sent from the IUT or the Lower Tester.

- Test Procedure

**==> picture [341 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) Command the IUT to send data<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00)<br>**----- End of picture text -----**<br>

_Figure 4.101: L2CAP/STM/BV-01-C [Streaming Mode Source] MSC_

- Expected Outcome

## Pass verdict

The Lower Tester receives three correctly formatted I-frames from the IUT.

## **L2CAP/STM/BV-02-C [Streaming Mode Sink]**

- Test Purpose

Verify that the IUT receives I-frames and handles SAR correctly.

- Reference

- [1] 3.3.2, 8.7

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **142 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The channel is in the OPEN state and configured to use Streaming Mode.

- No I-frames have been sent from the IUT or the Lower Tester.

- The IUT has configured a MTU and MPS size that is greater or equal to 48 bytes.

- Test Procedure

**==> picture [341 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode.<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10) 48 Bytes of data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.102: L2CAP/STM/BV-02-C [Streaming Mode Sink] MSC_

- Expected Outcome

## Pass verdict

The IUT passes the received data correctly to the Upper Tester.

## **L2CAP/STM/BV-03-C [Streaming Mode Source using SAR]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Control fields (SAR, F-bit, ReqSeq, TxSeq) while performing SAR.

- Reference

- [1] 3.3.2, 8.7

- Initial Condition

- The channel is in the OPEN state and configured to use Streaming Mode.

- No I-frames have been sent from the IUT or Lower Tester.

- The Lower Tester has configured a value for the MPS that ensures that the IUT performs SAR. The Lower Tester uses "TSPX_iut_SDU_size_in_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **143 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 211] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 01)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 11)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 10) Command the IUT to send data<br>I-Frame<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01)<br>I-Frame<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11)<br>I-Frame<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10)<br>**----- End of picture text -----**<br>

_Figure 4.103: L2CAP/STM/BV-03-C [Streaming Mode Source using SAR] MSC_

- Expected Outcome

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT.

## **4.11.9 Fixed Channel Support (FIX)**

Verify the correct implementation of fixed channels information response in L2CAP.

## **L2CAP/FIX/BV-01-C [Fixed Channels Supported Information Request]**

- Test Purpose

- Verify that the IUT can send an Information Request for the information type of Fixed Channels Supported.

- Reference

[1] 4.10, 4.11, 4.12, 4.13

- Initial Condition

- The IUT has established that the Lower Tester supports Fixed Channels with an Info Request with Info Type set to Extended Features.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **144 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [340 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in any state.<br>L2CAP_InfoReq<br>(ID, length, InfoType = 0x0003)<br>L2CAP_InfoRsp<br> (ID, length, InfoType = 0x0003,<br>Result=Success 0x0000, data)<br>**----- End of picture text -----**<br>

_Figure 4.104: L2CAP/FIX/BV-01-C [Fixed Channels Supported Information Request] MSC_

- Expected Outcome

## Pass verdict

The IUT sends Information Request [InfoType = Fixed Channels].

## **L2CAP/FIX/BV-02-C [AMP Manager Channel Supported]**

- Test Purpose

Verify that the IUT can send an Information Response for the information type of Fixed Channels Supported that contains the map of supported fixed channels with the AMP Manager Protocol Channel (bit-3 of octet 0) set to 1.

- Reference

[1] 4.10, 4.11, 4.12, 4.13

- Initial Condition

- The Lower Tester has established that the IUT supports Fixed Channels by using an Info Request with the Info Type set to 0x0002 (Extended Features).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **145 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [340 x 283] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP_InfoReq<br>(InfoType = Extended Features 0x0002)<br>RTX Timer<br>(5 Seconds)<br>L2CAP_InfoRsp<br>(InfoType = Extended Features, Extended<br>Feature Mask Fixed Channels bit =1)<br>L2CAP_InfoReq<br>(InfoType = Fixed Channels 0x0003)<br>RTX Timer<br>(5 Seconds)<br>L2CAP_InfoRsp<br>ID, length, InfoType = Fixed Channels,<br>Result=Success 0x0000, data(L2CAP<br>Signaling bit =1, AMP Manager Protocol bit<br>=1)<br>**----- End of picture text -----**<br>

_Figure 4.105: L2CAP/FIX/BV-02-C [AMP Manager Channel Supported] MSC_

- Expected Outcome

## Pass verdict

The IUT sends Information Response [InfoType = Fixed Channels] and a result code of “Success.”

The Fixed Channel Mask bit for L2CAP Signaling channel is set to 1.

The Fixed Channel Mask bit for AMP Manager Protocol channel is set to 1.

- **L2CAP/FIX/BV-03-C [Information Request, Fixed Channels Supported]**

- Test Purpose

Verify that the IUT returns the Fixed Channels Supported in response to the Information Request from the Lower Tester.

- Reference

- [11] 4.10

-

- Initial Condition

- The IUT is in the CLOSED state.

- No ACL link exists between the Lower Tester and the IUT.

- The IUT acts as an L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **146 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

The Lower Tester sends an information request to IUT.

**==> picture [355 x 96] intentionally omitted <==**

_Figure 4.106: L2CAP/FIX/BV-03-C [Information Request, Fixed Channels Supported] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP_INFORMATION_RSP PDU to the Lower Tester with the Info parameter containing 8 octets with the IUT Fixed L2CAP Channels. In the Info parameter, the octets match Table 4.25. In Table 4.25, the bit is set if the ICS entry is selected. All bits not listed are set to 0b0.

|**CID**|**Octet**|**Bit**|**Value**|
|0x0000(Null ID)|0|0|0b0|
|0x0001(L2CAP SignalingChannel)|0|1|0b1|
|0x0002(Connectionless reception)|0|2|L2CAP 2/35|
|0x0003(AMP Manager)|0|3|L2CAP 2/31|
|0x0007(BR/EDR SecurityManager)|0|7|0b0 OR 0b1|
|0x003F(AMP Test Manager)|7|7|L2CAP 2/29|

_Table 4.25: Fixed Channels Supported Mask bits_

- Notes

The Lower Tester’s RTX timer is set to maximum allowed initial value.

All CIDs that are RFU are set to 0b0.

## **4.11.10 Extended Window Size Configuration (EWC)**

Verify the configuration of the Extended Window size option of L2CAP.

## **L2CAP/EWC/BV-01-C [IUT Initiated Extended Window Size Option]**

- Test Purpose

Verify that the IUT can configure a channel to use the Extended Window size option.

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition

- The IUT has established that the peer L2CAP entity supports configuration of the Extended Window Size option (using the Information Request/Response [Extended Features] mechanism).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **147 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [379 x 258] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in CONFIG State. Tester has not sent L2CAP_ConfigReq<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(EWS Option bit = 1<br>Configuration Timer<br> [Ch. Mode = ERTM or STM<br>(120 Seconds)<br>Other Option fields = ANY])<br>L2CAP_ConfigRsp<br>(Result = Success)<br>L2CAP_ConfigReq<br>(EWS option bit = 1<br>RTX Timer [Ch. Mode = ERTM or STM<br>(5 Seconds) Other Option fields = ANY]<br>L2CAP_ConfigRsp<br>(Result = Success)<br>**----- End of picture text -----**<br>

_Figure 4.107: L2CAP/EWC/BV-01-C [IUT Initiated Extended Window Size Option] MSC_

- Expected Outcome

## Pass verdict

The channel is established.

The IUT sends an L2CAP_ConfigReq including the Extended Feature Mask bit for Extended Window size option before the Configuration timer expires.

The IUT responds with Success to the Lower Tester sending an L2CAP_ConfigReq including the Extended Window size option.

## **L2CAP/EWC/BV-02-C [Lower Tester Requests Extended Window Size]**

- Test Purpose

Verify that the IUT uses the Extended Control Field in I/S-frames if the Lower Tester requests that Extended Window Size is used.

- Reference

[1] 3.3.2, 4.4, 4.5, 5.7, 6.1.4, 7.1, 8.2 (CSA1)

-

- Initial Condition

- L2CAP/EWC/BV-01-C [IUT Initiated Extended Window Size Option] test case was completed successfully.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **148 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [378 x 229] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in CONFIG State. Tester has not sent L2CAP_ConfigReq<br>L2CAP_CONNECTION_RSP<br>L2CAP_ConfigReq<br>(EWS Option bit = 0<br> [Ch. Mode = ERTM or STM<br>Other Option fields = ANY])<br>L2CAP_ConfigRsp<br>Configuration Timer (Result = Success)<br>(120 Seconds) L2CAP_ConfigReq<br>(EWS option bit = 1<br>[Ch. Mode = ERTM or STM<br>Other Option fields = ANY]<br>L2CAP_ConfigRsp<br>RTX Timer<br>(Result = Success)<br>(5 Seconds)<br>S-frame (RR)<br>(Extended Control Field included)<br>Data to send<br>I-Frame<br>(Extended Control Field included)<br>**----- End of picture text -----**<br>

_Figure 4.108: L2CAP/EWC/BV-02-C [Lower Tester Requests Extended Window Size] MSC_

- Expected Outcome

## Pass verdict

The channel is established.

The IUT accepts the EWS option while configuring.

The IUT includes ECF in S-frames sent to the Lower Tester.

The IUT includes ECF in I-frames sent to the Lower Tester.

## **L2CAP/EWC/BV-03-C [Extended Window Size Option Not Supported by Lower Tester]**

- Test Purpose

Verify that the IUT does not include an Extended Window Size option when configuring the channel if the Lower Tester does not indicate support for the Extended Windows Size option in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **149 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [342 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established<br>Create Connection<br>(ERTM or STM,<br>Specify EWS Option))<br>L2CAP_InfoReq<br>(InfoType = Extended Features)<br>RTX Timer<br>L2CAP_InfoRsp<br>(InfoType = Extended Features<br>Extended Feature Mask<br> STM + ERTM bit = 1, EWS Option bit = 0)<br>L2CAP_CONNECTION_REQ<br>RTX Timer<br>L2CAP_CONNECTION_RSP<br>(Result = Success)<br>L2CAP_ConfigReq<br>(EWS Option bit = 0<br>Configuration Timer [Channel Mode = STM / ERTM<br>(120 Seconds) Other Option fields = ANY])<br>**----- End of picture text -----**<br>

_Figure 4.109: L2CAP/EWC/BV-03-C [Extended Window Size Option Not Supported by Lower Tester] MSC_

- Expected Outcome

## Pass verdict

The IUT sends L2CAP_ConfigReq before Configuration Timer expires, with EWS option bit = 0.

## **4.11.11 Lock Step Configuration (LSC)**

Verify the correct implementation of the Lock Step configuration Process.

## **L2CAP/LSC/BV-01-C [Normal Lock Step Configuration Process for Best Effort, BR/EDR ERTM Channel]**

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type “Best Effort”.

- Reference

- [8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.

- L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT’s Extended Features Mask.

- The IUT is in CONFIG state.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **150 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [339 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over BR/EDR using ERTM<br>with the Extended Flow Specification bit set in the Extended Features mask.<br>The L2CAP connection is in the CONFIG State<br>L2CAP_ConfigReq<br>(Channel Mode = ERTM,<br>Ext Flow Spec = BE,<br>QoS and Flush Timeout omitted) RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Success’,<br>Channel Mode = ERTM)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.110: L2CAP/LSC/BV-01-C [Normal Lock Step Configuration Process for Best Effort, BR/EDR ERTM Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigReq packet with Extended Flow Spec options for BE.

The IUT responds to an L2CAP_ConfigReq packet, including Extended Flow Spec options for BE, with status pending before its RTX timer expires.

The IUT sends an L2CAP_ConfigRsp packet with status success after reception of L2CAP_ConfigRsp with status.

## **L2CAP/LSC/BV-02-C [Normal Lock Step Configuration Process for Guaranteed, BR/EDR ERTM Channel]**

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type “Guaranteed”.

- Reference

- [8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **151 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT’s Extended Features Mask.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [340 x 340] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over BR/EDR using ERTM<br>with the Extended Flow Specification bit set in the Extended Features mask.<br>The L2CAP connection is in the CONFIG State<br>L2CAP_ConfigReq<br>(Channel Mode = STM, Ext Flow<br>Spec = G, Max SDU ANY, RTX<br>SDU inter-arrival ANY,<br>QoS and Flush Timeout omitted)<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>ERTX<br>L2CAP_ConfigReq<br>(Result = ‘Success’,<br>Channel Mode = STM, Ext Flow<br>Spec = G, Max SDU = ANY,<br>SDU inter-arrival = ANY,<br>QoS and Flush Timeout omitted)<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>L2CAP_ConfigRsp<br>(Result = ‘Success’)<br>L2CAP_ConfigRsp<br>(Result = ‘Success’)<br>**----- End of picture text -----**<br>

_Figure 4.111: L2CAP/LSC/BV-02-C [Normal Lock Step Configuration Process for Guaranteed, BR/EDR ERTM Channel] MSC_

- Expected Outcome

Pass verdict

The channel is established.

The IUT sends an L2CAP_ConfigReq packet with Extended Flow Spec options for Guaranteed.

The IUT responds to an L2CAP_ConfigReq packet with Extended Flow Spec options for Guaranteed, with status “pending” before its RTX timer expires.

The IUT sends an L2CAP_ConfigRsp packet with status “success” after reception of L2CAP_ConfigRsp with status pending before its ERTX timer expires.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **152 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel]**

- Test Purpose

Verify that the IUT closes the channel if it receives a Configuration response packet with result “success” before receiving a Configuration response packet with result “pending”.

- Reference

- [8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT’s Extended Features Mask.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [341 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over BR/EDR using ERTM<br>with the Extended Flow Specification bit set in the Extended Features mask.<br>The L2CAP connection is in the CONFIG State<br>L2CAP_ConfigReq<br>(Channel Mode = ERTM,<br>Ext Flow Spec = BE,<br>QoS and Flush Timeout omitted) RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Success’,<br>Channel Mode = ERTM)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.112: L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT stays in CONFIG state after receiving L2CAP_ConfigRsp with results before receiving L2CAP_ConfigRsp with “pending” status.

The IUT sends L2CAP_DisconnectReq with the same channel specified.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **153 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/LSC/BI-04-C [Mismatched Service Type, Best Effort, BR/EDR ERTM Channel]**

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type “Best Effort” and receives a Configuration request packet with an Extended Flow Specification containing service type “Guaranteed”. See test case L2CAP/LSC/BV-03C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

- [8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT’s Extended Features Mask.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [341 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over BR/EDR using ERTM<br>with the Extended Flow Specification bit set in the Extended Features mask.<br>The L2CAP connection is in the CONFIG State<br>L2CAP_ConfigReq<br>(Channel Mode = ERTM,<br>Ext Flow Spec = BE,<br>QoS and Flush Timeout omitted) RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>L2CAP_ConfigReq ERTX<br>(Channel Mode = ERTM,<br>Ext Flow Spec = GU,<br>QoS and Flush Timeout omitted)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.113: L2CAP/LSC/BI-04-C [Mismatched Service Type, Best Effort, BR/EDR ERTM Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT rejects mismatched L2CAP_ConfigRsp by sending an L2CAP_DisconnectReq.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **154 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/LSC/BI-05-C [Mismatched Service Type, Guaranteed, BR/EDR ERTM Channel]**

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type “Guaranteed” and receives a Configuration response packet with an Extended Flow Specification containing service type “Best Effort”.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

- [8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT’s Extended Features Mask.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [342 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over BR/EDR using ERTM<br>with the Extended Flow Specification bit set in the Extended Features mask.<br>The L2CAP connection is in the CONFIG State<br>L2CAP_ConfigReq (Channel<br>Mode=ERTM, Ext Flow Spec =<br>Guaranteed<br>RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>ERTX<br>L2CAP_ConfigReq<br>(Result = ‘Failure – flow spec rejected’)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.114: L2CAP/LSC/BI-05-C [Mismatched Service Type, Guaranteed, BR/EDR ERTM Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT rejects mismatched L2CAP_ConfigRsp by sending an L2CAP_DisconnectReq.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **155 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/LSC/BV-06-C [Remote Failed on Guaranteed, BR/EDR ERTM Channel]**

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type “Guaranteed” and after receiving a Configuration Response with result “Pending” it receives a Configuration request packet with a “Failure” result.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

- [8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT’s Extended Features Mask.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [342 x 260] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over BR/EDR using ERTM<br>with the Extended Flow Specification bit set in the Extended Features mask.<br>The L2CAP connection is in the CONFIG State<br>L2CAP_ConfigReq (Channel<br>Mode=ERTM, Ext Flow Spec =<br>Guaranteed<br>RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>ERTX<br>L2CAP_ConfigReq<br>(Result = ‘Failure – flow spec rejected’)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.115: L2CAP/LSC/BV-06-C [Remote Failed on Guaranteed, BR/EDR ERTM Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT detects L2CAP_ConfigRsp indicating ‘no resources’ (failure) by sending an L2CAP_DisconnectReq.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **156 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/LSC/BV-07-C [Normal Lock Step Configuration Process for Best Effort, AMP Channel]**

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type “Best Effort”.

- Reference

- [8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.

- L2CAP channel is connected over an AMP controller which can support guaranteed logical links.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [339 x 334] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over an AMP controller.<br>The L2CAP connection is in the CONFIG State.<br>L2CAP_ConfigReq<br>(Channel Mode = ERTM, Ext Flow<br>Spec = BE, Max SDU <=0xFFFF, RTX<br>SDU inter-arrival <=0xFFFFFFFF,<br>QoS and Flush Timeout omitted)<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>ERTX<br>L2CAP_ConfigReq<br>(Result = ‘Success’,<br>Channel Mode = ERTM, Ext Flow<br>Spec = BE, Max SDU <=0xFFFF,<br>SDU inter-arrival <=0xFFFFFFFF,<br>QoS and Flush Timeout omitted)<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>L2CAP_ConfigRsp<br>(Result = ‘Success’)<br>L2CAP_ConfigRsp<br>(Result = ‘success’)<br>**----- End of picture text -----**<br>

_Figure 4.116: L2CAP/LSC/BV-07-C [Normal Lock Step Configuration Process for Best Effort, AMP Channel] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **157 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP_ConfigReq packet with Extended Flow Spec options for BE.

The IUT responds to an L2CAP_ConfigReq packet, including Extended Flow Spec options for BE, with status pending and can correctly receive a configuration response from the Lower Tester with the result = “Pending” before its RTX timer expires.

The IUT sends an L2CAP_ConfigRsp packet with status success after reception of

L2CAP_ConfigRsp with status pending can correctly receive the configuration response from the Lower Tester with the result = “Success” before its ERTX timer expires.

## **L2CAP/LSC/BV-08-C [Normal Lock Step Configuration Process for Guaranteed, AMP Channel]**

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type “Guaranteed”.

- Reference

[8] 7.1.3

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.

- L2CAP channel is connected over an AMP controller which can support guaranteed logical links.

- The IUT is in CONFIG state.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **158 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 324] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over an AMP controller.<br>The L2CAP connection is in the CONFIG State.<br>L2CAP_ConfigReq<br>(Channel Mode = STM, Ext Flow<br>Spec = G, Max SDU ANY, RTX<br>SDU inter-arrival ANY,<br>QoS and Flush Timeout omitted)<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>ERTX<br>L2CAP_ConfigReq<br>(Result = ‘Success’,<br>Channel Mode = STM, Ext Flow<br>Spec = G, Max SDU = ANY,<br>SDU inter-arrival = ANY,<br>QoS and Flush Timeout omitted)<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>L2CAP_ConfigRsp<br>(Result = ‘Success’)<br>L2CAP_ConfigRsp<br>(Result = ‘Success’)<br>**----- End of picture text -----**<br>

_Figure 4.117: L2CAP/LSC/BV-08-C [Normal Lock Step Configuration Process for Guaranteed, AMP Channel] MSC_

- Expected Outcome

## Pass verdict

The channel is established.

The IUT sends an L2CAP_ConfigReq packet with Extended Flow Spec options for guaranteed service type.

The IUT responds to an L2CAP_ConfigReq packet with status pending before its RTX timer expires.

The IUT sends an L2CAP_ConfigRsp packet with status success after reception of L2CAP_ConfigRsp with status pending can correctly receive the configuration response from the Lower Tester with the result = “Success” before its ERTX timer expires.

## **L2CAP/LSC/BV-09-C [Premature Success in Configuration Response, AMP Channel]**

- Test Purpose

Verify that the IUT closes the channel if it receives a Configuration response packet with result “Success” before receiving a Configuration response packet with result “Pending”.

- Reference

[8] 7.1.3

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **159 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is connected over an AMP controller which can support guaranteed logical links.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [341 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over an AMP controller.<br>The L2CAP connection is in the CONFIG State.<br>L2CAP_ConfigReq<br>(Channel Mode = ERTM,<br>Ext Flow Spec = BE,<br>QoS and Flush Timeout omitted) RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Success’,<br>Channel Mode = ERTM)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.118: L2CAP/LSC/BV-09-C [Premature Success in Configuration Response, AMP Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT stays in CONFIG state after receiving L2CAP_ConfigRsp with results before receiving L2CAP_ConfigRsp with “Pending” status. IUT sends L2CAP_DisconnectReq with the same channel specified.

## **L2CAP/LSC/BI-10-C [Mismatched Service Type, Best Effort, AMP Channel]**

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type “Best Effort” and receives a Configuration request packet with an Extended Flow Specification containing service type “Guaranteed”.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

- [8] 7.1.3

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **160 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is connected over an AMP controller which can support guaranteed logical links.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [339 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over an AMP controller.<br>The L2CAP connection is in the CONFIG State.<br>L2CAP_ConfigReq<br>(Channel Mode = ERTM,<br>Ext Flow Spec = BE,<br>QoS and Flush Timeout omitted) RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>L2CAP_ConfigReq ERTX<br>(Channel Mode = ERTM,<br>Ext Flow Spec = GU,<br>QoS and Flush Timeout omitted)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.119: L2CAP/LSC/BV-10-I [Mismatched Service Type, Best Effort, AMP Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT rejects mismatched L2CAP_ConfigRsp by sending an L2CAP_DisconnectReq.

## **L2CAP/LSC/BI-11-C [Mismatched Service Type, Guaranteed, AMP Channel]**

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type “Guaranteed” and receives a Configuration request packet with an Extended Flow Specification containing service type “Best Effort”.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

- [8] 7.1.3

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **161 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is connected over an AMP controller which can support guaranteed logical links.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [340 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL Connection Established.<br>An L2CAP channel established over an AMP controller.<br>The L2CAP connection is in the CONFIG State.<br>L2CAP_ConfigReq<br>(Channel Mode = ERTM,<br>Ext Flow Spec = Guaranteed)<br>RTX<br>L2CAP_ConfigRsp<br>(Result = ‘Pending’)<br>L2CAP_ConfigReq ERTX<br>(Channel Mode = ERTM,<br>Ext Flow Spec = BE)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.120: L2CAP/LSC/BI-11-C [Mismatched Service Type, Guaranteed, AMP Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT rejects mismatched L2CAP_ConfigRsp by sending an L2CAP_DisconnectReq.

## **L2CAP/LSC/BV-12-C [Remote Failed on Guaranteed, AMP Channel]**

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type “Guaranteed” and after receiving a Configuration Response with result “Pending” it receives a Configuration request packet with a “Failure” result.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

- [8] 7.1.3

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **162 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An ACL connection has been established by the Lower Tester.

- L2CAP channel is connected over an AMP controller which can support guaranteed logical links.

- The IUT is in CONFIG state.

- Test Procedure

**==> picture [341 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL connection established<br>An L2CAP channel established over an AMP controller<br>The L2CAP connection is in the CONFIG state<br>L2CAP_ConfigReq<br>(Channel Mode = STM,<br>Ext Flow Spec = ‘Guaranteed’) RTX<br>L2CAP_ConfigRsp<br>(Result = 'Pending’)<br>ERTX<br>L2CAP_ConfigRsp<br>(Result = ‘Failure – flow spec rejected’)<br>L2CAP_DisconnectReq<br>(same channel)<br>**----- End of picture text -----**<br>

_Figure 4.121: L2CAP/LSC/BV-12-C [Remote Failed on Guaranteed, AMP Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT detects L2CAP_ConfigRsp indicating ‘no resources’ (failure) by sending an L2CAP_DisconnectReq.

## **4.11.12 Create Channel (CCH)**

Verify the correct implementation of the create channel request and response of the L2CAP layer.

## **L2CAP/CCH/BV-01-C [Create Channel Request for an AMP Physical Link]**

- Test Purpose

Verify that the IUT can request the creation of an L2CAP channel to run over an existing AMP physical link.

- Reference

- [1] 4.14, 4.15

- [8] 6.1, Figure 6.3

- Initial Condition

- The AMP Physical Link for the Controller ID exists.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **163 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [340 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in CLOSED state.<br>AMP OpenChannel_Req<br>L2CAP_CreateChannel_Req<br> (ID, length, PSM, SCID, AMP Controller<br>ID)<br>L2CAP_CreateChannel_Rsp optional<br>(ID, length, DCID, SCID, Result = pending,<br>Status)<br>L2CAP_CreateChannel_Rsp<br>(ID, length, DCID, SCID, Result = success,<br>Status) AMP OpenChannnel_Res<br>(success)<br>**----- End of picture text -----**<br>

_Figure 4.122: L2CAP/CCH/BV-01-C [Create Channel Request for an AMP Physical Link] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_CreateChannel_Req over the signaling channel using a dynamically allocated SCID, a valid PSM value, and the Controller ID matching the ID for the existing AMP channel.

The IUT enters the OPEN state.

**L2CAP/CCH/BV-02-C [Create Channel Request for an AMP Physical Link – Refused]**

- Test Purpose

Verify that the IUT can request the creation of an L2CAP channel to run over an existing AMP physical link, and to recover if the request is refused by the Lower Tester (L2CAP create channel response).

- Reference

- [1] 4.14, 4.15

- [8] 6.1, Figure 6.3

- Initial Condition

- The AMP Physical Link for the Controller ID exists.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **164 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

The ‘Connection Refused’ code sent by the Lower Tester may include: PSM not supported; Security Block; No Resources; Controller ID not supported.

**==> picture [340 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in CLOSED state.<br>AMP OpenChannel_Req<br>L2CAP_CreateChannelReq<br> (ID, length, PSM, SCID,<br>Controller ID=AMP)<br>L2CAP_CreateChannel_Rsp<br>(ID, length, DCID, SCID,<br>Result = ‘Connection Refused’, Status)<br>IUT returns to<br>CLOSED state.<br>AMP OpenChannel_Res<br>(failure)<br>**----- End of picture text -----**<br>

_Figure 4.123: L2CAP/CCH/BV-02-C [Create Channel Request for an AMP Physical Link – Refused] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_CreateChanAMP_Req over the signaling channel using a dynamically allocated SCID, a valid PSM value, and the Controller ID matching the ID for the existing AMP channel.

The IUT returns to the CLOSED state.

The IUT indicates failure to the Upper Tester.

**L2CAP/CCH/BV-03-C [Create Channel Request for an AMP Physical Link – Failed]**

- Test Purpose

Verify that the IUT can request the creation of an L2CAP channel to run over an existing AMP physical link, and to recover if the request is accepted (L2CAP create channel response = “Pending”) by the Lower Tester but is failed after initiation.

- Reference

[1] 4.14, 4.15

[8] 6.1, Figure 6.3

- Initial Condition

- The AMP Physical Link for the Controller ID exists.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **165 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

The ‘Connection Refused’ code sent by the Lower Tester may include: PSM not supported; Security Block; No Resources; Controller ID not supported.

**==> picture [340 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in CLOSED state.<br>AMP OpenChannel_Req<br>L2CAP_CreateChannelReq<br> (ID, length, PSM, SCID, Controller ID)<br>L2CAP_CreateChannelRsp<br>(ID, length, DCID, SCID, Result = pending,<br>Status)<br>L2CAP_CreateChannelRsp<br>(ID, length, DCID, SCID,<br>Result = ‘Connection Refused’, Status) AMP OpenChannel_Res<br>(failure)<br>**----- End of picture text -----**<br>

_Figure 4.124: L2CAP/CCH/BV-03-C [Create Channel Request for an AMP Physical Link – Failed] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_CreateChannelReq over the signaling channel using a dynamically allocated SCID, a valid PSM value, and the Controller ID matching the ID for the existing AMP channel.

The IUT returns to the CLOSED state.

The IUT indicates failure to the Upper Tester.

## **L2CAP/CCH/BV-04-C [Create Channel Response for an AMP Physical Link]**

- Test Purpose

Verify that the IUT can receive and handle a request for connection establishment and configuration of an L2CAP channel to run over an existing AMP physical link.

- Reference

[1] 4.14, 4.15

- Initial Condition

- The AMP Physical Link for the Controller ID exists.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **166 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [338 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in CLOSED state.<br>L2CAP_CreateChannel_Req<br>(ID, length, PSM, SCID, controller ID)<br>RTX Timer<br>(20 Seconds)<br>L2CAP_CreateChannel_Rsp<br>(ID, length, DCID, SCID, Result, Status)<br>**----- End of picture text -----**<br>

_Figure 4.125: L2CAP/CCH/BV-04-C [Create Channel Response for an AMP Physical Link] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_CreateChannelRsp with a result code of “Connection Successful” (0x0000) or “Connection Pending” (0x0001) before the Lower Tester RTX timer expires. If the result code = “Connection Pending”, the status code is 0x0000 - 0x0002.

The SCID in the response is equal to the SCID code in the request.

## **4.11.13 Move Channel (MCH)**

Verify the correct implementation of the Move Channel request and response of the L2CAP layer.

**L2CAP/MCH/BV-01-C [Move ERTM Channel Request for BR/EDR to AMP – Success]**

- Test Purpose

Verify that the IUT can request the move of an L2CAP ERTM channel from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition

- An L2CAP ERTM channel exists between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **167 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.126 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 332] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm<br>(success)<br>S-frame (over AMP on CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over AMP CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.126: L2CAP/MCH/BV-01-C [Move ERTM Channel Request for BR/EDR to AMP – Success] MSC_

## • Test Condition

The Lower Tester responds with a result field = “Move Pending” and configures the new AMP channel so the channel can be move from BR/EDR to AMP.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm with a result code = “Move Success” (0x0000). After it receives the L2CAP_MoveChanConfirmRsp from the Lower Tester, it sends a Receiver Ready message over the new AMP link on the same CID as before the move. The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **168 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- **L2CAP/MCH/BV-02-C [Move ERTM Channel Request for BR/EDR to AMP – Refused]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP ERTM channel from a BR/EDR link to an AMP link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the BR link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

-

## Initial Condition

- An L2CAP ERTM channel exists between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.127 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The ‘Move Refused’ result code sent by the Lower Tester may include: Controller ID not supported; new Controller ID is same as old Controller ID; configuration not supported; channel not allowed to be moved.

**==> picture [340 x 302] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVE_CHANNEL confirm (refused)<br>S-frame (over BR/EDR CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over BR/EDR CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.127: L2CAP/MCH/BV-02-C [Move ERTM Channel Request for BR/EDR to AMP – Refused] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **169 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Condition

The Lower Tester responds with result= “Move Refused” so that the Move Channel Request from the IUT fails.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move failure – one or both sides refuse” (0x0001) and it sends a Receiver Ready message over the BR/EDR link on the same CID as before the move attempt. The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

- **L2CAP/MCH/BV-03-C [Move ERTM Channel Request for BR/EDR to AMP – AMP Fail]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP channel from a BR/EDR link to an AMP link, and recover if the AMP channel creation fails. In this case the channel remains in state OPEN over the BR link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

-

- Initial Condition

- An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.128 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR channel after the unsuccessful move attempt.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **170 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**==> picture [340 x 334] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Failed (0x4)<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVEresponse (failed)_CHANNEL<br>S-frame (over BR/EDR on CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over BR/EDR CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.128: L2CAP/MCH/BV-03-C [Move ERTM Channel Request for BR/EDR to AMP – AMP Fail] MSC_

- Test Condition

The Lower Tester responds with a result field = “Move Pending” and configures the new AMP channel so the channel can be move from BR/EDR to AMP. However, the AMP channel configuration fails, so the Lower Tester replies with a failure indication.

-

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move failure – one or both sides refuse” (0x0001) and it sends a Receiver Ready message over the BR/EDR link on the same CID as before the move attempt. The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

- **L2CAP/MCH/BV-04-C [Move ERTM Channel Request for AMP to BR/EDR – Success]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP ERTM channel from an AMP link to a BR link.

If the operation is successful, the channel has to be in state OPEN over the BR link.

- Reference

[1] 4.16, 4.17, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **171 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT is in OPEN state.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.129 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The IUT and the Lower Tester move to the new BR/EDR channel successfully.

**==> picture [339 x 346] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>Admission Control<br>ERTX<br>Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVEconfirm (success)_CHANNEL.<br>S-frame (over BR/EDR on CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over BR/EDR CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.129: L2CAP/MCH/BV-04-C [Move ERTM Channel Request for AMP to BR/EDR – Success] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm with a result code of “Move Success” (0x0000). After it receives an L2CAP_MoveChanConfirmRsp from the Lower Tester, it sends a Receiver Ready message over the new BR/EDR link on the same CID as before the move.

The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **172 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- **L2CAP/MCH/BV-05-C [Move ERTM Channel Request for AMP to BR/EDR – Refused]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP channel from an AMP link to a BR link.

If the operation is refused by the Lower Tester, the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition

- The IUT is in OPEN state.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.130 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful refused by the Lower Tester. The IUT and the Lower Tester return to the AMP channel after the unsuccessful move attempt.

**==> picture [339 x 310] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller<br>ID=0x00)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result=<br>configuration not supported (0x0004))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initatorCID) MOVEConfirm (failure)_CHANNEL.<br>S-frame (over AMP Link CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over AMP Link CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.130: L2CAP/MCH/BV-05-C [Move ERTM Channel Request for AMP to BR/EDR – Refused] MSC_

- Test Condition

The AMP channel requires service not available on BR/EDR, e.g. much more bandwidth.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **173 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move refused - Configuration not supported” (0x0004).

The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

- **L2CAP/MCH/BV-06-C [Move ERTM Channel Response for BR/EDR to AMP – Success]**

- Test Purpose

Verify that the IUT can receive and handle a request to move a L2CAP channel from a BR/EDR link to an AMP link.

- Reference

- [1] 4.16, 4.17, 9.2

- Initial Condition

- An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.131 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **174 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**==> picture [340 x 329] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID) MOVEIndication _CHANNEL<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>S-frame (over AMP on CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over AMP CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.131: L2CAP/MCH/BV-06-C [Move ERTM Channel Response for BR/EDR to AMP – Success] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanRsp with a result code of “Move Success” (0x0000) and responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) on the AMP link.

**L2CAP/MCH/BV-07-C [Move ERTM Channel Response for BR/EDR to AMP – Failure]**

- Test Purpose

Verify that the IUT can receive and handle a request to move a L2CAP channel from a BR/EDR link to an AMP link where the move operation fails.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition

- An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **175 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.132 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID) MOVEIndication _CHANNEL<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>S-frame (over BR/EDR on CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over BR/EDR CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.132: L2CAP/MCH/BV-07-C [Move ERTM Channel Response for BR/EDR to AMP – Failure] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanRsp a result code of “Move Success” (0x0000) and responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) over the BR/EDR link.

**L2CAP/MCH/BV-08-C [Move ERTM Channel Response for AMP to BR/EDR – Success]**

- Test Purpose

Verify that the IUT can receive and handle a request to move a L2CAP channel from an AMP link to a BR/EDR link.

- Reference

[1] 4.16, 4.17, 9.2

-

- Initial Condition

- An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **176 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.133 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [333 x 367] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=X<br>(ID, length, initiatorCID, Dest Controller ID) MOVEIndication _CHANNEL<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX<br>Admission Control<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>S-frame (over BR/EDR on CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over BR/EDR CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.133: L2CAP/MCH/BV-08-C [Move ERTM Channel Response for AMP to BR/EDR – Success] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanRsp with result code success (0) and the IUT responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) over the AMP link.

**L2CAP/MCH/BV-09-C [Move ERTM Channel Response for AMP to BR/EDR – Failure]**

- Test Purpose

Verify that the IUT can receive and handle a request to move a L2CAP channel from an AMP link to a BR/EDR link where the move operation fails.

- Reference

- [1] 4.16, 4.17, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **177 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.134 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [333 x 373] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=X<br>(ID, length, initiatorCID, Dest Controller ID) MOVEIndication _CHANNEL<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX<br>Admission Control<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>S-frame (over AMP on CID=X)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over AMP CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.134: L2CAP/MCH/BV-09-C [Move ERTM Channel Response for AMP to BR/EDR – Failure] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanRsp with result code of “Move Success” (0x0000) and responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) over the AMP link.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **178 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/MCH/BV-10-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP]**

- Test Purpose

Verify that the IUT can move the active L2CAP ERTM channel from a BR/EDR link to an AMP link with no data loss above L2CAP.

- Reference

[1] 4.16, 4.17, 9.2

-

- Initial Condition

- A BR/EDR L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.135 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 371] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>The channel is configured to use ERTM<br>I-frame (over BR/EDR CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>RTX<br>S-frame (over BR/EDR on CID=X)<br>Timer (RR, ReqSeq=1, P=0, F=0) Data sent to Upper Tester<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, DestController ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>ERTX Timer pending (0x0001))<br>Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>S-frame (over AMP on CID=X)<br>(RR, ReqSeq=1, P=1, F=0)<br>I-frame (over AMP CID=X)<br>(TxSeq=1, ReqSeq=0, F=1) Data sent to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.135: L2CAP/MCH/BV-10-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **179 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT transmits a Receiver Ready packet over the new AMP channel at the end of the move with ReqSeq = 1.

**L2CAP/MCH/BV-11-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP – Unacknowledged Data]**

- Test Purpose

Verify that the IUT can move the active L2CAP channel from a BR/EDR link to an AMP link with no data loss above L2CAP, and recover from data sent before the move but not yet acknowledged by the Lower Tester.

- Reference

- [1] 4.16, 4.17, 9.2

-

- Initial Condition

- A BR/EDR L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **180 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.136 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 353] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>The channel is configured to use ERTM<br>I-frame (over BR/EDR CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, DestController ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>Logical Link Creation<br>ERTX Timer L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>S-frame (over AMP CID=X)<br>(RR ReqSeq =0, P=1, F=0)<br>S-frame (over AMP on CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>I-frame (over AMP CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.136: L2CAP/MCH/BV-11-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP – Unacknowledged Data] MSC_

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT transmits an RR(P=1, ReqSeq = 0) over the new AMP channel at the end of the move and it retransmits the I-frame over the new AMP channel when told by the Lower Tester.

## **L2CAP/MCH/BV-12-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR]**

- Test Purpose

Verify that the IUT can move the active L2CAP channel from an AMP link to a BR/EDR link with no data loss above L2CAP.

- Reference

[1] 4.16, 4.17, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **181 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Initial Condition

- An AMP L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## • Test Procedure

Figure 4.137 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [339 x 374] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>That channel is configured to use ERTM<br>I-frame (over AMP CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>RTX Data sent to Upper Tester<br>S-frame (over AMP on CID=X)<br>Timer<br>(RR, ReqSeq=1, P=0, F=0)<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, DestController ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Admission Control<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>S-frame (over BR/EDR on CID=X)<br>(RR, ReqSeq=1, P=1, F=0)<br>I-frame (over BR/EDR CID=X)<br>(TxSeq=1, ReqSeq=0, F=1) Data sent to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.137: L2CAP/MCH/BV-12-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR] MSC_

- Test Condition

In order for the Lower Tester to send an I-frame in response to the RR(P=1) at the end of the test it must be pending before the RR(P=1) is received.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **182 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT sends an RR(P=1, ReqSeq=0) over the BR/EDR link at the end of the move and passes received data to the Upper Tester.

**L2CAP/MCH/BV-13-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR – Unacknowledged Data]**

- Test Purpose

Verify that the IUT can move the active L2CAP channel from an AMP link to a BR/EDR link with no data loss above L2CAP, and recover from data sent before the move but not yet acknowledged by the Lower Tester.

- Reference

- [1] 4.16, 4.17, 9.2

-

- Initial Condition

- An AMP L2CAP channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **183 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.138 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [339 x 367] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>The channel is configured to use ERTM<br>I-frame (over AMP CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, DestController ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>Admission Control<br>ERTX Timer L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>S-frame (over BR/EDR CID=X)<br>(RR ReqSeq = 0, P=1, F=0)<br>S-frame (over BR/EDR on CID=X)<br>(RR, ReqSeq=m, P=0, F=1)<br>I-frame (over BR/EDR CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.138: L2CAP/MCH/BV-13-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR – Unacknowledged Data] MSC_

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT sends an RR(P=1, ReqSeq = 0) over the BR/EDR link at the end of the move operation and retransmits the I-frame over the BR/EDR channel when requested by the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **184 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/MCH/BV-14-C [Move Collision – ERTM]**

- Test Purpose

Verify that the IUT can properly handle a move collision when both the IUT and Lower Tester attempt to move an ERTM channel from the BR/EDR link to an AMP link simultaneously.

- Reference

- [1] 4.16, 4.17, 9.2

- Initial Condition

- An L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been no data transfer on the channel.

- The AMP Physical Link Exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.139 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **185 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**==> picture [342 x 570] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Refused collision (0x0005))<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Logical Link Creation<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm<br>S-frame (over AMP on CID=X) (success)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over AMP CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Refused collision (0x0005))<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Logical Link Creation<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm<br>S-frame (over AMP on CID=X) (success)<br>(RR, ReqSeq=0, P=1, F=0)<br>S-frame (over AMP CID=X)<br>(RR, ReqSeq=0, P=0, F=1)<br>**----- End of picture text -----**<br>

_Figure 4.139: L2CAP/MCH/BV-14-C [Move Collision – ERTM] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **186 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

Move operation is successful.

## ALT1:

The IUT’s BD_ADDR is larger than the Lower Tester’s BD_ADDR so the IUT sends L2CAP_MoveChannelRsp with result code “Move refused – Move Channel collision” (0x0005). It sends RR(P=1, ReqSeq = 0) at the end of the move operation over the AMP link.

## ALT2:

The IUT’s BD_ADDR is smaller than the Lower Tester’s BD_ADDR so the IUT sends L2CAP_MoveChannelRsp with result code of “Move Pending” (0x0001). It responds to the RR(P=1) from the Lower Tester with RR(F=1) over the AMP link.

**L2CAP/MCH/BV-15-C [Move Channel Request for BR/EDR to AMP (STM Source) – Success]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

-

## Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **187 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.140 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>Command IUT to send data<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.140: L2CAP/MCH/BV-15-C [Move Channel Request for BR/EDR to AMP (STM Source) – Success] MSC_

- Test Condition

The Lower Tester responds with result= Move Pending and create the new AMP logical link so the channel can be move from BR/EDR to AMP.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm with a result code of “Move Success” (0x0000). After receiving the L2CAP_MoveChanConfirmRsp from the Lower Tester, it sends an I-frame.

## **L2CAP/MCH/BV-16-C [Move Channel Request for BR/EDR to AMP (STM Sink) – Success]**

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **188 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.141 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 341] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.141: L2CAP/MCH/BV-16-C [Move Channel Request for BR/EDR to AMP (STM Sink) – Success] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm with a result code of “Move Success” (0x0000). IUT receives an I-frame on the AMP and passes data up to the Upper Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **189 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/MCH/BV-17-C [Move Channel Request for BR/EDR to AMP (STM Source) – Refused]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the BR/EDR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

-

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.142 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR link after the unsuccessful move attempt.

**==> picture [340 x 302] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVE_CHANNEL confirm (refused)<br>Command IUT to send data<br>I-frame (over BR/EDR CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.142: L2CAP/MCH/BV-17-C [Move Channel Request for BR/EDR to AMP (STM Source) – Refused] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **190 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move failure – one or both sides refuse” (0x0001) and it sends an I-frame over the BR/EDR link on the same CID as before the move attempt.

**L2CAP/MCH/BV-18-C [Move Channel Request for BR/EDR to AMP (STM Sink) – Refused]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the BR link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

-

## Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.143 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR link after the unsuccessful move attempt.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **191 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**==> picture [340 x 302] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVE_CHANNEL confirm (refused)<br>I-frame (over BR/EDR CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data set to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.143: L2CAP/MCH/BV-18-C [Move Channel Request for BR/EDR to AMP (STM Sink) – Refused] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of Failure (0x0001) and it passes received data to the Upper Tester.

**L2CAP/MCH/BV-19-C [Move Channel Request for BR/EDR to AMP (STM Source) – AMP Fail]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link, and recover if the AMP logical link creation fails. In this case the channel remains in state OPEN over the BR link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

-

## Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **192 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.144 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR link after the unsuccessful move attempt.

**==> picture [341 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>Command IUT to send data<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.144: L2CAP/MCH/BV-19-C [Move Channel Request for BR/EDR to AMP (STM Source) – AMP Fail] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move Failure – one or both sides refuse” (0x0001) and sends an I-frame over the BR/EDR link on the same CID as before the move attempt.

**L2CAP/MCH/BV-20-C [Move Channel Request for BR/EDR to AMP (STM Sink) – AMP Failed]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link, and recover if the AMP Logical Link creation fails. In this case the channel remains in state OPEN over the BR link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **193 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.145 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR channel after the unsuccessful move attempt.

**==> picture [341 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Command IUT to send data<br>**----- End of picture text -----**<br>

_Figure 4.145: L2CAP/MCH/BV-20-C [Move Channel Request for BR/EDR to AMP (STM Sink) – AMP Failed] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move Failure – one or both sides refuse” (0x0001) and passes the received data to the Upper Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **194 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/MCH/BV-21-C [Move Channel Request for AMP to BR/EDR (STM Source) – Success]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference [1] 4.16, 4.17, 4.18, 9.2

-

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists with a guaranteed logical link. The requirements for that AMP channel does not exceed the capabilities of EDR.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.146 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 327] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation on BR/EDR<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>Command IUT to send data<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.146: L2CAP/MCH/BV-21-C [Move Channel Request for AMP to BR/EDR (STM Source) – Success] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **195 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm with a result code of “Move Success” (0x0000). After receiving the L2CAP_MoveChanConfirmRsp from the Lower Tester, it sends an I-frame over BR/EDR.

**L2CAP/MCH/BV-22-C [Move Channel Request for AMP to BR/EDR (STM Sink) – Success]**

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from an AMP link to a BR/EDR link. If the operation is successful, the channel is in state OPEN over the BR/EDR link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

-

## Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **196 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.147 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Admission Control<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.147: L2CAP/MCH/BV-22-C [Move Channel Request for AMP to BR/EDR (STM Sink) – Success] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm with a result code of “Move Success” (0x0000). IUT receives I-frame on BR/EDR and passes data up to the Upper Tester.

**L2CAP/MCH/BV-23-C [Move Channel Request for AMP to BR/EDR (STM Source) – Refused]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data source from an AMP link to a BR/EDR link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the AMP link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **197 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.148 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP link after the unsuccessful move attempt.

**==> picture [340 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVE_CHANNEL confirm (refused)<br>Command IUT to send data<br>I-frame (over AMP CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.148: L2CAP/MCH/BV-23-C [Move Channel Request for AMP to BR/EDR (STM Source) – Refused] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move failure – one or both sides refuse” (0x0001) and it sends an I-frame over the AMP link on the same CID as before the move attempt.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **198 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- **L2CAP/MCH/BV-24-C [Move Channel Request for AMP to BR/EDR (STM Sink) – Refused]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data sink from an AMP link to a BR/EDR link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

-

## Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.149 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP channel after the unsuccessful move attempt.

**==> picture [340 x 312] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVE_CHANNEL confirm (refused)<br>I-frame (over AMP CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data set to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.149: L2CAP/MCH/BV-24-C [Move Channel Request for AMP to BR/EDR (STM Sink) – Refused] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **199 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move Failure – one or both side refuse” (0x0001) and it passes received data to the Upper Tester.

**L2CAP/MCH/BV-25-C [Move Channel Request for AMP to BR/EDR (STM Source) – AMP Fail]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data source from an AMP link to a BR/EDR link, and recover if the admission control fails. In this case the channel remains in state OPEN over the AMP link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

-

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.150 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP link after the unsuccessful move attempt.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **200 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**==> picture [341 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Admission Control<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>Command IUT to send data<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.150: L2CAP/MCH/BV-25-C [Move Channel Request for AMP to BR/EDR (STM Source) – AMP Fail] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move failure – one or both sides refuse” (0x0001) and sends an I-frame over the AMP link on the same CID as before the move attempt.

**L2CAP/MCH/BV-26-C [Move Channel Request for AMP to BR/EDR (STM Sink) – AMP Failed]**

- Test Purpose

Verify that the IUT can request the move of a L2CAP Streaming Mode channel where the IUT is the data sink from an AMP link to a BR/EDR link, and recover if the Admission Control fails. In this case the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

-

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **201 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.151 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP link after the unsuccessful move attempt.

**==> picture [304 x 301] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Admission Control<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>refused (0x0002-0x0006))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Command IUT to send data<br>**----- End of picture text -----**<br>

_Figure 4.151: L2CAP/MCH/BV-26-C [Move Channel Request for AMP to BR/EDR (STM Sink) – AMP Failed] MSC_

- Expected Outcome

Pass verdict

The IUT transmits an L2CAP_MoveChanConfirm packet with a result code of “Move failure – one or both sides refuse” (0x0001) and passes the received data to the Upper Tester.

**L2CAP/MCH/BV-27-C [Move Channel Response for BR/EDR to AMP (STM Source) – Success]**

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **202 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.152 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 317] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1 MOVEindication_CHANNEL<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>Command IUT to send data<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.152: L2CAP/MCH/BV-27-C [Move Channel Response for BR/EDR to AMP (STM Source) – Success] MSC_

- Expected Outcome

## Pass verdict

The channel is moved successfully and the IUT sends an I-frame over the AMP link after the move completes.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **203 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/MCH/BV-28-C [Move Channel Response for BR/EDR to AMP (STM Sink) – Success]**

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

-

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

-

- Test Procedure

Figure 4.153 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 317] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=X<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.153: L2CAP/MCH/BV-28-C [Move Channel Response for BR/EDR to AMP (STM Sink) – Success] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **204 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The channel is successfully moved from the BR/EDR link to the AMP link and the received data is passed to the Upper Tester.

**L2CAP/MCH/BV-29-C [Move Channel Response for AMP to BR/EDR (STM Source) – Success]**

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source. The channel is moved from an AMP to a BR/EDR link. If the operation is successful, the channel is in state OPEN over the BR/EDR link.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **205 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.154 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [339 x 399] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX<br>Admission Control<br>Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>Command IUT to send data<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.154: L2CAP/MCH/BV-29-C [Move Channel Response for AMP to BR/EDR (STM Source) – Success] MSC_

- Test Condition

The channel’s Extended Flow Specification is valid for a BR/EDR link.

-

- Expected Outcome

## Pass verdict

The channel is moved successfully and the IUT sends an I-frame over the BR/EDR link after the move completes.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **206 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/MCH/BV-30-C [Move Channel Response for AMP to BR/EDR (STM Sink) – Success]**

- Test Purpose

Verify that the IUT can respond to a move request for an L2CAP Streaming Mode channel where the IUT is the data sink. The channel is moved from an AMP link to a BR/EDR link. If the operation is successful, the channel is in state OPEN over the BR/EDR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.155 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [315 x 348] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=X<br>(ID, length, initiatorCID, Dest Controller ID)<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX<br>Admission Control<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (success)<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.155: L2CAP/MCH/BV-30-C [Move Channel Response for AMP to BR/EDR (STM Sink) – Success] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **207 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Condition

The channel’s Extended Flow Specification is valid for a BR/EDR link.

- Expected Outcome

## Pass verdict

The channel is successfully moved from the AMP link to the BR/EDR link and the received data is passed to the Upper Tester.

**L2CAP/MCH/BV-31-C [Move Channel Response for BR/EDR to AMP (STM Source) – Failed]**

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source and is able to recover when the move operation fails. The channel is to be moved from a BR/EDR link to an AMP link but move operation fails.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **208 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.156 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>Command IUT to send data<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.156: L2CAP/MCH/BV-31-C [Move Channel Response for BR/EDR to AMP (STM Source) – Failed] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an I-frame over the BR/EDR link after the failed move operation completes.

**L2CAP/MCH/BV-32-C [Move Channel Response for BR/EDR to AMP (STM Sink) – Failed]**

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data sink and recover when the move operation fails. The channel is to not be moved from a BR/EDR link to an AMP link, but instead remains in the BR/EDR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The AMP Physical Link exists.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **209 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.157 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=X<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Timer Logical Link Creation<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>I-frame (over BR/EDR on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.157: L2CAP/MCH/BV-32-C [Move Channel Response for BR/EDR to AMP (STM Sink) – Failed] MSC_

- Expected Outcome

## Pass verdict

The IUT passed received data to the Upper Tester after the failed move operation completes.

**L2CAP/MCH/BV-33-C [Move Channel Response for AMP to BR/EDR (STM Source) – Failed]**

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source and recover when the move operation fails. The channel is not to be moved from an AMP to a BR/EDR link, but instead remains on the AMP.

- Reference

- [1] 4.16, 4.17, 4.18, 9.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **210 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## • Test Procedure

Figure 4.158 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [334 x 386] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX<br>Admission Control<br>Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID) MOVE_CHANNEL confirm (failure)<br>Command IUT to send data<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.158: L2CAP/MCH/BV-33-C [Move Channel Response for AMP to BR/EDR (STM Source) – Failed] MSC_

- Test Condition

The channel’s Extended Flow Specification is valid for a BR/EDR link.

-

- Expected Outcome

## Pass verdict

The IUT sends an I-frame over the AMP link after the failed move operation completes.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **211 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- **L2CAP/MCH/BV-34-C [Move Channel Response for AMP to BR/EDR (STM Sink) – Failed]**

- Test Purpose

Verify that the IUT can respond to a move request for an L2CAP Streaming Mode channel where the IUT is the data sink and recover when the move operation fails. The channel is not to be moved from an AMP link to a BR/EDR link, but instead remains on the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition

- An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.

- The BR/EDR Physical Link exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **212 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.159 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 386] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over AMP.<br>No I-frames have been sent over the channel.<br>L2CAP_MoveChanReq on CID=X<br>(ID, length, initiatorCID, Dest Controller ID)<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX<br>Admission Control<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Failure (0x0001))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVE_CHANNEL confirm (failure)<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>Data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.159: L2CAP/MCH/BV-34-C [Move Channel Response for AMP to BR/EDR (STM Sink) – Failed] MSC_

- Test Condition

The channel’s Extended Flow Specification is valid for a BR/EDR link.

- Expected Outcome

## Pass verdict

The IUT passes received data to the Upper Tester after the failed moved operation completes.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **213 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/MCH/BV-35-C [Move Collision – STM Source]**

- Test Purpose

Verify that the IUT can properly handle a move collision when both the IUT and Lower Tester attempt to move a Streaming Mode channel from the BR/EDR link to an AMP link at the same time where the IUT is the data source.

- Reference

- [1] 4.16, 4.17, 9.2

-

- Initial Condition

- An L2CAP Streaming Mode channel exists between the IUT and the Lower Tester. There has been no data transfer on the channel.

- The AMP Physical Link Exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **214 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.160 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [340 x 585] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanReq on CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>ALT 1<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Refused collision (0x0005))<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Logical Link Creation<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>ALT 2<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Refused collision (0x0005))<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>ERTX Logical Link Creation<br> Timer<br>L2CAP_MoveChanRsp on CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP(ID, length, initiatorCID, Result=Move _MoveChanConfirm on CID=1<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRsp on CID=1<br>(ID, length, initiatorCID)<br>MOVE_CHANNEL confirm (success)<br>Command IUT to send data<br>I-frame (over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.160: L2CAP/MCH/BV-35-C [Move Collision – STM Source] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **215 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

Move operation is successful.

## ALT1:

The IUT’s BD_ADDR is larger than the Lower Tester’s BD_ADDR so the IUT sends L2CAP_MoveChannelRsp with result code of “Move refused – Move Channel collision” (0x0005). It sends an I-frame at the end of the move operation over the AMP link.

## ALT2:

The IUT’s BD_ADDR is smaller than Lower Tester’s BD_ADDR so IUT sends L2CAP_MoveChannelRsp with result code of “Move Pending” (0x0001). It sends an I-frame at the end of the move operation over the AMP link.

## **L2CAP/MCH/BV-36-C [Move Collision – STM Sink]**

- Test Purpose

Verify that the IUT can properly handle a move collision when both the IUT and Lower Tester attempt to move a Streaming Mode channel from the BR/EDR link to an AMP link at the same time where the IUT is the data sink.

- Reference

- [1] 4.16, 4.17, 9.2

-

## Initial Condition

- An L2CAP Streaming Mode channel exists between the IUT and the Lower Tester. There has been no data transfer on the channel.

- The AMP Physical Link Exists.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **216 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.161 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

|L2CAP_MoveChanReqon CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>Upper Tester<br>IUT<br>Lower Tester<br>IUT is in OPEN State On L2CAP Channel X over BR/EDR.<br>No I-frames have been sent over the channel.<br>MOVE_CHANNEL request<br>L2CAP_MoveChanReqon CID=1<br>(ID, length, initiatorCID, Dest Controller ID)|Lower Tester|Lower Tester|Lower Tester||IUT|IUT|IUT|||Upper Tester|Upper Tester|
||||IUT is in OPEN State On L2CAP Cha<br>No I-frames have been sent ov||||nnel X over BR/EDR.<br>er the channel.|||||
||||L2CAP_MoveChanReqon CID=1<br>(ID, length, initiatorCID, Dest Controller ID)<br>L2CAP_MoveChanReqon CID=1<br>(ID, length, initiatorCID, Dest Controller ID)||||MOVE_CHANNEL request|||||
|ERTX<br>Timer|||L2CAP_MoveChanRspon CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>L2CAP_MoveChanConfirm on CID=1<br>(ID, length, initiatorCID, Result=Move<br>Success (0x0000))<br>Logical Link Creation<br>L2CAP_MoveChanRspon CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRspon CID=1<br>(ID, length, initiatorCID)<br>L2CAP_MoveChanRspon CID=1<br>(ID, length, initiatorCID, Result= Move<br>Refused collision (0x0005))||||||||ALT 1|
|ERTX<br>Timer|||L2CAP_MoveChanRspon CID=1<br>(ID, length, initiatorCID, Result= Move<br>pending (0x0001))<br>L2CAP_MoveChanConfirm on CID=1<br>(ID, length, initiatorCID, Result=Move<br>Success (0x0000))<br>Logical Link Creation<br>L2CAP_MoveChanRspon CID=1<br>(ID, length, initiatorCID, Result= Move<br>Success (0x0000))<br>L2CAP_MoveChanConfirmRspon CID=1<br>(ID, length, initiatorCID)<br>L2CAP_MoveChanRspon CID=1<br>(ID, length, initiatorCID, Result= Move<br>Refused collision (0x0005))||||||||ALT 2|
||||I-frame(over AMP on CID=X)<br>(TxSeq=0, ReqSeq=0, F=0)||||MOVE_CHANNEL confirm<br>(success)<br>Data to Upper Tester|||||

_Figure 4.161: L2CAP/MCH/BV-36-C [Move Collision – STM Sink] MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **217 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

Move operation is successful.

## ALT1:

The IUT’s BD_ADDR is larger than Lower Tester’s BD_ADDR so IUT sends L2CAP_MoveChannelRsp with result code refused - collision (0x0005). It passes the received data to the Upper Tester at the end of the move operation.

## ALT 2:

The IUT’s BD_ADDR is smaller than the Lower Tester’s BD_ADDR so the IUT sends L2CAP_MoveChannelRsp with result code of “Move Pending” (0x0001). It passes the received data to the Upper Tester at the end of the move operation.

## **4.11.14 Enhanced Retransmission Mode with Extended Control Field (ECF)**

Verify the correct implementation of the Extended Control Field with Enhanced Retransmission Mode.

## **L2CAP/ECF/BV-01-C [Receive I-Frames with Extended Control Field]**

- Test Purpose

Verify that the IUT can receive in-sequence valid I-frames with the Extended Control Field and deliver L2CAP SDUs to the Upper Tester.

- Reference

[1] 3.3.2, 8.6

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID.

- The connection is configured as ERTM.

- No I-frames have been received from the Lower Tester.

- The IUT has configured a MTU and MPS size that is greater or equal to 48 bytes.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **218 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

Figure 4.162 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [334 x 358] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode.<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional (RR, 0 <= N(R) <= 1, P=0, F=0)<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 2, P=0, F=0)<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 3, P=0, F=0)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01)<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 4, P=0, F=0)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11)<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 5, P=0, F=0)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10) 48 Bytes of data to Upper Tester<br>S-Frame<br>Optional<br>(RR, 0 <= N(R) <= 6, P=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.162: L2CAP/ECF/BV-01-C [Receive I-Frames with Extended Control Field] MSC_

- Expected Outcome

## Pass verdict

Data in the received I-frame(s) match that sent by the Lower Tester.

SAR bits are set per specification.

F-bit is set to 0.

Complete SDU is sent to the Upper Tester.

All S-frames from the IUT contain the Extended Control Field.

**L2CAP/ECF/BV-02-C [Transmit I-Frames with Extended Control Field]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Extended Control Fields (SAR, F-bit, ReqSeq, TxSeq).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **219 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

[1] 3.3.2, 8.6

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID.

- The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.163 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [338 x 236] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 0)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 3, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.163: L2CAP/ECF/BV-02-C [Transmit I-Frames with Extended Control Field] MSC_

- Expected Outcome

## Pass verdict

The IUT sends I-frame(s) to the Lower Tester containing Extended Control Field.

Data in the I-frame(s) match that which was provided by the Upper Tester.

SAR bits are set per specification.

F-bit is set to 0.

## **L2CAP/ECF/BV-03-C [Acknowledging Received I-Frames with Extended Control Field]**

- Test Purpose

Verify that the IUT sends S-frame [RR] with Extended Control field and the Poll bit not set to acknowledge data received from the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **220 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

[1] 3.3.2, 8.6.1.1

- Initial Condition

- The IUT is in the INFO_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM. No I-frames have been received from the Lower Tester.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.164 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [375 x 196] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 1, P=0, F=0)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0)<br>Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 2, P=0, F=0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0)<br>Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 3, P=0, F=0)<br>**----- End of picture text -----**<br>

_Figure 4.164: L2CAP/ECF/BV-03-C [Acknowledging Received I-Frames with Extended Control Field] MSC_

- Expected Outcome

## Pass verdict

The IUT sends a Supervisory frame with S=RR, LastAckedReqSeq < ReqSeq <= last received I- frame’s TxSeq+1, F=0, P=0, Reserved bits = 0 and Extended Control Field.

## **L2CAP/ECF/BV-04-C [Send S-Frame [RR] with Extended Control Field and Poll Bit Set]**

- Test Purpose

Verify that the IUT sends an S-frame [RR] with the Extended Control field and the Poll bit set when its retransmission timer expires.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **221 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.165 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [376 x 171] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0) Retransmission<br>Timer<br>S-Frame<br>(RR, N(R) = 0, P = 1, F = 0)<br>Monitor Timer<br>S-Frame<br>(RR, N(R) = 1, P = 0, F = 1)<br>Retransmission<br>Timer of the IUT<br>**----- End of picture text -----**<br>

_Figure 4.165: L2CAP/ECF/BV-04-C [Send S-Frame [RR] with Extended Control Field and Poll Bit Set] MSC_

- Expected Outcome

## Pass verdict

The IUT sends an S-frame with Extended Control Field and with the POLL bit set after the IUT Retransmission Timer (as specified by Lower Tester during configuration) expires.

The IUT does not retransmit the I-frame after receiving an S-frame from the Lower Tester that acknowledges the previously sent I-frame.

## **L2CAP/ECF/BV-05-C [Respond to S-Frame [REJ] with Extended Control Field]**

- Test Purpose

Verify that the IUT retransmits I-frames with Extended Control Field starting from the sequence number specified in the S-frame [REJ] with an Extended Control Field.

- Reference

[1] 3.3.2, 8.6.1.2, 8.6.4

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin that is greater than 1 in the Configure Request sent to the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **222 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.166 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [376 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>I-Frame<br>Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>S-Frame<br>(REJ, N(R) = 0, P = 0, F = 0)<br>Monitor Timer of<br>the Tester I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission Retransmission<br>Timer of the IUT I-Frame Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.166: L2CAP/ECF/BV-05-C [Respond to S-Frame [REJ] with Extended Control Field] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the first I-frame requested in the REJ from the Lower Tester before the Monitor Timer of the Lower Tester expires, including the Extended Control Field.

The IUT retransmits the second I-frame requested in the REJ from the Lower Tester before the IUT Retransmission Timer expires.

**L2CAP/ECF/BV-06-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL bit Set]**

- Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame with an Extended Control Field. Verify that the IUT processes the acknowledgment of previously unacknowledged I- frames.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

-

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **223 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Figure 4.167 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [374 x 270] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>I-Frame<br>Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0)<br>S-Frame<br>(SREJ, N(R) = 1, P = 1, F = 0)<br>Monitor Timer of<br>the Tester I-Frame<br>(N(S) = 1, N(R) = 0, F = 1)<br>I-Frame Retransmission<br>(N(S) = 3, N(R) = 0, F = 0) Timer<br>S-Frame<br>(RR, N(R) = 2, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.167: L2CAP/ECF/BV-06-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL bit Set] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The I-frame retransmitted by the IUT has the Final bit = 1, and the Extended Control Field.

The IUT processes the acknowledgment of the first I-frame (N(S) = 0) from the SREJ received and consequently send the pending I-frame (N(S) = 3).

**L2CAP/ECF/BV-07-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL Bit Clear]**

- Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame with an Extended Control Field.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **224 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The channel is in the OPEN state and configured to use ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The MaxTransmit for the IUT is set to a value greater than 1.

- The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.

- Test Procedure

Figure 4.168 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [378 x 254] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0)<br>Retransmission<br>I-Frame<br>Timer<br>(N(S) = 1, N(R) = 0, F = 0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0)<br>S-Frame<br>(SREJ, N(R) = 1, P = 0, F = 0)<br>Monitor Timer of<br>the Tester I-Frame<br>(N(S) = 1, N(R) = 0, F = 0) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 3, P = 0, F = 0)<br>I-Frame<br>(N(S) = 3, N(R) = 0, F = 0) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 4, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.168: L2CAP/ECF/BV-07-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL Bit Clear] MSC_

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame, including an Extended Control Field, requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The IUT does not transmit I-frame (N(S) = 3) as a result of receiving the SREJ from the Lower Tester.

## **L2CAP/ECF/BV-08-C [Transmit I-Frames using Extended Control Field and SAR]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the extended control fields (SAR, F-bit, ReqSeq, TxSeq) when performing SAR.

- Reference

- [1] 3.3.2

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **225 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The connection is configured as ERTM.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The Lower Tester has configured a value for the MPS that ensures that the IUT performs SAR. The Lower Tester uses "TSPX_iut_SDU_size_in_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.

- The Lower Tester has configured a TxWindow size of 1.

- Test Procedure

Figure 4.169 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 327] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use ERTM.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 01) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 1, P = 0, F = 0)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 11) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 2, P = 0, F = 0)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 10) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 3, P = 0, F = 0)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 4, P = 0, F = 0)<br>I-Frame<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 5, P = 0, F = 0)<br>I-Frame<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10) Retransmission<br>S-Frame Timer<br>(RR, N(R) = 6, P = 0, F = 0)<br>**----- End of picture text -----**<br>

_Figure 4.169: L2CAP/ECF/BV-08-C [Transmit I-Frames using Extended Control Field and SAR] MSC_

- Expected Outcome

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT including an Extended Control Field.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **226 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.11.15 Streaming Mode with Extended Control Field (STM)**

Verify the correct implementation of the Extended Control Field with Streaming Mode.

## **L2CAP/STM/BV-11-C [Streaming Mode Source with Extended Control Field]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Extended Control fields (SAR, F-bit, ReqSeq, TxSeq).

- Reference

- [1] 3.3.2, 8.7

- Initial Condition

- The channel is in the OPEN state and configured to use Streaming Mode.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.170 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00)<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) Command the IUT to send data<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00)<br>**----- End of picture text -----**<br>

_Figure 4.170: L2CAP/STM/BV-01-C [Streaming Mode Source with Extended Control Field] MSC_

- Expected Outcome

## Pass verdict

The Lower Tester receives three correctly formatted I-frames from the IUT including Extended Control Fields.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **227 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/STM/BV-12-C [Streaming Mode Sink with Extended Control Field]**

- Test Purpose

Verify that the IUT receives I-frames with Extended Control Field and handles SAR correctly.

- Reference

- [1] 3.3.2, 8.7

- Initial Condition

- The channel is in the OPEN state and configured to use Streaming Mode.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The IUT has configured a MTU and MPS size that is greater or equal to 48 bytes.

- Test Procedure

Figure 4.171 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 222] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode.<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>I-Frame - Payload Length 48 Bytes<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 00) 48 Bytes of data to Upper Tester<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11)<br>I-Frame - Payload Length 16 Bytes<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10) 48 Bytes of data to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.171: L2CAP/STM/BV-02-C [Streaming Mode Sink with Extended Control Field] MSC_

- Expected Outcome

## Pass verdict

The IUT passes the received data correctly to the Upper Tester.

## **L2CAP/STM/BV-13-C [Streaming Mode Source using Extended Control Field and SAR]**

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Extended Control fields (SAR, F-bit, ReqSeq, TxSeq) while performing SAR.

- Reference

[1] 3.3.2, 8.7

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **228 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The channel is in the OPEN state and configured to use Streaming Mode.

- I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- The Lower Tester has configured a value for the MPS that ensures the IUT performs SAR. The Lower Tester uses "TSPX_iut_SDU_size_in_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.

- Test Procedure

Figure 4.172 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

**==> picture [341 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The Channel is in the OPEN state.<br>The Channel is configured to use Streaming Mode.<br>Command the IUT to send data<br>I-Frame<br>(N(S) = 0, N(R) = 0, F = 0, SAR = 01)<br>I-Frame<br>(N(S) = 1, N(R) = 0, F = 0, SAR = 11)<br>I-Frame<br>(N(S) = 2, N(R) = 0, F = 0, SAR = 10) Command the IUT to send data<br>I-Frame<br>(N(S) = 3, N(R) = 0, F = 0, SAR = 01)<br>I-Frame<br>(N(S) = 4, N(R) = 0, F = 0, SAR = 11)<br>I-Frame<br>(N(S) = 5, N(R) = 0, F = 0, SAR = 10)<br>**----- End of picture text -----**<br>

_Figure 4.172: L2CAP/STM/BV-13-C [Streaming Mode Source using Extended Control Field and SAR] MSC_

- Expected Outcome

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT, including Extended Control Fields.

## **4.12 Low Energy System tests**

Verify the correct implementation of the LE features of L2CAP.

## **4.12.1 Connection Parameter Update**

Verify the correct implementation of the LE connection parameter update feature.

**L2CAP/LE/CPU/BV-01-C [Send Connection Parameter Update Request]**

- Test Purpose

Verify that the IUT can send the connection parameter update Request to Lower Tester when acting as a Peripheral device.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **229 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

- [11] Table 2.1, Table 6.1, 4.20

- Initial Condition

- The Lower Tester acts as a connection initiator and the IUT acts as an advertiser.

- The IUT is in CLOSED state for data channel. No ACL link is established.

- The Lower Tester's LL feature mask indicates that it does not support the Connection Parameters Request Procedure.

- The Lower Tester becomes a Central device and the IUT becomes a Peripheral device after the connection is established.

- For the parameters to send and receive, see [5].

- Test Procedure

1. ACL link is established.

2. The IUT sends L2CAP_CONNECTION_PARAMETER_UPDATE_REQ.

**==> picture [340 x 198] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Connect Request<br>ACL Link establishment from the Lower Tester<br>L2CAP_CONNECTION_PARAMETER_<br>(Interval_Min, Interval_Max, Latency, UPDATE_REQ on CID=5<br>Timeout)<br>**----- End of picture text -----**<br>

_Figure 4.173: L2CAP/LE/CPU/BV-01-C [Send Connection Parameter Update Request] MSC_

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP_CONNECTION_PARAMETER_UPDATE_REQ over the LE signaling channel.

## **L2CAP/LE/CPU/BV-02-C [Accept Connection Parameter Update Request]**

- Test Purpose

Verify that the IUT can receive and handle a request for connection parameter update when acting as a Central device.

- Reference

- [11] Table 6.1, 4.20, 4.21

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **230 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The IUT is in CLOSED state. No ACL link exists. The IUT acts as L2CAP initiator.

- Test Procedure

ACL link establishment is part of the test case.

**==> picture [340 x 181] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Connect Request<br>ACL Link establishment from the IUT<br>L2CAP_CONNECTION_PARAMETER_<br>(Interval_Min, Interval_Max, Latency, UPDATE_REQ on CID=5<br>Timeout)<br>RTX_TIMER<br>L2CAP_CONNECTION_PARAMETER_<br>UPDATE_RSP on CID=5<br>(Result=0x0000)<br>**----- End of picture text -----**<br>

_Figure 4.174: L2CAP/LE/CPU/BV-02-C [Accept Connection Parameter Update Request] MSC_

- Test Condition

The IUT’s Bluetooth device address BD_ADDR is defined. For parameter to send and receive, see [5].

The IUT works as connection initiator, therefore, the IUT becomes a Central device and the Lower Tester acts as a Peripheral device after the connection is established.

-

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP_CONNECTION_PARAMETER_UPDATE_RSP over LE signaling channel before RTX timer expires with result code 0x0000.

-

- Notes

The Lower Tester’s RTX timer is set to maximum allowed initial value.

## **L2CAP/LE/CPU/BI-01-C [Reject Connection Parameter Update Parameters]**

- Test Purpose

Verify that the IUT can reject a request for connection parameter update with illegal parameters.

- Reference

- [11] Table 6.1, 4.20, 4.21

- Initial Condition

- The IUT is in CLOSED state. No ACL link exists. The IUT acts as L2CAP initiator.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **231 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

ACL link establishment is part of the test case.

The Lower Tester sends a Latency of larger than 500 in ConnectionParameterUpdateReq.

The IUT returns result of reject in ConnectionParameterUpdateRsp.

**==> picture [378 x 191] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Connect Request<br>ACL Link establishment from the IUT<br>L2CAP_CONNECTION_PARAMETER_<br>(Interval_Min, Interval_Max, Latency=512, UPDATE_REQ on CID=5<br>Timeout)<br>L2CAP_CONNECTION_PARAMETER_<br>UPDATE_RSP on CID=5<br>RTX_TIMER<br>(Result=0001)<br>**----- End of picture text -----**<br>

_Figure 4.175: L2CAP/LE/CPU/BI-01-C [Reject Connection Parameter Update Parameters] MSC_

- Test Condition

The IUT’s Bluetooth device address BD_ADDR is defined. For parameter to send and receive, see [5].

The IUT works as connection initiator, therefore the IUT becomes a Central device and the Lower Tester as a Peripheral device after the connection is established.

-

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP_CONNECTION_PARAMETER_UPDATE_RSP with result code 0x0001 over LE signaling channel before RTX timer expires.

-

- Notes

The Lower Tester’s RTX timer is set to maximum allowed initial value.

## **L2CAP/LE/CPU/BI-02-C [Reject Connection Parameter Update Request]**

- Test Purpose

Verify that the IUT can reject a request for connection parameter update in Peripheral mode.

- Reference

- [11] Table 6.1, 4.20, 4.21

- Initial Condition

- The IUT is in CLOSED state. No ACL link exists. The IUT acts as L2CAP acceptor.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **232 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

ACL link establishment is part of the test case.

The Lower Tester sends ConnectionParameterUpdateReq over the LE signaling channel.

**==> picture [343 x 177] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Connect Request<br>ACL Link establishment from the Lower Tester<br>L2CAP_CONNECTION_PARAMETER_<br>UPDATE(Interval_Min, Interval_Max, Latency=512, _REQ on CID=5<br>Timeout)<br>L2CAP_Command_Reject on CID=5<br>RTX_TIMER (command not understood)<br>**----- End of picture text -----**<br>

_Figure 4.176: L2CAP/LE/CPU/BI-02-C [Reject Connection Parameter Update Request] MSC_

- Test Condition

The IUT’s Bluetooth device address BD_ADDR is defined. For parameter to send and receive, see [5].

The Lower Tester acts as connection initiator, therefore the IUT becomes a Peripheral device and the Lower Tester acts as a Central device after the connection is established.

- Expected Outcome

## Pass verdict

The IUT sends L2CAP Command_Reject with reason “Command not understood” over the LE signaling channel before RTX timer expires.

-

- Notes

The Lower Tester’s RTX timer is set to maximum allowed initial value.

## **4.12.2 Command Reject**

Verify the correct implementation of the command reject.

## **4.12.2.1 Reject Unknown Command**

- Test Purpose

Verify that the IUT can reject reserved and unknown commands.

- Reference

- [11] 4.10

- [12] 4, Table 4.2

- Initial Condition

- The appropriate signaling channel for the transport is used as specified in Table 4.26.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **233 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test case**|L2CAP/COS/CED/BI-01-C [Reject<br>Unknown Command, BR/EDR]|L2CAP/LE/REJ/BI-02-C [Reject Unknown<br>Command – LE]|
|**Signaling**<br>**Channel**|0x0001|0x0005|
|**RFU Codes**|0x1B to 0xFF|0x1B to 0xFF|
|**Unsupported**<br>**Request and**<br>**Indication**<br>**Codes**|0x12 and 0x14<br>0x06 IF NOT L2CAP 2/45<br>0x08 IF NOT L2CAP 2/4<br>0x0A IF NOT L2CAP 2/6<br>0x0C, 0x0E, and 0x10 IF NOT L2CAP 2/29<br>0x16, 0x17, and 0x19 IF NOT L2CAP<br>2/48a|0x02, 0x04, 0x08, 0x0A, 0x0C, 0x0E, 0x10<br>0x06 IF NOT L2CAP 2/45a<br>0x12 IF NOT L2CAP 2/43<br>0x14 IF NOT L2CAP 2/46<br>0x16 IF NOT (L2CAP 2/46 OR L2CAP 2/48b)<br>0x17 and 0x19 IF NOT L2CAP 2/48b|
|**Unsupported**<br>**Response**<br>**Codes**|0x13 and 0x15<br>0x07 IF NOT L2CAP 2/45<br>0x09 IF NOT L2CAP 2/4<br>0x0B IF NOT L2CAP 2/6<br>0x0D, 0x0F, and 0x11 IF NOT L2CAP 2/29<br>0x18 and 0x1A IF NOT L2CAP 2/48a|0x03, 0x05, 0x09, 0x0B, 0x0D, 0x0F, and 0x11<br>0x07 IF NOT L2CAP 2/45a<br>0x13 IF NOT L2CAP 2/42<br>0x15 IF NOT L2CAP 2/46<br>0x18 and 0x1A IF NOT L2CAP 2/48b|

_Table 4.26: Reject Unknown Command test cases_

- Test Procedure

**==> picture [328 x 188] intentionally omitted <==**

_Figure 4.177: Reject Unknown Command MSC_

Repeat Steps 1 and 2 for every Unsupported Request and Indication Code based on the ICS support of the IUT in Table 4.26, for the first three RFU Codes in Table 4.26, and for three other RFU Codes in Table 4.26 selected at random.

1. The Lower Tester sends an L2CAP command with the Code defined in Table 4.26.

2. The IUT responds with an L2CAP_COMMAND_REJECT_RSP.

Repeat Steps 3 and 4 for every Unsupported Response Code based on the ICS support of the IUT in Table 4.26.

3. The Lower Tester sends an L2CAP command with the Response Code.

4. The IUT either responds with an L2CAP_COMMAND_REJECT_RSP or does not respond.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **234 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

In Step 2, and in Step 4 if the IUT responds, the IUT sends a correct

L2CAP_COMMAND_REJECT_RSP packet with reason “Command not understood” and no Reason Data field over the transport and signaling channel as specified in Table 4.26.

## **4.13 Connectionless Basic L2CAP Mode**

Verify the correct implementation of the connectionless services of the L2CAP layer.

## **4.13.1 Connectionless Reception Channel CLR**

Verify the procedures for data exchange over the connectionless channel with the subgroups send data, receive data, disable and enable connectionless traffic.

## **L2CAP/CLS/CLR/BV-01-C [Data Over Connectionless Channel]**

- Test Purpose

Verify that the IUT can send data over the connectionless channel.

- Reference

- [12] 3.2

- Initial Condition

- The Lower Tester utilizes version L2CAP Basic Mode.

- The IUT works as Central, a group has been created, and the Lower Tester has been added as member in the group.

- Test Procedure

**==> picture [340 x 120] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL link establishment from the IUT. IUT works as Central. IUT has added the tester as member in a group.<br>G-frame<br>(Length, CID=0x0002, data)<br>**----- End of picture text -----**<br>

_Figure 4.178: L2CAP/CLS/CLR/BV-01-C [Data Over Connectionless Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT sends connectionless G-frame to the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **235 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/CLS/UCD/BV-01-C [Data Reception over Unicast Connectionless Channel]**

- Test Purpose

Verify that the IUT has the UCD bit set in the L2CAP Extended Features Mask to indicate support for reception of unicast connectionless data. Also verify that the IUT can receive data over the connectionless channel.

- Reference

- [12] 3.2 and 7.6

- Initial Condition

- An ACL connection exists between the Lower Tester and the IUT.

- Test Procedure

The Lower Tester requests Extended Features Mask using L2CAP Information Request. The Lower Tester then transmits a G-frame over the air to the IUT.

**==> picture [341 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL link establishment between IUT and lower tester.<br>L2CAP_InfoReq<br>(InfoType = Extended Features)<br>L2CAP_InfoRes<br>(InfoType = Extended Features<br>Extended Features Mask UCD bit = 1)<br>G-frame<br>Length, CID=0x0002, data<br>G-frame<br>Length, CID=0x0002, data<br>**----- End of picture text -----**<br>

_Figure 4.179: L2CAP/CLS/UCD/BV-01-C [Data Reception over Unicast Connectionless Channel] MSC_

- Expected Outcome

Pass verdict

The following conditions are met:

- The L2CAP Extended Features Mask is successfully retrieved.

- The Unicast Connectionless Data Reception bit in the L2CAP Extended Features Mask is set.

- The IUT sends a connectionless G-frame to the Upper Tester.

**L2CAP/CLS/UCD/BV-02-C [Unencrypted data transmission over unicast connectionless channel]**

- Test Purpose

Verify that the IUT can send unencrypted data over the connectionless channel.

Verify that the IUT can correctly send unencrypted G-frames to the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **236 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

- [12] 7.6

- Initial Condition

- An ACL connection exists between the Lower Tester and the IUT.

- Test Procedure

**==> picture [342 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL link establishment from the IUT. IUT works as Central.<br>**----- End of picture text -----**<br>

_Figure 4.180: L2CAP/CLS/UCD/BV-02-C [Unencrypted data transmission over unicast connectionless channel] MSC_

- Expected Outcome

Pass verdict

The IUT sends an unencrypted connectionless G-frame to the Lower Tester.

**L2CAP/CLS/UCD/BV-03-C [Encrypted Data Transmission over Unicast Connectionless Channel]**

- Test Purpose

Verify that the IUT can send data over the connectionless channel.

- Reference

- [12] 7.6

- Initial Condition

- An unencrypted ACL connection exists between the Lower Tester and the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **237 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [340 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>ACL link establishment from the IUT. IUT works as Central.<br>IUT initiates authentication of Lower Tester.<br>Encryption enabled.<br>**----- End of picture text -----**<br>

_Figure 4.181: L2CAP/CLS/UCD/BV-03-C [Encrypted Data Transmission over Unicast Connectionless Channel] MSC_

- Expected Outcome

## Pass verdict

The IUT performs the following in the specified order:

1. Authenticates the link.

2. Enables encryption.

3. Sends an encrypted connectionless G-frame to the Lower Tester.

## **4.14 Channel Identifiers (CID)**

Tests that L2CAP in the IUT handles CIDs correctly on the connections to the same remote device.

## **L2CAP/LE/CID/BV-01-C [Receiving DCID over BR/EDR and LE]**

- Test Purpose

Test that the L2CAP entity can receive the same DCID in L2CAP connect responses on both the BR/EDR and LE links.

- Reference

- [12] 2.1

-

- Initial Condition

- An ACL-U logical link exists between the IUT and Lower Tester.

- An LE–U logical link exists between the IUT and Lower Tester.

- The IUT has determined from TSPX_psm or TSPX_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the Lower Tester.

- The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **238 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

1. The Upper Tester commands the IUT to create an L2CAP connection on the ACL-U logical link to the Lower Tester.

2. The IUT issues an L2CAP Connection Request over the ACL-U logical link to a known PSM on the Lower Tester, using any allowable dynamically allocated CID in the range 0x0040–0xFFFF for the SCID.

3. The Lower Tester sends an L2CAP Connection Response and assigns any allowable dynamically allocated CID in the range 0x0040–0xFFFF for the DCID to complete the L2CAP connection.

4. The Upper Tester commands the IUT to create an L2CAP connection on the LE-U logical link to the Lower Tester.

5. The IUT issues an L2CAP LE Credit Based Connection Request over the LE-U logical link to a known SPSM on the Lower Tester, using any allowable dynamically allocated CID in the range 0x0040–0x007F for the SCID.

6. The Lower Tester sends an LE Credit Based Connection Response and assigns the same CID used in Step 3 for the DCID to complete the LE L2CAP connection.

7. The Upper Tester commands the IUT to transfer data, of different content, over both L2CAP connections.

8. The Lower Tester displays received data along with the identification of which L2CAP channel it was transferred over.

9. The Lower Tester issues an L2CAP Disconnection Request over the ACL-U logical link.

10. The Lower Tester issues an L2CAP Disconnection Request over the LE-U logical link.

- Expected Outcome

## Pass verdict

Both L2CAP connections complete successfully.

Correct data for each channel is transferred successfully over both connections.

Both L2CAP connections disconnect successfully.

## **L2CAP/LE/CID/BV-02-C [Receiving SCID over BR/EDR and LE]**

- Test Purpose

Test that the L2CAP entity can receive the same SCID in L2CAP connect requests on both the BR/EDR and LE links.

- Reference

- [12] 2.1

-

- Initial Condition

- An ACL-U logical link exists between the IUT and Lower Tester.

- An LE–U logical link exists between the IUT and Lower Tester.

- The IUT has made known to the Lower Tester via TSPX_psm or TSPX_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the IUT.

- The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **239 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

1. The Upper Tester commands the IUT to accept L2CAP connections on both BR/EDR and LE transports

2. The Lower Tester issues an L2CAP Connection Request, using any allowable dynamically allocated CID in the range 0x0040–0x007F for the SCID, over the ACL-U logical link, to a known PSM on the IUT.

3. The IUT sends an L2CAP Connection Response, accepting the SCID proposed by the Lower Tester and using any allowable dynamically allocated CID in the range 0x0040–0x007F for the DCID, to complete the L2CAP connection.

4. The Lower Tester issues an L2CAP LE Credit Based Connection Request over the LE-U logical link to a known SPSM on the IUT, using the same CID used in Step 2 for the SCID.

5. The IUT sends an LE Credit Based Connection Response, accepting the SCID proposed by the Lower Tester and using any allowable dynamically allocated CID in the range 0x0040–0x007F for the DCID, to complete the L2CAP connection.

6. The Upper Tester commands the IUT to transfer data, of different content, over both L2CAP connections.

7. The Lower Tester issues an L2CAP Disconnection Request over the ACL-U logical link.

8. The Lower Tester issues an L2CAP Disconnection Request over the LE-U logical link.

- Expected Outcome

## Pass verdict

Both L2CAP connections complete successfully.

Correct data for each channel is transferred successfully over both connections.

Both L2CAP connections disconnect successfully.

## **L2CAP/LE/CID/BV-03-C [Receiving same DCID over BR/EDR and LE]**

- Test Purpose

Test that the L2CAP entity can receive the same DCID in L2CAP connect responses on both the BR/EDR and LE links, when operating in Enhanced Credit Based Flow Control Mode.

- Reference

- [13] 2.1

- Initial Condition

- An ACL-U logical link exists between the IUT and the Lower Tester.

- An LE-U logical link exists between the IUT and the Lower Tester.

- The IUT has determined from the TSPX_psm or TSPX_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the Lower Tester.

- The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.

- Test Procedure

Same as for L2CAP/LE/CID/BV-01-C [Receiving DCID over BR/EDR and LE], with the remark that the IUT and the Lower Tester uses an Enhanced Credit Based Flow Control channel SPSM as declared via IXIT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **240 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

Both L2CAP connections complete successfully.

Correct data for each channel is transferred successfully over both connections.

Both L2CAP connections disconnect successfully.

## **L2CAP/LE/CID/BV-04-C [Receiving same SCID over BR/EDR and LE]**

- Test Purpose

Test that the L2CAP entity can receive the same SCID in L2CAP connect responses on both the BR/EDR and LE links, when operating in Enhanced Credit Based Flow Control Mode.

- Reference

- [13] 2.1

- Initial Condition

- An ACL-U logical link exists between the IUT and the Lower Tester.

- An LE-U logical link exists between the IUT and the Lower Tester.

- The IUT has determined from the TSPX_psm or TSPX_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the Lower Tester.

- The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.

- Test Procedure

Same as for L2CAP/LE/CID/BV-02-C [Receiving SCID over BR/EDR and LE], with the remark that the IUT and the Lower Tester uses an Enhanced Credit Based Flow Control channel SPSM as declared via the TSPX_spsm IXIT value.

- Expected Outcome

## Pass verdict

Both L2CAP connections complete successfully.

Correct data for each channel is transferred successfully over both connections.

Both L2CAP connections disconnect successfully.

## **4.14.1 Ignore Unsupported CIDs**

- Test Purpose

Test that the L2CAP entity ignores unsupported CIDs in a logical link.

- Reference

- [13] 2.1

- Initial Condition

- A logical link as specified in Table 4.27 exists between the IUT and the Lower Tester.

- The Upper Tester can command the IUT to send data.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **241 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Logical Link**|**PDU CIDs**|
|L2CAP/COS/CID/BI-01-C [Ignore Unsupported<br>CIDs, ACL]|ACL|0x0004, 0x0005, 0x0006,<br>0x0008, 0x003E|
|L2CAP/LE/CID/BI-01-C [Ignore Unsupported<br>CIDs, LE]|LE-U|0x0001, 0x0002, 0x0003,<br>0x0007, 0x0019, 0x003F,<br>0x0100, 0xFFFF|

_Table 4.27: Ignore Unsupported CIDs test cases_

- Test Procedure

**==> picture [341 x 165] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>Logical Link is established<br>REPEAT L2CAP Data (B-frame)<br>(Length, CID, SDU Length, data)<br>IUT ignores L2CAP<br>PDU and does not<br>send PDU to the<br>Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.182: Ignore Unsupported CIDs MSC_

Repeat Steps 1 and 2 for each PDU CID in Table 4.27.

1. The Lower Tester sends an L2CAP Data (B-frame) PDU on the established logical link with the Channel ID of the PDU as specified in Table 4.27.

2. The IUT does not send the L2CAP data to the Upper Tester.

-

- Expected Outcome

Pass verdict

In Step 2, the IUT ignores the L2CAP Data (B-frame) PDU from Step 1 and does not send the data to the Upper Tester.

## **L2CAP/CLS/CID/BV-01-C [Ignore Unsupported CIDs, APB]**

- Test Purpose

Test that the L2CAP entity ignores unsupported CIDs in a BR/EDR APB logical link.

- Reference

- [13] 2.1

- Initial Condition

- An ACL connection exists between the Lower Tester and the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **242 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

The Lower Tester requests Extended Features Mask using an L2CAP Information Request. The Lower Tester then transmits a G-frame over the air to the IUT.

**==> picture [342 x 474] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>Logical Link is established<br>L2CAP_INFORMATION_REQ<br>(InfoType = Extended Features)<br>L2CAP_INFORMATION_RSP<br>(InfoType = Extended Features<br>Extended Features Mask UCD bit = 1)<br>L2CAP_ECHO_REQ<br>The IUT does not send an<br>L2CAP_ECHO_RSP to the Lower<br>Tester<br>Create Connection<br>L2CAP_CONNECTION_REQ<br>(Source CID)<br>L2CAP_CONNECTION_RSP<br>(Source CID, Destination CID)<br>Connection Complete Event<br>Connectionless Data<br>(Source CID, ACL)<br>Data Packet<br>(Length, CID, data)<br>Connectionless Data<br>(Source CID, Broadcast)<br>The IUT does not send data to the<br>Upper Tester<br>Disconnect Connection<br>L2CAP_DISCONNECT_REQ<br>(Source CID, Destination CID)<br>L2CAP_DISCONNECT_RSP<br>(Source CID, Destination CID)<br>Disconnection Complete Event<br>REPEAT<br>G-frame<br>(Length, CID, data)<br>The IUT does not send data to the<br>Upper Tester<br>G-frame<br>(Length, CID=0x0002, data)<br>Data Packet<br>(Length, CID=0x0002, data)<br>**----- End of picture text -----**<br>

_Figure 4.183: L2CAP/CLS/CID/BV-01-C [Ignore Unsupported CIDs, APB] MSC_

1. The Lower Tester sends an L2CAP Info Request to the IUT with InfoType set to ExtendedFeatures.

2. The IUT sends an L2CAP Info Response to the IUT with InfoType set to ExtendedFeatures and the Extended Features Mask UCD bit set to 1.

3. The Lower Tester sends an L2CAP_ECHO_REQ to the IUT on CID 0x0001 via Active Broadcast.

4. The IUT does not send an L2CAP_ECHO_RSP to the Lower Tester.

5. The Upper Tester commands the IUT to create a dynamic L2CAP channel.

6. The IUT sends an L2CAP_CONNECTION_REQ to the Lower Tester with Source CID set to a dynamic CID.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **243 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

7. The Lower Tester sends a successful L2CAP_CONNECTION_RSP with Source CID Set to the CID received in Step 6 and a Destination CID.

8. The IUT sends a successful Connection_Complete event to the Upper Tester.

9. The Lower Tester sends a data packet to the IUT on the Source CID from Step 6 over the ACL connection.

10. The IUT sends the data received in Step 9 to the Upper Tester.

11. The Lower Tester sends a data packet to the IUT on the Source CID channel received from Step 6 over Active Broadcast.

12. The IUT does not send the packet received in Step 11 to the Upper Tester.

13. The Upper Tester commands the IUT to disconnect the channel created in Step 6.

14. The IUT sends an L2CAP_DISCONNECTION_REQ to the IUT to disconnect the connection created in Step 6.

15. The Lower Tester sends a successful L2CAP_DISCONNECTION_RSP to the IUT with Destination CID and Source CID set to the values received in Step 14.

16. The IUT sends a disconnect event to the Upper Tester.

17. Repeat Steps 18–21 for CID values 0x0001, 0x0003, 0x00FF, 0xFFFF, and 2 random invalid CIDs from 0x0004–0x00FE.

18. The Lower Tester sends a connectionless G-frame via Active Broadcast on the CID from Step 17 to the IUT.

19. The IUT does not send a data packet to the Upper Tester.

20. The Lower Tester sends a connectionless G-frame via Active Broadcast on the CID set to 0x0002 to the IUT.

21. The IUT sends a data packet to the Upper Tester.

- Expected Outcome

## Pass verdict

- In Step 4, the IUT does not send an L2CAP_ECHO_RSP to the Lower Tester.

- In Step 10, the IUT sends a data packet to the Upper Tester.

- In Step 12, the IUT does not send a data packet to the Upper Tester.

- In Step 19, the IUT does not send a data packet to the Upper Tester.

- In Step 21, the IUT sends a data packet to the Upper Tester.

## **4.15 Credit Based Flow Control Mode**

## **4.15.1 Enhanced Credit Based Flow Control Mode**

- **4.15.1.1 L2CAP Credit Based Connection Request – Legacy Peer**

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request to a legacy peer and receiving an L2CAP Command Reject does not establish any channel.

- Reference

- [13] 4.25

- Initial Condition

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The signaling channel specified in Table 4.28 is used.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **244 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-01-C [L2CAP Credit Based Connection Request –<br>LegacyPeer, LE]|0x0005|
|L2CAP/ECFC/BV-45-C [L2CAP Credit Based Connection Request –<br>LegacyPeer, BR/EDR]|0x0001|

_Table 4.28: L2CAP Credit Based Connection Request – Legacy Peer test cases_

- Test Procedure

**==> picture [378 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between the IUT and the Lower Tester<br>Create L2CAP Credit Based Channel<br>L2CAP_Credit_Based_Connection_Req (SPSM)<br>(Code = 0x17)<br>L2CAP_Command_Rej<br>(Code = 0x01, Reason = 0)<br>L2CAP Connection Rejected<br>Passed to the Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.184: L2CAP Credit Based Connection Request – Legacy Peer MSC_

1. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) on the SPSM declared via IXIT.

2. The Lower Tester responds with an L2CAP Command Reject (Code = 0x01).

-

- Expected Outcome

## Pass verdict

After receiving the Command Reject from the Lower Tester, the IUT informs the Upper Tester.

## **4.15.1.2 L2CAP Credit Based Connection Request on Supported PSM**

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request to a peer establishes all the channels upon receiving the L2CAP Credit Based Connection Response.

- Reference

## 13 4.25

- Initial Condition

- The signaling channel specified in Table 4.29 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value and send credits.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **245 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-02-C [L2CAP Credit Based Connection Request on<br>Supported PSM, LE]|0x0005|
|L2CAP/ECFC/BV-46-C [L2CAP Credit Based Connection Request on<br>Supported PSM, BR/EDR]|0x0001|

_Table 4.29: L2CAP Credit Based Connection Request on Supported PSM test cases_

- Test Procedure

**==> picture [379 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, Result = 0)<br>An L2CAP channel on relevant SPSM is established between IUT and Lower Tester<br>Data (K Frames)<br>Data<br>**----- End of picture text -----**<br>

_Figure 4.185: L2CAP Credit Based Connection Request on Supported PSM MSC_

1. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) on the SPSM declared via IXIT.

2. The Lower Tester responds with an L2CAP Credit Based Connection Response (Code = 0x18) packet.

3. The Lower Tester sends data on the established channel.

- Expected Outcome

## Pass verdict

The IUT receives the data sent by the Lower Tester on the correct channel. The data is passed to the Upper Tester.

## **4.15.1.3 L2CAP Credit Based Connection Response on Supported PSM**

- Test Purpose

Verify that an IUT receiving a valid L2CAP Credit Based Connection Request from a peer sends an L2CAP Credit Based Connection Response and establishes the channels.

- Reference

- [13] 4.26

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **246 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The signaling channel specified in Table 4.30 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to send data and credits.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-03-C [L2CAP Credit Based Connection Response on<br>Supported PSM, LE]|0x0005|
|L2CAP/ECFC/BV-47-C [L2CAP Credit Based Connection Response on<br>Supported PSM, BR/EDR]|0x0001|

_Table 4.30: L2CAP Credit Based Connection Response on Supported PSM test cases_

## • Test Procedure

**==> picture [379 x 239] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, Result = 0)<br>An L2CAP channel on relevant SPSM is established between IUT and Lower Tester<br>Data<br>Data (K-frame(s))<br>**----- End of picture text -----**<br>

_Figure 4.186: L2CAP Credit Based Connection Response on Supported PSM MSC_

1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) to the IUT on the SPSM specified in the initial conditions.

2. The IUT responds with an L2CAP Credit Based Connection Response (Code = 0x18).

3. The Upper Tester commands the IUT to send data on the data channel.

-

- Expected Outcome

## Pass verdict

The IUT sends one or more correctly formatted K-frames on the correct channel to the Lower Tester. The data sent by the IUT to the Lower Tester matches the data sent by the Upper Tester to the IUT.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **247 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.15.1.4 L2CAP Credit Based Connection Request on an Unsupported PSM**

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request on an unsupported PSM does not establish any channel upon receiving an L2CAP Credit Based Connection Response refusing the connection.

- Reference

- [13] 4.25

- Initial Condition

- The signaling channel specified in Table 4.31 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-04-C [L2CAP Credit Based Connection Request on an<br>Unsupported PSM, LE]|0x0005|
|L2CAP/ECFC/BV-48-C [L2CAP Credit Based Connection Request on an<br>Unsupported PSM, BR/EDR]|0x0001|

_Table 4.31: L2CAP Credit Based Connection Request on an Unsupported PSM test cases_

- Test Procedure

**==> picture [379 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, All connections refused - LE PSM not<br>supported) Create L2CAP Credit Based Channel Response<br>(result)<br>**----- End of picture text -----**<br>

_Figure 4.187: L2CAP Credit Based Connection Request on an Unsupported PSM MSC_

1. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) packet on the SPSM specified in the initial conditions which is not supported by the Lower Tester.

2. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result "0x0002 – All connections refused - LE PSM not supported".

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **248 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT receives an L2CAP Credit Based Connection Response packet with result “0x0002 – All connections refused – LE PSM not supported” from the Lower Tester. This is indicated to the Upper Tester.

- **4.15.1.5 Credit Exchange – Receiving Incremental Credits**

- Test Purpose

Verify that the IUT handles flow control correctly, by handling the L2CAP Flow Control Credit Indication sent by the peer.

- Reference

[13] 4.24

- Initial Condition

- The signaling channel specified in Table 4.32 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- An LE or BR/EDR Data Channel is established on the SPSM.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The Upper Tester can command the IUT to send data.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-06-C [Credit Exchange – Receiving Incremental Credits,<br>LE]|0x0005|
|L2CAP/ECFC/BV-49-C [Credit Exchange – Receiving Incremental Credits,<br>BR/EDR]|0x0001|

_Table 4.32: Credit Exchange – Receiving Incremental Credits test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **249 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [378 x 225] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP channel over the relevant SPSM has been established between the IUT and the Lower Tester<br>Send data<br>Data (K-frame)<br>...<br>Data (K-frame)<br>Repeat for<br>L2CAP_Flow_Control_Credit_Ind N = { 1,>1}<br>(Code = 0x16, Credits = N)<br>Data (K-frame)<br>...<br>Data (K-frame)<br>**----- End of picture text -----**<br>

_Figure 4.188: Credit Exchange – Receiving Incremental Credits MSC_

1. The Upper Tester requests the IUT to send data packets to the Lower Tester.

2. The IUT sends K-frames containing data to the Lower Tester, as many as the initial credit count.

3. The Lower Tester sends an L2CAP Flow Control Credit Indication (Code = 0x16) packet with Credit Value N to the IUT on the CID.

4. The IUT sends K-frames containing data to the Lower Tester.

5. After receiving N K-frames from the IUT and ensuring that no more K-frames are received, the Lower Tester sends a new L2CAP Flow Control Credit Indication packet with a Credits Value of N on the CID. The IUT sends N K-frames containing data to the Lower Tester.

6. The Test Procedure Steps 3–5 are repeated with credit increment N = {1,>1} without disconnecting the channel.

-

- Expected Outcome

## Pass verdict

After receiving N credits, the IUT sends N correctly formatted K-frames containing data to the Lower Tester.

The IUT stops sending K-frames to the Lower Tester when the credit count reaches zero.

- **4.15.1.6 Credit Exchange – Sending Credits**

- Test Purpose

Verify that the IUT sends Flow Control Credit Indication to the peer.

- Reference

[13] 4.24

- Initial Condition

- The signaling channel specified in Table 4.33 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **250 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The Upper Tester can command the IUT to send credits.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-07-C[Credit Exchange – SendingCredits, LE]|0x0005|
|L2CAP/ECFC/BV-50-C[Credit Exchange – SendingCredits, BR/EDR]|0x0001|

_Table 4.33: Credit Exchange – Sending Credits test cases_

- Test Procedure

**==> picture [379 x 211] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP channel over the relevant SPSM has been established between the IUT and the Lower Tester<br>Data (K-frame)<br>Data (K-frame) ...<br>Send credits<br>L2CAP_Flow(Code = 0x16, Credits = N)_Control_Credit_Ind<br>Send N<br>Data (K-frame) data packets<br>**----- End of picture text -----**<br>

_Figure 4.189: Credit Exchange – Sending Credits MSC_

1. The Lower Tester sends data packets to the IUT until it gets credits returned, i.e., the data to send could consume more than the current credits available on the channel.

2. When the Lower Tester remains without credits, the Upper Tester commands the IUT to send N credits to the Lower Tester.

3. The IUT sends an L2CAP Flow Control Credit Indication (Code = 0x16) packet containing Credits = N to the Lower Tester.

4. The Lower Tester starts sending data packets to the IUT and sends N packets.

-

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP Flow Control Credit Indication (Code = 0x16) packet to the Lower Tester at least once doing the data transfer.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **251 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- **4.15.1.7 Credit Exchange – Zero Credits and Exceed Maximum Credits**

- Test Purpose

Verify that the IUT ignores an L2CAP Flow Control Credit Indication packet with credit value set to zero and disconnects the Data Channel created through Enhanced Credit Based Flow Control Mode when the credit count exceeds 65535.

- Reference

- [13] 4.24

- Initial Condition

- The signaling channel specified in Table 4.34 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- An LE or BR/EDR Data Channel is established on the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The initial credit on the LE or BR/EDR Data Channel set by the Lower Tester is more than 1.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BI-01-C [Credit Exchange – Zero Credits and Exceed<br>Maximum Credits, LE]|0x0005|
|L2CAP/ECFC/BI-10-C [Credit Exchange – Zero Credits and Exceed<br>Maximum Credits, BR/EDR]|0x0001|

_Table 4.34: Credit Exchange – Zero Credits and Exceed Maximum Credits test cases_

- Test Procedure

**==> picture [379 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP channel on relevant SPSM has been established between the IUT and the Lower Tester<br>Initial Credits = N<br>L2CAP_Flow_Control_Credit_Ind<br>(Code = 0x16, Credits = 0)<br>L2CAP_Flow_Control_Credit_Ind<br>(Code = 0x16, Credits > (65535 – (N - Packets Sent)))<br>L2CAP_Disconnection_Req<br>(Code = 0x06)<br>L2CAP_Disconnection_Rsp<br>(Code = 0x07)<br>**----- End of picture text -----**<br>

_Figure 4.190: Credit Exchange – Zero Credits and Exceed Maximum Credits MSC_

1. The Lower Tester sends an L2CAP Flow Control Credit Indication (Code = 0x16) packet to the IUT, with Credits = 0.

2. The IUT silently discards the packet and does not modify its credit count.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **252 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

3. The Lower Tester sends an L2CAP Flow Control Credit Indication packet containing a credit so large that it together with the remaining credits on the IUT exceeds 65535.

4. The IUT sends an L2CAP Disconnection Request (Code = 0x06) packet to the Lower Tester, for the CID with exceeding credits.

5. The Lower Tester sends an L2CAP Disconnection Response (Code = 0x07) to the IUT.

- Expected Outcome

## Pass verdict

The IUT ignores the L2CAP Flow Control Credit Indication packet with credit value set to zero, in Step 1.

Upon receiving a credit overflow, the IUT disconnects the Data Channel.

- **4.15.1.8 Credit Exchange – No Credits**

- Test Purpose

Verify that the IUT either returns credits or disconnects the Data Channel created through Enhanced Credit Based Flow Control Mode when receiving a K-frame from the peer device that has the credit count of 0 (zero).

- Reference

- [13] 4.24

- Initial Condition

- The signaling channel specified in Table 4.35 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The initial credit on the LE Data Channel sent to the Lower Tester in a signaling packet is N. If the IUT allows the number of credits to be chosen, then N should be the smallest supported number greater than 1.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BI-02-C[Credit Exchange – No Credits, LE]|0x0005|
|L2CAP/ECFC/BI-11-C[Credit Exchange – No Credits, BR/EDR]|0x0001|

_Table 4.35: Credit Exchange – No Credits test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **253 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [327 x 268] intentionally omitted <==**

_Figure 4.191: Credit Exchange – No Credits MSC_

1. The Lower Tester starts sending data packets to the IUT and sends N+1 packets.

2. After the IUT receives the N[th] packet, execute either alternative 2A or 2B. Alternative 2A (The IUT does not return credits to the Lower Tester):

- 2A.1 The IUT receives the N+1[st] packet, discards the packet, and sends an

- L2CAP_DISCONNECTION_REQ packet (Code = 0x06) to the Lower Tester.

- 2A.2 The Lower Tester sends an L2CAP_DISCONNECTION_RSP packet (Code = 0x07) to the IUT.

- Alternative 2B (The IUT returns credits to the Lower Tester):

- 2B.1 The IUT sends an L2CAP_FLOW_CONTROL_CREDIT_IND to the Lower Tester with Credits > 0.

- 2B.2 The IUT receives the N+1[st] packet.

- Expected Outcome

## Pass verdict

Upon receiving the N+1[st] packet in Step 2A.1, the IUT disconnects the Data Channel, sending an L2CAP_DISCONNECTION_REQ packet to the Lower Tester.

In Step 2B.1, the IUT returns credits to the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **254 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/ECFC/BV-11-C [Security – Insufficient Authentication – Responder, LE]**

- Test Purpose

Verify that an IUT refuses to create any connection upon reception of an L2CAP Credit Based Connection Request which fails to satisfy authentication requirements.

- Reference

- [13] 4.25

- Initial Condition

- An LE ACL connection is established between the IUT and the Lower Tester.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- An authentication requirement exists for the SPSM channel declared via the TSPX_spsm IXIT value.

- Either no LTK exists or an Unauthenticated LTK exists between the IUT and the Lower Tester.

- Test Procedure

**==> picture [398 x 97] intentionally omitted <==**

_Figure 4.192: Security – Insufficient Authentication – Responder, LE MSC_

1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) on the SPSM specified in the initial conditions which requires authentication.

2. The IUT detects either there was no LTK or LTK with insufficient security level and sends an L2CAP Credit Based Connection Response (Code = 0x18), rejecting the connection request with error code “All connections refused – insufficient authentication”.

- Expected Outcome

## Pass verdict

Upon reception of an L2CAP Credit Based Connection Request from the Lower Tester which fails to satisfy the authentication requirements, the IUT sends a correctly formatted L2CAP Credit Based Connection Response with Result 0x0005 (“All connections refused – insufficient authentication”) to the Lower Tester.

- **4.15.1.9 Security – Insufficient Encryption Key Size – Initiator**

- Test Purpose

Verify that the IUT does not establish any channel upon receipt of an L2CAP Credit Based Connection Response indicating the connections were refused with Result 0x0007 (“All connections refused – insufficient encryption key size”).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **255 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

[13] 4.25

- Initial Condition

- The signaling channel specified in Table 4.36 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value.

- Either an Unauthenticated or Authenticated LTK exists between the IUT and the Lower Tester.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-14-C [Security – Insufficient Encryption Key Size –<br>Initiator, LE]|0x0005|
|L2CAP/ECFC/BV-52-C [Security – Insufficient Encryption Key Size –<br>Initiator, BR/EDR]|0x0001|

_Table 4.36: Security – Insufficient Encryption Key Size – Initiator test cases_

- Test Procedure

**==> picture [379 x 196] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, All connections refused -<br>insufficient encryption key size) Create L2CAP Credit Based Channel Response<br>(result)<br>**----- End of picture text -----**<br>

_Figure 4.193: Security – Insufficient Encryption Key Size – Initiator MSC_

1. The Upper Tester commands the IUT to send a connection request.

2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).

3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0007 (“All connections refused - insufficient encryption key size"), refusing the connection request.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **256 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.15.1.10 L2CAP Credit Based Connection Response – refused due to insufficient resources**

- Test Purpose

Verify that an IUT receiving an L2CAP Credit Based Connection Request for several channels refuses the connections for which it doesn’t have sufficient resources with result 0x0004 (“Some connections refused – insufficient resources available").

- Reference

[13] 4.25

- Initial Condition

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The maximum number of L2CAP channels for the SPSM is declared via the TSPX_iut_supported_max_channels IXIT value that the IUT supports.

- The signaling channel specified in Table 4.37 is used.

- A number of LE or BR/EDR Data Channels are established on the SPSM declared via IXIT, such that this number is less than the maximum number previously stated in the TSPX_spsm IXIT value, with at most 4.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-17-C [L2CAP Credit Based Connection Response –<br>refused due to insufficient resources, LE]|0x0005|
|L2CAP/ECFC/BV-53-C [L2CAP Credit Based Connection Response –<br>refused due to insufficient resources, BR/EDR]|0x0001|

_Table 4.37: L2CAP Credit Based Connection Response – refused due to insufficient resources test cases_

- Test Procedure

**==> picture [379 x 222] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>Multiple L2CAP channels on relevant SPSM have been established between IUT and Lower Tester<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID=[...],<br>MTU, MPS, Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, Some connections refused -<br>insufficient resources available)<br>ALT1<br>An L2CAP channel on the relevant SPSM is established between IUT and Lower Tester<br>Data<br>Data (K Frames)<br>**----- End of picture text -----**<br>

_Figure 4.194: L2CAP Credit Based Connection Response – refused due to insufficient resources MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **257 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

1. The Lower Tester sends an L2CAP Credit Based Connection Request on different CIDs than the existing ones, to reach the maximum number of channels + 1.

2. Either the IUT establishes the new channels, up to the maximum supported, and sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with Result 0x0004 (“Some connections refused – insufficient resources available”) as in ALT 1, or if the IUT can support the maximum number of channels, then according to ALT 2, the new L2CAP channels are established.

3. The IUT sends data on at least one of the newly created channels.

- Expected Outcome

## Pass verdict

In Step 2, the IUT follows either ALT 1 or ALT 2:

ALT 1: The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x0004 (“Some connections refused – insufficient resources available”).

ALT 2: The IUT can establish the maximum number of channels, and the new L2CAP channels are successfully established. The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x0000 (“All connections successful”). The IUT sends at least one data packet on one of the newly created channels.

- **4.15.1.11 L2CAP Credit Based Connection Request – refused due to Invalid Source CID**

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request does not establish some of the requested channels upon receiving an L2CAP Credit Based Connection Response refusing the connections with result 0x0009 (“Some connections refused – Invalid Source CID").

- Reference

[13] 4.25

- Initial Condition

- The signaling channel specified in Table 4.38 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-18-C [L2CAP Credit Based Connection Request –<br>refused due to Invalid Source CID, LE]|0x0005|
|L2CAP/ECFC/BV-54-C [L2CAP Credit Based Connection Request –<br>refused due to Invalid Source CID, BR/EDR]|0x0001|

_Table 4.38: L2CAP Credit Based Connection Request – refused due to Invalid Source CID test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **258 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [377 x 265] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM, one or more channels)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x18, SPSM, SCID=[...],<br>MTU, MPS, Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, Some connections refused -<br>invalid Source CID) Create L2CAP Credit Based Channel Response<br>(result)<br>ALT1<br>An L2CAP channel on the relevant SPSM is established between IUT and Lower Tester<br>Data<br>Data (K Frames)<br>**----- End of picture text -----**<br>

_Figure 4.195: L2CAP Credit Based Connection Request – refused due to Invalid Source CID MSC_

1. The Upper Tester commands the IUT to send a connection request.

2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).

3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0009 (“Some connections refused - invalid Source CID”), refusing the connection request.

4. (ALT1) If the connection request was performed with more than one SCID and some of the channels were created, the Upper Tester commands the IUT to send data on the accepted CIDs.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester that some connections were refused.

(ALT1) The data sent by the IUT in Step 3 must be the same as that received by the Lower Tester.

The IUT does not send any data to the Lower Tester on the refused CID(s).

- **4.15.1.12 L2CAP Credit Based Connection Request – refused due to Source CID already allocated**

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request does not establish some of the requested channels upon receiving an L2CAP Credit Based Connection Response refusing some of the connections with result 0x000A (“Some connections refused – Source CID already allocated").

- Reference

- [13] 4.25

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **259 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Initial Condition

- The signaling channel specified in Table 4.39 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-19-C [L2CAP Credit Based Connection Request –<br>refused due to Source CID alreadyallocated, LE]|0x0005|
|L2CAP/ECFC/BV-55-C [L2CAP Credit Based Connection Request –<br>refused due to Source CID alreadyallocated, BR/EDR]|0x0001|

_Table 4.39: L2CAP Credit Based Connection Request – refused due to Source CID already allocated test cases_

- Test Procedure

**==> picture [378 x 267] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM, one or more channels)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID=[...],<br>MTU, MPS, Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, Some connections refused -<br>Source CID already allocated) Create L2CAP Credit Based Channel Response<br>(result)<br>ALT1<br>An L2CAP channel on the relevant SPSM is established between IUT and Lower Tester<br>Data<br>Data (K Frames)<br>**----- End of picture text -----**<br>

_Figure 4.196: L2CAP Credit Based Connection Request – refused due to Source CID already allocated MSC_

1. The Upper Tester commands the IUT to send a connection request.

2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).

3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x000A (“Some connections refused – Source CID already allocated”), refusing the connection request.

4. (ALT1) If the connection request was performed with more than one SCID and some of the channels were created, the Upper Tester commands the IUT to send data on the accepted CIDs.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **260 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester that the connection was refused.

(ALT1) The data send by the IUT in Step 3 must be the same as that received by the Lower Tester.

The IUT does not send any data to the Lower Tester on the refused CID(s).

- **4.15.1.13 L2CAP Credit Based Connection Response – refused due to Source CID already allocated**

- Test Purpose

Verify that an IUT receiving an L2CAP Credit Based Connection Request for several channels refuses some of the connections with result 0x000A (“Some connections refused – Source CID already allocated”) if it receives a Source CID which is already in use.

- Reference

[13] 4.25

- Initial Condition

- The signaling channel specified in Table 4.40 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- One LE or BR/EDR Data channel is established on the SPSM declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-20-C [L2CAP Credit Based Connection Response –<br>refused due to Source CID alreadyallocated, LE]|0x0005|
|L2CAP/ECFC/BV-56-C [L2CAP Credit Based Connection Response –<br>refused due to Source CID alreadyallocated, BR/EDR]|0x0001|

_Table 4.40: L2CAP Credit Based Connection Response – refused due to Source CID already allocated test cases_

- Test Procedure

**==> picture [378 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>Multiple L2CAP channels on the relevant SPSM have been established between IUT and Lower Tester<br>Credits > 0<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x18, SPSM, SCID=[...],<br>MTU, MPS, Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, Some connections refused -<br>Source CID already allocated)<br>**----- End of picture text -----**<br>

_Figure 4.197: L2CAP Credit Based Connection Response – refused due to Source CID already allocated MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **261 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) using the same CID as the previously established channel.

2. The IUT sends an L2CAP Credit Based Connection Response (Code = 0x18) to the Lower Tester with result 0x000A (“Some connections refused – Source CID already allocated”).

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x000A (“Some connections refused – Source CID already allocated”).

- **4.15.1.14 L2CAP Credit Based Connection Request – refused due to Unacceptable Parameters**

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request does not establish any channel upon receiving an L2CAP Credit Based Connection Response refusing the connections with result 0x000B (“All connections refused – unacceptable parameters”).

- Reference

- [13] 4.25

- Initial Condition

- The signaling channel specified in Table 4.41 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-21-C [L2CAP Credit Based Connection Request –<br>refused due to Unacceptable Parameters, LE]|0x0005|
|L2CAP/ECFC/BV-57-C [L2CAP Credit Based Connection Request –<br>refused due to Unacceptable Parameters, BR/EDR]|0x0001|

_Table 4.41: L2CAP Credit Based Connection Request – refused due to Unacceptable Parameters test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **262 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [379 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>L2CAP Credit Based Connection Request<br>L2CAP_Credit_Based_Connection_Req<br>(SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(All connections refused - unacceptable parameters)<br>L2CAP Credit Based Connection Response<br>(failure)<br>**----- End of picture text -----**<br>

_Figure 4.198: L2CAP Credit Based Connection Request – refused due to Unacceptable Parameters MSC_

1. The Upper Tester commands the IUT to send a connection request.

2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).

3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x000B (“All connections refused – unacceptable parameters”), refusing the connection request.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester that the connection was refused.

- **4.15.1.15 Renegotiate MTU – Initiator**

- Test Purpose

Verify that the IUT sending an L2CAP Credit Based Reconfigure Request can reconfigure the Maximum Transmission Unit (MTU) for the indicated channels, being able to receive larger SDUs.

- Reference

[13] 4.27

- Initial Condition

- The maximum supported MTU size is defined by the TSPX_l2ca_cbmtu_max IXIT entry.

- The minimum supported MTU size is defined by the TSPX_l2ca_cbmtu_min IXIT entry.

- The signaling channel specified in Table 4.42 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **263 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-22-C[Renegotiate MTU – Initiator, LE]|0x0005|
|L2CAP/ECFC/BV-58-C[Renegotiate MTU – Initiator, BR/EDR]|0x0001|

_Table 4.42: Renegotiate MTU – Initiator test cases_

- Test Procedure

**==> picture [415 x 323] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP channel on the relevant SPSM has been established between IUT and Lower Tester<br>Repeat<br>Opt Send credits 2 times<br>L2CAP_FLOW_CONTROL_CREDIT_IND<br>(Code = 0x16, Credits)<br>Data (K Frames)<br>Data<br>Increase MTU<br>L2CAP_CREDIT_BASED_RECONFIGURE_REQ<br>(Code = 0x19, MTU > MTUInitial)<br>L2CAP(Code = 0x1A, Result = 0x0000)_CREDIT_BASED_RECONFIGURE_RSP<br>Repeat<br>Opt Send credits 2 times<br>L2CAP_FLOW_CONTROL_CREDIT_IND<br>(Code = 0x16, Credits)<br>Data (K Frames)<br>Data<br>**----- End of picture text -----**<br>

_Figure 4.199: Renegotiate MTU – Initiator MSC_

1. If the minimum supported MTU size equals the maximum supported MTU size or the current MTU size equals the maximum supported MTU size, the test ends with a Pass verdict.

2. The Lower Tester continuously transmits SDUs of a size that the MTU negotiated at channel initialization, at a minimum rate of two packets per second, over the L2CAP channel. Transmit at least 2 SDUs.

3. The Upper Tester commands the IUT to increase the MTU size for the opened channel.

4. The IUT sends an L2CAP_CREDIT_BASED_RECONFIGURE_REQ (Code = 0x19) packet to the Lower Tester, with the MTU field greater than the one in the initial configuration of the channel.

5. The Lower Tester sends an L2CAP_CREDIT_BASED_RECONFIGURE_RSP (Code = 0x1A) packet to the IUT, with the Result field equal to 0x0000 (Reconfiguration successful).

6. The Lower Tester transmits SDUs of a size equal to the MTU in Step 3 to the IUT. Transmit at least 2 SDUs.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **264 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

Pass verdict

Complete SDUs are sent to the Upper Tester, for Steps 3 and 6.

- **4.15.1.16 Renegotiate MTU – Responder**

- Test Purpose

Verify that the IUT receiving an L2CAP Credit Based Reconfigure Request can reconfigure the Maximum Transmission Unit (MTU) for an indicated channel, being able to send larger SDUs.

- Reference

[13] 4.28

- Initial Condition

- The maximum supported MTU size is defined by the TSPX_l2ca_cbmtu_max IXIT entry.

- The minimum supported MTU size is defined by the TSPX_l2ca_cbmtu_min IXIT entry.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The signaling channel specified in Table 4.43 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Lower Tester’s initial MTU is equal to the IUT’s minimum MTU size from the TSPX_tester_mtu IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-23-C[Renegotiate MTU – Responder, LE]|0x0005|
|L2CAP/ECFC/BV-59-C[Renegotiate MTU – Responder, BR/EDR]|0x0001|

_Table 4.43: Renegotiate MTU – Responder test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **265 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [414 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP channel on the relevant SPSM has been established between IUT and Lower Tester<br>Repeat<br>Opt 2 times<br>L2CAP(Code = 0x16, Credits)_FLOW_CONTROL_CREDIT_IND<br>Send Data<br>Data (K Frames)<br>L2CAP_CREDIT_BASED_RECONFIGURE_REQ<br>(Code = 0x19, MTU = MTUMax)<br>L2CAP_CREDIT_(Code = 0x1A, Result = 0x0000)BASED_RECONFIGURE_RSP<br>Repeat<br>Opt 2 times<br>L2CAP(Code = 0x16, Credits)_FLOW_CONTROL_CREDIT_IND<br>Send Data<br>Data (K Frames)<br>**----- End of picture text -----**<br>

_Figure 4.200: Renegotiate MTU – Responder MSC_

1. If the minimum supported MTU size equals the maximum supported MTU size or the current MTU size equals the maximum supported MTU size, the test ends with a Pass verdict.

2. The Upper Tester commands the IUT to continuously transmit SDUs of a size equal to the MTU negotiated at channel initialization over the L2CAP channel at a minimum rate of two packets per second. Transmit at least 2 SDUs.

3. The Lower Tester sends an L2CAP_CREDIT_BASED_RECONFIGURE_REQ (Code = 0x19) packet to the IUT, with the MTU field set to the IUT’s maximum MTU size from IXIT.

4. The IUT sends an L2CAP_CREDIT_BASED_RECONFIGURE_RSP (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0000 (Reconfiguration successful).

5. The Upper Tester commands the IUT to transmit SDUs of a size equal to the MTU in Step 3 to the Lower Tester. Transmit at least 2 SDUs.

- Expected Outcome

## Pass verdict

Complete SDUs are sent to the Upper Tester, for Steps 2 and 5.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **266 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.15.1.17 Renegotiate MTU – MTU value is decreased**

- Test Purpose

Verify that the IUT refuses the MTU reconfiguration request for a Data Channel created through Enhanced Credit Based Flow Control Mode when receiving an L2CAP Credit Based Reconfigure Request with a lower MTU value than the existing one.

- Reference

- [13] 4.27

- Initial Condition

- The signaling channel specified in Table 4.44 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value, with the MTU on the Lower Tester side of at least 65 octets.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BI-03-C[Renegotiate MTU – MTU value is decreased, LE]|0x0005|
|L2CAP/ECFC/BI-12-C [Renegotiate MTU – MTU value is decreased,<br>BR/EDR]|0x0001|

_Table 4.44: Renegotiate MTU – MTU value is decreased test cases_

- Test Procedure

**==> picture [413 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP channel on the relevant SPSM has been established between IUT and Lower Tester<br>MTUInitial > 64<br>L2CAP_Credit_Based_Reconfigure_Req<br>(Code = 0x19, MTU < MTUInitial)<br>L2CAP_Credit_Based_Reconfigure_Rsp<br>(Code = 0x1A, Result = 0x0001)<br>**----- End of picture text -----**<br>

_Figure 4.201: Renegotiate MTU – MTU value is decreased MSC_

1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request (Code = 0x19) packet to the IUT, with the MTU field lower than the one in the channel initial configuration.

2. The IUT does not disconnect the channel. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0001 (Reconfiguration failed - reduction in size of MTU not allowed).

-

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0001 (Reconfiguration failed - reduction in size of MTU not allowed).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **267 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.15.1.18 Renegotiate MPS – Initiator**

- Test Purpose

Verify that the IUT sending an L2CAP Credit Based Reconfigure Request can receive differently sized L2CAP PDUs on the indicated channels.

- Reference

- [13] 4.27

- Initial Condition

- The signaling channel specified in Table 4.45 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The minimum supported IUT MPS size is defined by the TSPX_l2ca_cbmps_min IXIT entry.

- The maximum supported IUT MPS size is defined by the TSPX_l2ca_cbmps_max IXIT entry.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-24-C[Renegotiate MPS – Initiator, LE]|0x0005|
|L2CAP/ECFC/BV-60-C[Renegotiate MPS – Initiator, BR/EDR]|0x0001|

_Table 4.45: Renegotiate MPS – Initiator test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **268 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [414 x 551] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP channel on the relevant SPSM has been established between IUT and Lower Tester<br>IUT MPS = N<br>Repeat<br>Opt Send credits 5 times<br>L2CAP_FLOW_CONTROL(Code = 0x16, Credits)_CREDIT_IND<br>Data (K Frame)<br>(size = MPS)<br>...<br>Data (K Frame)<br>(size MPS) Received packet<br>Reconfigure MPS ALT A<br>L2CAP_CREDIT_BASED_RECONFIGURE_REQ (MPS = N+1)<br>(Code = 0x19, MPS = N+1)<br>L2CAP_CREDIT_BASED_RECONFIGURE_RSP<br>(Code = 0x1A, Result = 0x0000)<br>Repeat<br>Opt Send credits 5 times<br>L2CAP_FLOW_CONTROL(Code = 0x16, Credits)_CREDIT_IND<br>Data (K Frame)<br>(size = MPS)<br>...<br>Data (K Frame)<br>(size MPS) Received packet<br>Reconfigure MPS ALT A<br>L2CAP_CREDIT_BASED_RECONFIGURE_REQ (MPS = N-1)<br>(Code = 0x19, MPS = N-1)<br>L2CAP_CREDIT_BASED_RECONFIGURE_RSP<br>(Code = 0x1A, Result = 0x0000)<br>Repeat<br>Opt Send credits 5 times<br>L2CAP_FLOW_CONTROL(Code = 0x16, Credits)_CREDIT_IND<br>Data (K Frame)<br>(size = MPS)<br>...<br>Data (K Frame)<br>(size MPS) Received packet<br>**----- End of picture text -----**<br>

_Figure 4.202: Renegotiate MPS – Initiator MSC_

1. If TSPX_l2ca_cbmps_min equals TSPX_l2ca_cbmps_max, the test ends with a Pass verdict.

2. The IUT configures a value N for the MPS. If TSPX_l2ca_cbmps_max equals

- TSPX_l2ca_cbmps_min plus 1, then N equals TSPX_l2ca_cbmps_min. Otherwise, N is greater than TSPX_l2ca_cbmps_min and lower than TSPX_l2ca_cbmps_max. The Lower Tester

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **269 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

chooses, for the remaining steps, an SDU size that ensures that the Lower Tester performs segmentation.

3. The Lower Tester transmits SDUs (SDU size in Step 1) at a minimum rate of two packets per second, segmented into data packets with payload of size N over the L2CAP channel. Transmit at least 5 SDUs.

4. The IUT sends an L2CAP Credit Based Reconfigure Request (Code = 0x19) packet to the Lower Tester, with MPS = N + 1 bytes.

5. The Lower Tester sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the IUT, with the Result field equal to 0x0000 (Reconfiguration successful).

6. The Lower Tester transmits SDUs (SDU size in Step 2), segmented into data packets with payload of size N + 1 to the IUT. Transmit at least 5 SDUs. If N = TSPX_l2ca_cbmps_min, skip to Step 9.

7. The IUT sends an L2CAP_CREDIT_BASED_RECONFIGURE_REQ packet to the Lower Tester, with MPS = N – 1 bytes.

8. The Lower Tester sends an L2CAP_CREDIT_BASED_RECONFIGURE_RSP packet to the IUT, with the Result field equal to 0x0000 (Reconfiguration successful).

9. The Lower Tester transmits SDUs (SDU size in Step 2), segmented into data packets with payload of size N – 1 to the IUT. Transmit at least 5 SDUs.

- Expected Outcome

## Pass verdict

Complete SDUs are sent to the Upper Tester in Steps 3, 6, and 9.

## **4.15.1.19 Renegotiate MPS – Responder**

- Test Purpose

Verify that the IUT receiving an L2CAP Credit Based Reconfigure Request can send differently sized L2CAP PDUs on the indicated channel.

- Reference

- [13] 4.28

- Initial Condition

- The minimum supported IUT MPS size is defined by the TSPX_l2ca_cbmps_min IXIT entry.

- The maximum supported IUT MPS size is defined by the TSPX_l2ca_cbmps_max IXIT entry.

- The signaling channel specified in Table 4.46 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Lower Tester’s initial MTU is equal to the IUT’s maximum MTU size from the TSPX_l2ca_cbmtu_max IXIT value.

- The Lower Tester has configured a value N for the MPS, higher than TSPX_l2ca_cbmps_min and lower than TSPX_l2ca_cbmps_max, and the IUT chooses for transmitting an SDU size that, along with N, ensures that the IUT performs segmentation unless the IUT’s max SDU size is the same as the MPS size.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **270 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-25-C[Renegotiate MPS – Responder, LE]|0x0005|
|L2CAP/ECFC/BV-61-C[Renegotiate MPS – Responder, BR/EDR]|0x0001|

_Table 4.46: Renegotiate MPS – Responder test cases_

## • Test Procedure

**==> picture [405 x 531] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP channel on the relevant SPSM has been established between IUT and Lower Tester<br>Lower Tester MPS = N<br>Send packet Repeat<br>5 times<br>Opt<br>L2CAP(Code = 0x16, Credits)_FLOW_CONTROL_CREDIT_IND<br>Data (K-frame)<br>(size = MPS)<br>...<br>Data (K-frame)<br>(size MPS)<br>L2CAP(Code = 0x19, MPS = N + 1)_CREDIT_BASED_RECONFIGURE_REQ<br>L2CAP_CREDIT_(Code = 0x1A, Result = 0x0000)BASED_RECONFIGURE_RSP<br>Send packet Repeat<br>5 times<br>Opt<br>L2CAP_FLOW_CONTROL_CREDIT_IND<br>(Code = 0x16, Credits)<br>Data (K-frame)<br>(size = Negotiated MPS)<br>...<br>Data (K-frame)<br>(size Negotiated MPS)<br>L2CAP(Code = 0x19, MPS = N - 1)_CREDIT_BASED_RECONFIGURE_REQ<br>L2CAP_CREDIT_(Code = 0x1A, Result = 0x0000)BASED_RECONFIGURE_RSP<br>Send packet Repeat<br>5 times<br>Opt<br>L2CAP(Code = 0x16, Credits)_FLOW_CONTROL_CREDIT_IND<br>Data (K-frame)<br>(size = Negotiated MPS)<br>...<br>Data (K-frame)<br>(size Negotiated MPS)<br>**----- End of picture text -----**<br>

_Figure 4.203: Renegotiate MPS – Responder MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **271 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

1. If the minimum supported MPS size equals TSPX_l2ca_cbmps_max, the test ends with a Pass verdict.

2. If the MTU size equals MPS size, the test ends with a Pass verdict.

3. The Upper Tester commands the IUT to continuously transmits data packets (SDU size in Initial Condition) over the L2CAP channel at a minimum rate of 2 packets per second. Transmit at least 5 SDUs.

4. The IUT performs segmentation and transmit K-frames with payload equal to N (Lower Tester’s MPS).

5. The Lower Tester sends an L2CAP_CREDIT_BASED_RECONFIGURE_REQ (Code = 0x19) packet to the IUT, with MPS = N + 1.

6. The IUT sends an L2CAP_CREDIT_BASED_RECONFIGURE_RSP (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0000 (Reconfiguration successful).

7. The Upper Tester commands the IUT to transmit data packets (SDU size in Initial Condition) to the Lower Tester. Transmit at least 5 SDUs.

8. The IUT performs segmentation and transmit K-frames with payload equal to N+1 unless N+1 exceeds TSPX_l2ca_cbmps_max from IXIT. If N = TSPX_l2ca_cbmps_min, then the test ends with a Pass verdict.

9. The Lower Tester sends an L2CAP_CREDIT_BASED_RECONFIGURE_REQ packet to the IUT, with MPS = N – 1 bytes.

10. The IUT sends an L2CAP_CREDIT_BASED_RECONFIGURE_RSP packet to the Lower Tester, with the Result field equal to 0x0000 (Reconfiguration successful).

11. The Upper Tester commands the IUT to transmit data packets (SDU size in Initial Condition) to the Lower Tester. Transmit at least 5 SDUs.

12. The IUT performs segmentation and transmit K-frames with payload equal to N – 1 unless N – 1 is lower than TSPX_l2ca_cbmps_min.

- Expected Outcome

## Pass verdict

For each of the Steps 3, 8, and 12, the IUT segments the SDUs to a length no greater than the previously negotiated MPS size and send correct frames to the Lower Tester.

- **4.15.1.20 Renegotiate MPS – MPS value is decreased**

- Test Purpose

Verify that the IUT refuses the MPS reconfiguration request for multiple Data Channels created through Enhanced Credit Based Flow Control Mode, when receiving an L2CAP Credit Based Reconfigure Request with lower MPS value than the existing one for multiple channels and when receiving an L2CAP Credit Based Reconfigure Request with an MPS value between other existing MPS values for multiple channels.

- Reference

## 15 4.27

- Initial Condition

- The TSPX_l2ca_cbmps_min and TSPX_l2ca_cbmps_max IXIT values give the minimum and maximum supported IUT MPS size.

- The signaling channel specified in Table 4.47 is used.

- An SPSM for the Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **272 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BI-04-C[Renegotiate MPS – MPS value is decreased, LE]|0x0005|
|L2CAP/ECFC/BI-13-C [Renegotiate MPS – MPS value is decreased,<br>BR/EDR]|0x0001|

_Table 4.47: Renegotiate MPS – MPS value is decreased test cases_

- Test Procedure

**==> picture [379 x 138] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Two L2CAP channels on the relevant SPSM have been established between IUT and Lower Tester<br>Lower Tester SDU size = N, IUT MPS = N/3<br>L2CAP_Credit_Based_Reconfigure_Req<br>(Code = 0x19, DCID = [A, B], MPS = N/4)<br>L2CAP_Credit_Based_Reconfigure_Rsp<br>(Code = 0x1A, Result = 0x0002)<br>**----- End of picture text -----**<br>

_Figure 4.204: Renegotiate MPS – MPS value is decreased MSC_

1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, with Destination CID containing the list of CIDs of the opened channels and with a lower MPS value (in octets) than what was negotiated in the channel’s establishment. The lower MPS value must be at least 1 octet lower than the previous value.

2. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time). The IUT does not disconnect any of the channels requested in Step 1.

3. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, with Destination CID containing the list of CIDs of the opened channels and with an MPS value (in octets) that is between the minimum MPS value of the Destination CIDs and the maximum MPS value of the Destination CIDs that were negotiated for in each of the channels established.

4. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field set to any valid error code. The IUT does not disconnect any of the channels requested in Step 3.

-

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time).

In Step 4, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result set to any valid error code.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **273 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.15.1.21 L2CAP Credit Based Connection Response – refused due to Invalid Parameters**

- Test Purpose

Verify that an IUT does not establish any of the requested channels upon receiving an L2CAP Credit Based Connection Request containing a parameter with a value outside specifications and responds with result 0x000C (“All connections refused – invalid parameters”).

- Reference

[13] 4.26

- Initial Condition

- The signaling channel specified in Table 4.48 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-26-C [L2CAP Credit Based Connection Response –<br>refused due to Invalid Parameters, LE]|0x0005|
|L2CAP/ECFC/BV-62-C [L2CAP Credit Based Connection Response –<br>refused due to Invalid Parameters, BR/EDR]|0x0001|

_Table 4.48: L2CAP Credit Based Connection Response – refused due to Invalid Parameters test cases_

- Test Procedure

**==> picture [379 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID,<br>MTU < 64, MPS, Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, All connections refused -<br>Invalid parameters)<br>**----- End of picture text -----**<br>

_Figure 4.205: L2CAP Credit Based Connection Response – refused due to Invalid Parameters MSC_

1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) with the SPSM declared via IXIT and an MTU value less than 64.

2. The IUT rejects the connection request sending an L2CAP Credit Based Connection Response (Code = 0x18) to the Lower Tester with Result 0x000C (“All connections refused – invalid parameters”).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **274 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x000C (“All connections refused – Invalid parameters”).

- **4.15.1.22 L2CAP Credit Based Connection Response – refused due to Unacceptable Parameters**

- Test Purpose

Verify that an IUT does not establish any of the requested channels upon receiving an L2CAP Credit Based Connection Request containing a parameter with a value unacceptable for the Host and responds with result 0x000B (“All connections refused – unacceptable parameters”).

- Reference

- [13] 4.26

- Initial Condition

- TSPX_l2ca_cbmtu_min in the IXIT statement [3] is used to give the minimum peer MTU size that the IUT can accept on L2CAP Credit Based channels. The IXIT entry TSPX_l2ca_cbmtu_min should not be set to 64 if the IUT can accept peer MTU size larger than 64 octets for Credit Based Connection Requests.

- The signaling channel specified in Table 4.49 is used.

- An SPSM for the Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-27-C [L2CAP Credit Based Connection Response –<br>refused due to Unacceptable Parameters, LE]|0x0005|
|L2CAP/ECFC/BV-63-C [L2CAP Credit Based Connection Response –<br>refused due to Unacceptable Parameters, BR/EDR]|0x0001|

_Table 4.49: L2CAP Credit Based Connection Response – refused due to Unacceptable Parameters test cases_

- Test Procedure

**==> picture [378 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID,<br>MTU > MTUIUT, MPS, Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, All connections refused -<br>unacceptable parameters)<br>**----- End of picture text -----**<br>

_Figure 4.206: L2CAP Credit Based Connection Response – refused due to Unacceptable Parameters MSC_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **275 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

1. Perform alternative 1A or 1B depending on TSPX_l2ca_cbmtu_min. Alternative 1A (TSPX_l2ca_cbmtu_min is greater than 64):

- 1A.1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) with the SPSM declared via IXIT and an MTU value lower than TSPX_l2ca_cbmtu_min.

- 1A.2. The IUT rejects the connection request sending an L2CAP Credit Based Connection Response (Code = 0x18) to the Lower Tester with Result 0x000B (“All connections refused – unacceptable parameters”).

- Alternative 1B (TSPX_l2ca_cbmtu_min is 64):

- 1B.1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) with the SPSM declared via IXIT and an MTU value equal to 64.

- 1B.2. The channel is successfully established.

- Expected Outcome

## Pass verdict

In Step 1A.2, the IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x000B (“All connections refused – unacceptable parameters”).

In Step 1B.2, the channel is successfully established. The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x0000 (“All connections successful”).

## **4.15.1.23 Reconfigure – refused due to invalid Destination CID**

- Test Purpose

Verify that the IUT refuses a reconfiguration request for a Data Channel created through Enhanced Credit Based Flow Control Mode, when receiving an L2CAP Credit Based Reconfigure Request with invalid Destination CID.

- Reference

- [13] 4.27

-

- Initial Condition

- The TSPX_l2ca_cbmps_min and TSPX_l2ca_cbmps_max IXIT values give the minimum and maximum supported IUT MPS size.

- The signaling channel specified in Table 4.50 is used.

- An SPSM for the Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

-

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BI-05-C [Reconfigure – refused due to invalid Destination<br>CID, LE]|0x0005|
|L2CAP/ECFC/BI-14-C [Reconfigure – refused due to invalid Destination<br>CID, BR/EDR]|0x0001|

_Table 4.50: Reconfigure – refused due to invalid Destination CID test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **276 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [379 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Two L2CAP channels on the relevant SPSM have been established between IUT and Lower Tester<br>Lower Tester SDU size = N, IUT MPS = N/3<br>L2CAP_Credit_Based_Reconfigure_Req<br>(Code = 0x19, DCID = [invalid], MPS = N/4)<br>L2CAP_Credit_Based_Reconfigure_Rsp<br>(Code = 0x1A, Result = 0x0003)<br>**----- End of picture text -----**<br>

_Figure 4.207: Reconfigure – refused due to invalid Destination CID MSC_

1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, with Destination CID containing one invalid CID and with valid MPS.

2. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0003 (Reconfiguration failed – one or more Destination CIDs invalid).

-

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0003 (Reconfiguration failed – one or more Destination CIDs invalid).

## **4.15.1.24 Reconfigure – other unacceptable parameters**

- Test Purpose

Verify that the IUT refuses the MPS reconfiguration request for a Data Channel created through Enhanced Credit Based Flow Control Mode, when receiving an L2CAP Credit Based Reconfigure Request with an unacceptable MPS value.

- Reference

- [13] 4.28

- Initial Condition

- The TSPX_l2ca_cbmps_min IXIT value gives the minimum supported IUT MPS size.

- The signaling channel specified in Table 4.51 is used.

- An SPSM for the Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BI-06-C[Reconfigure – other unacceptableparameters, LE]|0x0005|
|L2CAP/ECFC/BI-15-C [Reconfigure – other unacceptable parameters,<br>BR/EDR]|0x0001|

_Table 4.51: Reconfigure – other unacceptable parameters test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **277 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [379 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP channel on the relevant SPSM has been established between IUT and Lower Tester<br>L2CAP_Credit_Based_Reconfigure_Req<br>(Code = 0x19, DCID = [A], MPS < MPSMIN)<br>L2CAP_Credit_Based_Reconfigure_Rsp<br>(Code = 0x1A, Result = 0x0004)<br>**----- End of picture text -----**<br>

_Figure 4.208: Reconfigure – other unacceptable parameters MSC_

1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, for the opened channel, with MPS < MPSMIN (minimum supported IUT MPS, as described in the IXIT).

2. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0004 (“Reconfiguration failed – other unacceptable parameters”).

-

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0004 (Reconfiguration failed – other unacceptable parameters).

- **4.15.1.25 L2CAP Credit Based Connection Response – Duplicate DCID**

- Test Purpose

Verify that an IUT receiving an L2CAP_CREDIT_BASED_CONNECTION_RSP having a duplicate DCID detects the duplicate DCID and does not continue to use either the original channel or the new channel.

- Reference

- [13] 4.26

-

- Initial Condition

- The signaling channel specified in Table 4.52 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value. A Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value.

-

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BV-29-C [L2CAP Credit Based Connection Response –<br>Duplicate DCID, LE]|0x0005|
|L2CAP/ECFC/BV-64-C [L2CAP Credit Based Connection Response –<br>Duplicate DCID, BR/EDR]|0x0001|

_Table 4.52: L2CAP Credit Based Connection Response – Duplicate DCID test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **278 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [379 x 181] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>An L2CAP channel over the relevant SPSM has been established between IUT and Lower Tester.<br>Create L2CAP Credit Based Channel<br>(SPSM)<br>L2CAP_CREDIT_BASED_CONNECTION_REQ<br>(Code = 0x17, SPSM)<br>L2CAP_CREDIT_BASED_CONNECTION_RSP<br>(Code = 0x18, SPSM, Destination CID =<br>duplicate)<br>**----- End of picture text -----**<br>

_Figure 4.209: L2CAP Credit Based Connection Response – Duplicate DCID MSC_

1. The Upper Tester commands the IUT to send a connection request on the SPSM declared via IXIT.

2. The IUT sends an L2CAP_CREDIT_BASED_CONNECTION_REQ (Code = 0x17) to the Lower Tester.

3. The Lower Tester sends an L2CAP_CREDIT_BASED_CONNECTION_RSP (Code = 0x18) having a duplicate DCID to the IUT.

4. The IUT detects the duplicate Destination CID and does not continue to use the original channel or the new channel. If a mechanism is available, the Upper Tester attempts to send data over each channel to verify this.

-

- Expected Outcome

## Pass verdict

The IUT does not continue to use either the original channel or the new channel with the duplicate Destination CID.

- **4.15.1.26 Renegotiate MPS – MPS value is decreased, Multiple Channels**

- Test Purpose

Verify that the IUT refuses the MPS reconfiguration request for multiple Data Channels created through Enhanced Credit Based Flow Control mode when receiving an L2CAP Credit Based Reconfigure Request with an MPS value between other existing MPU values for multiple channels.

- Reference

[15] 4.27

- Initial Condition

- The signaling channel specified in Table 4.53 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **279 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- A Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value, with the MPS on the Lower Tester side of at least 65 octets.

- Test Case Configuration

|**Test Case ID**|**Signaling Channel**|
|L2CAP/ECFC/BI-07-C [L2CAP Credit Based Connection Response –<br>Duplicate DCID, LE]|0x0005|
|L2CAP/ECFC/BI-16-C [L2CAP Credit Based Connection Response –<br>Duplicate DCID, BR/EDR]|0x0001|

_Table 4.53: L2CAP Credit Based Connection Response – Duplicate DCID test cases_

- Test Procedure

**==> picture [374 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between the IUT and the Lower Tester<br>Two L2CAP channels over the relevant SPSM have been established between the IUT and the Lower Tester<br>MPSInitial > 64<br>L2CAP_Credit_Based_Reconfigure_Req<br>(Code = 0x19, DCID = [A, B], MPS < MPSInitial)<br>L2CAP_Credit_Based_Reconfigure_Rsp<br>(Code = 0x1A, Result = 0x0002)<br>**----- End of picture text -----**<br>

_Figure 4.210: Renegotiate MPS – MPS value is decreased, Multiple Channels MSC_

1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request (Code = 0x19) packet to the IUT, with Destination CID containing the list of CIDs of the opened channels and with the MPS field value lower than the MPS value for one of the Destination CIDs that was negotiated during initial configuration.

2. The IUT does not disconnect the channel. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time).

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time).

## **4.15.2 LE Credit Based Flow Control Mode**

## **L2CAP/LE/CFC/BV-01-C [LE Credit Based Connection Request - Legacy Peer]**

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request to a legacy peer and receiving a Command Reject does not establish the channel.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **280 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

- [12] 4.22

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An SPSM for the desired LE Credit Based Flow Control based Channel is declared via the TSPX_spsm IXIT value.

- Test Procedure

**==> picture [306 x 183] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established<br>LE_Credit_Based_Connection_Request<br>(SPSM, Source CID, MTU, MPS, Initial credits)<br>L2CAP_Command_reject on CID=5<br>(Result)<br>L2CAP Command Reject<br>Passed to Upper Tester<br>**----- End of picture text -----**<br>

_Figure 4.211: L2CAP/LE/CFC/BV-01-C [LE Credit Based Connection Request - Legacy Peer] MSC_

The IUT sends an LE Credit Based Connection Request on an SPSM indicated in the IXIT.

The Lower Tester responds with a Command Reject.

-

- Expected Outcome

## Pass verdict

After receiving the Command Reject from the Lower Tester, the IUT inform the Upper Tester.

## **L2CAP/LE/CFC/BV-02-C [LE Credit Based Connection Request on Supported SPSM]**

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request to a peer establishes the channel upon receiving the LE Credit Based Connection Response.

- Reference

[12] 4.22

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An SPSM for the desired LE Credit Based Flow Control based Channel is declared in the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to send credits.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **281 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [375 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>LE Credit Based Connection<br>Request<br>LE_Credit_Based_Connection_Request<br>(SPSM, Source CID, MTU, MPS,<br>Initial credits)<br>LE_Credit_Based_Connection_Rsp<br>LE Credit Based Flow Control Channel Established<br>Send credits<br>ALT 1 LE_Flow_Control_Credit<br>Data<br>Data<br>**----- End of picture text -----**<br>

_Figure 4.212: L2CAP/LE/CFC/BV-02-C [LE Credit Based Connection Request on Supported SPSM] MSC_

The IUT sends an LE Credit Based Connection Request on the SPSM declared in IXIT.

The Lower Tester responds with an LE Credit Based Connection response PDU.

(ALT1) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data on the established channel.

- Expected Outcome

## Pass verdict

The IUT receives the data send by the Lower Tester on the correct channel. The data is passed to the Upper Tester.

## **L2CAP/LE/CFC/BV-03-C [LE Credit Based Connection Response on Supported SPSM]**

- Test Purpose

Verify that an IUT receiving a valid LE Credit Based Connection Request from a peer sends an LE Credit Based Connection Response and establishes the channel.

- Reference

[12] 4.23

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An SPSM for the desired LE Credit Based Flow Control based channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to send data.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **282 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [368 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel is established between the Lower Tester and IUT<br>LE_Credit_Based_Connection_Request<br>(SPSM, Source CID, MTU, MPS, Initial credits)<br>LE_Credit_Based_Connection_Rsp<br>LE Credit Based Flow Control Channel established<br>Data<br>Data (K-frame(s))<br>**----- End of picture text -----**<br>

_Figure 4.213: L2CAP/LE/CFC/BV-03-C [LE Credit Based Connection Response on Supported SPSM] MSC_

The Lower Tester sends an LE Credit Based Connection Request with nonzero credits to the IUT on the SPSM specified in initial conditions.

The IUT responds with an LE Credit Based Connection Response.

The IUT is commanded to send data on the LE data channel by the Upper Tester.

-

- Expected Outcome

## Pass verdict

The IUT sends one or more correctly formatted K-frames on the correct channel to the Lower Tester.

The data sent by the IUT to the Lower Tester matches the data sent by the Upper Tester to the IUT.

## **L2CAP/LE/CFC/BV-04-C [LE Credit Based Connection Request on an unsupported SPSM]**

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request on an unsupported SPSM does not establish a channel upon receiving an LE Credit Based Connection Response refusing the connection.

- Reference

[12] 4.22

-

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An SPSM for an unsupported LE Credit Based Flow Control based channel is declared via the TSPX_psm_unsupported IXIT value.

- The Upper Tester can command the IUT to create a connection.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **283 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [375 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>LE Credit Based Connection<br>Request<br>LE_Credit_Based_Connection_Request<br>(Unsupported PSM)<br>LE_Credit_Based_Connection_Response LE Credit Based Connection<br>(Connection refused – SPSM not supported) Response<br>(failure)<br>**----- End of picture text -----**<br>

_Figure 4.214: L2CAP/LE/CFC/BV-04-C [LE Credit Based Connection Request on an unsupported SPSM] MSC_

The IUT sends an LE Credit Based Connection Request PDU on the SPSM specified in the initial conditions which is not supported by the Lower Tester.

The Lower Tester responds with an LE Credit Based Connection Response with result “0x0002 – Connection Refused – SPSM not supported”.

-

- Expected Outcome

## Pass verdict

The IUT receives an LE Credit Based Connection Response PDU with result “0x0002 – Connection Refused – SPSM not supported” from the Lower Tester. This is indicated to the Upper Tester.

## **L2CAP/LE/CFC/BV-05-C [LE Credit Based Connection Request - unsupported SPSM]**

- Test Purpose

Verify that an IUT receiving an LE Credit Based Connection Request on an unsupported SPSM responds with an LE Credit Based Connection Response refusing the connection.

- Reference

- [12] 4.23

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An SPSM for an unsupported LE Credit Based Flow Control based channel is declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **284 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [375 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>LE_Credit_Based_Connection_Request<br>(Unsupported PSM)<br>LE_Credit_Based_Connection_Response<br>(Connection refused – SPSM not supported)<br>**----- End of picture text -----**<br>

_Figure 4.215: L2CAP/LE/CFC/BV-05-C [LE Credit Based Connection Request - unsupported SPSM] MSC_

The Lower Tester sends an LE Credit Based Connection Request on the SPSM specified in initial conditions.

- Expected Outcome

## Pass verdict

Upon receiving an LE Credit Based Connection Request containing an unsupported SPSM, the IUT sends a correctly formatted LE Credit Based Connection Response to the Lower Tester with Result “0x0002 – Connection Refused – SPSM not supported.

**L2CAP/LE/CFC/BV-06-C [Credit Exchange – Receiving Incremental Credits]**

- Test Purpose

Verify that the IUT handles flow control correctly, by handling the LE Flow Control Credit sent by the peer.

- Reference

[12] 4.24

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An LE Data Channel is established on an SPSM indicated in the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The initial credit on the LE Data Channel set by the Lower Tester is 0.

- The Upper Tester can command the IUT to send data.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **285 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [376 x 322] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>LE Credit Based Flow Control channel established<br>Initial Credit =0<br>Command the IUT to send data<br>LECredit Increment =1_Flow_Control_Credit<br>K-frame<br>LECredit Increment =1_Flow_Control_Credit<br>K-frame<br>LECredit Increment =2_Flow_Control_Credit<br>K-frame<br>K-frame<br>**----- End of picture text -----**<br>

_Figure 4.216: L2CAP/LE/CFC/BV-06-C [Credit Exchange – Receiving Incremental Credits] MSC_

1. The Upper Tester requests the IUT to send data packets to the Lower Tester.

2. The Lower Tester sends an LE Flow Control Credit Packet with Credit Value X to the IUT on the CID.

3. The IUT now sends K-frames containing data to the Lower Tester.

4. After receiving X K-frames from the IUT and ensuring that no more K-frames are received, the Lower Tester sends a new LE Flow Control Credit packet with a Credits value of X on the CID. The IUT sends X K-frames containing data to the Lower Tester.

5. The Test Procedure Steps 2–4 are repeated with credit increment X ={1,>1} without disconnecting the channel.

-

- Expected Outcome

## Pass verdict

After receiving X credits, the IUT sends X correctly formatted K-frames containing data to the Lower Tester.

The IUT stops sending K-frames to the Lower Tester after the credit count X reaches zero.

After receiving X credits, the IUT sends (X) correctly formatted K-frames containing data to the Lower Tester.

The IUT stops sending K-frames to the Lower Tester after the credit count X reaches zero.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **286 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/LE/CFC/BV-07-C [Credit Exchange – Sending Credits]**

- Test Purpose

Verify that the IUT sends LE Flow Control Credit to the peer.

- Reference

- [12] 4.24

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An LE Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The Upper Tester can command the IUT to send credits.

- Test Procedure

**==> picture [376 x 201] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>LE Credit Based Flow Control channel established<br>Send credits<br>ALT 1 LE_Flow_Control_Credit<br>Data packet<br>Data packet<br>Data packet<br>**----- End of picture text -----**<br>

_Figure 4.217: L2CAP/LE/CFC/BV-07-C [Credit Exchange – Sending Credits] MSC_

(ALT1) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data packets to the IUT until it gets credits returned i.e., the data to send could consume more than the current credits available on the channel.

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted LE Flow Control Credit packet to the Lower Tester minimum ones doing the data transfer.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **287 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **L2CAP/LE/CFC/BI-01-C [Credit Exchange – Exceed Initial Credits]**

- Test Purpose

Verify that the IUT disconnects the LE Data Channel when the credit count exceeds 65535.

- Reference

- [12] 4.24, 10.1

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An LE Data Channel is established on an SPSM indicated in the TSPX_spsm IXIT value.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

- The initial credit on the LE Data Channel set by the Lower Tester is more than 1.

- Test Procedure

**==> picture [376 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>LE Credit Based Flow Control channel established<br>Initial Credit: X<br>Data packet<br>Optional<br>Data packet<br>. .. Data packet<br>L2CAPCredit > (65535 – (X – Packets Sent))_LE_Flow_Control_Credit<br>L2CAP_Disconnect_Req<br>L2CAP_Disconnect_Rsp<br>**----- End of picture text -----**<br>

_Figure 4.218: L2CAP/LE/CFC/BI-01-C [Credit Exchange – Exceed Initial Credits] MSC_

(Optional) The IUT sends data packets to the Lower Tester.

The Lower Tester sends an LE Flow Control Credit PDU packet containing a credit so large that it together with the remaining credits on the IUT exceeds 65535.

-

- Expected Outcome

## Pass verdict

Upon receiving a credit overflow, the IUT disconnects the LE Data Channel.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **288 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**L2CAP/LE/CFC/BV-11-C [Security - Insufficient Authentication – Responder]**

- Test Purpose

Verify that an IUT refuses to create a connection upon reception of an LE Credit Based Connection Request which fails to satisfy authentication requirements.

- Reference

- [12] 4.22

- Initial Condition

- The appropriate signaling channel for the transport is used.

- An SPSM for the desired LE Credit Based Flow Control based Channel with authentication requirements is declared via the TSPX_psm_authentication_required IXIT value.

- No authentication procedure has been performed between the IUT and the Lower Tester.

- Test Procedure

**==> picture [378 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>LE_Credit_Based_Connection_Request<br>(SPSM, Source CID, MTU, MPS,<br>Initial credits)<br>**----- End of picture text -----**<br>

_Figure 4.219: L2CAP/LE/CFC/BV-11-C [Security - Insufficient Authentication – Responder] MSC_

1. The Lower Tester sends an LE Credit Based Connection Request on the SPSM specified in the initial conditions that requires authentication.

2. The IUT rejects the connection request with error code “Insufficient Authentication”.

-

- Expected Outcome

## Pass verdict

Upon reception of an LE Credit Based Connection Request from the Lower Tester which fails to satisfy the authentication requirements, the IUT sends a correctly formatted LE Credit Based Connection Response with Result “0x0005 – Connection Refused – Insufficient Authentication” to the Lower Tester.

- **L2CAP/LE/CFC/BV-14-C [Security - Insufficient Encryption Key Size – Initiator]**

- Test Purpose

Verify that the IUT does not establish the channel upon receipt of an LE Credit Based Connection Response indicating the connection was refused with Result “0x0007 – Connection Refused – Insufficient Encryption Key Size”.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **289 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Reference

- [12] 4.22

- Initial Condition

- The appropriate signaling channel for the transport is used.

- The Upper Tester can command the IUT to create a connection.

- Either an Unauthenticated or Authenticated LTK exists between the IUT and Lower Tester.

- Test Procedure

**==> picture [303 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUT<br>Security Level is maximum unauthenticated<br>E.g. LE_CFC_Connect<br>LE_Credit_Based_Connection_Req (SPSM)<br>LE_Credit_Based_Connection_Rsp<br>(Connection Refused - Insufficient<br>Encryption Key Size) E.g. Request Rejected<br>**----- End of picture text -----**<br>

_Figure 4.220: L2CAP/LE/CFC/BV-14-C [Security - Insufficient Encryption Key Size – Initiator] MSC_

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester refuses the Connection Request with result “0x0007 - Connection Refused - Insufficient Encryption Key Size”.

-

- Expected Outcome

Pass verdict

The IUT informs the Upper Tester about the rejection.

## **L2CAP/LE/CFC/BV-17-C [LE Credit Based Connection Response - refused due to insufficient resources - Responder]**

- Test Purpose

Verify that an IUT receiving an LE Credit Based Connection Request for a second channel refuses the connection with result "0x0004 - Connection refused – no resources available" if it does not support multiple simultaneous channels.

- Reference

[12] 4.22

- Initial Condition

- The appropriate signaling channel for the transport is used.

- One LE Data channel is established on an SPSM declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **290 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [341 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUTIUT Upper Tester<br>LE Credit Based Flow Control channel established<br>LE_Credit_Based_Connection_Request<br>(LE_PSM, Source CID (second CID), MTU,<br>MPS, Initial credits)<br>LE_Credit_Based_Connection_Rsp<br> (Connection refused – No resources available)<br>**----- End of picture text -----**<br>

_Figure 4.221: L2CAP/LE/CFC/BV-17-C [LE Credit Based Connection Response - refused due to insufficient resources - Responder] MSC_

The Lower Tester sends an LE Credit Based Connection Request on a different CID to than the first.

-

- Expected Outcome

## Pass verdict

Upon receiving an LE Credit Based Connection Request from the Lower Tester on a different CID than the previously-established channel, the IUT sends a correctly formatted LE Credit Based Connection Response to the Lower Tester with Result “0x0004 – Connection Refused – no resources available”.

**L2CAP/LE/CFC/BV-18-C [LE Credit Based Connection Request - refused due to Invalid Source CID - Initiator]**

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request does not establish the channel upon receiving an LE Credit Based Connection Response refusing the connection with result "0x0009 – Connection refused – Invalid Source CID".

- Reference

- [12] 4.22

-

- Initial Condition

- The appropriate signaling channel for the transport is used.

- The Upper Tester can command the IUT to create a connection.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **291 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [306 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between the Lower Tester and IUT<br>E.g. LE_CFC_Connect (SPSM)<br>LE_Credit_Based_Connection_Req<br>LE_Credit_Based_Connection_Rsp<br>(Connection refused – Invalid E.g. Request Rejected<br>Source CID)<br>data<br>**----- End of picture text -----**<br>

_Figure 4.222: L2CAP/LE/CFC/BV-18-C [LE Credit Based Connection Request - refused due to Invalid Source CID - Initiator] MSC_

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester Refuses the Connection Request with an LE Credit Based Connection Response with result “0x0009 – Connection Refused – Invalid Source CID”.

The Upper Tester commands the IUT to send data on the refused CID.

-

- Expected Outcome

Pass verdict

The IUT informs the Upper Tester the connection was refused.

The Lower Tester does not receive any data from the IUT on the refused CID.

**L2CAP/LE/CFC/BV-19-C [LE Credit Based Connection Request - refused due to source CID already allocated - Initiator]**

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request does not establish the channel upon receiving an LE Credit Based Connection Response refusing the connection with result "0x000A – Connection refused – Source CID already allocated".

- Reference

- [12] 4.22

- Initial Condition

- The appropriate signaling channel for the transport is used.

- The Upper Tester can command the IUT to create a connection.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **292 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [305 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between LT and IUT<br>E.g. LE_CFC_Connect (SPSM)<br>LE_Credit_Based_Connection_Req<br>LE_Credit_Based_Connection_Rsp<br>(Connection refused – Source CID<br>already allocated) E.g. Request Rejected<br>data<br>**----- End of picture text -----**<br>

_Figure 4.223: L2CAP/LE/CFC/BV-19-C [LE Credit Based Connection Request - refused due to source CID already allocated - Initiator] MSC_

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester Refuses the Connection Request with an LE Credit Based Connection Response with result “0x000A – Connection Refused – Source CID already allocated”.

The Upper Tester commands the IUT to send data on the refused CID.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester the connection was refused.

The Lower tester does not receive any data from the IUT on the refused CID.

**L2CAP/LE/CFC/BV-20-C [LE Credit Based Connection Response - refused due to Source CID already allocated - Responder]**

- Test Purpose

Verify that an IUT receiving an LE Credit Based Connection Request for a second channel refuses the connection with result "0x000A - Connection refused – Source CID already allocated" if it receives a Source CID which is already in use.

- Reference

- [12] 4.23

- Initial Condition

- The appropriate signaling channel for the transport is used.

- One LE Data channel is established on an SPSM declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **293 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [372 x 220] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel established between Lower Tester and IUTIUT Upper Tester<br>LE Credit Based Flow Control channel established<br>LE_Credit_Based_Connection_Request<br>(LE_PSM, Source CID (duplicate CID), MTU,<br>MPS, Initial credits)<br>LE_Credit_Based_Connection_Rsp (Connection<br>refused – Source CID already allocated )<br>Alternate 1<br>or<br>Alternate 2 Command Reject Packet, reason = 0x0002,<br>Invalid CID in request )<br>**----- End of picture text -----**<br>

_Figure 4.224: L2CAP/LE/CFC/BV-20-C [LE Credit Based Connection Response - refused due to Source CID already allocated - Responder] MSC_

The Lower Tester sends an LE Credit Based Connection Request using the same CID as the previously established channel.

-

- Expected Outcome

## Pass verdict

ALT1: Upon receipt of an LE Credit Based Connection Request using the same CID as the previously established channel, the IUT sends a correctly formatted LE Credit Based Connection Response to the Lower Tester with Result=0x000A - Connection Refused – Source CID already allocated.

ALT2: The IUT sends a correctly formatted Command Reject to the Lower Tester with Reason=0x0002 – Invalid CID in request.

## **L2CAP/LE/CFC/BV-21-C [LE Credit Based Connection Request - refused due to Unacceptable Parameters - Initiator]**

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request does not establish the channel upon receiving an LE Credit Based Connection Response refusing the connection with result “0x000B – Connection refused – Unacceptable Parameters”.

- Reference

[12] 4.22

- Initial Condition

- The appropriate signaling channel for the transport is used.

- The Upper Tester can command the IUT to create a connection.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **294 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [305 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>L2CAP fixed channel is established between the Lower Tester and IUT<br>E.g. LE_CFC_Connect (SPSM)<br>LE_Credit_Based_Connection_Req<br>LE_Credit_Based_Connection_Rsp<br>(Connection refused – Unacceptable<br>E.g. Request Rejected<br>Parameters)<br>**----- End of picture text -----**<br>

_Figure 4.225: L2CAP/LE/CFC/BV-21-C [LE Credit Based Connection Request - refused due to Unacceptable Parameters - Initiator] MSC_

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester refuses the Connection Request with an LE Credit Based Connection Response with result “0x000B – Connection Refused – Unacceptable Parameters”.

The Upper Tester commands the IUT to send data on the refused CID.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester the connection was refused.

The Lower Tester does not receive any data from the IUT on the refused CID.

- **4.15.2.1 Credit Based Connection Request Dynamically Allocated Source CID**

- Test Purpose

Verify that an IUT sending a Credit Based Connection Request to a peer allocates the Source CID from a dynamically allocated range and does not allocate one already in use.

- Reference

- [12] 4.22

- Initial Condition

- The signaling channel specified in Table 4.54 is used.

- An SPSM for the desired LE Credit Based or Enhanced Credit Based Flow Control based Channel is declared in the TSPX_spsm or the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to send credits.

- A value for the number of concurrent Credit Based Connections is defined by the TSPX_l2ca_num_concurrent_credit_based_connections IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **295 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/ECFC/BV-38-C [Credit<br>Based Connection Request<br>Dynamically Allocated Source<br>CID – LE]|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ<br>L2CAP_CREDIT_BASED_CONNECTION_RSP|
|L2CAP/LE/CFC/BV-29-C [Credit<br>Based Connection Request<br>Dynamically Allocated Source<br>CID]|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ<br>L2CAP_LE_CREDIT_BASED_CONNECTION_RSP|
|L2CAP/ECFC/BV-79-C [Credit<br>Based Connection Request<br>Dynamically Allocated Source<br>CID – BR/EDR]|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ<br>L2CAP_CREDIT_BASED_CONNECTION_RSP|

_Table 4.54: Credit Based Connection Request Dynamically Allocated Source CID test cases_

- Test Procedure

**==> picture [340 x 281] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>An L2CAP fixed channel Is established between the Lower Tester and the IUT<br>REPEAT<br>Create L2CAP [...]Credit Based Channel<br>L2CAP[ ]Credit_Based_Connection_Req<br>(SPSM, Source CID)<br>L2CAP[ ]Credit_Based_Connection_Rsp<br>(Destination CID)<br>L2CAP fixed channel established between the Lower Tester and the IUT<br>Create L2CAP [...]Credit Based Channel<br>Response<br>REPEAT for all the established channels<br>L2CAP(Source CID, Destination CID)_DISCONNECTION_REQ<br>L2CAP(Source CID, Destination CID)_DISCONNECTION_RSP<br>**----- End of picture text -----**<br>

_Figure 4.226: Credit Based Connection Request Dynamically Allocated Source CID MSC_

1. Perform Steps 2–6 a total of TSPX_l2ca_num_concurrent_credit_based_connections times.

2. The Upper Tester commands the IUT to create an L2CAP connection to the Lower Tester.

3. The IUT sends an L2CAP request command as specified in Table 4.54 to the Lower Tester on the SPSM as specified in Table 4.54 with a Source CID.

4. The Lower Tester confirms that the Source CID received in Step 3 is within the range 0x0040– 0x007F and is not the same as any of the Source CIDs received during this test procedure.

5. The Lower Tester sends an L2CAP response command as specified in Table 4.54 to the IUT with a Destination CID.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **296 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

6. The IUT notifies the Upper Tester that an L2CAP connection was completed with the Source CID from Step 3 and the Destination CID received in Step 5.

7. Repeat Steps 8 and 9 for all established channels.

8. The Lower Tester sends an L2CAP_DISCONNECTION_REQ PDU to the IUT with the Source CID and the Destination CIDs from Steps 2–6.

9. The IUT sends an L2CAP_DISCONNECTION_RSP PDU to the Lower Tester with the Source CID and the Destination CIDs set as received in Step 8.

- Expected Outcome

## Pass verdict

In Step 3, the Source CID in the L2CAP request command is in the range of 0x40–0x7F.

In each iteration of Step 3, the Source CID is not the same as any Source CID of an existing connection.

## **4.15.3 All Credit Based Flow Control Mode**

## **4.15.3.1 Disconnection Request**

- Test Purpose

Verify that the IUT can disconnect the channel.

- Initial Condition

- The signaling channel specified in Table 4.55 is used.

- A Data Channel as specified in Table 4.55 is established on the SPSM declared via the TSPX_spsm IXIT value using the commands specified in Table 4.55.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **297 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-08-C[Disconnection Request]|[12]4.6|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-08-C[Disconnection Request, LE]|[13]4.6|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-65-C[Disconnection Request, BR/EDR]|[13]4.6|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.55: Disconnection Request test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **298 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

**==> picture [373 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>An L2CAP channel on the relevant SPSM is established between the IUT and the Lower Tester<br>Disconnect L2CAP Channel<br>L2CAP_DISCONNECTION_REQ<br>(Code = 0x06)<br>L2CAP_DISCONNECTION_RSP<br>(Code = 0x07)<br>Channel Disconnected<br>**----- End of picture text -----**<br>

_Figure 4.227: Disconnection Request MSC_

1. The Upper Tester commands the IUT to disconnect the channel.

2. The IUT sends L2CAP Disconnection Request (Code = 0x06) to the Lower Tester.

3. The Lower Tester sends an L2CAP Disconnection Response (Code = 0x07).

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP_Disconnect_Req to the Lower Tester.

## **4.15.3.2 Disconnection Response**

- Test Purpose

Verify that the IUT responds correctly to reception of a Disconnection Request.

- Initial Condition

- The signaling channel specified in Table 4.56 is used.

- A Data Channel as specified in Table 4.56 is established on the SPSM declared via the TSPX_spsm IXIT value using the commands specified in Table 4.56.

- The role of the IUT is indicated in the TSPX_iut_role_initiator IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **299 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-09-C[Disconnection Response]|[12]4.7|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-09-C[Disconnection Response, LE]|[13]4.7|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-66-C [Disconnection Response,<br>BR/EDR]|[13]4.7|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.56: Disconnection Response test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **300 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [378 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP channel established between the IUT and the Lower Tester<br>L2CAP_Disconnection_Req<br>(Code = 0x06)<br>L2CAP_Disconnection_Rsp<br>(Code = 0x07)<br>Channel Disconnected<br>**----- End of picture text -----**<br>

_Figure 4.228: Disconnect Response MSC_

1. The Lower Tester sends an L2CAP Disconnection Request (Code = 0x06) to the IUT.

2. The IUT sends an L2CAP Disconnection Response (Code = 0x07) to the Lower Tester.

-

- Expected Outcome

## Pass verdict

The IUT responds to the request to disconnect the channel with a correctly formatted L2CAP_Disconnection Response.

- **4.15.3.3 Security – Insufficient Authentication – Initiator**

- Test Purpose

Verify that the IUT does not establish any channel upon receipt of an L2CAP LE Credit Based Connection Response / L2CAP Credit Based Connection Response indicating the connections were refused with Result 0x0005 (“All connections refused – insufficient authentication”).

- Initial Condition

- The signaling channel specified in Table 4.57 is used.

- The Upper Tester can command the IUT to create a credit based channel on an SPSM declared via the TSPX_psm_authentication_required IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **301 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**Signaling Commands**|**Result**|
|L2CAP/LE/CFC/BV-10-C<br>[Security – Insufficient<br>Authentication – Initiator]|[12]4.22|0x0005|L2CAP LE Credit Based Connection Request<br>(Code = 0x14)<br>L2CAP LE Credit Based Connection<br>Response(Code = 0x15)|0x0005 – Connection refused –<br>insufficient authentication|
|L2CAP/ECFC/BV-10-C [Security<br>– Insufficient Authentication –<br>Initiator, LE]|[13]4.25|0x0005|L2CAP Credit Based Connection Request<br>(Code = 0x17)<br>L2CAP Credit Based Connection Response<br>(Code = 0x18)|0x0005 – All connections refused –<br>insufficient authentication|
|L2CAP/ECFC/BV-67-C [Security<br>– Insufficient Authentication –<br>Initiator, BR/EDR]|[13]4.25|0x0001|L2CAP Credit Based Connection Request<br>(Code = 0x17)<br>L2CAP Credit Based Connection Response<br>(Code = 0x18)|0x0005 – All connections refused –<br>insufficient authentication|

_Table 4.57: Security – Insufficient Authentication – Initiator test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **302 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [378 x 196] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, All connections refused - insufficient<br>authentication) Create L2CAP Credit Based Channel Response<br>(result)<br>**----- End of picture text -----**<br>

_Figure 4.229: Security – Insufficient Authentication – Initiator MSC_

1. The Upper Tester commands the IUT to send a connection request.

2. The IUT sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17), as in Table 4.57.

3. The Lower Tester sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0005, as in Table 4.57, refusing the channel creation request.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

## **4.15.3.4 Security – Insufficient Authorization – Initiator**

- Test Purpose

Verify that the IUT does not establish any channel upon receipt of an L2CAP LE Credit Based Connection Response / L2CAP Credit Based Connection Response indicating the connections were refused with Result 0x0006.

- Initial Condition

- The signaling channel specified in Table 4.58 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_psm_authorization_required IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_psm_authorization_required IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **303 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**Signaling Commands**|**Result**|
|L2CAP/LE/CFC/BV-12-C<br>[Security – Insufficient<br>Authorization – Initiator]|[12]4.22|0x0005|L2CAP LE Credit Based Connection Request<br>(Code = 0x14)<br>L2CAP LE Credit Based Connection<br>Response(Code = 0x15)|0x0006 – Connection refused –<br>insufficient authorization|
|L2CAP/ECFC/BV-12-C [Security<br>– Insufficient Authorization –<br>Initiator, LE]|[13]4.25|0x0005|L2CAP Credit Based Connection Request<br>(Code = 0x17)<br>L2CAP Credit Based Connection Response<br>(Code = 0x18)|0x0006 – All connections refused –<br>insufficient authorization|
|L2CAP/ECFC/BV-68-C [Security<br>– Insufficient Authorization –<br>Initiator, BR/EDR]|[13]4.25|0x0001|L2CAP Credit Based Connection Request<br>(Code = 0x17)<br>L2CAP Credit Based Connection Response<br>(Code = 0x18)|0x0006 – All connections refused –<br>insufficient authorization|

_Table 4.58: Security – Insufficient Authorization – Initiator test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **304 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [377 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, All connections refused -<br>insufficient authorization) Create L2CAP Credit Based Channel Response<br>(result)<br>**----- End of picture text -----**<br>

_Figure 4.230: Security – Insufficient Authorization – Initiator MSC_

1. The Upper Tester commands the IUT to send a connection request.

2. The IUT sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17), as in Table 4.58.

3. The Lower Tester sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0006, as in Table 4.58, refusing the connection request.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

- **4.15.3.5 Security – Insufficient Authorization – Responder**

- Test Purpose

Verify that an IUT refuses to create any connection upon reception of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request which fails to satisfy authorization requirements.

- Initial Condition

- An LE ACL connection is established between the IUT and the Lower Tester.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_psm_authorization_required IXIT value.

- An authorization requirement exists for the SPSM declared via the TSPX_psm_authorization_required IXIT value.

- No authorization procedure has been performed between the IUT and the Lower Tester.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **305 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling Commands**|**Result**|
|L2CAP/LE/CFC/BV-13-C<br>[Security – Insufficient<br>Authorization – Responder]|[12]4.22|L2CAP LE Credit Based Connection Request (Code = 0x14)<br>L2CAP LE Credit Based Connection Response (Code = 0x15)|0x0006 – Connection<br>refused – insufficient<br>authorization|
|L2CAP/ECFC/BV-13-C [Security<br>– Insufficient Authorization –<br>Responder, LE]|[13]4.25|L2CAP Credit Based Connection Request (Code = 0x17)<br>L2CAP Credit Based Connection Response (Code = 0x18)|0x0006 – All connections<br>refused – insufficient<br>authorization|

_Table 4.59: Security – Insufficient Authorization – Responder test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **306 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [398 x 97] intentionally omitted <==**

_Figure 4.231: Security – Insufficient Authorization – Responder MSC_

1. The Lower Tester sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17).

2. The IUT detects the authorization requirement and sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18), rejecting the connection request with result 0x0006, as in Table 4.59.

-

- Expected Outcome

## Pass verdict

Upon reception of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request from the Lower Tester which fails to satisfy the authorization requirements, the IUT sends a correctly formatted L2CAP LE Credit Based Connection Response / L2CAP Credit Based Connection Response with Result 0x0006 to the Lower Tester.

- **4.15.3.6 Security – Insufficient Encryption Key Size – Responder**

- Test Purpose

Verify that an IUT refuses to create any connection upon receipt of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request which fails to satisfy Encryption Key Size requirements.

- Initial Condition

- The signaling channel specified in Table 4.60 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_psm_encryption_key_size_required IXIT value.

- An encrypted link over the transport is established between the IUT and the Lower Tester. The minimum key size required for the SPSM is declared via the TSPX_Min_Encryption_Key_Length IXIT value. If it is greater than the minimum encryption key size defined by the specification, then the encryption key size used by the Lower Tester is less than the minimum encryption key size, otherwise the Lower Tester uses an encryption key size that is equal to the minimum encryption key size defined by the specification.

- A preamble procedure defined in Section 4.10.2 is used to set up an encrypted link.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **307 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**Signaling Commands**|**Result**|
|L2CAP/LE/CFC/BV-15-C<br>[Security – Insufficient Encryption<br>Key Size – Responder]|[12]4.22|0x0005|L2CAP LE Credit Based Connection<br>Request (Code = 0x14)<br>L2CAP LE Credit Based Connection<br>Response(Code = 0x15)|0x0007 – Connection refused –<br>insufficient encryption key size|
|L2CAP/ECFC/BV-15-C [Security<br>– Insufficient Encryption Key Size<br>– Responder, LE]|[13]4.25|0x0005|L2CAP Credit Based Connection<br>Request (Code = 0x17)<br>L2CAP Credit Based Connection<br>Response(Code = 0x18)|0x0007 – All connections refused –<br>insufficient encryption key size|
|L2CAP/ECFC/BV-70-C [Security<br>– Insufficient Encryption Key Size<br>– Responder, BR/EDR]|[13]4.25|0x0001|L2CAP Credit Based Connection<br>Request (Code = 0x17)<br>L2CAP Credit Based Connection<br>Response(Code = 0x18)|0x0007 – All connections refused –<br>insufficient encryption key size|

_Table 4.60: Security – Insufficient Encryption Key Size – Responder test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **308 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [378 x 160] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, All connections refused -<br>insufficient encryption key size)<br>**----- End of picture text -----**<br>

_Figure 4.232: Security – Insufficient Encryption Key Size – Responder MSC_

1. The Lower Tester sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17).

2. If the minimum encryption key size for the PSM is greater than the minimum encryption key size defined by the specification: ALT 1 is followed and the IUT detects the encryption key size too short for the requirement and sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18), rejecting the connection request with Result = 0x0007, as in Table 4.60.

- If the minimum encryption key size for the PSM is equal to the minimum encryption key size defined by the specification: ALT 2 is followed, and the connection is successful.

-

- Expected Outcome

## Pass verdict

Upon reception of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request from the Lower Tester which fails to satisfy the encryption key size requirements, the IUT sends a correctly formatted L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Response with Result 0x0007 to the Lower Tester.

If the minimum encryption key size for the PSM is equal to the minimum encryption key size defined by the specification, the request from the Lower Tester does not fail to satisfy the encryption key size requirement, and the connection is successful.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **309 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- **4.15.3.7 L2CAP Credit Based Connection Request – refused due to insufficient resources**

- Test Purpose

Verify that an IUT sending an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request does not establish some of the requested channels upon receiving an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Response refusing the connection with result 0x0004.

- Initial Condition

- The signaling channel specified in Table 4.61 is used.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

- The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **310 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**Signaling Commands**|**Result**|
|L2CAP/LE/CFC/BV-16-C [L2CAP<br>LE Credit Based Connection<br>Request – refused due to<br>insufficient resources]|[12]4.22|0x0005|L2CAP LE Credit Based Connection<br>Request (Code = 0x14)<br>L2CAP LE Credit Based Connection<br>Response(Code = 0x15)|0x0004 – Connection refused –<br>insufficient resources available|
|L2CAP/ECFC/BV-16-C [L2CAP<br>Credit Based Connection<br>Request – refused due to<br>insufficient resources, LE]|[13]4.25|0x0005|L2CAP Credit Based Connection Request<br>(Code = 0x17)<br>L2CAP Credit Based Connection<br>Response(Code = 0x18)|0x0004 – Some connections<br>refused – insufficient resources<br>available|
|L2CAP/ECFC/BV-71-C [L2CAP<br>Credit Based Connection<br>Request – refused due to<br>insufficient resources, BR/EDR]|[13]4.25|0x0001|L2CAP Credit Based Connection Request<br>(Code = 0x17)<br>L2CAP Credit Based Connection<br>Response(Code = 0x18)|0x0004 – Some connections<br>refused – insufficient resources<br>available|

_Table 4.61: L2CAP Credit Based Connection Request – refused due to insufficient resources test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **311 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [379 x 264] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM, one or more channels)<br>L2CAP_Credit_Based_Connection_Req<br>(Code = 0x17, SPSM, SCID=[...],<br>MTU, MPS, Initial Credits)<br>L2CAP_Credit_Based_Connection_Rsp<br>(Code = 0x18, Some connections refused -<br>insufficient resources available) Create L2CAP Credit Based Channel Response<br>(result)<br>ALT1<br>An L2CAP channel on the relevant SPSM is established between IUT and Lower Tester<br>Data<br>Data (K Frames)<br>**----- End of picture text -----**<br>

_Figure 4.233: L2CAP Credit Based Connection Request – refused due to insufficient resources MSC_

1. The Upper Tester commands the IUT to send a connection request.

2. The Lower Tester sends an L2CAP LE Credit Based Connection Response (0x15) / L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0004, as in Table 4.61, refusing the connection request.

3. (ALT1) If run over an Enhanced Credit Based Flow Control channel and the connection request was performed with more than one SCID and some of the channels were created, the Upper Tester commands the IUT to send data on the accepted CIDs.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

(ALT1) The data sent by the IUT in Step 3 must be the same as that received by the Lower Tester.

The IUT does not send any data to the Lower Tester on the refused CID(s).

## **4.15.3.8 L2CAP Credit Based Connection Response on Unsupported SPSM**

- Test Purpose

Verify that an IUT receiving L2CAP_CREDIT_BASED_CONNECTION_REQ on an unsupported SPSM responds with L2CAP_CREDIT_BASED_CONNECTION_RSP refusing the connection.

- Initial Condition

- The signaling channel specified in Table 4.62 is used.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **312 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**Result**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-22-C [L2CAP<br>LE Credit Based Connection<br>Response on Unsupported<br>SPSM]|[13]4.23|0x0005|0x0002 – Connection<br>refused – SPSM not<br>supported|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-28-C [L2CAP<br>Credit Based Connection<br>Response on Unsupported<br>SPSM, LE]|[13]4.26|0x0005|0x0002 – All<br>connections refused –<br>SPSM not supported|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-72-C [L2CAP<br>Credit Based Connection<br>Response on Unsupported<br>SPSM, BR/EDR]|[13]4.26|0x0001|0x0002 – All<br>connections refused –<br>SPSM not supported|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.62: L2CAP Credit Based Connection Response on Unsupported SPSM test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **313 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

The L2CAP Credit Based Connection Request/Response commands are specified in Table 4.62.

**==> picture [378 x 178] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>L2CAP(SPSM = Unsupported)_[ CREDIT_BASED_CONNECTION_REQ<br>L2CAP_[ CREDIT_BASED_CONNE(Result = 0x0002)CTION_RSP<br>**----- End of picture text -----**<br>

_Figure 4.234: L2CAP Credit Based Connection Response on Unsupported SPSM MSC_

1. The Lower Tester sends a connection request command on an unsupported SPSM.

2. The IUT responds with a connection request response, with the Result in Table 4.62.

-

- Expected Outcome

## Pass verdict

Upon receiving a connection request command containing an unsupported SPSM, the IUT sends a correctly formatted connection request response to the Lower Tester with the Result in Table 4.62.

- **4.15.3.9 Disconnect Request – DCID not recognized**

- Test Purpose

Verify that an IUT receiving Disconnect Request from the Lower Tester for which DCID is not recognized by the IUT responds L2CAP_COMMAND_REJECT_RSP with an “invalid CID” result code.

- Reference

- [13] 4.1, 4.6

-

- Initial Condition

- The signaling channel specified in Table 4.63 is used.

- An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value using the commands specified in Table 4.63.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **314 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-23-C[Disconnect Request – DCID not recognized]|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-30-C[Disconnection Response, LE]|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-73-C[Disconnection Response, BR/EDR]|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.63: Disconnect Request – DCID not recognized test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **315 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [378 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP channel established between the IUT and the Lower Tester<br>L2CAP_DISCONNECTION_REQ<br>(Code = 0x06)<br>L2CAP_COMMAND_REJECT_RSP<br>(Code = 0x01, Reason = 0x0002)<br>**----- End of picture text -----**<br>

_Figure 4.235: Disconnect Request – DCID not recognized MSC_

1. The Lower Tester sends an L2CAP_DISCONNECTION_REQ (Code = 0x06) to the IUT on the PSM as specified in Table 4.63, with a DCID not recognized by the IUT.

2. The IUT sends an L2CAP_COMMAND_REJECT_RSP packet (Code = 0x01) to the Lower Tester, with Reason “0x0002 – Invalid CID in request”.

-

- Expected Outcome

## Pass verdict

The IUT responds to the request to disconnect the channel with a correctly formatted L2CAP_COMMAND_REJECT_RSP message.

- **4.15.3.10 Security – Insufficient Encryption – Initiator**

- Test Purpose

Verify that the IUT does not establish any channel upon receipt of an

L2CAP_CREDIT_BASED_CONNECTION_RSP indicating that the connections were refused with Result 0x0008 (“All connections refused – insufficient encryption”).

- Initial Condition

- The signaling channel specified in Table 4.64 is used.

- Either an LTK or STK exists between the IUT and the Lower Tester, but encryption is not enabled.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **316 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**Result**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-24-C<br>[Security – Insufficient Encryption<br>– Initiator]|[13]4.22|0x0005|0x0008 (“Connection<br>refused – insufficient<br>encryption”)|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-31-C [Security<br>– Insufficient Encryption –<br>Initiator, LE]|[13]4.25|0x0005|0x0008 (“All<br>connections refused –<br>insufficient encryption”)|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.64: Security – Insufficient Encryption – Initiator test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **317 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

The L2CAP Credit Based Connection Request/Response commands are specified in Table 4.64.

**==> picture [378 x 171] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower IUT Upper<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>Create L2CAP Credit Based Channel<br>(SPSM)<br>L2CAP_[ CREDIT_BASED_CONNECTION_REQ<br>(SPSM, SCID, MTU, MPS<br>Initial Credits)<br>L2CAP( Result = 0x0008)_[ CREDIT_BASED_CONNECTION_RSP<br>Create L2CAP Credit Based Channel Response<br>(result)<br>**----- End of picture text -----**<br>

_Figure 4.236: Security – Insufficient Encryption – Initiator MSC_

1. The Upper Tester commands the IUT to send a connection request on an SPSM as specified in Table 4.64.

2. The IUT sends an L2CAP_CREDIT_BASED_CONNECTION_REQ for the specified SPSM.

3. The Lower Tester sends an L2CAP_CREDIT_BASED_CONNECTION_RSP with Result 0x0008 (Table 4.64), refusing the channel creation request.

-

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

## **4.15.3.11 Security – Insufficient Encryption – Responder**

- Test Purpose

Verify that an IUT refuses to create any connection upon reception of an

L2CAP_CREDIT_BASED_CONNECTION_REQ that fails to satisfy encryption requirements.

- Initial Condition

- The signaling channel specified in Table 4.65 is used.

- Either an LTK or STK exists between the IUT and the Lower Tester, but encryption is not enabled.

- An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX_psm_encryption_required IXIT value.

- Encryption requirement exists for the SPSM in use.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **318 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Reference**|**Signaling**<br>**Channel**|**Result**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-25-C<br>[Security – Insufficient Encryption<br>– Responder]|[13]4.22|0x0005|0x0008 (“Connection<br>refused – insufficient<br>encryption”)|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-32-C [Security<br>– Insufficient Encryption –<br>Responder, LE]|[13]4.25|0x0005|0x0008 (“All<br>connections refused –<br>insufficient encryption”)|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.65: Security – Insufficient Encryption – Responder test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **319 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

The L2CAP Credit Based Connection Request/Response commands for the test are specified in Table 4.65.

**==> picture [377 x 173] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>An L2CAP fixed channel is established between IUT and Lower Tester<br>L2CAP_[ CREDIT_BASED_CONNECTION_REQ<br>(SPSM, SCID, MTU, MPS, Initial Credits)<br>L2CAP_[ CREDIT_BASED_CONNECTION_RSP<br>(Result = 0x0008)<br>**----- End of picture text -----**<br>

_Figure 4.237: Security – Insufficient Encryption – Responder MSC_

1. The Lower Tester sends an L2CAP_CREDIT_BASED_CONNECTION_REQ to the IUT for the specified SPSM.

2. The IUT sends an L2CAP_CREDIT_BASED_CONNECTION_RSP to the Lower Tester with Result 0x0008 (Table 4.65), refusing the channel creation request.

-

- Expected Outcome

## Pass verdict

Upon reception of an L2CAP_CREDIT_BASED_CONNECTION_REQ from the Lower Tester that fails to satisfy the authentication requirements, the IUT sends a correctly formatted L2CAP_CREDIT_BASED_CONNECTION_RSP with Result 0x0008 (Table 4.65) to the Lower Tester.

- **4.15.3.12 K-frame – SDU length greater than MTU of IUT**

- Test Purpose

Verify that an IUT receiving a K-frame from the Lower Tester with ‘L2CAP SDU Length’ field set to a value greater than the MTU of the IUT on L2CAP Credit Based Channel sends an L2CAP Disconnect Request for that channel.

- Reference

- [13] 3.4.3

- Initial Condition

- The signaling channel specified in Table 4.66 is used.

- A Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value using the commands specified in Table 4.66.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **320 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-26-C [K-frame – SDU length greater than<br>MTU of IUT]|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-33-C [K-frame – SDU length greater than MTU<br>of IUT, LE]|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-76-C [K-frame – SDU length greater than MTU<br>of IUT, BR/EDR]|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.66: K-frame - SDU length greater than MTU of IUT – test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **321 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [376 x 154] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>An L2CAP channel over relevant bearer has<br>been established between the IUT and the Lower Tester<br>Data (K-frame)<br>(L2CAP SDU Length > MTU)<br>L2CAP_DISCONNECTION_REQ<br>(Code = 0x06)<br>**----- End of picture text -----**<br>

_Figure 4.238: K-frame - SDU length greater than MTU of IUT MSC_

1. The Lower Tester sends a K-frame to the IUT with ‘L2CAP SDU Length’ field set to a value greater than the MTU of the IUT on L2CAP Credit Based Channel.

-

- Expected Outcome

## Pass verdict

The IUT terminates the channel and sends a correctly formatted L2CAP_DISCONNECT_REQ PDU (Code = 0x06) to the Lower Tester.

- **4.15.3.13 K-frame – Information Payload length greater than MPS of IUT**

- Test Purpose

Verify that an IUT receiving a K-frame from the Lower Tester with the length of ‘Information Payload’ field greater than the MPS of the IUT on L2CAP Credit Based Channel sends an L2CAP Disconnect Request for that channel.

- Reference

- [13] 3.4.3

- Initial Condition

- The signaling channel specified in Table 4.67 is used.

- A Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value using the commands specified in Table 4.67.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **322 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-27-C [K-frame – Information Payload length greater<br>than MPS of IUT]|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-34-C [K-frame – Information Payload length greater than<br>MPS of IUT, LE]|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-77-C [K-frame – Information Payload length greater than<br>MPS of IUT, BR/EDR]|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.67: K-frame – Information Payload length greater than MPS of IUT test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **323 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [377 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>An L2CAP channel over relevant bearer has<br>been established between the IUT and the Lower Tester<br>Data (K-frame)<br>(L2CAP SDU Length > MPS)<br>L2CAP_DISCONNECTION_REQ<br>(Code = 0x06)<br>**----- End of picture text -----**<br>

_Figure 4.239: K-frame – Information Payload length greater than MPS of IUT MSC_

1. The Lower Tester sends a K-frame to the IUT with the length of ‘Information Payload’ field greater than the MPS of the IUT on L2CAP Credit Based Channel.

- Expected Outcome

## Pass verdict

The IUT terminates the channel and sends a correctly formatted L2CAP_DISCONNECT_REQ PDU (Code = 0x06) to the Lower Tester.

## **4.15.3.14 Total length of segments greater than SDU length specified in first K-frame**

- Test Purpose

Verify that an IUT receiving segmented K-frames from the Lower Tester on L2CAP Credit Based Channel with total length of the segmented payloads greater than ‘L2CAP SDU Length’ field specified in the first K-frame sends an L2CAP Disconnect Request for that channel.

- Reference

- [13] 3.4.3

- Initial Condition

- The signaling channel specified in Table 4.68 is used.

- A Data Channel is established on the SPSM declared via the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **324 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case ID**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-28-C [Total length of segments greater than SDU<br>length specified in first K-frame]|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-35-C [Total length of segments greater than SDU length<br>specified in first K-frame, LE]|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-78-C [Total length of segments greater than SDU length<br>specified in first K-frame, BR/EDR]|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.68: Total length of segments greater than SDU length specified in first K-frame test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **325 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

Same as for L2CAP/COS/CFC/BV-03-C [Reassembling], but in the last segment, the Lower Tester sends an Information Payload longer (at least one byte) than the correct size, such that the total length of segmented payloads is greater than ‘L2CAP SDU Length’ field specified in first K-frame.

- Expected Outcome

## Pass verdict

The IUT terminates the channel and sends a correctly formatted L2CAP_DISCONNECT_REQ PDU (Code = 0x06) to the Lower Tester.

## **4.15.3.15 K-frame – SDU length = MPS**

- Test Purpose

Verify that an IUT does not disconnect the peer when the payload size does not exceed the MPS. Verify that the IUT does not use the SDU Length 2 octets into calculating the payload size.

- Reference

- [13] 3.4.3

- Initial Condition

- The SPSM for the control channel is declared by the TSPX_spsm IXIT value.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **326 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Case Configuration

|**Test Case ID**|**Signaling**<br>**Channel**|**L2CAP Command**|
|L2CAP/LE/CFC/BV-32-C[K-frame – SDU length = MPS]|0x0005|L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-80-C[K-frame – SDU length = MPS, LE]|0x0005|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|
|L2CAP/ECFC/BV-81-C[K-frame – SDU length = MPS, BR/EDR]|0x0001|L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP|

_Table 4.69: K-frame – SDU length = MPS test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **327 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Procedure

**==> picture [394 x 214] intentionally omitted <==**

_Figure 4.240: K-frame – SDU length = MPS MSC_

1. The Upper Tester commands the IUT to create an L2CAP channel using the SPSM set to TSPX_spsm.

2. The IUT sends the L2CAP command request specified in Table 4.69 to the Lower Tester on the SPSM from Step 1. The Lower Tester stores the MTU and MPS.

3. The Lower Tester sends the L2CAP command response specified in Table 4.69 to the IUT.

4. Perform alternative 4A or 4B depending on the MTU sent in Step 2: ALT 4A: The MTU in Step 2 is greater than or equal to the MPS in Step 2 – 1.

- 4A.1 Repeat Step 4 for all rounds in Table 4.704.71.

- 4A.2 The Lower Tester sends a K-frame to the IUT with the ‘L2CAP SDU Length’ field set to the value in Table 4.704.71 with a random payload.

- ALT 4B: The MTU in Step 2 is less than the MPS in Step 2 – 1:

- 4B.1 The L2CAP channel is created using MTU less than MPS – 1.

|**Round**|**SDU Length**|
|1|MPS|
|2|MPS – 1|
|3|MPS + 1|
|4|MPS x 2|
|5|MPS x 2 + 1|
|6|MTU|

_Table 4.704.71: K-frame – SDU length = MPS rounds_

- Expected Outcome

## Pass verdict

In Step 4, the IUT does not disconnect the channel created in Step 1.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **328 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **4.16 Generic Attribute Timing tests**

Check that the IUT respects the GATT timings.

## **4.16.1 Back-off on Connection Request Collision**

- Test Purpose

Verify that an IUT in a Peripheral role that initiates an L2CAP connection request and encounters a collision uses an appropriate back-off timer before initiating a retry.

- Reference

[13] 4.3, 4.26

[14] 5.3.2, 5.4

- Initial Condition

- The IUT acts in the Peripheral role.

- For EATT, an encrypted ACL link between the IUT and the Lower Tester is established.

- An L2CAP channel over the transport with the PSM/SPSM is set up as specified in Table 4.72.

- For the tests in Table 4.72 that use EATT as the bearer, the following also apply:

- The Server Supported Features characteristic is present and states that it supports Enhanced ATT bearers, on both the IUT and Lower Tester sides.

- (TSPX_iut_supported_max_channels – 1) LE or BR/EDR Data Channels are established on the EATT SPSM (the maximum number of EATT supported channels declared in the IXIT, minus 1).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **329 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## • Test Case Configuration

|**Test Case**|**Transport**|**Code**|**PSM/**<br>**SPSM**|**Min Back-off**|
|L2CAP/TIM/BV-01-C [Back-off on<br>Connection Request Collision,<br>BR/EDR, Dynamic]|BR/EDR|0x02|ATT|100 ms|
|L2CAP/TIM/BV-02-C [Back-off on<br>Connection Request Collision,<br>BR/EDR, EATT]|BR/EDR|0x17|EATT|100 ms|
|L2CAP/TIM/BV-03-C [Back-off on<br>Connection Request Collision,<br>LE, EATT]|LE|0x17|EATT|Max(100 ms, 2 × (_connPeripheralLatency_+ 1) ×_connInterval_)|

_Table 4.72: Back-off on Connection Request Collision test cases_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **330 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

- Test Procedure

**==> picture [376 x 345] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Upper<br>IUT<br>Tester Tester<br>Optional<br>One or more L2CAP channels on the relevant PSM have been established<br>between the IUT and the Lower Tester<br>Establish Connection<br>L2CAP_[...]Connection_Req<br>L2CAP_[...]Connection_Req<br>L2CAP_[...]Connection_Rsp<br>(Result = 0x0004)<br>L2CAP_[...]Connection_Rsp<br>(Result = 0x0004)<br>L2CAP_[...]Connection_Req<br>L2CAP_[...]Connection_Rsp<br>(Result = 0)<br>An L2CAP channel is established between the IUT and the Lower Tester<br>**----- End of picture text -----**<br>

_Figure 4.241: Back-off on Connection Request Collision MSC_

1. The Upper Tester commands the IUT to establish a connection to the Lower Tester.

2. The IUT sends an L2CAP Connection Request packet to the Lower Tester, in order to establish an L2CAP channel.

3. The Lower Tester sends an L2CAP Connection Request packet to the IUT (code as specified in Table 4.72).

4. The IUT sends the Lower Tester the response corresponding to the request sent in Step 3 with Result = 0x0004.

5. The Lower Tester sends the IUT the response corresponding to the request sent in Step 2 with Result = 0x0004.

6. The IUT waits for at least the time specified in Table 4.72. The Lower Tester does not send any packet during this time.

7. The IUT sends an L2CAP Connection Request packet to the Lower Tester, to establish an L2CAP channel.

8. The Lower Tester accepts the request, creates an L2CAP channel of the type described in Table 4.72, and responds with an L2CAP Connection Response packet with Result = 0x0000.

- Expected Outcome

## Pass verdict

The IUT sends the L2CAP Connection Request to the Lower Tester, in Step 8, after at least the time listed in Table 4.72.

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **331 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## Fail verdict

In Step 4, the IUT accepts the connection request from the Lower Tester and creates an L2CAP channel of the type described in Table 4.72.

- Note

The L2CAP packets exchanged between the IUT and the Lower Tester are of the type corresponding to the transport and bearer in Table 4.72 (L2CAP_CONNECTION_REQ /

L2CAP_CONNECTION_RSP and, respectively, L2CAP_CREDIT_BASED_CONNECTION_REQ / L2CAP_CREDIT_BASED_CONNECTION_RSP).

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **332 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **5 Test case ma in pp g**

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.

The columns for the TCMT are defined as follows:

**Item:** Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for L2CAP [5].

If a test case is mandatory within the respective layer, then the y/x reference is omitted.

**Feature:** A brief, informal description of the feature being tested.

**Test Case(s):** The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [10].

For the purpose and structure of the ICS/IXIT, refer to [10].

|**Item**|**Feature**|**Test Case(s)**|
|**General Operation**|||
|L2CAP 2/1|Signaling channel|L2CAP/COS/CED/BV-07-C<br>L2CAP/COS/CED/BV-08-C<br>L2CAP/COS/CED/BV-09-C<br>L2CAP/EXF/BV-08-C<br>L2CAP/FIX/BV-03-C|
|L2CAP 2/1 AND<br>L2CAP 2/41|Reject Unknown Command – BR/EDR|L2CAP/COS/CED/BI-01-C|
|L2CAP 2/2|Configuration process|L2CAP/COS/CFD/BV-01-C<br>L2CAP/COS/CFD/BV-02-C<br>L2CAP/COS/CFD/BV-03-C<br>L2CAP/COS/CFD/BV-11-C<br>L2CAP/COS/CFD/BV-12-C<br>L2CAP/COS/CFD/BV-14-C|
|L2CAP 1/1 AND<br>L2CAP 2/2|Configuration process – Initiator|L2CAP/COS/CFD/BV-08-C|
|L2CAP 2/3|Connection-oriented data channel|L2CAP/COS/CED/BV-03-C<br>L2CAP/COS/CED/BI-04-C<br>L2CAP/COS/CED/BI-06-C<br>L2CAP/COS/CED/BI-07-C<br>L2CAP/COS/CED/BI-08-C<br>L2CAP/COS/CED/BI-10-C<br>L2CAP/COS/CED/BI-12-C<br>L2CAP/COS/CED/BI-14-C<br>L2CAP/COS/CED/BI-15-C<br>L2CAP/COS/CED/BI-28-C|
|L2CAP 2/3 AND<br>L2CAP 0a/1|Connection-oriented data channel, BR/EDR|L2CAP/COS/CED/BI-03-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **333 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 2/45|Send Disconnect Request|L2CAP/COS/CED/BV-04-C|
|L2CAP 2/4|Command echo request|L2CAP/COS/ECH/BV-02-C|
|L2CAP 2/5|Echo response|L2CAP/COS/ECH/BV-01-C|
|L2CAP 2/6|Command information request|L2CAP/COS/IEX/BV-01-C|
|L2CAP 2/7|Information response|L2CAP/COS/IEX/BV-02-C<br>L2CAP/EXF/BV-07-C|
|L2CAP 2/9|Connectionless data channel|L2CAP/CLS/CLR/BV-01-C|
|L2CAP 2/10|Retransmission Mode|L2CAP/COS/CFD/BV-10-C<br>L2CAP/COS/RTX/BV-01-C<br>L2CAP/COS/RTX/BV-02-C<br>L2CAP/COS/RTX/BV-03-C|
|L2CAP 2/11|Flow Control Mode|L2CAP/COS/CED/BV-10-C<br>L2CAP/COS/FLC/BV-01-C<br>L2CAP/COS/FLC/BV-02-C<br>L2CAP/COS/FLC/BV-03-C<br>L2CAP/COS/FLC/BV-04-C<br>L2CAP/COS/CFD/BV-13-C|
|L2CAP 2/12|Enhanced Retransmission Mode|L2CAP/CMC/BV-01-C<br>L2CAP/CMC/BV-02-C<br>L2CAP/ERM/BV-01-C<br>L2CAP/ERM/BV-02-C<br>L2CAP/ERM/BV-03-C<br>L2CAP/ERM/BV-08-C<br>L2CAP/ERM/BV-09-C<br>L2CAP/ERM/BV-10-C<br>L2CAP/ERM/BV-11-C<br>L2CAP/ERM/BV-12-C<br>L2CAP/ERM/BV-18-C<br>L2CAP/ERM/BV-19-C<br>L2CAP/ERM/BV-20-C|
|L2CAP 2/13|Streaming Mode|L2CAP/CMC/BV-04-C<br>L2CAP/CMC/BV-05-C<br>L2CAP/STM/BV-01-C<br>L2CAP/STM/BV-02-C|
|L2CAP 2/13 AND<br>L2CAP 2/33 AND<br>L2CAP 2/44|Streaming Mode, STM source over AMP|L2CAP/STM/BV-11-C|
|L2CAP 2/13 AND<br>L2CAP 2/23 AND<br>L2CAP 2/34 AND<br>L2CAP 2/44|Streaming Mode, Send data using SAR. STM<br>sink over AMP|L2CAP/STM/BV-12-C|
|L2CAP 2/13 AND<br>L2CAP 2/23 AND<br>L2CAP 2/33 AND<br>L2CAP 2/44|Streaming Mode, Send data using SAR. STM<br>source over AMP|L2CAP/STM/BV-13-C|
|L2CAP 2/14a|Don’t send FCS Option|L2CAP/FOC/BV-06-C<br>L2CAP/FOC/BV-08-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **334 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 2/14b|Send FCS Option 0x00|L2CAP/FOC/BV-01-C<br>L2CAP/FOC/BV-02-C<br>L2CAP/FOC/BV-03-C<br>L2CAP/FOC/BV-05-C|
|L2CAP 2/14c|Send FCS Option 0x01|L2CAP/FOC/BV-04-C<br>L2CAP/FOC/BV-07-C|
|L2CAP 2/12 AND<br>(L2CAP 2/14a OR<br>L2CAP 2/14c)|ERTM with FCS Option, with FCS|L2CAP/OFS/BV-05-C<br>L2CAP/OFS/BV-06-C|
|L2CAP 2/12 AND<br>L2CAP 2/14b|ERTM with FCS Option, no FCS|L2CAP/OFS/BV-01-C<br>L2CAP/OFS/BV-02-C|
|L2CAP 2/13 AND<br>(L2CAP 2/14a OR<br>L2CAP 2/14c)|Streaming with FCS Option, with FCS|L2CAP/OFS/BV-07-C<br>L2CAP/OFS/BV-08-C|
|L2CAP 2/13 AND<br>L2CAP 2/14b|ERTM with FCS Option, no FCS|L2CAP/OFS/BV-03-C<br>L2CAP/OFS/BV-04-C|
|L2CAP 2/15|Can Generate Local Busy Condition|L2CAP/ERM/BV-07-C<br>L2CAP/ERM/BV-22-C|
|L2CAP 2/16|Can Send Reject|L2CAP/ERM/BV-16-C<br>L2CAP/ERM/BI-01-C|
|L2CAP 2/17|Can Send Selective Reject|L2CAP/ERM/BV-17-C<br>L2CAP/ERM/BI-02-C|
|L2CAP 2/18|Supports mandatory use of ERTM|L2CAP/CMC/BI-01-C<br>L2CAP/CMC/BI-02-C<br>L2CAP/CMC/BV-12-C|
|L2CAP 2/19|Supports mandatory use of Streaming Mode|L2CAP/CMC/BI-03-C<br>L2CAP/CMC/BI-04-C<br>L2CAP/CMC/BV-13-C|
|L2CAP 2/20|Supports optional use of ERTM|L2CAP/CMC/BV-03-C<br>L2CAP/CMC/BV-07-C<br>L2CAP/CMC/BV-10-C|
|L2CAP 2/21|Supports optional use of Streaming Mode|L2CAP/CMC/BV-06-C<br>L2CAP/CMC/BV-08-C<br>L2CAP/CMC/BV-11-C|
|L2CAP 2/22|Can send data usingSAR in ERTM|L2CAP/ERM/BV-23-C|
|L2CAP 2/23|Can send data usingSAR in StreamingMode|L2CAP/STM/BV-03-C|
|L2CAP 2/24|Can actively request Basic Mode for a PSM<br>that supports the use of ERTM or Streaming<br>Mode|L2CAP/CMC/BV-09-C<br>L2CAP/CMC/BI-05-C<br>L2CAP/CMC/BI-06-C|
|L2CAP 2/25|Supports performing L2CAP channel mode<br>configuration fallback from STM to ERTM|L2CAP/CMC/BV-14-C<br>L2CAP/CMC/BV-15-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **335 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 2/26|Supports sending more than one<br>unacknowledged I-frame when operating in<br>ERTM|L2CAP/ERM/BV-05-C<br>L2CAP/ERM/BV-06-C<br>L2CAP/ERM/BV-13-C<br>L2CAP/ERM/BI-03-C<br>L2CAP/ERM/BI-04-C<br>L2CAP/ERM/BI-05-C|
|L2CAP 2/27|Supports sending more than three<br>unacknowledged I-frames when operating in<br>ERTM|L2CAP/ERM/BV-14-C<br>L2CAP/ERM/BV-15-C|
|L2CAP 2/38 AND<br>L2CAP 3/14|Extended Flow Specification for ERTM over<br>BR/EDR|L2CAP/LSC/BV-01-C<br>L2CAP/LSC/BV-03-C<br>L2CAP/LSC/BI-04-C|
|L2CAP 2/38 AND<br>L2CAP 3/15|Extended Flow Specification for STM over<br>BR/EDR|L2CAP/LSC/BV-02-C<br>L2CAP/LSC/BI-05-C<br>L2CAP/LSC/BV-06-C|
|L2CAP 2/39|Extended Window Size|L2CAP/EWC/BV-01-C<br>L2CAP/EWC/BV-02-C<br>L2CAP/EWC/BV-03-C|
|L2CAP 2/12 AND<br>L2CAP 2/39|ERTM, EWS and Extended Control Field|L2CAP/ECF/BV-01-C<br>L2CAP/ECF/BV-02-C<br>L2CAP/ECF/BV-03-C<br>L2CAP/ECF/BV-04-C<br>L2CAP/ECF/BV-05-C<br>L2CAP/ECF/BV-06-C<br>L2CAP/ECF/BV-07-C<br>L2CAP/ECF/BV-08-C|
|**Configurable Parameters**|||
|L2CAP 3/3 AND<br>L2CAP 1/1|MTU size 48 bytes, Initiator|L2CAP/COS/CFD/BV-09-C<br>L2CAP/COS/CED/BV-01-C|
|L2CAP 3/3 AND<br>L2CAP 1/2|MTU size 48 bytes, Acceptor|L2CAP/COS/CED/BV-12-C|
|L2CAP 3/4|MTU size larger than 48 bytes|L2CAP/COS/CED/BV-11-C|
|**Credit Based Flow Control channels**|||
|L2CAP 2/40|Reject Invalid Command Length, LE|L2CAP/COS/CED/BI-11-C|
|L2CAP 2/40 AND<br>L2CAP 2/46|Reject Invalid Command Length, LE Credit<br>Based Flow Control Mode|L2CAP/COS/CED/BI-05-C<br>L2CAP/COS/CED/BI-09-C<br>L2CAP/COS/CED/BI-13-C<br>L2CAP/COS/CED/BI-16-C<br>L2CAP/COS/CED/BI-17-C<br>L2CAP/COS/CED/BI-29-C|
|L2CAP 2/40 AND<br>L2CAP 2/48b AND<br>NOT L2CAP 2/46|Reject Invalid Command Length, Enhanced<br>Credit Based Flow Control Mode – LE|L2CAP/COS/CED/BI-18-C<br>L2CAP/COS/CED/BI-20-C<br>L2CAP/COS/CED/BI-22-C<br>L2CAP/COS/CED/BI-24-C<br>L2CAP/COS/CED/BI-25-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **336 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 2/40 AND<br>NOT (L2CAP 2/46<br>OR L2CAP 2/48b)|Reject Invalid Command Length, LE Credit<br>Based Flow Control and Enhanced Credit<br>Based Flow Control modes not supported –<br>LE|L2CAP/COS/CED/BI-19-C<br>L2CAP/COS/CED/BI-21-C<br>L2CAP/COS/CED/BI-23-C|
|**AMP Parameters**|||
|L2CAP 2/32 AND<br>L2CAP 2/44 AND<br>L2CAP 3/14|ERTM over AMP with Extended Flow<br>Specification – service type “Best Effort”|L2CAP/LSC/BV-07-C<br>L2CAP/LSC/BV-09-C<br>L2CAP/LSC/BI-10-C|
|L2CAP 2/32 AND<br>L2CAP 2/44 AND<br>L2CAP 3/15|ERTM over AMP with Extended Flow<br>Specification – service type “Guaranteed”|L2CAP/LSC/BI-11-C|
|L2CAP 2/33 AND<br>L2CAP 2/34 AND<br>L2CAP 2/44 AND<br>L2CAP 3/15|Streaming Mode over AMP with Extended<br>Flow Specification – service type<br>“Guaranteed”|L2CAP/LSC/BV-08-C|
|L2CAP 2/33 AND<br>L2CAP 2/44 AND<br>L2CAP 3/15|Streaming Mode over AMP with Extended<br>Flow Specification – service type<br>“Guaranteed”|L2CAP/LSC/BV-12-C|
|L2CAP 2/30|Fixed Channel Support|L2CAP/FIX/BV-01-C|
|L2CAP 2/30 AND<br>L2CAP 2/31|Fixed Channel and AMP Manager Support|L2CAP/FIX/BV-02-C|
|L2CAP 2/31 AND<br>L2CAP 2/38|AMP Manager and Extended Flow<br>Specification Support|L2CAP/CCH/BV-01-C<br>L2CAP/CCH/BV-02-C<br>L2CAP/CCH/BV-03-C<br>L2CAP/CCH/BV-04-C|
|L2CAP 2/32|ERTM over AMP|L2CAP/MCH/BV-01-C<br>L2CAP/MCH/BV-02-C<br>L2CAP/MCH/BV-03-C<br>L2CAP/MCH/BV-04-C<br>L2CAP/MCH/BV-05-C<br>L2CAP/MCH/BV-06-C<br>L2CAP/MCH/BV-07-C<br>L2CAP/MCH/BV-08-C<br>L2CAP/MCH/BV-09-C<br>L2CAP/MCH/BV-10-C<br>L2CAP/MCH/BV-11-C<br>L2CAP/MCH/BV-14-C|
|L2CAP 2/33|Streaming Mode Source over AMP Support|L2CAP/MCH/BV-15-C<br>L2CAP/MCH/BV-17-C<br>L2CAP/MCH/BV-19-C<br>L2CAP/MCH/BV-21-C<br>L2CAP/MCH/BV-23-C<br>L2CAP/MCH/BV-27-C<br>L2CAP/MCH/BV-29-C<br>L2CAP/MCH/BV-31-C<br>L2CAP/MCH/BV-33-C<br>L2CAP/MCH/BV-35-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **337 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 2/34|Streaming Mode Sink over AMP Support|L2CAP/MCH/BV-16-C<br>L2CAP/MCH/BV-18-C<br>L2CAP/MCH/BV-20-C<br>L2CAP/MCH/BV-22-C<br>L2CAP/MCH/BV-24-C<br>L2CAP/MCH/BV-28-C<br>L2CAP/MCH/BV-30-C<br>L2CAP/MCH/BV-32-C<br>L2CAP/MCH/BV-34-C<br>L2CAP/MCH/BV-36-C|
|L2CAP 2/38 AND<br>L2CAP 2/31||L2CAP/MCH/BV-12-C<br>L2CAP/MCH/BV-13-C<br>L2CAP/MCH/BV-25-C<br>L2CAP/MCH/BV-26-C|
|**UCD Parameters**|||
|L2CAP 2/35|Unicast connectionless data reception|L2CAP/CLS/UCD/BV-01-C<br>L2CAP/CLS/CID/BV-01-C|
|L2CAP 2/36|Transmission of unencrypted unicast<br>connectionless data|L2CAP/CLS/UCD/BV-02-C|
|L2CAP 2/37|Transmission of encrypted unicast<br>connectionless data|L2CAP/CLS/UCD/BV-03-C|
|**Low Energy Operation**|||
|L2CAP 2/42|Support of Connection Parameter Update<br>Request|L2CAP/LE/CPU/BV-01-C<br>L2CAP/LE/CPU/BI-02-C|
|L2CAP 2/43|Support of Connection parameter update<br>Response|L2CAP/LE/CPU/BV-02-C<br>L2CAP/LE/CPU/BI-01-C|
|**Credit Based Flow Control channels**|||
|L2CAP 1/5 AND<br>L2CAP 2/46|LE Credit Based Flow Control Channel<br>Initiator|L2CAP/LE/CFC/BV-01-C<br>L2CAP/LE/CFC/BV-02-C<br>L2CAP/LE/CFC/BV-04-C<br>L2CAP/LE/CFC/BV-16-C<br>L2CAP/LE/CFC/BV-18-C<br>L2CAP/LE/CFC/BV-21-C<br>L2CAP/LE/CFC/BV-22-C<br>L2CAP/LE/CFC/BV-24-C<br>L2CAP/LE/CFC/BV-29-C|
|L2CAP 1/6 AND<br>L2CAP 2/46|LE Credit Based Flow Control Channel<br>Responder|L2CAP/LE/CFC/BV-03-C<br>L2CAP/LE/CFC/BV-05-C<br>L2CAP/LE/CFC/BV-25-C<br>L2CAP/LE/CFC/BV-30-C|
|L2CAP 2/40 AND<br>L2CAP 2/41|Reject Unknown Command – LE|L2CAP/LE/REJ/BI-02-C|
|L2CAP 1/5 AND<br>L2CAP 2/46 AND<br>L2CAP 4/1|LE Credit Based Flow Control Channel<br>Initiator with Authentication|L2CAP/LE/CFC/BV-10-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **338 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 1/5 AND<br>L2CAP 2/46 AND<br>L2CAP 4/2|LE Credit Based Flow Control Channel<br>Initiator with Authorization|L2CAP/LE/CFC/BV-12-C|
|L2CAP 1/5 AND<br>L2CAP 2/46 AND<br>L2CAP 4/3|LE Credit Based Flow Control Channel<br>Initiator with Encryption|L2CAP/LE/CFC/BV-14-C|
|L2CAP 1/6 AND<br>L2CAP 2/46 AND<br>L2CAP 4/1|LE Credit Based Flow Control Channel<br>Responder with Authentication|L2CAP/LE/CFC/BV-11-C|
|L2CAP 1/6 AND<br>L2CAP 2/46 AND<br>L2CAP 4/2|LE Credit Based Flow Control Channel<br>Responder with Authorization|L2CAP/LE/CFC/BV-13-C|
|L2CAP 1/6 AND<br>L2CAP 2/46 AND<br>L2CAP 4/3|LE Credit Based Flow Control Channel<br>Responder with Encryption|L2CAP/LE/CFC/BV-15-C|
|L2CAP 2/46|LE Credit Based Flow Control Channel - Data|L2CAP/COS/CFC/BV-01-C<br>L2CAP/COS/CFC/BV-02-C<br>L2CAP/COS/CFC/BV-03-C<br>L2CAP/COS/CFC/BV-04-C<br>L2CAP/LE/CFC/BV-06-C<br>L2CAP/LE/CFC/BV-07-C<br>L2CAP/LE/CFC/BI-01-C<br>L2CAP/LE/CFC/BV-09-C<br>L2CAP/LE/CFC/BV-23-C<br>L2CAP/LE/CFC/BV-26-C<br>L2CAP/LE/CFC/BV-27-C<br>L2CAP/LE/CFC/BV-28-C<br>L2CAP/LE/CFC/BV-31-C<br>L2CAP/LE/CFC/BV-32-C|
|L2CAP 2/46 AND<br>L2CAP 2/45a|LE Credit Based Flow Control Channel –<br>Send Disconnect|L2CAP/LE/CFC/BV-08-C|
|L2CAP 1/6 AND NOT<br>L2CAP 3/16|Multiple Simultaneous LE Credit Based Flow<br>Control Channels - Reject|L2CAP/LE/CFC/BV-17-C|
|L2CAP 3/16|Multiple Simultaneous LE Credit Based Flow<br>Control Channels|L2CAP/COS/CFC/BV-05-C|
|L2CAP 1/5 AND<br>L2CAP 3/16|Connection Request refused due to source<br>CID alreadyallocated - Initiator|L2CAP/LE/CFC/BV-19-C|
|L2CAP 1/6 AND<br>L2CAP 3/16|Connection Request refused due to source<br>CID alreadyallocated - Responder|L2CAP/LE/CFC/BV-20-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **339 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 1/5 AND<br>L2CAP 2/48b|Enhanced Credit Based Flow Control Channel<br>Initiator, LE|L2CAP/ECFC/BV-01-C<br>L2CAP/ECFC/BV-02-C<br>L2CAP/ECFC/BV-04-C<br>L2CAP/ECFC/BV-16-C<br>L2CAP/ECFC/BV-18-C<br>L2CAP/ECFC/BV-19-C<br>L2CAP/ECFC/BV-21-C<br>L2CAP/ECFC/BV-22-C<br>L2CAP/ECFC/BV-24-C<br>L2CAP/ECFC/BV-28-C<br>L2CAP/ECFC/BV-31-C<br>L2CAP/ECFC/BV-38-C|
|L2CAP 1/1 AND<br>L2CAP 2/48a|Enhanced Credit Based Flow Control Channel<br>Initiator, BR/EDR|L2CAP/ECFC/BV-45-C<br>L2CAP/ECFC/BV-46-C<br>L2CAP/ECFC/BV-48-C<br>L2CAP/ECFC/BV-52-C<br>L2CAP/ECFC/BV-54-C<br>L2CAP/ECFC/BV-55-C<br>L2CAP/ECFC/BV-57-C<br>L2CAP/ECFC/BV-58-C<br>L2CAP/ECFC/BV-60-C<br>L2CAP/ECFC/BV-71-C<br>L2CAP/ECFC/BV-72-C<br>L2CAP/ECFC/BV-79-C|
|L2CAP 1/6 AND<br>L2CAP 2/48b|Enhanced Credit Based Flow Control Channel<br>Responder, LE|L2CAP/ECFC/BI-03-C<br>L2CAP/ECFC/BI-04-C<br>L2CAP/ECFC/BI-05-C<br>L2CAP/ECFC/BI-06-C<br>L2CAP/ECFC/BI-07-C<br>L2CAP/ECFC/BV-03-C<br>L2CAP/ECFC/BV-15-C<br>L2CAP/ECFC/BV-17-C<br>L2CAP/ECFC/BV-20-C<br>L2CAP/ECFC/BV-23-C<br>L2CAP/ECFC/BV-25-C<br>L2CAP/ECFC/BV-26-C<br>L2CAP/ECFC/BV-27-C<br>L2CAP/ECFC/BV-29-C<br>L2CAP/ECFC/BV-32-C<br>L2CAP/ECFC/BV-39-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **340 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 1/2 AND<br>L2CAP 2/48a|Enhanced Credit Based Flow Control Channel<br>Responder – BR/EDR|L2CAP/ECFC/BI-09-C<br>L2CAP/ECFC/BV-40-C<br>L2CAP/ECFC/BV-47-C<br>L2CAP/ECFC/BV-53-C<br>L2CAP/ECFC/BV-56-C<br>L2CAP/ECFC/BV-59-C<br>L2CAP/ECFC/BI-12-C<br>L2CAP/ECFC/BV-61-C<br>L2CAP/ECFC/BI-13-C<br>L2CAP/ECFC/BV-62-C<br>L2CAP/ECFC/BV-63-C<br>L2CAP/ECFC/BI-14-C<br>L2CAP/ECFC/BI-15-C<br>L2CAP/ECFC/BV-64-C<br>L2CAP/ECFC/BI-16-C<br>L2CAP/ECFC/BV-70-C|
|L2CAP 1/5 AND<br>L2CAP 2/48b AND<br>L2CAP 4/1|Enhanced Credit Based Flow Control Channel<br>Initiator with Authentication, LE|L2CAP/ECFC/BV-10-C|
|L2CAP 1/1 AND<br>L2CAP 2/48a AND<br>L2CAP 5/1|Enhanced Credit Based Flow Control Channel<br>Initiator with Authentication, BR/EDR|L2CAP/ECFC/BV-67-C|
|L2CAP 1/5 AND<br>L2CAP 2/48b AND<br>L2CAP 4/2|Enhanced Credit Based Flow Control Channel<br>Initiator with Authorization, LE|L2CAP/ECFC/BV-12-C|
|L2CAP 1/1 AND<br>L2CAP 2/48a AND<br>L2CAP 5/2|Enhanced Credit Based Flow Control Channel<br>Initiator with Authorization, BR/EDR|L2CAP/ECFC/BV-68-C|
|L2CAP 1/5 AND<br>L2CAP 2/48b AND<br>L2CAP 4/3|Enhanced Credit Based Flow Control Channel<br>Initiator with Encryption, LE|L2CAP/ECFC/BV-14-C|
|L2CAP 1/6 AND<br>L2CAP 2/48b AND<br>L2CAP 4/1|Enhanced Credit Based Flow Control Channel<br>Responder with Authentication, LE|L2CAP/ECFC/BV-11-C|
|L2CAP 1/6 AND<br>L2CAP 2/48b AND<br>L2CAP 4/2|Enhanced Credit Based Flow Control Channel<br>Responder with Authorization, LE|L2CAP/ECFC/BV-13-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **341 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|L2CAP 2/48b|Enhanced Credit Based Flow Control Channel<br>- Data, LE|L2CAP/COS/ECFC/BV-01-C<br>L2CAP/COS/ECFC/BV-02-C<br>L2CAP/COS/ECFC/BV-03-C<br>L2CAP/COS/ECFC/BV-04-C<br>L2CAP/ECFC/BI-01-C<br>L2CAP/ECFC/BI-02-C<br>L2CAP/ECFC/BV-06-C<br>L2CAP/ECFC/BV-07-C<br>L2CAP/ECFC/BV-09-C<br>L2CAP/ECFC/BV-30-C<br>L2CAP/ECFC/BV-33-C<br>L2CAP/ECFC/BV-34-C<br>L2CAP/ECFC/BV-35-C<br>L2CAP/ECFC/BV-41-C<br>L2CAP/ECFC/BV-80-C|
|L2CAP 2/48a|Enhanced Credit Based Flow Control Channel<br>– Data, BR/EDR|L2CAP/ECFC/BV-42-C<br>L2CAP/ECFC/BV-49-C<br>L2CAP/ECFC/BV-50-C<br>L2CAP/ECFC/BI-10-C<br>L2CAP/ECFC/BI-11-C<br>L2CAP/ECFC/BV-66-C<br>L2CAP/ECFC/BV-73-C<br>L2CAP/ECFC/BV-76-C<br>L2CAP/ECFC/BV-77-C<br>L2CAP/ECFC/BV-78-C<br>L2CAP/ECFC/BV-81-C<br>L2CAP/COS/ECFC/BV-05-C<br>L2CAP/COS/ECFC/BV-06-C<br>L2CAP/COS/ECFC/BV-07-C<br>L2CAP/COS/ECFC/BV-08-C|
|L2CAP 2/48b AND<br>L2CAP 2/45a|Enhanced Credit Based Flow Control Channel<br>– Send Disconnect, LE|L2CAP/ECFC/BV-08-C|
|L2CAP 2/48a AND<br>L2CAP 2/45|Enhanced Credit Based Flow Control Channel<br>– Send Disconnect, BR/EDR|L2CAP/ECFC/BV-65-C|
|**CID**|||
|(GAP 44/1 OR<br>GAP 44/2 OR<br>GAP 45/1 OR<br>GAP 45/2) AND<br>L2CAP 1/5|LE Data Channel Initiator - Simultaneous<br>BR/EDR and LE Transports|L2CAP/LE/CID/BV-01-C|
|(GAP 44/1 OR<br>GAP 44/2 OR<br>GAP 45/1 OR<br>GAP 45/2) AND<br>L2CAP 1/6|LE Data Channel Acceptor - Simultaneous<br>BR/EDR and LE Transports|L2CAP/LE/CID/BV-02-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **342 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Item**|**Feature**|**Test Case(s)**|
|(GAP 44/1 OR GAP<br>44/2 OR GAP 45/1<br>OR GAP 45/2) AND<br>L2CAP 2/48a AND<br>L2CAP 2/48b|LE Data Channel Initiator – Simultaneous<br>BR/EDR and LE Transports – Enhanced<br>Credit Based Flow Control Mode|L2CAP/LE/CID/BV-03-C<br>L2CAP/LE/CID/BV-04-C|
|L2CAP 0a/1|BR/EDR Invalid CID|L2CAP/COS/CID/BI-01-C|
|L2CAP 0a/2|LE Invalid CID|L2CAP/LE/CID/BI-01-C|
|**TIM**|||
|(GATT 1a/2 AND<br>GATT 1a/4) AND<br>L2CAP 1/1 AND<br>L2CAP 1/2|L2CAP Collision Mitigation, BR/EDR, ATT|L2CAP/TIM/BV-01-C|
|(GATT 1a/2 AND<br>GATT 1a/4) AND<br>L2CAP 1/1 AND<br>L2CAP 1/2 AND<br>L2CAP 2/48a AND<br>GATT 2/3b|L2CAP Collision Mitigation, BR/EDR, EATT|L2CAP/TIM/BV-02-C|
|(GATT 1a/1 AND<br>GATT 1a/3) AND<br>L2CAP 1/4 AND<br>L2CAP 1/5 AND<br>L2CAP 1/6 AND<br>L2CAP 2/48b AND<br>GATT 2/3a|L2CAP Collision Mitigation, LE, EATT|L2CAP/TIM/BV-03-C|

_Table 5.1 Test case mapping_

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **343 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

## **6 Revision histor and acknowled ments y g**

## _**Revision History**_

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||D5r3|2003-11-05|Original Release|
||D10R00|2004-03-03|Re-partitioned to match Main Specification<br>Volume/Part partitioning. TSE 472, 473, 474, 475, 476,<br>477, 478, 482, and 485 incorporated|
||D12r01-02|2004-03-23|Editorial changes. Changed reference and document<br>numbering to D12 to reflect applicable Bluetooth<br>version.|
|0|1.2.1|2004-03-25|Editorial changes. Changed document numbering and<br>revision number to conform to legacysystem.|
|1|1.2.2|2004-07-01|Changed page numbering to begin part with page 1<br>and made editorial changes to accommodate Vol. 1,<br>Part A.|
|2|1.2.3|2004-08-24|TSE 549 affecting TP/COS/CED/BV-01-C<br>TSE 554 affecting the TCMT<br>TSE 576 affecting TP/COS/IEX/BV-02-C<br>TSE 611 affectingTP/COS/CED/BV-08-C|
|3|1.2.4|2005-03-23|TSE 564 : TP/COS/CFD/BV-09-C.<br>TSE 595 : TCMT.<br>TSE 597 : TP/COS/RTX/BV-01-C.<br>TSE 602 : TP/COS/CED/BV-10-C.<br>TSE 630 : TP/COS/ECH/BV-02-C.<br>TSE 635 : TP/COS/CFD/BV-02-C.<br>TSE 637 : TP/COS/CFD/BV-03-C.<br>TSE 698 : TP/COS/CED/BV-08-C.|
|4|1.2.5|2005-10-21|TSE 746 : TP/COS/CED/BV-08-C; change timer value<br>TSE 790 : TP/COS/CFD/BV-11-C<br>TSE 816 : TP/CLS/GRH/BV03|:04-C<br>TSE 817 : TP/COS/CFD/BV-09: update MSC<br>TSE 791 : TP/COS/CFD/BV-01<br>Removed all references to GRH, including an entry in<br>the table in 5.1.2, line in the test mapping table.<br>TSE 746: Update TP/COS/CED/BV-08-C per last TSE<br>comment|
|5|1.2.6|2006-06-05|TSE 851: TP/COS/CED/BV-11-C: add note to P/F<br>verdicts<br>TSE 870: TP/COS/CED.BV-10-C Change MMI to<br>Upper Tester in Pass verdict<br>--Removed Inconclusive verdicts and Uncertainties<br>with ‘N/A.’|
|6|1.2.7|2006-10-06|Update TCMT for TP/COS/CFD/BV-09-C<br>Added new TC TP/COS/CFD/BV-13<br>TSE 1728: TP/COS/RTX/BV-01-C|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **344 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 1834: Remove stmt “The Lower Tester acts as a<br>device...” Added sentence The Lower Tester utilizes<br>version 1.2 Basic Mode.<br>TP/COS/CED/BV-01-C, TP/COS/CED/BV-03-C,<br>TP/COS/CED/BV-04-C, TP/COS/CED/BV-05-C,<br>TP/COS/CED/BV-07-C, TP/COS/CED/BV-08-C,<br>TP/COS/CFD/BV-02-C, TP/COS/CFD/BV-03-C,<br>TP/COS/CFD/BV-08-C, TP/COS/ECH/BV-01-C,<br>TP/COS/ECH/BV-02-C, TP/CLS/CLR/BV-01-C|
|7|2.1.E.0|2006-12-28|Removed page numbers as part of references<br>TSE: 1437: TP/COS/CFD/BV-09-C: Remove 3rd<br>L2CAP_ConfigReq in MSC<br>TSE 2012: TP/COS/CFD/BV-09-C: MSC: Make last<br>payload optional.|
|8|2.1.E.1|2007-08-23|TSE 1987: TP/COS/CFD/BV-01-C; Fail verdict and<br>MSC|
|9|2.1.E.2|2008-04-18|TSE 2220: TP/COS/CFD/BV-09-C: TP, Pass verdict,<br>fail verdict|
|10|2.1.E.3|2008-04-19|Add new test cases for enhanced L2CAP|
||21.E.4r0|2008-10-08|TSE 2431:TP/COS/CFD/BV-09-C, MSC, pass verdict<br>TSE 2583: TP/COS/CFD/BV-01-Cgraphic replaced.|
|11|21.E.4|2008-12-12|Prepare forpublication.|
||2.1.E.5r0|2009-02-20|Incorporate Unicast connectionless data test cases<br>and new L2CAP test case.|
|12|3.0.H.0/<br>2.1.E.5|2009-04-14|Prepare for publication.|
|13|3.0.H.1|2009-08-16|TSE 2741: TP/ERM/BV-07-C MSC update<br>TSE 2756: TP/ERM/BV-19-C MSC update to I-frame<br>TSE 2758: TP/ERM/BV-16-C, TP/ERM/BV-17-C,<br>TP/ERM/BI-02-C , TP/ERM/BI-01-C: MSC update to<br>S-frame<br>TSE 2759: TP/ERM/BV-02-C: update MSC init.<br>condition<br>TSE 2787: TP/CMC/BV-04-C: Pass verdict<br>TSE 2785: Update caption for TP/CMC/BV-02-C<br>TSE 2662: TP/ERM/BV-06-C: Updated MSC.|
|14|3.0.H.2r0|2010-04-16|TSE 3463: TP/ERM/BI-05-C: Updated MSC.|
||4.0.0d1 to<br>4.0.d5|2010-05-10<br>to 2010-06-<br>23|Merged document with L2CAP TS for LE<br>Adding the following TCs for LE operation<br>TP/LE/CPU/BV-01-C, TP/LE/CPU/BI-02-C,<br>TP/LE/CPU/BV-02-C, TP/LE/CPU/BV-01-C,<br>TP/LE/REJ/BI-01-C<br>Updated TCMT to map with first L2CAP.ICS merged<br>version (L2CAP.ICS.4.0.0d1)<br>BTI review feedback addressed<br>TP/LE/CPU/BV-02-C in verdict<br>L2CAP_ConnecionParametertRsp changed to<br>L2CAP_ConnectionParameterUpdateRsp|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **345 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||Figure 4.1 obsolete, removed<br>Sections 5.2.1.1, 5.2.2.1, 5.2.4.1, 5.4.1.1, 5.2.1.11<br>removed as they repeated what is once defined in<br>4.4.2<br>Updated Conformance (section 4.2.6)<br>TSE 3490, labeling of MSC figure 5.111 corrected.<br>TSE 2778 initial condition for TP/COS/ECH/BV-02-C<br>corrected<br>TSE 3059 Test purpose of TP/MCH/BV-30-C<br>corrected<br>TSE 3061 Test purpose of TP/MCH/BV-32-C<br>corrected<br>TSE 3066 Test purpose of TP/MCH/BV-33-C<br>corrected<br>TSE 3067 Test purpose of TP/MCH/BV-34-C<br>corrected<br>TSE 3130 Pass verdicts of corrected<br>TSE 3223 Updated fail verdicts for TP/CMC/BV-09-C<br>and , TP/CMC/BI-05-C<br>TSE 3225 Re-added missing Figure 5.73 in<br>TP/ERM/BV-03-C<br>TSE 3305 Corrected TCMT for missing TP/CCH/BV-<br>02-C and TP/CCH/BV-03-C.<br>TSE 3344 Corrected TCMT for<br>TP/OFS/BV-01-C, TP/OFS/BV-02-C, TP/OFS/BV-05-C<br>TP/OFS/BV-06-C (L2CAP, 2/12 AND 2/14)<br>TP/OFS/BV-03-C TP/OFS/BV-04-C TP/OFS/BV-07-C<br>TP/OFS/BV-08-C (L2CAP, 2/13 AND 2/14)<br>TSE 3799 addressing duplicate TC-identifiers, second<br>instance of TP/STM/BV-01-C and TP/STM/BV-02-C,<br>renamed to TP/STM/BV-11-C and TP/STM/BV-12-C.<br>New TCMT for TP/STM/BV-11-C, TP/STM/BV-12-C<br>and TP/STM/BV-13-C<br>TSE 3422 updated TCMT for TP/LSC/BV-07-C,<br>TP/LSC/BV-09-C, TP/LSC/BI-10-C, TP/LSC/BI-11-C,<br>TP/LSC/BV-08-C, TP/LSC/BV-12-C<br>TSE 3805 editorial note in TP/LSC/BV-08-C test<br>purpose removed<br>TSE 3804 editorial note in TP/LSC/BV-02-C test<br>purpose removed<br>TSE 3803 editorial note in TP/EXF/BV-05-C fail verdict<br>removed<br>TSE 2980 IUT role clarified in initial conditions for<br>TP/COS/CFD/BV-09-C, TP/COS/ECH/BV-02-C,<br>TP/COS/CED/BV-11-C, TP/COS/CFD/BV-11-C,<br>TP/COS/CFD/BV-12-C<br>TSE 3382 TCMT corrected for TP/MCH/BV-25-C and<br>TP/MCH/BV-26-C<br>Editorial corrections<br>TSE 3130 edits backed out|
|15|4.0.0|2010-06-30|Publication.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **346 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||4.0.1r0|2010-11-01 –<br>2010-11-30|TSE 2734: TP/CMC/BV-03-C:Update MSC<br>TSE 2942: TP/CMC/BV-03-C, TP/CMC/BV-06-C,<br>TP/CMC/BV-07-C, TP/CMC/BV-08-C, TP/CMC/BV-09-<br>C,TP/CMC/BI-05-C, TP/CMC/BI-06-C, TP/CMC/BV-<br>10-C, TP/CMC/BV-11-C: update MSC<br>TSE 3052: TP/MCH/BV-03-C: update MSC<br>TSE 3057: TP/ERM/BV-21-C: update MSC<br>TSE 3070: TP/MCH/BV-36-C: update MCS<br>TSE 3109: TP/ERM/BV-21-C; updated MSC<br>TSE 3293: TP/LSC/BV-06-C, TP/LSC/BV-12-C:<br>update MSC.<br>TSE 3463: TP/ERM/BI-05-C: updated MSC (redone)<br>TSE 3475: TP/ERM/BV-02-C: specify 48-byte MTU<br>TSE 3539: TP/ERM/BV-19-C: updated MSC<br>TSE 3714: TP/CMC/BV-12-C, TP/CMC/BV-13-C<br>TSE 3731: TP/FOC/BV-04-C: Revised test procedure<br>TSE 4079: TP/CMC/BV-03-C - 09-C, TP/CMC/BI-01 -<br>06-C, TP/CMC/BV-14,15-C, TP/FOC/BV-01 - 03-C,<br>TP/EWC/BV-01-C, TP/EWC/BV-02-C: Change<br>Preamble in MSCs<br>TSE 4082: TP/LE/CPU/BI-01-C: TCMT: add entry<br>TSE 4164: TP/LE/CPU/BI-02-C: fix typos|
||4.0.1r1-r6|2011-01-31-<br>2011-05-11|Input reviewer’s comments,<br>TSE 3475: TP/ER/BV-02-C: edit MSC Figure 5.72<br>TSE 3714: TP/CMC/BV-12-C, TP/CMC/BV-13-C:edit<br>text per change tracking<br>TSE 3731: TP/FOC/BV-04-C: edited text per change<br>tracking<br>TSE 4079: Edit MSC preambles in the following<br>figures:<br>Fig. 5.43 - 5.51 and Fig 5.57-Fig 5.62, & Fig. 5.107 for<br>TP/CMC/BV-06-C to TP/CMC/BV-09-C, TP/CMC/BI-<br>01-C to TP/CMC/BI-04-C, TP/CMC/BI-06-C,<br>TP/CMC/BV-14-C, TP/CMC/BV-15-C, TP/FOC/BV-01-<br>C to TP/FOC/BV-04-C, and TP/EWC/BV-02-C<br>TSE 4164: Changed wording per change tracking.<br>TSE 4038: TCMT: add selection expressions for<br>TP/EXF/BV-04-C, TP/EXF/BV-05-C, TP/EXF/BV-06-C,<br>TP/EWC/BV-01-C, TP/EWC/BV-02-C, TP/EWC/BV-<br>03-C, TP/LSC/BV-01-C , TP/LSC/BV-02-C ,<br>TP/LSC/BV-03-C , TP/LSC/BI-04-C , TP/LSC/BI-05-C ,<br>TP/LSC/BV-06-C , TP/ECF/BV-01-C , TP/ECF/BV-02-<br>C , TP/ECF/BV-03-C , TP/ECF/BV-04-C , TP/ECF/BV-<br>05-C , TP/ECF/BV-06-C , TP/ECF/BV-07-C ,<br>TP/ECF/BV-08-C<br>More review comments:<br>TSE 3714: TP/CMC/BV-13-C: Pass verdict update<br>TSE 3731: TP/FOC/BV-04-C: typo in MSC|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **347 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 4079: Fig. 5.43 - 5.52 and Fig 5.57-Fig 5.62, &<br>Fig. 5.107 for TP/CMC/BV-06-C to TP/CMC/BV-09-C,<br>TP/CMC/BI-01-C to TP/CMC/BI-04-C, TP/CMC/BI-06-<br>C, TP/CMC/BV-14-C, TP/CMC/BV-15-C, TP/FOC/BV-<br>01-C to TP/FOC/BV-04-C, and TP/EWC/BV-02-C<br>TSE 4164: MSC and Pass verdict edits for all,<br>additional corrections for TP/LE/CPU/BI-01-C,<br>TP/LE/CPU/BI-02-C<br>Further revisions to Figs 5.43-5.52, 5.57-5.61, 5.107:<br>Change “sub-state” to “state”<br>Edit TSE 4164: TP/LE/CPU/BV-01-C and<br>TP/LE/CPU/BV-02-C change Request to Req in MSCs<br>TSE 4192, TSE 4367 TCMT for TP/FIX/BV-02-C|
|16|4.0.1|2011-07-15|Prepare forpublication.|
||4.0.2r0|2011-11-07|TSE 3490: Correct MSC figure 5.111 label. Done in<br>4.0.1<br>TSE 4073: TP/MCH/BV-12-C, TP/MCH/BV-13-C<br>TCMT change<br>TSE 4279: TP/MCH/BV-26-C: TCMT change per TSE<br>3382.<br>TSE 4341: TP/CMC/BI-03-C: Remove in TCMT<br>TSE 4373: TP/ERM/BV-21-C: Initial Condition, Pass<br>verdict, Fail verdict<br>TSE 3422,**ID:**9030: Fixed TP/LSC/BV-07-C,<br>TP/LSC/BV-08-C, TP/LSC/BV-09-C, TP/LSC/BI-10-C,<br>TP/LSC/BI-11-C, TP/LSC/BI-11-C in TCMT<br>TSE 4398: TP/CCH/BV-01-C, TP/CCH/BV-02-C,<br>TP/CCH/BV-03-C, TP/CCH/BV-04-C: TP/MCH/BV-01-<br>C, TP/MCH/BV-06-C, TP/MCH/BV-04-C, TP/MCH/BV-<br>08-C, TP/MCH/BV-10-C, TP/MCH/BV-12-C: update<br>TCMT<br>TSE 4486: TP/STM/BV-11-C,TP/STM/BV-12-C,<br>TP/STM/BV-13-C: Add to TCMT<br>TSE 4509: TP/ERM/BV-19-C: Update MSC and Pass<br>verdict<br>TSE 4530: TP/OFS/BV-08-C: Update MSC<br>TSE 4548: TP/EXF/BV-05-C: Pass verdict<br>TSE 4562: TP/LE/REJ/BI-01-C: TCMT|
|17|4.0.2r1|2012-01-24|From JN’s review; changes to TCMT for 4073<br>TSE 4584: Clarification of TSE 3422/Rejection of TSE<br>4378|
||4.0.3r0|2012-09-20|TSE 4817: Update to MSC for TP/ERM/BI-05-C<br>TSE 4811: Update to MSC for TP/ERM/BV-19-C|
|18|4.0.3|2012-11-12|Prepare for Publication|
||4.0.4r1|2013-05-31|TSE 4839:<br>Updated initial condition, pass and fail verdict, and<br>MSC for TP/COS/CED/BV-09-C.<br>Updated TCMT mapping for TP/COS/CFD/BV-09-C<br>and TP/COS/CED/BV-01-C to add “AND L2CAP 1/1”<br>and remove TP/COS/CED/BV-05-C.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **348 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||Added TP/COS/CED/BV-05-C to TCMT in a new row.<br>TSE 5027: Updated purpose, initial condition, MSC<br>andpass and fail verdicts for TP/ERM/BV-21-C.|
||4.0.4r2|2013-06-08|BTI Review, Alicia and Magnus:<br>Re-organized items ins 4 and 5 to align with the<br>current template for Test Suite Structure/Test Strategy<br>and Test Purposes.<br>Added the test naming for the LE test groups in the TP<br>naming conventions.<br>Regrouped the test cases in the Test Spec according<br>to the main groupings - CONNECTION ORIENTED<br>basic L2CAP mode; CONNECTION ORIENTED<br>retransmission/flow control/streaming modes;<br>CONNECTIONLESS basic L2CAP mode.<br>Applied some heading styles tos as needed.<br>Added missing test group objectives.<br>Regrouped the tests in the TCMT for the test groups.<br>Added missing features to the TCMT rows.<br>Corrected some type-o’s consistently applied Lower<br>Tester and Upper Tester and result codes as well as<br>other test naming/spelling capitalization conventions<br>per the L2CAP specification.<br>Inserted reference tags and updated fields in the test<br>case text.<br>Regenerated the Table of Contents.|
||4.0.4r3|2013-06-10|BTI review, Magnus: TSE 4839 TCMT changes were<br>not included originally. Updated.|
||4.0.4r1|2013-05-31|TSE 4839:<br>Updated initial condition, pass and fail verdict, and<br>MSC for TP/COS/CED/BV-09-C.<br>Updated TCMT mapping for TP/COS/CFD/BV-09-C<br>and TP/COS/CED/BV-01-C to add “AND L2CAP 1/1”<br>and remove TP/COS/CED/BV-05-C.<br>Added TP/COS/CED/BV-05-C to TCMT in a new row.<br>TSE 5027: Updated purpose, initial condition, MSC<br>andpass and fail verdicts for TP/ERM/BV-21-C.|
||4.0.4r2|2013-06-08|BTI Review, Alicia and Magnus:<br>Re-organized items ins 4 and 5 to align with the<br>current template for Test Suite Structure/Test Strategy<br>and Test Purposes.<br>Added the test naming for the LE test groups in the TP<br>naming conventions.<br>Regrouped the test cases in the Test Spec according<br>to the main groupings - CONNECTION ORIENTED<br>basic L2CAP mode; CONNECTION ORIENTED<br>retransmission/flow control/streaming modes;<br>CONNECTIONLESS basic L2CAP mode.<br>Applied some heading styles tos as needed.<br>Added missingtestgroupobjectives.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **349 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||Regrouped the tests in the TCMT for the test groups.<br>Added missing features to the TCMT rows.<br>Corrected some type-o’s consistently applied Lower<br>Tester and Upper Tester and result codes as well as<br>other test naming/spelling capitalization conventions<br>per the L2CAP specification.<br>Inserted reference tags and updated fields in the test<br>case text.<br>Regenerated the Table of Contents.|
||4.0.4r3|2013-06-10|BTI review, Magnus: TSE 4839 TCMT changes were<br>not included originally. Updated.|
|19|4.0.4|2013-07-02|Prepare for Publication|
||4.0.5rT|2013-07-03|Template Conversion:<br>- Update of language to match BTI approved wording<br>(example, fail verdicts)<br>- Removal of Test Subgroup Objectives<br>- Removal of s marked “N/A”|
||4.0.5rTr3|2013-08-01|Updated MSC per TSE 1662 in TP/COS/CFD/BV-11-<br>C.|
||4.0.5rTr4|2013-10-03|Template Conversion Finalization<br>-<br>Fail Verdicts Removed<br>-<br>New Pass/Fail Verdict Criteria added<br>-<br>Definitions/Abbreviationss removed, added to<br>Referencespreamble.|
||4.0.5rTr5|2013-10-03|Template Review Comment Resolution & Changes<br>Accepted|
||4.1.0r01|2013-10-07|TSE 4840: Updated Initial Condition, MSC and Pass<br>Verdict for TP/COS/CED/BV-08-C and updated TCMT<br>for TP/COS/CED/BV-04-C.<br>TSE 5244: Updated MSC and Pass Verdict for<br>TP/FOC/BV-04-C.<br>TSE 5291: Updated MSCs so the F-bit equals 0 for the<br>I-Frame in ALT 2 of TP/FOC/BV-01-C, TP/FOC/BV-02-<br>C, and TP/FOC/BV-03-C.|
||4.1.0r02|2013-10-11|LE L2CAP Connection Oriented Channels CR|
||4.1.0r03|2013-10-31|Erratum 5392: Addition of two new test cases,<br>TP/LE/CID/BV-01-C and TP/LE/CID/BV-02-C.|
|20|4.1.0|2013-12-03|Prepare for Publication|
||4.1.1r00|2014-01-23|TSE 5406: Removed duplicates in TCMT for<br>TP/LE/CFC/BV-08-C, TP/MCH/BV-01-C, TP/MCH/BV-<br>04-C, TP/MCH/BV-06-C, TP/MCH/BV-10-C, and<br>TP/MCH/BV-12-C.|
||4.1.1r01|2014-04-08|TSE 5371: Revision in MCH for Initial Conditions and<br>Test Procedures to clarify MSCs.<br>TSE 5409: Updated Mapping for TP/MCH/BV-12-C,<br>TP/MCH/BV-13-C, TP/MCH/BV-25-C, and<br>TP/MCH/BV-26-C.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **350 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 5519: Updated Test Case Description and added<br>5.5 as a reference for TP/FOC/BV-04-C.<br>SEE update to TSE 5519 in revision 4.1.1r04|
||4.1.1r02|2014-04-21|TSE 5580: Updated MSC for TP/LE/CFC/BV-01-C,<br>TP/LE/CFC/BV-03-C; Updated MSC, Test Procedure<br>and Pass verdict for TP/LE/CFC/BV-02-C; Numbered<br>the Test Procedure for TP/LE/CFC/BV-06-C; Updated<br>Test Procedure for TP/LE/CFC/BV-07-C and<br>TP/LE/CFC/BV-12-C; Updated Initial Condition of<br>TP/LE/CFC/BV-10-C and TP/LE/CFC/BV-14-C;<br>Updated Initial Condition and Test Procedure of<br>TP/LE/CFC/BV-11-C.|
||4.1.1r04|2014-06-21|Update to TSE 5519: Removed TP/FOC/BV-04-C.|
|21|4.1.1|2014-07-07|TCRL 2014-1 Publication|
||4.1.2r00|2014-10-21|TSE 5787: Added TC descriptions to TP/LE/CID/BV-<br>01-C and TP/LE/CID/BV-02-I.<br>TSE 5920: Corrected MSC for TP/COS/CED/BI-01-C.<br>TSE 5810: Updated CID numbers in TP/LE/CID/BV-<br>01-C and TP/LE/CID/BV-02-I. Updated TP/CID/BV-02-<br>I to a conformance test, TP/CID/BV-02-C. Updated<br>TCMT for the –I to –C change.<br>Updated PIXIT to IXIT, and MMI to Upper Tester.|
||4.2.0r00|2014-11-17|Revved version to align with Core Specification<br>Version 4.2 Release.|
||4.2.0r01|2014-11-25|BTI Review, Alicia, minor editorial corrections.|
|22|4.2.0|2014-12-04|Prepare for TCRL 2014-2publication|
||4.2.1r00|2015-05-05|TSE 6093: Updated TCMT to correct mapping for<br>TP/COS/CED/BV-04-C & TP/LE/CFC/BV-08-C (items<br>L2CAP 2/45 & 2/46)<br>TSE 6335: Updated TP/ERM/BV-07-C to enable<br>testing of both scenarios in PTS (via IXIT).<br>TSE 5520: Deleted test TP/ERM/BV-21-C and<br>removed it from TCMT.|
||4.2.1r01|2015-06-03|Updated date conventions and formatting in revision<br>historytable.|
||4.2.1r02|2015-06-15|TSE 6434: Added feature descriptions to TCMT for<br>TP/LE/CID/BV-01-C and TP/LE/CID/BV-02-C.|
|23|4.2.1|2015-07-14|Prepared for TCRL 2015-1publication|
||4.2.2r00|2015-10-07|TSE 6400: Added clarifying text to TP/FIX/BV-02-C<br>initial conditions and corrected InfoType in MSC for<br>TP/FIX/BV-02-C.|
||4.2.2r01|2015-10-23|Reviewed by Alicia Courtney. Updated terminology in<br>3.1 from “Host Subsystem” to “Host”.|
|24|4.2.2|2015-12-22|Prepared for TCRL 2015-2publication.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **351 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||4.2.3r00|2016-02-16|TSE 6812: MSCs updated for test cases<br>TP/COS/CFC/BV-01-C, TP/COS/CFC/BV-02-C,<br>TP/COS/CFC/BV-03-C, TP/COS/CFC/BV-04-C,<br>TP/COS/CFC/BV-05-C, TP/LE/CFC/BV-03-C. "LE<br>Data Channel established"/"Channel Established"<br>changed to "LE Credit Based Flow Control Channel<br>established".|
||4.2.3r01|2016-02-22|TSE 6725: Typo in I-frame at last sequence corrected:<br>“N(R)=0” changed to “N(R)=0 or 1”|
||4.2.3r02|2016-03-02|TSE 6680: Added new four new test procedures<br>(Sections 4.4.3.19–22) and test cases to TCMT:<br>TP/LE/CFC/BV-18-C – 21-C.|
||4.2.3r03|2016-04-28|Reviewed by BTI, Alicia. Editorial corrections. Some<br>MSCs updated.|
|25|4.2.3|2015-07-13|Prepared for TCRL 2016-1publication.|
||5.0.0r00|2016-08-17|TSE 7266: Updated Initial Condition and Test<br>Procedure for test case TP/LE/CID/BV-01-C and<br>TP/LE/CID/BV-02-C.|
||5.0.0r01|2016-11-20|Five test cases added back into TCMT which were<br>erroneously deleted after integration of TSE 5406:<br>TP/MCH/BV-01-C, TP/MCH/BV-04-C, TP/MCH/BV-06-<br>C, TP/MCH/BV-08-C, TP/MCH/BV-10-C|
|26|5.0.0|2016-12-13|Approved by BTI. Prepared for TCRL 2016-2<br>publication.|
||5.0.1r00|2017-03-27|TSE 7691: Reworded the pass verdict for<br>L2CAP/COS/CFC/BV-01-C.<br>TSE 8527: Updated TCMT item to “L2CAP 2/45” for<br>L2CAP/COS/CED/BV-04-C. Updated TCMT item to<br>“L2CAP 2/46 AND L2CAP 2/45a” for<br>L2CAP/LE/CFC/BV-08-C.|
||5.0.1r01|2017-05-22|Converted to new Test Case ID conventions as<br>defined in TSTO v4.1.|
|27|5.0.1|2017-07-05|Approved by BTI. Prepared for TCRL 2017-1<br>publication.|
||5.0.2r00|2017-08-17|TSE 9506: Revised TCMT for L2CAP/COS/CFD/BV-<br>08-C to “L2CAP 1/1 AND L2CAP 2/2”.|
||5.0.2r01|2017-09-05|TSE 9751: Revised text in the Channel Identifiers<br>(CID) test group objective and revised test procedure<br>steps for L2CAP/LE/CID/BV-01-C and<br>L2CAP/LE/CID/BV-02-C.|
|28|5.0.2|2017-12-07|Approved by BTI. Prepared for TCRL 2017-2<br>publication.|
||5.1.0r00|2018-11-13|Updated revision number to 5.1.0 to align with the<br>adoption of Core Specification version 5.1.|
|29|5.1.0|2018-12-07|Approved by BTI. Prepared for TCRL 2018-2<br>publication.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **352 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||5.1.1r00–r02|2019-04-15–<br>2019-06-13|TSE 11717 (rating 1): Updated text in the first<br>paragraph of the Test Strategy in the Test Suite<br>Structure (TSS) to address an issue with redundant<br>PDUs.<br>Editorial: rephrased “_The Lower Tester utilizes version_<br>_1.2 Basic Mode_” to “_The Lower Tester utilizes version_<br>_L2CAP Basic Mode_” throughout and moved statement<br>from test purpose to initial condition in those instances<br>where it existed.|
|30|5.1.1|2019-08-01|Approved by BTI. Prepared for TCRL 2019-1<br>publication.|
||p31r00–r08|2019-08-21 –<br>2019-11-22|Added test groups to accommodate adoption of Core<br>Specification v5.2 with regard to EATT CR r07.<br>Updated References with new Core Specification.<br>Updated Test Groups with new terminology. Updated<br>TCID Conventions table with new abbreviation.<br>Updated Connection Oriented Basic L2CAP Mode with<br>new test cases L2CAP/COS/ECFC/BV-01-C – -03-C;<br>deleteds for test cases L2CAP/LE/CFC/BV-08-C – -10-<br>C, -12-C, -13-C, -15-C, and -17-C (TCIDs added to<br>tables under news); added Connection Oriented<br>Enhanced L2CAP Mode, including addition of test<br>cases L2CAP/ECFC/BV-01-C – -04-C, -06-C – -27-C<br>and BI-01-C – -04-C; added new test cases<br>L2CAP/LE/CID/BV-03-C and -04-C to Channel<br>Identifiers (CID). Updated TCMT accordingly.<br>Issue 12289 (CR r03 file from comment 48454).<br>Replaced MSCs for test cases L2CAP/COS/ECFC/BV-<br>03-C, L2CAP/ECFC/BV-02-C – -04-C,<br>L2CAP/ECFC/BV-10-C – -21-C; replaced MSCs and<br>edited test step one for test cases L2CAP/ECFC/BV -<br>26-C and -27-C; edited initial condition for test cases<br>L2CAP/LE/CID/BV-03-C and -04-C.<br>Issue 12307 (CR from comment 48456). Updated<br>MSC and test step 4 for test case L2CAP/ECFC/BV-<br>22-C; updated MSC and test step 3 for test case<br>L2CAP/ECFC/BV-23-C; updated MSC, added new test<br>step 2, and updated the pass verdict for test case<br>L2CAP/ECFC/BI-03-C; updated MSC and test steps 3<br>and 6 for test case L2CAP/ECFC/BV-24-C; updated<br>MSC and test steps 4 and 7 for test case<br>L2CAP/ECFC/BV-25-C; updated MSC and updated<br>test steps and pass verdict for test case<br>L2CAP/ECFC/BI-04-C.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **353 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||Issue 12411 (CR from comment 49159). Updated test<br>purpose, replaced MSC, updated test step 2<br>(additional text to Issue 12307) and deleted test step 4<br>(was step 3 before Issue 12307), and modified Pass<br>Verdict (same text as Issue 12307 for that paragraph)<br>for test case L2CAP/ECFC/BI-03-C; updated test<br>purpose, replaced MSC, added text to test step 2<br>(additional text to Issue 12307) and deleted step 4<br>(was step 3 before Issue 12307), and modified Pass<br>Verdict (same text as Issue 12307 for that paragraph)<br>for test case L2CAP/ECFC/BI-04-C.<br>Issue 12484 (CR from comment 49740). Added<br>“Notes” heading to Test Cases tables and replaced<br>text in PSM column for the first item in those tables for<br>the “Connection Oriented Enhanced L2CAP Modes’s<br>subsections as follows: “Disconnection Request”,<br>“Disconnection Response”, “Security – Insufficient<br>Authentication – Initiator”, “Security – Insufficient<br>Authorization – Initiator”, “Security - Insufficient<br>Authorization – Responder”, “Security – Insufficient<br>Encryption Key Size – Responder”, and “L2CAP Credit<br>Based Connection Request – refused due to<br>insufficient resources”; didn’t make change for “L2CAP<br>Credit Based Connection Request – refused due to<br>Invalid Source CID” because those test cases are still<br>in two separates.<br>TSE 12429 (rating 1): Already incorporated into<br>LL.TS.Milan_r00 as part of the EATT CR integration.<br>Affected test cases L2CAP/LE/CFC/BV-08-C – -10-C,<br>-12-C, -13-C, -15-C, and -16-C.<br>Issue 12522 (CR from comment 50029): Added test<br>case L2CAP/ECFC/BI-05-C; updated TCMT entry per<br>email from Cloud2Gnd (Virgil Dragomir, 2019-09-25).<br>Issue 12626 (CR from comment 51183): Updated<br>TCMT to clear references to TBDs.<br>Issue 12630 (CR from comment 51702): Updated<br>Reference, Initial Condition, MSC, and test steps, and<br>added an Inconclusive Verdict for test cases<br>L2CAP/ECFC/BV-24-C and -25-C (for -25-C, also<br>updated Pass Verdict).<br>Issue 12729 (CR from comment 51741): Added new<br>test case L2CAP/ECFC/BI-06-C and updated TCMT<br>accordingly.<br>TSE 11162 (rating 3): For test case<br>L2CAP/COS/CFD/BV-12-C, updated test purpose, test<br>procedure (added rounds table), MSC, and pass<br>verdict. Added new test case L2CAP/COS/CFD/BV-<br>14-C and updated the TCMT accordingly.<br>Replaced .X and Milan references to real numbers.<br>Revised document numbering convention, setting last<br>release publication of 5.1.1 as p30; added publication<br>number column to Revision History.|
|31|p31|2020-01-07|Approved by BTI on 2019-12-22. Prepared for<br>TCRL 2019-2publication.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **354 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||p32r00–r28|2020-01-24 –<br>2021-06-09|TSE 12837 (rating 4): To address E12684 regarding<br>adding an L2CAP test on potential deadlock on<br>collision, added a reference to the GAP spec, added<br>“TIM” to the TCID identifier table (and editorially<br>cleaned up table), and added new TCs<br>L2CAP/TIM/BV-01-C – -03-C. Updated TCMT<br>accordingly.<br>TSE 12929 (rating 2): Updated TCMT to account for<br>new Security Aspects table in ICS document.<br>TSE 12937 (rating 1): Updated “LE_PSM” to “SPSM”<br>to align with an erratum that was filed for EATT,<br>affecting test cases L2CAP/COS/CFC/BV-01-C – -05-<br>C; L2CAP/LE/CFC/BV-01-C – -07-C, -11-C, -14-C,<br>and -17-C – 21-C; L2CAP/LE/CFC/BI-01-C; and<br>L2CAP/LE/CID/BV-01-C and -02-C.<br>TSE 13027 (rating 2): Updated test procedure and<br>replaced MSC for test cases L2CAP/ECFC/BV-22-C<br>and -23-C to improve test time.<br>TSE 13214 (rating 2): Updated initial condition, MSC,<br>and test step for test case L2CAP/ECFC/BI-04-C, and<br>updated test purpose, initial condition, MSC, and test<br>step for test case L2CAP/ECFC/BI-05-C.<br>TSE 13220 (rating 4): Added new tests to<br>accommodate additional L2CAP ECBFC Conformance<br>Tests. New test cases: L2CAP/ECFC/BV-28-C – -35-C<br>and L2CAP/LE/CFC/BV-22-C – -28-C. Updated TCMT<br>accordingly.<br>TSE 13405 (rating 1): Fixed typo in TCMT.<br>TSE 13577 (rating 1): Removed inconclusive verdict<br>for test case L2CAP/ECFC/BI-03-C to better align with<br>spec.<br>TSE 14659 (rating 1): Updated MSCs (and in some<br>cases pass verdicts) for test cases<br>L2CAP/COS/CED/BV-01-C and -05-C;<br>L2CAP/COS/CFD/BV-08-C; L2CAP/CMC/BV-01-C, -<br>03-C, -04-C, and -06-C – -15-C; L2CAP/CMC/BI-01-C<br>– -06-C; L2CAP/FOC/BV-01-C – -03-C;<br>L2CAP/EWC/BV-01-C – -03-C; L2CAP/LE/CPU/BV-<br>01-C and -02-C; and L2CAP/LE/CPU/BI-01-C and -02-<br>C to accommodate a PDU name change per Erratum<br>13186.<br>TSE 14672 (rating 4): To address an issue with<br>missing L2CAP tests for fragmentation and<br>reassembly, added new TCs L2CAP/COS/CED/BV-<br>12-C and -13-C and /BI-02-C; L2CAP/ECFC/BV-39-C<br>– -42-C and /BI-08-C and -09-C; and<br>L2CAP/LE/CFC/BV-30-C and -31-C and /BI-02-C.<br>Updated TCMT accordingly.<br>TSE 14675 (rating 2): Updated initial condition and test<br>steps for test case L2CAP/ECFC/BV-24-C to correct<br>language about the SDU size.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **355 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 14697 (ratings 1 and 3): Moved “LE Credit Based<br>Flow Control Mode” section from a subsection of 4.10<br>to a subsection of 4.13, moved all multiple mode tests<br>(table-based test case config) to a new “All Credit<br>Based Flow Control Mode” section (including those<br>added for TSE 13220), and made other edits to<br>existing tests as per red text in CR under “[New<br>Section]” categorization. Category 1 change for test<br>cases L2CAP/ECFC/BV-10-C, -12-C, -13-C, -15-C, -<br>16-C. Category 3 change for test cases<br>L2CAP/LE/CFC/BV-10-C, -12-C, -13-C, -15-C, -16-C.<br>TSE 14759 (rating 2): For test case L2CAP/ECFC/BV-<br>17-C, replaced MSC, updated test steps, updated<br>pass verdict, and deleted inconclusive verdict. For test<br>case L2CAP/ECFC/BV-21-C, deleted an initial<br>condition, updated test steps, and deleted inconclusive<br>verdict. For test case L2CAP/ECFC/BI-03-C, deleted<br>an initial condition, updated test steps. For test case<br>L2CAP/ECFC/BV-24-C, updated initial condition,<br>replaced MSC, updated test steps, updated pass<br>verdict, and deleted inconclusive verdict. For test case<br>L2CAP/ECFC/BV-25-C, deleted inconclusive verdict.<br>For test case L2CAP/ECFC/BV-27-C, replaced MSC,<br>updated test steps, updated pass verdict, and deleted<br>inconclusive verdict.<br>TSE 14994 (rating 2): For section containing test<br>cases L2CAP/LE/CFC/BV-15-C and<br>L2CAP/ECFC/BV-15-C, updated initial condition,<br>replaced MSC, updated test steps, updated pass<br>verdict. Updated L2CAP/ECFC/BV-15-C to Category D<br>in the TCRL (L2CAP/LE/CFC/BV-15-C was already<br>Category D).<br>TSE 15077 (rating 3): For test case<br>L2CAP/COS/CED/BV-08-C, replaced MSC, updated<br>test procedure, updated pass verdict.<br>TSE 15410 (rating 2): To address an issue with the<br>incorrect MTU value being sent, updated initial<br>condition, MSC, test steps, and pass verdict for TC<br>L2CAP/ECFC/BV-27-C (NOTE: overwrites changes<br>made under TSE 14759 for this TC only). Updated<br>reference [3] from “no longer used” to refer to the<br>Core.IXIT.<br>TSE 15450 (rating 1): Editorials to address Erratum<br>15353, globally change “Master” to “Central” and<br>“Slave” to “Peripheral.”<br>TSE 15612 (rating 4): To address E15554, L2CAP<br>Credit Based Reconfigure Request - MPS greater or<br>equal to all destination CIDs, added new TC<br>L2CAP/ECFC/BI-07-C and updated TC<br>L2CAP/ECFC/BI-04-C. Updated TCMT accordingly.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **356 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 15868 (rating 4): To address E15833, Ignore<br>PDUs on a CID that is not assigned or RFU, updated<br>the Channel Identifiers test group objectives and<br>added new TCs L2CAP/COS/CID/BI-01-C,<br>L2CAP/LE/CID/BI-01-C, and L2CAP/CLS/CID/BV-01-<br>C. Updated TCMT accordingly.<br>TSE 15918 (rating 4): To address E15323, regarding<br>“Source, Destination CID dynamically changed”,<br>added new section “Credit Based Connection Request<br>Dynamically Allocated Source CID” which includes<br>new TCs L2CAP/ECFC/BV-38-C and<br>L2CAP/LE/CFC/BV-29-C. Updated TCMT accordingly.<br>TSE 16021 (rating 1): To address parameter name<br>changes from E15944, updated MSCs for TCs<br>L2CAP/LE/CPU/BV-01-C and -02-C and<br>L2CAP/LE/CPU/BI-01-C and -02-C.<br>TSE 16088 (rating 1): Corrected Opcode in test step<br>for TC L2CAP/ECFC/BI-03-C.<br>TSE 16149 (rating 3): To address an issue with<br>needing to encrypt a link before sending an<br>LE_Credit_Based_Connection_Request, updated<br>references to include line items for the SM.TS and the<br>LMP.TS; added a Setup Preambles/Encryption Key<br>Size section; and updated TC L2CAP/LE/CFC/BV-11-<br>C, the section containing TCs L2CAP/LE/CFC/BV-13-<br>C and L2CAP/ECFC/BV-13-C, and the section<br>containing TCs L2CAP/LE/CFC/BV-15-C and<br>L2CAP/ECFC/BV-15-C.<br>TSE 16953 (rating 2): Updated step 17 of TC<br>L2CAP/CLS/CID/BV-01-C.<br>TSE 16955 (rating 2): Updated step 3 of section<br>containing TCs L2CAP/LE/CFC/BI-02-C and<br>L2CAP/ECFC/BI-08-C.<br>TSE 16964 (rating 1): Updated MSC and test step for<br>section containing TCs L2CAP/LE/CFC/BV-25-C and<br>L2CAP/ECFC/BV-32-C.<br>Template-related editorials.|
|32|p32|2021-07-13|Approved by BTI on 2021-06-27. Prepared for<br>TCRL 2021-1publication.|
||p33r00–r07|2021-08-17 –<br>2021-12-16|TSE 15271 (rating 4): To address E14605, added new<br>TCs L2CAP/ECFC/BV-43-C and -44-C; updated<br>TCMT accordingly. Updated TCMT item entries for<br>TCs L2CAP/ECFC/BV-10-C – -15-C.<br>TSE 15582 (rating 2): To address an issue with initial<br>conditions and/or test procedures not being consistent<br>for all IUTs, updated initial conditions, test procedures,<br>MSCs, and Pass verdicts for L2CAP/ECFC/BV-22-C –<br>-25-C.<br>TSE 16083 (rating 4): Added new TC<br>L2CAP/COS/ECFC/BV-04-C; updated TCMT<br>accordingly.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **357 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 16780 (rating 2): To avoid forcing EATT PSM,<br>updated the initial condition (and in many cases the<br>MSC, test steps, and/or TC Config table) for the<br>following TCs: L2CAP/COS/ECFC/BV-01-C – -03-C;<br>L2CAP/ECFC/BV-01-C – -04-C and -06-C – -35-C,<br>and -38-C – -44-C; L2CAP/ECFC/BI-01-C – -08-C;<br>L2CAP/LE/CFC/BV-08-C – -10-C and -12-C, -13-C, -<br>15-C, -16-C, and -22-C – -31-C; L2CAP/LE/CFC/BI-<br>02-C; and L2CAP/LE/CID/BV-03-C and -04-C.<br>TSE 16954 (rating 3): Updated CID column, MSC, test<br>steps, and Pass verdict for section containing TCs<br>L2CAP/ECFC/BV-38-C and L2CAP/LE/CFC/BV-29-C.<br>TSE 16995 (rating 3): Corrected the initial condition,<br>MSC, test steps, and Pass verdict for TC<br>L2CAP/LE/CID/BI-01-C.<br>TSE 17086 (rating 2): Replaced the MSC for TC<br>L2CAP/ECFC/BV-29-C and updated the code number<br>in step 2 for the section containing TCs<br>L2CAP/LE/CFC/BV-23-C and L2CAP/ECFC/BV-30-C.<br>TSE 17340 (rating 2): Replaced MSCs for TCs<br>L2CAP/COS/CED/BV-12-C and -13-C and for sections<br>containing TCs L2CAP/LE/CFC/BV-30-C,<br>L2CAP/ECFC/BV-39-C, and -40-C and<br>L2CAP/LE/CFC/BV-31-C and L2CAP/ECFC/BV-41-C<br>and -42-C.<br>TSE 17401 (rating 2): Updated TCMT entry for<br>L2CAP/LE/CID/BI-01-C. Updated TCMT intro text to<br>align with latest template.<br>TSE 17463 (rating 4): Split ECFC tests by transport<br>where they are not currently specified as supported by<br>a single transport. Corrected the TCMT for the new<br>and updated ICS items for Enhanced Credit Based<br>Flow Control Mode – BR/EDR and LE transports.<br>Affected test cases: L2CAP/COS/ECFC/BV-01-C – -<br>04-C; L2CAP/ECFC/BV-01-C – -04-C, -06-C – -35-C, -<br>43-C, and -44-C; L2CAP/ECFC/BI-01-C – -07-C. New<br>test cases: L2CAP/COS/ECFC/BV-05-C – -08-C;<br>L2CAP/ECFC/BV-45-C – -79-C; and L2CAP/ECFC/BI-<br>10-C – -16-C. Updated TCMT accordingly.<br>TSE 17581 (rating 2): Updated the MSC, test steps,<br>and pass verdict for the section containing<br>L2CAP/ECFC/BV-38-C and L2CAP/LE/CFC/BV-29-C.<br>TSE 17905 (rating 1): Combined TCMT entries for<br>L2CAP/COS/CED/BV-03-C and -13-C.<br>Performed template-related formatting fixes. Updated<br>the introduction text before the TCMT to align with the<br>template and the copyright page to align with v2 of the<br>DNMD.|
|33|p33|2022-01-25|Approved by BTI on 2021-12-27. Prepared for<br>TCRL 2021-2publication.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **358 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||p33ed2r00–<br>r01|2022-02-15 –<br>2022-03-07|TSE 18240 (rating 1): Changed “LE-frame” and “LE<br>frame” to “K-frame” globally, including in descriptions<br>for TCs L2CAP/LE/CFC/BV-26-C – -28-C,<br>L2CAP/ECFC/BV-33-C – -35-C, and -76C – -78-C.<br>TSE 18241 (rating 1): Changed “Kframe” and “K-<br>Frame” to “K-frame” globally.<br>Performed template-related formatting fixes. Updated<br>the introduction text before the TCMT to align with the<br>revised template.|
||p33 edition 2|2022-03-07|Approved by BTI on 2022-03-07. Prepared for<br>edition 2publication.|
||p34r00–r04|2022-03-07 –<br>2022-05-04|TSE 17725 (rating 2): Updated the MSC, test<br>procedure, and expected outcome for<br>L2CAP/CLS/CID/BV-01-C.<br>TSE 17728 (rating 3): Deleted test case<br>L2CAP/COS/CID/BI-01-C as a standalone test;<br>combined it with L2CAP/LE/CID/BI-01-C to create a<br>table-driven test. Updated the test header, test<br>purpose, initial condition, MSC, test procedure, and<br>expected outcome and added a test case configuration<br>table for TCs L2CAP/COS/CID/BI-01-C and<br>L2CAP/LE/CID/BI-01-C. Updated TCMT items for<br>L2CAP/COS/CID/BI-01-C and L2CAP/LE/CID/BI-01-C.<br>TSE 18192 (rating 2): Updated test procedures (and in<br>some cases MSCs or test purposes) for test cases<br>L2CAP/COS/CED/BV-12-C and -13-C,<br>L2CAP/COS/CED/BI-02-C, L2CAP/COS/CFC/BV-01-<br>C and -03-C, L2CAP/LE/CFC/BV-31-C,<br>L2CAP/ECFC/BV-41-C and -42-C,<br>L2CAP/LE/CFC/BI-02-C, L2CAP/ECFC/BI-08-C and<br>-09-C, L2CAP/ERM/BI-01-C, and<br>L2CAP/COS/ECFC/BV-01-C, -02-C, -05-C, and -06-C<br>to eliminate ambiguities per Erratum 16187.<br>TSE 18242 (rating 2): Added a test case configuration<br>table and updated the test procedure for<br>L2CAP/LE/CFC/BV-30-C, L2CAP/ECFC/BV-39-C, and<br>-40-C. Added a TCC table and updated the initial<br>condition and MSC for L2CAP/LE/CFC/BV-31-C,<br>L2CAP/ECFC/BV-41-C, and -42-C. Added a TCC<br>table and updated the test procedure for<br>L2CAP/LE/CFC/BI-02-C and L2CAP/ECFC/BI-08-C.<br>Added a new TCC table and updated the existing TCC<br>table, initial condition, and MSC for<br>L2CAP/LE/CFC/BV-08-C, L2CAP/ECFC/BV-08-C, and<br>-65-C. Added a new TCC table and updated the initial<br>condition for L2CAP/LE/CFC/BV-09-C,<br>L2CAP/ECFC/BV-09-C, and -66-C. Added a TCC<br>table and updated the test procedure for<br>L2CAP/LE/CFC/BV-22-C, L2CAP/ECFC/BV-28-C, and<br>-72-C. Added a new TCC table and updated the initial<br>condition for L2CAP/LE/CFC/BV-23-C,<br>L2CAP/ECFC/BV-30-C, and -73-C. Added a new TCC<br>table and updated the test procedure for<br>L2CAP/LE/CFC/BV-24-C, L2CAP/ECFC/BV-31-C, and|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **359 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||-74-C. Added a new TCC table and updated the test<br>procedure for L2CAP/LE/CFC/BV-25-C,<br>L2CAP/ECFC/BV-32-C, and -75-C. Added a new TCC<br>table and updated the initial condition and MSC for<br>L2CAP/LE/CFC/BV-26-C, L2CAP/ECFC/BV-33-C, and<br>-76-C. Added a new TCC table and updated the initial<br>condition and MSC for L2CAP/LE/CFC/BV-27-C,<br>L2CAP/ECFC/BV-34-C, and -77-C. Added a new TCC<br>table for L2CAP/LE/CFC/BV-28-C,<br>L2CAP/ECFC/BV-35-C, and -78-C.<br>TSE 18295 (rating 2): Updated the initial condition and<br>test procedure and deleted the test conditions for<br>L2CAP/LE/CPU/BV-01-C.<br>TSE 18297 (rating 2): Updated the TCMT item for<br>L2CAP/ECFC/BV-68-C to replace L2CAP 1/5 AND<br>L2CAP 2/48b AND L2CAP 4/2 with L2CAP 1/1 AND<br>L2CAP 2/48a AND L2CAP 5/2.<br>TSE 18301 (rating 2): Updated the TCMT item for<br>L2CAP/LE/CID/BV-04-C to replace L2CAP 2/48 with<br>L2CAP 2/48a AND L2CAP 2/48b.<br>TSE 18384 (rating 2): Added new Sections 4.9,<br>Common Packet Contents, and 4.91, Fields and Bits<br>Reserved for Future Use.<br>TSE 18441 (rating 2): Modified initial condition of<br>L2CAP/COS/CFD/BV-11-C, adding a new IXIT value.<br>TSE 18544 (rating 1): Removed L2CAP/ECFC/BV-74-<br>C and -75-C; updated the TCMT and TCRL<br>accordingly.<br>Performed template-related formatting fixes. Made<br>consistencychecker editorials.|
|34|p34|2022-06-28|Approved by BTI on 2022-05-31. Prepared for<br>TCRL 2022-1publication.|
||p34ed2<br>r00–r01|2022-07-19 –<br>2022-08-17|TSE 18915 (rating 1): Standardized the various ways<br>ACL connections are described in the Initial Conditions<br>section for the following test cases:<br>L2CAP/COS/CED/BI-02-C; L2CAP/COS/CFC/BV-01-<br>C – -05-C; L2CAP/LE/CFC/BV-01-C – -31-C;<br>L2CAP/ECFC/BV-01-C – -04-C,<br>-06-C – -35-C, -38-C, -39-C, -42-C, -45-C – -73-C,<br>-76-C – -79-C; L2CAP/LE/CFC/BI-01-C and -02-C;<br>L2CAP/ECFC/BI-01-C – -16-C;<br>L2CAP/COS/ECFC/BV-01-C – -08-C; and<br>L2CAP/LE/REJ/BI-02-C.<br>Template-related editorials.|
||p34 edition 2|2022-08-23|Approved by BTI on 2022-08-22. Prepared for<br>edition 2publication.|
||p35r00|2022-08-24|TSE 18813 (rating 2): Deleted a test step for the<br>section containing L2CAP/ECFC/BI-03-C and -12-C.<br>TSE 18837 (rating 2): Updated the TCMT entries for<br>L2CAP/TIM/BV-02-C and -03-C.|
|35|p35|2023-02-07|Approved by BTI on 2022-12-28. Prepared for<br>TCRL 2022-2publication.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **360 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||p36r00|2023-04-03|TSE 19049 (rating 3): Updated the Test Purpose,<br>Initial Condition, MSC, test steps, and Pass verdict for<br>the section containing L2CAP/ECFC/BV-29-C and<br>-64-C.<br>TSE 22286 (rating 2): Updated a Reference and<br>added an Initial Condition for the section containing<br>L2CAP/TIM/BV-01-C – -03-C.|
|36|p36|2023-06-29|Approved by BTI on 2023-06-05. Prepared for<br>TCRL 2023-1publication.|
||p37r00–r06|2023-10-05 –<br>2024-05-12|TSE 17840 (rating 2): Corrected the TCMT entries for<br>L2CAP/TIM/BV-01-C – -03-C.<br>TSE 18351 (rating 3): Deleted L2CAP/ECFC/BV-44-C<br>and -51-C, revised L2CAP/ECFC/BV-69-C to also<br>cover what was previously covered under -44-C,<br>revised L2CAP/ECFC/BV-11-C to a standalone test,<br>revised the section containing L2CAP/LE/CFC/BV-13-<br>C and L2CAP/ECFC/BV-13-C, and revised<br>L2CAPECFC/BV-43-C. Updated the TCMT<br>accordingly.<br>TSE 22166 (rating 4): Deleted L2CAP/EXF/BV-01-C –<br>-06-C. Added new test L2CAP/EXP/BV-01-C. Updated<br>the TCMT accordingly.<br>TSE 23052 (rating 4): Per E23048, to address how the<br>absence of the FCS Option bit is handled, combined<br>L2CAP/FOC/BV-01-C – -03-C into one table-based<br>test section, updating the test purpose, initial condition,<br>MSC, and Pass verdict to align, and added new tests<br>L2CAP/FOC/BV-04-C and BV-05-C. Updated the<br>TCMT accordingly.<br>TSE 24849 (rating 2): Updated the description of<br>L2CAP/ECFC/BI-09-C to include BR/EDR and<br>updated the TCMT entry for L2CAP/LE/REJ/BI-01-C.<br>TSE 24929 (rating 2): Updated the MSCs for<br>L2CAP/ERM/BV-17-C and /BI-02-C.<br>TSE 24933 (rating 3): Combined L2CAP/COS/CED/BI-<br>01 and L2CAP/LE/REJ/BI-02-C into one section with a<br>test case configuration table. Updated the TCMT<br>accordingly.|
|37|p37|2024-07-01|Approved by BTI on 2024-05-22. Prepared for<br>TCRL 2024-1publication.|
||p38r00|2024-07-19|TSE 24934 (rating 1): Per E24985, deleted<br>L2CAP/LE/REJ/BI-01-C and updated the TCMT<br>accordingly.<br>TSE 25417 (rating 1): Corrected the IXIT reference for<br>L2CAP/COS/CED/BV-11-C in the initial condition,<br>MSC, and Notes.<br>TSE 25764 (rating 1): Corrected an ICS reference in<br>the Test Case Configuration table for<br>L2CAP/LE/REJ/BI-02-C.|
|38|p38|2024-09-04|Approved by BTI on 2024-08-14. Prepared for<br>TCRL 2024-2publication.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **361 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||p39r00–r07|2024-10-31 –<br>2024-12-14|TSE 17703 (rating 4): Deleted TCs<br>L2CAP/COS/CED/BV-05-C, -13-C, and BI-02-C and<br>the entire section previously containing<br>L2CAP/LE/CFC/BI-02-C and L2CAP/ECFC/BI-08-C.<br>Added new TCs L2CAP/COS/CED/BI-03-C – 17-C.<br>Updated the TC Configuration for<br>L2CAP/COS/CED/BI-09-C. Added column to the TC<br>Configuration table and updated the test procedure for<br>L2CAP/COS/CED/BI-10-C and -11-C. Updated the TC<br>description for L2CAP/COS/CED/BI-14-C. Updated the<br>TCMT accordingly.<br>TSE 25882 (rating 4): Updated the test case config<br>table and the MSC for the section containing<br>L2CAP/FOC/BV-01-C – -03-C. Converted<br>L2CAP/FOC/BV-04-C from a standalone test into a<br>table-based test and added new TC L2CAP/FOC/BV-<br>06-C; updated MSC and rounds table. Converted<br>L2CAP/FOC/BV-05-C from a standalone test into a<br>table-based test and added new TCs L2CAP/FOC/BV-<br>07-C and -08-C; updated MSC and rounds table.<br>Updated the TCMT accordingly; also updated TCMT<br>entries for L2CAP/OFS/BV-01-C – -08-C.<br>TSE 25886 (rating 1): Editorial corrections to the rev<br>history entries for TSEs 23052 and 24929.<br>TSE 25902 (rating 2): Updated the test case config<br>table, MSC, test steps, and Pass verdict for the section<br>containing L2CAP/COS/CED/BI-01-C and<br>L2CAP/LE/REJ/BI-02-C.<br>TSE 25922 (rating 1): Updated generic IXIT references<br>to use the TSPX naming for L2CAP/COS/CFD/BV-12-<br>C and -14-C, L2CAP/COS/CFC/BV-01-C – -05-C,<br>L2CAP/COS/ECFC/BV-01-C – -08-C,<br>L2CAP/ECFC/BI-01-C – -07-C, L2CAP/ECFC/BI-09-C<br>– -16-C, L2CAP/ECFC/BV-01-C – -04-C,<br>L2CAP/ECFC/BV-06-C – -27-C, L2CAP/ECFC/BV-29-<br>C – -35-C, L2CAP/ECFC/BV-38-C – -43-C,<br>L2CAP/ECFC/BV-45-C – -50-C, L2CAP/ECFC/BV-52-<br>C – -71-C, L2CAP/ECFC/BV-73-C, L2CAP/ECFC/BV-<br>76-C – L2CAP/ECFC/BV-79-C, L2CAP/ERM/BV-07-C,<br>L2CAP/LE/CFC/BI-01-C, L2CAP/LE/CFC/BV-01-C – -<br>13-C, L2CAP/LE/CFC/BV-15-C – -17-C,<br>L2CAP/LE/CFC/BV-20-C, L2CAP/LE/CFC/BV-23-C – -<br>31-C, and L2CAP/LE/CID/BV-01-C – -04-C.<br>TSE 26003 (rating 2): Updated the initial condition,<br>MSC, and test steps for L2CAP/ECFC/BI-09-C.<br>TSE 26416 (rating 2): Corrected the initial condition,<br>test steps, MSC, and Pass verdict for the section<br>containingL2CAP/ECFC/BI-02-C and -11-C.|
|39|p39|2025-02-18|Approved by BTI on 2024-12-26. Prepared for<br>TCRL 2025-1publication.|
||p40r00–r03|2025-02-03 –<br>2025-03-27|TSE 17651 (rating 4): Added new TCs<br>L2CAP/EXF/BV-08-C and L2CAP/FIX/BV-03-C to<br>address a gap in feature masks testing. Updated the<br>TCMT accordingly.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **362 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 24756 (rating 4): Added new TCs<br>L2CAP/LE/CFC/BV-32-C and L2CAP/ECFC/BV-80-C<br>and -81-C to address the correct handling of a K-frame<br>with SDU-length octets of data. Updated the TCMT<br>accordingly.<br>TSE 26629 (rating 2): Replaced the MSC for the<br>section containing L2CAP/FOC/BV-05-C, -07-C, and<br>-08-C.<br>Per the BTI call on 2025-04-24, removed a broken<br>cross-reference in L2CAP/COS/CED/BV-12-C by<br>deleting unneeded introductory text in the test<br>procedure “The testing procedure is executed similar<br>to**Reference source not found.**, with the exception<br>that each transmission (C-frame) from the Lower<br>Tester is fragmented into two fragments.” (the error<br>text previously referred to the now-deleted<br>L2CAP/COS/CED/BV-05-C).|
|40|p40|2025-05-06|Approved by BTI on 2025-04-16. Prepared for<br>TCRL 2025-2publication.|
||p41r00–r09|2025-07-16 –<br>2025-09-11|TSE 26118 (rating 2): Deleted L2CAP/ECFC/BV-43-C<br>and L2CAP/ECFC/BV-69-C. Updated the TCMT<br>accordingly.<br>TSE 26689 (rating 3): Corrected the Pass verdict for<br>L2CAP/COS/CED/BV-08-C.<br>TSE 27163 (rating 4): To support the changes needed<br>for E26667, added new TCs L2CAP/COS/CED/BI-28-<br>C and -29-C. Updated the TCMT accordingly.<br>TSE 27216 (rating 2): Corrected an error code for<br>L2CAP/LE/REJ/BI-02-C.<br>TSE 27265 (rating 2): Updated the TCMT entries for<br>L2CAP/COS/CED/BI-03-C, L2CAP/COS/CID/BI-01-C,<br>and L2CAP/LE/CID/BI-01-C.<br>TSE 27274 (rating 2): Corrected values in the test<br>procedure for L2CAP/COS/CED/BI-06-C.<br>TSE 27281 (rating 2): Added a column to the test case<br>configuration table and updated the Test Procedure for<br>for L2CAP/COS/CED/BI-14-C – -15-C.<br>TSE 27414 (rating 2): Corrected the Pass verdict for<br>the section containing L2CAP/COS/CED/BI-10-C and<br>-11-C.<br>TSE 27460 (rating 2): Updated IXIT values throughout<br>the TS. Replaced the Setup Preamble section with the<br>Preamble IXITs table. Deleted Notes for<br>L2CAP/COS/CED/BV-11-C. Updated the Initial<br>Condition and Pass Verdict for L2CAP/COS/CFD/BV-<br>11-C. Updated the Initial Condition and Test<br>Procedure for the section containing<br>L2CAP/COS/ECFC/BV-03-C and -07-C. Updated the<br>Initial Condition for L2CAP/ECFC/BI-09-C,<br>L2CAP/ERM/BV-23-C, L2CAP/STM/BV-03-C and -13-<br>C, and L2CAP/ECF/BV-08-C.|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **363 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
||||TSE 27592 (rating 2): Updated the test purpose, MSC,<br>test procedure, and Pass verdict for the section<br>containing L2CAP/ECFC/BI-02-C and<br>L2CAP/ECFC/BI-11-C.<br>TSE 27636 (rating 4): Updated the section containing<br>L2CAP/COS/CED/BI-04-C and -05-C, enhancing the<br>description of -05-C, adding new tests<br>L2CAP/COS/CED/BI-18-C and -19-C to the TCC, and<br>making minor changes to the test procedure. Updated<br>the section containing L2CAP/COS/CED/BI-08-C and -<br>09-C, enhancing the description of -09-C, adding new<br>tests L2CAP/COS/CED/BI-20-C and -21-C to the TCC,<br>and making minor changes to the test procedure.<br>Converted L2CAP/COS/CED/BI-13-C into a table-<br>based test with new TCs L2CAP/COS/CED/BI-22-C<br>and -23-C, enhancing the description of -13-C and<br>making minor changes to the test procedure. Updated<br>the section containing L2CAP/COS/CED/BI-16-C and -<br>17-C, enhancing both test descriptions, expanding the<br>scope of the TCC with new columns, adding new tests<br>L2CAP/COS/CED/BI-24-C and -25-C to the TCC, and<br>making minor changes to the test procedure and test<br>purpose. Updated the TCMT accordingly.<br>TSE 27644 (rating 3): Updated the test procedure and<br>Pass verdict for L2CAP/COS/CED/BI-12-C.|
|41|p41|2025-11-04|Approved by BTI on 2025-10-05. Prepared for TCRL<br>pkg101publication.|

## _**Acknowledgments**_

|**Name**|**Company**|
|Virgil Dragomir|Bluetooth SIG, Inc.|
|Alicia Courtney|Broadcom|
|Leonid Eidelman|Broadcom|
|Ash Kapur|Broadcom|
|Angel Polo|Broadcom|
|Mayank Batra|CSR|
|Chris Church|CSR|
|GirirajGoyal|CSR|
|Robin Heydon|CSR|
|Tim Howes|CSR|
|Neil Stewart|CSR|
|Harish Balasubramaniam|Intel|
|Magnus Eriksson|Intel|
|Oren Haggai|Intel|
|Marcel Holtmann|Intel|
|Robert Hughes|Intel|
|Yao Wang|IVT|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **364 of 365**

**Logical Link Control and Adaptation Protocol (L2CAP) /** Test Suite

|**Name**|**Company**|
|Josselin De La Broise|Marvell|
|Anindya Bakshi|Mindtree|
|Shwetha Madadik|Mindtree|
|Krishna Singala|Mindtree|
|Niclas Granqvist|Polar|
|Joel Linsky|Qualcomm Atheros|
|Brian A. Redding|Qualcomm Atheros|
|Magnus Sommansson|Qualcomm Technologies International, Ltd.|
|Jean-Philippe Lambert|RivieraWaves|
|Rasmus Abildgren|SamsungElectronics|
|Jason Hillyard|Wicentric|

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary

Page **365 of 365**
