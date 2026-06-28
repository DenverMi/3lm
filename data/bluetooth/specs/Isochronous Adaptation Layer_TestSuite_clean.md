## Isochronous Adaptation Layer (IAL)

## Bluetooth ® Test Suite

- Revision: IAL.TS.p11
- Revision Date: 2026-05-05

## 1 Scope

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Isochronous Adaptation Layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers' Bluetooth devices.

## 2 References, definitions, and abbreviations

## 2.1 References

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [1], [2], [3], and [4].

- [1] Bluetooth Core Specification, Version 5.2 or later
- [2] Test Strategy and Terminology Overview
- [3] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification), Version 5.2 or later
- [4] Specification of the Bluetooth System, Volume 6, Part G (Isochronous Adaptation Layer), Version 5.2 or later
- [5] CS Proforma for Bluetooth Link Layer Protocol Specification
- [6] ICS Proforma for Bluetooth Isochronous Adaptation Layer Specification
- [7] Characteristic and Descriptor descriptions are accessible via the Bluetooth SIG Assigned Numbers
- [8] IXIT Proforma for Bluetooth Core, LL worksheet
- [9] Bluetooth Test Suite for Link Layer (LL.TS)
- [10] Appropriate Language Mapping Tables document
- [11] Specification of the Bluetooth System, Volume 6, Part G (Isochronous Adaptation Layer), Version 5.3 or later
- [12] Specification of the Bluetooth System, Volume 6, Part G (Isochronous Adaptation Layer), Version 5.4 or later
- [13] Specification for the Bluetooth System, Volume 6, Part G (Isochronous Adaptation Layer), Version 6.0 or later

## 2.2 Definitions

In this Bluetooth document, the definitions from [1], [2], [3], and [4] apply.

Certain terms that were identified as inappropriate have been replaced. For a list of the original terms and their replacement terms, see the Appropriate Language Mapping Tables document [10].

## 2.3 Acronyms and abbreviations

In this Bluetooth document, the definitions, acronyms, and abbreviations from [1], [2], [3], and [4] apply.

## 3 Test Suite Structure (TSS)

## 3.1 Overview

Figure 3.1: Test Suite Structure

## 3.2 Test Strategy

The test objectives are to verify the functionality of the Isochronous Adaptation Layer within a Bluetooth Host and enable interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory and optional requirements in the specification and matches these to the support of the IUT as described in the ICS. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test Case Mapping Table (TCMT) evaluates to true.

The test equipment provides an implementation of the Radio Controller and the parts of the Host needed to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT's peer device and interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement similar capabilities to communicate with the test equipment. For some test cases, it is necessary to stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface, a Man Machine Interface (MMI), or another interface supported by the IUT.

This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with catalogued specification requirements that were logically grouped and assessed for testability enabling coverage in defined test purposes.

Isochronous streams functionality includes specific testing features, see [9] Section 4.1.6.7.3, Test Command Generated Isochronous SDUs Optional Test Steps and Test Command Received Isochronous SDUs Optional Test Steps, providing approaches that may be employed when the Upper Tester may not be capable of meeting the bandwidth requirements of a given test procedure.

## 3.3 Test groups

The following test groups have been defined:

- Connected Isochronous Stream
- Broadcast Isochronous Stream
- Framed Data Traffic
- Unframed Data Traffic

## 4 Test cases (TC)

## 4.1 Introduction

## 4.1.1 Test case identification conventions

Test cases are assigned unique identifiers per the conventions in [2]. The convention used here is: &lt;spec abbreviation&gt; / &lt;IUT role&gt;/ &lt;class&gt; /&lt;feat&gt; /&lt;func&gt;/&lt;subfunc&gt;/&lt;cap&gt;/ &lt;xx&gt;-&lt;nn&gt;-&lt;y&gt; .

Table 4.1: IAL TC feature naming conventions

| Identifier Abbreviation | Spec Identifier <spec abbreviation> |
| IAL | Isochronous Adaptation Layer |
| Identifier Abbreviation | Feature Identifier <feat> |
| BIS | Broadcast Isochronous Stream |
| CIS | Connected Isochronous Stream |
| Identifier Abbreviation | Function Identifier <func> |
| FRA | Framed Data Traffic |
| UNF | Unframed Data Traffic |
| Identifier Abbreviation | Subfunction Identifier <subfunc> |
| BRD | Broadcaster role |
| CEN | Central role |
| PER | Peripheral role |
| SNC | Synchronized Receiver role |

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

## 4.1.3 Pass/Inconclusive/Fail verdict conventions

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met.

Certain test cases also have an Inconclusive verdict defined. If the conditions for this verdict are met, then the test provides evidence that the IUT neither meets nor violates the test case; instead, it means that the test case was not applicable to the IUT, and therefore a Pass verdict is not required in order to achieve Qualification of the IUT. Implementers are encouraged to provide mechanisms to avoid the behavior leading to an Inconclusive condition during testing.

The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict.

For an Inconclusive verdict, all the pass criteria conditions apply up to the point in the test procedure where an Inconclusive verdict is identified. If one of the pass criteria in a step prior to the Inconclusive verdict cannot be met, then the outcome of the test is the Fail verdict and not the Inconclusive verdict.

## 4.2 Common Packet Contents

## 4.2.1 Fields and Bits Reserved for Future Use

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers.

## 4.3 CIS

Tests that the IUT behaves according to the Isochronous Adaptation Layer Specifications for Connected Isochronous Streams.

## 4.3.1 Requirements

## 4.3.1.1 Timing Requirements

The timing of CIS tests in this section complies with the CIS timing requirements specified in [3] Section 4.10.1.2.

When using framed PDUs, the maximum allowed drift (MaxDrift) complies with the average timing of SDU delivery specified in [3] Section 2.2.

## 4.3.1.2 Configuring the ISO Data Path for HCI

The HCI\_LE\_Setup\_ISO\_Data\_Path is configured to use the HCI for input and/or output when appropriate for the test procedure. When applicable, Input\_Data\_Path is set to 0x00 (HCI transport), and likewise, Output\_Data\_Path is set to 0x00 (HCI transport).

## 4.3.2 Send Single SDU, CIS

- Test Purpose

Verify that the IUT can send an SDU with length ≤ the Isochronous PDU length.

- Reference

[3] 4.6.27

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts in the role as specified in Table 4.2.
- -The CIS has been created.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval\_C\_to\_P, SDU\_Interval\_P\_to\_C, Max\_PDU\_C\_to\_P, Max\_PDU\_P\_to\_C, ISO\_Interval, and Framing parameters are set as specified in Table 4.2. Max\_SDU\_C\_to\_P and Max\_SDU\_P\_to\_C are set to Max Data Length from Table 4.2. Framing is set to 0x00 if the test is Unframed, 0x01 if the test is Framed, Segmentable mode, and 0x02 if the test is Framed, Unsegmentable mode. When a field is designated as 'N/A', any valid value may be chosen.

## · Test Case Configuration

| Test Case | Role | NSE | Framed | Framing _Mode | LLID | P_To_C | P_To_C | C_To_P | C_To_P | C_To_P | SDU_Interval | SDU_Interval | ISO_Interval | Max Data Length |
| Test Case | Role | NSE | Framed | Framing _Mode | LLID | BN | Max PDU | BN | FT | Max PDU | P_To_C | C_To_P | ISO_Interval | Max Data Length |
| IAL/CIS/UNF/ CEN/BV-01-C | Central | 2 | 0 | 0 | 0b00 | 0 | N/A N/A | 1 | 1 | 32 | N/A | 15 ms (0x3A98) | 15 ms (0x0C) | 32 |
| IAL/CIS/UNF/ PER/BV-01-C | Peripheral | 3 | 0 | 0 | 0b00 | 2 | 32 | 0 | N/A | N/A | 6.25 ms (0x186A) | N/A | 12.5 ms (0x0A) | 32 |
| IAL/CIS/UNF/ CEN/BV-25-C | Central | 4 | 0 | 0 | 0b00 | 3 | 32 | 1 | 1 | 32 | 5 ms (0x1388) | 15 ms (0x3A98) | 15 ms (0x0C) | 32 |
| IAL/CIS/UNF/ PER/BV-25-C | Peripheral | 5 | 0 | 0 | 0b00 | 1 | 32 | 3 | 3 | 32 | 30 ms (0x7530) | 30 ms (0x7530) | 30 ms (0x18) | 32 |
| IAL/CIS/FRA/ CEN/BV-03-C | Central | 7 | 1 | 0 | 0b10 | 0 | N/A N/A | 3 | 4 | 32 | N/A | 40 ms (0x9C40) | 40 ms (0x20) | 27 |
| IAL/CIS/FRA/ PER/BV-03-C | Peripheral | 4 | 1 | 0 | 0b10 | 2 | 32 | 0 | N/A | N/A | 20 ms (0x4E20) | N/A | 25 ms (0x14) | 27 |
| IAL/CIS/FRA/ CEN/BV-26-C | Central | 3 | 1 | 0 | 0b10 | 1 | 32 | 2 | 3 | 32 | 20 ms (0x4E20) | 10 ms (0x2710) | 20 ms (0x10) | 19 |
| IAL/CIS/FRA/ PER/BV-26-C | Peripheral | 2 | 1 | 0 | 0b10 | 1 | 188 | 1 | 1 | 188 | 5.333 ms (0x14D5) | 5.333 ms (0x14D5) | 10 ms (0x08) | 92 |
| IAL/CIS/UNF/ CEN/BV-46-C | Central | 1 | 0 | 0 | 0b00 | 1 | 32 | 1 | 1 | 32 | 10 ms (0x2710) | 10 ms (0x2710) | 10 ms (0x08) | 32 |
| IAL/CIS/UNF/ PER/BV-47-C | Peripheral | 1 | 0 | 0 | 0b00 | 1 | 32 | 1 | 1 | 32 | 20 ms (0x4E20) | 20 ms (0x4E20) | 20 ms (0x10) | 32 |
| IAL/CIS/FRA/ CEN/BV-45-C | Central | 1 | 1 | 0 | 0b10 | 1 | 32 | 1 | 1 | 32 | 20 ms (0x4E20) | 20 ms (0x4E20) | 20 ms (0x10) | 19 |
| IAL/CIS/FRA/ PER/BV-45-C | Peripheral | 1 | 1 | 0 | 0b10 | 1 | 32 | 1 | 1 | 32 | 10 ms (0x2710) | 10 ms (0x2710) | 10 ms (0x08) | 19 |
| IAL/CIS/FRA/ CEN/BV-53-C | Central | 7 | 1 | 1 | 0b10 | 0 | N/A N/A | 2 | 4 | Max Data Length + 5 | N/A | 40 ms (0x9C40) | 40 ms (0x20) | 180 |
| IAL/CIS/FRA/ PER/BV-53-C | Peripheral | 4 | 1 | 1 | 0b10 | 2 | Max Data | 0 | N/A | N/A | 20 ms (0x4E20) | N/A | 25 ms (0x14) | 192 |

Table 4.2: Send Single SDU, CIS test cases

- Test Procedure

Figure 4.1: Send Single SDU, CIS MSC

If the values of NSE, BN, or FT specified in Table 4.2 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, refer to the Inconclusive verdict.

1. The Upper Tester sends an HCI ISO Data packet to the IUT with data length less than or equal to the Max Data Length as specified in Table 4.2.
2. The IUT sends a single ISO Data PDU to the Lower Tester with the LLID, Framed, and Framing as specified in Table 4.2 and Payload Data identical to the data in Step 1. If the BN value is not 0 in the direction from the Lower Tester to the IUT, then the Lower Tester sends a payload as configured in Table 4.2.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a PDU with LLID as specified in Table 4.2 and the same data in Step 1.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.2.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.2.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.2.

## 4.3.3 Send Large SDU, CIS

- Test Purpose

Verify that the IUT can send an SDU with length &gt; the Isochronous PDU length.

- Reference

[3] 4.6.27

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts in the role as specified in Table 4.3.
- -The CIS has been created.

- -In the LE Set CIG Parameters Test Command the NSE, BN\_P\_To\_C and BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval, ISO\_Interval, and Framing parameters are set as specified in Table 4.3.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- -Max\_SDU is set to 503 when the corresponding BN is not 0. Max\_SDU is set to 0 when the corresponding BN is 0.
- -Max\_PDU is set to 251 when the corresponding BN is not 0. Max\_PDU is set to 0 when the corresponding BN is 0.

## · Test Case Configuration

| Test Case | Role | NSE | Framing | P_To_C | P_To_C | C_To_P | C_To_P | SDU_Interval | ISO_Interval |
| Test Case | Role | NSE | Framing | BN | FT | BN | FT | SDU_Interval | ISO_Interval |
| IAL/CIS/UNF/CEN/BV-04-C | Central | 8 | Unframed (0x00) | 0 | N/A | 6 | 2 | 20 ms (0x4E20) | 40 ms (0x20) |
| IAL/CIS/UNF/PER/BV-04-C | Peripheral | 4 | Unframed (0x00) | 3 | 2 | 0 | N/A | 25 ms (0x61A8) | 25 ms (0x14) |
| IAL/CIS/UNF/CEN/BV-28-C | Central | 4 | Unframed (0x00) | 3 | 3 | 3 | 2 | 25 ms (0x61A8) | 25 ms (0x14) |
| IAL/CIS/UNF/PER/BV-28-C | Peripheral | 5 | Unframed (0x00) | 3 | 3 | 0 | N/A | 35 ms (0x88B8) | 35 ms (0x1C) |
| IAL/CIS/FRA/CEN/BV-05-C | Central | 5 | Framed, Segmentable mode (0x01) | 0 | N/A | 3 | 1 | 20 ms (0x4E20) | 25 ms (0x14) |
| IAL/CIS/FRA/PER/BV-05-C | Peripheral | 8 | Framed, Segmentable mode (0x01) | 5 | 2 | 0 | N/A | 25 ms (0x61A8) | 50 ms (0x28) |
| IAL/CIS/FRA/CEN/BV-29-C | Central | 4 | Framed, Segmentable mode (0x01) | 3 | 1 | 3 | 2 | 40 ms (0x9C40) | 40 ms (0x20) |
| IAL/CIS/FRA/PER/BV-29-C | Peripheral | 6 | Framed, Segmentable mode (0x01) | 4 | 2 | 4 | 3 | 22 ms (0x55F0) | 35 ms (0x1C) |
| IAL/CIS/FRA/CEN/BV-46-C | Central | 1 | Framed, Segmentable mode (0x01) | 1 | 1 | 1 | 1 | 30 ms (0x7530) | 10 ms (0x08) |
| IAL/CIS/FRA/PER/BV-46-C | Peripheral | 1 | Framed, Segmentable mode (0x01) | 1 | 1 | 1 | 1 | 30 ms (0x7530) | 10 ms (0x08) |

Table 4.3: Send Large SDU, CIS test cases

- Test Procedure

Figure 4.2: Send Large SDU, CIS MSC

If the values of NSE, BN, or FT specified in Table 4.3 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, go to the Inconclusive verdict.

Repeat Steps 1 -3 for each round in Table 4.4.

1. The Upper Tester sends an HCI ISO Data packet to the IUT with a data length specified in Table 4.4.
2. The IUT sends the specified number of Start/Continuation packets specified in Table 4.4 of ISO Data PDUs to the Lower Tester with the LLID=0b01 for unframed data and LLID=0b10 for framed, segmentable mode data. Payload Data every 251 bytes offset in Step 1. If the BN value is not 0 in the direction from the Lower Tester to the IUT, then the Lower Tester sends payloads as configured in Table 4.4.
3. The IUT sends the last ISO Data PDU to the Lower Tester with the LLID=0b00 for unframed data and LLID=0b10 for framed, segmentable mode data with the remaining Payload Data.
- Expected Outcome

Table 4.4: Send Large SDU, CIS rounds

| Round | SDU Data Length | Start/Continuation packets |
| 1 | 495 | 1 |
| 2 | 503 | 2 |

## Pass verdict

In Step 2, the IUT sends the correct number of Start/Continuation PDUs as specified in Table 4.4 and that each PDU contains a Segmentation Header.

In Step 3, the IUT sends a PDU with LLID=0b00 for unframed data and LLID=0b10 for framed, segmentable mode data and the same data in Step 1.

The bits in the RFU field in the Segmentation Headers from the IUT are clear.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.3.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.3.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.3.

## 4.3.4 Send Multiple, Small SDUs, CIS

- Test Purpose

Verify that the IUT can send multiple SDUs that can be combined into a single Isochronous PDU.

- Reference

[3] 4.6.27

[4] 2.2

- Initial Condition
- -The IUT acts in the role as specified in Table 4.5.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command the SDU\_Interval is half the ISO\_Interval, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval, and ISO\_Interval parameters are set as specified in Table 4.5. Framing is set to Framed, Segmentable mode (0x01).
- -Max\_SDU is set to 25 when the corresponding BN is not 0. Max\_SDU is set to 0 when the corresponding BN is 0.
- -Max\_PDU is set to 68 when the corresponding BN is not 0. Max\_PDU is set to 0 when the corresponding BN is 0.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- Test Case Configuration

Table 4.5: Send Multiple, Small SDUs, CIS test cases

