## Host Controller Interface (HCI)

## Bluetooth ® Test Suite

- Revision: HCI.TS.p39
- Revision Date: 2026-05-05

## 1 Scope

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth HCI layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers' Bluetooth devices.

## 2 References, definitions, and abbreviations

## 2.1 References

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [1] and [3].

- [1] Specification of the Bluetooth System, Volume 4 1 , Part E, Version 1.2 or later
- [2] Implementation Conformance Statement (ICS) for Host Controller Interface (HCI)
- [3] Test Strategy and Terminology Overview
- [4] Bluetooth Test Suite for Baseband, Version 1.2 or later
- [5] Bluetooth Test Suite for Link Manager, Version 1.2 or later
- [6] Bluetooth Test Suite for 802.11 PAL, Version 3.0 + HS or later
- [7] Bluetooth Test Suite for Link Layer, Version 4.0 or later
- [8] Specification of the Bluetooth System, Core Package, Volume 4 1 , Part E, Host Controller Interface (HCI), Version 4.2 or later
- [9] Specification of the Bluetooth System, Core Package, Volume 4 1 , Part E, Host Controller Interface (HCI), Version 5.0 or later
- [10] Erratum 10734: Pairing Updates
- [11] Specification of the Bluetooth System, Core Package, Volume 4 1 , Part E, Host Controller Interface (HCI), Version 5.1 or later
- [12] Specification of the Bluetooth System, Core Package, Volume 4 1 , Part E, Host Controller Interface (HCI), Version 5.2 or later
- [13] Specification of the Bluetooth System, Core Package, Volume 4 1 , Part E, Host Controller Interface (HCI), Version 5.3 or later
- [14] Bluetooth Test Suite for Link Layer, Version LL.TS.p18 or later
- [15] Bluetooth Test Suite for Link Layer, Version LL.TS.p17 or later
- [16] Appropriate Language Mapping Tables document
- [17] Specification of the Bluetooth System, Core Package, Volume 4, Part E, Host Controller Interface (HCI), Version 5.4 or later
- [18] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification), Version 6.0 or later
- [19] Specification of the Bluetooth System, Core Package, Volume 4, Part E, Host Controller Interface (HCI), Version 6.0 or later
- [20] Implementation Conformance Statement (ICS) for Link Layer (LL)

1 In versions 1.2 to 5.1, Volume 4, Part E was Volume 2, Part E.

- [21] Specification of the Bluetooth System, Core Package, Volume 2, Part C, Link Manager Protocol (LMP), Version 4.2 or later
- [22] Bluetooth Core Specification Volume 4, Part E, Host Controller Interface (HCI), Version 6.1 or later
- [23] Bluetooth Core Specification Volume 4, Part E, Host Controller Interface (HCI), Version 6.2 or later
- [24] Specification of the Bluetooth System, Volume 6, Part B (Link Layer Protocol Specification), Version 6.2 or later
- [25] Specification of the Bluetooth System, Core Package, Volume 4, Part E, Host Controller Interface (HCI), Version 6.3 or later

## 2.2 Definitions

In this Bluetooth document, the definitions from [1] and [3] apply.

Certain terms that were identified as inappropriate have been replaced. For a list of the original terms and their replacement terms, see the Appropriate Language Mapping Tables document [16].

## 2.3 Acronyms and abbreviations

In this Bluetooth document, the definitions, acronyms, and abbreviations from [1] and [3] apply.

## 3 Test Suite Structure (TSS)

## 3.1 Test Strategy

HCI is the interface between the upper and lower layers of the Bluetooth protocol stack.

The objective of HCI testing is to ensure interoperability and functionality between a Bluetooth Host and a Bluetooth Controller in order to enable qualification and combination of Controller and Host designs. The test cases cover mandatory and optional requirements in the protocol specification, matching these to the supported IUT features described in the Implementation Conformance Statement [2].

Conformance testing is the appropriate test method to meet this intent. The conformance test equipment provides a Lower and Upper Tester implementation.

HCI is being exercised extensively as the test controller (i.e., the Upper Tester) during the Link Layer and Link Manager conformance tests; many HCI commands and events are therefore implicitly proven already within these conformance tests.

HCI specifies the following groups of commands:

- Device Setup
- Controller Flow Control
- Controller Information
- Device Discovery
- Host Flow Control
- Authentication and Encryption
- Controller Configuration
- Controller Setup
- Connectionless Peripheral Broadcast
- LE Connection Management
- LE Power Control
- Isochronous Streams
- SCO and eSCO Connections

Figure 3.1 shows the HCI Test Suite Structure (TSS) including its subgroups defined for the conformance testing.

Figure 3.1: TSS for HCI

| Generic Events |
| Generic Events - Both Central and Peripheral |
| Device Setup |
| Device Setup - Both Central and Peripheral |
| Controller Flow Control |
| Controller Flow Control - Both Central and Peripheral |
| Controller Information |
| Controller Information - Both Central and Peripheral |
| Controller Configuration |
| Controller Configuration - Both Central and Peripheral |
| Device Discovery |
| Device Discovery - Both Central and Peripheral |
| Connection Setup |
| Connection Setup - Both Central and Peripheral |
| Host Flow Control |
| Host Flow control - Both Central and Peripheral |
| Authentication and Encryption |
| Authentication and encryption- Both Central and Peripheral |
| Connectionless Peripheral Broadcast |
| Connectionless Peripheral Broadcast - Both Central and Peripheral |
| Synchronization Train - Both Central and Peripheral |
| SCO and eSCO Connections - Both Central and Peripheral |
| LE Power Control - Both Central and Peripheral |
| Isochronous Streams |
| Broadcast Isochronous Streams |

## 3.2 Test groups

The test groups are organized in three levels. The first level defines the protocol groups representing the protocol services. The second level separates the protocol services in functional modules. The last level in each branch contains the standard ISO subgroups BV and BI.

## 3.2.1 Main test groups

The following test groups have been defined.

## 3.2.1.1 Generic Events

This generic events group covers the IUT response to commands not supported by the IUT or disallowed after receiving the first legacy or extended advertising command.

## 3.2.1.2 Device Setup

The device setup group of commands is used to place the Controller into a known state.

## 3.2.1.3 Controller Flow Control

The controller flow control group of commands and events are used to control data flow from the Host to the Controller.

## 3.2.1.4 Controller Information

The controller information group of commands allows the Host to discover local information about the device.

## 3.2.1.5 Device Discovery

The device discovery group of commands and events allows a device to discover other devices in the surrounding area. On LE this group of commands is also used to control advertising and scanning functionalities on the LL.

## 3.2.1.6 Host Flow Control

The Host flow control group of commands and events allows flow control to be used towards the Host.

## 3.2.1.7 Authentication and Encryption

The authentication and encryption group of commands and events allows authentication of a remote device and then encryption of the link to one or more remote devices.

## 3.2.1.8 Controller Configuration

The controller configuration group of commands and events allows the global configuration parameters to be configured.

## 3.2.1.9 Controller Setup

The controller setup group of commands and events are used to allow a device to make a connection to another device.

## 3.2.1.10 Connectionless Peripheral Broadcast

The Connectionless Peripheral Broadcast group of commands and events allows use of the CPB logical link to broadcast data to an unlimited number of recipients.

## 3.2.1.11 LE Power Control

The LE Power Control group of commands and events allows a device to query the controller's current and maximum transmit power levels.

## 3.2.1.12 Isochronous Streams

The Isochronous Streams group of commands and events allows use of Connected Isochronous Streams and Broadcast Isochronous Streams.

## 3.2.1.13 SCO and eSCO Connections

The SCO and eSCO Connections group of commands allow the creation, acceptance, and termination of SCO and eSCO Connections.

## 3.2.1.14 Event Versioning

The Event Versioning group of commands verifies that the controller sends the proper version of events that have multiple versions.

## 3.2.2 Behavior test groups

## 3.2.2.1 Valid Behavior (BV) tests

This subgroup provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt or exchange of valid HCI messages. Valid PDUs means that the exchange of messages and the content of the exchanged messages are considered as valid.

## 3.2.2.2 Invalid Behavior (BI) tests

This subgroup provides testing to verify that the IUT reacts in conformity with the Bluetooth standard, after receipt of a syntactically or semantically invalid HCI message.

## 3.3 HCI command and event version

If a command or event has more than one version and the test does not explicitly say otherwise:

- -A reference to a command specifying the version number means that that version or any highernumbered version supported by the IUT may be used.
- -A reference to an event specifying the version number means that that version or at least one higher-numbered version supported by the IUT is unmasked (other versions, including lowernumbered versions, may also be unmasked).
- -A reference to a command or event that does not specify the version number is equivalent to specifying [v1].

## 4 Test cases

## 4.1 Introduction

## 4.1.1 Test case identification conventions

Test cases are assigned unique identifiers per the conventions in [3]. The convention used here is:

&lt;spec abbreviation&gt;/&lt;IUT role&gt;/ &lt;class&gt;/ &lt;feat&gt; /&lt;func&gt;/&lt;subfunc&gt;/&lt;cap&gt;/ &lt;xx&gt;-&lt;nn&gt;-&lt;y&gt; .

Additional definitions and abbreviations can be found in [1].

Table 4.1: HCI TC feature naming conventions

| Identifier Abbreviation | Spec Identifier <spec abbreviation> |
| HCI | Host Controller Interface |
| Identifier Abbreviation | Feature Identifier <feat> |
| AEN | Authentication and Encryption |
| BIS | Broadcast Isochronous Stream |
| CCO | Controller Configuration |
| CFC | Controller Flow Control |
| CIN | Controller Information |
| CIS | Connected Isochronous Stream |
| CM | LE Connection Management |
| CPB | Connectionless Peripheral Broadcast |
| CSE | Controller Setup |
| DDI | Device Discovery |
| DSU | Device Setup |
| EVV | Event Versioning |
| GEV | Generic Events |
| HFC | Host Flow Control |
| PCL | LE Power Control |
| SCO | SCO and eSCO Connections |

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

## 4.1.3 Baseband assumptions

All test cases, except Connectionless Peripheral Broadcast, Synchronization Train, and Truncated Paging, are built upon having a Base Band Link up and running.

- The IUT and the Lower Tester must be in connection state (Active mode).
- DM1 packages must be used (Section 6.2 Preambles).
- All test cases are built upon a connection between two (2) devices, a Central and a Peripheral.

Connectionless Peripheral Broadcast and Synchronization Train cases are built upon having a Connectionless Peripheral Broadcast enabled.

Truncated Page testing assumes both devices are in Standby.

## 4.1.4 Role Switch

To force the IUT to become Central of the Piconet, Paging of the Lower Tester must be used as PDU LMP\_SWITCH\_REQ is optional and all IUTs will not support this (Section 6 Appendix MSC and Section 6.2 Preambles).

## 4.1.5 Default settings

The default settings must be carried out before each test case to guarantee a correct set up each time the tests are performed. Please see Section 6.2 Preambles for the set up messages used.

## 4.1.6 Applicable parameter values

The parameter values indicated in the test cases are thought to be reasonable. However, what is reasonable ultimately depends on the user scenario the IUT is intended for. In those cases where the Bluetooth System Specification does not require the implementation of a specific value, and the IUT cannot support the value indicated in a test case, it is allowed to test the IUT with another value. The selected value has to be given as IXIT information. When a value deviates from what is indicated in the test case, it is selected as close as possible to the value indicated in the test case. The selected value must not be such that the test purpose for the test case cannot be verified or the test case is not applicable. All test cases applicable as determined by the combination of Test Case Reference List, Implementation Conformance Statement and Test Case Mapping Table, must be executed successfully to complete the qualification of the IUT.

## 4.1.7 Pass/Inconclusive/Fail verdict conventions

Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met.

Certain test cases also have an Inconclusive verdict defined. If the conditions for this verdict are met, then the test provides evidence that the IUT neither meets nor violates the test case; instead, it means that the test case was not applicable to the IUT, and therefore a Pass verdict is not required in order to achieve Qualification of the IUT. Implementers are encouraged to provide mechanisms to avoid the behavior leading to an Inconclusive condition during testing.

The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict.

For an Inconclusive verdict, all the pass criteria conditions apply up to the point in the test procedure where an Inconclusive verdict is identified. If one of the pass criteria in a step prior to the Inconclusive verdict cannot be met, then the outcome of the test is the Fail verdict and not the Inconclusive verdict.

## 4.1.8 Notation conventions

The conventions in documenting events have varied over time, between different specification versions as well as their respective Test Suites. Due to this legacy, instances of "\_event", "\_Event", and " Event" may occur in this Test Suite ; all those should be understood to equate to 'event' as the settled convention applied in Bluetooth 5.1 and later specifications. It is intended to harmonize usage in this Test Suite over time.

## 4.2 Common Packet Contents

## 4.2.1 Fields and Bits Reserved for Future Use

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers.

## 4.3 Generic Events

Verify the correct implementation of the Generic Events.

## 4.3.1 HCI\_Command\_Status event alternatives

- Preamble Procedure

Alternative 1A (The IUT reports an error in the HCI\_Command\_Status event):

- 1A.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with the Status set to the appropriate error code.

Alternative 1B (The IUT reports an error in the procedure-specific event):

- 1B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with the Status set to 0x00.
- 1B.2 The IUT sends the appropriate HCI event with the appropriate error code.
- Notes

This alternative is not applicable in the following circumstances:

- -Any command that contains parameter values are out of range, unsupported, or inconsistent with another parameter must perform ALT 1A.
- -Any command that has sent or received a packet over the air must perform ALT 1B.

## HCI/GEV/BV-01-C [Unsupported Commands on each supported controller]

- Test Purpose

Verify that for each controller supported in the IUT, every HCI command not supported yields a Command Complete event with status 'Unknown HCI Command' in return.

- Reference

## 1 7.7.14

- Initial Condition
- -The IUT is not connected to the Lower Tester.
- Test Procedure

Repeat for each supported controller (1: BR/EDR Controller, 2: LE Controller, 3: AMP Controller) which has an unsupported HCI command.

The Upper Tester sends HCI commands not supported by the IUT and expects the IUT to return HCI\_Command\_Complete event or HCI\_Command\_Status event with Status = Unknown HCI Command.

Figure 4.1: HCI/GEV/BV-01-C [Unsupported Commands on each supported controller] MSC

- Expected Outcome

## Pass verdict

The IUT returns either an HCI\_Command\_Complete event with Status = Unknown HCI Command or an HCI\_Command\_Status event with Status = Unknown HCI Command.

- Notes

The test is run for all HCI commands indicated as not supported in the ICS. If all commands are supported on all supported controllers, then the test is not applicable.

Acceptable error codes for non-supported HCI Remote Name Request Cancel are: 0x01 or, alternately, 0x1F (Unspecified Error) or 0x0C (Command Disallowed).

## HCI/GEV/BV-02-C [Disallow Mixing Legacy and Extended Advertising Commands]

- Test Purpose

Verify that each supported legacy and extended advertising command yields a Command Complete event with status 'Command Disallowed' in return when sent after a command of the other type.

- Reference

[9] 3.19.1

- Test Procedure
1. The Upper Tester powers the IUT off and on or sends a reset.
2. The Upper Tester sends an LE Set Advertising Parameters command to the IUT and receives a Command Complete event with Status set to 0x00 (Success) in return.
3. For each command listed in Table 4.2, the Upper Tester sends the command and receives a Command Complete event with Status set as specified in Table 4.2 in return.

Figure 4.2: HCI/GEV/BV-02-C [Disallow Mixing Legacy and Extended Advertising Commands] MSC

| Round | Command (Step 3) | Command Complete Event |
| 1 | LE Set Extended Advertising Parameters | 0x0C (Command Disallowed) |
| 2 | LE Set Extended Advertising Data | 0x0C (Command Disallowed) |
| 3 | LE Set Extended Scan Response Data | 0x0C (Command Disallowed) |
| 4 | LE Set Extended Advertising Enable | 0x0C (Command Disallowed) |
| 5 | LE Read Maximum Advertising Data Length | 0x0C (Command Disallowed) |
| 6 | LE Read Number Of Supported Advertising Sets | 0x0C (Command Disallowed) |
| 7 | LE Remove Advertising Set | 0x0C (Command Disallowed) |
| 8 | LE Clear Advertising Sets | 0x0C (Command Disallowed) |

Table 4.2: Commands for each case variation

| Round | Command (Step 3) | Command Complete Event |
| 9 | LE Set Periodic Advertising Parameters | 0x0C (Command Disallowed) |
| 10 | LE Set Periodic Advertising Data | 0x0C (Command Disallowed) |
| 11 | LE Set Periodic Advertising Enable | 0x0C (Command Disallowed) |
| 12 | LE Set Periodic Advertising Sync Transfer Parameters | 0x0C (Command Disallowed) or 0x02 (Unknown Connection Identifier) |
| 13 | LE Set Default Periodic Advertising Sync Transfer Parameters | 0x0C (Command Disallowed) |

4. The Upper Tester powers the IUT off and on or sends a reset.
5. The Upper Tester sends an LE Set Extended Advertising Parameters command to the IUT and receives a Command Complete event with Status set to 0x00 (Success) in return.
6. For each command listed in Table 4.3, the Upper Tester sends the command and receives a Command Complete event with Status set to 0x0C (Command Disallowed) in return.
- Expected Outcome

Table 4.3: Commands for each case variation

| Round | Command (Step 6) |
| 1 | LE Set Advertising Parameters |
| 2 | LE Read Advertising Channel Tx Power |
| 3 | LE Set Advertising Data |
| 4 | LE Set Scan Response Data |
| 5 | LE Set Advertising Enable |

## Pass verdict

After receiving a legacy advertising command, the IUT returns an HCI\_Command\_Complete event with Status = Command Disallowed for any extended advertising command.

After receiving an extended advertising command, the IUT returns an HCI\_Command\_Complete event with Status = Command Disallowed for any legacy advertising command.

## HCI/GEV/BV-03-C [Disallow Mixing Legacy and Extended Scanning Commands]

- Test Purpose

Verify that each supported legacy and extended scanning command yields a Command Complete or Command Status event with status 'Command Disallowed' in return when sent after a command of the other type.

- Reference

[9] 3.19.1

- Test Procedure
1. The Upper Tester powers the IUT off and on or sends a reset.
2. The Upper Tester sends an LE Set Scan Parameters command to the IUT and receives a Command Complete event with Status set to 0x00 (Success) in return.
3. For each command listed in Table 4.4, the Upper Tester sends the command and receives a Command Complete or Command Status event with Status set to 0x0C (Command Disallowed) in return.

Figure 4.3: HCI/GEV/BV-03-C [Disallow Mixing Legacy and Extended Scanning Commands] MSC

| Round | Command (Step 3) | Associated Event |
| 1 | LE Set Extended Scan Parameters | HCI_Command_Complete event |
| 2 | LE Set Extended Scan Enable | HCI_Command_Complete event |
| 3 | LE Extended Create Connection | HCI_Command_Status event |
| 4 | LE Periodic Advertising Create Sync | HCI_Command_Status event |
| 5 | LE Periodic Advertising Create Sync Cancel | HCI_Command_Complete event |
| 6 | LE Periodic Advertising Terminate Sync | HCI_Command_Complete event |
| 7 | LE Add Device To Periodic Advertiser List | HCI_Command_Complete event |
| 8 | LE Remove Device From Periodic Advertiser List | HCI_Command_Complete event |
| 9 | LE Clear Periodic Advertiser List | HCI_Command_Complete event |
| 10 | LE Read Periodic Advertiser List Size | HCI_Command_Complete event |

Table 4.4: Commands for each case variation

4. The Upper Tester powers the IUT off and on or sends a reset.
5. The Upper Tester sends an LE Set Extended Scan Parameters command to the IUT and receives a Command Complete event with Status set to 0x00 (Success) in return.
6. For each command listed in Table 4.5, the Upper Tester sends the command and receives a Command Complete or Command Status event with Status set to 0x0C (Command Disallowed) in return.
- Expected Outcome

Table 4.5: Commands for each case variation

| Round | Command (Step 6) | Associated Event |
| 1 | LE Set Scan Parameters | HCI_Command_Complete event |
| 2 | LE Set Scan Enable | HCI_Command_Complete event |
| 3 | LE Create Connection | HCI_Command_Status event |

## Pass verdict

After receiving a legacy scanning command, the IUT returns an HCI Command Complete or Command Status event with Status = Command Disallowed for any extended scanning command.

After receiving an extended scanning command, the IUT returns an HCI Command Complete or Command Status event with Status = Command Disallowed for any legacy scanning command.

## HCI/GEV/BV-04-C [Extended Advertising Commands Without Scan Response Data]

- Test Purpose

Verify that the LE Extended Advertising Enable command yields a Command Complete event with status 'Command Disallowed' in return when no scan response data has been provided.

- Reference

[9] 7.8.55, 7.8.56

- Test Procedure
1. The Upper Tester powers the IUT off and on or sends a reset.
2. The Upper Tester sends an LE Set Extended Advertising Parameters command to the IUT with scannable advertising property bit set to 1 and receives a Command Complete event with Status set to 0x00 (Success) in return.
3. The Upper Tester sends an LE Set Extended Scan Response Data command to the IUT with no scan response data specified and receives a Command Complete event with Status set to 0x00 (Success) in return.
4. The Upper Tester sends an LE Set Extended Advertising Enable command to the IUT with no scan response data provided and receives a Command Complete event with Status set to 0x0C (Command Disallowed) in return.
- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event with Status set to 0x00 (Success) when the Upper Tester sends a HCI LE Set Extended Scan Response Data command with no scan response data.

The IUT returns an HCI\_Command\_Complete event with Status set to 0x0C (Command Disallowed) for HCI Set Extended Advertising Enable.

## HCI/GEV/BI-01-C [HCI Command with RFU OGF]

- Test Purpose

Verify that the IUT returns an Unknown HCI Command error when receiving an HCI command with an RFU (0x3E) OGF.

- Reference

[9] 5.4.1

- Test Procedure

Repeat Steps 1 and 2 for OCF values 0x000 to 0x00F, 0x3F0 to 0x3FF, and 20 random values between 0x010 and 0x3EF.

1. The Upper Tester sends an HCI command packet to the IUT with OGF set to 0x3E and OCF set as specified.
2. The IUT sends an HCI\_Command\_Complete event with Status set to Unknown HCI Command (0x01).
- Expected Outcome

## Pass verdict

In Step 2, the IUT returns an Unknown HCI Command error code.

## 4.4 Device Setup

Verify the correct implementation of the Device Setup commands.

## HCI/DSU/BV-01-C [BR/EDR Controller Reset Command]

- Test Purpose

Verify that the Reset command will reset the Controller, Link Manager, and the Bluetooth radio.

- Reference

[1] 7.3.2

- Initial Condition
- -See Section 4.1.3.

Figure 4.4: HCI/DSU/BV-01-C [BR/EDR Controller Reset Command] MSC

## · Expected Outcome

## Pass verdict

The IUT disconnects the ACL link after receiving an HCI\_Reset command.

The IUT returns the default page timeout.

## HCI/DSU/BV-02-C [Reset in Advertising State]

- Test Purpose

Verify that after receiving the HCI\_Reset the Bluetooth LE controller in advertiser state enters into Standby state.

- Reference

## 1 7.3.2

- Initial Condition
- -The IUT is configured in advertising state.
- Test Procedure

The Lower Tester receives ADV\_IND packets from the IUT.

The Upper Tester sends HCI Reset to the IUT and receives the HCI\_Command\_Complete event with Status = Success.

The Lower Tester receives no ADV\_IND packets from the IUT.

Figure 4.5: HCI/DSU/BV-02-C [Reset in Advertising State] MSC

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event with Status = Success.

The IUT stops sending ADV\_IND packets after reset command has been completed.

## HCI/DSU/BV-03-C [Reset to Peripheral]

- Test Purpose

Verify that after receiving the HCI\_Reset the Bluetooth LE controller in Peripheral role enters into Standby state. Verify that the link layer connection is lost.

## · Reference

## 1 7.3.2

- Initial Condition
- -LL connection established. The IUT is configured as Peripheral.

## · Test Procedure

The Lower Tester sends data to the IUT and receives data confirmation.

The Upper Tester sends HCI\_Reset to the IUT and receives the HCI\_Command\_Complete event with Status = Success.

The Lower Tester continues sending data packets and receives no packets from the IUT until connection timeout expires.

Figure 4.6: HCI/DSU/BV-03-C [Reset to Peripheral] MSC

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event with Status = Success.

The IUT stops sending data packets after reset command has been completed.

## HCI/DSU/BV-04-C [Reset in Scanning State]

- Test Purpose

Verify that after receiving the HCI\_Reset , the Bluetooth LE controller in scanning state IUT does not send any HCI LE Advertising Report Events.

- Reference

## 1 7.3.2

- Initial Condition
- -The IUT is configured in passive scanning state. The Lower Tester is in advertising state.
- Test Procedure

The Upper Tester receives HCI LE Advertising Report Event from the IUT.

The Upper Tester sends HCI Reset to the IUT and receives the HCI\_Command\_Complete event with Status = Success.

The Upper Tester receives no more HCI LE Advertising Report Events from the IUT.

Figure 4.7: HCI/DSU/BV-04-C [Reset in Scanning State] MSC

- Expected Outcome

## Pass verdict

The IUT returns HCI\_Command\_Complete event with Status = Success.

The IUT does not send HCI LE Advertising Report Event after reset.

## HCI/DSU/BV-05-C [Reset in Initiating State]

- Test Purpose

Verify that after receiving the HCI\_Reset the Bluetooth LE controller in initiating state enters into Standby state.

- Reference

## 1 7.3.2

- Initial Condition
- -The IUT is configured to be in initiating state. The Lower Tester is in idle state.
- Test Procedure

The Upper Tester sends HCI LE Create Connection to the IUT and receives HCI\_Command\_Status event with Status = Success.

The Upper Tester sends HCI Reset to the IUT and receives the HCI\_Command\_Complete event with Status = Success.

After the Upper Tester receives command complete for HCI Reset, the Lower Tester sends ADV\_IND packets and receives no CONNECT\_REQ packets from the IUT.

Figure 4.8: HCI/DSU/BV-05-C [Reset in Initiating State] MSC

- Expected Outcome

## Pass verdict

The IUT returns HCI\_Command\_Complete event with Status = Success.

The IUT does not send CONNECT\_REQ packet after Command\_Complete event of the Reset command.

The IUT does not return the HCI LE Connection Complete Event.

## HCI/DSU/BV-06-C [Reset to Central]

- Test Purpose

Verify that after receiving the HCI\_Reset the Bluetooth LE controller in Central role enters into Standby state. Verify that the link layer connection is lost.

- Reference

## 1 7.3.2

- Initial Condition
- -LL connection is established. The IUT is configured as Central.
- Test Procedure

The Lower Tester receives data packets from the IUT and sends confirmation.

The Upper Tester sends HCI Reset to the IUT and receives the HCI\_Command\_Complete event with Status = Success.

The Lower Tester receives no packets from the IUT until connection timeout expires.

Figure 4.9: HCI/DSU/BV-06-C [Reset to Central] MSC

- Expected Outcome

## Pass verdict

The IUT returns HCI\_Command\_Complete event with Status = Success.

The IUT stops sending data packets after reset command has been completed.

## HCI/DSU/BV-07-C [AMP Controller Reset Command]

- Test Purpose

Verify that the Reset Command will reset the HCI and the AMP PAL.

- Reference

## 1 7.3.2

- Initial Condition
- -See Section 4.1.3.

·

Figure 4.10: HCI/DSU/BV-07-C [AMP Controller Reset Command] MSC

- Expected Outcome

## Pass verdict

The IUT returns the default Logical Link Accept Timeout.

## 4.5 Controller Flow Control

Verify the correct implementation of the Controller Flow Control commands

## 4.5.1 Read Buffer Size Command

- Test Purpose

Verify that the Read\_Buffer\_Size command returns the buffer size, and that when data is transferred a 'number of completed packets' response is returned per packet.

- Reference

[13] 7.4.5

- Initial Condition
- -The IUT is in STANDBY Mode-3.
- Test Case Configuration
- Test Procedure

Table 4.6: Read Buffer Size Command test cases

| TCID | PHY | SCO or eSCO data over HCI support |
| HCI/CFC/BV-01-C | BR/EDR | Supported |
| HCI/CFC/BV-03-C | AMP | Supported |
| HCI/CFC/BV-06-C | BR/EDR | Not Supported |
| HCI/CFC/BV-07-C | AMP | Not Supported |

In the HCI ACL\_Data\_Packet, the N parameter is the data packet length returned in the HCI\_Read\_Buffer\_Size command.

An ACL connection is established using the PHY as specified in Table 4.6.

Figure 4.11: Read Buffer Size Command MSC

- Expected Outcome

## Pass verdict

The value of ACL\_Data\_Packet\_Length is greater than zero and less than the maximum ACL Data Packet size for a controller that supports BR/EDR in the returned HCI\_Command\_Complete event. If the controller supports SCO or eSCO over HCI as specified in Table 4.6, the value of Synchronous\_Data\_Packet\_Length is greater than zero and less than the maximum Synchronous Data Packet size.

The IUT returns one 'number of completed packets' response per packet for 1-byte packets.

The IUT returns one 'number of completed packets' response per packet for buffer -sized packets.

- Notes

All packets sent over HCI are valid L2CAP packets. In the first part of the test, the single byte data payload is encoded as an L2CAP packet with a 4-byte L2CAP header. For the second part of the test, for a buffer size N, the data payload is N-4 to allow for the L2CAP header.

## HCI/CFC/BV-02-C [Buffer Size]

- Test Purpose

Verify that the IUT returns the buffer size of the controller when receiving the LE\_Read\_Buffer\_Size command.

- Reference

[8] 7.8.2

- Initial Condition
- -No LL connection exists.
- Test Procedure

The Upper Tester sends HCI\_LE\_Read\_Buffer\_Size and receives an HCI\_Command\_Complete event in response with Status = Success.

In the HCI ACL\_Data\_Packet, the N parameter is the data packet length returned in the HCI\_LE\_Read\_Buffer\_Size command.

An ACL connection is established using the Bluetooth LE PHY.

Figure 4.12: HCI/CFC/BV-02-C [Buffer size] MSC

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event with Status = Success and Data\_Packet\_Length and Num\_Data\_Packet parameters with correct values.

The IUT returns one 'number of completed packets' response per packet for 1-data-byte packets.

The IUT returns one 'number of completed packets' response per packet for buffer -sized packets.

- Notes

All packets sent over HCI are valid L2CAP packets. In the first part of the test, the single byte data payload is encoded as an L2CAP packet with a 4-byte L2CAP header. For the second part of the test, for a buffer size N, the data payload is N-4 to allow for the L2CAP header.

## 4.5.2 Read Buffer Size and LE Read Buffer Size commands, Combined Data Buffers

- Test Purpose

Verify that the Read\_Buffer\_Size and LE\_Read\_Buffer\_Size commands on a device that has combined data buffers for both BR/EDR and LE return the proper buffer size on dual-mode devices, and that when data is transferred using both BR/EDR and LE connections, a 'number of completed packets' response is returned per packet.

- Reference

[13] 7.4.5, 7.8.2

- Initial Condition
- -The IUT is not connected to the Lower Tester.
- Test Case Configuration
- Test Procedure

Table 4.7: Read Buffer Size and LE Read Buffer Size commands, Combined Data Buffers

| TCID | SCO or eSCO data over HCI support |
| HCI/CFC/BV-04-C [Read Buffer Size and LE Read Buffer Size commands, Combined Data Buffers, SCO or eSCO data over HCI supported] | Supported |
| HCI/CFC/BV-08-C [Read Buffer Size and LE Read Buffer Size commands, Combined Data Buffers, SCO or eSCO data over HCI not supported] | Not Supported |

In the HCI ACL\_Data\_Packet, the N parameter is the data packet length returned in the HCI\_Read\_Buffer\_Size command.

Figure 4.13: Read Buffer Size and LE Read Buffer Size commands, Combined Data Buffers MSC

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event to the HCI\_Read\_Buffer\_Size command with Status = Success. The value of ACL\_Data\_Packet\_Length is greater than zero and less than the maximum ACL Data Packet size for a controller that supports BR/EDR. If the controller supports SCO or eSCO over HCI as specified in Table 4.7, the value of Synchronous\_Data\_Packet\_Length is greater than zero and less than the maximum Synchronous Data Packet size.

The IUT returns an HCI\_Command\_Complete event to the HCI\_LE\_Read\_Buffer\_Size command with Status = Success and LE\_Data\_Packet\_Length = 0 and Num\_LE\_Data\_Packets = 0.

The IUT returns one 'number of completed packets' response per packet for 1-byte packets on both BR/EDR and LE connections.

The IUT returns one 'number of completed packets' response per packet for buffer -sized packets on both BR/EDR and LE connections.

- Notes

All packets sent over HCI are valid L2CAP packets. In the first part of the test, the single byte data payload is encoded as an L2CAP packet with a 4-byte L2CAP header. For the second part of the test, for a buffer size N, the data payload is N-4 to allow for the L2CAP header.

## 4.5.3 Read Buffer Size and LE Read Buffer Size commands, Separate Data Buffers

- Test Purpose

Verify that the Read\_Buffer\_Size and LE\_Read\_Buffer\_Size commands that have separate data buffers for both BR/EDR and LE return the proper buffer size on dual-mode devices and that when data is transferred using both BR/EDR and LE connections, a 'number of completed packets' response is returned per packet.

- Reference

[13] 7.4.5, 7.8.2

- Initial Condition
- -The IUT is not connected to the Lower Tester.
- Test Case Configuration
- Test Procedure

Table 4.8: Read Buffer Size and LE Read Buffer Size commands, Separate Data Buffers

| TCID | SCO or eSCO data over HCI support |
| HCI/CFC/BV-05-C [Read Buffer Size and LE Read Buffer Size commands, Separate Data Buffers, SCO or eSCO data over HCI supported] | Supported |
| HCI/CFC/BV-09-C [Read Buffer Size and LE Read Buffer Size commands, Separate Data Buffers, SCO or eSCO data over HCI not supported] | Not Supported |

In the HCI ACL\_Data\_Packet, the N1 parameter is the data packet length returned in the HCI\_Read\_Buffer\_Size command, and the N2 parameter is the data packet length returned in the HCI\_LE\_Read\_Buffer\_Size command.

Figure 4.14: Read Buffer Size and LE Read Buffer Size commands, Separate Data Buffers MSC

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event to the HCI\_Read\_Buffer\_Size command with Status = Success. The value of ACL\_Data\_Packet\_Length is to be a non-zero value and less than the maximum ACL Data Packet size for a controller that supports BR/EDR. If the controller supports SCO or eSCO over HCI as specified in Table 4.8, the value of Synchronous\_Data\_Packet\_Length is to be a non-zero value and less than the maximum Synchronous Data Packet size.

The IUT returns an HCI\_Command\_Complete event to the HCI\_LE\_Read\_Buffer\_Size command with Status = Success and LE\_Data\_Packet\_Length and Num\_LE\_Data\_Packets with correct nonzero values.

The IUT returns one 'number of completed packets' response per packet for 1-byte packets on both BR/EDR and LE connections.

The IUT returns one 'number of completed packets' response per packet for buffer -sized packets on both BR/EDR and LE connections.

- Notes

All packets sent over HCI are valid L2CAP packets. In the first part of the test, the single-byte data payload is encoded as an L2CAP packet with a 4-byte L2CAP header. For the second part of the test, for a buffer size N, the data payload is N-4 to allow for the L2CAP header.

## 4.5.4 Read Buffer Size command, Invalid Parameters

- Test Purpose

Verify that the IUT properly responds to the HCI\_Read\_Buffer\_Size command, reporting a number of data packets that is consistent with the IUT ' s support or not for SCO or eSCO over HCI.

- Initial Condition
- -The IUT is in standby.
- Test Case Configuration
- Test Procedure
1. The Upper Tester sends the HCI\_Read\_Buffer\_Size command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0 and the parameters set as specified in Table 4.9.

Table 4.9: Read Buffer Size command, Invalid Parameters test cases

| Test Case | Reference | Event Parameter |
| HCI/CFC/BI-03-C [Read Buffer Size Command, [e]SCO data over HCI not supported] | [17] 7.4.5 | Total_Num_Synchronous_Data_Packets = 0 |
| HCI/CFC/BI-04-C [Read Buffer Size Command, [e]SCO data over HCI supported] | [17] 7.4.5 | Total_Num_Synchronous_Data_Packets > 0 Synchronous_Data_Packet_Length > 0 |

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with the parameters specified in Table 4.9.

## 4.6 Controller Information

Verify the correct implementation of the Controller Information commands.

## HCI/CIN/BV-01-C [Read Local Supported Features Command]

- Test Purpose

Verify that the Read Local Supported Features command returns with the correct features supported.

- Reference

[1] 7.4.3

- Initial Condition
- -No LL connection exists.
- Test Condition

Figure 4.15: HCI/CIN/BV-01-C [Read Local Supported Features Command] MSC

The manufacturer of the IUT must define features supported.

- Expected Outcome

## Pass verdict

The IUT returns parameter LMP\_Features containing features supported defined by the ICS as mapped by Table 3.2 in [21].

## HCI/CIN/BV-02-C [Read Local Extended Features Command]

- Test Purpose

Verify that the Read Local Extended Features command returns with the correct features supported.

- Reference

## 1 7.4.4

- Initial Condition
- -No LMP connection exists.
- Test Condition

Figure 4.16: HCI/CIN/BV-02-C [Read Local Extended Features Command] MSC

The manufacturer of the IUT must define the extended features supported.

- Expected Outcome

## Pass verdict

The IUT returns the requested page of extended LMP\_Features containing features supported defined by the ICS as mapped by Table 4.2 in [5].

Each HCI\_Command\_Complete event has the same Maximum Page Number.

## 4.6.1 Read Local Supported Commands command

- Test Purpose

Verify that the Read Local Supported Commands command returns with the correct commands supported.

- Reference

## 1 7.4.2

- Initial Condition
- -No LL connection exists.

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends the HCI command specified in Table 4.10 to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester with Supported\_Commands.
- Test Condition

Table 4.10: Read Local Supported Commands command test cases

| Test Case | HCI Command |
| HCI/CIN/BV-03-C [Read Local Supported Commands [v1] command] | HCI_Read_Local_Supported_Commands [v1] |
| HCI/CIN/BV-17-C [Read Local Supported Commands [v2] command] | HCI_Read_Local_Supported_Commands [v2] |

Figure 4.17: Read Local Supported Commands command MSC

The manufacturer of the IUT must define the commands supported.

The Supported\_Commands parameter matches those commands supported as mapped in the LE Command Tables in [2].

- Expected Outcome

## Pass verdict

The IUT returns the Supported\_Commands parameter with the correct commands supported as mapped in the LE Command Tables in [2]. The HCI [v1] command returns octets 0 -63 of Supported\_Commands. The HCI [v2] command returns octets 0 -250 of Supported\_Commands.

## HCI/CIN/BV-04-C [Read Local Version Information Command]

- Test Purpose

Verify that the Read Local Version Information command returns with the correct versions.

- Reference

[1] HCI 7.4.1

- Initial Condition
- -No LL connection exists.

- Test Procedure
- Test Condition

Figure 4.18: HCI/CIN/BV-04-C [Read Local Version Information Command] MSC

The manufacturer of the IUT must define versions supported.

- Expected Outcome

## Pass verdict

The IUT returns command complete with the version information containing HCI Version and LMP Version as defined in Bluetooth assigned numbers and HCI Revision, Manufacturer Name and LMP Subversion as defined by the manufacturer.

## HCI/CIN/BV-06-C [Filter Accept List Size]

- Test Purpose

Verify that the IUT responds with the number of empty entries that the radio has in its device addresses list.

- Reference

[8] 7.8.17

- Initial Condition
- -The IUT is not connected to the Lower Tester.
- Test Procedure

The Upper Tester sends HCI LE Clear Filter Accept List.

The Upper Tester reads the IUT ' s Filter Accept List size. The Upper Tester receives HCI\_Command\_Complete event with Filter Accept List Size parameter equal or greater than 1.

The Upper Tester adds different addresses until the list is full.

The Upper Tester adds one more address and expects the IUT to return an HCI\_Command\_Complete event with Status = Memory Capacity Exceeded.

The Upper Tester removes one address from the Filter Accept List so that there is now space for one more address.

The Upper Tester adds another address and expects the IUT to return an HCI\_Command\_Complete event with Status = Success.

Figure 4.19: HCI/CIN/BV-06-C [Filter Accept List Size] MSC

- Expected Outcome

## Pass verdict

The IUT returns HCI\_Command\_Complete event with Status = Success in response to HCI LE Read Filter Accept List Size command and with Filter Accept List Size parameter greater or equal to 0x01.

The IUT returns HCI Command Complete with Status = Success in response to HCI Add Device to Filter Accept List command while there is enough space in the list.

The IUT returns HCI Command Complete with Status = Memory Capacity Exceeded in response to HCI Add Device to Filter Accept List command while there is not enough space in the list.

The IUT returns HCI Command Complete with Status = Success in response to HCI Remove Device from Filter Accept List command.

The IUT returns HCI Command Complete with Status = Success in response to HCI Add Device to Filter Accept List command.

## HCI/CIN/BV-07-C [REMOVED TEST]

Test deleted. Section intentionally left blank.

## HCI/CIN/BV-08-C [Read Local Simple Pairing Options Command]

- Test Purpose

Verify that the Read Local Simple Pairing Options command returns with the correct options and key size supported.

- Reference

[10] 7.4.9

- Initial Condition
- -The IUT is not connected to the Lower Tester.
- Test Procedure
- Test Condition

Figure 4.20: HCI/CIN/BV-08-C [Read Local Simple Pairing Options Command] MSC

The manufacturer of the IUT supports remote public key validation performed and maximum encryption key size.

- Expected Outcome

## Pass verdict

The IUT has set the 'Remote public key validation is always performed' (bit 0) in the Simple Pairing Options Field to 1.

The IUT returns a Maximum Encryption Key Size greater than or equal to 0x07 and less than or equal to 0x10.

## HCI/CIN/BV-09-C [Read LE Public Key Validation Feature Bit]

- Test Purpose

Verify that the LE Read Local Supported Features Page 0 command returns with the Remote Public Key Validation feature bit enabled.

- Reference

[1] 7.4.3

- Initial Condition
- -The IUT is not connected to the Lower Tester.

- Test Procedure
- Expected Outcome

Figure 4.21: HCI/CIN/BV-09-C [Read LE Public Key Validation Feature Bit] MSC

## Pass verdict

The IUT returns a FeatureSet field with the Remote Public Key Validation bit set to 1.

## 4.6.2 Read Local Supported Codec Capabilities

- Test Purpose

Verify that the Read\_Local\_Supported\_Codecs command returns the correct codecs for the supported transport. For each supported codec, verify that the Read Local Supported Codec Capabilities returns the proper capabilities. Also verify that the proper min and max controller delay values are returned in the Read Local Supported Controller Delay.

- Reference

[12] 7.4.8

- Initial Condition
- -The IXIT parameters are specified in Table 4.11.

| IXIT Parameter | Description |
| TSPX_Number_Supported_Standard_Codecs_BR_EDR | Number of Standard Codecs, BR/EDR |
| TSPX_Number_Supported_Standard_Codecs_All_PHYs | Number of Standard Codecs, All PHYs |
| TSPX_Number_Supported_Vendor_Codecs_BR_EDR | Number of Vendor Specific Codecs, BR/EDR |
| TSPX_Number_Supported_Vendor_Codecs_All_PHYs | Number of Vendor Specific Codecs, All PHYs |

Table 4.11: Read Local Supported Codec Capabilities IXIT parameters

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends the HCI command as specified in Table 4.12 to the IUT.
2. The IUT responds with a successful HCI\_Command\_Complete event with return parameters as specified in Table 4.12.
3. The Upper Tester verifies that the IUT returns the Codec Parameters specified in Table 4.11 with Num\_Codec\_Capabilities entries. The Upper Tester also verifies that the number of array elements matches the number of supported codecs.
4. If the returned Num\_Supported\_Standard\_Codecs and Num\_Supported\_Vendor\_Specific\_Codecs both equal zero, the test ends with a Pass verdict.
5. For each standard codec and each vendor-specific codec returned in Step 2, perform Steps 6 -13.
6. For each transport supported for that codec as specified in the parameters returned in Step 2, perform Steps 7 -13.
7. For the two directions 0x00 and 0x01, perform Steps 8 -12.
8. The Upper Tester sends an HCI\_Read\_Local\_Supported\_Codec\_Capabilities command to the IUT with the appropriate Codec\_ID, Logical\_Transport\_Type, and Direction.
9. The IUT sends an HCI\_Command\_Complete event to the Upper Tester. If the status is zero, perform Steps 10 -12; otherwise, skip those steps.
10. For each codec capability returned in Step 9, perform Steps 11 and 12.
11. The Upper Tester sends an HCI\_Read\_Local\_Supported\_Controller\_Delay command to the IUT with Codec\_ID, Logical\_Transport\_Type, and Direction set to the values used in Step 8 and Codec\_Configuration\_Length and Codec\_Configuration set to the values selected in Step 10.
12. The IUT responds with a successful HCI\_Command\_Complete event with Min\_Controller\_Delay and Max\_Controller\_Delay set to a value between 0x000000 and 0x3D0900 and Max\_Controller\_Delay ≥ Min\_Controller\_Delay.
13. If for both directions the status in Step 9 is non-zero, the test ends with a Fail verdict.

Table 4.12: Read Local Supported Codec Capabilities test cases

| Test Case | HCI Command | Return Parameters | Execute Steps 4 - 13 |
| HCI/CIN/BV-10-C [Read Local Supported Codec Capabilities, BR/EDR] | HCI_Read_ Local_Supported_ Codecs [v1] | Num_Supported_Standard_Codecs = TSPX_Number_Supported_Standard_Codecs_BR_EDR Standard_Codec_ID[Num_Supported_Standard_Codecs] Num_Supported_Vendor_Specific_Codecs = TSPX_Number_Supported_Vendor_Codecs_BR_EDR Vendor_Specific_Codec_ID[Num_Supported_Vendor_ Specified_Codecs] | No |
| HCI/CIN/BV-11-C [Read Local Supported Codec Capabilities, All] | HCI_Read_ Local_Supported_ Codecs [v2] | Num_Supported_Standard_Codecs = TSPX_Number_Supported_Standard_Codecs_All_PHYs Standard_Codec_ID[Num_Supported_Standard_Codecs] Standard_Codec_Transport[Num_Supported_Standard_ Codecs] Num_Supported_Vendor_Specific_Codecs = TSPX_Number_Supported_Vendor_Codecs_All_PHYs Vendor_Specific_Codec_ID[Num_Supported_Vendor_ Specified_Codecs] Vendor_Specific_Codec_Transport[Num_Supported_ Vendor_Specified_Codecs] | Yes |

- Expected Outcome

## Pass verdict

In Step 2, the IUT responds with return parameters as specified in Table 4.12.

In Step 3, the IUT sends the correct number of Codec IDs and Codec Transports.

In Step 12, the IUT responds with return parameters with valid Min\_Controller\_Delay and Max\_Controller\_Delay values.

## Fail verdict

The status returned in Step 9 is non-zero for both directions for the same codec and transport.

## HCI/CIN/BV-12-C [LE Read Local Supported Features Page 0 Command]

- Test Purpose

Verify that the LE\_Read\_Local\_Supported\_Features\_Page\_0 command returns with the correct features supported.

- Reference

[1] 7.8.3

- Initial Condition
- -The IUT is not connected to the Lower Tester.
- Test Procedure

Figure 4.22: HCI/CIN/BV-12-C [LE Read Local Supported Features Page 0 Command] MSC

- Expected Outcome

## Pass verdict

The Features field in the HCI\_Command\_Complete event is set to a value containing all the features supported, matching those defined by the LL ICS as mapped by Table 2.1 in [20].

## HCI/CIN/BV-15-C [LE Read All Local Supported Features Command]

- Test Purpose

Verify that the LE\_Read\_All\_Local\_Supported\_Features command returns with the correct features supported.

- Reference

[1] 7.8.129

- Initial Condition
- -The IUT is not connected to the Lower Tester.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Read\_All\_Local\_Supported\_Features command to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester with Max\_Page and LE\_Features set.
- Expected Outcome

Figure 4.23: HCI/CIN/BV-15-C [LE Read All Local Supported Features Command] MSC

## Pass verdict

In Step 2, the LE\_Features field is set to a value matching the corresponding ICS entries as mapped by Table 2.1 in [20]. Max\_Page is set to the highest-numbered page with at least one bit set.

## 4.6.3 Read RSSI Value

- Test Purpose

Verify that the Read RSSI command returns a valid Received Signal Strength Indication value for a given connection.

- Reference

[12] 7.5.4

- Initial Condition
- -ACL connection established, the IUT is Central or Peripheral.
- Test Case Configuration

| Test Case ID | PHY |
| HCI/CIN/BV-13-C | BR/EDR |
| HCI/CIN/BV-14-C | LE PHY |

Table 4.13: Read RSSI Value test cases

- Test Procedure
1. The Upper Tester sends an HCI\_Read\_RSSI command to the IUT with Handle set to the value of the Connection\_Handle of the current connection.
2. The IUT sends a successful HCI Command\_Complete event to the Upper Tester with Handle set to the value of the Connection\_Handle in Step 1 and a valid RSSI value.
- Expected Outcome

Figure 4.24: Read RSSI Value MSC

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00, Handle set to the Connection\_Handle in Step 1, and a valid RSSI value.

## 4.7 Device Discovery

Verify the correct implementation of the Device Discovery commands.

## HCI/DDI/BV-01-C [Periodic Inquiry Mode Command]

- Test Purpose

Verify that the Periodic Inquiry Mode command configures the IUT to enter the Periodic Inquiry Mode, and that the Exit Periodic Inquiry Mode command configures the IUT to exit Periodic Inquiry Mode.

- Reference

[1] 7.1.3, 7.1.4

- Initial Condition
- -The IUT must be configured as Central.
- -The IUT is in STANDBY mode.

Figure 4.25: HCI/DDI/BV-01-C [Periodic Inquiry Mode Command] MSC

## · Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Periodic Inquiry Mode command.

The IUT returns an 'Inquiry Result' during each inquiry period.

The IUT returns an 'Inquiry Complete' event at the end of each inquiry period.

The IUT returns 'command complete' succeeded to the Exit Periodic Inquiry Mode command.

The IUT does not return an Inquiry Complete event after the periodic inquiry is exited.

## HCI/DDI/BV-02-C [Write Inquiry Mode Command]

- Test Purpose

Verify that the Write Inquiry Mode command writes the Inquiry Mode configuration parameter of the IUT, and that Read Inquiry Mode command returns the Inquiry Mode configuration parameter of the IUT.

- Reference

[1] 7.3.53, 7.3.54

- Initial Condition
- -The IUT must be configured as Central.
- -The IUT is in STANDBY mode.
- Expected Outcome

Figure 4.26: HCI/DDI/BV-02-C [Write Inquiry Mode Command] MSC

## Pass verdict

The IUT returns 'command complete' succeeded to the Write Inquiry Mode command.

The IUT returns the Inquiry\_Mode parameter with result 'Inquiry Result format with RSSI. The IUT returns an inquiry result with RSSI.

## HCI/DDI/BV-03-C [Set Advertising Enable]

- Test Purpose

Verify that the IUT stops advertising when receiving HCI LE SetAdvertising Enable with the parameter Advertising Enable set to Disabled.

- Reference

[8] 7.8.10

- Initial Condition
- -The IUT is configured in the advertising state.
- Test Procedure

The Lower Tester receives ADV\_IND packets from the IUT.

The Upper Tester sends HCI LE SetAdvertising Enable with parameter Advertising Enable set to Disabled to the IUT and receives the HCI\_Command\_Complete event with Status = Success.

The Lower Tester receives no ADV\_IND packets from the IUT.

Figure 4.27: HCI/DDI/BV-03-C [Set Advertising Enable] MSC

- Expected Outcome

## Pass verdict

The IUT returns HCI\_Command\_Complete event with Status = Success.

The IUT stops sending ADV\_IND packets.

## HCI/DDI/BV-04-C [Set Scan Enable]

- Test Purpose

Verify that the IUT stops scanning when receiving HCI LE SetScan Enable with the parameter LE Scan Enable set to Disabled.

- Reference

[8] 7.8.12

- Initial Condition
- -The IUT is configured as passive scanner. The Lower Tester is advertiser.
- Test Procedure

The Upper Tester receives HCI LE Advertising Report Event from the IUT.

The Upper Tester sends HCI LE SetScan Enable with LE Scan Enable parameter set to Disabled to the IUT and receives the HCI\_Command\_Complete event with Status = Success.

The Upper Tester receives no more HCI LE Advertising Report Events from the IUT.

Figure 4.28: HCI/DDI/BV-04-C [Set Scan Enable] MSC

- Expected Outcome

## Pass verdict

The IUT returns HCI\_Command\_Complete event with Status = Success.

The IUT does not send any more LE Advertising Report Events after it sends the HCI\_Command\_Complete for the HCI\_LE\_Set\_Scan\_Enable command that disables scanning.

## HCI/DDI/BV-05-C [Read Extended Inquiry Length]

- Test Purpose

Verify that the IUT correctly handles Read Extended Inquiry Length.

- Reference

[1] 7.3.98

- Initial Condition
- -The IUT is in standby.
- Test Procedure
1. The Upper Tester issues HCI\_Write\_Extended\_Inquiry\_Length Command with preset information to the IUT.
2. The Upper Tester receives success status in the HCI\_Write\_Extended\_Inquiry\_Length Command complete event.
3. The Upper Tester issues HCI\_Read\_Extended\_Inquiry\_Length Command to the IUT.
- Expected Outcome

## Pass verdict

The Upper Tester receives command complete event with success status for the commands sent in a and c. The Upper Tester receives the data returned by the HCI\_Read\_Extended\_Inquiry\_Length Command complete event. The received data matches that was used in the HCI\_Write\_Extended\_Inquiry\_Length Command.

## HCI/DDI/BI-01-C [Reject Invalid Extended Advertising Parameters]

- Test Purpose

Verify that the IUT properly rejects an invalid advertising interval provided to the HCI\_LE\_Set\_Extended\_Advertising\_Parameters command and returns the expected error code.

- Reference

[9] 7.8.53

- Initial Condition
- -The IUT is not currently advertising.
- -The minimum Primary\_Advertising\_Interval\_Min value (TSPX\_adv\_interval\_min) supported by the Controller is declared by the equipment manufacturer as an IXIT value.
- -The maximum Primary\_Advertising\_Interval\_Max value (TSPX\_adv\_interval\_max) supported by the Controller is declared by the equipment manufacturer as an IXIT value.
- -The legacy advertising type is defined by the TSPX\_legacy\_advertising\_event\_properties IXIT value.

- Test Procedure

The Upper Tester sends the HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with the Advertising\_Event\_Properties parameter set to TSPX\_legacy\_advertising\_event\_properties, the Primary\_Advertising\_Interval\_Max field set to TSPX\_adv\_interval\_min minus one, and Primary\_Advertising\_Interval\_Min set to TSPX\_adv\_interval\_min minus two.

If the TSPX\_adv\_interval\_max value is 0xFFFFFF, the test ends immediately with a Pass verdict. Otherwise, the Upper Tester sends the HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with the Advertising\_Event\_Properties parameter set to

TSPX\_legacy\_advertising\_event\_properties, the Primary\_Advertising\_Interval\_Min field set to TSPX\_adv\_interval\_max plus one, and Primary\_Advertising\_Interval\_Max set to

TSPX\_adv\_interval\_max plus one if TSPX\_adv\_interval\_max equals 0xFFFFFE, and plus two otherwise.

Figure 4.29: HCI/DDI/BI-01-C [Reject Invalid Extended Advertising Parameters] MSC

- Expected Outcome

## Pass verdict

HCI\_Command\_Complete event for HCI\_LE\_Set\_Extended\_Advertising\_Parameters is received by the Upper Tester.

- -If either Primary\_Advertising\_Interval\_Min or Max is less than 0x000020, the error code is either 0x11 (Unsupported Feature or Parameter Value) or 0x12 (Invalid HCI Command Parameter). Otherwise, the error code is 0x11.

## HCI/DDI/BI-02-C [Reject Invalid Advertising Parameters]

- Test Purpose

Verify that the IUT properly rejects an invalid advertising interval provided to the HCI\_LE\_Set\_Advertising\_Parameters command and returns the expected error code.

- Reference

[9] 7.8.5

- Initial Condition
- -The IUT is not currently advertising.
- -The minimum Advertising\_Interval\_Min value (TSPX\_adv\_interval\_min) supported by the Controller is declared by the equipment manufacturer as an IXIT value.
- -The maximum Advertising\_Interval\_Max value (TSPX\_adv\_interval\_max) supported by the Controller is declared by the equipment manufacturer as an IXIT value.
- Test Procedure

The Upper Tester sends the HCI\_LE\_Set\_Advertising\_Parameters to the IUT with the Advertising\_Type field set to 0x03 (ADV\_NONCONN\_IND), the Advertising\_Interval\_Max field set to TSPX\_adv\_interval\_min minus one, and Advertising\_Interval\_Min set to TSPX\_adv\_interval\_min minus two.

The Upper Tester sends the HCI\_LE\_Set\_Advertising\_Parameters to the IUT with the Advertising\_Type field set to 0x03 (ADV\_NONCONN\_IND), the Advertising\_Interval\_Max field set to TSPX\_adv\_interval\_max plus two, and Advertising\_Interval\_Max set to TSPX\_adv\_interval\_max plus one.

- Expected Outcome

## Pass verdict

- -HCI\_Command\_Complete event for HCI\_LE\_Set\_Advertising\_Parameters is received by the Upper Tester.
- -If either Advertising\_Interval\_Min or Advertising\_Interval\_Max or both are less than 0x0020 or greater than 0x4000, the error code is either 0x11 (Unsupported Feature or Parameter Value) or 0x12 (Invalid HCI Command Parameter). Otherwise, the error code is 0x11.

## HCI/DDI/BI-67-C [Reject Invalid Periodic Advertising Parameters]

- Test Purpose

Verify that the IUT properly rejects an invalid periodic advertising interval provided to the HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command and returns the expected error code.

- Reference

[9] 7.8.61

- Initial Condition
- -The IUT does not have periodic advertising enabled. An advertising set is configured with supported default values using the HCI\_LE\_Set\_Extended\_Advertising\_Parameters.
- -The minimum Periodic\_Advertising\_Interval\_Min value (TSPX\_periodic\_adv\_interval\_min) supported by the Controller is declared by the equipment manufacturer as an IXIT value.
- -The maximum Periodic\_Advertising\_Interval\_Max value (TSPX\_periodic\_adv\_interval\_max) supported by the Controller is declared by the equipment manufacturer as an IXIT value.
- Test Procedure

The Upper Tester sends the HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with Periodic\_Advertising\_Interval\_Max set to TSPX\_periodic\_adv\_interval\_min minus one, and Periodic\_Advertising\_interval\_Min set to TSPX\_periodic\_adv\_interval\_min minus two.

If the TSPX\_periodic\_adv\_interval\_max value is 0xFFFF, the test ends immediately with a Pass verdict. Otherwise, the Upper Tester sends the HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with Periodic\_Advertising\_Interval\_Min set to TSPX\_periodic\_adv\_interval\_max plus one, and Periodic\_Advertising\_interval\_Max set to TSPX\_periodic\_adv\_interval\_max plus one if TSPX\_periodic\_adv\_interval\_max equals 0xFFFE, and plus two otherwise.

Figure 4.30: HCI/DDI/BI-67-C [Reject Invalid Periodic Advertising Parameters] MSC

- Expected Outcome

## Pass verdict

The HCI\_Command\_Complete event for HCI\_LE\_Set\_Periodic\_Advertising\_Parameters is received by the Upper Tester.

If either Primary\_Advertising\_Interval\_Min or Max is less than 0x0006, the error code is either 0x11 (Unsupported Feature or Parameter Value) or 0x12 (Invalid HCI Command Parameter). Otherwise, the error code is 0x11.

## HCI/DDI/BI-03-C [Reject LE Periodic Advertising Create Sync Command With Disallowed Reporting Options]

- Test Purpose

Verify that the IUT properly rejects disallowed reporting options provided to the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command and returns the expected error code.

- Reference

## 11 7.8.67

- Initial Condition
- -The Lower Tester is advertising with extended advertising and periodic advertising.
- -The IUT is scanning for extended advertising and has received the Advertising SID, Advertiser Address Type, and Advertiser Address.
- Test Procedure

The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's periodic advertisements. Options is set to 0x02 (Don't Use List, Reporting Disabled).

Figure 4.31: HCI/DDI/BI-03-C [Reject LE Periodic Advertising Create Sync Command With Disallowed Reporting Options] MSC

- Expected Outcome

## Pass verdict

Alternative 1:

A Command Status event for the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command is received by the Upper Tester with the Connection Failed to be Established / Synchronization Timeout (0x3E) error code.

Alternative 2:

An LE Periodic Advertising Sync Established event is received by the Upper Tester with the Connection Failed to be Established / Synchronization Timeout (0x3E) error code.

## HCI/DDI/BI-04-C [Reject LE Periodic Advertising Create Sync Command to a Synchronized Advertising Set]

- Test Purpose

Verify that the IUT properly rejects setting a periodic advertising that the Controller is already synchronized to, to the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command and returns the expected error code.

- Reference

[12] 7.8.67

- Initial Condition
- -The Lower Tester is advertising with three periodic advertisements. All three have the same Advertising Address and Advertising Address Type. The first and third periodic advertisements have the same SID while the second has a different SID.
- -The IUT is scanning for extended advertising and is receiving SyncInfo for all three advertisements.

•

Test Procedure

Lower Tester

IUT

Upper Tester

HCI\_LE\_Periodic\_Advertising\_Create\_Sync

(First Periodic Advertisement Values,

Options bit 0: 0b0)

HCI\_Command\_Status

(Status: 0x00)

First Periodic Advertisement

Second Periodic Advertisement

Third Periodic Advertisement

HCI\_LE\_Periodic\_Advertising\_Sync\_Established

HCI\_LE\_Periodic\_Advertising\_Create\_Sync

(First Periodic Advertisement Values,

Options bit 0: 0b0)

HCI\_Command\_Status

(Status: 0x0B)

HCI\_LE\_Periodic\_Advertising\_Create\_Sync

(Second Periodic Advertisement Values,

Options bit 0: 0b0)

HCI\_Command\_Status

(Status: 0x00)

First Periodic Advertisement

Second Periodic Advertisement

Third Periodic Advertisement

HCI\_LE\_Periodic\_Advertising\_Sync\_Established

HCI\_LE\_Periodic\_Advertising\_Create\_Sync

(First Periodic Advertisement Values,

Options bit 0: 0b0)

HCI\_Command\_Status

(Status: 0x0B)

HCI\_LE\_Periodic\_Advertising\_Terminate\_Sync

(Sync\_Handle)

HCI\_Command\_Complete

(Status: 0x00)

HCI\_LE\_Periodic\_Advertising\_Create\_Sync

(First Periodic Advertisement Values,

Options bit 0: 0b0)

HCI\_Command\_Status

(Status: 0x00)

Second Periodic Advertisement

Third Periodic Advertisement

HCI\_LE\_Periodic\_Advertising\_Sync\_Established

Figure 4.32: HCI/DDI/BI-04-C [Reject LE Periodic Advertising Create Sync Command to a Synchronized Advertising Set] MSC

1. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's first periodic advertisement values and with bit 0 of the Options parameter set to 0.
2. An HCI\_Command\_Status event for the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command is received by the Upper Tester with a Success (0x00) error code.
3. The Upper Tester waits for the HCI\_LE\_Periodic\_Advertising\_Sync\_Established event.

4. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's first periodic advertisement values and with bit 0 of the Options parameter set to 0.
5. An HCI\_Command\_Status event for the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command is received by the Upper Tester with the Connection Already Exists (0x0B) error code.
6. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's second periodic advertisement values and with bit 0 of the Options parameter set to 0.
7. An HCI\_Command\_Status event for the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command is received by the Upper Tester with a Success (0x00) error code. An error code of Memory Capacity Exceeded (0x07) results in an Inconclusive verdict.
8. The Upper Tester waits for the HCI\_LE\_Periodic\_Advertising\_Sync\_Established event. An error code of Memory Capacity Exceeded (0x07) results in an Inconclusive verdict.
9. The Lower Tester stops the first periodic advertisement while continuing the other two periodic advertisements.
10. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's first periodic advertisement values and with bit 0 of the Options parameter set to 0.
11. An HCI\_Command\_Status event for the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command is received by the Upper Tester with the Connection Already Exists (0x0B) or Memory Capacity Exceeded (0x07) error code.
12. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Terminate\_Sync command to the IUT with the Sync\_Handle received in the HCI\_LE\_Periodic\_Advertising\_Sync\_Established event for the First Periodic Advertisement in Step 3.
13. An HCI\_Command\_Complete event for the HCI\_LE\_Periodic\_Advertising\_Terminate\_Sync command is received by the Upper Tester with a Success (0x00) error code.
14. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's first periodic advertisement values and with bit 0 of the Options parameter set to 0.
15. An HCI\_Command\_Status event for the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command is received by the Upper Tester with a Success (0x00) error code. An error code of Memory Capacity Exceeded (0x07) results in an Inconclusive verdict.
16. The Upper Tester waits for the HCI\_LE\_Periodic\_Advertising\_Sync\_Established event. An error code of Memory Capacity Exceeded (0x07) results in an Inconclusive verdict.
- Expected Outcome

## Pass verdict

The Upper Tester receives an HCI\_Command\_Status event with the expected status for each command.

The Upper Tester receives HCI\_LE\_Periodic\_Advertising\_Sync\_Established events as expected for each HCI\_LE\_Periodic\_Advertising\_Create\_Sync command that returned a status of success.

## Inconclusive verdict

In Steps 7, 8, 15, or 16, the Memory Capacity Exceeded (0x07) error is returned.

## HCI/DDI/BI-05-C [LE Set Extended Scan Parameters With Unsupported PHY]

- Test Purpose

Verify that the IUT properly rejects an HCI\_LE\_Set\_Extended\_Scan\_Parameters command that specifies unsupported PHYs.

- Reference

[9] 7.8.64

- Initial Condition
- -The IUT is not currently scanning.
- Test Procedure

For each bit on the Scanning\_PHYs parameter of the HCI\_LE\_Set\_Extended\_Scan\_Parameters command that is an RFU bit or corresponds to a PHY not supported by the IUT:

The Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Parameters command to the IUT with Scanning\_PHYs having only that bit set and receives an HCI\_Command\_Complete event with a nonzero status.

Figure 4.33: HCI/DDI/BI-05-C [LE Set Extended Scan Parameters With Unsupported PHY] MSC

- Expected Outcome

If the IUT supports PHYs corresponding to all 8 bits of the Scanning\_PHYs parameter, the test procedure will do nothing. This case is a Pass.

## Pass verdict

For each unsupported PHY (if applicable) and HCI\_LE\_Set\_Extended\_Scan\_Parameters command with an RFU bit set, a Command Complete event for HCI\_LE\_Set\_Extended\_Scan\_Parameters is received by the Upper Tester with the error Code Unsupported Feature or Parameter Value (0x11).

## 4.7.1 Reject Invalid Enable Command

- Test Purpose

Verify that the IUT properly rejects an enable command when the LE Random Device Address is unset, and returns the expected error code.

- Initial Condition
- -The IUT is in standby.
- -The IUT has not set its LE Random Device Address.
- Test Procedure
1. The Upper Tester sets the Own\_Address\_Type using the command and parameter in the 'HCI Set Command and Parameter' column in Table 4.14. Set all other fields to valid values.
2. The IUT returns an HCI\_Command\_Complete event with Success (0x00).
3. Upper Test sends the HCI Command under test from Table 4.14 with the 'Enable Parameter' set to 0x1 and with any other parameters set to valid values.
4. The IUT returns an HCI\_Command\_Complete event with the error code Invalid HCI Command Parameters (0x12).

Figure 4.34: Reject Invalid Enable Command MSC

| Test Case | HCI Set Command and Parameter | HCI Command and Parameter |
| HCI/DDI/BI-06-C [9] 7.8.9 | HCI_LE_Set_Advertising_Parameters (0x03) | HCI_LE_Set_Advertising_Enable (Advertising_Enable) |
| HCI/DDI/BI-07-C [9] 7.8.11 | HCI_LE_Set_Scan_Parameters (0x01 or 0x03) | HCI_LE_Set_Scan_Enable (LE_Scan_Enable) |
| HCI/DDI/BI-08-C [9] 7.8.56 | HCI_LE_Set_Extended_Advertising_Parameters (0x01) | HCI_LE_Set_Extended_Advertising_Enable (Enable) |
| HCI/DDI/BI-09-C [9] 7.8.56 | HCI_LE_Set_Extended_Advertising_Parameters (0x03) | HCI_LE_Set_Extended_Advertising_Enable (Enable) |
| HCI/DDI/BI-11-C [9] 7.8.65 | HCI_LE_Set_Extended_Scan_Parameters (0x01 or 0x03) | HCI_LE_Set_Extended_Scan_Enable (Enable) |

Table 4.14: Reject Invalid Enable Command test cases

- Expected Outcome

## Pass verdict

The IUT generates a Command Complete event for the HCI command under test with a status of Invalid HCI Command Parameters (0x12).

## HCI/DDI/BI-12-C [Reject Invalid Extended Advertising Enable Command]

- Test Purpose

Verify that the IUT properly rejects an HCI\_LE\_Set\_Extended\_Advertising\_Enable command when the IUT is not properly configured, and returns the expected error code.

- Reference

[9] 7.8.56

- Initial Condition
- -The IUT is in standby.
- -Extended advertising parameters with the scannable property set have been configured on the IUT for a particular advertising handle, but no scan response data has been set for that handle.
- Test Procedure
1. The Upper Tester sends the HCI\_LE\_Set\_Extended\_Advertising\_Enable command with the Enable parameter set to 0x01, the Advertising\_Handle set to existing Advertising\_Handle, Number\_Of\_Sets set to 0x01, and with all other parameters set to valid values.
2. The IUT returns an HCI\_Command\_Complete event with the error code Command Disallowed (0x0C).
3. The Upper Tester sends the HCI\_LE\_Set\_Extended\_Advertising\_Enable command with the Enable parameter set to 0x01, the Advertising\_Handle set to existing Advertising\_Handle, Number\_Of\_Sets set to 0x00, and with all other parameters set to valid values.
4. The IUT returns an HCI\_Command\_Complete event with the error code Invalid HCI Command Parameters (0x12).

Figure 4.35: HCI/DDI/BI-12-C [Reject Invalid Extended Advertising Enable Command] MSC

- Expected Outcome

## Pass verdict

The IUT generates a Command Complete event for each HCI\_LE\_Set\_Extended\_Advertising\_Enable command with the expected error code.

## HCI/DDI/BI-13-C [Reject Invalid Periodic Advertising Enable Command]

- Test Purpose

Verify that the IUT properly rejects an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command when the IUT is not properly set up, and returns the expected error code.

- Reference

[9] 7.8.63

- Initial Condition
- -The IUT is in standby.
- -Extended advertising parameters and periodic advertising parameters have been configured on the IUT for a particular advertising handle.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command with Operation parameter set to 0x01 and a non-zero Advertising\_Data\_Length.
2. The IUT returns an HCI\_Command\_Complete event with status set to 0x00.
3. The Upper Test sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable with the Enable parameter set to 0x01, the Advertising\_Handle set to the existing Advertising\_Handle.
4. The IUT returns an HCI\_Command\_Complete event with the error code Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

The IUT generates a Command Complete event for the HCI\_LE\_Set\_Periodic\_Advertising\_Enable command with the expected error code.

## HCI/DDI/BI-14-C [Reject LE Set Periodic Advertising Data setting the fragment when periodic advertising is enabled]

- Test Purpose

Verify that the IUT properly rejects the Upper Tester attempting to set the data fragment when periodic advertising is already enabled.

- Reference

[13] 7.8.62

- Initial Condition
- -The IUT is advertising with periodic advertisements.

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Operation set to the value specified in Table 4.15.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with the error code Command Disallowed (0x0C).
- Expected Outcome

Table 4.15: HCI/DDI/BI-14-C [Reject LE Set Periodic Advertising Data setting the fragment when periodic advertising is enabled] rounds

| Round | Operation |
| 1 | 0x00 |
| 2 | 0x01 |
| 3 | 0x02 |

## Pass verdict

In Step 2, the IUT returns an HCI\_Command\_Complete event with the Command Disallowed (0x0C) error code.

## 4.7.2 Reject Set Extended Advertising Parameters Command using a Periodic Advertising Set and Incompatible Advertising is Specified

- Test Purpose

Verify that the IUT properly rejects an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command when periodic advertising is enabled for the specified advertising set, and scannable, connectable, legacy, or anonymous advertising is specified.

- Reference

[12] 7.8.53

- Initial Condition
- -An advertising set exists and is no greater than 0x1F in length.
- Test Case Configuration

| Test Case | Specified Advertising Type | Advertising_Event_Properties |
| HCI/DDI/BI-15-C | Non-connectable non-scannable anonymous undirected | 0b00100000 |
| HCI/DDI/BI-16-C | Non-connectable non-scannable anonymous directed | 0b00100100 |
| HCI/DDI/BI-17-C | Legacy connectable and scannable undirected | 0b00010011 |
| HCI/DDI/BI-18-C | Legacy connectable directed (low duty cycle) | 0b00010101 |
| HCI/DDI/BI-19-C | Legacy connectable directed (high duty cycle) | 0b00011101 |
| HCI/DDI/BI-20-C | Legacy scannable undirected | 0b00010010 |

Table 4.16: Reject Set Extended Advertising Parameters Command using a Periodic Advertising Set and Incompatible Advertising is Specified test cases

| Test Case | Specified Advertising Type | Advertising_Event_Properties |
| HCI/DDI/BI-21-C | Legacy non-connectable and non- scannable, undirected | 0b00010000 |
| HCI/DDI/BI-22-C | Extended connectable undirected | 0b00000001 |
| HCI/DDI/BI-23-C | Extended connectable directed | 0b00000101 |
| HCI/DDI/BI-24-C | Extended scannable undirected | 0b00000010 |
| HCI/DDI/BI-25-C | Extended scannable directed | 0b00000110 |

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Advertising Handle set to a valid advertising set and Advertising\_Event\_Properties set to 0x00.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
3. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with Advertising\_Handle set equal to the Advertising\_Handle in Step 1.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
5. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set equal to the Advertising\_Handle in Step 1 and the specified Advertising Data.

Figure 4.36: Reject Set Extended Advertising Parameters Command using a Periodic Advertising Set and Incompatible Advertising is Specified MSC

6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
7. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Enable set to 1.
8. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
9. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command with the specified advertising set and type of advertising specified in Table 4.16.
10. The IUT returns an HCI\_Command\_Complete event with the error code Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

The IUT rejects the advertising set for each advertising type specified in Table 4.16, returning the error code Invalid HCI Command Parameters (0x12).

## 4.7.3 Reject Set Periodic Advertising Parameters Command when the Associated Handle Specifies Incompatible Advertising

- Test Purpose

Verify that the IUT properly rejects an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command when the associated handle specifies scannable, connectable, legacy, or anonymous advertising.

- Reference

[12] 7.8.61

- Initial Condition
- -An advertising set exists and is no greater than 0x1F in length, if required by the advertising type specified in Table 4.17.
- Test Case Configuration

| Test Case | Specified Advertising Type | Advertising_Event_Properties |
| HCI/DDI/BI-26-C | Non-connectable non-scannable anonymous undirected | 0b00100000 |
| HCI/DDI/BI-27-C | Non-connectable non-scannable anonymous directed | 0b00100100 |
| HCI/DDI/BI-28-C | Legacy connectable and scannable undirected | 0b00010011 |
| HCI/DDI/BI-29-C | Legacy connectable directed (low duty cycle) | 0b00010101 |
| HCI/DDI/BI-30-C | Legacy connectable directed (high duty cycle) | 0b00011101 |
| HCI/DDI/BI-31-C | Legacy scannable undirected | 0b00010010 |
| HCI/DDI/BI-32-C | Legacy non-connectable and non-scannable, undirected | 0b00010000 |
| HCI/DDI/BI-33-C | Extended connectable undirected | 0b00000001 |
| HCI/DDI/BI-34-C | Extended connectable directed | 0b00000101 |
| HCI/DDI/BI-35-C | Extended scannable undirected | 0b00000010 |
| HCI/DDI/BI-36-C | Extended scannable directed | 0b00000110 |

Table 4.17: Reject Set Periodic Advertising Parameters Command when the Associated Handle Specifies Incompatible Advertising test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command with the specified advertising set (if required) and type of advertising specified in Table 4.17.
2. The IUT returns a successful HCI\_Command\_Complete.
3. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters to the IUT using the Advertising Handle used in Step 1.
4. The IUT returns an HCI\_Command\_Complete with error code Invalid HCI Command Parameters (0x12).
- Expected Outcome

Figure 4.37: Reject Set Periodic Advertising Parameters Command when the Associated Handle Specifies Incompatible Advertising MSC

## Pass verdict

The IUT rejects the advertising set for each advertising type specified, returning the error code Invalid HCI Command Parameters (0x12).

## 4.7.4 Reject Set Periodic Advertising Enable Command when the Associated Handle Specifies Incompatible Advertising

- Test Purpose

Verify that the IUT properly rejects an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command when the associated handle specifies scannable, connectable, legacy, or anonymous advertising.

- Reference

[13] 7.8.63

- Initial Condition
- -An advertising set exists and is no greater than 0x1F in length, if required by the advertising type specified in Table 4.18.

- Test Case Configuration
- Test Procedure

Table 4.18: Reject Set Periodic Advertising Enable Command when the Associated Handle Specifies Incompatible Advertising test cases

| Test Case | Specified Advertising Type | Advertising_Event_Properties |
| HCI/DDI/BI-37-C | Non-connectable non-scannable anonymous undirected | 0b00100000 |
| HCI/DDI/BI-38-C | Non-connectable non-scannable anonymous directed | 0b00100100 |
| HCI/DDI/BI-39-C | Legacy connectable and scannable undirected | 0b00010011 |
| HCI/DDI/BI-40-C | Legacy connectable directed (low duty cycle) | 0b00010101 |
| HCI/DDI/BI-41-C | Legacy connectable directed (high duty cycle) | 0b00011101 |
| HCI/DDI/BI-42-C | Legacy scannable undirected | 0b00010010 |
| HCI/DDI/BI-43-C | Legacy non-connectable and non-scannable, undirected | 0b00010000 |
| HCI/DDI/BI-44-C | Extended connectable undirected | 0b00000001 |
| HCI/DDI/BI-45-C | Extended connectable directed | 0b00000101 |
| HCI/DDI/BI-46-C | Extended scannable undirected | 0b00000010 |
| HCI/DDI/BI-47-C | Extended scannable directed | 0b00000110 |

Figure 4.38: Reject Set Periodic Advertising Enable Command when the Associated Handle Specifies Incompatible Advertising MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Advertising Handle set to a valid advertising set and Advertising\_Event\_Properties set to 0x00.
2. The IUT returns a successful HCI\_Command\_Complete.
3. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters to the IUT using the Advertising Handle used in Step 1.
4. The IUT returns an HCI\_Command\_Complete event with Status set to 0x00.
5. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command with the specified advertising set and type of advertising specified in Table 4.18.
6. The IUT returns a successful HCI\_Command\_Complete.
7. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT using the Advertising Handle from Step 5 and Enable set to 1.
8. The IUT returns an HCI\_Command\_Complete event with Status set to Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

The IUT rejects the advertising set for each advertising type specified, returning the error code Command Disallowed (0x0C).

## HCI/DDI/BI-48-C [LE Set Data Related Address Changes, Invalid Parameter]

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Set\_Data\_Related\_Address\_Changes command with an invalid Advertising\_Handle parameter.

- Reference

[11] 7.8.122

- Initial Condition
- -The IUT is not currently advertising.
- -The Upper Tester has not sent Legacy Advertising commands to the IUT.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with a valid Advertising\_Handle parameter and receives a successful HCI\_Command\_Complete event in return.
2. The Upper Tester sends an HCI\_LE\_Set\_Data\_Related\_Address\_Changes command to the IUT with an Advertising\_Handle parameter that is not a valid advertising handle.
3. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with error Unknown Advertising Identifier (0x42).
- Expected Outcome

## Pass verdict

A Command\_Complete event for the HCI\_LE\_Set\_Data\_Related\_Address\_Changes command is received by the Upper Tester with the Unknown Advertising Identifier (0x42) error code.

## HCI/DDI/BV-06-C [Default Extended Scan Enable Command]

- Test Purpose

Verify that the IUT properly handles an HCI\_LE\_Set\_Extended\_Scan\_Enable command when the IUT is not properly configured, and returns the expected error code or executes with the vendorspecific parameters.

- Reference

[9] 7.8.65

- Initial Condition
- -The IUT is in standby.
- -Extended scanning parameters set have not been configured on the IUT (HCI\_LE\_Set\_Extended\_Scan\_Parameters was not previously executed).
- Test Procedure
1. The Upper Tester sends the HCI\_LE\_Set\_Extended\_Scan\_Enable command with the Enable parameter set to 0x01 and with all other parameters set to valid values.
2. The IUT returns an HCI\_Command\_Complete event with the Status = 0x0C ('Command Disallowed'), stopping the test here; or with Status = 0x00 ('Success') and the IUT starts a scanning procedure.
3. If the return code in Step 2 is Status = 0x00 ('Success'), the Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Parameters with a valid set of parameters (Scanning\_PHYs set to a supported PHY, Scan\_Type[0] set to 0x00 (Passive Scanning), Scan\_Interval[0] set to 0x0010, Scan\_Window[0] set to 0x0010, Own\_Address\_Type set to 0x00 (Public Device Address) and Scanning\_Filter\_Policy set to 0x00 (Accept All)).
4. The IUT sends to the Upper Tester an HCI\_Command\_Complete event with Status = 0x0C ('Command Disallowed').

Figure 4.39: HCI/DDI/BV-06-C [Default Extended Scan Enable Command] MSC

- Expected Outcome

## Pass verdict

In Step 2, the IUT generates an HCI\_Command\_Complete event either with Status = 0x0C ('Command Disallowed') or with Status = 0x00 ('Success').

If the status in Step 2 was Status = 0x00 ('Success'), then in Step 4 the IUT will generate an HCI\_Command\_Complete with Status = 0x0C ('Command Disallowed').

## HCI/DDI/BV-07-C [Set Periodic Advertising Before Periodic Advertising Parameters Command]

- Test Purpose

Verify that the IUT correctly handles an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command sent before the HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command is sent.

- Reference

[13] 7.8.63

- Initial Condition
- -The IUT is in standby.
- -Extended advertising parameters have not been configured on the IUT for a particular advertising handle.
- Test Procedure

Figure 4.40: HCI/DDI/BV-07-C [Set Periodic Advertising Before Periodic Advertising Parameters Command] MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT and receives a successful HCI\_Command\_Complete event in return from the IUT.
2. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable to the IUT with the Enable parameter set to 0x01 and the Advertising\_Handle set to the existing Advertising\_Handle.
3. Perform either alternative 3A or 3B depending on whether the IUT enabled advertising or not, which in turn depends on whether it supports vendor-specific advertising parameters: Alternative 3A (The IUT does not support vendor-specific advertising parameters):
4. 3A.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with the error code Command Disallowed (0x0C).
5. 3A.2 The IUT sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT.
6. 3A.3 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
7. Alternative 3B (The IUT supports vendor-specific advertising parameters):
8. 3B.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with the Status set to 0x00.
9. 3B.2 The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT.
10. 3B.3 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with the error code Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

In Step 3A.1, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with the error code Command Disallowed (0x0C).

In Steps 3A.3 and 3B.1, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with the Status set to 0x00.

In Step 3B.2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with the error code Command Disallowed (0x0C).

## HCI/DDI/BI-49-C [Reject LE Periodic Advertising Create Sync Command With Disallowed Reporting Options, Periodic Advertising ADI not supported]

- Test Purpose

Verify that the IUT that doesn't support Periodic Advertising ADI properly rejects invalid reporting options in the HCI\_LE\_Periodic\_Advertising\_Create\_Sync command and returns the expected error code.

- Reference

[13] 7.8.67

- Initial Condition
- -The Lower Tester is advertising with extended advertising and periodic advertising.
- -The IUT is scanning for extended advertising and has received the Advertising SID, Advertiser Address Type, and Advertiser Address.

## · Test Procedure

Figure 4.41: HCI/DDI/BI-49-C [Reject LE Periodic Advertising Create Sync Command With Disallowed Reporting Options, Periodic Advertising ADI not supported] MSC

## · Test Procedure

1. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's periodic advertisements. Options is set to 0x04 (Don't Use List, Reporting Enabled, Duplicate Filtering Enabled).
2. Perform either alternative 2A or 2B depending on the event returned.
3. Alternative 2A (The IUT returns a successful HCI\_Command\_Status event):
4. 2A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
5. 2A.2 The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester with Status set to a valid error code.
6. Alternative 2B (The IUT returns an HCI\_Command\_Status event with an error code):
7. 2B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to a valid error code.
3. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's periodic advertisements. Options is set to 0x05 (Use List, Reporting Enabled, Duplicate Filtering Enabled).
4. Perform either alternative 4A or 4B depending on the event returned.

Alternative 4A (The IUT returns a successful HCI\_Command\_Status event):

- 4A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 4A.2 The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester with Status set to a valid error code.
- Alternative 4B (The IUT returns an HCI\_Command\_Status event with an error code):
- 4B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to a valid error code.

- Expected Outcome

## Pass verdict

In Steps 2A.2 and 4A.2, the IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester with Status set to a valid error code.

In Steps 2B.1 and 4B.1, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to a valid error code.

## HCI/DDI/BV-08-C [LE Periodic Advertising Create Sync Command, Reporting Disabled]

- Test Purpose

Verify that the IUT that supports Periodic Advertising ADI properly handles disabling of periodic advertising reports.

- Reference

[13] 7.8.67

- Initial Condition
- -The Lower Tester is advertising with extended advertising and periodic advertising.
- -The IUT is scanning for extended advertising.
- Test Procedure

Figure 4.42: HCI/DDI/BV-08-C [LE Periodic Advertising Create Sync Command, Reporting Disabled] MSC

- Test Procedure
1. The IUT receives an AUX\_ADV\_IND packet from the Lower Tester and sends an HCI\_LE\_Extended\_Advertising\_Report event to the Upper Tester with the Advertising SID, Advertiser Address Type, and Advertiser Address of the Lower Tester.
2. If the Options Selected in Table 4.19 includes 'Use List', t he Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List with Advertiser\_Address\_Type, Advertiser\_Address, and Advertising\_SID set as received in Step 1 and receives a successful HCI\_Command\_Complete event in response.
3. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's periodic advertisements. The Options field is set to the value in Table 4.19 for the round, and a successful HCI\_Command\_Status event is sent in response.
4. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester with the Advertising\_SID, Advertiser\_Address\_Type, and Advertiser\_Address set to the values in Step 3 and with a valid Sync\_Handle.
5. The IUT does not send any HCI\_LE\_Periodic\_Advertising\_Report events to the Upper Tester for 3 advertising intervals.
6. Immediately after 3 periodic advertising events, the Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Terminate\_Sync command to the IUT with Sync\_Handle set to the value received in Step 4 and receives a successful HCI\_Command\_Complete event in response.
7. If the Options Selected in Table 4.19 includes 'Use List', the Upper Tester sends an HCI\_LE\_Clear\_Periodic\_Advertiser\_List and receives a successful HCI\_Command\_Complete event in response.
8. Repeat Steps 1 -7 for each round.

| Round | Options Field Value | Options Selected |
| 1 | 0x02 (Bit 1) | Don't Use List, Reporting Disabled, Duplicate Filtering Disabled |
| 2 | 0x03 (Bits 0, 1) | Use List, Reporting Disabled, Duplicate Filtering Disabled |
| 3 | 0x06 (Bits 1, 2) | Don't Use List, Reporting Disabled, Duplicate Filtering Enabled |
| 4 | 0x07 (Bits 0, 1, 2) | Use List, Reporting Disabled, Duplicate Filtering Enabled |

Table 4.19: HCI/DDI/BV-08-C [LE Periodic Advertising Create Sync Command, Reporting Disabled], option field value

## · Expected Outcome

## Pass verdict

In Step 5, the IUT does not send HCI\_LE\_Periodic\_Advertising\_Report events to the Upper Tester for 3 advertising intervals.

## HCI/DDI/BV-09-C [LE Periodic Advertising Enable Command, Disable Periodic Advertising, Periodic Advertising ADI Supported]

## · Test Purpose

Verify that the IUT that supports Periodic Advertising ADI properly handles disabling Periodic Advertising.

- Reference

[13] 7.8.63

- Initial Condition
- -Extended advertising parameters and periodic advertising parameters have been configured on the IUT for a particular advertising handle.
- Test Procedure
1. The IUT has started periodic advertising for a particular advertising handle.
2. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Advertising\_Handle set to the current advertising handle and Enable set to 0x00 and receives a successful HCI\_Command\_Complete event in response.
3. The Lower Tester verifies that no periodic advertisements are sent from the IUT for the next three periodic advertising events.
4. Immediately after 3 periodic advertising events, to restart periodic advertising, the Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Advertising\_Handle set to the advertising handle in Step 2 and Enable set to 0x01 and receives a successful HCI\_Command\_Complete event in response.

Figure 4.43: HCI/DDI/BV-09-C [LE Periodic Advertising Enable Command, Disable Periodic Advertising, Periodic Advertising ADI Supported] MSC

5. After three periodic advertising events, the Upper Tester sends an

HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Advertising\_Handle set to the advertising handle in Step 4 and Enable set to 0x02 and receives a successful HCI\_Command\_Complete event in response.

6. The Lower Tester verifies that no periodic advertisements are sent from the IUT for the next three periodic advertising events.
- Expected Outcome

## Pass verdict

In Step 3, the Lower Tester does not receive any periodic advertisements from the IUT.

In Step 6, the Lower Tester does not receive any periodic advertisements from the IUT.

## 4.7.5 Reject Set Periodic Advertising Parameters Command when Advertising Data Too Long

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command when existing periodic advertising data is greater than the controller can transmit within the periodic advertising interval.

- Reference

[12] 7.8.61

- Initial Condition
- -State: The IUT is in Standby.
- -TSPX\_per\_adv\_interval\_min is the minimum Periodic Advertising interval that is supported, as defined in the IXIT.
- Test Case Configuration

| Test Case | Primary_Advertising_PHY | Operation |
| HCI/DDI/BI-50-C [LE Set Periodic Advertising Parameters, Reject, Data Too Long, LE 1M PHY] | LE 1M PHY | 0x00 |
| HCI/DDI/BI-51-C [LE Set Periodic Advertising Parameters, Reject, Data Too Long, LE Coded PHY] | LE Coded PHY | 0x02 |

Table 4.20: Reject Set Periodic Advertising Parameters Command when Advertising Data Too Long test cases

·

Figure 4.44: Reject Set Periodic Advertising Parameters Command when Advertising Data Too Long MSC -Page 1 of 2

Figure 4.45: Reject Set Periodic Advertising Parameters Command when Advertising Data Too Long MSC -Page 2 of 2

1. The Upper Tester sends an HCI\_LE\_Read\_Maximum\_Advertising\_Data\_Length command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Max\_Advertising\_Data\_Length set to the IUT's maximum length of advertising data permitted.
3. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with valid values and receives a successful HCI\_Command\_Complete event.

4. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with Advertising\_Handle set to the value from Step 3, Periodic\_Advertising\_Interval\_Min set to 0x0050 (100 ms), and Periodic\_Advertising\_Interval\_Max set to 0x0050 (100 ms), and it receives a successful HCI\_Command\_Complete event.
5. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 3, Advertising\_Data\_Length set to 250 with Advertising\_Data set to 250 random octets from 1 to 254 as the payload. The Operation parameter is set to 0x01. The Upper Tester receives a successful HCI\_Command\_Complete event in response.
6. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 3, Advertising\_Data\_Length set to 250, Advertising\_Data set to 250 random octets from 1 to 254 as the payload, and Operation set as specified in Table 4.20, and it receives a successful HCI\_Command\_Complete event in response.
7. If LE 1M PHY is used, repeat Step 6 one time. If LE Coded PHY is used, go to Step 9.
8. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 3, Operation set to 0x02, and Advertising\_Data\_Length set to 5 and Advertising\_Data set to 5 random octets from 1 to 254 as the payload, and it receives a successful HCI\_Command\_Complete event in response.
9. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Enable command to the IUT with Enable set to 0x01, Num\_Sets set to 0x01, Advertising\_Handle set to the value in Step 3, and Duration set to 0x0000, and it receives a successful HCI\_Command\_Complete event in response.
10. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Enable set to 0x01, and it receives a successful HCI\_Command\_Complete event in response.
11. Immediately after 3 advertising events, the Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Enable set to 0x00, and it receives a successful HCI\_Command\_Complete event in response.
12. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with Advertising\_Handle set to the value from Step 3, Periodic\_Advertising\_Interval\_Min set to 0x0006 (7.5 ms), and Periodic\_Advertising\_Interval\_Max set to 0x0006 (7.5 ms).
13. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Packet Too Long (0x45).
14. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Enable set to 0x01, and it receives a successful HCI\_Command\_Complete event in response.
15. The IUT begins sending periodic advertisements.
- Expected Outcome

## Pass verdict

In Step 14, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Packet Too Long (0x45).

In Step 15, the IUT begins sending periodic advertisements.

## Inconclusive verdict

The Max\_Advertising\_Data\_Length of the IUT is less than 755 octets when the LE 1M PHY is used.

The Max\_Advertising\_Data\_Length of the IUT is less than 500 octets when the LE Coded PHY is used.

TSPX\_per\_adv\_interval\_min of the IUT is greater than 0x0006 (7.5 ms).

## HCI/DDI/BI-52-C [Reject Set Periodic Advertising Data Command when Advertising Data Too Long]

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Set\_Periodic\_Advertising\_Data command when provided periodic advertising data is greater than the controller can transmit within the periodic advertising interval.

- Reference

[12] 7.8.62

- Initial Condition
- -State: The IUT is in Standby.

Figure 4.46: HCI/DDI/BI-52-C [Reject Set Periodic Advertising Data Command when Advertising Data Too Long] MSC

1. The Upper Tester sends an HCI\_LE\_Read\_Maximum\_Advertising\_Data\_Length command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Max\_Advertising\_Data\_Length set to the IUT's maximum length of advertising data permitted.
3. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Secondary\_Advertising\_PHY set to 0x01 (LE 1M PHY) and valid values, and it receives a successful HCI\_Command\_Complete event.
4. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with Advertising\_Handle set to the value from Step 3, Periodic\_Advertising\_Interval\_Min set to 0x0006 (7.5 ms), and Periodic\_Advertising\_Interval\_Max set to 0x0006 (7.5 ms), and it receives a successful HCI\_Command\_Complete event.
5. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 3, Operation set to 0x01, and Advertising\_Data\_Length set to 250 and Advertising\_Data set to 250 random octets from 1 to 254 as the payload.
6. Perform alternative 6A or 6B depending on the received HCI\_Command\_Complete event. Alternative 6A (The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester):
7. 6A.1 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
8. Alternative 6B (The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x45):
9. 6B.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Packet Too Long (0x45).
10. 6B.2 The test ends with a Pass Verdict.
7. Perform Steps 8 and 9 twice.
8. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 3, Operation set to 0x00, and Advertising\_Data\_Length set to 250 and Advertising\_Data set to 250 random octets from 1 to 254 as the payload.
9. Perform alternative 9A or 9B depending on the received HCI\_Command\_Complete event. Alternative 9A (The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester):
14. 9A.1 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
15. Alternative 9B (The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x45):
16. 9B.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Packet Too Long (0x45).
17. 9B.2 The test ends with a Pass verdict.
10. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 3, Operation set to 0x02, Advertising\_Data\_Length set to 5, and Advertising\_Data set to 5 random octets from 1 to 254 as the payload.
11. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Packet Too Long (0x45).
- Expected Outcome

## Pass verdict

In Step 6B.1, 9B.1, or 11, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Packet Too Long (0x45).

## Inconclusive verdict

The Max\_Advertising\_Data\_Length of the IUT is less than 755 octets.

The Periodic\_Advertising\_Interval\_Min of the IUT is greater than 0x0006 (7.5 ms).

## 4.7.6 Reject LE Set Periodic Advertising Enable Command, Legacy Packet

## · Test Purpose

Verify that the IUT properly rejects enabling periodic advertising when the advertising set identifies scannable, connectable, legacy, or anonymous advertising.

- Reference

[12] 7.8.63

- Initial Condition
- -The IUT is in standby.
- Test Case Configuration

Table 4.21: Reject LE Periodic Advertising Enable Command, Legacy Packet test cases

| Test Case | Specified Advertising Type | Advertising_Event_Properties |
| HCI/DDI/BI-53-C | Non-connectable non-scannable anonymous undirected | 0b00100000 |
| HCI/DDI/BI-54-C | Non-connectable non-scannable anonymous directed | 0b00100100 |
| HCI/DDI/BI-55-C | Legacy connectable and scannable undirected | 0b00010011 |
| HCI/DDI/BI-56-C | Legacy scannable undirected | 0b00010010 |
| HCI/DDI/BI-57-C | Legacy non-connectable and non-scannable, undirected | 0b00010000 |
| HCI/DDI/BI-58-C | Extended connectable undirected | 0b00000001 |
| HCI/DDI/BI-59-C | Extended connectable directed | 0b00000101 |
| HCI/DDI/BI-60-C | Extended scannable undirected | 0b00000010 |
| HCI/DDI/BI-61-C | Extended scannable directed | 0b00000110 |

## · Test Procedure

Figure 4.47: Reject LE Periodic Advertising Enable Command, Legacy Packet MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with a valid Advertising\_Handle and with Advertising\_Event\_Properties set to extended nonscannable non-connectable (0b00000000) and receives a successful HCI\_Command\_Complete event in return.
2. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with the Advertising\_Handle set to the value from Step 1 and receives a successful HCI\_Command\_Complete event in return.
3. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the value from Step 1, Advertising\_Data\_Length set to 1, Advertising\_Data set to one random octet, and receives a successful HCI\_Command\_Complete event in return from the IUT.
4. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Advertising\_Handle set to the value from Step 1 and Advertising\_Event\_Properties set to the value in Table 4.21, and receives a successful HCI\_Command\_Complete event in return.
5. If the scannable advertising property bit (bit 1) is not set, skip to Step 6. Otherwise, the Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Response\_Data command to the IUT with Advertising\_Handle set to the value from Step 1, Scan\_Response\_Data\_Length set to 1, and Scan\_Response\_Data set to one random octet, and receives a successful HCI\_Command\_Complete event in return.
6. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Enable command to the IUT with Enable set to 0x01, and receives a successful HCI\_Command\_Complete event in return.
7. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Enable set to 0x01.
8. The IUT sends an HCI\_Command\_Complete event with Status set to Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

In Step 8, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

## HCI/DDI/BI-62-C [Reject Set Extended Advertising Parameters Command, Packet Too Long, LE Coded]

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Set\_Extended\_Advertising\_Parameters command when extended advertising data is greater than the controller can transmit within the advertising interval using the LE Coded PHY.

- Reference

[12] 7.8.53, 7.8.54

- Initial Condition
- -State: The IUT is in Standby.

Figure 4.48: HCI/DDI/BI-62-C [Reject Set Extended Advertising Parameters Command, Packet Too Long, LE Coded] MSC

1. The Upper Tester sends an HCI\_LE\_Read\_Maximum\_Advertising\_Data\_Length command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Max\_Advertising\_Data\_Length set to the IUT's maximum length of advertising data permitted.
3. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Primary\_Advertising\_Interval\_Min and Primary\_Advertising\_Interval\_Max set to 30 ms (0x30), Advertising\_Event\_Properties set to non-connectable, non-scannable (0x0000), Primary and Secondary Phys set to LE Coded, and receives a successful HCI\_Command\_Complete event in return.
4. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Data command to the IUT setting the advertising data to 251 octets using random octets from 1 to 255 as the payload. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
5. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Primary\_Advertising\_Interval\_Min and Primary\_Advertising\_Interval\_Max set to 20 ms (0x20), Advertising\_Event\_Properties set to non-connectable, non-scannable (0x0000), and Max\_Skip set to 0.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Packet Too Long (0x45).

- Expected Outcome

## Pass verdict

In Step 6, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with the Packet Too Long (0x45) error code.

## Inconclusive verdict

The Max\_Advertising\_Data\_Length received in Step 2 is less than 251 octets.

## 4.7.7 Reject Set Extended Advertising Data Commands, Data Too Long

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Set\_Extended\_Advertising\_Data and HCI\_LE\_Set\_Extended\_Scan\_Response\_Data commands when extended advertising data is greater than the controller can store.

- Reference

[12] 7.8.54, 7.8.55

- Initial Condition
- -State: The IUT is in Standby.
- Test Case Configuration

| Test Case | Primary Advertising PHY | Advertising_ Event_Properties (Step 3) | HCI Command (Step 4) |
| HCI/DDI/BI-63-C [Reject Set Extended Advertising Data Command, Data Too Long, LE 1M PHY] | LE 1M PHY | 0x0000 | HCI_LE_Set_Extended_Advertising_Data |
| HCI/DDI/BI-64-C [Reject Set Extended Advertising Data Command, Data Too Long, LE Coded PHY] | LE Coded PHY | 0x0000 | HCI_LE_Set_Extended_Advertising_Data |
| HCI/DDI/BI-65-C [Reject Set Extended Scan Response Data Command, Data Too Long, LE 1M PHY] | LE 1M PHY | 0x0002 | HCI_LE_Set_Extended_Scan_Response_Data |
| HCI/DDI/BI-66-C [Reject Set Extended Scan Response Data Command, Data Too Long, LE Coded PHY] | LE Coded PHY | 0x0002 | HCI_LE_Set_Extended_Scan_Response_Data |

Table 4.22: Reject Set Extended Advertising Data Commands, Data Too Long test cases

Figure 4.49: Reject Set Periodic Advertising Data Command when Advertising Data Too Long MSC

1. The Upper Tester sends an HCI\_LE\_Read\_Maximum\_Advertising\_Data\_Length command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Max\_Advertising\_Data\_Length set to the IUT's maximum length of advertising data permitted.
3. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Primary\_Advertising\_Interval\_Min and Primary\_Advertising\_Interval\_Max set to 200 ms (0x140) and Advertising\_Event\_Properties set to the value specified in Table 4.22 and receives a successful HCI\_Command\_Complete event in return.
4. Perform Steps 5 and 6 a total of 7 times. The total amount of data sent in the 7 commands equals Max\_Advertising\_Data\_Length -1 octets.
5. The Upper Tester sends the HCI Command specified in the HCI Command column in Table 4.22, using random octets as the payload. The first instance of this step sets Operation to 0x01 (first fragment), and the other instances set Operation to 0x00 (incomplete data).
6. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
7. The Upper Tester sends the HCI Command specified in the HCI Command column in Table 4.22, using 2 random octets as the payload and Operation set to 0x00 (incomplete data).
8. The IUT sends an HCI\_Command\_Complete event to the Upper Tester.
9. If the Status is Memory Capacity Exceeded (0x07), the test ends with a Pass verdict. Otherwise, if the Status is not Success (0x00), the test ends with a Fail verdict.

10. The Upper Tester sends the HCI Command specified in the HCI Command column in Table 4.22, using 1 random octet as the payload and Operation set to 0x02 (last fragment).
11. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Memory Capacity Exceeded (0x07).
- Expected Outcome

## Pass verdict

In Step 6, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.

In either Step 9 or Step 11, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Memory Capacity Exceeded (0x07).

## Fail verdict

The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to any value except Success (0x00) or Memory Capacity Exceeded (0x07).

## HCI/DDI/BI-68-C [Reject LE Set Extended Scan Parameters with Invalid Scan\_Filter\_Policy Parameters]

- Test Purpose

Verify that the IUT rejects the LE Set Extended Scan Parameters command when the controller does not support the Decision-based Advertising feature.

- Reference

[18] 7.8.64

- Initial Condition
- -The IUT is not currently scanning.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Parameters command to the IUT with Scan\_Filter\_Policy having bits 2 and 3 set to a value other than 0b00.
2. The IUT sends an HCI\_Command\_Complete event with a non-zero Status. If the Status is not set to Unsupported Feature or Parameter Value (0x11), then issue a warning.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with a non-zero Status.

## HCI/DDI/BI-69-C [LE Set Extended Advertising Parameters, Invalid Decision Parameters]

- Test Purpose

Verify that the IUT handles the Upper Tester sending invalid parameters for the LE Set Extended Advertising Parameters command using the Decision PDU bits.

- Reference

[18] 7.8.53

- Initial Condition
- -The IUT is not currently scanning.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with the Primary\_Advertising\_PHY set to LE 1M and a valid Advertising\_Event\_Parameters field with bits 2 and 7 set to 1 and bits 8 and 9 set to 0.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12.
3. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with the Primary\_Advertising\_PHY set to LE 1M and a valid Advertising\_Event\_Parameters field with bits 7 and 9 set to 0 and bit 8 set to 1.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12.
5. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with the Primary\_Advertising\_PHY set to LE 1M and a valid Advertising\_Event\_Parameters field with bits 7 and 8 set to 0 and bit 9 set to 1.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12.

## Pass verdict

In Steps 2, 4, and 6, the IUT returns an 0x12 error to the Upper Tester.

## 4.7.8 Reject Set Periodic Advertising Data Command, Not Configured for Periodic Advertising

- Test Purpose

Verify that the IUT properly rejects the start of a Periodic Advertising command when an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command has not been executed.

- Reference

[12] 7.8.62

- Initial Condition
- -Advertising data exists and is no greater than 0x1F in length.
- Test Case Configuration

| Test Case | HCI Command |
| HCI/DDI/BI-70-C | HCI_LE_Set_Periodic_Advertising_Data |
| HCI/DDI/BI-71-C | HCI_LE_Set_Periodic_Advertising_Subevent_Data |

Table 4.23: Reject Set Periodic Advertising Data Command, Not Configured for Periodic Advertising test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command with an Advertising\_Handle, Advertising\_Event\_Properties set to 0x0000, Primary\_Advertising\_PHY set to 0x01 (LE 1M), and Secondary\_Advertising\_PHY set to 0x01 (LE 1M).
2. The IUT sends a successful HCI\_Command\_Complete to the Upper Tester.
3. Perform either alternative 3A or 3B depending on the HCI Command. Alternative 3A (HCI\_LE\_Set\_Periodic\_Advertising\_Data command):
- 3A.1 The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT using the Advertising Handle used in Step 1, Operation set to 0x03, Advertising\_Data\_Length set to 0x01, and Advertising\_Data set to a random octet.

Figure 4.50: Reject Set Periodic Advertising Data Command, Not Configured For Periodic Advertising MSC

Alternative 3B (HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command):

- 3B.1 The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command to the IUT using the Advertising Handle used in Step 1, Subevent\_Data\_Length set to 0x01, Subevent\_Data set to a random octet, and Num\_Subevents\_With\_Data set to 1.
4. The IUT returns an HCI\_Command\_Complete with error code Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

The IUT rejects the periodic advertising data, returning the error code Command Disallowed (0x0C).

## HCI/DDI/BI-72-C [Reject LE Periodic Advertising Subevent Data Command, Advertising Duration Too Long]

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Periodic\_Advertising\_Subevent\_Data\_Request command when the Advertising Duration is longer than the Periodic Advertising Response Slot Delay.

- Reference

[12] 7.8.125

- Initial Condition
- -State: The IUT is in Standby.

·

Figure 4.51: Reject LE Periodic Advertising Subevent Data Command, Advertising Duration Too Long MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT using a randomly supported advertising channel and a selected advertising interval between the minimum and maximum advertising intervals supported and receives an HCI\_Command\_Complete event in response. The Advertising\_Event\_Properties parameter is set to 0x0000. The Own\_Address\_Type is set to 0x00 (Public Device Address). Both Primary\_Advertising\_PHY and Secondary\_Advertising\_PHY are set to 0x01 (LE 1M).
2. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters [v2] command to the IUT with Num\_Subevents set to 1, Subevent\_Interval set to 0x10 (20 ms), Response\_Slot\_Delay set to 0x01 (1.25 ms), Response\_Slot\_Spacing set to 0x0A, and Num\_Response\_Slots set to 0x3 and receives a successful HCI\_Command\_Complete event in response.
3. The Upper Tester enables periodic advertising using the HCI\_LE\_Set\_Periodic\_Advertising\_Enable command with the Enable parameter set to 0x01 (Periodic Advertising) and receives an HCI\_Command\_Complete event in response.
4. The Upper Tester enables advertising using the HCI\_LE\_Set\_Extended\_Advertising\_Enable command and receives an HCI\_Command\_Complete event in response.
5. The IUT sends ADV\_EXT\_IND PDUs to the Lower Tester with AdvMode set to 0b00 and an AuxPtr and AUX\_ADV\_IND PDUs on the secondary advertising channel with AdvMode set to 0b00 and SyncInfo Extended Header fields.
6. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Subevent\_Data\_Request event to the Upper Tester with Subevent\_Start set to 0 and Subevent\_Data\_Count set to 1.
7. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command to the IUT with Num\_Subevents set to 1, Subevent set to 0, Response\_Slot\_Start set to 0, Response\_Slot\_Count set to 1, Subevent\_Data\_Length[0] set to 127, and Subevent\_Data[0] set to 127 random bytes.
8. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x45 (Packet Too Long).
9. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Subevent\_Data\_Request event to the Upper Tester with Subevent\_Start set to 0 and Subevent\_Data\_Count set to 1.
10. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command to the IUT with Num\_Subevents set to 1, Subevent set to 0, Response\_Slot\_Start set to 0, Response\_Slot\_Count set to 0, Subevent\_Data\_Length[0] set to 127, and Subevent\_Data[0] set to 127 random bytes.
11. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x45 (Packet Too Long).
12. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Subevent\_Data\_Request event to the Upper Tester with Subevent\_Start set to 0 and Subevent\_Data\_Count set to 1.
13. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command to the IUT with Num\_Subevents set to 1, Subevent set to 0, Response\_Slot\_Start set to 0, Response\_Slot\_Count set to 1, Subevent\_Data\_Length[0] set to 126, and Subevent\_Data[0] set to 126 random bytes
14. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
15. The IUT sends an AUX\_SYNC\_SUBEVENT\_IND PDU to the Lower Tester on Subevent 1 with the Data from Step 13.

- Expected Outcome

## Pass verdict

In Steps 8 and 11, the IUT sends an 0x45 error in the HCI\_Command\_Complete event to the Upper Tester.

In Step 14, the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

In Step 15, the IUT advertises an AUX\_SYNC\_SUBEVENT\_IND PDU to the Lower Tester on Subevent 1 with 126 bytes of data from Step 13.

## HCI/DDI/BI-73-C [Reject LE Periodic Advertising Response Data Command, Advertising Duration Too Long]

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Periodic\_Advertising\_Response\_Data command when the Advertising Duration is longer than the Periodic Advertising Subevent Delay.

- Reference

[12] 7.8.126

- Initial Condition
- -State: The IUT is in Standby.

Figure 4.52: Reject LE Periodic Advertising Response Data Command, Advertising Duration Too Long MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Parameters command to the IUT and receives a successful HCI\_Command\_Complete event in return. The Scanning\_PHYs parameter is set to 0x01 (LE 1M), Scan\_Type[0] is set to 0x00 (Passive Scanning), Scan\_Interval[0] is set to 0x0010, Scan\_Window[0] is set to 0x0010, Own\_Address\_Type is set to 0x00 (Public Device Address), and Scanning\_Filter\_Policy is set to 0x00 (Accept All).
2. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Enable command to the IUT to enable scanning and receives a successful HCI\_Command\_Complete event in return. Filter\_Duplicates, Duration, and Period are all set to zero.
3. The Lower Tester begins advertising using ADV\_EXT\_IND and AUX\_ADV\_IND PDUs using the LE 1M PHY. The ADV\_EXT\_IND PDUs include an AuxPtr that refers to the AUX\_ADV\_IND PDUs on the secondary advertising channel. The AUX\_ADV\_IND PDUs include the AdvA field containing the Lower Tester address, a SyncInfo field referring to the AUX\_SYNC\_SUBEVENT\_IND PDUs, and the ACAD type for the Periodic Advertising Response Timing Information with subeventInterval set to 318.75 ms (0xFF), responseSlotDelay set to 313.75 ms (0xFB), and responseSlotSpacing set to 1.25 ms (0x0A). The Lower Tester continues advertising until directed to stop in the test procedure.
4. The Lower Tester is advertising using 5 Subevents, generating AUX\_SYNC\_SUBEVENT\_IND PDUs on the secondary advertising channel using the indices selected by the LE Channel Selection Algorithm #2 as specified in the SyncInfo in Step 3.
5. The IUT sends an HCI\_LE\_Extended\_Advertising\_Report event to the Upper Tester containing a non-zero Periodic\_Advertising\_Interval.
6. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's periodic advertisements and receives an HCI\_Command\_Status event in response. Options is set to 0x00 (Don't Use List, Reporting Initially Enabled, Duplicate Filtering Disabled), Advertising\_SID is set to the Advertising\_SID from Step 5, Advertiser\_Address\_Type is set to 0x00 (Public Device Address), Advertiser\_Address is set to the Lower Tester's address.
7. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established [v2] to the Upper Tester containing a Sync\_Handle, a Status of 0x00 (Success), and other fields matching the advertisements generated by the Lower Tester.
8. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Sync\_Subevent command to the IUT to synchronize with the Lower Tester's periodic advertisements, with Num\_Subevents set to 2, the Subevent field array set to [2, 4], and the Upper Tester receives a successful HCI\_Command\_Complete event in response.
9. The Lower Tester generates AUX\_SYNC\_SUBEVENT\_IND PDUs with 10 bytes of random Subevent data for the PDU corresponding to Subevent 2.
10. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Report [v2] event to the Upper Tester with Subevent set to the subevent of the received AUX\_SYNC\_SUBEVENT\_IND PDU.
11. For the report that contains Data\_Length &gt; 0, the Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Response\_Data command to the IUT with Response\_Slot set to 2, Subevent set to 2, and Response\_Data\_Length set to 127, and Response\_Data contains 127 random octets.
12. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x45 (Packet Too Long).
13. Repeat Steps 9 to 11 except that Response\_Data\_Length is set to 126 and Response\_Data contains 126 random octets.
14. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
15. The IUT sends an AUX\_SYNC\_SUBEVENT\_RSP PDU to the Lower Tester in response slot 2 and with the response data from Step 13.

- Expected Outcome

## Pass verdict

In Step 12, the IUT sends an 0x45 error in the HCI\_Command\_Complete event to the Upper Tester.

In Step 14, the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

In Step 15, the IUT sends an AUX\_SYNC\_SUBEVENT\_RSP PDU to the Lower Tester in response slot 2 and with the response data from Step 1 3.'

## HCI/DDI/BV-10-C [LE Set Resolvable Private Address Timeout v2 Range]

- Test Purpose

Verify that the controller changes the Resolvable Private Address between the specified min and max timeout. The IUT sends advertisements and changes the AdvA at random times.

- Reference

[22] 7.8.45

- Initial Condition
- -The IUT is in STANDBY mode.
- Test Procedure
1. The Upper Tester sends the HCI\_LE\_Add\_Device\_To\_Resolving\_List command to the IUT with PeerIRK set to 0 and Local\_IRK set to the local IRK and receives a successful HCI\_Command\_Complete event in response.
2. The Upper Tester sends the HCI\_LE\_Set\_Resolvable\_Private\_Address\_Timeout [v2] command to the IUT with RPA\_Timeout\_Min set to 0x0001 and RPA\_Timeout\_Max set to 0xB4 (180 s) and receives a successful HCI\_Command\_Complete event in response.
3. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Parameters command to the IUT with Advertising\_Interval\_Min and Advertising\_Interval\_Max set to 250 ms, Advertising\_Type set to 0x00, and Own\_Address\_Type set to 0x02 and receives a successful HCI\_Command\_Complete event in response.
4. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Data command to the IUT with Data\_Length set to 0 and receives a successful HCI\_Command\_Complete event in response.
5. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Enable command to the IUT with Enable set to 0x01 and receives a successful HCI\_Command\_Complete event in response.
6. The IUT starts sending ADV\_IND PDUs to the Lower Tester with AdvA set.
7. The Lower Tester receives the ADV\_IND PDUs and confirms that the AdvA changes between the RPA\_Timeout\_Min and RPA\_Timeout\_Max in Step 2.
8. Repeat Step 7 until the AdvA changes 10 times.
- Expected Outcome

## Pass verdict

In Step 7, the IUT changes the AdvA for the ADV\_IND PDU in the time between RPA\_Timeout\_Min and RPA\_Timeout\_Max in Step 3 since the most recent update or, for the first update, since Step 5 was performed.

The mean of the 10 times for changing the AdvA is between 58 seconds and 124 seconds (inclusive).

## Fail verdict

The IUT does not change the AdvA in the ADV\_IND PDU.

The IUT changes the AdvA in the ADV\_IND PDU shorter than RPA\_Timeout\_Min or longer than RPA\_Timeout\_Max.

More than 2 of the 10 timeout values are the same.

## HCI/DDI/BV-11-C [Default Advertising Interval Min and Max for Randomized Resolvable RPA Timeout]

- Test Purpose

Verify that the controller changes the Resolvable Private Address using the default min and max timeout value when the Host does not call the LE Set Resolvable Private Address Timeout [v2] command. The IUT sends advertisements and changes the AdvA at random times.

- Reference

[22] 7.8.45

- Initial Condition
- -The IUT is in STANDBY mode.
- Test Procedure
1. The Upper Tester sends the HCI\_LE\_Add\_Device\_To\_Resolving\_List command to the IUT with PeerIRK set to 0 and Local\_IRK set to the local IRK and receives a successful HCI\_Command\_Complete event in response.
2. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Parameters command to the IUT with Advertising\_Interval\_Min and Advertising\_Interval\_Max set to 250 ms, Advertising\_Type set to 0x00, and Own\_Address\_Type set to 0x02 and receives a successful HCI\_Command\_Complete event in response.
3. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Data command to the IUT with Data\_Length set to 0 and receives a successful HCI\_Command\_Complete event in response.
4. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Enable command to the IUT with Enable set to 0x01 and receives a successful HCI\_Command\_Complete event in response.
5. The IUT starts sending ADV\_IND PDUs to the Lower Tester with AdvA set.
6. The Lower Tester receives the ADV\_IND PDUs and confirms that the AdvA changes between the default.
7. Repeat Step 6 until the AdvA changes five times.
- Expected Outcome

## Pass verdict

In Step 6, the IUT changes the AdvA for the ADV\_IND PDU in the time between 8 and 15 minutes since the most recent update or, for the first update, since Step 4 was performed.

The mean of the 10 times for changing the AdvA is between 580 seconds and 800 seconds (inclusive).

Each of the timeouts in the repeats is different.

## Fail verdict

The IUT does not change the AdvA in the ADV\_IND PDU.

The IUT changes the AdvA in the ADV\_IND PDU shorter than 8 minutes or longer than 14 minutes.

## HCI/DDI/BI-74-C [LE Set Resolvable Private Address Timeout v2, Invalid Parameters]

- Test Purpose

Verify that the controller rejects an LE Set Resolvable Private Address Timeout [v2] command with invalid timeout parameters.

- Reference

[22] 7.8.45

- Initial Condition
- -The IUT is in STANDBY mode.
- Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.24.

1. The Upper Tester sends the HCI\_LE\_Set\_Resolvable\_Private\_Address\_Timeout [v2] command to the IUT with RPA\_Timeout\_Max and RPA\_Timeout\_Min set to the values in Table 4.24.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12.
3. The Upper Tester sends the HCI\_LE\_Set\_Resolvable\_Private\_Address\_Timeout [v2] command to the IUT with RPA\_Timeout\_Max set to 1 and RPA\_Timeout\_Min set to 0x0E10.
4. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

Repeat Steps 5 and 6 ten times.

5. The Upper Tester sends the HCI\_LE\_Set\_Resolvable\_Private\_Address\_Timeout [v2] command to the IUT with random RPA\_Timeout\_Max and RPA\_Timeout\_Min values with the condition 1 ≤ RPA\_Timeout\_Max &lt; RPA\_Timeout\_Min ≤ 0x0E10.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12.

| Round | Timeout Min | Timeout Max |
| 1 | 0 | 1 |
| 2 | 0 | 0 |
| 3 | 0x0E0F | 0x0E11 |
| 4 | 0x0E11 | 0x1000 |
| 5 | 0 | 0x0E10 |
| 6 | 1 | 0xFFFF |
| 7 | 2 | 1 |

Table 4.24: LE Set Resolvable Private Address Timeout v2, Invalid Parameters rounds

- Expected Outcome

## Pass verdict

In Steps 2 and 6, the IUT responds with an 0x12 error code.

In Step 4, the IUT sends a successful event.

## HCI/DDI/BV-12-C [Connect to one periodic advertising train, Periodic Advertiser List]

- Test Purpose

Verify that the IUT only synchronizes to one periodic advertising train for each address, address type, and Advertising SID.

- Reference

[12] 7.8.67

- Initial Condition
- -The Lower Tester is advertising with three periodic advertisements, PA1, PA2, and PA3. All three have the same Advertising Address, Advertising Address Type, and SID. PA1, PA2, and PA3 have periodic advertisement intervals of 20 ms, 25 ms, and 30 ms. The first PA2 is offset from PA1 by 2 ms, and the first PA3 is offset from PA1 by 5 ms.
- -The IUT is scanning for extended advertising and is receiving SyncInfo for all three advertisements.

## · Test Procedure

Figure 4.53: HCI/DDI/BV-12-C [Connect to one periodic advertising train, Periodic Advertiser List] MSC

1. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with information from the periodic advertising and receives a successful HCI\_Command\_Complete event in response.
2. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with information from the periodic advertising with a different SID than in Step 1 but with the

same address and address type as in Step 1 and receives a successful HCI\_Command\_Complete event in response.

3. The Lower Tester sends advertisement PDUs as specified in the Initial Condition. The Advertising\_SID and Advertiser\_Address are different for each advertisement.
4. After all the advertisements have started, the Upper Tester randomly sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT with the Lower Tester's periodic advertisement values and with bit 0 of the Options parameter set to 1 and receives a successful HCI\_Command\_Status in response.
5. When the IUT synchronizes with the periodic advertisement, the IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester with Periodic\_Advertising\_Interval. The Periodic\_Advertising\_Interval identifies the Periodic Advertiser that is synced.
6. The Lower Tester stops advertising the PA train identified in Step 5.
7. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT with the Lower Tester's periodic advertisement values and with bit 0 of the Options parameter set to 1 and receives a successful HCI\_Command\_Status in response.
8. For 3000 ms, the IUT does not synchronize with a periodic advertisement and does not send an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester.
9. The Lower Tester stops one of the other two Periodic Advertisements.
10. The Lower Tester changes the SID of the Periodic Advertisement in Step 9 to the SID in Step 2.
11. The Lower Tester starts advertising the SID of the Periodic Advertisement in Step 10.
12. When the IUT synchronizes with the periodic advertisement in Step 10, the IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester with a Periodic\_Advertising\_Interval. The Periodic\_Advertising\_Interval matches the periodic advertisement that was changed in Step 10.
- Expected Outcome

## Pass verdict

In Step 5, the IUT synchronizes with one of the Periodic Advertisements and sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester.

In Step 8, the IUT does not send an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester.

In Step 12, the IUT synchronizes with the Periodic Advertisement from Step 10 and sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester.

## 4.8 Host Flow Control

Verify the correct implementation of the Host flow control commands.

## HCI/HFC/BV-01-C [Set\_Event\_Mask Command]

- Test Purpose

Verify that the Set\_Event\_Mask command controls which events are generated by the IUT.

- Reference

## 1 7.3.1

- Initial Condition
- -The IUT must be configured as Central.
- -The IUT is in STANDBY mode.

Figure 4.54: HCI/HFC/BV-01-C [Set\_Event\_Mask Command] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set\_Event\_Mask command.

The IUT does not return a 'Connection Complete' event.

## HCI/HFC/BV-02-C [Set\_Event\_Filter Command]

- Test Purpose

Verify that the Set\_Event\_Filter command controls which events are generated using filters.

- Reference

## 1 7.3.3

- Initial Condition
- -The IUT must be configured as Peripheral.
- -The IUT is in STANDBY mode.

- Test Procedure
- Expected Outcome

Figure 4.55: HCI/HFC/BV-02-C [Set\_Event\_Filter Command] MSC

## Pass verdict

The IUT returns 'command complete' succeeded to the Set\_Event\_Filter command.

The IUT does not return a 'Connection Request' event.

The IUT returns a 'Role Change' event with role as Central if role switch is supported.

The IUT does return a 'Connection Complete' event.

## HCI/HFC/BV-03-C [Set\_Event\_Mask\_Page\_2 Command]

- Test Purpose

Verify that the Set Event Mask Page 2 command controls which events are generated by the IUT.

- Reference

[1] 7.3.69

- Initial Condition
- -The IUT is connected to the Lower Tester.

## · Test Procedure

Figure 4.56: HCI/HFC/BV-03-C [Set\_Event\_Mask\_Page\_2 Command] MSC

1. The Upper Tester sends an HCI\_Set\_Event\_Mask\_Page\_2 command to the IUT with Event\_Mask\_Page\_2 bits 8, 14 -25, and 63 set and receives a successful HCI\_Command\_Complete event in response.
2. The Upper Tester sends HCI ACL Data packets to the controller with 100 bytes of random data.
3. The IUT sends one or more BB packets containing the data from Step 2.
4. The IUT sends one or more HCI\_Number\_Of\_Completed\_Data\_Blocks event(s) to the Upper Tester.
5. Repeat Steps 6 -9 10 times.
6. The Upper Tester sends an HCI\_Set\_Event\_Mask\_Page\_2 command to the IUT with Event\_Mask\_Page\_2 bits 14 -25 and 63 set and receives a successful HCI\_Command\_Complete event in response.
7. The Upper Tester sends HCI ACL Data packets to the controller with 100 bytes of random data.
8. The IUT sends one or more BB packets containing the data from Step 2.
9. The IUT does not send any HCI\_Number\_Of\_Completed\_Data\_Blocks events to the Upper Tester.

- Expected Outcome

## Pass verdict

In Steps 1 and 6, t he IUT returns 'command complete' succeeded to the HCI\_Set\_Event\_Mask\_Page\_2 command.

In Step 4, the IUT sends one or more HCI\_Number\_Of\_Completed\_Data\_Blocks events to the Upper Tester.

## Fail verdict

In Step 9, the IUT sends one or more HCI\_Number\_Of\_Completed\_Data\_Blocks events to the Upper Tester.

## 4.8.1 LE Set Event Mask -Scanning state

- Test Purpose

Verify that the HCI\_LE\_Set\_Event\_Mask command controls which events are generated by the IUT when scanning is supported.

- Reference

[8] 7.3.1, 7.8.1

- Initial Condition
- -No LL connection exists.
- -The Lower Tester is configured to begin Advertising.
- -The IUT is configured to begin Passive Scanning.
- Test Case Configuration

| Test Case | HCI Command |
| HCI/HFC/BV-04-C [LE Set Event Mask - Scanning state, v1] | HCI_LE_Set_Event_Mask [v1] |
| HCI/HFC/BV-20-C [LE Set Event Mask - Scanning state, v2] | HCI_LE_Set_Event_Mask [v2] |

Table 4.25: LE Set Event Mask -Scanning state test cases

Figure 4.57: LE Set Event Mask -Scanning state MSC

1. The Upper Tester sends an HCI\_Set\_Event\_Mask command to the IUT with Event\_Mask bits 4, 7, 11, 15, 16, 47, and 61 set and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command version specified in Table 4.25 to the IUT with all Event\_Mask bits set except for 1 and 12 and receives a successful HCI\_Command\_Complete in response.
3. The Upper Tester sends an HCI\_LE\_Set\_Scan\_Enable with LE\_Scan\_Enable set to 0x01 and Filter\_Duplicates set to 0x00 and receives a successful HCI\_Command\_Complete in response.
4. The Lower Tester begins advertising.
5. After at least 20 advertisements, the Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command version specified in Table 4.25 to the IUT with Event\_Mask bit 1 set and receives a successful HCI\_Command\_Complete in response.
6. The IUT sends at least two LE Advertising Report events.

- Expected Outcome

## Pass verdict

The IUT returns HCI\_Command\_Complete event with Status = Success.

Before Step 5, the IUT does not send HCI LE Advertising Report events.

In Step 6, the IUT sends at least two LE Advertising Report events.

## 4.8.2 LE Set Event Mask -Initiating state

## · Test Purpose

Verify that the HCI\_LE\_Set\_Event\_Mask command controls which events are generated by the IUT when the Initiating state is supported.

- Reference

[8] 7.3.1, 7.8.1

- Initial Condition
- -No LL connection exists.
- -The Lower Tester sends connectable advertisements throughout the test.
- Test Case Configuration

| Test Case | HCI Command |
| HCI/HFC/BV-14-C [LE Set Event Mask - Initiating state, v1] | HCI_LE_Set_Event_Mask [v1] |
| HCI/HFC/BV-21-C [LE Set Event Mask - Initiating state, v2] | HCI_LE_Set_Event_Mask [v2] |

Table 4.26: LE Set Event Mask -Initiating state test cases

Figure 4.58: LE Set Event Mask -Initiating state MSC

1. The Upper Tester sends an HCI\_Set\_Event\_Mask command to the IUT with Event\_Mask bits 4, 7, 11, 15, 16, 47, and 61 set and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command version specified in Table 4.26 to the IUT with all Event\_Mask bits set except for 0, 2, 9, and 40 and receives a successful HCI\_Command\_Complete in response.
3. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT with valid parameters.
4. The IUT sends a CONNECT\_IND PDU to the Lower Tester.
5. The Lower Tester and the IUT establish an ACL connection.
6. The Lower Tester disconnects the connection.
7. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command version specified in Table 4.26 to the IUT with Event\_Mask bit 0 set and receives a successful HCI\_Command\_Complete in response.
8. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT with valid parameters.
9. The IUT sends a CONNECT\_IND PDU to the Lower Tester.
10. The Lower Tester and the IUT establish an ACL connection.
11. The IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester.

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event with Status = Success.

In Step 5, the IUT does not send an HCI LE Connection Complete event.

In Step 11, the IUT sends an HCI LE Connection Complete event after the connection is established.

## 4.8.3 LE Set Event Mask -Advertising state and connections supported

## · Test Purpose

Verify that the HCI\_LE\_Set\_Event\_Mask command controls which events are generated by the IUT when the Advertising state is supported.

- Reference

[8] 7.3.1, 7.8.1

- Initial Condition
- -No LL connection exists.
- -The IUT is configured to begin connectable Advertising.
- -The Lower Tester is configured to begin Active Scanning.
- Test Case Configuration

| Test Case | HCI Command |
| HCI/HFC/BV-15-C [LE Set Event Mask - Advertising state and connections supported, v1] | HCI_LE_Set_Event_Mask [v1] |
| HCI/HFC/BV-22-C [LE Set Event Mask - Advertising state and connections supported, v2] | HCI_LE_Set_Event_Mask [v2] |

Table 4.27: LE Set Event Mask - Advertising state and connections supported test cases

Figure 4.59: LE Set Event Mask -Advertising state and connections supported MSC

1. The Upper Tester sends an HCI\_Set\_Event\_Mask command to the IUT with Event\_Mask bits 4, 7, 11, 15, 16, 47, and 61 set and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command version specified in Table 4.27 to the IUT with all Event\_Mask bits set except for 0, 2, 9, and 40 and receives a successful HCI\_Command\_Complete in response.
3. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Enable with Advertising\_Enable set to 0x01 and receives a successful HCI\_Command\_Complete in response.
4. The IUT begins sending ADV\_IND PDUs to the Lower Tester.
5. The Lower Tester sends a CONNECT\_IND PDU to the IUT.
6. The IUT and the Lower Tester establish an ACL connection, but the IUT does not notify the Upper Tester.
7. The Lower Tester disconnects the connection.
8. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command version specified in Table 4.27 to the IUT with Event\_Mask bit 0 set and receives a successful HCI\_Command\_Complete in response.
9. The Lower Tester sends a CONNECT\_IND PDU to the IUT.
10. The IUT and the Lower Tester establish an ACL connection.
11. The IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester.

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Complete event with Status = Success.

Before Step 8, the IUT does not send HCI LE Advertising Report events.

In Step 11, the IUT sends an HCI\_LE\_Connection\_Complete event.

## 4.8.4 LE Set Event Mask -Key Event

## · Test Purpose

Verify that the LE Set Event Mask command masks the specified HCI Key event.

- Initial Condition
- -The IUT is in STANDBY mode.
- Test Case Configuration

| Test Case | Reference | Event Mask Bit | HCI Command/Event |
| HCI/HFC/BV-17-C [LE Set Event Mask - Key Event, LE Read Local P-256 Public Key] | [8] 7.3.1, 7.7.65.8, 7.8.1 | 7 | HCI_LE_Read_Local_P-256_Public_Key HCI_LE_Read_Local_P-256_Public_Key_Complete |
| HCI/HFC/BV-18-C [LE Set Event Mask - Key Event, LE Generate DHKey [v1]] | [8] 7.3.1, 7.7.65.9, 7.8.1 | 8 | HCI_LE_Generate_DHKey[v1] HCI_LE_Generate_DHKey_Complete |

Table 4.28: LE Set Event Mask -Key Event test cases

- Test Procedure
1. The Upper Tester sends an HCI\_Set\_Event\_Mask command to the IUT with Event\_Mask bit 61 set to 1 and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command to the IUT with the LE\_Event\_Mask bit specified in Table 4.28 set to 1 and receives a successful HCI\_Command\_Complete in response.
3. The Upper Tester sends the HCI command specified in Table 4.28 to the IUT. The tester notes the time this event is sent by the Upper Tester.
4. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
5. The IUT sends a successful HCI event specified in Table 4.28 to the Upper Tester. The tester notes the time this event is received by the Upper Tester.
6. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command to the IUT with LE\_Event\_Mask set to 0 and receives a successful HCI\_Command\_Complete in response.
7. The Upper Tester sends the HCI command specified in Table 4.28 to the IUT.
8. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.

Figure 4.60: LE Set Event Mask -Key Event MSC

9. The IUT does not send the HCI event specified in Table 4.28 to the Upper Tester. Wait for five times the time span between the times noted in Steps 3 and 5 to confirm this.
10. Repeat Steps 2 -5.
- Expected Outcome

## Pass verdict

In Step 5, the IUT sends the HCI event specified in Table 4.28 to the Upper Tester.

In Step 9, the IUT does not send the HCI event specified in Table 4.28.

## HCI/HFC/BV-19-C [LE Set Event Mask -Advertising Set Terminated event]

- Test Purpose

Verify that the LE Set Event Mask command masks the LE Advertising Set Terminated event.

- Reference

[8] 7.3.1, 7.7.65.18, 7.8.1

- Initial Condition
- -The IUT is in STANDBY mode.

Figure 4.61: HCI/HFC/BV-19-C [LE Set Event Mask -Advertising Set Terminated] MSC -Page 1 of 2

Figure 4.62: HCI/HFC/BV-19-C [LE Set Event Mask -Advertising Set Terminated] MSC -Page 2 of 2

1. The Upper Tester sends an HCI\_Set\_Event\_Mask command to the IUT with Event\_Mask bit 61 set to 1 and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command to the IUT with LE\_Event\_Mask set to 0 and receives a successful HCI\_Command\_Complete in response.
3. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with Advertising\_Event\_Properties set to 0b00000000\_00010000 and receives a successful HCI\_Command\_Complete event in response.
4. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Data command to the IUT with Advertising\_Data\_Length set to 10 and Advertising\_Data set to 10 random octets and receives a successful HCI\_Command\_Complete event in response.
5. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Enable command to the IUT with Enable set to 1, Num\_Sets set to 1, Duration [0] set to 0, and Max\_Extended\_Advertising\_Events[0] set to 8 and receives a successful HCI\_Command\_Complete event in response.
6. The IUT sends exactly eight ADV\_NONCONN\_IND PDUs to the Lower Tester.
7. For 10 advertising events after Step 6, the IUT does not send an HCI\_LE\_Advertising\_Set\_Terminated event to the Upper Tester.
8. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command to the IUT with LE\_Event\_Mask bit 17 set to 1 and receives a successful HCI\_Command\_Complete in response.
9. Repeat Steps 5 and 6.
10. The IUT sends an HCI\_LE\_Advertising\_Set\_Terminated event to the Upper Tester with Num\_Completed\_Extended\_Advertising\_Events set to 8.

- Expected Outcome

## Pass verdict

In Step 7, the IUT does not send an HCI\_LE\_Advertising\_Set\_Terminated event to the Upper Tester.

In Step 10, the IUT sends an HCI\_LE\_Advertising\_Set\_Terminated event to the Upper Tester.

## Fail verdict

In Step 6, the IUT sends fewer or more than eight PDUs to the Lower Tester.

## HCI/HFC/BV-05-C [Set\_Event\_Filter Command to perform auto accept connection from configured and specified bd address over ACL]

- Test Purpose

Verify that the Set\_Event\_Filter command can perform auto accept connection from configured and specified bd address.

- Reference

[1] 7.3.3

- Initial Condition
- -The IUT configured as Peripheral.
- -The IUT is in STANDBY mode.
- -BD address of the Lower Tester is set in HCI Set Event Filter.
- Test Procedure

Figure 4.63: HCI/HFC/BV-05-C [Set\_Event\_Filter Command to perform auto accept connection from configured and specified bd address over ACL] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set\_Event\_Filter command.

The IUT does not return a 'Connection Request' event.

The IUT does not perform role switch.

The IUT does return a 'Connection Complete' event.

## HCI/HFC/BV-06-C [Set\_Event\_Filter Command, connection request rejection]

- Test Purpose

Verify that the Set\_Event\_Filter command leads to connection request rejection from peer device which is not specified for auto accept in the filter condition.

- Reference

## 1 7.3.3

- Initial Condition
- -The IUT configured as Peripheral.
- -The IUT is in STANDBY mode.
- -BD address of the Lower Tester is NOT set in HCI Set Event Filter.
- Test Procedure

Figure 4.64: HCI/HFC/BV-06-C [Set\_Event\_Filter Command, connection request rejection] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set\_Event\_Filter command.

The IUT does not return a 'Connection Request' event.

The IUT does not perform role switch.

The IUT does not return a 'Connection Complete' event.

## HCI/HFC/BV-07-C [Set\_Event\_Filter Command, Host configures the Controller to Allow Connections, specifying a Class of Device and a Class of Device Mask]

## · Test Purpose

Verify that the Set\_Event\_Filter command controls which events are generated using filters.

In this test Host configure the Controller to Allow Connections from the Lower Tester, specifying a Class of Device and a Class of Device Mask. For this condition, the Auto Accept Flag is set to Do auto accept the connection with role switch disabled.

Test that Host will receive a Connection Complete event from the Lower Tester only when a connection request matches one of the filters set by the Host.

## · Reference

## 1 7.3.3

- Initial Condition
- -The IUT must be configured as Peripheral.
- -The IUT is in STANDBY mode.
- -Class of Device of the Lower Tester is set in HCI Set Event Filter.
- -Class of Device Mask is set to 0xFFFFFF in HCI Set Event Filter.
- -Auto Accept Flag is set to Do Auto accept the connection.

- Test Procedure
- Expected Outcome

Figure 4.65: HCI/HFC/BV-07-C [Set\_Event\_Filter Command, Host configures the Controller to Allow Connections, specifying a Class of Device and a Class of Device Mask] MSC

## Pass verdict

The IUT returns ' Command C omplete' (Status = 0x00) ( Success) to the Set\_Event\_Filter command.

The IUT will accept the connection request when the condition is met and the auto accept flag was set for that condition. The IUT will send the 'Connection Complete' (Status=0x00) (Success) event to the Host.

## HCI/HFC/BV-08-C [Set\_Event\_Filter Command to controls which events are generated using filters]

- Test Purpose

Verify that the Set\_Event\_Filter command controls which events are generated using filters.

In this test, the Host configure the Controller to Allow Connections from a device with a specific BD\_ADDR, specifying the BD\_ADDR of the Lower Tester. For this connection setup filter condition, the Auto\_Accept\_Flag is set to Do NOT auto accept the connection.

Test that the Host will receive a Connection Request event from the Lower Tester and will not auto accept the connection, and the Upper Tester verifies the behavior of the IUT for a successful connection and also an unsuccessful connection scenario.

- Reference

[1] 7.3.3

- Initial Condition
- -The IUT must be configured as Peripheral.
- -The IUT is in STANDBY mode.
- -BD address of the Lower Tester is set in HCI Set Event Filter.
- -Auto Accept Flag is set to Do NOT Auto accept the connection.
- -Connection Setup Filter Condition is set to Allow Connections from a device with a specific BD\_ADDR.
- Test Procedure

Figure 4.66: HCI/HFC/BV-08-C [Set\_Event\_Filter Command to controls which events are generated using filters] MSC -Page 1 of 2

MSC page 1 of 2: Host receives a connection request from the Lower Tester and connection is successful.

Reset the device before the next round.

Figure 4.67: HCI/HFC/BV-08-C [Set\_Event\_Filter Command to controls which events are generated using filters] MSC -Page 2 of 2

MSC page 2 of 2: The Host receives a connection request from the Lower Tester, and the Upper Tester does not reply.

- Expected Outcome

## Pass verdict

In the first round:

- -The IUT returns 'command complete' succe ss to the Set\_Event\_Filter command from the Upper Tester.
- -The IUT sends the 'Connection Request' event to the Upper Tester.
- -After the Upper Tester accepts the connection, the connection with the IUT and the Lower Tester is successfully established.

In the second round:

- -The IUT returns 'command complete' success to the Set\_Event\_Filter command from the Upper Tester.
- -The IUT sends the 'Connection Request' event to the Upper Tester.
- -After the Upper Tester does not answer the connection request, the IUT sends an LMP\_NOT\_ACCEPTED PDU with non-zero status to the Lower Tester.

## 4.8.5 Set\_Event\_Filter Command to perform auto accept synchronous connection from configured and specified bd address

- Test Purpose

Verify that the Set\_Event\_Filter command can perform auto accept connection from a configured and specified BD address over an SCO Type connection as specified in Table 4.29.

- Reference

[1] 7.3.3

- Initial Condition
- -The IUT configured as Peripheral.
- -See Section 4.1.3.
- -BD address of the Lower Tester is set in HCI Set Event Filter.
- Test Procedure
- Test Case Configuration

Figure 4.68: Set\_Event\_Filter Command to perform auto accept synchronous connection from configured and specified bd address MSC

| Test Case | SCO Type | LMP Command | LMP Accepted Command | HCI Event |
| HCI/HFC/BV-09-C | SCO | LMP_SCO_LINK_REQ | LMP_ACCEPTED | HCI Connection Complete Event |

Table 4.29: Set\_Event\_Filter Command to perform auto accept synchronous connection from configured and specified bd address test cases

| Test Case | SCO Type | LMP Command | LMP Accepted Command | HCI Event |
| HCI/HFC/BV-10-C | eSCO | LMP_eSCO_LINK_REQ | LMP_ACCEPTED_EXT | HCI Synchronous Connection Complete Event |

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set\_Event\_Filter command.

The IUT does not return a 'Connection Request' event.

The IUT does return a '(Synchronous) Connection Complete' event.

## HCI/HFC/BV-11-C [Auto Accept Off, Event Masked, connection request rejection over ACL]

- Test Purpose

Verify that the Set\_Event\_Filter command leads to connection request rejection from peer device when the HCI\_Connection\_Request event is masked.

- Reference

[1] 7.3.3

- Initial Condition
- -The IUT configured as Peripheral.
- -The IUT is in STANDBY mode.
- -The IUT has masked out the Connection Request Event (3) bit.
- Test Procedure

Figure 4.69: HCI/HFC/BV-11-C [Auto Accept Off, Event Masked, connection request rejection over ACL] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set\_Event\_Filter command.

The IUT does not return a 'Connection Request' event.

The IUT rejects the connection to the LT.

## 4.8.6 Auto Accept Off, Event Masked, connection request rejection over SCO Type

- Test Purpose

Verify that the Set\_Event\_Filter command leads to connection request rejection from peer device when the HCI\_Connection\_Request event is masked for a SCO Type connection as specified in Table 4.30.

- Reference

[1] 7.3.3

- Initial Condition
- -The IUT configured as Peripheral.
- -See Section 4.1.3.
- -The IUT has masked out the Connection Request Event (3) bit.
- Test Procedure
1. The Upper Tester calls HCI\_Set\_Event\_Filter with Auto\_Accept\_Flag=0x0 , and address of the Lower Tester, and valid values for all other parameters.
2. The Lower Tester initiates a connection to the IUT.
3. The IUT will reject the connection.

Figure 4.70: Auto Accept Off, Event Masked, connection request rejection over SCO Type MSC

- Test Case Configuration

| Test Case | SCO Type | LMP Command | LMP Not Accepted Command |
| HCI/HFC/BV-12-C | SCO | LMP_SCO_LINK_REQ | LMP_NOT_ACCEPTED |
| HCI/HFC/BV-13-C | eSCO | LMP_eSCO_LINK_REQ | LMP_NOT_ACCEPTED_EXT |

Table 4.30: Auto Accept Off, Event Masked, connection request rejection over SCO Type test cases

## · Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set\_Event\_Filter command.

The IUT does not return a 'Connection Request' event.

The IUT rejects the connection to the Lower Tester.

## 4.9 Authentication and Encryption

Verify the correct implementation of the Host flow control commands.

## HCI/AEN/BV-01-C [Link Key Commands]

- Test Purpose

Verify that the Write Stored Link Key, Read Stored Link Key, and Delete Stored Link Key commands write, read, and delete stored link keys.

## · Reference

[1] 7.3.8, 7.3.9, 7.3.10

- Initial Condition
- -No LL connection exists.

Figure 4.71: HCI/AEN/BV-01-C [Link Key Commands] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Write Stored Link Key command. The IUT returns 'command complete' succeeded to the Read Stored Link Key command and returns the expected stored link key.

The authentication using the stored link key succeeds as indicated by an 'Authentication Complete' event.

The IUT returns 'command complete' succeeded to the Delete Stored Link Key command.

The final authentication request results in a returned 'Link key Request' event.

- Note

This test case is applicable only to an IUT that support the Bluetooth Core Specification Version 2.0 or earlier.

## HCI/AEN/BV-02-C [Reading All Link Keys]

- Test Purpose

Verify that the IUT can have its link keys read, without revealing the values of the link keys stored in the controller.

- Reference

[1] 7.3.8

- Initial Condition
- -The IUT is connected via HCI and has a minimum of one stored link key.
- Test Procedure

Figure 4.72: HCI/AEN/BV-02-C [Reading All Link Keys] MSC

The Upper Tester issues a Read Stored Link Keys with Read\_All\_Flag.

The IUT returns a Return Link Keys event.

- Expected Outcome

## Pass verdict

The link key values in the Return Link Keys event are zero.

## HCI/AEN/BV-03-C [Reading Single Link Key]

- Test Purpose

Verify that the IUT can have a link key read, without revealing the value of the link keys stored in the controller.

- Reference

## 1 7.3.8

- Initial Condition
- -The IUT is connected via HCI and has a minimum of one stored link key.
- Test Procedure

The Upper Tester issues a Read Stored Link Keys for a single BD\_ADDR .

The IUT returns a Return Link Keys event.

Figure 4.73: HCI/AEN/BV-03-C [Reading Single Link Key] MSC

- Expected Outcome

## Pass verdict

The link key values in the Return Link Keys event are zero.

## HCI/AEN/BV-04-C [Link Key Commands -IUT Returns All Zero Link Key]

- Test Purpose

Verify that the Write Stored Link Key, Read Stored Link Key, and Delete Stored Link Key commands write, read, and delete stored link keys and the Return Link Keys Event does not return the value of the link keys.

- Reference

[1] 7.3.8, 7.3.9, 7.3.10

- Initial Condition
- -No LL connection exists.
- Test Procedure
- Expected Outcome

Figure 4.74: HCI/AEN/BV-04-C [Link Key Commands -IUT Returns All Zero Link Key] MSC

## Pass verdict

The IUT returns 'command complete' succeeded to the Write Stored Link Key command. The IUT returns 'command complete' succeeded to the Read Stored Link Key command and returns the all zero link key.

The authentication using the stored link key succeeds as indicated by an 'Authentication Complete' event.

The IUT returns 'command complete' succeeded to the Delete Stored Link Key command.

The final authentication request results in a returned 'Link key Request' event.

## HCI/AEN/BV-05-C [Read Local OOB Extended Data Command, test unique values]

- Test Purpose

Verify that the IUT uses distinctive random numbers to generate the P-192 and P-256 public-private key pairs.

- Reference

[1] 7.3.95

- Initial Condition
- -The IUT has been HCI reset and has been SSP enabled and Secure Connections enabled (if supported) by the Host via the Write Simple Pairing Mode and the Write Secure Connections Host Support Commands.
- Test Procedure

The Upper Tester issues a Read Local OOB Extended Data Command.

The IUT returns a Command Complete Event with four values C\_192, R\_192, C\_256, and R\_256.

Figure 4.75: HCI/AEN/BV-05-C [Read Local OOB Extended Data Command, test unique values] MSC

- Expected Outcome

## Pass verdict

For each Read Local OOB Extended Data Command, the values of R\_192 and R\_256 are different than the preceding set of values. For example, the values returned from the second read command should not be an identical match to the values from the first read command. Similarly, the values from the third read command should not be an identical match to the values from either the first or the second read command. Also, for each read command, the values of R\_192 and R\_256 should not match each other.

## HCI/AEN/BV-06-C [Public Keys]

- Test Purpose

Verify that the IUT can generate a P-256 Public-Private key pair and return the P-256 Public Key.

- Reference

[8] 7.7.65.8, 7.8.36

- Initial Condition
- -The IUT is in standby.
- Expected Outcome

Figure 4.76: HCI/AEN/BV-06-C [Public Keys] MSC

## Pass verdict

The IUT returns the local P-256 Public Key through the LE Read Local P-256 Public Key Complete event.

When the command is repeated, the IUT generates a new P-256 Public-Private key pair and returns the corresponding Public Key.

- Note

The parameter 'Local\_P -256\_Public\_Key' sent from the IUT to the Upper Tester is Key\_X\_Coordinate and Key\_Y\_Coordinate, where each of the two are 32 octets.

## HCI/AEN/BV-07-C [Generate DH Keys]

- Test Purpose

Verify that the IUT can generate a new P-256 DHKey.

- Reference

[8] 7.7.65.9, 7.8.37

- Initial Condition
- -The IUT is in standby.
- Expected Outcome

Figure 4.77: HCI/AEN/BV-07-C [Generate DH Keys] MSC

## Pass verdict

The IUT returns the DHkey through the LE Generate DHKey Complete event. The generated DHkey is verified by the Upper Tester.

- Notes

The Command is applicable only to an IUT that supports the LE Secure Connections feature.

The parameter 'Local\_P -256\_Public\_Key' sent from the IUT to the Upper Tester is Key\_X\_Coordinate and Key\_Y\_Coordinate, where each of the two are 32 octets.

## HCI/AEN/BV-08-C [Generate Debug Keys]

- Test Purpose

Verify that the IUT can generate a debug key.

- Reference

[11] 7.7.65.9, 7.8.93

- Initial Condition
- -The IUT is in standby.
- Test Procedure
- Expected Outcome

Figure 4.78: HCI/AEN/BV-08-C [Generate Debug Keys] MSC

## Pass verdict

The IUT returns the debug key through the LE Generate DHKey Complete event. The Upper Tester verifies the generated debug key.

## HCI/AEN/BV-09-C [Read Local OOB Extended Data command, Host bits not set]

- Test Purpose

Verify that the IUT rejects the Read Local OOB Extended Data command when both the Secure Connections (Host Support) and Secure Simple Pairing (Host Support) bits are not set.

- Reference

[1] 7.1.53

- Initial Condition
- -No LL connection exists.
- -The IUT has Secure Connections Host Support disabled.
- Test Procedure
1. The Upper Tester sends an HCI\_Read\_Secure\_Connections\_Host\_Support command to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester with the Secure\_Connections\_Host\_Support parameter. If Secure\_Connections\_Host\_Support is set to 0x01, then the test ends with a Fail verdict.

3. The Upper Tester sends an HCI\_Write\_Secure\_Connections\_Host\_Support command to the IUT with Secure\_Connections\_Host\_Support set to 0x00 and receives a successful HCI\_Command\_Complete event in response.
4. The Upper Tester sends an HCI\_Read\_Local\_OOB\_Extended\_Data command to the IUT.
5. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
6. The Upper Tester sends an HCI\_Write\_Secure\_Connections\_Host\_Support command to the IUT with Secure\_Connections\_Host\_Support set to 0x01 and receives a successful HCI\_Command\_Complete event in response.
7. The Upper Tester sends an HCI\_Read\_Local\_OOB\_Extended\_Data command to the IUT.
8. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
9. The Upper Tester sends an HCI\_Write\_Secure\_Connections\_Host\_Support command to the IUT with Secure\_Connections\_Host\_Support set to 0x00 and receives a successful HCI\_Command\_Complete event in response.
10. The Upper Tester sends an HCI\_Write\_Simple\_Pairing\_Mode command to the IUT with Simple\_Pairing\_Mode set to 0x01 and receives a successful HCI\_Command\_Complete event in response.
11. The Upper Tester sends an HCI\_Read\_Local\_OOB\_Extended\_Data command.
12. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
- Expected Outcome

## Pass verdict

In Step 5, the IUT returns a 0x0C error code.

In Steps 8 and 12, the IUT sends a successful HCI\_Command\_Complete event.

## Fail verdict

In Step 2, the IUT supports Secure Connections Host Support.

## 4.9.1 Generate DH Key Error With Invalid Point

## · Test Purpose

Verify that the IUT can return an error when invalid public keys are received.

## · Reference

[8], [10] 7.7.65.9, 7.8.37

- Initial Condition
- -The IUT is in standby.
- Test Case Configuration

Table 4.31: Generate DH Key Error With Invalid Point test cases

| Test Case | DH_Key Parameter |
| HCI/AEN/BI-01-C [Generate DH Key Error With Invalid Point, v5.4] | Any value |
| HCI/AEN/BI-02-C [Generate DH Key Error With Invalid Point, v6.0] | All octets set to 0xFF |

- Test Procedure

Run the test once for each of the rounds and generate invalid public keys as specified in Table 4.32 (HCI\_LE\_Generate\_DHKey PDU):

Figure 4.79: Generate DH Key Error With Invalid Point MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command to the IUT and receives a successful HCI\_Command\_Complete event in response.

Repeat Steps 2 -6 for each round in Table 4.32.

2. The Upper Tester sends an HCI\_LE\_Read\_Local\_P-256\_Public\_Key command to the IUT and receives a successful HCI\_Command\_Status event in response.
3. The IUT sends an HCI\_LE\_Read\_Local\_P-256\_Public\_Key\_Complete event to the Upper Tester with Status set to 0x00 and the generated Local\_P-256\_Public\_Key.
4. The Upper Tester sends an HCI\_LE\_Generate\_DHKey command to the IUT with the Invalid Key Type as specified in Table 4.32.
5. The IUT sends an HCI\_Command\_Status event to the Upper Tester.
6. If the Status is set to 0x00 in Step 5, the IUT sends an HCI\_LE\_Generate\_DHKey\_Complete event with Status &gt; 0x00.

| Round | Key Size | Invalid Key Type |
| 1 | P-256 | Generate valid public key and set y-coordinate = 0 |
| 2 | P-256 | Generate valid public key and flip a bit in y-coordinate |
| 3 | P-256 | Public Key coordinates (0, 0) |

Table 4.32: Generate DH Key Error With Invalid Point rounds

- Expected Outcome

## Pass verdict

The IUT returns an HCI\_Command\_Status event with Status != 0 in response to the HCI\_LE\_Generate\_DHKey.

## or

The IUT returns an HCI\_Command\_Status event with Status = 0 followed by a LE Generate DHKey Complete event with Status != 0 in response to the HCI\_LE\_Generate\_DHKey command.

In Step 6, all octets of the DH\_Key parameter are set as specified in Table 4.31.

- Note

The parameter 'Local\_P -256\_Public\_Key' sent from the IUT to the Upper Tester is Key\_X\_Coordinate and Key\_Y\_Coordinate, where each of the two are 32 octets.

## 4.10 Controller Configuration

Verify the controller configuration.

## HCI/CCO/BV-01-C [Write Location Data Command/Read Location Data Command]

- Test Purpose

Verify that the Write Location Data Command/ Read Location Data Command are handled correctly by the IUT.

- Reference

[1] 7.3.70, 7.3.71

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues Write Location Data Command with preset information to the IUT.

The Upper Tester receives success status in the Write Location Data command complete event.

The Upper Tester issues Read Location Data Command with preset information to the IUT.

Figure 4.80: HCI/CCO/BV-01-C [Write Location Data Command/ Read Location Data Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives command complete event with success status for two commands. The Upper Tester receives the data returned by the Read Location Data command complete event. The received data matches what was used in the Write Location Data Command.

## HCI/CCO/BV-03-C [Write LE Host Support Command]

- Test Purpose

Verify that the HCI\_Write\_LE\_Host\_Support command writes the LE\_Support\_Host configuration parameter of the IUT.

- Reference

[1] 7.3.79

- Initial Condition
- -The IUT is in standby.

Figure 4.81: HCI/CCO/BV-03-C [Write LE Host Support Command] MSC

- Expected Outcome

## Pass verdict

The IUT returns command complete to the first HCI\_Read\_LE\_Host\_Support command and returns the LE\_Support\_Host parameter set to 0x00.

In response to each HCI\_Read\_LE\_Host\_Support command, the Unused parameter is set to 0x00.

The IUT returns 'command complete' succeeded to the first and second HCI\_Write\_LE\_Host\_Support commands.

The IUT returns 'command complete' with LE\_Supported\_Host set to 0x01 in response to the second Read\_LE\_Host\_Support command.

The IUT returns 'command complete' with LE\_Supported\_Host set to 0x00 in response to the third Read\_LE\_Host\_Support command.

- Notes

In versions up to 5.2, the Unused parameter was called Simultaneous\_LE\_Host.

## HCI/CCO/BV-05-C [LE Not Supported]

- Test Purpose

Verify that an IUT that does not support LE does not recognize LE HCI commands.

- Reference

[1] 6.33

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester sends an HCI LE Set Event Mask Command and expects the IUT to return an HCI\_Command\_Complete event or HCI\_Command\_Status event with Status = Unknown HCI Command.

Figure 4.82: HCI/CCO/BV-05-C [LE Not Supported] MSC

- Expected Outcome

## Pass verdict

The IUT returns an HCI Command Complete or HCI\_Command\_Status event with Status = Unknown HCI Command.

## HCI/CCO/BV-07-C [BR/EDR Not Supported]

- Test Purpose

Verify that an IUT that supports LE only does not respond to BR/EDR HCI commands.

- Reference

[1] 3.2

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester sends an HCI Inquiry Command and expects the IUT to return an HCI\_Command\_Complete event or HCI\_Command\_Status event with Status = Unknown HCI Command.

Figure 4.83: HCI/CCO/BV-07-C [BR/EDR Not Supported] MSC

- Expected Outcome

## Pass verdict

The IUT returns an HCI Command Complete or HCI\_Command\_Status event with Status = Unknown HCI Command.

## HCI/CCO/BV-08-C [Read Extended Page Timeout]

- Test Purpose

Verify that the IUT correctly handles Read Extended Page Timeout.

- Reference

## 1 7.3

- Initial Condition
- -The IUT is in standby.
- Test Procedure
- a) The Upper Tester issues HCI\_Write\_Extended\_Page\_Timeout Command with preset information to the IUT.
- b) The Upper Tester receives success status in the HCI\_Write\_Extended\_Page\_Timeout Command complete event.
- c) The Upper Tester issues HCI\_Read\_Extended\_Page\_Timeout Command to the IUT.
- Expected Outcome

## Pass verdict

The Upper Tester receives command complete event with success status for the commands sent in a and c.

The Upper Tester receives the data returned by the HCI\_Read\_Extended\_Page\_Timeout Command complete event. The received data matches the data that was used in the HCI\_Write\_Extended\_Page\_Timeout Command.

## HCI/CCO/BV-09-C [LE Set Data Length]

- Test Purpose

Verify that the IUT correctly handles the LE Set Data Length Command

- Reference

[2] 7.8.33

- Initial Condition
- -LL connection established, the IUT is Central or Peripheral.
- Test Procedure

The Upper Tester issues an LE Set Data Length command to the IUT containing the current connection handle and with values for TxOctets and TxTime which lie in the permissible range.

The Upper Tester receives a Command Complete event from the IUT for the LE Set Data Length command.

If the command causes the maximum transmission packet size or maximum packet transmission time to change, the Upper Tester receives an LE Data Length Change event from the IUT containing the updated values.

Figure 4.84: HCI/CCO/BV-09-C [LE Set Data Length] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success) and with the value for Connection\_Handle matching the value sent in the LE Set Data Length Command.

The Upper Tester optionally receives an LE Data Length Change event from the IUT with updated maximum transmission packet size and maximum packet transmission time values.

## HCI/CCO/BV-10-C [LE Read Suggested Default Data Length Command]

- Test Purpose

Verify that the IUT correctly handles the LE Read Suggested Default Data Length Command

- Reference

[8] 7.8.34

- Initial Condition
- -The IUT has just been reset and is in standby.
- Test Procedure

The Upper Tester issues a LE Read Suggested Default Data Length Command to the IUT.

The Upper Tester receives a Command Complete event from the IUT for the LE Read Suggested Default Data Length Command.

Figure 4.85: HCI/CCO/BV-10-C [LE Read Suggested Default Data Length Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success) and with TxOctets equal to 0x001B and TxTime equal to 0x0148.

## HCI/CCO/BV-11-C [LE Write Suggested Default Data Length Command]

- Test Purpose

Verify that the IUT correctly handles the LE Write Suggested Default Data Length Command.

- Reference

[8] 7.8.35

- Initial Condition
- -The IUT is in standby.
- Test Procedure

For each row in Table 4.33:

The Upper Tester issues a LE Write Suggested Default Data Length Command to the IUT with the values for TxOctets and TxTime given in that row. The Upper Tester receives a Command Complete event from the IUT for the LE Write Suggested Default Data Length Command.

The Upper Tester issues a LE Read Suggested Default Data Length Command to the IUT. The Upper Tester receives a Command Complete event from the IUT for the LE Read Suggested Default Data Length Command.

Figure 4.86: HCI/CCO/BV-11-C [LE Write Suggested Default Data Length Command] MSC

| Round | TxOctets | TxTime |
| 1 | 0x001B | 0x0148 |
| 2 | 0x001B | 0x4290 |
| 3 | 0x001B | 0x2000 |
| 4 | 0x00FB | 0x0148 |
| 5 | 0x00FB | 0x4290 |
| 6 | 0x00FB | 0x2000 |
| 7 | 0x0080 | 0x0148 |
| 8 | 0x0080 | 0x4290 |
| 9 | 0x0080 | 0x2000 |
| 10 - 20 | A randomly selected value between 0x001B and 0x00FB inclusive. | A randomly selected value between 0x0148 and 0x4290 inclusive. |

Table 4.33: HCI/CCO/BV-11-C [LE Write Suggested Default Data Length Command], rounds

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status=0x00 (Success) for the LE Write Suggested Default Data Length Command.

The Upper Tester receives a Command Complete event from the IUT for the LE Read Suggested Default Data Length Command with Status=0x00 (Success).

The values for TxOctets and TxTime in the second Command Complete event equal the values sent in the LE Write Suggested Default Data Length Command.

## HCI/CCO/BV-12-C [LE Remove Device From Resolving List Command]

- Test Purpose

Verify that the IUT correctly handles the LE Remove Device From Resolving List Command

- Reference

[8] 7.8.39

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an LE Add Device To Resolving List Command to the IUT with a peer device identity.

The Upper Tester receives a Command Complete event from the IUT for the LE Add Device To Resolving List Command.

The Upper Tester issues an LE Remove Device From Resolving List Command to the IUT with the recently added peer device identity.

The Upper Tester receives a Command Complete event from the IUT for the LE Remove Device From Resolving List Command.

Figure 4.87: HCI/CCO/BV-12-C [LE Remove Device From Resolving List Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success) when sending the LE Remove Device From Resolving List Command with a valid device identity.

## HCI/CCO/BV-13-C [LE Clear Resolving List Command]

- Test Purpose

Verify that the IUT correctly handles the LE Clear Resolving List Command

- Reference

[8] 7.8.40

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an LE Add Device To Resolving List Command to the IUT with a peer device identity.

The Upper Tester receives a Command Complete event from the IUT for the LE Add Device To Resolving List Command.

The Upper Tester issues an LE Clear Resolving List Command to the IUT with the recently added peer device identity.

The Upper Tester receives a Command Complete event from the IUT for the LE Clear Resolving List Command.

Figure 4.88: HCI/CCO/BV-13-C [LE Clear Resolving List Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success) when sending the LE Clear Resolving List Command.

## HCI/CCO/BV-14-C [LE Read Resolving List Size Command]

- Test Purpose

Verify that the IUT correctly handles the LE Read Resolving List Size Command

- Reference

[8] 7.8.41

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an LE Read Resolving List Size Command to the IUT.

The Upper Tester receives a Command Complete event from the IUT for the LE Read Resolving List Size Command, with the size of the list.

Figure 4.89: HCI/CCO/BV-14-C [LE Read Resolving List Size Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success) and Resolving\_List\_Size = 0xXX when sending the LE Read Resolving List Size Command.

## HCI/CCO/BV-15-C [LE Set Default PHY Command]

- Test Purpose

Verify that the IUT correctly handles the LE Set Default PHY Command.

- Reference

[8] 7.8.48

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an LE Set Default PHY command to the IUT with ALL\_PHYS set to 0x03 (All PHYs Allowed) and both the TX\_PHYS and RX\_PHYS fields set to zero (no preferences).

The Upper Tester receives a Command Complete event from the IUT for the LE Set Default PHY command.

Figure 4.90: HCI/CCO/BV-15-C [LE Set Default PHY Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success).

## HCI/CCO/BV-16-C [LE Read Periodic Advertiser List Size Command]

- Test Purpose

Verify that the IUT correctly handles the LE Read Periodic Advertiser List Size Command.

- Reference

[9] 7.8.73

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an LE Read Periodic Advertiser List Size Command.

The Upper Tester receives a Command Complete event from the IUT for the LE Read Periodic Advertiser List Size Command, with the size of the list.

Figure 4.91: HCI/CCO/BV-16-01-C [LE Read Periodic Advertiser List Size Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete Event with Status = 0x00 (Success) and Periodic\_Advertiser\_List\_Size = 0xXX after sending the LE Read Periodic Advertiser List Size command.

## HCI/CCO/BV-17-C [LE Add/Remove/Clear Periodic Advertiser List Commands]

- Test Purpose

Verify that the IUT correctly handles the LE Add Device To Periodic Advertiser List, LE Remove Device From Periodic Advertiser List, and Clear Periodic Advertiser List commands.

- Reference

[9] 7.8.70, 7.8.71, 7.8.72

- Initial Condition
- -The IUT is in standby.
- -The IUT's Periodic Advertiser List is empty.

## · Test Procedure

Figure 4.92: HCI/CCO/BV-17-C [LE Add/Remove/Clear Periodic Advertiser List Commands] MSC

1. The Upper Tester sends an HCI\_LE\_Clear\_Periodic\_Advertiser\_List command to the IUT and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
2. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with an arbitrarily chosen valid address, address type, and SID and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
3. The Upper Tester sends an HCI\_LE\_Remove\_Device\_From\_Periodic\_Advertiser\_List command to the IUT with the parameter values from Step 2 and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
4. The Upper Tester sends an HCI\_LE\_Remove\_Device\_From\_Periodic\_Advertiser\_List command to the IUT with the parameter values from Step 2 and receives an HCI\_Command\_Complete event from the IUT with the Status set to 0x42 (Unknown Advertising Identifier).
5. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with with the same address, address type, and SID as used in Step 2 and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
6. The Upper Tester sends an HCI\_LE\_Clear\_Periodic\_Advertiser\_List command to the IUT and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
7. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with the same address, address type, and SID as used in Step 2 and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
8. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with the same address, address type, and SID as used in Step 2 and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x12 (Invalid HCI Command Parameters).
9. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with the same address and address type as used in Step 2 but a different SID and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
10. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Periodic\_Advertiser\_List command to the IUT with the same address and SID as Step 2 but a different address type and receives an HCI\_Command\_Complete event from the IUT with Status set to 0x00 (Success).
- Expected Outcome

## Pass verdict

The Upper Tester receives an HCI\_Command\_Complete event with the expected status for each command.

## HCI/CCO/BV-18-C [LE Read Transmit Power Command]

- Test Purpose

Verify that the IUT correctly handles the LE Read Transmit Power Command.

- Reference

## 9 7.8.74

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an HCI\_LE\_Read\_Transmit\_Power Command.

The Upper Tester receives a Command Complete event from the IUT with Status set to 0x00 (Success) and values for Min\_Tx\_Power and Max\_Tx\_Power.

Figure 4.93: HCI/CCO/BV-18-C [LE Read Transmit Power Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete Event with Status = 0x00 (Success), Min\_Tx\_Power = 0xXX, and Max\_Tx\_Power = 0xXX after sending the LE Read Transmit Power command.

## HCI/CCO/BV-19-C [LE Write RF Path Compensation Command]

- Test Purpose

Verify that the IUT correctly handles the LE Write RF Path Compensation Command.

- Reference

[9] 7.8.76

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an HCI\_LE\_Write\_RF\_Path\_Compensation Command with RF\_Tx\_Path\_Compensation\_Value set to 0x0001 and RF\_Rx\_Path\_Compensation\_Value set to 0x0001.

The Upper Tester receives a Command Complete event from the IUT with Status set to 0x00 (Success).

Figure 4.94: HCI/CCO/BV-19-C [LE Write RF Path Compensation Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete Event with Status = 0x00 (Success) after sending the LE Write RF Path Compensation Command.

## HCI/CCO/BV-20-C [LE Read RF Path Compensation Command]

- Test Purpose

Verify that the IUT correctly handles the LE Read RF Path Compensation Command.

- Reference

## 9 7.8.75

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues an HCI\_LE\_Read\_RF\_Path\_Compensation Command.

The Upper Tester receives a Command Complete event from the IUT with Status set to 0x00 (Success) and values for RF\_Tx\_Path\_Compensation\_Value and RF\_Rx\_Path\_Compensation\_Value.

Figure 4.95: HCI/CCO/BV-20-C [LE Read RF Path Compensation Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete Event with Status = 0x00 (Success), RF\_Tx\_Path\_Compensation\_Value = 0xXXXX, and RF\_Rx\_Path\_Compensation\_Value = 0xXXXX after sending the LE Read RF Path Compensation Command.

## HCI/CCO/BV-21-C [Set Minimum Encryption Key Size]

- Test Purpose

Verify that the IUT properly sets the minimum encryption key size.

- Reference

[13] 7.3.102

- Initial Condition
- -TSPX\_min\_encryption\_key\_size is the minimum encryption key size, as defined in the IXIT.
- -TSPX\_max\_encryption\_key\_size is the maximum encryption key size, as defined in the IXIT.
- Test Procedure

Figure 4.96: HCI/CCO/BV-21-C [Set Minimum Encryption Key Size] MSC

Repeat Steps 1 and 2 for each encryption key size value KS in the interval [TSPX\_min\_encryption\_key\_size, TSPX\_max\_encryption\_key\_size]:

1. The Upper Tester sends an HCI\_Set\_Min\_Encryption\_Key\_Size with the Min\_Encryption\_Key\_Size set to KS.
2. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 2, the Upper Tester receives a successful HCI\_Command\_Complete event.

## HCI/CCO/BV-27-C [Set Minimum Encryption Key Size, v6.2 or later]

- Test Purpose

Verify that the IUT that supports Core v6.2 or later properly sets the minimum encryption key size. The IUT returns an error when the encryption key size is less than max[7, TSPX\_min\_encryption\_key\_size].

- Reference

[13] 7.3.102

- Initial Condition
- -TSPX\_min\_encryption\_key\_size is the minimum encryption key size, as defined in the IXIT.
- -TSPX\_max\_encryption\_key\_size is the maximum encryption key size, as defined in the IXIT.
- Test Procedure

Repeat Steps 1 and 2 for each encryption key size value KS in the interval [1, TSPX\_max\_encryption\_key\_size]:

1. The Upper Tester sends an HCI\_Set\_Min\_Encryption\_Key\_Size with the Min\_Encryption\_Key\_Size set to KS.
2. 2.
3. Perform either alternative 2A or 2B depending on KS.

Alternative 2A (KS ≥ TSPX\_min\_encryption\_key\_size):

- 2A.1 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

Alternative 2B (KS &lt; TSPX\_min\_encryption\_key\_size):

- 2B.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11.
- Expected Outcome

## Pass verdict

In Step 2A.1, the Upper Tester receives a successful HCI\_Command\_Complete event.

In Step 2B.1, the Upper Tester receives an HCI\_Command\_Complete event with a 0x11 error code.

## Fail verdict

TSPX\_min\_encryption\_key\_size &lt; 7

## HCI/CCO/BV-22-C [Read Clock Offset, Peripheral]

- Test Purpose

Verify that the Peripheral IUT Read Clock Offset command immediately returns a Read Clock Offset Complete event.

- Reference

[13] 7.1.24

- Initial Condition
- -BR/EDR connection established, the IUT is Peripheral.
- Test Procedure
1. The Upper Tester sends an HCI\_Read\_Clock\_Offset command to the IUT with Connection\_Handle set to the current connection handle, and it receives a successful HCI\_Command\_Status event in return.
2. The IUT sends an HCI\_Read\_Clock\_Offset\_Complete event to the Upper Tester with Connection\_Handle set to the current connection handle, and the Clock\_Offset is set to the IUT's clock offset.

Figure 4.97: HCI/CCO/BV-22-C [Read Clock Offset, Peripheral] MSC

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Read\_Clock\_Offset\_Complete event to the Upper Tester. The IUT does not send LMP PDUs between Steps 1 and 2.

## Fail verdict

The IUT sends an LMP PDU between Steps 1 and 2.

## HCI/CCO/BV-23-C [LE Set Extended Advertising Parameters, Advertising Coding Selection Not Supported]

- Test Purpose

Verify that the IUT properly returns an error in response to the LE Set Extended Advertising Parameters [v2] command when the IUT does not support the Advertising Coding Selection feature.

- Reference

[13] 7.8.53

- Initial Condition
- -The IUT is configured in an advertising state.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters [v2] command to the IUT with Primary\_Advertising\_PHY and Secondary\_Advertising\_PHY set to 0x03, Primary\_Advertising\_PHY\_Options set to 0x01, and Secondary\_Advertising\_PHY\_Options set to 0x00.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11 ('Unsupported Feature or Parameter Value').
3. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters [v2] command to the IUT with Primary\_Advertising\_PHY and Secondary\_Advertising\_PHY set to 0x03, Primary\_Advertising\_PHY\_Options set to 0x00, and Secondary\_Advertising\_PHY\_Options set to 0x01.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11 ('Unsupported Feature or Parameter Value').
5. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters [v2] command to the IUT with Primary\_Advertising\_PHY and Secondary\_Advertising\_PHY set to 0x03 and Primary\_Advertising\_PHY\_Options and Secondary\_Advertising\_PHY\_Options both set to 0x00.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
- Expected Outcome

## Pass verdict

In Steps 2 and 4, the IUT returns an error in the HCI\_Command\_Complete event.

In Step 6, the IUT returns a successful HCI\_Command\_Complete event.

## HCI/CCO/BI-75-C [LE Frame Space Update, Invalid Frame Space Parameters]

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Frame Space Update command.

- Reference

[19] 7.7.65.48

- Initial Condition
- -The LL connection is established, the IUT is Central or Peripheral, and T\_IFS = 150 μs .
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Frame\_Space\_Update command to the IUT with the Parameters specified in Table 4.34.
2. Perform either alternative 2A or 2B depending on the IUT HCI\_Command\_Status response. Alternative 2A (Successful HCI\_Command\_Status):
- 2A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2A.2 The IUT sends an HCI\_LE\_Frame\_Space\_Update\_Complete event to the Upper Tester with Status set as specified in Table 4.34.

Alternative 2B (HCI\_Command\_Status with an error code):

- 2B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set as specified in Table 4.34.

Table 4.34: LE Frame Space Update, Invalid Parameters rounds

| Round | Parameters | Error |
| 1 | Frame_Space_Min = 0x2711 | 0x12 |
| 2 | Frame_Space_Max = 0x2711 | 0x12 |
| 3 | Connection_Handle != ACL connection handle | 0x02 |
| 4 | PHYs = 0x00 | 0x12 |
| 5 | Spacing_Type = 0x00 | 0x12 |
| 6 | Frame_Space_Min = 1, Frame_Space_Max = 0 | 0x12 |

## · Expected Outcome

## Pass verdict

In Step 2, the IUT rejects the command with the specified error code.

## 4.10.1 LE CS Set Procedure Parameters, Invalid Parameters

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an HCI\_LE\_CS\_Set\_Procedure\_Parameters command with invalid parameters.

## · Reference

[19] 7.8.140

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, exchanged capabilities, created a configuration with Config\_ID set to 0, and set default settings.
- -The max CS procedure count is defined by the TSPX\_CS\_Max\_Procedure\_Count IXIT value.
- Test Case Configuration
- Test Procedure

Table 4.35: LE CS Set Procedure Parameters, Invalid Parameters test cases

| Test Case | Rounds to perform |
| HCI/CCO/BI-116-C [LE CS Set Procedure Parameters, Invalid Parameters, v6.0] | 1 to 4 |
| HCI/CCO/BI-123-C [LE CS Set Procedure Parameters, Invalid Parameters, v6.1] | 1 to 5 |

Repeat Steps 1 and 2 for each round in Table 4.36. Each round has an interval of 1.25 seconds. Rounds 1 and 2 are executed only if TSPX\_CS\_Max\_Procedure\_Count &gt; 1 or TSPX\_CS\_Max\_Procedure\_Count = 0.

1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with Config\_ID set to 0, Max\_Procedure\_Count = 2, parameters set as specified in Table 4.36, and all other parameters set to valid values.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).
- Expected Outcome

Table 4.36: LE CS Set Procedure Parameters, Invalid Parameters rounds

| Round | Parameter | Value |
| 1 | Max_Procedure_Interval | 0 |
| 2 | Min_Procedure_Interval | 0 |
| 3 | Min_Subevent_Len | 1249 |
| 4 | Max_Subevent_Len | 40000001 |
| 5 | Max_Subevent_Len | 40000000 |

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event with Status set to 0x12.

## HCI/CCO/BI-117-C [HCI CS Command, Unencrypted ACL]

- Test Purpose

Verify that the IUT properly returns an error when the Upper Tester sends HCI CS commands that start an LL exchange with an unencrypted ACL connection with the Lower Tester.

- Initial Condition
- -The IUT and the Lower Tester have an unencrypted ACL connection.

## · Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.37.

1. The Upper Tester sends an HCI command in Table 4.37.
2. Perform alternative 2A or 2B depending on the IUT response.

Alternative 2A (HCI\_Command\_Status event with an error code):

- 2A.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status &gt; 0.
- Alternative 2B (Successful HCI\_Command\_Status event followed by an HCI event with an error):
- 2B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2B.2 The IUT sends an HCI event specified in Table 4.37 with Status &gt; 0.
- Expected Outcome

| Round | Reference | HCI Command/HCI Event | LL PDU |
| 1 | [19] 7.8.131 | HCI_LE_CS_Read_Remote_Supported_Capabilities HCI_LE_CS_Read_Remote_Supported_Capabilities_Complete | LL_CS_CAPABILITIES_REQ |
| 2 | [19] 7.8.135 | HCI_LE_CS_Read_Remote_FAE_Table HCI_LE_CS_Read_Remote_FAE_Table_Complete | LL_CS_FAE_REQ |
| 3 | [19] 7.8.137 | HCI_LE_CS_Create_Config HCI_LE_CS_Config_Complete | LL_CS_CONFIG_REQ |

Table 4.37: HCI CS Command, Unencrypted ACL rounds

## Pass verdict

In Step 2A.1 or 2B.2, the IUT sends an HCI event to the Upper Tester with an error code.

## Fail verdict

After Step 2B.1, the IUT sends the LL PDU specified in Table 4.37 on the unencrypted ACL.

## 4.10.2 Resolving List Commands fail when list in use

- Test Purpose

Verify that the IUT correctly fails the Resolving List commands when the resolving list is in use.

- Reference

[2] 7.8.38, 7.8.39, 7.8.40, 7.8.44, 7.8.77

- Initial Condition
- -The IUT is in standby.
- -The IUT has address resolution enabled with at least one device identity added to the resolving list.

## · Test Procedure

Figure 4.98: Resolving List Commands fail when list in use MSC

The Upper Tester issues the one or two commands specified in Table 4.38 to the IUT and receives a successful HCI\_Command\_Complete or HCI\_Command\_Status event in return for each.

The Upper Tester issues each of the following commands to the IUT and receives an HCI\_Command\_Complete event with a non-zero status in reply for each:

- -HCI\_LE\_Add\_Device\_To\_Resolving\_List
- -HCI\_LE\_Remove\_Device\_From\_Resolving\_List
- -HCI\_LE\_Clear\_Resolving\_List
- -HCI\_LE\_Set\_Address\_Resolution\_Enable (Address\_Resolution\_Enable = 0x00)
- -HCI\_LE\_Set\_Address\_Resolution\_Enable (Address\_Resolution\_Enable = 0x01)
- -HCI\_LE\_Set\_Privacy\_Mode (Peer\_Identity\_Address\_Type = 0x00)
- -HCI\_LE\_Set\_Privacy\_Mode (Peer\_Identity\_Address\_Type = 0x01)

- Test Case Configuration

Table 4.38: Resolving List Commands fail when list in use test cases

| Test Case | Reference | HCI Command(s) |
| HCI/CCO/BI-01-C | [2] 7.8.38 | HCI_LE_Set_Advertising_Parameters (Advertising_Type: 0x03) HCI_LE_Set_Advertising_Enable (Advertising_Enable: 0x01) |
| HCI/CCO/BI-02-C | [2] 7.8.39 | HCI_LE_Set_Scan_Parameters (LE_Scan_Type: 0x01) HCI_LE_Set_Scan_Enable (LE_Scan_Enable: 0x01) |
| HCI/CCO/BI-03-C | [2] 7.8.40 | HCI_LE_Create_Connection (Initiator_Filter_Policy: 0x00) |
| HCI/CCO/BI-04-C | [2] 7.8.44 | HCI_LE_Extended_Create_Connection (Initiator_Filter_Policy: 0x00) |
| HCI/CCO/BI-05-C | [2] 7.8.77 | HCI_LE_Periodic_Advertising_Create_Sync (Options: 0x00) |

All command parameters not explicitly listed in the table may have any valid value.

- Expected Outcome

## Pass verdict

The Upper Tester receives an HCI\_Command\_Complete event from the IUT with non-zero status when sending each Resolving List command.

## 4.10.3 Invalid LE Power Control HCI Parameters

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending invalid parameters for LE Power Control related HCI commands.

- Reference

[12] 7.8

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester in the relevant role.

## · Test Procedure

Figure 4.99: Invalid LE Power Control HCI Parameters MSC

1. The Upper Tester sends the HCI Command and Parameter as specified in Table 4.39.
2. The IUT sends the Event and Status/Error Code as specified in Table 4.39 to the Upper Tester.
- Test Case Configuration

| Test Case | HCI Command | Parameter | Event and Status/Error Code |
| HCI/CCO/BI-06-C [LE Enhanced Read Transmit Power Level - Invalid Connection Handle] | HCI_LE_Enhanced_ Read_Transmit_ Power_Level | Connection_Handle set to an invalid ACL | HCI_Command_Complete : Unknown Connection Identifier (0x02) |
| HCI/CCO/BI-07-C [LE Enhanced Read Transmit Power Level - Invalid PHY] | HCI_LE_Enhanced_ Read_Transmit_ Power_Level | PHY = 0xF0 | HCI_Command_Complete : Unsupported Feature or Parameter Value (0x11) |
| HCI/CCO/BI-08-C [LE Read Remote Transmit Power Level - Invalid Connection Handle] | HCI_LE_Read_ Remote_Transmit_ Power_Level | Connection_Handle set to an invalid ACL | HCI_Command_Status : Unknown Connection Identifier (0x02) or HCI_Command_Status : Status(0x00) HCI_LE_Transmit_Power_ Reporting event : Status (0x02) |

Table 4.39: Invalid LE Power Control HCI Parameters test cases

| Test Case | HCI Command | Parameter | Event and Status/Error Code |
| HCI/CCO/BI-09-C [LE Read Remote Transmit Power Level - Invalid PHY] | HCI_LE_Read_ Remote_Transmit_ Power_Level | PHY = 0xF0 | HCI_Command_Status : Unsupported Feature or Parameter Value (0x11) or HCI_Command_Status : Status(0x00) HCI_LE_Transmit_Power_ Reporting event : Status (0x11) |
| HCI/CCO/BI-10-C [LE Set Path Loss Reporting Parameters - Invalid Connection Handle] | HCI_LE_Set_Path_ Loss_Reporting_ Parameters | Connection_Handle set to an invalid ACL | HCI_Command_Complete : Unknown Connection Identifier (0x02) |
| HCI/CCO/BI-11-C [LE Set Path Loss Reporting Enable - Invalid Connection Handle] | HCI_LE_Set_Path_ Loss_Reporting_ Enable | Connection_Handle set to an invalid ACL | HCI_Command_Complete : Unknown Connection Identifier (0x02) |
| HCI/CCO/BI-12-C [LE Set Transmit Power Reporting Enable - Invalid Connection Handle] | HCI_LE_Set_ Transmit_Power_ Reporting_Enable | Connection_Handle set to an invalid ACL | HCI_Command_Complete : Unknown Connection Identifier (0x02) |

- Expected Outcome

## Pass verdict

In Step 2, the IUT returns the Status as specified in Table 4.39.

## HCI/CCO/BI-13-C [Invalid Path Loss Monitoring Parameters]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending invalid parameters for LE Path Loss Reporting -related HCI commands.

- Reference

[12] 7.8.119

- Initial Condition
- -Parameters: TSPX\_Path\_Loss\_Lower\_Boundary, TSPX\_Path\_Loss\_Upper\_Boundary (specified in LL IXIT). The Lower Tester and the IUT are configured as specified in the RF Test Conditions section in [5].
- -An ACL connection has been established between the IUT and the Lower Tester in the relevant role.

## · Test Procedure

Figure 4.100: HCI/CCO/BI-13-C [Invalid Path Loss Monitoring Parameters] MSC

1. The Lower Tester continuously transmits empty data packets over the ACL connection with a connection interval of 7.5 ms.
2. The Upper Tester enables path loss reporting for the active connection by sending an HCI\_LE\_Set\_Path\_Loss\_Reporting\_Enable command to the IUT with the Connection\_Handle corresponding to the active connection and Enable = 0x01. The IUT responds with an HCI\_Command\_Complete with Status=0x0C.
3. The Upper Tester sends an HCI\_LE\_Set\_Path\_Loss\_Reporting\_Parameters command to the IUT, with the following parameter values: Connection\_Handle set to the active connection handle, High\_Threshold = 0xF0, High\_Hysteresis = 0xF0. The IUT responds with an HCI\_Command\_Complete with Status = 0x12.
4. The Upper Tester sends an HCI\_LE\_Set\_Path\_Loss\_Reporting\_Parameters command to the IUT, with the following parameter values: Connection\_Handle set to the active connection handle, Low\_Threshold = 0x10, Low\_Hysteresis = 0x20. The IUT responds with an HCI\_Command\_Complete with Status = 0x12.

5. The Upper Tester sends an HCI\_LE\_Set\_Path\_Loss\_Reporting\_Parameters command to the IUT, with the following parameter values: Connection\_Handle set to the active connection handle, High\_Threshold = 0xE0, Lower\_Threshold 0xF0. The IUT responds with an HCI\_Command\_Complete with Status = 0x12.
6. The Upper Tester sends an HCI\_LE\_Set\_Path\_Loss\_Reporting\_Parameters command to the IUT, with the following parameter values: Connection\_Handle set to the active connection handle, High\_Threshold = 0x50, High\_Hysteresis = 0x03 (3dB), Low\_Threshold = 0x4F, Low\_Hysteresis = 0x05 (5 dB). The IUT responds with an HCI\_Command\_Complete with Status = 0x12.
- Note

Note that the RF Test Conditions in [5] provides flexibility in how the IUT's receive power is adjusted, and the means by which the apparent Path Loss is induced in the IUT may vary. An initial condition is chosen such that the apparent Path Loss as seen by the IUT can be varied across the supported Middle and Low Zone boundary.

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends the HCI\_Command\_Complete event with Status = 0x0C to the Upper Tester.

In Steps 3 -6, the IUT sends the HCI\_Command\_Complete event with Status = 0x12 to the Upper Tester.

## 4.10.4 Validate Unsupported Packet Types are Not Accepted

- Test Purpose

Verify that the IUT properly does not support unsupported Packet Types.

- Reference

[12] 7.1.5, 7.1.14, A.5

- Initial Condition
- -Initial Condition as specified in Table 4.40.
- Test Procedure
1. The Upper Tester sends the HCI command as specified in Table 4.40 to the IUT with the Packet\_Type parameter set to the Packet Type as specified in Table 4.40.
2. The IUT sends the HCI\_Command\_Status event to the Upper Tester with Status = Unsupported Feature or Parameter Value (0x11).

Figure 4.101: Validate Unsupported Packet Types are Not Accepted, Create Connection MSC

- Test Case Configuration
- Expected Outcome

Table 4.40: Validate Unsupported Packet Types are Not Accepted test cases

| Test Case | Reference | Initial Condition | HCI Command | Packet Type |
| HCI/CCO/BI-16-C [Validate Unsupported Packet Types are Not Accepted, Change Connection Packet Type, 3-slot] | [12] Section 7.1.14 | The IUT is connected to the Lower Tester. | HCI_Change_Connection_ Packet_Type | 0x0C00 |
| HCI/CCO/BI-17-C [Validate Unsupported Packet Types are Not Accepted, Change Connection Packet Type, 5-slot] | [12] Section 7.1.14 | The IUT is connected to the Lower Tester. | HCI_Change_Connection_ Packet_Type | 0xC000 |

## Pass verdict

In Step 2, the IUT sends the HCI\_Command\_Status event with Status = 0x11 to the Upper Tester.

## 4.10.5 Error Response for Commands not supporting all transports, Command Complete Response

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending commands not supporting all transports on a transport with a handle or connection handle. Also, unsupported events on a transport should not be generated.

- Reference

[12] 3.2

- Initial Condition
- -An ACL connection has been established on the transport as specified in Table 4.41 between the IUT and the Lower Tester.

Figure 4.102: Error Response for Commands not supporting all transports, Command Complete Response MSC

1. The Upper Tester sends the HCI Command and Parameter as specified in Table 4.41.
2. The IUT sends the HCI\_Command\_Complete Event to the Upper Tester with Status = Unsupported Feature or Parameter value (0x11).
- Test Case Configuration

| Test Case | HCI Command | Parameter | Transport |
| HCI/CCO/BI-18-C [Error Response for Commands not supporting all transports, Command Complete Response, Read Authenticated Payload Timeout, BR/EDR] | HCI_Read_Authenticated_ Payload_Timeout | Connection_Handle | BR/EDR |
| HCI/CCO/BI-19-C [Error Response for Commands not supporting all transports, Command Complete Response, Read Authenticated Payload Timeout, LE] | HCI_Read_Authenticated_ Payload_Timeout | Connection_Handle | LE |
| HCI/CCO/BI-20-C [Error Response for Commands not supporting all transports, Command Complete Response, Read Link Quality, BR/EDR] | HCI_Read_Link_Quality | Handle | BR/EDR |
| HCI/CCO/BI-21-C [Error Response for Commands not supporting all transports, Command Complete Response, Read Link Quality, AMP] | HCI_Read_Link_Quality | Handle | AMP |
| HCI/CCO/BI-22-C [Error Response for Commands not supporting all transports, Command Complete Response, Read Link Supervision Timeout, BR/EDR] | HCI_Read_Link_ Supervision_Timeout | Handle | BR/EDR |
| HCI/CCO/BI-25-C [Error Response for Commands not supporting all transports, Command Complete Response, Read RSSI, BR/EDR] | HCI_Read_RSSI | Handle | BR/EDR |
| HCI/CCO/BI-26-C [Error Response for Commands not supporting all transports, Command Complete Response, Read RSSI, AMP] | HCI_Read_RSSI | Handle | AMP |

| Test Case | HCI Command | Parameter | Transport |
| HCI/CCO/BI-27-C [Error Response for Commands not supporting all transports, Command Complete Response, Read RSSI, LE] | HCI_Read_RSSI | Handle | LE |
| HCI/CCO/BI-28-C [Error Response for Commands not supporting all transports, Command Complete Response, Read Transmit Power Level, BR/EDR] | HCI_Read_Transmit_ Power_Level | Connection_Handle | BR/EDR |
| HCI/CCO/BI-29-C [Error Response for Commands not supporting all transports, Command Complete Response, Read Transmit Power Level, LE] | HCI_Read_Transmit_ Power_Level | Connection_Handle | LE |
| HCI/CCO/BI-30-C [Error Response for Commands not supporting all transports, Command Complete Response, Write Authenticated Payload Timeout, BR/EDR] | HCI_Write_Authenticated_ Payload_Timeout | Connection_Handle | BR/EDR |
| HCI/CCO/BI-31-C [Error Response for Commands not supporting all transports, Command Complete Response, Write Authenticated Payload Timeout, LE] | HCI_Write_Authenticated_ Payload_Timeout | Connection_Handle | LE |
| HCI/CCO/BI-32-C [Error Response for Commands not supporting all transports, Command Complete Response, Write Link Supervision Timeout, BR/EDR] | HCI_Write_Link_ Supervision_Timeout | Handle | BR/EDR |

Table 4.41: Error Response for Commands not supporting all transports, Command Complete Response test cases

- Expected Outcome

## Pass verdict

In Step 2, the IUT returns the Status = 0x11 in the HCI\_Command\_Complete Event.

## 4.10.6 Error Response for Commands not supporting all transports, Command Status Response

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending commands not supporting all transports with a handle or connection handle. Also, events not supported on a transport should not be generated.

- Reference

[12] 3.2

- Initial Condition
- -An ACL connection has been established on the transport as specified in Table 4.42 between the IUT and the Lower Tester.

- Test Procedure
1. The Upper Tester sends the HCI Command and Parameter specified in Table 4.42.
2. The IUT sends the HCI\_Command\_Status event to the Upper Tester with Status = Unsupported Feature or Parameter value (0x11).
- Test Case Configuration
- Expected Outcome

Figure 4.103: Error Response for Commands not supporting all transports, Command Status Response MSC

Table 4.42: Error Response for Commands not supporting all transports, Command Status Response test cases

| Test Case | HCI Command | Parameter | Transport |
| HCI/CCO/BI-23-C [Error Response for Commands not supporting all transports, Command Status Response, Read Remote Version Information, BR/EDR] | HCI_Read_Remote_ Version_Information | Connection_Handle | BR/EDR |
| HCI/CCO/BI-24-C [Error Response for Commands not supporting all transports, Command Status Response, Read Remote Version Information, LE] | HCI_Read_Remote_ Version_Information | Connection_Handle | LE |

## Pass verdict

In Step 2, the IUT returns the Status = 0x11 in the HCI\_Command\_Status event.

## HCI/CCO/BI-33-C [Invalid LE Set Periodic Advertising Data Parameters]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending invalid parameters for LE Set Periodic Advertising Data related HCI commands when Periodic Advertising ADI is supported.

- Reference

[13] 7.8.62

- Initial Condition
- -The IUT is in standby.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT using all supported advertising channels and a selected advertising interval between the minimum and maximum advertising intervals supported. The Advertising\_Event\_Properties parameter is set to 0x0000, Own\_Address\_Type is set to 0x00 (Public Device Address),

Primary\_Advertising\_PHY is set to 0x01 (LE 1M), Secondary\_Advertising\_PHY is set to 0x01 (LE 1M) and receives a successful HCI\_Command\_Complete event in return.

2. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 1, using minimum periodic advertising interval and receives a successful HCI\_Command\_Complete event in return.
3. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 1, Operation set to 0x03, and Advertising\_Data\_Length set to 100 using 100 random octets from 1 to 254 as the payload and receives a successful HCI\_Command\_Complete event in return.
4. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 1, Operation set to 0x04.
5. The IUT sends an HCI\_Command\_Complete event with error code Invalid HCI Command Parameters (0x12) to the Upper Tester.
6. The Upper Tester enables periodic advertising using the HCI\_LE\_Set\_Periodic\_Advertising\_Enable command Enable Bit 0 (Periodic Advertising) set to 1 and the Advertising\_Handle set to the Advertising\_Handle in Step 1, and receives a successful HCI\_Command\_Complete event in return.
7. The Upper Tester enables advertising using the HCI\_LE\_Set\_Extended\_Advertising\_Enable command. The Duration[0] parameter is set to 0x0000 (No Advertising Duration).
8. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Operation set to 0x04 and Advertising\_Data\_Length set to 100 using 100 random octets from 1 to 254 as the payload.
9. The IUT sends an HCI\_Command\_Complete event with error code Invalid HCI Command Parameters (0x12) to the Upper Tester.
10. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Operation set to 0x04 and Advertising\_Data\_Length set to 0 and receives a successful HCI\_Command\_Complete event in return.
11. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 1, Operation set to 0x03, and Advertising\_Data\_Length set to 0 and receives a successful HCI\_Command\_Complete event in return.
12. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Data command to the IUT with Advertising\_Handle set to the Advertising\_Handle in Step 1, Operation set to 0x04.
13. The IUT sends an HCI\_Command\_Complete event with error code Invalid HCI Command Parameters (0x12) to the Upper Tester.

## · Expected Outcome

## Pass verdict

In Step 5, the IUT returns an HCI\_Command\_Complete event with the Invalid HCI Command Parameters (0x12) error code.

In Step 9, the IUT returns an HCI\_Command\_Complete event with the Invalid HCI Command Parameters (0x12) error code.

In Step 10, the IUT returns a successful HCI\_Command\_Complete event.

In Step 13, the IUT returns an HCI\_Command\_Complete event with the Invalid HCI Command Parameters (0x12) error code.

## HCI/CCO/BI-34-C [Invalid LE Set Periodic Advertising Enable Parameters, Periodic Advertising ADI Not Supported]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending invalid parameters for LE Set Periodic Advertising Enable related HCI commands when Periodic Advertising ADI is not supported.

- Reference

[13] 7.8.63

- Initial Condition
- -The IUT is in standby. Extended advertising parameters and periodic advertising parameters have been configured on the IUT for a particular advertising handle.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with the Enable bits 0 and 1 set to 1.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to a valid error code.
3. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Enable command to the IUT with Enable bit 0 set to 0 and Enable bit 1 set to 1.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to a valid error code.
- Expected Outcome

## Pass verdict

In Steps 2 and 4, the IUT returns an HCI\_Command\_Complete event with Status set to a valid error code.

## HCI/CCO/BI-35-C [Invalid Set Min Encryption Key Size Parameters]

- Test Purpose

Verify that the IUT properly rejects an unsupported encryption key size.

- Reference

[13] 7.3.102

- Initial Condition
- -TSPX\_min\_encryption\_key\_size is the minimum encryption key size, as defined in the IXIT.
- Test Procedure

Figure 4.104: HCI/CCO/BI-35-C [Invalid Set Min Encryption Key Size Parameters] MSC

1. The Upper Tester sends an HCI\_Set\_Min\_Encryption\_Key\_Size with the Min\_Encryption\_Key\_Size set to TSPX\_min\_encryption\_key\_size -1.
2. The IUT sends an HCI\_Command\_Complete event with the Unsupported Feature or Parameter Value (0x11) error code to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 2, the HCI\_Command\_Complete event has the Unsupported Feature or Parameter Value (0x11) error code.

## Inconclusive verdict

TSPX\_min\_encryption\_key\_size is 0x01, which prevents the Upper Tester from requesting a smaller Min\_Encryption\_Key\_Size.

## 4.10.7 Invalid Subrate Parameters

- Test Purpose

Verify that the IUT properly handles invalid parameters passed in from the Upper Tester. Invalid parameters include when the connection handle is not a valid ACL connection as well as verifying that the parameters are within acceptable ranges.

- Reference

[13] 7.8.123, 7.8.124

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester in the relevant role with a connection interval of 10 ms.
- Test Case Configuration
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Subrate\_Request command to the IUT with a Connection\_Handle that is not an ACL connection.
2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).
3. Repeat Steps 4 and 5 for each round in Table 4.44.
4. The Upper Tester sends the HCI command as specified in Table 4.43 with the parameters as specified in Table 4.44.
5. The IUT sends the Error Event as specified in Table 4.43 to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).

Table 4.43: Invalid Subrate Parameters test cases

| Test Case | HCI Command / Error Event | Perform Steps 1 and 2 | Perform round 9 |
| HCI/CCO/BI-36-C | HCI_LE_Subrate_Request HCI_Command_Status | Yes | Yes |
| HCI/CCO/BI-37-C | HCI_LE_Set_Default_Subrate HCI_Command_Complete | No | No |

| Round | Parameters | Requirement Violated |
| 1 | Subrate_Min = 0 Subrate_Max = 2 Max_Latency = 2 Continuation_Number = 0 Supervision_Timeout = 500 ms | Subrate_Min  1 |
| 2 | Subrate_Min = 4 Subrate_Max = 3 Max_Latency = 2 Continuation_Number = 0 Supervision_Timeout = 500 ms | Subrate_Min  Subrate_Max |
| 3 | Subrate_Min = 501 Subrate_Max = 500 Max_Latency = 500 Continuation_Number = 0 Supervision_Timeout = 500 ms | Subrate_Min  500 |
| 4 | Subrate_Min = 2 Subrate_Max = 501 Max_Latency = 2 Continuation_Number = 0 Supervision_Timeout = 500 ms | Subrate_Max  500 |
| 5 | Subrate_Min = 2 Subrate_Max = 3 Max_Latency = 0x1F4 Continuation_Number = 0 Supervision_Timeout = 500 ms | Max_Latency  0x01F3 |
| 6 | Subrate_Min = 2 Subrate_Max = 0X01F4 Max_Latency = 2 Continuation_Number = 0x01F4 Supervision_Timeout = 500 ms | Continuation_Number  0x01F3 |
| 7 | Subrate_Min = 2 Subrate_Max = 3 Max_Latency = 3 Continuation_Number = 0 Supervision_Timeout = 0x0009 | Supervision_Timeout  0x000A |
| 8 | Subrate_Min = 2 Subrate_Max = 3 Max_Latency = 3 Continuation_Number = 0 Supervision_Timeout = 0x0C81 | Supervision_Timeout  0x0C80 |
| 9 | Subrate_Min = 25 Subrate_Max = 25 Max_Latency = 5 Continuation_Number = 0 Supervision_Timeout = 2 sec (0xC8) | (connInterval current × Subrate_Max × (Max_Latency + 1))× 2 ≤ Supervision_Timeou t |

| Round | Parameters | Requirement Violated |
| 10 | Subrate_Min = 3 Subrate_Max = 5 Max_Latency = 2 Continuation_Number = 5 Supervision_Timeout = 500 ms | Continuation_Number < Subrate_Max |

Table 4.44: Invalid Subrate Parameters rounds

- Expected Outcome

## Pass verdict

In Step 3, the IUT returns an Unknown Connection Identifier (0x02) status.

In Step 5, the IUT returns an Invalid HCI Command Parameters (0x12) status.

## HCI/CCO/BI-38-C [Invalid Connection CTE Request Enable Parameters]

- Test Purpose

Verify that the IUT properly handles invalid parameters passed in from the Upper Tester to the HCI\_LE\_Connection\_CTE\_Request\_Enable command.

- Reference

[13] 7.8.85

- Initial Condition
- -LL connection is established. The IUT is Central or Peripheral.
- -The subrate factor is 3, the continuation number is 0, and the Peripheral latency is 1.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Subrate\_Request to the IUT with Subrate\_Min, Subrate\_Max, and Max\_Latency set as specified in Table 4.45 and receives a successful HCI\_Command\_Status event in return.
2. The IUT sends a successful HCI\_LE\_Subrate\_Change event to the Upper Tester with Subrate\_Factor and Connection\_Latency with the same values as received in Step 1.
3. The Upper Tester sends an HCI\_LE\_Set\_Connection\_CTE\_Receive\_Parameters command to the IUT with the Connection\_Handle set to the current connection handle and receives a successful HCI\_Command\_Complete event in return.
4. Repeat Steps 5, 6, and 7 for CTE\_Request\_Intervals between 1 and 10.
5. The Upper Tester sends an HCI\_LE\_Connection\_CTE\_Request\_Enable command to the IUT with Enable set to 0x01 and CTE\_Request\_Interval.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with error code set to Command Disallowed (0x0C) if the CTE\_Request\_Interval is less than the Acceptable CTE Request Interval in Table 4.45, otherwise the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
7. If the HCI Command Complete in Step 6 is successful, then the Upper Tester sends an HCI\_LE\_Connection\_CTE\_Request\_Enable command to the IUT with Enable set to 0x00 and receives a successful HCI\_Command\_Complete event.

| Round | Subrate Min and Max | Max_Latency | Acceptable CTE Request Interval |
| 1 | 1 | 3 | 4 |
| 2 | 3 | 2 | 9 |
| 3 | 5 | 0 | 5 |

Table 4.45: HCI/CCO/BI-38-C [Invalid Connection CTE Request Enable Parameters] rounds

- Expected Outcome

## Pass verdict

In Step 6, the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester when the CTE\_Request\_Interval in Step 5 is set to a value  Acceptable CTE Request Interval in Table 4.45, otherwise a Command Disallowed (0x0C) error is returned.

## HCI/CCO/BI-39-C [Invalid Write Authenticated Payload Timeout Parameters]

- Test Purpose

Verify that the IUT properly handles invalid parameters passed in from the Upper Tester to the HCI\_Write\_Authenticated\_Payload\_Timeout command.

- Reference

[13] 7.3.94

- Initial Condition
- -LL connection is established. The IUT is Central or Peripheral.
- -The connection interval is 10 ms, subrate factor is 3, continuation number is 0, and the Peripheral latency is 2.
- Test Procedure
1. The Upper Tester sends an HCI\_Write\_Authenticated\_Payload\_Timeout command to the IUT with an Authenticated\_Payload\_Timeout set to 0x0008 (80 ms).
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with any valid error code.
3. The Upper Tester sends an HCI\_Write\_Authenticated\_Payload\_Timeout command to the IUT with an Authenticated\_Payload\_Timeout set to 0x0009 (90 ms).
4. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with any valid error code. The Upper Tester gives a warning if the error code is not Command Disallowed (0x0C).

In Step 4, the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

## HCI/CCO/BI-40-C [LE Set Data Length, Invalid Parameters]

- Test Purpose

Verify that the IUT correctly returns an error when calling the LE\_Set\_Data\_Length command with invalid parameters.

- Reference

[2] 7.8.33

- Initial Condition
- -LL connection established, the IUT is Central or Peripheral.
- Test Procedure

The Upper Tester issues an LE\_Set\_Data\_Length command to the IUT with Tx\_Time set to 17041.

The Upper Tester receives a Command\_Complete event from the IUT with an Invalid Parameters (0x12) error.

Figure 4.105: HCI/CCO/BI-40-C [LE Set Data Length, Invalid Parameters] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command\_Complete event from the IUT with Status = 0x12 (Invalid Parameters).

## HCI/CCO/BI-42-C [Configure Data Path]

- Test Purpose

Verify that the IUT properly handles the Host sending an invalid Data\_Path\_ID.

- Reference

[12] 7.3.101

- Initial Condition
- -An invalid Data Path ID between the Host and the Controller is specified in the TSPX\_Invalid\_Data\_Path\_ID IXIT value.
- -The IXIT parameters are specified in Table 4.46.

| IXIT Parameter | Description |
| TSPX_Invalid_Data_Path_ID | An Invalid Data Path ID |

Table 4.46: Configure Data Path IXIT parameters

- Test Procedure
1. The Upper Tester sends an HCI\_Configure\_Data\_Path command to the IUT with Data\_Path\_ID set to TSPX\_Invalid\_Data\_Path\_ID, Data\_Path\_Direction set to 0x00, and any Vendor\_Specific\_Config\_Length and Vendor\_Specific\_Config.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with error code Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

In Step 2, the Upper Tester receives an HCI\_Command\_Complete event with error code Invalid HCI Command Parameters (0x12).

## HCI/CCO/BI-43-C [LE Read Channel Map -Reject Invalid Handle]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an invalid ACL handle for LE Read Channel Map HCI command.

- Reference

[13] 7.8.20

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The IUT acts in Peripheral or Central role.
- Test Procedure
1. The Upper Tester issues an HCI\_LE\_Read\_Channel\_Map command to the IUT with the Connection\_Handle parameter set to a different value than the established connection's handle.
2. The IUT sends the HCI\_Command\_Complete event with the Status = Unknown Connection Identifier (0x02) to the Upper Tester.

Figure 4.106: HCI/CCO/BI-43-C [LE Read Channel Map -Reject Invalid Handle] MSC

- Expected Outcome

## Pass verdict

In Step 2, the IUT returns the Status = Unknown Connection Identifier (0x02) to the Upper Tester.

## 4.10.8 Reject Setting Host Controlled FeatureSet Bit, Unsupported Feature on Controller

- Test Purpose

Verify that the IUT properly rejects the Upper Tester setting a Host Controlled FeatureSet bit for a feature not supported on the Controller.

- Reference

[12] 7.8.115

[13] 4.6

- Initial Condition
- -The FeatureSet Bit in Table 4.47 is clear.
- -The IUT is not connected to the Lower Tester.
- Test Case Configuration

| Test Case | FeatureSet Bit |
| HCI/CCO/BI-44-C | 32 (Connected Isochronous Streams (Host Support)) |
| HCI/CCO/BI-45-C | 38 (Connection Subrating (Host Support)) |
| HCI/CCO/BI-121-C | 41 (Advertising Coding Selection (Host Support)) |
| HCI/CCO/BI-122-C | 47 (Channel Sounding (Host Support)) |
| HCI/CCO/BI-133-C | 72 (Shorter Connection Intervals (Host Support)) |

Table 4.47: Reject Setting Host Controlled FeatureSet Bit, Unsupported Feature on Controller test cases

- Test Procedure
1. The Upper Tester sends the HCI\_LE\_Set\_Host\_Feature command to the IUT with Bit\_Number set to the FeatureSet Bit in Table 4.47 and Bit\_Value set to 1.
2. The IUT sends the HCI\_Command\_Complete event to the Upper Tester with Status set to Unsupported Feature or Parameter value (0x11).
- Expected Outcome

Figure 4.107: Reject Setting Host Controlled FeatureSet Bit, Unsupported Feature on Controller MSC

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unsupported Feature or Parameter value (0x11).

## 4.10.9 LE Add Device To Resolving List

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an invalid entry for an LE Add Device To Resolving List HCI command.

- Reference

[13] 7.8.38

- Initial Condition
- -None.
- Test Case Configuration

| Test Case | Parameters | HCI Command (in Step 5) | Expected Status / Result (in Step 6) |
| HCI/CCO/BI-46-C [LE Add Device To Resolving List - Duplicate Entry] | Peer_Identity_Address_Type, Peer_Identity_Address, Peer_IRK, Local_IRK | No command | N/A |
| HCI/CCO/BI-47-C [LE Add Device To Resolving List - Existing Peer IRK Entry] | Peer_Identity_Address_Type2, Peer_Identity_Address, Peer_IRK, Local_IRK | HCI_LE_Remove_ Device_From_ Resolving_List | Status = Unknown Connection Identifier (0x02) |
| HCI/CCO/BI-48-C [LE Add Device To Resolving List - Existing Peer IRK Entry] | Peer_Identity_Address_Type, Peer_Identity_Address2, Peer_IRK, Local_IRK | HCI_LE_Remove_ Device_From_ Resolving_List | Status = Unknown Connection Identifier (0x02) |

Table 4.48: LE Add Device To Resolving List test cases

## · Test Procedure

Figure 4.108: LE Add Device To Resolving List MSC

1. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Resolving\_List command to the IUT with a valid peer device identity.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success').
3. Repeat Step 1, with parameters as listed in Table 4.48.
4. The IUT sends the HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') or Status set to any valid error code.
5. The Upper Tester sends an HCI command, if specified and as listed in Table 4.48, to the IUT with the corresponding parameters added in Step 4.
6. Perform either alternative 6A or 6B depending on the Status in Step 4.

Alternative 6A (The Status is set to any valid error code):

- 6A.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester, with Status (and Result) as listed in Table 4.48.

Alternative 6B (The Status is set to 0x00):

- 6B.1 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
- Expected Outcome

## Pass verdict

The entry added in Step 4 is not added to the resolving list, and the Result in Step 6 is as indicated in Table 4.48.

## HCI/CCO/BI-50-C [LE Add Device To Resolving List -No Space Available, Scanner]

- Test Purpose

Verify that the scanner IUT properly handles the Upper Tester sending too many entries for an LE Add Device To Resolving List HCI command.

- Reference

[13] 7.8.38

- Initial Condition

Figure 4.109: HCI/CCO/BI-50-C [LE Add Device To Resolving List -No Space Available] MSC

1. The Upper Tester sends an HCI\_LE\_Read\_Resolving\_List\_Size command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') and the number of entries in the resolving list.
3. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Resolving\_List command to the IUT, with Peer\_Identity\_Address\_Type set to 0x01, Peer\_Identity\_Address set to a valid peer device identity, and Peer\_IRK set to the corresponding IRK.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') or 0x07 ('Memory Capacity Exceeded'), in which case, continue with Step 10.
5. Repeat Steps 3 and 4 with a different address and IRK until it adds (Resolving\_List\_Size (from Step 2) value + 1) entries, or until the IUT sends to the Upper Tester an HCI\_Command\_Complete event with Status = 0x07 ('Memory Capacity Exceeded').
6. Repeat Steps 1 and 2.
7. If the number of entries added in the resolving list (Step 3) is lower than the Resolving\_List\_Size value received in Step 6, repeat from Step 3; this indicates that the controller modified the resolving list size.
8. If the number of entries added in the resolving list (Step 3) is equal to the Resolving\_List\_Size value received in Step 6 and the IUT doesn't return Status set to 0x07 in Step 5, the test fails and stops.
9. The Upper Tester sends an HCI\_LE\_Set\_Address\_Resolution\_Enable command to the IUT.
10. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') .
11. The Upper Tester sends an HCI\_LE\_Set\_Scan\_Parameters command to the IUT.
12. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') .
13. The Upper Tester sends an HCI\_LE\_Set\_Scan\_Enable command to the IUT with the LE\_Scan\_Enable field set to 0x01.
14. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') .
15. The Lower Tester is configured to send ADV\_IND advertising packets with an advertising interval of 50 ms and the AdvA set to a resolvable private address generated using one of the IRKs in Step 3.
16. The Lower Tester advertises for 500 ms or until an HCI\_LE\_Advertising\_Report is sent from the IUT to the Upper Tester with AdvA set to the Identity Address corresponding to the IRK used in Step 15.
17. Repeat Steps 15 and 16 until each of the IRKs in Step 3 has been advertised in Step 15.
18. The Upper Tester sends HCI\_LE\_Read\_Peer\_Resolvable\_Address commands to the IUT, consecutively requesting all the entries successfully added in Step 3 (Peer\_Identity\_Address\_Type and Peer\_Identity\_Address parameters are set consecutively to the values used in Step 3).
19. For each of the commands in Step 18, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') and the Peer\_Resolvable\_Address set to the correct advertised Address used in Step 15 by the Lower Tester corresponding to the IRK set in Step 3.

- Expected Outcome

## Pass verdict

When the IUT cannot add any more entries in the resolving list, in Step 5 the IUT sends an HCI\_Command\_Complete event with Status set to 0x07 ('Memory Capacity Exceeded') to the Upper Tester.

All the resolving list entries that the IUT returns in Step 17 are those added in Step 3 for which the IUT returned Status set to 0x00.

## 4.10.10 LE Add Device To Resolving List -No Space Available, Advertiser

- Test Purpose

Verify that the advertiser IUT properly handles the Upper Tester sending too many entries for an LE Add Device To Resolving List HCI command.

- Reference

[13] 7.8.38

- Initial Condition
- -The advertiser IUT is configured in a standby state.
- Test Case Configuration

| Test Case | Advertising Type |
| HCI/CCO/BI-69-C [LE Add Device To Resolving List - No Space Available, Advertiser, Connectable] | ADV_IND (0x00) |
| HCI/CCO/BI-70-C [LE Add Device To Resolving List - No Space Available, Advertiser, Non-Connectable] | ADV_SCAN_IND (0x02) |

Table 4.49: LE Add Device To Resolving List -No Space Available, Advertiser test cases

·

Figure 4.110: LE Add Device To Resolving List -No Space Available, Advertiser MSC

1. The Upper Tester sends an HCI\_LE\_Read\_Resolving\_List\_Size command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') and the number of entries in the resolving list.
3. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Resolving\_List command to the IUT, with Peer\_Identity\_Address\_Type set to 0x01, Peer\_Identity\_Address set to a valid peer device identity, and Peer\_IRK set to the corresponding IRK.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success') or 0x07 ('Memory Capacity Exceeded'), in which case, continue with Step 9.
5. Repeat Steps 3 and 4 with a different address and IRK until it adds (Resolving\_List\_Size (from Step 2) value + 1) entries, or until the IUT sends to the Upper Tester an HCI\_Command\_Complete event with Status = 0x07 ('Memory Capacity Exceeded').
6. Repeat Steps 1 and 2.
7. If the number of entries added in the resolving list (Step 3) is less than or equal to the Resolving\_List\_Size value received in Step 6, repeat from Step 3; this indicates that the controller modified the resolving list size.
8. If the number of entries added in the resolving list (Step 3) is greater than the Resolving\_List\_Size value received in Step 6 and the IUT doesn't return Status set to 0x07 in Step 5, the test fails and stops.
9. The Upper Tester sends an HCI\_LE\_Set\_Address\_Resolution\_Enable command to the IUT.
10. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 ('Success').
11. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Parameters command to the IUT with Advertising\_Type set as specified in Table 4.49 and Advertising\_Filter\_Policy set to 0x03 and receives a successful HCI\_Command\_Complete event in response.
12. The Upper Tester sends an HCI\_LE\_Set\_Scan\_Response\_Data command to the IUT with Scan\_Response\_Data\_Length set to 1 and Scan\_Response\_Data set to one random octet and receives a successful HCI\_Command\_Complete event in response.

Perform Steps 13 -19 for each of the IRKs in Step 3.

13. The Upper Tester sends an HCI\_LE\_Add\_Device\_To\_Filter\_Accept\_List command to the IUT with Address set to the peer address corresponding to the IRK and receives a successful HCI\_Command\_Complete event in response.
14. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Enable command to the IUT enabling advertising and receives a successful HCI\_Command\_Complete event in response.
15. The IUT starts sending the advertising type PDUs specified in Table 4.49 to the Lower Tester.
16. The Lower Tester sends a SCAN\_REQ PDU to the IUT with AdvA set to a resolvable private address generated using the IRK.
17. The IUT sends a SCAN\_RSP PDU to the Lower Tester with ScanRspData set to the advertising data from Step 12.
18. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Enable command to the IUT disabling advertising and receives a successful HCI\_Command\_Complete event in response.
19. The Upper Tester sends an HCI\_LE\_Clear\_Filter\_Accept\_List command and receives a successful HCI\_Command\_Complete event in response.
- Expected Outcome

## Pass verdict

When the IUT cannot add any more entries in the resolving list, in Step 5 the IUT sends an HCI\_Command\_Complete event with Status set to 0x07 ('Memory Capacity Exceeded') to the Upper Tester.

In Step 17, the IUT sends a SCAN\_RSP PDU in response to Step 16 for each of the IRKs in Step 3.

## 4.10.11 Reject Invalid Create Connection Command

- Test Purpose

Verify that the IUT properly rejects a create connection command when the LE Random Device Address is unset, and it returns the expected error code.

- Initial Condition
- -The IUT is in Initiating State.
- -The IUT has not set its LE Random Device Address.
- Test Case Configuration
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT with Own\_Address\_Type and Initiator\_Filter\_Policy set to the values in Table 4.50. Set all other fields to valid values.
2. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status event response.

Table 4.50: Reject Invalid Create Connection Command test cases

| Test Case | Own_Address_Type | Initiator_Filter_Policy |
| HCI/CCO/BI-51-C | 0x01 | NA |
| HCI/CCO/BI-52-C | 0x03 | 0x00 |
| HCI/CCO/BI-53-C | 0x03 | 0x01 |

Figure 4.111: Reject Invalid Create Connection Command MSC

Alternative 2A (The IUT returns an HCI\_Command\_Status event with an error code):

- 2A.1 The IUT returns an HCI\_Command\_Status event with the error code Invalid HCI Command Parameters (0x12).

Alternative 2B (The IUT returns a successful HCI\_Command\_Status event):

- 2B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2B.2 The IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester with the error code Invalid HCI Command Parameters (0x12).

- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT sends an HCI\_Command\_Status event to the Upper Tester with a status of Invalid HCI Command Parameters (0x12).

In Step 2B.2, the IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester with a status of Invalid HCI Command Parameters (0x12).

## 4.10.12 Reject Invalid Extended Create Connection Command

- Test Purpose

Verify that the IUT properly rejects an extended create connection command when the LE Random Device Address is unset, and it returns the expected error code.

- Initial Condition
- -The IUT is in Initiating State.
- -The IUT has not set its LE Random Device Address.
- Test Case Configuration
- Test Procedure

Table 4.51: Reject Invalid Extended Create Connection Command test cases

| Test Case | Own_Address_Type | Initiator_Filter_Policy |
| HCI/CCO/BI-54-C | 0x01 | NA |
| HCI/CCO/BI-55-C | 0x03 | 0x00 |
| HCI/CCO/BI-56-C | 0x03 | 0x01 |

Figure 4.112: Reject Invalid Extended Create Connection Command MSC

1. The Upper Tester sends an HCI\_LE\_Extended\_Create\_Connection command to the IUT with Own\_Address\_Type and Initiator\_Filter\_Policy set to the values in Table 4.51. Set all other fields to valid values.
2. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status event response.

Alternative 2A (The IUT returns an HCI\_Command\_Status event with an error code):

- 2A.1 The IUT returns an HCI\_Command\_Status event with the error code Invalid HCI Command Parameters (0x12).

Alternative 2B (The IUT returns a successful HCI\_Command\_Status event):

- 2B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2B.2 The IUT sends an HCI\_LE\_Enhanced\_Connection\_Complete event to the Upper Tester with the error code Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

In Step 2A.1, the IUT sends an HCI\_Command\_Status event to the Upper Tester with a status of Invalid HCI Command Parameters (0x12).

In Step 2B.2, the IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester with a status of Invalid HCI Command Parameters (0x12).

## 4.10.13 LE Setup ISO Data Path

- Test Purpose

Verify that the IUT properly handles when the Host sends the LE\_Setup\_ISO\_Data\_Path command twice before sending the LE\_Remove\_ISO\_Data\_Path command. Also verify that the IUT properly handles invalid Host parameters for Codec\_Configuration\_Length and Codec\_ID.

- Reference

[12] 7.8.109

- Initial Condition

## CIS

- -A CIS has been established using the values specified in [14] Section 4.11.2, Default Values for Common Parameters.

## BIS Isochronous Broadcaster

- -The Isochronous Broadcaster IUT has created a BIS with the Lower Tester synchronized to the BIS.
- -The IXIT parameters are specified in Table 4.52.

## BIS Synchronized Receiver

- -The Synchronized Receiver IUT is synchronized with the Lower Tester broadcasting a BIS.
- -The IXIT parameters are specified in Table 4.52.

| IXIT Parameter | Description |
| TSPX_Data_Path_ID_CIS | CIS Data Path ID |
| TSPX_Data_Path_ID_BIS_Broadcaster | BIS Broadcaster Data Path ID |
| TSPX_Data_Path_ID_BIS_Receiver | BIS Receiver Data Path ID |
| TSPX_Number_Supported_Standard_Codecs_BR_EDR | Number of Standard Codecs, BR/EDR |

Table 4.52: LE Setup ISO Data Path IXIT Parameters

| IXIT Parameter | Description |
| TSPX_Number_Supported_Standard_Codecs_All_PHYs | Number of Standard Codecs, All PHYs |
| TSPX_Number_Supported_Vendor_Codecs_BR_EDR | Number of Vendor Specific Codecs, BR/EDR |
| TSPX_Number_Supported_Vendor_Codecs_All_PHYs | Number of Vendor Specific Codecs, All PHYs |
| TSPX_Codec_ID_CIS | CIS Codec ID |
| TSPX_Codec_ID_BIS_Broadcaster | BIS Broadcaster Codec ID |
| TSPX_Codec_ID_BIS_Receiver | BIS Receiver Codec ID |
| TSPX_Direction | Direction |
| TSPX_Codec_Configuration_CIS | CIS Codec Configuration |
| TSPX_Codec_Configuration_BIS_Broadcaster | BIS Broadcaster Codec Configuration |
| TSPX_Codec_Configuration_BIS_Receiver | BIS Receiver Codec Configuration |
| TSPX_Data_Path_Configuration | Vendor-specific data path configuration |

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends the HCI\_Read\_Local\_Supported\_Codecs [v2] command to the IUT.
2. The IUT responds with a successful HCI\_Command\_Complete event.
3. The Lower Tester verifies that the returned value of Num\_Supported\_Standard\_Codecs equals TSPX\_Number\_Supported\_Standard\_Codecs\_All\_PHYs, and the returned value of Num\_Supported\_Vendor\_Specific\_Codecs equals TSPX\_Number\_Supported\_Vendor\_Codecs\_All\_PHYs. The Lower Tester also verifies that one

Table 4.53: LE Setup ISO Data Path test cases

| Test Case | HCI/CCO/BI-57-C [LE Setup ISO Data Path, CIS] | HCI/CCO/BI-58-C [LE Setup ISO Data Path, BIS, Isochronous Broadcaster] | HCI/CCO/BI-62-C [LE Setup ISO Data Path, BIS, Synchronized Receiver] |
| ISOC Stream Type | CIS | BIS Isochronous Broadcaster | BIS Synchronized Receiver |
| Perform Steps 4 and 5 | Yes | Yes | No |
| Perform Steps 6 and 7 | Yes | No | Yes |
| Codec_ID | TSPX_Codec_ID_CIS | TSPX_Codec_ID_BIS_ Broadcaster | TSPX_Codec_ID_BIS_ Receiver |
| Direction | TSPX_Direction | 0 | 1 |
| Logical_Transport_Type | 0x02 (LE CIS) | 0x03 (LE BIS) | 0x03 (LE BIS) |
| Codec_Configuration | TSPX_Codec_ Configuration_CIS | TSPX_Codec_ Configuration_BIS_Broadcaster | TSPX_Codec_ Configuration_BIS_ Receiver |
| Data_Path_ID | TSPX_Data_Path_ID_CIS | TSPX_Data_Path_ID_ BIS_Broadcaster | TSPX_Data_Path_ID_ BIS_Receiver |

of the supported codecs (either standard or vendor-specific) has the Codec\_ID and Logical\_Transport\_Type specified in Table 4.53.

Perform Steps 4 and 5 if specified in Table 4.53.

4. The Upper Tester sends an HCI\_Read\_Local\_Supported\_Codec\_Capabilities command to the IUT with Codec\_ID and Logical\_Transport\_Type specified in Table 4.53, and Direction set to 0x00.
5. The IUT either sends a successful HCI\_Command\_Complete event with Num\_Codec\_Capabilities, Codec\_Capability\_Length, and Codec\_Capability or sends an HCI\_Command\_Complete event with Status &gt; 0x00.

Perform Steps 6 and 7 if specified in Table 4.53.

6. The Upper Tester sends an HCI\_Read\_Local\_Supported\_Codec\_Capabilities command to the IUT with Codec\_ID and Logical\_Transport\_Type specified in Table 4.53, and Direction set to 0x01.
7. The IUT either sends a successful HCI\_Command\_Complete event with Num\_Codec\_Capabilities, Codec\_Capability\_Length, and Codec\_Capability or sends an HCI\_Command\_Complete event with Status &gt; 0x00.
8. If both Steps 5 and 7 returned an error, or if only one of these steps was performed and returned an error, then the test ends with a Fail verdict. Otherwise, if either Step 5 or 7 was not run, returned an error, or succeeded and returned Num\_Codec\_Capabilities = 0, then the test ends with a Pass verdict.
9. The Upper Tester sends an HCI\_Read\_Local\_Supported\_Controller\_Delay command to the IUT with Codec\_ID, Logical\_Transport\_Type, Direction, and Codec\_Configuration set as specified in Table 4.53, and Codec\_Configuration\_Length set to the length of Codec\_Configuration.
10. The IUT responds with a successful HCI\_Command\_Complete event with Min\_Controller\_Delay and Max\_Controller\_Delay set to a value between 0x000000 and 0x3D0900 and Max\_Controller\_Delay  Min\_Controller\_Delay.
11. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the Data\_Path\_Direction, Codec\_ID, Codec\_Configuration\_Length, and Codec\_Configuration parameters set to the values used in Step 9, Controller\_Delay set to the mean of Min\_Controller\_Delay and Max\_Controller\_Delay returned in Step 10, and Data\_Path\_ID set as specified in Table 4.53.
12. If the Data\_Path\_ID is zero, then the IUT responds with a successful HCI\_Command\_Complete event, and skip Steps 13 and 14. Otherwise, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with a Command Disallowed (0x0C) error code.
13. The Upper Tester sends an HCI\_Configure\_Data\_Path command to the IUT with Data\_Path\_Direction and Data\_Path\_ID set as specified in Table 4.53 and Vendor\_Specific\_Config\_Length and Vendor\_Specific\_Config set to the length and value of TSPX\_Data\_Path\_Configuration (the length may be zero if there is no configuration required) and receives a successful HCI\_Command\_Complete in return.
14. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the Data\_Path\_Direction, and Data\_Path\_ID, Codec\_ID, Controller\_Delay, Codec\_Configuration\_Length, and Codec\_Configuration parameters set to the values used in Step 11, and the IUT responds with a successful HCI\_Command\_Complete event.
15. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the Data\_Path\_Direction, and Data\_Path\_ID, Codec\_ID, Controller\_Delay, Codec\_Configuration\_Length, and Codec\_Configuration parameters set to the values used in Step 11, and the IUT responds with an HCI\_Command\_Complete event with error code Command Disallowed (0x0C).

16. The Upper Tester sends an HCI\_LE\_Remove\_ISO\_Data\_Path command to the IUT with an invalid connection handle, and the IUT responds with error code Unknown Connection Identifier (0x02).
17. The Upper Tester sends an HCI\_LE\_Remove\_ISO\_Data\_Path command to the IUT with the Data\_Path\_Direction parameter the same as in Step 11, and the IUT responds with a successful HCI\_Command\_Complete event.
18. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the Codec\_Configuration\_Length &gt; 0 and Codec\_ID set to Transparent Air mode, the remaining parameters set to the values used in Step 11, and the IUT responds with an HCI\_Command\_Complete event with error code Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

In Step 12, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with error code Command Disallowed (0x0C) if TSPX\_Data\_Path\_ID is not zero.

In Step 14, the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

In Step 16, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with error code Unknown Connection Identifier (0x02).

In Step 15, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with error code Command Disallowed (0x0C).

In Step 18, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with error code Invalid HCI Command Parameters (0x12).

## HCI/CCO/BI-59-C [Invalid LE Set Periodic Advertising Receive Enable Parameters, Periodic Advertising ADI Not Supported]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending invalid parameters for LE Set Periodic Advertising Receive Enable related HCI commands when Periodic Advertising ADI is not supported.

- Reference

[13] 7.8.88

- Initial Condition
- -The IUT is in standby. Extended advertising parameters and periodic advertising parameters have been configured on the IUT for a particular advertising handle.
- -The IUT has synced to the Lower Tester Periodic Advertising.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Receive\_Enable command to the IUT with the Enable bits 0 and 1 set to 1.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with an error code.
- Expected Outcome

## Pass verdict

In Step 2, the IUT returns an HCI\_Command\_Complete event with Status set to an error code.

## 4.10.14 Invalid LE Set Periodic Advertising Sync Transfer Parameters, Periodic Advertising ADI Not Supported

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending invalid parameters for the LE Set Periodic Advertising Sync Transfer Parameters or LE Set Default Periodic Advertising Sync Transfer Parameters command when Periodic Advertising ADI is not supported.

- Reference

[13] 7.8.91, 7.8.92

- Initial Condition
- -State: Connected
- -Extended advertising parameters and periodic advertising parameters have been configured on the IUT.
- Test Case Configuration
- Test Procedure
1. The Upper Tester sends the HCI command as specified in Table 4.54 to the IUT with Mode set to 0x03 and all other parameters set to valid values.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with an error code.
- Expected Outcome

Table 4.54: Invalid LE Set Periodic Advertising Sync Transfer Parameters, Periodic Advertising ADI Not Supported test cases

| Test Case | HCI Command |
| HCI/CCO/BI-60-C [Invalid LE Set PAST Parameters, PA ADI Not Supported] | HCI_LE_Set_Periodic_Advertising_Sync_Transfer_Parameters |
| HCI/CCO/BI-61-C [Invalid LE Set Default PAST Parameters, PA ADI Not Supported] | HCI_LE_Set_Default_Periodic_Advertising_Sync_Transfer_Parameters |

## Pass verdict

In Step 2, the IUT returns an HCI\_Command\_Complete event with Status set to an error code.

## HCI/CCO/BI-63-C [LE Extended Create Connection [v2], Invalid Parameters]

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Extended Create Connection [v2] command.

- Reference

[17] 7.8.66

- Initial Condition
- -The IUT enables Periodic Advertising with Responses using Advertising Handle = 0x00.

- Test Procedure

Repeat Steps 1 -2 for each round in Table 4.55.

1. The Upper Tester sends the HCI\_LE\_Extended\_Create\_Connection [v2] command with the parameters specified in Table 4.55.
2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set as specified in Table 4.55.
- Expected Outcome

Table 4.55: LE Extended Create Connection [v2], Invalid Parameters test rounds

| Round | Parameter | Status |
| 1 | Advertising_Handle = 0x01 | Unknown Advertising Identifier (0x42) |
| 2 | Subevent = 0x80 | Invalid HCI Command Parameters (0x12) |
| 3 | Advertising_Handle = 0xFF Subevent = 1 | Invalid HCI Command Parameters (0x12) |
| 4 | Min_CE_Length > Max_CE_Length | Invalid HCI Command Parameters (0x12) |

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Status event with the error specified in Table 4.55.

## 4.10.15 LE Set Periodic Advertising Parameters, Invalid Parameters

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Set Periodic Advertising Parameters [v2] command.

- Reference

[17] 7.8.61

- Initial Condition
- -There is a valid advertising set configured on the IUT.
- Test Case Configuration
- Test Procedure

Table 4.56: LE Set Periodic Advertising Parameters, Invalid Parameters test cases

| Test Case | HCI Command | Rounds |
| HCI/CCO/BI-64-C | HCI_LE_Set_Periodic_Advertising_Parameters [v1] | 1 - 2 |
| HCI/CCO/BI-65-C | HCI_LE_Set_Periodic_Advertising_Parameters [v2] | All |

Repeat the steps specified in Table 4.56 for each round in Table 4.57.

1. The Upper Tester sends the HCI command specified in Table 4.56 with the parameters specified in Table 4.57.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set as specified in Table 4.57.

| Round | Parameter | Status |
| 1 | Advertising_Handle = set to unknown handle, all others set to valid values | Unknown Advertising Identifier (0x42) |
| 2 | Periodic_Advertising_Interval_Min > Periodic_Advertising_Interval_Max, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 3 | Subevent_Interval > Periodic_Advertising_Interval_Min / Num_Subevents, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 4 | Response_Slot_Delay >= Subevent_Interval, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 5 | Response_Slot_Delay = 0x00 Num_Response_Slots > 0, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 6 | Response_Slot_Spacing > 10x(Subevent_Interval - Response_Slot_Delay) / Num_Response_Slots, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 7 | Num_Subevents > 0x80, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 8 | Num_Subevents > 1, Subevent_Interval < 0x06, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 9 | Response_Slot_Delay = 0xFF, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 10 | Response_Slot_Spacing = 0x01, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 11 | Num_Response_Slots = 0, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 12 | Subevent_Interval = 24 (30 ms) Response_Slot_Delay = 12 (15 ms) Num_Response_Slots = 5 Response_Slot_Spacing = 25 (3.125 ms) | Invalid HCI Command Parameters (0x12) |
| 13 | Num_Subevents = 0 Subevent_Interval = 0x05 Response_Slot_Delay = 0xFF Response_Slot_Spacing = 0x01 Num_Response_Slots = 0x00 | Success (0x00) |
| 14 | Num_Subevents = 1, Subevent_Interval < 0x06, all others set to valid values | Success (0x00) |

Table 4.57: LE Set Periodic Advertising Parameters, Invalid Parameters test rounds

## · Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event with the error specified in Table 4.57.

## HCI/CCO/BI-66-C [LE Set Periodic Advertising Response Data, Invalid Parameters]

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Set Periodic Advertising Response Data command.

- Reference

[17] 7.8.126

- Initial Condition
- -The IUT is scanning for Periodic Advertising and is synchronized with the Lower Tester periodic advertising with response.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Sync\_Subevent to the IUT with Subevent set to 0.

Repeat Steps 2 -4 for each round in Table 4.58.

2. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Report [v2] event to the Upper Tester with Subevent set to 0x00.
3. The Upper Tester sends the HCI\_LE\_Set\_Periodic\_Advertising\_Response\_Data command with the parameters specified in Table 4.58.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set as specified in Table 4.58.
5. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Terminate\_Sync command to the IUT and receives a successful HCI\_Command\_Complete event in response.

| Round | Parameter | Status |
| 1 | Sync_Handle > 0x0EFF, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 2 | Response_Data_Length > max that controller can transmit | Packet Too Long (0x45) |
| 3 | Response_Slot has passed by the time this command is received by the Controller | TooLate (0x46) |
| 4 | Response_Data_Length = 255, Response_Data truncated to 247 bytes, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 5 | Response_Subevent set to 5 (above numSubevents), all others set to valid values | Command Disallowed (0x0C) |
| 6 | Response_Subevent set to 2 (subevent not synced), all others set to valid values | Command Disallowed (0x0C) |

Table 4.58: LE Set Periodic Advertising Response Data, Invalid Parameters test rounds

- Expected Outcome

## Pass verdict

In Step 4, the IUT sends an HCI\_Command\_Complete event with the error specified in Table 4.58.

## 4.10.15.1 LE Set Periodic Advertising Subevent Data, Invalid Parameters

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Set Periodic Advertising Subevent Data command.

- Reference

[17] 7.8.125

- Initial Condition
- -The IUT is in standby mode.
- Test Case Configuration

| Test Case | Execute Step 3 |
| HCI/CCO/BI-67-C [LE Set Periodic Advertising Subevent Data, Invalid Parameters, v5.4 or earlier] | No |
| HCI/CCO/BI-124-C [LE Set Periodic Advertising Subevent Data, Invalid Parameters, v6.0 or later] | Yes |

Table 4.59: LE Set Periodic Advertising Subevent Data, Invalid Parameters test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT using all supported advertising channels and a selected advertising interval between the minimum and maximum advertising intervals supported and receives a successful HCI\_Command\_Complete event in return. The Advertising\_Event\_Properties parameter is set to 0x0000, Primary\_Advertising\_PHY is set to 0x01 (LE 1M), and Secondary\_Advertising\_PHY is set to 0x01 (LE 1M).
2. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Parameters [v2] command to the IUT with Num\_Subevents\_With\_Data set to 10, Subevent\_Interval set to 0xFF (318.75 ms), Response\_Slot\_Delay set to 0x01 (1.25 ms), Response\_Slot\_Spacing set to 0x0A (1.25 ms), and Num\_Response\_Slots set to 0x05, and receives a successful HCI\_Command\_Complete event in response.
3. Execute Step 3 if specified in Table 4.59.
- 3a. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command to the IUT with Subevent\_Data\_Length set to 1.
- 3b. The IUT sends an HCI\_Command\_Complete event with Status &gt; 0.
4. The Upper Tester enables periodic advertising with Periodic Advertising Filtering using the HCI\_LE\_Set\_Periodic\_Advertising\_Enable command with bit 0 (Enable periodic advertising) and receives an HCI\_Command\_Complete event in response.
5. The Upper Tester enables advertising using the HCI\_LE\_Set\_Extended\_Advertising\_Enable command with the Duration[0] parameter set to 0x0000 (No Advertising Duration), and receives an HCI\_Command\_Complete event in response.

Repeat Steps 6 -8 for each round in Table 4.60. In round 10, repeat Step 6 until Subevent\_Data\_Count is greater than 1. If this doesn't happen within 10 periodic advertising events, then skip round 10.

6. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Subevent\_Data\_Request event to the Upper Tester with Subevent\_Start and Subevent\_Data\_Count.

7. The Upper Tester sends the HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command with the parameters specified in Table 4.60.
8. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set as specified in Table 4.60.
9. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Subevent\_Data\_Request event to the Upper Tester with Subevent\_Start and Subevent\_Data\_Count.
10. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command to the IUT with Num\_Subevents\_With\_Data set to 1 and Subevent set to Subevent\_Start from Step 9.
11. The IUT sends a successful HCI\_Command\_Complete event to the IUT.
12. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Subevent\_Data command to the IUT with Num\_Subevents\_With\_Data set to 1 and Subevent set to Subevent\_Start from Step 9.
13. The IUT sends an HCI\_Command\_Complete event to the IUT with Status &gt; 0.

Table 4.60: LE Set Periodic Advertising Subevent Data, Invalid Parameters test rounds

| Round | Parameter | Status |
| 1 | Advertising_Handle = set to unknown handle, all others set to valid values | Unknown Advertising Identifier (0x42) |
| 2 | Advertising_Handle > 0xEF, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 3 | Subevent_Data > max that controller can transmit | Packet Too Long (0x45) |
| 4 | Num_Subevents_With_Data = 0x00, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 5 | Num_Subevents_With_Data > 0x0F, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 6 | Subevent[0] > 0x7F, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 7 | Subevent[0] < Subevent_Start (Step 6) OR (Subevent_Start + Subevent_Data_Count) < Subevent[0] < 0x7F, all others set to valid values | Command Disallowed (0x0C) |
| 9 | Response_Slot_Start[0] = 6 | Invalid HCI Command Parameters (0x12) |
| 10 | Num_Subevents_With_Data = 2 Subevent[0] = Subevent_Start Subevent[1] = Subevent_Start Subevent_Data_Length[0] = 1 Subevent_Data[0] = 0x01 Subevent_Data_Length[1] = 1 Subevent_Data[1] = 0x01 | Invalid HCI Command Parameters (0x12) |

## · Expected Outcome

## Pass verdict

In Step 3b, the IUT sends an HCI\_Command\_Complete event with an error code.

In Step 8, the IUT sends an HCI\_Command\_Complete event with the error specified in Table 4.60.

In Step 13, the IUT sends an HCI\_Command\_Complete event with an error code.

## HCI/CCO/BI-68-C [LE Set Periodic Sync Subevent, Invalid Parameters]

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Set Periodic Sync Subevent command.

- Reference

[17] 7.8.127

- Initial Condition
- -The IUT is scanning for Periodic Advertising and is synchronized with the Lower Tester.

## · Test Procedure

Repeat Steps 1 -2 for each round in Table 4.61.

1. The Upper Tester sends the HCI\_LE\_Set\_Periodic\_Sync\_Subevent command with the parameters specified in Table 4.61.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set as specified in Table 4.61.
- Expected Outcome

Table 4.61: LE Set Periodic Sync Subevent, Invalid Parameters test rounds

| Round | Parameter | Event and Status/Error Code |
| 1 | Sync_Handle > 0x0EFF, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 2 | Num_Subevents_To_Sync = 0x00, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 3 | Num_Subevents_To_Sync > 0x80, all others set to valid values | Invalid HCI Command Parameters (0x12) |
| 4 | Num_Subevents_To_Sync > Number of Subevent from HCI_LE_Periodic_Advertising_Sync_Established [v2] | Invalid HCI Command Parameters (0x12) |
| 5 | Subevent[0] > 0x7F, all others set to valid values | Invalid HCI Command Parameters (0x12) |

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event with the error specified in Table 4.61.

## HCI/CCO/BV-24-C [LE Monitoring Advertisers RSSI command, Memory Capacity Exceeded]

- Test Purpose

Verify that the IUT does not add to the Monitored Advertisers List when Memory Capacity is Exceeded.

- Reference

[18] 7.8.146, 7.8.150

- Test Procedure
1. The Upper Tester sends HCI\_LE\_Add\_Device\_To\_Monitored\_Advertisers\_List commands to the IUT with valid parameters and different addresses and receives a successful HCI\_Command\_Complete event in response.
2. Repeat Step 1 until the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x07 (Memory Capacity Exceeded).
3. The Upper Tester sends an HCI\_LE\_Read\_Monitored\_Advertisers\_List\_Size command to the IUT with no command parameters.
4. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester with Number set to a valid value.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event with the error code 0x07 (Memory Capacity Exceeded).

In Step 4, the IUT sends an HCI\_Command\_Complete event with a valid Number value.

## HCI/CCO/BI-71-C [Invalid LE Monitoring Advertisers Parameters]

- Test Purpose

Verify that the IUT handles the Upper Tester sending invalid parameters for LE Monitoring Advertisers related HCI commands.

- Reference

[18] 7.8.146, 7.8.147, 7.8.149

- Test Procedure
1. The Upper Tester sends the HCI Command, with the Parameter and Value/Condition as specified in Table 4.62, to the IUT. All other values for the command are set to valid values.
2. The IUT sends the Event and Status/Error Code as specified in Table 4.62 to the Upper Tester.

| Round | Command | Parameter | Value/ Condition | Event and Status/Error Code |
| 1 | HCI_LE_Add_Device_ To_Monitored_ Advertisers_List | Address_Type | 0x02 | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |
| 2 | HCI_LE_Add_Device_ To_Monitored_ Advertisers_List | RSSI_Low_Threshold | 21 dBm | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |
| 3 | HCI_LE_Add_Device_ To_Monitored_ Advertisers_List | RSSI_High_Threshold | 21 dBm | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |
| 4 | HCI_LE_Add_Device_ To_Monitored_ Advertisers_List | RSSI_High_Threshold | <RSSI_Low_ Threshold | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |
| 5 | HCI_LE_Add_Device_ To_Monitored_ Advertisers_List | Timeout | 0x00 | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |
| 6 | HCI_LE_Remove_ Device_From_ Monitored_Advertisers_ List | Address_Type | 0x02 | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |

Table 4.62: Invalid LE Monitoring Advertisers Parameters rounds

| Round | Command | Parameter | Value/ Condition | Event and Status/Error Code |
| 7 | HCI_LE_Remove_ Device_From_ Monitored_ Advertisers_List | Address | Any valid address with the Monitoring List empty | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |
| 8 | HCI_LE_Enable_ Monitoring_Advertisers | Enable | 0x02 | HCI_Command_Complete: Invalid HCI Command Parameters (0x12) |

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event with the error code 0x12 (Invalid HCI Parameters).

## HCI/CCO/BI-72-C [Reject LE Extended Create Connection with Invalid Initiator\_Filter\_Policy Parameters]

- Test Purpose

Verify that the IUT rejects the LE Extended Create Connection command when the controller does not support Decision Based Advertising Filtering.

- Reference

[18] 7.8.66

- Initial Condition
- -The IUT is not currently scanning.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Extended\_Create\_Connection command to the IUT with the Initiator\_Filter\_Policy set to a value other than 0x00 or 0x01.
2. The IUT sends an HCI\_Command\_Complete event with Status set to Unsupported Feature or Parameter Value (0x11).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11).

## HCI/CCO/BI-73-C [LE Set Decision Data, Invalid Parameters]

- Test Purpose

Verify that the IUT handles invalid parameters for the LE Set Decision Data command.

- Reference

[18] 7.8.144

- Initial Condition
- -The IUT is not currently scanning.

- Test Procedure

Repeat Steps 1 to 3 for each round in Table 4.63.

1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Advertising\_Parameters command to the IUT with the Primary\_Advertising\_PHY set to LE 1M and a valid Advertising\_Event\_Parameters field with bit 7 set to 1 and receives a successful HCI\_Command\_Complete in return.
2. The Upper Tester sends the HCI\_LE\_Set\_Decision\_Data command to the IUT with the Parameter as set in Table 4.63. Decision\_Type\_Flags is set to 0x00 unless otherwise specified in Table 4.63.
3. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with the status specified in Table 4.63.

| Round | Parameter | Status |
| 1 | Invalid Advertising_Handle | 0x42 (Unknown Advertising Identifier) |
| 2 | Decision_Data_Length = 5 with Resolvable Tag Type set in Decision_Type_Flags | 0x12 (Invalid HCI Command Parameters) |
| 3 | Decision_Data_Length = 5 | 0x00 (Success) |
| 4 | Decision_Data_Length = 9 | 0x12 (Invalid HCI Command Parameters) |
| 5 | Decision_Data_Length = 0 | 0x00 (Success) |

Table 4.63: Decision-Based Advertisements, Test Groups rounds

- Expected Outcome

## Pass verdict

In Step 3, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set as specified in Table 4.63.

## HCI/CCO/BI-74-C [LE Set Decision Instructions, Invalid Parameters]

- Test Purpose

Verify that the IUT handles invalid parameters for the LE Set Decision Instructions command.

- Reference

[18] 7.8.145

- Initial Condition
- -The maximum number of supported tests in a Decision PDU is defined by the TSPX\_max\_decision\_tests IXIT value.
- Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.64. Skip Round 2 if TSPX\_max\_decision\_tests is greater than or equal to 14.

1. The Upper Tester sends an HCI\_LE\_Set\_Decision\_Instructions command to the IUT with the Num\_Tests field set as specified in Table 4.64.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Testers as specified in Table 4.64.

Table 4.64: Decision-Based Advertisements, Test Groups rounds

| Round | Parameter | Status |
| 1 | Num_Tests set to 0 | 0x12 (Invalid HCI Command Parameters) |
| 2 | Num_Tests = TSPX_max_decision_tests + 1 | 0x43 (Limit Reached) |
| 3 | Num_Tests = 1 and bit 0 of Test_Flags[0] set to 0 | 0x12 (Invalid HCI Command Parameters) |

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set as specified in Table 4.64.

## HCI/CCO/BV-25-C [LE Set Decision Instructions, Support for 8 Tests]

- Test Purpose

Verify that the IUT supports at least eight tests in the decision instructions.

- Reference

[18] 7.8.145

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Decision\_Instructions to the IUT with General\_Flags set to 0, Num\_Tests set to 8, and Test\_Field and Test\_Parameters set to 8 valid parameters.
2. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

## 4.10.16 LE Frame Space Update, PHY Not Supported

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Frame Space Update command when the PHY specified is not supported.

- Reference

[19] 7.7.65.48

- Initial Condition
- -LL connection is established, the IUT is Central or Peripheral, and T\_IFS = 150 μs
- Test Case Configuration

| Test Case | PHY |
| HCI/CCO/BI-76-C [LE Frame Space Update, PHY Not Supported, LE 2M PHY] | LE 2M |
| HCI/CCO/BI-77-C [LE Frame Space Update, PHY Not Supported, LE Coded PHY] | LE Coded |

Table 4.65: LE Frame Space Update, PHY Not Supported test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Frame\_Space\_Update command to the IUT with PHYs set as specified in Table 4.65 and all other parameters valid.
2. Perform either alternative 2A or 2B depending on the IUT HCI\_Command\_Status response. Alternative 2A (Successful HCI\_Command\_Status):
- 2A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2A.2 The IUT sends an HCI\_LE\_Frame\_Space\_Update\_Complete event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).

Alternative 2B (HCI\_Command\_Status with an error code):

- 2B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

In Step 2, the IUT rejects the command with an 0x12 error code.

## HCI/CCO/BI-78-C [LE Frame Space Update, CIS not supported]

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Frame Space Update command when CIS is not supported.

- Reference

[17] 7.7.65.48

- Initial Condition
- -LL connection is established, the IUT is Central or Peripheral, and T\_IFS = 150 μs
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Frame\_Space\_Update command to the IUT with Spacing\_Type set to 0x08 and all other parameters valid.
2. Perform either alternative 2A or 2B depending on the IUT HCI\_Command\_Status response. Alternative 2A (Successful HCI\_Command\_Status):
- 2A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2A.2 The IUT sends an HCI\_LE\_Frame\_Space\_Update\_Complete event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).

Alternative 2B (HCI\_Command\_Status with an error code):

- 2B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

In Step 2, the IUT rejects the command with an 0x12 error code.

## 4.10.17 LE CS Read Local Supported Capabilities

- Test Purpose

Verify that the IUT properly sets the RTT\_Capability depending on the RTT support.

- Reference

[19] 7.8.130

- Initial Condition
- -The IUT is not currently connected.
- -The Channel Sounding (Host Support) feature bit is set.
- Test Case Configuration

| Test Case | Parameter | HCI Command Version | Parameter Value | RTT Capability Bit | Bit Value |
| HCI/CCO/BI-79-C [LE CS Read Local Supported Capabilities, RTT Access Address] | RTT_AA_Only_N | v1 | >0 | 0 | 0 |
| HCI/CCO/BI-80-C [LE CS Read Local Supported Capabilities, RTT Sounding, Unsupported] | RTT_Sounding_N | v1 | 0 | 1 | 0 |
| HCI/CCO/BI-81-C [LE CS Read Local Supported Capabilities, RTT Random Sequence, Unsupported] | RTT_Random_Sequence_N | v1 | 0 | 2 | 0 |
| HCI/CCO/BI-128-C [LE CS Read Local Supported Capabilities, RTT Access Address, 10 ns] | RTT_AA_Only_N | v1 | >0 | 0 | 1 |
| HCI/CCO/BI-129-C [LE CS Read Local Supported Capabilities, RTT Sounding, 150 ns] | RTT_Sounding_N | v1 | >0 | 1 | 0 |
| HCI/CCO/BI-130-C [LE CS Read Local Supported Capabilities, RTT Sounding, 10 ns] | RTT_Sounding_N | v1 | >0 | 1 | 1 |
| HCI/CCO/BI-131-C [LE CS Read Local Supported Capabilities, RTT Random Sequence, 150 ns] | RTT_Random_Sequence_N | v1 | >0 | 2 | 0 |
| HCI/CCO/BI-132-C [LE CS Read Local Supported Capabilities, RTT Random Sequence, 10 ns] | RTT_Random_Sequence_N | v1 | >0 | 2 | 1 |
| HCI/CCO/BI-156-C [LE CS Read Local Supported Capabilities, RTT Access Address, 10 ns, LE 2M PHY] | RTT_2M_AA_Only_N | v2 | >0 | 3 | 1 |

| Test Case | Parameter | HCI Command Version | Parameter Value | RTT Capability Bit | Bit Value |
| HCI/CCO/BI-157-C [LE CS Read Local Supported Capabilities, RTT Sounding, 150 ns, LE 2M PHY] | RTT_2M_Sounding_N | v2 | >0 | 4 | 0 |
| HCI/CCO/BI-158-C [LE CS Read Local Supported Capabilities, RTT Sounding, 10 ns, LE 2M PHY] | RTT_2M_Sounding_N | v2 | >0 | 4 | 1 |
| HCI/CCO/BI-159-C [LE CS Read Local Supported Capabilities, RTT Random Sequence, 150 ns, LE 2M PHY] | RTT_2M_Random_Sequence_N | v2 | >0 | 5 | 0 |
| HCI/CCO/BI-160-C [LE CS Read Local Supported Capabilities, RTT Random Sequence, 10 ns, LE 2M PHY] | RTT_2M_Random_Sequence_N | v2 | >0 | 5 | 1 |

Table 4.66: LE CS Read Local Supported Capabilities test cases

- Test Procedure
1. The Upper Tester sends the HCI\_LE\_CS\_Read\_Local\_Supported\_Capabilities command version specified in Table 4.66 to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event with return parameters as specified in Table 4.66 and valid values for all other parameters.
- Expected Outcome

## Pass verdict

The IUT properly sets the RTT Capability Bit and Parameter to the Bit Value and Parameter Value specified in Table 4.66.

## HCI/CCO/BV-26-C [LE CS Read Remote Supported Capabilities]

- Test Purpose

Verify that the IUT properly sends a Read\_Remote\_Supported\_Capabilites\_Complete event after receiving an HCI\_LE\_CS\_Read\_Remote\_Supported\_Capabilities command.

- Reference
- [19] 7.8.131
- Initial Condition
- -The IUT and Lower Tester have an encrypted connection but have not performed a CS Capability Exchange.
- Test Procedure
1. The Upper Tester sends the HCI\_LE\_CS\_Read\_Remote\_Supported\_Capabilities command to the IUT.
2. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
3. The IUT performs the Channel Sounding Capability Exchange procedure with the Lower Tester. The Lower Tester sets bit 90 to 1.

4. The IUT generates an LE\_CS\_Read\_Remote\_Supported\_Capabilities\_Complete event. The Subfeatures\_Supported bit 0 is set to 0.
- Expected Outcome

## Pass verdict

The IUT properly generates the LE\_CS\_Read\_Remote\_Supported\_Capabilities\_Complete event after the Channel Sounding Capability Exchange procedures has completed with Subfeatures\_Supported bit 0 set to 0.

## 4.10.18 Reject LE CS Security Enable, Encryption

- Test Purpose

Verify that the IUT properly returns an error when the Host sends the LE CS Security Enable command when the IUT is a Central with an unencrypted connection or when the IUT is a Peripheral with an encrypted connection.

- Reference

[19] 7.8.133

- Initial Condition
- -The IUT is in the Role as specified in Table 4.67.
- -Encrypted Connection: The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings and have created a configuration.
- -Unencrypted Connection: The IUT and Lower Tester have an unencrypted connection.
- Test Case Configuration

| Test Case | Initial Condition | Error Code |
| HCI/CCO/BI-82-C [Reject LE CS Security Enable, Encryption, Unencrypted Connection, Central] | Unencrypted Connection Role = Central | 0x2F |
| HCI/CCO/BI-83-C [Reject LE CS Security Enable, Encryption, Peripheral] | Encrypted Connection Role = Peripheral | 0x0C |

Table 4.67: Reject LE CS Security Enable, Encryption test cases

- Test Procedure
1. The Upper Tester sends the HCI\_LE\_CS\_Security\_Enable command to the IUT with Connection\_Handle set to the ACL connection handle.
2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to the value in Table 4.67.
- Expected Outcome

## Pass verdict

In Step 2, the IUT responds to the HCI Command with an HCI\_Command\_Status event with Status set to the value in Table 4.67.

## 4.10.19 LE CS Set Default Settings, Disable Supported Role

- Test Purpose

Verify that the IUT properly returns an error when the HCI\_LE\_CS\_Set\_Default\_Settings command is called disabling a role the IUT supports with a valid CS Configuration.

- Reference

[19] 7.8.134

- Initial Condition
- -The IUT has the CS Role configuration as specified in Table 4.68.
- -The IUT and Lower Tester have an encrypted connection, completed the Capabilities Exchange procedure, and set default settings.
- Test Case Configuration

| Test Case | Role |
| HCI/CCO/BI-84-C [LE CS Set Default Settings Disable Supported Role, Initiator] | Initiator |
| HCI/CCO/BI-85-C [LE CS Set Default Settings Disable Supported Role, Reflector] | Reflector |

Table 4.68: LE CS Set Default Settings Disable Supported Role test cases

- Test Procedure
1. The Upper Tester sends an LE\_CS\_Create\_Config command with Role set as specified in Table 4.68 and all other parameters valid and receives an HCI\_Command\_Status in response.
2. The IUT sends an LL\_CS\_CONFIG\_REQ PDU to the Lower Tester.
3. The Lower Tester sends an LL\_CS\_CONFIG\_RSP PDU to the IUT.
4. The IUT sends a successful LE\_CS\_Config\_Complete event to the Upper Tester.
5. The Upper Tester sends an HCI\_LE\_CS\_Set\_Default\_Settings command to the IUT with Role\_Enable bit for the Role as specified in Table 4.68 to 0b0, and a valid CS\_SYNC\_Antenna\_Selection value.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).
- Expected Outcome

## Pass verdict

In Step 6, the IUT responds to the HCI Command with an Invalid HCI Command Parameters (0x12) error code.

## 4.10.20 LE CS Set Default Settings, Invalid Parameters

- Test Purpose

Verify that the IUT properly returns an error when the Host sends the LE CS Set Default Settings command with invalid parameters.

- Reference

[19] 7.8.134

- Initial Condition
- -The IUT and the Lower Tester have an encrypted ACL connection and exchanged capabilities.

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends the HCI\_LE\_CS\_Set\_Default\_Settings command to the IUT with Parameters set as specified in Table 4.69.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11 (Unsupported Feature or Parameter Value).
- Expected Outcome

Table 4.69: Reject LE CS Set Default Settings, Invalid Parameters test cases

| Test Case | Parameters |
| HCI/CCO/BI-86-C [Reject LE CS Set Default Settings, Invalid Parameters, Initiator Not Supported] | Role_Enable bit 0 = set to 0b1 CS_SYNC_Antenna_Selection = valid value |
| HCI/CCO/BI-87-C [Reject LE CS Set Default Settings, Invalid Parameters, Reflector Not Supported] | Role_Enable bit 1 = set to 0b1 CS_SYNC_Antenna_Selection = valid value |

## Pass verdict

In Step 2, the IUT responds to the HCI Command with an HCI\_Command\_Complete event with Status set to Unsupported Feature or Parameter Value (0x11).

## HCI/CCO/BI-88-C [LE CS Set Default Settings, Invalid Parameters, Antenna not Supported]

- Test Purpose

Verify that the IUT properly returns an error when the Host sends the LE CS Set Default Settings command with an unsupported Antenna Selection.

- Reference

[19] 7.8.134

- Initial Condition
- -The IUT and the Lower Tester have an encrypted ACL connection and exchanged capabilities.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Read\_Local\_Supported\_Capabilities command to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event with Num\_Antennas\_Supported.
3. If Num\_Antennas\_Supported is 4, then the test ends with a Pass verdict.
4. The Upper Tester sends an HCI\_LE\_CS\_Set\_Default\_Settings command to the IUT with CS\_SYNC\_Antenna\_Selection set to Num\_Antennas\_Supported + 1.
5. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11 (Unsupported Feature or Parameter Value).
- Expected Outcome

## Pass verdict

In Step 5, the IUT responds to the HCI Command with an HCI\_Command\_Complete event with Status set to Unsupported Feature or Parameter Value (0x11).

## HCI/CCO/BI-89-C [LE CS Read Remote FAE Table, noFAE set by Peer]

- Test Purpose

Verify that the IUT properly returns an error when the HCI LE CS Read Remote FAE Table command is called when the peer has the noFAE bit set.

- Reference
- [19] 7.8.135
- Initial Condition
- -The IUT has enabled the Initiator role.
- -The Lower Tester has the noFAE bit set in its capabilities.
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Read\_Remote\_FAE\_Table command to the IUT.
2. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status response.

Alternative 2A (Successful Status):

- 2A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 2A.2 The IUT sends an HCI\_LE\_CS\_Read\_Remote\_FAE\_Table\_Complete event to the Upper Tester with Status set to 0x11 (Unsupported Feature or Parameter Value).

Alternative 2B (Status = 0x11):

- 2B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x11 (Unsupported Feature or Parameter Value).
- Expected Outcome

## Pass verdict

In Step 2A.2 or 2B.1, the IUT responds with Status set to Unsupported Feature or Parameter Value (0x11).

## HCI/CCO/BI-90-C [LE CS Write Cached Remote FAE Table, noFAE set by Peer]

- Test Purpose

Verify that the IUT properly returns an error when the HCI LE CS Write Cached Remote FAE Table command is called when the peer has the noFAE bit set.

- Reference

[19] 7.8.136

- Initial Condition
- -The IUT and the Lower Tester have an encrypted ACL connection, set default settings, and exchanged capabilities.
- -The Lower Tester has the noFAE bit set in its capabilities.
- -The IUT has enabled the Initiator role.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Write\_Cached\_Remote\_FAE\_Table command to the IUT with Remote\_FAE\_Table.

2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11 (Unsupported Feature or Parameter Value).
- Expected Outcome

## Pass verdict

In Step 2, the IUT responds with an HCI\_Command\_Complete event with Status set to Unsupported Feature or Parameter Value (0x11).

## HCI/CCO/BI-91-C [LE CS Create Config, Disabled Role]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an HCI\_LE\_CS\_Create\_Config command for a role that is disabled.

- Reference

[19] 7.8.137

- Initial Condition
- -The IUT does not have a CS Role enabled by a prior HCI\_LE\_CS\_Set\_Default\_Settings command.
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with Role set to a supported role and all other values set to valid values.
2. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status response. Alternative 2A (Successful Status):
- 2A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 2A.2 The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

Alternative 2B (Status = 0x12):

- 2B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x12 (Invalid HCI Command Parameters).
- Expected Outcome

## Pass verdict

In Step 2A.2 or 2B.1, the IUT returns an error with Status set to 0x12 (Invalid HCI Command Parameters).

## HCI/CCO/BI-92-C [LE CS Create Config, Invalid Channels]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an HCI\_LE\_CS\_Create\_Config command with fewer than 15 channels.

- Reference

[19] 7.8.137

- Initial Condition
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with Config\_ID set to 0, Channel\_Map set with 14 random bits (excluding 0, 1, 23, 24, 25, 77, 78) set to 0b1, and all other values set to valid values.
2. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status response.

Alternative 2A (Successful Status):

- 2A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 2A.2 The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Status &gt; 0.

Alternative 2B (Status &gt; 0):

- 2B.1 The IUT sends an HCI\_Command\_Status event with Status &gt; 0.
- Expected Outcome

## Pass verdict

In Step 2A.2 or 2B.1, the IUT returns an error with Status &gt; 0.

## HCI/CCO/BI-93-C [LE CS Create Config, Unsupported Parameters]

## · Test Purpose

Verify that the IUT properly handles the Upper Tester sending an HCI\_LE\_CS\_Create\_Config command with values not supported by the local and remote controllers.

- Reference

[19] 7.8.137

- Initial Condition
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings.
- -The Lower Tester does not support Mode-3.
- Test Procedure

If the IUT supports all Channel Sounding configurable features, the test starts with Step 3.

1. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with values not supported by the IUT.
2. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status response. Alternative 2A (Successful Status):
3. 2A.1 The IUT sends a successful HCI\_Command\_Status event in response.
4. 2A.2 The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Status set to 0x11 (Unsupported Feature or Parameter Value).

Alternative 2B (Status = 0x11):

- 2B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x11 (Unsupported Feature or Parameter Value).
3. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with Main\_Mode\_Type set to 0x03.

4. Perform either alternative 4A or 4B depending on the HCI\_Command\_Status response.

Alternative 4A (Successful Status):

- 4A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 4.2 The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Status set to 0x11 (Unsupported Feature or Parameter Value).

Alternative 4B (Status = 0x11):

- 4B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x11 (Unsupported Feature or Parameter Value).
- Expected Outcome

## Pass verdict

In Step 2A.2 or 2B.1 and 4A.2 or 4B.1, the IUT returns an error with Status set to 0x11 (Unsupported Feature or Parameter Value).

## HCI/CCO/BI-94-C [LE CS Remove Config, Invalid Config ID]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an invalid Config ID for the LE Remove CS Config command with a Config ID that does not exist and was removed.

- Reference

[19] 7.8.138

- Initial Condition
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with Config\_ID set to 1 and valid parameters and receives a successful HCI\_Command\_Status in response.
2. The IUT sends an LL\_CS\_CONFIG\_REQ PDU to the Lower Tester with Config\_ID set to 1 and Action set to 0b01.
3. The Lower Tester sends an LL\_CS\_CONFIG\_RSP PDU to the IUT with Config\_ID set to 1.
4. The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Config\_ID set to 1, Status set to 0x00, and Action set to 0x01.
5. The Upper Tester sends an HCI\_LE\_CS\_Remove\_Config command to the IUT with Config\_ID set to 1 and receives a successful HCI\_Command\_Status in response.
6. The IUT sends an LL\_CS\_CONFIG\_REQ PDU to the Lower Tester with Config\_ID set to 1 and Action set to 0b00.
7. The Lower Tester sends an LL\_CS\_CONFIG\_RSP PDU to the IUT with Config\_ID set to 1.
8. The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Config\_ID set to 1, Status set to 0x00, and Action set to 0x00.
9. The Upper Tester sends an HCI\_LE\_CS\_Remove\_Config command to the IUT with Config\_ID set to 1.
10. Perform either alternative 10A or 10B depending on the HCI\_Command\_Status response. Alternative 10A (Successful Status):
- 10A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 10A.2 The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

Alternative 10B (Status = 0x12):

10B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x12 (Invalid HCI Command Parameters).

- Expected Outcome

## Pass verdict

In Step 10A.2 or 10B.1, the IUT sends an HCI event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

## HCI/CCO/BI-95-C [LE CS Set Procedure Parameters, Limited Resources]

- Test Purpose

Verify that the IUT properly returns an error when the Host makes calls to the LE CS Set Procedure Parameters command when resources are not available.

- Reference

[19] 7.8.140

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, exchanged capabilities, and created configurations.
- Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.70. Skip the round if the HCI command cannot be called with a parameter that is out of range, for example, if the IXIT value is the highest range of a Max parameter.

1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with the parameters set to a value outside of the IXIT value specified in Table 4.70.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0D (Rejected Due to Limited Resources).

| Round | Parameter | IXIT Value |
| 1 | Max_Procedure_Len | TSPX_CS_Max_Procedure_Duration |
| 2 | Min_Procedure_Interval | TSPX_CS_Min_Procedure_Interval |
| 3 | Max_Procedure_Interval | TSPX_CS_Max_Procedure_Interval |
| 4 | Max_Procedure_Count | TSPX_CS_Max_Procedure_Count |
| 5 | Min_Subevent_Len | TSPX_CS_Min_Subevent_Len |
| 6 | Max_Subevent_Len | TSPX_CS_Max_Subevent_Len |
| 7 | Tone_Antenna_Config_Selection | TSPX_CS_Supported_ACI_Mask |

Table 4.70: LE CS Set Procedure Parameters rounds

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0D (Rejected Due to Limited Resources).

## HCI/CCO/BI-149-C [LE CS Set Procedure Parameters, Invalid Parameter]

- Test Purpose

Verify that the IUT properly returns an error when the Host makes calls to the LE CS Set Procedure Parameters commands with invalid parameters.

- Reference

[19] 7.8.140

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, exchanged capabilities, and created configurations.
- Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.71.

1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with the parameters set as specified in Table 4.71.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).
- Expected Outcome

Table 4.71: LE CS Set Procedure Parameters Invalid Parameters

| Round | Parameter |
| 1 | Max_Procedure_Len = 0x0000 |
| 2 | Min_Procedure_Interval > Max_Procedure_Interval where Max_Procedure_Count is a valid value greater than 1 |
| 3 | Min_Subevent_Len > Max_Subevent_Len |
| 4 | Connection_Handle = 0xFFFF |

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

## HCI/CCO/BI-96-C [LE CS Set Procedure Parameters, Invalid Config ID]

- Test Purpose

Verify that the IUT properly returns an error when the Host makes calls to the LE CS Set Procedure Parameters commands where the Config ID is invalid.

- Reference

[19] 7.8.140

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, read the remote FAE, exchanged capabilities, executed the CS Security procedure, and set default settings.

Figure 4.113: LE CS Set Procedure Parameters, Invalid Config ID MSC

1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with parameters set to valid values and Config\_ID set to 0.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).
3. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with parameters set to valid values and Config\_ID set to 0 and receives a successful HCI\_Command\_Status in response.
4. The IUT and the Lower Tester complete the CS configuration procedure.
5. The IUT sends a successful HCI\_LE\_CS\_Config\_Complete event in response.
6. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with Config\_ID set to 0 and receives a successful HCI\_Command\_Complete event in response.
7. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to 0 and Enable set to 0x01.
8. The IUT sends a successful HCI\_Command\_Status event in response.
9. The IUT sends an LL\_CS\_REQ PDU to the Lower Tester.
10. Before completing the CS Start procedure, the Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with parameters set to valid values and Config\_ID set to 0.
11. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters) or 0x0C (Command Disallowed).
12. The Lower Tester and the IUT complete the CS Start Procedure.
13. The IUT sends a LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester.
14. After CS Procedure has been completed, the Upper Tester sends an HCI\_LE\_CS\_Remove\_Config command to the IUT with the Config\_ID set to 0 and receives a successful HCI\_Command\_Status event in response.
15. The IUT sends an LL\_CS\_CONFIG\_REQ PDU to the Lower Tester with Config\_ID set to 0 and Action set to 0b00.
16. The Lower Tester sends an LL\_CS\_CONFIG\_RSP PDU to the IUT with Config\_ID set to 0.
17. The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with Config\_ID set to 0 and Action set to 0x00.
18. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with parameters set to valid values and Config\_ID set to 0.
19. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).
- Expected Outcome

## Pass verdict

In Steps 2 and 19, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

In Step 11, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters) or 0x0C (Command Disallowed).

## HCI/CCO/BI-97-C [LE CS Procedure Enable after configuration and procedure parameters]

- Test Purpose

Verify that the IUT properly rejects the Upper Tester attempting to enable a CS Procedure until after the IUT has completed CS configuration and set the procedure parameters. The IUT also rejects an attempt to enable the procedure with the same configuration twice.

- Reference

## 19 7.8.141

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, read remote FAE Table, completed CS security procedure, exchanged capabilities, and set default settings.
- Test Procedure

Figure 4.114: LE CS Procedure Enable, Invalid Parameters MSC -Page 1 of 2

Figure 4.115: LE CS Procedure Enable, Invalid Parameters MSC -Page 2 of 2

1. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set a Config\_ID that does not exist, and Enable set to 0x01.
2. 2.
3. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status response. Alternative 2A (Successful Status):
4. 2A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester in response.
5. 2A.2 The IUT sends an HCI\_LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

Alternative 2B (Status = 0x12):

- 2B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x12 (Invalid HCI Command Parameters).
3. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with parameters set to valid values.
4. The IUT sends a successful HCI\_Command\_Status event in response.
5. The Lower Tester and the IUT execute the CS configuration procedure.
6. The IUT sends a successful HCI\_LE\_CS\_Config\_Complete event to the Upper Tester.
7. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to the value used in Step 3 and Enable set to 0x01.

- 8.
- Perform either alternative 8A or 8B depending on the HCI\_Command\_Status response. Alternative 8A (Successful Status):
- 8A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 8A.2 The IUT sends an HCI\_LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester with Status set to 0x0C (Command Disallowed).

Alternative 8B (Status = 0x0C):

- 8B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x0C (Command Disallowed).
9. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters with Config\_ID set to the value in Step 3, Max\_Procedure\_Len set to 0x7D00 (20s) or TSPX\_CS\_Max\_Procedure\_Duration (whichever is less), Min\_Procedure\_Interval and Max\_Procedure\_Interval set to 0x00, Max\_Procedure\_Count set to 0x01 or Min\_Subevent\_Len and Max\_Subevent\_Len set to 2.5ms, and all other parameters are valid.
10. The IUT sends a successful HCI\_Command\_Complete event in response.
11. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to the value used in Step 3, and Enable set to 0x01.
12. The IUT sends a successful HCI\_Command\_Status event in response.
13. The Lower Tester and the IUT exchange the CS Procedure Enable procedure.
14. The IUT sends a LE\_CS\_Procedure\_Enable\_Complete event.
15. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to the value used in Step 3, and Enable set to 0x01.
16. Perform either alternative 16A or 16B depending on the HCI\_Command\_Status response. Alternative 16A (Successful Status):
- 16A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 16A.2 The IUT sends an HCI\_LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester with Status set to 0x0C (Command Disallowed).

Alternative 16B (Status = 0x0C):

- 16B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x0C (Command Disallowed).
- Expected Outcome

## Pass verdict

In Steps 2A.2 or 2B.1, the IUT sends an HCI event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

In Step 8A.2 or 8B.1 and 16A.2 or 16B.1, the IUT sends an HCI event to the Upper Tester with Status set to 0x0C (Command Disallowed).

## 4.10.21 CS Invalid Connection Handle

## · Test Purpose

Verify that the IUT properly handles the Upper Tester sending an invalid connection handle for the CS commands.

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection.

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends an HCI Command specified in Table 4.72 to the IUT with Connection\_Handle set to an invalid ACL, and all other parameters set to valid values.
2. Perform either alternative 2A, 2B, or 2C depending on the Command Response in Table 4.72. Alternative 2A (HCI\_Command\_Status with Status = 0x00):
- 2A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 2A.2 The IUT sends an HCI event specified in Table 4.72 to the Upper Tester with Status set to 0x02 (Unknown Connection Identifier).

Table 4.72: CS Invalid Connection Handle test cases

| Test Case | Reference | HCI Command HCI Event | HCI Command Response |
| HCI/CCO/BI-98-C [CS Invalid Connection Handle, LE CS Read Remote Supported Capabilities] | [19] 7.8.131 | HCI_LE_CS_Read_Remote_Supported_ Capabilities HCI_LE_CS_Read_Remote_Supported_ Capabilities_Complete | HCI_Command _Status |
| HCI/CCO/BI-99-C [CS Invalid Connection Handle, LE CS Security Enable] | [19] 7.8.133 | HCI_LE_CS_Security_Enable HCI_LE_CS_Security_Enable_Complete | HCI_Command _Status |
| HCI/CCO/BI-100-C [CS Invalid Connection Handle, LE CS Set Default Settings] | [19] 7.8.134 | HCI_LE_CS_Set_Default_Settings | HCI_Command _Complete |
| HCI/CCO/BI-101-C [CS Invalid Connection Handle, LE CS Read Remote FAE Table] | [19] 7.8.135 | HCI_LE_CS_Read_Remote_FAE_Table HCI_LE_CS_Read_Remote_FAE_Table_ Complete | HCI_Command _Status |
| HCI/CCO/BI-102-C [CS Invalid Connection Handle, LE CS Write Cached Remote FAE Table] | [19] 7.8.136 | HCI_LE_CS_Write_Cached_Remote_FAE _Table | HCI_Command _Complete |
| HCI/CCO/BI-103-C [CS Invalid Connection Handle, LE CS Create Config] | [19] 7.8.137 | HCI_LE_CS_Create_Config HCI_LE_CS_Config_Complete | HCI_Command _Status |
| HCI/CCO/BI-104-C [CS Invalid Connection Handle, LE CS Remove Config] | [19] 7.8.138 | HCI_LE_CS_Remove_Config HCI_LE_CS_Config_Complete | HCI_Command _Status |
| HCI/CCO/BI-105-C [CS Invalid Connection Handle, LE CS Procedure Enable] | [19] 7.8.141 | HCI_LE_CS_Procedure_Enable HCI_LE_CS_Procedure_Enable_Complete | HCI_Command _Status |

Alternative 2B (HCI\_Command\_Status with Status = 0x02):

- 2B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x02 (Unknown Connection Identifier).

Alternative 2C (HCI\_Command\_Complete):

2C.1 The IUT sends an HCI\_Command\_Complete event with Status set to 0x02 (Unknown Connection Identifier).

## · Expected Outcome

## Pass verdict

In Step 2A.2, 2B.1, or 2C.1, the IUT sends an event to the Upper Tester with Status set to 0x02 (Unknown Connection Identifier).

## HCI/CCO/BI-106-C [LE CS Create Config, Invalid Mode and Submode Combinations]

## · Test Purpose

Verify that the IUT properly returns an error when the Host attempts to configure invalid combinations of the Main\_Mode and Submode.

## · Reference

[19] 7.8.137

- Initial Condition
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings and a supported Role has been enabled using Set\_Default\_Settings.

## · Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.73.

1. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with Main\_Mode\_Type and Sub\_Mode\_Type set as specified in Table 4.73 and a supported Role that has been enabled using Set\_Default\_Settings.
2. Perform either alternative 2A or 2B depending on the HCI\_Command\_Status response.
2. Alternative 2A (Successful Status):
4. 2A.1 The IUT sends a successful HCI\_Command\_Status event in response.

The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with

- 2A.2 Status &gt; 0.

Alternative 2B (Status &gt; 0):

- 2B.1 The IUT sends an HCI\_Command\_Status event with Status &gt; 0.

Table 4.73: LE CS Create Config, Invalid Mode and Submode Combinations rounds

| Round | Main_Mode | Submode |
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 1 | 3 |
| 4 | 2 | 2 |
| 5 | 3 | 1 |
| 6 | 3 | 3 |

## · Expected Outcome

## Pass verdict

In Step 2A.2 or 2B.1, the IUT rejects the invalid Main\_Mode and Submode combinations with an Error Status.

## HCI/CCO/BI-107-C [Channel Sounding Commands, Channel Sounding Host Support Bit Not Set]

## · Test Purpose

Verify that the IUT properly returns an error when the Channel Sounding (Host Support) feature bit is not set.

## · Reference

[25] 7.8.130, 7.8.131, 7.8.132, 7.8.133, 7.8.157, 7.8.158

## · Initial Condition

- -The IUT and Lower Tester have an encrypted connection but have not performed a CS Capability Exchange.
- -The Upper Tester has not set the Host Feature Bit.

## · Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.74.

1. The Upper Tester sends an HCI Command specified in Table 4.74 to the IUT valid parameters.
2. Perform alternatives 2A, 2B, or 2C depending on the HCI response event. Alternative 2A (HCI\_Command\_Status with Status = 0x00):
3. 2A.1 The IUT sends a successful HCI\_Command\_Status event in response.
4. 2A.2 The IUT sends an HCI event specified in Table 4.74 to the Upper Tester with Status set to 0x0C (Command Disallowed).
5. Alternative 2B (HCI\_Command\_Status with Status = 0x0C):
6. 2B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x0C (Command Disallowed).

Alternative 2C (HCI\_Command\_Complete):

- 2C.1 The IUT sends an HCI\_Command\_Complete event with Status set to 0x0C (Command Disallowed).

Table 4.74: Channel Sounding Commands, Channel Sounding Not Supported rounds

| Round | HCI Command/HCI Event | HCI Response |
| 1 | HCI_LE_CS_Read_Local_Supported_Capabilities No Event | HCI_Command_Complete |
| 2 | HCI_LE_CS_Read_Remote_Supported_Capabilities HCI_LE_CS_Read_Remote_Supported_Capabilities_Com plete | HCI_Command_Status |
| 3 | HCI_LE_CS_Write_Cached_Remote_Supported_Capabiliti es | HCI_Command_Complete |
| 4 | HCI_LE_CS_Security_Enable | HCI_Command_Status |
| 5 | HCI_LE_CS_Set_Security_Requirements | HCI_Command_Complete |
| 6 | HCI_LE_CS_Set_Default_Security_Requirements | HCI_Command_Complete |

## · Expected Outcome

## Pass verdict

In Step 2A.2, 2B.1, or 2C.1, the IUT sends an event to the Upper Tester with Status set to 0x0C (Command Disallowed).

## 4.10.22 LE CS Read Remote Supported Capabilities, Remote CS Host Bit Not Set

- Test Purpose

Verify that the IUT properly returns an error when the Lower Tester does not have the Channel Sounding Host Bit set.

- Reference

[19] 7.8.131

- Initial Condition
- -The IUT is in the Role as specified in Table 4.75.
- -The IUT and Lower Tester have an encrypted connection.
- -The Lower Tester does not have the Channel Sounding Host Bit set.
- Test Case Configuration

| Test Case | Role |
| HCI/CCO/BI-108-C [LE CS Read Remote Supported Capabilities, Remote CS Host Bit Not Set, Central] | Central |
| HCI/CCO/BI-109-C [LE CS Read Remote Supported Capabilities, Remote CS Host Bit Not Set, Peripheral] | Peripheral |

Table 4.75: LE CS Read Remote Supported Capabilities, Remote CS Host Bit Not Set test cases

## · Test Procedure

1. If the IUT autonomously performed a feature exchange, skip to Step 3.
2. Perform alternative 2A or 2B depending on the IUT role.

Alternative 2A (IUT is a Central):

- 2A.1 The Upper Tester sends an HCI\_LE\_Read\_Remote\_Features\_Page\_0 command to the IUT and receives a successful HCI\_Command\_Status in response.
- 2A.2 The IUT sends an LL\_FEATURE\_REQ to the Lower Tester.
- 2A.3 The Lower Tester sends an LL\_FEATURE\_RSP to the IUT.
- 2A.4 The IUT sends an HCI\_LE\_Read\_Remote\_Features\_Page\_0\_Complete event to the Upper Tester.

Alternative 2B (IUT is a Peripheral):

- 2B.1 The Lower Tester sends an LL\_FEATURE\_REQ to the IUT.
- 2B.2 The IUT sends an LL\_FEATURE\_RSP to the Lower Tester.
3. The Upper Tester sends an HCI\_LE\_CS\_Read\_Remote\_Supported\_Capabilities command to the IUT.
4. Perform either alternative 4A or 4B depending on the HCI response event.

Alternative 4A (HCI\_Command\_Status with Status = 0x00):

- 4A.1 The IUT sends a successful HCI\_Command\_Status event in response.
- 4A.2 The IUT sends an HCI\_LE\_CS\_Read\_Remote\_Supported\_Capabilities\_Complete event to the Upper Tester with Status set to 0x0C (Command Disallowed).

Alternative 4B (HCI\_Command\_Status with Status = 0x0C):

- 4B.1 The IUT sends an HCI\_Command\_Status event with Status set to 0x0C (Command Disallowed).

- Expected Outcome

## Pass verdict

In Step 4A.2 or 4B.1, the IUT sends an event to the Upper Tester with Status set to 0x0C (Command Disallowed).

## HCI/CCO/BI-110-C [LE CS Set Channel Classification, RFU Channels]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an HCI\_LE\_CS\_Set\_Channel\_Classification command with RFU Channels in the channel map.

- Reference

[19] 7.8.139

- Initial Condition
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings.
- Test Procedure

Repeat Steps 1 and 2 for each round in Table 4.76. Each round has an interval of 1.25 seconds.

1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Channel\_Classification command to the IUT with Channel\_Classification set with 14 valid channel bits set to 0b1 and the bit specified in Table 4.76 set to 0b1.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).

| Round | Channel Bit |
| 1 | 0 |
| 2 | 1 |
| 3 | 23 |
| 4 | 24 |
| 5 | 25 |
| 6 | 77 |
| 7 | 78 |

Table 4.76: LE CS Set Channel Classification, RFU Channels rounds

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event with Status set to 0x12.

## HCI/CCO/BI-111-C [LE CS Set Channel Classification, Invalid Interval]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an

HCI\_LE\_CS\_Set\_Channel\_Classification command at an interval shorter than 1 second. The IUT returns an error when successive calls the HCI\_LE\_CS\_Set\_Channel\_Classification shorter than 1 second.

- Reference

[19] 7.8.139

- Initial Condition
- -The IUT and Lower Tester have an encrypted connection, exchanged capabilities, and set default settings.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Channel\_Classification command to the IUT with Channel\_Classification set to at least 15 valid bits.
2. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
3. Less than 1 second after Step 1, the Upper Tester sends an HCI\_LE\_CS\_Set\_Channel\_Classification command to the IUT with Channel\_Classification set to at least 15 valid bits.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C (Command Disallowed).
5. At least 1 second after Step 1, the Upper Tester sends an HCI\_LE\_CS\_Set\_Channel\_Classification command to the IUT with Channel\_Classification set to at least 15 valid bits.
6. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 4, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C (Command Disallowed).

In Step 6, the IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.

## Inconclusive verdict

The Upper Tester is unable to execute Step 3 in less than 1 second after Step 1.

## HCI/CCO/BI-112-C [LE CS Create Config, Peer Capabilities Unknown]

- Test Purpose

Verify that the IUT properly handles the Upper Tester sending an HCI\_LE\_CS\_Create\_Config command when the Peer capabilities are unknown.

- Reference

[19] 7.8.137

- Initial Condition
- -The IUT and Lower Tester have an encrypted connection and set default settings but have not exchanged capabilities.

## · Test Procedure

| Test Procedure | Test Procedure | Test Procedure | Test Procedure |
| | Alternative 2A (Successful Status): | Alternative 2A (Successful Status): | Alternative 2A (Successful Status): |
| | Alternative 2A.2A (IUT initiates an LL capabilities exchange): | Alternative 2A.2A (IUT initiates an LL capabilities exchange): | Alternative 2A.2A (IUT initiates an LL capabilities exchange): |
| | | 2A.2A.1 | The IUT sends an LL_CS_CAPABILITIES_REQ PDU to the Lower |
| | | 2A.2A.3 | The IUT sends an HCI_LE_CS_Read_Remote_Supported_Capabilities_Complete event to |
| | Alternative 2A.2B (IUT does not initiate an LL capabilities exchange): | Alternative 2A.2B (IUT does not initiate an LL capabilities exchange): | Alternative 2A.2B (IUT does not initiate an LL capabilities exchange): |
| | | 2A.2B.1 | The IUT sends an HCI_LE_CS_Config_Complete event to the Upper |
| | Alternative 2B (Status = 0x0C): | Alternative 2B (Status = 0x0C): | Alternative 2B (Status = 0x0C): |
| | 2B.1 | The IUT sends an HCI_Command_Status event with Status set to 0x0C (Command | The IUT sends an HCI_Command_Status event with Status set to 0x0C (Command |
| | Alternative 3A (First execution round): | Alternative 3A (First execution round): | Alternative 3A (First execution round): |
| | Alternative 3B (Second round): | Alternative 3B (Second round): | Alternative 3B (Second round): |
| | 3B.1 | The Upper Tester sends an HCI_LE_CS_Write_Cached_Remote_Supported_Capabilities command to the IUT with valid configurations using the stored capabilities returned in the remote capabilities procedure. | The Upper Tester sends an HCI_LE_CS_Write_Cached_Remote_Supported_Capabilities command to the IUT with valid configurations using the stored capabilities returned in the remote capabilities procedure. |

- Expected Outcome

## Pass verdict

In Step 2A.2B.1 or 2B.1, the IUT returns an error with Status set to 0x0C (Command Disallowed).

In Step 2A.2A.1, the IUT initiates a CS capabilities exchange before beginning the CS configuration procedure.

In Step 7, the IUT sends a successful HCI\_LE\_CS\_Config\_Complete event to the Upper Tester.

## 4.10.23 Reject CS Start Procedure When IUT Configuration has not completed

- Test Purpose

Verify that a Central IUT rejects the CS Start Procedure when capability exchange, configuration, and security procedures have not been completed.

- Reference

[18] 5.1.25, 5.1.26

- Initial Condition
- -The Central IUT and Lower Tester have an encrypted connection but have not exchanged capabilities.
- Test Case Configuration

| Test Case | IUT Role |
| HCI/CCO/BI-113-C [Reject CS Start Procedure When IUT Configuration has not completed, Initiator] | Initiator |
| HCI/CCO/BI-114-C [Reject CS Start Procedure When IUT Configuration has not completed, Reflector] | Reflector |

Table 4.77: Reject CS Start Procedure When IUT Configuration has not completed test cases

·

Figure 4.116: Reject CS Start Procedure when IUT Configuration has not completed MSC -Page 1 of 2

Figure 4.117: Reject CS Start Procedure when IUT Configuration has not completed MSC -Page 2 of 2

1. The Upper Tester sends an HCI\_LE\_CS\_Read\_Local\_Supported\_Capabilities command to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
3. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to 1.

4. Perform alternative 4A or 4B depending on the IUT response.

Alternative 4A (Successful HCI\_Command\_Status):

- 4A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 4A.2 The IUT sends an HCI\_LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters) or 0x0C (Command Disallowed).
- Alternative 4B (The IUT returns an HCI\_Command\_Status event with an 0x12 (Invalid HCI Command Parameters or 0x0C (Command Disallowed)):
- 4B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters) or 0x0C (Command Disallowed).
5. The Upper Tester sends an HCI\_LE\_CS\_Read\_Remote\_Supported\_Capabilities command to the IUT.
6. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
7. The IUT sends an LL\_CS\_CAPABILITIES\_REQ PDU to the Lower Tester.
8. The Lower Tester sends an LL\_CS\_CAPABILITIES\_RSP PDU to the IUT with No\_FAE set to 1.
9. The IUT sends a successful HCI\_LE\_CS\_Read\_Remote\_Supported\_Capabilities\_Complete event to the Upper Tester.
10. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to 1.
11. Perform Step 4.
12. The Upper Tester sends an HCI\_LE\_CS\_Security\_Enable command to the IUT and receives a successful HCI\_Command\_Status in response.
13. The IUT sends an LL\_CS\_SEC\_REQ PDU to the Lower Tester.
14. The Lower Tester sends an LL\_CS\_SEC\_RSP PDU to the IUT.
15. The IUT sends a successful HCI\_LE\_CS\_Security\_Enable\_Complete event to the Upper Tester.
16. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to 1.
17. Perform Step 4.
18. The Upper Tester sends an HCI\_LE\_CS\_Set\_Default\_Settings to the IUT with Role\_Enable set as specified in Table 4.77 and receives a successful HCI\_Command\_Complete event in response.
19. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with Config\_ID set to 1, Role set to the Role in Table 4.77, and all other paraemters with valid values and receives a successful HCI\_Command\_Status event to the Upper Tester.
20. The IUT sends an LL\_CS\_CONFIG\_REQ PDU to the Lower Tester with the same parameters sent in Step 12.
21. The Lower Tester sends an LL\_CS\_CONFIG\_RSP PDU to the IUT with Config\_ID Set to 1.
22. The IUT sends an HCI\_LE\_CS\_Config\_Complete event to the Upper Tester with a Config\_ID.
23. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to 1.
24. Perform Step 4 however the Status is set to 0x0C (Command Disallowed) instead.
25. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with Config\_ID set to 1 and receives a successful HCI\_Command\_Complete event in response.
26. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT.
27. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.

- Expected Outcome

## Pass verdict

In Steps 4, 11, 17, and 24, the IUT rejects the HCI\_LE\_CS\_Procedure\_Enable command with an error code.

In Step 27, the IUT successfully starts the CS Procedure Enable procedure.

## HCI/CCO/BI-115-C [LE CS Set Procedure Parameters, Invalid Preferred Peer Antenna]

- Test Purpose

Verify that the IUT properly returns an Invalid HCI Command Parameters error when the Host makes calls to the LE CS Set Procedure Parameters commands with Preferred Peer Antenna set to 0x00.

- Reference

[1] 7.8.140

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, read remote FAE Table, completed CS security procedure, exchanged capabilities, and created configurations.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with Preferred\_Peer\_Antenna set to 0x00.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an 0x12 error.

## 4.10.24 HCI command fails when address is the IUT address

- Test Purpose

Verify that the IUT correctly rejects the HCI command when BD\_ADDR is set to the IUT device address.

- Initial Condition
- -The IUT is in Standby.
- Test Case Configuration

| Test Case | Reference | HCI Command | HCI Event |
| HCI/CCO/BI-118-C [HCI fails with address is the IUT address, Create Connection] | [8] 7.1.5 | HCI_Create_Connection | HCI_Connection_Comple te |
| HCI/CCO/BI-119-C [HCI fails with address is the IUT address, Truncated Page] | [8] 7.1.47 | HCI_Truncated_Page | HCI_Truncated_Page_C omplete |

Table 4.78: HCI command fails with address is the IUT address test cases

- Test Procedure
1. The Upper Tester sends the HCI command specified in Table 4.78 to the IUT with BD\_ADDR set to the IUT device address.
2. Perform either Alternative 2A or 2B depending on the IUT response.

Alternative 2A (Successful HCI\_Command\_Status):

- 2A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2A.2 The IUT sends the HCI Event specified in Table 4.78 to the Upper Tester with a nonzero Status.

Alternative 2B (HCI\_Command\_Status with an error code):

- 2B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with a non-zero Status.
- Expected Outcome

## Pass verdict

In Steps 2A.2 or 2B.1, the IUT sends an event with a non-zero error code.

The IUT does not transmit any paging packets from the start of Step 1 until at least 5 seconds after the end of Step 2.

## Warning

In Steps 2A.1 or 2B.1, the IUT sends an event with the error code Page\_Timeout (0x04).

## HCI/CCO/BI-120-C [LE Set Default Subrate, Invalid Parameters]

- Test Purpose

Verify that the LE Set Default Subrate command properly returns an error when there are invalid parameters.

- Reference

[1] 7.8.123

- Initial Condition
- -The IUT is in standby.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Default\_Subrate command to the IUT with Subrate\_Min set to 1, Subrate\_Max set to 3, and Max\_Latency set to 166.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).
3. The Upper Tester sends an HCI\_LE\_Set\_Default\_Subrate command to the IUT with Subrate\_Min set to 2 and Subrate\_Max set to 1.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).
5. The Upper Tester sends an HCI\_LE\_Set\_Default\_Subrate command to the IUT with Subrate\_Min set to 1, Subrate\_Max set to 2, and Continuation\_Number set to 3.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).

- Expected Outcome

## Pass verdict

In Steps 2, 4, and 6, the IUT returns a 0x12 error code.

## 4.10.25 LE CS Set Procedure Parameters, Unsupported PHY

- Test Purpose

Verify that the IUT properly returns an error when the Host makes calls to the LE CS Set Procedure Parameters commands with an unsupported PHY.

- Reference

[19] 7.8.140

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, exchanged capabilities, and created configurations.
- Test Case Configuration
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with the parameters set to valid values and the PHY value specified in Table 4.79.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to a valid error code.
- Expected Outcome

Table 4.79: LE CS Set Procedure Parameters, Unsupported PHY test cases

| Test Case | PHY |
| HCI/CCO/BI-125-C [LE CS Set Procedure Parameters, Unsupported PHY, LE 2M PHY] | LE 2M PHY |
| HCI/CCO/BI-126-C [LE CS Set Procedure Parameters, Unsupported PHY, LE Coded PHY, S=8] | LE Coded PHY, S=8 |
| HCI/CCO/BI-127-C [LE CS Set Procedure Parameters, Unsupported PHY, LE Coded PHY, S=2] | LE Coded PHY, S=2 |

## Pass verdict

In Step 2, the IUT responds with a valid error code.

## HCI/CCO/BI-134-C [LE Create Connection, Invalid Parameters]

- Test Purpose

Verify that the IUT properly handles the Host sending invalid parameters for the LE Create Connection command.

- Reference

[17] 7.8.12

- Initial Condition
- -The IUT is in the Initiating state.

- Test Procedure
1. The Upper Tester sends the HCI\_LE\_Create\_Connection command with the Min\_CE\_Length &gt; Max\_CE\_Length and all other parameters set to valid values.
2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Status event with Status set to (0x12).

## 4.10.26 Reject LE Connection Rate Request when peer Shorter Connection Intervals Host Support not set

- Test Purpose

Verify that the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command when the peer device does not have the Shorter Connection Intervals (Host Support) bit set.

- Reference

[23] 7.8.154 [24] 5.1.33

- Initial Condition
- -The IUT is in the role specified in Table 4.80.
- -The IUT and the Lower Tester have a connection.
- -The Lower Tester does not have the Shorter Connection Intervals (Host Support) bit set.
- -The Lower Tester has initiated and completed a Feature Exchange procedure with the IUT with the Shorter Connection Intervals feature set in Page 1.
- Test Case Configuration

| Test Case | Role |
| HCI/CCO/BI-135-C [Reject LE Connection Rate Request when peer Shorter Connection Intervals Host Support not set, Peripheral] | Peripheral |
| HCI/CCO/BI-136-C [Reject LE Connection Rate Request when peer Shorter Connection Intervals Host Support not set, Central] | Central |

Table 4.80: Reject LE Connection Rate Request when peer Shorter Connection Intervals Host Support not set test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Connection\_Rate\_Request command to the IUT.
2. Perform either alternative 2A or 2B depending on the IUT's response.

Alternative 2A (Successful HCI\_Command\_Status):

- 2A.1 The IUT sends a successful HCI\_Command\_Status to the Upper Tester.
- 2A.2 The IUT sends an HCI\_LE\_Connection\_Rate\_Change event to the Upper Tester with Status set to 0x1A.

Alternative 2B (HCI\_Command\_Status with Status = 0x1A):

- 2B.1 The IUT sends an HCI\_Command\_Status to the Upper Tester with Status set to 0x1A.

- Expected Outcome

## Pass verdict

In Step 2, the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command.

## 4.10.27 Connection Rate commands, invalid parameters

- Test Purpose

Verify that the IUT rejects an HCI command with invalid parameters.

- Initial Condition
- -The IUT and the Lower Tester have a connection.
- -The Lower Tester has initiated and completed a Feature Exchange procedure with the IUT with the Shorter Connection Intervals feature set in Page 1.
- -The IUT and the Lower Tester have the Shorter Connection Intervals (Host Support) feature bit set.
- Test Case Configuration
- Test Procedure

Table 4.81: Connection Rate commands, invalid parameters test cases

| Test Case | Reference | HCI Command/Event |
| HCI/CCO/BI-137-C [Connection Rate commands, invalid parameters, HCI_LE_Connection_Rate_Request] | [23] 7.8.154 | HCI_LE_Connection_Rate_Request HCI_Command_Status |
| HCI/CCO/BI-138-C [Connection Rate commands, invalid parameters, HCI_LE_Set_Default_Rate_Parameters] | [23] 7.8.155 | HCI_LE_Set_Default_Rate_Parameters HCI_Command_Complete |

Repeat Steps 1 and 2 for each round in Table 4.82.

1. The Upper Tester sends the HCI Command/Event specified in Table 4.81 to the IUT with the Parameters in Table 4.82.
2. Perform either alternative 2A or 2B depending on the HCI Command/Event specified in Table 4.81.

Alternative 2A (HCI\_Command\_Complete):

- 2A.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12.

Alternative 2B (HCI\_Command\_Status):

Perform either alternative 2B.1 or 2B.2 depending on the IUT's response.

Alternative 2B.1 (Successful HCI\_Command\_Status):

2B.1.1 The IUT sends a successful HCI\_Command\_Status to the Upper Tester.

2B.1.2

The IUT sends an HCI\_LE\_Connection\_Rate\_Change event to the Upper Tester with Status set to 0x12.

Alternative 2B.2 (HCI\_Command\_Status with Status = 0x12):

- 2B.2.1 The IUT sends an HCI\_Command\_Status to the Upper Tester with Status set to 0x12.
3. The Upper Tester sends the HCI\_LE\_Read\_Minimum\_Supported\_Connection\_Interval command to the IUT and receives a successful HCI\_Command\_Complete event with the Minimum\_Supported\_Connection\_Interval parameters. If Minimum\_Supported\_Connection\_Interval is 375 µs, then the test ends with a Pass verdict.

4. The Upper Tester sends an HCI command specified in Table 4.81 to the IUT with Connection\_Interval\_Min set to the Minimum\_Supported\_Connection\_Interval from Step 4, 125 µs.
5. The IUT returns an error to the Upper Tester by executing Step 2 with a 0x20 Error code.
- Expected Outcome

Table 4.82: Connection Rate commands, invalid parameters rounds

| Round | Invalid Parameter |
| 1 | Connection_Interval_Min = 0x7D01 |
| 2 | Connection_Interval_Max = 0x0002 |
| 3 | Connection_Interval_Max = 0x7D01 |
| 4 | Connection_Interval_Min = 4 Connection_Interval_Max = 3 |
| 5 | Subrate_Min = 0 |
| 6 | Subrate_Min = 0x1F5 |
| 7 | Subrate_Max = 0 |
| 8 | Subrate_Max = 0x1F5 |
| 9 | Subrate_Min = 2 Subrate_Max = 1 |
| 10 | Max_Latency = 0x1F4 |
| 11 | Continuation_Number = 0x1F4 |
| 12 | Supervision_Timeout = 0x0009 |
| 13 | Supervision_Timeout = 0x0C81 |
| 14 | Min_CE_Length > Max_CE_Length |
| 15 | Min_CE_Length = 0x7D00 |
| 16 | Max_CE_Length = 0x7D00 |

## Pass verdict

In Step 2, the IUT rejects the HCI command with error code 0x12.

In Step 5, the IUT rejects the HCI command with error code 0x20.

## HCI/CCO/BI-139-C [Reject LE Connection Rate Request when Connection Parameters Request in progress]

- Test Purpose

Verify that the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command when the IUT has a Connection Parameters Request in progress.

- Reference

[23] 7.8.154

- [24] 5.1.33

- Initial Condition
- -The IUT is in the Peripheral role.
- -The IUT and the Lower Tester have a connection.
- -The IUT and the Lower Tester have the Shorter Connection Intervals (Host Support) feature bit set.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Connection\_Update command to the IUT with Max\_Latency set to 0x100.
2. The IUT sends an LL\_CONNECTION\_PARAM\_REQ PDU to the Lower Tester with Latency set to 0x100.
3. The Upper Tester sends an HCI\_LE\_Connection\_Rate\_Request command to the IUT with Max\_Latency set to 0x01.
4. The IUT may initiate and complete a Feature Exchange procedure with the Lower Tester with both devices setting the Shorter Connection Intervals feature in Page 1.
5. Perform either alternative 5A or 5B depending on the IUT's response.

Alternative 5A (Successful HCI\_Command\_Status):

- 5A.1 The IUT sends a successful HCI\_Command\_Status to the Upper Tester.
- 5A.2 The IUT sends an HCI\_LE\_Connection\_Rate\_Change event to the Upper Tester with Status &gt; 0.

Alternative 5B (HCI\_Command\_Status with Status &gt; 0):

- 5B.1 The IUT sends an HCI\_Command\_Status to the Upper Tester with Status &gt; 0.
- Expected Outcome

## Pass verdict

In Step 5, the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command.

## HCI/CCO/BI-140-C [Reject LE Connection Rate Request when Connection Subrate Request in progress]

## · Test Purpose

Verify that the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command when the IUT has a Connection Subrate Request in progress.

- Reference

[23] 7.8.154 [24] 5.1.33

- Initial Condition
- -The IUT is in the Peripheral role.
- -The IUT and the Lower Tester have a connection.
- -The IUT and the Lower Tester have the Shorter Connection Intervals (Host Support) feature bit set.

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Subrate\_Request command to the IUT with Max\_Latency set to 0x100.
2. The IUT may initiate and complete a Feature Exchange procedure with the Lower Tester with both devices setting the Shorter Connection Intervals feature in Page 1.
3. The IUT sends an LL\_SUBRATE\_REQ PDU to the Lower Tester with Max\_Latency set to 0x100.
4. The Upper Tester sends an HCI\_LE\_Connection\_Rate\_Request command to the IUT with Max\_Latency set to 0x01.
5. Perform either alternative 5A or 5B depending on the IUT's response.

Alternative 5A (Successful HCI\_Command\_Status):

- 5A.1 The IUT sends a successful HCI\_Command\_Status to the Upper Tester.
- 5A.2 The IUT sends an HCI\_LE\_Connection\_Rate\_Change event to the Upper Tester with Status &gt; 0.

Alternative 5B (HCI\_Command\_Status with Status &gt; 0):

- 5B.1 The IUT sends an HCI\_Command\_Status to the Upper Tester with Status &gt; 0.
- Expected Outcome

## Pass verdict

In Step 5, the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command.

## 4.10.28 Reject LE Connection Rate Request when a Channel Sounding procedure in progress

- Test Purpose

Verify that the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command when the IUT has a Channel Sounding procedure in progress.

- Reference

[23] 7.8.154

[24] 5.1.33

- Initial Condition
- -The IUT is in the Peripheral role.
- -The IUT and the Lower Tester have a connection.
- -The Lower Tester has initiated and completed a Feature Exchange procedure with the IUT with the Shorter Connection Intervals feature set in Page 1.
- -The maximum CS procedure duration is defined by the TSPX\_CS\_Max\_Procedure\_Duration IXIT value.
- -The IUT and the Lower Tester have completed the CS Security Start and Capabilities Exchange procedures and Set Default Settings with the CS Role set to the value specified in Table 4.83 and the Max\_Procedures\_Supported field a value different than 1.
- -The IUT and the Lower Tester have completed the CS Configuration Procedure with the parameters specified in Section 4.14.2.2, Default Channel Sounding Parameters, and Main\_Mode set to 1, Sub\_Mode\_Type set to 0xFF, Min\_Main\_Mode\_Steps set to 0, Max\_Main\_Mode\_Steps set to 0, and Mode\_0\_Steps set to 3.
- -The IUT and the Lower Tester have the Shorter Connection Intervals (Host Support) feature bit set.

- Test Case Configuration
- Test Procedure
1. The Lower Tester sends an LL\_CS\_REQ PDU to the IUT with Max\_Procedure\_Len set to 0x7D00 (20 s) or TSPX\_CS\_Max\_Procedure\_Duration (whichever is less), Procedure\_Interval set to 0x32, Procedure\_Count set to N\_Procedure, Subevent\_Len set to 2.5 ms, and all valid parameters.
2. The IUT sends an LL\_CS\_RSP PDU to the Lower Tester.
3. The Lower Tester sends an LL\_CS\_IND PDU to the IUT.
4. The IUT sends an HCI\_LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester with State set to 0x01.
5. The IUT and the Lower Tester exchange Mode-0 and Mode-1 CS\_SYNC procedures.
6. The Upper Tester sends an HCI\_LE\_Connection\_Rate\_Request command to the IUT.
7. Perform either alternative 7A or 7B depending on the IUT's response.

Table 4.83: Reject LE Connection Rate Request when a Channel Sounding procedure in progress test cases

| Test Case | Channel Sounding Role |
| HCI/CCO/BI-141-C [Reject LE Connection Rate Request when a Channel Sounding procedure in progress, Initiator] | Initiator |
| HCI/CCO/BI-142-C [Reject LE Connection Rate Request when a Channel Sounding procedure in progress, Reflector] | Reflector |

Alternative 7A (Successful HCI\_Command\_Status):

- 7A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 7A.2 The IUT sends an HCI\_LE\_Connection\_Rate\_Change event to the Upper Tester with Status set to 0x0C.
- Alternative 7B (HCI\_Command\_Status with Status = 0x0C):
- 7B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0C.
8. The Lower Tester sends an LL\_CS\_TERMINATE\_REQ PDU to the IUT with a CsProcCount.
9. The IUT sends an LL\_CS\_TERMINATE\_RSP PDU to the Lower Tester.
10. The IUT sends an HCI\_LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester with State set to 0x00.
- Expected Outcome

## Pass verdict

In Step 7, the IUT returns a 0x0C error code.

## 4.10.29 Reject LE Connection Rate Request when Connection\_Interval\_Max is Too Small

- Test Purpose

Verify that the IUT rejects the HCI\_LE\_Connection\_Rate\_Request command when the Connection\_Interval\_Max parameter is smaller than connIntervalRequired.

- Reference

[23] 7.8.154

[24] 5.1.33

- Initial Condition
- -The IUT is in the Peripheral role.
- -The IUT and the Lower Tester have a connection on the PHY specified in Table 4.84 with a 10 ms connection interval.
- -The Lower Tester has initiated and completed a feature exchange procedure (with page 1) with the IUT before initiating SCI.
- -The IUT and the Lower Tester have the Shorter Connection Intervals (Host Support) feature bit set.
- Test Case Configuration

Table 4.84: Reject LE Connection Rate Request when Connection\_Interval\_Max is Too Small test cases

| Test Case | PHY | DLE Supported |
| HCI/CCO/BI-143-C [Reject LE Connection Rate Request when Connection_Interval_Max is Too Small, LE 1M] | LE 1M | No |
| HCI/CCO/BI-144-C [Reject LE Connection Rate Request when Connection_Interval_Max is Too Small, LE 1M, DLE Supported] | LE 1M | Yes |
| HCI/CCO/BI-145-C [Reject LE Connection Rate Request when Connection_Interval_Max is Too Small, LE Coded] | LE Coded | No |
| HCI/CCO/BI-146-C [Reject LE Connection Rate Request when Connection_Interval_Max is Too Small, LE Coded, DLE Supported] | LE Coded | Yes |

## · Test Procedure

1. If DLE is supported as specified in Table 4.84, execute Step 1.
2. 1A. The Lower Tester sends an LL\_LENGTH\_REQ PDU to the IUT with the maximum values for MaxRxOctets, MaxRxTime, MaxTxOctets, and MaxTxTime for the PHY specified in Table 4.84.
3. 1B. The IUT sends an LL\_LENGTH\_RSP PDU to the Lower Tester with MaxRxOctets, MaxRxTime, MaxTxOctets, and MaxTxTime.
4. 1C. If the values in either the LL\_LENGTH\_REQ or LL\_LENGTH\_RSP PDUs mean the connEffectiveMaxRxTime have changed, the IUT sends an
5. connEffectiveMaxTxOctets, connEffectiveMaxRxOctets, connEffectiveMaxTxTime, or HCI\_LE\_Data\_Length\_Change event to the Upper Tester with Max\_TX\_Octets, Max\_TX\_Time, Max\_RX\_Octets, and Max\_RX\_Time.
2. Perform either alternative 2A or 2B depending on DLE support specified in Table 4.84. Alternative 2A (DLE is supported):
7. 2A.1 The Upper Tester sends an HCI\_LE\_Connection\_Rate\_Request command to the IUT with Connection\_Interval\_Max set to a value one less than T\_IFS\_ACL\_CP + T\_MCES + min(connEffectiveMaxRxTime, ((connEffectiveMaxRxOctets × 64) + 976)).
8. 2A.2 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x11.
9. Alternative 2B (DLE is not supported):
10. 2B.1 The Upper Tester sends an HCI\_LE\_Connection\_Rate\_Request command to the IUT with Connection\_Interval\_Max set to one less than T\_IFS\_ACL\_CP + T\_MCES + connEffectiveMaxRxTime where connEffectiveMaxRxTime = 328 us for the LE 1M PHY and connEffectiveMaxRxTime = 2704 us for the LE Coded PHY.

## 2B.2 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x11 or 0x20.

- Expected Outcome

## Pass verdict

In Step 2A.2, the IUT returns a 0x11 error code.

In Step 2B.2, the IUT returns a 0x11 or 0x20 error code.

## HCI/CCO/BI-147-C [Reject LE Connection Update command when Connection Parameters Request in progress]

- Test Purpose

Verify that the IUT rejects the HCI\_LE\_Connection\_Update command when the IUT has a Connection Parameters Request in progress.

- Reference

[23] 7.8.18

- Initial Condition
- -The IUT is in the Peripheral role.
- -The IUT and the Lower Tester have a connection.
- -The IUT and the Lower Tester have the Shorter Connection Intervals (Host Support) feature bit set.
- -The Lower Tester has initiated and completed a Feature Exchange Procedure with the IUT with the Shorter Connection Intervals feature set in Page 1.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Connection\_Rate\_Request command to the IUT with Max\_Latency set to 0x100.
2. The IUT sends an LL\_CONNECTION\_RATE\_REQ PDU to the Lower Tester with Max\_Latency set to 0x100.
3. The Lower Tester does not send the LL\_CONNECTION\_RATE\_IND PDU to the IUT.
4. The Upper Tester sends an HCI\_LE\_Connection\_Update command to the IUT with Max\_Latency set to 0x101.
5. The IUT sends an HCI\_Command\_Status to the Upper Tester with Status set to 0x0C.
6. The Lower Tester sends an LL\_CONNECTION\_RATE\_IND PDU to the IUT.
7. The IUT sends an HCI\_LE\_Connection\_Rate\_Change event with Status set to 0x00.
- Expected Outcome

## Pass verdict

In Step 5, the IUT sends a 0x0C error.

In Step 7, the IUT sends a successful HCI event.

## HCI/CCO/BI-148-C [Reject the LE CS Procedure Enable command if the Security Start procedure has not completed, Central]

- Test Purpose

Verify that a Central IUT that has a Security Start procedure in progress rejects an Upper Tester initiating an LE CS Procedure Enable command.

- Reference

[18] 5.1.23

- Initial Condition
- -The IUT is in the Central role.
- -Encrypted Connection: The IUT and the Lower Tester have an encrypted connection, exchanged capabilities, and set default settings, and have created a configuration.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_CS\_Security\_Enable command to the IUT.
2. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
3. The IUT sends an LL\_CS\_SEC\_REQ PDU to the Lower Tester.
4. The Lower Tester does not send an LL\_CS\_SEC\_RSP PDU to the IUT.
5. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT.
6. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status &gt; 0.
7. The Lower Tester sends an LL\_CS\_SEC\_RSP PDU to the IUT.
8. The IUT sends a successful HCI\_LE\_CS\_Security\_Enable\_Complete event to the Upper Tester.
- Expected Outcome

## Pass verdict

In Step 6, the IUT sends an HCI\_Command\_Status event to the Upper Tester with a valid error code.

In Step 8, the IUT sends a successful event to the Upper Tester.

## 4.10.30 CS Set Security Requirements, Unsupported Feature

- Test Purpose

Verify that the CS Security Requirements command returns a 0x11 error when the IUT does not support the security parameter.

- Reference

[25] 7.8.157, 7.8.158

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection and have exchanged capabilities.
- Test Case Configuration

| Test Case | Feature |
| HCI/CCO/BI-150-C [CS Set Security Requirements, Unsupported Feature, CS Tone] | CS tone |
| HCI/CCO/BI-151-C [CS Set Security Requirements, Unsupported Feature, 150 ns RTT] | 150 ns RTT accuracy |

Table 4.85: CS Set Security Requirements, Unsupported Feature test cases

| Test Case | Feature |
| HCI/CCO/BI-152-C [CS Set Security Requirements, Unsupported Feature, 10 ns RTT] | 10 ns RTT accuracy |
| HCI/CCO/BI-153-C [CS Set Security Requirements, Unsupported Feature, RTT Sounding or Random Sequence] | RTT Sounding or Random Sequence |
| HCI/CCO/BI-154-C [CS Set Security Requirements, Unsupported Feature, NADM] | NADM |

- Test Procedure

Repeat the test steps for each round in Table 4.86.

1. The Upper Tester sends the HCI command specified in Table 4.86 with the Feature specified in Table 4.85.
2. The IUT sends an HCI\_Command\_Complete event with Status set to 0x11.
- Expected Outcome

Table 4.86: CS Set Security Requirements, Unsupported Feature rounds

| Round | Command (Step 3) |
| 1 | LE CS Set Security Requirements |
| 2 | LE CS Set Default Security Requirements |

## Pass verdict

In Step 2, the IUT sends a 0x11 error to the Upper Tester.

## HCI/CCO/BI-155-C [LE CS Set Security Requirements, CS procedure in progress]

- Test Purpose

Verify that the IUT rejects the LE CS Set Security Requirements command when a CS procedure is in progress.

- Reference

[25] 7.8.157

- Initial Condition
- -The IUT and the Lower Tester have an encrypted connection, read the remote FAE, exchanged capabilities, executed the CS Security procedure, and set default settings.

## · Test Procedure

Figure 4.118: LE CS Set Security Requirements, CS procedure in progress MSC

1. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with parameters set to valid values and Config\_ID set to 0.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x12 (Invalid HCI Command Parameters).
3. The Upper Tester sends an HCI\_LE\_CS\_Create\_Config command to the IUT with parameters set to valid values and Config\_ID set to 0 and receives a successful HCI\_Command\_Status in response.
4. The IUT and the Lower Tester complete the CS configuration procedure.
5. The IUT sends a successful HCI\_LE\_CS\_Config\_Complete event in response.
6. The Upper Tester sends an HCI\_LE\_CS\_Set\_Procedure\_Parameters command to the IUT with Config\_ID set to 0 and receives a successful HCI\_Command\_Complete event in response.
7. The Upper Tester sends an HCI\_LE\_CS\_Procedure\_Enable command to the IUT with Config\_ID set to 0 and Enable set to 0x01.
8. The IUT sends a successful HCI\_Command\_Status event in response.
9. The IUT sends an LL\_CS\_REQ PDU to the Lower Tester.
10. The Lower Tester sends an LL\_CS\_RSP PDU to the IUT.

11. The IUT sends a successful HCI\_LE\_CS\_Procedure\_Enable\_Complete event to the Upper Tester.
12. The Upper Tester sends an HCI\_LE\_CS\_Set\_Security\_Requirements command to the IUT.
13. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

## Pass verdict

In Step 13, the IUT sends a 0x0C error to the Upper Tester.

## 4.11 Controller Setup

## HCI/CSE/BV-01-C [Logical Link Cancel Command]

- Test Purpose

Verify that the Logical Link Cancel command does cancel a Create Logical Link command before the logical link is totally established.

- Reference

[1] 7.1.40, 7.1.43

- Initial Condition
- -The IUT is the initiator.
- Test Procedure

The Upper Tester sends Create Logical Link command to the IUT.

The Upper Tester receives command status event with success.

The Upper Tester sends Logical Link Cancel command right away.

Figure 4.119: HCI/CSE/BV-01-C [Logical Link Cancel Command] MSC

- Expected Outcome

## Pass verdict

Command Complete event for Logical Link Cancel is received by the Upper Tester.

Logical Link Complete event with error code Unknown Connection Identifier (0x02) is received by the Upper Tester.

## HCI/CSE/BV-02-C [Logical Link Cancel Command]

- Test Purpose

Verify that the Logical Link Cancel command does cancel a Create Logical Link command before the logical link is totally established.

- Reference

[1] 7.1.41, 7.1.43

- Initial Condition
- -The IUT is the responder and it has received Accept Logical Link Request command.
- Test Procedure

The Upper Tester sends Accept Logical Link command to the IUT.

The Upper Tester receives command status event with success.

The Upper Tester sends Logical Link Cancel command right away.

Figure 4.120: HCI/CSE/BV-02-C: [Logical Link Cancel Command] MSC

- Expected Outcome

## Pass verdict

Command Complete event for Logical Link Cancel is received by the Upper Tester.

Logical Link Complete event with error code Unknown Connection Identifier (0x02) is received by the Upper Tester.

## HCI/CSE/BI-03-C [Logical Link Cancel Command]

- Test Purpose

Verify that the Logical Link Cancel command is handled correctly after the logical link has been established already.

- Reference

[1] 7.1.43

- Initial Condition
- -The IUT and the Lower Tester have a Logical Link established already.
- Test Procedure

The Upper Tester sends Logical Link Cancel command to the IUT.

Figure 4.121: HCI/CSE/BI-03-C [Logical Link Cancel Command] MSC

- Expected Outcome

## Pass verdict

Command Complete event for Logical Link Cancel is received by the Upper Tester with error code ACL Connection Already Exists (0x0B).

## HCI/CSE/BI-04-C [Logical Link Cancel Command]

- Test Purpose

Verify that the Logical Link Cancel command is handled correctly if there is no logical link or an invalid logical link handle is given.

- Reference

[1] HCI 7.1.43

- Initial Condition
- -The IUT and the Lower Tester do not have any Logical Links established.
- Test Procedure

The Upper Tester sends Logical Link Cancel command to the IUT.

Figure 4.122: HCI/CSE/BI-04-C [Logical Link Cancel Command] MSC

- Expected Outcome

## Pass verdict

Command Complete event for Logical Link Cancel is received by the Upper Tester with error code Unknown Connection Identifier (0x02).

## HCI/CSE/BV-05-C [Write Logical Link Accept Timeout Command/Read Logical Link Accept Timeout Command]

- Test Purpose

Verify that the Write Logical Link Accept Timeout Command and Read Logical Link Accept Timeout Command are handled correctly by the IUT.

- Reference

[1] 7.3.15, 7.3.16

- Initial Condition
- -The IUT is in standby.
- Test Procedure

The Upper Tester issues Write Logical Link Accept Timeout Command with preset information to the IUT.

The Upper Tester receives success status in the Write Logical Link Accept Timeout Command complete event.

The Upper Tester issues Read Logical Link Accept Timeout Command with preset information to the IUT.

Figure 4.123: HCI/CSE/BV-05-C [Write Logical Link Accept Timeout Command/Read Logical Link Accept Timeout Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives command complete event with success status for two commands. The Upper Tester receives the data returned by the Read Logical Link Accept Timeout Command complete event. The received data matches that was used in the Write Logical Link Accept Timeout Command.

## HCI/CSE/BV-06-C [Verify Truncated Paging]

- Test Purpose

Verify that the Truncated Page command configures the IUT to perform a Truncated Page procedure. Verify that the IUT generates Truncated Page Complete event.

- Reference

[1] 7.1, 7.7

- Initial Condition
- -The IUT is in Standby.
- -The Lower Tester is performing R1 Interlaced Scans.

- Test Procedure

The Upper Tester sends HCI Truncated Page command to the IUT and receives HCI Command Status pending.

Figure 4.124: HCI/CSE/BV-06-C [Verify Truncated Paging] MSC

- Expected Outcome

## Pass verdict

The IUT performs a Truncated Page procedure on the Lower Tester AND

The IUT generates a Truncated Page Complete event with Status = Success.

## HCI/CSE/BV-07-C [Page Response Timeout Detection]

- Test Purpose

Verify that the IUT generates a Page Response Timeout event.

- Reference

## 1 7.7

- Initial Condition
- -The IUT is configured for R1 Page Scans.
- -The Lower Tester is in Standby.

- Test Procedure

The Lower Tester performs Truncated Paging on the IUT.

Figure 4.125: HCI/CSE/BV-07-C [Page Response Timeout Detection] MSC

- Expected Outcome

## Pass verdict

The IUT generates a Page Response Timeout event.

## HCI/CSE/BV-08-C [LE Set Host Feature Command During Connection, Initiator]

- Test Purpose

Verify that the Initiator IUT returns an error when the Upper Tester sends an HCI\_LE\_Set\_Host\_Feature command after a connection is completed with the Lower Tester.

- Reference

## 13 7.8.115

- Initial Condition
- -The IUT is the Initiator.

Figure 4.126: HCI/CSE/BV-08-C [LE Set Host Feature Command During Connection, Initiator] MSC

1. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT with Peer\_Address\_Type set to 0x00 and Peer\_Address set to the Lower Tester's public address , and it receives a successful HCI\_Command\_Status event in return.
2. The Lower Tester is configured to start advertising with a public address.
3. After receiving an ADV\_IND PDU from the Lower Tester, the IUT sends a CONNECT\_IND PDU to the Lower Tester with InitA set to the IUT public address.
4. The IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester.
5. The Upper Tester sends an HCI\_LE\_Set\_Host\_Feature command with Bit\_Number set to a supported feature bit and Bit\_Value set to 0x01.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

## Pass verdict

In Step 6, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.

## HCI/CSE/BV-09-C [LE Set Host Feature Command During Connection, Advertiser]

- Test Purpose

Verify that the Advertiser IUT returns an error when the Upper Tester sends an HCI\_LE\_Set\_Host\_Feature command after a connection is completed with the Lower Tester.

- Reference

## 13 7.8.115

- Initial Condition
- -The IUT is the Advertiser.

·

Figure 4.127: HCI/CSE/BV-09-C [LE Set Host Feature Command During Connection, Advertiser] MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Parameters command to the IUT with Advertising\_Type set to 0x00 and Own\_Address\_Type set to 0x00, and it receives a successful HCI\_Command\_Complete event in return.
2. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Data command to the IUT with Advertising\_Data\_Length set to 0, and it receives a successful HCI\_Command\_Complete event in return.
3. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Enable command to the IUT with Enable set to 0x01, and it receives a successful HCI\_Command\_Complete event in return.
4. After receiving an ADV\_IND PDU, the Lower Tester sends a CONNECT\_IND PDU to the IUT with InitA set to the Lower Tester public address.
5. The IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester.
6. The Upper Tester sends an HCI\_LE\_Set\_Host\_Feature command with Bit\_Number set to a supported feature bit and Bit\_Value set to 0x01.
7. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

## Pass verdict

In Step 7, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.

## 4.12 Connectionless Peripheral Broadcast

Verify the correct implementation of Connectionless Peripheral Broadcast commands and events.

Verify the correct implementation of Synchronization Train commands and events.

Verify the correct implementation of Truncated Page commands and events.

## HCI/CPB/BV-01-C [Connectionless Peripheral Broadcast Transmission]

- Test Purpose

Verify that:

- -The Set Reserved LT ADDR command reserves the correct LT ADDR on the IUT for Connectionless Broadcast.
- -The Write Synchronization Train Parameters command configures Synchronization Train parameters on the IUT.
- -The Read Synchronization Train Parameters command retrieves previously configured Synchronization Train parameters from the IUT.
- -The Set Connectionless Peripheral Broadcast Data command correctly configures the IUT to transmit the provided data.
- -The Set Connectionless Peripheral Broadcast command correctly configures the IUT to transmit Connectionless Broadcast packets.
- -The Start Synchronization Train command starts the Synchronization Train on the IUT.
- -The IUT sends a Synchronization Train Complete event to the Upper Tester after the Synchronization train completes after the configured time.
- Reference

[1] 7.1, 7.3, 7.7

- Initial Condition
- -The IUT is in Standby.
- Test Procedure
1. The Upper Tester sends HCI Set Reserved LT\_ADDR command to the IUT and receives HCI Command Complete with Status = Success.
2. The Upper Tester sends HCI Write Synchronization Train parameters and receives HCI Command Complete with Status = Success.
3. The Upper Tester sends HCI Read Synchronization Train parameters and receives HCI Command Complete with Status = Success and Synchronization Train parameters that match the values set in Step 2.
4. The Upper Tester sends HCI Set Connectionless Broadcast Data command to the IUT and receives HCI Command Complete with Status = Success.
5. The Upper Tester sends HCI Set Connectionless Broadcast command to the IUT and receives HCI Command Complete with Status = Success.
6. The Upper Tester sends HCI Start Synchronization Train command to the IUT and receives HCI Command Complete with Status = Success.

Figure 4.128: HCI/CPB/BV-01-C [Connectionless Peripheral Broadcast Transmission] MSC

## · Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set Reserved LT ADDR command AND The IUT returns 'command complete' succeeded to the Write Synchronization Train Parameters command AND

The IUT returns 'command complete' succeeded with the previously configured Synchronization Train parameters as a result of the Read Synchronization Train Parameters command AND

The IUT returns 'command complete' succeeded to the Set Connectionless Peripheral Broadcast Data command AND

The IUT returns 'command complete' succeeded to the Set Connectionless Peripheral Broadcast command AND

The IUT returns 'command status' pending to the Start Synchronization Train command AND

The Lower Tester successfully synchronizes to the IUT AND

The Lower Tester successfully receives broadcast data AND

The IUT returns 'synchronization train complete' event after the configured Synchronization Train duration.

## HCI/CPB/BV-02-C [Delete Reserved LT ADDR]

- Test Purpose

Verify that the Delete Reserved LT ADDR command cancels the reservation of a specific LT\_ADDR.

- Reference

[1] 7.3

- Initial Condition
- -The IUT is in Standby.
- Test Procedure

The Upper Tester sends HCI Set Reserved LT\_ADDR command to the IUT and receives HCI Command Complete with Status = Success.

The Upper Tester sends HCI Delete Reserved LT\_ADDR command and receives HCI Command Complete with Status = Success.

Figure 4.129: HCI/CPB/BV-02-C [Delete Reserved LT ADDR] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set Reserved LT\_ADDR command AND The IUT returns 'command complete' succeeded to the Delete Reserved LT\_ADDR command .

## HCI/CPB/BV-03-C [CPB Channel Map Change Event]

- Test Purpose

Verify that the IUT generates a Connectionless Peripheral Broadcast Channel Map Change event when the channel map for Connectionless Peripheral Broadcast changes.

- Reference

## 1 7.7

- Initial Condition
- -The IUT is in Standby.
- Test Procedure

The Upper Tester sends HCI Set Reserved LT\_ADDR command to the IUT and receives HCI Command Complete with Status = Success.

The Upper Tester sends HCI Write Synchronization Train parameters and receives HCI Command Complete with Status = Success.

The Upper Tester sends Set AFH Host Channel Classification command and receives HCI Command Complete with Status = Success.

The Upper Tester sends HCI Set Connectionless Broadcast command to the IUT and receives HCI Command Complete with Status = Success.

## The Upper Tester sends Set AFH Host Channel Classification command and receives HCI Command Complete with Status = Success.

Figure 4.130: HCI/CPB/BV-03-C [CPB Channel Map Change Event] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command complete' succeeded to the Set Reserved LT ADDR command AND

The IUT returns 'command complete' succeeded to the Write Synchronization Train Parameters command AND

The IUT returns 'command complete' succeeded to the Set AFH Host Channel Classification command AND

The IUT returns 'command complete' succeeded to the Set Connectionless Peripheral Broadcast command AND

The IUT returns 'command complete' succeeded to the Set AFH Host Channel Classification command AND

The IUT generate a Connectionless Peripheral Broadcast Channel Map change event with the channel map from the previous Set AFH Host Channel Classification command.

## HCI/CPB/BV-04-C [Connectionless Peripheral Broadcast Reception]

- Test Purpose

Verify that:

- a) The Receive Synchronization Train command configures the IUT to receive Synchronization Train
- b) The IUT generates Synchronization Train Received events
- c) The Set Connectionless Peripheral Broadcast Receive command configures the IUT to receive Connectionless Peripheral Broadcast packets
- d) The IUT generates Connectionless Broadcast Receive events
- Reference

[1] 7.1, 7.3, 7.7

- Initial Condition
- -The IUT is in Standby.
- -The Lower Tester is transmitting Connectionless Peripheral Broadcast packets using the following parameters:
- -LT\_ADDR: 1
- -LPO\_Allowed: 0 (No)
- -Packet\_Type: 0x330E (only DM1 packets allowed)
- -Interval: 0x0080 (80 ms)
- -Data\_Length = 0x02
- -Data = [0xAA, 0x55]
- -The Lower Tester is transmitting Synchronization Train continuously with an interval of 0x0080.

## · Test Procedure

The Upper Tester sends HCI Receive Synchronization Train command to the IUT and receives HCI Command Status pending.

The IUT generates a Synchronization Train Received event.

The Upper Tester uses the parameters from the Synchronization Train Received event to send the HCI Set Connectionless Broadcast Receive command and receives HCI Command Complete with Status = Success.

Figure 4.131: HCI/CPB/BV-04-C [Connectionless Peripheral Broadcast Reception] MSC

- Expected Outcome

## Pass verdict

The IUT returns 'command status' pending to the Receive Synchronization Train command AND

The IUT generates a Synchronization Train Received event AND

The IUT generates Connectionless Peripheral Broadcast Receive events with data transmitted by the Lower Tester.

## HCI/CPB/BV-05-C [Connectionless Peripheral Broadcast Reception Timeout]

- Test Purpose

Verify that the IUT generates Connectionless Peripheral Broadcast Timeout event.

- Reference

## 1 7.7

- Initial Condition
- -The IUT is in Standby.
- -The Lower Tester is transmitting Connectionless Peripheral Broadcast packets using the following parameters:
- -LT\_ADDR: 1
- -LPO\_Allowed: 0 (No)
- -Packet\_Type: 0x330E (only DM1 packets allowed)
- -Interval: 0x0080 (80 ms)
- -Data\_Length = 0x02
- -Data = [0xAA, 0x55]
- -The Lower Tester is transmitting Synchronization Train continuously with an interval of 0x0080.
- Test Procedure

The Upper Tester sends HCI Receive Synchronization Train command to the IUT and receives HCI Command Status pending.

The IUT generates a Synchronization Train Received event.

The Upper Tester uses the parameters from the Synchronization Train Received event to send the HCI Set Connectionless Broadcast Receive command and receives HCI Command Complete with Status = Success.

The IUT generates Connectionless Peripheral Broadcast Receive events.

Stop Connectionless Peripheral Broadcast from the Lower Tester.

The IUT generates Connectionless Peripheral Broadcast Timeout after the configured timeout period has expired.

Figure 4.132: HCI/CPB/BV-05-C [Connectionless Peripheral Broadcast Reception Timeout] MSC

- Expected Outcome

## Pass verdict

The IUT generates Connectionless Peripheral Broadcast Timeout event.

## 4.13 LE Connection Management

## HCI/CM/BV-01-C [LE Read Peer Resolvable Address Command -Central]

- Test Purpose

Verify that the IUT correctly handles the LE Read Peer Resolvable Address Command.

- Reference

[8] 7.8.42

- Initial Condition
- -The IUT is Central.
- Test Procedure

The Upper Tester populates the resolving list with the device identity of the Lower Tester, and its own device identity. The IUT uses this when generating a resolvable private address for the connection establishment.

The Upper Tester enables resolving list.

Configure the Lower Tester to initiate a connection while using directed advertisement with resolvable private addresses.

The Upper Tester commands the IUT to create a connection to the Lower Tester.

The IUT sends an LE Enhanced Connection Complete Event.

The Upper Tester issues a LE Read Peer Resolvable Address Command, with the identity address of the Lower Tester.

The Upper Tester receives a Command Complete event from the IUT for the LE Read Peer Resolvable Address Command with the Lower Tester's resolvable address.

Figure 4.133: HCI/CM/BV-01-C [LE Read Peer Resolvable Address Command -Central] MSC

## · Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status=0x00 (Success) and Peer\_resolvable\_address=0xXXXXXXXXXXXX.

The received resolvable address is identical with the Peer\_Resolvable\_Private\_Address received in the enhanced connection complete event.

## HCI/CM/BV-02-C [LE Read Local Resolvable Address Command -Central]

- Test Purpose

Verify that the IUT correctly handles the LE Read Local Resolvable Address Command

- Reference

[8] 7.8.43

- Initial Condition
- -The IUT is Central.
- Test Procedure

The Upper Tester populates the resolving list with the device identity of the Lower Tester, and its own device identity. The IUT uses this when generating a resolvable private address for the connection establishment.

The Upper Tester enables resolving list.

Configure the Lower Tester to initiate a connection while using directed advertisement with resolvable private addresses.

The Upper Tester command the IUT to create a connection to the Lower Tester.

The IUT sends an LE Enhanced Connection Complete Event.

The Upper Tester issues a LE Local Peer Resolvable Address Command, with the identity address of the Lower Tester.

The Upper Tester receives a Command Complete event from the IUT for the LE Local Peer Resolvable Address Command with the local resolvable address.

Figure 4.134: HCI/CM/BV-02-C [LE Read Local Resolvable Address Command -Central] MSC

## · Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status=0x00 (Success) and Local\_Resolvable\_Address=0xXXXXXXXXXXXX.

The received resolvable address is identical with the Local\_Resolvable\_Private\_Address received in the enhanced connection complete event.

## HCI/CM/BV-03-C [LE Read PHY Command]

- Test Purpose

Verify that the IUT correctly handles the LE Read PHY Command.

- Reference

[9] 7.8.47

- Initial Condition
- -LL connection established, the IUT is Central or Peripheral.
- Test Procedure

The Upper Tester issues an LE Read PHY command to the IUT containing the current connection handle.

The Upper Tester receives a Command Complete event from the IUT for the LE Read PHY command containing the connection handle and with values for TX\_PHY and RX\_PHY that match the current PHY for the active connection.

Figure 4.135: HCI/CM/BV-03-C [LE Read PHY Command] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success) and with the value for Connection\_Handle matching the value sent in the LE Read PHY Command.

The TX\_PHY and RX\_PHY fields contain values which match the PHY selected for the current active connection.

## HCI/CM/BV-04-C [Extended Scanning with Device Privacy, RPA Timeout During Connection Initiation]

## · Test Purpose

Verify that when the IUT is initiator and an RPA Timeout occurs between the IUT issuing an AUX\_CONNECT\_REQ PDU and the Lower Tester responding with an AUX\_CONNECT\_RSP PDU, the HCI\_LE\_Enhanced\_Connection\_Complete event returns the latest Peer\_Address, Peer\_Resolvable\_Private\_Address, and Local\_Resolvable\_Private\_Address sent and received over the air.

- Reference

[11] 7.7.65.10

- Initial Condition
- -The Lower Tester has previously distributed its IRK to the IUT.
- -The IUT has previously distributed its IRK to the Lower Tester.
- -The Lower Tester has added the IUT to its resolving list and sets the entry for device privacy mode.
- -The IUT has added the Lower Tester to its resolving list and sets the entry for device privacy mode.
- -Device privacy mode is enabled on the IUT and the Lower Tester.
- -The Lower Tester is using its Identity Address in the AdvA field of the advertisement packets.
- Test Procedure

Figure 4.136: HCI/CM/BV-04-C [Extended Scanning with Device Privacy, RPA Timeout During Connection Initiation] MSC

1. The Upper Tester sends an HCI\_LE\_Extended\_Create\_Connection command to the IUT. The peer address and address type is set to the ones used by the Lower Tester. The Upper Tester receives an HCI\_Command\_Status event in response.
2. The Lower Tester begins advertising using the ADV\_EXT\_IND PDU with the AuxPtr field referencing the AUX\_ADV\_IND.
3. The Lower Tester receives an AUX\_CONNECT\_REQ PDU on the secondary advertising channel after sending any of the AUX\_ADV\_IND PDUs.
4. An RPA Timeout is simulated on the Lower Tester.
5. The Lower Tester sends an AUX\_CONNECT\_RSP PDU to the IUT on the secondary advertising channel with a new RPA.
6. The Upper Tester receives an HCI\_LE\_Enhanced\_Connection\_Complete event from the IUT.
- Expected Outcome

## Pass verdict

The test procedure completes with the IUT establishing a connection with the Lower Tester.

The HCI\_LE\_Enhanced\_Connection\_Complete event returns the latest Peer\_Address, Peer\_Resolvable\_Private\_Address and Local\_Resolvable\_Private\_Address sent and received over the air.

## HCI/CM/BV-05-C [LE Read Peer Resolvable Address Command -Peripheral]

- Test Purpose

Verify that the IUT correctly handles the LE Read Peer Resolvable Address Command.

- Reference

[2] 7.8.42

- Initial Condition
- -The IUT is Peripheral.
- Test Procedure

The Upper Tester populates the resolving list with the device identity of the Lower Tester, and its own device identity. The IUT uses this when generating a resolvable private address for the connection establishment.

The Upper Tester enables resolving list.

Configure the Lower Tester to initiate a connection while using resolvable private addresses.

The Upper Tester enables resolving list and directed connectable advertising in the IUT.

The IUT sends an LE Enhanced Connection Complete Event.

The Upper Tester issues a LE Read Peer Resolvable Address Command, with the identity address of the Lower Tester.

The Upper Tester receives a Command Complete event from the IUT for the LE Read Peer Resolvable Address Command with the Lower Tester's resolvable address.

Figure 4.137: HCI/CM/BV-05-C [LE Read Peer Resolvable Address Command -Peripheral] MSC

## · Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status=0x00 (Success) and Peer\_resolvable\_address=0xXXXXXXXXXXXX.

The received resolvable address is identical with the Peer\_Resolvable\_Private\_Address received in the enhanced connection complete event.

## HCI/CM/BV-06-C [LE Read Local Resolvable Address Command -Peripheral]

- Test Purpose

Verify that the IUT correctly handles the LE Read Local Resolvable Address Command.

- Reference

[2] 7.8.43

- Initial Condition
- -The IUT is Peripheral.
- Test Procedure

The Upper Tester populates the resolving list with the device identity of the Lower Tester, and its own device identity. The IUT uses this when generating a resolvable private address for the connection establishment.

The Upper Tester enables resolving list.

Configure the Lower Tester to initiate a connection while using resolvable private addresses.

The Upper Tester enables resolving list and directed connectable advertising in the IUT.

The IUT sends an LE Enhanced Connection Complete Event.

The Upper Tester issues a LE Local Peer Resolvable Address Command, with the identity address of the Lower Tester.

The Upper Tester receives a Command Complete event from the IUT for the LE Local Peer Resolvable Address Command with the local resolvable address.

Figure 4.138: HCI/CM/BV-06-C [LE Read Local Resolvable Address Command -Peripheral] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status=0x00 (Success) and Local\_Resolvable\_Address=0xXXXXXXXXXXXX.

The received resolvable address is identical with the Local\_Resolvable\_Private\_Address received in the enhanced connection complete event.

## HCI/CM/BI-01-C [LE Extended Create Connection With Unsupported PHY]

- Test Purpose

Verify that the IUT properly rejects an HCI\_LE\_Extended\_Create\_Connection command that specifies unsupported PHYs.

- Reference

[9] 7.8.66

- Initial Condition
- -The IUT is not currently connected.
- Test Procedure

For each bit on the Initiating\_PHYs parameter of the HCI\_LE\_Extended\_Create\_Connection command that is an RFU bit or corresponds to a PHY not supported by the IUT:

The Upper Tester sends an HCI\_LE\_Extended\_Create\_Connection command to the IUT with Initiating\_PHYs having only that bit set and receives an HCI\_Command\_Complete event with a nonzero status.

Figure 4.139: HCI/CM/BI-01-C [LE Extended Create Connection With Unsupported PHY] MSC

- Expected Outcome

If the IUT supports PHYs corresponding to all 8 bits of the Initiating\_PHYs parameter, the test procedure will do nothing. This case is a Pass.

## Pass verdict

Command Complete event for HCI\_LE\_Extended\_Create\_Connection is received by the Upper Tester with the error code Unsupported Feature or Parameter Value (0x11).

## HCI/CM/BV-07-C [Request Sleep Clock Accuracy, unsupported SCA Update Feature]

- Test Purpose

Verify that when the IUT reads the peer's Sleep Clock Accuracy of a peer that doesn't support the Sleep Clock Accuracy Update feature, the Controller returns the error code Unsupported Remote Feature/Unsupported LMP Feature (0x1A).

- Reference

[12] 7.8.108

- Initial Condition
- -The IUT is connected to the Lower Tester.
- -The Lower Tester does not support the Sleep Clock Accuracy Update feature.
- -A feature exchange has been executed between the IUT and the Lower Tester.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Request\_Peer\_SCA command to the IUT.
2. The IUT returns an error code using one of the two following alternate test steps:

Figure 4.140: HCI/CM/BV-07-C [Request Sleep Clock Accuracy, unsupported SCA Update Feature] MSC

Alternate 1:

3. The IUT sends the Upper Tester an HCI\_Command\_Status event with status Unsupported Remote Feature/Unsupported LMP Feature (0x1A).

Alternate 2:

4. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
5. The IUT sends an HCI\_LE\_Request\_Peer\_SCA\_Complete event with Status set to Unsupported Remote Feature/Unsupported LMP Feature (0x1A).
- Expected Outcome

## Pass verdict

In Step 3, the IUT sends an HCI\_Command\_Status event to the Upper Tester with the status of 0x1A.

In Step 5, the IUT sends an HCI\_LE\_Request\_Peer\_SCA\_Complete event to the Upper Tester with an Unsupported Remote Feature/Unsupported LMP Feature (0x1A) status.

## 4.13.1 LE Create Connection Cancel, Command Disallowed

- Test Purpose

Verify that when the IUT is initiator, it returns an error when the LE Create Connection Cancel command is called if no LE Create Connection or LE Extended Create Connection is pending.

- Reference

[11] 7.8.13

- Initial Condition
- -The Lower Tester is configured as an advertiser using all supported advertising channels and using a public address.
- Test Case Configuration
- Test Procedure

Table 4.87: LE Create Connection Cancel, Command Disallowed test cases

| Test Case | Connect Command |
| HCI/CM/BI-02-C | HCI_LE_Create_Connection |
| HCI/CM/BI-03-C | HCI_LE_Extended_Create_Connection |

Figure 4.141: LE Create Connection Cancel, Command Disallowed MSC

1. The Upper Tester sends an HCI\_LE\_Create\_Connection\_Cancel command to the IUT.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
3. The Upper Tester sends a Connect command as specified in Table 4.87 to the IUT with Peer\_Address\_Type set to 0x00 and Peer\_Address set to the Lower Tester's public address , and it receives a successful HCI\_Command\_Status event in return.
4. The Lower Tester begins advertising ADV\_IND packets.
5. The IUT sends a CONNECT\_IND PDU to the Lower Tester after receiving an ADV\_IND PDU.
6. The IUT sends an HCI\_LE\_Connection\_Complete event to the Upper Tester with Peer\_Address\_Type set to 0x00 and the Peer\_Address set to the Lower Tester's public address.
7. The Upper Tester sends an HCI\_LE\_Create\_Connection\_Cancel command to the IUT.
8. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

In Steps 3 and 8, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

## 4.13.2 Connection Attempt Rejected When Connected to the Peer

- Test Purpose

Verify that when the IUT is initiator and connected to the peer device, it returns an error when there is a connection request to the peer device.

- Initial Condition
- -The Lower Tester is configured as an advertiser using all supported advertising channels and using a public address.
- Test Case Configuration

Table 4.88: Connection Attempt Rejected When Connected to the Peer test cases

| Test Case ID | Reference | HCI Command/Event |
| HCI/CM/BI-04-C | [11] 7.8.12 | HCI_LE_Create_Connection HCI_LE_Connection_Complete |
| HCI/CM/BI-05-C | [11] 7.8.66 | HCI_LE_Extended_Create_Connection HCI_LE_Enhanced_Connection_Complete |

·

Figure 4.142: Connection Attempt Rejected When Connected to the Peer MSC

1. The Upper Tester sends an HCI command as specified in Table 4.88 to the IUT with Peer\_Address\_Type set to 0x00 and Peer\_Address set to the Lower Tester's public address, and it receives a successful HCI\_Command\_Status event in return.
2. The Lower Tester begins advertising ADV\_IND packets.
3. The IUT sends a CONNECT\_IND PDU to the Lower Tester after receiving an ADV\_IND PDU.
4. The IUT sends an HCI event as specified in Table 4.88 to the Upper Tester with Peer\_Address\_Type set to 0x00 and the Peer\_Address set to the Lower Tester's public address.
5. The Lower Tester continues advertising ADV\_IND packets.
6. The Upper Tester sends an HCI command as specified in Table 4.88 to the IUT with Peer\_Address\_Type set to 0x00 and Peer\_Address set to the Lower Tester's public address.
7. Perform alternative 7A or 7B depending on the IUT 's response.

Alternative 7A (HCI\_Command\_Status event with an error code):

- 7A.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Connection Already Exists (0x0B).

Alternative 7B (Successful HCI\_Command\_Status event):

- 7B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 7B.2 The IUT sends an HCI event as specified in Table 4.88 to the Upper Tester with Status set to Connection Already Exists (0x0B).
- Expected Outcome

## Pass verdict

In Step 7A.1 or 7B.2, the IUT sends a 0x0B error code.

## 4.14 LE Power Control

## HCI/PCL/BV-01-C [LE Enhanced Read Transmit Power Level]

- Test Purpose

Verify that the LE Enhanced Read Transmit Power Level command returns the current and maximum transmit power level of the local Controller on an ACL connection.

- Reference

[12] 7.8.117

- Initial Condition
- -ACL connection established, the IUT is Central or Peripheral.
- Test Procedure
1. The Upper Tester issues an LE Enhanced Read Transmit Power Level command to the IUT containing the current connection handle.
2. The Upper Tester receives a Command Complete event from the IUT for the LE Enhanced Read Transmit Power Level command containing the connection handle, the value for PHY matching the current PHY for the active connection, and the values for Current\_TX\_Power\_Level and Max\_TX\_Power\_Level as the current and maximum transmit power level of the local Controller for the active connection.

Figure 4.143: HCI/PCL/BV-01-C [LE Enhanced Read Transmit Power Level] MSC

- Expected Outcome

## Pass verdict

The Upper Tester receives a Command Complete event from the IUT with Status = 0x00 (Success) and with the value for Connection\_Handle matching the value sent in the LE Enhanced Read Transmit Power Level command.

The PHY field contains a value which matches the PHY selected for the current active connection, Current\_TX\_Power\_Level and Max\_TX\_Power\_Level in the range described in the specifications, with Current\_TX\_Power\_Level less than or equal to Max\_TX\_Power\_Level.

## 4.14.1 LE Enhanced Read Transmit Power Level with Unsupported or Invalid Parameters

- Test Purpose

Verify that the IUT properly handles the LE Enhanced Read Transmit Power Level command with unsupported or invalid parameters.

- Reference

[13] 7.8.117

- Initial Condition
- -ACL connection established, the IUT is Central or Peripheral.
- Test Case Configuration
- Test Procedure
1. The Upper Tester sends the HCI\_LE\_Enhanced\_Read\_Transmit\_Power\_Level command to the IUT with the parameter and value specified in Table 4.89.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set as specified in Table 4.89.
- Expected Outcome

Table 4.89: LE Enhanced Read Transmit Power Level with Unsupported or Invalid Parameters test cases

| Test Case | Parameter | Value | Status |
| HCI/PCL/BI-01-C | PHY | 0x02 (LE 2M) | 0x11 |
| HCI/PCL/BI-02-C | PHY | 0x03 (LE Coded S=8) | 0x11 |
| HCI/PCL/BI-03-C | PHY | 0x04 (LE Coded S=2) | 0x11 |
| HCI/PCL/BI-04-C | Connection_Handle | Not the current ACL | 0x02 |

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event with Status set as specified in Table 4.89.

## 4.14.2 LE Read Remote Transmit Power Level with Unsupported or Invalid Parameters

## · Test Purpose

Verify that the IUT properly handles the LE Read Remote Transmit Power Level command with unsupported or invalid parameters.

- Reference

[13] 7.8.118

- Initial Condition
- -ACL connection established, the IUT is Central or Peripheral.
- Test Case Configuration

| Test Case | Parameter | Value | Status |
| HCI/PCL/BI-05-C | PHY | 0x02 (LE 2M) | 0x11 |
| HCI/PCL/BI-06-C | PHY | 0x03 (LE Coded S=8) | 0x11 |
| HCI/PCL/BI-07-C | PHY | 0x04 (LE Coded S=2) | 0x11 |
| HCI/PCL/BI-08-C | Connection_Handle | Not the current ACL | 0x02 |

Table 4.90: LE Read Remote Transmit Power Level with Unsupported or Invalid Parameters test cases

## · Test Procedure

1. The Upper Tester sends the HCI\_LE\_Read\_Remote\_Transmit\_Power\_Level command to the IUT with the parameter and value specified in Table 4.90.
2. Perform either alternative 2A or 2B depending on whether the IUT sends the error status in the HCI\_Command\_Status event.
3. Alternative 2A (The IUT sends the error in the HCI\_Command\_Status event)
4. 2A.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set as specified in Table 4.90.
5. Alternative 2B (The IUT sends the error in the HCI\_LE\_Transmit\_Power\_Reporting event)
6. 2B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
7. 2B.2 The IUT sends an HCI\_LE\_Transmit\_Power\_Reporting event to the Upper Tester with Status set as specified in Table 4.90.
- Expected Outcome

## Pass verdict

In Step 2A.1 or 2B.2, an error status is returned to the Upper Tester.

## 4.15 Isochronous Streams

## 4.15.1 Connected Isochronous Streams

Verify the correct implementation of the Connected Isochronous Stream commands and events.

## 4.15.1.1 Connected Isochronous Stream Using Non-Test Command, Central Initiated

- Test Purpose

Verify that a Central IUT can set up a Connected Isochronous Stream using the LE Setup CIG Parameters Command (the non-test variant) and correctly handles error conditions.

- Reference

[12] 7.1.6, 7.8.97

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle. The connection supervision timeout may be set to a long interval to facilitate testing.
- -The event mask has been configured to allow the HCI\_LE\_CIS\_Established [v1] and [v2] events to be passed to the Upper Tester.
- -The Lower Tester acts in the Peripheral role.
- -TSPX\_max\_cis\_per\_cigs is the Max Supported CIGs as specified in IXIT.
- Test Case Configuration

| Test Case | Steps 9 and 10 performed | Step 13 performed | Step 14 performed | Step 21B allowed |
| HCI/CIS/BV-01-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, asymmetric PHYs, Core v5.2 to v5.4] | No | Yes | No | Yes |
| HCI/CIS/BV-02-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, symmetric PHYs only, Core v5.2 to v5.4] | No | Yes | Yes | Yes |
| HCI/CIS/BV-03-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, asymmetric PHYs, Core v5.2 to v5.4] | Yes | Yes | No | Yes |
| HCI/CIS/BV-04-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, symmetric PHYs only, Core v5.2 to v5.4] | Yes | Yes | Yes | Yes |

| Test Case | Steps 9 and 10 performed | Step 13 performed | Step 14 performed | Step 21B allowed |
| HCI/CIS/BV-15-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, asymmetric PHYs, Unsegmented Framed mode] | No | No | No | No |
| HCI/CIS/BV-16-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, symmetric PHYs only, Unsegmented Framed mode] | No | No | Yes | No |
| HCI/CIS/BV-17-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, asymmetric PHYs, Unsegmented Framed mode] | Yes | No | No | No |
| HCI/CIS/BV-18-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, symmetric PHYs only, Unsegmented Framed mode] | Yes | No | Yes | No |
| HCI/CIS/BV-19-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, asymmetric PHYs, Core v6.0 or later, Unsegmented Framed mode not supported] | No | Yes | No | No |
| HCI/CIS/BV-20-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, symmetric PHYs only, Core v6.0 or later, Unsegmented Framed mode not supported] | No | Yes | Yes | No |
| HCI/CIS/BV-21-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, asymmetric PHYs, Core v6.0 or later, Unsegmented Framed mode not supported] | Yes | Yes | No | No |

Table 4.91: Connected Isochronous Stream Using Non-Test Command, Central Initiated test cases

| Test Case | Steps 9 and 10 performed | Step 13 performed | Step 14 performed | Step 21B allowed |
| HCI/CIS/BV-22-C [Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, symmetric PHYs only, Core v6.0 or later, Unsegmented Framed mode not supported] | Yes | Yes | Yes | No |

- Test Procedure

Figure 4.144: Connected Isochronous Stream Using Non-Test Command, Central Initiated MSC -Page 1 of 4

Figure 4.145: Connected Isochronous Stream Using Non-Test Command, Central Initiated MSC -Page 2 of 4

Figure 4.146: Connected Isochronous Stream Using Non-Test Command, Central Initiated MSC -Page 3 of 4

Figure 4.147: Connected Isochronous Stream Using Non-Test Command, Central Initiated MSC -Page 4 of 4

1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT using common values and CIS\_Count set to 0x10. Here, and elsewhere, to facilitate testing, long intervals may be used.
2. If TSPX\_max\_cis\_per\_cigs is less than 16, then the IUT returns error code Connection Limit Exceeded (0x09) to the Upper Tester. Proceed to Step 7.
3. The IUT returns a success response to the Upper Tester.
4. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT using default values and CIS\_Count set to 0x10.
5. The IUT returns error code Connection Limit Exceeded (0x09) to the Upper Tester.
6. The Upper Tester sends an HCI\_LE\_Remove\_CIG command with the CIG\_ID of the CIG that was initially created and receives a success response.
7. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with PHY\_C\_To\_P[0] set to 0x00 and the other values set to common values, and receives an error response.
8. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with PHY\_P\_To\_C[0] set to 0x00 and the other values set to common values, and receives an error response.
9. If this step is performed (see Table 4.91), the Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with PHY\_C\_To\_P[0] set to 0x07 to the IUT and receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.
10. If this step is performed (see Table 4.91), the Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with PHY\_P\_To\_C[0] set to 0x07 to the IUT and receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.
11. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with PHY\_C\_To\_P[0] set to 0x0F8 to the IUT and receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.
12. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with PHY\_P\_To\_C[0] set to 0x0F8 to the IUT and receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.
13. If this step is performed (see Table 4.91), the Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with Framing set to 0x01, SDU\_Interval\_C\_To\_P set to 0x4E20 (20 ms), SDU\_Interval\_P\_To\_C set to 0x4E20 (20 ms), Max\_Transport\_Latency\_C\_To\_P set to 0x0A (10 ms), and Max\_Transport\_Latency\_P\_To\_C set to 0x0A (10 ms) to the IUT and receives error code Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12) from the IUT.
14. If this step is performed (see Table 4.91), the Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command with PHY\_P\_To\_C[0] set to a valid but different value than PHY\_C\_To\_P[0] and receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.
15. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with default parameters but with framing enabled, and receives a success response from the IUT and CIS\_Count = 1.
16. The Upper Tester sends an HCI\_Disconnect command for the CIS to the IUT. The IUT responds with a successful HCI\_Command\_Status, followed by an HCI\_Disconnection\_Complete event with an error code Command Disallowed (0x0C). Alternately, the IUT replies with error code Command Disallowed (0x0C) in the HCI\_Command\_Status.
17. The Upper Tester sends an HCI\_LE\_Create\_CIS command to create a single CIS and receives a success response from the IUT.
18. The IUT may send an LL\_CIS\_REQ PDU, but the Lower Tester does not respond.

Steps 19 and 20 must execute before an HCI\_LE\_CIS\_Established event is received. If they cannot be executed quickly enough, they may need to be repeated individually under the same conditions.

19. Immediately, before an HCI\_LE\_CIS\_Established event is received, the Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT, and the IUT responds with an error code Command Disallowed (0x0C).
20. Immediately, before an HCI\_LE\_CIS\_Established event is received, the Upper Tester sends an HCI\_Disconnect command for the CIS being established to the IUT.
21. Perform either Step 21A or Step 21B depending on the IUT response. Step 21B is only allowed if specified in Table 4.91.

Alternative 21A (The IUT sends a successful HCI\_Command\_Status):

- 21A.1 The order of a), b), and c) may be swapped, as long as c) is after a).
- 21A.1.a) The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 21A.1.b) The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with an error code Operation Cancelled by Host (0x44).
- 21A.1.c) The IUT sends an HCI\_Disconnection\_Complete event to the Upper Tester with Reason set to Connection Terminated by Local Host (0x16).
- 21A.2 If the IUT sent an LL\_CIS\_REQ PDU in Step 18, then execute Steps 21A.2.a, 21A.2.b, and 21A.2.c.
- 21A.2.a) The Lower Tester sends an LL\_CIS\_RSP to the IUT as soon as either a) or b) of Step 20 has happened.
- 21A.2.b) The IUT sends an LL\_REJECT\_EXT\_IND PDU to the Lower Tester with ErrorCode set to Operation Cancelled by Host (0x44). This may happen before the remaining items in Step 20.
- 21A.2.c) The IUT does not send an event to the Upper Tester other than those in Step 21A.1.
- 21A.3 Repeat Steps 17, 18, 20, and 21A.1.
- 21A.4 The Lower Tester sends an LL\_REJECT\_EXT\_IND PDU to the IUT with ErrorCode set to Rejected Due To Limited Resources (0x0D).
- 21A.5 The IUT does not send an event to the Upper Tester other than those in Step 21A.1.
- 21A.6 The Upper Tester sends an HCI\_LE\_Create\_CIS command to create a single CIS and receives a success response from the IUT.
- Alternative 21B (The IUT sends an HCI\_Command\_Status with an 0x0C error code):
- 21B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with an error code Command Disallowed (0x0C).
22. The Lower Tester receives an LL\_CIS\_REQ PDU from the IUT.
23. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
24. The Lower Tester receives an LL\_CIS\_IND from the IUT.
25. The Upper Tester receives an HCI\_LE\_CIS\_Established event indicating success, after the first CIS packet sent by the Lower Tester. The Connection\_Handle parameter is set to the value provided in the HCI\_LE\_Create\_CIS command.
26. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command and receives a success response from the IUT.
27. The Upper Tester sends HCI ISO data packets over the CIS and the Lower Tester receives framed ISO data.
28. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the Connection\_Handle and Direction equal to that in Step 22 and the IUT sends error code Command Disallowed (0x0C) in return.

29. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with a previously unused Connection\_Handle value, and the IUT sends error code Unknown Connection Identifier (0x02) in return.
30. The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT with CIS\_Count set to 0x01 and CIS\_Connection\_Handle set to that in Step 25, and the IUT sends error code Connection Already Exists (0x0B) in return.
31. The Upper Tester sends an HCI\_LE\_Remove\_CIG command to the IUT with CIG\_ID set to a previously unused value, and the IUT sends error code Unknown Connection Identifier (0x02) in return.
32. The Upper Tester sends an HCI\_LE\_Accept\_CIS\_Request command to the IUT, and the IUT sends error code Command Disallowed (0x0C) in return if the IUT supports LL 9/32, and Unknown HCI command (0x01) otherwise.
33. The Upper Tester sends an HCI\_LE\_Reject\_CIS\_Request command to the IUT, and the IUT sends error code Command Disallowed (0x0C) in return if the IUT supports LL 9/32, and Unknown HCI command (0x01) otherwise.

## · Expected Outcome

## Pass verdict

If TSPX\_max\_cis\_per\_cigs is less than 16, then in Step 2, the IUT returns error code Connection Limit Exceeded (0x09) to the Upper Tester.

If TSPX\_max\_cis\_per\_cigs is 16 or greater, then the following pass criteria apply:

In Step 3, the IUT returns a success response to the Upper Tester.

In Step 5, the IUT returns error code Connection Limit Exceeded (0x09) to the Upper Tester.

In Step 6, the Upper Tester sends an HCI\_LE\_Remove\_CIG command with the CIG\_ID of the CIG that was initially created and receives a success response.

In Step 7, the Upper Tester receives an error response.

In Step 8, the Upper Tester receives an error response.

In Step 9, if performed, the Upper Tester receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.

In Step 10, if performed, the Upper Tester receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.

In Step 11, the IUT responds with error code Unsupported Feature or Parameter Value (0x11).

In Step 12, the IUT responds with error code Unsupported Feature or Parameter Value (0x11).

In Step 13, if performed, the Upper Tester receives error code Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12) from the IUT.

In Step 14, if performed, the Upper Tester receives error code Unsupported Feature or Parameter Value (0x11) from the IUT.

In Step 15, the Upper Tester receives a success response from the IUT and CIS\_Count = 1.

In Step 16, the IUT responds with a successful HCI\_Command\_Status, followed by an HCI\_Disconnection\_Complete event with an error code Command Disallowed (0x0C). Alternately, the IUT replies with error code Command Disallowed (0x0C) in the HCI\_Command\_Status.

In Step 17, the Upper Tester receives a success response from the IUT.

In Step 19, the IUT responds with an error code Command Disallowed (0x0C).

In Step 21A.1, the IUT responds as indicated.

In Step 21A.2.b, the IUT sends an LL\_REJECT\_EXT\_IND PDU to the Lower Tester with ErrorCode set to Operation Cancelled by Host (0x44).

In Step 21B.1, the IUT sends a Command Disallowed (0x0C) error code in response.

In Step 22, the Lower Tester receives an LL\_CIS\_REQ PDU from the IUT.

In Step 24, the Lower Tester receives an LL\_CIS\_IND from the IUT as described.

In Step 25, the Upper Tester receives an HCI\_LE\_CIS\_Established event indicating success. The Connection\_Handle parameter is set to the value provided in the HCI\_LE\_Create\_CIS command. If the IUT sends an HCI\_LE\_CIS\_Established [v2] event, then the Sub\_Interval, Max\_SDU\_C\_To\_P, Max\_SDU\_P\_To\_C, SDU\_Interval\_C\_To\_P, SDU\_Interval\_P\_To\_C, and Framing parameters are set to the corresponding values from the LL\_CIS\_REQ PDU sent in Step 22.

In Step 26, the Upper Tester receives a success response from the IUT.

In Step 27, the Lower Tester receives framed ISO data.

In Step 28, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

In Step 29, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unknown Connection Handle (0x02).

In Step 30, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Connection Already Exists (0x0B).

In Step 31, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).

In Step 32, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Command Disallowed (0x0C) if the IUT supports LL 9/32, and Unknown HCI command (0x01) otherwise.

In Step 33, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Command Disallowed (0x0C) if the IUT supports LL 9/32, and Unknown HCI command (0x01) otherwise.

## Fail verdict

In Step 21A.3, the IUT sends an event other than the ones in Step 20.

## HCI/CIS/BI-11-C [Connected Isochronous Stream, Central Initiated, CIG Parameters Failure Behavior]

- Test Purpose

Verify that a Central IUT ignores any settings provided in a Set CIG Parameters command that failed.

- Reference

[13] 7.8.97

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The Lower Tester acts in the Peripheral role.

·

Figure 4.148: HCI/CIS/BI-11-C [Connected Isochronous Stream, Central Initiated, CIG Parameters Failure Behavior] MSC

1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with
2. PHY\_C\_To\_P for both CIS = 0x00, all the remaining values as specified in Table 4.92.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester failing the command.
3. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with the values specified in the Initial Value(s) column specified in Table 4.92.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status = 0x00, CIG\_ID = 0x01, and CIS\_Count = 2.
5. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with the values specified in the Second Value(s) column specified in Table 4.92.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester failing the command.
7. The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT for CIS\_ID 0x01.
8. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status = 0x00.
9. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID set to 0x01.
10. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
11. The IUT sends an LL\_CIS\_IND PDU to the Lower Tester.
12. The IUT sends an empty ISO Data packet to the Lower Tester, and the Lower Tester sends an Ack to the IUT.
13. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester for CIS\_ID 0x01.
14. The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT for CIS\_ID 0x02.
15. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status = 0x00.
16. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID = 0x02.
17. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
18. The IUT sends an LL\_CIS\_IND PDU to the Lower Tester.
19. The IUT sends an empty ISO Data Packet to the Lower Tester, and the Lower Tester sends an Ack to the IUT.
20. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester for CIS\_ID 0x02.

Table 4.92: CIG Parameter Values

| Parameter | Initial Value(s) | Second Value(s) |
| CIG_ID | 0x01 | 0x01 |
| SDU_Interval_C_To_P, SDU_Interval_P_To_C | 50 ms | 60 ms |
| CIS_Count | 2 | 3 |
| CIS_ID[] | 0x01, 0x02 | 0x01, 0x02, 0x03 |
| Worst_Case_SCA | 0x00 | 0x01 |
| Packing | Sequential (0x00) | Interleaved (0x01) |
| Framing | Framed (0x01) | Unframed (0x00) |
| Max_SDU_C_To_P[] | 16, 16 | 4096, 4096, 4096 |
| Max_SDU_P_To_C[] | 16, 16 | 4096, 4096, 4096 |
| Max_Transport_Latency_C_To_P, Max_Transport_Latency_P_To_C | 200 ms | 250 ms |
| RTN_C_To_P[] | 4, 4 | 5, 5, 5 |
| RTN_P_To_C[] | 4, 4 | 5, 5, 5 |
| PHY_C_To_P[] | 0x01, 0x01 | 0x01, 0x01, 0x01 |
| PHY_P_To_C[] | 0x01, 0x01 | 0x00, 0x01, 0x01 |

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester failing the command.

In Step 4, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status = 0x00, CIG\_ID = 0x01, and CIS\_Count = 2.

In Step 6, the IUT sends an HCI\_Command\_Complete event to the Upper Tester failing the command.

In Step 8, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status = 0x00.

In Step 9, the IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID set to 0x01. Framed PDUs are specified.

In Step 11, the IUT sends an LL\_CIS\_IND PDU to the Lower Tester.

In Step 13, the IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester for CIS\_ID 0x01.

In Step 15, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status = 0x00.

In Step 16, the IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID = 0x02. Framed PDUs are specified.

In Step 18, the IUT sends an LL\_CIS\_IND PDU to the Lower Tester.

In Step 20, the IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester for CIS\_ID 0x02.

The resulting CIG with 2 CISes meets the following criteria:

- -SDU\_Interval\_C\_To\_P and SDU\_Interval\_P\_To\_C are the value specified in the Initial Value(s) column in Table 4.92.
- -The CIS IDs match the values specified in the Initial Value(s) column in Table 4.92.
- -Max\_SDU\_C\_To\_P[] are the values specified in the Initial Value(s) column in Table 4.92.
- -Max\_SDU\_P\_To\_C[] are the values specified in the Initial Value(s) column in Table 4.92.

## 4.15.1.2 Ignoring RFU Bits in HCI ISO Data Packets, CIS

- Test Purpose

Verify that the IUT ignores RFU bits in ISO Data Packets received from the Upper Tester and sends the ISO data in a CIS.

- Reference

[12] 5.4.5

- Initial Condition
- -CIS established in the relevant role defined in Table 4.95 per the following configurations:

| Variable | Value(s) |
| sdu_int_c2p | 0x186A0 (100 ms) |
| sdu_int_p2c | 0x186A0 (100 ms) |
| ft_c2p | 1 |
| ft_p2c | 1 |

| Variable | Value(s) |
| iso_int | 0x50 (100 ms) |
| packing | any supported |
| framing | any |
| cis_cnt | 1 |
| nse[] | 0x03 |
| mx_sdu_c2p[] | 8 |
| mx_sdu_p2c[] | 0 |
| mx_pdu_c2p[] | 8 |
| mx_pdu_p2c[] | 0 |
| phy_c2p[] | 0x01 |
| phy_p2c[] | 0x01 |
| bn_c2p[] | 0x01 |
| bn_p2c[] | 0x00 |

Table 4.93: IUT as Central configuration

| Variable | Value(s) |
| sdu_int_c2p | 0x186A0 (100 ms) |
| sdu_int_p2c | 0x186A0 (100 ms) |
| ft_c2p | 1 |
| ft_p2c | 1 |
| iso_int | 0x50 (100 ms) |
| packing | any supported |
| framing | any |
| cis_cnt | 1 |
| nse[] | 0x03 |
| mx_sdu_c2p[] | 0 |
| mx_sdu_p2c[] | 8 |
| mx_pdu_c2p[] | 0 |
| mx_pdu_p2c[] | 8 |
| phy_c2p[] | 0x01 |
| phy_p2c[] | 0x01 |
| bn_c2p[] | 0x00 |
| bn_p2c[] | 0x01 |

Table 4.94: IUT as Peripheral configuration

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends HCI ISO Data packets to the IUT with all RFU field bits set.
2. The IUT sends the ISO Data packets to the Lower Tester.
- Expected Outcome

Table 4.95: Ignoring RFU Bits in HCI ISO Data Packets, CIS test cases

| Test Case | IUT Role |
| HCI/CIS/BI-01-C [Receiving HCI ISO Data Packets with RFU Bits Set, CIS, Central] | Central |
| HCI/CIS/BI-02-C [Receiving HCI ISO Data Packets with RFU Bits Set, CIS, Peripheral] | Peripheral |

Figure 4.149: Ignoring RFU Bits in HCI ISO Data Packets, CIS MSC

## Pass verdict

The IUT sends the ISO Data packets to the Lower Tester.

## 4.15.1.3 Connected Isochronous Stream, Reject Early Read ISO TX Sync

- Test Purpose

Verify that an IUT properly rejects the LE Read ISO TX Sync command issued by the Upper Tester before an SDU has been transmitted by the IUT.

- Reference

[12] 7.8.96

- Initial Condition
- -The IUT is in the specified role.
- -A CIS has been established using Framing=unframed and all other values as specified in [14] Section 4.10.1.3, Default Values for Set\_CIG\_Parameters\_Test Commands, the ISO data path has been set up, and the Upper Tester does not provide SDU data.
- -The Lower Tester is in the peer role to the IUT.
- -The Lower Tester sends CIS NULL PDUs in each sub-event.

- Test Case Configuration
- Test Procedure
1. The IUT starts sending CIS PDUs to the Lower Tester.
2. As soon as the Lower Tester has received a PDU or after 5 seconds if the IUT does not transmit any PDUs, the Upper Tester sends an HCI\_LE\_Read\_ISO\_TX\_Sync command to the IUT.
3. The IUT sends an HCI\_Command\_Complete event to the Upper Tester.
- Expected Outcome

Table 4.96: Connected Isochronous Stream, Reject Early Read ISO TX Sync test cases

| Test Case |
| HCI/CIS/BI-03-C [Connected Isochronous Stream, Central, Reject Early Read ISO TX Sync] |
| HCI/CIS/BI-04-C [Connected Isochronous Stream, Peripheral, Reject Early Read ISO TX Sync] |

Figure 4.150: Connected Isochronous Stream, Reject Early Read ISO TX Sync MSC

## Pass verdict

In Step 3:

- -If the IUT only sends CIS Null PDUs to the Lower Tester or does not transmit in the subevent, then Status is set to Command Disallowed (0x0C).
- -Otherwise, Status is set to 0 and the event has the TX\_Time\_Stamp and Packet\_Sequence\_Number fields set to appropriate values.

## HCI/CIS/BV-05-C [Connected Isochronous Stream, Central Initiated, Add or Modify CIS]

- Test Purpose

Verify that a Central IUT can add or modify a Connected Isochronous Group before a CIS is created. Verify that a Central IUT rejects an LE Create CIS command when a CIS Connection Handle is specified twice.

- Reference
- [15] 4.10.1.3
- [12] 7.8.97
- [13] 7.8.99

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The Lower Tester acts in the Peripheral role.
- Test Procedure

Figure 4.151: HCI/CIS/BV-05-C [Connected Isochronous Stream, Central Initiated, Add or Modify CIS] MSC -Page 1 of 2

Figure 4.152: HCI/CIS/BV-05-C [Connected Isochronous Stream, Central Initiated, Add or Modify CIS] MSC -Page 2 of 2

1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with the CIG\_ID set to 1 and default values as specified in [15] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and a valid Connection\_Handle\_1.
3. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with the CIS\_ID set to 2, CIG\_ID set to 1, and default values as specified in [15] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and a valid Connection\_Handle\_2.
5. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with CIS\_ID set to 2, CIG\_ID set to 1, and the values as specified in Table 4.97.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Connection\_Handle\_2 received in Step 4.
7. The Upper Tester sends an HCI\_LE\_Create\_CIS command with a CIS\_Count of 2 and both connection handles set to CIS\_Connection\_Handle\_1.

8. Perform alternative 8A or 8B depending on how the IUT rejects the HCI\_LE\_Create\_CIS command.

Alternative 8A (The IUT returns an HCI\_Command\_Status event with an error code)

- 8A.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with the error code Invalid HCI Command Parameters (0x12).

Alternative 8B (The IUT returns an HCI\_LE\_CIS\_Established event with an error code)

- 8B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 8B.2 The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with the error code Invalid HCI Command Parameters (0x12).
9. The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT with a valid CIS\_Connection\_Handle\_1 for CIS\_ID 0x01.
10. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0.
11. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID set to 0x01.
12. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
13. The IUT sends an LL\_CIS\_IND PDU to the Lower Tester.
14. The IUT sends an empty ISO Data packet to the Lower Tester, and the Lower Tester sends an Ack to the IUT.
15. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with Connection\_Handle\_1 for CIS\_ID 0x01.
16. The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT with a valid CIS\_Connection\_Handle\_2 for CIS\_ID 0x02.
17. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0.
18. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID set to 0x02.
19. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
20. The IUT sends an LL\_CIS\_IND PDU to the Lower Tester.
21. The IUT sends an empty ISO Data Packet to the Lower Tester, and the Lower Tester sends an Ack to the IUT.
22. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with Connection\_Handle\_2 for CIS\_ID 0x02.

| Parameter | Value |
| SDU_Interval_C_To_P, SDU_Interval_P_To_C | 20 ms |
| CIS_Count | 1 |
| Peripherals_Clock_Accuracy | 0 |
| Packing | Sequential (0x00) |
| Framing | Unframed (0x00) |
| Max_SDU_C_To_P, Max_SDU_P_To_C | 100 |
| Max_Transport_Latency_C_To_P, Max_Transport_Latency_P_To_C | 40 ms |
| RTN_C_To_P, RTN_P_To_C | 4 |

Table 4.97: CIG Parameter Values

## · Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Connection\_Handle\_1.

In Step 4, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and valid Connection\_Handle\_2.

In Step 6, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and the Connection\_Handle received in Step 4.

In Step 8, the IUT rejects the HCI\_LE\_Create\_CIS command with the error code Invalid HCI Command Parameters (0x12).

In Step 10, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0.

In Step 11, the IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID set to 0x01 and CIS parameters matching the values in Step 1.

In Step 13, the IUT sends an LL\_CIS\_IND PDU to the Lower Tester.

In Step 14, the IUT sends an empty ISO Data Packet to the Lower Tester, and the Lower Tester sends an Ack to the IUT.

In Step 15, the IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with Connection\_Handle\_1 for CIS\_ID 0x01.

In Step 17, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0.

In Step 18, the IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID set to 0x02 and CIS parameters matching the values in Step 5.

In Step 20, the IUT sends an LL\_CIS\_IND PDU to the Lower Tester.

In Step 21, the IUT sends an empty ISO Data packet to the Lower Tester, and the Lower Tester sends an Ack to the IUT.

In Step 22, the IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with Connection\_Handle\_2 for CIS\_ID 0x02.

## HCI/CIS/BI-05-C [Connected Isochronous Stream Using Non-Test Command, Central, Reject Invalid Parameters]

- Test Purpose

Verify that a Central IUT properly rejects invalid parameters in the LE\_Set\_CIG\_Parameters command.

- Reference

[12] 7.8.97

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The Lower Tester acts in the Peripheral role.

## · Test Procedure

Figure 4.153: HCI/CIS/BI-05-C [Connected Isochronous Stream Using Non-Test Command, Central, Reject Invalid Parameters] MSC

1. For each round in Table 4.98, the Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with one parameter set to the value specified and all other values set as specified in Table 4.99.

Note: For round 7, the number of parameters required to describe the CIS\_Count specified exceeds the size of an HCI command. Fill in an array of 26 valid CIS values, leaving only the CIS\_Count in error.

2. The IUT then sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) in rounds 11 and 12 and Invalid HCI Command Parameters (0x12) in all other rounds.
3. Return to Step 1 until all rounds are completed.
4. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with values as specified in Table 4.99 except that SDU\_Interval\_C\_To\_P is set to 0x0000FF (255 µs) and Max\_SDU\_C\_to\_P = 28.
4. 5.
5. Perform either alternative 5A or 5B depending on the IUT response. Alternative 5A (non-zero status):
6. 5A.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to a valid error code.

Alternative 5B (Status set to 0x00):

- 5B.1 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
- 5B.2 The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT with CIS\_Count and CIS\_Connection\_Handle set to the values returned in Step 5B.1.
- 5B.3 Perform either 5B.3A or 5B.3B depending on the HCI\_Command\_Status response. Alternative 5B.3A (non-zero status):
- 5B.3A The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to a valid error code.
- Alternative 5B.3B (Status set to 0x00):

5B.3B

The IUT sends a successful HCI\_Command\_Status event to the Upper Tester followed by an HCI\_LE\_CIS\_Established event with Status set to a valid error code.

6. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with Max\_SDU\_C\_To\_P = 32, SDU\_Interval\_C\_To\_P = 0x0000FF (255 µs) and CIS\_Count = 16. All other values as specified in Table 4.99.
7. Perform either alternative 7A or 7B depending on the IUT response.

Alternative 7A (non-zero status):

- 7A.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to error code Invalid HCI Command Parameters (0x12), Unsupported Feature or Parameter Value (0x11), error code Memory Capacity Exceeded (0x07), error code Rejected Due to Limited Resources (0x0D), or error code Connection Limit Exceeded (0x09).
- Alternative 7B (Status set to 0x00):
- 7B.1 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
- 7B.2 The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT with CIS\_Count and CIS\_Connection\_Handle set to the values returned in Step 7B.1.
- 7B.3 Perform either 7B.3A or 7B.3B depending on the HCI\_Command\_Status response. Alternative 7B.3A (non-zero status):

7B.3A

The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to error code Invalid HCI Command Parameters (0x12), Unsupported Feature or Parameter Value (0x11), error code Memory Capacity Exceeded (0x07), error code Rejected Due to Limited Resources (0x0D), or error code Connection Limit Exceeded (0x09).

Alternative 7B.3B (Status set to 0x00):

7B.3B

The IUT sends a successful HCI\_Command\_Status event to the Upper Tester followed by an HCI\_LE\_CIS\_Established event with Status set to error code Invalid HCI Command Parameters (0x12), Unsupported Feature or Parameter Value (0x11), error code Memory Capacity Exceeded (0x07), error code Rejected Due to Limited Resources (0x0D), or error code Connection Limit Exceeded (0x09).

Table 4.98: CIG Parameters for each round

| Round | Parameter | Value |
| 1 | CIG_ID | 0xFF |
| 2 | SDU_Interval_C_To_P | 0xF00000 |
| 3 | Worst_Case_SCA | 0xF0 |
| 4 | Packing | 0xF0 |
| 5 | Framing | 0xF0 |
| 6 | Max_Transport_Latency_C_To_P | 0xF000 |
| 7 | CIS_Count | 0x20 |
| 8 | CIS_ID | 0xFF |
| 9 | Max_SDU_C_To_P | 0xF000 |
| 10 | Max_SDU_P_To_C | 0xF000 |
| 11 | PHY_C_To_P | 0xF0 |
| 12 | PHY_P_To_C | 0xF0 |

Table 4.99: CIG Default Parameters

| Parameter | Default Value |
| SDU_Interval_C_To_P | 20 ms |
| SDU_Interval_P_To_C | 20 ms |
| CIS_Count | 2 (round 4), 1 (all other rounds) |
| Worst_Case_SCA | 0 |
| Packing | Sequential (0x00) OR Interleaved (0x01) |
| Framing | Unframed (0x00) |
| Max_SDU_C_To_P | 10 |
| Max_SDU_P_To_C | 0 |
| PHY_C_To_P | LE 1M PHY |
| PHY_P_To_C | LE 1M PHY |
| Max_Transport_Latency_C_To_P | 40 ms |
| Max_Transport_Latency_P_To_C | 40 ms |
| RTN_C_To_P | 2 |
| RTN_P_To_C | 2 |

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) in rounds 11 and 12 and Invalid HCI Command Parameters (0x12) in all other rounds.

In Steps 5A.1, 5B.3A, and 5B.3B, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to a valid error code.

In Step 7A.1, 7B.3A, and 7B.3B, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to error code Invalid HCI Command Parameters (0x12), Unsupported Feature or Parameter Value (0x11), error code Memory Capacity Exceeded (0x07), error code Rejected Due to Limited Resources (0x0D), or error code Connection Limit Exceeded (0x09).

## HCI/CIS/BV-06-C [Connected Isochronous Stream Using Test Command, Central Initiated, Time\_Offset]

- Test Purpose

Verify that the Central IUT, when transmitting unframed data packets, returns a Time\_Offset value of 0 when LE Read ISO TX Sync is called.

- Reference

[12] 7.8.96

- Initial Condition
- -The Isochronous Channels (Host Support) FeatureSet bit is set.
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The Lower Tester acts in the Peripheral role.

## · Test Procedure

Figure 4.154: HCI/CIS/BV-06-C [Connected Isochronous Stream Using Test Command, Central Initiated, Time\_Offset] MSC

1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters\_Test command to the IUT with the default parameters in [15] Section 4.10.1.3, Default Values for Set CIG Parameters Commands. The Upper Tester receives an HCI\_Command\_Complete success response from the IUT and CIS\_Count = 1.
2. The Upper Tester sends an HCI\_LE\_Create\_CIS command to create a single CIS and receives a success response from the IUT.
3. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester.

4. The Lower Tester sends an LL\_CIS\_RSP PDU to the IUT.
5. The IUT sends an LL\_CIS\_IND to the Lower Tester.
6. The IUT sends an empty ISO Data packet to the Lower Tester.
7. The Lower Tester acknowledges the empty ISO Data packet.
8. The IUT sends an HCI\_LE\_CIS\_Established event indicating success to the Upper Tester. The Connection\_Handle parameter is set to the value provided in the HCI\_LE\_Create\_CIS command.
9. The Upper Tester sends an HCI\_LE\_Read\_Buffer\_Size [v2] command to the IUT and receives an HCI\_Command\_Complete event providing an ISO\_Data\_Packet\_Length.
10. Execute alternative 10A or 10B depending on the ISO\_Data\_Packet\_Length in Step 9. Alternative 10A (ISO\_Data\_Packet\_Length &gt; 0):
8. 10A.1 The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command with the Data\_Path\_Direction set to Input (0x00) to the IUT and receives a success response.

Alternative 10B (ISO\_Data\_Packet\_Length = 0):

- 10B.1 The Upper Tester uses an implementation-specific data path for Step 11.
11. The Upper Tester sends HCI ISO Data packets over the CIS, and the Lower Tester receives unframed ISO data. The HCI ISO Data packets are no larger than the permitted size read in Step 9.
12. The Upper Tester sends an HCI\_LE\_Read\_ISO\_TX\_Sync command to the IUT.
13. The IUT sends an HCI\_Command\_Complete event that includes the Time\_Offset to the Upper Tester. The Time\_Offset return parameter is 0.
- Expected Outcome

## Pass verdict

The IUT provides an HCI\_Command\_Complete success response in Step 1.

The IUT provides an HCI\_Command\_Status success response in Step 2.

In Step 8, the IUT sends an HCI\_LE\_CIS\_Established event indicating success to the Upper Tester. The Connection\_Handle parameter is set to the value provided in the HCI\_LE\_Create\_CIS command.

In Step 13, the value of the Time\_Offset return parameter is 0.

## 4.15.1.4 Connected Isochronous Stream, Invalid LE Read ISO TX Sync Parameters

- Test Purpose

Verify that an IUT returns an error when receiving an HCI\_LE\_Read\_ISO\_TX\_Sync command when the CIS is not configured to transmit from the IUT.

- Reference

[12] 7.8.96

- Initial Condition
- -The IUT and the Lower Tester are connected in their respective roles in a unidirectional CIS. The IUT does not transmit data and receives data from the Lower Tester.
- -IUT as Central: Max\_SDU\_C\_To\_P[] = 0x00; Max\_PDU\_C\_To\_P[] = 0x00; BN\_C\_To\_P[] = 0x00. All other values default as specified in [14] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.
- -IUT as Peripheral: Max\_SDU\_P\_To\_C[] = 0x00; Max\_PDU\_P\_To\_C[] = 0x00; BN\_P\_To\_C[] = 0x00. All other values default as specified in [14] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.

- Test Case Configuration
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Read\_ISO\_TX\_Sync command to the IUT with Connection\_Handle set to the current CIS connection handle.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

Table 4.100: Connected Isochronous Stream, Invalid LE Read ISO TX Sync Parameters test cases

| Test Case |
| HCI/CIS/BV-07-C [Connected Isochronous Stream, Invalid LE Read ISO TX Sync Parameters, Central] |
| HCI/CIS/BV-08-C [Connected Isochronous Stream, Invalid LE Read ISO TX Sync Parameters, Peripheral] |

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.

## HCI/CIS/BI-06-C [Invalid LE Accept or Reject CIS Request, Premature Setup ISO Data Path]

- Test Purpose

Verify that a Peripheral IUT returns an error when the Host sends an HCI\_LE\_Setup\_ISO\_Data\_Path command prior to sending the HCI\_LE\_Accept\_CIS\_Request command.

Verify that a Peripheral IUT returns an error when the Host sends an HCI\_LE\_Accept\_CIS\_Request or HCI\_LE\_Reject\_CIS\_Request command with an HCI\_LE\_Accept\_CIS\_Request command in progress or with a connected CIS.

- Initial Condition
- -The IUT is Peripheral.
- -The event mask has been configured to allow the HCI\_LE\_CIS\_Established [v1] and [v2] events to be passed to the Upper Tester.

## · Test Procedure

Figure 4.155: HCI/CIS/BI-06-C [Invalid LE Accept or Reject CIS Request, Premature Setup ISO Data Path] MSC

1. The Lower Tester sends an LL\_CIS\_REQ PDU to the IUT.
2. The IUT sends an HCI\_LE\_CIS\_Request event to the Upper Tester with a CIS\_Connection\_Handle.
3. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command with Data\_Path\_Direction set to Output (0x01) and using the CIS\_Connection\_Handle provided in Step 2. The IUT responds with an HCI\_Command\_Complete with error code Command Disallowed (0x0C).
4. The Upper Tester sends an HCI\_LE\_Accept\_CIS\_Request command to the IUT with the Connection\_Handle set to the CIS\_Connection\_Handle received in Step 2 and receives a successful HCI\_Command\_Status event in return.

5. The IUT sends an LL\_CIS\_RSP PDU to the Lower Tester.
6. The Upper Tester sends an HCI\_LE\_Accept\_CIS\_Request command to the IUT with the Connection\_Handle set to the CIS\_Connection\_Handle received in Step 2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0C.
7. The Upper Tester sends an HCI\_LE\_Reject\_CIS\_Request command to the IUT with the Connection\_Handle set to the CIS\_Connection\_Handle received in Step 2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0C.
8. The Lower Tester sends an LL\_CIS\_IND PDU to the IUT.
9. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with a Connection\_Handle. If the IUT sends an HCI\_LE\_CIS\_Established [v2] event, then the Sub\_Interval, Max\_SDU\_C\_To\_P, Max\_SDU\_P\_To\_C, SDU\_Interval\_C\_To\_P, SDU\_Interval\_P\_To\_C, and Framing parameters are set to the corresponding values from the LL\_CIS\_REQ PDU sent in Step 1.
10. The Upper Tester sends an HCI\_LE\_Accept\_CIS\_Request command to the IUT with the Connection\_Handle set to the Connection\_Handle received in Step 9.
11. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0C.
12. The Upper Tester sends an HCI\_LE\_Reject\_CIS\_Request command to the IUT with the Connection\_Handle set to the Connection\_Handle received in Step 9.
13. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

## Pass verdict

In Step 3, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed 0x0C.

In Steps 6, 7, 11, and 13, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0C.

## HCI/CIS/BI-07-C [LE CIS Request Timeout]

- Test Purpose

Verify that a Peripheral IUT returns an error when the Host fails to send an HCI\_LE\_Accept\_CIS\_Request or HCI\_LE\_Reject\_CIS\_Request command before the Connection Accept Timeout expires.

- Initial Condition
- -The IUT is Peripheral.
- Test Procedure
1. The Lower Tester sends an LL\_CIS\_REQ PDU to the IUT.
2. The IUT sends an HCI\_LE\_CIS\_Request event to the Upper Tester with a CIS\_Connection\_Handle.
3. The Upper Tester does not send an HCI\_LE\_Accept\_CIS\_Request or HCI\_LE\_Reject\_CIS\_Request within the Connection\_Accept\_Timeout.
4. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with Status set to Connection Accept Timeout Exceeded (0x10).
- Expected Outcome

## Pass verdict

In Step 4, the IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with Status set to 0x10 after Connection\_Accept\_Timeout after Step 2 has elapsed.

## HCI/CIS/BI-08-C [Connected Isochronous Stream, Peripheral, Reject Invalid Commands]

- Test Purpose

Verify that a Peripheral IUT properly rejects invalid CIS commands.

- Reference

[12] 7.8.99, 7.8.101, 7.8.109

- Initial Condition
- -A CIS has been established and the ISO data path has been set up. The Connection\_Handle of the CIS is preserved as Connection\_Handle\_1.
- -The Lower Tester acts in the Central role.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with Connection\_Handle set to Connection\_Handle\_1.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
3. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the Connection\_Handle set to a different value than Connection\_Handle\_1.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).

Figure 4.156: HCI/CIS/BI-08-C [Connected Isochronous Stream, Peripheral, Reject Invalid Commands] MSC

5. The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT with the ACL\_Connection\_Handle set to the value of the current ACL connection and CIS\_Handle set to Connection\_Handle\_1.
6. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unknown HCI Command (0x01), Unknown Connection Identifier (0x02), Connection Already Exists (0x0B), or Command Disallowed (0x0C).
7. The Upper Tester sends an HCI\_LE\_Accept\_CIS\_Request to the IUT with Connection\_Handle set to a different value than Connection\_Handle\_1.
8. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

In Step 4, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).

In Step 6, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unknown HCI Command (0x01), Unknown Connection Identifier (0x02), Connection Already Exists (0x0B), or Command Disallowed (0x0C).

In Step 8, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).

## HCI/CIS/BI-09-C [Connected Isochronous Stream, Peripheral, Reject Invalid Disconnect Command]

- Test Purpose

Verify that a Peripheral IUT connecting to a CIS properly rejects a disconnect command that was received before the CIS is fully established.

- Reference

[12] 7.1.6

- Initial Condition
- -The Isochronous Channels (Host Support) FeatureSet bit is set. The event mask has been configured to allow CIS events to be passed to the Upper Tester.
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The Lower Tester is configured as the Central.

## · Test Procedure

Figure 4.157: HCI/CIS/BI-09-C [Connected Isochronous Stream, Peripheral, Reject Invalid Disconnect Command] MSC

1. The Lower Tester sends an LL\_CIS\_REQ to the IUT with valid values.
2. The IUT sends an HCI\_LE\_CIS\_Request event to the Upper Tester and the parameters include the CIS\_Connection\_Handle assigned by the IUT.
3. The Upper Tester sends an HCI\_LE\_Accept\_CIS\_Request command to the IUT, with the Connection\_Handle field set to the value of the CIS\_Connection\_Handle received in Step 2.
4. The IUT sends a successful Command Status to the Upper Tester.
5. The IUT sends an LL\_CIS\_RSP PDU to the Lower Tester.
6. The Lower Tester sends an LL\_CIS\_IND to the IUT. The Lower Tester does not send ISO data PDUs to the IUT.
7. Before the CIS times out, the Upper Tester sends an HCI\_Disconnect command to the IUT with the Connection\_Handle equal to the CIS\_Connection\_Handle received in Step 2.
8. The IUT sends an HCI\_Command\_Status to the Upper Tester with Status set to error code Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_LE\_CIS\_Request event to the Upper Tester with the CIS\_Connection\_Handle assigned by the IUT.

In Step 4, the IUT sends a successful Command Status to the Upper Tester.

In Step 8, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to error code Command Disallowed (0x0C).

## 4.15.1.5 Connected Isochronous Stream, Time\_Stamp

- Test Purpose

Verify that a Central or Peripheral IUT sets the TS\_Flag bit if the ISO\_Data\_Load field provides a Time\_Stamp to the Upper Tester over the HCI, and the bit is only set if the PB\_Flag field equals 0b00 or 0b10.

Verify that a Central or Peripheral IUT provides a Time\_Stamp to the Upper Tester over the HCI when time stamps are mandatory.

Verify that an Isochronous Broadcaster IUT correctly handles receiving a Time\_Stamp in HCI ISO Data packets from the Upper Tester.

- Reference

[13] 5.4.5

- Initial Condition
- -The IUT and the Lower Tester are connected in their respective roles as specified in Table 4.101 in a CIS using framed PDUs. All other values as defined in [14] 4.10.1.
- -Peripheral IUT: The Lower Tester may request the IUT SCA if the IUT supports it in order to reduce timestamp tolerance.
- Test Case Configuration
- Test Procedure
1. The Lower Tester sends framed PDUs containing isochronous data to the IUT. The SDU data consists of octets that count from 0x00 to 0xFF and roll over back to 0x00, then the count resumes. This count continues across all SDU data.
2. The IUT sends the received data to the Upper Tester in HCI ISO Data packets.
3. The Upper Tester sends SDU data to the IUT and includes Time\_Stamps in the appropriate HCI ISO Data packets. The SDU data consists of octets that count from 0x00 to 0xFF and roll over back to 0x00, then the count resumes. This count continues across all SDU data.
4. The IUT sends the SDUs provided by the Upper Tester to the Lower Tester.
- Expected Outcome

Table 4.101: Connected Isochronous Stream, Time\_Stamp test cases

| Test Case | Role | Time_Stamp |
| HCI/CIS/BV-09-C | Central | Optional |
| HCI/CIS/BV-10-C | Peripheral | Optional |
| HCI/CIS/BV-11-C | Central | Mandatory |
| HCI/CIS/BV-12-C | Peripheral | Mandatory |

## Pass verdict

When the IUT sends HCI ISO Data packets with the PB\_Flag set to 0b00 or 0b10, then:

- -The Packet\_Sequence\_Number, ISO\_SDU\_Length, and Packet\_Status\_Flag fields are present.
- -If Time\_Stamps are mandatory, then the TS flag is set. Otherwise, the TS flag can be set or clear.
- -If the TS\_Flag is set, then a valid Time\_Stamp field is present. Otherwise, Time\_Stamp is not present.

When the IUT sends HCI ISO Data packets with the PB\_Flag set to 0b01 or 0b11, then the TS flag is clear and the Time\_Stamp, Packet\_Sequence\_Number, ISO\_SDU\_Length, and Packet\_Status\_Flag fields are not present.

When Time\_Stamps are provided, the difference between Time\_Stamps of adjacent SDUs is the SDU Interval within ±(SCA\_Central + SCA\_Peripheral) * ISO\_Interval ± Jitter.

The Lower Tester receives PDUs with data consisting of the data described in Step 3; the contents of the Upper Tester' s Time\_Stamp do not corrupt the contents of the data received by the Lower Tester.

The IUT sends SDUs to the Upper Tester with the contents as specified in Step 1.

## HCI/CIS/BI-10-C [Connected Isochronous Stream, Central, Reject Max\_SDU in Wrong Direction]

- Test Purpose

Verify that a Central IUT properly rejects Max\_SDU values that conflict with existing data path directions.

- Reference

[13] 7.8.97

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The Lower Tester acts in the Peripheral role.

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with CIG\_ID set to 0x00, CIS\_ID set to 0x00, Max\_SDU\_P\_To\_C set to 42, and Max\_SDU\_C\_To\_P set to 0x0000.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and a valid Connection\_Handle\_1.

Figure 4.158: HCI/CIS/BI-10-C [Connected Isochronous Stream, Central, Reject Max\_SDU in Wrong Direction] MSC

3. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with Connection\_Handle\_1 from Step 2 and Data\_Path\_Direction set to 0x01 for the Output direction.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
5. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with CIG\_ID set to 0x00, CIS\_ID set to 0x00, and Max\_SDU\_P\_To\_C set to 0x0000, and Max\_SDU\_C\_To\_P set to 42.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
7. The Upper Tester sends an HCI\_LE\_Remove\_ISO\_Data\_Path command to the IUT with Connection\_Handle set to Connection\_Handle\_1 and Data\_Path\_Direction set to 0x02.
8. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Connection\_Handle set to Connection\_Handle\_1.
9. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with CIG\_ID set to 0x00, CIS\_ID set to 0x00, Max\_SDU\_P\_To\_C set to 0x0000, and Max\_SDU\_C\_To\_P set to 42.
10. The IUT sends an HCI\_Command\_Complete to the Upper Tester with Status set to 0x00 and a valid Connection\_Handle\_1.
11. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path to the IUT with Connection\_Handle\_1 and Data\_Path\_Direction set to 0x00 for the Input direction.
12. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.
13. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with CIG\_ID set to 0x00, CIS\_ID set to 0x00, Max\_SDU\_P\_To\_C set to 42, and Max\_SDU\_C\_To\_P set to 0x0000.
14. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and a valid Connection\_Handle\_1.

In Step 4, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.

In Step 6, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

In Step 8, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00 and Connection\_Handle set to Connection\_Handle\_1.

In Step 10, the IUT sends an HCI\_Command\_Complete to the Upper Tester with Status set to 0x00 and a valid Connection\_Handle\_1.

In Step 12, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.

In Step 14, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

## HCI/CIS/BI-12-C [CIS Setup Procedure, Central Initiated, Invalid Transport Latency]

- Test Purpose

Verify that a Central IUT rejects the creation of a CIS with an invalid max transport latency value.

- Reference

[13] 7.8.97

- Initial Condition
- -The Isochronous Channels (Host Support) FeatureSet bit is set.
- -An ACL connection has been established between the IUT and the Lower Tester.
- -The Lower Tester acts in the Peripheral role.
- Test Procedure

Figure 4.159: HCI/CIS/BI-12-C [CIS Setup Procedure, Central Initiated, Invalid Transport Latency] MSC

1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with Framing set to 1, Max\_Transport\_Latency\_C\_To\_P and Max\_Transport\_Latency\_P\_To\_C set to 0x0005, SDU\_Interval\_C\_To\_P and SDU\_Interval\_P\_To\_C set to 100 ms, and Max\_SDU\_C\_To\_P and Max\_SDU\_P\_To\_C set to 384. All other values are assigned the default values specified in [14] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.
2. 2.
3. Perform either alternative 2A or 2B depending on the IUT response. Alternative 2A (Status set to 0x11 or 0x12):
4. 2A.1 The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12).
5. Alternative 2B (Status set to 0x00):
6. 2B.1 The IUT sends a successful HCI\_Command\_Complete event to the Upper Tester.
7. 2B.2 The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT with CIS\_Count and CIS\_Connection\_Handle set to the values returned in Step 2B.1.
8. Perform either 2B.3A or 2B.3B depending on the HCI\_Command\_Status response.
9. 2B.3A The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12).
10. 2B.3B The IUT sends a successful HCI\_Command\_Status event to the Upper Tester followed by an HCI\_LE\_CIS\_Established event with Status set to Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12).
- Expected Outcome

## Pass verdict

In Step 2A.1, 2B.3A, or 2B.3B, the IUT sends an HCI event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12).

## HCI/CIS/BV-13-C [Connected Isochronous Stream, Central, Removal of Configurable and Inactive CIG]

- Test Purpose

Verify that a Central IUT can remove a CIG in the configurable and inactive states.

- Reference

[13] 7.8.100

- Initial Condition
- -A single CIS has been established using the values specified in [14] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.
- -The Lower Tester is Peripheral.

Figure 4.160: HCI/CIS/BV-13-C [Connected Isochronous Stream, Central, Removal of Configurable and Inactive CIG] MSC

1. The Upper Tester sends an HCI\_Disconnect command to the IUT with Connection\_Handle set to the current CIS\_Connection\_Handle and Reason set to any valid value, and it receives a successful HCI\_Command\_Status in response.
2. The IUT sends an LL\_CIS\_TERMINATE\_IND PDU to the Lower Tester.
3. The Lower Tester sends an LL Ack to the IUT.
4. The IUT sends an HCI\_Disconnection\_Complete event to the Upper Tester with Status set to 0x00, Connection\_Handle set to the CIS\_Connection\_Handle in Step 1, and Reason set to a valid value.
5. The Upper Tester sends an HCI\_LE\_Remove\_CIG command to the IUT with CIG\_ID set to the value of CIG\_ID in Step 1.
6. The IUT sends the Upper Tester an HCI\_Command\_Complete event with CIG\_ID set to the CIG\_ID in Step 1 and Status set to 0x00.
7. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with values as stated in [14] Section 4.10.1.3, Default Values for Set CIG Parameters Commands, and receives a successful HCI\_Command\_Complete event in response.

8. The Upper Tester sends an HCI\_LE\_Remove\_CIG command to the IUT with CIG\_ID set to the CIG\_ID value in Step 7.
9. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with CIG\_ID set to the value in Step 7 and Status set to 0x00.
- Expected Outcome

## Pass verdict

In Step 1, the IUT sends a successful HCI\_Command\_Status to the Upper Tester.

In Step 4, the IUT sends an HCI\_Disconnection\_Complete event to the Upper Tester with Status set to 0x00, Connection\_Handle set to the CIS\_Connection\_Handle in Step 1, and Reason set to a valid value.

In Step 6, the IUT sends the Upper Tester an HCI\_Command\_Complete event with CIG\_ID set to the CIG\_ID in Step 1 and Status set to 0x00.

In Step 9, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with CIG\_ID set to the value in Step 7 and Status set to 0x00.

## HCI/CIS/BI-13-C [Connected Isochronous Stream, Central, Reject Parameter Change of Inactive CIG]

- Test Purpose

Verify that a Central IUT properly rejects the LE Setup CIG Parameters command (the non-test variant) used on an inactive Connected Isochronous Stream.

- Reference

[13] 7.8.97

- Initial Condition
- -A single CIS has been established using the values specified in [14] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.
- -The Lower Tester is Peripheral.

## · Test Procedure

Figure 4.161: HCI/CIS/BI-13-C [Connected Isochronous Stream, Central, Reject Parameter Change on Inactive CIG] MSC

1. The Upper Tester sends an HCI\_Disconnect command to the IUT with Connection\_Handle set to the current CIS\_Connection\_Handle and Reason set to any valid value, and it receives a successful HCI\_Command\_Status in response.
2. The IUT sends an LL\_CIS\_TERMINATE\_IND PDU to the Lower Tester.
3. The Lower Tester sends an LL Ack to the IUT.
4. The IUT sends an HCI\_Disconnection\_Complete event to the Upper Tester with Status set to 0x00, Connection\_Handle set to the CIS\_Connection\_Handle, and Reason set to a valid value.
5. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with values as stated in [14] Section 4.10.1.3, Default Values for Set CIG Parameters Commands.
6. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

## · Expected Outcome

## Pass verdict

In Step 1, the IUT sends a successful HCI\_Command\_Status to the Upper Tester.

In Step 4, the IUT sends an HCI\_Disconnection\_Complete event to the Upper Tester with Status set to 0x00, Connection\_Handle set to the CIS\_Connection\_Handle, and Reason set to a valid value.

In Step 6, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

## 4.15.1.6 Verify CIS Features Not Supported

- Test Purpose

Verify that an IUT does not support CIS features that are marked as unsupported features. The Upper Tester attempts to set CIG parameters that use the unsupported features, expecting the IUT to return an error.

- Reference

[7] 4.5.13

[12] 7.8.98

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- Test Case Configuration
- Test Procedure

Table 4.102: Verify CIS Features Not Supported test cases

| Test Case | HCI Parameters |
| HCI/CIS/BI-14-C [Verify CIS Features Not Supported, BN > 1] | BN_C_To_P = 2 BN_P_To_C = 2 |
| HCI/CIS/BI-15-C [Verify CIS Features Not Supported, FT > 1] | FT_C_TO_P = 2 FT_P_TO_C = 2 |

For each entry in the HCI Parameters in Table 4.102:

1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters\_Test command to the IUT with that parameter set as specified in Table 4.102 and the remaining parameters (including any others listed in Table 4.102) as valid parameters.
2. The IUT sends an HCI\_Command\_Complete event with Error set to 0x11 (Unsupported Feature or Parameter Value).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an error code of 0x11 to the IUT.

## HCI/CIS/BI-16-C [Disconnecting Immediately After a Failed Create CIS Attempt]

- Test Purpose

Verify that a Central IUT properly responds when an Upper Tester attempts to disconnect a connection after a failed CIS creation attempt. The Upper Tester sends an HCI\_Disconnect after the IUT sends the failed HCI\_LE\_CIS\_Established event.

- Reference

[13] 7.1.6, 7.8.99

- Initial Condition
- -An ACL connection has been established between the IUT and the Lower Tester with a valid Connection Handle.
- -The Lower Tester acts in the Peripheral role.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with the values specified in the Initial Value(s) column in Table 4.103.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status = 0x00, CIG\_ID = 0x01, and CIS\_Count = 1.
3. The Upper Tester sends an HCI\_LE\_Create\_CIS command to the IUT for CIS\_ID 0x01.
4. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status = 0x00.
5. The IUT sends an LL\_CIS\_REQ PDU to the Lower Tester with CIS\_ID set to 0x01.
6. The Lower Tester sends an LL\_REJECT\_EXT\_IND PDU to the IUT.
7. The IUT sends an HCI\_LE\_CIS\_Established event to the Upper Tester with Status &gt; 0.
8. The Upper Tester sends an HCI\_Disconnect command to the IUT.

Figure 4.162: HCI/CIS/BI-16-C [Disconnecting Immediately After a Failed Create CIS Attempt] MSC

9. Perform alternative 9A or 9B depending on the HCI\_Command\_Status response.

Alternative 9A (HCI\_Command\_Status = 0x0C):

- 9A.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0C (Command Disallowed).

Alternative 9B (Successful HCI\_Command\_Status):

- 9B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 9B.2 The IUT sends an HCI\_Disconnection\_Complete event to the Upper Tester with Status set to 0x0C (Command Disallowed).

| Parameter | Initial Value(s) |
| CIG_ID | 0x01 |
| SDU_Interval_C_To_P, SDU_Interval_P_To_C | 50 ms |
| CIS_Count | 1 |
| CIS_ID[] | 0x01 |
| Worst_Case_SCA | 0x00 |
| Packing | Sequential (0x00) |
| Framing | Framed (0x01) |
| Max_SDU_C_To_P[] | 16 |
| Max_SDU_P_To_C[] | 16 |
| Max_Transport_Latency_C_To_P, Max_Transport_Latency_P_To_C | 200 ms |
| RTN_C_To_P[] | 4 |
| RTN_P_To_C[] | 4 |
| PHY_C_To_P[] | 0x01 |
| PHY_P_To_C[] | 0x01 |

Table 4.103: CIG Parameter Values

## · Expected Outcome

## Pass verdict

In Steps 9A.1 or 9B.2, the IUT sends an event with Error Code 0x0C.

## HCI/CIS/BV-14-C [Number of Completed Packets Event after Sending data in Unidirectional CIS]

## · Test Purpose

Verify that the IUT properly sends the HCI Number of Completed Packets event after the IUT sends Isochronous data to a device in the Connected Isochronous Group.

## · Reference

[13] 7.7.19

## · Initial Condition

- -The maximum number of CISes in a CIG is defined in the TSPX\_max\_cis\_per\_cigs IXIT value.
- -A CIG with TSPX\_max\_cis\_per\_cigs CISes has been established between the IUT and the Lower Tester with Max\_SDU set to 4, BN set to 1, and FT set to 1 in each direction for each CIS. The remaining parameters are the defaults specified in [14] Section 4.10.1.3 Default Values for Set

CIG Parameters Commands but may be adjusted if necessary to establish the CIG. The IUT can be in either role.

- -The input data path (Host to Controller) for each CIS is set up to receive data over HCI.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Read\_Buffer\_Size [v2] command to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event with an ISO\_Data\_Packet\_Length and Total\_Num\_ISO\_Data\_Packets.
3. Let n = Total\_Num\_ISO\_Data\_Packets from Step 2.
4. Throughout the remaining steps:
- a) The IUT sends either CIS Null PDUs or the data from the HCI ISO Data packets in Step 7 to the Lower Tester.
- b) If the Lower Tester is the Central, then it sends CIS Null PDUs to the IUT in each CIS sub-event within the CIG.
- c) Whenever the IUT sends an HCI\_Number\_Of\_Completed\_Packets event to the Upper Tester, increase n by the sum of the Num\_Completed\_Packets[i] values in the event for those values of i where Connection\_Handle[i] refers to a CIS. Ignore those values of i where Connection\_Handle[i] does not refer to a CIS.
5. Perform Steps 6 -9 a total of 10 times.
6. Perform Steps 7 -9 for each CIS in a random order (different each time).
7. If n is zero, wait until n is non-zero.
8. The Upper Tester sends an HCI ISO Data packet to the IUT containing an SDU of length 4 octets and the correct connection handle for the CIS.
9. Decrement n by 1.
10. Wait for 10 seconds.
- Expected Outcome

## Pass verdict

For each CIS, the sum of the Num\_Completed\_Packets[i] where Connection\_Handle[i] refers to that CIS equals 10.

n = Total\_Num\_ISO\_Data\_Packets from Step 2.

## Fail verdict

After Step 10 completes, n does not equal Total\_Num\_ISO\_Data\_Packets from Step 2.

## HCI/CIS/BI-18-C [LE Set CIG Parameters, Framed, Unsegmented Mode Unsupported]

- Test Purpose

Verify that the IUT that does not support Framed, Unsegmented mode returns an error in response to the HCI\_LE\_Set\_CIG\_Parameters command.

- Reference

[19] 7.8.97

- Initial Condition
- -An ACL connection has been established between the IUT and Lower Tester with a valid Connection Handle.

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_CIG\_Parameters command to the IUT with Framing set to 0x02.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11.
- Expected Outcome

## Pass verdict

In Step 2, the IUT returns an Unsupported Feature or Parameter Value error.

## 4.15.1.7 Connected Isochronous Stream, HCI Read/Write Authenticated Payload Timeout error

- Test Purpose

Verify that an IUT rejects the Read or Write Authenticated Payload Timeout command applied to a CIS.

- Initial Condition
- -The IUT is in the role specified in Table 4.104.
- -The Lower Tester and the IUT have established an encrypted ACL connection.
- -A CIS has been established using values as specified in [14] Section 4.10.1.3, Default Values for Set\_CIG\_Parameters\_Test Commands, and the Upper Tester does not provide SDU data.
- -The Lower Tester is in the peer role to the IUT.
- Test Case Configuration

| Test Case | Role | Reference |
| HCI/CIS/BI-19-C [Connected Isochronous Stream, Central] | Central | [12] 7.3.93, 7.3.94 |
| HCI/CIS/BI-20-C [Connected Isochronous Stream, Peripheral] | Peripheral | [12] 7.3.93, 7.3.94 |

Table 4.104: Connected Isochronous Stream, HCI Read/Write Authenticated Payload Timeout error test cases

## · Test Procedure

1. The Upper Tester sends the HCI\_Read\_Authenticated\_Payload\_Timeout command to the IUT with Connection\_Handle set to the handle for the CIS.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
3. The Upper Tester sends the HCI\_Write\_Authenticated\_Payload\_Timeout command to the IUT with Connection\_Handle set to the handle for the CIS.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

## Pass verdict

In Steps 2 and 4, the IUT sends an 0x0C error to the Upper Tester.

## 4.15.2 Broadcast Isochronous Streams

Verify the correct implementation of the Broadcast Connected Isochronous Stream commands and events.

## HCI/BIS/BI-08-C [Invalid LE BIG Create Sync Parameters and LE ISO Remove Data Path behavior, BIS]

- Test Purpose

Verify that the IUT properly handles invalid parameters for the LE BIG Create Sync command. Also verify that the LE IUT properly handles the LE ISO Remove Data Path command being called by the Upper Tester before the ISO Data Path is properly set, and the IUT rejects a request to terminate a BIS when the IUT is a Synchronized Receiver.

- Reference

[12] 5.4.5

- Initial Condition
- -The IUT is configured in the passive scanning state. The Lower Tester is in the advertising state.
- -The IUT is synchronized to the Lower Tester Periodic Advertising.
- -The Lower Tester establishes a BIG with the values in Table 4.105.

| Variable | Value(s) |
| num_bis | 2 |
| sdu_int | 200 ms |
| iso_int | 200 ms |
| nse | 1 |
| mx_sdu | 32 |
| mx_pdu | 32 |
| phy | LE 1M PHY |
| packing | 0x00 |
| framing | 0x00 |
| bn | 1 |
| irc | 1 |
| pto | 0 |
| Encryption | 0x00 |
| broadcast_code | TSPX_broadcast_code |

Table 4.105: BIS Configuration

## · Test Procedure

Figure 4.163: HCI/BIS/BI-08-C [Invalid LE BIG Create Sync Parameters and LE ISO Remove Data Path behavior, BIS] MSC

1. The Lower Tester broadcasts the Broadcast ISO Data packets to the IUT.
2. The Upper Tester sends an HCI\_LE\_BIG\_Create\_Sync command to the IUT with an invalid Sync\_Handle.
3. Perform either alternative 3A or 3B depending on the value returned in the HCI\_Command\_Status event.
4. Alternative 3A (Successful HCI\_Command\_Status event):
5. 3A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
6. 3A.2 The IUT sends an HCI\_LE\_BIG\_Sync\_Established event with Status set to Unknown Advertising Identifier (0x42).
7. Alternative 3B (HCI\_Command\_Status event with an error):
8. 3B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unknown Advertising Identifier (0x42).

Repeat Steps 4 and 5 for each round in Table 4.106.

4. The Upper Tester sends an HCI\_LE\_BIG\_Create\_Sync command to the IUT with the correct Sync\_Handle and with Num\_BIS and the BIS set as specified in Table 4.106.
5. Perform either alternative 5A or 5B depending on the value returned in the HCI\_Command\_Status event.
3. Alternative 5A (Successful HCI\_Command\_Status event):
4. 5A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
5. 5A.2 The IUT sends an HCI\_LE\_BIG\_Sync\_Established event with Status set to the error in Table 4.106.
6. Alternative 5B (HCI\_Command\_Status event with an error):
7. 5B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to the error in Table 4.106.
6. The Upper Tester sends an HCI\_LE\_BIG\_Create\_Sync command to the IUT with the correct Sync\_Handle, Num\_BIS set to 0x01, and BIS set to [2] and receives a successful HCI\_Command\_Status in response.
7. Immediately after Step 6, the Upper Tester sends an HCI\_LE\_BIG\_Create\_Sync command to the IUT with the same values as in Step 6.
8. The IUT sends an HCI\_Command\_Status command to the Upper Tester with Status set to Command Disallowed (0x0C).
9. The IUT syncs with the BIG and sends a successful HCI\_LE\_BIG\_Sync\_Established event to the Upper Tester.
10. The Upper Tester sends an HCI\_LE\_Terminate\_BIG command to the IUT, and the IUT responds with Command Disallowed (0x0C).
11. The Upper Tester sends an HCI\_LE\_Remove\_ISO\_Data\_Path command to the IUT with Connection\_Handle set to the connection handle of the BIS.
12. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
13. The Upper Tester sends an HCI\_LE\_BIG\_Create\_Sync command to the IUT using the same BIG\_Handle as the established BIG.
14. Perform either alternative 14A or 14B depending on the value returned in the HCI\_Command\_Status event.
17. Alternative 14A (Successful HCI\_Command\_Status event):
18. 14A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
19. 14A.2 The IUT sends an HCI\_LE\_BIG\_Sync\_Established event with Status set to Command Disallowed (0x0C).
20. Alternative 14B (HCI\_Command\_Status event with an error):
21. 14B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Command Disallowed (0x0C).

| Round | Num_BIS | BIS | HCI Error |
| 1 | 3 | [1, 2, 3] | 0x11, 0x0D |
| 2 | 1 | [3] | 0x11 |
| 3 | 1 | [0] | 0x12 |

Table 4.106: Invalid LE BIG Create Sync Parameters and LE ISO Remove Data Path behavior, BIS rounds

- Expected Outcome

## Pass verdict

In Step 3, the IUT sends an Unknown Advertising Identifier (0x42) error to the Upper Tester.

In Step 5, the IUT sends an event with Status set to the error in Table 4.106 to the Upper Tester. In round 1, error Rejected Due To Limited Resources (0x0D) is allowed if TSPX\_max\_tx\_bises = 2.

In Steps 8, 10, 12, 14A.2, and 14B.1, the IUT sends a Command Disallowed (0x0C) error to the Upper Tester.

## HCI/BIS/BI-09-C [Invalid LE BIG Create Sync Encryption Parameter, BIS]

- Test Purpose

Verify that the IUT properly rejects when the Upper Tester attempts to sync to the BIG when the encryption is the opposite of the BIG encryption type.

- Reference

[12] 7.8.106

- Initial Condition
- -The IUT is configured in the passive scanning state. The Lower Tester is in the advertising state.
- -The IUT is synchronized to the Lower Tester Periodic Advertising.
- Test Procedure

Repeat Steps 1 -3 for each round in Table 4.107.

1. The Lower Tester establishes a BIG with the values in Table 4.105 except that Encryption is set as specified in Table 4.107.
2. The Upper Tester sends an HCI\_LE\_BIG\_Create\_Sync command to the IUT with Encryption set as specified in Table 4.107.
3. Perform either alternative 3A or 3B depending on the value returned in the HCI\_Command\_Status event.

Alternative 3A (Successful HCI\_Command\_Status event):

- 3A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 3A.2 The IUT sends an HCI\_LE\_BIG\_Sync\_Established event with Status set to Encryption Mode Not Acceptable (0x25).

Alternative 3B (HCI\_Command\_Status event with an error):

- 3B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Encryption Mode Not Acceptable (0x25).

| Round | Lower Tester BIG Encrypted | Upper Tester Encryption Parameter |
| 1 | Yes | 0x00 (Broadcast_Code invalid) |
| 2 | No | 0x01 (Broadcast_Code valid) |

Table 4.107: Invalid LE BIG Create Sync Encryption Parameter rounds

- Expected Outcome

## Pass verdict

In Step 3, the IUT sends an Encryption Mode Not Acceptable (0x25) error.

## HCI/BIS/BI-16-C [Reporting Failure to Sync to BIS]

- Test Purpose

Verify that a Synchronized Receiver IUT correctly reports failure to synchronize to BIS.

- Reference

[1] 7.8.106

- Initial Condition
- -The IUT is a Synchronized Receiver.
- -The Lower Tester is an Isochronous Broadcaster and broadcasts periodic advertising streams over the LE 1M PHY. The periodic advertising includes BIGInfo, but the BIS that BIGInfo would point to is never broadcast.

## · Test Procedure

Figure 4.164: HCI/BIS/BI-16-C [Reporting Failure to Sync to BIS] MSC

1. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Parameters command to the IUT using the LE 1M PHY and receives a successful HCI\_Command\_Complete in response.
2. The Upper Tester sends an HCI\_LE\_Set\_Extended\_Scan\_Enable command to the IUT to enable scanning and receives a successful HCI\_Command\_Complete in response.
3. The IUT sends an HCI\_LE\_Extended\_Advertising\_Report event to the Upper Tester.
4. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT to synchronize with the Lower Tester's periodic advertisements. The Upper Tester receives an HCI\_Command\_Status event in response.
5. The IUT sends a successful HCI\_LE\_Periodic\_Advertising\_Sync\_Established event to the Upper Tester. The event returns a Sync\_Handle as one of its parameters.
6. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Report event to the Upper Tester.
7. Immediately following sending an HCI\_LE\_Periodic\_Advertising\_Report to the Upper Tester, the IUT sends an HCI\_LE\_BIGInfo\_Advertising\_Report event.

8. The Upper Tester orders the IUT to synchronize to the Lower Tester's presumed BIG described in BIGInfo by sending an HCI\_LE\_BIG\_Create\_Sync command using the Sync\_Handle returned in the HCI\_LE\_Periodic\_Advertising\_Sync\_Established event and receives an HCI\_Command\_Status event in response.
9. After six BIS events, the IUT sends an HCI\_LE\_BIG\_Sync\_Established event to the Upper Tester with the Status field set to an error, which can be Connection Failed to be Established / Synchronization Timeout (0x3E).
- Expected Outcome

## Pass verdict

The IUT provides the event to the Upper Tester as described in Step 9.

## 4.15.2.1 Broadcast Isochronous Stream Using Non-Test Command, Isochronous Broadcaster

- Test Purpose

Verify that the IUT correctly executes the LE Create BIG Command (the non-test variant) and correctly handles error conditions.

- Reference

[12] 7.8.103, 7.8.109

- Initial Condition
- -State: Periodic Advertising, the IUT is advertiser.
- -TSPX\_max\_tx\_bises is the Max Supported TX NumBIS, as defined in IXIT.
- -TSPX\_max\_iso\_pkt is the ISO Max Data Packet Length, as defined in IXIT.
- -TSPX\_max\_periodic\_adv\_train is the maximum number of periodic advertising trains, as defined in IXIT.
- Test Case Configuration

| Test Case | Step 19 performed |
| HCI/BIS/BV-01-C [Broadcast Isochronous Stream Using Non-Test Command, all PHYs] | No |
| HCI/BIS/BV-02-C [Broadcast Isochronous Stream Using Non-Test Command, not all PHYs] | Yes |

Table 4.108: Broadcast Isochronous Stream Using Non-Test Command, Isochronous Broadcaster test cases

Figure 4.165: Broadcast Isochronous Stream Using Non-Test Command, Isochronous Broadcaster MSC -Page 1 of 2

Figure 4.166: Broadcast Isochronous Stream Using Non-Test Command, Isochronous Broadcaster MSC -Page 2 of 2

1. The Upper Tester sends an HCI\_LE\_Create\_BIG command using an Advertising\_Handle that does not identify a periodic advertising train and the IUT returns error code Unknown Advertising Identifier (0x42).
2. If TSPX\_max\_tx\_bises is less than 0x1F, then the Upper Tester sends an HCI\_LE\_Create\_BIG command using the correct Advertising\_Handle obtained previously and the Num\_BIS field set to TSPX\_max\_tx\_bises plus 1. The IUT returns the error code Rejected due to Limited Resources (0x0D) to the Upper Tester.
3. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the correct Advertising\_Handle obtained previously. The frame bit is set to 0b0 and encryption is disabled. The Upper Tester receives a successful HCI\_Command\_Status event in return.

4. The Upper Tester receives an HCI\_LE\_Create\_BIG\_Complete event from the IUT. The PHY matches the PHY used to create the BIG.
5. The Upper Tester sends an HCI\_LE\_Read\_Buffer\_Size [v2] command and the IUT responds with an HCI\_Command\_Complete event providing an ISO\_Data\_Packet\_Length that matches TSPX\_max\_iso\_pkt.
6. Execute alternative 6A or 6B depending on the ISO\_Data\_Packet\_Length in Step 5. Alternative 6A (ISO\_Data\_Packet\_Length &gt; 0):
4. 6A.1 The Upper Tester sets up Isochronous data paths on the IUT by sending an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT and receives a successful HCI\_Command\_Complete in response.

Alternative 6B (ISO\_Data\_Packet\_Length = 0):

- 6B.1 The Upper Tester uses an implementation-specific data path for Step 7.
7. The Upper Tester begins sending HCI ISO Data Packets to the IUT. The data size is less than the maximum buffer size as read from the IUT.
8. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the Advertising\_Handle used to create the previous BIG but a different BIG\_Handle. The IUT returns the error code Unknown Advertising Identifier (0x42) to the Upper Tester.
9. If the ISO\_Data\_Packet\_Length in Step 5 is &gt; 0, the Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with Connection\_Handle and Direction as in Step 6.
10. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
11. If the ISO\_Data\_Packet\_Length in Step 5 is &gt; 0, the Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with Connection\_Handle set to an invalid value.
12. If the ISO\_Data\_Packet\_Length in Step 5 is &gt; 0, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).
13. The Upper Tester sends an HCI\_LE\_BIG\_Terminate\_Sync command with the correct BIG\_Handle and expects the IUT to respond with Status parameter Command Disallowed (0x0C) if the IUT supports the Synchronized Receiver role feature; otherwise, with Unknown Command.
14. If TSPX\_max\_periodic\_adv\_train is 1, the test ends with a Pass verdict; otherwise, the Upper Tester commands the IUT to open a second periodic advertising train.
15. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the Advertising\_Handle created in the previous step but using the BIG\_Handle from the BIG previously created. The IUT returns the error code Command Disallowed (0x0C) to the Upper Tester.
16. The Upper Tester sends an HCI\_LE\_Terminate\_BIG command using the BIG\_Handle of the existing BIG to the IUT and receives an HCI\_Command\_Status event in response.
17. The Upper Tester receives an HCI\_LE\_Terminate\_BIG\_Complete event from the IUT.
18. If this step is performed (see Table 4.108), the Upper Tester sends an HCI\_LE\_Create\_BIG command using the Advertising\_Handle created in Step 14 and sets PHY=0x07. The IUT returns the error code Unsupported Feature or Parameter value (0x11) to the Upper Tester.
19. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the Advertising\_Handle created in Step 14 and sets PHY=0xF8. The IUT returns the error code Unsupported Feature or Parameter value (0x11) to the Upper Tester.
20. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the Advertising\_Handle created in Step 14 and sets Max\_Transport\_Latency to 0x0004. The IUT returns the error code Invalid HCI Command Parameters (0x12) to the Upper Tester.
21. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the Advertising\_Handle created in Step 14 and sets Max\_Transport\_Latency to 0x0FA1. The IUT returns the error code Invalid HCI Command Parameters (0x12) to the Upper Tester.

- Expected Outcome

## Pass verdict

In Step 1, the IUT returns error code Unknown Advertising Identifier (0x42).

In Step 2, the IUT returns error code Rejected due to Limited Resources (0x0D).

In Step 4, the Upper Tester receives an HCI\_LE\_Create\_BIG\_Complete event from the IUT.

In Step 5, the IUT broadcasts BIS Empty Data Packets.

In Step 5, the ISO\_Data\_Packet\_Length matches TSPX\_max\_iso\_pkt.

In Step 8, the IUT returns the error code Unknown Advertising Identifier (0x42).

HCI\_LE\_BIG\_Terminate\_Sync command, responding with Status parameter Command Disallowed

The IUT refuses to terminate the BIG when the Upper Tester sends an (0x0C).

In Step 10, the IUT returns the error code Command Disallowed (0x0C).

In Step 12, the IUT returns the error code Unknown Connection Identifier (0x02).

In Step 15, the IUT returns the error code Command Disallowed (0x0C).

In Step 17, the IUT returns an HCI\_LE\_Terminate\_BIG\_Complete event to the Upper Tester.

If the IUT does not support all PHYs, then in Step 18 the IUT returns the error code Unsupported Feature or Parameter value (0x11).

In Step 19, the IUT returns the error code Unsupported Feature or Parameter value (0x11).

In Steps 20 -21, the IUT returns the error code Invalid HCI Command Parameters (0x12).

## HCI/BIS/BI-01-C [Ignoring RFU Bits in HCI ISO Data Packets, BIS]

## · Test Purpose

Verify that the IUT ignores RFU bits in ISO Data Packets received from the Upper Tester and sends the ISO data when broadcasting a BIS.

- Reference

[12] 5.4.5

- Initial Condition
- -BIS established per the following configuration and broadcast by the IUT, with the Lower Tester synchronized to the BIS:

| Variable | Value(s) |
| num_bis | 1 |
| sdu_int | 100 ms |
| iso_int | 100 ms |
| nse | 3 |
| mx_sdu | 8 |
| mx_pdu | 8 |
| phy | LE 1M PHY |
| packing | any supported |

Table 4.109: BIS Configuration

| Variable | Value(s) |
| framing | any |
| bn | 1 |
| irc | 3 |
| pto | 0 |
| encryption | any supported |
| broadcast_code | any supported |

- Test Procedure
1. The Upper Tester sends HCI ISO Data packets to the IUT with all RFU field bits set.
2. The IUT broadcasts the ISO Data packets to the Lower Tester.
- Expected Outcome

Figure 4.167: HCI/BIS/BI-01-C [Ignoring RFU Bits in HCI ISO Data Packets, BIS] MSC

## Pass verdict

The IUT broadcasts the ISO Data packets to the Lower Tester.

## HCI/BIS/BV-03-C [Broadcast Isochronous Stream Using Test Command, Time\_Offset]

- Test Purpose

Verify that an Isochronous Broadcaster IUT, when sending unframed data packets, returns a Time\_Offset value of 0 when LE Read ISO TX Sync is called.

- Reference

[12] 7.8.103

- Initial Condition
- -The Isochronous Broadcaster IUT is advertising periodic advertising using selected parameters compatible with the default BIG values as defined in [15] Section 4.11.1, Common Parameters.

## · Test Procedure

Figure 4.168: HCI/BIS/BV-03-C [Broadcast Isochronous Stream Using Test Command, Time\_Offset] MSC

1. The Upper Tester sends an HCI\_LE\_Create\_BIG\_Test command to the IUT. The frame bit is set to 0b0, encryption is disabled, and NumBIS = 1. All other parameters set to default values as defined in [15] Section 4.11.1, Common Parameters. The Upper Tester receives an HCI\_Command\_Status event in return.
2. The IUT sends a successful HCI\_LE\_Create\_BIG\_Complete event to the Upper Tester.
3. The IUT sends advertising PDUs (AUX\_SYNC\_IND+ACAD) to the Lower Tester and BIS Empty Data packets.
4. The Upper Tester sends an HCI\_LE\_Read\_Buffer\_Size [v2] command, and the IUT responds with an HCI\_Command\_Complete event providing an ISO\_Data\_Packet\_Length.

5. Execute alternative 5A or 5B depending on the ISO\_Data\_Packet\_Length in Step 4.

Alternative 5A (ISO\_Data\_Packet\_Length &gt; 0):

- 5A.1 The Upper Tester sets up Isochronous data paths on the IUT by sending an HCI\_LE\_Setup\_ISO\_Data\_Path command with the Data\_Path\_Direction set to Input (0x00) to the IUT.

Alternative 5B (ISO\_Data\_Packet\_Length = 0):

5B.1 The Upper Tester uses an implementation-specific data path for Steps 6 and 7.

6. The Upper Tester begins sending HCI ISO Data packets to the IUT. The data size is the lesser of Default\_Data\_Size, Unframed as defined in [15] Section 4.11.1, Common Parameters, and the maximum buffer size as previously read from the IUT.
7. The IUT sends ISO Data packets to the Lower Tester. The data packets are unframed.
8. The Upper Tester sends an HCI\_LE\_Read\_ISO\_TX\_Sync command to the IUT.
9. The IUT sends an HCI\_Command\_Complete event that includes the Time\_Offset to the Upper Tester. The value of the Time\_Offset return parameter is 0.

## · Expected Outcome

## Pass verdict

In Step 1, the IUT sends a successful HCI\_Command\_Status to the Upper Tester.

In Step 2, the IUT sends a successful HCI\_LE\_Create\_BIG\_Complete event to the Upper Tester.

In Step 9, the value of the Time\_Offset return parameter is 0.

## HCI/BIS/BV-04-C [Broadcast Isochronous Stream, Invalid LE Read ISO TX Sync Parameters]

- Test Purpose

Verify that a Synchronized Receiver IUT returns an error when receiving an HCI\_LE\_Read\_ISO\_TX\_Sync command.

- Reference

[12] 7.8.96

- Initial Condition
- -The Synchronized Receiver IUT is synchronized to a BIS with a Lower Tester acting as an Isochronous Broadcaster.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Read\_ISO\_TX\_Sync command to the IUT with Connection\_Handle set to the current ACL connection handle.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.

## HCI/BIS/BI-02-C [Broadcast Isochronous Stream, Synchronized Receiver, Reject Invalid Commands]

- Test Purpose

Verify that the Synchronized Receiver IUT can correctly reject invalid LE Setup ISO Data Path commands.

- Reference

[12] 7.8.109

- Initial Condition
- -The Lower Tester broadcasts a BIS in a BIG, and the IUT has synchronized to it.
- Test Procedure
1. The Upper Tester creates an ISO output data path by sending an HCI\_LE\_Setup\_ISO\_Data\_Path command with the Connection\_Handle of the active BIS to the IUT, and the IUT sends a successful HCI\_Command\_Complete event in return.
2. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the same Connection\_Handle from Step 1.
3. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).
4. The Upper Tester sends an HCI\_LE\_Setup\_ISO\_Data\_Path command to the IUT with the Connection\_Handle set to an invalid value.
5. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).
- Expected Outcome

Figure 4.169: HCI/BIS/BI-02-C [Broadcast Isochronous Stream, Synchronized Receiver, Reject Invalid Commands] MSC

## Pass verdict

In Step 1, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x00.

In Step 3, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Command Disallowed (0x0C).

In Step 5, the IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to Unknown Connection Identifier (0x02).

## HCI/BIS/BV-05-C [Broadcast Isochronous Stream, Time\_Stamp, Isochronous Broadcaster]

- Test Purpose

Verify that an Isochronous Broadcaster IUT correctly handles receiving a Time\_Stamp in HCI ISO Data packets from the Upper Tester.

- Reference

[13] 5.4.5

- Initial Condition
- -The Isochronous Broadcaster IUT broadcasts a single BIS using framed PDUs.
- -The Lower Tester acts as a Synchronized Receiver and is synchronized to the IUT.
- -All other BIS values as defined in [14] 4.11.1.
- Test Procedure
1. The Upper Tester sends SDU data to the IUT and includes Time\_Stamps in the appropriate HCI ISO Data packets. The SDU data consists of octets that count from 0x00 to 0xFF and roll over back to 0x00, then the count resumes. This count continues across all SDU data.
2. The IUT broadcasts framed PDUs to the Lower Tester.
- Expected Outcome

## Pass verdict

The Lower Tester receives PDUs with data as described in Step 1. Specifically, the contents of the HCI ISO Data packet Time\_Stamp do not corrupt the contents of the data received by the Lower Tester.

## 4.15.2.2 Broadcast Isochronous Stream, Time\_Stamp, Synchronized Receiver

- Test Purpose

Verify that a Synchronized Receiver IUT sets the TS\_Flag bit if the ISO\_Data\_Load field provides a Time\_Stamp to the Upper Tester over the HCI, and the bit is only set if the PB\_Flag field equals 0b00 or 0b10.

Verify that a Synchronized Receiver IUT provides a Time\_Stamp to the Upper Tester over the HCI when time stamps are mandatory.

- Reference

[13] 5.4.5

- Initial Condition
- -The Synchronized Receiver IUT is synchronized to a single BIS using framed PDUs broadcast by the Lower Tester acting in the Isochronous Broadcaster role.
- -All other BIS values as defined in [14] 4.11.1.

- Test Case Configuration

| Test Case | Time_Stamp |
| HCI/BIS/BV-06-C | Optional |
| HCI/BIS/BV-07-C | Mandatory |

Table 4.110: Broadcast Isochronous Stream, Time\_Stamp, Synchronized Receiver test cases

- Test Procedure
1. The Lower Tester sends framed PDUs containing isochronous data to the IUT.
2. The IUT sends the received data to the Upper Tester in HCI ISO Data packets.
- Expected Outcome

## Pass verdict

When the IUT sends HCI ISO Data packets with the PB\_Flag set to 0b00 or 0b10, then:

- -The Packet\_Sequence\_Number, ISO\_SDU\_Length, and Packet\_Status\_Flag fields are present.
- -If Time\_Stamps are mandatory, then the TS flag is set. Otherwise, the TS flag can be set or clear.
- -If the TS\_Flag is set, then a valid Time\_Stamp field is present. Otherwise, Time\_Stamp is not present.

When the IUT sends HCI ISO Data packets with the PB\_Flag set to 0b01 or 0b11, then the TS flag is clear and the Time\_Stamp, Packet\_Sequence\_Number, ISO\_SDU\_Length, and Packet\_Status\_Flag fields are not present.

When Time\_Stamps are provided, the difference between Time\_Stamps of adjacent SDUs is the SDU Interval within ±(SCA\_Broadcaster + SCA\_Scanner) * ISO\_Interval ± Jitter. If SCA\_Scanner is not known, assume that it may be up to 500 ppm.

## HCI/BIS/BI-06-C [Broadcast Isochronous Stream Using Non-Test Command, Invalid BIG Parameters]

- Test Purpose

Verify that the IUT properly rejects the HCI\_LE\_Create\_BIG command with invalid parameters.

- Reference

[13] 7.8.103

- Initial Condition
- -State: Periodic Advertising, the IUT is advertiser.

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the parameter value specified in Table 4.111 for the round. All other parameters are set to valid, supported values.
2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) in round 8 and Invalid HCI Command Parameters (0x12) in all other rounds.
3. Repeat Steps 1 and 2 for each round in Table 4.111.
4. The Upper Tester sends an HCI\_LE\_Create\_BIG command using all of the values specified in Table 4.112.
5. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to a valid error code.

Figure 4.170: HCI/BIS/BI-06-C [Broadcast Isochronous Stream Using Non-Test Command, Invalid BIG Parameters] MSC

| Round | LE_Create_BIG Parameter | Value |
| 1 | BIG_Handle | 0xF0 |
| 2 | Advertising_Handle | 0xF0 |
| 3 | Num_BIS | 0x20 |
| 4 | SDU_Interval | 0x100000 |
| 5 | Max_SDU | 0x1000 |
| 6 | Max_Transport_Latency | 0x0FA1 |
| 7 | RTN | 0x20 |
| 8 | PHY | 0x09 |
| 9 | Packing | 0xF0 |
| 10 | Framing | 0xF0 |
| 11 | Encryption | 0xF0 |

Table 4.111: Parameter values for each case variation

Table 4.112: Parameter values for LE\_Create\_BIG command

| LE_Create_BIG Parameter | Value |
| BIG_Handle | 0xF0 |
| Advertising_Handle | 0xF0 |
| Num_BIS | 0x20 |
| SDU_Interval | 0x10000 |
| Max_SDU | 0x1000 |
| Max_Transport_Latency | 0x0FA1 |
| RTN | 0x20 |
| PHY | 0x09 |
| Packing | 0xF0 |
| Framing | 0xF0 |
| Encryption | 0xF0 |

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) in round 8, Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12) in round 12, and Invalid HCI Command Parameters (0x12) in all other rounds.

In Step 5, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to a valid error code.

## HCI/BIS/BI-07-C [Broadcast Isochronous Stream Using Non-Test Command, Invalid Transport Latency]

- Test Purpose

Verify that a Central IUT rejects the creation of a BIS with an invalid max transport latency value.

- Reference

[13] 7.8.103

- Initial Condition
- -State: Periodic Advertising, the IUT is advertiser.

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Create\_BIG command with Framing set to 1, Max\_Transport\_Latency set to 0x0005, Num\_BIS set to 0x01, Max\_SDU set to 753, SDU\_Interval set to 100 ms, and all others parameters set to the values in [14] Section 4.11.1, Common Parameters.
2. Perform alternative 2A or 2B depending on the IUT response.
- Alternative 2A (Successful HCI\_Command\_Status event):
- 2A.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2A.2 The IUT sends an HCI\_LE\_Create\_BIG\_Complete event to the Upper Tester with Status set to a valid error code, which can be Unsupported Feature or Parameter Value (0x11).

Figure 4.171: HCI/BIS/BI-07-C [Broadcast Isochronous Stream Using Non-Test Command, Invalid Transport Latency] MSC

Alternative 2B (HCI\_Command\_Status with an error code):

- 2B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester with Status set to a valid error code, which can be Unsupported Feature or Parameter Value (0x11).
- Expected Outcome

## Pass verdict

The IUT sends an HCI\_LE\_Create\_BIG\_Complete event to the Upper Tester with Status set to a valid error code, which can be Unsupported Feature or Parameter Value (0x11).

## HCI/BIS/BV-08-C [Number of Completed Packets Event after Sending data in a Broadcaster]

- Test Purpose

Verify that the IUT properly sends the HCI Number of Completed Packets event after the IUT broadcasts Isochronous data.

- Reference

[13] 7.7.19

- Initial Condition
- -State: Periodic Advertising, the IUT is advertiser.
- -The maximum number of BISes in a BIG is defined in the TSPX\_max\_tx\_bises IXIT value.
- -A BIG with TSPX\_max\_tx\_bises BISes has been established with the IUT as Isochronous Broadcaster, Max\_SDU set to 4, BN set to 1, and IRC set to GC. The remaining values are the defaults specified in [14] Section 4.11.1 Common Parameters for BIS but may be adjusted if necessary to establish the BIG.
- -The input data path (Host to Controller) for each BIS is set up to receive data over HCI.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Read\_Buffer\_Size [v2] command to the IUT.
2. The IUT sends a successful HCI\_Command\_Complete event with an ISO\_Data\_Packet\_Length and Total\_Num\_ISO\_Data\_Packets.
3. Let n = Total\_Num\_ISO\_Data\_Packets from Step 2.
4. Throughout the remaining steps:
- a) The IUT broadcasts either empty BIS PDUs or the data from the HCI ISO Data packets in Step 8.
- b) Whenever the IUT sends an HCI\_Number\_Of\_Completed\_Packets event to the Upper Tester, increase n by the sum of the Num\_Completed\_Packets[i] values in the event for those values of i where Connection\_Handle[i] refers to a BIS. Ignore those values of i where Connection\_Handle[i] does not refer to a BIS.
5. Perform Steps 6 -10 a total of 10 times.
6. Perform Steps 7 -9 for each BIS with the BISes in a random order (different each time).
7. If n is zero, wait until n is non-zero.
8. The Upper Tester sends an HCI ISO Data packet to the IUT containing an SDU of length 4 octets and the correct connection handle for the BIS.
9. Decrement n by 1.
10. Wait for 10 seconds.
- Expected Outcome

## Pass verdict

For each BIS, the sum of the Num\_Completed\_Packets[i] where Connection\_Handle[i] refers to that BIS equals 10.

n = Total\_Num\_ISO\_Data\_Packets from Step 2.

## Fail verdict

After Step 10 completes, n does not equal Total\_Num\_ISO\_Data\_Packets from Step 2.

## HCI/BIS/BI-10-C [LE Create BIG, Framed, Unsegmented Mode Unsupported]

- Test Purpose

Verify that the IUT that does not support Framed, Unsegmented mode returns an error in response to the HCI\_LE\_Create\_BIG command.

- Reference

[19] 7.8.103

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Create\_BIG command to the IUT with Framing set to 0x02.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x11.
- Expected Outcome

## Pass verdict

In Step 2, the IUT returns an Unsupported Feature or Parameter Value error.

## HCI/BIS/BI-11-C [Broadcast Isochronous Stream Using Non-Test Command, Invalid BIG Parameters]

- Test Purpose

Verify that the IUT properly rejects the LE Create BIG Command (the non-test variant) with invalid parameters.

- Reference

[13] 7.8.103

- Initial Condition
- -State: Periodic Advertising, the IUT is advertiser.
- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the parameter values specified in Table 4.113. All other parameters are set to valid, supported values.
2. The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x11 or 0x12.

| LE_Create_BIG Parameter | Value |
| Framing | 0x01 |
| SDU_Interval | 0x4E20 |
| Max_Transport_Latency | 0x0A |

Table 4.113: Parameter values

- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to Unsupported Feature or Parameter Value (0x11) or Invalid HCI Command Parameters (0x12) in round 12.

## HCI/BIS/BI-12-C [Broadcast Isochronous Stream, Broadcaster, HCI Read/Write Authenticated Payload Timeout error]

- Test Purpose

Verify that the IUT rejects an HCI Read or Write Authenticated Payload Timeout command applied to a BIS.

- Initial Condition
- -The IUT is the Broadcaster role.
- -BIS is established per the following configuration and broadcast by the IUT:
- Test Procedure
1. The Upper Tester sends the HCI\_Read\_Authenticated\_Payload\_Timeout command to the IUT with Connection\_Handle set to the handle for the BIS.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
3. The Upper Tester sends the HCI\_Write\_Authenticated\_Payload\_Timeout command to the IUT with Connection\_Handle set to the handle for the BIS.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

Table 4.114: BIS Configuration

| Variable | Value(s) |
| num_bis | 1 |
| sdu_int | 100 ms |
| iso_int | 100 ms |
| nse | 3 |
| mx_sdu | 8 |
| mx_pdu | 8 |
| phy | LE 1M PHY |
| packing | any supported |
| framing | any |
| bn | 1 |
| irc | 3 |
| pto | 0 |
| Encryption | 1 |
| broadcast_code | any supported |

## Pass verdict

In Steps 2 and 4, the IUT sends an 0x0C error to the Upper Tester.

## HCI/BIS/BI-14-C [Broadcast Isochronous Stream, Synchronized Receiver, HCI Read/Write Authenticated Payload Timeout error]

## · Test Purpose

Verify that the IUT rejects an HCI Read or Write Authenticated Payload Timeout command applied to a BIS.

- Initial Condition
- -The Lower Tester broadcasts a BIS in a BIG, and the IUT has synchronized to it.
- Test Procedure
1. The Upper Tester sends the HCI\_Read\_Authenticated\_Payload\_Timeout command to the IUT with Connection\_Handle set to the handle for the BIS.
2. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- The Upper Tester sends the HCI\_Write\_Authenticated\_Payload\_Timeout command to the IUT
3. with Connection\_Handle set to the handle for the BIS.
4. The IUT sends an HCI\_Command\_Complete event to the Upper Tester with Status set to 0x0C.
- Expected Outcome

## Pass verdict

In Steps 2 and 4, the IUT sends an 0x0C error to the Upper Tester.

## 4.15.2.3 Reject creating a BIG when the IUT does not support a BIG created from a Periodic Advertising with Responses

- Test Purpose

Verify that an Isochronous Broadcaster IUT fails the command to create a BIG when advertising using Periodic Advertising with Responses.

- Reference

[12] 7.8.103, 7.8.104

- Initial Condition
- -The Isochronous Broadcaster IUT is advertising periodic advertising with responses using selected parameters compatible with the default BIG values as defined in [15] Section 4.11.1, Common Parameters.
- Test Case Configuration

| Test Case | HCI Command |
| HCI/BIS/BV-09-C [Reject creating a BIG when the IUT does not support a BIG created from a Periodic Advertising with Responses, LE Create BIG] | HCI_LE_Create_BIG |
| HCI/BIS/BV-10-C [Reject creating a BIG when the IUT does not support a BIG created from a Periodic Advertising with Responses, LE Create BIG Test] | HCI_LE_Create_BIG_Test |

Table 4.115: Reject creating a BIG when the IUT does not support a BIG created from a Periodic Advertising with Responses test cases

Figure 4.172: Reject creating a BIG when the IUT does not support a BIG created from a Periodic Advertising with Responses MSC

1. The Upper Tester sends the HCI Command specified by Table 4.115 to the IUT.
2. Perform either alternative 2A or 2B depending on the IUT response.

Alternative 2A (Successful HCI\_Command\_Status):

- 2A.1 The IUT sends a successful HCI\_Command\_Status to the Upper Tester.
- 2A.2 The IUT sends an HCI\_LE\_Create\_BIG\_Complete event to the Upper Tester with Status set to 0x42 (Unknown Advertising Identifier).

Alternative 2B (HCI\_Command\_Status with an error code):

- 2B.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x42 (Unknown Advertising Identifier).
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an error to the Upper Tester.

## HCI/BIS/BV-11-C [Broadcast Isochronous Stream testing overlength data on the LE Coded PHY]

- Test Purpose

Verify that the IUT correctly handles Periodic Advertising data plus a BIGInfo that will not fit within the periodic advertising interval.

- Reference

[12] 7.8.103

- Initial Condition
- -State: Periodic Advertising, the IUT is advertiser, PHY is the LE Coded PHY, the periodic advertising interval is 7.5 ms, periodic advertising data is 93 random octets, and periodic advertising is enabled.

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Create\_BIG command using the Advertising\_Handle of the periodic advertising in the initial condition, PHY=0x04, and Encryption = 0x00.
2. The IUT returns an HCI\_Command\_Status or sends a successful HCI\_Command\_Status followed by an HCI\_LE\_Create\_BIG\_Complete event with the error code Packet Too Long (0x45) set on one of them to the Upper Tester.
3. The Upper Tester commands the IUT to stop the periodic advertising.
4. Repeat Steps 1 and 2.
- Expected Outcome

## Pass verdict

In Step 2, the IUT returns the error code Packet Too Long (0x45).

## 4.16 SCO and eSCO Connections

Verify that the IUT correctly rejects an attempt to create a SCO connection when retransmission mandates an eSCO connection.

## 4.16.1 SCO and eSCO default settings

These default settings will be used for the different SCO and eSCO test cases.

Figure 4.173: Default settings used for SCO and eSCO test cases MSC

All events are enabled in the Event\_mask field in HCI\_Set\_Event\_Mask with the exception of bit 30 Page Scan Mode Change event, which is deprecated. Bit 61, which is the LE Meta event, is considered 'don't care', and may or may not be set.

## 4.16.2 Do Not Establish a SCO Connection When Retransmission is Specified

- Test Purpose

Verify that the IUT acting as either Central or Peripheral does not establish a SCO connection when retransmission is specified.

- Initial Condition
- -See Section 4.16.1 SCO and eSCO default settings.
- -An LMP features request has been executed.
- -An ACL connection is established between the IUT and the Lower Tester.
- -Valid parameters for the HCI\_Setup\_Synchronous\_Connection command are defined by the TSPX\_hci\_setup\_synchronous\_connection\_params IXIT value.
- -Valid parameters for the HCI\_Enhanced\_Setup\_Synchronous\_Connection command are defined by the TSPX\_hci\_enhanced\_setup\_connection\_params IXIT value.
- Test Case Configuration

| Test Case | Role | HCI Command |
| HCI/SCO/BV-01-C [11] 7.1.26 | Central | HCI_Setup_Synchronous_Connection |
| HCI/SCO/BV-02-C [11] 7.1.26 | Peripheral | HCI_Setup_Synchronous_Connection |
| HCI/SCO/BV-03-C [11] 7.1.45 | Central | HCI_Enhanced_Setup_Synchronous_Connection |
| HCI/SCO/BV-04-C [11] 7.1.45 | Peripheral | HCI_Enhanced_Setup_Synchronous_Connection |

Table 4.116: Do Not Establish a SCO Connection When Retransmission is Specified test cases

Figure 4.174: Do Not Establish a SCO Connection When Retransmission is Specified MSC

1. The Upper Tester sends an HCI Command as specified in Table 4.116 to the IUT with the supported SCO packet bits set in Packet\_Type, no eSCO ' may be used ' bits set, all eSCO ' shall not be used ' bits set, the Retransmission\_Effort set to 0x01, and all other parameters as specified in the IXIT.
2. The Upper Tester receives an HCI\_Command\_Status event from the IUT indicating that the command failed or receives a successful HCI\_Command\_Status event followed by an HCI\_Synchronous\_Connection\_Complete event with an error.
3. If the Lower Tester receives either an LMP\_SCO\_LINK\_REQ or LMP\_eSCO\_LINK\_REQ PDU, the test fails.
4. The Upper Tester sends the same command with the same parameters as in Step 1, except that Packet\_Type is set to allow all SCO and eSCO packet types supported by the IUT.
5. The Upper Tester receives an HCI\_Command\_Status event from the IUT indicating success.
6. Perform Steps 7 and 8 between 1 to N times where N is the number of different eSCO packet types supported by the IUT as specified in the HCI Command in Step 4. In Step 7, a different eSCO packet type must be used each time.

7. The Lower Tester receives an LMP\_eSCO\_LINK\_REQ PDU from the IUT. If the IUT sends an LMP\_SCO\_LINK\_REQ PDU to the Lower Tester, the test fails.
8. The Lower Tester refuses the eSCO connection by sending an LMP\_NOT\_ACCEPTED\_EXT PDU to the IUT.
9. The Upper Tester receives an HCI\_Synchronous\_Connection\_Complete event indicating failure.
10. Repeat Steps 1 -9 but using a Retransmission\_Effort of 0x02.
- Expected Outcome

## Pass verdict

In Step 2, the IUT sends an HCI\_Command\_Status event indicating that the HCI command specified in Table 4.116 failed, or the IUT sends a successful HCI\_Command\_Status event followed by an HCI\_Synchronous\_Connection\_Complete event with an error.

In Step 5, the IUT sends an HCI\_Command\_Status event indicating success.

In Step 7, the IUT sends an LMP\_eSCO\_LINK\_REQ PDU.

In Step 9, the IUT sends an HCI\_Synchronous\_Connection\_Complete event indicating failure.

## Fail verdict

In Step 3, the IUT sends an LMP\_SCO\_LINK\_REQ or LMP\_eSCO\_LINK\_REQ PDU.

In Step 7, the IUT sends an LMP\_SCO\_LINK\_REQ.

## 4.16.3 Accept Synchronous Connection Request, Ignore Transmit\_Bandwidth, Receive\_Bandwidth, and Retransmission\_Effort, SCO

- Test Purpose

Verify that the IUT acting as either Central or Peripheral ignores the Transmit\_Bandwidth, Receive\_Bandwidth, and Retransmission\_Effort parameters for an SCO connection.

- Initial Condition
- -See Section 4.16.1 SCO and eSCO default settings.
- -An LMP features request has been executed.
- -An ACL connection is established between the IUT and the Lower Tester.
- -Valid parameters for the HCI\_Accept\_Synchronous\_Connection\_Request command are defined by the TSPX\_hci\_accept\_synchronous\_connection\_request\_params IXIT value.
- Test Case Configuration

| Test Case | Role | HCI Command |
| HCI/SCO/BV-09-C [11] 7.1.27 | Central | HCI_Accept_Synchronous_Connection_Request |
| HCI/SCO/BV-10-C [11] 7.1.27 | Peripheral | HCI_Accept_Synchronous_Connection_Request |
| HCI/SCO/BV-11-C [11] 7.1.46 | Central | HCI_Enhanced_Accept_Synchronous_Connection_Request |
| HCI/SCO/BV-12-C [11] 7.1.46 | Peripheral | HCI_Enhanced_Accept_Synchronous_Connection_Request |

Table 4.117: Accept Synchronous Connection Request, Ignore Transmit\_Bandwidth, Receive\_Bandwidth, and Retransmission\_Effort, SCO test cases

## · Test Procedure

Figure 4.175: Accept Synchronous Connection Request, Ignore Transmit\_Bandwidth, Receive\_Bandwidth, and Retransmission\_Effort, SCO MSC

Repeat Steps 1 -10 for each round in Table 4.118.

1. Perform either alternative 1A or 1B depending on the IUT role.
2. Alternative 1A (The IUT is Peripheral):
3. 1A.1 The Lower Tester sends an LMP\_SCO\_LINK\_REQ PDU to the IUT with SCO\_Handle set to 0x01.

Alternative 1B (The IUT is Central):

- 1B.1 The Lower Tester sends an LMP\_SCO\_LINK\_REQ PDU to the IUT with SCO\_Handle set to 0x00.
2. The IUT sends an HCI\_Connection\_Request event with Link\_Type set to 0x00 to the IUT.
3. The Upper Tester sends an HCI command as specified in Table 4.117 to the IUT with Transmit\_Bandwidth, Retransmission\_Effort, and Receive\_Bandwidth set as specified in Table 4.118 and all other parameters as specified in the IXIT.
4. The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
5. Perform either alternative 5A or 5B depending on the IUT role.

Alternative 5A (The IUT is Peripheral):

- 5A.1 The IUT sends an LMP\_ACCEPTED PDU to the Lower Tester.

Alternative 5B (The IUT is Central):

- 5B.1 The IUT sends an LMP\_SCO\_LINK\_REQ PDU to the Lower Tester.
- 5B.2 The Lower Tester sends an LMP\_ACCEPTED PDU to the IUT.
6. The IUT sends an HCI\_Synchronous\_Connection\_Complete command to the Upper Tester with Status set to 0x00, Link\_Type set to SCO, and a Connection\_Handle.
7. The Upper Tester sends an HCI\_Disconnect command to the IUT with Connection\_Handle set to the value in Step 6 and receives a successful HCI\_Command\_Status in response.
8. The IUT sends an LMP\_REMOVE\_SCO\_LINK\_REQ to the Lower Tester with an SCO\_Handle.
9. The Lower Tester sends an LMP\_ACCEPTED PDU to the IUT.
10. The IUT sends a successful HCI\_Disconnection\_Complete event to the Upper Tester.

| Round | Retransmission_Effort | Receive_Bandwidth | Transmit_Bandwidth |
| 1 | 0x01 | 0x00000001 | 0x00000001 |
| 2 | 0x02 | 0xFFFFFFFE | 0xFFFFFFFE |
| 3 | 0xFF | 0xFFFFFFFF | 0xFFFFFFFF |

Table 4.118: Accept Synchronous Connection Request, Ignore Transmit\_Bandwidth, Receive\_Bandwidth, and Retransmission\_Effort, SCO rounds

- Expected Outcome

## Pass verdict

In Step 5A.1, the IUT sends an LMP\_ACCEPTED PDU with the OpCode set to LMP\_SCO\_LINK\_REQ.

In Step 5B.1, the IUT sends an LMP\_SCO\_LINK\_REQ PDU to the Lower Tester.

## 4.16.4 SCO Connection creation fails when AES-CCM encryption is enabled

- Test Purpose

Verify that if AES-CCM encryption has been enabled on an ACL connection, SCO connection creation requests (using the HCI Enhanced Setup Synchronous Connection command) from the Upper Tester will be rejected by the IUT with Error\_Code 0x0E: Rejected Due to Security Reasons.

- Reference

[1] 4.6.1

- Initial Condition
- -The IUT is in the role specified in Table 4.119.
- -An AES-CCM encrypted point-to-point connection has been established between the IUT and the Lower Tester.

- Test Case Configuration

| Test Case | Role | HCI Command |
| HCI/SCO/BV-13-C [SCO Connection creation fails when AES-CCM encryption is enabled - Setup Synchronous Connection] | Central | HCI_Setup_Synchronous_Connection |
| HCI/SCO/BV-14-C [SCO Connection creation fails when AES-CCM encryption is enabled - Setup Synchronous Connection] | Peripheral | HCI_Setup_Synchronous_Connection |
| HCI/SCO/BV-15-C [SCO Connection creation fails when AES-CCM encryption is enabled - Enhanced Setup Synchronous Connection] | Central | HCI_Enhanced_Setup_Synchronous_Connection |
| HCI/SCO/BV-16-C [SCO Connection creation fails when AES-CCM encryption is enabled - Enhanced Setup Synchronous Connection] | Peripheral | HCI_Enhanced_Setup_Synchronous_Connection |

Table 4.119: SCO Connection creation fails when AES-CCM encryption is enabled test cases

- Test Procedure
1. The Upper Tester sends the HCI command specified in Table 4.119 to the IUT with Packet\_Type set to 0x07 (HV1, HV2, HV3).
2. Perform either alternative 2A or 2B depending on the IUT 's response.

Alternative 2A (HCI\_Command\_Status = 0x0E):

- 2A.1 The IUT sends an HCI\_Command\_Status event to the Upper Tester with Status set to 0x0E.

Alternative 2B (Successful HCI\_Command\_Status):

- 2B.1 The IUT sends a successful HCI\_Command\_Status event to the Upper Tester.
- 2B.2 The IUT sends an HCI\_Synchronous\_Connection\_Complete event to the Upper Tester with Status set to 0x0E.
- Expected Outcome

## Pass verdict

The IUT responds to the HCI\_Enhanced\_Setup\_Synchronous\_Connection command with either an HCI\_Command\_Status event or an HCI\_Synchronous\_Connection\_Complete event with Error\_Code 0x0E: Rejected Due to Security Reasons.

- Notes

If the IUT sends an LMP\_SCO\_LINK\_REQ to the Lower Tester, the Lower Tester should accept the request.

## 4.17 Event Versioning

## 4.17.1 Check correct handling of HCI Encryption Change event, BR/EDR

- Test Purpose

Tests that the IUT returns the correct HCI Encryption Change event on BR/EDR depending on which of the v1 and v2 versions are set in the event mask.

- Reference

[17] 7.7.8

- Initial Condition
- -The IUT is in the Peripheral role.
- -The min supported encryption key size is specified by the TSPX\_min\_supported\_encryption\_key\_size IXIT value.
- Test Case Configuration

| Test Case ID | Alternative |
| HCI/EVV/BV-01-C | A |
| HCI/EVV/BV-02-C | B |

Table 4.120: Check correct handling of HCI Encryption Change event, BR/EDR test cases

- Test Procedure
1. The Upper Tester sends an HCI\_Set\_Event\_Mask command that enables both [v1] and [v2] versions of the HCI\_Encryption\_Change event.
2. The Upper Tester sends an HCI\_Set\_Connection\_Encryption command to the IUT with Encryption\_Enable set to 0x01 and receives a successful HCI\_Command\_Complete in response.
3. The Lower Tester rejects every received LMP PDU.
4. Perform either alternative 4A or 4B depending on the alternative specified in Table 4.120. Alternative 4A (alternative A is specified):
- 4A.1 The IUT sends the HCI\_Encryption\_Change [v1] event to the Upper Tester. Alternative 4B (alternative B is specified):
- 4B.1 The IUT sends the HCI\_Encryption\_Change [v2] event to the Upper Tester.
5. The Upper Tester sends an HCI\_Set\_Event\_Mask command that enables the [v2] version of the HCI\_Encryption\_Change event but masks out the [v1] version.
6. The Upper Tester sends an HCI\_Set\_Connection\_Encryption command to the IUT with Encryption\_Enable set to 0x01 and receives a successful HCI\_Command\_Complete in response.
7. The Lower Tester rejects every received LMP PDU.
- Perform either alternative 8A or 8B depending on the alternative specified in Table 4.120.
8. Alternative 8A (alternative A is specified):
- 8A.1 The IUT does not send an HCI\_Encryption\_Change event.

Alternative 8B (alternative B is specified):

- 8B.1 The IUT sends the HCI\_Encryption\_Change [v2] event to the Upper Tester.
9. The Upper Tester sends an HCI\_Set\_Event\_Mask command that enables the HCI\_Encryption\_Change [v1] of the event but masks out the [v2] version.
10. The Upper Tester sends an HCI\_Set\_Connection\_Encryption command to the IUT with Encryption\_Enable set to 0x01 and receives a successful HCI\_Command\_Complete in response.
11. The Lower Tester rejects every received LMP PDU.
12. The IUT sends the HCI\_Encryption\_Change [v1] event to the Upper Tester.

- Expected Outcome

## Pass verdict

The IUT sends the [v1] versions of the events in Steps 4A.1 and 12.

The IUT sends the [v2] versions of the events in Steps 4B.1 and 8B.1.

The IUT does not send an event in Step 8A.1.

## 4.17.2 Check correct handling of HCI Encryption Change event with two versions, LE

## · Test Purpose

Tests that the IUT returns the correct HCI Encryption Change event on LE depending on which of the v1 and v2 versions are set in the event mask.

- Reference

[17] 7.7.8

- Initial Condition
- -The IUT is in the role specified in Table 4.121.
- Test Case Configuration

Table 4.121: Check correct handling of HCI Encryption Change event with two versions, LE test cases

| Test Case ID | Role | LL Test | Alternative |
| HCI/EVV/BV-03-C | Peripheral | LL/SEC/PER/BV-01-C | A |
| HCI/EVV/BV-04-C | Peripheral | LL/SEC/PER/BV-01-C | B |
| HCI/EVV/BV-05-C | Central | LL/SEC/CEN/BV-01-C | A |
| HCI/EVV/BV-06-C | Central | LL/SEC/CEN/BV-01-C | B |

## · Test Procedure

1. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables both [v1] and [v2] versions of the HCI event specified in Table 4.121.
2. Perform the LL test specified in Table 4.121 up to the HCI\_Encryption\_Change event.
3. Perform either alternative 3A or 3B depending on the alternative specified in Table 4.121. Alternative 3A (alternative A is specified):
4. 3A.1 The IUT sends the HCI\_Encryption\_Change [v1] event to the Upper Tester. Alternative 3B (alternative B is specified):
5. 3B.1 The IUT sends the HCI\_Encryption\_Change [v2] event to the Upper Tester.
4. The Lower Tester terminates the connection and then creates a new one in the same role.
5. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the [v2] version of the HCI\_Encryption\_Change event but masks out the [v1] version.
6. Perform the LL test specified in Table 4.121 up to the HCI\_Encryption\_Change event.
7. Perform either alternative 7A or 7B depending on the alternative specified in Table 4.121.
10. Alternative 7A (alternative A is specified):
11. 7A.1 The IUT does not send an HCI\_Encryption\_Change event.

Alternative 7B (alternative B is specified):

- 7B.1 The IUT sends the HCI\_Encryption\_Change [v2] event to the Upper Tester.
8. The Lower Tester terminates the connection and then creates a new one in the same role.

9. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_Encryption\_Change [v1] event but masks out the [v2] version.
10. Perform the LL test specified in Table 4.121 up to the HCI\_Encryption\_Change [v1] event.
11. The IUT sends the HCI\_Encryption\_Change [v1] event to the Upper Tester.
- Expected Outcome

## Pass verdict

The IUT sends the HCI\_Encryption\_Change [v1] event in Steps 3A.1 and 11.

The IUT sends the HCI\_Encryption\_Change [v2] event in Steps 3B.1 and 7B.1.

The IUT does not send an HCI\_Encryption\_Change event in Step 7A.1.

## 4.17.3 Check correct handling of LE Periodic Advertising Sync Established event with two versions

- Test Purpose

Tests that the IUT returns the correct HCI\_LE\_Periodic\_Advertising\_Sync\_Established event depending on which of the v1 and v2 versions are set in the event mask.

- Reference

[17] 7.7.65.14

- Initial Condition
- -The IUT is scanning.
- Test Case Configuration

| Test Case ID | Alternative |
| HCI/EVV/BV-07-C | A |
| HCI/EVV/BV-08-C | B |

Table 4.122: Check correct handling of LE Periodic Advertising Sync Established event with two versions test cases

- Test Procedure
1. The Lower Tester begins advertising using ADV\_EXT\_IND and AUX\_ADV\_IND PDUs. The ADV\_EXT\_IND PDUs include an AuxPtr that refers to the AUX\_ADV\_IND PDU on the secondary advertising channel. The AUX\_ADV\_IND PDUs include the AdvA field containing the Lower Tester address and the SyncInfo field referring to a missing AUX\_SYNC\_IND PDU such that sync is not possible. The Lower Tester continues advertising until directed to stop in the test procedure.
2. The IUT sends an HCI\_LE\_Extended\_Advertising\_Report event to the Upper Tester containing a nonzero Periodic\_Advertising\_Interval, Data Status in the Event\_Type[i] field set to the value 0b00 (Complete).
3. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables both [v1] and [v2] versions of the HCI\_LE\_Periodic\_Advertising\_Sync\_Established event.
4. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT and receives a successful HCI\_Command\_Status event in response.
5. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync\_Cancel command to the IUT and receives a successful HCI\_Command\_Complete event in response.

- 6.
- Perform either alternative 6A or 6B depending on the alternative specified in Table 4.122. Alternative 6A (alternative A is specified):
- 6A.1 The IUT sends the HCI\_LE\_Periodic\_Advertising\_Sync\_Established [v1] event to the Upper Tester.

Alternative 6B (alternative B is specified):

- 6B.1 The IUT sends the HCI\_LE\_Periodic\_Advertising\_Sync\_Established [v2] event to the Upper Tester.
7. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the [v2] version of the HCI\_LE\_Periodic\_Advertising\_Sync\_Established event but masks out the [v1] version.
8. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT and receives a successful HCI\_Command\_Status event in response.
9. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync\_Cancel command to the IUT and receives a successful HCI\_Command\_Complete event in response.
10. Perform either alternative 10A or 10B depending on the alternative specified in Table 4.122. Alternative 10A (alternative A is specified):
- 10A.1 The IUT does not send an HCI\_LE\_Periodic\_Advertising\_Sync\_Established event. Alternative 10B (alternative B is specified):
- 10B.1 The IUT sends the HCI\_LE\_Periodic\_Advertising\_Sync\_Established [v2] event to the Upper Tester.
11. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Periodic\_Advertising\_Sync\_Established [v1] event but masks out the [v2] version.
12. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync command to the IUT and receives a successful HCI\_Command\_Status event in response.
13. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Create\_Sync\_Cancel command to the IUT and receives a successful HCI\_Command\_Complete event in response.
14. The IUT sends the HCI\_LE\_Periodic\_Advertising\_Sync\_Established [v1] event to the Upper Tester with error code 0x3E.
- Expected Outcome

## Pass verdict

The IUT sends the [v1] versions of the events in Steps 6A.1 and 12.

The IUT sends the [v2] versions of the events in Steps 6B.1 and 10B.1.

The IUT does not send an event in Step 10A.1.

## 4.17.4 Check correct handling of LE Periodic Advertising Report event with two versions

- Test Purpose

Tests that the IUT returns the correct LE Periodic Advertising Report event depending on which of the v1 and v2 versions are set in the event mask.

## · Reference

[17] 7.7.65.15

- Initial Condition
- -The IUT is scanning.
- -The Lower Tester is configured to send periodic advertising events.
- -The IUT is synchronized to the periodic advertising sent by the Lower Tester.

- Test Case Configuration

Table 4.123: Check correct handling of LE Periodic Advertising Report event with two versions test cases

| Test Case ID | Alternative |
| HCI/EVV/BV-09-C | A |
| HCI/EVV/BV-10-C | B |

## · Test Procedure

1. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables both [v1] and [v2] versions of the HCI\_LE\_Periodic\_Advertising\_Report event.
2. 2.
3. Perform either alternative 2A or 2B depending on the alternative specified in Table 4.123. Alternative 2A (alternative A is specified):
4. 2A.1 The IUT sends at least one HCI\_LE\_Periodic\_Advertising\_Report [v1] event to the Upper Tester.

Alternative 2B (alternative B is specified):

- 2B.1 The IUT sends at least one HCI\_LE\_Periodic\_Advertising\_Report [v2] event to the Upper Tester.
3. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the [v2] version of the HCI\_LE\_Periodic\_Advertising\_Report event but masks out the [v1] version.
4. Perform either alternative 4A or 4B depending on the alternative specified in Table 4.123.
- Alternative 4A (alternative A is specified):
- 4A.1 The IUT does not send any HCI\_LE\_Periodic\_Advertising\_Report events. Alternative 4B (alternative B is specified):
- 4B.1 The IUT sends HCI\_LE\_Periodic\_Advertising\_Report [v2] events to the Upper Tester.
5. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Periodic\_Advertising\_Report [v1] event but masks out the [v2] version.
6. The IUT sends HCI\_LE\_Periodic\_Advertising\_Report [v1] events to the Upper Tester.
- Note

Steps 3 and 5 may take a little while for the new event mask to take effect, and therefore Steps 4 and 6 should run for at least 50 periodic connection events or, for Step 6, until a [v1] event is sent to the Upper Tester.

- Expected Outcome

## Pass verdict

The IUT sends the [v1] versions of the events in Steps 2A.1 and 6.

The IUT sends the [v2] versions of the events in Steps 2B.1 and 4B.1.

The IUT does not send an event in Step 4A.1.

## 4.17.5 Check correct handling of HCI LE Periodic Advertising Sync Transfer Received event with two versions

- Test Purpose

Tests that the IUT returns the correct HCI LE Periodic Advertising Sync Transfer Received event on LE depending on which of the v1 and v2 versions are set in the event mask.

- Reference

[17] 7.7.65.24

- Initial Condition
- -An ACL connection has been established between the Central IUT and the Peripheral Lower Tester with a valid Connection Handle.

## · Test Case Configuration

| Test Case ID | Alternative |
| HCI/EVV/BV-11-C | A |
| HCI/EVV/BV-12-C | B |

Table 4.124: Check correct handling of HCI LE Periodic Advertising Sync Transfer Received event with two versions test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables both [v1] and [v2] versions of the HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer event.
2. The Upper Tester sends an HCI\_LE\_Set\_Periodic\_Advertising\_Sync\_Transfer\_Parameters command to the IUT with Mode set to 0x02, Skip set to 0, and receives a successful HCI\_Command\_Complete event in response.
3. The Lower Tester sends an LL\_PERIODIC\_SYNC\_IND PDU to the IUT with ID set to any nonzero value, SyncInfo set to any values such that sync is not possible, and all other parameters set to valid values.
4. Perform either alternative 4A or 4B depending on the alternative specified in Table 4.124. Alternative 4A (alternative A is specified):
- 4A.1 The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer\_Received [v1] event to the Upper Tester with status set to 0x3E (Connection Failed to be established).
- Alternative 4B (alternative B is specified):
- 4B.1 The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer\_Received [v2] event to the Upper Tester with status set to 0x3E (Connection Failed to be established).
5. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer\_Received [v2] event but masks out the [v1] version.
6. The Lower Tester sends an LL\_PERIODIC\_SYNC\_IND PDU to the IUT with ID set to any nonzero value, SyncInfo set to any values such that sync is not possible, and all other parameters set to valid values.
7. Perform either alternative 7A or 7B depending on the alternative specified in Table 4.124. Alternative 7A (alternative A is specified):
- 7A.1 The IUT does not send an HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer\_Received [v1] event.

Alternative 7B (alternative B is specified):

- 7B.1 The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer\_Received [v2] event to the Upper Tester with status set to 0x3E (Connection Failed to be established).
8. The Upper Tester sends an HCI\_LE\_Periodic\_Advertising\_Terminate\_Sync command to the IUT and receives a successful HCI\_Command\_Complete event in response.
9. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer\_Received [v1] event but masks out the [v2] version.
10. The Lower Tester sends an LL\_PERIODIC\_SYNC\_IND PDU to the IUT with ID set to any nonzero value, SyncInfo set to any values such that sync is not possible, and all other parameters set to valid values.

11. The IUT sends an HCI\_LE\_Periodic\_Advertising\_Sync\_Transfer\_Received [v1] event to the Upper Tester with status set to 0x3E (Connection Failed to be established).
- Expected Outcome

## Pass verdict

The IUT sends the [v1] versions of the events in Steps 4A.1 and 12.

The IUT sends the [v2] versions of the events in Steps 4B.1 and 7B.1.

The IUT does not send an event in Step 7A.1.

## 4.17.6 Check correct handling of LE Enhanced Connection Complete Event with two versions and legacy LE Connection Complete Event, Central

- Test Purpose

Tests that the central IUT returns the correct HCI\_LE\_Enhanced\_Connection\_Complete event depending on which of the v1 and v2 versions are set in the event mask.

- Reference

[17] 7.7.65.1

- Initial Condition
- -State: Standby
- Test Case Configuration

| Test Case ID | Alternative |
| HCI/EVV/BV-13-C | A |
| HCI/EVV/BV-14-C | B |
| HCI/EVV/BV-15-C | C |

Table 4.125: Check correct handling of LE Enhanced Connection Complete Event with two versions and legacy LE Connection Complete Event, Central test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Connection\_Complete event and enables both [v1] and [v2] versions of the HCI\_LE\_Enhanced\_Connection\_Complete event.
2. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT and receives a successful HCI\_Command\_Status event in response.
3. The Upper Tester sends an HCI\_LE\_Create\_Connection\_Cancel command to the IUT and receives a successful HCI\_Command\_Complete event in response.
4. Perform either alternative 4A, 4B, or 4C depending on the alternative specified in Table 4.125. Alternative 4A (alternative A is specified):
- 4A.1 The IUT sends the HCI\_LE\_Connection\_Complete event to the Upper Tester with a valid error code.

Alternative 4B (alternative B is specified):

- 4B.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v1] event to the Upper Tester with a valid error code.
- Alternative 4C (alternative C is specified):
- 4C.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v2] event to the Upper Tester with a valid error code.

5. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that disables the HCI\_LE\_Connection\_Complete event and enables the [v2] version of the HCI\_LE\_Enhanced\_Connection\_Complete event but masks out the [v1] version.
6. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT and receives a successful HCI\_Command\_Status event in response.
7. The Upper Tester sends an HCI\_LE\_Create\_Connection\_Cancel command to the IUT and receives a successful HCI\_Command\_Complete event in response.
8. Perform either alternative 8A, 8B, or 8C depending on the alternative specified in Table 4.125. Alternative 8A (alternative A is specified):
5. 8A.1 The IUT does not send an HCI\_LE\_Connection\_Complete or HCI\_LE\_Enhanced\_Connection\_Complete event.
6. Alternative 8B (alternative B is specified):
7. 8B.1 The IUT does not send an HCI\_LE\_Connection\_Complete or HCI\_LE\_Enhanced\_Connection\_Complete event.
8. Alternative 8C (alternative C is specified):
9. 8C.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v2] event to the Upper Tester with a valid error code.
9. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that disables the HCI\_LE\_Connection\_Complete event and enables the HCI\_LE\_Enhanced\_Connection\_Complete [v1] event but masks out the [v2] version.
10. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT and receives a successful HCI\_Command\_Status event in response.
11. The Upper Tester sends an HCI\_LE\_Create\_Connection\_Cancel command to the IUT and receives a successful HCI\_Command\_Complete event in response.
12. Perform either alternative 12A, 12B, or 12C depending on the alternative specified in Table 4.125. Alternative 12A (alternative A is specified):
14. 12A.1 The IUT does not send an HCI\_LE\_Connection\_Complete or HCI\_LE\_Enhanced\_Connection\_Complete event.
15. Alternative 12B (alternative B is specified):
16. 12B.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v1] event to the Upper Tester with a valid error code.
17. Alternative 12C (alternative C is specified):
18. 12C.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v1] event to the Upper Tester with a valid error code.
13. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Connection\_Complete event and masks out both the [v1] and [v2] versions of the HCI\_LE\_Enhanced\_Connection\_Complete event.
14. The Upper Tester sends an HCI\_LE\_Create\_Connection command to the IUT and receives a successful HCI\_Command\_Status event in response.
15. The Upper Tester sends an HCI\_LE\_Create\_Connection\_Cancel command to the IUT and receives a successful HCI\_Command\_Complete event in response.
16. The IUT sends the HCI\_LE\_Connection\_Complete event to the Upper Tester with a valid error code.

- Expected Outcome

## Pass verdict

The IUT sends the HCI\_LE\_Connection\_Complete event in Steps 4A.1 and 16.

The IUT sends the [v1] versions of the events in Steps 4B.1, 12B.1, and 12C.1.

The IUT sends the [v2] versions of the events in Steps 4C.1 and 8C.1.

The IUT does not send an event in Steps 8A.1, 8B.1, and 12A.1.

## 4.17.7 Check correct handling of LE Enhanced Connection Complete Event with two versions and legacy LE Connection Complete Event, Peripheral

- Test Purpose

Tests that the peripheral IUT returns the correct HCI\_LE\_Enhanced\_Connection\_Complete event depending on which of the v1 and v2 versions are set in the event mask.

- Reference

[17] 7.7.65.1

- Initial Condition
- -State: Standby
- Test Case Configuration

| Test Case ID | Alternative |
| HCI/EVV/BV-16-C | A |
| HCI/EVV/BV-17-C | B |
| HCI/EVV/BV-18-C | C |

Table 4.126: Check correct handling of LE Enhanced Connection Complete Event with two versions and legacy LE Connection Complete Event, Peripheral test cases

- Test Procedure
1. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Connection\_Complete event and enables both [v1] and [v2] versions of the HCI\_LE\_Enhanced\_Connection\_Complete event.
2. The Upper Tester sends the HCI\_LE\_Set\_Advertising\_Parameters command to the IUT with Advertising\_Type set to 0x00 (ADV\_IND), Advertising\_Filter\_Policy set to 0x00, and other parameters valid, and receives a successful HCI\_Command\_Complete event in response.
3. The Upper Tester sends an HCI\_LE\_Set\_Advertising\_Enable command to the IUT with Enable set to 0x01 and receives a successful HCI\_Command\_Complete event in response.
4. The IUT sends an ADV\_IND PDU to the Lower Tester.
5. The Lower Tester sends a CONNECT\_IND PDU to the IUT but does not send any ACL packet to the IUT.
6. Perform either alternative 6A, 6B, or 6C depending on the alternative specified in Table 4.126. Alternative 6A (alternative A is specified):
- 6A.1 The IUT sends the HCI\_LE\_Connection\_Complete event to the Upper Tester. Alternative 6B (alternative B is specified):
- 6B.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v1] event to the Upper Tester.

Alternative 6C (alternative C is specified):

- 6C.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v2] event to the Upper Tester.
7. The IUT is sending an HCI\_Disconnection\_Complete event with reason set to 0x3E (Connection Failed to be established)
8. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that disables the HCI\_LE\_Connection\_Complete event and enables the [v2] version of the HCI\_LE\_Enhanced\_Connection\_Complete event but masks out the [v1] version.

Repeat Steps 2 -5.

9. Perform either alternative 9A, 9B, or 9C depending on the alternative specified in Table 4.126. Alternative 9A (alternative A is specified):
2. 9A.1 The IUT does not send an HCI\_LE\_Connection\_Complete or HCI\_LE\_Enhanced\_Connection\_Complete event.
3. Alternative 9B (alternative B is specified):
4. 9B.1 The IUT does not send an HCI\_LE\_Connection\_Complete or HCI\_LE\_Enhanced\_Connection\_Complete event.
5. Alternative 9C (alternative C is specified):
6. 9C.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v2] event to the Upper Tester.
10. The IUT is sending an HCI\_Disconnection\_Complete event with reason set to 0x3E (Connection Failed to be established).
11. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that disables the HCI\_LE\_Connection\_Complete event and enables the [v1] version of the HCI\_LE\_Enhanced\_Connection\_Complete event but masks out the [v2] version.

Repeat Steps 2 -5.

12. Perform either alternative 12A, 12B, or 12C depending on the alternative specified in Table 4.126. Alternative 12A (alternative A is specified):
2. 12A.1 The IUT does not send an HCI\_LE\_Connection\_Complete or HCI\_LE\_Enhanced\_Connection\_Complete event.
3. Alternative 12B (alternative B is specified):
4. 12B.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v1] event to the Upper Tester.
5. Alternative 12C (alternative C is specified):
6. 12C.1 The IUT sends the HCI\_LE\_Enhanced\_Connection\_Complete [v1] event to the Upper Tester.
13. The IUT is sending an HCI\_Disconnection\_Complete event with reason set to 0x3E (Connection Failed to be established).
14. The Upper Tester sends an HCI\_LE\_Set\_Event\_Mask command that enables the HCI\_LE\_Connection\_Complete event and masks out both the [v1] and [v2] versions of the HCI\_LE\_Enhanced\_Connection\_Complete event.

Repeat Steps 2 -5.

15. The IUT sends the HCI\_LE\_Connection\_Complete event to the Upper Tester.
16. The IUT is sending an HCI\_Disconnection\_Complete event with reason set to 0x3E (Connection Failed to be established).

## · Expected Outcome

## Pass verdict

The IUT sends the HCI\_LE\_Connection\_Complete event in Steps 6A.1 and 15.

The IUT sends the [v1] versions of the events in Steps 6B.1, 12B.1, and 12C.1.

The IUT sends the [v2] versions of the events in Steps 6C.1 and 9C.1.

The IUT does not send an event in Steps 9A.1, 9B.1, and 12A.1.

## 5 Test case mapping

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.

The columns for the TCMT are defined as follows:

Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for HCI [2].

If a test case is mandatory within the respective layer, then the y/x reference is omitted.

Feature: A brief, informal description of the feature being tested.

Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [3].

For the purpose and structure of the ICS/IXIT, refer to [3].

| Item | Feature | Test Case(s) |
| (HCI 1a/1 AND NOT HCI 1/1b) OR (HCI 1a/3 AND NOT HCI 1/1c) OR (HCI 1a/4 AND NOT HCI 1/1d) | Command Complete Event on each supported controller | HCI/GEV/BV-01-C |
| LL 3/9 | Extended Advertising Extended Scanning | HCI/GEV/BV-02-C HCI/GEV/BV-04-C |
| LL 4/7 | Extended Scanning | HCI/GEV/BV-03-C |
| HCI 1/1 | RFU OGF | HCI/GEV/BI-01-C |
| HCI 1a/1 | Reset Command | HCI/DSU/BV-01-C |
| LL 1/1 AND LL 3/2 AND HCI 1a/4 | Reset Command | HCI/DSU/BV-02-C |
| LL 1/4 AND HCI 1a/4 | Reset Command | HCI/DSU/BV-03-C |
| LL 1/2 AND HCI 1a/4 | Reset Command | HCI/DSU/BV-04-C |
| LL 1/3 AND HCI 1a/4 | Reset Command | HCI/DSU/BV-05-C |
| LL 1/5 AND HCI 1a/4 | Reset Command | HCI/DSU/BV-06-C |
| HCI 1a/3 | Reset Command | HCI/DSU/BV-07-C |
| HCI 16/68 AND CORE 1b/61 | Set Min Encryption Key Size, Core v6.1 or earlier | HCI/CCO/BV-21-C HCI/CCO/BI-35-C |
| HCI 16/68 AND CORE 1a/62 | Set Min Encryption Key Size, Core v6.2 or later | HCI/CCO/BV-27-C |

| Item | Feature | Test Case(s) |
| HCI 3/1 AND NOT HCI 3/5 AND (HCI 9/6 OR HCI 9/7) AND HCI 1a/1 | Read Buffer Size Command, BR/EDR, [e]SCO data over HCI supported | HCI/CFC/BV-01-C |
| HCI 3/1 AND NOT HCI 3/5 AND (HCI 9/6 OR HCI 9/7) AND HCI 1a/3 | Read Buffer Size Command, AMP, [e]SCO data over HCI supported | HCI/CFC/BV-03-C |
| HCI 3/1 AND NOT HCI 3/5 AND NOT HCI 9/6 AND NOT HCI 9/7 AND HCI 1a/1 | Read Buffer Size Command, BR/EDR, [e]SCO data over HCI not supported | HCI/CFC/BV-06-C |
| HCI 3/1 AND NOT HCI 3/5 AND NOT HCI 9/6 AND NOT HCI 9/7 AND HCI 1a/3 | Read Buffer Size Command, AMP, [e]SCO data over HCI not supported | HCI/CFC/BV-07-C |
| HCI 3/5 AND NOT HCI 3/1 | LE Read Buffer Size Command | HCI/CFC/BV-02-C |
| HCI 3/1 AND HCI 3/5 AND (HCI 9/6 OR HCI 9/7) AND NOT HCI 14/23 | Read Buffer Size Command, BR/EDR/LE, Combined Data Buffers, [e]SCO data over HCI supported | HCI/CFC/BV-04-C |
| HCI 3/1 AND HCI 3/5 AND (HCI 9/6 OR HCI 9/7) AND HCI 14/23 | Read Buffer Size Command, BR/EDR/LE, Separate Data Buffers, [e]SCO data over HCI supported | HCI/CFC/BV-05-C |
| HCI 3/1 AND HCI 3/5 AND NOT HCI 9/6 AND NOT HCI 9/7 AND NOT HCI 14/23 | Read Buffer Size Command, BR/EDR/LE, Combined Data Buffers, [e]SCO data over HCI not supported | HCI/CFC/BV-08-C |
| HCI 3/1 AND HCI 3/5 AND NOT HCI 9/6 AND NOT HCI 9/7 AND HCI 14/23 | Read Buffer Size Command, BR/EDR/LE, Separate Data Buffers, [e]SCO data over HCI not supported | HCI/CFC/BV-09-C |
| HCI 3/1 AND NOT HCI 9/6 AND NOT HCI 9/7 | Read Buffer Size Command, [e]SCO data over HCI not supported | HCI/CFC/BI-03-C |
| HCI 3/1 AND (HCI 9/6 OR HCI 9/7) | Read Buffer Size Command, [e]SCO data over HCI supported | HCI/CFC/BI-04-C |
| HCI 4/2 | Read Local Supported Commands command [v1] | HCI/CIN/BV-03-C |
| HCI 4/2a | Read Local Supported Commands command [v2] | HCI/CIN/BV-17-C |

| Item | Feature | Test Case(s) |
| (HCI 1a/1 OR HCI 1a/3) AND HCI 4/3 | Read Local Supported Features Command | HCI/CIN/BV-01-C |
| (HCI 1a/1 OR HCI 1a/3) AND HCI 4/4 | Read Local Extended Features Command | HCI/CIN/BV-02-C |
| HCI 4/1 | Read Local Version Information Command | HCI/CIN/BV-04-C |
| HCI 1a/4 | LE Filter Accept List | HCI/CIN/BV-06-C |
| HCI 4/12 | Read Local Simple Pairing Options Command | HCI/CIN/BV-08-C |
| HCI 4/10 | Read Local Supported Codecs [v1] | HCI/CIN/BV-10-C |
| HCI 4/13 AND HCI 4/14 AND HCI 4/15 | Locally supported Codecs | HCI/CIN/BV-11-C |
| HCI 4/8 | LE Read Local Supported Features Page 0 Command | HCI/CIN/BV-12-C |
| HCI 4/18 | LE Read All Local Supported Features Page 0 Command | HCI/CIN/BV-15-C |
| HCI 15/4a | Read RSSI Value, BR/EDR | HCI/CIN/BV-13-C |
| HCI 15/4c | Read RSSI Value, LE Controller | HCI/CIN/BV-14-C |
| HCI 5/27 OR HCI 5/28 OR HCI 5/29 OR HCI 5/30 | LE Resolving List Management | HCI/CCO/BV-12-C HCI/CCO/BV-13-C HCI/CCO/BV-14-C HCI/CCO/BI-46-C HCI/CCO/BI-47-C HCI/CCO/BI-48-C |
| HCI 7/39 AND HCI 5/27 AND HCI 6/20 | LE Add Device To Resolving List, Scanner | HCI/CCO/BI-50-C |
| HCI 7/39 AND HCI 6/15 AND LL 3/2 | LE Add Device To Resolving List, Advertiser, Connectable | HCI/CCO/BI-69-C |
| HCI 7/39 AND HCI 6/15 AND NOT LL 3/2 AND LL 3/5 | LE Add Device To Resolving List, Advertiser, Non-Connectable | HCI/CCO/BI-70-C |
| HCI 7/23 AND LL 1/3 AND LL 2/2 | Reject Create Connection Command, Random Device Address | HCI/CCO/BI-51-C |
| HCI 7/23 AND LL 1/3 AND LL 2/4 AND LL 5/3 | Reject Create Connection Command, Resolvable Private Address, Filter Accept List Used or Not Used | HCI/CCO/BI-52-C HCI/CCO/BI-53-C |
| HCI 7/41 AND LL 1/3 AND LL 2/2 | Reject Extended Create Connection Command, Random Device Address | HCI/CCO/BI-54-C |
| HCI 7/41 AND LL 1/3 AND LL 2/4 AND LL 5/3 | Reject Extended Create Connection Command, Random Device Address, Filter Accept List Used or Not Used | HCI/CCO/BI-55-C HCI/CCO/BI-56-C |
| HCI 13/10 | LE Set Default PHY Command | HCI/CCO/BV-15-C |

| Item | Feature | Test Case(s) |
| HCI 14/17 AND HCI 14/18 AND HCI 14/19 | LE Add Device To Periodic Advertiser List Command, LE Remove Device From Periodic Advertiser List Command, LE Clear Periodic Advertiser List Command | HCI/CCO/BV-17-C |
| HCI 14/20 | LE Read Periodic Advertiser List Size Command | HCI/CCO/BV-16-C |
| HCI 5/44 | LE Read Transmit Power Command | HCI/CCO/BV-18-C |
| HCI 5/45 | LE Write RF Path Compensation Command | HCI/CCO/BV-19-C |
| HCI 5/46 | LE Read RF Path Compensation Command | HCI/CCO/BV-20-C |
| LL 9/13 AND LL 1/1 | LE Resolving List and Advertising | HCI/CCO/BI-01-C |
| LL 9/13 AND LL 1/2 | LE Resolving List and Scanning | HCI/CCO/BI-02-C |
| LL 9/13 AND LL 1/3 AND HCI 7/23 | LE Resolving List and Create Connection | HCI/CCO/BI-03-C |
| LL 9/13 AND LL 1/3 AND HCI 7/41 | LE Resolving List and Extended Create Connection | HCI/CCO/BI-04-C |
| LL 9/13 AND LL 4/8 | LE Resolving List and Periodic Advertising | HCI/CCO/BI-05-C |
| HCI 7/1 AND NOT LMP 2/1 | Validate Unsupported Packet Types are Not Accepted, Create Connection, 3-slot | HCI/CCO/BI-14-C |
| HCI 7/1 AND NOT LMP 2/2 | Validate Unsupported Packet Types are Not Accepted, Create Connection, 5-slot | HCI/CCO/BI-15-C |
| HCI 7/1 AND CORE 1a/60 | Create Connection, Invalid Address | HCI/CCO/BI-118-C |
| HCI 7/29 AND CORE 1a/60 | Truncated Page, Invalid Address | HCI/CCO/BI-119-C |
| HCI 7/50 | LE Set Default Subrate | HCI/CCO/BI-120-C |
| HCI 13/6 AND NOT LMP 2/1 | Validate Unsupported Packet Types are Not Accepted, Change Connection Packet Type, 3- slot | HCI/CCO/BI-16-C |
| HCI 13/6 AND NOT LMP 2/2 | Validate Unsupported Packet Types are Not Accepted, Change Connection Packet Type, 5- slot | HCI/CCO/BI-17-C |
| HCI 15/8 | LE Read Channel Map | HCI/CCO/BI-43-C |
| HCI 1a/1 AND (NOT HCI 16/47a) AND HCI 16/47b | Error Response for Unsupported Transports on Commands, Read Authenticated Payload Timeout, BR/EDR | HCI/CCO/BI-18-C |
| HCI 1a/4 AND HCI 16/47a AND (NOT HCI 16/47b) | Error Response for Unsupported Transports on Commands, Read Authenticated Payload Timeout, LE | HCI/CCO/BI-19-C |
| HCI 1a/1 AND (NOT HCI 15/3a) AND HCI 15/3b | Error Response for Unsupported Transports on Commands, Read Link Quality, BR/EDR | HCI/CCO/BI-20-C |
| HCI 1a/3 AND HCI 15/3a AND (NOT HCI 15/3b) | Error Response for Unsupported Transports on Commands, Read Link Quality, AMP | HCI/CCO/BI-21-C |

| Item | Feature | Test Case(s) |
| HCI 1a/1 AND (NOT HCI 13/1a) AND HCI 13/1b | Error Response for Unsupported Transports on Commands, Read Link Supervision Timeout, BR/EDR | HCI/CCO/BI-22-C |
| HCI 1a/1 AND (NOT HCI 8/8a) AND HCI 8/8b | Error Response for Unsupported Transports on Commands, Read Remote Version Information, BR/EDR | HCI/CCO/BI-23-C |
| HCI 1a/4 AND HCI 8/8a AND (NOT HCI 8/8b) | Error Response for Unsupported Transports on Commands, Read Remote Version Information, LE | HCI/CCO/BI-24-C |
| HCI 1a/1 AND (NOT HCI 15/4a) AND HCI 15/4b AND HCI 15/4c | Error Response for Unsupported Transports on Commands, Read RSSI, BR/EDR | HCI/CCO/BI-25-C |
| HCI 1a/3 AND HCI 15/4a AND (NOT HCI 15/4b) AND HCI 15/4c | Error Response for Unsupported Transports on Commands, Read RSSI, AMP | HCI/CCO/BI-26-C |
| HCI 1a/4 AND HCI 15/4a AND HCI 15/4b AND (NOT HCI 15/4c) | Error Response for Unsupported Transports on Commands, Read RSSI, LE | HCI/CCO/BI-27-C |
| HCI 1a/1 AND (NOT HCI 15/2b) AND HCI 15/2c | Error Response for Unsupported Transports on Commands, Read Transmit Power Level, BR/EDR | HCI/CCO/BI-28-C |
| HCI 1a/4 AND HCI 15/2b AND (NOT HCI 15/2c) | Error Response for Unsupported Transports on Commands, Read Transmit Power Level, LE | HCI/CCO/BI-29-C |
| HCI 1a/1 AND (NOT HCI 16/48a) AND HCI 16/48b | Error Response for Unsupported Transports on Commands, Write Authenticated Payload Timeout, BR/EDR | HCI/CCO/BI-30-C |
| HCI 1a/4 AND HCI 16/48a AND (NOT HCI 16/48b) | Error Response for Unsupported Transports on Commands, Write Authenticated Payload Timeout, LE | HCI/CCO/BI-31-C |
| HCI 1a/1 AND (NOT HCI 13/2a) AND HCI 13/2b | Error Response for Unsupported Transports on Commands, Write Link Supervision Timeout, BR/EDR | HCI/CCO/BI-32-C |
| HCI 5/37 AND LL 9/43 | Invalid LE Set Periodic Advertising Data Parameters, Periodic Advertising ADI Supported | HCI/CCO/BI-33-C |
| HCI 5/41 AND NOT LL 9/43 | Invalid LE Set Periodic Advertising Enable Parameters | HCI/CCO/BI-34-C |
| HCI 6/37 AND NOT LL 9/43 | Invalid LE Set Periodic Advertising Receive Enable, Periodic Advertising ADI Not Supported | HCI/CCO/BI-59-C |
| HCI 10/27 AND NOT LL 9/43 | Invalid LE Set Periodic Advertising Sync Transfer Parameters, Periodic Advertising ADI Not Supported | HCI/CCO/BI-60-C |
| HCI 10/28 AND NOT LL 9/43 | Invalid LE Set Default Periodic Advertising Sync Transfer Parameters, Periodic Advertising ADI Not Supported | HCI/CCO/BI-61-C |

| Item | Feature | Test Case(s) |
| HCI 7/50 | Invalid Default Subrate Parameters | HCI/CCO/BI-37-C |
| HCI 7/51 | Invalid Subrate Requests | HCI/CCO/BI-36-C |
| HCI 10/20 AND LL 9/45 | Invalid LE Connection CTE Request Enable Parameters | HCI/CCO/BI-38-C |
| HCI 16/48b AND LL 9/45 | Invalid Write Authenticated Payload Timeout Parameters | HCI/CCO/BI-39-C |
| HCI 5/66 | Configure Data Path | HCI/CCO/BI-42-C |
| HCI 20/5 AND NOT LL 9/31 AND NOT LL 9/32 | Reject Setting Host Controlled FeatureSet Bit, Unsupported Feature on Controller, Connected Isochronous Stream | HCI/CCO/BI-44-C |
| HCI 20/5 AND NOT LL 9/45 | Reject Setting Host Controlled FeatureSet Bit, Unsupported Feature on Controller, Connection Subrating | HCI/CCO/BI-45-C |
| HCI 20/5 AND NOT LL 9/48 | Reject Setting Host Controlled FeatureSet Bit, Unsupported Feature on Controller, Advertising Coding Selection | HCI/CCO/BI-121-C |
| HCI 20/5 AND NOT LL 9/56 | Reject Setting Host Controlled FeatureSet Bit, Unsupported Feature on Controller, Channel Sounding | HCI/CCO/BI-122-C |
| HCI 20/5 AND LL 5/1 AND LL 9/60 | LE Set Host Feature, During Connection, Initiator | HCI/CSE/BV-08-C |
| HCI 20/5 AND LL 3/1 AND LL 9/60 | LE Set Host Feature, During Connection, Advertiser | HCI/CSE/BV-09-C |
| HCI 15/5 | Read Clock Offset, Peripheral | HCI/CCO/BV-22-C |
| HCI 4/13 AND HCI 5/54 AND (LL 9/31 OR LL 9/32) | LE Setup ISO Data Path, CIS | HCI/CCO/BI-57-C |
| HCI 4/13 AND HCI 5/54 AND LL 9/33 | LE Setup ISO Data Path, BIS, Isochronous Broadcaster | HCI/CCO/BI-58-C |
| HCI 5/54 AND LL 9/34 AND HCI 4/13 | LE Setup ISO Data Path, BIS, Synchronized Receiver | HCI/CCO/BI-62-C |
| HCI 5/34a AND LL 9/9 AND NOT LL 9/48 | LE Set Extended Advertising Parameters, Advertising Coding Selection not supported | HCI/CCO/BV-23-C |
| HCI 7/41a | LE Extended Create Connection [v2] | HCI/CCO/BI-63-C |
| HCI 5/35 | LE Set Periodic Advertising Parameters [v1] | HCI/CCO/BI-64-C |
| HCI 5/35a | LE Set Periodic Advertising Parameters [v2] | HCI/CCO/BI-65-C |
| HCI 6/51 | LE Set Periodic Advertising Response Data | HCI/CCO/BI-66-C HCI/DDI/BI-73-C |
| HCI 5/69 | LE Set Periodic Advertising Subevent Data | HCI/DDI/BI-71-C HCI/DDI/BI-72-C |
| HCI 5/69 AND CORE 1b/54 | LE Set Periodic Advertising Subevent Data, v5.4 or earlier | HCI/CCO/BI-67-C |
| HCI 5/69 AND CORE 1a/60 | LE Set Periodic Advertising Subevent Data, v6.0 or later | HCI/CCO/BI-124-C |
| HCI 6/50 | LE Set Periodic Sync Subevent | HCI/CCO/BI-68-C |

| Item | Feature | Test Case(s) |
| LL 9/52 | Monitoring Advertising | HCI/CCO/BV-24-C HCI/CCO/BI-71-C |
| HCI 13/15 | LE Frame Space Update | HCI/CCO/BI-75-C |
| HCI 13/15 AND NOT LL 9/7 | LE Frame Space Update, LE 2M PHY | HCI/CCO/BI-76-C |
| HCI 13/15 AND NOT LL 9/9 | LE Frame Space Update, LE Coded PHY | HCI/CCO/BI-77-C |
| HCI 13/15 AND NOT (LL 9/31 OR LL 9/32) | LE Frame Space Update, CIS not supported | HCI/CCO/BI-78-C |
| LL 9/56 | Channel Sounding Commands, Channel Sounding Host Support Bit Not Set | HCI/CCO/BI-107-C |
| HCI 21/1 AND LL 13/4 AND NOT LL 13/5 | LE CS Read Local Supported Capabilities, RTT Access Address, 10 ns | HCI/CCO/BI-128-C |
| HCI 21/1a AND LL 13/4 AND NOT LL 13/5 AND LL 13/10 | LE CS Read Local Supported Capabilities, RTT Access Address, 10 ns, LE 2M PHY | HCI/CCO/BI-156-C |
| HCI 21/1 AND NOT LL 13/4 AND LL 13/5 | LE CS Read Local Supported Capabilities, RTT Access Address | HCI/CCO/BI-79-C |
| HCI 21/1 AND LL 13/6 AND NOT LL 13/7 | LE CS Read Local Supported Capabilities, RTT Sounding, 10 ns | HCI/CCO/BI-130-C |
| HCI 21/1a AND LL 13/6 AND NOT LL 13/7 AND LL 13/10 | LE CS Read Local Supported Capabilities, RTT Sounding, 10 ns, LE 2M PHY | HCI/CCO/BI-158-C |
| HCI 21/1 AND NOT (LL 13/6 OR LL 13/7) | LE CS Read Local Supported Capabilities, RTT Sounding, Unsupported | HCI/CCO/BI-80-C |
| HCI 21/1 AND LL 13/7 AND NOT LL 13/6 | LE CS Read Local Supported Capabilities, RTT Sounding, 150 ns | HCI/CCO/BI-129-C |
| HCI 21/1a AND LL 13/7 AND NOT LL 13/6 AND LL 13/10 | LE CS Read Local Supported Capabilities, RTT Sounding, 150 ns, LE 2M PHY | HCI/CCO/BI-157-C |
| HCI 21/1 AND LL 13/8 AND NOT LL 13/9 | LE CS Read Local Supported Capabilities, RTT Random Sequence, 10 ns | HCI/CCO/BI-132-C |
| HCI 21/1a AND LL 13/8 AND NOT LL 13/9 AND LL 13/10 | LE CS Read Local Supported Capabilities, RTT Random Sequence, 10 ns, LE 2M PHY | HCI/CCO/BI-160-C |
| HCI 21/1 AND NOT (LL 13/8 OR LL 13/9) | LE CS Read Local Supported Capabilities, RTT Random Sequence, Unsupported | HCI/CCO/BI-81-C |

| Item | Feature | Test Case(s) |
| HCI 21/1 AND LL 13/9 AND NOT LL 13/8 | LE CS Read Local Supported Capabilities, RTT Random Sequence, 150 ns | HCI/CCO/BI-131-C |
| HCI 21/1a AND LL 13/9 AND NOT LL 13/8 AND LL 13/10 | LE CS Read Local Supported Capabilities, RTT Random Sequence, 150 ns, LE 2M PHY | HCI/CCO/BI-159-C |
| HCI 21/2 | LE CS Read Remote Supported Capabilities | HCI/CCO/BV-26-C HCI/CCO/BI-98-C |
| HCI 21/2 AND LL 1/5 | LE CS Read Remote Supported Capabilities, Central | HCI/CCO/BI-108-C |
| HCI 21/2 AND LL 1/4 | LE CS Read Remote Supported Capabilities, Peripheral | HCI/CCO/BI-109-C |
| HCI 21/4 | LE CS Security Enable | HCI/CCO/BI-99-C |
| HCI 21/4 AND LL 1/5 | LE CS Security Enable, Central | HCI/CCO/BI-82-C HCI/CCO/BI-148-C |
| HCI 21/4 AND LL 1/4 | LE CS Security Enable, Peripheral | HCI/CCO/BI-83-C |
| HCI 21/5 AND LL 1/7 | LE CS Set Default Settings, Initiator | HCI/CCO/BI-84-C |
| HCI 21/5 AND LL 1/8 | LE CS Set Default Settings, Reflector | HCI/CCO/BI-85-C |
| HCI 21/5 AND NOT LL 1/7 | LE CS Set Default Settings, Initiator Not Supported | HCI/CCO/BI-86-C |
| HCI 21/5 AND NOT LL 1/8 | LE CS Set Default Settings, Reflector Not Supported | HCI/CCO/BI-87-C |
| HCI 21/5 | LE CS Set Default Settings | HCI/CCO/BI-88-C HCI/CCO/BI-100-C |
| HCI 21/6 AND LL 1/8 | LE CS Read Remote FAE Table, FAE Not Supported, Reflector Role | HCI/CCO/BI-89-C |
| HCI 21/6 | LE CS Read Remote FAE Table | HCI/CCO/BI-101-C |
| HCI 21/7 AND LL 1/8 | LE CS Write Remote FAE Table, FAE Not Supported, Reflector Role | HCI/CCO/BI-90-C |
| HCI 21/7 | LE CS Write Remote FAE Table | HCI/CCO/BI-102-C |
| HCI 21/8 | LE CS Create Config | HCI/CCO/BI-91-C HCI/CCO/BI-93-C HCI/CCO/BI-103-C HCI/CCO/BI-106-C HCI/CCO/BI-92-C HCI/CCO/BI-112-C |
| HCI 21/9 | LE CS Remove Config | HCI/CCO/BI-94-C HCI/CCO/BI-104-C |
| HCI 21/11 | LE CS Set Procedure Parameters | HCI/CCO/BI-95-C HCI/CCO/BI-96-C HCI/CCO/BI-115-C HCI/CCO/BI-149-C |

| Item | Feature | Test Case(s) |
| HCI 21/11 AND CORE 1b/60 | LE CS Set Procedure Parameters, v6.0 or earlier | HCI/CCO/BI-116-C |
| HCI 21/11 AND CORE 1a/61 | LE CS Set Procedure Parameters, v6.1 or later | HCI/CCO/BI-123-C |
| HCI 21/11 AND NOT LL 9/7 | LE CS Set Procedure Parameters, Unsupported PHY, LE 2M PHY | HCI/CCO/BI-125-C |
| HCI 21/11 AND NOT LL 9/9 | LE CS Set Procedure Parameters, Unsupported PHY, LE Coded PHY | HCI/CCO/BI-126-C HCI/CCO/BI-127-C |
| HCI 21/12 | LE CS Procedure Enable | HCI/CCO/BI-97-C HCI/CCO/BI-105-C |
| HCI 21/10 | LE CS Set Channel Classification | HCI/CCO/BI-110-C HCI/CCO/BI-111-C |
| HCI 21/12 AND LL 1/7 | LE CS Procedure Enable, Initiator | HCI/CCO/BI-113-C |
| HCI 21/12 AND LL 1/8 | LE CS Procedure Enable, Reflector | HCI/CCO/BI-114-C |
| HCI 1a/4 AND LL 9/56 | Channel Sounding | HCI/CCO/BI-117-C |
| HCI 21/23 AND NOT (LL 13/2 OR LL 13/3) | CS Set Security Requirements, CS Tone Unsupported | HCI/CCO/BI-150-C |
| HCI 21/23 AND NOT (LL 13/5 OR LL 13/7 OR LL 13/9) | CS Set Security Requirements, 150 ns RTT accuracy Unsupported | HCI/CCO/BI-151-C |
| HCI 21/23 AND NOT (LL 13/4 OR LL 13/6 OR LL 13/8) | CS Set Security Requirements, 10 ns RTT accuracy Unsupported | HCI/CCO/BI-152-C |
| HCI 21/23 AND NOT (LL 13/4 OR LL 13/5 OR LL 13/6 OR LL 13/7 OR LL 13/8 OR LL 13/9) | CS Set Security Requirements, RTT Unsupported | HCI/CCO/BI-153-C |
| HCI 21/23 AND NOT (CS 2/14a OR CS 2/14b OR CS 2/16) | CS Set Security Requirements, NADM Unsupported | HCI/CCO/BI-154-C |
| HCI 21/23 | CS Set Security Requirements | HCI/CCO/BI-155-C |
| HCI 20/5 AND NOT LL 9/69 | Reject Setting Host Controlled FeatureSet bit, unsupported feature on controller, Connection Rate procedure | HCI/CCO/BI-133-C |
| HCI 7/23 AND CORE 1a/62 | LE Create Connection, v6.2 or later | HCI/CCO/BI-134-C |
| HCI 7/53 AND LL 1/4 | LE Connection Rate Request, Peripheral | HCI/CCO/BI-135-C |
| HCI 7/53 AND LL 6/10a | LE Connection Rate Request, Peripheral, LE Connection Update | HCI/CCO/BI-147-C HCI/CCO/BI-139-C |

| Item | Feature | Test Case(s) |
| HCI 7/53 AND LL 1/5 | LE Connection Rate Request, Central | HCI/CCO/BI-136-C |
| HCI 7/53 | LE Connection Rate Request | HCI/CCO/BI-137-C |
| HCI 7/53 | LE Connection Rate Request, LE 1M | HCI/CCO/BI-143-C |
| HCI 7/53 | LE Connection Rate Request, LE 1M, DLE | HCI/CCO/BI-144-C |
| HCI 7/53 AND LL 9/9 | LE Connection Rate Request, LE Coded | HCI/CCO/BI-145-C |
| HCI 7/53 AND LL 9/9 | LE Connection Rate Request, LE Coded, DLE | HCI/CCO/BI-146-C |
| HCI 7/55 AND LL 1/5 | LE Set Default Rate | HCI/CCO/BI-138-C |
| HCI 7/53 AND HCI 7/51 | LE Connection Rate Request, Subrate Request | HCI/CCO/BI-140-C |
| HCI 7/53 AND LL 9/56 AND LL 1/7 | LE Connection Rate Request, Channel Sounding, Initiator | HCI/CCO/BI-141-C |
| HCI 7/53 AND LL 9/56 AND LL 1/8 | LE Connection Rate Request, Channel Sounding, Reflector | HCI/CCO/BI-142-C |
| HCI 1a/1 AND HCI 6/3 AND HCI 6/4 | Periodic Inquiry Mode | HCI/DDI/BV-01-C |
| HCI 1a/1 AND HCI 6/9 AND HCI 6/10 | Inquiry Mode Command | HCI/DDI/BV-02-C |
| LL 1/1 AND LL 3/2 AND HCI 1a/4 AND HCI 6/15 AND HCI 6/16 | LE Set Advertising Enable Command | HCI/DDI/BV-03-C |
| LL 1/1 AND LL 2/5 AND HCI 1a/4 AND HCI 6/15 AND HCI 6/16 | LE Set Advertising Enable Command, RPA | HCI/DDI/BI-06-C |
| LL 1/2 AND HCI 1a/4 AND HCI 6/20 | LE Set Scan Enable Command | HCI/DDI/BV-04-C |
| LL 1/2 AND LL 2/5 AND HCI 1a/4 AND HCI 6/20 | LE Set Scan Enable Command | HCI/DDI/BI-07-C |
| LL 3/9 AND LL 2/2 AND HCI 5/40 | LE Set Extended Advertising Enable Command, Random Address | HCI/DDI/BI-08-C |
| LL 3/9 AND LL 2/5 AND HCI 5/40 | LE Set Extended Advertising Enable Command, RPA | HCI/DDI/BI-09-C |
| LL 3/9 AND HCI 5/40 | LE Set Extended Advertising Enable Command | HCI/DDI/BI-12-C |
| LL 3/10 AND HCI 5/41 | LE Set Periodic Advertising Enable Command | HCI/DDI/BI-13-C HCI/DDI/BV-07-C |
| LL 1/2 AND (LL 2/2 OR LL 2/5) AND HCI 1a/4 AND HCI 6/28 | LE Set Extended Scan Enable Command | HCI/DDI/BI-11-C |

| Item | Feature | Test Case(s) |
| LL 1/2 AND HCI 1a/4 AND HCI 6/27 AND HCI 6/28 | LE Set Extended Scan Enable Command - Default Parameters | HCI/DDI/BV-06-C |
| (HCI 1a/1 OR HCI 1a/3) AND HCI 6/24 | Read Extended Inquiry Length Command | HCI/DDI/BV-05-C |
| HCI 5/34 AND LL 1/1 | LE Set Extended Advertising Parameters Command | HCI/DDI/BI-01-C |
| HCI 5/34 AND CORE 1a/60 | LE Set Extended Advertising Parameters Command, Decision-Based Advertising Filtering, v6.0 or later | HCI/DDI/BI-69-C |
| HCI 6/16 AND LL 3/9 | LE Set Advertising Parameters Command | HCI/DDI/BI-02-C |
| HCI 6/16 AND LL 3/10 | LE Set Periodic Advertising Parameters Command | HCI/DDI/BI-67-C |
| HCI 6/30 AND NOT HCI 6/37 | Create periodic advertising sync without possibility to enable reports later | HCI/DDI/BI-03-C |
| HCI 6/30 | Reject LE Periodic Advertising Create Sync Command to a synchronized Advertising Set | HCI/DDI/BI-04-C HCI/DDI/BV-12-C |
| LL 4/7 | LE Set Extended Scan Parameters With Unsupported PHY | HCI/DDI/BI-05-C |
| HCI 5/37 | Invalid LE Set Periodic Advertising Data Parameters | HCI/DDI/BI-14-C HCI/DDI/BI-70-C |
| LL 3/10 AND HCI 5/35 | LE Set Periodic Advertising Parameters, Reject, Data Too Long, LE 1M PHY | HCI/DDI/BI-50-C |
| LL 3/10 AND LL 9/9 AND HCI 5/35 | LE Set Periodic Advertising Parameters, Reject, Data Too Long, LE Coded PHY | HCI/DDI/BI-51-C |
| LL 3/10 AND HCI 5/34 AND LL 3/1 | LE Set Extended Advertising Parameters Command, Reject, Anonymous, undirected | HCI/DDI/BI-15-C HCI/DDI/BI-53-C |
| LL 3/10 AND HCI 5/34 AND LL 3/1a | LE Set Extended Advertising Parameters Command, Reject, Anonymous, directed | HCI/DDI/BI-16-C HCI/DDI/BI-54-C |
| LL 3/10 AND HCI 5/34 AND LL 3/2 | LE Set Extended Advertising Parameters Command, Reject, Connectable and scannable undirected | HCI/DDI/BI-17-C HCI/DDI/BI-55-C |
| LL 3/10 AND HCI 5/34 AND LL 3/4 AND LL 3/4a | LE Set Extended Advertising Parameters Command, Reject, Connectable directed (low duty cycle) | HCI/DDI/BI-18-C |
| LL 3/10 AND HCI 5/34 AND LL 3/4 | LE Set Extended Advertising Parameters Command, Reject, Connectable directed | HCI/DDI/BI-19-C HCI/DDI/BI-23-C HCI/DDI/BI-59-C |
| LL 3/10 AND HCI 5/34 AND LL 3/5 | LE Set Extended Advertising Parameters Command, Reject, Scannable undirected | HCI/DDI/BI-20-C HCI/DDI/BI-24-C HCI/DDI/BI-56-C HCI/DDI/BI-60-C |

| Item | Feature | Test Case(s) |
| LL 3/10 AND HCI 5/34 AND LL 3/1 | LE Set Extended Advertising Parameters Command, Reject, Non-connectable and non- scannable, undirected | HCI/DDI/BI-21-C HCI/DDI/BI-57-C |
| LL 3/10 AND HCI 5/34 AND LL 3/4b | LE Set Extended Advertising Parameters Command, Reject, Connectable undirected | HCI/DDI/BI-22-C HCI/DDI/BI-58-C |
| LL 3/10 AND HCI 5/34 AND LL 3/5a | LE Set Extended Advertising Parameters Command, Reject, Scannable directed | HCI/DDI/BI-25-C HCI/DDI/BI-61-C |
| LL 3/10 AND HCI 5/37 | LE Set Periodic Advertising Data, Reject, Data Too Long | HCI/DDI/BI-52-C |
| LL 3/10 AND HCI 5/35 AND LL 3/1 | LE Set Periodic Advertising Parameters Command, Reject, Anonymous, undirected | HCI/DDI/BI-26-C |
| LL 3/10 AND HCI 5/35 AND LL 3/1a | LE Set Periodic Advertising Parameters Command, Reject, Anonymous, directed | HCI/DDI/BI-27-C |
| LL 3/10 AND HCI 5/35 AND LL 3/2 | LE Set Periodic Advertising Parameters Command, Reject, Connectable and scannable undirected | HCI/DDI/BI-28-C |
| LL 3/10 AND HCI 5/35 AND LL 3/4 AND LL 3/4a | LE Set Periodic Advertising Parameters Command, Reject, Connectable directed (low duty cycle) | HCI/DDI/BI-29-C |
| LL 3/10 AND HCI 5/35 AND LL 3/4 | LE Set Periodic Advertising Parameters Command, Reject, Connectable directed | HCI/DDI/BI-30-C HCI/DDI/BI-34-C |
| LL 3/10 AND HCI 5/35 AND LL 3/5 | LE Set Periodic Advertising Parameters Command, Reject, Scannable undirected | HCI/DDI/BI-31-C HCI/DDI/BI-35-C |
| LL 3/10 AND HCI 5/35 AND LL 3/1 | LE Set Periodic Advertising Parameters Command, Reject, Non-connectable and non- scannable, undirected | HCI/DDI/BI-32-C |
| LL 3/10 AND HCI 5/35 AND LL 3/4b | LE Set Periodic Advertising Parameters Command, Reject, Connectable undirected | HCI/DDI/BI-33-C |
| LL 3/10 AND HCI 5/35 AND LL 3/5a | LE Set Periodic Advertising Parameters Command, Reject, Scannable directed | HCI/DDI/BI-36-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/1 | LE Set Periodic Advertising Enable Command, Reject, Anonymous, undirected | HCI/DDI/BI-37-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 | LE Set Periodic Advertising Enable Command, Reject, Anonymous, directed | HCI/DDI/BI-38-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/2 | LE Set Periodic Advertising Enable Command, Reject, Connectable and scannable undirected | HCI/DDI/BI-39-C |

| Item | Feature | Test Case(s) |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/4 AND LL 3/4a | LE Set Periodic Advertising Enable Command, Reject, Connectable directed (low duty cycle) | HCI/DDI/BI-40-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/4 | LE Set Periodic Advertising Enable Command, Reject, Connectable directed | HCI/DDI/BI-41-C HCI/DDI/BI-45-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/5 | LE Set Periodic Advertising Enable Command, Reject, Scannable undirected | HCI/DDI/BI-42-C HCI/DDI/BI-46-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/1 | LE Set Periodic Advertising Enable Command, Reject, Non-connectable and non-scannable, undirected | HCI/DDI/BI-43-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/4b | LE Set Periodic Advertising Enable Command, Reject, Connectable undirected | HCI/DDI/BI-44-C |
| LL 3/10 AND HCI 5/34 AND HCI 5/41 AND LL 3/5a | LE Set Periodic Advertising Enable Command, Reject, Scannable directed | HCI/DDI/BI-47-C |
| HCI 10/40 AND LL 3/9 | LE Set Data Related Address Changes Command | HCI/DDI/BI-48-C |
| HCI 6/30 AND NOT LL 9/43 | LE Periodic Advertising Create Sync Command, Periodic Advertising ADI not supported | HCI/DDI/BI-49-C |
| HCI 5/41 AND LL 9/43 | LE Set Periodic Advertising Enable Parameters, Periodic Advertising ADI Supported | HCI/DDI/BV-09-C |
| HCI 6/30 AND LL 9/43 | LE Periodic Advertising Create Sync Command, Periodic Advertising ADI Supported | HCI/DDI/BV-08-C |
| HCI 5/34 AND HCI 5/36 AND LL 9/9 | LE Set Extended Advertising Parameters, Packet Too Long, LE Coded PHY | HCI/DDI/BI-62-C |
| HCI 5/36 | LE Set Extended Advertising Data, Packet Too Long | HCI/DDI/BI-63-C |
| HCI 5/36 AND LL 9/9 | LE Set Extended Advertising Data, Packet Too Long, LE Coded PHY | HCI/DDI/BI-64-C |
| HCI 5/38 | LE Set Extended Scan Response Data, Packet Too Long | HCI/DDI/BI-65-C |
| HCI 5/38 AND LL 9/9 | LE Set Extended Scan Response Data, Packet Too Long, LE Coded PHY | HCI/DDI/BI-66-C |
| HCI 6/27 AND NOT LL 9/51 AND CORE 1a/60 | LE Set Extended Scan Parameters, Decision- Based Advertising Filtering not supported, v6.0 or later | HCI/DDI/BI-68-C |

| Item | Feature | Test Case(s) |
| HCI 7/41 AND NOT LL 9/51 AND CORE 1a/60 | LE Extended Create Connection, Decision- Based Advertising Filtering not supported, v6.0 or later | HCI/CCO/BI-72-C |
| HCI 5/32a | LE Set Resolvable Private Address Timeout [v2] | HCI/DDI/BI-74-C HCI/DDI/BV-10-C HCI/DDI/BV-11-C |
| HCI 5/70 | LE Set Decision Data | HCI/CCO/BI-73-C |
| HCI 5/71 | LE Set Decision Instructions | HCI/CCO/BI-74-C HCI/CCO/BV-25-C |
| (HCI 1a/1 OR HCI 1a/3) AND HCI 7/33 | Read Extended Page Timeout Command | HCI/CCO/BV-08-C |
| HCI 10/12 | LE Set Data Length Command | HCI/CCO/BV-09-C HCI/CCO/BI-40-C |
| HCI 10/14 | LE Read Suggested Default Data Length Command | HCI/CCO/BV-10-C |
| HCI 10/15 | LE Write Suggested Default Data Length Command | HCI/CCO/BV-11-C |
| (HCI 1a/1 OR HCI 1a/3) AND HCI 14/2 | Set Event Mask Command | HCI/HFC/BV-01-C |
| HCI 1a/1 AND HCI 14/3 | Set Event Filter Command | HCI/HFC/BV-02-C HCI/HFC/BV-05-C HCI/HFC/BV-06-C HCI/HFC/BV-07-C HCI/HFC/BV-08-C HCI/HFC/BV-11-C |
| HCI 1a/1 AND HCI 14/3 AND LMP 2/12 | Set Event Filter Command, SCO | HCI/HFC/BV-09-C HCI/HFC/BV-12-C |
| HCI 1a/1 AND HCI 14/3 AND LMP 2/15 | Set Event Filter Command, eSCO | HCI/HFC/BV-10-C HCI/HFC/BV-13-C |
| HCI 1a/1 AND HCI 16/15 AND (NOT HCI 16/27) | Link Key Commands - IUT does not support SPP | HCI/AEN/BV-01-C |
| HCI 1a/1 AND HCI 16/15 AND HCI 16/27 | Link Key Commands | HCI/AEN/BV-02-C HCI/AEN/BV-03-C HCI/AEN/BV-04-C |
| HCI 16/50 AND HCI 16/52 | LE Read Local P-256 Public Key, LE Read Local P-256 Public Key Complete | HCI/AEN/BV-06-C |
| HCI 16/51 AND HCI 16/53 | LE Generate DHKey, LE Generate DHKey Complete Event | HCI/AEN/BV-07-C |
| HCI 1a/1 AND HCI 16/44 | Read Local OOB Extended Data Command | HCI/AEN/BV-05-C HCI/AEN/BV-09-C |

| Item | Feature | Test Case(s) |
| HCI 16/51 AND HCI 16/53 AND CORE 1b/54 | LE Generate DHKey, Invalid Point, v5.4 and earlier | HCI/AEN/BI-01-C |
| HCI 16/51 AND HCI 16/53 AND CORE 1a/60 | LE Generate DHKey, Invalid Point, v6.0 and later | HCI/AEN/BI-02-C |
| HCI 16/53 AND HCI 16/51a | LE Generate DHKey [v2] | HCI/AEN/BV-08-C |
| HCI 1a/3 AND (HCI 5/11 OR HCI 5/12) | Write Location Data Command/ Read Location Data Command | HCI/CCO/BV-01-C |
| HCI 1a/3 AND HCI 7/20 | Logical Link Cancel Command | HCI/CSE/BV-01-C HCI/CSE/BV-02-C HCI/CSE/BI-03-C HCI/CSE/BI-04-C |
| HCI 1a/3 AND (HCI 7/21 OR HCI 7/22) | Logical Link Accept Timeout | HCI/CSE/BV-05-C |
| HCI 14/8 AND HCI 14/22 | Set Event Mask 2 Command, Data Block Based Flow Control | HCI/HFC/BV-03-C |
| LL 1/2 AND HCI 14/14 | LE Set Event Mask [v1] command - Scanning state | HCI/HFC/BV-04-C |
| LL 1/2 AND HCI 14/14a | LE Set Event Mask [v2] command - Scanning state | HCI/HFC/BV-20-C |
| (NOT LL 1/2) AND LL 1/3 AND HCI 14/14 | LE Set Event Mask [v1] command - Initiating state | HCI/HFC/BV-14-C |
| (NOT LL 1/2) AND LL 1/3 AND HCI 14/14a | LE Set Event Mask [v2] command - Initiating state | HCI/HFC/BV-21-C |
| LL 1/1 AND NOT LL 1/2 AND NOT LL 1/3 AND LL 1/4 AND HCI 14/14 | LE Set Event Mask [v1] command - Advertising state | HCI/HFC/BV-15-C |
| LL 1/1 AND NOT LL 1/2 AND NOT LL 1/3 AND LL 1/4 AND HCI 14/14a | LE Set Event Mask [v2] command - Advertising state | HCI/HFC/BV-22-C |
| LL 1/1 AND NOT LL 1/2 AND NOT LL 1/3 AND NOT LL 1/4 AND HCI 14/14 AND HCI 16/52 | LE Set Event Mask command, LE Read Local P-256 Public Key | HCI/HFC/BV-17-C |

| Item | Feature | Test Case(s) |
| LL 1/1 AND NOT LL 1/2 AND NOT LL 1/3 AND NOT LL 1/4 AND HCI 14/14 AND NOT HCI 16/52 AND HCI 16/53 | LE Set Event Mask command, LE Generate DHKey [v1] | HCI/HFC/BV-18-C |
| LL 1/1 AND NOT LL 1/2 AND NOT LL 1/3 AND NOT LL 1/4 AND LL 3/9 AND HCI 14/14 AND NOT HCI 16/52 AND NOT HCI 16/53 | LE Set Event Mask command, Advertising Set Terminated | HCI/HFC/BV-19-C |
| HCI 14/15 AND HCI 14/16 | Write LE Host Support | HCI/CCO/BV-03-C |
| HCI 1a/1 AND (NOT HCI 1a/4) | LE Not Supported | HCI/CCO/BV-05-C |
| HCI 1a/4 AND (NOT HCI 1a/1) | BR/EDR Not Supported | HCI/CCO/BV-07-C |
| LL 9/25 | Read LE Public Key Validation Feature Bit | HCI/CIN/BV-09-C |
| HCI 7/39 AND LL 1/5 | LE Read Peer Resolvable Address Command - Central | HCI/CM/BV-01-C |
| HCI 7/40 AND LL 1/5 | LE Read Local Resolvable Address Command - Central | HCI/CM/BV-02-C |
| HCI 13/9 | LE Read PHY Command | HCI/CM/BV-03-C |
| LL 2/7 AND LL 2/5 AND HCI 7/38 AND HCI 7/41 | Extended Scanning with Device Privacy, RPA Timeout During Connection Initiation | HCI/CM/BV-04-C |
| HCI 7/39 AND LL 1/4 | LE Read Peer Resolvable Address Command - Peripheral | HCI/CM/BV-05-C |
| HCI 7/40 AND LL 1/4 | LE Read Local Resolvable Address Command - Peripheral | HCI/CM/BV-06-C |
| LL 5/4 AND LL 5/1 | LE Extended Create Connection With Unsupported PHY | HCI/CM/BI-01-C |
| HCI 3/6 | Sleep Clock Accuracy | HCI/CM/BV-07-C |
| HCI 7/23 AND HCI 7/24 | LE Create Connection Cancel Command, LE Create Connection | HCI/CM/BI-02-C |
| HCI 7/24 AND HCI 7/41 | LE Create Connection Cancel Command, LE Extended Create Connection | HCI/CM/BI-03-C |
| HCI 7/23 AND CORE 1a/60 | LE Create Connection, v6.0 or later | HCI/CM/BI-04-C |
| (HCI 7/41 OR HCI 7/41a) AND CORE 1a/60 | LE Extended Create Connection, v6.0 or later | HCI/CM/BI-05-C |

| Item | Feature | Test Case(s) |
| HCI 18/5 AND HCI 18/8 AND HCI 18/9 AND HCI 18/7 AND HCI 18/1 AND HCI 18/3 AND HCI 18/10 | Connectionless Peripheral Broadcast Transmission | HCI/CPB/BV-01-C |
| HCI 18/6 | Delete Reserved LT_ADDR | HCI/CPB/BV-02-C |
| HCI 18/14 | Connectionless Peripheral Broadcast Channel Map Change | HCI/CPB/BV-03-C |
| HCI 18/4 AND HCI 18/11 AND HCI 18/2 AND HCI 18/12 | Connectionless Peripheral Broadcast Reception | HCI/CPB/BV-04-C |
| HCI 18/13 | Connectionless Peripheral Broadcast Timeout | HCI/CPB/BV-05-C |
| HCI 7/29 AND HCI 7/31 | Truncated Page, Truncated Page Complete | HCI/CSE/BV-06-C |
| HCI 7/32 | Page Response Timeout | HCI/CSE/BV-07-C |
| HCI 5/59 | LE Enhanced Read Transmit Power Level Command | HCI/PCL/BV-01-C HCI/PCL/BI-04-C |
| HCI 5/59 AND NOT LL 9/7 | LE Enhanced Read Transmit Power Level Command, LE 2M PHY not supported | HCI/PCL/BI-01-C |
| HCI 5/59 AND NOT LL 9/9 | LE Enhanced Read Transmit Power Level Command, LE Coded PHY not supported | HCI/PCL/BI-02-C HCI/PCL/BI-03-C |
| HCI 8/10 | LE Read Remote Transmit Power Level Command | HCI/PCL/BI-08-C |
| HCI 8/10 AND NOT LL 9/7 | LE Read Remote Transmit Power Level Command, LE 2M PHY not supported | HCI/PCL/BI-05-C |
| HCI 8/10 AND NOT LL 9/9 | LE Read Remote Transmit Power Level Command, LE Coded PHY not supported | HCI/PCL/BI-06-C HCI/PCL/BI-07-C |
| LL 9/37 AND HCI 5/59 | LE Enhanced Read Transmit Power Level Command, Invalid Host Parameters | HCI/CCO/BI-06-C HCI/CCO/BI-07-C |
| LL 9/37 AND HCI 8/10 | LE Read Remote Transmit Power Level Command, Invalid Host Parameters | HCI/CCO/BI-08-C HCI/CCO/BI-09-C |
| LL 9/37 AND HCI 5/60 | LE Set Path Loss Reporting Parameters Command, Invalid Host Parameters | HCI/CCO/BI-10-C |
| LL 9/37 AND HCI 5/61 | LE Set Path Loss Reporting Enable Command, Invalid Host Parameters | HCI/CCO/BI-11-C |
| LL 9/37 AND HCI 5/64 | LE Set Transmit Power Reporting Enable Command, Invalid Host Parameters | HCI/CCO/BI-12-C |
| HCI 5/60 AND HCI 5/61 | LE Path Loss Monitoring, Invalid Parameters | HCI/CCO/BI-13-C |
| LL 9/7 AND LL 9/8 AND LL 9/9 AND LL 9/31 AND CORE 1b/54 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, asymmetric PHYs, Core v5.2 to v5.4 | HCI/CIS/BV-01-C |

| Item | Feature | Test Case(s) |
| LL 9/7 AND (NOT LL 9/8) AND LL 9/9 AND LL 9/31 AND CORE 1b/54 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, symmetric PHYs only, Core v5.2 to 5.4 | HCI/CIS/BV-02-C |
| LL 9/7 AND LL 9/9 AND LL 12/2 | Broadcast Isochronous Stream Using Non- Test Command, Isochronous Broadcaster, all PHYs | HCI/BIS/BV-01-C |
| NOT (LL 9/7 AND LL 9/9) AND LL 9/8 AND LL 9/31 AND CORE 1b/54 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, asymmetric PHYs, Core v5.2 to v5.4 | HCI/CIS/BV-03-C |
| NOT (LL 9/7 AND LL 9/9) AND (NOT LL 9/8) AND LL 9/31 AND CORE 1b/54 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, symmetric PHYs only, Core v5.2 to v5.4 | HCI/CIS/BV-04-C |
| LL 9/7 AND LL 9/8 AND LL 9/9 AND LL 9/31 AND LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, asymmetric PHYs, Unsegmented Framed mode | HCI/CIS/BV-15-C |
| LL 9/7 AND (NOT LL 9/8) AND LL 9/9 AND LL 9/31 AND LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, symmetric PHYs only, Unsegmented Framed mode | HCI/CIS/BV-16-C |
| NOT (LL 9/7 AND LL 9/9) AND LL 9/8 AND LL 9/31 AND LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, asymmetric PHYs, Unsegmented Framed mode | HCI/CIS/BV-17-C |
| NOT (LL 9/7 AND LL 9/9) AND (NOT LL 9/8) AND LL 9/31 AND LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, symmetric PHYs only, Unsegmented Framed mode | HCI/CIS/BV-18-C |
| LL 9/7 AND LL 9/8 AND LL 9/9 AND LL 9/31 AND NOT LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, asymmetric PHYs, Core v6.0 or later, Unsegmented Framed mode not supported | HCI/CIS/BV-19-C |
| LL 9/7 AND (NOT LL 9/8) AND LL 9/9 AND LL 9/31 AND NOT LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, all PHYs, symmetric PHYs only, Core v6.0 or later, Unsegmented Framed mode not supported | HCI/CIS/BV-20-C |
| NOT (LL 9/7 AND LL 9/9) AND LL 9/8 AND LL 9/31 AND NOT LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, asymmetric PHYs, Core v6.0 or later, Unsegmented Framed mode not supported | HCI/CIS/BV-21-C |

| Item | Feature | Test Case(s) |
| NOT (LL 9/7 AND LL 9/9) AND (NOT LL 9/8) AND LL 9/31 AND NOT LL 9/53 AND CORE 1a/60 | Connected Isochronous Stream Using Non- Test Command, Central Initiated, not all PHYs, symmetric PHYs only, Core v6.0 or later, Unsegmented Framed mode not supported | HCI/CIS/BV-22-C |
| NOT (LL 9/7 AND LL 9/9) AND LL 12/2 | Broadcast Isochronous Stream Using Non- Test Command, Isochronous Broadcaster, not all PHYs | HCI/BIS/BV-02-C |
| LL 9/9 AND LL 12/2 | Broadcast Isochronous Stream Using Non- Test Command, Isochronous Broadcaster, LE Coded PHY | HCI/BIS/BV-11-C |
| LL 9/31 | Connected Isochronous Stream, Central | HCI/CIS/BV-05-C HCI/CIS/BV-09-C HCI/CIS/BV-13-C HCI/CIS/BI-01-C HCI/CIS/BI-03-C HCI/CIS/BI-05-C HCI/CIS/BI-10-C HCI/CIS/BI-11-C HCI/CIS/BI-12-C HCI/CIS/BI-13-C HCI/CIS/BI-16-C |
| LL 9/31 AND HCI 16/48b | Connected Isochronous Stream, HCI Read/Write Authenticated Payload Timeout, Central | HCI/CIS/BI-19-C |
| LL 9/31 AND LL 9/32 | Receiving HCI ISO Data Packets with RFU Bits Set, CIS, Peripheral | HCI/CIS/BI-02-C |
| LL 9/31 AND HCI 3/9 | Connected Isochronous Stream Using Test Command, Central Initiated, Time_Offset | HCI/CIS/BV-06-C HCI/CIS/BV-07-C |
| LL 9/31 AND HCI 20/4 | Connected Isochronous Stream, Central | HCI/CIS/BV-11-C |
| LL 9/32 | Connected Isochronous Stream, Peripheral | HCI/CIS/BV-10-C HCI/CIS/BI-04-C HCI/CIS/BI-07-C HCI/CIS/BI-08-C HCI/CIS/BI-09-C |
| LL 9/32 AND HCI 16/48b | Connected Isochronous Stream, HCI Read/Write Authenticated Payload Timeout, Peripheral | HCI/CIS/BI-20-C |
| LL 9/32 AND HCI 3/9 | Connected Isochronous Stream, Invalid LE Read ISO TX Sync Parameters, Peripheral | HCI/CIS/BV-08-C |
| LL 9/32 AND HCI 10/33 AND HCI 10/34 | Invalid LE Accept or Reject CIS Request, Premature Setup ISO Data Path, CIS Peripheral | HCI/CIS/BI-06-C |
| LL 9/32 AND HCI 20/4 | Connected Isochronous Stream, Peripheral | HCI/CIS/BV-12-C |
| LL 1/6 AND LL 9/33 | Broadcast Isochronous Stream Using Non- Test Command, Invalid BIG Parameters | HCI/BIS/BI-06-C |

| Item | Feature | Test Case(s) |
| LL 1/6 AND LL 9/33 AND NOT LL 9/53 | Broadcast Isochronous Stream Using Non- Test Command, Invalid BIG Parameters, Unsegmented Framed mode not supported | HCI/BIS/BI-11-C |
| LL 9/33 AND HCI 3/9 | Broadcast Isochronous Stream Using Test Command, Time_Offset | HCI/BIS/BV-03-C |
| LL 9/34 AND HCI 3/9 | Broadcast Isochronous Stream, Invalid LE Read ISO TX Sync Parameters, Synchronized Receiver | HCI/BIS/BV-04-C |
| LL 11/4 AND LL 9/34 AND HCI 5/55 AND HCI 6/38 | Broadcast Isochronous Stream, Invalid LE BIG Create Sync Parameters and LE Remove ISO Data Path Parameters, Synchronized Receiver | HCI/BIS/BI-08-C |
| LL 9/34 AND HCI 6/38 | Broadcast Isochronous Stream, Invalid LE BIG Create Sync behavior, Synchronized Receiver | HCI/BIS/BI-09-C HCI/BIS/BI-16-C |
| NOT LL 9/46 AND HCI 5/58 | Connected Isochronous Stream, BN > 1 Not Supported | HCI/CIS/BI-14-C |
| NOT LL 9/47 AND HCI 5/58 | Connected Isochronous Stream, FT > 1 Not Supported | HCI/CIS/BI-15-C |
| LL 11/3 | Broadcast Isochronous Stream, Synchronized Receiver, Reject Invalid Commands | HCI/BIS/BI-02-C |
| LL 11/3 AND HCI 16/48b | Broadcast Isochronous Stream, Synchronized Receiver, HCI Read/Write Authenticated Payload Timeout | HCI/BIS/BI-14-C |
| LL 12/2 | HCI ISO Data Packets, BIS | HCI/BIS/BV-05-C HCI/BIS/BI-01-C |
| LL 12/2 AND HCI 16/48b | Broadcast Isochronous Stream, Broadcaster, HCI Read/Write Authenticated Payload Timeout | HCI/BIS/BI-12-C |
| LL 9/34 AND HCI 20/4 | Broadcast Isochronous Stream, Synchronized Receiver | HCI/BIS/BV-06-C HCI/BIS/BV-07-C |
| LL 9/33 AND HCI 3/8 AND HCI 14/12 AND HCI 20/1 | Broadcast Isochronous Stream, Broadcaster | HCI/BIS/BI-07-C |
| LL 9/33 AND HCI 3/8 AND HCI 14/12 AND HCI 20/1 AND HCI 20/4 | Broadcast Isochronous Stream, Broadcaster | HCI/BIS/BV-08-C |
| HCI 3/8 AND HCI 14/12 AND HCI 5/56 AND HCI 20/4 | Sending HCI ISO Data Packets, CIS, Number of Completed Packets Event | HCI/CIS/BV-14-C |
| HCI 5/56 AND NOT LL 9/53 AND CORE 1a/60 | LE Set CIG Parameters, Unsegmented Framed mode not supported | HCI/CIS/BI-18-C |
| HCI 20/1 AND LL 9/33 AND NOT LL 9/53 AND CORE 1a/60 | LE Create BIG, Unsegmented Framed mode not supported | HCI/BIS/BI-10-C |

| Item | Feature | Test Case(s) |
| HCI 20/1 AND LL 12/2 AND LL 9/49 AND NOT LL 12/6 | Broadcast Isochronous Stream not created from PAwR | HCI/BIS/BV-09-C |
| HCI 20/2 AND LL 12/2 AND LL 9/49 AND NOT LL 12/6 | Broadcast Isochronous Stream not created from PAwR, Test Command | HCI/BIS/BV-10-C |
| LMP 2/12 AND LMP 2/15 AND HCI 9/1 | Do Not Establish a SCO Connection When Retransmission is Specified | HCI/SCO/BV-01-C HCI/SCO/BV-02-C |
| LMP 2/12 AND LMP 2/15 AND HCI 9/10 | Do Not Establish a SCO Connection When Retransmission is Specified - Enhanced Setup | HCI/SCO/BV-03-C HCI/SCO/BV-04-C |
| LMP 2/12 AND HCI 9/2 | Accept SCO Connection | HCI/SCO/BV-09-C HCI/SCO/BV-10-C |
| LMP 2/12 AND HCI 9/11 | Enhanced Accept SCO Connection | HCI/SCO/BV-11-C HCI/SCO/BV-12-C |
| LMP 2/12 AND LMP 6/11 AND HCI 9/1 | SCO Connection creation fails when AES- CCM encryption is enabled - setup synchronous command | HCI/SCO/BV-13-C HCI/SCO/BV-14-C |
| LMP 2/12 AND LMP 6/11 AND HCI 9/10 | SCO Connection creation fails when AES- CCM encryption is enabled - enhanced setup synchronous command | HCI/SCO/BV-15-C HCI/SCO/BV-16-C |
| HCI 16/37a AND NOT HCI 16/37c | Event version check, Encryption Change, BR/EDR, [v1] only | HCI/EVV/BV-01-C |
| HCI 16/37c | Event version check, Encryption Change, BR/EDR, [v1] and [v2] | HCI/EVV/BV-02-C |
| HCI 16/37b AND NOT HCI 16/37d AND LL 1/4 | Event version check, Encryption Change, LE, [v1] only, Peripheral | HCI/EVV/BV-03-C |
| HCI 16/37d AND LL 1/4 | Event version check, Encryption Change, LE, [v1] and [v2], Peripheral | HCI/EVV/BV-04-C |
| HCI 16/37b AND NOT HCI 16/37d AND LL 1/5 | Event version check, Encryption Change, LE, [v1] only, Central | HCI/EVV/BV-05-C |
| HCI 16/37d AND LL 1/5 | Event version check, Encryption Change, LE, [v1] and [v2], Central | HCI/EVV/BV-06-C |
| HCI 6/35 AND NOT HCI 6/35a | Event version check, LE Periodic Advertising Sync Established, [v1] only | HCI/EVV/BV-07-C |
| HCI 6/35a | Event version check, LE Periodic Advertising Sync Established, [v1] and [v2] | HCI/EVV/BV-08-C |
| HCI 6/33 AND NOT HCI 6/33a | Event version check, LE Periodic Advertising Report, [v1] only | HCI/EVV/BV-09-C |
| HCI 6/33a | Event version check, LE Periodic Advertising Report, [v1] and [v2] | HCI/EVV/BV-10-C |
| HCI 10/26 AND NOT HCI 10/26a | Event version check, LE Periodic Advertising Sync Transfer Received, [v1] only | HCI/EVV/BV-11-C |

| Item | Feature | Test Case(s) |
| HCI 10/26a | Event version check, LE Periodic Advertising Sync Transfer Received, [v1] and [v2] | HCI/EVV/BV-12-C |
| HCI 7/25 AND NOT HCI 7/38 AND NOT HCI 7/38a AND LL 1/5 | Event version check, LE Connection Complete, Central | HCI/EVV/BV-13-C |
| HCI 7/38 AND NOT HCI 7/38a AND LL 1/5 | Event version check, LE Enhanced Connection Complete, [v1], Central | HCI/EVV/BV-14-C |
| HCI 7/38a AND LL 1/5 | Event version check, LE Enhanced Connection Complete, [v1] and [v2], Central | HCI/EVV/BV-15-C |
| HCI 7/25 AND NOT HCI 7/38 AND NOT HCI 7/38a AND LL 1/4 AND NOT LL 1/5 | Event version check, LE Connection Complete, Peripheral | HCI/EVV/BV-16-C |
| HCI 7/38 AND NOT HCI 7/38a AND LL 1/4 AND NOT LL 1/5 | Event version check, LE Enhanced Connection Complete, [v1], Peripheral | HCI/EVV/BV-17-C |
| HCI 7/38a AND LL 1/4 AND NOT LL 1/5 | Event version check, LE Enhanced Connection Complete, [v1] and [v2], Peripheral | HCI/EVV/BV-18-C |

Table 5.1: Test case mapping

## 6 Appendix MSC

## 6.1 Default settings

## 6.1.1 Authentication and encryption

This default setting will be used for the different authentication and encryption test cases.

Figure 6.1: Authentication and encryption, default settings MSC

## 6.1.2 Device setup, Controller Flow Control, Controller Information, Device Discovery, and Host Flow Control

This default setting will be used for the Device setup, Controller Flow Control, Controller Information, Device Discovery, and Host Flow Control test cases.

Figure 6.2: Device setup, Controller Flow Control, Controller Information, Device Discovery, and Host Flow Control, default settings MSC

## 6.2 Preambles

## 6.2.1 Connection Establishment IUT Central

This Preamble will be used when the IUT will act as Central.

Figure 6.3: Connection Establishment IUT Central preamble MSC

## 6.2.2 Connection Establishment Lower Tester

This Preamble will be used in all cases when the IUT will act as a Peripheral.

Figure 6.4: Connection Establishment Lower Tester preamble MSC

## 7 Revision history and acknowledgments
