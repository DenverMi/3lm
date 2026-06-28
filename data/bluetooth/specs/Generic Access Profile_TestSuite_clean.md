## Generic Access Profile (GAP)

## Bluetooth ® Test Suite

- Revision: GAP.TS.p50
- Revision Date: 2026-05-05

## 1 Scope

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Generic Access Profile (GAP) layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers ' Bluetooth devices.

## 2 References, definitions, and abbreviations

## 2.1 References

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

## 2.2 Definitions

In this Bluetooth document, the definitions from [1], [4], and [5] apply.

Certain terms that were identified as inappropriate have been replaced. For a list of the original terms and their replacement terms, see the Appropriate Language Mapping Tables document [16].

## 2.3 Acronyms and abbreviations

In this Bluetooth document, the definitions, acronyms, and abbreviations from [1], [4], and [5] apply.

## 3 Test Suite Structure (TSS)

## 3.1 Test Strategy

The test objectives are to verify the functionality of the Generic Access Profile within a Bluetooth Host and enable interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory and optional requirements in the specification and matches these to the support of the IUT as described in the ICS. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test Case Mapping Table (TCMT) evaluates to true.

The test equipment provides an implementation of the Radio Controller and the parts of the Host needed to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT's peer device and interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement similar capabilities to communicate with the test equipment. For some test cases, it is necessary to stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface, a Man Machine Interface (MMI), or another interface supported by the IUT.

This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with catalogued specification requirements that were logically grouped and assessed for testability enabling coverage in defined test purposes.

## 3.2 Test groups

The Test Suite Structure is a tree with the first level representing the protocol groups that apply to the device types defined by the Generic Access Profile.

The second level separates the protocol services in functional modules. The last level in each branch contains the standard ISO subgroups BV and BI.

## 3.2.1 BR/EDR Protocol groups

## 3.2.1.1 Modes

This group handles testing of the modes for discoverability, connectability, and pairability, and synchronizability of a Bluetooth device.

## 3.2.1.2 Security Aspects

This group handles testing of the GAP security aspects.

## 3.2.1.3 Idle mode procedures

This group handles testing of the different Idle mode procedures.

## 3.2.1.4 Establishment procedures

This group handles testing of the different establishment procedures as defined in GAP.

## 3.2.2 LE Only Protocol groups

## 3.2.2.1 Broadcasting and Observing

This group handles testing of the broadcasting and observing modes and procedures of a LE-only device.

## 3.2.2.2 Discovery modes and procedures

This group handles testing of the discovery modes and procedures of a LE-only device.

## 3.2.2.3 Connection modes and procedures

This group handles testing of the connection modes and procedures of a LE-only device.

## 3.2.2.4 Bonding modes and procedures

This group handles testing of the bonding modes and procedures of a LE-only device.

## 3.2.2.5 Security Aspects

This group handles testing of the security aspects for a LE-only device.

## 3.2.2.6 Advertising and Scan Response Data Format

This group handles testing of the advertising and scan response data format of a LE-only device.

## 3.2.2.7 Generic Access Profile Characteristics for Low Energy

This group handles testing of the GAP characteristics of a LE-only device.

## 3.2.2.8 Discovery of Devices with Resolvable Private Address

This group handles testing of the discovery of devices with Resolvable Private Addresses of a LE-only device.

## 3.2.2.9 Periodic Advertising modes and procedures

This group handles testing of the periodic advertising modes and procedures of an LE-only device.

## 3.2.2.10 Broadcast Isochronous Streaming modes and procedures

This group handles testing of the Broadcast Isochronous Streaming modes and procedures of an LEcapable device. The test cases found in this group are based on the Generic Access Profile.

## 3.2.2.11 Connection Subrating procedure

This group handles testing of the Connection Subrating procedure of an LE-only device.

## 3.2.2.12 Scanning Advertisement

This group handles testing of scanning advertisements on a LE-only device.

## 3.2.2.13 Channel Sounding

This group handles testing of the Channel Sounding feature.

## 3.2.3 BR/EDR/LE (Dual Mode) Protocol groups

## 3.2.3.1 Modes

This group handles testing of the modes for discoverability, connectability, and pairability, and synchronizability of a BR/EDR/LE device.

## 3.2.3.2 Idle mode procedures

This group handles testing of the different Idle mode procedures for a BR/EDR/LE device.

## 3.2.3.3 Establishment procedures

This group handles testing of the different establishment procedures for a BR/EDR/LE device.

## 3.2.3.4 BR/EDR/LE security aspects

This group handles testing of the security aspects for a BR/EDR/LE device.

## 3.2.4 Main test groups

## 3.2.4.1 Valid Behavior (BV) Tests

This subgroup provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt or exchange of valid Protocol Data Units (PDUs). Valid PDUs means that the exchange of messages and the content of the exchanged messages are considered as valid.

## 3.2.4.2 Invalid Behavior (BI) Tests

This subgroup provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt of a syntactically or semantically invalid PDU.

## 4 Test cases (TC)

## 4.1 Introduction

## 4.1.1 Test case identification conventions

Test cases are assigned unique identifiers per the conventions in [5]. The convention used here is: &lt;spec abbreviation&gt;/&lt;IUT role&gt;/ &lt;class&gt;/ &lt;feat&gt; /&lt;func&gt;/&lt;subfunc&gt;/&lt;cap&gt;/ &lt;xx&gt;-&lt;nn&gt;-&lt;y&gt; .

| Identifier Abbreviation | Spec Identifier <spec abbreviation> |
| GAP | Generic Access Profile |
| Identifier Abbreviation | Function Identifier <func> |
| ADV | Advertising Data Format |
| BIS | Broadcast Isochronous Streaming modes and procedures |
| BOND | Bonding modes and procedures |
| BROB | Broadcasting and Observing |
| CONN | Connection modes and procedures |
| CS | Channel Sounding |
| CSUB | Connection Subrating procedure |
| DISC | Discovery modes and procedures |
| DM | Dual Mode (BR/EDR/LE) |
| EST | Establishment procedures |
| GAT | Generic Access Profile characteristics |
| IDLE | Idle mode |
| MOD | Modes |
| PADV | Periodic Advertising modes and procedures |
| PRIV | Privacy |
| SCN | Scanner |
| SEC | Security modes and procedures |
| Identifier Abbreviation | Subfunction Identifier <subfunc> |
| AUT | Authentication |
| BBM | Broadcast Isochronous Stream Broadcasting mode |
| BSE | Broadcast Isochronous Stream Synchronization Establishment |
| CON | Connectable mode |
| CSR | Connection Subrate Request |
| CSU | Connection Subrate Response |
| DED | Device Discovery |
| DNDIS | Device Name Discovery |
| GDIS | General Discoverable mode |
| GIN | General Inquiry |
| LDIS | Limited Discoverable mode |
| LIN | Limited Inquiry |

Table 4.1: GAP TC feature naming conventions

| NAD | Name Discovery |
| NBON | Non-bondable mode |
| Identifier Abbreviation | Subfunction Identifier <subfunc> |
| NCON | Non-connectable mode |
| NDIS | Non-discoverable mode |
| NSYN | Non-synchronizable mode |
| PAC | Periodic Advertising Connection |
| PAIR | Pairable mode |
| PAM | Periodic Advertising mode |
| PASE | Periodic Advertising Synchronization Establishment procedure |
| PASM | Periodic Advertising Synchronizability mode |
| PAST | Periodic Advertising Synchronization Transfer procedure |
| RPA | Discovery of Devices with Resolvable Private Address |
| SEM | Security modes |
| SYN | Synchronizable mode |
| SYNE | Synchronization Establishment |

## 4.1.2 Conformance

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

## 4.1.3 Pass/Fail verdict conventions

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met.

The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict.

## 4.2 Preambles

## 4.2.1 Link Establishment Lower Tester Started (for generic authentication)

Figure 4.1: Link Establishment Tester Started (for generic authentication) MSC

Figure 4.2: Inquiry procedure MSC

Figure 4.3: Paging procedure MSC

Figure 4.4: Bring IUT to Link Key Available MSC

Figure 4.5: Secure Simple Pairing MSC

## 4.2.6 GAP Mandatory Characteristics

Figure 4.6: GAP Mandatory Characteristics MSC

## 4.3 Common Packet Contents

## 4.3.1 Fields and Bits Reserved for Future Use

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers.

## 4.4 Modes

Verify the correct implementation of the modes.

## 4.4.1 Non-discoverable bondable mode -Peripheral

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor.

## GAP/MOD/NDIS/BV-01-C [Non-discoverable mode -Peripheral]

- Test Purpose

Verify that the IUT does not respond to inquiry if it is in non-discoverable mode.

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure.

- Reference

## 1 4.1.1

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.

- Test Procedure

Figure 4.7: GAP/MOD/NDIS/BV-01-C [Non-discoverable mode -Peripheral] MSC

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in non-discoverable mode. Every inquiry train is repeated for N=256 times.

- Expected Outcome

## Pass verdict

The IUT does not answer to an inquiry request.

## 4.4.2 Limited Discoverable mode -Peripheral

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor.

## GAP/MOD/LDIS/BV-01-C [Limited Discoverable mode and LIAC -Peripheral]

- Test Purpose

Verify that the IUT answers to inquiry (LIAC) if it is in limited-discoverable mode.

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure.

- Reference

[1] 4.1 (Discoverability modes)

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.

- Test Procedure

Figure 4.8: GAP/MOD/LDIS/BV-01-C [Limited Discoverable mode and LIAC -Peripheral] MSC

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in limited-discoverable mode. Every inquiry train is repeated for N = 256 times.

- Expected Outcome

## Pass verdict

The IUT answers to an inquiry request (LIAC) with the FHS-packet. The Inquiry response message is received by the Lower Tester within TGAP(103).

The COD has the bit number 13 set in the Major Service Class part of the Class of Device field.

## GAP/MOD/LDIS/BV-02-C [Limited Discoverable mode and GIAC -Peripheral]

- Test Purpose

Verify that the IUT answers to inquiry (GIAC) if it is in limited-discoverable mode.

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure.

- Reference

## 1 4.1

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and Idle mode.

- Test Procedure

Figure 4.9: GAP/MOD/LDIS/BV-02-C [Limited Discoverable mode and GIAC -Peripheral] MSC

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in limited-discoverable mode. Every inquiry train is repeated for N = 256 times.

- Expected Outcome

## Pass verdict

The IUT answers to an inquiry request (GIAC) with the FHS-packet. The Inquiry response message is received by the Lower Tester within TGAP(103).

The COD has the bit number 13 set in the Major Service Class part of the Class of Device field.

## GAP/MOD/LDIS/BV-03-C [Limited Discovery mode time-out]

- Test Purpose

Verify that the IUT ceases to answer to inquiry after a time-out, if it is in limited-discoverable mode.

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure.

- Reference

## 4 4.1.2

- Initial Condition
- -The IUT is in Baseband state 'Standby' and in Idle mode.
- -The limited discoverable mode time TGAP is defined by the TSPX\_Tgap\_104 IXIT value.

- Test Procedure
1. The Upper Tester orders the IUT to go in limited-discoverable mode. The Lower Tester waits for TGAP(104) to expire. (TGAP(104) has a default of 1 minute, but an alternate value may be invoked via TSPX\_Tgap\_104.)
2. After TGAP(104) has expired, the Lower Tester sends a series of 256 inquiry request messages (IDpackets) with LIAC. Since the IUT has left the Limited Discoverable mode on the expiration of the timer, it does not respond.
- Expected Outcome

Figure 4.10: GAP/MOD/LDIS/BV-03-C [Limited Discovery mode time-out] MSC

## Pass verdict

The IUT does not answer any inquiry request (LIAC) with an FHS-packet.

## 4.4.3 General Discoverable mode -Peripheral

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor.

## GAP/MOD/GDIS/BV-01-C [General Discoverable mode and GIAC -Peripheral]

- Test Purpose

Verify that the IUT answers to inquiry (GIAC) if it is in general-discoverable mode.

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure.

- Reference

## 1 4.1

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and Idle mode.

- Test Procedure

Figure 4.11: GAP/MOD/GDIS/BV-01-C [General Discoverable mode and GIAC -Peripheral] MSC

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in general-discoverable mode. Every inquiry train is repeated for N=256 times.

- Expected Outcome

## Pass verdict

The IUT answers to an inquiry request (GIAC) with the FHS-packet. The Inquiry response message is received by the Lower Tester within TGAP(103).

## GAP/MOD/GDIS/BV-02-C [General Discoverable mode and LIAC -Peripheral]

- Test Purpose

Verify that the IUT in general-discoverable mode does not respond inquiry requests (using LIAC).

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the inquiry procedure.

- Reference

## 1 4.1

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and Idle mode.

- Test Procedure

Figure 4.12: GAP/MOD/GDIS/BV-02-C [General Discoverable mode and LIAC -Peripheral] MSC

The Lower Tester sends for a time [TGAP(103)] inquiry request messages (ID-packets) after the Upper Tester has ordered the IUT to go in general-discoverable mode. Every inquiry train is repeated for N=256 times.

- Expected Outcome

## Pass verdict

The IUT does not answer to an inquiry request (LIAC).

## 4.4.4 Non-connectable mode -Peripheral

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor.

## GAP/MOD/NCON/BV-01-C [Non-connectable mode -Peripheral]

- Test Purpose

Verify that the IUT does not respond to paging if it is in non-connectable mode.

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the paging procedure.

The BD\_ADDR of the IUT is specified by the TSPX\_bd\_addr\_iut IXIT value.

- Reference

[1] 4.3

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.

- Test Procedure

Figure 4.13: GAP/MOD/NCON/BV-01-C [Non-connectable mode -Peripheral] MSC

The Lower Tester sends for the time max. PageTO paging request messages (ID-packets) after the Upper Tester has ordered the IUT to go in non-connectable mode.

- Expected Outcome

## Pass verdict

The IUT does not answer to paging requests.

- Notes

It must be possible to select a certain BD\_ADDR or CoD for the Lower Tester if necessary.

## 4.4.5 Connectable mode -Peripheral

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor.

## GAP/MOD/CON/BV-01-C [Connectable mode -Peripheral]

- Test Purpose

Verify that the IUT responds to paging requests if it is in connectable mode.

The IUT is Peripheral and acceptor and the Lower Tester is Central and initiator of the paging procedure.

- Reference

[1] 4.3

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.
- -The BD\_ADDR of the IUT is specified by the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Lower Tester sends for the time max. PageTO paging request messages (ID-packets) after the Upper Tester has ordered the IUT to go in connectable mode.
2. The IUT answers to the paging request.
- Expected Outcome

Figure 4.14: GAP/MOD/CON/BV-01-C [Connectable mode -Peripheral] MSC

## Pass verdict

The IUT answers to paging request messages with the paging response message (ID-packet) within PageTO.

- Notes

It must be possible to select a certain BD\_ADDR or CoD for the Lower Tester if necessary.

## 4.4.6 Non-bondable mode -Peripheral

Verify the correct behavior in this mode. The role of the IUT is Peripheral and acceptor.

## GAP/MOD/NBON/BV-02-C [Non-bondable mode, IUT rejects pairing procedure]

## · Test Purpose

Verify that the IUT rejects a pairing procedure, if it is in non-bondable mode.

The IUT is Peripheral and claimant. The Lower Tester is Central and verifier of the pairing procedure.

- Reference

## 1 4.3

- Initial Condition
- -The IUT is in non-bondable mode.
- -Any link keys associated with the IUT and Lower Tester are deleted.
- -The IUT and Lower Tester support Secure Simple Pairing and have set Write Simple Pairing mode to their respective Controllers.
- -The Lower Tester ' s IO capabilities are set to 'DisplayYesNo'.
- -The Lower Tester ' s Authentication\_Requirements are set to ' MITM Protection Not Required -Dedicated Bonding. Numeric comparison with automatic accept allowed. ' (0x02).
- -The IUT is in a connectable state.
- Test Procedure
1. The Lower Tester establishes a connection to the IUT and initiates a secure simple pairing procedure. The Lower Tester 's IO capabilities are set to 'DisplayYesNo' and the Authentication\_Requirements are set to ' MITM Protection Not Required -Dedicated Bonding. Numeric comparison with automatic accept allowed. ' (0x02).
2. The IUT in non-bondable mode responds negatively to the IO capability request where the Lower Tester's Authentication\_Requirements parameter requests dedicated bonding.

Figure 4.15: GAP/MOD/NBON/BV-02-C [Non-bondable mode, IUT rejects pairing procedure] MSC

- Expected Outcome

## Pass verdict

The IUT in non-bondable mode does not accept the pairing request from the Lower Tester where the Authentication\_Requirements parameter requests dedicated bonding. Secure Simple Pairing does not complete with dedicated bonding.

## GAP/MOD/NBON/BV-03-C [Non-bondable mode, IUT accepts a non-bonded connection]

- Test Purpose

Verify that the IUT accepts a non-bonded connection when it is in non-bondable mode.

The IUT is Peripheral and claimant. The Lower Tester is Central and verifier of the pairing procedure.

- Reference

[1] 4.3

- Initial Condition
- -The IUT is in non-bondable mode.
- -An ACL connection exists between the IUT and Lower Tester.
- -The IUT and Lower Tester support Pairing and have set Write Simple Pairing mode to their respective Controllers.
- -The Lower Tester's IO capabilities are set to 'DisplayYesNo'.
- -The Lower Tester ' s Authentication\_Requirements are set to ' MITM Protection Not Required -No Bonding ' (0x00).
- Test Procedure
1. The Lower Tester establishes a connection to the IUT and initiates a secure simple pairing procedure. The Lower Tester's IO capabilities are set to 'DisplayYesNo' and the Authentication\_Requirements are set to 'MITM Protection Not Required No Bonding' (0x00).
2. The IUT in nonbondable mode accepts the IO capability request where the Lower Tester's Authentication\_Requirements parameter requests no bonding and secure simple pairing is successful.

Figure 4.16: GAP/MOD/NBON/BV-03-C [Non-bondable mode, IUT accepts a non-bonded connection] MSC

- Expected Outcome

## Pass verdict

The Secure Simple Pairing procedure is completed successfully.

## 4.4.7 Pairing mode -Peripheral

## 4.4.8 Non-synchronizable mode -Connectionless Peripheral Broadcaster

Verify the correct behavior in this mode. The role of the IUT is connectionless Peripheral broadcast transmitter.

## GAP/MOD/NSYN/BV-01-C [Non-synchronizable mode, IUT is Connectionless Peripheral Broadcast Transmitter]

- Test Purpose

Verify that the IUT does not send the synchronization train if it is in non-synchronizable mode. The IUT is the connectionless Peripheral broadcast transmitter and the Lower Tester is the connectionless Peripheral broadcast receiver.

- References

[9] 4.4.1

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.
- -The BD\_ADDR of the IUT is specified by the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure

The Lower Tester scans for Sync\_Scan\_Timeout = 10.12 seconds for the synchronization train after the Upper Tester has ordered the IUT to go in non-synchronizable mode.

Figure 4.17: GAP/MOD/NSYN/BV-01-C [Non-synchronizable mode, IUT is Connectionless Peripheral Broadcast Transmitter] MSC

- Expected Outcome

## Pass verdict

The Lower Tester is unable to synchronize to the IUT.

## 4.4.9 Synchronizable mode -Connectionless Peripheral Broadcaster

Verify the correct behavior in this mode. The role of the IUT is connectionless Peripheral broadcast transmitter.

## GAP/MOD/SYN/BV-01-C [Synchronizable mode -IUT is Connectionless Peripheral Broadcast Transmitter]

- Test Purpose

Verify that the IUT transmits the Synchronization Train when it is in Synchronizable mode. The IUT is the connectionless Peripheral broadcast transmitter and the Lower Tester is the connectionless Peripheral broadcast receiver.

- References

## 9 4.4.2

- Initial Condition
- -The IUT is in Standby state.
- Test Procedure
1. The Upper Tester configures the Synchronization Train on the IUT with Interval = 80 ms, Timeout = 120 seconds, and Service\_Data = 0x01.
2. The Upper Tester reserves LT\_ADDR=1 on the IUT and enables a Connectionless Peripheral Broadcast on the IUT using the reserved LT\_ADDR with Interval = 80 ms.
3. The Upper Tester places the IUT in Synchronizable mode.
4. The Lower Tester receives the Synchronization Train from the IUT.

Figure 4.18: GAP/MOD/SYN/BV-01-C [Synchronizable mode -IUT is Connectionless Peripheral Broadcast Transmitter] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives the Synchronization Train from the IUT in accordance with the configuration via the Upper Tester.

## 4.5 Security aspects

Verify the correct implementation of the modes, behavior, and procedures of the IUT.

## 4.5.1 BR/EDR security modes -Peripheral

Verify the correct behavior in BR/EDR security modes. The role of the IUT is Peripheral and acceptor.

## GAP/SEC/SEM/BV-02-C [Channel Establishment procedure -Security mode 2]

- Test Purpose

Verify that the IUT in security mode 2 performs a channel establishment procedure.

The IUT is responder. The Lower Tester is initiator of the channel establishment procedure.

- Reference

[1] 5.2

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode. The IUT has to be configured such that it will not reject the channel establishment procedure.
- -The BD\_ADDR of the IUT is specified by the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. After the Upper Tester has ordered the IUT to go in connectable mode, the Lower Tester starts the link establishment with paging.
2. If the link establishment was completed, a channel establishment is performed.
- Expected Outcome

Figure 4.19: GAP/SEC/SEM/BV-02-C [Channel Establishment procedure -Security mode 2] MSC

## Pass verdict

After the link establishment is completed and a channel establishment was initiated by the Lower Tester (with L2CAP\_CONNECTION\_REQ), the IUT sends the L2CAP\_CONNECTION\_RSP message with the result: ' Connection successful ' for completion.

- Notes

Recommend to test with connection to protocol/application that requires authentication.

## GAP/SEC/SEM/BV-04-C [Security mode 4 -Responder]

- Test Purpose

Verify that the IUT in security mode 4 performs a channel establishment procedure. The IUT is responder. The Lower Tester is initiator of the channel establishment procedure.

- Reference

[13] 5.2.2

- Initial Condition
- -The IUT is in Idle mode. The IUT has to be configured such that it will not reject the channel establishment procedure.
- -The BD\_ADDR of the IUT is specified by the TSPX\_bd\_addr\_iut IXIT value.

- Test Procedure

Figure 4.20: GAP/SEC/SEM/BV-04-C [Security mode 4 -Responder] MSC

After the Upper Tester has ordered the IUT to go in connectable mode and in security mode 4, the Lower Tester starts the link establishment with paging. If the link establishment was completed, a channel establishment is performed.

- Expected Outcome

## Pass verdict

After the link establishment is completed and a channel establishment was initiated by the Lower Tester (with L2CAP\_CONNECTION\_REQ), the IUT sends the L2CAP\_CONNECTION\_RSP message with the result: ' Connection successful ' for completion.

- Notes

Recommend to test with connection to protocol/application that requires authentication.

## GAP/SEC/SEM/BV-11-C [Secure Connections Only mode BR/EDR transport -IUT Peripheral , responder, Lower Tester doesn't support Secure Connections in Controller]

- Test Purpose

The Lower Tester doesn't support Secure Connections at the Controller level. Verify that the IUT in Secure Connections Only mode rejects a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3 on the IUT. The IUT is Peripheral and responder of the channel establishment procedure.

- Reference

[1] 5.2.2

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX\_psm\_sm4I3 IXIT value.
- -Set the Secure Connections (Controller Support) LMP feature bit on the Lower Tester to 0.
- -The IUT and the Lower Tester are not bonded (neither IUT nor Lower Tester has link keys).
- -ACL connection does not exist between the devices.
- Test Procedure

Figure 4.21: GAP/SEC/SEM/BV-11-C [Secure Connections Only mode BR/EDR Transport -IUT Peripheral, responder, Lower Tester doesn't support Secure Connections in Controller] MSC

1. The Upper Tester puts the IUT in Secure Connections Only mode and connectable mode.
2. The Lower Tester creates an ACL connection with the IUT.
3. The Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption. The IUT is allowed to reject this pairing procedure. If the IUT rejects the pairing procedure then the test case ends there.
4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3.
- Expected Outcome

## Pass verdict

The IUT rejects the pairing procedure OR

The pairing procedure succeeds and the IUT then rejects the Lower Tester's request to establish a channel to access a service on the IUT that requires security mode 4 level 3 OR

The IUT disconnects the ACL connection with error code 0x05 (Authentication Failure).

- Notes

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4.

## GAP/SEC/SEM/BV-12-C [Secure Connections Only mode BR/EDR transport -IUT Peripheral , responder, Lower Tester doesn't support Secure Connections in Host]

- Test Purpose

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT in Secure Connections Only mode rejects a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3. The IUT is Peripheral and responder of the channel establishment procedure.

- Reference

## 1 5.2.2

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).
- -An ACL connection does not exist between the devices.

## · Test Procedure

Figure 4.22: GAP/SEC/SEM/BV-12-C [Secure Connections Only mode BR/EDR transport -IUT Peripheral, responder, Lower Tester doesn't support Secure Connections in Host] MSC

1. The Upper Tester puts the IUT in Secure Connections Only mode and connectable mode.
2. The Lower Tester creates an ACL connection with the IUT.
3. The Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption. The IUT is allowed to reject this pairing procedure. If the IUT rejects the pairing procedure then the test case ends there.
4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3.
- Expected Outcome

## Pass verdict

The IUT rejects the pairing procedure OR

The pairing procedure succeeds and the IUT then rejects the Lower Tester's request to establish a channel to access a service on the IUT that requires security mode 4 level 3 OR

The IUT disconnects the ACL connection with error code 0x05 (Authentication Failure).

- Notes

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4.

## GAP/SEC/SEM/BI-01-C [Security mode 2 BR/EDR Transport, Responder -Invalid Encryption Key Size]

- Test Purpose

Verify that the IUT in security mode 2 rejects channel establishment with an invalid encryption key size.

The Lower Tester is initiator of the channel establishment procedure. The IUT is responder.

- Reference

## 1 5.2

- Initial Condition
- -The Lower Tester is in security mode 2 and thus the IUT operates in security mode 2 during the connection with the Lower Tester.
- -The IUT is configured such that it will not reject the channel establishment procedure for any other reasons.
- -The IUT and Lower Tester are in a connection and have exchanged a link key with the correct level of authentication while pairing in security mode 2, either during this connection or in a previous connection with bonding. Link has not yet been encrypted.
- -The minimum encryption key size supported is defined in the TSPX\_Min\_Encryption\_Key\_Size IXIT parameter.
- -The BD\_ADDR of the IUT is specified by the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure

Figure 4.23: GAP/SEC/SEM/BI-01-C [Security mode 2 BR/EDR Transport, Responder -Invalid Encryption Key Size] MSC

Repeat Steps 1 -4 for each value of the encryption key size (in Step 3) in the range [1, TSPX\_Min\_Encryption\_Key\_Size -1]:

1. Bring the IUT and the Lower Tester into the Initial Condition.
2. The Lower Tester performs a channel establishment procedure for a service requiring security mode 2.
3. The IUT triggers link encryption and the Lower Tester requests an encryption key size equal to the value selected for the current iteration. The IUT may accept the key size or may fail the link encryption procedure.
4. The IUT rejects the channel establishment after link encryption has been completed.
- Expected Outcome

## Pass verdict

For each requested value of the encryption key size that is less than the minimum supported encryption key size, the IUT rejects the channel establishment over the insufficiently encrypted link. Optionally, the IUT also fails the link encryption procedure or terminates the connection.

## 4.5.1.1 Security mode 4, Responder -Invalid Encryption Key Size

- Test Purpose

Verify that the IUT in security mode 4 rejects channel establishment with an invalid encryption key size.

The Lower Tester is initiator of the channel establishment procedure. The IUT is responder.

- Reference

## 1 5.2, 5.2.2.8

- Initial Condition
- -The IUT is in the security mode and level indicated in the test procedure and is configured such that it will not reject the channel establishment procedure for any other reasons.
- -The minimum encryption key size supported is defined in the TSPX\_Min\_Encryption\_Key\_Size IXIT parameter.
- -The BD\_ADDR of the IUT is specified by the TSPX\_bd\_addr\_iut IXIT value.
- Test Case Configuration

| TCID | Security Mode and Level | Minimum Key Size (octets) |
| GAP/SEC/SEM/BI-11-C [Security mode 4 level 1, Responder - Invalid Encryption Key Size] | Security mode 4 level 1 | TSPX_Min_Encryption_Key_Size |
| GAP/SEC/SEM/BI-02-C [Security mode 4 level 2, Responder - Invalid Encryption Key Size] | Security mode 4 level 2 | TSPX_Min_Encryption_Key_Size |
| GAP/SEC/SEM/BI-03-C [Security mode 4 level 3, Responder - Invalid Encryption Key Size] | Security mode 4 level 3 | TSPX_Min_Encryption_Key_Size |

Table 4.2: Security mode 4, Responder -Invalid Encryption Key Size test cases

| TCID | Security Mode and Level | Minimum Key Size (octets) |
| GAP/SEC/SEM/BI-04-C [Security mode 4 level 4, Responder - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 4 | 16 |
| GAP/SEC/SEM/BI-14-C [Security mode 4 level 1, Responder - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 1 | 16 |
| GAP/SEC/SEM/BI-15-C [Security mode 4 level 2, Responder - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 2 | 16 |
| GAP/SEC/SEM/BI-16-C [Security mode 4 level 3, Responder - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 3 | 16 |

- Test Procedure

Figure 4.24: Security mode 4, Responder -Invalid Encryption Key Size MSC

Repeat Steps 1 -5 for each value of the encryption key size (in Step 3) in the range [1, Min\_Key\_Size -1], where Min\_Key\_Size is indicated in Table 4.2, column Minimum Key Size, for each test case.

1. The IUT and the Lower Tester initiate a connection and exchange a link key with the correct level of authentication while pairing in the same security mode and level indicated in the test procedure. The link has not yet been encrypted.

2. Bring the IUT and the Lower Tester into the Initial Condition for the security mode and level indicated in Table 4.2, column Security Mode and Level.
3. The Lower Tester and the IUT perform link encryption, and the Lower Tester requests an encryption key size equal to the value selected for the current iteration.
4. Perform either alternative 4A or 4B depending on the IUT 's behavior.

Alternative 4A (The IUT fails the link encryption procedure):

- 4A.1 The IUT rejects the link encryption.
- 4A.2 The IUT may disconnect the ACL connection with error code 0x05 (Authentication Failure).

Alternative 4B (The Link Encryption procedure completes successfully):

- 4B.1 The Lower Tester requests a channel establishment for a service requiring the same security mode and level as indicated in Step 1.
- 4B.2 The IUT rejects the channel establishment after link encryption has been completed.
5. Unless the IUT disconnected the ACL connection in Step 4A.2, the IUT and the Lower Tester disconnect the ACL connection.
- Expected Outcome

## Pass verdict

For each value of the encryption key size tested, the IUT either fails the link encryption procedure or completes the procedure successfully but rejects the channel establishment over the insufficiently encrypted link.

## GAP/SEC/SEM/BI-05-C [Security mode 2, Initiator -Invalid Key Size]

- Test Purpose

Verify that the IUT in security mode 2 rejects channel establishment with an invalid encryption key size.

The IUT is initiator of the channel establishment procedure. The Lower Tester is responder.

- Reference

[1] 5.2

- Initial Condition
- -The Lower Tester is in security mode 2 and thus the IUT operates in security mode 2 during the connection with the Lower Tester.
- -The IUT and Lower Tester are in a connection and have exchanged a link key with the correct level of authentication while pairing in the same security mode and level indicated in the test procedure, either during this connection or in a previous connection with bonding. Link has not yet been encrypted.
- -The minimum encryption key size supported is defined in the TSPX\_Min\_Encryption\_Key\_Size IXIT parameter.

- Test Procedure

Figure 4.25: GAP/SEC/SEM/BI-05-C [Security mode 2, Initiator -Invalid Key Size] MSC

Repeat Steps 1 -4 for each value of the encryption key size (in Step 3) in the range [1, TSPX\_Min\_Encryption\_Key\_Size -1]:

1. Bring the IUT and the Lower Tester into the Initial Condition.
2. The Upper Tester orders the IUT to perform a channel establishment procedure for a service requiring security mode 2. The IUT initiates link encryption.
3. In the link encryption phase, the Lower Tester requests an encryption key size equal to the value selected for the current iteration. The IUT may accept the key size or may fail the link encryption procedure.
4. The IUT signals to the Upper Tester that the channel establishment failure after link encryption has been completed.
- Expected Outcome

## Pass verdict

For each requested value of the encryption key size that is less than the minimum supported encryption key size, the IUT fails the channel establishment due to the insufficiently encrypted link. Optionally, the IUT also fails the link encryption procedure or terminates the connection.

## 4.5.1.2 Security mode 4, Initiator -Invalid Encryption Key Size

- Test Purpose

Verify that the IUT in security mode 4 rejects channel establishment with an invalid encryption key size.

The IUT is initiator of the channel establishment procedure. The Lower Tester is responder.

- Reference

[1] 5.2

- Initial Condition
- -The IUT is in the security mode and level indicated in the test procedure.
- -The IUT and Lower Tester are in a connection and have exchanged a link key with the correct level of authentication while pairing in the same security mode and level indicated in the test procedure, either during this connection or in a previous connection with bonding. Link has not yet been encrypted.
- -The minimum encryption key size supported is defined in the TSPX\_Min\_Encryption\_Key\_Size IXIT parameter.
- Test Case Configuration

| TCID | Security Mode and Level | Minimum Key Size (octets) |
| GAP/SEC/SEM/BI-12-C [Security mode 4 level 1, Initiator - Invalid Encryption Key Size] | Security mode 4 level 1 | TSPX_Min_Encryption_Key_Size |
| GAP/SEC/SEM/BI-06-C [Security mode 4 level 2, Initiator - Invalid Encryption Key Size] | Security mode 4 level 2 | TSPX_Min_Encryption_Key_Size |
| GAP/SEC/SEM/BI-07-C [Security mode 4 level 3, Initiator - Invalid Encryption Key Size] | Security mode 4 level 3 | TSPX_Min_Encryption_Key_Size |
| GAP/SEC/SEM/BI-08-C [Security mode 4 level 4, Initiator - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 4 | 16 |
| GAP/SEC/SEM/BI-17-C [Security mode 4 level 1, Initiator - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 1 | 16 |
| GAP/SEC/SEM/BI-18-C [Security mode 4 level 2, Initiator - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 2 | 16 |
| GAP/SEC/SEM/BI-19-C [Security mode 4 level 3, Initiator - Invalid Encryption Key Size - 128 bit] | Security mode 4 level 3 | 16 |

Table 4.3: Security mode 4, Initiator -Invalid Encryption Key Size test cases

- Test Procedure

Figure 4.26: Security mode 4, Initiator -Invalid Encryption Key Size MSC

Repeat Steps 1 -4 for each value of the encryption key size (in Step 3) in the range [1, (Min\_Key\_Size -1)], where Min\_Key\_Size is indicated in Table 4.3, column Minimum Key Size, for each test case.

1. Bring the IUT and the Lower Tester into the Initial Condition for the security mode and level indicated in Table 4.3, column Security Mode and Level.
2. The Upper Tester orders the IUT to perform a channel establishment procedure for a service requiring the same security mode and level as indicated in Step 1 and minimum key size indicated in Table 4.3. The IUT initiates link encryption with the Lower Tester.
3. In the link encryption phase, the Lower Tester requests an encryption key size equal to the value selected for the current iteration. The IUT may accept the key size or may fail the link encryption procedure.
4. The IUT signals to the Upper Tester that the channel establishment failure after link encryption has been completed.
- Expected Outcome

## Pass verdict

For each requested value of the encryption key size that is less than the minimum required by the security mode and level under test, the IUT fails the channel establishment due to the insufficiently encrypted link. Optionally, the IUT also fails the link encryption procedure or terminates the connection.

## GAP/SEC/SEM/BI-24-C [Security mode 4, Unencrypted connections rejected -Responder]

- Test Purpose

Verify that the IUT disconnects the connection if the initiating side sends the L2CAP\_CONNECTION\_REQ without first enabling encryption.

- Reference

[13] 5.2.2

- Initial Condition
- -Write\_Authentication\_Enable (disabled) on IUT.
- -Write\_Simple\_Pairing\_Mode is set (enabled) on the Lower Tester acting as responder.
- -The IUT and the Lower Tester are not Bonded.
- Test Procedure
1. The Lower Tester creates an ACL connection with the IUT.
2. The Authentication\_Requirements are set to 'MITM Protection Not Required No Bonding' (0x00) on the Lower Tester.
3. The Lower Tester sends L2CAP\_CONNECTION\_REQ without performing Secure Simple Pairing and without enabling encrypting.
- Expected Outcome

Figure 4.27: Security mode 4, Unencrypted connections rejected -Responder MSC

## Pass verdict

Based on ALT 1 shown in Figure 4.27, the test results in pass when the IUT initiates the Secure Simple Pairing procedure autonomously before the Lower Tester initiates the L2CAP connection. Verify that the IUT authenticates the Lower Tester.

Based on ALT 2 shown in Figure 4.27, the test will result in pass when the IUT rejects the L2CAP connection and disconnects the ACL link with error code authentication failure 0x05.

## 4.5.1.3 Secure Connections Only mode BR/EDR transport -IUT Peripheral, responder, Lower Tester supports Secure Connections in Controller and Host

- Test Purpose

The Lower Tester supports Secure Connections both at the Controller and Host level. Verify that the IUT in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3. The IUT is Peripheral and responder of the channel establishment procedure.

- Reference

[1] 5.2.2

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -Set both the Secure Connections (Controller Support) and the Secure Connections (Host Support) LMP feature bits on the Lower Tester to 1.
- -The IUT and the Lower Tester are bonded as specified in Table 4.4.
- -ACL connection does not exist between the devices.
- Test Case Configuration

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-13-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-47-C | Bonded, Has Link Keys | Generic authentication procedure |

Table 4.4: Secure Connections Only mode -IUT Peripheral, responder, Lower Tester supports Secure Connections in Controller and Host test cases

## · Test Procedure

Figure 4.28: Secure Connections Only mode BR/EDR transport -IUT Peripheral, responder, Lower Tester supports Secure Connections in Controller and Host MSC

1. The Upper Tester puts the IUT in Secure Connections Only mode and connectable mode.
2. The Lower Tester creates an ACL connection with the IUT.
3. If the test requires Secure Simple Pairing, the Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption.
4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3.
- Expected Outcome

## Pass verdict

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester.

The IUT accepts the Lower Tester's request to establish a channel to access a service on the IUT that requires security mode 4 level 3 and the channel establishment procedure is successful.

- Notes

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4.

## 4.5.1.4 IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host

- Test Purpose

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 3. The IUT is Peripheral and responder of the channel establishment procedure.

- Reference

[1] 5.2.2

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 3 is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -The IUT and the Lower Tester are bonded as specified in Table 4.5.
- -ACL connection does not exist between the devices.
- Test Case Configuration

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-14-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-48-C | Bonded, Has Link Keys | Generic authentication procedure |

Table 4.5: IUT Peripheral, responder, not in Secure Connections Only mode, Lower Tester does not support Secure Connections in Host test cases

- Test Procedure
1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode) and connectable mode.
2. The Lower Tester creates an ACL connection with the IUT.
3. If the test requires Secure Simple Pairing, the Lower Tester performs the Secure Simple Pairing procedure that results in an authenticated link key and enables encryption.
4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 3.
- Expected Outcome

Figure 4.29: IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host MSC

## Pass verdict

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester.

The IUT accepts the Lower Tester's request to establish a channel to access a service on the IUT that requires security mode 4 level 3 and the channel establishment procedure is successful.

## 4.5.1.5 IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service

- Test Purpose

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode rejects a request to perform a channel establishment procedure over the BR/EDR transport if the service on the IUT requires security mode 4 level 4. The IUT is Peripheral and responder of the channel establishment procedure.

- Reference

[1] 5.2.2

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX\_psm\_sm4l4 IXIT value.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -IUT and Lower Tester are bonded as specified in Table 4.6.
- -ACL connection does not exist between the devices.
- Test Case Configuration

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-15-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-49-C | Bonded, Has Link Keys | Generic authentication procedure |

Table 4.6: IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service test cases

## · Test Procedure

Figure 4.30: IUT Peripheral, responder, not in Secure Connections Only mode BR/EDR Transport, Lower Tester does not support Secure Connections in Host, level 4 service MSC

1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode) and connectable mode.
2. The Lower Tester creates an ACL connection with the IUT.
3. The Lower Tester performs the Secure Simple Pairing procedure that results an authenticated link key and enables encryption.
4. The Lower Tester requests establishing a channel to access a service on the IUT that requires security mode 4 level 4.
- Expected Outcome

## Pass verdict

If the test requires Secure Simple Pairing, the Secure Simple Pairing procedure between the IUT and the Lower Tester is successful.

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester.

The IUT rejects the Lower Tester's request to establish a channel to access a service on the IUT that requires security mode 4 level 4.

## 4.5.2 LE security modes -Peripheral

Verify the correct behavior in LE security modes. The role of the IUT is Peripheral.

## 4.5.2.1 LE Secure Connections, Peripheral -outgoing service level connection

- Test Purpose

Verify that the IUT, supporting LE Secure Connections, performing the authentication procedure will achieve a connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Peripheral.

- Reference

[9] 10.3

- Initial Condition
- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The Lower Tester will establish a GATT service request when TSPX\_Use\_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel.
- Test Case Configuration
- Test Procedure
1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.7.
2. The Upper Tester configures the IUT to advertise (in Peripheral role) for a connection by the Lower Tester (in Central role), and accept link establishment.
3. The Upper Tester triggers the authentication procedure on the IUT, e.g., by an L2CAP channel establishment or a GATT service request.
4. The IUT begins LE Secure Connections Phase 1 by sending an SMP Security Request, with the Secure Connections bit set to 1. The Lower Tester responds with an SMP Pairing Request, with the Secure Connections bit set to 1. The IUT answers with SMP Pairing Response, with the Secure Connections bit set to 1.
5. The Lower Tester and the IUT complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
6. The IUT replies with a successful response.

Table 4.7: LE Secure Connections, Peripheral -outgoing service level connection test cases

| TCID | Security Mode and Level |
| GAP/SEC/SEM/BV-21-C [LE security mode: mode 1 level 4, Peripheral - outgoing service level connection] | LE security mode 1 level 4 |
| GAP/SEC/SEM/BV-37-C [LE Secure Connections Only: mode 1 level 2, Peripheral - outgoing service level connection] | LE security mode 1 level 2 |
| GAP/SEC/SEM/BV-38-C [LE Secure Connections Only: mode 1 level 3, Peripheral - outgoing service level connection] | LE security mode 1 level 3 |

Figure 4.31: LE Secure Connections, Peripheral -outgoing service level connection MSC

## · Expected Outcome

## Pass verdict

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted and operating in the security mode and level specified in Table 4.7.

## · Notes

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.7.

## 4.5.2.2 LE Secure Connections, Peripheral -incoming service level connection

## · Test Purpose

Verify that the IUT, supporting LE Secure Connections, after performing the authentication procedure will achieve an incoming service level connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Peripheral.

- Reference

[9] 10.3.1

- Initial Condition
- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The Lower Tester will establish a GATT service request when TSPX\_Use\_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel.
- Test Case Configuration

Table 4.8: LE Secure Connections, Peripheral -incoming service level connection test cases

| TCID | Security Mode and Level |
| GAP/SEC/SEM/BV-22-C [LE security mode: mode 1 level 4, Peripheral - incoming service level connection] | LE security mode 1 level 4 |
| GAP/SEC/SEM/BV-39-C [LE Secure Connections Only: mode 1 level 2, Peripheral - incoming service level connection] | LE security mode 1 level 2 |
| GAP/SEC/SEM/BV-40-C [LE Secure Connections Only: mode 1 level 3, Peripheral - incoming service level connection] | LE security mode 1 level 3 |

## · Test Procedure

1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.8.
2. The Upper Tester configures the IUT to advertise (in Peripheral role) for a connection by the Lower Tester (in Central role), and accept link establishment.
3. The Lower Tester initiates LE Secure Connections pairing according to the security mode and level specified in Table 4.8.
4. The Lower Tester and the IUT complete SMP Phase 1, Phase 2 (pairing), and Phase 3 (encryption and key distribution).
5. The Lower Tester sends either an L2CAP channel establishment or GATT service request to the IUT.
6. The IUT replies with a successful response.

Figure 4.32: LE Secure Connections, Peripheral -incoming service level connection MSC

- Expected Outcome

## Pass verdict

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted on the security mode and level specified in Table 4.8.

The initiated procedure is successful.

- Notes

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.8.

## GAP/SEC/SEM/BV-23-C [Secure Connections Only mode LE transport -failed procedure, Peripheral -outgoing service level connection]

- Test Purpose

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only initiating the authentication procedure will result in a failed procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Peripheral.

- Reference

[9] 10.2.4, 10.3

- Initial Condition
- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The Lower Tester is configured so that it does not support LE Secure Connections.
- -The IUT will initiate a GATT service request when TSPX\_Use\_GATT is set to TRUE. Otherwise, the IUT will establish an L2CAP channel.
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

Figure 4.33: GAP/SEC/SEM/BV-23-C [Secure Connections Only mode LE transport -failed procedure, Peripheral -outgoing service level connection] MSC

- Expected Outcome

## Pass verdict

In ALT 1, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1.

In ALT 2, the IUT does not complete the L2CAP Channel establishment or GATT service request.

## GAP/SEC/SEM/BV-24-C [Secure Connections Only mode LE transport -failed procedure, Peripheral -incoming service level connection]

## · Test Purpose

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only rejects an L2CAP channel establishment or GATT service request both before and after the authentication procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Peripheral.

- Reference

[9] 10.2.4, 10.3.1

## · Initial Condition

- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject a correctly initiated procedure to either establish an L2CAP channel or a GATT service request.
- -The Lower Tester is configured so that it does not support LE Secure Connections.
- -The Lower Tester will establish a GATT service request when TSPX\_Use\_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel.

## · Test Procedure

1. The Upper Tester configures the IUT into Secure Connections Only mode or to only support LE Secure Connections.
2. The Upper Tester configures the IUT (in Peripheral role) to send advertising packets to the Lower Tester (in Central role), and complete link establishment with the Lower Tester.
3. The Lower Tester initiates either an L2CAP channel establishment or GATT service request to the IUT.
4. The IUT rejects the request.
5. The Lower Tester initiates authenticated LE Legacy pairing.
6. Alternative 1: The IUT rejects the pairing by sending an SMP Pairing Failed message. Alternative 2: The Lower Tester and the IUT complete LE legacy pairing. The Lower Tester reinitiates the procedure request to the IUT as attempted in Step 3. The IUT rejects the request.

Figure 4.34: GAP/SEC/SEM/BV-24-C [Secure Connections Only mode LE transport -failed procedure, Peripheral -incoming service level connection] MSC

- Expected Outcome

## Pass verdict

The L2CAP channel establishment or GATT service request is rejected before the authentication procedure.

Alternative 1: IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1.

Alternative 2: The IUT and the Lower Tester complete LE legacy pairing and the IUT rejects the initiated procedure request from the Lower Tester with the error code 'Insufficient Authentication' .

## GAP/SEC/SEM/BV-25-C [Secure Connections Only mode LE transport, Peripheral, Failure, BR/EDR and LE transports]

- Test Purpose

Verify that the IUT in Secure Connections Only mode performs either an L2CAP channel establishment or GATT service request procedure over LE and a channel establishment procedure over BR/EDR. The IUT is initiator of the procedure over both LE and BR/EDR. The Lower Tester supports neither LE Secure Connections nor BR/EDR Secure Connections. The procedure fails over both LE and BR/EDR. The IUT is the Peripheral.

- Reference

[9] 10.2.4

- Initial Condition
- -The IUT supports both LE Secure Connections and BR/EDR Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The Lower Tester is configured so that it does not support LE Secure Connections and BR/EDR Secure Connections.
- -The PSM for the service on the IUT that requires security mode 4 level 3 on BR/EDR is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -The IUT and the Lower Tester are not bonded on BR/EDR (neither the IUT nor the Lower Tester has link keys).
- -A BR/EDR ACL connection does not exist between the devices.
- Test Procedure
1. The Upper Tester configures the IUT into Secure Connections Only mode.
2. The Upper Tester configures the IUT (in Peripheral role) to send advertising packets to the Lower Tester (in Central role), and complete link establishment with the Lower Tester.
3. The IUT begins the LE Pairing Procedure Phase 1 by sending an SMP Security Request, with the Secure Connections bit set to 1. The Lower Tester responds with an SMP Pairing Request, with the Secure Connections bit set to 0. The IUT will respond with an SMP Pairing Failed message.
4. The IUT terminates the LE connection.
5. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT.
6. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester.

Figure 4.35: GAP/SEC/SEM/BV-25-C [Secure Connections Only mode LE transport, Peripheral, Failure, BR/EDR and LE Transports] MSC

- Expected Outcome

## Pass verdict

On the LE transport, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1.

On the BR/EDR transport, t he IUT rejects the Upper Tester's request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT.

## 4.5.2.3 LE security mode 1, Peripheral -Invalid Encryption Key Size

- Test Purpose

Verify that the IUT in LE security mode 1 as Peripheral fails pairing when receiving an invalid key size.

- Reference

[9] 10.3.2, 10.2.1

- Initial Condition
- -The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.

- Test Case Configuration
- Test Procedure

Table 4.9: LE security mode 1, Peripheral -Invalid Encryption Key Size test cases

| TCID | Security Mode and Level |
| GAP/SEC/SEM/BI-09-C [LE security mode 1 level 4, Peripheral - Invalid Encryption Key Size] | Security mode 1 level 4 |
| GAP/SEC/SEM/BI-20-C [Security mode 1 level 3, Peripheral - Invalid Encryption Key Size] | Security mode 1 level 3 with LE Secure Connections Pairing only |
| GAP/SEC/SEM/BI-21-C [Security mode 1 level 2, Peripheral - Invalid Encryption Key Size] | Security mode 1 level 2 with LE Secure Connections Pairing only |

Figure 4.36: LE security mode 1, Peripheral -Invalid Encryption Key Size MSC

Repeat Steps 1 -5 for all values of the Maximum Encryption Key Size field (in Step 3) in the interval [7, 15].

1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.9.
2. The Upper Tester configures the IUT to advertise (in Peripheral role) for a connection by the Lower Tester (in Central role), and to accept link establishment.
3. The Lower Tester initiates pairing by sending an SMP Pairing Request, with the Secure Connections bit set to 1 and Maximum Encryption Key Size set to the value selected for this iteration.
4. The IUT sends to the Lower Tester an SMP Pairing Failed with the Reason set to 'Encryption Key Size' (0x06).
5. The Lower Tester terminates the LE connection.
- Expected Outcome

## Pass verdict

The IUT fails pairing for any key size value less than 16 while in the specified security mode and level.

## 4.5.3 BR/EDR security modes -Central

Verify the correct behavior in BR/EDR security modes. The role of the IUT is Central and initiator.

## 4.5.3.1 Security mode 4 -Unauthenticated Link Key -Initiator

- Test Purpose

Verify that the IUT in security mode 4 performs a channel establishment procedure. The Lower Tester is responder. The IUT is initiator of the channel establishment procedure.

- Reference

[13] 5.2.2

- Initial Condition
- -Write\_Authentication\_Enable (disabled) on the IUT.
- -Write\_Simple\_Pairing\_Mode is set (enabled) on the Lower Tester acting as responder.
- -The IUT has link keys as specified in Table 4.10.
- Test Case Configuration
- Test Procedure

Table 4.10: Security mode 4 -Unauthenticated Link Key -Initiator test cases

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-05-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-50-C | Bonded, Has Link Keys | Generic authentication procedure |

Figure 4.37: Security mode 4 -Unauthenticated Link Key -Initiator MSC

1. The IUT creates an L2CAP connection to the Lower Tester.
2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.10.

Alternative 2A (Secure Simple Pairing):

- 2A.1 Set Authentication Requirements to MITM protection not required and no bonding on IUT.
- 2A.2 Set Authentication Requirements to MITM protection not required and no bonding on the Lower Tester.
- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an unauthenticated link key.

Alternative 2B (Generic authentication procedure):

- 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure.
3. The IUT sends an L2CAP\_CONNECTION\_REQ PDU to the Lower Tester.
4. The Lower Tester sends an L2CAP\_CONNECTION\_RSP PDU to the IUT.
- Expected Outcome

## Pass verdict

In Step 2A, verify that secure simple pairing occurs prior to sending the L2CAP\_CONNECTION\_REQ and before the L2CAP\_CONNECTION\_RSP is received, and results in an unauthenticated link key.

In Step 2B, verify that the IUT authenticates the Lower Tester.

Verify that encryption is enabled.

## 4.5.3.2 Security mode 4 -Authenticated Link Key No MITM -Initiator

- Test Purpose

Verify that secure simple pairing occurs prior to sending the L2CAP\_CONNECTION\_REQ and before the L2CAP\_CONNECTION\_RSP is received, and results in an authenticated link key.

- Reference

[13] 5.2.2

- Initial Condition
- -Write\_Authentication\_Enable (disabled) on the IUT.
- -Write\_Simple\_Pairing\_Mode is set (enabled) on the Lower Tester acting as responder.
- -The IUT has link keys as specified in Table 4.11.
- Test Case Configuration

Table 4.11: Security mode 4 -Authenticated Link Key No MITM -Initiator test cases

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-06-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-51-C | Bonded, Has Link Keys | Generic authentication procedure |

## · Test Procedure

Figure 4.38: Security mode 4 -Authenticated Link Key No MITM -Initiator MSC

1. The IUT creates an L2CAP connection to the Lower Tester.
2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.11.

Alternative 2A (Secure Simple Pairing):

- 2A.1 Set Authentication Requirements to MITM protection not required and no bonding on IUT.
- 2A.2 Set Authentication Requirements to MITM protection required and no bonding on the Lower Tester.
- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an authenticated link key.

Alternative 2B (Generic authentication procedure):

- 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure.
3. The IUT sends an L2CAP\_CONNECTION\_REQ PDU to the Lower Tester.
4. The Lower Tester sends an L2CAP\_CONNECTION\_RSP PDU to the IUT.
- Expected Outcome

## Pass verdict

In Step 2A, verify that secure simple pairing occurs prior to sending the L2CAP\_CONNECTION\_REQ and before the L2CAP\_CONNECTION\_RSP is received, and results in an authenticated link key.

In Step 2B, verify that the IUT authenticates the Lower Tester.

Verify that encryption is enabled.

## 4.5.3.3 Security mode 4 -Authenticated Link Key MITM -Initiator

## · Test Purpose

Verify that secure simple pairing occurs before the L2CAP\_CONNECTION\_REQ is sent and results in an authenticated link key.

- Reference

[13] 5.2.2

- Initial Condition
- -Write\_Authentication\_Enable (disabled) on the IUT.
- -Write\_Simple\_Pairing\_Mode is set (enabled) on the Lower Tester acting as responder.
- -The IUT has link keys as specified in Table 4.12.
- Test Case Configuration
- Test Procedure

Table 4.12: Security mode 4 -Authenticated Link Key MITM -Initiator test cases

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-07-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-52-C | Bonded, Has Link Keys | Generic authentication procedure |

Figure 4.39: Security mode 4 -Authenticated Link Key MITM -Initiator MSC

1. The IUT creates an L2CAP connection to the Lower Tester.
2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.12.

Alternative 2A (Secure Simple Pairing):

- 2A.1 Set Authentication\_Requirements to 'MITM Protection Required No Bonding' (0x01) on IUT.
- 2A.2 Set Authentication\_Requirements to 'MITM Protection Not Required No Bonding' (0x00) on the Lower Tester.
- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an authenticated link key.

Alternative 2B (Generic authentication procedure):

- 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure.
3. The IUT sends an L2CAP\_CONNECTION\_REQ PDU to the Lower Tester.
4. The Lower Tester sends an L2CAP\_CONNECTION\_RSP PDU to the IUT.
- Expected Outcome

## Pass verdict

In Step 2A, verify that secure simple pairing occurs before the L2CAP\_CONNECTION\_REQ is sent, and results in an authenticated link key.

In Step 2B, verify that the IUT authenticates the Lower Tester.

Verify that encryption is enabled.

## GAP/SEC/SEM/BV-08-C [Security mode 4 -Initiator]

- Test Purpose

Verify that authentication succeeds and occurs before the L2CAP Connection request.

- Reference

[13] 5.2.2

- Initial Condition
- -Write\_Authentication\_Enable (disabled) on the IUT.
- -Write\_Simple\_Pairing\_Mode is set (enabled).
- -Link key is on IUT and responder.

## · Test Procedure

Figure 4.40: GAP/SEC/SEM/BV-08-C [Security mode 4 -Initiator] MSC

The IUT creates L2CAP connection to the Lower Tester.

- Expected Outcome

## Pass verdict

Verify that authentication succeeds and occurs before the L2CAP\_CONNECTION\_REQ. Verify that encryption is enabled.

## 4.5.3.4 Security mode 4 -Link Key Upgrade -Initiator

- Test Purpose

Verify that a link key can be upgraded from unauthenticated to authenticated.

- Reference

[13] 5.2.2

- Initial Condition
- -Write\_Authentication\_Enable (disabled) on the IUT.
- -Write\_Simple\_Pairing\_Mode is set (enabled) on the Lower Tester acting as responder.
- -The IUT has link keys as specified in Table 4.13.
- Test Case Configuration

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-09-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-53-C | Bonded, Has Link Keys | Generic authentication procedure |

Table 4.13: Security mode 4 -Link Key Upgrade -Initiator test cases

## · Test Procedure

Figure 4.41: Security mode 4 -Link Key Upgrade -Initiator MSC

1. The IUT creates an L2CAP connection to the Lower Tester.
2. Perform either alternative 2A or 2B depending on the pairing/authentication procedure specified in Table 4.13.

Alternative 2A (Secure Simple Pairing):

- 2A.1 Set Authentication\_Requirements to 'MITM Protection Not Required No Bonding' (0x00) on the IUT.
- 2A.2 Set Authentication\_Requirements to 'MITM Protection Not Required No Bonding' (0x00) on the responder.
- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an un-authenticated link key.

Alternative 2B (Generic authentication procedure):

- 2B.1 The IUT and the Lower Tester execute the Generic authentication procedure.
3. The IUT initializes a second service to the Lower Tester that requires an authenticated link key.
4. Perform either alternative 4A or 4B depending on the pairing/authentication procedure specified in Table 4.13.

Alternative 4A (Secure Simple Pairing):

- 4A.1 Set Authentication\_Requirements to 'MITM Protection Required No Bonding' (0x01) on the IUT.
- 4A.2 Set Authentication\_Requirements to 'MITM Protection Required No Bonding' (0x01) on the responder.
- 4A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an authenticated link key.

Alternative 4B (Generic authentication procedure):

- 4B.1 The IUT and the Lower Tester execute the Generic authentication procedure.
5. The IUT and the Lower Tester pause and resume encryption.
6. The IUT sends an L2CAP\_CONNECTION\_REQ PDU to the Lower Tester.
7. The Lower Tester sends an L2CAP\_CONNECTION\_RSP PDU to the IUT.
- Expected Outcome

## Pass verdict

In Step 2A, verify that secure simple pairing occurs prior to sending the L2CAP\_CONNECTION\_REQ and before the L2CAP\_CONNECTION\_RSP is received, and results in an unauthenticated link key.

Verify that the IUT authenticates the Lower Tester.

Verify that encryption is enabled.

In Step 4A, on second service initialization, verify that Secure Simple Pairing occurs before the L2CAP\_CONNECTION\_REQ and results in an authenticated link key.

In Step 4B, on second service initialization, verify that the IUT authenticates the Lower Tester.

## 4.5.3.5 Security mode 4 -Responder

- Test Purpose

Verify that the IUT fails and disconnects the connection if the initiating side sends the L2CAP Connection Request as specified in Table 4.14 without first enabling encryption.

- Reference

[17] 5.2.2

- Initial Condition
- -Write\_Authentication\_Enable (disabled) on the IUT.
- -Write\_Simple\_Pairing\_Mode is set (enabled) on the Lower Tester acting as responder.
- -No link key is on the IUT.
- Test Case Configuration

| Test Case ID | L2CAP Command | L2CAP Response | Response Result Code |
| GAP/SEC/SEM/BV-10-C | L2CAP_CONNECTION_REQ | L2CAP_CONNECTION_RSP | 0x0003 |
| GAP/SEC/SEM/BV-46-C | L2CAP_CREDIT_BASED_ CONNECTION_REQ | L2CAP_CREDIT_BASED_ CONNECTION_RSP | 0x0005, 0x0006, 0x0007, 0x0008 |

Table 4.14: Security mode 4 -Responder test cases

## · Test Procedure

Figure 4.42: Security mode 4 -Responder MSC

1. The Lower Tester creates L2CAP connection to the IUT.
2. Perform either alternative 2A or 2B depending on the Connect Request type specified in Table 4.14.

Alternative 2A (Connection Request):

- 2A.1 Set Authentication\_Requirements to 'MITM Protection Not Required No Bonding' (0x00) on the IUT.
- 2A.2 Set Authentication\_Requirements to 'MITM Protection Not Required No Bonding' (0x00) on the responder.
- 2A.3 The IUT and the Lower Tester complete Secure Simple Pairing with an un-authenticated link key.
- 2A.4 The Lower Tester sends the L2CAP command in Table 4.14 to the IUT.
- 2A.5 The IUT sends an L2CAP Response command in Table 4.14 to the Lower Tester.

Alternative 2B (Credit-based Connection Request):

- 2B.1 The Lower Tester sends the L2CAP command in Table 4.14 to the IUT.
- 2B.2 The IUT may send an L2CAP Response command in Table 4.14 to the Lower Tester with Result Pending.
- 2B.3 The IUT sends a Disconnect ACL Link to the Lower Tester with Authentication Failure.
- Expected Outcome

## Pass verdict

Based on ALT 2A shown in Figure 4.42: Security mode 4 -Responder the test results in pass when the IUT initiates the Secure Simple Pairing procedure autonomously before the Lower Tester initiates the L2CAP connection. Verify that the IUT authenticates the Lower Tester.

Based on ALT 2B shown in Figure 4.42: Security mode 4 -Responder the test will result in pass when the IUT rejects the L2CAP connection with the L2CAP Response containing a result code in Table 4.14 and disconnects the ACL link with error code authentication failure 0x05.

## GAP/SEC/SEM/BV-16-C [Secure Connections Only mode -IUT Central, initiator, Lower Tester doesn't support Secure Connections in Controller]

## · Test Purpose

The Lower Tester doesn't support Secure Connections at the Controller level. Verify that the IUT in Secure Connections Only mode rejects a request to perform a channel establishment procedure if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure.

- Reference

## 1 5.2.2

- Initial Condition
- -The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -Set the Secure Connections (Controller Support) LMP feature bit on the Lower Tester to 0.
- -The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).
- -An ACL connection does not exist between the devices.

- Test Procedure
1. The Upper Tester puts the IUT in Secure Connections Only mode.
2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT.
3. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester.
- Expected Outcome

Figure 4.43: GAP/SEC/SEM/BV-16-C [Secure Connections Only mode -IUT Central, initiator, Lower Tester doesn't support Secure Connections in Controller] MSC

## Pass verdict

The IUT rejects the Upper Tester's request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT.

- Notes

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4.

## GAP/SEC/SEM/BV-17-C [Secure Connections Only mode -IUT Central, initiator, Lower Tester doesn't support Secure Connections in Host]

- Test Purpose

The Lower Tester doesn't support Secure Connections at the Host level. Verify that the IUT in Secure Connections Only mode rejects a request to perform a channel establishment procedure if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure.

- Reference

## 1 5.2.2

- Initial Condition
- -The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1.

- -The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).
- -An ACL connection does not exist between the devices.
- Test Procedure
1. The Upper Tester puts the IUT in Secure Connections Only mode.
2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT.
3. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester.
- Expected Outcome

Figure 4.44: GAP/SEC/SEM/BV-17-C [Secure Connections Only mode -IUT Central, initiator, Lower Tester doesn't support Secure Connections in Host] MSC

## Pass verdict

The IUT rejects the Upper Tester's request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT.

- Notes

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4.

## 4.5.3.6 Secure Connections Only mode BR/EDR transport -IUT Central, initiator, Lower Tester supports Secure Connections in Controller and Host

- Test Purpose

The Lower Tester supports Secure Connections both at the Controller and Host level. Verify that the IUT in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure.

- Reference

[1] 5.2.2

- Initial Condition
- -The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -Set both the Secure Connections (Controller Support) and the Secure Connections (Host Support) LMP feature bits on the Lower Tester to 1.
- -The IUT and the Lower Tester are bonded as specified in Table 4.15.
- -An ACL connection does not exist between the devices.
- Test Case Configuration
- Test Procedure

Table 4.15: Secure Connections Only mode BR/EDR transport -IUT Central, initiator, Lower Tester supports Secure Connections in Controller and Host test cases

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-18-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-54-C | Bonded, Has Link Keys | Generic authentication procedure |

Figure 4.45: Secure Connections Only mode BR/EDR transport -IUT Central, initiator, Lower Tester supports Secure Connections in Controller and Host MSC

1. The Upper Tester puts the IUT in Secure Connections Only mode.
2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT.
3. The IUT creates an ACL connection with the Lower Tester.
- Expected Outcome

## Pass verdict

The IUT accepts the Upper Tester's request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT and the channel establishment procedure is successful.

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester.

- Notes

When in Secure Connections Only mode, all services (except those allowed to have security mode 4 level 0) require security mode 4 level 4.

## 4.5.3.7 IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host

- Test Purpose

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode accepts a request to perform a channel establishment procedure over the BR/EDR transport if the service requires security mode 4 level 3 on the IUT. The IUT is Central and initiator of the channel establishment procedure.

- Reference

[1] 5.2.2

- Initial Condition
- -The PSM for the service that requires security mode 4 level 3 on the IUT is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -The IUT and the Lower Tester are bonded as specified in Table 4.16.
- -An ACL connection does not exist between the devices.
- Test Case Configuration

| Test Case | Link Keys | Pairing/Authentication |
| GAP/SEC/SEM/BV-19-C | Not Bonded, No Link Keys | Secure Simple Pairing |
| GAP/SEC/SEM/BV-55-C | Bonded, Has Link Keys | Generic authentication procedure |

Table 4.16: IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host test cases

- Test Procedure
1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode).
2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT.
3. The IUT creates an ACL connection with the Lower Tester.
- Expected Outcome

Figure 4.46: IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host MSC

## Pass verdict

The IUT accepts the Upper Tester's request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT and the channel establishment procedure is successful.

If the test requires the generic authentication procedure, verify that the IUT authenticates the Lower Tester.

## GAP/SEC/SEM/BV-20-C [IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service]

- Test Purpose

The Lower Tester does not support Secure Connections at the Host level. Verify that the IUT that is not in Secure Connections Only mode rejects a request to perform a channel establishment procedure over the BR/EDR transport if the service requires security mode 4 level 4 on the IUT. The IUT is Central and initiator of the channel establishment procedure.

- Reference

[1] 5.2.2

- Initial Condition
- -The PSM for the service that requires security mode 4 level 4 is specified in the TSPX\_psm\_sm4l4 IXIT value.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has link keys).
- -An ACL connection does not exist between the devices.
- Test Procedure
1. The Upper Tester puts the IUT in security mode 4 (but not in Secure Connections Only mode).
2. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 4 on the IUT.
3. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester.

Figure 4.47: GAP/SEC/SEM/BV-20-C [IUT Central, initiator, not in Secure Connections Only mode BR/EDR transport, Lower Tester does not support Secure Connections in Host, level 4 service] MSC

- Expected Outcome

## Pass verdict

The IUT rejects the Upper Tester's request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 4 on the IUT.

## 4.5.4 LE security modes -Central

Verify the correct behavior in LE security modes. The role of the IUT is Central.

## 4.5.4.1 LE Secure Connections, Central -outgoing service level connection

- Test Purpose

Verify that the IUT, supporting LE Secure Connections, after performing the authentication procedure will achieve an outgoing service level connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Central.

- Reference

[10] 2.3.5.6

- Initial Condition
- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The IUT will initiate a GATT service request when TSPX\_Use\_GATT is set to TRUE. Otherwise, the IUT will establish an L2CAP channel.
- Test Case Configuration
- Test Procedure
1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.17.
2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester.
3. The Upper Tester triggers authentication procedure on the IUT, e.g., by an L2CAP channel establishment or a GATT service request.
4. The IUT begins LE Secure Connections Phase 1 by sending an SMP Pairing Request, with the Secure Connections bit set to 1. The Lower Tester answers with SMP Pairing Response, with the Secure Connections bit set to 1.
5. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
6. The Lower Tester replies with a successful response.

Table 4.17: LE Secure Connections, Central -outgoing service level connection test cases

| TCID | Security Mode and Level |
| GAP/SEC/SEM/BV-26-C [LE security mode: mode 1 level 4, Central - outgoing service level connection] | LE security mode 1 level 4 |
| GAP/SEC/SEM/BV-41-C [LE Secure Connections Only: mode 1 level 2, Central - outgoing service level connection] | LE security mode 1 level 2 |
| GAP/SEC/SEM/BV-42-C [LE Secure Connections Only: mode 1 level 3, Central - outgoing service level connection] | LE security mode 1 level 3 |

Figure 4.48: LE Secure Connections, Central -outgoing service level connection MSC

- Expected Outcome

## Pass verdict

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted on the security mode and level specified in Table 4.17.

The initiated procedure is successful.

## · Notes

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.17.

## 4.5.4.2 LE Secure Connections, Central -incoming service level connection

## · Test Purpose

Verify that the IUT, supporting LE Secure Connections, after performing the authentication procedure will achieve an incoming service level connection operating in the correct security mode and level. The Lower Tester supports LE Secure Connections. The IUT is the Central.

## · Reference

[10] 2.3.5.6

## · Initial Condition

- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The Lower Tester will establish a GATT service request when TSPX\_Use\_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel.

## · Test Case Configuration

Table 4.18: LE Secure Connections, Central -incoming service level connection test cases

| TCID | Security Mode and Level |
| GAP/SEC/SEM/BV-27-C [LE security mode: mode 1 level 4, Central - incoming service level connection] | LE security mode 1 level 4 |
| GAP/SEC/SEM/BV-43-C [LE Secure Connections Only: mode 1 level 2, Central - incoming service level connection] | LE security mode 1 level 2 |
| GAP/SEC/SEM/BV-44-C [LE Secure Connections Only: mode 1 level 3, Central - incoming service level connection] | LE security mode 1 level 3 |

## · Test Procedure

1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.18.
2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester.
3. The Lower Tester initiates LE Secure Connections pairing according to the security mode and level specified in Table 4.18.
4. The Lower Tester and the IUT complete SMP Phase 1, Phase 2 (pairing), and Phase 3 (encryption and key distribution).
5. The Lower Tester initiates either an L2CAP channel establishment or GATT service request to the IUT.
6. The IUT replies with the correct channel establishment response.

Figure 4.49: LE Secure Connections, Central -incoming service level connection MSC

## · Expected Outcome

## Pass verdict

The Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted on the security mode and level specified in Table 4.18.

The initiated procedure is successful.

## · Notes

It is recommended to test with a service or profile that requires the mode and level specified by Table 4.18.

## GAP/SEC/SEM/BV-28-C [Secure Connections Only mode LE transport -failed procedure, Central -outgoing service level connection]

- Test Purpose

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only initiating the authentication procedure will result in a failed procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Central.

- Reference

[9] 10.2.4

- Initial Condition
- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- Test Procedure
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

Figure 4.50: GAP/SEC/SEM/BV-28-C [Secure Connections Only mode LE transport -failed procedure, Central -outgoing service level connection] MSC

- Expected Outcome

## Pass verdict

In ALT 1, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1.

In ALT 2, the IUT does not complete the L2CAP Channel establishment or GATT service request.

## GAP/SEC/SEM/BV-29-C [Secure Connections Only mode LE transport -failed procedure, Central -incoming service level connection]

- Test Purpose

Verify that the IUT in Secure Connections Only mode or that supports Unauthenticated Pairing with LE Secure Connections only or Authenticated Pairing with LE Secure Connections only rejects an L2CAP channel establishment or GATT service request procedure both before and after the authentication procedure when performed toward a peer not supporting LE Secure Connections. The Lower Tester does not support LE Secure Connections. The IUT is the Central.

- Reference

[9] 10.2.4

- Initial Condition
- -The IUT supports LE Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The Lower Tester is configured so that it does not support LE Secure Connections.
- -The Lower Tester will establish a GATT service request when TSPX\_Use\_GATT is set to TRUE. Otherwise, the Lower Tester will establish an L2CAP channel.

- Test Procedure
1. The Upper Tester configures the IUT into Secure Connections Only mode or to only support LE Secure Connections.
2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester.
3. The Lower Tester initiates either an L2CAP channel establishment or GATT service request to the IUT.
4. The IUT rejects the request.
5. The Lower Tester initiates authenticated LE Legacy pairing.
6. Alternative 1: the IUT rejects the pairing by sending an SMP Pairing Failed message.
7. Alternative 2: the Lower Tester and the IUT complete LE legacy pairing. The Lower Tester reinitiates the request to the IUT as attempted in Step 3. The IUT rejects the request.

Figure 4.51: GAP/SEC/SEM/BV-29-C [Secure Connections Only mode -failed procedure, Central -incoming service level connection] MSC

- Expected Outcome

## Pass verdict

The L2CAP channel establishment or GATT service request is rejected before the authentication procedure.

Alternative 1: IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1.

Alternative 2: The IUT and the Lower Tester complete LE legacy pairing and the IUT rejects the request from the Lower Tester.

## GAP/SEC/SEM/BV-30-C [Secure Connections Only mode, Central, failure, BR/EDR and LE transports]

- Test Purpose

Verify that the IUT in Secure Connections Only mode performs either an L2CAP channel establishment or GATT service procedure over LE and a channel establishment procedure over BR/EDR. The IUT is initiator of the procedure over both LE and BR/EDR. The Lower Tester supports neither LE Secure Connections nor BR/EDR Secure Connections. The procedure fails over both LE and BR/EDR. The IUT is the Central.

- Reference

[9] 10.2.4

- Initial Condition
- -The IUT supports both LE Secure Connections and BR/EDR Secure Connections. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.
- -The Lower Tester is configured so that it does not support LE Secure Connections and BR/EDR Secure Connections.
- -The PSM for the service on the IUT that requires security mode 4 level 3 on BR/EDR is specified in the TSPX\_psm\_sm4l3 IXIT value.
- -The IUT and the Lower Tester are not bonded on BR/EDR (neither the IUT nor the Lower Tester has link keys).
- -A BR/EDR ACL connection does not exist between the devices.
- Test Procedure
1. The Upper Tester configures the IUT into Secure Connections Only mode.
2. The Upper Tester configures the IUT (in Central role) to receive advertising packets from the Lower Tester (in Peripheral role), and complete link establishment with the Lower Tester.
3. The IUT begins LE Secure Connections Phase 1 by sending an SMP Pairing Request, with the Secure Connections bit set to 1. The Lower Tester responds with an SMP Pairing Response with the Secure Connections bit set to 0. The IUT will respond with an SMP Pairing Failed message.
4. The IUT terminates the LE connection.
5. The Upper Tester requests the IUT to establish a channel to access a service on the Lower Tester. The service requires security mode 4 level 3 on the IUT.
6. The IUT creates an ACL connection with the Lower Tester and may optionally perform the Secure Simple Pairing procedure with the Lower Tester.

Figure 4.52: GAP/SEC/SEM/BV-30-C [Secure Connections Only mode, Central, Failure, BR/EDR and LE Transports] MSC

- Expected Outcome

## Pass verdict

On the LE transport, the IUT sends an SMP Pairing Failed message to the Lower Tester to end SMP Pairing Phase 1.

On the BR/EDR transport, t he IUT rejects the Upper Tester's request to establish a channel to access the service on the Lower Tester when the service requires security mode 4 level 3 on the IUT.

## 4.5.4.3 LE security mode 1, Central -Invalid Encryption Key Size

- Test Purpose

Verify that the IUT in LE security mode 1 as Central fails pairing when receiving an invalid key size.

- Reference

[9] 10.3.2, 10.2.1

- Initial Condition
- -The IUT is in Link Layer Standby state.
- Test Case Configuration
- Test Procedure

Table 4.19: LE security mode 1, Central -Invalid Encryption Key Size test cases

| TCID | LE Security Mode and Level |
| GAP/SEC/SEM/BI-10-C [LE security mode 1 level 4, Central - Invalid Encryption Key Size] | LE security mode 1 level 4 |
| GAP/SEC/SEM/BI-22-C [LE security mode 1 level 3, Central - Invalid Encryption Key Size] | LE security mode 1 level 3 with LE Secure Connections Pairing only |
| GAP/SEC/SEM/BI-23-C [LE security mode 1 level 2, Central - Invalid Encryption Key Size] | LE security mode 1 level 2 with LE Secure Connections Pairing only |

Figure 4.53: LE security mode 1, Central -Invalid Encryption Key Size MSC

Repeat Steps 1 -6 for all values of the Maximum Encryption Key Size field (in Step 4) in the interval [7, 15].

1. The Upper Tester configures the IUT into the security mode and level specified in Table 4.19.
2. The Upper Tester configures the IUT to connect to the Lower Tester.
3. The Upper Tester orders the IUT to initiate pairing, and the IUT sends to the Lower Tester an SMP Pairing Request with the Secure Connections bit set to 1 and Maximum Encryption Key Size set to 16.
4. The Lower Tester responds with an SMP Pairing Response, with the Secure Connections bit set to 1 and Maximum Encryption Key Size set to the value selected for this iteration.
5. The IUT sends to the Lower Tester an SMP Pairing Failed with the Reason set to 'Encryption Key Size' (0x06) and to report the procedure failure to the Upper Tester.
6. The Lower Tester terminates the LE connection.
- Expected Outcome

## Pass verdict

The IUT fails pairing for any key size value less than 16 while in the specified security mode and level.

## 4.5.5 LE security modes -Both connected roles

## 4.5.5.1 Incoming GATT indication, LE security mode 1 level 2

- Test Purpose

Verify that the IUT properly handles a GATT indication before security requirements are performed in LE security mode 1 level 2.

- Reference

[17] 10.3.2.2

- Initial Condition
- -The IUT is in the Standby state.
- -The IUT is the GATT Client in the role specified in Table 4.20.
- -The Lower Tester is configured so that it sends GATT indications.
- Test Case Configuration

Table 4.20: Incoming GATT indication, LE security mode 1 level 2 test cases

| TCID | IUT Role |
| GAP/SEC/SEM/BV-56-C [Incoming GATT indication, LE security mode 1 level 2, Peripheral] | Peripheral |
| GAP/SEC/SEM/BV-62-C [Incoming GATT indication, LE security mode 1 level 2, Central] | Central |

## · Test Procedure

Figure 4.54: Incoming GATT indication, LE security mode 1 level 2 MSC -Page 1 of 2

Figure 4.55: Incoming GATT indication, LE security mode 1 level 2 MSC -Page 2 of 2

1. The Upper Tester puts the IUT into LE security mode 1 level 2.
2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.20.
3. Perform alternative 3A or 3B depending on the IUT role in Table 4.20.
4. Alternative 3A (IUT is Peripheral):
5. 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding\_Flags bit set to 1 and the MITM and SC bits set to 0 or 1.
6. 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding\_Flags bit set to 1 and the MITM set to 0 and SC bit set to 1.
7. 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding\_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1.

Alternative 3B (IUT is Central):

- 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding\_Flags bit set to 1 and the MITM and SC bits set to 0 or 1.
- 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding\_Flags set to 1 and MITM set to 0 and SC bit set to 1.
4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
5. The Upper Tester commands the IUT to enable GATT indications with the Lower Tester.
6. The IUT sends an ATT\_WRITE\_REQ to the Lower Tester with CCCD set to 0x0002.
7. The Lower Tester sends an ATT\_WRITE\_RSP to the IUT.
8. The IUT and the Lower Tester disconnect.
9. Perform either alternative 9A, 9B, or 9C depending on if the IUT starts an encryption request. Alternative 9A (The IUT does not start an encryption request):
- 9A.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.20.
- 9A.2 The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.
- 9A.3 The IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.
- 9A.4 The IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- 9A.5 The Lower Tester initiates and completes the encryption procedure with the IUT.
- Alternative 9B (The IUT starts an encryption request):
- 9B.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.20.
- 9B.2 The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.

Steps 9B.3 -9B.5 may occur in any order.

- 9B.3 The IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.
- 9B.4 The IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- 9B.5 The IUT initiates and completes the encryption procedure with the Lower Tester.
10. The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.
11. The IUT sends an ATT\_HANDLE\_VALUE\_CFM to the Lower Tester.
12. The IUT sends a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 9A.3 or 9B.3, the IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.

In Step 9A.4 or 9B.4, the IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.

In Step 12, the IUT sends a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.

## 4.5.5.2 Incoming GATT indication, LE security mode 1 level 3

- Test Purpose

Verify that the IUT properly handles a GATT indication before security requirements are performed in LE security mode 1 level 3.

- Reference

[17] 10.3.2.2

- Initial Condition
- -The IUT is in the Standby state.
- -The IUT is the GATT Client in the role specified in Table 4.21.
- -The Lower Tester is configured so that it sends GATT indications.
- Test Case Configuration

| TCID | IUT Role |
| GAP/SEC/SEM/BV-57-C [Incoming GATT indication, LE security mode 1 level 3, Peripheral] | Peripheral |
| GAP/SEC/SEM/BV-63-C [Incoming GATT indication, LE security mode 1 level 3, Central] | Central |

Table 4.21: Incoming GATT indication, LE security mode 1 level 3 test cases

## · Test Procedure

Figure 4.56: Incoming GATT indication, LE security mode 1 level 3 MSC -Page 1 of 2

Figure 4.57: Incoming GATT indication, LE security mode 1 level 3 MSC -Page 2 of 2

1. The Upper Tester puts the IUT into LE security mode 1 level 3.
2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.21.
3. 3.
4. Perform alternative 3A or 3B depending on the IUT role in Table 4.21. Alternative 3A (IUT is Peripheral):
5. 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 0 or 1.
6. 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 1.
7. 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 0 or 1.

Alternative 3B (IUT is Central):

- 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 0 or 1.
- 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 1.
4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
5. The Upper Tester commands the IUT to enable GATT indications with the Lower Tester.
6. The IUT sends an ATT\_WRITE\_REQ to the Lower Tester with CCCD set to 0x0002.
7. The Lower Tester sends an ATT\_WRITE\_RSP to the IUT.
8. The IUT and the Lower Tester disconnect.
9. Perform either alternative 9A, 9B, or 9C depending on if the IUT starts an encryption request. Alternative 9A (The IUT does not start an encryption request):
- 9A.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.21.
- 9A.2 The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.
- 9A.3 The IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.
- 9A.4 The IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- 9A.5 The Lower Tester initiates and completes the encryption procedure with the IUT.
- Alternative 9B (The IUT starts an encryption request):
- 9B.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.21.
- 9B.2 The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.

Steps 9B.3 -9B.5 may occur in any order.

- 9B.3 The IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.
- 9B.4 The IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- 9B.5 The IUT initiates and completes the encryption procedure with the Lower Tester.
10. The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.
11. The IUT sends an ATT\_HANDLE\_VALUE\_CFM to the Lower Tester.
12. The IUT sends a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 9A.3 or 9B.3, the IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.

In Step 9A.4 or 9B.4, the IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.

In Step 12, the IUT sends a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.

## 4.5.5.3 LE Secure Connections Only, Incoming GATT Indication

- Test Purpose

Verify that the IUT that supports LE Secure Connections only properly handles a GATT indication before security requirements are performed.

- Reference

[17] 10.3.2.2

- Initial Condition
- -The IUT is in the Standby state.
- -The IUT supports LE Secure Connections. The IUT is the GATT Client in the role specified in Table 4.22. The Lower Tester supports LE Secure Connections.
- -The IUT is configured to receive GATT indications from the Lower Tester.
- Test Case Configuration

| TCID | IUT Role |
| GAP/SEC/SEM/BV-58-C [LE Secure Connections Only - Incoming GATT indication, Peripheral] | Peripheral |
| GAP/SEC/SEM/BV-64-C [LE Secure Connections Only - Incoming GATT indication, Central] | Central |

Table 4.22: LE Secure Connections Only, Incoming GATT Indication test cases

## · Test Procedure

Figure 4.58: LE Secure Connections Only, Incoming GATT Indication MSC -Page 1 of 2

Figure 4.59: LE Secure Connections Only, Incoming GATT Indication MSC -Page 2 of 2

1. The Upper Tester puts the IUT into the Secure Connections Only mode.
2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.22.
3. Perform alternative 3A or 3B depending on the IUT role in Table 4.22. Alternative 3A (IUT is Peripheral):
4. 3A.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Security Request, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
5. 3A.2 The Lower Tester responds by sending an SMP Pairing Request, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
6. 3A.3 The IUT replies with an SMP Pairing Response, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.

## Alternative 3B (IUT is Central):

- 3B.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Pairing Request, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
- 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
5. The Upper Tester commands the IUT to enable GATT indications with the Lower Tester.
6. The IUT sends an ATT\_WRITE\_REQ to the Lower Tester with CCCD set to 0x0002.
7. The Lower Tester sends an ATT\_WRITE\_RSP to the IUT.
8. The IUT and the Lower Tester disconnect.
9. Perform either alternative 9A, 9B, or 9C depending on if the IUT starts an encryption request. Alternative 9A (The IUT does not start an encryption request):
- 9A.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.22.
- 9A.2 The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.
- 9A.3 The IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.
- 9A.4 The IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- 9A.5 The Lower Tester initiates and completes the encryption procedure with the IUT.
- Alternative 9B (The IUT starts an encryption request):
- 9B.1 The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.22.
- 9B.2 The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.

Steps 9B.3 -9B.5 may occur in any order.

- 9B.3 The IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.
- 9B.4 The IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- 9B.5 The IUT initiates and completes the encryption procedure with the Lower Tester.
10. The Lower Tester sends an ATT\_HANDLE\_VALUE\_IND PDU to the IUT containing a valid Attribute Handle and Attribute Value.
11. The IUT sends an ATT\_HANDLE\_VALUE\_CFM to the Lower Tester.
12. The IUT sends a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 9A.3 or 9B.3, the IUT sends an ATT\_HANDLE\_VALUE\_CFM PDU to the Lower Tester.

In Step 9A.4 or 9B.4, the IUT does not send a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.

In Step 12, the IUT sends a ATT\_HANDLE\_VALUE\_IND to the Upper Tester.

## 4.5.5.4 Incoming GATT notification, LE security mode 1 level 2

- Test Purpose

Verify that the IUT properly handles a GATT notification before security requirements are performed for LE security mode 1 level 2.

- Reference

[17] 10.3.2.2

- Initial Condition
- -The IUT is in the Standby state.
- -The IUT is the GATT Client in the role specified in Table 4.23.
- -The Lower Tester is configured so that it sends GATT notifications.
- Test Case Configuration

| TCID | Role |
| GAP/SEC/SEM/BV-59-C [Incoming GATT notification, LE security mode 1 level 2, Peripheral] | Peripheral |
| GAP/SEC/SEM/BV-65-C [Incoming GATT notification, LE security mode 1 level 2, Central] | Central |

Table 4.23: Incoming GATT notification, LE security mode 1 level 2 test cases

## · Test Procedure

Figure 4.60: Incoming GATT notification, LE security mode 1 level 2 MSC

1. The Upper Tester puts the IUT into LE security mode 1 level 2.
2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.23.
3. Perform alternative 3A or 3B depending on the IUT role in Table 4.23.

Alternative 3A (IUT is Peripheral):

- 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding\_Flags bit set to 1 and the MITM and SC bits set to 0 or 1.
- 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding\_Flags bit set to 1 and the MITM set to 0 and SC bit set to 1.
- 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding\_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1.

Alternative 3B (IUT is Central):

- 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding\_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1.
- 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding\_Flags bit set to 1 and the MITM set to 0 and SC bit set to 0 or 1.
4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
5. The Upper Tester commands the IUT to enable GATT notifications with the Lower Tester.
6. The IUT sends an ATT\_WRITE\_REQ to the Lower Tester with CCCD set to 0x0001.
7. The Lower Tester sends an ATT\_WRITE\_RSP to the IUT.
8. The IUT and the Lower Tester disconnect.
9. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.23.
10. The Lower Tester sends an ATT\_HANDLE\_VALUE\_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value.
11. The IUT does not send a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.
12. Perform alternative 12A or 12B depending on the IUT role in Table 4.23. Alternative 12A (IUT is Peripheral):
- 12A.1 The Lower Tester initiates and completes the encryption procedure with the IUT. Alternative 12B (IUT is Central):
- 12B.1 The IUT initiates and completes the encryption procedure with the Lower Tester.
13. The Lower Tester sends an ATT\_HANDLE\_VALUE\_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value.
14. The IUT sends a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester with a valid Characteristic Handle value.
- Expected Outcome

## Pass verdict

In Step 11, the IUT does not send a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.

In Step 14, the IUT sends a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.

## 4.5.5.5 Incoming GATT notification, LE security mode 1 level 3

- Test Purpose

Verify that the IUT properly handles a GATT notification before security requirements are performed for LE security mode 1 level 3.

- Reference

[17] 10.3.2.2

- Initial Condition
- -The IUT is in the Standby state.
- -The IUT is the GATT Client in the role specified in Table 4.24.
- -The Lower Tester is configured so that it sends GATT notifications.
- Test Case Configuration

| TCID | Role |
| GAP/SEC/SEM/BV-60-C [Incoming GATT notification, LE security mode 1 level 3, Peripheral] | Peripheral |
| GAP/SEC/SEM/BV-66-C [Incoming GATT notification, LE security mode 1 level 3, Central] | Central |

Table 4.24: Incoming GATT notification, LE security mode 1 level 3 test cases

## · Test Procedure

Figure 4.61: Incoming GATT notification, LE security mode 1 level 3 MSC

1. The Upper Tester puts the IUT into LE security mode 1 level 3.
2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.24.
3. Perform alternative 3A or 3B depending on the IUT role in Table 4.24.

Alternative 3A (IUT is Peripheral):

- 3A.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Security Request, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 0.
- 3A.2 The Lower Tester responds to the LE Pairing Reply Phase 1 by sending an SMP Pairing Request, with the Bonding\_Flags and MITM bits set to 1and the SC bit set to 0.
- 3A.3 The IUT replies with an SMP Pairing Response, with the Bonding\_Flags and MITM bits set to 1and the SC bit set to 0.

Alternative 3B (IUT is Central):

- 3B.1 The IUT begins the pairing phase 1 with LE legacy pairing by sending an SMP Pairing Request, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 0.
- 3B.2 The Lower Tester replies with an SMP Pairing Response, with the Bonding\_Flags and MITM bits set to 1 and the SC bit set to 0.
4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
5. The Upper Tester commands the IUT to enable GATT notifications with the Lower Tester.
6. The IUT sends an ATT\_WRITE\_REQ to the Lower Tester with CCCD set to 0x0001.
7. The Lower Tester sends an ATT\_WRITE\_RSP to the IUT.
8. The IUT and the Lower Tester disconnect.
9. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.24.
10. The Lower Tester sends an ATT\_HANDLE\_VALUE\_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value.
11. The IUT does not send a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.
12. Perform alternative 12A or 12B depending on the IUT role in Table 4.24. Alternative 12A (IUT is Peripheral):

12A.1 The Lower Tester initiates and completes the encryption procedure with the IUT. Alternative 12B (IUT is Central):

- 12B.1 The IUT initiates and completes the encryption procedure with the Lower Tester.
13. The Lower Tester sends an ATT\_HANDLE\_VALUE\_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value.
14. The IUT sends a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester with a valid Characteristic Handle value.

## · Expected Outcome

## Pass verdict

In Step 11, the IUT does not send a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.

In Step 14, the IUT sends a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.

## 4.5.5.6 LE Secure Connections Only, Incoming GATT Notification

- Test Purpose

Verify that the IUT that supports LE Secure Connections only properly handles a GATT notification before security requirements are performed.

- Reference

[17] 10.3.2.2

- Initial Condition
- -The IUT is in the Standby state.
- -The IUT supports LE Secure Connections. The IUT is the GATT Client in the role specified in Table 4.25. The Lower Tester supports LE Secure Connections.
- -The IUT is configured to receive GATT notifications from the Lower Tester.
- Test Case Configuration

| TCID | Role |
| GAP/SEC/SEM/BV-61-C [LE Secure Connections Only, Incoming GATT notification, Peripheral] | Peripheral |
| GAP/SEC/SEM/BV-67-C [LE Secure Connections Only, Incoming GATT notification, Central] | Central |

Table 4.25: Incoming GATT notification, LE security mode 1 level 3 test cases

## · Test Procedure

Figure 4.62: LE Secure Connections Only, Incoming GATT Notification MSC

1. The Upper Tester puts the IUT into the Secure Connections Only mode.
2. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.25.
3. Perform alternative 3A or 3B depending on the IUT role in Table 4.25.

Alternative 3A (IUT is Peripheral):

- 3A.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Security Request, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
- 3A.2 The Lower Tester responds by sending an SMP Pairing Request, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
- 3A.3 The IUT replies with an SMP Pairing Response, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.

Alternative 3B (IUT is Central):

- 3B.1 The IUT begins the pairing phase 1 with Secure Connections by sending an SMP Pairing Request, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
- 3B.2 The Lower Tester replies with SMP Pairing Response, with the Secure Connections, Bonding\_Flags, and MITM bits set to 1.
4. The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
5. The Upper Tester commands the IUT to enable GATT notifications with the Lower Tester.
6. The IUT sends an ATT\_WRITE\_REQ to the Lower Tester with CCCD set to 0x0001.
7. The Lower Tester sends an ATT\_WRITE\_RSP to the IUT.
8. The IUT and the Lower Tester disconnect.
9. The Upper and Lower Testers perform the steps required to create a connection between the Lower Tester and the IUT, with the IUT in the role specified in Table 4.25.
10. The Lower Tester sends a ATT\_HANDLE\_VALUE\_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value.
11. The IUT does not send a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.
12. Perform alternative 12A or 12B depending on the IUT role in Table 4.25. Alternative 12A (IUT is Peripheral):

12A.1 The Lower Tester initiates and completes the encryption procedure with the IUT. Alternative 12B (IUT is Central):

12B.1 The IUT initiates and completes the encryption procedure with the Lower Tester.

13. The Lower Tester sends an ATT\_HANDLE\_VALUE\_NTF PDU to the IUT containing a valid Attribute Handle and Attribute Value.
14. The IUT sends a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 11, the IUT does not send a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.

In Step 14, the IUT sends a ATT\_HANDLE\_VALUE\_NTF to the Upper Tester.

## 4.5.6 Security modes -Observer role

Verify the correct behavior in this mode. The role of the IUT is the Observer and Acceptor.

## 4.5.6.1 LE security mode 3 -Observer role, Acceptor

- Test Purpose

Verify that the IUT in the LE security mode 3 with level as specified in Table 4.26 receives BIS data.

- Reference

[15] 9.2.5, 1.2.2.1, 1.2.2.2

- Initial Condition
- -The IUT is in Synchronization State.
- -The Lower Tester is in Isochronous Broadcasting State.
- -The Broadcast\_Code has been obtained by the IUT's Host using an unauthenticated or authenticated method as defined by the IUT's application. The Lower Tester may obtain the Broadcast\_Code by any means, including reading the TSPX\_broadcast\_code IXIT parameter, and for test purposes may be considered either authenticated or unauthenticated.
- Test Case Configuration
- Test Procedure
1. Perform test case GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment procedure]. When enabling the BIG, set the Encryption parameter as specified in Table 4.26.
2. The Lower Tester sends BIS data to the IUT with the Encryption specified in Table 4.26.
3. The IUT receives the BIS data and reports the data to the Upper Tester. The Lower Tester and the IUT operate on the same security mode and level.

Table 4.26: LE security mode 3 -Observer role, Acceptor test cases

| Test Case ID | Security Level | Encryption | Initial Condition Encryption Information |
| GAP/SEC/SEM/BV-31-C | 1 | Disabled(0x00) | None |
| GAP/SEC/SEM/BV-32-C | 2 or 3 | Enabled(0x01) | The Broadcast_Code has been obtained by the IUT's Host . |

Figure 4.63: LE security mode 3 -Observer role, Acceptor MSC

- Expected Outcome

## Pass verdict

In Step 3, the IUT receives the BIS data and reports the data to the Upper Tester. The Lower Tester and the IUT operate on the same security mode and level.

## GAP/SEC/SEM/BI-13-C [LE security mode 3 -Observer, Reject Lower Level Security]

- Test Purpose

Verify that the IUT in the LE security mode 3 rejects BIS events with lower level security.

- Reference

[15] 9.2.5, 1.2.2.1, 1.2.2.2

- Initial Condition
- -The IUT is in Synchronization State.
- -The Lower Tester is in Isochronous Broadcasting State.
- -The Broadcast\_Code has been obtained by the IUT's Host using a method as defined by the IUT's application. The Lower Tester may obtain the Broadcodeast\_Code by any means, including reading the TSPX\_broadcast\_code IXIT parameter, and for test purposes may be considered either authenticated or unauthenticated.
- Test Procedure
1. Attempt to perform test case GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment procedure]. When creating the BIG, the Lower Tester disables encryption. The security level of the IUT is set to level 2 or 3.
2. The IUT is unable to synchronize to the BIG.
- Expected Outcome

## Pass verdict

In Step 2, the IUT is unable to synchronize to the BIG.

## GAP/SEC/SEM/BV-45-C [Re-pair or stop a connection attempt when a connection fails due to failed encryption, LE security mode 1 level 4]

- Test Purpose

Verify that the IUT in LE security mode 1 level 4 properly handles when a connection attempt with a bonded peer fails during the encryption phase. The IUT can either stop the connection attempt or notify the Upper Tester for User Interaction to pair with the peer. The IUT is the Central. The Lower Tester supports LE Secure Connections.

- Reference

[9] 10.3

- Initial Condition
- -The IUT is bonded with the Lower Tester. The IUT is in Link Layer Standby state. The IUT has to be configured such that it will not reject the initiated procedure.

## · Test Procedure

1. The Upper Tester configures the IUT into LE security mode 1 level 4.
2. The Upper Tester configures the IUT (in the Central role) to receive advertising packets from the Lower Tester (in the Peripheral role) and completes link establishment with the Lower Tester.
3. The Upper Tester triggers a GATT service request.
4. The IUT starts the encryption procedure with the Lower Tester using the LTK for the Lower Tester.
5. The Lower Tester fails the encryption procedure.
6. Perform either alternative 6A or 6B depending on how the IUT handles the encryption failure.
6. Alternative 6A (The IUT stops the connection attempt):
8. 6A.1 The IUT sends an event to the Upper Tester that indicates that the connection procedure trigged in Step 2 failed.
9. Alternative 6B (The IUT starts the pairing process with the Lower Tester):
10. 6B.1 The IUT sends a request to the Upper Tester for user interaction to pair with the peer device.
11. 6B.2 The Upper Tester accepts the request to pair with the peer device.
12. 6B.3 The Upper Tester triggers an authentication procedure on the IUT, e.g., by an L2CAP channel.
13. 6B.4 The IUT begins LE Secure Connections Phase 1 by sending an SMP Pairing Request, with the Secure Connections bit set to 1.
14. 6B.5 The Lower Tester answers with SMP Pairing Response, with the Secure Connections bit set to 1.
15. 6B.6 The IUT and the Lower Tester complete SMP Phase 2 (pairing) and Phase 3 (encryption and key distribution).
16. 6B.7 The IUT sends a successful GATT service request event to the Upper Tester.

Figure 4.64: GAP/SEC/SEM/BV-45-C [Re-pair or stop a connection attempt when a connection fails due to failed encryption, LE security mode 1 level 4] MSC

- Expected Outcome

## Pass verdict

In Step 6A.1, the IUT sends an event to the Upper Tester that the service request failed.

In alternative 6B, the Lower Tester and the IUT complete SMP phases 1, 2, and 3. The resulting connection is encrypted and operating in LE security mode 1 level 4.

- Notes

It is recommended to test with a service or profile that requires security mode 1 level 4.

## 4.5.7 Security modes -Broadcaster role

Verify the correct behavior in this mode. The role of the IUT is Broadcaster and Initiator.

## 4.5.7.1 LE security mode 3 -Broadcaster role, Initiator

- Test Purpose

Verify that the IUT in the LE security mode 3 level as specified in Table 4.27 sends BIS data.

- Reference

[15] 9.2.5, 1.2.2.1, 1.2.2.2

- Initial Condition
- -The IUT is in Isochronous Broadcasting State.
- -The Lower Tester is in Synchronization State.
- -The Broadcast\_Code has been obtained by the IUT's Host using an unauthenticated or authenticated method per Table 4.27 as defined by the IUT's application. The Lower Tester may obtain the Broadcast\_Code by any means, including reading the TSPX\_broadcast\_code IXIT parameter, and for test purposes may be considered either authenticated or unauthenticated.
- -The encryption information is broadcast as specified in Table 4.27.
- Test Case Configuration
- Test Procedure
1. Perform test case GAP/BIS/BBM/BV-01-C [Broadcast Isochronous Stream Broadcasting mode]. When enabling the BIG, set the Encryption parameter as specified in Table 4.27.
2. The Lower Tester receives the Broadcast Isochronous data. The Lower Tester and the IUT operate on the same security mode and level.

Table 4.27: LE security mode 3 -Broadcaster role, Initiator test cases

| Test Case ID | Security Level | Encryption | Initial Condition Encryption Information |
| GAP/SEC/SEM/BV-34-C | 1 | Disabled(0x00) | None |
| GAP/SEC/SEM/BV-35-C | 2 or 3 | Enabled(0x01) | The Broadcast_Code has been obtained by the IUT's Host. |

Figure 4.65: LE security mode 3 -Broadcaster role, Initiator MSC

- Expected Outcome

## Pass verdict

In Step 2, the Lower Tester receives the Broadcast Isochronous data. The IUT and the Lower Tester operate on the same security mode and level.

## 4.5.8 Security modes -Both connected roles

## 4.5.8.1 Security mode 4 -Initiator, Channel Establishment, Encryption Not Enabled

- Test Purpose

Verify that an IUT in the security mode and level specified in Table 4.28 that initiates a data transmission to a remote service does not send a channel establishment request to the Lower Tester when encryption has not been enabled on the connection. The IUT is the initiator of the channel establishment procedure. The Lower Tester is the responder.

- Reference

[17] 5.2.2.1.2

- Initial Condition
- -The IUT is in Idle mode.
- -The PSM for the service on the IUT that requires the security mode and level specified in Table 4.28 is specified in the IXIT values in Table 4.28.
- -The Lower Tester does not support encryption.
- -The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has stored link keys).
- -An ACL connection is established between the devices.
- Test Case Configuration

| TCID | Security Mode and Level | IXIT |
| GAP/SEC/SEM/BI-25-C [Security mode 4 level 2 - Initiator, Encryption Not Enabled] | Security mode 4 level 2 | TSPX_psm_sm4l2 |
| GAP/SEC/SEM/BI-26-C [Security mode 4 level 3 - Initiator, Encryption Not Enabled] | Security mode 4 level 3 | TSPX_psm_sm4l3 |
| GAP/SEC/SEM/BI-27-C [Security mode 4 level 4 - Initiator, Encryption Not Enabled] | Security mode 4 level 4 | TSPX_psm_sm4l4 |

Table 4.28: Security mode 4 -Initiator, Channel Establishment, Encryption Not Enabled test cases

## · Test Procedure

Figure 4.66: Security mode 4 -Initiator, Channel Establishment, Encryption Not Enabled MSC

1. The Upper Tester puts the IUT into the security mode and level specified in Table 4.28.
2. The Upper Tester triggers a channel creation event to set up a channel with the Lower Tester.
3. The IUT performs the generic authentication procedure with the Lower Tester. The generic authentication procedure successfully completes.
4. The IUT performs link encryption with the Lower Tester. The link encryption fails.
5. The IUT signals to the Upper Tester that the channel creation failed after link encryption fails.
6. The IUT does not send an L2CAP channel establishment request to the Lower Tester.
- Expected Outcome

## Pass verdict

The IUT is to not send an L2CAP channel establishment request to the Lower Tester.

## 4.5.8.2 Security mode 4 -Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled

- Test Purpose

Verify that an IUT in the security mode and level specified in Table 4.29 that initiates a unicast data transmission on a connectionless channel does not send unicast data to the Lower Tester when encryption has not been enabled on the connection. The IUT is the initiator of the connectionless channel procedure.

- Reference

[17] 5.2.2.1.2

- Initial Condition
- -The IUT is in Idle mode.
- -The PSM for the service on the IUT that requires the security mode and level specified in Table 4.29 is specified in the IXIT values in Table 4.29.
- -The Lower Tester does not support encryption.
- -The IUT and the Lower Tester are not bonded (neither the IUT nor the Lower Tester has stored link keys).
- -An ACL connection is established between the devices.
- Test Case Configuration
- Test Procedure

Table 4.29: Security mode 4 -Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled test cases

| TCID | Security Mode and Level | IXIT |
| GAP/SEC/SEM/BI-28-C [Security mode 4 level 2 - Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled] | Security mode 4 level 2 | TSPX_psm_sm4l2 |
| GAP/SEC/SEM/BI-29-C [Security mode 4 level 3 - Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled] | Security mode 4 level 3 | TSPX_psm_sm4l3 |
| GAP/SEC/SEM/BI-30-C [Security mode 4 level 4 - Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled] | Security mode 4 level 4 | TSPX_psm_sm4l4 |

Figure 4.67: Security mode 4 -Initiator, Connectionless Channel, Unicast Data, Encryption Not Enabled MSC

1. The Upper Tester puts the IUT into the security mode and level specified in Table 4.29.
2. The Upper Tester sends an L2CAP G-Frame to the IUT with unicast data.
3. The IUT performs the generic authentication procedure with the Lower Tester. The generic authentication procedure successfully completes.
4. The IUT performs link encryption with the Lower Tester. The link encryption fails.
5. The IUT signals to the Upper Tester that the link encryption fails.
6. The IUT does not send any unicast data to the Lower Tester.
- Expected Outcome

## Pass verdict

The IUT is to not send any unicast data to the Lower Tester.

## GAP/SEC/SEM/BI-31-C [Security mode 4 level 4, Secure Connections -Responder, Insufficient Encryption Type]

- Test Purpose

Verify that an IUT in security mode 4 level 4 supporting Secure Connections rejects a received channel establishment request from the Lower Tester if an insufficient encryption type is selected on the connection between the IUT and the Lower Tester. The IUT is the responder of the channel establishment procedure. The Lower Tester is the initiator.

- Reference

## 17 5.2.2.2.1

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX\_psm\_sm4l4 IXIT value.
- -The IUT and the Lower Tester have previously bonded using Secure Connections.
- -An ACL connection exists between the devices.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 1 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -The IUT is in connectable mode.

## · Test Procedure

Figure 4.68: Security mode 4 level 4, Secure Connections -Responder, Insufficient Encryption Type MSC

1. The existing ACL connection between the IUT and the Lower Tester is disconnected.
2. On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0.
3. The Lower Tester establishes an ACL connection with the IUT.
4. The Lower Tester requests establishing a channel to access the TSPX\_psm\_sm4l4 PSM.
5. The IUT and the Lower Tester may begin link encryption.
6. The IUT rejects the L2CAP channel establishment request from the Lower Tester.
- Expected Outcome

## Pass verdict

The IUT is to reject the L2CAP channel establishment request from the Lower Tester.

## GAP/SEC/SEM/BI-32-C [Security mode 4 level 4, Secure Connections -Initiator, Channel Establishment, Insufficient Encryption Type]

- Test Purpose

Verify that an IUT in security mode 4 level 4 supporting Secure Connections rejects a received channel establishment if an insufficient encryption type is selected on the connection between the IUT and the Lower Tester. The IUT is the initiator of the channel establishment procedure. The Lower Tester is the responder.

- Reference

[17] 5.2.2.2.2

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX\_psm\_sm4l4 IXIT value.
- -The IUT and the Lower Tester have previously bonded using Secure Connections.
- -An ACL connection exists between the devices.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 1 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -The IUT is in connectable mode.
- Test Procedure
1. The existing ACL connection between the IUT and the Lower Tester is disconnected.
2. On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0.
3. The Lower Tester establishes an ACL connection with the IUT.
4. The Upper Tester triggers an event to create a channel to the Lower Tester.
5. Perform either alternative 5A or 5B depending on the IUT behavior.

Figure 4.69: Security mode 4 level 4, Secure Connections -Initiator, Channel Establishment, Insufficient Encryption Type MSC

Alternative 5A (The IUT executes a feature exchange):

- 5A.1 The IUT sends an LMP\_FEATURES\_REQ PDU to the Lower Tester with Features set to the IUT feature set.
- 5A.2 The Lower Tester sends an LMP\_FEATURES\_RES PDU to the IUT with Features set to the Lower Tester feature set.

Alternative 5B (The IUT begins encryption):

- 5B.1 The IUT and the Lower Tester begin link encryption.
6. The IUT notifies the Upper Tester that the channel creation with the Lower Tester failed due to a security block.
7. The IUT does not send an L2CAP channel establishment request to the Lower Tester.
- Expected Outcome

## Pass verdict

In Step 7, the IUT does not send an L2CAP channel establishment request to the Lower Tester.

## GAP/SEC/SEM/BI-33-C [Security mode 4, Secure Connections -Initiator, Connectionless Channel, Unicast Data, Insufficient Encryption Type]

- Test Purpose

Verify that an IUT in security mode 4 level 4 supporting Secure Connections does not send unicast data to the Lower Tester if an insufficient encryption type is selected on the connection between the IUT and the Lower Tester. The IUT is the initiator of the connectionless channel establishment procedure. The Lower Tester is the responder.

- Reference

[17] 5.2.2.2.2

- Initial Condition
- -The PSM for the service on the IUT that requires security mode 4 level 4 is specified in the TSPX\_psm\_sm4l4 IXIT value.
- -The IUT and the Lower Tester have previously bonded using Secure Connections.
- -An ACL connection exists between the devices.
- -On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 1 and the Secure Connections (Controller Support) LMP feature bit to 1.
- -The IUT is in connectable mode.

## · Test Procedure

Figure 4.70: Security mode 4, Secure Connections -Initiator, Connectionless Channel, Unicast Data, Insufficient Encryption Type MSC

1. The existing ACL connection between the IUT and the Lower Tester is disconnected.
2. On the Lower Tester, set the Secure Connections (Host Support) LMP feature bit to 0.
3. The Lower Tester establishes an ACL connection with the IUT.
4. The Upper Tester sends an L2CAP G-Frame to the IUT.
5. The IUT and the Lower Tester begin link encryption.
6. The IUT signals to the Upper Tester that the link encryption is insufficient.
7. The IUT does not send any unicast data to the Lower Tester.
- Expected Outcome

## Pass verdict

The IUT is to not send any unicast data to the Lower Tester.

## 4.5.9 Channel Sounding

## 4.5.9.1 Channel Sounding Security

- Test Purpose

Verify that the IUT uses the proper CS procedure based on the LE security mode.

- Reference

[19] 10.11.1

- Initial Condition
- -The Lower Tester has the Channel Sounding feature bit set.
- -The Lower Tester and the IUT have completed the encryption procedure with the LE security mode listed in Table 4.30.
- Test Case Configuration

| TCID | LE Security Mode | CS Procedure |
| GAP/SEC/SEM/BV-69-C [Channel Sounding Security, CS Security L1, Initiator] | Channel Sounding Security level 1 | CS Reflector procedure, CS Tone or CS RTT |
| GAP/SEC/SEM/BV-70-C [Channel Sounding Security, CS Security L2, Initiator] | Channel Sounding Security level 2 | CS Reflector procedure, 150 ns CS RTT accuracy with CS Tones |
| GAP/SEC/SEM/BV-71-C [Channel Sounding Security, CS Security L3, Initiator] | Channel Sounding Security level 3 | CS Reflector procedure, 10 ns CS RTT accuracy with CS Tones |
| GAP/SEC/SEM/BV-72-C [Channel Sounding Security, CS Security L4, Initiator] | Channel Sounding Security level 4 | CS Reflector procedure, 10 ns CS RTT accuracy with CS RTT with Sounding Sequence or CS RTT with Random Sequence |
| GAP/SEC/SEM/BV-73-C [Channel Sounding Security, CS Security L1, Reflector] | Channel Sounding Security level 1 | CS Initiator procedure, CS Tone or CS RTT |
| GAP/SEC/SEM/BV-74-C [Channel Sounding Security, CS Security L2, Reflector] | Channel Sounding Security level 2 | CS Initiator procedure, 150 ns CS RTT accuracy with CS Tones |
| GAP/SEC/SEM/BV-75-C [Channel Sounding Security, CS Security L3, Reflector] | Channel Sounding Security level 3 | CS Initiator procedure, 10 ns CS RTT accuracy with CS Tones |
| GAP/SEC/SEM/BV-76-C [Channel Sounding Security, CS Security L4, Reflector] | Channel Sounding Security level 4 | CS Initiator procedure, 10 ns CS RTT accuracy with CS RTT with Sounding Sequence or CS RTT with Random Sequence |

Table 4.30:Channel Sounding Security test cases

- Test Procedure
1. The Lower Tester sends a CS procedure request specified in Table 4.30 to the IUT.
2. The IUT performs the CS procedure as described in Table 4.30.
- Expected Outcome

Figure 4.71: Channel Sounding Security MSC

## Pass verdict

The IUT that is using the LE security mode specified in Table 4.30 uses the CS procedure specified in Table 4.30.

## 4.6 Idle mode procedures

## 4.6.1 General Inquiry -Central

Verify the correct behavior in this mode. The role of the IUT is Central and initiator.

## GAP/IDLE/GIN/BV-01-C [General Inquiry -IUT is Central]

- Test Purpose

Verify that if general inquiry is initiated by the IUT, it sends for at least TGAP(100) inquiry request messages (GIAC).

The IUT is Central and initiator and the Lower Tester is Peripheral and acceptor of the general inquiry procedure.

- Reference

## 1 6.1

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.
- -If the IUT supports general-discoverable mode, the Lower Tester performs inquiry to get the clock offset with respect to the IUT and after the Upper Tester has ordered the IUT to be in generaldiscoverable mode.
- -If the IUT does not support general-discoverable mode, the IUT has to be configured to page the Lower Tester in order to get the CLK offset after the Upper Tester has ordered the IUT to be in connectable mode.

## · Test Procedure

Figure 4.72: GAP/IDLE/GIN/BV-01-C [General Inquiry -IUT is Central] MSC

1. The Upper Tester orders the IUT to initiate general inquiry.
2. The Lower Tester scans for inquiry packets from the IUT to receive a packet within the IUT's repetition of A-train.
3. The Lower Tester monitors the train A during 10 ms. If no inquiry packet is received, the Lower Tester switches to scan train B during 10 ms.
4. Switching trains will continue until first ID packet is received by the Lower Tester. The Lower Tester adjusts its RX window and phase to get the remaining hops.
5. The Lower Tester monitors inquiry packets for 255 times.
6. The Lower Tester immediately starts listening on the other train frequencies. It monitors for 256 times.
7. Steps 5 and 6 are repeated until 10.24 s - 10 ms - 20 ms.
- Expected Outcome

## Pass verdict

The IUT sends at least for TGAP(100) - 30 ms inquiry messages (ID-Packet) by using GIAC.

## 4.6.2 Device Name during General Inquiry

Verify the correct behavior in this mode. The role of the IUT is Peripheral.

## GAP/IDLE/DNDIS/BV-01-C [Device Name During General Inquiry -IUT is Peripheral]

- Test Purpose

Verify that the Lower Tester during general inquiry receives device name from IUT in the reception of extended inquiry response data.

The Lower Tester is Central and initiator and the IUT is Peripheral and acceptor of the general inquiry procedure.

- Reference

## 1 8

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.
- -The IUT device name is defined by the TSPX\_device\_name IXIT value.
- Test Procedure
1. The Lower Tester initiates general inquiry.
2. The Lower Tester receives extended inquiry response data from the IUT.
- Expected Outcome

Figure 4.73: GAP/IDLE/DNDIS/BV-01-C [Device Name During General Inquiry -IUT is Peripheral] MSC

## Pass verdict

The Lower Tester decodes EIR data and finds the IUT's device name ('complete' or 'shortened').

## 4.6.3 Limited Inquiry -Central

Verify the correct behavior in this mode. The role of the IUT is Central and initiator.

## GAP/IDLE/LIN/BV-01-C [Limited Inquiry -IUT is Central]

- Test Purpose

Verify that if limited inquiry is initiated by the IUT, it sends for at least TGAP(100) inquiry request messages (LIAC).

The IUT is Central and initiator and the Lower Tester is Peripheral and acceptor of the limited inquiry procedure.

- Reference

## 1 6.2

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.
- -If the IUT supports general-discoverable mode, the Lower Tester performs inquiry to get the clock offset with respect to the IUT and after the Upper Tester has ordered the IUT to be in generaldiscoverable mode.
- -If the IUT does not support general-discoverable mode, the IUT has to be configured to page the Lower Tester in order to get the CLK offset after the Upper Tester has ordered the IUT to be in connectable mode.
- Test Procedure
1. The IUT is ordered (by using the Upper Tester) to initiate limited inquiry.
2. The Lower Tester scans for inquiry packets from the IUT to receive a packet within the IUT's repetition of A-train.
3. The Lower Tester monitors the train A during 10 ms. If no inquiry packet is received, the Lower Tester switches to scan train B during 10 ms.
4. Switching trains will continue until first ID packet is received by the Lower Tester. The Lower Tester adjusts its RX window and phase to get the remaining hops.
5. The Lower Tester monitors inquiry packets for 255 times.
6. The Lower Tester immediately starts listening on the other train frequencies. It monitors for 256 times.
7. Steps 5 and 6 are repeated until 10.24s - 10ms - 20 ms.
- Expected Outcome

Figure 4.74: GAP/IDLE/LIN/BV-01-C [Limited Inquiry -IUT is Central] MSC

## Pass verdict

The IUT sends at least for TGAP(100) - 30 ms inquiry messages (ID-Packet) by using LIAC.

## 4.6.4 Device Discovery -Central

Verify the correct behavior in this mode. The role of the IUT is Central and initiator.

## GAP/IDLE/DED/BV-02-C [Device Discovery and Name Discovery -Secure Simple Pairing Supported by IUT]

- Test Purpose

Verify that the IUT that supports Secure Simple Pairing first performs the inquiry procedure and afterwards it performs the name discovery procedure for one Peripheral if device discovery is required by upper layer of the IUT.

- Reference

[1] 6.4

- Initial Condition
- -The IUT is in Idle mode with security mode 4 supported by the IUT.
- -The Lower Tester's LMP features include:
- Feature bit 51 (Secure Simple Pairing) set to 1
- Feature bit 63 (Extended Features) set to 1
- Feature bit 64 (Secure Simple Pairing -Host Support) set to 1
- -The Lower Tester is discoverable and connectable.
- Test Procedure

Figure 4.75: GAP/IDLE/DED/BV-02-C [Device Discovery and Name Discovery -Secure Simple Pairing Supported by IUT] MSC

- Expected Outcome

## Pass verdict

After inquiry, the IUT performs a successful name request procedure.

## 4.6.5 Bonding -Central

Verify the correct behavior in this mode. The role of the IUT is Central and initiator.

Applicable only for IUTs supporting initiation of dedicated bonding and initiation of limited or general inquiry.

## GAP/IDLE/BON/BV-02-C [Bonding -Central]

- Test Purpose

Verify that, if the bonding procedure is required by upper layer of the IUT with the reason only to create and exchange a link key (dedicated bonding), it performs the dedicated bonding procedure.

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor.

- Reference

## 1 6.5

- Initial Condition
- -The Preamble ' Inquiry procedure ' is performed with supported security mode 2 or 4 of the IUT.
- -The Lower Tester ' s LMP features include:
- Feature bit 51 (Secure Simple Pairing) set to 1
- Feature bit 63 (Extended Features) set to 1
- Feature bit 64 (Secure Simple Pairing -Host Support) set to 0

Figure 4.76: GAP/IDLE/BON/BV-02-C [Bonding -Central] MSC

1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the dedicated bonding procedure.
2. Afterwards, the Dedicated Bonding procedure is performed successfully.
- Expected Outcome

## Pass verdict

After the authentication is completed, the IUT has sent an "LMP\_DETACH" message.

Verify that the resulting link key is a combination key.

## 4.6.6 Dedicated Bonding test cases GAP/IDLE/BON/BV-03-C [Dedicated Bonding]

- Test Purpose

Verify that dedicated bonding is performed.

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor.

- Reference

## 1 6.5

- Initial Condition
- -The Preamble ' Inquiry procedure ' is performed with security mode 4 of the IUT.
- -The Lower Tester ' s LMP features include:
- Feature bit 51 (Secure Simple Pairing) set to 1
- Feature bit 63 (Extended Features) set to 1
- Feature bit 64 (Secure Simple Pairing -Host Support) set to 1
- -The Lower Tester's IO capabilities are set to 'DisplayYesNo'.
- -The Lower Tester ' s Authentication\_Requirements set to ' MITM protection not required -Dedicated Bonding ' (0x02).

Figure 4.77: GAP/IDLE/BON/BV-03-C [Dedicated Bonding] MSC

1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the dedicated bonding procedure.
2. Afterwards, the Dedicated Bonding procedure is performed successfully.
- Expected Outcome

## Pass verdict

After the authentication is completed, the IUT has sent an ' LMP\_DETACH ' message.

Verify that the Authentication\_Requirements parameter received from the IUT is either: 0x02 (MITM Protection Not Required -Dedicated Bonding)

or

0x03 (MITM Protection Required -Dedicated Bonding).

If the Authentication\_Requirements parameter is 0x02, verify that the link key is an unauthenticated combination key. If the Authentication\_Requirements parameter is 0x03, verify that the link key is an authenticated combination key.

## GAP/IDLE/BON/BV-04-C [Dedicated Bonding -Authenticated Link Key]

## · Test Purpose

Verify that dedicated bonding is performed.

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor.

- Reference

[1] 6.5

- Initial Condition
- -The Preamble ' Inquiry procedure ' is performed.
- -The Lower Tester ' s LMP features include:
- Feature bit 51 (Secure Simple Pairing) set to 1
- Feature bit 63 (Extended Features) set to
- Feature bit 64 (Secure Simple Pairing -Host Support) set to 1
- -The Lower Tester's IO capabilities are set to 'DisplayYesNo'.
- -The Lower Tester ' s Authentication\_Requirements set to ' MITM protection required -Dedicated Bonding ' (0x03).

Figure 4.78: GAP/IDLE/BON/BV-04-C [Dedicated Bonding -Authenticated Link Key] MSC

1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the dedicated bonding procedure.
2. Afterwards, the Dedicated Bonding procedure is performed successfully.
- Expected Outcome

## Pass verdict

After the authentication is completed, the IUT has sent an ' LMP\_DETACH ' message.

Verify that the Authentication\_Requirements parameter received from the IUT is either: 0x02 (MITM Protection Not Required -Dedicated Bonding) or 0x03 (MITM Protection Required -Dedicated Bonding).

Verify that the resulting link key is an authenticated combination key.

## 4.6.7 General Bonding test cases

## GAP/IDLE/BON/BV-05-C [General Bonding]

- Test Purpose

Verify that general bonding is performed.

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor.

- Reference

[1] 6.5

- Initial Condition
- -The Preamble ' Inquiry procedure ' is performed with security mode 4 of the IUT.
- -The Lower Tester ' s LMP features include:
- Feature bit 51 (Secure Simple Pairing) set to 1
- Feature bit 63 (Extended Features) set to 1
- Feature bit 64 (Secure Simple Pairing -Host Support) set to 1
- -The Lower Tester's IO capabilities are set to 'DisplayYesNo'.
- -The Lower Tester ' s Authentication\_Requirements set to ' MITM protection no required -General Bonding ' (0x04).

Figure 4.79: GAP/IDLE/BON/BV-05-C [General Bonding] MSC

1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the general bonding procedure.
2. Afterwards, the General Bonding procedure is performed successfully.
- Expected Outcome

## Pass verdict

After the authentication is completed, the IUT has sent an ' L2CAP\_CONNECTION\_REQ ' message.

Verify that the Authentication\_Requirements parameter received from the IUT is either: 0x04 (MITM Protection Not Required -General Bonding) or 0x05 (MITM Protection Required -General Bonding).

If the Authentication\_Requirements parameter is 0x04, verify that the link key is an unauthenticated combination key. If the Authentication\_Requirements parameter is 0x05, verify that the link key is an authenticated combination key.

## GAP/IDLE/BON/BV-06-C [General Bonding -Authenticated Link Key]

- Test Purpose

Verify that general bonding is performed.

The IUT is Central and initiator of the bonding procedure. The Lower Tester is Peripheral and acceptor.

- Reference

## 1 6.5

- Initial Condition
- -The Preamble ' Inquiry procedure ' is performed with security mode 4 of the IUT.
- -The Lower Tester ' s LMP features include:
- Feature bit 51 (Secure Simple Pairing) set to 1
- Feature bit 63 (Extended Features) set to 1
- Feature bit 64 (Secure Simple Pairing -Host Support) set to 1
- -The Lower Tester 's IO capabilities are set to 'DisplayYesNo'.
- -The Lower Tester ' s Authentication\_Requirements are set to ' MITM Protection Required -General Bonding ' (0x05).

Figure 4.80: GAP/IDLE/BON/BV-06-C [General Bonding -Authenticated Link Key] MSC

1. After the Preamble, the IUT is ordered by the Upper Tester to initiate the general bonding procedure.
2. Afterwards, the General Bonding procedure is performed successfully.
- Expected Outcome

## Pass verdict

After the authentication is completed, the IUT has sent an ' L2CAP\_CONNECTION\_REQ ' message.

Verify that the Authentication\_Requirements parameter received from the IUT is either: 0x04 (MITM Protection Not Required -General Bonding) or 0x05 (MITM Protection Required -General Bonding).

Verify that the resulting link key is an authenticated combination key.

## 4.6.8 Link Establishment -Central

Verify the correct behavior in this mode. The role of the IUT is Central and initiator.

## GAP/EST/LIE/BV-02-C [Link Establishment -Initiator]

- Test Purpose

Verify that the IUT performs a link establishment procedure, initiated by itself.

The IUT is Central and initiator. The Lower Tester is Peripheral and acceptor of the link establishment procedure.

- Reference

[1] 7.1

- Initial Condition
- -The IUT is in Baseband state ' Standby ' and in Idle mode.
- -The Lower Tester is in the Discoverable mode.
- -The Preamble for ' Inquiry procedure ' is performed.

## · Test Procedure

Figure 4.81: GAP/EST/LIE/BV-02-C [Link Establishment -Initiator] MSC

- Expected Outcome

## Pass verdict

For completion of the link establishment a mutual ' LMP\_SETUP\_COMPLETE ' occurs.

## 4.7 Operational modes and procedures for use on LE physical channels

## 4.7.1 Broadcasting and Observing

Verify the correct implementation of the Broadcast Mode and Observation procedure.

## 4.7.1.1 Broadcast mode

Verify the correct implementation of the Broadcast mode.

## GAP/BROB/BCST/BV-01-C [Broadcast mode, No Scan Response]

- Test Purpose

Verify that the IUT in Broadcast mode does not implement scan response data; the peer device is Passive Scanning.

- Reference

[4], [6], [9] 9.1.1, 9.1.1.2

## 7 1.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The advertising data in Broadcast mode for the IUT is defined by the TSPX\_advertising\_data IXIT value.
- Test Procedure
1. The Lower Tester performs the Observation procedure using Passive Scanning.
2. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data.
- Expected Outcome

Figure 4.82: GAP/BROB/BCST/BV-01-C [Broadcast mode, no scan response] MSC

## Pass verdict

The Lower Tester receives non-connectable advertising events sent by the IUT.

The Lower Tester receives the specified advertising data sent from the IUT.

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0.

- Notes

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## GAP/BROB/BCST/BV-02-C [Broadcast mode, Scan Response]

- Test Purpose

Verify that the IUT is in Broadcast mode and implements scan response data; the peer device is Active Scanning.

- Reference

[4] 9.1.1

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The advertising data in Broadcast mode is specified for the IUT as defined by the TSPX\_advertising\_data IXIT value.
- Test Procedure
1. The Lower Tester performs the Observation procedure using Active Scanning.
2. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data.
- Expected Outcome

Figure 4.83: GAP/BROB/BCST/BV-02-C [Broadcast mode, scan response] MSC

## Pass verdict

The Lower Tester receives scannable advertising events sent by the IUT.

The Lower Tester receives the specified advertising data and scan response data sent from the IUT.

The advertising data or scan response data either does not contains the Flags AD type or contains the Flags AD type but the LE Limited Discoverable Flag and the LE General Discoverable Flag are not set.

- Notes

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## GAP/BROB/BCST/BV-03-C [Broadcast mode, Resolvable Private Address]

- Test Purpose

Verify that the IUT in Broadcast mode is using a resolvable private address.

- Reference
- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections.
- -The advertising data in Broadcast mode is specified by the TSPX\_advertising\_data IXIT value.
- -The Device Identity (IRK and Identity Address) used in the Resolvable Private Address Generation procedure and Resolvable Private Address Resolution procedure is specified by the TSPX\_iut\_device\_IRK\_for\_resolvable\_privacy\_address\_generation\_procedure and TSPX\_identity\_address IXIT values for the IUT. Alternatively, the IUT may use a Device Identity distributed to the Lower Tester prior to executing this test procedure.
- Test Procedure
1. The Lower Tester performs the Observation procedure using Passive Scanning.
2. The IUT generates a resolvable private address using the Resolvable Private Address Generation procedure.
3. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data; the IUT advertises using a generated resolvable private address.

```
[4], [6], [9] 9.1.1, 9.1.1.2 [7] 1.3 [9] 10.7 [11] 1.3.2.3
```

Figure 4.84: GAP/BROB/BCST/BV-03-C [Broadcast mode, Resolvable Private Address] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives non-connectable advertising events sent by the IUT.

The Lower Tester receives the specified advertising data sent from the IUT.

The Lower Tester successfully resolves the private address (the private address is associated with the IUT) received in the advertising events using the Resolvable Private Address Resolution procedure.

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0.

- Notes

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## GAP/BROB/BCST/BV-04-C [Broadcast mode, Non-Resolvable Private Address]

- Test Purpose

Verify that the IUT in Broadcast mode is using a non-resolvable private address.

- Reference

[6], [9] 10.7.3, 9.1.1.2

## 7 1.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The advertising data in Broadcast mode is specified for the IUT in the TSPX\_advertising\_data IXIT value.
- -TGAP (private\_addr\_int) for the IUT is specified in the TSPX\_iut\_private\_address\_interval IXIT value.
- Test Procedure
1. The Lower Tester performs the Observation procedure using Passive Scanning.
2. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising data; the IUT generates a non-resolvable private address using the non-resolvable Private Address Generation procedure and advertises using the generated non-resolvable private address.

Figure 4.85: GAP/BROB/BCST/BV-04-C [Broadcast mode, Non-Resolvable Private Address] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives non-connectable advertising events sent by the IUT.

The Lower Tester receives the specified advertising data sent from the IUT that includes the nonresolvable private address.

The Lower Tester verifies that the IUT changes the non-resolvable private address in the advertiser address of the received advertising events after TGAP(private\_addr\_int).

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0.

- Notes

Since broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## GAP/BROB/BCST/BV-05-C [Broadcast mode, Resolvable Private Address, Scan Response]

- Test Purpose

Verify that the IUT in Broadcast mode implements scan response data using a resolvable private address; the Lower Tester is Active Scanning. Lower Tester and IUT are using Resolvable Private Addresses and Filter Accept List.

- Reference
- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections.

```
[7] 1.3 [9] 9.1.1, 10.7.3, 9.1.1.2
```

- -The advertising data in Broadcast mode is specified for the IUT in the TSPX\_advertising\_data IXIT value.
- -The Lower Tester and the IUT have exchanged bonding information for resolving.
- Test Procedure
1. The Lower Tester performs the Observation procedure using Active Scanning.
2. The Upper Tester adds the device identity of the Lower Tester to the Resolving List.
3. The Upper Tester orders the IUT to enter Broadcast mode using the specified advertising and scan response data; the IUT advertises using the generated resolvable private address.
4. The Lower Tester resolves the address of the IUT and sends a scan request to the IUT.
5. The IUT resolves the scan request but the Lower Tester is not in the Filter Accept List, so no scan response is sent.
6. The Upper Tester orders the IUT to add the Lower Tester ' s Identity to the Filter Accept List, and continue advertising using the generated resolvable private address.
7. The Lower Tester resolves the address of the IUT and sends a scan request to the IUT.
8. The IUT resolves the scan request, identifies the Lower Tester on the Filter Accept List, and sends a scan response.

Figure 4.86: GAP/BROB/BCST/BV-05-C [Broadcast mode, Resolvable Private Address, Scan Response] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives scannable advertising events sent by the IUT.

The Lower Tester receives the specified advertising data sent from the IUT.

The Lower Tester successfully resolves the private address (the private address is associated with the IUT) received in the advertising events.

The Lower Tester sends scan requests to the IUT. Before the Lower Tester's identity address is added to the IUT's Filter Accept List, the Lower Tester does not receive any scan response. After adding the Lower Tester's identity address to the IUT's Filter Accept List, the Lower Tester receives the scan responses with the specified scan response data sent from the IUT.

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0.

- Notes

Since broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## 4.7.1.2 Observation procedure

Verify the correct implementation of the Observation procedure.

## GAP/BROB/OBSV/BV-01-C [Observation procedure, Passive Scanning]

- Test Purpose

Verify the IUT performing the Observation procedure using Passive Scanning.

- Reference

[4] 9.1.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The advertising data used in Broadcast mode is specified for the Lower Tester in the TSPX\_advertising\_data IXIT value.
- Test Procedure
1. The Lower Tester enters Broadcast mode using the specified advertising data.
2. The Upper Tester orders the IUT to perform the Observation procedure using Passive Scanning.

Figure 4.87: GAP/BROB/OBSV/BV-01-C [Observation procedure, Passive Scanning] MSC

- Expected Outcome

## Pass verdict

The IUT receives the specified advertising data sent from Lower Tester.

- Notes

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## GAP/BROB/OBSV/BV-02-C [Observation procedure, Active Scanning]

- Test Purpose

Verify the IUT performing the Observation procedure using Active Scanning.

- Reference

[4] 9.1.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The advertising data used in Broadcast mode is specified for the Lower Tester in the TSPX\_advertising\_data IXIT value.
- -The scan response data used in Broadcast mode is specified for the Lower Tester in the TSPX\_scan\_response\_data IXIT value.
- Test Procedure
1. The Lower Tester enters Broadcast mode using the specified advertising data.
2. The Upper Tester orders the IUT to perform the Observation procedure using Active Scanning.

Figure 4.88: GAP/BROB/OBSV/BV-02-C [Observation procedure, Active Scanning] MSC

- Expected Outcome

## Pass verdict

The IUT receives the specified advertising data and scan response data from Lower Tester.

- Notes

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## GAP/BROB/OBSV/BV-05-C [Observation procedure, Active Scanning Non-Resolvable Private Address or Resolvable Private Address]

- Test Purpose

Verify that the IUT can perform the Observation procedure using Active Scanning and a nonresolvable private address or resolvable private address.

- Reference

## 4, [9] 9.1.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The advertising data used in Broadcast mode is specified for the Lower Tester in the TSPX\_advertising\_data IXIT value.
- -The scan response data used in Broadcast mode is specified for the Lower Tester in the TSPX\_scan\_response\_data IXIT value.
- Test Procedure
1. The Lower Tester enters Broadcast mode using scannable undirected advertising events containing the specified advertising data and responds to scan requests using the specified scan response data.
2. The Upper Tester orders the IUT to perform the Observation procedure using Active Scanning and a non-resolvable private address or resolvable private address.

Figure 4.89: GAP/BROB/OBSV/BV-05-C [Observation procedure, Active Scanning Non-Resolvable Private Address or Resolvable Private Address] MSC

- Expected Outcome

## Pass verdict

The IUT receives the specified advertising data and scan response data sent by the Lower Tester.

The Lower Tester receives a non-resolvable private address or a resolvable private address in scan request sent from the IUT.

- Notes

Since the broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## GAP/BROB/OBSV/BV-06-C [Observation procedure with Active Scanning, IUT and Peer using Resolvable Private Address]

- Test Purpose

Verify that the IUT can perform the Observation procedure using Active Scanning when the Lower Tester is using a resolvable private address.

- Reference

[6], [9] 9.1.2, 10.7.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections.
- -The Lower Tester and the IUT have exchanged bonding information for resolving.
- -The advertising and scan response data used in Broadcast mode is specified for the Lower Tester in the TSPX\_advertising\_data and TSPX\_scan\_response\_data IXIT values.
- Test Procedure
1. The Lower Tester generates a resolvable private address using the Resolvable Private Address Generation procedure.
2. The Lower Tester enters Broadcast mode using the specified advertising data and the generated resolvable private address.
3. The Upper Tester orders the IUT to add the Lower Tester's Identity to the resolving list and Filter Accept List.
4. The Upper Tester orders the IUT to perform the Observation procedure using Active Scanning; the IUT resolves the address received in the advertising events sent by the Lower Tester, and sends a Scan Request.
5. The Lower Tester resolves the IUT's address and send the Scan Response.
- Expected Outcome

Figure 4.90: GAP/BROB/OBSV/BV-06-C [Observation procedure with Active Scanning, IUT and Peer using Resolvable Private Address] MSC

## Pass verdict

The IUT successfully resolves the address in the advertising events sent by the Lower Tester.

The IUT receives the Scan Response data correctly.

- Notes

Since broadcasting is not a reliable transmission method, multiple broadcast packets may need to be sent to verify compliance.

## 4.7.2 Discovery modes and procedures

## 4.7.2.1 Non-Discoverable mode

## GAP/DISC/NONM/BV-01-C [Non-Discoverable mode, Non-Connectable mode]

- Test Purpose

Verify that the IUT in Non-Discoverable mode and Non-Connectable mode is not discoverable by a device performing the General Discovery procedure using Active Scanning.

The IUT is operating in the Peripheral role.

- Reference

[4], [6], [9] 9.2.2, 9.2.2.2

## 7 1.3

- Initial Condition
- -The IUT i s in Link Layer state 'Standby'.
- -The IUT is in Non-Connectable mode.
- Test Procedure
1. The Lower Tester performs the General Discovery procedure using Active Scanning.
2. The Upper Tester orders IUT to enter Non-Discoverable mode and Non-Connectable mode.
- Expected Outcome

Figure 4.91: GAP/DISC/NONM/BV-01-C [Non-Discoverable mode, Non-Connectable mode] MSC

## Pass verdict

The Lower Tester receives either no advertising events or non-connectable advertising events from the IUT.

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0.

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

## GAP/DISC/NONM/BV-02-C [Non-Discoverable mode, Undirected Connectable mode]

- Test Purpose

Verify that the IUT in Non-Discoverable mode and Undirected Connectable mode is not discoverable by a device performing the General Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

## 4 9.2.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Undirected Connectable mode.
- Test Procedure
1. The Lower Tester performs the General Discovery procedure.
2. The Upper Tester orders IUT to enter Non-Discoverable mode and Undirected Connectable mode.
- Expected Outcome

Figure 4.92: GAP/DISC/NONM/BV-02-C [Non-Discoverable mode, Undirected Connectable mode] MSC

## Pass verdict

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT.

If the advertising data includes the Flags AD type, both the LE General Discoverable Mode and LE Limited Discoverable Mode flags are set to 0.

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

## 4.7.2.2 Limited Discoverable mode

## GAP/DISC/LIMM/BV-01-C [Limited Discoverable mode, Non-Connectable mode -BR/EDR/LE]

- Test Purpose

Verify that the IUT in Limited Discoverable mode and the Non-Connectable mode can be discovered by a device performing the Limited Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.2.3, 13.1.1.2, 9.2.3.2

[6], [9] 9.2.3, 13.1.1

[7] 1.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Non-Connectable mode.
- -TGAP(lim\_adv\_timeout) for the IUT is specified in the TSPX\_lim\_adv\_timeout IXIT value.
- Test Procedure

The Upper Tester orders the IUT to enter Limited Discoverable mode and Non-Connectable mode.

Figure 4.93: GAP/DISC/LIMM/BV-01-C [Limited Discoverable mode, Non-Connectable mode -BR/EDR/LE] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives non-connectable advertising events from the IUT.

The advertising data contains the Flags AD type as follows:

- Limited Discoverable flag set to 1
- General Discoverable flag set to 0
- BR/EDR Not Supported flag set to 0
- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

Within TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, if the Lower Tester receives advertising data from the IUT containing the Flags AD type, the General Discoverable Flag is set to 0 and the Limited Discoverable Flag set to 1.

After TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type as described:

- -Limited Discoverable flag set to 1
- -General Discoverable flag set to 0
- -BR/EDR Not Supported flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

## GAP/DISC/LIMM/BV-02-C [Limited Discoverable mode, Undirected Connectable mode -BR/EDR/LE]

- Test Purpose

Verify that the IUT in Limited Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the Limited Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.2.3, 13.1.1

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Undirected Connectable mode.
- -TGAP(lim\_adv\_timeout) is specified for the IUT in the TSPX\_lim\_adv\_timeout IXIT value.
- Test Procedure

The Upper Tester orders the IUT to enter Limited Discoverable mode and Undirected Connectable mode.

Figure 4.94: GAP/DISC/LIMM/BV-02-C [Limited Discoverable mode, Undirected Connectable mode -BR/EDR/LE] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT.

The advertising data received by the Lower Tester contains the Flags AD type as described:

- -Limited Discoverable flag set to 1
- -General Discoverable flag set to 0
- -BR/EDR Not Supported flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

Within TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester receives advertising data from the IUT containing the Flags AD type as described:

- -Limited Discoverable flag set to 1
- -General Discoverable flag set to 0
- -BR/EDR Not Supported flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

After TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type with the Limited Discoverable Flag set to 1.

## GAP/DISC/LIMM/BV-03-C [Limited Discoverable mode, Non-Connectable mode -LE Only]

- Test Purpose

Verify that an LE only IUT in Limited Discoverable mode and the Non-Connectable mode can be discovered by a device performing the Limited Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4], [6], [9] 9.2.3, 9.2.3.2

[7] 1.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Non-Connectable mode.
- -TGAP(lim\_adv\_timeout) for the IUT is specified in the TSPX\_lim\_adv\_timeout IXIT value.
- Test Procedure

The Upper Tester orders the IUT to enter Limited Discoverable mode and Non-Connectable mode.

Figure 4.95: GAP/DISC/LIMM/BV-03-C [Limited Discoverable mode, Non-Connectable mode -LE Only] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives non-connectable advertising events from the IUT.

The advertising data contains the Flags AD type as follows:

- Limited Discoverable flag set to 1
- General Discoverable flag set to 0
- BR/EDR Not Supported flag set to 1
- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

Within TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester receives advertising data from the IUT containing the Flags AD type as described:

- -Limited Discoverable flag set to 1
- -General Discoverable flag set to 0
- -BR/EDR Not Supported flag set to 1
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

After TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type with the Limited Discoverable Flag set to 1.

## GAP/DISC/LIMM/BV-04-C [Limited Discoverable mode, Undirected Connectable mode -LE Only]

- Test Purpose

Verify that an LE only IUT in Limited Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the Limited Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.2.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Undirected Connectable mode.
- -TGAP(lim\_adv\_timeout) is specified for the IUT in the TSPX\_lim\_adv\_timeout IXIT value.
- Test Procedure

The Upper Tester orders the IUT to enter Limited Discoverable mode and Undirected Connectable mode.

Figure 4.96: GAP/DISC/LIMM/BV-04-C [Limited Discoverable mode, Undirected Connectable mode -LE Only] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT.

The advertising data received by the Lower Tester contains the Flags AD type as described:

- -Limited Discoverable flag set to 1
- -General Discoverable flag set to 0
- -BR/EDR Not Supported flag set to 1
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

Within TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester receives advertising data from the IUT containing the Flags AD type as described:

- -Limited Discoverable flag set to 1
- -General Discoverable flag set to 0
- -BR/EDR Not Supported flag set to 1
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

After TGAP(lim\_adv\_timeout) from the time the IUT enters Limited Discoverable mode, the Lower Tester does not receive any advertising data from the IUT containing the Flags AD type with the Limited Discoverable Flag set to 1.

## 4.7.2.3 General Discoverable mode

## GAP/DISC/GENM/BV-01-C [General Discoverable mode, Non-Connectable mode -BR/EDR/LE]

- Test Purpose

Verify that the IUT in General Discoverable mode and the Non-Connectable mode can be discovered by a device performing the General Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.2.4, 9.2.4.2, 13.1.1.2

[6], [9] 9.2.4, 13.1.1

## 7 1.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Non-Connectable mode.
- -The Lower Tester performs the General Discovery procedure.
- Test Procedure

The Upper Tester orders IUT to enter General Discoverable mode and Non-Connectable mode.

Figure 4.97: GAP/DISC/GENM/BV-01-C [General Discoverable mode, Non-Connectable mode -BR/EDR/LE] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives non-connectable advertising events from the IUT.

The advertising data contains the Flags AD type as follows:

- Limited Discoverable flag set to 0
- General Discoverable flag set to 1
- BR/EDR Not Supported flag set to 0
- Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

## GAP/DISC/GENM/BV-02-C [General Discoverable mode, Undirected Connectable mode -BR/EDR/LE]

- Test Purpose

Verify that the IUT in General Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the General Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.2.4, 13.1.1

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Undirected Connectable mode.
- -The Lower Tester performs the General Discovery procedure.
- Test Procedure

The Upper Tester orders the IUT to enter General Discoverable mode and Undirected Connectable mode.

Figure 4.98: GAP/DISC/GENM/BV-02-C [General Discoverable mode, Undirected Connectable mode -BR/EDR/LE] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT.

The advertising data received by the Lower Tester contains the Flags AD as described:

- -Limited Discoverable flag set to 0
- -General Discoverable flag set to 1

- -BR/EDR Not Supported flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

## GAP/DISC/GENM/BV-03-C [General Discoverable mode, Non-Connectable mode -LE Only]

- Test Purpose

Verify that an LE only IUT in General Discoverable mode and the Non-Connectable mode can be discovered by a device performing the General Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.2.4, 9.2.4.2. 13.1.1.2

[6], [9] 9.2.4, 13.1.1

[7] 1.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Non-Connectable mode.
- -The Lower Tester performs the General Discovery procedure.
- Test Procedure

The Upper Tester orders the IUT to enter General Discoverable mode and Non-Connectable mode.

Figure 4.99: GAP/DISC/GENM/BV-03-C [General Discoverable mode, Non-Connectable mode -LE Only] MSC

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

## GAP/DISC/GENM/BV-04-C [General Discoverable mode, Undirected Connectable mode -LE Only]

- Test Purpose

Verify that an LE only IUT in General Discoverable mode and the Undirected Connectable mode can be discovered by a device performing the General Discovery procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.2.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The IUT is in Undirected Connectable mode.
- -The Lower Tester performs the General Discovery procedure.
- Test Procedure

The Upper Tester orders the IUT to enter General Discoverable mode and Undirected Connectable mode.

Figure 4.100: GAP/DISC/GENM/BV-04-C [General Discoverable mode, Undirected Connectable mode -LE Only] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT.

The advertising data received by the Lower Tester contains the Flags AD type as described:

- -Limited Discoverable flag set to 0
- -General Discoverable flag set to 1
- -BR/EDR Not Supported flag set to 1
- -Simultaneous LE and BR/EDR to Same Device Capable (Controller) flag set to 0
- -Simultaneous LE and BR/EDR to Same Device Capable (Host) flag set to 0

If the Flags AD type is present in the advertising data then it only appears once per advertising event.

The Flags AD type is not present in any scan response data received.

## 4.7.2.4 Limited Discovery procedure

## GAP/DISC/LIMP/BV-01-C [Limited Discovery procedure, find Limited Discoverable device]

- Test Purpose

Verify that the IUT can perform the Limited Discovery procedure to find a device in the Limited Discoverable mode.

The IUT is operating in the Central role.

- Reference

## 4 9.2.5

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(lim\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_lim\_disc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters Limited Discoverable mode.
2. The Upper Tester orders the IUT to perform the Limited Discovery procedure.

Figure 4.101: GAP/DISC/LIMP/BV-01-C [Limited Discovery procedure, find Limited Discoverable device] MSC

- Expected Outcome

## Pass verdict

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN\_REQ is a nonresolvable private address.

The IUT lists the Lower Tester during the discovery period.

## GAP/DISC/LIMP/BV-02-C [Limited Discovery procedure does not find General Discoverable device]

- Test Purpose

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the General Discoverable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.5

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -TGAP(gen\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_gen\_disc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters General Discoverable mode.
2. The Upper Tester orders the IUT to perform the Limited Discovery procedure.

Figure 4.102: GAP/DISC/LIMP/BV-02-C [Limited Discovery procedure does not find general discoverable device] MSC

- Expected Outcome

## Pass verdict

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN\_REQ is a nonresolvable private address.

The IUT does not discover the Lower Tester during the discovery period.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DISC/LIMP/BV-03-C [Limited Discovery procedure does not find Broadcast device]

- Test Purpose

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the Broadcast mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.5

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(lim\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_lim\_disc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters Broadcast mode.
2. The Upper Tester orders the IUT to perform the Limited Discovery procedure.

Figure 4.103: GAP/DISC/LIMP/BV-03-C [Limited Discovery procedure does not find Broadcast device] MSC

- Expected Outcome

## Pass verdict

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN\_REQ is a nonresolvable private address.

The IUT does not discover the Lower Tester during the discovery period.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DISC/LIMP/BV-04-C [Limited Discovery procedure does not find Undirected Connectable device]

- Test Purpose

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the Undirected Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.5

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(lim\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_lim\_disc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters Undirected Connectable mode; the Lower Tester does not include the Flags AD type in the advertising data with either the General Discoverable Flag or Limited Discoverable Flag set to 1.
2. The Upper Tester orders the IUT to perform the Limited Discovery procedure.

Figure 4.104: GAP/DISC/LIMP/BV-04-C [Limited Discovery procedure does not find Undirected Connectable device] MSC

- Expected Outcome

## Pass verdict

The IUT does not discover the Lower Tester during the discovery period.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DISC/LIMP/BV-05-C [Limited Discovery procedure does not find Directed Connectable device]

- Test Purpose

Verify that the IUT can perform the Limited Discovery procedure and does not find a device in the Directed Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.5

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(lim\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_lim\_disc\_scan\_min IXIT value.
- -The initiator address for the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders the IUT to perform the Limited Discovery procedure.
2. The Lower Tester enters Directed Connectable mode using the specified initiator address for the IUT.

Figure 4.105: GAP/DISC/LIMP/BV-05-C [Limited Discovery procedure does not find Directed Connectable device] MSC

- Expected Outcome

## Pass verdict

The IUT does not discover the Lower Tester during the discovery period.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## 4.7.2.5 General Discovery procedure

## GAP/DISC/GENP/BV-01-C [General Discovery procedure, finding General Discoverable device]

- Test Purpose

Verify that the IUT can perform the General Discovery procedure and can find a device in the General Discoverable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.6

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(gen\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_gen\_disc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters General Discoverable mode.
2. The Upper Tester orders IUT to start the General Discovery procedure.

Figure 4.106: GAP/DISC/GENP/BV-01-C [General Discovery procedure finding General Discoverable device] MSC

- Expected Outcome

## Pass verdict

The IUT discovers the Lower Tester during the General Discovery procedure.

## GAP/DISC/GENP/BV-02-C [General Discovery procedure, finding Limited Discoverable device]

- Test Purpose

Verify that the IUT can perform the General Discovery procedure and can find devices in the Limited Discoverable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.6

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(gen\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_gen\_disc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters Limited Discoverable mode.
2. The Upper Tester orders the IUT to start the General Discovery procedure.

Figure 4.107: GAP/DISC/GENP/BV-02-C [General Discovery procedure finding Limited Discoverable device] MSC

- Expected Outcome

## Pass verdict

The IUT lists the Lower Tester during the discovery period.

## GAP/DISC/GENP/BV-03-C [General Discovery procedure does not find Broadcast device]

- Test Purpose

Verify that the IUT can perform the General Discovery procedure and does not find a device in the Broadcast mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.6

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(gen\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_gen\_disc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters Broadcast mode.
2. The Upper Tester orders the IUT to perform the General Discovery procedure.

Figure 4.108: GAP/DISC/GENP/BV-03-C [General Discovery procedure does not find Broadcast device] MSC

- Expected Outcome

## Pass verdict

The IUT does not discover the Lower Tester during the discovery period.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DISC/GENP/BV-04-C [General Discovery procedure does not find Undirected Connectable device]

- Test Purpose

Verify that the IUT can perform the General Discovery procedure and does not find a device in the Undirected Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.6

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(gen\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_gendisc\_scan\_min IXIT value.
- Test Procedure
1. The Lower Tester enters Undirected Connectable mode; the Lower Tester does not include the Flags AD Type in the advertising data with either the General Discoverable Flag or Limited Discoverable Flag set to 1.
2. The Upper Tester orders the IUT to perform the General Discovery procedure.

Figure 4.109: GAP/DISC/GENP/BV-04-C [General Discovery procedure does not find Undirected Connectable device] MSC

- Expected Outcome

## Pass verdict

The IUT does not discover the Lower Tester during the discovery period.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DISC/GENP/BV-05-C [General Discovery procedure does not find Directed Connectable device]

- Test Purpose

Verify that the IUT can perform the General Discovery procedure and does not find a device in the Directed Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.2.6

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -TGAP(gen\_disc\_scan\_min) for the IUT is specified in the TSPX\_Tgap\_gen\_disc\_scan\_min IXIT value.
- -The initiator address for the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Lower Tester enters Directed Connectable mode using the specified initiator address for the IUT.
2. The Upper Tester orders the IUT to perform the General Discovery procedure.

Figure 4.110: GAP/DISC/GENP/BV-05-C [General Discovery procedure does not find Directed Connectable device] MSC

- Expected Outcome

## Pass verdict

The IUT does not discover the Lower Tester during the discovery period.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## 4.7.2.6 Name Discovery procedure

## GAP/IDLE/NAMP/BV-01-C [Name Discovery procedure, GATT Client]

- Test Purpose

Verify that the IUT can perform the Name Discovery procedure and retrieve the device name from a peer device.

The IUT is operating as the GATT client.

- Reference

## 4 9.2.7

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in the role specified in the TSPX\_gap\_iut\_role IXIT entry.
- -The Lower Tester and IUT are connected.
- -The Lower Tester is a GATT server and exposes the Device Name characteristic.
- -The Device Name Characteristic value for the Lower Tester is specified in the TSPX\_device\_name IXIT value.

- Test Procedure

The Upper Tester orders the IUT to perform the Name Discovery procedure.

Figure 4.111: GAP/IDLE/NAMP/BV-01-C [Name Discovery procedure, GATT Client] MSC

- Expected Outcome

## Pass verdict

The IUT retrieves the specified Device Name from the Lower Tester.

## GAP/IDLE/NAMP/BV-02-C [Name Discovery procedure, GATT Server]

- Test Purpose

Verify that the IUT can support the Name Discovery procedure and allow a peer device to retrieve the device name.

The IUT is operating as the GATT Server.

- Reference

[4] 9.2.7

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in the role specified in the TSPX\_gap\_iut\_role IXIT entry.
- -The Lower Tester and IUT are connected.
- -The IUT is a GATT server and exposes the Device Name characteristic.
- -The Device Name Characteristic value for the IUT is specified in the TSPX\_device\_name IXIT value.

- Test Procedure

The Lower Tester performs the Name Discovery procedure.

Figure 4.112: GAP/IDLE/NAMP/BV-02-C [Name Discovery procedure, GATT Server] MSC

- Expected Outcome

## Pass verdict

The Lower Tester retrieves the specified Device Name from the IUT.

## 4.7.2.7 Discovery of devices with Resolvable Private Address

## GAP/DISC/RPA/BV-01-C [Discovery procedure, find discoverable device using Resolvable Private Address]

- Test Purpose

Verify that the IUT can perform any of the Discovery procedures to find a device in any of the Discoverable modes, when resolvable private addresses are used.

The IUT is operating in the Central role.

- Reference

[9] 9.2.5, 10.7, 10.7.2.1

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT and the Lower Tester are paired using either LE Legacy or LE Secure Connections.
- -The Lower Tester and the IUT have exchanged bonding information for resolving.
- Test Procedure
1. The Lower Tester generates a resolvable private address using the Resolvable Private Address Generation procedure.
2. The Lower Tester enters Limited Discoverable mode or General Discoverable mode.
3. The Upper Tester orders the IUT to add the Lower Tester's Identity to the resolving list.
4. The Upper Tester orders the IUT to perform the Limited Discovery procedure or the General Discovery procedure.

Figure 4.113: GAP/DISC/RPA/BV-01-C [Discovery procedure, find discoverable device using Resolvable Private Address] MSC

- Expected Outcome

## Pass verdict

The IUT lists the Lower Tester during the discovery period by its identity address.

## 4.7.3 Connection modes and procedures

## 4.7.3.1 Non-Connectable mode

## GAP/CONN/NCON/BV-01-C [Non-Connectable mode]

- Test Purpose

Verify that the IUT in the Non-Connectable mode does not allow another device performing the Direct Connection Establishment procedure to connect.

The IUT is operating in the Broadcaster role or the Peripheral role or the Observer role.

- Reference

[4] 9.3.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address for the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders IUT to enter Non-Connectable mode.
2. The Lower Tester performs the Direct Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the specified public/static address for the IUT.

Figure 4.114: GAP/CONN/NCON/BV-01-C [Non-Connectable mode] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives either no advertising events or non-connectable advertising events from IUT whilst in Non-Connectable mode.

For IUT acting in the Broadcaster role, the Lower Tester receives non-connectable advertising events from IUT whilst broadcasting data in Non-Connectable mode.

In each advertising event received the advertiser address is set to the specified public/static address for the IUT.

The Lower Tester fails to establish a connection with the IUT.

## GAP/CONN/NCON/BV-02-C [Non-Connectable mode, General Discoverable mode]

- Test Purpose

Verify that the IUT in the Non-Connectable mode and General Discoverable mode does not allow a connection to be established with another device.

The IUT is operating in the Peripheral role.

- Reference

## 4 9.3.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders the IUT to enter General Discoverable mode.
2. The Upper Tester orders the IUT to enter Non-Connectable mode.
3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the specified public/static address.

Figure 4.115: GAP/CONN/NCON/BV-02-C [Non-Connectable mode, General Discoverable mode] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives non-connectable advertising events from IUT whilst in Non-Connectable mode and General Discoverable mode.

In each advertising event received the advertiser address is set to the specified public/static address for the IUT.

The Lower Tester fails to establish a connection with the IUT.

## GAP/CONN/NCON/BV-03-C [Non-Connectable mode, Limited Discoverable mode]

- Test Purpose

Verify that the IUT in the Non-Connectable mode and Limited Discoverable mode does not allow a connection to be established with another device.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.3.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders the IUT to enter Limited Discoverable mode.
2. The Upper Tester orders the IUT to enter Non-Connectable mode.
3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the specified public/static address for the IUT.

Figure 4.116: GAP/CONN/NCON/BV-03-C [Non-Connectable mode, Limited Discoverable mode] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives non-connectable advertising events from the IUT while in NonConnectable mode and Limited Discoverable mode.

In each advertising event received the advertiser address is set to the specified public/static address for the IUT.

The Lower Tester fails to establish a connection with the IUT.

## 4.7.3.2 Directed Connectable mode

## GAP/CONN/DCON/BV-01-C [Directed Connectable mode]

- Test Purpose

Verify that the IUT in the Directed Connectable mode can connect with another device performing the General Connection Establishment procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.3.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received advertiser address.
2. The Upper Tester orders IUT to enter Direct Connectable m ode; the IUT sets the advertiser's address to the public/static address of the IUT and sets the initiator address to the public/static address of the Lower Tester.
3. The Lower Tester or the IUT terminates the connection.

Figure 4.117: GAP/CONN/DCON/BV-01-C [Directed Connectable mode] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives connectable directed advertising events from IUT during the period that the IUT is in Directed Connectable mode.

In each connectable directed advertising event received the advertiser address is set to the public/static address of the IUT and the initiator address is set to the public/static address of the Lower Tester.

The Lower Tester establishes a connection with the IUT using the received advertiser address.

The Lower Tester or IUT successfully terminates the connection.

## GAP/CONN/DCON/BV-04-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution]

- Test Purpose

Verify that the IUT in the Directed Connectable mode using a Resolvable Private Address can connect with another device using a Resolvable Private Address performing the General Connection Establishment procedure when the other device indicates support for Central Address Resolution.

The IUT is operating in the Peripheral role.

- Reference

[9] 9.3.3, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Privacy mode.
- -The Lower Tester exposes the Central Address Resolution characteristic which is set to 1.
- -TGAP(private\_addr\_int) for the IUT is specified in the TSPX\_iut\_private\_address\_interval IXIT value.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.

- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Tester ' s Device Identity to the resolving list.
2. The Upper Tester orders the IUT to enter General Connectable mode.
3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received advertiser address.
4. When connected, the IUT optionally reads the value of the Central Address Resolution characteristic.
5. The Lower Tester or the IUT terminates the connection.
6. The Upper Tester orders the IUT to enter Direct Connectable mode targeting the Lower Tester by its identity address.
7. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; upon receiving the directed advertisement, the Lower Tester resolves the initiator and advertiser address, and set the advertiser address equivalent to the resolved advertiser address when creating the connection to the IUT.
8. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.
- Expected Outcome

Figure 4.118: GAP/CONN/DCON/BV-04-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution] MSC

## Pass verdict

In each connectable directed advertising event received by the Lower Tester, the advertiser address is set to a resolvable private address for the IUT and the initiator address is set to a generated resolvable private address based on the device identity of the Lower Tester.

The Lower Tester establishes a connection with the IUT using a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request.

## GAP/CONN/DCON/BV-05-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution not supported]

- Test Purpose

Verify that the IUT does not initiate the Directed Connectable mode using a Resolvable Private Address, towards another privacy enabled device, which does not indicate support for Central Address Resolution.

The IUT is operating in the Peripheral role.

- Reference

[9] 9.3.3, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT is in Privacy mode.
- -The Lower Tester may expose the Central Address Resolution characteristic. If present it is set to 0.
- -TGAP(private\_addr\_int) for the IUT is specified in the TSPX\_iut\_private\_address\_interval IXIT value.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.
- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list.
2. The Upper Tester orders the IUT to enter General Connectable mode.
3. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received advertiser address.
4. When connected, the IUT optionally reads the value of the Central Address Resolution characteristic of the Lower Tester.
5. The Lower Tester or the IUT terminates the connection.
6. The Upper Tester orders the IUT to enter Direct Connectable mode targeting the Lower Tester by its identity address.
7. The IUT refuses the order. The IUT might enter another connectable mode and establish the connection this way.

Figure 4.119: GAP/CONN/DCON/BV-05-C [Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution not supported] MSC

- Expected Outcome

## Pass verdict

The Lower Tester does not establish a connection with the IUT based on directed advertisement.

## 4.7.3.3 Undirected Connectable mode

## GAP/CONN/UCON/BV-01-C [Undirected Connectable mode, Non-Discoverable mode]

- Test Purpose

Verify that the IUT in Undirected Connectable mode can connect with another device performing the General Connection Establishment procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.3.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates a connection using the advertiser's address in the received advertising events from the IUT.
2. The Upper Tester orders IUT to enter Undirected Connectable mode and Non-Discoverable mode; the IUT sets the advertiser address to the public/static address of the IUT.

Figure 4.120: GAP/CONN/UCON/BV-01-C [Undirected Connectable mode, Non-Discoverable mode] MSC

- Expected Outcome

## Pass verdict

The IUT sends either connectable and scannable undirected advertising events or connectable undirected advertising events.

In each advertising event received the advertiser address is set to the specified public/static address for the IUT.

The Lower Tester establishes a connection with IUT.

## GAP/CONN/UCON/BV-02-C [Undirected Connectable mode, General Discoverable mode]

- Test Purpose

Verify that the IUT in Undirected Connectable mode and General Discoverable mode can connect with another device performing the General Connection Establishment procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.3.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'
- -The public/static address for the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders IUT to enter Undirected Connectable mode and General Discoverable mode; the IUT sets the advertiser address to the specified public/static address for the IUT.
2. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT.

Figure 4.121: GAP/CONN/UCON/BV-02-C [Undirected Connectable mode, General Discoverable mode] MSC

- Expected Outcome

## Pass verdict

The IUT sends either connectable and scannable undirected advertising events or connectable undirected advertising events.

In each advertising event received the advertiser address is set to the specified public/static address for the IUT.

The Lower Tester establishes a connection with IUT.

## GAP/CONN/UCON/BV-03-C [Undirected Connectable mode, Limited Discoverable mode]

- Test Purpose

Verify that the IUT in Undirected Connectable mode and Limited Discoverable mode can connect with another device performing the General Connection Establishment procedure.

The IUT is operating in the Peripheral role.

- Reference

[4] 9.3.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The public/static address for the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders the IUT to enter Limited Discoverable mode and Undirected Connectable mode; the IUT sets the advertiser address to the public/static address for the IUT.
2. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT.

Figure 4.122: GAP/CONN/UCON/BV-03-C [Undirected Connectable mode, Limited Discoverable mode] MSC

- Expected Outcome

## Pass verdict

The IUT sends either connectable and scannable undirected advertising events or connectable undirected advertising events.

In each advertising event received the advertiser address is set to the specified public/static address for the IUT.

The Lower Tester establishes a connection with IUT.

## 4.7.3.4 Auto Connection Establishment procedure

## GAP/CONN/ACEP/BV-01-C [Auto Connection Establishment procedure, Directed Connectable mode]

- Test Purpose

Verify that the IUT can perform the Auto Connection Establishment procedure to connect to another device in the Directed Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.3.5

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders IUT to perform the Auto Connection Establishment procedure using the specified public/static address of the Lower Tester.
2. The Lower Tester sets the advertiser address to the specified public/static address of the Lower Tester.
3. The Lower Tester sets the initiator address to the specified public/static address of the IUT.
4. The Lower Tester enters the Directed Connectable mode.

Figure 4.123: GAP/CONN/ACEP/BV-01-C [Auto Connection Establishment procedure, Directed Connectable mode] MSC

- Expected Outcome

## Pass verdict

The IUT autonomously establishes a connection with the Lower Tester.

## GAP/CONN/ACEP/BV-03-C [Auto Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]

- Test Purpose

Verify that the IUT using Resolvable Private Address can perform the Auto Connection Establishment procedure to connect to another device in the Directed Connectable mode that is using Resolvable Private Addresses.

The IUT is operating in the Central role.

- Reference

[9] 9.3.5, 10.7.2.1, 10.7.2.2, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT exposes the Central Address Resolution Characteristic set to 1.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.
- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Tester's Device Identity to the resolving list and Filter Accept List.
2. The Upper Tester orders the IUT to perform the Auto Connection Establishment procedure using resolvable private address.
3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester.
4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester.
5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.

Figure 4.124: GAP/CONN/ACEP/BV-03-C [Auto Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC

- Expected Outcome

## Pass verdict

The IUT uses a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request.

The IUT autonomously establishes a connection with the Lower Tester.

## GAP/CONN/ACEP/BV-04-C [Auto Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address]

- Test Purpose

Verify that the IUT using Resolvable Private Address can perform the Auto Connection Establishment procedure to connect to another device in the Undirected Connectable mode using Resolvable Private Address.

The IUT is operating in the Central role.

- Reference

[9] 9.3.5, 10.7.2.1, 10.7.2.2, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.
- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list and Filter Accept List.
2. The Upper Tester orders the IUT to perform the Auto Connection Establishment procedure using resolvable private address.
3. The Lower Tester enters the Undirected Connectable mode using the device identity for the Lower Tester.
4. Upon receiving the undirected advertisement, the IUT resolves the address and sends a connect request to the Lower Tester.

5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.
- Expected Outcome

Figure 4.125: GAP/CONN/ACEP/BV-04-C [Auto Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address] MSC

## Pass verdict

The IUT uses a resolvable private address as the initiator address and advertiser address present in the undirected advertisement in the connection request.

The IUT autonomously establishes a connection with the Lower Tester.

## 4.7.3.5 General Connection Establishment procedure

## GAP/CONN/GCEP/BV-01-C [General Connection Establishment procedure, Directed Connectable mode]

- Test Purpose

Verify that the IUT can perform the General Connection Establishment procedure to connect to another device in the Directed Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.3.6

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders the IUT to perform the General Connection Establishment procedure; the IUT uses the specified public/static address of the Lower Tester.
2. The Lower Tester sets the advertiser address to the public/static address of the Lower Tester.
3. The Lower Tester sets the initiator address to the public/static address of the IUT.
4. The Lower Tester enters the Directed Connectable mode.

Figure 4.126: GAP/CONN/GCEP/BV-01-C [General Connection Establishment procedure Directed Connectable mode] MSC

- Expected Outcome

## Pass verdict

The IUT receives the connectable directed advertising events from the Lower Tester.

If the IUT is Active Scanning with privacy enabled then the address used in the SCAN\_REQ is a nonresolvable private address.

If the IUT has privacy enabled then the address used in the connection request is a non-resolvable private address.

The IUT establishes a connection with the Lower Tester.

## GAP/CONN/GCEP/BV-02-C [General Connection Establishment procedure, Undirected Connectable mode]

- Test Purpose

Verify that the IUT can perform the General Connection Establishment procedure to connect to another device in the Undirected Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.3.6

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders the IUT to perform the General Connection Establishment procedure; the IUT uses the specified public/static address of the Lower Tester.
2. The Lower Tester sets the advertiser address to the public/static address of the Lower Tester.
3. The Lower Tester enters the Undirected Connectable mode.

Figure 4.127: GAP/CONN/GCEP/BV-02-C [General Connection Establishment procedure Undirected Connectable mode] MSC

- Expected Outcome

## Pass verdict

The IUT receives the connectable and scannable undirected advertising events or connectable undirected advertising events from the Lower Tester.

The IUT establishes a connection with the Lower Tester.

## GAP/CONN/GCEP/BV-05-C [General Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]

- Test Purpose

Verify that the IUT using a Resolvable Private Address can perform the General Connection Establishment procedure to connect to another device in the Directed Connectable mode using Resolvable Private Address.

The IUT is operating in the Central role.

- Reference

[9] 9.3.6. 10.7.2.1, 10.7.2.2, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT exposes the Central Address Resolution Characteristic set to 1.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.
- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list.
2. The Upper Tester orders the IUT to perform the General Connection Establishment procedure using resolvable private address.
3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester.

4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester.
5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.
- Expected Outcome

Figure 4.128: GAP/CONN/GCEP/BV-05-C [General Connection Establishment procedure Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC

## Pass verdict

The IUT receives the connectable directed advertising events from the Lower Tester.

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address.

The IUT uses a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request.

The IUT establishes a connection with the Lower Tester.

## GAP/CONN/GCEP/BV-06-C [General Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address]

- Test Purpose

Verify that the IUT using Resolvable Private Address can perform the General Connection Establishment procedure to connect to another device in the Undirected Connectable mode using Resolvable Private Address.

The IUT is operating in the Central role.

- Reference

[9] 9.3.6, 10.7.2.1, 10.7.2.2, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.

- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Tester's Identity to the resolving list.
2. The Upper Tester orders the IUT to perform the General Connection Establishment procedure using resolvable private address.
3. The Lower Tester enters the Undirected Connectable mode using the device identity for the Lower Tester.
4. Upon receiving the undirected advertisement, the IUT resolves the address and sends a connect request to the Lower Tester.
5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.
- Expected Outcome

Figure 4.129: GAP/CONN/GCEP/BV-06-C [General Connection Establishment procedure Undirected Connectable mode, Resolvable Private Address] MSC

## Pass verdict

The IUT receives the connectable and scannable undirected advertising events or connectable undirected advertising events from the Lower Tester.

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address.

The IUT uses a resolvable private address as the initiator address and advertiser address present in the undirected advertisement in the connection request.

The IUT establishes a connection with the Lower Tester.

## 4.7.3.6 Selective Connection Establishment procedure

## GAP/CONN/SCEP/BV-01-C [Selective Connection Establishment procedure, Directed Connectable mode]

- Test Purpose

Verify that the IUT can perform the Selective Connection Establishment procedure to connect to another device in the Directed Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.3.7

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The public/static address of the IUT is specified in the TSPX\_bd\_addr\_iut IXIT value.
- Test Procedure
1. The Upper Tester orders the IUT to perform the Selective Connection Establishment procedure using the specified public/static address of the Lower Tester.
2. The Lower Tester sets the advertiser address to the specified public/static address of the Lower Tester.
3. The Lower Tester sets the initiator address to the specified public/static address of the IUT.
4. The Lower Tester enters the Directed Connectable mode.
- Expected Outcome

Figure 4.130: GAP/CONN/SCEP/BV-01-C [Selective Connection Establishment procedure, Directed Connectable mode] MSC

## Pass verdict

The IUT Host receives advertising event reports sent from the Lower Tester and any other devices in the Filter Accept List; the IUT does not receive advertising event reports from any other devices.

The IUT establishes a connection with the Lower Tester.

## GAP/CONN/SCEP/BV-03-C [Selective Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]

- Test Purpose

Verify that the IUT using a Resolvable Private Address can perform the Selective Connection Establishment procedure to connect to another device in the Directed Connectable mode using Resolvable Private Address.

The IUT is operating in the Central role.

- Reference

[9] 9.3.7, 10.7.2.1, 10.7.2.2, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT exposes the Central Address Resolution Characteristic set to 1.

- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.
- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Tester ' s Device Identity to the resolving list and Filter Accept List.
2. The Upper Tester orders the IUT to perform the Selective Connection Establishment procedure using the device identity of the Lower Tester.
3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester.
4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester.
5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.
- Expected Outcome

Figure 4.131: GAP/CONN/SCEP/BV-03-C [Selective Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC

## Pass verdict

The IUT ' s advertising reports includes the Lower Tester.

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address.

The IUT uses a resolvable private address as the initiator address and the advertiser address present in the directed advertisement as the advertiser address in the connection request.

The IUT establishes a connection with the Lower Tester.

## 4.7.3.7 Direct Connection Establishment procedure

## GAP/CONN/DCEP/BV-01-C [Direct Connection Establishment procedure, Directed Connectable mode]

- Test Purpose

Verify that the IUT can perform the Direct Connection Establishment procedure to connect to another device in the Directed Connectable mode.

The IUT is operating in the Central role.

- Reference

## 4 9.3.8

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT has the address of the peer device.
- Test Procedure
1. The Upper Tester orders the IUT to perform the Direct Connection Establishment procedure using the static address, public address or non-resolvable private address of the Lower Tester.
2. The Lower Tester sets the advertiser address to the static address, public address or nonresolvable private address of the Lower Tester.
3. The Lower Tester sets the initiator address to the static address, public address or non-resolvable private address of the IUT.
4. The Lower Tester enters the Directed Connectable mode.
- Expected Outcome

Figure 4.132: GAP/CONN/DCEP/BV-01-C [Direct Connection Establishment procedure, Directed Connectable mode] MSC

## Pass verdict

If the IUT has privacy enabled then the address used in the connection request is a static address, public address, non-resolvable private address, or resolvable private address.

The IUT establishes a connection with the Lower Tester.

## GAP/CONN/DCEP/BV-03-C [Direct Connection Establishment procedure, Undirected Connectable mode]

- Test Purpose

Verify that the IUT can perform the Direct Connection Establishment procedure to connect to another device in the Undirected Connectable mode.

The IUT is operating in the Central role.

- Reference

[4] 9.3.8

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.

- Test Procedure
1. The Upper Tester orders IUT to perform the Direct Connection Establishment procedure using the static address, public address, non-resolvable private address, or resolvable private address of the Lower Tester.
2. The Lower Tester sets the advertiser address to the static address, public address, nonresolvable private address, resolvable private address of the Lower Tester.
3. The Lower Tester sets the initiator address to the static address, public address or non-resolvable private address of the IUT.
4. The Lower Tester enters the Undirected Connectable mode.
- Expected Outcome

Figure 4.133: GAP/CONN/DCEP/BV-03-C [Direct Connection Establishment procedure, Undirected Connectable mode] MSC

## Pass verdict

If the IUT has privacy enabled then the address used in the connection request is a static address, public address, non-resolvable private address, or resolvable private address.

The IUT establishes a connection with the Lower Tester.

## GAP/CONN/DCEP/BV-05-C [Direct Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution]

- Test Purpose

Verify that the IUT using Resolvable Private Address can perform the Direct Connection Establishment procedure to connect to another device in the Directed Connectable mode that is using a Resolvable Private Address.

The IUT is operating in the Central role.

- Reference

[9] 9.3.8, 10.7.2.1, 10.7.2.2, 12.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT exposes the Central Address Resolution Characteristic set to 1.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.

- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list.
2. The Upper Tester orders the IUT to perform the Direct Connection Establishment procedure using resolvable private address.
3. The Lower Tester enters the Directed Connectable mode using the device identities for the IUT and Lower Tester.
4. Upon receiving the directed advertisement, the IUT resolves the addresses and sends a connect request to the Lower Tester.
5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.
- Expected Outcome

Figure 4.134: GAP/CONN/DCEP/BV-05-C [Direct Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution] MSC

## Pass verdict

The IUT receives the connectable directed advertising events from the Lower Tester.

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address.

The IUT uses the advertiser address present in the directed advertisement as the advertiser address and a resolvable private address as the initiator address in the connection request.

The IUT establishes a connection with the Lower Tester.

## GAP/CONN/DCEP/BV-06-C [Direct Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address]

- Test Purpose

Verify that the IUT using Resolvable Private Address can perform the Direct Connection Establishment procedure to connect to another device in the Undirected Connectable mode that is using Resolvable Private Address.

The IUT is operating in the Central role.

- Reference

[9] 9.3.8, 10.7.2.1, 10.7.2.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The Lower Tester is using a resolvable private address and has distributed its IRK.
- -The IUT is using a resolvable private address and has distributed its IRK.
- Test Procedure
1. The Upper Tester orders the IUT to add the Lower Testers Identity to the resolving list.
2. The Upper Tester orders the IUT to perform the Direct Connection Establishment procedure using resolvable private address.
3. The Lower Tester enters the Undirected Connectable mode using the device identities for the Lower Tester.
4. Upon receiving the undirected advertisement, the IUT resolves the address and sends a connect request to the Lower Tester.
5. After the connection establishment, either the Lower Tester or the IUT should terminate the connection.
- Expected Outcome

Figure 4.135: GAP/CONN/DCEP/BV-06-C [Direct Connection Establishment procedure, Undirected Connectable mode, Resolvable Private Address] MSC

## Pass verdict

The IUT receives the connectable and scannable undirected advertising events or connectable undirected advertising events from the Lower Tester.

The IUT is able to resolve and confirm the identity of the Lower Tester from the received resolvable private address.

The IUT use a resolvable private address as the initiator address and advertiser address present in the undirected advertisement in the connection request.

The IUT establishes a connection with the Lower Tester.

## 4.7.3.8 Connection Parameter Update procedure

## GAP/CONN/CPUP/BV-01-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over L2CAP]

- Test Purpose

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device, using the L2CAP Connection Parameter Update Request procedure; the peer device accepts the updated connection parameters.

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder.

- Reference

[4] 9.3.9

- Initial Condition
- -On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0.
- -The IUT and the Lower Tester are connected.
- -The valid connection update parameters for the IUT are specified in the following IXIT [3]:
- TSPX\_conn\_update\_int\_min
- TSPX\_conn\_update\_int\_max
- TSPX\_conn\_update\_peripheral\_latency
- TSPX\_conn\_update\_supervision\_timeout
- -TGAP(conn\_param\_timeout) for the IUT is specified in the TSPX\_Tgap\_conn\_param\_timeout IXIT value.
- -The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure.
- Test Procedure
1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters.
2. The IUT executes the L2CAP Connection Parameter Update Request procedure.
3. The Lower Tester accepts the updated connection parameters and sends the appropriate L2CAP connection parameter update response within the specified TGAP(conn\_param\_timeout).

Figure 4.136: GAP/CONN/CPUP/BV-01-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over L2CAP] MSC

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP connection parameter update request command with the specified update connection parameters.

The IUT Host receives an indication from the IUT controller that the connection parameters have been updated.

- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges.

## GAP/CONN/CPUP/BV-02-C [Connection Parameter Update procedure, valid parameters, Timeout Peripheral Initiator]

- Test Purpose

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device; the peer device fails to respond in a timely manner.

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder.

- Reference

## 4 9.3.9

- Initial Condition
- -On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0.
- -The IUT and the Lower Tester are connected.
- -The valid connection update parameters for the Lower Tester are specified in the following IXIT [3]:
- TSPX\_conn\_update\_int\_min
- TSPX\_conn\_update\_int\_max
- TSPX\_conn\_update\_peripheral\_latency

- -RTX timer is set to maximum allowed initial value.
- -The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure.
- Test Procedure
1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters.
2. The Lower Tester does not send the appropriate L2CAP connection parameter update response within the specified RTX timeout.
- Expected Outcome

Figure 4.137: GAP/CONN/CPUP/BV-02-C [Connection Parameter Update procedure, valid parameters, Timeout Peripheral Initiator] MSC

## Pass verdict

The IUT transmits a correctly formatted L2CAP Connection Parameter Update Request to the Lower Tester, containing valid connection update parameters matching those received from the Upper Tester.

After RTX timer expires, the IUT either:

1. IUT resends the L2CAP Connection Parameter Update Request command.
2. IUT disconnects the connection at the Link Layer.
3. IUT ignores the error case and continues without disconnecting or resending.
- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges but in this test case does not respond to the connection parameter update request sent by the IUT.

## GAP/CONN/CPUP/BV-03-C [Connection Parameter Update procedure, invalid parameters, Peripheral Initiator]

- Test Purpose

Verify that the IUT can perform the Connection Parameter Update procedure using invalid parameters for the peer device; the peer device rejects the updated connection parameters.

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder.

- Reference

## 4 9.3.9

- Initial Condition
- -On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0.
- -The IUT and the Lower Tester are connected.
- -The invalid connection update parameters for the Lower Tester are specified in the following IXIT [3]:
- TSPX\_iut\_invalid\_connection\_interval\_min
- TSPX\_iut\_invalid\_connection\_interval\_max
- TSPX\_iut\_invalid\_connection\_latency
- TSPX\_iut\_invalid\_conn\_update\_supervision\_timeout
- -TGAP(conn\_param\_timeout) for the IUT is specified in the TSPX\_Tgap\_conn\_param\_timeout IXIT value.
- -The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure.
- Test Procedure
1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified invalid connection update parameters.
2. The Lower Tester rejects the updated connection parameters and sends the appropriate L2CAP connection parameter update response within the specified TGAP(conn\_param\_timeout).
- Expected Outcome

Figure 4.138: GAP/CONN/CPUP/BV-03-C [Connection Parameter Update procedure, invalid parameters, Peripheral Initiator] MSC

## Pass verdict

The Lower Tester receives an L2CAP connection parameter update request command with the specified update connection parameters sent by the IUT.

The IUT Host does not receive an indication from the IUT controller that the connection parameters have been updated.

- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges but in this test case rejects the update connection parameters request sent by the IUT.

## GAP/CONN/CPUP/BV-04-C [Connection Parameter Update procedure, valid parameters, Central Responder]

- Test Purpose

Verify that the IUT accepts the connection parameter update request from a peer device performing the Connection Parameter Update procedure using valid parameters for the IUT.

The Lower Tester is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the IUT is operating in the Central role and is the responder.

- Reference

[4] 9.3.9

- Initial Condition
- -On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0.
- -The IUT and the Lower Tester are connected.
- -The valid connection update parameters for the IUT are specified in the following IXIT [3]:
- TSPX\_conn\_update\_int\_min
- TSPX\_conn\_update\_int\_max

▪

TSPX\_conn\_update\_peripheral\_latency

- TSPX\_conn\_update\_supervision\_timeout
- -The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure.
- Test Procedure

The Lower Tester performs the Connection Parameter Update procedure using the specified valid connection update parameters.

Figure 4.139: GAP/CONN/CPUP/BV-04-C [Connection Parameter Update procedure, valid parameters, Central Responder] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives an L2CAP connection parameter update response within TGAP(conn\_param\_timeout) after sending the L2CAP connection parameter update request.

The L2CAP connection parameter update response result code is set to 'parameters accepted'.

The IUT uses the new connection parameters after the Lower Tester receives the L2CAP connection parameter update response.

- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges.

## GAP/CONN/CPUP/BV-05-C [Connection Parameter Update procedure, invalid parameters, Central Responder]

- Test Purpose

Verify that the IUT rejects the connection parameter update request from a peer device performing the Connection Parameter Update procedure using invalid connection parameters for the IUT.

The Lower Tester is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure and the IUT is operating in the Central role and is the responder.

- Reference

[4] 9.3.9

- Initial Condition
- -On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0.
- -The IUT and the Lower Tester are connected.
- -The invalid connection update parameters for the IUT are specified in the following IXIT [3]:
- TSPX\_iut\_invalid\_connection\_interval\_min
- TSPX\_iut\_invalid\_connection\_interval\_max
- TSPX\_iut\_invalid\_connection\_latency
- TSPX\_iut\_invalid\_conn\_update\_supervision\_timeout
- -The Lower Tester has indicated that it does not support the LL Connection Parameters Request procedure.

- Test Procedure

The Lower Tester performs the Connection Parameter Update procedure using the specified invalid connection update parameters.

Figure 4.140: GAP/CONN/CPUP/BV-05-C [Connection Parameter Update procedure, invalid parameters, Central Responder] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives an L2CAP connection parameter update response within TGAP(conn\_param\_timeout) after sending the L2CAP connection parameter update request.

The L2CAP connection parameter update response result code is set to 'request rejected'.

The IUT continues to use the default connection parameters after the Lower Tester receives the L2CAP connection parameter update response.

- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges.

## GAP/CONN/CPUP/BV-06-C [Connection Parameter Update procedure, valid parameters, Central Initiator]

- Test Purpose

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device; the peer device accepts the updated connection parameters.

The IUT is operating in the Central role and is the initiator performing the Connection Parameter Update procedure and the Lower Tester is operating in the Peripheral role and is the responder.

- Reference

[4] 9.3.9

- Initial Condition
- -On the Lower Tester, set the Connection Parameters Request procedure LL feature bit to 0.
- -The IUT and the Lower Tester are connected.
- -The valid connection update parameters for the Lower Tester are specified in the following IXIT [3]:
- TSPX\_conn\_update\_int\_min
- TSPX\_conn\_update\_int\_max
- TSPX\_conn\_update\_peripheral\_latency
- TSPX\_conn\_update\_supervision\_timeout
- Test Procedure
1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters.
2. The Lower Tester expects the IUT to initiate either the Link Layer Connection Update procedure or the Connection Parameters Request Link Layer control procedure.
3. The Lower Tester accepts the updated connection parameters and completes the Link Layer procedure initiated by the IUT.
- Expected Outcome

Figure 4.141: GAP/CONN/CPUP/BV-06-C [Connection Parameter Update procedure, valid parameters, Central Initiator] MSC

## Pass verdict

The Lower Tester receives the L2CAP connection parameter update response sent by the IUT in either the Link Layer Connection Update procedure or the Connection Parameters Request Link Layer control procedure.

The IUT and the Lower Tester use the new parameters and the link is not dropped due to Link Supervision Timeout.

- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges.

## GAP/CONN/CPUP/BV-08-C [Connection Parameter Update procedure, valid parameters, Peripheral Responder -LL Connection Parameters Request]

- Test Purpose

Verify that the IUT accepts the connection parameter update request from a peer device performing the Connection Parameter Update procedure using valid parameters for the IUT when both the IUT and the peer device support the Link Layer Connection Parameters Request control procedure.

The Lower Tester is operating in the Central role and is the initiator performing the Connection Parameter Update procedure; the IUT is operating in the Peripheral role and is the responder.

- Reference

[4] 9.3.9

- Initial Condition
- -The IUT and the Lower Tester are connected.
- -The valid connection update parameters for the IUT are specified in the following IXIT [3]:
- TSPX\_conn\_update\_int\_min
- TSPX\_conn\_update\_int\_max
- TSPX\_conn\_update\_peripheral\_latency
- TSPX\_conn\_update\_supervision\_timeout
- Test Procedure
1. The Lower Tester initiates the Connection Parameters Request Link Layer Control procedure, sending the specified valid connection update parameters to the IUT.
2. The Lower Tester expects the IUT to accept the connection update parameters.
3. The Lower Tester completes the Connection Parameters Request Link Layer Control procedure.
4. The Lower Tester expects the IUT to maintain the connection with the new parameters.

Figure 4.142: GAP/CONN/CPUP/BV-08-C [Connection Parameter Update procedure, valid parameters, Peripheral Responder -LL Connection Parameters Request] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives a response from the IUT accepting the connection update parameters within procedure response timeout after initiating the Connection Parameters Request Link Layer Control procedure.

The IUT uses the new connection parameters after the Link Layer Connection Parameters Request control procedure completes.

- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges.

## GAP/CONN/CPUP/BV-10-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over LL]

- Test Purpose

Verify that the IUT can perform the Connection Parameter Update procedure using valid parameters for the peer device, using the LL Connection Parameters Request procedure; the peer device accepts the updated connection parameters.

The IUT is operating in the Peripheral role and is the initiator performing the Connection Parameter Update procedure; the Lower Tester is operating in the Central role and is the responder.

- Reference

## 4 9.3.9

- Initial Condition
- -The IUT and the Lower Tester are connected.
- -The valid connection update parameters for the IUT are specified in the following IXIT [3]:
- TSPX\_conn\_update\_int\_min
- TSPX\_conn\_update\_int\_max
- TSPX\_conn\_update\_peripheral\_latency
- TSPX\_conn\_update\_supervision\_timeout
- -TGAP(conn\_param\_timeout) for the IUT is specified in the TSPX\_Tgap\_conn\_param\_timeout IXIT value.
- -The Lower Tester has indicated that it supports the LL Connection Parameter Request procedure.
- Test Procedure
1. The Upper Tester orders the IUT to perform the Connection Parameter Update procedure using the specified valid connection update parameters.
2. The IUT executes the LL Connection Parameters Request procedure.
3. The Lower Tester accepts the updated connection parameters and executes the LL Connection Parameter Update procedure within the specified TGAP(conn\_param\_timeout).

Figure 4.143: GAP/CONN/CPUP/BV-10-C [Connection Parameter Update procedure, valid parameters, Peripheral Initiator over LL] MSC

- Expected Outcome

## Pass verdict

The IUT executes the LL Connection Parameters Request procedure and accepts the parameter update.

The IUT Host receives an indication from the IUT controller that the connection parameters have been updated.

- Notes

The Lower Tester should be capable of using any connection parameters within the valid ranges.

## 4.7.3.9 Terminate Connection procedure

## GAP/CONN/TERM/BV-01-C [Terminate Connection procedure]

- Test Purpose

Verify that the IUT can perform the Terminate Connection procedure.

The IUT is Central or Peripheral and the Lower Tester is Peripheral or Central, respectively.

- Reference

## 4 9.3.8

- Initial Condition
- -The IUT and the Lower Tester are connected.
- -The IUT is the role as specified in the TSPX\_gap\_iut\_role IXIT entry.

- Test Procedure

The Upper Tester orders the IUT to perform the Terminate Connection procedure.

Figure 4.144: GAP/CONN/TERM/BV-01-C [Terminate Connection procedure] MSC

- Expected Outcome

## Pass verdict

The IUT performs the Link Layer Termination procedure and disconnects from the Lower Tester.

## 4.7.3.10 Random Device Address

## GAP/CONN/PRDA/BV-01-C [Respond to Private Random Device Address after Bonding -Peripheral role]

- Test Purpose

Verify that the IUT can properly respond to connections after bonding when Private Random Addresses are used by the Lower Tester.

The IUT is the responder and is in the Peripheral role.

The IUT supports security manager pairing and is in bondable mode.

After the bonding has completed, authentication procedure is performed to assure that bonding information is stored properly and that Private Resolvable Addresses are accepted across connections.

- Reference

[4] 10.8

- Initial Condition
- -Physical link is established between the IUT and Lower Tester. Lower Tester uses a Resolvable Private Address as its Device Address.
- -After the connection is established, Lower Tester initiates pairing using either LE Legacy or LE Secure Connections with Bonding Flags set to 'Bonding'.
- -The pairing procedure is completed successfully between Lower Tester and IUT.
- -The Lower Tester distributes its own IRK to the IUT.

- Test Procedure
1. The Lower Tester disconnects the physical link with IUT.
2. The Lower Tester establishes connection with the IUT. The Lower Tester uses a new Resolvable Private Address as its own Device Address for the connection establishment procedure. The Lower Tester may continue to try to establish connection for 30 seconds.
3. The Lower Tester performs authentication procedure.
4. Repeat the test procedure twice with the Lower Tester generating new RPAs between each new connection.
- Expected Outcome

Figure 4.145: GAP/CONN/PRDA/BV-01-C [Respond to Private Random Device Address after Bonding -Peripheral role] MSC

## Pass verdict

The IUT reconnects with the Lower Tester and authentication is successful.

## GAP/CONN/PRDA/BV-02-C [Respond to Private Random Device Address after Bonding -Central role]

- Test Purpose

Verify that the IUT can properly respond to connections after bonding when Private Random Addresses are used by the Lower Tester.

The IUT is the initiator and is in Central role.

The IUT supports security manager pairing and is in bondable mode.

After the bonding has completed, authentication procedure is performed to assure that bonding information is stored properly and that Private Resolvable Addresses are accepted across connections.

- Reference

[4] 10.8

- Initial Condition
- -Physical link is established between IUT and Lower Tester. The Lower Tester uses a Resolvable Private Address as its Device Address.
- -After the connection is established, the Lower Tester initiates security request with Bonding Flags set to 'Bonding'.
- -The IUT initiates pairing procedure using either LE Legacy or LE Secure Connections.
- -The pairing procedure is completed successfully between the Lower Tester and IUT.
- -The Lower Tester distributes its own IRK to the IUT.
- Test Procedure
1. The Lower Tester disconnects the physical link with the IUT.
2. The IUT establishes connection with the Lower Tester; the Lower Tester uses a new Resolvable Private Address as part of the connection establishment procedure.
3. The Lower Tester performs the authentication procedure.
4. Repeat the test procedure twice with the Lower Tester generating new RPAs between each new connection.

Figure 4.146: GAP/CONN/PRDA/BV-02-C [Respond to Private Random Device Address after Bonding -Central role] MSC

## · Expected Outcome

## Pass verdict

The IUT reconnects to a Lower Tester and authentication is successful.

## 4.7.4 Bonding modes and procedures

## 4.7.4.1 Non-bondable mode

## GAP/BOND/NBON/BV-01-C [Non-bondable mode -Central as Responder]

- Test Purpose

Verify that the IUT does not store bonding information after pairing while in non-bondable mode.

The Lower Tester is the initiator. The Lower Tester sends security request to invoke the pairing procedure.

The IUT supports security manager pairing but is in non-bondable mode.

The pairing is performed as unauthenticated pairing (Just Works).

The bonding is performed twice to make sure pairing is invoked both times.

The IUT is the Central and the Lower Tester is the Peripheral.

- Reference

## 4 9.4.2

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -The IUT and the Lower Tester are not bonded before.
- Test Procedure
1. After the connection is established, the Lower Tester initiates security request with Bonding\_Flags set to 'No Bonding'.
2. The IUT responses to security request with pairing procedure.
3. The pairing procedure is completed successfully between the Lower Tester and the IUT.
4. The Lower Tester disconnects the physical link with the IUT.
5. The IUT establishes connection with the Lower Tester again.
6. The Lower Tester re-initiates security request and verifies that the pairing procedure is invoked and completed successfully.
- Expected Outcome

## Pass verdict

Pairing is successful each time.

Authentication is invoked each time.

## GAP/BOND/NBON/BV-02-C [Non-bondable mode -Central as Initiator]

## · Test Purpose

Verify that the IUT does not store bonding information after pairing while in non-bondable mode.

The IUT is the initiator. The Upper Tester requests the authentication.

The IUT initiates the pairing procedure with bonding flag = 'no bonding'.

The pairing is performed as unauthenticated pairing (Just Works).

The bonding is performed twice to make sure pairing is invoked both times.

The IUT is the Central and the Lower Tester is the Peripheral.

## · Reference

## 4 9.4.2

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -The IUT and the Lower Tester are not bonded before.

## · Test Procedure

1. After the connection is established, Upper Tester requests authentication with Bonding\_Flags set to 'No Bonding'.
2. The IUT initiates the pairing procedure.
3. The pairing procedure is completed successfully between the Lower Tester and the IUT.
4. The Lower Tester disconnects the physical link with the IUT.
5. The IUT establishes a connection with the Lower Tester again.
6. The Upper Tester re-initiates authentication and the pairing procedure is invoked and completed successfully.

Figure 4.147: GAP/BOND/NBON/BV-02-C [Non-bondable mode -Central as Initiator] MSC

## · Expected Outcome

## Pass verdict

Pairing is successful each time.

Authentication is invoked each time.

## GAP/BOND/NBON/BV-03-C [Non-bondable mode -Peripheral as Responder]

- Test Purpose

Verify that the IUT does not exchange bonding information after pairing while in non-bondable mode.

The Lower Tester is the initiator. The Lower Tester requires authentication to invoke the pairing procedure.

The IUT either does not support security manager pairing or supports security manager pairing, but is in non-bondable mode.

The pairing is performed as unauthenticated pairing (Just Works).

Both the initiator and the responder key distribution field are set to 0 and bonding flag is set to 'no bonding' .

The IUT is Peripheral.

- Reference

[4] 9.4.2

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -The IUT and the Lower Tester are not bonded before.
- Test Procedure
1. After the connection is established, the Lower Tester initiates pairing with Bonding\_Flags set to 'No Bonding' and both 'Initiator Key Distribution = 0' and 'Responder Key Distribution = 0'.
2. There are two alternatives, depending on if the IUT supports security manager pairing.
3. Alternative 1 (The IUT supports security manager pairing):
- The IUT sends a pairing response with Bonding\_Flags = 'No Bonding' and both 'Initiator Key Distribution = 0' and 'Responder Key Distribution = 0'.
- The pairing procedure is completed successfully between the Lower Tester and the IUT.
- The Lower Tester disconnects the physical link with the IUT.
4. Alternative 2 (The IUT does not support security manager pairing):
- The IUT sends a Pairing Failed message with the error code 'Pairing not supported'.

Figure 4.148: GAP/BOND/NBON/BV-03-C [Non-bondable mode -Peripheral as Responder] MSC

- Expected Outcome

## Pass verdict

## Alternative 1:

- -The p airing procedure is completed successfully with Bonding\_Flags = 'no bonding' and initiator/responder key distribution are set to 0.
- -The link is encrypted correctly with STK.

## Alternative 2:

- -The p airing procedure fails with 'Pairing not supported'.

## 4.7.4.2 Bondable mode

## GAP/BOND/BON/BV-01-C [Initiate bonding -Peripheral role]

- Test Purpose

Verify that the IUT can properly initiate the bonding procedure and store bonding information after pairing while in bondable mode in the Peripheral role.

The IUT is the initiator and is in the Peripheral role.

The IUT supports security manager pairing and is in bondable mode.

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing.

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing.

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly.

## · Reference

## 4 9.4.3, 9.4.4

## · Initial Condition

- -Physical link is established by either directed or undirected connectable mode.
- -The IUT and the Lower Tester are not bonded before.

## · Test Procedure

1. After the connection is established, the IUT initiates security request with Bonding\_Flags set to 'Bonding'.
2. The IUT initiates bonding by sending 'security request' to the Lower Tester.
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

Figure 4.149: GAP/BOND/BON/BV-01-C [Initiate bonding -Peripheral role] MSC

- Expected Outcome

## Pass verdict

If the IUT supports LE security mode 1, then encryption is done successfully.

If the IUT supports LE security mode 2, then data signing is done successfully.

## GAP/BOND/BON/BV-02-C [Initiate bonding -Central role]

- Test Purpose

Verify that the IUT can properly initiate bonding procedure and store bonding information after pairing while in bondable mode in the Central role.

The IUT is the initiator and is in the Central role.

The IUT supports security manager pairing and is in bondable mode.

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing.

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing.

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly.

- Reference

[4] 9.4.3, 9.4.4

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -The IUT and the Lower Tester are not bonded before.

## · Test Procedure

1. After the connection is established, the IUT initiates pairing with Bonding\_Flags set to 'Bonding'.
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

Figure 4.150: GAP/BOND/BON/BV-02-C [Initiate bonding -Central role] MSC

## · Expected Outcome

## Pass verdict

If the IUT supports LE security mode 1, then encryption is done successfully.

If the IUT supports LE security mode 2, then data signing is done successfully.

## GAP/BOND/BON/BV-03-C [Respond to bonding -Peripheral role]

## · Test Purpose

Verify that the IUT can properly respond to bonding and store bonding information after pairing while in bondable mode in the Peripheral role.

The IUT is the responder and is in the Peripheral role.

The IUT supports security manager pairing and is in bondable mode.

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing.

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing.

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly.

## · Reference

[4] 9.4.3, 9.4.4

## · Initial Condition

- -Physical link is established by either directed or undirected connectable mode.
- -The IUT and the Lower Tester are not bonded before.

## · Test Procedure

1. After the connection is established, the Lower Tester initiates pairing with Bonding\_Flags set to 'Bonding'.
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
- Expected Outcome

Figure 4.151: GAP/BOND/BON/BV-03-C [Respond to bonding -Peripheral role] MSC

## Pass verdict

If the IUT supports LE security mode 1, then encryption is done successfully.

If the IUT supports LE security mode 2, then data signing is done successfully.

## GAP/BOND/BON/BV-04-C [Respond to bonding -Central role]

- Test Purpose

Verify that the IUT can properly respond to bonding and store bonding information after pairing while in bondable mode as Central role.

The IUT is the responder and is in the Central role.

The IUT supports security manager pairing and is in bondable mode.

If the IUT supports LE security mode 1, then pairing may be performed as unauthenticated pairing.

If the IUT supports LE security mode 2, then pairing is performed as authenticated pairing.

After the bonding, either data signing or encryption is performed to assure that bonding information is stored properly.

- Reference

[4] 9.4.3, 9.4.4

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -The IUT and the Lower Tester are not bonded before.
- Test Procedure
1. After the connection is established, the Lower Tester initiates security request with Bonding\_Flags set to 'Bonding'.
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

Figure 4.152: GAP/BOND/BON/BV-04-C [Respond to bonding -Central role] MSC

- Expected Outcome

## Pass verdict

If the IUT supports LE security mode 1, then encryption is done successfully.

If the IUT supports LE security mode 2, then data signing is done successfully.

## 4.7.5 Security

Verify the correct implementation of the security procedure in various LE security modes, [4] Section 10.

## 4.7.5.1 Authentication procedure

## GAP/SEC/AUT/BV-11-C [Service Response -Insufficient Authentication, Peripheral]

- Test Purpose

Verify that the IUT properly rejects the service request when there is no sufficient bonding and then completes service correctly with the Lower Tester in the Central role.

The IUT is operating in the Peripheral role.

The Lower Tester is operating in the Central role.

- Reference

[4] 10.3

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -No previous bond or insufficient bond exists between the IUT and the Lower Tester.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.

- Test Procedure
1. The Lower Tester initiates a service request to IUT.
2. The Upper Tester of the IUT detects either there was no bonding or bonding with insufficient security level.
3. The Upper Tester of the IUT rejects the service request with error code 'Insufficient Authentication'.
4. The Lower Tester initiates authenticated pairing using either LE Legacy or LE Secure Connections.
5. Authentication is completed successfully and key information is exchanged properly.
6. If the IUT supports LE security mode 1, then the Lower Tester initiates encryption and send service request again.
7. If the IUT supports LE security mode 2, then the Lower Tester sends signed service request with previously distributed CSRK.
8. The IUT replies with correct service response.
- Expected Outcome

Figure 4.153: GAP/SEC/AUT/BV-11-C [Service Response -Insufficient Authentication, Peripheral] MSC

## Pass verdict

Authentication completes successfully.

Service response is properly sent by the IUT.

## GAP/SEC/AUT/BV-12-C [Service Response -Insufficient Authentication, Central]

- Test Purpose

Verify that the IUT properly rejects the service request when there is no sufficient bonding and then completes service correctly with the Lower Tester in the Peripheral role.

The IUT is operating in the Central role.

The Lower Tester is operating in the Peripheral role.

- Reference

[4] 10.3

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -No previous bond or insufficient bond exists between the IUT and the Lower Tester.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.
- Test Procedure
1. The Lower Tester initiates a service request to the IUT.
2. The Upper Tester of the IUT detects either there was no bonding or bonding with insufficient security level.
3. The Upper Tester of the IUT rejects the service request with error code 'Insufficient Authentication'.
4. The Lower Tester initiates pairing using either LE Legacy or LE Secure Connections.
5. Pairing is completed successfully and key information is exchanged properly.
6. If the IUT supports LE security mode 1, then the Lower Tester initiates encryption and send service request again.
7. If the IUT supports LE security mode 2, then the Lower Tester sends signed service request with previously distributed CSRK.
8. The IUT replies with correct service response.

Figure 4.154: GAP/SEC/AUT/BV-12-C [Service Response -Insufficient Authentication, Central] MSC

## · Expected Outcome

## Pass verdict

Authentication completes successfully.

Service response is properly sent by the IUT.

## GAP/SEC/AUT/BV-13-C [Service Response -Insufficient Authentication, Central]

## · Test Purpose

Verify that the IUT properly rejects the service request when there is insufficient authentication and then completes service correctly with the Lower Tester in the Peripheral role.

The IUT is operating in the Central role.

The Lower Tester is operating in the Peripheral role.

The IUT is capable of supporting LE security mode 1 level 3 (authenticated paring).

Either test procedure A or B may be used.

## · Reference

[4] 10.3, 10.6

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -Previous bond exists between the IUT and Lower Tester with unauthenticated pairing.
- -Upper Tester of the IUT is either a GATT profile or a higher layer protocol.
- Test Procedure A
1. The Lower Tester initiates encryption by sending 'security request' on the link with MITM = 0.
2. The IUT initiates and completes the encryption of the link.
3. The Lower Tester initiates a service request to the IUT.
4. The Upper Tester of the IUT detects the bonding has insufficient security level.
5. The Upper Tester of the IUT rejects the service request with error code 'Insufficient Authentication' .
6. The Lower Tester initiates higher level bonding by sending 'security request' on the link with MITM = 1.
7. The IUT initiates pairing with MITM = 1 and then encrypts the link.
8. The Lower Tester sends service request again.
9. The IUT replies with correct service response.

Figure 4.155: GAP/SEC/AUT/BV-13-C [Service Response -Insufficient Authentication, Central] -Test Procedure A MSC

## · Test Procedure B

1. The IUT initiates encryption with previously unauthenticated bonding info.
2. The IUT initiates and completes the encryption of the link.
3. The IUT initiates a service request to the Lower Tester.
4. The Lower Tester detects the bonding has insufficient security level.
5. The Lower Tester rejects the service request with error code 'Insufficient Authentication' .
6. The IUT initiates pairing with MITM = 1 and then encrypts the link.
7. The IUT sends service request again.
8. The Lower Tester replies with correct service response.

Figure 4.156: GAP/SEC/AUT/BV-13-C [Service Response -Insufficient Authentication, Central] -Test Procedure B MSC

- Expected Outcome

## Pass verdict

Authentication completes successfully.

Service response is properly sent by the IUT.

## GAP/SEC/AUT/BV-14-C [Service Response -Insufficient Authentication, Peripheral]

- Test Purpose

Verify that the IUT properly rejects the service request when there is insufficient authentication and then completes service correctly with the Lower Tester in the Central role.

The IUT is capable of supporting LE security mode 1 level 3 (authenticated paring).

The IUT is operating in the Peripheral role.

The Lower Tester is operating in the Central role.

- Reference

[4] 10.3, 10.6

- Initial Condition
- -Physical link is established by either directed or undirected connectable mode.
- -Previous bond exists between the IUT and the Lower Tester with unauthenticated pairing.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.

- Test Procedure
1. The Lower Tester initiates and completes the encryption on the link.
2. The Lower Tester initiates a service request to the IUT.
3. The Upper Tester of the IUT detects the bonding has insufficient security level.
4. The Upper Tester of the IUT rejects the service request with error code 'Insufficient Authentication'.
5. The Lower Tester initiates pairing MITM = 1 and then encrypts the link again.
6. The Lower Tester sends service request again.
7. The IUT replies with correct service response.
- Expected Outcome

Figure 4.157: GAP/SEC/AUT/BV-14-C [Service Response -Insufficient Authentication, Peripheral] MSC

## Pass verdict

Authentication completes successfully.

Service response is properly sent by the IUT.

## GAP/SEC/AUT/BV-17-C [Correct Pairing after Insufficient Authentication -Central role]

- Test Purpose

Verify that the IUT can pair with a device whose IO capabilities do not allow an authenticated pairing, after a service request has been denied with the error response 'Insufficient Authentication'.

The IUT is the SM initiator, GATT client and is in the Central role.

The IUT supports security manager pairing.

- Reference

[9] 10.3

- Initial Condition
- -Whether the IUT starts the pairing procedure before issuing any service request is specified in the TSPX\_pairing\_before\_service\_request IXIT value.
- -The IUT security policy of whether or not it mandates MITM is specified in the TSPX\_iut\_mandates\_mitm IXIT value.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT and the Lower Tester have not previously bonded.
- Test Procedure
1. If the IUT starts the pairing procedure before issuing any service request is recorded in the IXIT, proceed to Step 5.
2. The IUT performs a service request which will be denied by the Lower Tester with the error code 'Insufficient Authentication'.
3. The IUT initiates a pairing procedure. The authentication requirement field should only be set to MITM if the IUT mandates MITM or if it allows security level downgrade during pairing; i.e., proceeding with the pairing procedure even though the request for MITM protection could not be met.
4. The Lower Tester sets its IO capabilities to 'NoInputNoOutput' and the authentication requirements field to zero in pairing phase 1.
5. If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the pairing will succeed, and the link will now be encrypted with an unauthenticated STK. The IUT completes the previous ordered service request with a success.

Figure 4.158: GAP/SEC/AUT/BV-17-C [Correct Pairing after Insufficient Authentication -Central role] MSC

- Expected Outcome

## Pass verdict

If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the IUT will successfully complete an unauthenticated pairing with the Lower Tester and perform the service request.

## GAP/SEC/AUT/BV-18-C [Correct Pairing after Insufficient Authentication -Peripheral role]

- Test Purpose

Verify that the IUT can pair with a device whose IO capabilities do not allow an authenticated pairing, after a service request has been denied with the error response 'Insufficient Authentication'.

The IUT is the SM responder, GATT Client, and is in the Peripheral role.

The IUT supports security manager pairing.

- Reference

[9] 10.3

- Initial Condition
- -Whether the IUT starts the pairing procedure before issuing any service request is specified in the TSPX\_pairing\_before\_service\_request IXIT value.
- -The IUT's security policy of whether or not it mandates MITM is specified in the TSPX\_iut\_mandates\_mitm IXIT value.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT and the Lower Tester have not previously bonded.
- Test Procedure
1. If the IUT starts the pairing procedure before issuing any service request is recorded in the IXIT, proceed to Step 5.
2. The IUT performs a service request which will be denied by the Lower Tester with the error code 'Insufficient Authentication'.
3. The IUT sends a security request to initiate the pairing procedure. The authentication requirement field should only be set to MITM if the IUT mandates MITM or if it allows security level downgrade during pairing; i.e., proceeding with the pairing procedure even though the request for MITM protection could not be met.
4. The Lower Tester sets its IO capabilities to 'NoInputNoOutput' and mimics the authentication requirements field from the security request in pairing phase 1.
5. If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the pairing will succeed, and the link will now be encrypted with an unauthenticated STK. The IUT completes the previous ordered service request with a success.

Figure 4.159: GAP/SEC/AUT/BV-18-C [Correct Pairing after Insufficient Authentication -Peripheral role] MSC

- Expected Outcome

## Pass verdict

If the IUT has stated that it mandates MITM in the IXIT, the pairing procedure will fail; otherwise, the IUT will successfully complete an unauthenticated pairing with the Lower Tester and perform the service request.

## GAP/SEC/AUT/BV-19-C [Service Response Insufficient Authentication -Central role]

- Test Purpose

Verify that the IUT, when bonded with a peer device, tests the bond when receiving the error response 'Insufficient Authentication' if the link is unencrypted.

- Reference

[9] 10.3

- Initial Condition
- -The IUT is the SM initiator and GATT Client and is in the Central role.
- -The IUT supports security manager bonding.
- -Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value.
- -A physical link is established between the IUT and the Lower Tester.

- -The IUT and the Lower Tester are bonded before the connection, and service discovery has been performed. The Lower Tester's LTK has been distributed.
- -The Lower Tester has not stored the LTK from the IUT, which will result in the 'Insufficient Authentication' error in Step 2.

## · Test Procedure

1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value, go to Step 3.
2. The IUT performs a service request that is rejected by the Lower Tester with the error code 'Insufficient Authentication'.
3. Perform Step 3 if and only if the IUT starts encryption with the Lower Tester.
- a. The IUT starts the encryption process with the Lower Tester.
- b. The Lower Tester fails the encryption process.
4. Perform Step 4 if and only if the IUT initiates pairing with the Lower Tester.
- a. The IUT sends an event to the Upper Tester to confirm the peer device.
- b. The Upper Tester verifies the peer device with the IUT.
- c. The IUT and the Lower Tester complete the pairing procedure.
- d. The IUT encrypts the link using a new Long Term Key.
- e. The IUT completes the previously ordered service request successfully.

Figure 4.160: GAP/SEC/AUT/BV-19-C [Service Response Insufficient Authentication -Central role] MSC

- Expected Outcome

## Pass verdict

After receiving the error response 'Insufficient Authentication' , the IUT behaves correctly. If the IUT re-pairs, the Upper Tester confirms the remote device before starting the pairing procedure and encrypts the link with a new LTK.

## GAP/SEC/AUT/BV-20-C [Service Response Insufficient Authentication -Peripheral role]

- Test Purpose

Verify that the IUT, when bonded with a peer device, tests the bond when receiving the error response 'Insufficient Authentication', if link is unencrypted, before eventually removing the bond to perform a new pairing. During the new pairing, the IUT triggers user interaction to confirm the remote device.

- Reference

[9] 10.3, 10.3.2

- Initial Condition
- -The IUT is the SM responder and the GATT Client and is in the Peripheral role.
- -The IUT supports security manager bonding.
- -Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT and the Lower Tester are bonded before the connection and service discovery has been performed. The IUT's LTK has been distributed.
- -The Lower Tester has not stored the LTK from the IUT, which will result in the 'Insufficient Authentication' error in Step 2.
- Test Procedure
1. Perform either alternative 1A or 1B depending on if the IUT automatically starts the encryption procedure with bonded devices before issuing any service request.

Alternative 1A (The IUT does not automatically start the encryption procedure.)

- 1A.1 The IUT performs a service request with the Lower Tester.
- 1A.2 The Lower Tester rejects the service request with the error code 'Insufficient Authentication'.
- 1A.3 Optionally: The IUT may initiate the pairing procedure.

Alternative 1B (The IUT automatically starts the encryption procedure.)

- 1B.1 The IUT sends a Security Request for the link to be encrypted.
- 1B.2 The Lower Tester initiates the pairing procedure with the IUT.
- 1B.3 Optionally: The IUT may initiate the pairing procedure.
2. Perform Step 2 if and only if the pairing procedure has been initiated by the IUT in 1A.3 or 1B.3.
- a. The IUT sends an event to the Upper Tester to confirm the peer device.
- b. The Upper Tester verifies the peer device with the IUT.
- c. The pairing procedure is completed.
3. The IUT performs a service request with the Lower Tester.
4. The Lower Tester completes the service request successfully.

Figure 4.161: GAP/SEC/AUT/BV-20-C [Service Response Insufficient Authentication -Peripheral role] MSC

## · Expected Outcome

## Pass verdict

After receiving the error response 'Insufficient Authentication' , the IUT behaves correctly.

If the IUT re-pairs, the Upper Tester confirms the remote device before the Lower Tester initiates the pairing procedure and encrypts the link with a new LTK.

## GAP/SEC/AUT/BV-21-C [Lost Bond -Initiator role]

- Test Purpose

Verify that the IUT will inform the upper layer about a lost bond, if the link is refused to be encrypted with the LTK distributed during the prior pairing procedure.

The IUT is the SM initiator, GATT Client, and is in the Central role.

The IUT supports security manager bonding.

- Reference

[9] 10.3

- Initial Condition
- -The IUT and the Lower Tester are bonded during a prior connection, and the Lower Tester's LTK has been distributed.
- -The Lower Tester has removed its bond with the IUT prior to the IUT connecting.
- -A physical link is established between the IUT and the Lower Tester.
- Test Procedure
1. The IUT is bonded with the Lower Tester. It challenges the bond by (re)-encrypting the link with the distributed LTK.
2. The bond has been removed on the Lower Tester. The Lower Tester responds 'PIN or Key Missing' to the encryption request.
3. The IUT informs the upper layer that the bond has been lost.
- Expected Outcome

Figure 4.162: GAP/SEC/AUT/BV-21-C [Lost Bond -Initiator role] MSC

## Pass verdict

On receiving the error response 'PIN or Key Missing' the IUT informed the upper layer that the bond has been lost.

## GAP/SEC/AUT/BV-22-C [Lost Bond -Responder role]

- Test Purpose

Verify that the IUT will inform the upper layer about a lost bond, if the peer refuses to encrypt the link with the LTK distributed during the prior pairing procedure.

The IUT is the SM responder, GATT Client, and is in the Peripheral role.

The IUT supports security manager bonding.

- Reference

[9] 10.3

- Initial Condition
- -The IUT and the Lower Tester were bonded during a prior connection, and the IUT's LTK has been distributed.
- -The Lower Tester has removed its bond with the IUT prior to the IUT connecting.
- -Physical link is established between the IUT and the Lower Tester.
- Test Procedure
1. The IUT is bonded with the Lower Tester. It challenges the bond by sending a security request to enable encryption.
2. The bond has been removed on the Lower Tester. The Lower Tester initiates a pairing procedure.
3. The IUT informs the upper layer that the bond has been lost.
- Expected Outcome

Figure 4.163: GAP/SEC/AUT/BV-22-C [Lost Bond -Responder role] MSC

## Pass verdict

On receiving a pairing request as a successor to the security request, the IUT informed the upper layer that the bond has been lost.

## GAP/SEC/AUT/BV-23-C [Service Response -Insufficient Encryption, Peripheral]

- Test Purpose

Verify that the IUT properly rejects the service request when the required pairing has occurred and encryption is required (LE security mode 1) if encryption is not enabled and then completes service correctly with the Lower Tester acting in the Central role.

The IUT is operating in the Peripheral role.

The Lower Tester is operating in the Central role.

- Reference

[4] 10.3

- Initial Condition
- -Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value.
- -A physical link is established by either directed or undirected connectable mode.
- -Previous bond exists between the IUT and the Lower Tester with authenticated pairing.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.
- Test Procedure
1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value, go to Step 4.
2. If the link is not encrypted, the Lower Tester initiates a service request to the IUT.
3. If the IUT detects that no LTK is available then the IUT rejects the service request with error code 'Insufficient Authentication'. If the IUT detects LTK is available and link is unencrypted then the IUT rejects the service request with error code 'Insufficient Encryption'.
4. The Lower Tester initiates encryption and sends service request again.
5. Link encryption is completed successfully.
6. The IUT replies with correct service response.

Figure 4.164: GAP/SEC/AUT/BV-23-C [Service Response -Insufficient Encryption, Peripheral] MSC

- Expected Outcome

## Pass verdict

Encryption setup completes successfully.

Service response is properly sent by the IUT after Step 6.

## GAP/SEC/AUT/BV-24-C [Service Response -Insufficient Encryption, Central]

- Test Purpose

Verify that the IUT properly rejects the service request when the required pairing has occurred and encryption is required (LE security mode 1) if encryption is not enabled and then completes service correctly with the Lower Tester acting in the Peripheral role.

The IUT is the SM initiator, GATT Server, and is operating in the Central role.

The Lower Tester is operating in the Peripheral role.

- Reference

[4] 10.3

- Initial Condition
- -Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value.
- -A physical link is established by either directed or undirected connectable mode.
- -Previous bond exists between the IUT and the Lower Tester with authenticated pairing using either LE Legacy or LE Secure Connections.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.
- Test Procedure
1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value, go to Step 5.
2. If the link is not encrypted, then the Lower Tester initiates a service request to the IUT.
3. The IUT detects that the link is not encrypted.
4. The IUT rejects the service. If the IUT detects that no LTK is available then the IUT rejects the service request with error code 'Insufficient Authentication'. If the IUT detects that LTK is available and link is unencrypted, then the IUT rejects the service request with error code 'Insufficient Encryption'.
5. The Lower Tester initiates encryption and sends the service request again.
6. Link encryption is completed successfully.
7. The IUT replies with correct service response.

Figure 4.165: GAP/SEC/AUT/BV-24-C [Service Response -Insufficient Encryption, Central] MSC

- Expected Outcome

## Pass verdict

Encryption setup completes successfully.

Service response is properly sent by the IUT after Step 7.

## 4.7.5.1.1 Service Response -Insufficient Authentication

- Test Purpose

Verify that the IUT prompts a user interaction before initiating the pairing procedure when a service request failed for 'Insufficient Authentication' and the encryption procedure has failed.

- Reference

[17] 10.3.2

- Initial Condition
- -The IUT is the GATT Client and is in the role specified in Table 4.31.
- -The IUT supports security manager bonding.
- -Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value.
- -TSPX\_Use\_IXIT\_TSPX\_spsm determines whether the Upper Tester uses the TSPX\_spsm or will use the MMI to prompt for the L2CAP SPSM.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT and the Lower Tester are bonded before the connection and service discovery have been performed.
- -The Initial Condition from Table 4.31 is established.
- -The Lower Tester has not stored the LTK from the IUT, which will result in the 'Insufficient Authentication' error in Step 2.

## · Test Case Configuration

Table 4.31: Service Response -Insufficient Authentication test cases

| Test Case | Role | Initial Condition |
| GAP/SEC/AUT/BV-25-C | Central | The Lower Tester's LTK has been distributed. |

## · Test Procedure

1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value, go to Step 3.
2. The IUT performs a service request that is rejected by the Lower Tester with the error code 'Insufficient Authentication'.
3. The IUT starts the encryption procedure.
4. Perform either alternative 4A or 4B depending on the IUT role.

Alternative 4A (The IUT is in the Central role):

- 4A.1 The Lower Tester is to fail the encryption procedure.

Alternative 4B (The IUT is in the Peripheral role):

- 4B.1 The Lower Tester initiates pairing.
5. The IUT may start User Interaction by executing Steps 6 -9.
6. The remote device is confirmed by the Upper Tester, prompting the IUT to initiate, if the IUT is in the Central role, or to continue, if the IUT is in the Peripheral role, the pairing procedure.
7. The pairing is completed successfully and key information is exchanged properly.
8. If the IUT supports LE security mode 1, then the Lower Tester initiates encryption and send the service request again. If the IUT supports LE security mode 2, then the Lower Tester sends a signed service request with previously distributed CSRK.
9. The IUT completes the previously ordered service request with success.

Figure 4.166: Service Response -Insufficient Authentication MSC

- Expected Outcome

## Pass verdict

In Step 5, after the encryption procedure fails, the IUT prompts the Upper Tester to initiate a user interaction to confirm the remote device.

## 4.7.5.1.2 Service Response -Insufficient Encryption

- Test Purpose

Verify that the IUT prompts a user interaction before initiating the pairing procedure when a service request failed for 'Insufficient Encryption' and the encryption procedure has failed.

## · Reference

[17] 10.3.2

## · Initial Condition

- -The IUT is the GATT Client and is in the role specified in Table 4.32.
- -The IUT supports security manager bonding.
- -Whether the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value.
- -A physical link is established by either directed or undirected connectable mode.
- -A previous bond exists between the IUT and the Lower Tester with authenticated pairing.
- -The Upper Tester of the IUT is either a GATT profile or a higher-layer protocol.
- Test Case Configuration
- Test Procedure
1. If the IUT starts the encryption procedure with bonded devices before issuing any service request is specified in the TSPX\_encryption\_before\_service\_request IXIT value, go to Step 5.
2. The IUT initiates a service request to the Lower Tester.
3. The Lower Tester detects that the link is not encrypted.
4. The Lower Tester rejects the service request with error code 'Insufficient Encryption'.
5. The IUT initiates the encryption procedure.
6. Perform either alternative 6A or 6B depending on the IUT role.
- Alternative 6A (The IUT is in the Central role):
- 6A.1 The Lower Tester fails the encryption procedure.
- Alternative 6B (The IUT is in the Peripheral role):
- 6B.1 The Lower Tester initiates pairing.
7. The IUT may start User Interaction by executing Steps 9 -11.
8. The remote device is confirmed by the Upper Tester, prompting the IUT to initiate, if the IUT is in the Central role, or to continue, if the IUT is in the Peripheral role, the pairing procedure.
9. The pairing is completed successfully, and key information is exchanged properly.
10. The IUT sends the service request again.
11. The Lower Tester replies with a correct service response.

Table 4.32: Service Response -Insufficient Encryption test cases

| Test Case | Role |
| GAP/SEC/AUT/BV-27-C | Central |
| GAP/SEC/AUT/BV-28-C | Peripheral |

Figure 4.167: Service Response -Insufficient Encryption MSC

- Expected Outcome

## Pass verdict

In Step 9, the IUT prompts the Upper Tester to initiate a user interaction to confirm the remote device.

## 4.7.5.2 Connection Based Data Signing

Verify the correct implementation of the GAP data signing procedure.

## GAP/SEC/CSIGN/BV-01-C [Connection Based Signing -Sender]

- Test Purpose

Verify that the IUT can properly sign the data when LE security mode 2 is required.

Verify that the IUT sends data that is properly signed using the Connection Signature Resolving Key (CSRK) previously distributed to the Lower Tester.

The Lower Tester receives the signed data from the IUT and verifies that the MAC and SignCounter are correct.

- Reference

[4] 10.4

- Initial Condition
- -The IUT is the role specified in the TSPX\_gap\_iut\_role IXIT entry.
- -A dedicated bonding was performed and a CSRK was distributed from the IUT to the Lower Tester.
- -A physical link is established between the IUT and the Lower Tester.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.
- Test Procedure
1. The Upper Tester of the IUT requests the IUT to send a service request signed with previously distributed CSRK.
2. The Lower Tester receives the signed service request and verifies the MAC and SignCounter.
3. The Lower Tester accepts the service request from the IUT.
- Expected Outcome

Figure 4.168: GAP/SEC/CSIGN/BV-01-C [Connection Based Signing -Sender] MSC

## Pass verdict

The Lower Tester receives the signed service request and verifies that the MAC and SignCounter are correct.

## GAP/SEC/CSIGN/BV-02-C [Connection Based Signing -Receiver]

- Test Purpose

Verify that the IUT can properly verify the MAC and SignCounter when LE security mode 2 is required.

Verify that the IUT can properly verify the MAC and SignCounter from the Lower Tester.

The data is signed using the Connection Signature Resolving Key (CSRK) previously distributed from the Lower Tester.

- Reference

[4] 10.4

- Initial Condition
- -The IUT is the role as specified in the TSPX\_gap\_iut\_role IXIT entry.
- -A dedicated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT.
- -A physical link is established between the IUT and the Lower Tester.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.
- Test Procedure
1. The Lower Tester sends a service request signed with previously distributed CSRK to the IUT.
2. The IUT receives the signed service request and verifies the MAC and SignCounter.
3. The IUT forwards the service request to the Upper Tester.
4. The Upper Tester accepts the service request.
5. The Upper Tester sends the proper service response to the Lower Tester.
- Expected Outcome

Figure 4.169: GAP/SEC/CSIGN/BV-02-C [Connection Based Signing -Receiver] MSC

## Pass verdict

The Upper Tester receives a correct service request.

## GAP/SEC/CSIGN/BI-01-C [Connection Based Signing -Receiver -Invalid Signing]

- Test Purpose

Verify that the IUT can detect an invalid signed service request from the Lower Tester and reject it.

The data is signed with an incorrect CSRK.

- Reference

[4] 10.4

- Initial Condition
- -The IUT is in the role specified in the TSPX\_gap\_iut\_role IXIT entry.
- -A dedicated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT.
- -A physical link is established between the IUT and the Lower Tester.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.
- Test Procedure
1. The Lower Tester sends a service request signed with incorrect CSRK to IUT.
2. The IUT receives the signed service request and detects invalid MAC.
3. The IUT silently discards the service request.
- Expected Outcome

Figure 4.170: GAP/SEC/CSIGN/BI-01-C [Connection Based Signing -Receiver -Invalid Signing] MSC

## Pass verdict

The IUT receives signed data from the Lower Tester.

The IUT detects the signed data has incorrect CSRK.

The IUT ignores the received signed data.

The IUT does not forward the received signed data to the Upper Tester.

If this is a service request, the Lower Tester does not receive any service response or receives an error response from the IUT.

## GAP/SEC/CSIGN/BI-02-C [Connection Based Signing -Receive Invalid SignCounter]

- Test Purpose

Verify that the IUT can detect an invalid signed service request from the Lower Tester and reject it. The data is signed with invalid SignCounter.

- Reference

[4] 10.4

- Initial Condition
- -The IUT is in the role specified in the TSPX\_gap\_iut\_role IXIT entry.
- -A dedicated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT.
- -A physical link is established between the IUT and the Lower Tester.
- -The Upper Tester of the IUT is either a GATT profile or a higher layer protocol.

## · Test Procedure

1. The Lower Tester sends a service request with SignCounter = 0 to the IUT.
2. The IUT receives the signed service request and properly forwards it to the Upper Tester.
3. The Lower Tester sends a service request with SignCounter = 1 to the IUT.
4. The IUT receives the signed service request and properly forwards it to the Upper Tester.
5. The Lower Tester sends a service request with SignCounter = 0 to the IUT.
6. The IUT receives the signed service request and silently discards it.
- Expected Outcome

Figure 4.171: GAP/SEC/CSIGN/BI-02-C [Connection Based Signing -Receive Invalid SignCounter] MSC

## Pass verdict

The IUT does not forward the last received signed data with incorrect SignCounter value to the Upper Tester.

## GAP/SEC/CSIGN/BI-03-C [Connection Based Signing -Receive, No Bonding, as Peripheral]

- Test Purpose

Verify that the IUT properly discards the message when receiving a 'signed write command' with no bonding info when LE security mode 2 level 1 is required.

The data is signed with a CSRK that was distributed with either unauthenticated or authenticated bonding. After bonding, the IUT's bonding information was removed by the Upper Tester.

The IUT's bonding information can be removed by the Upper Tester.

- Reference

[4] 10.4

- Initial Condition
- -An unauthenticated or authenticated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT.
- -The IUT's bonding information was removed by the Upper Tester.
- -The IUT is in the role specified in the TSPX\_gap\_iut\_role IXIT entry.
- -A physical link is established between the IUT and the Lower Tester.
- -The Upper Tester of the IUT has a pre-defined characteristic attribute value handle that supports signed write command with security request of LE security mode 2 level 1.
- Test Procedure
1. The Lower Tester sends a 'signed write command' with distributed CSRK to the IUT.
2. The IUT receives the 'signed write command' but detects that there is no bonding information of the Lower Tester.
3. The IUT discards the 'signed write command'.
4. The IUT does not try to re-establish bonding.
- Expected Outcome

Figure 4.172: GAP/SEC/CSIGN/BI-03-C [Connection Based Signing -Receive, No Bonding, as Peripheral] MSC

## Pass verdict

The Upper Tester does not receive the 'signed write' command.

## GAP/SEC/CSIGN/BI-04-C [Connection Based Signing -Receive, Insufficient Authentication, as Peripheral]

- Test Purpose

Verify that the IUT properly discards a signed data write with insufficient security level when LE security mode 2 level 2 is required.

The data is signed with a CSRK that was distributed with unauthenticated bonding.

- Reference

[4] 10.4

- Initial Condition
- -An unauthenticated bonding was performed and a CSRK was distributed from the Lower Tester to the IUT.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT is in the role specified in the TSPX\_gap\_iut\_role IXIT entry.
- -The Upper Tester of the IUT has a pre-defined characteristic attribute value handle that supports signed write command with security request of LE security mode 2 level 2.
- Test Procedure
1. The Lower Tester sends a 'signed write command' with distributed CSRK to the IUT.
2. The IUT receives the 'signed write command' but detects that there is insufficient authentication level of the bonding information of the Lower Tester.
3. The IUT discards the 'signed write command'.
- Expected Outcome

Figure 4.173: GAP/SEC/CSIGN/BI-04-C [Connection Based Signing -Receive, Insufficient Authentication, as Peripheral] MSC

## Pass verdict

The Upper Tester does not receive the 'signed write command' .

## 4.7.5.3 Privacy

Verify IUT compliance to the privacy feature.

## GAP/PRIV/CONN/BV-10-C [Peripheral Privacy]

- Test Purpose

Verify that the IUT in the Undirected Connectable mode supporting the Privacy feature can connect with another device performing the General Connection Establishment procedure.

The IUT is operating in the Peripheral role.

- Reference

[6] 10.7.1

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT has Privacy feature enabled.
- -TGAP(private\_addr\_int) for the IUT is specified in the TSPX\_iut\_private\_address\_interval IXIT value.
- -The IUT and the Lower Tester have performed the bonding procedures and distributed their respective IRKs using either LE Legacy or LE Secure Connections.
- Test Procedure
1. The Upper Tester orders the IUT to enter Undirected Connectable mode; the IUT sets the advertiser ' s address to a resolvable private address based on the IRK distributed during the bonding procedure.
2. The IUT changes the advertiser address to a new and unique resolvable address every TGAP(private\_addr\_int).
3. The Lower Tester verifies that the resolvable private address changes at least once after TGAP(private\_addr\_int).
4. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT; the Lower Tester creates the connection using the received resolvable private address from the IUT and sets the initiator ' s address to an RPA value based on the IRK of the Lower Tester.
5. The Lower Tester or the IUT terminates the connection.

Figure 4.174: GAP/PRIV/CONN/BV-10-C [Peripheral Privacy] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives connectable undirected advertising events from the IUT during the period that the IUT has privacy enabled and is in Undirected Connectable mode.

In each connectable undirected advertising event received, the advertiser address is set to a valid resolvable private address.

The Lower Tester is able to resolve and confirm the identity of the IUT from the received resolvable private address.

The Lower Tester verifies that the IUT changes the resolvable private address in the advertiser address of the received advertising events after TGAP(private\_addr\_int).

The Lower Tester establishes a connection with the IUT using the received advertiser address.

The Lower Tester or the IUT successfully terminates the connection.

## GAP/PRIV/CONN/BV-11-C [Central Privacy]

- Test Purpose

Verify that the IUT supporting the Privacy feature and performing the General Connection Establishment procedure can connect with another device supporting the Privacy feature in the Undirected Connectable mode.

The IUT is operating in the Central role.

- Reference

[6] 10.7.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT has Privacy feature enabled.
- -The support for accepting Public or Static addresses is specified in the TSPX\_bd\_addr\_iut IXIT value.

- -The IUT and the Lower Tester have performed the bonding procedures and distributed their respective IRKs using either LE Legacy or LE Secure Connections.
- Test Procedure
1. The Lower Tester enters Undirected Connectable mode; the Lower Tester sets the advertisers address to an RPA value based on the IRK of the Lower Tester.
2. The Upper Tester orders the IUT to perform the General Connection Establishment procedure; the IUT sets the initiator ' s address to a resolvable private address based on the IRK of the IUT.
3. A connection is established.
4. The Lower Tester or the IUT terminates the connection.
5. The Lower Tester enters Undirected Connectable mode; the Lower Tester sets the advertiser ' s address to a resolvable private address based on a random number that is not its IRK.
6. The Upper Tester orders the IUT to perform the General Connection Establishment procedure.
- Expected Outcome

Figure 4.175: GAP/PRIV/CONN/BV-11-C [Central Privacy] MSC

## Pass verdict

The Lower Tester receives a connection request from the IUT during the period that the IUT has privacy enabled and is performing the General Connection Establishment procedure.

In each connection request packet received by the Lower Tester, the initiator ' s address is set to a valid resolvable private address.

The Lower Tester is able to resolve and confirm the identity of the IUT from the received resolvable private address.

The Lower Tester verifies that the IUT changes its (InitA field) resolvable private address in the connection request packet.

The Lower Tester establishes a connection with the IUT.

The Lower Tester or the IUT successfully terminates the connection.

The IUT does not perform the Connection Establishment procedure when the Lower Tester uses a resolvable private address based on an incorrect IRK.

## · Notes

Since the IUT, when receiving advertisement packets with incorrect RPAs, should not initiate the connection establishment procedure, multiple undirected connectable advertisement packets should be sent to verify compliance.

## GAP/PRIV/CONN/BV-12-C [Peripheral Privacy, Unresolvable RPA]

## · Test Purpose

Verify that the IUT in the Undirected Connectable mode supporting the Privacy feature properly handles the connection request when the IUT receives an unresolvable RPA. The IUT handles the connection request using one of the following: accept the connection, disconnect with the error code 'Authentication Failure', perform the pairing procedure, perform the authentication procedure.

The IUT is operating in the Peripheral role.

- Reference

[17] 10.7.1

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- -The IUT has the Privacy feature enabled.
- -The IUT has a stored bond.
- Test Procedure
1. The Upper Tester orders the IUT to enter Undirected Connectable mode.
2. The Lower Tester performs the General Connection Establishment procedure to connect to the IUT.
3. The Lower Tester attempts to create the connection and sets the initiator ' s address to an unresolvable RPA.
4. The IUT fails to resolve the initiator's RPA.

Alternative 1: The IUT accepts and establishes the connection.

Alternative 2: The IUT disconnects the connection with the error code 'Authentication Failure'.

Alternative 3: The IUT accepts the connection and performs the pairing procedure with the Lower Tester.

Alternative 4: The IUT accepts the connection and performs the authentication procedure with the Lower Tester.

Figure 4.176: GAP/PRIV/CONN/BV-12-C [Peripheral Privacy, Unresolvable RPA] MSC

## · Expected Outcome

## Pass verdict

In Step 4 , the IUT fails to resolve the initiator's RPA.

Alternative 1: In Step 5, the IUT accepts and establishes the connection.

Alternative 2: In Step 5 , the IUT disconnects with the error code 'Authentication Failure'.

Alternative 3: In Step 5, the IUT and the Lower Tester pair successfully.

Alternative 4: In Step 5, the IUT and the Lower Tester complete the authentication procedure successfully.

## 4.7.6 AD type

- Test Purpose

Verify that the IUT sends the valid AD type specified in Table 4.33 in advertising and scan response data.

- Reference

## 4 11

- Initial Condition
- -The IUT is Broadcaster or Peripheral.
- -The Lower Tester is Observer or Central.
- -The IUT is in Link Layer state 'Standby'.
- -For GAP/ADV/BV-17-C, the expected URI UTF-8 string is defined in TSPX\_URI in IXIT [3].

## · Test Case Configuration

| Test Case ID | Reference | AD Type | Additional Test Requirements |
| GAP/ADV/BV-03-C [AD type - Flags] | [7] 1.3 | Flags | This AD type must be present if the advertising packet is connectable and the IUT supports at least one of the features listed in [7] 1.3.2. Otherwise, it is optional, but, if present, it must meet these requirements. The flags in the data must match the features supported by the IUT. The last octet in the data must not be zero. The data may be omitted (with the AD structure Length equal to 1) if the data would be all zeroes. There must be only one instance of this AD type and it must be in the advertising data, not the scan response data. |

| Test Case ID | Reference | AD Type | Additional Test Requirements |
| GAP/ADV/BV-13-C [AD type - Random Target Address] | [4] 10.8 [7] 1.14 [8] 1.3.2 | Random Target Address | The advertising or scan response data has a length that is a multiple of 6 and contains one or more addresses. For each address, either: The two most significant bits of the address are the same and the remaining 46 bits contain at least one 0 bit and one 1 bit. The most significant bit is 0, the next bit is 1, and the next 22 bits contain at least one 0 bit and one 1 bit. (The least significant 24 bits are unconstrained.) There must be only one instance of this AD type and it must not appear in both the advertising and scan response data of the same advertisement. |

| Test Case ID | Reference | AD Type | Additional Test Requirements |
| GAP/ADV/BV-17-C [AD type - URI] | [7] 1.18 | URI | The advertising data and scan response data must contain a correctly formatted UTF-8 string representing the URI. The first code point must be one that is in the relevant Assigned Numbers. If the first code point is U+0001, represented in UTF-8 as a single octet with value 0x01, the actual scheme and ':' are included in the remaining UTF -8 string. Otherwise, they are omitted from the string. The string matches the value provided in TSPX_URI. |

Table 4.33: AD type test cases

- Test Procedure
1. The Upper Tester orders the IUT to start advertising; the IUT enters broadcast mode or a discoverable mode.
2. The Lower Tester enters Active Scanning.
- Expected Outcome

Figure 4.177: AD type MSC

## Pass verdict

The Advertising or Scan Response data does not contain zero octets between the AD structures or after the last AD structure.

Reserved bits or values are not used.

All the requirements in the Additional Test Requirements column of Table 4.33 are met.

- Notes

Unless stated otherwise in the Additional Test Requirements, an AD type may appear more than once in the same advertisement, including in both the advertising data and scan response data.

## 4.7.6.1 AD type -Encrypted Data

- Test Purpose

Verify that the IUT sends valid Encrypted Data AD type in advertising. The AD Data payload is encrypted using a pre-shared key, a pre-shared initialization vector, and a randomizer. If supported, the IUT may include non-significant data.

- Reference

[7] 1.23

- Initial Condition
- -The IUT is Peripheral.
- -The Lower Tester is Central.
- -The IUT is in Link Layer state 'Standby'.
- -The Lower Tester is in the Passive Scanning state.
- -If TSPX\_ead\_keys\_sharing\_method is selected as 'KEYS\_SHARED\_VIA\_IXIT', the IUT and the Lower Tester will use the already shared Session Key and IV value from TSPX\_encrypted\_data\_key and TSPX\_initialization\_vector.

- -If TSPX\_ead\_keys\_sharing\_method is selected as 'KEYS\_EXCHANGED\_VIA\_CONNECTION', the IUT will read the already shared Session Key and IV from the Encrypted Data Key Material characteristic.
- Test Case Configuration
- Test Procedure
1. The Upper Tester orders the IUT to start advertising; the IUT enters broadcast mode or a discoverable mode and begins advertising using Encrypted Advertising Data with a random payload.
2. The IUT sends an Advertising event using Encrypted Advertising Data with the payload from Step 1.
3. The Upper Tester orders the IUT to begin advertising using Encrypted Advertising Data with a payload that is different from the payload in Step 1.
4. The IUT sends an Advertising event using Encrypted Advertising Data with the payload from Step 3. If allowed by Table 4.34, the IUT may send non-significant data after the payload of encrypted AD structures.
5. The Upper Tester orders the IUT to begin advertising using Encrypted Advertising Data with the same payload as Step 1.
6. The IUT sends an Advertising event using Encrypted Advertising Data with the payload in Step 5.
- Expected Outcome

Table 4.34: AD type -Encrypted Data test cases

| Test Case | Non-significant data |
| GAP/ADV/BV-20-C [AD type - Encrypted Data] | No |
| GAP/ADV/BV-21-C [AD type - Encrypted Data] | Yes |

Figure 4.178: AD type -Encrypted Data MSC

## Pass verdict

In Steps 2, 4, and 6, the IUT sends Advertising Data that contains a 5 octet Randomizer, a properly encrypted Payload, and a 4 valid octet MIC. The encrypted Payload Data, MIC, and Randomizer are different each time the payload data is changed.

In Step 2, the decrypted payload matches the payload in Step 1.

In Step 4, the decrypted payload matches the payload in Step 3.

In Step 6, the decrypted payload matches the payload in Step 5.

- Notes

It is optional to include any of the AD types in advertising and scan response data.

## GAP/SCN/BV-01-C [AD type -Encrypted Data, Decrypt Advertising Data]

- Test Purpose

Verify that the IUT correctly decodes a received Encrypted Data AD type from the Lower Tester.

- Reference

[7] 1.23

- Initial Condition
- -The Lower Tester is Peripheral.
- -The IUT is Central.
- -The IUT is in Link Layer state 'Standby'.
- -If TSPX\_ead\_keys\_sharing\_method is selected as 'KEYS\_SHARED\_VIA\_IXIT', the IUT and the Lower Tester will use the already shared Session Key and IV value from TSPX\_encrypted\_data\_key and TSPX\_initialization\_vector.
- -If TSPX\_ead\_keys\_sharing\_method is selected as 'KEYS\_EXCHANGED\_VIA\_CONNECTION', the IUT will read the already shared Session Key and IV from the Encrypted Data Key Material characteristic.
- Test Procedure
1. The Upper Tester orders the IUT to start Passive Scanning.
2. The Lower Tester starts advertising an Encrypted Data AD type with encrypted advertising with a valid MIC.
3. The IUT reports the unencrypted advertising data to the Upper Tester.

Figure 4.179: GAP/SCN/BV-01-C [AD type -Encrypted Data, Decrypt Advertising Data] MSC

- Expected Outcome

## Pass verdict

In Step 3, the IUT sends an advertising report to the Upper Tester with the same advertising data as the Lower Tester unencrypted advertising data from Step 2.

## GAP/GAT/BV-15-C [Encrypted Data Key Characteristic Indication, GATT Server]

- Test Purpose

Verify that the IUT with an authenticated and authorized connection properly sends a GATT Indication PDU to the Lower Tester when the Encrypted Data Key Characteristic value is updated.

- Reference

[18] 12.6

- Initial Condition
- -The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT Server.
- -A physical link is established between the IUT and the Lower Tester that is authenticated and authorized.
- Test Procedure
1. The Lower Tester sends an ATT\_WRITE\_REQ to the IUT with CCCD set to 0x0002.
2. The IUT sends an ATT\_WRITE\_RSP to the Lower Tester.
3. The Upper Tester commands the IUT to change the Encrypted Data Key Characteristic value with a new key.
4. The IUT sends an ATT\_HANDLE\_VALUE\_IND PDU to the Lower Tester with Attribute Handle set to the Encrypted Data Key Characteristic, and Attribute Value set to the new value.
5. The Lower Tester sends an ATT\_HANDLE\_VALUE\_CFM PDU to the IUT.
- Expected Outcome

Figure 4.180: GAP/GAT/BV-15-C [Encrypted Data Key Characteristic Indication, GATT Server] MSC

## Pass verdict

In Step 4, the IUT sends an ATT Handle Value Indication PDU to the Lower Tester.

## 4.7.7 Generic Access Profile characteristics

Verify the correct implementation of the GAP characteristics.

## 4.7.7.1 GAP attributes

## GAP/GAT/BV-09-C [Encrypted Data Key Material, Authenticated and Authorized]

- Test Purpose

Verify that the GAP 'Encrypted Data Key Material' Characteristic on the IUT is readable by the Lower Tester when the connection is authenticated and authorized.

- Reference

[18] 12.6

- Initial Condition
- -The Lower Tester is a GATT client.
- -The Upper Tester is a GATT server that has implemented the GATT service discovery procedures.
- -The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT server.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT and the Lower Tester are authenticated and have exchanged the Session Key and IV.
- Test Procedure
1. The Lower Tester performs a GATT service discovery for the GAP Service UUID.
2. The IUT responds with a GATT service discovery response for the GAP Service UUID with the Handles Information List.
3. The Lower Tester performs a GATT characteristic discovery by UUID.
4. The IUT responds with a GATT characteristic discovery by UUID response with an attribute Data List that contains the Encrypted Data Key Material Handle.
5. The Lower Tester performs a GATT characteristic read value with the Encrypted Data Key Material Handle from Step 4.
6. The IUT sends an authorization request to the Upper Tester.
7. The Upper Tester orders the IUT to authorize the Lower Tester.
8. The IUT responds to the request in Step 5 with a GATT characteristic read value response with the Encrypted Data Key Material value.
9. The Lower Tester performs a GATT characteristic write value with the Encrypted Data Key Material Handle from Step 4 and 24 octets of random values.
10. The IUT responds with an ATT error response with Error Code &gt; 0.

Figure 4.181: GAP/GAT/BV-09-C [Encrypted Data Key Material, Authenticated and Authorized] MSC

- Expected Outcome

## Pass verdict

In Step 8, the IUT responds with the Encrypted Data Key Material value.

In Step 10, the IUT sends an ATT Error response to the Lower Tester.

## GAP/GAT/BV-10-C [Encrypted Data Key Material, Not Authenticated]

- Test Purpose

Verify that the GAP 'Encrypted Key Data Material' Characteristic on the IUT cannot be read by the Lower Tester when the connection is not authenticated.

- Reference

[18] 12.6

- Initial Condition
- -The Lower Tester is a GATT client.
- -The Upper Tester is a GATT server that has implemented the GATT service discovery procedures.
- -The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT Server.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT and the Lower Tester are not authenticated.

- Test Procedure
1. The Lower Tester performs a GATT service discovery for the GAP Service UUID.
2. The IUT responds with a GATT service discovery response for the GAP Service UUID with the Handles Information List.
3. The Lower Tester performs a GATT characteristic discovery by UUID.
4. The IUT responds with a GATT characteristic discovery by UUID response with an attribute Data List that contains the Encrypted Data Key Material Handle.
5. The Lower Tester performs a GATT characteristic read value with the Encrypted Data Key Material Handle from Step 4.
6. The IUT responds with an ATT Error response with Error Code &gt; 0.
- Expected Outcome

Figure 4.182: GAP/GAT/BV-10-C [Encrypted Data Key Material, Not Authenticated] MSC

## Pass verdict

In Step 6, the IUT sends an ATT Error response to the Lower Tester.

## GAP/GAT/BV-11-C [Encrypted Data Key Material, Not Authorized]

- Test Purpose

Verify that the GAP 'Encrypted Key Data Material' Characteristic on the IUT cannot be read by the Lower Tester when the connection is not authorized.

- Reference

[18] 12.6

- Initial Condition
- -The Lower Tester is a GATT client.
- -The Upper Tester is a GATT server that has implemented the GATT service discovery procedures.
- -The IUT is in an LE connection in the Peripheral role or a BR/EDR connection and is a GATT Server.

- -A physical link is established between the IUT and the Lower Tester.
- -The IUT and the Lower Tester are authenticated but not authorized.
- Test Procedure
1. The Lower Tester performs a GATT service discovery for the GAP Service UUID.
2. The IUT responds with a GATT service discovery response for the GAP Service UUID with the Handles Information List.
3. The Lower Tester performs a GATT characteristic discovery by UUID.
4. The IUT responds with a GATT characteristic discovery by UUID response with an attribute Data List that contains the Encrypted Data Key Material Handle.
5. The Lower Tester performs a GATT characteristic read value with the Encrypted Data Key Material Handle from Step 4.
6. The IUT sends an authorization request to the Upper Tester.
7. The Upper Tester orders the IUT not to authorize the Lower Tester.
8. The IUT responds to the request in Step 5 with an ATT Error Response.
- Expected Outcome

Figure 4.183: GAP/GAT/BV-11-C [Encrypted Data Key Material, Not Authorized] MSC

## Pass verdict

In Step 8, the IUT sends an ATT Error response to the Lower Tester.

## 4.7.7.1.1 Discover GAP characteristic

- Test Purpose

Verify that the IUT properly implements the GAP characteristic.

- Reference

[18] 12

- Initial Condition
- -The Lower Tester is a GATT Client.
- -The IUT is a GATT Server.
- -A physical link is established between the IUT and the Lower Tester.
- -The IUT is not bonded or paired with the Lower Tester.
- -The IUT has the Authorization and Authentication for GATT attributes specified in Table 4.35.
- -The IUT is discoverable.
- Test Case Configuration

| Test Case | Authorization and Authentication | Characteristic | Perform Step 6 | Characteristic Value |
| GAP/GAT/BV-04-C [Discover GAP Characteristic, Peripheral Preferred Connection Parameters Characteristic] | Any required to read Peripheral Preferred Connection Parameters | Peripheral Preferred Connection Parameters | Yes | 8 octets |
| GAP/GAT/BV-12-C [Discover GAP Characteristic, LE GATT Security Levels Characteristic] | None | LE GATT Security Levels | Yes | Even number of octets; each pair of octets corresponds to a valid and properly formatted security mode and level for that mode |
| GAP/GAT/BV-16-C [Discover GAP Characteristic, Device Name] | None | Device Name | No | 0 or more octets |
| GAP/GAT/BV-17-C [Discover GAP Characteristic, Appearance] | None | Appearance | No | 2 octets |
| GAP/GAT/BV-18-C [Discover GAP Characteristic, Central Address Resolution] | None | Central Address Resolution | Yes | 1 octet with the value 0x00 or 0x01 |
| GAP/GAT/BV-19-C [Discover GAP Characteristic, Resolvable Private Address Only] | None | Resolvable Private Address Only | Yes | 1 octet with the value 0x00 |

Table 4.35: Discover GAP Characteristic test cases

## · Test Procedure

Figure 4.184: Discover GAP Characteristic MSC

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

## 4.7.7.1.2 Writeable characteristic

- Test Purpose

Verify that an IUT can support a writeable characteristic.

- Reference

[4] 12

- Initial Condition
- -A physical link is established between the IUT and the Lower Tester.
- -The Lower Tester knows the handle and the current value of the Characteristic specified in Table 4.36, after executing the procedure defined in Section 4.2.6.
- -The characteristic declaration includes either the Write (0x04) or Write Without Response (0x08) characteristic properties value, or both.
- Test Case Configuration

| Test Case | Characteristic |
| GAP/GAT/BV-05-C [Writeable Characteristic, Device Name] | Device Name |
| GAP/GAT/BV-06-C [Writeable Characteristic, Appearance] | Appearance |

Table 4.36: LE Discover Writeable Characteristics test cases

## · Test Procedure

Figure 4.185: Writeable Characteristic MSC

1. The Lower Tester sends an ATT\_WRITE\_CMD with the handle and new value of the Characteristic specified in Table 4.36.
2. The Lower Tester sends an ATT\_READ\_REQ to the IUT with the handle sent in Step 1.
3. The IUT sends an ATT\_READ\_RSP to the Lower Tester. If the handle and value are those sent in Step 1, the test ends with a Pass verdict.
4. The Lower Tester sends an ATT\_WRITE\_REQ with the handle and new value of the Characteristic specified in Table 4.36.
5. Perform either Alternative 5A or 5B depending on the IUT response:

Alternative 5A: The IUT responds with an ATT\_ERROR\_RSP with the error code 0x05 'Insufficient Authentication':

- 5A.1 The Lower Tester elevates the authentication or security level.
- 5A.2 Return to Step 4.

Alternative 5B: The IUT responds with an ATT\_WRITE\_RSP with the handle and value sent in Steps 1 and 4:

- 5B.1 The Lower Tester sends an ATT\_READ\_REQ to the IUT with the handle sent in Steps 1 and 4.
- 5B.2 The IUT sends an ATT\_READ\_RSP to the Lower Tester with the handle and value sent in Steps 1 and 4.
- Expected Outcome

## Pass verdict

In Step 3 or Step 5B.2, the IUT sends the handle and new value of the characteristic specified in Table 4.36.

## Fail verdict

In Step 5, the IUT responds with any PDU or PDU contents other than those specified in the two options.

## 4.7.8 Periodic Advertising modes and procedures

## 4.7.8.1 Periodic Advertising Synchronizability mode

## 4.7.8.1.1 Periodic Advertising Synchronizability mode -Broadcaster role

- Test Purpose

Verify the IUT in Periodic Advertising Synchronizability mode in the Broadcaster role where the Lower Tester, in the Observer role, performs the Periodic Advertising Synchronization Establishment procedure using extended advertising events, without listening for periodic advertising data.

- Reference

## 12 9.5.1

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- Test Case Configuration

| TCID | Periodic Advertising Type |
| GAP/PADV/PASM/BV-01-C | Periodic Advertising |
| GAP/PADV/PASM/BV-02-C | Periodic Advertising with Responses |

Table 4.37: Periodic Advertising Synchronizability mode -Broadcaster role test cases

Figure 4.186: Periodic Advertising Synchronizability mode -Broadcaster role MSC

1. The Upper Tester orders the IUT to enter Periodic Advertising Synchronizability mode.
2. The Lower Tester performs the Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising data for the Periodic Advertising Type specified in Table 4.37 and receives periodic advertising synchronization information.
- Expected Outcome

## Pass verdict

The Lower Tester receives periodic advertising synchronization information sent by the IUT.

The IUT stays in periodic advertising synchronizability mode for at minimum one extended advertising event.

- Notes

Since the periodic advertising synchronization information transmission is not a reliable transmission method, multiple periodic advertising synchronization information packets may need to be sent to verify compliance.

## 4.7.8.2 Periodic Advertising mode

## 4.7.8.2.1 Periodic Advertising mode -Broadcaster role

- Test Purpose

Verify the IUT in Periodic Advertising mode in the Broadcaster role where the Lower Tester, in the Observer role, synchronizes and listens for periodic advertising.

- Reference

[12] 9.5.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The periodic advertising data in Periodic Advertising mode for the IUT is specified in the TSPX\_periodic\_advertising\_data IXIT value.
- -The Lower Tester has synchronization information for the IUT's periodic advertising.

- Test Case Configuration
- Test Procedure
1. The Upper Tester orders the IUT to enter Periodic Advertising mode using the Periodic Advertising Type in Table 4.38 and the specified periodic advertising data.
2. The Lower Tester synchronizes and receives periodic advertising events.
- Expected Outcome

Table 4.38: Periodic Advertising Synchronizability mode -Broadcaster role test cases

| TCID | Periodic Advertising Type |
| GAP/PADV/PAM/BV-01-C | Periodic Advertising |
| GAP/PADV/PAM/BV-02-C | Periodic Advertising with Responses |

Figure 4.187: Periodic Advertising mode -Broadcaster role MSC

## Pass verdict

The Lower Tester receives periodic advertising events sent by the IUT.

The Lower Tester receives the specified periodic advertising data sent by the IUT.

- Notes

Since the periodic advertising is not a reliable transmission method, multiple periodic advertising packets may need to be sent to verify compliance.

## 4.7.8.3 Periodic Advertising Synchronization Establishment procedure

## 4.7.8.3.1 Periodic Synchronization Establishment procedure using extended advertising events without listening for Periodic Advertising -Observer role

- Test Purpose

Verify that the IUT in the Observer role performs the Periodic Synchronization Establishment procedure using extended advertising events and does not listen for periodic advertising events.

- Reference

[12] 9.5.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .

## · Test Case Configuration

Table 4.39: Periodic Synchronization Establishment procedure using extended advertising events without listening for Periodic Advertising -Observer role test cases

| TCID | Periodic Advertising Type |
| GAP/PADV/PASE/BV-01-C | Periodic Advertising |
| GAP/PADV/PASE/BV-07-C | Periodic Advertising with Responses |

- Test Procedure
1. The Lower Tester enters Periodic Advertising Synchronizability mode and begins transmitting periodic advertising synchronization information with the Periodic Advertising Type specified in Table 4.39.
2. The Lower Tester enters Periodic Advertising mode and begins transmitting periodic advertising events.
3. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising events.
4. The Upper Tester receives periodic advertising synchronization information from the IUT.
5. The Upper Tester does not receive periodic advertising reports from the IUT.
- Expected Outcome

Figure 4.188: Periodic Synchronization Establishment procedure using extended advertising events without listening for Periodic Advertising -Observer role MSC

## Pass verdict

The IUT receives the periodic advertising synchronization information sent from the Lower Tester and reports it to the Upper Tester.

The IUT does not report periodic advertising events to the Upper Tester.

- Notes

Since the periodic advertising synchronization information transmission is not a reliable transmission method, multiple periodic advertising synchronization information packets may need to be sent to verify compliance.

## 4.7.8.3.2 Periodic Synchronization Establishment procedure using extended advertising events listening for Periodic Advertising -Observer role

- Test Purpose

Verify that the IUT in the Observer role performs the Periodic Synchronization Establishment procedure using extended advertising events and listens for periodic advertising events.

- Reference

[12] 9.5.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The periodic advertising data in Periodic Advertising mode for the Lower Tester is specified in the TSPX\_periodic\_advertising\_data IXIT value.
- Test Case Configuration
- Test Procedure

Table 4.40: Periodic Synchronization Establishment procedure using extended advertising events listening for Periodic Advertising -Observer role test cases

| TCID | Periodic Advertising Type |
| GAP/PADV/PASE/BV-02-C | Periodic Advertising |
| GAP/PADV/PASE/BV-08-C | Periodic Advertising with Responses |

Figure 4.189: Periodic Synchronization Establishment procedure using extended advertising events listening for Periodic Advertising -Observer role MSC

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

## 4.7.8.3.3 Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising -Peripheral role

- Test Purpose

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection does not listen for periodic advertising events in the Peripheral role.

- Reference

[14] 9.5.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- Test Case Configuration

| TCID | Periodic Advertising Type |
| GAP/PADV/PASE/BV-03-C | Periodic Advertising |
| GAP/PADV/PASE/BV-09-C | Periodic Advertising with Responses |

Table 4.41: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising -Peripheral role test cases

Figure 4.190: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising -Peripheral role MSC

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

## 4.7.8.3.4 Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising -Peripheral role

- Test Purpose

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection listens for periodic advertising events in the Peripheral role.

- Reference

[14] 9.5.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- Test Case Configuration
- Test Procedure

Table 4.42: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising -Peripheral role test cases

| TCID | Periodic Advertising Type |
| GAP/PADV/PASE/BV-04-C | Periodic Advertising |
| GAP/PADV/PASE/BV-10-C | Periodic Advertising with Responses |

Figure 4.191: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising -Peripheral role MSC

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

## 4.7.8.3.5 Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising -Central role

- Test Purpose

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection does not listen for periodic advertising events in the Central role.

- Reference

[14] 9.5.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- Test Case Configuration

| TCID | Periodic Advertising Type |
| GAP/PADV/PASE/BV-05-C | Periodic Advertising |
| GAP/PADV/PASE/BV-11-C | Periodic Advertising with Responses |

Table 4.43: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising -Central role test cases

## · Test Procedure

Figure 4.192: Periodic Synchronization Establishment procedure over an LE connection without listening for Periodic Advertising -Central role MSC

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

## 4.7.8.3.6 Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising -Central role

- Test Purpose

Verify that the IUT performing the Periodic Synchronization Establishment procedure over an LE connection listens for periodic advertising events in the Central role.

- Reference

[14] 9.5.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- Test Case Configuration
- Test Procedure

Table 4.44: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising -Central role test cases

| TCID | Periodic Advertising Type |
| GAP/PADV/PASE/BV-06-C | Periodic Advertising |
| GAP/PADV/PASE/BV-12-C | Periodic Advertising with Responses |

Figure 4.193: Periodic Synchronization Establishment procedure over an LE connection listening for Periodic Advertising -Central role MSC

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

## 4.7.8.4 Periodic Advertising Synchronization Transfer procedure

## 4.7.8.4.1 Periodic Advertising Synchronization Transfer procedure -Peripheral role

- Test Purpose

Verify the IUT performing the Periodic Advertising Synchronization Transfer procedure in the Peripheral role; the Lower Tester, in the Central role, performs the Periodic Advertising Synchronization Establishment procedure over an LE connection.

- Reference

[14] 9.5.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- Test Case Configuration

| TCID | Periodic Advertising Type |
| GAP/PADV/PAST/BV-01-C | Periodic Advertising |
| GAP/PADV/PAST/BV-03-C | Periodic Advertising with Responses |

Table 4.45: Periodic Advertising Synchronization Transfer procedure -Peripheral role test cases

## · Test Procedure

Figure 4.194: Periodic Advertising Synchronization Transfer procedure -Peripheral role MSC

1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Peripheral role.
2. The Upper Tester configures the IUT to enter Periodic Advertising Synchronizability mode.
3. The Lower Tester performs the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.45.
4. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Transfer procedure with the Periodic Advertising Type specified in Table 4.45.
5. The Lower Tester receives periodic advertising synchronization information from the IUT.
6. Terminate the connection between the IUT and the Lower Tester.
- Expected Outcome

## Pass verdict

The Lower Tester receives periodic advertising synchronization information sent by the IUT.

## 4.7.8.4.2 Periodic Advertising Synchronization Transfer procedure -Central role

- Test Purpose

Verify the IUT performing the Periodic Advertising Synchronization Transfer procedure in the Central role; the Lower Tester, in the Peripheral role, performs the Periodic Advertising Synchronization Establishment procedure over an LE connection.

- Reference

[14] 9.5.4

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.

## · Test Case Configuration

Table 4.46: Periodic Advertising Synchronization Transfer procedure -Central role test cases

| TCID | Periodic Advertising Type |
| GAP/PADV/PAST/BV-02-C | Periodic Advertising |
| GAP/PADV/PAST/BV-04-C | Periodic Advertising with Responses |

## · Test Procedure

Figure 4.195: Periodic Advertising Synchronization Transfer procedure -Central role MSC

1. The Upper Tester configures the IUT to connect with the Lower Tester on the LE 1M PHY, and the Lower Tester connects with the IUT on the LE 1M PHY, with the IUT in the Central role.
2. The Upper Tester configures the IUT to enter Periodic Advertising Synchronizability mode.
3. The Lower Tester performs the Periodic Advertising Synchronization Establishment procedure over the LE connection for the Periodic Advertising Type specified in Table 4.46.
4. The Upper Tester orders the IUT to perform the Periodic Advertising Synchronization Transfer procedure with the Periodic Advertising Type specified in Table 4.46.
5. The Lower Tester receives periodic advertising synchronization information from the IUT.
6. Terminate the connection between the IUT and the Lower Tester.
- Expected Outcome

## Pass verdict

The Lower Tester receives periodic advertising synchronization information sent by the IUT.

## 4.7.8.5 Periodic Advertising Connection procedure

## GAP/PADV/PAC/BV-01-C [Create connection with synchronized device using the Periodic Advertising Connection procedure, Periodic Advertiser]

- Test Purpose

Verify that the IUT as a periodic advertiser can initiate a Link Layer connection with a synchronized device.

- Reference

[18] 9.5.5.2

- Initial Condition
- -The IUT is in the Link Layer Standby state as a Periodic Advertiser.
- Test Procedure
1. The Upper Tester orders the IUT to enter Periodic Advertising with Responses mode with valid Periodic Advertising Response Timing Information.
2. The Lower Tester synchronizes and receives periodic advertising events.
3. The Upper Tester orders the IUT to connect with the Lower Tester using the Periodic Advertising Connection procedure.
4. The IUT and the Lower Tester complete a Link Layer connection.
- Expected Outcome

Figure 4.196: Create connection with synchronized device using the Periodic Advertising Connection procedure, Periodic Advertiser MSC

## Pass verdict

In Step 4, the IUT has a Link Layer connection with the Lower Tester.

## GAP/PADV/PAC/BV-02-C [Create connection with synchronized device using the Periodic Advertising Connection procedure, Scanner]

- Test Purpose

Verify that the IUT can accept a connection request and create a connection with a periodic advertiser.

- Reference

[18] 9.5.5.2

- Initial Condition
- -The IUT is in Link Layer state 'Standby'.
- Test Procedure
1. The Lower Tester enters Periodic Advertising mode and begins transmitting Periodic Advertising events with Periodic Advertising Response Timing Information.
2. The Upper Tester orders the IUT to synchronize with Periodic Advertising events.
3. The Lower Tester synchronizes and receives periodic advertising events.
4. The Lower Tester sends a connection request to the IUT.
5. The IUT accepts the connection request to the Lower Tester.
6. The IUT sends a successful connection request event to the Upper Tester.
7. The IUT and the Lower Tester complete a Link Layer connection.
- Expected Outcome

Figure 4.197: Create connection with synchronized device using the Periodic Advertising Connection procedure, Scanner MSC

## Pass verdict

In Step 7, the IUT has a Link Layer connection with the Lower Tester.

## 4.7.9 Broadcast Isochronous Streaming modes and procedures

## 4.7.9.1 Broadcast Isochronous Synchronization Establishment

## GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment procedure]

- Test Purpose

Verify that the IUT performs the Broadcast Isochronous Synchronization Establishment procedure.

- Reference

[15] 9.6, 9.6.3

- Initial Condition
- -The IUT is in Link Layer state 'Standby' .
- -The Lower Tester is in Broadcasting State.
- Test Procedure
1. The Lower Tester establishes a BIG with a single BIS and begins sending periodic advertising trains with BIGInfo in the ACAD field of AUX\_SYNC\_IND PDU.
2. The Upper Tester orders the IUT to synchronize to the Lower Tester's BIG.
3. The IUT synchronizes to the BIG.
4. The Upper Tester enables ISO data.
5. The Upper Tester expects the IUT to begin providing isochronous data from the single BIS from the Lower Tester.
- Expected Outcome

Figure 4.198: GAP/BIS/BSE/BV-01-C [Broadcast Isochronous Synchronization Establishment] MSC

## Pass verdict

The IUT synchronizes with the Lower Tester.

The Upper Tester receives the Broadcast Isochronous Stream data sent by the Lower Tester.

## 4.7.9.2 Broadcast Isochronous Broadcasting mode

## GAP/BIS/BBM/BV-01-C [Broadcast Isochronous Stream Broadcasting mode]

- Test Purpose

Verify the IUT in Broadcast Isochronous Stream Broadcasting mode; the peer device synchronizes and listens for isochronous data payloads.

- Reference

[15] 9.6.2

- Initial Condition
- -The IUT is in Broadcasting State.
- -The Lower Tester is in Synchronization State.
- Test Procedure
1. The Upper Tester instructs the IUT to create a BIG.
2. The Lower Tester receives periodic advertising packets from the IUT containing BIGInfo.
3. The Upper Tester enables ISO data on the IUT.
4. The Upper Tester begins sending data to the IUT.
5. The Lower Tester receives BIS Data Packets from the IUT.
- Expected Outcome

Figure 4.199: GAP/BIS/BBM/BV-01-C [Broadcast Isochronous Stream Broadcasting mode] MSC

## Pass verdict

The IUT sends isochronous data payloads in Broadcast Isochronous Stream subevents.

## 4.7.10 Connection Subrating procedure

## 4.7.10.1 Connection Subrate Request procedure

## GAP/CSUB/CSR/BV-01-C [Connection Subrate Request procedure]

- Test Purpose

Verify that the IUT as a Peripheral performs a subrate request and returns the LE Subrate Change event to the Upper Tester.

- Reference

[17] 9.3.16

- Initial Condition
- -The IUT is a Peripheral and in Link Layer state 'Connected'.
- Test Procedure
1. The Upper Tester orders the IUT to perform the LE Subrate Request procedure.
2. The IUT and the Lower Tester exchange connection subrate messages.
3. The IUT sends an LE Subrate Change event to the Upper Tester.
- Expected Outcome

Figure 4.200: GAP/CSUB/CSR/BV-01-C [Connection Subrate Request procedure] MSC

## Pass verdict

The IUT sends an LE Subrate Change event to the Upper Tester.

## 4.7.10.2 Connection Subrate Update procedure

## GAP/CSUB/CSU/BV-01-C [Connection Subrate Update procedure]

- Test Purpose

Verify that the IUT as a Central performs a subrate update procedure and returns the Subrate Update event to the Upper Tester.

- Reference

[17] 9.3.16

- Initial Condition
- -The IUT is a Central and in Link Layer state 'Connected'.
- Test Procedure
1. The Upper Tester orders the IUT to perform the LE Subrate Update procedure.
2. The IUT sends a connection subrate indication to the Lower Tester.
3. The IUT sends an LE Subrate Update event to the Upper Tester.
- Expected Outcome

Figure 4.201: GAP/CSUB/CSU/BV-01-C [Connection Subrate Update procedure] MSC

## Pass verdict

The IUT sends an LE Subrate Update event to the Upper Tester.

## 4.7.11

## Channel Sounding procedure

## GAP/CS/BV-01-C [Starting Channel Sounding, Initiator]

- Test Purpose

Verify that the Initiator IUT starts Channel Sounding using the Channel Sounding Start procedure.

- Reference

[19] 9.7.1

- Initial Condition
- -The Lower Tester has the Channel Sounding feature bit set.
- -The Lower Tester and the IUT have completed the encryption procedure with the LE security mode 1 level 2 or higher.

- Test Procedure
1. The Upper Tester orders the IUT to perform the LE Channel Sounding Start procedure.
2. The IUT and the Lower Tester exchange Channel Sounding messages.
3. The IUT sends an LE Channel Sounding event to the Upper Tester.
- Expected Outcome

Figure 4.202: Starting Channel Sounding, Initiator MSC

## Pass verdict

The IUT is able to start the Channel Sounding procedure using the Channel Sounding Start procedure.

## GAP/CS/BV-02-C [Starting Channel Sounding, Reflector]

- Test Purpose

Verify that the Reflector IUT starts Channel Sounding using the Channel Sounding Start procedure.

- Reference

[19] 9.7.2

- Initial Condition
- -The Lower Tester has the Channel Sounding feature bit set.
- -The Lower Tester and the IUT have completed the encryption procedure with the LE security mode 1 level 2 or higher.
- Test Procedure

Figure 4.203: Starting Channel Sounding, Initiator MSC

1. The Lower Tester orders the IUT to perform the LE Channel Sounding Start procedure.
2. The IUT and the Lower Tester exchange Channel Sounding messages.
3. The IUT sends an LE Channel Sounding event to the Upper Tester.
- Expected Outcome

## Pass verdict

The IUT is able to be configured in the Channel Sounding Reflector role and exchange Channel events.

## 4.8 BR/EDR/LE operational modes and procedures

Verify the correct implementation of the BR/EDR/LE devices (devices that support LE and BR/EDR together).

## 4.8.1 Non-connectable mode

## GAP/DM/NCON/BV-01-C [BR/EDR/LE non-connectable mode]

- Test Purpose

Verify that the IUT can properly handle the non-connectable mode in both BR/EDR and LE physical channels.

This test case is only valid for a BR/EDR/LE device that supports the Peripheral role.

- Reference

[4] 13.1.2.1

- Initial Condition
- -The IUT is in Link Layer Standby state.
- Test Procedure
1. The Upper Tester orders the IUT to enter non-connectable mode.
2. For BR/EDR, this means paging scan is disabled on the IUT.
3. The Lower Tester verifies that the device is non-connectable in BR/EDR using the BR/EDR connection procedure.
4. The Lower Tester verifies that the device is non-connectable in LE using GAP/CONN/NCON/BV01-C [Non-Connectable mode] to GAP/CONN/NCON/BV-03-C [Non-Connectable mode, Limited Discoverable mode] depending on the IUT capability.

Figure 4.204: GAP/DM/NCON/BV-01-C [BR/EDR/LE non-connectable mode] MSC

- Expected Outcome

## Pass verdict

The IUT passes correspondent non-connectable mode test cases for LE and BR/EDR.

## 4.8.2 Connectable mode

## GAP/DM/CON/BV-01-C [BR/EDR/LE connectable mode]

- Test Purpose

Verify that the IUT can properly handle the connectable mode in both BR/EDR.

- Reference

[4] 13.1.2.2

- Initial Condition
- -The IUT is in Link Layer Standby state.
- Test Procedure
1. The Upper Tester orders the IUT to enter connectable mode.
2. For BR/EDR, this means page scan is enabled.
3. The Lower Tester verifies that the IUT can be connected in BR/EDR using the corresponding connection procedure.
4. For this test case, the IUT only has to complete the corresponding test case for connectable mode as a BR/EDR device.

Figure 4.205: GAP/DM/CON/BV-01-C [BR/EDR/LE connectable mode] MSC

- Expected Outcome

## Pass verdict

The Lower Tester finds the IUT is connectable using the BR/EDR procedure.

## 4.8.3 Non-bondable mode

## GAP/DM/NBON/BV-01-C [BR/EDR/LE non-bondable mode]

- Test Purpose

Verify that the IUT is non-bondable in both BR/EDR and LE.

The Lower Tester is a BR/EDR/LE Peripheral device.

The IUT is a BR/EDR/LE Central Device.

- Reference

[4] 13.1.3.2

- Initial Condition
- -The IUT is in Link Layer Standby state.
- Test Procedure
1. The Upper Tester orders the IUT to enter non-bondable mode.
2. The Lower Tester verifies that the device is non-bondable in BR/EDR with the corresponding test case procedure GAP/MOD/NBON/BV-02-C [Non-bondable mode, IUT rejects pairing procedure].
3. The Lower Tester and the IUT are disconnected.

4. The Lower Tester advertises itself as LEonly, Peripheral role for the LE 'non -bondable' testing part that follows.
2. 5.
3. The Lower Tester verifies that the device is non-bondable mode in LE using

GAP/BOND/NBON/BV-01-C [Non-bondable mode -Central as Responder] followed by GAP/BOND/NBON/BV-02-C [Non-bondable mode -Central as Initiator].

Figure 4.206: GAP/DM/NBON/BV-01-C [BR/EDR/LE non-bondable mode] MSC

- Expected Outcome

## Pass verdict

The Lower Tester verifies that the IUT supports non-bondable mode correctly for both BR/EDR and LE procedures.

## 4.8.4 Bondable mode

## GAP/DM/BON/BV-01-C [BR/EDR/LE bondable mode]

- Test Purpose

Verify that the IUT can properly handle the bonding procedure in both BR/EDR and LE as Central role.

- Reference

[4] 13.1.5

- Initial Condition
- -The IUT is in Link Layer Standby state.

- Test Procedure
1. The Upper Tester orders the IUT to enter bondable mode.
2. The Lower Tester verifies that the device is bondable in BR/EDR using the corresponding test case procedure.
3. The Lower Tester has to advertise itself as LEonly, Peripheral role for the LE 'bondable' testing part.
4. The Lower Tester verifies that the device is bondable in LE using corresponding test case procedures in GAP/BOND/BON/ test group.
- Expected Outcome

Figure 4.207: GAP/DM/BON/BV-01-C [BR/EDR/LE bondable mode] MSC

## Pass verdict

The Lower Tester finds the IUT is bondable using both BR/EDR and LE procedures.

## 4.8.5 General Discovery procedure

## GAP/DM/GIN/BV-01-C [BR/EDR/LE General Discovery -Finding General Discoverable devices]

- Test Purpose

Verify that the IUT performing the General Discovery procedure can discover a BR/EDR/LE device in the General Discovery mode over both BR/EDR and LE.

Verify that the IUT performing the General Discovery procedure can discover a BR/EDR/LE device in the Limited Discovery mode over both BR/EDR and LE.

The IUT is a BR/EDR/LE device as the Central and initiator over BR/EDR and in the Central role over LE.

The Lower Tester is a BR/EDR/LE device operating as the Peripheral and acceptor over BR/EDR and in the Peripheral role over LE.

- Reference

[4] 13.2.1

- Initial Condition
- -The IUT is in Link Layer Standby state.
- Test Procedure
1. The Lower Tester enters General Discoverable mode; the Lower Tester interleaves General Discoverable mode over BR/EDR and LE.
2. The Upper Tester orders the IUT to perform the General Discovery procedure; the IUT verifies that it can discover the Lower Tester over both BR/EDR and LE.
3. The Lower Tester enters Limited Discoverable mode; the Lower Tester interleaves Limited Discoverable mode over BR/EDR and LE.
4. The Upper Tester orders IUT to perform the General Discovery procedure; the IUT verifies that it can discover the Lower Tester over both BR/EDR and LE.

Figure 4.208: GAP/DM/GIN/BV-01-C [BR/EDR/LE General Discovery -Finding General Discoverable Devices] MSC

- Expected Outcome

## Pass verdict

The IUT discovers the Lower Tester when the Lower Tester is operating in General Discoverable mode and the IUT is performing the General Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 0 and the General Discoverable flag set to 1.

The IUT discovers the Lower Tester when the Lower Tester is operating in Limited Discoverable mode and the IUT is performing the General Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 1 and the General Discoverable flag set to 0.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify that the Flags AD type presence and setting according to the test pass verdict in any received advertising data.

## 4.8.6 Limited Discovery procedure

## GAP/DM/LIN/BV-01-C [BR/EDR/LE Limited Discovery -Find Limited Discoverable devices]

- Test Purpose

Verify that the IUT performing the Limited Discovery procedure can discover a BR/EDR/LE device in the Limited Discoverable mode over both BR/EDR and LE.

Verify that the IUT performing the Limited Discovery procedure does not discover a BR/EDR/LE device in the General Discoverable mode over both BR/EDR and LE.

The IUT is a BR/EDR/LE device performing the Limited Discovery procedure as the Central and initiator over BR/EDR and in the Central role over LE.

The Lower Tester is a BR/EDR/LE device operating as the Peripheral and acceptor over BR/EDR and in the Peripheral role over LE.

- Reference

[4] 13.2.2

- Initial Condition
- -The IUT is in Link Layer Standby state.
- Test Procedure
1. The Lower Tester enters Limited Discoverable mode; the Lower Tester interleaves Limited Discoverable mode over BR/EDR and LE.
2. The Upper Tester orders the IUT to perform the Limited Discovery procedure; the IUT verifies that it can discover the Lower Tester over both BR/EDR and LE.
3. The Lower Tester enters General Discoverable mode; the Lower Tester interleaves General Discoverable mode over BR/EDR and LE.
4. The Upper Tester orders the IUT to perform the Limited Discovery procedure; the IUT verifies that it does not discover the Lower Tester over both BR/EDR and LE.

Figure 4.209: GAP/DM/LIN/BV-01-C [BR/EDR/LE Limited Discovery -Find Limited Discoverable Devices] MSC

- Expected Outcome

## Pass verdict

The IUT discovers the Lower Tester when the Lower Tester is operating in Limited Discoverable mode and the IUT is performing the Limited Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 1 and the General Discoverable flag set to 0.

The IUT does not discover the Lower Tester when the Lower Tester is operating in General Discoverable mode and the IUT is performing the Limited Discovery procedure over BR/EDR and LE; the advertising data received from the Lower Tester includes the Flags AD type with the Limited Discoverable flag set to 0 and the General Discoverable flag set to 1.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## 4.8.7 Name Discovery procedure

## GAP/DM/NAD/BV-01-C [BR/EDR/LE Name Discovery]

- Test Purpose

Verify that the IUT can properly perform the name discovery procedure for both BR/EDR and LE devices as a Central role.

The IUT is a BR/EDR/LE device.

The Lower Tester is a BR/EDR/LE device.

- Reference

[4] 6.3, 13.2.4

- Initial Condition
- -The IUT is in Link Layer 'Standby' state.
- Test Procedure
1. The Lower Tester is a BR/EDR/LE device.
2. The Upper Tester orders the IUT to do Name Discovery of Lower Tester on BR/EDR link as defined in Section 6.3 of [4] , which is the BR/EDR standard procedure of HCI command 'remote name request' .
- Expected Outcome

Figure 4.210: GAP/DM/NAD/BV-01-C [BR/EDR/LE Name Discovery] MSC

## Pass verdict

Device name is discovered correctly and passed up to the Upper Tester for verification.

- Notes

The IUT first performs the Device Capability Discovery procedure.

## GAP/DM/NAD/BV-02-C [LE Name Discovery]

- Test Purpose

Verify that the IUT can properly perform the name discovery procedure for LE devices.

The IUT is a BR/EDR/LE device.

The Lower Tester is an LE-only Peripheral device.

- Reference

## 4 9.2.7

- Initial Condition
- -The IUT is in Link Layer 'Standby' state.

- Test Procedure

The Upper Tester orders the IUT to do a Name Discovery of the Lower Tester on LE link as defined in Section 9.2.7 of [4] , which could be through the GATT profile to access GAP characteristics of 'device name.'

Figure 4.211: GAP/DM/NAD/BV-02-C [LE Name Discovery] MSC

- Expected Outcome

## Pass verdict

Device name is discovered correctly and passed up to the Upper Tester for verification.

## 4.8.8 Link Establishment procedure GAP/DM/LEP/BV-01-C [BR/EDR/LE and BR/EDR/LE Link Establishment -BR/EDR Transport]

- Test Purpose

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the BR/EDR Transport.

The IUT is a BR/EDR/LE Peripheral device.

The Lower Tester is a BR/EDR/LE Central device.

- Reference

[9] 13.1, 13.3.1

- Initial Condition
- -The IUT is in Link Layer 'Standby' state.
- Test Procedure
1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode; the IUT is a BR/EDR/LE Peripheral device.
2. The Lower Tester performs the General Discovery procedure to discover the IUT; the Lower Tester is a BR/EDR/LE Central device.
3. The Lower Tester performs the Link Establishment procedure to connect to the IUT.
4. When connected the Lower Tester or the IUT terminates the connection.

Figure 4.212: GAP/DM/LEP/BV-01-C [BR/EDR/LE and BR/EDR/LE Link Establishment -BR/EDR Transport] MSC

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

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DM/LEP/BV-06-C [BR/EDR/LE and LE Link Establishment IUT is BR/EDR/LE]

- Test Purpose

Verify IUT compliance to the Link Establishment procedure to connect with an LE-only device.

The IUT is a BR/EDR/LE* device.

The Lower Tester is an LE-only* device.

*LE GAP role is defined as required in the test procedure.

- Reference

[9] 13.1, 13.3.1

- Initial Condition
- -The IUT is in Link Layer 'Standby' state.
- Test Procedure
1. The Lower Tester enters General Discoverable mode and Undirected Connectable mode over LE; the Lower Tester is a LE-Only Peripheral device.
2. The Upper Tester orders the IUT to perform the General Discovery procedure to discover the Lower Tester; the IUT is a BR/EDR/LE Central device.
3. The Upper Tester orders the IUT to perform the Connection Establishment procedure to connect to the Lower Tester.
4. When connected the Lower Tester or the IUT terminates the connection.
- Expected Outcome

Figure 4.213: GAP/DM/LEP/BV-06-C [BR/EDR/LE and LE Link Establishment IUT is BR/EDR/LE] MSC

## Pass verdict

The IUT receives either connectable and scannable undirected advertising events or connectable undirected advertising events from Lower Tester during the period that the Lower Tester is in General Discoverable mode and Undirected Connectable mode.

In each advertising event received, the advertiser address is set to the address of the Lower Tester. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 1. The Flags AD type is not present in any scan response data received.

The IUT establishes a connection with the Lower Tester using the received advertiser address.

The Lower Tester or the IUT successfully terminates the connection.

## GAP/DM/LEP/BV-07-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral -LE Transport]

- Test Purpose

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the LE transport.

Both the IUT and the Lower Tester are BR/EDR/LE devices.

- Reference

[9] 13.1

- Initial Condition
- -The IUT is in Link Layer 'Standby' state.
- Test Procedure
1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode on the LE transport; the IUT is a BR/EDR/LE Peripheral device.
2. The Lower Tester performs the General Discovery procedure on the LE transport to discover the IUT; the Lower Tester is a BR/EDR/LE Central device.
3. The Lower Tester performs the Link Establishment procedure on the LE transport to connect to the IUT.
4. The Lower Tester or the IUT terminates the connection.
- Expected Outcome

Figure 4.214: GAP/DM/LEP/BV-07-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral -LE Transport] MSC

## Pass verdict

The Lower Tester discovers the IUT over BR.

The Lower Tester verifies that the LE Supported (Controller) bit is set to 1 and the LE Supported (Host) bit is set to 1 in the LMP features.

The Lower Tester discovers the IUT over LE.

The Lower Tester receives either connectable and scannable undirected advertising events or connectable undirected advertising events from the IUT during the period that the IUT is in General Discoverable mode and connectable mode.

In each advertising event received, the advertiser address is set to the address of the IUT. The Flags AD type is present only once in the advertising data, the General Discoverable flag is set to 1, the Limited Discoverable flag is set to 0, and the BR/EDR Not Supported flag is set to 0. The Flags AD type is not present in any scan response data received.

The Lower Tester establishes an LE connection with the IUT using the received LE address.

The Lower Tester or the IUT successfully terminates the connection.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DM/LEP/BV-08-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Peripheral -LE and BR/EDR Transports]

- Test Purpose

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the BR/EDR and LE transports simultaneously.

Both the IUT and the Lower Tester are BR/EDR/LE* devices.

- Reference

[9] 13.1.1

- Initial Condition
- -The IUT is in Link Layer 'Standby' state.
- -The Lower Tester is using the same address on the LE and BR/EDR transports.
- Test Procedure
1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode on both the LE and BR/EDR transports; the IUT is a BR/EDR/LE Peripheral device.
2. The Lower Tester performs the General Discovery procedure on both the LE and BR/EDR transports to discover the IUT; the Lower Tester is a BR/EDR/LE Central device.
3. The Lower Tester performs the Link Establishment procedure to connect to the IUT on both the LE and BR/EDR transports.
4. When connected on both transports the Lower Tester or the IUT terminates the connections.

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific.

Figure 4.215: GAP/DM/LEP/BV-08-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Peripheral -LE and BR/EDR Transports] MSC

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

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DM/LEP/BV-09-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Central -LE and BR/EDR Transports]

- Test Purpose

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device on the BR/EDR and LE transports simultaneously.

Both the IUT and the Lower Tester are BR/EDR/LE devices.

- Reference

[9] 13.1.1

- Initial Condition
- -The IUT is in Link Layer 'Standby' state .
- -The Lower Tester is using the same address on the LE and BR/EDR transports.
- Test Procedure
1. The Lower Tester enters General Discoverable mode and connectable mode on both the LE and BR/EDR transports; the Lower Tester is a BR/EDR/LE Peripheral device.
2. The Upper Tester orders the IUT to perform the General Discovery procedure on both the LE and BR/EDR transports to discover the Lower Tester; the IUT is a BR/EDR/LE Central device.
3. The Upper Tester orders the IUT to perform the Link Establishment procedure to connect to the Lower Tester on both the LE and BR/EDR transports.
4. When connected on both transports the Lower Tester or the IUT terminates the connections.

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific.

Figure 4.216: GAP/DM/LEP/BV-09-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Central -LE and BR/EDR Transports] MSC

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

## GAP/DM/LEP/BV-10-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Central -LE and BR/EDR Transports]

- Test Purpose

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device using the BR/EDR and LE transports simultaneously.

The IUT is a BR/EDR/LE device.

The Lower Tester is a BR/EDR/LE device.

- Reference

[9] 13.1.1

- Initial Condition
- -The IUT is in Link Layer 'Standby' state.
- -The Lower Tester is using the same address on the LE and BR/EDR transports.
- Test Procedure
1. The Upper Tester orders the IUT to enter General Discoverable mode and connectable mode on the LE transport. The Upper Tester orders the IUT to perform the General Discovery procedure on the BR/EDR transport. The IUT is a BR/EDR/LE Peripheral device.
2. The Lower Tester performs the General Discovery procedure on the LE transport to discover the IUT and enters the General Discoverable mode on the BR/EDR transport. The Lower Tester is a BR/EDR/LE Central device.
3. The Lower Tester performs the Link Establishment procedure on the LE transport to connect to the IUT.
4. The Upper Tester orders the IUT to perform the Link Establishment procedure on the BR/EDR transport to connect to the Lower Tester.
5. When connected on both transports the Lower Tester or the IUT terminates the connections.

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific.

Figure 4.217: GAP/DM/LEP/BV-10-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Peripheral/BR Central -LE and BR/EDR Transports] MSC

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

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific.

- Notes

'Discover' in the context of the test text means to report to the application layer and/or verify the Flags AD type presence and setting according to the test Pass verdict in any received advertising data.

## GAP/DM/LEP/BV-11-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Peripheral -LE and BR/EDR Transports]

- Test Purpose

Verify IUT compliance to the Link Establishment procedure to connect with a BR/EDR/LE device on the BR/EDR and LE transports simultaneously.

Both the IUT and the Lower Tester are BR/EDR/LE devices.

- Reference

[9] 13.1.1

- Initial Condition
- -The IUT is in Link Layer 'Standby' state .
- -The Lower Tester is using the same address on the LE and BR/EDR transports.
- Test Procedure
1. The Lower Tester enters General Discoverable mode and connectable mode on the LE transport. The Lower Tester performs the General Discovery procedure on the BR/EDR transport. The Lower Tester is a BR/EDR/LE Peripheral device.
2. The Upper Tester orders the IUT to perform the General Discovery procedure on the LE physical transport to discover the Lower Tester and enters the General Discoverable mode on the BR/EDR transport. The IUT is a BR/EDR/LE Central device.
3. The Upper Tester orders the IUT to perform the Link Establishment procedure on the LE physical transport to connect to the Lower Tester.
4. The Lower Tester performs the Link Establishment procedure on the BR/EDR transport to connect to the IUT.
5. The Lower Tester or the IUT terminates the connection.

Note: The order used for the discovery sequence and connection establishment sequence is implementation specific.

Figure 4.218: GAP/DM/LEP/BV-11-C [BR/EDR/LE and BR/EDR/LE Link Establishment IUT is Central/BR Peripheral -LE and BR/EDR Transports] MSC

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

## GAP/DM/LEP/BV-12-C [Generate BR/EDR Link Key from LE LTK, as Initiator]

- Test Purpose

Verify that the LTK generated on the LE transport as an initiator can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device when BR/EDR Secure Connections is supported by both devices. The IUT is the Central device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester.
- Test Procedure
1. The IUT initiates LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase two (pairing).
2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation.
3. The IUT terminates the LE connection.
4. The IUT performs the BR/EDR Link Establishment procedure and encrypts the link using the derived BR/EDR Link Key.

Figure 4.219: GAP/DM/LEP/BV-12-C [Generate BR/EDR Link Key from LE LTK, as Initiator] MSC

- Expected Outcome

## Pass verdict

LE Secure Connections Pairing is complete, with an LE encrypted link, and BR/EDR Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport.

- Notes

This test procedure requires Secure Connections pairing to occur first on the LE transport.

## GAP/DM/LEP/BV-13-C [Upgrade of BR/EDR Link Key Regenerates LTK]

- Test Purpose

Verify that after cross-transport key derivation, upgrading the BR/EDR Link Key causes the LTK to be regenerated. The IUT is the Central device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester.

## · Test Procedure

1. The IUT initiates unauthenticated LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase two (pairing).
2. The state of Link Key bit in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation.
3. The IUT terminates the LE connection.
4. The IUT performs the BR/EDR Link Establishment procedure and encrypts the link using the derived BR/EDR Link Key.
5. The IUT upgrades the security level of the BR/EDR Link Key from unauthenticated to authenticated.
6. The IUT performs SMP over BR/EDR.
7. The IUT terminates the BR/EDR connection.
8. The IUT creates an LE connection with the Lower Tester and encrypts the link using the LTK derived from the authenticated BR/EDR Link Key.

Figure 4.220: GAP/DM/LEP/BV-13-C [Upgrade of BR/EDR Link Key Regenerates LTK] MSC

- Expected Outcome

## Pass verdict

LE Secure Connections Pairing is complete, with an LE encrypted link, and BR/EDR Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport. The BR/EDR Link Key can be upgraded from unauthenticated to authenticated. The LE link can be encrypted using the LTK derived from the authenticated BR/EDR Link Key.

## GAP/DM/LEP/BV-14-C [Generate BR/EDR Link Key from LE LTK, as Responder]

- Test Purpose

Verify that the LTK generated on the LE transport as a responder can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device, on a device that supports BR/EDR Secure Connections. The IUT is the Peripheral device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has been discovered and is connected to by the Lower Tester.
- Test Procedure
1. The Lower Tester initiates LE Secure Connections Pairing with the IUT. They complete Pairing phase one (negotiation) and phase 2 (pairing).
2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation.
3. The Lower Tester terminates the LE connection.
4. The Upper Tester puts the IUT in connectable mode on the BR/EDR transport.
5. The Lower Tester establishes a BR/EDR link with the IUT and encrypts the link with the derived BR/EDR Link Key.

Figure 4.221: GAP/DM/LEP/BV-14-C [Generate BR/EDR Link Key from LE LTK, as Responder] MSC

- Expected Outcome

## Pass verdict

LE Secure Connections Pairing is complete, with an LE encrypted link, and Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport.

## GAP/DM/LEP/BV-15-C [Generate BR/EDR Link Key from LE LTK, as Initiator]

- Test Purpose

Verify that the LTK generated on the LE transport as an initiator can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device which supports BR/EDR Secure Simple Pairing but not BR/EDR Secure Connections. The IUT is the Central device.

- Reference

## 9 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with LE Secure Connections capabilities but only Secure Simple Pairing for BR/EDR. The IUT has discovered and connected to the Lower Tester.

- Test Procedure
1. The IUT initiates LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase 2 (pairing).
2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation.
3. The IUT terminates the LE connection.
4. The IUT performs the BR/EDR Link Establishment procedure and encrypts the link using the derived BR/EDR Link Key.
- Expected Outcome

Figure 4.222: GAP/DM/LEP/BV-15-C [Generate BR/EDR Link Key from LE LTK, as Initiator] MSC

## Pass verdict

LE Secure Connections Pairing is complete, with an LE encrypted link, and Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport.

## GAP/DM/LEP/BV-16-C [Generate BR/EDR Link Key from LE LTK, as Responder]

- Test Purpose

Verify that the LTK generated on the LE transport as a responder can be used to generate the Link Key for the BR/EDR transport in a BR/EDR/LE device which supports BR/EDR Secure Simple Pairing but not BR/EDR Secure Connections. The IUT is the Peripheral device.

- Reference

## 9 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with LE Secure Connections capabilities but only Secure Simple Pairing for BR/EDR. The IUT has been discovered and is connected to by the Lower Tester.
- Test Procedure
1. The Lower Tester initiates LE Secure Connections Pairing with the IUT. They complete Pairing phase one (negotiation) and phase 2 (pairing).
2. The state of Link Key bits in the Key Distribution/Generation Fields tells the devices to continue with BR/EDR Link Key derivation.
3. The Lower Tester terminates the LE connection.
4. The Upper Tester puts the IUT in connectable mode on the BR/EDR transport.
5. The Lower Tester establishes a BR/EDR link with the IUT and encrypts the link with the derived BR/EDR Link Key.

Figure 4.223: GAP/DM/LEP/BV-16-C [Generate BR/EDR Link Key from LE LTK, as Responder] MSC

- Expected Outcome

## Pass verdict

LE Secure Connections Pairing is complete, with an LE encrypted link, and Link Key of identical strength as the LTK has been derived and can be used to encrypt the BR/EDR link. The IUT does not initiate pairing on the BR/EDR transport.

## GAP/DM/LEP/BV-17-C [Generate LE LTK from BR/EDR Link Key, as Initiator]

- Test Purpose

Verify that the Link Key generated on the BR/EDR transport as an initiator can be used to generate the LTK for the LE transport in a BR/EDR/LE device. The IUT is the Central device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester.
- Test Procedure
1. The IUT initiates BR/EDR Secure Connections Pairing with the Lower Tester. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link.
2. The IUT then sends an SMP Pairing Request to the Lower Tester on the encrypted BR/EDR link. The Lower Tester replies with an SMP Pairing Response. The two devices derive the LTK, and optionally generate and distribute additional keys.
3. The IUT terminates the BR/EDR connection.
4. The IUT connects to the Lower Tester on the LE transport and encrypts the link with the derived LTK.

Figure 4.224: GAP/DM/LEP/BV-17-C [Generate LE LTK from BR/EDR Link Key, as Initiator] MSC

- Expected Outcome

## Pass verdict

BR/EDR Secure Connections Pairing is complete, with a BR/EDR encrypted link, the LE LTK of identical strength as the BR/EDR Link Key has been derived, other keys such as the IRK and CSRK have been optionally distributed. The LE LTK can be used to encrypt the LE connection. The IUT does not initiate pairing on the LE transport.

## GAP/DM/LEP/BV-18-C [Upgrade of LTK Regenerates BR/EDR Link Key]

- Test Purpose

Verify that after cross-transport key derivation, upgrading the LTK causes the BR/EDR Link Key to be regenerated. The IUT is the Central device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester.
- Test Procedure
1. The IUT initiates unauthenticated BR/EDR Secure Connections Pairing with the Lower Tester. They complete Pairing phases for public key exchange, authentication, key generation and encryption of the BR/EDR link.
2. The IUT then sends an SMP Pairing Request to the Lower Tester on the encrypted BR/EDR link. The Lower Tester replies with an SMP Pairing Response. The two devices derive the LTK, and optionally generate and distribute additional keys.
3. The IUT terminates the BR/EDR connection.
4. The IUT connects to the Lower Tester on the LE transport and encrypts the link with the derived LTK.
5. The IUT upgrades the security level of the LTK from unauthenticated to authenticated.
6. The IUT terminates the LE connection.
7. The IUT creates BR/EDR connection with the Lower Tester and encrypts the link using the BR/EDR Link Key derived from the authenticated LTK.

Figure 4.225: GAP/DM/LEP/BV-18-C [Upgrade of LTK Regenerates BR/EDR Link Key] MSC

- Expected Outcome

## Pass verdict

BR/EDR Secure Connections Pairing is complete, with a BR/EDR encrypted link, the LE LTK of identical strength as the BR/EDR Link Key has been derived, other keys such as the IRK and CSRK have been optionally distributed. The LE LTK can be used to encrypt the LE connection. The IUT does not initiate pairing on the LE transport. The LTK can be upgraded from unauthenticated to authenticated. The BR/EDR link can be encrypted using the Link Key derived from the authenticated LTK.

## GAP/DM/LEP/BV-19-C [Generate LE LTK from BR/EDR Link Key, as Responder]

- Test Purpose

Verify that the Link Key generated on the BR/EDR transport as a responder can be used to generate the LTK for the LE transport in a BR/EDR/LE device. The IUT is the Peripheral device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester has discovered and connected with the IUT over BR/EDR.
- Test Procedure
1. The Lower Tester initiates BR/EDR Secure Connections Pairing with the IUT. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link.
2. The Lower Tester then sends an SMP Pairing Request on the encrypted BR/EDR link. The IUT replies with an SMP Pairing Response. The two devices derive the LTKand optionally generate and distribute other keys.
3. The Lower Tester terminates the BR/EDR connection.
4. The Upper Tester puts the IUT in connectable mode on the LE transport.
5. The Lower Tester establishes an LE link with the IUT and encrypts the link with the derived LE LTK.

Figure 4.226: GAP/DM/LEP/BV-19-C [Generate LE LTK from BR/EDR Link Key, as Responder] MSC

- Expected Outcome

## Pass verdict

BR/EDR Secure Connections Pairing is complete, with a BR/EDR encrypted link, the LE LTK of identical strength as the BR/EDR Link Key has been derived, other keys such as the IRK and CSRK have been optionally distributed. The LE LTK can be used to encrypt the LE connection. The IUT does not initiate pairing on the LE transport.

## GAP/DM/LEP/BI-01-C [Do Not Generate LE LTK from BR/EDR P-192 Link Key, as Initiator]

- Test Purpose

Verify that the P-192 Link Key generated on the BR/EDR transport as an initiator is not used to generate the LTK for the LE transport in a BR/EDR/LE device when either the IUT or the Lower Tester or both do not support BR/EDR Secure Connections. The IUT is the Central device.

- Reference

[9] 2.3.5.7, 2.4.2.5.

- Initial Condition
- -The IUT supports LE Secure Connections and may or may not support BR/EDR Secure Connections. The Lower Tester supports LE Secure Connections but not BR/EDR Secure Connections. The IUT has discovered and connected to the Lower Tester.
- Test Procedure
1. The IUT initiates BR/EDR Secure Simple Pairing with the Lower Tester. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link.
2. The IUT terminates the BR/EDR connection.
3. The IUT connects to the Lower Tester on the LE transport.
4. The IUT initiates LE Secure Connections Pairing with the Lower Tester. They complete Pairing phase one (negotiation) and phase 2 (pairing).

Figure 4.227: GAP/DM/LEP/BI-01-C [Do Not Generate LE LTK from BR/EDR P-192 Link Key, as Initiator] MSC

- Expected Outcome

## Pass verdict

BR/EDR Secure Simple Pairing is complete, with a BR/EDR encrypted link.

The IUT does not initiate LE Secure Connections Pairing on the BR/EDR transport.

The IUT and the Lower Tester successfully complete LE Secure Connections Pairing on the LE transport.

## GAP/DM/LEP/BI-02-C [Do Not Generate LE LTK from P-192 BR/EDR Link Key, as Responder]

- Test Purpose

Verify that the P-192 Link Key generated on the BR/EDR transport as a responder is not used to generate the LTK for the LE transport in a BR/EDR/LE device. The IUT is the Peripheral device.

- Reference

[9] 2.3.5.7, 2.4.2.5; optional: 2.4.2.1

- Initial Condition
- -The IUT supports LE Secure Connections. The IUT may or may not support BR/EDR Secure Connections. The Lower Tester support LE Secure Connections but not BR/EDR Secure Connections. The Lower Tester has discovered and connected with the IUT over BR/EDR.
- Test Procedure
1. The Lower Tester initiates BR/EDR Secure Simple Pairing with the IUT. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link.
2. The Lower Tester then sends an SMP Pairing Request on the encrypted BR/EDR link. The IUT responds with an SMP Pairing Failed with reason code 'Cross Transport Key Derivation/Generation not allowed' (0x0E).
3. The Lower Tester terminates the BR/EDR connection.
4. The Upper Tester puts the IUT in connectable mode on the LE transport.
5. The Lower Tester connects to the IUT on the LE transport.
6. The Lower Tester initiates LE Secure Connections Pairing with the IUT. They complete Pairing phase one (negotiation) and phase 2 (pairing).

Figure 4.228: GAP/DM/LEP/BI-02-C [Do Not Generate LE LTK from P-192 BR/EDR Link Key, as Responder] MSC

- Expected Outcome

## Pass verdict

BR/EDR Secure Simple Pairing is complete, with a BR/EDR encrypted link.

The IUT rejects the Lower Tester's request LE Secure Connections Pairing on the BR/EDR transport.

The IUT and the Lower Tester successfully complete LE Secure Connections Pairing on the LE transport.

## GAP/DM/LEP/BV-20-C [Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Initiator]

- Test Purpose

Verify that an LE LTK is not overwritten by the LE LTK generated via the cross-transport key derivation procedure using a weaker BR/EDR Link Key. The IUT is the Central device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has been discovered and is connected to the Lower Tester over LE.
- Test Procedure

Figure 4.229: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Initiator MSC -Page 1 of 2

Figure 4.230: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Initiator MSC -Page 2 of 2

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

## · Expected Outcome

## Pass verdict

The IUT reconnects to the Lower Tester over LE using the existing LE keys exchanged and stored in Step 4.

## GAP/DM/LEP/BV-21-C [Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Responder]

- Test Purpose

Verify that an LE LTK is not overwritten by the LE LTK generated via the cross-transport key derivation procedure using a weaker BR/EDR Link Key. The IUT is the Peripheral device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has been discovered and is connected to the Lower Tester over LE.
- Test Procedure

Figure 4.231: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Responder MSC -Page 1 of 2

Figure 4.232: Verify that a Weaker BR/EDR Key Does Not Overwrite a Stronger Key, as Responder MSC -Page 2 of 2

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
- Expected Outcome

## Pass verdict

The IUT and the Lower Tester reconnect over LE using the existing keys exchanged and stored in Step 4.

## GAP/DM/LEP/BV-22-C [Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Initiator]

- Test Purpose

Verify that a BR/EDR Link Key is not overwritten by the BR/EDR Link Key generated via the crosstransport key derivation procedure using a weaker LE LTK. The IUT is the Central device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The IUT has discovered and connected to the Lower Tester.
- Test Procedure

Figure 4.233: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Initiator MSC -Page 1 of 2

Figure 4.234: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Initiator MSC -Page 2 of 2

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

## GAP/DM/LEP/BV-23-C [Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Responder]

- Test Purpose

Verify that a BR/EDR Link Key is not overwritten by the BR/EDR Link Key generated via the crosstransport key derivation procedure using a weaker LE LTK. The IUT is the Peripheral device.

- Reference

[9] 14.1

- Initial Condition
- -The IUT supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester also supports BR/EDR/LE with Secure Connections capabilities on both transports. The Lower Tester has discovered and connected with the IUT over BR/EDR.
- Test Procedure

Figure 4.235: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Responder MSC -Page 1 of 2

Figure 4.236: Verify that a Weaker LE Key Does Not Overwrite a Stronger Key, as Responder MSC -Page 2 of 2

1. The Lower Tester initiates BR/EDR Secure Connections Pairing with the IUT. They complete Pairing phases for public key exchange, authentication, key generation, and encryption of the BR/EDR link.
2. The Lower Tester terminates the BR/EDR connection.
3. The Upper Tester puts the IUT in connectable mode on the LE transport.
4. The Lower Tester establishes an LE link with the IUT.
5. The Lower Tester initiates an SMP Pairing Request without MITM support and LinkKey set to 1.
6. The IUT sends an SMP Pairing Response to the Lower Tester and may complete or fail during the pairing procedure.
7. The Lower Tester terminates the LE connection with the IUT.
8. The Lower Tester initiates a BR/EDR connection with the IUT. They complete encryption using the Link Key from Step 1.
- Expected Outcome

## Pass verdict

The IUT and the Lower Tester reconnect over BR/EDR using the existing keys exchanged and stored in Step 1.

## 4.8.9 Synchronization Establishment -Receiver

Verify the correct behavior in this mode. The role of the IUT is broadcast receiver.

## GAP/EST/SYNE/BV-01-C [Synchronization Establishment procedure, IUT is Receiver]

- Test Purpose

Verify that the IUT performs a synchronization establishment procedure initiated by itself. The IUT is the connectionless Peripheral broadcast receiver and the Lower Tester is the connectionless Peripheral broadcast transmitter.

- References

[9] 7.5

- Initial Condition
- -The IUT is in Standby state.
- -The Lower Tester is transmitting Synchronization Train with Interval = 80 ms.
- Test Procedure

Receive Synchronization Train on the IUT from the Lower Tester.

Figure 4.237: GAP/EST/SYNE/BV-01-C [Synchronization Establishment procedure, IUT is Receiver] MSC

- Expected Outcome

## Pass verdict

The IUT receives the Synchronization Train from the Lower Tester.

## 5 Test case mapping

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.

The columns for the TCMT are defined as follows:

Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for GAP [2].

If a test case is mandatory within the respective layer, then the y/x reference is omitted.

Feature: A brief, informal description of the feature being tested.

Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [5].

For the purpose and structure of the ICS/IXIT, refer to [5].

| Item | Feature | Test Case(s) |
| GAP 1/2 | Limited-discoverable mode | GAP/MOD/LDIS/BV-01-C GAP/MOD/LDIS/BV-02-C GAP/MOD/LDIS/BV-03-C |
| GAP 1/3 | General-discoverable mode | GAP/MOD/GDIS/BV-01-C GAP/MOD/GDIS/BV-02-C |
| GAP 3/1 | Verify that if general inquiry is initiated by the IUT, it sends for at least TGAP(100) inquiry request messages (GIAC). | GAP/IDLE/GIN/BV-01-C |
| GAP 3/2 | Verify that if limited inquiry is initiated by the IUT, it sends for at least TGAP(100) inquiry request messages (LIAC). | GAP/IDLE/LIN/BV-01-C |
| GAP 2/7 AND GAP 3/4 AND GAP 3/3 | Device discovery procedure - Central | GAP/IDLE/DED/BV-02-C |

| Item | Feature | Test Case(s) |
| GAP 2/7 AND GAP 3/6 AND (GAP 3/1 OR GAP 3/2) | Bonding - Central | GAP/IDLE/BON/BV-02-C |
| GAP 2/7 AND GAP 3/6 | Dedicated Bonding | GAP/IDLE/BON/BV-03-C |
| GAP 2/7 AND GAP 3/6 AND GAP 2/8 | Dedicated Bonding - Authenticated Link Key | GAP/IDLE/BON/BV-04-C |
| GAP 2/7 AND GAP 3/5 | General Bonding | GAP/IDLE/BON/BV-05-C |
| GAP 2/7 AND GAP 3/5 AND GAP 2/8 | General Bonding - Authenticated Link Key | GAP/IDLE/BON/BV-06-C |
| GAP 4/1 AND (GAP 3/1 OR GAP 3/2) | Verify that the IUT performs a link establishment procedure, initiated by itself | GAP/EST/LIE/BV-02-C |
| GAP 1/5 AND GAP 2/7 AND GAP 4/2 AND GAP 4/4 | Channel establishment, security mode 4 | GAP/SEC/SEM/BV-04-C |
| GAP 2/7 AND GAP 2/9 AND GAP 4/3 | Channel establishment, security mode 4 | GAP/SEC/SEM/BV-08-C |
| GAP 2/7 AND GAP 2/9 AND GAP 4/3 AND GAP 1/6 | Channel establishment, security mode 4, Non- bondable mode | GAP/SEC/SEM/BV-05-C GAP/SEC/SEM/BV-50-C |
| GAP 2/7 AND GAP 2/8 AND GAP 4/3 AND GAP 1/6 | Channel establishment, security mode 4, Non- bondable mode | GAP/SEC/SEM/BV-06-C GAP/SEC/SEM/BV-07-C GAP/SEC/SEM/BV-51-C GAP/SEC/SEM/BV-52-C |
| GAP 4/3 AND GAP 2/7 AND GAP 2/8 AND GAP 2/9 AND GAP 1/6 | Authenticated Link Key, Non-bondable mode | GAP/SEC/SEM/BV-09-C GAP/SEC/SEM/BV-53-C |
| GAP 2/7 AND (GAP 2/8 OR GAP 2/9) AND GAP 1/6 | Verify disconnect without encryption, Non-bondable mode | GAP/SEC/SEM/BV-10-C GAP/SEC/SEM/BI-24-C |
| GAP 2/7 AND (GAP 2/8 OR GAP 2/9) AND GAP 1/6 AND L2CAP 2/48a | Verify disconnect without encryption, Credit Based Flow Control, Non-bondable mode | GAP/SEC/SEM/BV-46-C |
| GAP 1/3 AND GAP 4e/3 | Device name during general inquiry | GAP/IDLE/DNDIS/BV-01-C |
| GAP 1/9 | Synchronization train | GAP/MOD/NSYN/BV-01-C GAP/MOD/SYN/BV-01-C |

| Item | Feature | Test Case(s) |
| GAP 4/7 | Verify that the IUT performs a synchronization establishment procedure initiated by itself. | GAP/EST/SYNE/BV-01-C |
| (GAP 22/4 OR GAP 32/3) AND GATT 1a/1 | Name Discovery procedure GATT Client | GAP/IDLE/NAMP/BV-01-C |
| (GAP 5/3 OR GAP 5/4) AND GATT 1a/3 | Name Discovery procedure GATT Server | GAP/IDLE/NAMP/BV-02-C |
| GAP 5/1 OR GAP 5/2 OR GAP 5/3 | Non-connectable mode | GAP/CONN/NCON/BV-01-C |
| GAP 23/5 OR GAP 33/6 | Terminate Connection procedure | GAP/CONN/TERM/BV-01-C |
| GAP 25/5 OR GAP 35/5 | Connection based signing - Sender | GAP/SEC/CSIGN/BV-01-C |
| GAP 25/6 OR GAP 35/6 | Connection based signing | GAP/SEC/CSIGN/BV-02-C GAP/SEC/CSIGN/BI-01-C GAP/SEC/CSIGN/BI-02-C GAP/SEC/CSIGN/BI-03-C GAP/SEC/CSIGN/BI-04-C |
| GAP 20a/1 OR GAP 8a/1 | AD type - Service UUID | GAP/ADV/BV-01-C |
| GAP 20a/2 OR GAP 8a/2 | AD type - Local Name | GAP/ADV/BV-02-C |
| GAP 20a/3 OR GAP 8a/3 | AD type - Flags | GAP/ADV/BV-03-C |
| GAP 20a/4 OR GAP 8a/4 | AD type - Manufacturer Specific Data | GAP/ADV/BV-04-C |
| GAP 20a/5 OR GAP 8a/5 | AD type - TX Power Level | GAP/ADV/BV-05-C |
| GAP 20a/8 OR GAP 8a/8 | AD type - Peripheral Connection Interval Range | GAP/ADV/BV-08-C |
| GAP 20a/9 OR GAP 8a/9 | AD type - Service Solicitation | GAP/ADV/BV-09-C |
| GAP 20a/10 OR GAP 8a/10 | AD type - Service Data | GAP/ADV/BV-10-C |
| GAP 8a/11 OR GAP 20a/11 | AD type - Appearance | GAP/ADV/BV-11-C |
| GAP 8a/12 OR GAP 20a/12 | AD type - Public Target Address | GAP/ADV/BV-12-C |
| GAP 8a/13 OR GAP 20a/13 | AD type - Random Target Address | GAP/ADV/BV-13-C |
| GAP 8a/14 OR GAP 20a/14 | AD type Advertising Interval | GAP/ADV/BV-14-C |
| GAP 8a/14a OR GAP 20a/14a | AD type Advertising Interval - Long | GAP/ADV/BV-18-C |
| GAP 8a/17 OR GAP 20a/17 | AD type - URI | GAP/ADV/BV-17-C |

| Item | Feature | Test Case(s) |
| GAP 8a/18 OR GAP 20a/18 | AD type - LE Supported Features | GAP/ADV/BV-19-C |
| (GAP 8a/19 OR GAP 20a/19) AND CORE 2b/61 | AD type - Encrypted Data, Advertising, v6.1 or earlier | GAP/ADV/BV-20-C |
| (GAP 8a/19 OR GAP 20a/19) AND CORE 2a/62 | AD type - Encrypted Data, Advertising, v6.2 or later | GAP/ADV/BV-21-C |
| GAP 14a/19 OR GAP 30a/19 | AD type - Encrypted Data, Scanning | GAP/SCN/BV-01-C |
| GAP 0b/1 AND GAP 5/3 AND GAP 1/4 | BR/EDR/LE non-connectable mode | GAP/DM/NCON/BV-01-C |
| GAP 0b/1 AND GAP 5/3 | BR/EDR/LE connectable mode | GAP/DM/CON/BV-01-C |
| GAP 0b/1 AND GAP 5/4 AND GAP 1/6 | BR/EDR/LE non-bondable mode | GAP/DM/NBON/BV-01-C |
| GAP 0b/1 AND GAP 5/4 AND GAP 1/7 AND (GAP 34/2 OR GAP 34/3) | BR/EDR/LE bondable mode | GAP/DM/BON/BV-01-C |
| GAP 0b/1 AND GAP 5/4 AND GAP 3/1 | BR/EDR/LE General Discovery - Finding General Discoverable Devices in General discovery | GAP/DM/GIN/BV-01-C |
| GAP 0b/1 AND GAP 5/4 AND GAP 3/2 AND GAP 32/1 | BR/EDR/LE Limited Discovery- Find Limited Discoverable Devices | GAP/DM/LIN/BV-01-C |
| GAP 3/3 AND GAP 0b/1 AND GAP 0b/2 | BR/EDR/LE Name Discovery over BR/EDR | GAP/DM/NAD/BV-01-C |
| GAP 0b/1 AND GAP 5/4 AND GAP 32/3 | BR/EDR/LE Name Discovery over LE | GAP/DM/NAD/BV-02-C |
| GAP 0b/1 AND GAP 5/3 AND GAP 1/5 | BR/EDR/LE and BR/EDR/LE Link Establishment - Peripheral | GAP/DM/LEP/BV-01-C |
| GAP 0b/1 AND GAP 5/4 AND (GAP 33/2 OR GAP 33/3) | BR/EDR/LE with LE-only Link Establishment - Central | GAP/DM/LEP/BV-06-C |
| GAP 5/1 | Broadcast mode - No Scan Response | GAP/BROB/BCST/BV-01-C |
| GAP 6/2 AND (GAP 8/2 OR GAP 8/4) | Broadcast mode - Scan Response | GAP/BROB/BCST/BV-02-C |
| GAP 11/2 | Broadcast mode Resolvable Private Address | GAP/BROB/BCST/BV-03-C |

| Item | Feature | Test Case(s) |
| GAP 5/1 AND GAP 11/1 AND GAP 11/3 | Broadcast mode Non-Resolvable Private Address | GAP/BROB/BCST/BV-04-C |
| GAP 11a/1 | Periodic Advertising Synchronizability mode | GAP/PADV/PASM/BV-01-C |
| GAP 11a/1 AND GAP 11a/3 | Periodic Advertising Synchronizability mode, PAwR | GAP/PADV/PASM/BV-02-C |
| GAP 11a/2 | Periodic Advertising mode | GAP/PADV/PAM/BV-01-C |
| GAP 11a/2 AND GAP 11a/3 | Periodic Advertising mode, PAwR | GAP/PADV/PAM/BV-02-C |
| GAP 23/9 | Periodic Advertising Connection | GAP/PADV/PAC/BV-01-C |
| GAP 5/2 | Observation procedure, Passive Scanning | GAP/BROB/OBSV/BV-01-C |
| GAP 14/2 | Observation procedure, Active Scanning | GAP/BROB/OBSV/BV-02-C |
| GAP 17/1 AND GAP 14/2 AND (GAP 17/2 OR GAP 17/4) | Observation procedure, Active Scanning Non- Resolvable Private Address or Resolvable Private Address | GAP/BROB/OBSV/BV-05-C |
| GAP 17a/1 | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising | GAP/PADV/PASE/BV-01-C |
| GAP 17a/1 AND GAP 11a/3 | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising, PAwR | GAP/PADV/PASE/BV-07-C |
| GAP 17a/2 | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising | GAP/PADV/PASE/BV-02-C |
| GAP 17a/2 AND GAP 11a/3 | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising, PAwR | GAP/PADV/PASE/BV-08-C |
| GAP 33/10 | Periodic Advertising Connection | GAP/PADV/PAC/BV-02-C |
| GAP 27/5 OR GAP 4b/3 | Peripheral Preferred Connection Parameters Characteristic | GAP/GAT/BV-04-C |
| GAP 27/6 OR GAP 37/6 OR GAP 4b/8 | Writeable Device Name | GAP/GAT/BV-05-C |
| GAP 27/7 OR GAP 37/7 OR GAP 4b/9 | Writeable Appearance | GAP/GAT/BV-06-C |
| GAP 27/10 OR GAP 4b/6 | Encrypted Data Key Material | GAP/GAT/BV-09-C GAP/GAT/BV-10-C GAP/GAT/BV-11-C |
| GAP 27/10a OR GAP 4b/7 | Encrypted Data Key Material Indications | GAP/GAT/BV-15-C |
| GAP 27/1 OR GAP 37/1 OR GAP 4b/1 | Device Name | GAP/GAT/BV-16-C |
| GAP 27/2 OR GAP 37/2 OR GAP 4b/2 | Appearance | GAP/GAT/BV-17-C |

| Item | Feature | Test Case(s) |
| GAP 27/9 OR GAP 37/3 OR GAP 4b/4 | Central Address Resolution | GAP/GAT/BV-18-C |
| GAP 27/12 OR GAP 37/5 OR GAP 4b/5 | Resolvable Private Address Only | GAP/GAT/BV-19-C |
| GAP 37/4 OR GAP 27/11 | LE GATT Security Levels Characteristic | GAP/GAT/BV-12-C |
| GAP 22/1 | Non-discoverable mode, non-connectable modes - Peripheral role | GAP/DISC/NONM/BV-01-C |
| (GAP 20/1 OR GAP 20/5) AND GAP 22/1 AND GAP 23/3 | Non-discoverable mode, Undirected Connectable mode - Peripheral role | GAP/DISC/NONM/BV-02-C GAP/CONN/UCON/BV-01-C |
| GAP 23/2 OR GAP 23/3 | Non-Bondable mode - Peripheral role | GAP/BOND/NBON/BV-03-C |
| GAP 0b/1 AND GAP 22/2 AND GAP 5/3 AND (GAP 20/3 OR GAP 20/4 OR GAP 20/6 OR GAP 20/7) | Limited Discoverable mode - Non-connectable mode - Peripheral role - BR/EDR/LE | GAP/DISC/LIMM/BV-01-C |
| GAP 0b/1 AND GAP 5/3 AND GAP 22/2 AND (GAP 20/1 OR GAP 20/5) AND GAP 23/3 | Limited Discoverable mode - Undirected Connectable mode - Peripheral role - BR/EDR/LE | GAP/DISC/LIMM/BV-02-C |
| GAP 22/2 | Non-connectable mode, Limited Discoverable mode | GAP/CONN/NCON/BV-03-C |
| GAP 22/2 AND GAP 23/3 | Undirected Connectable mode, Limited Discoverable mode | GAP/CONN/UCON/BV-03-C |
| GAP 5/3 AND GAP 22/2 AND (GAP 20/3 OR GAP 20/4 OR GAP 20/6 OR GAP 20/7) | Limited Discoverable mode - Non-connectable mode - Peripheral role - LE Only | GAP/DISC/LIMM/BV-03-C |
| GAP 5/3 AND GAP 22/2 | Limited Discoverable mode - Undirected Connectable mode - Peripheral role - LE Only | GAP/DISC/LIMM/BV-04-C |
| GAP 0b/1 AND GAP 5/3 AND GAP 22/3 AND (GAP 20/3 OR GAP 20/4 OR GAP 20/6 OR GAP 20/7) | General Discoverable mode - Non-connectable mode - Peripheral role - BR/EDR/LE | GAP/DISC/GENM/BV-01-C |

| Item | Feature | Test Case(s) |
| GAP 0b/1 AND GAP 5/3 AND GAP 22/3 AND (GAP 20/1 OR GAP 20/5) AND GAP 23/3 | General Discoverable mode - Undirected Connectable mode - Peripheral role - BR/EDR/LE | GAP/DISC/GENM/BV-02-C |
| GAP 5/3 AND GAP 22/3 AND (GAP 20/3 OR GAP 20/4 OR GAP 20/6 OR GAP 20/7) | General Discoverable mode - Non-connectable mode - Peripheral role - LE Only | GAP/DISC/GENM/BV-03-C |
| GAP 5/3 AND GAP 22/3 AND (GAP 20/1 OR GAP 20/5) AND GAP 23/3 | General Discoverable mode - Undirected Connectable mode - Peripheral role - LE Only | GAP/DISC/GENM/BV-04-C |
| GAP 22/3 AND (GAP 20/3 OR GAP 20/4 OR GAP 20/6 OR GAP 20/7) | Non-connectable mode, General Discoverable mode | GAP/CONN/NCON/BV-02-C |
| GAP 0b/1 AND GAP 5/3 AND GAP 22/3 AND (GAP 20/1 OR GAP 20/5) | BR/EDR/LE to BR/EDR/LE over LE physical transport - IUT is Peripheral | GAP/DM/LEP/BV-07-C |
| GAP 0b/1 AND GAP 5/3 AND (GAP 20/1 OR GAP 20/5) | Undirected Connectable mode, General Discoverable mode | GAP/CONN/UCON/BV-02-C |
| GAP 23/2 | Directed Connectable mode | GAP/CONN/DCON/BV-01-C |
| GAP 23/4 | Connection Parameter Update procedure, Peripheral role, Initiator over L2CAP | GAP/CONN/CPUP/BV-01-C GAP/CONN/CPUP/BV-02-C GAP/CONN/CPUP/BV-03-C |
| GAP 23/4 AND GAP 21/9 | Connection Parameter Update procedure, Peripheral role, Initiator over LL | GAP/CONN/CPUP/BV-10-C |
| GAP 24/3 AND GAP 27b/10 AND (GAP 25/1 OR GAP 25/2) | Initiate Bonding - Peripheral role | GAP/BOND/BON/BV-01-C |
| GAP 24/2 AND (GAP 25/1 OR GAP 25/2) | Respond to Bonding - Peripheral role | GAP/BOND/BON/BV-03-C |
| (GAP 25/1 OR GAP 25/2) AND GAP 25/3 | Service Response - insufficient authentication - Peripheral role | GAP/SEC/AUT/BV-11-C |
| (GAP 25/1 OR GAP 25/2) AND GAP 25/3 AND GATT 3a/1 | Service Response - insufficient authentication - Peripheral role | GAP/SEC/AUT/BV-26-C |

| Item | Feature | Test Case(s) |
| GAP 25/3 AND GAP 25/7 AND GAP 25/8 | Service Response - insufficient authentication, Peripheral role | GAP/SEC/AUT/BV-14-C |
| GAP 25/3 AND GAP 25/7 AND GATT 1/1 | Correct Pairing after Insufficient Authentication - Peripheral role | GAP/SEC/AUT/BV-18-C |
| GAP 25/3 AND GAP 25/8 AND GATT 1/1 | Service response Insufficient Authentication - Peripheral role | GAP/SEC/AUT/BV-20-C |
| GAP 25/1 AND GAP 25/8 AND GATT 1/1 | Lost Bond - Responder role | GAP/SEC/AUT/BV-22-C |
| GAP 25/3 AND GAP 25/7 | Service Response - Insufficient encryption, Peripheral role | GAP/SEC/AUT/BV-23-C |
| GAP 25/3 AND GAP 25/7 AND GATT 3a/1 | Service Response - Insufficient encryption, Peripheral role | GAP/SEC/AUT/BV-28-C |
| GAP 22/3 AND GAP 23/3 AND (GAP 24/2 OR GAP 24/3) AND GAP 26/1 | Privacy connection handling and RPA generation and resolution | GAP/PRIV/CONN/BV-12-C |
| GAP 21/9 | Connection Parameter Update procedure, Valid Parameters Peripheral role - LL Connection Parameters Request | GAP/CONN/CPUP/BV-08-C |
| GAP 24/2 AND GAP 26/1 | Connection handling with Private Random Device Address - Peripheral role | GAP/CONN/PRDA/BV-01-C |
| GAP 27a/1 | Periodic Advertising Synchronization Transfer procedure | GAP/PADV/PAST/BV-01-C |
| GAP 27a/1 AND GAP 11a/3 | Periodic Advertising Synchronization Transfer procedure, PAwR | GAP/PADV/PAST/BV-03-C |
| GAP 27a/2 | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising | GAP/PADV/PASE/BV-03-C |
| GAP 27a/2 AND GAP 11a/3 | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising, PAwR | GAP/PADV/PASE/BV-09-C |
| GAP 27a/3 | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising | GAP/PADV/PASE/BV-04-C |
| GAP 27a/3 AND GAP 11a/3 | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising, PAwR | GAP/PADV/PASE/BV-10-C |
| GAP 5/3 AND GAP 25/8 AND GATT 3/18 AND GAP 25/14 | Security mode 1 level 2 - GATT Indications, Peripheral | GAP/SEC/SEM/BV-56-C |
| GAP 5/3 AND GAP 25/8 AND GATT 3/17 AND GAP 25/14 | Security mode 1 level 2 - GATT Notifications, Peripheral | GAP/SEC/SEM/BV-59-C |

| Item | Feature | Test Case(s) |
| GAP 5/3 AND GAP 25/7 AND GATT 3/18 AND GAP 25/14 | Security mode 1 level 3 - GATT Indications, Peripheral | GAP/SEC/SEM/BV-57-C |
| GAP 5/3 AND GAP 25/7 AND GATT 3/17 AND GAP 25/14 | Security mode 1 level 3 - GATT Notifications, Peripheral | GAP/SEC/SEM/BV-60-C |
| GAP 32/2 | Discovery and Connection procedures - Central role | GAP/DISC/GENP/BV-01-C GAP/DISC/GENP/BV-02-C GAP/DISC/GENP/BV-03-C GAP/DISC/GENP/BV-04-C GAP/DISC/GENP/BV-05-C |
| GAP 33/2 AND (GAP 34/2 OR GAP 34/3) AND GAP 36/1 | Privacy connection handling and RPA generation and resolution | GAP/PRIV/CONN/BV-11-C |
| GAP 33/5 | Connection Parameter Update procedure, Central role | GAP/CONN/CPUP/BV-04-C GAP/CONN/CPUP/BV-05-C GAP/CONN/CPUP/BV-06-C |
| GAP 34/1 | Non-bondable mode - Central | GAP/BOND/NBON/BV-01-C GAP/BOND/NBON/BV-02-C |
| GAP 32/1 | Limited Discovery procedure - Central role | GAP/DISC/LIMP/BV-01-C GAP/DISC/LIMP/BV-02-C GAP/DISC/LIMP/BV-03-C GAP/DISC/LIMP/BV-04-C GAP/DISC/LIMP/BV-05-C |
| GAP 33/1 | Auto Connection Establishment procedure Directed Connectable mode - Central role | GAP/CONN/ACEP/BV-01-C |
| GAP 33/2 | General Connection Establishment procedure - Central role | GAP/CONN/GCEP/BV-01-C GAP/CONN/GCEP/BV-02-C |
| GAP 33/3 | Selective Connection Establishment procedure, Directed Connectable mode | GAP/CONN/SCEP/BV-01-C |
| GAP 33/4 | Direct Connection Establishment procedure, Directed and Undirected Connectable modes | GAP/CONN/DCEP/BV-01-C GAP/CONN/DCEP/BV-03-C |
| GAP 34/3 AND (GAP 35/1 OR GAP 35/2) | Initiate Bonding - Central role | GAP/BOND/BON/BV-02-C |
| GAP 34/2 AND (GAP 35/1 OR GAP 35/2) | Respond to Bonding - Central role | GAP/BOND/BON/BV-04-C |
| (GAP 35/1 OR GAP 35/2) AND GAP 35/3 | Service Response - Insufficient authentication, Central role | GAP/SEC/AUT/BV-12-C GAP/SEC/AUT/BV-25-C |
| GAP 35/3 AND GAP 35/7 AND GAP 35/8 | Service Response - Insufficient Authentication, Central role | GAP/SEC/AUT/BV-13-C |

| Item | Feature | Test Case(s) |
| GAP 35/3 AND GAP 35/7 AND GATT 1/1 | Correct Pairing after Insufficient Authentication - Central role | GAP/SEC/AUT/BV-17-C |
| GAP 35/3 AND GAP 35/8 AND GATT 1/1 | Service response Insufficient Authentication - Central role | GAP/SEC/AUT/BV-19-C |
| GAP 35/1 AND GAP 35/8 | Lost Bond - Initiator role | GAP/SEC/AUT/BV-21-C |
| GAP 35/3 | Service Response - Insufficient Encryption, Central role | GAP/SEC/AUT/BV-24-C GAP/SEC/AUT/BV-27-C |
| GAP 34/2 AND GAP 36/1 | Connection handling with Private Random Device Address - Central role | GAP/CONN/PRDA/BV-02-C |
| GAP 37a/1 | Periodic Advertising Synchronization Transfer procedure | GAP/PADV/PAST/BV-02-C |
| GAP 37a/1 AND GAP 11a/3 | Periodic Advertising Synchronization Transfer procedure, PAwR | GAP/PADV/PAST/BV-04-C |
| GAP 37a/2 | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising | GAP/PADV/PASE/BV-05-C |
| GAP 37a/2 AND GAP 11a/3 | Periodic Advertising Synchronization Establishment procedure without listening for periodic advertising, PAwR | GAP/PADV/PASE/BV-11-C |
| GAP 37a/3 | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising | GAP/PADV/PASE/BV-06-C |
| GAP 37a/3 AND GAP 11a/3 | Periodic Advertising Synchronization Establishment procedure with listening for periodic advertising, PAwR | GAP/PADV/PASE/BV-12-C |
| GAP 5/4 AND GAP 35/8 AND GATT 3/18 AND GAP 35/15 | Security mode 1 level 2 - GATT Indications, Central | GAP/SEC/SEM/BV-62-C |
| GAP 5/4 AND GAP 35/8 AND GATT 3/17 AND GAP 35/15 | Security mode 1 level 2 - GATT Notifications, Central | GAP/SEC/SEM/BV-65-C |
| GAP 5/4 AND GAP 35/7 AND GATT 3/18 AND GAP 35/15 | Security mode 1 level 3 - GATT Indications, Central | GAP/SEC/SEM/BV-63-C |
| GAP 5/4 AND GAP 35/7 AND GATT 3/17 AND GAP 35/15 | Security mode 1 level 3 - GATT Notifications, Central | GAP/SEC/SEM/BV-66-C |

| Item | Feature | Test Case(s) |
| GAP 1/5 AND GAP 4/2 AND GAP 4/4 AND GAP 4/6 AND GAP 2/11 | Verify Secure Connections Only mode when IUT is Peripheral and responder | GAP/SEC/SEM/BV-11-C GAP/SEC/SEM/BV-12-C GAP/SEC/SEM/BV-13-C GAP/SEC/SEM/BV-14-C GAP/SEC/SEM/BV-15-C GAP/SEC/SEM/BV-47-C GAP/SEC/SEM/BV-48-C GAP/SEC/SEM/BV-49-C |
| GAP 4/1 AND GAP 4/3 AND GAP 4/5 AND GAP 2/11 | Verify Secure Connections only mode when IUT is Central and initiator | GAP/SEC/SEM/BV-16-C GAP/SEC/SEM/BV-17-C GAP/SEC/SEM/BV-18-C GAP/SEC/SEM/BV-19-C GAP/SEC/SEM/BV-20-C GAP/SEC/SEM/BV-54-C GAP/SEC/SEM/BV-55-C |
| GAP 2/5 | BR/EDR security mode 2 | GAP/SEC/SEM/BI-01-C GAP/SEC/SEM/BI-05-C |
| GAP 2/7d | BR/EDR security mode 4 level 1 - Invalid Key Size - Any Key Size | GAP/SEC/SEM/BI-11-C GAP/SEC/SEM/BI-12-C |
| GAP 2/7c | BR/EDR security mode 4 level 2 - Invalid Key Size - Any Key Size | GAP/SEC/SEM/BI-02-C GAP/SEC/SEM/BI-06-C |
| GAP 2/7b | BR/EDR security mode 4 level 3 - Invalid Key Size - Any Key Size | GAP/SEC/SEM/BI-03-C GAP/SEC/SEM/BI-07-C |
| GAP 2/7a | BR/EDR security mode 4 level 4 | GAP/SEC/SEM/BI-31-C |
| GAP 2/13d | BR/EDR security mode 4 level 1 - Invalid Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-14-C GAP/SEC/SEM/BI-17-C |
| GAP 2/13c | BR/EDR security mode 4 level 2 - Invalid Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-15-C GAP/SEC/SEM/BI-18-C |
| GAP 2/13b | BR/EDR security mode 4 level 3 - Invalid Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-16-C GAP/SEC/SEM/BI-19-C |
| GAP 2/13a | BR/EDR security mode 4 level 4 - Invalid Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-04-C GAP/SEC/SEM/BI-08-C |
| GAP 0b/1 AND GAP 5/3 AND GAP 45/1 | BR/EDR/LE to BR/EDR/LE over both transports - IUT is LE peripheral/BR Peripheral | GAP/DM/LEP/BV-08-C |
| GAP 0b/1 AND GAP 5/4 AND GAP 44/2 | BR/EDR/LE to BR/EDR/LE over both transports - IUT is LE central/BR Central | GAP/DM/LEP/BV-09-C |
| GAP 0b/1 AND GAP 5/3 AND GAP 45/2 | BR/EDR/LE to BR/EDR/LE over both transports - IUT is LE peripheral/BR Central | GAP/DM/LEP/BV-10-C |
| GAP 0b/1 AND GAP 5/4 AND GAP 44/1 | BR/EDR/LE to BR/EDR/LE over both transports - IUT is LE central/BR Peripheral | GAP/DM/LEP/BV-11-C |

| Item | Feature | Test Case(s) |
| GAP 35/9 AND GAP 41/2a AND GAP 2/11 | Generate BR/EDR Link Key from LE LTK, as initiator | GAP/DM/LEP/BV-12-C GAP/DM/LEP/BV-15-C GAP/DM/LEP/BV-20-C |
| GAP 25/9 AND GAP 43/2a AND GAP 2/11 | Generate BR/EDR Link Key from LE LTK, as responder | GAP/DM/LEP/BV-14-C GAP/DM/LEP/BV-16-C GAP/DM/LEP/BV-21-C |
| GAP 35/9 AND GAP 41/2b AND GAP 2/11 | Generate LE LTK from BR/EDR Link Key, as initiator | GAP/DM/LEP/BV-17-C GAP/DM/LEP/BI-01-C GAP/DM/LEP/BV-22-C |
| GAP 25/9 AND GAP 43/2b AND GAP 2/11 | Generate LE LTK from BR/EDR Link Key, as responder | GAP/DM/LEP/BV-19-C GAP/DM/LEP/BI-02-C GAP/DM/LEP/BV-23-C |
| GAP 35/9 AND GAP 2/11 AND GAP 41/2a AND GAP 41/2b | Regenerate BR/EDR Link Key or LE LTK following cross-transport key upgrade | GAP/DM/LEP/BV-13-C GAP/DM/LEP/BV-18-C |
| GAP 5/3 AND GAP 25/9 | Peripheral, LE Secure Connections - security mode 1 level 4 | GAP/SEC/SEM/BV-21-C GAP/SEC/SEM/BV-22-C |
| GAP 5/3 AND GAP 25/13a | Peripheral, LE Secure Connections Only - security mode 1 level 4 - 128-bit Key Size | GAP/SEC/SEM/BI-09-C |
| GAP 5/3 AND GAP 25/12 | Peripheral, LE Secure Connections Only - security mode 1 level 3 | GAP/SEC/SEM/BV-38-C GAP/SEC/SEM/BV-40-C |
| GAP 5/3 AND GAP 25/11 | Peripheral, LE Secure Connections Only - security mode 1 level 2 | GAP/SEC/SEM/BV-37-C GAP/SEC/SEM/BV-39-C |
| GAP 5/3 AND (GAP 25/9 OR GAP 25/11 OR GAP 25/12) AND GATT 3/18 AND GAP 25/14 | LE Secure Connections Only - GATT Indications, Peripheral | GAP/SEC/SEM/BV-58-C |
| GAP 5/3 AND ((GAP 25/9 AND GAP 25/10) OR GAP 25/11 OR GAP 25/12) AND GATT 3/17 AND GAP 25/14 | LE Secure Connections Only - GATT Notifications, Peripheral | GAP/SEC/SEM/BV-61-C |
| GAP 5/3 AND GAP 25/13b | Peripheral, LE security mode 1 level 3 - Invalid Encryption Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-20-C |
| GAP 5/3 AND GAP 25/13c | Peripheral, LE security mode 1 level 2 - Invalid Encryption Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-21-C |
| GAP 2/7a AND GAP 4/3 | BR/EDR security mode 4 level 4, Initiator, Channel Establishment | GAP/SEC/SEM/BI-27-C GAP/SEC/SEM/BI-32-C |
| GAP 2/7b AND GAP 4/3 | BR/EDR security mode 4 level 3, Initiator, Channel Establishment | GAP/SEC/SEM/BI-26-C |
| GAP 2/7c AND GAP 4/3 | BR/EDR security mode 4 level 2, Initiator, Channel Establishment | GAP/SEC/SEM/BI-25-C |

| Item | Feature | Test Case(s) |
| GAP 2/7a AND L2CAP 2/37 | BR/EDR security mode 4 level 4, Initiator, Connectionless Channel, Unicast Data | GAP/SEC/SEM/BI-30-C GAP/SEC/SEM/BI-33-C |
| GAP 2/7b AND L2CAP 2/37 | BR/EDR security mode 4 level 3, Initiator, Connectionless Channel, Unicast Data | GAP/SEC/SEM/BI-29-C |
| GAP 2/7c AND L2CAP 2/37 | BR/EDR security mode 4 level 2, Initiator, Connectionless Channel, Unicast Data | GAP/SEC/SEM/BI-28-C |
| GAP 5/3 AND (GAP 25/10 OR GAP 25/11 OR GAP 25/12) | Peripheral, Secure Connections Only mode | GAP/SEC/SEM/BV-23-C GAP/SEC/SEM/BV-24-C |
| GAP 2/11 AND GAP 25/10 | Security Connections Only mode, Peripheral, BR/EDR and LE transports | GAP/SEC/SEM/BV-25-C |
| GAP 5/4 AND GAP 35/9 | Central, LE security mode 1 level 4 | GAP/SEC/SEM/BV-26-C GAP/SEC/SEM/BV-27-C GAP/SEC/SEM/BV-45-C |
| GAP 5/4 AND GAP 35/12 | Central, LE Secure Connections Only - LE security mode 1 level 3 | GAP/SEC/SEM/BV-42-C GAP/SEC/SEM/BV-44-C |
| GAP 5/4 AND GAP 35/11 | Central, LE Secure Connections Only - LE security mode 1 level 2 | GAP/SEC/SEM/BV-41-C GAP/SEC/SEM/BV-43-C |
| GAP 5/4 AND (GAP 35/9 OR GAP 35/11 OR GAP 35/12) AND GATT 3/18 AND GAP 35/15 | LE Secure Connections Only - GATT Indications, Central | GAP/SEC/SEM/BV-64-C |
| GAP 5/4 AND ((GAP 35/9 AND GAP 35/10) OR GAP 35/11 OR GAP 35/12) AND GATT 3/17 AND GAP 35/15 | LE Secure Connections Only - GATT Notifications, Central | GAP/SEC/SEM/BV-67-C |
| GAP 5/4 AND GAP 35/13a | Central, LE security mode 1 level 4 - Invalid Encryption Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-10-C |
| GAP 5/4 AND GAP 35/13b | Central, LE security mode 1 level 3 - Invalid Encryption Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-22-C |
| GAP 5/4 AND GAP 35/13c | Central, LE security mode 1 level 2 - Invalid Encryption Key Size - 128-bit Key Size | GAP/SEC/SEM/BI-23-C |
| GAP 5/4 AND (GAP 35/10 OR GAP 35/11 OR GAP 35/12) | Central, Secure Connections Only mode | GAP/SEC/SEM/BV-28-C GAP/SEC/SEM/BV-29-C |
| GAP 2/11 AND GAP 35/10 | Secure Connections Only mode, Central, BR/EDR and LE transports | GAP/SEC/SEM/BV-30-C |
| (GAP 8/2 OR GAP 8/4) AND GAP 11/2 AND GAP 11/4 AND GAP 11/5 | Broadcast mode Resolvable Private Address, Scan Response | GAP/BROB/BCST/BV-05-C |

| Item | Feature | Test Case(s) |
| GAP 14/2 AND GAP 17/3 AND GAP 17/4 | Observation procedure with Active Scanning, using Resolvable Private Address | GAP/BROB/OBSV/BV-06-C |
| GAP 36/1 AND GAP 36/3 AND (GAP 32/1 OR GAP 32/2) | Discovery procedure Finding Discoverable Device using Resolvable Privacy Address | GAP/DISC/RPA/BV-01-C |
| GAP 26/1 AND GAP 27/9 AND GAP 23/2 | Directed Connectable mode, Privacy, Resolvable Private Address, Central Address Resolution | GAP/CONN/DCON/BV-04-C GAP/CONN/DCON/BV-05-C |
| GAP 26/1 AND GAP 23/3 | Undirected Connectable mode Resolvable Private Address | GAP/PRIV/CONN/BV-10-C |
| GAP 36/1 AND GAP 36/3 AND GAP 33/1 | Auto Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution | GAP/CONN/ACEP/BV-03-C GAP/CONN/ACEP/BV-04-C |
| GAP 36/1 AND GAP 36/3 AND GAP 33/2 | General Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address, Central Address Resolution | GAP/CONN/GCEP/BV-05-C GAP/CONN/GCEP/BV-06-C |
| GAP 36/1 AND GAP 36/3 AND GAP 33/3 | Selective Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address | GAP/CONN/SCEP/BV-03-C |
| GAP 36/1 AND GAP 36/3 AND GAP 33/4 | Direct Connection Establishment procedure, Directed Connectable mode, Resolvable Private Address | GAP/CONN/DCEP/BV-05-C GAP/CONN/DCEP/BV-06-C |
| GAP 17b/2 AND GAP 2/9 | LE security mode 3, Observer, No Security | GAP/SEC/SEM/BV-31-C |
| (GAP 17b/3 OR GAP 17b/4) AND GAP 2/9 | LE security mode 3, Observer, Encryption | GAP/SEC/SEM/BV-32-C |
| GAP 17b/1 | LE security mode, Observer, Reject | GAP/SEC/SEM/BI-13-C |
| GAP 11b/2 AND GAP 2/9 | LE security mode 3, Broadcaster, No Security | GAP/SEC/SEM/BV-34-C |
| (GAP 11b/3 OR GAP 11b/4) AND GAP 2/9 | LE security mode 3, Broadcaster, Encryption | GAP/SEC/SEM/BV-35-C |
| GAP 16/2 | Broadcast Isochronous Stream Synchronization Establishment procedure | GAP/BIS/BSE/BV-01-C |
| GAP 10/2 AND GAP 10/3 | Broadcast Isochronous Stream Broadcasting mode | GAP/BIS/BBM/BV-01-C |
| GAP 23/8 | Connection Subrate Request procedure | GAP/CSUB/CSR/BV-01-C |
| GAP 33/9 | Connection Subrate Update procedure | GAP/CSUB/CSU/BV-01-C |
| GAP 23a/1 OR GAP 33a/1 | Channel Sounding, Initiator | GAP/CS/BV-01-C |
| GAP 23a/2 OR GAP 33a/2 | Channel Sounding, Reflector | GAP/CS/BV-02-C |

| Item | Feature | Test Case(s) |
| (GAP 23a/1 AND GAP 25/15) OR (GAP 33a/1 AND GAP 35/16) | Channel Sounding Security Level 1, Initiator | GAP/SEC/SEM/BV-69-C |
| (GAP 23a/1 AND GAP 25/16) OR (GAP 33a/1 AND GAP 35/17) | Channel Sounding Security Level 2, Initiator | GAP/SEC/SEM/BV-70-C |
| (GAP 23a/1 AND GAP 25/17) OR (GAP 33a/1 AND GAP 35/18) | Channel Sounding Security Level 3, Initiator | GAP/SEC/SEM/BV-71-C |
| (GAP 23a/1 AND GAP 25/18) OR (GAP 33a/1 AND GAP 35/19) | Channel Sounding Security Level 4, Initiator | GAP/SEC/SEM/BV-72-C |
| (GAP 23a/2 AND GAP 25/15) OR (GAP 33a/2 AND GAP 35/16) | Channel Sounding Security Level 1, Reflector | GAP/SEC/SEM/BV-73-C |
| (GAP 23a/2 AND GAP 25/16) OR (GAP 33a/2 AND GAP 35/17) | Channel Sounding Security Level 2, Reflector | GAP/SEC/SEM/BV-74-C |
| (GAP 23a/2 AND GAP 25/17) OR (GAP 33a/2 AND GAP 35/18) | Channel Sounding Security Level 3, Reflector | GAP/SEC/SEM/BV-75-C |
| (GAP 23a/2 AND GAP 25/18) OR (GAP 33a/2 AND GAP 35/19) | Channel Sounding Security Level 4, Reflector | GAP/SEC/SEM/BV-76-C |

Table 5.1: Test case mapping

## 6 Annex: Generic GAP Integrated Tests (GGAIT)

This annex defines generic GAP test procedures that are required to be executed for supported security features.

## 6.1 Identification conventions

In addition to the conventions defined in Section 4.1.1, the following identifiers are introduced in this annex.

| Identifier Abbreviation | Group Identifier <class> |
| CGGAIT | Client GGAIT test procedures |
| GGAIT | Generic GAP Integrated Tests |
| GP | Generated Passkeys |
| SGGAIT | Server GGAIT test procedures |

Table 6:1: Identification conventions

## 6.2 GGAIT input tables

The GGAIT procedures are executed with an input consisting of a table that is defined by each identifier abbreviation, e.g., GP-.

In Test Suite documents that use the GGAIT procedures, it may be a good idea to use the 'landscape' page setup to achieve better readability to avoid the page width limitations the regular 'portrait' page setup yields.

## 6.2.1 Input table for GP-tests

The table lists all the requirements that are being tested.

| TCID | Reference |
| TCID | [SPEC] X.Y |
| … | … |

Table 6:2: GGAIT input table format

The recommended format for the TCID of these tests is:

&lt;spec abbreviation&gt; /ROLE/ SGGAIT / GP /BV-XX-C, (for Server Tests), and

&lt;spec abbreviation&gt; /ROLE/ CGGAIT / GP /BV-XX-C, (for Client Tests)

## 6.2.1.1 Example usage -CGM Profile TS

[This is an extract showing how the CGM Profile TS can reference the GGAIT as an alternative to creating test cases for each security requirement related procedures.]

Execute the Generic GAP Integrated Tests defined in [GAP.TS.REF#] Section 6.3 and Section 6.4 using Table 6:3 below as input:

[REF#] below is the reference to the related specification (in this case CGM Profile) as the CGMP.TS defines it.

| TCID | Reference |
| CGMP/SEN/SGGAIT/GP/BV-01-C [Passkey Generation for Passkey Entry - Sensor Responder] | [REF#] 6.1.1 |
| CGMP/COL/CGGAIT/GP/BV-01-C [Passkey Generation for Passkey Entry - Collector Initiator] | [REF#] 6.1.1, 6.2.1 |

Table 6:3: Example input table for GGAIT Server and Client tests

## 6.3 Server test procedures (SGGAIT)

In the case of GP-tests, the IUT and the Lower Tester have not bonded, for each row of the Server GGAIT input table:

- The test sequences in Section 6.3.1 are executed.

## 6.3.1 SGGAIT/GP [Generated Passkeys]

Execute all the following test steps three times or until one of the Passkey Entry method pairing attempts fails to generate a unique 6-digit passkey.

1. Establish an LE transport connection between the IUT and the Lower Tester.
2. Establish an L2CAP channel 0x0004 between the IUT and the Lower Tester over that LE Transport.
3. The Lower Tester sends a Pairing Request command, for the Passkey Entry method, with the IO capabilities set to 'KeyboardOnly', OOB data flag set to 0x00 , and the MITM flag set to 0x01.
4. The IUT sends a Pairing Response command with the IO capabilities set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardDisplay', and OOB data flag set to 0x00.
5. The Lower Tester and the IUT perform the Phase 2 (LE Secure Connections) pairing successfully using the Passkey Entry association model and using the same 6-digit passkey displayed by the IUT.
6. The Upper Tester induces the IUT to initiate an unpairing request to remove the bonding.

## Pass verdict

The IUT generates a passkey value for each Passkey Entry pairing attempt.

Each generated passkey is a unique 6-digit value within the range of 000000 to 999999, inclusive.

## 6.4 Client test procedures (CGGAIT)

In case of GP-tests, the IUT and the Lower Tester have not bonded, for each row of the Client GGAIT input table:

- The test sequences in Section 6.4.1 are executed.

## 6.4.1 CGGAIT/GP [Generated Passkeys]

Execute all the following test steps three times or until one of the Passkey Entry method pairing attempts fails to generate a unique 6-digit passkey.

1. Establish an LE transport connection between the IUT and the Lower Tester.
2. Establish an L2CAP channel 0x0004 between the IUT and the Lower Tester over that LE Transport.
3. The Upper Tester sends a command to the IUT to initiate a Pairing Request for the Passkey Entry method.
4. The IUT sends a Pairing Request command with the IO capabilities set to "DisplayOnly' or 'DisplayYesNo' or 'KeyboardDisplay', and OOB data flag set to 0x00.
5. The Lower Tester sends a Pairing Response command with the IO capability set to 'KeyboardOnly', OOB data flag set to 0x00, and the MITM flag set to 0x01.
6. The Lower Tester and the IUT perform the Phase 2 (LE Secure Connections) pairing successfully using the Passkey Entry association model and using the same 6-digit passkey displayed by the IUT.
7. The Upper Tester sends a command to the IUT to initiate an unpairing request to remove the bonding.

## Pass verdict

The IUT generates a passkey value for each Passkey Entry pairing attempt.

Each generated passkey is a unique 6-digit value within the range of 000000 to 999999, inclusive.

## 7 Revision history and acknowledgments