| Test Case | Role | NSE | P_To_C | P_To_C | C_To_P | C_To_P | SDU_Interval | ISO_Interval |
| | | | BN | FT | BN | FT | | |
| IAL/CIS/FRA/CEN/BV-07-C | Central | 2 | 0 | N/A | 1 | 4 | 500 ms (0x7A120) | 1000 ms (0x320) |
| IAL/CIS/FRA/PER/BV-07-C | Peripheral | 2 | 1 | 1 | 0 | N/A | 500 ms (0x7A120) | 1000 ms (0x320) |
| IAL/CIS/FRA/CEN/BV-31-C | Central | 7 | 0 | N/A | 2 | 4 | 1000 ms (0xF4240) | 2000 ms (0x640) |
| IAL/CIS/FRA/PER/BV-31-C | Peripheral | 4 | 2 | 1 | 2 | 2 | 1000 ms (0xF4240) | 2000 ms (0x640) |
| IAL/CIS/FRA/CEN/BV-47-C | Central | 1 | 1 | 1 | 1 | 1 | 500 ms (0x7A120) | 1000 ms (0x320) |
| IAL/CIS/FRA/PER/BV-47-C | Peripheral | 1 | 1 | 1 | 1 | 1 | 500 ms (0x7A120) | 1000 ms (0x320) |

## · Test Procedure

Figure 4.3: Send Multiple, Small SDUs, CIS MSC

If the values of NSE, BN, or FT specified in Table 4.5 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, then refer to the Inconclusive verdict.

1. The Upper Tester sends to the IUT a small SDU1 with data length of 20 bytes.
2. The Upper Tester sends to the IUT a small SDU2 with data length of 25 bytes.
3. The IUT sends a single PDU with SDU1 followed by SDU2 to the Lower Tester. Each SDU header has SC = 0 and CMPT = 1.
- Expected Outcome

## Pass verdict

In Step 3, the IUT sends a single small PDU with data length of 55 bytes with SDU1 followed by SDU2.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.5.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.5.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.5.

## 4.3.5 Receive Single SDU, CIS

- Test Purpose

Verify that the IUT can receive an SDU with length ≤ the Isochronous PDU length.

- Reference

[3] 4.6.27

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts in the role as specified in Table 4.6.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval, ISO\_Interval, and Framing parameters are set as specified in Table 4.6. Framed is set to 0b0 and Framing\_Mode is set to 0b0 if the test is Unframed. Framed

is set to 0b1 and Framing\_Mode is set to 0b0 if the test is Framed, Segmentable mode. Framed is set to 0b1 and Framing\_Mode is set to 0b1 if the test is Framed, Unsegmented mode.

- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- -If the corresponding BN is not 0, then Max\_SDU is set to the value in Table 4.6.
- -If the corresponding BN is 0, then Max\_SDU is set to 0 and Max\_PDU is set to 0.

## · Test Case Configuration

| Test Case | Role | NSE | Framed | Framing _Mode | LLID | P_To_C | P_To_C | C_To_P | C_To_P | SDU_Interval | ISO_Interval | Max_SDU |
| Test Case | Role | NSE | Framed | Framing _Mode | LLID | BN | FT | BN | FT | SDU_Interval | ISO_Interval | Max_SDU |
| IAL/CIS/UNF/CEN/BV-09-C | Central | 4 | 0 | 0 | 0b00 | 3 | 1 | 0 | N/A | 5 ms (0x1388) | 15 ms (0x0C) | 251 |
| IAL/CIS/UNF/PER/BV-09-C | Peripheral | 2 | 0 | 0 | 0b00 | 0 | N/A | 1 | 1 | 15 ms (0x3A98) | 15 ms (0x0C) | 251 |
| IAL/CIS/UNF/CEN/BV-33-C | Central | 5 | 0 | 0 | 0b00 | 3 | 3 | 3 | 2 | 30 ms (0x7530) | 30 ms (0x18) | 251 |
| IAL/CIS/UNF/PER/BV-33-C | Peripheral | 4 | 0 | 0 | 0b00 | 3 | 1 | 3 | 1 | 10 ms (0x2710) | 30 ms (0x18) | 251 |
| IAL/CIS/FRA/CEN/BV-10-C | Central | 4 | 1 | 0 | 0b10 | 2 | 2 | 0 | N/A | 20 ms (0x4E20) | 25 ms (0x14) | 251 |
| IAL/CIS/FRA/PER/BV-10-C | Peripheral | 7 | 1 | 0 | 0b10 | 0 | N/A | 3 | 4 | 40 ms (0x9C40) | 40 ms (0x20) | 251 |
| IAL/CIS/FRA/CEN/BV-35-C | Central | 3 | 1 | 0 | 0b10 | 2 | 1 | 0 | N/A | 5.333 ms (0x14D5) | 10 ms (0x08) | 251 |
| IAL/CIS/FRA/PER/BV-35-C | Peripheral | 4 | 1 | 0 | 0b10 | 0 | N/A | 3 | 3 | 10 ms (0x2710) | 20 ms (0x10) | 251 |
| IAL/CIS/UNF/CEN/BV-47-C | Central | 1 | 0 | 0 | 0b00 | 1 | 1 | 1 | 1 | 15 ms (0x3A98) | 15 ms (0x0C) | 251 |
| IAL/CIS/UNF/PER/BV-48-C | Peripheral | 1 | 0 | 0 | 0b00 | 1 | 1 | 1 | 1 | 10 ms (0x2710) | 10 ms (0x08) | 251 |
| IAL/CIS/FRA/CEN/BV-48-C | Central | 1 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | 20 ms (0x4E20) | 20 ms (0x10) | 238 or (TSPX_ max_pdu_length -13) whichever is less |
| IAL/CIS/FRA/PER/BV-48-C | Peripheral | 1 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | 30 ms (0x7530) | 30 ms (0x18) | 238 or (TSPX_ max_pdu_length -13) whichever is less |
| IAL/CIS/FRA/CEN/BV-54-C | Central | 4 | 1 | 1 | 0b10 | 2 | 2 | 0 | N/A | 20 ms (0x4E20) | 25 ms (0x14) | 246 |
| IAL/CIS/FRA/PER/BV-54-C | Peripheral | 7 | 1 | 1 | 0b10 | 0 | N/A | 2 | 2 | 20 ms (0x4E20) | 20 ms (0x14) | 246 |

Table 4.6: Receive Single SDU, CIS test cases

- Test Procedure

Figure 4.4: Receive Single SDU, CIS MSC

If the values of NSE, BN, or FT specified in Table 4.6 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, go to the Inconclusive verdict.

1. The Lower Tester sends the IUT a single ISO Data PDU with the LLID, Framed, and Framing as specified in Table 4.6. The SDU size is equivalent to the Max payload contained in a Max\_PDU. If the BN value is not 0 in the direction from the IUT to the Lower Tester, then the IUT sends a payload as configured in Table 4.6.
2. The IUT sends an Isochronous Data SDU to the Upper Tester with Payload Data identical to the data in Step 1 and Data\_Total\_Length identical to the data length sent in Step 1.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends to the Upper Tester the same data sent by the Lower Tester in Step 1.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.6.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.6.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.6.

## 4.3.6 Receive Large SDU, CIS, Unframed

- Test Purpose

Verify that the IUT can receive an SDU with length &gt; the Isochronous PDU length.

- Reference

[3] 4.6.27

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts in the role specified in Table 4.7.
- -The CIS has been created.

- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval, ISO\_Interval, and Framing parameters are set as specified in Table 4.7.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- -If the corresponding BN is not 0, then Max\_SDU is set to 754 and Max\_PDU is set to 251.
- -If the corresponding BN is 0, then Max\_SDU is set to 0 and Max\_PDU is set to 0.
- Test Case Configuration
- Test Procedure

Table 4.7: Receive Large SDU, CIS, Unframed test cases

| Test Case | Role | NSE | Framing | P_To_C | P_To_C | C_To_P | C_To_P | SDU_Interval | ISO_ Interval |
| | | | | BN | FT | BN | FT | | |
| IAL/CIS/UNF/CEN/BV-12-C | Central | 6 | Unframed (0) | 4 | 2 | 0 | N/A | 25 ms (0x61A8) | 25 ms (0x14) |
| IAL/CIS/UNF/PER/BV-12-C | Peripheral | 10 | Unframed (0) | 0 | N/A | 8 | 2 | 20 ms (0x4E20) | 40 ms (0x20) |
| IAL/CIS/UNF/CEN/BV-36-C | Central | 12 | Unframed (0) | 8 | 3 | 0 | N/A | 25 ms (0x61A8) | 50 ms (0x28) |
| IAL/CIS/UNF/PER/BV-36-C | Peripheral | 6 | Unframed (0) | 0 | N/A | 4 | 3 | 25 ms (0x61A8) | 25 ms (0x14) |

Figure 4.5: Receive Large SDU, CIS, Unframed MSC

If the values of NSE, BN, or FT specified in Table 4.7 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, go to the Inconclusive verdict.

Repeat Steps 1 -3 for each round in Table 4.8.

1. The Lower Tester sends the IUT the specified number of Start/Continuation packets specified in Table 4.8 of ISO Data PDU with the LLID=0b01. If the BN value is not 0 in the direction from the IUT to the Lower Tester, then the IUT also sends payloads to the Lower Tester as configured in Table 4.8.
2. The Lower Tester sends the IUT the last ISO Data PDU with the LLID=0b00 with the remaining Payload Data.
3. The IUT sends an ISO Data packet to the Upper Tester with a data length specified in Table 4.8 and the data sent by the Lower Tester.

| Round | SDU Data Length | Start/Continuation packets |
| 1 | 753 | 2 |
| 2 | 754 | 3 |

Table 4.8: Receive Large SDU, CIS, Unframed rounds

- Expected Outcome

## Pass verdict

In Step 3, the IUT sends an SDU with data length as specified in Table 4.8.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.7.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.7.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.7.

## 4.3.7 Receive Large SDU, CIS, Framed

## · Test Purpose

Verify that the IUT can receive an SDU with length &gt; the Isochronous PDU length.

- Reference

[3] 4.6.27

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts in the role specified in Table 4.9.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval, ISO\_Interval, and Framing parameters are set as specified in Table 4.9.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- -If the corresponding BN is not 0, then Max\_SDU is set to 251 and Max\_PDU is set to 251.
- -If the corresponding BN is 0, then Max\_SDU is set to 0 and Max\_PDU is set to 0.

- Test Case Configuration
- Test Procedure

Table 4.9: Receive Large SDU, CIS, Framed test cases

| Test Case | Role | NSE | Framing | P_To_C | P_To_C | C_To_P | C_To_P | SDU_Interval | ISO_ Interval |
| | | | | BN | FT | BN | FT | | |
| IAL/CIS/FRA/CEN/BV-13-C | Central | 12 | Framed (1) | 7 | 2 | 0 | N/A | 25 ms (0x61A8) | 50 ms (0x28) |
| IAL/CIS/FRA/PER/BV-13-C | Peripheral | 6 | Framed (1) | 0 | N/A | 4 | 1 | 20 ms (0x4E20) | 25 ms (0x14) |
| IAL/CIS/FRA/CEN/BV-38-C | Central | 8 | Framed (1) | 5 | 2 | 0 | N/A | 22 ms (0x55F0) | 35 ms (0x1C) |
| IAL/CIS/FRA/PER/BV-38-C | Peripheral | 7 | Framed (1) | 4 | 1 | 4 | 2 | 40 ms (0x9C40) | 40 ms (0x20) |
| IAL/CIS/FRA/CEN/BV-49-C | Central | 1 | Framed (1) | 1 | 1 | 1 | 1 | 200 ms (0x30D40) | 50 ms (0x28) |
| IAL/CIS/FRA/PER/BV-49-C | Peripheral | 1 | Framed (1) | 1 | 1 | 1 | 1 | 200 ms (0x30D40) | 50 ms (0x28) |

Figure 4.6: Receive Large SDU, CIS, Framed MSC

If the values of NSE, BN, or FT specified in Table 4.9 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, go to the Inconclusive verdict.

Repeat Steps 1 -3 for each round in Table 4.10.

1. The Lower Tester sends the IUT the first fragment of SDU with LLID=0b10, SC set to 0, CMPLT set to 0.
2. The Lower Tester sends the IUT an ISO Data PDU containing the next SDU fragment with LLID=0b10, SC set to 1, and CMPLT set to 0. If the BN value is not 0 in the direction from the IUT to the Lower Tester, then the IUT also sends payloads to the Lower Tester as configured in Table 4.9. The bits in the RFU field of the Segmentation Header are set for framed payloads.
3. Repeat Step 2 'Number of Fragment(s)' 2 times as specified in Table 4.10.

4. The Lower Tester sends the IUT the last ISO Data PDU with the LLID=0b10, SC set to 1, CMPLT set to 1, with the remaining Payload Data. The bits in the RFU field of the Segmentation Header are set for framed payloads.
5. The IUT sends an ISO Data packet to the Upper Tester with a data length specified in Table 4.10 and the data sent by the Lower Tester.
- Expected Outcome

Table 4.10: Receive Large SDU, CIS, Framed rounds

| Round | SDU Data Length | Number of Fragment(s) |
| 1 | 744 | 3 |
| 2 | 745 | 4 |

## Pass verdict

In Step 5, the IUT sends an SDU with data length as specified in Table 4.10.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.9.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.9.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.9.

## 4.3.8 Receive Multiple, Small SDUs, CIS

- Test Purpose

Verify that the IUT can receive a single ISOC Data PDU and sends multiple smaller SDUs to the Upper Tester.

- Reference

[3] 4.6.27

[4] 2.2

- Initial Condition
- -The IUT acts in the role as specified in Table 4.11.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval, ISO\_Interval, and Framing = Framed(1) parameters are set as specified in Table 4.11.
- -If the corresponding BN is not 0 then Max\_SDU is set to 25 and Max\_PDU is set to 68.
- -If the corresponding BN is 0 then Max\_SDU is set to 0 and Max\_PDU is set to 0.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.

- Test Case Configuration
- Test Procedure

Table 4.11: Receive Multiple, Small SDUs, CIS test cases

| Test Case | Role | NSE | P_To_C | P_To_C | C_To_P | C_To_P | SDU_Interval | ISO_Interval |
| | | | BN | FT | BN | FT | | |
| IAL/CIS/FRA/CEN/BV-15-C | Central | 2 | 1 | 1 | 0 | N/A | 10 ms (0x2710) | 5 ms (0x04) |
| IAL/CIS/FRA/PER/BV-15-C | Peripheral | 2 | 0 | N/A | 1 | 4 | 10 ms (0x2710) | 5 ms (0x04) |
| IAL/CIS/FRA/CEN/BV-39-C | Central | 4 | 2 | 1 | 2 | 2 | 20 ms (0x4E20) | 10 ms (0x08) |
| IAL/CIS/FRA/PER/BV-39-C | Peripheral | 7 | 0 | N/A | 3 | 4 | 10 ms (0x2710) | 10 ms (0x08) |
| IAL/CIS/FRA/CEN/BV-50-C | Central | 1 | 1 | 1 | 1 | 1 | 20 ms (0x4E20) | 40 ms (0x20) |
| IAL/CIS/FRA/PER/BV-50-C | Peripheral | 1 | 1 | 1 | 1 | 1 | 10 ms (0x2710) | 20 ms (0x10) |

Figure 4.7: Receive Multiple, Small SDUs, CIS MSC

If the values of NSE, BN, or FT specified in Table 4.11 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, then go to the Inconclusive verdict.

1. The Lower Tester sends a single PDU to the IUT with a data length of 55 bytes.
2. The IUT sends an SDU1 packet to the Upper Tester with a data length of 20 bytes.
3. The IUT sends an SDU2 packet to the Upper Tester with a data length of 25 bytes.
- Expected Outcome

## Pass verdict

In Step 1, the IUT receives a PDU with two SDUs. In each SDU header SC = 0 and CMPLT = 1.

In Step 2, the IUT sends an SDU with the data for SDU1 from Step 1.

In Step 3, the IUT sends an SDU with the data for SDU2 from Step 1.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.11.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.11.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.11.

## 4.3.9 Send a Zero-Length SDU, CIS

- Test Purpose

Verify that the IUT can send a zero-length SDU.

- Reference

[3] 4.6.27 [4] 2.1, 2.2, 3.1

- Initial Condition
- -The IUT acts in the role as specified in Table 4.12.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, and Framing parameters are set as specified in Table 4.12. Framing is set to 0x00 if the test is Unframed, 0x01 if the test is Framed, Segmentable mode, and 0x02 if the test is Framed, Unsegmented mode. ISO\_Interval and SDU\_Interval are both set to 10 milliseconds. Max\_PDU\_C\_To\_P and Max\_PDU\_P\_To\_C are both set to 20 when BN in the corresponding direction is not 0, and to 0 when BN in the corresponding direction is 0.
- -Max\_SDU\_C\_To\_P and Max\_SDU\_P\_To\_C are the maximum SDU size as defined by the bandwidth requirements specified in [4] Section 2.1 for unframed PDUs and Section 2.2 for framed PDUs.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.

## · Test Case Configuration

