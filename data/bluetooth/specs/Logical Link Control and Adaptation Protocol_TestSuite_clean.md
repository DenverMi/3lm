## Logical Link Control and Adaptation Protocol (L2CAP)

## Bluetooth ® Test Suite
- Revision: L2CAP.TS
- Revision Date: 2026-05-05

## 1 Scope

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Logical Link Control and Adaptation Protocol (L2CAP) layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers' Bluetooth devices.

## 2 References, definitions, and abbreviations

## 2.1 References

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
- [19] Specification of the Bluetooth System, Version 6.3 or later, Volume 3, Part A (L2CAP)

## 2.2 Definitions

In this Bluetooth document, the definitions from [9] and [10] apply.

Certain terms that were identified as inappropriate have been replaced. For a list of the original terms and their replacement terms, see the Appropriate Language Mapping Tables document [18].

## 2.3 Acronyms and abbreviations

In this Bluetooth document, the definitions, acronyms, and abbreviations from [9] and [10] apply.

## 3 Test Suite Structure (TSS)

## 3.1 Test Strategy

The test objectives are to verify the functionality of the L2CAP layer within a Bluetooth Host and enable interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory and optional requirements in the specification and matches these to the support of the IUT as described in the ICS. At the same time, unless specifically prohibited by a test procedure, it is acceptable for IUTs to send redundant PDUs not described by the test procedure. When observed, such PDUs do not result in a test case failure. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test Case Mapping Table (TCMT) evaluates to true.

The test equipment provides an implementation of the Radio Controller and the parts of the Host needed to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT's peer device and interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement similar capabilities to communicate with the test equipment. For some test cases, it is necessary to stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface, a Man Machine Interface (MMI), or another interface supported by the IUT.

This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with catalogued specification requirements that were logically grouped and assessed for testability enabling coverage in defined test purposes.

The L2CAP layer specifies three groups of services:

- CONNECTION ORIENTED basic L2CAP mode
- CONNECTION ORIENTED retransmission/flow control/streaming modes
- CONNECTIONLESS basic L2CAP mode

The Test Suite Structure is a tree with the first level defined as L2CAP representing the protocol services. From these services, the test groups and functional modules are derived.

## 3.2 Test groups

Tests are defined in terms of a sequence of L2CAP and AMP Manager operations in the Implementation Under Test (IUT) and over-the-air interface operations.

The test groups are organized in three levels. The first level defines the protocol groups representing the protocol services. The second level separates the protocol services in functional modules. The last level in each branch contains the standard ISO subgroups BV and BI.

## 3.2.1 Protocol service groups

The protocol groups identify the Bluetooth L2CAP Layer services Connection-Oriented Services and the Connectionless Service.

## 3.2.1.1 Connection-Oriented Service -Basic L2CAP Mode

With the functional modules:

- Basic operation data channel
- Configuration of data channel
- Implementation-specific information exchange
- Echo handling

## 3.2.1.2 Connection-Oriented Service -Retransmission/Flow Control/Streaming Modes

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

## 3.2.1.3 Low Energy System tests

- Connection parameter update
- Command reject

## 3.2.1.4 Connectionless Service

- Connectionless reception channel

## 3.2.2 Main test groups

## 3.2.2.1 Fixed Channel Support

The Generic AMP defines a method to determine if a device supports fixed channels beyond the two currently defined. A fixed channel is present as soon as the ACL link is created. These fixed channels can be used for the AMP Manager protocol and other protocols in the future.

Refer to [8] Section 2.1 for a list of the characteristics of each fixed channel (e.g., reliability, MTU size, QoS). Table 2.1 in Section 2.1 lists the defined fixed channels and provides a reference to where the associated channel characteristics are defined.

## 3.2.2.2 AMP Manager Channel Support

The AMP Manager protocol uses L2CAP fixed channel 3 for communication between individual device AMP Managers. These tests relate to the creation of AMP channels and moving data channels between AMPs and the BR/EDR controllers.

## 3.2.2.3 AMP Manager Protocol

The AMP Manager provides information on available AMPs and their characteristics to other AMP capable Bluetooth devices. These tests relate to AMP Discovery, info exchange and change in available AMP status.

## 3.2.2.4 AMP Manager Physical Channel Interface

The AMP Manager must be able to acquire AMP info from the local available AMPs. These tests relate to AMP Manager / AMP HCI / AMP PAL interface and control. The interface and exchange of information is defined in terms of AMP HCI command packets and events. Note that a specific instance of a Bluetooth stack and AMP PAL may not necessarily need to exchange an AMP HCI Packet if the interaction between the layers 'acts' as if an AMP HCI packet was exchanged.

## 3.2.2.5 Low Energy Signaling Channel Support

The Low Energy Signaling channel uses L2CAP fixed channel 5 for communication between Low energy capable devices.

## 3.2.3 Behavior testing groups

## 3.2.3.1 Valid Behavior (BV) tests

This sub group provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt or exchange of a valid Protocol Data Units (PDUs). Valid PDUs means that the exchange of messages and the content of the exchanged messages are considered as valid.

## 3.2.3.2 Invalid Behavior (BI) tests

This sub group provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt of a syntactically or semantically invalid PDU.

## 4 Test cases (TC)

## 4.1 Introduction

## 4.1.1 Test case identification conventions

Test cases are assigned unique identifiers per the conventions in [10]. The convention used here is: &lt;spec abbreviation&gt;/&lt;IUT role&gt;/ &lt;class&gt;/ &lt;feat&gt; /&lt;func&gt;/&lt;subfunc&gt;/&lt;cap&gt;/ &lt;xx&gt;-&lt;nn&gt;-&lt;y&gt; .

| Identifier Abbreviation | Spec Identifier <spec abbreviation> |
| L2CAP | Logical Link Control and Adaptation Protocol |
| Identifier Abbreviation | Function Identifier <func> |
| CLS | Connectionless services |
| COS | Connection-oriented services |
| LE | Low Energy signaling channel |
| Identifier Abbreviation | Subfunction Identifier <subfunc> |
| CCH | Create Channel |
| CED | Basic operation data channel |
| CFC | LE Credit Based Flow Control Mode |
| CFD | Configuration of data channel |
| CID | Channel Identifiers |
| CLR | Connectionless reception channel |
| CMC | Channel Mode configuration |
| CPU | Connection Parameter Update |
| ECF | Enhanced Retransmission Mode using Extended Control Field |
| ECH | Echo handling |
| ERM | Use of Enhanced Retransmission Mode |
| EWC | Extended Window Size Configuration |
| EXF | Extended Features |
| FIX | Fixed Channel Support |
| FLC | Flow control mode |
| FOC | Optional FCS configuration |
| IEX | Implementation-specific information exchange |
| LSC | Lock Step Configuration |
| MCH | Move Channel |
| OFS | Use of Optional FCS |
| REJ | Command reject |
| RTX | Retransmission mode |
| STM | Streaming Mode |
| UCD | Unicast Connectionless Data |
| Identifier Abbreviation | Class Identifier <class> |
| TIM | Generic Attribute Timing Tests |

Table 4.1: L2CAP TC feature naming conventions

| Item | Support |
| ECFC | Enhanced Credit Based Flow Control Mode |

## 4.1.2 MSC abbreviations

Table 4.2 provides the definitions of abbreviations used in the test case MSCs.

Table 4.2: MSC abbreviations

| MSC Abbr | Use in Frame | Description | Reference |
| SAR | I-Frame | I-Frame Segmentation And Reassembly indicator (i.e., Un-segmented SDU / Start, Continuation, End of SDU) | [1] 3.3.2 |
| F | I/S-Frame | Final Bit | [1] 3.3.2 |
| P | S-Frame | Poll Bit | [1] 3.3.2 |
| RR | S-Frame | S-Frame Supervisory Function = Receiver Ready | [1] 3.3.2 |
| RNR | S-Frame | S-Frame Supervisory Function = Receiver Not Ready | [1] 3.3.2 |
| REJ | S-Frame | S-Frame Supervisory Function = Reject | [1] 3.3.2 |
| SREJ | S-Frame | S-Frame Supervisory Function = Selective Reject | [1] 3.3.2 |

## 4.1.3 Conformance

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

## 4.1.4 Lower layer assumptions

For conformance testing L2CAP and enhanced L2CAP layers it is necessary to have working lower layers in conformance with lower layer specifications.

For testing it is necessary to have an ACL link between the Lower Tester and IUT set up.

For connection-oriented operation no more than one ACL link exists between an IUT and the Lower Tester.

In the L2CAP test cases the IUT may act either as L2CAP initiator or as L2CAP acceptor. In each test case is defined which of these roles apply. The L2CAP initiator is assumed to be the Central of the piconet when executing these tests.

## 4.1.5 Upper Tester

For some test cases, it is necesary to stimulate the IUT from an Upper Tester. In practice, this could be special test interface, an MMI, or other interface as supported by the IUT.

## 4.1.6 General information about MSC

The reception of L2CAP\_CONFIGURATION\_REQ/RSP PDUs from the IUT by the Lower Tester is described in more detail in [6] Section 5.2. The MSC diagrams for each Test Case only reflect the case where these PDUs are not segmented by IUT. If segmentation occurs, the MSC diagrams for each Test Case can be seen as the final outcome of the configuration procedure.

## 4.1.7 Pass/Fail verdict conventions

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met.

The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict.

## 4.2 Preamble IXITs

The following IXIT items are defined to assist with general establishment of initial conditions. As such they are noted here rather than in specific tests.

| TSPX_iut_device_name_in_adv_packet_for_random_address | Device Name. IUT advertising this local name for the Lower Tester to make connection to. The default is that this not using it with empty string. |

Table 4.3: Preamble IXITs

| TSPX_delete_link_key | Determine whether the Lower Tester has to delete the stored link key in the beginning of each test case. |

## 4.3 Common Packet Contents

## 4.3.1 Fields and Bits Reserved for Future Use

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers.

## 4.4 Connection-Oriented Basic L2CAP mode

Verify the correct implementation of the connection-oriented services of the L2CAP layer.

## 4.4.1 Basic Operation Data Channel CED

Verify the basic procedures for connection establishment of a data channel. That describes the setup phases, the data exchange and the release.

## L2CAP/COS/CED/BV-01-C [Request Connection]

- Test Purpose

Verify that the IUT can request the connection establishment for an L2CAP data channel and initiate the configuration procedure.

- Reference

[1] Table 2.1, Table 6.1, 2.2, 4.2, 4.3

- Initial Condition
- -The IUT is in CLOSED state for data channel. No ACL link is established.
- -It must be possible to send a connection request from the Upper Tester to create an L2CAP channel.
- Test Procedure

ACL link establishment is part of the test case. The Lower Tester imposes 48 byte MTU for both configuration directions.

Figure 4.1: L2CAP/COS/CED/BV-01-C [Request Connection] MSC

- Test Condition

The Lower Tester utilizes version L2CAP Basic Mode.

The Lower Tester's Bluetooth device address BD\_ADDR is defined. For parameters to send and receive, see [5].

The IUT acts as L2CAP initiator.

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP\_CONNECTION\_REQ over the signaling channel and dynamically allocates an SCID.

The IUT initiates the configuration process as indicated by the generation of an L2CAP\_CONFIGURATION\_REQ.

The IUT accepts configuration of the MTU=48 bytes.

## L2CAP/COS/CED/BV-03-C [Send Data]

- Test Purpose

Verify that the IUT can send DATA.

- Reference

[1] Table 6.1, Section 4

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in the OPEN state for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.

- Test Procedure
- Expected Outcome

Figure 4.2: L2CAP/COS/CED/BV-03-C [Send Data] MSC

## Pass verdict

The IUT transmits L2CAP\_Data over the assigned channel with correct DCID assigned by the Lower Tester.

## L2CAP/COS/CED/BV-04-C [Disconnect]

- Test Purpose

Verify that the IUT can disconnect the data channel.

- Reference

[1] Table 2.2, Table 6.1, 2.2, 4, 4.6

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in the OPEN state for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure

Figure 4.3: L2CAP/COS/CED/BV-04-C [Disconnect] MSC

- Expected Outcome

## Pass verdict

The IUT transmits a correct L2CAP\_DISCONNECTION\_REQ.

## L2CAP/COS/CED/BV-07-C [Accept Disconnect]

- Test Purpose

Verify that the IUT can respond to the request to disconnect the data channel.

- Reference
- [1] Table 2.2, Table 6.1, 2.2, 4, 4.4, 4.5
- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in OPEN state for a data channel with assigned CID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure
- Expected Outcome

Figure 4.4: L2CAP/COS/CED/BV-07-C [Accept Disconnect] MSC

## Pass verdict

The IUT sends a correct L2CAP\_DISCONNECTION\_RSP before the RTX timer expires.

- Notes

The Lower Tester's RTX timer is set to TSPX\_timer\_rtx\_max.

## L2CAP/COS/CED/BV-08-C [Disconnect on Timeout]

- Test Purpose

Verify that the IUT disconnects the data channel and shuts down this channel if no response occurs.

- Reference

[1] 4.6, 4.7, 6.2.1

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in WAIT CONFIG state for a data channel with assigned CID.
- -The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure

Figure 4.5: L2CAP/COS/CED/BV-08-C [Disconnect on Timeout] MSC

The Lower Tester transmits L2CAP\_CONFIGURATION\_REQ 5 seconds after receiving the last L2CAP\_DISCONNECTION\_REQ or 65 seconds after receiving the first L2CAP ConfigReq.

The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP with reason 0x0002 ' Invalid CID in request ' in response to the L2CAP\_CONFIGURATION\_REQ received.

The supplier may be required to state the number of L2CAP\_DISCONNECTION\_REQ retransmissions that the IUT performs.

Following the expiration of TSPX\_timer\_rtx, it is possible that the IUT terminates the ACL -in this case the test stops.

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP\_CONFIGURATION\_REQ to the Lower Tester.

If the IUT retransmits the L2CAP\_CONFIGURATION\_REQ more than once, each subsequent delay is at least twice the previous delay, and the identifier used for the original transmission is also used for each retransmission.

If the IUT sends an L2CAP\_DISCONNECTION\_REQ, it is correctly formatted.

If the IUT retransmits the L2CAP\_DISCONNECTION\_REQ more than once, each subsequent delay is at least twice the previous delay, and the identifier used for the original transmission is also used for each retransmission.

The IUT may terminate the ACL at the expiration of the RTX timer.

If the IUT does not terminate the ACL:

- -The IUT does not transmit an L2CAP\_CONFIGURATION\_RSP to the Lower Tester within 5 seconds of the L2CAP\_CONFIGURATION\_REQ sent by the Lower Tester.
- -The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP with reason 0x0002 ' Invalid CID in request ' in response to the L2CAP\_CONFIGURATION\_REQ received.

## L2CAP/COS/CED/BV-09-C [Receive Multi-Command Packet]

- Test Purpose

Verify that the IUT can receive more than one signaling command in one L2CAP packet.

- Reference

## 1 4

- Initial Condition
- -Either the IUT initiated the connection or the Lower Tester initiated the connection and the IUT is in CONFIG state for a data channel with assigned CID. The IUT may act as either L2CAP initiator or L2CAP acceptor. Either the initiator or responder can send the first L2CAP\_CONFIGURATION\_REQ.
- Test Procedure

Figure 4.6: L2CAP/COS/CED/BV-09-C [Receive Multi-Command Packet] MSC

- Expected Outcome

## Pass verdict

ALT1:

The IUT sends a correctly formatted L2CAP\_CONFIGURATION\_REQ to the Lower Tester, the first on the CID, and, having received an L2CAP\_CONFIGURATION\_RSP and an L2CAP\_CONFIGURATION\_REQ in a single L2CAP packet from the Lower Tester, sends a correctly formatted L2CAP\_CONFIGURATION\_RSP to the Lower Tester within 60s.

## ALT2:

The IUT, having received the first L2CAP\_CONFIGURATION\_REQ from the Lower Tester and having sent a correctly formatted L2CAP\_CONFIGURATION\_RSP to the Lower Tester, sends a correctly formatted L2CAP\_CONFIGURATION\_REQ to the Lower Tester and, upon reception of an L2CAP\_CONFIGURATION\_RSP and an L2CAP\_ECHO\_REQ in a single L2CAP packet from the Lower Tester, sends an L2CAP\_ECHO\_RSP to the Lower Tester within 60s.

## L2CAP/COS/CED/BV-10-C [Transmit I-frames]

- Test Purpose

Verify that IUT can transmit I-frames including correct CRC.

- Reference

[1] 5.4, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.
- Test Procedure

Figure 4.7: L2CAP/COS/CED/BV-10-C [Transmit I-frames] MSC

- Expected Outcome

## Pass verdict

The IUT sends I-frames until TxWindow is full.

Data in the I-frames matches that provided by the Upper Tester. CRC value is set per the specification.

## L2CAP/COS/CED/BV-11-C [Configure MTU Size]

- Test Purpose

Verify that the IUT can configure the supported MTU size.

- Reference

## 1 5

- Initial Condition
- -Maximum supported MTU size set in TSPX\_l2ca\_inmtu.
- -The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure
- Expected Outcome

Figure 4.8: L2CAP/COS/CED/BV-11-C [Configure MTU Size] MSC

## Pass verdict

The IUT sends a correct L2CAP\_CONFIGURATION\_RSP to the Lower Tester accepting the MTU.

The IUT sends a correct L2CAP\_CONFIGURATION\_REQ to the Lower Tester indicating maximum supported MTU.

## L2CAP/COS/CED/BV-12-C [Recombination of Signaling Packets]

- Test Purpose

Verify that the IUT correctly handles fragmented L2CAP signaling PDUs.

- Reference

[1] 3.1, 4.2, 4.3, 7.2.2

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in CLOSED state. No ACL link is established. The IUT acts as L2CAP acceptor.
- Test Procedure

The IUT waits for all the fragments of each C-frame before interpreting the latter, i.e., until the received size of the C-frame equals the value of the PDU Length field of the C-frame + length of the L2CAP header (4 octets).

Figure 4.9: L2CAP/COS/CED/BV-12-C [Recombination of Signaling Packets] MSC

- Expected Outcome

## Pass verdict

The IUT sends correct L2CAP signaling PDUs before the RTX timer expires in response to the correctly recombined L2CAP PDUs sent by the Lower Tester.

- Notes

The Lower Tester's RTX timer is set to maximum allowed initial value.

It is allowed for the IUT to fragment its signaling packets, as well.

## L2CAP/COS/CED/BI-03-C [Incorrect PDU Length, Received Data Packet, Basic]

- Test Purpose

Verify that the IUT properly handles L2CAP Data PDUs that have an invalid PDU length.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The IUT is in the OPEN state with the BR/EDR transport for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure
1. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 3, and 4 octets of Information Payload Data.
2. Perform alternative 2A, 2B, or 2C depending on the IUT 's response.

Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.
- 2A.2 The test ends with a Pass verdict.

Alternative 2B (IUT discards the frame):

- 2B.1 The IUT discards the frame.
- 2B.2 The IUT does not send data to the Upper Tester.

Alternative 2C (Any other IUT response):

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

## L2CAP/COS/CED/BI-30-C [Accept Reject of Connection Request, Peer Older Than v4.2]

- Test Purpose

Verify that the IUT can request the connection establishment for an L2CAP data channel and initiate the configuration procedure.

- Reference

## 19 4.3

- Initial Condition
- -The IUT is an L2CAP Initiator.
- -The IUT is in CLOSED state for data channel. No ACL link is established.
- -It must be possible to send a connection request from the Upper Tester to create an L2CAP channel.

- -The Lower Tester's Bluetooth device address BD\_ADDR is defined. For parameters to send and receive, see [5].
- -The Lower Tester is configured to support Core v4.1.
- Test Procedure

ACL link establishment is part of the test case. The Lower Tester imposes 48 byte MTU for both configuration directions.

Figure 4.10: L2CAP/COS/CED/BI-30-C [Accept Reject of Connection Request, Peer Older Than v4.2] MSC

1. The Upper Tester commands the IUT to send a connection request.
2. The IUT sends an L2CAP\_CONNECTION\_REQ PDU to the Lower Tester.
3. The Lower Tester sends an L2CAP\_COMMAND\_REJECT\_RSP PDU with Reason set to 0x0002.
4. The IUT sends a connection request response to the Upper Tester with an 0x0002 error.
- Expected Outcome

## Pass verdict

In Step 4, the IUT sends an 0x0002 error.

## 4.4.1.1 Incorrect PDU Length, C-Frame

- Test Purpose

Verify that the IUT properly handles L2CAP C-Frame PDUs that have an invalid PDU length.

- Reference

## 1 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The L2CAP signaling channel specified in Table 4.4 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.

- Test Case Configuration
- Test Procedure
1. The Lower Tester sends a C-frame to the IUT with LLID set to 0b10, PDU Length specified in Table 4.4, and Channel ID set to the correct signaling channel for the logical link. The Information payload contains the packet payload request specified in Table 4.4. For the ECHO request, the payload contains 1 octet of ECHO data.
2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT 's response.

Table 4.4: Incorrect PDU Length, C-Frame test cases

| Test Case | Transport | Signaling Channel | L2CAP payload/ PDU_Length/ Payload Length |
| L2CAP/COS/CED/BI-04-C [Incorrect PDU Length, C-Frame, BR/EDR] | BR/EDR | 0x0001 | L2CAP_ECHO_REQ/RSP 4 5 |
| L2CAP/COS/CED/BI-05-C [Incorrect PDU Length, C-Frame, LE Credit Based Connection Request] | LE | 0x0005 | L2CAP_LE_CREDIT_ BASED_CONNECTION_ REQ/RSP 13 14 |
| L2CAP/COS/CED/BI-18-C [Incorrect PDU Length, C-Frame, LE Enhanced Credit Based Connection Request] | LE | 0x0005 | L2CAP_CREDIT_BASED_ CONNECTION_REQ/RSP 13 14 |
| L2CAP/COS/CED/BI-19-C [Incorrect PDU Length, C-Frame, LE Credit Based Connection Request Rejected] | LE | 0x0005 | L2CAP_LE_CREDIT_ BASED_CONNECTION_ REQ L2CAP_COMMAND_ REJECT_RSP 7 8 |

Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.

2A.2 The test ends with a Pass verdict.

Alternative 2B (IUT discards the frame):

2B.1 The IUT does not send a reply to the Lower Tester.

Alternative 2C (IUT rejects PDU):

2C.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP PDU to the Lower Tester.

Alternative 2D (Any other IUT response):

2D.1 The Upper Tester issues a warning and the test ends.

3. The Lower Tester sends a C-frame to the IUT with LLID set to 0b10 and PDU Length set to the payload length specified in Table 4.4. The Information payload contains the payload length specified in Table 4.4 octets of data containing the L2CAP payload. For the ECHO request, the payload contains 1 octet of ECHO data.
4. The IUT sends the L2CAP response PDU specified in Table 4.4 to the Lower Tester.
- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the Upper Tester.

## L2CAP/COS/CED/BI-06-C [Incorrect PDU Length, Received Data Packets with Continuation, Basic]

## · Test Purpose

Verify that the IUT properly handles L2CAP Data PDUs that contain continuation packets that have an invalid PDU length.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The IUT is in the OPEN state with the BR/EDR transport for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure
1. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 11, and 4 octets of Information Payload Data that contains 4 octets of data.
2. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b01 that contains 8 octets of data.
3. Perform alternative 3A, 3B, or 3C depending on the IUT 's response.

Alternative 3A (IUT terminates the link):

- 3A.1 The IUT terminates the link.
- 3A.2 The test ends with a Pass verdict.

Alternative 3B (IUT discards the frame):

- 3B.1 The IUT discards the frame.
- 3B.2 The IUT does not send data to the Upper Tester.
- Alternative 3C (Any other IUT response):
- 3C.1 The Upper Tester issues a warning and the test ends.
4. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b01, PDU Length set to 12, and 8 octets of Information Payload Data that contains 8 octets of data.
5. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 that contains 4 octets of data.
6. The IUT sends the data received in Steps 4 and 5 as one PDU to the Upper Tester.

## · Test Condition

Reliability for the basic mode channel is not needed, so the first PDU in Step 1 can be silently discarded. The IUT can use a finite flush timeout or an ERTM channel.

## · Expected Outcome

## Pass verdict

In Step 3A.1, the IUT terminates the link.

In Step 3B.2, the IUT does not send the data from Step 1 to the Upper Tester.

In Step 3C.1, the IUT sends any valid response.

In Step 6, the IUT sends the data received in Steps 4 and 5 as one PDU to the Upper Tester.

## L2CAP/COS/CED/BI-07-C [Incorrect PDU Length, Received Data Packets with Multiple Continuation]

- Test Purpose

Verify that the IUT properly handles L2CAP Data PDUs that contain multiple continuation packets that have an invalid PDU length.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The IUT is in the OPEN state with the BR/EDR transport for a data channel with assigned SCID and DCID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure
1. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 4, and 4 octets of Information Payload Data that contains 4 octets of data.
2. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 and 8 octets of Information Payload Data that contains 8 octets of data.
3. The IUT sends the data in Step 1 to the Upper Tester as one PDU.
4. Perform alternative 4A, 4B, or 4C depending on the IUT 's response.

Alternative 4A (IUT terminates the link):

- 4A.1 The IUT terminates the link.
- 4A.2 The test ends with a Pass verdict.

Alternative 4B (IUT discards the frame):

- 4B.1 The IUT discards the frame from Step 2.
- 4B.2 The IUT does not send data to the Upper Tester.

Alternative 4C (Any other IUT response):

- 4C.1 The Upper Tester issues a warning and the test ends.
5. The Lower Tester sends an L2CAP Data PDU to the IUT with LLID set to 0b10, PDU Length set to 12, and 4 octets of Information Payload Data that contains 4 octets of data.
6. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 and 8 octets of Information Payload Data that contains 8 octets of data.
7. The Lower Tester sends the continuation of the L2CAP Data PDU to the IUT with LLID set to 0b10 and 8 octets of Information Payload Data that contains 8 octets of data.
8. The IUT sends the data in Steps 5 and 6 as one PDU to the Upper Tester.
9. Perform alternative 9A, 9B, or 9C depending on the IUT 's response.

Alternative 9A (IUT terminates the link):

- 9A.1 The IUT terminates the link.
- 9A.2 The test ends with a Pass verdict.

Alternative 9B (IUT discards the frame):

- 9B.1 The IUT discards the frame from Step 7.
- 9B.2 The IUT does not send data to the Upper Tester.

Alternative 9C (Any other IUT response):

- 9C.1 The Upper Tester issues a warning and the test ends.

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

## 4.4.1.2 Valid Signaling Command, Data Length &gt; PDU Space

- Test Purpose

Verify that the IUT properly handles incorrect L2CAP signaling command packets with invalid Data length.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The L2CAP signaling channel specified in Table 4.5 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.
- Test Case Configuration

| Test Case | Transport | Signaling Channel | L2CAP payload/ PDU_Length/ Data Length |
| L2CAP/COS/CED/BI-08-C [Valid Signaling Command, Data Length > PDU Space, BR/EDR] | BR/EDR | 0x0001 | L2CAP_ECHO_REQ/RSP 7 4 |
| L2CAP/COS/CED/BI-09-C [Valid Signaling Command, Data Length > PDU Space, LE Credit Based Connection Request] | LE | 0x0005 | L2CAP_LE_CREDIT_ BASED_CONNECTION_ REQ/RSP 14 11 |

Table 4.5: Valid Signaling Command, Data Length &gt; PDU Space test cases

| Test Case | Transport | Signaling Channel | L2CAP payload/ PDU_Length/ Data Length |
| L2CAP/COS/CED/BI-20-C [Valid Signaling Command, Data Length > PDU Space, LE Enhanced Credit Based Connection Request] | LE | 0x0005 | L2CAP_CREDIT_ BASED_CONNECTION_ REQ/RSP 14 11 |
| L2CAP/COS/CED/BI-21-C [Valid Signaling Command, Data Length > PDU Space, LE Credit Based Connection Request Rejected] | LE | 0x0005 | L2CAP_LE_CREDIT_ BASED_CONNECTION_ REQ L2CAP_COMMAND_ REJECT_RSP 8 5 |

- Test Procedure
1. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.5 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length and L2CAP payload set as specified in Table 4.5. For the ECHO request, the payload contains 3 octets of ECHO data.
2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT 's response.

Alternative 2A (IUT terminates the link):

2A.1 The IUT terminates the link.

2A.2 The test ends with a Pass verdict.

Alternative 2B (IUT discards the frame):

2B.1 The IUT does not send a reply to the Lower Tester.

Alternative 2C (IUT rejects PDU):

2C.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP PDU to the Lower Tester.

Alternative 2D (Any other IUT response):

2D.1 The Upper Tester issues a warning and the test ends.

3. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.5 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains the correct data length for the L2CAP payload specified in Table 4.5. For the ECHO request, the payload contains 3 octets of ECHO data.
4. The IUT sends the L2CAP response PDU specified in Table 4.5 to the Lower Tester.
- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the Lower Tester.

## 4.4.1.3 Incorrect Signaling Command Packets, Invalid Data Length for Command

- Test Purpose

Verify that the IUT properly handles incorrect L2CAP signaling command packets with invalid Data length.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The L2CAP signaling channel specified in Table 4.6 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.
- Test Case Configuration

Table 4.6: Incorrect Signaling Command Packets, Invalid Data Length for Command test cases

| Test Case | Transport | Signaling Channel | Execute Steps 3 and 4 |
| L2CAP/COS/CED/BI-10-C [Incorrect Signaling Command Packets, Invalid Data Length for Command, BR/EDR] | BR/EDR | 0x0001 | Yes |
| L2CAP/COS/CED/BI-11-C [Incorrect Signaling Command Packets, Invalid Data Length for Command, LE] | LE | 0x0005 | No |

## · Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length set to 9 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 5 with an L2CAP\_DISCONNECTION\_REQ packet followed by an octet with value 0x00.
2. Perform alternatives 2A, 2B, 2C, or 2D depending on the IUT 's response.

Alternative 2A (IUT terminates the link):

2A.1 The IUT terminates the link.

2A.2 The test ends with a Pass verdict.

Alternative 2B (IUT discards the frame):

2B.1 The IUT does not send a reply to the Lower Tester.

Alternative 2C (IUT rejects PDU):

2C.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP PDU to the Lower Tester.

Alternative 2D (Any other IUT response):

2D.1 The Upper Tester issues a warning and the test ends.

Execute Steps 3 and 4 if indicated in Table 4.6.

3. The Lower Tester sends a C-frame to the IUT with PDU Length set to 7 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 3 with an L2CAP\_ECHO\_REQ packet with 3 octets of echo data.
4. The IUT sends an L2CAP\_ECHO\_RSP PDU to the Lower Tester.

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

- In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the Lower Tester.

## L2CAP/COS/CED/BI-12-C [Valid Signaling Command, Shorter Data Length, Extra Zero Octet, BR/EDR]

## · Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with extra data in the Information Payload.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The BR/EDR L2CAP signaling channel 0x0001 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.
- Test Procedure
1. The Lower Tester sends a C-frame to the IUT with PDU Length set to 9 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 4 with an L2CAP\_ECHO\_REQ packet with 4 octets of echo data followed by a 0 octet.
2. Perform alternative 2A or 2B depending on the IUT 's response.

Alternative 2A (Send the echo response):

- 2A.1 The IUT sends an L2CAP\_ECHO\_RSP PDU to the Lower Tester.

Alternative 2B (Disconnect):

- 2B.1 The IUT terminates the link.
- 2B.2 The test ends with a Pass verdict.
3. Perform alternative 3A, 3B, or 3C depending on the IUT 's response.

Alternative 3A (Reject the signaling command):

- 3A.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP to the Lower Tester with Reason set to 0x0000.

Alternative 3B (Disconnect):

- 3B.1 The IUT terminates the link.

Alternative 3C (Ignore the invalid command):

- 3C.1 The IUT does not send a response to the Lower Tester.
- 3C.2 The Lower Tester sends a C-frame to the IUT with PDU Length set to 8 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 4 with an L2CAP\_ECHO\_REQ packet with 4 octets of echo data.
- 3C.3 The IUT sends an L2CAP\_ECHO\_RSP PDU to the Lower Tester.

- Expected Outcome

## Pass verdict

In Step 2, the IUT responds to the L2CAP\_ECHO\_REQ from Step 1.

In Step 3A, the IUT rejects the command from Step 1.

In Step 2B or 3B, the IUT disconnects the link.

In Step 3C, the IUT ignores the invalid command and responds to the ECHO request.

## 4.4.1.4 Valid Signaling Command, Data Length &gt; PDU Space

- Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with extra data in the Information Payload.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The LE L2CAP signaling channel 0x0005 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.

## · Test Case Configuration

| Test Case | Transport | Signaling Channel | L2CAP payload | Step 1 PDU Length / Data Length | Step 3 PDU Length / Data Length |
| L2CAP/COS/CED/BI-13-C [Valid Signaling Command, Shorter Data Length, Extra Zero Octet, LE Credit Based Connection Request] | LE | 0x0005 | L2CAP_LE_CREDIT_ BASED_CONNECTION_ REQ/RSP | 15 10 | 14 10 |
| L2CAP/COS/CED/BI-22-C [Valid Signaling Command, Shorter Data Length, Extra Zero Octet, LE Enhanced Credit Based Connection Request] | LE | 0x0005 | L2CAP_CREDIT_ BASED_CONNECTION_ REQ/RSP | 15 10 | 14 10 |
| L2CAP/COS/CED/BI-23-C [Valid Signaling Command, Shorter Data Length, Extra Zero Octet, LE Enhanced Credit Based Connection Request Rejected] | LE | 0x0005 | L2CAP_CREDIT_ BASED_CONNECTION_ REQ L2CAP_COMMAND_ REJECT_RSP | 9 4 | 8 4 |

Table 4.7: Valid Signaling Command, Data Length &gt; PDU Space test cases

- Test Procedure
1. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.7 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set as specified in Table 4.7 with an L2CAP packet payload request as specified in Table 4.7 with data length octets of connection data followed by a 0 octet.
2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT 's response.

Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.
- 2A.2 The test ends with a Pass verdict.

Alternative 2B (IUT discards the frame):

- 2B.1 The IUT does not send a reply to the Lower Tester.

Alternative 2C (IUT rejects PDU):

2C.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP PDU to the Lower Tester.

Alternative 2D (Any other IUT response):

- 2D.1 The Upper Tester issues a warning and the test ends.
3. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.7 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains an L2CAP packet payload request as specified in Table 4.7 with Data Length set as specified in Table 4.7 and with data length octets of connection request data.
4. The IUT sends the L2CAP response PDU specified in Table 4.7 to the Lower Tester. If that response is L2CAP\_COMMAND\_REJECT\_RSP, the test ends with a Pass verdict.
5. The Lower Tester sends an L2CAP\_DISCONNECTION\_REQ PDU to the IUT.
6. The IUT sends an L2CAP\_DISCONNECTION\_RSP PDU to the Lower Tester.
- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the connection request in Step 3.

## 4.4.1.5 Multiple Signaling Command in one PDU, Data Truncated, BR/EDR

- Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with a Data Length of 0 in the Information Payload.

- Reference

## 1 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The BR/EDR L2CAP signaling channel 0x0001 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.

- Test Case Configuration
- Test Procedure
1. The Lower Tester sends a C-frame to the IUT with PDU Length as specified in Table 4.8 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains one L2CAP\_ECHO\_REQ packet with Data Length set to 0 with 0 octets of echo data and one command packet and Data Length set as specified in Table 4.8.
2. The IUT may send an L2CAP\_ECHO\_RSP PDU to the Lower Tester.
3. Perform alternative 3A, 3B, 3C, or 3D depending on the IUT 's response.

Table 4.8: Multiple Signaling Command in one PDU, Data Truncated, BR/EDR test cases

| Test Case | Second Command/Response | Second Command Data Length | PDU Length |
| L2CAP/COS/CED/BI-14-C [Multiple Signaling Command in one PDU, Data Truncated, BR/EDR, Echo Request] | L2CAP_ECHO_REQ L2CAP_ECHO_RSP | 1 | 8 |
| L2CAP/COS/CED/BI-15-C [Multiple Signaling Command in one PDU, Data Truncated, BR/EDR, Disconnection Request] | L2CAP_DISCONNECTION_ REQ L2CAP_DISCONNECTION_ RSP | 0 | 8 |

Alternative 3A (IUT terminates the link):

3A.1 The IUT terminates the link.

3A.2 The test ends with a Pass verdict.

Alternative 3B (IUT discards the frame):

3B.1 The IUT does not send a reply to the Lower Tester.

Alternative 3C (IUT rejects PDU):

3C.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP PDU to the Lower Tester.

Alternative 3D (Any other IUT response):

- 3D.1 The Upper Tester issues a warning and the test ends.
4. The Lower Tester sends a C-frame to the IUT with PDU Length set to 4 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains Data Length set to 0 with an L2CAP\_ECHO\_REQ packet with 0 octets of echo data.
5. The IUT sends an L2CAP\_ECHO\_RSP PDU to the Lower Tester.
- Expected Outcome

## Pass verdict

In Step 5, the IUT responds with an L2CAP\_ECHO\_RSP.

In Step 3A.1, the IUT terminates the link.

In Step 3B.1, the IUT does not send a reply to the Lower Tester.

In Step 3C.1, the IUT rejects the PDU.

In Step 3D.1, the IUT sends any valid response.

## 4.4.1.6 Multiple Signaling Command in one PDU, Data Truncated, LE

- Test Purpose

Verify that the IUT properly handles invalid L2CAP signaling command packets with an incorrect PDU length in the Information Payload.

- Reference

[1] 3.1, 4

- Initial Condition
- -The Lower Tester uses version L2CAP Basic Mode.
- -No security is used in this test case.
- -The LE L2CAP signaling channel 0x0005 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.

## · Test Case Configuration

