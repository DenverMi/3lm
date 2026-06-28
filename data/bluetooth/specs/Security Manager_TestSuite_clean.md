## Security Manager (SM)

## Bluetooth ® Test Suite

- Revision: SM.TS.p30
- Revision Date: 2026-05-05

## 1 Scope

This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Security Manager layer with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers' Bluetooth devices.

## 2 References, definitions, and abbreviations

## 2.1 References

This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [1] and [7].

- [1] Test Strategy and Terminology Overview
- [2] ICS Proforma for Bluetooth Low Energy Security Manager
- [3] Specification of the Bluetooth System, Volume 3 Part A (GAP), Version 4.0 or later
- [4] Specification of the Bluetooth System, Volume 3 Part A (L2CAP), Version 4.0 or later
- [5] Specification of the Bluetooth System, Volume 6 Part B (Link Layer), Version 4.0 or later
- [6] Implementation eXtra Information for Test (IXIT) for Security Manager
- [7] Specification of the Bluetooth System, Volume 3 Part H, Security Manager (SM), Version 4.2 or later
- [8] Erratum 10734: Pairing Updates
- [9] Appropriate Language Mapping Tables document
- [10] Specification of the Bluetooth System, Volume 3 Part H, Security Manager (SM), Version 4.2 or later
- [11] Specification of the Bluetooth System, Volume 3 Part H, Security Manager (SM), Version 6.2 or later

## 2.2 Definitions

In this Bluetooth document, the definitions from [1] and [7] apply.

Certain terms that were identified as inappropriate have been replaced. For a list of the original terms and their replacement terms, see the Appropriate Language Mapping Tables document [9].

## 2.3 Acronyms and abbreviations

In this Bluetooth document, the definitions, acronyms, and abbreviations from [1] and [7] apply.

## 3 Test Suite Structure (TSS)

## 3.1 Test Strategy

The test objectives are to verify the functionality of the Security Manager layer within a Bluetooth Host and enable interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory and optional requirements in the specification and matches these to the support of the IUT as described in the ICS. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test Case Mapping Table (TCMT) evaluates to true.

The test equipment provides an implementation of the Radio Controller and the parts of the Host needed to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT's peer device and interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement similar capabilities to communicate with the test equipment. For some test cases, it is necessary to stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface, a Man Machine Interface (MMI), or another interface supported by the IUT.

This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with catalogued specification requirements that were logically grouped and assessed for testability enabling coverage in defined test purposes.

The Test Suite Structure is a tree with the first level representing the protocol groups.

- Protocol
- -SMP Timeout
- STK Pairing Method
- -Just Works
- -Passkey Entry
- -Out of Band
- Encryption Key Size
- -Signing
- Central Signing
- Peripheral Signing
- Key Distribution and Usage
- -Key Distribution During Bonding
- -Re-encrypt an Encrypted Link with LTK
- Peripheral Initiated Security
- Pairing Methods using LE Secure Connections
- -Just works and Numeric Comparison
- -Passkey Entry
- Out of Band
- Cross Transport Key Derivation

## 3.2 Test groups

The following test groups have been defined:

- Protocol
- STK Pairing Method
- Signing
- Encryption Key Size
- Key Distribution and Usage
- Peripheral Initiated Security
- LE Secure Connections Pairing

## 4 Test cases (TC)

## 4.1 Introduction

## 4.1.1 Test case identification conventions

Test cases are assigned unique identifiers per the conventions in [1]. The convention used here is: &lt;spec abbreviation&gt;/&lt;IUT role&gt;/ &lt;class&gt;/ &lt;feat&gt; /&lt;func&gt;/&lt;subfunc&gt;/&lt;cap&gt;/ &lt;xx&gt;-&lt;nn&gt;-&lt;y&gt; . If the IUT role is omitted from the TCID, then the test case is applicable to both roles.

Table 4.1: SM TC feature naming conventions

| Identifier Abbreviation | Spec Identifier <spec abbreviation> |
| SM | Security Manager |
| Identifier Abbreviation | Role Identifier <IUT role> |
| CEN | Central Role |
| PER | Peripheral Role |
| Identifier Abbreviation | Feature Identifier <feat> |
| EKS | Encryption Key Size |
| JW | Just Works |
| OOB | Out Of Band |
| PIS | Peripheral Initiated Security |
| PKE | Passkey Entry |
| PROT | Protocol |
| SCCT | LE Secure Connections Cross Transport Key Derivation |
| SCJW | LE Secure Connections Numeric Comparison (including Just Works) |
| SCOB | LE Secure Connections Out-of-Band |
| SCPK | LE Secure Connections Passkey Entry |
| SIGN | Signing |

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

## 4.2 Setup preambles

The procedures defined in this section are provided for information, as they are used by test equipment in achieving the Initial Condition in certain tests.

## 4.2.1 Security Manager Channel over L2CAP

- Reference

[5] 2.1 [7] 3.2

- Preamble Procedure

Establish an LE transport connection between the IUT and the Lower Tester.

Establish the Security Manager Channel over L2CAP fixed channel 0x0006 between the IUT and the Lower Tester over the LE transport.

- Notes

For any tests where no role is assigned and both roles are supported, the Lower Tester may assign either role and the test needs to be run only once.

## 4.3 Common Packet Contents

## 4.3.1 Fields and Bits Reserved for Future Use

Unless a specific test states otherwise, all fields within packets and all bits within fields that are described as reserved for future use are set to 0 in packets sent by the Upper and Lower Testers.

## 4.4 Protocol

Verify the correct implementation of the SMP timeout protocol.

## 4.4.1 SMP Timeout

## SM/CEN/PROT/BV-01-C [SMP Time Out -IUT Initiator]

- Test Purpose

Verify that the IUT handles the lack of pairing response after 30 seconds when acting as initiator.

- Reference

[7] 3.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits pairing request.
2. The Lower Tester does not respond to this pairing request.
3. IUT timeout after 30 seconds and the procedure is considered to have failed.
4. The IUT reports the failure to the Upper Tester.
5. After additionally (at least) 10 seconds the Lower Tester responds to the pairing request.
6. The IUT closes the connection before receiving the delayed response or does not respond to it when it is received.
- Expected Outcome

## Pass verdict

The IUT notifies the Upper Tester after the 30 seconds timeout.

The IUT does not respond to a delayed response after the timeout, as there should be no more transactions on the channel. Alternatively, the IUT does not respond to a delayed response after the timeout.

- Notes

After the Upper Tester is alerted, the channel is not used until the link is reconnected.

## SM/PER/PROT/BV-02-C [SMP Time Out -IUT Responder]

- Test Purpose

Verify that the IUT responder disconnects the link if pairing does not follow Pairing Feature Exchange within 30 seconds after receiving Pairing Request command.

- Reference

[7] 3.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.

- Test Procedure
1. The Lower Tester transmits Pairing Request.
2. Perform either alternative 2A or 2B depending on the IUT Pairing Methods support.

Alternative 2A (The IUT supports Pairing Methods):

- 2A.1 The IUT responds with Pairing Response.
- 2A.2 In phase 2, the Lower Tester does not issue the expected Pairing Confirm.
- 2A.3 The IUT times out 30 seconds after issued Pairing Response and reports the failure to the Upper Tester.
- 2A.4 After additionally (at least) 10 seconds, the Lower Tester issues the expected Pairing Confirm.
- 2A.5 The IUT closes the connection before receiving the delayed response or does not respond to it when it is received.
- Alternative 2B (The IUT does not support Pairing Methods):
- 2B.1 The IUT responds with a Pairing Failed Response with Reason set to 'Pairing Not Supported' .
- Expected Outcome

## Pass verdict

Alternative 2A:

The IUT notifies the Upper Tester after the 30 seconds timeout.

The IUT does not respond to a delayed Pairing Confirm after the timeout, as there should be no more transactions on the channel. Alternatively, the IUT does not respond to a delayed response after the timeout.

Alternative 2B:

The IUT fails the Pairing Request with 'Pairing Not Supported'.

## 4.5 STK Pairing Method

Verify the correct implementation of the Just Works, Passkey Entry, and Out of Band pairing methods.

## 4.5.1 Just Works

## SM/CEN/JW/BV-01-C [Just Works IUT Initiator -Success]

- Test Purpose

Verify that the IUT performs the Just Works pairing procedure correctly as Central, initiator when both sides do not require MITM protection.

- Reference

[7] 2.3.5.1, 2.3.5.2, C.1, C.2.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.

- Test Procedure
1. The IUT transmits Pairing Request command with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq Bonding Flags set to '00' and the MITM flag set to '0' and all the reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardDisplay'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq Bonding Flags set to '00', and the MITM flag set to '0' and all the reserved bits are set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing procedure and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the IUT completes successfully.

The IUT can encrypt the link successfully.

## SM/PER/JW/BV-02-C [Just Works IUT Responder -Success]

## · Test Purpose

Verify that the IUT is able to perform the Just Works pairing procedure correctly when acting as Peripheral, responder.

- Reference

[7] 2.3.5.2, 2.4.6, C.1, C.2.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits Pairing Request command with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. MITM flag set to '0' and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated STK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the Central completes successfully.

The Central can encrypt the link successfully.

## SM/PER/JW/BI-03-C [Just Works IUT Responder -Handle AuthReq flag RFU correctly]

- Test Purpose

Verify that the IUT is able to perform the Just Works pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Peripheral, responder.

- Reference

[7] 2.3.5.2, 2.4.6, C.1, C.2.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits Pairing Request command with:
- a. IO Capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. MITM set to '0' and all reserved bits are set to '1'
2. The IUT responds with a Pairing Response command, with:
- a. IO Capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated STK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the Lower Tester completes successfully.

The Lower Tester can encrypt the link successfully.

## SM/CEN/JW/BV-05-C [Just Works, IUT Initiator -Pairing Failed]

- Test Purpose

Verify that the IUT handles Just Works pairing failures.

- Reference

[7] 3.5.5

- Initial Condition
- -The IUT is Central. The Lower Tester is Peripheral.

## · Test Procedure

Figure 4.1: SM/CEN/JW/BV-05-C [Just Works, IUT Initiator -Pairing Failed] MSC

1. Run preamble to reestablish Initial Condition.
2. The IUT transmits Pairing Request command with:
- a. IO capability is set to any IO capability.
- b. OOB data flag is set to 0x00 (OOB Authentication data not present).
- c. All reserved bits are set to '0' .
3. The Lower Tester responds with a Pairing Failed command with the reason code specified in Table 4.2.
4. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Repeat Steps 1 -4 for each round in Table 4.2.

Table 4.2: Just Works, IUT Initiator -Pairing Failed rounds

| Round | Reason Code |
| 1 | '0x08' (Unspecified Reason) |
| 2 | '0x05' (Pairing Not Supported) |
| 3 | '0x09' (Repeated Attempts) |
| 4 | '0x10' (Busy) |

- Expected Outcome

## Pass verdict

For each pairing failure, the IUT detects the failures reported by the responder and responds correctly to the Lower Tester.

For each pairing failure, the IUT aborts the pairing process and reports the failure to the Upper Tester.

## SM/CEN/JW/BI-04-C [Just Works IUT Initiator -Handle AuthReq flag RFU correctly]

## · Test Purpose

Verify that the IUT is able to perform the Just Works pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Central, initiator.

- Reference

[7] 2.3.5.2, 2.4.6, C.1, C.2.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO Capability set to any IO Capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'. For the purposes of this test, the Secure Connections bit and the Keypress bits in the AuthReq bonding flag set by the IUT are ignored by the Lower Tester.
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO Capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags' and the MITM flag set to '0' and all reserved bits are set to '1'. The SC and Keypress bits in the AuthReq bonding flag are set to 0 by the Lower Tester for this test.
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated STK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the IUT completes successfully.

The link is encrypted successfully.

## SM/CEN/JW/BI-01-C [Just Works, IUT Initiator -Failure]

- Test Purpose

Verify that the IUT handles Just Works pairing failure as initiator correctly.

- Reference

[7] 2.3.5.1, 2.3.5.2, C.5.7

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability is set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'

2. The Lower Tester responds with a Pairing Response command with:
- a. IO capability set to ' NoInputNoOutput '
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq Bonding Flags set to '01' and the MITM flag set to '0' and all reserved bits are set to '0'
3. During phase 2 of the pairing procedure, the Lower Tester transmits a Pairing Confirm command with an incorrect LP\_CONFIRM\_S value.
4. The IUT transmits a Pairing Failed command with Reason set to 'Confirm Value Failed' after receiving the LP\_RAND\_R and detecting the LP\_CONFIRM\_S is incorrect.
5. The Lower Tester disconnects the link.
- Expected Outcome

## Pass verdict

The IUT detects the incorrect confirm values and responds to the Lower Tester accordingly.

## SM/PER/JW/BI-02-C [Just Works, IUT Responder -Failure]

- Test Purpose

Verify that the IUT handles Just Works pairing failure as responder correctly.

- Reference

[7] 2.3.5.1, 2.3.5.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits a Pairing Request command with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '01', and the MITM flag set to '0' and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'
3. During phase 2 of the Just Works pairing procedure, the Lower Tester transmits a Pairing Confirm command with an incorrect LP\_CONFIRM\_I Value.
4. The IUT transmits a Pairing Failed command with Reason set to 'Confirm Value Failed' after receiving the LP\_RAND\_I and detecting the LP\_CONFIRM\_I is incorrect.
- Expected Outcome

## Pass verdict

The IUT detects the incorrect confirm value responds correctly to the Lower Tester.

## SM/CEN/JW/BI-06-C [Just Works IUT Initiator -Abort when LP\_CONFIRM\_R = LP\_CONFIRM\_I]

- Test Purpose

Verify that the IUT aborts the Just Works pairing procedure during Phase 2 when the Responder sends an LP\_CONFIRM\_R = LP\_CONFIRM\_I.

- Reference

[7] 2.3.5.5

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits the Pairing Request command with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq Bonding Flags set to '00' and the MITM flag set to '0' and all the reserved bits set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to ' NoInputNoOutput '
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq Bonding Flags set to '00', and the MITM flag set to '0' and all the reserved bits set to '0'
3. The IUT and the Lower Tester perform Phase 2 of the Just Works pairing procedure. The Lower Tester sends LP\_CONFIRM\_R equal to the LP\_CONFIRM\_I received from the IUT.
4. The IUT may send the LP\_RAND\_I to the Lower Tester. If it does, then the Lower Tester replies with an LP\_RAND\_R equal to LP\_RAND\_I.
5. The pairing process is aborted. The IUT reports the failure to the Upper Tester with the reason code 'Confirm Value Failed'.
- Expected Outcome