| Case | Role | NSE | Framed | Framing_ Mode | LLID | P_To_C | P_To_C | C_To_P | C_To_P | Segmentation Header | Time Offset |
| Case | Role | NSE | Framed | Framing_ Mode | LLID | BN | FT | BN | FT | Segmentation Header | Time Offset |
| IAL/CIS/UNF/CEN/BV-17-C | Central | 4 | 0 | 0 | 0b00 | 0 | N/A | 2 | 2 | N/A | N/A |
| IAL/CIS/UNF/PER/BV-17-C | Peripheral | 7 | 0 | 0 | 0b00 | 3 | 4 | 0 | N/A | N/A | N/A |
| IAL/CIS/UNF/CEN/BV-41-C | Central | 1 | 0 | 0 | 0b00 | 0 | N/A | 1 | 1 | N/A | N/A |
| IAL/CIS/UNF/PER/BV-41-C | Peripheral | 2 | 0 | 0 | 0b00 | 1 | 3 | 1 | 2 | N/A | N/A |
| IAL/CIS/FRA/CEN/BV-18-C | Central | 5 | 1 | 0 | 0b10 | 0 | N/A | 2 | 2 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/CIS/FRA/PER/BV-18-C | Peripheral | 2 | 1 | 0 | 0b10 | 1 | 4 | 0 | N/A | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/CIS/FRA/CEN/BV-42-C | Central | 2 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/CIS/FRA/PER/BV-42-C | Peripheral | 5 | 1 | 0 | 0b10 | 1 | 2 | 3 | 3 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/CIS/UNF/PER/BV-49-C | Peripheral | 1 | 0 | 0 | 0b00 | 1 | 1 | 1 | 1 | N/A | N/A |
| IAL/CIS/FRA/CEN/BV-51-C | Central | 1 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/CIS/FRA/PER/BV-51-C | Peripheral | 1 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/CIS/FRA/CEN/BV-55-C | Central | 5 | 1 | 1 | 0b10 | 0 | N/A | 2 | 2 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/CIS/FRA/PER/BV-55-C | Peripheral | 2 | 1 | 1 | 0b10 | 1 | 4 | 0 | N/A | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |

Table 4.12: Send Zero-Length SDU, CIS test cases

- Test Procedure

Figure 4.8: Send Zero-Length SDU, CIS MSC

If the values of NSE, BN, or FT specified in Table 4.12 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, go to the Inconclusive verdict.

1. The Upper Tester sends an HCI ISO Data packet to the IUT with zero data length.
2. The IUT sends a single ISO Data PDU to the Lower Tester with the LLID, Framed, and Framing\_Mode as specified in Table 4.12, the segmentation header and time offset fields as specified in Table 4.12. Length is 0 if LLID is 0b00 and is 5 (Segmentation Header + TimeOffset) if LLID is 0b10. SDU field is empty. NPI is set to 0b00.
- Expected Outcome

## Pass verdict

The IUT sends a single ISO Data PDU with the LLID, segmentation header, and time offset fields as specified in Table 4.12 and an empty SDU.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.12.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.12.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.12.

## 4.3.10 Receive a Zero-Length SDU, CIS

- Test Purpose

Verify that the IUT can receive a zero-length SDU. If the Time\_Stamp is included in the ISO Data packet, then verify that the value is equal to the sync reference calculated according to either [4] Section 3.2.1 for framed PDUs or [4] Section 3.2.2 for unframed PDUs.

- Reference
- Initial Condition
- -The IUT acts in the role as specified in Table 4.13.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, and Framing parameters are set as specified in Table 4.13. Framing is

[3] 4.6.27

[4] 2.1, 2.2, 3.1

set to 0x00 if the test is Unframed, 0x01 if the test is Framed, Segmentable mode and 0x02 if the test is Framed, Unsegmented mode. ISO\_Interval and SDU\_Interval are both chosen by the tester. Max\_PDU\_C\_To\_P and Max\_PDU\_P\_To\_C are both set to 20 when BN in the corresponding direction is not 0, and to 0 when BN in the corresponding direction is 0.

- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.

## · Test Case Configuration

| Test Case | Role | NSE | Framed | Framing _Mode | LLID | P_To_C | P_To_C | C_To_P | C_To_P | Segmentation Header | Time_ Offset and Time_ Stamp |
| Test Case | Role | NSE | Framed | Framing _Mode | LLID | BN | FT | BN | FT | Segmentation Header | Time_ Offset and Time_ Stamp |
| IAL/CIS/UNF/CEN/BV-19-C | Central | 7 | 0 | 0 | 0b00 | 3 | 4 | 0 | N/A | N/A | N/A |
| IAL/CIS/UNF/PER/BV-19-C | Peripheral | 4 | 0 | 0 | 0b00 | 0 | N/A | 2 | 2 | N/A | N/A |
| IAL/CIS/UNF/CEN/BV-43-C | Central | 2 | 0 | 0 | 0b00 | 1 | 3 | 1 | 2 | N/A | N/A |
| IAL/CIS/UNF/PER/BV-43-C | Peripheral | 1 | 0 | 0 | 0b00 | 0 | N/A | 1 | 1 | N/A | N/A |
| IAL/CIS/FRA/CEN/BV-20-C | Central | 2 | 1 | 0 | 0b10 | 1 | 4 | 0 | N/A | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |
| IAL/CIS/FRA/PER/BV-20-C | Peripheral | 5 | 1 | 0 | 0b10 | 0 | N/A | 2 | 2 | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |
| IAL/CIS/FRA/CEN/BV-44-C | Central | 5 | 1 | 0 | 0b10 | 1 | 2 | 3 | 3 | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |
| IAL/CIS/FRA/PER/BV-44-C | Peripheral | 2 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |
| IAL/CIS/UNF/CEN/BV-48-C | Central | 1 | 0 | 0 | 0b00 | 1 | 1 | 1 | 1 | N/A | N/A |
| IAL/CIS/FRA/CEN/BV-52-C | Central | 1 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |
| IAL/CIS/FRA/PER/BV-52-C | Peripheral | 1 | 1 | 0 | 0b10 | 1 | 1 | 1 | 1 | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |

| Test Case | Role | NSE | Framed | Framing _Mode | LLID | P_To_C | P_To_C | C_To_P | C_To_P | Segmentation Header | Time_ Offset and Time_ Stamp |
| Test Case | Role | NSE | Framed | Framing _Mode | LLID | BN | FT | BN | FT | Segmentation Header | Time_ Offset and Time_ Stamp |
| IAL/CIS/FRA/CEN/BV-56-C | Central | 2 | 1 | 1 | 0b10 | 1 | 4 | 0 | N/A | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |
| IAL/CIS/FRA/PER/BV-56-C | Peripheral | 5 | 1 | 1 | 0b10 | 0 | N/A | 2 | 2 | SC=0 CMPLT=1 LENGTH=length of Time_Offset | Yes |

Table 4.13: Receive Zero-Length SDU, CIS test cases

- Test Procedure

Figure 4.9: Receive Zero-Length SDU, CIS MSC

If the values of NSE, BN, or FT specified in Table 4.13 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively, go to the Inconclusive verdict.

1. The Lower Tester sends a single ISO Data PDU to the IUT with no data and with the LLID, Framed, and Framing\_Mode as specified in Table 4.13 and with the segmentation header and Time\_Offset fields as specified in Table 4.13.
2. The IUT sends an empty ISO Data packet to the Upper Tester. If Framed PDUs are used, but the Time\_Stamp field is not included, the Lower Tester sends a warning.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an empty SDU. If present, the Time\_Stamp field is equal to the SDU sync reference defined in either [4] Section 3.2.1 for framed PDUs or [4] Section 3.2.2 for unframed PDUs.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of NSE specified in Table 4.13.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.13.

TSPX\_max\_cis\_ft is less than the value of FT specified in Table 4.13.

## 4.3.11 Receive an Unsuccessful Large SDU, CIS

- Test Purpose

Verify that the IUT sends an ISO Data packet to the Upper Tester with a Packet\_Status\_Flag error when receiving Isochronous PDUs with SDU data length &gt; Isochronous PDU length and one of the continuation PDU packets fails to be received, when no PDUs are received, and when an invalid sequence of PDUs is received.

- Reference

[3] 4.6.27

[4] 2.1

- Initial Condition
- -The IUT acts in the role as specified in Table 4.14.
- -The CIS has been created.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.

- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- -In the LE Set CIG Parameters Test Command, the parameter NSE is set to 0x04, CIS\_Count is 1, Framing is 0x00, FT\_C\_To\_P and FT\_P\_To\_C are set to 0x01, and the BN\_P\_To\_C and BN\_C\_To\_P parameters are set as specified in Table 4.14. Max\_SDU\_C\_To\_P, Max\_SDU\_P\_To\_C, Max\_PDU\_C\_To\_P, and Max\_PDU\_P\_To\_C are set to valid values that support fragmenting the SDU across 4 PDUs, and the SDU size in the direction of data transfer is the largest permissible value. The SDU intervals and ISO interval are set to valid values.
- Test Case Configuration

Table 4.14: Receive an Unsuccessful Large SDU, CIS test cases

| Test Case | Role | BN_P_To_C | BN_C_To_P |
| IAL/CIS/UNF/CEN/BI-02-C | Central | 0x04 | 0x00 |
| IAL/CIS/UNF/PER/BI-02-C | Peripheral | 0x00 | 0x04 |
| IAL/CIS/UNF/CEN/BI-03-C | Central | 0x04 | 0x04 |
| IAL/CIS/UNF/PER/BI-03-C | Peripheral | 0x04 | 0x04 |

## · Test Procedure

Figure 4.10: Receive an Unsuccessful Large SDU, CIS MSC

If TSPX\_max\_cis\_nse is less than 4 or TSPX\_max\_cis\_bn is less than 4, go to the Inconclusive verdict.

The rounds in Table 4.15 are performed in any order in consecutive isochronous events. In each round:

1. The Lower Tester sends the IUT the PDUs listed in Table 4.15.
2. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag=0b01 or Packet\_Status\_Flag=0b10. If Packet\_Status\_Flag=0b10, then PB\_Flag=0b10, ISO\_SDU\_Length=0, and there is no data.

Table 4.15: Receive an Unsuccessful Large SDU, CIS rounds

| Round | PDUs sent |
| 1 | 4 PDUs with LLID=0b01 and no data |
| 2 | 4 PDUs with LLID=0b01 and data |
| 3 | 3 PDUs with LLID=0b01 and data, then 1 PDU with LLID=0b00 and data; one of the first three PDUs has a CRC error |
| 4 | 2 PDUs with LLID=0b01 and data, then 2 PDUs with LLID=0b00 and data |
| 5 | 2 PDUs with LLID=0b01 and no data, then 1 PDU with LLID=0b00 and data, then 1 PDU with LLID=0b01 and data |
| 6 | 2 PDUs with LLID=0b01 and no data, then 1 PDU with LLID=0b00 and data, then 1 PDU with LLID=0b10 and no data |
| 7 | 2 PDUs with LLID=0b01 and no data, then 1 PDU with LLID=0b10 and data, then 1 PDU with LLID=0b00 and no data |
| 8 | 2 PDUs with LLID=0b01 and data, then 1 PDU with LLID=0b00 and data; one of the four PDUs is omitted to simulate losing one PDU |
| 9 | 1 PDU with LLID=0b00 and data, then 3 PDUs with LLID=0b01, at least one of which has data |
| 10 | No PDUs |

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an ISO Data packet with Packet\_Status\_Flag=0b01 or Packet\_Status\_Flag=0b10. If Packet\_Status\_Flag=0b10, then PB\_Flag=0b10, ISO\_SDU\_Length=0, and there is no data.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than 4.

TSPX\_max\_cis\_bn is less than 4.

## 4.3.12 Simultaneous Sending and Receiving SDUs, CIS

- Test Purpose

Verify that the IUT can simultaneously send and receive SDUs with the Lower Tester.

- Reference

[3] 4.6.27

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts in the role as specified in Table 4.16.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, and Framing parameters are set as specified in Table 4.16.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.

- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- Test Case Configuration

Table 4.16: Simultaneous Sending and Receiving SDUs, CIS test cases

| Test Case | Role | NSE | Framing | P_To_C | P_To_C | C_To_P | C_To_P |
| | | | | BN | FT | BN | FT |
| IAL/CIS/UNF/CEN/BV-21-C | Central | 2 (see Note 1) | Unframed (0) | 1 | 1 | 1 | 1 |
| IAL/CIS/UNF/PER/BV-21-C | Peripheral | 2 (see Note 1) | Unframed (0) | 1 | 1 | 1 | 1 |
| IAL/CIS/UNF/CEN/BV-24-C | Central | 3 | Unframed (0) | 1 | 2 | 2 | 3 |
| IAL/CIS/UNF/PER/BV-24-C | Peripheral | 3 | Unframed (0) | 1 | 2 | 2 | 3 |
| IAL/CIS/FRA/CEN/BV-22-C | Central | 5 | Framed (1) | 1 | 2 | 3 | 3 |
| IAL/CIS/FRA/PER/BV-22-C | Peripheral | 5 | Framed (1) | 1 | 2 | 3 | 3 |

Note 1: If TSPX\_max\_cis\_nse is 1, then an NSE of 1 is used.

- Test Procedure

Figure 4.11: Simultaneous Sending and Receiving SDUs, CIS MSC

If the specified value of NSE is larger than TSPX\_max\_cis\_nse (does not apply if Note 1 in Table 4.16 is applicable), or the specified value of BN in either or both directions exceeds TSPX\_max\_cis\_bn, or the specified value of FT in either or both directions exceeds TSPX\_max\_cis\_ft, then refer to the Inconclusive verdict.

1. The Upper Tester sends HCI ISO Data packets to the IUT.
2. The IUT sends ISO Data PDUs to the Lower Tester.
3. At the same time, the Lower Tester sends ISO Data PDUs to the IUT.
4. The IUT sends Isochronous Data SDUs to the Upper Tester.

- Expected Outcome

## Pass Verdict

The IUT sends ISO Data PDUs to the Lower Tester with the data received in Step 1 and sends Isochronous Data SDUs to the Upper Tester with the data received in Step 3.

## Inconclusive verdict

The specified value of NSE is larger than TSPX\_max\_cis\_nse. This does not apply if Note 1 in Table 4.16 is applicable.

The specified value of BN in either or both directions exceeds TSPX\_max\_cis\_bn.

The specified value of FT in either or both directions exceeds TSPX\_max\_cis\_ft.

## 4.3.13 Sending and Receiving Unframed Empty PDUs with LLID=0b01, CIS

- Test Purpose

Test that the IUT can send and receive unframed empty PDUs with LLID = 0b01 when the number of required PDUs to transmit an SDU is less than BN×(SDU\_Interval÷ISO\_Interval) fragment PDUs.

- Reference

[3] 4.6.27

[4] 2.1

- Initial Condition
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -Connected in the relevant role per Table 4.18 as defined in the following initial states:
- -State: Connected Isochronous Stream (values as specified in Table 4.17)

| State Variable | Value(s) |
| sdu_int_C_To_P | 0x186A0 (100 ms) |
| sdu_int_P_To_C | 0x186A0 (100 ms) |
| ft_C_To_P | 1 |
| ft_P_To_C | 1 |
| iso_int | 0x50 (100 ms) |
| packing | Sequential (0x00) |
| framing | Unframed (0x00) |
| cis_cnt | 1 |
| nse[] | per Table 4.18 |
| mx_sdu_C_To_P [] | 128 |
| mx_sdu_P_To_C [] | 128 |
| mx_pdu_C_To_P [] | 128 |
| mx_pdu_P_To_C [] | 128 |

Table 4.17: State Variable Values

| State Variable | Value(s) |
| phy_C_To_P [] | 0x01 |
| phy_P_To_C [] | 0x01 |
| bn_C_To_P [] | per BN value specified in Table 4.18 |
| bn_P_To_C [] | per BN value specified in Table 4.18 |

- Test Case Configuration

Table 4.18: Sending and Receiving Unframed Empty PDUs with LLID=0b01, CIS test cases

| Test Case | Role | BN | NSE (see Note 1) |
| IAL/CIS/UNF/CEN/BV-45-C | Central | 0x04 | 0x08 |
| IAL/CIS/UNF/PER/BV-45-C | Peripheral | 0x04 | 0x08 |
| IAL/CIS/UNF/PER/BV-46-C | Peripheral | 0x06 | 0x0C |

Note 1: If TSPX\_max\_cis\_nse is less than the specified value of NSE, then NSE is TSPX\_max\_cis\_nse. If the resulting value of NSE is less than the specified value of BN, then refer to the Inconclusive verdict.

## · Test Procedure

Figure 4.12: Sending and Receiving Unframed Empty PDUs with LLID=0b01, CIS MSC

If TSPX\_max\_cis\_nse is less than the value of BN specified in Table 4.18 or TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.18, then refer to the Inconclusive verdict.

1. The Upper Tester submits an SDU at its SDU interval of variable length, ranging from 4 to 128 octets. Note that the Test Command Generated Isochronous SDUs Optional Test Steps, ALT 3, VARIABLE LENGTH PAYLOADS in [9] Section 4.1.6.7.3 may be used for this purpose.

Steps 2 and 3 describe an exchange of data between the Central and Peripheral during a CIS event.

2. The Lower Tester receives PDUs from the IUT. When the required number of PDUs to transmit the SDU is less than BN PDUs, the remainder of BN PDUs are empty PDUs with LLID=0b01.
3. The Lower Tester sends PDUs based on an SDU of variable length, ranging from 4 to 128 octets. When the required number of PDUs to transmit the SDU is less than BN PDUs, the remainder of BN PDUs are empty PDUs with LLID=0b01.
4. The IUT sends the variable length SDUs from the Lower Tester to the Upper Tester.
5. Repeat Steps 1 -4 a minimum of 32 times.

- Expected Outcome

## Pass verdict