| Test Case | PDU Length | First Command/Response | First Command Data Length | Second Command/Response | Second Command Data Length |
| L2CAP/COS/CED/BI-16-C [Multiple Signaling Command in one PDU, Data Truncated, LE Credit Based Flow Control Mode, LE Credit Based Connection Request] | 28 | L2CAP_LE_CREDIT_BASED_ CONNECTION_REQ L2CAP_LE_CREDIT_BASED_ CONNECTION_RSP | 10 | L2CAP_LE_CREDIT_BASED_ CONNECTION_REQ L2CAP_LE_CREDIT_BASED_ CONNECTION_RSP | 11 |
| L2CAP/COS/CED/BI-17-C [Multiple Signaling Command in one PDU, Data Truncated, LE Credit Based Flow Control Mode, Disconnection Request] | 22 | L2CAP_LE_CREDIT_BASED_ CONNECTION_REQ L2CAP_LE_CREDIT_BASED_ CONNECTION_RSP | 10 | L2CAP_DISCONNECTION_ REQ L2CAP_DISCONNECTION_ RSP | 5 |
| L2CAP/COS/CED/BI-24-C [Multiple Signaling Command in one PDU, LE, Data Truncated, Enhanced Credit Based Flow Control Mode, Enhanced Credit Based Connection Request] | 28 | L2CAP_CREDIT_BASED_ CONNECTION_REQ L2CAP_CREDIT_BASED_ CONNECTION_RSP | 10 | L2CAP_CREDIT_BASED_ CONNECTION_REQ L2CAP_CREDIT_BASED_ CONNECTION_RSP | 11 |
| L2CAP/COS/CED/BI-25-C [Multiple Signaling Command in one PDU, LE, Data Truncated, Enhanced Credit Based Flow Control Mode, Disconnection Request] | 22 | L2CAP_CREDIT_BASED_ CONNECTION_REQ L2CAP_CREDIT_BASED_ CONNECTION_RSP | 10 | L2CAP_DISCONNECTION_ REQ L2CAP_DISCONNECTION_ RSP | 5 |

Table 4.9: Multiple Signaling Command in one PDU, Data Truncated, LE test cases

## · Test Procedure

1. The Lower Tester sends a C-frame to the IUT with PDU Length set as specified in Table 4.9 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains one first L2CAP command request packet, Data Length, and connection request data size as specified in Table 4.9 and one second command request packet and Data Length set as specified in Table 4.9 and the correct command data.
2. Perform alternative 2A, 2B, 2C, or 2D depending on the IUT 's response.

Alternative 2A (IUT terminates the link):

- 2A.1 The IUT terminates the link.

2A.2 The test ends with a Pass verdict.

Alternative 2B (IUT discards the frame):

- 2B.1 The IUT does not send a reply to the Lower Tester.

Alternative 2C (IUT rejects PDU):

- 2C.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP PDU to the Lower Tester.

Alternative 2D (Any other IUT response):

- 2D.1 The Upper Tester issues a warning and the test ends.
3. The Lower Tester sends a C-frame to the IUT with PDU Length set to 14 and Channel ID set to the correct signaling channel for the logical link. The Information payload contains a first L2CAP command request packet, Data Length, and connection request data size as specified in Table 4.9.
4. The IUT sends the first L2CAP response PDU to the Lower Tester.
5. The Lower Tester sends an L2CAP\_DISCONNECTION\_REQ PDU to the IUT.
6. The IUT sends an L2CAP\_DISCONNECTION\_RSP PDU to the Lower Tester.
- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT terminates the link.

In Step 2B.1, the IUT does not send a reply to the Lower Tester.

In Step 2C.1, the IUT rejects the PDU.

In Step 2D.1, the IUT sends any valid response.

In Step 4, the IUT sends a response to the connection request in Step 4.

## 4.4.1.7 Ignore Command Response with Invalid ID or Duplicate Response

- Test Purpose

Verify that the IUT ignores a Command Response with an Invalid ID and a duplicate response. The Invalid ID can be an ID of 0. The test also verifies that identifiers are not duplicated until all valid identifiers have been used.

- Reference

## 1 4

- Initial Condition
- -The IUT is in CLOSED state for data channel. No ACL link is established.
- -No security is used in this test case.
- -The L2CAP signaling channel specified in Table 4.10 is established between the IUT and the Lower Tester.
- -The IUT is in CLOSED state and acts as an L2CAP acceptor.

- Test Case Configuration

| Test Case | Transport | Signaling Channel | L2CAP Signaling Packet |
| L2CAP/COS/CED/BI-28-C [Ignore Command Response with Invalid ID or Duplicate Response, BR/EDR] | BR/EDR | 0x0001 | L2CAP_CONNECTION_ REQ/RSP |
| L2CAP/COS/CED/BI-29-C [Ignore Command Response with Invalid ID or Duplicate Response, LE] | LE | 0x0005 | L2CAP_LE_CREDIT_ BASED_CONNECTION_ REQ/RSP |

Table 4.10: Ignore Command Response with Invalid ID or Duplicate Response test cases

## · Test Procedure

Figure 4.11: Ignore Command Response with Invalid ID or Duplicate Response MSC

1. The Upper Tester commands the IUT to start the procedure that initiates the connection request specified in Table 4.10.
2. The IUT sends an L2CAP request PDU specified in Table 4.10 to the Lower Tester with an Identifier. The Lower Tester saves the Identifier.
3. The Lower Tester sends a successful L2CAP response PDU specified in Table 4.10 to the IUT with the Identifier set to 0. The IUT and the Lower Tester do not make a connection.
4. The Lower Tester sends an unsuccessful L2CAP response PDU specified in Table 4.10 to the IUT with the identifier from Step 2, and a non-zero Result. The IUT and the Lower Tester do not make a connection.

5. Repeat Steps 1 -4 with the Identifier in Step 3 set to any non-zero value other than the two values saved in Step 2.
6. Repeat Steps 1 -4 253 times with the Identifier in Step 3 set to 0x00. The test fails if the IUT reuses an Identifier that already was used.
7. The Upper Tester commands the IUT to start the procedure that initiates the connection request specified in Table 4.10.
8. The IUT sends an L2CAP request PDU specified in Table 4.10 to the Lower Tester with an Identifier.
9. The Lower Tester sends a successful L2CAP response PDU specified in Table 4.10 to the IUT with the Identifier set to the value in Step 8.
10. If the Transport is BR/EDR, the Lower Tester and the IUT may execute the L2CAP Configuration Process.
11. The IUT sends a connection complete event to the Upper Tester.
12. The Lower Tester sends the same L2CAP response PDU as was sent in Step 9.
13. If the IUT sends a connection complete event to the Upper Tester, the test ends with a Fail verdict.
14. The Lower Tester sends an L2CAP\_DISCONNECTION\_REQ PDU to the IUT.
15. The IUT sends an L2CAP\_DISCONNECTION\_RSP PDU to the Lower Tester.
- Expected Outcome

## Pass verdict

In Step 4, the IUT and the Lower Tester do not make a connection.

In Step 15, the IUT sends an L2CAP\_DISCONNECTION\_RSP PDU.

## Fail verdict

The IUT reuses an Identifier in Step 2 in the first 255 repeats.

In Step 13, the IUT sends a connection complete event.

## 4.4.2 Encryption Key Size

Tests for insufficient encryption key size require an encrypted link with a key size less than the size required by an L2CAP channel. The encryption key size requirements of attributes are determined by the associated profile.

## Preamble procedure:

Establish an encrypted link over the LE transport between the IUT and the Lower Tester. For example, see test SM/CEN/EKS/BV-01-C or SM/PER/EKS/BV-02-C in [16] for LE transport, or LMP/ENC/BV-01-C or LMP/ENC/BV-05-C in [17] for BR/EDR transport. The key size is less than the size required by the security requirements of the L2CAP channel.

## 4.4.3 Configuration of Data Channel CFD

Verify the procedures for configuration of a data channel.

## L2CAP/COS/CFD/BV-01-C [Continuation Flag]

- Test Purpose

Verify that the IUT can receive configuration requests that have the continuation flag set.

- Reference

[1] Table 6.1, 4.4, 4.5, 5

- Initial Condition
- -The IUT is in CONFIG state for a data channel with assigned CID. The IUT's request path is already configured. The connection was initiated from the Lower Tester.
- Test Procedure
- Test Condition

Figure 4.12: L2CAP/COS/CFD/BV-01-C [Continuation Flag] MSC

Acceptable configuration parameter values are supplied by the manufacturer.

- Expected Outcome

## Pass verdict

The IUT responds to each L2CAP\_CONFIGURATION\_REQ message with an L2CAP\_CONFIGURATION\_RSP message indicating "success". The response to the first message has the continuation flag set. The final response has the continuation flag cleared. One of the two responses indicates an MTU size equal to that in the request.

- Notes

The Lower Tester sets the most significant bit of the type parameter to '1', indicating a "hint", for the optional parameters Quality of Service, and Retransmission and Flow Control. If the IUT supports the optional parameter, it accepts the default value; if it does not support an optional parameter, it should ignore the hint and take no additional action.

## L2CAP/COS/CFD/BV-02-C [Negotiation with Reject]

- Test Purpose

Verify that the IUT can perform negotiation while the Lower Tester rejects the proposed configuration parameter values.

- Reference

[1] Table 6.1, 4.4, 4.5

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in CONFIG state for a data channel with assigned CID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure
- Test Condition

Figure 4.13: L2CAP/COS/CFD/BV-02-C [Negotiation with Reject] MSC

Acceptable configuration parameter values have to be stated by the manufacturer.

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_REQ with acceptable values received in the L2CAP\_CONFIGURATION\_RSP with Result= Failure -unacceptable parameters or the L2CAP\_CONFIGURATION\_REQ contains no options.

or

The IUT closes the channel.

## L2CAP/COS/CFD/BV-03-C [Send Requested Options]

- Test Purpose

Verify that the IUT can receive a configuration request with no options and send the requested options to the Lower Tester.

- Reference

[1] Table 6.1, 4.4, 4.5

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in CONFIG state for data channel with assigned CID. The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure
- Expected Outcome

Figure 4.14: L2CAP/COS/CFD/BV-03-C [Send Requested Options] MSC

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_RSP before expiration of RTX timer.

- Notes

The Lower Tester uses TSPX\_timer\_rtx\_max for RTX timer.

## L2CAP/COS/CFD/BV-08-C [Non-blocking Config Response]

- Test Purpose

Verify that the IUT does not block transmitting L2CAP\_CONFIGURATION\_RSP while waiting for L2CAP\_CONFIGURATION\_RSP from the Lower Tester.

- Reference

[1] 4.4, 4.5

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in CONFIG state for a channel with CID. The IUT acts as L2CAP initiator.

- Test Procedure
- Expected Outcome

Figure 4.15: L2CAP/COS/CFD/BV-08-C [Non-blocking Config Response] MSC

## Pass verdict

After receiving L2CAP\_CONFIGURATION\_REQ from the Lower Tester, the IUT transmits L2CAP\_CONFIGURATION\_RSP to the Lower Tester.

- Notes

The Lower Tester uses an MTU value not exceeding what is transmitted from the IUT in the L2CAP\_CONFIGURATION\_REQ. Other options have default or accepted values, and hence, need not be transmitted. It is implementation dependent which options are transmitted by the IUT.

## L2CAP/COS/CFD/BV-09-C [Mandatory 48 Byte MTU]

- Test Purpose

Verify that the IUT can support mandatory 48 byte MTU.

- Reference

[1] 5.1, 7.1

- Initial Condition
- -The IUT is in CONFIG state for a channel with CID.
- -The IUT acts as L2CAP initiator.

## · Test Procedure

Figure 4.16: L2CAP/COS/CFD/BV-09-C [Mandatory 48 Byte MTU] MSC

- Expected Outcome

## Pass verdict

The IUT transmits a configuration request containing InMTU or omit the InMTU. Regardless of indicated MTU, when the Lower Tester responds with MTU=48 the configuration completes successfully without further negotiation.

The IUT responds with MTU=48 or omit the MTU in its configuration response. The configuration completes successfully without further negotiation.

- Notes

In part 1, the IUT may request any MTU &gt; 48.

## L2CAP/COS/CFD/BV-10-C [Retransmission Mode Negotiation]

- Test Purpose

Verify that the IUT can negotiate L2CAP F+E for Retransmission mode.

- Reference

[1] 5.3, 7.4

- Initial Condition
- -The IUT is in CONFIG state for a data channel with assigned CID.
- Test Procedure
- Expected Outcome

Figure 4.17: L2CAP/COS/CFD/BV-10-C [Retransmission Mode Negotiation] MSC

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_REQ with L2CAP Flow and Error control option for Retransmission mode.

## L2CAP/COS/CFD/BV-11-C [Negotiation of Unsupported Parameter]

- Test Purpose

Verify that the IUT can negotiate when the Lower Tester proposes an unsupported configuration parameter value.

- Reference

[1] 4.4, 4.5

- Initial Condition
- -The Lower Tester performs an Information Request/Response command to read the supported mode of the IUT.
- -The Lower Tester then sends a Configuration Request with unsupported configuration parameters to the IUT.

- Test Procedure

The Lower Tester proposes configuration parameter values the IUT does not support.

The IUT acts either as L2CAP initiator or as L2CAP acceptor.

Figure 4.18: L2CAP/COS/CFD/BV-11-C [Negotiation of Unsupported Parameter] MSC

- Expected Outcome

## Pass verdict

The IUT negotiates the configuration parameters to supported values (ALT 1). If NO unacceptable options are possible, the IUT may respond as shown in ALT 2.

## L2CAP/COS/CFD/BV-12-C [Unknown Option Response]

- Test Purpose

Verify that the IUT can give the appropriate error code when the Lower Tester proposes any number of unknown options that are optional.

- Reference

[1] 4.4, 4.5

- Initial Condition
- -The IUT is in CONFIG state. Supported configuration option types are given as the TSPX\_supported\_config\_options IXIT value.
- -The IUT either acts as L2CAP initiator or as L2CAP acceptor.
- Test Procedure

Repeat the steps for each round in Table 4.11.

The Lower Tester transmits a configuration request with a number of options as specified in Table 4.11 where the option types are not supported by the IUT and all have the MSB set to 1.

Table 4.11: L2CAP/COS/CFD/BV-12-C [Unknown Option Response] rounds

| Round | Number of Options |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 10 |

Figure 4.19: L2CAP/COS/CFD/BV-12-C [Unknown Option Response] MSC

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP\_CONFIGURATION\_RSP before expiration of RTX timer.

## L2CAP/COS/CFD/BV-13-C [Flow Control Mode Negotiation]

- Test Purpose

Verify that the IUT can negotiate L2CAP F+E for Flow Control only mode.

- Reference

## 1 5.4, 7.4

- Initial Condition
- -The IUT is in CONFIG state for a data channel with assigned CID.

- Test Procedure
- Expected Outcome

Figure 4.20: L2CAP/COS/CFD/BV-13-C [Flow Control Mode Negotiation] MSC

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_REQ with L2CAP Flow and Error control option for Flow Control only mode.

## L2CAP/COS/CFD/BV-14-C [Unknown Mandatory Options Request]

- Test Purpose

Verify that the IUT can give the appropriate error code when the Lower Tester proposes any number of unknown options where at least one is mandatory.

- Reference

[1] 4.4, 4.5

- Initial Condition
- -The IUT is in CONFIG state. Supported configuration option types are given as the TSPX\_supported\_config\_options IXIT value.
- -The IUT acts either as L2CAP initiator or as L2CAP acceptor.
- Test Procedure

The Lower Tester transmits a configuration request with a number of options as specified in Table 4.12 where the option types are not supported by the IUT and have the MSBs set as specified in Table 4.12.

| Round | Number of Options | MSB value |
| 1 | 1 | All set to 0 |
| 2 | 2 | All set to 1, except the last one set to 0 |
| 3 | 3 | All set to 0 |
| 4 | 4 | Two at random set to 0, the rest set to 1 |
| 5 | 5 | All set to 1, except the last one set to 0 |
| 6 | 6 | Two at random set to 0, the rest set to 1 |

Table 4.12: L2CAP/COS/CFD/BV-14-C [Unknown Mandatory Options Request] rounds

| Round | Number of Options | MSB value |
| 7 | 7 | All set to 0 |
| 8 | 8 | All set to 1, except the last one set to 0 |
| 9 | 9 | Two at random set to 0, the rest set to 1 |
| 10 | 10 | All set to 1, except the last one set to 0 |

Figure 4.21: L2CAP/COS/CFD/BV-14-C [Unknown Mandatory Options Request] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_CONFIGURATION\_RSP with Result=0x0003 and specifying one of the unsupported options that has the MSB set to 0.

## 4.4.4 Implementation-Specific Information Exchange IEX

Verify the implementation-specific information exchange feature.

## L2CAP/COS/IEX/BV-01-C [Query for 1.2 Features]

- Test Purpose

Verify that the IUT transmits an information request command to solicit if the remote device supports Specification 1.2 features.

- Reference

[1] 4.10, 4.11

- Initial Condition
- -The IUT is in any state.

- Test Procedure
- Expected Outcome

Figure 4.22: L2CAP/COS/IEX/BV-01-C [Query for 1.2 Features] MSC

## Pass verdict

The IUT transmits L2CAP\_INFORMATION\_REQ with InfoType=0x0002.

## L2CAP/COS/IEX/BV-02-C [Respond with 1.2 Features]

- Test Purpose

Verify that the IUT responds to an information request command soliciting for Specification 1.2 features.

- Reference

[1] 4.10, 4.11, 4.12

- Initial Condition
- -The IUT is in any state.
- Test Procedure
- Expected Outcome

Figure 4.23: L2CAP/COS/IEX/BV-02-C [Respond with 1.2 Features] MSC

## Pass verdict

The IUT transmits L2CAP\_INFORMATION\_RSP with InfoType=0x0002.

If the IUT supports any extended features:

The Result=Success and Data is formatted correctly for an Extended Feature Mask.

Otherwise:

The Result=Success, and Data is set to 0x0000 0000, OR

The Result=Not Supported, and Data is not present.

## L2CAP/COS/IEX/BI-01-C [Accept Reject of Information Request, Peer Older Than v3.0]

- Test Purpose

Verify that the IUT transmits an information request command to solicit if the remote device supports Specification 1.2 features.

- Reference

[1] 4.11

- Initial Condition
- -The IUT is in any state.
- -The Lower Tester is configured to support Core v2.1.
- Test Procedure
1. The Upper Tester commands the IUT to send an information request.
2. The IUT sends an L2CAP\_INFORMATION\_REQ PDU to the Lower Tester.
3. The Lower Tester sends an L2CAP\_INFORMATION\_RSP PDU to the IUT with Result set to 'Not Supported'.
4. The IUT sends an Information Request Response to the Upper Tester with a 'Not Supported' error.
- Expected Outcome

Figure 4.24: L2CAP/COS/IEX/BI-01-C [Accept Reject of Information Request, Peer Older Than v3.0] MSC

## Pass verdict

In Step 4, the IUT sends a 'Not Supported' error.

## 4.4.5 Echo Handling ECH

Verify the procedures for echo handling, which means link testing and passing of vendor-specific information with the ECHO\_REQUEST and ECHO\_RESPONSE signaling command.

## L2CAP/COS/ECH/BV-01-C [Respond to Echo Request]

- Test Purpose

Verify that the IUT responds to an echo request.

- Reference

[1] Table 6.1, 4.8, 4.9

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in CLOSED state for data channel. No ACL link is established. The IUT acts as L2CAP acceptor.
- Test Procedure
- Expected Outcome

Figure 4.25: L2CAP/COS/ECH/BV-01-C [Respond to Echo Request] MSC

## Pass verdict

The IUT sends an L2CAP\_ECHO\_RSP before expiration of RTX timer.

- Notes

The Lower Tester uses maximum value for RTX timer.

## L2CAP/COS/ECH/BV-02-C [Send Echo Request]

- Test Purpose

Verify that the IUT sends an echo request.

- Reference
- [1] Table 6.1, 4.8, 4.9

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT is in CLOSED state for data channel. No ACL link is established. The IUT acts as L2CAP initiator.
- Test Procedure

ACL link establishment is part of the test case.

Figure 4.26: L2CAP/COS/ECH/BV-02-C [Send Echo Request] MSC

- Test Condition

It must be possible to send an echo request from the Upper Tester to the Lower Tester.

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP\_ECHO\_REQ.

## 4.4.6 LE Credit Based Flow Control Mode

Verify the correct implementation of the data channel in LE Credit Based Flow Control mode.

## L2CAP/COS/CFC/BV-01-C [Segmentation]

- Test Purpose

Verify that the IUT can send data segments that are larger than the K-frame payload size.

- Reference

[12] 3.4

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An LE Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value with credits returned to the IUT by the Lower Tester.
- -The role of the IUT is indicated via TSPX\_iut\_role\_initiator.
- -The MTU and MPS of the Lower Tester are indicated in the TSPX\_tester\_mtu and TSPX\_tester\_mps IXIT values.
- -The Upper Tester can command the IUT to send data.

- Test Procedure

Figure 4.27: L2CAP/COS/CFC/BV-01-C [Segmentation] MSC

The Upper Tester sends a data packet to the IUT which is larger than or equal to the Lower Tester's MPS and smaller than or equal to the Lower Tester's MTU.

- Expected Outcome

## Pass verdict

The IUT sends at least one K-frame containing data to the Lower Tester.

If the Upper Test sends a data packet to the IUT which is larger than the Lower Tester's MPS and smaller than the Lower Tester's MTU, the IUT segments the K-frames correctly.

The data sent by the IUT to the Lower Tester matches the data sent to the IUT by the Upper Tester.

## L2CAP/COS/CFC/BV-02-C [No Segmentation]

- Test Purpose

Verify that the IUT can send data segments that do not require segmentation.

- Reference

[12] 3.4

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An LE Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value with credits returned to the IUT by the Lower Tester.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

- Test Procedure

Figure 4.28: L2CAP/COS/CFC/BV-02-C [No Segmentation] MSC

The Upper Tester sends a data packet of one octet to the IUT.

- Expected Outcome

## Pass verdict

The IUT send a K-frame containing the data to the Lower Tester.

The data sent by the IUT to the Lower Tester matches the data sent to the IUT by the Upper Tester.

## L2CAP/COS/CFC/BV-03-C [Reassembling]

- Test Purpose

Verify that the IUT can correctly reassemble data received from the Lower Tester where the L2CAP SDU Length is greater than the IUT K-frame payload size.

- Reference

## 12 3.4

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An LE Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

- Test Procedure

Figure 4.29: L2CAP/COS/CFC/BV-03-C [Reassembling] MSC

(Optional) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data in a series of K-frames to the IUT with the L2CAP SDU Length smaller than the IUT MTU.

- Expected Outcome

## Pass verdict

The IUT correctly reassembles the data received from the Lower Tester and sends it to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## L2CAP/COS/CFC/BV-04-C [Data Receiving]

- Test Purpose

Verify that the IUT can receive unsegmented data correctly.

- Reference

## 12 3.4

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An LE Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

- Test Procedure

Figure 4.30: L2CAP/COS/CFC/BV-04-C [Data Receiving] MSC

(Optional) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data in a single K-frame to the IUT. The SDU length is less than or equal to the length of the K-frame - 2.

- Expected Outcome

## Pass verdict

The IUT sends the received data to the Upper Tester

The data sent to the Upper Tester by the IUT matches the data sent by the Lower Tester to the IUT

## L2CAP/COS/CFC/BV-05-C [Multiple Channels with Interleaved Data Streams]

- Test Purpose

Verify that an IUT can create multiple channels and receives data streams on the channels when the streams are interleaved.

- Reference

## 12 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -The LE Data Channel is established using the SPSM declared via the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

## · Test Procedure

Figure 4.31: L2CAP/COS/CFC/BV-05-C [Multiple Channels with Interleaved Data Streams] MSC

(Optional) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data on the different channels interleaved.

## · Expected Outcome

## Pass verdict

The IUT sends the received data to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## 4.4.6.1 Recombination of Signaling Packets

- Test Purpose

Verify that the IUT correctly handles fragmented L2CAP signaling PDUs.

- Initial Condition
- -The signaling channel specified in Table 4.13 is used.
- -An SPSM for the desired Credit Based or Enhanced Credit Based Flow Control based channel is declared via the TSPX\_spsm IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-30-C [Recombination of Signaling Packets] | [1] 4.22, 4.23 | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-39-C [Recombination of Signaling Packets - LE] | [1] 4.25, 4.26 | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-40-C [Recombination of Signaling Packets - BR/EDR] | [1] 4.25, 4.26 | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.13: Recombination of Signaling Packets test cases

- Test Procedure

Figure 4.32: Recombination of Signaling Packets MSC

The L2CAP Credit Based Connection Request/Response commands are specified in Table 4.13.

The Lower Tester sends a valid connection request command, with nonzero credits to the IUT on the SPSM specified in the initial condition, fragmented into two fragments.

The IUT responds with a connection request response and establishes the credit-based channel.

- Expected Outcome

## Pass verdict

The IUT sends a correct connection request response in response to the connection request command received in the recombined C-frame.

- Note

It is allowed for the IUT to fragment its signaling packets, as well.

## 4.4.6.2 Recombination of Data Packets

- Test Purpose

Verify that the IUT correctly handles fragmented L2CAP data PDUs.

- Reference

## 12 3.4

- Initial Condition
- -The signaling channel specified in Table 4.14 is used.
- -A Data Channel over the relevant bearer is established on the SPSM declared via the TSPX\_spsm IXIT value using the commands specified in Table 4.14.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-31-C [Recombination of Data Packets] | [1] 3.4, 7.2.2 | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-41-C [Recombination of Data Packets] | [1] 3.4, 7.2.2 | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-42-C [Recombination of Data Packets] | [1] 3.4, 7.2.2 | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.14: Recombination of Data Packets test cases

- Test Procedure

(Optional, for LE Credit-based) If the channel has been created with zero credits, the Upper Tester issues a command to the IUT to send credits to the Lower Tester.

The Lower Tester sends Credit-based frames (K-frame) on the established CID, with PDU Length equal to 10 bytes, fragmented into two fragments.

The IUT recombines the fragments and sends the received data to the Upper Tester.

Figure 4.33: Recombination of Data Packets MSC

- Expected Outcome

## Pass verdict

The IUT receives the fragments and recombines them into correctly formatted K-frames and sends the data to the Upper Tester. The data sent to the Upper Tester matches the data sent by the Lower Tester.

## L2CAP/ECFC/BI-09-C [Incorrect Size Signaling Packets, BR/EDR]

- Test Purpose

Verify that the IUT properly handles L2CAP signaling PDUs that have invalid length over BR/EDR.

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -No security is used in this test case.
- -An SPSM for the desired Credit Based Flow Control based channel is declared via the TSPX\_spsm IXIT value.
- -An ACL connection is established between the Lower Tester and the IUT.

- Test Procedure
1. The Lower Tester sends a C-frame to the IUT with PDU Length smaller than the signaling packet's actual size, Channel ID set to the correct signaling channel for the logical link, and the Information payload containing a correct L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ packet. The L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ packet contains only one SCID.
2. Perform either alternative 2A, 2B, or 2C depending on the IUT's response.

Figure 4.34: L2CAP/ECFC/BI-09-C [Incorrect Size Signaling Packets] MSC

Alternative 2A (IUT disconnects the connection):

- 2A.1 The IUT disconnects the ACL connection.
- 2A.2 The IUT and the Lower Tester create an ACL connection.
- Alternative 2B (IUT ignores the C-frame):
- 2B.1 The IUT discards the frame.

Alternative 2C (IUT rejects the C-frame):

- 2C.1 The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP to the Lower Tester with a valid Reason code.
3. The Lower Tester sends a C-frame to the IUT with PDU Length = 18, Channel ID set to the correct signaling channel for the logical link, and the Information payload containing a correct L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ packet (of length 14 bytes), padded with '0's. The L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ packet contains only one SCID.

4. The IUT sends a correctly formatted L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP to the Lower Tester and an L2CAP\_COMMAND\_REJECT\_RSP rejecting the partial packet, with Reason = 0x0000 ( ' Command not understood ' ).
5. The Lower Tester sends a correctly formatted C-frame to the IUT with valid PDU Length and Channel ID set to the correct signaling channel for the logical link.
- Expected Outcome

## Pass verdict

The IUT sends an L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP only in response to the second C-frame.

In Step 5, the IUT correctly handles the received C-frame.

## 4.4.7 Enhanced Credit Based Flow Control Mode

Verify the correct implementation of the data channel in Enhanced Credit Based Flow Control mode.

## 4.4.7.1 Segmentation

- Test Purpose

Verify that the IUT can send data segments that are larger than the K-frame payload size.

- Reference

[13] 3.4

- Initial Condition
- -The signaling channel specified in Table 4.15 is used.
- -An SPSM for the desired Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -A Data Channel as specified in Table 4.15 is established on the SPSM declared via the TSPX\_spsm IXIT value with credits returned to the IUT by the Lower Tester.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The Upper Tester can command the IUT to send data.
- Test Case Configuration
- Test Procedure

Table 4.15: Segmentation test cases

| Test Case ID | Signaling Channel |
| L2CAP/COS/ECFC/BV-01-C [Segmentation, LE] | 0x0005 |
| L2CAP/COS/ECFC/BV-05-C [Segmentation, BR/EDR] | 0x0001 |

Same as for L2CAP/COS/CFC/BV-01-C [Segmentation].

- Expected Outcome

## Pass verdict

The IUT sends at least one K-frame containing data to the Lower Tester.

If the Upper Test sends a data packet to the IUT larger than the Lower Tester's MPS and smaller than the Lower Tester's MTU, the IUT segments the K-frames correctly.

## 4.4.7.2 Reassembling

- Test Purpose

Verify that the IUT can correctly reassemble data received from the Lower Tester where the L2CAP SDU Length is greater than the IUT K-frame payload size.

- Reference

[13] 3.4

- Initial Condition
- -The signaling channel specified in Table 4.16 is used.
- -An SPSM for the desired Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -A Data Channel as specified in Table 4.16 is established on the SPSM declared via the TSPX\_spsm IXIT value with credits returned to the IUT by the Lower Tester.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- Test Case Configuration
- Test Procedure

Table 4.16: Reassembling test cases

| Test Case ID | Signaling Channel |
| L2CAP/COS/ECFC/BV-02-C [Reassembling, LE] | 0x0005 |
| L2CAP/COS/ECFC/BV-06-C [Reassembling, BR/EDR] | 0x0001 |

Same as for L2CAP/COS/CFC/BV-03-C [Reassembling].

- Expected Outcome

## Pass verdict

The IUT correctly reassembles the data received from the Lower Tester and sends it to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## 4.4.7.3 Multiple Channels with Interleaved Data Streams

- Test Purpose

Verify that an IUT can create multiple channels and receives data streams on the channels when the streams are interleaved.

- Reference

[13] 4.25

- Initial Condition
- -The signaling channel specified in Table 4.17 is used.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

- -An SPSM for the desired Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value, send data and credits.
- Test Case Configuration
- Test Procedure
1. The Upper Tester commands the IUT to send a connection request on the SPSM, with two channels.
2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) to the Lower Tester, with two valid CIDs, on the SPSM.
3. The Lower Tester responds with an L2CAP Credit Based Connection Response (Code = 0x18), establishing all channels.
4. The Lower Tester sends K-Frames to the IUT, alternatively on the two established channels.

Table 4.17: Multiple Channels with Interleaved Data Streams test cases

| Test Case ID | Signaling Channel |
| L2CAP/COS/ECFC/BV-03-C [Multiple Channels with Interleaved Data Streams, LE] | 0x0005 |
| L2CAP/COS/ECFC/BV-07-C [Multiple Channels with Interleaved Data Streams, BR/EDR] | 0x0001 |

Figure 4.35: Multiple Channels with Interleaved Data Streams MSC

- Expected Outcome

## Pass verdict

The IUT sends the received data to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## 4.4.7.4 Reassembling

- Test Purpose

Verify that the IUT can correctly report data received from the Lower Tester when MTU = MPS in the direction from the Lower Tester to the IUT and the data received length = MTU.

- Reference

[13] 3.4

- Initial Condition
- -The signaling channel specified in Table 4.18 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -A Data Channel as specified in Table 4.18 is established on SPSM declared via the TSPX\_spsm IXIT value with credits returned to the IUT by the Lower Tester.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- Test Case Configuration
- Test Procedure

Table 4.18: Reassembling test cases

| Test Case ID | Signaling Channel |
| L2CAP/COS/ECFC/BV-04-C [Reassembling, LE] | 0x0005 |
| L2CAP/COS/ECFC/BV-08-C [Reassembling, BR/EDR] | 0x0001 |

Same as for L2CAP/COS/CFC/BV-04-C [Data Receiving]. The Credit Based Connection Request includes the MTU and MPS parameters set to the same value that is between the minimum and the IUT's MTU read by the Lower Tester . The length of the data sent by the Lower Tester is the same size as the MTU/MPS parameters in the Credit Based Connection Request.

- Expected Outcome

## Pass verdict

The IUT correctly reports the data received from the Lower Tester to the Upper Tester.

The data sent to the Upper Tester matches the data sent by the Lower Tester.

## 4.5 Connection-Oriented Retransmission/Flow Control/Streaming modes

Verify the correct implementation of the features of the Retransmission, Flow Control, and Streaming modes of the connection-oriented L2CAP service.

## 4.5.1 Flow Control

Verify the correct implementation of the Flow Control feature.

## L2CAP/COS/FLC/BV-01-C [Flow Control without Acks]

- Test Purpose

Verify that the IUT does not transmit packets with sequence numbers higher than flow control window when no acknowledgment is received.

- Reference

[1] 5.4, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.
- Test Procedure
- Expected Outcome

Figure 4.36: L2CAP/COS/FLC/BV-01-C [Flow Control without Acks] MSC

## Pass verdict

The IUT does not send any I-frames when the TxWindow is full until the RetransmissionTimer, which has been started with the sending of the first I-frame (N(S)=0), expires.

## L2CAP/COS/FLC/BV-02-C [Resume Flow on RR Frame Ack]

- Test Purpose

Verify that the IUT resumes transmission on reception of acknowledgment in an RR frame.

- Reference

[1] 5.4, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.
- Test Procedure
- Expected Outcome

Figure 4.37: L2CAP/COS/FLC/BV-02-C [Resume Flow on RR Frame Ack] MSC

## Pass verdict

The IUT does not send any I-frames when the TxWindow is full and the IUT RetransmissionTimer, which has been started with the sending of the first I-frame (N(S)=0), has not expired yet.

The IUT resumes transmission when it receives acknowledgment for the first I-frame in a RR frame before IUT Retransmission time-out.

## L2CAP/COS/FLC/BV-03-C [Resume Flow on I-frame Ack]

- Test Purpose

Verify that the IUT resumes transmission on the reception of acknowledgment in an I-frame.

- Reference

[1] 5.4, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.
- Test Procedure
- Expected Outcome

Figure 4.38: L2CAP/COS/FLC/BV-03-C [Resume Flow on I-frame Ack] MSC

## Pass verdict

The IUT does not send any I-frames when the TxWindow is full and the RetransmissionTimer, which has been started with the sending of the first I-frame (N(S)=0), has not expired yet.

The IUT resumes transmission when it receives an acknowledgment for the first I-frame in an I-frame sent by the Lower Tester before IUT Retransmission time-out.

## L2CAP/COS/FLC/BV-04-C [Transmit RR Frame on Monitor Timeout]

- Test Purpose

Verify that the IUT transmits an RR frame after Monitor time-out.

- Reference

## 1 5.4, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Flow Control only mode.
- Test Procedure
- Expected Outcome

Figure 4.39: L2CAP/COS/FLC/BV-04-C [Transmit RR Frame on Monitor Timeout] MSC

## Pass verdict

The Lower Tester receives the IUT ' s RR frame within the timing window, [Monitor Time-out (+/- 10%)], after transmission of its own RR frame.

- Notes

The 10 percent timing window is to account for timing differences between IUT and Lower Tester, as well as minor measurement error.

## 4.5.2 Retransmission

Verify the correct implementation of the retransmission feature.

## L2CAP/COS/RTX/BV-01-C [No Retransmission with R=1]

- Test Purpose

Verify that the IUT does not retransmit packets when the retransmission flag is set to R=1.

- Reference

[1] 5.3, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Retransmission mode.
- Test Procedure
- Expected Outcome

Figure 4.40: L2CAP/COS/RTX/BV-01-C [No Retransmission with R=1] MSC

## Pass verdict

The IUT does not retransmit an I-frame with sequence number N(S)=0 after IUT Retransmission timeout when the latest received R bit in a RR frame is 1.

## L2CAP/COS/RTX/BV-02-C [Retransmission with R=0 in RR frame]

- Test Purpose

Verify that the IUT retransmits packets after retransmission time-out when the retransmission flag is set to R=0 received in a RR frame.

- Reference

[1] 5.3, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Retransmission mode.

- Test Procedure
- Expected Outcome

Figure 4.41: L2CAP/COS/RTX/BV-02-C [Retransmission with R=0 in RR frame] MSC

## Pass verdict

The IUT retransmits an I-frame with sequence number N(S)=0 after IUT Retransmission time-out when the latest received R bit in a RR frame is 0.

## L2CAP/COS/RTX/BV-03-C [Retransmission with R=0 in I-frame]

- Test Purpose

Verify that the IUT retransmits packets after retransmission time-out when retransmission flag is set to R=0 received in an I-frame.

- Reference

[1] 5.3, 7.4

- Initial Condition
- -The IUT is in OPEN state for data channel with assigned CID. L2CAP connection configured as Retransmission mode.

Figure 4.42: L2CAP/COS/RTX/BV-03-C [Retransmission with R=0 in I-frame] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits I-frame with sequence number N(S)=0 after IUT Retransmission time-out when latest received R bit in a I-frame is 0.

## 4.5.3 Extended Features (EXF)

Verify the correct implementation of the extended features information requests and responses of the L2CAP layer.

## L2CAP/EXF/BV-07-C [Extended Features Information Response]

- Test Purpose

Verify that the IUT can format an Information Response for the information type of Extended Features.

- Reference

[1] 4.10, 4.11, 4.12

- Initial Condition
- -An ACL connection has been established by the Lower Tester.