## Pass verdict

In S tep 5, the IUT aborts the pairing process and returns the 'Confirm Value Failed' reason code.

## 4.5.2 Passkey Entry (PKE)

## SM/CEN/PKE/BV-01-C [Passkey Entry, IUT Initiator -Success]

- Test Purpose

Verify that the IUT performs the Passkey Entry pairing procedure correctly as initiator.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.

- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly '
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '00', and the MITM flag set to '1' and all reserved bits are set to '0'
3. During the phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester prompts user to enter the 6-digit passkey. If the IUT IO capabilities are 'KeyboardOnly' the passkey is not displayed and both the IUT and the Lower Tester enter the same 6-digit passkey.
4. The IUT and the Lower Tester use the same 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the Passkey Entry pairing procedure and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

## SM/PER/PKE/BV-02-C [Passkey Entry, IUT Responder -Success]

- Test Purpose

Verify that the IUT performs the Passkey Entry pairing procedure correctly as responder.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to ' Keyboard Display'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags' , and the MITM flag set to '1' and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly ' or ' KeyboardDisplay ' or 'DisplayYesNo' or 'DisplayOnly'
- b. OOB data flag set to 0x00
- c. All reserved bits are set to '0'
3. During the phase 2 passkey pairing process, the Lower Tester displays the 6-digit passkey while the IUT prompts user to enter the 6-digit passkey. If the IO capabilities of the IUT are 'DisplayYesNo' or 'DisplayOnly' the IUT displays the 6 -digit passkey while the Lower Tester enters the 6-digit passkey.

4. The IUT and the Lower Tester use the same pre-defined 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The Central can encrypt the link successfully.

## SM/CEN/PKE/BV-04-C [Passkey Entry, IUT Initiator -Results in Unauthenticated Success]

- Test Purpose

Verify that the IUT performs the Passkey Entry pairing procedure correctly as initiator and pairing is successful if the Lower Tester only supports IO capabilities resulting in an Unauthenticated key.

- Reference

[7] 2.3.5.1, C.2.1.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags', and the MITM flag set to '0' and all reserved bits set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated STK.
- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

## SM/CEN/PKE/BI-01-C [Passkey Entry, IUT Initiator -Failure on Responder Side]

- Test Purpose

Verify that the IUT handles the invalid Passkey Entry pairing procedure correctly as initiator.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00 and all the reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly '
- b. OOB data flag set to 0x0 0 and MITM bit set to '1'
3. During the phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester enters a different 6-digit passkey. If the IUT IO capabilities are 'KeyboardOnly' then both the IUT and the Lower Tester enter different passkeys.
4. The IUT and the Lower Tester perform phase 2 of the LE pairing.
5. The Lower Tester transmits 'Pairing Random' ( LP\_RAND\_R) command even though the passkey entry was incorrect.
6. The IUT responds with 'Pairing Failed' command.
- Expected Outcome

## Pass verdict

The IUT detects that the 'Pairing Random' value from the Lower T ester is incorrect and sends 'Pairing Failed' command to the Lower Tester.

## SM/CEN/PKE/BI-02-C [Passkey Entry, IUT Initiator -Interrupted passkey entry by Responder Side]

- Test Purpose

Verify that the IUT handles the interrupted passkey entry by the responder.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00 and all reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly '
- b. OOB data flag set to 0x0 0 and MITM bit set to '1' and all the reserved bits are set to '0'
3. During the phase 2 pairing, if IO capability is set to 'DisplayOnly', 'DisplayYesNo' or 'KeyboardDisplay' the IUT displays the 6 -digit passkey. If the IUT IO capabilities are

'KeyboardOnly' the passkey is not displayed and both the IUT and the Lower Tester enter the same 6-digit passkey.

4. Emulating interrupted passkey entry the Lower Tester issues a Pairing Failed command with reason code set to '0x01' (Passkey Entry Failed).
5. The pairing process is aborted. The IUT reports the failure to the Upper Tester.
- Expected Outcome

## Pass verdict

The IUT detects the Pairing Failed from the Lower Tester and reports the failure to the Upper Tester.

## SM/PER/PKE/BI-03-C [Passkey Entry, IUT Responder -Failure on Initiator Side]

- Test Purpose

Verify that the IUT handles the invalid passkey entry pairing procedure correctly as responder.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 and MITM bit set to '1' and all the reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to 'DisplayOnly' or ' DisplayYesNo ' or 'KeyboardDisplay' or 'KeyboardOnly'
- b. OOB data flag set to 0x00 and all the reserved bits are set to '0'
3. The IUT and the Lower Tester use different 6-digit passkey.
4. During the phase 2 pairing, the IUT displays 6-digit passkey while the Lower Tester enters different 6-digit passkey. If the IUT IO capabilities are 'KeyboardOnly' the passkey is not displayed and the IUT and the Lower Tester enter different 6-digit passkeys.
5. The IUT and the Lower Tester perform phase 2 of the LE pairing.
- Expected Outcome

## Pass verdict

The IUT detects the ' Pairing C onfirm' value from the Lower T ester is incorrect and sends ' Pairing Failed ' command to the Lower Tester.

## SM/CEN/PKE/BV-05-C [Passkey Entry, IUT Initiator -Verify Random Passkeys]

- Test Purpose

Verify that the IUT generates random passkeys as initiator.

- Reference

[10] 2.3.5.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure

Repeat the test procedure three times.

1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '00', and the MITM flag set to '1' and all reserved bits set to '0'
3. During the phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester prompts the user to enter the 6digit passkey. If the IUT IO capabilities are 'KeyboardOnly' , the passkey is not displayed and both the IUT and the Lower Tester enter the same 6-digit passkey.
4. The IUT and the Lower Tester use the same 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the Passkey Entry pairing procedure and establish an encrypted link with the key generated in phase 2.
6. The IUT and the Lower Tester disconnect the ACL connection.
7. The Lower Tester removes bonding information with the IUT.
- Expected Outcome

## Pass verdict

The Lower Tester verifies that the IUT generates unique keys.

## SM/CEN/PKE/BI-03-C [Passkey Entry, IUT Initiator -Abort when LP\_CONFIRM\_R = LP\_CONFIRM\_I]

- Test Purpose

Verify that the IUT performs the Passkey Entry pairing procedure correctly as initiator. The IUT fails the pairing procedure when LP\_CONFIRM\_R = LP\_CONFIRM\_I.

- Reference

[7] 2.3.5.5

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)

2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '00', and the MITM flag set to '1' and all reserved bits set to '0'
3. During the Phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester prompts the user to enter the 6digit passkey. If the IUT IO capabilities are 'KeyboardOnly' , then the passkey is not displayed and both the IUT and the Lower Tester enter the same 6-digit passkey.
4. The IUT and the Lower Tester use the same 6-digit passkey.
5. The IUT and the Lower Tester perform Phase 2 of the Passkey Entry pairing procedure. The Lower Tester sends LP\_CONFIRM\_R equal to the LP\_CONFIRM\_I received from the IUT.
6. The IUT may send the LP\_RAND\_I to the Lower Tester. If it does, then the Lower Tester replies with an LP\_RAND\_R equal to LP\_RAND\_I.
7. The pairing process is aborted. The IUT reports the failure to the Upper Tester with the reason code 'Confirm Value Failed' .
- Expected Outcome

## Pass verdict

In S tep 7, the IUT aborts the pairing process and returns the 'Confirm Value Failed' reason code.

## 4.5.2.1 Passkey Entry, IUT Responder -Lower Tester has insufficient security for Passkey Entry

- Test Purpose

Verify that the IUT that supports the Passkey Entry pairing procedure as responder correctly handles an initiator with insufficient security to result in an Authenticated key, yielding an unauthenticated key.

- Reference

[7] 2.3.5.1, C.2.1.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Case Configuration

Table 4.3: Passkey Entry, IUT Responder -Lower Tester has insufficient security for Passkey Entry test cases

| Test Case | MITM |
| SM/PER/PKE/BV-05-C [Passkey Entry, IUT Responder - Lower Tester has insufficient security for Passkey Entry, v6.1 or earlier] | 1 |
| SM/PER/PKE/BV-06-C [Passkey Entry, IUT Responder - Lower Tester has insufficient security for Passkey Entry, v6.2 or later] | 0 |

## · Test Procedure

1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '00', and the MITM flag set to '0' and all reserved bits are set to '0'

2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly' or 'KeyboardDisplay' or 'DisplayYesNo' or 'DisplayOnly'
- b. OOB data flag set to 0x00 and the MITM flag set to the value in Table 4.3 and all reserved bits are set to '0'
- c. Alternatively, the IUT may respond with Pairing Failed command with reason code set to 'Authentication Requirements'.
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated STK.
- Expected Outcome

## Pass verdict

In Step 2b, the IUT sets the MITM flag as specified in Table 4.3.

The Central can encrypt the link successfully.

ALT: The IUT responds with Pairing Failed command with reason code set to 'Authentication Requirements'.

## 4.5.3 Out of Band (OOB)

## 4.5.3.1 IUT Initiator -Both sides have OOB data -Success

- Test Purpose

Verify that the IUT performs the OOB pairing procedure correctly as initiator.

- Reference

[7] 2.3.5.4, C.2.1.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Case Configuration

Table 4.4: IUT Initiator -Both sides have OOB data -Success test cases

| Test Case | Random Key Requirement |
| SM/CEN/OOB/BV-01-C [IUT Initiator - Both sides have OOB data - Success, v6.2 and earlier] | May be repeated |
| SM/CEN/OOB/BV-10-C [IUT Initiator - Both sides have OOB data - Success, v6.3 and later] | Unique |

## · Test Procedure

Repeat the test procedure 5 times.

1. The IUT transmits a Pairing Request command with OOB data flag set to 0x01.
2. The Lower Tester responds with a Pairing Response command with OOB data flag set to 0x01.
3. The IUT and the Lower Tester use the same 128-bit value as OOB data.
4. The IUT and the Lower Tester perform phase 2 of the pairing process and establish an encrypted link with the key generated in phase 2.

- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

If specified in Table 4.6, the random number sent by the IUT in Step 4 is always unique.

- Notes

OOB data are exchanged out of band.

## 4.5.3.2 IUT Responder -Both sides have OOB data -Success

- Test Purpose

Verify that the IUT performs the OOB pairing procedure correctly as responder.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Case Configuration
- Test Procedure

Table 4.5: IUT Responder -Both sides have OOB data -Success test cases

| Test Case | Random Key Requirement |
| SM/PER/OOB/BV-02-C [IUT Responder - Both sides have OOB data - Success, v6.2 and earlier] | May be repeated |
| SM/PER/OOB/BV-11-C [IUT Responder - Both sides have OOB data - Success, v6.3 and later] | Unique |

Repeat the test procedure 5 times.

1. The Lower Tester initiates a Pairing Request command with OOB data flag set to 0x01.
2. The IUT responds with a Pairing Response command with OOB data flag set to 0x01.
3. The IUT and the Lower Tester use the same 128 bit value as OOB data.
4. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
- Test Condition

The IUT and the Lower Tester use the same OOB data values in this test case.

- Expected Outcome

## Pass verdict

The Central can encrypt the link successfully.

If specified in Table 4.5, the random number sent by the IUT in Step 4 is always unique.

## SM/CEN/OOB/BV-03-C [IUT Initiator -Only IUT has OOB data -Success]

- Test Purpose

Verify that the IUT performs pairing correctly as initiator if the responder does not have OOB data.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x01
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly '
- b. OOB data flag set to 0x0 0 and MITM bit set to '1'
3. The IUT generates a random 6-digit passkey between 000,000 and 999,999.
4. During the phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester enters the same 6-digit passkey. If the IUT IO capabilities are 'KeyboardOnly' the passkey is not displayed and both the IUT and the Lower Tester enter the same 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

## SM/PER/OOB/BV-04-C [IUT Responder -Only IUT has OOB data -Success]

- Test Purpose

Verify that the IUT performs the pairing procedure correctly as responder if only the IUT has OOB data.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to ' Keyboard Display'
- b. OOB data flag set to 0x00 and MITM bit set to '1'

2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly ' or 'KeyboardDisplay' or 'DisplayOnly' or 'DisplayYesNo'
- b. OOB data flag set to 0x0 1 and MITM bit set to '1'
3. The Lower Tester has a pre-defined 6-digit passkey.
4. During the phase 2 pairing, the Lower Tester displays the 6-digit passkey while the user of the IUT enters the same 6-digit passkey. If the IO capabilities of the IUT are 'DisplayYesNo' or 'DisplayOnly' the IUT displays the 6 -digit passkey while the Lower Tester enters the 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The Central can encrypt the link successfully.

## SM/CEN/OOB/BV-05-C [IUT Initiator -Only Lower Tester has OOB data -Success]

- Test Purpose

Verify that the IUT performs the OOB pairing procedure correctly as initiator if only the Lower Tester has OOB data.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo', or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly '
- b. OOB data flag set to 0x0 1 and MITM bit set to '1'
3. The IUT generates a random pre-defined 6-digit passkey between 000,000 and 999,999 and begins phase 2 pairing.
4. During the phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester enters the same 6-digit passkey. If the IUT has IO capabilities set to 'KeyboardOnly' the passkey is not displayed and both initiator and responder input the same 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

## SM/PER/OOB/BV-06-C [IUT Responder -Only Lower Tester has OOB data -Success]

- Test Purpose

Verify that the IUT performs the pairing procedure correctly as responder if only the Lower Tester has OOB data.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to ' Keyboard Display' .
- b. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags', and the MITM flag set to '1' and all reserved b i ts are set to '0'.
- c. OOB data flag set to 0x01.
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to ' KeyboardOnly ' or 'KeyboardDisplay' or 'DisplayOnly' or 'DisplayYesNo'
- b. OOB data flag set to 0x00
3. Alternatively, the IUT may respond with Pairing Failed command with reason code set to 'OOB Not Available' or 'Authentication Requirements'.
4. The Lower Tester has a pre-defined 6-digit passkey.
5. During the phase 2 pairing, the Lower Tester displays the 6-digit passkey while the user of the IUT enters the same 6-digit passkey.
6. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2. If the IO capabilities of the IUT are 'DisplayYesNo' or 'DisplayOnly' the IUT displays the 6 -digit passkey while the Lower Tester enters the 6-digit passkey.
- Expected Outcome