The IUT sends empty PDUs with LLID=0b01 as required.

The IUT receives at least 32 variable length SDUs from the Lower Tester.

## Inconclusive verdict

TSPX\_max\_cis\_nse is less than the value of BN specified in Table 4.18.

TSPX\_max\_cis\_bn is less than the value of BN specified in Table 4.18.

## 4.3.14 SDU Reporting, CIS, Unframed PDU

- Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Connected Isochronous Stream, Unframed.

- Reference

[3] 4.6.27 [4] 2.1 [11] 4

- Initial Condition
- -The IUT acts in the role as specified in Table 4.19.
- -The CIS has been created.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_ft is the maximum supported FT as defined in the IXIT [8] entry.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, and FT\_P\_To\_C values are set as specified in Table 4.19.

## · Test Case Configuration

| Test Case | Role | NSE | P_To_C | P_To_C | P_To_C | P_To_C | C_To_P | C_To_P | C_To_P | C_To_P |
| | | | BN | FT | Max_SDU | Max_PDU | BN | FT | Max_SDU | Max_PDU |
| IAL/CIS/UNF/CEN/BI-04-C | Central | 4 | 4 | 1 | 128 (0x0080) | 32 (0x0020) | 0 | 1 | 0 | 0 |
| IAL/CIS/UNF/PER/BI-04-C | Peripheral | 4 | 0 | 1 | 0 | 0 | 4 | 1 | 128 (0x0080) | 32 (0x0020) |

Table 4.19: SDU Reporting, CIS, Unframed PDU test cases

## · Test Procedure

Figure 4.13: SDU Reporting, CIS, Unframed PDU MSC

1. The Lower Tester sends the IUT 2 unframed Start/Continuation ISO Data PDUs to the IUT with the LLID=0b01.
2. The Lower Tester sends the IUT 1 unframed Start/Continuation ISO Data PDU with an invalid CRC.
3. The Lower Tester sends the IUT the last unframed ISO Data PDU to the IUT with the LLID=0b00 and with the remaining Payload Data.
4. Perform either alternative 4A or 4B depending on how the IUT reports the SDU:

Alternative 4A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 4A.1 The IUT sends an ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 4B (The IUT reports the SDU as 0b10 'lost data'):

- 4B.1 The IUT sends an ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

5. The Lower Tester sends unframed ISO Data PDUs to the IUT with all LLID = 0b01.
2. 6.
3. Perform either alternative 6A or 6B depending on how the IUT reports the SDU:

Alternative 6A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 6A.1 The IUT sends an ISO Data packet with the truncated SDU data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 6B (The IUT reports the SDU as 0b10 'lost data'):

- 6B.1 The IUT sends an ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.
- Expected Outcome

## Pass verdict

In Step 4A.1, the IUT sends an ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 4B.1, the IUT sends an SDU to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

In Step 6A.1, the IUT sends an ISO Data packet with the truncated SDU data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 6B.1, the IUT sends an ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.

## Inconclusive verdict

The values of NSE, BN, or FT specified in Table 4.19 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively.

## 4.3.15 SDU Reporting, CIS, Unframed PDU, BN = 1, NSE = 1

- Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Connected Isochronous Stream with BN = 1 and NSE = 1, Unframed.

- Reference

[3] 4.6.27 [4] 2.1 [11] 4

- Initial Condition
- -The IUT acts in the role specified in Table 4.20.
- -The CIS has been created.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, and FT\_P\_To\_C values are set as specified in Table 4.20.

## · Test Case Configuration

| Test Case | Role | NSE | P_To_C | P_To_C | P_To_C | P_To_C | C_To_P | C_To_P | C_To_P | C_To_P |
| | | | BN | FT | Max_SDU | Max_PDU | BN | FT | Max_SDU | Max_PDU |
| IAL/CIS/UNF/CEN/BI-05-C | Central | 1 | 1 | 1 | 32 (0x0020) | 32 (0x0020) | 0 | 1 | 0 | 0 |
| IAL/CIS/UNF/PER/BI-05-C | Peripheral | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 32 (0x0020) | 32 (0x0020) |

Table 4.20: SDU Reporting, CIS, Unframed PDU, BN = 1, NSE = 1 test cases

- Test Procedure
1. The Lower Tester sends the IUT 1 unframed Start/Continuation ISO Data PDU with LLID=0b00 and an invalid CRC.
2. Perform either alternative 2A or 2B depending on how the IUT reports the SDU:

Figure 4.14: SDU Reporting, CIS, Unframed PDU, BN = 1, NSE = 1 MSC

Alternative 2A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 2A.1 The IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 2B (The IUT reports the SDU as 0b10 'lost data'):

- 2B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.
3. The Lower Tester sends unframed ISO Data PDUs to the IUT with LLID=0b01.
4. Perform either alternative 4A or 4B depending on how the IUT reports the SDU:

Alternative 4A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 4A.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the truncated SDU data with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 4B (The IUT reports the SDU as 0b10 'lost data'):

- 4B.1 The IUT sends an SDU to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 2B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

In Step 4A.1, the IUT sends an HCI ISO Data packet with the truncated SDU data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 4B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.

## 4.3.16 SDU Reporting, CIS, Framed PDU

## · Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Connected Isochronous Stream, Framed.

- Reference

[3] 4.6.27

[4] 2.2

## 11 4

- Initial Condition
- -The CIS has been created.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, and FT\_P\_To\_C values are set as specified in Table 4.21.

## · Test Case Configuration

| Test Case | Role | NSE | P_To_C | P_To_C | P_To_C | P_To_C | C_To_P | C_To_P | C_To_P | C_To_P |
| | | | BN | FT | Max_SDU | Max_PDU | BN | FT | Max_SDU | Max_PDU |
| IAL/CIS/FRA/CEN/BI-01-C | Central | 4 | 4 | 1 | 108 (0x006C) | 32 (0x0020) | 0 | 1 | 0 | 0 |
| IAL/CIS/FRA/PER/BI-01-C | Peripheral | 4 | 0 | 1 | 0 | 0 | 4 | 1 | 108 (0x006C) | 32 (0x0020) |

Table 4.21: SDU Reporting, CIS, Framed PDU test cases

## · Test Procedure

Figure 4.15: SDU Reporting, CIS, Framed PDU MSC

1. The Lower Tester sends 1 framed ISO Data PDU to the IUT with SC set to 0 and CMPLT set to 0.
2. The Lower Tester sends 1 framed ISO Data PDU to the IUT with SC set to 1 and CMPLT set to 0.
3. The Lower Tester sends 1 framed ISO Data PDU to the IUT with SC set to 1, CMPLT set to 0, and the Length field in the Segmentation Header set to 255.
4. The Lower Tester sends the last framed ISO Data PDU to the IUT with SC set to 1 and CMPLT set to 1 with the remaining Payload Data.
5. Perform either alternative 5A or 5B depending on how the IUT reports the SDU:

Alternative 5A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 5A.1 The IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 5B (The IUT reports the SDU as 0b10 'lost data'):

- 5B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.
- Expected Outcome

## Pass verdict

In Step 5A.1, the IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 5B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

## Inconclusive verdict

The values of NSE, BN, or FT specified in Table 4.21 exceed the corresponding values of TSPX\_max\_cis\_nse, TSPX\_max\_cis\_bn, or TSPX\_max\_cis\_ft, respectively.

## 4.3.17 SDU Reporting, CIS, Framed PDU, BN = 1, NSE = 1

- Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Connected Isochronous Stream with BN = 1 and NSE = 1, Framed.

- Reference

[3] 4.6.27 [4] 2.2 [11] 4

- Initial Condition
- -The CIS has been created.
- -TSPX\_max\_cis\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_cis\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -In the LE Set CIG Parameters Test Command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, and FT\_P\_To\_C values are set as specified in Table 4.22.

## · Test Case Configuration

| Test Case | Role | NSE | P_To_C | P_To_C | P_To_C | P_To_C | C_To_P | C_To_P | C_To_P | C_To_P |
| | | | BN | FT | Max_SDU | Max_PDU | BN | FT | Max_SDU | Max_PDU |
| IAL/CIS/FRA/CEN/BI-02-C | Central | 1 | 1 | 1 | 32 (0x0020) | 45 (0x002D) | 0 | 1 | 0 | 0 |
| IAL/CIS/FRA/PER/BI-02-C | Peripheral | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 32 (0x0020) | 40 (0x0028) |

Table 4.22: SDU Reporting, CIS, Framed PDU, BN = 1, NSE = 1 test cases

- Test Procedure
1. The Lower Tester sends 1 framed ISO Data PDU to the IUT with SC set to 0, CMPLT set to 1, and the Length field in the Segmentation Header set to 255.
2. Perform either alternative 2A or 2B depending on how the IUT reports the SDU:

Figure 4.16: SDU Reporting, CIS, Framed PDU, BN = 1, NSE = 1 MSC

Alternative 2A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 2A.1 The IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 2B (The IUT reports the SDU as 0b10 'lost data'):

- 2B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.
- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 2B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

## 4.3.18 Receive an SDU Larger than a PDU, CIS, Unframed

- Test Purpose

Verify that the IUT can receive an SDU with length &gt; the Isochronous PDU length, when two PDUs are required to transport an SDU.

- Reference

[3] 4.6.27

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts in the role specified in Table 4.23.
- -The CIS has been created.

- -In the LE Set CIG Parameters test command, the NSE, BN\_P\_To\_C, BN\_C\_To\_P, FT\_C\_To\_P, FT\_P\_To\_C, SDU\_Interval, ISO\_Interval, and Framing parameters are set as specified in Table 4.23.
- -If the corresponding BN is not 0, then Max\_PDU is set to 251 and Max\_SDU is set to Max\_PDU + 1.
- -If the corresponding BN is 0, then Max\_SDU is set to 0 and Max\_PDU is set to 0.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends the IUT an ISO Data PDU with the LLID=0b01 and Max\_PDU octets of data.
2. The Lower Tester sends the IUT an ISO Data PDU with the LLID=0b00 and 1 octet of data.
3. The IUT sends a Max\_SDU octet ISO Data packet to the Upper Tester.
- Expected Outcome

Table 4.23: Receive an SDU Larger than a PDU, CIS, Unframed test cases

| Test Case | Role | NSE | Framing | P_To_C | P_To_C | C_To_P | C_To_P | SDU_ Interval | ISO_ Interval |
| | | | | BN | FT | BN | FT | | |
| IAL/CIS/UNF/CEN/BV-49-C | Central | 2 | Unframed (0) | 2 | 1 | 0 | N/A | 25 ms (0x61A8) | 25 ms (0x14) |
| IAL/CIS/UNF/PER/BV-50-C | Peripheral | 2 | Unframed (0) | 0 | N/A | 2 | 1 | 25 ms (0x61A8) | 25 ms (0x14) |

Figure 4.17: Receive an SDU Larger than a PDU, CIS, Unframed MSC

## Pass verdict

The IUT sends a Max\_SDU octet SDU to the Upper Tester.

## 4.3.19 Reporting an Unsuccessful Large SDU, Framed CIS

- Test Purpose

Verify that the IUT sends an ISO Data packet to the Upper Tester with a Packet\_Status\_Flag error value of 0b10 when some PDU packets in an SDU are not received.

- Reference

[12] 2.2

- Initial Condition
- -The IUT acts in the role specified in Table 4.24.
- -An unencrypted CIG has been created with NSE = 2, CIS\_Count = 1, Framing = 0x01, FT\_C\_To\_P and FT\_P\_To\_C set to 0x01, and BN\_P\_To\_C and BN\_C\_To\_P set as specified in Table 4.24.
- -Max\_SDU\_C\_To\_P and Max\_SDU\_P\_To\_C are set to 16 when BN&gt;0 and 0 when BN=0.
- -Max\_PDU\_C\_To\_P and Max\_PDU\_P\_To\_C are set to 16 when BN&gt;0 and 0 when BN=0.
- -The SDU interval and ISO interval are set to the same values.
- Test Case Configuration

| Test Case | Role | BN_P_To_C | BN_C_To_P |
| IAL/CIS/FRA/CEN/BI-03-C | Central | 0x02 | 0x00 |
| IAL/CIS/FRA/PER/BI-03-C | Peripheral | 0x00 | 0x02 |

Table 4.24: Reporting an Unsuccessful Large SDU, Framed CIS test cases

## · Test Procedure

Figure 4.18: Report an Unsuccessful Large SDU, Framed CIS MSC

Perform Step 1A four times, Step 1B four times, and Step 1C four times, in 12 consecutive isochronous events. The order of the 12 steps is selected at random.

- 1A. The Lower Tester sends two ISO Data PDUs to the IUT with the LLID = 0b10 in the same isochronous interval. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag = 0b00 and PB\_Flag = 0b10 and containing all the data.
- 1B. The Lower Tester sends an ISO Data PDU with the LLID = 0b10 in the first sub-event of an ISO interval and nothing in the second sub-event. The IUT sends the Upper Tester an ISO Data packet either with Packet\_Status\_Flag = 0b01 and containing the data, or with Packet\_Status\_Flag = 0b10 and ISO\_SDU\_Length = 0 and with no data.
- 1C. The Lower Tester sends nothing in the first sub-event of an ISO interval and an ISO Data PDU with the LLID = 0b10 in the second sub-event. The IUT sends the Upper Tester an ISO Data packet either with Packet\_Status\_Flag = 0b01 and containing the data, or with Packet\_Status\_Flag = 0b10 and ISO\_SDU\_Length = 0 and with no data.
- Expected Outcome

## Pass verdict

In at least 10 of the 12 events, the IUT sends an ISO Data packet to the Upper Tester with the proper Packet\_Status\_Flag, ISO\_SDU\_Length, and ISO Data.

## 4.3.20 Reporting a missing or damaged SDU, Framed CIS

- Test Purpose

Verify that the IUT sends an ISO Data packet to the Upper Tester with a Packet\_Status\_Flag error value of 0b10 when all PDU packets in an SDU are not received and the SDU is discarded.

- Reference

[12] 2.2

- Initial Condition
- -The IUT acts in the role specified in Table 4.25.
- -An unencrypted CIG has been created with NSE = 1, CIS\_Count = 1, Framing = 0x01, FT\_C\_To\_P and FT\_P\_To\_C set to 0x01, and BN\_P\_To\_C and BN\_C\_To\_P set as specified in Table 4.25.
- -Max\_PDU\_C\_To\_P and Max\_PDU\_P\_To\_C are set to Max\_SDU + 13 when BN&gt;0 and 0 when BN=0.
- -The SDU interval and ISO interval are set to the same values.
- Test Case Configuration

| Test Case | Role | BN_P_To_C | BN_C_To_P |
| IAL/CIS/FRA/CEN/BI-04-C | Central | 0x01 | 0x00 |
| IAL/CIS/FRA/PER/BI-04-C | Peripheral | 0x00 | 0x01 |

Table 4.25: Reporting a missing or damaged SDU, Framed CIS test cases

- Test Procedure

Figure 4.19: Reporting a missing or damaged SDU, Framed CIS MSC

Perform Step 1A five times and Step 1B five times, in 10 consecutive isochronous events. The order of the 10 steps is selected at random.

- 1A. The Lower Tester sends an ISO Data PDU to the IUT with the LLID = 0b10. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag = 0b00 and PB\_Flag = 0b10 and containing all the data.
- 1B. The Lower Tester sends an ISO Null PDU. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag = 0b10 and ISO\_SDU\_Length = 0 and with no data.
- Expected Outcome

## Pass verdict

In at least 9 of the 10 repeats, the IUT sends an ISO Data packet to the Upper Tester with the proper Packet\_Status\_Flag, ISO\_SDU\_Length, and ISO Data.

## IAL/CIS/FRA/CEN/BV-58-C [Unsegmented Framed LL PDUs at 7.5 ms ISO Interval]

- Test Purpose

Verify that an IUT receiving ISO Data Packets at 10 ms SDU Intervals sends them as unsegmented framed LL PDUs across three of four 7.5 ms ISO Intervals.

- Reference

[13] 2

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The IUT is in the Central role.

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters\_Test command to the IUT with Framing set to 0x02 (Unsegmented Framed) and all other parameters set as default and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Create\_CIS command to create a single CIS and receives a successful HCI\_Command\_Status in response.
3. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with Framed set to 1 and Framing\_Mode set to 1.
4. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
5. The IUT sends an LL\_CIS\_IND PDU to the Lower Tester.
6. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester.
7. The Upper Tester sends HCI ISO Data Packets to the IUT with the payload size set to 40 octets and 40 octets of random data at an interval of 10 ms.

Figure 4.20: Unsegmented Framed LL PDUs at 7.5 ms ISO Interval MSC

8. The IUT sends CIS ISO Data PDUs to the Lower Tester with a data length of 45 octets at an interval of 7.5 ms using the Unsegmented Framed mode.
9. Repeat Steps 7 and 8 for 50 Data PDUs.
- Expected Outcome

## Pass verdict

In Step 8, the IUT sends ISO Data Packets 7.5 ms apart. On average, 75% of packets will contain 45 octets of data and the remainder will be empty.

The data octets received by the Lower Tester are the same as those sent by the Upper Tester, in the same order.

## 4.3.21 Permitted Framing Mode Packets

- Test Purpose

Verify that an IUT sends ISO Data Packets using permitted framing modes.

- Reference

## 13 2

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The IUT acts in the role specified in Table 4.26.
- Test Case Configuration