- Test Procedure
- Expected Outcome

Figure 4.43: L2CAP/EXF/BV-07-C [Extended Features Information Response] MSC

## Pass verdict

The IUT sends Information Response [InfoType = Extended Features] and with a result code of Success and containing extended features supported defined by the ICS as mapped by Table 3.1 in [5].

## L2CAP/EXF/BV-08-C [Information Request, Extended Features]

- Test Purpose

Verify that the IUT returns the proper L2CAP Extended Features in response to the Information Request from the Lower Tester.

- Reference

[11] 4.10

- Initial Condition
- -The IUT is in the CLOSED state.
- -No ACL link exists.
- -The IUT acts as an L2CAP acceptor.
- Test Procedure

The Lower Tester sends an information request to the IUT.

Figure 4.44: L2CAP/EXF/BV-08-C [Information Request, Extended Features] MSC

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP\_INFORMATION\_RSP PDU to the Lower Tester with the Info parameter containing 4 octets that match the ICS entries as shown in Table 4.19 and all bits not listed are set to 0b0.

Table 4.19: Extended Feature Mask bits

| Feature | Octet | Bit | ICS |
| Flow Control mode | 0 | 0 | L2CAP 2/11 |
| Retransmission mode | 0 | 1 | L2CAP 2/10 |
| Bi-directional QoS | 0 | 2 | L2CAP 3/7 |
| Enhanced Retransmission mode | 0 | 3 | L2CAP 2/12 |
| Streaming mode | 0 | 4 | L2CAP 2/13 |
| FCS Option | 0 | 5 | L2CAP 2/14 |
| Extended Flow Specification for BR/EDR | 0 | 6 | L2CAP 2/38 |
| Fixed Channels supported over BR/EDR | 0 | 7 | L2CAP 2/30 |
| Extended Window Size | 1 | 0 | L2CAP 2/39 |
| Unicast Connectionless Data Reception | 1 | 1 | L2CAP 2/35 |
| Enhanced Credit Based Flow Control mode over BR/EDR | 1 | 2 | L2CAP 2/48a |

- Notes

The Lower Tester's RTX timer is set to maximum allowed initial value.

## 4.5.4 Channel Mode Configuration (CMC)

Verify the configuration of L2CAP channels using the various L2CAP supported modes.

## L2CAP/CMC/BV-01-C [IUT Initiated Configuration of Enhanced Retransmission Mode]

- Test Purpose

Verify that the IUT can send a Configuration Request command containing the F&amp;EC option that specifies Enhanced Retransmission Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has been established by the Lower Tester.

## · Test Procedure

Figure 4.45: L2CAP/CMC/BV-01-C [IUT Initiated Configuration of Enhanced Retransmission Mode] MSC

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP Configure Request for Enhanced Retransmission Mode before the Lower Tester configuration timer (120 seconds) expires.

## L2CAP/CMC/BV-02-C [Lower Tester Initiated Configuration of Enhanced Retransmission Mode]

- Test Purpose

Verify that the IUT can accept a Configuration Request from the Lower Tester containing an F&amp;EC option that specifies Enhanced Retransmission Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -Test L2CAP/CMC/BV-01-C [IUT Initiated Configuration of Enhanced Retransmission Mode] has been performed successfully.

- Test Procedure
- Expected Outcome

Figure 4.46: L2CAP/CMC/BV-02-C [Lower Tester Initiated Configuration of Enhanced Retransmission Mode] MSC

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_RSP before the Lower Tester TSPX\_timer\_rtx timer expires with a result code of 'Success.'

## L2CAP/CMC/BV-03-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Optional]

- Test Purpose

When configuring a PSM that can optionally support ERTM, verify that the IUT can handle receipt (renegotiate the channel mode in accordance with the specification) of a Configure Response indicating the peer L2CAP entity doesn't wish to use Enhanced Retransmission Mode (Configure Response Result = Reject Unacceptable Parameters).

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.

- Test Procedure
- Expected Outcome

Figure 4.47: L2CAP/CMC/BV-03-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Optional] MSC

## Pass verdict

The channel is successfully configured to Basic Mode.

## L2CAP/CMC/BV-04-C [IUT Initiated Configuration of Streaming Mode]

- Test Purpose

Verify that the IUT can send a Configuration Request command containing the F&amp;EC option that specifies Streaming Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports the Streaming Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has been established by the Lower Tester.

- Test Procedure
- Expected Outcome

Figure 4.48: L2CAP/CMC/BV-04-C [IUT Initiated Configuration of Streaming Mode] MSC

## Pass verdict

The IUT sends a correctly formatted L2CAP Configure Request for Streaming Mode before the Lower Tester Configuration Timer (120 seconds) expires.

## L2CAP/CMC/BV-05-C [Lower Tester Initiated Configuration of Streaming Mode]

- Test Purpose

Verify that the IUT can accept a Configuration Request from the Lower Tester containing an F&amp;EC option that specifies Streaming Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -Test L2CAP/CMC/BV-04-C [IUT Initiated Configuration of Streaming Mode] has been performed successfully.

## · Test Procedure

Figure 4.49: L2CAP/CMC/BV-05-C [Lower Tester Initiated Configuration of Streaming Mode] MSC

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_RSP before the Lower Tester RTX timer expires with a result code of 'Success.'

## L2CAP/CMC/BV-06-C [Failed Configuration of Streaming Mode when use of the Mode is Optional]

- Test Purpose

When configuring a PSM that can optionally support Streaming Mode, verify that the IUT can handle receipt (renegotiate the channel mode in accordance with the specification) of a Configure Response indicating the peer L2CAP entity does not wish to use the tested mode (Configure Response Result = Reject Unacceptable Parameters).

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.

## · Test Procedure

Figure 4.50: L2CAP/CMC/BV-06-C [Failed Configuration of Streaming Mode when use of the Mode is Optional] MSC

- Expected Outcome

## Pass verdict

The channel is successfully configured to Basic Mode.

## L2CAP/CMC/BV-07-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Optional]

- Test Purpose

When configuring a PSM that can optionally support the use of ERTM, verify that the IUT renegotiates the channel mode to Basic Mode if the Lower Tester attempts to configure Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.51: L2CAP/CMC/BV-07-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Optional] MSC

## Pass verdict

The channel is successfully configured to Basic Mode.

## L2CAP/CMC/BV-08-C [Configuration Mode Mismatch when use of Streaming Mode is Optional]

- Test Purpose

When configuring a PSM that can optionally support the use of Streaming Mode, verify that the IUT renegotiates the channel mode to Basic Mode if the Lower Tester attempts to configure Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.52: L2CAP/CMC/BV-08-C [Configuration Mode Mismatch when use of Streaming Mode is Optional] MSC

## Pass verdict

The channel is successfully configured to Basic Mode.

## L2CAP/CMC/BV-09-C [Configuration to Basic Mode by the IUT]

- Test Purpose

The IUT wishes to use Basic Mode when configuring a PSM that can optionally support the use of ERTM or Streaming Mode. Verify that the IUT correctly rejects the request for ERTM or Streaming Mode from the Lower Tester.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The Lower Tester has determined which Enhanced L2CAP Mode the IUT supports (using the Information Request/Response [Extended Features] mechanism). If the IUT supports both, the Lower Tester attempts to configure ERTM.
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.53: L2CAP/CMC/BV-09-C [Configuration to Basic Mode by the IUT] MSC

## Pass verdict

The IUT sends a Configure Response with result code of Unacceptable Parameters to the request from the Lower Tester for ERTM or STM.

The channel is successfully configured for Basic Mode.

## L2CAP/CMC/BI-01-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Mandatory]

- Test Purpose

When creating a connection for a PSM that mandates the use of ERTM, verify that the IUT can handle receipt (close the channel in accordance with the specification) of a Configure Response indicating the peer L2CAP entity does not wish to use Enhanced Retransmission Mode (Configure Response Result = Reject Unacceptable Parameters).

- Reference

<!-- formula-not-decoded -->

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.54: L2CAP/CMC/BI-01-C [Failed Configuration of Enhanced Retransmission Mode when use of the Mode is Mandatory] MSC

## Pass verdict

The IUT initiates closure of the channel.

## L2CAP/CMC/BI-02-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Mandatory]

- Test Purpose

When creating a connection for a PSM that mandates the use of ERTM, verify that the IUT closes the channel if the Lower Tester attempts to configure Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Enhanced Retransmission Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.55: L2CAP/CMC/BI-02-C [Configuration Mode mismatch when use of Enhanced Retransmission Mode is Mandatory] MSC

## Pass verdict

The IUT initiates closure of the channel.

## L2CAP/CMC/BI-03-C [Failed Configuration of Streaming Mode when use of the Mode is Mandatory]

- Test Purpose

When creating a connection for a PSM that mandates the use of Streaming Mode, verify that the IUT can handle receipt (close the channel in accordance with the specification) of a Configure Response indicating the peer L2CAP entity does not wish to use Streaming Mode (Configure Response Result = Reject Unacceptable Parameters).

## · Reference

## 1 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.56: L2CAP/CMC/BI-03-C [Failed Configuration of Streaming Mode when use of the Mode is Mandatory] MSC

## Pass verdict

The IUT initiates closure of the channel.

## L2CAP/CMC/BI-04-C [Configuration Mode mismatch when use of Streaming Mode is Mandatory]

- Test Purpose

When creating a connection for a PSM that mandates the use of Streaming Mode, verify that the IUT closes the channel if the Lower Tester attempts to configure Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.57: L2CAP/CMC/BI-04-C [Configuration Mode mismatch when use of Streaming Mode is Mandatory] MSC

## Pass verdict

The IUT initiates closure of the channel.

## L2CAP/CMC/BI-05-C [Failed Configuration to Basic Mode by the IUT]

- Test Purpose

The IUT wishes to use Basic Mode when configuring a PSM that can optionally support the use of ERTM or Streaming Mode. Verify that the IUT initiates channel closure if the Lower Tester refuses to negotiate the channel to Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The Lower Tester has determined which Enhanced L2CAP Mode the IUT supports (using the Information Request/Response [Extended Features] mechanism). If the IUT supports both, the Lower Tester attempts to configure ERTM.
- -The channel connection has completed.

## · Test Procedure

Figure 4.58: L2CAP/CMC/BI-05-C [Failed Configuration to Basic Mode by the IUT] MSC

- Expected Outcome

## Pass verdict

The IUT sends a Configure Response with result code of Unacceptable Parameters to the request from the Lower Tester for ERTM.

The IUT initiates closure of the channel when it receives the second Configure Request for ERTM from the Lower Tester.

## L2CAP/CMC/BI-06-C [Configuration to Basic Mode Rejected by the Lower Tester]

- Test Purpose

The IUT wishes to use Basic Mode when configuring a PSM that can optionally support the use of ERTM or Streaming Mode. Verify that the IUT initiates channel closure if the Lower Tester rejects the IUT configure request for Basic Mode.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The Lower Tester has determined which Enhanced L2CAP Mode the IUT supports (using the Information Request/Response [Extended Features] mechanism). If the IUT supports both, the Lower Tester attempts to configure ERTM.
- -The channel connection has completed.
- Test Procedure
- Expected Outcome

Figure 4.59: L2CAP/CMC/BI-06-C [Configuration to Basic Mode Rejected by the Lower Tester] MSC

## Pass verdict

The IUT initiates closure of the channel when it receives the Configure Response rejecting Basic Mode from the Lower Tester.

## L2CAP/CMC/BV-10-C [ERTM Not Supported by Lower Tester for Optional ERTM Channel]

- Test Purpose

The IUT is initiating connection of an L2CAP channel that can optionally support use of ERTM. Verify that the IUT attempts to configure Basic Mode if the Lower Tester does not indicate support for ERTM in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 4.10, 4.11, 4.12, 5.4, 6.1.4, 7.1

- Initial Condition
- -An ACL connection has been established by the Lower Tester.

## · Test Procedure

Figure 4.60: L2CAP/CMC/BV-10-C [ERTM Not Supported by Lower Tester for Optional ERTM Channel] MSC

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT opens the L2CAP channel to the Lower Tester.

The IUT attempts to configure the channel to Basic Mode.

## L2CAP/CMC/BV-11-C [Streaming Mode not supported by Lower Tester for Optional Streaming Mode Channel]

- Test Purpose

The IUT is initiating connection of an L2CAP channel that can optionally support use of STM. Verify that the IUT attempts to configure Basic Mode if the Lower Tester does not indicate support for STM in the Information Response [Extended Features].

- Reference

<!-- formula-not-decoded -->

- Initial Condition
- -An ACL connection has been established by the Lower Tester

## · Test Procedure

Figure 4.61: L2CAP/CMC/BV-11-C [Streaming Mode not supported by Lower Tester for Optional Streaming Mode Channel] MSC

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT opens the L2CAP channel to the Lower Tester.

The IUT attempts to configure the channel to Basic Mode.

## L2CAP/CMC/BV-12-C [ERTM Not Supported by Lower Tester for Mandatory ERTM channel]

- Test Purpose

The IUT is initiating connection of an L2CAP channel that mandates use of ERTM. Verify that the IUT does not attempt to configure the connection to ERTM if the Lower Tester has not indicated support for ERTM in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 4.10, 4.11, 4.12, 5.4, 6.1.4, 7.1

- Initial Condition
- -An ACL connection has been established by the Lower Tester.

- Test Procedure
- Expected Outcome

Figure 4.62: L2CAP/CMC/BV-12-C [ERTM Not Supported by Lower Tester for Mandatory ERTM channel] MSC

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT does not attempt to configure the connection to the unsupported mode of the Lower Tester and informs the Upper Tester that the connection has failed.

## L2CAP/CMC/BV-13-C [Streaming Mode not supported by Lower Tester for Mandatory Streaming Mode Channel]

- Test Purpose

The IUT is initiating connection of an L2CAP channel that mandates use of STM. Verify that the IUT does not attempt to configure the connection to STM if the Lower Tester has not indicated support for STM in the Information Response [Extended Features].

- Reference

[1] 4.4, 4.5, 4.10, 4.11, 4.12, 5.4, 6.1.4, 7.1

- Initial Condition
- -An ACL connection has been established by the Lower Tester.

- Test Procedure
- Expected Outcome

Figure 4.63: L2CAP/CMC/BV-13-C [Streaming Mode not supported by Lower Tester for Mandatory Streaming Mode Channel] MSC

## Pass verdict

The IUT sends an L2CAP Information Request for the Extended Features of the Lower Tester.

The IUT does not attempt to configure the connection to the unsupported mode of the Lower Tester and informs the Upper Tester that the connection has failed.

## L2CAP/CMC/BV-14-C [Failed Configuration of Streaming Mode when use of the mode is optional and ERTM is proposed by the Lower Tester]

- Test Purpose

When configuring a PSM that can optionally support Streaming Mode, verify that the IUT can handle receipt (renegotiate the channel mode in accordance with the specification) of a Configure Response indicating the peer L2CAP entity wishes to use ERTM (Configure Response Result = Reject Unacceptable Parameters).

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.

- Test Procedure
- Expected Outcome

Figure 4.64: L2CAP/CMC/BV-14-C [Failed Configuration of Streaming Mode when use of the mode is optional and ERTM is proposed by the Lower Tester] MSC

## Pass verdict

The channel is successfully configured to Enhanced Retransmission Mode.

## L2CAP/CMC/BV-15-C [Configuration Mode Mismatch when use of Streaming Mode is Optional and ERTM is proposed by the Lower Tester]

- Test Purpose

When configuring a PSM that can optionally support the use of Streaming Mode, verify that the IUT renegotiates the channel mode to ERTM if the Lower Tester attempts to configure ERTM.

- Reference

[1] 4.4, 4.5, 5.4, 6.1.4, 7.1

## · Initial Condition

- -The IUT has established that the peer L2CAP entity supports Streaming Mode (using the Information Request/Response [Extended Features] mechanism).
- -The channel connection has completed.
- Test Procedure

Figure 4.65: L2CAP/CMC/BV-15-C [Configuration Mode Mismatch when use of Streaming Mode is Optional and ERTM is proposed by the Lower Tester] MSC

## · Expected Outcome

## Pass verdict

The channel is successfully configured to Enhanced Retransmission Mode.

## 4.5.5 Frame Check Sequence (FCS) Option Configuration (FOC)

Verify the configuration of the FCS option of the L2CAP layer.

## 4.5.5.1 IUT Initiated Configuration of the FCS Option, IUT No FCS

- Test Purpose

Verify that an IUT that does not support FCS sends S-frame or I-frame PDUs with or without FCS depending on the Lower Tester FCS support.

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition
- -The initiator IUT has established that the peer L2CAP entity supports configuration of the Optional FCS option (using the Information Request/Response [Extended Features] mechanism).
- Test Case Configuration

| Test Case | FCS Type (Lower Tester) | IUT S/I-Frame FCS |
| L2CAP/FOC/BV-01-C [IUT Initiated Configuration of the FCS Option, IUT No FCS Option, Lower Tester No FCS Option] | 0x00: No FCS | No |
| L2CAP/FOC/BV-02-C [IUT Initiated Configuration of the FCS Option, IUT No FCS Option, Lower Tester Yes FCS Option] | 0x01: 16-bit FCS | Yes |
| L2CAP/FOC/BV-03-C [IUT Initiated Configuration of the FCS Option, IUT No FCS Option, Lower Tester Omitted FCS Option] | Omitted | Yes |

Table 4.20: IUT Initiated Configuration of the FCS Option, IUT No FCS test cases

## · Test Procedure

Figure 4.66: IUT Initiated Configuration of the FCS Option, IUT No FCS MSC

- Expected Outcome

## Pass verdict

The channel is established.

The IUT sends an S-frame (in response to the S-frame [POLL] from the sender) or an I-frame with or without the FCS field as specified in Table 4.20.

## 4.5.5.2 IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted

- Test Purpose

Verify that the IUT sends I/S-frames with the FCS field present when the IUT either supports or omits the FCS type and the Lower Tester supports, does not support, or omits the FCS Type.

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition
- -The initiator IUT has established that the peer L2CAP entity supports configuration of the Optional FCS option (using the Information Request/Response [Extended Features] mechanism).
- Test Case Configuration

| Test Case | FCS Type (IUT) |
| L2CAP/FOC/BV-04-C [IUT Initiated Configuration of the FCS Option, IUT FCS 0x01] | 0x01: 16-bit FCS |
| L2CAP/FOC/BV-06-C [IUT Initiated Configuration of the FCS Option, IUT FCS Omitted] | Omitted |

Table 4.21: IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted test cases

## · Test Procedure

Figure 4.67: IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted MSC

| Rounds | FCS Type (Lower Tester) |
| 1 | 0x00: No FCS |
| 2 | 0x01: 16-bit FCS |
| 3 | Omitted |

Table 4.22: IUT Initiated Configuration of the FCS Option, IUT FCS or Omitted rounds

- Expected Outcome

## Pass verdict

The channel is established.

The IUT sends an S-frame (in response to the S-frame [POLL] from the sender) or an I-frame with the FCS field present.

## 4.5.5.3 IUT Responder, Configuration of the FCS Option

- Test Purpose

Verify that the IUT can respond to a channel configuration. The IUT is configured to support, not support, or omit the FCS type as specified in Table 4.24 in I/S-frames and will send I/S-frames with the FCS field as specified in Table 4.24.

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition
- -The responder IUT has established that the peer L2CAP entity supports configuration of the Optional FCS option (using the Information Request/Response [Extended Features] mechanism).
- Test Case Configuration

| Test Case | FCS Type (IUT) | IUT S/I-Frame FCS | IUT S/I-Frame FCS |
| | | Round 1 | Rounds 2 & 3 |
| L2CAP/FOC/BV-05-C [IUT Responder, Configuration of the FCS Option, IUT FCS 0x00] | 0x00: No FCS | No | Yes |
| L2CAP/FOC/BV-07-C [IUT Responder, Configuration of the FCS Option, IUT FCS 0x01] | 0x01: 16-bit FCS | Yes | Yes |
| L2CAP/FOC/BV-08-C [IUT Responder, Configuration of the FCS Option, IUT FCS Omitted] | Omitted | Yes | Yes |

Table 4.23: IUT Responder, Configuration of the FCS Option test cases

## · Test Procedure

Figure 4.68: IUT Responder, Configuration of the FCS Option MSC

| Rounds | FCS Type (Lower Tester) |
| 1 | 0x00: No FCS |
| 2 | 0x01: 16-bit FCS |
| 3 | Omitted |

Table 4.24: IUT Responder, Configuration of the FCS Option rounds

- Expected Outcome

## Pass verdict

The channel is established.

The IUT sends an S-frame (in response to the S-frame [POLL] from the sender) or an I-frame with the FCS field as specified in Table 4.24.

## 4.5.6 Optional FCS (OFS)

Verify the correct implementation of the Optional FCS feature.

## L2CAP/OFS/BV-01-C [Sending I-Frames without FCS for ERTM]

- Test Purpose

Verify that the IUT does not include the FCS in I-frames.

- Reference

[1] 3.3.5, 8.6

- Initial Condition
- -The channel is configured to not include FCS in I/S-frames.
- -The channel is configured to use ERTM.
- Test Procedure
- Expected Outcome

Figure 4.69: L2CAP/OFS/BV-01-C [Sending I-Frames without FCS for ERTM] MSC

## Pass verdict

The IUT sends an I-frame without the FCS field.

## L2CAP/OFS/BV-02-C [Receiving Frames without FCS for ERTM]

- Test Purpose

Verify that the IUT can handle I-frames that do not contain the FCS.

- Reference

[1] 3.3.5, 8.6

- Initial Condition
- -The channel is configured to not include FCS in I/S-frames.
- -The channel is configured to use ERTM.
- Test Procedure
- Expected Outcome

Figure 4.70: L2CAP/OFS/BV-02-C [Receiving Frames without FCS for ERTM] MSC

## Pass verdict

The IUT passes the received data to the Upper Tester.

The IUT acknowledges the received I-frame before the Retransmission timer of the Lower Tester expires.

## L2CAP/OFS/BV-03-C [Sending I-Frames without FCS for Streaming Mode]

- Test Purpose

Verify that the IUT does not include the FCS in I-frames.

- Reference

[1] 3.3.5, 8.7

- Initial Condition
- -The channel is configured to not include FCS in I/S-frames.
- -The channel is configured to use Streaming Mode.
- Test Procedure

Figure 4.71: L2CAP/OFS/BV-03-C [Sending I-Frames without FCS for Streaming Mode] MSC

- Expected Outcome

## Pass verdict

The IUT sends an I-frame without the FCS field.

## L2CAP/OFS/BV-04-C [Receiving Frames without FCS for Streaming Mode]

- Test Purpose

Verify that the IUT can handle I-frames that do not contain the FCS.

- Reference

[1] 3.3.5, 8.7

- Initial Condition
- -The channel is configured to not include FCS in I/S-frames.
- -The channel is configured to use Streaming Mode.
- Test Procedure
- Expected Outcome

Figure 4.72: L2CAP/OFS/BV-04-C [Receiving Frames without FCS for Streaming Mode] MSC

## Pass verdict

The IUT passes the received data to the Upper Tester.

## L2CAP/OFS/BV-05-C [Sending I-Frames with FCS for ERTM]

- Test Purpose

Verify that the IUT does include the FCS in I-frames.

- Reference

[1] 3.3.5, 8.6

- Initial Condition
- -The channel is configured to include FCS in I/S-frames.
- -The channel is configured to use ERTM.

- Test Procedure
- Expected Outcome

Figure 4.73: L2CAP/OFS/BV-05-C [Sending I-Frames with FCS for ERTM] MSC

## Pass verdict

The IUT sends an I-frame with the correct FCS included.

## L2CAP/OFS/BV-06-C [Receiving Frames with FCS for ERTM]

- Test Purpose

Verify that the IUT can handle I-frames that do contain the FCS.

- Reference

[1] 3.3.5, 8.6

- Initial Condition
- -The channel is configured to include FCS in I/S-frames.
- -The channel is configured to use ERTM.
- Test Procedure

Figure 4.74: L2CAP/OFS/BV-06-C [Receiving Frames with FCS for ERTM] MSC

- Expected Outcome

## Pass verdict

The IUT passes the received data to the Upper Tester.

The IUT acknowledges the received I-frame before the Retransmission timer of the Lower Tester expires.

## L2CAP/OFS/BV-07-C [Sending I-Frames with FCS for Streaming Mode]

- Test Purpose

Verify that the IUT does include the FCS in I-frames.

- Reference

[1] 3.3.5, 8.7

- Initial Condition
- -The channel is configured to include FCS in I/S-frames.
- -The channel is configured to use Streaming Mode.
- Test Procedure
- Expected Outcome

Figure 4.75: L2CAP/OFS/BV-07-C [Sending I-Frames with FCS for Streaming Mode] MSC

## Pass verdict

The IUT sends an I-frame with the FCS field.

## L2CAP/OFS/BV-08-C [Receiving Frames with FCS for Streaming Mode]

- Test Purpose

Verify that the IUT can handle I-frames that do contain the FCS.

- Reference

[1] 3.3.5, 8.7

- Initial Condition
- -The channel is configured to include FCS in I/S-frames.
- -The channel is configured to use Streaming Mode.

- Test Procedure
- Expected Outcome

Figure 4.76: L2CAP/OFS/BV-08-C [Receiving Frames with FCS for Streaming Mode] MSC

## Pass verdict

The IUT passes the received data to the Upper Tester.

## 4.5.7 Enhanced Retransmission Mode (ERM)

Verify the correct implementation of the Enhanced Retransmission Mode of L2CAP.

## L2CAP/ERM/BV-01-C [Transmit I-frames]

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the enhanced control fields (SAR, F-bit, ReqSeq, TxSeq).

- Reference

[1] 3.3.2, 8.6

- Initial Condition
- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID.
- -The connection is configured as ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.77 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.77: L2CAP/ERM/BV-01-C [Transmit I-frames] MSC

- Expected Outcome

## Pass verdict

The IUT sends I-frame(s) to the Lower Tester.

Data in the I-frame(s) match that provided by the Upper Tester.

SAR bits are set per the Specification in [8].

F-bit is set to 0.

## L2CAP/ERM/BV-02-C [Receive I-Frames]

- Test Purpose

Verify that the IUT can receive in-sequence valid I-frames and deliver L2CAP SDUs to the Upper Tester.

- Reference

## 1 3.3.2, 8.6

- Initial Condition
- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID.
- -The connection is configured as ERTM.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The IUT has configured an MPS size that is equal to 48 bytes.

## · Test Procedure

Figure 4.78 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.78: L2CAP/ERM/BV-02-C [Receive I-Frames] MSC

- Expected Outcome

## Pass verdict

Data in the received I-frame(s) match that sent by the Lower Tester.

SAR bits are set per specification.

F-bit is set to 0.

Complete SDU is sent to the Upper Tester.

## L2CAP/ERM/BV-03-C [Acknowledging Received I-Frames]

- Test Purpose

Verify that the IUT sends S-frame [RR] with the Poll bit not set to acknowledge data received from the Lower Tester.

- Reference

[1] 3.3.2, 8.6.1.1

- Initial Condition
- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.79 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.79: L2CAP/ERM/BV-03-C [Acknowledging Received I-Frames] MSC

- Expected Outcome

## Pass verdict

The IUT sends a Supervisory Frame with S=RR, LastAckedReqSeq &lt; ReqSeq &lt;= last received Iframe's TxSeq+1, F=0, P=0, Reserved bits = 0.

## L2CAP/ERM/BV-05-C [Resume Transmitting I-Frames when an S-Frame [RR] is Received]

- Test Purpose

Verify that the IUT ceases transmission of I-frames when the negotiated TxWindow is full. Verify that the IUT resumes transmission of I-frames when an S-frame [RR] is received that acknowledges previously sent I-frames.

- Reference

[1] 3.3.2, 8.6.4

## · Initial Condition

- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The Lower Tester specifies a TxWindow size of 1 in the Configuration Request it sends to the IUT.

## · Test Procedure

Figure 4.80 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.80: L2CAP/ERM/BV-05-C [Resume Transmitting I-Frames when an S-Frame [RR] is Received] MSC

- Expected Outcome

## Pass verdict

The IUT sends I-frames until TxWindow is full.

The IUT does not send any I-frame when the TxWindow is full.

The IUT sends the outstanding I-frame when it receives the acknowledgment of the first I-frame from the Lower Tester.

## L2CAP/ERM/BV-06-C [Resume Transmitting I-Frames when an I-Frame is Received]

## · Test Purpose

Verify that the IUT ceases transmission of I-frames when the negotiated TxWindow is full. Verify that the IUT resumes transmission of I-frames when an I-frame is received that acknowledges previously sent I-frames.

- Reference

[1] 3.3.2, 8.6.4

- Initial Condition
- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The Lower Tester specifies a TxWindow size of 1 in the Configuration Request it sends to the IUT.
- Test Procedure

Figure 4.81 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.81: L2CAP/ERM/BV-06-C [Resume Transmitting I-Frames when an I-Frame is Received] MSC

- Expected Outcome

## Pass verdict

The IUT sends I-frames until TxWindow is full.

The IUT does not send any I-frame when the TxWindow is full.

The IUT sends the outstanding I-frame when it receives the acknowledgment of the first I-frame from the Lower Tester.

## L2CAP/ERM/BV-07-C [Send S-Frame [RNR]]

- Test Purpose

Verify that the IUT sends an S-frame [RNR] when it detects a Local Busy condition.

- Reference

## 1 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- -Whether the IUT has the capability to set the Local Busy condition from the Upper Tester is specified in the L2CAP TSPX\_generate\_local\_busy IXIT value.
- Test Procedure

Figure 4.82 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The Lower Tester sends as many I-frames as are permitted by the IUT TxWindow to trigger the Local Busy condition at the IUT. Once the Lower Tester receives the RNR from the IUT it will stop sending I-frames.

Figure 4.82: L2CAP/ERM/BV-07-C [Send S-Frame [RNR]] MSC

- Expected Outcome

## Pass verdict

ALT 1: The IUT immediately sends an S-frame with function RNR after the Local Busy condition is set by the Upper Tester.

ALT 2: The IUT sends an S-frame with function RNR after receiving I-frame(s) from the Lower Tester when the Local Busy condition is reached.

## L2CAP/ERM/BV-08-C [Send S-Frame [RR] with Poll Bit Set]

- Test Purpose

Verify that the IUT sends an S-frame [RR] with the Poll bit set when its retransmission timer expires.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.83 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.83: L2CAP/ERM/BV-08-C [Send S-Frame [RR] with Poll Bit Set] MSC

- Expected Outcome

## Pass verdict

The IUT sends an S-frame with the POLL bit set after the IUT Retransmission Timer (as specified by Lower Tester during configuration) expires.

The IUT does not retransmit the I-frame after receiving an S-frame from the Lower Tester that acknowledges the previously sent I-frame.

## L2CAP/ERM/BV-09-C [Send S-frame [RR] with Final Bit Set]

- Test Purpose

Verify that the IUT responds with an S-frame [RR] with the Final bit set after receiving an S-frame [RR] with the Poll bit set.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.84 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.84: L2CAP/ERM/BV-09-C [Send S-frame [RR] with Final Bit Set] MSC

- Expected Outcome

## Pass verdict

The IUT sends an S-frame with the Final bit set before the Monitor Timer of the Lower Tester expires.

## L2CAP/ERM/BV-10-C [Retransmit S-Frame [RR] with Poll Bit Set]

- Test Purpose

Verify that the IUT will retransmit the S-frame [RR] with the Poll bit set when the Monitor Timer expires.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.

## · Test Procedure

Figure 4.85 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.85: L2CAP/ERM/BV-10-C [Retransmit S-Frame [RR] with Poll Bit Set] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the S-frame with the POLL bit set after the Monitor Timer expires.

The IUT does not retransmit the S-frame with the POLL bit set after receiving the S-frame acknowledgment of the previously sent I-frame.

## L2CAP/ERM/BV-11-C [S-Frame Transmissions Exceed MaxTransmit]

- Test Purpose

Verify that the IUT closes the channel when the Monitor Timer expires.

- Reference

[1] 3.3.2, 5.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to 1.

## · Test Procedure

Figure 4.86 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.86: L2CAP/ERM/BV-11-C [S-Frame Transmissions Exceed MaxTransmit] MSC

- Expected Outcome

## Pass verdict

The IUT initiates closure of the L2CAP channel when the Monitor Timer expires.

## L2CAP/ERM/BV-12-C [I-Frame Transmissions Exceed MaxTransmit]

- Test Purpose

Verify that the IUT closes the channel when it receives an S-frame [RR] with the final bit set that does not acknowledge the previous I-frame sent by the IUT.

- Reference

[1] 3.3.2, 5.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to 1.

## · Test Procedure

Figure 4.87 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.87: L2CAP/ERM/BV-12-C [I-Frame Transmissions Exceed MaxTransmit] MSC

- Expected Outcome

## Pass verdict

The IUT initiates closure of the L2CAP channel when it receives the S-frame from the Lower Tester that does not acknowledge the previously sent I-frame.

## L2CAP/ERM/BV-13-C [Respond to S-Frame [REJ]]

- Test Purpose

Verify that the IUT retransmits I-frames starting from the sequence number specified in the S-frame [REJ].

- Reference

[1] 3.3.2, 8.6.1.2, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin that is greater than 1 in the Configure Request sent to the IUT.

## · Test Procedure

Figure 4.88 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.88: L2CAP/ERM/BV-13-C [Respond to S-Frame [REJ]] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the first I-frame requested in the REJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The IUT retransmits the second I-frame requested in the REJ from the Lower Tester before the IUT Retransmission Timer expires.

## L2CAP/ERM/BV-14-C [Respond to S-Frame [SREJ] POLL Bit Set]

- Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame. Verify that the IUT processes the acknowledgment of previously unacknowledged I-frames.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.

## · Test Procedure

Figure 4.89 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.89: L2CAP/ERM/BV-14-C [Respond to S-Frame [SREJ] POLL Bit Set] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The I-frame retransmitted by the IUT has the Final bit = 1.

The IUT processes the acknowledgment of the first I-frame (N(S) = 0) from the SREJ received and consequently send the pending I-frame (N(S) = 3).

## L2CAP/ERM/BV-15-C [Respond to S-Frame [SREJ] POLL bit clear]

- Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.
- Test Procedure

Figure 4.90 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.90: L2CAP/ERM/BV-15-C [Respond to S-Frame [SREJ] POLL bit clear] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The IUT does not transmit I-frame (N(S) = 3) as a result of receiving the SREJ from the Lower Tester.

## L2CAP/ERM/BV-16-C [Send S-Frame [REJ]]

- Test Purpose

Verify that the IUT can send an S-frame [REJ] after receiving out of sequence I-frames.

- Reference

## 1 3.3.2, 8.6.1.2, 8.6.4

- Initial Condition
- -The TxWindow size of the Lower Tester must be greater than 2 and should be the largest value that can be supported by the IUT.
- -The channel is in the OPEN state and configured to use ERTM.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.91 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.91: L2CAP/ERM/BV-16-C [Send S-Frame [REJ]] MSC

- Expected Outcome

## Pass verdict

The IUT sends an S-frame REJ requesting I-frames with N(S) &gt;= 1 prior to the Retransmission timer of the Lower Tester expiring.

The IUT acknowledges all the I-frames that are sent by the Lower Tester after the S-frame REJ is sent.

## L2CAP/ERM/BV-17-C [Send S-Frame [SREJ]]

- Test Purpose

Verify that the IUT can send an S-frame [SREJ] after receiving out of sequence I-frames.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The TxWindow size of the Lower Tester must be greater than 2.
- -The channel is in the OPEN state and configured to use ERTM.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.92 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.92: L2CAP/ERM/BV-17-C [Send S-Frame [SREJ]] MSC

- Expected Outcome

## Pass verdict

The IUT sends an S-frame SREJ requesting I-frame with N(S) = 1 prior to the Retransmission timer of the Lower Tester expiring.

The IUT acknowledges all the I-frames that are sent by the Lower Tester.

## L2CAP/ERM/BV-18-C [Receive S-Frame [RR] Final Bit = 1]

- Test Purpose

Verify that the IUT retransmits any previously sent I-frames unacknowledged by receipt of an SFrame [RR] with the Final Bit set.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -MaxTransmit for the IUT is set to a value greater than 1.

## · Test Procedure

Figure 4.93 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.93: L2CAP/ERM/BV-18-C [Receive S-Frame [RR] Final Bit = 1] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame when it receives the S-frame from the Lower Tester that indicates that the previous transmission failed.

## L2CAP/ERM/BV-19-C [Receive I-Frame Final Bit = 1]

- Test Purpose

Verify that the IUT retransmits any previously sent I-frames unacknowledged by receipt of an I-frame with the final bit set.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -MaxTransmit for the IUT is set to a value greater than 1.

## · Test Procedure

Figure 4.94 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.94: L2CAP/ERM/BV-19-C [Receive I-Frame Final Bit = 1] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame when it receives the I-frame from the Lower Tester that indicates that the previous transmission failed.

## L2CAP/ERM/BV-20-C [Enter Remote Busy Condition]

- Test Purpose

Verify that the IUT does not retransmit any I-frames when it receives a remote busy indication from the Lower Tester (S-frame [RNR]).

- Reference

[1] 3.3.2, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -MaxTransmit for the IUT is set to a value greater than 1.

## · Test Procedure

Figure 4.95 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.95: L2CAP/ERM/BV-20-C [Enter Remote Busy Condition] MSC

- Expected Outcome

## Pass verdict

The IUT does not retransmit the unacknowledged I-frame.

## L2CAP/ERM/BV-22-C [Exit Local Busy Condition]

- Test Purpose

Verify that the IUT sends an S-frame [RR] Poll = 1 when the local busy condition is cleared.

- Reference

## 1 3.3.2, 8.6.4

- Initial Condition
- -Run test L2CAP/ERM/BV-07-C [Send S-Frame [RNR]].

- Test Procedure
- Expected Outcome

Figure 4.96: L2CAP/ERM/BV-22-C [Exit Local Busy Condition] MSC

## Pass verdict

The IUT sends an S-frame RR with the POLL bit set.