## Pass verdict

The Central can encrypt the link successfully.

ALT: The IUT responds with Pairing F ailed, with reason code set to 'OOB Not Available' or 'Authentication Requirements'.

## SM/CEN/OOB/BV-07-C [IUT Initiator -Only Lower Tester has OOB data -Unauthenticated Success]

## · Test Purpose

Verify that the IUT performs the OOB pairing procedure correctly as initiator if only the Lower Tester has OOB data and the IUT does not require MITM protection.

- Reference

[7] 2.3.5.1, C.2.1.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x01 and MITM bit set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing procedure and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

## SM/PER/OOB/BV-08-C [IUT Responder -Only Lower Tester has OOB data -Lower Tester also supports Just Works]

## · Test Purpose

Verify that the IUT performs the pairing procedure correctly as responder if only the Lower Tester has OOB data and supports the Just Works pairing method.

- Reference

[7] 2.3.5.1, C.2.1.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x01 and MITM bit set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00
3. Alternatively, the IUT may respond with Pairing Failed command with reason code set to 'OOB Not Available' or 'Authentication Requirements'.
4. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated STK.
- Expected Outcome

## Pass verdict

The Central can encrypt the link successfully.

ALT: The IUT responds with Pairing Failed with reason code set to 'OOB Not Available' or 'Authentication Requirements'.

## SM/CEN/OOB/BV-09-C [IUT Initiator -Only IUT has OOB data -Unauthenticated Success]

- Test Purpose

Verify that the IUT performs pairing correctly as initiator if the responder does not have OOB data and the IUT does not require MITM protection.

- Reference

[7] 2.3.5.1, C.2.1.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x01
2. The Lower Tester responds with a Pairing Response command ,with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 and MITM bit set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing procedure and establish an encrypted link with the key generated in phase 2.
- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

## SM/PER/OOB/BV-10-C [IUT Responder -Only IUT has OOB data -Lower Tester also supports Just Works]

- Test Purpose

Verify that the IUT performs the pairing procedure correctly as responder if only the IUT has OOB data and the Lower Tester supports the Just Works pairing method.

- Reference

[7] 2.3.5.1, C.2.1.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 and MITM bit set to '0'

2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x01
3. Alternatively, the IUT may respond with Pairing Failed command with reason code set to 'Authentication Requirements'.
4. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated STK.
- Expected Outcome

## Pass verdict

The Central encrypts the link successfully or in the alternate case the IUT responds with the Pairing Failed commend with the reason code set to 'Authentication Requirements'.

## SM/CEN/OOB/BI-01-C [IUT Initiator -Both sides have different OOB data -Failure]

- Test Purpose

Verify that the IUT initiates OOB pairing procedure and handles the failure correctly.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT and the Lower Tester have different 128 bit OOB data.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits Pairing Request command with OOB data flag set to0x01 and its MITM bit set to '1'.
2. The Lower Tester responds with a Pairing Response command, with OOB data flag to set 0x01 and MITM bit set to '1'.
3. The IUT detects the mismatch of confirm value. The IUT sends Pairing Failed and the Lower Tester initiates disconnect.
- Expected Outcome

## Pass verdict

The IUT detects the mismatch of confirm value, sends ' Pairing Failed ' and the Lower Tester disconnects the link.

## SM/PER/OOB/BI-02-C [IUT Responder -Both sides have different OOB data -Failure]

- Test Purpose

Verify that the IUT responds to OOB pairing procedure and handles the failure correctly.

- Reference

[7] 2.3.5.3, C.2.1.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- -The IUT and the Lower Tester have different 128 bit OOB data.
- -The IUT OOB data can be anything but the same value as the OOB data in the Lower Tester.
- Test Procedure
1. The Lower Tester initiates Pairing Request command with OOB data flag set to 0x01 and its MITM bit set to '1'.
2. The IUT responds with Pairing Response command with OOB data flag set to 0x01 and MITM bit set to '1'.
3. The IUT detects the mismatch of confirm value, sends Pairing Failed and notifies the Upper Tester.
- Expected Outcome

## Pass verdict

The IUT detects the mismatch of confirm value and notifies the Upper Tester.

## 4.6 Encryption Key Size

Verify the correct implementation of the encryption key size negotiation procedure.

## 4.6.1 Encryption Key Size Negotiation

## SM/CEN/EKS/BV-01-C [IUT initiator, Lower Tester Maximum Encryption Key Size = Min\_Encryption\_Key\_Length]

- Test Purpose

Verify that the IUT uses correct key size during encryption as initiator.

- Reference

## 7 2.3.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits pairing request.
2. The Lower Tester responds with Pairing Response command with Maximum Encryption Key Size field set to Min\_Encryption\_Key\_Length '.
3. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
4. The Lower Tester disconnects the connection.
5. The Upper Tester initiates a connection with the Lower Tester.
6. The IUT and the Lower Tester create a connection.
7. The Upper Tester initiates encryption with the Lower Tester.
8. The IUT and the Lower Tester encrypt the connection using the LTK.

- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully.

In Step 8, the connection is encrypted using the LTK.

- Notes

The value of Min\_Encryption\_Key\_Length is specified in the IXIT [6].

## SM/PER/EKS/BV-02-C [IUT Responder, Lower Tester Maximum Encryption Key Size = Min\_Encryption\_Key\_Length]

- Test Purpose

Verify that the IUT uses correct key size during encryption as responder.

- Reference

## 7 2.3.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates Pairing Request command with Maximum Encryption Key Size field set to Min\_Encryption\_Key\_Length '.
2. The IUT responds with Pairing Response command.
3. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
4. The Lower Tester disconnects the connection.
5. The Lower Tester initiates a connection with the IUT.
6. After the connection is completed, the Lower Tester initiates encryption with the IUT using the LTK.
7. The IUT and the Lower Tester successfully encrypt the connection.
- Expected Outcome

## Pass verdict

The Lower Tester can encrypt the link successfully.

In Step 7, the connection is encrypted using the LTK.

- Notes

The value of Min\_Encryption\_Key\_Length is specified in the IXIT [6].

## SM/CEN/EKS/BI-01-C [IUT initiator, Lower Tester Maximum Encryption Key Size &lt; Min\_Encryption\_Key\_Length]

- Test Purpose

Verify that the IUT checks that the resultant encryption key size is not smaller than the minimum key size.

- Reference

## 7 2.3.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command.
2. The Lower Tester responds with a Pairing Response command with Maximum Encryption Key Size field set to Min\_Encryption\_Key\_Length -1. The value of Min\_Encryption\_Key\_Length used should be determined by the value supported on the IUT and given by IXIT [6] value.
3. The IUT transmits the Pairing Failed command.
- Expected Outcome

## Pass verdict

- -The IUT transmits Pairing Failed command.
- -If the IUT supports a value of Min\_Encryption\_Key\_Length greater than the minimum defined value for the encryption key length parameter in the specification, the IUT transmits the Pairing Failed comment with error code 'Encryption Key Size'.
- -If the IUT supports only the minimum defined values for the encryption key length parameter in the specification, the IUT transmits the Pairing Failed command and may respond with error code 'Invalid Parameters'.

## SM/PER/EKS/BI-02-C [IUT Responder, Lower Tester Maximum Encryption Key Size &lt; Min\_Encryption\_Key\_Length]

- Test Purpose

Verify that the IUT uses correct key size during encryption as responder.

- Reference

[7] 2.3, 2.3.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates Pairing Request command with Maximum Encryption Key Size field set to Min\_Encryption\_Key\_Length-1.
2. The IUT transmits the Pairing Failed command.
- Expected Outcome

## Pass verdict

The IUT detects that encryption key size is smaller than the minimum key size parameter for the IUT and responds with Pairing Failed command.

If the IUT supports a value of Maximum Encryption Key Size greater than the minimum defined value for the encryption key length parameter in the Specification the IUT transmits the Pairing Failed command with error code 'Encryption Key Size'.

If the IUT supports only the minimum defined value for the encryption key length parameter the IUT transmits the Pairing Failed command and may respond with error code 'Invalid Parameters'.

## 4.7 Signing

Verify the correct implementation of the generation and verification of MAC with signed data.

## 4.7.1 Signing of Data

## SM/SIGN/BV-01-C [IUT transfers signed data -Success]

- Test Purpose

Verify that the IUT has implemented the signing algorithm correctly for data transferring.

- Reference

[7] 2.4.5

- Initial Condition
- -The preamble has been executed.
- -Pairing has been executed and the IUT has distributed CSRK as requested by the Lower Tester.
- -A new link has been established with no encryption.
- -SignCounter is set to 0.
- Test Procedure

The IUT transfers a pre-defined packet with signed MAC and SignCounter.

- Expected Outcome

## Pass verdict

The IUT has correct MAC in the signed data.

## SM/SIGN/BV-03-C [IUT receives signed data -Success]

- Test Purpose

Verify that the IUT has implemented the signing algorithm correctly for data receiving.

- Reference

[7] 2.4.5

- Initial Condition
- -The preamble has been executed.
- -Pairing has been executed and the Lower Tester has distributed CSRK as requested by the IUT.
- -A new link has been established with no encryption.
- -SignCounter is set to 0.

- Test Procedure

The Lower Tester transfers a pre-defined packet with signed MAC and SignCounter.

The IUT has verified the MAC with signed data correctly.

- Expected Outcome

## Pass verdict

The IUT has verified the MAC with signed data correctly.

The IUT has forwarded the signed data to the Upper Tester correctly.

## SM/SIGN/BI-01-C [IUT receives signed data -Failure]

- Test Purpose

Verify that the IUT has implemented the signing algorithm correctly to detect a failure in signed data.

- Reference

[7] 2.4.5

- Initial Condition
- -The preamble has been executed.
- -Pairing has been executed and the Lower Tester has distributed CSRK as requested by the IUT.
- -A new link has been established with no encryption.
- Test Procedure

The Lower Tester transfers a pre-defined packet with incorrectly signed MAC.

The IUT has detected the incorrectly signed MAC and ignores the received PDU.

- Expected Outcome

## Pass verdict

The IUT has detected the incorrectly signed MAC and ignores the received PDU.

The Upper Tester may be notified.

## SM/SIGN/BI-02-C [IUT ignores a PDU with the SignCounter the same as the previous PDU]

- Test Purpose

Verify that the IUT handles replay attack by ignoring a received PDU when the SignCounter is the same as the last successful PDU.

- Reference

## 7 2.4.5

- Initial Condition
- -The preamble has been executed.
- -Pairing has been executed, and the Lower Tester has distributed CSRK as requested by the IUT.
- -A new link has been established with no encryption.

- Test Procedure

The Lower Tester transfers a predefined packet with signed MAC and SignCounter set to SC1.

The IUT has verified the MAC with signed data correctly.

The Lower Tester transfers a predefined packet with signed MAC and SignCounter set to SC1.

The IUT has detected the incorrectly signed MAC and ignores the received PDU.

The Lower Tester transfers a predefined packet with signed MAC and SignCounter set to SC1.

The IUT has detected the incorrectly signed MAC and ignores the received PDU.

The Lower Tester transfers a predefined packet with signed MAC and SignCounter set to SC2.

The IUT has verified the MAC with signed data correctly.

- Expected Outcome

## Pass verdict

The IUT has detected the first PDUs with SignCounter set to SC1 and SC2.

The Upper Tester may be notified.

The IUT ignores the second and third PDUs with SignCounter set to SC1.

## 4.8 Key Distribution and Usage

Verify the correct implementation of key distribution and usage.

## 4.8.1 Key Distribution during bonding

## 4.8.1.1 Key Distribution -Success -Peripheral

- Test Purpose

Verify correct behavior during the key distribution phase.

- Reference

[7] 3.6.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Case Configuration

| Test Case | Lower Tester Responder Key Distribution | IUT Responder Key Distribution |
| SM/PER/KDU/BV-01-C [LE Legacy Pairing, IUT Responder - Lower Tester sets EncKey bit - Success] | SC: 0 EncKey: 1 IdKey: 0 SignKey: 0 | SC: 0 EncKey: 1 IdKey: 0 SignKey: 0 |
| SM/PER/KDU/BV-02-C [LE Legacy Pairing, IUT Responder - Lower Tester sets IdKey bit - Success] | SC: 0 EncKey: 0 IdKey: 1 SignKey: 0 | SC: 0 EncKey: 0 IdKey: 1 SignKey: 0 |

Table 4.6: Key Distribution -Success -Peripheral test cases

| Test Case | Lower Tester Responder Key Distribution | IUT Responder Key Distribution |
| SM/PER/KDU/BV-03-C [LE Legacy Pairing, IUT Responder - Lower Tester sets SignKey bit - Success, v6.2 or earlier] | SC: 0 EncKey: 0 IdKey: 0 SignKey: 1 | SC: 0 EncKey: 0 IdKey: 0 SignKey: 1 |
| SM/PER/KDU/BV-08-C [LE Secure Connections Pairing, IUT Responder - Lower Tester sets IdKey bit - Success] | SC: 1 EncKey: 0 IdKey: 1 SignKey: 0 | SC: 1 EncKey: 0 IdKey: 1 SignKey: 0 |
| SM/PER/KDU/BV-09-C [LE Secure Connections Pairing, IUT Responder - Lower Tester sets SignKey bit - Success, v6.2 or earlier] | SC: 1 EncKey: 0 IdKey: 0 SignKey: 1 | SC: 1 EncKey: 0 IdKey: 0 SignKey: 1 |

Figure 4.2: Key Distribution -Success -Peripheral MSC

- Test Procedure
1. The Lower Tester initiates a Pairing Request command with the SC bit of AuthReq , 'Initiator Key Distribution' field with SC set to 1 and all other bits set to 0 , and 'Responder Key Distribution' field as specified in Table 4.6.
2. The IUT responds with a Pairing Response command with the SC bit of AuthReq , 'Responder Key Distribution' field as specified in Table 4.6.
3. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
4. The IUT distributes only the requested key and information associated with it.
- Expected Outcome

## Pass verdict

The IUT sets the bits as specified in Table 4.6 in the Pairing Request and Pairing Response.