Table 4.26: Permitted Framing Mode Packets test cases

| Test Case | Role | Framing (HCI and LL) |
| IAL/CIS/FRA/CEN/BV-57-C | Central | Framed PDUs, Segmentable mode |
| IAL/CIS/FRA/CEN/BV-59-C | Central | Framed PDUs, Unsegmented mode |

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with Framing set as specified in Table 4.26 and all other parameters set as default and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Create\_CIS command to create a single CIS and receives a successful HCI\_Command\_Status in response.
3. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with Framed set to 1 and Framing\_Mode set to either 0 or 1.
4. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
5. The IUT sends an LL\_CIS\_IND PDU to the Lower Tester.
6. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester.
7. The Upper Tester sends HCI ISO Data Packets to the IUT.
8. The IUT sends CIS ISO Data PDUs to the Lower Tester using the framing selection in Step 3.
9. Repeat Steps 7 and 8 for 50 Data PDUs.

Figure 4.21: Permitted Framing Mode Packets MSC

10. The Upper Tester sends an HCI\_Disconnect command to the IUT and receives a successful HCI\_Command\_Status in response.
11. The IUT sends an LL\_CIS\_TERMINATE\_IND PDU to the Lower Tester.
12. The IUT sends an HCI\_Disconnection\_Complete event to the Upper Tester.
13. Repeat Steps 2 -12 ten times.
- Expected Outcome

## Pass verdict

In Step 3, the IUT selects one of the framing modes specified in Table 4.26.

In Step 8, the IUT sends ISO Data Packets using either Unsegmented Framed or Segmented Framed mode.

The data octets received by the Lower Tester are the same as those sent by the Upper Tester, in the same order.

## Fail verdict

In Step 3, the IUT selects the unframed framing mode.

In Step 8, the ISO Data PDUs use the unframed mode.

## 4.4 BIS

Tests that the IUT behaves according to the Isochronous Adaptation Layer Specifications for Broadcast Isochronous Streams.

## 4.4.1 Common Timing and Variables

## 4.4.1.1 Timing Requirements

The timing of BIS tests in this section complies with the BIS timing requirements specified in [3] Section 4.10.1.2.

When using framed PDUs, the maximum allowed drift (MaxDrift) complies with the average timing of SDU delivery specified in [3] Section 2.2.

## 4.4.1.2 Value of IRC

As pre-transmission is not employed in this Test Suite, IRC is calculated as NSE/BN unless explicitly defined in the test case.

## 4.4.2 Broadcast Single SDU, BIS

- Test Purpose

Verify that the IUT can send a Broadcast ISO PDU over a BIS with length ≤ the Isochronous PDU length.

- Reference
- [3] 4.6.28
- [4] 2.1, 2.2