## L2CAP/ERM/BV-23-C [Transmit I-Frames using SAR]

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the enhanced control fields (SAR, F-bit, ReqSeq, TxSeq) when performing SAR.

- Reference

## 1 3.3.2

- Initial Condition
- -The connection is configured as ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The Lower Tester has configured a value for the MPS that ensures that the IUT performs SAR. The Lower Tester uses "TSPX\_iut\_SDU\_size\_in\_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.
- -The Lower Tester has configured a TxWindow size of 1.

## · Test Procedure

Figure 4.97 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.97: L2CAP/ERM/BV-23-C [Transmit I-Frames using SAR] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT.

## L2CAP/ERM/BI-01-C [S-Frame [REJ] Lost or Corrupted]

- Test Purpose

Verify that the IUT can handle receipt of an S-frame [RR] Poll = 1 if the S-frame [REJ] sent from the IUT is lost.

- Reference

[1] 3.3.2, 8.6.1.2, 8.6.4

- Initial Condition
- -The TxWindow size of the Lower Tester must be greater than 2 and should be the largest value that can be supported by the IUT.
- -The channel is in the OPEN state and configured to use ERTM.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.98 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.98: L2CAP/ERM/BI-01-C [S-Frame [REJ] Lost or Corrupted] MSC

- Expected Outcome

## Pass verdict

The IUT responds to the S-frame [RR] Poll = 1 with an S-frame [RR] Final = 1 that includes the TxSeq of the last received in sequence I-frame.

The IUT acknowledges all the I-frames that are sent by the Lower Tester after the S-frame REJ is sent.

## L2CAP/ERM/BI-02-C [S-Frame [SREJ] Lost or Corrupted]

- Test Purpose

Verify that the IUT can handle receipt of an S-frame [RR] Poll = 1 if the S-frame [SREJ] sent from the IUT is lost.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The TxWindow size of the Lower Tester must be greater than 2.
- -The channel is in the OPEN state and configured to use ERTM.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.99 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.99: L2CAP/ERM/BI-02-C [S-Frame [SREJ] Lost or Corrupted] MSC

- Expected Outcome

## Pass verdict

The IUT responds to the S-frame [RR] Poll = 1 with an S-frame [SREJ] Final = 1 that includes the TxSeq of the missing I-frame (N(S) = 1).

The IUT acknowledges all the I-frames that are sent by the Lower Tester after the S-frame SREJ is sent.

## L2CAP/ERM/BI-03-C [Handle Duplicate S-Frame [SREJ]]

- Test Purpose

Verify that the IUT only retransmits the requested I-frame once after receiving a duplicate SREJ.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin &gt; 1 in the Configure Request sent to the IUT.
- Test Procedure

Figure 4.100 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.100: L2CAP/ERM/BI-03-C [Handle Duplicate S-Frame [SREJ]] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester only once.

## L2CAP/ERM/BI-04-C [Handle Receipt of S-Frame [REJ] and S-Frame [RR, F=1] that Both Require Retransmission of the Same I-Frames]

- Test Purpose

Verify that the IUT only retransmits the requested I-frames once after receiving an S-frame [REJ] followed by an S-frame [RR] with the Final bit set that indicates the same I-frames should be retransmitted.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin &gt; 1 in the Configure Request sent to the IUT.
- Test Procedure

Figure 4.101 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.101: L2CAP/ERM/BI-04-C [Handle Receipt of S-Frame [REJ] and S-Frame [RR, F=1] that Both Require Retransmission of the Same I-Frames] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frames requested in the REJ from the Lower Tester only once.

## L2CAP/ERM/BI-05-C [Handle receipt of S-Frame [REJ] and I-Frame [F=1] that Both Require Retransmission of the Same I-Frames]

- Test Purpose

Verify that the IUT only retransmits the requested I-frames once after receiving an S-frame [REJ] followed by an I-frame with the Final bit set that indicates the same I-frames should be retransmitted.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin &gt; 1 in the Configure Request sent to the IUT.
- Test Procedure

Figure 4.102 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.102: L2CAP/ERM/BI-05-C [Handle receipt of S-Frame [REJ] and I-Frame [F=1] that Both Require Retransmission of the Same I-Frames] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frames requested in the REJ from the Lower Tester only once.

## 4.5.8 Streaming Mode (STM)

Verify the correct implementation of Streaming Mode in the IUT.

## L2CAP/STM/BV-01-C [Streaming Mode Source]

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Control fields (SAR, F-bit, ReqSeq, and TxSeq).

- Reference

## 1 3.3.2, 8.7

- Initial Condition
- -The channel is in the OPEN state and configured to use Streaming Mode.
- -No I-frames have been sent from the IUT or the Lower Tester.
- Test Procedure
- Expected Outcome

Figure 4.103: L2CAP/STM/BV-01-C [Streaming Mode Source] MSC

## Pass verdict

The Lower Tester receives three correctly formatted I-frames from the IUT.

## L2CAP/STM/BV-02-C [Streaming Mode Sink]

- Test Purpose

Verify that the IUT receives I-frames and handles SAR correctly.

- Reference

## 1 3.3.2, 8.7

- Initial Condition
- -The channel is in the OPEN state and configured to use Streaming Mode.
- -No I-frames have been sent from the IUT or the Lower Tester.
- -The IUT has configured a MTU and MPS size that is greater or equal to 48 bytes.

- Test Procedure
- Expected Outcome

Figure 4.104: L2CAP/STM/BV-02-C [Streaming Mode Sink] MSC

## Pass verdict

The IUT passes the received data correctly to the Upper Tester.

## L2CAP/STM/BV-03-C [Streaming Mode Source using SAR]

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Control fields (SAR, F-bit, ReqSeq, TxSeq) while performing SAR.

- Reference

[1] 3.3.2, 8.7

- Initial Condition
- -The channel is in the OPEN state and configured to use Streaming Mode.
- -No I-frames have been sent from the IUT or Lower Tester.
- -The Lower Tester has configured a value for the MPS that ensures that the IUT performs SAR. The Lower Tester uses "TSPX\_iut\_SDU\_size\_in\_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.

- Test Procedure
- Expected Outcome

Figure 4.105: L2CAP/STM/BV-03-C [Streaming Mode Source using SAR] MSC

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT.

## 4.5.9 Fixed Channel Support (FIX)

Verify the correct implementation of fixed channels information response in L2CAP.

## L2CAP/FIX/BV-01-C [Fixed Channels Supported Information Request]

- Test Purpose

Verify that the IUT can send an Information Request for the information type of Fixed Channels Supported.

- Reference

[1] 4.10, 4.11, 4.12, 4.13

- Initial Condition
- -The IUT has established that the Lower Tester supports Fixed Channels with an Info Request with Info Type set to Extended Features.

- Test Procedure
- Expected Outcome

Figure 4.106: L2CAP/FIX/BV-01-C [Fixed Channels Supported Information Request] MSC

## Pass verdict

The IUT sends Information Request [InfoType = Fixed Channels].

## L2CAP/FIX/BV-02-C [AMP Manager Channel Supported]

- Test Purpose

Verify that the IUT can send an Information Response for the information type of Fixed Channels Supported that contains the map of supported fixed channels with the AMP Manager Protocol Channel (bit-3 of octet 0) set to 1.

- Reference

[1] 4.10, 4.11, 4.12, 4.13

- Initial Condition
- -The Lower Tester has established that the IUT supports Fixed Channels by using an Info Request with the Info Type set to 0x0002 (Extended Features).

- Test Procedure
- Expected Outcome

Figure 4.107: L2CAP/FIX/BV-02-C [AMP Manager Channel Supported] MSC

## Pass verdict

The IUT sends Information Response [InfoType = Fixed Channels] and a result code of 'Success.'

The Fixed Channel Mask bit for L2CAP Signaling channel is set to 1.

The Fixed Channel Mask bit for AMP Manager Protocol channel is set to 1.

## L2CAP/FIX/BV-03-C [Information Request, Fixed Channels Supported]

- Test Purpose

Verify that the IUT returns the Fixed Channels Supported in response to the Information Request from the Lower Tester.

- Reference

[11] 4.10

- Initial Condition
- -The IUT is in the CLOSED state.
- -No ACL link exists between the Lower Tester and the IUT.
- -The IUT acts as an L2CAP acceptor.

- Test Procedure

The Lower Tester sends an information request to IUT.

Figure 4.108: L2CAP/FIX/BV-03-C [Information Request, Fixed Channels Supported] MSC

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP\_INFORMATION\_RSP PDU to the Lower Tester with the Info parameter containing 8 octets with the IUT Fixed L2CAP Channels. In the Info parameter, the octets match Table 4.25. In Table 4.25, the bit is set if the ICS entry is selected. All bits not listed are set to 0b0.

Table 4.25: Fixed Channels Supported Mask bits

| CID | Octet | Bit | Value |
| 0x0000 (Null ID) | 0 | 0 | 0b0 |
| 0x0001 (L2CAP Signaling Channel) | 0 | 1 | 0b1 |
| 0x0002 (Connectionless reception) | 0 | 2 | L2CAP 2/35 |
| 0x0003 (AMP Manager) | 0 | 3 | L2CAP 2/31 |
| 0x0007 (BR/EDR Security Manager) | 0 | 7 | 0b0 OR 0b1 |
| 0x003F (AMP Test Manager) | 7 | 7 | L2CAP 2/29 |

- Notes

The Lower Tester's RTX timer is set to maximum allowed initial value.

All CIDs that are RFU are set to 0b0.

## 4.5.10 Extended Window Size Configuration (EWC)

Verify the configuration of the Extended Window size option of L2CAP.

## L2CAP/EWC/BV-01-C [IUT Initiated Extended Window Size Option]

- Test Purpose

Verify that the IUT can configure a channel to use the Extended Window size option.

- Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1

- Initial Condition
- -The IUT has established that the peer L2CAP entity supports configuration of the Extended Window Size option (using the Information Request/Response [Extended Features] mechanism).

- Test Procedure
- Expected Outcome

Figure 4.109: L2CAP/EWC/BV-01-C [IUT Initiated Extended Window Size Option] MSC

## Pass verdict

The channel is established.

The IUT sends an L2CAP\_CONFIGURATION\_REQ including the Extended Feature Mask bit for Extended Window size option before the Configuration timer expires.

The IUT responds with Success to the Lower Tester sending an L2CAP\_CONFIGURATION\_REQ including the Extended Window size option.

## L2CAP/EWC/BV-02-C [Lower Tester Requests Extended Window Size]

- Test Purpose

Verify that the IUT uses the Extended Control Field in I/S-frames if the Lower Tester requests that Extended Window Size is used.

- Reference

[1] 3.3.2, 4.4, 4.5, 5.7, 6.1.4, 7.1, 8.2 (CSA1)

- Initial Condition
- -L2CAP/EWC/BV-01-C [IUT Initiated Extended Window Size Option] test case was completed successfully.

## · Test Procedure

Figure 4.110: L2CAP/EWC/BV-02-C [Lower Tester Requests Extended Window Size] MSC

- Expected Outcome

## Pass verdict

The channel is established.

The IUT accepts the EWS option while configuring.

The IUT includes ECF in S-frames sent to the Lower Tester.

The IUT includes ECF in I-frames sent to the Lower Tester.

## L2CAP/EWC/BV-03-C [Extended Window Size Option Not Supported by Lower Tester]

## · Test Purpose

Verify that the IUT does not include an Extended Window Size option when configuring the channel if the Lower Tester does not indicate support for the Extended Windows Size option in the Information Response [Extended Features].

## · Reference

[1] 4.4, 4.5, 5.5, 6.1.4, 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.

- Test Procedure
- Expected Outcome

Figure 4.111: L2CAP/EWC/BV-03-C [Extended Window Size Option Not Supported by Lower Tester] MSC

## Pass verdict

The IUT sends L2CAP\_CONFIGURATION\_REQ before Configuration Timer expires, with EWS option bit = 0.

## 4.5.11 Lock Step Configuration (LSC)

Verify the correct implementation of the Lock Step configuration Process.

## L2CAP/LSC/BV-01-C [Normal Lock Step Configuration Process for Best Effort, BR/EDR ERTM Channel]

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type 'Best Effort'.

- Reference

## 8 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.

- -L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT's Extended Features Mask.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.112: L2CAP/LSC/BV-01-C [Normal Lock Step Configuration Process for Best Effort, BR/EDR ERTM Channel] MSC

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_REQ packet with Extended Flow Spec options for BE.

The IUT responds to an L2CAP\_CONFIGURATION\_REQ packet, including Extended Flow Spec options for BE, with status pending before its RTX timer expires.

The IUT sends an L2CAP\_CONFIGURATION\_RSP packet with status success after reception of L2CAP\_CONFIGURATION\_RSP with status.

## L2CAP/LSC/BV-02-C [Normal Lock Step Configuration Process for Guaranteed, BR/EDR ERTM Channel]

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type 'Guaranteed'.

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.
- -L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT's Extended Features Mask.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.113: L2CAP/LSC/BV-02-C [Normal Lock Step Configuration Process for Guaranteed, BR/EDR ERTM Channel] MSC

## Pass verdict

The channel is established.

The IUT sends an L2CAP\_CONFIGURATION\_REQ packet with Extended Flow Spec options for Guaranteed.

The IUT responds to an L2CAP\_CONFIGURATION\_REQ packet with Extended Flow Spec options for Guaranteed, with status 'pending' before its RTX timer expires.

The IUT sends an L2CAP\_CONFIGURATION\_RSP packet with status 'success' after reception of L2CAP\_CONFIGURATION\_RSP with status pending before its ERTX timer expires.

## L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel]

- Test Purpose

Verify that the IUT closes the channel if it receives a Configuration response packet with result 'success' before receiving a Configuration response packet with result 'pending'.

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT's Extended Features Mask.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.114: L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel] MSC

## Pass verdict

The IUT stays in CONFIG state after receiving L2CAP\_CONFIGURATION\_RSP with results before receiving L2CAP\_CONFIGURATION\_RSP with 'pending' status.

The IUT sends L2CAP\_DISCONNECTION\_REQ with the same channel specified.

## L2CAP/LSC/BI-04-C [Mismatched Service Type, Best Effort, BR/EDR ERTM Channel]

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type 'Best Effort' and receives a Configuration request packet with an Extended Flow Specification containing service type 'Guaranteed'. S ee test case L2CAP/LSC/BV-03C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT's Extended Features Mask.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.115: L2CAP/LSC/BI-04-C [Mismatched Service Type, Best Effort, BR/EDR ERTM Channel] MSC

## Pass verdict

The IUT rejects mismatched L2CAP\_CONFIGURATION\_RSP by sending an L2CAP\_DISCONNECTION\_REQ.

## L2CAP/LSC/BI-05-C [Mismatched Service Type, Guaranteed, BR/EDR ERTM Channel]

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type 'Guaranteed' and receives a Configuration response packet with an Extended Flow Specification containing service type 'Best Effort'.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT's Extended Features Mask.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.116: L2CAP/LSC/BI-05-C [Mismatched Service Type, Guaranteed, BR/EDR ERTM Channel] MSC

## Pass verdict

The IUT rejects mismatched L2CAP\_CONFIGURATION\_RSP by sending an L2CAP\_DISCONNECTION\_REQ.

## L2CAP/LSC/BV-06-C [Remote Failed on Guaranteed, BR/EDR ERTM Channel]

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type 'Guaranteed' and after receiving a Configuration Response with result 'Pending' it receives a Configuration request packet with a 'Failure' result.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is established over BR/EDR using ERTM with the Extended Flow Specification bit set in the IUT's Extended Features Mask.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.117: L2CAP/LSC/BV-06-C [Remote Failed on Guaranteed, BR/EDR ERTM Channel] MSC

## Pass verdict

The IUT detects L2CAP\_CONFIGURATION\_RSP indicating 'no resources' (failure) by sending an L2CAP\_DISCONNECTION\_REQ.

## L2CAP/LSC/BV-07-C [Normal Lock Step Configuration Process for Best Effort, AMP Channel]

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type 'Best Effort'.

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.
- -L2CAP channel is connected over an AMP controller which can support guaranteed logical links.
- -The IUT is in CONFIG state.
- Test Procedure

Figure 4.118: L2CAP/LSC/BV-07-C [Normal Lock Step Configuration Process for Best Effort, AMP Channel] MSC

- Expected Outcome

## Pass verdict

The IUT sends an L2CAP\_CONFIGURATION\_REQ packet with Extended Flow Spec options for BE.

The IUT responds to an L2CAP\_CONFIGURATION\_REQ packet, including Extended Flow Spec options for BE, with status pending and can correctly receive a configuration response from the Lower Tester with the result = 'Pending' before its RTX timer expires.

The IUT sends an L2CAP\_CONFIGURATION\_RSP packet with status success after reception of L2CAP\_CONFIGURATION\_RSP with status pending can correctly receive the configuration response from the Lower Tester with the result = ' Success ' before its ERTX timer expires.

## L2CAP/LSC/BV-08-C [Normal Lock Step Configuration Process for Guaranteed, AMP Channel]

- Test Purpose

Verify that the IUT performs the Lock-step Configuration process including sending a properly formatted Enhanced Flow Specification option for service type 'Guaranteed'.

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -The IUT has established that the peer L2CAP entity supports Lockstep Configuration Process using the Information Request/Response [Extended Features] mechanism.
- -L2CAP channel is connected over an AMP controller which can support guaranteed logical links.
- -The IUT is in CONFIG state.

## · Test Procedure

Figure 4.119: L2CAP/LSC/BV-08-C [Normal Lock Step Configuration Process for Guaranteed, AMP Channel] MSC

- Expected Outcome

## Pass verdict

The channel is established.

The IUT sends an L2CAP\_CONFIGURATION\_REQ packet with Extended Flow Spec options for guaranteed service type.

The IUT responds to an L2CAP\_CONFIGURATION\_REQ packet with status pending before its RTX timer expires.

The IUT sends an L2CAP\_CONFIGURATION\_RSP packet with status success after reception of L2CAP\_CONFIGURATION\_RSP with status pending can correctly receive the configuration response from the Lower Tester with the result = ' Success ' before its ERTX timer expires.

## L2CAP/LSC/BV-09-C [Premature Success in Configuration Response, AMP Channel]

## · Test Purpose

Verify that the IUT closes the channel if it receives a Configuration response packet with result 'Success' before receiving a Configuration response packet with result 'Pending'.

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is connected over an AMP controller which can support guaranteed logical links.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.120: L2CAP/LSC/BV-09-C [Premature Success in Configuration Response, AMP Channel] MSC

## Pass verdict

The IUT stays in CONFIG state after receiving L2CAP\_CONFIGURATION\_RSP with results before receiving L2CAP\_CONFIGURATION\_RSP with 'Pending' status. IUT sends L2CAP\_DISCONNECTION\_REQ with the same channel specified.

## L2CAP/LSC/BI-10-C [Mismatched Service Type, Best Effort, AMP Channel]

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type 'Best Effort' and receives a Configuration request packet with an Extended Flow Specification containing service type 'Guaranteed'.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is connected over an AMP controller which can support guaranteed logical links.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.121: L2CAP/LSC/BV-10-I [Mismatched Service Type, Best Effort, AMP Channel] MSC

## Pass verdict

The IUT rejects mismatched L2CAP\_CONFIGURATION\_RSP by sending an L2CAP\_DISCONNECTION\_REQ.

## L2CAP/LSC/BI-11-C [Mismatched Service Type, Guaranteed, AMP Channel]

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type 'Guaranteed' and receives a Configuration request packet with an Extended Flow Specification containing service type 'Best Effort'.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is connected over an AMP controller which can support guaranteed logical links.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.122: L2CAP/LSC/BI-11-C [Mismatched Service Type, Guaranteed, AMP Channel] MSC

## Pass verdict

The IUT rejects mismatched L2CAP\_CONFIGURATION\_RSP by sending an L2CAP\_DISCONNECTION\_REQ.

## L2CAP/LSC/BV-12-C [Remote Failed on Guaranteed, AMP Channel]

- Test Purpose

Verify that the IUT closes the channel if it sends a Configuration request containing an Extended Flow Specification with service type 'Guaranteed' and after receiving a Configuration Response with result 'Pending' it receives a Configuration request packet with a 'Failure' result.

See test case L2CAP/LSC/BV-03-C [Premature Success in Configuration Response, BR/EDR ERTM Channel].

- Reference

[8] 7.1.3

- Initial Condition
- -An ACL connection has been established by the Lower Tester.
- -L2CAP channel is connected over an AMP controller which can support guaranteed logical links.
- -The IUT is in CONFIG state.
- Test Procedure
- Expected Outcome

Figure 4.123: L2CAP/LSC/BV-12-C [Remote Failed on Guaranteed, AMP Channel] MSC

## Pass verdict

The IUT detects L2CAP\_CONFIGURATION\_RSP indicating 'no resources' (failure) by sending an L2CAP\_DISCONNECTION\_REQ.

## 4.5.12 Create Channel (CCH)

Verify the correct implementation of the create channel request and response of the L2CAP layer.

## L2CAP/CCH/BV-01-C [Create Channel Request for an AMP Physical Link]

- Test Purpose

Verify that the IUT can request the creation of an L2CAP channel to run over an existing AMP physical link.

- Reference

[1] 4.14, 4.15

[8] 6.1, Figure 6.3

- Initial Condition
- -The AMP Physical Link for the Controller ID exists.

- Test Procedure
- Expected Outcome

Figure 4.124: L2CAP/CCH/BV-01-C [Create Channel Request for an AMP Physical Link] MSC

## Pass verdict

The IUT transmits L2CAP\_CREATE\_CHANNEL\_REQ over the signaling channel using a dynamically allocated SCID, a valid PSM value, and the Controller ID matching the ID for the existing AMP channel.

The IUT enters the OPEN state.

## L2CAP/CCH/BV-02-C [Create Channel Request for an AMP Physical Link -Refused]

- Test Purpose

Verify that the IUT can request the creation of an L2CAP channel to run over an existing AMP physical link, and to recover if the request is refused by the Lower Tester (L2CAP create channel response).

- Reference
- [1] 4.14, 4.15
- [8] 6.1, Figure 6.3
- Initial Condition
- -The AMP Physical Link for the Controller ID exists.

- Test Procedure

The 'Connection Refused' code sent by the Lower Tester may include: PSM not supported; Security Block; No Resources; Controller ID not supported.

Figure 4.125: L2CAP/CCH/BV-02-C [Create Channel Request for an AMP Physical Link -Refused] MSC

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP\_CREATE\_CHANNEL\_REQ over the signaling channel using a dynamically allocated SCID, a valid PSM value, and the Controller ID matching the ID for the existing AMP channel.

The IUT returns to the CLOSED state.

The IUT indicates failure to the Upper Tester.

## L2CAP/CCH/BV-03-C [Create Channel Request for an AMP Physical Link -Failed]

- Test Purpose

Verify that the IUT can request the creation of an L2CAP channel to run over an existing AMP physical link, and to recover if the request is accepted (L2CAP create channel response = 'Pending') by the Lower Tester but is failed after initiation.

- Reference

[1] 4.14, 4.15

[8] 6.1, Figure 6.3

- Initial Condition
- -The AMP Physical Link for the Controller ID exists.

- Test Procedure

The 'Connection Refused' code sent by the Lower Tester may include: PSM not supported; Security Block; No Resources; Controller ID not supported.

Figure 4.126: L2CAP/CCH/BV-03-C [Create Channel Request for an AMP Physical Link -Failed] MSC

- Expected Outcome

## Pass verdict

The IUT transmits L2CAP\_CREATE\_CHANNEL\_REQ over the signaling channel using a dynamically allocated SCID, a valid PSM value, and the Controller ID matching the ID for the existing AMP channel.

The IUT returns to the CLOSED state.

The IUT indicates failure to the Upper Tester.

## L2CAP/CCH/BV-04-C [Create Channel Response for an AMP Physical Link]

- Test Purpose

Verify that the IUT can receive and handle a request for connection establishment and configuration of an L2CAP channel to run over an existing AMP physical link.

- Reference

[1] 4.14, 4.15

- Initial Condition
- -The AMP Physical Link for the Controller ID exists.

- Test Procedure
- Expected Outcome

Figure 4.127: L2CAP/CCH/BV-04-C [Create Channel Response for an AMP Physical Link] MSC

## Pass verdict

The IUT transmits an L2CAP\_CREATE\_CHANNEL\_RSP with a result code of 'Connection Successful' (0x0000) or 'Connection Pending' (0x0001) before the Lower Tester RTX timer expires. If the result code = 'Connection Pending', the status code is 0x0000 - 0x0002.

The SCID in the response is equal to the SCID code in the request.

## 4.5.13 Move Channel (MCH)

Verify the correct implementation of the Move Channel request and response of the L2CAP layer.

## L2CAP/MCH/BV-01-C [Move ERTM Channel Request for BR/EDR to AMP -Success]

- Test Purpose

Verify that the IUT can request the move of an L2CAP ERTM channel from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP ERTM channel exists between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.128 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.128: L2CAP/MCH/BV-01-C [Move ERTM Channel Request for BR/EDR to AMP -Success] MSC

- Test Condition

The Lower Tester responds with a result field = 'Move Pending' and configures the new AMP channel so the channel can be move from BR/EDR to AMP.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ with a result code = 'Move Success' (0x0000). After it receives the L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_RSP from the Lower Tester, it sends a Receiver Ready message over the new AMP link on the same CID as before the move. The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

## L2CAP/MCH/BV-02-C [Move ERTM Channel Request for BR/EDR to AMP -Refused]

- Test Purpose

Verify that the IUT can request the move of an L2CAP ERTM channel from a BR/EDR link to an AMP link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the BR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP ERTM channel exists between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.129 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The 'Move Refused' result code sent by the Lower Tester may include: Controller ID not supported; new Controller ID is same as old Controller ID; configuration not supported; channel not allowed to be moved.

Figure 4.129: L2CAP/MCH/BV-02-C [Move ERTM Channel Request for BR/EDR to AMP -Refused] MSC

- Test Condition

The Lower Tester responds with result= 'Move Refused' so that the Move Channel Request from the IUT fails.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move failure one or both sides refuse' (0x0001) and it sends a Receiver Ready message over the BR/EDR link on the same CID as before the move attempt. The IUT does not transmit any Iframes between the Move Channel Request and RR packets.

## L2CAP/MCH/BV-03-C [Move ERTM Channel Request for BR/EDR to AMP -AMP Fail]

- Test Purpose

Verify that the IUT can request the move of an L2CAP channel from a BR/EDR link to an AMP link, and recover if the AMP channel creation fails. In this case the channel remains in state OPEN over the BR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.130 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR channel after the unsuccessful move attempt.

Figure 4.130: L2CAP/MCH/BV-03-C [Move ERTM Channel Request for BR/EDR to AMP -AMP Fail] MSC

- Test Condition

The Lower Tester responds with a result field = 'Move Pending' and configures the new AMP channel so the channel can be move from BR/EDR to AMP. However, the AMP channel configuration fails, so the Lower Tester replies with a failure indication.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move failure one or both sides refuse' (0x0001) and it sends a Receiver Ready message over the BR/EDR link on the same CID as before the move attempt. The IUT does not transmit any Iframes between the Move Channel Request and RR packets.

## L2CAP/MCH/BV-04-C [Move ERTM Channel Request for AMP to BR/EDR -Success]

- Test Purpose

Verify that the IUT can request the move of an L2CAP ERTM channel from an AMP link to a BR link.

If the operation is successful, the channel has to be in state OPEN over the BR link.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -The IUT is in OPEN state.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.131 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The IUT and the Lower Tester move to the new BR/EDR channel successfully.

Figure 4.131: L2CAP/MCH/BV-04-C [Move ERTM Channel Request for AMP to BR/EDR -Success] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ with a result code of 'Move Success' (0x0000). After it receives an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_RSP from the Lower Tester, it sends a Receiver Ready message over the new BR/EDR link on the same CID as before the move.

The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

## L2CAP/MCH/BV-05-C [Move ERTM Channel Request for AMP to BR/EDR -Refused]

- Test Purpose

Verify that the IUT can request the move of an L2CAP channel from an AMP link to a BR link.

If the operation is refused by the Lower Tester, the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -The IUT is in OPEN state.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.132 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful refused by the Lower Tester. The IUT and the Lower Tester return to the AMP channel after the unsuccessful move attempt.

Figure 4.132: L2CAP/MCH/BV-05-C [Move ERTM Channel Request for AMP to BR/EDR -Refused] MSC

- Test Condition

The AMP channel requires service not available on BR/EDR, e.g. much more bandwidth.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move refused - Configurat ion not supported' (0x0004).

The IUT does not transmit any I-frames between the Move Channel Request and RR packets.

## L2CAP/MCH/BV-06-C [Move ERTM Channel Response for BR/EDR to AMP -Success]

- Test Purpose

Verify that the IUT can receive and handle a request to move an L2CAP channel from a BR/EDR link to an AMP link.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.133 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.133: L2CAP/MCH/BV-06-C [Move ERTM Channel Response for BR/EDR to AMP -Success] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_RSP with a result code of 'Move Success' (0x0000) and responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) on the AMP link.

## L2CAP/MCH/BV-07-C [Move ERTM Channel Response for BR/EDR to AMP -Failure]

- Test Purpose

Verify that the IUT can receive and handle a request to move an L2CAP channel from a BR/EDR link to an AMP link where the move operation fails.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.134 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.134: L2CAP/MCH/BV-07-C [Move ERTM Channel Response for BR/EDR to AMP -Failure] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_RSP a result code of 'Move Success' (0x0000) and responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) over the BR/EDR link.

## L2CAP/MCH/BV-08-C [Move ERTM Channel Response for AMP to BR/EDR -Success]

- Test Purpose

Verify that the IUT can receive and handle a request to move an L2CAP channel from an AMP link to a BR/EDR link.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.135 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.135: L2CAP/MCH/BV-08-C [Move ERTM Channel Response for AMP to BR/EDR -Success] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_RSP with result code success (0) and the IUT responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) over the AMP link.

## L2CAP/MCH/BV-09-C [Move ERTM Channel Response for AMP to BR/EDR -Failure]

- Test Purpose

Verify that the IUT can receive and handle a request to move an L2CAP channel from an AMP link to a BR/EDR link where the move operation fails.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An L2CAP channel exists between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.136 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.136: L2CAP/MCH/BV-09-C [Move ERTM Channel Response for AMP to BR/EDR -Failure] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_RSP with result code of 'Move Success' (0x0000) and responds to the RR(P=1) with an RR(F=1, ReqSeq = 0) over the AMP link.

## L2CAP/MCH/BV-10-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP]

- Test Purpose

Verify that the IUT can move the active L2CAP ERTM channel from a BR/EDR link to an AMP link with no data loss above L2CAP.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -A BR/EDR L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.137 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.137: L2CAP/MCH/BV-10-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP] MSC

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT transmits a Receiver Ready packet over the new AMP channel at the end of the move with ReqSeq = 1.

## L2CAP/MCH/BV-11-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP -Unacknowledged Data]

- Test Purpose

Verify that the IUT can move the active L2CAP channel from a BR/EDR link to an AMP link with no data loss above L2CAP, and recover from data sent before the move but not yet acknowledged by the Lower Tester.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -A BR/EDR L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.138 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.138: L2CAP/MCH/BV-11-C [Data Transfer while Moving ERTM Channel from BR/EDR to AMP -Unacknowledged Data] MSC

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT transmits an RR(P=1, ReqSeq = 0) over the new AMP channel at the end of the move and it retransmits the I-frame over the new AMP channel when told by the Lower Tester.

## L2CAP/MCH/BV-12-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR]

## · Test Purpose

Verify that the IUT can move the active L2CAP channel from an AMP link to a BR/EDR link with no data loss above L2CAP.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An AMP L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.139 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.139: L2CAP/MCH/BV-12-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR] MSC

- Test Condition

In order for the Lower Tester to send an I-frame in response to the RR(P=1) at the end of the test it must be pending before the RR(P=1) is received.

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT sends an RR(P=1, ReqSeq=0) over the BR/EDR link at the end of the move and passes received data to the Upper Tester.

## L2CAP/MCH/BV-13-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR -Unacknowledged Data]

- Test Purpose

Verify that the IUT can move the active L2CAP channel from an AMP link to a BR/EDR link with no data loss above L2CAP, and recover from data sent before the move but not yet acknowledged by the Lower Tester.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An AMP L2CAP channel exists between the IUT and the Lower Tester. There has been data transfer on the channel.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.140 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.140: L2CAP/MCH/BV-13-C [Data Transfer while Moving ERTM Channel from AMP to BR/EDR -Unacknowledged Data] MSC

- Expected Outcome

## Pass verdict

The move operation is successful, the IUT sends an RR(P=1, ReqSeq = 0) over the BR/EDR link at the end of the move operation and retransmits the I-frame over the BR/EDR channel when requested by the Lower Tester.

## L2CAP/MCH/BV-14-C [Move Collision -ERTM]

- Test Purpose

Verify that the IUT can properly handle a move collision when both the IUT and Lower Tester attempt to move an ERTM channel from the BR/EDR link to an AMP link simultaneously.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An L2CAP ERTM channel exists between the IUT and the Lower Tester. There has been no data transfer on the channel.
- -The AMP Physical Link Exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.141 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.141: L2CAP/MCH/BV-14-C [Move Collision -ERTM] MSC

- Expected Outcome

## Pass verdict

Move operation is successful.

## ALT1:

The IUT's BD\_ADDR is larger than the Lower Tester's BD\_ADDR so the IUT sends L2CAP\_MOVE\_CHANNEL\_RSP with result code 'Move refused Move Channel collision' (0x0005). It sends RR(P=1, ReqSeq = 0) at the end of the move operation over the AMP link.

## ALT2:

The IUT's BD\_ADDR is smaller than the Lower Tester's BD\_ADDR so the IUT sends L2CAP\_MOVE\_CHANNEL\_RSP with result code of 'Move Pending' (0x0001). It responds to the RR(P=1) from the Lower Tester with RR(F=1) over the AMP link.

## L2CAP/MCH/BV-15-C [Move Channel Request for BR/EDR to AMP (STM Source) -Success]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.142 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.142: L2CAP/MCH/BV-15-C [Move Channel Request for BR/EDR to AMP (STM Source) -Success] MSC

- Test Condition

The Lower Tester responds with result= Move Pending and create the new AMP logical link so the channel can be move from BR/EDR to AMP.

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ with a result code of 'Move Success' (0x0000). After receiving the L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_RSP from the Lower Tester, it sends an I-frame.

## L2CAP/MCH/BV-16-C [Move Channel Request for BR/EDR to AMP (STM Sink) -Success]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

## · Reference

## 1 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.143 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.143: L2CAP/MCH/BV-16-C [Move Channel Request for BR/EDR to AMP (STM Sink) -Success] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ with a result code of 'Move Success' (0x0000). IUT receives an I -frame on the AMP and passes data up to the Upper Tester.

## L2CAP/MCH/BV-17-C [Move Channel Request for BR/EDR to AMP (STM Source) -Refused]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the BR/EDR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.144 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR link after the unsuccessful move attempt.

Figure 4.144: L2CAP/MCH/BV-17-C [Move Channel Request for BR/EDR to AMP (STM Source) -Refused] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move failure one or both sides refuse' (0x0001) and it sends an I -frame over the BR/EDR link on the same CID as before the move attempt.

## L2CAP/MCH/BV-18-C [Move Channel Request for BR/EDR to AMP (STM Sink) -Refused]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the BR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.145 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR link after the unsuccessful move attempt.

Figure 4.145: L2CAP/MCH/BV-18-C [Move Channel Request for BR/EDR to AMP (STM Sink) -Refused] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of Failure (0x0001) and it passes received data to the Upper Tester.

## L2CAP/MCH/BV-19-C [Move Channel Request for BR/EDR to AMP (STM Source) -AMP Fail]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link, and recover if the AMP logical link creation fails. In this case the channel remains in state OPEN over the BR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.146 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR link after the unsuccessful move attempt.

Figure 4.146: L2CAP/MCH/BV-19-C [Move Channel Request for BR/EDR to AMP (STM Source) -AMP Fail] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move Failure one or both sides refuse' (0x0001) and sends an I -frame over the BR/EDR link on the same CID as before the move attempt.

## L2CAP/MCH/BV-20-C [Move Channel Request for BR/EDR to AMP (STM Sink) -AMP Failed]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link, and recover if the AMP Logical Link creation fails. In this case the channel remains in state OPEN over the BR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.147 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the BR/EDR channel after the unsuccessful move attempt.

Figure 4.147: L2CAP/MCH/BV-20-C [Move Channel Request for BR/EDR to AMP (STM Sink) -AMP Failed] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move Failure one or both sides refuse' (0x0001) and passes the received data to the Upper Tester.

## L2CAP/MCH/BV-21-C [Move Channel Request for AMP to BR/EDR (STM Source) -Success]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

## · Reference

[1] 4.16, 4.17, 4.18, 9.2

## · Initial Condition

- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists with a guaranteed logical link. The requirements for that AMP channel does not exceed the capabilities of EDR.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.148 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.148: L2CAP/MCH/BV-21-C [Move Channel Request for AMP to BR/EDR (STM Source) -Success] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ with a result code of 'Move Success' (0x0000). After receiving the L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_RSP from the Lower Tester, it sends an I-frame over BR/EDR.

## L2CAP/MCH/BV-22-C [Move Channel Request for AMP to BR/EDR (STM Sink) -Success]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from an AMP link to a BR/EDR link. If the operation is successful, the channel is in state OPEN over the BR/EDR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

- Test Procedure

Figure 4.149 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.149: L2CAP/MCH/BV-22-C [Move Channel Request for AMP to BR/EDR (STM Sink) -Success] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ with a result code of 'Move Success' (0x0000). IUT receives I -frame on BR/EDR and passes data up to the Upper Tester.

## L2CAP/MCH/BV-23-C [Move Channel Request for AMP to BR/EDR (STM Source) -Refused]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data source from an AMP link to a BR/EDR link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.150 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP link after the unsuccessful move attempt.

