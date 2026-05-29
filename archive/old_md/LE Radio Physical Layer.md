## **LE Radio Physical Layer (RFPHY)** 

## _**Bluetooth[®]**_ **Test Suite** 

- **Revision:** RFPHY.TS.p24ed2 

- **Revision Date:** 2025-11-17 

- **Prepared By:** BTI 

- **Published during TCRL:** TCRL.pkg101 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. (“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located at www.bluetooth.com.** 

**THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.** 

**TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.** 

**This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.** 

## **This document is subject to change without notice.** 

**Copyright © 2009–2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third-party brands and names are the property of their respective owners.** 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **2 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **Contents** 

|**1**|**Scope ..................................................................................................................................................... 7**|
|---|---|
|**2**|**References, definitions, and abbreviations ....................................................................................... 8**|
||2.1<br>References .................................................................................................................................... 8|
||2.2<br>Definitions ..................................................................................................................................... 8|
||2.3<br>Acronyms and abbreviations ........................................................................................................ 8|
|**3**|**Test Suite Structure (TSS) ................................................................................................................... 9**|
||3.1<br>Test Strategy ................................................................................................................................. 9|
||3.2<br>Test groups ................................................................................................................................... 9|
||3.2.1<br>Protocol groups ....................................................................................................................................... 9|
|**4**|**Test cases (TC) ................................................................................................................................... 10**|
||4.1<br>Introduction ................................................................................................................................. 10|
||4.1.1<br>Test case identification conventions ..................................................................................................... 10|
||4.1.2<br>Conformance ........................................................................................................................................ 10|
||4.2<br>Cabled test setup configurations ................................................................................................ 11|
||4.2.1<br>Test Equipment Setup for AoD Receiver testing ................................................................................... 11|
||4.2.2<br>Test Equipment Setup for AoA Receiver or AoD Transmitter testing .................................................... 11|
||4.2.3<br>Test Equipment Setup for Channel Sounding testing ........................................................................... 12|
||4.3<br>Common test case conditions and parameters .......................................................................... 12|
||4.3.1<br>Default Frequencies .............................................................................................................................. 12|
||4.3.2<br>Channel Sounding Default Frequencies ............................................................................................... 13|
||4.3.3<br>Common Parameters and Variables ..................................................................................................... 13|
||4.4<br>Pass/Fail verdict conventions ..................................................................................................... 16|
||4.5<br>Common Packet Contents .......................................................................................................... 16|
||4.5.1<br>Fields and Bits Reserved for Future Use .............................................................................................. 16|
||4.6<br>Transmitter tests (TRM) .............................................................................................................. 16|
||4.6.1<br>Output power ........................................................................................................................................ 16|
||RFPHY/TRM/BV-01-C [Output power, 1 Ms/s] ..................................................................................................... 17|
||RFPHY/TRM/BV-18-C [Output power, Class 1, 1 Ms/s] ....................................................................................... 17|
||RFPHY/TRM/BV-19-C [Output power, 2 Ms/s] ..................................................................................................... 17|
||RFPHY/TRM/BV-20-C [Output power, Class 1, 2 Ms/s] ....................................................................................... 17|
||RFPHY/TRM/BV-15-C [Output power, With Constant Tone Extension, 1 Ms/s] ................................................... 17|
||RFPHY/TRM/BV-21-C [Output power, With Constant Tone Extension, Class1, 1 Ms/s] ...................................... 17|
||RFPHY/TRM/BV-22-C [Output power, With Constant Tone Extension, 2 Ms/s] ................................................... 17|
||RFPHY/TRM/BV-23-C [Output power, With Constant Tone Extension, Class1, 2 Ms/s] ...................................... 17|
||4.6.2<br>In-band emissions ................................................................................................................................. 18|
||RFPHY/TRM/BV-03-C [In-band emissions, uncoded data at 1 Ms/s] ................................................................... 19|
||RFPHY/TRM/BV-08-C [In-band emissions at 2 Ms/s] ........................................................................................... 19|
||4.6.3<br>Modulation characteristics .................................................................................................................... 20|
||RFPHY/TRM/BV-05-C [Modulation Characteristics, uncoded data at 1 Ms/s] ...................................................... 20|
||RFPHY/TRM/BV-09-C [Stable Modulation Characteristics, uncoded data at 1 Ms/s] ........................................... 20|
||RFPHY/TRM/BV-10-C [Modulation Characteristics at 2 Ms/s] .............................................................................. 20|
||RFPHY/TRM/BV-11-C [Stable Modulation Characteristics at 2 Ms/s] ................................................................... 21|
||RFPHY/TRM/BV-13-C [Modulation Characteristics, LE Coded (S=8)].................................................................. 21|
||4.6.4<br>Carrier frequency offset and drift .......................................................................................................... 24|
||RFPHY/TRM/BV-06-C [Carrier frequency offset and drift, uncoded data at 1 Ms/s] ............................................. 24|
||RFPHY/TRM/BV-12-C [Carrier frequency offset and drift at 2 Ms/s] ..................................................................... 24|
||RFPHY/TRM/BV-14-C [Carrier frequency offset and drift, LE Coded (S=8)] ........................................................ 24|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **3 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|4.6.5<br>Carrier frequency offset and drift, Constant Tone Extension ................................................................ 27|
|---|
|RFPHY/TRM/BV-16-C [Carrier frequency offset and drift, uncoded data at 1 Ms/s, Constant Tone|
|Extension] ............................................................................................................................................................. 28|
|RFPHY/TRM/BV-17-C [Carrier frequency offset and drift at 2 Ms/s, Constant Tone Extension] .......................... 28|
|4.6.6<br>Tx Power Stability, AoD Transmitter ..................................................................................................... 31|
|RFPHY/TRM/PS/BV-01-C [Tx Power Stability, AoD Transmitter at 1 Ms/s with 2 µs Switching Slot] ................... 32|
|RFPHY/TRM/PS/BV-02-C [Tx Power Stability, AoD Transmitter at 1 Ms/s with 1 µs Switching Slot] ................... 32|
|RFPHY/TRM/PS/BV-03-C [Tx Power Stability, AoD Transmitter at 2 Ms/s with 2 µs Switching Slot] ................... 32|
|RFPHY/TRM/PS/BV-04-C [Tx Power Stability, AoD Transmitter at 2 Ms/s with 1 µs Switching Slot] ................... 32|
|4.6.7<br>Antenna switching integrity, AoD Transmitter ....................................................................................... 33|
|RFPHY/TRM/ASI/BV-05-C [Antenna switching integrity, AoD Transmitter at 1 Ms/s with 2 µs Switching|
|Slot] ....................................................................................................................................................................... 33|
|RFPHY/TRM/ASI/BV-06-C [Antenna switching integrity, AoD Transmitter at 1 Ms/s with 1 µs Switching|
|Slot] ....................................................................................................................................................................... 33|
|RFPHY/TRM/ASI/BV-07-C [Antenna switching integrity, AoD Transmitter at 2 Ms/s with 2 µs Switching|
|Slot] ....................................................................................................................................................................... 33|
|RFPHY/TRM/ASI/BV-08-C [Antenna switching integrity, AoD Transmitter at 2 Ms/s with 1 µs Switching|
|Slot] ....................................................................................................................................................................... 33|
|4.6.8<br>CS Stable Phase ................................................................................................................................... 35|
|RFPHY/TRM/CS/BV-01-C [Stable Phase, 1 Ms/s, CS_Tone]............................................................................... 36|
|RFPHY/TRM/CS/BV-02-C [Stable Phase, 2 Ms/s, CS_Tone]............................................................................... 36|
|4.6.9<br>CS Modulation Characteristics, 2 Ms/s, BT = 2.0 .................................................................................. 37|
|RFPHY/TRM/CS/BV-03-C [Modulation Characteristics, 2 Ms/s, BT = 2.0, Mode-1] ............................................. 37|
|RFPHY/TRM/CS/BV-04-C [Modulation Characteristics, 2 Ms/s, BT = 2.0, Mode-3] ............................................. 37|
|4.6.10<br>CS TX Output SNR Control .................................................................................................................. 40|
|RFPHY/TRM/CS/BV-05-C [TX SNR Output Control, 1 Ms/s, Mode-1] ................................................................. 40|
|RFPHY/TRM/CS/BV-06-C [TX SNR Output Control, 1 Ms/s, Mode-3] ................................................................. 40|
|RFPHY/TRM/CS/BV-07-C [TX SNR Output Control, 2 Ms/s, Mode-1] ................................................................. 40|
|RFPHY/TRM/CS/BV-08-C [TX SNR Output Control, 2 Ms/s, Mode-3] ................................................................. 40|
|RFPHY/TRM/CS/BV-09-C [TX SNR Output Control, 2 Ms/s, Mode-1, BT = 2.0] .................................................. 40|
|RFPHY/TRM/CS/BV-10-C [TX SNR Output Control, 2 Ms/s, Mode-3, BT = 2.0] .................................................. 40|
|4.7<br>Receiver tests (RCV) .................................................................................................................. 41|
|4.7.1<br>Receiver sensitivity ............................................................................................................................... 41|
|RFPHY/RCV/BV-01-C [Receiver sensitivity, uncoded data at 1 Ms/s] .................................................................. 42|
|RFPHY/RCV/BV-08-C [Receiver sensitivity at 2 Ms/s] ......................................................................................... 42|
|RFPHY/RCV/BV-14-C [Receiver Sensitivity, uncoded data at 1 Ms/s, Stable Modulation Index] ......................... 42|
|RFPHY/RCV/BV-20-C [Receiver sensitivity at 2 Ms/s, Stable Modulation Index] ................................................. 42|
|RFPHY/RCV/BV-26-C [Receiver sensitivity, LE Coded (S=2)] ............................................................................. 42|
|RFPHY/RCV/BV-27-C [Receiver sensitivity, LE Coded (S=8)] ............................................................................. 42|
|RFPHY/RCV/BV-32-C [Receiver sensitivity, LE Coded (S=2), Stable Modulation Index] ..................................... 42|
|RFPHY/RCV/BV-33-C [Receiver sensitivity, LE Coded (S=8), Stable Modulation Index] ..................................... 42|
|4.7.2<br>C/I and Receiver Selectivity Performance ............................................................................................. 44|
|RFPHY/RCV/BV-03-C [C/I and Receiver Selectivity Performance, uncoded data at 1 Ms/s] ............................... 44|
|RFPHY/RCV/BV-09-C [C/I and Receiver Selectivity Performance at 2 Ms/s] ....................................................... 44|
|RFPHY/RCV/BV-15-C [C/I and Receiver Selectivity Performance, uncoded data at 1 Ms/s, Stable|
|Modulation Index] .................................................................................................................................................. 44|
|RFPHY/RCV/BV-21-C [C/I and Receiver Selectivity Performance at 2 Ms/s, Stable Modulation Index] ............... 44|
|RFPHY/RCV/BV-28-C [C/I and Receiver Selectivity Performance, LE Coded (S=2)] ........................................... 44|
|RFPHY/RCV/BV-29-C [C/I and Receiver Selectivity Performance, LE Coded (S=8)] ........................................... 44|
|RFPHY/RCV/BV-34-C [C/I and Receiver Selectivity Performance, LE Coded (S=2), Stable Modulation|
|Index] .................................................................................................................................................................... 44|
|RFPHY/RCV/BV-35-C [C/I and Receiver Selectivity Performance, LE Coded (S=8), Stable Modulation|
|Index] .................................................................................................................................................................... 44|
|4.7.3<br>Blocking Performance ........................................................................................................................... 46|
|RFPHY/RCV/BV-04-C [Blocking Performance, uncoded data at 1 Ms/s] ............................................................. 47|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **4 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|RFPHY/RCV/BV-10-C [Blocking performance at 2 Ms/s] ..................................................................................... 47|
|---|
|RFPHY/RCV/BV-16-C [Blocking Performance, uncoded data at 1 Ms/s, Stable Modulation Index] ..................... 47|
|RFPHY/RCV/BV-22-C [Blocking performance at 2 Ms/s, Stable Modulation Index] ............................................. 47|
|4.7.4<br>Intermodulation Performance ................................................................................................................ 49|
|RFPHY/RCV/BV-05-C [Intermodulation Performance, uncoded data at 1 Ms/s] .................................................. 49|
|RFPHY/RCV/BV-11-C [Intermodulation performance at 2 Ms/s] .......................................................................... 49|
|RFPHY/RCV/BV-17-C [Intermodulation Performance, uncoded data at 1 Ms/s, Stable Modulation Index] .......... 49|
|RFPHY/RCV/BV-23-C [Intermodulation performance at 2 Ms/s, Stable Modulation Index] .................................. 49|
|4.7.5<br>Maximum input signal level ................................................................................................................... 51|
|RFPHY/RCV/BV-06-C [Maximum input signal level, uncoded data at 1 Ms/s]...................................................... 52|
|RFPHY/RCV/BV-12-C [Maximum input signal level at 2 Ms/s] ............................................................................. 52|
|RFPHY/RCV/BV-18-C [Maximum input signal level, uncoded data at 1 Ms/s, Stable Modulation Index] ............. 52|
|RFPHY/RCV/BV-24-C [Maximum input signal level at 2 Ms/s, Stable Modulation Index] ..................................... 52|
|4.7.6<br>PER report integrity ............................................................................................................................... 53|
|RFPHY/RCV/BV-07-C [PER Report Integrity, uncoded data at 1 Ms/s] ................................................................ 53|
|RFPHY/RCV/BV-13-C [PER Report Integrity at 2 Ms/s] ....................................................................................... 53|
|RFPHY/RCV/BV-19-C [PER Report Integrity, uncoded data at 1 Ms/s, Stable Modulation Index] ....................... 53|
|RFPHY/RCV/BV-25-C [PER Report Integrity at 2 Ms/s, Stable Modulation Index] ............................................... 53|
|RFPHY/RCV/BV-30-C [PER Report Integrity, LE Coded (S=2)] ........................................................................... 53|
|RFPHY/RCV/BV-31-C [PER Report Integrity, LE Coded (S=8)] ........................................................................... 53|
|RFPHY/RCV/BV-36-C [PER Report Integrity, LE Coded (S=2), Stable Modulation Index] ................................... 53|
|RFPHY/RCV/BV-37-C [PER Report Integrity, LE Coded (S=8), Stable Modulation Index] ................................... 53|
|4.7.7<br>IQ Samples Coherency, AoD Receiver ................................................................................................. 54|
|RFPHY/RCV/IQC/BV-01-C [IQ Samples Coherency, AoD Receiver at 1 Ms/s with 2 µs Slot] ............................. 54|
|RFPHY/RCV/IQC/BV-02-C [IQ Samples Coherency, AoD Receiver at 1 Ms/s with 1 µs Slot] ............................. 54|
|RFPHY/RCV/IQC/BV-03-C [IQ Samples Coherency, AoD Receiver at 2 Ms/s with 2 µs Slot] ............................. 54|
|RFPHY/RCV/IQC/BV-04-C [IQ Samples Coherency, AoD Receiver at 2 Ms/s with 1 µs Slot] ............................. 55|
|4.7.8<br>IQ Samples Coherency, AoA Receiver ................................................................................................. 55|
|RFPHY/RCV/IQC/BV-05-C [IQ Samples Coherency, AoA Receiver at 1 Ms/s with 2 µs Slot] .............................. 56|
|RFPHY/RCV/IQC/BV-06-C [IQ Samples Coherency, AoA Receiver at 2 Ms/s with 2 µs Slot] .............................. 56|
|4.7.9<br>IQ Samples Dynamic Range, AoD Receiver ......................................................................................... 57|
|RFPHY/RCV/IQDR/BV-07-C [IQ Samples Dynamic Range, AoD Receiver at 1 Ms/s with 2 µs Slot] ................... 57|
|RFPHY/RCV/IQDR/BV-08-C [IQ Samples Dynamic Range, AoD Receiver at 1 Ms/s with 1 µs Slot] ................... 57|
|RFPHY/RCV/IQDR/BV-09-C [IQ Samples Dynamic Range, AoD Receiver at 2 Ms/s with 2 µs Slot] ................... 57|
|RFPHY/RCV/IQDR/BV-10-C [IQ Samples Dynamic Range, AoD Receiver at 2 Ms/s with 1 µs Slot] ................... 57|
|4.7.10<br>IQ Samples Dynamic Range, AoA Receiver ......................................................................................... 59|
|RFPHY/RCV/IQDR/BV-11-C [IQ Samples Dynamic Range, AoA Receiver at 1 Ms/s with 2 µs Slot] ................... 59|
|RFPHY/RCV/IQDR/BV-12-C [IQ Samples Dynamic Range, AoA Receiver at 2 Ms/s with 2 µs Slot] ................... 59|
|4.8<br>Transmitter/Receiver tests (TRM-RCV) ...................................................................................... 60|
|4.8.1<br>CS Step Mode-0, Frequency Verification .............................................................................................. 60|
|RFPHY/TRM-RCV/CS/BV-01-C [Step Mode-0, Frequency Verification, 1 Ms/s] .................................................. 61|
|RFPHY/TRM-RCV/CS/BV-02-C [Step Mode-0, Frequency Verification, 2 Ms/s] .................................................. 61|
|RFPHY/TRM-RCV/CS/BV-03-C [Step Mode-0, Frequency Verification, 2 Ms/s, BT = 2.0] ................................... 61|
|4.8.2<br>CS Step Main Mode, Frequency Verification ........................................................................................ 62|
|RFPHY/TRM-RCV/CS/BV-04-C [Step Main Mode, Frequency Verification, 1 Ms/s, Mode-1]............................... 63|
|RFPHY/TRM-RCV/CS/BV-05-C [Step Main Mode, Frequency Verification, 1 Ms/s, Mode-2]............................... 63|
|RFPHY/TRM-RCV/CS/BV-06-C [Step Main Mode, Frequency Verification, 1 Ms/s, Mode-3]............................... 63|
|RFPHY/TRM-RCV/CS/BV-07-C [Step Main Mode, Frequency Verification, 2 Ms/s, Mode-1]............................... 63|
|RFPHY/TRM-RCV/CS/BV-08-C [Step Main Mode, Frequency Verification, 2 Ms/s, Mode-3]............................... 63|
|RFPHY/TRM-RCV/CS/BV-09-C [Step Main Mode, Frequency Verification, 2 Ms/s, BT = 2.0, Mode-1] ............... 63|
|RFPHY/TRM-RCV/CS/BV-10-C [Step Main Mode, Frequency Verification, 2 Ms/s, BT = 2.0, Mode-3] ............... 63|
|4.8.3<br>CS Phase Measurement Accuracy ....................................................................................................... 65|
|RFPHY/TRM-RCV/CS/BV-11-C [Phase Measurement Accuracy, 1 Ms/s, Mode-2, Reflector, N_AP:1] ............... 66|
|RFPHY/TRM-RCV/CS/BV-19-C [Phase Measurement Accuracy, 1 Ms/s, Mode-2, Reflector, 1:N_AP] ............... 66|
|RFPHY/TRM-RCV/CS/BV-20-C [Phase Measurement Accuracy, 1 Ms/s, Mode-2, Reflector, 2:2] ...................... 66|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **5 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

||RFPHY/TRM-RCV/CS/BV-12-C [Phase Measurement Accuracy, 1 Ms/s, Mode-3, Reflector, N_AP:1] ............... 66|
|---|---|
||RFPHY/TRM-RCV/CS/BV-21-C [Phase Measurement Accuracy, 1 Ms/s, Mode-3, Reflector, 1:N_AP] ............... 67|
||RFPHY/TRM-RCV/CS/BV-22-C [Phase Measurement Accuracy, 1 Ms/s, Mode-3, Reflector, 2:2] ...................... 67|
||RFPHY/TRM-RCV/CS/BV-13-C [Phase Measurement Accuracy, 2 Ms/s, Mode-3, Reflector, N_AP:1] ............... 67|
||RFPHY/TRM-RCV/CS/BV-23-C [Phase Measurement Accuracy, 2 Ms/s, Mode-3, Reflector, 1:N_AP] ............... 67|
||RFPHY/TRM-RCV/CS/BV-24-C [Phase Measurement Accuracy, 2 Ms/s, Mode-3, Reflector, 2:2] ...................... 67|
||RFPHY/TRM-RCV/CS/BV-14-C [Phase Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-3, Reflector,|
||N_AP:1] ................................................................................................................................................................ 67|
||RFPHY/TRM-RCV/CS/BV-25-C [Phase Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-3, Reflector,|
||1:N_AP] ................................................................................................................................................................ 67|
||RFPHY/TRM-RCV/CS/BV-26-C [Phase Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-3, Reflector,|
||2:2] ........................................................................................................................................................................ 67|
||RFPHY/TRM-RCV/CS/BV-15-C [Phase Measurement Accuracy, 1 Ms/s, Mode-2, Initiator, N_AP:1] ................. 67|
||RFPHY/TRM-RCV/CS/BV-27-C [Phase Measurement Accuracy, 1 Ms/s, Mode-2, Initiator, 1:N_AP] ................. 67|
||RFPHY/TRM-RCV/CS/BV-28-C [Phase Measurement Accuracy, 1 Ms/s, Mode-2, Initiator, 2:2] ......................... 67|
||RFPHY/TRM-RCV/CS/BV-16-C [Phase Measurement Accuracy, 1 Ms/s, Mode-3, Initiator, N_AP:1] ................. 67|
||RFPHY/TRM-RCV/CS/BV-29-C [Phase Measurement Accuracy, 1 Ms/s, Mode-3, Initiator, 1:N_AP] ................. 67|
||RFPHY/TRM-RCV/CS/BV-30-C [Phase Measurement Accuracy, 1 Ms/s, Mode-3, Initiator, 2:2] ......................... 67|
||RFPHY/TRM-RCV/CS/BV-17-C [Phase Measurement Accuracy, 2 Ms/s, Mode-3, Initiator, N_AP:1] ................. 67|
||RFPHY/TRM-RCV/CS/BV-31-C [Phase Measurement Accuracy, 2 Ms/s, Mode-3, Initiator, 1:N_AP] ................. 67|
||RFPHY/TRM-RCV/CS/BV-32-C [Phase Measurement Accuracy, 2 Ms/s, Mode-3, Initiator, 2:2] ......................... 68|
||RFPHY/TRM-RCV/CS/BV-18-C [Phase Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-3, Initiator,|
||N_AP:1] ................................................................................................................................................................ 68|
||RFPHY/TRM-RCV/CS/BV-33-C [Phase Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-3, Initiator,|
||1:N_AP] ................................................................................................................................................................ 68|
||RFPHY/TRM-RCV/CS/BV-34-C [Phase Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-3, Initiator,|
||2:2] ........................................................................................................................................................................ 68|
|**5**|**Test case mapping ............................................................................................................................. 70**|
|**6**|**Appendix ............................................................................................................................................. 76**|
||6.1<br>Reference Signal Definition ........................................................................................................ 76|
||6.2<br>Normal Operating Conditions (NOC) .......................................................................................... 76|
||6.2.1<br>Normal Temperature ............................................................................................................................. 76|
||6.2.2<br>Nominal Supply Voltage ........................................................................................................................ 77|
||6.3<br>Packet Error Rate / Bit Error Rate Measurements ..................................................................... 77|
||6.3.1<br>PER Test Definition ............................................................................................................................... 77|
||6.3.2<br>BER to PER Mapping ........................................................................................................................... 78|
||6.4<br>Definition of the Position of Bit p0 ............................................................................................... 83|
||6.5<br>Measurement Uncertainty ........................................................................................................... 83|
||6.6<br>Packet Lengths ........................................................................................................................... 84|
||6.7<br>Number of Valid IQ Sample Pairs ............................................................................................... 85|
||6.7.1<br>Maximum Number of Packets for IQ Coherency Measurements .......................................................... 85|
||6.8<br>Antenna Gain .............................................................................................................................. 86|
||6.9<br>Tester Filter Characteristics ........................................................................................................ 86|
|**7**|**Revision history and acknowledgments .......................................................................................... 87**|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **6 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **1 Sco e p** 

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the LE Radio Physical (RFPHY) layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers’ Bluetooth devices. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **7 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **2 References, definitions, and abbreviations** 

## **2.1 References** 

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [1] and [2]. Mathematical conventions used in this document comply with the definitions given in [1]. 

- [1] Test Strategy and Terminology Overview 

- [2] Bluetooth Specification, Version 4.0 or later, Vol. 6, Part A: Physical Layer Specification 

- [3] ICS Proforma for RFPHY 

- [4] Bluetooth Specification, Version 4.0 or later, Vol. 6, Part F: Direct Test Mode 

- [5] Bluetooth Core IXIT Proforma 

- [6] Bluetooth Core Specification Addendum 5, Volume 6, Part A: Physical Layer Specification 

- [7] Bluetooth Specification, Version 5.0 or later, Vol. 6, Part A: Physical Layer Specification 

- [8] Bluetooth Specification, Version 5.1 or later, Vol. 6, Part A: Physical Layer Specification 

- [9] Bluetooth Specification, Version 5.1 or later, Vol. 6, Part F: Direct Test Mode 

- [10] Bluetooth Specification, Version 5.0 or later, Vol. 6, Part B: Link Layer Specification 

- [11] Bluetooth Specification, Version 6.0 or later, Vol. 6, Part A: Physical Layer Specification 

- [12] Bluetooth Specification, Version 6.0 or later, Vol. 6, Part F: Direct Test Mode 

- [13] Bluetooth Specification, Version 6.0 or later, Vol. 6 Part H: Channel Sounding 

## **2.2 Definitions** 

In this Bluetooth document, the definitions from [1] and [2] apply. 

## **2.3 Acronyms and abbreviations** 

In this Bluetooth document, the definitions, acronyms, and abbreviations from [1] and [2] apply. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **8 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **3 Test Suite Structure (TSS)** 

## **3.1 Test Strategy** 

The two primary objectives of the Test Strategy are: 

- To ensure interoperability between devices in the marketplace 

- To verify that a basic level of system performance is provided by devices in the marketplace 

The objectives are met by performing a series of functional and parametric tests over the allowed range of parameter variation. 

With these objectives in mind, the creation of the Test Strategy also considers ways to reduce the test execution time required for product qualification. 

To avoid qualification test redundancy, telecommunication regulatory motivated tests are not included in the Bluetooth qualification requirements. 

## **3.2 Test groups** 

The test groups are organized in two levels. The first level defines the protocol groups representing the protocol services. The second level separates the protocol services in functional modules. All tests are Capability tests as defined in the standard ISO subgroups. 

## **3.2.1 Protocol groups** 

The protocol group identifies the following test purposes: 

- Transmitter 

- Receiver 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **9 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4 Test cases (TC)** 

## **4.1 Introduction** 

## **4.1.1 Test case identification conventions** 

Test cases are assigned unique identifiers per the conventions in [1]. The convention used here is: **<spec abbreviation>/<IUT role>/** <class>/ **<feat>** /<func>/<subfunc>/<cap>/ **<xx>-<nn>-<y>** . 

|**Identifier Abbreviation**|**Spec Identifier <spec abbreviation>**|
|---|---|
|RFPHY|Bluetooth Low Energy physical layer specification|
|**Identifier Abbreviation**|**Class Identifier <class>**|
|RCV|Receiver tests|
|TRM|Transmitter tests|
|TRM-RCV|Transmitter/Receiver tests|
|**Identifier Abbreviation**|**Feature Identifier <feat>**|
|CS|Channel Sounding|
|IQC|IQ samples Coherency|
|IQDR|IQ samples Dynamic Range|
|PS|Power Stability|



_Table 4.1: RFPHY TC feature naming conventions_ 

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

In any case, where a member finds an issue with the test plan generated by the Bluetooth SIG qualification tool, with the test case as described in the Test Suite, or with the test system utilized, the 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **10 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

member is required to notify the responsible party via an erratum request such that the issue may be addressed. 

## **4.2 Cabled test setup configurations** 

This section describes the cabled test setups for tests between an IUT and a test system when performing specific groups of tests in this Test Suite. 

## **4.2.1 Test Equipment Setup for AoD Receiver testing** 

This setup is used to test IQ samples coherency on an IUT that is an AoD Receiver. 

**==> picture [243 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
Upper<br>Coaxial Tester<br>Variable RF<br>Lower<br>Attenuator IUT<br>Tester<br>(Optional)<br>**----- End of picture text -----**<br>


_Figure 4.1: Test Equipment Setup for AoD Receiver_ 

## **4.2.2 Test Equipment Setup for AoA Receiver or AoD Transmitter testing** 

This setup is used to test IQ samples coherency on an IUT that is an AoD Transmitter or an AoA Receiver. 

**==> picture [362 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
Coaxial<br>Digital<br>IUT<br>Upper<br>ANT 0 Tester<br>RF  ANT 1<br>Lower  Combiner<br>Tester /Splitter RF  Bluetooth<br>(Optional) ANT 2 (C.1) Switch Tx / Rx<br>ANT 3 (C.1)<br>**----- End of picture text -----**<br>


_Figure 4.2: Test Equipment Setup for AoA Receiver or AoD Transmitter (C.1 – Mandatory to support if declared, otherwise Excluded)_ 

The IUT provides 2–4 antenna input/output ports, matching the maximum number of antennae supported (TSPX_number_of_antennae) declared in the IXIT [5]. The antenna ports are marked as 0, 1, 2, and 3 in Figure 4.2. If the IUT only supports external antenna switching, an IUT-controlled RF switch component is used. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **11 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4.2.3 Test Equipment Setup for Channel Sounding testing** 

This test setup is used to test Channel Sounding on an IUT. 

**==> picture [432 x 164] intentionally omitted <==**

_Figure 4.3: Test Equipment Setup for Channel Sounding_ 

The IUT provides 1–4 antenna input/output ports, matching the maximum number of antenna supported (TSPX_number_of_cs_antennae) declared in the IXIT [5]. The antenna ports are marked as 0, 1, 2, and 3, as shown in Figure 4.3. 

The optional inline attenuator shown in Figure 4.3 is for use in level adjustment purposes to balance the input signal levels present at the VSA’s input RF port. The VSA’s input RF port is exposed to both the transmission energy from the VSG and the IUT in 2-way Channel Sounding ranging procedures. 

## **4.3 Common test case conditions and parameters** 

Unless stated otherwise in individual test cases the following applies throughout this Test Suite: 

1. The IUT is connected to the Lower Tester via a 50Ω connector. If there is no antenna interface, a temporary 50Ω interface or a suitable coupling device may be used. 

2. The test case is to be performed at normal operating conditions. 

The Bluetooth low energy system uses center frequencies 2402 + n*2 MHz, where n = 0,1,2…39. The total number of communication frequencies is 40. 

A Bluetooth low energy system supporting Channel Sounding uses 72 RF channels for CS exchanges. These RF channels have center frequencies at 2402 + k*1 MHz, where k is an integer from 2 to 22 and 26 to 76. 

The Test Suite uses the direct test mode in all transmit and receive test cases [4]. In direct test mode, hopping is disabled and the IUT’s transmit and receive frequencies are set according to the frequencies for testing defined for each test. 

## **4.3.1 Default Frequencies** 

The default frequencies for testing are as follows: 

|**Modulation**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|
|1 Ms/s|2402 MHz (n=0)|2426 MHz (n=12) or 2440<br>MHz (n=19) at the choice of<br>the IUT|2480 MHz (n=39)|
|2 Ms/s|2404 MHz(n=1)|2440 MHz(n=19)|2478 MHz(n=38)|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **12 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4.3.2 Channel Sounding Default Frequencies** 

The default frequencies (𝑓𝑂) used for Channel Sounding (populated in the Override Channel[i] channel pattern list) testing are as follows: 

|**Modulation**|**IUT Low**|**IUT Mid**|**IUT High **|
|---|---|---|---|
|1 Ms/s|2404 MHz(k=2)|2440 MHz(k=38)|2478 MHz(k=76)|
|2 Ms/s|2404 MHz(k=2)|2440 MHz(k=38)|2478 MHz(k=76)|
|2 Ms/s, BT = 2.0|2412 MHz(k=10)|2440 MHz(k=38)|2470 MHz(k=68)|



The number of Mode-0 and Main-Mode CS steps per CS sub-event that use the static CS test frequencies is defined in Section 4.3.3.3. The channels specified for test are repeated for as many CS procedures that are required to satisfy the test case criteria. 

## **4.3.3 Common Parameters and Variables** 

## **4.3.3.1 Channel Sounding Access Addresses** 

CS packets containing a CS_SYNC portion (including CS test packets) use a role-dependent static Access Address (CS synchronization word): 

- Role = Initiator: ‘10100001111010100100110101101100’ (in transmission order) 

- Role = Reflector: ‘00011110011101101000011110000101’ (in transmission order) 

Note: CS roles are interchangeable dependent upon the test to be performed between the Tester and the IUT. 

## **4.3.3.2 Channel Sounding Test Command Parameters** 

This section defines the HCI_LE_CS_Test Command default parameters (see Vol. 4, Part E, Section 7.8.142, “LE CS Test Command”). This command is used to schedule a single CS procedure that consists of one CS subevent used for the CS RFPHY test. 

The default values detailed in Table 4.2 are used unless otherwise specified. 

|**Parameter**|**Value**|
|---|---|
|Main_Mode_Type|0x01(Mode-1)|
|Sub_Mode_Type|0xFF(Unused)|
|Main_Mode_Repetition|0x00(No repetition)|
|Mode_0_Steps|0x03(Maximum)|
|Role|0x00(Initiator)|
|RTT_Type|0x00(RTT AA Only)|
|CS_SYNC_PHY|0x01(LE 1M PHY)|
|CS_SYNC_Antenna_Selection|0x01(A1)|
|Subevent_Len|0x3D08FF|
|Subevent_Interval|0x0000(Single sub-event)|
|Max_Num_Sub_events|0x00(Ignore)|
|Transmit_Power_Level|0x7F(Maximum)|
|T_IP1_Time|Shortest supported bythe IUT|
|T_IP2_Time|Shortest supported bythe IUT|
|T_FCS_Time|Shortest supported bythe IUT|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **13 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Parameter**|**Value**|
|---|---|
|T_PM_Time|0x28(40 us)|
|T_SW_Time|0x00(0 us)|
|Tone_Antenna_Config|0x00(1:1)|
|Reserved|0x00|
|DRBG_Nonce|0x0000|
|Channel_Map_Repetition|0x01(Single repetition)|
|Override_Config|0x0129 (Bits 0, 3, 5, and 8 enabled:<br>0: Channel_Length and Channel[i]<br>3: T_PM_Tone_Ext<br>5: Access Address<br>8: Payloadpattern)|
|Override_Parameters_Length|0x0E|
|Override_Parameters_Data|0x03 (Channel_Length)<br>0x02, 0x02, 0x02 (Channel[i])<br>0x00 (T_PM_Tone_Ext: No tone extensions)<br>0x36B25785 (CS_SYNC_AA_Initiator)<br>0xA1E16E78 (CS_SYNC_AA_Reflector)<br>0x00(Payload Pattern, PRBS9)|



_Table 4.2: LE CS Test Command Default Parameters_ 

For tests requiring a pseudo random full-band frequency sweep, the Override parameters are set as specified in Table 4.3. 

|**Parameter**|**Value**|
|---|---|
|Override_Config|0x0129(Bits 0, 3, 5, and 8 enabled)|
|Override_Parameters_Length|0x53|
|Override_Parameters_Data|0x48 (Channel_Length)<br>{SeeTable 4.5} (Channel[i])<br>0x00 (T_PM_Tone_Ext)<br>0x36B25785 (CS_Sync_AA_Initiator)<br>0xA1E16E78 (CS_Sync_AA_Reflector)<br>0x00(Payload Pattern, PRBS9)|



_Table 4.3: LE CS Test Command Override Parameters for the full-band frequency sweep_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **14 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

For the Step Mode-0, Frequency Verification measurements, the Override parameters are set as specified in Table 4.4. 

|**Parameter**|**Value**|
|---|---|
|Override_Config|0x0129(Bits 0, 3, 5, and 8 enabled)|
|Override_Parameters_Length|0x0E|
|Override_Parameters_Data|0x03 (Channel_Length)<br>{SeeTable 4.5} (Channel[i])<br>0x00 (T_PM_Tone_Ext)<br>0x36B25785 (CS_Sync_AA_Initiator)<br>0xA1E16E78 (CS_Sync_AA_Reflector)<br>0x00(Payload Pattern, PRBS9)|



_Table 4.4: LE CS Test Command Override Parameter for Step Mode-0, Frequency Verification test cases_ 

List of channels used in the test pattern are populated via the Channel[i] parameter. 

- For the full-band frequency sweep (see Table 4.3) (used in phase measurement accuracy tests) the entire 72 CS channel list as defined in Table 4.5 is utilized. 

- For Step Mode-0, Frequency Verification (see Table 4.4), three channels (3 Mode-0, and 1 MainMode) are used. These channels are defined as channel[i mod 72] to channel[(i+2) mod 72] in channel list. In the first subevent tested [i] = 0. For each subsequent subevent, the channels used are shifted by [i+1], i.e., the channels used in the second subevent are channel[i+1] to channel[i+3] and so on. The Channel[i] list in Table 4.5 is cycled through for as many times as required to perform the test case. The selected three channels may end at any position in the Channel[i] list. 

|**Parameter**|**Value**|
|---|---|
|Channel[i]|{ 0x15, 0x0c, 0x0a, 0x1d, 0x05, 0x11, 0x4a, 0x4c, 0x14, 0x41,<br>0x0b, 0x02, 0x24, 0x3e, 0x13, 0x2c, 0x32, 0x43, 0x1e, 0x2a,<br>0x2b, 0x06, 0x0e, 0x25, 0x22, 0x1c, 0x03, 0x3d, 0x29, 0x34,<br>0x45, 0x1a, 0x2d, 0x26, 0x09, 0x36, 0x48, 0x21, 0x04, 0x44,<br>0x31, 0x3a, 0x28, 0x0d, 0x4b, 0x27, 0x39, 0x16, 0x33, 0x49,<br>0x3f, 0x46, 0x1f, 0x47, 0x3c, 0x37, 0x42, 0x2f, 0x07, 0x1b,<br>0x23, 0x10, 0x30, 0x35, 0x12, 0x2e, 0x20, 0x40, 0x08, 0x38,<br>0x0f, 0x3b}|



_Table 4.5: LE CS Test Command Channel[i] Override Parameter values_ 

## **4.3.3.3 Channel Sounding Signal Transmission** 

This section defines the generic Initiator-Reflector signal exchange used for Channel Sounding RFPHY tests. Tests are performed on a CS sub-event basis. A single CS sub-event is scheduled within each CS procedure utilized, see [12]. 

Each CS sub-event contains the following CS steps (signal exchanges): 

- 𝑀 Mode-0 CS steps, in the range 1 ≤𝑀≤3 followed by, 

- 𝐾 Main-Mode CS steps, in the range 1 ≤𝐾≤72, 

Figure 4.4 outlines the CS step exchanges within a single CS sub-event. T_IPx refers to a CS step mode dependent Initiator-Reflector interlude period: 

- T_IP1; Mode-0, and Mode-1 CS signal exchange interlude period. 

- T_IP2; Mode-2, and Mode-3 CS signal exchange interlude period. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **15 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [396 x 254] intentionally omitted <==**

_Figure 4.4: Channel Sounding RFPHY test signal transmission overview_ 

## **4.4 Pass/Fail verdict conventions** 

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met. 

The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict. 

## **4.5 Common Packet Contents** 

## **4.5.1 Fields and Bits Reserved for Future Use** 

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers. 

## **4.6 Transmitter tests (TRM)** 

## **4.6.1 Output power** 

- Test Purpose 

Verify the maximum peak and average power emitted from the IUT. 

- Reference 

   - [2] Chapter 3 

   - [6] Chapter 3 

- Initial Condition 

   - The IUT is set to direct TX mode at maximum output power. Whitening is turned off. 

   - Frequency hopping off, fixed frequency. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **16 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

   - The values of MAX_TX_LENGTH and MAX_TX_LENGTH_2M (for which the TC is performed) are specified in Section 6.6. 

   - TSPX_Antenna_Gain is declared by the manufacturer of the IUT in the IXIT [5]. 

   - The IUT is set for a symbol rate as specified in Table 4.6. 

   - If the IUT supports CTE as specified in Table 4.6, the IUT is set to transmit AoA Constant Tone Extensions. 

- Test Case Configuration 

|**Test Case**|**PAVG Requirements**|**Symbol Rate**|**Payload Length**|
|---|---|---|---|
|RFPHY/TRM/BV-01-C<br>[Outputpower, 1 Ms/s]|-20 dBm ≤ PAVG≤ +10 dBm|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-18-C<br>[Output power, Class 1,<br>1 Ms/s]|+10 dBm < PAVG≤ +20 dBm|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-19-C<br>[Outputpower, 2 Ms/s]|-20 dBm≤PAVG ≤+10 dBm|2 Ms/s|MAX_TX_LENGTH_2M|
|RFPHY/TRM/BV-20-C<br>[Output power, Class 1,<br>2 Ms/s]|+10 dBm < PAVG ≤+20 dBm|2 Ms/s|MAX_TX_LENGTH_2M|
|RFPHY/TRM/BV-15-C<br>[Output power, With<br>Constant Tone<br>Extension, 1 Ms/s]|-20 dBm≤PAVG ≤+10 dBm|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-21-C<br>[Output power, With<br>Constant Tone<br>Extension, Class1,<br>1 Ms/s]|+10 dBm < PAVG ≤+20 dBm|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-22-C<br>[Output power, With<br>Constant Tone<br>Extension, 2 Ms/s]|-20 dBm≤PAVG ≤+10 dBm|2 Ms/s|MAX_TX_LENGTH_2M|
|RFPHY/TRM/BV-23-C<br>[Output power, With<br>Constant Tone<br>Extension, Class1,<br>2 Ms/s]|+10 dBm < PAVG ≤+20 dBm|2 Ms/s|MAX_TX_LENGTH_2M|



_Table 4.6: Output power test cases_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **17 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Test Procedure 

   1. The IUT transmits LE test packets with PRBS9 payload (Payload Length specified in Table 4.6). See [4] Section 4, “LE Test Packet Definition” for details. If the IUT supports CTE as specified in Table 4.6, then the Constant Tone Extension is TSPX_CTE_len_max * 8 μs. 

   2. The following settings are used for the Lower Tester: 

Center frequency at the lowest frequency for testing defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case) Frequency span Zero span Resolution BW 3 MHz Video BW 3 MHz Detector Peak Mode Clear/Write Sweep time Must cover at least one complete test packet Trigger RF (trigger on rising edge) 

   3. Upon packet transmission, the Lower Tester is triggered to make a sweep over the duration of one packet. The sweep starts at the beginning of the first bit in the preamble. 

   4. The peak power value, PPK, of the sweep is recorded. 

   5. The Lower Tester calculates average power PAVG over at least 20%–80% of the burst duration (position of p0 defines the beginning of the burst; see Section 6.4 Definition of the Position of Bit p0). 

   6. Steps 2–5 are repeated for the remaining frequencies for testing defined in the test condition section. 

   7. The antenna gain G (in dBi) is added to the PAVG results (in dBm) to calculate the average equivalent isotropic radiated power PAVG EIRP. 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- Expected Outcome 

## Pass verdict 

All measured values fulfill the following conditions: 

PPK ≤ (PAVG + 3 dB) 

PAVG EIRP = PAVG + G ≤ 100 mW (20 dBm) EIRP 

PAVG meets the requirements in Table 4.6. 

## **4.6.2 In-band emissions** 

- Test Purpose 

Verify that the in-band spectral emissions are within limits at normal operating conditions from the IUT. 

- Reference 

[2] Chapter 3.2 

- [7] Chapter 3.2.2 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **18 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Initial Condition 

   - The IUT is set to direct TX mode at maximum output power. Whitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The value of MAX_TX_LENGTH and MAX_TX_LENGTH_2M (for which the TC is performed) is specified in Section 6.6. 

- Test Case Configuration 

|**Test Case**|**In-band Emission**<br>**Requirements**|**Frequencies To**<br>**Skip**|**Symbol**<br>**Rate**|**Payload Length**|
|---|---|---|---|---|
|RFPHY/TRM/BV-03-C<br>[In-band emissions,<br>uncoded data at 1<br>Ms/s]|PTX≤ -20 dBm<br>for (fTX 2 MHz)<br>PTX≤ -30 dBm<br>for (fTX [3 + n] MHz])*|fTX<br>fTX - 1MHz,fTX+ 1MHz|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-08-C<br>[In-band emissions at<br>2 Ms/s]|PTX ≤-20 dBm<br>for (fTX 4 MHz)<br>PTX ≤-20 dBm<br>for (fTX 5 MHz)<br>PTX ≤-30 dBm<br>for (fTX [6 + n] MHz])*|fTX<br>fTX - 1MHz,fTX+ 1MHz<br>fTX - 2MHz, fTX + 2MHz<br>fTX - 3MHz, fTX + 3MHz|2 Ms/s|MAX_TX_LENGTH_2M|



- where n=0,1,2… 

_Table 4.7: In-band emissions test cases_ 

- Test Procedure 

   1. The IUT is set to receive at the lowest frequency for testing defined in frequencies for testing defined in the test condition section. 

   2. The IUT transmits LE test packets with PRBS9 payload (Payload Length specified in Table 4.7). See [4], Section 4, “LE Test Packet Definition” for details. 

   3. Set N:=0 

   4. The following settings are used for the Lower Tester: 

Center frequency 2401 MHz + N MHz Frequency span 1 MHz Resolution BW 100 kHz Video BW 300 kHz Detector Average Mode Maximum hold Sweep time 100 ms Number of sweeps 10 

5. Measure the power levels, PTX_N,i at the following 10 frequencies: (2401 MHz + N MHz) – 450 kHz + i100 kHz, where i=0…9 

6. Calculate and record PTX = (PTX_N,i) 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **19 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

   7. Increase center frequency by 1 MHz; N:=N+1 AND skip to next frequency if the increased frequency is equal to Frequency To Skip specified in Table 4.7. 

   8. Repeat Steps 4–7 until the center frequency is 2481 MHz 

   9. Set the IUT transmit frequency (fTX) to: 

   10. The mid operating frequency defined in the frequencies for testing defined in the test condition section and 

   11. The high operating frequency defined in the frequencies for testing defined in the test condition section 

   12. Repeat Steps 3–8 for both frequencies. 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- Expected Outcome 

## Pass verdict 

All measured values fulfill the In-band Emission Requirements specified in Table 4.7. 

For each operating frequency, up to three bands of 1 MHz width (as defined in the measurement) can be exempted from the requirements. The excepted values, however, comply with an absolute value of PTX ≤ -20 dBm. 

## **4.6.3 Modulation characteristics** 

- Test Purpose 

Verify that the modulation characteristics of the transmitted signal are correct. 

- Reference 

   - [2] Chapter 3.1 

   - [6] Chapter 3.1, Chapter 3.1.1 

- Initial Condition 

   - The IUT is set to direct TX mode at maximum output power. Whitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The value of MAX_TX_LENGTH, MAX_TX_LENGTH_2M, and MAX_TX_LENGTH_CODED_S8 (for which the TC is performed) is specified in Section 6.6. 

- Test Case Configuration 

|**Test Case**|**f1avg Requirements**|**Symbol Rate**|**Payload Length**|
|---|---|---|---|
|||||
|RFPHY/TRM/BV-05-C<br>[Modulation<br>Characteristics, uncoded<br>data at 1 Ms/s]|225 kHz ≤f1avg≤<br>275 kHz|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-09-C<br>[Stable Modulation<br>Characteristics, uncoded<br>data at 1 Ms/s]|247.5 kHz≤∆f1avg ≤<br>252.5 kHz|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-10-C<br>[Modulation<br>Characteristics at 2 Ms/s]|450 kHz≤∆f1avg ≤<br>550 kHz|2 Ms/s|MAX_TX_LENGTH_2M|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **20 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Test Case**|**f1avg Requirements**|**Symbol Rate**|**Payload Length**|
|---|---|---|---|
|||||
|RFPHY/TRM/BV-11-C<br>[Stable Modulation<br>Characteristics at 2 Ms/s]|495 kHz≤∆f1avg<br>≤505 kHz|2 Ms/s|MAX_TX_LENGTH_2M|
|RFPHY/TRM/BV-13-C<br>[Modulation<br>Characteristics, LE<br>Coded (S=8)]|225 kHz ≤f1avg<br>≤ 275 kHz<br>99.9% of all ∆f1max<br>frequency values<br>recorded over 10 LE<br>test packets are<br>>  185 kHz|1 Ms/s coded<br>S=8|MAX_TX_LENGTH_CODED_S8|



_Table 4.8: Modulation characteristics test cases_ 

- Test Procedure 

   1. The IUT is set to transmit at the lowest frequency for testing defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case). 

   2. The IUT transmits LE test packets with Payload Length (specified in Table 4.8) octet packet payload. See [4], Section 4, “LE Test Packet Definition”, for details. 

For Uncoded 1 Ms/s and 2 Ms/s, the payload consists of a repetitive sequence of 0Fhex octets (11110000bin in transmission order). 

For LE Coded (S=8), the payload consists of a repetitive sequence of 0xFF octets (binary ‘11111111’ in transmission order). This sequence, once passed through the S=8 encoder, becomes a repetitive sequence of ‘00111100’ symbols. The symbol duration is 1 µs. 

3. The following settings are used for the Lower Tester: 

Center frequency lowest frequency for testing as defined in the test condition section Mode FM demodulation Demodulator filter BW Specified in Section 6.9 (minimum) Filter passband ripple Specified in Section 6.9 Trigger RF (trigger on rising edge) 

The following measurement channel filter minimum attenuator characteristics are used: 

|**Frequency (for 1 Ms/s)**|**Frequency (for 2 Ms/s)**|**Attenuation**|
|---|---|---|
|650 kHz|±1.3 MHz|-3 dB|
|1 MHz|±2.0 MHz|-14 dB|
|2 MHz|±4.0 MHz|-44 dB|



4. The payload is FM demodulated with the settings described in Step 3. 

For Uncoded 1 Ms/s and 2 Ms/s, the measurement starts at the beginning of the fifth bit of the payload (see Figure 4.5 for description). The last four bits in the payload are disregarded (i.e., last bit in the measurement is the fourth bit in the final payload octet). 

For LE Coded (S=8), the measurement starts at the beginning of the 31[st] symbol in the payload. The last 34 symbols in the payload are disregarded. 

5. Each individual bit is to be oversampled at least 32 times. The sequence center frequency; f1ccf is calculated as the average frequency of all samples over each 00001111bin sequence. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **21 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

6. For the second, third, sixth and seventh bits in each 00001111bin sequence, the absolute value of the frequency offset from f1ccf is recorded as ∆f1max. ∆f1max is defined as the average deviation for each individual bit. See Figure 4.5 for reference. 

7. The average frequency value of all ∆f1max frequencies in a packet is calculated and recorded as ∆f1avg. 

8. For LE Coded (S=8), skip Steps 9–13; S=8 only supports ‘0011’ and ‘1100’ see Section 3.3.2, “Pattern mapper” in [10] for details. 

9. The IUT transmits LE test packets with Payload Length (specified in Table 4.8) octet payload consisting of a repetitive sequence of 55hex octets (10101010bin in transmission order). See [4], Section 4, “LE Test Packet Definition” for details. 

10. The payload is FM demodulated with the settings described in Step 3. The measurement starts at the beginning of the fifth bit in the payload field. The last four bits in the payload are disregarded (i.e., last bit in the measurement is the fourth bit in the final payload octet). 

11. Each individual bit is to be oversampled at least 32 times. The sequence center frequency; f2ccf is calculated as the average frequency of all samples over each 10101010bin sequence. 

12. The maximum deviation from the sequence center frequency, f2ccf is recorded as ∆f2max for each individual bit. See Figure 4.6 for reference. 

13. The average frequency value of all ∆f2max frequencies in a packet is calculated and recorded as ∆f2avg. 

14. Steps 2–13 are repeated for ≥ 10 packets. 

15. Steps 2–14 are repeated when the IUT is transmitting at the remaining frequencies defined in the test condition section. 

**==> picture [414 x 309] intentionally omitted <==**

**----- Start of picture text -----**<br>
average over samples<br>Note    f1  is defined as<br> max<br>the average of the samples<br>within the bit period 1 1 1 1<br>f<br>  f 1<br> avg<br> f1  f1<br> max    max<br>1 1 1 1 0 0 0 0 1 1 1 1 f1<br> ccf<br> f1  f1<br> max 2  max 3<br>t   f1<br> avg<br>11110000 sequence 1 sequence 2<br>Start of  Start of  Start of<br>payload field measurement  1 measurement  2<br>**----- End of picture text -----**<br>


_Figure 4.5: Frequency deviation measurement principle for 11110000-payload sequence_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **22 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [411 x 312] intentionally omitted <==**

**----- Start of picture text -----**<br>
maximum sample<br>f<br> f2  f2  f2  f2<br> max 1  max 3  max 5  max<br>  f2<br> avg<br>1 0 1 0 1 0 1 0 1 0 1 0 f2<br> ccf<br>  f2<br> avg<br> f2 max 2  f2 max 4  f2 max    f2 max 8 t<br>10101010 sequence 1 sequence 2<br>Start of  Start of  Start of<br>payload field measurement  1 measurement  2<br>**----- End of picture text -----**<br>


_Figure 4.6: Frequency deviation measurement principle for 10101010-payload sequence_ 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- 

## Expected Outcome 

## Pass verdict 

All measured values fulfill the f1avg Requirements specified in Table 4.8 at the low, mid, and high frequencies: 

Where ∆f2max is recorded (all cases except LE Coded, S=8), at least 99.9% of all ∆f2max frequency values recorded over 10 LE test packets are > 185 kHz (for 1 Ms/s) or 370 kHz (for 2 Ms/s). 

**==> picture [329 x 33] intentionally omitted <==**

- Notes 

To compensate for the statistical distribution of individual samples, the decision criteria is applied to 99.9% of the sample values. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **23 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4.6.4 Carrier frequency offset and drift** 

- Test Purpose 

Verify that the carrier frequency offset and carrier drift of the transmitted signal are correct. 

- Reference 

[2] Chapter 3.3 

   - [6] Chapter 3.3 

- Initial Condition 

   - The IUT is set to direct TX mode at maximum output power. Whitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The value of MAX_TX_LENGTH, MAX_TX_LENGTH_2M, and MAX_TX_LENGTH_CODED_S8 (for which the TC is performed) is specified in Section 6.6. 

- Test Case Configuration 

|**Test Case**|**Drift Requirement Limits**|**Symbol**|**Payload Length**|
|---|---|---|---|
|||**Rate**||
|RFPHY/TRM/BV-06-C<br>[Carrier frequency<br>offset and drift,<br>uncoded data at 1<br>Ms/s]||f1-f0| ≤ 23 kHz<br>|fn– fn-5|n= ,  , 8…k≤ 20 kHz|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-12-C<br>[Carrier frequency<br>offset and drift at 2<br>Ms/s]||f1-f0| ≤ 13.3 kHz<br>|fn– fn-5|n= ,  , 8…k≤ 20 kHz|2 Ms/s|MAX_TX_LENGTH_2M|
|RFPHY/TRM/BV-14-C<br>[Carrier frequency<br>offset and drift, LE<br>Coded(S=8)]||f0-f3| ≤ 19.2 kHz<br>|fn– fn-3|n= , 8, 9…k≤ 19.2 kHz|1 Ms/s<br>coded S=8|MAX_TX_LENGTH_CODED_S8|



_Table 4.9: Carrier frequency offset and drift test cases_ 

- Test Procedure 

   1. The IUT is set to transmit at the lowest frequency for testing defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case. 

   2. The IUT transmits LE test packets with Payload Length (specified in Table 4.8) octet payload. See [4], Section 4, “LE Test Packet Definition”, for details. 

For Uncoded 1 Ms/s and 2 Ms/s, the payload consists of a repetitive sequence of 55hex octets (10101010bin in transmission order) in the payload. 

For LE Coded (S=8), the payload consists of a repetitive sequence of 0xFF octets (binary ‘11111111’ in transmission order). This sequence, once passed through the S=8 encoder, becomes a repetitive sequence of ‘00111100’ symbols. The symbol duration is 1 µs. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **24 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## 3. The following settings are used for the Lower Tester: 

Center frequency lowest frequency for testing defined in the test condition section Mode FM demodulation Demodulator filter BW Specified in Section 6.9 (minimum) Filter passband ripple Specified in Section 6.9 Trigger RF (trigger on rising edge) 

The following measurement channel filter minimum attenuator characteristics are used: 

|**Frequency (for 1 Ms/s)**|**Frequency (for 2 Ms/s)**|**Attenuation**|
|---|---|---|
|650 kHz|±1.3 MHz|-3 dB|
|1 MHz|±2.0 MHz|-14 dB|
|2 MHz|±4.0 MHz|-44 dB|



The packet is FM demodulated with the settings described in Step 3. The measurement is to be performed at the start of the preamble field in the transmitted packet. 

For Uncoded 1 Ms/s, the Lower Tester integrates the frequency of the FM demodulated signal from the center of the first preamble bit to the center of the first bit following the 8th preamble bit, 8 bits in total. See Figure 4.7 for reference. 

For 2 Ms/s, the Lower Tester integrates the frequency of the FM demodulated signal from the center of the first preamble bit to the center of the first bit following the 16th preamble bit, 16 bits in total. 

For LE Coded (S=8), the Lower Tester integrates the frequency of the FM demodulated signal in groups of 16 symbols. The first symbol in the integration group corresponds to the third symbol of the preamble (first 1 of the ‘11110000’… sequence). The last 14 symbols of the preamble are disregarded. 

4. The integral sum in Step 4 is considered to be the initial carrier frequency of the IUT, and is recorded as f0 for Uncoded 1 Ms/s and 2 Ms/s and f0, f1, f2, and f3 for LE Coded (2 Ms/s). 

5. Throughout the payload of the packet: 

For Uncoded 1 Ms/s, the Lower Tester integrates the frequency of the FM demodulated signal in 10-bit intervals, starting at the second bit in the payload. 

For 2 Ms/s, the Lower Tester integrates the frequency of the FM demodulated signal in 20-bit intervals, starting at the second bit in the payload. 

For LE Coded (S=8), the Lower Tester integrates the frequency of the FM demodulated signals in 16-symbol intervals, starting at the 27th symbol in the PDU payload and until the (8*MAX_TX_LENGTH_CODED_S8)th symbol. The last 16-symbol sequence should not overlap the CRC field at the end of the packet. 

The measurement is repeated until the end of the payload duration. The last bit interval (10-bit for Uncoded 1 Ms/s, 20-bit for 2 Ms/s) should not overlap the CRC-field at the end of the packet. See Figure 4.8 and Figure 4.10 for reference. The integral sums are recorded as fn, where n is an integer from 1 to k (for Uncoded 1 Ms/s and 2 Ms/s) and 5 to k (for LE Coded S=8). fk represents the last integral sum before the start of the CRC field in the packet. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **25 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

6. Steps 2–6 are repeated for ≥ 10 packets. 

7. Steps 2–7 are repeated when the IUT is transmitting at the remaining frequencies defined in the test condition section. 

**==> picture [442 x 319] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 0 1 0 1 0 1 0 1 0 0<br>fTX0 Actual center frequency<br>fTX Nominal center frequency<br>Integration interval<br>02.12.2008 - 09.12.2008 t<br>Start of preamble Start of sync word<br>Figure 4.7: Initial frequency offset (f0) measurement principle 0) measurement principle ) measurement principle<br>Sync word and  Payload<br>Preamble header/length field<br>f<br>Integration interval9/22/2017 - 9/29/2017 Integration interval #19/22/2017 - 9/29/2017 f1 Integration interval #29/22/2017 - 9/29/2017 f2 t<br>Start of  Start of sync  Start of<br>preamble word payload field<br>1 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1<br>fTX0<br>**----- End of picture text -----**<br>


_Figure 4.7: Initial frequency offset (f0) measurement principle 0) measurement principle ) measurement principle_ 

_Figure 4.8: Frequency drift measurement principle_ 

**==> picture [440 x 75] intentionally omitted <==**

**----- Start of picture text -----**<br>
sync word, header-<br>and length fields Payload<br>Preamble<br>f0 f1 f2 f3 f4 f5 f6 f7<br>Frequency drift rate Frequency drift rate 1 = f #1  =n f – f6 n-–5 f(150 (50ms intervalms interval))<br>Frequency drift rate  #2 = f7 – f2 (50ms interval)<br>Frequency drift rate  #3 = f8 – f3 (50ms interval)<br>Frequency drift rate  #0  = f1 –<br>f0 (57.5ms interval)<br>**----- End of picture text -----**<br>


_Figure 4.9: Frequency drift rate measurement principle_ 

**==> picture [435 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
PREAMBLE AA + CI + PHR PDU PAYLOAD<br>16us 16us 16us 16us 26us 16us 16us 16us 16us 16us 16us<br>f0 f1 f2 f3 f4 f5 f6 f7 f8 fk<br>First 2  48us Last 14  48us<br>symbols of symbols of 48us<br>preamble preamble<br>**----- End of picture text -----**<br>


_Figure 4.10: Frequency drift rate measurement principle for S=8_ 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **26 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Expected Outcome 

For Uncoded 1 Ms/s and 2 Ms/s, the maximum drift rate is 20 kHz/50 µs, anywhere in the packet. The maximum drift rate applies to the difference between any two bit groups (10-bit for Uncoded 1 Ms/s, 20-bit for 2 Ms/s) separated by 50 µs within the payload field of the packet transmitted by the IUT. The requirement also applies to the frequency difference between the initial frequency measurement f0 and the first payload frequency measurement f1. See Figure 4.9 for reference. 

For LE Coded (S=8), the maximum drift rate is 19.2 kHz/48 µs, anywhere in the packet. The maximum drift rate applies to the difference between any two groups of 16 symbols separated by 48 µs within the payload field of the packet transmitted by the IUT. The requirement also applies to the frequency difference between the initial frequency measurement f0 and f3 within the preamble. See Figure 4.10 for reference. 

All measured values fulfill the following conditions at the low, mid and high frequencies. 

## Pass verdict 

fTX – 150 kHz ≤ fn ≤ fTX + 150 kHz 

where fTX is the nominal transmit frequency and n=0,1,2,3…k 

- |f0 – fn| ≤ 50 kHz 

where n=2,3,4…k 

and Drift Requirement Limits specified in Table 4.9. 

In all of the above pass verdict requirements, fk is the last frequency measurement before the CRC field. 

## **4.6.5 Carrier frequency offset and drift, Constant Tone Extension** 

- Test Purpose 

Verify that the carrier frequency offset and carrier drift of the transmitted Constant Tone Extension portion in a transmitted signal with uncoded data is within specified limits at normal operating conditions. 

- Reference 

[8] Chapter 3.3 

- 

- Initial Condition 

- The IUT is set to direct TX mode at maximum output power. Whitening is turned off. 

- Frequency hopping off, fixed frequency. 

- The values of MAX_TX_LENGTH, MAX_TX_LENGTH_2M, and TSPX_CTE_len_max (for which the TC is performed) are specified in Section 6.6. 

- The IUT is set to transmit AoA Constant Tone Extensions. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **27 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Test Case Configuration 

|**Test Case**|**Drift Requirement Limits**|**Symbol Rate**|**Payload Length**|
|---|---|---|---|
|||||
|RFPHY/TRM/BV-16-C [Carrier<br>frequency offset and drift, uncoded<br>data at 1 Ms/s, Constant Tone<br>Extension]||fs1– fp| ≤ 19.2 kHz<br>|fsi– f0|i=1,2,3,4…k≤ 50 kHz<br>|fsi– fsi-3|i=4…k≤ 19.2 kHz|1 Ms/s|MAX_TX_LENGTH|
|RFPHY/TRM/BV-17-C [Carrier<br>frequency offset and drift at 2 Ms/s,<br>Constant Tone Extension]||fs1– fp| ≤ 13.  kHz<br>|fsi– f0|i=1,2,3,4…k≤ 50 kHz<br>|fsi– fsi-3|i=4…k≤ 19.2 kHz|2 Ms/s|MAX_TX_LENGTH_2M|



_Table 4.10: Carrier frequency offset and drift, Constant Tone Extension test cases_ 

- Test Procedure 

   1. The IUT is set to transmit at the lowest frequency for testing defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case). 

   2. The IUT transmits LE test packets with Payload Length (specified in Table 4.10) octet payload consisting of a repetitive sequence of 0Fhex octets (11110000bin in transmission order) in the payload and with TSPX_CTE_len_max * 8 μs Constant Tone Extension. See [9] Section 4, “LE Test Packet Definition” for details. 

   3. The following settings are used for the Lower Tester: 

Center frequency lowest frequency for testing as defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case) 

Mode FM demodulation Demodulator filter BW Specified in Section 6.9 (minimum) Filter passband ripple Specified in Section 6.9 Trigger RF (trigger on rising edge) 

The following measurement channel filter minimum attenuator characteristics are used: 

|**Frequency (for 1Ms/s)**|**Frequency (for 2Ms/s)**|**Attenuation**|
|---|---|---|
|650 kHz|±1.3 MHz|-3 dB|
|1 MHz|±2.0 MHz|-14 dB|
|2 MHz|±4.0 MHz|-44 dB|



4. The payload is FM demodulated with the settings described in Step 3. The average frequency deviation measurement starts at the beginning of the fifth bit of the payload (see Figure 4.11 for description). The last four bits in the payload are disregarded (i.e., last bit in the measurement is the fourth bit in the final payload octet). 

5. Each individual bit is to be oversampled at least 32 times. The sequence center frequency; f1ccf is calculated as the average frequency of all samples over each 00001111bin sequence. 

6. For the second, third, sixth, and seventh bits in each 00001111bin sequence, the absolute value of the frequency offset from f1ccf is recorded as ∆f1max. ∆f1max is defined as the average deviation for each individual bit. See Figure 4.11 for reference. 

7. The average frequency value of all ∆f1max frequencies in a packet is calculated and recorded as ∆f1avg. 

8. The initial frequency offset measurement f0 is to be performed at the start of the preamble field in the transmitted packet. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **28 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

For Uncoded 1 Ms/s, the Lower Tester integrates the frequency of the FM demodulated signal from the center of the first preamble bit to the center of the first bit following the 8th preamble bit, 8 bits in total. See Figure 4.12 for reference. 

For 2 Ms/s, the Lower Tester integrates the frequency of the FM demodulated signal from the center of the first preamble bit to the center of the first bit following the 16th preamble bit, 16 bits in total. 

9. The integral sum in Step 8 is considered to be the initial carrier frequency of the IUT, and is recorded as f0. 

10. The average center frequency measurement fp is to be performed starting at the (n+1)th bit of the payload and 

For Uncoded 1 Ms/s, covering 16 bits, where n = (MAX_TX_LENGTH * 8) - 20. 

For 2 Ms/s, covering 32 bits, where n = (MAX_TX_LENGTH_2M * 8) – 36. 

The first n bits and the last 4 bits are not used for this measurement. See Figure 4.13 and Figure 4.14 for reference. 

11. The average frequency deviation measurement f3maxi and carrier frequency offset measurement fsi within the Constant Tone Extension are to be performed starting at the first bit of the reference period within the Constant Tone Extension covering 16 µs units. The first 4 µs of the Constant Tone Extension are not used for the measurement. For bursts with odd number of Constant Tone Extension units, the last 4 µs of the Constant Tone Extension portion are not used. For bursts with even number of Constant Tone Extension units, the last 12 µs of the Constant Tone Extension portion are not used for the measurement. fsi is recorded as f3maxi - ∆f1avg. See Figure 4.15 for reference. 

12. Steps 2–11 are repeated for ≥ 10 packets. 

13. Steps 2–12 are repeated when the IUT is transmitting at the remaining frequencies defined in the test condition section. 

**==> picture [343 x 256] intentionally omitted <==**

**----- Start of picture text -----**<br>
average over samples<br>Note    f1  is defined as<br> max<br>the average of the samples<br>within the bit period 1 1 1 1<br>f<br>  f 1<br> avg<br> f1  f1<br> max    max<br>1 1 1 1 0 0 0 0 1 1 1 1 f1<br> ccf<br> f1  f1<br> max 2  max 3<br>t   f1<br> avg<br>11110000 sequence 1 sequence 2<br>Start of  Start of  Start of<br>payload field measurement  1 measurement  2<br>**----- End of picture text -----**<br>


_Figure 4.11: Frequency deviation measurement principle for 11110000-payload sequence_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **29 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [345 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 0 1 0 1 0 1 0 1 0 0<br>fTX0 Actual center frequency<br>fTX Nominal center frequency<br>Integration interval<br>02.12.2008 - 09.12.2008 t<br>Start of preamble Start of sync word<br>**----- End of picture text -----**<br>


_Figure 4.12: Initial carrier frequency (f0) measurement principle for 1 Ms/s_ 

**==> picture [373 x 315] intentionally omitted <==**

**----- Start of picture text -----**<br>
Sync word, header, length, CTEInfo<br>Payload<br>Preamble CRC<br>16ms<br>Last 4 bits of payload<br>Figure 4.13: Average center frequency measurement (fp) measurement location p) measurement location ) measurement location<br>Time (bits or symbols)<br>0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1<br>  = Mean Frequency<br>Deviation over the 16 bit<br>00001111bin sequence<br>Frequency deviation<br>**----- End of picture text -----**<br>


_Figure 4.13: Average center frequency measurement (fp) measurement location p) measurement location ) measurement location_ 

_Figure 4.14: Average center frequency measurement (fp) principle_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **30 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [408 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Constant Tone Extension<br>Guard (4ms) Reference (8ms) 8ms 8ms 8ms 8ms 8ms 8ms 8ms 4ms Odd number of CTE Units<br>OR<br>Constant Tone Extension<br>Guard (4ms) Reference (8ms) 8ms 8ms 8ms 8ms 8ms 8ms 8ms 8ms 4ms Even number of CTE Units<br>**----- End of picture text -----**<br>


**==> picture [33 x 16] intentionally omitted <==**

**==> picture [32 x 17] intentionally omitted <==**

**==> picture [32 x 17] intentionally omitted <==**

**==> picture [32 x 16] intentionally omitted <==**

_Figure 4.15: Average frequency deviation measurement principle_ 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- 

- Expected Outcome 

## Pass verdict 

fTX – 150 kHz ≤ fsi ≤ fTX + 150 kHz 

where fTX is the nominal transmit frequency and i=1,2,3…k 

fTX – 150 kHz ≤ f0 ≤ fTX + 150 kHz 

and Drift Requirement Limits specified in Table 4.10. 

## **4.6.6 Tx Power Stability, AoD Transmitter** 

- Test Purpose 

Verify that the AoD transmit signal has settled at the beginning of the reference period and the transmit slots, and remains stable within the reference period and transmit slots, respectively. 

- Reference 

   - [8] Section 5 

   - [9] Section 4.1 

- Initial Condition 

   - The IUT is set to direct TX mode at maximum output power. Whitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The values of TSPX_CTE_len_max (for which the TC is performed) are specified in Section 6.6. 

   - The IUT is set for a symbol rate as specified in Table 4.21. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **31 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Test Case Configuration 

|**Test Case**|**PHY**|**Slot Duration**|
|---|---|---|
|RFPHY/TRM/PS/BV-01-C [Tx Power Stability, AoD<br>Transmitter at 1 Ms/s with 2µs SwitchingSlot]|1 Ms/s|2 µs|
|RFPHY/TRM/PS/BV-02-C [Tx Power Stability, AoD<br>Transmitter at 1 Ms/s with 1µs SwitchingSlot]|1 Ms/s|1 µs|
|RFPHY/TRM/PS/BV-03-C [Tx Power Stability, AoD<br>Transmitter at 2 Ms/s with 2µs SwitchingSlot]|2 Ms/s|2 µs|
|RFPHY/TRM/PS/BV-04-C [Tx Power Stability, AoD<br>Transmitter at 2 Ms/s with 1µs SwitchingSlot]|2 Ms/s|1 µs|



_Table 4.11: Tx Power Stability, AoD Transmitter test cases_ 

- Test Procedure 

   1. The IUT transmits LE test packets with no payload and with TSPX_CTE_len_max * 8 µs Constant Tone Extension with switching slots as specified in Table 4.11. See [9], Section 4, “LE Test Packet Definition” for details. 

   2. The following settings are used for the Lower Tester: 

Center Frequency at the lowest frequency for testing defined in the test condition section Frequency Span Zero Span Resolution BW 3 MHz Video BW 3 MHz Detector Average 

   3. The RF power of the CTE is measured with the settings described in Step 2. 

   4. The Lower Tester records PREF,AVE, as the average power during the reference period, measured from the beginning of the first symbol of the reference period to the end of the last symbol within the reference period. 

   5. The Lower Tester records PREF,DEV as the maximum absolute deviation between any one sample of the output power taken during the reference period relative to PREF,AVE, recorded in Step 4. 

   6. For each transmit slot, n, Lower Tester records Pn,AVE as the average power within the slot, where n is an integer from 1 to k, where k is the number of transmit slots within the packet. 

   7. For each transmit slot, n, Lower Tester records Pn,DEV as the as the maximum absolute deviation between any one sample of the output power within the transmit slot relative to average power within the slot, PN,AVE, recorded in Step 6. 

   8. Steps 3–7 are repeated when the IUT is transmitting at the remaining frequencies defined in the test condition section. 

- Test Condition 

The IUT and the Lower Tester are set up according to the cabled testing setup described in Section 4.8 and Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**PHY**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|---|
|All|1 Ms/s|2402 MHz(n=0)|2440 MHz(n=19)|2480 MHz(n=39)|
|All|2 Ms/s|2404 MHz(n=1)|2440 MHz(n=19)|2478 MHz(n=38)|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **32 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Expected Outcome 

The maximum deviation of the signal power within the reference period is ≤ 25% of the average signal power measured within the reference period. 

The maximum deviation of the signal power within a TX slot is ≤ 25% of the average signal power measured within that TX slot. 

All measured values fulfill the following conditions at the low, mid, and high frequencies. 

## Pass verdict 

For each frequency, the following conditions are satisfied: 

- PREF,DEV / PREF,AVE < 0.25 

- Pn,DEV / Pn,AVE < 0.25 for n=1,2,3,…,k 

## **4.6.7 Antenna switching integrity, AoD Transmitter** 

- Test Purpose 

Verify that the antenna switching occurs during the switching slots of the Constant Tone Extension for an AoD transmit signal. 

- Reference 

   - [8] Section 5 

   - [9] Section 4.1 

- Initial Condition 

   - The IUT is set to direct TX mode at maximum output power. Whitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The values of TSPX_CTE_len_max (for which the TC is performed) are specified in Section 6.6. 

   - The IUT is set for a symbol rate as specified in Table 4.12. 

- Test Case Configuration 

|**Test Case**|**PHY**|**Slot Duration**|
|---|---|---|
|RFPHY/TRM/ASI/BV-05-C [Antenna switching integrity,<br>AoD Transmitter at 1 Ms/s with 2µs SwitchingSlot]|1 Ms/s|2 µs|
|RFPHY/TRM/ASI/BV-06-C [Antenna switching integrity,<br>AoD Transmitter at 1 Ms/s with 1µs SwitchingSlot]|1 Ms/s|1 µs|
|RFPHY/TRM/ASI/BV-07-C [Antenna switching integrity,<br>AoD Transmitter at 2 Ms/s with 2µs SwitchingSlot]|2 Ms/s|2 µs|
|RFPHY/TRM/ASI/BV-08-C [Antenna switching integrity,<br>AoD Transmitter at 2 Ms/s with 1µs SwitchingSlot]|2 Ms/s|1 µs|



_Table 4.12: Antenna switching integrity, AoD Transmitter test cases_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **33 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Test Procedure 

   1. The IUT transmits LE test packets with no payload and with TSPX_CTE_len_max * 8 µs Constant Tone Extension with switching slots as specified in Table 4.12. See [9], Section 4, “LE Test Packet Definition” for details. 

   2. The following settings are used for the Lower Tester: 

Center Frequency at the lowest frequency for testing defined in the test condition section Frequency Span Zero Span Resolution BW 3 MHz Video BW 3 MHz Detector Average 

   3. All non-reference antenna ports are disconnected and terminated. 

   4. The Lower Tester records the average output power during nth Tx slot, where n = 1 to k (Nof Tx slots in the packet), Pn,AVE,OFF. 

   5. Connect the Xth non reference antenna port, where X = 1 .. number of non-reference antennae. All other non-reference antennae are disconnected and terminated. 

   6. The Lower Tester records the average output power during the nth Tx slot, where n = 1 to k (Nof Tx slots in the packet), Pn,X,AVE,ON. 

   7. Repeat Steps 5–6 for all non-reference antennae. 

- Test Condition 

The IUT and Lower Tester are set up according to the cabled testing setup described in Section 4.8 and Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**PHY**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|---|
|All|1 Ms/s|2402 MHz(n=0)|2440 MHz(n=19)|2480 MHz(n=39)|
|All|2 Ms/s|2404 MHz(n=1)|2440 MHz(n=19)|2478 MHz(n=38)|



- Expected Outcome 

The average signal power measured when an antenna port is connected is at least 10 dB > the average signal power measured when the antenna port is disconnected in the transmit slots corresponding to the antenna. 

All measured values fulfill the following conditions at the low, mid and high frequencies. 

## Pass verdict 

For each frequency, the following conditions are satisfied: 

- Pm,X,AVE,ON - Pm,AVE,OFF ≥ 10 dB, 

where m corresponds to the Tx slot corresponding to the antenna X transmission, and 

X = 1 .. Number of non-reference antenna 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **34 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4.6.8 CS Stable Phase** 

- Test Purpose 

Verify that the IUT’s carrier phase remains stable for the period of T_PM_MEAS, where T_PM_MEAS is the maximum duration of a CS_Tone used for measurement. 

- Reference 

   - [11] Section 3.4 

- Initial Condition 

   - Roles are non-configurable; the IUT is fixed in the Initiator role. 

   - A static Access Address (CS Sync Word) is used for the duration of the test, see Section 4.3.3.1. 

   - A fixed 1:1 antenna configuration is used in the Test Equipment Setup, see Section 4.2.3. 

   - The IUT’s transmitter is set to maximum output power. 

   - The transmit frequency for the entire CS subevent is fixed at 𝑓𝑂 , see Section 4.3.2. 

Within the Main-Mode period, only a single IUT transmission occurs as described in Figure 4.16. This is a special test scenario whereby the Lower Tester (in the Reflector role), may choose not to respond to the IUT’s transmission, see [12] Section 2.4 for details. 

**==> picture [341 x 278] intentionally omitted <==**

_Figure 4.16: Stable Phase test signal transmission overview_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **35 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

The IUT transmits a CS_Tone of duration 652 μs (T_PM) as shown in Figure 4.17. T_PM_MEAS (of duration 650 us) is defined as the Stable Phase Evaluation Window, the period in which the Lower Tester samples the CS_Tone as described in Figure 4.17. 

**==> picture [342 x 270] intentionally omitted <==**

_Figure 4.17: Stable Phase measurement overview_ 

- Test Case Configuration 

|**Test Case**|**PHY**|**Main Mode**<br>**Type**|
|---|---|---|
|RFPHY/TRM/CS/BV-01-C[Stable Phase, 1 Ms/s, CS_Tone]|1 Ms/s|CS_Tone|
|RFPHY/TRM/CS/BV-02-C[Stable Phase, 2 Ms/s, CS_Tone]|2 Ms/s|CS_Tone|



_Table 4.13: CS Stable Phase test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to enable the Channel Sounding procedure using the Override_Config bit number 10 parameter enabled (Stable Phase test). 

   2. The Lower Tester uses the PHY test filter characteristics as defined in Section 6.9. 

   3. The IUT sends a Mode-0 transmission to the Lower Tester. The Lower Tester responds with a Mode-0 transmission. 

   4. The IUT sends a CS_Tone transmission. The Lower Tester synchronizes to the previous Mode0 CS_SYNC (CS_SYNC_0_I) transmission, measuring the CS_Tone sent by the IUT following a period of T_RD+T_IP2+T_SY+T_GD+T_FM+T_RD+T_FCS+ 1 μ𝑠 , where 1 μ𝑠 accounts for exclusion period (see Figure 4.17). 

   5. The CS_Tone is down converted and sampled at 1 μ𝑠 intervals during the period of T_PM_MEAS. 

   6. The zero mean, detrended phase ϕ𝑧𝑚𝑑[𝑛] is calculated (see [11] Chapter 3.4, Stable Phase). 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **36 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

7. Steps 1–6 are repeated to obtain at least 10,000 absolute values of ϕ𝑧𝑚𝑑[𝑛] . 

10,000 This will require [ 650 ] CS sub-events, where ⌈𝑥⌉= 𝑐𝑒𝑖𝑙𝑖𝑛𝑔(𝑥) . 

   8. Steps 1–7 are repeated for the remaining frequencies as defined in Section 4.3.2. 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. The default frequencies are defined in Section 4.3.2. 

- Expected Outcome 

Pass verdict 

95% of at least 10,000 absolute values of ϕ𝑧𝑚𝑑[𝑛] are ≤20° . 

## **4.6.9 CS Modulation Characteristics, 2 Ms/s, BT = 2.0** 

- Test Purpose 

Verify that the modulation characteristics of the transmitted signal are correct when transmitting data at 2 Ms/s, BT = 2.0. 

- Reference 

   - [11] Section 3.1 

- Initial Condition 

   - The Lower Tester is configured as the Reflector and the IUT as the Initiator. 

   - A static Access Address (CS Sync Word) is used for the duration of the test, see Section 4.3.3.1. 

   - A fixed 1:1 antenna configuration is used in the Test Equipment Setup, see Section 4.2.3. 

   - The IUT’s transmitter is set to maximum output power. 

   - The IUT is configured to transmit a fixed sequence of 𝑀 Mode-0 CS steps, where 𝑀 is the minimum number of Mode-0 steps the IUT supports. 

   - The transmit frequency for the entire CS subevent is fixed at 𝑓0 (see Section 4.3.2). 

- Test Case Configuration 

|**TCID**|**PHY**|**Main Mode Type**|
|---|---|---|
|RFPHY/TRM/CS/BV-03-C [Modulation<br>Characteristics, 2 Ms/s, BT = 2.0, Mode-1]|2 Ms/s, BT = 2.0|Mode-1|
|RFPHY/TRM/CS/BV-04-C [Modulation<br>Characteristics, 2 Ms/s, BT = 2.0, Mode-3]|2 Ms/s, BT = 2.0|Mode-3|



_Table 4.14: CS Modulation Characteristics, 2 Ms/s, BT = 2.0 test cases_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **37 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [339 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
average over samples<br>1 4<br>3 4<br>1 1 1 1<br>f<br>  f3<br> avg<br> f3<br> avg 2<br>1 1 1 1 0 0 0 0 1 1 1 1 f3<br> ccf<br> f3<br> avg 1<br>t   f3<br> avg<br>11110000 sequence 1 sequence 2<br>Start of  Start of  Start of<br>payload field measurement  1 measurement  2<br>**----- End of picture text -----**<br>


_Figure 4.18: CS 2Ms/s BT = 2.0 frequency deviation measurement principle for 11110000-payload sequence_ 

**==> picture [342 x 269] intentionally omitted <==**

_Figure 4.19: CS 2Ms/s BT = 2.0 frequency deviation measurement principle for 10101010-payload sequence_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **38 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester commands the IUT to enable the Channel Sounding procedure with: ▪ Role set to Initiator 

      - Test command Override_Config bit 8 set enabling the CS_SYNC_Payload_Pattern parameter 

      - CS_SYNC_Payload_Pattern set to 0x01, the value for repeated 11110000𝑏𝑖𝑛 sequence (in transmission order) 

      - Mode-0 CS Steps set to 𝑀 steps, where 𝑀= 3 

      - Main Mode CS steps set to 1 ≤𝐾 ≤72 

      - Lowest frequency for testing as defined in Section 4.3.2 

      - Other parameters as specified in Section 4.3.3 

   2. The Lower Tester uses the 2 Ms/s, BT = 2.0 PHY test filter characteristics as defined in Section 6.9. 

   3. The IUT sends a Mode-0 transmission to the Lower Tester. 

   4. The Lower Tester responds with a Mode-0 transmission. 

   5. Main-Mode CS steps are exchanged between the Lower Tester and the IUT. 

   6. The wanted signal packet payload is FM demodulated with the settings described in Step 2. The measurement starts at the beginning of the fifth bit of the payload (see Figure 4.18 for description). The last four bits in the payload are disregarded (i.e., the last bit in the measurement is the fourth bit in the 16th octet). 

   7. Each individual bit is to be oversampled at least 32 times. The sequence center frequency 𝑓3𝑐𝑐𝑓 is calculated as the average frequency of all samples over each 11110000𝑏𝑖𝑛 sequence. 

   8. Starting at ¾ of the first bit and ending after ¼ of the fourth bit, and starting at ¾ of the fifth bit and ending after ¼ of the eighth bit in each 11110000𝑏𝑖𝑛 sequence, the absolute value of the frequency offset from 𝑓3𝑐𝑐𝑓 is recorded as ∆𝑓3𝑚𝑎𝑥 . ∆𝑓3𝑚𝑎𝑥 and is defined as the average deviation for each individual bit. See Figure 4.18 for reference. 

   9. The average frequency value of all ∆𝑓3𝑚𝑎𝑥 frequencies in a packet is calculated and recorded as ∆𝑓3𝑎𝑣𝑔 . 

   10. The IUT transmits LE CS test packets of maximal length with payload pattern set to a repetitive 1010101010𝑏𝑖𝑛 sequence. 

   11. The payload is FM demodulated with the settings described in Step 2. The measurement starts at the beginning of the fifth bit in the payload field. The last four bits in the payload are disregarded (i.e., last bit in the measurement is the fourth bit in the final payload octet). 

   12. Each individual bit is oversampled at least 32 times. The sequence center frequency 𝑓4𝑐𝑐𝑓 is calculated as the average frequency of all samples over each 1010101010𝑏𝑖𝑛 sequence. 

   13. The average deviation measured from ¼ to ¾ of each bit from the sequence center frequency 𝑓4𝑐𝑐𝑓 is recorded as ∆𝑓4𝑎𝑣𝑔 for each individual bit. See Figure 4.19 for reference. 

   14. Main-Mode steps are measured to obtain a total number of 𝐾= 52 CS steps. 52 

   This will require [ 𝐾 ] CS sub-events, where [𝑥] = 𝑐𝑒𝑖𝑙𝑖𝑛𝑔(𝑥) . 

   15. Repeat Steps 1–14 for the remaining frequencies as defined in Section 4.3.2. 

- Expected Outcome 

## Pass verdict 

All measured values must fulfill the following conditions at the test frequencies defined in Section 4.3.2: 

- 450 𝑘𝐻𝑧≤ ∆𝑓3𝑎𝑣𝑔 ≤550 𝑘𝐻𝑧 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **39 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

At least 99.7% of all ∆𝑓4𝑎𝑣𝑔 frequency values recorded over 52 LE CS test packets must be > 420 kHz. 

∆𝑓4𝑎𝑣𝑔 ▪ ≥0.95 ∆𝑓3𝑎𝑣𝑔 

## **4.6.10 CS TX Output SNR Control** 

- Test Purpose 

Verify that the configured SNR output for an IUT’s transmitted signal is within limits. 

- Reference 

   - [11] Section 3.1.3 

- Initial Condition 

   - The Lower Tester is configured as the Reflector and the IUT as the Initiator. 

   - A static Access Address (CS Sync Word) is used for the duration of the test, see Section 4.3.3.1. 

   - A fixed 1:1 antenna configuration is used in the Test Equipment Setup, see Section 4.2.3. 

   - The IUT’s transmitter is set to maximum output power. 

   - The IUT is configured to the lowest supported SNR (SNRmin) output level index (SOI). 

   - The IUT is configured to transmit a fixed sequence of 𝑀 Mode-0 CS steps, where 𝑀 is the minimum number of Mode-0 steps the IUT supports. 

   - The transmit frequency for the entire CS subevent is fixed at 𝑓0 (see Section 4.3.2). 

   - The list of supported SNR Output Levels is defined by the TSPX_SNR IXIT value. 

- Test Case Configuration 

|**TCID**|**PHY**|**Main Mode**<br>**Type**|
|---|---|---|
|RFPHY/TRM/CS/BV-05-C [TX SNR Output Control, 1<br>Ms/s, Mode-1]|1 Ms/s|Mode-1|
|RFPHY/TRM/CS/BV-06-C [TX SNR Output Control, 1<br>Ms/s, Mode-3]|1 Ms/s|Mode-3|
|RFPHY/TRM/CS/BV-07-C [TX SNR Output Control, 2<br>Ms/s, Mode-1]|2 Ms/s|Mode-1|
|RFPHY/TRM/CS/BV-08-C [TX SNR Output Control, 2<br>Ms/s, Mode-3]|2 Ms/s|Mode-3|
|RFPHY/TRM/CS/BV-09-C [TX SNR Output Control, 2<br>Ms/s, Mode-1, BT = 2.0]|2 Ms/s, BT = 2.0|Mode-1|
|RFPHY/TRM/CS/BV-10-C [TX SNR Output Control, 2<br>Ms/s, Mode-3, BT = 2.0]|2 Ms/s, BT = 2.0|Mode-3|



_Table 4.15: CS TX Output SNR Control test cases_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **40 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Test Procedure 

   1. The Upper Tester commands the IUT to enable the Channel Sounding procedure with: 

         - Role set to Initiator 

         - RTT_Type set to the value of 0𝑥00 (RTT AA Only) 

         - Mode-0 CS Steps set to 𝑀 steps, where 𝑀= 1 

         - Main Mode CS steps set to 1 ≤𝐾 ≤72 

         - Lowest frequency for testing as defined in Section 4.3.2 

         - Other parameters as specified in Section 4.3.3 

   2. The Lower Tester uses the PHY test filter characteristics as defined in Section 6.9. 

   3. The IUT sends a Mode-0 transmission to the Lower Tester. 

   4. The Lower Tester responds with a Mode-0 transmission. 

   5. Main-Mode CS steps as defined in Table 4.15 are exchanged between the Lower Tester and the IUT. 

   6. The Lower Tester down converts and measures the CS_SYNC portion sent by the IUT continuously over time within step 𝑘 (see [11] Section 3.1.1) for each Main-Mode packet received with the filter characteristics as defined in Section 6.9. The IUT’s transmitter SNR is then computed per CS Main-Mode step to provide a value of 𝑆𝑁𝑅𝑇𝑋(𝑘) . 

   7. For each CS Main-Mode step, a value of 𝑆𝑁𝑅𝑇𝑋𝑒𝑟𝑟𝑜𝑟(𝑘) is calculated as |𝑆𝑁𝑅𝑇𝑋𝑑𝑒𝑠𝑖𝑟𝑒𝑑 − 𝑆𝑁𝑅𝑇𝑋(𝑘)| , where 𝑆𝑁𝑅𝑇𝑋𝑑𝑒𝑠𝑖𝑟𝑒𝑑 is the configured SNR output value at the IUT. 

   - 𝑒𝑟𝑟𝑜𝑟 

   - 8. Steps 1–7 are repeated to obtain at least 10,000 values of 𝑆𝑁𝑅𝑇𝑋 (𝑘) . 

      - 10,000 

      - This will require [ 𝐾 ] CS sub-events, where [𝑥] = 𝑐𝑒𝑖𝑙𝑖𝑛𝑔(𝑥) . 

   9. Repeat Steps 1–8 for the remaining frequencies as defined in Section 4.3.2. 

   10. Repeat Steps 1–9 for each supported SNR output level in TSPX_SNR. 

- Expected Outcome 

## Pass verdict 

The measured SNR output control error values must fulfill the following condition: 

- 𝑆𝑁𝑅𝑇𝑋𝑒𝑟𝑟𝑜𝑟(𝑘) ≤3 𝑑𝐵 

The standard deviation of the randomness of the added error satisfies: 

• 𝑠𝑡𝑑(𝑆𝑁𝑅𝑇𝑋𝑒𝑟𝑟𝑜𝑟(𝑘)) ≥0.25 𝑑𝐵 

for 95% of at least 10,000 CS steps. 

## **4.7 Receiver tests (RCV)** 

## **4.7.1 Receiver sensitivity** 

- Test Purpose 

Verify that the receiver sensitivity is within limits for non-ideal signals at normal operating conditions when receiving a signal. For stable modulation tests, the receiver is set to assume the transmitter has a stable modulation index. The non-ideal signals used in this test are within the specification limits but deviate from the ideal case. 

- Reference 

   - [2] Chapter 4.1 

   - [6] Chapter 4.1 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **41 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The Lower Tester’s transmit power is chosen such that the input power to the IUT receiver is as specified in Table 4.9. 

   - The value of MAX_RX_LENGTH, MAX_RX_LENGTH_2M, MAX_RX_LENGTH_CODED_S2, and MAX_RX_LENGTH_CODED_S8 (for which the TC is performed) is specified in Section 6.6. 

   - The IUT is set to assume the transmitter has a standard modulation index or stable modulation index (specified in Table 4.16). 

- Test Case Configuration 

|**Test Case**|**Modulation**|**Input**<br>**Power**|**Symbol**<br>**Rate**|**Payload Length**|
|---|---|---|---|---|
|RFPHY/RCV/BV-01-C [Receiver sensitivity,<br>uncoded data at 1 Ms/s]|Standard|-70 dBm|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-08-C [Receiver sensitivity at 2<br>Ms/s]|Standard|-70 dBm|2 Ms/s|MAX_RX_LENGTH_2M|
|RFPHY/RCV/BV-14-C [Receiver Sensitivity,<br>uncoded data at 1 Ms/s, Stable Modulation<br>Index]|Stable|-70 dBm|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-20-C [Receiver sensitivity at 2<br>Ms/s, Stable Modulation Index]|Stable|-70 dBm|2 Ms/s|MAX_RX_LENGTH_2M|
|RFPHY/RCV/BV-26-C [Receiver sensitivity, LE<br>Coded (S=2)]|Standard|-75 dBm|1 Ms/s<br>coded S=2|MAX_RX_LENGTH_CO<br>DED_S2|
|RFPHY/RCV/BV-27-C [Receiver sensitivity, LE<br>Coded (S=8)]|Standard|-82 dBm|1 Ms/s<br>coded S=8|MAX_RX_LENGTH_CO<br>DED_S8|
|RFPHY/RCV/BV-32-C [Receiver sensitivity, LE<br>Coded (S=2), Stable Modulation Index]|Stable|-75 dBm|1 Ms/s<br>coded S=2|MAX_RX_LENGTH_CO<br>DED_S2|
|RFPHY/RCV/BV-33-C [Receiver sensitivity, LE<br>Coded (S=8), Stable Modulation Index]|Stable|-82 dBm|1 Ms/s<br>coded S=8|MAX_RX_LENGTH_CO<br>DED_S8|



_Table 4.16: Receiver sensitivity test cases_ 

- Test Procedure 

   1. The IUT is set to receive at the lowest frequency for testing defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case). 

   2. The Lower Tester transmits LE test packets with PRBS9 payload with Payload Length (specified in Table 4.16). See [4], Section 4, “LE Test Packet Definition” for details. 

   3. The signal characteristics of the modulated signal transmitted by the Lower Tester are to be changed over time. The signal parameter sets to be used are described in Table 4.17. All other parameters are as defined in Section 6.1. 

   4. The Lower Tester transmits the first 50 packets using the first parameter set; the next 50 packets are transmitted using the second parameter set etc. Upon completion of the last parameter set, the sequence is repeated. The PER is measured according to Section 6.3. 

   5. Steps 2–4 are repeated when the IUT is receiving at the remaining frequencies defined in the test condition section. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **42 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Test Run**|**Carrier Frequency**<br>**Offset**|**Modulation Index**||**Symbol Timing**<br>**Error**|
|---|---|---|---|---|
|||**Standard**<br>**Modulation**|**Stable**<br>**Modulation**||
|**1**|100 kHz|0.45|0.495|-50ppm|
|**2**|19 kHz|0.48|0.498|-50ppm|
|**3**|-3 kHz|0.46|0.496|+50ppm|
|**4**|1 kHz|0.52|0.502|+50ppm|
|**5**|52 kHz|0.53|0.503|+50ppm|
|**6**|0 kHz|0.54|0.504|-50ppm|
|**7**|-56 kHz|0.47|0.497|-50ppm|
|**8**|97 kHz|0.5|0.500|-50ppm|
|**9**|-25 kHz|0.45|0.495|-50ppm|
|**10**|-100 kHz|0.55|0.505|+50ppm|



_Table 4.17: Transmitter parameter settings for PER test_ 

In addition to fixed frequency offset, frequency drift over time is added to the signal characteristics. This is implemented by adding a low frequency modulation to the signal. The modulating signal is sinusoidal with deviation of 50 kHz and a modulation frequency of 1250 Hz. The modulating signal is synchronized with the packets so that packets start alternately at 0° and 180° of the modulating signal. See Figure 4.20 for reference. 

**==> picture [340 x 182] intentionally omitted <==**

_Figure 4.20: Dirty transmitter frequency drift emulation principle_ 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- 

- Expected Outcome 

## Pass verdict 

All measured values fulfill the following condition: 

PER < **30.8%** for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is 37 bytes. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **43 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

PER < the value calculated according to the formula specified in Section 6.3.1 for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is > 37 bytes. 

## **4.7.2 C/I and Receiver Selectivity Performance** 

- Test Purpose 

Verify the receiver's performance in the presence of co-/adjacent channel interference. For stable modulation tests, the receiver is set to assume the transmitter has a stable modulation index. The receiver mirror image rejection performance is also verified in this test. 

- Reference 

[2] Chapter 4.2 

[6] Chapter 4.2 

- Initial Condition 

   - Refer to Figure 4.21 for test setup principle. 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The image frequency (fimage for 1 Ms/s or fimage-2M for 2 Ms/s) of the receiver relative to the receiver frequency is declared by the equipment manufacturer as an IXIT value. 

   - The value of MAX_RX_LENGTH, MAX_RX_LENGTH_2M, MAX_RX_LENGTH_CODED_S2, and MAX_RX_LENGTH_CODED_S8 (for which the TC is performed) is specified in Section 6.6. 

   - The IUT is set for a symbol rate as specified in Table 4.18. 

   - The IUT is set to assume the transmitter has a standard modulation index or stable modulation index (specified in Table 4.18). 

- Test Case Configuration 

|**Test Case**|**Modulation**|**Input**<br>**Power**|**Symbol**<br>**Rate**|**Payload Length**|
|---|---|---|---|---|
|RFPHY/RCV/BV-03-C [C/I and Receiver Selectivity<br>Performance, uncoded data at 1 Ms/s]|Standard|-67 dBm|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-09-C [C/I and Receiver Selectivity<br>Performance at 2 Ms/s]|Standard|-67 dBm|2 Ms/s|MAX_RX_LENGTH_2<br>M|
|RFPHY/RCV/BV-15-C [C/I and Receiver Selectivity<br>Performance, uncoded data at 1 Ms/s, Stable<br>Modulation Index]|Stable|-67 dBm|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-21-C [C/I and Receiver Selectivity<br>Performance at 2 Ms/s, Stable Modulation Index]|Stable|-67 dBm|2 Ms/s|MAX_RX_LENGTH_2<br>M|
|RFPHY/RCV/BV-28-C [C/I and Receiver Selectivity<br>Performance, LE Coded (S=2)]|Standard|-72 dBm|1 Ms/s<br>coded<br>S=2|MAX_RX_LENGTH_C<br>ODED_S2|
|RFPHY/RCV/BV-29-C [C/I and Receiver Selectivity<br>Performance, LE Coded (S=8)]|Standard|-79 dBm|1 Ms/s<br>coded<br>S=8|MAX_RX_LENGTH_C<br>ODED_S8|
|RFPHY/RCV/BV-34-C [C/I and Receiver Selectivity<br>Performance, LE Coded (S=2), Stable Modulation<br>Index]|Stable|-72 dBm|1 Ms/s<br>coded<br>S=2|MAX_RX_LENGTH_C<br>ODED_S2|
|RFPHY/RCV/BV-35-C [C/I and Receiver Selectivity<br>Performance, LE Coded (S=8), Stable Modulation<br>Index]|Stable|-79 dBm|1 Ms/s<br>coded<br>S=8|MAX_RX_LENGTH_C<br>ODED_S8|



_Table 4.18: C/I and receiver selectivity performance test cases_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **44 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Test Procedure 

   1. The IUT is set to receive at the low operating frequency listed in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case). 

   2. Two test signals are fed to the IUT input port: 

Wanted signal: 

Packets transmitted at the receiving frequency (fRX) with Payload Length (specified in Table 4.18) octet PRBS9 payload at a Symbol Rate specified in Table 4.18. Refer to Section 6.1 and [4], Section 4 for details. Signal level of the wanted signal at the IUT input port is Input Power (specified in Table 4.18). 

Interference signal: 

Continuous modulated carrier at 2400 MHz, modulated with PRBS15 data at a Symbol Rate specified in Table 4.18. Refer to Section 6.1 and [4], Section 4 for details. Signal level of the interference signal at the IUT input port and frequency relative to the receiving frequency is as defined in Table 4.19. 

3. The Lower Tester's transmit power is chosen such that the input power to the IUT receiver is as listed in Table 4.19. 

4. For 1 Ms/s, Steps 2–3 are repeated for interference frequencies 2400 MHz+NMHz where N=1,2,3…83. 

For 2 Ms/s, Steps 2–3 are repeated for interference frequencies 2400MHz+2N MHz where N=1,2,3…41. 

5. The PER is measured according to Section 6.3. 

6. Steps 2–5 are repeated when the IUT is receiving at the mid- and high operation frequencies listed in the test condition section. 

**==> picture [360 x 160] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tester implementation<br>BluetoothLE modulation Signal generator<br>PRBS15 Input power - C/I + Lt<br>Interferer (Frequency of operation  Isolator<br>and output power as listed  Power combiner Counter incremented for<br>in Table 4.12) 1 each packet received.<br>Dout<br>Isolator  IUT<br>22<br>Bluetooth LE modulation  Signal generator<br>Wanted  PRBS9 Input power + Lt<br>signal (Frequency of operation<br>as listed in Section 4.2)<br>Cable, Isolator and power<br>combiner attenuation<br>Lt<br>**----- End of picture text -----**<br>


_Figure 4.21: C/I and receiver selectivity test setup_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **45 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Interference**<br>**signal frequency1**|**finterference**||**Interferer signal level at IUT**<br>**input port (dBm)**|**Interferer signal level at IUT**<br>**input port (dBm)**|**Interferer signal level at IUT**<br>**input port (dBm)**|**Wanted signal level relative to**<br>**interference signal level**<br>**(C/I requirement) (dB)**|**Wanted signal level relative to**<br>**interference signal level**<br>**(C/I requirement) (dB)**|**Wanted signal level relative to**<br>**interference signal level**<br>**(C/I requirement) (dB)**|
|---|---|---|---|---|---|---|---|---|
|||||**dBm)**|||||
||||||||||
||**1Ms/s and LE**<br>**Coded**|**2Ms/s**|**Uncoded**|**S=2**|**S=8**|**Uncoded**|**S=2**|**S=8**|
|**Co-channel**|**fRX**|**fRX**|-88|-89|-91|21|17|12|
|**Adjacent channel**|**fRX ****1 MHz**|**fRX ****2 MHz**|-82|-83|-85|15|11|6|
|**Adjacent channel**|**fRX ****2 MHz**|**fRX ****4 MHz**|-50|-51|-53|-17|-21|-26|
|**Adjacent channel**|**fRX ****(3+n)**<br>**MHz**<br>**[n=0,1,2…]**|**fRX ****(6+2n)**<br>**MHz**<br>**[n=0,1,2…]**|-40|-41|-43|-27|-31|-36|
|**Image frequency**|**fimage**|**fimage-2M**|-58|-59|-61|-9|-13|-18|
|**Adjacent channel**<br>**to image**<br>**frequency**|**fimage ****1 MHz**|**fimage-2M ****2**<br>**MHz**|-52|-53|-55|-15|-19|-24|



_Table 4.19: C/I and receiver selectivity test parameter settings_ 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- 

- Expected Outcome 

## Pass verdict 

All measured values fulfill the following condition: 

PER < **30.8%** for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is 37 bytes. 

PER < the value calculated according to the formula specified in Section 6.3.1 for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is > 37 bytes. 

For each individual measurement the C/I requirement may be relaxed for a maximum of five interference frequency settings. The C/I-performance is in this case ≤ -17 dB (Interference level at least 17 dB higher than wanted signal level). This relaxation applies to the following measurements: 

- Adjacent channel  2 MHz (for 1 Ms/s) or ± 4 MHz (for 2 Ms/s) 

- Adjacent channel  (3+n) MHz (for 1 Ms/s) or ± (6+2n) MHz (for 2 Ms/s) [n=0,1,2…] 

## **4.7.3 Blocking Performance** 

- Test Purpose 

Verify that the receiver performs satisfactorily in the presence of interference sources operating outside the 2400 MHz – 2483.5 MHz band. 

- Reference 

   - [2] Chapter 4.3 

   - [6] Chapter 4.3 

> 1 If two frequencies defined in Table 4.19 refer to the same physical channel, the less stringent requirement applies. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **46 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The value of MAX_RX_LENGTH and MAX_RX_LENGTH_2M (for which the TC is performed) is specified in Section 6.6. 

   - The IUT is set for a symbol rate as specified in Table 4.20. 

   - The IUT is set to assume the transmitter has a standard modulation index or stable modulation index (specified in Table 4.20). 

- Test Case Configuration 

|**Test Case**|**Modulation**|**Symbol Rate**|**Payload Length**|
|---|---|---|---|
|RFPHY/RCV/BV-04-C [Blocking<br>Performance, uncoded data at 1 Ms/s]|Standard|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-10-C [Blocking<br>performance at 2 Ms/s]|Standard|2 Ms/s|MAX_RX_LENGTH_2M|
|RFPHY/RCV/BV-16-C [Blocking<br>Performance, uncoded data at 1 Ms/s,<br>Stable Modulation Index]|Stable|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-22-C [Blocking<br>performance at 2 Ms/s, Stable<br>Modulation Index]|Stable|2 Ms/s|MAX_RX_LENGTH_2M|



_Table 4.20: Blocking performance test cases_ 

- Test Procedure 

   1. Two test signals are fed to the IUT input port: 

Wanted signal: 

Modulated carrier, packets transmitted at the mid operating frequency listed in the frequencies for testing (listed in the test condition section of this test case) with PRBS9 payload with Payload Length (specified in Table 4.20). See Section 6.1 and [4], Section 4 for details. Signal level of the wanted signal at the IUT input port is as defined in Table 4.21. 

Blocking signal: 

Sinusoidal, un-modulated carrier transmitted at a blocker frequency of fblocker = 30 MHz. Signal level of the blocker signal at the IUT input port is as defined in Table 4.21. 

2. The PER is measured according to Section 6.3. If the PER exceeds the minimum requirement, the frequency is recorded as fbf_1. 

3. Repeat Steps 1 and 2 for 30 MHz  fblocker  12.75 GHz with the measurement frequency resolution defined in Table 4.21. 

4. fblocker n+1 = fblocker_n + measurement frequency resolution (n=0,1,2…) 

5. The PER measurement is repeated for all recorded frequencies in Step 4 but with -50 dBm blocker level at the IUT input ports. If the PER exceeds the minimum requirement, the frequency is recorded as fbf_2. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **47 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [377 x 160] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tester implementation<br>Un-modulated carrier Signal generator<br>(Frequency of operation  Blocker level + Lt<br>Interferer and output power as  Isolator<br>listed in Table 4.14) Power combiner Counter incremented for<br>11 each packet received.<br>Dout<br>Isolator  IUT<br>2<br>Bluetooth LE modulation  Signal generator<br>Wanted  PRBS9 -67dBm + Lt<br>signal (Frequency of operation<br>2426MHz)<br>Cable, Isolator, circulator<br>and power combiner<br>attenuation<br>Lt<br>**----- End of picture text -----**<br>


_Figure 4.22: Blocking performance test setup_ 

|**Interference signal**<br>**frequency**|**Wanted signal level**<br>**at IUT input port**|**Blocking signal**<br>**level at IUT input**<br>**port**|**Measurement**<br>**frequency**<br>**resolution**|
|---|---|---|---|
|**30 – 2000 MHz**|-67 dBm|-30 dBm|10 MHz|
|**2003 – 2399 MHz**|-67 dBm|-35 dBm|3 MHz|
|**2484 – 2997 MHz**|-67 dBm|-35 dBm|3 MHz|
|**3000 MHz – 12.75 GHz**|-67 dBm|-30 dBm|25 MHz|



_Table 4.21: Out-of-band blocking performance and measurement parameters_ 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|
|All||2426 MHz(n=12)||



- Expected Outcome 

## Pass verdict 

All measured values fulfill the following condition: 

PER < **30.8%** for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is 37 bytes. 

PER < the value calculated according to the formula specified in Section 6.3.1 for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is > 37 bytes. 

The number of fbf_1 frequencies recorded in Step 2 do not exceed 10, and the number of fbf_2 frequencies recorded in Step 5 do not exceed 3. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **48 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4.7.4 Intermodulation Performance** 

- Test Purpose 

Verify that the receiver intermodulation performance is satisfactory. 

- Reference 

[2] Chapter 4.4 

   - [6] Chapter 4.4 

- Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The value of MAX_RX_LENGTH and MAX_RX_LENGTH_2M (for which the TC is performed) is specified in Section 6.6. 

   - The IUT is set for a symbol rate as specified in Table 4.22. 

   - The IUT is set to assume the transmitter has a standard modulation index or stable modulation index (specified in Table 4.22). 

- Test Case Configuration 

|**Test Case**|**Modulation**|**Symbol Rate**|**Payload Length**|
|---|---|---|---|
|RFPHY/RCV/BV-05-C [Intermodulation<br>Performance, uncoded data at 1 Ms/s]|Standard|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-11-C [Intermodulation<br>performance at 2 Ms/s]|Standard|2 Ms/s|MAX_RX_LENGTH_2M|
|RFPHY/RCV/BV-17-C [Intermodulation<br>Performance, uncoded data at 1 Ms/s,<br>Stable Modulation Index]|Stable|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-23-C [Intermodulation<br>performance at 2 Ms/s, Stable Modulation<br>Index]|Stable|2 Ms/s|MAX_RX_LENGTH_2M|



_Table 4.22: Intermodulation performance test cases_ 

- Test Procedure 

   1. The IUT is set to receive at the lowest frequency for testing defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case). Three test signals are fed to the IUT input port: 

Wanted signal: 

Modulated carrier, packets transmitted at the receiving frequency (fRX) with octet PRBS9 payload with Payload Length (specified in Table 4.22). Refer to Section 6.1 and [4], Section 4 for details. Signal level of the wanted signal at the IUT input port is -64 dBm. 

Interference signal #1: 

Sinusoidal, un-modulated carrier transmitted at an interferer frequency of f1. Signal level of the interferer signal at the IUT input port is -50 dBm. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **49 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

Interference signal #2: 

Continuous modulated carrier at frequency f2, modulated with PRBS15 data at a symbol rate as specified in Table 4.22. See Section 6.1 and [4] for details of the Bluetooth LE signal, Section 4 for details. Signal level of the interferer signal at the IUT input port is -50 dBm. The frequency relation between the wanted signal and the interferers is as follows: 

fRX = 2 × f1 – f2 and |f2 – f1| = n × 1 MHz for 1 Ms/s symbol rate 

fRX = 2 × f1 – f2 and |f2 – f1| = n × 2 MHz for 2 Ms/s symbol rate 

where n=3, 4, or 5 

Once the frequency configuration is chosen, the PER is measured with the interferers both below _and_ above the receive frequency, covering both cases implied by |f2 - f1|, i.e., the PER is measured twice for each receive frequency. 

Figure 4.24 shows the frequency combination alternatives for the intermodulation test. 

2. The Lower Tester’s transmit power is chosen such that the input power to the IUT receiver is as listed in Step 1. Figure 4.23 illustrates the test setup principle. 

3. The PER is measured according to Section 6.3. 

4. Steps 2 and 3 are repeated when the IUT is receiving at the remaining frequencies defined in the test condition section. 

## _**Tester implementation**_ 

**==> picture [445 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
Signal generator Isolator<br>Bluetooth LE -50dBm + Lt<br>Interferer #2 modulation<br>PRBS15 Power combiner Counter incremented for<br>Signal generator Isolator 1 each packet received.<br>Unmodulated -50dBm + Lt<br>Interferer #1 2 Dout<br>carrier Isolator 50W  IUT<br>3<br>term.<br>4<br>Signal generator<br>Wanted  Bluetooth LE -64dBm + Lt<br>signal modulation<br>PRBS9<br>Cable, Isolator, circulator<br>and power combiner<br>attenuation<br>Lt<br>**----- End of picture text -----**<br>


_Figure 4.23: Test setup for intermodulation test_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **50 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [140 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
Alternative #1 Alternative #2 Alternative #3<br>**----- End of picture text -----**<br>


**==> picture [443 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
Signal power<br>[dBm]<br>fRX-(10k)MHz fRX-(8k)MHz fRX-(6k)MHz fRX-(5k)MHz fRX-(4k)MHz fRX-(3k)MHz<br>-50dBm<br>Unmodulated<br>Bluetooth LE  carrier (f1)<br>modulated signal<br>(f2)<br>Receiving channel<br>fRX<br>-64dBm<br>frequency<br>**----- End of picture text -----**<br>


_Figure 4.24: Test signal allocation alternatives in the frequency domain at symbol rate k (in Ms/s). Note: figure shows only frequencies below f0._ 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- 

- Expected Outcome 

## Pass verdict 

The measured values fulfill the following condition: 

PER < **30.8%** for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is 37 bytes. 

PER < the value calculated according to the formula specified in Section 6.3.1 for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is > 37 bytes. 

The value of n (for which the TC is performed) is declared by the manufacturer in the IXIT table [3]. 

## **4.7.5 Maximum input signal level** 

- Test Purpose 

Verify that the receiver is able to demodulate a wanted signal at high signal input levels. 

- Reference 

   - [2] Chapter 4.5 

   - [6] Chapter 4.5 

- Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

- The value of MAX_RX_LENGTH and MAX_RX_LENGTH_2M (for which the TC is performed) is specified in Section 6.6. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **51 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

   - The IUT is set for a symbol rate as specified in Table 4.23. 

   - The IUT is set to assume the transmitter has a standard modulation index or stable modulation index (specified in Table 4.23). 

- Test Case Configuration 

|**Test Case**|**Modulation**|**Symbol Rate**|**Payload Length**|
|---|---|---|---|
|RFPHY/RCV/BV-06-C [Maximum<br>input signal level, uncoded data<br>at 1 Ms/s]|Standard|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-12-C [Maximum<br>input signal level at 2 Ms/s]|Standard|2 Ms/s|MAX_RX_LENGTH_2M|
|RFPHY/RCV/BV-18-C [Maximum<br>input signal level, uncoded data<br>at 1 Ms/s, Stable Modulation<br>Index]|Stable|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-24-C [Maximum<br>input signal level at 2 Ms/s, Stable<br>Modulation Index]|Stable|2 Ms/s|MAX_RX_LENGTH_2M|



_Table 4.23: Maximum input signal level test cases_ 

- Test Procedure 

   1. The IUT is set to receive at the lowest frequency for testing defined in the frequencies for testing applicable to the IUT (listed in the test condition section of this test case). 

   2. The Lower Tester transmits packets with octet PRBS9 payload with Payload Length (specified in Table 4.23). Refer to Section 6.1, “Reference Signal Definition” and [4], Section 4 for details. The signal level at the IUT input port is -10 dBm. 

   3. The PER is measured according to Section 6.3. 

   4. Steps 1–3 are repeated when the IUT is receiving at the remaining frequencies defined in the test condition section. 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- 

- Expected outcome 

## Pass verdict 

All measured values fulfill the following condition: 

PER < **30.8%** for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is 37 bytes. 

PER < the value calculated according to the formula specified in Section 6.3.1 for ≥ **1500** packets transmitted by the Lower Tester if the IUT’s Payload Length is > 37 bytes. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **52 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4.7.6 PER report integrity** 

- Test Purpose 

Verify that the IUT PER report mechanism reports the correct number of received packets to the Lower Tester. 

- Reference 

Section 6.3 

[2] Chapter 2.3 

[6] Chapter 2.3 

- Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The value of MAX_RX_LENGTH, MAX_RX_LENGTH_2M, MAX_RX_LENGTH_CODED_S2, and MAX_RX_LENGTH_CODED_S8 (for which the TC is performed) is specified in Section 6.6. 

   - The IUT is set for a symbol rate as specified in Table 4.24. 

   - The IUT is set to assume the transmitter has a standard modulation index or stable modulation index (specified in Table 4.24). 

- 

## Test Case Configuration 

|**Test Case**|**Modulation**|**Symbol**<br>**Rate**|**Payload Length**|
|---|---|---|---|
|RFPHY/RCV/BV-07-C [PER Report Integrity, uncoded<br>data at 1 Ms/s]|Standard|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-13-C [PER Report Integrity at 2 Ms/s]|Standard|2 Ms/s|MAX_RX_LENGTH_2M|
|RFPHY/RCV/BV-19-C [PER Report Integrity, uncoded<br>data at 1 Ms/s, Stable Modulation Index]|Stable|1 Ms/s|MAX_RX_LENGTH|
|RFPHY/RCV/BV-25-C [PER Report Integrity at 2 Ms/s,<br>Stable Modulation Index]|Stable|2 Ms/s|MAX_RX_LENGTH_2M|
|RFPHY/RCV/BV-30-C [PER Report Integrity, LE<br>Coded (S=2)]|Standard|1 Ms/s<br>coded S=2|MAX_RX_LENGTH_CODED_S2|
|RFPHY/RCV/BV-31-C [PER Report Integrity, LE<br>Coded (S=8)]|Standard|1 Ms/s<br>coded S=8|MAX_RX_LENGTH_CODED_S8|
|RFPHY/RCV/BV-36-C [PER Report Integrity, LE<br>Coded (S=2), Stable Modulation Index]|Stable|1 Ms/s<br>coded S=2|MAX_RX_LENGTH_CODED_S2|
|RFPHY/RCV/BV-37-C [PER Report Integrity, LE<br>Coded (S=8), Stable Modulation Index]|Stable|1 Ms/s<br>coded S=8|MAX_RX_LENGTH_CODED_S8|



_Table 4.24: PER Report Integrity test cases_ 

- Test Procedure 

   1. The IUT is set to receive at the middle frequency for testing defined in the test condition section. 

   2. The Lower Tester transmits packets with octet PRBS9 payload with Payload Length (specified in Table 4.24). Refer to Section 6.1 and [4], Section 4 for details. 

   3. The total number of packets transmitted by the Lower Tester is an even random number in the interval [100  RND  1500]. 

   4. Every alternating packet transmitted by the Lower Tester has an intentionally corrupted CRC value. 

   5. The signal level at the IUT input port is -30 dBm. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **53 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

   6. The PER is measured according to Section 6.3. 

   7. Steps 1–4 are repeated two times (i.e., three PER measurements in total). 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|
|All||2440 MHz(n=19)||



- Expected Outcome 

## Pass verdict 

All measured values fulfill the following condition: 

50%  PER  (50 + P/2)% for each individual measurement (where P is the appropriate PER value taken from Table 6.2). 

## **4.7.7 IQ Samples Coherency, AoD Receiver** 

- Test Purpose 

This test group is for generic use and contains four test cases to verify that the measured relative phase values derived from the I and Q values sampled on an IUT AoD Receiver from a Constant Tone Extension are within specified limits. 

- Reference 

   - [8] Section 5 

   - [9] Section 4.1.7 

- Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The Lower Tester’s transmit power is chosen such that the input power to the IUT receiver is -67 dBm. The Lower Tester does not change its transmit power during the Constant Tone Extension (except during the guard period and the switch slots). 

   - The IUT is set to assume the transmitter has a standard modulation index. 

   - The IUT is set for a symbol rate as specified in Table 4.25. 

   - The rate at which the IUT generates IQ reports (TSPX_IQ_Report_Rate) is defined in the IXIT [5]. 

- Test Case Configuration 

|**Test Case**|**PHY**|**CTE Type (Slot Duration)**|
|---|---|---|
|RFPHY/RCV/IQC/BV-01-C [IQ Samples Coherency,<br>AoD Receiver at 1 Ms/s with 2µs Slot]|1 Ms/s|(0x02) 2 µs|
|RFPHY/RCV/IQC/BV-02-C [IQ Samples Coherency,<br>AoD Receiver at 1 Ms/s with 1µs Slot]|1 Ms/s|(0x01) 1 µs|
|RFPHY/RCV/IQC/BV-03-C [IQ Samples Coherency,<br>AoD Receiver at 2 Ms/s with 2µs Slot]|2 Ms/s|(0x02) 2 µs|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **54 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Test Case**|**PHY**|**CTE Type (Slot Duration)**|
|---|---|---|
|RFPHY/RCV/IQC/BV-04-C [IQ Samples Coherency,<br>AoD Receiver at 2 Ms/s with 1µs Slot]|2 Ms/s|(0x01) 1 µs|



_Table 4.25: IQ Samples Coherency, AoD Receiver test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to receive test packets at the lowest frequency for testing as defined in the frequencies for testing (listed in the test condition section of this test case), with expected CTE length of 20 and expected CTE type as specified in Table 4.25. 

   2. The Lower Tester transmits LE test packets with no PDU payload and with 20 * 8 μs Constant Tone Extension. Antenna switching is executed for each Constant Tone Extension with slot durations as specified in Table 4.25, length of switching pattern and switching pattern set as described in Section 5.2.3 [8] with the number of antenna elements set to 4. See [9] Section 4, “LE Test Packet Definition” for details. 

   3. The Upper Tester expects to receive HCI_LE_Connectionless_IQ_Report events at the rate specified by TSPX_IQ_Report_Rate and calculates the relative phase and reference phase deviation values for each non-reference antenna, as described in Section 5.2.1 [8]. 

   4. The Lower Tester transmits LE test packets until it reaches the maximum number of packets defined in Section 6.7 or until the RP(m) and RPD sets each contain at least 2,000 values. 

   5. Repeat Steps 1–4 until the IUT has received on all the remaining frequencies defined in the test condition section. 

- Test Condition 

The IUT and Lower Tester are set up according to the cabled testing setup described in Section 4.8 and Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**PHY**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|---|
|All|1 Ms/s|2402 MHz(n=0)|2440 MHz(n=19)|2480 MHz(n=39)|
|All|2 Ms/s|2404 MHz(n=1)|2440 MHz(n=19)|2478 MHz(n=38)|



- Expected Outcome 

## Pass verdict 

For each frequency tested, RP(m) and RPD sets contain at least 2,000 valid values each. 

For each frequency tested, the IUT meets the requirements from Section 5.2.2 [8]. 

The presence of invalid IQ samples does not constitute a failure. 

## **4.7.8 IQ Samples Coherency, AoA Receiver** 

- Test Purpose 

This test group is for generic use and contains two test cases to verify that the measured relative phase values derived from the I and Q values sampled on an IUT AoA Receiver from a Constant Tone Extension are within specified limits. 

- Reference 

   - [8] Section 5 

   - [9] Section 4.1.7 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **55 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The Lower Tester’s transmit power is chosen such that the input power to the IUT receiver is -67 dBm. The Lower Tester does not change its transmit power during the Constant Tone Extension (except during the guard period and the switch slots). 

   - The IUT is set to assume the transmitter has a standard modulation index. 

   - The IUT is set for a symbol rate as specified in Table 4.26. 

   - The maximum number of antennae supported by the IUT (TSPX_number_of_antennae) is defined in the IXIT [5]. 

   - The rate at which the IUT generates IQ reports (TSPX_IQ_Report_Rate) is defined in the IXIT [5]. 

- Test Case Configuration 

|**Test Case**|**PHY**|
|---|---|
|RFPHY/RCV/IQC/BV-05-C [IQ Samples Coherency, AoA Receiver at 1 Ms/s with<br>2µs Slot]|1 Ms/s|
|RFPHY/RCV/IQC/BV-06-C [IQ Samples Coherency, AoA Receiver at 2 Ms/s with<br>2µs Slot]|2 Ms/s|



_Table 4.26: IQ Samples Coherency, AoA Receiver test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to receive test packets at the lowest frequency for testing as defined in the frequencies for testing (listed in the test condition section of this test case), with expected CTE length of 20, CTE type of 0x00 (AoA CTE), slot durations of 2 μs, length of switching pattern and the switching pattern set as described in Section 5.2.3 [8] with the number of antenna elements set to the minimum value between 4 and TSPX_number_of_antennae. 

   2. The Lower Tester transmits LE test packets with no PDU payload and with 20 * 8 μs Constant Tone Extension. See [9] Section 4, “LE Test Packet Definition” for details. 

   3. The Upper Tester expects to receive HCI_LE_Connectionless_IQ_Report events at the rate specified by TSPX_IQ_Report_Rate and calculates the relative phase and reference phase deviation values for each non-reference antenna, as described in Section 5.2.1 [8]. 

   4. The Lower Tester transmits LE test packets until it reaches the maximum number of packets defined in Section 6.7 or until the RP(m) and RPD sets each contain at least 2,000 values. 

   5. Repeat Steps 1–4 until the IUT has received on all the remaining frequencies defined in the test condition section. 

- Test Condition 

The IUT and Lower Tester are set up according to the cabled testing setup described in Section 4.8 and Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**PHY**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|---|
|All|1 Ms/s|2402 MHz(n=0)|2440 MHz(n=19)|2480 MHz(n=39)|
|All|2 Ms/s|2404 MHz(n=1)|2440 MHz(n=19)|2478 MHz(n=38)|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **56 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Expected Outcome 

## Pass verdict 

For each frequency tested, RP(m) and RPD sets contain at least 2,000 valid values each. 

For each frequency tested, the IUT meets the requirements from Section 5.2.2 [8]. 

The presence of invalid IQ samples does not constitute a failure. 

## **4.7.9 IQ Samples Dynamic Range, AoD Receiver** 

- Test Purpose 

This test group is for generic use and contains four test cases to verify that the I and Q values sampled on receiving an AoD Constant Tone Extension from a peer device have specified values when varying the dynamic range of the Constant Tone Extension and marks any invalid samples as invalid. 

- Reference 

   - [8] Section 5 

   - [9] Section 4.1.7 

- 

## Initial Condition 

   - The IUT is set to direct RX mode. Dewhitening is turned off. 

   - The IUT is set to assume the transmitter has a standard modulation index. 

   - The IUT is set for a symbol rate as specified in Table 4.27. 

   - Frequency hopping off, fixed frequency. 

   - The rate at which the IUT generates IQ reports (TSPX_IQ_Report_Rate) is defined in the IXIT [5]. 

- 

## Test Case Configuration 

|**Test Case**|**PHY**|**CTE Type (Slot Duration)**|
|---|---|---|
|RFPHY/RCV/IQDR/BV-07-C [IQ Samples Dynamic<br>Range, AoD Receiver at 1 Ms/s with 2µs Slot]|1 Ms/s|(0x02) 2 µs|
|RFPHY/RCV/IQDR/BV-08-C [IQ Samples Dynamic<br>Range, AoD Receiver at 1 Ms/s with 1µs Slot]|1 Ms/s|(0x01) 1 µs|
|RFPHY/RCV/IQDR/BV-09-C [IQ Samples Dynamic<br>Range, AoD Receiver at 2 Ms/s with 2µs Slot]|2 Ms/s|(0x02) 2 µs|
|RFPHY/RCV/IQDR/BV-10-C [IQ Samples Dynamic<br>Range, AoD Receiver at 2 Ms/s with 1µs Slot]|2 Ms/s|(0x01) 1 µs|



_Table 4.27: IQ Samples Dynamic Range, AoD Receiver test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to receive test packets at the lowest frequency for testing as defined in the frequencies for testing (listed in the test condition section of this test case), with expected CTE length of 20 and expected CTE type as specified in Table 4.27. 

   2. The Lower Tester transmits LE test packets with no PDU payload and with 20 * 8 μs Constant Tone Extension. The Lower Tester applies an attenuation on the line while sending the Preamble, preamble, synchronization word, LE test packet PDU, and CRC, such that the input power to the IUT receiver is set to the value described in Table 4.28 for antenna index 0. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **57 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

Antenna switching is executed for each Constant Tone Extension with slot durations as specified in Table 4.27, length of switching pattern and the switching pattern set as described in Section 5.2.3 [8] with the number of antenna elements set to 4. See [9] Section 4, “LE Test Packet Definition” for details. 

3. The Lower Tester controls a variable attenuator that applies an additional attenuation on the line while sending the Constant Tone Extension, such that the input power to the IUT receiver is set to the value described in Table 4.28 for each antenna index. 

4. The Upper Tester expects to receive HCI_LE_Connectionless_IQ_Report events at the rate specified by TSPX_IQ_Report_Rate and calculates amplitude A = sqrt(I[2] + Q[2] ) for each valid sample that was not taken during the reference period. 

5. The Lower Tester transmits LE test packets until it reaches the maximum number of packets defined in Section 6.7 or until the IUT reports at least 2,000 valid IQ sample pairs per antenna, except for antenna index 1. 

6. Repeat Steps 1–5 until the IUT has received on all the remaining frequencies defined in the test condition section. 

|**Antenna Index**|**Input Power (dBm)**|
|---|---|
|0<br>1<br>2<br>3|-52|
||-49|
||-57|
||-62|



_Table 4.28: Input Power values for each antenna index_ 

- Test Condition 

The IUT and Lower Tester are set up according to the cabled testing setup described in Section 4.8 and Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**PHY**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|---|
|All|1 Ms/s|2402 MHz(n=0)|2440 MHz(n=19)|2480 MHz(n=39)|
|All|2 Ms/s|2404 MHz(n=1)|2440 MHz(n=19)|2478 MHz(n=38)|



- Expected Outcome 

## Pass verdict 

For each frequency tested, the mean of amplitudes measured for each Lower Tester antenna index ‘i’ from Table 4.28 follows the equation: 

AmeanANT3 < AmeanANT2 < AmeanANT0 < AmeanANT1 

Should there be no valid samples in the non-reference antenna 1, due to saturation, then the Pass verdict is: 

AmeanANT3 < AmeanANT2 < AmeanANT0 

For each frequency tested, the IUT reports at least 2,000 valid IQ sample pairs per antenna, except for antenna index 1, to the Upper Tester. 

The presence of invalid I or Q samples does not constitute a failure. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **58 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **4.7.10 IQ Samples Dynamic Range, AoA Receiver** 

- Test Purpose 

This test group is for generic use and contains two test cases to verify that the I and Q values sampled on receiving an AoA Constant Tone Extension from a peer device have specified values when varying the dynamic range of the Constant Tone Extension and marks any invalid samples as invalid. 

- Reference 

   - [8] Section 5 

   - [9] Section 4.1.7 

- Initial Condition 

   - The IUT is set to direct RX mode at maximum output power. Whitening is turned off. 

   - Frequency hopping off, fixed frequency. 

   - The IUT is set to assume the transmitter has a standard modulation index. 

   - The IUT is set for a symbol rate as specified in Table 4.29. 

   - The maximum number of antennae supported by the IUT (TSPX_number_of_antennae) and the rate at which the IUT generates IQ reports (TSPX_Report_Rate) are defined in the IXIT [5]. 

- Test Case Configuration 

|**Test Case**|**PHY**|
|---|---|
|RFPHY/RCV/IQDR/BV-11-C [IQ Samples Dynamic Range, AoA Receiver<br>at 1 Ms/s with 2µs Slot]|1 Ms/s|
|RFPHY/RCV/IQDR/BV-12-C [IQ Samples Dynamic Range, AoA Receiver<br>at 2 Ms/s with 2µs Slot]|2 Ms/s|



_Table 4.29: IQ Samples Dynamic Range, AoA Receiver test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to receive test packets at the lowest frequency for testing as defined in the frequencies for testing (listed in the test condition section of this test case), with expected CTE length of 20, CTE type of 0x00 (AoA CTE), slot durations of 0x02 (2 μs), length of switching pattern and the switching pattern set as described in Section 5.2.3 [8] with the number of antenna elements set to the minimum value between 4 and TSPX_number_of_antennae. 

   2. The Lower Tester transmits LE test packets with no PDU payload and with 20 * 8 μs Constant Tone Extension. The Lower Tester applies an attenuation on the line while sending the preamble, synchronization word, LE test packet PDU, and CRC, such that the input power to the IUT receiver is set to the value described in Table 4.30 for antenna index 0. See [9] Section 4, “LE Test Packet Definition” for details. 

   3. The Lower Tester controls a variable attenuator that applies an additional attenuation on the line while sending the Constant Tone Extension, such that the input power to the IUT receiver is set to the value described in Table 4.30 for each antenna index. 

   4. The Upper Tester expects to receive HCI_LE_Connectionless_IQ_Report events at the rate specified by TSPX_IQ_Report_Rate and calculates the amplitude A = sqrt(I[2] + Q[2] ) for each valid sample that was not taken during the reference period. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **59 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

5. The Lower Tester transmits LE test packets until it reaches the maximum number of packets defined in Section 6.7 or until the IUT reports at least 2,000 valid IQ sample pairs per antenna, except for antenna index 1. 

6. Repeat Steps 1–5 until the IUT has received on all the remaining frequencies defined in the test condition section. 

|**Antenna Index**|**Input Power (dBm)**|
|---|---|
|0<br>1<br>2<br>3|-52|
||-49|
||-57|
||-62|



_Table 4.30: Input Power values for each antenna index_ 

- Test Condition 

The IUT and Lower Tester are set up according to the cabled testing setup described in Section 4.8 and Common test case conditions and parameters defined in Section 4.3 apply. 

Frequencies for Testing: 

|**Role**|**PHY**|**IUT Low**|**IUT Mid**|**IUT High**|
|---|---|---|---|---|
|All|1 Ms/s|2402 MHz(n=0)|2440 MHz(n=19)|2480 MHz(n=39)|
|All|2 Ms/s|2404 MHz(n=1)|2440 MHz(n=19)|2478 MHz(n=38)|



- Expected Outcome 

## Pass verdict 

For each frequency tested, the mean of amplitudes measured for each antenna index ‘i’ from Table 4.30 follows the equation: 

AmeanANT3 < AmeanANT2 < AmeanANT0 < AmeanANT1 

Should there be no valid samples in the non-reference antenna 1, due to saturation, then the Pass verdict is: 

**==> picture [123 x 9] intentionally omitted <==**

For each frequency tested, the IUT reports at least 2,000 valid IQ sample pairs per antenna, except for antenna index 1, to the Upper Tester. 

The presence of invalid IQ samples does not constitute a failure. 

## **4.8 Transmitter/Receiver tests (TRM-RCV)** 

## **4.8.1 CS Step Mode-0, Frequency Verification** 

- Test Purpose 

Verify that the IUT’s Fractional Frequency Offset (FFO), and expected transmitted frequencies for Mode-0 transmissions are within limits. 

- Reference 

   - [11] Section 3.5.1 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **60 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- Initial Condition 

   - The Lower Tester is configured as the Initiator and the IUT as the Reflector. 

   - A static Access Address (CS Sync Word) is used for the duration of the test, see Section 4.3.3.1. 

   - A fixed 1:1 antenna configuration is used in the Test Equipment Setup, see Section 4.2.3. 

   - The IUT’s transmitter is set to maximum output power. 

   - The IUT is configured to transmit a fixed sequence of 𝑀 Mode-0 CS steps, where 𝑀 is the maximum number of Mode-0 steps the IUT supports. 

   - The IUT transmitter is configured to transmit a single Main-Mode CS step. This Main-Mode CS step is Mode-1. 

   - The test frequencies used are swept across all available CS channels in a pseudo random manner, as defined in Section 4.3.3.2 (Table 4.5). 

**==> picture [378 x 166] intentionally omitted <==**

_Figure 4.25: Step Mode-0, Reflector signal CFO measurement windows_ 

- Test Case Configuration 

|**TCID**|**PHY**|**Main Mode**<br>**Type**|
|---|---|---|
|RFPHY/TRM-RCV/CS/BV-01-C [Step Mode-0, Frequency<br>Verification, 1 Ms/s]|1 Ms/s|Mode-1|
|RFPHY/TRM-RCV/CS/BV-02-C [Step Mode-0, Frequency<br>Verification, 2 Ms/s]|2 Ms/s|Mode-1|
|RFPHY/TRM-RCV/CS/BV-03-C [Step Mode-0, Frequency<br>Verification, 2 Ms/s, BT = 2.0]|2 Ms/s, BT = 2.0|Mode-1|



_Table 4.31: CS Step Mode-0, Frequency Verification test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to enable the Channel Sounding procedure with: 

      - Role set to Reflector 

      - Mode-0 CS steps set to of 𝑀= 3 steps 

      - Main Mode type set to Mode-1 

      - Main Mode CS steps set to 𝐾= 1 

      - Other parameters as specified in Section 4.3.3 

   2. The Lower Tester sends a Mode-0 transmission to the IUT. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **61 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

   3. The IUT responds with a Mode-0 transmission, which includes the CS_Tone. 

   4. The Lower Tester uses the PHY test filter characteristics as defined in Section 6.9. 

   5. The Lower Tester integrates the FM demodulated signal starting at the center of the first preamble bit to the center of the first bit following the last access address bit, and uses this to calculate the center frequency of the packet 𝑓𝑝𝑘𝑡[𝑘] . 

   6. For each step 𝑘= 1 . . 𝑀 , the Lower Tester measures the average frequency of the CS Tone and records this as 𝐹𝑡𝑜𝑛𝑒[𝑘, 1] . 

   7. Calculate the Fractional Frequency Offset (FFO) for each CS step 𝑘 , 𝐹𝐹𝑂[𝑘] = 

      - 𝐹𝑡𝑜𝑛𝑒[𝑘,1]−𝑓0[𝑘](1+10[−6] 𝐹𝐴𝐸[𝑘]) 

      - 10[6] . ~~,~~ where 𝑘= 1 . . 𝑀 , 𝑓0[𝑘] is nominal carrier frequency of the CS 𝑓0[𝑘](1+10[−6] 𝐹𝐴𝐸[𝑘]) 

      - Channel for step 𝑘 _**,**_ 𝐹𝐴𝐸[𝑘] is fractional frequency offset actuation error for the CS channel used in step k of the IUT. 

   8. Repeat Steps 2–7 for all 𝑀 Mode-0 CS steps within the CS sub-event. 

   9. The Lower Tester sends a Main Mode transmission. 

   10. The IUT responds with a Main Mode transmission. 

   11. Repeat Steps 1–10 to obtain a total of 1,000 Mode-0 CS steps. 

   12. Steps 1–11 are repeated for the PHYs specified in Table 4.31. 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- Expected Outcome 

## Pass verdict 

For every sub-event measured: 

- |𝐹𝐹𝑂[𝑘]| ≤50 ppm , where 𝑘= 1 . . 𝑀 

- |𝐹𝐹𝑂[𝑘] − 𝐹𝐹𝑂[1]| ≤1 ppm , where 𝑘= 2 . . 𝑀 

For all sub-events measured: 

- 95% 𝑜𝑓 𝑎𝑙𝑙 𝑟𝑒𝑐𝑜𝑟𝑑𝑒𝑑 |𝐹𝑡𝑜𝑛𝑒 −𝑓𝑝𝑘𝑡(𝑘)| < 20 𝑘𝐻𝑧, where 𝑘= 2, … , 𝑀 

## **4.8.2 CS Step Main Mode, Frequency Verification** 

- Test Purpose 

Verify that the average frequency of each of the IUT’s Main Mode transmissions within the CS subevent are aligned with the initial FFO measurement. 

- Reference 

   - [11] Section 3.5.2, 4.5 

- Initial Condition 

   - The Lower Tester is configured as the Initiator and the IUT as the Reflector. 

   - A static Access Address (CS Sync Word) is used for the duration of the test, see Section 4.3.3.1. 

   - The maximum value of N_AP supported by the IUT is used in the Test Equipment Setup, see Section 4.2.3. 

   - The IUT’s transmitter is set to maximum output power. 

   - The IUT is configured to transmit a fixed sequence of 𝑀 Mode-0 CS steps, where 𝑀 is the maximum number of Mode-0 steps the IUT supports. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **62 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

   - Tone extension is set to disabled. 

   - The transmit frequency for the entire CS subevent is fixed at 𝑓0 , (Section 4.3.2). 

- Test Case Configuration 

|**TCID**|**PHY**|**Main Mode**<br>**Type**|
|---|---|---|
|RFPHY/TRM-RCV/CS/BV-04-C [Step Main Mode,<br>FrequencyVerification, 1 Ms/s, Mode-1]|1 Ms/s|Mode-1|
|RFPHY/TRM-RCV/CS/BV-05-C [Step Main Mode,<br>FrequencyVerification, 1 Ms/s, Mode-2]|1 Ms/s|Mode-2|
|RFPHY/TRM-RCV/CS/BV-06-C [Step Main Mode,<br>FrequencyVerification, 1 Ms/s, Mode-3]|1 Ms/s|Mode-3|
|RFPHY/TRM-RCV/CS/BV-07-C [Step Main Mode,<br>FrequencyVerification, 2 Ms/s, Mode-1]|2 Ms/s|Mode-1|
|RFPHY/TRM-RCV/CS/BV-08-C [Step Main Mode,<br>FrequencyVerification, 2 Ms/s, Mode-3]|2 Ms/s|Mode-3|
|RFPHY/TRM-RCV/CS/BV-09-C [Step Main Mode,<br>FrequencyVerification, 2 Ms/s, BT = 2.0, Mode-1]|2 Ms/s, BT = 2.0|Mode-1|
|RFPHY/TRM-RCV/CS/BV-10-C [Step Main Mode,<br>FrequencyVerification, 2 Ms/s, BT = 2.0, Mode-3]|2 Ms/s, BT = 2.0|Mode-3|



_Table 4.32: CS Step Main Mode, Frequency Verification test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to enable the Channel Sounding procedure with: 

      - Role set to Reflector 

      - Mode-0 CS Steps set to of 𝑀 = 3 steps, where 𝑀 is the maximum number of Mode-0 steps the IUT supports 

      - Main Mode CS steps set to 1 ≤𝐾 ≤72 

      - Lowest frequency for testing as defined in Section 4.3.2 

      - Other parameters as specified in Section 4.3.3 

   2. The IUT sends a Mode-0 transmission to the Lower Tester. 

   3. The Lower Tester responds with a Mode-0 transmission. 

   4. The 𝐹𝐹𝑂 of first Mode-0 transmission, 𝐹𝐹𝑂[1] , is measured according to Section 4.8.1. For each CS sub-event used in the measurement, 𝐹𝐹𝑂𝐸 =  𝐹𝐹𝑂[1] . 

   5. For each CS step, calculate the expected carrier frequency 𝑓𝐸[𝑘] = 𝑓0 [𝑘](1 + 10[−6] 𝐹𝐹𝑂𝐸 ) . 

   6. Perform alternative 6a, 6b, or 6c depending on the Main Mode type and PHY specified in Table 4.32. 

## Alternative 6a [Mode-1]: 

- 6a.1 The Lower Tester sends a Mode-1 transmission (CS_SYNC_1) to the IUT. 

- 6a.2 The IUT replies with a Mode-1 transmission (CS_SYNC_1) to the Lower Tester. 

- 6a.3 The Lower Tester integrates the FM demodulated signal of the IUT’s CS_SYNC_1 packet starting from the center of the first preamble bit to the center of the first bit following the last access address bit. The Lower Tester uses this to calculate the center frequency of the packet 𝑓𝑝𝑘𝑡[𝑘] , see Figure 4.26. 

- 6a.4 Repeat Steps 6a.1–6a.3 for all Mode-1 transmissions within the CS sub-event. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **63 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

**==> picture [234 x 186] intentionally omitted <==**

_Figure 4.26: Step Main Mode-1, Reflector signal CFO measurement window_ 

## Alternative 6b [Mode-2]: 

- 6b.1 The Lower Tester sends a Mode-2 transmission (CS_Tone) to the IUT. 

- 6b.2 The IUT replies with a Mode-2 transmission (CS_Tone) to the Lower Tester. 

- 6b.3 The Lower Tester performs 𝑓𝑡𝑜𝑛𝑒[𝑘, 𝑝] measurements on the CS_Tone packet portion for duration T_PM per antenna, on Step k, and antenna path p, see Figure 4.27. Refer to [11] Volume 6, Part H: Section 4.5 ‘Timing of Steps’. 

- 6b.4 Repeat Steps 6b.1–6b.3 for all Mode-2 transmissions within the CS sub-event. 

**==> picture [378 x 239] intentionally omitted <==**

_Figure 4.27: Step Main Mode-2, Reflector signal CS tone measurement window_ 

## Alternative 6c [Mode-3]: 

- 6c.1 The Lower Tester sends a Mode-3 transmission (CS_SYNC_3 + CS_Tone) to the IUT. 

- 6c.2 The IUT replies with a Mode-3 transmission (CS_Tone + CS_SYNC_3) to the Lower Tester. 

- 6c.3 The Lower Tester performs 𝑓𝑡𝑜𝑛𝑒[𝑘, 𝑝] measurements on the CS_Tone packet portion for duration T_PM per antenna, on Step k, and antenna path p. In addition, 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **64 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

the Lower Tester integrates the FM demodulated signal of the IUT’s CS_SYNC_3 packet starting from the center of the first preamble bit to the center of the first bit following the last access address bit and uses this to calculate the center frequency of the packet 𝑓𝑝𝑘𝑡[𝑘] , see Figure 4.28. Refer to [11] Volume 6, Part H: Section 4.5 ‘Timing of Steps’. 

- 6c.4 Repeat Steps 6c.1–6c.3 for all Mode-3 transmissions within the CS sub-event. 

**==> picture [378 x 152] intentionally omitted <==**

_Figure 4.28: Step Main Mode-3, Reflector signal CFO and Ftone measurement windows_ 

   7. Repeat Steps 1–6 to obtain a total of 1,000 Main-Mode CS steps. 

- 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- Expected Outcome 

Pass verdict 

For every CS sub-event measured, in the case of: 

- Mode-1 and Mode-3 CS steps: 

   - 95% 𝑜𝑓 𝑎𝑙𝑙 𝑚𝑒𝑎𝑠𝑢𝑟𝑒𝑚𝑒𝑛𝑡𝑠: | 𝑓𝐸[𝑘] −𝑓𝑝𝑘𝑡[𝑘]| < 20 kHz 

- Mode-2 and Mode-3 CS steps: 

   - 95% 𝑜𝑓 𝑎𝑙𝑙 𝑚𝑒𝑎𝑠𝑢𝑟𝑒𝑚𝑒𝑛𝑡𝑠: | 𝑓𝐸[𝑘] −𝑓𝑡𝑜𝑛𝑒[𝑘, 𝑝]| < 10 kHz 

## **4.8.3 CS Phase Measurement Accuracy** 

- Test Purpose 

Verify that the IUT’s phase measurement accuracy is within acceptable limits during the phase measurement period for CS tone exchanges. 

- Reference 

   - [11] Section 6.1, 6.2, 6.4 

- Initial Condition 

   - The Lower Tester and the IUT are configured as specified in Table 4.34. 

   - A static Access Address (CS Sync Word) is used for the duration of the test, see Section 4.3.3.1. 

   - The IUT’s transmitter is set to maximum output power. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **65 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

- The number of CS antennae (N_AP) in the IUT is defined by the TSPX_number_of_cs_antennae IXIT value. 

- The maximum supported CS antenna path is defined by the TSPX_cs_max_antenna_path IXIT value. 

- The value of N_AP is defined in Table 4.33 based on the Role and Antenna Configuration in Table 4.34. 

|**Role**|**Antenna Configuration**|**N_AP**|
|---|---|---|
|Reflector|N_AP:1|TSPX_cs_max_antenna_path|
|Reflector|1:N_AP|TSPX_number_of_cs_antennae|
|Reflector|2:2|4|
|Initiator|1:N_AP|TSPX_cs_max_antenna_path|
|Initiator|N_AP:1|TSPX_number_of_cs_antennae|
|Initiator|2:2|4|



_Table 4.33: Antenna Configuration_ 

   - The Lower Tester is configured to transmit a fixed sequence of 𝑀 Mode-0 CS steps, where 𝑀 is the minimum number of Mode-0 steps the IUT supports. 

   - The Lower Tester’s transmit power is adjusted such that the input power to the IUT receiver is −70 𝑑𝐵𝑚 . 

   - The test frequencies used are swept across all available CS channels in a pseudo random manner, as defined in Section 4.3.3.2. 

   - The FFO of the Lower Tester, as applied to the RF frequencies and the symbol and link layer timing, is set to 50 ppm. This value is initialized to 0 ppm for the first pass of the test procedure. 

   - The electrical length from the center point of the resistive splitter through to the IUT’s antenna connector is predetermined (measured) at each RF channel center frequency. The value of this parameter is used as an offset (to calibrate out the test up) for every RF channel tested during the measurement procedure. This step relocates the test setups reference plane shown in Figure 4.3 (as being at the center of the resistive splitter) to the antenna connector of the IUT. 

- Test Case Configuration 

|**TCID**|**PHY/Role**|**Main Mode**<br>**Type**|**Antenna**<br>**Configuration**|
|---|---|---|---|
|RFPHY/TRM-RCV/CS/BV-11-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-2,<br>Reflector, N_AP:1]|1 Ms/s<br>Reflector|Mode-2|N_AP:1|
|RFPHY/TRM-RCV/CS/BV-19-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-2,<br>Reflector, 1:N_AP]|1 Ms/s<br>Reflector|Mode-2|1:N_AP|
|RFPHY/TRM-RCV/CS/BV-20-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-2,<br>Reflector, 2:2]|1 Ms/s<br>Reflector|Mode-2|2:2|
|RFPHY/TRM-RCV/CS/BV-12-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-3,<br>Reflector, N_AP:1]|1 Ms/s<br>Reflector|Mode-3|N_AP:1|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **66 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**TCID**|**PHY/Role**|**Main Mode**<br>**Type**|**Antenna**<br>**Configuration**|
|---|---|---|---|
|RFPHY/TRM-RCV/CS/BV-21-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-3,<br>Reflector, 1:N_AP]|1 Ms/s<br>Reflector|Mode-3|1:N_AP|
|RFPHY/TRM-RCV/CS/BV-22-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-3,<br>Reflector, 2:2]|1 Ms/s<br>Reflector|Mode-3|2:2|
|RFPHY/TRM-RCV/CS/BV-13-C [Phase<br>Measurement Accuracy, 2 Ms/s, Mode-3,<br>Reflector, N_AP:1]|2 Ms/s<br>Reflector|Mode-3|N_AP:1|
|RFPHY/TRM-RCV/CS/BV-23-C [Phase<br>Measurement Accuracy, 2 Ms/s, Mode-3,<br>Reflector, 1:N_AP]|2 Ms/s<br>Reflector|Mode-3|1:N_AP|
|RFPHY/TRM-RCV/CS/BV-24-C [Phase<br>Measurement Accuracy, 2 Ms/s, Mode-3,<br>Reflector, 2:2]|2 Ms/s<br>Reflector|Mode-3|2:2|
|RFPHY/TRM-RCV/CS/BV-14-C [Phase<br>Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-<br>3, Reflector, N_AP:1]|2 Ms/s, BT =<br>2.0<br>Reflector|Mode-3|N_AP:1|
|RFPHY/TRM-RCV/CS/BV-25-C [Phase<br>Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-<br>3, Reflector, 1:N_AP]|2 Ms/s, BT =<br>2.0<br>Reflector|Mode-3|1:N_AP|
|RFPHY/TRM-RCV/CS/BV-26-C [Phase<br>Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-<br>3, Reflector, 2:2]|2 Ms/s, BT =<br>2.0<br>Reflector|Mode-3|2:2|
|RFPHY/TRM-RCV/CS/BV-15-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-2, Initiator,<br>N_AP:1]|1 Ms/s<br>Initiator|Mode-2|N_AP:1|
|RFPHY/TRM-RCV/CS/BV-27-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-2, Initiator,<br>1:N_AP]|1 Ms/s<br>Initiator|Mode-2|1:N_AP|
|RFPHY/TRM-RCV/CS/BV-28-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-2, Initiator,<br>2:2]|1 Ms/s<br>Initiator|Mode-2|2:2|
|RFPHY/TRM-RCV/CS/BV-16-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-3, Initiator,<br>N_AP:1]|1 Ms/s<br>Initiator|Mode-3|N_AP:1|
|RFPHY/TRM-RCV/CS/BV-29-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-3, Initiator,<br>1:N_AP]|1 Ms/s<br>Initiator|Mode-3|1:N_AP|
|RFPHY/TRM-RCV/CS/BV-30-C [Phase<br>Measurement Accuracy, 1 Ms/s, Mode-3, Initiator,<br>2:2]|1 Ms/s<br>Initiator|Mode-3|2:2|
|RFPHY/TRM-RCV/CS/BV-17-C [Phase<br>Measurement Accuracy, 2 Ms/s, Mode-3, Initiator,<br>N_AP:1]|2 Ms/s<br>Initiator|Mode-3|N_AP:1|
|RFPHY/TRM-RCV/CS/BV-31-C [Phase<br>Measurement Accuracy, 2 Ms/s, Mode-3, Initiator,<br>1:N_AP]|2 Ms/s<br>Initiator|Mode-3|1:N_AP|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **67 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**TCID**|**PHY/Role**|**Main Mode**<br>**Type**|**Antenna**<br>**Configuration**|
|---|---|---|---|
|RFPHY/TRM-RCV/CS/BV-32-C [Phase<br>Measurement Accuracy, 2 Ms/s, Mode-3, Initiator,<br>2:2]|2 Ms/s<br>Initiator|Mode-3|2:2|
|RFPHY/TRM-RCV/CS/BV-18-C [Phase<br>Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-<br>3, Initiator, N_AP:1]|2 Ms/s, BT =<br>2.0<br>Initiator|Mode-3|N_AP:1|
|RFPHY/TRM-RCV/CS/BV-33-C [Phase<br>Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-<br>3, Initiator, 1:N_AP]|2 Ms/s, BT =<br>2.0<br>Initiator|Mode-3|1:N_AP|
|RFPHY/TRM-RCV/CS/BV-34-C [Phase<br>Measurement Accuracy, 2 Ms/s, BT = 2.0, Mode-<br>3, Initiator, 2:2]|2 Ms/s, BT =<br>2.0<br>Initiator|Mode-3|2:2|



_Table 4.34: CS Phase Measurement Accuracy test cases_ 

- Test Procedure 

   1. The Upper Tester commands the IUT to enable the Channel Sounding procedure with: 

      - Role set as specified in Table 4.3 

      - Mode-0 CS Steps set to 𝑀= 1 step 

      - Main Mode CS steps 𝐾 set to 72 (all available CS channels) 

      - Other parameters as specified in Section 4.3.3 

   2. The Lower Tester uses the relevant PHY test filter characteristics as defined in Section 6.9. 

   3. The Lower Tester and the IUT exchange Mode-0 transmissions. 

   4. The 𝐹𝐹𝑂 of first Mode-0 transmission, 𝐹𝐹𝑂[1] , is measured according to Section 4.8.1. For each CS sub-event used in the measurement, 𝐹𝐹𝑂𝐸 =  𝐹𝐹𝑂[1] . If the Role is Initiator, this is measured on the Lower Tester’s Mode-0 tone. 

   5. Main-Mode CS steps are exchanged between the Lower Tester and the IUT. The initiator adjusts the timing and frequency of its CS_SYNC packet, refer to [13] Section 4.5 ‘Timing of steps’ and [11] Section 3.5 ‘Frequency measurement and generation in Channel Sounding’. For each Main-Mode CS step, calculate the expected carrier frequency 𝑓𝐸[𝑘] = 𝑓0 [𝑘](1 + 10[−6] 𝐹𝐹𝑂𝐸 ) . 

   6. For each Main-Mode step, the Lower Tester down converts the signals by 𝑓𝐸 [𝑘] , sent by the Lower Tester and the IUT. See [11] Section 6.1. 

   7. For each phase measurement period, excluding the tone extension slot, within each Main-Mode step, the Lower Tester measures the average phase (see [11] Section 6.2) sent by the Lower Tester during the IUT’s valid region (see [11] Section 6.4) and references this to the IUT’s antenna port. Denote this value as 𝜑𝑅𝑋[𝑘, 𝑝] , where p is the antenna pair. 

   8. For each phase measurement period, excluding the tone extension slot, within each Main-Mode step, the Lower Tester measures the average phase (see [11] Section 6.2) sent by the IUT during the Lower Tester’s valid region (see [11] Section 6.4) and references this to the IUT’s antenna port. Denote this value as 𝜑𝑇𝑋[𝑘, 𝑝] , where p is the antenna pair. 

   9. The Lower Tester obtains the PCT [𝑘, 𝑝] parameters reported by the IUT from the LE CS Subevent Result event. 

   10. The Upper Tester calculates the internal phase offset 𝜃𝐶[𝑘, 𝑝] using the measured values of 𝜑𝑅𝑋[𝑘, 𝑝], 𝜑𝑇𝑋[𝑘, 𝑝] as well as the value of PCT [𝑘, 𝑝] reported by the IUT. 

   11. For each antenna pair p, the Upper Tester calculates the linear regression parameters 𝛼[𝑝] and 𝛽[𝑝] as described in [11] Section 6.2. Values of 𝜃𝑐, 𝑢𝑤[𝑘, 𝑝] are only used in the calculation of the linear regression when the value of the Tone_Quality_Indicator[k] is the highest quality that the IUT supports. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **68 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

   12. Repeat Steps 1–11 139 times in order to obtain a total of 10,000 values of 𝜃𝑐, 𝑢𝑤[𝑘, 𝑝] . 

   13. Repeat Steps 1–12 for Lower Tester FFO values of –50 ppm and 50 ppm. 

- Test Condition 

Common test case conditions and parameters defined in Section 4.3 apply. 

- Expected Outcome 

## Pass verdict 

For each antenna pair, the solution to the linear regression satisfies: 

- For 95% of CS sub-events: 

   - |𝛼[𝑝]| < 2𝜋 × 1.7 ns 

## and 

- for 95% of the values of 𝜃𝑐[𝑘, 𝑝] within each CS sub-event: 

   - |𝑝𝑟𝑖𝑛𝑐𝑖𝑝𝑎𝑙(𝛼[𝑝]𝑓𝐸[𝑘] + 𝛽[𝑝] −𝜃𝑐, 𝑢𝑤[𝑘, 𝑝])| < 0.28 rad 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **69 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **5 Test case ma in pp g** 

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document. 

The columns for the TCMT are defined as follows: 

**Item:** Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for RFPHY [3]. 

If a test case is mandatory within the respective layer, then the y/x reference is omitted. 

**Feature:** A brief, informal description of the feature being tested. 

**Test Case(s):** The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [1]. 

For the purpose and structure of the ICS/IXIT, refer to [1]. 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|RFPHY1/1 OR<br>RFPHY1/3|Transmitter functionality|RFPHY/TRM/BV-03-C<br>RFPHY/TRM/BV-05-C<br>RFPHY/TRM/BV-06-C|
|(RFPHY 1/1 OR<br>RFPHY 1/3) AND<br>NOT RFPHY 1/15|Transmitter functionality, not Power Class 1|RFPHY/TRM/BV-01-C|
|RFPHY 1/15|Transmitter functionality, Power Class 1|RFPHY/TRM/BV-18-C|
|RFPHY 1/8 AND<br>NOT RFPHY 1/15|Transmitting Constant Tone Extensions, not<br>Power Class 1|RFPHY/TRM/BV-15-C|
|RFPHY1/8|TransmittingConstant Tone Extensions|RFPHY/TRM/BV-16-C|
|RFPHY 1/8 AND<br>RFPHY 1/15|Transmitting Constant Tone Extensions,<br>Power Class 1|RFPHY/TRM/BV-21-C|
|(RFPHY 1/1 OR<br>RFPHY 1/3) AND<br>RFPHY 1/4 AND<br>NOT RFPHY 1/15|Transmitter functionality, not Power Class 1<br>LE 2M PHY|RFPHY/TRM/BV-19-C|
|RFPHY 1/4 AND<br>RFPHY 1/15|Transmitter functionality, Power Class 1<br>LE 2M PHY|RFPHY/TRM/BV-20-C|
|RFPHY 1/4 AND<br>RFPHY 1/8 AND<br>NOT RFPHY 1/15|Transmitting Constant Tone Extensions, not<br>Power Class 1<br>LE 2M PHY|RFPHY/TRM/BV-22-C|
|RFPHY 1/4 AND<br>RFPHY 1/8 AND<br>RFPHY 1/15|Transmitting Constant Tone Extensions,<br>Power Class 1<br>LE 2M PHY|RFPHY/TRM/BV-23-C|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **70 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|RFPHY1/2 OR<br>RFPHY1/3|Receiver functionality|RFPHY/RCV/BV-01-C<br>RFPHY/RCV/BV-03-C<br>RFPHY/RCV/BV-04-C<br>RFPHY/RCV/BV-05-C<br>RFPHY/RCV/BV-06-C<br>RFPHY/RCV/BV-07-C|
|(RFPHY 1/1 OR<br>RFPHY 1/3) AND<br>RFPHY1/4|Transmitterfunctionality<br>LE2M PHY|RFPHY/TRM/BV-08-C<br>RFPHY/TRM/BV-10-C<br>RFPHY/TRM/BV-12-C|
|(RFPHY 1/2 OR<br>RFPHY 1/3) AND<br>RFPHY 1/4|Receiver functionality,<br>LE 2M PHY|RFPHY/RCV/BV-08-C<br>RFPHY/RCV/BV-09-C<br>RFPHY/RCV/BV-10-C<br>RFPHY/RCV/BV-11-C<br>RFPHY/RCV/BV-12-C<br>RFPHY/RCV/BV-13-C|
|RFPHY 1/4 AND<br>RFPHY1/8|LE 2M PHY,<br>TransmittingConstant Tone Extensions|RFPHY/TRM/BV-17-C|
|RFPHY1/4 AND<br>RFPHY1/5|LE2M PHY,<br>Stable Modulation Index- Transmitter|RFPHY/TRM/BV-11-C|
|RFPHY1/4 AND<br>RFPHY1/6|LE 2M PHY.<br>Stable Modulation Index - Receiver|RFPHY/RCV/BV-20-C<br>RFPHY/RCV/BV-21-C<br>RFPHY/RCV/BV-22-C<br>RFPHY/RCV/BV-23-C<br>RFPHY/RCV/BV-24-C<br>RFPHY/RCV/BV-25-C|
|RFPHY1/5|Stable Modulation Index - Transmitter|RFPHY/TRM/BV-09-C|
|RFPHY1/6|Stable Modulation Index - Receiver|RFPHY/RCV/BV-14-C<br>RFPHY/RCV/BV-15-C<br>RFPHY/RCV/BV-16-C<br>RFPHY/RCV/BV-17-C<br>RFPHY/RCV/BV-18-C<br>RFPHY/RCV/BV-19-C|
|(RFPHY1/2 OR<br>RFPHY 1/3) AND<br>RFPHY1/7|Receiver Functionality,<br>LE Coded PHY|RFPHY/RCV/BV-26-C<br>RFPHY/RCV/BV-27-C<br>RFPHY/RCV/BV-28-C<br>RFPHY/RCV/BV-29-C<br>RFPHY/RCV/BV-30-C<br>RFPHY/RCV/BV-31-C|
|(RFPHY1/1 OR<br>RFPHY 1/3) AND<br>RFPHY1/7|Transmitter Functionality,<br>LE Coded PHY|RFPHY/TRM/BV-13-C<br>RFPHY/TRM/BV-14-C|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **71 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|RFPHY1/6 AND<br>RFPHY1/7|Stable Modulation Index - Receiver,<br>LE Coded PHY|RFPHY/RCV/BV-32-C<br>RFPHY/RCV/BV-33-C<br>RFPHY/RCV/BV-34-C<br>RFPHY/RCV/BV-35-C<br>RFPHY/RCV/BV-36-C<br>RFPHY/RCV/BV-37-C|
|RFPHY 1/11 AND<br>NOT RFPHY 1/12|2 µs Antenna Sampling During Constant Tone<br>Extension Reception (AoD)|RFPHY/RCV/IQC/BV-01-C<br>RFPHY/RCV/IQDR/BV-07-C|
|RFPHY 1/4 AND<br>RFPHY 1/11 AND<br>NOT RFPHY 1/12|LE 2M PHY,<br>2 µs Antenna Sampling During Constant Tone<br>Extension Reception(AoD)for 2 Ms/s PHY|RFPHY/RCV/IQC/BV-03-C<br>RFPHY/RCV/IQDR/BV-09-C|
|RFPHY1/13 AND<br>NOT RFPHY 1/14|1 µs Antenna Sampling During Constant Tone<br>Extension Reception (AoD)|RFPHY/RCV/IQC/BV-02-C<br>RFPHY/RCV/IQDR/BV-08-C|
|RFPHY 1/4 AND<br>RFPHY 1/13 AND<br>NOT RFPHY 1/14|LE 2M PHY,<br>1 µs Antenna Sampling During Constant Tone<br>Extension Reception(AoD)for 2 Ms/s PHY|RFPHY/RCV/IQC/BV-04-C<br>RFPHY/RCV/IQDR/BV-10-C|
|RFPHY1/12|2 µs Antenna Switching and Sampling During<br>Constant Tone Extension Reception (AoA)|RFPHY/RCV/IQC/BV-05-C<br>RFPHY/RCV/IQDR/BV-11-C|
|RFPHY 1/4 AND<br>RFPHY 1/12|LE 2M PHY,<br>2 µs Antenna Switching and Sampling During<br>Constant Tone Extension Reception (AoA) for<br>2 Ms/s PHY|RFPHY/RCV/IQC/BV-06-C<br>RFPHY/RCV/IQDR/BV-12-C|
|RFPHY1/9|2 µs Antenna Switching During Constant<br>Tone Extension Transmission (AoD)|RFPHY/TRM/PS/BV-01-C<br>RFPHY/TRM/ASI/BV-05-C|
|RFPHY 1/4 AND<br>RFPHY 1/9|LE 2M PHY,<br>2 µs Antenna Switching During Constant<br>Tone Extension Transmission (AoD) for 2<br>Ms/s PHY|RFPHY/TRM/PS/BV-03-C<br>RFPHY/TRM/ASI/BV-07-C|
|RFPHY 1/10|1 µs Antenna Switching During Constant<br>Tone Extension Transmission (AoD)|RFPHY/TRM/PS/BV-02-C<br>RFPHY/TRM/ASI/BV-06-C|
|RFPHY 1/4 AND<br>RFPHY 1/10|LE 2M PHY,<br>1 µs Antenna Switching During Constant<br>Tone Extension Transmission (AoD) for 2<br>Ms/s PHY|RFPHY/TRM/PS/BV-04-C<br>RFPHY/TRM/ASI/BV-08-C|
|**Channel Sounding**|||
|RFPHY 1/16|Channel Sounding, Transmitter, LE 1M|RFPHY/TRM/CS/BV-01-C|
|RFPHY 1/16 AND<br>RFPHY 3/10|Channel Sounding, Transmitter, LE 2M|RFPHY/TRM/CS/BV-02-C|
|RFPHY 3/9|Channel Sounding, Transmitter, LE 2M 2BT|RFPHY/TRM/CS/BV-03-C|
|RFPHY 3/7 AND<br>RFPHY 3/9|Channel Sounding, Transmitter, LE 2M 2BT,<br>Mode-3|RFPHY/TRM/CS/BV-04-C|
|RFPHY 1/16 AND<br>RFPHY 3/2|Channel Sounding, Transmitter-Receiver, LE<br>1M|RFPHY/TRM-RCV/CS/BV-01-C<br>RFPHY/TRM-RCV/CS/BV-04-C|
|RFPHY 3/2 AND<br>RFPHY 3/6|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-2|RFPHY/TRM-RCV/CS/BV-05-C|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **72 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|RFPHY 3/2 AND<br>RFPHY 3/7|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-3|RFPHY/TRM-RCV/CS/BV-06-C|
|RFPHY 1/16 AND<br>RFPHY 3/10|Channel Sounding, Transmitter-Receiver, LE<br>2M|RFPHY/TRM-RCV/CS/BV-02-C<br>RFPHY/TRM-RCV/CS/BV-07-C|
|RFPHY 3/7 AND<br>RFPHY 3/10|Channel Sounding, Transmitter-Receiver, LE<br>2M, Mode-3|RFPHY/TRM-RCV/CS/BV-08-C|
|RFPHY 3/9|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT|RFPHY/TRM-RCV/CS/BV-03-C<br>RFPHY/TRM-RCV/CS/BV-09-C|
|RFPHY 3/7 AND<br>RFPHY 3/9|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT, Mode-3|RFPHY/TRM-RCV/CS/BV-10-C|
|RFPHY 3/2 AND<br>RFPHY 3/6|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-2, Reflector|RFPHY/TRM-RCV/CS/BV-11-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/6 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-2, Reflector, CS Antenna Array|RFPHY/TRM-RCV/CS/BV-19-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/3a AND<br>RFPHY 3/6|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-2, Reflector, 2:2|RFPHY/TRM-RCV/CS/BV-20-C|
|RFPHY 3/2 AND<br>RFPHY 3/7|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-3, Reflector|RFPHY/TRM-RCV/CS/BV-12-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/7 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-3, Reflector, CS Antenna Array|RFPHY/TRM-RCV/CS/BV-21-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/3a AND<br>RFPHY 3/7|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-3, Reflector, 2:2|RFPHY/TRM-RCV/CS/BV-22-C|
|RFPHY 3/2 AND<br>RFPHY 3/7 AND<br>RFPHY 3/10|Channel Sounding, Transmitter-Receiver, LE<br>2M, Mode-3, Reflector|RFPHY/TRM-RCV/CS/BV-13-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/7 AND<br>RFPHY 3/10 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>2M, Mode-3, Reflector, CS Antenna Array|RFPHY/TRM-RCV/CS/BV-23-C|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **73 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/3a AND<br>RFPHY 3/7 AND<br>RFPHY 3/10|Channel Sounding, Transmitter-Receiver, LE<br>2M, Mode-3, Reflector: 2:2|RFPHY/TRM-RCV/CS/BV-24-C|
|RFPHY 3/2 AND<br>RFPHY 3/7 AND<br>RFPHY 3/9|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT, Mode-3, Reflector|RFPHY/TRM-RCV/CS/BV-14-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/7 AND<br>RFPHY 3/9 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT, Mode-3, Reflector, CS Antenna<br>Array|RFPHY/TRM-RCV/CS/BV-25-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/2 AND<br>RFPHY 3/3a AND<br>RFPHY 3/7 AND<br>RFPHY 3/9|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT, Mode-3, Reflector: 2:2|RFPHY/TRM-RCV/CS/BV-26-C|
|RFPHY 3/1 AND<br>RFPHY 3/6|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-2, Initiator, CS Antenna Array|RFPHY/TRM-RCV/CS/BV-15-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/6 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-2, Initiator|RFPHY/TRM-RCV/CS/BV-27-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/3a AND<br>RFPHY 3/6|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-2, Initiator: 2:2|RFPHY/TRM-RCV/CS/BV-28-C|
|RFPHY 3/1 AND<br>RFPHY 3/7|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-3, Initiator, CS Antenna Array|RFPHY/TRM-RCV/CS/BV-16-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/7 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-3, Initiator|RFPHY/TRM-RCV/CS/BV-29-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/3a AND<br>RFPHY 3/7|Channel Sounding, Transmitter-Receiver, LE<br>1M, Mode-3, Initiator, 2:2|RFPHY/TRM-RCV/CS/BV-30-C|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **74 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Item**|**Feature**|**Test Case(s)**|
|---|---|---|
|RFPHY 3/1 AND<br>RFPHY 3/7 AND<br>RFPHY 3/10|Channel Sounding, Transmitter-Receiver, LE<br>2M, Mode-3, Initiator, CS Antenna Array|RFPHY/TRM-RCV/CS/BV-17-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/7 AND<br>RFPHY 3/10 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>2M, Mode-3, Initiator|RFPHY/TRM-RCV/CS/BV-31-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/3a AND<br>RFPHY 3/7 AND<br>RFPHY 3/10|Channel Sounding, Transmitter-Receiver, LE<br>2M, Mode-3, Initiator, 2:2|RFPHY/TRM-RCV/CS/BV-32-C|
|RFPHY 3/1 AND<br>RFPHY 3/7 AND<br>RFPHY 3/9|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT, Mode-3, Initiator, CS Antenna Array|RFPHY/TRM-RCV/CS/BV-18-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/7 AND<br>RFPHY 3/9 AND<br>NOT RFPHY 3/3b|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT, Mode-3, Initiator|RFPHY/TRM-RCV/CS/BV-33-C|
|((RFPHY 1/1 AND<br>RFPHY 1/2) OR<br>RFPHY 1/3) AND<br>RFPHY 3/1 AND<br>RFPHY 3/3a AND<br>RFPHY 3/7 AND<br>RFPHY 3/9|Channel Sounding, Transmitter-Receiver, LE<br>2M 2BT, Mode-3, Initiator, 2:2|RFPHY/TRM-RCV/CS/BV-34-C|
|RFPHY 3/8|Channel Sounding, Transmitter, LE 1M,<br>TX/SNR|RFPHY/TRM/CS/BV-05-C|
|RFPHY 3/7 AND<br>RFPHY 3/8|Channel Sounding, Transmitter, LE 1M,<br>Mode-3, TX/SNR|RFPHY/TRM/CS/BV-06-C|
|RFPHY 3/8 AND<br>RFPHY 3/10|Channel Sounding, Transmitter, LE 2M,<br>TX/SNR|RFPHY/TRM/CS/BV-07-C|
|RFPHY 3/7 AND<br>RFPHY 3/8 AND<br>RFPHY 3/10|Channel Sounding, Transmitter, LE 2M,<br>Mode-3, TX/SNR|RFPHY/TRM/CS/BV-08-C|
|RFPHY 3/8 AND<br>RFPHY 3/9|Channel Sounding, Transmitter, LE 2M 2BT,<br>TX/SNR|RFPHY/TRM/CS/BV-09-C|
|RFPHY 3/7 AND<br>RFPHY 3/8 AND<br>RFPHY 3/9|Channel Sounding, Transmitter, LE 2M 2BT,<br>Mode-3, TX/SNR|RFPHY/TRM/CS/BV-10-C|



_Table 5.1: Test case mapping_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **75 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **6 A endix pp** 

## **6.1 Reference Signal Definition** 

The Bluetooth low energy reference signal, either as wanted or an interfering signal, has the following characteristics defined in [6] Chapter 4.6. 

Payload content of the wanted signal is a PRBS9 sequence and is identical for all transmitted packets. 

In test cases where an interfering signal is used, the interferer is continuously modulated with PRBS15 data (i.e., no packet structures or pauses in the signal). The interfering signal has settled at least 1 ms prior to the activation of the wanted signal. 

The Lower Tester used for the qualification tests has the ramp up characteristics shown in Figure 6.1. 

- trampup is the time from when the Lower Tester output is 40 dB below the final output power (x dBm) to the time when the output power has reached a level within 3 dB of the final output power. 

- tsettling is the time from when the Lower Tester output is 40 dB below the final output power (x dBm) to the time when the output power has reached a level within 1 dB of the final output power. 

- tp0 is the time at which the first preamble bit begins. 

**==> picture [318 x 279] intentionally omitted <==**

**----- Start of picture text -----**<br>
trampup = 2 ms<br>tsettling = 4 ms<br>3 dB<br>1 dB<br>X dBm<br>tp0<br>(modulation first starts at tp0;<br> min 40 dB<br>start of first preamble bit)<br>**----- End of picture text -----**<br>


_Figure 6.1: Lower Tester ramp-up characteristics requirement, modulation first starts at tp0_ 

## **6.2 Normal Operating Conditions (NOC)** 

## **6.2.1 Normal Temperature** 

The normal operating temperature is declared by the equipment manufacturer as an IXIT value. The NOC test temperature is within ± 10°C of this value. 

The temperature value during the test is recorded in the test documentation. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **76 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **6.2.2 Nominal Supply Voltage** 

The IUT supply voltage under normal operating conditions is the nominal supply voltage as declared by the IUT manufacturer. 

The nominal supply voltage is recorded in the test documentation. 

## **6.3 Packet Error Rate / Bit Error Rate Measurements** 

The Packet Error Rate (PER) measurement is used in all measurements testing receiver characteristics in the Bluetooth low energy RFPHY Test Suite. PER tests are based on the direct test mode described in [4]. 

## **6.3.1 PER Test Definition** 

PER tests are based on counting the number of packets received by the IUT out of a series of consecutive LE test packets transmitted by the Lower Tester. The test is performed with frequency hopping disabled. 

The packet error rate is defined as follows: 

PER = (𝟏−[𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐩𝐚𝐜𝐤𝐞𝐭𝐬 𝐫𝐞𝐜𝐞𝐢𝐯𝐞𝐝 𝐛𝐲 𝐭𝐡𝐞 𝐈𝐔𝐓 𝐩𝐚𝐬𝐬𝐢𝐧𝐠 𝐂𝐑𝐂] 𝐓𝐨𝐭𝐚𝐥 𝐧𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐩𝐚𝐜𝐤𝐞𝐭𝐬 𝐭𝐫𝐚𝐧𝐬𝐦𝐢𝐭𝐭𝐞𝐝 𝐛𝐲 𝐭𝐡𝐞 𝐭𝐞𝐬𝐭𝐞𝐫 ) × 100% 

The Lower Tester transmits LE test packets with PRBS9 payload as defined in [4], Section 4 to the IUT. Upon request from the Lower Tester to the IUT, the IUT reports the number of LE test packets that has been correctly received (i.e., passing CRC) since last request. Refer to [4] for detailed description of the direct test mode. 

The sensitivity level based on BER measurements is defined as the input power level at which a BER of value specified in Table 6.1 is achieved measured with a reference signal as described in Section 6.1, and packet with PRBS9 payload as described in [4], Section 4. 

|**Maximum Supported Payload Length in Receiver (bytes)**|**BER (%)**|
|---|---|
|37|0.1|
|≥38 and≤63|0.064|
|≥64 and≤127|0.034|
|≥128 and≤255|0.017|



_Table 6.1: Sensitivity BER level by maximum payload length in receiver_ 

The PER corresponding to the acceptable BER limit is calculated according to the formula below: 

PER = (1 - X[[(MAX_RX_LENGTH * 8) + 72]] ) × 100% 

- X = 1 – BER, 

- i.e., X=0.99900 if MAX_RX_LENGTH=37, 

- X=0.99936 if 38 ≤ MAX_RX_LENGTH ≤ 63, 

- X=0.99966 if 64 ≤ MAX_RX_LENGTH ≤ 127, 

- X=0.99983 if 128 ≤ MAX_RX_LENGTH ≤ 255. 

- MAX_RX_LENGTH is the maximum supported payload length in IUT’s receiver and it is declared in RFPHY IXIT proforma [5] in range of 37 ~ 255. 

- 72 in the formula is total length of synchronization word, PDU header, PDU length & CRC parts in LE test packet in bit unit. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **77 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **6.3.2 BER to PER Mapping** 

This PER requirement defined in Section 6.3.1 equates to the corresponding BER value under the following assumptions: 

- Bit errors are randomly distributed with a rectangular error probability density function 

- Bit errors are not correlated 

Furthermore, the following reasoning is applied (using an example of BER to PER mapping based on a BER value of 0.1% and MAX_RX_LENGTH of 37 bytes): 

- The probability of a particular bit being in error at a BER of 0.1% is 0.001 

- It follows that the probability of a bit being OK under the same condition is 0.999 

- Examining the impact of a bit error in the LE test packet with a 37-byte payload length: 

Preamble (8 bit) Packet can be recovered2 Sync word (32 bit) Error; Packet is lost Packet type field (16 bit) Error; Packet is lost Payload (296 bit) Error; Packet is lost CRC (24 bit) Error; Packet is lost 

- The number of significant bits in a 37-byte payload LE test packet is thus 368 bits (out of a total of 376 bits). 

- The probability of a 368 bit sequence containing no bit errors is 0.999[368] = 0.692 

- Resulting PER requirement is then (1 - 0.692)*100% = 30.8% 

The sensitivity BER by maximum payload length in the receiver corresponds to the PER requirements listed in Table 6.2 below: 

|**Maximum Supported Payload**<br>**Length in Receiver (bytes)**|**PER**|
|---|---|
|37|30.8%|
|38|21.4%|
|39|21.8%|
|40|22.2%|
|41|22.6%|
|42|23.0%|
|43|23.4%|
|44|23.8%|
|45|24.2%|
|46|24.5%|
|47|24.9%|
|48|25.3%|
|49|25.7%|
|50|26.1%|
|51|26.5%|
|52|26.8%|
|53|27.2%|



> 2 The effect of errors in the preamble is implementation dependent. In general, a bit error in the preamble does not automatically imply that the packet is lost. It is therefore assumed that an error in the preamble is “allowed” and that the packet is recoverable. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **78 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Maximum Supported Payload**<br>**Length in Receiver (bytes)**|**PER**|
|---|---|
|54|27.6%|
|55|27.9%|
|56|28.3%|
|57|28.7%|
|58|29.0%|
|59|29.4%|
|60|29.8%|
|61|30.1%|
|62|30.5%|
|63|30.8%|
|64|18.0%|
|65|18.2%|
|66|18.5%|
|67|18.7%|
|68|18.9%|
|69|19.1%|
|70|19.3%|
|71|19.6%|
|72|19.8%|
|73|20.0%|
|74|20.2%|
|75|20.4%|
|76|20.6%|
|77|20.9%|
|78|21.1%|
|79|21.3%|
|80|21.5%|
|81|21.7%|
|82|21.9%|
|83|22.1%|
|84|22.4%|
|85|22.6%|
|86|22.8%|
|87|23.0%|
|88|23.2%|
|89|23.4%|
|90|23.6%|
|91|23.8%|
|92|24.0%|
|93|24.2%|
|94|24.4%|
|95|24.6%|
|96|24.8%|
|97|25.1%|
|98|25.3%|
|99|25.5%|
|100|25.7%|
|101|25.9%|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **79 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Maximum Supported Payload**<br>**Length in Receiver (bytes)**|**PER**|
|---|---|
|102|26.1%|
|103|26.3%|
|104|26.5%|
|105|26.7%|
|106|26.9%|
|107|27.1%|
|108|27.3%|
|109|27.5%|
|110|27.7%|
|111|27.9%|
|112|28.0%|
|113|28.2%|
|114|28.4%|
|115|28.6%|
|116|28.8%|
|117|29.0%|
|118|29.2%|
|119|29.4%|
|120|29.6%|
|121|29.8%|
|122|30.0%|
|123|30.2%|
|124|30.4%|
|125|30.5%|
|126|30.7%|
|127|30.9%|
|128|17.0%|
|129|17.1%|
|130|17.2%|
|131|17.3%|
|132|17.5%|
|133|17.6%|
|134|17.7%|
|135|17.8%|
|136|17.9%|
|137|18.0%|
|138|18.1%|
|139|18.2%|
|140|18.3%|
|141|18.5%|
|142|18.6%|
|143|18.7%|
|144|18.8%|
|145|18.9%|
|146|19.0%|
|147|19.1%|
|148|19.2%|
|149|19.3%|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **80 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Maximum Supported Payload**<br>**Length in Receiver (bytes)**|**PER**|
|---|---|
|150|19.4%|
|151|19.6%|
|152|19.7%|
|153|19.8%|
|154|19.9%|
|155|20.0%|
|156|20.1%|
|157|20.2%|
|158|20.3%|
|159|20.4%|
|160|20.5%|
|161|20.6%|
|162|20.8%|
|163|20.9%|
|164|21.0%|
|165|21.1%|
|166|21.2%|
|167|21.3%|
|168|21.4%|
|169|21.5%|
|170|21.6%|
|171|21.7%|
|172|21.8%|
|173|21.9%|
|174|22.0%|
|175|22.1%|
|176|22.2%|
|177|22.4%|
|178|22.5%|
|179|22.6%|
|180|22.7%|
|181|22.8%|
|182|22.9%|
|183|23.0%|
|184|23.1%|
|185|23.2%|
|186|23.3%|
|187|23.4%|
|188|23.5%|
|189|23.6%|
|190|23.7%|
|191|23.8%|
|192|23.9%|
|193|24.0%|
|194|24.1%|
|195|24.2%|
|196|24.3%|
|197|24.4%|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **81 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Maximum Supported Payload**<br>**Length in Receiver (bytes)**|**PER**|
|---|---|
|198|24.5%|
|199|24.6%|
|200|24.7%|
|201|24.8%|
|202|24.9%|
|203|25.0%|
|204|25.2%|
|205|25.3%|
|206|25.4%|
|207|25.5%|
|208|25.6%|
|209|25.7%|
|210|25.8%|
|211|25.9%|
|212|26.0%|
|213|26.1%|
|214|26.2%|
|215|26.3%|
|216|26.4%|
|217|26.5%|
|218|26.6%|
|219|26.7%|
|220|26.8%|
|221|26.9%|
|222|27.0%|
|223|27.1%|
|224|27.2%|
|225|27.3%|
|226|27.4%|
|227|27.5%|
|228|27.6%|
|229|27.7%|
|230|27.8%|
|231|27.9%|
|232|27.9%|
|233|28.0%|
|234|28.1%|
|235|28.2%|
|236|28.3%|
|237|28.4%|
|238|28.5%|
|239|28.6%|
|240|28.7%|
|241|28.8%|
|242|28.9%|
|243|29.0%|
|244|29.1%|
|245|29.2%|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **82 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Maximum Supported Payload**<br>**Length in Receiver (bytes)**|**PER**|
|---|---|
|246|29.3%|
|247|29.4%|
|248|29.5%|
|249|29.6%|
|250|29.7%|
|251|29.8%|
|252|29.9%|
|253|30.0%|
|254|30.1%|
|255|30.2%|



_Table 6.2: PER level by maximum payload length in receiver_ 

## **6.4 Definition of the Position of Bit p0** 

Bit p0 is defined as the first bit in the preamble sequence. The start of p0 is defined to occur at the point in time 56 bit periods before the instant at which the modulated carrier passes through the nominal channel frequency immediately prior to the deviation corresponding to the first bit of the payload field. 

The start of bit p0 is calculated using averaging based on the position of all the zero crossings in the packet: 

For the m zero crossings in the packet, the i’th zero crossing time instant is t(i) in µs; this is the start of bit p(i). 

The start of bit p0 is then calculated as: 

**==> picture [108 x 42] intentionally omitted <==**

**==> picture [27 x 12] intentionally omitted <==**

## **6.5 Measurement Uncertainty** 

Table 6.3 contains the measurement accuracy requirements for the test cases described in this document. The test equipment used for the tests must have measurement accuracy within the listed limits. The verdict decision limits for each test case take the measurement uncertainty listed in Table 6.3 into account. All figures in the table reflect a 95% confidence level. 

|**Type of measurement**|**Measurement**<br>**accuracy**<br>**requirement**|
|---|---|
|**Conducted measurements**:<br>Absolute RF power (wanted channel)<br>Absolute RF power (unwanted emissions in the 2400 – 2483.5 MHz band)<br>Absolute RF power (unwanted emissions outside the 2400 – 2483.5 MHz<br>band)|1.2 dB<br>3 dB<br>3 dB3|
|**Relative RF power:**<br>Relative RF power (wanted channel)|1 dB|



> 3 For frequencies above 4 GHz, a measurement accuracy requirement of  4 dB applies 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **83 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Type of measurement**|**Measurement**<br>**accuracy**<br>**requirement**|
|---|---|
|**Radiated measurements:**<br>Absolute RF power (wanted channel)<br>Radiated emissions (for unwanted emissions)|6 dB<br>6 dB|
|**Absolute frequency:**<br>Absolute frequency (RF frequencies)<br>Absolute frequency (Frequency deviation of modulated signal)|5 kHz<br>4 kHz|
|**Relative frequency:**<br>Relative frequency (Frequency drift of carrier during modulation)|1 kHz|



_Table 6.3: Measurement accuracy requirements_ 

## **6.6 Packet Lengths** 

Note: Symbols with names beginning “PL_” are only defined and used within this section. 

For each symbol in the first column of Table 6.4, the value of the symbol is the greater of the values of the symbols in the other two columns. 

|symbols in the other two columns.|||
|---|---|---|
|MAX_TX_LENGTH|PL_ADV_L|PL_DTX_1M|
|MAX_TX_LENGTH_2M|PL_ADV_X|PL_DTX_2M|
|MAX_TX_LENGTH_CODED_S2|PL_ADV_X|PL_DTX_C2|
|MAX_TX_LENGTH_CODED_S8|PL_ADV_X|PL_DTX_C8|
|MAX_RX_LENGTH|PL_SCN_L|PL_DRX_1M|
|MAX_RX_LENGTH_2M|PL_SCN_X|PL_DRX_2M|
|MAX_RX_LENGTH_CODED_S2|PL_SCN_X|PL_DRX_C2|
|MAX_RX_LENGTH_CODED_S8|PL_SCN_X|PL_DRX_C8|



_Table 6.4: Overall Inputs for Packet Length Symbols_ 

If the Link Layer of the IUT supports the Advertising Extension feature, then: 

- PL_ADV_L and PL_ADV_X equals TSPX_AdvOctets_Max. 

- PL_SCN_L and PL_SCN_X equals 255. 

Otherwise: 

- PL_ADV_L and PL_SCN_L equals 37. 

- PL_ADV_X and PL_SCN_X equals 31. 

If the Link Layer of the IUT supports the Data Length Extension feature, then for each symbol in the first column of Table 6.5, the value of the symbol is the lesser of the values of the expressions in the other two 

columns (“ ⌊ X ⌋ ” means the greatest integer ≤ X). 

|PL_DTX_1M|TSPX_TxOctets_Max+4|⌊TSPX_TxTime_Max÷8–10⌋|
|---|---|---|
|PL_DTX_2M|TSPX_TxOctets_Max+4|⌊TSPX_TxTime_Max÷4–11⌋|
|PL_DTX_C2|TSPX_TxOctets_Max+4|⌊TSPX_TxTime_Max ÷ 16– 28⌋|
|PL_DTX_C8|TSPX_TxOctets_Max+4|⌊TSPX_TxTime_Max÷64–11⌋|
|PL_DRX_1M|TSPX_RxOctets_Max+4|⌊TSPX_RxTime_Max÷8–10⌋|
|PL_DRX_2M|TSPX_RxOctets_Max+4|⌊TSPX_RxTime_Max ÷ 4 – 11⌋|
|PL_DRX_C2|TSPX_RxOctets_Max+4|⌊TSPX_RxTime_Max÷16–28⌋|
|PL_DRX_C8|TSPX_RxOctets_Max+4|⌊TSPX_RxTime_Max÷64–11⌋|



_Table 6.5: Maximum Lengths When Data Length Extension is Supported_ 

Otherwise, the values of all the symbols in the first column of Table 6.5 are 31. 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **84 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

Note: For each symbol in the first column of Table 6.6, the reference for that symbol in [5] is given in the second column. The third and fourth columns give the minimum and maximum permitted values for the symbol. 

|symbol.||||
|---|---|---|---|
|TSPX_AdvOctets_Max|LL:P4:19 on the LL tab|37|255|
|TSPX_RxOctets_Max|LL:P4:17 on the LL tab|27|251|
|TSPX_RxTime_Max|LL:P4:18 on the LL tab|328|17040|
|TSPX_TxOctets_Max|LL:P4:15 on the LL tab|27|251|
|TSPX_TxTime_Max|LL:P4:16 on the LL tab|328|17040|



_Table 6.6: References_ 

## **6.7 Number of Valid IQ Sample Pairs** 

This section and its subsections are explanatory. 

A controller can return IQ sample pairs where either I or Q, or both, are marked as ‘No Valid Sample Available’. These IQ sample pairs are discarded as invalid. Invalid IQ sample pairs are not used in the magnitude, relative phase, and reference phase deviation calculations. 

The number of valid IQ sample pairs required per non-reference antenna for the IQ Samples Coherency tests is chosen as 10,000. The same number of valid IQ sample pairs is chosen for the IQ Dynamic Range tests, to maintain consistency across the tests. 

## **6.7.1 Maximum Number of Packets for IQ Coherency Measurements** 

The tests require LE packets to be sent with maximum length CTE comprising of 1 µs or 2 µs slots. The number of collected IQ sample pairs per packet is either 74 or 37, respectively. The measurements are performed using IQ sample pair groups that must include non-reference antenna transmissions. Using the pre-defined switching pattern (x000, …, where x is a non-reference antenna), a maximum of 18 sample pairs groups for 1 µs slots and 8 sample pairs groups for 2 µs slots that include all required IQ sample measurements are possible from every CTE. 

The following tables show the number of IQ sample pairs returned by the IUT for different number of non-reference antenna for 1us and 2us switching slots, respectively. 

|**Number of non-reference antennae**|**1**|**2**|**3**|
|---|---|---|---|
|1|18|0|0|
|2|9|9|0|
|3|6|6|6|



_Table 6.7: Number of I/Q samples per antenna element for 1 µs switching slots_ 

|**Number of non-reference antennae**|**1**|**2**|**3**|
|---|---|---|---|
|1|8|0|0|
|2|4|4|0|
|3|2|3|3|



_Table 6.8: Number of I/Q samples per antenna element for 2 µs switching slots_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **85 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

Table for the number of packets transmitted required to obtain 10,000 IQ sample pairs per non-reference antenna on the receiver is shown below: 

|**Number of non-reference antennae**|**1 µs switching slot**|**2 µs switching slot**|
|---|---|---|
|1|556|1250|
|2|1112|2500|
|3|1667|3334|



_Table 6.9: Number of packets required for 10,000 IQ sample pairs_ 

The Table 6.9 assumes that IUT receives all packets successfully, and all the IQ sample pairs reported are marked valid. 

The number of packets transmitted required for the test needs to be increased to allow for both lost packets and invalid IQ sample pairs. A 20% allowance to account for lost packets and invalid IQ sample pairs is recommended. The IUT reports IQ sample pairs at a rate of TSPX_IQ_Report_Rate. The number of packets transmitted by the Lower Tester for the measurement needs to scale by the following factor: 

**==> picture [224 x 25] intentionally omitted <==**

This is the recommended maximum number of packets transmitted by the Lower Tester for the coherency tests. 

## **6.8 Antenna Gain** 

If it is necessary for Regulatory test purposes, the TX peak antenna gain is used and declared by the manufacturer. 

## **6.9 Tester Filter Characteristics** 

This section defines the PHY-dependent Lower Tester settings used for the RF channel filter (see Table 6.10) and the FM demodulator (see Table 6.11). 

|**Frequency (for 1 Ms/s)**|**Frequency (for 2 Ms/s)**|**Frequency (for 2 Ms/s; BT=2.0)**|**Attenuation**|
|---|---|---|---|
|±650kHz<br>Passband ripple:<br>0.5 dB (within ± 550 kHz)|±1.3 𝑀𝐻𝑧<br>Passband ripple:<br>0.5 dB (within ± 1.1 MHz)|±7.8 𝑀𝐻𝑧<br>Passband ripple:<br>0.5 dB (within ± 4.4 MHz)|3 dB|
|±1.0MHz|±2.0 𝑀𝐻𝑧|±9.2 𝑀𝐻𝑧|14dB|
|±2.0MHz|±4.0 𝑀𝐻𝑧|±11.0 𝑀𝐻𝑧|44 dB|



_Table 6.10: Lower Tester minimum channel filter attenuation characteristics_ 

|**FM Demodulator Characteristic**|**1 Ms/s PHY**|**2 Ms/s PHY**|**2 Ms/s; BT=2.0 PHY**|
|---|---|---|---|
|Bandwidth (minimum)|2.0 𝑀𝐻𝑧|4.0 𝑀𝐻𝑧|16.0 𝑀𝐻𝑧|



_Table 6.11: Lower Tester FM demodulation characteristics_ 

**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **86 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

## **7 Revision histor and acknowled ments y g** 

## _**Revision History**_ 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
|0|RF-<br>PHY.TS/4.0.0|2009-12-15|Prepare for publication.|
||4.0.1r0<br>4.0.1r1|2010-12-01-<br>2011-02-02|TSE 3408: TRM-LE/CA/BV-03-C , TRM-LE/CA/BV-<br>04-C: updates 5, 6<br>TSE 3462 Rename test case in Tables 7.2 and 7.3 :<br>TSE 3945: Remove Section 7.2 and refer to ESR05,<br>eventually to be moved to core spec Vol 6, Part D<br>Section 4. See also TSE 4204.<br>TSE 4204: Additional changes for E3696 ( see also<br>TSE 3945)|
|1|4.0.1|2011-07-18|Prepare forpublication.|
||4.0.2r0|2012-09-06|TSE 4906: Change to test procedure of TRM-<br>LE/CA/BV-03-C added, "AND skip to next frequency if<br>the increased frequency equals to fTX or "fTX - 1MHz"<br>or "fTX + 1MHz".|
|2|4.0.2|2012-11-15|Prepare for Publication|
||4.0.3r1|2013-05-31|TSE 5041: Editorial correction in step 3 of the test<br>procedure for test case RCV-LE/CA/BV-01-C,<br>incorrect cross-reference.<br>TSE 5042: Editorial correction to the cross-reference<br>in Figure 6.7 in RCV-LE/CA/BV-03-C that referenced<br>“Table  .4” when it should have referenced “ .3”.<br>TSE 5043: Editorial correction to the cross-reference<br>in Figure 6.8 in RCV-LE/CA/BV-04-C that referenced<br>“Table  .5” when it should have referenced “ .4”.<br>TSE 5044: Editorial correction in the 3rd paragraph of<br>thepass verdict for test case RCV-LE/CA/BV-04-C.|
||4.0.3r2,|2013-06-03|BTI Review, comments from Miles.|
||4.0.3r3|2013-06-04|BTI Review, comments from Dan.<br>Updated Copyright Notice to 2013.<br>Changed Table reference to figure reference in Step 4<br>of TRM-LE/CA/BV-06-C.|
||4.0.3r4|2013-06-04|BTI Review, additional comments from Dan<br>TRM-LE/CA/BV-04-C was an incorrect heading level,<br>changed it to the test case heading level which<br>updated the section from 6.3 to 6.3.4.|
|3|4.0.3|2013-07-02|Prepare for Publication|
||4.1.0r01|2013-11-11|Revision to accommodate  v 4.1|
|4|4.1.0|2013-12-03|Prepare for Publication|
||4.1.0 –<br>Template<br>Conversion|2014-01-23|Template Conversion into Template_TS_2014r02|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **87 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||4.1.1r00|2014-01-23|TSE 5507: Correctly formatted the TC IDs for TRM-<br>LE/CA/BV-01-C, TRM-LE/CA/BV-02-C, TRM-<br>LE/CA/BV-03-C, TRM-LE/CA/BV-04-C, TRM-<br>LE/CA/BV-05-C, TRM-LE/CA/BV-06-C, TRM-<br>LE/CA/BV-07-C, RCV-LE/CA/BV-01-C, RCV-<br>LE/CA/BV-02-C, RCV-LE/CA/BV-03-C, RCV-<br>LE/CA/BV-04-C, RCV-LE/CA/BV-05-C, RCV-<br>LE/CA/BV-06-C, RCV-LE/CA/BV-07-C.|
||4.1.2r00|2014-10-21|TSE 5635: Corrected a statement that had lost the<br>superscript, “The probability of a 3 8 bit sequence<br>containingnot bit errors is 0.999^3 8 = 0. 92”|
||4.1.2r01|2014-11-05|BTI Review, Magnus, Removed Test Suite Structure<br>illustration.|
||4.2.0r00|2014-11-07|Integrated CRs from RF-PHY TS 4 1 0-<br>Data_Length_Increase_r02.|
||4.2.0r01|2014-11-24|Updated Test Case numbering convention to match<br>convention in TCRL(added “BV” and dashes).|
|5|4.2.0|2014-12-04|Prepare for TCRL 2014-2publication|
||4.2.1r00|2015-05-06|TSE 6142: Updated Section 6.6 to be consistent with<br>revised sensitivity levels in Core spec. Revised Pass<br>verdicts accordingly for TP/RCV-LE/CA/BV-01-C,<br>TP/RCV-LE/CA/BV-03-C, TP/RCV-LE/CA/BV-04-C,<br>TP/RCV-LE/CA/BV-05-C, TP/RCV-LE/CA/BV-06-C.<br>TSE  100  Deleted “EIRP” in TP TRM-LE/CA/BV-01-<br>C Pass verdict.<br>TSE 6140: Revised References section to remove<br>redundant entries and correct errors. Updated<br>instances of those references throughout the<br>document.<br>TSE 6340: Corrected equation in step 5 of TP/TRM-<br>LE/CA/BV-03-C<br>TSE 6368: Corrected references to other steps in<br>steps 8 and 12 of TP/TRM-LE/CA/BV-03-C|
||4.2.1r01|2015-05-18|TSE 6413: Revised PER value in Pass verdict of<br>TP/RCV-LE/CA/BV-07-C|
||4.2.1r02|2015-06-03|Editorial: Universal change from EUT to IUT<br>Removal of redundant Section 6.5 (Test Conditions<br>Summary)|
|6|4.2.1|2015-07-14|Prepared for TCRL 2015-1publication|
||4.2.2r00|2015-10-09|TSE 6369: Changed interval for frequency drift rate #0<br>in Figure 4.5 and updated the pass criterion frequency<br>for TP/TRM-LE/CA/BV-06-C.<br>TSE 6622: Removed TP/TRM-LE/CA/BV-02-C,<br>TP/TRM-LE/CA/BV-04-C, TP/TRM-LE/CA/BV-07-C,<br>and TP/RCV-LE/CA/BV-02-C.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **88 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 6682: Revised initial conditions for TP/TRM-<br>LE/CA/BV-01-C, TP/TRM-LE/CA/BV-03-C, TP/TRM-<br>LE/CA/BV-05-C, TP/TRM-LE/CA/BV-06-C, TP/RCV-<br>LE/CA/BV-01-C, TP/RCV-LE/CA/BV-03-C, TP/RCV-<br>LE/CA/BV-04-C, TP/RCV-LE/CA/BV-05-C, TP/RCV-<br>LE/CA/BV-06-C, and TP/RCV-LE/CA/BV-07-C. Also<br>added Section 6.8 Packet Lengths.|
||4.2.2r01|2015-10-27|Reviewed by Dave Richter.<br>Editorial changes resulting from TSE 6622: Removed<br>Section 6.4 (EOC); removed other references to<br>extreme conditions throughout; removed references to<br>normal conditions throughout where they became<br>redundant with the removal of extreme operating<br>conditions.|
||4.2.2r02|2015-11-03|Reviewed by Magnus Sommansson.<br>Reinstated “Test Condition” test sections with<br>instructions to perform tests at normal operating<br>conditions.|
||4.2.2r03|2015-11-18|Integrated changes for Core Specification Addendum<br>5 (CSA5): Added references and updated pass verdict<br>for TP/TRM-LE/CA/BV-01-C[Outputpower].|
|7|4.2.2|2015-12-22|Prepared for TCRL 2015-2publication|
||4.2.3r00|2016-02-11|TSE 6818: Added Section 4.4 Common Test Case<br>Conditions. The following changes applied to all test<br>cases: First initial condition moved to Section 4.4.<br>Added new test condition with cross-reference to<br>Section 4.4. Deleted test condition moved to<br>Section 4.4.|
||4.2.3r01|2016-03-02|TSE 6917: Relaxation measurement criteria changed<br>in TP/RCV-LE/CA/BV-03-C from “does not apply”<br>exceptions to “does apply” admissions.|
||4.2.3r02|2016-04-07|TSE 6395: Updated Initial Condition of test case<br>TP/RCV-LE/CA/BV-01-C. Corrected “2) to 3)” to “2) to<br>4).” Changed modulation frequency to 1250 Hz.<br>Second to last sentence reworded slightly. MSC<br>updated. Changed fmodto “1250 Hz” and T 4 to<br>“200μs.”|
|8|4.2.3|2016-07-13|Prepared for TCRL 2016-1publication|
||5.0.0r00|2016-07-07|Integrated changes for Core Specification 5.0 release:<br>2MBPS_Test_Cases_CRr12: Global edit. Added 5<br>new sections for test cases TRM-LE/CA/BV-07-C –<br>11-C. Added 18 new sections for test cases TP/RCV-<br>LE/CA/BV-08-C – 25-C.<br>BLR_Test_Cases_CRr12: Global edit. Added 2 new<br>sections for test cases TP/TRM-LE/CA/BV-12-C & 13-<br>C. Added 12 new sections for test cases TP/RCV-<br>LE/CA/BV-26-C – 37 C.|
||5.0.0r01|2016-06-28|Issue 7189: Updated test case TP/TRM-LE/CA/BV-<br>12-C: Updated Steps 4, 8, and 9. Deleted Steps 8–12.<br>Updated Pass Verdict.<br>Issue 7286: Entire “Packet Lengths” section rewritten.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **89 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||5.0.0r02|2016-09-02|Issue  553  Added sum symbol (∑) to step   in test<br>case TP/TRM-LE/CA/BV-07-C. Global edits:<br>Removed replaced “must” in Pass verdict. Updated<br>legacy test text  Changed “…at 1 Ms s” to “…uncoded<br>data at 1 Ms s.” Deleted condition from legacy tests.<br>Reference instead Section 4.4, Common Test Case<br>Conditions. Updated Test Condition to reference<br>Section 4.4. Step numbering corrected in test case<br>TP/RCV-LE/CA/BV-09-C and TP/RCV-LE/CA/BV-11-<br>C. Replaced all occurrences of “at NOC” with<br>“uncoded data at 1 Ms s.”|
||5.0.0r03|2016-09-20|Issue 7643: Updated description of interference signal<br>in Test Procedure for test cases TP/RCV-LE/CA/BV-<br>03-C, 05-C, 09-C, 11-C, 28-C, and 29-C.|
||5.0.0r04|2016-10-03|Issue 7733: Added missing space between sentences<br>in Test Purposes > Conformance section. Updated<br>test case TP/RCV-LE/CA/BV-03-C  Changed “Steps 2<br>to 4” to “Steps 2 to 3.” Changed “Steps 2 to  ” to<br>“Steps 2 to 5.” Updated Initial Condition, Test<br>Procedure, and Pass Verdict of test case TP/RCV-<br>LE/CA/BV-24-C to align with style in test case<br>TP/RCV-LE/CA/BV-18-C.<br>Issue 7774: Changed test cases TP/TRM-LE/CA/BV-<br>07-C – 13-C to TP/TRM-LE/CA/BV-08-C – 14-C,<br>respectively, in test case headings, TCMT, and<br>Appendix.|
||5.0.0r05|2016-10-10|TSE 7551: Deleted notes from test case TP/TRM-<br>LE/CA/BV-01-C.|
||5.0.0r06|2016-10-12|TSE  450  Standardized “Pass Verdict” wording for<br>test case TP/TRM-LE/CA/BV-01-C.|
||5.0.0r07|2016-11-08|Issue 7806: In the TP/TRM-LE/CA/BV-14-C: Updated<br>steps 4-6 (including Figure 4.6) in test procedure to<br>match symbols before and after all 16-symbol blocks;<br>Removed "|f0 – f3|"from Pass Verdict, and adjusted<br>“n” range for |”fn – f(n-3)|.”<br>Issue 7905: For TP/RCV-LE/CA/BV-09-C, updated<br>interference frequency selection formula in step 4 of<br>test procedure and updated adjacent channels in table<br>and Pass Verdict.|
||5.0.0r08|2016-11-22|Removed obsolete TC references that got accidentally<br>reintroduced with the Shanghai CRs. Removed<br>TP/TRM-LE/CA/BV-02-C from 6.2.2. Removed<br>TP/TRM-LE/CA/BV-02-C and –BV-04-C as well as<br>TP/RCV-LE/CA/BV-02-C from 6.2.3|
|9|5.0.0|2016-12-13|Approved by BTI. Prepared for TCRL 2016-2<br>publication.|
||5.0.1r00|2017-03-08|TSE 7818: In RF-PHY/TRM-LE/CA/BV-01-C, updated<br>Pass Verdict and added IEEE term “shall”.<br>TSE 8337: See notes below for TSE 8339.<br>TSE 8338: See notes below for TSE 8339.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **90 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 8339: In RF-PHY/RCV-LE/CA/BV-03-C and RF-<br>PHY/RCV-LE/CA/BV-09-C, updated figure: Changed<br>interference signal level from "-67dBm + C/I + Lt" to "-<br>67dBm - C/I + Lt". In RF-PHY/RCV-LE/CA/BV-28-C,<br>updated figure: Changed interference signal level from<br>"-89dBm + C/I + Lt" to "-72dBm - C/I + Lt". In RF-<br>PHY/RCV-LE/CA/BV-29-C, updated figure: Changed<br>interference signal level from "-91dBm + C/I + Lt" to "-<br>79dBm - C/I + Lt". Note: TSE 8339 includes TSE 8337<br>and TSE 8338.|
||5.0.1r01|2017-05-10|Converted to new Test Case ID conventions as<br>defined in TSTO v4.1.|
|10|5.0.1|2017-07-05|Approved by BTI. Prepared for TCRL 2017-1<br>publication.|
||5.0.2r00|2017-08-18|TSE 9161: In Frequencies for Testing: Peripheral and<br>Central Devices, reorganized RF-PHY/TRM-<br>LE/CA/BV-13-C and RF-PHY/TRM-LE/CA/BV-14-C<br>and deleted RF-PHY/TRM-LE/CA/BV-04-C in the test<br>case(s) table. Added the following 20 TCIDs to<br>Appendix > In Frequencies for Testing: Broadcaster<br>and Observer Devices section: RF-PHY/TRM-<br>LE/CA/BV-13-C - …14-C, RF-PHY/RCV-LE/CA/BV-<br>14-C - …25-C, and RF-PHY/RCV-LE/CA/BV-32-C -<br>…3 -C.<br>TSE 9173: Deleted test in Test Strategy. Deleted<br>Provisional RF Testing and Test Equipment sections<br>from Test Cases > Introduction section.|
||5.0.2r01|2017-09-19|AoA/AoD: Integrated the AoA/AoD CR into the<br>Reference section and test cases RF-PHY/TRM-<br>LE/CA/BV-01-C, RF-PHY/TRM-LE/CA/BV-06-C, and<br>RF-PHY/TRM-LE/CA/BV-12-C. Added new test cases<br>RF-PHY/TRM-LE/CA/BV-15-C - …1 -C. Added new<br>tests to TCMT.|
||5.0.2r02|2017-10-02|TSE 9858: Resized RF-PHY/TRM-LE/CA/BV-06-C<br>Figures 4.4 and 4.5 to fit portrait page.<br>TSE 9895: Fixed RF-PHY/RCV-LE/CA/BV-31-C test<br>procedure typo in data codingscheme.|
||5.0.2r03|2017-10-13|TSE 9859: Revised the RF-PHY/TRM-LE/CA/BV-05-C<br>“Frequency deviation measurement principle for<br>10101010-payload sequence” figure.|
||5.0.2r04|2017-10-31|TSE 9161:Reorganized RF-PHY/TRM-LE/CA/BV-13-<br>C and RF-PHY/TRM-LE/CA/BV-14-C in the test<br>case(s) table in “Frequencies for Testing: Peripheral<br>and Central Devices.”|
|11|5.0.2|2017-12-07|Approved by BTI. Prepared for TCRL 2017-2<br>publication.|
||5.0.3r00-02|2018-01-26 –<br>2018-06-08|Issue 10132 : deleted AoA/AoD text from test cases<br>RF-PHY/TRM-LE/CA/BV-01-C (section 4.4.1), RF-<br>PHY/TRM-LE/CA/BV-06-C (section 4.4.4), and RF-<br>PHY/TRM-LE/CA/BV-12-C(section 4.4.9).|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **91 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 1010  (rating 1)  Changed “TRM-LE/CA”to<br>“TRM”and “RCV-LE/CA”to “RCV”in test case<br>names.<br>TSE 10106 : fixed integration error. Applied change to<br>two more instances in test case RF-PHY/TRM/BV-11-<br>C.|
|12|5.0.3|2018-07-02|Approved by BTI. Prepared for TCRL 2018-1<br>publication.|
||5.0.4r00-r04|2018-08-20 -<br>2018-10-25|Incorporated RF-PHY.DF.Test CRr09: Added 20 new<br>test cases to spec text, TCMT, and Appendix Table<br>6.2: RF-PHY/TRM/IQC/BV-01-C – 08-C; RF-<br>PHY/RCV/IQC/BV-01-C – 12-C. Added 2 new<br>sections: "Test Setups Examples" (Section 4.6) and<br>"Error Measurement for IQ Samples" (Section 6.8).<br>Issue 11046: Various clarifications and typo<br>corrections for IQ sample test material. Sections: Tx<br>Power Stability, AoD Transmitter; Antenna switching<br>integrity, AoD Transmitter; IQ Samples Coherency,<br>AoD Receiver; IQ Samples Coherency, AoA Receiver;<br>IQ Samples Dynamic Range, AoD Receiver; IQ<br>Samples Dynamic Range, AoD Receiver; Appendix.<br>Issue 11081: Clarifications and typo corrections for IQ<br>sample test material.<br>Issue 11085: Clarified test procedure step repetition in<br>IQ Samples Coherency and Dynamic Range test<br>cases.<br>TSE 11072 (rating 1): Fixed typo in revision date on<br>first page.<br>TSE 10897 (rating 2): Changed Interference Signal #2<br>from 1 Ms/s to 2 Ms/s for test case RF-PHY/RCV/BV-<br>11-C.<br>Issue 11082: Comprehensive re-write of the IQ<br>Sample Appendix section for clarity and accuracy.<br>Integration review, renaming from /TRM/IQC/BV-01.. -<br>04-C to “ TRM PS BV-01-C etc., from /TRM/IQC/BV-<br>05..08-C to /TRM/ASI/BV-05-C etc., from<br>/RCV/IQC/BV-07..-12-C to /RCV/IQDR/BV-07 etc.|
||5.1.0|2018-11-13|Updated revision number to 5.1.0 to align with the<br>adoption of Core Specification version 5.1|
|13|5.1.0|2018-12-07|Approved by BTI. Prepared for TCRL 2018-2<br>publication.|
||5.1.1r00–r02|2019-03-29–<br>2019-05-15|TSE 11535 (rating 1): Updated TCMT Item to LL 9/22<br>for test cases RF-PHY/TRM/PS/BV-02-C, 04-C; and<br>RF-PHY/TRM/ASI/BV-06-C, BV-08-C.<br>TSE 11732 (rating 1): Updated the test procedure in<br>the "IQ Samples Dynamic Range, AoD Receiver" and<br>"IQ Samples Dynamic Range, AoA Receiver"<br>sections.<br>TSE 11791 (rating 2): TCMT-only change to<br>accommodate ICS/IXIT updates.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **92 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
|14|5.1.1|2019-08-01|Approved by BTI. Prepared for TCRL 2019-1<br>publication.|
||p15r00–r02|2019-09-06 –<br>2019-11-12|TSE 1209  (rating 3)  Updated pass verdict for “IQ<br>Samples Coherency, AoD Receiver” section, which<br>affects test cases RF-PHY/RCV/IQC/BV-01-C – -04-<br>C. Updated pass verdict for “IQ Samples Coherency,<br>AoA Receiver” section, which affects test cases RF-<br>PHY/RCV/IQC/BV-05-C and -06-C.<br>TSE 12098 (rating 1): Updated test step for “IQ<br>Samples Coherency, AoD Receiver” section, which<br>affects test cases RF-PHY/RCV/IQC/BV-01-C – -04-<br>C, and test step for “IQ Samples Coherency, AoA<br>Receiver” section, which affects test cases RF-<br>PHY/RCV/IQC/BV-05-C and -06-C.<br>TSE 12127 (rating 2): Updated TCMT to take into<br>account the PHYs for the IQ sample tests.<br>TSE 12384 (rating 1): Clarified expected outcome text<br>and fixed subscripting of text in test cases RF-<br>PHY/TRM/BV-16-C and -17-C.<br>Revised document numbering convention, setting last<br>release publication of 5.1.1 as p14; added publication<br>number column to Revision History.|
|15|p15|2020-01-07|Approved by BTI on 2019-12-22. Prepared for<br>TCRL 2019-2publication.|
||p16r00–r07|2020-01-31 –<br>2021-06-04|TSEs 12505, 12947, 12948 (rating 2): Editorial<br>adjustment that involved removing Section 6.2 and the<br>testing frequencies tables in Sections 6.2.1 and 6.2.2,<br>adding testing frequencies tables to the test condition<br>section of each test case, and moving the introduction<br>text from Section 6.2 regarding direct test mode, etc.<br>to Section 4.2_“Common Test Case Conditions”._<br>(Note: All changes for TSEs 12505, 12947, and 12948<br>are flagged for this integration as TSE 12505, as they<br>use a single CR to incorporate all of the changes<br>required for all three TSEs.)<br>TSE 12941 (rating 2): Updated TCMT to include<br>“2Ms/s” to better align with ICS; affected test cases<br>RF-PHY/RCV/IQC/BV-03-C, -04-C, and -06-C; RF-<br>PHY/RCV/IQDR/BV-09-C, -10-C, and -12-C; RF-<br>PHY/TRM/PS/BV-03-C and -04-C; and RF-<br>PHY/TRM/ASI/BV-07-C and -08-C.<br>TSE 13402 (rating 2): Edited test steps and pass<br>verdicts to address an issue with requiring too many<br>packets to be transmitted per test. Affected sections<br>containing test cases RF-PHY/RCV/IQC/BV-01-C –-<br>06-C and RF-PHY/RCV/IQDR/BV-07-C – -12-C.<br>TSE 14692 (rating 2): Updated TCMT to fix a mapping<br>error.<br>TSE 16485 (rating 4): To address E16372 regarding<br>Transmit Power Level for Power Class, moved<br>RFPHY/TRM/BV-01-C into a TC Config table with new<br>TC RFPHY/TRM/BV-18-C and updated Pass verdict.<br>Updated TCMT accordingly.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **93 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 16596 (rating 1): Corrected an error in the<br>formulae calculating amplitude A in the “IQ Samples<br>Dynamic Range, AoD Receiver” and “IQ Samples<br>Dynamic Range, AoA Receiver” sections by updating<br>step 4 and the Pass verdict.<br>TSE 16697 (rating 1): Updated title/header and<br>document ID; updated all instances of “RF PHY” and<br>“RF-PHY” to “RFPHY” to align with the latest naming<br>conventions.<br>Template-related and consistency checker editorials.<br>Editorial corrections to properties requiring subscript<br>formatting (e.g., fRXand fTX).|
|16|p16|2021-07-13|Approved by BTI on 2021-06-27. Prepared for<br>TCRL 2021-1publication.|
||p17r00–r04|2021-08-26 –<br>2021-11-29|TSE 16706 (rating 2): Changed test items related to<br>LE 2M to not test CH0/12/39. Simplified the frequency<br>tables by combining roles where they contained the<br>same test frequencies and removing Tx frequencies<br>from Rx tests (and vice versa). Added MHz units to<br>frequency tables. Changed n=2 and n=37, to n=1 and<br>n=38 for 2 Ms/s tests. Removed 2 Ms/s reference<br>from the section containing tests<br>RFPHY/TRM/BV-01-C and -18-C and from -15-C.<br>Overall affected TCs as follows:<br>RFPHY/TRM/BV-01-C, -03-C, -05-C, -06-C, -08-C –<br>-18-C; RFPHY/TRM/PS/BV-01-C – -04-C;<br>RFPHY/TRM/ASI/BV-05-C – -08-C; RFPHY/RCV/BV-<br>01-C and -03-C – -37-C; RFPHY/RCV/IQC/BV-01-C –<br>-06-C; and RFPHY/RCV/IQDR/BV-07-C – -12-C.<br>TSE 17311 (rating 2): Updated the initial conditions<br>and test procedure of the section containing<br>RFPHY/TRM/BV-01-C and -18-C to use Antenna Gain<br>G as specified in the IXIT. Added a section in the<br>Appendix on Antenna Gain.<br>TSE 17395 (rating 1): Editorial corrections to fix<br>superscript formatting in Section 6.3.2 and add a 0 to<br>0.9990 in Section 6.3.1 to align with the significant<br>figures in the rest of the bulleted list.<br>TSE 17727 (rating 1): Updated Acknowledgments list.<br>Performed template-related editorial work, including<br>aligningthe copyrightpage with v2 of the DNMD.|
|17|p17|2022-01-25|Approved by BTI on 2021-12-27. Prepared for<br>TCRL 2021-2publication.|
||p18r00–r03|2022-02-03 –<br>2022-04-08|TSE 17597 (rating 4): To address a need for 2M<br>versions of certain tests, updated the “Output power”<br>section, modifying Test Purpose, Initial Condition, and<br>test steps. Affected test cases are RFPHY/TRM/BV-<br>01-C, -15-C, and -18-C (note that -15-C was removed<br>as a freestanding TC and is now in the TC Config<br>table in this test group); new test cases are<br>RFPHY/TRM/BV-19-C – -23-C. Updated the TCMT<br>accordingly.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **94 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 17599 (rating 2): Added default frequencies for<br>testing in Section 4.2. Deleted “Frequencies for<br>Testing” tables and made related edits in the Test<br>Condition sections in RFPHY/TRM/BV-01-C, -03-C,<br>-05-C, -06-C, -08-C – -17-C and<br>RFPHY/RCV/BV-01-C, -03-C, -05-C, -06-C,<br>-08-C – -12-C, -14-C, -15-C, -17-C, -18-C,<br>-20-C – -24-C, -26-C – -29-C, -32-C – -35-C.<br>TSE 18260 (rating 2): Updated TCMT items for<br>RFPHY/RCV/IQC/BV-01-C – -04-C<br>RFPHY/RCV/IQDR/BV-07-C – -10-C.<br>TSE 18298 (rating 1): Corrected missing superscript<br>formatting in Section 6.3.1.<br>TSE 18348 (rating 2): Updated TCMT items for<br>RFPHY/TRM/BV-15-C, -16-C, and -18-C.<br>TSE 1838  (rating 2)  Added “Fields and Bits<br>Reserved for Future Use” section.<br>TSE 18554 (rating 2): Updated the expected outcome<br>for RFPHY/TRM/BV-12-C.<br>TSE 18635 (rating 1): Updated the test procedure and<br>expected outcome for RFPHY/TRM/BV-16-C.<br>Performed template-related formatting fixes. Replaced<br>all mentions of “Common Test Case Conditions” with<br>a link to that section heading.|
|18|p18|2022-06-28|Approved by BTI on 2022-05-31. Prepared for<br>TCRL 2022-1publication.|
||p19r00|2022-09-27|TSE 20370 (rating 1): Updated some of the<br>drawings/pictures for TCs RFPHY/TRM/BV-05-C and<br>-16-C.|
|19|p19|2023-02-07|Approved by BTI on 2022-12-28. Prepared for<br>TCRL 2022-2publication.|
||p20r00–r01|2023-03-10 –<br>2023-04-04|TSE 22581 (rating 1): For consistency, replaced the<br>instances of “DUT” with “IUT” in RFPHY/RCV/<br>BV-07-C, -13-C, -19-C, -25-C, -30-C, -31-C, -36-C,<br>and -37-C.<br>TSE 22909 (rating 2): Reformatted the following test<br>cases into a table-driven structure: RFPHY/TRM/BV-<br>03-C, -05-C, -06-C, -08-C – -14-C, -16-C, and -17-C;<br>and RFPHY/RCV/BV-01-C and -03-C – -37-C.|
|20|p20|2023-06-29|Approved by BTI on 2023-06-05. Prepared for<br>TCRL 2023-1publication.|
||p20ed2<br>r00–r01|2023-08-07 –<br>2023-08-25|TSE 23263 (rating 1): In the “C I and Receiver<br>Selectivity Performance” section, updated the<br>captions to align with the section title, replaced the<br>figure, and revised the parameter table to correct the<br>labels and subscripted text. Replaced the figure in the<br>“Blocking Performance” section.<br>TSE 23337 (rating 1): Replaced the figure in the<br>“Intermodulation Performance” section.|
||p20 edition 2|2023-08-28|Approved by BTI on 2023-08-24. Prepared for<br>edition 2publication.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **95 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||p21r00–r01|2023-08-28 –<br>2023-10-30|TSE 23568 (rating 1): Updated a test step in the<br>section containing RFPHY/TRM/BV-05-C, -09-C –<br>-11-C, and -13-C.<br>TSE 24252 (rating 1): Added a reference to Core v5.0<br>LL spec.; updated the requirements for<br>RFPHY/TRM/BV-13-C and updated the test steps and<br>Pass verdict for the section containing that TC as well<br>as -05-C and -09-C – -11-C.|
|21|p21|2024-07-01|Approved by BTI on 2024-05-22. Prepared for<br>TCRL 2024-1publication.|
||p22r00–r09|2024-07-09 –<br>2024-08-20|Incorporated CS_RFPHY.TS_CR_r13 (which includes<br>Test Issues 23205, 23293, 23331, 23332, 23361,<br>23362, 23363, 23364, 23365, 23378, 23379, 23381,<br>23382, 23384, 23404, 23419, 23422, 23424, 23425,<br>23500, 23501, 23502, 23503, 23504, 23506, 23594,<br>23693, 23694, 23696, 23701, 23706, 23711, 23732,<br>23736, 23737, 23738, 23776, 23842, 23923, 23993,<br>24023, 24033, 24043, 24049, 24133, 24135, 24137,<br>24138, 24139, 24141, 24142, 24143, 24146, 24147,<br>24149, 24150, 24151, 24153, 24177, 24181, 24231,<br>24232, 24330, 24331, 24332, 24410, 24411, 24418,<br>24419, 24478, 24483, 24515, 24531, 24599, 24601,<br>24602, 24614, 24618, 24619, 24621, 24623, 24624,<br>24625, 24627, 24630, 24639, 24645, 24646, 24655,<br>24656, 24657, 24659, 24660, 24669, 24681, 24717,<br>24769, 24776, 24789, 24808, 24809, 24838, 24844,<br>24850, 24867, 24868, 24893, 24894, 24895, 25028,<br>25029, 25040, 25042, 25053, 25055, 25111, 25112,<br>25120, 25139, 25140, 25141, 25142, 25143, 25148,<br>25149, 25150, 25157, 25166, 25209, 25240, 25278,<br>25282, 25299, 25428, 25443, 25479, 25498, 25511,<br>25512, 25525, 25585, 25617, 25632). To account for<br>the Channel Sounding feature of Core v6.0, added<br>references to Core v6.0 Vol. 6 Part A and Vol. 6<br>Part F; added Channel Sounding to the TC feature<br>naming conventions table; updated the “Common test<br>case conditions and parameters” section; added new<br>sections for “Default Frequencies”, “Channel<br>Sounding Default Frequencies”, and “Common<br>Parameters and Variables” (with subsections); added<br>new subsections for TRM TCs (new TCs<br>RFPHY/TRM/CS/BV-01-C – -10-C) and a new section<br>for TRM-RCV TCs (new TCs RFPHY/TRM-<br>RCV/CS/BV-01-C – -18-C) and updated the TCMT<br>accordingly; added a new section to the Test Setup<br>Examples section for Channel Sounding setup; and<br>added a new subsection to the Appendix for Test<br>Filter Characteristics.<br>Incorporated Test Issues 24727, 25785, 25798,<br>25850.<br>TSE 25482 (rating 1): Performed editorial updates<br>throughout the TCMT.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **96 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 26029 (rating 2): Updated the TCMT to remove<br>RFPHY 1/1 and RFPHY 1/2 from the Channel<br>Sounding section (now covered by the revised<br>prerequisite to Table 3 in the ICS).|
|22|p22|2024-09-04|Approved by BTI on 2024-08-14. Prepared for<br>TCRL 2024-2publication.|
||p22ed2r00–<br>r03_BTI|2024-10-29 –<br>2024-11-01|TSE 26134 (rating 1): Updated the drawing used for<br>Figures 4.2, 4.3, and 4.8.<br>TSE 26208 (rating 1): Corrected an equation in the<br>test procedure for the section containing<br>RFPHY/TRM-RCV/CS/BV-04-C – -10-C.<br>TSE 26209 (rating 1): Corrected test steps for the<br>section containing RFPHY/TRM-RCV/CS/BV-11-C – -<br>18-C.<br>TSE 26312 (rating 1): Corrected the Subevent_Len<br>value in the Channel Sounding Test Command<br>Parameters table.<br>TSE 26331 (rating 1): Corrected the test procedure for<br>the section containing RFPHY/TRM/CS/BV-03-C and<br>-04-C.<br>TSE 26424 (rating 1): Per E26162, updated<br>“antennas” to “antennae” globally in running text.<br>TSE 26546 (rating 1): Moved the “Test Setup<br>Examples” section to earlier in the document with<br>other common test case conditions and updated<br>wordingas necessary.|
||p22 edition 2|2024-11-12|Approved by BTI on 2024-11-12. Prepared for<br>edition 2publication.|
||p23r00–r04|2024-11-12 –<br>2024-11-25|TSE 25993 (rating 2): Added cross-references to the<br>Test Equipment Setup section in the initial condition<br>section for several Channel Sounding test groups.<br>Updated Channel Sounding TCMT entries as<br>necessary.<br>TSE 26020 (rating 4): Updated the test procedure for<br>RFPHY/TRM/CS/BV-01-C and -02-C. Updated the<br>initial conditions and combined the Role and PHY<br>columns in the TC configuration table in the Channel<br>Sounding Phase Measurement Accuracy section.<br>Updated the TCID descriptions for RFPHY/TRM-<br>RCV/CS/BV-11-C – -18-C, added new TCs<br>RFPHY/TRM-RCV/CS/BV-19-C – -34-C, and updated<br>the TCMT accordingly.<br>TSE 26206 (rating 1): Updated a test step in the<br>section containing RFPHY/TRM-RCV/CS/BV-01-C, -<br>02-C, and -03-C.<br>TSE 26300 (rating 1): Updated the initial condition in<br>the CS Phase Measurement Accuracy section and<br>corrected an IXIT value in the Test Equipment Setup<br>for Channel Sounding section.<br>TSE 26327 (rating 2): Corrected the TCMT entries for<br>RFPHY/TRM-RCV/CS/BV-05-C and RFPHY/TRM-<br>RCV/CS/BV-15-C to account for a removed ICS item.|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **97 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Publication**<br>**Number**|**Revision**<br>**Number**|**Date**|**Comments**|
|---|---|---|---|
||||TSE 26600 (rating 1): Updated test doc title to better<br>align with the associated spec.<br>TSE 26749 (rating 1): Deleted extraneous text from<br>the end of Appendix 6.7.1, Maximum Number of<br>Packets for IQ CoherencyMeasurements.|
|23|p23|2025-02-18|Approved by BTI on 2024-12-26. Prepared for<br>TCRL 2025-1publication.|
||p23ed2<br>r00–r01|2025-06-03 –<br>2025-06-14|TSE 27168 (rating 1): Corrected the MSC for “CS<br>2Ms/s BT = 2.0 frequency deviation measurement<br>principle for 11110000-payload sequence”.<br>TSE 27584 (rating 1): Updated editorially for<br>consistent use of mathematical expressions/symbols<br>throughout TS.<br>TSE 27608 (rating 1): Corrected a spacing issue in<br>the equation for the “PER Test Definition” section.<br>TSE 27614 (rating 1): Corrected subscript issues in<br>the section containing RFPHY/TRM/BV-03-C and<br>-08-C.|
||p23 edition 2|2025-06-25|Approved by BTI on 2025-06-22. Prepared for<br>edition 2publication.|
||p24r00–r02|2025-07-30 –<br>2025-08-14|TSE 17193 (rating 2): Updated the test procedure and<br>a related figure for the section containing<br>RFPHY/RCV/BV-05-C, -11-C, -17-C, and -23-C.<br>TSE 25828 (rating 1): Removed text regarding air<br>humidity.<br>TSE 27158 (rating 3): Added an IXIT value to the<br>initial condition and test steps of the section<br>containing RFPHY/TRM/CS/BV-05-C – -10-C.<br>TSE 27633 (rating 2): Updated the TCMT entries for<br>RFPHY/TRM-RCV/CS/BV-19-C, -21-C, -23-C, -25-C,<br>-27-C, -29-C, -31-C, and -33-C.<br>TSE 27737 (rating 3): Added a reference to Core v6.0<br>Volume 6 Part H. Updated the initial condition and test<br>steps of the section containing RFPHY/TRM-<br>RCV/CS/BV-11-C – -34-C.|
|24|p24|2025-11-04|Approved by BTI on 2025-10-05. Prepared for TCRL<br>pkg101publication.|
||p24ed2r00|2025-11-14|TSE 28403 (rating 1): Corrected TCMT entries to<br>include “OR RFPHY 1/3” when “RFPHY 1 1 AND<br>RFPHY 1 2” arepresent.|
||p24ed2|2025-11-17|Approved by BTI on 2025-11-17. Prepared for<br>edition 2publication.|



## _**Acknowledgments**_ 

|**Name**|**Company**|
|---|---|
|Nils Schapmann|7 Layers|
|Edward Harrison|Anritsu|
|Juan Manuel Hidalgo Perdiguero|AT4 wireless|
|Ángel Romero|AT4 wireless|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **98 of 99** 

**LE Radio Physical Layer (RFPHY)  /** Test Suite 

|**Name**|**Company**|
|---|---|
|Totti Huang|Attestation of Global Compliance(Shenzhen)Co., Ltd.|
|Alexandru Andreescu|Bluetooth SIG, Inc.|
|Norbert Grünert|Broadcom|
|Zhang Zhiwei|China Academy of Information and Communications<br>Technology|
|Peter Flittner|CSR|
|Magnus Sommansson|CSR|
|Steven Wenham|CSR|
|Ole Myrtue|Nokia|
|Jukka Reunamaki|Nokia|
|Frank Karlsen|Nordic Semiconductor A/S|
|Miles Smith|Nordic Semiconductor A/S|
|Tor Ø. Vedal|Nordic Semiconductor A/S|
|Dave Richter|Qualcomm|
|Magnus Sommansson|Qualcomm|
|Peter Dziwior|Rohde & Schwarz|
|Kenton Payne|Rohde & Schwarz|
|Clive Feather|Samsung|
|Rogier Schaeffer|ST Microelectronics|
|Paul vanOostende|ST Microelectronics|
|Karim Sharf|Teledyne LeCroy|
|Øystein Bjørndal|Texas Instruments|



**==> picture [17 x 23] intentionally omitted <==**

Bluetooth SIG Proprietary 

Page **99 of 99** 