If the Lower Tester sets the EncKey bit: The IUT distributes LTK using the Encryption Information command followed by EDIV and Rand using the Central Identification command. The IUT does not distribute any other key information to the Lower Tester.

If the Lower Tester sets the IdKey bit: The IUT distributes IRK using the Identity Information command followed by the Identity Address Information command. The IUT does not distribute any other keys. If BR\_ADDR is a static random address, then AddrType is set to 0x01. If BR\_ADDR is a public device address, then AddrType is set to 0x00.

If the Lower Tester sets the SignKey bit: The IUT distributes CSRK using the Signing Information command and does not distribute any other keys.

## 4.8.1.2 Key Distribution -Success -Central

- Test Purpose

Verify correct behavior during the key distribution phase.

- Reference

[7] 3.6.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Case Configuration

Table 4.7: Key Distribution -Success -Central test cases

| Test Case | IUT Initiator Key Distribution | Lower Tester Initiator Key Distribution |
| SM/CEN/KDU/BV-04-C [LE Legacy Pairing, IUT Initiator - Lower Tester sets SignKey bit - Success, v6.2 or earlier] | SC: 0 EncKey: 0 IdKey: 0 SignKey: 1 | SC: 0 EncKey: 0 IdKey: 0 SignKey: 1 |
| SM/CEN/KDU/BV-05-C [LE Legacy Pairing, IUT Initiator - Lower Tester sets IdKey bit - Success] | SC: 0 EncKey: 0 IdKey: 1 SignKey: 0 | SC: 0 EncKey:0 IdKey: 1 SignKey: 0 |
| SM/CEN/KDU/BV-06-C [LE Legacy Pairing, IUT Initiator - Lower Tester sets EncKey bit - Success] | SC: 0 EncKey: 1 IdKey: 0 SignKey: 0 | SC: 0 EncKey:1 IdKey: 0 SignKey: 0 |
| SM/CEN/KDU/BV-10-C [LE Secure Connections Pairing, IUT Initiator - Lower Tester sets IdKey bit - Success] | SC: 1 EncKey: 0 IdKey: 1 SignKey: 0 | SC: 1 EncKey: 0 IdKey: 1 SignKey: 0 |
| SM/CEN/KDU/BV-11-C [LE Secure Connections Pairing, IUT Initiator - Lower Tester sets SignKey bit - Success, v6.2 or earlier] | SC: 1 EncKey: 0 IdKey: 0 SignKey: 1 | SC: 1 EncKey: 0 IdKey: 0 SignKey: 1 |

Figure 4.3: Key Distribution -Success -Central MSC

- Test Procedure
1. The IUT transmits a Pairing Request command with the SC bit of AuthReq , 'Initiator Key Distribution' field as specified in Table 4.7 , and 'Responder Key Distribution' field with all bits set to 0.
2. The Lower Tester responds with a Pairing Response command with the SC bit of AuthReq, 'Initiator Key Distribution' field as specified in Table 4.7 , and 'Responder Key Distribution' field with all bits set to 0.
3. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
4. The IUT distributes only the requested key and information associated with it.
- Expected Outcome

## Pass verdict

The IUT sets the bits as specified in Table 4.7 in the Pairing Request and Pairing Response.

If the Lower Tester sets the EncKey bit: The IUT distributes LTK using the Encryption Information command followed by EDIV and Rand using the Central Identification command. The IUT does not distribute any other key information to the Lower Tester.

If the Lower Tester sets the IdKey bit: The IUT distributes IRK using the Identity Information command followed by the Identity Address Information command. The IUT does not distribute any other keys. If BR\_ADDR is a static random address, then AddrType is set to 0x01. If BR\_ADDR is a public device address, then AddrType is set to 0x00.

If the Lower Tester sets the SignKey bit: The IUT distributes CSRK using the Signing Information command and does not distribute any other keys.

## 4.8.1.3 LE Secure Connections Pairing -Lower Tester sends invalid public key

- Test Purpose

Verify that the IUT detects an invalid public key from the Lower Tester.

- Reference

[7], [8] 2.3.5.6.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is in the role specified in Table 4.8.

- -FKC is the number of failed pairing attempts before the Upper Tester generates a new key pair as defined in the IXIT [6] entry and is used in Table 4.9.
- -The Lower Tester generates and uses only private/public key pairs where bit 0 of the private key is set to 0.
- Test Case Configuration
- Test Procedure

Table 4.8: LE Secure Connections Pairing -Lower Tester sends invalid public key test cases

| Test Case | Role | Rounds | Pass Verdict |
| SM/PER/KDU/BI-01-C [LE Secure Connections Pairing - Lower Tester sends invalid public key, v5.4 or earlier] | Peripheral | 1 - 4 | A |
| SM/PER/KDU/BI-04-C [LE Secure Connections Pairing - Lower Tester sends invalid public key, v6.0 or later] | Peripheral | 1 - 4 | B |
| SM/CEN/KDU/BI-01-C [LE Secure Connections Pairing - Lower Tester sends invalid public key, v5.4 or earlier] | Central | 1 - 4 | A |
| SM/CEN/KDU/BI-04-C [LE Secure Connections Pairing - Lower Tester sends invalid public key, v6.0 or later] | Central | 1 - 5 | B |

Figure 4.4: LE Secure Connections Pairing -Lower Tester sends invalid public key MSC

Execute Steps 1 -5 for each round in Table 4.9, repeating the number of times as specified in Table 4.9.

1. The Central initiates a Pairing Request command, with the SC bit of AuthReq set to '1'.
2. The Peripheral responds with a Pairing Response command with the SC bit of AuthReq set to '1'. If the Lower Tester is the Peripheral, then it also sets all bits in the 'Responder Key Distribution' field to '0'.
3. The IUT and the Lower Tester perform the Public Key Exchange. The Lower Tester generates a new valid private/public key pair and modifies the keys as specified in Table 4.9. The Lower Tester verifies that these new coordinates are not on the curve before sending them; if accidentally the new coordinates are valid, then the generation procedure is repeated. The resulting invalid Public Key is sent over the air.
4. The Lower Tester continues the pairing procedure using the public key value sent over the air until the IUT fails the pairing procedure. In Authentication Stage 2, the Lower Tester either uses the computed DHKey or DHKey = 0 as specified in Table 4.9.
- Expected Outcome

Table 4.9: Invalid Public Key generation for each round

| Round | Key Size | Invalid Key Type | Repeat # of times | Lower Tester DHKey |
| 1 | P-256 | Generate valid public key and set y-coordinate = 0 | If FKC = 0, then run once; otherwise, run 20×FKC times | 0 |
| 2 | P-256 | Generate valid public key and set y-coordinate = 0 | 1 | Computed DHKey |
| 3 | P-256 | Generate valid public key and flip a bit in y-coordinate | 1 | Computed DHKey |
| 4 | P-256 | Public Key coordinates (0, 0) | 1 | 0 |
| 5 | P-256 | Generate valid public key with same X-coordinate as the IUT | 1 | Computed DHKey |

## Pass verdict

The applicable Pass verdict specified in Table 4.8 is applied as stated below.

- A) The IUT fails the pairing procedure any time after receiving the invalid public key. If the IUT sends a Pairing Failed message, then any reason code is allowed.
- B) The IUT sends a Pairing Failed message after receiving the invalid public key or immediately after Public Key Exchange has completed with Reason set to 0x0B (DHKey Check Failed).

## Fail verdict

The IUT successfully completes the pairing procedure.

If the IUT is the Central, then the second and subsequent Pairing Requests sent by the IUT have a decreasing waiting interval between the pairing failing and the Pairing request.

## SM/PER/KDU/BI-02-C [LE Legacy Pairing, IUT Responder -Key Rejected]

- Test Purpose

Verify that the IUT properly handles a Pairing\_Failed command when a key is rejected.

- Reference

[7] 3.5.5, 3.6.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing\_ Request command, with the SC bit of AuthReq set to '0' and with the IdKey, EncKey, and SignKey bits of 'Responder Key Distribution' and 'Initiator Key Distribution' set to '1'.
2. The IUT responds with a Pairing\_Response command with at least one of the IdKey, EncKey, or SignKey bits of 'Responder Key Distribution' set to '1'. Perform either alternative 2A or 2B based on the Initiator key bits set in the Pairing\_Response.

Alternative 2A (Initiator Key has at least one bit set in the Pairing\_Response)

- 2A.1 The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
- 2A.2 The IUT distributes the keys specified in the Pairing\_Response using the correct commands in the correct order. The IUT does not distribute any other keys to the Lower Tester.
- 2A.3 The Lower Tester sends a Pairing\_Failed command to the IUT with reason code set to '0x0F' (Key Rejected).
- 2A.4 The pairing process is aborted and the IUT reports the failure to the Upper Tester.
- Alternative 2B (Initiator Key has no bits set in the Pairing\_Response)
- 2B.1 The Lower Tester sends a Pairing\_Failed command to the IUT with reason code set to '0x0F' (Key Rejected) .
- 2B.2 The pairing process is aborted and the IUT reports the failure to the Upper Tester.
- Expected Outcome

## Pass verdict

The IUT detects the Pairing\_Failed command from the Lower Tester and reports the failure to the Upper Tester.

The IUT distributes the keys specified in the Pairing\_Response using the correct commands in the correct order. The IUT does not distribute any other keys to the Lower Tester.

## SM/PER/KDU/BI-03-C [LE Secure Connections Pairing, IUT Responder -Key Rejected]

- Test Purpose

Verify that the IUT properly handles a Pairing\_Failed command when a key is rejected.

- Reference

[7] 3.5.5, 3.6.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing\_ Request command, with the SC bit of AuthReq set to '1' and with the IdKey, EncKey, and SignKey bits of 'Responder Key Distribution' set to '1'.

2. The IUT responds with a Pairing\_ Response command with the SC bit of AuthReq set to '1' and with at least one of the IdKey, EncKey, or SignKey bits of 'Responder Key Distribution' set to '1'. Perform either alternative 2A or 2B based on the 'Initiator Key' bits set in the Pairing\_Response. Alternative 2A ('Initiator Key' has at least one bit set in the Pairing\_Response)
2. 2A.1 The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the key generated in phase 2.
3. 2A.2 The IUT distributes the keys specified in the Pairing\_Response using the correct commands in the correct order. The IUT does not distribute any other keys to the Lower Tester.
4. 2A.3 The Lower Tester sends a Pairing\_Failed command to the IUT with reason code set to '0x0F' (Key Rejected).
5. 2A.4 The pairing process is aborted and the IUT reports the failure to the Upper Tester. Alternative 2B ('Initiator Key' has no bits set in the Pairing\_Response)
6. 2B.1 The Lower Tester sends a Pairing\_Failed command to the IUT with reason code set to '0x0F' (Key Rejected) .
7. 2B.2 The pairing process is aborted and the IUT reports the failure to the Upper Tester.
- Expected Outcome

## Pass verdict

The IUT detects the Pairing\_Failed command from the Lower Tester and reports the failure to the Upper Tester.

The IUT distributes the keys specified in the Pairing\_Response using the correct commands in the correct order. The IUT does not distribute any other keys to the Lower Tester.

## 4.8.2 Re-encrypt an encrypted link with LTK

## SM/PER/KDU/BV-07-C [IUT Responder -Existing encrypted link is re-encrypted using LTK]

- Test Purpose

Verify that the IUT correctly handles a requested encrypted session setup to use the distributed LTK, EDIV and Rand values when the key distribution phase has completed.

- Reference

[7] 3.6.1

- Initial Condition
- -The Lower Tester and the IUT have completed SM/PER/KDU/BV-01-C [LE Legacy Pairing, IUT Responder -Lower Tester sets EncKey bit -Success] and have not disconnected the link.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure

The Lower Tester re-encrypts the link using the LTK EDIV and RAND values distributed by the IUT.

- Expected Outcome

## Pass verdict

The Lower Tester can re-encrypt the link successfully, i.e., the IUT sends an encrypted LL\_START\_ENC\_RSP packet with the correct MIC, which is acknowledged by the Lower Tester.

## 4.9 Peripheral Initiated Security Request

Verify the correct implementation of the Peripheral initiated security request.

## 4.9.1 Peripheral Initiated Pairing

## SM/PER/PIS/BV-01-C [Peripheral initiates pairing]

- Test Purpose

Verify that the IUT is able to initiate a pairing as a Peripheral.

- Reference

[7] 2.4.6

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- -The IUT is not bonded with the Lower Tester.
- Test Procedure
1. The Upper T ester commands the IUT to send 'security request' with an MITM.
2. Upon receiving the security request from the IUT, the Lower Tester initiates pairing.
- Test Condition

It must be guaranteed that the IUT is able to send security request if requested via the Upper Tester.

- Expected Outcome

## Pass verdict

The IUT sends Security Request.

Pairing has completed successfully.

## SM/CEN/PIS/BV-02-C [Peripheral Initiates pairing -Central Response]

- Test Purpose

Verify that the IUT, as Central, is able to respond to Peripheral initiated pairing.

- Reference

[7] 2.4.6

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- -The IUT is not bonded with the Lower Tester.

- Test Procedure
1. The Lower Tester sends 'security request' with MITM as ' 1 ' to the IUT.
2. Upon receiving the security request from the Lower Tester, the IUT initiates pairing or the IUT responds to the request with a Pairing Failure Response with the reason field set to 'Pairing Not Supported.'
- Expected Outcome

## Pass verdict

Pairing has completed successfully, or

The IUT response to the request with a Pairing Failure Response with the reason set to 'Pairing Not Supported' .

## 4.9.2 Peripheral Initiated Encryption

## SM/PER/PIS/BV-02-C [Peripheral initiates encryption]

- Test Purpose

Verify that the IUT is able to initiate encryption as a Peripheral.

- Reference

[7] 2.4.6, C.1.1

- Initial Condition
- -The Lower Tester and the IUT have been bonded with exchanged security information with security property of MITM protection not required.
- -The Lower Tester and the IUT both maintained the bond information.
- -The Lower Tester and the IUT currently have established link layer connection without encryption and SMP fixed channel is ready.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Upper T ester commands the IUT to send 'security request' with MITM as '0'.
2. The Lower Tester starts the link encryption procedure with bonded security information, and link is encrypted successfully.
- Test Condition

It must be guaranteed that the IUT is able to send a security request if requested via the Upper Tester.