Figure 4.150: L2CAP/MCH/BV-23-C [Move Channel Request for AMP to BR/EDR (STM Source) -Refused] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move failure one or both sides refuse' (0x0001) and it sends an I -frame over the AMP link on the same CID as before the move attempt.

## L2CAP/MCH/BV-24-C [Move Channel Request for AMP to BR/EDR (STM Sink) -Refused]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from an AMP link to a BR/EDR link, and recover if the Lower Tester refuses the move. In this case the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.151 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP channel after the unsuccessful move attempt.

Figure 4.151: L2CAP/MCH/BV-24-C [Move Channel Request for AMP to BR/EDR (STM Sink) -Refused] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move Failure one or both side refuse' (0x0001) and it passes received data to the Upper Tester.

## L2CAP/MCH/BV-25-C [Move Channel Request for AMP to BR/EDR (STM Source) -AMP Fail]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data source from an AMP link to a BR/EDR link, and recover if the admission control fails. In this case the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.152 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP link after the unsuccessful move attempt.

Figure 4.152: L2CAP/MCH/BV-25-C [Move Channel Request for AMP to BR/EDR (STM Source) -AMP Fail] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move failure one or both sides refuse' (0x0001) and sends an I -frame over the AMP link on the same CID as before the move attempt.

## L2CAP/MCH/BV-26-C [Move Channel Request for AMP to BR/EDR (STM Sink) -AMP Failed]

- Test Purpose

Verify that the IUT can request the move of an L2CAP Streaming Mode channel where the IUT is the data sink from an AMP link to a BR/EDR link, and recover if the Admission Control fails. In this case the channel remains in state OPEN over the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.153 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

The channel move is not successful. The IUT and the Lower Tester return to the AMP link after the unsuccessful move attempt.

Figure 4.153: L2CAP/MCH/BV-26-C [Move Channel Request for AMP to BR/EDR (STM Sink) -AMP Failed] MSC

- Expected Outcome

## Pass verdict

The IUT transmits an L2CAP\_MOVE\_CHANNEL\_CONFIRMATION\_REQ packet with a result code of 'Move failure one or both sides refuse' (0x0001) and passes the received data to the Upper Tester.

## L2CAP/MCH/BV-27-C [Move Channel Response for BR/EDR to AMP (STM Source) -Success]

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

## · Reference

## 1 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.154 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.154: L2CAP/MCH/BV-27-C [Move Channel Response for BR/EDR to AMP (STM Source) -Success] MSC

- Expected Outcome

## Pass verdict

The channel is moved successfully and the IUT sends an I-frame over the AMP link after the move completes.

## L2CAP/MCH/BV-28-C [Move Channel Response for BR/EDR to AMP (STM Sink) -Success]

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data sink from a BR/EDR link to an AMP link. If the operation is successful, the channel is in state OPEN over the AMP link.

## · Reference

[1] 4.16, 4.17, 4.18, 9.2

## · Initial Condition

- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.155 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.155: L2CAP/MCH/BV-28-C [Move Channel Response for BR/EDR to AMP (STM Sink) -Success] MSC

- Expected Outcome

## Pass verdict

The channel is successfully moved from the BR/EDR link to the AMP link and the received data is passed to the Upper Tester.

## L2CAP/MCH/BV-29-C [Move Channel Response for AMP to BR/EDR (STM Source) -Success]

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source. The channel is moved from an AMP to a BR/EDR link. If the operation is successful, the channel is in state OPEN over the BR/EDR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.156 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.156: L2CAP/MCH/BV-29-C [Move Channel Response for AMP to BR/EDR (STM Source) -Success] MSC

- Test Condition

The channel's Extended Flow Specification is valid for a BR/EDR link.

- Expected Outcome

## Pass verdict

The channel is moved successfully and the IUT sends an I-frame over the BR/EDR link after the move completes.

## L2CAP/MCH/BV-30-C [Move Channel Response for AMP to BR/EDR (STM Sink) -Success]

- Test Purpose

Verify that the IUT can respond to a move request for an L2CAP Streaming Mode channel where the IUT is the data sink. The channel is moved from an AMP link to a BR/EDR link. If the operation is successful, the channel is in state OPEN over the BR/EDR link.

## · Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.157 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.157: L2CAP/MCH/BV-30-C [Move Channel Response for AMP to BR/EDR (STM Sink) -Success] MSC

- Test Condition

The channel's Extended Flow Specification is valid for a BR/EDR link.

- Expected Outcome

## Pass verdict

The channel is successfully moved from the AMP link to the BR/EDR link and the received data is passed to the Upper Tester.

## L2CAP/MCH/BV-31-C [Move Channel Response for BR/EDR to AMP (STM Source) -Failed]

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source and is able to recover when the move operation fails. The channel is to be moved from a BR/EDR link to an AMP link but move operation fails.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.158 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.158: L2CAP/MCH/BV-31-C [Move Channel Response for BR/EDR to AMP (STM Source) -Failed] MSC

- Expected Outcome

## Pass verdict

The IUT sends an I-frame over the BR/EDR link after the failed move operation completes.

## L2CAP/MCH/BV-32-C [Move Channel Response for BR/EDR to AMP (STM Sink) -Failed]

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data sink and recover when the move operation fails. The channel is to not be moved from a BR/EDR link to an AMP link, but instead remains in the BR/EDR link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The AMP Physical Link exists.

- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.159 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.159: L2CAP/MCH/BV-32-C [Move Channel Response for BR/EDR to AMP (STM Sink) -Failed] MSC

- Expected Outcome

## Pass verdict

The IUT passed received data to the Upper Tester after the failed move operation completes.

## L2CAP/MCH/BV-33-C [Move Channel Response for AMP to BR/EDR (STM Source) -Failed]

- Test Purpose

Verify that the IUT can respond to a move request of an L2CAP Streaming Mode channel where the IUT is the data source and recover when the move operation fails. The channel is not to be moved from an AMP to a BR/EDR link, but instead remains on the AMP.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data source between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.160 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.160: L2CAP/MCH/BV-33-C [Move Channel Response for AMP to BR/EDR (STM Source) -Failed] MSC

- Test Condition

The channel's Extended Flow Specification is valid for a BR/EDR link.

- Expected Outcome

## Pass verdict

The IUT sends an I-frame over the AMP link after the failed move operation completes.

## L2CAP/MCH/BV-34-C [Move Channel Response for AMP to BR/EDR (STM Sink) -Failed]

- Test Purpose

Verify that the IUT can respond to a move request for an L2CAP Streaming Mode channel where the IUT is the data sink and recover when the move operation fails. The channel is not to be moved from an AMP link to a BR/EDR link, but instead remains on the AMP link.

- Reference

[1] 4.16, 4.17, 4.18, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists where the IUT is the data sink between the IUT and the Lower Tester in OPEN state.
- -The BR/EDR Physical Link exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.161 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.161: L2CAP/MCH/BV-34-C [Move Channel Response for AMP to BR/EDR (STM Sink) -Failed] MSC

- Test Condition

The channel's Extended Flow Specification is valid for a BR/EDR link.

- Expected Outcome

## Pass verdict

The IUT passes received data to the Upper Tester after the failed moved operation completes.

## L2CAP/MCH/BV-35-C [Move Collision -STM Source]

- Test Purpose

Verify that the IUT can properly handle a move collision when both the IUT and Lower Tester attempt to move a Streaming Mode channel from the BR/EDR link to an AMP link at the same time where the IUT is the data source.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists between the IUT and the Lower Tester. There has been no data transfer on the channel.
- -The AMP Physical Link Exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.162 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.162: L2CAP/MCH/BV-35-C [Move Collision -STM Source] MSC

- Expected Outcome

## Pass verdict

Move operation is successful.

## ALT1:

The IUT's BD\_ADDR is larger than the Lower Tester's BD\_ADDR so the IUT sends L2CAP\_MOVE\_CHANNEL\_RSP with result code of 'Move refused Move Channel collision' (0x0005). It sends an I-frame at the end of the move operation over the AMP link.

## ALT2:

The IUT's BD\_ADDR is smaller than Lower Tester's BD\_ADDR so IUT sends L2CAP\_MOVE\_CHANNEL\_RSP with result code of 'Move Pending' (0x0001). It sends an I -frame at the end of the move operation over the AMP link.

## L2CAP/MCH/BV-36-C [Move Collision -STM Sink]

- Test Purpose

Verify that the IUT can properly handle a move collision when both the IUT and Lower Tester attempt to move a Streaming Mode channel from the BR/EDR link to an AMP link at the same time where the IUT is the data sink.

- Reference

[1] 4.16, 4.17, 9.2

- Initial Condition
- -An L2CAP Streaming Mode channel exists between the IUT and the Lower Tester. There has been no data transfer on the channel.
- -The AMP Physical Link Exists.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.163 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.163: L2CAP/MCH/BV-36-C [Move Collision -STM Sink] MSC

- Expected Outcome

## Pass verdict

Move operation is successful.

## ALT1:

The IUT's BD\_ADDR is larger than Lower Tester's BD\_ADDR so IUT sends L2CAP\_MOVE\_CHANNEL\_RSP with result code refused - collision (0x0005). It passes the received data to the Upper Tester at the end of the move operation.

## ALT 2:

The IUT's BD\_ADDR is smaller than the Lower Tester's BD\_ADDR so the IUT sends L2CAP\_MOVE\_CHANNEL\_RSP with result code of 'Move Pending' (0x0001). It passes the received data to the Upper Tester at the end of the move operation.

## 4.5.14 Enhanced Retransmission Mode with Extended Control Field (ECF)

Verify the correct implementation of the Extended Control Field with Enhanced Retransmission Mode.

## L2CAP/ECF/BV-01-C [Receive I-Frames with Extended Control Field]

- Test Purpose

Verify that the IUT can receive in-sequence valid I-frames with the Extended Control Field and deliver L2CAP SDUs to the Upper Tester.

- Reference

[1] 3.3.2, 8.6

- Initial Condition
- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID.
- -The connection is configured as ERTM.
- -No I-frames have been received from the Lower Tester.
- -The IUT has configured a MTU and MPS size that is greater or equal to 48 bytes.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.164 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.164: L2CAP/ECF/BV-01-C [Receive I-Frames with Extended Control Field] MSC

## · Expected Outcome

## Pass verdict

Data in the received I-frame(s) match that sent by the Lower Tester.

SAR bits are set per specification.

F-bit is set to 0.

Complete SDU is sent to the Upper Tester.

All S-frames from the IUT contain the Extended Control Field.

## L2CAP/ECF/BV-02-C [Transmit I-Frames with Extended Control Field]

## · Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Extended Control Fields (SAR, F-bit, ReqSeq, TxSeq).

- Reference

[1] 3.3.2, 8.6

- Initial Condition
- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID.
- -The connection is configured as ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.165 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.165: L2CAP/ECF/BV-02-C [Transmit I-Frames with Extended Control Field] MSC

- Expected Outcome

## Pass verdict

The IUT sends I-frame(s) to the Lower Tester containing Extended Control Field.

Data in the I-frame(s) match that which was provided by the Upper Tester.

SAR bits are set per specification.

F-bit is set to 0.

## L2CAP/ECF/BV-03-C [Acknowledging Received I-Frames with Extended Control Field]

- Test Purpose

Verify that the IUT sends S-frame [RR] with Extended Control field and the Poll bit not set to acknowledge data received from the Lower Tester.

- Reference

## 1 3.3.2, 8.6.1.1

- Initial Condition
- -The IUT is in the INFO\_TRANSFER state for a data channel with assigned CID. The connection is configured as ERTM. No I-frames have been received from the Lower Tester.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.

## · Test Procedure

Figure 4.166 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.166: L2CAP/ECF/BV-03-C [Acknowledging Received I-Frames with Extended Control Field] MSC

- Expected Outcome

## Pass verdict

The IUT sends a Supervisory frame with S=RR, LastAckedReqSeq &lt; ReqSeq &lt;= last received Iframe's TxSeq+1, F=0, P=0, Reserved bits = 0 and Extended Control Field.

## L2CAP/ECF/BV-04-C [Send S-Frame [RR] with Extended Control Field and Poll Bit Set]

- Test Purpose

Verify that the IUT sends an S-frame [RR] with the Extended Control field and the Poll bit set when its retransmission timer expires.

- Reference

[1] 3.3.2, 8.6.1.4, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.167 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.167: L2CAP/ECF/BV-04-C [Send S-Frame [RR] with Extended Control Field and Poll Bit Set] MSC

- Expected Outcome

## Pass verdict

The IUT sends an S-frame with Extended Control Field and with the POLL bit set after the IUT Retransmission Timer (as specified by Lower Tester during configuration) expires.

The IUT does not retransmit the I-frame after receiving an S-frame from the Lower Tester that acknowledges the previously sent I-frame.

## L2CAP/ECF/BV-05-C [Respond to S-Frame [REJ] with Extended Control Field]

- Test Purpose

Verify that the IUT retransmits I-frames with Extended Control Field starting from the sequence number specified in the S-frame [REJ] with an Extended Control Field.

- Reference

[1] 3.3.2, 8.6.1.2, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin that is greater than 1 in the Configure Request sent to the IUT.

## · Test Procedure

Figure 4.168 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.168: L2CAP/ECF/BV-05-C [Respond to S-Frame [REJ] with Extended Control Field] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the first I-frame requested in the REJ from the Lower Tester before the Monitor Timer of the Lower Tester expires, including the Extended Control Field.

The IUT retransmits the second I-frame requested in the REJ from the Lower Tester before the IUT Retransmission Timer expires.

## L2CAP/ECF/BV-06-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL bit Set]

- Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame with an Extended Control Field. Verify that the IUT processes the acknowledgment of previously unacknowledged Iframes.

- Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

## · Initial Condition

- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.

## · Test Procedure

Figure 4.169 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.169: L2CAP/ECF/BV-06-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL bit Set] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The I-frame retransmitted by the IUT has the Final bit = 1, and the Extended Control Field.

The IUT processes the acknowledgment of the first I-frame (N(S) = 0) from the SREJ received and consequently send the pending I-frame (N(S) = 3).

## L2CAP/ECF/BV-07-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL Bit Clear]

## · Test Purpose

Verify that the IUT responds with the correct I-frame when sent an SREJ frame with an Extended Control Field.

## · Reference

[1] 3.3.2, 8.6.1.3, 8.6.4

- Initial Condition
- -The channel is in the OPEN state and configured to use ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The MaxTransmit for the IUT is set to a value greater than 1.
- -The Lower Tester has specified a value for TxWin of 3 in the Configure Request sent to the IUT.

## · Test Procedure

Figure 4.170 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.170: L2CAP/ECF/BV-07-C [Respond to S-Frame [SREJ] with Extended Control Field and POLL Bit Clear] MSC

- Expected Outcome

## Pass verdict

The IUT retransmits the I-frame, including an Extended Control Field, requested in the SREJ from the Lower Tester before the Monitor Timer of the Lower Tester expires.

The IUT does not transmit I-frame (N(S) = 3) as a result of receiving the SREJ from the Lower Tester.

## L2CAP/ECF/BV-08-C [Transmit I-Frames using Extended Control Field and SAR]

## · Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the extended control fields (SAR, F-bit, ReqSeq, TxSeq) when performing SAR.

- Reference

[1] 3.3.2

- Initial Condition
- -The connection is configured as ERTM.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The Lower Tester has configured a value for the MPS that ensures that the IUT performs SAR. The Lower Tester uses "TSPX\_iut\_SDU\_size\_in\_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.
- -The Lower Tester has configured a TxWindow size of 1.
- Test Procedure

Figure 4.171 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.171: L2CAP/ECF/BV-08-C [Transmit I-Frames using Extended Control Field and SAR] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT including an Extended Control Field.

## 4.5.15 Streaming Mode with Extended Control Field (STM)

Verify the correct implementation of the Extended Control Field with Streaming Mode.

## L2CAP/STM/BV-11-C [Streaming Mode Source with Extended Control Field]

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Extended Control fields (SAR, F-bit, ReqSeq, TxSeq).

- Reference

[1] 3.3.2, 8.7

- Initial Condition
- -The channel is in the OPEN state and configured to use Streaming Mode.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- Test Procedure

Figure 4.172 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.172: L2CAP/STM/BV-01-C [Streaming Mode Source with Extended Control Field] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives three correctly formatted I-frames from the IUT including Extended Control Fields.

## L2CAP/STM/BV-12-C [Streaming Mode Sink with Extended Control Field]

- Test Purpose

Verify that the IUT receives I-frames with Extended Control Field and handles SAR correctly.

- Reference

[1] 3.3.2, 8.7

- Initial Condition
- -The channel is in the OPEN state and configured to use Streaming Mode.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The IUT has configured a MTU and MPS size that is greater or equal to 48 bytes.
- Test Procedure

Figure 4.173 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.173: L2CAP/STM/BV-02-C [Streaming Mode Sink with Extended Control Field] MSC

- Expected Outcome

## Pass verdict

The IUT passes the received data correctly to the Upper Tester.

## L2CAP/STM/BV-13-C [Streaming Mode Source using Extended Control Field and SAR]

- Test Purpose

Verify that the IUT can send correctly formatted sequential I-frames with valid values for the Extended Control fields (SAR, F-bit, ReqSeq, TxSeq) while performing SAR.

- Reference

[1] 3.3.2, 8.7

- Initial Condition
- -The channel is in the OPEN state and configured to use Streaming Mode.
- -I(out) outgoing I-frames and I(in) incoming I-frames have been sent and received by the IUT over the channel after it was opened and before the test is executed.
- -The Lower Tester has configured a value for the MPS that ensures the IUT performs SAR. The Lower Tester uses "TSPX\_iut\_SDU\_size\_in\_bytes" as the value SDUs of N bytes that the IUT sends the Lower Tester.
- Test Procedure

Figure 4.174 assumes I(out) and I(in) are 0. The actual values of N(S) and N(R) for both incoming and outgoing traffic must take the number of previously sent and received I-frames into account.

Figure 4.174: L2CAP/STM/BV-13-C [Streaming Mode Source using Extended Control Field and SAR] MSC

- Expected Outcome

## Pass verdict

The Lower Tester receives six correctly formatted I-frames from the IUT, including Extended Control Fields.

## 4.6 Low Energy System tests

Verify the correct implementation of the LE features of L2CAP.

## 4.6.1 Connection Parameter Update

Verify the correct implementation of the LE connection parameter update feature.

## L2CAP/LE/CPU/BV-01-C [Send Connection Parameter Update Request]

- Test Purpose

Verify that the IUT can send the connection parameter update Request to Lower Tester when acting as a Peripheral device.

- Reference

[11] Table 2.1, Table 6.1, 4.20

- Initial Condition
- -The Lower Tester acts as a connection initiator and the IUT acts as an advertiser.
- -The IUT is in CLOSED state for data channel. No ACL link is established.
- -The Lower Tester's LL feature mask indicates that it does not support the Connection Parameters Request Procedure.
- -The Lower Tester becomes a Central device and the IUT becomes a Peripheral device after the connection is established.
- -For the parameters to send and receive, see [5].
- Test Procedure
1. ACL link is established.
2. The IUT sends L2CAP\_CONNECTION\_PARAMETER\_UPDATE\_REQ.
- Expected Outcome

Figure 4.175: L2CAP/LE/CPU/BV-01-C [Send Connection Parameter Update Request] MSC

## Pass verdict

The IUT transmits L2CAP\_CONNECTION\_PARAMETER\_UPDATE\_REQ over the LE signaling channel.

## L2CAP/LE/CPU/BV-02-C [Accept Connection Parameter Update Request]

- Test Purpose

Verify that the IUT can receive and handle a request for connection parameter update when acting as a Central device.

- Reference

[11] Table 6.1, 4.20, 4.21

- Initial Condition
- -The IUT is in CLOSED state. No ACL link exists. The IUT acts as L2CAP initiator.
- Test Procedure

ACL link establishment is part of the test case.

Figure 4.176: L2CAP/LE/CPU/BV-02-C [Accept Connection Parameter Update Request] MSC

- Test Condition

The IUT's Bluetooth device address BD\_ADDR is defined. For parameter to send and receive, see [5].

The IUT works as connection initiator, therefore, the IUT becomes a Central device and the Lower Tester acts as a Peripheral device after the connection is established.

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP\_CONNECTION\_PARAMETER\_UPDATE\_RSP over LE signaling channel before RTX timer expires with result code 0x0000.

- Notes

The Lower Tester's RTX timer is set to maximum allowed initial value.

## L2CAP/LE/CPU/BI-01-C [Reject Connection Parameter Update Parameters]

- Test Purpose

Verify that the IUT can reject a request for connection parameter update with illegal parameters.

- Reference

[11] Table 6.1, 4.20, 4.21

- Initial Condition
- -The IUT is in CLOSED state. No ACL link exists. The IUT acts as L2CAP initiator.

- Test Procedure

ACL link establishment is part of the test case.

The Lower Tester sends a Latency of larger than 500 in ConnectionParameterUpdateReq.

The IUT returns result of reject in ConnectionParameterUpdateRsp.

Figure 4.177: L2CAP/LE/CPU/BI-01-C [Reject Connection Parameter Update Parameters] MSC

- Test Condition

The IUT's Bluetooth device address BD\_ADDR is defined. For parameter to send and receive, see [5].

The IUT works as connection initiator, therefore the IUT becomes a Central device and the Lower Tester as a Peripheral device after the connection is established.

- Expected Outcome

## Pass verdict

The IUT sends a correct L2CAP\_CONNECTION\_PARAMETER\_UPDATE\_RSP with result code 0x0001 over LE signaling channel before RTX timer expires.

- Notes

The Lower Tester's RTX timer is set to maximum allowed initial value.

## L2CAP/LE/CPU/BI-02-C [Reject Connection Parameter Update Request]

- Test Purpose

Verify that the IUT can reject a request for connection parameter update in Peripheral mode.

- Reference

[11] Table 6.1, 4.20, 4.21

- Initial Condition
- -The IUT is in CLOSED state. No ACL link exists. The IUT acts as L2CAP acceptor.

- Test Procedure

ACL link establishment is part of the test case.

The Lower Tester sends ConnectionParameterUpdateReq over the LE signaling channel.

Figure 4.178: L2CAP/LE/CPU/BI-02-C [Reject Connection Parameter Update Request] MSC

- Test Condition

The IUT's Bluetooth device address BD\_ADDR is defined. For parameter to send and receive, see [5].

The Lower Tester acts as connection initiator, therefore the IUT becomes a Peripheral device and the Lower Tester acts as a Central device after the connection is established.

- Expected Outcome

## Pass verdict

The IUT sends L2CAP Command\_Reject with reason 'Command not understood' over the LE signaling channel before RTX timer expires.

- Notes

The Lower Tester's RTX timer is set to maximum allowed initial value.

## 4.6.2 Command Reject

Verify the correct implementation of the command reject.

## 4.6.2.1 Reject Unknown Command

- Test Purpose

Verify that the IUT can reject reserved and unknown commands.

- Reference

```
[11] 4.10
```

[12] 4, Table 4.2

- Initial Condition
- -The appropriate signaling channel for the transport is used as specified in Table 4.26.

- Test Case Configuration
- Test Procedure

Table 4.26: Reject Unknown Command test cases

| Test case | L2CAP/COS/CED/BI-01-C [Reject Unknown Command, BR/EDR] | L2CAP/LE/REJ/BI-02-C [Reject Unknown Command - LE] |
| Signaling Channel | 0x0001 | 0x0005 |
| RFU Codes | 0x1B to 0xFF | 0x1B to 0xFF |
| Unsupported Request and Indication Codes | 0x12 and 0x14 0x06 IF NOT L2CAP 2/45 0x08 IF NOT L2CAP 2/4 0x0A IF NOT L2CAP 2/6 0x0C, 0x0E, and 0x10 IF NOT L2CAP 2/29 0x16, 0x17, and 0x19 IF NOT L2CAP 2/48a | 0x02, 0x04, 0x08, 0x0A, 0x0C, 0x0E, 0x10 0x06 IF NOT L2CAP 2/45a 0x12 IF NOT L2CAP 2/43 0x14 IF NOT L2CAP 2/46 0x16 IF NOT (L2CAP 2/46 OR L2CAP 2/48b) 0x17 and 0x19 IF NOT L2CAP 2/48b |
| Unsupported Response Codes | 0x13 and 0x15 0x07 IF NOT L2CAP 2/45 0x09 IF NOT L2CAP 2/4 0x0B IF NOT L2CAP 2/6 0x0D, 0x0F, and 0x11 IF NOT L2CAP 2/29 0x18 and 0x1A IF NOT L2CAP 2/48a | 0x03, 0x05, 0x09, 0x0B, 0x0D, 0x0F, and 0x11 0x07 IF NOT L2CAP 2/45a 0x13 IF NOT L2CAP 2/42 0x15 IF NOT L2CAP 2/46 0x18 and 0x1A IF NOT L2CAP 2/48b |

Figure 4.179: Reject Unknown Command MSC

Repeat Steps 1 and 2 for every Unsupported Request and Indication Code based on the ICS support of the IUT in Table 4.26, for the first three RFU Codes in Table 4.26, and for three other RFU Codes in Table 4.26 selected at random.

1. The Lower Tester sends an L2CAP command with the Code defined in Table 4.26.
2. The IUT responds with an L2CAP\_COMMAND\_REJECT\_RSP.

Repeat Steps 3 and 4 for every Unsupported Response Code based on the ICS support of the IUT in Table 4.26.

3. The Lower Tester sends an L2CAP command with the Response Code.
4. The IUT either responds with an L2CAP\_COMMAND\_REJECT\_RSP or does not respond.

- Expected Outcome

## Pass verdict

In Step 2, and in Step 4 if the IUT responds, the IUT sends a correct L2CAP\_COMMAND\_REJECT\_RSP packet with reason 'Command not understood' and no Reason Data field over the transport and signaling channel as specified in Table 4.26.

## 4.7 Connectionless Basic L2CAP Mode

Verify the correct implementation of the connectionless services of the L2CAP layer.

## 4.7.1 Connectionless Reception Channel CLR

Verify the procedures for data exchange over the connectionless channel with the subgroups send data, receive data, disable and enable connectionless traffic.

## L2CAP/CLS/CLR/BV-01-C [Data Over Connectionless Channel]

- Test Purpose

Verify that the IUT can send data over the connectionless channel.

- Reference

[12] 3.2

- Initial Condition
- -The Lower Tester utilizes version L2CAP Basic Mode.
- -The IUT works as Central, a group has been created, and the Lower Tester has been added as member in the group.
- Test Procedure
- Expected Outcome

Figure 4.180: L2CAP/CLS/CLR/BV-01-C [Data Over Connectionless Channel] MSC

## Pass verdict

The IUT sends connectionless G-frame to the Lower Tester.

## L2CAP/CLS/UCD/BV-01-C [Data Reception over Unicast Connectionless Channel]

- Test Purpose

Verify that the IUT has the UCD bit set in the L2CAP Extended Features Mask to indicate support for reception of unicast connectionless data. Also verify that the IUT can receive data over the connectionless channel.

- Reference

[12] 3.2 and 7.6

- Initial Condition
- -An ACL connection exists between the Lower Tester and the IUT.
- Test Procedure

The Lower Tester requests Extended Features Mask using L2CAP Information Request. The Lower Tester then transmits a G-frame over the air to the IUT.

Figure 4.181: L2CAP/CLS/UCD/BV-01-C [Data Reception over Unicast Connectionless Channel] MSC

- Expected Outcome

## Pass verdict

The following conditions are met:

- -The L2CAP Extended Features Mask is successfully retrieved.
- -The Unicast Connectionless Data Reception bit in the L2CAP Extended Features Mask is set.
- -The IUT sends a connectionless G-frame to the Upper Tester.

## L2CAP/CLS/UCD/BV-02-C [Unencrypted data transmission over unicast connectionless channel]

- Test Purpose

Verify that the IUT can send unencrypted data over the connectionless channel.

Verify that the IUT can correctly send unencrypted G-frames to the Lower Tester.

- Reference

[12] 7.6

- Initial Condition
- -An ACL connection exists between the Lower Tester and the IUT.
- Test Procedure
- Expected Outcome

Figure 4.182: L2CAP/CLS/UCD/BV-02-C [Unencrypted data transmission over unicast connectionless channel] MSC

## Pass verdict

The IUT sends an unencrypted connectionless G-frame to the Lower Tester.

## L2CAP/CLS/UCD/BV-03-C [Encrypted Data Transmission over Unicast Connectionless Channel]

- Test Purpose

Verify that the IUT can send data over the connectionless channel.

- Reference

## 12 7.6

- Initial Condition
- -An unencrypted ACL connection exists between the Lower Tester and the IUT.

- Test Procedure
- Expected Outcome

Figure 4.183: L2CAP/CLS/UCD/BV-03-C [Encrypted Data Transmission over Unicast Connectionless Channel] MSC

## Pass verdict

The IUT performs the following in the specified order:

1. Authenticates the link.
2. Enables encryption.
3. Sends an encrypted connectionless G-frame to the Lower Tester.

## 4.8 Channel Identifiers (CID)

Tests that L2CAP in the IUT handles CIDs correctly on the connections to the same remote device.

## L2CAP/LE/CID/BV-01-C [Receiving DCID over BR/EDR and LE]

- Test Purpose

Tests that the L2CAP entity can receive the same DCID in L2CAP connect responses on both the BR/EDR and LE links.

- Reference

## 12 2.1

- Initial Condition
- -An ACL-U logical link exists between the IUT and Lower Tester.
- -An LE -U logical link exists between the IUT and Lower Tester.
- -The IUT has determined from TSPX\_psm or TSPX\_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the Lower Tester.
- -The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.

- Test Procedure
1. The Upper Tester commands the IUT to create an L2CAP connection on the ACL-U logical link to the Lower Tester.
2. The IUT issues an L2CAP Connection Request over the ACL-U logical link to a known PSM on the Lower Tester, using any allowable dynamically allocated CID in the range 0x0040 -0xFFFF for the SCID.
3. The Lower Tester sends an L2CAP Connection Response and assigns any allowable dynamically allocated CID in the range 0x0040 -0xFFFF for the DCID to complete the L2CAP connection.
4. The Upper Tester commands the IUT to create an L2CAP connection on the LE-U logical link to the Lower Tester.
5. The IUT issues an L2CAP LE Credit Based Connection Request over the LE-U logical link to a known SPSM on the Lower Tester, using any allowable dynamically allocated CID in the range 0x0040 -0x007F for the SCID.
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

## L2CAP/LE/CID/BV-02-C [Receiving SCID over BR/EDR and LE]

## · Test Purpose

Tests that the L2CAP entity can receive the same SCID in L2CAP connect requests on both the BR/EDR and LE links.

- Reference

## 12 2.1

- Initial Condition
- -An ACL-U logical link exists between the IUT and Lower Tester.
- -An LE -U logical link exists between the IUT and Lower Tester.
- -The IUT has made known to the Lower Tester via TSPX\_psm or TSPX\_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the IUT.
- -The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.

- Test Procedure
1. The Upper Tester commands the IUT to accept L2CAP connections on both BR/EDR and LE transports
2. The Lower Tester issues an L2CAP Connection Request, using any allowable dynamically allocated CID in the range 0x0040 -0x007F for the SCID, over the ACL-U logical link, to a known PSM on the IUT.
3. The IUT sends an L2CAP Connection Response, accepting the SCID proposed by the Lower Tester and using any allowable dynamically allocated CID in the range 0x0040 -0x007F for the DCID, to complete the L2CAP connection.
4. The Lower Tester issues an L2CAP LE Credit Based Connection Request over the LE-U logical link to a known SPSM on the IUT, using the same CID used in Step 2 for the SCID.
5. The IUT sends an LE Credit Based Connection Response, accepting the SCID proposed by the Lower Tester and using any allowable dynamically allocated CID in the range 0x0040 -0x007F for the DCID, to complete the L2CAP connection.
6. The Upper Tester commands the IUT to transfer data, of different content, over both L2CAP connections.
7. The Lower Tester issues an L2CAP Disconnection Request over the ACL-U logical link.
8. The Lower Tester issues an L2CAP Disconnection Request over the LE-U logical link.
- Expected Outcome

## Pass verdict

Both L2CAP connections complete successfully.

Correct data for each channel is transferred successfully over both connections.

Both L2CAP connections disconnect successfully.

## L2CAP/LE/CID/BV-03-C [Receiving same DCID over BR/EDR and LE]

## · Test Purpose

Tests that the L2CAP entity can receive the same DCID in L2CAP connect responses on both the BR/EDR and LE links, when operating in Enhanced Credit Based Flow Control Mode.

- Reference

## 13 2.1

- Initial Condition
- -An ACL-U logical link exists between the IUT and the Lower Tester.
- -An LE-U logical link exists between the IUT and the Lower Tester.
- -The IUT has determined from the TSPX\_psm or TSPX\_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the Lower Tester.
- -The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.
- Test Procedure

Same as for L2CAP/LE/CID/BV-01-C [Receiving DCID over BR/EDR and LE], with the remark that the IUT and the Lower Tester uses an Enhanced Credit Based Flow Control channel SPSM as declared via IXIT.

- Expected Outcome

## Pass verdict

Both L2CAP connections complete successfully.

Correct data for each channel is transferred successfully over both connections.

Both L2CAP connections disconnect successfully.

## L2CAP/LE/CID/BV-04-C [Receiving same SCID over BR/EDR and LE]

- Test Purpose

Tests that the L2CAP entity can receive the same SCID in L2CAP connect responses on both the BR/EDR and LE links, when operating in Enhanced Credit Based Flow Control Mode.

- Reference

## 13 2.1

- Initial Condition
- -An ACL-U logical link exists between the IUT and the Lower Tester.
- -An LE-U logical link exists between the IUT and the Lower Tester.
- -The IUT has determined from the TSPX\_psm or TSPX\_spsm IXIT values, or SDP and GATT, available PSMs and SPSMs on the Lower Tester.
- -The Lower Tester has the same public Bluetooth address on the BR/EDR and LE physical transports.
- Test Procedure

Same as for L2CAP/LE/CID/BV-02-C [Receiving SCID over BR/EDR and LE], with the remark that the IUT and the Lower Tester uses an Enhanced Credit Based Flow Control channel SPSM as declared via the TSPX\_spsm IXIT value.

- Expected Outcome

## Pass verdict

Both L2CAP connections complete successfully.

Correct data for each channel is transferred successfully over both connections.

Both L2CAP connections disconnect successfully.

## 4.8.1 Ignore Unsupported CIDs

- Test Purpose

Tests that the L2CAP entity ignores unsupported CIDs in a logical link.

- Reference

## 13 2.1

- Initial Condition
- -A logical link as specified in Table 4.27 exists between the IUT and the Lower Tester.
- -The Upper Tester can command the IUT to send data.

- Test Case Configuration
- Test Procedure

Table 4.27: Ignore Unsupported CIDs test cases

| Test Case ID | Logical Link | PDU CIDs |
| L2CAP/COS/CID/BI-01-C [Ignore Unsupported CIDs, ACL] | ACL | 0x0004, 0x0005, 0x0006, 0x0008, 0x003E |
| L2CAP/LE/CID/BI-01-C [Ignore Unsupported CIDs, LE] | LE-U | 0x0001, 0x0002, 0x0003, 0x0007, 0x0019, 0x003F, 0x0100, 0xFFFF |

Figure 4.184: Ignore Unsupported CIDs MSC

Repeat Steps 1 and 2 for each PDU CID in Table 4.27.

1. The Lower Tester sends an L2CAP Data (B-frame) PDU on the established logical link with the Channel ID of the PDU as specified in Table 4.27.
2. The IUT does not send the L2CAP data to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 2, the IUT ignores the L2CAP Data (B-frame) PDU from Step 1 and does not send the data to the Upper Tester.

## L2CAP/CLS/CID/BV-01-C [Ignore Unsupported CIDs, APB]

- Test Purpose

Tests that the L2CAP entity ignores unsupported CIDs in a BR/EDR APB logical link.

- Reference

## 13 2.1

- Initial Condition
- -An ACL connection exists between the Lower Tester and the IUT.

## · Test Procedure

The Lower Tester requests Extended Features Mask using an L2CAP Information Request. The Lower Tester then transmits a G-frame over the air to the IUT.

Figure 4.185: L2CAP/CLS/CID/BV-01-C [Ignore Unsupported CIDs, APB] MSC

1. The Lower Tester sends an L2CAP Info Request to the IUT with InfoType set to ExtendedFeatures.
2. The IUT sends an L2CAP Info Response to the IUT with InfoType set to ExtendedFeatures and the Extended Features Mask UCD bit set to 1.
3. The Lower Tester sends an L2CAP\_ECHO\_REQ to the IUT on CID 0x0001 via Active Broadcast.
4. The IUT does not send an L2CAP\_ECHO\_RSP to the Lower Tester.
5. The Upper Tester commands the IUT to create a dynamic L2CAP channel.
6. The IUT sends an L2CAP\_CONNECTION\_REQ to the Lower Tester with Source CID set to a dynamic CID.

7. The Lower Tester sends a successful L2CAP\_CONNECTION\_RSP with Source CID Set to the CID received in Step 6 and a Destination CID.
8. The IUT sends a successful Connection\_Complete event to the Upper Tester.
9. The Lower Tester sends a data packet to the IUT on the Source CID from Step 6 over the ACL connection.
10. The IUT sends the data received in Step 9 to the Upper Tester.
11. The Lower Tester sends a data packet to the IUT on the Source CID channel received from Step 6 over Active Broadcast.
12. The IUT does not send the packet received in Step 11 to the Upper Tester.
13. The Upper Tester commands the IUT to disconnect the channel created in Step 6.
14. The IUT sends an L2CAP\_DISCONNECTION\_REQ to the IUT to disconnect the connection created in Step 6.
15. The Lower Tester sends a successful L2CAP\_DISCONNECTION\_RSP to the IUT with Destination CID and Source CID set to the values received in Step 14.
16. The IUT sends a disconnect event to the Upper Tester.
17. Repeat Steps 18 -21 for CID values 0x0001, 0x0003, 0x00FF, 0xFFFF, and 2 random invalid CIDs from 0x0004 -0x00FE.
18. The Lower Tester sends a connectionless G-frame via Active Broadcast on the CID from Step 17 to the IUT.
19. The IUT does not send a data packet to the Upper Tester.
20. The Lower Tester sends a connectionless G-frame via Active Broadcast on the CID set to 0x0002 to the IUT.
21. The IUT sends a data packet to the Upper Tester.
- Expected Outcome

