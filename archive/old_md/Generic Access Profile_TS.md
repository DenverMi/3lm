## **Generic Access Profile (GAP)** 

## _**Bluetooth[®]**_ **Test Suite** 

- **Revision:** GAP.TS.p49 

- **Revision Date:** 2025-11-04 

- **Prepared By:** BTI 

- **Published during TCRL:** TCRL.pkg101 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

**Generic Access Profile (GAP)  /** Test Suite 

**This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.** 

**THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.** 

**TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.** 

**This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.** 

**This document is subject to change without notice.** 

**Copyright © 2003–2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.** 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **2 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **Contents** 

|**1**|**Scope ................................................................................................................................................... 12**|**Scope ................................................................................................................................................... 12**|
|---|---|---|
|**2**|**References, definitions, and abbreviations ..................................................................................... 13**||
||2.1|References .................................................................................................................................. 13|
||2.2|Definitions ................................................................................................................................... 14|
|**3**|**Test**|**Suite Structure (TSS) ................................................................................................................. 15**|
||3.1|Test Strategy ............................................................................................................................... 15|
||3.2|Test groups ................................................................................................................................. 15|
||3.2.1|BR/EDR Protocol groups ...................................................................................................................... 15|
||3.2.2|LE Only Protocol groups ....................................................................................................................... 15|
||3.2.3|BR/EDR/LE (Dual Mode) Protocol groups ............................................................................................ 16|
||3.2.4|Main test groups ................................................................................................................................... 17|
|**4**|**Test**|**cases (TC) ................................................................................................................................... 18**|
||4.1|Introduction ................................................................................................................................. 18|
||4.1.1|Test case identification conventions ..................................................................................................... 18|
||4.1.2|Conformance ........................................................................................................................................ 19|
||4.1.3|Pass/Fail verdict conventions ............................................................................................................... 20|
||4.2|Preambles ................................................................................................................................... 20|
||4.2.1|Link Establishment Lower Tester Started (for generic authentication) .................................................. 20|
||4.2.2|Inquiry procedure .................................................................................................................................. 21|
||4.2.3|Paging procedure .................................................................................................................................. 22|
||4.2.4|Bring IUT to Link Key Available ............................................................................................................ 23|
||4.2.5|Secure Simple Pairing .......................................................................................................................... 24|
||4.2.6|GAP Mandatory Characteristics ............................................................................................................ 25|
||4.3|Common Packet Contents .......................................................................................................... 25|
||4.3.1|Fields and Bits Reserved for Future Use .............................................................................................. 25|
||4.4|Modes ......................................................................................................................................... 25|
||4.4.1|Non-discoverable bondable mode – Peripheral .................................................................................... 25|
||GAP/MOD/NDIS/BV-01-C [Non-discoverable mode – Peripheral] ........................................................................ 25||
||4.4.2|Limited Discoverable mode – Peripheral .............................................................................................. 26|
||GAP/MOD/LDIS/BV-01-C [Limited Discoverable mode and LIAC – Peripheral] ................................................... 26||
||GAP/MOD/LDIS/BV-02-C [Limited Discoverable mode and GIAC – Peripheral] .................................................. 27||
||GAP/MOD/LDIS/BV-03-C [Limited Discovery mode time-out] .............................................................................. 28||
||4.4.3|General Discoverable mode – Peripheral ............................................................................................. 29|
||GAP/MOD/GDIS/BV-01-C [General Discoverable mode and GIAC – Peripheral] ................................................ 29||
||GAP/MOD/GDIS/BV-02-C [General Discoverable mode and LIAC – Peripheral] ................................................. 30||
||4.4.4|Non-connectable mode – Peripheral ..................................................................................................... 31|
||GAP/MOD/NCON/BV-01-C [Non-connectable mode – Peripheral] ....................................................................... 31||
||4.4.5|Connectable mode – Peripheral ........................................................................................................... 32|
||GAP/MOD/CON/BV-01-C [Connectable mode – Peripheral] ................................................................................ 32||
||4.4.6|Non-bondable mode – Peripheral ......................................................................................................... 33|
||GAP/MOD/NBON/BV-02-C [Non-bondable mode, IUT rejects pairing procedure] ................................................ 33||
||GAP/MOD/NBON/BV-03-C [Non-bondable mode, IUT accepts a non-bonded connection] ................................. 35||
||4.4.7|Pairing mode – Peripheral .................................................................................................................... 36|
||4.4.8|Non-synchronizable mode – Connectionless Peripheral Broadcaster .................................................. 36|
||GAP/MOD/NSYN/BV-01-C [Non-synchronizable mode, IUT is Connectionless Peripheral Broadcast||
||Transmitter] ........................................................................................................................................................... 36||



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **3 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|4.4.9<br>Synchronizable mode – Connectionless Peripheral Broadcaster ......................................................... 37|
|---|
|GAP/MOD/SYN/BV-01-C [Synchronizable mode – IUT is Connectionless Peripheral Broadcast|
|Transmitter] ........................................................................................................................................................... 37|
|4.5<br>Security aspects .......................................................................................................................... 38|
|4.5.1<br>BR/EDR security modes – Peripheral ................................................................................................... 38|
|GAP/SEC/SEM/BV-02-C [Channel Establishment procedure – Security mode 2] ................................................ 38|
|GAP/SEC/SEM/BV-04-C [Security mode 4 – Responder] .................................................................................... 39|
|GAP/SEC/SEM/BV-11-C [Secure Connections Only mode BR/EDR transport – IUT Peripheral,|
|responder, Lower Tester doesn’t support Secure Connections in Controller] ....................................................... 41|
|GAP/SEC/SEM/BV-12-C [Secure Connections Only mode BR/EDR transport – IUT Peripheral,|
|responder, Lower Tester doesn’t support Secure Connections in Host] ............................................................... 42|
|GAP/SEC/SEM/BI-01-C [Security mode 2 BR/EDR Transport, Responder – Invalid Encryption Key Size] .......... 44|
|GAP/SEC/SEM/BI-11-C [Security mode 4 level 1, Responder – Invalid Encryption Key Size] ............................. 45|
|GAP/SEC/SEM/BI-02-C [Security mode 4 level 2, Responder – Invalid Encryption Key Size] ............................. 45|
|GAP/SEC/SEM/BI-03-C [Security mode 4 level 3, Responder – Invalid Encryption Key Size] ............................. 45|
|GAP/SEC/SEM/BI-04-C [Security mode 4 level 4, Responder – Invalid Encryption Key Size – 128 bit] .............. 46|
|GAP/SEC/SEM/BI-14-C [Security mode 4 level 1, Responder – Invalid Encryption Key Size – 128 bit] .............. 46|
|GAP/SEC/SEM/BI-15-C [Security mode 4 level 2, Responder – Invalid Encryption Key Size – 128 bit] .............. 46|
|GAP/SEC/SEM/BI-16-C [Security mode 4 level 3, Responder – Invalid Encryption Key Size – 128 bit] .............. 46|
|GAP/SEC/SEM/BI-05-C [Security mode 2, Initiator – Invalid Key Size] ................................................................ 47|
|GAP/SEC/SEM/BI-12-C [Security mode 4 level 1, Initiator – Invalid Encryption Key Size] ................................... 49|
|GAP/SEC/SEM/BI-06-C [Security mode 4 level 2, Initiator – Invalid Encryption Key Size] ................................... 49|
|GAP/SEC/SEM/BI-07-C [Security mode 4 level 3, Initiator – Invalid Encryption Key Size] ................................... 49|
|GAP/SEC/SEM/BI-08-C [Security mode 4 level 4, Initiator – Invalid Encryption Key Size – 128 bit] .................... 49|
|GAP/SEC/SEM/BI-17-C [Security mode 4 level 1, Initiator – Invalid Encryption Key Size – 128 bit] .................... 49|
|GAP/SEC/SEM/BI-18-C [Security mode 4 level 2, Initiator – Invalid Encryption Key Size – 128 bit] .................... 49|
|GAP/SEC/SEM/BI-19-C [Security mode 4 level 3, Initiator – Invalid Encryption Key Size – 128 bit] .................... 49|
|GAP/SEC/SEM/BI-24-C [Security mode 4, Unencrypted connections rejected – Responder] .............................. 50|
|GAP/SEC/SEM/BV-13-C ...................................................................................................................................... 52|
|GAP/SEC/SEM/BV-47-C ...................................................................................................................................... 52|
|GAP/SEC/SEM/BV-14-C ...................................................................................................................................... 54|
|GAP/SEC/SEM/BV-48-C ...................................................................................................................................... 54|
|GAP/SEC/SEM/BV-15-C ...................................................................................................................................... 56|
|GAP/SEC/SEM/BV-49-C ...................................................................................................................................... 56|
|4.5.2<br>LE security modes – Peripheral ............................................................................................................ 58|
|GAP/SEC/SEM/BV-21-C [LE security mode: mode 1 level 4, Peripheral – outgoing service level|
|connection] ............................................................................................................................................................ 58|
|GAP/SEC/SEM/BV-37-C [LE Secure Connections Only: mode 1 level 2, Peripheral – outgoing service|
|level connection] ................................................................................................................................................... 58|
|GAP/SEC/SEM/BV-38-C [LE Secure Connections Only: mode 1 level 3, Peripheral – outgoing service|
|level connection] ................................................................................................................................................... 58|
|GAP/SEC/SEM/BV-22-C [LE security mode: mode 1 level 4, Peripheral – incoming service level|
|connection] ............................................................................................................................................................ 60|
|GAP/SEC/SEM/BV-39-C [LE Secure Connections Only: mode 1 level 2, Peripheral – incoming service|
|level connection] ................................................................................................................................................... 60|
|GAP/SEC/SEM/BV-40-C [LE Secure Connections Only: mode 1 level 3, Peripheral – incoming service|
|level connection] ................................................................................................................................................... 60|
|GAP/SEC/SEM/BV-23-C [Secure Connections Only mode LE transport – failed procedure, Peripheral –|
|outgoing service level connection] ........................................................................................................................ 62|
|GAP/SEC/SEM/BV-24-C [Secure Connections Only mode LE transport – failed procedure, Peripheral –|
|incoming service level connection] ........................................................................................................................ 63|
|GAP/SEC/SEM/BV-25-C [Secure Connections Only mode LE transport, Peripheral, Failure, BR/EDR|
|and LE transports] ................................................................................................................................................. 66|
|GAP/SEC/SEM/BI-09-C [LE security mode 1 level 4, Peripheral – Invalid Encryption Key Size].......................... 68|
|GAP/SEC/SEM/BI-20-C [Security mode 1 level 3, Peripheral – Invalid Encryption Key Size] .............................. 68|
|GAP/SEC/SEM/BI-21-C [Security mode 1 level 2, Peripheral – Invalid Encryption Key Size] .............................. 68|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **4 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|4.5.3<br>BR/EDR security modes – Central ........................................................................................................ 69|
|---|
|GAP/SEC/SEM/BV-05-C ...................................................................................................................................... 69|
|GAP/SEC/SEM/BV-50-C ...................................................................................................................................... 69|
|GAP/SEC/SEM/BV-06-C ...................................................................................................................................... 70|
|GAP/SEC/SEM/BV-51-C ...................................................................................................................................... 70|
|GAP/SEC/SEM/BV-07-C ...................................................................................................................................... 72|
|GAP/SEC/SEM/BV-52-C ...................................................................................................................................... 72|
|GAP/SEC/SEM/BV-08-C [Security mode 4 – Initiator] .......................................................................................... 73|
|GAP/SEC/SEM/BV-09-C ...................................................................................................................................... 74|
|GAP/SEC/SEM/BV-53-C ...................................................................................................................................... 74|
|GAP/SEC/SEM/BV-10-C ...................................................................................................................................... 77|
|GAP/SEC/SEM/BV-46-C ...................................................................................................................................... 77|
|GAP/SEC/SEM/BV-16-C [Secure Connections Only mode – IUT Central, initiator, Lower Tester doesn’t|
|support Secure Connections in Controller]............................................................................................................ 79|
|GAP/SEC/SEM/BV-17-C [Secure Connections Only mode – IUT Central, initiator, Lower Tester doesn’t|
|support Secure Connections in Host] .................................................................................................................... 80|
|GAP/SEC/SEM/BV-18-C ...................................................................................................................................... 82|
|GAP/SEC/SEM/BV-54-C ...................................................................................................................................... 82|
|GAP/SEC/SEM/BV-19-C ...................................................................................................................................... 83|
|GAP/SEC/SEM/BV-55-C ...................................................................................................................................... 83|
|GAP/SEC/SEM/BV-20-C [IUT Central, initiator, not in Secure Connections Only mode BR/EDR|
|transport, Lower Tester does not support Secure Connections in Host, level 4 service] ...................................... 85|
|4.5.4<br>LE security modes – Central ................................................................................................................. 86|
|GAP/SEC/SEM/BV-26-C [LE security mode: mode 1 level 4, Central – outgoing service level|
|connection] ............................................................................................................................................................ 86|
|GAP/SEC/SEM/BV-41-C [LE Secure Connections Only: mode 1 level 2, Central – outgoing service level|
|connection] ............................................................................................................................................................ 86|
|GAP/SEC/SEM/BV-42-C [LE Secure Connections Only: mode 1 level 3, Central – outgoing service level|
|connection] ............................................................................................................................................................ 86|
|GAP/SEC/SEM/BV-27-C [LE security mode: mode 1 level 4, Central – incoming service level|
|connection] ............................................................................................................................................................ 88|
|GAP/SEC/SEM/BV-43-C [LE Secure Connections Only: mode 1 level 2, Central – incoming service|
|level connection] ................................................................................................................................................... 88|
|GAP/SEC/SEM/BV-44-C [LE Secure Connections Only: mode 1 level 3, Central – incoming service|
|level connection] ................................................................................................................................................... 88|
|GAP/SEC/SEM/BV-28-C [Secure Connections Only mode LE transport – failed procedure, Central –|
|outgoing service level connection] ........................................................................................................................ 90|
|GAP/SEC/SEM/BV-29-C [Secure Connections Only mode LE transport – failed procedure, Central –|
|incoming service level connection] ........................................................................................................................ 91|
|GAP/SEC/SEM/BV-30-C [Secure Connections Only mode, Central, failure, BR/EDR and LE transports] ........... 93|
|GAP/SEC/SEM/BI-10-C [LE security mode 1 level 4, Central – Invalid Encryption Key Size] .............................. 95|
|GAP/SEC/SEM/BI-22-C [LE security mode 1 level 3, Central – Invalid Encryption Key Size] .............................. 95|
|GAP/SEC/SEM/BI-23-C [LE security mode 1 level 2, Central – Invalid Encryption Key Size] .............................. 95|
|4.5.5<br>LE security modes – Both connected roles ........................................................................................... 96|
|GAP/SEC/SEM/BV-56-C [Incoming GATT indication, LE security mode 1 level 2, Peripheral] ............................ 96|
|GAP/SEC/SEM/BV-62-C [Incoming GATT indication, LE security mode 1 level 2, Central] ................................. 96|
|GAP/SEC/SEM/BV-57-C [Incoming GATT indication, LE security mode 1 level 3, Peripheral] .......................... 100|
|GAP/SEC/SEM/BV-63-C [Incoming GATT indication, LE security mode 1 level 3, Central] ............................... 100|
|GAP/SEC/SEM/BV-58-C [LE Secure Connections Only – Incoming GATT indication, Peripheral] .................... 104|
|GAP/SEC/SEM/BV-64-C [LE Secure Connections Only – Incoming GATT indication, Central] ......................... 104|
|GAP/SEC/SEM/BV-59-C [Incoming GATT notification, LE security mode 1 level 2, Peripheral] ........................ 108|
|GAP/SEC/SEM/BV-65-C [Incoming GATT notification, LE security mode 1 level 2, Central] ............................. 108|
|GAP/SEC/SEM/BV-60-C [Incoming GATT notification, LE security mode 1 level 3, Peripheral] ........................ 111|
|GAP/SEC/SEM/BV-66-C [Incoming GATT notification, LE security mode 1 level 3, Central] ............................. 111|
|GAP/SEC/SEM/BV-61-C [LE Secure Connections Only, Incoming GATT notification, Peripheral] .................... 114|
|GAP/SEC/SEM/BV-67-C [LE Secure Connections Only, Incoming GATT notification, Central] ......................... 114|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **5 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|4.5.6<br>Security modes – Observer role.......................................................................................................... 117|
|---|
|GAP/SEC/SEM/BV-31-C .................................................................................................................................... 117|
|GAP/SEC/SEM/BV-32-C .................................................................................................................................... 117|
|GAP/SEC/SEM/BI-13-C [LE security mode 3 – Observer, Reject Lower Level Security] ................................... 118|
|GAP/SEC/SEM/BV-45-C [Re-pair or stop a connection attempt when a connection fails due to failed|
|encryption, LE security mode 1 level 4] .............................................................................................................. 118|
|4.5.7<br>Security modes – Broadcaster role ..................................................................................................... 121|
|GAP/SEC/SEM/BV-34-C .................................................................................................................................... 121|
|GAP/SEC/SEM/BV-35-C .................................................................................................................................... 121|
|4.5.8<br>Security modes – Both connected roles .............................................................................................. 122|
|GAP/SEC/SEM/BI-25-C [Security mode 4 level 2 – Initiator, Encryption Not Enabled] ....................................... 122|
|GAP/SEC/SEM/BI-26-C [Security mode 4 level 3 – Initiator, Encryption Not Enabled] ....................................... 122|
|GAP/SEC/SEM/BI-27-C [Security mode 4 level 4 – Initiator, Encryption Not Enabled] ....................................... 122|
|GAP/SEC/SEM/BI-28-C [Security mode 4 level 2 – Initiator, Connectionless Channel, Unicast Data,|
|Encryption Not Enabled] ..................................................................................................................................... 124|
|GAP/SEC/SEM/BI-29-C [Security mode 4 level 3 – Initiator, Connectionless Channel, Unicast Data,|
|Encryption Not Enabled] ..................................................................................................................................... 124|
|GAP/SEC/SEM/BI-30-C [Security mode 4 level 4 – Initiator, Connectionless Channel, Unicast Data,|
|Encryption Not Enabled] ..................................................................................................................................... 124|
|GAP/SEC/SEM/BI-31-C [Security mode 4 level 4, Secure Connections – Responder, Insufficient|
|Encryption Type] ................................................................................................................................................. 125|
|GAP/SEC/SEM/BI-32-C [Security mode 4 level 4, Secure Connections – Initiator, Channel|
|Establishment, Insufficient Encryption Type]....................................................................................................... 126|
|GAP/SEC/SEM/BI-33-C [Security mode 4, Secure Connections – Initiator, Connectionless Channel,|
|Unicast Data, Insufficient Encryption Type]......................................................................................................... 128|
|4.5.9<br>Channel Sounding .............................................................................................................................. 130|
|GAP/SEC/SEM/BV-69-C [Channel Sounding Security, CS Security L1, Peripheral, Initiator] ............................ 130|
|GAP/SEC/SEM/BV-70-C [Channel Sounding Security, CS Security L2, Peripheral, Initiator] ............................ 130|
|GAP/SEC/SEM/BV-71-C [Channel Sounding Security, CS Security L3, Peripheral, Initiator] ............................ 130|
|GAP/SEC/SEM/BV-72-C [Channel Sounding Security, CS Security L4, Peripheral, Initiator] ............................ 130|
|GAP/SEC/SEM/BV-73-C [Channel Sounding Security, CS Security L1, Peripheral, Reflector] .......................... 130|
|GAP/SEC/SEM/BV-74-C [Channel Sounding Security, CS Security L2, Peripheral, Reflector] .......................... 130|
|GAP/SEC/SEM/BV-75-C [Channel Sounding Security, CS Security L3, Peripheral, Reflector] .......................... 130|
|GAP/SEC/SEM/BV-76-C [Channel Sounding Security, CS Security L4, Peripheral, Reflector] .......................... 130|
|4.6<br>Idle mode procedures ............................................................................................................... 131|
|4.6.1<br>General Inquiry – Central .................................................................................................................... 131|
|GAP/IDLE/GIN/BV-01-C [General Inquiry – IUT is Central] ................................................................................ 131|
|4.6.2<br>Device Name during General Inquiry .................................................................................................. 132|
|GAP/IDLE/DNDIS/BV-01-C [Device Name During General Inquiry – IUT is Peripheral] ..................................... 132|
|4.6.3<br>Limited Inquiry – Central ..................................................................................................................... 133|
|GAP/IDLE/LIN/BV-01-C [Limited Inquiry – IUT is Central] .................................................................................. 133|
|4.6.4<br>Device Discovery – Central ................................................................................................................. 135|
|GAP/IDLE/DED/BV-02-C [Device Discovery and Name Discovery – Secure Simple Pairing Supported|
|by IUT] ................................................................................................................................................................ 135|
|4.6.5<br>Bonding – Central ............................................................................................................................... 136|
|GAP/IDLE/BON/BV-02-C [Bonding – Central] .................................................................................................... 136|
|4.6.6<br>Dedicated Bonding test cases ............................................................................................................ 138|
|GAP/IDLE/BON/BV-03-C [Dedicated Bonding] ................................................................................................... 138|
|GAP/IDLE/BON/BV-04-C [Dedicated Bonding – Authenticated Link Key] .......................................................... 140|
|4.6.7<br>General Bonding test cases ................................................................................................................ 142|
|GAP/IDLE/BON/BV-05-C [General Bonding] ...................................................................................................... 142|
|GAP/IDLE/BON/BV-06-C [General Bonding – Authenticated Link Key] .............................................................. 144|
|4.6.8<br>Link Establishment – Central .............................................................................................................. 146|
|GAP/EST/LIE/BV-02-C [Link Establishment – Initiator] ....................................................................................... 146|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **6 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|4.7<br>Operational modes and procedures for use on LE physical channels ..................................... 148|
|---|
|4.7.1<br>Broadcasting and Observing ............................................................................................................... 148|
|GAP/BROB/BCST/BV-01-C [Broadcast mode, No Scan Response] .................................................................. 148|
|GAP/BROB/BCST/BV-02-C [Broadcast mode, Scan Response] ........................................................................ 149|
|GAP/BROB/BCST/BV-03-C [Broadcast mode, Resolvable Private Address] ..................................................... 150|
|GAP/BROB/BCST/BV-04-C [Broadcast mode, Non-Resolvable Private Address] ............................................. 151|
|GAP/BROB/BCST/BV-05-C [Broadcast mode, Resolvable Private Address, Scan Response] .......................... 152|
|GAP/BROB/OBSV/BV-01-C [Observation procedure, Passive Scanning] .......................................................... 154|
|GAP/BROB/OBSV/BV-02-C [Observation procedure, Active Scanning] ............................................................. 155|
|GAP/BROB/OBSV/BV-05-C [Observation procedure, Active Scanning Non-Resolvable Private Address|
|or Resolvable Private Address] ........................................................................................................................... 156|
|GAP/BROB/OBSV/BV-06-C [Observation procedure with Active Scanning, IUT and Peer using|
|Resolvable Private Address] ............................................................................................................................... 157|
|4.7.2<br>Discovery modes and procedures....................................................................................................... 159|
|GAP/DISC/NONM/BV-01-C [Non-Discoverable mode, Non-Connectable mode] ............................................... 159|
|GAP/DISC/NONM/BV-02-C [Non-Discoverable mode, Undirected Connectable mode] ..................................... 160|
|GAP/DISC/LIMM/BV-01-C [Limited Discoverable mode, Non-Connectable mode – BR/EDR/LE] ...................... 161|
|GAP/DISC/LIMM/BV-02-C [Limited Discoverable mode, Undirected Connectable mode – BR/EDR/LE] ........... 162|
|GAP/DISC/LIMM/BV-03-C [Limited Discoverable mode, Non-Connectable mode – LE Only] ............................ 164|
|GAP/DISC/LIMM/BV-04-C [Limited Discoverable mode, Undirected Connectable mode – LE Only] ................. 165|
|GAP/DISC/GENM/BV-01-C [General Discoverable mode, Non-Connectable mode – BR/EDR/LE] ................... 167|
|GAP/DISC/GENM/BV-02-C [General Discoverable mode, Undirected Connectable mode – BR/EDR/LE] ........ 168|
|GAP/DISC/GENM/BV-03-C [General Discoverable mode, Non-Connectable mode – LE Only] ......................... 169|
|GAP/DISC/GENM/BV-04-C [General Discoverable mode, Undirected Connectable mode – LE Only] .............. 170|
|GAP/DISC/LIMP/BV-01-C [Limited Discovery procedure, find Limited Discoverable device] ............................. 171|
|GAP/DISC/LIMP/BV-02-C [Limited Discovery procedure does not find General Discoverable device] .............. 172|
|GAP/DISC/LIMP/BV-03-C [Limited Discovery procedure does not find Broadcast device] ................................. 173|
|GAP/DISC/LIMP/BV-04-C [Limited Discovery procedure does not find Undirected Connectable device] .......... 174|
|GAP/DISC/LIMP/BV-05-C [Limited Discovery procedure does not find Directed Connectable device] .............. 175|
|GAP/DISC/GENP/BV-01-C [General Discovery procedure, finding General Discoverable device] .................... 176|
|GAP/DISC/GENP/BV-02-C [General Discovery procedure, finding Limited Discoverable device] ...................... 177|
|GAP/DISC/GENP/BV-03-C [General Discovery procedure does not find Broadcast device] .............................. 178|
|GAP/DISC/GENP/BV-04-C [General Discovery procedure does not find Undirected Connectable|
|device] ................................................................................................................................................................ 179|
|GAP/DISC/GENP/BV-05-C [General Discovery procedure does not find Directed Connectable device] ........... 180|
|GAP/IDLE/NAMP/BV-01-C [Name Discovery procedure, GATT Client] ............................................................. 181|
|GAP/IDLE/NAMP/BV-02-C [Name Discovery procedure, GATT Server] ............................................................ 182|
|GAP/DISC/RPA/BV-01-C [Discovery procedure, find discoverable device using Resolvable Private|
|Address] .............................................................................................................................................................. 183|
|4.7.3<br>Connection modes and procedures .................................................................................................... 184|
|GAP/CONN/NCON/BV-01-C [Non-Connectable mode] ...................................................................................... 184|
|GAP/CONN/NCON/BV-02-C [Non-Connectable mode, General Discoverable mode] ........................................ 185|
|GAP/CONN/NCON/BV-03-C [Non-Connectable mode, Limited Discoverable mode] ......................................... 186|
|GAP/CONN/DCON/BV-01-C [Directed Connectable mode] ............................................................................... 187|
|GAP/CONN/DCON/BV-04-C [Directed Connectable mode, Privacy, Resolvable Private Address,|
|Central Address Resolution] ............................................................................................................................... 188|
|GAP/CONN/DCON/BV-05-C [Directed Connectable mode, Privacy, Resolvable Private Address,|
|Central Address Resolution not supported]......................................................................................................... 190|
|GAP/CONN/UCON/BV-01-C [Undirected Connectable mode, Non-Discoverable mode] ................................... 191|
|GAP/CONN/UCON/BV-02-C [Undirected Connectable mode, General Discoverable mode] ............................. 192|
|GAP/CONN/UCON/BV-03-C [Undirected Connectable mode, Limited Discoverable mode] .............................. 193|
|GAP/CONN/UCON/BV-06-C [Undirected Connectable mode, Resolvable Private Address] ............................. 194|
|GAP/CONN/ACEP/BV-01-C [Auto Connection Establishment procedure, Directed Connectable mode] ........... 195|
|GAP/CONN/ACEP/BV-03-C [Auto Connection Establishment procedure, Directed Connectable mode,|
|Resolvable Private Address, Central Address Resolution] ................................................................................. 196|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **7 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|GAP/CONN/ACEP/BV-04-C [Auto Connection Establishment procedure, Undirected Connectable|
|---|
|mode, Resolvable Private Address] .................................................................................................................... 197|
|GAP/CONN/GCEP/BV-01-C [General Connection Establishment procedure, Directed Connectable|
|mode] .................................................................................................................................................................. 198|
|GAP/CONN/GCEP/BV-02-C [General Connection Establishment procedure, Undirected Connectable|
|mode] .................................................................................................................................................................. 199|
|GAP/CONN/GCEP/BV-05-C [General Connection Establishment procedure, Directed Connectable|
|mode, Resolvable Private Address, Central Address Resolution] ....................................................................... 200|
|GAP/CONN/GCEP/BV-06-C [General Connection Establishment procedure, Undirected Connectable|
|mode, Resolvable Private Address] .................................................................................................................... 201|
|GAP/CONN/SCEP/BV-01-C [Selective Connection Establishment procedure, Directed Connectable|
|mode] .................................................................................................................................................................. 202|
|GAP/CONN/SCEP/BV-03-C [Selective Connection Establishment procedure, Directed Connectable|
|mode, Resolvable Private Address, Central Address Resolution] ....................................................................... 203|
|GAP/CONN/DCEP/BV-01-C [Direct Connection Establishment procedure, Directed Connectable mode] ......... 204|
|GAP/CONN/DCEP/BV-03-C [Direct Connection Establishment procedure, Undirected Connectable|
|mode] .................................................................................................................................................................. 205|
|GAP/CONN/DCEP/BV-05-C [Direct Connection Establishment procedure, Directed Connectable mode,|
|Resolvable Private Address, Central Address Resolution] ................................................................................. 206|
|GAP/CONN/DCEP/BV-06-C [Direct Connection Establishment procedure, Undirected Connectable|
|mode, Resolvable Private Address] .................................................................................................................... 207|
|GAP/CONN/CPUP/BV-01-C [Connection Parameter Update procedure, valid parameters, Peripheral|
|Initiator over L2CAP] ........................................................................................................................................... 209|
|GAP/CONN/CPUP/BV-02-C [Connection Parameter Update procedure, valid parameters, Timeout|
|Peripheral Initiator] .............................................................................................................................................. 210|
|GAP/CONN/CPUP/BV-03-C [Connection Parameter Update procedure, invalid parameters, Peripheral|
|Initiator] ............................................................................................................................................................... 211|
|GAP/CONN/CPUP/BV-04-C [Connection Parameter Update procedure, valid parameters, Central|
|Responder] ......................................................................................................................................................... 213|
|GAP/CONN/CPUP/BV-05-C [Connection Parameter Update procedure, invalid parameters, Central|
|Responder] ......................................................................................................................................................... 214|
|GAP/CONN/CPUP/BV-06-C [Connection Parameter Update procedure, valid parameters, Central|
|Initiator] ............................................................................................................................................................... 215|
|GAP/CONN/CPUP/BV-08-C [Connection Parameter Update procedure, valid parameters, Peripheral|
|Responder – LL Connection Parameters Request] ............................................................................................. 217|
|GAP/CONN/CPUP/BV-10-C [Connection Parameter Update procedure, valid parameters, Peripheral|
|Initiator over LL] .................................................................................................................................................. 218|
|GAP/CONN/TERM/BV-01-C [Terminate Connection procedure] ........................................................................ 219|
|GAP/CONN/PRDA/BV-01-C [Respond to Private Random Device Address after Bonding – Peripheral|
|role] ..................................................................................................................................................................... 220|
|GAP/CONN/PRDA/BV-02-C [Respond to Private Random Device Address after Bonding – Central role] ......... 221|
|4.7.4<br>Bonding modes and procedures ......................................................................................................... 223|
|GAP/BOND/NBON/BV-01-C [Non-bondable mode – Central as Responder] ..................................................... 223|
|GAP/BOND/NBON/BV-02-C [Non-bondable mode – Central as Initiator] ........................................................... 223|
|GAP/BOND/NBON/BV-03-C [Non-bondable mode – Peripheral as Responder] ................................................ 225|
|GAP/BOND/BON/BV-01-C [Initiate bonding – Peripheral role] ........................................................................... 226|
|GAP/BOND/BON/BV-02-C [Initiate bonding – Central role] ................................................................................ 228|
|GAP/BOND/BON/BV-03-C [Respond to bonding – Peripheral role] ................................................................... 229|
|GAP/BOND/BON/BV-04-C [Respond to bonding – Central role] ........................................................................ 231|
|4.7.5<br>Security ............................................................................................................................................... 232|
|GAP/SEC/AUT/BV-11-C [Service Response – Insufficient Authentication, Peripheral] ...................................... 232|
|GAP/SEC/AUT/BV-12-C [Service Response – Insufficient Authentication, Central] ........................................... 233|
|GAP/SEC/AUT/BV-13-C [Service Response – Insufficient Authentication, Central] ........................................... 235|
|GAP/SEC/AUT/BV-14-C [Service Response – Insufficient Authentication, Peripheral] ...................................... 237|
|GAP/SEC/AUT/BV-17-C [Correct Pairing after Insufficient Authentication – Central role] .................................. 238|
|GAP/SEC/AUT/BV-18-C [Correct Pairing after Insufficient Authentication – Peripheral role] ............................. 240|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **8 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|GAP/SEC/AUT/BV-19-C [Service Response Insufficient Authentication – Central role] ..................................... 242|
|---|
|GAP/SEC/AUT/BV-20-C [Service Response Insufficient Authentication – Peripheral role] ................................ 244|
|GAP/SEC/AUT/BV-21-C [Lost Bond – Initiator role] ........................................................................................... 246|
|GAP/SEC/AUT/BV-22-C [Lost Bond – Responder role] ...................................................................................... 247|
|GAP/SEC/AUT/BV-23-C [Service Response – Insufficient Encryption, Peripheral] ............................................ 248|
|GAP/SEC/AUT/BV-24-C [Service Response – Insufficient Encryption, Central] ................................................. 249|
|GAP/SEC/AUT/BV-25-C ..................................................................................................................................... 251|
|GAP/SEC/AUT/BV-26-C ..................................................................................................................................... 251|
|GAP/SEC/AUT/BV-27-C ..................................................................................................................................... 253|
|GAP/SEC/AUT/BV-28-C ..................................................................................................................................... 253|
|GAP/SEC/CSIGN/BV-01-C [Connection Based Signing – Sender] .................................................................... 255|
|GAP/SEC/CSIGN/BV-02-C [Connection Based Signing – Receiver] .................................................................. 256|
|GAP/SEC/CSIGN/BI-01-C [Connection Based Signing – Receiver – Invalid Signing] ........................................ 257|
|GAP/SEC/CSIGN/BI-02-C [Connection Based Signing – Receive Invalid SignCounter] .................................... 258|
|GAP/SEC/CSIGN/BI-03-C [Connection Based Signing – Receive, No Bonding, as Peripheral] ......................... 259|
|GAP/SEC/CSIGN/BI-04-C [Connection Based Signing – Receive, Insufficient Authentication, as|
|Peripheral] ........................................................................................................................................................... 260|
|GAP/PRIV/CONN/BV-10-C [Peripheral Privacy] ................................................................................................. 261|
|GAP/PRIV/CONN/BV-11-C [Central Privacy] ...................................................................................................... 262|
|GAP/PRIV/CONN/BV-12-C [Peripheral Privacy, Unresolvable RPA] .................................................................. 264|
|4.7.6<br>AD type ............................................................................................................................................... 266|
|GAP/ADV/BV-01-C [AD type – Service UUID] .................................................................................................... 267|
|GAP/ADV/BV-02-C [AD type – Local Name]....................................................................................................... 267|
|GAP/ADV/BV-03-C [AD type – Flags] ................................................................................................................. 267|
|GAP/ADV/BV-04-C [AD type – Manufacturer Specific Data] .............................................................................. 267|
|GAP/ADV/BV-05-C [AD type – TX Power Level] ................................................................................................ 267|
|GAP/ADV/BV-08-C [AD type – Peripheral Connection Interval Range] .............................................................. 267|
|GAP/ADV/BV-09-C [AD type – Service Solicitation] ........................................................................................... 268|
|GAP/ADV/BV-10-C [AD type – Service Data] ..................................................................................................... 268|
|GAP/ADV/BV-11-C [AD type – Appearance] ...................................................................................................... 268|
|GAP/ADV/BV-12-C [AD type – Public Target Address] ...................................................................................... 268|
|GAP/ADV/BV-13-C [AD type – Random Target Address] ................................................................................... 268|
|GAP/ADV/BV-14-C [AD type – Advertising Interval] ........................................................................................... 268|
|GAP/ADV/BV-17-C [AD type – URI] ................................................................................................................... 269|
|GAP/ADV/BV-18-C [AD type – Advertising Interval, Long] ................................................................................. 269|
|GAP/ADV/BV-19-C [AD type – LE Supported Features] ..................................................................................... 269|
|GAP/ADV/BV-20-C [AD type – Encrypted Data] ................................................................................................. 271|
|GAP/ADV/BV-21-C [AD type – Encrypted Data] ................................................................................................. 271|
|GAP/SCN/BV-01-C [AD type – Encrypted Data, Decrypt Advertising Data] ....................................................... 272|
|GAP/GAT/BV-15-C [Encrypted Data Key Characteristic Indication, GATT Server] ............................................ 273|
|4.7.7<br>Generic Access Profile characteristics ................................................................................................ 274|
|GAP/GAT/BV-09-C [Encrypted Data Key Material, Authenticated and Authorized] ............................................ 274|
|GAP/GAT/BV-10-C [Encrypted Data Key Material, Not Authenticated] .............................................................. 275|
|GAP/GAT/BV-11-C [Encrypted Data Key Material, Not Authorized] ................................................................... 276|
|GAP/GAT/BV-04-C [Discover GAP Characteristic, Peripheral Preferred Connection Parameters|
|Characteristic] ..................................................................................................................................................... 278|
|GAP/GAT/BV-12-C [Discover GAP Characteristic, LE GATT Security Levels Characteristic] ............................ 278|
|GAP/GAT/BV-16-C [Discover GAP Characteristic, Device Name] ...................................................................... 278|
|GAP/GAT/BV-17-C [Discover GAP Characteristic, Appearance] ........................................................................ 278|
|GAP/GAT/BV-18-C [Discover GAP Characteristic, Central Address Resolution] ................................................ 278|
|GAP/GAT/BV-19-C [Discover GAP Characteristic, Resolvable Private Address Only] ....................................... 278|
|GAP/GAT/BV-05-C [Writeable Characteristic, Device Name] ............................................................................. 280|
|GAP/GAT/BV-06-C [Writeable Characteristic, Appearance] ............................................................................... 280|
|4.7.8<br>Periodic Advertising modes and procedures ....................................................................................... 282|
|GAP/PADV/PASM/BV-01-C ................................................................................................................................ 282|
|GAP/PADV/PASM/BV-02-C ................................................................................................................................ 282|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **9 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|GAP/PADV/PAM/BV-01-C .................................................................................................................................. 284|
|---|
|GAP/PADV/PAM/BV-02-C .................................................................................................................................. 284|
|GAP/PADV/PASE/BV-01-C ................................................................................................................................ 285|
|GAP/PADV/PASE/BV-07-C ................................................................................................................................ 285|
|GAP/PADV/PASE/BV-02-C ................................................................................................................................ 286|
|GAP/PADV/PASE/BV-08-C ................................................................................................................................ 286|
|GAP/PADV/PASE/BV-03-C ................................................................................................................................ 287|
|GAP/PADV/PASE/BV-09-C ................................................................................................................................ 287|
|GAP/PADV/PASE/BV-04-C ................................................................................................................................ 289|
|GAP/PADV/PASE/BV-10-C ................................................................................................................................ 289|
|GAP/PADV/PASE/BV-05-C ................................................................................................................................ 290|
|GAP/PADV/PASE/BV-11-C ................................................................................................................................ 290|
|GAP/PADV/PASE/BV-06-C ................................................................................................................................ 292|
|GAP/PADV/PASE/BV-12-C ................................................................................................................................ 292|
|GAP/PADV/PAST/BV-01-C ................................................................................................................................. 293|
|GAP/PADV/PAST/BV-03-C ................................................................................................................................. 293|
|GAP/PADV/PAST/BV-02-C ................................................................................................................................. 295|
|GAP/PADV/PAST/BV-04-C ................................................................................................................................. 295|
|GAP/PADV/PAC/BV-01-C [Create connection with synchronized device using the Periodic Advertising|
|Connection procedure, Periodic Advertiser] ........................................................................................................ 296|
|GAP/PADV/PAC/BV-02-C [Create connection with synchronized device using the Periodic Advertising|
|Connection procedure, Scanner] ........................................................................................................................ 297|
|4.7.9<br>Broadcast Isochronous Streaming modes and procedures ................................................................ 298|
|GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment procedure] ............................ 298|
|GAP/BIS/BBM/BV-01-C [Broadcast Isochronous Stream Broadcasting mode] .................................................. 299|
|4.7.10<br>Connection Subrating procedure ........................................................................................................ 300|
|GAP/CSUB/CSR/BV-01-C [Connection Subrate Request procedure] ................................................................ 300|
|GAP/CSUB/CSU/BV-01-C [Connection Subrate Update procedure] .................................................................. 300|
|4.7.11<br>Channel Sounding procedure ............................................................................................................. 301|
|GAP/CS/BV-01-C [Starting Channel Sounding, Initiator] .................................................................................... 301|
|GAP/CS/BV-02-C [Starting Channel Sounding, Reflector] .................................................................................. 302|
|4.8<br>BR/EDR/LE operational modes and procedures ...................................................................... 303|
|4.8.1<br>Non-connectable mode ....................................................................................................................... 303|
|GAP/DM/NCON/BV-01-C [BR/EDR/LE non-connectable mode] ........................................................................ 303|
|4.8.2<br>Connectable mode .............................................................................................................................. 304|
|GAP/DM/CON/BV-01-C [BR/EDR/LE connectable mode] .................................................................................. 304|
|4.8.3<br>Non-bondable mode ........................................................................................................................... 305|
|GAP/DM/NBON/BV-01-C [BR/EDR/LE non-bondable mode] ............................................................................. 305|
|4.8.4<br>Bondable mode ................................................................................................................................... 306|
|GAP/DM/BON/BV-01-C [BR/EDR/LE bondable mode] ....................................................................................... 306|
|4.8.5<br>General Discovery procedure ............................................................................................................. 307|
|GAP/DM/GIN/BV-01-C [BR/EDR/LE General Discovery – Finding General Discoverable devices] ................... 307|
|4.8.6<br>Limited Discovery procedure .............................................................................................................. 309|
|GAP/DM/LIN/BV-01-C [BR/EDR/LE Limited Discovery – Find Limited Discoverable devices] ........................... 309|
|4.8.7<br>Name Discovery procedure ................................................................................................................ 310|
|GAP/DM/NAD/BV-01-C [BR/EDR/LE Name Discovery] ..................................................................................... 310|
|GAP/DM/NAD/BV-02-C [LE Name Discovery] .................................................................................................... 311|
|4.8.8<br>Link Establishment procedure ............................................................................................................. 312|
|GAP/DM/LEP/BV-01-C [BR/EDR/LE and BR/EDR/LE Link Establishment – BR/EDR Transport] ...................... 312|
|GAP/DM/LEP/BV-06-C [BR/EDR/LE and LE Link Establishment IUT is BR/EDR/LE] ........................................ 313|
|GAP/DM/LEP/BV-07-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral – LE|
|Transport]............................................................................................................................................................ 315|
|GAP/DM/LEP/BV-08-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR|
|Peripheral – LE and BR/EDR Transports] ........................................................................................................... 316|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **10 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

||GAP/DM/LEP/BV-09-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Central –|
|---|---|
||LE and BR/EDR Transports] ............................................................................................................................... 318|
||GAP/DM/LEP/BV-10-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Central –|
||LE and BR/EDR Transports] ............................................................................................................................... 320|
||GAP/DM/LEP/BV-11-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Peripheral –|
||LE and BR/EDR Transports] ............................................................................................................................... 322|
||GAP/DM/LEP/BV-12-C [Generate BR/EDR Link Key from LE LTK, as Initiator] ................................................. 324|
||GAP/DM/LEP/BV-13-C [Upgrade of BR/EDR Link Key Regenerates LTK] ........................................................ 325|
||GAP/DM/LEP/BV-14-C [Generate BR/EDR Link Key from LE LTK, as Responder] ........................................... 328|
||GAP/DM/LEP/BV-15-C [Generate BR/EDR Link Key from LE LTK, as Initiator] ................................................. 329|
||GAP/DM/LEP/BV-16-C [Generate BR/EDR Link Key from LE LTK, as Responder] ........................................... 330|
||GAP/DM/LEP/BV-17-C [Generate LE LTK from BR/EDR Link Key, as Initiator] ................................................. 332|
||GAP/DM/LEP/BV-18-C [Upgrade of LTK Regenerates BR/EDR Link Key] ........................................................ 334|
||GAP/DM/LEP/BV-19-C [Generate LE LTK from BR/EDR Link Key, as Responder] ........................................... 336|
||GAP/DM/LEP/BI-01-C [Do Not Generate LE LTK from BR/EDR P-192 Link Key, as Initiator]............................ 337|
||GAP/DM/LEP/BI-02-C [Do Not Generate LE LTK from P-192 BR/EDR Link Key, as Responder] ...................... 339|
||GAP/DM/LEP/BV-20-C [Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as|
||Initiator] ............................................................................................................................................................... 340|
||GAP/DM/LEP/BV-21-C [Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as|
||Responder] ......................................................................................................................................................... 343|
||GAP/DM/LEP/BV-22-C [Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Initiator] ............ 345|
||GAP/DM/LEP/BV-23-C [Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as|
||Responder] ......................................................................................................................................................... 347|
||4.8.9<br>Synchronization Establishment – Receiver ......................................................................................... 349|
||GAP/EST/SYNE/BV-01-C [Synchronization Establishment procedure, IUT is Receiver] .................................... 349|
|**5**|**Test case mapping ........................................................................................................................... 350**|
|**6**|**Revision history and acknowledgments ........................................................................................ 366**|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **11 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **1 Sco e p** 

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Generic Access Profile (GAP) layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers’ Bluetooth devices. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **12 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **2 References, definitions, and abbreviations** 

## **2.1 References** 

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [1], [4], and [5]. 

- [1] Bluetooth Specification Version 1.2 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [2] Profile ICS proforma for Generic Access Profile (GAP) 

- [3] Core IXIT Proforma 

- [4] Bluetooth Specification Version 4.0 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [5] Test Strategy and Terminology Overview 

- [6] Bluetooth Specification Version 4.1 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [7] Core Specification Supplement (CSS), Part A, Current Version 

- [8] Bluetooth Specification Version 4.0 or later Core System Package, Volume 6, Part B, Link Layer (LL) 

- [9] Bluetooth Specification Version 4.2 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [10] Bluetooth Specification Version 4.2 or later Core System Package, Volume 3, Part H, Security Manager (SM) 

- [11] Bluetooth Specification Version 4.2 or later Core System Package, Volume 6, Part B, Link Layer (LL) 

- [12] Bluetooth Specification Version 5.0 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [13] Bluetooth Specification Version 2.1 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [14] Bluetooth Specification Version 5.1 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [15] Bluetooth Specification Version 5.2 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [16] Appropriate Language Mapping Tables document 

- [17] Bluetooth Specification Version 5.3 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [18] Bluetooth Specification Version 5.4 or later Core System Package, Volume 3, Part C, Generic Access Profile (GAP) 

- [19] Bluetooth Specification Version 6.0 or later Core System Package, Volume 3 Part C, Generic Access Profile (GAP) 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **13 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **2.2 Definitions** 

In this Bluetooth document, the definitions from [1], [4], and [5] apply. 

Certain terms that were identified as inappropriate have been replaced. For a list of the original terms and their replacement terms, see the Appropriate Language Mapping Tables document [16]. 

## **2.3 Acronyms and abbreviations** 

In this Bluetooth document, the definitions, acronyms, and abbreviations from [1], [4], and [5] apply. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **14 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **3 Test Suite Structure (TSS)** 

## **3.1 Test Strategy** 

The test objectives are to verify the functionality of the Generic Access Profile within a Bluetooth Host and enable interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory and optional requirements in the specification and matches these to the support of the IUT as described in the ICS. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test Case Mapping Table (TCMT) evaluates to true. 

The test equipment provides an implementation of the Radio Controller and the parts of the Host needed to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT’s peer device and interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement similar capabilities to communicate with the test equipment. For some test cases, it is necessary to stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface, a Man Machine Interface (MMI), or another interface supported by the IUT. 

This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with catalogued specification requirements that were logically grouped and assessed for testability enabling coverage in defined test purposes. 

## **3.2 Test groups** 

The Test Suite Structure is a tree with the first level representing the protocol groups that apply to the device types defined by the Generic Access Profile. 

The second level separates the protocol services in functional modules. The last level in each branch contains the standard ISO subgroups BV and BI. 

## **3.2.1 BR/EDR Protocol groups** 

## **3.2.1.1 Modes** 

This group handles testing of the modes for discoverability, connectability, and pairability, and synchronizability of a Bluetooth device. 

## **3.2.1.2 Security Aspects** 

This group handles testing of the GAP security aspects. 

## **3.2.1.3 Idle mode procedures** 

This group handles testing of the different Idle mode procedures. 

## **3.2.1.4 Establishment procedures** 

This group handles testing of the different establishment procedures as defined in GAP. 

## **3.2.2 LE Only Protocol groups** 

## **3.2.2.1 Broadcasting and Observing** 

This group handles testing of the broadcasting and observing modes and procedures of a LE-only device. 

## **3.2.2.2 Discovery modes and procedures** 

This group handles testing of the discovery modes and procedures of a LE-only device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **15 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **3.2.2.3 Connection modes and procedures** 

This group handles testing of the connection modes and procedures of a LE-only device. 

## **3.2.2.4 Bonding modes and procedures** 

This group handles testing of the bonding modes and procedures of a LE-only device. 

## **3.2.2.5 Security Aspects** 

This group handles testing of the security aspects for a LE-only device. 

## **3.2.2.6 Advertising and Scan Response Data Format** 

This group handles testing of the advertising and scan response data format of a LE-only device. 

## **3.2.2.7 Generic Access Profile Characteristics for Low Energy** 

This group handles testing of the GAP characteristics of a LE-only device. 

## **3.2.2.8 Discovery of Devices with Resolvable Private Address** 

This group handles testing of the discovery of devices with Resolvable Private Addresses of a LE-only device. 

## **3.2.2.9 Periodic Advertising modes and procedures** 

This group handles testing of the periodic advertising modes and procedures of an LE-only device. 

## **3.2.2.10 Broadcast Isochronous Streaming modes and procedures** 

This group handles testing of the Broadcast Isochronous Streaming modes and procedures of an LEcapable device. The test cases found in this group are based on the Generic Access Profile. 

## **3.2.2.11 Connection Subrating procedure** 

This group handles testing of the Connection Subrating procedure of an LE-only device. 

## **3.2.2.12 Scanning Advertisement** 

This group handles testing of scanning advertisements on a LE-only device. 

## **3.2.2.13 Channel Sounding** 

This group handles testing of the Channel Sounding feature. 

## **3.2.3 BR/EDR/LE (Dual Mode) Protocol groups** 

## **3.2.3.1 Modes** 

This group handles testing of the modes for discoverability, connectability, and pairability, and synchronizability of a BR/EDR/LE device. 

## **3.2.3.2 Idle mode procedures** 

This group handles testing of the different Idle mode procedures for a BR/EDR/LE device. 

## **3.2.3.3 Establishment procedures** 

This group handles testing of the different establishment procedures for a BR/EDR/LE device. 

## **3.2.3.4 BR/EDR/LE security aspects** 

This group handles testing of the security aspects for a BR/EDR/LE device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **16 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **3.2.4 Main test groups** 

## **3.2.4.1 Valid Behavior (BV) Tests** 

This subgroup provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt or exchange of valid Protocol Data Units (PDUs). Valid PDUs means that the exchange of messages and the content of the exchanged messages are considered as valid. 

## **3.2.4.2 Invalid Behavior (BI) Tests** 

This subgroup provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt of a syntactically or semantically invalid PDU. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **17 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4 Test cases (TC)** 

## **4.1 Introduction** 

## **4.1.1 Test case identification conventions** 

Test cases are assigned unique identifiers per the conventions in [5]. The convention used here is: **<spec abbreviation>/<IUT role>/** <class>/ **<feat>** /<func>/<subfunc>/<cap>/ **<xx>-<nn>-<y>** . 

|**Identifier Abbreviation**|**Spec Identifier <spec abbreviation>**|
|---|---|
|GAP|Generic Access Profile|
|**Identifier Abbreviation**|**Function Identifier <func>**|
|ADV|AdvertisingData Format|
|BIS|Broadcast Isochronous Streamingmodes andprocedures|
|BOND|Bondingmodes andprocedures|
|BROB|Broadcastingand Observing|
|CONN|Connection modes andprocedures|
|CS|Channel Sounding|
|CSUB|Connection Subrating procedure|
|DISC|Discoverymodes andprocedures|
|DM|Dual Mode(BR/EDR/LE)|
|EST|Establishmentprocedures|
|GAT|Generic Access Profile characteristics|
|IDLE|Idle mode|
|MOD|Modes|
|PADV|Periodic Advertisingmodes andprocedures|
|PRIV|Privacy|
|SCN|Scanner|
|SEC|Securitymodes andprocedures|
|**Identifier Abbreviation**|**Subfunction Identifier <subfunc>**|
|AUT|Authentication|
|BBM|Broadcast Isochronous Stream Broadcastingmode|
|BSE|Broadcast Isochronous Stream Synchronization Establishment|
|CON|Connectable mode|
|CSR|Connection Subrate Request|
|CSU|Connection Subrate Response|
|DED|Device Discovery|
|DNDIS|Device Name Discovery|
|GDIS|General Discoverable mode|
|GIN|General Inquiry|
|LDIS|Limited Discoverable mode|
|LIN|Limited Inquiry|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **18 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|NAD|Name Discovery|
|---|---|
|NBON|Non-bondable mode|
|**Identifier Abbreviation**|**Subfunction Identifier <subfunc>**|
|NCON|Non-connectable mode|
|NDIS|Non-discoverable mode|
|NSYN|Non-synchronizable mode|
|PAC|Periodic AdvertisingConnection|
|PAIR|Pairable mode|
|PAM|Periodic Advertisingmode|
|PASE|Periodic AdvertisingSynchronization Establishmentprocedure|
|PASM|Periodic AdvertisingSynchronizabilitymode|
|PAST|Periodic AdvertisingSynchronization Transferprocedure|
|RPA|Discoveryof Devices with Resolvable Private Address|
|SEM|Securitymodes|
|SYN|Synchronizable mode|
|SYNE|Synchronization Establishment|



_Table 4.1: GAP TC feature naming conventions_ 

## **4.1.2 Conformance** 

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

Page **19 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.1.3 Pass/Fail verdict conventions** 

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met. 

The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict. 

## **4.2 Preambles** 

## **4.2.1 Link Establishment Lower Tester Started (for generic authentication)** 

**==> picture [358 x 410] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby, in Idle mode and a link key is available.<br>BB-functionality: All used BB-<br>messages are explained in the  Bring IUT in security mode 3<br>BB Test Spec.<br>Bring IUT in connectable mode<br>Page request (BB functionality)<br>(ID-packet (Peripherals DAC))<br>Page request (BB functionality)<br>(ID-packet (Peripherals DAC))<br>Page response (BB functionality)<br>(ID-packet (Peripherals DAC))<br>FHS-packet (BB functionality)<br>FHS-acknowledge (BB functionality)<br>(ID-packet (Peripherals DAC))<br>POLL-packet (BB functionality) The IUT sends one of the<br>possible one-slot packets,<br>implementation-dependent IUT.<br>DM1, DH1, NULL or AUX1<br>(BB-functionality)<br>LMP_features_req (features)<br>LMP_features_res (features)<br>Paging procedure is<br>performed successfully on<br>LMP_host_connection_req BB-Level and link<br>establishment is started.<br>LMP_accepted<br>(opcode: LMP_host_connection_req)<br>**----- End of picture text -----**<br>


_Figure 4.1: Link Establishment Tester Started (for generic authentication) MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **20 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.2.2 Inquiry procedure** 

**==> picture [357 x 286] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby, Idle mode<br>Command IUT to enter (General or<br>Limited) discoverable mode<br>Inquiry: ID packet (GIAC or LIAC)<br>Inquiry: ID packet (GIAC or LIAC)<br>Inquiry: ID packet (GIAC or LIAC)<br>Inquiry: ID packet (GIAC or LIAC)<br>Inquiry response: FHS packet<br>(Parity bits, LAP, EIR, Undef=0b,<br>SR, Reserved=10b, UAP, NAP,<br>CoD, LT_ADDR, CLK27-2, Page Scan<br>Mode)<br>Extended inquiry response<br>(EIR data)<br>**----- End of picture text -----**<br>


_Figure 4.2: Inquiry procedure MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **21 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.2.3 Paging procedure** 

**==> picture [358 x 417] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby, in Idle mode, and a link key is available.<br>BB-functionality:<br>All used BB-messages are  Bring IUT in security mode 3<br>explained in the BB Test Spec.<br>Bring IUT in connectable mode<br>Page request (BB functionality)<br>(ID-packet (Peripherals DAC))<br>Page request (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>Page response (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>FHS-packet (BB-functionality)<br>FHS-acknowledge (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>POLL-packet (BB-functionality) The IUT sends one of the<br>possible one-slot packets,<br>implementation-dependent IUT.<br>DM1, DH1, NULL or AUX1<br>(BB-functionality)<br>LMP_features_req (features)<br>LMP_features_res (features)<br>Paging procedure is<br>performed successfully on<br>LMP_host_connection_req BB-Level and link<br>establishment is started.<br>LMP_accepted<br>(opcode: LMP_host_connection_req)<br>**----- End of picture text -----**<br>


_Figure 4.3: Paging procedure MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **22 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.2.4 Bring IUT to Link Key Available** 

**==> picture [358 x 559] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-standby, in Idle mode with any supported security mode and no link key<br>available.<br>Page request (BB-functionality) The Lower Tester has to know the<br>BD_ADDR for the IUT before<br>(ID-packets (Peripherals DAC))<br>paging is initiated.<br>Pararequest (BB-functionality)<br>(ID-packets (Peripherals DAC)) BB-functionality:All used BB-<br>messages are explained in the<br>Pararequest (BB-functionality) BB Test Spec.<br>(ID-packets (Peripherals DAC))<br>FHS-packet (BB-functionality)<br>FHS-acknowledge (BB-functionality)<br>(ID-packets (Peripherals DAC))<br>POLL-packet (BB-functionality)<br>DM1, DH1, AUX1 or NULL-packet<br>(BB-functionality)<br>Paging procedure is performed<br>LMP_features_req (features) successfully on BB-level and link<br>establishment is started.<br>LMP_features_res (features)<br>LMP_host_connection_req<br>LMP_accepted<br>Authentication is initiated by<br>(opcode LMP_host_connection_req) Lower Tester (LMP_Pairing).<br>LMP_in_rand<br>(rand_nr)<br>LMP_accepted<br>(opcode LMP_in_rand)<br>LMP_comb_key<br>(rand_nr)<br>ALT LMP_comb_key<br>(rand_nr)<br>LMP_unit_key (key)<br>mutual authentication messages<br>mutual LMP_Setup_Complete messages<br>LMP_detach<br>(Reason: Other End Terminated Connection: User Ended Connection)<br>**----- End of picture text -----**<br>


_Figure 4.4: Bring IUT to Link Key Available MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **23 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.2.5 Secure Simple Pairing** 

|Lower T|Lower T|ester|ester||IUT|IUT|IUT||||Upper Tester|Upper Tester|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Page request (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>Page response (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>FHS-packet (BB-functionality)<br>FHS-acknowledge (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>POLL-packet (BB-functionality)<br>DM1, DH1, NULL, or AUX1<br>(BB-functionality)<br>LMP_features_req (features)<br>LMP_features_res (features)<br>LMP_accepted<br>(opcode: LMP_host_connection_req)<br>LMP_host_connection_req<br>Mutual LMP_setup_complete<br>Public Key Exchange<br>Numeric Comparison<br>DHKey Check<br>LMP_sres<br>LMP_features_req_ext (features)<br>LMP_features_res_ext (features)<br>LMP_au_rand<br>LMP_sres<br>LMP_au_rand||||||Bring IUT in security mode 4|||||
|||||||||Bring IUT in connectable mode|||||
||||||||||||||
||||||||||||||
||||||||||||||



_Figure 4.5: Secure Simple Pairing MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **24 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.2.6 GAP Mandatory Characteristics** 

**==> picture [357 x 253] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>Find by type value request<br>“Service”, “GAP”<br>Find by type value response<br>“GAP_Handle”<br>Read by type request<br>“GAP_Handle”, “Characteristic”<br>Read by type response<br>“02, “GAP_Handle”, 02,<br>DevName_Handle, “Device Name<br>UUID”, “GAP_Handle”, 02,<br>Appearance_Hdl, “Appearance UUID”<br>Read request<br>“DevName_Handle”<br>Read Response<br>“Example_Device Name”<br>Read request<br>“Appearance_Handle”<br>Read Response<br>“Appearance Value”<br>**----- End of picture text -----**<br>


**==> picture [64 x 32] intentionally omitted <==**

**==> picture [63 x 32] intentionally omitted <==**

**==> picture [63 x 32] intentionally omitted <==**

_Figure 4.6: GAP Mandatory Characteristics MSC_ 

## **4.3 Common Packet Contents** 

## **4.3.1 Fields and Bits Reserved for Future Use** 

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers. 

## **4.4 Modes** 

Verify the correct implementation of the modes. 

## **4.4.1 Non-discoverable bondable mode – Peripheral** 

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor. 

**GAP/MOD/NDIS/BV-01-C [Non-discoverable mode – Peripheral]** 

- Test Purpose 

Verify that the IUT does not respond to inquiry if it is in non-discoverable mode. 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure. 

- Reference 

   - [1] 4.1.1 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **25 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [335 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device in non- discoverable mode<br>Inquiry (ID-Packet)<br>(GIAC)<br>Inquiry (ID-Packet)<br>(GIAC)<br>Verify that the IUT does not<br>respond to inquiry-requests.<br>T GAP (103)<br>**----- End of picture text -----**<br>


_Figure 4.7: GAP/MOD/NDIS/BV-01-C [Non-discoverable mode – Peripheral] MSC_ 

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in non-discoverable mode. Every inquiry train is repeated for N=256 times. 

- Expected Outcome 

## Pass verdict 

The IUT does not answer to an inquiry request. 

## **4.4.2 Limited Discoverable mode – Peripheral** 

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor. 

**GAP/MOD/LDIS/BV-01-C [Limited Discoverable mode and LIAC – Peripheral]** 

- Test Purpose 

Verify that the IUT answers to inquiry (LIAC) if it is in limited-discoverable mode. 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure. 

- Reference 

   - [1] 4.1 (Discoverability modes) 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **26 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [342 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device in limited- discoverable mode<br>Inquiry (ID-Packet)<br>(LIAC)<br>Inquiry (ID-Packet)<br>(LIAC)<br>Inquiry Response: FHS-packet Verify that the Inquiry<br>response(LIAC) message is received<br>(parity bits, LAP, undef., SR,<br>T GAP (103) Reserved=10B, UAP,NAP,CoD,   by the Lower Tester within T GAP<br>(103).<br>LT_ADDR, CLK)<br>**----- End of picture text -----**<br>


_Figure 4.8: GAP/MOD/LDIS/BV-01-C [Limited Discoverable mode and LIAC – Peripheral] MSC_ 

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in limited-discoverable mode. Every inquiry train is repeated for N = 256 times. 

- Expected Outcome 

## Pass verdict 

The IUT answers to an inquiry request (LIAC) with the FHS-packet. The Inquiry response message is received by the Lower Tester within TGAP(103). 

The COD has the bit number 13 set in the Major Service Class part of the Class of Device field. 

**GAP/MOD/LDIS/BV-02-C [Limited Discoverable mode and GIAC – Peripheral]** 

- Test Purpose 

Verify that the IUT answers to inquiry (GIAC) if it is in limited-discoverable mode. 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure. 

- Reference 

[1] 4.1 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and Idle mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **27 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [336 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device in limited- discoverable mode<br>Inquiry (ID-Packet)<br>(GIAC)<br>Inquiry (ID-Packet)<br>(GIAC)<br>Inquiry Response: FHS-packet Verify that the Inquiry<br>response(GIAC) message is received<br>T GAP (103) (parity bits, LAP, undef., SR, Reserved=10B, UAP,NAP, CoD,   by the Lower Tester within T GAP (103).<br>LT_ADDR, CLK)<br>**----- End of picture text -----**<br>


_Figure 4.9: GAP/MOD/LDIS/BV-02-C [Limited Discoverable mode and GIAC – Peripheral] MSC_ 

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in limited-discoverable mode. Every inquiry train is repeated for N = 256 times. 

- Expected Outcome 

## Pass verdict 

The IUT answers to an inquiry request (GIAC) with the FHS-packet. The Inquiry response message is received by the Lower Tester within TGAP(103). 

The COD has the bit number 13 set in the Major Service Class part of the Class of Device field. 

## **GAP/MOD/LDIS/BV-03-C [Limited Discovery mode time-out]** 

- Test Purpose 

Verify that the IUT ceases to answer to inquiry after a time-out, if it is in limited-discoverable mode. 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure. 

- Reference 

   - [4] 4.1.2 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

   - The limited discoverable mode time TGAP is defined by the TSPX_Tgap_104 IXIT value. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **28 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [339 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT in BB_Standby and Idle Mode.<br>Bring device in limited -discoverable mode<br>TGAP(104)<br>Inquiry (ID-Packet)<br>(LIAC)<br>Inquiry (ID-Packet)<br>(LIAC)<br>**----- End of picture text -----**<br>


_Figure 4.10: GAP/MOD/LDIS/BV-03-C [Limited Discovery mode time-out] MSC_ 

   1. The Upper Tester orders the IUT to go in limited-discoverable mode. The Lower Tester waits for TGAP(104) to expire. (TGAP(104) has a default of 1 minute, but an alternate value may be invoked via TSPX_Tgap_104.) 

   2. After TGAP(104) has expired, the Lower Tester sends a series of 256 inquiry request messages (IDpackets) with LIAC. Since the IUT has left the Limited Discoverable mode on the expiration of the timer, it does not respond. 

- 

- Expected Outcome 

## Pass verdict 

The IUT does not answer any inquiry request (LIAC) with an FHS-packet. 

## **4.4.3 General Discoverable mode – Peripheral** 

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor. 

**GAP/MOD/GDIS/BV-01-C [General Discoverable mode and GIAC – Peripheral]** 

- Test Purpose 

Verify that the IUT answers to inquiry (GIAC) if it is in general-discoverable mode. 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure. 

- Reference 

[1] 4.1 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and Idle mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **29 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [336 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device in general- discoverable mode<br>Inquiry (ID-Packet)<br>(GIAC)<br>Inquiry (ID-Packet)<br>First Inquiry message received:IUT<br>(GIAC) starts the Random Access:0-1023.<br>Inquiry Response: FHS-packet Verify that the Inquiry response (GIAC)<br>message is received by the Lower<br>(parity bits, LAP, undef., SR,<br>T GAP (103) Reserved=10B, UAP, NAP, CoD,   Tester within T GAP (103).<br>LT_ADDR, CLK)<br>**----- End of picture text -----**<br>


_Figure 4.11: GAP/MOD/GDIS/BV-01-C [General Discoverable mode and GIAC – Peripheral] MSC_ 

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in general-discoverable mode. Every inquiry train is repeated for N=256 times. 

- Expected Outcome 

## Pass verdict 

The IUT answers to an inquiry request (GIAC) with the FHS-packet. The Inquiry response message is received by the Lower Tester within TGAP(103). 

**GAP/MOD/GDIS/BV-02-C [General Discoverable mode and LIAC – Peripheral]** 

- Test Purpose 

Verify that the IUT in general-discoverable mode does not respond inquiry requests (using LIAC). 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure. 

- Reference 

[1] 4.1 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and Idle mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **30 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [335 x 236] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device in general- discoverable mode<br>Inquiry (ID-Packet)<br>(LIAC)<br>Inquiry (ID-Packet)<br>Verify that the IUT does not<br>(LIAC)<br>respond to inquiry-requests if<br>T GAP (103) it is in general discoverable<br>mode and LIAC is used for<br>inquiry.<br>**----- End of picture text -----**<br>


_Figure 4.12: GAP/MOD/GDIS/BV-02-C [General Discoverable mode and LIAC – Peripheral] MSC_ 

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in general-discoverable mode. Every inquiry train is repeated for N=256 times. 

- Expected Outcome 

## Pass verdict 

The IUT does not answer to an inquiry request (LIAC). 

## **4.4.4 Non-connectable mode – Peripheral** 

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor. 

**GAP/MOD/NCON/BV-01-C [Non-connectable mode – Peripheral]** 

- Test Purpose 

Verify that the IUT does not respond to paging if it is in non-connectable mode. 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the paging procedure. 

The BD_ADDR of the IUT is specified by the TSPX_bd_addr_iut IXIT value. 

- Reference 

[1] 4.3 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **31 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [337 x 264] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device in non-connectable mode<br>Page request (ID-packet (Peripherals  DAC))<br>Verify that the IUT does not answer to a<br>paging request message (ID-Packet)<br>Page request (ID-packet (Peripherals DAC)) until PageTO while in non-connectable<br>mode.<br>max. PageTO<br>**----- End of picture text -----**<br>


_Figure 4.13: GAP/MOD/NCON/BV-01-C [Non-connectable mode – Peripheral] MSC_ 

The Lower Tester sends for the time max. PageTO paging request messages (ID-packets) after the Upper Tester has ordered the IUT to go in non-connectable mode. 

- Expected Outcome 

## Pass verdict 

The IUT does not answer to paging requests. 

- 

- Notes 

It must be possible to select a certain BD_ADDR or CoD for the Lower Tester if necessary. 

## **4.4.5 Connectable mode – Peripheral** 

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor. 

**GAP/MOD/CON/BV-01-C [Connectable mode – Peripheral]** 

- Test Purpose 

Verify that the IUT responds to paging requests if it is in connectable mode. 

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the paging procedure. 

- Reference 

## [1] 4.3 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **32 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

   - The BD_ADDR of the IUT is specified by the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

**==> picture [335 x 249] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device in connectable mode<br>Page request (ID-packet (Peripherals DAC))<br>Page request (ID-packet (Peripherals DAC))<br>Verify that the IUT responds to a<br>Page response (ID-packet (Peripherals DAC)) paging request message(ID-<br>max. PageTO packet) before PageTO while in<br>connectable mode.<br>**----- End of picture text -----**<br>


_Figure 4.14: GAP/MOD/CON/BV-01-C [Connectable mode – Peripheral] MSC_ 

   1. The Lower Tester sends for the time max. PageTO paging request messages (ID-packets) after the Upper Tester has ordered the IUT to go in connectable mode. 

   2. The IUT answers to the paging request. 

- 

## Expected Outcome 

## Pass verdict 

The IUT answers to paging request messages with the paging response message (ID-packet) within PageTO. 

- Notes 

It must be possible to select a certain BD_ADDR or CoD for the Lower Tester if necessary. 

## **4.4.6 Non-bondable mode – Peripheral** 

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor. 

## **GAP/MOD/NBON/BV-02-C [Non-bondable mode, IUT rejects pairing procedure]** 

- Test Purpose 

Verify that the IUT rejects a pairing procedure, if it is in non-bondable mode. 

The IUT is Peripheral and claimant. The Lower Tester is Central and verifier of the pairing procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **33 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference 

   - [1] 4.3 

- Initial Condition 

   - The IUT is in non-bondable mode. 

   - Any link keys associated with the IUT and Lower Tester are deleted. 

   - The IUT and Lower Tester support Secure Simple Pairing and have set Write Simple Pairing mode to their respective Controllers. 

   - The Lower Tester’s IO capabilities are set to “DisplayYesNo”. 

   - The Lower Tester’s Authentication_Requirements are set to “MITM Protection Not Required – Dedicated Bonding. Numeric comparison with automatic accept allowed.” (0x02). 

   - The IUT is in a connectable state. 

- Test Procedure 

**==> picture [338 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in security mode 4 and is connectable and in non-bondable mode.<br>Authentication_Requirements: Authentication_Requirements:<br>MITM Protection, Not Required  No Bonding on IUT<br>and Dedicated Bonding on<br>Lower Tester<br>Secure Simple Pairing Procedure<br>Pairing is rejected<br>Secure Simple Pairing is not successful<br>**----- End of picture text -----**<br>


_Figure 4.15: GAP/MOD/NBON/BV-02-C [Non-bondable mode, IUT rejects pairing procedure] MSC_ 

1. The Lower Tester establishes a connection to the IUT and initiates a secure simple pairing procedure. The Lower Tester’s IO capabilities are set to “DisplayYesNo” and the Authentication_Requirements are set to “MITM Protection Not Required – Dedicated Bonding. Numeric comparison with automatic accept allowed.” (0x02). 

2. The IUT in non-bondable mode responds negatively to the IO capability request where the Lower Tester’s Authentication_Requirements parameter requests dedicated bonding. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **34 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The IUT in non-bondable mode does not accept the pairing request from the Lower Tester where the Authentication_Requirements parameter requests dedicated bonding. Secure Simple Pairing does not complete with dedicated bonding. 

## **GAP/MOD/NBON/BV-03-C [Non-bondable mode, IUT accepts a non-bonded connection]** 

- Test Purpose 

Verify that the IUT accepts a non-bonded connection when it is in non-bondable mode. 

The IUT is Peripheral and claimant. The Lower Tester is Central and verifier of the pairing procedure. 

- Reference 

   - [1] 4.3 

- Initial Condition 

   - The IUT is in non-bondable mode. 

   - An ACL connection exists between the IUT and Lower Tester. 

   - The IUT and Lower Tester support Pairing and have set Write Simple Pairing mode to their respective Controllers. 

   - The Lower Tester’s IO capabilities are set to “DisplayYesNo”. 

   - The Lower Tester’s Authentication_Requirements are set to “MITM Protection Not Required – No Bonding” (0x00). 

- Test Procedure 

**==> picture [341 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT connected to Lower Tester and in non-bondable mode<br>Authentication_Requirements:<br>MITM Protection, Not Required<br>and No Bonding on Lower<br>Tester Authentication_Requirements:<br>No Bonding on IUT<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing is successful<br>**----- End of picture text -----**<br>


_Figure 4.16: GAP/MOD/NBON/BV-03-C [Non-bondable mode, IUT accepts a non-bonded connection] MSC_ 

1. The Lower Tester establishes a connection to the IUT and initiates a secure simple pairing 

   - procedure. The Lower Tester’s IO capabilities are set to “DisplayYesNo” and the Authentication_Requirements are set to “MITM Protection Not Required – No Bonding” (0x00). 

2. The IUT in non-bondable mode accepts the IO capability request where the Lower Tester’s Authentication_Requirements parameter requests no bonding and secure simple pairing is successful. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **35 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Secure Simple Pairing procedure is completed successfully. 

## **4.4.7 Pairing mode – Peripheral** 

## **4.4.8 Non-synchronizable mode – Connectionless Peripheral Broadcaster** 

Verify the correct behavior in this mode. The role of the IUT is connectionless Peripheral broadcast transmitter. 

## **GAP/MOD/NSYN/BV-01-C [Non-synchronizable mode, IUT is Connectionless Peripheral Broadcast Transmitter]** 

- Test Purpose 

Verify that the IUT does not send the synchronization train if it is in non-synchronizable mode. The IUT is the connectionless Peripheral broadcast transmitter and the Lower Tester is the connectionless Peripheral broadcast receiver. 

- References 

   - [9] 4.4.1 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

   - The BD_ADDR of the IUT is specified by the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

The Lower Tester scans for Sync_Scan_Timeout = 10.12 seconds for the synchronization train after the Upper Tester has ordered the IUT to go in non-synchronizable mode. 

**==> picture [332 x 245] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby and Idle mode.<br>Bring device to non-synchronizable mode<br> Lower Tester attempts<br>to synchronize<br> Lower Tester attempts<br>to synchronize<br>Verify that the IUT is not sending<br>Sync_Scan  Synchronization Train<br>Timeout<br>**----- End of picture text -----**<br>


_Figure 4.17: GAP/MOD/NSYN/BV-01-C [Non-synchronizable mode, IUT is Connectionless Peripheral Broadcast Transmitter] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **36 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Lower Tester is unable to synchronize to the IUT. 

## **4.4.9 Synchronizable mode – Connectionless Peripheral Broadcaster** 

Verify the correct behavior in this mode. The role of the IUT is connectionless Peripheral broadcast transmitter. 

**GAP/MOD/SYN/BV-01-C [Synchronizable mode – IUT is Connectionless Peripheral Broadcast Transmitter]** 

- Test Purpose 

Verify that the IUT transmits the Synchronization Train when it is in Synchronizable mode. The IUT is the connectionless Peripheral broadcast transmitter and the Lower Tester is the connectionless Peripheral broadcast receiver. 

- References 

   - [9] 4.4.2 

- Initial Condition 

   - The IUT is in Standby state. 

- Test Procedure 

   1. The Upper Tester configures the Synchronization Train on the IUT with Interval = 80 ms, Timeout = 120 seconds, and Service_Data = 0x01. 

   2. The Upper Tester reserves LT_ADDR=1 on the IUT and enables a Connectionless Peripheral Broadcast on the IUT using the reserved LT_ADDR with Interval = 80 ms. 

   3. The Upper Tester places the IUT in Synchronizable mode. 

   4. The Lower Tester receives the Synchronization Train from the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **37 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [295 x 284] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Configure Synchronization Train<br>Start Connectionless Broadcast<br>Start Synchronization Train<br>Receive Synchronization Train<br>**----- End of picture text -----**<br>


_Figure 4.18: GAP/MOD/SYN/BV-01-C [Synchronizable mode – IUT is Connectionless Peripheral Broadcast Transmitter] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives the Synchronization Train from the IUT in accordance with the configuration via the Upper Tester. 

## **4.5 Security aspects** 

Verify the correct implementation of the modes, behavior, and procedures of the IUT. 

## **4.5.1 BR/EDR security modes – Peripheral** 

Verify the correct behavior in BR/EDR security modes. The role of the IUT is Peripheral and acceptor. 

**GAP/SEC/SEM/BV-02-C [Channel Establishment procedure – Security mode 2]** 

- Test Purpose 

Verify that the IUT in security mode 2 performs a channel establishment procedure. 

The IUT is responder. The Lower Tester is initiator of the channel establishment procedure. 

- Reference 

   - [1] 5.2 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **38 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. The IUT has to be configured such that it will not reject the channel establishment procedure. 

   - The BD_ADDR of the IUT is specified by the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

**==> picture [333 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT connected to Lower Tester and in security mode 2<br>L2CAP ConnectReq(Code=0x02,<br>Identifier 1, Length=0x0004, PSM, SCID1)<br>An intermediate<br>Generic Authentication Procedure L2CAP_ConnectRsp(result pending) is<br>possible<br>encryption messages<br>Identifier 1, Length=0x0008, PSM, DCID1,L2CAP_ConnectResp (Code=0x03, Verify that the IUT performs a successful channel establishment<br>Result: Connection successful, Status: N/A) after having performed a link<br>establishment<br>**----- End of picture text -----**<br>


_Figure 4.19: GAP/SEC/SEM/BV-02-C [Channel Establishment procedure – Security mode 2] MSC_ 

   1. After the Upper Tester has ordered the IUT to go in connectable mode, the Lower Tester starts the link establishment with paging. 

   2. If the link establishment was completed, a channel establishment is performed. 

- Expected Outcome 

## Pass verdict 

After the link establishment is completed and a channel establishment was initiated by the Lower Tester (with L2CAP_ConnectReq), the IUT sends the L2CAP_ConnectRsp message with the result: “Connection successful” for completion. 

- Notes 

Recommend to test with connection to protocol/application that requires authentication. 

**GAP/SEC/SEM/BV-04-C [Security mode 4 – Responder]** 

- Test Purpose 

Verify that the IUT in security mode 4 performs a channel establishment procedure. The IUT is responder. The Lower Tester is initiator of the channel establishment procedure. 

- Reference 

[13] 5.2.2 

- Initial Condition 

   - The IUT is in Idle mode. The IUT has to be configured such that it will not reject the channel establishment procedure. 

   - The BD_ADDR of the IUT is specified by the TSPX_bd_addr_iut IXIT value. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **39 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [335 x 377] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in Idle mode.<br>Bring IUT in security mode 4<br>Bring IUT in connectable mode<br>Paging<br>Link Establishment<br>Generic Authentication Procedure<br>Encryption messages<br>L2CAP ConnectReq<br>Channel establishment<br>(Code=0x02, Identifier 1, Length=0x0004,<br>PSM, SCID1) started<br>An intermediate<br>L2CAP_ConnectRsp(result<br>pending) is possible<br>L2CAP_ConnectRsp<br>(Code=0x03, Identifier 1, Length=0x0008,  Verify that the IUT performs a<br>PSM, DCID1, result: Connection successful,  successful channel<br>Status: N/A) establishment after having<br>performed a link establishment<br>by the Lower Tester.<br>**----- End of picture text -----**<br>


_Figure 4.20: GAP/SEC/SEM/BV-04-C [Security mode 4 – Responder] MSC_ 

After the Upper Tester has ordered the IUT to go in connectable mode and in security mode 4, the Lower Tester starts the link establishment with paging. If the link establishment was completed, a channel establishment is performed. 

- 

- Expected Outcome 

## Pass verdict 

After the link establishment is completed and a channel establishment was initiated by the Lower Tester (with L2CAP_ConnectReq), the IUT sends the L2CAP_ConnectRsp message with the result: “Connection successful” for completion. 

- Notes 

Recommend to test with connection to protocol/application that requires authentication. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **40 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/SEM/BV-11-C [Secure Connections Only mode BR/EDR transport – IUT Peripheral, responder, Lower Tester doesn’t support Secure Connections in Controller]** 

- Test Purpose 

The Lower Tester doesn’t support Secure Connections at the Controller level. Verify that the IUT in Secure Connections Only mode rejects a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3 on the IUT. The IUT is Peripheral and responder of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX_psm_sm4I3 IXIT value. 

   - Set the Secure Connections (Controller Support) LMP feature bit on the Lower Tester to 0. 

   - The IUT and the Lower Tester are not bonded (neither IUT nor Lower Tester has link keys). 

   - ACL connection does not exist between the devices. 

- Test Procedure 

**==> picture [338 x 323] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are not bonded (Neither IUT nor Lower tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Secure Connections Only Mode<br>Bring IUT in connectable mode<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing Complete (Authenticated link key)<br>Encryption LMP messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result=Connection<br>refused-security block, status)<br>**----- End of picture text -----**<br>


_Figure 4.21: GAP/SEC/SEM/BV-11-C [Secure Connections Only mode BR/EDR Transport – IUT Peripheral, responder, Lower Tester doesn’t support Secure Connections in Controller] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **41 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Upper Tester puts the IUT in Secure Connections Only mode and connectable mode. 

   2. The Lower Tester creates an ACL connection with the IUT. 

   3. The Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption. The IUT is allowed to reject this pairing procedure. If the IUT rejects the pairing procedure then the test case ends there. 

   4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3. 

- Expected Outcome 

## Pass verdict 

The IUT rejects the pairing procedure OR 

The pairing procedure succeeds and the IUT then rejects the Lower Tester’s request to establish a channel to access a service on the IUT that requires security mode 4 level 3 OR 

The IUT disconnects the ACL connection with error code 0x05 (Authentication Failure). 

- Notes 

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4. 

**GAP/SEC/SEM/BV-12-C [Secure Connections Only mode BR/EDR transport – IUT Peripheral, responder, Lower Tester doesn’t support Secure Connections in Host]** 

- Test Purpose 

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT in Secure Connections Only mode rejects a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3. The IUT is Peripheral and responder of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX_psm_sm4l3 IXIT value. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys). 

   - An ACL connection does not exist between the devices. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **42 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [338 x 326] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are not bonded (Neither IUT nor Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Secure Connections Only Mode<br>Bring IUT in connectable mode<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing Complete (Authenticated link key)<br>Encryption LMP messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result=Connection<br>refused-security block, status)<br>**----- End of picture text -----**<br>


_Figure 4.22: GAP/SEC/SEM/BV-12-C [Secure Connections Only mode BR/EDR transport – IUT Peripheral, responder, Lower Tester doesn’t support Secure Connections in Host] MSC_ 

   1. The Upper Tester puts the IUT in Secure Connections Only mode and connectable mode. 

   2. The Lower Tester creates an ACL connection with the IUT. 

   3. The Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption. The IUT is allowed to reject this pairing procedure. If the IUT rejects the pairing procedure then the test case ends there. 

   4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3. 

- 

- Expected Outcome 

## Pass verdict 

The IUT rejects the pairing procedure OR 

The pairing procedure succeeds and the IUT then rejects the Lower Tester’s request to establish a channel to access a service on the IUT that requires security mode 4 level 3 OR 

The IUT disconnects the ACL connection with error code 0x05 (Authentication Failure). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **43 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Notes 

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4. 

**GAP/SEC/SEM/BI-01-C [Security mode 2 BR/EDR Transport, Responder – Invalid Encryption Key Size]** 

- Test Purpose 

Verify that the IUT in security mode 2 rejects channel establishment with an invalid encryption key size. 

The Lower Tester is initiator of the channel establishment procedure. The IUT is responder. 

- Reference 

[1] 5.2 

- Initial Condition 

   - The Lower Tester is in security mode 2 and thus the IUT operates in security mode 2 during the connection with the Lower Tester. 

   - The IUT is configured such that it will not reject the channel establishment procedure for any other reasons. 

   - The IUT and Lower Tester are in a connection and have exchanged a link key with the correct level of authentication while pairing in security mode 2, either during this connection or in a previous connection with bonding. Link has not yet been encrypted. 

   - The minimum encryption key size supported is defined in the TSPX_Min_Encryption_Key_Size IXIT parameter. 

   - The BD_ADDR of the IUT is specified by the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

**==> picture [336 x 201] intentionally omitted <==**

**----- Start of picture text -----**<br>
Upper Tester<br>L2CAP_Connect Req<br>(Service requiring Security Mode X Level Y)<br>Perform Link Encryption<br>(Lower Tester requests encryption key size KS)<br>[IUT may reject the procedure]<br>L2CAP_ConnectRsp<br>(Rejected due to Connection refused – security block)<br>**----- End of picture text -----**<br>


_Figure 4.23: GAP/SEC/SEM/BI-01-C [Security mode 2 BR/EDR Transport, Responder – Invalid Encryption Key Size] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **44 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

Repeat Steps 1–4 for each value of the encryption key size (in Step 3) in the range [1, TSPX_Min_Encryption_Key_Size – 1]: 

   1. Bring the IUT and the Lower Tester into the Initial Condition. 

   2. The Lower Tester performs a channel establishment procedure for a service requiring security mode 2. 

   3. The IUT triggers link encryption and the Lower Tester requests an encryption key size equal to the value selected for the current iteration. The IUT may accept the key size or may fail the link encryption procedure. 

   4. The IUT rejects the channel establishment after link encryption has been completed. 

- Expected Outcome 

## Pass verdict 

For each requested value of the encryption key size that is less than the minimum supported encryption key size, the IUT rejects the channel establishment over the insufficiently encrypted link. Optionally, the IUT also fails the link encryption procedure or terminates the connection. 

- **4.5.1.1 Security mode 4, Responder – Invalid Encryption Key Size** 

- Test Purpose 

Verify that the IUT in security mode 4 rejects channel establishment with an invalid encryption key size. 

The Lower Tester is initiator of the channel establishment procedure. The IUT is responder. 

- Reference 

[1] 5.2, 5.2.2.8 

- Initial Condition 

   - The IUT is in the security mode and level indicated in the test procedure and is configured such that it will not reject the channel establishment procedure for any other reasons. 

   - The minimum encryption key size supported is defined in the TSPX_Min_Encryption_Key_Size IXIT parameter. 

   - The BD_ADDR of the IUT is specified by the TSPX_bd_addr_iut IXIT value. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|**Minimum Key Size (octets)**|
|---|---|---|
|GAP/SEC/SEM/BI-11-C<br>[Security mode 4 level 1,<br>Responder – Invalid<br>Encryption KeySize]|Security mode 4 level 1|TSPX_Min_Encryption_Key_Size|
|GAP/SEC/SEM/BI-02-C<br>[Security mode 4 level 2,<br>Responder – Invalid<br>Encryption KeySize]|Security mode 4 level 2|TSPX_Min_Encryption_Key_Size|
|GAP/SEC/SEM/BI-03-C<br>[Security mode 4 level 3,<br>Responder – Invalid<br>Encryption KeySize]|Security mode 4 level 3|TSPX_Min_Encryption_Key_Size|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **45 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**TCID**<br>**S**|**ecurity Mode and Level**|**Minimum Key Size (octets)**|
|---|---|---|
|GAP/SEC/SEM/BI-04-C<br>[Security mode 4 level 4,<br>Responder – Invalid<br>Encryption KeySize – 128 bit]<br>S|ecurity mode 4 level 4|16|
|GAP/SEC/SEM/BI-14-C<br>[Security mode 4 level 1,<br>Responder – Invalid<br>Encryption KeySize – 128 bit]<br>S|ecurity mode 4 level 1|16|
|GAP/SEC/SEM/BI-15-C<br>[Security mode 4 level 2,<br>Responder – Invalid<br>Encryption KeySize – 128 bit]<br>S|ecurity mode 4 level 2|16|
|GAP/SEC/SEM/BI-16-C<br>[Security mode 4 level 3,<br>Responder – Invalid<br>Encryption KeySize – 128 bit]<br>S|ecurity mode 4 level 3|16|



_Table 4.2: Security mode 4, Responder – Invalid Encryption Key Size test cases_ 

- Test Procedure 

**==> picture [374 x 267] intentionally omitted <==**

_Figure 4.24: Security mode 4, Responder – Invalid Encryption Key Size MSC_ 

Repeat Steps 1–5 for each value of the encryption key size (in Step 3) in the range [1, Min_Key_Size – 1], where Min_Key_Size is indicated in Table 4.2, column Minimum Key Size, for each test case. 

1. The IUT and the Lower Tester initiate a connection and exchange a link key with the correct level of authentication while pairing in the same security mode and level indicated in the test procedure. The link has not yet been encrypted. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **46 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

2. Bring the IUT and the Lower Tester into the Initial Condition for the security mode and level indicated in Table 4.2, column Security Mode and Level. 

3. The Lower Tester and the IUT perform link encryption, and the Lower Tester requests an encryption key size equal to the value selected for the current iteration. 

4. Perform either alternative 4A or 4B depending on the IUT’s behavior. Alternative 4A (The IUT fails the link encryption procedure): 

   - 4A.1 The IUT rejects the link encryption. 

   - 4A.2 The IUT may disconnect the ACL connection with error code 0x05 (Authentication Failure). 

Alternative 4B (The Link Encryption procedure completes successfully): 

      - 4B.1 The Lower Tester requests a channel establishment for a service requiring the same security mode and level as indicated in Step 1. 

      - 4B.2 The IUT rejects the channel establishment after link encryption has been completed. 

   5. Unless the IUT disconnected the ACL connection in Step 4A.2, the IUT and the Lower Tester disconnect the ACL connection. 

- Expected Outcome 

## Pass verdict 

For each value of the encryption key size tested, the IUT either fails the link encryption procedure or completes the procedure successfully but rejects the channel establishment over the insufficiently encrypted link. 

**GAP/SEC/SEM/BI-05-C [Security mode 2, Initiator – Invalid Key Size]** 

- Test Purpose 

Verify that the IUT in security mode 2 rejects channel establishment with an invalid encryption key size. 

The IUT is initiator of the channel establishment procedure. The Lower Tester is responder. 

- Reference 

[1] 5.2 

- Initial Condition 

   - The Lower Tester is in security mode 2 and thus the IUT operates in security mode 2 during the connection with the Lower Tester. 

   - The IUT and Lower Tester are in a connection and have exchanged a link key with the correct level of authentication while pairing in the same security mode and level indicated in the test procedure, either during this connection or in a previous connection with bonding. Link has not yet been encrypted. 

   - The minimum encryption key size supported is defined in the TSPX_Min_Encryption_Key_Size IXIT parameter. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **47 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [337 x 199] intentionally omitted <==**

**----- Start of picture text -----**<br>
Upper Tester<br>Establish Channel<br>in Security Mode 2<br>Perform Link Encryption<br>(Lower Tester requests encryption key size KS)<br>[IUT may reject the procedure]<br>Channel Establishment Failure:<br>(Rejected due to Connection refused – security<br>block)<br>**----- End of picture text -----**<br>


_Figure 4.25: GAP/SEC/SEM/BI-05-C [Security mode 2, Initiator – Invalid Key Size] MSC_ 

Repeat Steps 1–4 for each value of the encryption key size (in Step 3) in the range [1, TSPX_Min_Encryption_Key_Size – 1]: 

   1. Bring the IUT and the Lower Tester into the Initial Condition. 

   2. The Upper Tester orders the IUT to perform a channel establishment procedure for a service requiring security mode 2. The IUT initiates link encryption. 

   3. In the link encryption phase, the Lower Tester requests an encryption key size equal to the value selected for the current iteration. The IUT may accept the key size or may fail the link encryption procedure. 

   4. The IUT signals to the Upper Tester that the channel establishment failure after link encryption has been completed. 

- Expected Outcome 

## Pass verdict 

For each requested value of the encryption key size that is less than the minimum supported encryption key size, the IUT fails the channel establishment due to the insufficiently encrypted link. Optionally, the IUT also fails the link encryption procedure or terminates the connection. 

- **4.5.1.2 Security mode 4, Initiator – Invalid Encryption Key Size** 

- Test Purpose 

Verify that the IUT in security mode 4 rejects channel establishment with an invalid encryption key size. 

The IUT is initiator of the channel establishment procedure. The Lower Tester is responder. 

- Reference 

   - [1] 5.2 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **48 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is in the security mode and level indicated in the test procedure. 

   - The IUT and Lower Tester are in a connection and have exchanged a link key with the correct level of authentication while pairing in the same security mode and level indicated in the test procedure, either during this connection or in a previous connection with bonding. Link has not yet been encrypted. 

   - The minimum encryption key size supported is defined in the TSPX_Min_Encryption_Key_Size IXIT parameter. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|**Minimum Key Size (octets)**|
|---|---|---|
|GAP/SEC/SEM/BI-12-C<br>[Security mode 4 level 1,<br>Initiator – Invalid Encryption<br>KeySize]|Security mode 4 level 1|TSPX_Min_Encryption_Key_Size|
|GAP/SEC/SEM/BI-06-C<br>[Security mode 4 level 2,<br>Initiator – Invalid Encryption<br>KeySize]|Security mode 4 level 2|TSPX_Min_Encryption_Key_Size|
|GAP/SEC/SEM/BI-07-C<br>[Security mode 4 level 3,<br>Initiator – Invalid Encryption<br>KeySize]|Security mode 4 level 3|TSPX_Min_Encryption_Key_Size|
|GAP/SEC/SEM/BI-08-C<br>[Security mode 4 level 4,<br>Initiator – Invalid Encryption<br>KeySize – 128 bit]|Security mode 4 level 4|16|
|GAP/SEC/SEM/BI-17-C<br>[Security mode 4 level 1,<br>Initiator – Invalid Encryption<br>KeySize – 128 bit]|Security mode 4 level 1|16|
|GAP/SEC/SEM/BI-18-C<br>[Security mode 4 level 2,<br>Initiator – Invalid Encryption<br>KeySize – 128 bit]|Security mode 4 level 2|16|
|GAP/SEC/SEM/BI-19-C<br>[Security mode 4 level 3,<br>Initiator – Invalid Encryption<br>KeySize – 128 bit]|Security mode 4 level 3|16|



_Table 4.3: Security mode 4, Initiator – Invalid Encryption Key Size test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **49 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [337 x 199] intentionally omitted <==**

**----- Start of picture text -----**<br>
Upper Tester<br>Establish Channel<br>in Security Mode 4 Level Y<br>Perform Link Encryption<br>(Lower Tester requests encryption key size KS)<br>[IUT may reject the procedure]<br>Channel Establishment Failure:<br>(Rejected due to Connection refused – security<br>block)<br>**----- End of picture text -----**<br>


_Figure 4.26: Security mode 4, Initiator – Invalid Encryption Key Size MSC_ 

Repeat Steps 1–4 for each value of the encryption key size (in Step 3) in the range [1, (Min_Key_Size – 1)], where Min_Key_Size is indicated in Table 4.3, column Minimum Key Size, for each test case. 

   1. Bring the IUT and the Lower Tester into the Initial Condition for the security mode and level indicated in Table 4.3, column Security Mode and Level. 

   2. The Upper Tester orders the IUT to perform a channel establishment procedure for a service requiring the same security mode and level as indicated in Step 1 and minimum key size indicated in Table 4.3. The IUT initiates link encryption with the Lower Tester. 

   3. In the link encryption phase, the Lower Tester requests an encryption key size equal to the value selected for the current iteration. The IUT may accept the key size or may fail the link encryption procedure. 

   4. The IUT signals to the Upper Tester that the channel establishment failure after link encryption has been completed. 

- Expected Outcome 

## Pass verdict 

For each requested value of the encryption key size that is less than the minimum required by the security mode and level under test, the IUT fails the channel establishment due to the insufficiently encrypted link. Optionally, the IUT also fails the link encryption procedure or terminates the connection. 

**GAP/SEC/SEM/BI-24-C [Security mode 4, Unencrypted connections rejected – Responder]** 

- Test Purpose 

Verify that the IUT disconnects the connection if the initiating side sends the L2CAP_ConnectReq without first enabling encryption. 

- Reference 

[13] 5.2.2 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **50 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - Write_Authentication_Enable (disabled) on IUT. 

   - Write_Simple_Pairing_Mode is set (enabled) on the Lower Tester acting as responder. 

   - The IUT and the Lower Tester are not Bonded. 

- Test Procedure 

**==> picture [330 x 308] intentionally omitted <==**

_Figure 4.27: Security mode 4, Unencrypted connections rejected – Responder MSC_ 

   1. The Lower Tester creates an ACL connection with the IUT. 

   2. The Authentication_Requirements are set to “MITM Protection Not Required No Bonding” (0x00) on the Lower Tester. 

   3. The Lower Tester sends L2CAP_ConnectReq without performing Secure Simple Pairing and without enabling encrypting. 

- 

- Expected Outcome 

## Pass verdict 

Based on ALT 1 shown in Figure 4.27, the test results in pass when the IUT initiates the Secure Simple Pairing procedure autonomously before the Lower Tester initiates the L2CAP connection. Verify that the IUT authenticates the Lower Tester. 

Based on ALT 2 shown in Figure 4.27, the test will result in pass when the IUT rejects the L2CAP connection and disconnects the ACL link with error code authentication failure 0x05. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **51 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.5.1.3 Secure Connections Only mode BR/EDR transport – IUT Peripheral, responder, Lower Tester supports Secure Connections in Controller and Host** 

- Test Purpose 

The Lower Tester supports Secure Connections both at the Controller and Host level. Verify that the IUT in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3. The IUT is Peripheral and responder of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX_psm_sm4l3 IXIT value. 

   - Set both the Secure Connections (Controller Support) and the Secure Connections (Host Support) LMP feature bits on the Lower Tester to 1. 

   - The IUT and the Lower Tester are bonded as specified in Table 4.4. 

   - ACL connection does not exist between the devices. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-13-C|Not Bonded, No Link Keys|Secure Simple Pairing|
|GAP/SEC/SEM/BV-47-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.4: Secure Connections Only mode – IUT Peripheral, responder, Lower Tester supports Secure Connections in Controller and Host test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **52 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [337 x 340] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Secure Connections Only Mode<br>Bring IUT in connectable mode<br>NO LINK KEY<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing Complete (Authenticated link key)<br>LINK KEY<br>Generic Authentication Procedure<br>Encryption LMP messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result=Connection<br>successful, status)<br>**----- End of picture text -----**<br>


_Figure 4.28: Secure Connections Only mode BR/EDR transport – IUT Peripheral, responder, Lower Tester supports Secure Connections in Controller and Host MSC_ 

   1. The Upper Tester puts the IUT in Secure Connections Only mode and connectable mode. 

   2. The Lower Tester creates an ACL connection with the IUT. 

   3. If the test requires Secure Simple Pairing, the Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption. 

   4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3. 

- 

- Expected Outcome 

## Pass verdict 

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester. 

The IUT accepts the Lower Tester’s request to establish a channel to access a service on the IUT that requires security mode 4 level 3 and the channel establishment procedure is successful. 

- 

- Notes 

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **53 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.5.1.4 IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host** 

- Test Purpose 

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3. The IUT is Peripheral and responder of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX_psm_sm4l3 IXIT value. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - The IUT and the Lower Tester are bonded as specified in Table 4.5. 

   - ACL connection does not exist between the devices. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-14-C|Not Bonded, No Link Keys|Secure Simple Pairing|
|GAP/SEC/SEM/BV-48-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.5: IUT Peripheral, responder, not in Secure Connections Only mode, Lower Tester does not support Secure Connections in Host test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **54 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [337 x 341] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Security Mode 4 (but not in Secure<br>Connections Only Mode)<br>Bring IUT in connectable mode<br>NO LINK KEY<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing Complete (Authenticated link key)<br>LINK KEY<br>Generic Authentication Procedure<br>Encryption LMP messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result=Connection<br>successful, status)<br>**----- End of picture text -----**<br>


_Figure 4.29: IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host MSC_ 

   1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode) and connectable mode. 

   2. The Lower Tester creates an ACL connection with the IUT. 

   3. If the test requires Secure Simple Pairing, the Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption. 

   4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3. 

- 

- Expected Outcome 

## Pass verdict 

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester. 

The IUT accepts the Lower Tester’s request to establish a channel to access a service on the IUT that requires security mode 4 level 3 and the channel establishment procedure is successful. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **55 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.5.1.5 IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service** 

- Test Purpose 

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode rejects a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 4. The IUT is Peripheral and responder of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX_psm_sm4l4 IXIT value. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - IUT and Lower Tester are bonded as specified in Table 4.6. 

   - ACL connection does not exist between the devices. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-15-C|Not Bonded, No Link Keys|Secure Simple Pairing|
|GAP/SEC/SEM/BV-49-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.6: IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **56 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [337 x 342] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Security Mode 4 (but not in Secure<br>Connections Only Mode)<br>Bring IUT in connectable mode<br>NO LINK KEY<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing Complete (Authenticated link key)<br>LINK KEY<br>Generic Authentication Procedure<br>Encryption LMP messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result=Connection<br>refused-security block, status)<br>**----- End of picture text -----**<br>


_Figure 4.30: IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR Transport, Lower Tester does not support Secure Connections in Host, level 4 service MSC_ 

   1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode) and connectable mode. 

   2. The Lower Tester creates an ACL connection with the IUT. 

   3. The Lower Tester performs the Secure Simple Pairing procedure that results an authenticated link key and enables encryption. 

   4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 4. 

- 

- Expected Outcome 

## Pass verdict 

If the test requires Secure Simple Pairing, the Secure Simple Pairing procedure between the IUT and the Lower Tester is successful. 

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester. 

The IUT rejects the Lower Tester’s request to establish a channel to access a service on the IUT that requires security mode 4 level 4. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **57 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.2 LE security modes – Peripheral** 

Verify the correct behavior in LE security modes. The role of the IUT is Peripheral. 

## **4.5.2.1 LE Secure Connections, Peripheral – outgoing service level connection** 

- Test Purpose 

Verify that the IUT, supporting LE Secure Connections, performing the authentication procedure will achieve a connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Peripheral. 

- Reference 

   - [9] 10.3 

- Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The Lower Tester will establish a GATT service request when TSPX_Use_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|
|---|---|
|GAP/SEC/SEM/BV-21-C [LE security mode: mode 1 level 4,<br>Peripheral – outgoingservice level connection]|LE security mode 1 level 4|
|GAP/SEC/SEM/BV-37-C [LE Secure Connections Only: mode 1<br>level 2, Peripheral – outgoingservice level connection]|LE security mode 1 level 2|
|GAP/SEC/SEM/BV-38-C [LE Secure Connections Only: mode 1<br>level 3, Peripheral – outgoingservice level connection]|LE security mode 1 level 3|



_Table 4.7: LE Secure Connections, Peripheral – outgoing service level connection test cases_ 

- Test Procedure 

   1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.7. 

   2. The Upper Tester configures the IUT to advertise (in Peripheral role) for a connection by the Lower Tester (in Central role), and accept link establishment. 

   3. The Upper Tester triggers the authentication procedure on the IUT, e.g., by an L2CAP channel establishment or a GATT service request. 

   4. The IUT begins LE Secure Connections Phase 1 by sending an SMP Security Request, with the Secure Connections bit set to 1. The Lower Tester responds with an SMP Pairing Request, with the Secure Connections bit set to 1. The IUT answers with SMP Pairing Response, with the Secure Connections bit set to 1. 

   5. The Lower Tester and the IUT complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   6. The IUT replies with a successful response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **58 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [326 x 499] intentionally omitted <==**

_Figure 4.31: LE Secure Connections, Peripheral – outgoing service level connection MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted and operating in the security mode and level specified in Table 4.7. 

- 

- Notes 

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.7. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **59 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.5.2.2 LE Secure Connections, Peripheral – incoming service level connection** 

- Test Purpose 

Verify that the IUT, supporting LE Secure Connections, after performing the authentication procedure will achieve an incoming service level connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Peripheral. 

- Reference 

   - [9] 10.3.1 

- Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The Lower Tester will establish a GATT service request when TSPX_Use_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|
|---|---|
|GAP/SEC/SEM/BV-22-C [LE security mode: mode 1 level 4,<br>Peripheral – incomingservice level connection]|LE security mode 1 level 4|
|GAP/SEC/SEM/BV-39-C [LE Secure Connections Only: mode 1<br>level 2, Peripheral – incomingservice level connection]|LE security mode 1 level 2|
|GAP/SEC/SEM/BV-40-C [LE Secure Connections Only: mode 1<br>level 3, Peripheral – incomingservice level connection]|LE security mode 1 level 3|



_Table 4.8: LE Secure Connections, Peripheral – incoming service level connection test cases_ 

- Test Procedure 

   1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.8. 

   2. The Upper Tester configures the IUT to advertise (in Peripheral role) for a connection by the Lower Tester (in Central role), and accept link establishment. 

   3. The Lower Tester initiates LE Secure Connections pairing according to the security mode and level specified in Table 4.8. 

   4. The Lower Tester and the IUT complete SMP Phase 1, Phase 2 (pairing), and Phase 3 (encryption and key distribution). 

   5. The Lower Tester sends either an L2CAP channel establishment or GATT service request to the IUT. 

   6. The IUT replies with a successful response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **60 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [328 x 355] intentionally omitted <==**

_Figure 4.32: LE Secure Connections, Peripheral – incoming service level connection MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted on the security mode and level specified in Table 4.8. 

The initiated procedure is successful. 

- 

- Notes 

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.8. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **61 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/SEM/BV-23-C [Secure Connections Only mode LE transport – failed procedure, Peripheral – outgoing service level connection]** 

- Test Purpose 

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only initiating the authentication procedure will result in a failed procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Peripheral. 

- Reference 

   - [9] 10.2.4, 10.3 

- Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The Lower Tester is configured so that it does not support LE Secure Connections. 

- The IUT will initiate a GATT service request when TSPX_Use_GATT is set to TRUE. Otherwise, the IUT will establish an L2CAP channel. 

- Test Procedure 

   1. The Upper Tester configures the IUT into Secure Connections Only mode or to only support LE Secure Connections. 

   2. The Upper Tester configures the IUT (in Peripheral role) to send advertising packets to the Lower Tester (in Central role), and complete link establishment with the Lower Tester. 

   3. The Upper Tester triggers the authentication procedure on the IUT, e.g., by an L2CAP channel establishment or a GATT service request. 

   4. The IUT begins the LE Pairing Procedure Phase 1 by sending an SMP Security Request, with the Secure Connections bit set to 1. 

   5. The Lower Tester responds with an SMP Pairing Request, with the Secure Connections bit set to 0. 

   6. Alternative 1: (for security mode 1 level 4 connections): 

      - a. The IUT responds with an SMP Pairing Failed message. 

   7. Alternative 2: (for security mode 1 level 2 or 3 with Secure Connections): 

      - a. The IUT responds with an SMP Pairing Response. 

      - b. The IUT and the Lower Tester complete the LE Legacy Pairing procedure. 

      - c. The IUT responds with a failure message. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **62 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [145 x 51] intentionally omitted <==**

**==> picture [290 x 181] intentionally omitted <==**

_Figure 4.33: GAP/SEC/SEM/BV-23-C [Secure Connections Only mode LE transport – failed procedure, Peripheral – outgoing service level connection] MSC_ 

- Expected Outcome 

## Pass verdict 

In ALT 1, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1. 

In ALT 2, the IUT does not complete the L2CAP Channel establishment or GATT service request. 

**GAP/SEC/SEM/BV-24-C [Secure Connections Only mode LE transport – failed procedure, Peripheral – incoming service level connection]** 

- Test Purpose 

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only rejects an L2CAP channel establishment or GATT service request both before and after the authentication procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Peripheral. 

- Reference 

[9] 10.2.4, 10.3.1 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **63 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject a correctly initiated procedure to either establish an L2CAP channel or a GATT service request. 

   - The Lower Tester is configured so that it does not support LE Secure Connections. 

   - The Lower Tester will establish a GATT service request when TSPX_Use_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel. 

- Test Procedure 

   1. The Upper Tester configures the IUT into Secure Connections Only mode or to only support LE Secure Connections. 

   2. The Upper Tester configures the IUT (in Peripheral role) to send advertising packets to the Lower Tester (in Central role), and complete link establishment with the Lower Tester. 

   3. The Lower Tester initiates either an L2CAP channel establishment or GATT service request to the IUT. 

   4. The IUT rejects the request. 

   5. The Lower Tester initiates authenticated LE Legacy pairing. 

   6. Alternative 1: The IUT rejects the pairing by sending an SMP Pairing Failed message. Alternative 2: The Lower Tester and the IUT complete LE legacy pairing. The Lower Tester reinitiates the procedure request to the IUT as attempted in Step 3. The IUT rejects the request. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **64 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [272 x 400] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Lower Tester finds IUT<br>Establishes LE connection<br>ALT A GATT service request<br>ALT B L2CAP channel<br>establishment<br>Request rejected<br>SMP Pairing Req.<br>AuthReq.SC=0<br>SMP Pairing Failed<br>Auth. Requirements ALT 1<br>ALT 2<br>LE Legacy Pairing<br>ALT A GATT service request<br>ALT B L2CAP channel<br>establishment<br>Request Rejected<br>“Insufficient Authentication”<br>**----- End of picture text -----**<br>


_Figure 4.34: GAP/SEC/SEM/BV-24-C [Secure Connections Only mode LE transport – failed procedure, Peripheral – incoming service level connection] MSC_ 

- Expected Outcome 

## Pass verdict 

The L2CAP channel establishment or GATT service request is rejected before the authentication procedure. 

Alternative 1: IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1. 

Alternative 2: The IUT and the Lower Tester complete LE legacy pairing and the IUT rejects the initiated procedure request from the Lower Tester with the error code “Insufficient Authentication”. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **65 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/SEM/BV-25-C [Secure Connections Only mode LE transport, Peripheral, Failure, BR/EDR and LE transports]** 

- Test Purpose 

Verify that the IUT in Secure Connections Only mode performs either an L2CAP channel establishment or GATT service request procedure over LE and a channel establishment procedure over BR/EDR. The IUT is initiator of the procedure over both LE and BR/EDR. The Lower Tester supports neither LE Secure Connections nor BR/EDR Secure Connections. The procedure fails over both LE and BR/EDR. The IUT is the Peripheral. 

- Reference 

   - [9] 10.2.4 

- Initial Condition 

   - The IUT supports both LE Secure Connections and BR/EDR Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The Lower Tester is configured so that it does not support LE Secure Connections and BR/EDR Secure Connections. 

   - The PSM for the service on the IUT that requires security mode 4 level 3 on BR/EDR is specified in the TSPX_psm_sm4l3 IXIT value. 

   - The IUT and the Lower Tester are not bonded on BR/EDR (neither the IUT nor the Lower Tester has link keys). 

   - A BR/EDR ACL connection does not exist between the devices. 

- Test Procedure 

   1. The Upper Tester configures the IUT into Secure Connections Only mode. 

   2. The Upper Tester configures the IUT (in Peripheral role) to send advertising packets to the Lower Tester (in Central role), and complete link establishment with the Lower Tester. 

   3. The IUT begins the LE Pairing Procedure Phase 1 by sending an SMP Security Request, with the Secure Connections bit set to 1. The Lower Tester responds with an SMP Pairing Request, with the Secure Connections bit set to 0. The IUT will respond with an SMP Pairing Failed message. 

   4. The IUT terminates the LE connection. 

   5. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT. 

   6. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **66 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [265 x 352] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>Lower Tester finds IUT<br>Establishes LE connection<br>ALT GATT service request<br>L2CAP channel<br>establishment<br>SMP Security Req.<br>LE Secure AuthReq.SC=1<br>Connections<br>Phase 1 SMP Pairing Req.<br>AuthReq.SC=0<br>SMP Pairing Failed<br>Auth. Requirements<br>ALT GATT service request<br>failure<br>L2CAP channel<br>establishment failure<br>Terminate LE connection Initiate action to<br>trigger an L2CAP<br>connection with<br>BR/EDR L2CAP channel  the tester<br>establishment<br>Establish ACL connection The IUT is allowed to reject the Upper Tester’s request at<br>either of the following steps:<br>1. When the IUT reads the Lower Tester’s LMP features<br>and sees that it does not support BR/EDR Secure<br>Connections.<br>2. At the end of the Secure Simple Pairing Procedure when<br>the IUT sees that the Link Key is not strong enough.<br>Request rejected<br>**----- End of picture text -----**<br>


_Figure 4.35: GAP/SEC/SEM/BV-25-C [Secure Connections Only mode LE transport, Peripheral, Failure, BR/EDR and LE Transports] MSC_ 

- Expected Outcome 

## Pass verdict 

On the LE transport, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1. 

On the BR/EDR transport, the IUT rejects the Upper Tester’s request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT. 

- **4.5.2.3 LE security mode 1, Peripheral – Invalid Encryption Key Size** 

- Test Purpose 

Verify that the IUT in LE security mode 1 as Peripheral fails pairing when receiving an invalid key size. 

- Reference 

   - [9] 10.3.2, 10.2.1 

- 

- Initial Condition 

- The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **67 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|
|---|---|
|GAP/SEC/SEM/BI-09-C [LE security mode 1 level 4,<br>Peripheral – Invalid Encryption KeySize]|Security mode 1 level 4|
|GAP/SEC/SEM/BI-20-C [Security mode 1 level 3,<br>Peripheral – Invalid Encryption KeySize]|Security mode 1 level 3 with LE<br>Secure Connections Pairingonly|
|GAP/SEC/SEM/BI-21-C [Security mode 1 level 2,<br>Peripheral – Invalid Encryption KeySize]|Security mode 1 level 2 with LE<br>Secure Connections Pairingonly|



_Table 4.9: LE security mode 1, Peripheral – Invalid Encryption Key Size test cases_ 

- Test Procedure 

**==> picture [271 x 214] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(Central) (Peripheral)<br>Repeat for each KS in the range [7,15]<br>IUT is configured in Security Mode 1 Level 4<br>Lower Tester has established an LE connection with the IUT<br>SMP Pairing Request<br>(AuthReq: SC=1<br>Maximum Encryption Key<br>Size=KS)<br>SMP Pairing Failed<br>Reason=Encryption Key<br>Size (0x06)<br>Terminate LE connection<br>**----- End of picture text -----**<br>


_Figure 4.36: LE security mode 1, Peripheral – Invalid Encryption Key Size MSC_ 

Repeat Steps 1–5 for all values of the Maximum Encryption Key Size field (in Step 3) in the interval [7, 15]. 

   1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.9 2. The Upper Tester configures the IUT to advertise (in Peripheral role) for a connection by the Lower Tester (in Central role), and to accept link establishment. 

   3. The Lower Tester initiates pairing by sending an SMP Pairing Request, with the Secure Connections bit set to 1 and Maximum Encryption Key Size set to the value selected for this iteration. 

   4. The IUT sends to the Lower Tester an SMP Pairing Failed with the Reason set to “Encryption Key Size” (0x06). 

   5. The Lower Tester terminates the LE connection. 

- Expected Outcome 

## Pass verdict 

The IUT fails pairing for any key size value less than 16 while in the specified security mode and level. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **68 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.3 BR/EDR security modes – Central** 

Verify the correct behavior in BR/EDR security modes. The role of the IUT is Central and initiator. 

## **4.5.3.1 Security mode 4 – Unauthenticated Link Key – Initiator** 

- Test Purpose 

Verify that the IUT in security mode 4 performs a channel establishment procedure. The Lower Tester is responder. The IUT is initiator of the channel establishment procedure. 

- Reference [13] 5.2.2 

- Initial Condition 

   - Write_Authentication_Enable (disabled) on the IUT. 

   - Write_Simple_Pairing_Mode is set (enabled) on the Lower Tester acting as responder. 

   - The IUT has link keys as specified in Table 4.10. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-05-C|<br>Not Bonded, No Link Key|s<br>Secure Simple Pairing|
|GAP/SEC/SEM/BV-50-C|<br>Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.10: Security mode 4 – Unauthenticated Link Key – Initiator test cases_ 

- Test Procedure 

**==> picture [293 x 237] intentionally omitted <==**

_Figure 4.37: Security mode 4 – Unauthenticated Link Key – Initiator MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **69 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

1. The IUT creates an L2CAP connection to the Lower Tester. 

2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.10. 

Alternative 2A (Secure Simple Pairing): 

- 2A.1 Set Authentication Requirements to MITM protection not required and no bonding on IUT. 

- 2A.2 Set Authentication Requirements to MITM protection not required and no bonding on the Lower Tester. 

- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an unauthenticated link key. 

Alternative 2B (Generic authentication procedure): 

      - 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure. 

   3. The IUT sends an L2CAP_CONNECTION_REQ PDU to the Lower Tester. 

   4. The Lower Tester sends an L2CAP_CONNECTION_RSP PDU to the IUT. 

- Expected Outcome 

## Pass verdict 

In Step 2A, verify that secure simple pairing occurs prior to sending the L2CAP_ConnectReq and before the L2CAP_ConnectRsp is received, and results in an unauthenticated link key. 

In Step 2B, verify that the IUT authenticates the Lower Tester. 

Verify that encryption is enabled. 

- **4.5.3.2 Security mode 4 – Authenticated Link Key No MITM – Initiator** 

- Test Purpose 

Verify that secure simple pairing occurs prior to sending the L2CAP_ConnectReq and before the L2CAP_ConnectRsp is received, and results in an authenticated link key. 

- Reference 

[13] 5.2.2 

- Initial Condition 

   - Write_Authentication_Enable (disabled) on the IUT. 

   - Write_Simple_Pairing_Mode is set (enabled) on the Lower Tester acting as responder. 

   - The IUT has link keys as specified in Table 4.11. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-06-C|Not Bonded, No Link Keys|Secure Simple Pairing|
|GAP/SEC/SEM/BV-51-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.11: Security mode 4 – Authenticated Link Key No MITM – Initiator test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **70 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [293 x 236] intentionally omitted <==**

_Figure 4.38: Security mode 4 – Authenticated Link Key No MITM – Initiator MSC_ 

1. The IUT creates an L2CAP connection to the Lower Tester. 

2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.11. 

Alternative 2A (Secure Simple Pairing): 

- 2A.1 Set Authentication Requirements to MITM protection not required and no bonding on IUT. 

- 2A.2 Set Authentication Requirements to MITM protection required and no bonding on the Lower Tester. 

- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an authenticated link key. 

Alternative 2B (Generic authentication procedure): 

   - 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure. 

3. The IUT sends an L2CAP_CONNECTION_REQ PDU to the Lower Tester. 

4. The Lower Tester sends an L2CAP_CONNECTION_RSP PDU to the IUT. 

- Expected Outcome 

## Pass verdict 

In Step 2A, verify that secure simple pairing occurs prior to sending the L2CAP_ConnectReq and before the L2CAP_ConnectRsp is received, and results in an authenticated link key. 

In Step 2B, verify that the IUT authenticates the Lower Tester. 

Verify that encryption is enabled. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **71 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.3.3 Security mode 4 – Authenticated Link Key MITM – Initiator** 

- Test Purpose 

Verify that secure simple pairing occurs before the L2CAP_ConnectReq is sent and results in an authenticated link key. 

- Reference [13] 5.2.2 

- Initial Condition 

   - Write_Authentication_Enable (disabled) on the IUT. 

   - Write_Simple_Pairing_Mode is set (enabled) on the Lower Tester acting as responder. 

   - The IUT has link keys as specified in Table 4.12. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-07-C|Not Bonded, No Link Ke|ys<br>Secure Simple Pairing|
|GAP/SEC/SEM/BV-52-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.12: Security mode 4 – Authenticated Link Key MITM – Initiator test cases_ 

- Test Procedure 

**==> picture [293 x 236] intentionally omitted <==**

_Figure 4.39: Security mode 4 – Authenticated Link Key MITM – Initiator MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **72 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

1. The IUT creates an L2CAP connection to the Lower Tester. 

2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.12. 

Alternative 2A (Secure Simple Pairing): 

- 2A.1 Set Authentication_Requirements to “MITM Protection Required – No Bonding” (0x01) on IUT. 

- 2A.2 Set Authentication_Requirements to “MITM Protection Not Required – No Bonding” (0x00) on the Lower Tester. 

- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an authenticated link key. 

Alternative 2B (Generic authentication procedure): 

      - 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure. 

   3. The IUT sends an L2CAP_CONNECTION_REQ PDU to the Lower Tester. 

   4. The Lower Tester sends an L2CAP_CONNECTION_RSP PDU to the IUT. 

- Expected Outcome 

## Pass verdict 

In Step 2A, verify that secure simple pairing occurs before the L2CAP_ConnectReq is sent, and results in an authenticated link key. 

In Step 2B, verify that the IUT authenticates the Lower Tester. 

Verify that encryption is enabled. 

**GAP/SEC/SEM/BV-08-C [Security mode 4 – Initiator]** 

- Test Purpose 

Verify that authentication succeeds and occurs before the L2CAP Connection request. 

- Reference 

   - [13] 5.2.2 

- Initial Condition 

   - Write_Authentication_Enable (disabled) on the IUT. 

   - Write_Simple_Pairing_Mode is set (enabled). 

   - Link key is on IUT and responder. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **73 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [339 x 215] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded by Secure Simple Pairing. (i.e,. Both IUT and Lower Tester have link keys)<br>ACL link does not exist between the devices.<br>Bring IUT in Security Mode 4<br>Initiate action to trigger an L2CAP Connection with the<br>Lower Tester<br>Establish ACL link<br>Authentication procedure<br>Encryption messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result, status)<br>**----- End of picture text -----**<br>


_Figure 4.40: GAP/SEC/SEM/BV-08-C [Security mode 4 – Initiator] MSC_ 

The IUT creates L2CAP connection to the Lower Tester. 

- Expected Outcome 

## Pass verdict 

Verify that authentication succeeds and occurs before the L2CAP_ConnectReq. 

Verify that encryption is enabled. 

- **4.5.3.4 Security mode 4 – Link Key Upgrade – Initiator** 

- Test Purpose 

Verify that a link key can be upgraded from unauthenticated to authenticated. 

- Reference 

   - [13] 5.2.2 

- Initial Condition 

   - Write_Authentication_Enable (disabled) on the IUT. 

   - Write_Simple_Pairing_Mode is set (enabled) on the Lower Tester acting as responder. 

   - The IUT has link keys as specified in Table 4.13. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-09-C|Not Bonded, No Link Keys|Secure Simple Pairing|
|GAP/SEC/SEM/BV-53-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.13: Security mode 4 – Link Key Upgrade – Initiator test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **74 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [326 x 263] intentionally omitted <==**

**==> picture [166 x 42] intentionally omitted <==**

**==> picture [312 x 200] intentionally omitted <==**

_Figure 4.41: Security mode 4 – Link Key Upgrade – Initiator MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **75 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

1. The IUT creates an L2CAP connection to the Lower Tester. 

2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.13. 

Alternative 2A (Secure Simple Pairing): 

- 2A.1 Set Authentication_Requirements to “MITM Protection Not Required – No Bonding” (0x00) on the IUT. 

- 2A.2 Set Authentication_Requirements to “MITM Protection Not Required – No Bonding” (0x00) on the responder. 

- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an un-authenticated link key. 

Alternative 2B (Generic authentication procedure): 

   - 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure. 

3. The IUT initializes a second service to the Lower Tester that requires an authenticated link key. 

4. Perform either alternative 4A or 4B depending on the pairing/authentication procedure specified in Table 4.13. 

Alternative 4A (Secure Simple Pairing): 

- 4A.1 Set Authentication_Requirements to “MITM Protection Required – No Bonding” (0x01) on the IUT. 

- 4A.2 Set Authentication_Requirements to “MITM Protection Required – No Bonding” (0x01) on the responder. 

- 4A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an authenticated link key. 

Alternative 4B (Generic authentication procedure): 

      - 4B.1 The IUT and the Lower Tester execute the Generic authentication procedure. 

   5. The IUT and the Lower Tester pause and resume encryption. 

   6. The IUT sends an L2CAP_CONNECTION_REQ PDU to the Lower Tester. 

   7. The Lower Tester sends an L2CAP_CONNECTION_RSP PDU to the IUT. 

- Expected Outcome 

## Pass verdict 

In Step 2A, verify that secure simple pairing occurs prior to sending the L2CAP_ConnectReq and before the L2CAP_ConnectRsp is received, and results in an unauthenticated link key. 

Verify that the IUT authenticates the Lower Tester. 

Verify that encryption is enabled. 

In Step 4A, on second service initialization, verify that Secure Simple Pairing occurs before the L2CAP_ConnectReq and results in an authenticated link key. 

In Step 4B, on second service initialization, verify that the IUT authenticates the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **76 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.3.5 Security mode 4 – Responder** 

- Test Purpose 

Verify that the IUT fails and disconnects the connection if the initiating side sends the L2CAP Connection Request as specified in Table 4.14 without first enabling encryption. 

- Reference 

   - [17] 5.2.2 

- Initial Condition 

   - Write_Authentication_Enable (disabled) on the IUT. 

   - Write_Simple_Pairing_Mode is set (enabled) on the Lower Tester acting as responder. 

   - No link key is on the IUT. 

- Test Case Configuration 

|**Test Case ID**|**L2CAP Command**|**L2CAP Response**|**Response**<br>**Result Code**|
|---|---|---|---|
|GAP/SEC/SEM/BV-10-C|L2CAP_CONNECTION_REQ|L2CAP_CONNECTION_RSP|0x0003|
|GAP/SEC/SEM/BV-46-C|L2CAP_CREDIT_BASED_<br>CONNECTION_REQ|L2CAP_CREDIT_BASED_<br>CONNECTION_RSP|0x0005,<br>0x0006,<br>0x0007,<br>0x0008|



_Table 4.14: Security mode 4 – Responder test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **77 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [430 x 478] intentionally omitted <==**

_Figure 4.42: Security mode 4 – Responder MSC_ 

1. The Lower Tester creates L2CAP connection to the IUT. 

2. Perform either alternative 2A or 2B depending on the Connect Request type specified in Table 

   - 4.14. 

Alternative 2A (Connection Request): 

- 2A.1 Set Authentication_Requirements to “MITM Protection Not Required No Bonding” (0x00) on the IUT. 

- 2A.2 Set Authentication_Requirements to “MITM Protection Not Required No Bonding” (0x00) on the responder. 

- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an un-authenticated link key. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **78 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

      - 2A.4 The Lower Tester sends the L2CAP command in Table 4.14 to the IUT. 

   - 2A.5 The IUT sends an L2CAP Response command in Table 4.14 to the Lower Tester. 

   - Alternative 2B (Credit-based Connection Request): 

      - 2B.1 The Lower Tester sends the L2CAP command in Table 4.14 to the IUT. 

      - 2B.2 The IUT may send an L2CAP Response command in Table 4.14 to the Lower Tester with Result Pending. 

      - 2B.3 The IUT sends a Disconnect ACL Link to the Lower Tester with Authentication Failure. 

- Expected Outcome 

## Pass verdict 

Based on ALT 2A shown in Figure 4.42: Security mode 4 – Responder the test results in pass when the IUT initiates the Secure Simple Pairing procedure autonomously before the Lower Tester initiates the L2CAP connection. Verify that the IUT authenticates the Lower Tester. 

Based on ALT 2B shown in Figure 4.42: Security mode 4 – Responder the test will result in pass when the IUT rejects the L2CAP connection with the L2CAP Response containing a result code in Table 4.14 and disconnects the ACL link with error code authentication failure 0x05. 

**GAP/SEC/SEM/BV-16-C [Secure Connections Only mode – IUT Central, initiator, Lower Tester doesn’t support Secure Connections in Controller]** 

- Test Purpose 

The Lower Tester doesn’t support Secure Connections at the Controller level. Verify that the IUT in Secure Connections Only mode rejects a request to perform a channel establishment procedure if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure. 

- Reference 

[1] 5.2.2 

- Initial Condition 

   - The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX_psm_sm4l3 IXIT value. 

   - Set the Secure Connections (Controller Support) LMP feature bit on the Lower Tester to 0. 

   - The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys). 

   - An ACL connection does not exist between the devices. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **79 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [376 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are not bonded (Neither IUT nor Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Secure Connections Only Mode<br>Initiate action to trigger an L2CAP connection with the<br>Lower Tester<br>The IUT is optionally allowed<br>Establish ACL connection to perform the Secure Simple<br>Pairing procedure before<br>rejecting the Upper Tester’s<br>request.<br>Request rejected<br>**----- End of picture text -----**<br>


**==> picture [46 x 32] intentionally omitted <==**

_Figure 4.43: GAP/SEC/SEM/BV-16-C [Secure Connections Only mode – IUT Central, initiator, Lower Tester doesn’t support Secure Connections in Controller] MSC_ 

   1. The Upper Tester puts the IUT in Secure Connections Only mode. 

   2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT. 

   3. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT rejects the Upper Tester’s request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT. 

- Notes 

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4. 

**GAP/SEC/SEM/BV-17-C [Secure Connections Only mode – IUT Central, initiator, Lower Tester doesn’t support Secure Connections in Host]** 

- Test Purpose 

The Lower Tester doesn’t support Secure Connections at the Host level. Verify that the IUT in Secure Connections Only mode rejects a request to perform a channel establishment procedure if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX_psm_sm4l3 IXIT value. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **80 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys). 

   - An ACL connection does not exist between the devices. 

- Test Procedure 

**==> picture [376 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are not bonded (Neither IUT nor Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Secure Connections Only Mode<br>Initiate action to trigger an L2CAP connection with the Lower<br>Tester<br>Establish ACL connection The IUT is optionally allowed<br>to perform the Secure Simple<br>Pairing procedure before<br>rejecting the Upper Tester’s<br>request.<br>Request rejected<br>**----- End of picture text -----**<br>


_Figure 4.44: GAP/SEC/SEM/BV-17-C [Secure Connections Only mode – IUT Central, initiator, Lower Tester doesn’t support Secure Connections in Host] MSC_ 

   1. The Upper Tester puts the IUT in Secure Connections Only mode. 

   2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT. 

   3. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT rejects the Upper Tester’s request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT. 

- Notes 

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4. 

- **4.5.3.6 Secure Connections Only mode BR/EDR transport – IUT Central, initiator, Lower Tester supports Secure Connections in Controller and Host** 

- Test Purpose 

The Lower Tester supports Secure Connections both at the Controller and Host level. Verify that the IUT in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **81 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX_psm_sm4l3 IXIT value. 

   - Set both the Secure Connections (Controller Support) and the Secure Connections (Host Support) LMP feature bits on the Lower Tester to 1. 

   - The IUT and the Lower Tester are bonded as specified in Table 4.15. 

   - An ACL connection does not exist between the devices. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-18-C|Not Bonded, No Link Keys|Secure Simple Pairing|
|GAP/SEC/SEM/BV-54-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.15: Secure Connections Only mode BR/EDR transport – IUT Central, initiator, Lower Tester supports Secure Connections in Controller and Host test cases_ 

- Test Procedure 

**==> picture [377 x 348] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Secure Connections Only Mode<br>Initiate action to trigger an L2CAP connection with the<br>Lower Tester<br>Establish ACL connection<br>NO LINK KEY<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing Complete (Authenticated link key)<br>LINK KEY<br>Generic Authentication Procedure<br>Encryption LMP messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result=Connection<br>successful, status)<br>**----- End of picture text -----**<br>


_Figure 4.45: Secure Connections Only mode BR/EDR transport – IUT Central, initiator, Lower Tester supports Secure Connections in Controller and Host MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **82 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Upper Tester puts the IUT in Secure Connections Only mode. 

   2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT. 

   3. The IUT creates an ACL connection with the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT accepts the Upper Tester’s request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT and the channel establishment procedure is successful. 

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester. 

- Notes 

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4. 

- **4.5.3.7 IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host** 

- Test Purpose 

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX_psm_sm4l3 IXIT value. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - The IUT and the Lower Tester are bonded as specified in Table 4.16. 

   - An ACL connection does not exist between the devices. 

- Test Case Configuration 

|**Test Case**|**Link Keys**|**Pairing/Authentication**|
|---|---|---|
|GAP/SEC/SEM/BV-19-C|Not Bonded, No Link Keys|Secure Simple Pairing|
|GAP/SEC/SEM/BV-55-C|Bonded, Has Link Keys|Generic authenticationprocedure|



_Table 4.16: IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **83 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [377 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Security Mode 4 (but not in<br>Secure Connections Only Mode)<br>Initiate action to trigger an L2CAP connection with the Lower<br>Tester<br>Establish ACL connection<br>NO LINK KEY<br>Secure Simple Pairing Procedures<br>Secure Simple Pairing Complete (Authenticated link key)<br>LINK KEY<br>Generic Authentication Procedure<br>Encryption LMP messages<br>L2CAP_ConnectReq<br>(ID, length, PSM, SCID)<br>L2CAP_ConnectRsp<br>(ID, length, DCID, SCID, result=Connection<br>successful, status)<br>**----- End of picture text -----**<br>


_Figure 4.46: IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host MSC_ 

   1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode). 

   2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT. 

   3. The IUT creates an ACL connection with the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT accepts the Upper Tester’s request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT and the channel establishment procedure is successful. 

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **84 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/SEM/BV-20-C [IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service]** 

- Test Purpose 

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode rejects a request to perform a channel establishment procedure over the BR/EDR transport if the service requires security mode 4 level 4 on the IUT. The IUT is Central and initiator of the channel establishment procedure. 

- Reference 

   - [1] 5.2.2 

- Initial Condition 

   - The PSM for the service that requires security mode 4 level 4 is specified in the TSPX_psm_sm4l4 IXIT value. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys). 

   - An ACL connection does not exist between the devices. 

- Test Procedure 

**==> picture [378 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are not bonded (neither IUT nor Lower Tester has link keys).<br>ACL connection does not exist between the devices.<br>Bring IUT in Security Mode 4 (but not in<br>Secure Connections Only Mode)<br>Initiate action to trigger an L2CAP connection with the Lower<br>Tester<br>Establish ACL connection<br>Request rejected<br>**----- End of picture text -----**<br>


_Figure 4.47: GAP/SEC/SEM/BV-20-C [IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service] MSC_ 

1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode). 

2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 4 on the IUT. 

3. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **85 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The IUT rejects the Upper Tester’s request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 4 on the IUT. 

## **4.5.4 LE security modes – Central** 

Verify the correct behavior in LE security modes. The role of the IUT is Central. 

- **4.5.4.1 LE Secure Connections, Central – outgoing service level connection** 

- Test Purpose 

Verify that the IUT, supporting LE Secure Connections, after performing the authentication procedure will achieve an outgoing service level connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Central. 

- Reference 

   - [10] 2.3.5.6 

- Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The IUT will initiate a GATT service request when TSPX_Use_GATT is set to TRUE. Otherwise, the IUT will establish an L2CAP channel. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|
|---|---|
|GAP/SEC/SEM/BV-26-C [LE security mode: mode 1 level 4,<br>Central – outgoingservice level connection]|LE security mode 1 level 4|
|GAP/SEC/SEM/BV-41-C [LE Secure Connections Only: mode 1<br>level 2, Central – outgoingservice level connection]|LE security mode 1 level 2|
|GAP/SEC/SEM/BV-42-C [LE Secure Connections Only: mode 1<br>level 3, Central – outgoingservice level connection]|LE security mode 1 level 3|



_Table 4.17: LE Secure Connections, Central – outgoing service level connection test cases_ 

- Test Procedure 

   1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.17. 

   2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester. 

   3. The Upper Tester triggers authentication procedure on the IUT, e.g., by an L2CAP channel establishment or a GATT service request. 

   4. The IUT begins LE Secure Connections Phase 1 by sending an SMP Pairing Request, with the Secure Connections bit set to 1. The Lower Tester answers with SMP Pairing Response, with the Secure Connections bit set to 1. 

   5. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   6. The Lower Tester replies with a successful response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **86 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [273 x 437] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT finds Lower Tester<br>Establishes LE connection<br>ALT A GATT service request<br>ALT B L2CAP channel<br>establishment<br>Authenticate<br>LE Secure SMP Pairing Req.<br>AuthReq.SC=1<br>Connections<br>Phase 1 SMP Pairing Resp.<br>AuthReq.SC=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption<br>LE Secure Connections Phase 3:<br>Key distribution<br>ALT A<br>GATT service request<br>ALT B<br>L2CAP channel<br>establishment<br>ALT A GATT service request  GATT service request<br>success success<br>ALT B L2CAP channel  L2CAP channel<br>establishment success<br>establishment success<br>Authenticated<br>**----- End of picture text -----**<br>


_Figure 4.48: LE Secure Connections, Central – outgoing service level connection MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted on the security mode and level specified in Table 4.17. 

The initiated procedure is successful. 

- Notes 

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.17. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **87 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.5.4.2 LE Secure Connections, Central – incoming service level connection** 

- Test Purpose 

Verify that the IUT, supporting LE Secure Connections, after performing the authentication procedure will achieve an incoming service level connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Central. 

- Reference 

   - [10] 2.3.5.6 

- Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The Lower Tester will establish a GATT service request when TSPX_Use_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|
|---|---|
|GAP/SEC/SEM/BV-27-C [LE security mode: mode 1 level 4,<br>Central – incomingservice level connection]|LE security mode 1 level 4|
|GAP/SEC/SEM/BV-43-C [LE Secure Connections Only: mode 1<br>level 2, Central – incomingservice level connection]|LE security mode 1 level 2|
|GAP/SEC/SEM/BV-44-C [LE Secure Connections Only: mode 1<br>level 3, Central – incomingservice level connection]|LE security mode 1 level 3|



_Table 4.18: LE Secure Connections, Central – incoming service level connection test cases_ 

- Test Procedure 

   1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.18. 

   2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester. 

   3. The Lower Tester initiates LE Secure Connections pairing according to the security mode and level specified in Table 4.18. 

   4. The Lower Tester and the IUT complete SMP Phase 1, Phase 2 (pairing), and Phase 3 (encryption and key distribution). 

   5. The Lower Tester initiates either an L2CAP channel establishment or GATT service request to the IUT. 

   6. The IUT replies with the correct channel establishment response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **88 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [391 x 450] intentionally omitted <==**

_Figure 4.49: LE Secure Connections, Central – incoming service level connection MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted on the security mode and level specified in Table 4.18. 

The initiated procedure is successful. 

- 

- Notes 

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.18. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **89 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/SEM/BV-28-C [Secure Connections Only mode LE transport – failed procedure, Central – outgoing service level connection]** 

- Test Purpose 

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only initiating the authentication procedure will result in a failed procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Central. 

- Reference 

   - [9] 10.2.4 

- 

   - Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

- 

## Test Procedure 

1. The Upper Tester configures the IUT into Secure Connections Only mode or to only support LE Secure Connections. 

2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester. 

3. The Upper Tester triggers authentication procedure on the IUT, e.g., by an L2CAP channel establishment or a GATT service request. 

4. The IUT begins LE Secure Connections Phase 1 by sending an SMP Pairing Request, with the Secure Connections bit set to 1. 

5. The Lower Tester responds with an SMP Pairing Response with the Secure Connections bit set to 0. 

6. Alternative 1: (for security mode 1 level 4 connections): 

   - a. The IUT responds with an SMP Pairing Failed message. 

7. Alternative 2: (for security mode 1 level 2 or 3 with Secure Connections): 

   - a. The IUT and the Lower Tester complete the LE Legacy Pairing procedure. 

   - b. The Lower Tester continues the authentication procedure started in Step 3. 

   - c. The IUT responds with a failure message. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **90 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [145 x 51] intentionally omitted <==**

**==> picture [290 x 161] intentionally omitted <==**

_Figure 4.50: GAP/SEC/SEM/BV-28-C [Secure Connections Only mode LE transport – failed procedure, Central – outgoing service level connection] MSC_ 

- Expected Outcome 

## Pass verdict 

In ALT 1, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1. 

In ALT 2, the IUT does not complete the L2CAP Channel establishment or GATT service request. 

**GAP/SEC/SEM/BV-29-C [Secure Connections Only mode LE transport – failed procedure, Central – incoming service level connection]** 

- Test Purpose 

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only rejects an L2CAP channel establishment or GATT service request procedure both before and after the authentication procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Central. 

- Reference 

[9] 10.2.4 

- Initial Condition 

   - The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The Lower Tester is configured so that it does not support LE Secure Connections. 

   - The Lower Tester will establish a GATT service request when TSPX_Use_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **91 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester configures the IUT into Secure Connections Only mode or to only support LE Secure Connections. 

   2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester. 

   3. The Lower Tester initiates either an L2CAP channel establishment or GATT service request to the IUT. 

   4. The IUT rejects the request. 

   5. The Lower Tester initiates authenticated LE Legacy pairing. 

   6. Alternative 1: the IUT rejects the pairing by sending an SMP Pairing Failed message. 

   7. Alternative 2: the Lower Tester and the IUT complete LE legacy pairing. The Lower Tester reinitiates the request to the IUT as attempted in Step 3. The IUT rejects the request. 

**==> picture [267 x 446] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT finds Lower Tester<br>Establishes LE connection<br>ALT A GATT service request<br>ALT B L2CAP channel<br>establishment<br>Error<br>SMP Security Req.<br>AuthReq.SC=0<br>ALT 1<br>SMP Pairing Failed<br>Auth. Requirements<br>ALT 2<br>LE Legacy Pairing<br>Channel establishment<br>ALT A GATT service request<br>ALT B L2CAP channel<br>establishment<br>Error<br>**----- End of picture text -----**<br>


_Figure 4.51: GAP/SEC/SEM/BV-29-C [Secure Connections Only mode – failed procedure, Central – incoming service level connection] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **92 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The L2CAP channel establishment or GATT service request is rejected before the authentication procedure. 

Alternative 1: IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1. 

Alternative 2: The IUT and the Lower Tester complete LE legacy pairing and the IUT rejects the request from the Lower Tester. 

**GAP/SEC/SEM/BV-30-C [Secure Connections Only mode, Central, failure, BR/EDR and LE transports]** 

- Test Purpose 

Verify that the IUT in Secure Connections Only mode performs either an L2CAP channel establishment or GATT service procedure over LE and a channel establishment procedure over BR/EDR. The IUT is initiator of the procedure over both LE and BR/EDR. The Lower Tester supports neither LE Secure Connections nor BR/EDR Secure Connections. The procedure fails over both LE and BR/EDR. The IUT is the Central. 

- Reference 

   - [9] 10.2.4 

- 

- Initial Condition 

- The IUT supports both LE Secure Connections and BR/EDR Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

   - The Lower Tester is configured so that it does not support LE Secure Connections and BR/EDR Secure Connections. 

   - The PSM for the service on the IUT that requires security mode 4 level 3 on BR/EDR is specified in the TSPX_psm_sm4l3 IXIT value. 

   - The IUT and the Lower Tester are not bonded on BR/EDR (neither the IUT nor the Lower Tester has link keys). 

   - A BR/EDR ACL connection does not exist between the devices. 

- Test Procedure 

   1. The Upper Tester configures the IUT into Secure Connections Only mode. 

   2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester. 

   3. The IUT begins LE Secure Connections Phase 1 by sending an SMP Pairing Request, with the Secure Connections bit set to 1. The Lower Tester responds with an SMP Pairing Response with the Secure Connections bit set to 0. The IUT will respond with an SMP Pairing Failed message. 

   4. The IUT terminates the LE connection. 

   5. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT. 

   6. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **93 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [301 x 474] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>IUT finds Lower Tester<br>Establishes LE connection<br>ALT GATT service request<br>L2CAP channel<br>establishment<br>SMP Pairing Req.<br>LE Secure<br>AuthReq.SC=1<br>Connections<br>Phase 1 SMP Pairing Resp.<br>AuthReq.SC=0<br>SMP Pairing Failed<br>Auth. Requirements<br>ALT GATT service request<br>failure<br>L2CAP channel<br>establishment failure<br>Initiate action<br>to trigger an<br>Terminate LE connection<br>L2CAP<br>connection<br>with the<br>BR/EDR L2CAP channel<br>Upper Tester<br>establishment<br>Establish ACL connection The IUT is allowed to reject the Upper<br>Tester’s request at either of the<br>following steps:<br>1. When the IUT reads the Lower<br>Tester’s LMP features and sees that it<br>does not support BR/EDR Secure<br>Connections.<br>2. At the end of the Secure Simple<br>Pairing Procedure when the IUT sees<br>that the Link Key is not strong enough.<br>Request rejected<br>**----- End of picture text -----**<br>


_Figure 4.52: GAP/SEC/SEM/BV-30-C [Secure Connections Only mode, Central, Failure, BR/EDR and LE Transports] MSC_ 

- Expected Outcome 

## Pass verdict 

On the LE transport, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1. 

On the BR/EDR transport, the IUT rejects the Upper Tester’s request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **94 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.4.3 LE security mode 1, Central – Invalid Encryption Key Size** 

- Test Purpose 

Verify that the IUT in LE security mode 1 as Central fails pairing when receiving an invalid key size. 

- Reference 

[9] 10.3.2, 10.2.1 

- Initial Condition 

   - The IUT is in Link Layer Standby state. 

- Test Case Configuration 

|**TCID**|**LE Security Mode and Level**|
|---|---|
|GAP/SEC/SEM/BI-10-C [LE security mode 1 level 4,<br>Central – Invalid Encryption KeySize]|LE security mode 1 level 4|
|GAP/SEC/SEM/BI-22-C [LE security mode 1 level 3,<br>Central – Invalid Encryption KeySize]|LE security mode 1 level 3 with LE<br>Secure Connections Pairingonly|
|GAP/SEC/SEM/BI-23-C [LE security mode 1 level 2,<br>Central – Invalid Encryption KeySize]|LE security mode 1 level 2 with LE<br>Secure Connections Pairingonly|



_Table 4.19: LE security mode 1, Central – Invalid Encryption Key Size test cases_ 

- Test Procedure 

**==> picture [271 x 249] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(Peripheral) (Central)<br>Repeat for each KS in the range [7,15]<br>IUT is configured in Security Mode-1 Level 4<br>Lower Tester has established an LE connection with the IUT<br>Initiate pairing<br>SMP Pairing Request<br>AuthReq: SC=1<br>Maximum Encryption Key<br>Size=16<br>SMP Pairing Response<br>(AuthReq: SC=1<br>Maximum Encryption<br>Key Size=KS)<br>SMP Pairing Failed<br>Pairing failed due to<br>Reason=Encryption Key<br>insufficient key size<br>Size (0x06)<br>Terminate LE connection<br>**----- End of picture text -----**<br>


_Figure 4.53: LE security mode 1, Central – Invalid Encryption Key Size MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **95 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

Repeat Steps 1–6 for all values of the Maximum Encryption Key Size field (in Step 4) in the interval [7, 15]. 

   1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.19. 

   2. The Upper Tester configures the IUT to connect to the Lower Tester. 

   3. The Upper Tester orders the IUT to initiate pairing, and the IUT sends to the Lower Tester an SMP Pairing Request with the Secure Connections bit set to 1 and Maximum Encryption Key Size set to 16. 

   4. The Lower Tester responds with an SMP Pairing Response, with the Secure Connections bit set to 1 and Maximum Encryption Key Size set to the value selected for this iteration. 

   5. The IUT sends to the Lower Tester an SMP Pairing Failed with the Reason set to “Encryption Key Size” (0x06) and to report the procedure failure to the Upper Tester. 

   6. The Lower Tester terminates the LE connection. 

- Expected Outcome 

## Pass verdict 

The IUT fails pairing for any key size value less than 16 while in the specified security mode and level. 

## **4.5.5 LE security modes – Both connected roles** 

## **4.5.5.1 Incoming GATT indication, LE security mode 1 level 2** 

- Test Purpose 

Verify that the IUT properly handles a GATT indication before security requirements are performed in LE security mode 1 level 2. 

- Reference 

   - [17] 10.3.2.2 

- Initial Condition 

   - The IUT is in the Standby state. 

   - The IUT is the GATT Client in the role specified in Table 4.20. 

   - The Lower Tester is configured so that it sends GATT indications. 

- Test Case Configuration 

|**TCID**|**IUT Role**|
|---|---|
|GAP/SEC/SEM/BV-56-C [Incoming GATT indication, LE security mode 1<br>level 2, Peripheral]|Peripheral|
|GAP/SEC/SEM/BV-62-C [Incoming GATT indication, LE security mode 1<br>level 2, Central]|Central|



_Table 4.20: Incoming GATT indication, LE security mode 1 level 2 test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **96 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [398 x 447] intentionally omitted <==**

_Figure 4.54: Incoming GATT indication, LE security mode 1 level 2 MSC – Page 1 of 2_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **97 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [399 x 425] intentionally omitted <==**

_Figure 4.55: Incoming GATT indication, LE security mode 1 level 2 MSC – Page 2 of 2_ 

1. The Upper Tester puts the IUT into LE security mode 1 level 2. 

2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.20. 

3. Perform alternative 3A or 3B depending on the IUT role in Table 4.20. Alternative 3A (IUT is Peripheral): 

   - 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding_Flags bit set to 1 and the MITM and SC bits set to 0 or 1. 

   - 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding_Flags bit set to 1 and the MITM set to 0 and SC bit set to 1. 

   - 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **98 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

Alternative 3B (IUT is Central): 

      - 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding_Flags bit set to 1 and the MITM and SC bits set to 0 or 1. 

      - 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding_Flags set to 1 and MITM set to 0 and SC bit set to 1. 

   4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   5. The Upper Tester commands the IUT to enable GATT indications with the Lower Tester. 

   6. The IUT sends an ATT_WRITE_REQUEST to the Lower Tester with CCCD set to 0x0002. 

   7. The Lower Tester sends an ATT_WRITE_RESPONSE to the IUT. 

   8. The IUT and the Lower Tester disconnect. 

   9. Perform either alternative 9A, 9B, or 9C depending on if the IUT starts an encryption request. Alternative 9A (The IUT does not start an encryption request): 

      - 9A.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.20. 

      - 9A.2 The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

      - 9A.3 The IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

      - 9A.4 The IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

      - 9A.5 The Lower Tester initiates and completes the encryption procedure with the IUT. 

      - Alternative 9B (The IUT starts an encryption request): 

      - 9B.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.20. 

      - 9B.2 The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

      - Steps 9B.3–9B.5 may occur in any order. 

      - 9B.3 The IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

      - 9B.4 The IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

      - 9B.5 The IUT initiates and completes the encryption procedure with the Lower Tester. 

   10. The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   11. The IUT sends an ATT_HANDLE_VALUE_CFM to the Lower Tester. 

   12. The IUT sends a GATT_HandleValueIndication to the Upper Tester. 

- Expected Outcome 

## Pass verdict 

In Step 9A.3 or 9B.3, the IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

In Step 9A.4 or 9B.4, the IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

In Step 12, the IUT sends a GATT_HandleValueIndication to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **99 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.5.2 Incoming GATT indication, LE security mode 1 level 3** 

- Test Purpose 

Verify that the IUT properly handles a GATT indication before security requirements are performed in LE security mode 1 level 3. 

- Reference 

   - [17] 10.3.2.2 

- Initial Condition 

   - The IUT is in the Standby state. 

   - The IUT is the GATT Client in the role specified in Table 4.21. 

   - The Lower Tester is configured so that it sends GATT indications. 

- Test Case Configuration 

|**TCID**|**IUT Role**|
|---|---|
|GAP/SEC/SEM/BV-57-C [Incoming GATT indication, LE security mode 1<br>level 3, Peripheral]|Peripheral|
|GAP/SEC/SEM/BV-63-C [Incoming GATT indication, LE security mode 1<br>level 3, Central]|Central|



_Table 4.21: Incoming GATT indication, LE security mode 1 level 3 test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **100 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [399 x 447] intentionally omitted <==**

_Figure 4.56: Incoming GATT indication, LE security mode 1 level 3 MSC – Page 1 of 2_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **101 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [398 x 424] intentionally omitted <==**

_Figure 4.57: Incoming GATT indication, LE security mode 1 level 3 MSC – Page 2 of 2_ 

1. The Upper Tester puts the IUT into LE security mode 1 level 3. 

2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.21. 

3. Perform alternative 3A or 3B depending on the IUT role in Table 4.21. 

   - Alternative 3A (IUT is Peripheral): 

   - 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 0 or 1. 

   - 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 1. 

   - 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 0 or 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **102 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

Alternative 3B (IUT is Central): 

      - 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 0 or 1. 

      - 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 1. 

   4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   5. The Upper Tester commands the IUT to enable GATT indications with the Lower Tester. 

   6. The IUT sends an ATT_WRITE_REQUEST to the Lower Tester with CCCD set to 0x0002. 

   7. The Lower Tester sends an ATT_WRITE_RESPONSE to the IUT. 

   8. The IUT and the Lower Tester disconnect. 

   9. Perform either alternative 9A, 9B, or 9C depending on if the IUT starts an encryption request. Alternative 9A (The IUT does not start an encryption request): 

      - 9A.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.21. 

      - 9A.2 The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

      - 9A.3 The IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

      - 9A.4 The IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

      - 9A.5 The Lower Tester initiates and completes the encryption procedure with the IUT. 

      - Alternative 9B (The IUT starts an encryption request): 

      - 9B.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.21. 

      - 9B.2 The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

      - Steps 9B.3–9B.5 may occur in any order. 

      - 9B.3 The IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

      - 9B.4 The IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

      - 9B.5 The IUT initiates and completes the encryption procedure with the Lower Tester. 

   10. The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   11. The IUT sends an ATT_HANDLE_VALUE_CFM to the Lower Tester. 

   12. The IUT sends a GATT_HandleValueIndication to the Upper Tester. 

- Expected Outcome 

## Pass verdict 

In Step 9A.3 or 9B.3, the IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

In Step 9A.4 or 9B.4, the IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

In Step 12, the IUT sends a GATT_HandleValueIndication to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **103 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.5.3 LE Secure Connections Only, Incoming GATT Indication** 

- Test Purpose 

Verify that the IUT that supports LE Secure Connections only properly handles a GATT indication before security requirements are performed. 

- Reference 

   - [17] 10.3.2.2 

- Initial Condition 

   - The IUT is in the Standby state. 

   - The IUT supports LE Secure Connections. The IUT is the GATT Client in the role specified in Table 4.22. The Lower Tester supports LE Secure Connections. 

   - The IUT is configured to receive GATT indications from the Lower Tester. 

- Test Case Configuration 

|**TCID**|**IUT Role**|
|---|---|
|GAP/SEC/SEM/BV-58-C [LE Secure Connections Only – Incoming GATT<br>indication, Peripheral]|Peripheral|
|GAP/SEC/SEM/BV-64-C [LE Secure Connections Only – Incoming GATT<br>indication, Central]|Central|



_Table 4.22: LE Secure Connections Only, Incoming GATT Indication test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **104 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [400 x 448] intentionally omitted <==**

_Figure 4.58: LE Secure Connections Only, Incoming GATT Indication MSC – Page 1 of 2_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **105 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [399 x 425] intentionally omitted <==**

_Figure 4.59: LE Secure Connections Only, Incoming GATT Indication MSC – Page 2 of 2_ 

1. The Upper Tester puts the IUT into the Secure Connections Only mode. 

2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.22. 

3. Perform alternative 3A or 3B depending on the IUT role in Table 4.22. Alternative 3A (IUT is Peripheral): 

   - 3A.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Security Request, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

   - 3A.2 The Lower Tester responds by sending an SMP Pairing Request, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

   - 3A.3 The IUT replies with an SMP Pairing Response, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **106 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

Alternative 3B (IUT is Central): 

      - 3B.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Pairing Request, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

      - 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

   4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   5. The Upper Tester commands the IUT to enable GATT indications with the Lower Tester. 

   6. The IUT sends an ATT_WRITE_REQUEST to the Lower Tester with CCCD set to 0x0002. 

   7. The Lower Tester sends an ATT_WRITE_RESPONSE to the IUT. 

   8. The IUT and the Lower Tester disconnect. 

   9. Perform either alternative 9A, 9B, or 9C depending on if the IUT starts an encryption request. Alternative 9A (The IUT does not start an encryption request): 

      - 9A.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.22. 

      - 9A.2 The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

      - 9A.3 The IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

      - 9A.4 The IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

      - 9A.5 The Lower Tester initiates and completes the encryption procedure with the IUT. 

      - Alternative 9B (The IUT starts an encryption request): 

      - 9B.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.22. 

      - 9B.2 The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

      - Steps 9B.3–9B.5 may occur in any order. 

      - 9B.3 The IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

      - 9B.4 The IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

      - 9B.5 The IUT initiates and completes the encryption procedure with the Lower Tester. 

   10. The Lower Tester sends an ATT_HANDLE_VALUE_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   11. The IUT sends an ATT_HANDLE_VALUE_CFM to the Lower Tester. 

   12. The IUT sends a GATT_HandleValueIndication to the Upper Tester. 

- Expected Outcome 

## Pass verdict 

In Step 9A.3 or 9B.3, the IUT sends an ATT_HANDLE_VALUE_CFM PDU to the Lower Tester. 

In Step 9A.4 or 9B.4, the IUT does not send a GATT_HandleValueIndication to the Upper Tester. 

In Step 12, the IUT sends a GATT_HandleValueIndication to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **107 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.5.4 Incoming GATT notification, LE security mode 1 level 2** 

- Test Purpose 

Verify that the IUT properly handles a GATT notification before security requirements are performed for LE security mode 1 level 2. 

- Reference 

   - [17] 10.3.2.2 

- Initial Condition 

   - The IUT is in the Standby state. 

   - The IUT is the GATT Client in the role specified in Table 4.23. 

   - The Lower Tester is configured so that it sends GATT notifications. 

- Test Case Configuration 

|**TCID**|**Role**|
|---|---|
|GAP/SEC/SEM/BV-59-C [Incoming GATT notification, LE security mode 1<br>level 2, Peripheral]|Peripheral|
|GAP/SEC/SEM/BV-65-C [Incoming GATT notification, LE security mode 1<br>level 2, Central]|Central|



_Table 4.23: Incoming GATT notification, LE security mode 1 level 2 test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **108 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [434 x 590] intentionally omitted <==**

_Figure 4.60: Incoming GATT notification, LE security mode 1 level 2 MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **109 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Upper Tester puts the IUT into LE security mode 1 level 2. 

   2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.23. 

   3. Perform alternative 3A or 3B depending on the IUT role in Table 4.23. Alternative 3A (IUT is Peripheral): 

      - 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding_Flags bit set to 1 and the MITM and SC bits set to 0 or 1. 

      - 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding_Flags bit set to 1 and the MITM set to 0 and SC bit set to 1. 

      - 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1. 

      - Alternative 3B (IUT is Central): 

      - 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1. 

      - 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1. 

   4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   5. The Upper Tester commands the IUT to enable GATT notifications with the Lower Tester. 

   6. The IUT sends an ATT_WRITE_REQUEST to the Lower Tester with CCCD set to 0x0001. 

   7. The Lower Tester sends an ATT_WRITE_RESPONSE to the IUT. 

   8. The IUT and the Lower Tester disconnect. 

   9. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.23. 

   10. The Lower Tester sends an ATT_HANDLE_VALUE_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   11. The IUT does not send a GATT_HandleValueNotification to the Upper Tester. 

   12. Perform alternative 12A or 12B depending on the IUT role in Table 4.23. Alternative 12A (IUT is Peripheral): 

      - 12A.1 The Lower Tester initiates and completes the encryption procedure with the IUT. 

      - Alternative 12B (IUT is Central): 

      - 12B.1 The IUT initiates and completes the encryption procedure with the Lower Tester. 

   13. The Lower Tester sends an ATT_HANDLE_VALUE_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   14. The IUT sends a GATT_HandleValueNotification to the Upper Tester with a valid Characteristic Handle value. 

- Expected Outcome 

## Pass verdict 

In Step 11, the IUT does not send a GATT_HandleValueNotification to the Upper Tester. 

In Step 14, the IUT sends a GATT_HandleValueNotification to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **110 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.5.5 Incoming GATT notification, LE security mode 1 level 3** 

- Test Purpose 

Verify that the IUT properly handles a GATT notification before security requirements are performed for LE security mode 1 level 3. 

- Reference 

   - [17] 10.3.2.2 

- Initial Condition 

   - The IUT is in the Standby state. 

   - The IUT is the GATT Client in the role specified in Table 4.24. 

   - The Lower Tester is configured so that it sends GATT notifications. 

- Test Case Configuration 

|**TCID**|**Role**|
|---|---|
|GAP/SEC/SEM/BV-60-C [Incoming GATT notification, LE security mode 1 level 3,<br>Peripheral]|Peripheral|
|GAP/SEC/SEM/BV-66-C [Incoming GATT notification, LE security mode 1 level 3,<br>Central]|Central|



_Table 4.24: Incoming GATT notification, LE security mode 1 level 3 test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **111 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [408 x 583] intentionally omitted <==**

_Figure 4.61: Incoming GATT notification, LE security mode 1 level 3 MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **112 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

1. The Upper Tester puts the IUT into LE security mode 1 level 3. 

2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.24. 

3. Perform alternative 3A or 3B depending on the IUT role in Table 4.24. Alternative 3A (IUT is Peripheral): 

   - 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 0. 

   - 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding_Flags and MITM bits set to 1and the SC bit set to 0. 

   - 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding_Flags and MITM bits set to 1and the SC bit set to 0. 

Alternative 3B (IUT is Central): 

      - 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 0. 

      - 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding_Flags and MITM bits set to 1 and the SC bit set to 0. 

   4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   5. The Upper Tester commands the IUT to enable GATT notifications with the Lower Tester. 

   6. The IUT sends an ATT_WRITE_REQUEST to the Lower Tester with CCCD set to 0x0001. 

   7. The Lower Tester sends an ATT_WRITE_RESPONSE to the IUT. 

   8. The IUT and the Lower Tester disconnect. 

   9. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.24. 

   10. The Lower Tester sends an ATT_HANDLE_VALUE_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   11. The IUT does not send a GATT_HandleValueNotification to the Upper Tester. 

   12. Perform alternative 12A or 12B depending on the IUT role in Table 4.24. Alternative 12A (IUT is Peripheral): 

      - 12A.1 The Lower Tester initiates and completes the encryption procedure with the IUT. 

      - Alternative 12B (IUT is Central): 

      - 12B.1 The IUT initiates and completes the encryption procedure with the Lower Tester. 

   13. The Lower Tester sends an ATT_HANDLE_VALUE_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   14. The IUT sends a GATT_HandleValueNotification to the Upper Tester with a valid Characteristic Handle value. 

- Expected Outcome 

## Pass verdict 

In Step 11, the IUT does not send a GATT_HandleValueNotification to the Upper Tester. 

In Step 14, the IUT sends a GATT_HandleValueNotification to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **113 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.5.6 LE Secure Connections Only, Incoming GATT Notification** 

- Test Purpose 

Verify that the IUT that supports LE Secure Connections only properly handles a GATT notification before security requirements are performed. 

- Reference 

   - [17] 10.3.2.2 

- Initial Condition 

   - The IUT is in the Standby state. 

   - The IUT supports LE Secure Connections. The IUT is the GATT Client in the role specified in Table 4.25. The Lower Tester supports LE Secure Connections. 

   - The IUT is configured to receive GATT notifications from the Lower Tester. 

- Test Case Configuration 

|**TCID**|**Role**|
|---|---|
|GAP/SEC/SEM/BV-61-C [LE Secure Connections Only, Incoming GATT<br>notification, Peripheral]|Peripheral|
|GAP/SEC/SEM/BV-67-C [LE Secure Connections Only, Incoming GATT<br>notification, Central]|Central|



_Table 4.25: Incoming GATT notification, LE security mode 1 level 3 test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **114 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [410 x 577] intentionally omitted <==**

_Figure 4.62: LE Secure Connections Only, Incoming GATT Notification MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **115 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Upper Tester puts the IUT into the Secure Connections Only mode. 

   2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.25. 

   3. Perform alternative 3A or 3B depending on the IUT role in Table 4.25. Alternative 3A (IUT is Peripheral): 

      - 3A.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Security Request, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

      - 3A.2 The Lower Tester responds by sending an SMP Pairing Request, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

      - 3A.3 The IUT replies with an SMP Pairing Response, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

      - Alternative 3B (IUT is Central): 

      - 3B.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Pairing Request, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

      - 3B.2 The Lower Tester replies with SMP Pairing Response, with the Secure Connections, Bonding_Flags, and MITM bits set to 1. 

   4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

   5. The Upper Tester commands the IUT to enable GATT notifications with the Lower Tester. 

   6. The IUT sends an ATT_WRITE_REQUEST to the Lower Tester with CCCD set to 0x0001. 

   7. The Lower Tester sends an ATT_WRITE_RESPONSE to the IUT. 

   8. The IUT and the Lower Tester disconnect. 

   9. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.25. 

   10. The Lower Tester sends a GATT_HANDLE_VALUE_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   11. The IUT does not send a GATT_HandleValueNotification to the Upper Tester. 

   12. Perform alternative 12A or 12B depending on the IUT role in Table 4.25. Alternative 12A (IUT is Peripheral): 

      - 12A.1 The Lower Tester initiates and completes the encryption procedure with the IUT. 

      - Alternative 12B (IUT is Central): 

      - 12B.1 The IUT initiates and completes the encryption procedure with the Lower Tester. 

   13. The Lower Tester sends an ATT_HANDLE_VALUE_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value. 

   14. The IUT sends a GATT_HandleValueNotification to the Upper Tester. 

- Expected Outcome 

## Pass verdict 

In Step 11, the IUT does not send a GATT_HandleValueNotification to the Upper Tester. 

In Step 14, the IUT sends a GATT_HandleValueNotification to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **116 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.6 Security modes – Observer role** 

Verify the correct behavior in this mode. The role of the IUT is the Observer and Acceptor. 

## **4.5.6.1 LE security mode 3 – Observer role, Acceptor** 

- Test Purpose 

Verify that the IUT in the LE security mode 3 with level as specified in Table 4.26 receives BIS data. 

- Reference 

[15] 9.2.5, 1.2.2.1, 1.2.2.2 

- Initial Condition 

   - The IUT is in Synchronization State. 

   - The Lower Tester is in Isochronous Broadcasting State. 

   - The Broadcast_Code has been obtained by the IUT’s Host using an unauthenticated or authenticated method as defined by the IUT’s application. The Lower Tester may obtain the Broadcast_Code by any means, including reading the TSPX_broadcast_code IXIT parameter, and for test purposes may be considered either authenticated or unauthenticated. 

- Test Case Configuration 

|**Test Case ID**|**Security**<br>**Level**|**Encryption**|**Initial Condition Encryption**<br>**Information**|
|---|---|---|---|
|GAP/SEC/SEM/BV-31-C|1|Disabled(0x00)|None|
|GAP/SEC/SEM/BV-32-C|2 or 3|Enabled(0x01)|The Broadcast_Code has been<br>obtained bythe IUT’s Host.|



_Table 4.26: LE security mode 3 – Observer role, Acceptor test cases_ 

- Test Procedure 

**==> picture [301 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Execute GAP/BIS/BSE/BV-01-C to set up a BIS<br>Repeat<br>BIS Data<br>(Encryption)<br>BIS Data<br>(Encryption)<br>**----- End of picture text -----**<br>


_Figure 4.63: LE security mode 3 – Observer role, Acceptor MSC_ 

1. Perform test case GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment procedure]. When enabling the BIG, set the Encryption parameter as specified in Table 4.26. 

2. The Lower Tester sends BIS data to the IUT with the Encryption specified in Table 4.26. 

3. The IUT receives the BIS data and reports the data to the Upper Tester. The Lower Tester and the IUT operate on the same security mode and level. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **117 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

In Step 3, the IUT receives the BIS data and reports the data to the Upper Tester. The Lower Tester and the IUT operate on the same security mode and level. 

**GAP/SEC/SEM/BI-13-C [LE security mode 3 – Observer, Reject Lower Level Security]** 

- Test Purpose 

Verify that the IUT in the LE security mode 3 rejects BIS events with lower level security. 

- Reference 

[15] 9.2.5, 1.2.2.1, 1.2.2.2 

- Initial Condition 

   - The IUT is in Synchronization State. 

   - The Lower Tester is in Isochronous Broadcasting State. 

   - The Broadcast_Code has been obtained by the IUT’s Host using a method as defined by the IUT’s application. The Lower Tester may obtain the Broadcodeast_Code by any means, including reading the TSPX_broadcast_code IXIT parameter, and for test purposes may be considered either authenticated or unauthenticated. 

- Test Procedure 

   1. Attempt to perform test case GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment procedure]. When creating the BIG, the Lower Tester disables encryption. The security level of the IUT is set to level 2 or 3. 

   2. The IUT is unable to synchronize to the BIG. 

- Expected Outcome 

## Pass verdict 

In Step 2, the IUT is unable to synchronize to the BIG. 

**GAP/SEC/SEM/BV-45-C [Re-pair or stop a connection attempt when a connection fails due to failed encryption, LE security mode 1 level 4]** 

- Test Purpose 

Verify that the IUT in LE security mode 1 level 4 properly handles when a connection attempt with a bonded peer fails during the encryption phase. The IUT can either stop the connection attempt or notify the Upper Tester for User Interaction to pair with the peer. The IUT is the Central. The Lower Tester supports LE Secure Connections. 

- Reference 

   - [9] 10.3 

- Initial Condition 

   - The IUT is bonded with the Lower Tester. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **118 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester configures the IUT into LE security mode 1 level 4. 

   2. The Upper Tester configures the IUT (in the Central role) to receive advertising packets from the Lower Tester (in the Peripheral role) and completes link establishment with the Lower Tester. 

   3. The Upper Tester triggers a GATT service request. 

   4. The IUT starts the encryption procedure with the Lower Tester using the LTK for the Lower Tester. 

   5. The Lower Tester fails the encryption procedure. 

   6. Perform either alternative 6A or 6B depending on how the IUT handles the encryption failure. Alternative 6A (The IUT stops the connection attempt): 

      - 6A.1 The IUT sends an event to the Upper Tester that indicates that the connection procedure trigged in Step 2 failed. 

Alternative 6B (The IUT starts the pairing process with the Lower Tester): 

- 6B.1 The IUT sends a request to the Upper Tester for user interaction to pair with the peer device. 

- 6B.2 The Upper Tester accepts the request to pair with the peer device. 

- 6B.3 The Upper Tester triggers an authentication procedure on the IUT, e.g., by an L2CAP channel. 

- 6B.4 The IUT begins LE Secure Connections Phase 1 by sending an SMP Pairing Request, with the Secure Connections bit set to 1. 

- 6B.5 The Lower Tester answers with SMP Pairing Response, with the Secure Connections bit set to 1. 

- 6B.6 The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution). 

- 6B.7 The IUT sends a successful GATT service request event to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **119 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [262 x 450] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(Peripheral) (Central)<br>IUT finds Lower Tester<br>Establishes LE connection<br>GATT service Req.<br>Encryption Req.<br>Encryption Res.<br>Fail<br>ALT 6A<br>GATT service request<br>failed<br>ALT 6B User Interface bonding<br>request<br>Bonding Resp.<br>Accept<br>SMP Pairing Req.<br>AuthReq.SC=1 LE Secure<br>Connections<br>SMP Pairing Resp<br>Phase 1<br>AuthReq.SC=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption<br>LE Secure Connections Phase 3:<br>Key distribution<br>GATT service request<br>GATT service request<br>success<br>GATT service request<br>success<br>**----- End of picture text -----**<br>


_Figure 4.64: GAP/SEC/SEM/BV-45-C [Re-pair or stop a connection attempt when a connection fails due to failed encryption, LE security mode 1 level 4] MSC_ 

- Expected Outcome 

## Pass verdict 

In Step 6A.1, the IUT sends an event to the Upper Tester that the service request failed. 

In alternative 6B, the Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted and operating in LE security mode 1 level 4. 

- 

- Notes 

It is recommended to test with a service or profile that requires security mode 1 level 4. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **120 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.7 Security modes – Broadcaster role** 

Verify the correct behavior in this mode. The role of the IUT is Broadcaster and Initiator. 

## **4.5.7.1 LE security mode 3 – Broadcaster role, Initiator** 

- Test Purpose 

Verify that the IUT in the LE security mode 3 level as specified in Table 4.27 sends BIS data. 

- Reference 

[15] 9.2.5, 1.2.2.1, 1.2.2.2 

- Initial Condition 

   - The IUT is in Isochronous Broadcasting State. 

   - The Lower Tester is in Synchronization State. 

   - The Broadcast_Code has been obtained by the IUT’s Host using an unauthenticated or authenticated method per Table 4.27 as defined by the IUT’s application. The Lower Tester may obtain the Broadcast_Code by any means, including reading the TSPX_broadcast_code IXIT parameter, and for test purposes may be considered either authenticated or unauthenticated. 

   - The encryption information is broadcast as specified in Table 4.27. 

- Test Case Configuration 

|**Test Case ID**|**Security**<br>**Level**|**Encryption**|**Initial Condition Encryption**<br>**Information**|
|---|---|---|---|
|GAP/SEC/SEM/BV-34-C|1|Disabled(0x00)|None|
|GAP/SEC/SEM/BV-35-C|2 or 3|Enabled(0x01)|The Broadcast_Code has been<br>obtained bythe IUT’s Host.|



_Table 4.27: LE security mode 3 – Broadcaster role, Initiator test cases_ 

- Test Procedure 

**==> picture [303 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Execute GAP/BIS/BBM/BV-01-C to set up a BIS<br>Repeat BIS Data<br>(Encryption)<br>BIS Data<br>(Encryption)<br>**----- End of picture text -----**<br>


_Figure 4.65: LE security mode 3 – Broadcaster role, Initiator MSC_ 

1. Perform test case GAP/BIS/BBM/BV-01-C [Broadcast Isochronous Stream Broadcasting mode]. When enabling the BIG, set the Encryption parameter as specified in Table 4.27. 

2. The Lower Tester receives the Broadcast Isochronous data. The Lower Tester and the IUT operate on the same security mode and level. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **121 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

In Step 2, the Lower Tester receives the Broadcast Isochronous data. The IUT and the Lower Tester operate on the same security mode and level. 

## **4.5.8 Security modes – Both connected roles** 

- **4.5.8.1 Security mode 4 – Initiator, Channel Establishment, Encryption Not Enabled** 

- Test Purpose 

Verify that an IUT in the security mode and level specified in Table 4.28 that initiates a data transmission to a remote service does not send a channel establishment request to the Lower Tester when encryption has not been enabled on the connection. The IUT is the initiator of the channel establishment procedure. The Lower Tester is the responder. 

- Reference 

   - [17] 5.2.2.1.2 

- Initial Condition 

   - The IUT is in Idle mode. 

   - The PSM for the service on the IUT that requires the security mode and level specified in Table 4.28 is specified in the IXIT values in Table 4.28. 

   - The Lower Tester does not support encryption. 

   - The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has stored link keys). 

   - An ACL connection is established between the devices. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|**IXIT**|
|---|---|---|
|GAP/SEC/SEM/BI-25-C [Security mode 4<br>level 2 – Initiator, Encryption Not Enabled]|Security mode 4 level 2|TSPX_psm_sm4l2|
|GAP/SEC/SEM/BI-26-C [Security mode 4<br>level 3 – Initiator, Encryption Not Enabled]|Security mode 4 level 3|TSPX_psm_sm4l3|
|GAP/SEC/SEM/BI-27-C [Security mode 4<br>level 4 – Initiator, Encryption Not Enabled]|Security mode 4 level 4|TSPX_psm_sm4l4|



_Table 4.28: Security mode 4 – Initiator, Channel Establishment, Encryption Not Enabled test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **122 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [375 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
ACL Connection Established.<br>Bring IUT in Security Mode and Level<br>Trigger Channel Creation<br>Generic Authentication Procedure<br>Generic Authentication Procedure Completes<br>Perform Link Encryption<br>Channel Creation Failure<br>(Rejected due to Connection refused – security<br>block)<br>**----- End of picture text -----**<br>


_Figure 4.66: Security mode 4 – Initiator, Channel Establishment, Encryption Not Enabled MSC_ 

   1. The Upper Tester puts the IUT into the security mode and level specified in Table 4.28. 

   2. The Upper Tester triggers a channel creation event to set up a channel with the Lower Tester. 

   3. The IUT performs the generic authentication procedure with the Lower Tester. The generic authentication procedure successfully completes. 

   4. The IUT performs link encryption with the Lower Tester. The link encryption fails. 

   5. The IUT signals to the Upper Tester that the channel creation failed after link encryption fails. 

   6. The IUT does not send an L2CAP channel establishment request to the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT is to not send an L2CAP channel establishment request to the Lower Tester. 

- **4.5.8.2 Security mode 4 – Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled** 

- Test Purpose 

Verify that an IUT in the security mode and level specified in Table 4.29 that initiates a unicast data transmission on a connectionless channel does not send unicast data to the Lower Tester when encryption has not been enabled on the connection. The IUT is the initiator of the connectionless channel procedure. 

- Reference 

   - [17] 5.2.2.1.2 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **123 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is in Idle mode. 

   - The PSM for the service on the IUT that requires the security mode and level specified in Table 4.29 is specified in the IXIT values in Table 4.29. 

   - The Lower Tester does not support encryption. 

   - The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has stored link keys). 

   - An ACL connection is established between the devices. 

- Test Case Configuration 

|**TCID**|**Security Mode and Level**|**IXIT**|
|---|---|---|
|GAP/SEC/SEM/BI-28-C [Security mode 4<br>level 2 – Initiator, Connectionless Channel,<br>Unicast Data, Encryption Not Enabled]|Security mode 4 level 2|TSPX_psm_sm4l2|
|GAP/SEC/SEM/BI-29-C [Security mode 4<br>level 3 – Initiator, Connectionless Channel,<br>Unicast Data, Encryption Not Enabled]|Security mode 4 level 3|TSPX_psm_sm4l3|
|GAP/SEC/SEM/BI-30-C [Security mode 4<br>level 4 – Initiator, Connectionless Channel,<br>Unicast Data, Encryption Not Enabled]|Security mode 4 level 4|TSPX_psm_sm4l4|



_Table 4.29: Security mode 4 – Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled test cases_ 

- Test Procedure 

**==> picture [340 x 266] intentionally omitted <==**

**----- Start of picture text -----**<br>
ACL Connection Established.<br>Bring IUT in Security Mode and Level<br>G-Frame<br>Length, CID=0x0002, data<br>Generic Authentication Procedure<br>Generic Authentication Procedure Completes<br>Perform Link Encryption<br>Encryption Failed Notification<br>**----- End of picture text -----**<br>


_Figure 4.67: Security mode 4 – Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **124 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Upper Tester puts the IUT into the security mode and level specified in Table 4.29. 

   2. The Upper Tester sends an L2CAP G-Frame to the IUT with unicast data. 

   3. The IUT performs the generic authentication procedure with the Lower Tester. The generic authentication procedure successfully completes. 

   4. The IUT performs link encryption with the Lower Tester. The link encryption fails. 

   5. The IUT signals to the Upper Tester that the link encryption fails. 

   6. The IUT does not send any unicast data to the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT is to not send any unicast data to the Lower Tester. 

**GAP/SEC/SEM/BI-31-C [Security mode 4 level 4, Secure Connections – Responder, Insufficient Encryption Type]** 

- Test Purpose 

Verify that an IUT in security mode 4 level 4 supporting Secure Connections rejects a received channel establishment request from the Lower Tester if an insufficient encryption type is selected on the connection between the IUT and the Lower Tester. The IUT is the responder of the channel establishment procedure. The Lower Tester is the initiator. 

- Reference 

   - [17] 5.2.2.2.1 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX_psm_sm4l4 IXIT value. 

   - The IUT and the Lower Tester have previously bonded using Secure Connections. 

   - An ACL connection exists between the devices. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 1 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - The IUT is in connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **125 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [363 x 270] intentionally omitted <==**

_Figure 4.68: Security mode 4 level 4, Secure Connections – Responder, Insufficient Encryption Type MSC_ 

   1. The existing ACL connection between the IUT and the Lower Tester is disconnected. 

   2. On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0. 

   3. The Lower Tester establishes an ACL connection with the IUT. 

   4. The Lower Tester requests establishing a channel to access the TSPX_psm_sm4l4 PSM. 

   5. The IUT and the Lower Tester may begin link encryption. 

   6. The IUT rejects the L2CAP channel establishment request from the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT is to reject the L2CAP channel establishment request from the Lower Tester. 

**GAP/SEC/SEM/BI-32-C [Security mode 4 level 4, Secure Connections – Initiator, Channel Establishment, Insufficient Encryption Type]** 

- Test Purpose 

Verify that an IUT in security mode 4 level 4 supporting Secure Connections rejects a received channel establishment if an insufficient encryption type is selected on the connection between the IUT and the Lower Tester. The IUT is the initiator of the channel establishment procedure. The Lower Tester is the responder. 

- Reference 

   - [17] 5.2.2.2.2 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **126 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX_psm_sm4l4 IXIT value. 

   - The IUT and the Lower Tester have previously bonded using Secure Connections. 

   - An ACL connection exists between the devices. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 1 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - The IUT is in connectable mode. 

- Test Procedure 

**==> picture [409 x 334] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester  IUT  Upper Tester<br>IUT and Lower Tester are bonded. An ACL connection exists between the devices.<br>Both devices are in Secure Connections Only mode.<br>ACL connection is disconnected<br>Secure Connections<br>(Host Support) LMP<br>feature bit is set to 0<br>Establish ACL connection.<br>ACL connection is established.<br>Trigger Channel Creation<br>ALT 5A<br>LMP_FEATURES_REQ<br>(Features)<br>LMP_FEATURES_RES<br>(Features)<br>ALT 5B<br>Encryption LMP Messages<br>Channel Connection Failure<br>(Rejected due to Connection Refused -<br>security block)<br>IUT does not send a channel<br>establishment request to the<br>Lower Tester<br>**----- End of picture text -----**<br>


_Figure 4.69: Security mode 4 level 4, Secure Connections – Initiator, Channel Establishment, Insufficient Encryption Type MSC_ 

1. The existing ACL connection between the IUT and the Lower Tester is disconnected. 

2. On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0. 

3. The Lower Tester establishes an ACL connection with the IUT. 

4. The Upper Tester triggers an event to create a channel to the Lower Tester. 

5. Perform either alternative 5A or 5B depending on the IUT behavior. Alternative 5A (The IUT executes a feature exchange): 

   - 5A.1 The IUT sends an LMP_FEATURES_REQ PDU to the Lower Tester with Features set to the IUT feature set. 

   - 5A.2 The Lower Tester sends an LMP_FEATURES_RES PDU to the IUT with Features set to the Lower Tester feature set. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **127 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## Alternative 5B (The IUT begins encryption): 

      - 5B.1 The IUT and the Lower Tester begin link encryption. 

   6. The IUT notifies the Upper Tester that the channel creation with the Lower Tester failed due to a security block. 

   7. The IUT does not send an L2CAP channel establishment request to the Lower Tester. 

- Expected Outcome 

## Pass verdict 

In Step 7, the IUT does not send an L2CAP channel establishment request to the Lower Tester. 

**GAP/SEC/SEM/BI-33-C [Security mode 4, Secure Connections – Initiator, Connectionless Channel, Unicast Data, Insufficient Encryption Type]** 

- Test Purpose 

Verify that an IUT in security mode 4 level 4 supporting Secure Connections does not send unicast data to the Lower Tester if an insufficient encryption type is selected on the connection between the IUT and the Lower Tester. The IUT is the initiator of the connectionless channel establishment procedure. The Lower Tester is the responder. 

- Reference 

   - [17] 5.2.2.2.2 

- Initial Condition 

   - The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX_psm_sm4l4 IXIT value. 

   - The IUT and the Lower Tester have previously bonded using Secure Connections. 

   - An ACL connection exists between the devices. 

   - On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 1 and the Secure Connections (Controller Support) LMP feature bit to 1. 

   - The IUT is in connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **128 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [374 x 358] intentionally omitted <==**

**----- Start of picture text -----**<br>
IUT and Lower Tester are bonded. An ACL connection exists between the devices.<br>Both devices are in Secure Connections Only mode.<br>ACL connection is disconnected.<br>Secure Connections<br>(Host Support) LMP<br>feature bit is set to 0.<br>Establish ACL connection.<br>ACL connection is established.<br>G-Frame<br>Length. CID=0x0002, data<br>Encryption LMP Messages<br>Insufficient Encryption Notification<br>The IUT does not send unicast<br>data to the Lower Tester.<br>**----- End of picture text -----**<br>


_Figure 4.70: Security mode 4, Secure Connections – Initiator, Connectionless Channel, Unicast Data, Insufficient Encryption Type MSC_ 

   1. The existing ACL connection between the IUT and the Lower Tester is disconnected. 

   2. On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0. 

   3. The Lower Tester establishes an ACL connection with the IUT. 

   4. The Upper Tester sends an L2CAP G-Frame to the IUT. 

   5. The IUT and the Lower Tester begin link encryption. 

   6. The IUT signals to the Upper Tester that the link encryption is insufficient. 

   7. The IUT does not send any unicast data to the Lower Tester. 

- 

- Expected Outcome 

## Pass verdict 

The IUT is to not send any unicast data to the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **129 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.5.9 Channel Sounding** 

## **4.5.9.1 Channel Sounding Security** 

- Test Purpose 

Verify that the IUT uses the proper CS procedure based on the LE security mode. 

- Reference 

   - [19] 10.11.1 

- Initial Condition 

   - The Lower Tester has the Channel Sounding feature bit set. 

   - The Lower Tester and the IUT have completed the encryption procedure with the LE security mode listed in Table 4.30. 

- Test Case Configuration 

|**TCID**|**LE Security Mode**|**CS Procedure**|
|---|---|---|
|GAP/SEC/SEM/BV-69-C [Channel<br>Sounding Security, CS Security L1,<br>Peripheral, Initiator]|Channel Sounding<br>Security level 1|CS Reflector procedure, CS Tone or<br>CS RTT|
|GAP/SEC/SEM/BV-70-C [Channel<br>Sounding Security, CS Security L2,<br>Peripheral, Initiator]|Channel Sounding<br>Security level 2|CS Reflector procedure, 150 ns CSS<br>RTT accuracy with CS Tones|
|GAP/SEC/SEM/BV-71-C [Channel<br>Sounding Security, CS Security L3,<br>Peripheral, Initiator]|Channel Sounding<br>Security level 3|CS Reflector procedure, 10 ns CSS<br>RTT accuracy with CS Tones|
|GAP/SEC/SEM/BV-72-C [Channel<br>Sounding Security, CS Security L4,<br>Peripheral, Initiator]|Channel Sounding<br>Security level 4|CS Reflector procedure, 10 ns CSS<br>RTT accuracy with CS RTT with<br>Sounding Sequence or CS RTT with<br>Random Sequence|
|GAP/SEC/SEM/BV-73-C [Channel<br>Sounding Security, CS Security L1,<br>Peripheral, Reflector]|Channel Sounding<br>Security level 1|CS Initiator procedure, CS Tone or<br>CS RTT|
|GAP/SEC/SEM/BV-74-C [Channel<br>Sounding Security, CS Security L2,<br>Peripheral, Reflector]|Channel Sounding<br>Security level 2|CS Initiator procedure, 150 ns CSS<br>RTT accuracy with CS Tones|
|GAP/SEC/SEM/BV-75-C [Channel<br>Sounding Security, CS Security L3,<br>Peripheral, Reflector]|Channel Sounding<br>Security level 3|CS Initiator procedure, 10 ns CSS<br>RTT accuracy with CS Tones|
|GAP/SEC/SEM/BV-76-C [Channel<br>Sounding Security, CS Security L4,<br>Peripheral, Reflector]|Channel Sounding<br>Security level 4|CS Initiator procedure, 10 ns CSS<br>RTT accuracy with CS RTT with<br>Sounding Sequence or CS RTT with<br>Random Sequence|



_Table 4.30:Channel Sounding Security test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **130 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [361 x 97] intentionally omitted <==**

_Figure 4.71: Channel Sounding Security MSC_ 

   1. The Lower Tester sends a CS procedure request specified in Table 4.30 to the IUT. 

   2. The IUT performs the CS procedure as described in Table 4.30. 

- 

- Expected Outcome 

## Pass verdict 

The IUT that is using the LE security mode specified in Table 4.30 uses the CS procedure specified in Table 4.30. 

## **4.6 Idle mode procedures** 

## **4.6.1 General Inquiry – Central** 

Verify the correct behavior in this mode. The role of the IUT is Central and initiator. 

**GAP/IDLE/GIN/BV-01-C [General Inquiry – IUT is Central]** 

- Test Purpose 

Verify that if general inquiry is initiated by the IUT, it sends for at least TGAP(100) inquiry request messages (GIAC). 

The IUT is Central and initiator and the Lower Tester is Peripheral and acceptor of the general inquiry procedure. 

- Reference 

   - [1] 6.1 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

   - If the IUT supports general-discoverable mode, the Lower Tester performs inquiry to get the clock offset with respect to the IUT and after the Upper Tester has ordered the IUT to be in generaldiscoverable mode. 

   - If the IUT does not support general-discoverable mode, the IUT has to be configured to page the Lower Tester in order to get the CLK offset after the Upper Tester has ordered the IUT to be in connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **131 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [373 x 248] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby Idle mode.<br>Initiate general inquiry<br>Inquiry (ID-Packet,  [train A 1(B) 1,..])<br>(GIAC)<br>Inquiry (ID-Packet,  [train A n(B) n,..]) Verify that the IUT performs<br>general inquiry (GIAC) for at least T<br>(GIAC)<br>GAP (100) if it was required.<br>T GAP (100)<br>**----- End of picture text -----**<br>


_Figure 4.72: GAP/IDLE/GIN/BV-01-C [General Inquiry – IUT is Central] MSC_ 

   1. The Upper Tester orders the IUT to initiate general inquiry. 

   2. The Lower Tester scans for inquiry packets from the IUT to receive a packet within the IUT’s repetition of A-train. 

   3. The Lower Tester monitors the train A during 10 ms. If no inquiry packet is received, the Lower Tester switches to scan train B during 10 ms. 

   4. Switching trains will continue until first ID packet is received by the Lower Tester. The Lower Tester adjusts its RX window and phase to get the remaining hops. 

   5. The Lower Tester monitors inquiry packets for 255 times. 

   6. The Lower Tester immediately starts listening on the other train frequencies. It monitors for 256 times. 

   7. Steps 5 and 6 are repeated until 10.24 s - 10 ms - 20 ms. 

- Expected Outcome 

## Pass verdict 

The IUT sends at least for TGAP(100) - 30 ms inquiry messages (ID-Packet) by using GIAC. 

## **4.6.2 Device Name during General Inquiry** 

Verify the correct behavior in this mode. The role of the IUT is Peripheral. 

**GAP/IDLE/DNDIS/BV-01-C [Device Name During General Inquiry – IUT is Peripheral]** 

- Test Purpose 

Verify that the Lower Tester during general inquiry receives device name from IUT in the reception of extended inquiry response data. 

The Lower Tester is Central and initiator and the IUT is Peripheral and acceptor of the general inquiry procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **132 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference 

   - [1] 8 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

   - The IUT device name is defined by the TSPX_device_name IXIT value. 

- Test Procedure 

**==> picture [375 x 262] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby Idle mode with any supported security mode. IUT is<br>configured to provide Extended Inquiry Response with Device Name.<br>Initiate<br>general  Inquiry (ID-Packet, (BB-functionality))<br>inquiry<br>(LIAC or GIAC)<br>(May be repeated several times) IUT (Peripheral) sends the<br>address and the Device<br>Inquiry (ID-Packet, (BB-functionality)) Name.<br>(LIAC or GIAC)<br>FHS-packet<br>(EIR = 1)<br>EIR-Packet<br>Lower Tester is able to decode the<br>Device name from the EIR<br>response<br>**----- End of picture text -----**<br>


_Figure 4.73: GAP/IDLE/DNDIS/BV-01-C [Device Name During General Inquiry – IUT is Peripheral] MSC_ 

   1. The Lower Tester initiates general inquiry. 

   2. The Lower Tester receives extended inquiry response data from the IUT. 

- 

- Expected Outcome 

## Pass verdict 

The Lower Tester decodes EIR data and finds the IUT's device name ('complete' or 'shortened'). 

## **4.6.3 Limited Inquiry – Central** 

Verify the correct behavior in this mode. The role of the IUT is Central and initiator. 

**GAP/IDLE/LIN/BV-01-C [Limited Inquiry – IUT is Central]** 

- Test Purpose 

Verify that if limited inquiry is initiated by the IUT, it sends for at least TGAP(100) inquiry request messages (LIAC). 

The IUT is Central and initiator and the Lower Tester is Peripheral and acceptor of the limited inquiry procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **133 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference 

   - [1] 6.2 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

   - If the IUT supports general-discoverable mode, the Lower Tester performs inquiry to get the clock offset with respect to the IUT and after the Upper Tester has ordered the IUT to be in generaldiscoverable mode. 

   - If the IUT does not support general-discoverable mode, the IUT has to be configured to page the Lower Tester in order to get the CLK offset after the Upper Tester has ordered the IUT to be in connectable mode. 

- Test Procedure 

**==> picture [338 x 229] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in BB-Standby Idle mode.<br>Initiate limited inquiry<br>Inquiry (ID-Packet,  [train A 1(B) 1,..])<br>(LIAC)<br>Inquiry (ID-Packet,  [train A n(B) n,..]) Verify that the IUT performs<br>limited inquiry (LIAC) for at least T<br>(LIAC)<br>GAP (100) if it was required.<br>T GAP (100)<br>**----- End of picture text -----**<br>


_Figure 4.74: GAP/IDLE/LIN/BV-01-C [Limited Inquiry – IUT is Central] MSC_ 

   1. The IUT is ordered (by using the Upper Tester) to initiate limited inquiry. 

   2. The Lower Tester scans for inquiry packets from the IUT to receive a packet within the IUT’s repetition of A-train. 

   3. The Lower Tester monitors the train A during 10 ms. If no inquiry packet is received, the Lower Tester switches to scan train B during 10 ms. 

   4. Switching trains will continue until first ID packet is received by the Lower Tester. The Lower Tester adjusts its RX window and phase to get the remaining hops. 

   5. The Lower Tester monitors inquiry packets for 255 times. 

   6. The Lower Tester immediately starts listening on the other train frequencies. It monitors for 256 times. 

   7. Steps 5 and 6 are repeated until 10.24s - 10ms - 20 ms. 

- Expected Outcome 

## Pass verdict 

The IUT sends at least for TGAP(100) - 30 ms inquiry messages (ID-Packet) by using LIAC. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **134 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.6.4 Device Discovery – Central** 

Verify the correct behavior in this mode. The role of the IUT is Central and initiator. 

**GAP/IDLE/DED/BV-02-C [Device Discovery and Name Discovery – Secure Simple Pairing Supported by IUT]** 

- Test Purpose 

Verify that the IUT that supports Secure Simple Pairing first performs the inquiry procedure and afterwards it performs the name discovery procedure for one Peripheral if device discovery is required by upper layer of the IUT. 

- Reference 

   - [1] 6.4 

- Initial Condition 

   - The IUT is in Idle mode with security mode 4 supported by the IUT. 

   - The Lower Tester's LMP features include: 

      - Feature bit 51 (Secure Simple Pairing) set to 1 

      - Feature bit 63 (Extended Features) set to 1 

      - Feature bit 64 (Secure Simple Pairing – Host Support) set to 1 

   - The Lower Tester is discoverable and connectable. 

- Test Procedure 

**==> picture [337 x 291] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT is in Idle mode and supports security mode 4.<br>Initiate device discovery<br>Inquiry<br>(LIAC or GIAC)<br>Inquiry IUT (Central) gets the address<br>of the Lower Tester<br>(LIAC or GIAC) (Peripheral).<br>Inquiry Response<br>Name request procedure is<br>started.<br>Name request<br>Name response Name request procedure is<br>completed<br>Verify that the IUT performs a<br>name request after having<br>performed inquiry.<br>**----- End of picture text -----**<br>


_Figure 4.75: GAP/IDLE/DED/BV-02-C [Device Discovery and Name Discovery – Secure Simple Pairing Supported by IUT] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **135 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

After inquiry, the IUT performs a successful name request procedure. 

## **4.6.5 Bonding – Central** 

Verify the correct behavior in this mode. The role of the IUT is Central and initiator. 

Applicable only for IUTs supporting initiation of dedicated bonding and initiation of limited or general inquiry. 

**GAP/IDLE/BON/BV-02-C [Bonding – Central]** 

- Test Purpose 

Verify that, if the bonding procedure is required by upper layer of the IUT with the reason only to create and exchange a link key (dedicated bonding), it performs the dedicated bonding procedure. 

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor. 

- Reference 

[1] 6.5 

- Initial Condition 

   - The Preamble “Inquiry procedure” is performed with supported security mode 2 or 4 of the IUT. 

   - The Lower Tester’s LMP features include: 

      - Feature bit 51 (Secure Simple Pairing) set to 1 

      - Feature bit 63 (Extended Features) set to 1 

      - Feature bit 64 (Secure Simple Pairing – Host Support) set to 0 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **136 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [373 x 603] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Preamble Inquiry is performed.<br>Initiate dedicated bonding<br>Page request (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>BB-funtionality: All used BB-messages are<br>Page request (BB-functionality) explained in the BB test suite.<br>(ID-packet (Peripherals DAC))<br>Page response (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>FHS-packet (BB-functionality)<br>FHS-acknowledge (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>POLL-packet (BB-functionality)<br>NULL-packet (BB-functionality)<br>LMP_features_req (features)<br>LMP_features_res (features)<br>LMP_features_req_ext (optional)<br>LMP_features_res_ext (optional)<br>Paging procedure is performed<br>LMP_host_connection_req successfully on BB-Level, and link<br>establishment is started.<br>LMP_accepted<br>(opcode: LMP_host_connection_req)<br>LMP_in_rand)<br>(rand_nr)<br>LMP_accepted<br>Authentication is initiated by<br>(opcode: LMP_in_rand)<br>IUT (LMP_Pairing)<br>LMP_comb_key<br>(rand_nr)<br>LMP_comb_key<br>(rand_nr)<br>**----- End of picture text -----**<br>


_Figure 4.76: GAP/IDLE/BON/BV-02-C [Bonding – Central] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **137 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the dedicated bonding procedure. 

   2. Afterwards, the Dedicated Bonding procedure is performed successfully. 

- Expected Outcome 

## Pass verdict 

After the authentication is completed, the IUT has sent an "LMP_detach" message. 

Verify that the resulting link key is a combination key. 

## **4.6.6 Dedicated Bonding test cases** 

## **GAP/IDLE/BON/BV-03-C [Dedicated Bonding]** 

- Test Purpose 

Verify that dedicated bonding is performed. 

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor. 

- Reference 

[1] 6.5 

- Initial Condition 

   - The Preamble “Inquiry procedure” is performed with security mode 4 of the IUT. 

   - The Lower Tester’s LMP features include: 

      - Feature bit 51 (Secure Simple Pairing) set to 1 

      - Feature bit 63 (Extended Features) set to 1 

      - Feature bit 64 (Secure Simple Pairing – Host Support) set to 1 

   - The Lower Tester’s IO capabilities are set to “DisplayYesNo”. 

   - The Lower Tester’s Authentication_Requirements set to “MITM protection not required – Dedicated Bonding” (0x02). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **138 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

Upper Tester LMP_features_req_ext LMP_features_res_ext 

_Figure 4.77: GAP/IDLE/BON/BV-03-C [Dedicated Bonding] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **139 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the dedicated bonding procedure. 

   2. Afterwards, the Dedicated Bonding procedure is performed successfully. 

- Expected Outcome 

## Pass verdict 

After the authentication is completed, the IUT has sent an “LMP_detach” message. 

Verify that the Authentication_Requirements parameter received from the IUT is either: 0x02 (MITM Protection Not Required – Dedicated Bonding) 

or 

- 0x03 (MITM Protection Required – Dedicated Bonding). 

If the Authentication_Requirements parameter is 0x02, verify that the link key is an unauthenticated combination key. If the Authentication_Requirements parameter is 0x03, verify that the link key is an authenticated combination key. 

**GAP/IDLE/BON/BV-04-C [Dedicated Bonding – Authenticated Link Key]** 

- Test Purpose 

Verify that dedicated bonding is performed. 

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor. 

- Reference 

[1] 6.5 

- Initial Condition 

   - The Preamble “Inquiry procedure” is performed. 

   - The Lower Tester’s LMP features include: 

      - Feature bit 51 (Secure Simple Pairing) set to 1 

      - Feature bit 63 (Extended Features) set to 

      - Feature bit 64 (Secure Simple Pairing – Host Support) set to 1 

   - The Lower Tester’s IO capabilities are set to “DisplayYesNo”. 

   - The Lower Tester’s Authentication_Requirements set to “MITM protection required – Dedicated Bonding” (0x03). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **140 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

Upper Tester LMP_features_req_ext LMP_features_res_ext 

_Figure 4.78: GAP/IDLE/BON/BV-04-C [Dedicated Bonding – Authenticated Link Key] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **141 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the dedicated bonding procedure. 

   2. Afterwards, the Dedicated Bonding procedure is performed successfully. 

- Expected Outcome 

## Pass verdict 

After the authentication is completed, the IUT has sent an “LMP_detach” message. 

Verify that the Authentication_Requirements parameter received from the IUT is either: 0x02 (MITM Protection Not Required – Dedicated Bonding) or 

0x03 (MITM Protection Required – Dedicated Bonding). 

Verify that the resulting link key is an authenticated combination key. 

## **4.6.7 General Bonding test cases** 

## **GAP/IDLE/BON/BV-05-C [General Bonding]** 

- Test Purpose 

Verify that general bonding is performed. 

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor. 

- Reference 

[1] 6.5 

- Initial Condition 

   - The Preamble “Inquiry procedure” is performed with security mode 4 of the IUT. 

   - The Lower Tester’s LMP features include: 

      - Feature bit 51 (Secure Simple Pairing) set to 1 

      - Feature bit 63 (Extended Features) set to 1 

      - Feature bit 64 (Secure Simple Pairing – Host Support) set to 1 

   - The Lower Tester’s IO capabilities are set to “DisplayYesNo”. 

   - The Lower Tester’s Authentication_Requirements set to “MITM protection no required – General Bonding” (0x04). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **142 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [374 x 594] intentionally omitted <==**

**----- Start of picture text -----**<br>
Upper Tester<br>LMP_features_req_ext<br>LMP_features_res_ext<br>**----- End of picture text -----**<br>


_Figure 4.79: GAP/IDLE/BON/BV-05-C [General Bonding] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **143 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the general bonding procedure. 

   2. Afterwards, the General Bonding procedure is performed successfully. 

- Expected Outcome 

## Pass verdict 

After the authentication is completed, the IUT has sent an “L2CAP_connect_req” message. 

Verify that the Authentication_Requirements parameter received from the IUT is either: 0x04 (MITM Protection Not Required – General Bonding) or 

0x05 (MITM Protection Required – General Bonding). 

If the Authentication_Requirements parameter is 0x04, verify that the link key is an unauthenticated combination key. If the Authentication_Requirements parameter is 0x05, verify that the link key is an authenticated combination key. 

**GAP/IDLE/BON/BV-06-C [General Bonding – Authenticated Link Key]** 

- Test Purpose 

Verify that general bonding is performed. 

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor. 

- Reference 

[1] 6.5 

- Initial Condition 

   - The Preamble “Inquiry procedure” is performed with security mode 4 of the IUT. 

   - The Lower Tester’s LMP features include: 

      - Feature bit 51 (Secure Simple Pairing) set to 1 

      - Feature bit 63 (Extended Features) set to 1 

      - Feature bit 64 (Secure Simple Pairing – Host Support) set to 1 

   - The Lower Tester’s IO capabilities are set to “DisplayYesNo”. 

   - The Lower Tester’s Authentication_Requirements are set to “MITM Protection Required – General Bonding” (0x05). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **144 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

Upper Tester LMP_features_req_ext LMP_features_res_ext 

_Figure 4.80: GAP/IDLE/BON/BV-06-C [General Bonding – Authenticated Link Key] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **145 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the general bonding procedure. 

   2. Afterwards, the General Bonding procedure is performed successfully. 

- Expected Outcome 

## Pass verdict 

After the authentication is completed, the IUT has sent an “L2CAP_connect_req” message. 

Verify that the Authentication_Requirements parameter received from the IUT is either: 0x04 (MITM Protection Not Required – General Bonding) or 

0x05 (MITM Protection Required – General Bonding). 

Verify that the resulting link key is an authenticated combination key. 

## **4.6.8 Link Establishment – Central** 

Verify the correct behavior in this mode. The role of the IUT is Central and initiator. 

**GAP/EST/LIE/BV-02-C [Link Establishment – Initiator]** 

- Test Purpose 

Verify that the IUT performs a link establishment procedure, initiated by itself. 

The IUT is Central and initiator. The Lower Tester is Peripheral and acceptor of the link establishment procedure. 

- Reference 

[1] 7.1 

- Initial Condition 

   - The IUT is in Baseband state ‘Standby’ and in Idle mode. 

   - The Lower Tester is in the Discoverable mode. 

   - The Preamble for “Inquiry procedure” is performed. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **146 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## • Test Procedure 

**==> picture [374 x 557] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Preamble Inquiry is performed.<br>Initiate connection<br>Page request (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>Page request (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>Page response (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>FHS-packet (BB-functionality)<br>FHS-acknowledge (BB-functionality)<br>(ID-packet (Peripherals DAC))<br>POLL-packet (BB-functionality)<br>LMP_features_req (features)<br>LMP_features_res (features)<br>LMP_host_connection_req Paging procedure is performed<br>successfully on BB-Level and link<br>establishment is started.<br>LMP_accepted<br>(opcode: LMP_host_connection_req)<br>If the IUT is in security mode 3 it<br>initiates an authentication procedure<br>Generic Authentication Procedure and performs optional encryption<br>procedure.<br>encryption messages<br>Verify that a mutual<br>LMP_setup_complete occur to<br>accomplish the link establishment<br>LMP_setup_complete initiated by IUT.<br>**----- End of picture text -----**<br>


_Figure 4.81: GAP/EST/LIE/BV-02-C [Link Establishment – Initiator] MSC_ 

## • Expected Outcome 

## Pass verdict 

For completion of the link establishment a mutual “LMP_setup_complete” occurs. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **147 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7 Operational modes and procedures for use on LE physical channels** 

## **4.7.1 Broadcasting and Observing** 

Verify the correct implementation of the Broadcast Mode and Observation procedure. 

## **4.7.1.1 Broadcast mode** 

Verify the correct implementation of the Broadcast mode. 

## **GAP/BROB/BCST/BV-01-C [Broadcast mode, No Scan Response]** 

- Test Purpose 

Verify that the IUT in Broadcast mode does not implement scan response data; the peer device is Passive Scanning. 

- Reference 

   - [4], [6], [9] 9.1.1, 9.1.1.2 

[7] 1.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The advertising data in Broadcast mode for the IUT is defined by the TSPX_advertising_data IXIT value. 

- Test Procedure 

   1. The Lower Tester performs the Observation procedure using Passive Scanning. 

   2. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data. 

**==> picture [305 x 135] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Observation<br>Procedure<br>Passive  Enter Broadcast Mode<br>Scanning<br>Advertising Event<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.82: GAP/BROB/BCST/BV-01-C [Broadcast mode, no scan response] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events sent by the IUT. 

The Lower Tester receives the specified advertising data sent from the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **148 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0. 

- Notes 

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

## **GAP/BROB/BCST/BV-02-C [Broadcast mode, Scan Response]** 

- Test Purpose 

Verify that the IUT is in Broadcast mode and implements scan response data; the peer device is Active Scanning. 

- Reference 

   - [4] 9.1.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The advertising data in Broadcast mode is specified for the IUT as defined by the TSPX_advertising_data IXIT value. 

- Test Procedure 

   1. The Lower Tester performs the Observation procedure using Active Scanning. 

   2. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data. 

**==> picture [304 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Observation<br>Procedure  Enter Broadcast Mode<br>Active<br>Scanning<br>Advertising Event<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.83: GAP/BROB/BCST/BV-02-C [Broadcast mode, scan response] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives scannable advertising events sent by the IUT. 

The Lower Tester receives the specified advertising data and scan response data sent from the IUT. 

The advertising data or scan response data either does not contains the Flags AD type or contains the Flags AD type but the LE Limited Discoverable Flag and the LE General Discoverable Flag are not set. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **149 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Notes 

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

## **GAP/BROB/BCST/BV-03-C [Broadcast mode, Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT in Broadcast mode is using a resolvable private address. 

- Reference 

   - [4], [6], [9] 9.1.1, 9.1.1.2 

[7] 1.3 

[9] 10.7 [11] 1.3.2.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections. 

   - The advertising data in Broadcast mode is specified by the TSPX_advertising_data IXIT value. 

- The Device Identity (IRK and Identity Address) used in the Resolvable Private Address Generation procedure and Resolvable Private Address Resolution procedure is specified by the TSPX_iut_device_IRK_for_resolvable_privacy_address_generation_procedure and 

TSPX_identity_address IXIT values for the IUT. Alternatively, the IUT may use a Device Identity distributed to the Lower Tester prior to executing this test procedure. 

- Test Procedure 

   1. The Lower Tester performs the Observation procedure using Passive Scanning. 

   2. The IUT generates a resolvable private address using the Resolvable Private Address Generation procedure. 

   3. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data; the IUT advertises using a generated resolvable private address. 

**==> picture [304 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Observation<br>Procedure<br>Passive  Enter Broadcast Mode<br>Scanning<br>Advertising Event<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.84: GAP/BROB/BCST/BV-03-C [Broadcast mode, Resolvable Private Address] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **150 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events sent by the IUT. 

The Lower Tester receives the specified advertising data sent from the IUT. 

The Lower Tester successfully resolves the private address (the private address is associated with the IUT) received in the advertising events using the Resolvable Private Address Resolution procedure. 

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0. 

- Notes 

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

## **GAP/BROB/BCST/BV-04-C [Broadcast mode, Non-Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT in Broadcast mode is using a non-resolvable private address. 

- Reference 

[6], [9] 10.7.3, 9.1.1.2 

[7] 1.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The advertising data in Broadcast mode is specified for the IUT in the TSPX_advertising_data IXIT value. 

   - TGAP (private_addr_int) for the IUT is specified in the TSPX_iut_private_address_interval IXIT value. 

- Test Procedure 

   1. The Lower Tester performs the Observation procedure using Passive Scanning. 

   2. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data; the IUT generates a non-resolvable private address using the non-resolvable Private Address Generation procedure and advertises using the generated non-resolvable private address. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **151 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Enter Broadcasting Mode<br>Observation<br>Procedure<br>Passive<br>Scanning<br>Advertising Event<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.85: GAP/BROB/BCST/BV-04-C [Broadcast mode, Non-Resolvable Private Address] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events sent by the IUT. 

The Lower Tester receives the specified advertising data sent from the IUT that includes the nonresolvable private address. 

The Lower Tester verifies that the IUT changes the non-resolvable private address in the advertiser address of the received advertising events after TGAP(private_addr_int). 

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0. 

- Notes 

Since broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

**GAP/BROB/BCST/BV-05-C [Broadcast mode, Resolvable Private Address, Scan Response]** 

- Test Purpose 

Verify that the IUT in Broadcast mode implements scan response data using a resolvable private address; the Lower Tester is Active Scanning. Lower Tester and IUT are using Resolvable Private Addresses and Filter Accept List. 

- Reference 

   - [7] 1.3 

[9] 9.1.1, 10.7.3, 9.1.1.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **152 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - The advertising data in Broadcast mode is specified for the IUT in the TSPX_advertising_data IXIT value. 

   - The Lower Tester and the IUT have exchanged bonding information for resolving. 

- Test Procedure 

   1. The Lower Tester performs the Observation procedure using Active Scanning. 

   2. The Upper Tester adds the device identity of the Lower Tester to the Resolving List. 

   3. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising and scan response data; the IUT advertises using the generated resolvable private address. 

   4. The Lower Tester resolves the address of the IUT and sends a scan request to the IUT. 

   5. The IUT resolves the scan request but the Lower Tester is not in the Filter Accept List, so no scan response is sent. 

   6. The Upper Tester orders the IUT to add the Lower Tester’s Identity to the Filter Accept List, and continue advertising using the generated resolvable private address. 

   7. The Lower Tester resolves the address of the IUT and sends a scan request to the IUT. 

   8. The IUT resolves the scan request, identifies the Lower Tester on the Filter Accept List, and sends a scan response. 

**==> picture [306 x 362] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Observation<br>Procedure  Add Lower Tester Identity to<br>Passive  Resolving List<br>Scanning<br>Enter Broadcast Mode<br>Advertising Event<br>Advertising Event<br>Address<br>Resolution<br>Scan Request<br>Address<br>Resolution<br>Device not in<br>filter accept list<br>Add Lower Tester Identity to<br>Advertising Event Filter Accept List<br>Advertising Event<br>Address<br>Resolution<br>Scan Request<br>Address<br>Resolution<br>Scan Response<br>**----- End of picture text -----**<br>


_Figure 4.86: GAP/BROB/BCST/BV-05-C [Broadcast mode, Resolvable Private Address, Scan Response] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **153 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives scannable advertising events sent by the IUT. 

The Lower Tester receives the specified advertising data sent from the IUT. 

The Lower Tester successfully resolves the private address (the private address is associated with the IUT) received in the advertising events. 

The Lower Tester sends scan requests to the IUT. Before the Lower Tester’s identity address is added to the IUT’s Filter Accept List, the Lower Tester does not receive any scan response. After adding the Lower Tester’s identity address to the IUT’s Filter Accept List, the Lower Tester receives the scan responses with the specified scan response data sent from the IUT. 

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0. 

- Notes 

Since broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

## **4.7.1.2 Observation procedure** 

Verify the correct implementation of the Observation procedure. 

## **GAP/BROB/OBSV/BV-01-C [Observation procedure, Passive Scanning]** 

- Test Purpose 

Verify the IUT performing the Observation procedure using Passive Scanning. 

- Reference 

[4] 9.1.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The advertising data used in Broadcast mode is specified for the Lower Tester in the TSPX_advertising_data IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Broadcast mode using the specified advertising data. 

   2. The Upper Tester orders the IUT to perform the Observation procedure using Passive Scanning. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **154 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Broadcast<br>Mode<br>Perform Observation Procedure<br>Advertising Event<br>Advertising Event<br>**----- End of picture text -----**<br>


**==> picture [188 x 44] intentionally omitted <==**

_Figure 4.87: GAP/BROB/OBSV/BV-01-C [Observation procedure, Passive Scanning] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the specified advertising data sent from Lower Tester. 

- Notes 

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

## **GAP/BROB/OBSV/BV-02-C [Observation procedure, Active Scanning]** 

- Test Purpose 

Verify the IUT performing the Observation procedure using Active Scanning. 

- Reference 

[4] 9.1.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The advertising data used in Broadcast mode is specified for the Lower Tester in the TSPX_advertising_data IXIT value. 

   - The scan response data used in Broadcast mode is specified for the Lower Tester in the TSPX_scan_response_data IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Broadcast mode using the specified advertising data. 

   2. The Upper Tester orders the IUT to perform the Observation procedure using Active Scanning. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **155 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [301 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower<br>IUT Upper Tester<br>Tester<br>Broadcast<br>Mode<br>Start Observation<br>Procedure<br>Advertising Event<br>Advertising Event<br>Advertising Report Event<br>**----- End of picture text -----**<br>


_Figure 4.88: GAP/BROB/OBSV/BV-02-C [Observation procedure, Active Scanning] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the specified advertising data and scan response data from Lower Tester. 

- Notes 

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

**GAP/BROB/OBSV/BV-05-C [Observation procedure, Active Scanning Non-Resolvable Private Address or Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT can perform the Observation procedure using Active Scanning and a nonresolvable private address or resolvable private address. 

- Reference 

   - [4], [9] 9.1.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The advertising data used in Broadcast mode is specified for the Lower Tester in the TSPX_advertising_data IXIT value. 

   - The scan response data used in Broadcast mode is specified for the Lower Tester in the TSPX_scan_response_data IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Broadcast mode using scannable undirected advertising events containing the specified advertising data and responds to scan requests using the specified scan response data. 

   2. The Upper Tester orders the IUT to perform the Observation procedure using Active Scanning and a non-resolvable private address or resolvable private address. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **156 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [285 x 258] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Broadcast<br>Mode<br>Start Observation Procedure<br>Advertising Event<br>Advertising Event<br>Advertising Report Event<br>Scan Request<br>Scan Response<br>Scan Report Event<br>**----- End of picture text -----**<br>


_Figure 4.89: GAP/BROB/OBSV/BV-05-C [Observation procedure, Active Scanning Non-Resolvable Private Address or Resolvable Private Address] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the specified advertising data and scan response data sent by the Lower Tester. 

The Lower Tester receives a non-resolvable private address or a resolvable private address in scan request sent from the IUT. 

- Notes 

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

**GAP/BROB/OBSV/BV-06-C [Observation procedure with Active Scanning, IUT and Peer using Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT can perform the Observation procedure using Active Scanning when the Lower Tester is using a resolvable private address. 

- Reference 

[6], [9] 9.1.2, 10.7.4 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **157 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections. 

   - The Lower Tester and the IUT have exchanged bonding information for resolving. 

   - The advertising and scan response data used in Broadcast mode is specified for the Lower Tester in the TSPX_advertising_data and TSPX_scan_response_data IXIT values. 

- Test Procedure 

   1. The Lower Tester generates a resolvable private address using the Resolvable Private Address Generation procedure. 

   2. The Lower Tester enters Broadcast mode using the specified advertising data and the generated resolvable private address. 

   3. The Upper Tester orders the IUT to add the Lower Tester’s Identity to the resolving list and Filter Accept List. 

   4. The Upper Tester orders the IUT to perform the Observation procedure using Active Scanning; the IUT resolves the address received in the advertising events sent by the Lower Tester, and sends a Scan Request. 

   5. The Lower Tester resolves the IUT’s address and send the Scan Response. 

**==> picture [278 x 208] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Add Lower Tester Identity to<br>Resolving List<br>Perform Observation Procedure<br>Start<br>Advertising<br>Add Lower Tester Identity to<br>Filter Accept List<br>Advertising Event<br>Address<br>Resolution<br>Scan Request<br>Address<br>Resolution<br>Scan Response<br>Advertising Report Event<br>**----- End of picture text -----**<br>


_Figure 4.90: GAP/BROB/OBSV/BV-06-C [Observation procedure with Active Scanning, IUT and Peer using Resolvable Private Address] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT successfully resolves the address in the advertising events sent by the Lower Tester. 

The IUT receives the Scan Response data correctly. 

- 

- Notes 

Since broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **158 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.2 Discovery modes and procedures** 

## **4.7.2.1 Non-Discoverable mode** 

**GAP/DISC/NONM/BV-01-C [Non-Discoverable mode, Non-Connectable mode]** 

- Test Purpose 

Verify that the IUT in Non-Discoverable mode and Non-Connectable mode is not discoverable by a device performing the General Discovery procedure using Active Scanning. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4], [6], [9] 9.2.2, 9.2.2.2 

   - [7] 1.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Non-Connectable mode. 

- Test Procedure 

   1. The Lower Tester performs the General Discovery procedure using Active Scanning. 

   2. The Upper Tester orders IUT to enter Non-Discoverable mode and Non-Connectable mode. 

**==> picture [303 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General<br>Discovery<br>Procedure<br>Non-Discoverable Mode and<br>Non-Connectable Mode<br>Advertising Event<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.91: GAP/DISC/NONM/BV-01-C [Non-Discoverable mode, Non-Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either no advertising events or non-connectable advertising events from the IUT. 

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0. 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **159 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **GAP/DISC/NONM/BV-02-C [Non-Discoverable mode, Undirected Connectable mode]** 

- Test Purpose 

Verify that the IUT in Non-Discoverable mode and Undirected Connectable mode is not discoverable by a device performing the General Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.2.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Undirected Connectable mode. 

- Test Procedure 

   1. The Lower Tester performs the General Discovery procedure. 

   2. The Upper Tester orders IUT to enter Non-Discoverable mode and Undirected Connectable mode. 

**==> picture [304 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Discovery<br>Procedure<br>Non-Discoverable Mode and<br>Undirected Connectable Mode<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.92: GAP/DISC/NONM/BV-02-C [Non-Discoverable mode, Undirected Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT. 

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0. 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **160 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.2.2 Limited Discoverable mode** 

**GAP/DISC/LIMM/BV-01-C [Limited Discoverable mode, Non-Connectable mode – BR/EDR/LE]** 

- Test Purpose 

Verify that the IUT in Limited Discoverable mode and the Non-Connectable mode can be discovered by a device performing the Limited Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.2.3, 13.1.1.2, 9.2.3.2 

   - [6], [9] 9.2.3, 13.1.1 

   - [7] 1.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Non-Connectable mode. 

   - TGAP(lim_adv_timeout) for the IUT is specified in the TSPX_lim_adv_timeout IXIT value. 

- Test Procedure 

The Upper Tester orders the IUT to enter Limited Discoverable mode and Non-Connectable mode. 

**==> picture [303 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Limited Discovery<br>Procedure Limited Discoverable Mode<br>and Non-Connectable<br>Mode<br>Advertising Event<br>Advertising Event TLE_GAP(lim_a<br>dv_timeout)<br>**----- End of picture text -----**<br>


_Figure 4.93: GAP/DISC/LIMM/BV-01-C [Limited Discoverable mode, Non-Connectable mode – BR/EDR/LE] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events from the IUT. 

The advertising data contains the Flags AD type as follows: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **161 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- BR/EDR Not Supported flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

Within TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, if the Lower Tester receives advertising data from the IUT containing the Flags AD type, the General Discoverable Flag is set to 0 and the Limited Discoverable Flag set to 1. 

After TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type as described: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

- BR/EDR Not Supported flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

**GAP/DISC/LIMM/BV-02-C [Limited Discoverable mode, Undirected Connectable mode – BR/EDR/LE]** 

- Test Purpose 

Verify that the IUT in Limited Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the Limited Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.2.3, 13.1.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Undirected Connectable mode. 

   - TGAP(lim_adv_timeout) is specified for the IUT in the TSPX_lim_adv_timeout IXIT value. 

- Test Procedure 

The Upper Tester orders the IUT to enter Limited Discoverable mode and Undirected Connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **162 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [299 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Limited Discovery<br>Procedure Limited Discoverable Mode<br>and Undirected<br>Connectable Mode<br>Advertising Event<br>TLE_GAP<br>Advertising Event (lim_adv_ti<br>meout)<br>**----- End of picture text -----**<br>


_Figure 4.94: GAP/DISC/LIMM/BV-02-C [Limited Discoverable mode, Undirected Connectable mode – BR/EDR/LE] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT. 

The advertising data received by the Lower Tester contains the Flags AD type as described: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

- BR/EDR Not Supported flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

Within TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester receives advertising data from the IUT containing the Flags AD type as described: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

- BR/EDR Not Supported flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

After TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type with the Limited Discoverable Flag set to 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **163 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/DISC/LIMM/BV-03-C [Limited Discoverable mode, Non-Connectable mode – LE Only]** 

- Test Purpose 

Verify that an LE only IUT in Limited Discoverable mode and the Non-Connectable mode can be discovered by a device performing the Limited Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4], [6], [9] 9.2.3, 9.2.3.2 

   - [7] 1.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Non-Connectable mode. 

   - TGAP(lim_adv_timeout) for the IUT is specified in the TSPX_lim_adv_timeout IXIT value. 

- Test Procedure 

The Upper Tester orders the IUT to enter Limited Discoverable mode and Non-Connectable mode. 

**==> picture [303 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Limited Discovery<br>Procedure Limited Discoverable Mode<br>and Non-Connectable<br>Mode<br>Advertising Event<br>Advertising Event TLE_GAP<br>(lim_adv_ti<br>meout)<br>**----- End of picture text -----**<br>


_Figure 4.95: GAP/DISC/LIMM/BV-03-C [Limited Discoverable mode, Non-Connectable mode – LE Only] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events from the IUT. 

The advertising data contains the Flags AD type as follows: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

- BR/EDR Not Supported flag set to 1 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **164 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

Within TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester receives advertising data from the IUT containing the Flags AD type as described: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

- BR/EDR Not Supported flag set to 1 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

After TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type with the Limited Discoverable Flag set to 1. 

**GAP/DISC/LIMM/BV-04-C [Limited Discoverable mode, Undirected Connectable mode – LE Only]** 

- Test Purpose 

Verify that an LE only IUT in Limited Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the Limited Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.2.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Undirected Connectable mode. 

   - TGAP(lim_adv_timeout) is specified for the IUT in the TSPX_lim_adv_timeout IXIT value. 

- Test Procedure 

The Upper Tester orders the IUT to enter Limited Discoverable mode and Undirected Connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **165 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Limited Discovery<br>Procedure Limited Discoverable Mode<br>and Undirected<br>Connectable Mode<br>Advertising Event<br>TLE_GAP<br>Advertising Event (lim_adv_ti<br>meout)<br>**----- End of picture text -----**<br>


_Figure 4.96: GAP/DISC/LIMM/BV-04-C [Limited Discoverable mode, Undirected Connectable mode – LE Only] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT. 

The advertising data received by the Lower Tester contains the Flags AD type as described: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

- BR/EDR Not Supported flag set to 1 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

Within TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester receives advertising data from the IUT containing the Flags AD type as described: 

- Limited Discoverable flag set to 1 

- General Discoverable flag set to 0 

- BR/EDR Not Supported flag set to 1 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

After TGAP(lim_adv_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type with the Limited Discoverable Flag set to 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **166 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.2.3 General Discoverable mode** 

**GAP/DISC/GENM/BV-01-C [General Discoverable mode, Non-Connectable mode – BR/EDR/LE]** 

- Test Purpose 

Verify that the IUT in General Discoverable mode and the Non-Connectable mode can be discovered by a device performing the General Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.2.4, 9.2.4.2, 13.1.1.2 

   - [6], [9] 9.2.4, 13.1.1 

## [7] 1.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Non-Connectable mode. 

   - The Lower Tester performs the General Discovery procedure. 

- Test Procedure 

The Upper Tester orders IUT to enter General Discoverable mode and Non-Connectable mode. 

**==> picture [305 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Discovery<br>Procedure<br>General Discoverable Mode and<br>Non-Connectable Mode<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.97: GAP/DISC/GENM/BV-01-C [General Discoverable mode, Non-Connectable mode – BR/EDR/LE] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events from the IUT. 

The advertising data contains the Flags AD type as follows: 

- Limited Discoverable flag set to 0 

- General Discoverable flag set to 1 

- BR/EDR Not Supported flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **167 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

**GAP/DISC/GENM/BV-02-C [General Discoverable mode, Undirected Connectable mode – BR/EDR/LE]** 

- Test Purpose 

Verify that the IUT in General Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the General Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.2.4, 13.1.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Undirected Connectable mode. 

   - The Lower Tester performs the General Discovery procedure. 

- Test Procedure 

The Upper Tester orders the IUT to enter General Discoverable mode and Undirected Connectable mode. 

**==> picture [305 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Discovery<br>Procedure<br>General Discoverable Mode and<br>the Undirected Connectable<br>Mode<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.98: GAP/DISC/GENM/BV-02-C [General Discoverable mode, Undirected Connectable mode – BR/EDR/LE] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT. 

The advertising data received by the Lower Tester contains the Flags AD as described: 

- Limited Discoverable flag set to 0 

- General Discoverable flag set to 1 

- BR/EDR Not Supported flag set to 0 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **168 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

**GAP/DISC/GENM/BV-03-C [General Discoverable mode, Non-Connectable mode – LE Only]** 

- Test Purpose 

Verify that an LE only IUT in General Discoverable mode and the Non-Connectable mode can be discovered by a device performing the General Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

[4] 9.2.4, 9.2.4.2. 13.1.1.2 

[6], [9] 9.2.4, 13.1.1 

[7] 1.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Non-Connectable mode. 

   - The Lower Tester performs the General Discovery procedure. 

- Test Procedure 

The Upper Tester orders the IUT to enter General Discoverable mode and Non-Connectable mode. 

**==> picture [305 x 104] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Discovery<br>Procedure<br>General Discoverable Mode and<br>Non-Connectable Mode<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.99: GAP/DISC/GENM/BV-03-C [General Discoverable mode, Non-Connectable mode – LE Only] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **169 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events from the IUT. 

The advertising data contains the Flags AD type as follows: 

- Limited Discoverable flag set to 0 

- General Discoverable flag set to 1 

- BR/EDR Not Supported flag set to 1 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

**GAP/DISC/GENM/BV-04-C [General Discoverable mode, Undirected Connectable mode – LE Only]** 

- Test Purpose 

Verify that an LE only IUT in General Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the General Discovery procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.2.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Undirected Connectable mode. 

   - The Lower Tester performs the General Discovery procedure. 

- Test Procedure 

The Upper Tester orders the IUT to enter General Discoverable mode and Undirected Connectable mode. 

**==> picture [303 x 109] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Discovery<br>Procedure<br>General Discoverable Mode and<br>the Undirected Connectable<br>Mode<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.100: GAP/DISC/GENM/BV-04-C [General Discoverable mode, Undirected Connectable mode – LE Only] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **170 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT. 

The advertising data received by the Lower Tester contains the Flags AD type as described: 

- Limited Discoverable flag set to 0 

- General Discoverable flag set to 1 

- BR/EDR Not Supported flag set to 1 

- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0 

- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0 

If the Flags AD type is present in the advertising data then it only appears once per advertising event. 

The Flags AD type is not present in any scan response data received. 

## **4.7.2.4 Limited Discovery procedure** 

## **GAP/DISC/LIMP/BV-01-C [Limited Discovery procedure, find Limited Discoverable device]** 

- Test Purpose 

Verify that the IUT can perform the Limited Discovery procedure to find a device in the Limited Discoverable mode. 

The IUT is operating in the Central role. 

- Reference 

[4] 9.2.5 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(lim_disc_scan_min) for the IUT is specified in the TSPX_Tgap_lim_disc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Limited Discoverable mode. 

   2. The Upper Tester orders the IUT to perform the Limited Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **171 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Limited  Limited<br>Discoverable Mode Discovery Procedure<br>Advertising Event<br>Discovered Device<br>TGAP(lim_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.101: GAP/DISC/LIMP/BV-01-C [Limited Discovery procedure, find Limited Discoverable device] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN_REQ is a nonresolvable private address. 

The IUT lists the Lower Tester during the discovery period. 

**GAP/DISC/LIMP/BV-02-C [Limited Discovery procedure does not find General Discoverable device]** 

- Test Purpose 

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the General Discoverable mode. 

The IUT is operating in the Central role. 

- Reference 

[4] 9.2.5 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(gen_disc_scan_min) for the IUT is specified in the TSPX_Tgap_gen_disc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters General Discoverable mode. 

   2. The Upper Tester orders the IUT to perform the Limited Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **172 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [336 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General  Limited<br>Discoverable Mode Discovery Procedure<br>Advertising Event<br>TGAP(lim_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.102: GAP/DISC/LIMP/BV-02-C [Limited Discovery procedure does not find general discoverable device] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN_REQ is a nonresolvable private address. 

The IUT does not discover the Lower Tester during the discovery period. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

## **GAP/DISC/LIMP/BV-03-C [Limited Discovery procedure does not find Broadcast device]** 

- Test Purpose 

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the Broadcast mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.2.5 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(lim_disc_scan_min) for the IUT is specified in the TSPX_Tgap_lim_disc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Broadcast mode. 

   2. The Upper Tester orders the IUT to perform the Limited Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **173 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [334 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Broadcast Mode Limited<br>Discovery Procedure<br>Advertising Event<br>Discovered Device<br>TGAP(lim_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.103: GAP/DISC/LIMP/BV-03-C [Limited Discovery procedure does not find Broadcast device] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN_REQ is a nonresolvable private address. 

The IUT does not discover the Lower Tester during the discovery period. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

**GAP/DISC/LIMP/BV-04-C [Limited Discovery procedure does not find Undirected Connectable device]** 

- Test Purpose 

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the Undirected Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.2.5 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(lim_disc_scan_min) for the IUT is specified in the TSPX_Tgap_lim_disc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Undirected Connectable mode; the Lower Tester does not include the Flags AD type in the advertising data with either the General Discoverable Flag or Limited Discoverable Flag set to 1. 

   2. The Upper Tester orders the IUT to perform the Limited Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **174 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [334 x 161] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Undirected  Limited<br>Connectable Mode Discovery Procedure<br>Advertising Event<br>TGAP(lim_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.104: GAP/DISC/LIMP/BV-04-C [Limited Discovery procedure does not find Undirected Connectable device] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT does not discover the Lower Tester during the discovery period. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

**GAP/DISC/LIMP/BV-05-C [Limited Discovery procedure does not find Directed Connectable device]** 

- Test Purpose 

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the Directed Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.2.5 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(lim_disc_scan_min) for the IUT is specified in the TSPX_Tgap_lim_disc_scan_min IXIT value. 

   - The initiator address for the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Limited Discovery procedure. 

   2. The Lower Tester enters Directed Connectable mode using the specified initiator address for the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **175 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [334 x 154] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Directed  Limited<br>Connectable Mode Discovery Procedure<br>Advertising Event<br>TGAP(lim_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.105: GAP/DISC/LIMP/BV-05-C [Limited Discovery procedure does not find Directed Connectable device] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT does not discover the Lower Tester during the discovery period. 

- 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

## **4.7.2.5 General Discovery procedure** 

**GAP/DISC/GENP/BV-01-C [General Discovery procedure, finding General Discoverable device]** 

- Test Purpose 

Verify that the IUT can perform the General Discovery procedure and can find a device in the General Discoverable mode. 

The IUT is operating in the Central role. 

- Reference 

## [4] 9.2.6 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(gen_disc_scan_min) for the IUT is specified in the TSPX_Tgap_gen_disc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters General Discoverable mode. 

   2. The Upper Tester orders IUT to start the General Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **176 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [339 x 154] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General  General<br>Discoverable Mode Discovery Procedure<br>Advertising Event<br>Discovered Device<br>TGAP(gen_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.106: GAP/DISC/GENP/BV-01-C [General Discovery procedure finding General Discoverable device] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT discovers the Lower Tester during the General Discovery procedure. 

**GAP/DISC/GENP/BV-02-C [General Discovery procedure, finding Limited Discoverable device]** 

- Test Purpose 

Verify that the IUT can perform the General Discovery procedure and can find devices in the Limited Discoverable mode. 

The IUT is operating in the Central role. 

- Reference 

[4] 9.2.6 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(gen_disc_scan_min) for the IUT is specified in the TSPX_Tgap_gen_disc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Limited Discoverable mode. 

   2. The Upper Tester orders the IUT to start the General Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **177 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [335 x 161] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Limited  General<br>Discoverable Mode Discovery Procedure<br>Advertising Event<br>Discovered Device<br>TGAP(gen_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.107: GAP/DISC/GENP/BV-02-C [General Discovery procedure finding Limited Discoverable device] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT lists the Lower Tester during the discovery period. 

## **GAP/DISC/GENP/BV-03-C [General Discovery procedure does not find Broadcast device]** 

- Test Purpose 

Verify that the IUT can perform the General Discovery procedure and does not find a device in the Broadcast mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.2.6 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(gen_disc_scan_min) for the IUT is specified in the TSPX_Tgap_gen_disc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Broadcast mode. 

   2. The Upper Tester orders the IUT to perform the General Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **178 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [333 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General<br>Broadcast Mode<br>Discovery Procedure<br>Advertising Event<br>TGAP(gen_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.108: GAP/DISC/GENP/BV-03-C [General Discovery procedure does not find Broadcast device] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT does not discover the Lower Tester during the discovery period. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

**GAP/DISC/GENP/BV-04-C [General Discovery procedure does not find Undirected Connectable device]** 

- Test Purpose 

Verify that the IUT can perform the General Discovery procedure and does not find a device in the Undirected Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.2.6 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(gen_disc_scan_min) for the IUT is specified in the TSPX_Tgap_gendisc_scan_min IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Undirected Connectable mode; the Lower Tester does not include the Flags AD Type in the advertising data with either the General Discoverable Flag or Limited Discoverable Flag set to 1. 

   2. The Upper Tester orders the IUT to perform the General Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **179 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [340 x 161] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General<br>Broadcast Mode<br>Discovery Procedure<br>Advertising Event<br>TGAP(gen_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.109: GAP/DISC/GENP/BV-04-C [General Discovery procedure does not find Undirected Connectable device] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT does not discover the Lower Tester during the discovery period. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

**GAP/DISC/GENP/BV-05-C [General Discovery procedure does not find Directed Connectable device]** 

- Test Purpose 

Verify that the IUT can perform the General Discovery procedure and does not find a device in the Directed Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.2.6 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - TGAP(gen_disc_scan_min) for the IUT is specified in the TSPX_Tgap_gen_disc_scan_min IXIT value. 

   - The initiator address for the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Lower Tester enters Directed Connectable mode using the specified initiator address for the IUT. 

   2. The Upper Tester orders the IUT to perform the General Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **180 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [333 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General<br>Broadcast Mode<br>Discovery Procedure<br>Advertising Event<br>TGAP(gen_disc_scan_min)<br>List of device<br>address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.110: GAP/DISC/GENP/BV-05-C [General Discovery procedure does not find Directed Connectable device] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT does not discover the Lower Tester during the discovery period. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

## **4.7.2.6 Name Discovery procedure** 

## **GAP/IDLE/NAMP/BV-01-C [Name Discovery procedure, GATT Client]** 

- Test Purpose 

Verify that the IUT can perform the Name Discovery procedure and retrieve the device name from a peer device. 

The IUT is operating as the GATT client. 

- Reference 

   - [4] 9.2.7 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in the role specified in the TSPX_gap_iut_role IXIT entry. 

   - The Lower Tester and IUT are connected. 

   - The Lower Tester is a GATT server and exposes the Device Name characteristic. 

   - The Device Name Characteristic value for the Lower Tester is specified in the TSPX_device_name IXIT value. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **181 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

The Upper Tester orders the IUT to perform the Name Discovery procedure. 

**==> picture [305 x 109] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Start Name Discovery Procedure<br>Name Request<br>Name Response<br>**----- End of picture text -----**<br>


_Figure 4.111: GAP/IDLE/NAMP/BV-01-C [Name Discovery procedure, GATT Client] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT retrieves the specified Device Name from the Lower Tester. 

## **GAP/IDLE/NAMP/BV-02-C [Name Discovery procedure, GATT Server]** 

- Test Purpose 

Verify that the IUT can support the Name Discovery procedure and allow a peer device to retrieve the device name. 

The IUT is operating as the GATT Server. 

- Reference 

[4] 9.2.7 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in the role specified in the TSPX_gap_iut_role IXIT entry. 

   - The Lower Tester and IUT are connected. 

   - The IUT is a GATT server and exposes the Device Name characteristic. 

   - The Device Name Characteristic value for the IUT is specified in the TSPX_device_name IXIT value. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **182 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

The Lower Tester performs the Name Discovery procedure. 

**==> picture [306 x 109] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Name Discovery<br>Procedure<br>Name Request<br>Name Response<br>**----- End of picture text -----**<br>


_Figure 4.112: GAP/IDLE/NAMP/BV-02-C [Name Discovery procedure, GATT Server] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester retrieves the specified Device Name from the IUT. 

## **4.7.2.7 Discovery of devices with Resolvable Private Address** 

**GAP/DISC/RPA/BV-01-C [Discovery procedure, find discoverable device using Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT can perform any of the Discovery procedures to find a device in any of the Discoverable modes, when resolvable private addresses are used. 

The IUT is operating in the Central role. 

- Reference 

[9] 9.2.5, 10.7, 10.7.2.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections. 

   - The Lower Tester and the IUT have exchanged bonding information for resolving. 

- Test Procedure 

   1. The Lower Tester generates a resolvable private address using the Resolvable Private Address Generation procedure. 

   2. The Lower Tester enters Limited Discoverable mode or General Discoverable mode. 

   3. The Upper Tester orders the IUT to add the Lower Tester’s Identity to the resolving list. 

   4. The Upper Tester orders the IUT to perform the Limited Discovery procedure or the General Discovery procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **183 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 167] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Add Lower Tester Device<br>Identity to Resolving List<br>Limited or General  Limited or General<br>Discoverable Mode Discovery Procedure<br>Advertising Event<br>Discovered Device<br>TGAP(lim_disc_scan_min)<br>or<br>TGAP(gen_disc_scan_min)<br>List of resolved<br>device address and<br>advertising data<br>**----- End of picture text -----**<br>


_Figure 4.113: GAP/DISC/RPA/BV-01-C [Discovery procedure, find discoverable device using Resolvable Private Address] MSC_ 

- Expected Outcome 

Pass verdict 

The IUT lists the Lower Tester during the discovery period by its identity address. 

## **4.7.3 Connection modes and procedures** 

## **4.7.3.1 Non-Connectable mode** 

## **GAP/CONN/NCON/BV-01-C [Non-Connectable mode]** 

- Test Purpose 

Verify that the IUT in the Non-Connectable mode does not allow another device performing the Direct Connection Establishment procedure to connect. 

The IUT is operating in the Broadcaster role or the Peripheral role or the Observer role. 

- Reference 

   - [4] 9.3.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address for the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders IUT to enter Non-Connectable mode. 

   2. The Lower Tester performs the Direct Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the specified public/static address for the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **184 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [336 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Direct Connection<br>Establishment<br>Procedure Non-Connectable Mode<br>OPTIONAL Advertising Event<br>Connect Req<br>Connection<br>attempt is not<br>successful<br>**----- End of picture text -----**<br>


_Figure 4.114: GAP/CONN/NCON/BV-01-C [Non-Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either no advertising events or non-connectable advertising events from IUT whilst in Non-Connectable mode. 

For IUT acting in the Broadcaster role, the Lower Tester receives non-connectable advertising events from IUT whilst broadcasting data in Non-Connectable mode. 

In each advertising event received the advertiser address is set to the specified public/static address for the IUT. 

The Lower Tester fails to establish a connection with the IUT. 

## **GAP/CONN/NCON/BV-02-C [Non-Connectable mode, General Discoverable mode]** 

- Test Purpose 

Verify that the IUT in the Non-Connectable mode and General Discoverable mode does not allow a connection to be established with another device. 

The IUT is operating in the Peripheral role. 

- Reference 

[4] 9.3.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter General Discoverable mode. 

   2. The Upper Tester orders the IUT to enter Non-Connectable mode. 

   3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the specified public/static address. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **185 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection<br>Establishment  Non-Connectable Mode and General<br>Procedure Discoverable Mode<br>Advertising Event<br>Connect Req Connection<br>attempt is not<br>successful<br>**----- End of picture text -----**<br>


_Figure 4.115: GAP/CONN/NCON/BV-02-C [Non-Connectable mode, General Discoverable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events from IUT whilst in Non-Connectable mode and General Discoverable mode. 

In each advertising event received the advertiser address is set to the specified public/static address for the IUT. 

The Lower Tester fails to establish a connection with the IUT. 

## **GAP/CONN/NCON/BV-03-C [Non-Connectable mode, Limited Discoverable mode]** 

- Test Purpose 

Verify that the IUT in the Non-Connectable mode and Limited Discoverable mode does not allow a connection to be established with another device. 

The IUT is operating in the Peripheral role. 

- Reference 

[4] 9.3.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter Limited Discoverable mode. 

   2. The Upper Tester orders the IUT to enter Non-Connectable mode. 

   3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the specified public/static address for the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **186 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection<br>Establishment  Non-Connectable Mode and Limited<br>Procedure Discoverable Mode<br>Advertising Event<br>Connect Req Connection<br>attempt is not<br>successful<br>**----- End of picture text -----**<br>


_Figure 4.116: GAP/CONN/NCON/BV-03-C [Non-Connectable mode, Limited Discoverable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives non-connectable advertising events from the IUT while in NonConnectable mode and Limited Discoverable mode. 

In each advertising event received the advertiser address is set to the specified public/static address for the IUT. 

The Lower Tester fails to establish a connection with the IUT. 

## **4.7.3.2 Directed Connectable mode** 

## **GAP/CONN/DCON/BV-01-C [Directed Connectable mode]** 

- Test Purpose 

Verify that the IUT in the Directed Connectable mode can connect with another device performing the General Connection Establishment procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.3.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received advertiser address. 

   2. The Upper Tester orders IUT to enter Direct Connectable mode; the IUT sets the advertiser’s address to the public/static address of the IUT and sets the initiator address to the public/static address of the Lower Tester. 

   3. The Lower Tester or the IUT terminates the connection. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **187 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection<br>Establishment<br>Procedure Direct Connectable Mode<br>Advertising Event<br>Connect Req<br>**----- End of picture text -----**<br>


_Figure 4.117: GAP/CONN/DCON/BV-01-C [Directed Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives connectable directed advertising events from IUT during the period that the IUT is in Directed Connectable mode. 

In each connectable directed advertising event received the advertiser address is set to the public/static address of the IUT and the initiator address is set to the public/static address of the Lower Tester. 

The Lower Tester establishes a connection with the IUT using the received advertiser address. 

The Lower Tester or IUT successfully terminates the connection. 

**GAP/CONN/DCON/BV-04-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution]** 

- Test Purpose 

Verify that the IUT in the Directed Connectable mode using a Resolvable Private Address can connect with another device using a Resolvable Private Address performing the General Connection Establishment procedure when the other device indicates support for Central Address Resolution. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [9] 9.3.3, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Privacy mode. 

   - The Lower Tester exposes the Central Address Resolution characteristic which is set to 1. 

   - TGAP(private_addr_int) for the IUT is specified in the TSPX_iut_private_address_interval IXIT value. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **188 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Tester’s Device Identity to the resolving list. 

   2. The Upper Tester orders the IUT to enter General Connectable mode. 

   3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received advertiser address. 

   4. When connected, the IUT optionally reads the value of the Central Address Resolution characteristic. 

   5. The Lower Tester or the IUT terminates the connection. 

   6. The Upper Tester orders the IUT to enter Direct Connectable mode targeting the Lower Tester by its identity address. 

   7. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; upon receiving the directed advertisement, the Lower Tester resolves the initiator and advertiser address, and set the advertiser address equivalent to the resolved advertiser address when creating the connection to the IUT. 

   8. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

**==> picture [306 x 275] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection  Add Lower Tester s identity to resolving list<br>Establishment<br>Procedure General Connectable Mode<br>Advertising Event<br>Connection Established<br>Optional Read Central Address Resolution<br>Terminate  Terminate Connection<br>Connection<br>Connection Terminated<br>General Connection<br>Establishment<br>Procedure<br>Advertising Event<br>Connection Established<br>Terminate  Terminate Connection<br>Connection<br>Connection Terminated<br>**----- End of picture text -----**<br>


_Figure 4.118: GAP/CONN/DCON/BV-04-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution] MSC_ 

- Expected Outcome 

## Pass verdict 

In each connectable directed advertising event received by the Lower Tester, the advertiser address is set to a resolvable private address for the IUT and the initiator address is set to a generated resolvable private address based on the device identity of the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **189 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

The Lower Tester establishes a connection with the IUT using a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request. 

**GAP/CONN/DCON/BV-05-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution not supported]** 

- Test Purpose 

Verify that the IUT does not initiate the Directed Connectable mode using a Resolvable Private Address, towards another privacy enabled device, which does not indicate support for Central Address Resolution. 

The IUT is operating in the Peripheral role. 

- Reference 

[9] 9.3.3, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT is in Privacy mode. 

   - The Lower Tester may expose the Central Address Resolution characteristic. If present it is set to 0. 

   - TGAP(private_addr_int) for the IUT is specified in the TSPX_iut_private_address_interval IXIT value. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list. 

   2. The Upper Tester orders the IUT to enter General Connectable mode. 

   3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received advertiser address. 

   4. When connected, the IUT optionally reads the value of the Central Address Resolution characteristic of the Lower Tester. 

   5. The Lower Tester or the IUT terminates the connection. 

   6. The Upper Tester orders the IUT to enter Direct Connectable mode targeting the Lower Tester by its identity address. 

   7. The IUT refuses the order. The IUT might enter another connectable mode and establish the connection this way. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **190 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [306 x 261] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection  Add Lower Tester s identity to resolving list<br>Establishment<br>Procedure General Connectable Mode<br>Advertising Event<br>Connection Established<br>Optional Read Central Address Resolution<br>Terminate  Terminate Connection<br>Connection<br>Connection Terminated<br>General Connection<br>Establishment<br>Procedure<br>Advertising Event<br>Connection Established<br>Terminate  Terminate Connection<br>Connection<br>Connection Terminated<br>**----- End of picture text -----**<br>


_Figure 4.119: GAP/CONN/DCON/BV-05-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution not supported] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester does not establish a connection with the IUT based on directed advertisement. 

## **4.7.3.3 Undirected Connectable mode** 

## **GAP/CONN/UCON/BV-01-C [Undirected Connectable mode, Non-Discoverable mode]** 

- Test Purpose 

Verify that the IUT in Undirected Connectable mode can connect with another device performing the General Connection Establishment procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [4] 9.3.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the advertiser’s address in the received advertising events from the IUT. 

   2. The Upper Tester orders IUT to enter Undirected Connectable mode and Non-Discoverable mode; the IUT sets the advertiser address to the public/static address of the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **191 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection<br>Establishment  Undirected Connectable Mode and Non-<br>Procedure Discoverable Mode<br>Advertising Event<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.120: GAP/CONN/UCON/BV-01-C [Undirected Connectable mode, Non-Discoverable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT sends either connectable and scannable undirected advertising events or connectable undirected advertising events. 

In each advertising event received the advertiser address is set to the specified public/static address for the IUT. 

The Lower Tester establishes a connection with IUT. 

## **GAP/CONN/UCON/BV-02-C [Undirected Connectable mode, General Discoverable mode]** 

- Test Purpose 

Verify that the IUT in Undirected Connectable mode and General Discoverable mode can connect with another device performing the General Connection Establishment procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

[4] 9.3.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’ 

   - The public/static address for the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders IUT to enter Undirected Connectable mode and General Discoverable mode; the IUT sets the advertiser address to the specified public/static address for the IUT. 

   2. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **192 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 120] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection<br>Establishment  Undirected Connectable and General<br>Procedure Discoverable Mode<br>Advertising Event<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.121: GAP/CONN/UCON/BV-02-C [Undirected Connectable mode, General Discoverable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT sends either connectable and scannable undirected advertising events or connectable undirected advertising events. 

In each advertising event received the advertiser address is set to the specified public/static address for the IUT. 

The Lower Tester establishes a connection with IUT. 

## **GAP/CONN/UCON/BV-03-C [Undirected Connectable mode, Limited Discoverable mode]** 

- Test Purpose 

Verify that the IUT in Undirected Connectable mode and Limited Discoverable mode can connect with another device performing the General Connection Establishment procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

[4] 9.3.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address for the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter Limited Discoverable mode and Undirected Connectable mode; the IUT sets the advertiser address to the public/static address for the IUT. 

   2. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **193 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection<br>Establishment  Undirected Connectable and Limited<br>Procedure Discoverable Mode<br>Advertising Event<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.122: GAP/CONN/UCON/BV-03-C [Undirected Connectable mode, Limited Discoverable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT sends either connectable and scannable undirected advertising events or connectable undirected advertising events. 

In each advertising event received the advertiser address is set to the specified public/static address for the IUT. 

The Lower Tester establishes a connection with IUT. 

## **GAP/CONN/UCON/BV-06-C [Undirected Connectable mode, Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT in the Undirected Connectable mode using Resolvable Private Address can connect with another device performing the General Connection Establishment procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [6], [9] 9.3.4, 10.7.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections. 

   - The IUT is in Privacy mode. 

   - TGAP(private_addr_int) for the IUT is specified in the TSPX_iut_private_address_interval IXIT value. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter Undirected Connectable mode using private addresses. 

   2. If the IUT is a Peripheral with Host-based privacy, then the IUT changes the advertiser address to a new and unique resolvable address every TGAP(private_addr_int). The Lower Tester verifies that the resolvable private address changes at least once after TGAP(private_addr_int). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **194 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received resolvable private address from the IUT. 

   4. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT. 

In each advertising event received, the advertiser address is set to a valid resolvable private address. 

The Lower Tester is able to resolve and confirm the identity of the IUT from the received private address. 

When the IUT is a Peripheral with Host-based privacy, the Lower Tester verifies that the IUT changes the resolvable private address in the advertiser address of the received advertising events after TGAP(private_addr_int). 

The Lower Tester establishes a connection with the IUT using the received advertiser address. 

## **4.7.3.4 Auto Connection Establishment procedure** 

**GAP/CONN/ACEP/BV-01-C [Auto Connection Establishment procedure, Directed Connectable mode]** 

- Test Purpose 

Verify that the IUT can perform the Auto Connection Establishment procedure to connect to another device in the Directed Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

[4] 9.3.5 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders IUT to perform the Auto Connection Establishment procedure using the specified public/static address of the Lower Tester. 

   2. The Lower Tester sets the advertiser address to the specified public/static address of the Lower Tester. 

   3. The Lower Tester sets the initiator address to the specified public/static address of the IUT. 

   4. The Lower Tester enters the Directed Connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **195 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Directed Connectable  Auto Connection Establishment Procedure<br>Mode<br>Advertising Event<br>Connect Req<br>Connect Resp<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.123: GAP/CONN/ACEP/BV-01-C [Auto Connection Establishment procedure, Directed Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT autonomously establishes a connection with the Lower Tester. 

**GAP/CONN/ACEP/BV-03-C [Auto Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]** 

- Test Purpose 

Verify that the IUT using Resolvable Private Address can perform the Auto Connection Establishment procedure to connect to another device in the Directed Connectable mode that is using Resolvable Private Addresses. 

The IUT is operating in the Central role. 

- Reference 

[9] 9.3.5, 10.7.2.1, 10.7.2.2, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT exposes the Central Address Resolution Characteristic set to 1. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Tester’s Device Identity to the resolving list and Filter Accept List. 

   2. The Upper Tester orders the IUT to perform the Auto Connection Establishment procedure using resolvable private address. 

   3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester. 

   4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester. 

   5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **196 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [299 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Add Lower Tester Identity to resolving list<br>Directed Connectable  Add Lower Tester Identity to filter accept list<br>Mode<br>Auto Connection Establishment Procedure<br>Advertising Event<br>Resolve<br>Addresses<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.124: GAP/CONN/ACEP/BV-03-C [Auto Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT uses a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request. 

The IUT autonomously establishes a connection with the Lower Tester. 

**GAP/CONN/ACEP/BV-04-C [Auto Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT using Resolvable Private Address can perform the Auto Connection Establishment procedure to connect to another device in the Undirected Connectable mode using Resolvable Private Address. 

The IUT is operating in the Central role. 

- Reference 

[9] 9.3.5, 10.7.2.1, 10.7.2.2, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list and Filter Accept List. 

   2. The Upper Tester orders the IUT to perform the Auto Connection Establishment procedure using resolvable private address. 

   3. The Lower Tester enters the Undirected Connectable mode using the device identity for the Lower Tester. 

   4. Upon receiving the undirected advertisement, the IUT resolves the address and sends a connect request to the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **197 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

**==> picture [302 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Add Lower Tester Identity to resolving list<br>Undirected  Add Lower Tester Identity to filter accept list<br>Connectable Mode<br>Auto Connection Establishment Procedure<br>Advertising Event<br>Resolve<br>Address<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.125: GAP/CONN/ACEP/BV-04-C [Auto Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT uses a resolvable private address as the initiator address and advertiser address present in the undirected advertisement in the connection request. 

The IUT autonomously establishes a connection with the Lower Tester. 

## **4.7.3.5 General Connection Establishment procedure** 

**GAP/CONN/GCEP/BV-01-C [General Connection Establishment procedure, Directed Connectable mode]** 

- Test Purpose 

Verify that the IUT can perform the General Connection Establishment procedure to connect to another device in the Directed Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.3.6 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the General Connection Establishment procedure; the IUT uses the specified public/static address of the Lower Tester. 

   2. The Lower Tester sets the advertiser address to the public/static address of the Lower Tester. 

   3. The Lower Tester sets the initiator address to the public/static address of the IUT. 

   4. The Lower Tester enters the Directed Connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **198 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [301 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Directed Connectable  General Connection Establishment Procedure<br>Mode<br>Advertising Event<br>Connect Req<br>Connect Resp<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.126: GAP/CONN/GCEP/BV-01-C [General Connection Establishment procedure Directed Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the connectable directed advertising events from the Lower Tester. 

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN_REQ is a nonresolvable private address. 

If the IUT has privacy enabled then the address used in the connection request is a non-resolvable private address. 

The IUT establishes a connection with the Lower Tester. 

**GAP/CONN/GCEP/BV-02-C [General Connection Establishment procedure, Undirected Connectable mode]** 

- Test Purpose 

Verify that the IUT can perform the General Connection Establishment procedure to connect to another device in the Undirected Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

[4] 9.3.6 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the General Connection Establishment procedure; the IUT uses the specified public/static address of the Lower Tester. 

   2. The Lower Tester sets the advertiser address to the public/static address of the Lower Tester. 

   3. The Lower Tester enters the Undirected Connectable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **199 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [301 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Undirected<br>Connectable Mode<br>General Connection Establishment Procedure<br>Advertising Event<br>Connect Req<br>Connect Resp<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.127: GAP/CONN/GCEP/BV-02-C [General Connection Establishment procedure Undirected Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the connectable and scannable undirected advertising events or connectable undirected advertising events from the Lower Tester. 

The IUT establishes a connection with the Lower Tester. 

**GAP/CONN/GCEP/BV-05-C [General Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]** 

- Test Purpose 

Verify that the IUT using a Resolvable Private Address can perform the General Connection Establishment procedure to connect to another device in the Directed Connectable mode using Resolvable Private Address. 

The IUT is operating in the Central role. 

- Reference 

[9] 9.3.6. 10.7.2.1, 10.7.2.2, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT exposes the Central Address Resolution Characteristic set to 1. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list. 

   2. The Upper Tester orders the IUT to perform the General Connection Establishment procedure using resolvable private address. 

   3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **200 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester. 

5. After the connection establishment, either the Lower Tester or the IUT should terminate the 

   - connection. 

**==> picture [304 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Add Lower Tester Identity to resolving list<br>Directed Connectable<br>Mode General Connection Establishment Procedure<br>Advertising Event<br>Resolve<br>Addresses<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.128: GAP/CONN/GCEP/BV-05-C [General Connection Establishment procedure Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC_ 

- Expected Outcome 

Pass verdict 

The IUT receives the connectable directed advertising events from the Lower Tester. 

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address. 

The IUT uses a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request. 

The IUT establishes a connection with the Lower Tester. 

**GAP/CONN/GCEP/BV-06-C [General Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT using Resolvable Private Address can perform the General Connection Establishment procedure to connect to another device in the Undirected Connectable mode using Resolvable Private Address. 

The IUT is operating in the Central role. 

- Reference 

[9] 9.3.6, 10.7.2.1, 10.7.2.2, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **201 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Tester’s Identity to the resolving list. 

   2. The Upper Tester orders the IUT to perform the General Connection Establishment procedure using resolvable private address. 

   3. The Lower Tester enters the Undirected Connectable mode using the device identity for the Lower Tester. 

   4. Upon receiving the undirected advertisement, the IUT resolves the address and sends a connect request to the Lower Tester. 

   5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

**==> picture [304 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Add Lower Tester Identity to resolving list<br>Undirected<br>Connectable Mode General Connection Establishment Procedure<br>Advertising Event<br>Resolve<br>Address<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.129: GAP/CONN/GCEP/BV-06-C [General Connection Establishment procedure Undirected Connectable mode, Resolvable Private Address] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the connectable and scannable undirected advertising events or connectable undirected advertising events from the Lower Tester. 

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address. 

The IUT uses a resolvable private address as the initiator address and advertiser address present in the undirected advertisement in the connection request. 

The IUT establishes a connection with the Lower Tester. 

## **4.7.3.6 Selective Connection Establishment procedure** 

**GAP/CONN/SCEP/BV-01-C [Selective Connection Establishment procedure, Directed Connectable mode]** 

- Test Purpose 

Verify that the IUT can perform the Selective Connection Establishment procedure to connect to another device in the Directed Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.3.7 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **202 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The public/static address of the IUT is specified in the TSPX_bd_addr_iut IXIT value. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Selective Connection Establishment procedure using the specified public/static address of the Lower Tester. 

   2. The Lower Tester sets the advertiser address to the specified public/static address of the Lower Tester. 

   3. The Lower Tester sets the initiator address to the specified public/static address of the IUT. 

   4. The Lower Tester enters the Directed Connectable mode. 

**==> picture [305 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Directed Connectable<br>Mode Selective Connection Establishment<br>Procedure<br>Advertising Event<br>Connect Req<br>Connect Resp<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.130: GAP/CONN/SCEP/BV-01-C [Selective Connection Establishment procedure, Directed Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT host receives advertising event reports sent from the Lower Tester and any other devices in the Filter Accept List; the IUT does not receive advertising event reports from any other devices. 

The IUT establishes a connection with the Lower Tester. 

**GAP/CONN/SCEP/BV-03-C [Selective Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]** 

- Test Purpose 

Verify that the IUT using a Resolvable Private Address can perform the Selective Connection Establishment procedure to connect to another device in the Directed Connectable mode using Resolvable Private Address. 

The IUT is operating in the Central role. 

- Reference 

[9] 9.3.7, 10.7.2.1, 10.7.2.2, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT exposes the Central Address Resolution Characteristic set to 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **203 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Tester’s Device Identity to the resolving list and Filter Accept List. 

   2. The Upper Tester orders the IUT to perform the Selective Connection Establishment procedure using the device identity of the Lower Tester. 

   3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester. 

   4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester. 

   5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

**==> picture [301 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Add Lower Tester Identity to resolving list<br>Add Lower Tester Identity to filter accept list<br>Directed Connectable<br>Mode Selective Connection Establishment<br>Procedure<br>Advertising Event<br>Resolve<br>Addresses<br>Connect Req<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.131: GAP/CONN/SCEP/BV-03-C [Selective Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC_ 

- Expected Outcome 

Pass verdict 

The IUT’s advertising reports includes the Lower Tester. 

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address. 

The IUT uses a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request. 

The IUT establishes a connection with the Lower Tester. 

## **4.7.3.7 Direct Connection Establishment procedure** 

**GAP/CONN/DCEP/BV-01-C [Direct Connection Establishment procedure, Directed Connectable mode]** 

- Test Purpose 

Verify that the IUT can perform the Direct Connection Establishment procedure to connect to another device in the Directed Connectable mode. 

The IUT is operating in the Central role. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **204 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference 

[4] 9.3.8 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT has the address of the peer device. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Direct Connection Establishment procedure using the static address, public address or non-resolvable private address of the Lower Tester. 

   2. The Lower Tester sets the advertiser address to the static address, public address or nonresolvable private address of the Lower Tester. 

   3. The Lower Tester sets the initiator address to the static address, public address or non-resolvable private address of the IUT. 

   4. The Lower Tester enters the Directed Connectable mode. 

**==> picture [105 x 51] intentionally omitted <==**

_Figure 4.132: GAP/CONN/DCEP/BV-01-C [Direct Connection Establishment procedure, Directed Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT has privacy enabled then the address used in the connection request is a static address, public address, non-resolvable private address, or resolvable private address. 

The IUT establishes a connection with the Lower Tester. 

**GAP/CONN/DCEP/BV-03-C [Direct Connection Establishment procedure, Undirected Connectable mode]** 

- Test Purpose 

Verify that the IUT can perform the Direct Connection Establishment procedure to connect to another device in the Undirected Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

   - [4] 9.3.8 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **205 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester orders IUT to perform the Direct Connection Establishment procedure using the static address, public address, non-resolvable private address, or resolvable private address of the Lower Tester. 

   2. The Lower Tester sets the advertiser address to the static address, public address, nonresolvable private address, resolvable private address of the Lower Tester. 

   3. The Lower Tester sets the initiator address to the static address, public address or non-resolvable private address of the IUT. 

   4. The Lower Tester enters the Undirected Connectable mode. 

**==> picture [304 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Undirected<br>Connectable Mode<br>Direct Connection Establishment Procedure<br>Advertising Event<br>Connect Req<br>Connect Resp<br>Connection Established<br>**----- End of picture text -----**<br>


_Figure 4.133: GAP/CONN/DCEP/BV-03-C [Direct Connection Establishment procedure, Undirected Connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT has privacy enabled then the address used in the connection request is a static address, public address, non-resolvable private address, or resolvable private address. 

The IUT establishes a connection with the Lower Tester. 

**GAP/CONN/DCEP/BV-05-C [Direct Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]** 

- Test Purpose 

Verify that the IUT using Resolvable Private Address can perform the Direct Connection Establishment procedure to connect to another device in the Directed Connectable mode that is using a Resolvable Private Address. 

The IUT is operating in the Central role. 

- Reference 

[9] 9.3.8, 10.7.2.1, 10.7.2.2, 12.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT exposes the Central Address Resolution Characteristic set to 1. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **206 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list. 

   2. The Upper Tester orders the IUT to perform the Direct Connection Establishment procedure using resolvable private address. 

   3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester. 

   4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester. 

   5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

**==> picture [104 x 50] intentionally omitted <==**

**==> picture [189 x 59] intentionally omitted <==**

_Figure 4.134: GAP/CONN/DCEP/BV-05-C [Direct Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the connectable directed advertising events from the Lower Tester. 

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address. 

The IUT uses the advertiser address present in the directed advertisement as the advertiser address and a resolvable private address as the initiator address in the connection request. 

The IUT establishes a connection with the Lower Tester. 

**GAP/CONN/DCEP/BV-06-C [Direct Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address]** 

- Test Purpose 

Verify that the IUT using Resolvable Private Address can perform the Direct Connection Establishment procedure to connect to another device in the Undirected Connectable mode that is using Resolvable Private Address. 

The IUT is operating in the Central role. 

- Reference 

   - [9] 9.3.8, 10.7.2.1, 10.7.2.2 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **207 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The Lower Tester is using a resolvable private address and has distributed its IRK. 

   - The IUT is using a resolvable private address and has distributed its IRK. 

- Test Procedure 

   1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list. 

   2. The Upper Tester orders the IUT to perform the Direct Connection Establishment procedure using resolvable private address. 

   3. The Lower Tester enters the Undirected Connectable mode using the device identities for the Lower Tester. 

   4. Upon receiving the undirected advertisement, the IUT resolves the address and sends a connect request to the Lower Tester. 

   5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection. 

**==> picture [105 x 50] intentionally omitted <==**

**==> picture [189 x 59] intentionally omitted <==**

_Figure 4.135: GAP/CONN/DCEP/BV-06-C [Direct Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the connectable and scannable undirected advertising events or connectable undirected advertising events from the Lower Tester. 

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address. 

The IUT use a resolvable private address as the initiator address and advertiser address present in the undirected advertisement in the connection request. 

The IUT establishes a connection with the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **208 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.3.8 Connection Parameter Update procedure** 

**GAP/CONN/CPUP/BV-01-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over L2CAP]** 

- Test Purpose 

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device, using the L2CAP Connection Parameter Update Request procedure; the peer device accepts the updated connection parameters. 

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder. 

- Reference 

   - [4] 9.3.9 

- Initial Condition 

   - On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0. 

   - The IUT and the Lower Tester are connected. 

   - The valid connection update parameters for the IUT are specified in the following IXIT [3]: 

      - TSPX_conn_update_int_min 

      - TSPX_conn_update_int_max 

      - TSPX_conn_update_peripheral_latency 

      - TSPX_conn_update_supervision_timeout 

   - TGAP(conn_param_timeout) for the IUT is specified in the TSPX_Tgap_conn_param_timeout IXIT value. 

   - The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters. 

   2. The IUT executes the L2CAP Connection Parameter Update Request procedure. 

   3. The Lower Tester accepts the updated connection parameters and sends the appropriate L2CAP connection parameter update response within the specified TGAP(conn_param_timeout). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **209 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Peripheral<br>Initiate Connection<br>Parameter Update<br>Connection Parameter<br>Update Request<br>Connection Parameter<br>Update Response<br>TLE _ GAP (conn_param_timeout)<br>**----- End of picture text -----**<br>


_Figure 4.136: GAP/CONN/CPUP/BV-01-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over L2CAP] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT sends an L2CAP connection parameter update request command with the specified update connection parameters. 

The IUT host receives an indication from the IUT controller that the connection parameters have been updated. 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges. 

**GAP/CONN/CPUP/BV-02-C [Connection Parameter Update procedure, valid parameters, Timeout Peripheral Initiator]** 

- Test Purpose 

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device; the peer device fails to respond in a timely manner. 

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder. 

- Reference 

   - [4] 9.3.9 

- Initial Condition 

   - On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0. 

   - The IUT and the Lower Tester are connected. 

   - The valid connection update parameters for the Lower Tester are specified in the following IXIT [3]: 

      - TSPX_conn_update_int_min 

      - TSPX_conn_update_int_max 

      - TSPX_conn_update_peripheral_latency 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **210 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - RTX timer is set to maximum allowed initial value. 

   - The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters. 

   2. The Lower Tester does not send the appropriate L2CAP connection parameter update response within the specified RTX timeout. 

**==> picture [300 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Peripheral.<br>Initiate Connection<br>Parameter Update<br>Connection Parameter<br>Update Request<br>T GAP (conn_param_timeout)<br>**----- End of picture text -----**<br>


_Figure 4.137: GAP/CONN/CPUP/BV-02-C [Connection Parameter Update procedure, valid parameters, Timeout Peripheral Initiator] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT transmits a correctly formatted L2CAP Connection Parameter Update Request to the Lower Tester, containing valid connection update parameters matching those received from the Upper Tester. 

After RTX timer expires, the IUT either: 

   1. IUT resends the L2CAP Connection Parameter Update Request command. 

   2. IUT disconnects the connection at the Link Layer. 

   3. IUT ignores the error case and continues without disconnecting or resending. 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges but in this test case does not respond to the connection parameter update request sent by the IUT. 

**GAP/CONN/CPUP/BV-03-C [Connection Parameter Update procedure, invalid parameters, Peripheral Initiator]** 

- Test Purpose 

Verify that the IUT can perform the Connection Parameter Update procedure using invalid parameters for the peer device; the peer device rejects the updated connection parameters. 

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **211 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference 

[4] 9.3.9 

- Initial Condition 

   - On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0. 

   - The IUT and the Lower Tester are connected. 

   - The invalid connection update parameters for the Lower Tester are specified in the following IXIT [3]: 

      - TSPX_iut_invalid_connection_interval_min 

      - TSPX_iut_invalid_connection_interval_max 

      - TSPX_iut_invalid_connection_latency 

      - TSPX_iut_invalid_conn_update_supervision_timeout 

   - TGAP(conn_param_timeout) for the IUT is specified in the TSPX_Tgap_conn_param_timeout IXIT value. 

   - The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified invalid connection update parameters. 

   2. The Lower Tester rejects the updated connection parameters and sends the appropriate L2CAP connection parameter update response within the specified TGAP(conn_param_timeout). 

**==> picture [303 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Peripheral.<br>Initiate Connection<br>Parameter Update<br>Connection Parameter<br>Update Request<br>Connection Parameter<br>Update Response<br>TGAP(conn_param_timeout)<br>**----- End of picture text -----**<br>


_Figure 4.138: GAP/CONN/CPUP/BV-03-C [Connection Parameter Update procedure, invalid parameters, Peripheral Initiator] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives an L2CAP connection parameter update request command with the specified update connection parameters sent by the IUT. 

The IUT host does not receive an indication from the IUT controller that the connection parameters have been updated. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **212 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges but in this test case rejects the update connection parameters request sent by the IUT. 

**GAP/CONN/CPUP/BV-04-C [Connection Parameter Update procedure, valid parameters, Central Responder]** 

- Test Purpose 

Verify that the IUT accepts the connection parameter update request from a peer device performing the Connection Parameter Update procedure using valid parameters for the IUT. 

The Lower Tester is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the IUT is operating in the Central role and is the responder. 

- Reference 

## [4] 9.3.9 

- Initial Condition 

   - On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0. 

   - The IUT and the Lower Tester are connected. 

   - The valid connection update parameters for the IUT are specified in the following IXIT [3]: 

      - TSPX_conn_update_int_min 

      - TSPX_conn_update_int_max 

      - TSPX_conn_update_peripheral_latency 

      - TSPX_conn_update_supervision_timeout 

   - The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure. 

- Test Procedure 

The Lower Tester performs the Connection Parameter Update procedure using the specified valid connection update parameters. 

**==> picture [323 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Central.<br>Initiate Connection<br>Parameter Update<br>Connection Parameter<br>Update Request<br>Connection Parameter<br>TGAP(conn_param_timeout)  Update Response<br>**----- End of picture text -----**<br>


_Figure 4.139: GAP/CONN/CPUP/BV-04-C [Connection Parameter Update procedure, valid parameters, Central Responder] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **213 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives an L2CAP connection parameter update response within TGAP(conn_param_timeout) after sending the L2CAP connection parameter update request. 

The L2CAP connection parameter update response result code is set to “parameters accepted”. 

The IUT uses the new connection parameters after the Lower Tester receives the L2CAP connection parameter update response. 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges. 

**GAP/CONN/CPUP/BV-05-C [Connection Parameter Update procedure, invalid parameters, Central Responder]** 

- Test Purpose 

Verify that the IUT rejects the connection parameter update request from a peer device performing the Connection Parameter Update procedure using invalid connection parameters for the IUT. 

The Lower Tester is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure and the IUT is operating in the Central role and is the responder. 

- Reference 

   - [4] 9.3.9 

- Initial Condition 

   - On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0. 

   - The IUT and the Lower Tester are connected. 

   - The invalid connection update parameters for the IUT are specified in the following IXIT [3]: 

      - TSPX_iut_invalid_connection_interval_min 

      - TSPX_iut_invalid_connection_interval_max 

      - TSPX_iut_invalid_connection_latency 

      - TSPX_iut_invalid_conn_update_supervision_timeout 

   - The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **214 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

The Lower Tester performs the Connection Parameter Update procedure using the specified invalid connection update parameters. 

**==> picture [326 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Central.<br>Initiate Connection<br>Parameter Update<br>Connection Parameter<br>Update Request<br>Connection Parameter<br>TGAP(conn_param_timeout)  Update Response<br>**----- End of picture text -----**<br>


_Figure 4.140: GAP/CONN/CPUP/BV-05-C [Connection Parameter Update procedure, invalid parameters, Central Responder] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives an L2CAP connection parameter update response within TGAP(conn_param_timeout) after sending the L2CAP connection parameter update request. 

The L2CAP connection parameter update response result code is set to “request rejected”. 

The IUT continues to use the default connection parameters after the Lower Tester receives the L2CAP connection parameter update response. 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges. 

**GAP/CONN/CPUP/BV-06-C [Connection Parameter Update procedure, valid parameters, Central Initiator]** 

- Test Purpose 

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device; the peer device accepts the updated connection parameters. 

The IUT is operating in the Central role and is the initiator performing the Connection Parameter Update procedure and the Lower Tester is operating in the Peripheral role and is the responder. 

- Reference 

[4] 9.3.9 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **215 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0. 

   - The IUT and the Lower Tester are connected. 

   - The valid connection update parameters for the Lower Tester are specified in the following IXIT [3]: 

      - TSPX_conn_update_int_min 

      - TSPX_conn_update_int_max 

      - TSPX_conn_update_peripheral_latency 

      - TSPX_conn_update_supervision_timeout 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters. 

   2. The Lower Tester expects the IUT to initiate either the Link Layer Connection Update procedure or the Connection Parameters Request Link Layer control procedure. 

   3. The Lower Tester accepts the updated connection parameters and completes the Link Layer procedure initiated by the IUT. 

**==> picture [341 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Central.<br>Initiate Connection<br>LL Connection Update or  Parameter Update<br>Connection Parameters<br>Request Procedure<br>LSTO or<br>Procedure Response Timeout<br>**----- End of picture text -----**<br>


_Figure 4.141: GAP/CONN/CPUP/BV-06-C [Connection Parameter Update procedure, valid parameters, Central Initiator] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives the L2CAP connection parameter update response sent by the IUT in either the Link Layer Connection Update procedure or the Connection Parameters Request Link Layer control procedure. 

The IUT and the Lower Tester use the new parameters and the link is not dropped due to Link Supervision Timeout. 

- 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **216 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/CONN/CPUP/BV-08-C [Connection Parameter Update procedure, valid parameters, Peripheral Responder – LL Connection Parameters Request]** 

- Test Purpose 

Verify that the IUT accepts the connection parameter update request from a peer device performing the Connection Parameter Update procedure using valid parameters for the IUT when both the IUT and the peer device support the Link Layer Connection Parameters Request control procedure. 

The Lower Tester is operating in the Central role and is the initiator performing the Connection Parameter Update procedure; the IUT is operating in the Peripheral role and is the responder. 

- Reference 

[4] 9.3.9 

- Initial Condition 

   - The IUT and the Lower Tester are connected. 

   - The valid connection update parameters for the IUT are specified in the following IXIT [3]: 

      - TSPX_conn_update_int_min 

      - TSPX_conn_update_int_max 

      - TSPX_conn_update_peripheral_latency 

      - TSPX_conn_update_supervision_timeout 

- Test Procedure 

   1. The Lower Tester initiates the Connection Parameters Request Link Layer Control procedure, sending the specified valid connection update parameters to the IUT. 

   2. The Lower Tester expects the IUT to accept the connection update parameters. 

   3. The Lower Tester completes the Connection Parameters Request Link Layer Control procedure. 

   4. The Lower Tester expects the IUT to maintain the connection with the new parameters. 

**==> picture [323 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Peripheral.<br>Initiate Connection<br>Parameter Update<br>Initiate<br>Connection Parameters Request Link<br>Layer control procedure<br>Accept New Connection Parameters<br>Complete<br>Connection Parameters Request<br>Procedure Response Timeout Link Layer control procedure<br>**----- End of picture text -----**<br>


_Figure 4.142: GAP/CONN/CPUP/BV-08-C [Connection Parameter Update procedure, valid parameters, Peripheral Responder – LL Connection Parameters Request] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **217 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives a response from the IUT accepting the connection update parameters within procedure response timeout after initiating the Connection Parameters Request Link Layer Control procedure. 

The IUT uses the new connection parameters after the Link Layer Connection Parameters Request control procedure completes. 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges. 

**GAP/CONN/CPUP/BV-10-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over LL]** 

- Test Purpose 

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device, using the LL Connection Parameters Request procedure; the peer device accepts the updated connection parameters. 

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder. 

- Reference 

   - [4] 9.3.9 

- Initial Condition 

   - The IUT and the Lower Tester are connected. 

   - The valid connection update parameters for the IUT are specified in the following IXIT [3]: 

      - TSPX_conn_update_int_min 

      - TSPX_conn_update_int_max 

      - TSPX_conn_update_peripheral_latency 

      - TSPX_conn_update_supervision_timeout 

   - TGAP(conn_param_timeout) for the IUT is specified in the TSPX_Tgap_conn_param_timeout IXIT value. 

   - The Lower Tester has indicated that it supports the LL Connection Parameter Request procedure. 

- Test Procedure 

   1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters. 

   2. The IUT executes the LL Connection Parameters Request procedure. 

   3. The Lower Tester accepts the updated connection parameters and executes the LL Connection Parameter Update procedure within the specified TGAP(conn_param_timeout). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **218 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [307 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected.<br>IUT is Peripheral<br>Initiate Connection<br>Parameter Update<br>Connection Parameter<br>Update Request<br>Connection Parameter<br>Update Response<br>TLE _ GAP (conn_param_timeout)<br>**----- End of picture text -----**<br>


_Figure 4.143: GAP/CONN/CPUP/BV-10-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over LL] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT executes the LL Connection Parameters Request procedure and accepts the parameter update. 

The IUT host receives an indication from the IUT controller that the connection parameters have been updated. 

- Notes 

The Lower Tester should be capable of using any connection parameters within the valid ranges. 

## **4.7.3.9 Terminate Connection procedure** 

## **GAP/CONN/TERM/BV-01-C [Terminate Connection procedure]** 

- Test Purpose 

Verify that the IUT can perform the Terminate Connection procedure. 

The IUT is Central or Peripheral and the Lower Tester is Peripheral or Central, respectively. 

- Reference 

   - [4] 9.3.8 

- Initial Condition 

   - The IUT and the Lower Tester are connected. 

   - The IUT is the role as specified in the TSPX_gap_iut_role IXIT entry. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **219 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

The Upper Tester orders the IUT to perform the Terminate Connection procedure. 

**==> picture [301 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Start Terminate Connection<br>Procedure<br>Terminate Connection<br>IUT and Lower Tester are disconnected<br>**----- End of picture text -----**<br>


_Figure 4.144: GAP/CONN/TERM/BV-01-C [Terminate Connection procedure] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT performs the Link Layer Termination procedure and disconnects from the Lower Tester. 

## **4.7.3.10 Random Device Address** 

**GAP/CONN/PRDA/BV-01-C [Respond to Private Random Device Address after Bonding – Peripheral role]** 

- Test Purpose 

Verify that the IUT can properly respond to connections after bonding when Private Random Addresses are used by the Lower Tester. 

The IUT is the responder and is in the Peripheral role. 

The IUT supports security manager pairing and is in bondable mode. 

After the bonding has completed, authentication procedure is performed to assure that bonding information is stored properly and that Private Resolvable Addresses are accepted across connections. 

- Reference 

   - [4] 10.8 

- 

- Initial Condition 

- Physical link is established between the IUT and Lower Tester. Lower Tester uses a Resolvable Private Address as its Device Address. 

- After the connection is established, Lower Tester initiates pairing using either LE Legacy or LE Secure Connections with Bonding Flags set to “Bonding”. 

- The pairing procedure is completed successfully between Lower Tester and IUT. 

- The Lower Tester distributes its own IRK to the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **220 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Lower Tester disconnects the physical link with IUT. 

   2. The Lower Tester establishes connection with the IUT. The Lower Tester uses a new Resolvable Private Address as its own Device Address for the connection establishment procedure. The Lower Tester may continue to try to establish connection for 30 seconds. 

   3. The Lower Tester performs authentication procedure. 

   4. Repeat the test procedure twice with the Lower Tester generating new RPAs between each new connection. 

**==> picture [339 x 279] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded, IRK distributed<br>Lower Tester  Terminate Connection<br>uses a new<br>Resolvable<br>Private Address<br>as its own<br>Device Address<br>Connect Req<br>The Lower Tester may<br>continue to try to<br>establish connection<br>for 30 seconds<br>Connect Resp<br>Authentication procedure complete<br>**----- End of picture text -----**<br>


_Figure 4.145: GAP/CONN/PRDA/BV-01-C [Respond to Private Random Device Address after Bonding – Peripheral role] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT reconnects with the Lower Tester and authentication is successful. 

**GAP/CONN/PRDA/BV-02-C [Respond to Private Random Device Address after Bonding – Central role]** 

- Test Purpose 

Verify that the IUT can properly respond to connections after bonding when Private Random Addresses are used by the Lower Tester. 

The IUT is the initiator and is in Central role. 

The IUT supports security manager pairing and is in bondable mode. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **221 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

After the bonding has completed, authentication procedure is performed to assure that bonding information is stored properly and that Private Resolvable Addresses are accepted across connections. 

- Reference 

## [4] 10.8 

- 

## Initial Condition 

   - Physical link is established between IUT and Lower Tester. The Lower Tester uses a Resolvable Private Address as its Device Address. 

   - After the connection is established, the Lower Tester initiates security request with Bonding Flags set to “Bonding”. 

   - The IUT initiates pairing procedure using either LE Legacy or LE Secure Connections. 

   - The pairing procedure is completed successfully between the Lower Tester and IUT. 

   - The Lower Tester distributes its own IRK to the IUT. 

- Test Procedure 

   1. The Lower Tester disconnects the physical link with the IUT. 

   2. The IUT establishes connection with the Lower Tester; the Lower Tester uses a new Resolvable Private Address as part of the connection establishment procedure. 

   3. The Lower Tester performs the authentication procedure. 

   4. Repeat the test procedure twice with the Lower Tester generating new RPAs between each new connection. 

**==> picture [338 x 241] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded, IRK distributed<br>Terminate Connection<br>Lower Tester<br>uses a new<br>Resolvable<br>Private Address<br>Connect Req<br>Connect Resp<br>Authentication procedure complete<br>**----- End of picture text -----**<br>


_Figure 4.146: GAP/CONN/PRDA/BV-02-C [Respond to Private Random Device Address after Bonding – Central role] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **222 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

Pass verdict 

The IUT reconnects to a Lower Tester and authentication is successful. 

## **4.7.4 Bonding modes and procedures** 

## **4.7.4.1 Non-bondable mode** 

**GAP/BOND/NBON/BV-01-C [Non-bondable mode – Central as Responder]** 

- Test Purpose 

Verify that the IUT does not store bonding information after pairing while in non-bondable mode. 

The Lower Tester is the initiator. The Lower Tester sends security request to invoke the pairing procedure. 

The IUT supports security manager pairing but is in non-bondable mode. 

The pairing is performed as unauthenticated pairing (Just Works). 

The bonding is performed twice to make sure pairing is invoked both times. 

The IUT is the Central and the Lower Tester is the Peripheral. 

- Reference 

[4] 9.4.2 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - The IUT and the Lower Tester are not bonded before. 

- Test Procedure 

   1. After the connection is established, the Lower Tester initiates security request with Bonding_Flags set to “No Bonding”. 

   2. The IUT responses to security request with pairing procedure. 

   3. The pairing procedure is completed successfully between the Lower Tester and the IUT. 

   4. The Lower Tester disconnects the physical link with the IUT. 

   5. The IUT establishes connection with the Lower Tester again. 

   6. The Lower Tester re-initiates security request and verifies that the pairing procedure is invoked and completed successfully. 

- Expected Outcome 

## Pass verdict 

Pairing is successful each time. 

Authentication is invoked each time. 

**GAP/BOND/NBON/BV-02-C [Non-bondable mode – Central as Initiator]** 

- Test Purpose 

Verify that the IUT does not store bonding information after pairing while in non-bondable mode. 

The IUT is the initiator. The Upper Tester requests the authentication. 

The IUT initiates the pairing procedure with bonding flag = “no bonding”. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **223 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

The pairing is performed as unauthenticated pairing (Just Works). 

The bonding is performed twice to make sure pairing is invoked both times. 

The IUT is the Central and the Lower Tester is the Peripheral. 

- Reference 

   - [4] 9.4.2 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - The IUT and the Lower Tester are not bonded before. 

- Test Procedure 

   1. After the connection is established, Upper Tester requests authentication with Bonding_Flags set to “No Bonding”. 

   2. The IUT initiates the pairing procedure. 

   3. The pairing procedure is completed successfully between the Lower Tester and the IUT. 

   4. The Lower Tester disconnects the physical link with the IUT. 

   5. The IUT establishes a connection with the Lower Tester again. 

   6. The Upper Tester re-initiates authentication and the pairing procedure is invoked and completed successfully. 

**==> picture [336 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Request authentication<br>Pairing procedure is invoked<br>Terminate<br>connection<br>terminate connection<br>Initiate connection<br>connection request<br>IUT and Lower Tester are connected<br>Request authentication<br>Pairing procedure is invoked<br>**----- End of picture text -----**<br>


_Figure 4.147: GAP/BOND/NBON/BV-02-C [Non-bondable mode – Central as Initiator] MSC_ 

- Expected Outcome 

## Pass verdict 

Pairing is successful each time. 

Authentication is invoked each time. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **224 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/BOND/NBON/BV-03-C [Non-bondable mode – Peripheral as Responder]** 

- Test Purpose 

Verify that the IUT does not exchange bonding information after pairing while in non-bondable mode. 

The Lower Tester is the initiator. The Lower Tester requires authentication to invoke the pairing procedure. 

The IUT either does not support security manager pairing or supports security manager pairing, but is in non-bondable mode. 

The pairing is performed as unauthenticated pairing (Just Works). 

Both the initiator and the responder key distribution field are set to 0 and bonding flag is set to “no bonding”. 

The IUT is Peripheral. 

- Reference 

[4] 9.4.2 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - The IUT and the Lower Tester are not bonded before. 

- Test Procedure 

   1. After the connection is established, the Lower Tester initiates pairing with Bonding_Flags set to “No Bonding” and both “Initiator Key Distribution = 0” and “Responder Key Distribution = 0”. 

   2. There are two alternatives, depending on if the IUT supports security manager pairing. 

   3. Alternative 1 (The IUT supports security manager pairing): 

      - The IUT sends a pairing response with Bonding_Flags = “No Bonding” and both “Initiator Key Distribution = 0” and “Responder Key Distribution = 0”. 

      - The pairing procedure is completed successfully between the Lower Tester and the IUT. 

      - The Lower Tester disconnects the physical link with the IUT. 

   4. Alternative 2 (The IUT does not support security manager pairing): 

      - The IUT sends a Pairing Failed message with the error code “Pairing not supported”. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **225 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 281] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Request<br>authentication Pairing request  No bonding<br>Initiator Key Distribution = 0,<br>Responder Key Distribution = 0,<br>Alternative 1<br>Pairing response  No bonding<br>Initiator Key Distribution = 0,<br>Responder Key Distribution = 0<br>Pairing procedure completes and STK is generated<br>Link is encrypted<br>Terminate<br>connection<br>Link is disconnected<br>Alternative 1<br>Pairing Failed response  Pairing<br>not supported<br>**----- End of picture text -----**<br>


_Figure 4.148: GAP/BOND/NBON/BV-03-C [Non-bondable mode – Peripheral as Responder] MSC_ 

- Expected Outcome 

Pass verdict 

Alternative 1: 

- The pairing procedure is completed successfully with Bonding_Flags = “no bonding” and initiator/responder key distribution are set to 0. 

- The link is encrypted correctly with STK. 

Alternative 2: 

- The pairing procedure fails with “Pairing not supported”. 

## **4.7.4.2 Bondable mode** 

**GAP/BOND/BON/BV-01-C [Initiate bonding – Peripheral role]** 

- Test Purpose 

Verify that the IUT can properly initiate the bonding procedure and store bonding information after pairing while in bondable mode in the Peripheral role. 

The IUT is the initiator and is in the Peripheral role. 

The IUT supports security manager pairing and is in bondable mode. 

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing. 

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing. 

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **226 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference 

   - [4] 9.4.3, 9.4.4 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - The IUT and the Lower Tester are not bonded before. 

- Test Procedure 

   1. After the connection is established, the IUT initiates security request with Bonding_Flags set to “Bonding”. 

   2. The IUT initiates bonding by sending “security request” to the Lower Tester. 

   3. The pairing procedure is completed successfully between the Lower Tester and the IUT. 

   4. If the IUT supports LE security mode 1, then LTK is distributed from the IUT. 

   5. If the IUT supports the generation of resolvable private addresses and generates a resolvable private address for its local address, then it sends Identity Information with SMP, including a valid IRK. 

   6. If the IUT does not generate a resolvable private address for its own address and it sends Identity Information with SMP, then it sends an all-zero IRK. 

   7. If the IUT supports resolving resolvable private addresses, then it requests the Lower Tester to send its Identity Information with SMP. 

   8. If the IUT supports LE security mode 2, then CSRK is distributed. 

   9. The Lower Tester disconnects the physical link with the IUT. 

   10. The Lower Tester establishes a connection with the IUT again. 

   11. If the IUT supports security mode 1, then the Lower Tester starts the encryption procedure with the previously distributed LTK from the IUT. 

   12. If the IUT supports security mode 2, then the IUT sends signed data with the previously distributed CSRK. 

**==> picture [300 x 260] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Security Request (Bonding)<br>IUT and Lower Tester are connected<br>Pairing<br>Authenticated (LTK or CSRK distributed)<br>Update list of  Update list of<br>paired devices paired devices<br>Disconnect/Re-establish physical link<br>Start encryption If LE SM 1<br>Supported<br>Start data signing If LE SM 2<br>Supported<br>**----- End of picture text -----**<br>


_Figure 4.149: GAP/BOND/BON/BV-01-C [Initiate bonding – Peripheral role] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **227 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

If the IUT supports LE security mode 1, then encryption is done successfully. 

If the IUT supports LE security mode 2, then data signing is done successfully. 

**GAP/BOND/BON/BV-02-C [Initiate bonding – Central role]** 

- Test Purpose 

Verify that the IUT can properly initiate bonding procedure and store bonding information after pairing while in bondable mode in the Central role. 

The IUT is the initiator and is in the Central role. 

The IUT supports security manager pairing and is in bondable mode. 

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing. 

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing. 

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly. 

- Reference 

   - [4] 9.4.3, 9.4.4 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - The IUT and the Lower Tester are not bonded before. 

- Test Procedure 

   1. After the connection is established, the IUT initiates pairing with Bonding_Flags set to “Bonding”. 

   2. The pairing procedure is completed successfully between the Lower Tester and the IUT. 

   3. If the IUT supports LE security mode 1, then LTK is distributed from the Lower Tester. 

   4. If the IUT supports the generation of resolvable private addresses and generates a resolvable private address for its local address, then it sends Identity Information with SMP, including a valid IRK. 

   5. If the IUT does not generate a resolvable private address for its own address and it sends Identity Information with SMP, then it sends an all-zero IRK. 

   6. If the IUT supports resolving resolvable private addresses, then it requests the Lower Tester to send its Identity Information with SMP. 

   7. If the IUT supports LE security mode 2, then CSRK is distributed. 

   8. The Lower Tester disconnects the physical link with the IUT. 

   9. The Lower Tester establishes connection with the IUT again. 

   10. If the IUT supports security mode 1, then the IUT starts the encryption procedure with the previously distributed LTK from the Lower Tester. 

   11. If the IUT supports security mode 2, then the IUT sends signed data with the previously distributed CSRK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **228 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 264] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Initiate Bonding<br>Pairing(bonding)<br>Authenticated (LTK or CSRK distributed)<br>Update list of  Update list of<br>paired devices paired devices<br>Disconnect/Re-establish physical link<br>If LE SM 1<br>Start encryption<br>Supported<br>Start data signing If LE SM 2<br>Supported<br>**----- End of picture text -----**<br>


_Figure 4.150: GAP/BOND/BON/BV-02-C [Initiate bonding – Central role] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT supports LE security mode 1, then encryption is done successfully. 

If the IUT supports LE security mode 2, then data signing is done successfully. 

**GAP/BOND/BON/BV-03-C [Respond to bonding – Peripheral role]** 

- Test Purpose 

Verify that the IUT can properly respond to bonding and store bonding information after pairing while in bondable mode in the Peripheral role. 

The IUT is the responder and is in the Peripheral role. 

The IUT supports security manager pairing and is in bondable mode. 

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing. 

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing. 

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly. 

- Reference 

[4] 9.4.3, 9.4.4 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - The IUT and the Lower Tester are not bonded before. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **229 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. After the connection is established, the Lower Tester initiates pairing with Bonding_Flags set to “Bonding”. 

   2. The pairing procedure is completed successfully between the Lower Tester and the IUT. 

   3. If the IUT supports LE security mode 1, then the LTK is distributed from the IUT. 

   4. If the IUT supports the generation of resolvable private addresses and generates a resolvable private address for its local address, then it sends Identity Information with SMP, including a valid IRK. 

   5. If the IUT does not generate a resolvable private address for its own address and it sends Identity Information with SMP, then it sends an all-zero IRK. 

   6. If the IUT supports resolving resolvable private addresses, then it requests the Lower Tester to send its Identity Information with SMP. 

   7. If the IUT supports LE security mode 2, then the CSRK is distributed. 

   8. The Lower Tester disconnects the physical link with the IUT. 

   9. The Lower Tester establishes the connection with the IUT again. 

   10. If the IUT supports security mode 1, then the Lower Tester starts the encryption procedure with the previously distributed LTK from the IUT. 

   11. If the IUT supports security mode 2, then the IUT sends signed data with the previously distributed CSRK. 

**==> picture [304 x 265] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Tester are connected<br>Pairing Initiate Bonding<br>Security Request (Bonding)<br>Authenticated (LTK or CSRK distributed)<br>Update list of  Update list of<br>paired devices paired devices<br>Disconnect/Re-establish physical link<br>Start encryption If LE SM 1<br>Supported<br>Start data signing If LE SM 2<br>Supported<br>**----- End of picture text -----**<br>


_Figure 4.151: GAP/BOND/BON/BV-03-C [Respond to bonding – Peripheral role] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT supports LE security mode 1, then encryption is done successfully. 

If the IUT supports LE security mode 2, then data signing is done successfully. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **230 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/BOND/BON/BV-04-C [Respond to bonding – Central role]** 

- Test Purpose 

Verify that the IUT can properly respond to bonding and store bonding information after pairing while in bondable mode as Central role. 

The IUT is the responder and is in the Central role. 

The IUT supports security manager pairing and is in bondable mode. 

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing. 

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing. 

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly. 

- Reference 

   - [4] 9.4.3, 9.4.4 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - The IUT and the Lower Tester are not bonded before. 

- Test Procedure 

   1. After the connection is established, the Lower Tester initiates security request with Bonding_Flags set to “Bonding”. 

   2. The IUT initiates the pairing procedure. 

   3. The pairing procedure is completed successfully between the Lower Tester and the IUT. 

   4. If the IUT supports LE security mode 1, then LTK is distributed from the Lower Tester. 

   5. If the IUT supports the generation of resolvable private addresses and generates a resolvable private address for its local address, then it sends Identity Information with SMP, including a valid IRK. 

   6. If the IUT does not generate a resolvable private address for its own address and it sends Identity Information with SMP, then it sends an all-zero IRK. 

   7. If the IUT supports resolving resolvable private addresses, then it requests the Lower Tester to send its Identity Information with SMP. 

   8. If the IUT supports LE security mode 2, then CSRK is distributed. 

   9. The Lower Tester disconnects the physical link with the IUT. 

   10. The IUT establishes the connection with the Lower Tester again. 

   11. If the IUT supports security mode 1, then the IUT starts the encryption procedure with the previously distributed LTK from the Lower Tester. 

   12. If the IUT supports security mode 2, then the Lower Tester sends signed data with the previously distributed CSRK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **231 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [292 x 253] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Tester are connected<br>Pairing(bonding)<br>Authenticated (LTK or CSRK distributed)<br>Update list of  Update list of<br>paired devices paired devices<br>Disconnect/Re-establish physical link<br>If LE SM 1<br>Start encryption Supported<br>Start data signing If LE SM 2<br>Supported<br>**----- End of picture text -----**<br>


_Figure 4.152: GAP/BOND/BON/BV-04-C [Respond to bonding – Central role] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT supports LE security mode 1, then encryption is done successfully. 

If the IUT supports LE security mode 2, then data signing is done successfully. 

## **4.7.5 Security** 

Verify the correct implementation of the security procedure in various LE security modes, [4] Section 10. 

## **4.7.5.1 Authentication procedure** 

**GAP/SEC/AUT/BV-11-C [Service Response – Insufficient Authentication, Peripheral]** 

- Test Purpose 

Verify that the IUT properly rejects the service request when there is no sufficient bonding and then completes service correctly with the Lower Tester in the Central role. 

The IUT is operating in the Peripheral role. 

The Lower Tester is operating in the Central role. 

- Reference 

   - [4] 10.3 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - No previous bond or insufficient bond exists between the IUT and the Lower Tester. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **232 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Lower Tester initiates a service request to IUT. 

   2. The Upper Tester of the IUT detects either there was no bonding or bonding with insufficient security level. 

   3. The Upper Tester of the IUT rejects the service request with error code “Insufficient Authentication”. 

   4. The Lower Tester initiates authenticated pairing using either LE Legacy or LE Secure Connections. 

   5. Authentication is completed successfully and key information is exchanged properly. 

   6. If the IUT supports LE security mode 1, then the Lower Tester initiates encryption and send service request again. 

   7. If the IUT supports LE security mode 2, then the Lower Tester sends signed service request with previously distributed CSRK. 

   8. The IUT replies with correct service response. 

**==> picture [299 x 265] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Service Request<br>Insufficient Authentication<br>Error Response (insufficient<br>authentication) Detected<br>SM Pairing (bonding)<br>Authentication Process Complete<br>Update list of  Update list of<br>paired devices paired devices<br>Encryption or data signing<br>Service Request<br>Service Response<br>**----- End of picture text -----**<br>


_Figure 4.153: GAP/SEC/AUT/BV-11-C [Service Response – Insufficient Authentication, Peripheral] MSC_ 

- Expected Outcome 

## Pass verdict 

Authentication completes successfully. 

Service response is properly sent by the IUT. 

**GAP/SEC/AUT/BV-12-C [Service Response – Insufficient Authentication, Central]** 

- Test Purpose 

Verify that the IUT properly rejects the service request when there is no sufficient bonding and then completes service correctly with the Lower Tester in the Peripheral role. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **233 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

The IUT is operating in the Central role. 

The Lower Tester is operating in the Peripheral role. 

- Reference 

   - [4] 10.3 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - No previous bond or insufficient bond exists between the IUT and the Lower Tester. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- Test Procedure 

   1. The Lower Tester initiates a service request to the IUT. 

   2. The Upper Tester of the IUT detects either there was no bonding or bonding with insufficient security level. 

   3. The Upper Tester of the IUT rejects the service request with error code “Insufficient Authentication”. 

   4. The Lower Tester initiates pairing using either LE Legacy or LE Secure Connections. 

   5. Pairing is completed successfully and key information is exchanged properly. 

   6. If the IUT supports LE security mode 1, then the Lower Tester initiates encryption and send service request again. 

   7. If the IUT supports LE security mode 2, then the Lower Tester sends signed service request with previously distributed CSRK. 

   8. The IUT replies with correct service response. 

**==> picture [300 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Service Request<br>Error Response (insufficient  Insufficient Authentication<br>authentication) Detected<br>SM Pairing (bonding)<br>Authentication Process Complete<br>Update list of  Update list of<br>paired devices paired devices<br>Encryption or data signing<br>Service Request<br>Service Response<br>**----- End of picture text -----**<br>


_Figure 4.154: GAP/SEC/AUT/BV-12-C [Service Response – Insufficient Authentication, Central] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **234 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

Pass verdict 

Authentication completes successfully. 

Service response is properly sent by the IUT. 

**GAP/SEC/AUT/BV-13-C [Service Response – Insufficient Authentication, Central]** 

- Test Purpose 

Verify that the IUT properly rejects the service request when there is insufficient authentication and then completes service correctly with the Lower Tester in the Peripheral role. 

The IUT is operating in the Central role. 

The Lower Tester is operating in the Peripheral role. 

The IUT is capable of supporting LE security mode 1 level 3 (authenticated paring). 

Either test procedure A or B may be used. 

- Reference 

   - [4] 10.3, 10.6 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - Previous bond exists between the IUT and Lower Tester with unauthenticated pairing. 

   - Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- Test Procedure A 

   1. The Lower Tester initiates encryption by sending “security request” on the link with MITM = 0. 

   2. The IUT initiates and completes the encryption of the link. 

   3. The Lower Tester initiates a service request to the IUT. 

   4. The Upper Tester of the IUT detects the bonding has insufficient security level. 

   5. The Upper Tester of the IUT rejects the service request with error code “Insufficient Authentication”. 

   6. The Lower Tester initiates higher level bonding by sending “security request” on the link with MITM = 1. 

   7. The IUT initiates pairing with MITM = 1 and then encrypts the link. 

   8. The Lower Tester sends service request again. 

   9. The IUT replies with correct service response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **235 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 259] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Service Request<br>Error Response<br>(insufficient authentication)<br>SM Pairing (bonding)<br>Bonded with authenticated pairing<br>Update list of  Update list of<br>paired devices paired devices<br>Enable encryption of the link<br>Service Request<br>Service Response<br>**----- End of picture text -----**<br>


_Figure 4.155: GAP/SEC/AUT/BV-13-C [Service Response – Insufficient Authentication, Central] – Test Procedure A MSC_ 

- Test Procedure B 

   1. The IUT initiates encryption with previously unauthenticated bonding info. 

   2. The IUT initiates and completes the encryption of the link. 

   3. The IUT initiates a service request to the Lower Tester. 

   4. The Lower Tester detects the bonding has insufficient security level. 

   5. The Lower Tester rejects the service request with error code “Insufficient Authentication”. 

   6. The IUT initiates pairing with MITM = 1 and then encrypts the link. 

   7. The IUT sends service request again. 

   8. The Lower Tester replies with correct service response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **236 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [300 x 286] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Initiate Encryption<br>Service Request<br>Error Response<br>(insufficient authentication)<br>SM Pairing<br>Bonded with authenticated pairing<br>Update list of  Update list of<br>paired devices paired devices<br>Enable encryption of the link<br>Service Request<br>Service Response<br>**----- End of picture text -----**<br>


_Figure 4.156: GAP/SEC/AUT/BV-13-C [Service Response – Insufficient Authentication, Central] – Test Procedure B MSC_ 

- Expected Outcome 

## Pass verdict 

Authentication completes successfully. 

Service response is properly sent by the IUT. 

**GAP/SEC/AUT/BV-14-C [Service Response – Insufficient Authentication, Peripheral]** 

- Test Purpose 

Verify that the IUT properly rejects the service request when there is insufficient authentication and then completes service correctly with the Lower Tester in the Central role. 

The IUT is capable of supporting LE security mode 1 level 3 (authenticated paring). 

The IUT is operating in the Peripheral role. 

The Lower Tester is operating in the Central role. 

- Reference 

[4] 10.3, 10.6 

- Initial Condition 

   - Physical link is established by either directed or undirected connectable mode. 

   - Previous bond exists between the IUT and the Lower Tester with unauthenticated pairing. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **237 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Lower Tester initiates and completes the encryption on the link. 

   2. The Lower Tester initiates a service request to the IUT. 

   3. The Upper Tester of the IUT detects the bonding has insufficient security level. 

   4. The Upper Tester of the IUT rejects the service request with error code “Insufficient Authentication”. 

   5. The Lower Tester initiates pairing MITM = 1 and then encrypts the link again. 

   6. The Lower Tester sends service request again. 

   7. The IUT replies with correct service response. 

**==> picture [303 x 243] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Service Request<br>Error Response<br>(insufficient authentication)<br>SM Pairing (bonding)<br>Bonded with authenticated pairing<br>Update list of  Update list of<br>paired devices paired devices<br>Enable encryption of the link<br>Service Request<br>Service Response<br>**----- End of picture text -----**<br>


_Figure 4.157: GAP/SEC/AUT/BV-14-C [Service Response – Insufficient Authentication, Peripheral] MSC_ 

- Expected Outcome 

Pass verdict 

Authentication completes successfully. 

Service response is properly sent by the IUT. 

**GAP/SEC/AUT/BV-17-C [Correct Pairing after Insufficient Authentication – Central role]** 

- Test Purpose 

Verify that the IUT can pair with a device whose IO capabilities do not allow an authenticated pairing, after a service request has been denied with the error response “Insufficient Authentication”. 

The IUT is the SM initiator, GATT client and is in the Central role. 

The IUT supports security manager pairing. 

- Reference 

   - [9] 10.3 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **238 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - Whether the IUT starts the pairing procedure before issuing any service request is specified in the TSPX_pairing_before_service_request IXIT value. 

   - The IUT security policy of whether or not it mandates MITM is specified in the TSPX_iut_mandates_mitm IXIT value. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The IUT and the Lower Tester have not previously bonded. 

- Test Procedure 

   1. If the IUT starts the pairing procedure before issuing any service request is recorded in the IXIT, proceed to Step 5. 

   2. The IUT performs a service request which will be denied by the Lower Tester with the error code “Insufficient Authentication”. 

   3. The IUT initiates a pairing procedure. The authentication requirement field should only be set to MITM if the IUT mandates MITM or if it allows security level downgrade during pairing; i.e., proceeding with the pairing procedure even though the request for MITM protection could not be met. 

   4. The Lower Tester sets its IO capabilities to “NoInputNoOutput” and the authentication requirements field to zero in pairing phase 1. 

   5. If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the pairing will succeed, and the link will now be encrypted with an unauthenticated STK. The IUT completes the previous ordered service request with a success. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **239 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Initiate Service request<br>Service Request<br>Insufficient Authentication<br>Initiate Pairing<br>(if not automatic)<br>Pairing Request<br>Pairing Response (No-MITM)<br>Pairing phase 2 & 3<br>Service Request<br>Service Response (Success)<br>Pairing Failed (Auth req)<br>Optional: No auto  devices<br>pairing with  non-bonded<br>Alternative 1:<br>Not insisting on MITM<br>MITM<br>Insist on<br>Alternative 2:<br>**----- End of picture text -----**<br>


_Figure 4.158: GAP/SEC/AUT/BV-17-C [Correct Pairing after Insufficient Authentication – Central role] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the IUT will successfully complete an unauthenticated pairing with the Lower Tester and perform the service request. 

**GAP/SEC/AUT/BV-18-C [Correct Pairing after Insufficient Authentication – Peripheral role]** 

- Test Purpose 

Verify that the IUT can pair with a device whose IO capabilities do not allow an authenticated pairing, after a service request has been denied with the error response “Insufficient Authentication”. 

The IUT is the SM responder, GATT Client, and is in the Peripheral role. 

The IUT supports security manager pairing. 

- Reference 

   - [9] 10.3 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **240 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - Whether the IUT starts the pairing procedure before issuing any service request is specified in the TSPX_pairing_before_service_request IXIT value. 

   - The IUT’s security policy of whether or not it mandates MITM is specified in the TSPX_iut_mandates_mitm IXIT value. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The IUT and the Lower Tester have not previously bonded. 

- Test Procedure 

   1. If the IUT starts the pairing procedure before issuing any service request is recorded in the IXIT, proceed to Step 5. 

   2. The IUT performs a service request which will be denied by the Lower Tester with the error code “Insufficient Authentication”. 

   3. The IUT sends a security request to initiate the pairing procedure. The authentication requirement field should only be set to MITM if the IUT mandates MITM or if it allows security level downgrade during pairing; i.e., proceeding with the pairing procedure even though the request for MITM protection could not be met. 

   4. The Lower Tester sets its IO capabilities to “NoInputNoOutput” and mimics the authentication requirements field from the security request in pairing phase 1. 

   5. If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the pairing will succeed, and the link will now be encrypted with an unauthenticated STK. The IUT completes the previous ordered service request with a success. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **241 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 339] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Tester are connected<br>Initiate Service request<br>Service Request<br>Insufficient Authentication<br>Initiate Security<br>(if not automatic)<br>Security Request<br>Pairing Request<br>Pairing Response<br>Pairing phase 2 & 3<br>Service Request<br>Service Response (Success)<br>Pairing Failed (Auth req)<br>Optional: No auto  devices<br>pairing with  non-bonded<br>Alternative 1:<br>Not insisting on MITM<br>MITM<br>Insist on<br>Alternative 2:<br>**----- End of picture text -----**<br>


_Figure 4.159: GAP/SEC/AUT/BV-18-C [Correct Pairing after Insufficient Authentication – Peripheral role] MSC_ 

- Expected Outcome 

## Pass verdict 

If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the IUT will successfully complete an unauthenticated pairing with the Lower Tester and perform the service request. 

**GAP/SEC/AUT/BV-19-C [Service Response Insufficient Authentication – Central role]** 

- Test Purpose 

Verify that the IUT, when bonded with a peer device, tests the bond when receiving the error response “Insufficient Authentication” if the link is unencrypted. 

- Reference 

## [9] 10.3 

- Initial Condition 

   - The IUT is the SM initiator and GATT Client and is in the Central role. 

   - The IUT supports security manager bonding. 

   - Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value. 

   - A physical link is established between the IUT and the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **242 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - The IUT and the Lower Tester are bonded before the connection, and service discovery has been performed. The Lower Tester’s LTK has been distributed. 

   - The Lower Tester has not stored the LTK from the IUT, which will result in the “Insufficient Authentication” error in Step 2. 

- Test Procedure 

   1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value, go to Step 3. 

   2. The IUT performs a service request that is rejected by the Lower Tester with the error code “Insufficient Authentication”. 

   3. Perform Step 3 if and only if the IUT starts encryption with the Lower Tester. 

      - a. The IUT starts the encryption process with the Lower Tester. 

      - b. The Lower Tester fails the encryption process. 

   4. Perform Step 4 if and only if the IUT initiates pairing with the Lower Tester. 

      - a. The IUT sends an event to the Upper Tester to confirm the peer device. 

      - b. The Upper Tester verifies the peer device with the IUT. 

      - c. The IUT and the Lower Tester complete the pairing procedure. 

      - d. The IUT encrypts the link using a new long-term key. 

      - e. The IUT completes the previously ordered service request successfully. 

**==> picture [337 x 383] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester  IUT  Upper Tester<br>IUT and Lower Tester are connected<br>Optional: No auto encryption with bonded devices<br>Initiate Service Request<br>Service Request<br>Insufficient Authentication<br>if not automatic, Raise Security Level<br>Optional: Encryption<br>Start Encryption<br>Encryption fails<br>Optional: Pairing<br>Confirm Peer Device<br>UI to<br>confirm<br>peer device<br>Verify Peer Device<br>Encrypting with new LTK<br>Service Request<br>Service Response (success)<br>**----- End of picture text -----**<br>


_Figure 4.160: GAP/SEC/AUT/BV-19-C [Service Response Insufficient Authentication – Central role] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **243 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

After receiving the error response “Insufficient Authentication”, the IUT behaves correctly. If the IUT re-pairs, the Upper Tester confirms the remote device before starting the pairing procedure and encrypts the link with a new LTK. 

**GAP/SEC/AUT/BV-20-C [Service Response Insufficient Authentication – Peripheral role]** 

- Test Purpose 

Verify that the IUT, when bonded with a peer device, tests the bond when receiving the error response “Insufficient Authentication”, if link is unencrypted, before eventually removing the bond to perform a new pairing. During the new pairing, the IUT triggers user interaction to confirm the remote device. 

- Reference 

   - [9] 10.3, 10.3.2 

- 

## Initial Condition 

- The IUT is the SM responder and the GATT Client and is in the Peripheral role. 

- The IUT supports security manager bonding. 

- Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value. 

- A physical link is established between the IUT and the Lower Tester. 

- The IUT and the Lower Tester are bonded before the connection and service discovery has been performed. The IUT’s LTK has been distributed. 

- The Lower Tester has not stored the LTK from the IUT, which will result in the “Insufficient Authentication” error in Step 2. 

- 

## Test Procedure 

1. Perform either alternative 1A or 1B depending on if the IUT automatically starts the encryption procedure with bonded devices before issuing any service request. Alternative 1A (The IUT does not automatically start the encryption procedure.) 

   - 1A.1 The IUT performs a service request with the Lower Tester. 

   - 1A.2 The Lower Tester rejects the service request with the error code “Insufficient Authentication”. 

   - 1A.3 Optionally: The IUT may initiate the pairing procedure. 

   - Alternative 1B (The IUT automatically starts the encryption procedure.) 

   - 1B.1 The IUT sends a Security Request for the link to be encrypted. 

   - 1B.2 The Lower Tester initiates the pairing procedure with the IUT. 

   - 1B.3 Optionally: The IUT may initiate the pairing procedure. 

2. Perform Step 2 if and only if the pairing procedure has been initiated by the IUT in 1A.3 or 1B.3. 

   - a. The IUT sends an event to the Upper Tester to confirm the peer device. 

   - b. The Upper Tester verifies the peer device with the IUT. 

   - c. The pairing procedure is completed. 

3. The IUT performs a service request with the Lower Tester. 

4. The Lower Tester completes the service request successfully. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **244 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [323 x 451] intentionally omitted <==**

_Figure 4.161: GAP/SEC/AUT/BV-20-C [Service Response Insufficient Authentication – Peripheral role] MSC_ 

- Expected Outcome 

## Pass verdict 

After receiving the error response “Insufficient Authentication”, the IUT behaves correctly. 

If the IUT re-pairs, the Upper Tester confirms the remote device before the Lower Tester initiates the pairing procedure and encrypts the link with a new LTK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **245 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/AUT/BV-21-C [Lost Bond – Initiator role]** 

- Test Purpose 

Verify that the IUT will inform the upper layer about a lost bond, if the link is refused to be encrypted with the LTK distributed during the prior pairing procedure. 

The IUT is the SM initiator, GATT Client, and is in the Central role. 

The IUT supports security manager bonding. 

- Reference 

   - [9] 10.3 

- Initial Condition 

   - The IUT and the Lower Tester are bonded during a prior connection, and the Lower Tester’s LTK has been distributed. 

   - The Lower Tester has removed its bond with the IUT prior to the IUT connecting. 

   - A physical link is established between the IUT and the Lower Tester. 

- Test Procedure 

   1. The IUT is bonded with the Lower Tester. It challenges the bond by (re)-encrypting the link with the distributed LTK. 

   2. The bond has been removed on the Lower Tester. The Lower Tester responds “PIN or Key Missing” to the encryption request. 

   3. The IUT informs the upper layer that the bond has been lost. 

**==> picture [305 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Raise Security Level<br>Encryption Request<br>Failed (PIN or Key Missing)<br>Bond Lost<br>**----- End of picture text -----**<br>


_Figure 4.162: GAP/SEC/AUT/BV-21-C [Lost Bond – Initiator role] MSC_ 

- Expected Outcome 

## Pass verdict 

On receiving the error response “PIN or Key Missing” the IUT informed the upper layer that the bond has been lost. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **246 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/AUT/BV-22-C [Lost Bond – Responder role]** 

- Test Purpose 

Verify that the IUT will inform the upper layer about a lost bond, if the peer refuses to encrypt the link with the LTK distributed during the prior pairing procedure. 

The IUT is the SM responder, GATT Client, and is in the Peripheral role. 

The IUT supports security manager bonding. 

- Reference 

   - [9] 10.3 

- Initial Condition 

   - The IUT and the Lower Tester were bonded during a prior connection, and the IUT’s LTK has been distributed. 

   - The Lower Tester has removed its bond with the IUT prior to the IUT connecting. 

   - Physical link is established between the IUT and the Lower Tester. 

- Test Procedure 

   1. The IUT is bonded with the Lower Tester. It challenges the bond by sending a security request to enable encryption. 

   2. The bond has been removed on the Lower Tester. The Lower Tester initiates a pairing procedure. 

   3. The IUT informs the upper layer that the bond has been lost. 

**==> picture [305 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Raise Security Level<br>Security Request<br>Pairing Request<br>Bond Lost<br>**----- End of picture text -----**<br>


_Figure 4.163: GAP/SEC/AUT/BV-22-C [Lost Bond – Responder role] MSC_ 

- Expected Outcome 

## Pass verdict 

On receiving a pairing request as a successor to the security request, the IUT informed the upper layer that the bond has been lost. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **247 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/AUT/BV-23-C [Service Response – Insufficient Encryption, Peripheral]** 

- Test Purpose 

Verify that the IUT properly rejects the service request when the required pairing has occurred and encryption is required (LE security mode 1) if encryption is not enabled and then completes service correctly with the Lower Tester acting in the Central role. 

The IUT is operating in the Peripheral role. 

The Lower Tester is operating in the Central role. 

- Reference 

   - [4] 10.3 

- Initial Condition 

   - Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value. 

   - A physical link is established by either directed or undirected connectable mode. 

   - Previous bond exists between the IUT and the Lower Tester with authenticated pairing. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- Test Procedure 

   1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value, go to Step 4. 

   2. If the link is not encrypted, the Lower Tester initiates a service request to the IUT. 

   3. If the IUT detects that no LTK is available then the IUT rejects the service request with error code “Insufficient Authentication”. If the IUT detects LTK is available and link is unencrypted then the IUT rejects the service request with error code “Insufficient Encryption”. 

   4. The Lower Tester initiates encryption and sends service request again. 

   5. Link encryption is completed successfully. 

   6. The IUT replies with correct service response. 

**==> picture [304 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Service Request<br>Error Response (Insufficient Encryption or<br>Insufficient Authentication)<br>Enable Encryption of the link<br>Service Request<br>Service Response (Success)<br>Optional: No auto  encryption  devices<br>with bonded<br>**----- End of picture text -----**<br>


_Figure 4.164: GAP/SEC/AUT/BV-23-C [Service Response – Insufficient Encryption, Peripheral] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **248 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

Pass verdict 

Encryption setup completes successfully. 

Service response is properly sent by the IUT after Step 6. 

**GAP/SEC/AUT/BV-24-C [Service Response – Insufficient Encryption, Central]** 

- Test Purpose 

Verify that the IUT properly rejects the service request when the required pairing has occurred and encryption is required (LE security mode 1) if encryption is not enabled and then completes service correctly with the Lower Tester acting in the Peripheral role. 

The IUT is the SM initiator, GATT Server, and is operating in the Central role. 

The Lower Tester is operating in the Peripheral role. 

- Reference 

   - [4] 10.3 

- Initial Condition 

   - Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value. 

   - A physical link is established by either directed or undirected connectable mode. 

   - Previous bond exists between the IUT and the Lower Tester with authenticated pairing using either LE Legacy or LE Secure Connections. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- Test Procedure 

   1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value, go to Step 5. 

   2. If the link is not encrypted, then the Lower Tester initiates a service request to the IUT. 

   3. The IUT detects that the link is not encrypted. 

   4. The IUT rejects the service. If the IUT detects that no LTK is available then the IUT rejects the service request with error code “Insufficient Authentication”. If the IUT detects that LTK is available and link is unencrypted, then the IUT rejects the service request with error code “Insufficient Encryption”. 

   5. The Lower Tester initiates encryption and sends the service request again. 

   6. Link encryption is completed successfully. 

   7. The IUT replies with correct service response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **249 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [298 x 217] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are connected<br>Service Request<br>Error Response (Insufficient Encryption or<br>Insufficient Authentication)<br>Enable Encryption of the link<br>Service Request<br>Service Response (Success)<br>Optional: No auto  encryption  devices<br>with bonded<br>**----- End of picture text -----**<br>


_Figure 4.165: GAP/SEC/AUT/BV-24-C [Service Response – Insufficient Encryption, Central] MSC_ 

- Expected Outcome 

Pass verdict 

Encryption setup completes successfully. 

Service response is properly sent by the IUT after Step 7. 

- **4.7.5.1.1 Service Response – Insufficient Authentication** 

- Test Purpose 

Verify that the IUT prompts a user interaction before initiating the pairing procedure when a service request failed for “Insufficient Authentication” and the encryption procedure has failed. 

- Reference 

   - [17] 10.3.2 

- Initial Condition 

   - The IUT is the GATT Client and is in the role specified in Table 4.31. 

   - The IUT supports security manager bonding. 

   - Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value. 

   - TSPX_Use_IXIT_TSPX_spsm determines whether the Upper Tester uses the TSPX_spsm or will use the MMI to prompt for the L2CAP SPSM. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The IUT and the Lower Tester are bonded before the connection and service discovery have been performed. 

   - The Initial Condition from Table 4.31 is established. 

   - The Lower Tester has not stored the LTK from the IUT, which will result in the “Insufficient Authentication” error in Step 2. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **250 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Case Configuration 

|**Test Case**|**Role**|**Initial Condition**|
|---|---|---|
|GAP/SEC/AUT/BV-25-C|Central|The Lower Tester’s LTK has been distributed.|
|GAP/SEC/AUT/BV-26-C|Peripheral|The IUT’s LTK has been distributed.|



_Table 4.31: Service Response – Insufficient Authentication test cases_ 

- Test Procedure 

   1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value, go to Step 3. 

   2. The IUT performs a service request that is rejected by the Lower Tester with the error code “Insufficient Authentication”. 

   3. The IUT starts the encryption procedure. 

   4. Perform either alternative 4A or 4B depending on the IUT role. Alternative 4A (The IUT is in the Central role): 

      - 4A.1 The Lower Tester is to fail the encryption procedure. 

      - Alternative 4B (The IUT is in the Peripheral role): 

         - 4B.1 The Lower Tester initiates pairing. 

   5. The IUT may start User Interaction by executing Steps 6–9. 

   6. The remote device is confirmed by the Upper Tester, prompting the IUT to initiate, if the IUT is in the Central role, or to continue, if the IUT is in the Peripheral role, the pairing procedure. 

   7. The pairing is completed successfully and key information is exchanged properly. 

   8. If the IUT supports LE security mode 1, then the Lower Tester initiates encryption and send the service request again. If the IUT supports LE security mode 2, then the Lower Tester sends a signed service request with previously distributed CSRK. 

   9. The IUT completes the previously ordered service request with success. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **251 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [175 x 51] intentionally omitted <==**

**==> picture [339 x 436] intentionally omitted <==**

_Figure 4.166: Service Response – Insufficient Authentication MSC_ 

- Expected Outcome 

## Pass verdict 

In Step 5, after the encryption procedure fails, the IUT prompts the Upper Tester to initiate a user interaction to confirm the remote device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **252 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.5.1.2 Service Response – Insufficient Encryption** 

- Test Purpose 

Verify that the IUT prompts a user interaction before initiating the pairing procedure when a service request failed for “Insufficient Encryption” and the encryption procedure has failed. 

- Reference 

   - [17] 10.3.2 

- Initial Condition 

   - The IUT is the GATT Client and is in the role specified in Table 4.32. 

   - The IUT supports security manager bonding. 

   - Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value. 

   - A physical link is established by either directed or undirected connectable mode. 

   - A previous bond exists between the IUT and the Lower Tester with authenticated pairing. 

   - The Upper Tester of the IUT is either a GATT profile or a higher-layer protocol. 

- Test Case Configuration 

|**Test Case**|**Role**|
|---|---|
|GAP/SEC/AUT/BV-27-C|Central|
|GAP/SEC/AUT/BV-28-C|Peripheral|



_Table 4.32: Service Response – Insufficient Encryption test cases_ 

- Test Procedure 

   1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX_encryption_before_service_request IXIT value, go to Step 5. 

   2. The IUT initiates a service request to the Lower Tester. 

   3. The Lower Tester detects that the link is not encrypted. 

   4. The Lower Tester rejects the service request with error code “Insufficient Encryption”. 

   5. The IUT initiates the encryption procedure. 

   6. Perform either alternative 6A or 6B depending on the IUT role. Alternative 6A (The IUT is in the Central role): 

      - 6A.1 The Lower Tester fails the encryption procedure. 

      - Alternative 6B (The IUT is in the Peripheral role): 

         - 6B.1 The Lower Tester initiates pairing. 

   7. The IUT may start User Interaction by executing Steps 9–11. 

   8. The remote device is confirmed by the Upper Tester, prompting the IUT to initiate, if the IUT is in the Central role, or to continue, if the IUT is in the Peripheral role, the pairing procedure. 

   9. The pairing is completed successfully, and key information is exchanged properly. 

   10. The IUT sends the service request again. 

   11. The Lower Tester replies with a correct service response. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **253 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [174 x 52] intentionally omitted <==**

**==> picture [338 x 452] intentionally omitted <==**

_Figure 4.167: Service Response – Insufficient Encryption MSC_ 

- Expected Outcome 

## Pass verdict 

In Step 9, the IUT prompts the Upper Tester to initiate a user interaction to confirm the remote device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **254 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.5.2 Connection Based Data Signing** 

Verify the correct implementation of the GAP data signing procedure. 

**GAP/SEC/CSIGN/BV-01-C [Connection Based Signing – Sender]** 

- Test Purpose 

Verify that the IUT can properly sign the data when LE security mode 2 is required. 

Verify that the IUT sends data that is properly signed using the Connection Signature Resolving Key (CSRK) previously distributed to the Lower Tester. 

The Lower Tester receives the signed data from the IUT and verifies that the MAC and SignCounter are correct. 

- Reference 

   - [4] 10.4 

- Initial Condition 

   - The IUT is the role specified in the TSPX_gap_iut_role IXIT entry. 

   - A dedicated bonding was performed and a CSRK was distributed from the IUT to the Lower Tester. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- Test Procedure 

   1. The Upper Tester of the IUT requests the IUT to send a service request signed with previously distributed CSRK. 

   2. The Lower Tester receives the signed service request and verifies the MAC and SignCounter. 

   3. The Lower Tester accepts the service request from the IUT. 

**==> picture [304 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded with SRK<br>Send signed data<br>Send signed data<br>**----- End of picture text -----**<br>


_Figure 4.168: GAP/SEC/CSIGN/BV-01-C [Connection Based Signing – Sender] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives the signed service request and verifies that the MAC and SignCounter are correct. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **255 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/CSIGN/BV-02-C [Connection Based Signing – Receiver]** 

- Test Purpose 

Verify that the IUT can properly verify the MAC and SignCounter when LE security mode 2 is required. 

Verify that the IUT can properly verify the MAC and SignCounter from the Lower Tester. 

The data is signed using the Connection Signature Resolving Key (CSRK) previously distributed from the Lower Tester. 

- Reference 

   - [4] 10.4 

- 

   - Initial Condition 

   - The IUT is the role as specified in the TSPX_gap_iut_role IXIT entry. 

   - A dedicated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- 

- Test Procedure 

1. The Lower Tester sends a service request signed with previously distributed CSRK to the IUT. 

2. The IUT receives the signed service request and verifies the MAC and SignCounter. 

3. The IUT forwards the service request to the Upper Tester. 

4. The Upper Tester accepts the service request. 

5. The Upper Tester sends the proper service response to the Lower Tester. 

**==> picture [305 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded with SRK<br>Receive signed data<br>Send signed data<br>**----- End of picture text -----**<br>


_Figure 4.169: GAP/SEC/CSIGN/BV-02-C [Connection Based Signing – Receiver] MSC_ 

- Expected Outcome 

## Pass verdict 

The Upper Tester receives a correct service request. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **256 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/CSIGN/BI-01-C [Connection Based Signing – Receiver – Invalid Signing]** 

- Test Purpose 

Verify that the IUT can detect an invalid signed service request from the Lower Tester and reject it. 

The data is signed with an incorrect CSRK. 

- Reference 

   - [4] 10.4 

- Initial Condition 

   - The IUT is in the role specified in the TSPX_gap_iut_role IXIT entry. 

   - A dedicated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- Test Procedure 

   1. The Lower Tester sends a service request signed with incorrect CSRK to IUT. 

   2. The IUT receives the signed service request and detects invalid MAC. 

   3. The IUT silently discards the service request. 

**==> picture [305 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded with SRK<br>Receive signed data<br>Send incorrect signed data<br>**----- End of picture text -----**<br>


_Figure 4.170: GAP/SEC/CSIGN/BI-01-C [Connection Based Signing – Receiver – Invalid Signing] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives signed data from the Lower Tester. 

The IUT detects the signed data has incorrect CSRK. 

The IUT ignores the received signed data. 

The IUT does not forward the received signed data to the Upper Tester. 

If this is a service request, the Lower Tester does not receive any service response or receives an error response from the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **257 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/CSIGN/BI-02-C [Connection Based Signing – Receive Invalid SignCounter]** 

- Test Purpose 

Verify that the IUT can detect an invalid signed service request from the Lower Tester and reject it. 

The data is signed with invalid SignCounter. 

- Reference 

   - [4] 10.4 

- Initial Condition 

   - The IUT is in the role specified in the TSPX_gap_iut_role IXIT entry. 

   - A dedicated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The Upper Tester of the IUT is either a GATT profile or a higher layer protocol. 

- Test Procedure 

   1. The Lower Tester sends a service request with SignCounter = 0 to the IUT. 

   2. The IUT receives the signed service request and properly forwards it to the Upper Tester. 

   3. The Lower Tester sends a service request with SignCounter = 1 to the IUT. 

   4. The IUT receives the signed service request and properly forwards it to the Upper Tester. 

   5. The Lower Tester sends a service request with SignCounter = 0 to the IUT. 

   6. The IUT receives the signed service request and silently discards it. 

**==> picture [304 x 177] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded with SRK<br>Send signed data with SignCounter 0<br>Send signed data with SignCounter 1<br>Send signed data with SignCounter 0<br>**----- End of picture text -----**<br>


_Figure 4.171: GAP/SEC/CSIGN/BI-02-C [Connection Based Signing – Receive Invalid SignCounter] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT does not forward the last received signed data with incorrect SignCounter value to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **258 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/CSIGN/BI-03-C [Connection Based Signing – Receive, No Bonding, as Peripheral]** 

- Test Purpose 

Verify that the IUT properly discards the message when receiving a “signed write command” with no bonding info when LE security mode 2 level 1 is required. 

The data is signed with a CSRK that was distributed with either unauthenticated or authenticated bonding. After bonding, the IUT’s bonding information was removed by the Upper Tester. 

The IUT’s bonding information can be removed by the Upper Tester. 

- Reference 

   - [4] 10.4 

- Initial Condition 

   - An unauthenticated or authenticated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT. 

   - The IUT’s bonding information was removed by the Upper Tester. 

   - The IUT is in the role specified in the TSPX_gap_iut_role IXIT entry. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The Upper Tester of the IUT has a pre-defined characteristic attribute value handle that supports signed write command with security request of LE security mode 2 level 1. 

- Test Procedure 

   1. The Lower Tester sends a “signed write command” with distributed CSRK to the IUT. 

   2. The IUT receives the “signed write command” but detects that there is no bonding information of the Lower Tester. 

   3. The IUT discards the “signed write command”. 

   4. The IUT does not try to re-establish bonding. 

**==> picture [340 x 118] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester are bonded with CSRK<br>Bonding info is removed<br>Send “Signed Write Command”<br>**----- End of picture text -----**<br>


_Figure 4.172: GAP/SEC/CSIGN/BI-03-C [Connection Based Signing – Receive, No Bonding, as Peripheral] MSC_ 

- Expected Outcome 

## Pass verdict 

The Upper Tester does not receive the “signed write” command. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **259 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/SEC/CSIGN/BI-04-C [Connection Based Signing – Receive, Insufficient Authentication, as Peripheral]** 

- Test Purpose 

Verify that the IUT properly discards a signed data write with insufficient security level when LE security mode 2 level 2 is required. 

The data is signed with a CSRK that was distributed with unauthenticated bonding. 

- Reference 

[4] 10.4 

- Initial Condition 

   - An unauthenticated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The IUT is in the role specified in the TSPX_gap_iut_role IXIT entry. 

   - The Upper Tester of the IUT has a pre-defined characteristic attribute value handle that supports signed write command with security request of LE security mode 2 level 2. 

- Test Procedure 

   1. The Lower Tester sends a “signed write command” with distributed CSRK to the IUT. 

   2. The IUT receives the “signed write command” but detects that there is insufficient authentication level of the bonding information of the Lower Tester. 

   3. The IUT discards the “signed write command”. 

**==> picture [340 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT and Lower Tester bonded with “unauthenticated<br>pairing”, CSRK is distributed.<br>Send “Signed Write Command”<br>**----- End of picture text -----**<br>


_Figure 4.173: GAP/SEC/CSIGN/BI-04-C [Connection Based Signing – Receive, Insufficient Authentication, as Peripheral] MSC_ 

- Expected Outcome 

## Pass verdict 

The Upper Tester does not receive the “signed write command”. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **260 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.5.3 Privacy** 

Verify IUT compliance to the privacy feature. 

## **GAP/PRIV/CONN/BV-10-C [Peripheral Privacy]** 

- Test Purpose 

Verify that the IUT in the Undirected Connectable mode supporting the Privacy feature can connect with another device performing the General Connection Establishment procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [6] 10.7.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT has Privacy feature enabled. 

   - TGAP(private_addr_int) for the IUT is specified in the TSPX_iut_private_address_interval IXIT value. 

   - The IUT and the Lower Tester have performed the bonding procedures and distributed their respective IRKs using either LE Legacy or LE Secure Connections. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter Undirected Connectable mode; the IUT sets the advertiser’s address to a resolvable private address based on the IRK distributed during the bonding procedure. 

   2. The IUT changes the advertiser address to a new and unique resolvable address every TGAP(private_addr_int). 

   3. The Lower Tester verifies that the resolvable private address changes at least once after TGAP(private_addr_int). 

   4. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received resolvable private address from the IUT and sets the initiator’s address to an RPA value based on the IRK of the Lower Tester. 

   5. The Lower Tester or the IUT terminates the connection. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **261 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [268 x 174] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Enter Undirected<br>General  Connectable Mode<br>Connection<br>Establishment<br>Procedure<br>Advertising Event<br>Connect Request<br>Connection Establishment<br>**----- End of picture text -----**<br>


_Figure 4.174: GAP/PRIV/CONN/BV-10-C [Peripheral Privacy] MSC_ 

- Expected Outcome 

Pass verdict 

The Lower Tester receives connectable undirected advertising events from the IUT during the period that the IUT has privacy enabled and is in Undirected Connectable mode. 

In each connectable undirected advertising event received, the advertiser address is set to a valid resolvable private address. 

The Lower Tester is able to resolve and confirm the identity of the IUT from the received resolvable private address. 

The Lower Tester verifies that the IUT changes the resolvable private address in the advertiser address of the received advertising events after TGAP(private_addr_int). 

The Lower Tester establishes a connection with the IUT using the received advertiser address. 

The Lower Tester or the IUT successfully terminates the connection. 

## **GAP/PRIV/CONN/BV-11-C [Central Privacy]** 

- Test Purpose 

Verify that the IUT supporting the Privacy feature and performing the General Connection Establishment procedure can connect with another device supporting the Privacy feature in the Undirected Connectable mode. 

The IUT is operating in the Central role. 

- Reference 

[6] 10.7.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT has Privacy feature enabled. 

   - The support for accepting Public or Static addresses is specified in the TSPX_bd_addr_iut IXIT value. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **262 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - The IUT and the Lower Tester have performed the bonding procedures and distributed their respective IRKs using either LE Legacy or LE Secure Connections. 

- Test Procedure 

   1. The Lower Tester enters Undirected Connectable mode; the Lower Tester sets the advertisers address to an RPA value based on the IRK of the Lower Tester. 

   2. The Upper Tester orders the IUT to perform the General Connection Establishment procedure; the IUT sets the initiator’s address to a resolvable private address based on the IRK of the IUT. 

   3. A connection is established. 

   4. The Lower Tester or the IUT terminates the connection. 

   5. The Lower Tester enters Undirected Connectable mode; the Lower Tester sets the advertiser’s address to a resolvable private address based on a random number that is not its IRK. 

   6. The Upper Tester orders the IUT to perform the General Connection Establishment procedure. 

**==> picture [266 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General Connection<br>Enter Undirected  Establishment Procedure<br>Connectable Mode<br>Advertising Event<br>Connect Request<br>Connection Establishment<br>Terminate<br>Advertising Event<br>Advertising Event<br>Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.175: GAP/PRIV/CONN/BV-11-C [Central Privacy] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives a connection request from the IUT during the period that the IUT has privacy enabled and is performing the General Connection Establishment procedure. 

In each connection request packet received by the Lower Tester, the initiator’s address is set to a valid resolvable private address. 

The Lower Tester is able to resolve and confirm the identity of the IUT from the received resolvable private address. 

The Lower Tester verifies that the IUT changes its (InitA field) resolvable private address in the connection request packet. 

The Lower Tester establishes a connection with the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **263 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

The Lower Tester or the IUT successfully terminates the connection. 

The IUT does not perform the Connection Establishment procedure when the Lower Tester uses a resolvable private address based on an incorrect IRK. 

- Notes 

Since the IUT, when receiving advertisement packets with incorrect RPAs, should not initiate the connection establishment procedure, multiple undirected connectable advertisement packets should be sent to verify compliance. 

## **GAP/PRIV/CONN/BV-12-C [Peripheral Privacy, Unresolvable RPA]** 

- Test Purpose 

Verify that the IUT in the Undirected Connectable mode supporting the Privacy feature properly handles the connection request when the IUT receives an unresolvable RPA. The IUT handles the connection request using one of the following: accept the connection, disconnect with the error code “Authentication Failure”, perform the pairing procedure, perform the authentication procedure. 

The IUT is operating in the Peripheral role. 

- Reference 

   - [17] 10.7.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The IUT has the Privacy feature enabled. 

   - The IUT has a stored bond. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter Undirected Connectable mode. 

   2. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT. 

   3. The Lower Tester attempts to create the connection and sets the initiator’s address to an unresolvable RPA. 

   4. The IUT fails to resolve the initiator’s RPA. 

Alternative 1: The IUT accepts and establishes the connection. 

- Alternative 2: The IUT disconnects the connection with the error code “Authentication Failure”. Alternative 3: The IUT accepts the connection and performs the pairing procedure with the Lower Tester. 

Alternative 4: The IUT accepts the connection and performs the authentication procedure with the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **264 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [268 x 400] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Enter Undirected<br>Connectable Mode<br>Undirected<br>Connectable<br>Mode<br>General/Direct Connection<br>Establishment Procedure<br>Advertising Event<br>Connect Request<br>Address<br>Resolution<br>Failure<br>ALT 1<br>Connection Establishment<br>Connection Complete<br>Disconnect ACL Link ALT 2<br>(Authentication Failure –<br>0x05)<br>ALT 3<br>Connection Establishment<br>Connection Complete<br>Pairing Procedure<br>ALT 4<br>Connection Establishment<br>Connection Complete<br>Authentication Procedure<br>**----- End of picture text -----**<br>


_Figure 4.176: GAP/PRIV/CONN/BV-12-C [Peripheral Privacy, Unresolvable RPA] MSC_ 

- Expected Outcome 

## Pass verdict 

In Step 4, the IUT fails to resolve the initiator’s RPA. 

Alternative 1: In Step 5, the IUT accepts and establishes the connection. Alternative 2: In Step 5, the IUT disconnects with the error code “Authentication Failure”. Alternative 3: In Step 5, the IUT and the Lower Tester pair successfully. 

Alternative 4: In Step 5, the IUT and the Lower Tester complete the authentication procedure successfully. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **265 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.6 AD type** 

- Test Purpose 

Verify that the IUT sends the valid AD type specified in Table 4.33 in advertising and scan response data. 

- Reference 

   - [4] 11 

- Initial Condition 

   - The IUT is Broadcaster or Peripheral. 

   - The Lower Tester is Observer or Central. 

   - The IUT is in Link Layer state ‘Standby’. 

   - For GAP/ADV/BV-17-C, the expected URI UTF-8 string is defined in TSPX_URI in IXIT [3]. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **266 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Case Configuration 

|**Test Case ID**|**Reference**|**AD Type**|**Additional Test Requirements**|
|---|---|---|---|
|GAP/ADV/BV-01-C<br>[AD type – Service<br>UUID]|[7]1.1|Any of the Service UUID<br>AD types|The advertising or scan response data has a length that is a multiple of 2, 4,<br>or 16 octets depending on the AD type.|
|GAP/ADV/BV-02-C<br>[AD type – Local<br>Name]|[7]1.2|Complete Local Name or<br>Shortened Local Name|The advertising or scan response data must contain only one instance of<br>these AD types in each of the advertising and scan response data; it need<br>not be present in both.<br>The Lower Tester reads the complete name from the Device Name<br>Characteristic on the IUT. If the AD type is Complete Local Name, then the<br>data must be the same as the complete name. If the AD type is Shortened<br>Local Name, then the data must be the first octets of the complete name.|
|GAP/ADV/BV-03-C<br>[AD type – Flags]|[7]1.3|Flags|This AD type must be present if the advertising packet is connectable and<br>the IUT supports at least one of the features listed in[7]1.3.2. Otherwise, it<br>is optional, but, if present, it must meet these requirements.<br>The flags in the data must match the features supported by the IUT.<br>The last octet in the data must not be zero. The data may be omitted (with<br>the AD structure Length equal to 1) if the data would be all zeroes.<br>There must be only one instance of this AD type and it must be in the<br>advertisingdata, not the scan response data.|
|GAP/ADV/BV-04-C<br>[AD type –<br>Manufacturer<br>Specific Data]|[7]1.4|Manufacturer Specific<br>Data|The advertising or scan response data contains the Manufacturer Specific<br>Data AD type with the first 2 octets containing the Company Identifier Code.|
|GAP/ADV/BV-05-C<br>[AD type – TX Power<br>Level]|[7]1.5|TX Power Level|The advertising or scan response data contains the TX Power Level AD type<br>with 1 octet of data not equal to 0x80.|
|GAP/ADV/BV-08-C<br>[AD type – Peripheral<br>Connection Interval<br>Range]|[7]1.9|Peripheral Connection<br>Interval Range|The advertising or scan response data has a length of 4 and contains two<br>16-bit unsigned values. Each must be in the range 0x0006 to 0x0C80, and<br>the first must not be greater than the second.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **267 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Test Case ID**|**Reference**|**AD Type**|**Additional Test Requirements**|
|---|---|---|---|
|GAP/ADV/BV-09-C<br>[AD type – Service<br>Solicitation]|[7]1.10|Any of the Service<br>Solicitation AD types|The advertising or scan response data has a length that is a multiple of 2, 4,<br>or 16 octets depending on the AD type.|
|GAP/ADV/BV-10-C<br>[AD type – Service<br>Data]|[7]1.11|Any of the Service Data<br>AD types|The advertising or scan response data has a length that is greater than 2, 4,<br>or 16 depending on the AD type.|
|GAP/ADV/BV-11-C<br>[AD type –<br>Appearance]|[4]12.2<br>[7]1.12|Appearance|The advertising or scan response data has a length of 2 octets.<br>There must be only one instance of this AD type and it must not appear in<br>both the advertisingand scan response data of the same advertisement.|
|GAP/ADV/BV-12-C<br>[AD type – Public<br>Target Address]|[7]1.13<br>[8]1.3.1|Public Target Address|The advertising or scan response data has a length that is a multiple of 6.<br>There must be only one instance of this AD type and it must not appear in<br>both the advertisingand scan response data of the same advertisement.|
|GAP/ADV/BV-13-C<br>[AD type – Random<br>Target Address]|[4]10.8<br>[7]1.14<br>[8]1.3.2|Random Target Address|The advertising or scan response data has a length that is a multiple of 6<br>and contains one or more addresses. For each address, either:<br>The two most significant bits of the address are the same and the remaining<br>46 bits contain at least one 0 bit and one 1 bit.<br>The most significant bit is 0, the next bit is 1, and the next 22 bits contain at<br>least one 0 bit and one 1 bit. (The least significant 24 bits are<br>unconstrained.)<br>There must be only one instance of this AD type and it must not appear in<br>both the advertisingand scan response data of the same advertisement.|
|GAP/ADV/BV-14-C<br>[AD type –<br>Advertising Interval]|[7]1.15<br>[8]4.2.2.2|Advertising Interval|The advertising or scan response data has a length of 2 and contains an<br>unsigned 16-bit value.<br>There must be only one instance of this AD type in each of the advertising<br>and scan response data; it need not bepresent in both.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **268 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Test Case ID**|**Reference**|**AD Type**|**Additional Test Requirements**|
|---|---|---|---|
|GAP/ADV/BV-17-C<br>[AD type – URI]|[7]1.18|URI|The advertising data and scan response data must contain a correctly<br>formatted UTF-8 string representing the URI. The first code point must be<br>one that is in the relevant Assigned Numbers. If the first code point is<br>U+0001, represented in UTF-8 as a single octet with value 0x01, the actual<br>scheme and “:” are included in the remaining UTF-8 string. Otherwise, they<br>are omitted from the string. The string matches the value provided in<br>TSPX_URI.|
|GAP/ADV/BV-18-C<br>[AD type –<br>Advertising Interval,<br>Long]|[7]1.15<br>[8]4.2.2.2|Advertising Interval –<br>Long|The advertising or scan response data has a length of 3 or 4 and contains<br>an unsigned 24-bit or 32-bit value that must be at least 0x10000.|
|GAP/ADV/BV-19-C<br>[AD type – LE<br>Supported Features]|[7]1.19<br>[8]4.6|LE Supported Features|The advertising or scan response data has a length no greater than 8. The<br>last octet must not be zero. Those octets that are present, padded to 8<br>octets with zeroes, must be the same as the Link Layer’s FeatureSet.<br>There must be only one instance of this AD type in each of the advertising<br>and scan response data; it need not bepresent in both.|



_Table 4.33: AD type test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **269 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester orders the IUT to start advertising; the IUT enters broadcast mode or a discoverable mode. 

   2. The Lower Tester enters Active Scanning. 

**==> picture [342 x 136] intentionally omitted <==**

_Figure 4.177: AD type MSC_ 

- Expected Outcome 

## Pass verdict 

The Advertising or Scan Response data does not contain zero octets between the AD structures or after the last AD structure. 

Reserved bits or values are not used. 

All the requirements in the Additional Test Requirements column of Table 4.33 are met. 

- Notes 

Unless stated otherwise in the Additional Test Requirements, an AD type may appear more than once in the same advertisement, including in both the advertising data and scan response data. 

## **4.7.6.1 AD type – Encrypted Data** 

- Test Purpose 

Verify that the IUT sends valid Encrypted Data AD type in advertising. The AD Data payload is encrypted using a pre-shared key, a pre-shared initialization vector, and a randomizer. If supported, the IUT may include non-significant data. 

- Reference 

   - [7] 1.23 

- Initial Condition 

   - The IUT is Peripheral. 

   - The Lower Tester is Central. 

   - The IUT is in Link Layer state ‘Standby’. 

   - The Lower Tester is in the Passive Scanning state. 

   - If TSPX_ead_keys_sharing_method is selected as ‘KEYS_SHARED_VIA_IXIT’, the IUT and the Lower Tester will use the already shared Session Key and IV value from TSPX_encrypted_data_key and TSPX_initialization_vector. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **270 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - If TSPX_ead_keys_sharing_method is selected as ‘KEYS_EXCHANGED_VIA_CONNECTION’, the IUT will read the already shared Session Key and IV from the Encrypted Data Key Material characteristic. 

- Test Case Configuration 

|**Test Case**|**Non-significant data**|
|---|---|
|GAP/ADV/BV-20-C[AD type – Encrypted Data]|No|
|GAP/ADV/BV-21-C[AD type – Encrypted Data]|Yes|



_Table 4.34: AD type – Encrypted Data test cases_ 

- Test Procedure 

   1. The Upper Tester orders the IUT to start advertising; the IUT enters broadcast mode or a discoverable mode and begins advertising using Encrypted Advertising Data with a random payload. 

   2. The IUT sends an Advertising event using Encrypted Advertising Data with the payload from Step 1. 

   3. The Upper Tester orders the IUT to begin advertising using Encrypted Advertising Data with a payload that is different from the payload in Step 1. 

   4. The IUT sends an Advertising event using Encrypted Advertising Data with the payload from Step 3. If allowed by Table 4.34, the IUT may send non-significant data after the payload of encrypted AD structures. 

   5. The Upper Tester orders the IUT to begin advertising using Encrypted Advertising Data with the same payload as Step 1. 

   6. The IUT sends an Advertising event using Encrypted Advertising Data with the payload in Step 5. 

**==> picture [81 x 167] intentionally omitted <==**

**==> picture [77 x 47] intentionally omitted <==**

_Figure 4.178: AD type – Encrypted Data MSC_ 

- Expected Outcome 

## Pass verdict 

In Steps 2, 4, and 6, the IUT sends Advertising Data that contains a 5 octet Randomizer, a properly encrypted Payload, and a 4 valid octet MIC. The encrypted Payload Data, MIC, and Randomizer are different each time the payload data is changed. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **271 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

In Step 2, the decrypted payload matches the payload in Step 1. 

In Step 4, the decrypted payload matches the payload in Step 3. 

In Step 6, the decrypted payload matches the payload in Step 5. 

- Notes 

It is optional to include any of the AD types in advertising and scan response data. 

**GAP/SCN/BV-01-C [AD type – Encrypted Data, Decrypt Advertising Data]** 

- Test Purpose 

Verify that the IUT correctly decodes a received Encrypted Data AD type from the Lower Tester. 

- Reference 

[7] 1.23 

- Initial Condition 

   - The Lower Tester is Peripheral. 

   - The IUT is Central. 

   - The IUT is in Link Layer state ‘Standby’. 

   - If TSPX_ead_keys_sharing_method is selected as ‘KEYS_SHARED_VIA_IXIT’, the IUT and the Lower Tester will use the already shared Session Key and IV value from TSPX_encrypted_data_key and TSPX_initialization_vector. 

   - If TSPX_ead_keys_sharing_method is selected as ‘KEYS_EXCHANGED_VIA_CONNECTION’, the IUT will read the already shared Session Key and IV from the Encrypted Data Key Material characteristic. 

- Test Procedure 

   1. The Upper Tester orders the IUT to start Passive Scanning. 

   2. The Lower Tester starts advertising an Encrypted Data AD type with encrypted advertising with a valid MIC. 

   3. The IUT reports the unencrypted advertising data to the Upper Tester. 

**==> picture [419 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester  IUT  Upper Tester<br>Start Passive Scanning<br>Lower Tester starts<br>Advertising<br>Advertising Event<br>(Encrypted Advertising, MIC)<br>Advertising Report<br>(Data)<br>**----- End of picture text -----**<br>


_Figure 4.179: GAP/SCN/BV-01-C [AD type – Encrypted Data, Decrypt Advertising Data] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **272 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

In Step 3, the IUT sends an advertising report to the Upper Tester with the same advertising data as the Lower Tester unencrypted advertising data from Step 2. 

## **GAP/GAT/BV-15-C [Encrypted Data Key Characteristic Indication, GATT Server]** 

- Test Purpose 

Verify that the IUT with an authenticated and authorized connection properly sends a GATT Indication PDU to the Lower Tester when the Encrypted Data Key Characteristic value is updated. 

- Reference 

[18] 12.6 

- Initial Condition 

   - The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT Server. 

   - A physical link is established between the IUT and the Lower Tester that is authenticated and authorized. 

- Test Procedure 

**==> picture [361 x 159] intentionally omitted <==**

_Figure 4.180: GAP/GAT/BV-15-C [Encrypted Data Key Characteristic Indication, GATT Server] MSC_ 

   1. The Lower Tester sends an ATT_WRITE_REQ to the IUT with CCCD set to 0x0002. 

   2. The IUT sends an ATT_WRITE_RSP to the Lower Tester. 

   3. The Upper Tester commands the IUT to change the Encrypted Data Key Characteristic value with a new key. 

   4. The IUT sends an ATT_HANDLE_VALUE_IND PDU to the Lower Tester with Attribute Handle set to the Encrypted Data Key Characteristic, and Attribute Value set to the new value. 

   5. The Lower Tester sends an ATT_HANDLE_VALUE_CFM PDU to the IUT. 

- 

- Expected Outcome 

## Pass verdict 

In Step 4, the IUT sends an ATT Handle Value Indication PDU to the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **273 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.7 Generic Access Profile characteristics** 

Verify the correct implementation of the GAP characteristics. 

## **4.7.7.1 GAP attributes** 

## **GAP/GAT/BV-09-C [Encrypted Data Key Material, Authenticated and Authorized]** 

- Test Purpose 

Verify that the GAP ‘Encrypted Data Key Material’ Characteristic on the IUT is readable by the Lower Tester when the connection is authenticated and authorized. 

- Reference 

   - [18] 12.6 

- 

- Initial Condition 

- The Lower Tester is a GATT client. 

- The Upper Tester is a GATT server that has implemented the GATT service discovery procedures. 

   - The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT server. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The IUT and the Lower Tester are authenticated and have exchanged the Session Key and IV. 

- 

## Test Procedure 

1. The Lower Tester performs a GATT service discovery for the GAP Service UUID. 

2. The IUT responds with a GATT service discovery response for the GAP Service UUID with the Handles Information List. 

3. The Lower Tester performs a GATT characteristic discovery by UUID. 

4. The IUT responds with a GATT characteristic discovery by UUID response with an attribute Data List that contains the Encrypted Data Key Material Handle. 

5. The Lower Tester performs a GATT characteristic read value with the Encrypted Data Key Material Handle from Step 4. 

6. The IUT sends an authorization request to the Upper Tester. 

7. The Upper Tester orders the IUT to authorize the Lower Tester. 

8. The IUT responds to the request in Step 5 with a GATT characteristic read value response with the Encrypted Data Key Material value. 

9. The Lower Tester performs a GATT characteristic write value with the Encrypted Data Key Material Handle from Step 4 and 24 octets of random values. 

10. The IUT responds with an ATT error response with Error Code > 0. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **274 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [363 x 299] intentionally omitted <==**

_Figure 4.181: GAP/GAT/BV-09-C [Encrypted Data Key Material, Authenticated and Authorized] MSC_ 

- Expected Outcome 

## Pass verdict 

In Step 8, the IUT responds with the Encrypted Data Key Material value. 

In Step 10, the IUT sends an ATT Error response to the Lower Tester. 

## **GAP/GAT/BV-10-C [Encrypted Data Key Material, Not Authenticated]** 

- Test Purpose 

Verify that the GAP ‘Encrypted Key Data Material’ Characteristic on the IUT cannot be read by the Lower Tester when the connection is not authenticated. 

- Reference 

   - [18] 12.6 

- 

- Initial Condition 

- The Lower Tester is a GATT client. 

- The Upper Tester is a GATT server that has implemented the GATT service discovery procedures. 

- The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT Server. 

- A physical link is established between the IUT and the Lower Tester. 

- The IUT and the Lower Tester are not authenticated. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **275 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Lower Tester performs a GATT service discovery for the GAP Service UUID. 

   2. The IUT responds with a GATT service discovery response for the GAP Service UUID with the Handles Information List. 

   3. The Lower Tester performs a GATT characteristic discovery by UUID. 

   4. The IUT responds with a GATT characteristic discovery by UUID response with an attribute Data List that contains the Encrypted Data Key Material Handle. 

   5. The Lower Tester performs a GATT characteristic read value with the Encrypted Data Key Material Handle from Step 4. 

   6. The IUT responds with an ATT Error response with Error Code > 0. 

**==> picture [362 x 214] intentionally omitted <==**

_Figure 4.182: GAP/GAT/BV-10-C [Encrypted Data Key Material, Not Authenticated] MSC_ 

- Expected Outcome 

## Pass verdict 

In Step 6, the IUT sends an ATT Error response to the Lower Tester. 

**GAP/GAT/BV-11-C [Encrypted Data Key Material, Not Authorized]** 

- Test Purpose 

Verify that the GAP ‘Encrypted Key Data Material’ Characteristic on the IUT cannot be read by the Lower Tester when the connection is not authorized. 

- Reference 

   - [18] 12.6 

- 

- Initial Condition 

- The Lower Tester is a GATT client. 

- The Upper Tester is a GATT server that has implemented the GATT service discovery procedures. 

- The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT Server. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **276 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   - A physical link is established between the IUT and the Lower Tester. 

   - The IUT and the Lower Tester are authenticated but not authorized. 

- Test Procedure 

   1. The Lower Tester performs a GATT service discovery for the GAP Service UUID. 

   2. The IUT responds with a GATT service discovery response for the GAP Service UUID with the Handles Information List. 

   3. The Lower Tester performs a GATT characteristic discovery by UUID. 

   4. The IUT responds with a GATT characteristic discovery by UUID response with an attribute Data List that contains the Encrypted Data Key Material Handle. 

   5. The Lower Tester performs a GATT characteristic read value with the Encrypted Data Key Material Handle from Step 4. 

   6. The IUT sends an authorization request to the Upper Tester. 

   7. The Upper Tester orders the IUT not to authorize the Lower Tester. 

   8. The IUT responds to the request in Step 5 with an ATT Error Response. 

**==> picture [364 x 235] intentionally omitted <==**

_Figure 4.183: GAP/GAT/BV-11-C [Encrypted Data Key Material, Not Authorized] MSC_ 

- Expected Outcome 

## Pass verdict 

In Step 8, the IUT sends an ATT Error response to the Lower Tester. 

## **4.7.7.1.1 Discover GAP characteristic** 

- Test Purpose 

Verify that the IUT properly implements the GAP characteristic. 

- Reference 

[18] 12 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **277 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The Lower Tester is a GATT Client. 

   - The IUT is a GATT Server. 

   - A physical link is established between the IUT and the Lower Tester. 

   - The IUT is not bonded or paired with the Lower Tester. 

   - The IUT has the Authorization and Authentication for GATT attributes specified in Table 4.35. 

   - The IUT is discoverable. 

- Test Case Configuration 

|**Test Case**|**Authorization**<br>**and**<br>**Authentication**|**Characteristic**|**Perform**<br>**Step 6**|**Characteristic**<br>**Value**|
|---|---|---|---|---|
|GAP/GAT/BV-04-C<br>[Discover GAP<br>Characteristic, Peripheral<br>Preferred Connection<br>Parameters Characteristic]|Any required to<br>read Peripheral<br>Preferred<br>Connection<br>Parameters|Peripheral<br>Preferred<br>Connection<br>Parameters|Yes|8 octets|
|GAP/GAT/BV-12-C<br>[Discover GAP<br>Characteristic, LE GATT<br>Security Levels<br>Characteristic]|None|LE GATT<br>Security Levels|Yes|Even number<br>of octets; each<br>pair of octets<br>corresponds to<br>a valid and<br>properly<br>formatted<br>security mode<br>and level for<br>that mode|
|GAP/GAT/BV-16-C<br>[Discover GAP<br>Characteristic, Device<br>Name]|None|Device Name|No|1 or more<br>octets|
|GAP/GAT/BV-17-C<br>[Discover GAP<br>Characteristic, Appearance]|None|Appearance|No|2 octets|
|GAP/GAT/BV-18-C<br>[Discover GAP<br>Characteristic, Central<br>Address Resolution]|None|Central<br>Address<br>Resolution|Yes|1 octet with the<br>value 0x00 or<br>0x01|
|GAP/GAT/BV-19-C<br>[Discover GAP<br>Characteristic, Resolvable<br>Private Address Only]|None|Resolvable<br>Private<br>Address Only|Yes|1 octet with the<br>value 0x00|



_Table 4.35: Discover GAP Characteristic test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **278 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [361 x 206] intentionally omitted <==**

_Figure 4.184: Discover GAP Characteristic MSC_ 

   1. The Lower Tester performs a GATT Service Discovery for the GAP Service. 

   2. The IUT responds with a GATT Service Discovery Response with the list of handles. 

   3. The Lower Tester performs a GATT Discover Characteristics by UUID for the characteristic specified in Table 4.35. 

   4. The IUT returns one attribute in the Attribute Data list with the characteristic specified in Table 4.35. 

   5. The Lower Tester verifies that the Characteristic Properties has bit 1 (Read) set. 

   6. If this step is required in Table 4.35, then the Lower Tester verified that the Characteristics Properties has bits 2 and 3 (Write Without Response and Write) not set. 

   7. The Lower Tester performs a GATT Read Characteristic Value for the characteristic specified in Table 4.35. 

   8. The IUT responds with a GATT Read Characteristic value response with the values for the characteristic meeting the requirements specified in Table 4.35. 

- Expected Outcome 

## Pass verdict 

In Step 4, the IUT returns only one attribute with the Read bit set in the Characteristic Properties. 

In Step 6, if performed, the Characteristic Properties do not have the Write and Write Without Response bits set. 

In Step 8, the IUT returns a value that meets the specified requirements. 

## **4.7.7.1.2 Writeable characteristic** 

- Test Purpose 

Verify that an IUT can support a writeable characteristic. 

- Reference 

   - [4] 12 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **279 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - A physical link is established between the IUT and the Lower Tester. 

   - The Lower Tester knows the handle and the current value of the Characteristic specified in Table 4.36, after executing the procedure defined in Section 4.2.6. 

   - The characteristic declaration includes either the Write (0x04) or Write Without Response (0x08) characteristic properties value, or both. 

- Test Case Configuration 

|**Test Case**|**Characteristic**|
|---|---|
|GAP/GAT/BV-05-C[Writeable Characteristic, Device Name]|Device Name|
|GAP/GAT/BV-06-C[Writeable Characteristic, Appearance]|Appearance|



_Table 4.36: LE Discover Writeable Characteristics test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **280 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [361 x 439] intentionally omitted <==**

_Figure 4.185: Writeable Characteristic MSC_ 

1. The Lower Tester sends an ATT_WRITE_CMD with the handle and new value of the Characteristic specified in Table 4.36. 

2. The Lower Tester sends an ATT_READ_REQ to the IUT with the handle sent in Step 1. 

3. The IUT sends an ATT_READ_RSP to the Lower Tester. If the handle and value are those sent in Step 1, the test ends with a Pass verdict. 

4. The Lower Tester sends an ATT_WRITE_REQ with the handle and new value of the Characteristic specified in Table 4.36. 

5. Perform either Alternative 5A or 5B depending on the IUT response: 

   - Alternative 5A: The IUT responds with an ATT_ERROR_RSP with the error code 0x05 “Insufficient Authentication”: 

      - 5A.1 The Lower Tester elevates the authentication or security level. 

      - 5A.2 Return to Step 4. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **281 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

Alternative 5B: The IUT responds with an ATT_WRITE_RSP with the handle and value sent in Steps 1 and 4: 

   - 5B.1 The Lower Tester sends an ATT_READ_REQ to the IUT with the handle sent in Steps 1 and 4. 

   - 5B.2 The IUT sends an ATT_READ_RSP to the Lower Tester with the handle and value sent in Steps 1 and 4. 

- Expected Outcome 

## Pass verdict 

In Step 3 or Step 5B.2, the IUT sends the handle and new value of the characteristic specified in Table 4.36. 

## Fail verdict 

In Step 5, the IUT responds with any PDU or PDU contents other than those specified in the two options. 

## **4.7.8 Periodic Advertising modes and procedures** 

## **4.7.8.1 Periodic Advertising Synchronizability mode** 

- **4.7.8.1.1 Periodic Advertising Synchronizability mode – Broadcaster role** 

- Test Purpose 

Verify the IUT in Periodic Advertising Synchronizability mode in the Broadcaster role where the Lower Tester, in the Observer role, performs the Periodic Advertising Synchronization Establishment procedure using extended advertising events, without listening for periodic advertising data. 

- Reference 

[12] 9.5.1 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PASM/BV-01-C|Periodic Advertising|
|GAP/PADV/PASM/BV-02-C|Periodic Advertisingwith Responses|



_Table 4.37: Periodic Advertising Synchronizability mode – Broadcaster role test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **282 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [305 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Periodic<br>Advertising<br>Synchronization<br>Establishment  Enter Periodic Advertising<br>Procedure Synchronizability Mode<br>Periodic Advertising<br>Synchronization Information<br>Periodic Advertising<br>Synchronization Information<br>**----- End of picture text -----**<br>


_Figure 4.186: Periodic Advertising Synchronizability mode – Broadcaster role MSC_ 

   1. The Upper Tester orders the IUT to enter Periodic Advertising Synchronizability mode. 

   2. The Lower Tester performs the Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising data for the Periodic Advertising Type specified in Table 4.37 and receives periodic advertising synchronization information. 

- 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives periodic advertising synchronization information sent by the IUT. 

The IUT stays in periodic advertising synchronizability mode for at minimum one extended advertising event. 

- Notes 

Since the periodic advertising synchronization information transmission is not a reliable transmission method, multiple periodic advertising synchronization information packets may need to be sent to verify compliance. 

## **4.7.8.2 Periodic Advertising mode** 

- **4.7.8.2.1 Periodic Advertising mode – Broadcaster role** 

- Test Purpose 

Verify the IUT in Periodic Advertising mode in the Broadcaster role where the Lower Tester, in the Observer role, synchronizes and listens for periodic advertising. 

- Reference 

   - [12] 9.5.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The periodic advertising data in Periodic Advertising mode for the IUT is specified in the TSPX_periodic_advertising_data IXIT value. 

   - The Lower Tester has synchronization information for the IUT’s periodic advertising. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **283 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PAM/BV-01-C|Periodic Advertising|
|GAP/PADV/PAM/BV-02-C|Periodic Advertisingwith Responses|



_Table 4.38: Periodic Advertising Synchronizability mode – Broadcaster role test cases_ 

- Test Procedure 

**==> picture [304 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Synchronize<br>and Scan for<br>Periodic  Enter Periodic Advertising Mode<br>Advertising<br>Periodic Advertising Event<br>Periodic Advertising Event<br>**----- End of picture text -----**<br>


_Figure 4.187: Periodic Advertising mode – Broadcaster role MSC_ 

   1. The Upper Tester orders the IUT to enter Periodic Advertising mode using the Periodic Advertising Type in Table 4.38 and the specified periodic advertising data. 

   2. The Lower Tester synchronizes and receives periodic advertising events. 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives periodic advertising events sent by the IUT. 

The Lower Tester receives the specified periodic advertising data sent by the IUT. 

- Notes 

Since the periodic advertising is not a reliable transmission method, multiple periodic advertising packets may need to be sent to verify compliance. 

- **4.7.8.3 Periodic Advertising Synchronization Establishment procedure** 

- **4.7.8.3.1 Periodic Synchronization Establishment procedure using extended advertising events without listening for Periodic Advertising – Observer role** 

- Test Purpose 

Verify that the IUT in the Observer role performs the Periodic Synchronization Establishment procedure using extended advertising events and does not listen for periodic advertising events. 

- Reference 

   - [12] 9.5.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **284 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PASE/BV-01-C|Periodic Advertising|
|GAP/PADV/PASE/BV-07-C|Periodic Advertisingwith Responses|



_Table 4.39: Periodic Synchronization Establishment procedure using extended advertising events without listening for Periodic Advertising – Observer role test cases_ 

- Test Procedure 

**==> picture [302 x 165] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Periodic<br>Advertising<br>Synchronizability<br>Perform Periodic Advertising<br>Mode<br>Synchronization Establishment<br>Procedure<br>Periodic Advertising<br>Synchronization Information<br>Periodic Advertising<br>Synchronization Information<br>**----- End of picture text -----**<br>


**==> picture [159 x 50] intentionally omitted <==**

_Figure 4.188: Periodic Synchronization Establishment procedure using extended advertising events without listening for Periodic Advertising – Observer role MSC_ 

   1. The Lower Tester enters Periodic Advertising Synchronizability mode and begins transmitting periodic advertising synchronization information with the Periodic Advertising Type specified in Table 4.39. 

   2. The Lower Tester enters Periodic Advertising mode and begins transmitting periodic advertising events. 

   3. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising events. 

   4. The Upper Tester receives periodic advertising synchronization information from the IUT. 

   5. The Upper Tester does not receive periodic advertising reports from the IUT. 

- 

- Expected Outcome 

## Pass verdict 

The IUT receives the periodic advertising synchronization information sent from the Lower Tester and reports it to the Upper Tester. 

The IUT does not report periodic advertising events to the Upper Tester. 

- 

- Notes 

Since the periodic advertising synchronization information transmission is not a reliable transmission method, multiple periodic advertising synchronization information packets may need to be sent to verify compliance. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **285 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.7.8.3.2 Periodic Synchronization Establishment procedure using extended advertising events listening for Periodic Advertising – Observer role** 

- Test Purpose 

Verify that the IUT in the Observer role performs the Periodic Synchronization Establishment procedure using extended advertising events and listens for periodic advertising events. 

- Reference [12] 9.5.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The periodic advertising data in Periodic Advertising mode for the Lower Tester is specified in the TSPX_periodic_advertising_data IXIT value. 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PASE/BV-02-C|Periodic Advertising|
|GAP/PADV/PASE/BV-08-C|Periodic Advertisingwith Responses|



_Table 4.40: Periodic Synchronization Establishment procedure using extended advertising events listening for Periodic Advertising – Observer role test cases_ 

- Test Procedure 

**==> picture [301 x 249] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Periodic<br>Advertising<br>Synchronizability<br>Mode<br>Periodic<br>Advertising Mode<br>Perform Periodic Advertising<br>Synchronization Establishment<br>Procedure<br>Periodic Advertising<br>Synchronization Information<br>Periodic Advertising<br>Synchronization Information<br>Periodic Advertising Event<br>**----- End of picture text -----**<br>


**==> picture [182 x 43] intentionally omitted <==**

_Figure 4.189: Periodic Synchronization Establishment procedure using extended advertising events listening for Periodic Advertising – Observer role MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **286 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Lower Tester enters Periodic Advertising Synchronizability mode and begins transmitting periodic advertising synchronization information with the Periodic Advertising Type specified in Table 4.40. 

   2. The Lower Tester enters Periodic Advertising mode and begins transmitting periodic advertising events. 

   3. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Establishment procedure for the Periodic Advertising Type specified in Table 4.40 and to listen for periodic advertising events. 

   4. The Upper Tester receives periodic advertising synchronization information from the IUT. 

   5. The Upper Tester receives periodic advertising reports with periodic advertising data from the IUT. 

- Expected Outcome 

## Pass verdict 

The IUT receives the periodic advertising synchronization information sent from the Lower Tester and reports it to the Upper Tester. 

The IUT synchronizes and receives the periodic advertising events from the Lower Tester and reports the periodic advertising events and the periodic advertising data to the Upper Tester. 

- Notes 

Since the periodic advertising is not a reliable transmission method, multiple periodic advertising packets may need to be sent to verify compliance. 

- **4.7.8.3.3 Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising – Peripheral role** 

- Test Purpose 

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection does not listen for periodic advertising events in the Peripheral role. 

- Reference 

   - [14] 9.5.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PASE/BV-03-C|Periodic Advertising|
|GAP/PADV/PASE/BV-09-C|Periodic Advertisingwith Responses|



_Table 4.41: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising – Peripheral role test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **287 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [304 x 290] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Establish connection<br>Periodic Advertising Event<br>Perform Periodic Advertising<br>Synchronization Establishment<br>Procedure Over the LE<br>Connection<br>Periodic Advertising<br>Synchronization<br>Information<br>Periodic Advertising Event<br>Upper Tester expects not to receive<br>periodic advertising report<br>Terminate connection<br>**----- End of picture text -----**<br>


_Figure 4.190: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising – Peripheral role MSC_ 

   1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Peripheral role. 

   2. The Lower Tester enters Periodic Advertising mode and begins transmitting periodic advertising events. 

   3. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.41 without listening for periodic advertising events. 

   4. The Lower Tester executes the Periodic Advertising Synchronization Transfer procedure over the LE connection with the Periodic Advertising Type specified in Table 4.41. 

   5. The Upper Tester receives periodic advertising synchronization information from the IUT. 

   6. The Upper Tester does not receive periodic advertising reports from the IUT. 

   7. Terminate the connection between the IUT and the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT receives the periodic advertising synchronization information sent from Lower Tester and reports it to the Upper Tester. 

The IUT does not report periodic advertising events to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **288 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.7.8.3.4 Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising – Peripheral role** 

- Test Purpose 

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection listens for periodic advertising events in the Peripheral role. 

- Reference [14] 9.5.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PASE/BV-04-C|Periodic Advertising|
|GAP/PADV/PASE/BV-10-C|Periodic Advertisingwith Responses|



_Table 4.42: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising – Peripheral role test cases_ 

- Test Procedure 

**==> picture [303 x 276] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Establish connection<br>Periodic Advertising Event<br>Perform Periodic Advertising<br>Synchronization Establishment<br>Procedure Over the LE<br>Connection<br>Periodic Advertising<br>Synchronization Information<br>Terminate connection<br>**----- End of picture text -----**<br>


_Figure 4.191: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising – Peripheral role MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **289 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Peripheral role. 

   2. The Lower Tester enters Periodic Advertising mode and begins transmitting periodic advertising events. 

   3. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.42 without listening for periodic advertising events. 

   4. The Lower Tester executes the Periodic Advertising Synchronization Transfer procedure over the LE connection with the Periodic Advertising Type specified in Table 4.42. 

   5. The Upper Tester receives periodic advertising synchronization information from the IUT. 

   6. The Upper Tester receives periodic advertising reports with periodic advertising data from the IUT. 

   7. Terminate the connection between the IUT and the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT receives the periodic advertising synchronization information sent from the Lower Tester and reports it to the Upper Tester. 

The IUT synchronizes and receives the periodic advertising events from the Lower Tester and reports the periodic advertising events and the periodic advertising data to the Upper Tester. 

- Notes 

Since the periodic advertising is not a reliable transmission method, multiple periodic advertising packets may need to be sent for reliable test results. 

- **4.7.8.3.5 Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising – Central role** 

- Test Purpose 

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection does not listen for periodic advertising events in the Central role. 

- Reference 

   - [14] 9.5.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PASE/BV-05-C|Periodic Advertising|
|GAP/PADV/PASE/BV-11-C|Periodic Advertisingwith Responses|



_Table 4.43: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising – Central role test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **290 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [304 x 287] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Establish connection<br>Periodic Advertising Event<br>Perform Periodic Advertising<br>Synchronization Establishment<br>Procedure Over the LE<br>Periodic Advertising  Connection<br>Synchronization Information<br>Periodic Advertising Event<br>Upper Tester expects not to receive<br>periodic advertising report<br>Terminate connection<br>**----- End of picture text -----**<br>


_Figure 4.192: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising – Central role MSC_ 

   1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Central role. 

   2. The Lower Tester enters Periodic Advertising mode and begins transmitting periodic advertising events. 

   3. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.43 without listening for periodic advertising events. 

   4. The Lower Tester executes the Periodic Advertising Synchronization Transfer procedure over the LE connection with the Periodic Advertising Type specified in Table 4.43. 

   5. The Upper Tester receives periodic advertising synchronization information from the IUT, but no periodic advertising reports. 

   6. Terminate the connection between the IUT and the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT receives the periodic advertising synchronization information sent from the Lower Tester and reports it to the Upper Tester. 

The IUT does not report periodic advertising events to the Upper Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **291 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- **4.7.8.3.6 Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising – Central role** 

- Test Purpose 

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection listens for periodic advertising events in the Central role. 

- Reference [14] 9.5.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PASE/BV-06-C|Periodic Advertising|
|GAP/PADV/PASE/BV-12-C|Periodic Advertisingwith Responses|



_Table 4.44: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising – Central role test cases_ 

- Test Procedure 

**==> picture [305 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Establish connection<br>Periodic Advertising Event<br>Perform Periodic Advertising<br>Synchronization Establishment<br>Procedure Over the LE<br>Periodic Advertising  Connection<br>Synchronization<br>Information<br>Periodic Advertising<br>Synchronization Information<br>Terminate connection<br>**----- End of picture text -----**<br>


_Figure 4.193: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising – Central role MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **292 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Central role. 

   2. The Lower Tester enters Periodic Advertising mode and begins transmitting periodic advertising events. 

   3. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.44, listening for periodic advertising events. 

   4. The Lower Tester executes the Periodic Advertising Synchronization Transfer procedure over the LE connection with the Periodic Advertising Type specified in Table 4.44. 

   5. The Upper Tester receives periodic advertising synchronization information from the IUT. 

   6. The Upper Tester receives periodic advertising reports with periodic advertising data from the IUT. 

   7. Terminate the connection between the IUT and the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT receives the periodic advertising synchronization information sent from the Lower Tester and reports it to the Upper Tester. 

The IUT synchronizes and receives the periodic advertising events from the Lower Tester and reports the periodic advertising events and the periodic advertising data to the Upper Tester. 

- Notes 

Since the periodic advertising is not a reliable transmission method, multiple periodic advertising packets may need to be sent to obtain reliable test results. 

## **4.7.8.4 Periodic Advertising Synchronization Transfer procedure** 

- **4.7.8.4.1 Periodic Advertising Synchronization Transfer procedure – Peripheral role** 

- Test Purpose 

Verify the IUT performing the Periodic Advertising Synchronization Transfer procedure in the Peripheral role; the Lower Tester, in the Central role, performs the Periodic Advertising Synchronization Establishment procedure over an LE connection. 

- Reference 

[14] 9.5.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PAST/BV-01-C|Periodic Advertising|
|GAP/PADV/PAST/BV-03-C|Periodic Advertisingwith Responses|



_Table 4.45: Periodic Advertising Synchronization Transfer procedure – Peripheral role test cases_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **293 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [268 x 257] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Establish connection<br>The Upper Tester configures the IUT to<br>enter Periodic Advertising<br>Synchronizability Mode<br>The Lower Tester performs the Periodic<br>Advertising Synchronization Establishment<br>Procedure Over the LE Connection<br>Perform Periodic Advertising<br>Synchronization Transfer<br>Procedure<br>Terminate connection<br>**----- End of picture text -----**<br>


_Figure 4.194: Periodic Advertising Synchronization Transfer procedure – Peripheral role MSC_ 

   1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Peripheral role. 

   2. The Upper Tester configures the IUT to enter Periodic Advertising Synchronizability mode. 

   3. The Lower Tester performs the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.45. 

   4. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Transfer procedure with the Periodic Advertising Type specified in Table 4.45. 

   5. The Lower Tester receives periodic advertising synchronization information from the IUT. 

   6. Terminate the connection between the IUT and the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives periodic advertising synchronization information sent by the IUT. 

- **4.7.8.4.2 Periodic Advertising Synchronization Transfer procedure – Central role** 

- Test Purpose 

Verify the IUT performing the Periodic Advertising Synchronization Transfer procedure in the Central role; the Lower Tester, in the Peripheral role, performs the Periodic Advertising Synchronization Establishment procedure over an LE connection. 

- Reference 

[14] 9.5.4 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **294 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Case Configuration 

|**TCID**|**Periodic Advertising Type**|
|---|---|
|GAP/PADV/PAST/BV-02-C|Periodic Advertising|
|GAP/PADV/PAST/BV-04-C|Periodic Advertisingwith Responses|



_Table 4.46: Periodic Advertising Synchronization Transfer procedure – Central role test cases_ 

- Test Procedure 

**==> picture [269 x 257] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Establish connection<br>The Upper Tester configures the IUT to<br>enter Periodic Advertising<br>Synchronizability Mode<br>The Lower Tester performs the Periodic<br>Advertising Synchronization Establishment<br>Procedure Over the LE Connection<br>Perform Periodic Advertising<br>Synchronization Transfer<br>Procedure<br>Terminate connection<br>**----- End of picture text -----**<br>


_Figure 4.195: Periodic Advertising Synchronization Transfer procedure – Central role MSC_ 

   1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Central role. 

   2. The Upper Tester configures the IUT to enter Periodic Advertising Synchronizability mode. 

   3. The Lower Tester performs the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.46. 

   4. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Transfer procedure with the Periodic Advertising Type specified in Table 4.46. 

   5. The Lower Tester receives periodic advertising synchronization information from the IUT. 

   6. Terminate the connection between the IUT and the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The Lower Tester receives periodic advertising synchronization information sent by the IUT. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **295 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.8.5 Periodic Advertising Connection procedure** 

**GAP/PADV/PAC/BV-01-C [Create connection with synchronized device using the Periodic Advertising Connection procedure, Periodic Advertiser]** 

- Test Purpose 

Verify that the IUT as a periodic advertiser can initiate a Link Layer connection with a synchronized device. 

- Reference 

   - [18] 9.5.5.2 

- Initial Condition 

   - The IUT is in the Link Layer Standby state as a Periodic Advertiser. 

- Test Procedure 

**==> picture [128 x 62] intentionally omitted <==**

**==> picture [84 x 46] intentionally omitted <==**

**==> picture [86 x 41] intentionally omitted <==**

_Figure 4.196: Create connection with synchronized device using the Periodic Advertising Connection procedure, Periodic Advertiser MSC_ 

   1. The Upper Tester orders the IUT to enter Periodic Advertising with Responses mode with valid Periodic Advertising Response Timing Information. 

   2. The Lower Tester synchronizes and receives periodic advertising events. 

   3. The Upper Tester orders the IUT to connect with the Lower Tester using the Periodic Advertising Connection procedure. 

   4. The IUT and the Lower Tester complete a Link Layer connection. 

- 

- Expected Outcome 

## Pass verdict 

In Step 4, the IUT has a Link Layer connection with the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **296 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/PADV/PAC/BV-02-C [Create connection with synchronized device using the Periodic Advertising Connection procedure, Scanner]** 

- Test Purpose 

Verify that the IUT can accept a connection request and create a connection with a periodic advertiser. 

- Reference 

   - [18] 9.5.5.2 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

- Test Procedure 

**==> picture [213 x 151] intentionally omitted <==**

_Figure 4.197: Create connection with synchronized device using the Periodic Advertising Connection procedure, Scanner MSC_ 

   1. The Lower Tester enters Periodic Advertising mode and begins transmitting Periodic Advertising events with Periodic Advertising Response Timing Information. 

   2. The Upper Tester orders the IUT to synchronize with Periodic Advertising events. 

   3. The Lower Tester synchronizes and receives periodic advertising events. 

   4. The Lower Tester sends a connection request to the IUT. 

   5. The IUT accepts the connection request to the Lower Tester. 

   6. The IUT sends a successful connection request event to the Upper Tester. 

   7. The IUT and the Lower Tester complete a Link Layer connection. 

- 

- Expected Outcome 

## Pass verdict 

In Step 7, the IUT has a Link Layer connection with the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **297 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.9 Broadcast Isochronous Streaming modes and procedures** 

## **4.7.9.1 Broadcast Isochronous Synchronization Establishment** 

## **GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment procedure]** 

- Test Purpose 

Verify that the IUT performs the Broadcast Isochronous Synchronization Establishment procedure. 

- Reference 

   - [15] 9.6, 9.6.3 

- Initial Condition 

   - The IUT is in Link Layer state ‘Standby’. 

   - The Lower Tester is in Broadcasting State. 

- Test Procedure 

**==> picture [374 x 198] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower  Upper<br>IUT<br>Tester Tester<br>IUT is in Link Layer state  Standby . Lower Tester is in Broadcasting State.<br>AUX_SYNC_IND PDU<br>(BIGInfo) Synchronize to BIG<br>AUX_SYNC_IND PDU<br>(BIGInfo) Enable ISO Data<br>Broadcast ISO Data<br>Broadcast ISO Data<br>**----- End of picture text -----**<br>


_Figure 4.198: GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment] MSC_ 

   1. The Lower Tester establishes a BIG with a single BIS and begins sending periodic advertising trains with BIGInfo in the ACAD field of AUX_SYNC_IND PDU. 

   2. The Upper Tester orders the IUT to synchronize to the Lower Tester’s BIG. 

   3. The IUT synchronizes to the BIG. 

   4. The Upper Tester enables ISO data. 

   5. The Upper Tester expects the IUT to begin providing isochronous data from the single BIS from the Lower Tester. 

- Expected Outcome 

## Pass verdict 

The IUT synchronizes with the Lower Tester. 

The Upper Tester receives the Broadcast Isochronous Stream data sent by the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **298 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.9.2 Broadcast Isochronous Broadcasting mode** 

**GAP/BIS/BBM/BV-01-C [Broadcast Isochronous Stream Broadcasting mode]** 

- Test Purpose 

Verify the IUT in Broadcast Isochronous Stream Broadcasting mode; the peer device synchronizes and listens for isochronous data payloads. 

- Reference 

   - [15] 9.6.2 

- Initial Condition 

   - The IUT is in Broadcasting State. 

   - The Lower Tester is in Synchronization State. 

- Test Procedure 

**==> picture [339 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower  Upper<br>IUT<br>Tester Tester<br>IUT is in Broadcasting State. Lower Tester is in Synchronization State.<br>AUX_SYNC_IND + ACAD PDU(BIGInfo)<br>Enable ISO Data<br>AUX_SYNC_IND + ACAD PDU(BIGInfo)<br>ISO Data<br>ISO Data Packets<br>**----- End of picture text -----**<br>


_Figure 4.199: GAP/BIS/BBM/BV-01-C [Broadcast Isochronous Stream Broadcasting mode] MSC_ 

   1. The Upper Tester instructs the IUT to create a BIG. 

   2. The Lower Tester receives periodic advertising packets from the IUT containing BIGInfo. 

   3. The Upper Tester enables ISO data on the IUT. 

   4. The Upper Tester begins sending data to the IUT. 

   5. The Lower Tester receives BIS Data Packets from the IUT. 

- Expected Outcome 

## Pass verdict 

The IUT sends isochronous data payloads in Broadcast Isochronous Stream subevents. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **299 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.7.10 Connection Subrating procedure** 

## **4.7.10.1 Connection Subrate Request procedure** 

**GAP/CSUB/CSR/BV-01-C [Connection Subrate Request procedure]** 

- Test Purpose 

Verify that the IUT as a Peripheral performs a subrate request and returns the LE Subrate Change event to the Upper Tester. 

- Reference [17] 9.3.16 

- Initial Condition 

   - The IUT is a Peripheral and in Link Layer state ‘Connected’. 

- Test Procedure 

**==> picture [377 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower  Upper<br>IUT<br>Tester Tester<br>IUT and Lower Tester are connected<br>LE Subrate Request Procedure<br>Connection Subrate Request<br>Connection Subrate Indication<br>LE Subrate Change Event<br>**----- End of picture text -----**<br>


_Figure 4.200: GAP/CSUB/CSR/BV-01-C [Connection Subrate Request procedure] MSC_ 

   1. The Upper Tester orders the IUT to perform the LE Subrate Request procedure. 

   2. The IUT and the Lower Tester exchange connection subrate messages. 

   3. The IUT sends an LE Subrate Change event to the Upper Tester. 

- Expected Outcome 

## Pass verdict 

The IUT sends an LE Subrate Change event to the Upper Tester. 

## **4.7.10.2 Connection Subrate Update procedure** 

## **GAP/CSUB/CSU/BV-01-C [Connection Subrate Update procedure]** 

- Test Purpose 

Verify that the IUT as a Central performs a subrate update procedure and returns the Subrate Update event to the Upper Tester. 

- Reference 

   - [17] 9.3.16 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **300 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT is a Central and in Link Layer state ‘Connected’. 

- Test Procedure 

**==> picture [377 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower  Upper<br>IUT<br>Tester Tester<br>IUT and Lower Tester are connected<br>LE Subrate Update Procedure<br>Connection Subrate Indication<br>LE Subrate Update Event<br>**----- End of picture text -----**<br>


_Figure 4.201: GAP/CSUB/CSU/BV-01-C [Connection Subrate Update procedure] MSC_ 

   1. The Upper Tester orders the IUT to perform the LE Subrate Update procedure. 

   2. The IUT sends a connection subrate indication to the Lower Tester. 

   3. The IUT sends an LE Subrate Update event to the Upper Tester. 

- 

- Expected Outcome 

## Pass verdict 

The IUT sends an LE Subrate Update event to the Upper Tester. 

## **4.7.11 Channel Sounding procedure** 

## **GAP/CS/BV-01-C [Starting Channel Sounding, Initiator]** 

- Test Purpose 

Verify that the Initiator IUT starts Channel Sounding using the Channel Sounding Start procedure. 

- Reference 

   - [19] 9.7.1 

- Initial Condition 

   - The Lower Tester has the Channel Sounding feature bit set. 

   - The Lower Tester and the IUT have completed the encryption procedure with the LE security mode 1 level 2 or higher. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **301 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

**==> picture [395 x 127] intentionally omitted <==**

_Figure 4.202: Starting Channel Sounding, Initiator MSC_ 

   1. The Upper Tester orders the IUT to perform the LE Channel Sounding Start procedure. 

   2. The IUT and the Lower Tester exchange Channel Sounding messages. 

   3. The IUT sends an LE Channel Sounding event to the Upper Tester. 

- Expected Outcome 

## Pass verdict 

The IUT is able to start the Channel Sounding procedure using the Channel Sounding Start procedure. 

## **GAP/CS/BV-02-C [Starting Channel Sounding, Reflector]** 

- Test Purpose 

Verify that the Reflector IUT starts Channel Sounding using the Channel Sounding Start procedure. 

- Reference 

   - [19] 9.7.2 

- Initial Condition 

   - The Lower Tester has the Channel Sounding feature bit set. 

   - The Lower Tester and the IUT have completed the encryption procedure with the LE security mode 1 level 2 or higher. 

- Test Procedure 

**==> picture [395 x 127] intentionally omitted <==**

_Figure 4.203: Starting Channel Sounding, Initiator MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **302 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

   1. The Lower Tester orders the IUT to perform the LE Channel Sounding Start procedure. 

   2. The IUT and the Lower Tester exchange Channel Sounding messages. 

   3. The IUT sends an LE Channel Sounding event to the Upper Tester. 

- Expected Outcome 

## Pass verdict 

The IUT is able to be configured in the Channel Sounding Reflector role and exchange Channel events. 

## **4.8 BR/EDR/LE operational modes and procedures** 

Verify the correct implementation of the BR/EDR/LE devices (devices that support LE and BR/EDR together). 

## **4.8.1 Non-connectable mode** 

## **GAP/DM/NCON/BV-01-C [BR/EDR/LE non-connectable mode]** 

- Test Purpose 

Verify that the IUT can properly handle the non-connectable mode in both BR/EDR and LE physical channels. 

This test case is only valid for a BR/EDR/LE device that supports the Peripheral role. 

- Reference 

   - [4] 13.1.2.1 

- Initial Condition 

   - The IUT is in Link Layer Standby state. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter non-connectable mode. 

   2. For BR/EDR, this means paging scan is disabled on the IUT. 

   3. The Lower Tester verifies that the device is non-connectable in BR/EDR using the BR/EDR connection procedure. 

   4. The Lower Tester verifies that the device is non-connectable in LE using GAP/CONN/NCON/BV01-C [Non-Connectable mode] to GAP/CONN/NCON/BV-03-C [Non-Connectable mode, Limited Discoverable mode] depending on the IUT capability. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **303 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 266] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Non-Connectable Mode<br>BR/EDR connection<br>BR/EDR is non-connectable<br>Reference to GAP/CONN/NCON/BV-01 to BV-03<br>**----- End of picture text -----**<br>


_Figure 4.204: GAP/DM/NCON/BV-01-C [BR/EDR/LE non-connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT passes correspondent non-connectable mode test cases for LE and BR/EDR. 

## **4.8.2 Connectable mode** 

## **GAP/DM/CON/BV-01-C [BR/EDR/LE connectable mode]** 

- Test Purpose 

Verify that the IUT can properly handle the connectable mode in both BR/EDR. 

- Reference 

[4] 13.1.2.2 

- Initial Condition 

   - The IUT is in Link Layer Standby state. 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter connectable mode. 

   2. For BR/EDR, this means page scan is enabled. 

   3. The Lower Tester verifies that the IUT can be connected in BR/EDR using the corresponding connection procedure. 

   4. For this test case, the IUT only has to complete the corresponding test case for connectable mode as a BR/EDR device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **304 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 267] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Connectable Mode<br>BR/EDR connection<br>BR/EDR is connected<br>BR/EDR Disconnection<br>BR/EDR is disconnected<br>**----- End of picture text -----**<br>


_Figure 4.205: GAP/DM/CON/BV-01-C [BR/EDR/LE connectable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester finds the IUT is connectable using the BR/EDR procedure. 

## **4.8.3 Non-bondable mode** 

## **GAP/DM/NBON/BV-01-C [BR/EDR/LE non-bondable mode]** 

- Test Purpose 

Verify that the IUT is non-bondable in both BR/EDR and LE. 

The Lower Tester is a BR/EDR/LE Peripheral device. 

The IUT is a BR/EDR/LE Central Device. 

- Reference 

   - [4] 13.1.3.2 

- 

   - Initial Condition 

   - The IUT is in Link Layer Standby state. 

- 

- Test Procedure 

1. The Upper Tester orders the IUT to enter non-bondable mode. 

2. The Lower Tester verifies that the device is non-bondable in BR/EDR with the corresponding test case procedure GAP/MOD/NBON/BV-02-C [Non-bondable mode, IUT rejects pairing procedure] 

3. The Lower Tester and the IUT are disconnected. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **305 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

4. The Lower Tester advertises itself as LE-only, Peripheral role for the LE “non-bondable” testing part that follows. 

5. The Lower Tester verifies that the device is non-bondable mode in LE using 

GAP/BOND/NBON/BV-01-C [Non-bondable mode – Central as Responder] followed by GAP/BOND/NBON/BV-02-C [Non-bondable mode – Central as Initiator]. 

**==> picture [300 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br> BR/EDR Bonding with “No Bonding”  No-Bonding Mode<br>option<br>BR/EDR is paired but not bonded<br>BR/EDR Disconnection<br>BR/EDR is disconnected<br>GAP/BOND/NBON/BV-01-C<br>GAP/BOND/NBON/BV-02-C<br>**----- End of picture text -----**<br>


_Figure 4.206: GAP/DM/NBON/BV-01-C [BR/EDR/LE non-bondable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester verifies that the IUT supports non-bondable mode correctly for both BR/EDR and LE procedures. 

## **4.8.4 Bondable mode** 

## **GAP/DM/BON/BV-01-C [BR/EDR/LE bondable mode]** 

- Test Purpose 

Verify that the IUT can properly handle the bonding procedure in both BR/EDR and LE as Central role. 

- Reference 

   - [4] 13.1.5 

- 

- Initial Condition 

- The IUT is in Link Layer Standby state. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **306 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester orders the IUT to enter bondable mode. 

   2. The Lower Tester verifies that the device is bondable in BR/EDR using the corresponding test case procedure. 

   3. The Lower Tester has to advertise itself as LE-only, Peripheral role for the LE “bondable” testing part. 

   4. The Lower Tester verifies that the device is bondable in LE using corresponding test case procedures in GAP/BOND/BON/ test group. 

**==> picture [305 x 284] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>BR/EDR Bonding with “Dedicated  Bonding Mode<br>Bonding” option<br>BR/EDR is paired and bonded<br>BR/EDR Disconnection<br>BR/EDR is disconnected<br>GAP/BOND/BON test cases<br>**----- End of picture text -----**<br>


_Figure 4.207: GAP/DM/BON/BV-01-C [BR/EDR/LE bondable mode] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester finds the IUT is bondable using both BR/EDR and LE procedures. 

## **4.8.5 General Discovery procedure** 

**GAP/DM/GIN/BV-01-C [BR/EDR/LE General Discovery – Finding General Discoverable devices]** 

- Test Purpose 

Verify that the IUT performing the General Discovery procedure can discover a BR/EDR/LE device in the General Discovery mode over both BR/EDR and LE. 

Verify that the IUT performing the General Discovery procedure can discover a BR/EDR/LE device in the Limited Discovery mode over both BR/EDR and LE. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **307 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

The IUT is a BR/EDR/LE device as the Central and initiator over BR/EDR and in the Central role over LE. 

The Lower Tester is a BR/EDR/LE device operating as the Peripheral and acceptor over BR/EDR and in the Peripheral role over LE. 

- Reference 

   - [4] 13.2.1 

- Initial Condition 

   - The IUT is in Link Layer Standby state. 

- Test Procedure 

   1. The Lower Tester enters General Discoverable mode; the Lower Tester interleaves General Discoverable mode over BR/EDR and LE. 

   2. The Upper Tester orders the IUT to perform the General Discovery procedure; the IUT verifies that it can discover the Lower Tester over both BR/EDR and LE. 

   3. The Lower Tester enters Limited Discoverable mode; the Lower Tester interleaves Limited Discoverable mode over BR/EDR and LE. 

   4. The Upper Tester orders IUT to perform the General Discovery procedure; the IUT verifies that it can discover the Lower Tester over both BR/EDR and LE. 

**==> picture [305 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Start General Discovery<br>BR/EDR/LE General Discoverable mode.<br>IUT discovers the Lower Tester over BR/EDR and LE<br>BR/EDR/LE Limited Discoverable mode.<br>IUT discovers the Lower Tester over BR/EDR and LE<br>**----- End of picture text -----**<br>


_Figure 4.208: GAP/DM/GIN/BV-01-C [BR/EDR/LE General Discovery – Finding General Discoverable Devices] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **308 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

The IUT discovers the Lower Tester when the Lower Tester is operating in General Discoverable mode and the IUT is performing the General Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 0 and the General Discoverable flag set to 1. 

The IUT discovers the Lower Tester when the Lower Tester is operating in Limited Discoverable mode and the IUT is performing the General Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 1 and the General Discoverable flag set to 0. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify that the Flags AD type presence and setting according to the test pass verdict in any received advertising data. 

## **4.8.6 Limited Discovery procedure** 

**GAP/DM/LIN/BV-01-C [BR/EDR/LE Limited Discovery – Find Limited Discoverable devices]** 

- Test Purpose 

Verify that the IUT performing the Limited Discovery procedure can discover a BR/EDR/LE device in the Limited Discoverable mode over both BR/EDR and LE. 

Verify that the IUT performing the Limited Discovery procedure does not discover a BR/EDR/LE device in the General Discoverable mode over both BR/EDR and LE. 

The IUT is a BR/EDR/LE device performing the Limited Discovery procedure as the Central and initiator over BR/EDR and in the Central role over LE. 

The Lower Tester is a BR/EDR/LE device operating as the Peripheral and acceptor over BR/EDR and in the Peripheral role over LE. 

- Reference 

   - [4] 13.2.2 

- Initial Condition 

   - The IUT is in Link Layer Standby state. 

- Test Procedure 

   1. The Lower Tester enters Limited Discoverable mode; the Lower Tester interleaves Limited Discoverable mode over BR/EDR and LE. 

   2. The Upper Tester orders the IUT to perform the Limited Discovery procedure; the IUT verifies that it can discover the Lower Tester over both BR/EDR and LE. 

   3. The Lower Tester enters General Discoverable mode; the Lower Tester interleaves General Discoverable mode over BR/EDR and LE. 

   4. The Upper Tester orders the IUT to perform the Limited Discovery procedure; the IUT verifies that it does not discover the Lower Tester over both BR/EDR and LE. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **309 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 260] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Start Limited Discovery<br>BR/EDR/LE Limited Discoverable mode.<br>IUT discovers the Lower Tester over BR/EDR and LE<br>BR/EDR/LE General Discoverable mode.<br>IUT does not discover the Lower Tester over BR/<br>EDR or LE<br>**----- End of picture text -----**<br>


_Figure 4.209: GAP/DM/LIN/BV-01-C [BR/EDR/LE Limited Discovery – Find Limited Discoverable Devices] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT discovers the Lower Tester when the Lower Tester is operating in Limited Discoverable mode and the IUT is performing the Limited Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 1 and the General Discoverable flag set to 0. 

The IUT does not discover the Lower Tester when the Lower Tester is operating in General Discoverable mode and the IUT is performing the Limited Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 0 and the General Discoverable flag set to 1. 

- 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

## **4.8.7 Name Discovery procedure** 

## **GAP/DM/NAD/BV-01-C [BR/EDR/LE Name Discovery]** 

- Test Purpose 

Verify that the IUT can properly perform the name discovery procedure for both BR/EDR and LE devices as a Central role. 

The IUT is a BR/EDR/LE device. 

The Lower Tester is a BR/EDR/LE device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **310 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference 

   - [4] 6.3, 13.2.4 

- Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

- Test Procedure 

   1. The Lower Tester is a BR/EDR/LE device. 

   2. The Upper Tester orders the IUT to do Name Discovery of Lower Tester on BR/EDR link as defined in Section 6.3 of [4], which is the BR/EDR standard procedure of HCI command “remote name request”. 

**==> picture [301 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Name Discovery<br>BR/EDR device name discovery “Remote<br>Name Request”<br>IUT properly discovers the device name of the Lower Tester<br>**----- End of picture text -----**<br>


_Figure 4.210: GAP/DM/NAD/BV-01-C [BR/EDR/LE Name Discovery] MSC_ 

- Expected Outcome 

## Pass verdict 

Device name is discovered correctly and passed up to the Upper Tester for verification. 

- Notes 

The IUT first performs the Device Capability Discovery procedure. 

## **GAP/DM/NAD/BV-02-C [LE Name Discovery]** 

- Test Purpose 

Verify that the IUT can properly perform the name discovery procedure for LE devices. 

The IUT is a BR/EDR/LE device. 

The Lower Tester is an LE-only Peripheral device. 

- Reference 

   - [4] 9.2.7 

- Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **311 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

The Upper Tester orders the IUT to do a Name Discovery of the Lower Tester on LE link as defined in Section 9.2.7 of [4], which could be through the GATT profile to access GAP characteristics of “device name.” 

**==> picture [304 x 182] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Name Discovery<br>GATT Profile access to LT’s device name<br>characteristic<br>IUT properly discovers the device name of the Lower Tester<br>**----- End of picture text -----**<br>


_Figure 4.211: GAP/DM/NAD/BV-02-C [LE Name Discovery] MSC_ 

- Expected Outcome 

## Pass verdict 

Device name is discovered correctly and passed up to the Upper Tester for verification. 

## **4.8.8 Link Establishment procedure** 

**GAP/DM/LEP/BV-01-C [BR/EDR/LE and BR/EDR/LE Link Establishment – BR/EDR Transport]** 

- Test Purpose 

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the BR/EDR Transport. 

The IUT is a BR/EDR/LE Peripheral device. 

The Lower Tester is a BR/EDR/LE Central device. 

- Reference 

   - [9] 13.1, 13.3.1 

- 

   - Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

- 

## Test Procedure 

1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode; the IUT is a BR/EDR/LE Peripheral device. 

2. The Lower Tester performs the General Discovery procedure to discover the IUT; the Lower Tester is a BR/EDR/LE Central device. 

3. The Lower Tester performs the Link Establishment procedure to connect to the IUT. 

4. When connected the Lower Tester or the IUT terminates the connection. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **312 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 167] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General  Discovery  Enter General Discoverable<br>Procedure and Connectable Mode<br>Discovers IUT is BR/EDR/LE device<br>Link Establishment<br>Procedure<br>BR/EDR connection establishment<br>Connection Complete<br>Connection complete<br>Terminate connection<br>Terminate Connection<br>Procedure<br>**----- End of picture text -----**<br>


_Figure 4.212: GAP/DM/LEP/BV-01-C [BR/EDR/LE and BR/EDR/LE Link Establishment – BR/EDR Transport] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester discovers the IUT over BR/EDR. 

The Lower Tester verifies that the LE Supported (Controller) bit is set to 1 and the LE Supported (Host) bit is set to 1 in the LMP features. 

The Lower Tester discovers the IUT over LE. 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from IUT during the period that the IUT is in General Discoverable mode and connectable mode. 

In each advertising event received, the advertiser address is set to the address of the IUT. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 0. The Flags AD type is not present in any scan response data received. 

The Lower Tester establishes a BR/EDR connection with the IUT using the received BR/EDR address. 

The Lower Tester or the IUT successfully terminates the connection. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

## **GAP/DM/LEP/BV-06-C [BR/EDR/LE and LE Link Establishment IUT is BR/EDR/LE]** 

- Test Purpose 

Verify IUT compliance to the Link Establishment procedure to connect with an LE-only device. 

The IUT is a BR/EDR/LE* device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **313 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

The Lower Tester is an LE-only* device. 

*LE GAP role is defined as required in the test procedure. 

- Reference 

[9] 13.1, 13.3.1 

- Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

- Test Procedure 

   1. The Lower Tester enters General Discoverable mode and Undirected Connectable mode over LE; the Lower Tester is a LE-Only Peripheral device. 

   2. The Upper Tester orders the IUT to perform the General Discovery procedure to discover the Lower Tester; the IUT is a BR/EDR/LE Central device. 

   3. The Upper Tester orders the IUT to perform the Connection Establishment procedure to connect to the Lower Tester. 

   4. When connected the Lower Tester or the IUT terminates the connection. 

**==> picture [305 x 161] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General  Discoverable  Enter General Discovery<br>Connectable Mode Procedure<br>Discovers LT is LE only device<br>Perform Link Establishment<br>Procedure<br>LE connection establishment<br>Connection Complete<br>Connection Complete<br>Terminate Connection   Terminate connection<br>Procedure<br>**----- End of picture text -----**<br>


_Figure 4.213: GAP/DM/LEP/BV-06-C [BR/EDR/LE and LE Link Establishment IUT is BR/EDR/LE] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives either connectable and scannable undirected advertising events or connectable undirected advertising events from Lower Tester during the period that the Lower Tester is in General Discoverable mode and Undirected Connectable mode. 

In each advertising event received, the advertiser address is set to the address of the Lower Tester. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 1. The Flags AD type is not present in any scan response data received. 

The IUT establishes a connection with the Lower Tester using the received advertiser address. 

The Lower Tester or the IUT successfully terminates the connection. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **314 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/DM/LEP/BV-07-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral – LE Transport]** 

- Test Purpose 

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the LE transport. 

Both the IUT and the Lower Tester are BR/EDR/LE devices. 

- Reference 

   - [9] 13.1 

- 

   - Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

- 

- Test Procedure 

1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode on the LE transport; the IUT is a BR/EDR/LE Peripheral device. 

2. The Lower Tester performs the General Discovery procedure on the LE transport to discover the IUT; the Lower Tester is a BR/EDR/LE Central device. 

3. The Lower Tester performs the Link Establishment procedure on the LE transport to connect to the IUT. 

4. The Lower Tester or the IUT terminates the connection. 

**==> picture [305 x 166] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General  Discovery  Enter General Discoverable<br>Procedure and Connectable Mode<br>Discovers IUT is BR/EDR/LE device<br>Link Establishment<br>Procedure<br>LE connection establishment<br>Connection Complete<br>Connection complete<br>Terminate connection<br>Terminate Connection<br>Procedure<br>**----- End of picture text -----**<br>


_Figure 4.214: GAP/DM/LEP/BV-07-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral – LE Transport] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester discovers the IUT over BR. 

The Lower Tester verifies that the LE Supported (Controller) bit is set to 1 and the LE Supported (Host) bit is set to 1 in the LMP features. 

The Lower Tester discovers the IUT over LE. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **315 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT during the period that the IUT is in General Discoverable mode and connectable mode. 

In each advertising event received, the advertiser address is set to the address of the IUT. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 0. The Flags AD type is not present in any scan response data received. 

The Lower Tester establishes an LE connection with the IUT using the received LE address. 

The Lower Tester or the IUT successfully terminates the connection. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

**GAP/DM/LEP/BV-08-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Peripheral – LE and BR/EDR Transports]** 

- Test Purpose 

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the BR/EDR and LE transports simultaneously. 

Both the IUT and the Lower Tester are BR/EDR/LE* devices. 

- Reference 

   - [9] 13.1.1 

- 

## Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

   - The Lower Tester is using the same address on the LE and BR/EDR transports. 

- 

## Test Procedure 

1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode on both the LE and BR/EDR transports; the IUT is a BR/EDR/LE Peripheral device. 

2. The Lower Tester performs the General Discovery procedure on both the LE and BR/EDR transports to discover the IUT; the Lower Tester is a BR/EDR/LE Central device. 

3. The Lower Tester performs the Link Establishment procedure to connect to the IUT on both the LE and BR/EDR transports. 

4. When connected on both transports the Lower Tester or the IUT terminates the connections. 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **316 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 246] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General  Discovery  Enter General Discoverable<br>Procedure and Connectable Mode<br>Discovers IUT is BR/EDR/LE device<br>LE Link Establishment<br>Procedure<br>LE connection establishment<br>LE Connection  LE Connection Complete<br>complete<br>BR/EDR Link<br>Establishment  Procedure<br>BR/EDR connection establishment<br>BR/EDR Connection  BR/EDR Connection<br>complete Complete<br>Terminate connection<br>Terminate Connection<br>Procedure<br>**----- End of picture text -----**<br>


_Figure 4.215: GAP/DM/LEP/BV-08-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Peripheral – LE and BR/EDR Transports] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester discovers the IUT over BR. 

The Lower Tester verifies that the LE Supported (Controller) bit is set to 1 and the LE Supported (Host) bit is set to 1 in the LMP features. 

The Lower Tester discovers the IUT over LE. 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT during the period that the IUT is in General Discoverable mode and connectable mode. 

In each advertising event received, the advertiser address is set to the address of the IUT. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 0. The Flags AD type is not present in any scan response data received. 

The Lower Tester establishes an LE connection with the IUT using the received LE address. 

The Lower Tester establishes a BR/EDR connection with the IUT using the received BR/EDR address. 

The Lower Tester or the IUT successfully terminates the connections. 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **317 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

**GAP/DM/LEP/BV-09-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Central – LE and BR/EDR Transports]** 

- Test Purpose 

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device on the BR/EDR and LE transports simultaneously. 

Both the IUT and the Lower Tester are BR/EDR/LE devices. 

- Reference 

## [9] 13.1.1 

- 

   - Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

   - The Lower Tester is using the same address on the LE and BR/EDR transports. 

- 

## Test Procedure 

1. The Lower Tester enters General Discoverable mode and connectable mode on both the LE and BR/EDR transports; the Lower Tester is a BR/EDR/LE Peripheral device. 

2. The Upper Tester orders the IUT to perform the General Discovery procedure on both the LE and BR/EDR transports to discover the Lower Tester; the IUT is a BR/EDR/LE Central device. 

3. The Upper Tester orders the IUT to perform the Link Establishment procedure to connect to the Lower Tester on both the LE and BR/EDR transports. 

4. When connected on both transports the Lower Tester or the IUT terminates the connections. 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **318 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [305 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>General  Discoverable  Enter General Discovery<br>Connectable Mode Procedure<br>Discovers LT is BR/EDR/LE device<br>Perform LE Link<br>Establishment Procedure<br>LE connection establishment<br>LE Connection  LE Connection Complete<br>Complete Perform BR/EDR Link<br>Establishment Procedure<br>BR/EDR connection establishment<br>BR/EDR Connection  BR/EDR Connection<br>Complete Complete<br>Terminate Connection   Terminate connections<br>Procedures<br>**----- End of picture text -----**<br>


_Figure 4.216: GAP/DM/LEP/BV-09-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Central – LE and BR/EDR Transports] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT discovers the Lower Tester over BR. 

The IUT verifies that the LE Supported (Controller) bit is set to 1 and the LE Supported (Host) bit is set to 1 in the LMP features. 

The IUT discovers the Lower Tester over LE. 

The IUT receives either connectable and scannable undirected advertising events or connectable undirected advertising events from Lower Tester during the period that the Lower Tester is in General Discoverable mode and connectable mode. 

In each advertising event received, the advertiser address is set to the address of the Lower Tester. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 0. The Flags AD type is not present in any scan response data received. 

The IUT establishes an LE connection with the Lower Tester using the received LE address. 

The IUT establishes a BR/EDR connection with the Lower Tester using the received BR/EDR address. 

The Lower Tester or the IUT successfully terminates the connections. 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **319 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/DM/LEP/BV-10-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Central – LE and BR/EDR Transports]** 

- Test Purpose 

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the BR/EDR and LE transports simultaneously. 

The IUT is a BR/EDR/LE device. 

The Lower Tester is a BR/EDR/LE device. 

- Reference 

   - [9] 13.1.1 

- 

   - Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

   - The Lower Tester is using the same address on the LE and BR/EDR transports. 

- 

- Test Procedure 

1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode on the LE transport. The Upper Tester orders the IUT to perform the General Discovery procedure on the BR/EDR transport. The IUT is a BR/EDR/LE Peripheral device. 

2. The Lower Tester performs the General Discovery procedure on the LE transport to discover the IUT and enters the General Discoverable mode on the BR/EDR transport. The Lower Tester is a BR/EDR/LE Central device. 

3. The Lower Tester performs the Link Establishment procedure on the LE transport to connect to the IUT. 

4. The Upper Tester orders the IUT to perform the Link Establishment procedure on the BR/EDR transport to connect to the Lower Tester. 

5. When connected on both transports the Lower Tester or the IUT terminates the connections. 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **320 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 309] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>LE General  Discovery  Enter LE General<br>Procedure Discoverable and<br>Connectable Mode<br>BR/EDR General   Perform BR/EDR General<br>Discoverable Mode Discovery Procedure<br>Discovers IUT on LE transport<br>Discovers Lower Tester on BR/EDR transport<br>LE Link Establishment<br>Procedure<br>LE connection establishment<br>LE Connection  LE Connection Complete<br>complete<br>Perform BR/EDR Link<br>Establishment Procedure<br>BR/EDR connection establishment<br>BR/EDR Connection  BR/EDR Connection<br>complete Complete<br>Terminate connection<br>Terminate Connection<br>Procedure<br>**----- End of picture text -----**<br>


_Figure 4.217: GAP/DM/LEP/BV-10-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Central – LE and BR/EDR Transports] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT discovers the Lower Tester over BR. 

The Lower Tester verifies that the LE Supported (Controller) bit is set to 1 and the LE Supported (Host) bit is set to 1 in the LMP features. 

The Lower Tester discovers the IUT over LE. 

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from IUT during the period that the IUT is in General Discoverable mode and connectable mode. 

In each advertising event received, the advertiser address is set to the address of the IUT. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 0. The Flags AD type is not present in any scan response data received. 

The IUT establishes a BR/EDR connection with the Lower Tester using the received BR/EDR address. 

The Lower Tester establishes an LE connection with the IUT using the received LE address. 

The Lower Tester or the IUT successfully terminates the connections. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **321 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

- Notes 

“Discover” in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data. 

**GAP/DM/LEP/BV-11-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Peripheral – LE and BR/EDR Transports]** 

- Test Purpose 

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device on the BR/EDR and LE transports simultaneously. 

Both the IUT and the Lower Tester are BR/EDR/LE devices. 

- Reference 

   - [9] 13.1.1 

- 

   - Initial Condition 

   - The IUT is in Link Layer ‘Standby’ state. 

   - The Lower Tester is using the same address on the LE and BR/EDR transports. 

- 

## Test Procedure 

1. The Lower Tester enters General Discoverable mode and connectable mode on the LE transport. The Lower Tester performs the General Discovery procedure on the BR/EDR transport. The Lower Tester is a BR/EDR/LE Peripheral device. 

2. The Upper Tester orders the IUT to perform the General Discovery procedure on the LE physical transport to discover the Lower Tester and enters the General Discoverable mode on the BR/EDR transport. The IUT is a BR/EDR/LE Central device. 

3. The Upper Tester orders the IUT to perform the Link Establishment procedure on the LE physical transport to connect to the Lower Tester. 

4. The Lower Tester performs the Link Establishment procedure on the BR/EDR transport to connect to the IUT. 

5. The Lower Tester or the IUT terminates the connection. 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **322 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [285 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>LE General<br>Discoverable  Perform LE General<br>Connectable Mode Discovery Procedure<br>BR/EDR General   Enter BR/EDR General<br>Discovery Procedure Discoverable Mode<br>Discovers IUT on BR/EDR Transports<br>Discovers Lower Tester on LE Transport<br>Perform LE Link<br>Establishment Procedure<br>LE connection establishment<br>LE Connection<br>LE Connection Complete<br>Complete<br>BR/EDR Link<br>Establishment Procedure<br>BR/EDR connection establishment<br>BR/EDR Connection  BR/EDR Connection<br>Complete Complete<br>Terminate Connection   Terminate connections<br>Procedures<br>**----- End of picture text -----**<br>


_Figure 4.218: GAP/DM/LEP/BV-11-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Peripheral – LE and BR/EDR Transports] MSC_ 

- Expected Outcome 

## Pass verdict 

The Lower Tester discovers the IUT over BR. 

The IUT verifies that the LE Supported (Controller) bit is set to 1 and the LE Supported (Host) bit is set to 1 in the LMP features. 

The IUT discovers the Lower Tester over LE. 

The IUT receives either connectable and scannable undirected advertising events or connectable undirected advertising events from Lower Tester during the period that the Lower Tester is in General Discoverable mode and connectable mode. 

In each advertising event received, the advertiser address is set to the address of the Lower Tester. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 0. The Flags AD type is not present in any scan response data received. 

The IUT establishes an LE connection with the Lower Tester using the received LE address. 

The Lower Tester establishes a BR/EDR connection with the IUT using the received BR/EDR address. 

The Lower Tester or the IUT successfully terminates the connections. 

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **323 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **GAP/DM/LEP/BV-12-C [Generate BR/EDR Link Key from LE LTK, as Initiator]** 

- Test Purpose 

Verify that the LTK generated on the LE transport as an initiator can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device when BR/EDR Secure Connections is supported by both devices. The IUT is the Central device. 

- Reference 

   - [9] 14.1 

- 

## Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester. 

- Test Procedure 

   1. The IUT initiates LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase two (pairing). 

   2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation. 

   3. The IUT terminates the LE connection. 

   4. The IUT performs the BR/EDR Link Establishment procedure and encrypts the link using the derived BR/EDR Link Key. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **324 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 348] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>IUT finds Lower Tester<br>Establishes LE connection<br>Initiate LE Secure<br>SMP Pairing Req. Connections Pairing<br>LE Secure<br>AuthReq.SC=1<br>Connections<br>InitKeyDist.LinkKey=1<br>Phase 1<br>Indicate BR/EDR SMP Pairing Resp.<br>Link Key Generation AuthReq.SC=1<br>RespKeyDist.LinkKey=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption using LTK<br>Derive BR/EDR Link  Derive BR/EDR Link<br>Key Key<br>Terminate LE connection<br>Perform BR/EDR Link<br>Establishment Procedure<br>BR/EDR connection establishment<br>Encryption messages<br>(AES-CCM)<br>**----- End of picture text -----**<br>


_Figure 4.219: GAP/DM/LEP/BV-12-C [Generate BR/EDR Link Key from LE LTK, as Initiator] MSC_ 

- Expected Outcome 

## Pass verdict 

LE Secure Connections Pairing is complete, with an LE encrypted link, and BR/EDR Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport. 

- Notes 

This test procedure requires Secure Connections pairing to occur first on the LE transport. 

## **GAP/DM/LEP/BV-13-C [Upgrade of BR/EDR Link Key Regenerates LTK]** 

- Test Purpose 

Verify that after cross-transport key derivation, upgrading the BR/EDR Link Key causes the LTK to be regenerated. The IUT is the Central device. 

- Reference 

   - [9] 14.1 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **325 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester. 

- Test Procedure 

   1. The IUT initiates unauthenticated LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase two (pairing). 

   2. The state of Link Key bit in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation. 

   3. The IUT terminates the LE connection. 

   4. The IUT performs the BR/EDR Link Establishment procedure and encrypts the link using the derived BR/EDR Link Key. 

   5. The IUT upgrades the security level of the BR/EDR Link Key from unauthenticated to authenticated. 

   6. The IUT performs SMP over BR/EDR. 

   7. The IUT terminates the BR/EDR connection. 

   8. The IUT creates an LE connection with the Lower Tester and encrypts the link using the LTK derived from the authenticated BR/EDR Link Key. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **326 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 518] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>IUT finds Lower Tester<br>Establishes LE connection<br>Initiate LE Secure<br>SMP Pairing Req. Connections Pairing<br>LE Secure<br>AuthReq.SC=1<br>Connections<br>InitKeyDist.LinkKey=1<br>Phase 1<br>Indicate BR/EDR SMP Pairing Resp.<br>Link Key Generation AuthReq.SC=1<br>RespKeyDist.LinkKey=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption using LTK<br>Derive BR/EDR Link  Derive BR/EDR Link<br>Key Key<br>Terminate LE connection<br>Perform BR/EDR Link<br>Establishment Procedure<br>BR/EDR connection establishment<br>Encryption messages<br>(AES-CCM)<br>Upgrade BR/EDR Link Key to Authenticated<br>SMP Pairing Req.<br>AuthReq.SC=0<br>InitKeyDist.EncKey=1<br>SMP Pairing Resp.<br>AuthReq.SC=0<br>RespKeyDist.EncKey=1<br>Derive LE LTK Derive LE LTK<br>Optionally distribute other keys e.g. IRK, CSRK<br>Terminate BR/EDR<br>connection<br>Establish LE connection<br>Encryption messages<br>**----- End of picture text -----**<br>


_Figure 4.220: GAP/DM/LEP/BV-13-C [Upgrade of BR/EDR Link Key Regenerates LTK] MSC_ 

- Expected Outcome 

## Pass verdict 

LE Secure Connections Pairing is complete, with an LE encrypted link, and BR/EDR Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport. The BR/EDR Link Key can be upgraded from unauthenticated to authenticated. The LE link can be encrypted using the LTK derived from the authenticated BR/EDR Link Key. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **327 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **GAP/DM/LEP/BV-14-C [Generate BR/EDR Link Key from LE LTK, as Responder]** 

- Test Purpose 

Verify that the LTK generated on the LE transport as a responder can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device, on a device that supports BR/EDR Secure Connections. The IUT is the Peripheral device. 

- Reference 

   - [9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has been discovered and is connected to by the Lower Tester. 

- Test Procedure 

   1. The Lower Tester initiates LE Secure Connections Pairing with the IUT. They complete Pairing phase one (negotiation) and phase 2 (pairing). 

   2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation. 

   3. The Lower Tester terminates the LE connection. 

   4. The Upper Tester puts the IUT in connectable mode on the BR/EDR transport. 

   5. The Lower Tester establishes a BR/EDR link with the IUT and encrypts the link with the derived BR/EDR Link Key. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **328 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [303 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(initiator) (responder)<br>Lower Tester finds the IUT<br>Establishes LE connection<br>SMP Pairing Req.<br>LE Secure<br>AuthReq.SC=1<br>Connections<br>InitKeyDist.LinkKey=1<br>Phase 1<br>Indicate BR/EDR SMP Pairing Resp.<br>Link Key Generation AuthReq.SC=1<br>RespKeyDist.LinkKey=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption<br>Derive BR Link Key Derive BR Link Key<br>Terminate LE connection<br>Bring IUT in connectable<br>mode<br>BR/EDR Link<br>Establishment<br>Encryption messages<br>(AES-CCM)<br>**----- End of picture text -----**<br>


_Figure 4.221: GAP/DM/LEP/BV-14-C [Generate BR/EDR Link Key from LE LTK, as Responder] MSC_ 

- Expected Outcome 

## Pass verdict 

LE Secure Connections Pairing is complete, with an LE encrypted link, and Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport. 

## **GAP/DM/LEP/BV-15-C [Generate BR/EDR Link Key from LE LTK, as Initiator]** 

- Test Purpose 

Verify that the LTK generated on the LE transport as an initiator can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device which supports BR/EDR Secure Simple Pairing but not BR/EDR Secure Connections. The IUT is the Central device. 

- Reference 

## [9] 14.1 

- 

- Initial Condition 

- The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with LE Secure Connections capabilities but only Secure Simple Pairing for BR/EDR. The IUT has discovered and connected to the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **329 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Test Procedure 

   1. The IUT initiates LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase 2 (pairing). 

   2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation. 

   3. The IUT terminates the LE connection. 

   4. The IUT performs the BR/EDR Link Establishment procedure and encrypts the link using the derived BR/EDR Link Key. 

**==> picture [304 x 353] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>IUT finds Lower Tester<br>Establishes LE connection<br>Initiate LE Secure<br>SMP Pairing Req. Connections Pairing<br>LE Secure<br>AuthReq.SC=1<br>Connections<br>InitKeyDist.LinkKey=1<br>Phase 1<br>Indicate BR/EDR SMP Pairing Resp.<br>Link Key Generation AuthReq.SC=1<br>RespKeyDist.LinkKey=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption using LTK<br>Derive BR/EDR Link  Derive BR/EDR Link<br>Key Key<br>Terminate LE connection<br>Perform BR/EDR Link<br>Establishment Procedure<br>BR/EDR connection establishment<br>Encryption messages<br>(E0)<br>**----- End of picture text -----**<br>


_Figure 4.222: GAP/DM/LEP/BV-15-C [Generate BR/EDR Link Key from LE LTK, as Initiator] MSC_ 

- Expected Outcome 

## Pass verdict 

LE Secure Connections Pairing is complete, with an LE encrypted link, and Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport. 

## **GAP/DM/LEP/BV-16-C [Generate BR/EDR Link Key from LE LTK, as Responder]** 

- Test Purpose 

Verify that the LTK generated on the LE transport as a responder can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device which supports BR/EDR Secure Simple Pairing but not BR/EDR Secure Connections. The IUT is the Peripheral device. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **330 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Reference [9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with LE Secure Connections capabilities but only Secure Simple Pairing for BR/EDR. The IUT has been discovered and is connected to by the Lower Tester. 

- Test Procedure 

   1. The Lower Tester initiates LE Secure Connections Pairing with the IUT. They complete Pairing phase one (negotiation) and phase 2 (pairing). 

   2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation. 

   3. The Lower Tester terminates the LE connection. 

   4. The Upper Tester puts the IUT in connectable mode on the BR/EDR transport. 

   5. The Lower Tester establishes a BR/EDR link with the IUT and encrypts the link with the derived BR/EDR Link Key. 

**==> picture [304 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(initiator) (responder)<br>Lower Tester finds the IUT<br>Establishes LE connection<br>SMP Pairing Req.<br>LE Secure<br>AuthReq.SC=1<br>Connections<br>InitKeyDist.LinkKey=1<br>Phase 1<br>Indicate BR/EDR SMP Pairing Resp.<br>Link Key Generation AuthReq.SC=1<br>RespKeyDist.LinkKey=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption<br>Derive BR/EDR Link  Derive BR/EDR Link<br>Key Key<br>Terminate LE connection<br>Bring IUT in connectable<br>mode<br>BR/EDR Link<br>Establishment<br>Encryption messages<br>(E0)<br>**----- End of picture text -----**<br>


_Figure 4.223: GAP/DM/LEP/BV-16-C [Generate BR/EDR Link Key from LE LTK, as Responder] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **331 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

LE Secure Connections Pairing is complete, with an LE encrypted link, and Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport. 

## **GAP/DM/LEP/BV-17-C [Generate LE LTK from BR/EDR Link Key, as Initiator]** 

- Test Purpose 

Verify that the Link Key generated on the BR/EDR transport as an initiator can be used to generate the LTK for the LE transport in a BR/EDR/LE device. The IUT is the Central device. 

- Reference 

   - [9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester. 

- Test Procedure 

   1. The IUT initiates BR/EDR Secure Connections Pairing with the Lower Tester. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link. 

   2. The IUT then sends an SMP Pairing Request to the Lower Tester on the encrypted BR/EDR link. The Lower Tester replies with an SMP Pairing Response. The two devices derive the LTK, and optionally generate and distribute additional keys. 

   3. The IUT terminates the BR/EDR connection. 

   4. The IUT connects to the Lower Tester on the LE transport and encrypts the link with the derived LTK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **332 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 419] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>IUT finds Lower Tester<br>Establishes BR/EDR connection<br>Initiate BR/EDR Secure<br>Connections Pairing<br>BR/EDR Secure Connections Pairing:<br>Public Key Exchange<br>Authentication stages 1 & 2<br>Link Key generation<br>Authentication and Encryption<br>SMP Pairing Req.<br>LE Secure Connections AuthReq.SC=0<br>Phase 1 on  InitKeyDist.EncKey=1<br>Encrypted BR/EDR SMP Pairing Resp.<br>AuthReq.SC=0<br>RespKeyDist.EncKey=1<br>Derive LE LTK Derive LE LTK<br>Optionally distribute other keys e.g. IRK, CSRK<br>Terminate BR/EDR<br>connection<br>Perform LE Link<br>Establishment Procedure<br>LE connection establishment<br>Encryption messages<br>**----- End of picture text -----**<br>


_Figure 4.224: GAP/DM/LEP/BV-17-C [Generate LE LTK from BR/EDR Link Key, as Initiator] MSC_ 

- Expected Outcome 

## Pass verdict 

BR/EDR Secure Connections Pairing is complete, with a BR/EDR encrypted link, the LE LTK of identical strength as the BR/EDR Link Key has been derived, other keys such as the IRK and CSRK have been optionally distributed. The LE LTK can be used to encrypt the LE connection. The IUT does not initiate pairing on the LE transport. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **333 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **GAP/DM/LEP/BV-18-C [Upgrade of LTK Regenerates BR/EDR Link Key]** 

- Test Purpose 

Verify that after cross-transport key derivation, upgrading the LTK causes the BR/EDR Link Key to be regenerated. The IUT is the Central device. 

- Reference 

   - [9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester. 

- Test Procedure 

   1. The IUT initiates unauthenticated BR/EDR Secure Connections Pairing with the Lower Tester. They complete Pairing phases for public key exchange, authentication, key generation and encryption of the BR/EDR link. 

   2. The IUT then sends an SMP Pairing Request to the Lower Tester on the encrypted BR/EDR link. The Lower Tester replies with an SMP Pairing Response. The two devices derive the LTK, and optionally generate and distribute additional keys. 

   3. The IUT terminates the BR/EDR connection. 

   4. The IUT connects to the Lower Tester on the LE transport and encrypts the link with the derived LTK. 

   5. The IUT upgrades the security level of the LTK from unauthenticated to authenticated. 

   6. The IUT terminates the LE connection. 

   7. The IUT creates BR/EDR connection with the Lower Tester and encrypts the link using the BR/EDR Link Key derived from the authenticated LTK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **334 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [302 x 507] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>IUT finds Lower Tester<br>Establishes BR/EDR connection<br>Initiate BR/EDR Secure<br>Connections Pairing<br>BR/EDR Secure Connections Pairing:<br>Public Key Exchange<br>Authentication stages 1 & 2<br>Link Key generation<br>Authentication and Encryption<br>SMP Pairing Req.<br>LE Secure Connections AuthReq.SC=0<br>Phase 1 on  InitKeyDist.EncKey=1<br>Encrypted BR/EDR SMP Pairing Resp.<br>AuthReq.SC=0<br>RespKeyDist.EncKey=1<br>Derive LE LTK Derive LE LTK<br>Optionally distribute other keys e.g. IRK, CSRK<br>Terminate BR/EDR<br>connection<br>Perform LE Link<br>Establishment Procedure<br>LE connection establishment<br>Encryption messages<br>Upgrade LTK to Authenticated<br>Derive BR/EDR Link  Derive BR/EDR Link<br>Key Key<br>Terminate LE<br> connection<br>Establish BR/EDR<br>Encryption messages connection<br>**----- End of picture text -----**<br>


_Figure 4.225: GAP/DM/LEP/BV-18-C [Upgrade of LTK Regenerates BR/EDR Link Key] MSC_ 

- Expected Outcome 

## Pass verdict 

BR/EDR Secure Connections Pairing is complete, with a BR/EDR encrypted link, the LE LTK of identical strength as the BR/EDR Link Key has been derived, other keys such as the IRK and CSRK have been optionally distributed. The LE LTK can be used to encrypt the LE connection. The IUT does not initiate pairing on the LE transport. The LTK can be upgraded from unauthenticated to authenticated. The BR/EDR link can be encrypted using the Link Key derived from the authenticated LTK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **335 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **GAP/DM/LEP/BV-19-C [Generate LE LTK from BR/EDR Link Key, as Responder]** 

- Test Purpose 

Verify that the Link Key generated on the BR/EDR transport as a responder can be used to generate the LTK for the LE transport in a BR/EDR/LE device. The IUT is the Peripheral device. 

- Reference 

[9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester has discovered and connected with the IUT over BR/EDR. 

- Test Procedure 

   1. The Lower Tester initiates BR/EDR Secure Connections Pairing with the IUT. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link. 

   2. The Lower Tester then sends an SMP Pairing Request on the encrypted BR/EDR link. The IUT replies with an SMP Pairing Response. The two devices derive the LTKand optionally generate and distribute other keys. 

   3. The Lower Tester terminates the BR/EDR connection. 

   4. The Upper Tester puts the IUT in connectable mode on the LE transport. 

   5. The Lower Tester establishes an LE link with the IUT and encrypts the link with the derived LE LTK. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **336 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 367] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(initiator) (responder)<br>Lower Tester finds the IUT<br>Establishes BR/EDR connection<br>BR/EDR Secure Connections Pairing:<br>Public Key Exchange<br>Authentication stages 1 & 2<br>Link Key generation<br>Authentication and Encryption<br>SMP Pairing Req.<br>AuthReq.SC=0<br>LE Secure Connections<br>InitKeyDist.EncKey=1<br>Phase 1 on<br>Encrypted BR/EDR SMP Pairing Resp.<br>AuthReq.SC=0<br>RespKeyDist.EncKey=1<br>Derive LE LTK Derive LE LTK<br>Optionally distribute other keys e.g. IRK, CSRK<br>Terminate BR/EDR<br>connection Bring IUT in connectable<br>mode<br>LE Link Establishment<br>Encryption messages<br>**----- End of picture text -----**<br>


_Figure 4.226: GAP/DM/LEP/BV-19-C [Generate LE LTK from BR/EDR Link Key, as Responder] MSC_ 

- Expected Outcome 

## Pass verdict 

BR/EDR Secure Connections Pairing is complete, with a BR/EDR encrypted link, the LE LTK of identical strength as the BR/EDR Link Key has been derived, other keys such as the IRK and CSRK have been optionally distributed. The LE LTK can be used to encrypt the LE connection. The IUT does not initiate pairing on the LE transport. 

## **GAP/DM/LEP/BI-01-C [Do Not Generate LE LTK from BR/EDR P-192 Link Key, as Initiator]** 

- Test Purpose 

Verify that the P-192 Link Key generated on the BR/EDR transport as an initiator is not used to generate the LTK for the LE transport in a BR/EDR/LE device when either the IUT or the Lower Tester or both do not support BR/EDR Secure Connections. The IUT is the Central device. 

- Reference 

[9] 2.3.5.7, 2.4.2.5. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **337 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT supports LE Secure Connections and may or may not support BR/EDR Secure Connections. The Lower Tester supports LE Secure Connections but not BR/EDR Secure Connections. The IUT has discovered and connected to the Lower Tester. 

- Test Procedure 

   1. The IUT initiates BR/EDR Secure Simple Pairing with the Lower Tester. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link. 

   2. The IUT terminates the BR/EDR connection. 

   3. The IUT connects to the Lower Tester on the LE transport. 

   4. The IUT initiates LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase 2 (pairing). 

**==> picture [302 x 449] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(responder) (initiator)<br>IUT finds Lower Tester<br>Establishes BR/EDR connection<br>Initiate BR/EDR Secure<br>Simple Pairing<br>BR/EDR Secure Simple Pairing:<br>Public Key Exchange<br>Authentication stages 1 & 2<br>Link Key generation<br>Authentication and Encryption<br>Terminate BR/EDR<br>connection<br>Perform LE Link<br>Establishment Procedure<br>LE connection establishment<br>SMP Pairing Req.<br>LE Secure AuthReq.SC=1<br>Connections<br>Phase 1<br>SMP Pairing Resp.<br>AuthReq.SC=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2<br>LE transport encryption<br>**----- End of picture text -----**<br>


_Figure 4.227: GAP/DM/LEP/BI-01-C [Do Not Generate LE LTK from BR/EDR P-192 Link Key, as Initiator] MSC_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **338 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

BR/EDR Secure Simple Pairing is complete, with a BR/EDR encrypted link. 

The IUT does not initiate LE Secure Connections Pairing on the BR/EDR transport. 

The IUT and the Lower Tester successfully complete LE Secure Connections Pairing on the LE transport. 

**GAP/DM/LEP/BI-02-C [Do Not Generate LE LTK from P-192 BR/EDR Link Key, as Responder]** 

- Test Purpose 

Verify that the P-192 Link Key generated on the BR/EDR transport as a responder is not used to generate the LTK for the LE transport in a BR/EDR/LE device. The IUT is the Peripheral device. 

- Reference 

   - [9] 2.3.5.7, 2.4.2.5; optional: 2.4.2.1 

- Initial Condition 

- The IUT supports LE Secure Connections. The IUT may or may not support BR/EDR Secure Connections. The Lower Tester support LE Secure Connections but not BR/EDR Secure Connections. The Lower Tester has discovered and connected with the IUT over BR/EDR. 

- Test Procedure 

   1. The Lower Tester initiates BR/EDR Secure Simple Pairing with the IUT. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link. 

   2. The Lower Tester then sends an SMP Pairing Request on the encrypted BR/EDR link. The IUT responds with an SMP Pairing Failed with reason code ‘Cross Transport Key Derivation/Generation not allowed’ (0x0E). 

   3. The Lower Tester terminates the BR/EDR connection. 

   4. The Upper Tester puts the IUT in connectable mode on the LE transport. 

   5. The Lower Tester connects to the IUT on the LE transport. 

   6. The Lower Tester initiates LE Secure Connections Pairing with the IUT. They complete Pairing phase one (negotiation) and phase 2 (pairing). 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **339 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [304 x 388] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT<br>Upper Tester<br>(initiator) (responder)<br>Lower Tester finds the IUT<br>Establishes BR/EDR connection<br>BR/EDR Secure Simple Pairing:<br>Public Key Exchange<br>Authentication stages 1 & 2<br>Link Key generation<br>Authentication and Encryption<br>SMP Pairing Req.<br>AuthReq.SC=1<br>LE Secure Connections<br>InitKeyDist.EncKey=1<br>Phase 1 on<br>Encrypted BR/EDR SMP Pairing Failed<br>Reason=0x0E<br>Terminate BR/EDR<br>connection Bring IUT in connectable<br>mode<br>LE Link Establishment<br>SMP Pairing Req.<br>LE Secure<br>AuthReq.SC=1<br>Connections<br>Phase 1<br>SMP Pairing Resp.<br>AuthReq.SC=1<br>LE Secure Connections Phase 2:<br>Public Key Exchange<br>Authentication Stages 1 & 2Encryption LL messages<br>LE transport encryption<br>**----- End of picture text -----**<br>


_Figure 4.228: GAP/DM/LEP/BI-02-C [Do Not Generate LE LTK from P-192 BR/EDR Link Key, as Responder] MSC_ 

- Expected Outcome 

## Pass verdict 

BR/EDR Secure Simple Pairing is complete, with a BR/EDR encrypted link. 

The IUT rejects the Lower Tester’s request LE Secure Connections Pairing on the BR/EDR transport. 

The IUT and the Lower Tester successfully complete LE Secure Connections Pairing on the LE transport. 

**GAP/DM/LEP/BV-20-C [Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Initiator]** 

- Test Purpose 

Verify that an LE LTK is not overwritten by the LE LTK generated via the cross-transport key derivation procedure using a weaker BR/EDR Link Key. The IUT is the Central device. 

- Reference 

   - [9] 14.1 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **340 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has been discovered and is connected to the Lower Tester over LE. 

- Test Procedure 

**==> picture [338 x 319] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT connected to Lower Tester<br>Initiate LE Secure Connections Pairing<br>MITM<br>LE Secure Connections<br>Pairing Phase 1<br>SMP Pairing Request<br>MITM<br>SMP Pairing Response<br>MITM, Bonding, LinkKey = 0<br>Pairing Phase 2 and Phase 3:<br>Public Key Exchange<br>Authentication Stages 1&2<br>Terminate LE connection<br>IUT disconnected from Lower Tester<br>Initiate BR/EDR Link Establishment<br>No MITM<br>BR/EDR Secure Connection Pairing<br>**----- End of picture text -----**<br>


_Figure 4.229: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Initiator MSC – Page 1 of 2_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **341 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [318 x 233] intentionally omitted <==**

**----- Start of picture text -----**<br>
Optional<br>SMP Pairing Request<br>IUT completes or fails<br>during the pairing<br>procedure<br>Terminate BR/EDR connection<br>IUT disconnected from Lower Tester<br>Initiate LE Connection<br>IUT connected to Lower Tester<br>Link Encryption<br>**----- End of picture text -----**<br>


_Figure 4.230: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Initiator MSC – Page 2 of 2_ 

   1. The Upper Tester directs the IUT to start LE Secure Connections pairing with the Lower Tester. 

   2. The IUT initiates LE Secure Connections Pairing with the Lower Tester with MITM support. 

   3. The Lower Tester responds to the Pairing request with Secure Connections, MITM support, Bonding support, and the LinkKey flag not set. 

   4. They complete Pairing phase one (negotiation), phase two (pairing), and phase three (key distribution). 

   5. The Upper Tester directs the IUT to disconnect the connection with the Lower Tester. 

   6. The IUT terminates the LE connection. 

   7. The Upper Tester directs the IUT to start the BR/EDR Link Establishment procedure with the Lower Tester without MITM support. 

   8. The IUT performs the BR/EDR Link Establishment with Secure Connections and Bonding and without MITM support and initiates BR/EDR Secure Connection Pairing with the Lower Tester. 

   9. The IUT may initiate or skip SMP Pairing. If the IUT initiates SMP Pairing, it may complete or fail during the pairing procedure. 

   10. The IUT establishes a connection with the Lower Tester over BR/EDR. 

   11. The Upper Tester directs the IUT to disconnect the BR/EDR connection with the Lower Tester. 

   12. The Upper Tester directs the IUT to connect to the Lower Tester using LE Secure Connections. 

   13. The IUT initiates a connection to the Lower Tester over LE. 

   14. The IUT and the Lower Tester complete authentication and encryption using the LE LTK from Step 4. 

- 

- Expected Outcome 

## Pass verdict 

The IUT reconnects to the Lower Tester over LE using the existing LE keys exchanged and stored in Step 4. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **342 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/DM/LEP/BV-21-C [Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Responder]** 

- Test Purpose 

Verify that an LE LTK is not overwritten by the LE LTK generated via the cross-transport key derivation procedure using a weaker BR/EDR Link Key. The IUT is the Peripheral device. 

- Reference 

   - [9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has been discovered and is connected to the Lower Tester over LE. 

- Test Procedure 

**==> picture [342 x 335] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Bring IUT into connectable mode<br>on LE Transport<br>IUT connected to Lower Tester On LE Transport<br>SMP Pairing Request<br>MITM, LinkKey = 0<br>SMP Pairing Response<br>MITM, Bonding<br>Pairing Phase 1, Phase 2, Phase 3<br>Terminate LE connection<br>IUT disconnected from Lower Tester<br>Bring IUT into connectable mode<br>on BR/EDR Transport<br>Initiate BR/EDR Link Establishment<br>Bonding, No MITM<br>IUT connected to Lower Tester On BR/EDR Transport<br>BR/EDR SMP Pairing Request<br>EncKey = 1<br>**----- End of picture text -----**<br>


_Figure 4.231: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Responder MSC – Page 1 of 2_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **343 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [319 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
Optional<br>BR/EDR SMP Pairing Response<br>EncKey = 1<br>IUT completes or fails the<br>pairing procedure.<br>Terminate BR/EDR connection<br>IUT disconnected from Lower Tester<br>Bring IUT into connectable mode<br>on LE Transport<br>Initiate LE Connection<br>IUT connected to Lower Tester On LE Transport<br>Authentication and Encryption<br>**----- End of picture text -----**<br>


_Figure 4.232: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Responder MSC – Page 2 of 2_ 

   1. The Upper Tester puts the IUT in connectable mode on the LE transport. 

   2. The Lower Tester initiates LE Secure Connections Pairing with the IUT with MITM support and the LinkKey flag not set. 

   3. The IUT responds to the Pairing request with Secure Connections, MITM support. 

   4. They complete Pairing phase one (negotiation), phase two (pairing), and phase three (key distribution). 

   5. The Lower Tester terminates the LE connection. 

   6. The Upper Tester puts the IUT in connectable mode on the BR/EDR transport. 

   7. The Lower Tester performs the BR/EDR Link Establishment procedure with Bonding and without MITM support. 

   8. The Lower Tester sends an SMP Pairing Request to the IUT with EncKey set to 1. 

   9. The IUT may send an SMP Pairing Failed or an SMP Pairing Response to the Lower Tester. If the IUT sends an SMP Pairing Response, it completes or fails during the pairing procedure. 

   10. The Lower Tester disconnects the BR/EDR connection with the IUT. 

   11. The Upper Tester puts the IUT in connectable mode on the LE transport. 

   12. The Lower Tester initiates a new connection to the IUT over LE. 

   13. The IUT and the Lower Tester complete authentication and encryption using the LE LTK from Step 4. 

- 

- Expected Outcome 

## Pass verdict 

The IUT and the Lower Tester reconnect over LE using the existing keys exchanged and stored in Step 4. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **344 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/DM/LEP/BV-22-C [Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Initiator]** 

- Test Purpose 

Verify that a BR/EDR Link Key is not overwritten by the BR/EDR Link Key generated via the crosstransport key derivation procedure using a weaker LE LTK. The IUT is the Central device. 

- Reference 

   - [9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester. 

- Test Procedure 

**==> picture [341 x 349] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT finds Lower Tester<br>Establishes BR/EDR connection<br>Initiate BR/EDR Secure Connections<br>Pairing<br>BR/EDR Secure Connections Pairing:<br>Public Key Exchange<br>Authentication stages 1&2<br>Link Key generation<br>Authentication and Encryption<br>SMP Pairing Request<br>AuthReq, InitKeyDist<br>SMP Pairing Response<br>AuthReq, InitKeyDist, EncKey=0<br>Terminate BR/EDR connection<br>IUT disconnected from Lower Tester<br>Connect to the Lower Tester over LE<br>IUT connected to Lower Tester<br>Over LE<br>Initiate LE Secure Connections Pairing<br>No MITM<br>**----- End of picture text -----**<br>


_Figure 4.233: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Initiator MSC – Page 1 of 2_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **345 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [336 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
Optional<br>SMP Pairing Request<br>SC: 1, LinkKey: 1<br>IUT completes or fails<br>during the pairing<br>procedure.<br>Terminate LE connection<br>IUT disconnected from Lower Tester<br>Initiate BR/EDR Connection<br>IUT connected to Lower Tester<br>Link Encryption<br>**----- End of picture text -----**<br>


_Figure 4.234: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Initiator MSC – Page 2 of 2_ 

   1. The IUT initiates BR/EDR Secure Connections Pairing with the Lower Tester. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link. 

   2. The IUT then sends an SMP Pairing Request to the Lower Tester on the encrypted BR/EDR link. The Lower Tester replies with an SMP Pairing Response with the EncKey set to 0. 

   3. The IUT terminates the BR/EDR connection. 

   4. The IUT connects to the Lower Tester on the LE transport and pairs without MITM support. 

   5. The IUT may initiate or skip SMP Pairing. If the IUT initiates the SMP Pairing Request, it may complete or fail partway during the pairing procedure. 

   6. The Upper Tester directs the IUT to disconnect the connection with the Lower Tester. 

   7. The Upper Tester directs the IUT to initiate a BR/EDR connection. 

   8. The Upper Tester directs the IUT to encrypt the BR/EDR link. 

   9. The IUT and the Lower Tester complete authentication and encryption using the BR/EDR Link Key from Step 1. 

- Expected Outcome 

## Pass verdict 

The IUT and the Lower Tester reconnect over BR/EDR using the existing keys exchanged and stored in Step 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **346 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**GAP/DM/LEP/BV-23-C [Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Responder]** 

- Test Purpose 

Verify that a BR/EDR Link Key is not overwritten by the BR/EDR Link Key generated via the crosstransport key derivation procedure using a weaker LE LTK. The IUT is the Peripheral device. 

- Reference 

   - [9] 14.1 

- Initial Condition 

   - The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester has discovered and connected with the IUT over BR/EDR. 

- Test Procedure 

**==> picture [341 x 313] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>IUT finds Lower Tester<br>Establishes BR/EDR connection<br>Initiate BR/EDR Secure Connections<br>Pairing<br>BR/EDR Secure Connections Pairing:<br>Public Key Exchange<br>Authentication stages 1&2<br>Link Key generation<br>Authentication and Encryption<br>Terminate BR/EDR connection<br>IUT disconnected from Lower Tester<br>Bring the device to connectable mode on<br>LE<br>IUT connected to Lower Tester<br>over LE Transport<br>SMP Pairing Request<br>No MITM, LinkKey = 1<br>**----- End of picture text -----**<br>


_Figure 4.235: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Responder MSC – Page 1 of 2_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **347 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

**==> picture [330 x 264] intentionally omitted <==**

**----- Start of picture text -----**<br>
Optional<br>SMP Pairing Response<br>SC: 1, LinkKey: 1<br>IUT may complete or fail<br>during the pairing<br>procedure.<br>Terminate LE connection<br>IUT disconnected from Lower Tester<br>Initiate BR/EDR Connection<br>IUT connected to Lower Tester<br>Link Encryption<br>**----- End of picture text -----**<br>


_Figure 4.236: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Responder MSC – Page 2 of 2_ 

   1. The Lower Tester initiates BR/EDR Secure Connections Pairing with the IUT. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link. 

   2. The Lower Tester terminates the BR/EDR connection. 

   3. The Upper Tester puts the IUT in connectable mode on the LE transport. 

   4. The Lower Tester establishes an LE link with the IUT. 

   5. The Lower Tester initiates an SMP Pairing Request without MITM support and LinkKey set to 1. 

   6. The IUT sends an SMP Pairing Response to the Lower Tester and may complete or fail during the pairing procedure. 

   7. The Lower Tester terminates the LE connection with the IUT. 

   8. The Lower Tester initiates a BR/EDR connection with the IUT. They complete encryption using the Link Key from Step 1. 

- 

- Expected Outcome 

## Pass verdict 

The IUT and the Lower Tester reconnect over BR/EDR using the existing keys exchanged and stored in Step 1. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **348 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **4.8.9 Synchronization Establishment – Receiver** 

Verify the correct behavior in this mode. The role of the IUT is broadcast receiver. 

## **GAP/EST/SYNE/BV-01-C [Synchronization Establishment procedure, IUT is Receiver]** 

- Test Purpose 

Verify that the IUT performs a synchronization establishment procedure initiated by itself. The IUT is the connectionless Peripheral broadcast receiver and the Lower Tester is the connectionless Peripheral broadcast transmitter. 

- References 

   - [9] 7.5 

- Initial Condition 

   - The IUT is in Standby state. 

   - The Lower Tester is transmitting Synchronization Train with Interval = 80 ms. 

- Test Procedure 

Receive Synchronization Train on the IUT from the Lower Tester. 

**==> picture [304 x 306] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lower Tester IUT Upper Tester<br>Start<br>Synchronization<br>Train<br>Receive Synchronization Train<br>IUT scans for and receives Synchronization Train<br>From Lower Tester<br>Verify that IUT correctly<br>receives the<br>Synchronization Train from<br>the Lower Tester<br>**----- End of picture text -----**<br>


_Figure 4.237: GAP/EST/SYNE/BV-01-C [Synchronization Establishment procedure, IUT is Receiver] MSC_ 

- Expected Outcome 

## Pass verdict 

The IUT receives the Synchronization Train from the Lower Tester. 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **349 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **5 Test case ma in pp g** 

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document. 

The columns for the TCMT are defined as follows: 

**Item:** Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for GAP [2]. 

If a test case is mandatory within the respective layer, then the y/x reference is omitted. 

**Feature:** A brief, informal description of the feature being tested. 

**Test Case(s):** The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [5]. 

For the purpose and structure of the ICS/IXIT, refer to [5]. 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|**BR/EDR Parameters or BR/EDR/LE Parameters**|||
|GAP 1/1|Verify that the IUT does not respond to inquiry if it is<br>in non-discoverable mode. BR/EDR/LE Name<br>Discovery.|GAP/MOD/NDIS/BV-01-C|
|GAP 1/2|Limited-discoverable mode|GAP/MOD/LDIS/BV-01-C<br>GAP/MOD/LDIS/BV-02-C<br>GAP/MOD/LDIS/BV-03-C|
|GAP 1/3|General-discoverable mode|GAP/MOD/GDIS/BV-01-C<br>GAP/MOD/GDIS/BV-02-C|
|GAP 1/4|Verify that the IUT does not respond to paging if it is<br>in non-connectable mode.|GAP/MOD/NCON/BV-01-C|
|GAP 1/5|Verify that the IUT responds to paging requests if it<br>is in connectable mode.|GAP/MOD/CON/BV-01-C|
|GAP 1/5 AND<br>GAP 1/6 AND<br>GAP 2/7 AND<br>GAP 4/2|Verify that the IUT performs a pairing procedure, if it<br>is in pairable mode.|GAP/MOD/NBON/BV-02-C<br>GAP/MOD/NBON/BV-03-C|
|GAP 1/5 AND<br>GAP 2/5 AND<br>GAP 4/2 AND<br>GAP 4/4|Verify that the IUT in security mode 2 performs a<br>channel establishment procedure.|GAP/SEC/SEM/BV-02-C|
|GAP 3/1|Verify that if general inquiry is initiated by the IUT, it<br>sends for at least TGAP(100) inquiry request<br>messages(GIAC).|GAP/IDLE/GIN/BV-01-C|
|GAP 3/2|Verify that if limited inquiry is initiated by the IUT, it<br>sends for at least TGAP(100) inquiry request<br>messages(LIAC).|GAP/IDLE/LIN/BV-01-C|
|GAP 2/7 AND<br>GAP 3/4 AND<br>GAP 3/3|Device discovery procedure – Central|GAP/IDLE/DED/BV-02-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **350 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 2/7 AND<br>GAP 3/6 AND<br>(GAP 3/1 OR<br>GAP 3/2)|Bonding – Central|GAP/IDLE/BON/BV-02-C|
|GAP 2/7 AND<br>GAP 3/6|Dedicated Bonding|GAP/IDLE/BON/BV-03-C|
|GAP 2/7 AND<br>GAP 3/6 AND<br>GAP 2/8|Dedicated Bonding – Authenticated Link Key|GAP/IDLE/BON/BV-04-C|
|GAP 2/7 AND<br>GAP 3/5|General Bonding|GAP/IDLE/BON/BV-05-C|
|GAP 2/7 AND<br>GAP 3/5 AND<br>GAP 2/8|General Bonding – Authenticated Link Key|GAP/IDLE/BON/BV-06-C|
|GAP 4/1 AND<br>(GAP 3/1 OR<br>GAP 3/2)|Verify that the IUT performs a link establishment<br>procedure, initiated by itself|GAP/EST/LIE/BV-02-C|
|GAP 1/5 AND<br>GAP 2/7 AND<br>GAP 4/2 AND<br>GAP 4/4|Channel establishment, security mode 4|GAP/SEC/SEM/BV-04-C|
|GAP 2/7 AND<br>GAP 2/9 AND<br>GAP 4/3|Channel establishment, security mode 4|GAP/SEC/SEM/BV-08-C|
|GAP 2/7 AND<br>GAP 2/9 AND<br>GAP 4/3 AND<br>GAP 1/6|Channel establishment, security mode 4, Non-<br>bondable mode|GAP/SEC/SEM/BV-05-C<br>GAP/SEC/SEM/BV-50-C|
|GAP 2/7 AND<br>GAP 2/8 AND<br>GAP 4/3 AND<br>GAP 1/6|Channel establishment, security mode 4, Non-<br>bondable mode|GAP/SEC/SEM/BV-06-C<br>GAP/SEC/SEM/BV-07-C<br>GAP/SEC/SEM/BV-51-C<br>GAP/SEC/SEM/BV-52-C|
|GAP 4/3 AND<br>GAP 2/7 AND<br>GAP 2/8 AND<br>GAP 2/9 AND<br>GAP 1/6|Authenticated Link Key, Non-bondable mode|GAP/SEC/SEM/BV-09-C<br>GAP/SEC/SEM/BV-53-C|
|GAP 2/7 AND<br>(GAP 2/8 OR<br>GAP 2/9) AND<br>GAP 1/6|Verify disconnect without encryption, Non-bondable<br>mode|GAP/SEC/SEM/BV-10-C<br>GAP/SEC/SEM/BI-24-C|
|GAP 2/7 AND<br>(GAP 2/8 OR<br>GAP 2/9) AND<br>GAP 1/6 AND<br>L2CAP 2/48a|Verify disconnect without encryption, Credit Based<br>Flow Control, Non-bondable mode|GAP/SEC/SEM/BV-46-C|
|GAP 1/3 AND<br>BB 10/7|Device name during general inquiry|GAP/IDLE/DNDIS/BV-01-C|
|GAP 1/9|Synchronization train|GAP/MOD/NSYN/BV-01-C<br>GAP/MOD/SYN/BV-01-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **351 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 4/7|Verify that the IUT performs a synchronization<br>establishmentprocedure initiated byitself.|GAP/EST/SYNE/BV-01-C|
|**LE Parameters**|||
|(GAP 22/4 OR<br>GAP 32/3) AND<br>GATT 1a/1|Name Discovery procedure GATT Client|GAP/IDLE/NAMP/BV-01-C|
|(GAP 5/3 OR<br>GAP 5/4) AND<br>GATT 1a/3|Name Discovery procedure GATT Server|GAP/IDLE/NAMP/BV-02-C|
|GAP 5/1 OR<br>GAP 5/2 OR<br>GAP 5/3|Non-connectable mode|GAP/CONN/NCON/BV-01-C|
|GAP 23/5 OR<br>GAP 33/6|Terminate Connection procedure|GAP/CONN/TERM/BV-01-C|
|GAP 25/5 OR<br>GAP 35/5|Connection based signing – Sender|GAP/SEC/CSIGN/BV-01-C|
|GAP 25/6 OR<br>GAP 35/6|Connection based signing|GAP/SEC/CSIGN/BV-02-C<br>GAP/SEC/CSIGN/BI-01-C<br>GAP/SEC/CSIGN/BI-02-C<br>GAP/SEC/CSIGN/BI-03-C<br>GAP/SEC/CSIGN/BI-04-C|
|GAP 20a/1 OR<br>GAP 8a/1|AD type – Service UUID|GAP/ADV/BV-01-C|
|GAP 20a/2 OR<br>GAP 8a/2|AD type – Local Name|GAP/ADV/BV-02-C|
|GAP 20a/3 OR<br>GAP 8a/3|AD type – Flags|GAP/ADV/BV-03-C|
|GAP 20a/4 OR<br>GAP 8a/4|AD type – Manufacturer Specific Data|GAP/ADV/BV-04-C|
|GAP 20a/5 OR<br>GAP 8a/5|AD type – TX Power Level|GAP/ADV/BV-05-C|
|GAP 20a/8 OR<br>GAP 8a/8|AD type – Peripheral Connection Interval Range|GAP/ADV/BV-08-C|
|GAP 20a/9 OR<br>GAP 8a/9|AD type – Service Solicitation|GAP/ADV/BV-09-C|
|GAP 20a/10 OR<br>GAP 8a/10|AD type – Service Data|GAP/ADV/BV-10-C|
|GAP 8a/11 OR<br>GAP 20a/11|AD type – Appearance|GAP/ADV/BV-11-C|
|GAP 8a/12 OR<br>GAP 20a/12|AD type – Public Target Address|GAP/ADV/BV-12-C|
|GAP 8a/13 OR<br>GAP 20a/13|AD type – Random Target Address|GAP/ADV/BV-13-C|
|GAP 8a/14 OR<br>GAP 20a/14|AD type Advertising Interval|GAP/ADV/BV-14-C|
|GAP 8a/14a OR<br>GAP 20a/14a|AD type Advertising Interval – Long|GAP/ADV/BV-18-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **352 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 8a/17 OR<br>GAP 20a/17|AD type – URI|GAP/ADV/BV-17-C|
|GAP 8a/18 OR<br>GAP 20a/18|AD type – LE Supported Features|GAP/ADV/BV-19-C|
|(GAP 8a/19 OR<br>GAP 20a/19)<br>AND<br>CORE 1b/61|AD type – Encrypted Data, Advertising, v6.1 or<br>earlier|GAP/ADV/BV-20-C|
|(GAP 8a/19 OR<br>GAP 20a/19)<br>AND<br>CORE 1a/62|AD type – Encrypted Data, Advertising, v6.2 or later|GAP/ADV/BV-21-C|
|GAP 14a/19 OR<br>GAP 30a/19|AD type – Encrypted Data, Scanning|GAP/SCN/BV-01-C|
|**BR/EDR/LE Parameters**|||
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 1/4|BR/EDR/LE non-connectable mode|GAP/DM/NCON/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/3|BR/EDR/LE connectable mode|GAP/DM/CON/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>GAP 1/6|BR/EDR/LE non-bondable mode|GAP/DM/NBON/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>GAP 1/7 AND<br>(GAP 34/2 OR<br>GAP 34/3)|BR/EDR/LE bondable mode|GAP/DM/BON/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>GAP 3/1|BR/EDR/LE General Discovery – Finding General<br>Discoverable Devices in General discovery|GAP/DM/GIN/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>GAP 3/2 AND<br>GAP 32/1|BR/EDR/LE Limited Discovery- Find Limited<br>Discoverable Devices|GAP/DM/LIN/BV-01-C|
|GAP 3/3 AND<br>GAP 0b/1 AND<br>GAP 0b/2|BR/EDR/LE Name Discovery over BR/EDR|GAP/DM/NAD/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>GAP 32/3|BR/EDR/LE Name Discovery over LE|GAP/DM/NAD/BV-02-C|
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 1/5|BR/EDR/LE and BR/EDR/LE Link Establishment –<br>Peripheral|GAP/DM/LEP/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>(GAP 33/2 OR<br>GAP 33/3)|BR/EDR/LE with LE-only Link Establishment –<br>Central|GAP/DM/LEP/BV-06-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **353 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|**LE Broadcaster**|||
|GAP 5/1|Broadcast mode – No Scan Response|GAP/BROB/BCST/BV-01-C|
|GAP 6/2 AND<br>(GAP 8/2 OR<br>GAP 8/4)|Broadcast mode – Scan Response|GAP/BROB/BCST/BV-02-C|
|GAP 11/2|Broadcast mode Resolvable Private Address|GAP/BROB/BCST/BV-03-C|
|GAP 5/1 AND<br>GAP 11/1 AND<br>GAP 11/3|Broadcast mode Non-Resolvable Private Address|GAP/BROB/BCST/BV-04-C|
|GAP 11a/1|Periodic AdvertisingSynchronizabilitymode|GAP/PADV/PASM/BV-01-C|
|GAP 11a/1 AND<br>GAP 11a/3|Periodic Advertising Synchronizability mode, PAwR|GAP/PADV/PASM/BV-02-C|
|GAP 11a/2|Periodic Advertisingmode|GAP/PADV/PAM/BV-01-C|
|GAP 11a/2 AND<br>GAP 11a/3|Periodic Advertising mode, PAwR|GAP/PADV/PAM/BV-02-C|
|GAP 23/9|Periodic AdvertisingConnection|GAP/PADV/PAC/BV-01-C|
|**LE Observer**|||
|GAP 5/2|Observationprocedure, Passive Scanning|GAP/BROB/OBSV/BV-01-C|
|GAP 14/2|Observationprocedure, Active Scanning|GAP/BROB/OBSV/BV-02-C|
|GAP 17/1 AND<br>GAP 14/2 AND<br>(GAP 17/2 OR<br>GAP 17/4)|Observation procedure, Active Scanning Non-<br>Resolvable Private Address or Resolvable Private<br>Address|GAP/BROB/OBSV/BV-05-C|
|GAP 17a/1|Periodic Advertising Synchronization Establishment<br>procedure without listeningforperiodic advertising|GAP/PADV/PASE/BV-01-C|
|GAP 17a/1 AND<br>GAP 11a/3|Periodic Advertising Synchronization Establishment<br>procedure without listening for periodic advertising,<br>PAwR|GAP/PADV/PASE/BV-07-C|
|GAP 17a/2|Periodic Advertising Synchronization Establishment<br>procedure with listeningforperiodic advertising|GAP/PADV/PASE/BV-02-C|
|GAP 17a/2 AND<br>GAP 11a/3|Periodic Advertising Synchronization Establishment<br>procedure with listening for periodic advertising,<br>PAwR|GAP/PADV/PASE/BV-08-C|
|GAP 33/10|Periodic AdvertisingConnection|GAP/PADV/PAC/BV-02-C|
|**GAP Characteristics**|||
|GAP 27/5 OR<br>GAP 4b/3|Peripheral Preferred Connection Parameters<br>Characteristic|GAP/GAT/BV-04-C|
|GAP 27/6 OR<br>GAP 37/6 OR<br>GAP 4b/8|Writeable Device Name|GAP/GAT/BV-05-C|
|GAP 27/7 OR<br>GAP 37/7 OR<br>GAP 4b/9|Writeable Appearance|GAP/GAT/BV-06-C|
|GAP 27/10 OR<br>GAP 4b/6|Encrypted Data Key Material|GAP/GAT/BV-09-C<br>GAP/GAT/BV-10-C<br>GAP/GAT/BV-11-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **354 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 27/10a OR<br>GAP 4b/7|Encrypted Data Key Material Indications|GAP/GAT/BV-15-C|
|GAP 27/1 OR<br>GAP 37/1 OR<br>GAP 4b/1|Device Name|GAP/GAT/BV-16-C|
|GAP 27/2 OR<br>GAP 37/2 OR<br>GAP 4b/2|Appearance|GAP/GAT/BV-17-C|
|GAP 27/9 OR<br>GAP 37/3 OR<br>GAP 4b/4|Central Address Resolution|GAP/GAT/BV-18-C|
|GAP 27/12 OR<br>GAP 37/5 OR<br>GAP 4b/5|Resolvable Private Address Only|GAP/GAT/BV-19-C|
|GAP 37/4 OR<br>GAP 27/11|LE GATT Security Levels Characteristic|GAP/GAT/BV-12-C|
|**LE Peripheral**|||
|GAP 22/1|Non-discoverable mode, non-connectable modes –<br>Peripheral role|GAP/DISC/NONM/BV-01-C|
|(GAP 20/1 OR<br>GAP 20/5) AND<br>GAP 22/1 AND<br>GAP 23/3|Non-discoverable mode, Undirected Connectable<br>mode – Peripheral role|GAP/DISC/NONM/BV-02-C<br>GAP/CONN/UCON/BV-01-C|
|GAP 23/2 OR<br>GAP 23/3|Non-Bondable mode – Peripheral role|GAP/BOND/NBON/BV-03-C|
|GAP 0b/1 AND<br>GAP 22/2 AND<br>GAP 5/3 AND<br>(GAP 20/3 OR<br>GAP 20/4 OR<br>GAP 20/6 OR<br>GAP 20/7)|Limited Discoverable mode – Non-connectable<br>mode – Peripheral role – BR/EDR/LE|GAP/DISC/LIMM/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 22/2 AND<br>(GAP 20/1 OR<br>GAP 20/5) AND<br>GAP 23/3|Limited Discoverable mode – Undirected<br>Connectable mode – Peripheral role –BR/EDR/LE|GAP/DISC/LIMM/BV-02-C|
|GAP 22/2|Non-connectable mode, Limited Discoverable mode|GAP/CONN/NCON/BV-03-C|
|GAP 22/2 AND<br>GAP 23/3|Undirected Connectable mode, Limited<br>Discoverable mode|GAP/CONN/UCON/BV-03-C|
|GAP 5/3 AND<br>GAP 22/2 AND<br>(GAP 20/3 OR<br>GAP 20/4 OR<br>GAP 20/6 OR<br>GAP 20/7)|Limited Discoverable mode – Non-connectable<br>mode – Peripheral role – LE Only|GAP/DISC/LIMM/BV-03-C|
|GAP 5/3 AND<br>GAP 22/2|Limited Discoverable mode – Undirected<br>Connectable mode – Peripheral role – LE Only|GAP/DISC/LIMM/BV-04-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **355 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 22/3 AND<br>(GAP 20/3 OR<br>GAP 20/4 OR<br>GAP 20/6 OR<br>GAP 20/7)|General Discoverable mode – Non-connectable<br>mode – Peripheral role – BR/EDR/LE|GAP/DISC/GENM/BV-01-C|
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 22/3 AND<br>(GAP 20/1 OR<br>GAP 20/5) AND<br>GAP 23/3|General Discoverable mode – Undirected<br>Connectable mode – Peripheral role – BR/EDR/LE|GAP/DISC/GENM/BV-02-C|
|GAP 5/3 AND<br>GAP 22/3 AND<br>(GAP 20/3 OR<br>GAP 20/4 OR<br>GAP 20/6 OR<br>GAP 20/7)|General Discoverable mode – Non-connectable<br>mode – Peripheral role – LE Only|GAP/DISC/GENM/BV-03-C|
|GAP 5/3 AND<br>GAP 22/3 AND<br>(GAP 20/1 OR<br>GAP 20/5) AND<br>GAP 23/3|General Discoverable mode – Undirected<br>Connectable mode – Peripheral role – LE Only|GAP/DISC/GENM/BV-04-C|
|GAP 22/3 AND<br>(GAP 20/3 OR<br>GAP 20/4 OR<br>GAP 20/6 OR<br>GAP 20/7)|Non-connectable mode, General Discoverable<br>mode|GAP/CONN/NCON/BV-02-C|
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 22/3 AND<br>(GAP 20/1 OR<br>GAP 20/5)|BR/EDR/LE to BR/EDR/LE over LE physical<br>transport – IUT is Peripheral|GAP/DM/LEP/BV-07-C|
|GAP 0b/1 AND<br>GAP 5/3 AND<br>(GAP 20/1 OR<br>GAP 20/5)|Undirected Connectable mode, General<br>Discoverable mode|GAP/CONN/UCON/BV-02-C|
|GAP 23/2|Directed Connectable mode|GAP/CONN/DCON/BV-01-C|
|GAP 23/4|Connection Parameter Update procedure,<br>Peripheral role, Initiator over L2CAP|GAP/CONN/CPUP/BV-01-C<br>GAP/CONN/CPUP/BV-02-C<br>GAP/CONN/CPUP/BV-03-C|
|GAP 23/4 AND<br>GAP 21/9|Connection Parameter Update procedure,<br>Peripheral role, Initiator over LL|GAP/CONN/CPUP/BV-10-C|
|GAP 24/3 AND<br>GAP 27b/10<br>AND (GAP 25/1<br>OR GAP 25/2)|Initiate Bonding – Peripheral role|GAP/BOND/BON/BV-01-C|
|GAP 24/2 AND<br>(GAP 25/1 OR<br>GAP 25/2)|Respond to Bonding – Peripheral role|GAP/BOND/BON/BV-03-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **356 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|(GAP 25/1 OR<br>GAP 25/2) AND<br>GAP 25/3|Service Response – insufficient authentication –<br>Peripheral role|GAP/SEC/AUT/BV-11-C|
|(GAP 25/1 OR<br>GAP 25/2) AND<br>GAP 25/3 AND<br>GATT 3a/1|Service Response – insufficient authentication –<br>Peripheral role|GAP/SEC/AUT/BV-26-C|
|GAP 25/3 AND<br>GAP 25/7 AND<br>GAP 25/8|Service Response – insufficient authentication,<br>Peripheral role|GAP/SEC/AUT/BV-14-C|
|GAP 25/3 AND<br>GAP 25/7 AND<br>GATT 1/1|Correct Pairing after Insufficient Authentication –<br>Peripheral role|GAP/SEC/AUT/BV-18-C|
|GAP 25/3 AND<br>GAP 25/8 AND<br>GATT 1/1|Service response Insufficient Authentication –<br>Peripheral role|GAP/SEC/AUT/BV-20-C|
|GAP 25/1 AND<br>GAP 25/8 AND<br>GATT 1/1|Lost Bond – Responder role|GAP/SEC/AUT/BV-22-C|
|GAP 25/3 AND<br>GAP 25/7|Service Response – Insufficient encryption,<br>Peripheral role|GAP/SEC/AUT/BV-23-C|
|GAP 25/3 AND<br>GAP 25/7 AND<br>GATT 3a/1|Service Response – Insufficient encryption,<br>Peripheral role|GAP/SEC/AUT/BV-28-C|
|GAP 22/3 AND<br>GAP 23/3 AND<br>(GAP 24/2 OR<br>GAP 24/3) AND<br>GAP 26/1|Privacy connection handling and RPA generation<br>and resolution|GAP/PRIV/CONN/BV-10-C<br>GAP/PRIV/CONN/BV-12-C|
|GAP 21/9|Connection Parameter Update procedure, Valid<br>Parameters Peripheral role – LL Connection<br>Parameters Request|GAP/CONN/CPUP/BV-08-C|
|GAP 24/2 AND<br>GAP 26/1|Connection handling with Private Random Device<br>Address – Peripheral role|GAP/CONN/PRDA/BV-01-C|
|GAP 27a/1|Periodic Advertising Synchronization Transfer<br>procedure|GAP/PADV/PAST/BV-01-C|
|GAP 27a/1 AND<br>GAP 11a/3|Periodic Advertising Synchronization Transfer<br>procedure, PAwR|GAP/PADV/PAST/BV-03-C|
|GAP 27a/2|Periodic Advertising Synchronization Establishment<br>procedure without listeningforperiodic advertising|GAP/PADV/PASE/BV-03-C|
|GAP 27a/2 AND<br>GAP 11a/3|Periodic Advertising Synchronization Establishment<br>procedure without listening for periodic advertising,<br>PAwR|GAP/PADV/PASE/BV-09-C|
|GAP 27a/3|Periodic Advertising Synchronization Establishment<br>procedure with listeningforperiodic advertising|GAP/PADV/PASE/BV-04-C|
|GAP 27a/3 AND<br>GAP 11a/3|Periodic Advertising Synchronization Establishment<br>procedure with listening for periodic advertising,<br>PAwR|GAP/PADV/PASE/BV-10-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **357 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 5/3 AND<br>GAP 25/8 AND<br>GATT 3/18 AND<br>GAP 25/14|Security mode 1 level 2 – GATT Indications,<br>Peripheral|GAP/SEC/SEM/BV-56-C|
|GAP 5/3 AND<br>GAP 25/8 AND<br>GATT 3/17 AND<br>GAP 25/14|Security mode 1 level 2 – GATT Notifications,<br>Peripheral|GAP/SEC/SEM/BV-59-C|
|GAP 5/3 AND<br>GAP 25/7 AND<br>GATT 3/18 AND<br>GAP 25/14|Security mode 1 level 3 – GATT Indications,<br>Peripheral|GAP/SEC/SEM/BV-57-C|
|GAP 5/3 AND<br>GAP 25/7 AND<br>GATT 3/17 AND<br>GAP 25/14|Security mode 1 level 3 – GATT Notifications,<br>Peripheral|GAP/SEC/SEM/BV-60-C|
|**LE Central**|||
|GAP 32/2|Discovery and Connection procedures – Central<br>role|GAP/DISC/GENP/BV-01-C<br>GAP/DISC/GENP/BV-02-C<br>GAP/DISC/GENP/BV-03-C<br>GAP/DISC/GENP/BV-04-C<br>GAP/DISC/GENP/BV-05-C|
|GAP 33/2 AND<br>(GAP 34/2 OR<br>GAP 34/3) AND<br>GAP 36/1|Privacy connection handling and RPA generation<br>and resolution|GAP/PRIV/CONN/BV-11-C|
|GAP 33/5|Connection Parameter Update procedure, Central<br>role|GAP/CONN/CPUP/BV-04-C<br>GAP/CONN/CPUP/BV-05-C<br>GAP/CONN/CPUP/BV-06-C|
|GAP 34/1|Non-bondable mode – Central|GAP/BOND/NBON/BV-01-C<br>GAP/BOND/NBON/BV-02-C|
|GAP 32/1|Limited Discovery procedure – Central role|GAP/DISC/LIMP/BV-01-C<br>GAP/DISC/LIMP/BV-02-C<br>GAP/DISC/LIMP/BV-03-C<br>GAP/DISC/LIMP/BV-04-C<br>GAP/DISC/LIMP/BV-05-C|
|GAP 33/1|Auto Connection Establishment procedure Directed<br>Connectable mode – Central role|GAP/CONN/ACEP/BV-01-C|
|GAP 33/2|General Connection Establishment procedure –<br>Central role|GAP/CONN/GCEP/BV-01-C<br>GAP/CONN/GCEP/BV-02-C|
|GAP 33/3|Selective Connection Establishment procedure,<br>Directed Connectable mode|GAP/CONN/SCEP/BV-01-C|
|GAP 33/4|Direct Connection Establishment procedure,<br>Directed and Undirected Connectable modes|GAP/CONN/DCEP/BV-01-C<br>GAP/CONN/DCEP/BV-03-C|
|GAP 34/3 AND<br>(GAP 35/1 OR<br>GAP 35/2)|Initiate Bonding – Central role|GAP/BOND/BON/BV-02-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **358 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 34/2 AND<br>(GAP 35/1 OR<br>GAP 35/2)|Respond to Bonding – Central role|GAP/BOND/BON/BV-04-C|
|(GAP 35/1 OR<br>GAP 35/2) AND<br>GAP 35/3|Service Response – Insufficient authentication,<br>Central role|GAP/SEC/AUT/BV-12-C<br>GAP/SEC/AUT/BV-25-C|
|GAP 35/3 AND<br>GAP 35/7 AND<br>GAP 35/8|Service Response – Insufficient Authentication,<br>Central role|GAP/SEC/AUT/BV-13-C|
|GAP 35/3 AND<br>GAP 35/7 AND<br>GATT 1/1|Correct Pairing after Insufficient Authentication –<br>Central role|GAP/SEC/AUT/BV-17-C|
|GAP 35/3 AND<br>GAP 35/8 AND<br>GATT 1/1|Service response Insufficient Authentication –<br>Central role|GAP/SEC/AUT/BV-19-C|
|GAP 35/1 AND<br>GAP 35/8|Lost Bond – Initiator role|GAP/SEC/AUT/BV-21-C|
|GAP 35/3|Service Response – Insufficient Encryption, Central<br>role|GAP/SEC/AUT/BV-24-C<br>GAP/SEC/AUT/BV-27-C|
|GAP 34/2 AND<br>GAP 36/1|Connection handling with Private Random Device<br>Address – Central role|GAP/CONN/PRDA/BV-02-C|
|GAP 37a/1|Periodic Advertising Synchronization Transfer<br>procedure|GAP/PADV/PAST/BV-02-C|
|GAP 37a/1 AND<br>GAP 11a/3|Periodic Advertising Synchronization Transfer<br>procedure, PAwR|GAP/PADV/PAST/BV-04-C|
|GAP 37a/2|Periodic Advertising Synchronization Establishment<br>procedure without listeningforperiodic advertising|GAP/PADV/PASE/BV-05-C|
|GAP 37a/2 AND<br>GAP 11a/3|Periodic Advertising Synchronization Establishment<br>procedure without listening for periodic advertising,<br>PAwR|GAP/PADV/PASE/BV-11-C|
|GAP 37a/3|Periodic Advertising Synchronization Establishment<br>procedure with listeningforperiodic advertising|GAP/PADV/PASE/BV-06-C|
|GAP 37a/3 AND<br>GAP 11a/3|Periodic Advertising Synchronization Establishment<br>procedure with listening for periodic advertising,<br>PAwR|GAP/PADV/PASE/BV-12-C|
|GAP 5/4 AND<br>GAP 35/8 AND<br>GATT 3/18 AND<br>GAP 35/15|Security mode 1 level 2 – GATT Indications, Central|GAP/SEC/SEM/BV-62-C|
|GAP 5/4 AND<br>GAP 35/8 AND<br>GATT 3/17 AND<br>GAP 35/15|Security mode 1 level 2 – GATT Notifications,<br>Central|GAP/SEC/SEM/BV-65-C|
|GAP 5/4 AND<br>GAP 35/7 AND<br>GATT 3/18 AND<br>GAP 35/15|Security mode 1 level 3 – GATT Indications, Central|GAP/SEC/SEM/BV-63-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **359 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 5/4 AND<br>GAP 35/7 AND<br>GATT 3/17 AND<br>GAP 35/15|Security mode 1 level 3 – GATT Notifications,<br>Central|GAP/SEC/SEM/BV-66-C|
|**BR/EDR Secure Connections**|||
|GAP 1/5 AND<br>GAP 4/2 AND<br>GAP 4/4 AND<br>GAP 4/6 AND<br>GAP 2/11|Verify Secure Connections Only mode when IUT is<br>Peripheral and responder|GAP/SEC/SEM/BV-11-C<br>GAP/SEC/SEM/BV-12-C<br>GAP/SEC/SEM/BV-13-C<br>GAP/SEC/SEM/BV-14-C<br>GAP/SEC/SEM/BV-15-C<br>GAP/SEC/SEM/BV-47-C<br>GAP/SEC/SEM/BV-48-C<br>GAP/SEC/SEM/BV-49-C|
|GAP 4/1 AND<br>GAP 4/3 AND<br>GAP 4/5 AND<br>GAP 2/11|Verify Secure Connections only mode when IUT is<br>Central and initiator|GAP/SEC/SEM/BV-16-C<br>GAP/SEC/SEM/BV-17-C<br>GAP/SEC/SEM/BV-18-C<br>GAP/SEC/SEM/BV-19-C<br>GAP/SEC/SEM/BV-20-C<br>GAP/SEC/SEM/BV-54-C<br>GAP/SEC/SEM/BV-55-C|
|GAP 2/5|BR/EDR security mode 2|GAP/SEC/SEM/BI-01-C<br>GAP/SEC/SEM/BI-05-C|
|GAP 2/7d|BR/EDR security mode 4 level 1 – Invalid Key Size<br>– Any Key Size|GAP/SEC/SEM/BI-11-C<br>GAP/SEC/SEM/BI-12-C|
|GAP 2/7c|BR/EDR security mode 4 level 2 – Invalid Key Size<br>– Any Key Size|GAP/SEC/SEM/BI-02-C<br>GAP/SEC/SEM/BI-06-C|
|GAP 2/7b|BR/EDR security mode 4 level 3 – Invalid Key Size<br>– Any Key Size|GAP/SEC/SEM/BI-03-C<br>GAP/SEC/SEM/BI-07-C|
|GAP 2/7a|BR/EDR securitymode 4 level 4|GAP/SEC/SEM/BI-31-C|
|GAP 2/13d|BR/EDR security mode 4 level 1 – Invalid Key Size<br>– 128-bit Key Size|GAP/SEC/SEM/BI-14-C<br>GAP/SEC/SEM/BI-17-C|
|GAP 2/13c|BR/EDR security mode 4 level 2 – Invalid Key Size<br>– 128-bit Key Size|GAP/SEC/SEM/BI-15-C<br>GAP/SEC/SEM/BI-18-C|
|GAP 2/13b|BR/EDR security mode 4 level 3 – Invalid Key Size<br>– 128-bit Key Size|GAP/SEC/SEM/BI-16-C<br>GAP/SEC/SEM/BI-19-C|
|GAP 2/13a|BR/EDR security mode 4 level 4 – Invalid Key Size<br>– 128-bit Key Size|GAP/SEC/SEM/BI-04-C<br>GAP/SEC/SEM/BI-08-C|
|**Simultaneous Physical Transports**|||
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 45/1|BR/EDR/LE to BR/EDR/LE over both transports –<br>IUT is LE peripheral/BR Peripheral|GAP/DM/LEP/BV-08-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>GAP 44/2|BR/EDR/LE to BR/EDR/LE over both transports –<br>IUT is LE central/BR Central|GAP/DM/LEP/BV-09-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **360 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 0b/1 AND<br>GAP 5/3 AND<br>GAP 45/2|BR/EDR/LE to BR/EDR/LE over both transports –<br>IUT is LE peripheral/BR Central|GAP/DM/LEP/BV-10-C|
|GAP 0b/1 AND<br>GAP 5/4 AND<br>GAP 44/1|BR/EDR/LE to BR/EDR/LE over both transports –<br>IUT is LE central/BR Peripheral|GAP/DM/LEP/BV-11-C|
|**LE Secure Connections – Host**|||
|GAP 35/9 AND<br>GAP 41/2a AND<br>GAP 2/11|Generate BR/EDR Link Key from LE LTK, as<br>initiator|GAP/DM/LEP/BV-12-C<br>GAP/DM/LEP/BV-15-C<br>GAP/DM/LEP/BV-20-C|
|GAP 25/9 AND<br>GAP 43/2a AND<br>GAP 2/11|Generate BR/EDR Link Key from LE LTK, as<br>responder|GAP/DM/LEP/BV-14-C<br>GAP/DM/LEP/BV-16-C<br>GAP/DM/LEP/BV-21-C|
|GAP 35/9 AND<br>GAP 41/2b AND<br>GAP 2/11|Generate LE LTK from BR/EDR Link Key, as<br>initiator|GAP/DM/LEP/BV-17-C<br>GAP/DM/LEP/BI-01-C<br>GAP/DM/LEP/BV-22-C|
|GAP 25/9 AND<br>GAP 43/2b AND<br>GAP 2/11|Generate LE LTK from BR/EDR Link Key, as<br>responder|GAP/DM/LEP/BV-19-C<br>GAP/DM/LEP/BI-02-C<br>GAP/DM/LEP/BV-23-C|
|GAP 35/9 AND<br>GAP 2/11 AND<br>GAP 41/2a AND<br>GAP 41/2b|Regenerate BR/EDR Link Key or LE LTK following<br>cross-transport key upgrade|GAP/DM/LEP/BV-13-C<br>GAP/DM/LEP/BV-18-C|
|GAP 5/3 AND<br>GAP 25/9|Peripheral, LE Secure Connections – security mode<br>1 level 4|GAP/SEC/SEM/BV-21-C<br>GAP/SEC/SEM/BV-22-C|
|GAP 5/3 AND<br>GAP 25/13a|Peripheral, LE Secure Connections Only – security<br>mode 1 level 4 – 128-bit KeySize|GAP/SEC/SEM/BI-09-C|
|GAP 5/3 AND<br>GAP 25/12|Peripheral, LE Secure Connections Only – security<br>mode 1 level 3|GAP/SEC/SEM/BV-38-C<br>GAP/SEC/SEM/BV-40-C|
|GAP 5/3 AND<br>GAP 25/11|Peripheral, LE Secure Connections Only – security<br>mode 1 level 2|GAP/SEC/SEM/BV-37-C<br>GAP/SEC/SEM/BV-39-C|
|GAP 5/3 AND<br>(GAP 25/9 OR<br>GAP 25/11 OR<br>GAP 25/12)<br>AND GATT 3/18<br>AND GAP 25/14|LE Secure Connections Only – GATT Indications,<br>Peripheral|GAP/SEC/SEM/BV-58-C|
|GAP 5/3 AND<br>((GAP 25/9 AND<br>GAP 25/10) OR<br>GAP 25/11 OR<br>GAP 25/12)<br>AND GATT 3/17<br>AND GAP 25/14|LE Secure Connections Only – GATT Notifications,<br>Peripheral|GAP/SEC/SEM/BV-61-C|
|GAP 5/3 AND<br>GAP 25/13b|Peripheral, LE security mode 1 level 3 – Invalid<br>Encryption KeySize – 128-bit KeySize|GAP/SEC/SEM/BI-20-C|
|GAP 5/3 AND<br>GAP 25/13c|Peripheral, LE security mode 1 level 2 – Invalid<br>Encryption KeySize – 128-bit KeySize|GAP/SEC/SEM/BI-21-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **361 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 2/7a AND<br>GAP 4/3|BR/EDR security mode 4 level 4, Initiator, Channel<br>Establishment|GAP/SEC/SEM/BI-27-C<br>GAP/SEC/SEM/BI-32-C|
|GAP 2/7b AND<br>GAP 4/3|BR/EDR security mode 4 level 3, Initiator, Channel<br>Establishment|GAP/SEC/SEM/BI-26-C|
|GAP 2/7c AND<br>GAP 4/3|BR/EDR security mode 4 level 2, Initiator, Channel<br>Establishment|GAP/SEC/SEM/BI-25-C|
|GAP 2/7a AND<br>L2CAP 2/37|BR/EDR security mode 4 level 4, Initiator,<br>Connectionless Channel, Unicast Data|GAP/SEC/SEM/BI-30-C<br>GAP/SEC/SEM/BI-33-C|
|GAP 2/7b AND<br>L2CAP 2/37|BR/EDR security mode 4 level 3, Initiator,<br>Connectionless Channel, Unicast Data|GAP/SEC/SEM/BI-29-C|
|GAP 2/7c AND<br>L2CAP 2/37|BR/EDR security mode 4 level 2, Initiator,<br>Connectionless Channel, Unicast Data|GAP/SEC/SEM/BI-28-C|
|GAP 5/3 AND<br>(GAP 25/10 OR<br>GAP 25/11 OR<br>GAP 25/12)|Peripheral, Secure Connections Only mode|GAP/SEC/SEM/BV-23-C<br>GAP/SEC/SEM/BV-24-C|
|GAP 2/11 AND<br>GAP 25/10|Security Connections Only mode, Peripheral,<br>BR/EDR and LE transports|GAP/SEC/SEM/BV-25-C|
|GAP 5/4 AND<br>GAP 35/9|Central, LE security mode 1 level 4|GAP/SEC/SEM/BV-26-C<br>GAP/SEC/SEM/BV-27-C<br>GAP/SEC/SEM/BV-45-C|
|GAP 5/4 AND<br>GAP 35/12|Central, LE Secure Connections Only – LE security<br>mode 1 level 3|GAP/SEC/SEM/BV-42-C<br>GAP/SEC/SEM/BV-44-C|
|GAP 5/4 AND<br>GAP 35/11|Central, LE Secure Connections Only – LE security<br>mode 1 level 2|GAP/SEC/SEM/BV-41-C<br>GAP/SEC/SEM/BV-43-C|
|GAP 5/4 AND<br>(GAP 35/9 OR<br>GAP 35/11 OR<br>GAP 35/12)<br>AND GATT 3/18<br>AND GAP 35/15|LE Secure Connections Only – GATT Indications,<br>Central|GAP/SEC/SEM/BV-64-C|
|GAP 5/4 AND<br>((GAP 35/9 AND<br>GAP 35/10) OR<br>GAP 35/11 OR<br>GAP 35/12)<br>AND GATT 3/17<br>AND GAP 35/15|LE Secure Connections Only – GATT Notifications,<br>Central|GAP/SEC/SEM/BV-67-C|
|GAP 5/4 AND<br>GAP 35/13a|Central, LE security mode 1 level 4 – Invalid<br>Encryption KeySize – 128-bit KeySize|GAP/SEC/SEM/BI-10-C|
|GAP 5/4 AND<br>GAP 35/13b|Central, LE security mode 1 level 3 – Invalid<br>Encryption KeySize – 128-bit KeySize|GAP/SEC/SEM/BI-22-C|
|GAP 5/4 AND<br>GAP 35/13c|Central, LE security mode 1 level 2 – Invalid<br>Encryption KeySize – 128-bit KeySize|GAP/SEC/SEM/BI-23-C|
|GAP 5/4 AND<br>(GAP 35/10 OR<br>GAP 35/11 OR<br>GAP 35/12)|Central, Secure Connections Only mode|GAP/SEC/SEM/BV-28-C<br>GAP/SEC/SEM/BV-29-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **362 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|GAP 2/11 AND<br>GAP 35/10|Secure Connections Only mode, Central, BR/EDR<br>and LE transports|GAP/SEC/SEM/BV-30-C|
|**LE Privacy**|||
|(GAP 8/2 OR<br>GAP 8/4) AND<br>GAP 11/2 AND<br>GAP 11/4 AND<br>GAP 11/5|Broadcast mode Resolvable Private Address, Scan<br>Response|GAP/BROB/BCST/BV-05-C|
|GAP 14/2 AND<br>GAP 17/3 AND<br>GAP 17/4|Observation procedure with Active Scanning, using<br>Resolvable Private Address|GAP/BROB/OBSV/BV-06-C|
|GAP 36/1 AND<br>GAP 36/3 AND<br>(GAP 32/1 OR<br>GAP 32/2)|Discovery procedure Finding Discoverable Device<br>using Resolvable Privacy Address|GAP/DISC/RPA/BV-01-C|
|GAP 26/1 AND<br>GAP 27/9 AND<br>GAP 23/2|Directed Connectable mode, Privacy, Resolvable<br>Private Address, Central Address Resolution|GAP/CONN/DCON/BV-04-C<br>GAP/CONN/DCON/BV-05-C|
|GAP 26/1 AND<br>GAP 23/3|Undirected Connectable mode Resolvable Private<br>Address|GAP/CONN/UCON/BV-06-C|
|GAP 36/1 AND<br>GAP 36/3 AND<br>GAP 33/1|Auto Connection Establishment procedure, Directed<br>Connectable mode, Resolvable Private Address,<br>Central Address Resolution|GAP/CONN/ACEP/BV-03-C<br>GAP/CONN/ACEP/BV-04-C|
|GAP 36/1 AND<br>GAP 36/3 AND<br>GAP 33/2|General Connection Establishment procedure,<br>Directed Connectable mode, Resolvable Private<br>Address, Central Address Resolution|GAP/CONN/GCEP/BV-05-C<br>GAP/CONN/GCEP/BV-06-C|
|GAP 36/1 AND<br>GAP 36/3 AND<br>GAP 33/3|Selective Connection Establishment procedure,<br>Directed Connectable mode, Resolvable Private<br>Address|GAP/CONN/SCEP/BV-03-C|
|GAP 36/1 AND<br>GAP 36/3 AND<br>GAP 33/4|Direct Connection Establishment procedure,<br>Directed Connectable mode, Resolvable Private<br>Address|GAP/CONN/DCEP/BV-05-C<br>GAP/CONN/DCEP/BV-06-C|
|GAP 17b/2 AND<br>GAP 2/9|LE security mode 3, Observer, No Security|GAP/SEC/SEM/BV-31-C|
|(GAP 17b/3 OR<br>GAP 17b/4)<br>AND GAP 2/9|LE security mode 3, Observer, Encryption|GAP/SEC/SEM/BV-32-C|
|GAP 17b/1|LE securitymode, Observer, Reject|GAP/SEC/SEM/BI-13-C|
|GAP 11b/2 AND<br>GAP 2/9|LE security mode 3, Broadcaster, No Security|GAP/SEC/SEM/BV-34-C|
|(GAP 11b/3 OR<br>GAP 11b/4)<br>AND GAP 2/9|LE security mode 3, Broadcaster, Encryption|GAP/SEC/SEM/BV-35-C|
|GAP 16/2|Broadcast Isochronous Stream Synchronization<br>Establishmentprocedure|GAP/BIS/BSE/BV-01-C|
|GAP 10/2 AND<br>GAP 10/3|Broadcast Isochronous Stream Broadcasting mode|GAP/BIS/BBM/BV-01-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **363 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|**Connection Subrating Procedure**|||
|GAP 23/8|Connection Subrate Requestprocedure|GAP/CSUB/CSR/BV-01-C|
|GAP 33/9|Connection Subrate Updateprocedure|GAP/CSUB/CSU/BV-01-C|
|**Channel Sounding**|||
|GAP 23a/1 OR<br>GAP 33a/1|Channel Sounding, Initiator|GAP/CS/BV-01-C|
|GAP 23a/2 OR<br>GAP 33a/2|Channel Sounding, Reflector|GAP/CS/BV-02-C|
|(GAP 23a/1<br>AND GAP<br>25/15) OR<br>(GAP 33a/1<br>AND<br>GAP 35/16)|Channel Sounding Security Level 1, Initiator|GAP/SEC/SEM/BV-69-C|
|(GAP 23a/1<br>AND GAP<br>25/16) OR<br>(GAP 33a/1<br>AND<br>GAP 35/17)|Channel Sounding Security Level 2, Initiator|GAP/SEC/SEM/BV-70-C|
|(GAP 23a/1<br>AND GAP<br>25/17) OR<br>(GAP 33a/1<br>AND<br>GAP 35/18)|Channel Sounding Security Level 3, Initiator|GAP/SEC/SEM/BV-71-C|
|(GAP 23a/1<br>AND GAP<br>25/18) OR<br>(GAP 33a/1<br>AND<br>GAP 35/19)|Channel Sounding Security Level 4, Initiator|GAP/SEC/SEM/BV-72-C|
|(GAP 23a/2<br>AND GAP<br>25/15) OR<br>(GAP 33a/2<br>AND<br>GAP 35/16)|Channel Sounding Security Level 1, Reflector|GAP/SEC/SEM/BV-73-C|
|(GAP 23a/2<br>AND GAP<br>25/16) OR<br>(GAP 33a/2<br>AND<br>GAP 35/17)|Channel Sounding Security Level 2, Reflector|GAP/SEC/SEM/BV-74-C|
|(GAP 23a/2<br>AND GAP<br>25/17) OR<br>(GAP 33a/2<br>AND<br>GAP 35/18)|Channel Sounding Security Level 3, Reflector|GAP/SEC/SEM/BV-75-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **364 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|(GAP 23a/2<br>AND GAP<br>25/18) OR<br>(GAP 33a/2<br>AND<br>GAP 35/19)|Channel Sounding Security Level 4, Reflector|GAP/SEC/SEM/BV-76-C|



_Table 5.1: Test case mapping_ 

**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **365 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

## **6 Revision histor and acknowled ments y g** 

## _**Revision History**_ 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
|10|D5r3|2003-11-05|Original Release|
|11|D10R00,<br>1.2.1, 1.2.2|2004-03-03,<br>2004-03-25|Re-partitioned to match Main Specification<br>Volume/Part partitioning. TSE 511, 515, 516, and 517<br>incorporated<br>Editorial changes|
||1.2.3r1|2005-01-04|Changed document numbering.<br>Incorporate TSE 657 for Figure 5.5 and<br>TP/SEC/AUT/BV-01-C MSC, Figure 5.14.<br>Incorporate TSE 672 for TCMT for TC<br>TP/EST/LIE/BV-02-C.|
|12|1.2.3|2005-01-13|Release after review.|
||1.2.4r1|2005-03-12|Changed the way TSE 657 was incorporated for<br>ESR02: Errata Service Release to Specification<br>Versions 1.1, 1.2, and Profiles which added an<br>additional Figure 5.5 in paragraph 5.2.4 and added an<br>additional Test Procedure MSC (Figure 5.14) to test<br>case TP/SEC/AUT/BV-01-C.|
|13|1.2.4|2005-03-16|Prepare forpublication.|
||1.2.5r0|2005-08-23|TSE 760(v1.2)/TSE 803 (v2.0): Changes to<br>TP/MOD/LDIS/[BV-01|BV-02]-C;<br>TSE 794 changes TCMT for TP/EST/LIE/BV-02 to<br>refer to 3/1<br>Changed coverpage title|
||1.2.5r1|2005-09-20|Corrected TSE 794: to [GAP 41/ AND (GAP 3/1 or<br>GAP 3/2)]|
|14|1.2.5|2005-09-26|Prepare forpublication.|
||2.1.E.1r0<br>(1.2.6r0) to<br>2.1.E.1r5|2006-05-24<br>to<br>2007 06-06|TSE 852: TP/EST/LIE/BV-02-C: Modify TCMT<br>selection set. Same as TSE 794<br>TSE 1566: TP/MOD/NPAIR/BV-01-C,<br>TP/SEC/AUT/BV-01-C, TP/SEC/AUT/BV-02-C,<br>TP/SEC/SEM/BV-01-C, TP/SEC/SEM/BV-02-C,<br>TP/SEC/SEM/BV-03-C<br>TSE 1820: Add test case TP/MOD/LDIS/BV-03-C<br>TP 1890: Remove “Applicable if…” stmts for<br>TP/MOD/NDIS/BV-01-C,TP/MOD/LDIS/BV-01-C,<br>TP/MOD/LDIS/BV-02-C, TP/MOD/GDIS/BV-01-C,<br>TP/MOD/GDIS/BV-02-C, TP/MOD/NCON/BV-01-C,<br>TP/MOD/CON/BV-01-C, TP/MOD/NPAIR/BV-01-C,<br>TP/MOD/PAIR/BV-01-C, TP/SEC/AUT/BV-01-C,<br>TP/SEC/AUT/BV-02-C, TP/SEC/SEM/BV-01-C,<br>TP/SEC/SEM/BV-02-C, TP/SEC/SEM/BV-03-C,<br>TP/IDLE/GIN/BV-01-C,TP/IDLE/LIN/BV-01-C,<br>TP/IDLE/DED/BV-01-C, TP/IDLE/BON/BV-01-C,<br>TP/EST/LIE/BV-01-C, TP/EST/LIE/BV-02-C<br>Modified Section 5.2.1, Fig. 5.1 for Simple Pairing<br>Added TC TP/SEC/SEM/BV-04-C for Simple Pairing|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **366 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||Added MSC for Security mode 4 to TP/IDLE/BOV/BV-<br>01-C<br>Modified text for TP/EST/LIE/BV-01-C,<br>TP/EST/LIE/BV-02-C, and TP/EST/CHE/BV-01-C<br>Changed TCMT for TP/IDLE/BOV/BV-01-C,<br>TP/EST/LIE/BV-01-C, TP/EST/LIE/BV-02-C,<br>TP/EST/CHE/BV-01-C<br>Modifications:<br>--Section 5.3, updated Figure 5.2<br>--TP/IDLE/BON/BV-01, changed Pass Verdict<br>--TP/SEC/SEM/BV-04-C; modified MSC<br>New test cases:<br>TP/IDLE/BON/BV-02-C, TP/IDLE/BON/BV-03-C,<br>TP/IDLE/BON/BV-04-C, TP/IDLE/BON/BV-05-C,<br>TP/IDLE/BON/BV-06-C<br>TP/MOD/NPAIR/BV-02-C, TP/MOD/NPAIR/BV-03-C<br>TP/IDLE/DED/BV-02-C<br>TP/SEC/SEM/BV-05-C, TP/SEC/SEM/BV-06-C,<br>TP/SEC/SEM/BV-07-C, TP/SEC/SEM/BV-08-C,<br>TP/SEC/SEM/BV-09-C<br>--New Section 5.5.2 with new test case<br>TP/IDLE/DNDIS/BV-01-C|
|15|2.1.E.1|2007-Jun-07|Prepare forpublication|
||2.1.E.2r1-5|2007-August-<br>29 to 2008-<br>March|TSE: 2245: TP/IDLE/BON/BV-05, TP/IDLE/BON/BV-<br>06, update MSCs and Pass Verdict<br>TSE 2246 for TP/SEC/SEM/BV-10-C<br>TSE 2237 for TP/SEC/AUT/BV-01-C<br>TSE 2282 TP/MOD/NPAIR/BV-02-C and<br>TP/MOD/NPAIR/BV-03-C: update MSCs<br>TSE 2329 TP/SEC/SEM/BV-04-C: update MSCs<br>TSE 2330 TP/SEC/SEM/BV-04-C: update MSCs<br>TSE 2331 TP/SEC/SEM/BV-05-C: update test<br>purpose<br>TSE 2411: add preamble to Section 5.2. for<br>TP/SEC/SEM/BV-07-C, TP/SEC/SEM/BV-08-C<br>TSE 2412: TP/SEC/SEM/BV-09-C|
|16|2.1.E.2|2008-April|Prepare forpublication.|
||2.1.E.3r0-1|2008-May<br>2008<br>October|TSE 2532: TP/SEC/SEM-BV-03-C: fix graphic<br>TSE 2332; TP/MOD/NPAIR/BV-03-C,<br>TP/SEC/SEM/BV-05-C, TP/SEC/SEM/BV-06-C,<br>TP/SEC/SEM/BV-07-C, TP/SEC/SEM/BV-09-C<br>TSE 2477: TP/SEC/SEM/BV-04-C: MSC<br>TSE 2494; TP/SEC/SEM/BV-09-C, TCMT<br>TSE 2546 TP/IDLE/DED/BV-01-C, TP/IDLE/BON/BV-<br>01-C, TP/EST/LIE/BV-02-C, TP/IDLE/DED/BV-02-C,<br>TP/IDLE/BON/BV-02-C, TP/IDLE/BON/BV-03-C,<br>TP/IDLE/BON/BV-04-C, TP/IDLE/BON/BV-05-C,<br>TP/IDLE/BON/BV-06-C: Update preamble<br>TSE 2631: TP/SEC/SEM/BV-06-C, TP/SEC/SEM/BV-<br>07-C: TCMT<br>TSE 2633: TP/SEC/SEM/BV-10-C: update MSC|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **367 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 2638: TP/IDLE/BON/BV-04-C, TP/IDL/BON/BV-<br>06-C: TCMT 2656: TP/IDLE/BON/BV-01-<br>C,TP/IDLE/BON/BV-02-C: TCMT|
|17|2.1.E.3|2008<br>December|Prepare for publication.|
|18|2.1.E.4r0|March 2010|TSE 2675: TP/SEC/AUT/BV-01-C: MSC and test<br>proc.<br>TSE 2944: TP/IDLE/BON/BV-03-C,<br>TP/IDLE/BON/BV-04-C; Initial Conditions<br>TSE 2989: TP/SEC/SEM/BV-09-C<br>TSE 3012: TP/SEC/SEM/BV-05-C: TCMT update<br>TSE 3284: TP/IDLE/BON/BV-05-C,<br>TP/IDLE/BON/BV-06-C Initial Conditions|
|19|4.0.0d10-<br>4.0.0d23a|11-06-10-<br>08-07-10|Document merge between GAP.TS/2.1.E.4r0 and LE<br>specific GAP TS called 0.9d9 dated 2010-06-10<br>Editorial changes New sub group 5.4.4 introduced<br>Added TP/SEC/CSIGN/BI-03-C and<br>TP/SEC/CSIGN/BI-04-C<br>Update to Test Procedure in TP/CONN/DCON/BV-03-<br>C<br>Addressing review comments by adjusted intimal<br>conditions in TP/DISC/GENM/BV-01-C,<br>TP/DISC/GENM/BV-02-C, TP/DISC/LIMM/BV-02-C<br>Addressed review comments, text clarifications to<br>match IOP testing performed.<br>Change “discoverable” to “scannable” to align with<br>latest core spec change when referring to advertising<br>events.<br>Modified test cases TO/SEC/AUT/BV-13-C and BV-<br>14-C more specific and correct the MSC where data<br>signing shall not be mentioned.<br>Added SM dependencies in TCMT for<br>TP/BOND/NBON/BV-01-C, TP/BOND/NBON/BV-02-<br>C, TP/BOND/NBON/BV-03-C,<br>TP/ADV/BV-06-C and TP/ADV/BV-07-C<br>Align TCMT with ICS compliance to BR/EDR/LE<br>Central and Peripheral devices<br>Formatting, prepare for publication. Republished as<br>4.0.0a|
||4.0.1r0 to<br>4.0.1r5|11 October<br>2010 to<br>22 June<br>2011|TSE 3785: Errata on Mapping table for TP/GAT/BV-<br>02-C and TP/GAT/BV-03-C<br>TSE 3914: TP/GAT/BV-02-C, TP/GAT/BV-03-C,<br>TP/GAT/BV-04-C: Change test purpose and MSCs<br>TP/ADV/BV-06-C, TP/ADV/BV-07-C, TP/ADV/BV-08-<br>C, TP/ADV/BV-09-C, TP/ADV/BV-10-C<br>TSE 3837: See entry 4.0.0d23. The last six rows of<br>the TCMT table were entered as two separate tables<br>in d21 and were not included in a copy/paste into d22.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **368 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 3848, TSE 4090: TCMT changes for<br>TP/DISC/LIMM/BV-01-C, TP/DISC/GENM/BV-01-C,<br>TP/CONN/NCON/BV-03-C and TP/CONN/NCON/BV-<br>02-C and TP/GAT/BV-01-C<br>TSE 3913: update Reference section in TP/ADV/BV-<br>06-C, TP/ADV/BV-07-C, TP/ADV/BV-08-C,<br>TP/ADV/BV-09-C, TP/ADV/BV-10-C<br>TSE 3947: TP/SEC/CSIGN/BI-03-C,<br>TP/SEC/CSIGN/BI-04<br>TSE 4105: TP/CONN/NCON/BV-03-C: TCMT<br>TSE 4116: TP/SEC/AUT/BV-12-C, TP/SEC/AUT/BV-<br>14-C TCMT updates<br>TSE 4112: TP/CONN/CPUP/BV-01-C,<br>TP/CONN/CPUP/BV-02-C, TP/CONN/CPUP/BV-03-<br>C, TP/CONN/CPUP/BV-04-C, TP/CONN/CPUP/BV-<br>05-C, TP/CONN/CPUP/BV-06-C<br>TSE 4151: TP/CONN/CPUP/BV-03-C: Init. Condition,<br>Test proc: change valid to invalid<br>TSE 4166: TP/BOND/NBON/BV-03-C:bong->bond<br>TSE 4235: IXIT changes for TP/BROB/OBSV/BV-03-<br>C, TP/CONN/CPUP/BV-01-C, TP/CONN/CPUP/BV-<br>02-C, TP/CONN/CPUP/BV-03-C,<br>TP/CONN/CPUP/BV-04-C, TP/CONN/CPUP/BV-05-<br>C, TP/CONN/CPUP/BV-06-C, TP/PRIV/CONN/BV-01-<br>C, TP/PRIV/CONN/BV-02-C, TP/PRIV/CONN/BV-06-<br>C<br>TSE 4178: TP/CONN/GCEP/BV-02-C: edit Pass<br>verdict<br>Fix TCMT for<br>TSE 4116: remove text in TP/SEC/AUT/BV-12-<br>TSE 3848: TP/GAT/BV-01-C<br>TSE 4105: TP/CONN/NCON/BV-03<br>TSE 4306: Update TCMT for LE single mode devices:<br>TP/CONN/UCON/BV-01-C, TP/GAT/BV-01-C,<br>TP/GAT/BV-02-C, TP/GAT/BV-03-C, TP/GAT/BV-04-<br>C, TP/CONN/UCON/BV-03-C, TP/CONN/UCON/BV-<br>02-C, TP/CONN/DCON/BV-01-C,<br>TP/CONN/DCON/BV-02-C, TP/CONN/DCON/BV-03-<br>C, TP/CONN/UCON/BV-04-C, TP/CONN/UCON/BV-<br>05-C, TP/CONN/CPUP/BV-01-C ,<br>TP/CONN/CPUP/BV-02-C , TP/CONN/CPUP/BV-03-<br>C, TP/BOND/BON/BV-01-C, TP/BOND/BON/BV-03-<br>C, TP/SEC/AUT/BV-11-C, TP/SEC/AUT/BV-12-C,<br>TP/PRIV/CONN/BV-05-C , TP/PRIV/CONN/BV-06-C ,<br>TP/PRIV/CONN/BV-07-C , TP/PRIV/CONN/BV-08-C ,<br>TP/PRIV/CONN/BV-09-C<br>TSE 4224: TP/DM/LEP/BV-03-C Update test<br>procedure<br>Fix TSE 4306: TP/BOND/BON/BV-01-C,<br>TP/BOND/BON/BV-03-C|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **369 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 3862: TCMT updates for TP/ADV/BV-01-C,<br>TP/ADV/BV-02-C, TP/ADV/BV-03-C, TP/ADV/BV-04-<br>C, TP/ADV/BV-05-C, TP/ADV/BV-06-C, TP/ADV/BV-<br>07-C, TP/ADV/BV-08-C, TP/ADV/BV-09-C,<br>TP/ADV/BV-10-C<br>TSE 4316 Fix TCMT for TP/GAT/BV-01-C<br>TSE 4423: Fix heading numbering for<br>TP/SEC/AUT/BV-13-C, TP/SEC/AUT/BV-14-C|
|20|4.0.1|2011-07-18|Prepare forpublication.|
||4.0.2r0|2011-11-17|TSE 4325: TP/SEC/CSIGN/BI-03-C,<br>TP/SEC/CSIGN/BI-04-C Rewrite without security<br>TSE 4332: new test cases TP/DM/LEP/BV-04-C,<br>TP/DM/LEP/BV-05-C, TP/DM/LEP/BV-06-C<br>TSE 4334: TP/SEC/SEM/BV-10-C: update MSC per<br>TSE 2633<br>TSE 4346: TP/SEC/SEM/BV-02-C: update Initial<br>condition<br>TSE 4363:<br>--Updated pass verdicts for TP/DISC/LIMP/BV-04-C,<br>TP/DISC/LIMP/BV-05-C, TP/DISC/GENP/BV-01-C,<br>TP/DISC/GENP/BV-02-C, TP/CONN/GCEP/BV-02-C,<br>TP/CONN/GCEP/BV-03-C, TP/CONN/GCEP/BV-04-<br>C, TP/CONN/SCEP/BV-01-C, TP/CONN/SCEP/BV-<br>02-C<br>--updated references, pass verdicts, & MSCs for<br>TP/DISC/GENP/BV-03-C, TP/DISC/GENP/BV-04-C,<br>TP/DISC/GENP/BV-05-C<br>TSE 4387: New test cases TP/SEC/AUT/BV-15-C,<br>TP/SEC/AUT/BV-16-C<br>TSE 4420: TP/BOND/NBON/BV-01-C,<br>TP/BOND/NBON/BV-02-C; Test procedure updates<br>TSE 4439: TP/CONN/CPUP/BV-06-C: Pass verdict.<br>TSE 4452: TP/SEC/AUT/BV-13-C: Add 2ndTest<br>procedure<br>TSE 4453: TP/SEC/AUT/BV-13-C: Correct test<br>purpose.<br>TSE 4455: TP/SEC/AUT/BV-11-C, TP/SEC/AUT/BV-<br>12-C: TCMT<br>TSE 4560: New test cases TP/GAT/BV-05-C,<br>TP/GAT/BV-06-C; update TCMT<br>TSE 4565: --TP/DISC/LIMM/BV-01-C,<br>TP/DISC/LIMM/BV-02-C, TP/DISC/GENM/BV-01-C<br>TP/DISC/GENM/BV-02-C: Pass verdict, References<br>--New test cases TP/DISC/LIMM/BV-03-C,<br>TP/DISC/LIMM/BV-04-C, TP/DISC/GENM/BV-03-C,<br>TP/DISC/GENM/BV-04-C<br>--TCMT updates<br>TSE 4571: TP/CONN/DCON/BV-02-<br>C,TP/CONN/UCON/BV-04-C update TCMT|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **370 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.02r1|2012-01-31|Accepted reviewer’s comments, updated graphic for<br>TP/SEC/AUT/BV-12-C, and made cover page date<br>current.|
|21|4.0.2|2012-03-30|Prepare forpublication.|
||4.0.3r0|2012-05-16|TSE 4568: TP/PRIV/CONN/BV-09-C: TCMT<br>TSE 4741: New test case TP/GAT/BV-07-C, updated<br>test case TP/PRIV/CONN/BV-07-C<br>TSE 4741: TCMT changes to<br>TP/PRIV/CONN/BV-05, 06, 07, 08, 09-C,<br>TP/PRIV/CONN/BV-01, 02, 03-C<br>TP/CONN/DCON/BV-02, 03-C<br>TP/CONN/UCON/BV-04, 05-C<br>TP/CONN/GCEP/BV-04-C<br>TP/GAT/BV-07-C<br>TSE 4573: TP/BOND/BON/BV-03-C and<br>TP/SEC/AUT/BV-11|12|13|14-C: TCMT<br>TSE 4608: TP/CONN/UCON/BV-01|02|03-C: MSCs<br>TSE 4618: TP/BOND/NBON/BV-03-C: Remove<br>“Store”<br>TSE 4619: TP/BOND/BON/BV-01-C,<br>TP/BOND/BON/BV-02-C, TP/BOND/BON/BV-03-C,<br>TP/BOND/BON/BV-04-C: Update MSCs<br>TSE 4622: TP/PRIV/CONN/BV-01-C<br>TSE 4623: TP/PRIV/CONN/BV-02-C<br>TP/PRIV/CONN/BV-03-C, TP/PRIV/CONN/BV-04-C<br>TSE 4624: TP/PRIV/CONN/BV-02-C: Fix reference<br>TSE 4625: TP/PRIV/CONN/BV-02-C: Fix test<br>procedure<br>TSE 4626: TP/PRIV/CONN/BV-03-C: Change Initial<br>condition<br>TSE 4650: TP/DISC/LIMM/BV-01-C,<br>TP/DISC/GENM/BV-01-C, TP/CONN/NCON/BV-02-C,<br>TP/CONN/NCON/BV-03-C: Pass verdict addition<br>TSE 4660: TP/DM/BON/BV-01-C TMCT change<br>TSE 4698 TP/PRIV/CONN/BV-04-C: Update test<br>procedure<br>TSE 4740: TP/SEC/SEM/BV-01 through 09-C:<br>Change Master/Slave to Initiator/Responder;<br>TP/SEC/SEM/BV-10-C: Change Master to Responder<br>and revise TCMT for Verify disconnection without<br>encryption.<br>TSE 4746: TP/CONN/DCON/BV-02-C:Update Initial<br>condition and Test procedure<br>TSE 4784: TP/CONN/GCEP/BV-03-C: Remove last<br>statement of Pass verdict.|
||4.0.3r1|2012-06-21|Fix Heading 5 numbering<br>TSE 4879: Delete TP/MOD/PAIR/BV-01-C,<br>TP/IDLE/NAD/BV-01-C<br>Update TCMT|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **371 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.0.3r2|2012-07-03|Add new test cases for CSA3:  TP/CONN/PRDA/BV-<br>01-C and TP/CONN/PRDA/BV-02-C.<br>TSE 4611: New test case TP/GAT/BV-08-C|
|22|4.0.3r3|2012-07-12|TSE 4620: TP/BROB/OBSV/BV-03-C: Revise initial<br>condition<br>Editorial corrections to the change history|
||4.0.4r0|2012-08-31|TSE: 4890: Remove TP/EST/CHE/BV-02-C, and all<br>references including deleting the line in the TCMT.<br>TSE 4889: Remove TP/EST/CHE/BV-01-C and<br>TP/EST/CHE/BV-01-C, and all references to them,<br>including their lines in the TCMT.<br>TSE 4786: Split TP/DM/NAD/BV-01 into two test<br>cases, added TP/DM/NAD/BV-02-C and added<br>TP/DM/NAD/BV-02-C to the TCMT.<br>TSE 4966: Added normative reference to CSA 3,<br>added new test case TP/BROB/OBSV/BV-05-C to<br>Operational Modes and Procedures on LE Physical<br>Channels, added TP/BROB/OBSV/BV-05-C to the<br>TCMT.<br>TSE 4873: Changes to test case TP/ADV/BV-06-C<br>and TP/ADV/BV-07-C.|
||4.0.4r1|2012-11-06|Updated Table of Contents to include Heading 4.<br>Fixed incorrect numberingfor all Heading5.|
||4.0.4r2|2012-11-15|TSE 4896: Added 6 new test cases for GAP<br>Authentication and Lost Bond CR, and added to<br>TCMT.<br>TP/SEC/AUT/BV-17-C (Correct Pairing after<br>Insufficient Authentication – Central role)<br>TP/SEC/AUT/BV-18-C (Correct Pairing after<br>Insufficient Authentication – Peripheral role)<br>TP/SEC/AUT/BV-19-C (Service Response Insufficient<br>Authentication – Central role)<br>TP/SEC/AUT/BV-20-C (Service response Insufficient<br>Authentication – Peripheral role)<br>TP/SEC/AUT/BV-21-C (Lost Bond – Initiator role)<br>TP/SEC/AUT/BV-22-C(Lost Bond – Responder role)|
||4.0.4r3|2012-11-16|Addressed review comments from Magnus:<br>- Edited TOC<br>- Edited Numbering (Heading 5)<br>- Reference for TP/SEC/AUT/BV-17-C should be 12<br>instead of 10.<br>- Removed the statement, “IUT supports security<br>mode 1 level 3” for the following test cases:<br>TP/SEC/AUT/BV-17-C, TP/SEC/AUT/BV-18-C,<br>TP/SEC/AUT/BV-19-C, TP/SEC/AUT/BV-20-C,<br>TP/SEC/AUT/BV-21-C, TP/SEC/AUT/BV-22-C.<br>- Edited test sequence numbering for<br>TP/SEC/AUT/BV-22-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **372 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.0.4r4,<br>4.0.4r5|2012-11-29,<br>2012-12-07|Per BQRB review included an additional reference in<br>section 5.6.6, Advertising and Scan Response Data<br>Format, to include the CSS document.<br>Added [13] Core Specification Supplement (CSS) v2,<br>Part A<br>Added reference to [13] to all test cases in section<br>5.6.6.<br>Editorial corrections|
|23|4.0.4|2012-12-07|Prepare for Publication|
||4.0.5r1|2012-12-20|Connectionless Broadcast Change Request|
||4.0.5r2|2013-01-02|Connectionless Broadcast Review:<br>Synchronizable and Non-Synchronizable Modes<br>moved from section 5.4 to 5.3<br>Synchronization Establishment moved from 5.4 to 5.7.|
||4.0.5r3|2013-01-22|Connectionless Broadcast Review (Jason & Magnus)<br>Edited Normative Reference 13 (CSS v2 per previous<br>revision history) and added CSA4 and cross-<br>references to CSA4 in the applicable test cases.<br>Removed sections only populated with N/A for Test<br>Conditions and Notes.<br>Revised the Test Condition for TP/MOD/SYN/BV-01-<br>C.|
||4.0.5r4|2013-01-24|Connectionless Broadcast Review (Jason, Alicia,<br>Meagan)<br>Conformance Section updated.<br>Misplaced MSCs corrected.|
||4.0.5r5|2013-01-28|Connectionless Broadcast Review (Alicia)<br>Updated Heading5 and TOC.|
||4.0.5r6|2013-01-28|Approved byBTI|
||4.0.5r6|2013-02-13|Approved byBQRB|
|24|4.0.5|2013-02-19|Prepare for Publication|
||4.0.6r1|2013-05-30|TSE 4838: New Test Cases:<br>TP/SEC/AUT/BV-23-C (Service Response –<br>insufficient encryption, peripheral)<br>TP/SEC/AUT/BV-24-C (Service Response –<br>insufficient encryption, central)<br>TCMT Updates:<br>Updated mapping  for TP/SEC/AUT/BV-16-C to add<br>“AND NOT GAP 0a/1”<br>Added TP/SEC/AUT/BV-24-C mapping, “(GAP 5/4<br>OR GAP 38/4) AND GAP 35/3 AND GAP 0a/1”<br>Updated mapping for TP/SEC/AUT/BV-15-C to add<br>“AND NOT GAP 0a/1”<br>Added TP/SEC/AUT/BV-24-C mapping, “GAP 5/3<br>AND GAP 25/3 AND GAP 25/7 AND GAP 0a/1”|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **373 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 4988: Updated Test Procedure for<br>TP/CONN/DCEP/BV-01-C and changed all text that<br>says “an unresolvable” to “non-resolvable” in<br>TP/CONN/DCEP/BV-02-C for consistency.<br>TSE 5015: Updated the initial condition and pass and<br>fail verdicts of TP/CONN/CPUP/BV-02-C.<br>TSE 5113: Updated initial condition in<br>TP/CONN/UCON/BV-05-C.<br>TSE 5120: Updated initial conditions of<br>TP/CONN/DCEP/BV-02-C and TP/CONN/SCEP/BV-<br>02-C to replace “unresolvable” with “non-resolvable”<br>to maintain consistencyin the document.|
||4.0.6r2,<br>4.0.6r3|2013-06-02,<br>2013-06-03|Integration reviews|
|25|4.0.6|2013-07-02|Prepare for Publication|
||4.0.7rT,<br>4.0.7rTr5,<br>4.0.7rTr6|2013-07-02,<br>2013-09-24,<br>2013-09-24|Template Conversion:<br>- Update of language to match BTI approved wording<br>(example, fail verdicts)<br>- Removal of Test Subgroup Objectives<br>- Removal of  sections marked “N/A”|
||4.1.0r01|2013-09-24|BR/EDR Secure Connections CR|
||4.1.0r02|2013-09-26|Updatedpictures to Visiographics where commented.|
||4.1.0r03|2013-09-26|32-bit UUID CR|
||4.1.0r04|2013-09-26|LE Privacy1.1 CR|
||4.1.0r05|2013-09-26|TSE 5293: Updated Security Mode 4 test cases,<br>TP/SEC/SEM/BV-07-C, TP/SEC/SEM/BV-09-C, and<br>TP/SEC/SEM/BV-10-C, test procedures to say<br>"Authentication Requirements" instead of "IO<br>Capabilities"<br>TSE 5279: Updated sentence in Test Procedure to<br>read "IUT establishes connection with the Lower<br>Tester again" in TP/BOND/NBON/BV-02-C.<br>TSE 5349: Update to MSCs for TP/CONN/NCON/BV-<br>01-C, TP/CONN/NCON/BV-02-C,<br>TP/CONN/NCON/BV-03-C, TP/CONN/PRDA/BV-01-<br>C, and TP/CONN/PRDA/BV-02-C.|
||4.1.0r06|2013-10-04|LE Dual Mode Topology CR<br>Updated test TP/DM/LEP/BV-01-C for 4.1 – IUT is<br>connectable and discoverable over BR/EDR and LE<br>Updated test TP/DM/LEP/BV-04-C for 4.1<br>Removed test TP/DM/LEP/BV-03-C<br>New tests TP/DM/LEP/BV-07-C, TP/DM/LEP/BV-08-<br>C, TP/DM/LEP/BV-09-C, TP/DM/LEP/BV-10-C,<br>TP/DM/LEP/BV-11-C.|
||4.1.0r07|2013-10-16|LE Link Layer TopologyCR|
||4.1.0r08|2013-10-22|Correction of CR implementation, removal of<br>TP/DM/LEP/BV-03-C via the DM Topology CR was<br>missed initially.|
||4.1.0r10|2013-10-28|Additional Comment from Mayank in the TCMT|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **374 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.1.0r11|2013-10-31|Amended TCMT to align with GAP.ICS 4.1.0r12,<br>including removing redundant pre-requisites where<br>possible, and tying support of BR/EDR/LE Peripheral<br>role connection-related test cases to support of<br>connectable modes.<br>Added 6 new test cases for CSSv4 AD Types:<br>TP/ADV/BV-11-C, TP/ADV/BV-12-C, TP/ADV/BV-13-<br>C, TP/ADV/BV-14-C, TP/ADV/BV-15-C, TP/ADV/BV-<br>16-C|
||4.1.0r13|2013-11-07|Chris: deleted EST/CHE/BV-01-C from the TCMT,<br>fixed selection expressions for DM/LEP/BV-01-C and<br>CONN/SCEP/BV-02-C respectively|
||4.1.0r14|2013-11-08|Review by Miles<br>Chris: Updated TCMT for TP/SEC/AUT/BV-17-C<br>through TP/SEC/AUT/BV-24-C.|
||4.1.0r15|2013-11-10|Revision of TCMT entries for TP/SEC/AUT/BV-17-C<br>through TP/SEC/AUT/BV-24-C.|
|26|4.1.0|2013-12-03|Prepare for Publication|
||4.1.1r00|2014-01-23|TSE 5422: Updated TCMT mapping for<br>TP/BROB/OBSV/BV-04-C and TP/BROB/OBSV/BV-<br>05-C.<br>TSE 5498: Added "AND GAP 0/3" to TCMT mapping<br>for TP/DM/NAD/BV-01-C<br>TSE 5477: Updated TCMT mapping for<br>TP/DM/LEP/BV-09-C and TP/DM/LEP/BV-11-C.<br>TSE 5455: Updated Pass Verdict # 1 for TP/ADV/BV-<br>13-C.|
||4.1.1r01|2014-04-07|TSE 5400: Revised MSC for TP/SEC/AUT/BV-19-C<br>and TP/SEC/AUT/BV-20-C. Updated Test Procedure<br>for TP/SEC/AUT/BV-23-C and TP/SEC/AUT/BV-24-C.<br>TSE 5414: Updated TCMT for TP/SEC/AUT/BV-18-C,<br>TP/SEC/AUT/BV-20-C, and TP/SEC/AUT/BV-22-C.<br>TSE 5553: Updated TCMT for TP/DM/NAD/BV-02-C.<br>TSE 5536: Updated Initial Condition of<br>TP/SEC/AUT/BV-16-C.<br>TSE 5456: Updated pass verdict and TCMT mapping<br>for TP/BROB/OBSV/BV-03-C and<br>TP/BROB/OBSV/BV-05-C.<br>TSE 5470: Updated TCMT mapping for<br>TP/BOND/BON/BV-01-C and TP/BOND/BON/BV-03-<br>C.<br>TSE 5544: Updated mapping for TP/DISC/LIMM/BV-<br>01-C to include GAP 22/2.|
||4.1.1r02|2014-04-10|TSE 5535: Updated TCMT mapping for<br>TP/DM/LEP/BV-01-C and TP/DM/LEP/BV-04-C to<br>add "AND GAP 0a/3" for 4.1 mapping.|
||4.1.1r03|2014-04-21|TSE 5596: Updated TCMT mapping for<br>TP/CONN/PRDA/BV-01-C and TP/CONN/PRDA/BV-<br>02-C.|
|27|4.1.1|2014-07-07|TCRL 2014-1 Publication|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **375 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.1.2r00|2014-10-20|TSE 5634: Corrected reference from GAP to LMP for<br>TP/SEC/SEM/BV-04-C, TP/SEC/SEM/BV-05-C,<br>TP/SEC/SEM/BV-06-C, TP/SEC/SEM/BV-07-C,<br>TP/SEC/SEM/BV-08-C, TP/SEC/SEM/BV-09-C,<br>TP/SEC/SEM/BV-10-C.<br>TSE 5770: Editorial correction to test description for<br>TP/BROB/BCST/BV-02-C. Add new row for the TCMT<br>for TP/BROB/BCST/BV-02-C and map to GAP 6/2<br>AND GAP 8/2.<br>TSE 5795: Corrected the order of Lower Tester and<br>IUT in Pass Verdicts for TP/BROB/OBSV/BV-03-C,<br>TP/BROB/OBSV/BV-05-C.<br>TSE 5933: Updated TCMT mapping for<br>TP/IDLE/NAMP/BV-01-C and TP/IDLE/NAMP/BV-02-<br>C.<br>TSE 5836: Update to Initial Condition, Test<br>Procedure, MSC, and Pass verdict for<br>TP/SEC/AUT/BV-19-C and TP/SEC/AUT/BV-20-C.|
||4.2.0r00|2014-11-14|Integrated Section 6 of<br>Core_LE_Secure_Connections.TS.CR.R16 & 1.1 –<br>1.2 of Core_Enhanced_Privacy_1_2.TS.CR.R05|
||4.2.0r01,<br>4.2.0r02,<br>4.2.0r03|2014-11-19,<br>2014-11-21,<br>2014-11-24|Integration reviews|
|28|4.2.0|2014-12-04|Prepared for TCRL 2014-2publication|
||4.2.1r00|2015-05-08|TSE 6080: Corrected Pass verdicts in<br>TP/CONN/DCEP/BV-01-C, TP/CONN/DCEP/BV-03-<br>C, and TP/CONN/DCEP/BV-04-C. Updated TCMT for<br>TP/CONN/DCEP/BV-04-C.<br>TSE 5934: Revised test procedure in<br>TP/SEC/AUT/BV-12-C<br>TSE 6161: Added BR/EDR discovery step to<br>TP/DM/LEP/BV-11-C.<br>TSE 6230: Revised TCMT mapping for<br>TP/SEC/SEM/BV-25-C and 30-C to require Secure<br>Connections Only Mode.<br>TSE 6272: Deleted unresolved “if” in Pass verdicts of<br>TP/DISC/LIMM/BV-02-C, 03-C, and 04-C<br>TSE 6233: Corrected typo in TCMT entry for<br>TP/CONN/SCEP/BV-03-C<br>TSE 6253: Corrected Test Procedure step numbering<br>in TP/DM/LEP/BV-19-C<br>TSE 6298: Corrected typo in TCMT entry for<br>TP/BROB/OBSV/BV-03-C<br>TSE 6385: Corrected Test Procedure step error in<br>TP/DM/LEP/BI-02-C<br>TSE 6296: Updated tests TP/SEC/SEM/BV-21-C<br>through 30-C to clarify "channel establishment" for LE<br>Secure Connections.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **376 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.2.1r01|2015-06-22|Integrated changes for Core Specification Supplement<br>(CSS) v6.<br>Efficient Non-Connectable Advertising: Revised<br>references and pass verdicts to accommodate the<br>Efficient NCA changes in:  TP/BROB/BCST/BV-01-C,<br>TP/BROB/BCST/BV-03-C, TP/BROB/BCST/BV-04-C,<br>TP/BROB/BCST/BV-05-C, TP/DISC/NONM/BV-01-C,<br>TP/DISC/LIMM/BV-01-C, TP/DISC/LIMM/BV-03-C,<br>TP/DISC/GENM/BV-01-C, TP/DISC/GENM/BV-03-C,<br>TP/ADV/BV-03-C.<br>Advertising URI: Added new test TP/ADV/BV-17-C<br>and a correspondingnew row to TCMT.|
||4.2.1r02|2015-06-23|CSSv6 changes reviewed by Magnus Sommansson<br>and Chris Church.|
|29|4.2.1|2015-07-14|Prepared for TCRL 2015-1publication|
||4.2.2r00|2015-10-09|TSE 6681: Revised initial conditions for<br>TP/BROB/BCST/BV-03-C.<br>TSE 6490: Corrected steps 6 and 7 in MSC for<br>TP/DM/LEP/BV-18-C.<br>TSE 6387: Removed Security Mode 4 from MSC for<br>TP/SEC/AUT/BV-01-C; added title for<br>TP/SEC/AUT/BV-01-C; and added test condition to<br>initial conditions for TP/SEC/AUT/BV-01-C.<br>TSE 6600: Removed TP/ADV/BV-06-C and<br>TP/ADV/BV-07-C.<br>TSE 6715: Updated MSC in TP/BOND/NBON/BV-03-<br>C to correct pairing message details from IUT to<br>Lower Tester<br>TSE 6169 & 6323: Updated TCMT and references to<br>resolve Core Privacyfeature issues.|
||4.2.2r03|2015-11-16|TSE 6778: Corrected test case mapping from TSE<br>6169 forTP/BROB/OBSV/BV-06-C,<br>TP/CONN/DCEP/BV-05-C, TP/CONN/DCEP/BV-06-C|
|30|4.2.2|2015-12-22|Prepared for TCRL 2015-2publication|
||4.2.3r00|2015-01-15|TSE 6862: Added parentheses to Item for Test Case<br>Mappingfor TP/DM/LEP/BV-06-C.|
||4.2.3r01|2016-03-04|TSE 6978: Corrected “Undirected” to “Directed” in<br>Test Condition for test cases TP/CONN/DCEP/BV-03-<br>C and TP/CONN/DCEP/BV-04-C.|
||4.2.3r02|2016-04-01|TSE 6955: Updated Figure 4.2 (Inquiry Procedure)<br>MSC.<br>Added new section (Figure 4.3 Paging Procedure)<br>and MSC.<br>Global edit. Updated all Section 4 figure caption<br>numbers (Figure 4.3 – 4.51).<br>Added heading title and updated "Inquiry Procedure"<br>hyperlink in Initial Condition for test cases<br>TP/IDLE/BON/BV-01-C, TP/IDLE/BON/BV-02-C,<br>TP/IDLE/BON/BV-03-C, TP/IDLE/BON/BV-04-C,<br>TP/IDLE/BON/BV-05-C, TP/IDLE/BON/BV-06-C,<br>TP/EST/LIE/BV-02-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **377 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.2.3r03|2016-04-06|TSE 6995: Updated TCMT, LE Secure Connections –<br>Host tests: TP/DM/LEP/BI-01-C, TP/DM/LEP/BI-02-C,<br>TP/DM/LEP/BV-13-C, TP/DM/LEP/BV-18-C.<br>TSE 7014: Updated TCMT item for test case<br>TP/CONN/GCEP/BV-03-C.|
|31|4.2.3|2016-07-13|Prepared for TCRL 2016-1publication.|
||5.0.0r00|2016-10-03|Issue 7732: Added two new references to References<br>section. Added new LE Only Protocol Group to Test<br>Strategy section. Added new Identifier and Function<br>Identifier to TP Naming Conventions section. Added<br>three new Identifiers and Subfunction Identifiers to TP<br>Naming Conventions section. Added new section<br>“Periodic Advertising Modes and Procedures” and<br>four new test cases: TP/PADV/PASM/BV-01-C,<br>TP/PADV/PAM/BV-01-C, TP/PADV/PASE/BV-01-C,<br>and TP/PADV/PASE/BV-02-C. Added references for<br>four new test cases to TCMT.|
||5.0.0r01|2016-10-07|TSE 7240: Updated test procedure and replaced MSC<br>in TP/SEC/AUT/BV-11-C to correct authentication<br>references. Replaced MSC in TP/SEC/AUT/BV-12-C.<br>TSE 7570: Updated tests TP/BOND/BON/BV-01-C<br>through 04-C for device/network privacy (erratum<br>6356).<br>TSE 7324: Updated first paragraph of test case<br>TP/CONN/CPUP/BV-03-C.|
||5.0.0r02|2016-11-11|Issue 7803: Updated Pass Verdicts for<br>TP/BROB/BCST/BV-01-C – 05-C,<br>TP/DISC/NONM/BV-01-C & 02-C, TP/DISC/LIMM/BV-<br>01-C – 04-C, TP/DISC/GENM/BV-01-C – 04-C,<br>TP/CONN/NCON/BV-02-C & 03-C,<br>TP/CONN/UCON/BV-01-C – 06-C,<br>TP/CONN/GCEP/BV-02-C, 03-C & 06-C,<br>TP/CONN/DCEP/BV-06-C, TP/DM/LEP/BV-01-C,<br>04-C, 06-C – 11-C. Updated TCMT items for<br>TP/BROB/BCST/BV-02-C, TP/DISC/NONM/BV-02-C,<br>TP/CONN/UCON/BV-01-C, TP/DISC/LIMM/BV-01-C,<br>TP/DISC/LIMM/BV-02-C, TP/DISC/LIMM/BV-03-C,<br>TP/DISC/GENM/BV-01-C, TP/DISC/GENM/BV-02-C,<br>TP/DISC/GENM/BV-03-C, TP/DISC/GENM/BV-04-C,<br>TP/CONN/NCON/BV-02-C, TP/DM/LEP/BV-07-C,<br>TP/CONN/UCON/BV-02-C, TP/BROB/BCST/BV-<br>05-C.|
|32|5.0.0|2016-12-13|Approved by BTI. Prepared for TCRL 2016-2<br>publication.|
||5.0.0 (2nd<br>edition)|2016-12-15|TSE 8263: Corrected test case mapping for 25 test<br>cases requiring inclusion of Core Specification 5.0<br>support (GAP 0a/5).<br>Approved by BTI and re-issued for TCRL 2016-2<br>publication.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **378 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||5.0.1r00|2017-03-08|TSE 7918: Corrected test case mapping for<br>GAP/SEC/SEM/BV-21-C, GAP/SEC/SEM/BV-22-C,<br>GAP/SEC/SEM/BV-26-C, GAP/SEC/SEM/BV-27-C.<br>TSE 8357: Corrected references to section 14.1 and<br>removed LL and LMP from MSCs for<br>GAP/DM/LEP/BV-12-C, GAP/DM/LEP/BV-13-C,<br>GAP/DM/LEP/BV-14-C, GAP/DM/LEP/BV-15-C,<br>GAP/DM/LEP/BV-16-C, GAP/DM/LEP/BV-17-C,<br>GAP/DM/LEP/BV-18-C, GAP/DM/LEP/BV-19-C.|
||5.0.1r01|2017-03-28|TSE 8356: Updated the Test Procedure about the<br>Lower Tester for GAP/CONN/CPUP/BV-06-C,<br>GAP/CONN/CPUP/BV-08-C. Updated the Pass<br>Verdict for GAP/CONN/CPUP/BV-06-C,<br>GAP/CONN/CPUP/BV-08-C. Removed<br>TP/CONN/CPUP/BV-07-C since it is covered by<br>GAP/CONN/CPUP/BV-01-C. Removed<br>TP/CONN/CPUP/BV-09-C since it is covered by<br>GAP/CONN/CPUP/BV-04-C. Removed<br>TP/CONN/CPUP/BV-07-C from TCMT. Removed<br>TP/CONN/CPUP/BV-09-C from TCMT.|
||5.0.1r02|2017-04-11|TSE 8360: Updated GAP/IDLE/DED/BV-01-C: Added<br>“[Device Discovery and Name Discovery – Secure<br>Simple Pairing Not Supported by IUT]” to heading,<br>added “that does not support Secure Simple Pairing”<br>to introduction, modified the initial condition, and<br>updated MSC (Figure 4.43).<br>Updated GAP/IDLE/DED/BV-02-C: Added “[Device<br>Discovery and Name Discovery – Secure Simple<br>Pairing Supported by IUT]” to heading, added “which<br>supports Secure Simple Pairing” to introduction,<br>modified the initial condition and updated MSC<br>(Figure 4.44).<br>Corrected TCMT for GAP/IDLE/DED/BV-01-C and<br>GAP/IDLE/DED/BV-02-C and updated the<br>descriptions.<br>TSE 8359: Added reference [25] to test spec<br>references section. Changes made to<br>GAP/SEC/SEM/BV-04-C: Updated reference section<br>to “[25] Section 5.2.2”, modified the initial condition,<br>and updated MSC (Figure 4.23).<br>Changes made to GAP/SEC/SEM/BV-05-C: Updated<br>reference section to “[25] Section 5.2.2”, updated<br>MSC (Figure 4.29), modified the test procedure and<br>pass verdict.<br>Changes made to GAP/SEC/SEM/BV-06-C: Modified<br>introduction, test procedure, and pass verdict,<br>updated reference section to “[25] Section 5.2.2”, and<br>updated MSC Figure (4.30).<br>Changes made to GAP/SEC/SEM/BV-07-C: Modified<br>introduction, updated reference section to “[25]<br>Section 5.2.2”, and updated MSC Figure(4.31).|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **379 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||Changes made to GAP/SEC/SEM/BV-08-C: Modified<br>introduction, updated reference section to “[25]<br>Section 5.2.2”, and updated MSC Figure (4.32).<br>Changes made to GAP/SEC/SEM/BV-09-C: Modified<br>introduction and pass verdict, updated reference<br>section to “[25] Section 5.2.2”, and updated MSC<br>Figure (4.33).<br>Changes made to GAP/SEC/SEM/BV-10-C: Modified<br>the introduction and pass verdict, updated reference<br>section to “[25] Section 5.2.2”, and updated MSC<br>Figure(4.34).|
||5.0.1r03|2017-05-10|Converted to new Test Case ID conventions as<br>defined in TSTO v4.1.|
|33|5.0.1|2017-07-05|Approved by BTI. Prepared for TCRL 2017-1<br>publication.|
||5.0.2r00|2017-07-21|TSE 9047: Clarifies advertising event type in the test<br>procedure of GAP/BROB/OBSV/BV-05-C and revises<br>the MSC.|
||5.0.2r01|2017-08-22|TSE 9665: Changed MSC values for SC bit to 0 in<br>GAP/DM/LEP/BV-13-C and 17-C - ...19-C which<br>previouslyincorrectlyshowed SC bit =1.|
||5.0.2r02|2017-10-13|TSE 9912: Revised GAP/ADV/BV-03-C expected<br>outcome.|
|34|5.0.2|2017-12-07|Approved by BTI. Prepared for TCRL 2017-2<br>publication.|
||5.0.3r00-01|2018-02-16 –<br>2018-04-12|TSE 10182 (rating 2): Revised mapping to include<br>NOT (GAP 0a/3 OR GAP 0a/4 OR GAP 0a/5) for<br>GAP/CONN/ACEP/BV-02-C in TCMT.<br>TSE 10381 (rating 3): Editorial revisions to<br>GAP/GAT/BV-04-C reference and MSC.|
|35|5.0.3|2018-07-02|Approved by BTI. Prepared for TCRL 2018-1<br>publication.|
||5.0.4r00-r05|2018-07-20 -<br>2018-11-13|Incorporated Core_PAST_CLE_TEST_CR_r05:<br>Modified test case description, Test Purpose, and<br>figure caption for GAP/PADV/PASM/BV-01-C,<br>GAP/PADV/PAM/BV-01-C, GAP/PADV/PASE/BV-01-<br>C, GAP/PADV/PASE/BV-02-C. Added 6 new test<br>cases to TS and TCMT GAP/PADV/PASE/BV-03-C -<br>06-C; GAP/PADV/PAST/BV-01-C, 02-C.<br>Incorporated Core Minor Enhancements Batch 1 Test<br>CRr10-clean: Modified Pass Verdict for<br>GAP/PADV/PASM/BV-01-C.<br>TSE 10425 (rating 3): Updated test purpose, initial<br>condition, test procedure, MSC, and pass verdict for<br>test cases GAP/SEC/AUT/BV-23-C and 24-C.<br>TSE 10874 (rating 2): In TCMT, added GATT 1/1 to<br>test cases GAP/SEC/AUT/BV-17-C and 19-C.<br>TSE 10875 (rating 2): In TCMT, added GAP 11/2 to<br>test case GAP/BROB/BCST/BV-05-C.<br>TSE 10883 (rating 2): In TCMT, added GAP 17/4 to<br>test case GAP/BROB/OBSV/BV-06-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **380 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 11113 (rating 4): Added new test case<br>GAP/PRIV/CONN/BI-01-C; updated TCMT with new<br>test case.<br>TSE 10585 (rating 3): Pass verdict for test case<br>GAP/PADV/PASM/BV-01-C has already been<br>updated per Core Minor Enhancements Batch 1 Test<br>CRr10-clean.<br>Replaced [X] values with actual values. Added new<br>reference for Bluetooth Core Specification version 5.1.<br>Updated Madrid styles - changed light grey text to<br>black text.|
||5.1.0r00-r01|2018-11-13 -<br>2018-12-07|Updated revision number from 5.0.4 to 5.1.0 to align<br>with the adoption of Core Specification version 5.1.<br>Updated test case mapping for 26 test cases to be<br>inclusive of new Core Spec version 5.1(GAP 0a/6).|
|36|5.1.0|2018-12-07|Approved by BTI. Prepared for TCRL 2018-2<br>publication.|
||5.1.1r00–r08|2019-04-09–<br>2019-07-18|TSE 11417 (rating 3): Modified test step, replaced<br>MSC and updated Pass Verdict for test cases<br>GAP/CONN/DCON/BV-04-C and -05-C.<br>TSE 10916 (rating 3): Updated Test Purpose,<br>Reference, Test Procedure steps, MSC, and Pass<br>verdict as appropriate for test cases<br>GAP/SEC/SEM/BV-21-C – -24-C and -26-C – -29-C;<br>updated TCMT accordingly.<br>Incorporated changes associated with Key<br>Negotiation specification erratum 11838: Added new<br>sections to the “Security Modes - Slave” section with<br>test cases for Invalid Encryption Key Size in Security<br>Mode 2, Security Mode 4, and LE Security Mode 1 for<br>devices operating over BR/EDR transport (new test<br>cases GAP/SEC/SEM/BI-01-C – -12-C).<br>Incorporated changes associated with Key<br>Negotiation specification erratum 11838: Updated to<br>indicate if the IUT enforces a minimum encryption key<br>size of 56 bits; that has a range of 7–16 octets<br>(updated sections GAP/SEC/SEM/BI-01-C (initial<br>condition, MSC, test procedure, and pass verdict);<br>section containing test cases GAP/SEC/SEM/BI-11-C<br>and -02-C – -04-C (initial condition, MSC, test<br>procedure, and minimum key sizes in test case table);<br>test case GAP/SEC/SEM/BI-05-C (initial condition,<br>MSC, test procedure, and pass verdict); section<br>containing test cases GAP/SEC/SEM/BI-12-C and -<br>06-C – -08-C (initial condition, MSC, test procedure,<br>and minimum key sizes in test case table); test case<br>GAP/SEC/SEM/BI-09-C(MSC). Updated TCMT.|
|37|5.1.1|2019-08-01|Approved by BTI. Prepared for TCRL 2019-1<br>publication.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **381 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||p38r00–r04|2019-08-06 –<br>2019-11-22|Added test groups to accommodate adoption of Core<br>Specification v5.2 with regard to Isochronous<br>Channels CR r20 (includes Issues 11742, 11762,<br>11777, 11778, 11779, 11783,11786, 11804, 11817,<br>11819, 11820, 11852, 11917, 11919, 11928, 11929,<br>11930, 11983, 11740, 11801, 11941, 12029, 12030,<br>12043, 12052, 12053, 12054, 12055, 12059, 12061,<br>12071, 12072, 12073, 12077, 12084, 12031, 12078,<br>12094, 12095, 12106, 12107, 12130, 12132, 12133,<br>12251, 12280, and 12321). Added Section 4.4.5,<br>"Security Modes – Observer Role", subsection<br>4.4.5.1, "LE Security Mode 3 – Observer Role,<br>Acceptor", containing new test cases<br>GAP/SEC/SEM/BV-31-C – -33-C; subsection 4.4.5.2<br>for new test case GAP/SEC/SEM/BI-13-C; Section<br>4.4.6 "Security Modes – Broadcaster Role",<br>subsection 4.4.6.1, "LE Security Mode 3 –<br>Broadcaster Role, Initiator", containing new test cases<br>GAP/SEC/SEM/BV-34-C – -36-C; added Section<br>4.6.9, "Broadcast Isochronous Streaming Modes and<br>Procedures", and subsections 4.6.9.1, "Broadcast<br>Isochronous Synchronizability mode", and 4.6.9.1.1<br>for new test case GAP/BIS/BSM/BV-01-C, and<br>subsections 4.6.9.2, "Broadcast Isochronous<br>Broadcasting Mode", and 4.6.9.2.1 for new test case<br>GAP/BIS/BBM/BV-01-C; updated TCMT accordingly;<br>updated references section with new Core<br>Specification.<br>TSE 12354 (rating 4): Deleted test cases<br>GAP/ADV/BV-15-C and -16-C to eliminate tests that<br>require the IUT to advertise with data types that are<br>not allowed in AD or SRD per CSS 8. Updated TCMT<br>accordingly.<br>TSE 11639 (rating 1): Removed test case<br>GAP/PRIV/CONN/BI-01-C and updated the TCMT<br>accordingly.<br>TSE 11968 (rating 1): Removed unused references,<br>combined ICS and IXIT proforma, changed cross-<br>references within doc from [4] to [2] and from [6] 4 to<br>[1] 4.1.1 as requested in problem statement, and<br>updated two references from the non-combined IXIT<br>reference to the new combined IXIT reference.<br>TSE 12447 (rating 2): Updated Pass Verdict for test<br>cases GAP/CONN/ACEP/BV-03-C and -04-C;<br>GAP/CONN/GCEP/BV-01-C, -04-C – -06-C;<br>GAP/CONN/SCEP/BV-03-C; GAP/CONN/DCEP/BV-<br>01-C, – -06-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **382 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 12754 (rating 2): Deleted test cases<br>GAP/BROB/OBSV/BV-03-C and -04-C;<br>GAP/GAT/BV-01-C - -03-C, -07-C and -08-C;<br>GAP/CONN/DCON/BV-02-C and -03-C;<br>GAP/CONN/UCON/BV-04-C and -05-C;<br>GAP/SEC/AUT/BV-15-C and -16-C;<br>GAP/PRIV/CONN/BV-01-C - -09-C;<br>GAP/CONN/ACEP/BV-02-C; GAP/CONN/GCEP/BV-<br>03-C and -04-C; GAP/CONN/SCEP/BV-02-C; and<br>GAP/CONN/DCEP/BV-02-C and -04-C and updated<br>TCMT accordingly. Subsequent CR added a<br>preamble section for “GAP Mandatory Characteristics”<br>and fixed links in test cases GAP/GAT/BV-05-C and -<br>06-C to address procedures previously cross-<br>referenced to in TCs deleted as part of this TSE.<br>TSE 12731 (rating 1): Updated initial condition of test<br>cases GAP/IDLE/NAMP/BV-01-C and -02-C;<br>GAP/CONN/TERM/BV-01-C; GAP/SEC/CSIGN/BV-<br>01-C and -02-C; GAP/SEC/CSIGN/BI-01-C – -04-C<br>(GAP/GAT/BV-01-C deleted as part of TSE 12754).<br>TSE 12927 (rating 1): Globally fixed “Lower/Upper<br>Tester expects” types of wording to “Lower/Upper<br>Tester receives” types of wording where appropriate.<br>Integration review feedback: Resolved .X and Milan<br>references with real numbers.<br>Revised document numbering convention, setting last<br>release publication of 5.1.1 as p37; added publication<br>number column to Revision History.|
|38|p38|2020-01-07|Approved by BTI on 2019-12-22. Prepared for<br>TCRL 2019-2publication.|
||p39r00–r06|2020-06-24 –<br>2020-11-18|TSE 13341 (rating 4): Updated to accommodate<br>allowing SM1L2 and SM1L3 to use LE Secure<br>Connections pairing only, as follows: updated section<br>containing test case GAP/SEC/SEM/BV-21-C to a<br>table-based TCID config and added new test cases<br>GAP/SEC/SEM/BV-37-C and -38-C; updated section<br>containing test case GAP/SEC/SEM/BV-22-C to a<br>table-based TCID config and added new test cases<br>GAP/SEC/SEM/BV-39-C and -40-C; updated test<br>purpose and test procedure for test cases<br>GAP/SEC/SEM/BV-23-C, -24-C, -28-C, and -29-C;<br>updated section containing test case<br>GAP/SEC/SEM/BV-26-C to a table-based TCID config<br>and added new test cases GAP/SEC/SEM/BV-41-C<br>and -42-C; updated section containing test case<br>GAP/SEC/SEM/BV-27-C to a table-based TCID config<br>and added new test cases GAP/SEC/SEM/BV-43-C<br>and -44-C; updated TCMT accordingly.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **383 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 13140 (rating 3): Corrected issues with<br>Broadcast Code and LL Test Criteria, affecting most<br>aspects of the test procedures for test cases<br>GAP/SEC/SEM/BV-31-C, -32-C, -34-C, and -35-C<br>and GAP/SEC/SEM/BI-13-C; deleted test cases<br>GAP/SEC/SEM/BV-33-C and -36-C. Updated TCMT<br>accordingly.<br>TSE 15150 (rating 4): To support new LE Audio<br>Security Consideration requirements, in "Security<br>Mode 4, Responder - Invalid Encryption Key Size"<br>section: added a reference section number, for test<br>case GAP/SEC/SEM/BI-04-C added "128 bit" to the<br>test name, added new test cases GAP/SEC/SEM/BI-<br>14-C – -16-C; in "Security Mode 4, Initiator - Invalid<br>Encryption Key Size" section: for test case<br>GAP/SEC/SEM/BI-08-C added "128 bit" to the test<br>name, added new test cases GAP/SEC/SEM/BI-17-C<br>– -19-C; updated TCMT accordingly.<br>TSE 15762 (rating 4): To address adding Minimum<br>128 Bit Key Size for the LE ICS entry, modified<br>section containing TC GAP/SEC/SEM/BI-09-C by<br>moving that TC to a TC Config table and adding new<br>TCs GAP/SEC/SEM/BI-20-C and -21-C and updating<br>the test heading, test purpose, test steps, and pass<br>verdict; modified section containing TC<br>GAP/SEC/SEM/BI-10-C by moving that TC to a TC<br>Config table and adding new TCs GAP/SEC/SEM/BI-<br>22-C and -23-C and updating the test heading, test<br>purpose, test steps, and pass verdict. Updated TCMT<br>accordingly.<br>TSE 15432 (rating 1): Editorials to address<br>Erratum 15348, globally change “White List” to “Filter<br>Accept List”, including in MSCs.<br>TSE 15447 (rating 1): Editorials to address<br>Erratum 15353 (Vol 3), globally change “Master” to<br>“Central” and “Slave” to “Peripheral” including in<br>MSCs.<br>Made template-related editorials, including updating<br>Conformance and Pass/Fail Verdict Conventions text,<br>updating TCID headings, adding Appropriate<br>Language reference, and making Consistency<br>Checker fixes.|
|39|p39|2020-12-22|Approved by BTI on 2020-12-03. Prepared for<br>TCRL 2020-1publication.|
||p40r00–r16|2020-12-23 –<br>2021-06-10|TSE 12791 (rating 1): Replaced MSC for test<br>procedure B for TC GAP/SEC/AUT/BV-13-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **384 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 12794 (rating 2): Removed preamble “Bring IUT<br>to no_link_key Available (IUT=slave, security mode<br>3)”. Removed the following test cases and their TCMT<br>entries associated with security mode 1 and security<br>mode 3: GAP/SEC/AUT/BV-01-C,<br>GAP/SEC/SEM/BV-01-C and -03-C,<br>GAP/IDLE/DED/BV-01-C, and GAP/IDLE/BON/BV-<br>01-C. Removed “(NOT GAP 2/6)” from the TCMT<br>expression for test case GAP/IDLE/BON/BV-02-C.<br>Edited references to security modes in initial<br>conditions for test cases GAP/IDLE/GIN/BV-01-C,<br>GAP/IDLE/LIN/BV-01-C, GAP/IDLE/BON/BV-02-C<br>and -03-C, and GAP/EST/LIE/BV-02-C.<br>TSE 12856 (rating 1): Updated instances of “Simple<br>Pairing” to read “Secure Simple Pairing”, which<br>involved replacing MSCs for test cases<br>GAP/SEC/SEM/BV-11-C – -15-C, -18-C, and -19-C<br>and GAP/IDLE/BON/BV-03-C – -06-C; replacing<br>MSCs and updating pass verdict for test cases<br>GAP/MOD/NPAIR/BV-03-C and GAP/SEC/SEM/BV-<br>05-C and -09-C; replacing MSCs and updating test<br>purpose and pass verdict for test cases<br>GAP/SEC/SEM/BV-06-C and -07-C; and replacing<br>MSCs and updating test procedure and pass verdict<br>for test case GAP/SEC/SEM/BV-10-C.<br>TSE 13120 (rating 2): Updated Initial Condition and<br>Pass Verdict of TC GAP/ADV/BV-17-C.<br>TSE 13158 (rating 2): Updated test procedure and<br>pass verdict for test case GAP/CONN/UCON/BV-06-<br>C.<br>TSE 13194 (rating 2): Corrected TCMT entry for test<br>cases GAP/SEC/SEM/BI-04 and -08-C.<br>TSE 13285 (rating 4): Updated<br>terminology/abbreviation table; changed 4.3.6 section<br>title from “pairable” to “bondable”; deleted test case<br>GAP/MOD/NPAIR/BV-01-C; changed TCIDs<br>GAP/MOD/NPAIR/BV-02-C to GAP/MOD/NBON/BV-<br>02-C and GAP/MOD/NPAIR/BV-03-C to<br>GAP/MOD/NBON/BV-03-C and modified Initial<br>Condition, MSC, Test Procedure, and Pass Verdict;<br>updated Test Procedure for test case<br>GAP/DM/NBON/BV-01-C; updated TCMT<br>accordingly.<br>TSE 13373 (rating 1): Made minor revisions to the<br>revision history for TSE 12447 from the 2019-2<br>release to remove references to test cases that are no<br>longer in the Test Suite.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **385 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 13381 (rating 2): Updated initial conditions for<br>test cases GAP/CONN/DCON/BV-04-C and -05-C,<br>GAP/CONN/UCON/BV-06-C, GAP/CONN/ACEP/BV-<br>03-C and -04-C, GAP/CONN/GCEP/BV-05-C and -06-<br>C, GAP/CONN/SCEP/BV-03-C, and<br>GAP/CONN/DCEP/BV-05-C and -06-C to allow a<br>general connection procedure and exchange security<br>keys for Privacy-related test cases.<br>TSE 13481 (rating 2): Updated MSC to align better<br>with test procedure for section containing test cases<br>GAP/SEC/SEM/BV-21-C, -37-C, and -38-C.<br>TSE 13585 (rating 3): To address Erratum 13407,<br>added a new test step to the Test Procedures for TCs<br>GAP/BOND/BON/BV-01-C – -04-C.<br>TSE 14791 (rating 4): To address an issue with<br>L2CAP connection parameter update, updated TCs<br>GAP/CONN/CPUP/BV-01-C – -03-C, and added new<br>TC GAP/CONN/CPUP/BV-10-C. Updated TCMT<br>accordingly.<br>TSE 14861 (rating 4): To address Erratum 12322,<br>added new TC GAP/PRIV/CONN/BV-12-C; updated<br>TCMT accordingly.<br>TSE 14910 (rating 2): Updated the Pass Verdict for<br>TC GAP/CONN/DCON/BV-04-C.<br>TSE 14973 (rating 1): Changed the Test Purpose of<br>TC GAP/PADV/PAST/BV-01-C to address a copy-<br>paste error.<br>TSE 15026 (rating 4): To address E13335, updated<br>TCs GAP/SEC/SEM/BV-05-C – -07-C, -09-C, -13-C –<br>-15-C, -18-C, and -19-C and moved them into TCID<br>tables with new TCs GAP/SEC/SEM/BV-47-C – 55-C.<br>Left GAP/SEC/SEM/BV-10-C as modified for 15915<br>and added new TC GAP/SEC/SEM/BI-24-C as a<br>standalone test. Updated TCMT accordingly.<br>TSE 15078 (rating 4): Added new TCs<br>GAP/DM/LEP/BV-20-C – -23-C to address an issue<br>with missing tests for not overwriting an existing key<br>with a key that is weaker in strength or MITM<br>protection; updated TCMT accordingly.<br>TSE 15170 (rating 1): Typo fix in Test Purpose of TC<br>GAP/DM/LEP/BV-18-C and corrected “. . ” globally.<br>TSE 15521 (rating 4): To address E11787, Failed<br>encryption when bond no longer exists or wrong<br>device is connected, added new TC<br>GAP/SEC/SEM/BV-45-C. Updated TCMT accordingly.<br>TSE 15601 (rating 4): To address E15385, added two<br>new sections containing new TCs GAP/SEC/AUT/BV-<br>25-C – 28-C. Updated TCMT accordingly.<br>TSE 15676 (rating 2): Clarified the initial conditions for<br>TCs GAP/CONN/CPUP/BV-01-C – -06-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **386 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 15689 (rating 4): To address E15498, added new<br>TC GAP/ADV/BV-18-C to “AD Type – Advertising<br>Interval” section, previously containing only TC<br>GAP/ADV/BV-14-C. Updated TCMT accordingly.<br>TSE 15841 (rating 1): Copy-paste error fix in test step<br>of TC GAP/PADV/PASE/BV-06-C.<br>TSE 15915 (rating 4): To address E15255, Add error<br>code return for Credit based Connection request test,<br>updated “Security Mode 4 – Responder” section,<br>which previously included only TC<br>GAP/SEC/SEM/BV-10-C, and added new TC<br>GAP/SEC/SEM/BV-46-C. Updated TCMT accordingly.<br>TSE 15950 (rating 2): Updated test procedure and<br>replaced MSC for TC GAP/GAT/BV-05-C.<br>TSE 16098 (rating 2): Updated MSCs and test steps<br>of TCs GAP/PADV/PAST/BV-01-C and -02-C to set<br>up the IUT to sync with the Lower Tester.<br>TSE 16221 (rating 2): Updated test purpose, test<br>procedure, and pass verdict for TC<br>GAP/BOND/NBON/BV-03-C.<br>TSE 16369 (rating 2): Replaced MSCs to remove the<br>Page Scan Mode parameter in TCs<br>GAP/MOD/LDIS/BV-01-C and -02-C and<br>GAP/MOD/GDIS/BV-01-C per E16209.<br>TSE 16410 (rating 2): Updated TC<br>GAP/SEC/AUT/BV-20-C to make steps clearer.<br>TSE 16507 (rating 1): Deleted a legacy Initial<br>Condition that was removed from Core spec v4.1 from<br>TCs GAP/CONN/GCEP/BV-01-C and -02-C and<br>/SCEP/BV-01-C.<br>TSE 16571 (rating 2): Made TCMT corrections<br>needed for LE Secure Connections only tests.<br>Affected TCs: GAP/SEC/SEM/BV-21-C<br>GAP/SEC/SEM/BV-22-C, GAP/SEC/SEM/BV-26-C,<br>GAP/SEC/SEM/BV-27-C, GAP/SEC/SEM/BV-37-C,<br>GAP/SEC/SEM/BV-38-C, GAP/SEC/SEM/BV-39-C,<br>GAP/SEC/SEM/BV-40-C, GAP/SEC/SEM/BV-41-C,<br>GAP/SEC/SEM/BV-42-C, GAP/SEC/SEM/BV-43-C,<br>GAP/SEC/SEM/BV-44-C.<br>TSE 16617 (rating 2): Replaced MSC in section<br>containing TCs GAP/SEC/SEM/BV-26-C, -41-C, and -<br>42-C.<br>TSE 16633 (rating 2): Added an option to terminate<br>the connection in the Pass verdicts for the sections<br>containing TCs GAP/SEC/SEM/BI-01-C – -08-C, -11-<br>C, -12-C, and -14-C – -19-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **387 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||Incorporated<br>Enhanced_Connection_Update_TEST_CR_r17:<br>Added a reference to the v5.3 Core release; added<br>Section 3.2.2.11 “Connection Subrating Procedure”;<br>added CSUB, CSR, and CSU to the Acronyms table;<br>added Section 4.6.10 and related subsections,<br>including new TCs GAP/CSUB/CSR/BV-01-C and<br>GAP/CSUB/CSU/BV-01-C; updated TCMT<br>accordingly. Subsequently converted to “Sydney” and<br>“.x” to real numbers.<br>Minor template-related editorials.|
|40|p40|2021-07-13|Approved by BTI on 2021-06-27. Prepared for<br>TCRL 2021-1publication.|
||p41r00–r06|2021-08-13 –<br>2021-12-21|TSE 14953 (rating 4): To address E13336 (related to<br>Core v5.3), added new TCs GAP/SEC/SEM/BI-25-C –<br>-33-C. Updated TCMT accordingly.<br>TSE 15919 (rating 4): To address E15384, added new<br>TCs GAP/SEC/SEM/BV-56-C – -67-C. Updated<br>TCMT accordingly.<br>TSE 16692 (rating 2): Added BR/EDR info to sections<br>“Mode-independent Authentication – Peripheral”,<br>“Security Modes – Peripheral”, and “Security Modes –<br>Central” and to TCs GAP/SEC/SEM/BV-11-C – -15-C,<br>-18-C – -20-C, -47-C – -49-C, -54-C, -55-C,<br>GAP/SEC/AUT/BV-02-C, and GAP/SEC/SEM/BI-01-<br>C; moved TCs GAP/SEC/SEM/BI-01-C and -05-C and<br>sections “Security Mode 4, Responder - Invalid<br>Encryption Key Size” and “Security Mode 4, Initiator -<br>Invalid Encryption Key Size” to improve the grouping;<br>added new subsection title/subgroup objectives for<br>“LE Security Modes – Peripheral” and “LE Security<br>Modes – Central”; updated test purpose for TCs<br>GAP/SEC/SEM/BV-26-C, -41-C, and -42-C; updated<br>test purpose, initial condition, test steps, MSC, and<br>Pass verdict for section containing TCs<br>GAP/SEC/SEM/BV-22-C, -39-C, and -40-C and for<br>section containing TCs GAP/SEC/SEM/BV-27-C,<br>-43-C, and -44-C; added LE Transport info for TCs<br>GAP/SEC/SEM/BV-23-C – -25-C, -28-C, -29-C,<br>-62-C, -63-C, -65-C, -66-C, and /BI-22-C – -23-C;<br>added descriptive information to TCID titles for TCs<br>GAP/SEC/SEM/BV-05-C – -07-C, -09-C, and -50-C, –<br>-53-C; updated TCMT to align with<br>regrouping/renaming.<br>TSE 17011 (rating 2): Replaced MSC Part A for TC<br>GAP/DM/LEP/BV-20-C.<br>TSE 17023 (rating 2): Removed test cases<br>GAP/DM/LEP/BV-02-C and -05-C; updated TCMT<br>accordingly.<br>TSE 17132 (rating 2): Modified the initial conditions<br>for GAP/CONN/CPUP/BV-04-C and -05-C. Updated<br>the TCMT for GAP/CONN/CPUP/BV-01-C – -05-C to<br>be less restrictive and moved the TCMT entry for<br>GAP/CONN/CPUP/BV-06-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **388 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 17224 (rating 2): Corrected the TCMT entry for<br>TC GAP/SEC/SEM/BV-46-C.<br>TSE 17496 (rating 2): Updated 8a and 20a<br>capitalization in TCMT entries affected.<br>TSE 17539 (rating 2): Updated TCID Conventions<br>section, replacing BSM with BSE and updating<br>subfunction identifier; updated section name from<br>“Broadcast Isochronous Synchronizability mode” to<br>“Broadcast Isochronous Synchronization<br>Establishment”; updated GAP/BIS/BSM/BV-01-C to<br>GAP/BIS/BSE/BV-01-C and updated test case name,<br>test purpose, reference, initial condition, MSC, and<br>TCMT entry; updated reference and TCMT entry for<br>GAP/BIS/BBM/BV-01-C.<br>TSE 17600 (rating 1): Corrected the reference for<br>GAP/PADV/PASM/BV-01-C.<br>Performed template-related formatting fixes, including<br>updating to the introduction text before the TCMT to<br>align with the template and the copyright page to align<br>with v2 of the DNMD.|
|41|p41|2022-01-25|Approved by BTI on 2021-12-27. Prepared for<br>TCRL 2021-2publication.|
||p42r00–r04|2022-02-01 –<br>2022-04-26|TSE 18155 (rating 2): Updated the TCMT entry for<br>GAP/SEC/SEM/BV-45-C.<br>TSE 18380 (rating 2): Added “Fields and Bits<br>Reserved for Future Use” section.<br>TSE 18454 (rating 2): Added SUM ICS values to<br>TCMT for GAP/SEC/SEM/BV-56-C – -67-C to<br>address the fact that execution is necessary only if<br>supporting Core v5.3 or later.<br>TSE 18488 (rating 2): Updated the MSC, test<br>procedure, and expected outcome for<br>GAP/SEC/SEM/BI-32-C.<br>TSE 18519 (rating 1): Updated the MSCs for<br>GAP/ADV/BV-01-C, -02-C, -04-C, -05-C,<br>-08-C – -14-C, -17-C, -18-C.|
|42|p42|2022-06-28|Approved by BTI on 2022-05-31. Prepared for<br>TCRL 2022-1publication.|
||p43r00–r17|2022-07-27 –<br>2022-12-22|TSE 17045 (rating 2): Added and/or updated an initial<br>condition or test step to include LE Secure Pairing for<br>GAP/BROB/BCST/BV-03-C and -05-C;<br>GAP/BROB/OBSV/BV-06-C; GAP/CONN/PRDA/BV-<br>01-C and -02-C; GAP/CONN/UCON/BV-06-C;<br>GAP/DISC/RPA/BV-01-C; GAP/PRIV/CONN/BV-10-C<br>and -11-C; and GAP/SEC/AUT/BV-11-C, -12-C, and -<br>24-C.<br>TSE 17699 (rating 2): Updated the initial condition,<br>test steps, and MSCs for the sections containing TCs<br>GAP/SEC/AUT/BV-25-C and -26-C and<br>GAP/SEC/AUT/BV-27-C and -28-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **389 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 18349 (rating 2): Combined coordinating Central<br>and Peripheral tests into table-based, both-roles<br>format for GAP/SEC/SEM/BV-62-C – -67-C (Central<br>tests) and GAP/SEC/SEM/BV-56-C – -61-C<br>(Peripheral tests). Updated test purpose, initial<br>condition, MSC, test procedure, and pass verdict as<br>necessary.<br>TSE 18444 (rating 4): Per E17946, concatenated TCs<br>GAP/ADV/BV-01-C – -05-C and -08-C – -14-C and -<br>17-C and -18-C into a table-based section. Added<br>new TC GAP/ADV/BV-19-C. Updated TCMT<br>accordingly.<br>TSE 18664 (rating 2): Clarified transports in Steps 10,<br>11, and 13 of GAP/DM/LEP/BV-20-C. Updated the<br>MSC in GAP/DM/LEP/BV-21-C to reflect the test<br>procedure, removed extraneous Step 11, and<br>corrected the typo in Step 13.<br>TSE 19113 (rating 2): Updated test purpose, initial<br>condition, test procedure, MSC, and pass verdict for<br>GAP/SEC/AUT/BV-19-C and -20-C to clarify the<br>recommended behavior from the spec.<br>TSE 20339 (rating 2): Updated TCMT entries for<br>GAP/SEC/AUT/BV-26-C and -28-C.<br>TSE 20378 (rating 2): Corrected MSCs for<br>GAP/SEC/SEM/BV-23-C and -28-C.<br>TSE 20469 (rating 1): Corrected references and initial<br>conditions for GAP/GAT/BV-04-C – -06-C. Removed<br>Test Condition for GAP/GAT/BV-04-C.<br>TSE 20501 (rating 2): Corrected the TCMT entry for<br>GAP/SEC/SEM/BV-46-C.<br>TSE 22131 (rating 1): Combined two references to the<br>CSS into one and updated cross-references<br>throughout the TS accordingly.<br>TSE 22133 (rating 1): Per E20606, removed<br>GAP/SEC/AUT/BV-02-C. Updated TCMT accordingly.<br>TSE 22228 (rating 4): Per E22185, added “PAC” to<br>the abbreviations list and added new TCs<br>GAP/PADV/PAC/BV-01-C and -02-C. Updated the<br>TCMT accordingly.<br>Core v5.4 CR incorporation:<br>EAD (from CR Encrypted_Advertising_Data<br>.Test.CR.13): Added new reference to Core v5.4.<br>Added new test group description for Scanning<br>Advertisement. Added new abbreviation for Scanner<br>(SCN). Added new TCs: GAP/ADV/BV-20-C,<br>GAP/SCN/BV-01-C, and GAP/GAT/BV-09-C – -11-C.<br>Updated TCMT accordingly.<br>Incorporated test issue 22239, which is associated<br>with the EAD CR for v5.4.<br>SLC (from CR Security_Level_Characteristics.<br>Test.CR_r07): Added a new section containing new<br>TCs GAP/GAT/BV-12-C and -13-C. Updated the<br>TCMT accordingly.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **390 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||PAwR (from CR<br>Periodic_Advertising_with_Responses_TEST_<br>CR_r22): Added new TCs: GAP/PADV/PASM/BV-02-<br>C; GAP/PADV/PAM/BV-02-C; GAP/PADV/PASE/BV-<br>07-C – -12-C; and GAP/PADV/PAST/BV-03-C and -<br>04-C; affected sections containing TCs:<br>GAP/PADV/PASM/BV-01-C; GAP/PADV/PAM/BV-01-<br>C; GAP/PADV/PASE/BV-01-C – -06-C; and<br>GAP/PADV/PAST/BV-01-C and -02-C; updated<br>TCMT accordingly.<br>Incorporated test issue 22233 to address spec issue<br>20452.<br>Resolved .X references per email key from Alicia on<br>2022-12-19.<br>Editorials to align the document with the latest TS<br>template conventions.|
|43|p43|2023-02-07|Approved by BTI on 2022-12-28. Prepared for<br>TCRL 2022-2publication.|
||p43ed2<br>r00–r01|2023-03-08 –<br>2023-4-13|TSE 22544 (rating 1): Updated TCID<br>GAP/BIS/BSM/BV-01-C to GAP/BIS/BSE/BV-01-C in<br>Figure 4.60.|
||p43 edition 2|2023-04-13|Approved by BTI on 2023-04-13. Prepared for<br>edition 2publication.|
||p44r00–r03|2023-04-16 –<br>2023-05-26|TSE 18332 (rating 2): Updated the Initial Condition<br>and test steps for the sections containing<br>GAP/SEC/SEM/BV-21-C, -37-C, and -38-C and<br>GAP/SEC/SEM/BV-26-C, -41-C, and -42-C; updated<br>the Initial Condition, test steps, MSC, and Pass<br>verdict for GAP/SEC/SEM/BV-23-C and -28-C; and<br>updated the MSC for the section containing<br>GAP/SEC/SEM/BV-22-C, -39-C, and -40-C.<br>TSE 20390 (rating 1): Deleted GAP/DM/LEP/BV-04-<br>C; updated the TCMT accordingly.<br>TSE 22294 (rating 2): Updated TCMT entries for<br>GAP/SEC/SEM/BV-56-C – -62-C and -64-C – -67-C.<br>TSE 22413 (rating 1): Corrected an attribute name in<br>the test steps and MSCs of GAP/GAT/BV-09-C –<br>-11-C.<br>TSE 22429 (rating 2): Updated the Initial Condition,<br>MSCs, test steps, and Pass verdict for the sections<br>containing GAP/SEC/SEM/BV-56-C and -62-C; -57-C<br>and -63-C; and -58-C and -64-C.<br>TSE 22501 (rating 4): Per E20385, added new TC<br>GAP/GAT/BV-14-C. Updated the TCMT accordingly.<br>TSE 22521 (rating 1): Replaced the MSC for<br>GAP/SEC/AUT/BV-20-C.<br>TSE 22563 (rating 3): Updated the TCMT entry for<br>GAP/BROB/BCST/BV-05-C.|
|44|p44|2023-06-29|Approved by BTI on 2023-06-05. Prepared for<br>TCRL 2023-1publication.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **391 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||p45r00–r03|2023-08-07 –<br>2023-10-30|TSE 22986 (rating 2): Updated the test procedure for<br>GAP/SEC/AUT/BV-11-C.<br>TSE 23041 (rating 2): Removed an initial condition<br>and updated the MSC, test procedure, test condition,<br>and Pass verdict for the section containing<br>GAP/SEC/SEM/BI-02-C – -04-C, -11-C, and -14-C – -<br>16-C.<br>TSE 23143 (rating 4): Per E20385, added new TC<br>GAP/GAT/BV-15-C. Updated the TCMT accordingly.|
|45|p45|2024-07-01|Approved by BTI on 2024-05-22. Prepared for<br>TCRL 2024-1publication.|
||p46r00–r14|2024-06-25 –<br>2024-08-07|TSE 20647 (rating 2): Updated MSCs and text for<br>GAP/SEC/SEM/BI-24-C and the sections containing<br>GAP/SEC/SEM/BV-05-C – -09-C and<br>GAP/SEC/SEM/BV-50-C – -53-C. Updated the TCMT<br>accordingly.<br>TSE 23081 (rating 2): Updated text for<br>GAP/SEC/SEM/BI-06-C – -08-C, GAP/SEC/SEM/BI-<br>12-C, and GAP/SEC/SEM/BI-17-C – -19-C. Updated<br>the TCMT accordingly.<br>TSE 24059 (rating 1): Per E24057, updated<br>procedure name to Direct Connection Establishment<br>Procedure and added new MSCs for<br>GAP/CONN/DCEP/BV-01-C, -05-C, and -06-C.<br>TSE 24466 (rating 2): Added GAP 11/5 to the TCMT<br>for GAP/BROB/BCST/BV-05-C.<br>TSE 24837 (rating 2): Added GAP 27b/10 to the<br>TCMT for GAP/BOND/BON/BV-01-C.<br>TSE 25249 (rating 4): Per E24891, updated the initial<br>condition, MSC, and test procedure for GAP/GAT/BV-<br>14-C and -15-C. Updated the initial condition for<br>GAP/GAT/BV-09-C – -11-C. Converted GAP/GAT/BV-<br>04-C – -06C to a table-driven format. Deleted<br>GAP/GAT/BV-13-C. Added new TCs GAP/GAT/BV-<br>16-C – -19-C. Updated the section title, test purpose,<br>initial condition, test case configuration, MSC, and test<br>procedure for GAP/GAT/BV-04-C, -12-C, and -16-C –<br>-19-C.<br>Incorporated CR CS_Test_CR_r16-jorg (which<br>includes Test Issues 23205, 23293, 23331, 23332,<br>23361, 23362, 23363, 23364, 23365, 23378, 23379,<br>23381, 23382, 23384, 23404, 23419, 23422, 23424,<br>23425, 23500, 23501, 23502, 23503, 23504, 23506,<br>23594, 23693, 23694, 23696, 23701, 23706, 23711,<br>23732, 23736, 23737, 23738, 23776, 23842, 23923,<br>23993, 24023, 24033, 24043, 24049, 24133, 24135,<br>24137, 24138, 24139, 24141, 24142, 24143, 24146,<br>24147, 24149, 24150, 24151, 24153, 24177, 24181,<br>24231, 24232, 24330, 24331, 24332, 24410, 24411,<br>24418, 24419, 24478, 24483, 24515, 24531, 24599,<br>24601, 24602, 24614, 24618, 24619, 24621, 24623,<br>24624, 24625, 24627, 24630, 24639, 24645, 24646,<br>24655, 24656, 24657, 24659, 24660, 24669, 24681,|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **392 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||24717, 24769, 24776, 24789, 24808, 24809, 24838,<br>24844, 24850, 24867, 24868, 24893, 24894, 24895,<br>25028, 25029, 25040, 25042, 25053, 25055, 25111,<br>25112, 25120, 25139, 25140, 25141, 25142, 25143,<br>25148, 25149, 25150, 25157, 25166, 25209, 25240,<br>25278, 25282, 25299, 25428, 25443, 25479, 25498,<br>25511, 25512, 25525, 25585, 25617, 25632). To<br>account for the Channel Sounding feature in Core<br>Specification v6.0, added new TCs<br>GAP/SEC/SEM/BV-68-C – -72-C and GAP/CS/BV-01-<br>C and -02-C. Updated the TCMT accordingly.<br>Updated the references list, test groups, and the TCID<br>conventions table.<br>Incorporated Test Issue 25788.|
|46|p46|2024-09-04|Approved by BTI on 2024-08-14. Prepared for<br>TCRL 2024-2publication.|
||p46ed2r00|2024-10-04 –<br>2024-10-08|TSE 26362 (rating 1): Fixed instances of “Mode-#” to<br>“mode #” where non-Channel Sounding terminology<br>was changed in error. Fixed instances of adjectival<br>“128 Bit” to “128-bit”. Made editorial corrections to<br>other capitalization to better align with the spec and/or<br>to be internallyconsistent.|
||p46 edition 2|2024-10-24|Approved by BTI on 2024-10-24. Prepared for<br>edition 2publication.|
||p47r00–r05|2024-10-28 –<br>2024-12-11|TSE 25059 (rating 2): Corrected the initial condition,<br>test procedure, and expected outcome sections<br>affecting test cases GAP/SEC/SEM/BV-56-C – -58-C<br>and -62-C – -64-C. Made additional editorial updates<br>for consistency.<br>TSE 25477 (rating 1): Removed GAP/GAT/BV-14-C.<br>Updated the TCMT accordingly.<br>TSE 26005 (rating 2): Updated the TCMT entries for<br>GAP/BROB/OBSV/BV-06-C, GAP/DISC/RPA/BV-01-<br>C, GAP/CONN/ACEP/BV-03-C,<br>GAP/CONN/ACEP/BV-04-C, GAP/CONN/GCEP/BV-<br>05-C, GAP/CONN/GCEP/BV-06-C,<br>GAP/CONN/SCEP/BV-03-C, GAP/CONN/DCEP/BV-<br>05-C, GAP/CONN/DCEP/BV-06-C to replace 37/3<br>with 37/3a, which was added as part of TSE 25249.<br>TSE 26117 (rating 2): Updated the MSC and a test<br>step for GAP/SEC/SEM/BI-31-C.<br>TSE 26322 (rating 2): Updated the reference, initial<br>condition, test case configuration table, test steps,<br>and Pass verdict for the section containing<br>GAP/GAT/BV-04-C, -12-C, and -16-C – -19-C.<br>Updated GAP/GAT/BV-17-C characteristic value.|
|47|p47|2025-02-18|Approved by BTI on 2024-12-26. Prepared for<br>TCRL 2025-1publication.|
||p48r00–r10|2025-01-29 –<br>2025-03-24|TSE 18571 (rating 2): To accommodate ES-18819<br>and ES-19323, updated the TCMT entries for<br>GAP/MOD/NSYN/BV-01-C and<br>GAP/MOD/SYN/BV-01-C.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **393 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 26034 (rating 2): Corrected TCMT entries in LE<br>Privacy section.<br>TSE 26461 (rating 1): Removed “Test Conditions”<br>sections from tests, modifying/adding test purpose,<br>initial conditions, test configuration parameters, and<br>test steps where necessary to realign. Made<br>necessary updates to the TCMT.<br>TSE 26582 (rating 3): Updated the MSCs for the<br>sections containing GAP/SEC/SEM/BV-21-C, -37-C,<br>-38-C; GAP/SEC/SEM/BV-22-C, -39-C, -40-C;<br>GAP/SEC/SEM/BV-27-C, -43-C, -44-C;<br>GAP/SEC/SEM/BV-56-C, -62-C (also updates to test<br>procedure); GAP/SEC/SEM/BV-57-C, -63-C (also<br>updates to test procedure); GAP/SEC/SEM/BV-59-C,<br>-65-C (also updates to test procedure); updated the<br>TCMT entries for GAP/SEC/SEM/BV-21-C, -22-C;<br>GAP/SEC/SEM/BV-61-C; GAP/SEC/SEM/BV-26-C,<br>-27-C; GAP/SEC/SEM/BV-67-C.<br>TSE 26734 (rating 4): Deleted<br>GAP/SEC/SEM/BV-68-C. Updated the test<br>descriptions, test procedure, and MSC for the section<br>containing GAP/SEC/SEM/BV-69-C – -72-C and<br>added new TCs GAP/SEC/SEM/BV-73-C – -76-C.<br>Updated the TCMT accordingly.<br>TSE 26813 (rating 1): Modernized the Test Strategy<br>and Test Groups wording and the structure of the IXIT<br>reference.|
|48|p48|2025-05-06|Approved by BTI on 2025-04-16. Prepared for<br>TCRL 2025-2publication.|
||p48ed2<br>r00–r01|2025-05-20 –<br>2025-06-02|TSE 26815 (rating 1): Updated references and Pass<br>verdicts to address an issue with Core v4.0 no longer<br>being relevant, affecting TCs GAP/BROB/BCST/BV-<br>01-C, and -03-C – -05-C; GAP/DISC/NONM/BV-01-C<br>and -02-C; GAP/DISC/LIMM/BV-01-C and -03-C, and<br>GAP/DISC/GENM/BV-01-C and -03-C.<br>TSE 27441 (rating 1): Removed CSA 3 and CSA 4<br>from the references section, redirecting all references<br>within test cases to Core GAP v 4.2. Removed<br>unused reference to Core GAP v4.0 from the<br>references list.|
||p48 edition 2|2025-06-25|Approved by BTI on 2025-06-22. Prepared for<br>edition 2publication.|
||p49r00–r02|2025-07-14 –<br>2025-08-06|TSE 27212 (rating 2): Updated the test procedures for<br>the sections containing GAP/SEC/SEM/BV-05-C and -<br>50-C, -06-C and -51-C, -07-C and -52-C, -09-C and -<br>53-C, and -10-C and -46-C (also updated MSC for the<br>last section). Updated the TCMT for those TCs and<br>for BI-24-C and BV-63-C – -67-C.<br>TSE 27259 (rating 2): Updated the TCMT to align with<br>ICS table and item modifications that support<br>subsetting.<br>TSE 27509 (rating 1): Corrected IXIT values<br>throughout the TS.|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **394 of 395** 

**Generic Access Profile (GAP)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 27704 (rating 4): To accommodate changes<br>made under E27645, added new TC GAP/ADV/BV-<br>21-C to the section containing GAP/ADV/BV-20-C,<br>updating the Test Purpose, Test Procedure, and<br>TCMT accordingly.|
|49|p49|2025-11-04|Approved by BTI on 2025-10-05. Prepared for TCRL<br>pkg101publication.|



## _**Acknowledgments**_ 

|**Name**|**Company**|
|---|---|
|Elisa Rincón|AT4 wireless|
|Angel Romero|AT4 wireless|
|Mike Tsai|Atheros|
|Christopher Badder|Bluetooth SIG, Inc.|
|Nathan Burns|Bluetooth SIG, Inc.|
|Matt Canavan|Bluetooth SIG, Inc.|
|Gene Chang|Bluetooth SIG, Inc.|
|Jeff Drake|Bluetooth SIG, Inc.|
|Alicia Courtney|Broadcom|
|ChaojingSun|Broadcom|
|Mayank Batra|CSR|
|Tim Howes|CSR|
|Magnus Sommansson|CSR|
|Erik Peterson|Microsoft Corporation|
|Anindya Bakshi|MindTree|
|James Dent|Nokia|
|Miika Laaksonen|Nokia|
|Jonathan Tanner|Nokia|
|David Engelien-Lopes|Nordic Semiconductor|
|Frank Karlsen|Nordic Semiconductor ASA|
|Chris Church|Qualcomm|
|Brian A. Redding|Qualcomm|
|Rasmus Abildgren|SamsungElectronics Co., Ltd|
|Masaya Masuda|Toshiba|



**==> picture [17 x 22] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **395 of 395** 