- Initial Condition
- -The IUT acts as an Isochronous Broadcaster.
- -State: Isochronous Broadcasting, Test (single BIS, packing: 0x01 (Interleaved), other values as specified in Table 4.27; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -TSPX\_max\_tx\_nse is the maximum supported TX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_tx\_bn is the maximum supported TX BN as defined in the IXIT [8] entry.
- -Max\_SDU is set to 32. Max\_PDU is set as specified in Table 4.27.

## · Test Case Configuration

Table 4.27: Send Single SDU, BIS test cases

| Test Case | NSE | Framed | Framing_Mode | Max_PDU | LLID | BN | SDU_Interval | ISO_Interval |
| IAL/BIS/UNF/BRD/BV-01-C | 2 (see Note 1) | 0 | 0 | 40 | 0b00 or 0b01 | 1 | 10 ms (0x2710) | 10 ms (0x08) |
| IAL/BIS/UNF/BRD/BV-02-C | 4 | 0 | 0 | 40 | 0b00 or 0b01 | 2 | 5 ms (0x1388) | 10 ms (0x08) |
| IAL/BIS/UNF/BRD/BV-03-C | 2 | 0 | 0 | 40 | 0b00 or 0b01 | 2 | 5 ms (0x1388) | 10 ms (0x08) |
| IAL/BIS/FRA/BRD/BV-06-C | 4 | 1 | 0 | 40 | 0b10 | 2 | 5 ms (0x1388) | 10 ms (0x08) |
| IAL/BIS/FRA/BRD/BV-08-C | 2 (see Note 1) | 1 | 0 | 40 | 0b10 | 1 | 10 ms (0x2710) | 10 ms (0x08) |
| IAL/BIS/FRA/BRD/BV-29-C | 6 | 1 | 1 | Max_SDU + 5 | 0b10 | 3 | 5 ms (0x1388) | 10 ms (0x08) |

Note 1: If TSPX\_max\_tx\_nse is 1, then an NSE of 1 and an IRC of 1 are used.

- Test Procedure

Figure 4.22: Send Single SDU, BIS MSC

If TSPX\_max\_tx\_nse is less than the value of NSE specified in Table 4.27 (does not apply if Note 1 in Table 4.27 is applicable), or TSPX\_max\_tx\_bn is less than the value of BN specified in Table 4.27, then refer to the Inconclusive verdict.

1. The Upper Tester sends an HCI ISO Data packet to the IUT with data length equal to the Max\_SDU size.
2. The IUT sends a Broadcast ISO Data PDU over the BIS with the LLID, Framed, and Framing\_Mode as specified in Table 4.27 and Payload Data identical to the data in Step 1.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a PDU with LLID set as specified in Table 4.27 and the same data in Step 1.

## Inconclusive verdict

TSPX\_max\_tx\_nse is less than the value of NSE specified in Table 4.27. This does not apply if Note 1 in Table 4.27 is applicable.

TSPX\_max\_tx\_bn is less than the value of BN specified in Table 4.27.

## 4.4.3 Broadcast Large SDU, BIS

- Test Purpose

Verify that the IUT can send a Broadcast ISO PDU over a BIS with length &gt; the Isochronous PDU length.

- Reference

[3] 4.6.28

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts as an Isochronous Broadcaster.
- -State: Isochronous Broadcasting, Test (single BIS, packing: 0x01 (Interleaved), other values as specified in Table 4.28; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -TSPX\_max\_tx\_nse is the maximum supported TX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_tx\_bn is the maximum supported TX BN as defined in the IXIT [8] entry.
- -Max\_SDU is set to 503. Max\_PDU is set to 251.

- Test Case Configuration

Table 4.28: Send Large SDU, BIS test cases

| Test Case | NSE (see Note 1) | Framing | BN | SDU_Interval | ISO_Interval |
| IAL/BIS/UNF/BRD/BV-09-C | 12 | Unframed (0) | 6 | 20 ms (0x4E20) | 40 ms (0x20) |
| IAL/BIS/UNF/BRD/BV-10-C | 6 | Unframed (0) | 3 | 20 ms (0x4E20) | 20 ms (0x10) |
| IAL/BIS/UNF/BRD/BV-11-C | 8 | Unframed (0) | 4 | 25 ms (0x61A8) | 25 ms (0x14) |
| IAL/BIS/FRA/BRD/BV-13-C | 10 | Framed (1) | 5 | 15 ms (0x3A98) | 30 ms (0x18) |
| IAL/BIS/FRA/BRD/BV-15-C | 6 | Framed (1) | 3 | 20 ms (0x4E20) | 20 ms (0x10) |

Note 1: If TSPX\_max\_tx\_nse ≥ NSE, then NSE is the value specified in Table 4.28. If TSPX\_max\_tx\_nse &lt; NSE and TSPX\_max\_tx\_nse and TSPX\_max\_tx\_bn are both ≥ the value of BN specified in Table 4.28, then NSE is the value of BN specified in Table 4.28 and IRC = 1. If neither of the previous conditions can be met, then refer to the Inconclusive verdict.

- Test Procedure

Figure 4.23: Send Large SDU, BIS MSC

Run each round in Table 4.29 unless TSPX\_max\_tx\_nse and/or TSPX\_max\_tx\_bn are less than the value of BN specified in Table 4.28, in which case refer to the Inconclusive verdict.

1. The Upper Tester sends HCI ISO Data packets to the IUT including an SDU whose length is specified in Table 4.29.
2. The IUT sends the specified number of Start/Continuation packets specified in Table 4.29 of ISO Data PDUs to the Lower Tester with the LLID=0b01 for unframed payloads and LLID=0b10 for framed payloads, and Payload Data every 251 bytes offset in Step 1.
3. The IUT sends the last ISO Data PDU to the Lower Tester with the LLID=0b00 for unframed payloads and LLID=0b10 for framed payloads, with the remaining Payload Data.

| Round | SDU Data Length | Start/Continuation packets |
| 1 | 495 | 1 |
| 2 | 503 | 2 |

Table 4.29: Send Large SDU, BIS rounds

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends the correct number of Start/Continuation PDUs as specified in Table 4.29 and that each PDU contains a Segmentation Header.

In Step 3, the IUT sends a PDU with LLID=0b00 for unframed payloads and LLID=0b10 for framed payloads, and the same data in Step 1.

The bits in the RFU field in the Segmentation Headers from the IUT are clear.

## Inconclusive verdict

TSPX\_max\_tx\_nse is less than the value of BN specified in Table 4.28.

TSPX\_max\_tx\_bn is less than the value of BN specified in Table 4.28.

## 4.4.4 Broadcast Multiple, Small SDUs, BIS

- Test Purpose

Verify that the IUT can send multiple SDUs that can be combined into a single Broadcast Isochronous PDU.

- Reference

[3] 4.6.28

[4] 2.2

- Initial Condition
- -The IUT acts as an Isochronous Broadcaster.
- -State: Isochronous Broadcasting, Test (single BIS, packing: 0x01 (Interleaved), framing: 0x01 (Framed), other values as specified in Table 4.30; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -Max\_SDU is set to 25. Max\_PDU is set as specified in Table 4.30.
- -TSPX\_max\_tx\_nse is the maximum supported TX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_tx\_bn is the maximum supported TX BN as defined in the IXIT [8] entry.
- Test Case Configuration

Table 4.30: Send Multiple, Small SDUs, BIS test cases

| Test Case | NSE | BN | Max_PDU | SDU_Interval | ISO_Interval |
| IAL/BIS/FRA/BRD/BV-17-C | 2 (see Note 1) | 1 | 68 | 500 ms (0x7A120) | 1000 ms (0x320) |
| IAL/BIS/FRA/BRD/BV-18-C | 2 (see Note 1) | 1 | 68 | 1000 ms (0xF4240) | 2000 ms (0x640) |
| IAL/BIS/FRA/BRD/BV-20-C | 4 | 2 | 65 | 500 ms (0x7A120) | 2000 ms (0x640) |

Note 1: If TSPX\_max\_tx\_nse is 1, then an NSE of 1 and an IRC of 1 are used.

Figure 4.24: Send Multiple, Small SDUs, BIS MSC

If TSPX\_max\_tx\_nse &lt; the value of NSE specified in Table 4.30 (unless Note 1 is applied) or TSPX\_max\_tx\_bn &lt; the value of BN specified in Table 4.30, then refer to the Inconclusive verdict.

1. The Upper Tester sends to the IUT a small SDU1 with data length of 20 bytes.
2. The Upper Tester sends to the IUT a small SDU2 with data length of 25 bytes.
3. The IUT sends a single Broadcast ISO Data PDU with SDU1 followed by SDU2 over the BIS. Each SDU header has SC = 0 and CMPT = 1.
- Expected Outcome

## Pass verdict

In Step 3, the IUT sends a single small Broadcast ISO Data PDU with data length of 55 bytes with SDU1 followed by SDU2.

## Inconclusive verdict

TSPX\_max\_tx\_nse &lt; the value of NSE specified in Table 4.30 and Note 1 does not apply.

TSPX\_max\_tx\_bn &lt; the value of BN specified in Table 4.30.

## 4.4.5 Receive a Single SDU, BIS

- Test Purpose

Verify that the IUT can receive an SDU over a BIS with length &lt;= the Isochronous PDU length.

- Reference

[3] 4.6.29

[4] 2

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (values as specified in Table 4.31, Max\_SDU and Max\_PDU as specified below, NumBis set to 1; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).

- -TSPX\_max\_sdu\_length is the maximum ISOAL SDU Length, as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_nse is the maximum supported RX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_bn is the maximum supported RX BN as defined in the IXIT [8] entry.
- -Max\_SDU is set to 32 or TSPX\_max\_sdu\_length, whichever is lesser. The actual SDU payload length equals Max\_SDU.

## · Test Case Configuration

Table 4.31: Receive Single SDU, BIS test cases

| Test Case | Max_PDU | NSE | Framed | Framing_Mode | LLID | BN | SDU_Interval | ISO_Interval |
| IAL/BIS/UNF/SNC/BV-01-C | 40 | 2 | 0 | 0 | 0b00 | 2 | 5 ms (0x1388) | 10 ms (0x08) |
| IAL/BIS/UNF/SNC/BV-02-C | 40 | 1 | 0 | 0 | 0b00 | 1 | 10 ms (0x2710) | 10 ms (0x08) |
| IAL/BIS/UNF/SNC/BV-03-C | 40 | 2 | 0 | 0 | 0b00 | 2 | 10 ms (0x2710) | 10 ms (0x08) |
| IAL/BIS/FRA/SNC/BV-06-C | 42 | 4 | 1 | 0 | 0b10 | 2 | 5 ms (0x1388) | 10 ms (0x08) |
| IAL/BIS/FRA/SNC/BV-08-C | 45 | 2 (see Note 1) | 1 | 0 | 0b10 | 1 | 10 ms (0x2710) | 10 ms (0x08) |
| IAL/BIS/FRA/SNC/BV-29-C | 3*(Max_SDU+5) | 4 | 1 | 1 | 0b10 | 1 | 5 ms (0x1388) | 10 ms (0x08) |

Note 1: If TSPX\_max\_rx\_nse is 1, then an NSE of 1 and an IRC of 1 are used.

- Test Procedure

Figure 4.25: Receive Single SDU, BIS MSC

If TSPX\_max\_rx\_nse is less than the value of NSE specified in Table 4.31 (does not apply if Note 1 in Table 4.31 is applicable) or TSPX\_max\_rx\_bn is less than the value of BN specified in Table 4.31, then refer to the Inconclusive verdict.

1. The Lower Tester sends Broadcast ISOC Data PDU with the LLID, Framed, and Framing\_Mode set as specified in Table 4.31.
2. The IUT sends an Isochronous Data SDU to the Upper Tester with Payload Data identical to the data in Step 1 and Data\_Total\_Length identical to the data length sent in Step 1.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an Isochronous Data SDU to the Upper Tester with Payload Data identical to the data in Step 1 and Data\_Total\_Length identical to the data length sent in Step 1.

## Inconclusive verdict

TSPX\_max\_rx\_nse &lt; the value of NSE specified in Table 4.31 and Note 1 does not apply.

TSPX\_max\_rx\_bn &lt; the value of BN specified in Table 4.31.

## 4.4.6 Receive Large SDU, BIS

- Test Purpose

Verify that the IUT can receive an SDU over a BIS with length &gt; the Isochronous PDU length.

- Reference

[3] 4.6.29

[4] 2.1, 2.2

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (single BIS, Max\_SDU is 754, Max\_PDU is 251; other values as specified in Table 4.32; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -TSPX\_max\_rx\_nse is the maximum supported RX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_bn is the maximum supported RX BN as defined in the IXIT [8] entry.

- Test Case Configuration

Table 4.32: Receive Large SDU, BIS test cases

| Test Case | NSE (see Note 1) | Framing | BN | SDU_Interval | ISO_Interval |
| IAL/BIS/UNF/SNC/BV-09-C | 8 | Unframed (0) | 4 | 25 ms (0x61A8) | 25 ms (0x14) |
| IAL/BIS/UNF/SNC/BV-10-C | 8 | Unframed (0) | 4 | 50 ms (0xC350) | 50 ms (0x28) |
| IAL/BIS/FRA/SNC/BV-11-C | 8 | Framed (1) | 4 | 40 ms (0x9C40) | 50 ms (0x28) |
| IAL/BIS/FRA/SNC/BV-13-C | 8 | Framed (1) | 4 | 25 ms (0x61A8) | 25 ms (0x14) |
| IAL/BIS/FRA/SNC/BV-15-C | 8 | Framed (1) | 4 | 30 ms (0x7530) | 35 ms (0x1C) |

Note 1: If TSPX\_max\_rx\_nse ≥ 8, then NSE is 8. If TSPX\_max\_rx\_nse &lt; 8 and TSPX\_max\_rx\_nse and TSPX\_max\_rx\_bn are both ≥ 4, then NSE = 4 and IRC = 1. If neither of the previous conditions can be met, then refer to the Inconclusive verdict.

- Test Procedure

Figure 4.26: Receive Large SDU, BIS MSC

Run each round in Table 4.33 unless TSPX\_max\_rx\_nse &lt; 4 or TSPX\_max\_rx\_bn &lt; 4, in which case refer to the Inconclusive verdict.

1. The Lower Tester sends the number of Start/Continuation packets specified in Table 4.33 of Broadcast ISO Data PDU with the LLID=0b01 for unframed payloads and LLID=0b10 for framed payloads. The bits in the RFU field of the Segmentation Header are set for framed payloads.
2. The Lower Tester sends the last ISO Data PDU with the LLID=0b00 for unframed payloads and LLID=0b10 for framed payloads, with the remaining Payload Data in a Broadcast ISO data PDU. The bits in the RFU field of the Segmentation Header are set for framed payloads.
3. The IUT sends an ISO Data packet to the Upper Tester with a data length specified in Table 4.33.

| Round | Unframed SDU Data Length | Framed SDU Data Length | Start/Continuation packets |
| 1 | 753 | 744 | 2 |
| 2 | 754 | 745 | 3 |

Table 4.33: Receive Large SDU, BIS rounds

- Expected Outcome

## Pass verdict

In Step 3, the Upper Tester receives an SDU with data length as specified in Table 4.33.

## Inconclusive verdict

TSPX\_max\_rx\_nse &lt; 4.

TSPX\_max\_rx\_bn &lt; 4.

## 4.4.7 Receive Multiple, Small SDUs, BIS

- Test Purpose

Verify that the IUT can receive a single Broadcast ISOC Data PDU and sends multiple small SDUs to the Upper Tester.

- Reference

[3] 4.6.29

[4] 2.2

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (values as specified in Table 4.34; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -Max\_SDU is set to 25.
- -TSPX\_max\_rx\_nse is the maximum supported RX NSE as defined in the IXIT [8] entry.
- -Max\_PDU is 68.
- Test Case Configuration

| Test Case | NSE | BN | SDU_Interval | ISO_Interval |
| IAL/BIS/FRA/SNC/BV-17-C | 2 (see Note 1) | 1 | 5 ms (0x1388) | 10 ms (0x08) |
| IAL/BIS/FRA/SNC/BV-18-C | 2 | 2 | 5 ms (0x1388) | 20 ms (0x10) |
| IAL/BIS/FRA/SNC/BV-20-C | 4 (see Note 2) | 2 | 5 ms (0x1388) | 20 ms (0x10) |

Table 4.34: Receive Multiple, Small SDUs, BIS test cases

Note 1:

If TSPX\_max\_rx\_nse = 1, then NSE = 1 and IRC = 1.

Note 2: If TSPX\_max\_rx\_nse &lt; 4, then refer to the Inconclusive verdict.

- Test Procedure
1. The Lower Tester sends a single Broadcast ISO data PDU with a data length of 55 bytes.
2. The IUT sends an SDU1 packet to the Upper Tester with data length of 20 bytes.
3. The IUT sends an SDU2 packet to the Upper Tester with data length of 25 bytes.
- Expected Outcome

Figure 4.27: Receive Multiple, Small SDUs, BIS MSC

## Pass verdict

In Step 2, the IUT sends an SDU to the Upper Tester with the data for SDU1 from Step 1.

In Step 3, the IUT sends an SDU to the Upper Tester with the data for SDU2 from Step 1.

## Inconclusive verdict

The specified value of NSE in Table 4.34 is 4 and TSPX\_max\_rx\_nse &lt; 4.

## 4.4.8 Broadcast a Zero-Length SDU, BIS

- Test Purpose

Verify that the IUT can send a zero-length SDU in a Broadcast ISO PDU over a BIS.

- Reference

[3] 4.6.28

[4] 2.1, 2.2, 3.1

- Initial Condition
- -The IUT acts as an Isochronous Broadcaster.
- -State: Broadcasting a Broadcast Isochronous Stream (single BIS, other values as specified in Table 4.35; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -TSPX\_max\_tx\_nse is the maximum supported TX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_tx\_bn is the maximum supported TX BN as defined in the IXIT [8] entry.

## · Test Case Configuration

Table 4.35: Send Zero-Length SDU, BIS test cases

| Test Case | NSE | Framed | Framing_Mode | LLID | BN | Segmentation Header | Time Offset |
| IAL/BIS/UNF/BRD/BV-21-C | 4 | 0 | 0 | 0b00 | 2 | N/A | N/A |
| IAL/BIS/UNF/BRD/BV-22-C | 6 | 0 | 0 | 0b00 | 3 | N/A | N/A |
| IAL/BIS/UNF/BRD/BV-23-C | 1 | 0 | 0 | 0b00 | 1 | N/A | N/A |
| IAL/BIS/UNF/BRD/BV-24-C | 2 | 0 | 0 | 0b00 | 1 | N/A | N/A |
| IAL/BIS/FRA/BRD/BV-25-C | 6 | 1 | 0 | 0b10 | 2 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/BRD/BV-26-C | 2 (see Note 1) | 1 | 0 | 0b10 | 1 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/BRD/BV-27-C | 4 | 1 | 0 | 0b10 | 1 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/BRD/BV-28-C | 6 | 1 | 0 | 0b10 | 3 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/BRD/BV-30-C | 6 | 1 | 1 | 0b10 | 2 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |

Note 1:

If TSPX\_max\_tx\_nse = 1, then NSE = 1 and IRC = 1.

- Test Procedure

Figure 4.28: Send Zero-Length SDU, BIS MSC

If TSPX\_max\_tx\_nse is less than the value of NSE specified in Table 4.35 (does not apply if Note 1 in Table 4.35 is applicable), or TSPX\_max\_tx\_bn is less than the value of BN specified in Table 4.35, then refer to the Inconclusive verdict.

1. The Upper Tester sends an HCI ISO Data packet to the IUT with zero data length.
2. The IUT sends a single Broadcast ISO Data PDU with the LLID, Framed, Framing\_Mode, the segmentation header and time offset fields as specified in Table 4.35. Length is 0 if LLID is 0b00 and is 5 (Segmentation Header + TimeOffset) if LLID is 0b10. SDU field is empty.
- Expected Outcome

## Pass verdict

The IUT sends a single Broadcast ISO Data PDU with the LLID=0b00 for unframed payloads and LLID=0b10 for framed payloads. The segmentation header and time offset fields are as specified in Table 4.35. The SDU is empty.

## Inconclusive verdict

TSPX\_max\_tx\_nse &lt; the value of NSE specified in Table 4.35 and Note 1 does not apply.

TSPX\_max\_tx\_bn &lt; the value of BN specified in Table 4.35.

## 4.4.9 Receive a Zero-Length SDU, BIS

- Test Purpose

Verify that the IUT can receive a zero-length SDU from a Broadcast ISO Data PDU.

- Reference

[3] 4.6.29

[4] 2.1, 2.2, 3.1

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (values as specified in Table 4.36; the ISO\_Interval and SDU\_Interval are chosen by the tester; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters, or Section 4.1.2.1, Common Parameters, BN = 1 if BN value is 1 in Table 4.36).
- -TSPX\_max\_rx\_nse is the maximum supported RX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_bn is the maximum supported RX BN as defined in the IXIT [8] entry.

## · Test Case Configuration

Table 4.36: Receive Zero-Length SDU, BIS test cases

| Test Case | NSE | Framed | Framing_Mode | LLID | BN | Segmentation Header | Time Offset |
| IAL/BIS/UNF/SNC/BV-21-C | 4 | 0 | 0 | 0b00 | 2 | N/A | N/A |
| IAL/BIS/UNF/SNC/BV-22-C | 6 | 0 | 0 | 0b00 | 3 | N/A | N/A |
| IAL/BIS/UNF/SNC/BV-23-C | 1 | 0 | 0 | 0b00 | 1 | N/A | N/A |
| IAL/BIS/UNF/SNC/BV-24-C | 2 | 0 | 0 | 0b00 | 1 | N/A | N/A |
| IAL/BIS/FRA/SNC/BV-25-C | 6 | 1 | 0 | 0b10 | 2 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/SNC/BV-26-C | 2 (see Note 1) | 1 | 0 | 0b10 | 1 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/SNC/BV-27-C | 4 | 1 | 0 | 0b10 | 1 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/SNC/BV-28-C | 6 | 1 | 0 | 0b10 | 3 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |
| IAL/BIS/FRA/SNC/BV-30-C | 6 | 1 | 1 | 0b10 | 2 | SC=0 CMPLT=1 LENGTH=length of TimeOffset | Yes |

Note 1:

If TSPX\_max\_rx\_nse = 1, then NSE = 1 and IRC = 1.

- Test Procedure

Figure 4.29: Receive Zero-Length SDU, BIS MSC

If TSPX\_max\_rx\_nse is less than the value of NSE specified in Table 4.36 (does not apply if Note 1 in Table 4.36 is applicable) or TSPX\_max\_rx\_bn is less than the value of BN specified in Table 4.36, then refer to the Inconclusive verdict.

1. The Lower Tester sends a single ISO Data PDU to the IUT with the LLID, Framed, and Framing\_Mode, and the segmentation header and time offset fields as specified in Table 4.36.
2. The IUT sends an empty ISO Data packet to the Upper Tester with the TimeOffset field as specified in Table 4.36.
- Expected Outcome

## Pass verdict

In Step 2 the IUT sends an empty SDU to the Upper Tester with the TimeOffset field as specified in Table 4.36.

## Inconclusive verdict

TSPX\_max\_rx\_nse &lt; the value of NSE specified in Table 4.36 and Note 1 does not apply.

TSPX\_max\_rx\_bn &lt; the value of BN specified in Table 4.36.

## IAL/BIS/UNF/SNC/BI-02-C [Receive an unsuccessful Large SDU, BIS]

- Test Purpose

Verify that the IUT sends an HCI ISO Data packet with a Packet\_Status\_Flag error when receiving Isochronous PDUs with SDU data length &gt; Isochronous PDU length and one of the continuation PDU packets fails to be received, when no PDUs are received, and when an invalid sequence of PDUs is received.

- Reference
- [3] 4.6.28

[4] 2.1

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (single BIS, NSE is 4, BN is 4, and packing is 0x01 (Interleaved); any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).

- -TSPX\_max\_rx\_nse is the maximum supported RX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_bn is the maximum supported RX BN as defined in the IXIT [8] entry.
- Test Procedure

Figure 4.30: IAL/BIS/UNF/SNC/BI-02-C [Receive an unsuccessful Large SDU, BIS] MSC

If TSPX\_max\_rx\_nse &lt; 4 or TSPX\_max\_rx\_bn &lt; 4, then refer to the Inconclusive verdict.

The rounds in Table 4.37 are performed in any order in consecutive isochronous events. In each round:

1. The Lower Tester sends the IUT the PDUs listed in Table 4.37.
2. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag=0b01 or Packet\_Status\_Flag=0b10. If Packet\_Status\_Flag=0b10, then PB\_Flag=0b10, ISO\_SDU\_Length=0, and there is no data.
- Expected Outcome

Table 4.37: IAL/BIS/UNF/SNC/BI-02-C [Receive an unsuccessful Large SDU, BIS] rounds

| Round | PDUs sent |
| 1 | 4 PDUs with LLID=0b01 and no data |
| 2 | 4 PDUs with LLID=0b01 and data |
| 3 | 3 PDUs with LLID=0b01 and data, then 1 PDU with LLID=0b00 and data; one of the first three PDUs has a CRC error |
| 4 | 2 PDUs with LLID=0b01 and data, then 2 PDUs with LLID=0b00 and data |
| 5 | 2 PDUs with LLID=0b01 and no data, then 1 PDU with LLID=0b00 and data, then 1 PDU with LLID=0b01 and data |
| 6 | 2 PDUs with LLID=0b01 and no data, then 1 PDU with LLID=0b00 and data, then 1 PDU with LLID=0b10 and no data |
| 7 | 2 PDUs with LLID=0b01 and no data, then 1 PDU with LLID=0b10 and data, then 1 PDU with LLID=0b00 and no data |
| 8 | 2 PDUs with LLID=0b01 and data, then 1 PDU with LLID=0b00 and data; one of the four PDUs is omitted to simulate losing one PDU |
| 9 | 1 PDU with LLID=0b00 and data, then 3 PDUs with LLID=0b01, at least one of which has data |
| 10 | No PDUs |

## Pass verdict

In Step 2, the IUT sends an ISO Data packet with Packet\_Status\_Flag=0b01 or Packet\_Status\_Flag=0b10. If Packet\_Status\_Flag=0b10, then PB\_Flag=0b10, ISO\_SDU\_Length=0, and there is no data.

## Inconclusive verdict

TSPX\_max\_rx\_nse &lt; 4.

TSPX\_max\_rx\_bn &lt; 4.

## 4.4.10 Broadcasting Unframed Empty PDUs with LLID=0b01, BIS

- Test Purpose

Test that the Isochronous Broadcaster IUT sends unframed empty PDUs with LLID = 0b01 when the number of required PDUs to transmit an SDU is less than BN×(SDU\_Interval÷ISO\_Interval) fragment PDUs, and encryption works correctly when empty PDUs are sent.

- Reference

[3] 4.6.28 [4] 2.1

- Initial Condition
- -TSPX\_broadcast\_code is the 4 -16 character Broadcast Code as defined in the IXIT [8] entry.
- -TSPX\_max\_tx\_nse is the maximum supported TX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_tx\_bn is the maximum supported TX BN as defined in the IXIT [8] entry.
- -State: Isochronous Broadcasting, Test (values as specified in Table 4.38)

Table 4.38: State Variable Values

| State Variable | Value(s) |
| num_bis | 1 |
| sdu_int | 100 ms |
| iso_int | 100 ms |
| nse | 12 (see Note 1) |
| mx_sdu | 128 |
| mx_pdu | 128 |
| phy | 0x01 (LE 1M PHY) |
| packing | 0x00 (Sequential) |
| framing | 0x00 (Unframed) |
| bn | 4 |
| irc | 3 (see Note 1) |
| pto | 0 |
| encryption | Per Table 4.39 |
| broadcast_code | TSPX_broadcast_code, if applicable |

Note 1: If TSPX\_max\_tx\_nse ≥ 12, then NSE = 12 and IRC = 3. If TSPX\_max\_tx\_nse &lt; 12 and ≥ 8, then NSE = 8 and IRC = 2. If TSPX\_max\_tx\_nse &lt; 8 and ≥ 4, then NSE = 4 and IRC = 1. Otherwise, see the Inconclusive verdict.

- Test Case Configuration

| Test Case | Encryption |
| IAL/BIS/UNF/BRD/BV-29-C | Disabled |
| IAL/BIS/UNF/BRD/BV-30-C | Enabled |

Table 4.39: Broadcasting Unframed Empty PDUs with LLID=0b01, BIS test cases

## · Test Procedure

Figure 4.31: Sending Unframed Empty PDUs with LLID=0b01, BIS MSC

If TSPX\_max\_tx\_nse &lt; 4 or TSPX\_max\_tx\_bn &lt; 4, then refer to the Inconclusive verdict.

1. The Upper Tester submits an SDU at its SDU interval of variable length, ranging from 4 to mx\_sdu octets. Note that the Test Command Generated Isochronous SDUs Optional Test Steps, ALT 3, VARIABLE LENGTH PAYLOADS in [9] Section 4.1.6.7.3 may be used for this purpose.
2. The Lower Tester receives PDUs from the IUT. When the required number of PDUs to transmit the SDU is less than BN PDUs, the remainder of BN PDUs are empty PDUs with LLID=0b01.
3. Repeat Steps 1 and 2 a minimum of 32 times.

## · Expected Outcome

## Pass verdict

The IUT sends empty PDUs with LLID=0b01 as required.

If encryption is enabled, the IUT sends correctly encrypted payload PDUs despite sending empty PDUs.

## Inconclusive verdict

TSPX\_max\_tx\_nse &lt; 4.

TSPX\_max\_tx\_bn &lt; 4.

## 4.4.11 Receiving Unframed Empty PDUs with LLID=0b01, BIS

## · Test Purpose

Test that the Synchronized Receiver IUT receives SDUs when unframed empty PDUs with LLID = 0b01 when the number of required PDUs to transmit an SDU is less than BN×(SDU\_Interval÷ISO\_Interval) fragment PDUs are received, and encryption works correctly when empty PDUs are received.

- Reference

[3] 4.6.28

[4] 2.1

- Initial Condition
- -TSPX\_broadcast\_code is the 4 -16 character Broadcast Code as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_nse is the maximum supported RX NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_bn is the maximum supported RX BN as defined in the IXIT [8] entry.
- -State: Synchronized to a Broadcast Isochronous Stream (values as specified in Table 4.40)

| State Variable | Value(s) |
| sync_timeout | default, as defined in [9] Section 4.11.2 |
| padv_interval | default, as defined in Section [9] Section 4.11.2 |
| big_sync_timeout | default, as defined in Section [9] Section 4.11.2 |
| adv_phy | default, as defined in Section [9] Section 4.11.2 |
| num_bis | 1 |
| sdu_int | 100 ms |
| iso_int | 100 ms |
| nse | 12 (see Note 1) |
| mx_sdu | 128 |
| mx_pdu | 128 |
| packing | 0x00 (Sequential) |
| framing | 0x00 (Unframed) |
| bn | 4 |
| irc | 3 (see Note 1) |
| pto | 0 |

Table 4.40: State Variable Values

| State Variable | Value(s) |
| encryption | Per Table 4.41 |
| broadcast_code | TSPX_broadcast_code, if applicable |

Note 1: If TSPX\_max\_rx\_nse ≥ 12, then NSE = 12 and IRC = 3. If TSPX\_max\_rx\_nse &lt; 12 and ≥ 8, then NSE = 8 and IRC = 2. If TSPX\_max\_rx\_nse &lt; 8 and ≥ 4, then NSE = 4 and IRC = 1. Otherwise, see the Inconclusive verdict.

- Test Case Configuration

| Test Case | Encryption |
| IAL/BIS/UNF/SNC/BV-29-C | Disabled |
| IAL/BIS/UNF/SNC/BV-30-C | Enabled |

Table 4.41: Receiving Unframed Empty PDUs with LLID=0b01, BIS test cases

- Test Procedure

Figure 4.32: Receiving Unframed Empty PDUs with LLID=0b01, BIS MSC

If TSPX\_max\_rx\_nse &lt; 4 or TSPX\_max\_rx\_bn &lt; 4, then refer to the Inconclusive verdict.

1. The Lower Tester sends PDUs based on an SDU of variable length, ranging from 4 to mx\_sdu octets. When the required number of PDUs to transmit the SDU is less than BN PDUs, the remainder of BN PDUs are empty PDUs with LLID=0b01.
2. The IUT sends the variable length SDUs from the Lower Tester to the Upper Tester.
3. Repeat Steps 1 and 2 a minimum of 32 times.

- Expected Outcome

## Pass verdict

The IUT receives at least 32 variable length PDUs from the Lower Tester and provides variable length SDUs to the Upper Tester. The SDU length is from 4 to 256 octets.

If encryption is enabled, the IUT sends correctly unencrypted SDUs to the Upper Tester despite receiving empty PDUs.

## Inconclusive verdict

TSPX\_max\_rx\_nse &lt; 4.

TSPX\_max\_rx\_bn &lt; 4.

## IAL/BIS/UNF/SNC/BI-05-C [SDU Reporting, BIS, Unframed PDU]

- Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Broadcast Isochronous Stream , Unframed.

- Reference

[3] 4.6.28 [4] 2.1 [11] 4

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (IRC is 1, BN is min(TSPX\_max\_rx\_bn, 3), NSE is equal to BN, Max\_SDU is set to 64, and Max\_PDU is set to 32; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -TSPX\_max\_rx\_bn is the maximum supported BN as defined in the IXIT [8] entry.

## · Test Procedure

Figure 4.33: IAL/BIS/UNF/SNC/BI-05-C [SDU Reporting, BIS, Unframed PDU] MSC

Steps 1 -3 all take place in the same BIS event.

1. The Lower Tester sends an unframed Start/Continuation ISO Data PDU with 21 octets of random data to the IUT with the LLID=0b01. If BN equals 2, omit this step.
2. The Lower Tester sends the IUT an unframed Start/Continuation ISO Data PDU with 21 octets of random data and an invalid CRC.
3. The Lower Tester sends the last unframed ISO Data PDU with 21 octets of random data to the IUT with the LLID=0b00.

4. Perform either alternative 4A or 4B depending on how the IUT reports the SDU:

Alternative 4A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 4A.1 The IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 4B (The IUT reports the SDU as 0b10 'lost data'):

- 4B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.
5. The Lower Tester sends unframed ISO Data PDUs to the IUT all with LLID = 0b01 and 21 octets of random data.
6. Perform either alternative 6A or 6B depending on how the IUT reports the SDU:

Alternative 6A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 6A.1 The IUT sends an HCI ISO Data packet with the truncated SDU data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 6B (The IUT reports the SDU as 0b10 'lost data'):

- 6B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.
- Expected Outcome

## Pass verdict

In Step 4A.1, the IUT sends data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 4B.1, the IUT sends an SDU to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

In Step 6A.1, the IUT sends the truncated SDU data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 6B.1, the IUT sends an SDU to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.

## IAL/BIS/UNF/SNC/BI-06-C [SDU Reporting, BIS, BN = 1, NSE = 1, Unframed PDU]

- Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Broadcast Isochronous Stream with BN = 1 and NSE =1, Unframed.

- Reference

[3] 4.6.28

[4] 2.1

[11] 4

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (IRC is 1, NSE is 1, BN is 1; Max\_SDU and Max\_PDU as specified below; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -Max\_SDU is set to 32. Max\_PDU is 32.

## · Test Procedure

Figure 4.34: IAL/BIS/UNF/SNC/BI-06-C [SDU Reporting, BIS, BN = 1, NSE = 1, Unframed PDU] MSC

1. The Lower Tester sends 1 unframed complete ISO Data PDU to the IUT with LLID=0b00 and with an invalid CRC.
2. Perform either alternative 2A or 2B depending on how the IUT reports the SDU:

Alternative 2A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 2A.1 The IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 2B (The IUT reports the SDU as 0b10 'lost data'):

- 2B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.
3. The Lower Tester sends unframed ISO Data PDUs to the IUT with LLID=0b01.
4. Perform either alternative 4A or 4B depending on how the IUT reports the SDU:

Alternative 4A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 4A.1 The IUT sends an HCI ISO Data packet with the truncated SDU data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 4B (The IUT reports the SDU as 0b10 'lost data'):

- 4B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 2B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

In Step 4A.1, the IUT sends an HCI ISO Data packet with the truncated SDU data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 4B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' with no data.

## IAL/BIS/FRA/SNC/BI-01-C [SDU Reporting, BIS, Framed PDU]

- Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Broadcast Isochronous Stream, Framed .

- Reference

[3] 4.6.28

[4] 2.2

[11] 4

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (IRC is 1, NSE is 4, BN is 4; Max\_SDU and Max\_PDU as specified below; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -TSPX\_max\_rx\_nse is the maximum supported NSE as defined in the IXIT [8] entry.
- -TSPX\_max\_rx\_bn is the maximum supported BN as defined in the IXIT [8] entry.
- -Max\_SDU is set to 108. Max\_PDU is 32.

Figure 4.35: IAL/BIS/FRA/SNC/BI-01-C [SDU Reporting, BIS, Framed PDU] MSC

1. The Lower Tester sends two framed Start/Continuation ISO Data PDUs to the IUT with the LLID=0b01.
2. The Lower Tester sends one framed Start/Continuation ISO Data PDU to the IUT with the LLID=0b00 and with the Length field in the Segmentation Header set to 255.
3. The Lower Tester sends the last framed ISO Data PDU to the IUT with the LLID=0b00 and with the remaining Payload Data.
4. Perform either alternative 4A or 4B depending on how the IUT reports the SDU:

Alternative 4A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 4A.1 The IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 4 B (The IUT reports the SDU as 0b10 'lost data'):

- 4B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.
5. Repeat Steps 1 -4 with LLID=0b10 in Steps 1 -3.
- Expected Outcome

## Pass verdict

In Step 4A.1, the IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 4B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Fla g set to 0b10 'lost data' and no data.

## Inconclusive verdict

The values of NSE or BN specified exceed the corresponding values of TSPX\_max\_rx\_nse or TSPX\_max\_rx\_bn, respectively.

## IAL/BIS/FRA/SNC/BI-02-C [SDU Reporting, BIS, BN = 1, NSE = 1, Framed PDU]

- Test Purpose

Verify that the IUT reports an SDU as 'data with possible errors' or discards and reports an SDU as 'lost data' in a Broadcast Isochronous Stream with BN = 1 and NSE = 1, Framed.

- Reference

[3] 4.6.28

[4] 2.2

[11] 4

- Initial Condition
- -The IUT acts as a Synchronized Receiver.
- -State: Synchronized to a Broadcast Isochronous Stream (IRC is 1, NSE is 1, BN is 1; Max\_SDU and Max\_PDU as specified below; any otherwise unspecified values as specified in [9] Section 4.11.2, Common Parameters).
- -Max\_SDU is set to 32. Max\_PDU is 45.
- Test Procedure
1. The Lower Tester sends 1 framed complete ISO Data PDU to the IUT with LLID = 0b10 and with the Length field of the Segmentation Header set to 255.
2. Perform either alternative 2A or 2B depending on how the IUT reports the SDU:

Figure 4.36: IAL/BIS/FRA/SNC/BI-02-C [SDU Reporting, BIS, BN = 1, NSE = 1, Framed PDU] MSC

Alternative 2A (The IUT reports the SDU as 0b01 'data with possible errors'):

- 2A.1 The IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

Alternative 2B (The IUT reports the SDU as 0b10 'lost data'):

- 2B.1 The IUT sends an HCI ISO Data packet to the Upper Tester with the Packet\_Status\_Flag set to 0b10 'lost data' and no data.

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT sends an HCI ISO Data packet with data to the Upper Tester with the Packet\_Status\_Flag set to 0b01 'data with possible errors'.

In Step 2B.1, the IUT sends an HCI ISO Data packet to the Upper Tester with the P acket\_Status\_Flag set to 0b10 'lost data' and no data.

## IAL/BIS/FRA/SNC/BI-03-C [Reporting an Unsuccessful Large SDU, Framed BIS]

- Test Purpose

Verify that the IUT sends an ISO Data packet to the Upper Tester with a Packet\_Status\_Flag error value of 0b10 when some packets in an SDU are not received.

- Reference

[12] 2.2

- Initial Condition
- -An unencrypted BIG has been created with BN = NSE = 2, Num\_BIS = 1, IRC = 1, and Framing = 0x01.
- -Max\_SDU is set to 16.
- -Max\_PDU is set to 16.
- -The IUT is synchronized to the only BIS in the BIG.

## · Test Procedure

Figure 4.37: Report an Unsuccessful Large SDU, Framed BIS MSC

Perform Step 1A four times, Step 1B four times, and Step 1C four times, in 12 consecutive isochronous events. The order of the 12 steps is selected at random.

- 1A. The Lower Tester sends two ISO Data PDUs to the IUT with the LLID = 0b10 in the same isochronous interval. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag = 0b00 and PB\_Flag = 0b10 and containing all the data.
- 1B. The Lower Tester sends an ISO Data PDU with the LLID = 0b10 in the first sub-event of an ISO interval and nothing in the second sub-event. The IUT sends the Upper Tester an ISO Data packet either with Packet\_Status\_Flag = 0b01 and containing the data, or with Packet\_Status\_Flag = 0b10 and ISO\_SDU\_Length = 0 and with no data.
- 1C. The Lower Tester sends nothing in the first sub-event of an ISO interval and an ISO Data PDU with the LLID = 0b10 in the second sub-event. The IUT sends the Upper Tester an ISO Data packet either with Packet\_Status\_Flag = 0b01 and containing the data, or with Packet\_Status\_Flag = 0b10 and ISO\_SDU\_Length = 0 and with no data.
- Expected Outcome

## Pass verdict

In at least 10 of the 12 events, the IUT sends an ISO Data packet to the Upper Tester with the proper Packet\_Status\_Flag, ISO\_SDU\_Length, and ISO Data.

## IAL/BIS/FRA/SNC/BI-04-C [Reporting a missing or damaged SDU, Framed BIS]

- Test Purpose

Verify that the IUT sends an ISO Data packet to the Upper Tester with a Packet\_Status\_Flag error value of 0b10 when some or all PDU packets in an SDU are not received and the SDU is discarded.

- Reference

[12] 2.2

- Initial Condition
- -An unencrypted BIG has been created with BN = NSE = 1, Num\_BIS = 1, IRC = 1, and Framing = 0x01.
- -Max\_PDU is set to Max\_SDU + 13.
- -The SDU interval and ISO interval are set to the same values.
- -The IUT is synchronized to the only BIS in the BIG.

- Test Procedure

Figure 4.38: Reporting a missing or damaged SDU, Framed BIS MSC

Perform Step 1A five times and Step 1B five times, in 10 consecutive isochronous events. The order of the 10 steps is selected at random.

- 1A. The Lower Tester sends an ISO Data PDU to the IUT with the LLID = 0b10. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag = 0b00 and PB\_Flag = 0b10 and containing all the data.
- 1B. The Lower Tester sends an ISO Null PDU. The IUT sends the Upper Tester an ISO Data packet with Packet\_Status\_Flag = 0b10 and ISO\_SDU\_Length = 0 and with no data.
- Expected Outcome

## Pass verdict

In at least 9 of the 10 repeats, the IUT sends an ISO Data packet to the Upper Tester with the proper Packet\_Status\_Flag, ISO\_SDU\_Length, and ISO Data.

## 4.4.12 Unsegmented Framed LL Broadcast PDUs at 7.5 ms ISO Interval, Isochronous Broadcaster

- Test Purpose

Verify that an Isochronous Broadcaster IUT sends ISO Data Packets using permitted framing modes.

- Reference

[13] 2

- Initial Condition
- -The Upper Tester creates a BIG using the HCI\_LE\_Create\_BIG\_Test command with Framing set to 0x02.
- -The IUT acts in the Isochronous Broadcaster role.

- -The Lower Tester acts in the Synchronized Receiver role.
- -State: Synchronized to a Broadcast Isochronous Stream (values as specified in [9], Section 4.11.1, Common Parameters).
- Test Case Configuration
- Test Procedure
1. The Upper Tester continuously sends HCI ISO Data Packets with the payload size set to 10.
2. The IUT transmits Broadcast Isochronous Data PDUs using unsegmented framed PDUs.
3. Repeat Steps 1 and 2 twenty times.
4. The Upper Tester sends HCI ISO Data Packets to the IUT with the payload size set to 40 octets and 40 octets of random data at an interval of 10 ms.
5. The IUT transmits Broadcast Isochronous Data PDUs with a data length of 45 octets at an interval of 7.5 ms using unsegmented framed.
- Expected Outcome

Table 4.42: Unsegmented Framed LL Broadcast PDUs at 7.5 ms ISO Interval Permitted Framing Mode Packets , Isochronous Broadcaster test cases

| Test Case | Framing (HCI) |
| IAL/BIS/FRA/BRD/BV-32-C | Unsegmented framed (0x02) |

Figure 4.39: Unsegmented Framed LL Broadcast PDUs at 7.5 ms ISO Interval, Isochronous Broadcaster MSC

## Pass verdict

In Step 2, the IUT sends Broadcast ISO Data Packets using unsegmented framed PDUs.

In Step 5, the IUT sends ISO Data Packets 7.5 ms apart. On average, 75% of packets will contain 45 octets of data and the remainder will be empty.

The data octets received by the Lower Tester are the same as those sent by the Upper Tester, in the same order.

## 4.4.13 Permitted Framing Mode Packets, Isochronous Broadcaster

- Test Purpose

Verify that an Isochronous Broadcaster IUT sends ISO Data Packets using permitted framing modes.

- Reference

## 13 2

- Initial Condition
- -The IUT acts in the Isochronous Broadcaster role.
- -The Lower Tester acts in the Synchronized Receiver role and is synchronized to the IUT.
- -State: Synchronized to a Broadcast Isochronous Stream (values as specified in [9], Section 4.11.1, Common Parameters).
- Test Case Configuration
- Test Procedure
1. Execute the LL/BIS/BRD/BV-13-C test up to Step 8. In LL/BIS/BRD/BV-13-C Step 1, Framing is set as specified in Table 4.43. All ISO data packets sent by the IUT to the Lower Tester in Step 8 are sent using the framed PDUs with the same framing mode, which can be either Segmentable or Unsegmented irrespective of the mode requested by the Upper Tester.
2. After the IUT sends 100 ISO data packets in Step 8, the Upper Tester sends the HCI\_LE\_Terminate\_BIG command.
3. The IUT sends the BIG\_TERMINATE\_IND PDU in the Control subevents.
4. The IUT sends the HCI\_LE\_Terminate\_BIG\_Complete event to the Upper Tester.
5. Repeat Steps 1 -4 ten times.
- Expected Outcome

Table 4.43: Permitted Framing Mode Packets, Isochronous Broadcaster test cases

| Test Case | Framing |
| IAL/BIS/FRA/BRD/BV-31-C | Framed, Segmentable mode |
| IAL/BIS/FRA/BRD/BV-33-C | Framed, Unsegmented mode |

## Pass verdict

In Step 1, the ISO data packets only use the framed modes.

The data octets received by the Lower Tester are the same as those sent by the Upper Tester, in the same order.

## 4.4.14 Framing\_Mode bit in BIGInfo Ignored, Unsegmented Framed not supported

- Test Purpose

Verify that a Synchronized Receiver IUT that does not support Unsegmented Framed packets treats Segmentable framed and Unsegmented framed packets as framed packets.

- Reference

[13] 2

- Initial Condition
- -The IUT is in the Synchronized Receiver role.
- -The Lower Tester acts in the Isochronous Broadcaster role with a BIS using a Framing Mode as specified in Table 4.44.
- -State: Synchronized to a Broadcast Isochronous Stream (values as specified in [9], Section 4.11.1, Common Parameters, Framing as specified in Table 4.44).
- Test Case Configuration
- Test Procedure
1. The Lower Tester transmits Broadcast Isochronous Data PDUs using the Framing Mode specified in Table 4.44.
2. The IUT sends an Isochronous Data SDU to the Upper Tester as a Framed packet with Payload Data identical to the data in Step 1 and Data\_Total\_Length identical to the data length sent in Step 1.
- Expected Outcome

Table 4.44: Framing\_B bit in BIGInfo Ignored, Unsegmented Framed not supported test cases

| Test Case | Framing Mode | Framing_Mode |
| IAL/BIS/FRA/SNC/BV-31-C | Framed, Segmentable mode | 0 |
| IAL/BIS/FRA/SNC/BV-32-C | Framed, Unsegmented mode | 1 |

## Pass verdict

In Step 2, the IUT sends each incoming Broadcast ISOC Data PDU to the Upper tester as Framed Packets.

## 5 Test case mapping

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.

The columns for the TCMT are defined as follows:

Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for IAL [6].

If a test case is mandatory within the respective layer, then the y/x reference is omitted.

Feature: A brief, informal description of the feature being tested.

Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [2].

For the purpose and structure of the ICS/IXIT, refer to [2].

| Item | Feature | Test Case(s) |
| IAL 1/2 AND IAL 1/3 AND IAL 2/1 | Send and Receive CIS SDUs Using Unframed PDUs, Central | IAL/CIS/UNF/CEN/BV-01-C IAL/CIS/UNF/CEN/BV-41-C IAL/CIS/UNF/CEN/BV-21-C IAL/CIS/UNF/CEN/BV-46-C IAL/CIS/UNF/CEN/BV-47-C IAL/CIS/UNF/CEN/BV-48-C IAL/CIS/UNF/CEN/BI-05-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/1 AND LL 9/46 | Send and Receive CIS SDUs Using Unframed PDUs, Central, BN > 1 | IAL/CIS/UNF/CEN/BV-25-C IAL/CIS/UNF/CEN/BI-02-C IAL/CIS/UNF/CEN/BI-03-C IAL/CIS/UNF/CEN/BV-09-C IAL/CIS/UNF/CEN/BV-45-C IAL/CIS/UNF/CEN/BI-04-C IAL/CIS/UNF/CEN/BV-49-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/1 AND LL 9/46 AND LL 9/47 | Send and Receive CIS SDUs Using Unframed PDUs, Central, BN > 1, FT > 1 | IAL/CIS/UNF/CEN/BV-04-C IAL/CIS/UNF/CEN/BV-28-C IAL/CIS/UNF/CEN/BV-17-C IAL/CIS/UNF/CEN/BV-24-C IAL/CIS/UNF/CEN/BV-12-C IAL/CIS/UNF/CEN/BV-19-C IAL/CIS/UNF/CEN/BV-33-C IAL/CIS/UNF/CEN/BV-36-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/1 AND LL 9/47 | Receive CIS SDUs Using Unframed PDUs, Central, FT > 1 | IAL/CIS/UNF/CEN/BV-43-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/2 | Send and Receive CIS SDUs Using Unframed PDUs, Peripheral | IAL/CIS/UNF/PER/BV-21-C IAL/CIS/UNF/PER/BV-47-C IAL/CIS/UNF/PER/BV-48-C IAL/CIS/UNF/PER/BV-49-C |

| Item | Feature | Test Case(s) |
| IAL 1/2 AND IAL 1/3 AND IAL 2/2 AND LL 9/46 | Send and Receive CIS SDUs Using Unframed PDUs, Peripheral, BN > 1 | IAL/CIS/UNF/PER/BV-01-C IAL/CIS/UNF/PER/BI-02-C IAL/CIS/UNF/PER/BI-03-C IAL/CIS/UNF/PER/BV-45-C IAL/CIS/UNF/PER/BV-46-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/2 AND LL 9/47 | Send and Receive CIS SDUs Using Unframed PDUs, Peripheral, FT > 1 | IAL/CIS/UNF/PER/BV-41-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/2 AND LL 9/46 AND LL 9/47 | Send and Receive CIS SDUs Using Unframed PDUs, Peripheral, BN > 1, FT > 1 | IAL/CIS/UNF/PER/BV-04-C IAL/CIS/UNF/PER/BV-17-C IAL/CIS/UNF/PER/BV-24-C IAL/CIS/UNF/PER/BV-25-C IAL/CIS/UNF/PER/BV-28-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/2 | Receive CIS SDUs Using Unframed PDUs, Peripheral | IAL/CIS/UNF/PER/BV-09-C IAL/CIS/UNF/PER/BV-43-C IAL/CIS/UNF/PER/BI-05-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/2 AND LL 9/46 | Receive CIS SDUs Using Unframed PDUs, Peripheral, BN > 1 | IAL/CIS/UNF/PER/BV-33-C IAL/CIS/UNF/PER/BI-04-C IAL/CIS/UNF/PER/BV-50-C |
| IAL 1/2 AND IAL 1/3 AND IAL 2/2 AND LL 9/46 AND LL 9/47 | Receive CIS SDUs Using Unframed PDUs, Peripheral, BN > 1, FT > 1 | IAL/CIS/UNF/PER/BV-12-C IAL/CIS/UNF/PER/BV-19-C IAL/CIS/UNF/PER/BV-36-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/1 | Send and Receive CIS SDUs Using Framed PDUs, Central | IAL/CIS/FRA/CEN/BV-42-C IAL/CIS/FRA/CEN/BV-45-C IAL/CIS/FRA/CEN/BV-46-C IAL/CIS/FRA/CEN/BV-47-C IAL/CIS/FRA/CEN/BV-48-C IAL/CIS/FRA/CEN/BV-49-C IAL/CIS/FRA/CEN/BV-50-C IAL/CIS/FRA/CEN/BV-51-C IAL/CIS/FRA/CEN/BV-52-C IAL/CIS/FRA/CEN/BV-15-C IAL/CIS/FRA/CEN/BI-02-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/1 AND LL 9/47 | Send and Receive CIS SDUs Using Framed PDUs, Central, FT > 1 | IAL/CIS/FRA/CEN/BV-05-C IAL/CIS/FRA/CEN/BV-07-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/1 AND LL 9/46 AND LL 9/47 | Send and Receive CIS SDUs Using Framed PDUs, Central, BN > 1, FT > 1 | IAL/CIS/FRA/CEN/BV-03-C IAL/CIS/FRA/CEN/BV-18-C IAL/CIS/FRA/CEN/BV-22-C IAL/CIS/FRA/CEN/BV-26-C IAL/CIS/FRA/CEN/BV-29-C IAL/CIS/FRA/CEN/BV-31-C IAL/CIS/FRA/CEN/BV-10-C IAL/CIS/FRA/CEN/BV-13-C IAL/CIS/FRA/CEN/BV-38-C IAL/CIS/FRA/CEN/BV-39-C IAL/CIS/FRA/CEN/BV-44-C |

| Item | Feature | Test Case(s) |
| IAL 1/1 AND IAL 1/3 AND IAL 1/6 AND IAL 2/1 AND LL 9/46 AND LL 9/47 | Send and Receive CIS SDUs Using Framed PDUs, Unsegmented mode, Central, BN > 1, FT > 1 | IAL/CIS/FRA/CEN/BV-53-C IAL/CIS/FRA/CEN/BV-55-C |
| IAL 1/1 AND IAL 1/3 AND IAL 1/6 AND LL 1/5 AND LL 9/46 AND LL 9/47 | Receive CIS SDUs Using Framed PDUs, Unsegmented mode, Central, BN > 1, FT > 1 | IAL/CIS/FRA/CEN/BV-54-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/1 AND LL 9/47 | Receive CIS SDUs Using Framed PDUs, Central, FT > 1 | IAL/CIS/FRA/CEN/BV-20-C |
| IAL 1/1 AND IAL 1/3 AND IAL 1/6 AND LL 1/5 AND LL 9/47 | Receive CIS SDUs Using Framed PDUs, Unsegmented mode, Central, FT > 1 | IAL/CIS/FRA/CEN/BV-56-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/1 AND LL 9/46 | Send and Receive CIS SDUs Using Framed PDUs, BN > 1, Central | IAL/CIS/FRA/CEN/BI-01-C IAL/CIS/FRA/CEN/BV-35-C IAL/CIS/FRA/CEN/BI-03-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/1 | Send and Receive CIS SDUs Using Framed PDUs, Central | IAL/CIS/FRA/CEN/BI-04-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/2 AND LL 9/47 | Send CIS SDUs Using Framed PDUs, Peripheral, FT > 1 | IAL/CIS/FRA/PER/BV-18-C |
| IAL 1/1 AND IAL 1/3 AND IAL 1/6 AND LL 1/4 AND LL 6/32 AND LL 9/47 | Send CIS SDUs Using Framed PDUs, Unsegmented mode, Peripheral, FT > 1 | IAL/CIS/FRA/PER/BV-55-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/1 | Permitted Frame Mode CIS Packets, Framed PDUs, Segmentable Framed mode, Central | IAL/CIS/FRA/CEN/BV-57-C |
| IAL 1/1 AND IAL 1/3 AND IAL 1/6 AND IAL 2/1 | Permitted Frame Mode CIS Packets, Framed PDUs, Unsegmented Framed mode, Central | IAL/CIS/FRA/CEN/BV-58-C IAL/CIS/FRA/CEN/BV-59-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/2 AND LL 9/46 AND LL 9/47 | Send and Receive CIS SDUs Using Framed PDUs, Peripheral, BN > 1, FT > 1 | IAL/CIS/FRA/PER/BV-03-C IAL/CIS/FRA/PER/BV-05-C IAL/CIS/FRA/PER/BV-29-C IAL/CIS/FRA/PER/BV-22-C IAL/CIS/FRA/PER/BV-31-C IAL/CIS/FRA/PER/BV-42-C IAL/CIS/FRA/PER/BV-10-C IAL/CIS/FRA/PER/BV-20-C IAL/CIS/FRA/PER/BV-35-C IAL/CIS/FRA/PER/BV-38-C IAL/CIS/FRA/PER/BV-39-C |
| IAL 1/1 AND IAL 1/3 AND IAL 1/6 AND LL 1/4 AND LL 6/32 AND LL 9/46 AND LL 9/47 | Send and Receive CIS SDUs Using Framed PDUs, Unsegmented mode, Peripheral, BN > 1, FT > 1 | IAL/CIS/FRA/PER/BV-53-C |

| Item | Feature | Test Case(s) |
| IAL 1/1 AND IAL 1/3 AND IAL 1/6 AND IAL 2/2 AND LL 9/46 AND LL 9/47 | Send and Receive CIS SDUs Using Framed PDUs, Unsegmented mode, Peripheral, BN > 1, FT > 1 | IAL/CIS/FRA/PER/BV-54-C IAL/CIS/FRA/PER/BV-56-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/2 | Send and Receive CIS SDUs Using Framed PDUs, Peripheral | IAL/CIS/FRA/PER/BV-44-C IAL/CIS/FRA/PER/BI-02-C IAL/CIS/FRA/PER/BV-26-C IAL/CIS/FRA/PER/BV-07-C IAL/CIS/FRA/PER/BV-45-C IAL/CIS/FRA/PER/BV-46-C IAL/CIS/FRA/PER/BV-47-C IAL/CIS/FRA/PER/BV-48-C IAL/CIS/FRA/PER/BV-49-C IAL/CIS/FRA/PER/BV-50-C IAL/CIS/FRA/PER/BV-51-C IAL/CIS/FRA/PER/BV-52-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/2 AND LL 9/46 | Send and Receive CIS SDUs Using Framed PDUs, Peripheral, BN > 1 | IAL/CIS/FRA/PER/BV-13-C IAL/CIS/FRA/PER/BI-01-C IAL/CIS/FRA/PER/BI-03-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/2 | Send and Receive CIS SDUs Using Framed PDUs, Peripheral | IAL/CIS/FRA/PER/BI-04-C |
| IAL 1/1 AND IAL 1/3 AND IAL 2/2 AND LL 9/47 | Send and Receive CIS SDUs Using Framed PDUs, Peripheral, FT > 1 | IAL/CIS/FRA/PER/BV-15-C |
| IAL 1/2 AND IAL 1/4 | Broadcast BIS SDUs Using Unframed PDUs | IAL/BIS/UNF/BRD/BV-01-C IAL/BIS/UNF/BRD/BV-23-C IAL/BIS/UNF/BRD/BV-24-C |
| IAL 1/2 AND IAL 1/4 AND LL 12/4 | Broadcast BIS SDUs Using Unframed PDUs, BN > 1 | IAL/BIS/UNF/BRD/BV-02-C IAL/BIS/UNF/BRD/BV-03-C IAL/BIS/UNF/BRD/BV-09-C IAL/BIS/UNF/BRD/BV-10-C IAL/BIS/UNF/BRD/BV-11-C IAL/BIS/UNF/BRD/BV-21-C IAL/BIS/UNF/BRD/BV-22-C IAL/BIS/UNF/BRD/BV-29-C |
| IAL 1/2 AND IAL 1/5 AND LL 11a/1 | Receive an unsuccessful Large SDU, BIS, BN > 1 | IAL/BIS/UNF/SNC/BI-02-C |
| IAL 1/2 AND IAL 1/5 | Receive BIS SDUs Using Unframed PDUs | IAL/BIS/UNF/SNC/BV-02-C IAL/BIS/UNF/SNC/BV-23-C IAL/BIS/UNF/SNC/BV-24-C IAL/BIS/UNF/SNC/BI-06-C |

| Item | Feature | Test Case(s) |
| IAL 1/2 AND IAL 1/5 AND LL 11a/1 | Receive BIS SDUs Using Unframed PDUs, BN > 1 | IAL/BIS/UNF/SNC/BV-01-C IAL/BIS/UNF/SNC/BV-03-C IAL/BIS/UNF/SNC/BV-09-C IAL/BIS/UNF/SNC/BV-10-C IAL/BIS/UNF/SNC/BV-21-C IAL/BIS/UNF/SNC/BV-22-C IAL/BIS/UNF/SNC/BV-29-C IAL/BIS/UNF/SNC/BI-05-C |
| IAL 1/1 AND IAL 1/4 | Broadcast BIS SDUs Using Framed PDUs | IAL/BIS/FRA/BRD/BV-17-C IAL/BIS/FRA/BRD/BV-18-C |
| IAL 1/1 AND IAL 1/4 AND IAL 1/6 | Broadcast BIS SDUs Using Framed PDUs, Segmentable mode | IAL/BIS/FRA/BRD/BV-08-C IAL/BIS/FRA/BRD/BV-26-C IAL/BIS/FRA/BRD/BV-27-C |
| IAL 1/1 AND IAL 1/4 AND LL 12/4 | Broadcast BIS SDUs Using Framed PDUs, BN > 1 | IAL/BIS/FRA/BRD/BV-13-C IAL/BIS/FRA/BRD/BV-15-C IAL/BIS/FRA/BRD/BV-20-C |
| IAL 1/1 AND IAL 1/4 AND LL 12/4 | Broadcast BIS SDUs Using Framed PDUs, Segmentable mode, BN > 1 | IAL/BIS/FRA/BRD/BV-06-C IAL/BIS/FRA/BRD/BV-25-C IAL/BIS/FRA/BRD/BV-28-C |
| IAL 1/1 AND IAL 1/4 AND IAL 1/6 AND LL 12/4 | Broadcast BIS SDUs Using Framed PDUs, Unsegmented mode, BN > 1 | IAL/BIS/FRA/BRD/BV-29-C IAL/BIS/FRA/BRD/BV-30-C |
| IAL 1/1 AND IAL 1/5 | Receive BIS SDUs Using Framed PDUs | IAL/BIS/FRA/SNC/BV-17-C IAL/BIS/FRA/SNC/BI-02-C IAL/BIS/FRA/SNC/BI-04-C |
| IAL 1/1 AND IAL 1/5 | Receive BIS SDUs Using Framed PDUs, Segmentable mode | IAL/BIS/FRA/SNC/BV-08-C IAL/BIS/FRA/SNC/BV-26-C IAL/BIS/FRA/SNC/BV-27-C |
| IAL 1/1 AND IAL 1/5 AND LL 11a/1 | Receive BIS SDUs Using Framed PDUs, BN > 1 | IAL/BIS/FRA/SNC/BV-11-C IAL/BIS/FRA/SNC/BV-13-C IAL/BIS/FRA/SNC/BV-15-C IAL/BIS/FRA/SNC/BV-18-C IAL/BIS/FRA/SNC/BV-20-C IAL/BIS/FRA/SNC/BI-01-C IAL/BIS/FRA/SNC/BI-03-C |
| IAL 1/1 AND IAL 1/5 AND LL 11a/1 | Receive BIS SDUs Using Framed PDUs, Segmentable mode, BN > 1 | IAL/BIS/FRA/SNC/BV-06-C IAL/BIS/FRA/SNC/BV-25-C IAL/BIS/FRA/SNC/BV-28-C |
| IAL 1/1 AND IAL 1/5 AND IAL 1/6 AND LL 11a/1 | Receive BIS SDUs Using Framed PDUs, Unsegmented mode PDUs, BN > 1 | IAL/BIS/FRA/SNC/BV-29-C IAL/BIS/FRA/SNC/BV-30-C |
| IAL 1/1 AND IAL 1/4 | Permitted Frame Mode BIS Packets, Framed PDUs, Segmentable Framed mode, Broadcaster | IAL/BIS/FRA/BRD/BV-31-C |
| IAL 1/1 AND IAL 1/4 AND IAL 1/6 | Permitted Frame Mode BIS Packets, Framed PDUs, Unsegmented Framed mode, Broadcaster | IAL/BIS/FRA/BRD/BV-32-C IAL/BIS/FRA/BRD/BV-33-C |

| Item | Feature | Test Case(s) |
| IAL 1/1 AND IAL 1/5 AND NOT IAL 1/6 | Framed PDUs, Unsegmented mode not supported or Core v5.4 not supported | IAL/BIS/FRA/SNC/BV-31-C IAL/BIS/FRA/SNC/BV-32-C |
| IAL 1/2 AND IAL 1/4 AND LL 9/1 AND LL 12/4 | Broadcast Encrypted BIS SDUs Using Unframed PDUs, BN > 1 | IAL/BIS/UNF/BRD/BV-30-C |
| IAL 1/2 AND IAL 1/5 AND LL 9/1 AND LL 11a/1 | Receive Encrypted BIS SDUs Using Unframed PDUs, BN > 1 | IAL/BIS/UNF/SNC/BV-30-C |

Table 5.1: Test case mapping

## 6 Revision history and acknowledgments