## Pass verdict

- -In Step 4, the IUT does not send an L2CAP\_ECHO\_RSP to the Lower Tester.
- -In Step 10, the IUT sends a data packet to the Upper Tester.
- -In Step 12, the IUT does not send a data packet to the Upper Tester.
- -In Step 19, the IUT does not send a data packet to the Upper Tester.
- -In Step 21, the IUT sends a data packet to the Upper Tester.

## 4.9 Credit Based Flow Control Mode

## 4.9.1 Enhanced Credit Based Flow Control Mode

## 4.9.1.1 L2CAP Credit Based Connection Request -Legacy Peer

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request to a legacy peer and receiving an L2CAP Command Reject does not establish any channel.

- Reference

## 13 4.25

- Initial Condition
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The signaling channel specified in Table 4.28 is used.

- Test Case Configuration
- Test Procedure
1. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) on the SPSM declared via IXIT.
2. The Lower Tester responds with an L2CAP Command Reject (Code = 0x01).
- Expected Outcome

Table 4.28: L2CAP Credit Based Connection Request -Legacy Peer test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-01-C [L2CAP Credit Based Connection Request - Legacy Peer, LE] | 0x0005 |
| L2CAP/ECFC/BV-45-C [L2CAP Credit Based Connection Request - Legacy Peer, BR/EDR] | 0x0001 |

Figure 4.186: L2CAP Credit Based Connection Request -Legacy Peer MSC

Pass verdict

After receiving the Command Reject from the Lower Tester, the IUT informs the Upper Tester.

## 4.9.1.2 L2CAP Credit Based Connection Request on Supported PSM

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request to a peer establishes all the channels upon receiving the L2CAP Credit Based Connection Response.

- Reference

[13] 4.25

- Initial Condition
- -The signaling channel specified in Table 4.29 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value and send credits.

- Test Case Configuration
- Test Procedure
1. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) on the SPSM declared via IXIT.
2. The Lower Tester responds with an L2CAP Credit Based Connection Response (Code = 0x18) packet.
3. The Lower Tester sends data on the established channel.
- Expected Outcome

Table 4.29: L2CAP Credit Based Connection Request on Supported PSM test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-02-C [L2CAP Credit Based Connection Request on Supported PSM, LE] | 0x0005 |
| L2CAP/ECFC/BV-46-C [L2CAP Credit Based Connection Request on Supported PSM, BR/EDR] | 0x0001 |

Figure 4.187: L2CAP Credit Based Connection Request on Supported PSM MSC

## Pass verdict

The IUT receives the data sent by the Lower Tester on the correct channel. The data is passed to the Upper Tester.

## 4.9.1.3 L2CAP Credit Based Connection Response on Supported PSM

- Test Purpose

Verify that an IUT receiving a valid L2CAP Credit Based Connection Request from a peer sends an L2CAP Credit Based Connection Response and establishes the channels.

- Reference

[13] 4.26

- Initial Condition
- -The signaling channel specified in Table 4.30 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to send data and credits.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) to the IUT on the SPSM specified in the initial conditions.
2. The IUT responds with an L2CAP Credit Based Connection Response (Code = 0x18).
3. The Upper Tester commands the IUT to send data on the data channel.
- Expected Outcome

Table 4.30: L2CAP Credit Based Connection Response on Supported PSM test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-03-C [L2CAP Credit Based Connection Response on Supported PSM, LE] | 0x0005 |
| L2CAP/ECFC/BV-47-C [L2CAP Credit Based Connection Response on Supported PSM, BR/EDR] | 0x0001 |

Figure 4.188: L2CAP Credit Based Connection Response on Supported PSM MSC

## Pass verdict

The IUT sends one or more correctly formatted K-frames on the correct channel to the Lower Tester.

The data sent by the IUT to the Lower Tester matches the data sent by the Upper Tester to the IUT.

## 4.9.1.4 L2CAP Credit Based Connection Request on an Unsupported PSM

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request on an unsupported PSM does not establish any channel upon receiving an L2CAP Credit Based Connection Response refusing the connection.

- Reference

[13] 4.25

- Initial Condition
- -The signaling channel specified in Table 4.31 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value.
- Test Case Configuration
- Test Procedure
1. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17) packet on the SPSM specified in the initial conditions which is not supported by the Lower Tester.
2. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result "0x0002 -All connections refused - LE PSM not supported".

Table 4.31: L2CAP Credit Based Connection Request on an Unsupported PSM test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-04-C [L2CAP Credit Based Connection Request on an Unsupported PSM, LE] | 0x0005 |
| L2CAP/ECFC/BV-48-C [L2CAP Credit Based Connection Request on an Unsupported PSM, BR/EDR] | 0x0001 |

Figure 4.189: L2CAP Credit Based Connection Request on an Unsupported PSM MSC

- Expected Outcome

## Pass verdict

The IUT receives an L2CAP Credit Based Connection Response packet with result '0x0002 All connections refused -LE PSM not supported' from the Lower Tester. This is indicated to the Upper Tester.

## 4.9.1.5 Credit Exchange -Receiving Incremental Credits

- Test Purpose

Verify that the IUT handles flow control correctly, by handling the L2CAP Flow Control Credit Indication sent by the peer.

- Reference

[13] 4.24

- Initial Condition
- -The signaling channel specified in Table 4.32 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -An LE or BR/EDR Data Channel is established on the SPSM.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The Upper Tester can command the IUT to send data.
- Test Case Configuration

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-06-C [Credit Exchange - Receiving Incremental Credits, LE] | 0x0005 |
| L2CAP/ECFC/BV-49-C [Credit Exchange - Receiving Incremental Credits, BR/EDR] | 0x0001 |

Table 4.32: Credit Exchange -Receiving Incremental Credits test cases

## · Test Procedure

Figure 4.190: Credit Exchange -Receiving Incremental Credits MSC

1. The Upper Tester requests the IUT to send data packets to the Lower Tester.
2. The IUT sends K-frames containing data to the Lower Tester, as many as the initial credit count.
3. The Lower Tester sends an L2CAP Flow Control Credit Indication (Code = 0x16) packet with Credit Value N to the IUT on the CID.
4. The IUT sends K-frames containing data to the Lower Tester.
5. After receiving N K-frames from the IUT and ensuring that no more K-frames are received, the Lower Tester sends a new L2CAP Flow Control Credit Indication packet with a Credits Value of N on the CID. The IUT sends N K-frames containing data to the Lower Tester.
6. The Test Procedure Steps 3 -5 are repeated with credit increment N = {1,&gt;1} without disconnecting the channel.
- Expected Outcome

## Pass verdict

After receiving N credits, the IUT sends N correctly formatted K-frames containing data to the Lower Tester.

The IUT stops sending K-frames to the Lower Tester when the credit count reaches zero.

## 4.9.1.6 Credit Exchange -Sending Credits

- Test Purpose

Verify that the IUT sends Flow Control Credit Indication to the peer.

- Reference

## 13 4.24

- Initial Condition
- -The signaling channel specified in Table 4.33 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.

- -An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The Upper Tester can command the IUT to send credits.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends data packets to the IUT until it gets credits returned, i.e., the data to send could consume more than the current credits available on the channel.
2. When the Lower Tester remains without credits, the Upper Tester commands the IUT to send N credits to the Lower Tester.
3. The IUT sends an L2CAP Flow Control Credit Indication (Code = 0x16) packet containing Credits = N to the Lower Tester.
4. The Lower Tester starts sending data packets to the IUT and sends N packets.
- Expected Outcome

Table 4.33: Credit Exchange -Sending Credits test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-07-C [Credit Exchange - Sending Credits, LE] | 0x0005 |
| L2CAP/ECFC/BV-50-C [Credit Exchange - Sending Credits, BR/EDR] | 0x0001 |

Figure 4.191: Credit Exchange -Sending Credits MSC

## Pass verdict

The IUT sends a correctly formatted L2CAP Flow Control Credit Indication (Code = 0x16) packet to the Lower Tester at least once doing the data transfer.

## 4.9.1.7 Credit Exchange -Zero Credits and Exceed Maximum Credits

- Test Purpose

Verify that the IUT ignores an L2CAP Flow Control Credit Indication packet with credit value set to zero and disconnects the Data Channel created through Enhanced Credit Based Flow Control Mode when the credit count exceeds 65535.

- Reference

[13] 4.24

- Initial Condition
- -The signaling channel specified in Table 4.34 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -An LE or BR/EDR Data Channel is established on the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The initial credit on the LE or BR/EDR Data Channel set by the Lower Tester is more than 1.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends an L2CAP Flow Control Credit Indication (Code = 0x16) packet to the IUT, with Credits = 0.
2. The IUT silently discards the packet and does not modify its credit count.

Table 4.34: Credit Exchange -Zero Credits and Exceed Maximum Credits test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BI-01-C [Credit Exchange - Zero Credits and Exceed Maximum Credits, LE] | 0x0005 |
| L2CAP/ECFC/BI-10-C [Credit Exchange - Zero Credits and Exceed Maximum Credits, BR/EDR] | 0x0001 |

Figure 4.192: Credit Exchange -Zero Credits and Exceed Maximum Credits MSC

3. The Lower Tester sends an L2CAP Flow Control Credit Indication packet containing a credit so large that it together with the remaining credits on the IUT exceeds 65535.
4. The IUT sends an L2CAP Disconnection Request (Code = 0x06) packet to the Lower Tester, for the CID with exceeding credits.
5. The Lower Tester sends an L2CAP Disconnection Response (Code = 0x07) to the IUT.
- Expected Outcome

## Pass verdict

The IUT ignores the L2CAP Flow Control Credit Indication packet with credit value set to zero, in Step 1.

Upon receiving a credit overflow, the IUT disconnects the Data Channel.

## 4.9.1.8 Credit Exchange -No Credits

- Test Purpose

Verify that the IUT either returns credits or disconnects the Data Channel created through Enhanced Credit Based Flow Control Mode when receiving a K-frame from the peer device that has the credit count of 0 (zero).

- Reference

[13] 4.24

- Initial Condition
- -The signaling channel specified in Table 4.35 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The initial credit on the LE Data Channel sent to the Lower Tester in a signaling packet is N. If the IUT allows the number of credits to be chosen, then N should be the smallest supported number greater than 1.
- Test Case Configuration

Table 4.35: Credit Exchange -No Credits test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BI-02-C [Credit Exchange - No Credits, LE] | 0x0005 |
| L2CAP/ECFC/BI-11-C [Credit Exchange - No Credits, BR/EDR] | 0x0001 |

- Test Procedure
1. The Lower Tester starts sending data packets to the IUT and sends N+1 packets.
2. After the IUT receives the N th packet, execute either alternative 2A or 2B.

Figure 4.193: Credit Exchange -No Credits MSC

Alternative 2A (The IUT does not return credits to the Lower Tester):

- 2A.1 The IUT receives the N+1 st packet, discards the packet, and sends an L2CAP\_DISCONNECTION\_REQ packet (Code = 0x06) to the Lower Tester.
- 2A.2 The Lower Tester sends an L2CAP\_DISCONNECTION\_RSP packet (Code = 0x07) to the IUT.
- Alternative 2B (The IUT returns credits to the Lower Tester):
- 2B.1 The IUT sends an L2CAP\_FLOW\_CONTROL\_CREDIT\_IND to the Lower Tester with Credits &gt; 0.
- 2B.2 The IUT receives the N+1 st packet.
- Expected Outcome

## Pass verdict

Upon receiving the N+1 st packet in Step 2A.1, the IUT disconnects the Data Channel, sending an L2CAP\_DISCONNECTION\_REQ packet to the Lower Tester.

In Step 2B.1, the IUT returns credits to the Lower Tester.

## L2CAP/ECFC/BV-11-C [Security -Insufficient Authentication -Responder, LE]

- Test Purpose

Verify that an IUT refuses to create any connection upon reception of an L2CAP Credit Based Connection Request which fails to satisfy authentication requirements.

- Reference

[13] 4.25

- Initial Condition
- -An LE ACL connection is established between the IUT and the Lower Tester.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -An authentication requirement exists for the SPSM channel declared via the TSPX\_spsm IXIT value.
- -Either no LTK exists or an Unauthenticated LTK exists between the IUT and the Lower Tester.
- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) on the SPSM specified in the initial conditions which requires authentication.
2. The IUT detects either there was no LTK or LTK with insufficient security level and sends an L2CAP Credit Based Connection Response (Code = 0x18), rejecting the connection request with error code ' All connections refused -insufficient authentication ' .
- Expected Outcome

Figure 4.194: Security -Insufficient Authentication -Responder, LE MSC

## Pass verdict

Upon reception of an L2CAP Credit Based Connection Request from the Lower Tester which fails to satisfy the authentication requirements, the IUT sends a correctly formatted L2CAP Credit Based Connection Response with Result 0x0005 ( ' All connections refused -insufficient a uthentication' ) to the Lower Tester.

## 4.9.1.9 Security -Insufficient Encryption Key Size -Initiator

- Test Purpose

Verify that the IUT does not establish any channel upon receipt of an L2CAP Credit Based Connection Response indicating the connections were refused with Result 0x0007 ('All c onnections refused -insufficient encryption key s ize' ).

## · Reference

## 13 4.25

- Initial Condition
- -The signaling channel specified in Table 4.36 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value.
- -Either an Unauthenticated or Authenticated LTK exists between the IUT and the Lower Tester.

## · Test Case Configuration

Table 4.36: Security -Insufficient Encryption Key Size -Initiator test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-14-C [Security - Insufficient Encryption Key Size - Initiator, LE] | 0x0005 |
| L2CAP/ECFC/BV-52-C [Security - Insufficient Encryption Key Size - Initiator, BR/EDR] | 0x0001 |

- Test Procedure
1. The Upper Tester commands the IUT to send a connection request.
2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).
3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0007 ('All c onnections refused - insufficient encryption key size"), refusing the connection request.
- Expected Outcome

Figure 4.195: Security -Insufficient Encryption Key Size -Initiator MSC

## Pass verdict

The IUT informs the Upper Tester about the rejection.

## 4.9.1.10 L2CAP Credit Based Connection Response -refused due to insufficient resources

- Test Purpose

Verify that an IUT receiving an L2CAP Credit Based Connection Request for several channels refuses the connection s for which it doesn't have sufficient resources with result 0x0004 ('Some connections refused -insufficient resources available").

- Reference

[13] 4.25

- Initial Condition
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The maximum number of L2CAP channels for the SPSM is declared via the TSPX\_iut\_supported\_max\_channels IXIT value that the IUT supports.
- -The signaling channel specified in Table 4.37 is used.
- -A number of LE or BR/EDR Data Channels are established on the SPSM declared via IXIT, such that this number is less than the maximum number previously stated in the TSPX\_spsm IXIT value, with at most 4.
- Test Case Configuration
- Test Procedure

Table 4.37: L2CAP Credit Based Connection Response -refused due to insufficient resources test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-17-C [L2CAP Credit Based Connection Response - refused due to insufficient resources, LE] | 0x0005 |
| L2CAP/ECFC/BV-53-C [L2CAP Credit Based Connection Response - refused due to insufficient resources, BR/EDR] | 0x0001 |

Figure 4.196: L2CAP Credit Based Connection Response -refused due to insufficient resources MSC

1. The Lower Tester sends an L2CAP Credit Based Connection Request on different CIDs than the existing ones, to reach the maximum number of channels + 1.
2. Either the IUT establishes the new channels, up to the maximum supported, and sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with Result 0x0004 (' Some connections refused -insufficient resources available ' ) as in ALT 1, or if the IUT can support the maximum number of channels, then according to ALT 2, the new L2CAP channels are established.
3. The IUT sends data on at least one of the newly created channels.
- Expected Outcome

## Pass verdict

In Step 2, the IUT follows either ALT 1 or ALT 2:

ALT 1: The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x0004 (' Some connections refused -insufficient resources available ' ).

ALT 2: The IUT can establish the maximum number of channels, and the new L2CAP channels are successfully established. The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x0000 ('All connections successful'). The IUT sends at least one data packet on one of the newly created channels.

## 4.9.1.11 L2CAP Credit Based Connection Request -refused due to Invalid Source CID

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request does not establish some of the requested channels upon receiving an L2CAP Credit Based Connection Response refusing the connections with result 0x0009 ('Some c onnections refused -Invalid Source CID").

- Reference

[13] 4.25

- Initial Condition
- -The signaling channel specified in Table 4.38 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value.
- Test Case Configuration

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-18-C [L2CAP Credit Based Connection Request - refused due to Invalid Source CID, LE] | 0x0005 |
| L2CAP/ECFC/BV-54-C [L2CAP Credit Based Connection Request - refused due to Invalid Source CID, BR/EDR] | 0x0001 |

Table 4.38: L2CAP Credit Based Connection Request -refused due to Invalid Source CID test cases

## · Test Procedure

Figure 4.197: L2CAP Credit Based Connection Request -refused due to Invalid Source CID MSC

1. The Upper Tester commands the IUT to send a connection request.
2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).
3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0009 ('Some c onnections refused - invalid Source CID' ), refusing the connection request.
4. (ALT1) If the connection request was performed with more than one SCID and some of the channels were created, the Upper Tester commands the IUT to send data on the accepted CIDs.
- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester that some connections were refused.

(ALT1) The data sent by the IUT in Step 3 must be the same as that received by the Lower Tester.

The IUT does not send any data to the Lower Tester on the refused CID(s).

## 4.9.1.12 L2CAP Credit Based Connection Request -refused due to Source CID already allocated

## · Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request does not establish some of the requested channels upon receiving an L2CAP Credit Based Connection Response refusing some of the connections with result 0x000A ('Some c onnections refused -Source CID already allocated").

- Reference

[13] 4.25

- Initial Condition
- -The signaling channel specified in Table 4.39 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value.
- Test Case Configuration
- Test Procedure
1. The Upper Tester commands the IUT to send a connection request.
2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).
3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x000A ('Some c onnections refused -Source CID already allocated' ), refusing the connection request.
4. (ALT1) If the connection request was performed with more than one SCID and some of the channels were created, the Upper Tester commands the IUT to send data on the accepted CIDs.

Table 4.39: L2CAP Credit Based Connection Request -refused due to Source CID already allocated test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-19-C [L2CAP Credit Based Connection Request - refused due to Source CID already allocated, LE] | 0x0005 |
| L2CAP/ECFC/BV-55-C [L2CAP Credit Based Connection Request - refused due to Source CID already allocated, BR/EDR] | 0x0001 |

Figure 4.198: L2CAP Credit Based Connection Request -refused due to Source CID already allocated MSC

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester that the connection was refused.

(ALT1) The data send by the IUT in Step 3 must be the same as that received by the Lower Tester.

The IUT does not send any data to the Lower Tester on the refused CID(s).

## 4.9.1.13 L2CAP Credit Based Connection Response -refused due to Source CID already allocated

- Test Purpose

Verify that an IUT receiving an L2CAP Credit Based Connection Request for several channels refuses some of the connections with result 0x000A ('Some c onnections refused -Source CID already allocated ' ) if it receives a Source CID which is already in use.

- Reference

[13] 4.25

- Initial Condition
- -The signaling channel specified in Table 4.40 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -One LE or BR/EDR Data channel is established on the SPSM declared via the TSPX\_spsm IXIT value.
- Test Case Configuration
- Test Procedure

Table 4.40: L2CAP Credit Based Connection Response -refused due to Source CID already allocated test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-20-C [L2CAP Credit Based Connection Response - refused due to Source CID already allocated, LE] | 0x0005 |
| L2CAP/ECFC/BV-56-C [L2CAP Credit Based Connection Response - refused due to Source CID already allocated, BR/EDR] | 0x0001 |

Figure 4.199: L2CAP Credit Based Connection Response -refused due to Source CID already allocated MSC

1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) using the same CID as the previously established channel.
2. The IUT sends an L2CAP Credit Based Connection Response (Code = 0x18) to the Lower Tester with result 0x000A ('Some c onnections refused -Source CID already allocated ') .
- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x000A ('Some c onnections refused -Source CID already allocated ') .

## 4.9.1.14 L2CAP Credit Based Connection Request -refused due to Unacceptable Parameters

- Test Purpose

Verify that an IUT sending an L2CAP Credit Based Connection Request does not establish any channel upon receiving an L2CAP Credit Based Connection Response refusing the connections with result 0x000B ('All c onnections refused -unacceptable parameters ' ).

- Reference

[13] 4.25

- Initial Condition
- -The signaling channel specified in Table 4.41 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value.
- Test Case Configuration

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-21-C [L2CAP Credit Based Connection Request - refused due to Unacceptable Parameters, LE] | 0x0005 |
| L2CAP/ECFC/BV-57-C [L2CAP Credit Based Connection Request - refused due to Unacceptable Parameters, BR/EDR] | 0x0001 |

Table 4.41: L2CAP Credit Based Connection Request -refused due to Unacceptable Parameters test cases

- Test Procedure
1. The Upper Tester commands the IUT to send a connection request.
2. The IUT sends an L2CAP Credit Based Connection Request (Code = 0x17).
3. The Lower Tester sends an L2CAP Credit Based Connection Response (Code = 0x18) with result 0x000B ('All c onnections refused -unacceptable parameters ' ), refusing the connection request.
- Expected Outcome

Figure 4.200: L2CAP Credit Based Connection Request -refused due to Unacceptable Parameters MSC

## Pass verdict

The IUT informs the Upper Tester that the connection was refused.

## 4.9.1.15 Renegotiate MTU -Initiator

- Test Purpose

Verify that the IUT sending an L2CAP Credit Based Reconfigure Request can reconfigure the Maximum Transmission Unit (MTU) for the indicated channels, being able to receive larger SDUs.

- Reference

[13] 4.27

- Initial Condition
- -The maximum supported MTU size is defined by the TSPX\_l2ca\_cbmtu\_max IXIT entry.
- -The minimum supported MTU size is defined by the TSPX\_l2ca\_cbmtu\_min IXIT entry.
- -The signaling channel specified in Table 4.42 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.

## · Test Case Configuration

Table 4.42: Renegotiate MTU -Initiator test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-22-C [Renegotiate MTU - Initiator, LE] | 0x0005 |
| L2CAP/ECFC/BV-58-C [Renegotiate MTU - Initiator, BR/EDR] | 0x0001 |

- Test Procedure
1. If the minimum supported MTU size equals the maximum supported MTU size or the current MTU size equals the maximum supported MTU size, the test ends with a Pass verdict.
2. The Lower Tester continuously transmits SDUs of a size that the MTU negotiated at channel initialization, at a minimum rate of two packets per second, over the L2CAP channel. Transmit at least 2 SDUs.
3. The Upper Tester commands the IUT to increase the MTU size for the opened channel.
4. The IUT sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_REQ (Code = 0x19) packet to the Lower Tester, with the MTU field greater than the one in the initial configuration of the channel.
5. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_RSP (Code = 0x1A) packet to the IUT, with the Result field equal to 0x0000 (Reconfiguration successful).
6. The Lower Tester transmits SDUs of a size equal to the MTU in Step 3 to the IUT. Transmit at least 2 SDUs.

Figure 4.201: Renegotiate MTU -Initiator MSC

- Expected Outcome

## Pass verdict

Complete SDUs are sent to the Upper Tester, for Steps 3 and 6.

## 4.9.1.16 Renegotiate MTU -Responder

- Test Purpose

Verify that the IUT receiving an L2CAP Credit Based Reconfigure Request can reconfigure the Maximum Transmission Unit (MTU) for an indicated channel, being able to send larger SDUs.

- Reference

[13] 4.28

- Initial Condition
- -The maximum supported MTU size is defined by the TSPX\_l2ca\_cbmtu\_max IXIT entry.
- -The minimum supported MTU size is defined by the TSPX\_l2ca\_cbmtu\_min IXIT entry.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The signaling channel specified in Table 4.43 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Lower Tester's initial MTU is equal to the IUT's minimum MTU size from the TSPX\_tester\_mtu IXIT value.
- Test Case Configuration

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-23-C [Renegotiate MTU - Responder, LE] | 0x0005 |
| L2CAP/ECFC/BV-59-C [Renegotiate MTU - Responder, BR/EDR] | 0x0001 |

Table 4.43: Renegotiate MTU -Responder test cases

## · Test Procedure

Figure 4.202: Renegotiate MTU -Responder MSC

1. If the minimum supported MTU size equals the maximum supported MTU size or the current MTU size equals the maximum supported MTU size, the test ends with a Pass verdict.
2. The Upper Tester commands the IUT to continuously transmit SDUs of a size equal to the MTU negotiated at channel initialization over the L2CAP channel at a minimum rate of two packets per second. Transmit at least 2 SDUs.
3. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_REQ (Code = 0x19) packet to the IUT, with the MTU field set to the IUT's maximum MTU size from IXIT .
4. The IUT sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_RSP (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0000 (Reconfiguration successful).
5. The Upper Tester commands the IUT to transmit SDUs of a size equal to the MTU in Step 3 to the Lower Tester. Transmit at least 2 SDUs.
- Expected Outcome

## Pass verdict

Complete SDUs are sent to the Upper Tester, for Steps 2 and 5.

## 4.9.1.17 Renegotiate MTU -MTU value is decreased

- Test Purpose

Verify that the IUT refuses the MTU reconfiguration request for a Data Channel created through Enhanced Credit Based Flow Control Mode when receiving an L2CAP Credit Based Reconfigure Request with a lower MTU value than the existing one.

- Reference

[13] 4.27

- Initial Condition
- -The signaling channel specified in Table 4.44 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value, with the MTU on the Lower Tester side of at least 65 octets.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request (Code = 0x19) packet to the IUT, with the MTU field lower than the one in the channel initial configuration.
2. The IUT does not disconnect the channel. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0001 (Reconfiguration failed - reduction in size of MTU not allowed).
- Expected Outcome

Table 4.44: Renegotiate MTU -MTU value is decreased test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BI-03-C [Renegotiate MTU - MTU value is decreased, LE] | 0x0005 |
| L2CAP/ECFC/BI-12-C [Renegotiate MTU - MTU value is decreased, BR/EDR] | 0x0001 |

Figure 4.203: Renegotiate MTU -MTU value is decreased MSC

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0001 (Reconfiguration failed - reduction in size of MTU not allowed).

## 4.9.1.18 Renegotiate MPS -Initiator

- Test Purpose

Verify that the IUT sending an L2CAP Credit Based Reconfigure Request can receive differently sized L2CAP PDUs on the indicated channels.

- Reference

[13] 4.27

- Initial Condition
- -The signaling channel specified in Table 4.45 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The minimum supported IUT MPS size is defined by the TSPX\_l2ca\_cbmps\_min IXIT entry.
- -The maximum supported IUT MPS size is defined by the TSPX\_l2ca\_cbmps\_max IXIT entry.
- Test Case Configuration

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-24-C [Renegotiate MPS - Initiator, LE] | 0x0005 |
| L2CAP/ECFC/BV-60-C [Renegotiate MPS - Initiator, BR/EDR] | 0x0001 |

Table 4.45: Renegotiate MPS -Initiator test cases

## · Test Procedure

Figure 4.204: Renegotiate MPS -Initiator MSC

1. If TSPX\_l2ca\_cbmps\_min equals TSPX\_l2ca\_cbmps\_max, the test ends with a Pass verdict.
2. The IUT configures a value N for the MPS. If TSPX\_l2ca\_cbmps\_max equals TSPX\_l2ca\_cbmps\_min plus 1, then N equals TSPX\_l2ca\_cbmps\_min. Otherwise, N is greater than TSPX\_l2ca\_cbmps\_min and lower than TSPX\_l2ca\_cbmps\_max. The Lower Tester

chooses, for the remaining steps, an SDU size that ensures that the Lower Tester performs segmentation.

3. The Lower Tester transmits SDUs (SDU size in Step 1) at a minimum rate of two packets per second, segmented into data packets with payload of size N over the L2CAP channel. Transmit at least 5 SDUs.
4. The IUT sends an L2CAP Credit Based Reconfigure Request (Code = 0x19) packet to the Lower Tester, with MPS = N + 1 bytes.
5. The Lower Tester sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the IUT, with the Result field equal to 0x0000 (Reconfiguration successful).
6. The Lower Tester transmits SDUs (SDU size in Step 2), segmented into data packets with payload of size N + 1 to the IUT. Transmit at least 5 SDUs. If N = TSPX\_l2ca\_cbmps\_min, skip to Step 9.
7. The IUT sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_REQ packet to the Lower Tester, with MPS = N -1 bytes.
8. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_RSP packet to the IUT, with the Result field equal to 0x0000 (Reconfiguration successful).
9. The Lower Tester transmits SDUs (SDU size in Step 2), segmented into data packets with payload of size N -1 to the IUT. Transmit at least 5 SDUs.
- Expected Outcome

## Pass verdict

Complete SDUs are sent to the Upper Tester in Steps 3, 6, and 9.

## 4.9.1.19 Renegotiate MPS -Responder

- Test Purpose

Verify that the IUT receiving an L2CAP Credit Based Reconfigure Request can send differently sized L2CAP PDUs on the indicated channel.

- Reference

[13] 4.28

- Initial Condition
- -The minimum supported IUT MPS size is defined by the TSPX\_l2ca\_cbmps\_min IXIT entry.
- -The maximum supported IUT MPS size is defined by the TSPX\_l2ca\_cbmps\_max IXIT entry.
- -The signaling channel specified in Table 4.46 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Lower Tester's initial MTU is equal to the IUT's maximum MTU size from the TSPX\_l2ca\_cbmtu\_max IXIT value.
- -The Lower Tester has configured a value N for the MPS, higher than TSPX\_l2ca\_cbmps\_min and lower than TSPX\_l2ca\_cbmps\_max, and the IUT chooses for transmitting an SDU size that, along with N, ensures that the IUT performs segmentation unless the IUT's max SDU size is the same as the MPS size.

## · Test Case Configuration

Table 4.46: Renegotiate MPS -Responder test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-25-C [Renegotiate MPS - Responder, LE] | 0x0005 |
| L2CAP/ECFC/BV-61-C [Renegotiate MPS - Responder, BR/EDR] | 0x0001 |

## · Test Procedure

Figure 4.205: Renegotiate MPS -Responder MSC

1. If the minimum supported MPS size equals TSPX\_l2ca\_cbmps\_max, the test ends with a Pass verdict.
2. If the MTU size equals MPS size, the test ends with a Pass verdict.
3. The Upper Tester commands the IUT to continuously transmits data packets (SDU size in Initial Condition) over the L2CAP channel at a minimum rate of 2 packets per second. Transmit at least 5 SDUs.
4. The IUT performs segmentation and transmit K-frames with payload equal to N ( Lower Tester's MPS).
5. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_REQ (Code = 0x19) packet to the IUT, with MPS = N + 1.
6. The IUT sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_RSP (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0000 (Reconfiguration successful).
7. The Upper Tester commands the IUT to transmit data packets (SDU size in Initial Condition) to the Lower Tester. Transmit at least 5 SDUs.
8. The IUT performs segmentation and transmit K-frames with payload equal to N+1 unless N+1 exceeds TSPX\_l2ca\_cbmps\_max from IXIT. If N = TSPX\_l2ca\_cbmps\_min, then the test ends with a Pass verdict.
9. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_REQ packet to the IUT, with MPS = N -1 bytes.
10. The IUT sends an L2CAP\_CREDIT\_BASED\_RECONFIGURE\_RSP packet to the Lower Tester, with the Result field equal to 0x0000 (Reconfiguration successful).
11. The Upper Tester commands the IUT to transmit data packets (SDU size in Initial Condition) to the Lower Tester. Transmit at least 5 SDUs.
12. The IUT performs segmentation and transmit K-frames with payload equal to N -1 unless N -1 is lower than TSPX\_l2ca\_cbmps\_min.
- Expected Outcome

## Pass verdict

For each of the Steps 3, 8, and 12, the IUT segments the SDUs to a length no greater than the previously negotiated MPS size and send correct frames to the Lower Tester.

## 4.9.1.20 Renegotiate MPS -MPS value is decreased

- Test Purpose

Verify that the IUT refuses the MPS reconfiguration request for multiple Data Channels created through Enhanced Credit Based Flow Control Mode, when receiving an L2CAP Credit Based Reconfigure Request with lower MPS value than the existing one for multiple channels and when receiving an L2CAP Credit Based Reconfigure Request with an MPS value between other existing MPS values for multiple channels.

- Reference

[15] 4.27

- Initial Condition
- -The TSPX\_l2ca\_cbmps\_min and TSPX\_l2ca\_cbmps\_max IXIT values give the minimum and maximum supported IUT MPS size.
- -The signaling channel specified in Table 4.47 is used.
- -An SPSM for the Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.

- Test Case Configuration
- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, with Destination CID containing the list of CIDs of the opened channels and with a lower MPS value (in octets) than what was negotiated in the channel ' s establishment. The lower MPS value must be at least 1 octet lower than the previous value.
2. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time). The IUT does not disconnect any of the channels requested in Step 1.
3. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, with Destination CID containing the list of CIDs of the opened channels and with an MPS value (in octets) that is between the minimum MPS value of the Destination CIDs and the maximum MPS value of the Destination CIDs that were negotiated for in each of the channels established.
4. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field set to any valid error code. The IUT does not disconnect any of the channels requested in Step 3.
- Expected Outcome

Table 4.47: Renegotiate MPS -MPS value is decreased test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BI-04-C [Renegotiate MPS - MPS value is decreased, LE] | 0x0005 |
| L2CAP/ECFC/BI-13-C [Renegotiate MPS - MPS value is decreased, BR/EDR] | 0x0001 |

Figure 4.206: Renegotiate MPS -MPS value is decreased MSC

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time).

In Step 4, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result set to any valid error code.

## 4.9.1.21 L2CAP Credit Based Connection Response -refused due to Invalid Parameters

- Test Purpose

Verify that an IUT does not establish any of the requested channels upon receiving an L2CAP Credit Based Connection Request containing a parameter with a value outside specifications and responds with result 0x000C ('All c onnections refused -invalid parameters ' ).

- Reference

[13] 4.26

- Initial Condition
- -The signaling channel specified in Table 4.48 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) with the SPSM declared via IXIT and an MTU value less than 64.
2. The IUT rejects the connection request sending an L2CAP Credit Based Connection Response (Code = 0x18) to the Lower Tester with Result 0x000C ('All c onnections refused -invalid parameters ' ).

Table 4.48: L2CAP Credit Based Connection Response -refused due to Invalid Parameters test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-26-C [L2CAP Credit Based Connection Response - refused due to Invalid Parameters, LE] | 0x0005 |
| L2CAP/ECFC/BV-62-C [L2CAP Credit Based Connection Response - refused due to Invalid Parameters, BR/EDR] | 0x0001 |

Figure 4.207: L2CAP Credit Based Connection Response -refused due to Invalid Parameters MSC

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x000C ('All c onnections refused -Invalid parameters ' ).

## 4.9.1.22 L2CAP Credit Based Connection Response -refused due to Unacceptable Parameters

- Test Purpose

Verify that an IUT does not establish any of the requested channels upon receiving an L2CAP Credit Based Connection Request containing a parameter with a value unacceptable for the Host and responds with result 0x000B ('All connections refused unacceptable parameters ' ).

- Reference

[13] 4.26

- Initial Condition
- -TSPX\_l2ca\_cbmtu\_min in the IXIT statement [3] is used to give the minimum peer MTU size that the IUT can accept on L2CAP Credit Based channels. The IXIT entry TSPX\_l2ca\_cbmtu\_min should not be set to 64 if the IUT can accept peer MTU size larger than 64 octets for Credit Based Connection Requests.
- -The signaling channel specified in Table 4.49 is used.
- -An SPSM for the Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- Test Case Configuration
- Test Procedure

Table 4.49: L2CAP Credit Based Connection Response -refused due to Unacceptable Parameters test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-27-C [L2CAP Credit Based Connection Response - refused due to Unacceptable Parameters, LE] | 0x0005 |
| L2CAP/ECFC/BV-63-C [L2CAP Credit Based Connection Response - refused due to Unacceptable Parameters, BR/EDR] | 0x0001 |

Figure 4.208: L2CAP Credit Based Connection Response -refused due to Unacceptable Parameters MSC

1. Perform alternative 1A or 1B depending on TSPX\_l2ca\_cbmtu\_min.

Alternative 1A (TSPX\_l2ca\_cbmtu\_min is greater than 64):

- 1A.1 The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) with the SPSM declared via IXIT and an MTU value lower than TSPX\_l2ca\_cbmtu\_min.
- 1A.2 The IUT rejects the connection request sending an L2CAP Credit Based Connection Response (Code = 0x18) to the Lower Tester with Result 0x000B ('All connections refused -unacceptable parameters ' ).

Alternative 1B (TSPX\_l2ca\_cbmtu\_min is 64):

- 1B.1 The Lower Tester sends an L2CAP Credit Based Connection Request (Code = 0x17) with the SPSM declared via IXIT and an MTU value equal to 64.
- 1B.2 The channel is successfully established.
- Expected Outcome

## Pass verdict

In Step 1A.2, the IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x000B ('All c onnections refused -unacceptable parameters ' ).

In Step 1B.2, the channel is successfully established. The IUT sends a correctly formatted L2CAP Credit Based Connection Response to the Lower Tester with result 0x0000 ('All connections successful').

## 4.9.1.23 Reconfigure -refused due to invalid Destination CID

- Test Purpose

Verify that the IUT refuses a reconfiguration request for a Data Channel created through Enhanced Credit Based Flow Control Mode, when receiving an L2CAP Credit Based Reconfigure Request with invalid Destination CID.

- Reference

[13] 4.27

- Initial Condition
- -The TSPX\_l2ca\_cbmps\_min and TSPX\_l2ca\_cbmps\_max IXIT values give the minimum and maximum supported IUT MPS size.
- -The signaling channel specified in Table 4.50 is used.
- -An SPSM for the Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- Test Case Configuration