- Expected Outcome

## Pass verdict

The IUT sends Security Request with required authentication requirement.

Encryption procedure with LTK is performed correctly.

## SM/CEN/PIS/BV-03-C [Peripheral Initiates Encryption -Central Response]

- Test Purpose

Verify that the IUT, as Central, is able to respond to Peripheral initiated encryption and checks if that it has the required information.

- Reference

[7] 2.4.6

- Initial Condition
- -The IUT is Central. The Lower Tester is Peripheral.
- -The IUT is not bonded with the Lower Tester.
- -The IUT does not have LTK, Rand, or EDIV from the Lower Tester.
- Test Procedure
1. The Lower Tester sends a Security Request to the IUT.
2. The IUT does not begin encryption and instead sends a Pairing Request.
3. The Lower Tester sends another Security Request to the IUT following the Pairing Request.
4. The Lower Tester sends a Pairing Response shortly after the second Security Request.
5. The IUT and the Lower Tester complete the Pairing procedure.
- Expected Outcome

Figure 4.5: SM/CEN/PIS/BV-03-C [Peripheral Initiates Encryption -Central Response] MSC

## Pass verdict

In Step 2, the IUT does not begin Encryption and instead sends a Pairing Request.

The IUT ignores the second Security Request in Step 3 and does not begin encryption.

## 4.10 Pairing Methods Using LE Secure Connections

## 4.10.1 Common Procedures

## 4.10.1.1 DH Key Generation

After exchanging the Pairing Request and Pairing Response procedures, the IUT and the Lower Tester generate the DH Key, exchanging Pairing Public Key packets.

## 4.10.2 Just Works (SCJW)

## SM/CEN/SCJW/BV-01-C [Just Works, IUT Initiator, Secure Connections -Success]

- Test Purpose

Verify that the IUT supporting LE Secure Connections performs the Just Works or Numeric Comparison pairing procedure correctly as initiator. Verify that the IUT generates a different 128-bit nonce value each time Authentication Stage 1 executes.

- Reference

[7] 2.3.5.1, 2.3.5.6

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure

Repeat the test steps three times. In Authentication Stage 1, the Lower Tester is to store the Simple Pairing Number of the IUT for each of the three rounds, to be compared at the end of round 3.

1. The IUT transmits Pairing Request command with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. T he MITM flag set to either '0' for Just Works or ' 1 ' for Numeric Comparison, the Secure Connections flag set to ' 1 ', and all the reserved bits set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq Bonding Flags set to '00', the MITM flag set to '0', Secure Connections flag set to '1' and all the reserved bits are set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works or Numeric Comparison pairing procedure according to the MITM flag and IO capabilities, and establish an encrypted link with the LTK generated in phase 2.

The test is repeated by the IUT to test all supported combinations of [7] Section 2.3.5.1, Table 2.8 which do not result in passkey entry.

- Expected Outcome

## Pass verdict

The encryption procedure initiated by the IUT completes successfully.

The IUT can encrypt the link successfully using LE Secure Connections.

The 128-bit nonce generated by the IUT during each Authentication Stage 1 are different values.

## SM/PER/SCJW/BV-02-C [Just Works, IUT Responder, Secure Connections -Success]

- Test Purpose

Verify that the IUT supporting LE Secure Connections is able to perform the Just Works or Numeric Comparison pairing procedure correctly when acting as responder. Verify that the IUT generates a different 128-bit nonce value each time Authentication Stage 1 executes.

- Reference

[7] 2.3.5.1, 2.3.5.6.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure

Repeat the test steps 3 times. In Authentication Stage 1, the Lower Tester is to store the Simple Pairing Number of the IUT for each of the 3 rounds, to be compared at the end of round 3.

1. The Lower Tester transmits Pairing Request command with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq Bonding Flags set to '00', MITM flag set to '0', Secure Connections flag set to '1' and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. The MITM flag set to either '0' for Just Works or ' 1 ' for Numeric Comparison, the Secure Connections flag set to ' 1 ', and all reserved bits set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works or Numeric Comparison pairing procedure according to the MITM flag and IO capabilities, and establish an encrypted link with the LTK generated in phase 2.

The test is repeated by the IUT to test all supported combinations of [7] Section 2.3.5.1, Table 2.8 which do not result in passkey entry.

- Expected Outcome

## Pass verdict

The encryption procedure initiated by the Lower Tester completes successfully.

The IUT and the Lower Tester can encrypt the link successfully using LE Secure Connections.

The 128-bit nonce generated by the IUT during each Authentication Stage 1 are different values.

## SM/PER/SCJW/BV-03-C [Just Works, IUT Responder, Secure Connections -Handle AuthReq Flag RFU Correctly]

- Test Purpose

Verify that the IUT is able to perform the Just Works pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Peripheral, responder.

- Reference

[7] 2.3.5.1, 2.3.5.6.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.

- Test Procedure
1. The Lower Tester transmits Pairing Request command with:
- a. IO Capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. MITM set to '0' and all reserved bits are set to '1' .
2. The IUT responds with a Pairing Response command, with:
- a. IO Capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated LTK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the Lower Tester completes successfully.

The IUT and the Lower Tester can encrypt the link successfully.

## SM/CEN/SCJW/BV-04-C [Just Works, IUT Initiator, Secure Connections -Handle AuthReq Flag RFU Correctly]

- Test Purpose

Verify that the IUT is able to perform the Just Works pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Central, initiator.

- Reference

[7] 2.3.5.1, 2.3.5.6.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO Capability set to any IO Capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO Capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags' and the MITM flag set to '0' , Secure Connections flag set to '1', and all reserved bits are set to '1' .
3. The IUT and the Lower Tester perform phase 2 of the Just Works pairing and establish an encrypted link with the generated LTK.

- Expected Outcome

## Pass verdict

The encryption procedure initiated by the IUT completes successfully.

The link is encrypted successfully.

## SM/CEN/SCJW/BI-01-C [Just Works, IUT Initiator, Secure Connections -Pairing Failed]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Just Works or Numeric Comparison pairing failures.

- Reference

[7] 3.5.5, 2.3.5.6.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits Pairing Request command with:
- a. IO capability is set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to '1' and all reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Failed command with reason code '0x03' (Authentication Requirements).
3. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

4. Execute Step 1.
5. The Lower Tester responds with a Pairing Failed command with reason code '0x08' (Unspecified Reason).
6. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

7. Execute Step 1.
8. The Lower Tester responds with a Pairing Failed command with reason code '0x05' (Pairing Not Supported).
9. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

10. Execute Step 1.
11. The Lower Tester responds with a Pairing Failed command with reason code '0x09' (Repeated Attempts).
12. The pairing process is aborted. The IUT reports the failure to the Upper Tester.
13. Execute Step 1.
14. The Lower Tester transmits Pairing Response command with:
- a. IO capability is set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to '1' and all reserved bits are set to '0'

15. The Lower Tester responds with a Pairing Failed command in phase 2 with reason code '0x0C (Numeric Comparison Failed).
16. The pairing process is aborted. The IUT reports the failure to the Upper Tester.
- Expected Outcome

## Pass verdict

For each pairing failure, the IUT detects the failures reported by the responder and responds correctly to the Lower Tester.

For each pairing failure, the IUT aborts the pairing process and reports the failure to the Upper Tester.

## SM/PER/SCJW/BI-02-C [Just Works, IUT Responder, Secure Connections -Confirm Check Failure]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Just Works pairing failure as responder correctly, when the Lower Tester does not confirm 'OK' .

- Reference

[7] 2.3.5.1, 2.3.5.6.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits a Pairing Request command with:
- a. IO capability set to 'NoInputNoOutput'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '01', and the MITM flag set to '0', Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to any IO capability
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
3. During phase 2 of the Just Works pairing procedure, the Lower Tester transmits a Pairing Failed command with (Confirm Value Failed).
- Expected Outcome

## Pass verdict

The IUT aborts the pairing.

## 4.10.3 Passkey Entry (SCPK)

## SM/CEN/SCPK/BV-01-C [Passkey Entry, IUT Initiator, Secure Connections -Success]

- Test Purpose

Verify that the IUT supporting LE Secure Connections performs the Passkey Entry pairing procedure correctly as Central, initiator.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 ' . Keypress bit is set to '1' if supported
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly' .
- b. OOB data flag set to 0x00 (OOB Authentication data not present).
- c. AuthReq bonding flag set to '00', the MITM flag set to '1', Secure Connections flag set to '1' and all reserved bits are set to '0'. Keypress bit is set to '1' if supported by the IUT.
3. During the phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester prompts user to enter the 6digit passkey. If the IUT's IO capabilities are 'KeyboardOnly' the passkey is not displayed and both the IUT and the Lower Tester enter the same 6-digit passkey. If Keypress bit is set, pairing keypress notifications are sent by the Lower Tester.
4. The IUT and the Lower Tester use the same 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the Passkey Entry pairing procedure and establish an encrypted link with the LTK generated in phase 2.
- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully using LE Secure Connections.

- Notes

This test also covers the use of the keypress bit.

## SM/PER/SCPK/BV-02-C [Passkey Entry, IUT Responder, Secure Connections -Success]

- Test Purpose

Verify that the IUT supporting LE Secure Connections is able to perform the Passkey Entry pairing procedure correctly when acting as Peripheral, responder.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester initiates a Pairing Request command with:
- a. IO capability set to 'Keyboard Display '
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags', and the MITM flag set to '1' Secure Connections flag set to '1' and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly' or ' KeyboardDisplay ' or 'DisplayYesNo' or 'DisplayOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 ' . Keypress bit is set to ' 1 ' if supported by the IUT
3. During the phase 2 passkey pairing process, the Lower Tester displays the 6-digit passkey while the IUT prompts user to enter the 6-digit passkey. If the IO capabilities of the IUT are 'DisplayYesNo' or 'DisplayOnly' the IUT displays the 6 -digit passkey while the Lower Tester enters the 6-digit passkey. If Keypress bit is set, pairing keypress notifications are send by the IUT
4. The IUT and the Lower Tester use the same pre-defined 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the LE pairing and establish an encrypted link with the LTK generated in phase 2.

The test is repeated where the Lower Tester also sets the Keypress bit to '1' if supported by the IUT in Step 1c.

- Expected Outcome

## Pass verdict

The Central can encrypt the link successfully with LE Secure Connections.

The IUT only sends keypress notification if supported by the Lower Tester.

- Notes

This test also covers the use of the keypress bit.

## SM/PER/SCPK/BV-03-C [Passkey Entry, IUT Responder, Secure Connections -Handle AuthReq Flag RFU Correctly]

## · Test Purpose

Verify that the IUT supporting LE Secure Connections is able to perform the Passkey Entry pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Peripheral, responder.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits Pairing Request command with:
- a. IO Capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. MITM set to '1' and all reserved bits are set to '1'
2. The IUT responds with a Pairing Response command, with:
- a. IO Capability set to 'KeyboardOnly' or 'DisplayOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'
3. The IUT and the Lower Tester perform phase 2 of the Passkey Entry pairing and establish an encrypted link with the generated LTK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the Lower Tester completes successfully.

The Lower Tester can encrypt the link successfully.

## SM/CEN/SCPK/BV-04-C [Passkey Entry, IUT Initiator, Secure Connections -Handle AuthReq Flag RFU Correctly]

- Test Purpose

Verify that the IUT supporting LE Secure Connections is able to perform the Passkey Entry pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Central, initiator.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO Capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardOnly' or 'KeyboardDisplay'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. All reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO Capability set to ' KeyboardOnly '
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags' and the MITM flag set to ' 1 ' , Secure Connections flag set to ' 1 ' , and all reserved bits are set to '1' .

3. The IUT and the Lower Tester perform phase 2 of the Passkey Entry pairing and establish an encrypted link with the generated LTK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the IUT completes successfully.

The link is encrypted successfully.

## SM/CEN/SCPK/BI-01-C [Passkey Entry, IUT Initiator, Secure Connections -Pairing Failed]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Passkey Entry pairing failures.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits Pairing Request command with:
- a. IO capability is set to 'KeyboardOnly' or 'DisplayOnly' or 'DisplayYesNo' or 'DisplayOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Failed command with reason code '0x03' (Authentication Requirements).
3. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

4. Execute Step 1.
5. The Lower Tester responds with a Pairing Failed command with reason code '0x08' (Unspecified Reason).
6. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

7. Execute Step 1.
8. The Lower Tester responds with a Pairing Failed command with reason code '0x05' (Pairing Not Supported).
9. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

10. Execute Step 1.
11. The Lower Tester responds with a Pairing Failed command with reason code '0x09' (Repeated Attempts).
12. The pairing process is aborted. The IUT reports the failure to the Upper Tester.
13. Execute Step 1.

14. The Lower Tester transmits Pairing Response command with:
- a. IO capability is set to ' KeyboardOnly '
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to the value indicated in the IXIT [6] for 'Bonding Flags', and the MITM flag set to '1' , Secure Connections flag set to ' 1 ' and all reserved bits are set to '0' .
15. The Lower Tester responds with a Pairing Failed command in phase 2 with reason code '0x01 (Passkey Entry Failed).
16. The pairing process is terminated. The IUT reports the failure to the Upper Tester.
- Expected Outcome

## Pass verdict

For each pairing failure, the IUT detects the failures reported by the responder and responds correctly to the Lower Tester.

For each pairing failure, the IUT aborts the pairing process and reports the failure to the Upper Tester.

## SM/CEN/SCPK/BI-02-C [Passkey Entry, IUT Initiator, Secure Connections -Failure]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Passkey Entry pairing failure as initiator correctly.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'KeyboardOnly' or 'DisplayOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '01', Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
- d. MITM set to ' 1 '
3. During phase 2 of the pass key entry pairing procedure, the Lower Tester transmits an incorrect Pairing Confirm Value.
4. The IUT detects the incorrect confirm value and sends a Pairing Failed command with '0x04 (Confirm Value Failed).
- Expected Outcome

## Pass verdict

The IUT terminates the pairing.

## SM/PER/SCPK/BI-03-C [Passkey Entry, IUT Responder, Secure Connections -Confirm Value Check Failure]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Passkey Entry pairing failure with confirm value check as responder correctly.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits a Pairing Request command with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '01', and the MITM flag set to ' 1 ', Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly' or 'KeyboardDisplay' or 'Display YesNo' or 'DisplayOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
3. During phase 2 of the pass key entry pairing procedure, the Lower Tester transmits an incorrect Pairing Confirm Value.
4. The IUT detects the incorrect confirm value and sends a Pairing Failed command with '0x04' (Confirm Value Failed).
- Expected Outcome