Table 4.50: Reconfigure -refused due to invalid Destination CID test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BI-05-C [Reconfigure - refused due to invalid Destination CID, LE] | 0x0005 |
| L2CAP/ECFC/BI-14-C [Reconfigure - refused due to invalid Destination CID, BR/EDR] | 0x0001 |

- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, with Destination CID containing one invalid CID and with valid MPS.
2. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0003 (Reconfiguration failed -one or more Destination CIDs invalid).
- Expected Outcome

Figure 4.209: Reconfigure -refused due to invalid Destination CID MSC

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0003 (Reconfiguration failed -one or more Destination CIDs invalid).

## 4.9.1.24 Reconfigure -other unacceptable parameters

- Test Purpose

Verify that the IUT refuses the MPS reconfiguration request for a Data Channel created through Enhanced Credit Based Flow Control Mode, when receiving an L2CAP Credit Based Reconfigure Request with an unacceptable MPS value.

- Reference

[13] 4.28

- Initial Condition
- -The TSPX\_l2ca\_cbmps\_min IXIT value gives the minimum supported IUT MPS size.
- -The signaling channel specified in Table 4.51 is used.
- -An SPSM for the Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- Test Case Configuration

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BI-06-C [Reconfigure - other unacceptable parameters, LE] | 0x0005 |
| L2CAP/ECFC/BI-15-C [Reconfigure - other unacceptable parameters, BR/EDR] | 0x0001 |

Table 4.51: Reconfigure -other unacceptable parameters test cases

- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request packet to the IUT, for the opened channel, with MPS &lt; MPSMIN (minimum supported IUT MPS, as described in the IXIT).
2. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0004 ('Reconfiguration failed other unacceptable parameters').
- Expected Outcome

Figure 4.210: Reconfigure -other unacceptable parameters MSC

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0004 (Reconfiguration failed -other unacceptable parameters).

## 4.9.1.25 L2CAP Credit Based Connection Response -Duplicate DCID

- Test Purpose

Verify that an IUT receiving an L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP having a duplicate DCID detects the duplicate DCID and does not continue to use either the original channel or the new channel.

- Reference

[13] 4.26

- Initial Condition
- -The signaling channel specified in Table 4.52 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value. A Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value.
- Test Case Configuration

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BV-29-C [L2CAP Credit Based Connection Response - Duplicate DCID, LE] | 0x0005 |
| L2CAP/ECFC/BV-64-C [L2CAP Credit Based Connection Response - Duplicate DCID, BR/EDR] | 0x0001 |

Table 4.52: L2CAP Credit Based Connection Response -Duplicate DCID test cases

- Test Procedure
1. The Upper Tester commands the IUT to send a connection request on the SPSM declared via IXIT.
2. The IUT sends an L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ (Code = 0x17) to the Lower Tester.
3. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP (Code = 0x18) having a duplicate DCID to the IUT.
4. The IUT detects the duplicate Destination CID and does not continue to use the original channel or the new channel. If a mechanism is available, the Upper Tester attempts to send data over each channel to verify this.
- Expected Outcome

Figure 4.211: L2CAP Credit Based Connection Response -Duplicate DCID MSC

## Pass verdict

The IUT does not continue to use either the original channel or the new channel with the duplicate Destination CID.

## 4.9.1.26 Renegotiate MPS -MPS value is decreased, Multiple Channels

- Test Purpose

Verify that the IUT refuses the MPS reconfiguration request for multiple Data Channels created through Enhanced Credit Based Flow Control mode when receiving an L2CAP Credit Based Reconfigure Request with an MPS value between other existing MPU values for multiple channels.

- Reference

[15] 4.27

- Initial Condition
- -The signaling channel specified in Table 4.53 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.

- -A Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value, with the MPS on the Lower Tester side of at least 65 octets.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends an L2CAP Credit Based Reconfigure Request (Code = 0x19) packet to the IUT, with Destination CID containing the list of CIDs of the opened channels and with the MPS field value lower than the MPS value for one of the Destination CIDs that was negotiated during initial configuration.
2. The IUT does not disconnect the channel. The IUT sends an L2CAP Credit Based Reconfigure Response (Code = 0x1A) packet to the Lower Tester, with the Result field equal to 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time).
- Expected Outcome

Table 4.53: L2CAP Credit Based Connection Response -Duplicate DCID test cases

| Test Case ID | Signaling Channel |
| L2CAP/ECFC/BI-07-C [L2CAP Credit Based Connection Response - Duplicate DCID, LE] | 0x0005 |
| L2CAP/ECFC/BI-16-C [L2CAP Credit Based Connection Response - Duplicate DCID, BR/EDR] | 0x0001 |

Figure 4.212: Renegotiate MPS -MPS value is decreased, Multiple Channels MSC

## Pass verdict

In Step 2, the IUT sends a correctly formatted L2CAP Credit Based Reconfigure Response packet, with Result = 0x0002 (Reconfiguration failed - reduction in size of MPS not allowed for more than one channel at a time).

## 4.9.2 LE Credit Based Flow Control Mode

## L2CAP/LE/CFC/BV-01-C [LE Credit Based Connection Request - Legacy Peer]

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request to a legacy peer and receiving a Command Reject does not establish the channel.

- Reference

## 12 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An SPSM for the desired LE Credit Based Flow Control based Channel is declared via the TSPX\_spsm IXIT value.
- Test Procedure

Figure 4.213: L2CAP/LE/CFC/BV-01-C [LE Credit Based Connection Request - Legacy Peer] MSC

The IUT sends an LE Credit Based Connection Request on an SPSM indicated in the IXIT.

The Lower Tester responds with a Command Reject.

- Expected Outcome

## Pass verdict

After receiving the Command Reject from the Lower Tester, the IUT inform the Upper Tester.

## L2CAP/LE/CFC/BV-02-C [LE Credit Based Connection Request on Supported SPSM]

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request to a peer establishes the channel upon receiving the LE Credit Based Connection Response.

- Reference

[12] 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An SPSM for the desired LE Credit Based Flow Control based Channel is declared in the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to send credits.

Figure 4.214: L2CAP/LE/CFC/BV-02-C [LE Credit Based Connection Request on Supported SPSM] MSC

The IUT sends an LE Credit Based Connection Request on the SPSM declared in IXIT.

The Lower Tester responds with an LE Credit Based Connection response PDU.

(ALT1) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data on the established channel.

- Expected Outcome

## Pass verdict

The IUT receives the data send by the Lower Tester on the correct channel. The data is passed to the Upper Tester.

## L2CAP/LE/CFC/BV-03-C [LE Credit Based Connection Response on Supported SPSM]

- Test Purpose

Verify that an IUT receiving a valid LE Credit Based Connection Request from a peer sends an LE Credit Based Connection Response and establishes the channel.

- Reference

## 12 4.23

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An SPSM for the desired LE Credit Based Flow Control based channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to send data.

- Test Procedure

Figure 4.215: L2CAP/LE/CFC/BV-03-C [LE Credit Based Connection Response on Supported SPSM] MSC

The Lower Tester sends an LE Credit Based Connection Request with nonzero credits to the IUT on the SPSM specified in initial conditions.

The IUT responds with an LE Credit Based Connection Response.

The IUT is commanded to send data on the LE data channel by the Upper Tester.

- Expected Outcome

## Pass verdict

The IUT sends one or more correctly formatted K-frames on the correct channel to the Lower Tester.

The data sent by the IUT to the Lower Tester matches the data sent by the Upper Tester to the IUT.

## L2CAP/LE/CFC/BV-04-C [LE Credit Based Connection Request on an unsupported SPSM]

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request on an unsupported SPSM does not establish a channel upon receiving an LE Credit Based Connection Response refusing the connection.

- Reference

## 12 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An SPSM for an unsupported LE Credit Based Flow Control based channel is declared via the TSPX\_psm\_unsupported IXIT value.
- -The Upper Tester can command the IUT to create a connection.

Figure 4.216: L2CAP/LE/CFC/BV-04-C [LE Credit Based Connection Request on an unsupported SPSM] MSC

The IUT sends an LE Credit Based Connection Request PDU on the SPSM specified in the initial conditions which is not supported by the Lower Tester.

The Lower Tester responds with an LE Credit Based Connection Response with result '0x0002 Connection Refused -S PSM not supported'.

- Expected Outcome

## Pass verdict

The IUT receives an LE Credit Based Connection Response PDU with result '0x0002 Connection Refused -S PSM not supported' from the Lower Tester. This is indicated to the Upper Tester .

## L2CAP/LE/CFC/BV-05-C [LE Credit Based Connection Request - unsupported SPSM]

- Test Purpose

Verify that an IUT receiving an LE Credit Based Connection Request on an unsupported SPSM responds with an LE Credit Based Connection Response refusing the connection.

- Reference

[12] 4.23

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An SPSM for an unsupported LE Credit Based Flow Control based channel is declared via the TSPX\_spsm IXIT value.

Figure 4.217: L2CAP/LE/CFC/BV-05-C [LE Credit Based Connection Request - unsupported SPSM] MSC

The Lower Tester sends an LE Credit Based Connection Request on the SPSM specified in initial conditions.

- Expected Outcome

## Pass verdict

Upon receiving an LE Credit Based Connection Request containing an unsupported SPSM, the IUT sends a correctly formatted LE Credit Based Connection Response to the Lower Tester with Result '0x0002 Connection Refused -SPSM not supported.

## L2CAP/LE/CFC/BV-06-C [Credit Exchange -Receiving Incremental Credits]

- Test Purpose

Verify that the IUT handles flow control correctly, by handling the LE Flow Control Credit sent by the peer.

- Reference

[12] 4.24

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An LE Data Channel is established on an SPSM indicated in the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The initial credit on the LE Data Channel set by the Lower Tester is 0.
- -The Upper Tester can command the IUT to send data.

## · Test Procedure

Figure 4.218: L2CAP/LE/CFC/BV-06-C [Credit Exchange -Receiving Incremental Credits] MSC

1. The Upper Tester requests the IUT to send data packets to the Lower Tester.
2. The Lower Tester sends an LE Flow Control Credit Packet with Credit Value X to the IUT on the CID.
3. The IUT now sends K-frames containing data to the Lower Tester.
4. After receiving X K-frames from the IUT and ensuring that no more K-frames are received, the Lower Tester sends a new LE Flow Control Credit packet with a Credits value of X on the CID. The IUT sends X K-frames containing data to the Lower Tester.
5. The Test Procedure Steps 2 -4 are repeated with credit increment X ={1,&gt;1} without disconnecting the channel.
- Expected Outcome

## Pass verdict

After receiving X credits, the IUT sends X correctly formatted K-frames containing data to the Lower Tester.

The IUT stops sending K-frames to the Lower Tester after the credit count X reaches zero.

After receiving X credits, the IUT sends (X) correctly formatted K-frames containing data to the Lower Tester.

The IUT stops sending K-frames to the Lower Tester after the credit count X reaches zero.

## L2CAP/LE/CFC/BV-07-C [Credit Exchange -Sending Credits]

- Test Purpose

Verify that the IUT sends LE Flow Control Credit to the peer.

- Reference

## 12 4.24

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An LE Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The Upper Tester can command the IUT to send credits.
- Test Procedure

Figure 4.219: L2CAP/LE/CFC/BV-07-C [Credit Exchange -Sending Credits] MSC

(ALT1) If the channel was created with zero credits, the Upper Tester issues a command to the IUT to send credits.

The Lower Tester sends data packets to the IUT until it gets credits returned i.e., the data to send could consume more than the current credits available on the channel.

- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted LE Flow Control Credit packet to the Lower Tester minimum ones doing the data transfer.

## L2CAP/LE/CFC/BI-01-C [Credit Exchange -Exceed Initial Credits]

- Test Purpose

Verify that the IUT disconnects the LE Data Channel when the credit count exceeds 65535.

- Reference

[12] 4.24, 10.1

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An LE Data Channel is established on an SPSM indicated in the TSPX\_spsm IXIT value.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.
- -The initial credit on the LE Data Channel set by the Lower Tester is more than 1.
- Test Procedure

Figure 4.220: L2CAP/LE/CFC/BI-01-C [Credit Exchange -Exceed Initial Credits] MSC

(Optional) The IUT sends data packets to the Lower Tester.

The Lower Tester sends an LE Flow Control Credit PDU packet containing a credit so large that it together with the remaining credits on the IUT exceeds 65535.

- Expected Outcome

## Pass verdict

Upon receiving a credit overflow, the IUT disconnects the LE Data Channel.

## L2CAP/LE/CFC/BV-11-C [Security - Insufficient Authentication -Responder]

- Test Purpose

Verify that an IUT refuses to create a connection upon reception of an LE Credit Based Connection Request which fails to satisfy authentication requirements.

- Reference

[12] 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -An SPSM for the desired LE Credit Based Flow Control based Channel with authentication requirements is declared via the TSPX\_psm\_authentication\_required IXIT value.
- -No authentication procedure has been performed between the IUT and the Lower Tester.
- Test Procedure
1. The Lower Tester sends an LE Credit Based Connection Request on the SPSM specified in the initial conditions that requires authentication.
2. The IUT rejects the connection request with error code 'Insufficient Authentication' .
- Expected Outcome

Figure 4.221: L2CAP/LE/CFC/BV-11-C [Security - Insufficient Authentication -Responder] MSC

## Pass verdict

Upon reception of an LE Credit Based Connection Request from the Lower Tester which fails to satisfy the authentication requirements, the IUT sends a correctly formatted LE Credit Based Connection Response with Result '0x0005 Connection Refused -Insufficient Authe ntication' to the Lower Tester.

## L2CAP/LE/CFC/BV-14-C [Security - Insufficient Encryption Key Size -Initiator]

- Test Purpose

Verify that the IUT does not establish the channel upon receipt of an LE Credit Based Connection Response indicating the connection was refused with Result '0x0007 Connection Refused -Insufficient Encryption Key Size'.

- Reference

## 12 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -The Upper Tester can command the IUT to create a connection.
- -Either an Unauthenticated or Authenticated LTK exists between the IUT and Lower Tester.
- Test Procedure

Figure 4.222: L2CAP/LE/CFC/BV-14-C [Security - Insufficient Encryption Key Size -Initiator] MSC

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester refuses the Connection Request with result '0x0007 - Connection Refused Insufficient Encryption Key Size'.

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

## L2CAP/LE/CFC/BV-17-C [LE Credit Based Connection Response - refused due to insufficient resources - Responder]

- Test Purpose

Verify that an IUT receiving an LE Credit Based Connection Request for a second channel refuses the connection with result "0x0004 - Connection refused -no resources available" if it does not support multiple simultaneous channels.

- Reference

## 12 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -One LE Data channel is established on an SPSM declared via the TSPX\_spsm IXIT value.

Figure 4.223: L2CAP/LE/CFC/BV-17-C [LE Credit Based Connection Response - refused due to insufficient resources - Responder] MSC

The Lower Tester sends an LE Credit Based Connection Request on a different CID to than the first.

- Expected Outcome

## Pass verdict

Upon receiving an LE Credit Based Connection Request from the Lower Tester on a different CID than the previously-established channel, the IUT sends a correctly formatted LE Credit Based Connection Response to the Lower Tester with Result '0x0004 Connection Refused -no resources available'.

## L2CAP/LE/CFC/BV-18-C [LE Credit Based Connection Request - refused due to Invalid Source CID - Initiator]

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request does not establish the channel upon receiving an LE Credit Based Connection Response refusing the connection with result "0x0009 -Connection refused -Invalid Source CID".

- Reference

## 12 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -The Upper Tester can command the IUT to create a connection.

- Test Procedure

Figure 4.224: L2CAP/LE/CFC/BV-18-C [LE Credit Based Connection Request - refused due to Invalid Source CID - Initiator] MSC

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester Refuses the Connection Request with an LE Credit Based Connection Response with result '0x0009 Connection Refused -Invalid Source CID'.

The Upper Tester commands the IUT to send data on the refused CID.

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester the connection was refused.

The Lower Tester does not receive any data from the IUT on the refused CID.

## L2CAP/LE/CFC/BV-19-C [LE Credit Based Connection Request - refused due to source CID already allocated - Initiator]

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request does not establish the channel upon receiving an LE Credit Based Connection Response refusing the connection with result "0x000A -Connection refused -Source CID already allocated".

- Reference

[12] 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -The Upper Tester can command the IUT to create a connection.

- Test Procedure

Figure 4.225: L2CAP/LE/CFC/BV-19-C [LE Credit Based Connection Request - refused due to source CID already allocated - Initiator] MSC

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester Refuses the Connection Request with an LE Credit Based Connection Response with result '0x000A Connection Refused -Source CID already allocated'.

The Upper Tester commands the IUT to send data on the refused CID.

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester the connection was refused.

The Lower tester does not receive any data from the IUT on the refused CID.

## L2CAP/LE/CFC/BV-20-C [LE Credit Based Connection Response - refused due to Source CID already allocated - Responder]

- Test Purpose

Verify that an IUT receiving an LE Credit Based Connection Request for a second channel refuses the connection with result "0x000A - Connection refused -Source CID already allocated" if it receives a Source CID which is already in use.

- Reference

## 12 4.23

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -One LE Data channel is established on an SPSM declared via the TSPX\_spsm IXIT value.

- Test Procedure

Figure 4.226: L2CAP/LE/CFC/BV-20-C [LE Credit Based Connection Response - refused due to Source CID already allocated - Responder] MSC

The Lower Tester sends an LE Credit Based Connection Request using the same CID as the previously established channel.

- Expected Outcome

## Pass verdict

ALT1: Upon receipt of an LE Credit Based Connection Request using the same CID as the previously established channel, the IUT sends a correctly formatted LE Credit Based Connection Response to the Lower Tester with Result=0x000A - Connection Refused -Source CID already allocated.

ALT2: The IUT sends a correctly formatted Command Reject to the Lower Tester with Reason=0x0002 -Invalid CID in request.

## L2CAP/LE/CFC/BV-21-C [LE Credit Based Connection Request - refused due to Unacceptable Parameters - Initiator]

- Test Purpose

Verify that an IUT sending an LE Credit Based Connection Request does not establish the channel upon receiving an LE Credit Based Connection Response refusing the connection with result ' 0x000B -Connection refused -Unacceptable Parameters ' .

- Reference

## 12 4.22

- Initial Condition
- -The appropriate signaling channel for the transport is used.
- -The Upper Tester can command the IUT to create a connection.

- Test Procedure

Figure 4.227: L2CAP/LE/CFC/BV-21-C [LE Credit Based Connection Request - refused due to Unacceptable Parameters - Initiator] MSC

The Upper Tester commands the IUT to create a connection on an SPSM.

The Lower Tester refuses the Connection Request with an LE Credit Based Connection Response with result '0x000B Connection Refused -Unacceptable Parameters'.

The Upper Tester commands the IUT to send data on the refused CID.

- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester the connection was refused.

The Lower Tester does not receive any data from the IUT on the refused CID.

## 4.9.2.1 Credit Based Connection Request Dynamically Allocated Source CID

- Test Purpose

Verify that an IUT sending a Credit Based Connection Request to a peer allocates the Source CID from a dynamically allocated range and does not allocate one already in use.

- Reference

[12] 4.22

- Initial Condition
- -The signaling channel specified in Table 4.54 is used.
- -An SPSM for the desired LE Credit Based or Enhanced Credit Based Flow Control based Channel is declared in the TSPX\_spsm or the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to send credits.
- -A value for the number of concurrent Credit Based Connections is defined by the TSPX\_l2ca\_num\_concurrent\_credit\_based\_connections IXIT value.

- Test Case Configuration
- Test Procedure
1. Perform Steps 2 -6 a total of TSPX\_l2ca\_num\_concurrent\_credit\_based\_connections times.
2. The Upper Tester commands the IUT to create an L2CAP connection to the Lower Tester.
3. The IUT sends an L2CAP request command as specified in Table 4.54 to the Lower Tester on the SPSM as specified in Table 4.54 with a Source CID.
4. The Lower Tester confirms that the Source CID received in Step 3 is within the range 0x0040 -0x007F and is not the same as any of the Source CIDs received during this test procedure.
5. The Lower Tester sends an L2CAP response command as specified in Table 4.54 to the IUT with a Destination CID.

Table 4.54: Credit Based Connection Request Dynamically Allocated Source CID test cases

| Test Case ID | Signaling Channel | L2CAP Command |
| L2CAP/ECFC/BV-38-C [Credit Based Connection Request Dynamically Allocated Source CID - LE] | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ L2CAP_CREDIT_BASED_CONNECTION_RSP |
| L2CAP/LE/CFC/BV-29-C [Credit Based Connection Request Dynamically Allocated Source CID] | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ L2CAP_LE_CREDIT_BASED_CONNECTION_RSP |
| L2CAP/ECFC/BV-79-C [Credit Based Connection Request Dynamically Allocated Source CID - BR/EDR] | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ L2CAP_CREDIT_BASED_CONNECTION_RSP |

Figure 4.228: Credit Based Connection Request Dynamically Allocated Source CID MSC

6. The IUT notifies the Upper Tester that an L2CAP connection was completed with the Source CID from Step 3 and the Destination CID received in Step 5.
7. Repeat Steps 8 and 9 for all established channels.
8. The Lower Tester sends an L2CAP\_DISCONNECTION\_REQ PDU to the IUT with the Source CID and the Destination CIDs from Steps 2 -6.
9. The IUT sends an L2CAP\_DISCONNECTION\_RSP PDU to the Lower Tester with the Source CID and the Destination CIDs set as received in Step 8.
- Expected Outcome

## Pass verdict

In Step 3, the Source CID in the L2CAP request command is in the range of 0x40 -0x7F.

In each iteration of Step 3, the Source CID is not the same as any Source CID of an existing connection.

## 4.9.3 All Credit Based Flow Control Mode

## 4.9.3.1 Disconnection Request

## · Test Purpose

Verify that the IUT can disconnect the channel.

- Initial Condition
- -The signaling channel specified in Table 4.55 is used.
- -A Data Channel as specified in Table 4.55 is established on the SPSM declared via the TSPX\_spsm IXIT value using the commands specified in Table 4.55.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-08-C [Disconnection Request] | [12] 4.6 | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-08-C [Disconnection Request, LE] | [13] 4.6 | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-65-C [Disconnection Request, BR/EDR] | [13] 4.6 | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.55: Disconnection Request test cases

Figure 4.229: Disconnection Request MSC

1. The Upper Tester commands the IUT to disconnect the channel.
2. The IUT sends L2CAP Disconnection Request (Code = 0x06) to the Lower Tester.
3. The Lower Tester sends an L2CAP Disconnection Response (Code = 0x07).
- Expected Outcome

## Pass verdict

The IUT sends a correctly formatted L2CAP\_DISCONNECTION\_REQ to the Lower Tester.

## 4.9.3.2 Disconnection Response

- Test Purpose

Verify that the IUT responds correctly to reception of a Disconnection Request.

- Initial Condition
- -The signaling channel specified in Table 4.56 is used.
- -A Data Channel as specified in Table 4.56 is established on the SPSM declared via the TSPX\_spsm IXIT value using the commands specified in Table 4.56.
- -The role of the IUT is indicated in the TSPX\_iut\_role\_initiator IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-09-C [Disconnection Response] | [12] 4.7 | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-09-C [Disconnection Response, LE] | [13] 4.7 | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-66-C [Disconnection Response, BR/EDR] | [13] 4.7 | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.56: Disconnection Response test cases

## · Test Procedure

Figure 4.230: Disconnect Response MSC

1. The Lower Tester sends an L2CAP Disconnection Request (Code = 0x06) to the IUT.
2. The IUT sends an L2CAP Disconnection Response (Code = 0x07) to the Lower Tester.
- Expected Outcome

## Pass verdict

The IUT responds to the request to disconnect the channel with a correctly formatted L2CAP\_DISCONNECTION\_RSP.

## 4.9.3.3 Security -Insufficient Authentication -Initiator

- Test Purpose

Verify that the IUT does not establish any channel upon receipt of an L2CAP LE Credit Based Connection Response / L2CAP Credit Based Connection Response indicating the connections were refused with Result 0x0005 ('All c onnections refused -insufficient authentication ' ).

- Initial Condition
- -The signaling channel specified in Table 4.57 is used.
- -The Upper Tester can command the IUT to create a credit based channel on an SPSM declared via the TSPX\_psm\_authentication\_required IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | Signaling Commands | Result |
| L2CAP/LE/CFC/BV-10-C [Security - Insufficient Authentication - Initiator] | [12] 4.22 | 0x0005 | L2CAP LE Credit Based Connection Request (Code = 0x14) L2CAP LE Credit Based Connection Response (Code = 0x15) | 0x0005 - Connection refused - insufficient authentication |
| L2CAP/ECFC/BV-10-C [Security - Insufficient Authentication - Initiator, LE] | [13] 4.25 | 0x0005 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0005 - All connections refused - insufficient authentication |
| L2CAP/ECFC/BV-67-C [Security - Insufficient Authentication - Initiator, BR/EDR] | [13] 4.25 | 0x0001 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0005 - All connections refused - insufficient authentication |

Table 4.57: Security -Insufficient Authentication -Initiator test cases

## · Test Procedure

Figure 4.231: Security -Insufficient Authentication -Initiator MSC

1. The Upper Tester commands the IUT to send a connection request.
2. The IUT sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17), as in Table 4.57.
3. The Lower Tester sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0005, as in Table 4.57, refusing the channel creation request.
- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

## 4.9.3.4 Security -Insufficient Authorization -Initiator

## · Test Purpose

Verify that the IUT does not establish any channel upon receipt of an L2CAP LE Credit Based Connection Response / L2CAP Credit Based Connection Response indicating the connections were refused with Result 0x0006.

## · Initial Condition

- -The signaling channel specified in Table 4.58 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_psm\_authorization\_required IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_psm\_authorization\_required IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | Signaling Commands | Result |
| L2CAP/LE/CFC/BV-12-C [Security - Insufficient Authorization - Initiator] | [12] 4.22 | 0x0005 | L2CAP LE Credit Based Connection Request (Code = 0x14) L2CAP LE Credit Based Connection Response (Code = 0x15) | 0x0006 - Connection refused - insufficient authorization |
| L2CAP/ECFC/BV-12-C [Security - Insufficient Authorization - Initiator, LE] | [13] 4.25 | 0x0005 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0006 - All connections refused - insufficient authorization |
| L2CAP/ECFC/BV-68-C [Security - Insufficient Authorization - Initiator, BR/EDR] | [13] 4.25 | 0x0001 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0006 - All connections refused - insufficient authorization |

Table 4.58: Security -Insufficient Authorization -Initiator test cases

## · Test Procedure

Figure 4.232: Security -Insufficient Authorization -Initiator MSC

1. The Upper Tester commands the IUT to send a connection request.
2. The IUT sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17), as in Table 4.58.
3. The Lower Tester sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0006, as in Table 4.58, refusing the connection request.
- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

## 4.9.3.5 Security -Insufficient Authorization -Responder

## · Test Purpose

Verify that an IUT refuses to create any connection upon reception of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request which fails to satisfy authorization requirements.

## · Initial Condition

- -An LE ACL connection is established between the IUT and the Lower Tester.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_psm\_authorization\_required IXIT value.
- -An authorization requirement exists for the SPSM declared via the TSPX\_psm\_authorization\_required IXIT value.
- -No authorization procedure has been performed between the IUT and the Lower Tester.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Commands | Result |
| L2CAP/LE/CFC/BV-13-C [Security - Insufficient Authorization - Responder] | [12] 4.22 | L2CAP LE Credit Based Connection Request (Code = 0x14) L2CAP LE Credit Based Connection Response (Code = 0x15) | 0x0006 - Connection refused - insufficient authorization |
| L2CAP/ECFC/BV-13-C [Security - Insufficient Authorization - Responder, LE] | [13] 4.25 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0006 - All connections refused - insufficient authorization |

Table 4.59: Security -Insufficient Authorization -Responder test cases

- Test Procedure
1. The Lower Tester sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17).
2. The IUT detects the authorization requirement and sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18), rejecting the connection request with result 0x0006, as in Table 4.59.
- Expected Outcome

Figure 4.233: Security -Insufficient Authorization -Responder MSC

## Pass verdict

Upon reception of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request from the Lower Tester which fails to satisfy the authorization requirements, the IUT sends a correctly formatted L2CAP LE Credit Based Connection Response / L2CAP Credit Based Connection Response with Result 0x0006 to the Lower Tester.

## 4.9.3.6 Security -Insufficient Encryption Key Size -Responder

- Test Purpose

Verify that an IUT refuses to create any connection upon receipt of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request which fails to satisfy Encryption Key Size requirements.

- Initial Condition
- -The signaling channel specified in Table 4.60 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_psm\_encryption\_key\_size\_required IXIT value.
- -An encrypted link over the transport is established between the IUT and the Lower Tester. The minimum key size required for the SPSM is declared via the TSPX\_Min\_Encryption\_Key\_Length IXIT value. If it is greater than the minimum encryption key size defined by the specification, then the encryption key size used by the Lower Tester is less than the minimum encryption key size, otherwise the Lower Tester uses an encryption key size that is equal to the minimum encryption key size defined by the specification.
- -A preamble procedure defined in Section 4.4.2 is used to set up an encrypted link.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | Signaling Commands | Result |
| L2CAP/LE/CFC/BV-15-C [Security - Insufficient Encryption Key Size - Responder] | [12] 4.22 | 0x0005 | L2CAP LE Credit Based Connection Request (Code = 0x14) L2CAP LE Credit Based Connection Response (Code = 0x15) | 0x0007 - Connection refused - insufficient encryption key size |
| L2CAP/ECFC/BV-15-C [Security - Insufficient Encryption Key Size - Responder, LE] | [13] 4.25 | 0x0005 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0007 - All connections refused - insufficient encryption key size |
| L2CAP/ECFC/BV-70-C [Security - Insufficient Encryption Key Size - Responder, BR/EDR] | [13] 4.25 | 0x0001 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0007 - All connections refused - insufficient encryption key size |

Table 4.60: Security -Insufficient Encryption Key Size -Responder test cases

- Test Procedure
1. The Lower Tester sends an L2CAP LE Credit Based Connection Request (Code = 0x14) / L2CAP Credit Based Connection Request (Code = 0x17).
2. If the minimum encryption key size for the PSM is greater than the minimum encryption key size defined by the specification: ALT 1 is followed and the IUT detects the encryption key size too short for the requirement and sends an L2CAP LE Credit Based Connection Response (Code = 0x15) / L2CAP Credit Based Connection Response (Code = 0x18), rejecting the connection request with Result = 0x0007, as in Table 4.60. If the minimum encryption key size for the PSM is equal to the minimum encryption key size

Figure 4.234: Security -Insufficient Encryption Key Size -Responder MSC

defined by the specification: ALT 2 is followed, and the connection is successful.

- Expected Outcome

## Pass verdict

Upon reception of an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request from the Lower Tester which fails to satisfy the encryption key size requirements, the IUT sends a correctly formatted L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Response with Result 0x0007 to the Lower Tester.

If the minimum encryption key size for the PSM is equal to the minimum encryption key size defined by the specification, the request from the Lower Tester does not fail to satisfy the encryption key size requirement, and the connection is successful.

## 4.9.3.7 L2CAP Credit Based Connection Request -refused due to insufficient resources

- Test Purpose

Verify that an IUT sending an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Request does not establish some of the requested channels upon receiving an L2CAP LE Credit Based Connection Request / L2CAP Credit Based Connection Response refusing the connection with result 0x0004.

- Initial Condition
- -The signaling channel specified in Table 4.61 is used.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.
- -The Upper Tester can command the IUT to create a credit based channel on the SPSM declared via the TSPX\_spsm IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | Signaling Commands | Result |
| L2CAP/LE/CFC/BV-16-C [L2CAP LE Credit Based Connection Request - refused due to insufficient resources] | [12] 4.22 | 0x0005 | L2CAP LE Credit Based Connection Request (Code = 0x14) L2CAP LE Credit Based Connection Response (Code = 0x15) | 0x0004 - Connection refused - insufficient resources available |
| L2CAP/ECFC/BV-16-C [L2CAP Credit Based Connection Request - refused due to insufficient resources, LE] | [13] 4.25 | 0x0005 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0004 - Some connections refused - insufficient resources available |
| L2CAP/ECFC/BV-71-C [L2CAP Credit Based Connection Request - refused due to insufficient resources, BR/EDR] | [13] 4.25 | 0x0001 | L2CAP Credit Based Connection Request (Code = 0x17) L2CAP Credit Based Connection Response (Code = 0x18) | 0x0004 - Some connections refused - insufficient resources available |

Table 4.61: L2CAP Credit Based Connection Request -refused due to insufficient resources test cases

## · Test Procedure

Figure 4.235: L2CAP Credit Based Connection Request -refused due to insufficient resources MSC

1. The Upper Tester commands the IUT to send a connection request.
2. The Lower Tester sends an L2CAP LE Credit Based Connection Response (0x15) / L2CAP Credit Based Connection Response (Code = 0x18) with result 0x0004, as in Table 4.61, refusing the connection request.
3. (ALT1) If run over an Enhanced Credit Based Flow Control channel and the connection request was performed with more than one SCID and some of the channels were created, the Upper Tester commands the IUT to send data on the accepted CIDs.
- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

(ALT1) The data sent by the IUT in Step 3 must be the same as that received by the Lower Tester.

The IUT does not send any data to the Lower Tester on the refused CID(s).

## 4.9.3.8 L2CAP Credit Based Connection Response on Unsupported SPSM

## · Test Purpose

Verify that an IUT receiving L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ on an unsupported SPSM responds with L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP refusing the connection.

## · Initial Condition

- -The signaling channel specified in Table 4.62 is used.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | Result | L2CAP Command |
| L2CAP/LE/CFC/BV-22-C [L2CAP LE Credit Based Connection Response on Unsupported SPSM] | [13] 4.23 | 0x0005 | 0x0002 - Connection refused - SPSM not supported | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-28-C [L2CAP Credit Based Connection Response on Unsupported SPSM, LE] | [13] 4.26 | 0x0005 | 0x0002 - All connections refused - SPSM not supported | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-72-C [L2CAP Credit Based Connection Response on Unsupported SPSM, BR/EDR] | [13] 4.26 | 0x0001 | 0x0002 - All connections refused - SPSM not supported | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.62: L2CAP Credit Based Connection Response on Unsupported SPSM test cases

- Test Procedure

The L2CAP Credit Based Connection Request/Response commands are specified in Table 4.62.

Figure 4.236: L2CAP Credit Based Connection Response on Unsupported SPSM MSC

1. The Lower Tester sends a connection request command on an unsupported SPSM.
2. The IUT responds with a connection request response, with the Result in Table 4.62.
- Expected Outcome

## Pass verdict

Upon receiving a connection request command containing an unsupported SPSM, the IUT sends a correctly formatted connection request response to the Lower Tester with the Result in Table 4.62.

## 4.9.3.9 Disconnect Request -DCID not recognized or fixed channel

- Test Purpose

Verify that an IUT receiving Disconnect Request from the Lower Tester for which the DCID is not recognized by the IUT or is a fixed channel responds with L2CAP\_COMMAND\_REJECT\_RSP with an 'invalid CID' result code .

- Reference

[13] 4.1, 4.6

- Initial Condition
- -The signaling channel specified in Table 4.63 is used.
- -An LE or BR/EDR Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value using the commands specified in Table 4.63.

## · Test Case Configuration

| Test Case ID | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-23-C [Disconnect Request - DCID not recognized or fixed channel] | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-30-C [Disconnection Response - DCID not recognized or fixed channel, LE] | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-73-C [Disconnection Response - DCID not recognized or fixed channel, BR/EDR] | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.63: Disconnect Request -DCID not recognized or fixed channel test cases

- Test Procedure
1. The Lower Tester sends an L2CAP\_DISCONNECTION\_REQ (Code = 0x06) to the IUT on the PSM as specified in Table 4.63, with a DCID not recognized by the IUT.
2. The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP packet (Code = 0x01) to the Lower Tester, with Reason '0x0002 Invalid CID in request'.
3. The Lower Tester sends an L2CAP\_DISCONNECTION\_REQ (Code = 0x06) to the IUT on the PSM as specified in Table 4.63, with the CID set to the signaling channel being used.
4. The IUT sends an L2CAP\_COMMAND\_REJECT\_RSP packet (Code = 0x01) to the Lower Tester, with Reason '0x0002 Invalid CID in request'.
- Expected Outcome

Figure 4.237: Disconnect Request -DCID not recognized or fixed channel MSC

## Pass verdict

The IUT responds to the request to disconnect the channel with a correctly formatted L2CAP\_COMMAND\_REJECT\_RSP message.

## 4.9.3.10 Security -Insufficient Encryption -Initiator

- Test Purpose

Verify that the IUT does not establish any channel upon receipt of an L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP indicating that the connections were refused with Result 0x0008 ('All connections refused insufficient encryption').

- Initial Condition
- -The signaling channel specified in Table 4.64 is used.
- -Either an LTK or STK exists between the IUT and the Lower Tester, but encryption is not enabled.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_spsm IXIT value.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | Result | L2CAP Command |
| L2CAP/LE/CFC/BV-24-C [Security - Insufficient Encryption - Initiator] | [13] 4.22 | 0x0005 | 0x0008 ('Connection refused - insufficient encryption') | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-31-C [Security - Insufficient Encryption - Initiator, LE] | [13] 4.25 | 0x0005 | 0x0008 ('All connections refused - insufficient encryption') | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.64: Security -Insufficient Encryption -Initiator test cases

## · Test Procedure

The L2CAP Credit Based Connection Request/Response commands are specified in Table 4.64.

Figure 4.238: Security -Insufficient Encryption -Initiator MSC

1. The Upper Tester commands the IUT to send a connection request on an SPSM as specified in Table 4.64.
2. The IUT sends an L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ for the specified SPSM.
3. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP with Result 0x0008 (Table 4.64), refusing the channel creation request.
- Expected Outcome