## Pass verdict

The IUT terminates the pairing.

## SM/PER/SCPK/BI-04-C [Passkey Entry, IUT Responder, Secure Connections -Pairing Failed]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Passkey Entry pairing failures.

- Reference

[7] 2.3.5.1, 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.

- Test Procedure
1. The Lower Tester transmits the Pairing Request command with:
- a. IO capability is set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
- d. MITM set to '1'
2. The IUT transmits the Pairing Response command with:
- a. OOB data flag set to 0x00 (OOB Authentication data not present)
- b. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
3. The Lower Tester responds with a Pairing Failed command with reason code '0x03' (Authentication Requirements).
4. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

5. Execute Steps 1 and 2.
6. The Lower Tester responds with a Pairing Failed command with reason code '0x08' (Unspecified Reason).
7. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

8. Execute Steps 1 and 2.
9. The Lower Tester responds with a Pairing Failed command with reason code '0x05' (Pairing Not Supported).
10. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

11. Execute Steps 1 and 2.
12. The Lower Tester responds with a Pairing Failed command with reason code '0x09' (Repeated Attempts).
13. The pairing process is aborted. The IUT reports the failure to the Upper Tester.
14. Execute Steps 1 and 2.
15. The Lower Tester responds with a Pairing Failed command in phase 2 with reason code '0x01' (Passkey Entry Failed).
16. The pairing process is terminated. The IUT reports the failure to the Upper Tester.
- Expected Outcome

## Pass verdict

For each pairing failure, the IUT detects the failures reported by the initiator and responds correctly to the Lower Tester.

For each pairing failure, the IUT terminates the pairing process and reports the failure to the Upper Tester.

## SM/CEN/SCPK/BV-05-C [Passkey Entry, IUT Initiator, Secure Connections -Verify Random Passkeys]

- Test Purpose

Verify that the IUT generates random passkeys supporting LE Secure Connections as Central, initiator.

- Reference

[10] 2.3.5.6.3

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure

Repeat the test procedure three times.

1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'DisplayOnly' or 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to ' 1 '; Keypress bit set to ' 1 ' if supported
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '00', the MITM flag set to '1', Secure Connections flag set to ' 1 ' and all reserved bits set to '0' ; Keypress bit set to ' 1 ' if supported by the IUT
3. During the phase 2 pairing, the IUT displays the 6-digit passkey while the Lower Tester prompts the user to enter the 6digit passkey. If the IUT's IO capabilities are 'KeyboardOnly' . the passkey is not displayed and both the IUT and the Lower Tester enter the same 6-digit passkey. If the Keypress bit is set, pairing keypress notifications are sent by the Lower Tester.
4. The IUT and the Lower Tester use the same 6-digit passkey.
5. The IUT and the Lower Tester perform phase 2 of the Passkey Entry pairing procedure and establish an encrypted link with the LTK generated in phase 2.
6. The IUT and the Lower Tester disconnect the ACL connection.
7. The Lower Tester removes bonding information with the IUT.
- Expected Outcome

## Pass verdict

The Lower Tester verifies that the IUT generates unique keys.

## SM/CEN/SCPK/BI-03-C [Passkey Entry, IUT Initiator, Secure Connections -Peer Invalid Passkey]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Passkey Entry pairing failure as initiator correctly.

- Reference

[7] 2.3.5.6.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.

- Test Procedure
1. The IUT transmits a Pairing Request command with:
- a. IO capability set to 'KeyboardOnly' or 'DisplayOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '01', Secure Connections flag set to '1' and all reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)

c.

Secure Connections flag set to '1' and all reserved bits are set to '0'

- d. MITM set to '1'
3. During phase 2 of the Passkey Entry pairing procedure, the IUT displays the 6-digit passkey while the Lower Tester enters a different 6digit passkey. If the IUT IO capabilities are 'KeyboardOnly' then both the IUT and the Lower Tester enter different passkeys.
4. The IUT detects the incorrect confirm value and sends a Pairing Failed command with 'Confirm Value Failed'.
- Expected Outcome

## Pass verdict

The IUT terminates the pairing with Confirm Value Failed.

## SM/PER/SCPK/BI-05-C [Passkey Entry, IUT Responder, Secure Connections -Peer Invalid Passkey]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Passkey Entry pairing failure as initiator correctly.

- Reference

[7] 2.3.5.6.2

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits a Pairing Request command with:
- a. IO capability set to 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. AuthReq bonding flag set to '01', Secure Connections flag set to '1' , and all reserved bits are set to '0'
2. The IUT responds with a Pairing Response command, with:
- a. IO capability set to 'DisplayOnly' or 'DisplayYesNo' or 'KeyboardDisplay' or 'KeyboardOnly'
- b. OOB data flag set to 0x00 (OOB Authentication data not present)
- c. Secure Connections flag set to '1' and all reserved bits are set to '0'
- d. MITM set to '1'

3. During phase 2 of the Passkey Entry pairing procedure, the IUT displays the 6-digit passkey while the Lower Tester enters a different 6digit passkey. If the IUT IO capabilities are 'KeyboardOnly' , then both the IUT and the Lower Tester enter different passkeys.
4. The IUT detects the incorrect confirm value and sends a Pairing Failed command with 'Confirm Value Failed'.
- Expected Outcome

## Pass verdict

The IUT terminates the pairing with Confirm Value Failed.

## 4.10.4 Out of Band (SCOB)

## SM/CEN/SCOB/BV-01-C [Out of Band, IUT Initiator, Secure Connections -Success]

- Test Purpose

Verify that the IUT supporting LE Secure Connections performs the Out-of-Band pairing procedure correctly as Central, initiator.

- Reference

[7] 2.3.5.1, 2.3.5.6.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with OOB data flag set to either 0x00 or 0x01, and Secure Connections flag set to ' 1 ' .
2. The Lower Tester responds with a Pairing Response command with Secure Connections flag set to ' 1 ' and OOB data flag set to either 0x00 or 0x01.
3. The IUT uses the 128-bit value generated by the Lower Tester as the confirm value. Similarly, the Lower Tester uses the 128-bit value generated by the IUT as the confirm value.
4. The IUT and the Lower Tester perform phase 2 of the pairing process and establish an encrypted link with an LTK generated using the OOB data in phase 2.

The test is repeated with OOB data flag combinations set to {0x01, 0x01}, {0x01, 0x00} and {0x00, 0x01}.

- Expected Outcome

## Pass verdict

The IUT can encrypt the link successfully as a Secure Connection.

The IUT indicates successful Secure Connections pairing to the Upper Tester.

- Notes

OOB data are exchanged out of band.

## SM/PER/SCOB/BV-02-C [Out of Band, IUT Responder, Secure Connections -Success]

- Test Purpose

Verify that the IUT supporting LE Secure Connections is able to perform the Out-of-Band pairing procedure correctly when acting as Peripheral, responder.

- Reference

[7] 2.3.5.1, 2.3.5.6.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits a Pairing Request command with OOB data flag set to either 0x00 or 0x01, and Secure Connections flag set to ' 1 ' .
2. The IUT responds with a Pairing Response command with Secure Connections flag set to ' 1 ' and OOB data flag set to either 0x00 or 0x01.
3. The IUT uses the 128-bit value generated by the Lower Tester as the confirm value. Similarly, the Lower Tester uses the 128-bit value generated by the IUT as the confirm value.
4. The IUT and the Lower Tester perform phase 2 of the pairing process and establish an encrypted link with an LTK generated using the OOB data in phase 2.

The test is repeated with OOB data flag combinations set to {0x01, 0x01}, {0x01, 0x00} and {0x00, 0x01}.

- Expected Outcome

## Pass verdict

The Initiator can encrypt the link successfully as Secure Connections.

The IUT indicates successful Secure Connections pairing to the Upper Tester.

## SM/PER/SCOB/BV-03-C [Out of Band, IUT Responder, Secure Connections -Handle AuthReq Flag RFU Correctly]

- Test Purpose

Verify that the IUT supporting LE Secure Connections is able to perform the Out-of-Band pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Peripheral, responder.

- Reference

[7] 2.3.5.1, 2.3.5.2, 2.3.5.6.4, 2.4.6, C.1, C.2.1

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.

- Test Procedure
1. The Lower Tester transmits Pairing Request command with:
- a. IO Capability set to any IO capability
- b. OOB data flag set to 0x01 (OOB Authentication data from remote device present)
- c. MITM set to '0', Secure Connections flag is set to ' 1 ' , and all reserved bits are set to '1'
2. The IUT responds with a Pairing Response command, with:
- a. IO Capability set to any IO capability
- b. OOB data flag set to 0x01 (OOB Authentication data present)
- c. Secure Connections flag is set to ' 1 ', All reserved bits are set to '0'
3. The IUT and the Lower Tester perform phase 2 of the OOB authenticated pairing and establish an encrypted link with the generated LTK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the Lower Tester completes successfully.

The IUT and the Lower Tester can encrypt the link successfully.

## SM/CEN/SCOB/BV-04-C [Out of Band, IUT Initiator, Secure Connections -Handle AuthReq Flag RFU Correctly]

- Test Purpose

Verify that the IUT supporting LE Secure Connections is able to perform the Out-of-Band pairing procedure when receiving additional bits set in the AuthReq flag. Reserved For Future Use bits are correctly handled when acting as Central, initiator.

- Reference

[7] 2.3.5.1, 2.3.5.6.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits Pairing Request command with:
- a. IO Capability set to any IO capability
- b. OOB data flag set to 0x01 (OOB Authentication data present)
- c. MITM set to '0', Secure Connections flag is set to ' 1 ', and all reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Response command, with:
- a. IO Capability set to any IO capability
- b. OOB data flag set to 0x01 (OOB Authentication data present)
- c. Secure Connections flag is set to ' 1 ' , and all reserved bits are set to '1' .
3. The IUT and the Lower Tester perform phase 2 of the OOB authenticated pairing and establish an encrypted link with the generated LTK.
- Expected Outcome

## Pass verdict

The encryption procedure initiated by the IUT completes successfully.

The IUT can encrypt the link successfully.

## SM/CEN/SCOB/BI-01-C [Out of Band, IUT Initiator, Secure Connections -Failure]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Out-of-Band pairing failure as initiator correctly.

- Reference