## Pass verdict

The IUT informs the Upper Tester about the rejection.

## 4.9.3.11 Security -Insufficient Encryption -Responder

## · Test Purpose

Verify that an IUT refuses to create any connection upon reception of an L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ that fails to satisfy encryption requirements.

## · Initial Condition

- -The signaling channel specified in Table 4.65 is used.
- -Either an LTK or STK exists between the IUT and the Lower Tester, but encryption is not enabled.
- -An SPSM for the Enhanced Credit Based Flow Control channel is declared via the TSPX\_psm\_encryption\_required IXIT value.
- -Encryption requirement exists for the SPSM in use.

## · Test Case Configuration

| Test Case ID | Reference | Signaling Channel | Result | L2CAP Command |
| L2CAP/LE/CFC/BV-25-C [Security - Insufficient Encryption - Responder] | [13] 4.22 | 0x0005 | 0x0008 ('Connection refused - insufficient encryption') | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-32-C [Security - Insufficient Encryption - Responder, LE] | [13] 4.25 | 0x0005 | 0x0008 ('All connections refused - insufficient encryption') | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.65: Security -Insufficient Encryption -Responder test cases

- Test Procedure

The L2CAP Credit Based Connection Request/Response commands for the test are specified in Table 4.65.

Figure 4.239: Security -Insufficient Encryption -Responder MSC

1. The Lower Tester sends an L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ to the IUT for the specified SPSM.
2. The IUT sends an L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP to the Lower Tester with Result 0x0008 (Table 4.65), refusing the channel creation request.
- Expected Outcome

## Pass verdict

Upon reception of an L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ from the Lower Tester that fails to satisfy the authentication requirements, the IUT sends a correctly formatted L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP with Result 0x0008 (Table 4.65) to the Lower Tester.

## 4.9.3.12 K-frame -SDU length greater than MTU of IUT

- Test Purpose

Verify that an IUT receiving a Kframe from the Lower Tester with 'L2CAP SDU Length' field set to a value greater than the MTU of the IUT on L2CAP Credit Based Channel sends an L2CAP Disconnect Request for that channel.

- Reference

[13] 3.4.3

- Initial Condition
- -The signaling channel specified in Table 4.66 is used.
- -A Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value using the commands specified in Table 4.66.

## · Test Case Configuration

| Test Case ID | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-26-C [K-frame - SDU length greater than MTU of IUT] | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-33-C [K-frame - SDU length greater than MTU of IUT, LE] | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-76-C [K-frame - SDU length greater than MTU of IUT, BR/EDR] | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.66: K-frame - SDU length greater than MTU of IUT -test cases

Figure 4.240: K-frame - SDU length greater than MTU of IUT MSC

1. The Lower Tester sends a Kframe to the IUT with 'L2CAP SDU Length' field set to a value greater than the MTU of the IUT on L2CAP Credit Based Channel.
- Expected Outcome

## Pass verdict

The IUT terminates the channel and sends a correctly formatted L2CAP\_DISCONNECTION\_REQ PDU (Code = 0x06) to the Lower Tester.

## 4.9.3.13 K-frame -Information Payload length greater than MPS of IUT

- Test Purpose

Verify that an IUT receiving a Kframe from the Lower Tester with the length of 'Information Payload' field greater than the MPS of the IUT on L2CAP Credit Based Channel sends an L2CAP Disconnect Request for that channel.

- Reference

[13] 3.4.3

- Initial Condition
- -The signaling channel specified in Table 4.67 is used.
- -A Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value using the commands specified in Table 4.67.

## · Test Case Configuration

| Test Case ID | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-27-C [K-frame - Information Payload length greater than MPS of IUT] | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-34-C [K-frame - Information Payload length greater than MPS of IUT, LE] | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-77-C [K-frame - Information Payload length greater than MPS of IUT, BR/EDR] | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.67: K-frame -Information Payload length greater than MPS of IUT test cases

Figure 4.241: K-frame -Information Payload length greater than MPS of IUT MSC

1. The Lower Tester sends a Kframe to the IUT with the length of 'Information Payload' field greater than the MPS of the IUT on L2CAP Credit Based Channel.
- Expected Outcome

## Pass verdict

The IUT terminates the channel and sends a correctly formatted L2CAP\_DISCONNECTION\_REQ PDU (Code = 0x06) to the Lower Tester.

## 4.9.3.14 Total length of segments greater than SDU length specified in first K-frame

- Test Purpose

Verify that an IUT receiving segmented K-frames from the Lower Tester on L2CAP Credit Based Channel with total length of the segmented payloads greater than 'L2CAP SDU Length' field specified in the first K-frame sends an L2CAP Disconnect Request for that channel.

- Reference

[13] 3.4.3

- Initial Condition
- -The signaling channel specified in Table 4.68 is used.
- -A Data Channel is established on the SPSM declared via the TSPX\_spsm IXIT value.

## · Test Case Configuration

| Test Case ID | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-28-C [Total length of segments greater than SDU length specified in first K-frame] | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-35-C [Total length of segments greater than SDU length specified in first K-frame, LE] | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-78-C [Total length of segments greater than SDU length specified in first K-frame, BR/EDR] | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.68: Total length of segments greater than SDU length specified in first K-frame test cases

- Test Procedure

Same as for L2CAP/COS/CFC/BV-03-C [Reassembling], but in the last segment, the Lower Tester sends an Information Payload longer (at least one byte) than the correct size, such that the total length of segmented payloads is greater than 'L2CAP SDU Length' field specified in first K -frame.

- Expected Outcome

## Pass verdict

The IUT terminates the channel and sends a correctly formatted L2CAP\_DISCONNECTION\_REQ PDU (Code = 0x06) to the Lower Tester.

## 4.9.3.15 K-frame -SDU length = MPS

- Test Purpose

Verify that an IUT does not disconnect the peer when the payload size does not exceed the MPS. Verify that the IUT does not use the SDU Length 2 octets into calculating the payload size.

- Reference

[13] 3.4.3

- Initial Condition
- -The SPSM for the control channel is declared by the TSPX\_spsm IXIT value.

## · Test Case Configuration

| Test Case ID | Signaling Channel | L2CAP Command |
| L2CAP/LE/CFC/BV-32-C [K-frame - SDU length = MPS] | 0x0005 | L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-80-C [K-frame - SDU length = MPS, LE] | 0x0005 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |
| L2CAP/ECFC/BV-81-C [K-frame - SDU length = MPS, BR/EDR] | 0x0001 | L2CAP_CREDIT_BASED_CONNECTION_REQ/RSP |

Table 4.69: K-frame -SDU length = MPS test cases

## · Test Procedure

Figure 4.242: K-frame -SDU length = MPS MSC

1. The Upper Tester commands the IUT to create an L2CAP channel using the SPSM set to TSPX\_spsm.
2. The IUT sends the L2CAP command request specified in Table 4.69 to the Lower Tester on the SPSM from Step 1. The Lower Tester stores the MTU and MPS.
3. The Lower Tester sends the L2CAP command response specified in Table 4.69 to the IUT.
4. 4.
5. Perform alternative 4A or 4B depending on the MTU sent in Step 2:
6. ALT 4A: The MTU in Step 2 is greater than or equal to the MPS in Step 2 -1.
7. 4A.1 Repeat Step 4 for all rounds in Table 4.704.71.
8. 4A.2 The Lower Tester sends a Kframe to the IUT with the 'L2CAP SDU Length' field set to the value in Table 4.704.71 with a random payload.
9. ALT 4B: The MTU in Step 2 is less than the MPS in Step 2 -1:
10. 4B.1 The L2CAP channel is created using MTU less than MPS -1.
- Expected Outcome

Table 4.704.71: K-frame -SDU length = MPS rounds

| Round | SDU Length |
| 1 | MPS |
| 2 | MPS - 1 |
| 3 | MPS + 1 |
| 4 | MPS x 2 |
| 5 | MPS x 2 + 1 |
| 6 | MTU |

## Pass verdict

In Step 4, the IUT does not disconnect the channel created in Step 1.

## 4.10 Generic Attribute Timing tests

Check that the IUT respects the GATT timings.

## 4.10.1 Back-off on Connection Request Collision

- Test Purpose

Verify that an IUT in a Peripheral role that initiates an L2CAP connection request and encounters a collision uses an appropriate back-off timer before initiating a retry.

- Reference

[13] 4.3, 4.26

[14] 5.3.2, 5.4

- Initial Condition
- -The IUT acts in the Peripheral role.
- -For EATT, an encrypted ACL link between the IUT and the Lower Tester is established.
- -An L2CAP channel over the transport with the PSM/SPSM is set up as specified in Table 4.72.
- -For the tests in Table 4.72 that use EATT as the bearer, the following also apply:
- The Server Supported Features characteristic is present and states that it supports Enhanced ATT bearers, on both the IUT and Lower Tester sides.
- (TSPX\_iut\_supported\_max\_channels -1) LE or BR/EDR Data Channels are established on the EATT SPSM (the maximum number of EATT supported channels declared in the IXIT, minus 1).

## · Test Case Configuration

| Test Case | Transport | Code | PSM/ SPSM | Min Back-off |
| L2CAP/TIM/BV-01-C [Back-off on Connection Request Collision, BR/EDR, Dynamic] | BR/EDR | 0x02 | ATT | 100 ms |
| L2CAP/TIM/BV-02-C [Back-off on Connection Request Collision, BR/EDR, EATT] | BR/EDR | 0x17 | EATT | 100 ms |
| L2CAP/TIM/BV-03-C [Back-off on Connection Request Collision, LE, EATT] | LE | 0x17 | EATT | Max(100 ms, 2 × ( connPeripheralLatency + 1) × connInterval ) |

Table 4.72: Back-off on Connection Request Collision test cases

## · Test Procedure

Figure 4.243: Back-off on Connection Request Collision MSC

1. The Upper Tester commands the IUT to establish a connection to the Lower Tester.
2. The IUT sends an L2CAP Connection Request packet to the Lower Tester, in order to establish an L2CAP channel.
3. The Lower Tester sends an L2CAP Connection Request packet to the IUT (code as specified in Table 4.72).
4. The IUT sends the Lower Tester the response corresponding to the request sent in Step 3 with Result = 0x0004.
5. The Lower Tester sends the IUT the response corresponding to the request sent in Step 2 with Result = 0x0004.
6. The IUT waits for at least the time specified in Table 4.72. The Lower Tester does not send any packet during this time.
7. The IUT sends an L2CAP Connection Request packet to the Lower Tester, to establish an L2CAP channel.
8. The Lower Tester accepts the request, creates an L2CAP channel of the type described in Table 4.72, and responds with an L2CAP Connection Response packet with Result = 0x0000.

## · Expected Outcome

## Pass verdict

The IUT sends the L2CAP Connection Request to the Lower Tester, in Step 8, after at least the time listed in Table 4.72.

## Fail verdict

In Step 4, the IUT accepts the connection request from the Lower Tester and creates an L2CAP channel of the type described in Table 4.72.

- Note

The L2CAP packets exchanged between the IUT and the Lower Tester are of the type corresponding to the transport and bearer in Table 4.72 (L2CAP\_CONNECTION\_REQ / L2CAP\_CONNECTION\_RSP and, respectively, L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ / L2CAP\_CREDIT\_BASED\_CONNECTION\_RSP).

## 5 Test case mapping

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.

The columns for the TCMT are defined as follows:

Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for L2CAP [5].

If a test case is mandatory within the respective layer, then the y/x reference is omitted.

Feature: A brief, informal description of the feature being tested.

Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [10].

For the purpose and structure of the ICS/IXIT, refer to [10].

| Item | Feature | Test Case(s) |
| L2CAP 2/1 | Signaling channel | L2CAP/COS/CED/BV-07-C L2CAP/COS/CED/BV-08-C L2CAP/COS/CED/BV-09-C L2CAP/EXF/BV-08-C L2CAP/FIX/BV-03-C |
| L2CAP 2/1 AND CORE 2a/63 | Signaling channel, peer v4.1 or earlier | L2CAP/COS/CED/BI-30-C |
| L2CAP 2/1 AND L2CAP 2/41 | Reject Unknown Command - BR/EDR | L2CAP/COS/CED/BI-01-C |
| L2CAP 2/2 | Configuration process | L2CAP/COS/CFD/BV-01-C L2CAP/COS/CFD/BV-02-C L2CAP/COS/CFD/BV-03-C L2CAP/COS/CFD/BV-11-C L2CAP/COS/CFD/BV-12-C L2CAP/COS/CFD/BV-14-C |
| L2CAP 1/7 AND L2CAP 2/2 | Configuration process - Initiator | L2CAP/COS/CFD/BV-08-C |
| L2CAP 2/3 | Connection-oriented data channel | L2CAP/COS/CED/BV-03-C L2CAP/COS/CED/BI-04-C L2CAP/COS/CED/BI-06-C L2CAP/COS/CED/BI-07-C L2CAP/COS/CED/BI-08-C L2CAP/COS/CED/BI-10-C L2CAP/COS/CED/BI-12-C L2CAP/COS/CED/BI-14-C L2CAP/COS/CED/BI-15-C L2CAP/COS/CED/BI-28-C |

| Item | Feature | Test Case(s) |
| L2CAP 2/3 AND L2CAP 0a/1 | Connection-oriented data channel, BR/EDR | L2CAP/COS/CED/BI-03-C |
| L2CAP 2/45 | Send Disconnect Request | L2CAP/COS/CED/BV-04-C |
| L2CAP 2/4 | Command echo request | L2CAP/COS/ECH/BV-02-C |
| L2CAP 2/5 | Echo response | L2CAP/COS/ECH/BV-01-C |
| L2CAP 2/6 | Command information request | L2CAP/COS/IEX/BV-01-C |
| L2CAP 2/6 AND CORE 2a/63 | Command information request, peer v2.1or earlier | L2CAP/COS/IEX/BI-01-C |
| L2CAP 2/7 | Information response | L2CAP/COS/IEX/BV-02-C L2CAP/EXF/BV-07-C |
| L2CAP 2/9 | Connectionless data channel | L2CAP/CLS/CLR/BV-01-C |
| L2CAP 2/10 | Retransmission Mode | L2CAP/COS/CFD/BV-10-C L2CAP/COS/RTX/BV-01-C L2CAP/COS/RTX/BV-02-C L2CAP/COS/RTX/BV-03-C |
| L2CAP 2/11 | Flow Control Mode | L2CAP/COS/CED/BV-10-C L2CAP/COS/FLC/BV-01-C L2CAP/COS/FLC/BV-02-C L2CAP/COS/FLC/BV-03-C L2CAP/COS/FLC/BV-04-C L2CAP/COS/CFD/BV-13-C |
| L2CAP 2/12 | Enhanced Retransmission Mode | L2CAP/CMC/BV-01-C L2CAP/CMC/BV-02-C L2CAP/ERM/BV-01-C L2CAP/ERM/BV-02-C L2CAP/ERM/BV-03-C L2CAP/ERM/BV-08-C L2CAP/ERM/BV-09-C L2CAP/ERM/BV-10-C L2CAP/ERM/BV-11-C L2CAP/ERM/BV-12-C L2CAP/ERM/BV-18-C L2CAP/ERM/BV-19-C L2CAP/ERM/BV-20-C |
| L2CAP 2/13 | Streaming Mode | L2CAP/CMC/BV-04-C L2CAP/CMC/BV-05-C L2CAP/STM/BV-01-C L2CAP/STM/BV-02-C |
| L2CAP 2/13 AND L2CAP 2/33 AND L2CAP 2/44 | Streaming Mode, STM source over AMP | L2CAP/STM/BV-11-C |
| L2CAP 2/13 AND L2CAP 2/23 AND L2CAP 2/34 AND L2CAP 2/44 | Streaming Mode, Send data using SAR. STM sink over AMP | L2CAP/STM/BV-12-C |

| Item | Feature | Test Case(s) |
| L2CAP 2/13 AND L2CAP 2/23 AND L2CAP 2/33 AND L2CAP 2/44 | Streaming Mode, Send data using SAR. STM source over AMP | L2CAP/STM/BV-13-C |
| L2CAP 2/14a | Don't send FCS Option | L2CAP/FOC/BV-06-C L2CAP/FOC/BV-08-C |
| L2CAP 2/14b | Send FCS Option 0x00 | L2CAP/FOC/BV-01-C L2CAP/FOC/BV-02-C L2CAP/FOC/BV-03-C L2CAP/FOC/BV-05-C |
| L2CAP 2/14c | Send FCS Option 0x01 | L2CAP/FOC/BV-04-C L2CAP/FOC/BV-07-C |
| L2CAP 2/12 AND (L2CAP 2/14a OR L2CAP 2/14c) | ERTM with FCS Option, with FCS | L2CAP/OFS/BV-05-C L2CAP/OFS/BV-06-C |
| L2CAP 2/12 AND L2CAP 2/14b | ERTM with FCS Option, no FCS | L2CAP/OFS/BV-01-C L2CAP/OFS/BV-02-C |
| L2CAP 2/13 AND (L2CAP 2/14a OR L2CAP 2/14c) | Streaming with FCS Option, with FCS | L2CAP/OFS/BV-07-C L2CAP/OFS/BV-08-C |
| L2CAP 2/13 AND L2CAP 2/14b | ERTM with FCS Option, no FCS | L2CAP/OFS/BV-03-C L2CAP/OFS/BV-04-C |
| L2CAP 2/15 | Can Generate Local Busy Condition | L2CAP/ERM/BV-07-C L2CAP/ERM/BV-22-C |
| L2CAP 2/16 | Can Send Reject | L2CAP/ERM/BV-16-C L2CAP/ERM/BI-01-C |
| L2CAP 2/17 | Can Send Selective Reject | L2CAP/ERM/BV-17-C L2CAP/ERM/BI-02-C |
| L2CAP 2/18 | Supports mandatory use of ERTM | L2CAP/CMC/BI-01-C L2CAP/CMC/BI-02-C L2CAP/CMC/BV-12-C |
| L2CAP 2/19 | Supports mandatory use of Streaming Mode | L2CAP/CMC/BI-03-C L2CAP/CMC/BI-04-C L2CAP/CMC/BV-13-C |
| L2CAP 2/20 | Supports optional use of ERTM | L2CAP/CMC/BV-03-C L2CAP/CMC/BV-07-C L2CAP/CMC/BV-10-C |
| L2CAP 2/21 | Supports optional use of Streaming Mode | L2CAP/CMC/BV-06-C L2CAP/CMC/BV-08-C L2CAP/CMC/BV-11-C |
| L2CAP 2/22 | Can send data using SAR in ERTM | L2CAP/ERM/BV-23-C |
| L2CAP 2/23 | Can send data using SAR in Streaming Mode | L2CAP/STM/BV-03-C |
| L2CAP 2/24 | Can actively request Basic Mode for a PSM that supports the use of ERTM or Streaming Mode | L2CAP/CMC/BV-09-C L2CAP/CMC/BI-05-C L2CAP/CMC/BI-06-C |

| Item | Feature | Test Case(s) |
| L2CAP 2/25 | Supports performing L2CAP channel mode configuration fallback from STM to ERTM | L2CAP/CMC/BV-14-C L2CAP/CMC/BV-15-C |
| L2CAP 2/26 | Supports sending more than one unacknowledged I-frame when operating in ERTM | L2CAP/ERM/BV-05-C L2CAP/ERM/BV-06-C L2CAP/ERM/BV-13-C L2CAP/ERM/BI-03-C L2CAP/ERM/BI-04-C L2CAP/ERM/BI-05-C |
| L2CAP 2/27 | Supports sending more than three unacknowledged I-frames when operating in ERTM | L2CAP/ERM/BV-14-C L2CAP/ERM/BV-15-C |
| L2CAP 2/38 AND L2CAP 3/14 | Extended Flow Specification for ERTM over BR/EDR | L2CAP/LSC/BV-01-C L2CAP/LSC/BV-03-C L2CAP/LSC/BI-04-C |
| L2CAP 2/38 AND L2CAP 3/15 | Extended Flow Specification for STM over BR/EDR | L2CAP/LSC/BV-02-C L2CAP/LSC/BI-05-C L2CAP/LSC/BV-06-C |
| L2CAP 2/39 | Extended Window Size | L2CAP/EWC/BV-01-C L2CAP/EWC/BV-02-C L2CAP/EWC/BV-03-C |
| L2CAP 2/12 AND L2CAP 2/39 | ERTM, EWS and Extended Control Field | L2CAP/ECF/BV-01-C L2CAP/ECF/BV-02-C L2CAP/ECF/BV-03-C L2CAP/ECF/BV-04-C L2CAP/ECF/BV-05-C L2CAP/ECF/BV-06-C L2CAP/ECF/BV-07-C L2CAP/ECF/BV-08-C |
| L2CAP 3/3 AND L2CAP 1/7 | MTU size 48 bytes, Initiator | L2CAP/COS/CFD/BV-09-C L2CAP/COS/CED/BV-01-C |
| L2CAP 3/3 AND L2CAP 1/8 | MTU size 48 bytes, Acceptor | L2CAP/COS/CED/BV-12-C |
| L2CAP 3/4 | MTU size larger than 48 bytes | L2CAP/COS/CED/BV-11-C |
| L2CAP 2/40 | Reject Invalid Command Length, LE | L2CAP/COS/CED/BI-11-C |
| L2CAP 2/40 AND L2CAP 2/46 | Reject Invalid Command Length, LE Credit Based Flow Control Mode | L2CAP/COS/CED/BI-05-C L2CAP/COS/CED/BI-09-C L2CAP/COS/CED/BI-13-C L2CAP/COS/CED/BI-16-C L2CAP/COS/CED/BI-17-C L2CAP/COS/CED/BI-29-C |
| L2CAP 2/40 AND L2CAP 2/48b AND NOT L2CAP 2/46 | Reject Invalid Command Length, Enhanced Credit Based Flow Control Mode - LE | L2CAP/COS/CED/BI-18-C L2CAP/COS/CED/BI-20-C L2CAP/COS/CED/BI-22-C L2CAP/COS/CED/BI-24-C L2CAP/COS/CED/BI-25-C |

| Item | Feature | Test Case(s) |
| L2CAP 2/40 AND NOT (L2CAP 2/46 OR L2CAP 2/48b) | Reject Invalid Command Length, LE Credit Based Flow Control and Enhanced Credit Based Flow Control modes not supported - LE | L2CAP/COS/CED/BI-19-C L2CAP/COS/CED/BI-21-C L2CAP/COS/CED/BI-23-C |
| L2CAP 2/32 AND L2CAP 2/44 AND L2CAP 3/14 | ERTM over AMP with Extended Flow Specification - service type 'Best Effort' | L2CAP/LSC/BV-07-C L2CAP/LSC/BV-09-C L2CAP/LSC/BI-10-C |
| L2CAP 2/32 AND L2CAP 2/44 AND L2CAP 3/15 | ERTM over AMP with Extended Flow Specification - service type 'Guaranteed' | L2CAP/LSC/BI-11-C |
| L2CAP 2/33 AND L2CAP 2/34 AND L2CAP 2/44 AND L2CAP 3/15 | Streaming Mode over AMP with Extended Flow Specification - service type 'Guaranteed' | L2CAP/LSC/BV-08-C |
| L2CAP 2/33 AND L2CAP 2/44 AND L2CAP 3/15 | Streaming Mode over AMP with Extended Flow Specification - service type 'Guaranteed' | L2CAP/LSC/BV-12-C |
| L2CAP 2/30 | Fixed Channel Support | L2CAP/FIX/BV-01-C |
| L2CAP 2/30 AND L2CAP 2/31 | Fixed Channel and AMP Manager Support | L2CAP/FIX/BV-02-C |
| L2CAP 2/31 AND L2CAP 2/38 | AMP Manager and Extended Flow Specification Support | L2CAP/CCH/BV-01-C L2CAP/CCH/BV-02-C L2CAP/CCH/BV-03-C L2CAP/CCH/BV-04-C |
| L2CAP 2/32 | ERTM over AMP | L2CAP/MCH/BV-01-C L2CAP/MCH/BV-02-C L2CAP/MCH/BV-03-C L2CAP/MCH/BV-04-C L2CAP/MCH/BV-05-C L2CAP/MCH/BV-06-C L2CAP/MCH/BV-07-C L2CAP/MCH/BV-08-C L2CAP/MCH/BV-09-C L2CAP/MCH/BV-10-C L2CAP/MCH/BV-11-C L2CAP/MCH/BV-14-C |
| L2CAP 2/33 | Streaming Mode Source over AMP Support | L2CAP/MCH/BV-15-C L2CAP/MCH/BV-17-C L2CAP/MCH/BV-19-C L2CAP/MCH/BV-21-C L2CAP/MCH/BV-23-C L2CAP/MCH/BV-27-C L2CAP/MCH/BV-29-C L2CAP/MCH/BV-31-C L2CAP/MCH/BV-33-C L2CAP/MCH/BV-35-C |

| Item | Feature | Test Case(s) |
| L2CAP 2/34 | Streaming Mode Sink over AMP Support | L2CAP/MCH/BV-16-C L2CAP/MCH/BV-18-C L2CAP/MCH/BV-20-C L2CAP/MCH/BV-22-C L2CAP/MCH/BV-24-C L2CAP/MCH/BV-28-C L2CAP/MCH/BV-30-C L2CAP/MCH/BV-32-C L2CAP/MCH/BV-34-C L2CAP/MCH/BV-36-C |
| L2CAP 2/38 AND L2CAP 2/31 | | L2CAP/MCH/BV-12-C L2CAP/MCH/BV-13-C L2CAP/MCH/BV-25-C L2CAP/MCH/BV-26-C |
| L2CAP 2/35 | Unicast connectionless data reception | L2CAP/CLS/UCD/BV-01-C L2CAP/CLS/CID/BV-01-C |
| L2CAP 2/36 | Transmission of unencrypted unicast connectionless data | L2CAP/CLS/UCD/BV-02-C |
| L2CAP 2/37 | Transmission of encrypted unicast connectionless data | L2CAP/CLS/UCD/BV-03-C |
| L2CAP 2/42 | Support of Connection Parameter Update Request | L2CAP/LE/CPU/BV-01-C L2CAP/LE/CPU/BI-02-C |
| L2CAP 2/43 | Support of Connection parameter update Response | L2CAP/LE/CPU/BV-02-C L2CAP/LE/CPU/BI-01-C |
| L2CAP 1/7 AND L2CAP 2/46 | LE Credit Based Flow Control Channel Initiator | L2CAP/LE/CFC/BV-01-C L2CAP/LE/CFC/BV-02-C L2CAP/LE/CFC/BV-04-C L2CAP/LE/CFC/BV-16-C L2CAP/LE/CFC/BV-18-C L2CAP/LE/CFC/BV-21-C L2CAP/LE/CFC/BV-22-C L2CAP/LE/CFC/BV-24-C L2CAP/LE/CFC/BV-29-C |
| L2CAP 1/8 AND L2CAP 2/46 | LE Credit Based Flow Control Channel Responder | L2CAP/LE/CFC/BV-03-C L2CAP/LE/CFC/BV-05-C L2CAP/LE/CFC/BV-25-C L2CAP/LE/CFC/BV-30-C |
| L2CAP 2/40 AND L2CAP 2/41 | Reject Unknown Command - LE | L2CAP/LE/REJ/BI-02-C |
| L2CAP 1/7 AND L2CAP 2/46 AND L2CAP 4/1 | LE Credit Based Flow Control Channel Initiator with Authentication | L2CAP/LE/CFC/BV-10-C |
| L2CAP 1/7 AND L2CAP 2/46 AND L2CAP 4/2 | LE Credit Based Flow Control Channel Initiator with Authorization | L2CAP/LE/CFC/BV-12-C |

| Item | Feature | Test Case(s) |
| L2CAP 1/7 AND L2CAP 2/46 AND L2CAP 4/3 | LE Credit Based Flow Control Channel Initiator with Encryption | L2CAP/LE/CFC/BV-14-C |
| L2CAP 1/8 AND L2CAP 2/46 AND L2CAP 4/1 | LE Credit Based Flow Control Channel Responder with Authentication | L2CAP/LE/CFC/BV-11-C |
| L2CAP 1/8 AND L2CAP 2/46 AND L2CAP 4/2 | LE Credit Based Flow Control Channel Responder with Authorization | L2CAP/LE/CFC/BV-13-C |
| L2CAP 1/8 AND L2CAP 2/46 AND L2CAP 4/3 | LE Credit Based Flow Control Channel Responder with Encryption | L2CAP/LE/CFC/BV-15-C |
| L2CAP 2/46 | LE Credit Based Flow Control Channel - Data | L2CAP/COS/CFC/BV-01-C L2CAP/COS/CFC/BV-02-C L2CAP/COS/CFC/BV-03-C L2CAP/COS/CFC/BV-04-C L2CAP/LE/CFC/BV-06-C L2CAP/LE/CFC/BV-07-C L2CAP/LE/CFC/BI-01-C L2CAP/LE/CFC/BV-09-C L2CAP/LE/CFC/BV-23-C L2CAP/LE/CFC/BV-26-C L2CAP/LE/CFC/BV-27-C L2CAP/LE/CFC/BV-28-C L2CAP/LE/CFC/BV-31-C L2CAP/LE/CFC/BV-32-C |
| L2CAP 2/46 AND L2CAP 2/45a | LE Credit Based Flow Control Channel - Send Disconnect | L2CAP/LE/CFC/BV-08-C |
| L2CAP 1/8 AND NOT L2CAP 3/16 | Multiple Simultaneous LE Credit Based Flow Control Channels - Reject | L2CAP/LE/CFC/BV-17-C |
| L2CAP 3/16 | Multiple Simultaneous LE Credit Based Flow Control Channels | L2CAP/COS/CFC/BV-05-C |
| L2CAP 1/7 AND L2CAP 3/16 | Connection Request refused due to source CID already allocated - Initiator | L2CAP/LE/CFC/BV-19-C |
| L2CAP 1/8 AND L2CAP 3/16 | Connection Request refused due to source CID already allocated - Responder | L2CAP/LE/CFC/BV-20-C |
| L2CAP 1/7 AND L2CAP 2/48b | Enhanced Credit Based Flow Control Channel Initiator, LE | L2CAP/ECFC/BV-01-C L2CAP/ECFC/BV-02-C L2CAP/ECFC/BV-04-C L2CAP/ECFC/BV-16-C L2CAP/ECFC/BV-18-C L2CAP/ECFC/BV-19-C L2CAP/ECFC/BV-21-C L2CAP/ECFC/BV-22-C L2CAP/ECFC/BV-24-C L2CAP/ECFC/BV-28-C L2CAP/ECFC/BV-31-C L2CAP/ECFC/BV-38-C |

| Item | Feature | Test Case(s) |
| L2CAP 1/7 AND L2CAP 2/48a | Enhanced Credit Based Flow Control Channel Initiator, BR/EDR | L2CAP/ECFC/BV-45-C L2CAP/ECFC/BV-46-C L2CAP/ECFC/BV-48-C L2CAP/ECFC/BV-52-C L2CAP/ECFC/BV-54-C L2CAP/ECFC/BV-55-C L2CAP/ECFC/BV-57-C L2CAP/ECFC/BV-58-C L2CAP/ECFC/BV-60-C L2CAP/ECFC/BV-71-C L2CAP/ECFC/BV-72-C L2CAP/ECFC/BV-79-C |
| L2CAP 1/8 AND L2CAP 2/48b | Enhanced Credit Based Flow Control Channel Responder, LE | L2CAP/ECFC/BI-03-C L2CAP/ECFC/BI-04-C L2CAP/ECFC/BI-05-C L2CAP/ECFC/BI-06-C L2CAP/ECFC/BI-07-C L2CAP/ECFC/BV-03-C L2CAP/ECFC/BV-15-C L2CAP/ECFC/BV-17-C L2CAP/ECFC/BV-20-C L2CAP/ECFC/BV-23-C L2CAP/ECFC/BV-25-C L2CAP/ECFC/BV-26-C L2CAP/ECFC/BV-27-C L2CAP/ECFC/BV-29-C L2CAP/ECFC/BV-32-C |
| L2CAP 1/8 AND L2CAP 2/48a | Enhanced Credit Based Flow Control Channel Responder - BR/EDR | L2CAP/ECFC/BI-09-C L2CAP/ECFC/BV-40-C L2CAP/ECFC/BV-47-C L2CAP/ECFC/BV-53-C L2CAP/ECFC/BV-56-C L2CAP/ECFC/BV-59-C L2CAP/ECFC/BI-12-C L2CAP/ECFC/BV-61-C L2CAP/ECFC/BI-13-C L2CAP/ECFC/BV-62-C L2CAP/ECFC/BV-63-C L2CAP/ECFC/BI-14-C L2CAP/ECFC/BI-15-C L2CAP/ECFC/BV-64-C L2CAP/ECFC/BI-16-C L2CAP/ECFC/BV-70-C |
| L2CAP 1/7 AND L2CAP 2/48b AND L2CAP 4/1 | Enhanced Credit Based Flow Control Channel Initiator with Authentication, LE | L2CAP/ECFC/BV-10-C |

| Item | Feature | Test Case(s) |
| L2CAP 1/7 AND L2CAP 2/48a AND L2CAP 5/1 | Enhanced Credit Based Flow Control Channel Initiator with Authentication, BR/EDR | L2CAP/ECFC/BV-67-C |
| L2CAP 1/7 AND L2CAP 2/48b AND L2CAP 4/2 | Enhanced Credit Based Flow Control Channel Initiator with Authorization, LE | L2CAP/ECFC/BV-12-C |
| L2CAP 1/7 AND L2CAP 2/48a AND L2CAP 5/2 | Enhanced Credit Based Flow Control Channel Initiator with Authorization, BR/EDR | L2CAP/ECFC/BV-68-C |
| L2CAP 1/7 AND L2CAP 2/48b AND L2CAP 4/3 | Enhanced Credit Based Flow Control Channel Initiator with Encryption, LE | L2CAP/ECFC/BV-14-C |
| L2CAP 1/8 AND L2CAP 2/48b AND L2CAP 4/1 | Enhanced Credit Based Flow Control Channel Responder with Authentication, LE | L2CAP/ECFC/BV-11-C |
| L2CAP 1/8 AND L2CAP 2/48b AND L2CAP 4/2 | Enhanced Credit Based Flow Control Channel Responder with Authorization, LE | L2CAP/ECFC/BV-13-C |
| L2CAP 2/48b | Enhanced Credit Based Flow Control Channel - Data, LE | L2CAP/COS/ECFC/BV-01-C L2CAP/COS/ECFC/BV-02-C L2CAP/COS/ECFC/BV-03-C L2CAP/COS/ECFC/BV-04-C L2CAP/ECFC/BI-01-C L2CAP/ECFC/BI-02-C L2CAP/ECFC/BV-06-C L2CAP/ECFC/BV-07-C L2CAP/ECFC/BV-09-C L2CAP/ECFC/BV-30-C L2CAP/ECFC/BV-33-C L2CAP/ECFC/BV-34-C L2CAP/ECFC/BV-35-C L2CAP/ECFC/BV-41-C L2CAP/ECFC/BV-80-C |
| L2CAP 2/48a | Enhanced Credit Based Flow Control Channel - Data, BR/EDR | L2CAP/ECFC/BV-42-C L2CAP/ECFC/BV-49-C L2CAP/ECFC/BV-50-C L2CAP/ECFC/BI-10-C L2CAP/ECFC/BI-11-C L2CAP/ECFC/BV-66-C L2CAP/ECFC/BV-73-C L2CAP/ECFC/BV-76-C L2CAP/ECFC/BV-77-C L2CAP/ECFC/BV-78-C L2CAP/ECFC/BV-81-C L2CAP/COS/ECFC/BV-05-C L2CAP/COS/ECFC/BV-06-C L2CAP/COS/ECFC/BV-07-C L2CAP/COS/ECFC/BV-08-C |

| Item | Feature | Test Case(s) |
| L2CAP 2/48b AND L2CAP 2/45a | Enhanced Credit Based Flow Control Channel - Send Disconnect, LE | L2CAP/ECFC/BV-08-C |
| L2CAP 2/48a AND L2CAP 2/45 | Enhanced Credit Based Flow Control Channel - Send Disconnect, BR/EDR | L2CAP/ECFC/BV-65-C |
| (GAP 44/1 OR GAP 44/2 OR GAP 45/1 OR GAP 45/2) AND L2CAP 1/7 | Initiator - Simultaneous BR/EDR and LE Transports | L2CAP/LE/CID/BV-01-C |
| (GAP 44/1 OR GAP 44/2 OR GAP 45/1 OR GAP 45/2) AND L2CAP 1/8 | Acceptor - Simultaneous BR/EDR and LE Transports | L2CAP/LE/CID/BV-02-C |
| (GAP 44/1 OR GAP 44/2 OR GAP 45/1 OR GAP 45/2) AND L2CAP 2/48a AND L2CAP 2/48b | Initiator - Simultaneous BR/EDR and LE Transports - Enhanced Credit Based Flow Control Mode | L2CAP/LE/CID/BV-03-C L2CAP/LE/CID/BV-04-C |
| L2CAP 0a/1 | BR/EDR Invalid CID | L2CAP/COS/CID/BI-01-C |
| L2CAP 0a/2 | LE Invalid CID | L2CAP/LE/CID/BI-01-C |
| (GATT 1a/2 AND GATT 1a/4) AND L2CAP 1/7 AND L2CAP 1/8 | L2CAP Collision Mitigation, BR/EDR, ATT | L2CAP/TIM/BV-01-C |
| (GATT 1a/2 AND GATT 1a/4) AND L2CAP 1/7 AND L2CAP 1/8 AND L2CAP 2/48a AND GATT 2/3b | L2CAP Collision Mitigation, BR/EDR, EATT | L2CAP/TIM/BV-02-C |
| (GATT 1a/1 AND GATT 1a/3) AND L2CAP 1/7 AND L2CAP 1/8 AND L2CAP 2/48b AND GATT 2/3a | L2CAP Collision Mitigation, LE, EATT | L2CAP/TIM/BV-03-C |

Table 5.1 Test case mapping

## 6 Revision history and acknowledgments