[7] 2.3.5.1, 2.3.5.6.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits Pairing Request command with:
- a. IO capability is set to any value
- b. OOB data flag set to 0x01 (OOB Authentication data from remote device present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
2. The Lower Tester responds with a Pairing Failed command with reason code '0x03' (Authentication Requirements).
3. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

4. Execute Step 1.
5. The Lower Tester responds with a Pairing Failed command with reason code '0x08' (Unspecified Reason).
6. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

7. Execute Step 1.
8. The Lower Tester responds with a Pairing Failed command with reason code '0x05' (Pairing Not Supported).
9. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

10. Execute Step 1.
11. The Lower Tester responds with a Pairing Failed command with reason code '0x09' (Repeated Attempts).
12. The pairing process is aborted. The IUT reports the failure to the Upper Tester.
13. Execute Step 1.
14. The Lower Tester transmits Pairing Response command with:
- a. IO capability is set to any value
- b. OOB data flag set to 0x01 (OOB Authentication data present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
15. The Lower Tester responds with a Pairing Failed command in phase 2 with reason code '0x02 (OOB Not Available).
16. The pairing process is terminated. The IUT reports the failure to the Upper Tester.

- Expected Outcome

## Pass verdict

For each pairing failure, the IUT detects the failures reported by the responder and responds correctly to the Lower Tester.

For each pairing failure, the IUT terminates the pairing process and reports the failure to the Upper Tester.

## SM/PER/SCOB/BI-02-C [Out of Band, IUT Responder, Secure Connections -Failure]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Out-of-Band pairing failure as responder correctly.

- Reference

[7] 2.3.5.1, 2.3.5.6.4

- Initial Condition
- -The preamble has been executed.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits Pairing Request command with:
- a. IO capability is set to any value
- b. OOB data flag set to 0x01 (OOB Authentication data present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
2. The IUT transmits Pairing Response command with:
- a. IO capability is set to any value
- b. OOB data flag set to 0x01 (OOB Authentication data from remote device present)
- c. Secure Connections flag set to ' 1 ' and all reserved bits are set to '0'
3. The Lower Tester responds with a Pairing Failed command with reason code '0x03' (Authentication Requirements).
4. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

5. Execute Steps 1 and 2.
6. The Lower Tester responds with a Pairing Failed command with reason code '0x08' (Unspecified Reason).
7. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

8. Execute Steps 1 and 2.
9. The Lower Tester responds with a Pairing Failed command with reason code '0x05' (Pairing Not Supported).
10. The pairing process is aborted. The IUT reports the failure to the Upper Tester.

Run preamble to re-establish Initial Condition.

11. Execute Steps 1 and 2.
12. The Lower Tester responds with a Pairing Failed command with reason code '0x09' (Repeated Attempts).

13. The pairing process is aborted. The IUT reports the failure to the Upper Tester.
14. Execute Steps 1 and 2.
15. The Lower Tester responds with a Pairing Failed command in phase 2 with reason code '0x02 (OOB Not Available).
16. The pairing process is terminated. The IUT reports the failure to the Upper Tester.
- Expected Outcome

## Pass verdict

For each pairing failure, the IUT detects the failures reported by the initiator and responds correctly to the Lower Tester.

For each pairing failure, the IUT terminates the pairing process and reports the failure to the Upper Tester.

## SM/PER/SCOB/BI-03-C [Out of Band, IUT Responder, Secure Connections -Pairing Failed]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Out-of-Band pairing failures.

- Reference

[7] 2.3.5.1, 2.3.5.6.4

- Initial Condition
- -The preamble has been executed.
- -The Lower Tester has sent the wrong OOB data to the IUT.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits a Pairing Request command with OOB data flag set to 0x01 and Secure Connections flag set to ' 1 ' .
2. Responder responds with a Pairing Response command, with OOB data flag to set 0x01 and Secure Connections flag set to ' 1 ' .
3. The IUT detects the incorrect confirm value.
4. The Lower Tester transmits a Pairing Random command.
5. The IUT responds with a Pairing Failed ("Confirm Value Failed") command; the Lower Tester initiates disconnect.
- Expected Outcome

## Pass verdict

The IUT detects the mismatch of confirm value and sends 'Pairing Failed'.

## SM/CEN/SCOB/BI-04-C [Out of Band, IUT Initiator, Secure Connections -Pairing Failed]

- Test Purpose

Verify that the IUT supporting LE Secure Connections handles Out-of-Band pairing failures.

- Reference

[7] 2.3.5.1, 2.3.5.6.4

- Initial Condition
- -The preamble has been executed.
- -The Lower Tester has sent the wrong OOB data to the IUT.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Procedure
1. The IUT transmits a Pairing Request command with OOB data flag set to 0x01 and Secure Connections flag set to ' 1 ' .
2. The Lower Tester responds with a Pairing Response command, with OOB data flag to set 0x01 and Secure Connections flag set to ' 1 ' .
3. The IUT detects the incorrect confirm value and sends a Pairing Failed ("Confirm Value Failed") command; the Lower Tester initiates disconnect.
- Expected Outcome

## Pass verdict

The IUT detects the mismatch of confirm value and sends 'Pairing Failed'.

## 4.10.5 Cross Transport Key Derivation (SCCT)

## 4.10.5.1 Cross Transport Key Derivation, IUT Initiator, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h6

- Test Purpose

Verify that the IUT supporting LE Secure Connections and being a BR/EDR/LE device can derive the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h6.

- Reference

[7] 2.3.5.7, 2.4.2.5

- Initial Condition
- -The IUT and the Lower Tester have paired over BR/EDR using Secure Connections.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Case Configuration

| Test Case | CSRK Allowed |
| SM/CEN/SCCT/BV-03-C [Cross Transport Key Derivation, IUT Initiator, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h6, CSRK] | Yes |
| SM/CEN/SCCT/BV-10-C [Cross Transport Key Derivation, IUT Initiator, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h6, No CSRK] | No |

Table 4.10: Cross Transport Key Derivation, IUT Initiator, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h6 tests

- Test Procedure
1. The IUT transmits Pairing Request command with the CT2 bit in the AuthReq field set to either value, and the EncKey bit in the Initiator Key Distribution/Generation field set to '1' on SMP over BR/EDR.

2. The Lower Tester responds with a Pairing Response command with the CT2 bit in the AuthReq field set to '0', and the EncKey bit in the Responder Key Distribution/Generation field set to '1' on SMP over BR/EDR.
3. The IUT optionally distributes the negotiated keys such as the IRK. The CSRK may be distributed if allowed in Table 4.10.
4. The Lower Tester or the IUT disconnects the BR/EDR transport.
5. The IUT and the Lower Tester connect on the LE transport and encrypt the link using the derived LTK.
- Expected Outcome

## Pass verdict

The IUT derives the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h6.

## Fail verdict

If the CSRK is not allowed in Table 4.10, in Step 3, the IUT distributes the CSRK.

## 4.10.5.2 Cross Transport Key Derivation, IUT Responder, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h6

- Test Purpose

Verify that the IUT supporting LE Secure Connections and being a BR/EDR/LE device can derive the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h6.

- Reference

[7] 2.3.5.7, 2.4.2.5

- Test Case Configuration
- Initial Condition
- -The IUT and the Lower Tester have paired over BR/EDR using Secure Connections.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Procedure
1. The Lower Tester transmits Pairing Request command with the CT2 bit in the AuthReq field set to '0', and the EncKey bit in the Initiator Key Distribution/Generation field set to '1' on SMP over BR/EDR.
2. The IUT responds with a Pairing Response command with the CT2 bit in the AuthReq field set to either value, and the EncKey bit in the Responder Key Distribution/Generation field set to '1' on SMP over BR/EDR.

Table 4.11: Cross Transport Key Derivation, IUT Responder, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h6 tests

| Test Case | CSRK Allowed |
| SM/PER/SCCT/BV-04-C [Cross Transport Key Derivation, IUT Responder, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h6, CSRK] | Yes |
| SM/PER/SCCT/BV-11-C [Cross Transport Key Derivation, IUT Responder, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h6, No CSRK] | No |

3. The IUT optionally distributes the negotiated keys such as the IRK. The CSRK may be distributed if allowed in Table 4.11.
4. The Lower Tester or the IUT disconnects the BR/EDR transport.
5. The IUT and the Lower Tester connect on the LE transport and encrypt the link using the derived LTK.
- Expected Outcome

## Pass verdict

The IUT derives the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h6.

## Fail verdict

If the CSRK is not allowed in Table 4.11, in Step 3, the IUT distributes the CSRK.

## 4.10.5.3 Cross Transport Key Derivation, IUT Initiator, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h7

- Test Purpose

Verify that the IUT supporting LE Secure Connections and being a BR/EDR/LE device can derive the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h7.

- Reference

[7] 2.3.5.7, 2.4.2.5

- Initial Condition
- -The IUT and the Lower Tester have paired over BR/EDR using Secure Connections.
- -The IUT is Central. The Lower Tester is Peripheral.
- Test Case Configuration

Table 4.12: Cross Transport Key Derivation, IUT Initiator, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h7 tests

| Test Case | CSRK Allowed |
| SM/CEN/SCCT/BV-05-C [Cross Transport Key Derivation, IUT Initiator, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h7, CSRK] | Yes |
| SM/CEN/SCCT/BV-11-C [Cross Transport Key Derivation, IUT Initiator, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h7, No CSRK] | No |

## · Test Procedure

1. The IUT transmits Pairing Request command with the CT2 bit in the AuthReq field set to '1', and the EncKey bit in the Initiator Key Distribution/Generation field set to '1' on SMP over BR/EDR.
2. The Lower Tester responds with a Pairing Response command with the CT2 bit in the AuthReq field set to '1', and the EncKey bit in the Responder Key Distribution/Generation field set to '1' on SMP over BR/EDR.
3. The IUT optionally distributes the negotiated keys such as the IRK. The CSRK may be distributed if allowed in Table 4.12.
4. The Lower Tester or the IUT disconnects the BR/EDR transport.
5. The IUT and the Lower Tester connect on the LE transport and encrypt the link using the derived LTK.

- Expected Outcome

## Pass verdict

The IUT derives the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h7.

## Fail verdict

If the CSRK is not allowed in Table 4.12, in Step 3, the IUT distributes the CSRK.

## 4.10.5.4 Cross Transport Key Derivation, IUT Responder, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h7

- Test Purpose

Verify that the IUT supporting LE Secure Connections and being a BR/EDR/LE device can derive the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h7.

- Reference

[7] 2.3.5.7, 2.4.2.5

- Initial Condition
- -The IUT and the Lower Tester have paired over BR/EDR using Secure Connections.
- -The IUT is Peripheral. The Lower Tester is Central.
- Test Case Configuration
- Test Procedure
1. The Lower Tester transmits Pairing Request command with the CT2 bit in the AuthReq field set to '1', and the EncKey bit in the Initiator Key Distribution/Generation field set to '1' on SMP over BR/EDR.
2. The IUT responds with a Pairing Response command with the CT2 bit in the AuthReq field set to '1', and the EncKey bit in the Responder Key Distribution/Generation field set to ' 1 ' on SMP over BR/EDR.
3. The IUT optionally distributes the negotiated keys such as the IRK. The CSRK may be distributed if allowed in Table 4.13.
4. The Lower Tester or the IUT disconnects the BR/EDR transport.
5. The IUT and the Lower Tester connect on the LE transport and encrypt the link using the derived LTK.
- Expected Outcome

Table 4.13: Cross Transport Key Derivation, IUT Responder, Secure Connections -Derive LE LTK from BR/EDR Link Key Using h7 tests

| Test Case | CSRK Allowed |
| SM/PER/SCCT/BV-06-C [Cross Transport Key Derivation, IUT Responder, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h7, CSRK] | Yes |
| SM/PER/SCCT/BV-12-C [Cross Transport Key Derivation, IUT Responder, Secure Connections - Derive LE LTK from BR/EDR Link Key Using h7, No CSRK] | No |

## Pass verdict

The IUT derives the LE LTK from the BR/EDR Link Key using Link Key Conversion Function h7.

## Fail verdict

If the CSRK is not allowed in Table 4.13, in Step 3, the IUT distributes the CSRK.

## 4.10.5.5 Cross Transport Key Derivation, IUT Initiator, Secure Connections -Derive BR/EDR Link Key from LE Unmasked LTK

- Test Purpose

Verify that the IUT supporting LE Secure Connections and being a BR/EDR/LE device can derive the BR/EDR Link Key from the LE Unmasked LTK using the specified Link Key Conversion Function.

- Reference

[7] 2.3.5.7, 2.4.2.4

- Initial Condition
- -The IUT is Central. The Lower Tester is Peripheral.
- -The Lower Tester supports a 7 octet encryption key size.
- Test Case Configuration
- Test Procedure
1. The IUT transmits a Pairing Request command with the SC bit in the AuthReq field set to '1', the CT2 bit in the AuthReq field set to '1', and the LinkKey bit in the Initiator Key Distribution/Generation field set to '1' on SMP over LE.
2. The Lower Tester responds with a Pairing Response command with the SC bit in the AuthReq field set to '1', the CT2 bit in the AuthReq field set as specified in Table 4.14, the Maximum Encryption Key Size field set to 7, and the LinkKey bit in the Responder Key Distribution/Generation field set to ' 1 ' on SMP over LE. The Lower Tester saves the value of the key derived from the secret before the key is shortened.
3. The IUT optionally distributes the negotiated keys such as the IRK. The CSRK may be distributed if allowed in Table 4.14.
4. The Lower Tester or the IUT disconnects the LE transport.
5. The IUT and the Lower Tester connect on the BR/EDR transport and encrypt the link using the derived Link Key and either E0 or AES-CCM encryption as supported by the IUT. The Lower Tester uses the saved key from Step 2 as the link key.
- Expected Outcome

Table 4.14: Cross Transport Key Derivation, IUT Initiator, Secure Connections -Derive BR/EDR Link Key from Unmasked LE LTK test cases

| Test Case | Conversion Function | CT2 bit | CSRK Allowed |
| SM/CEN/SCCT/BV-07-C | h6 | 0 | Yes |
| SM/CEN/SCCT/BV-09-C | h7 | 1 | Yes |
| SM/CEN/SCCT/BV-12-C | h6 | 0 | No |
| SM/CEN/SCCT/BV-13-C | h7 | 1 | No |

## Pass verdict

The IUT derives the BR/EDR Link Key from the LE LTK using the Link Key Conversion Function specified in Table 4.14.

In Step 5, the IUT is able to connect to the Lower Tester using the derived key.

## Fail verdict

If the CSRK is not allowed in Table 4.14, in Step 3, the IUT distributes the CSRK.

## 4.10.5.6 Cross Transport Key Derivation, IUT Responder, Secure Connections -Derive BR/EDR Link Key from LE Unmasked LTK

- Test Purpose

Verify that the IUT supporting LE Secure Connections and being a BR/EDR/LE device can derive the BR/EDR Link Key from the LE Unmasked LTK using the specified Link Key Conversion Function.

- Reference

[7] 2.3.5.7, 2.4.2.4

- Initial Condition
- -The IUT is Peripheral. The Lower Tester is Central.
- -The Lower Tester supports a 7 octet encryption key size.
- Test Case Configuration
- Test Procedure
1. The Lower Tester transmits a Pairing Request command with the SC bit in the AuthReq field set to '1', the CT2 bit in the AuthReq field set as specified in Table 4.15, the Maximum Encryption Key Size field set to 7, and the LinkKey bit in the Initiator Key Distribution/Generation field set to ' 1 ' on SMP over LE.
2. The IUT responds with a Pairing Response command with the SC bit in the AuthReq field set to '1', the CT2 bit in the AuthReq field set to '1', and the LinkKey bit in the Responder Key Distribution/Generation field set to ' 1 ' on SMP over LE. The Lower Tester saves the value of the key derived from the secret before the key is shortened.
3. The IUT optionally distributes the negotiated keys such as the IRK. The CSRK may be distributed if allowed in Table 4.15.
4. The Lower Tester or the IUT disconnects the LE transport.
5. The IUT and the Lower Tester connect on the BR/EDR transport and encrypt the link using the derived Link Key and either E0 or AES-CCM encryption as supported by the IUT. The Lower Tester uses the saved key from Step 2 as the link key.
- Expected Outcome

Table 4.15: Cross Transport Key Derivation, IUT Responder, Secure Connections -Derive BR/EDR Link Key from Unmasked LE LTK

| Test Case | Conversion Function | CT2 bit | CSRK Allowed |
| SM/PER/SCCT/BV-08-C | h6 | 0 | Yes |
| SM/PER/SCCT/BV-10-C | h7 | 1 | Yes |
| SM/PER/SCCT/BV-13-C | h6 | 0 | No |
| SM/PER/SCCT/BV-14-C | h7 | 1 | No |

## Pass verdict

The IUT derives the BR/EDR Link Key from the LE LTK using the Link Key Conversion Function specified in Table 4.15.

In Step 5, the IUT is able to connect to the Lower Tester using the derived key.

## Fail verdict

If the CSRK is not allowed in Table 4.15, in Step 3, the IUT distributes the CSRK.

## 5 Test case mapping

The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.

The columns for the TCMT are defined as follows:

Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for SM [2].

If a test case is mandatory within the respective layer, then the y/x reference is omitted.

Feature: A brief, informal description of the feature being tested.

Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [1].

For the purpose and structure of the ICS/IXIT, refer to [1].

| Item | Feature | Test Case(s) |
| SM 6/1 AND CORE 2b/62 | Signing - Generation, v6.2 or earlier | SM/SIGN/BV-01-C |
| SM 6/2 AND CORE 2b/62 | Signing - Resolving, v6.2 or earlier | SM/SIGN/BV-03-C SM/SIGN/BI-01-C |
| (SM 4a/2 OR SM 4b/2) AND SM 6/2 AND CORE 2a/62 | Signing - Resolving, Ignore repeated SignCounter, Core v6.2 or later | SM/SIGN/BI-02-C |
| SM 1/1 | Initiator tests | SM/CEN/PROT/BV-01-C |
| SM 1/1 | Central Respond to Encryption Request | SM/CEN/PIS/BV-03-C |
| SM 2a/1 AND SM 7a/1 | Pairing type and key being distributed, Central Key Distribution - Encryption Key bit | SM/CEN/KDU/BV-06-C |
| SM 2a/1 AND SM 7a/2 | Pairing type and key being distributed, Central Key Distribution - Identity Key bit | SM/CEN/KDU/BV-05-C |
| SM 2a/1 AND SM 7a/3 AND CORE 2b/62 | Pairing type and key being distributed, Central Key Distribution - Signing Key bit, v6.2 or earlier | SM/CEN/KDU/BV-04-C |
| SM 2a/2 AND SM 7a/2 | Pairing type and key being distributed, Central Key Distribution - Identity Key bit, LE Secure Connections | SM/CEN/KDU/BV-10-C |
| SM 2a/2 AND SM 7a/3 AND CORE 2b/62 | Pairing type and key being distributed, Central Key Distribution - Signing Key bit, LE Secure Connections, v6.2 or earlier | SM/CEN/KDU/BV-11-C |
| SM 1/1 AND SM 2a/1 | Initiate Encryption key size negotiation | SM/CEN/EKS/BV-01-C SM/CEN/EKS/BI-01-C |
| SM 1/1 AND SM 4a/1 | Initiate Just Works pairing with no MITM | SM/CEN/JW/BV-01-C |
| SM 1/1 AND SM 4a/1 | Initiate Just Works pairing | SM/CEN/JW/BI-01-C SM/CEN/JW/BV-05-C SM/CEN/JW/BI-04-C |

| Item | Feature | Test Case(s) |
| SM 1/1 AND SM 4a/2 | Initiate Passkey Entry pairing | SM/CEN/PKE/BI-01-C SM/CEN/PKE/BI-02-C SM/CEN/PKE/BV-01-C |
| SM 1/1 AND SM 4a/2 AND CORE 2a/62 | Initiate Passkey Entry pairing, Core v6.2 or later | SM/CEN/PKE/BV-05-C |
| SM 1/1 AND SM 4a/2 AND SM 4a/1 | Initiate pairing - Unauthenticated key | SM/CEN/PKE/BV-04-C |
| SM 1/1 AND SM 4a/3 AND CORE 2b/62 | Initiate OOB pairing, v6.2 and earlier | SM/CEN/OOB/BI-01-C SM/CEN/OOB/BV-01-C |
| SM 1/1 AND SM 4a/3 AND CORE 2a/63 | Initiate OOB pairing, v6.3 and later | SM/CEN/OOB/BV-10-C |
| SM 1/1 AND SM 4a/3 AND SM 4a/2 | Initiate pairing, only IUT has OOB data | SM/CEN/OOB/BV-03-C |
| SM 1/1 AND SM 4a/2 AND NOT SM 4a/3 | Initiate pairing, only Lower Tester has OOB data | SM/CEN/OOB/BV-05-C |
| SM 1/1 AND SM 4a/1 AND NOT SM 4a/3 | Initiate pairing, only Lower Tester has OOB data | SM/CEN/OOB/BV-07-C |
| SM 1/1 AND SM 4a/3 AND SM 4a/1 | Initiate pairing, only IUT has OOB data | SM/CEN/OOB/BV-09-C |
| SM 5/4 | Peripheral Initiated Security - Central response | SM/CEN/PIS/BV-02-C |
| SM 1/1 AND SM 4b/1 | Just Works, IUT Initiator, Secure Connections | SM/CEN/SCJW/BV-01-C SM/CEN/SCJW/BV-04-C SM/CEN/SCJW/BI-01-C |
| SM 1/1 AND SM 4b/2 | Passkey Entry, IUT Initiator, Secure Connections | SM/CEN/SCPK/BV-01-C SM/CEN/SCPK/BV-04-C SM/CEN/SCPK/BI-01-C SM/CEN/SCPK/BI-02-C |
| SM 1/1 AND SM 4b/2 AND CORE 2a/62 | Passkey Entry, IUT Initiator, Secure Connections, Core v6.2 or later | SM/CEN/SCPK/BV-05-C |
| SM 1/1 AND SM 4b/2 AND CORE 2a/63 | Passkey Entry, IUT Initiator, Secure Connections, Core v6.3 or later | SM/CEN/SCPK/BI-03-C |
| SM 1/1 AND SM 4b/3 | Out of Band, IUT Initiator, Secure Connections | SM/CEN/SCOB/BV-01-C SM/CEN/SCOB/BI-04-C SM/CEN/SCOB/BV-04-C SM/CEN/SCOB/BI-01-C |
| SM 1/1 AND SM 2a/2 AND CORE 2b/54 | Central Public Key Validation - LE Secure Connections - Invalid Public Key, v5.4 or earlier | SM/CEN/KDU/BI-01-C |
| SM 1/1 AND SM 2a/2 AND CORE 2a/60 | Central Public Key Validation - LE Secure Connections - Invalid Public Key, v6.0 or later | SM/CEN/KDU/BI-04-C |
| SM 8a/2 AND CORE 2b/62 | Cross Transport Key Derivation, IUT Initiator, Secure Connections, Link Key Conversion Function h6, Derive LE LTK from BR/EDR, v6.2 or earlier | SM/CEN/SCCT/BV-03-C |

| Item | Feature | Test Case(s) |
| SM 8a/2 AND CORE 2a/63 | Cross Transport Key Derivation, IUT Initiator, Secure Connections, Link Key Conversion Function h6, Derive LE LTK from BR/EDR, v6.3 or later | SM/CEN/SCCT/BV-10-C |
| SM 8a/3 AND SM 5/5 AND CORE 2b/62 | Cross Transport Key Derivation, IUT Initiator, Secure Connections, Link Key Conversion Functions h6 and h7, Derive BR/EDR Link Key from LE LTK, v6.2 or earlier | SM/CEN/SCCT/BV-07-C SM/CEN/SCCT/BV-09-C |
| SM 8a/3 AND SM 5/5 AND CORE 2a/63 | Cross Transport Key Derivation, IUT Initiator, Secure Connections, Link Key Conversion Functions h6 and h7, Derive BR/EDR Link Key from LE LTK, v6.3 or later | SM/CEN/SCCT/BV-12-C SM/CEN/SCCT/BV-13-C |
| SM 8a/2 AND SM 5/5 AND CORE 2b/62 | Cross Transport Key Derivation, IUT Initiator, Secure Connections, Link Key Conversion Function h7, Derive LE LTK from BR/EDR Link Key, v6.2 or earlier | SM/CEN/SCCT/BV-05-C |
| SM 8a/2 AND SM 5/5 AND CORE 2a/63 | Cross Transport Key Derivation, IUT Initiator, Secure Connections, Link Key Conversion Function h7, Derive LE LTK from BR/EDR Link Key, v6.3 or later | SM/CEN/SCCT/BV-11-C |
| SM 1/1 AND SM 4a/1 AND CORE 2a/62 | Initiate Just Works pairing, Core v6.2 or later | SM/CEN/JW/BI-06-C |
| SM 1/1 AND SM 4a/2 AND CORE 2a/62 | Initiate Passkey Entry pairing, Core v6.2 or later | SM/CEN/PKE/BI-03-C |
| SM 1/2 | Responder tests | SM/PER/PROT/BV-02-C |
| SM 1/2 AND SM 5/3 | Peripheral Initiated Security | SM/PER/PIS/BV-01-C SM/PER/PIS/BV-02-C |
| SM 2a/1 AND SM 7b/1 | Pairing type and key being distributed, Peripheral Key Distribution - Encryption Key bit | SM/PER/KDU/BV-01-C |
| SM 2a/1 AND SM 7b/2 | Pairing type and key being distributed, Peripheral Key Distribution - Identity Key bit | SM/PER/KDU/BV-02-C |
| SM 2a/1 AND (SM 7b/1 OR SM 7b/2 OR SM 7b/3) AND CORE 2a/53 | Peripheral Key Distribution - Legacy pairing, Key Rejected | SM/PER/KDU/BI-02-C |
| SM 2a/2 AND (SM 7b/2 OR SM 7b/3) AND CORE 2a/53 | Peripheral Key Distribution - LE Secure Connections, Key Rejected | SM/PER/KDU/BI-03-C |
| SM 2a/1 AND SM 7b/3 AND CORE 2b/62 | Pairing type and key being distributed, Peripheral Key Distribution - Signing Key bit, v6.2 or earlier | SM/PER/KDU/BV-03-C |
| SM 1/2 | Encryption Key size negotiation - Respond | SM/PER/EKS/BV-02-C SM/PER/EKS/BI-02-C |
| SM 1/2 AND SM 4a/1 | Respond to Just Works pairing | SM/PER/JW/BV-02-C SM/PER/JW/BI-03-C |
| SM 1/2 AND SM 4a/1 | Respond to Just Works pairing with Unauthenticated no MITM protection | SM/PER/JW/BI-02-C |

| Item | Feature | Test Case(s) |
| SM 1/2 AND SM 4a/2 | Respond to Pass key Entry pairing | SM/PER/PKE/BI-03-C SM/PER/PKE/BV-02-C |
| SM 1/2 AND SM 4a/2 AND SM 4a/1 AND CORE 2b/61 | Respond to pairing - Unauthenticated key, v6.1 and earlier | SM/PER/PKE/BV-05-C |
| SM 1/2 AND SM 4a/2 AND SM 4a/1 AND CORE 2a/62 | Respond to pairing - Unauthenticated key, v6.2 and later | SM/PER/PKE/BV-06-C |
| SM 1/2 AND SM 4a/3 AND CORE 2b/62 | Respond to OOB pairing - Both sides have OOB data, v6.2 and earlier | SM/PER/OOB/BI-02-C SM/PER/OOB/BV-02-C |
| SM 1/2 AND SM 4a/3 AND CORE 2a/63 | Respond to OOB pairing - Both sides have OOB data, v6.3 and later | SM/PER/OOB/BV-11-C |
| SM 1/2 AND SM 4a/3 AND SM 4a/2 | Respond to pairing - IUT has OOB data | SM/PER/OOB/BV-04-C |
| SM 1/2 AND SM 2a/1 | Pairing type and key being distributed, Re- encrypt an encrypted link with LTK | SM/PER/KDU/BV-07-C |
| SM 7b/2 AND SM 2a/2 | Pairing type and key being distributed, Peripheral Key Distribution - Identity Key bit, LE Secure Connections | SM/PER/KDU/BV-08-C |
| SM 7b/3 AND SM 2a/2 AND CORE 2b/62 | Pairing type and key being distributed, Peripheral Key Distribution - Signing Key bit, LE Secure Connections, v6.2 or earlier | SM/PER/KDU/BV-09-C |
| SM 1/2 AND SM 4a/2 AND NOT SM 4a/3 | Respond to OOB pairing where IUT lacks OOB data | SM/PER/OOB/BV-06-C |
| SM 1/2 AND SM 4a/1 AND NOT SM 4a/3 | Respond to OOB pairing where IUT lacks OOB data | SM/PER/OOB/BV-08-C |
| SM 1/2 AND SM 4a/3 AND SM 4a/1 | Respond to pairing - IUT has OOB data | SM/PER/OOB/BV-10-C |
| SM 1/2 AND SM 4b/1 | Just Works, IUT Responder, Secure Connections | SM/PER/SCJW/BV-02-C SM/PER/SCJW/BV-03-C SM/PER/SCJW/BI-02-C |
| SM 1/2 AND SM 4b/2 | Passkey Entry, IUT Responder, Secure Connections | SM/PER/SCPK/BV-02-C SM/PER/SCPK/BV-03-C SM/PER/SCPK/BI-03-C SM/PER/SCPK/BI-04-C |
| SM 1/2 AND SM 4b/2 AND CORE 2a/63 | Passkey Entry, IUT Responder, Secure Connections, v6.3 or later | SM/PER/SCPK/BI-05-C |
| SM 1/2 AND SM 4b/3 | Out of Band, IUT Responder, Secure Connections | SM/PER/SCOB/BV-02-C SM/PER/SCOB/BV-03-C SM/PER/SCOB/BI-02-C SM/PER/SCOB/BI-03-C |
| SM 1/2 AND SM 2a/2 AND CORE 2b/54 | Peripheral Public Key Validation - LE Secure Connections - Invalid Public Key, v5.4 or earlier | SM/PER/KDU/BI-01-C |
| SM 1/2 AND SM 2a/2 AND CORE 2a/60 | Peripheral Public Key Validation - LE Secure Connections - Invalid Public Key, v6.0 or later | SM/PER/KDU/BI-04-C |

| Item | Feature | Test Case(s) |
| SM 8b/2 AND CORE 2b/62 | Cross Transport Key Derivation, IUT Responder, Secure Connections, Link Key Conversion Function h6, Derivation of LE LTK from BR/EDR Link Key, v6.2 or earlier | SM/PER/SCCT/BV-04-C |
| SM 8b/2 AND CORE 2a/63 | Cross Transport Key Derivation, IUT Responder, Secure Connections, Link Key Conversion Function h6, Derivation of LE LTK from BR/EDR Link Key, v6.3 or later | SM/PER/SCCT/BV-11-C |
| SM 8b/3 AND SM 5/5 AND CORE 2b/62 | Cross Transport Key Derivation, IUT Responder, Secure Connections, Link Key Conversion Functions h6 and h7, Derive BR/EDR Link Key from LE LTK, v6.2 or earlier | SM/PER/SCCT/BV-08-C SM/PER/SCCT/BV-10-C |
| SM 8b/3 AND SM 5/5 AND CORE 2a/63 | Cross Transport Key Derivation, IUT Responder, Secure Connections, Link Key Conversion Functions h6 and h7, Derive BR/EDR Link Key from LE LTK, v6.3 or later | SM/PER/SCCT/BV-13-C SM/PER/SCCT/BV-14-C |
| SM 5/5 AND SM 8b/2 AND CORE 2b/62 | Cross Transport Key Derivation, IUT Responder, Secure Connections, Link Key Conversion Function h7, Derivation of LE LTK from BR/EDR Link Key, v6.2 or earlier | SM/PER/SCCT/BV-06-C |
| SM 5/5 AND SM 8b/2 AND CORE 2a/63 | Cross Transport Key Derivation, IUT Responder, Secure Connections, Link Key Conversion Function h7, Derivation of LE LTK from BR/EDR Link Key, v6.3 or later | SM/PER/SCCT/BV-12-C |

Table 5.1: Test case mapping

## 6 Revision history and acknowledgments
