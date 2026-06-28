## Matter Test Plan

Version 1.6-release-updated, 2026-06-02 15:46:29 -0700: Approved

## Introduction

## Scope

This test plan covers the tests for Matter.

## Purpose

Describe the tests to be performed for supported Matter features. The tests are split over two documents:

- Core Test Plan (this document)
- Cluster Test Plan (see Matter Cluster Test Plan)

## Prerequisites

A test plan may have prerequisites that should be met before the test plan can be executed with the expected results. Examples of prerequisites include dependency certifications and security conformance.

| Ref | Authority | Doc No. | Test Plan Name | Prerequisites |
| TBD | TBD | TBD | TBD | TBD |

## References

## Matter Documents

| Ref | Authority | Doc No. | Specification Name | Test Plan Name |
| [C1] | Connectivity Standards Alliance / Matter | Github-Latest | Matter Specification - Section 4 | Secure Channel Test Plan |
| [C1] | Connectivity Standards Alliance / Matter | Github-Latest | Matter Specification - Section 5 | Device Discovery Test Plan |
| [C1] | Connectivity Standards Alliance / Matter | Github-Latest | Matter Specification - Section 6 | Device Attestation Test Plan |
| [C1] | Connectivity Standards Alliance / Matter | Github-Latest | Matter Specification - Section 11 | Device Management Test Plan |

| Ref | Authority | Doc No. | Specification Name | Test Plan Name |
| [C1] | Connectivity Standards Alliance / Matter | Github-Latest | Matter Specification - Section 12 | Multiple Administrators Test Plan |
| [C1] | Connectivity Standards Alliance / Matter | Github-Latest | Matter Specification - Section 9.12 | Bridge Test Plan |

| Reference | Reference Location/URL | Description |
| [MatterCluste rTestPlan] | https://groups.csa-iot.org/wg/ members-all/document/ folder/2269 | Matter Clusters Test Plan |

## Dependency Certification Documents

| Ref | Authority | Doc No. | Specification Name |
| TBD | TBD | TBD | TBD |

## Definitions

## Acronyms

| Acronym or Abbreviation | Description |
| PICS | Protocol Implementation Conformance Statement(s). |
| PIXIT | Protocol Implementation eXtra Information for Testing |
| DUT | Device under test |
| PAKE | Password Authenticated Key Exchange |
| PASE | Passcode Authenticated Session Establishment |
| PBKDF | Password-Based Key Derivation Function |
| MIC | Message integrity check |
| CASE | Certificate Authenticated Session Establishment |
| TLV | Tag Length Value |
| TH | Test Harness |
| CSR | Certificate Signing Request |

## Glossary

| Term | Description |
| Node | An addressable entity which supports the Matter protocol stack and (once Commissioned) has its own operational Node ID and Operational Credential. Example: Matter app(lication)s on a mobile phone are Nodes, the mobile phone itself is a Device. |
| Controller | A Role of a Node that has permissions to enable it to control one or more Nodes |

## Identifications/Identifiers

Explanation of test case IDs, failure IDs, any other UUIDs

## Conformance Levels

Reference: IETF RFC-2119

| Keyword | Synonyms / Variants | Meaning |
| SHOULD NOT | NOT RECOMMENDED | May be acceptable in particular circumstances, but implications should be understood and weighed carefully before implementation. |

## Diagram Definitions

This section defines picture/symbol element meaning for diagrams used later in this document.

## Test Setup

This section will define any required steps necessary to set up an environment that will be used for subsequent execution of test cases contained in this test plan. Examples include the usage of particular certificates, internet/cloud connectivity setup.

Test harness setup will be covered in the test tools documentation.

## Platform Certification

A platform certification is performed with PICS\_PLAT\_CERT = 1 and PICS\_PLAT\_CERT\_TESTS\_DONE = 0. It serves as a foundation for a Derived Matter Product, which certifies additional clusters and functionalities. The Matter Certification program identifies which test cases as being either required for Platform Certification or DMP certification by tagging them with one of the following tags:

- platform: Test cases that are required for platform certification only (Platform and Standard).
- product: Test cases that are required for product certification only (DMP and Standard).
- both: Test cases that are required for all certification types (Platform, DMP, and Standard).

## Derived Matter Product Certification

A DMP uses a Matter Certified Platform to certify a product with additional clusters and functionalities. It is performed with PICS\_PLAT\_CERT = 0 and PICS\_PLAT\_CERT\_TESTS\_DONE = 1 to indicate that the certification is being run on top of a certified platform. A certified DMP has the same rights and requirements as a Matter Product, including logo usage and DCL registration. It must indicate the Matter Platform Certification ID and version used and have access to all applicable test results.

## Standard Matter Product Certification

A standard Matter product certification is performed with PICS\_PLAT\_CERT = 0 and PICS\_PLAT\_CERT\_TESTS\_DONE = 0. This is the most common certification type, where the product is certified without relying on a platform certification. All required test cases must be executed regardless of the test case tagging.

## Timing and Tolerance Considerations

## NOTE

This section summarizes timing tolerances and clock allowances relevant to test cases. The same information is also present in the shared cluster\_common.adoc front matter for consistency across test plans.

There are two main types of timing tolerances:

## 1. Action-at-End Tolerance:

- Actions-at-End tolerances apply to tests that check that an action occurs at the end of a timer (e.g., a device closes a valve after a set period, a failsafe timer expires, a commissioning window is closed).
- The Action-at-End tolerance permits the expected action to occur at the expected time +/- the tolerance
- The tolerance for these actions is {clockAllowancePercent} of the set timer time or {clockAllowanceMinMs}, whichever is larger

## 2. Action-Over-Time Tolerance:

- Action-over-time tolerances apply to tests where the device changes occur continuously over a set period (for example, a light bulb ramping or changing color).
- Tests checking for value changes during the ongoing operation use a larger tolerance to account for both clock differences and algorithmic differences in applying the requested changes.
- Tests that use Action-Over-Time tolerances normally apply a tolerance of 15% of the expected change, calculated as follows:

For an action started at time T ₀ with a starting value V ₀ and an action-overtime change rate C (where C = Δ V ÷ Δ T), the expected change in value Δ V ₁ at time T ₁ is:

```
Δ V ₁ = C × (T ₁ T ₀ )
```

The allowed range of expected values for V ₁ at time T ₁ is:

```
V ₁ = V ₀ ± ( Δ V ₁ × tol)
```

where *tol* is the tolerance value and is normally 0.15.

It is important to differentiate between these two types of tolerances when writing or interpreting test cases. The default clock allowance applies to action-at-end scenarios, while action-over-time tolerances should be explicitly stated where used.

## Chapter 1. TestEventTrigger Overview

## 1.1. EventTrigger Encoding

This details the encoding of the EventTrigger field used in the TestEventTrigger command.

The EventTrigger is defined as a uint64, but the underlying encoding follows this schema:

0xYYYY\_XXXX\_ZZZZ\_ZZZZ

## 1.1.1. YYYY Value

The cluster ID related to the trigger event.

## 1.1.2. XXXX Value

The targeting endpoint ID for the specific trigger event.

A value of 0xFFFF SHALL trigger the event on all supported endpoints.

A value of 0x0000 MAY trigger the event on the first supported endpoint (in some legacy devices).

## 1.1.3. ZZZZ\_ZZZZ Value

The cluster-specific trigger event value.

## 1.2. EventTrigger Values

The following EventTrigger values are defined:

| ICD Management | ICD Management |
| PIXIT.ICDM.TEST_EVENT_TRIGGER | Triggered Event |
| 0x0046_XXXX_0000_0001 | Adds the test event trigger ActiveMode requirement |
| 0x0046_XXXX_0000_0002 | Removes the test event trigger ActiveMode requirement |
| 0x0046_XXXX_0000_0003 | Invalidate ICD half counter values |
| 0x0046_XXXX_0000_0004 | Invalidate ICD all counter values |
| Smoke CO Alarm | Smoke CO Alarm |
| PIXIT.SMOKECO.TEST_EVENT_TRIGGER | Triggered Event |
| 0x005c_XXXX_0000_0090 | Warning Smoke Alarm Test Event |
| 0x005c_XXXX_0000_0091 | Warning CO Alarm Test Event |

| 0x005c_XXXX_0000_0092 | Interconnect Smoke Alarm Test Event |
| 0x005c_XXXX_0000_0093 | Hardware Fault Alert Test Event |
| 0x005c_XXXX_0000_0094 | Interconnect CO Alarm Test Event |
| 0x005c_XXXX_0000_0095 | Warning Battery Alert Test Event |
| 0x005c_XXXX_0000_0096 | Contamination State (High) Test Event |
| 0x005c_XXXX_0000_0097 | Contamination State (Low) Test Event |
| 0x005c_XXXX_0000_0098 | Smoke Sensitivity Level (High) Test Event |
| 0x005c_XXXX_0000_0099 | Smoke Sensitivity Level (Low) Test Event |
| 0x005c_XXXX_0000_009a | End of Service Alert Test Event |
| 0x005c_XXXX_0000_009b | Manual Device Mute Test Event |
| 0x005c_XXXX_0000_009c | Critical Smoke Alarm Test Event |
| 0x005c_XXXX_0000_009d | Critical CO Alarm Test Event |
| 0x005c_XXXX_0000_009e | Critical Battery Alert Test Event |
| 0x005c_XXXX_0000_00a0 | Smoke Alarm Test Event Clear |
| 0x005c_XXXX_0000_00a1 | CO Alarm Test Event Clear |
| 0x005c_XXXX_0000_00a2 | Interconnect Smoke Alarm Test Event Clear |
| 0x005c_XXXX_0000_00a3 | Hardware Fault Alert Test Event Clear |
| 0x005c_XXXX_0000_00a4 | Interconnect CO Alarm Test Event Clear |
| 0x005c_XXXX_0000_00a5 | Battery Alert Test Event Clear |
| 0x005c_XXXX_0000_00a6 | Contamination State Test Event Clear |
| 0x005c_XXXX_0000_00a8 | Smoke Sensitivity Level Test Event Clear |
| 0x005c_XXXX_0000_00aa | End of Service Alert Test Event Clear |
| 0x005c_XXXX_0000_00ab | Manual Device Mute Test Event Clear |
| Boolean State Configuration | Boolean State Configuration |
| PIXIT.BOOLCFG.TEST_EVENT_TRIGGER | Triggered Event |
| 0x0080_XXXX_0000_0000 | SensorTrigger Event |
| 0x0080_XXXX_0000_0001 | SensorUntrigger Event |
| Electrical Energy Measurement | Electrical Energy Measurement |
| PIXIT.EEM.TEST_EVENT_TRIGGER | Triggered Event |
| 0x0091_XXXX_0000_0000 | Stop Fake Readings Test Event |
| 0x0091_XXXX_0000_0001 | Start Fake 1kW Load @2s Event |
| 0x0091_XXXX_0000_0002 | Start Fake 3kW Generator @5s Event |
| Electrical Power Measurement | Electrical Power Measurement |
| PIXIT.EPM.TEST_EVENT_TRIGGER | Triggered Event |

| 0x0091_XXXX_0000_0000 | Stop Fake Readings Event |
| 0x0091_XXXX_0000_0001 | Start Fake 1kW Load @2s Event |
| Water Heater Management | Water Heater Management |
| PIXIT.EWATERHTR.TEST_EVENT_TRIGGER | Triggered Event |
| 0x0094_XXXX_0000_0000 | Basic installation Test Event |
| 0x0094_XXXX_0000_0001 | Basic installation Test Event Clear |
| 0x0094_XXXX_0000_0002 | Water Temperature 20C Test Event |
| 0x0094_XXXX_0000_0003 | Water Temperature 61C Test Event |
| 0x0094_XXXX_0000_0004 | Water Temperature 66C Test Event |
| 0x0094_XXXX_0000_0005 | Manual mode Test Event |
| 0x0094_XXXX_0000_0006 | Off mode Test Event |
| 0x0094_XXXX_0000_0007 | Draw off hot water Test Event |
| Device Energy Management | Device Energy Management |
| PIXIT.DEM.TEST_EVENT_TRIGGER | Triggered Event |
| 0x0098_XXXX_0000_0000 | Power Adjustment Test Event |
| 0x0098_XXXX_0000_0001 | Power Adjustment Test Event Clear |
| 0x0098_XXXX_0000_0002 | User Opt-out Local Optimization Test Event |
| 0x0098_XXXX_0000_0003 | User Opt-out Grid Optimization Test Event |
| 0x0098_XXXX_0000_0004 | User opt-out Test Event Clear |
| 0x0098_XXXX_0000_0005 | Start Time Adjustment Test Event |
| 0x0098_XXXX_0000_0006 | Start Time Adjustment Test Event Clear |
| 0x0098_XXXX_0000_0007 | Pausable Test Event |
| 0x0098_XXXX_0000_0008 | Pausable Test Event Next Slot |
| 0x0098_XXXX_0000_0009 | Pausable Test Event Clear |
| 0x0098_XXXX_0000_000A | Forecast Adjustment Test Event |
| 0x0098_XXXX_0000_000B | Forecast Adjustment Test Event Next Slot |
| 0x0098_XXXX_0000_000C | Forecast Adjustment Test Event Clear |
| 0x0098_XXXX_0000_000D | Constraints-based Adjustment Test Event |
| 0x0098_XXXX_0000_000E | Constraints-based Adjustment Test Event Clear |
| 0x0098_XXXX_0000_000F | Forecast Test Event |
| 0x0098_XXXX_0000_0010 | Forecast Test Event Clear |
| EEVSE | EEVSE |
| PIXIT.EEVSE.TEST_EVENT_TRIGGER | Triggered Event |
| 0x0099_XXXX_0000_0000 | Basic Functionality Test Event |

| 0x0099_XXXX_0000_0001 | Basic Functionality Test Event Clear |
| 0x0099_XXXX_0000_0002 | EV Plugged-in Test Event |
| 0x0099_XXXX_0000_0003 | EV Plugged-in Test Event Clear |
| 0x0099_XXXX_0000_0004 | EV Charge Demand Test Event |
| 0x0099_XXXX_0000_0005 | EV Charge Demand Test Event Clear |
| 0x0099_XXXX_0000_0006 | EVSE TimeOfUse Mode Test Event |
| 0x0099_XXXX_0000_0010 | EVSE Ground Fault Test Event |
| 0x0099_XXXX_0000_0011 | EVSE Over Temperature Fault Test Event |
| 0x0099_XXXX_0000_0012 | EVSE Fault Test Event Clear |
| 0x0099_XXXX_0000_0020 | EVSE Diagnostics Complete |
| 0x0099_XXXX_0000_0021 | EVSE TimeOfUse Mode Test Event Clear |
| Closure Control | Closure Control |
| PIXIT.CLCTRL.TEST_EVENT_TRIGGER | * Triggered Event* |
| 0x0104_XXXX_0000_0000 | MainState is Error(3) Test Event |
| 0x0104_XXXX_0000_0001 | MainState is Protected(5) Test Event |
| 0x0104_XXXX_0000_0002 | MainState is Disengaged(6) Test Event |
| 0x0104_XXXX_0000_0003 | MainState is SetupRequired(7) Test Event |
| 0x0104_XXXX_0000_0004 | MainState Test Event Clear |

## Chapter 2. MCORE PICS Definition

## 2.1. PICS Definition

This section covers a part of the MCORE related PICS items. MCORE PICS can be found and used among several clusters test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

## 2.1.1. Communication/Transport

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.COM.BLE | Does the device support communication over Bluetooth Low Energy (BLE) ? | O | |
| MCORE.COM.WIFI_2P4 GHZ | Does the device support communication over 2.4GHz Wi-Fi ? | O | |
| MCORE.COM.WIFI_5GH Z | Does the device support communication over 5GHz Wi-Fi ? | O | |
| MCORE.COM.WIFI | Does the device support communication over Wi-Fi ? | MCORE.COM.WIFI_2P4 GHZ, MCORE.COM.WIFI_5GH Z | |
| MCORE.COM.ETH | Does the device support communication over Ethernet ? | O | |
| MCORE.COM.THR | Does the device support communication over Thread ? | O | |
| MCORE.COM.WIRELESS | Does the device support Wi-Fi or Thread interfaces communication ? | MCORE.COM.WIFI, MCORE.COM.THR | |

## 2.1.2. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |

| MCORE.ROLE.COMMISS IONER | Does the device implement a Commissioner ? | O |
| MCORE.ROLE.COMMISS IONEE | Does the device implement a Commissionee ? | O |
| MCORE.ROLE.CONTRO LLER | Does the device implement a Controller ? | O |

## 2.1.3. Device Management

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.DLOG.S.UTCTI MESTAMP | Does the device support UTCTimeStamp field in the RetrieveLogsResponse Command of the Diagnostic Logs Cluster? | O | |
| MCORE.DLOG.S.TIMESI NCEBOOT | Does the device support TimeSinceBoot field in the RetrieveLogsResponse Command of the Diagnostic Logs Cluster? | O | |

## Chapter 3. Platform Certification Definitions

## Document History

| Rev | Date | Author | Description |

## 3.1. Platform Definition

A Matter Platform Supported Operating Environment (SOE) may be a single system-on-chip solution, or it may be a multi-chip system comprising different hardware elements providing Matter functionality. The Matter functionality includes the radio layers, network stack, and the main Matter platform elements. The Platform SOE must specify the Matter-dependent hardware in the system but may do so utilizing one or more hardware families that applies to multiple unique elements. The Platform SOE must also include a software package that specifies the framework, SDK, or operating systems along with the supported version. The Matter Platform may be located on a different hardware element from the Matter Product or application elements.

## 3.2. Derived Matter Product (DMP) Definition

A Derived Matter Product (DMP) makes use of a Matter Certified Platform (MCP) to certify a product and include other clusters and functionality required. Those items that are added to the platform are generally tested during the product testing while functionality previously tested by the certified platform is skipped. The full set of results of the Derived Matter Product with the previously certified Matter Platform is reviewed by the Alliance Certification Team to verify all tests appropriate for the product have been run. A certified Derived Matter Product is considered to have the same rights, requirements, and status as a Matter Product that was certified without use of a Platform. A DMP is required to abide by all the same rules of a Matter Product, for example usage of the logo and requirements to be registered in the DCL. The maker of a Derived Matter Product must indicate to the Alliance Certification Team the Certification ID of the Matter Certified Platform which was used and the specifics around the version. This ID allows the Certification Team to confirm the compliance of the DMP configuration with the platform certified configuration and to validate what test must be run during the certification. The Alliance Certification Team is responsible for verifying the status of a Matter Platform Certification ID used by the Product maker.

## 3.3. PICS Definition

This section covers a part of the platform certification related PICS items. Platform certification PICS can be found and used among clusters targeted by the platform certification test plan.

## 3.3.1. Test Context

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |

| PLAT.CERT | Is the TH performing a Platform Certification? | O |
| PLAT.CERT.TESTS.DONE | Is the TH performing a DMP Certification? | O |

## 3.3.2. PICS Usage

The following Logic tables explains how the PICS are used throughout Product and Platform Certification test plans.

| Value | Description |
| 1 | Behavior when the PICS is 1 |
| 0 | Behavior when the PICS is 0 |

## 3.3.3. PICS Usage Scenarios

| PICS_PLAT_CERT | PICS_PLAT_CERT_TESTS_DON E | Description |
| 0 | 0 | TH is performing a standard matter product certification. |

## Chapter 4. Device Discovery Test Plan

## 4.1. PICS Definition

This section covers the Device Discovery related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.DD.CHIP_DEV | Does the commissionee device only function within a Matter network? | O | |
| MCORE.DD.QR | Does the commissionee device or device packaging have a QR code based onboarding payload? | MCORE.DD.CONCATEN ATED_QR_CODE:M, O | |
| MCORE.DD.MANUAL_P C | Does the commissionee device or device packaging have a Manual Pairing Code? | O | |
| MCORE.DD.NFC | Does the commissionee device have a NFC tag containing the onboarding payload? | O | MCORE.DD.QR and/or MCORE.DD.MANUAL_P C are mandatory if this item is supported/true. |
| MCORE.DD.NTL | Does the DUT support NFC Transport Layer for commissioning? | O | |
| MCORE.DD.UI | Does the DUT support user interface? | O | |
| MCORE.DD.COMM_DIS COVERY | Does the DUT support Commissioner Discovery? | O | |

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.DD.CTRL_CONC ATENATED_QR_CODE_1 | Does the commissioner support scanning and processing concatenated QR codes? | O | |
| MCORE.DD.CTRL_CONC ATENATED_QR_CODE_2 | Does the Commissioner indicate to the user that devices must be commissioned individually using their separate QR codes or Manual Pairing Codes? | [!MCORE.DD.CTRL_CON CATENATED_QR_CODE _1] | |
| MCORE.DD.DISCOVERY _BLE | Does the commissioner support Discovery Capability over BLE? | MCORE.ROLE.COMMISS IONER & MCORE.COM.BLE | |
| MCORE.DD.DISCOVERY _PAF | Does the commissioner or device support Discovery Capability over Wi-Fi PAF? | O | |
| MCORE.DD.DISCOVERY _IP | Does the commissioner support Discovery Capability over IP Network? | MCORE.ROLE.COMMISS IONER:M | |
| MCORE.DD.STANDARD _COMM_FLOW | Does the DUT support commissioning via Standard Commissioning Flow? | MCORE.DD.11_MANUA L_PC:M | |
| MCORE.DD.NON_CONC URRENT_CONNECTION | Does the commissionee require Non- concurrent connection commissioning flow? | O | |
| MCORE.DD.USER_INTE NT_COMM_FLOW | Does the DUT support User-Intent Commissioning Flow? | O | |
| MCORE.DD.CUSTOM_C OMM_FLOW | Does the DUT support Custom Commissioning Flow? | O | |
| MCORE.DD.MANUAL_P C_COMMISSIONING | Does the commissioner support accepting a Manual Pairing Code for commissioning? | O | |

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.DD.21_MANUA L_PC | Does the commissioner support accepting a 21- digit Manual Pairing Code for commissioning? | O | MCORE.DD.USER_INTE NT_COMM_FLOW and/or MCORE.DD.CUSTOM_C OMM_FLOW are mandatory if this item is supported/true. |
| MCORE.DD.PHYSICAL_ TAMPERING | Is commissionee device subject to physical tampering (doorbell, camera, door lock, designed for outdoor usage)? | O | |
| MCORE.DD.SCAN_NFC | Does the commissioner support scanning NFC tags containing the onboarding payload? | O | |
| MCORE.DD.QR_COMMI SSIONING | Does the commissioner support accepting a QR code for commissioning? | O | |
| MCORE.DD.SCAN_QR_C ODE | Does the commissioner support scanning QR codes containing the onboarding payload? | O | |
| MCORE.DD.EXTENDED_ DISCOVERY | Does the commissionee device support Extended Discovery through DNS-SD advertisements when device is not in commissioning mode? | O | |

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.DD.COMMISSIO NING_SUBTYPE_V | Does the commissionee device support advertising the Vendor ID Commissioning Subtype in Commissionable Node Discovery through DNS-SD advertisements? | O | |
| MCORE.DD.COMMISSIO NING_SUBTYPE_T | Does the commissionee device support advertising the Device Type Commissioning Subtype in Commissionable Node Discovery through DNS-SD | O | |
| MCORE.DD.TXT_KEY_V P | Does the commissionee device support TXT Key 'VP' (Vendor ID / Product ID) in it's DNS- SD TXT Records for Commissionable Node Discovery? | O | |
| MCORE.DD.TXT_KEY_D T | Does the commissionee device support TXT Key 'DT' (Device Type) in it's DNS-SD TXT Records for Commissionable Node Discovery? | O | |
| MCORE.DD.TXT_KEY_D N | Does the commissionee device support TXT Key 'DN' (Device Name) in it's DNS-SD TXT Records for Commissionable Node Discovery? | O | |

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.DD.TXT_KEY_RI | Does the commissionee device support TXT Key 'RI' (Rotating Identifier) in it's DNS-SD TXT Records for Commissionable Node Discovery? | O | |
| MCORE.DD.TXT_KEY_P H | Does the commissionee device support TXT Key 'PH' (Pairing Hint) in it's DNS-SD TXT Records for Commissionable Node Discovery? | O | If MCORE.DD.EXTENDED_ DISCOVERY is true, then this record is required when not in Commissioning Mode (CM=0). |
| MCORE.DD.TXT_KEY_PI | Does the commissionee device support TXT Key 'PI' (Pairing Instruction) in it's DNS-SD TXT Records for Commissionable Node Discovery? | O | |
| MCORE.COM.PAF | Does the commissioner or the device support Commissioning over Wi-Fi PAF? | MCORE.COM.WIFI & MCORE.DD.DISCOVERY _PAF:M | |
| MCORE.DD.ESF_TC_CO MMISSIONER | Does the commissionee support Enhanced Setup Flow Terms and Conditions? | O | |

## 4.2. Test Case List

| TC UUID | Test Case Name |
| TC-DD-1.1 | QR Code Onboarding Payload Verification [DUT - Commissionee] |
| TC-DD-1.2 | Manual Pairing Code Payload Verification [DUT - Commissionee] |
| TC-DD-1.3 | NFC Onboarding Payload Verification [DUT - Commissionee] |

| TC UUID | Test Case Name |
| TC-DD-1.4 | Concatenation - QR Code Onboarding Payload Verification [DUT - Commissionee] - PROVISIONAL |
| TC-DD-1.5 | NFC Rules of Advertisement and Onboarding [DUT - Commissionee] |
| TC-DD-1.6 | QR Code Format and Label [DUT - Commissionee] |
| TC-DD-1.7 | Setup Code Format and Label [DUT - Commissionee] |
| TC-DD-1.8 | QR Code Onboarding Payload Verification [DUT Commissioner] |
| TC-DD-1.9 | Manual Pairing Code Payload Verification [DUT Commissioner] |
| TC-DD-1.10 | NFC Onboarding Payload Verification [DUT - Commissioner] |
| TC-DD-1.11 | Concatenation - QR Code Onboarding Payload Verification [DUT - Commissioner] - PROVISIONAL |
| TC-DD-1.12 | Onboarding Payload Verification - Custom Flow = 0 [DUT - Commissionee] |
| TC-DD-1.13 | Onboarding Payload Verification - Custom Flow = 1 [DUT - Commissionee] |
| TC-DD-1.14 | Onboarding Payload Verification - Custom Flow = 2 [DUT - Commissionee] |
| TC-DD-2.1 | Announcement by Device Verification [DUT - Commissionee] |
| TC-DD-2.2 | Discovery by Commissioner Verification [DUT - Commissioner] |
| TC-DD-3.3 | User Directed Commissioning [DUT - Commissionee] |
| TC-DD-3.4 | User Directed Commissioning [DUT - Commissioner] |
| TC-DD-3.5 | Commissioning Flow - Concurrent [DUT - Commissioner] |
| TC-DD-3.6 | Commissioning Flow - Non-concurrent [DUT - Commissioner] |
| TC-DD-3.7 | Commissioning Flow - Concurrent - Negative Scenario [DUT - Commissioner] - PROVISIONAL |

| TC UUID | Test Case Name |
| TC-DD-3.8 | Commissioning Flow - Non-concurrent - Negative Scenario [DUT - Commissioner] - PROVISIONAL |
| TC-DD-3.9 | Commissioning Flow - Custom Flow = 2 [DUT - Commissionee] |
| TC-DD-3.10 | Commissioning Flow - Custom Flow = 2 [DUT - Commissioner] |
| TC-DD-3.11 | Commissioning Flow = 0 (Standard Flow) - QR Code [DUT - Commissioner] |
| TC-DD-3.12 | Commissioning Flow = 1 (User-Intent Flow) - QR Code [DUT - Commissioner] |
| TC-DD-3.13 | Commissioning Flow = 2 (Custom Flow) - QR Code [DUT - Commissioner] |
| TC-DD-3.14 | Commissioning Flow - QR Code - Negative Scenario [DUT - Commissioner] |
| TC-DD-3.15 | Commissioning Flow - Manual Pairing Code [DUT - Commissioner] |
| TC-DD-3.16 | Commissioning Flow - 11-digit Manual Pairing Code - Negative Scenario [DUT - Commissioner] |
| TC-DD-3.17 | Commissioning Flow - 21-digit Manual Pairing Code - Negative Scenario [DUT - Commissioner] |
| TC-DD-3.18 | Commissioning Flow - Commissioning Multiple Devices [DUT - Commissioner] |
| TC-DD-3.19 | Commissioning Flow - Commission, Unpair and Re-commission Device [DUT - Commissionee] |
| TC-DD-3.20 | Commissioning Flow - Commission, Unpair and Re-commission Device [DUT - Commissioner] |
| TC-DD-3.21 | Commissioning Flow - Commission Multiple- Endpoint Device [DUT - Commissioner] |
| TC-DD-3.22 | NFC-based Commissioning [DUT as Commissioner] - PROVISIONAL |
| TC-DD-3.23 | NFC-based Commissioning - DUT with power [DUT as Commissionee] |
| TC-DD-3.24 | NFC-based Commissioning - DUT without power [DUT as Commissionee] |

## 4.3. Test Cases

## 4.3.1. Onboarding Payload Test Cases

## TC-DD-1.1 QR Code Onboarding Payload Verification [DUT - Commissionee]

## Purpose

This test case verifies that the onboarding QR code contains the necessary information to onboard the device onto the Matter network.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.QR

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | DUT | DUT as Commissionee device with the QR code printed on it or contained in additional provided materials. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 2.b | 5.1.3.1 Table 34 | | Verify Vendor ID and Product ID | Verify Vendor ID and Product ID match the values submitted by manufacturer in Distributed Compliance Ledger |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2.c | 5.1.3.1 Table 34 | | Verify the Custom Flow bit | Verify the Custom Flow bit has one of the following values: 0, 1 or 2 |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2.d | 5.1.3.1 Table 34 | | Verify 8-bit Discovery Capabilities bit mask | Verify that the onboarding payload contains an 8-bit Discovery Capabilities bitmask. Each bit must represent the following transport support: Bit 0 - Reserved (SHALL be 0) Bit 1 - BLE: - 0: Device does not support BLE for discovery or is currently commissioned into one or more fabrics. - 1: Device supports BLE for discovery when not commissioned. Bit 2 - On IP network: - 1: Device is already on the IP network Bits 3 - Wi-Fi Public Action Frame: - 0: Device does not support Wi-Fi Public Action Frame for discovery or is currently commissioned into one or more fabrics. - 1: Device supports Wi-Fi Public Action Frame for discovery when not commissioned. Bits 4 - NFC Transport Layer - 0: Device does not support NFC Transport Layer (NTL) for commissioning or is currently commissioned into one or more fabrics. - 1: Device supports NFC Transport Layer (NTL) for commissioning when not commissioned. Bits 7-5 - Reserved (SHALL be 0) |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2.f | 5.1.3.1 Table 34 | | Verify the onboarding payload contains a 27-bit Passcode | Verify the 27-bit unsigned integer encodes an 8-digit decimal numeric value and shall be a value between 0x0000001 to 0x5f5e0fe (00000001 to 99999998) |

## Notes/Testing considerations

## TC-DD-1.2 Manual Pairing Code Payload Verification [DUT - Commissionee]

## Purpose

This test case verifies that the Manual Pairing Code contains the necessary information to onboard the device onto the Matter network.

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.MANUAL\_PC

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as a Checksum script used to validate the check digit using the Verhoeff algorithm |
| 2 | DUT | DUT as Commissionee device with the Manual Pairing Code printed on it or contained in additional provided materials. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 5.1.4.1 Table 38 | | Verify the first digit of the Manual Pairing Code for the DUT | The first digit must be between 0 and 7. If the digit is between 0 and 3, the code length must be 11 digits (VID_PID flag not set). If the digit is between 4 and 7, the code length must be 21 digits (VID_PID flag set) |
| 2 | 5.1.4.1 Table 38 | | If the Manual Pairing Code is 11 digits/the VID_PID flag is not set, verify the encoded elements. | Digits 2 through 6 must be between 00000 and 65535 Digits 7 through 10 must be between 0000 and 8191 |

## Notes/Testing considerations

## TC-DD-1.3 NFC Onboarding Payload Verification [DUT - Commissionee]

## Purpose

This test case verifies that the NFC tag's onboarding payload contains the necessary information to onboard the device onto the Matter network.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.NFC

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as an NFC code reader device that can read and decode a NFC code |
| 2 | DUT | DUT as Commissionee device with the NFC tag containing an onboarding payload |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Power up the DUT and put the DUT in pairing mode | |
| 2 | | | Bring the NFC code reader close to the DUT | |

| 3.a | 5.1.3.1 Table 33/34 | Verify the NFC's onboarding payload code version | Verify the NFC's onboarding payload code version is '000'. |

| 5.1.3.1 Table | 3.b | Verify that the onboarding payload contains an 8-bit |
| | | Discovery Capabilities |
| 34/35 | | |
| | | bitmask. Each bit must represent the following |
| | | transport support: |
| | | Bit 1 - BLE: - 0: Device does not support BLE for discovery or is currently |
| | | commissioned into one or |
| | | more fabrics. - 1: Device supports BLE for |
| | | discovery |
| | | Bit 2 - On IP network: - 1: |
| | | Device is already on the IP |
| | | network |
| | | Bits 3 - Wi-Fi Public Action Frame: - 0: Device does not support Wi-Fi Public Action Frame for discovery or is |
| | | currently commissioned into one or more fabrics. - 1: |
| | | Device supports Wi-Fi Public |
| | | Action Frame for discovery |
| | | Bits 4 - NFC Transport Layer - 0: Device does not support |
| | | NFC Transport Layer (NTL) for commissioning or is currently commissioned into one or more fabrics. - 1: Device supports NFC |
| | | Transport Layer (NTL) for |
| | | Bits 7-5 - Reserved |
| | | be 0) |
| | | (SHALL |
| | | Ensure that the bitmask |
| | | accurately reflects the DUT's |
| | | commissioning when not |

| 3.d | | | Verify the onboarding payload contains a 27-bit Passcode | Verify the 27-bit unsigned integer encodes an 8-digit decimal numeric value and shall be a value between 0x0000001 to 0x5f5e0fe (00000001 to 99999998) |
| 3.e | | | Verify passcode is valid | Verify passcode does not use any trivial values: 00000000, 11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999, 12345678, 87654321 Verify Passcode is not derived from public information as serial number, manufacturer date, MAC address, region of origin etc. |
| | | 3.f | Verify NFC's onboarding payload code prefix | Verify NFC's onboarding payload code prefix is "MT:" |
| 3.g | | | Verify Vendor ID and Product ID | Verify Vendor ID and Product ID match the values submitted by manufacturer in Distributed Compliance Ledger |

## Notes/Testing considerations

## TC-DD-1.4 Concatenation - QR Code Onboarding Payload Verification [DUT - Commissionee] PROVISIONAL

## Purpose

This test case verifies that the onboarding QR code contains information on the onboarding of multiple DUT.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.CONCATENATED\_QR\_CODE

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as a QR code reader device that can read and decode a QR code |
| 2 | DUT | DUT as Commissionee device with the QR code printed on it or contained in additional provided materials. |

## Test Setup

The DUT may include in its packaging a combined QR code containing a concatenation of all the devices that will be available for commissioning.

## Test Procedure

| # | Ref | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-1.5 NFC Rules of Advertisement and Onboarding [DUT - Commissionee]

## Purpose

This test case verifies that the NFC Tag setup experience follows guidance in section 5.1.8

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.NFC

## Preconditions

- DUT is in its retail packaging.

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as an NFC reader device that can read and decode an NFC Tag |
| 2 | DUT | DUT as Commissionee device with the NFC tag containing an onboarding payload |

## Device Topology

N/A.

## Test Setup

DUT can be reached (at contact) by the TH NFC reader.

## Test Procedure

| # | Ref | Test Step | Expected Outcome |

| # | Ref | PIC S | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-1.6 QR Code Format and Label [DUT - Commissionee]

## Purpose

This test case verifies that the onboarding QR code is of scannable size.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.QR

## Required Devices

| # | Device Name | Device Description |
| 2 | DUT | DUT as Commissionee device with the QR code printed on it or contained in additional provided materials. |

## Test Setup

Final label of DUT is ready to be scanned

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-1.7 Setup Code Format and Label [DUT - Commissionee]

## Purpose

This test case verifies that the Manual Pairing Code size meets the minimum requirements.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.MANUAL\_PC

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | Ruler/Measur ing Device | Used to validate the size of the Manual Pairing Code |
| 2 | DUT | DUT as Commissionee device with the Manual Pairing Code printed on it or contained in additional provided materials. |

## Test Setup

## Final label of DUT is ready to be scanned

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 5.1.4, 1.6.1, 5.7.4 | | Verify using instruments | The Manual Pairing Code shall meet the following requirements: - Printed using a minimum font size of 6 points, typically producing a typeface height of 2.1mm (6/72 inches) - Include dashes between the groups of Manual Pairing Code digits with the following spacing: - For 11 or 21-digit codes, the first row spacing is 4-3-4 (First Row: "1234-567-8901") - For 21-digit codes, the second row spacing is 4-3-2- 1 (Second Row:"9876-543-21- 0") |

## Notes/Testing considerations

## TC-DD-1.8 QR Code Onboarding Payload Verification [DUT - Commissioner]

## Purpose

This test case verifies that the Commissioner is able to scan and parse the QR code to onboard the device onto the Matter network.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING

| # | Doc. Ref. | Condition | Notes |
| 1 | 5.1.3, 5.1.5 | QR Code is printed on the Commissionee device or in additional provided materials (ex: manual, companion app, web service). Device also has additional TLV data with a non-zero length appended to the end of the QR code. An example onboarding QR code could be "MT:- 24J029Q00KA064IJ3P0IXZB0DK5N1K8SQ1RYCU1-A40" (following 5.1.3 "QR Code", Table 34 "Packed Binary Data Structure for Onboarding Payload") which includes: - 3-bit Version String=000 - 16-bit Vendor ID=0xFFF1 (as defined in section 2.5.2. "Vendor Identifier") - 16-bit Product ID=0x8001 (as defined in section 2.5.3. "Product Identifier") - 2-bit Custom Flow=10 (Custom Commissioning Flow = 2) - 8-bit Discovery Capabilities Bitmask=00000100 (OnNetwork) - 12-bit Discriminator=0xF00 - 27-bit Passcode=20202021 - 4-bit Padding=0000 - TLV Data=0x152C000A3132333435363738393018 included (as defined in section 5.1.3.1. "Payload", subsection "TLV | |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device with the QR code printed on it or contained in additional provided materials. |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 4.b | | | Using the DUT, parse the TH's QR code to onboard the TH Device onto the Matter network. | Verify the TH's QR code with the appended TLV data was parsed successfully by the DUT (where the DUT may ignore the TLV contents) |

## Notes/Testing considerations

## TC-DD-1.9 Manual Pairing Code Payload Verification [DUT - Commissioner]

## Purpose

This test case verifies that the Manual Pairing Code can be provided to the Commissioner and parsed to onboard the device onto the Matter network.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.MANUAL\_PC\_COMMISSIONING

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a Commissioner device that can read and decode a Manual Pairing Code. |

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a device used to validate the check digit using the Verhoeff algorithm |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-1.10 NFC Onboarding Payload Verification [DUT - Commissioner]

## Purpose

This test case verifies that the Commissioner is able to read and decode the NFC code to onboard the device onto the Matter network.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.SCAN\_NFC

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a Commissioner device that can read and decode an NFC tag containing an Onboarding Payload. |
| 2 | TH | Test Harness as a Commissionee device with NFC tag/ Reference NFC tag |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Power up the TH Device and put the TH Device in commissioning mode | TH is in a state to be commissioned by the DUT Commissioner |

| 2 | Bring the DUT close to the NFC tag for the TH Device | Verify the DUT is able to read and decode the NFC tag's onboarding payload successfully to onboard the TH Device onto the Matter network. |

## Notes/Testing considerations

## TC-DD-1.11 Concatenation - QR Code Onboarding Payload Verification [DUT - Commissioner] - PROVISIONAL

## Purpose

This test case verifies that the Commissioner is able to scan and correctly parse a concatenated QR code containing onboarding payloads for multiple TH(Commissionee) devices.

It further verifies that the DUT provisions each device one by one using the parsed payload information and successfully commissions all devices onto the Matter network.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a Commissioner device capable of scanning a concatenated QR code and commissioning multiple devices onto the Matter network. |
| 2 | TH | Test Harness as Multiple Devices that are Commissionees with a concatenated QR code |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | | !(MCORE.DD.CTRL _CONCATENATED_ QR_CODE_1) & MCORE.DD.CTRL_ CONCATENATED_ QR_CODE_2 | | Verify the DUT indicates to the user that TH devices must be commissioned individually using their separate QR codes or Manual Pairing Codes. |

## Notes/Testing considerations

chip-tool support for concatenated QR code parsing is available from Matter SDK version 1.6 onward.

## TC-DD-1.12 Onboarding Payload Verification - Custom Flow = 0 [DUT - Commissionee]

## Purpose

This test case verifies that the interactions defined by the Custom Flow field are reflected by the DUT supporting Standard Commissioning Flow

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.QR
- MCORE.DD.STANDARD\_COMM\_FLOW

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | DUT | DUT as Commissionee device with the QR code printed on it or contained in additional provided materials. DUT supports Standard Commissioning Flow. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-1.13 Onboarding Payload Verification - Custom Flow = 1 [DUT - Commissionee]

## Purpose

This test case verifies that the interactions defined by the Custom Flow field are reflected by the DUT supporting User-Intent Commissioning Flow

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.QR
- MCORE.DD.USER\_INTENT\_COMM\_FLOW

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as a QR code reader device that can read and decode a QR code. |

| # | Device Name | Device Description |
| 2 | DUT | DUT as Commissionee device with the QR code printed on it or contained in additional provided materials. DUT supports User- Intent Commissioning Flow. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-1.14 Onboarding Payload Verification - Custom Flow = 2 [DUT - Commissionee]

## Purpose

This test case verifies that the interactions defined by the Custom Flow field are reflected by the DUT supporting Custom Commissioning Flow

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.QR
- MCORE.DD.CUSTOM\_COMM\_FLOW

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | DUT | DUT as Commissionee device with the QR code printed on it or contained in additional provided materials. DUT supports Custom Commissioning Flow. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## 4.3.2. Pre-Commissioning Discovery Test Cases

## TC-DD-2.1 Announcement by Device Verification [DUT - Commissionee]

## Purpose

The purpose of this test case is to verify if the DUT properly announces its uncommissioned state to allow a Matter Commissioner to discover the DUT to be commissioned.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | The DUT is switched on and the DUT is transport-connected (BLE, Wi-Fi or Ethernet) | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as a Matter Commissioner that is already joined in a Matter network |
| 2 | DUT | DUT as a Commissionee device that is in an uncommissioned state |

## Platform Certification

In the context of a platform certification, if the platform supports multiple configuration related to device types PICS, this test will have to be run once for each configuration. Same applies for the support of different transport PICS, such as PICS\_MCORE\_COM\_BLE, PICS\_MCORE\_COM\_THREAD and PICS\_MCORE\_COM\_WIFI. For PICS related to the content of DNS-SD TXT Records, such as,MCORE.DD.TXT\_KEY\_DT, the test only needs to be run once to show support of the feature.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 15 | 5.4.2.1, 4.3.1.5., 4.3.1.7., 4.3.1.11. | | TH and DUT are connected to the same network through vendor-unique means or by commissioning the DUT onto the Matter network and opening a commissioning window. The DUT is sending mandatory Commissionable Node Discovery service records over DNS-SD. | DUT is able to be discovered over DNS-SD. For each of the following required TXT record keys for DNS-SD based discovery, validate that the DUT's TXT records contain a valid key/value pair corresponding to the rules for each TXT key listed: D: Full 12-bit discriminator for the Commissionable Node (Spec. 4.3.1.5.). The discriminator value SHALL be encoded as a variable- length decimal number in ASCII text, with up to four digits, omitting any leading zeroes. For example, value D=840 would indicate that this Commissionable Node has a decimal long discriminator=840. CM: Commissioning Mode, The absence of key CM SHALL imply a value of 0 (CM=0). CM=0 SHALL indicate that the publisher is not currently in Commissioning Mode. CM=1 SHALL indicate that the publisher is currently in Commissioning Mode and requires use of a passcode for commissioning provided by the Commissionee CM=2 SHALL indicate that the publisher is currently in Commissioning Mode and requires use of a dynamically generated passcode for commissioning corresponding to the verifier that was passed to the device using the Open |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 19.b | 4.3.1.3., 4.3.1.13. | | Send a browse request for '_matterc._udp' using a DNS- SD records command-line test tool (i.e. 'dns-sd -B _matterc._udp' or 'avahi- browse _matterc._udp -r') | DUT responds to the '_matterc._udp' browse request from the TH. Verify TH is able to read the Matter pointer records for the DUT |

## TC-DD-2.2 Discovery by Commissioner Verification [DUT - Commissioner]

## Purpose

The purpose of the test case is to verify that a device acting as Commissioner is able to properly discover an uncommissioned matter device that wants to join the network using all discovery transport technologies specified.

## PICS

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| 1 | 5.4.3. Discovery by Commissioner | DUT supports BLE (central role), Wi-Fi and IP connectivity | Wi-Fi certified n client |
| 2 | | Test Harness must support all discovery transport technologies as the DUT (i.e. BLE, Wi-Fi and IP connectivity) | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as a Commissionee device acting as a joiner that supports all discovery transports (i.e. BLE, Wi-Fi and IP connectivity) |
| 2 | DUT | DUT as Commissioner device that is joined already in a Matter network |

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## 4.3.3. Commissioning Flows Test Cases

## TC-DD-3.3 User Directed Commissioning [DUT - Commissionee]

## Purpose

This test case verifies that a Commissionee is able to initiate the commissioning procedure using User Directed Commissioning.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.UI
- MCORE.DD.COMM\_DISCOVERY

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | | User must indicate the intention for commissioning using a display or other UI elements. |
| 2 | | | TH is not advertising Commissioner Discovery Service at start |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as a Matter Commissioner that supports Commissioner Discovery and is already in network |
| 2 | DUT | DUT as a Commissionee device that is in an uncommissioned state, supports Commissioner Discovery and has UI |

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

Test Steps 4, 5: Out of Scope for V1.0

## TC-DD-3.4 User Directed Commissioning [DUT - Commissioner]

## Purpose

This test case verifies that a Commissioner is able to handle the commissioning procedure initiated by a commissionee using User Directed Commissioning.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.UI
- MCORE.DD.COMM\_DISCOVERY

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | | User must indicate the intention for commissioning using a display or other UI elements. |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a Matter Commissioner that supports Commissioner Discovery and is already in network |
| 2 | TH | Test Harness as a Commissionee device that is in an uncommissioned state and supports Commissioner Discovery |

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

Test Steps 3, 4: Out of Scope for V1.0

## TC-DD-3.5 Commissioning Flow - Concurrent [DUT - Commissioner]

## Purpose

The purpose of the following test cases is to verify the End to End Concurrent Commissioning Flow of commissioner that can discover and commission a device in the Matter network.

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a device that has Commissioner role |
| 2 | TH | Test Harness as a Commissionee device that is connected to an operational network(i.e. BLE, Wi-Fi, or Ethernet) and is prepared for commissioning |

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1 | DU T | 5.5 - 1 | | Commissioner has regulatory and fabric information available and has accurate date, time and timezone | Check time, date and timezone on DUT |
| 2 | | 5.5 - 2, 5.4. 3.3, 5.4. 2.1 | | Commissioner and Commissionee discover each other and connect via the discovery mode applicable for the DUT. TH device is advertising over IP Network using DNS- based Service Discovery (DNS-SD) | Commissioner and Commissionee can discover each other and connect to each other. |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 3 | DU T | 5.5 - 3 | | Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel | DUT is able to establish encryption keys using PASE |
| 4 | DU T | 5.5 - 4 | | Commissioner SHALL re- arm Fail-safe timer on Commissionee within 60s (the autonomously Fail-safe timer length set by Commissionee) | TH arm the Fail-safe timer with success |
| 6 | DU T | 5.5 - 8 | | Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command | TH generate a new operational key pair |
| 7 | DU T | 5.5 - 9 | | Commissioner configures operational credentials on DUT if not previously installed | TH is able to install Trusted Root Certificate if needed |
| 8 | DU T | 5.5 - 10 | | Commissioner configures itself as administrator in ACL on TH if needed | TH configure the ACL with success |
| 9 | DU T | 5.5 - 11 | | Commissioner configures operational network on TH if TH both supports and requires | TH configure the correct operational network credentials |
| 10 | DU T | 5.5 - 12 | | Commissioner instructs Commissionee to connect to operational network if not already connected | TH successfully connect to operational network |
| 12 | DU T | 5.5 - 13 | | Commissioner starts discovery of TH using Operational Discovery | |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 13 | DU T | 5.5 - 14 | | Commissioner opens a CASE session with TH over operational network | TH is able to open the CASE session with DUT |
| 14 | DU T | 5.5 - 15 | | Commissioner sends CommissioningComplete command | TH respond with success at CommissioningComplete command sent by DUT |

## Notes/Testing considerations

## TC-DD-3.6 Commissioning Flow - Non-concurrent [DUT - Commissioner] - PROVISIONAL

## Purpose

The purpose of the following test cases is to verify the End to End Non-Concurrent Commissioning Flow of commissioner that can commission a device in the Matter network.

## PICS

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a device that has Commissioner role |
| 2 | TH | Test Harness as a Commissionee device that is not connected to an operational network(i.e. BLE, Wi-Fi, or Ethernet) and is prepared for commissioning as a Non-concurrent device |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1 | DU T | 5.5 - 1 | | Commissioner has regulatory and fabric information available and has accurate date, time and timezone | Check time, date and timezone on DUT |
| 3 | DU T | 5.5 - 3 | | Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel | DUT is able to establish encryption keys using PASE |
| 4 | DU T | 5.5 - 4 | | Commissioner SHALL re- arm Fail-safe timer on Commissionee within 60s (the autonomously Fail-safe timer length set by Commissionee) | TH arm the Fail-safe timer with success |
| 6 | DU T | 5.5 - 8 | | Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command | TH generate a new operational key pair |
| 7 | DU T | 5.5 - 9 | | Commissioner configures operational credentials on DUT if not previously installed | TH is able to install Trusted Root Certificate if needed |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 8 | DU T | 5.5 - 11 | | Commissioner configures itself as administrator in ACL on TH if needed | TH configure the ACL with success |
| 9 | DU T | 5.5 - 12 | | Commissioner configures operational network on TH if TH both supports and requires | TH configure the correct operational network credentials |
| 10 | DU T | 5.5 - 13, 11. 8.7. 9 | | Commissioner instructs Commissionee to connect to operational network | DUT waits for success in the ConnectNetworkResponse command and moves onto the next step |
| 11 | TH | 5.5 - 13, 11. 8.7. 9 | | Commissioning channel between the Commissioner and Commissionee is closed, operational channel started | |
| 12 | DU T | 5.5 - 14 | | Commissioner starts discovery of TH using Operational Discovery | |
| 13 | DU T | 5.5 - 15 | | Commissioner opens a CASE session with TH over operational network | TH is able to open the CASE session with DUT |
| 14 | DU T | 5.5 - 16 | | Commissioner sends CommissioningComplete command | TH respond with success at CommissioningComplete command sent by DUT |

## Notes/Testing considerations

## TC-DD-3.7 Commissioning Flow - Concurrent - Negative Scenario [DUT - Commissioner] PROVISIONAL

## Purpose

The purpose of the following test cases is to verify the End to End Concurrent Commissioning Flow of commissioner that can commission a device in the Matter network.

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a Matter Commissioner device |
| 2 | TH | Test Harness as a Commissionee device that is connected to an operational network(i.e. BLE, Wi-Fi, or Ethernet) and is prepared for commissioning |

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1 | DU T | 5.5 - 1 | | Commissioner has regulatory and fabric information available and has accurate date, time and timezone | Check time, date and timezone on DUT |
| 2 | | 5.5 - 2 | | Commissioner and Commissionee discover each other and connect via the discovery mode applicable for the DUT. | Commissioner and Commissionee can discover each other and connect to each other. |
| 3 | DU T | 5.5 - 3 | | Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel | DUT is able to establish encryption keys using PASE |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 4 | DU T | 5.5 - 4 | | Commissioner SHALL re- arm Fail-safe timer on Commissionee within 60s (the autonomously Fail-safe timer length set by Commissionee) | TH arm the Fail-safe timer with success |
| 7 | DU T | 5.5 - 3 | | Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel | DUT is able to establish encryption keys using PASE |
| 8 | DU T | 5.5 - 4 | | Commissioner SHALL re- arm Fail-safe timer on Commissionee within 60s (the autonomously Fail-safe timer length set by Commissionee) | TH arm the Fail-safe timer with success |
| 10 | DU T | 5.5 - 8 | | Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command | TH generate a new operational key pair |
| 11 | DU T | 5.5 - 9 | | Commissioner configures operational credentials on DUT if not previously installed | TH is able to install Trusted Root Certificate if needed |
| 12 | DU T | 5.5 - 10 | | Commissioner configures itself as administrator in ACL on TH if needed | TH configure the ACL with success |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 13 | DU T | 5.5 - 11 | | Commissioner configures operational network on TH if TH both supports and requires | TH configure the correct operational network credentials |
| 14 | DU T | 5.5 - 12 | | Commissioner instructs Commissionee to connect to operational network if not already connected | TH successfully connect to operational network |
| 17 | DU T | 5.5 - 12 | | Commissioner instructs Commissionee to connect to operational network if not already connected | TH successfully connect to operational network |
| 18 | DU T | 5.5 - 13 | | Commissioner starts discovery of TH using Operational Discovery | |
| 19 | DU T | 5.5 - 14 | | Commissioner opens a CASE session with TH over operational network | TH is able to open the CASE session with DUT |
| 20 | DU T | 5.5 - 15 | | Commissioner sends CommissioningComplete command | TH respond with success at CommissioningComplete command sent by DUT |

## Notes/Testing considerations

## TC-DD-3.8 Commissioning Flow - Non-concurrent - Negative Scenario [DUT - Commissioner] PROVISIONAL

## Purpose

The purpose of the following test cases is to verify the End to End Non-Concurrent Commissioning Flow of commissioner that can commission a device in the Matter network.

## PICS

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a Matter Commissioner device |
| 2 | TH | Test Harness as a Commissionee device that is not connected to an operational network(i.e. BLE, Wi-Fi, or Ethernet) and is prepared for commissioning |

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1 | DU T | 5.5 - 1 | | Commissioner has regulatory and fabric information available and has accurate date, time and timezone | Check time, date and timezone on DUT |
| 2 | | 5.5 - 2 | | Commissioner and Commissionee discover each other and connect via the discovery mode applicable for the DUT. | Commissioner and Commissionee can discover each other and connect to each other. |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 3 | DU T | 5.5 - 3 | | Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel | DUT is able to establish encryption keys using PASE |
| 4 | DU T | 5.5 - 4 | | Commissioner SHALL re- arm Fail-safe timer on Commissionee within 60s (the autonomously Fail-safe timer length set by Commissionee) | TH arm the Fail-safe timer with success |
| 6 | DU T | 5.5 - 8 | | Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command | TH generate a new operational key pair |
| 7 | DU T | 5.5 - 9 | | Commissioner configures operational credentials on DUT if not previously installed | TH is able to install Trusted Root Certificate if needed |
| 8 | DU T | 5.5 - 11 | | Commissioner configures itself as administrator in ACL on TH if needed | TH configure the ACL with success |
| 9 | DU T | 5.5 - 12 | | Commissioner configures operational network on TH if TH both supports and requires | TH configure the correct operational network credentials |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 10 | DU T | 5.5 - 13, 11. 8.7. | | Commissioner instructs Commissionee to connect to operational network | DUT waits for success in the ConnectNetworkResponse command and moves onto the next step |
| 13 | DU T | 5.5 - 3 | | Establish encryption keys with Password Authenticated Session Establishment on the commissioning channel | DUT is able to establish encryption keys using PASE |
| 14 | DU T | 5.5 - 3 | | Commissioner re-arms Fail- safe timer on Commissionee within 60s (the autonomously Fail-safe timer length set by Commissionee) | TH arm the Fail-safe timer with success |
| 16 | DU T | 5.5 - 8 | | Commissioner requests operational CSR from Commissionee with OperationalCSRRequest command | TH generate a new operational key pair |
| 17 | DU T | 5.5 - 9 | | Commissioner configures operational credentials on DUT if not previously installed | TH is able to install Trusted Root Certificate if needed |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 18 | DU T | 5.5 - 11 | | Commissioner configures itself as administrator in ACL on TH if needed | TH configure the ACL with success |
| 19 | DU T | 5.5 - 12 | | Commissioner configures operational network on TH if TH both supports and requires | TH configure the correct operational network credentials |
| 20 | DU T | 5.5 - 13 | | Commissioner instructs Commissionee to connect to operational network if not already connected | TH successfully connect to operational network |
| 22 | DU T | 5.5 - 14 | | Commissioner starts discovery of TH using Operational Discovery | |
| 23 | DU T | 5.5 - 15 | | Commissioner opens a CASE session with TH over operational network | TH is able to open the CASE session with DUT |
| 24 | DU T | 5.5 - 16 | | Commissioner sends CommissioningComplete command | TH respond with success at CommissioningComplete command sent by DUT |

## Notes/Testing considerations

## TC-DD-3.9 Commissioning Flow - Custom Flow = 2 [DUT - Commissionee]

## Purpose

The purpose of this test case is to verify if a device that is not a commissioner and has a custom commissioning flow is able to complete the commissioning procedure with success.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.CUSTOM\_COMM\_FLOW

| # | Doc. Ref. | Condition | Notes |
| 1 | | Commissioner is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

## Required Devices

| # | Device Name | Device Description |
| 2 | DUT | DUT as a Commissionee device acting as a commissionee to join a Matter network that has a custom commissioning flow. |

## Device Topology

Commissioner (TH) ←→ DUT

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.10 Commissioning Flow - Custom Flow = 2 [DUT - Commissioner]

## Purpose

The purpose of this test case is to verify if a node that acts as a commissioner is able to properly use custom commissioning data that a commissionee may require in order to complete the commissioning procedure with success.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.CUSTOM\_COMM\_FLOW

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness Commissionee device acting as a commissionee to join a Matter network that has a custom commissioning flow. |

## Device Topology

## DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

The test should be run for all transport layers supported for commissioning among BTP, WiFi-PAF, NTL

## TC-DD-3.11 Commissioning Flow = 0 (Standard Flow) - QR Code [DUT - Commissioner]

## Purpose

This test case verifies that the Commissioner can scan a device onboarding QR code, successfully parse the QR code and successfully complete the commissioning procedure using Standard commissioning flow.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING
- MCORE.DD.STANDARD\_COMM\_FLOW

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device acting as a commissionee to join a Matter network. |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## TC-DD-3.12 Commissioning Flow = 1 (User-Intent Flow) - QR Code [DUT - Commissioner]

## Purpose

This test case verifies that the Commissioner can scan a device onboarding QR code, successfully parse the QR code and successfully complete the commissioning procedure using User-Intent commissioning flow.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING
- MCORE.DD.USER\_INTENT\_COMM\_FLOW

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device acting as a commissionee to join a Matter network. |

## Device Topology

## DUT ←→ Commissionee

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## TC-DD-3.13 Commissioning Flow = 2 (Custom Flow) - QR Code [DUT - Commissioner]

## Purpose

This test case verifies that the Commissioner can scan a device onboarding QR code, successfully parse the QR code and successfully complete the commissioning procedure using Custom commissioning flow.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING
- MCORE.DD.CUSTOM\_COMM\_FLOW

## Preconditions

| # | Doc. Ref. | Condition | Notes |

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device acting as a commissionee to join a Matter network. |

## Device Topology

## DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## TC-DD-3.14 Commissioning Flow - QR Code - Negative Scenario [DUT - Commissioner]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissioner can scan a device onboarding QR code, successfully parse the QR code and prevent the commissioning of any devices when scanning an invalid QR code.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device acting as a commissionee to join a Matter network. |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.15 Commissioning Flow - Manual Pairing Code [DUT - Commissioner]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissioner can use a Manual Pairing Code, successfully parse the Manual Pairing Code and complete the commissioning procedure with success.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.MANUAL\_PC\_COMMISSIONING

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device acting as a commissionee to join a Matter network. |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.16 Commissioning Flow - 11-digit Manual Pairing Code - Negative Scenario [DUT Commissioner]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissioner can take an 11-digit Manual Pairing Code, successfully parse the Manual Pairing Code and prevent the commissioning of any devices when the Manual Pairing Code is invalid.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.11\_MANUAL\_PC

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device acting as a commissionee to join a Matter network. |

## Device Topology

DUT ←→ Commissionee

Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.17 Commissioning Flow - 21-digit Manual Pairing Code - Negative Scenario [DUT Commissioner]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissioner can take a 21-digit Manual Pairing Code, successfully parse the Manual Pairing Code and prevent the commissioning of any devices when the Manual Pairing Code is invalid.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.21\_MANUAL\_PC

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device acting as a commissionee to join a Matter network. |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.18 Commissioning Flow - Commissioning Multiple Devices [DUT - Commissioner]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissioner can successfully commission multiple devices onto a Matter network.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING

## Preconditions

| Doc. Ref. | Condition | Notes |

| 1 | | DUT is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH1 | Test Harness 1 as a Commissionee device with its Onboarding payload QR code printed on the device or in additional provided materials (ex: manual) |
| 3 | TH2 | Test Harness 2 as a Commissionee device with its Onboarding payload QR code printed on the device or in additional provided materials (ex: manual) |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1.a | | | | Place TH1 into commissioning mode using the TH manufacturer's means to be discovered by a commissioner | Verify that TH1 is advertising and able to be discovered by a commissioner. |
| 1.b | | | | Place TH2 into commissioning mode using the TH manufacturer's means to be discovered by a commissioner | Verify that TH2 is advertising and able to be discovered by a commissioner. |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.19 Commissioning Flow - Commission, Unpair and Re-commission Device [DUT Commissionee]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissionee can successfully be commissioned onto a Matter network, unpaired from that Matter network and recommissioned back onto a Matter network.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## · MCORE.DD.QR

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Commissioner is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as a Commissionee device with its Onboarding payload QR code printed on the device or in additional provided materials (ex: manual) |

## Device Topology

## DUT ←→ Commissioner

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | | Place DUT into commissioning mode using the DUT's manufacturer's means to be discovered by the TH Commissioner | Verify that the DUT is advertising and able to be discovered by a commissioner. |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.20 Commissioning Flow - Commission, Unpair and Re-commission Device [DUT Commissioner]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissioner can successfully commission a device onto a Matter network, unpair the device from the Matter network and re-commission the device onto a Matter network.

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.QR\_COMMISSIONING

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee device with its Onboarding payload QR code printed on the device or in additional provided materials (ex: manual) |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | | Place TH into commissioning mode using the TH manufacturer's means to be discovered by the DUT Commissioner | Verify that the TH is advertising and able to be discovered by a commissioner. |

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.21 Commissioning Flow - Commission Multiple-Endpoint Device [DUT Commissioner]

## Purpose

This test case verifies End to End Commissioning Flows and ensures that the Commissioner can successfully commission a device with multiple endpoints onto a Matter network.

## PICS

## · MCORE.ROLE.COMMISSIONER

## · MCORE.DD.QR\_COMMISSIONING

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT is on an operational network and has accurate date, time, timezone, regulatory, and fabric information available. | |

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test Harness as a Commissionee with its Onboarding payload QR code printed on the device or in additional provided materials (ex: manual). Commissionee implements the On/Off light device type on at least 2 (non-zero) endpoints. For example, TH implements the On/Off light device type on endpoints 2 and 4. |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Place TH into commissioning mode using the TH manufacturer's means to be discovered by the DUT Commissioner | Verify that the TH is advertising and able to be discovered by the DUT commissioner. |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-DD-3.22 NFC-based commissioning [DUT as Commissioner] - PROVISIONAL

## Purpose

This test case verifies that the DUT as Commissioner can complete the Commissioning procedure using NFC interface as temporary transport channel.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.SCAN\_NFC
- MCORE.DD.NTL

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness with NFC interface implementing NFC tag and NTL, acting as the Matter Commissionee device. |

## Device Topology

DUT ←→ Commissionee

## Test Procedure

| # | De vic e | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | | Power up the TH Device and put the TH Device in commissioning mode | TH is in a state to be commissioned by the DUT Commissioner |

## Notes/Testing considerations

## TC-DD-3.23 NFC-based commissioning - DUT with power [DUT as Commissionee]

## Purpose

This test case verifies that a DUT, initially powered, can complete the Commissioning procedure using NFC interface as temporary transport channel.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.NFC
- MCORE.DD.NTL

## Preconditions

- A single NFC Reader is connected to the machine used for the test.
- DUT's NFC antenna and TH's NFC antenna are in close proximity.
- DUT is powered and in commissioning mode.

## Required Devices

| # | Device Name | Device Description |
| 2 | DUT | Device Under Test as the Commissionee device, with NFC tag containing an onboarding payload. |

## Test Setup

DUT ←→ TH

| # | Ref | PIC S | Test Step | Expected Outcome |
| 1 | | | Activate and read the tag, then parse the onboarding data to identify the following information: - Discriminator - Passcode - Discovery Capabilities Bitmask | - The tag is detected, activated and read, - The onboarding payload is correctly parsed - NFC Transport Layer bit of 'Discovery Capabilities Bitmask' is set. |

## Notes/Testing considerations

## TC-DD-3.24 NFC-based commissioning - DUT without power [DUT as Commissionee]

## Purpose

This test case verifies that a DUT, initially not powered, can complete the Commissioning procedure using NFC interface as temporary transport channel. During the test, the device should be powered to complete the commissioning on the operational network.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.NFC
- MCORE.DD.NTL

## Preconditions

- A single NFC Reader is connected to the machine used for the test.
- DUT's NFC antenna and TH's NFC antenna are in close proximity.
- DUT is not powered and currently not commissioned to any fabric.

## Required Devices

| # | Device Name | Device Description |
| 2 | DUT | Device Under Test as the Commissionee device, with NFC tag containing an onboarding payload. |

## DUT ←→ TH

## Test Procedure

| # | Ref | PIC S | Test Step | Expected Outcome |
| 1 | | | Activate and read the tag, then parse the onboarding data to identify the following information: - Discriminator - Passcode - Discovery Capabilities Bitmask | - The tag is detected, activated and read, - The onboarding payload is correctly parsed - NFC Transport Layer bit of 'Discovery Capabilities Bitmask' is set. |

Notes/Testing considerations

## Chapter 5. Basic Information Cluster Test Plan

## 5.1. PICS Definition

This section covers the Device Management related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

## 5.1.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| BINFO.S | Does the device implement the Basic Information Cluster as a server? | O | |
| BINFO.C | Does the device implement the Basic Information Cluster as a client? | O | |

## 5.1.2. Server

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| BINFO.S.A0000(DataMo delRevision) | Does the DUT(server) support the DataModelRevision attribute? | BINFO.S :M | |
| BINFO.S.A0001(Vendor Name) | Does the DUT(server) support the VendorName attribute? | BINFO.S :M | |
| BINFO.S.A0002(VendorI D) | Does the DUT(server) support the VendorID attribute? | BINFO.S :M | |
| BINFO.S.A0003(Product Name) | Does the DUT(server) support the ProductName attribute? | BINFO.S :M | |

| BINFO.S.A0004(Product ID) | Does the DUT(server) support the ProductID attribute? | BINFO.S :M | |
| BINFO.S.A0005(NodeLa | Does the DUT(server) support the NodeLabel attribute? | BINFO.S :M | bel) |
| BINFO.S.A0006(Locatio | Does the DUT(server) support the Location attribute? | BINFO.S :M | n) |
| BINFO.S.A0007(Hardwa | Does the DUT(server) support the HardwareVersion attribute? | BINFO.S :M | reVersion) |
| BINFO.S.A0008(Hardwa reVersionString) | Does the DUT(server) support the HardwareVersionString attribute? | BINFO.S :M | |
| BINFO.S.A0009(Softwar | Does the DUT(server) support the SoftwareVersion attribute? | BINFO.S :M | eVersion) |
| BINFO.S.A000a(Softwar eVersionString) | Does the DUT(server) support the SoftwareVersionString attribute? | BINFO.S :M | |
| BINFO.S.A000b(Manufa cturingDate) | Does the DUT(server) support the ManufacturingDate attribute? | BINFO.S : O | |
| BINFO.S.A000c(PartNu | Does the DUT(server) support the PartNumber attribute? | BINFO.S : O | mber) |
| BINFO.S.A000d(Product | Does the DUT(server) support the ProductURL attribute? | BINFO.S : O | URL) |
| BINFO.S.A000e(Product | Does the DUT(server) support the ProductLabel attribute? | BINFO.S : O | Label) |
| BINFO.S.A000f(SerialNu | Does the DUT(server) support the SerialNumber attribute? | BINFO.S : O | mber) |

| BINFO.S.A0010(LocalCo nfigDisabled) | Does the DUT(server) support the LocalConfigDisabled attribute? | BINFO.S : O | |
| BINFO.S.A0011(Reacha ble) | Does the DUT(server) support the Reachable attribute? | BINFO.S : O | |
| BINFO.S.A0012(UniqueI D) | Does the DUT(server) support the UniqueID attribute? | BINFO.S :M | |
| BINFO.S.A0013(Capabili tyMinima) | Does the DUT(server) support the CapabilityMinima attribute? | BINFO.S :M | |
| BINFO.S.A0014(Product Appearance) | Does the DUT(server) support the ProductAppearance attribute? | BINFO.S : O | |
| BINFO.S.A0015(Specific ationVersion) | Does the DUT(server) support the SpecificationVersion attribute? | BINFO.S :M | |
| BINFO.S.A0016(MaxPat hsPerInvoke) | Does the DUT(server) support the MaxPathsPerInvoke attribute? | BINFO.S :M | |
| BINFO.S.A0017(DeviceL | Does the DUT(server) support the DeviceLocation attribute? | BINFO.S : P, O | ocation) |
| BINFO.S.A0018(Configu rationVersion) | Does the DUT(server) support the ConfigurationVersion attribute? | BINFO.S :M | |

## Manual controllable

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| BINFO.S.M.DeviceConfi gurationChange | Can the configuration of the DUT be changed at run-time? | BINFO.S: O | |

## Events

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| BINFO.S.E00(StartUp) | Does the DUT(server) support the StartUp event? | BINFO.S :M | |
| BINFO.S.E01(ShutDown ) | Does the DUT(server) support the ShutDown event? | BINFO.S : O | |
| BINFO.S.E02(Leave) | Does the DUT(server) support the Leave event? | BINFO.S : O | |
| BINFO.S.E03(Reachable Changed) | Does the DUT(server) support the ReachableChanged event? | BINFO.S.A0011(Reacha ble) | |

## 5.1.3. Client

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| BINFO.C.A0005(NodeLa bel) | Does the DUT(client) support the NodeLabel attribute? | O | |

## 5.2. PIXIT Definition

This section covers the Basic Information Cluster's Test Plan related PIXIT items that might be required in the following test cases.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PIXIT.BINFO.PrimaryCo lor | ProductAppearance.Pri maryColor should reflect the product's color | BINFO.S.A0014(Product Appearance) | |
| PIXIT.BINFO.Finish | ProductAppearance.Fin ish should reflect the product's finish | BINFO.S.A0014(Product Appearance) | |

## 5.3. Test Case List

| TC UUID | Test Case Name |
| TC-BINFO-2.1 | Attributes [DUT-Server] |
| TC-BINFO-2.2 | Events [DUT-Server] |
| TC-BINFO-3.1 | Appearance Attribute DUT as Server |
| TC-BINFO-3.2 | ConfigurationVersion Attribute DUT as Server |

## 5.4. Test Cases

## 5.4.1. DUT as Server

## TC-BINFO-2.1 Attributes [DUT-Server]

## Purpose

Verify if all the server attributes have been implemented correctly on the DUT.

## PICS

- BINFO.S

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | Commission DUT to TH | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness that will query/modify for Basic Information cluster attributes. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

This will describe how to set up for testing.

| # | PICS | Test Step | Expected Outcome |
| 1 | | TH reads DataModelRevision from the DUT. | • Verify that the value is 19 The following values is applicable for the listed Matter version: • DataModelRevision is 1 or 16 for Matter 1.0 and 1.1. • DataModelRevision is 17 for Matter 1.2 and 1.3. • DataModelRevision is 18 for Matter 1.4 and 1.4.1. • DataModelRevision is 19 for Matter 1.4.2 and 1.5. |
| 2 | | TH reads VendorName from the DUT. | • Verify that the VendorName returns a string with max 32 bytes |
| 5 | | TH reads ProductID from the DUT. | • Verify that the value is in the inclusive range of 1 to 65534 and not 0 |
| 8 | | TH reads HardwareVersion from the DUT. | • Verify that the value is in range of 0 to 65534 |

| # | PICS | Test Step | Expected Outcome |
| 9 | | TH reads HardwareVersionString from the DUT. | • Verify it is of type string. • Verify it has a value length in the range of 1 to 64 bytes |
| 10 | | TH reads SoftwareVersion from the DUT. | • Verify that the value is the range of 0 to 4294967294 |
| 12 | BINFO.S.A000b (Manufacturin gDate) | TH reads ManufacturingDate from the DUT. | • Verify it is of type string. • Verify it has length in the inclusive range of 8 to 16 bytes. • Verify if the first 8 characters specify date according to ISO 8601, i.e, YYYYMMDD. |

| # | PICS | Test Step | Expected Outcome |
| 20 | | TH reads CapabilityMinima attribute from the DUT | • Verify that the CaseSessionsPerFabric field is in the inclusive range of 3 to 10000 • Verify that the SubscriptionsPerFabric field is in the inclusive range of 3 to 10000 • If the ClusterRevision is 6 or above: ◦ Verify that the SimultaneousInvocationsSupported field is in the inclusive range of 1 to 10000 ◦ Verify that the SimultaneousWritesSupported field is in the inclusive range of 1 to 10000 ◦ Verify that the ReadPathsSupported field is in the inclusive range of 9 to 10000 ◦ Verify that the SubscribePathsSupported field is in |

| # | PICS | Test Step | Expected Outcome |
| NOT E | | DeviceLocation is not currently supported | • The DeviceLocation verification steps (24-28) are conditionally included via {includeDeviceLocation}. • which intentionally hides these steps in the test plan and causes the python test module to skip them currently. • This is expected and avoids confusion when step numbers appear to 'jump'. |
| 29 | BINFO.S.A0018 (Configuration Version) | TH reads ConfigurationVersion from the DUT. | • Verify that the value is in the range of 1 to 4294967295 |

## TC-BINFO-2.2 Events [DUT-Server]

## Purpose

Verify if all the events have been implemented correctly on the DUT.

## PICS

- BINFO.S

## Precondition

| 2 | BINFO.S.A000 9(SoftwareVe rsion) | TH reads SoftwareVersion attribute from DUT and saves for future use | |
| 3 | BINFO.S.A001 1(Reachable) | TH reads Reachable attribute from DUT and saves for future use | Should be True |
| 4 | BINFO.S.E00( StartUp) &#124; BINFO.S.E01( ShutDown) &#124; BINFO.S.E02( Leave) &#124; BINFO.S.E03( ReachableCh anged) | TH subscribes to StartUp, ShutDown, Leave and ReachableChanged events on the Basic Information cluster of the DUT | |
| 5 | | TH saves the FabricIndex during commissioning | |

| # | Device Name | Device Description |
| 1 | TH | Test harness which will be used to send and receive events and messages to the DUT |
| 2 | DUT | DUT which will send events to the TH |

## Device Topology

DUT and TH are on the same fabric

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 11.1.6.2- 0 | BINFO.S.E00( StartUp) | • Reboot the DUT • TH reads the StartUp event from DUT | • Verify that the DUT sends the StartUp event before other events to TH • Verify that the SoftwareVersion field in the event data is equivalent to the precondition • Verify that StartUp event has priority set as CRITICAL |
| 2 | 11.1.6.2- 1 | BINFO.S.E01( ShutDown) | TH subscribes to the ShutDown event on the DUT. Shutdown DUT. | Verify that ShutDown event is received from DUT and has priority set as CRITICAL |

## TC-BINFO-3.1 Appearance Attribute DUT as Server

## Purpose

Verify if the appearance is correctly set within the allowed ranges. Finish and PrimaryColor should reasonably reflect the appearance of the product.

## PICS

- BINFO.S.A0014(ProductAppearance)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | TestStep | Expected Outcome |
| 0 | DUT commissioned if not already done | |
| 1 | TH reads ProductAppearance attribute from the DUT. | Verify the finish is a valid ProductFinishEnum and the PrimaryColor is a valid ColorEnum |

## TC-BINFO-3.2 ConfigurationVersion Attribute DUT as Server

## Purpose

Verify that the ConfigurationVersion attribute is increased if the configuration of the node is changed.

## PICS

- BINFO.S
- BINFO.S.M.DeviceConfigurationChange

## Precondition

| Ref | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Test Step | Expected Outcome |
| 2 | Change the configuration version in a way which results in functionality to be added or removed (e.g. rewire thermostat to support a new mode) | |

## Chapter 6. Node Operational Credentials Cluster Test Plan

## 6.1. PICS Definition

This section covers the Node Operational Credentials Cluster related PICS items that are referenced in the following test cases.

## 6.1.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| OPCREDS.S | Does the device implement the Node Operational Credentials Cluster as a server? | O | |
| OPCREDS.C | Does the device implement the Node Operational Credentials Cluster as a client? | O | |

## 6.1.2. Server

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| OPCREDS.S.A0000(NOC s) | Does the DUT(server) support the NOCs list attribute? | OPCREDS.S :M | |
| OPCREDS.S.A0001(Fabri cs) | Does the DUT(server) support the Fabrics list attribute? | OPCREDS.S :M | |
| OPCREDS.S.A0002(Supp ortedFabrics) | Does the DUT(server) support the SupportedFabrics attribute? | OPCREDS.S :M | |
| OPCREDS.S.A0003(Com missionedFabrics) | Does the DUT(server) support the CommissionedFabrics attribute? | OPCREDS.S :M | |

| OPCREDS.S.A0004(Trust edRootCertificates) | Does the DUT(server) support the TrustedRootCertificates attribute? | OPCREDS.S :M |
| OPCREDS.S.A0005(Curr entFabricIndex) | Does the DUT(server) support the CurrentFabricIndex attribute? | OPCREDS.S :M |
| MCORE.DD.EXTENDED_ DISCOVERY | Does the DUT(server) support Extended Discovery through DNS-SD advertisements when device is not in commissioning mode? | OPCREDS.S : O |

## Commands received

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| OPCREDS.S.C00.Rsp(Att estationRequest) | Does the Device(Server) implement receiving the AttestationRequest command? | OPCREDS.S :M | |
| OPCREDS.S.C02.Rsp(Cer tificateChainRequest) | Does the Device(Server) implement receiving the CertificateChainReques t command? | OPCREDS.S :M | |
| OPCREDS.S.C04.Rsp(CS RRequest) | Does the Device(Server) implement receiving the CSRRequest command? | OPCREDS.S :M | |
| OPCREDS.S.C06.Rsp(Ad dNOC) | Does the Device(Server) implement receiving the AddNOC command? | OPCREDS.S :M | |
| OPCREDS.S.C07.Rsp(Up dateNOC) | Does the Device(Server) implement receiving the UpdateNOC command? | OPCREDS.S :M | |
| OPCREDS.S.C09.Rsp(Up dateFabricLabel) | Does the Device(Server) implement receiving the UpdateFabricLabel command? | OPCREDS.S :M | |

| OPCREDS.S.C0a.Rsp(Re moveFabric) | Does the Device(Server) implement receiving the RemoveFabric command? | OPCREDS.S :M | |
| OPCREDS.S.C0b.Rsp(Ad dTrustedRootCertificate | Does the Device(Server) implement receiving the AddTrustedRootCertific ate command? | OPCREDS.S :M | ) |
| OPCREDS.S.C0c.Rsp(Set VIDVerificationStateme | Does the Device(Server) implement receiving the SetVIDVerificationState ment command? | OPCREDS.S : P,M | nt) |
| OPCREDS.S.C0d.Rsp(Sig nVIDVerificationReque st) | Does the Device(Server) implement receiving the SignVIDVerificationReq uest command? | OPCREDS.S : P,M | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| OPCREDS.S.C01.Tx(Atte stationResponse) | Does the Device(Server) invoking/generating the AttestationResponse command? | OPCREDS.S :M | |
| OPCREDS.S.C03.Tx(Certi ficateChainResponse) | Does the Device(Server) invoking/generating the CertificateChainRespon se command? | OPCREDS.S :M | |
| OPCREDS.S.C05.Tx(CSR Response) | Does the Device(Server) invoking/generating the CSRResponse command? | OPCREDS.S :M | |
| OPCREDS.S.C08.Tx(NOC Response) | Does the Device(Server) invoking/generating the NOCResponse command? | OPCREDS.S :M | |
| OPCREDS.S.C0e.Tx(Sign VIDVerificationRespons e) | Does the Device(Server) invoking/generating the SignVIDVerificationRes ponse command? | OPCREDS.S : P,M | |

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| OPCREDS.C.A0000(NOC s) | Does the DUT(client) have access privileges for the NOC list attribute implemented on the server? | OPCREDS.C : O | |
| OPCREDS.C.A0001(Fabr ics) | Does the DUT(client) have access privileges for the SupportedFabrics attribute implemented on the server? | OPCREDS.C : O | |
| OPCREDS.C.A0002(Supp ortedFabrics) | Does the DUT(client) have access privileges for the SupportedFabrics attribute implemented on the server? | OPCREDS.C : O | |
| OPCREDS.C.A0003(Com missionedFabrics) | Does the DUT(client) have access privileges for the CommissionedFabrics attribute implemented on the server? | OPCREDS.C : O | |
| OPCREDS.C.A0004(Trus tedRootCertificates) | Does the DUT(client) have access privileges for the TrustedRootCertificates attribute implemented on the server? | OPCREDS.C : O | |
| OPCREDS.C.A0005(Curr entFabricIndex) | Does the DUT(client) have access privileges for the CurrentFabricIndex attribute implemented on the server? | OPCREDS.C : O | |

## Commands received

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| OPCREDS.C.C01.Rsp(Att estationResponse) | Does the Device(Client) invoking/generating the AttestationResponse command? | OPCREDS.C : O | |
| OPCREDS.C.C03.Rsp(Cer tificateChainResponse) | Does the Device(Client) invoking/generating the CertificateChainRespon se command? | OPCREDS.C : O | |
| OPCREDS.C.C05.Rsp(CS RResponse) | Does the Device(Client) invoking/generating the CSRResponse command? | OPCREDS.C : O | |
| OPCREDS.C.C08.Rsp(NO CResponse) | Does the Device(Client) invoking/generating the NOCResponse command? | OPCREDS.C : O | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| OPCREDS.C.C00.Tx(Atte stationRequest) | Does the DUT(client) support transmitting of AttestationRequest command? | OPCREDS.C : O | |
| OPCREDS.C.C02.Tx(Cert ificateChainRequest) | Does the DUT(client) support transmitting of CertificateChainReques t command? | OPCREDS.C : O | |
| OPCREDS.C.C04.Tx(CSR Request) | Does the DUT(client) support transmitting of CSRRequest command? | OPCREDS.C : O | |
| OPCREDS.C.C06.Tx(Add NOC) | Does the DUT(client) support transmitting of AddNOC command? | OPCREDS.C : O | |
| OPCREDS.C.C07.Tx(Upd ateNOC) | Does the DUT(client) support transmitting of UpdateNOC command? | OPCREDS.C : O | |

| OPCREDS.C.C09.Tx(Upd ateFabricLabel) | Does the DUT(client) support transmitting of UpdateFabricLabel command? | OPCREDS.C : O |
| OPCREDS.C.C0a.Tx(Rem oveFabric) | Does the DUT(client) support transmitting of RemoveFabric command? | OPCREDS.C : O |
| OPCREDS.C.C0b.Tx(Add TrustedRootCertificate) | Does the DUT(client) support transmitting of AddTrustedRootCertific ate command? | OPCREDS.C : O |

## 6.2. Test Case List

| TC UUID | Test Case Name |
| TC-OPCREDS-3.1 | Attribute-NOCs,TrustedRootCertificates list validation [DUT-Server] |
| TC-OPCREDS-3.2 | Attribute-CurrentFabricIndex validation [DUT-Server] |
| TC-OPCREDS-3.3 | Attribute-NOCs,Commands[DUT-Client] |
| TC-OPCREDS-3.4 | UpdateNOC-Error Condition [DUT-Server] |
| TC-OPCREDS-3.5 | NOC Check for UpdateNOC [DUT-Server] |
| TC-OPCREDS-3.6 | Last Fabric removal validation [DUT-Server] |
| TC-OPCREDS-3.7 | Add Second Fabric over CASE [DUT-Server] |
| TC-OPCREDS-3.8 | VID Verification Attribute, Commands Error Conditions [DUT as Server] |

## 6.3. Test Cases

## 6.3.1. DUT as Server

## TC-OPCREDS-3.1 Attribute-NOCs, TrustedRootCertificates list validation [DUT-Server]

## Purpose

The following checks are covered by this test:

## AddNOC error cases

- (25) Prior AddNOC command successfully executed in fail-safe timer period → CONSTRAINT\_ERROR
- (70) Prior CSRRequest has IsForUpdateNOC set to true → CONSTRAINT\_ERROR

- (63) Adding NOC for &lt;Root Public Key, FabricID&gt; already on device → FabricConflict
- ([invalid-public-key]) Public Key in NOC does not match Public Key in NOCSR → InvalidPublicKey
- (22) Validation error (signed by TrustedRoot not in table) → InvalidNOC
- (51) No prior CSR matching NOC → MissingCsr
- (23) CaseAdminSubject field is not a valid ACL subject → InvalidAdminSubject
- (77) ICACValue field is not a valid ICAC (invalid Subject DN) → InvalidNOC

## AddNOC positive cases

- (24) Valid AddNOC with CaseAdminSubject is NodeID
- ([add-noc-cat]) Valid AddNOC with CaseAdminSubject is CAT
- ([fabrics-table-ok]) AddNOC results in generation of new fabric and is reflected in fabrics table
- (39) AddNOC results in entry in NOC table
- (42) AddNOC results in IPK added to Groups Management cluster
- (41) AddNOC results in ACL added to ACL cluster
- ([multiple-nocs], 48) Multiple NOCs can be added and are reflected in the NOC and fabric tables
- ([fill-fabric-table]) Able to add NumSupportedFabrics fabrics will full-size certificates
- (78) Valid AddNOC with Certificate Chain that omits ICAC (NOC signed directly by Root)

## AddTrustedRootCertificate error cases

- (18) Adding a second trusted root certificate in the same fail-safe period → CONSTRAINT\_ERROR
- (12) Validity check fails → INVALID\_COMMAND

## AddTrustedRootCertificate positive cases

- ([root-cert-cmd-ok], 21) Valid AddTrustedRootCertificate is reflected in TrustedRootCertificates attribute
- (16) Adding an exact duplicate succeeds with no change to list
- ([multiple-trusted-root-certs]) Multiple Trusted Root Certificates can be added and are reflected in the Trusted Root Certificate attribute

## NOC attribute

- (26) NOC attribute contains successfully added NOCs
- (27) NOC attribute is not writeable

## TrustedRootCertificates attribute

- (21) TrustedRootCertificates attribute contains successfully added Trusted root certificates
- (20) TrustedRootCertificates attribute is not writeable

## Failsafe tests

- (34, 35, 36) failsafe results in no changes to fabric table, noc table, trusted root table

## UpdateFabricLabel error cases

- (47) duplicate label cannot be added → CONSTRAINT\_ERROR

UpdateFabricLabel positive cases

- (29, 31) UpdateFabricLabel successfully adds label to fabric
- (48) Multiple fabrics can each have a different label

## RemoveFabric error cases

- (81) Invalid fabric index → InvalidFabricIndex

## PICS

- OPCREDS.S

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | server |
| 2 | TH0 | client - already commissioned DUT |
| 3 | TH1 | client - DUT not previously commissioned by this client, separate fabric |
| 4 | TH2 | client - DUT not previously commissioned by this client, separate fabric |
| 5 | TH3 | client - DUT not previously commissioned by this client, separate fabric |

## Device Topology

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| 1 | C.11.19.8 .1 | TH0 opens a commissioning window on the DUT | |
| 2 | C.11.10.5 .2 | TH0 reads the BasicCommissioningInfo field from the General commissioning cluster saves MaxCumulativeFailsafeSeco nds as failsafe_max | |
| 3 | C.4.14.1 | TH1 opens a PASE connection to the DUT | |
| 4 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with the ExpiryLengthSeconds field set to failsafe_max | Verify that the DUT sends ArmFailSafeResponse Command to TH1 with field ErrorCode as 'OK'(0) |
| 5 | C.11.18.6 .5 | TH1 Sends CSRRequest command with a random 32- byte nonce | • Verify that the DUT responds with the CSRResponse Command |

| 6 C.6.4 |

| 7 | C.6.4 | • TH1 obtains or generates Root Certificate with a different Root CA ID and the corresponding ICAC, NOC and IPK using the CSR elements from step 5 • Save RCAC as Root_CA_Certificate_TH1 _2 • Save ICAC as Intermediate_Certificat e_TH1_2 • Save NOC as Node_Operational_Certif icate_TH1_2 • Save IPK as IPK_TH1_2 | |
| 8 | C.6.4 | TH1 generates an INVALID Root Certificate where the signature does not match the public key and saves it as Root_CA_Malformed | |
| 9 | C.11.18.5 .5 | TH1 reads the trusted root cert list from the DUT. Save the list size as trusted_root_original_size | |
| 10 | C.11.18.5 .2 | TH1 reads the fabrics attribute from the DUT. Save the list size as fabrics_original_size | |
| 11 | C.11.18.5 .1 | TH1 reads the NOCs attribute from the DUT using a non-fabric-filtered read. Save the list size as nocs_original_size | |
| 12 | C.11.18.5 .5 | TH1 sends AddTrustedRootCertificate command to DUT to install Root_CA_Malformed | Verify that AddTrustedRootCertificate Command fails by sending the status code as INVALID_COMMAND |
| 13 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificate attribute | Verify it contains only trusted_root_original_size entries |

| 14 | C.11.18.6 .13 | TH1 sends AddTrustedRootCertificate command to DUT with RootCACertificate set to Root_CA_Certificate_TH1 | Verify that AddTrustedRootCertificate Command succeeds by sending the status code as SUCCESS |
| 15 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificate attribute | Verify it contains trusted_root_original_size + 1 entries |
| 16 | C.11.18.6 .13 | TH1 sends AddTrustedRootCertificate command to DUT again with the RootCACertificate field set to Root_CA_Certificate_TH1 | Verify that the returned Status Code is SUCCESS |
| 17 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificate attribute | Verify it contains trusted_root_original_size + 1 entries |
| 18 | C.11.18.6 .13 | TH1 sends AddTrustedRootCertificate command to DUT again with the RootCACertificate field set to Root_CA_Certificate_TH1_2 | Verify that the returned Status Code is CONSTRAINT_ERROR |
| 19 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificates list from DUT and saves as TrustedRootsList | Verify that there are trusted_root_original_size + 1 entries |
| 20 | C.11.18.5 .5 | TH1 appends Root_CA_Certificate_TH1_2 to TrustedRootsList and writes the TrustedRootCertificates attribute with that value | Verify that the returned status code is UNSUPPORTED_WRITE |
| 21 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificates list from DUT | Verify that there are trusted_root_original_size + 1 entries |

| 22 | C.11.18.6 .8 | • TH1 sends the AddNOC Command to DUT with the following fields: • NOCValue as Node_Operational_Certif icate_TH1_2 • ICACValue as Intermediate_Certificat e_TH1_2 • IpkValue as IPK_TH1_2 • CaseAdminSubject as the NodeID of TH1 • AdminVendorId as the Vendor ID of TH1 | • Verify that DUT responds with NOCResponse command with status code InvalidNOC |
| 23 | C.11.18.6 .8 | • TH1 sends the AddNOC Command to DUT with the following fields: • NOCValue as | • Verify that DUT responds with NOCResponse command with status code InvalidAdminSubject |

| 24 | C.11.18.6 .8 | • TH1 sends the AddNOC Command to DUT with the following fields: • NOCValue as Node_Operational_Certif icate_TH1 • ICACValue as Intermediate_Certificat e_TH1 • IpkValue as IPK_TH1 • CaseAdminSubject as the NodeID of TH1 • AdminVendorId as the Vendor ID of TH1 | Verify that DUT responds with NOCResponse command with status code OK |
| 25 | C.11.18.6 .8 | • TH1 re-sends the AddNOC Command to DUT with the following fields: • NOCValue as Node_Operational_Certif icate_TH1_1 • ICACValue as Intermediate_Certificat e_TH1_1 • IpkValue as IPK_TH1_1 • CaseAdminSubject as the NodeID of TH1 • AdminVendorId as the Vendor ID of TH1 | Verify that DUT responds with status code CONSTRAINT_ERROR |
| 26 | C.11.18.5 .1 | TH1 reads the NOCs attribute from DUT using a fabric-filtered read and saves the list as NOCList | Verify that the list contains one entry with NOC field Node_Operational_Certificate_TH1 and ICAC field Intermediate_Certificate_TH1 |
| 27 | C.11.18.5 .1 | TH1 modifies the NOC list to use Node_Operational_Certificat e_TH1_2 and Intermediate_Certificate_TH 1_2 | Verify that the returned status code is UNSUPPORTED_WRITE |

| 28 | C.11.18.5 .1 | TH1 reads the NOCs attribute from DUT using a fabric-filtered read | Verify that the list contains one entry with NOC field Node_Operational_Certificate_TH1 and ICAC field Intermediate_Certificate_TH1 |
| 29 | C.11.18.6 .11 | TH1 sends UpdateFabricLabel command with 'Label 1' as Label field to DUT | • Verify that the DUT responds with the NOCResponse Command with status OK |
| 30 | C.11.18.5 .2 | TH1 reads the Fabrics Attribute from DUT using a fabric-filtered read | Verify that there is only 1 entry |
| 31 | C.11.18.5 .2 | | • Read the other fields from FabricDescriptorStruct 1. RootPublicKey 2. VendorID 3. FabricID 4. NodeID 5. Label • Verify that the size of RootPublicKey is exactly 65 bytes • Verify that the RootPublicKey matches Root_Public_Key_TH1 • Verify that the NodeID is the same as the matter-node-id field in the NOC sent with AddNOC Command • Verify that the VendorID is the same as the AdminVendorID sent with AddNOC Command • Verify that the FabricID is the same as the matter-fabric-id field in the NOC sent with AddNOC Command • Verify that the Label field has value "Label 1" |
| 32 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds field set to 0 | |
| 33 | C.4.14.1 | TH1 reconnects to the DUT over PASE | |

| 34 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificates list from DUT | Verify that list contains trusted_root_original_size entries |
| 35 | C.11.18.5 .1 | TH1 reads the NOCs attribute from DUT using a non-fabric-filtered read | Verify that the list contains nocs_original_size entries |
| 36 | C.11.18.5 .2 | TH1 reads the Fabrics attribute from the DUT using a non-fabric-filtered read | Verify that the list contains fabrics_original_size entries |
| 37 | {REF_CO DE}.5.5 | TH1 fully commissions DUT onto the fabric, using a valid set of certificates | Verify that TH1 successfully completes commissioning |
| 38 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificates list from DUT | Verify that there are trusted_root_original_size + 1 entries |
| 39 | C.11.18.5 .1 | TH1 reads the NOCs attribute from DUT using a non-fabric-filtered read | Verify that the list contains nocs_original_size + 1 entries |
| 40 | C.11.18.5 .2 | TH1 reads the Fabrics attribute from DUT using a non-fabric-filtered | Verify that the list contains fabrics_original_size + 1 entries |
| 41 | C.9.10.5. 3 | TH1 reads the ACL attribute from the Access Control cluster | • Verify that the returned list includes an entry with: • Fabric index of TH1_FABRICINDEX • Administer privilege (5) • CASE AuthMode (2) • Includes the NodeID of TH1 in the list of subjects |
| 43 | C.11.18.6 .11 | TH1 sends UpdateFabricLabel command with 'Label 1' as Label field to DUT | Verify status OK |
| 44 | C.11.19.8 .1 | TH1 sends an OpenCommissioningWindo wcommand to the Administrator Commissioning cluster | |

| 45 | {REF_CO DE}.5.5 | TH2 fully commissions the DUT | |
| 46 | C.11.18.6 .11 | TH2 sends UpdateFabricLabel command with 'Label 2' as Label field to DUT | • Verify that the DUT responds with the NOCResponse Command with status OK |
| 47 | C.11.18.6 .11 | TH2 sends UpdateFabricLabel command with 'Label 1' as Label field to DUT | • Verify that the DUT responds with the NOCResponse Command with status LabelConflict |
| 48 | C.11.18.5 .2 | Read the Fabrics List from DUT using a non-fabric- filtered read | • Verify that there are 'fabrics_original_size` + 2 entries • Verify that one entry has Label field 'Label 1' • Verify that the other entry has label field 'Label 2' • Verify that the list item with Label 'Label 1' has VendorID equal to the vendor ID of TH1 • Verify that the list item with Label 'Label 2' has VendorID equal to the vendor ID of TH2 |
| 49 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with the ExpiryLengthSeconds field set to failsafe_max | Verify that the DUT sends ArmFailSafeResponse Command to TH1 with field ErrorCode as 'OK'(0) |
| 50 | C.11.18.6 .13 | TH1 sends AddTrustedRootCertificate command to DUT with RootCACertificate set to Root_CA_Certificate_TH1_1 | Verify that AddTrustedRootCertificate Command succeeds by sending the status code as SUCCESS |

| 51 | C.11.18.6 .8 | • TH1 sends the AddNOC Command to DUT with the following fields: • NOCValue as Node_Operational_Certif icate_TH1_1 • ICACValue as Intermediate_Certificat e_TH1_1 • IpkValue as IPK_TH1_1 • CaseAdminSubject as the NodeID of TH1 • AdminVendorId as the Vendor ID of TH1 | Verify that DUT responds with status code MissingCsr |
| 52 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | |
| 53 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to failsafe_max | |
| 54 | C.11.18.6 .5 | TH1 Sends CSRRequest command with a random 32- byte nonce | |
| 55 | C.6.4 | TH1 generates a new RCAC, ICAC, NOC and IPK using the csr returned in step 5 (ie, NOT the most recent CSR) and saves them as TH1_RCAC_bad_csr , TH1_ICAC_bad_csr , TH1_NOC_bad_csr and TH1_IPK_bad_csr | |
| 57 | C.11.18.6 .8 | TH1 sends the AddNOC Command to DUT using TH1_ICAC_bad_csr , TH1_NOC_bad_csr and TH1_IPK_bad_csr | Verify that DUT responds with status code InvalidPublicKey |

| 58 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | |
| 59 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to failsafe_max | |
| 60 | C.11.18.6 .5 | TH1 Sends CSRRequest command with a random 32- byte nonce | |
| 61 | C.6.4 | TH1 obtains or generates a NOC and ICAC using the CSR elements from step 60 with a different NodeID, but the same Root CA Certificate and fabric ID as step 6. Save as Node_Operational_Certificat es_TH1_fabric_conflict and Intermediate_Certificate_TH 1_fabric_conflict | |
| 62 | C.11.18.6 .13 | TH1 sends the AddTrustedRootCert command using the certs generated in step 61 | |
| 63 | C.11.18.6 .8 | • TH1 sends the AddNOC Command to DUT with the following fields: • NOCValue as Node_Operational_Certif icate_TH1_fabric_confli ct • ICACValue as Intermediate_Certificat e_TH1_fabric_conflict • CaseAdminSubject as the NodeID of TH1 • AdminVendorId as the Vendor ID of TH1 | Verify that DUT responds with status code FabricConflict |
| 64 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that the DUT sends ArmFailSafeResponse Command to TH1 with field ErrorCode as 'OK'(0) |

| 65 | C.11.18.5 .5 | TH1 reads the TrustedRootCertificates list from DUT | Verify that list contains trusted_root_original_size + 2 entries |
| 66 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with the ExpiryLengthSeconds field set to failsafe_max | Verify that the DUT sends ArmFailSafeResponse Command to TH1 with field ErrorCode as 'OK'(0) |
| 67 | C.11.18.6 .5 | TH1 Sends CSRRequest command with a random 32- byte nonce and the IsForUpdateNOC field set to true | |
| 68 | C.6.4 | • TH1 obtains or generates a NOC, Root CA Certificate, ICAC using the CSR elements from the previous step • Save RCAC as Root_CA_Certificate_TH1 _3 • Save ICAC as Intermediate_Certificat e_TH1_3 • Save NOC as Node_Operational_Certif | |
| 69 | C.11.18.6 .13 | TH1 sends AddTrustedRootCertificate command to DUT with RootCACertificate set to Root_CA_Certificate_TH1_3 | Verify that AddTrustedRootCertificate Command succeeds by sending the status code as SUCCESS |

| 70 | C.11.18.6 .8 | • TH1 sends the AddNOC Command to DUT with the following fields: • NOCValue as Node_Operational_Certif icate_TH1_3 • ICACValue as Intermediate_Certificat e_TH1_3 • CaseAdminSubject as the NodeID of TH1 • AdminVendorId as the Vendor ID of TH1 | Verify that DUT responds with status code CONSTRAINT_ERROR |
| 71 | C.11.10.6 .2 | TH1 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that the DUT sends ArmFailSafeResponse Command to TH1 with field ErrorCode as 'OK'(0) |
| 72 | | • Skip to step 80 if the SpecificationVersion attribute in the BasicInformation cluster is either missing or has a value < 0x01060000 (i.e. reported Matter version is < 1.6). • Create a new CA and Controller (TH3) configured to generate a certificate chain without an ICAC, then TH3 establishes PASE to DUT. | |
| 73 | C.11.10.6 .2 | TH3 sends ArmFailSafe command to the DUT with the ExpiryLengthSeconds field set to failsafe_max | Verify that the DUT sends ArmFailSafeResponse Command to TH3 with field ErrorCode as 'OK'(0) |
| 74 | C.11.18.6 .5 | TH3 Sends CSRRequest command with a random 32- byte nonce and saves the response as csrResponseNoIcac | |

| 75 | C.6.4 | • TH3 obtains or generates a new RCAC and NOC but Omits ICAC in the Certificate Chain • Save RCAC as Root_CA_Certificate_TH3 • Save NOC as Node_Operational_Certif icate_TH3 | |
| 76 | C.11.18.6 .13 | TH3 sends the AddTrustedRootCert command using the certs generated in step 75 | |
| 77 | C.11.18.6 .8 | • TH3 sends the AddNOC Command to DUT using the certs generated in step 75. The RCAC is re- used and presented as an ICAC: • NOCValue as Node_Operational_Certif icate_TH3 • ICACValue as Root_CA_Certificate_TH3 • CaseAdminSubject as the NodeID of TH3 • AdminVendorId as the Vendor ID of TH3 | Verify that DUT responds with status code InvalidNOC |
| 78 | C.11.18.6 .8 | • TH3 sends the AddNOC Command to DUT using the certs generated in step 75. This time, the ICAC is omitted: • NOCValue as Node_Operational_Certif icate_TH3 • ICACValue as None • CaseAdminSubject as the NodeID of TH3 | Verify that DUT responds with status code OK |

| 79 | C.11.10.6 .2 | TH3 sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that the DUT sends ArmFailSafeResponse Command to TH3 with field ErrorCode as 'OK'(0) |
| 80 | C.11.18.5 .6 | TH2 reads its fabric index from the CurrentFabricIndex attribute and saves as FabricIndex_TH2 | |
| 81 | C.11.18.6 .12 | TH2 sends RemoveFabric command with Fabric Index as FabricIndexTH2 + 5 (Invalid Fabric Index) to DUT | Verify that DUT sends NOCResponse Command with StatusCode of InvalidFabricIndex |
| 82 | C.11.18.5 .2 | TH2 reads the Fabrics List from DUT using a non- fabric-filtered read | Verify that there are fabrics_original_size + 2 entries |
| 83 | C.11.18.5 .6 | TH1 reads its fabric index from the CurrentFabricIndex attribute and saves as TH1_FABRICINDEX | |
| 84 | C.11.18.6 .12 | TH0 sends RemoveFabric command with Fabric Index as TH1_FABRICINDEX | Verify that DUT sends NOCResponse Command with StatusCode of OK |
| 85 | C.11.18.6 .12 | TH0 sends RemoveFabric command with Fabric Index as TH2_FABRICINDEX | Verify that DUT sends NOCResponse Command with StatusCode of OK |

## Notes/Testing considerations

Step 15 currently fails in the SDK and is therefore off in the test. Please see (#30798) Step 68 Currently fails in the SDK and is therefore off in the test. Please see (#3126). This also affects step 69, which is also off in the automation.

## TC-OPCREDS-3.2 Attribute-CurrentFabricIndex validation [DUT-Server]

## Purpose

To Verify that the CurrentFabricIndex attribute satisfies the following conditions:

1. CurrentFabricIndex is same as the accessing fabric index in the DUT
2. CurrentFabricIndex references an entry in the fabric list

- OPCREDS.S

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | server |
| 2 | CR1 | client |
| 3 | CR2 | client (separate fabric) |
| 3 | CR3 | client (separate fabric) |

## Spec references

- C.11.18 - Node Operational Credential cluster
- C.11.18.5.6 - CurrentFabricIndex attribute

## Test Procedure

| # | TestStep | Expected Outcome |
| 0 | Commission DUT to CR1 if not already done | |

| 1 | Create a new controller on a new fabric called CR2. Commission the new controller from CR1 as follows: • CR1 sends an ArmFailsafe command, followed by a CSRRequest command. • Generate credentials on CR2 using the returned CSR. • Save the RCAC as rcac_CR2. Save the ICAC as `icac_CR2 . Save the NOC as noc_CR2 . Save the IPK as ipk_CR2. • CR1 sends the AddTrustedRootCertificate command with rcac_CR2 - CR1 sends the AddNOC command with the fields set as follows: ◦ NOCValue: noc_CR2 ◦ ICACValue: icac_CR2 ◦ IPKValue: ipk_CR2 ◦ CaseAdminSubject: CR2 node ID ◦ AdminVendorId: CR2 vendor ID • CR2 connects over CASE and sends the commissioning complete command 1. Save the FabricIndex from the NOCResponse as fabric_index_CR2 . | Verify the commissioning is successful. |

| 3 | CR2 reads the CurrentFabricIndex attribute | Verify the returned value is fabric_index_CR2 |
| 4 | CR3 reads the CurrentFabricIndex attribute | Verify the returned value is fabric_index_CR3 |
| 5 | CR2 reads the Fabrics attribute using a fabric- filtered read | • Verify there is one entry returned. Verify FabricIndex matches fabric_index_CR2 . • Verify the RootPublicKey matches the public key for rcac_CR2. • Verify the VendorID matches the vendor ID for CR2. • Verify the FabricID matches the fabricID |

| 6 | CR3 reads the Fabrics attribute using a fabric- filtered read | • Verify there is one entry returned. Verify FabricIndex matches fabric_index_CR3 . • Verify the RootPublicKey matches the public key for rcac_CR3. • Verify the VendorID matches the vendor ID for CR3. • Verify the FabricID matches the fabricID for CR3 |
| 7 | CR1 sends the RemoveFabric command to the Node Operational Credentials cluster with the FabricIndex set to fabric_index_CR2. | Verify DUT responds w/ status SUCCESS |
| 8 | CR1 sends the RemoveFabric command to the Node Operational Credentials cluster with the FabricIndex set to fabric_index_CR3. | Verify DUT responds w/ status SUCCESS |

## Notes/Testing considerations

## TC-OPCREDS-3.4 UpdateNOC-Error Condition [DUT-Server]

## Purpose

This test verifies that the DUT properly handles the following error conditions on UpdateNOC command:

- (4) UpdateNOC command sent without failsafe armed → FAILSAFE\_REQUIRED
- (6) UpdateNOC command sent without CSRRequest → MissingCsr in StatusCode field in the CSRResponse
- (9) UpdateNOC command send with CSRRequest for IsForUpdateNOC set to false → CONSTRAINT\_ERROR
- (13) UpdateNOC certificate public key does not match CSRRequest → InvalidPublicKey in the StatusCode field in the CSRResponse
- (16) NOC does not chain back to the TrustedRoot for this fabric → InvalidNOC in StatusCode field in the CSRResponse
- (18) NOC has improper FabricID for this fabric → InvalidNOC in StatusCode field in the CSRResponse
- (20)ICAC has improper FabricID for this fabric → InvalidNOC in StatusCode field in the CSRResponse
- (25) AddTrustedRootCertificate in same failsafe causes CONSTRAINT\_ERROR
- (30) Send CSRRequest for IsForUpdateNOC set to true → INVALID\_COMMAND

## · OPCREDS.S

## Pre-Conditions

| # | Doc. Ref. | Condition |
| 1 | | TH and DUT are commissioned |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | server |
| 2 | TH | client |

## Device Topology

TH1 commissions DUT on its fabric

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## TC-OPCREDS-3.5 NOC Check for UpdateNOC [DUT-Server]

## Purpose

1. To verify that when TH sends UpdateNOC command the NOC values are updated correctly on the DUT.
2. To verify that the previous NOC value from TH is not stored on DUT.
3. To verify that failsafe expiry successfully reverts NOC changes.

## PICS

- OPCREDS.S

## Pre-Conditions

| # | Doc. Ref. | Condition |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | server |
| 2 | TH1 | client |

## Device Topology

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

Notes/Testing considerations

## TC-OPCREDS-3.6 Last Fabric removal validation [DUT-Server]

## Purpose

To verify that when TH sends RemoveFabric command for last Fabric, DUT SHALL delete all Matter related data on the node which was created since it was commissioned.

## PICS

- OPCREDS.S

## Pre-Conditions

| # | Doc. Ref. | Condition |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | server |

| # | Device Name | Device Description |
| 2 | TH1 | client |

## Device Topology

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-OPCREDS-3.7 Add Second Fabric over CASE [DUT-Server]

## Purpose

To verify that a DUT can be added to a second fabric using AddNOC command.

## PICS

## · OPCREDS.S

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

| # | Device Name | Device Description |
| 1 | TH1 | Test harness as Client 1, a commissioner device |
| 2 | TH2 | Test harness as Client 2, a commissioner device |
| 3 | DUT | DUT - Server, a commissionee device |

## Spec Reference

{REF\_CODE}.5.5 - Commissioning flow C.4.14.2 - Case session establishment C.6.4 - Node Operational Certificate (NOC) usage C.11.10.6.2 - Arm fail-safe C.11.18 - Operational credentials

## Device Topology

## Test Setup

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | Commission DUT to TH1 if not already done | |
| 2 | TH1 sends ArmFailSafe command to the DUT with the ExpiryLengthSeconds field set to 60 seconds | Verify that the DUT sends ArmFailSafeResponse command to TH1 with field ErrorCode as OK (0) |
| 3 | TH1 Sends CSRRequest command with a random 32-byte nonce | Verify that the DUT responds with the CSRResponse command |
| 4 | TH2 generates the NOC, ICAC, and IPK for its fabric using the CSR elements from Step 3 . * Save ICAC as Intermediate_Certificate_TH2 * Save NOC as Node_Operational_Certificate_TH2 * Save IPK as IPK_TH2 * Extract the RCAC public key and save as Root_Public_Key_TH2 | |
| 5 | TH1 sends TH2's root certificate in th AddTrustedRootCertificate chain to DUT with RootCACertificate | |

| # | Test Step | Expected Outcome |
| 6 | TH1 sends the AddNOC command to DUT with the following fields: * NOCValue as [TH2_NOC] * ICACValue as [TH2_ICAC] * IpkValue as [TH2_IPK] * CaseAdminSubject as the NodeID of TH2 * AdminVendorId as the Vendor ID of TH2 | Verify that DUT responds with NOCResponse with status code OK |
| 7 | TH2 starts discovery of DUT using Operational Discovery | |
| 8 | TH2 opens a CASE session with DUT over operational network | DUT is able to open the CASE session with TH2 |
| 9 | TH2 sends CommissioningComplete command | DUT respond with SUCCESS at CommissioningComplete command sent by TH2 |
| 11a | TH1 does a fabric-filtered read of the Fabrics attribute from the Node Operational Credentials cluster | Verify that there is one entry in the list that matches TH1_fabric_index . |
| 11b | TH2 does a fabric-filtered read of the Fabrics attribute from the Node Operational Credentials cluster | Verify that there is one entry in the list that matches [TH2_FABRICINDEX]. |

## Notes/Testing considerations

## TC-OPCREDS-3.8 VID Verification Attribute, Commands Error Conditions [DUT as Server]

## Purpose

This test case verifies that the DUT properly implements the VID Verification Procedure payload generation

## PICS

- OPCREDS.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH1 | Test harness as Client 1, a commissioner device |
| 2 | TH2 | Test harness as Client 2, a commissioner device |
| 3 | DUT | DUT - Server, a commissionee device |

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Spec Reference

- C.11.18 - Operational Credentials
- C.6.4 - Node Operational Certificate (NOC) usage
- C.11.18.5.2 - Fabrics Attribute
- C.11.18.6.14 - SetVIDVerificationStatement Command
- C.11.18.6.15 - SignVIDVerificationRequest Command

## Device Topology

TH1 commissions DUT on its fabric

## Test Setup

## Test Procedure

| # | Test Step | Expected Outcome |
| 0 | • Commission DUT in TH1's fabric using FabricId= 1 and VID= 0xFFF1 . • Ensure that the NOC chain DOES include an ICAC. • Save the FabricIndex for TH1 as TH1_fabric_index . • Save the NodeID used for DUT commissioning as TH1_dut_node_id . • Save the RCAC used for DUT commissioning as TH1_rcac . • Save the subject key of TH1's RCAC used for DUT commissioning as TH1_root_public_key . | Commissioning succeeds. |

| # | Test Step | Expected Outcome |

| # | Test Step | Expected Outcome |
| 3 | TH1 reads the Fabrics attribute from the DUT using a non-fabric-filtered read. | • Verify that there exists entries both for TH1's and TH2's fabrics (one for TH1_fabric_index , one for [TH2_FABRICINDEX]). • Verify that the RootPublicKey field of |

| # | Test Step | |
| 4 | • TH1 invokes a SignVidVerificationRequest against the FabricIndex for TH2 ([TH2_FABRICINDEX]) using ClientChallenge octet string of a1:a2:a3:a4:a5:a6:a7:a8:a9:aa:ab:ac:ad :ae:af:b0:b1 :b2:b3:b4:b5:b6:b7:b8:b9:ba:bb:bc:bd:b e:bf:c0 . | Expected Outcome • Verify that a SignVidVerificationResponse is received after successful invocation of the command. • Verify that the FabricIndex field of the SignVidVerificationResponse is set to [TH2_FABRICINDEX]. • Locally generate the expected Vendor Fabric Binding Message using [TH2_root_public_key], Vendor ID 0xFFF2 and Fabric ID value of 2222 : vendor_fabric_binding_message := fabric_binding_version (0x01) &#124;&#124; root_public_key &#124;&#124; fabric_id &#124;&#124; vendor_id . • Locally generate the vendor_id_verification_tbs := fabric_binding_version &#124;&#124; client_challenge &#124;&#124; attestation_challenge &#124;&#124; fabric_index &#124;&#124; vendor_fabric_binding_message &#124;&#124; <vid_verification_statement> using the prior vendor_fabric_binding_message , prior client_challenge , secure session's attestation_challenge , |

| # | Test Step | Expected Outcome |

| # | Test Step | Expected Outcome |
| 13 | • TH2 invokes SetVIDVerificationStatement against the FabricIndex for TH2 ([TH2_FABRICINDEX]) outside fail-safe with the following fields: ◦ Maximum-sized VVSC equal 0xaa repeated 400 times. ◦ VIDVerificationStatement equal to 0x01 repeated 85 times. ◦ A VID equal to 0x6a01 . | • Verify the FabricIndex is set to [TH2_FABRICINDEX]. • Verify VVSC is set to 0xaa * 400. • Verify VIDVerificationStatement is set to 0x01 * 85. • Verify VID is set to 0x6a01 . • Verify subscription received the updated values. |
| 14 | • TH1 invokes SetVIDVerificationStatement against the FabricIndex for TH1 ( TH1_fabric_index ) outside fail-safe with the following fields: ◦ Maximum-sized VVSC equal 0xaa | • Verify the command fails with a status code of INVALID_COMMAND because the ICAC field is present in the NOCs attribute entry |

| # | Test Step | Expected Outcome |
| 19 | • Create a new fabric under TH2's root with the following fields: ◦ Fabric ID equal to 0x3333 . Save the FabricIndex for TH3 as TH3_fabric_index ◦ Node ID equal to 0x33333333 . ◦ Vendor ID equal to 0xFFF2 . • Invoke a ArmFailSafe timer for 600s, a CSRRequest, a AddTrustedRootCertificate and an AddNOC. • Do not disarm failsafe. | |

| # | Test Step | Expected Outcome |
| 23 | • TH2 invokes SetVIDVerificationStatement against the FabricIndex for TH2 ([TH2_FABRICINDEX]) outside fail-safe with the following fields: ◦ Maximum-sized VVSC equal 0x5a repeated 400 times. ◦ VIDVerificationStatement equal to 0x01 repeated 85 times. ◦ VID equal to 0x6a01 . | • Verify the command succeeded. |

#

## Test Step

- TH1 sends SignVIDVerificationRequest for TH2's fabric ([TH2\_FABRICINDEX]) with the following field:
- VIDVerificationStatement equal to 0x01 repeated 85 times.

## Expected Outcome

- Verify that a SignVidVerificationResponse is received after successful invocation of the command.
- Verify that the FabricIndex field of the SignVidVerificationResponse is set to [TH2\_FABRICINDEX].
- Locally generate the expected Vendor Fabric Binding Message using [TH2\_root\_public\_key], Vendor ID 0xFFF2 and Fabric ID value of 2222 : vendor\_fabric\_binding\_message := fabric\_binding\_version (0x01) || root\_public\_key || fabric\_id || vendor\_id .
- Locally generate the vendor\_id\_verification\_tbs := fabric\_binding\_version || client\_challenge || attestation\_challenge || fabric\_index || vendor\_fabric\_binding\_message || &lt;vid\_verification\_statement&gt; using the prior vendor\_fabric\_binding\_message , prior client\_challenge , secure session's attestation\_challenge ,

[TH2\_fabric\_index],

vid\_verification\_statement

"0x01"

equal

*

and using

SignVidVerificationResponse's

FabricBindingVersion

field value.

- Verify that the Signature field of SignVidVerificationResponse validates against a message of vendor\_id\_verification\_tbs with the [TH2\_NOC\_PUBLIC\_KEY].

a

to

the

| # | Test Step | Expected Outcome |
| 25 | • Update fabric under TH2's root with the following fields: ◦ Fabric ID equal to 0x2222 . ◦ Node ID equal to 0x22222222 . ◦ Vendor ID equal to 0xFFF2 . • Invoke a ArmFailSafe timer for 600s, a CSRRequest and an UpdateNOC. • Do not disarm failsafe. • Do not execute commissioning complete. | |
| 28 | • Update fabric under TH2's root with the following fields: ◦ Fabric ID equal to 0x2222 . ◦ Node ID equal to 0x77777777 . ◦ Vendor ID equal to 0xFFF2 . • Invoke a ArmFailSafe timer for 600s, a CSRRequest and an UpdateNOC. • Do not disarm failsafe. • Do not execute commissioning complete. | |

| # | Test Step | Expected Outcome |
| 29 | • TH2 invokes SetVIDVerificationStatement under TH2's fabric, inside fail-safe, with the following fields: ◦ VVSC equal to 0xcd repeated 400 times. ◦ VIDVerificationStatement equal to ( 0x01 + ( 0x03 repeated 84 times)). ◦ VID equal to 0xFFF4 . ◦ Fabric ID equal to 0x2222 . | • Verify VVSC is set to 0xcd * 400. • Verify VIDVerificationStatement is set to ( 0x01 + ( 0x03 * 84)). • Verify VID is 0xFFF4 . |

## Notes/Testing considerations

## 6.3.2. DUT as Client

## TC-OPCREDS-3.3 Attribute-NOCs, Commands [DUT-Client]

## Purpose

This test case verifies that the

1. DUT is able to read the attributes of Node Operational Credential cluster
2. DUT is able to send the commands of the Operational Credential cluster from the client side.

## PICS

- OPCREDS.C

## Pre-Conditions

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | client |
| 2 | TH | server |

## Device Topology

## Test Setup

## A new fabric is created by DUT to which the TH will be commissioned

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 5b | | | Extract the CSRResponse values for future use from TH 1. NOCSRElements - which contains the Node Operational PublicKey from CSR 2. AttestationSignature | |

| 7b | | | TH saves the following values as: • NOCValue as nocvalue1 • ICACValue as icacvalue1 • IpkValue as ipkvalue1 • CaseAdminSubject as caseadmin1 • AdminVendorId as adminvendorid1 | |
| 8 | | | Extract the following FabricDescriptorStruct values from TH 1. RootPublicKey 2. VendorID 3. FabricID 4. NodeID | |
| 9 | | | | • Verify that the size of RootPublicKey is within 65 octstr • Verify that the NodeID is the same as the chip-node-id in the NOC sent with AddNOC Command • Verify that the VendorID is the same as the AdminVendorID sent with AddNOC Command • Verify that the FabricID is the same as the matter-fabric-id field from the operational certificate • Verify that the size of Label has a maximum value of 32 bytes. |
| 10 | | | | • Verify that the public Key extracted NOCValue of the AddNOC matches the Node Operational Public Key extracted from CSRResponse |

## Notes/Testing considerations

Test Step #10 cannot be executed with V1.0 SDK.

## Chapter 7. Network Commissioning Cluster Test Plan

## 7.1. PICS Definition

This section covers the NetworkCommissioning Cluster related PICS items that are referenced in the following test cases.

## 7.1.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CNET.S | Does the device implement the NetworkCommissionin g Cluster as a server? | O | |
| CNET.C | Does the device implement the NetworkCommissionin g Cluster as a client? | O | |

## 7.1.2. Server

## Features

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CNET.S.F00(WI) | Does the device implement the "Wi-Fi related features" ? | CNET.S & MCORE.COM.WIFI | |
| CNET.S.F01(TH) | Does the device implement the "Thread related features" | CNET.S & MCORE.COM.THR | |
| CNET.S.F02(ET) | Does the device implement the "Ethernet related features" ? | CNET.S & MCORE.COM.ETH | |

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |

| CNET.S.A0000(MaxNet works) | Does the DUT(Server) support MaxNetworks attribute? | CNET.S :M | |
| CNET.S.A0001(Network | Does the DUT(Server) support Networks attribute? | CNET.S :M | s) |
| CNET.S.A0002(ScanMax TimeSeconds) | Does the DUT(Server) support ScanMaxTimeSeconds attribute? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |
| CNET.S.A0003(Connect MaxTimeSeconds) | Does the DUT(Server) support ConnectMaxTimeSecon ds attribute? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |
| CNET.S.A0004(Interface | Does the DUT(Server) support InterfaceEnabled attribute? | CNET.S :M | Enabled) |
| CNET.S.A0005(LastNet workingStatus) | Does the DUT(Server) support LastNetworkingStatus attribute? | CNET.S :M | |
| CNET.S.A0006(LastNet | Does the DUT(Server) support LastNetworkID attribute? | CNET.S :M | workID) |
| CNET.S.A0007(LastCon nectErrorValue) | Does the DUT(Server) support LastConnectErrorValue attribute? | CNET.S :M | |
| CNET.S.A0008(Supporte dWiFiBands) | Does the DUT(Server) support SupportedWiFiBands attribute? | CNET.S.F00(WI) | |
| CNET.S.A0009(Supporte dThreadFeatures) | Does the DUT(Server) support SupportedThreadFeatu res attribute? | CNET.S.F01(TH) | |
| CNET.S.A000a(ThreadV | Does the DUT(Server) support ThreadVersion attribute? | CNET.S.F01(TH) | ersion) |

## Commands received

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CNET.S.C00.Rsp(ScanNe tworks) | Does the Device(Server) implement receiving the ScanNetworks command? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |
| CNET.S.C02.Rsp(AddOr UpdateWiFiNetwork) | Does the Device(Server) implement receiving the AddOrUpdateWiFiNetw ork command? | CNET.S.F00(WI) | |
| CNET.S.C03.Rsp(AddOr UpdateThreadNetwork) | Does the Device(Server) implement receiving the AddOrUpdateThreadNe twork command? | CNET.S.F01(TH) | |
| CNET.S.C04.Rsp(Remov eNetwork) | Does the Device(Server) implement receiving the RemoveNetwork command? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |
| CNET.S.C06.Rsp(Connec tNetwork) | Does the Device(Server) implement receiving the ConnectNetwork command? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |
| CNET.S.C08.Rsp(Reorde rNetwork) | Does the Device(Server) implement receiving the ReorderNetwork command? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CNET.S.C01.Tx(ScanNet worksResponse) | Does the Device(Server) invoking/generating the ScanNetworksResponse command? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |
| CNET.S.C05.Tx(Network ConfigResponse) | Does the Device(Server) invoking/generating the NetworkConfigRespons e command? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) | |

| CNET.S.C07.Tx(Connect NetworkResponse) | Does the Device(Server) invoking/generating the ConnectNetworkRespo nse command? | CNET.S.F00(WI)&#124;CNET. S.F01(TH) |

## 7.1.3. Client

## Features

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CNET.C.F00(WI) | Does the device implement the "Wi-Fi related features" ? | O | |
| CNET.C.F01(TH) | Does the device implement the "Thread related features" | O | |
| CNET.C.F02(ET) | Does the device implement the "Ethernet related features" ? | O | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CNET.C.C00.Tx(ScanNet works) | Does the Device(Client) invoking/generating the ScanNetworks command? | CNET.C : O | |
| CNET.C.C02.Tx(AddOrU pdateWiFiNetwork) | Does the Device(Client) invoking/generating the AddOrUpdateWiFiNetw ork command? | CNET.C : O | |
| CNET.C.C03.Tx(AddOrU pdateThreadNetwork) | Does the Device(Client) invoking/generating the AddOrUpdateThreadNe twork command? | CNET.C : O | |
| CNET.C.C04.Tx(Remove Network) | Does the Device(Client) invoking/generating the RemoveNetwork command? | CNET.C : O | |

| CNET.C.C06.Tx(Connect Network) | Does the Device(Client) invoking/generating the ConnectNetwork command? | CNET.C : O |
| CNET.C.C08.Tx(Reorder Network) | Does the Device(Client) invoking/generating the ReorderNetwork command? | CNET.C : O |

## 7.2. PIXIT Definition

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PIXIT.CNET.WIFI_1ST_ ACCESSPOINT_SSID | Access point SSID(dual band 2.4GHz and 5GHz) to use for tests | CNET.S.F00(WI) | |
| PIXIT.CNET.WIFI_1ST_ ACCESSPOINT_CREDEN TIALS | Credentials for SSID PIXIT.CNET.WIFI_1ST_ ACCESSPOINT_SSID | CNET.S.F00(WI) | |
| PIXIT.CNET.WIFI_2ND_ ACCESSPOINT_SSID | SSID of a second valid access point | CNET.S.F00(WI) | |
| PIXIT.CNET.WIFI_2ND_ ACCESSPOINT_CREDEN TIALS | Credentials for SSID PIXIT.CNET.WIFI_2ND_ ACCESSPOINT_SSID | CNET.S.F00(WI) | |
| PIXIT.CNET.THREAD_1S T_OPERATIONALDATA SET | Valid thread OperationalDataset | CNET.S.F01(TH) | |
| PIXIT.CNET.THREAD_2 ND_OPERATIONALDAT ASET | Second valid thread OperationalDataset | CNET.S.F01(TH) | |
| PIXIT.CNET.ENDPOINT_ WIFI | DUT's supporting Endpoint for the Network Commissioning | CNET.S.F00(WI) | |
| PIXIT.CNET.ENDPOINT_ THREAD | DUT's supporting Endpoint for the Network Commissioning | CNET.S.F01(TH) | |
| PIXIT.CNET.ENDPOINT_ ETHERNET | DUT's supporting Endpoint for the Network Commissioning | CNET.S.F02(ET) | |

## 7.3. Test Case List

| TC UUID | Test Case Name |
| TC-CNET-1.4 | Verification for Network Commissioning cluster dependencies [DUT-Server] |
| TC-CNET-4.1 | [Wi-Fi] Verification for attributes check [DUT-Server] |
| TC-CNET-4.2 | [Thread] Verification for attributes check [DUT-Server] |
| TC-CNET-4.3 | [Ethernet] Verification for attributes check [DUT-Server] |
| TC-CNET-4.4 | [Wi-Fi] Verification for ScanNetworks command [DUT-Server] |
| TC-CNET-4.5 | [Wi-Fi] FAILSAFE_REQUIRED message Validation [DUT-Server] |
| TC-CNET-4.6 | [Thread] FAILSAFE_REQUIRED message Validation [DUT-Server] |
| TC-CNET-4.9 | [Wi-Fi] Verification for RemoveNetwork Command [DUT-Server] |
| TC-CNET-4.10 | [Thread] Verification for RemoveNetwork Command [DUT-Server] |
| TC-CNET-4.11 | [Wi-Fi] Verification for ConnectNetwork Command [DUT-Server] |
| TC-CNET-4.12 | [Thread] Verification for ConnectNetwork Command [DUT-Server] |
| TC-CNET-4.13 | [Wi-Fi] Verification for ReorderNetwork command [DUT-Server] - PROVISIONAL |
| TC-CNET-4.14 | [Thread] Verification for ReorderNetwork command [DUT-Server] - PROVISIONAL |
| TC-CNET-4.15 | [Wi-Fi] NetworkIDNotFound returned in LastNetworkingStatus field validation [DUT-Server] |
| TC-CNET-4.16 | [Thread] NetworkIDNotFound returned in LastNetworkingStatus field validation [DUT-Server] |
| TC-CNET-4.20 | [Wi-Fi] Verification for commands check [DUT-Client] |
| TC-CNET-4.21 | [Thread] Verification for commands check [DUT-Client] |
| TC-CNET-4.22 | [Thread] Verification for ScanNetworks command [DUT-Server] |

## 7.4. Test Cases

## 7.4.1. Server Test Cases

## TC-CNET-1.4 Verification for Network Commissioning cluster dependencies [DUT-Server]

## Category

Functional conformance.

## Purpose

This test case verifies that Network Commissioning clusters are either on the Root Node or the Secondary Network Interface endpoint. Additionally, it ensures that concurrent commissioning mode is supported if multiple Network Commissioning clusters are present.

## PICS

- CNET.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 5 | | | TH reads from the DUT the Descriptor Cluster DeviceTypeList attribute on each endpoint from the NetworkCommissioningResponse (except for Endpoint 0) | Verify DUT responds w/ status SUCCESS(0x00) and the Secondary Network Interface device type id (0x0019) is listed in the DeviceTypeList |
| 6 | | | TH reads from the DUT the SupportsConcurrentConnection attribute from the General Commissioning Cluster | Verify DUT responds w/ status SUCCESS(0x00) and a true value is returned |

## 7.4.2. DUT as Server

## TC-CNET-4.1 [Wi-Fi] Verification for attributes check [DUT-Server]

## Purpose

- Verifying the DUT is connected with the Wi-Fi interface
- Verifying the following attributes check:
1. DUT's MaxNetworks attribute value needs to be within a range of 1 to 255
2. DUT's Networks attribute list will follow the NetworkInfo structure for each entry
3. DUT's ScanMaxTimeSeconds attribute value must be within 255 seconds
4. DUT's ConnectMaxTimeSeconds attribute value must be within 255 seconds
5. DUT's InterfaceEnabled attribute value must be True
6. DUT's LastNetworkingStatus attribute value will be within any one of the following values Success, NetworkNotFound, OutOfRange, RegulatoryError, UnknownError, null
7. DUT's LastNetworkID attribute value will be of type octstr with a length range of 1 to 32 and even null value
8. DUT's LastConnectErrorValue attribute value must be null
9. DUT's SupportedWiFiBands attribute value has one or more entries.

## PICS

## · CNET.S.F00(WI)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F00(WI) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ WIFI with FeatureMap attribute of 1 | |
| 4 | | TH can communicate with the DUT | |

| 5 | Commission DUT if not already done |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | TestStep | Expected Outcome |
| 1 | TH reads the MaxNetworks attribute from the DUT | Verify that MaxNetworks attribute value is within a range of 1 to 255 |
| 3 | TH reads ScanMaxTimeSeconds attribute from the DUT | Verify that ScanMaxTimeSeconds attribute value is within the range of 1 to 255 seconds |
| 4 | TH reads ConnectMaxTimeSeconds attribute from the DUT | Verify that ConnectMaxTimeSeconds attribute value is within the range of 1 to 255 seconds |
| 5 | TH reads the Networks attribute list from the DUT on all available endpoints | Verify that each element in the Networks attribute list has the following fields: 'NetworkID', 'connected'. NetworkID field is of type octstr with a length range 1 to 32 The connected field is of type bool Verify that only one entry has connected status as TRUE Verify that the number of entries in the Networks attribute is less than or equal to 'MaxNetworksValue' |
| 6 | Skip remaining steps if the connected network is not on the cluster currently being verified.TH reads InterfaceEnabled attribute from the DUT | Verify that InterfaceEnabled attribute value is true |
| 7 | TH reads LastNetworkingStatus attribute from the DUT | LastNetworkingStatus attribute value will be within any one of the following values Success, NetworkNotFound, OutOfRange, RegulatoryError, UnknownError, null |
| 8 | TH reads the LastNetworkID attribute from the DUT. TH reads the Networks attribute from the DUT | Verify that LastNetworkID attribute matches the NetworkID value of one of the entries in the Networks attribute list |

## TC-CNET-4.2 [Thread] Verification for attributes check [DUT-Server]

## Purpose

- Verifying the DUT is connected with the Thread interface
- Verifying the following attributes check:
1. DUT's MaxNetworks attribute value needs to be within a range of 1 to 255
2. DUT's Networks attribute list will follow the NetworkInfo structure for each entry
3. DUT's ScanMaxTimeSeconds attribute value must be within 255 seconds
4. DUT's ConnectMaxTimeSeconds attribute value must be within 255 seconds
5. DUT's InterfaceEnabled attribute value must be True
6. DUT's LastNetworkingStatus attribute value is Success
7. DUT's LastNetworkID attribute value will be of type octstr with a length range of 1 to 32 and even null value
8. DUT's LastConnectErrorValue attribute value must be null
9. DUT's SupportedThreadFeatures attribute value must not be an empty bitmap.

## PICS

## · CNET.S.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F01(TH) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ THREAD with FeatureMap attribute of 2 | |

| 4 | TH can communicate with the DUT on PIXIT.CNET.THREAD_1S T_OPERATIONALDATA SET |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | TestStep | Expected Outcome |

| | | Verify that Bit 4 (IsSynchronizedSleepyEndDeviceCapable) is only set if bit 2 |
| | | Verify that Bit 1 (IsRouterCapable) is only set if bit 3 (IsFullThreadDevice) is also set. Verify that at least one of the following bits is set: |
| | | Bit 4 (IsSynchronizedSleepyEndDeviceCapable), Bit 2 (IsSleepyEndDeviceCapable), |

## TC-CNET-4.3 [Ethernet] Verification for attributes check [DUT-Server]

## Purpose

- Verifying the DUT is connected with Ethernet interface
- Verifying the following attributes check:
1. DUT's MaxNetworks attribute value needs to be within a range of 1 to 255
2. DUT's Networks attribute list will follow the NetworkInfo structure for each entry
3. DUT's InterfaceEnabled attribute value must be True
4. DUT's LastNetworkingStatus attribute value is Success
5. DUT's LastNetworkID attribute value will be of type octstr with a length range of 1 to 32 and even null value
6. DUT's LastConnectErrorValue attribute value must be null

## PICS

- CNET.S.F02(ET)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F02(ET) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ ETHERNET with FeatureMap attribute of 4 | |
| 4 | | TH can communicate with the DUT | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | TestStep | Expected Outcome |
| 1 | Commission DUT if not already done | Device commissioned |
| 2 | TH reads the MaxNetworks attribute from the DUT | Verify that MaxNetworks attribute value is within a range of 1 to 255 |
| 3 | TH reads the Networks attribute list from the DUT on all endpoints (all network commissioning clusters of the DUT) | Verify that each element in the Networks attribute list has the following fields: 'NetworkID', 'connected'. NetworkID field is of type octstr with a length range 1 to 32 The connected field is of type bool Verify that there is a single connected network across ALL network commissioning clusters Verify that the number of entries in the Networks attribute is less than or equal to 'MaxNetworksValue' |

| 4 | Skip remaining steps if the connected network is not on the cluster currently being verified. TH reads InterfaceEnabled attribute from the DUT | Verify that InterfaceEnabled attribute value is true |
| 6 | TH reads the LastNetworkID attribute from the DUT | Verify that LastNetworkID attribute matches the NetworkID value of one of the entries in the Networks attribute list |
| 7 | TH reads the LastConnectErrorValue attribute from the DUT | Verify that LastConnectErrorValue attribute value is null |

## TC-CNET-4.4 [Wi-Fi] Verification for ScanNetworks command [DUT-Server]

## Purpose

1. Verification of ScanNetworks command for listing all available Wi-Fi networks within the range using a null value
2. Verification of ScanNetworks command for user-input SSID Wi-Fi network

## PICS

- CNET.S

## Pre-Conditions

| Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Platform Certification

In the context of a platform certification, if the platform supports devices with various supported\_wifi\_bands values, this test case must be ran for each supported\_wifi\_bands value.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | C.11.9.4 | | TH reads from the DUT the Network Commissioning Cluster FeatureMap . If the FeatureMap does not include the WI flag (bit 0), skip the remaining steps in this test case | |
| 2 | C.11.9.6. 9 | | TH reads from the DUT the SupportedWifiBands attribute and saves as supported_wifi_bands | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 4 | C.11.9.7. 1 | | TH sends ScanNetworks command to the DUT with the SSID field set to 'null' and Breadcrumb field set to 1 | Verify that DUT sends ScanNetworksResponse command to the TH with the following fields: • NetworkingStatus is Success • DebugText is of type string with max length 512 or absent • WiFiScanResults contains at least one element • At least one of the WifiScanResults entries has an SSID of known_ssid • Each element in the WiFiScanResults list will have the following fields: 1. Security contains only flags supported in the WiFiSecurityBitmap Type 2. SSID is of type octstr with a length range 0 to 32. 3. BSSID is of type octstr with a length of 6. 4. Channel is of type uint16 with a range 0 to 65,535 5. Wi-Fi Band, if present, is one of the values present in the supported_wifi_bands and in the range of values in the WiFiBandEnum. 6. RSSI, if present, is of type int8 |
| 5 | C.11.10.5 .1 | | TH reads from the DUT the Breadcrumb attribute from the General Commissioning Cluster | Verify that the Breadcrumb attribute is set to 1 |

| # | Ref | PICS | Test Step | Expected Outcome |
| 6 | C.11.9.7. 1 | | TH sends ScanNetworks Command to the DUT with SSID field set to known_ssid and Breadcrumb field set to 2 | Verify that DUT sends ScanNetworksResponse command to the TH with the following fields: • NetworkingStatus is Success • DebugText is of type string with max length 512 or absent • WiFiScanResults contains at least one element • Each element in the WiFiScanResults list will have the following fields: 1. Security contains only flags supported in the WiFiSecurityBitmap Type 2. SSID is known_ssid 3. BSSID is of type octstr with a length of 6. 4. Channel is of type uint16 with a range 0 to 65,535 5. Wi-Fi Band, if present, is one of the values present in the supported_wifi_bands and in the range of values in the WiFiBandEnum. |
| 7 | C.11.10.5 .1 | | TH reads Breadcrumb attribute from the General Commissioning Cluster | Verify that the Breadcrumb attribute is set to 2 |

## Notes/Testing Considerations

Verification steps for the scan networks command should include verification that the BSSIDs returned map only to the supported bands and match to a known set configuration parameters for a given BSSID, supplied as a PIXIT. Please see https://github.com/CHIP-Specifications/chip-test-plans/

## TC-CNET-4.5 [Wi-Fi] FAILSAFE\_REQUIRED message Validation [DUT-Server]

## Purpose

- Verify that DUT sends status code FAILSAFE\_REQUIRED message for the following commands that are initiated before sending ArmFailSafe command by the TH:
1. AddOrUpdateWiFiNetwork Command
2. RemoveNetwork Command and
3. ConnectNetwork command

## PICS

## · CNET.S.F00(WI)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F00(WI) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ WIFI with FeatureMap attribute of 1 | |
| 4 | | TH can communicate with the DUT | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## TC-CNET-4.6 [Thread] FAILSAFE\_REQUIRED message Validation [DUT-Server]

## Purpose

- Verify that DUT sends status code FAILSAFE\_REQUIRED message for the following commands that are initiated before sending ArmFailSafe command by the TH:
1. AddOrUpdateThreadNetwork Command
2. RemoveNetwork Command and
3. ConnectNetwork command

## PICS

- CNET.S.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F01(TH) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ THREAD with FeatureMap attribute of 2 | |
| 4 | | TH can communicate with the DUT on PIXIT.CNET.THREAD_1S T_OPERATIONALDATA SET | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## TC-CNET-4.9 [Wi-Fi] Verification for RemoveNetwork Command [DUT-Server]

## Purpose

1. Verification for RemoveNetwork Command by removing a Wi-Fi network from the Networks list
2. Verification that network changes are reverted when fail safe times out
3. Verification that network changes are retained when CommissioningComplete command is called

## PICS

## · CNET.S.F00(WI)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F00(WI) | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | TestStep | Expected Outcome |
| Precondi tion | Commission DUT if not already done | DUT is commissioned on wifi network provided in --wifi-ssid parameter; TH can communicate with the DUT |

| 4 | TH reads Networks attribute from the DUT on the current endpoint and saves the number of entries as 'NumNetworks' | Verify that the Networks attribute list has an entry with the following values: 1. NetworkID field value as provided in the --wifi-ssid parameter; 2. Connected field value is of type bool and has the value true. |
| 5 | TH finds the index of the Networks list entry with NetworkID field value as provided in the --wifi-ssid parameter and saves it as Userwifi_netidx. | |
| 6 | TH sends RemoveNetwork Command to the DUT with NetworkID field set to the as provided in the --wifi-ssid parameter and Breadcrumb field set to 1. | Verify that DUT sends NetworkConfigResponse to command with the following fields: 1. NetworkingStatus is success; 2. NetworkIndex is 'Userwifi_netidx' |
| 11 | TH sends ConnectNetwork command to the DUT with NetworkID field set to the value provided in the --wifi-ssid parameter and Breadcrumb field set to 2. | Verify that the DUT sends a ConnectNetworkResponse to the command with the NetworkingStatus field set to NetworkIdNotFound |
| 13 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that DUT sends ArmFailSafeResponse command to the TH |

| 14 | TH reads Networks attribute from the DUT on the current endpoint | Verify that the Networks attribute list contains 'NumNetworks' entries and has an entry with the following fields: NetworkID is the hex representation of the ASCII values for the value provided in the --wifi -ssid parameter;Connected is of type bool and has the value true |
| 15 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 16 | TH sends RemoveNetwork Command to the DUT with NetworkID field set to the value provided in the --wifi-ssid parameter and Breadcrumb field set to 1 | Verify that DUT sends NetworkConfigResponse to command with the following fields:NetworkingStatus is success |
| 17 | TH sends the CommissioningComplete command to the DUT | Verify that DUT sends CommissioningCompleteResponse with the ErrorCode field set to OK (0) |
| 18 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 to ensure the CommissioningComplete call properly persisted the failsafe context. This call should have no effect if Commissioning Complete call is handled correctly | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 19 | TH reads Networks attribute from the DUT on the current endpoint | Verify that the Networks attribute list has 'NumNetworks' - 1 entries and does NOT contain an entry with the NetworkID value provided in the --wifi-ssid parameter |
| 21 | TH sends the AddOrUpdateWiFiNetwork command to the DUT | Verify that DUT sends the NetworkConfigResponse to each command with the following fields: NetworkingStatus is success which is 0 |
| 22 | TH sends the CommissioningComplete command to the DUT | Verify that DUT sends CommissioningCompleteResponse with the ErrorCode field set to OK (0) |

## TC-CNET-4.10 [Thread] Verification for RemoveNetwork Command [DUT-Server]

## Purpose

1. Verification for RemoveNetwork Command by removing a thread network from the Networks list
2. Verification that network changes are reverted when fail safe times out
3. Verification that network changes are retained when CommissioningComplete command is

## PICS

## · CNET.S.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F01(TH) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ THREAD with FeatureMap attribute of 2 | |
| 4 | | TH can communicate with the DUT on the commissioned Thread network | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | TestStep | Expected Outcome |
| 1 | Commission DUT if not already done | DUT is commissioned, TH can communicate with the DUT on thread dataset provided in --thread-dataset-hex parameter. |

| 4 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 and Breadcrumb set to 0 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 5 | TH reads Networks attribute from the DUT and save the number of entries as 'NumNetworks' | Verify that the Networks attribute list has an entry with the following values: 1. NetworkID field value set as the Extended PAN ID from the operational dataset 2. Connected field value is of type boolean and has the value True |
| 6 | TH sends RemoveNetwork Command to the DUT with NetworkID field set to the Extended PAN ID from the operational dataset and Breadcrumb field set to 1 | Verify that DUT sends NetworkConfigResponse to command with the following fields: 1. NetworkingStatus is success 2. NetworkIndex is 'Userth_netidx' |
| 7 | TH reads Networks attribute from the DUT | Verify that the Networks attribute list has 'NumNetworks' - 1 entries |
| 10 | TH reads Breadcrumb attribute from the General Commissioning cluster | Verify that the breadcrumb value is set to 1 |
| 11 | TH sends ConnectNetwork command to the DUT with NetworkID field set to the Extended PAN ID from the operational dataset and Breadcrumb set to 2 | Verify that the DUT sends a ConnectNetworkResponse to the command with the NetworkingStatus field set to NetworkIdNotFound |
| 12 | TH reads Breadcrumb attribute from the General Commissioning cluster | Verify that the breadcrumb value is set to 1 |
| 13 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 and Breadcrumb set to 0 | Verify that the DUT sends ArmFailSafeResponse command to the TH |
| 14 | TH reads Networks attribute from the DUT | Verify that the Networks attribute list contains 'NumNetworks' entries and has an entry with the following values:1. NetworkID field value set as the Extended PAN ID from the operational dataset 2. Connected field value is of type boolean and has the value True |

| 15 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 and Breadcrumb set to 0 | Verify that the DUT sends ArmFailSafeResponse command to the TH |
| 16 | TH sends RemoveNetwork Command to the DUT with NetworkID set to the Extended PAN ID from the operational dataset and Breadcrumb set to 1 | Verify that the DUT sends NetworkConfigResponse to command with the following fields: 1. NetworkingStatus is success 2. NetworkIndex is 'Userth_netidx' |
| 17 | TH sends CommissioningComplete command to the DUT | Verify that the DUT sends CommissioningCompleteResponse to the command with the ErrorCode field set to OK (0) |
| 18 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 and Breadcrumb set to 0 | Verify that the DUT sends ArmFailSafeResponse command to the TH |
| 19 | TH reads Networks attribute from the DUT | Verify that the Networks attribute list contains 'NumNetworks' -1 entries and does not contain the Extended PAN ID from the operational dataset |

## TC-CNET-4.11 [Wi-Fi] Verification for ConnectNetwork Command [DUT-Server]

## Purpose

1. Verify that the Wi-Fi network is connected using the ConnectNetwork Command
2. Verify that changes are reverted successfully after a failsafe timeout
3. Verify that changes are persisted successfully after a CommissioningComplete command

## PICS

## · CNET.S.F00(WI)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F00(WI) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ WIFI with FeatureMap attribute of 1 | |

| 4 | | TH can connect to two valid Wi-Fi access points: PIXIT.CNET.WIFI_1ST_ ACCESSPOINT_SSID and PIXIT.CNET.WIFI_2ND_ ACCESSPOINT_SSID |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Platform Certification

If the platform supports devices with various supported\_wifi\_bands values, this test case must be ran for each supported\_wifi\_bands value.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |

| 4 | • 11.8. 8.8 • 11.8. 8.9 | • CNET.S.C0 4.Rsp(Re moveNet work) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends RemoveNetwork Command to the DUT with NetworkID field set to PIXIT.CNET.WIFI_1ST_ACCE SSPOINT_SSID and Breadcrumb field set to 1 | • Verify that DUT sends NetworkConfigResponse to command with the following fields: 1. NetworkingStatus is Success 2. NetworkIndex matches previously saved 'Userwifi_netidx' |
| 5 | • 11.8. 8.4 • 11.8. 8.6 • 11.8. 8.9 | • CNET.S.C0 2.Rsp(Add OrUpdate WiFiNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends AddOrUpdateWiFiNetwork command to the DUT with SSID field set to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_SSID, Credentials field set to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_CREDENTIALS and Breadcrumb field set to 1 | • Verify that DUT sends the NetworkConfigResponse command to the TH with the following response fields: 1. NetworkingStatus is success which is "0" 2. DebugText is of type string with max length 512 or empty |

| 8 | | | TH changes its WiFi connection to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_SSID | |
| 11 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0. This forcibly disarms the fail-safe and is expected to cause the changes of configuration to NetworkCommissioning cluster done so far to be reverted. | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 12 | | | TH changes its Wi-Fi connection to PIXIT.CNET.WIFI_1ST_ACCE SSPOINT_SSID | |
| 14 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |

| 15 | * 11.8.8.8 * 11.8.8.9 | • CNET.S.C0 4.Rsp(Re moveNet work) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends RemoveNetwork Command to the DUT with NetworkID field set to PIXIT.CNET.WIFI_1ST_ACCE SSPOINT_SSID and Breadcrumb field set to 1 | • Verify that DUT sends NetworkConfigResponse to command with the following response fields: 1. NetworkingStatus is success 2. NetworkIndex is 'Userwifi_netidx' |
| 16 | * 11.8.8.4 * 11.8.8.6 * 11.8.8.9 | • CNET.S.C0 2.Rsp(Add OrUpdate WiFiNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends AddOrUpdateWiFiNetwork command to the DUT with SSID field set to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_SSID, Credentials field set to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_CREDENTIALS and Breadcrumb field set to 1 | • Verify that DUT sends the NetworkConfigResponse command to the TH with the following response fields: 1. NetworkingStatus is success which is "0" 2. DebugText is of type string with max length 512 or empty |
| 17 | • 11.8. 8.10 • 11.8. 8.11 | • CNET.S.C0 6.Rsp(Con nectNetw ork) • CNET.S.C0 7.Tx(Conn ectNetwo rkRespon se) | TH sends ConnectNetwork command to the DUT with NetworkID field set to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_SSID and Breadcrumb field set to 3 | |
| 18 | | | TH changes its Wi-Fi connection to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_SSID | |

## Notes/Testing Considerations

Test Steps #11- #16 cannot be executed with V1.0 SDK

## TC-CNET-4.12 [Thread] Verification for ConnectNetwork Command [DUT-Server]

## Purpose

1. Verify that the time taken by DUT to make successful connectivity is within ConnectMaxTimeSeconds by thread network
2. Verify that the thread network is connected using the ConnectNetwork Command

## PICS

- CNET.S.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F01(TH) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint specified by the --endpoint argument with FeatureMap attribute of 2 | |

| 4 | TH has can communicate to two valid thread PANs: THREAD_1ST_OPERATIONAL DATASET and PIXIT.CNET.THREAD_2 ND_OPERATIONALDAT ASET |
| 5 | XPANID of THREAD_1ST_OPERATI ONALDATASET is saved as th_xpan_1 and the XPANID of PIXIT.CNET.THREAD_2 ND_OPERATIONALDAT ASET is saved as th_xpan_2 |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

## Spec Reference

## C.11.9.6.2 - CNET Networks

| # | TestStep | Expected Outcome |
| 1 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT responds with ArmFailSafeResponse to the TH |
| 2 | TH reads Networks attribute from the DUT and saves the number of entries as NumNetworks | • Verify that the Networks attribute list has an entry with the following fields: 1. NetworkID is th_xpan_1 2. Connected is of type bool and is TRUE |
| 3 | TH saves the index of the Networks list entry from step 2 as Userth_netidx | |

| # | TestStep | Expected Outcome |
| 4 | TH sends RemoveNetwork Command to the DUT with NetworkID field set to th_xpan_1 and Breadcrumb field set to 1 | • Verify that DUT sends NetworkConfigResponse to command with the following response fields: 1. NetworkingStatus is success 2. NetworkIndex is Userth_netidx |
| 5 | TH sends AddOrUpdateThreadNetwork command to the DUT with operational dataset field set to PIXIT.CNET.THREAD_2ND_OPERATIONALD ATASET and Breadcrumb field set to 1 | • Verify that DUT sends the NetworkConfigResponse command to the TH with the following fields: 1. NetworkingStatus is success which is '0' 2. DebugText is of type string with max length 512 or empty |
| 6 | TH reads Networks attribute from the DUT | • Verify that the Networks attribute list has an entry with the following fields: 1. NetworkID is th_xpan_2 2. Connected is of type bool and is FALSE |
| 8 | TH discovers and connects to DUT on the PIXIT.CNET.THREAD_2ND_OPERATIONALD ATASET operational network | Verify that the TH successfully connects to the DUT |
| 9 | TH reads Breadcrumb attribute from the General Commissioning cluster of the DUT | Verify that the breadcrumb value is set to 2 |
| 10 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 11 | TH ensures it can communicate with THREAD_1ST_OPERATIONALDATASET operational network (from --thread-dataset -hex) | |
| 12 | TH discovers and connects to DUT on the THREAD_1ST_OPERATIONALDATASET operational network (from --thread-dataset -hex) | Verify that the TH successfully connects to the DUT |
| 13 | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |

| # | TestStep | Expected Outcome |
| 14 | TH sends RemoveNetwork Command to the DUT with NetworkID field set to 'th_xpan_1' and Breadcrumb field set to 1 | • Verify that DUT sends NetworkConfigResponse to command with the following fields:. NetworkingStatus is success. NetworkIndex is Userth_netidx |
| 15 | TH sends AddOrUpdateThreadNetwork command to the DUT with the OperationalDataset field set to PIXIT.CNET.THREAD_2ND_OPERATIONALD ATASET and Breadcrumb field set to 1 | • Verify that DUT sends the NetworkConfigResponse command to the TH with the following fields: 1. NetworkingStatus is success which is '0' 2. DebugText is of type string with max length 512 or empty |
| 17 | TH discovers and connects to DUT on the PIXIT.CNET.THREAD_2ND_OPERATIONALD ATASET operational network | Verify that the TH successfully connects to the DUT |
| 18 | TH reads Breadcrumb attribute from the General Commissioning cluster of the DUT | Verify that the breadcrumb value is set to 3. Note: Wait for device to connect to the Thread network. A wait time of connect_max_time_seconds + fudge_factor_seconds is applied to allow Thread network connection and SRP record propagation. |
| 19 | TH sends the CommissioningComplete command to the DUT | Verify that DUT sends CommissioningCompleteResponse with the ErrorCode field set to OK (0) |
| 20 | TH reads Networks attribute from the DUT | • Verify that the Networks attribute list has an entry with the following values: 1. NetworkID field value as the extended PAN ID of PIXIT.CNET.THREAD_2ND_OPERATI ONALDATASET 2. Connected field value is of type bool and is TRUE |

| # | TestStep | Expected Outcome |
| 21 | TH switches back to THREAD_1ST_OPERATIONALDATASET operational network (from --thread-dataset -hex) | • Verify that the Networks attribute list has an entry with the following values: 1. NetworkID field value as the extended PAN ID of PIXIT.CNET.THREAD_1ST_OPERATI ONALDATASET 2. Connected field value is of type bool and is TRUE |

## TC-CNET-4.13 [Wi-Fi] Verification for ReorderNetwork command [DUT-Server] PROVISIONAL

## Purpose

Verify that the Networks list is re-ordered when using ReorderNetwork Command

## PICS

## · CNET.S.F00(WI)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| 1a | | | TH reads MaxNetworks attribute from DUT and is saved as 'MaxNetworksValue' for future use | • If MaxNetworksValue is < 2, skip the remaining steps. • Note: This test case is applicable for MaxNetworksValue >= 2 |
| 1b | * 11.9.7.1 * 11.9.7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 3 | | | TH calculates the number of remaining network slots as 'MaxNetworksValue' - 'NumNetworks' and saves as 'RemainingNetworkSlots' | |
| 4 | | | TH calculates the midpoint of the network list as floor(('MaxNetworksValue' + 1)/2) and saves as 'Midpoint' | |
| 5 | • 11.8. 8.4 • 11.8. 8.6 • 11.8. 8.9 | • CNET.S.C0 2.Rsp(Add OrUpdate WiFiNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends AddOrUpdateWiFiNetwork command to the DUT. This step should be repeated 'RemainingNetworkSlots' times using DIFFERENT SSID and credential values and the Breadcrumb field set to 1. Note that these credentials are NOT required to be connectable. | • Verify that DUT sends the NetworkConfigResponse to each command with the following fields: 1. NetworkingStatus is success which is "0" 2. DebugText is of type string with max length 512 or empty |

| 7 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is PIXIT.CNET.WIFI_1S T_ACCESSPOINT_SSI D 2. NetworkIndex is 'MaxNetworksValue' 3. Breadcrumb is 2 | • Verify that DUT sends NetworkConfigResponse to the TH with following fields: 1. NetworkingStatus is OutOfRange 2. DebugText is of type string with max length 512 or empty |
| 9 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is a NetworkID value NOT present in 'OriginalNetworkList' 2. NetworkIndex is 'Midpoint' 3. Breadcrumb is 2 | • Verify that DUT sends NetworkConfigResponse to the TH with following fields: 1. NetworkingStatus is NetworkIdNotFound 2. DebugText is of type string with max length 512 or empty |
| 11 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is PIXIT.CNET.WIFI_1S T_ACCESSPOINT_SSI D 2. NetworkIndex is 'Midpoint' 3. Breadcrumb is 2 | • Verify that DUT sends NetworkConfigResponse to the TH with following fields: 1. NetworkingStatus is success 2. DebugText is of type string with max length 512 or empty 3. NetworkIndex value as 'Midpoint' |

| 14 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 16 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 17 | • 11.8. 8.4 • 11.8. 8.6 • 11.8. 8.9 | • CNET.S.C0 2.Rsp(Add OrUpdate WiFiNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends AddOrUpdateWiFiNetwork command to the DUT. This step should be repeated 'RemainingNetworkSlots' times using DIFFERENT SSID and credential values and Breadcrumb field set to 1. Note that these credentials are NOT required to be connectable. | • Verify that DUT sends the NetworkConfigResponse command to each command to the TH with the following fields: 1. NetworkingStatus is success which is "0" 2. DebugText is of type string with max length 512 or empty |

| 18 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is PIXIT.CNET.WIFI_1S T_ACCESSPOINT_SSI D 2. NetworkIndex is 'Midpoint' 3. Breadcrumb is 2 | • Verify that DUT sends NetworkConfigResponse Command to the TH with following fields: 1. NetworkingStatus is success 2. DebugText is of type string with max length 512 or empty 3. NetworkIndex is 'Midpoint' |
| 20 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that DUT sends ArmFailSafeResponse command to the TH |

## TC-CNET-4.14 [Thread] Verification for ReorderNetwork command [DUT-Server] PROVISIONAL

## Purpose

Verify that the Networks list is re-ordered when using ReorderNetwork Command

## PICS

## · CNET.S.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | TH reads MaxNetworks attribute from DUT and is saved as 'MaxNetworksValue' for future use | • If MaxNetworksValue is < 2, skip the remaining steps. • Note: This test case is applicable for MaxNetworksValue >= 2 |
| 1b | * 11.9.7.1 * 11.9.7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |

| 3 | | | TH calculates the number of remaining network slots as 'MaxNetworksValue' - 'NumNetworks' and saves as 'RemainingNetworkSlots' | |
| 4 | | | TH calculates the midpoint of the network list as floor(('MaxNetworksValue' + 1)/2) and saves as 'Midpoint' | |
| 5 | • 11.8. 8.5 • 11.8. 8.6 • 11.8. 8.9 | • CNET.S.C0 3.Rsp(Add OrUpdate ThreadNe twork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends AddOrUpdateThreadNetwor k command to the DUT. This step should be repeated 'RemainingNetworkSlots' times using DIFFERENT OperationalDataset values and Breadcrumb set to 1. Note that these credentials are NOT required to be connectable. | • Verify that DUT sends the NetworkConfigResponse command to each command to the TH with the following fields: 1. NetworkingStatus is success, which is "0" 2. DebugText is of type string with max length 512 or empty |
| 7 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is the extended PAN ID of PIXIT.CNET.THREAD _1ST_OPERATIONAL DATASET 2. NetworkIndex is 'MaxNetworksValue' 3. Breadcrumb is 2 | • Verify that DUT sends NetworkConfigResponse to the TH with following fields: 1. NetworkingStatus is OutOfRange 2. DebugText is of type string with max length 512 or empty |

| 9 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is a NetworkID NOT present in 'OriginalNetworkList' 2. NetworkIndex is 'Midpoint' 3. Breadcrumb is 2 | • Verify that DUT sends NetworkConfigResponse to the TH with following fields: 1. NetworkingStatus is NetworkIdNotFound 2. DebugText is of type string with max length 512 or empty |
| 11 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is the extended PAN ID of PIXIT.CNET.THREAD _1ST_OPERATIONAL DATASET 2. NetworkIndex is 'Midpoint' | • Verify that DUT sends NetworkConfigResponse Command to the TH with following fields: 1. NetworkingStatus is success 2. DebugText is of type string with max length 512 or empty 3. NetworkIndex value as 'Midpoint' |

| 14 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 16 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 17 | • 11.8. 8.5 • 11.8. 8.6 • 11.8. 8.9 | • CNET.S.C0 3.Rsp(Add OrUpdate ThreadNe twork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends AddOrUpdateThreadNetwor k command to the DUT. This step should be repeated 'RemainingNetworkSlots' times using DIFFERENT OperationalDataset values and Breadcrumb set to 1. Note that these credentials are NOT required to be connectable. | • Verify that DUT sends the NetworkConfigResponse command to each command to the TH with the following fields: 1. NetworkingStatus is success, which is "0" 2. DebugText is of type string with max length 512 or empty |
| 18 | • 11.8. 8.12 • 11.8. 8.9 | • CNET.S.C0 8.Rsp(Reo rderNetw ork) • CNET.S.C0 5.Tx(Net workConf igRespons e) | • TH sends ReorderNetwork Command to the DUT with the following fields: 1. NetworkID is the extended PAN ID of PIXIT.CNET.THREAD _1ST_OPERATIONAL DATASET 2. NetworkIndex is 'Midpoint' | • Verify that DUT sends NetworkConfigResponse Command to the TH with following fields: 1. NetworkingStatus is success 2. DebugText is of type string with max length 512 or empty 3. NetworkIndex value as 'Midpoint' |
| 20 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with ExpiryLengthSeconds set to 0 | Verify that DUT sends ArmFailSafeResponse command to the TH |

## TC-CNET-4.15 [Wi-Fi] NetworkIDNotFound returned in LastNetworkingStatus field validation [DUT-Server]

## Purpose

- Verify that DUT responds with LastNetworkingStatus field set to NetworkIDNotFound for the following commands when the NetworkID does not exist:
1. RemoveNetwork Command
2. ConnectNetwork Command

## PICS

- CNET.S.F00(WI)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F00(WI) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ WIFI with FeatureMap attribute of 1 | |
| 3 | | DUT is factory reset | |
| 5 | | TH can communicate with the DUT | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with the ExpiryLengthSeconds field set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |
| 2 | • 11.8. 8.8 • 11.8. 8.9 | • CNET.S.C0 4.Rsp(Re moveNet work) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends RemoveNetwork Command to the DUT with NetworkID field set to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_SSID, which does not match the provisioned network, and Breadcrumb field set to 1 | Verify that DUT sends NetworkConfigResponse command to the TH1 with NetworkingStatus field set as NetworkIDNotFound which is '3' |
| 3 | • 11.8. 8.10 • 11.8. 8.9 | • CNET.S.C0 6.Rsp(Con nectNetw ork) • CNET.S.C0 7.Tx(Conn ectNetwo rkRespon se) | TH sends ConnectNetwork Command to the DUT with NetworkID field set to PIXIT.CNET.WIFI_2ND_ACCE SSPOINT_SSID, which does not match the provisioned network, and Breadcrumb field set to 1 | Verify that DUT sends ConnectNetworkResponse command to the TH1 with NetworkingStatus field as NetworkIDNotFound which is '3' |

## TC-CNET-4.16 [Thread] NetworkIDNotFound returned in LastNetworkingStatus field validation [DUT-Server]

## Purpose

- Verify that DUT responds with LastNetworkingStatus field set to NetworkIDNotFound for the following commands when the NetworkID does not exist:

1. RemoveNetwork Command
2. ConnectNetwork Command

## PICS

## · CNET.S.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 2 | | TH can communicate with the DUT on PIXIT.CNET.THREAD_1S T_OPERATIONALDATA SET | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | • 11.9. 7.1 • 11.9. 7.2 | | TH sends ArmFailSafe command to the DUT with the ExpiryLengthSeconds field set to 900 | Verify that DUT sends ArmFailSafeResponse command to the TH |

| 2 | • 11.8. 8.8 • 11.8. 8.9 | • CNET.S.C0 4.Rsp(Re moveNet work) • CNET.S.C0 5.Tx(Net workConf igRespons e) | TH sends RemoveNetwork Command to the DUT with NetworkID field set to the extended PAN ID of PIXIT.CNET.THREAD_2ND_O PERATIONALDATASET, which does not match the commissioned network, and Breadcrumb field set to 1 | Verify that DUT sends NetworkConfigResponse command to the TH1 with NetworkingStatus field set to NetworkIDNotFound which is '3' |
| 3 | • 11.8. 8.10 • 11.8. 8.9 | • CNET.S.C0 6.Rsp(Con nectNetw ork) • CNET.S.C0 7.Tx(Conn ectNetwo rkRespon se) | TH sends ConnectNetwork Command to the DUT with NetworkID value as the extended PAN ID of PIXIT.CNET.THREAD_2ND_O PERATIONALDATASET, which does not match the commissioned network, and Breadcrumb field set to 1 | Verify that DUT sends ConnectNetworkResponse command to the TH1 with NetworkingStatus field set to NetworkIDNotFound which is '3' |

## TC-CNET-4.22 [Thread] Verification for ScanNetworks command [DUT-Server]

## Purpose

1. Verification of ScanNetworks command for listing all available Thread networks within the range

## PICS

- CNET.S.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.S.F01(TH) | |
| 2 | | DUT has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ THREAD with FeatureMap attribute of 2 | |

| 4 | | TH can communicate with the DUT on PIXIT.CNET.THREAD_1S T_OPERATIONALDATA SET |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Server |
| 2 | TH | Client |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| 1 | • 11.8. 8.2 • 11.8. 8.3 | • CNET.S.C0 0.Rsp(Sca nNetwork s) • CNET.S.C0 1.Tx(Scan Networks Response) | TH sends ScanNetworks command to the DUT with the SSID field omitted and the Breadcrumb field set to 1 | • Verify that DUT sends ScanNetworksResponse command to the TH with the following fields: • NetworkingStatus field value is Success • DebugText is of type string with max length 512 or absent • Verify WiFiScanResults is None • Verify Thread interfaces are not None and length equal to 0 • Each element in the ThreadScanResults list will have the following fields: 1. PanId with a range of 0 to 65534 2. ExtendedPanId 3. NetworkName is a string with a size of 1 to 16 bytes |

| 3 | | • CNET.S.C0 0.Rsp(Sca nNetwork s) • CNET.S.C0 1.Tx(Scan Networks Response) | TH sends ScanNetworks command to the DUT with the SSID field set to null and the Breadcrumb field set to 2 | • Verify that DUT sends ScanNetworksResponse command to the TH with the following fields: • NetworkingStatus field value is Success • DebugText is of type string with max length 512 or absent • Verify WiFiScanResults is None • Verify Thread interfaces are not None and length equal to 0 • Each element in the ThreadScanResults list will have the following fields: 1. PanId with a range of 0 to 65534 2. ExtendedPanId 3. NetworkName is a string with a size of 1 to 16 bytes 4. Channel is of type uint16 with a range 0 to 65535 5. Version is a uint8 |

| 5 | | • CNET.S.C0 0.Rsp(Sca nNetwork s) • CNET.S.C0 1.Tx(Scan Networks Response) | TH sends ScanNetworks command to the DUT with the SSID field set to a random string of ASCII characters with a size of between 1 and 31 characters and the Breadcrumb field set to 3 | • Verify that DUT sends ScanNetworksResponse command to the TH with the following fields: • NetworkingStatus field value is Success • DebugText is of type string with max length 512 or absent • Verify WiFiScanResults is None • Verify Thread interfaces are not None and length equal to 0 • Each element in the ThreadScanResults list will have the following fields: 1. PanId with a range of 0 to 65534 2. ExtendedPanId 3. NetworkName is a string with a size of 1 to 16 bytes 4. Channel is of type uint16 with a range 0 to 65535 5. Version is a uint8 6. ExtendedAddress is a hwaddr with a size of 8 bytes |

## 7.4.3. DUT as Client

## TC-CNET-4.20 [Wi-Fi] Verification for commands check [DUT-Client]

## Purpose

Verify the DUT is able to correctly send all commands to the TH

## · CNET.C.F00(WI)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.C.F00(WI) | |
| 2 | | TH has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ WIFI with FeatureMap attribute of 1 | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Client |
| 2 | TH | Server |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## TC-CNET-4.21 [Thread] Verification for commands check [DUT-Client]

## Purpose

Verify the DUT is able to correctly send all commands to the TH

## PICS

## · CNET.C.F01(TH)

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT supports CNET.C.F01(TH) | |
| 2 | | TH has a Network Commissioning cluster on endpoint PIXIT.CNET.ENDPOINT_ THREAD with FeatureMap attribute of 2 | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Client |
| 2 | TH | Server |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Chapter 8. Secure Channel Test Plan

## 8.1. PICS Definition

This section covers the Secure Channel related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.SC.VENDOR_SU BTYPE | Does device support optional subtype _V in commissionable node discovery mDNS? | O | |
| MCORE.SC.DEVTYPE_S UBTYPE | Does device support optional subtype _T in commissionable node discovery mDNS? | O | |
| MCORE.SC.VP_KEY | Does device support optional key VP in commissionable node discovery mDNS? | O | |
| MCORE.SC.DT_KEY | Does device support optional key DT in commissionable node discovery mDNS? | O | |
| MCORE.SC.DN_KEY | Does device support optional key DN in commissionable node discovery mDNS? | O | |
| MCORE.SC.RI_KEY | Does device support optional key RI in commissionable node discovery mDNS? | O | |
| MCORE.SC.PH_KEY | Does device support optional key PH in commissionable node discovery mDNS? | O | |
| MCORE.SC.PI_KEY | Does device support optional key PI in commissionable node discovery mDNS? | O | |

| MCORE.SC.SII_OP_DISC OVERY_KEY | Does device support optional key SII in operational discovery mDNS? | O |
| MCORE.SC.SAI_OP_DISC OVERY_KEY | Does device support optional key SAI in operational discovery mDNS? | O |
| MCORE.SC.SAT_OP_DIS COVERY_KEY | Does device support optional key SAT in operational discovery mDNS? | O |
| MCORE.SC.T_KEY | Does device support optional key T in operational discovery mDNS? | O |
| MCORE.SC.SII_COMM_D ISCOVERY_KEY | Does device support optional key SII in commissionable node discovery mDNS? | O |
| MCORE.SC.SAI_COMM_ DISCOVERY_KEY | Does device support optional key SAI in commissionable node discovery mDNS? | O |
| MCORE.SC.EXTENDED_ DISCOVERY | Does device support Extended Discovery for Commissionable Node Discovery? | O |
| MCORE.SC.SIT_ICD | Is the device a Short Idle Time ICD? | O |
| MCORE.DD.COMM_DIS COVERY | Does the DUT support advertising Commissioner Discovery service records? | O |
| MCORE.SC.TCP | Does Device support TCP? | O |

Additionally, a few PICS items from the ICDM cluster, Basic Information cluster, and Administrator Commissioning cluster are used in this test plan.

## 8.2. Test Case List

| TC UUID | Test Case Name |
| TC-SC-1.1 | MRP Max Messaging Size Verification - PROVISIONAL |
| TC-SC-1.2 | MRP Message Flows - PROVISIONAL |
| TC-SC-1.3 | MRP Retransmissions - PROVISIONAL |
| TC-SC-1.4 | MRP Message Counter and Duplicate Messaging Verification - PROVISIONAL |
| TC-SC-2.1 | PASE Session Establishment - PROVISIONAL |
| TC-SC-2.3 | PASE Error Handling [DUT_Responder/Commissionee] - PROVISIONAL |
| TC-SC-2.4 | PASE Error Handling [DUT_Initiator/Commissioner] - PROVISIONAL |
| TC-SC-3.1 | CASE Session Establishment - PROVISIONAL |
| TC-SC-3.2 | CASE Session Resumption [DUT_Responder] - PROVISIONAL |
| TC-SC-3.3 | CASE Session Resumption [DUT_Initiator] - PROVISIONAL |
| TC-SC-3.4 | CASE Error Handling [DUT_Responder] |
| TC-SC-3.5 | CASE Error Handling [DUT_Initiator] - PROVISIONAL |
| TC-SC-3.6 | CASE Resource validation |
| TC-SC-4.1 | Commissionable Node Discovery [DUT as Commissionee] |
| TC-SC-4.2 | Discovery [DUT as Commissioner] |
| TC-SC-4.3 | Discovery [DUT as Commissionee] |
| TC-SC-4.4 | Discovery [DUT as Controller] |
| TC-SC-4.6 | Commissioner Discovery [DUT as Commissioner] |
| TC-SC-4.7 | Commissioner Discovery [DUT as Commissionee] |
| TC-SC-4.8 | Compressed Fabric ID remains the same for Nodes commissioned to the same fabric [DUT as Commissioner] |
| TC-SC-4.9 | Operational Discovery - RIO support [DUT as Commissionee] |
| TC-SC-7.1 | Unique discriminators [DUT as Commissionee] |

| TC UUID | Test Case Name |
| TC-SC-8.5 | Test InvokeCommandRequest and CommandResponse over a TCP-based CASE session established with DUT. |
| TC-SC-8.6 | Test a Large Payload interaction over a TCP- based CASE session with DUT via a wildcard Read operation. |
| TC-SC-8.7 | Test that an IM operation(possible over MRP) can use an already existing TCP-based session with DUT. |

## 8.3. Test Cases

## 8.3.1. Matter Reliable Message Protocol (MRP) Test Cases

## TC-SC-1.1 MRP Max Message Size - PROVISIONAL

## Purpose

This test case verifies that the DUT handles large messages as per the specification

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT has implemented/supports the Matter Echo protocol | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network |
| 2 | DUT | Device acting as a node on a Matter network |

## Device Topology

TH and DUT are on the same fabric

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 4.4.4 (Messag e Size Require ments) | | TH sends a single message to DUT with a message size equal to 1280 bytes inclusive of headers and reliability flag set to 1 | Verify DUT responds with an acknowledgement of receipt. |

## Notes/Testing considerations

## TC-SC-1.2 MRP Message Flows - PROVISIONAL

## Purpose

Verify that MRP handles and processes messages accordingly with flags set in the message header.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |

| # | Doc. Ref. | Condition | Notes |
| 2 | | DUT has implemented/supports the Matter Echo protocol | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network |
| 2 | DUT | Device acting as a node on a Matter network |

## Device Topology

TH and DUT are on the same fabric

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 3b | 4.11.2.2, 4.11.5.1 | | DUT must respond to the message with a MRP reply packet that doesn't piggyback the ACK (A flag not set). | DUT should send only a MRP reply packet to TH with no ACK piggybacked or sent in a separate message. |

## Notes/Testing considerations

## TC-SC-1.3 MRP Retransmissions - PROVISIONAL

## Purpose

This test case verifies that the message is dropped after the max number of failed attempts

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT has implemented/supports the Matter Echo protocol | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network |
| 2 | DUT | Device acting as a node on a Matter network |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Simulate TH to ignore all messages received by DUT (100% message loss) | |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

1. Step 3 - The DUT should also start operational discovery in parallel with retransmission and the DUT should also be able to receive discovery packets during this test. Associated verification steps are not yet included here due to a desire to keep test cases separated/single-purpose, but we may add a combined test case at a later point.
2. Step 3 - The value for MRP\_RETRY\_INTERVAL\_IDLE should be obtained by the TH from the DNSSD TXT record for the node if present. If it is not available, then the default value is 5000 ms.
3. Step 4 - The default value for MRP\_MAX\_TRANSMISSIONS is 4.

## TC-SC-1.4 MRP message counter and duplicate messaging - PROVISIONAL

## Purpose

This test case verifies that duplicate messages are discarded.

## PICS

- MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT has implemented/supports the Matter Echo protocol | |

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network |
| 2 | DUT | Device acting as a node on a Matter network |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## 8.3.2. Session Establishment

## TC-SC-2.1 Session Establishment - Passcode Authenticated Session Establishment (PASE) PROVISIONAL

## Purpose

This test case verifies that the DUT can successfully establish a session using a passcode and Password Authenticated Key Agreement (PAKE), which for now is only used when commissioning a node.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | Spec 4.13.1.1 | Initiator has obtained the Matter passcode and that the responder has the relevant CHIP_Crypto_PAKEValu es_Responder corresponding to the passcode | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network |
| 2 | DUT | Device acting as a node on a Matter network |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | Test Step | Expected Outcome |
| 3 | 4.1 3.1. 2, 3.5 | Initiator constructs and sends a TLV-encoded Pake1 message | Verify that the Responder receives the Pake1 message. Verify that the protocol header is properly constructed: 1. Message Flags: S Flag is set to 0, and DSIZ field is set to 0 2. Session ID is set to 0 3. Security Flags: Session Type bits are set to 0 4. Exchange Flags: I Flag is set to 1 5. Protocol Opcode is set to 34 (0x22) 6. Protocol ID is set to 0 Verify, if possible in a debug mode, that the Pake1 message contains: 1. pA - 65 bit octet string |

| # | Ref | Test Step | Expected Outcome |
| 4 | 4.1 3.1. 2, 3.5, 3.3 | Responder constructs and sends a TLV-encoded Pake2 message | Verify that the Initiator receives the Pake2 message. Verify that the protocol header is properly constructed: 1. Message Flags: S Flag is set to 0, and DSIZ field is set to 0 2. Session ID is set to 0 3. Security Flags: Session Type bits are set to 0 4. Exchange Flags: I Flag is set to 0 5. Protocol Opcode is set to 35 (0x23) 6. Protocol ID is set to 0 Verify, if possible in a debug mode, that the Pake1 message contains: 1. pB - 65 bit octet string 2. cB - 32 bit octet string |

| # | Ref | Test Step | Expected Outcome |
| 5 | 4.1 3.1. 2, 3.3 | Initiator constructs and sends a TLV-encoded Pake3 message | Verify that the Responder receives the Pake3 message. Verify that the protocol header is properly constructed: 1. Message Flags: S Flag is set to 0, and DSIZ field is set to 0 2. Session ID is set to 0 3. Security Flags: Session Type bits are set to 0 4. Exchange Flags: I Flag is set to 1 5. Protocol Opcode is set to 36 (0x24) 6. Protocol ID is set to 0 Verify, if possible in a debug mode, that the Pake3 message contains: |
| 6 | 4.1 3.1. 2, 4.9. 1 | Responder validates Pake3, then constructs and sends a status report (PakeFinished) message | Verify that the Initiator receives the status report/PakeFinished message. Verify that the status report contains: 1. GeneralCode - SUCCESS (value 0) 2. ProtocolId - SECURE_CHANNEL (value 0x0000) 3. ProtocolCode - SESSION_ESTABLISHMENT_SUCCESS (value 0x0000) Verify that the initiator has not sent any encrypted data to the responder prior to |

## Notes/Testing considerations

1. Step 1 and Step 3 - Potentially non-testable item - Session IDs, InitiatorSessionId in this case, should not overlap.
2. Can we check session context somehow?

## TC-SC-2.3 PASE Error Handling [DUT\_Responder/Commissionee] - PROVISIONAL

## Purpose

This test case verifies that the DUT can properly respond to error cases during PASE messaging

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | Spec 4.12.1.2 | Initiator has obtained the Matter passcode and that the responder has the relevant CHIP_Crypto_PAKEValu es_Responder corresponding to the passcode | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a initiator node on a Matter network |
| 2 | DUT | Device acting as a responder node on a Matter network |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

The TH is set up as a Commissioner/Initiator and the DUT as a Commissionee/Responder

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-2.4 PASE Error Handling [DUT\_Initiator/Commissioner] - PROVISIONAL

## Purpose

This test case verifies that the DUT can properly respond to error cases during PASE messaging

## PICS

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | Spec-4.12.1.2 | Initiator has obtained the Matter passcode and that the responder has the relevant CHIP_Crypto_PAKEValu es_Responder corresponding to the passcode | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a responder node on a Matter network |
| 2 | DUT | Device acting as a initiator node on a Matter network |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

The DUT set up as a Commissioner/Initiator and the TH as a Commissionee/Responder

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## 8.3.3. Certificate Authenticated Session Establishment (CASE) Test Cases

## TC-SC-3.1 Session Establishment - PROVISIONAL

## Purpose

This test case verifies that the initiator and responder can establish a sessions to successfully send and receive encrypted messages

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network - Initiator |

| # | Device Name | Device Description |
| 2 | DUT | DUT acting as a node on a Matter network -Responder |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-3.2 CASE Session Resumption [DUT\_Responder] - PROVISIONAL

## Purpose

This test case verifies that the initiator and responder can successfully resume a CASE exchange

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network - Initiator |
| 2 | DUT | DUT acting as a node on a Matter network -Responder |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH is the Initiator and the DUT is the Responder. TH and the DUT are commissioned.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## TC-SC-3.3 CASE Session Resumption [DUT\_Initiator] - PROVISIONAL

## Purpose

This test case verifies that the Initiator and Responder can successfully resume a CASE exchange

## PICS

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network - Responder |
| 2 | DUT | DUT acting as a node on a Matter network - Initiator |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

DUT is the Initiator and the TH is the Responder.TH and the DUT are commissioned.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 2a | | | | Verify that the Initiator sends the Sigma1 message to Responder |

| 2b | 4.13.2.2, 4.13.2.3, | Responder receives the Sigma1 message and extracts the following | • Verify that the message is properly formatted: |
| | | 2. initiatorSessionId | 2. S flag and DSIZ fields of message flags are set to 0 |
| | | 3. destinationId 4. resumptionID | 3. The Session Key Type field is set to 0 |
| | | 5. initiatorResumeMIC 6. initiatorEphPubKey | 4. The Protocol ID field is set to 0x0000 and |
| | | 7. initiatorSessionParams | 5. The Protocol Opcode field is set to 0x30 |
| | | | • Verify that the initiatorRandom is of Octet String maximum of length 32 bytes |
| | | | • Verify that the initiatorSessionId is of uint16 |
| | | | • Verify that the destinationId is of Octet string |
| | | | • Verify that the resumptionID from the Initiator matches with the precondition 1. Verify that the |
| | | | resumptionID is of Octet String maximum of length |
| | | | • Verify that the initiatorEphPubKey is of Octet string |
| | | | • Verify that the initiatorResumeMIC is of Octet |
| | | | string • Verify that |
| | | | the responderSessionParams is from any one of the following: |
| | | | 1. SESSION_IDLE_INTERVAL a. Verify that it is of uint32 |
| | | | 2. L |
| | | | SESSION_ACTIVE_INTERVA |
| | | | a. Verify that it is of uint32 |
| | | | 3. SESSION_ACTIVE_THRESH |

## Notes/Testing considerations

## TC-SC-3.4 CASE Error Handling [DUT\_Responder]

## Purpose

This test case verifies that the DUT can handle CASE error scenarios as a responder

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Condition | Notes |
| 1 | Underlying transport is reliable, either implicitly (i.e.: TCP) or explicitly (i.e.: MRP) | |
| 2 | DUT is commissioned by TH | |
| 3 | TH has an existing CASE Session with DUT at the start of the test | Having an open CASE Session ensures that TH will send a "Sigma1 with Resumption" in Test Step #1 |

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node on a Matter network - Initiator |
| 2 | DUT | Device acting as a node on a Matter network - Responder |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

The TH is the Initiator and the DUT is the Responder

All Steps make use of Fault Injection locally on the TH itself

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH constructs and sends a Sigma1 message with a resumptionID and no initiatorResumeMIC to DUT | • Verify that the DUT sends a status report to the TH with a FAILURE general code , Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no |
| 2 | TH constructs and sends a Sigma1 message with a initiatorResumeMIC and no resumptionID to DUT | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no further processing after sending the status report. |

| # | Test Step | Expected Outcome |
| 4 | TH constructs and sends a Sigma1 message with an invalid destinationId to DUT | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of NO_SHARED_TRUST_ROOTS (0X0001). • Verify that the DUT performs no further processing after sending the |
| 5 | TH sends a valid Sigma1 message to DUT. In reply to the received Sigma2, TH Sends back a Sigma3 message with improperly generated encrypted integrity data ( TBEData3Encrypted ) | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no |
| 6 | TH sends a valid Sigma1 message to DUT. In reply to the received Sigma2, TH Sends back a Sigma3 message with invalid initiatorNOC data | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no |

| # | Test Step | Expected Outcome |
| 7 | TH sends a valid Sigma1 message to DUT. In reply to the received Sigma2, TH Sends back a Sigma3 message with invalid initiatorICAC data | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no further processing after sending the |
| 8 | TH sends a valid Sigma1 message to DUT. In reply to the received Sigma2, TH Sends back a Sigma3 message with invalid signature data | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no |
| 9 | TH sends a valid Sigma1 message to DUT. In reply to the received Sigma2, TH Sends back a Sigma3 message with invalid initiatorEphPubKey data | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no |
| 10 | TH sends a valid Sigma1 message to DUT. In reply to the received Sigma2, TH Sends back a Sigma3 message with invalid responderEphPubKey data | • Verify that the DUT sends a status report to the TH with a FAILURE general code, Protocol ID of SECURE_CHANNEL (0x0000), and Protocol Code of INVALID_PARAMETER (0X0002). • Verify that the DUT performs no |

## Notes/Testing considerations

## TC-SC-3.5 CASE Error Handling [DUT\_Initiator] - PROVISIONAL

## Purpose

This test case verifies that the DUT can handle CASE error scenarios as a initiator

## PICS

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Condition | Notes |
| 1 | Underlying transport is reliable, either implicitly (i.e.: TCP) or explicitly (i.e.: MRP) | |
| 2 | TH_SERVER has been commissioned to TH_CLIENT | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CLIENT | Test harness acting as a client on a Matter network |
| 2 | TH_SERVER | Test Harness Server application (such as all-cluster-app) that includes Fault Injection Cluster. |
| 3 | DUT | Device acting as an Initiator on a Matter network (Usually Commissioner) |

## Device Topology

TH\_CLIENT and TH\_SERVER are on the same fabric

## Test Setup

The DUT is the Initiator and the TH\_SERVER is the Responder.

TH\_CLIENT will be used to Send Fault Injection Commands to TH\_SERVER.

TH\_CLIENT will also be used to Open Commissioning Window on TH\_SERVER to allow it to accept Commissioning Requests from DUT.

CASE Failures will show up in the CASE Handshake Step of the Commissioning

## Test Procedure

| # | Test Step | Expected Outcome |
| 1a | TH Client sends an OpenCommissioningWindow command to TH_SERVER to allow it to be commissioned by DUT_Commissioner to determine if the DUT_Commissioner has an ICAC in its NOC Chain | Verify that the TH_SERVER returns SUCCESS |
| 1c | TH Client Reads the NOCs attribute on TH_SERVER and checks if DUT_Commissioner has ICAC in its NOC Chain | Verify that NOCs attribute returns two NOCStructs and determine if DUT_Commissioner has ICAC |
| 1d | TH Client removes the DUT_Commissioner's fabric from TH_SERVER | Verify that the DUT_Commissioner's fabric is removed from TH_SERVER |
| 2a | TH Client sends an OpenCommissioningWindow command to TH_SERVER to allow it to be commissioned by DUT_Commissioner and trigger CASE Handshake | Verify that the TH_SERVER returns SUCCESS |
| 2c | TH prompts the user to Commission DUT_Commissioner to TH_SERVER | Verify that the DUT sends a status report to TH_SERVER with a FAILURE general code (value 1), protocol ID of SECURE_CHANNEL (0x0000), and Protocol code of INVALID_PARAMETER (0X0002). Verify that the commissioning failed by checking that the commissioning window is still open on TH_SERVER. |
| 3a | TH Client revokes the Commissioning Window and resend an OpenCommissioningWindow command to TH_SERVER to allow commissioning by DUT_Commissioner again and re-trigger the CASE handshake. | Verify that the TH_SERVER returns SUCCESS |

| # | Test Step | Expected Outcome |
| 4a | TH Client revokes the Commissioning Window and resend an OpenCommissioningWindow command to TH_SERVER to allow commissioning by DUT_Commissioner again and re-trigger the CASE handshake. | This Test Step is skipped if DUT_Commissioner does not have ICAC in its NOC Chain, Verify that the TH_SERVER returns SUCCESS |
| 5a | TH Client revokes the Commissioning Window and resend an OpenCommissioningWindow command to TH_SERVER to allow commissioning by DUT_Commissioner again and re-trigger the CASE handshake. | Verify that the TH_SERVER returns SUCCESS |

| # | Test Step | Expected Outcome |
| 5b | TH Client sends FailAtFault command to FaultInjection cluster on TH_SERVER to include a corrupt Signature in the Sigma2 it will send during CASE Handshake | Verify that the TH_SERVER receives the message |
| 5c | TH prompts the user to Commission DUT_Commissioner to TH_SERVER again | Verify that the DUT sends a status report to TH_SERVER with a FAILURE general code (value 1), protocol ID of SECURE_CHANNEL (0x0000), and Protocol code of INVALID_PARAMETER (0X0002). Verify that the commissioning failed by checking that the commissioning window is still open on TH_SERVER. |

## TC-SC-3.6 CASE Resource validation

## Purpose

This test case verifies that the DUT is able to handle at least three CASE sessions.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT's CaseSessionsPerFabric in CapabilityMinima is at least 3 | |

## Required Devices

| # | Device Name | Device Description |
| 1 | RD1A | Reference Device 1A as the commissioner and subscriber |
| 2 | RD1B | Reference Device 1B as the subscriber |
| 3 | RD1C | Reference Device 1C as the subscriber |
| 4 | RD2A | Reference Device 2A as the commissioner and subscriber |
| 5 | RD2B | Reference Device 2B as the subscriber |
| 6 | RD2C | Reference Device 2C as the subscriber |
| 7 | RD3A | Reference Device 3A as the commissioner and subscriber |
| 8 | RD3B | Reference Device 3B as the subscriber |
| 9 | RD3C | Reference Device 3C as the subscriber |

| # | Device Name | Device Description |
| 10 | RD4A | Reference Device 4A as the commissioner and subscriber |
| 11 | RD4B | Reference Device 4B as the subscriber |
| 12 | RD4C | Reference Device 4C as the subscriber |
| 13 | RD5A | Reference Device 5A as the commissioner and subscriber |
| 14 | RD5B | Reference Device 5B as the subscriber |
| 15 | RD5C | Reference Device 5C as the subscriber |

## Device Topology

RD1X, RD2X, RD3X, RD4X, RD5X should be on separate, distinct fabrics.

- RD1A, RD1B and RD1C should be on the same fabric.
- RD2A, RD2B and RD2C should be on the same fabric.
- RD3A, RD3B and RD3C should be on the same fabric.
- RD4A, RD4B and RD4C should be on the same fabric.
- RD5A, RD5B and RD5C should be on the same fabric.
- DUT should be commissioned onto all fabrics

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | RD1X, RD2X, RD3X, RD4X, RD5X each send 1 Subscribe Request Messages to DUT.(Total - 15 active subscriptions) They can subscribe to any attribute. Once all subscriptions are active, change the value of the attribute that has been subscribed to | Verify that all subscribers get data reports. Verify on each of these Reference Devices that the appropriate attribute value has been received. |

## Notes/Testing considerations

1. RD1X indicates RD1A, RD1B, RD1C
2. RD2X indicates RD2A, RD2B, RD2C
3. RD3X indicates RD3A, RD3B, RD3C
4. RD4X indicates RD4A, RD4B, RD4C

5. RD5X indicates RD5A, RD5B, RD5C
6. Vendor can have greater than 3 CaseSessionsPerFabric

## 8.3.4. Discovery

## TC-SC-4.1 Commissionable Node Discovery [DUT as Commissionee]

## Purpose

The purpose of this test case is to verify that a device is able to correctly advertise Commissionable Node Discovery service.

## PICS

- MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Node that is advertising Commissionable Node Discovery service using DNS-SD. |
| 2 | TH | Commissioner that is scanning for DNS-SD |

## Device Topology

N/A

Test Setup

N/A

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | DUT is Commissioned | |
| 2 | Check if the ICD Management cluster is present | TH checks for the presence of the ICD Management cluster by reading from the DUT the ServerList attribute from the Descriptor cluster on EP0 • Set supports_icd to True if present, otherwise, to False • If supports_icd is True ◦ TH reads ActiveModeThreshold from the ICD Management cluster on EP0 and saves as active_mode_threshold_ms |
| 3 | Check if the LITS (Long Idle Time Support) feature is supported | If supports_icd is True : • TH checks for support of the LITS feature by reading from the DUT the FeatureMap attribute from the ICD Management cluster on EP0 ◦ Set supports_lit to True if supported, otherwise, to False |
| 4 | Check if TCP is supported by the DUT | Set supports_tcp_dut to True if supported, otherwise, to False |
| 5 | Check if TCP is supported by the PICS | Set supports_tcp_pics to True if supported, otherwise, to False |
| 6 | Check the setup code type used during commissioning ( QR or Manual ) | Save as setup_code_type |
| 7 | Check if the Open Basic Commissioning Window command is supported | Set supports_obcw to True if supported, otherwise, to False |
| 8 | DUT is put in Commissioning Mode using the Open Basic Commissioning Window command if supported | DUT starts advertising Commissionable Node Discovery services |

| # | Test Step | Expected Outcome |
| 9 | TH gets the discriminator from the DUT and constructs the Discriminator subtype ( Long or Short ) based on the setup code type ( QR or | If setup_code_type is QR , construct the Long Discriminator Subtype • Verify that the discriminator value is a valid 12-bit variable length decimal number in ASCII text, omitting any leading zeros If setup_code_type is Manual , construct the Short Discriminator Subtype • Verify that the discriminator value is a valid 4-bit variable length decimal number in ASCII text, omitting any leading zeros |
| 10 | Get the Discriminator Subtype PTR record's instance name | TH performs a PTR record query against the Discriminator Subtype ( Long or Short from the previous step) • Verify that there is one, and only one, Discriminator subtype PTR record • Save the Discriminator Subtype PTR record's instance name as |
| 11 | Verify commissionable subtype advertisements | See the Commissionable Subtypes Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |
| 12 | Verify SRV record advertisements | See the SRV Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |
| 13 | Verify TXT record advertisements | See the TXT Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed. Expected CM TXT key value = 1 |
| 14 | Verify AAAA records | See the AAAA Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |
| 15 | Close commissioning window | DUT stops advertising Commissionable Node Discovery services |
| 16 | TH gets the Long Discriminator from the DUT and constructs the Long Discriminator Subtype | Verify that the Long discriminator value is a valid 12-bit variable length decimal number in ASCII text, omitting any leading zeros Save the Long Discriminator value as long_discriminator Save the Long Discriminator Subtype as long_discriminator_subtype |

| # | Test Step | Expected Outcome |
| 17 | DUT is put in Commissioning Mode using Open Commissioning Window command | DUT starts advertising Commissionable Node Discovery services |
| 18 | Get the Long Discriminator Subtype PTR record's instance name | TH performs a PTR record query against the Long Discriminator Subtype • Verify that there is one, and only one, Long Discriminator Subtype PTR record • Save the Long Discriminator Subtype PTR record's instance name as long_discriminator_subtype_ptr_instance_name |
| 19 | Verify commissionable subtype advertisements | See the Commissionable Subtypes Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |
| 20 | Verify SRV record advertisements | See the SRV Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |
| 21 | Verify TXT record advertisements | See the TXT Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed. Expected CM TXT key value = 2 |
| 22 | Verify AAAA records | See the AAAA Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |
| 23 | Close commissioning window | DUT stops advertising Commissionable Node Discovery services |
| 24 | Check if DUT Extended Discovery mode is active | The DUT will be advertising Commissionable Service services without having a commissioning window open if in Extended Discovery mode • Get the Long Discriminator Subtype PTR record's instance name ◦ If the DUT's Long Discriminator Subtype PTR record's instance name is present, Extended Discovery mode is active, if so, save the _Long Discriminator Subtype PTR record's instance name as long_discriminator_subtype_ptr_instance_name |
| 25 | Verify commissionable subtype advertisements (if in Extended Discovery mode) | See the Commissionable Subtypes Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |

| # | Test Step | Expected Outcome |
| 26 | Verify SRV record advertisements (if in Extended Discovery mode) | See the SRV Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |
| 27 | Verify TXT record advertisements (if in Extended Discovery mode) | See the TXT Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed. Expected CM TXT key value = 0 or omitted key |
| 28 | Verify AAAA records (if in Extended Discovery mode) | See the AAAA Record Verifications table in the Notes/Testing considerations section for the list of verifications to be performed |

## Notes/Testing considerations

Perform each of the following verifications where indicated in the test steps, updating only the expected TXT record CM key value.

In previous steps, either the Long or Short discriminator was verified (depending on weather QR Code or Manual setup code was used respectively), for the below verifications, the opposing discriminator will be verified (if Long Discriminator was verified earlier, then the below verification will check the Short Discriminator ).

## Commissionable Subtypes Verifications

## TH performs a browse for the Commissionable Service subtypes

## Mandatory Subtypes

- Long/Short Discriminator
- Verify that the Discriminator Subtype is present
- Verify that it contains a valid 12-bit (Long) or 4 bit (Short) variable length decimal number in ASCII text, omitting any leading zeros 'Discriminator' value
- When the Long Discriminator is provided, the TH performs a PTR record query against the Short Discriminator Subtype and performs verifications, omit if the Short Discriminator is provided
- Verify that there is one, and only one, Short Discriminator Subtype PTR record
- Verify that the Short and Long Discriminator Subtype ( discriminator\_subtype\_ptr\_instance\_name ) PTR record's instance names are equal
- In Commissioning Mode
- Verify the expected presence of the In Commissioning Mode Subtype \_CM
- If the DUT is in Extended Discovery Mode:
- Verify that the \_CM subtype is NOT present
- If the DUT is NOT in Extended Discovery Mode
- Verify that the \_CM subtype is present
- TH performs a PTR record query against the In Commissioning Mode Subtype
- Verify that there is one, and only one, In Commissioning Mode Subtype PTR record
- Verify that the In Commissioning Mode Subtype PTR record's instance name is equal to discriminator\_subtype\_ptr\_instance\_name

## Optional Subtypes

- Vendor
- Check for the presence of the Vendor Subtype \_V, if present:
- Verify that it contains a valid 16-bit variable length decimal number in ASCII text, omitting any leading zeros Vendor Subtype value
- TH performs a PTR record query against the Vendor Subtype , if present:
- Verify that the Vendor Subtype PTR record's instance name is equal to discriminator\_subtype\_ptr\_instance\_name
- Devtype
- Check for the presence of the Devtype Subtype \_T, if present:
- Verify that it contains a valid 32-bit variable length decimal number in ASCII text, omitting any leading zeros Devtype Subtype value
- TH performs a PTR record query against the Devtype Subtype , if present:

## SRV Record Verifications

TH performs a Commissionable Service SRV record query against discriminator\_subtype\_ptr\_instance\_name

- Verify SRV record is returned
- Verify that the SRV record's instance name is equal to discriminator\_subtype\_ptr\_instance\_name
- Verify that the SRV record's instance name is a 64-bit randomly selected ID expressed as a sixteen-char hex string with capital letters
- Verify that the SRV record's service type is '\_matterc.\_udp' and service domain '.local.'
- Verify that the target hostname is derived from the 48bit or 64bit MAC address expressed as a twelve or sixteen capital letter hex string

## TXT Record Verifications

## TH performs a Commissionable Service TXT record query against discriminator\_subtype\_ptr\_instance\_name

- Verify that the TXT record is returned and is non-empty
- Verify that the TXT record's instance name is equal to discriminator\_subtype\_ptr\_instance\_name

## TXT key verifications

## ICD Key

- If supports\_lit is True
- Verify that the ICD key is present and non-empty
- Verify that the ICD key has the value of 0 or 1 encoded as a decimal number in ASCII text omitting any leading zeros
- If supports\_lit is False
- Verify that the ICD key is NOT present

## SIT Mode

- Set sit\_mode to True when:
- supports\_icd is True and supports\_lit is False or
- supports\_icd is True and supports\_lit is True and ICD == 0
- Set sit\_mode to False when:
- supports\_icd is False or
- supports\_icd is True and supports\_lit is True and ICD == 1

## SII Key

- Verify that the SII key is present and non-empty if sit\_mode is True
- Verify that the SII key is an unsigned integer with units of milliseconds encoded as a variable length decimal number in ASCII text, omitting any leading zeros, and shall not exceed 3600000

## SAI Key

- Verify that the SAI key is present and non-empty if supports\_icd is True
- Verify that the SAI key is an unsigned integer with units of milliseconds encoded as a variable length decimal number in ASCII text, omitting any leading zeros, and shall not exceed 3600000

## SAT Key

- If the SAT key is present
- Verify that it is non-empty
- Verify that it is an unsigned integer with units of milliseconds encoded as a variable length decimal number in ASCII text, omitting any leading zeros, and shall be less than or equal to 65535

## AAAA Record Verifications

TH performs a AAAA record query against the target hostname listed in the Commissionable Service SRV record

- Verify that at least 1 AAAA record is returned for each IPv6 a address
- Verify that each AAAA record contains a valid IPv6 address

## TC-SC-4.2 Discovery [DUT as Commissioner]

## Purpose

The purpose of this test case is to verify that a commissioner is able to discover a node that announce Commissionable Node Discovery service.

## PICS

## · MCORE.ROLE.COMMISSIONER

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissioner scanning for commissionee nodes that advertise Commissionable Node Discovery service. |

## Device Topology

N/A

Test Setup

N/A

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | By any means, TH adds an unknown key/value pair in the advertised data(e.g. AB=12345) and is in Commissioning Mode | TH must advertise with new data added |
| 2 | | | DUT attempts to commission TH | DUT successfully commissions TH and the unknown key/value pair added at step 1 must be silently discarded |

## Notes/Testing considerations

Open discussion over the utility of this TC. May be removed in the future!

## TC-SC-4.3 Discovery [DUT as Commissionee]

## Purpose

The purpose of this test case is to verify that a Matter node is discoverable and can advertise its services in a Matter network.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Nodes are joined in the same Fabric | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Matter Node that is advertising a service |
| 2 | TH | Matter Controller |

## Platform Certification

In the context of a platform certification, If the platform supports multiple transport layers, the test case must be executed for each supported transport layer.

For other PICS such as C.9.17 and C.4.3.2, since their support does not change the outcome of other steps in this test case, the test does not need to be repeated with or without these PICS.

TH and DUT are on the same fabric.

## Test Setup

## N/A

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | DUT is commissioned on the same fabric as TH | |
| 2 | C.9.17 | | TH reads from the DUT the ServerList attribute from the Descriptor cluster on EP0. If the ICD Management cluster ID (70,0x46) is present in the list, set supports_icd to true, otherwise set supports_icd to false. | |
| 3 | C.9.17 | | If supports_icd is true, TH reads from the DUT the ActiveModeThreshold from the ICD Management cluster on EP0 and saves as active_mode_threshold | |
| 5 | | | TH checks if TCP is supported by the DUT | Set supports_tcp_dut to True if supported, otherwise, to False |
| 6 | | | TH checks if TCP is supported by the PICS | Set supports_tcp_pics to True if supported, otherwise, to False |

| 7 | C.4.3.2 | TH constructs the instance name for the DUT as the 64-bit compressed Fabric identifier, and the assigned 64-bit Node identifier, each expressed as a fixed-length sixteen-character hexadecimal string, encoded as ASCII (UTF-8) text using capital letters, separated by a hyphen. For example, a Matter Node with Matter compressed fabric identifier 2906- C908-D115-D362 and Matter Node identifier 8FC7-7724-01CD-0696 has Matter operational discovery DNS-SD instance name 2906C908D115D362- 8FC7772401CD0696. Save the operational instance name as 'instance_name'. TH constructs the instance qname as instance_name ._matter._tcp.local and saves as instance_qname | |
| 8 | C.4.3.2 | TH performs a query for the SRV record against the qname instance_qname | Verify SRV record is returned |
| 9 | C.4.3.2 | TH performs a query for the TXT record against the qname instance_qname | Verify TXT record is returned if the device supports ICD or TCP. The TXT record MAY be returned if these are not supported, but it is not required. |
| 10 | C.4.3.2 | TH performs a query for the AAAA record against the target listed in the SRV record | Verify AAAA record is returned |

| 11 | the Hostname: |
| | • The hostname must be a fixed- length twelve-character (or sixteen-character) hexadecimal string, encoded as ASCII (UTF- 8) text using capital letters. |
| | ICD TXT key: |
| | • If supports_lit is false, verify that the ICD key is NOT present in the TXT record |
| | • If supports_lit is true, verify the ICD key IS present in the TXT record, and it has the |
| | value of 0 or 1 (ASCII) SII TXT key: |
| | • If supports_icd is true and supports_lit is true, set sit_mode to true if ICD=0 |
| | otherwise set sit_mode to false • If supports_icd is false, |
| | set sit_mode to false |
| | • If sit_mode is true, verify that the SII key IS present in the TXT record |
| | • if the SII key is present, it is a decimal value with |
| | verify no leading zeros and is less than or equal to 3600000 (1h in ms) |
| | • if supports_icd is true, that the SAI key is present the TXT record |
| | verify in • If the SAI key is present, |
| | it is a decimal value with leading zeros and is less |
| | or equal to 3600000 (1h in ms) |
| | than |
| | no |
| | verify |

| 12 | C.4.3.2 | TH performs a DNS-SD browse for _I<hhhh>._sub._matter._tcp.local, where <hhhh> is the 64-bit compressed Fabric identifier, expressed as a fixed-length, sixteen-character hexadecimal string, encoded as ASCII (UTF-8) text using capital letters. | Verify DUT returns a PTR record with DNS-SD instance name set instance_name |
| 13 | C.4.3.2 | TH performs a DNS-SD browse for _matter._tcp.local | Verify DUT returns a PTR record with DNS-SD instance name set instance_name |

## Notes/Testing considerations

## TC-SC-4.4 Discovery [DUT as Controller]

## Purpose

The purpose of this test case is to verify that a Matter controller is able to discover the IP address of nodes that interacted with.

## PICS

## · MCORE.ROLE.CONTROLLER

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Nodes are joined in the same Fabric | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Matter Controller |
| 2 | TH | Matter Node that is advertising a service |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-4.6Commissioner Discovery [DUT as Commissioner]

## Purpose

The purpose of this test case is to verify that a device that support Commissioner Discovery is able to advertise its commissioner service. This feature is optional for both Commissioner and Commissionee and must be run only if the device have support for this.

## PICS

- MCORE.ROLE.COMMISSIONER
- MCORE.DD.COMM\_DISCOVERY

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Node that is scanning for DNS- SD records from DUT |

| # | Device Name | Device Description |
| 2 | DUT | Node that is advertising its services using DNS-SD |

## Device Topology

TH and DUT are in the same IP network if DUT has support.

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | DUT is instructed to start advertising its presence as a commissioner in the network | |

| | SC.DEV TYPE_S | following: - DNS-SD instance name must be 64-bit randomly selected ID expressed as a sixteen-char hex string with capital letters - service type must be _matterd._udp |
| | UBTYPE MCORE. SC.VP_K EY | |
| | MCORE. SC.DT_ KEY | |
| | SC.DN_ | |
| | | - service domain is .local. For |
| | | Unicast DNS such as used on |
| | | Thread the service domain SHALL |
| | KEY | be as configured automatically by |
| | | the Thread Border Router |
| | | - if (MCORE.SC.DEVTYPE_SUBTYPE) |
| | | present, _T<ddd> subtype is |
| | | present, <ddd> represents device |
| | | type from Data Model and must |
| | | be |
| | | represented as a variable length |
| | | decimal number in ASCII without |
| | | - target hostname is derived from |
| | | the 48bit MAC address as a twelve capital letter hex |
| | | expressed string. If the MAC is randomized |
| | | for privacy, the randomized |
| | | version must be used each |
| | | - if (MCORE.SC.VP_KEY) present, key must contain at least |
| | | Vendor |
| | | VP ID and if Product ID is present, |
| | | values must be separated by a + |
| | | - if (MCORE.SC.DT_KEY) DT key must contain the device |
| | | type identifier from Data Model |
| | | present, Device Types and must be |
| | | as a variable length decimal |
| | | number without leading zeros |
| | | encoded |
| | | ASCII |

## TC-SC-4.7 Commissioner Discovery [DUT as Commissionee]

## Purpose

The purpose of this test case is to verify that a device that is already connected to an IP network is able to discover a commissioner. This feature is optional for both Commissioner and Commissionee and must be run only if the device have support for this.

## PICS

- MCORE.ROLE.COMMISSIONEE
- MCORE.DD.COMM\_DISCOVERY

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Node that is scanning for DNS- SD records from DUT |
| 2 | TH | Node that is advertising its services using DNS-SD |

## Device Topology

TH and DUT are in the same IP network if DUT has support.

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH is instructed to start advertising its presence as a commissioner in the network | |

| | SC.DEV TYPE_S UBTYPE MCORE. SC.VP_K EY | following: - DNS-SD instance name must be 64-bit randomly selected ID |
| | MCORE. SC.DT_ KEY MCORE. SC.DN_ KEY | expressed as a sixteen-char hex string with capital letters - service type must be _matterd._udp |
| | | be as configured automatically by the Thread Border Router - if (MCORE.SC.DEVTYPE_SUBTYPE) present, _T<ddd> subtype is present, <ddd> represents device be |
| | | - service domain is .local. For |
| | | Unicast DNS such as used on |
| | | Thread the service domain SHALL |
| | | type from Data Model and must |
| | | represented as a variable length |
| | | decimal number in ASCII without |
| | | - target hostname is derived from the 48bit MAC address expressed |
| | | as a twelve capital letter hex |
| | | string. If the MAC is randomized |
| | | for privacy, the randomized |
| | | - if (MCORE.SC.VP_KEY ) |
| | | VP key must contain at least |
| | | present, Vendor ID and if Product ID is |
| | | present, values must be |
| | | - if (MCORE.SC.DT_KEY) present, |
| | | DT key must contain the device type identifier from Data Model |
| | | Device Types and must be |
| | | as a variable length decimal |
| | | number without leading zeros |
| | | encoded ASCII |

| 3 | Scan for DNS-SD commissioner advertisements from TH | DUT is able to discover TH |

## Notes/Testing considerations

## TC-SC-4.8 Compressed Fabric ID remains the same for Nodes commissioned to the same fabric [DUT as Commissioner]

## Purpose

This test case validates the following conditions:

1. Nodes on the same fabric has the same compressed fabric ID
2. Node removed from fabric and commissioned back to the same fabric has the same compressed fabric ID

## PICS

- MCORE.ROLE.COMMISSIONER

## Preconditions

| Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissioner |
| 2 | TH1 | Commissionee |
| 3 | TH2 | Commissionee |

## Device Topology

TH1, TH2 and DUT are on the same fabric

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Commission TH1 to DUT's Fabric | Extract the Compressed Fabric ID assigned from DUT to TH1 and save the value for future use |

| 2 | Commission TH2 to DUT's Fabric | • Extract the Compressed Fabric ID assigned from DUT to TH2 and save the value for future use • Verify that the value obtained from TH1 and TH2 are same |
| 3 | Send RemoveFabric from DUT to TH1 and commission DUT to TH1 again | Extract the Compressed Fabric ID assigned from DUT to TH1 and verify it is same as the value obtained in Step1 |
| 4 | Send RemoveFabric from DUT to TH2 and commission DUT to TH2 again | Extract the Compressed Fabric ID assigned from DUT to TH2 and verify it is same as the value obtained in Step2 |

## Notes/Testing considerations

## TC-SC-4.9 Operational Discovery - RIO support [DUT as Commissionee]

## Purpose

This test case validates that RIO (Route Information Options) is properly processed by Matter nodes.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Preconditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as a Commissioner, working over Ethernet or Wi-Fi transport, |
| 2 | TH_CR2 | Test harness as a Commissioner/Controller Thread 1.3 device |
| 3 | DUT_CE | DUT - Commissionee over Ethernet or Wi-Fi transport |
| 4 | BR | Thread 1.3 Border Router - This is a passive element |
| 5 | RT | Wi-Fi or Ethernet Router - This is a passive element |

## Device Topology

TH\_CR1 will use to commission DUT\_CE. TH\_CR2 is on thread network whose BR is reachable to TH\_CR1.

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## 8.3.5. TCP Test Cases

## TC-SC-8.1 Test TCP Connection Establishment with DUT

## Category

Functional conformance

## Purpose

This test case validates that a TCP-enabled Matter node can accept a TCP connection request from an initiator and establish a connection. The initiator tries to establish a session that requires a TCP connection underneath. The test validates that the underlying connection has been set up.

## PICS

## · MCORE.SC.TCP

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT is a TCP server | |
| 3 | | TH is a TCP client | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node that is a TCP client on a Matter network |
| 2 | DUT | Device acting as a node that is a TCP server on a Matter network. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-8.2 Test CASE Session allowing large payloads set up over TCP Connection with DUT.

## Category

Functional conformance

## Purpose

This test case validates that a Matter node can set up a CASE session over a TCP connection with another Matter node when both support TCP.

## PICS

## · MCORE.SC.TCP

## Preconditions

| Doc. Ref. | Condition | Notes |

| DUT and TH are on the same fabric and joined to the same Matter network | 1 |
| DUT is a TCP server | 2 |
| TH is a TCP client | 3 |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node that is a TCP client on a Matter network |
| 2 | DUT | Device acting as a node that is a TCP server on a Matter network. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-8.3 Test CASE Session becomes inactive after underlying TCP Connection with DUT is dropped.

## Category

Functional conformance

## Purpose

This test case validates that when two Matter nodes have a CASE session set up over TCP, the session would be marked inactive and deemed unusable when the underlying TCP connection is broken.

## PICS

## · MCORE.SC.TCP

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT is a TCP server | |
| 3 | | TH is a TCP client | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node that is a TCP client on a Matter network |
| 2 | DUT | Device acting as a node that is a TCP server on a Matter network. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-8.4 Test Back to back TCP Connection establishment, disconnection and reestablishment with DUT.

## Category

Functional conformance

## Purpose

This test case validates that a client is able to reconnect and establish a new CASE session over a new TCP connection after an existing session with the DUT gets disconnected.

## PICS

- MCORE.SC.TCP

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT is a TCP server | |
| 3 | | TH is a TCP client | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node that is a TCP client on a Matter network |
| 2 | DUT | Device acting as a node that is a TCP server on a Matter network. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-8.5 Test InvokeCommandRequest and CommandResponse over a TCP-based CASE session established with DUT.

## Category

Functional conformance

## Purpose

This test case validates the ability to send and receive IM Commands over a CASE session established over a TCP connection between two TCP-enabled Matter nodes.

## PICS

- MCORE.SC.TCP

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT is a TCP server | |
| 3 | | TH is a TCP client | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node that is a TCP client on a Matter network |

| # | Device Name | Device Description |
| 2 | DUT | Device acting as a node that is a TCP server on a Matter network. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-8.6 Test a Large Payload interaction over a TCP-based CASE session with DUT via a wildcard Read operation.

## Category

Functional conformance

## Purpose

This test case validates that when two Matter nodes are interacting over a CASE session set up over TCP, they can exchange messages with large payloads that exceed the 1280 bytes IPv6 MTU for MRP.

## PICS

## · MCORE.SC.TCP

## Preconditions

| Doc. Ref. | Condition | Notes |

| DUT and TH are on the same fabric and joined to the same Matter network | 1 |
| DUT is a TCP server | 2 |
| TH is a TCP client | 3 |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node that is a TCP client on a Matter network |
| 2 | DUT | Device acting as a node that is a TCP server on a Matter network. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-8.7 Test that an IM operation(possible over MRP) can use an already existing TCPbased session with DUT.

## Category

## Functional conformance

## Purpose

This test case validates that an initiator, when sending a regularly sized payload, can request for a session over either MRP or TCP as a transport, and use whichever one is available. While a MRP session is preferred, if it does not exist, a TCP based session can be used, if it exists.

## PICS

## · MCORE.SC.TCP

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT and TH are on the same fabric and joined to the same Matter network | |
| 2 | | DUT is a TCP server | |
| 3 | | TH is a TCP client | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness acting as a node that is a TCP client on a Matter network |
| 2 | DUT | Device acting as a node that is a TCP server on a Matter network. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing considerations

## TC-SC-7.1 Unique discriminators [DUT as Commissionee]

## Purpose

This test case validates that discriminators are not common between units.

## PICS

- MCORE.DD.MANUAL\_PC

## Spec References

{REF\_CODE}.5.1: Onboarding payload discriminator value

## Preconditions

Both DUTs are factory reset

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as controller |
| 2 | DUT1 | First DUT |
| 3 | DUT2 | Second DUT |

## Test Setup

## Test Procedure

| # | TestStep | Expected Outcome |

| 1 | TH establishes a PASE session to DUT1 using the provided setup code and reads the TrustedRootCertificates attribute from the operational credentials cluster over PASE | List should be empty as the DUT should be in factory reset |
| 2 | TH establishes a PASE session to DUT2 using the provided setup code and reads the TrustedRootCertificates attribute from the operational credentials cluster over PASE | List should be empty as the DUT should be in factory reset |
| 3 | TH compares the discriminators from the provided setup codes | Discriminators do not match |
| 4 | TH compares the passcodes from the provided setup codes | Passcodes do not match |

## Notes/Testing considerations

## Chapter 9. Group Communication

## 9.1. PICS Definition

This section covers the Group Communication related PICS items that are referenced in the following test cases.

## 9.1.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| GRPKEY.S | Does the device implement the Group Key Management Cluster as a server? | O | |
| GRPKEY.C | Does the device implement the Group Key Management Cluster as a client? | O | |

## 9.1.2. Server

## Features

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| GRPKEY.S.F00(CS) | Does the DUT(Server) support CacheAndSync security policy and MCSP feature? | P | |
| GRPKEY.S.F01(GCAST) | Does the DUT(Server) support groups using the GroupCast cluster? | GRPKEY.S:P, O | |

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| GRPKEY.S.A0000(Group KeyMap) | Does the device implement the GroupKeyMap attribute? | GRPKEY.S:M | |

| GRPKEY.S.A0001(Group Table) | Does the device implement the GroupTable attribute? | GRPKEY.S:M |
| GRPKEY.S.A0002(MaxG roupsPerFabric) | Does the device implement the MaxGroupsPerFabric attribute? | GRPKEY.S:M |
| GRPKEY.S.A0003(MaxG roupKeysPerFabric) | Does the device implement the MaxGroupKeysPerFabr ic attribute? | GRPKEY.S:M |
| GRPKEY.S.A0004(Group castAdoption) | Does the device implement the GroupcastAdoption attribute? | GRPKEY.S: P, GRPKEY.S.F01(GCAST) |

## Commands received

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| GRPKEY.S.C00.Rsp(KeyS etWrite) | Does the device implement the KeySetWrite command? | GRPKEY.S:M | |
| GRPKEY.S.C01.Rsp(KeyS etRead) | Does the device implement the KeySetRead command? | GRPKEY.S:M | |
| GRPKEY.S.C03.Rsp(KeyS etRemove) | Does the device implement the KeySetRemove command? | GRPKEY.S:M | |
| GRPKEY.S.C04.Rsp(KeyS etReadAllIndices) | Does the device implement the KeySetReadAllIndices command? | GRPKEY.S:M | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |

| GRPKEY.S.C02.Tx(KeySe tReadResponse) | Does the device implement transmitting of the KeySetReadResponse command? | GRPKEY.S:M |
| GRPKEY.S.C05.Tx(KeySe tReadAllIndicesRespons e) | Does the device implement transmitting of the KeySetReadAllIndicesR esponse command? | GRPKEY.S:M |

## 9.1.3. Client

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| GRPKEY.C.A0000(Group KeyMap) | Does the DUT(client) have access privileges for the GroupKeyMap attribute implemented on the server? | GRPKEY.C:O | |
| GRPKEY.C.A0001(Group KeyTable) | Does the DUT(client) have access privileges for the GroupKeyTable attribute implemented on the server? | GRPKEY.C:O | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| GRPKEY.C.C00.Tx(KeyS etWrite) | Does the DUT(Client) implement sending KeySetWrite Command? | GRPKEY.C:O | |
| GRPKEY.C.C01.Tx(KeyS etRead) | Does the DUT(Client) implement sending KeySetRead Command? | GRPKEY.C:O | |
| GRPKEY.C.C03.Tx(KeyS etRemove) | Does the DUT(Client) implement sending KeySetRemove Command? | GRPKEY.C:O | |

| GRPKEY.C.C04.Tx(KeyS etReadAllIndices) | Does the DUT(Client) implement sending KeySetReadAllIndices Command? | GRPKEY.C:O |

## 9.2. PIXIT Definition

This section covers the Group Communication related PIXIT items that are referenced in the following test cases

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PIXIT.G.ENDPOINT | Endpoint supported for Groups cluster is given by the DUT Manufacturer | M | |

## 9.3. Test Case List

| TC UUID | Test Case Name |
| TC-GRPKEY-2.1 | Attributes {DUT-Server} |
| TC-GRPKEY-2.2 | Primary functionality with DUT as Server |
| TC-SC-5.1 | Adding member to a group - TH as Admin and DUT as Group Member |
| TC-SC-5.2 | Receiving a group message - TH to DUT |
| TC-SC-5.3 | Sending a group message - TH to DUT |
| TC-GRPKEY-5.4 | Verification for KeySetReadResponse Command for CacheAndSync - PROVISIONAL |
| TC-SC-6.1 | Adding member to a group - DUT as Admin and TH as Group Member [DUT-Client] |

## 9.4. Test Cases

## 9.4.1. Server as DUT

## 9.4.2. DUT as Server

## TC-GRPKEY-2.1 Attributes [DUT-Server]

## Purpose

This test case verifies the non-global attributes of the Group Key Management Cluster server.

## PICS

- GRPKEY.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH (can be skipped if done in a preceding test).

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | Cor eSp ec- 11. 2.6. 1 | GRPKEY. S.A0000( GroupKe yMap) | TH binds GroupId 0x0103 with GroupKeySetID 0x01a3 in the GroupKeyMap attribute list on GroupKeyManagement cluster by writing the GroupKeyMap attribute with one entry as follows: List item 1: | Verify DUT responds w/ status SUCCESS(0x00) |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | Cor eSp ec- 11. 2.6. 1 | GRPKEY. S.A0000( GroupKe yMap) | TH reads GroupKeyMap Attribute from the GroupKeyManagement cluster from DUT using a fabric- filtered read. | Verify that the returned list contains a a single list item with structure fields: GroupId: 0x0103 GroupKeySetId: 0x01a3 |

## Notes/Testing Considerations

* This test checks for attribute values in basic ranges. The Resource Requirement test (TC-RR-1.1) will test that the minimum values are set correctly based on the device requirements.

## TC-GRPKEY-2.2 Primary functionality with DUT as Server

## Purpose

This test case verifies the primary functionality of the Group Key Management Cluster server. The test case verifies for the DUT response when the below commands are sent with different EpochKey,EpochKeyStartTime and GroupKeySetID values covering negative checks.

```
KeySetWrite KeySetRead KeySetRemove
```

```
KeySetReadAllIndices
```

## PICS

- GRPKEY.S

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH (can be skipped if done in a preceding test).

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| 2 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 1 • EpochKey1: d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2:184467 | Verify DUT responds w/ status SUCCESS(0x00) |

| 3 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C01.Rsp( KeySetRead),GRPK EY.S.C02.Tx(KeySe tReadResponse) | TH sends KeySetRead command to GroupKeyManagement cluster with GroupKeySetID as 0x01a | • Verify that EpochKey fields are replaced by null. • Verify that EpochStartTime values |
| | | | | GroupKeySetID: 0x01a |
| | | | | GroupKeySecurityPolicy: |
| | | | | TrustFirst (0) |
| | | | | EpochKey0: null |
| | | | | EpochStartTime0: 1 |
| | | | | EpochStartTime1: 18446744073709551613 |
| | | | | EpochKey2: null |
| | | | | EpochStartTime2: |
| | | | | 18446744073709551614 |

| 4 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 1 • EpochKey1: null • EpochStartTime1: null • EpochKey2: null • EpochStartTime2: null ◦ Note: EpochKey1 and EpochKey2 are null | Verify DUT responds w/ status SUCCESS(0x00) |

| 5 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 1 • EpochKey1: d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 18446744073709551613 • EpochKey2: null • EpochStartTime2: null ◦ Note: Only EpochKey2 is null | Verify DUT responds w/ status SUCCESS(0x00) |

| 6 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with command fields as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: null • EpochStartTime0: 1 • EpochKey1: d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2: 18446744073709551614 ◦ Note: EpochKey0 is null | Verify DUT responds w/ status INVALID_COMMAND(0x85) |

| 7 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: null • EpochKey1: d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2: 18446744073709551614 ◦ Note: EpochStartTime0 is null | Verify DUT responds w/ status INVALID_COMMAND(0x85) |

| 8 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement | Verify DUT responds w/ status INVALID_COMMAND(0x85) |
| | | | • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 | |
| | | | dadbdcdddedf • EpochStartTime0: 0 • EpochKey1: | |
| | | | d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf | |
| | | | • EpochStartTime1: 18446744073709551613 | |
| | | | • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf | |
| | | | • EpochStartTime2:184467 44073709551614 ◦ Note: EpochStartTime0 is | |
| | | | set to 0 | |

| 9 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 1 • EpochKey1: null • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2:184467 44073709551614 ◦ Note: EpochKey1 is set to null and EpochStartTime1 is not null | Verify DUT responds w/ status INVALID_COMMAND(0x85) |

| 10 | CoreSpe c- | TH sends KeySetWrite in the | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | |
| | | cluster to DUT on EP0 | cluster to DUT on EP0 | | | | | | | | | | | | | | | |
| | | GroupKeySet fields are | GroupKeySet fields are | with | with | with | with | with | with | with | with | with | with | with | with | with | with | |
| | | | as | as | as | as | as | as | as | as | as | as | as | as | as | as | as | |
| | follows: | | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | GroupKeySecurityPolicy: | |
| | | • EpochKey0: | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | |
| | | | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | |
| | | • EpochStartTime0: | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | |
| | | • EpochKey1: | • EpochKey1: | | | | | | | | | | | | | | | |
| | | | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | |
| | | dadbdcdddedf | dadbdcdddedf | | | | | | | | | | | | | | | |
| | | | null | null | null | null | null | null | null | null | null | null | null | null | null | null | null | |
| | • | | | | | | | | | | | | | | | | | |
| | | EpochStartTime1: | EpochStartTime1: | | | | | | | | | | | | | | | |
| | | • EpochKey2: | • EpochKey2: | | | | | | | | | | | | | | | |
| | | | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | |
| | | dadbdcdddedf | dadbdcdddedf | | | | | | | | | | | | | | | |
| | | • | • | | | | | | | | | | | | | | | |
| | | | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | EpochStartTime2:184467 | |
| | | 44073709551614 | 44073709551614 | | | | | | | | | | | | | | | |
| | | | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | EpochKey1 is | |
| | | | null and | null and | null and | null and | null and | null and | null and | null and | null and | null and | null and | null and | null and | null and | null and | |
| | | ◦ Note: | ◦ Note: | | | | | | | | | | | | | | | |
| | | not | not | | | | | | | | | | | | | | | |
| | | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is | EpochStartTime1 is |

| 11 | CoreSpe c- | TH sends | KeySetWrite the | Verify DUT responds w/ status | Verify DUT responds w/ status |
| | | follows: • GroupKeySetID: 0x01a • TrustFirst (0) • EpochKey0: | follows: • GroupKeySetID: 0x01a • TrustFirst (0) • EpochKey0: | | |
| | | GroupKeySecurityPolicy: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 18446744073709551613 • EpochKey1: | GroupKeySecurityPolicy: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 18446744073709551613 • EpochKey1: | | |
| | | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | | |
| | | dadbdcdddedf | dadbdcdddedf | | |
| | | • EpochStartTime1: 1 • EpochKey2: | • EpochStartTime1: 1 • EpochKey2: | | |
| | | d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf | d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf | | |
| | | • EpochStartTime2: | • EpochStartTime2: | | |
| | | 18446744073709551614 ◦ Note: | 18446744073709551614 ◦ Note: | | |
| | | EpochStartTime1 earlier | EpochStartTime1 earlier | | |
| | | than | than | | |
| | | EpochStartTime0 | EpochStartTime0 | | |

| 12 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as | Verify DUT responds w/ status INVALID_COMMAND(0x85) |
| | | | • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 1 • EpochKey1: null • EpochStartTime1: null • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2: 18446744073709551614 ◦ Note: EpochKey1 and EpochStartTime1 are null when EpochKey2 and EpochStartTime2 are not null | |

| KeySetWrite) TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 | Verify DUT responds w/ status |
| GRPKEY.S.C00.Rsp( | |
| | INVALID_COMMAND(0x85) |
| | with |
| GroupKeySet fields | |
| | are as |
| TrustFirst (0) | |
| • EpochKey0: | 1 |
| d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf | |
| • EpochStartTime0: • EpochKey1: | |
| d1d1d2d3d4d5d6d7d8d9 | |
| dadbdcdddedf | |
| • EpochStartTime1: | |
| 18446744073709551613 | |
| • EpochKey2: | |
| null | |
| • | |
| EpochStartTime2: | |
| 18446744073709551614 | |
| | is |
| ◦ Note: | |
| | and |
| EpochKey2 | |
| set to | |
| null | |
| EpochStartTime2 | |
| | is |

| 14 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 1 • EpochKey1: d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2: null ◦ Note: EpochKey2 is not null and EpochStartTime2 is null | Verify DUT responds w/ status INVALID_COMMAND(0x85) |

| CoreSpe c- | TH sends KeySetWrite in the GroupKeyManagement cluster to | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status | Verify DUT responds w/ status |
| | | DUT on EP0 with | DUT on EP0 with | DUT on EP0 with | DUT on EP0 with | DUT on EP0 with | DUT on EP0 with | DUT on EP0 with |
| | GroupKeySet | GroupKeySet | | | | | | |
| | | fields are as | fields are as | fields are as | fields are as | fields are as | fields are as | fields are as |
| | • EpochKey0: | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 | d0d1d2d3d4d5d6d7d8d9 |
| | | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf | dadbdcdddedf |
| | • EpochStartTime0: | • EpochStartTime0: | | | | | | |
| | • EpochKey1: | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 | d1d1d2d3d4d5d6d7d8d9 |
| | dadbdcdddedf | dadbdcdddedf | | | | | | |
| | EpochStartTime1: | EpochStartTime1: | | | | | | |
| | • | • | | | | | | |
| | | 18446744073709551613 | 18446744073709551613 | 18446744073709551613 | 18446744073709551613 | 18446744073709551613 | 18446744073709551613 | 18446744073709551613 |
| | • | • | | | | | | |
| | | EpochKey2: | EpochKey2: | EpochKey2: | EpochKey2: | EpochKey2: | EpochKey2: | EpochKey2: |
| | | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 | d2d1d2d3d4d5d6d7d8d9 |
| | dadbdcdddedf | dadbdcdddedf | | | | | | |
| | • | • | | | | | | |
| | EpochStartTime2: ◦ Note: | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | | EpochStartTime2 | EpochStartTime2 | EpochStartTime2 | EpochStartTime2 | EpochStartTime2 | EpochStartTime2 | EpochStartTime2 |
| | | is | is | is | is | is | is | is |
| | earlier | earlier | | | | | | |
| | | than | than | than | than | than | than | than |
| | EpochStartTime1 | EpochStartTime1 | | | | | | |

| 16 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields are as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0 • EpochStartTime0: 1 • EpochKey1: d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2: 1 ◦ Note1: Repeat the step by sending EpochKey1 and EpochKey2 with 1 byte value (< 16 | Verify DUT responds w/ status CONSTRAINT_ERROR(0x87) |
| 16a | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | Repeat step 16 by sending KeySetWrite Command with EpochKey0, EpochKey1 and EpochKey2 having 15 bytes value (< 16 byte) | Verify DUT responds w/ status CONSTRAINT_ERROR(0x87) |
| 16b | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | Repeat step 16 by sending KeySetWrite Command with EpochKey0, EpochKey1 and EpochKey2 having 17 bytes value (> 16 bytes) | Verify DUT responds w/ status CONSTRAINT_ERROR(0x87) |

| 17 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C00.Rsp( KeySetWrite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT on EP0 with GroupKeySet fields as follows: • GroupKeySetID: 0x01a • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d3d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 1 • EpochKey1: d4d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 17446744073709551613 • EpochKey2: d5d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2: 17446744073709551614 ◦ Note: KeySetWrite command is sent with different EpochKeys,EpochSta rtTime1 and EpochStartTime2 values | Verify DUT responds w/ status SUCCESS(0x00) |

| 18 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C01.Rsp( KeySetRead) | TH sends KeySetRead command to GroupKeyManagement cluster with GroupKeySetID as 0x01a | • Verify that EpochStartTime values matches the values sent in the previous step • Verify that the DUT sends a KeySetReadResponse with the GroupKeySet having the following fields: GroupKeySetID: 0x01a GroupKeySecurityPolicy: TrustFirst (0) EpochKey0: null EpochStartTime0: 1 EpochKey1: null EpochStartTime1: 17446744073709551613 EpochKey2: null |
| 20 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C03.Rsp( KeySetRemove) | TH removes the Group key set that was added by sending a KeySetRemove command to the GroupKeyManagement cluster with the GroupKeySetID field set to 0x01a. | Verify DUT responds w/ status SUCCESS(0x00) |

| 24 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C03.Rsp( KeySetRemove) | TH removes the Group key set that was added by sending a KeySetRemove command to the GroupKeyManagement cluster with the GroupKeySetID field set to 0x0 | Verify DUT responds w/ status INVALID_COMMAND(0x85) |
| 25 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C03.Rsp( KeySetRemove) | TH removes the Group key set that was added by sending a KeySetRemove command to the GroupKeyManagement cluster with the GroupKeySetID field set to 0x01b that does not exist in the GroupKeyMap attribute list. | Verify DUT responds w/ status NOT_FOUND(0x8b) |
| 26 | CoreSpe c- 11.2.5.1. | GRPKEY.S.C03.Rsp( KeySetRemove) | TH removes all the existing GroupKeySetID that were added in Step 21 by sending a KeySetRemove command starting from GroupKeySetID 1 to the GroupKeyManagement cluster | Verify DUT responds w/ status SUCCESS(0x00) |

## TC-SC-5.1 Adding member to a group - TH as Admin and DUT as Group Member

## Purpose

To verify that GroupKeySets and Groups can be added and removed from DUT

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | CoreSpe c-5.5 | DUT is commissioned by TH | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness |
| 2 | DUT | Device Under Test |

## Device Topology

DUT is commissioned to a single fabric by TH.

## Test Setup

## Test Procedure

| # | Ref | PIC S | Test Step | Expected Outcome |
| 0a | | | Commission DUT to TH if not already done | |
| 0b | | | Repeat the remaining steps once for each endpoint with a groups cluster: | |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 1 | CoreSpe c- 9.10.5.3 | | TH writes the ACL attribute in the Access Control cluster to add Operate privileges for group 0x0103 and maintain the current administrative privileges for the TH. The following access control list shall be used: • List item 1 (TH admin): ◦ Privilege: Administer (5) ◦ AuthMode: CASE (2) ◦ Subjects: TH node id ([ N1 ]) ◦ Targets: all (null) • List item 2 (group operate access): ◦ Privilege: Operate (3) ◦ AuthMode: Group (3) ◦ Subjects: group 0x0103 ([0x0103]) ◦ Targets: all (null) | Verify DUT responds w/ status SUCCESS(0x00) |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 2a | CoreSpe c- 11.2.5.1. | GR PK EY. S.C 00. Rsp (Ke ySe tWr ite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT using a key that is NOT installed on the TH. This is intended to test that the key set is correctly updated in the next step. GroupKeySet fields are as follows: • GroupKeySetID: 0x01a3 • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: 00000000000000000000000000000 001 • EpochStartTime0: 111 • EpochKey1: 00000000000000000000000000000 002 • EpochStartTime1: 222 • EpochKey2: 00000000000000000000000000000 003 • EpochStartTime2: 333 | Verify DUT responds w/ status SUCCESS(0x00) |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 2b | CoreSpe c- 11.2.5.1. | GR PK EY. S.C 00. Rsp (Ke ySe tWr ite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT using a key that is pre-installed on the TH. GroupKeySet fields are as follows: • GroupKeySetID: 0x01a3 • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9dadbdcdd dedf • EpochStartTime0: 1 • EpochKey1: d1d1d2d3d4d5d6d7d8d9dadbdcdd dedf • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9dadbdcdd dedf | Verify DUT responds w/ status SUCCESS(0x00) |
| 3 | CoreSpe c- 11.2.7.2 | GR PK EY. S.A 000 0(G rou pKe yM ap) | 18446744073709551614 If Groupcast cluster is enabled on the RootNode endpoint of the DUT, skip to step 7. Otherwise, TH binds GroupId 0x0103 with GroupKeySetID 0x01a3 in the GroupKeyMap attribute list on GroupKeyManagement cluster by writing the GroupKeyMap attribute with one entry as follows: • List item 1: ◦ GroupId: 0x0103 ◦ GroupKeySetId: 0x01a3 | Verify DUT responds w/ status SUCCESS(0x00) |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 4 | appclust ers- 1.3.7.5 | G.S. C04 .Rs p(R em ove All Gro ups | TH sends RemoveAllGroups command to the DUT on the current endpoint under test | Verify that the DUT sends SUCCESS response |
| 5 | appclust ers- 1.3.6.1 | G.S. C00 .Rs p(A dd Gro up) | TH sends AddGroup Command to DUT on the current endpoint under test with the the following settings • GroupID: 0x0103 • GroupName: "Test Group" | Verify that the DUT sends a AddGroupResponse with the Status set to SUCCESS and the GroupID set to 0x0103 |
| 6a | appclust ers- 1.3.7.2 | G.S. F00 (GN ),G. S.C 01. Rsp (Vie wG rou p) | TH sends ViewGroup command with the GroupID to the Group cluster on the DUT on the current endpoint under test | Verify DUT sends a ViewGroupResponse command with • Status: SUCCESS • GroupID: 0x0103 • GroupName: "Test Group" |
| 6b | appclust ers- 1.3.7.2 | !G.S .F0 0(G N), G.S. C01 .Rs p(V iew | TH sends ViewGroup command with the GroupID to the Group cluster on the DUT on the current endpoint under test | Verify DUT sends a ViewGroupResponse command with • Status: SUCCESS • GroupID: 0x0103 • GroupName: "" |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 7 | | | If Groupcast cluster is NOT enabled on the RootNode endpoint of the DUT, skip to step 10. Otherwise, TH sends a LeaveGroup command to the Groupcast cluster on the DUT on EP0 with GroupID 0 (leave all groups) | Verify DUT responds w/ status SUCCESS(0x00) |
| 8 | | | TH sends the Groupcast cluster's JoinGroup command on the DUT on EP0 with the following fields: * GroupID: 0x0103 * Endpoints: [Any endpoint from the list of endpoints in the PartsList attribute] If the Groupcast listener feature is enabled else provide an empty list []. * KeySetID: 0x01a3 | Verify DUT responds w/ status SUCCESS(0x00) |
| 10 | CoreSpe c- 11.2.5.2 | | TH sends KeySetRead command to GroupKeyManagement cluster with GroupKeySetID as 0x01a3 | Verify that the DUT sends a KeySetReadResponse with the GroupKeySet having the following fields: • GroupKeySetID: 0x01a3 • GroupKeySecurityPolicy: TrustFirst (0) |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 11 | | GR PK EY. S.A 000 0(G rou pKe yM | TH reads GroupKeyMap Attribute from the GroupKeyManagement cluster from DUT | Verify that the returned list contains a a single list item with structure fields • GroupId: 0x0103 • GroupKeySetId: 0x01a3 |
| 12a | CoreSpe c- 11.2.7.3 | G.S. F00 (GN ),G RP KE Y.S. A00 01( Gro upT abl e) | TH reads GroupTable attribute from GroupKeyManagement cluster on DUT using a fabric-filtered read. | Verify the returned list has a single item containing a GroupInfoMapStruct with: • GroupId: 0x0103 • Endpoints: [PIXIT.G.ENDPOINT] • GroupName: "Test Group" |
| 12b | CoreSpe c- 11.2.7.3 | !G.S .F0 0(G N), GR PK EY. S.A 000 1(G rou pTa | TH reads GroupTable attribute from GroupKeyManagement cluster on DUT using a fabric-filtered read. | Verify the returned list has a single item containing a GroupInfoMapStruct with: • GroupId: 0x0103 • Endpoints: [PIXIT.G.ENDPOINT] • GroupName: "" |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 13 | CoreSpe c- 11.2.9.4 | GR PK EY. S.C 03. Rsp (Ke ySe tRe mo ve) | TH removes the Group key set that was added by sending a KeySetRemove command to the GroupKeyManagement cluster with the GroupKeySetID field set to 0x01a3 | Verify that the DUT sends SUCCESS response |
| 14 | CoreSpe c- 11.2.9.4 | GR PK EY. S.A 000 0(G rou pKe yM ap) | TH verifies that the key set removal in step 13 also removed the corresponding entries in the GroupKeyMap by Reading the GroupKeyMap attribute from the GroupKeyManagement cluster using a fabric-filtered read. | Verify that the returned list contains no items |
| 15 | appclust ers- 1.3.7.5 | G.S. C04 .Rs p(R em ove All Gro ups ) | TH cleans up the groups by sending the RemoveAllGroups command to the DUT on PIXIT.G.ENDPOINT | Verify that the DUT sends SUCCESS response |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 17 | CoreSpe c- 9.10.5.3 | | TH writes the ACL attribute in the Access Control cluster to remove Operate privileges for group 0x0103 and maintain the current administrative privileges for the TH. The following access control list shall be used: • List item 1 (TH admin): ◦ Privilege: Administer (5) ◦ AuthMode: CASE (2) ◦ Subjects: TH node id ([ N1 ]) ◦ Targets: all (null) | Verify DUT responds w/ status SUCCESS(0x00) |

## TC-SC-5.2 Receiving a group message - TH to DUT

## Purpose

To verify that the DUT can receive group message sent by TH.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | CoreSpe c-5.5 | DUT and TH are commissioned | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness with node ID N1 |
| 2 | DUT | DUT |

## Device Topology

TH and DUT are on the same fabric

## Test Setup

| # | Ref | PIC S | Test Step | Expected Outcome |
| 0a | | | Commission DUT to TH if not already done | |
| 0b | | | Repeat the remaining steps once for each endpoint with a groups cluster: | |
| 1 | CoreSpe c- 9.10.5.3 | | TH writes the ACL attribute in the Access Control cluster to add Manage privileges for group 0x0103 and maintain the current administrative privileges for the TH. The following access control list shall be used: • List item 1 (TH admin): ◦ Privilege: Administer (5) ◦ AuthMode: CASE (2) ◦ Subjects: TH node id ([ N1 ]) ◦ Targets: all (null) • List item 2 (group operate access): ◦ Privilege: Manage (4) ◦ AuthMode: Group (3) ◦ Subjects: group 0x0103 ([0x0103]) ◦ Targets: all (null) | Verify that the DUT sends SUCCESS response. |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 2 | CoreSpe c- 11.2.5.1. | GR PK EY. S.C 00. Rsp (Ke ySe tWr ite) | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT using a key that is pre-installed on the TH. GroupKeySet fields are as follows: • GroupKeySetID: 0x01a3 • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9dadbdcdd dedf • EpochStartTime0:1 • EpochKey1: d1d1d2d3d4d5d6d7d8d9dadbdcdd dedf • EpochStartTime1: 18446744073709551613 • EpochKey2: d2d1d2d3d4d5d6d7d8d9dadbdcdd dedf • EpochStartTime2: | Verify DUT responds w/ status SUCCESS(0x00) |
| 3 | CoreSpe c- 11.2.7.2 | GR PK EY. S.A 000 0(G rou pKe yM ap) | 18446744073709551614 if Groupcast cluster is enabled on the RootNode endpoint of the DUT, skip to step 12. Otherwise, TH binds GroupId 0x0103 and 0x0101 with GroupKeySetID 0x01a3 in the GroupKeyMap attribute list on GroupKeyManagement cluster by writing the GroupKeyMap attribute with 2 entries as follows: • List item 1: ◦ GroupId: 0x0103 ◦ GroupKeySetId: 0x01a3 • List item 2: ◦ GroupId: 0x0101 | Verify that the DUT sends SUCCESS response. |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 4 | appclust ers- 1.3.7.5 | G.S. C04 .Rs p(R em ove All Gro ups | TH cleans up the groups by sending the RemoveAllGroups command to the DUT on the current endpoint under test | Verify DUT responds w/ status SUCCESS(0x00) |
| 5 | appclust ers- 1.3.6.1 | G.S. C00 .Rs p(A dd Gro up) | TH sends AddGroup Command to DUT on the current endpoint under test with the the following settings • GroupID: 0x0103 • GroupName: "Test Group 0103" | Verify that the DUT sends a AddGroupResponse with the Status set to SUCCESS and the GroupID set to 0x0103 |
| 6 | appclust ers- 1.3.6.1 | G.S. C00 .Rs p(A dd Gro up) | TH sends a AddGroup Command to the Groups cluster with the GroupID field set to 0x0101 and the GroupName set to an "Test Group 0101". The command is sent as a group command using GroupID 0x0103 | |
| 7 | appclust ers- 1.3.7.2 | G.S. F00 (GN ), G.S. C01 .Rs p(V iew Gro | TH sends a ViewGroup Command to the Groups cluster on the current endpoint under test over CASE with the GroupID set to 0x0101 to confirm that the AddGroup command from step 6 was successful | Verify DUT sends a ViewGroupResponse command with * Status: SUCCESS * GroupID: 0x0101 * GroupName: "Test Group 0101" |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 8 | appclust ers- 1.3.7.2 | !G.S .F0 0(G N), G.S. C01 .Rs p(V iew Gro up) | TH sends a ViewGroup Command to the Groups cluster on the current endpoint under test over CASE with the GroupID set to 0x0101 to confirm that the AddGroup command from step 6 was successful | Verify DUT sends a ViewGroupResponse command with * Status: SUCCESS * GroupID: 0x0101 * GroupName: "" |
| 9 | appclust ers- 1.3.6.1 | G.S. C03 .Rs p(R em ove Gro up) | TH sends a RemoveGroup Command to the Groups cluster with the GroupID field set to 0x0101. The command is sent as a group command using GroupID 0x0103 | |
| 10 | appclust ers- 1.3.7.2 | G.S. C01 .Rs p(V iew Gro up) | TH sends a ViewGroup Command to the Groups cluster on the current endpoint under test over CASE with the GroupID set to 0x0101 to confirm that the RemoveGroup command from step 9 was successful | Verify DUT responds w/ status NOT_FOUND(0x8b) |
| 11 | appclust ers- 1.3.7.5 | G.S. C04 .Rs p(R em ove All Gro ups ) | TH cleans up the groups by sending the RemoveAllGroups command to the DUT on PIXIT.G.ENDPOINT | Verify that the DUT sends SUCCESS response |
| 12 | | | If Groupcast cluster is NOT enabled on the RootNode endpoint of the DUT or its Listener feature is disabled, skip to step 17. Otherwise, TH sends the Groupcast cluster's LeaveGroup command on the DUT on EP0 with GroupID 0 (leave all groups) | Verify DUT responds w/ status SUCCESS(0x00) |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 13 | | | TH sends the Groupcast cluster's JoinGroup command on the DUT on EP0 with the following fields: * GroupID: 0x0103 * Endpoints: [Any endpoint from the list of endpoints in the PartsList attribute]. * KeySetID: 0x01a3 | Verify DUT responds w/ status SUCCESS(0x00) |
| 14 | | | TH reads the Groupcast 'membership' attribute on the DUT on EP0 | Validate that the Membership attribute contains the entry for the joined GroupID 0x0103, with KeySetID 0x01a3 and the endpoint List Provided. |
| 15 | | | TH sends a command from a cluster enabled on the Endpoint provided in step 13 to DUT. The command is sent as a group command using GroupID 0x0103. The command selected SHALL be a command that will modify an attribute so that the TH can validate the message was received by DUT. For example, the OnOff cluster's On command can be used to set the OnOff attribute to ON. | |
| 17 | CoreSpe c- | GR PK | TH removes the Group key set that was added by sending a | Verify that the DUT sends SUCCESS response |
| | | Rsp | | |
| | | (Ke | | |
| | | ySe | | |
| | | tRe | | |
| | | mo | | |
| | | ve) | | |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 18 | CoreSpe c- 9.10.5.3 | | TH writes the ACL attribute in the Access Control cluster to remove Manage privileges for group 0x0103 and maintain the current administrative privileges for the TH. The following access control list shall be used: • List item 1 (TH admin): ◦ Privilege: Administer (5) ◦ AuthMode: CASE (2) ◦ Subjects: TH node id ([ N1 ]) ◦ Targets: all (null) | Verify that the DUT sends SUCCESS response. |

## TC-SC-5.3 Sending a group message - DUT to TH

## Purpose

To verify that the DUT can send group message to TH and validate the Group Message received by TH.

## PICS

- MCORE.ROLE.COMMISSIONER
- GRPKEY.C

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | CoreSpe c-5.5 | DUT and TH are commissioned. | |
| 2 | | DUT supports Groups Cluster | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as server |
| 2 | DUT | DUT as client |

## Device Topology

TH and DUT are on the same fabric

## Test Procedure

| # | Ref | PIC S | Test Step | Expected Outcome |
| 1a | | | TH should have the ACL entry with the AuthMode as Group by DUT | |
| 3 | CoreSpe c- 11.2.5.1 | GR PK EY. C.A 000 0(G rou pKe yM ap) | If Groupcast cluster is enabled on the RootNode endpoint of the DUT, skip to step 6. Otherwise, DUT binds GroupId with GroupKeySetID in the GroupKeyMap attribute list on GroupKeyManagement cluster | Test Harness receives the binding of GroupKeySetID with the GroupID from DUT |
| 4 | appclust ers- 1.3.6.1 | G.C. C00 .Tx( Ad dGr oup ) | DUT sends AddGroup Command to DUT on EP0 with the the following settings • GroupID: 1 • GroupName: "GroupOne" | Test Harness receives the AddGroup command from the DUT |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 5 | appclust ers- 1.3.6.1 | G.C. C00 .Tx( Ad dGr oup ) | DUT sends a AddGroup Command to the Groups cluster with the GroupID field set to 2 and the GroupName set to "GroupTwo". The command is sent as a group command using GroupID 1 | Validate the group message received from DUT: • Verify that the IPv6 Destination Multicast address follows the format "FF35:0040:FD<Fabric ID>00:<Group ID> • Verify the UDP port is 5540 • Verify the DSIZ flag is set to group • Verify the Destination Node ID matches the GroupID of 1 |
| 6 | | | If Groupcast cluster is NOT enabled on the RootNode endpoint of the DUT or its Sender feature is disabled, skip remaining steps. Otherwise, DUT sends the Groupcast JoinGroup command on the TH on EP0 with the following fields: * GroupID: 1 * Endpoints: [Any endpoint from the list of endpoints in the TH's PartsList attribute]. * KeySetID: 1 | Verify TH responds w/ status SUCCESS(0x00) |

## Notes/Testing considerations

In the above test case Groups cluster is used for testing the multicast message. Any other cluster like Identify can also be used depending on the DUT capability.

## TC-GRPKEY-5.4 Verification for KeySetReadResponse Command for CacheAndSync PROVISIONAL

## Purpose

To verify that the DUT sends the correct KeySetReadResponse command for CacheAndSync

## PICS

- GRPKEY.S

| # | Doc. Ref. | Condition | Notes |
| 1 | CoreSpe c-5.5 | Group Member is commissioned with Admin | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as Admin |
| 2 | DUT | Device Under Test as GM-Group Member |

## Device Topology

DUT and Admin are on the same fabric.

## Test Setup

## Test Procedure

| # | Ref | PIC | Test Step | Expected Outcome |
| 1 | CoreSpe c- 11.2.5.1. | S !GR PK EY. S.F 00( CS), GR PK EY. S.C 00. Rsp (Ke ySe tWr ite) | • Admin sends KeySetWrite command by setting GroupKeySecurityPolicy to CacheAndSync to GroupKeyManagement cluster on the DUT • Note: KeySetWrite command is sent by setting the following fields to the corresponding values. Values given below are for reference purpose. 1. groupKeySetID: 0x01a3 2. groupKeySecurityPolicy: CacheAndSync (1) 3. epochKey0: d0d1d2d3d4d5d6d7d8d9dadbd cdddedf 4. epochStartTime0: 1 5. epochKey1: d1d1d2d3d4d5d6d7d8d9dadbd cdddedf 6. epochStartTime1: 2220001 7. epochKey2: d2d1d2d3d4d5d6d7d8d9dadbd cdddedf 8. epochStartTime2: 2220002 | Verify that the DUT sends INVALID_COMMAND response as CacheAndSync is not supported. |

| # | Ref | PIC S | Test Step | Expected Outcome | Expected Outcome | Expected Outcome | Expected Outcome |
| 2 | CoreSpe c- 11.2.5.1. | GR PK EY. S.F 00( CS) ,GR PK EY. S.C 00. Rsp (Ke ySe | Admin sends KeySetWrite command by setting the values as given in Step 1 | Verify that response supported | the DUT as | sends CacheAndSync | SUCCESS is |
| 3 | | GR PK EY. S.F 00( CS), GR PK EY. S.A 000 0(G rou pKe yM ap) | Admin maps GroupId 0x0103 with GroupKeySetID 0x01a3 in the GroupKeyMap attribute list on GroupKeyManagement cluster on the DUT | Verify DUT SUCCESS(0x00) | responds | w/ | status |

| # | Ref | PIC S | Test Step | Expected Outcome |
| 4 | CoreSpe c- 11.2.6.2 | GR PK EY. S.F 00( CS), GR PK EY. S.C 01. Rsp (Ke ySe tRe | Admin sends KeySetRead Command to DUT | • Verify that the DUT sends a KeySetReadResponse Command with the GroupKeySetStructure. • Verify that GroupKeySetStructure has GroupKeySecurityPolicy value set to CacheAndSync (1) |

## 9.4.3. Client as DUT

[TC-SC-6.1] Adding member to a group - DUT as Admin and TH as Group Member [DUT-Client]

## Purpose

To verify that the TH can be added to a group by DUT

## PICS

- MCORE.ROLE.COMMISSIONER
- GRPKEY.C

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | CoreSpe c-5.5 | Group Member is commissioned with Admin | |
| 2 | | DUT supports Groups Cluster | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as GM-Group Member |
| 2 | DUT | Device Under Test as Admin |

DUT and TH are on the same fabric.

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | TH should have the ACL entry with the AuthMode as Group by DUT | |
| 1b | | | • DUT generates a random key and EpochKey0 assigned to GroupKeySetID 1. • Admin sets GroupKeySecurityPolicy = TrustFirst (0) EpochStartTime0 = 1 | |
| 3 | CoreSpe c- 11.2.5.1 | GRPKEY.C.A0000( GroupKeyMap) | If Groupcast cluster is enabled on the RootNode endpoint of the TH, skip to step 6. Otherwise, DUT binds GroupID 1 with GroupKeySetID 1 in the GroupKeyMap attribute list on GroupKeyManagement cluster | Test Harness receives the binding of GroupKeySetID 1 with the GroupID 1 from DUT |
| 4 | appclust ers- 1.3.6.1 | G.C.C00.Tx(AddGr oup) | DUT sends AddGroup Command to TH on EP0 with the GroupID 1 and GroupName "GroupOne" | Test Harness receives the AddGroup command from the DUT |

| # | Ref | PICS | Test Step | Expected Outcome |
| 5 | appclust ers- 1.3.7.2 | G.C.C01.Tx(ViewGr oup) | DUT sends ViewGroup command with the GroupID 1 to the Group cluster on the TH on EP0 | Test Harness receives the ViewGroup command from the DUT and sends a ViewGroupResponse command with the Status set to SUCCESS and the GroupID set to 1 and the GroupName set to either "GroupOne" when the TH supports GroupNames feature or empty string when the TH does not support GroupNames feature. |
| 6 | | | If Groupcast cluster is not enabled on the RootNode endpoint of the TH, skip to step 8. Otherwise, DUT sends Groupcast JoinGroup command to the TH on EP0 with the following fields: * GroupID: 1 * Endpoints: [Any endpoint from the list of endpoints in the TH's PartsList attribute]. * KeySetID: 1 | Verify TH responds w/ status SUCCESS(0x00) |
| 7 | | | DUT reads the Groupcast 'membership' attribute on the TH on EP0 | Test Harness receives the Membership attribute read from DUT |
| 8 | CoreSpe c- 11.2.5.2 | GRPKEY.C.C01.Tx( KeySetRead) | DUT sends KeySetRead Command to TH | Test Harness receives the KeySetRead command from the DUT |
| 9 | CoreSpe c- 11.2.5.2 | GRPKEY.C.C03.Tx( KeySetRemove) | DUT sends KeySetRemove Command to TH | Test Harness receives the KeySetRemove command from the DUT |
| 10 | CoreSpe c- 11.2.5.2 | GRPKEY.C.C04.Tx( KeySetReadAllIndi ces) | DUT sends KeySetReadAllIndices Command to TH | Test Harness receives the KeySetReadAllIndices command from the DUT |

## Chapter 10. Device Attestation Test Plan

## 10.1. Test Case List

| TC UUID | Test Case Name |
| TC-DA-1.1 | The NOC SHALL be wiped on Factory Reset [DUT-Commissionee] |
| TC-DA-1.2 | Device Attestation Request Validation [DUT- Commissionee] |
| TC-DA-1.3 | Device Attestation Request Validation [DUT- Commissioner] |
| TC-DA-1.4 | Device Attestation Request Validation-Error Scenario [DUT-Commissioner] |
| TC-DA-1.5 | NOCSR Procedure Validation [DUT- Commissionee] |
| TC-DA-1.6 | NOCSR Procedure Validation [DUT- Commissioner] - PROVISIONAL |
| TC-DA-1.7 | Validate CertificateChainRequest [DUT- Commissionee] |
| TC-DA-1.8 | Device Attestation Request Validation-Success Scenario [DUT-Commissioner] |
| TC-DA-1.9 | Device Attestation Revocation [DUT- Commissioner] |

## 10.2. Test Cases

## 10.2.1. Server as DUT

## TC-DA-1.1 The NOC SHALL be wiped on Factory Reset [DUT - Commissionee]

## Purpose

This test case validates the following condition:

1. NOCs attribute gets deleted on the DUT after factory reset.

## PICS

- MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT Commissioned to TH1's fabric | |
| 2 | | DUT Supports Factory Reset Method | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |
| 3 | TH2 | Commissioner |

## Device Topology

DUT will be commissioned in a Fabric 1 with TH1 and a Fabric 2 with TH2. These are separate fabrics.

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Commission DUT to TH1's Fabric | |
| 3 | | | • Factory reset DUT and perform the necessary actions to put the DUT into a commissionable state | |
| 4 | | | Commission DUT to TH2's Fabric | |

## TC-DA-1.2 Device Attestation Request Validation [DUT - Commissionee]

## Purpose

To verify the following during the Device Attestation procedure:

1. DUT responds with correct AttestationResponse upon receiving AttestationRequest Command with AttestationNonce from TH1
2. DUT-generated AttestationResponse Information is valid and sent through AttestationResponse Command to TH1
3. DUT does not accept invalid AttestationNonce sent by TH1

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |

## Spec References

C.11.18.6.1, C.11.18.6.2 -AttestationRequest, AttestationResponse C.11.18.6.3, C.11.18.6.4 -CertificateChainRequest, CertificateChainResponse C.6.3.1 - Certification Declaration format

| # | TestStep | Expected Outcome |
| 0 | Commission DUT if not done | |
| 1 | TH1 generates 32-byte AttestationNonce and saves as `nonce | |
| 2 | TH1 sends AttestationRequest Command to the DUT with AttestationNonce set to nonce | Verify AttestationResponse is received |
| 3a | TH1 sends CertificateChainRequest Command with CertificateType field set to DACCertificate (1) to DUT to obtain DAC | DUT responds with CertificateChainResponse the DAC certificate in X.509v3 format with size ⇐ 600 bytes |
| 3b | TH1 sends CertificateChainRequest Command with CertificateType field set to PAICertificate (2) to DUT to obtain PAI | DUT responds with CertificateChainResponse the PAI certificate in X.509v3 format with size ⇐ 600 bytes |
| 4a | TH1 Reads the VendorID attribute of the Basic Information cluster and saves it as basic_info_vendor_id | |
| 4b | TH1 Reads the ProductID attribute of the Basic Information cluster and saves it as basic_info_product_id | |
| 5 | Extract the attestation_elements_message structure fields from the AttestationResponse | |

| 8 | If the Certification Declaration has authorized_paa_list, check that the authority_key_id extension of the PAI matches one found in the authorized_paa_list | PAA from PAI authority_key_id extension matches one found in authorized_paa_list |

| 9 | Verify that the certification_declaration CMS enveloped can be verified with Certification Declaration public key. For official CDs the signer must be one of the well-known CSA CD signing keys. For provisional CDs, the signer must be one of the well-known CSA CD signing keys unless the override_provisional_cd_check_warning flag is set to acknowledge the use of a provisional CD that cannot be used in production devices.For test and development CDs, the signer certificates may be one of the development certificates or can be provided by the tester. | Signature verification passes |
| 10 | Verify attestation_nonce | • attestation_nonce is present in the attestation_elements_message structure • attestation_nonce value matches the AttestationNonce field value sent in the AttestationRequest Command sent by the commissioner • attestation_nonce is a 32 byte-long octet string |
| 11 | If firmware_information is present, verify firmware information type | firmware_information is an octet string |

## TC-DA-1.3 Device Attestation Request Validation [DUT - Commissioner]

## Purpose

Validate correct handling of a well-formed AttestationResponse Command by the DUT, including all the following fields being valid:

- AttestationInformation
- AttestationNonce properly repeated
- certification\_declaration present
- firmware\_information validated if present
- AttestationSignature value

## PICS

## · MCORE.ROLE.COMMISSIONER

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissioner |
| 2 | TH1 | Commissionee |

## Device Topology

## Test Setup

| # | Condition | Notes |
| 1 | Manual intervention would be required during Device Attestation Test Procedure | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Start the commissioning process of TH1 on DUT | |
| 6 | | | | Verify that DUT Completes the commissioning process successfully |
| 7 | | | Factory Reset TH1 so that it is commissionable again | |

## TC-DA-1.4 Device Attestation Request Validation-Error Scenario [DUT-Commissioner]

## Purpose

Validate the handling of an invalid AttestationResponse received by the DUT from TH during commissioning process and ensure the DUT responds with correct warning message.

## PICS

## · MCORE.ROLE.COMMISSIONER

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissioner |
| 2 | TH | Commissionee |

## Test Setup

| # | Condition | Notes |
| 1 | Manual intervention would be required during Device Attestation Test Procedure | |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Start the commissioning process of TH on DUT | |
| 4 | | | • TH responds to the DUT with an invalid AttestationRespons e Command by setting the following error condition: 1. Commissionee is not yet certified | Verify that the DUT indicates that the device is not genuine, or otherwise indicates a failure of device attestation, within its error handling APIs or user interface. |
| 5 | | | Factory Reset TH so that it is commissionable again | |

## Certificates for TC-DA-1.4

| # | Cert Description | Example certs |
| 3 | CD Test Vector: The authorized_paa_list contains ten PAAs none of which is a valid PAA authorized to sign the PAI. | struct_cd_authorized_paa_list_c ount10_invalid (pid=32768) |
| 4 | CD Test Vector: The authorized_paa_list contains three PAAs none of which is a valid PAA authorized to sign the PAI. | struct_cd_authorized_paa_list_c ount3_invalid (pid=32768) |
| 10 | CD Test Vector: Invalid CMS eContentType is set to Microsoft Authenticode [MSAC] OID = { 1.3.6.1.4.1.311.2.1.4 }. | struct_cd_cms_econtent_type_m sac (pid=32768) |

| 15 | CD Test Vector: The dac_origin_vendor_id and dac_origin_product_id fields present and the PID value doesn't match the PID found in the DAC Subject DN. | struct_cd_dac_origin_vid_pid_pr esent_pid_mismatch (pid=32768) |
| 16 | CD Test Vector: The dac_origin_vendor_id and dac_origin_product_id fields present and the VID value doesn't match the VID found in the DAC Subject DN. | struct_cd_dac_origin_vid_pid_pr esent_vid_mismatch (pid=32768) |

| 29 | CD Test Vector: The subjectKeyIdentifier contains invalid SKID of a certificate unknown by Zigbee Alliance. | struct_cd_signer_info_skid_inva lid (pid=32768) |
| 34 | DAC Test Vector: Invalid certificate version field set to v2(1) | struct_dac_cert_version_v2 (pid=32768) |
| 35 | DAC Test Vector: Certificate doesn't include Authority Key ID (AKID) extension | struct_dac_ext_akid_missing (pid=32768) |
| 36 | DAC Test Vector: Certificate Basic Constraint extension CA field is missing | struct_dac_ext_basic_ca_missing (pid=32768) |
| 37 | DAC Test Vector: Certificate Basic Constraint extension CA field is wrong (TRUE for DAC and FALSE for PAI) | struct_dac_ext_basic_ca_wrong (pid=32768) |
| 38 | DAC Test Vector: Certificate Basic Constraint extension critical field is missing | struct_dac_ext_basic_critical_mi ssing (pid=32768) |

| 39 | DAC Test Vector: Certificate Basic Constraint extension critical field is set as 'non- critical' | struct_dac_ext_basic_critical_wr ong (pid=32768) |
| 40 | DAC Test Vector: Certificate doesn't include Basic Constraint extension | struct_dac_ext_basic_missing (pid=32768) |
| 41 | DAC Test Vector: Certificate Basic Constraint extension PathLen field set to 0 | struct_dac_ext_basic_pathlen0 (pid=32768) |
| 42 | DAC Test Vector: Certificate Basic Constraint extension PathLen field set to 1 | struct_dac_ext_basic_pathlen1 (pid=32768) |
| 43 | DAC Test Vector: Certificate Basic Constraint extension PathLen field set to 2 | struct_dac_ext_basic_pathlen2 (pid=32768) |
| 44 | DAC Test Vector: Certificate Basic Constraint extension PathLen field presence is wrong (present for DAC not present for PAI) | struct_dac_ext_basic_pathlen_pr esence_wrong (pid=32768) |
| 45 | DAC Test Vector: Certificate Key Usage extension critical field is missing | struct_dac_ext_key_usage_critic al_missing (pid=32768) |
| 46 | DAC Test Vector: Certificate Key Usage extension critical field is set as 'non-critical' | struct_dac_ext_key_usage_critic al_wrong (pid=32768) |
| 47 | DAC Test Vector: Certificate Key Usage extension cRLSign field is wrong (present for DAC and not present for PAI) | struct_dac_ext_key_usage_crl_si gn_wrong (pid=32768) |
| 48 | DAC Test Vector: Certificate Key Usage extension digitalSignature field is wrong (not present for DAC and present for PAI, which is OK as optional) | struct_dac_ext_key_usage_dig_si g_wrong (pid=32768) |
| 49 | DAC Test Vector: Certificate Key Usage extension keyCertSign field is wrong (present for DAC and not present for PAI) | struct_dac_ext_key_usage_key_c ert_sign_wrong (pid=32768) |

| 50 | DAC Test Vector: Certificate doesn't include Key Usage extension | struct_dac_ext_key_usage_missi ng (pid=32768) |
| 51 | DAC Test Vector: Certificate doesn't include Subject Key ID (SKID) extension | struct_dac_ext_skid_missing (pid=32768) |
| 52 | DAC Test Vector: Invalid certificate signature algorithm ECDSA_WITH_SHA1 | struct_dac_sig_algo_ecdsa_with_ sha1 (pid=32768) |
| 53 | DAC Test Vector: Invalid certificate public key curve secp256k1 | struct_dac_sig_curve_secp256k1 (pid=32768) |
| 54 | DAC Test Vector: PID in Subject field doesn't match PID in Issuer field | struct_dac_subject_pid_mismatc h (pid=32768) |
| 55 | DAC Test Vector: VID in Subject field doesn't match VID in Issuer field | struct_dac_subject_vid_mismatc h (pid=32768) |
| 56 | DAC Test Vector: Certificate validity period starts in the future | struct_dac_valid_in_future (pid=32768) |
| 57 | DAC Test Vector: Certificate validity period starts in the past | struct_dac_valid_in_past (pid=32768) |
| 58 | DAC Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mvid: is not exactly 4 uppercase hexadecimal digits | struct_dac_vidpid_fallback_enco ding_06 (pid=177) |
| 59 | DAC Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mvid: is not exactly 4 uppercase hexadecimal digits | struct_dac_vidpid_fallback_enco ding_07 (pid=177) |
| 60 | DAC Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mpid: is not exactly 4 uppercase hexadecimal digits | struct_dac_vidpid_fallback_enco ding_08 (pid=177) |
| 61 | DAC Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mpid: is not exactly 4 uppercase hexadecimal digits | struct_dac_vidpid_fallback_enco ding_09 (pid=177) |

| 62 | DAC Test Vector: Fallback VID and PID encoding example: invalid VID encoding | struct_dac_vidpid_fallback_enco ding_10 (pid=177) |
| 63 | DAC Test Vector: Fallback VID and PID encoding example: invalid, PID not present and VID not upper case | struct_dac_vidpid_fallback_enco ding_12 (pid=177) |
| 64 | DAC Test Vector: Fallback VID and PID encoding example: invalid VID prefix | struct_dac_vidpid_fallback_enco ding_13 (pid=177) |
| 65 | DAC Test Vector: Fallback VID and PID encoding example: invalid PID and VID prefixes | struct_dac_vidpid_fallback_enco ding_14 (pid=177) |
| 66 | DAC Test Vector: Mix of Fallback and Matter OID encoding for VID and PID: wrong, Correct values encoded in the common- name are ignored | struct_dac_vidpid_fallback_enco ding_16 (pid=177) |
| 67 | DAC Test Vector: Mix of Fallback and Matter OID encoding for VID and PID: invalid, PID is using Matter OID then VID must also use Matter OID | struct_dac_vidpid_fallback_enco ding_17 (pid=177) |
| 68 | DAC Test Vector: Fallback VID and PID encoding example from spec: PID is not a number | struct_dac_vidpid_fallback_enco ding_19 (pid=177) |
| 69 | PAI Test Vector: Invalid certificate version field set to v2(1) | struct_pai_cert_version_v2 (pid=32768) |
| 70 | PAI Test Vector: Certificate doesn't include Authority Key ID (AKID) extension | struct_pai_ext_akid_missing (pid=32768) |
| 71 | PAI Test Vector: Certificate Basic Constraint extension CA field is missing | struct_pai_ext_basic_ca_missing (pid=32768) |
| 72 | PAI Test Vector: Certificate Basic Constraint extension CA field is wrong (TRUE for DAC and FALSE for PAI) | struct_pai_ext_basic_ca_wrong (pid=32768) |
| 73 | PAI Test Vector: Certificate Basic Constraint extension critical field is missing | struct_pai_ext_basic_critical_mi ssing (pid=32768) |

| 74 | PAI Test Vector: Certificate Basic Constraint extension critical field is set as 'non-critical' | struct_pai_ext_basic_critical_wr ong (pid=32768) |
| 75 | PAI Test Vector: Certificate doesn't include Basic Constraint extension | struct_pai_ext_basic_missing (pid=32768) |
| 76 | PAI Test Vector: Certificate Basic Constraint extension PathLen field set to 1 | struct_pai_ext_basic_pathlen1 (pid=32768) |
| 77 | PAI Test Vector: Certificate Basic Constraint extension PathLen field set to 2 | struct_pai_ext_basic_pathlen2 (pid=32768) |
| 78 | PAI Test Vector: Certificate Basic Constraint extension PathLen field presence is wrong (present for DAC not present for PAI) | struct_pai_ext_basic_pathlen_pr esence_wrong (pid=32768) |
| 79 | PAI Test Vector: Certificate Key Usage extension critical field is missing | struct_pai_ext_key_usage_critic al_missing (pid=32768) |
| 80 | PAI Test Vector: Certificate Key Usage extension critical field is set as 'non-critical' | struct_pai_ext_key_usage_critic al_wrong (pid=32768) |
| 81 | PAI Test Vector: Certificate Key Usage extension cRLSign field is wrong (present for DAC and not present for PAI) | struct_pai_ext_key_usage_crl_si gn_wrong (pid=32768) |
| 82 | PAI Test Vector: Certificate Key Usage extension keyCertSign field is wrong (present for DAC and not present for PAI) | struct_pai_ext_key_usage_key_c ert_sign_wrong (pid=32768) |
| 83 | PAI Test Vector: Certificate doesn't include Key Usage extension | struct_pai_ext_key_usage_missi ng (pid=32768) |
| 84 | PAI Test Vector: Certificate doesn't include Subject Key ID (SKID) extension | struct_pai_ext_skid_missing (pid=32768) |
| 85 | PAI Test Vector: Invalid certificate signature algorithm ECDSA_WITH_SHA1 | struct_pai_sig_algo_ecdsa_with_ sha1 (pid=32768) |
| 86 | PAI Test Vector: Invalid certificate public key curve secp256k1 | struct_pai_sig_curve_secp256k1 (pid=32768) |

| 87 | PAI Test Vector: PID in Subject field doesn't match PID in Issuer field | struct_pai_subject_pid_mismatc h (pid=32768) |
| 88 | PAI Test Vector: VID in Subject field doesn't match VID in Issuer field | struct_pai_subject_vid_mismatc h (pid=32768) |
| 89 | PAI Test Vector: Certificate validity period starts in the future | struct_pai_valid_in_future (pid=32768) |
| 90 | PAI Test Vector: Certificate validity period starts in the past | struct_pai_valid_in_past (pid=32768) |
| 91 | PAI Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mvid: is not exactly 4 uppercase hexadecimal digits | struct_pai_vidpid_fallback_enco ding_06 (pid=177) |
| 92 | PAI Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mvid: is not exactly 4 uppercase hexadecimal digits | struct_pai_vidpid_fallback_enco ding_07 (pid=177) |
| 93 | PAI Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mpid: is not exactly 4 uppercase hexadecimal digits | struct_pai_vidpid_fallback_enco ding_08 (pid=177) |
| 94 | PAI Test Vector: Fallback VID and PID encoding example from spec: invalid, since substring following Mpid: is not exactly 4 uppercase hexadecimal digits | struct_pai_vidpid_fallback_enco ding_09 (pid=177) |
| 95 | PAI Test Vector: Fallback VID and PID encoding example: invalid VID encoding | struct_pai_vidpid_fallback_enco ding_10 (pid=177) |
| 96 | PAI Test Vector: Fallback VID and PID encoding example: invalid, PID not present and VID not upper case | struct_pai_vidpid_fallback_enco ding_12 (pid=177) |
| 97 | PAI Test Vector: Fallback VID and PID encoding example: invalid VID prefix | struct_pai_vidpid_fallback_enco ding_13 (pid=177) |

| 98 | PAI Test Vector: Fallback VID and PID encoding example: invalid PID and VID prefixes | struct_pai_vidpid_fallback_enco ding_14 (pid=177) |
| 99 | PAI Test Vector: Mix of Fallback and Matter OID encoding for VID and PID: wrong, Correct values encoded in the common- name are ignored | struct_pai_vidpid_fallback_enco ding_16 (pid=177) |
| 100 | PAI Test Vector: Mix of Fallback and Matter OID encoding for VID and PID: invalid, PID is using Matter OID then VID must also use Matter OID | struct_pai_vidpid_fallback_enco ding_17 (pid=177) |
| 101 | PAI Test Vector: Fallback VID and PID encoding example from spec: PID is not a number | struct_pai_vidpid_fallback_enco ding_19 (pid=177) |

## TC-DA-1.5 NOCSR Procedure Validation [DUT - Commissionee]

## Purpose

To verify the following checks during the NOCSR procedure:

1. DUT generates the NOCSR Information using CSRResponse Command
2. DUT generated NOCSR Information includes a signature using the Device Attestation Private Key
3. CSR SHALL follow the encoding and rules from PKCS #10
4. DUT generated that Node Operational Key Pair is unique
5. DUT rejects invalid CSRNonce sent by TH1

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | TH1 fully commissions DUT | |
| 2 | | PAI, DAC certificates are obtained and validated against externally obtained PAA certificate | |

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |
| 3 | TH2 | Commissioner |

## Device Topology

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | | | TH1 establishes a CASE session to the DUT and saves the attestation challenge as attestation_challe nge | |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Test Steps 6,7,8 cannot be executed with V1.0 SDK

## TC-DA-1.6 NOCSR Procedure Validation [DUT - Commissioner] - PROVISIONAL

## Purpose

To verify the following checks during the NOCSR procedure

To verify the following checks during the NOCSR procedure

1. DUT generates a valid 32 byte CSRNonce
2. 2.DUT detects errors generated by the TH1 in the NOCSR Information and reports failure
3. 3.DUT detects collision in Node Operational Key Pair sent from TH1 and reports failure

## PICS

## · MCORE.ROLE.COMMISSIONER

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissioner |
| 2 | TH1 | Commissionee |

## Device Topology

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 4 | | | | Verify that DUT reports error |
| 5 | | | Factory Reset DUT so that it is commissionable again | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 6 | | | Repeat Step1 to Step 4 multiple times. For each time in Step 3 TH1 generates the following error: | |

## Notes/Testing Considerations

Test Steps 3, 6, 6.1, 6.2, 6.3 cannot be executed with V1.0 SDK

## TC-DA-1.7 Validate CertificateChainRequest [DUT-Commissionee]

## Purpose

This test case validates that the device attestation certificates are properly signed and use different device attestation keys on each individual device.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | TH only has official PAAs from DCL | |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT1 | Commissionee |

| # | Device Name | Device Description |
| 2 | DUT2 | Commissionee - different device within the same device family as DUT1 (same VID/PID) |
| 3 | TH | Commissioner |

## Device Topology

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected |

| # | Ref | PICS | Test Step | Expected Outcome |

## TC-DA-1.8 Device Attestation Request Validation-Success Scenario [DUT-Commissioner]

## Purpose

Validate successful handing of valid certificates with different properties.

## PICS

## · MCORE.ROLE.COMMISSIONER

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissioner |
| 2 | TH | Commissionee |

## Device Topology

## Test Setup

| # | Condition | Notes |
| 1 | Manual intervention would be required during Device Attestation Test Procedure | |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Certificates for TC-DA-1.8

| # | Cert Description | Example certs |
| 1 | CD Test Vector: The authorized_paa_list contains ten PAAs one of which is valid PAA authorized to sign the PAI. | struct_cd_authorized_paa_list_c ount10_valid (pid=32768) |
| 3 | CD Test Vector: The authorized_paa_list contains two PAAs one of which is valid PAA authorized to sign the PAI. | struct_cd_authorized_paa_list_c ount2_valid (pid=32768) |

| 12 | CD Test Vector: Origin VID/PID different than VID/PID (correct use of origin) | struct_cd_origin_pid_vid_correc t (pid=32768) |
| 17 | CD Test Vector: The version_number field matches the VID and PID used in a DeviceSoftwareVersionModel entry in the DCL matching the certification record associated with the product presenting this CD. | struct_cd_version_number_mat ch (pid=32768) |
| 18 | DAC Test Vector: Valid certificate version field set to v3(2) | struct_dac_cert_version_v3 (pid=32768) |
| 19 | DAC Test Vector: Certificate includes optional Authority Information Access extension | struct_dac_ext_authority_info_a ccess_present (pid=32768) |

| 20 | DAC Test Vector: Certificate includes optional Extended Key Usage extension | struct_dac_ext_extended_key_us age_present (pid=32768) |
| 21 | DAC Test Vector: Certificate includes optional Subject Alternative Name extension | struct_dac_ext_subject_alt_nam e_present (pid=32768) |
| 22 | DAC Test Vector: Valid certificate signature algorithm ECDSA_WITH_SHA256 | struct_dac_sig_algo_ecdsa_with_ sha256 (pid=32768) |
| 23 | DAC Test Vector: Valid certificate public key curve prime256v1 | struct_dac_sig_curve_prime256 v1 (pid=32768) |
| 24 | DAC Test Vector: Fallback VID and PID encoding example from spec: valid and recommended since easily human-readable | struct_dac_vidpid_fallback_enco ding_01 (pid=177) |
| 25 | DAC Test Vector: Fallback VID and PID encoding example from spec: valid and recommended since easily human-readable | struct_dac_vidpid_fallback_enco ding_02 (pid=177) |
| 26 | DAC Test Vector: Fallback VID and PID encoding example from spec: valid example showing that order or separators are not considered at all for the overall validity of the embedded fields | struct_dac_vidpid_fallback_enco ding_03 (pid=177) |
| 27 | DAC Test Vector: Fallback VID and PID encoding example from spec: valid, but less readable | struct_dac_vidpid_fallback_enco ding_04 (pid=177) |
| 28 | DAC Test Vector: Fallback VID and PID encoding example from spec: valid, but highly discouraged, since embedding of substrings within other substrings may be confusing to human readers | struct_dac_vidpid_fallback_enco ding_05 (pid=177) |
| 29 | DAC Test Vector: Fallback VID and PID encoding example: valid, but less human-readable | struct_dac_vidpid_fallback_enco ding_11 (pid=177) |

| 30 | DAC Test Vector: Mix of Fallback and Matter OID encoding for VID and PID: valid, Matter OIDs are used and wrong values in the common-name are ignored | struct_dac_vidpid_fallback_enco ding_15 (pid=177) |
| 31 | DAC Test Vector: Fallback VID and PID encoding example from spec: valid and PID numeric only | struct_dac_vidpid_fallback_enco ding_18 (pid=1) |
| 32 | PAI Test Vector: Valid certificate version field set to v3(2) | struct_pai_cert_version_v3 (pid=32768) |
| 33 | PAI Test Vector: Certificate includes optional Authority Information Access extension | struct_pai_ext_authority_info_a ccess_present (pid=32768) |
| 34 | PAI Test Vector: Certificate Basic Constraint extension PathLen field set to 0 | struct_pai_ext_basic_pathlen0 (pid=32768) |
| 35 | PAI Test Vector: Certificate includes optional Extended Key Usage extension | struct_pai_ext_extended_key_us age_present (pid=32768) |
| 36 | PAI Test Vector: Certificate Key Usage extension digitalSignature field is wrong (not present for DAC and present for PAI, which is OK as optional) | struct_pai_ext_key_usage_dig_si g_wrong (pid=32768) |
| 37 | PAI Test Vector: Certificate includes optional Subject Alternative Name extension | struct_pai_ext_subject_alt_name _present (pid=32768) |
| 38 | PAI Test Vector: Valid certificate signature algorithm ECDSA_WITH_SHA256 | struct_pai_sig_algo_ecdsa_with_ sha256 (pid=32768) |
| 39 | PAI Test Vector: Valid certificate public key curve prime256v1 | struct_pai_sig_curve_prime256v 1 (pid=32768) |
| 40 | PAI Test Vector: Fallback VID and PID encoding example from spec: valid and recommended since easily human-readable | struct_pai_vidpid_fallback_enco ding_01 (pid=177) |
| 41 | PAI Test Vector: Fallback VID and PID encoding example from spec: valid and recommended since easily human-readable | struct_pai_vidpid_fallback_enco ding_02 (pid=177) |

[TC-DA-1.9] Device Attestation Revocation [DUT-Commissioner]

| 42 | PAI Test Vector: Fallback VID and PID encoding example from spec: valid example showing that order or separators are not considered at all for the overall validity of the embedded fields | struct_pai_vidpid_fallback_enco ding_03 (pid=177) |
| 43 | PAI Test Vector: Fallback VID and PID encoding example from spec: valid, but less readable | struct_pai_vidpid_fallback_enco ding_04 (pid=177) |
| 44 | PAI Test Vector: Fallback VID and PID encoding example from spec: valid, but highly discouraged, since embedding of substrings within other substrings may be confusing to human readers | struct_pai_vidpid_fallback_enco ding_05 (pid=177) |
| 45 | PAI Test Vector: Fallback VID and PID encoding example: valid, but less human-readable | struct_pai_vidpid_fallback_enco ding_11 (pid=177) |
| 46 | PAI Test Vector: Mix of Fallback and Matter OID encoding for VID and PID: valid, Matter OIDs are used and wrong values in the common-name are ignored | struct_pai_vidpid_fallback_enco ding_15 (pid=177) |
| 47 | PAI Test Vector: Fallback VID and PID encoding example from spec: valid and PID numeric only | struct_pai_vidpid_fallback_enco ding_18 (pid=1) |

## Purpose

Validate that the DUT properly handles revoked device attestation certificates during commissioning, including certificates revoked through indirect CRLs.

## PICS

## · MCORE.ROLE.COMMISSIONER

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissioner |
| 2 | TH | Commissionee |

## Device Topology

## Test Setup

| # | Condition | Notes |
| 1 | DUT SHALL be configured with the revocation information, revocation information can be generated by accessing the Device Attestation PKI Revocation Distribution Points Schema in the DCL. | For DUTs that support access to the DCL, the revocation information can be retrieved directly from the DCL. For DUTs that do not support DCL access, revocation information should be generated out of band and made available to the DUT. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Revocation Test Cases

| # | Test Case | Expected Result |
| 1 | TH presents a revoked DAC | DUT provides a clear indication to the user that the device may not be genuine |
| 2 | TH presents a revoked PAI | DUT provides a clear indication to the user that the device may not be genuine |
| 3 | TH presents both revoked DAC and PAI | DUT provides a clear indication to the user that the device may not be genuine |

| 4 | TH presents a valid non- revoked DAC and PAI | DUT proceeds with commissioning without warning |
| 5 | TH presents a DAC revoked using delegated CRL signer | DUT provides a clear indication to the user that the device may not be genuine |
| 6 | TH presents a PAI revoked using delegated CRL signer | DUT provides a clear indication to the user that the device may not be genuine |
| 7 | TH presents DAC and PAI both revoked using delegated CRL signer | DUT provides a clear indication to the user that the device may not be genuine |

## Chapter 11. Interaction Data Model Test Plan

## 11.1. PICS Definition

This section covers the Interaction Data Model Test Plan related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.IDM.S | Is the device a Server | O | |
| MCORE.IDM.C | Is the device a Client | O | |
| MCORE.IDM.C.InvokeR equest | Is the device a Client and Supports sending a Invoke Request Message | O | |
| MCORE.IDM.C.ReadReq uest | Is the device a Client and Supports sending a Read Request Message | O | |
| MCORE.IDM.C.WriteRe quest | Is the device a Client and Supports sending a Write Request Message | O | |
| MCORE.IDM.C.Subscrib eRequest | Is the device a Client and Supports sending a Subscribe Request Message | O | |
| MCORE.IDM.C.InvokeR equest.BatchCommand s | Is the device a Client and Supports sending multiple commands batched into a single Invoke Request Message | O | |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType _Bool | Is the device a Client and supports Reading an attribute of DataType Bool | O | |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType _String | Is the device a Client and supports Reading an attribute of DataType String | O | |

| MCORE.IDM.C.ReadReq uest.Attribute.DataType _UnsignedInteger | Is the device a Client and supports Reading an attribute of DataType Unsigned Integer | O | |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType _SignedInteger | Is the device a Client and supports Reading an attribute of DataType Signed Integer | O | |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType | Is the device a Client and supports Reading an attribute of DataType Struct | O | _Struct |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType _FloatingPoint | Is the device a Client and supports Reading an attribute of DataType Floating Point | O | |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType | Is the device a Client and supports Reading an attribute of DataType List | O | _List |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType _OctetString | Is the device a Client and supports Reading an attribute of DataType Octet String | O | |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType | Is the device a Client and supports Reading an attribute of DataType Enum | O | _Enum |
| MCORE.IDM.C.ReadReq uest.Attribute.DataType _Bitmap | Is the device a Client and supports Reading an attribute of DataType Bitmap | O | |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_Bool | Is the device a Client and supports Writing an attribute of DataType Bool | O | |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy | Is the device a Client and supports Writing an attribute of DataType String | O | pe_String |

| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_UnsignedInteger | Is the device a Client and supports Writing an attribute of DataType Unsigned Integer | O |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_SignedInteger | Is the device a Client and supports Writing an attribute of DataType Signed Integer | O |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_Struct | Is the device a Client and supports Writing an attribute of DataType Struct | O |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_FloatingPoint | Is the device a Client and supports Writing an attribute of DataType Floating Point | O |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_List | Is the device a Client and supports Writing an attribute of DataType List | O |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_OctetString | Is the device a Client and supports Writing an attribute of DataType Octet String | O |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_Enum | Is the device a Client and supports Writing an attribute of DataType Enum | O |
| MCORE.IDM.C.WriteRe quest.Attribute.DataTy pe_Bitmap | Is the device a Client and supports Writing an attribute of DataType Bitmap | O |
| MCORE.IDM.C.Subscrib eRequest.Attribute.Data Type_Bool | Is the device a Client and supports subscribing to an attribute of DataType Bool | O |

| MCORE.IDM.C.Subscrib eRequest.Attribute.Data Type_String | Is the device a Client and supports subscribing to an attribute of DataType String | O |
| MCORE.IDM.C.Subscrib eRequest.Attribute.Data Type_UnsignedInteger | Is the device a Client and supports subscribing to an attribute of DataType UnsignedInteger | O |
| MCORE.IDM.C.Subscrib eRequest.Attribute.Data Type_Integer | Is the device a Client and supports subscribing to an attribute of DataType Integer | O |
| MCORE.IDM.C.Subscrib eRequest.Attribute.Data Type_FloatingPoint | Is the device a Client and supports subscribing to an attribute of DataType FloatingPoint | O |
| MCORE.IDM.C.Subscrib eRequest.Attribute.Data Type_List | Is the device a Client and supports subscribing to an attribute of DataType List | O |
| MCORE.IDM.S.LargeDat a | Is the device a Server and capable of generating large data which is greater than 1 MTU(1280 bytes) | O |
| MCORE.IDM.C.Subscrib eEvent | Is the device a Client and supports subscribing to an individual Event | O |
| MCORE.IDM.C.ReadEve nt | Is the device a Client and supports Reading an individual Event | O |
| MCORE.IDM.C.Subscrib eRequest.MultipleAttrib utes | Is the device a client and supports subscribing to Multiple Attributes | O |
| MCORE.IDM.S.Persisten tSubscription | Is the device a Server and supports Persistent subscription | O |

Additionally, these PICS items from the ICD Management cluster are used in this test plan - these definitions are copies from the relevant test plan:

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S | Does the device implement the ICD Management cluster as a server? | O | |

## 11.2. PIXIT Definition

This section covers the Interaction Data Model Test Plan related PIXIT items that might be required in the following test cases.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PIXIT.IDM.ALLOW_EXT RA_CLUSTERS_ON_END POINT | Boolean indicating if the device adds extra clusters on endpoints | MCORE.IDM.S: O | Please note the warning in the specification C.7.17.4 before turning on this option |

## 11.3. Test Case List

| TC UUID | Test Case Name |
| TC-IDM-1.1 | Invoke Request Action from DUT to TH. [DUT as Client] |
| TC-IDM-1.2 | Invoke Response Action from DUT to TH. [DUT as Server] |
| TC-IDM-1.3 | Batched Commands Invoke Request Action from DUT to TH. [DUT as Client] |
| TC-IDM-1.4 | Batched Commands Invoke Response Action from DUT to TH. [DUT as Server] |
| TC-IDM-2.1 | Read Request Action from DUT to TH. [DUT as Client] |
| TC-IDM-2.2 | Report Data Action from DUT to TH. [DUT as Server] |

| TC-IDM-2.3 | Read and Subscribe from DUT to TH with the maximum number of paths supported. [DUT as Server] |
| TC-IDM-3.1 | Write Request Message from DUT to TH. [DUT as Client] |
| TC-IDM-3.2 | Write Response Message from DUT to TH. [DUT as Server] |
| TC-IDM-4.1 | Subscription Request Action from DUT. [DUT as Client] |
| TC-IDM-4.2 | Subscription Response Action from DUT. [DUT as Server] |
| TC-IDM-4.3 | Report Data Messages post Subscription Activation from DUT. [DUT as Server] |
| TC-IDM-4.4 | Persistent Subscription Test Cases. [DUT as Server] |
| TC-IDM-4.5 | Subscription Wildcard Path Filter [DUT as Server] - PROVISIONAL |
| TC-IDM-5.1 | Timed Request Action from DUT to TH. [DUT as Client] |
| TC-IDM-5.2 | Status Response from DUT in response to a Timed Request Action from TH. [DUT as Server] |
| TC-IDM-6.1 | Events Read Interaction from TH to DUT. [DUT as Server] |
| TC-IDM-6.2 | Events Subscribe Interaction from TH to DUT. [DUT as Server] |
| TC-IDM-6.3 | Events Read Interaction from DUT to TH. [DUT as Client] |
| TC-IDM-6.4 | Events Subscribe Interaction from DUT to TH. [DUT as Client] |
| TC-IDM-7.1 | Multi Fabric Subscription Test Cases. [DUT as Server] |
| TC-IDM-8.1 | Fabric scoped test cases. [DUT as Server] |
| TC-IDM-9.1 | CONSTRAINT_ERROR status response test cases [DUT as Server] - PROVISIONAL |
| TC-IDM-10.1 | Cluster requirements - Global attributes [DUT as Server] |
| TC-IDM-10.2 | Cluster requirements - Conformance [DUT as Server] |
| TC-IDM-10.3 | Cluster requirements - Revision [DUT as Server] |
| TC-IDM-10.4 | Cluster requirements - PICS [DUT as Server] |

| TC-IDM-10.5 | Device Type Requirements [DUT as Server] |
| TC-IDM-10.6 | Device Type Revisions [DUT as Server] |
| TC-IDM-11.1 | Data types - attribute strings [DUT as Server] |
| TC-IDM-12.1 | Device attribute information[DUT as Server] - data model |
| TC-IDM-13.1 | Accidental defaults check [DUT as Server] |
| TC-IDM-14.1 | Device-type-restricted clusters check [DUT as Server] |

## 11.4. Test Cases

## 11.4.1. Invoke Transaction Test Cases

## TC-IDM-1.1 Invoke Request Action from DUT to TH - [DUT as Client]

## Purpose

Verifying the Invoke Request Action sent from the DUT is according to the specification.

## PICS

- MCORE.IDM.C.InvokeRequest

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which is the recipient of the Invoke Request Message - Server |
| 2 | DUT | DUT as the device which sends the Invoke Request Message - Client |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Test Setup

Test will need a reference implementation of the cluster of which the DUT is the client.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | 8.8.2.1/1 0.6.9 | | DUT sends the Invoke Request Message to the TH. The Message should contain one valid CommandDataIB, which has the specific Endpoint, Specific Cluster and Specific Command. Send 2 more Invoke Request Messages to the TH. | On the TH verify the received request messages have the same paths as provided in the command. |

## Notes/Testing Considerations

The Cluster and Commands should be based on the cluster implementation on the DUT. Test Step 2 is not in scope for 1.3

Test Step 3 can be tested by using the command scan networks.

## TC-IDM-1.2 Invoke Response Action from DUT to TH - [DUT as Server]

## Purpose

Verifying the Invoke Response of the DUT once it receives the Invoke Request Action.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which sends the Invoke Request Message - Client |

| # | Device Name | Device Description |
| 2 | DUT | DUT as the device which responds to the Invoke Request Message - Server |

## Device Topology

Depending on the Test Case, TH and DUT will be commissioned and are on the same fabric.

## Test Setup

## Test will need a reference implementation of the cluster of which the DUT is the server

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Test Steps #7 cannot be executed with V1.0 SDK

## TC-IDM-1.3 Batched Commands Invoke Request Action from DUT to TH - [DUT as Client]

## Purpose

Verifying the Batched Commands Invoke Request Action sent from the DUT is according to the specification.

## PICS

- MCORE.IDM.C.InvokeRequest.BatchCommands

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which is the recipient of the Invoke Request Message - Server. This device needs nlfaultinject enabled at compile time. |
| 2 | TH Client | Test harness as client used to set up fault injection on TH server during precondition - Client |

| # | Device Name | Device Description |
| 3 | DUT | DUT as the device which sends the Invoke Request Message - Client |

## Device Topology

TH device (Server) and TH client will be commissioned and are on the same fabric. TH device (Server) and DUT will be commissioned and are on the same fabric.

## Test Setup

Test will need a reference implementation of the cluster of which the DUT is the client.

## Pre-Conditions

| # | Doc. Ref. | Condition | Notes |
| 3 | | TH Client send FailAtFault command to FaultInjection cluster to TH device (Server). FailAtFault arguments are: • Type: 3 (ChipFault) • Id: 12 • NumberCallsToSkip: 3 • NumCallsToFail: 1 • TakeMutex: False | Make sure command's response indicates it was successful |
| 4 | | TH Client send FailAtFault command to FaultInjection cluster to TH device (Server). FailAtFault arguments are: • Type: 3 (ChipFault) • Id: 13 • NumberCallsToSkip: 2 • NumCallsToFail: 1 • TakeMutex: False | Make sure command's response indicates it was successful |

| # | Doc. Ref. | Condition | Notes |
| 5 | | TH Client send FailAtFault command to FaultInjection cluster to TH device (Server). FailAtFault arguments are: • Type: 3 (ChipFault) • Id: 14 • NumberCallsToSkip: 1 • NumCallsToFail: 1 • TakeMutex: False | Make sure command's response indicates it was successful |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.8.2.1/1 0.6.9 | | DUT sends the Invoke Request Message to the TH. The Message should contain multiple valid unique paths. For example this could be, Path = • Endpoint = Endpoint1, Cluster = ClusterID, Command Command1 • Endpoint = Endpoint1, Cluster = ClusterID, Command Command2 TH responds with a single command response message containing responses to both of the messages in the same order | = = On the DUT: • Verify it does not crash. • Note: If validating response on DUT, responses will be based on TH servers ability to response to those requests. On the TH device (server) verify: * The received request message has the same paths as provided in the command (compare with information provided by the manufacturer) and that the paths are unique. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | 8.8.2.1/1 0.6.9/10. 6.10.2 | | DUT sends the Invoke Request Message to the TH. The Message should contain multiple valid unique paths. For example this could be, Path = • Endpoint = Endpoint1, Cluster = ClusterID, Command = Command1 • Endpoint = Endpoint1, Cluster = ClusterID, Command = Command2 TH SHALL responds in the following manner (some fields omitted, only critical fields for validating spec behavior are mentioned): • Invoke Response Message #1: ◦ InvokeResponses = [Status = (CommandPath = (Endpoint = Endpoint1, Cluster = ClusterID, Command = Command1), StatusIB = (Status = FAILURE (0x1)))] ◦ MoreChunkedMessages = True • Invoke Response Message #2: ◦ InvokeResponses = [Status = (CommandPath = (Endpoint = Endpoint1, Cluster = ClusterID, Command = Command2), StatusIB = (Status = FAILURE (0x1)))] Note there are two Invoke Response Messages, responses are | On the DUT: • Verify it does not crash. • Note: If validating response on DUT, it will have received 2 responses with status FAILURE(0x01). On TH device (server) verify: • It has not crashed. • Verify logs indicate separate Invoke Response Messages and that responses are in same order as requests. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | 8.8.2.1/1 0.6.9/10. 6.10.2 | | DUT sends the Invoke Request Message to the TH. The Message should contain multiple valid unique paths. For example this could be, Path = • Endpoint = Endpoint1, Cluster = ClusterID, Command = Command1 • Endpoint = Endpoint1, Cluster = ClusterID, Command = Command2 TH SHALL responds in the following manner (some fields omitted, only critical fields for validating spec behavior are mentioned): • Invoke Response Message #1: ◦ InvokeResponses = [Status = (CommandPath = (Endpoint = Endpoint1, Cluster = ClusterID, Command = Command2), StatusIB = (Status = FAILURE (0x1)))] ◦ MoreChunkedMessages = True • Invoke Response Message #2: ◦ InvokeResponses = [Status = (CommandPath = (Endpoint = Endpoint1, Cluster = ClusterID, Command = Command1), StatusIB = (Status = FAILURE (0x1)))] Note there are two Invoke Response Messages, the order of responses is the opposite of the | On the DUT: • Verify it does not crash. • Note: If validating response on DUT, it will have received 2 responses with status FAILURE(0x01). On TH device (server) verify: • It has not crashed. • Verify logs indicate separate Invoke Response Messages and that responses are in reverse order. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 4 | 8.8.2.1/1 0.6.9/10. 6.10.2 | | DUT sends the Invoke Request Message to the TH. The Message should contain multiple valid unique paths. For example this could be, Path = • Endpoint = Endpoint1, Cluster = ClusterID, Command = Command1 • Endpoint = Endpoint1, Cluster = ClusterID, Command = Command2 TH SHALL responds in the following manner (some fields omitted, only critical fields for validating spec behavior are mentioned): • Invoke Response Message #1: ◦ InvokeResponses = [Status = (CommandPath = (Endpoint = Endpoint1, Cluster = ClusterID, Command = Command1), StatusIB = (Status = FAILURE (0x1)))] Note there is a single Invoke | On the DUT: • Verify it does not crash. • Note: If validating response on DUT, it will have received 1 responses with status FAILURE(0x01), the other command will not have been responded and might show up as Status = NO_COMMAND_RESPONSE(0x CC) On TH device (server) verify: • It has not crashed. that a response was dropped. |
| 4 | 8.8.2.1/1 0.6.9/10. 6.10.2 | | Response Messages, only one request is responded to, the other | • Verify logs indicate single Invoke Response Message and |

## Notes/Testing Considerations

Test Steps 1 through 4 requires Product Maker to provide instructions for how to trigger sending multiple commands on the DUT to the TH. The commands used may be the same for all 4 test steps Test Step 1 requires Product Maker to provide the concrete command paths that the aforementioned instructions are targeting for validation.

Test Step 5 requires Product Maker to provide instructions for how to trigger single command on the DUT to the TH.

No other commands are allowed to be sent between Pre-Conditions and Test Procedure doing so may cause TH device (Server) to misbehave.

## TC-IDM-1.4 Batched Commands Invoke Response Action from DUT to TH - [DUT as Server]

## Purpose

Verifying the Invoke Response of the DUT once it receives the Invoke Request Action.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which sends the Invoke Request Message - Client |
| 2 | DUT | DUT as the device which responds to the Invoke Request Message - Server |

## Device Topology

Depending on the Test Case, TH and DUT will be commissioned and are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 11 | 8.8.2.3/1 0.6.10.2 | MCORE. IDM.S: DMTES T | If MaxPathsPerInvoke > 1, TH sends the Invoke Request Message to the DUT with the following two CommandPaths : • [Endpoint = 0, Cluster = General Diagnostics Cluster (0x33), Command = PayloadTestRequest (0x03)] ◦ The data for PayloadTestRequest must have EnableKey field set to PIXIT.DGGEN.TEST_EVENT_ TRIGGER_KEY, Value field set to 65 (value for "A" in ASCII), Count field set to 800. • [Endpoint = 0, Cluster = Node Operational Credentials Cluster (0x3E), Command = CertificateChainRequest (0x02)] ◦ The data for CertificateChainRequest must have the CertificateType field set to 1. | On the TH verify the received response message has two successful responses. On TH verify that we received two separate Invoke Response Messages. |

## Notes/Testing Considerations

Test does not try sending as many batched commands in a single invoke message indicated by MaxPathsPerInvoke . This is because the value provided might be higher than number of commands we can

fit into single InvokeRequest base on packet MTU size.

If DUT supports batched commands, it SHALL provide PIXIT.DGGEN.TEST\_EVENT\_TRIGGER\_KEY

## 11.4.2. Read Transaction Test Cases

## TC-IDM-2.1 Read Request Action from DUT to TH. [DUT as Client]

## Purpose

Verifying the Read Request Action sent from the DUT is according to the specification.

## PICS

## · MCORE.IDM.C.ReadRequest

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which is the recipient of the Read Request Message - Server |
| 2 | DUT | DUT as the device which sends the Read Request Message - Client |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Test Setup

Test will need a reference implementation of the cluster of which the DUT is the client. TH with Manufacturer specific clusters and attributes to be used for Test #21.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.4.2.1/1 0.6.2 | | DUT sends the Read Request Message to the TH to read one attribute on a given cluster and endpoint. AttributePath = [[Endpoint = Specific Endpoint, Cluster = Specific ClusterID, Attribute = Specific Attribute]] On receipt of this message, TH should send a report data action with the attribute value to the DUT. | Verify that the TH receives the right Read Request Message. + |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | 8.4.2.1/1 0.6.2 | | DUT sends the Read Request Message to the TH to read all attributes on a given cluster and Endpoint AttributePath = [[Endpoint = Specific Endpoint, Cluster = Specific ClusterID]] On receipt of this message, TH should send a report data action with the attribute value to the DUT. | Verify that the TH receives the right Read Request Message. + |

| # | Ref | PICS | Test Step | Expected Outcome |
| 8 | 8.4.2.1/1 0.6.2 | | DUT sends the Read Request Message to the TH to a specific endpoint to read a particular attribute from all the clusters at that endpoint AttributePath = [[ Endpoint = Specific Endpoint, Attribute = specific attribute]] On receipt of this message, TH should send a report data action with the attribute value to the DUT. | Verify that the TH receives the right Read Request Message. + |
| 9 | 8.4.2.1/1 0.6.2 | MCORE. IDM.C.R eadReq uest.Att ribute. DataTy pe_Bool | DUT sends the Read Request Message to the TH to read an attribute of data type bool. + | Verify that the TH receives the right Read Request Message. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 10 | 8.4.2.1/1 0.6.2 | MCORE. IDM.C.R eadReq uest.Att ribute. DataTy pe_Stri ng | DUT sends the Read Request Message to the TH to read an attribute of data type string. + | Verify that the TH receives the right Read Request Message. |
| 11 | 8.4.2.1/1 0.6.2 | MCORE. IDM.C.R eadReq uest.Att ribute. DataTy pe_Unsi gnedInt eger | DUT sends the Read Request Message to the TH to read an attribute of data type unsigned integer. + | Verify that the TH receives the right Read Request Message. |
| 12 | 8.4.2.1/1 0.6.2 | MCORE. IDM.C.R eadReq uest.Att ribute. DataTy pe_Sign edInteg er | DUT sends the Read Request Message to the TH to read an attribute of data type signed integer. + | Verify that the TH receives the right Read Request Message. |
| 13 | 8.4.2.1/1 0.6.2 | MCORE. IDM.C.R eadReq uest.Att ribute. DataTy pe_Floa tingPoi nt | DUT sends the Read Request Message to the TH to read an attribute of data type floating point. + | Verify that the TH receives the right Read Request Message. |
| 14 | 8.4.2.1/1 0.6.2 | MCORE. IDM.C.R eadReq uest.Att ribute. DataTy pe_Octe tString | DUT sends the Read Request Message to the TH to read an attribute of data type Octet String. + | Verify that the TH receives the right Read Request Message. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 20 | 8.4.2.1/1 0.6.2 | | DUT sends the Read Request Message to the TH to read something(Attribute) which is larger than 1 MTU(1280 bytes) and per spec can be chunked. For every chunked data message received, except the last one, DUT sends a status response. | Verify on the TH that the DUT sends a status message back to the TH on receipt of the report data action for every chunked message except the last one. Verify that the last chunked message DUT does not send a status response back. |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

The Cluster and Commands should be based on the cluster implementation on the DUT.

## TC-IDM-2.2 Report Data Action from DUT to TH. [DUT as Server]

## Purpose

Verifying the Report Data Action sent from the DUT in response to the Read Request Action is according to the specification.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness sends Read Request Message - Client |
| 2 | DUT | DUT as the device which responds to the Read Request Message - Server |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Test Setup

N/A

## Test Procedure

| # | Test Step | Expected Outcome |

| # | Test Step | Expected Outcome |

| # | Test Step | Expected Outcome |

| # | Test Step | Expected Outcome |
| 20 | TH should have access to only a single cluster at one Endpoint1. TH sends a Read Request Message to the DUT to read all attributes from all clusters at Endpoint1 AttributePath = [[Endpoint = Specific Endpoint]] + | Verify that the DUT sends back data of all attributes only from that one cluster to which it has access. Verify that there are no errors sent back for attributes the TH has no access to. |

## Notes/Testing Considerations

The Cluster and Commands should be based on the cluster implementation on the DUT.

## TC-IDM-2.3 Read and Subscribe from DUT to TH with the maximum number of paths supported. [DUT as Server]

## Purpose

This test case verifies that the DUT properly handles Read and Subscribe requests with the maximum number of read/subscribe paths reported to be supported. This information comes from the CapabilityMinima struct from BasicInformation cluster.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness sends Read Request and Subscribe Request Messages - Client |
| 2 | DUT | DUT as the device which responds to the Read and Subscribe Request Messages - Server |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Test Setup

N/A

## Test Procedure

| # | Test Step | Expected Outcome |
| 4 | TH sends a Subscribe Request Message to the DUT with a number of paths up to the SubscribePathsSupported value. TH then modifies one of the subscribed attributes and waits for a Report Data Action. | Verify that the subscription is established and that the DUT sends a Report Data Action when the subscribed attribute is modified. |

## Notes/Testing Considerations

1. The number of paths in the request may be reduced to fit into a single MTU as requests cannot be chained.

## 11.4.3. Write Transaction Test Cases

## TC-IDM-3.1 Write Request Action from DUT to TH. [DUT as Client]

## Purpose

Verifying the Write Request Action sent from the DUT is according to the specification.

## PICS

- MCORE.IDM.C.WriteRequest

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which is the recipient of the Write Request Message - Server |
| 2 | DUT | DUT as the device which sends the Write Request Message - Client |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Test Setup

Test will need a reference implementation of the cluster of which the DUT is the client.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.7.2.1/1 0.6.6 | | DUT sends the WriteRequestMessage to the TH modify one attribute data + | Verify on the TH that the correct WriteRequestMessage has been received. + |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | 8.7.2.1/1 0.6.6 | | DUT sends the WriteRequestMessage to the TH to modify one attribute on all Endpoints. On receipt of this message, TH should modify the attribute and send a WriteResponseMessage to the DUT. | Verify on the TH that the correct WriteRequestMessage has been received. |
| 3 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Bo ol | DUT sends the WriteRequestMessage to the TH to write an attribute of data type bool. + | Verify on the TH that the correct WriteRequestMessage has been received. |
| 4 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Str ing | DUT sends the WriteRequestMessage to the TH to write an attribute of data type string. + | Verify on the TH that the correct WriteRequestMessage has been received. |
| 5 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Un signedI nteger | DUT sends the WriteRequestMessage to the TH to write an attribute of data type unsigned integer. + | Verify on the TH that the correct WriteRequestMessage has been received. |
| 6 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Sig nedInte ger | DUT sends the WriteRequestMessage to the TH to write an attribute of data type signed integer. + | Verify on the TH that the correct WriteRequestMessage has been received. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 7 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Flo atingPo int | DUT sends the WriteRequestMessage to the TH to write an attribute of data type floating point. + | Verify on the TH that the correct WriteRequestMessage has been received. |
| 8 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Oct etString | DUT sends the WriteRequestMessage to the TH to write an attribute of data type Octet String. + | Verify on the TH that the correct WriteRequestMessage has been received. |
| 9 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Str uct | DUT sends the WriteRequestMessage to the TH to write an attribute of data type Struct. + | Verify on the TH that the correct WriteRequestMessage has been received. |
| 10 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_Lis t | DUT sends the WriteRequestMessage to the TH to write an attribute of data type List. + | Verify on the TH that the correct WriteRequestMessage has been received. |
| 11 | 8.7.2.1/1 0.6.6 | MCORE. IDM.C. WriteR equest. Attribut e.DataT ype_En um | DUT sends the WriteRequestMessage to the TH to write an attribute of data type enum. + | Verify on the TH that the correct WriteRequestMessage has been received. |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

The Cluster and Commands should be based on the cluster implementation on the DUT. Test Steps #2 and #15 cannot be executed with V1.0 SDK

## TC-IDM-3.2 Write Response Action from DUT to TH. [DUT as Server]

## Purpose

Verifying the Write Response Action sent from the DUT in response to the Write Request Action is according to the specification.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness sends Write Request Message |
| 2 | DUT | DUT as the device which responds with a Write Response Message. |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Spec References

C.8.7 - write interaction

## Test Setup

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH sends the WriteRequestMessage to the DUT to write any attribute on an unsupported Endpoint. DUT responds with the Write Response action | Verify on the TH that the DUT sends the status code UNSUPPORTED_ENDPOINT |
| 2 | TH sends the WriteRequestMessage to the DUT to write any attribute on an unsupported cluster. DUT responds with the Write Response action | Verify on the TH that the DUT sends the status code UNSUPPORTED_CLUSTER |
| 3 | TH sends the WriteRequestMessage to the DUT to write an unsupported attribute DUT responds with the Write Response action | Verify on the TH that the DUT sends the status code UNSUPPORTED_ATTRIBUTE |

| # | Test Step | Expected Outcome |
| NOTE | SuppressResponse is not currently supported | • Please see connectedhomeip/#41227 issue referencing this not currently supported • Please see this following PR that will be updated and merged once the SuppressResponse functionality is known to be working: connectedhomeip/#41590 (This updated IDM_3_2 test step 4 to validate SuppressResponse behavior) |

## Notes/Testing Considerations

1. The Cluster and Commands should be based on the cluster implementation on the DUT.
2. Test Step 4 cannot be executed with current SDK

## 11.4.4. Subscription Transaction Test Cases

## TC-IDM-4.1 SubscriptionRequestMessage from DUT test cases. [DUT as Client]

## Purpose

This test case will verify the subscription request messages sent from the DUT to the target node

## PICS

- MCORE.IDM.C.SubscribeRequest

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as Publisher/Server |
| 2 | DUT | DUT as subscriber/Client |

## Device Topology

DUT and TH are on the same fabric

Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest | DUT sends a subscription request message to the target node/reference device for a single attribute of any data type supported. | On the reference device verify the subscription message received has the following fields. KeepSubscriptions which is of type bool MinIntervalFloor which is of type uint16 MaxIntervalCeilin g which is of type uint16 [Optional]Attribut eRequests which is of type list and contains the attribute paths [Optional]DataVer sionFilters which is of type list and contains the data versions of the attributes requested.+ [Optional]EventRe quests which is of type list [Optional]EventFil ters which is of type list [Optional]FabricFi ltered which is of type bool + |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest | DUT sends the subscription request message to TH TH sends a report data DUT sends the status response back to TH | Verify on the TH that the status response received from the DUT is "Success" |
| 3 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest.Attr ibute.DataType_Bo ol | Activate the subscription between the DUT and the TH for an attribute of data type boolean. Modify that attribute on the TH. TH should send the modified data to the DUT. Modify the attribute multiple times (3 times). | Verify on the TH that the status response received from the DUT for every report data sent is a "Success" |
| 4 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest.Attr ibute.DataType_St ring | Activate the subscription between the DUT and the TH for an attribute of data type string. Modify that attribute on the TH. TH should send the modified data to the DUT. Modify the attribute multiple times (3 times). | Verify on the TH that the status response received from the DUT for every report data sent is a "Success" |

| # | Ref | PICS | Test Step | Expected Outcome |
| 5 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest.Attr ibute.DataType_U nsignedInteger | Activate the subscription between the DUT and the TH for an attribute of data type unsigned integer. Modify that attribute on the TH. TH should send the modified data to the DUT. Modify the attribute multiple times (3 times). | Verify on the TH that the status response received from the DUT for every report data sent is a "Success" |
| 6 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest.Attr ibute.DataType_In teger | Activate the subscription between the DUT and the TH for an attribute of data type signed integer. Modify that attribute on the TH. TH should send the modified data to the DUT. Modify the attribute multiple times (3 times) | Verify on the TH that the status response received from the DUT for every report data sent is a "Success" |

| # | Ref | PICS | Test Step | Expected Outcome |
| 7 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest.Attr ibute.DataType_Fl oatingPoint | Activate the subscription between the DUT and the TH for an attribute of data type Floating Point. Modify that attribute on the TH. TH should send the modified data to the DUT. Modify the attribute multiple | Verify on the TH that the status response received from the DUT for every report data sent is a "Success" |
| 8 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest.Attr ibute.DataType_Li st | Activate the subscription between the DUT and the TH for an attribute of data type list. Modify that attribute on the TH. TH should send the modified data to the DUT. Modify the attribute multiple times (3 times) | Verify on the TH that the status response received from the DUT for every report data sent is a "Success" |

| # | Ref | PICS | Test Step | Expected Outcome |
| 9 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest | Activate the subscription between the DUT and the TH for an attribute. Force the TH to not send any report data for the duration of the maximum interval. After the maximum interval, TH sends a report data with the subscription id created during the subscription activation. | Verify on the TH that the status response received from the DUT says "INVALID_SUBSCR IPTION". |

| # | Ref | PICS | Test Step | Expected Outcome |
| 10 | 10.6.4/8.5.2 | MCORE.IDM.C.Sub scribeRequest.Mul tipleAttributes | DUT sends a subscription request message to the target node/reference device for multiple attributes (>1 attributes). | On the reference device verify the subscription request message received has the following fields. KeepSubscriptions which is of type bool MinIntervalFloor which is of type uint16 MaxIntervalCeilin g which is of type uint16 AttributeRequests which is of type list and contains the paths for the requested attributes. DataVersionFilters which is of type list and contains the data versions of the attributes requested. [Optional]EventRe quests which is of type list [Optional]EventFil ters which is of type list FabricFiltered which is of type bool + |

## Notes/Testing Considerations

The Expected Outcome for the tests is verified by looking at the pretty printed TLV on the TH. Vendor needs to specify how to trigger the subscription on the DUT.

## TC-IDM-4.2 Subscription Response Messages from DUT Test Cases. [DUT as Server]

## Purpose

This test case will verify the subscription response messages sent in response to the subscription request messages to activate a subscription are according to specification.

## PICS

## · MCORE.IDM.S

## Pre-Conditions

| # | Doc. Ref. | Condition |
| 1 | | Commission TH to DUT |

## Required Devices

| # | Device Name | Device Description |
| 1 | CR1 | Controller 1 as the subscriber - client |
| 2 | CR2 | Controller 2 as the subscriber with limited access to the DUT - client |
| 3 | DUT | DUT as the target of the subscription - server |

## Device Topology

DUT, CR1 and CR2 are on the same fabric.

CR2 is setup such that it has limited access to the DUT based on the test step.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| 1 | C.9.17 | CR1 reads the ServerList attribute from the Descriptor cluster on EP0. If the ICD Management cluster ID (70,0x46) is present in the list: * CR1 reads the IdleModeDuration attribute from the DUT and sets SUBSCRIPTION_M AX_INTERVAL_PU BLISHER_LIMIT_S EC = IdleModeDuration and min_interval_floor _s to 0, otherwise, set SUBSCRIPTION_M AX_INTERVAL_PU BLISHER_LIMIT_S EC = 60 mins and min_interval_floor _s to 3. |

| 10.6.5/8.5.3 | 2 |

| 3 | 10.6.5/8.5.3 | | CR1 sends a subscription message to the DUT with MaxIntervalCeiling set to a value less than SUBSCRIPTION_M AX_INTERVAL_PU BLISHER_LIMIT . DUT sends a report data action to the CR1. CR1 sends a success status response to the DUT. DUT sends a Subscribe Response Message to the CR1 to activate the subscription. | Verify on the CR1, a report data message is received. Verify it contains the following data Report data - data of the attribute/event requested earlier. Verify on the CR1 the Subscribe Response has the following fields, SubscriptionId - Verify it is of type uint32. MaxInterval - Verify it is of type uint32. Verify that the MaxInterval is less than or equal to SUBSCRIPTION_M |

| 5 | 10.6.5/8.5.3 | Setup CR2 such that it does not have access to all attributes on a specific cluster and endpoint. CR2 sends a subscription request to subscribe to all attributes for which it does not have access. AttributePath = [[Cluster = ClusterID, Endpoint = EndpointID ]]. | Verify that the DUT returns a "INVALID_ACTION " status response. |

| 8 | 10.6.5/8.5.3 | CR1 sends a subscription request action for an attribute with an empty DataVersionFilters field. DUT sends a report data action with the data of the attribute along with the data version. Tear down the subscription for that attribute. Start another subscription with the DataVersionFilter field set to the data version received above. | Verify that the subscription is activated between CR1 and DUT. |

| | 10.6.5/8.5.3 | 9 | CR1 sends a subscription request action for an attribute and sets the MinIntervalFloor to min_interval_floor _s and MaxIntervalCeilin g to 10. Activate the Subscription between CR1 and DUT and record the time when the priming ReportDataMessag e is received as t_report . Save the returned MaxInterval from the SubscribeRespons | |

| 13 | 10.6.5/8.5.3 | | CR1 sends a subscription request to subscribe to a global attribute on an endpoint on all clusters. AttributePath = [[Attribute = Global Attribute, Endpoint = EndpointID ]]. + | Verify that the Subscription succeeds and the DUT sends back the attribute values for the global attribute. Verify no data from other endpoints is sent back. |

## TC-IDM-4.3 Report Data Messages post Subscription Activation from DUT Test Cases. [DUT as Server]

## Purpose

This test case will verify the report data messages sent from the DUT after activating subscription are according to specification.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as the subscriber - Client |
| 2 | DUT | DUT as the target of the subscription - Server |

## Device Topology

## DUT and TH are on the same fabric

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | 10.6.5/8. 5.3 | | DUT and TH activate the subscription. | Verify on the TH, a report data message is received. Verify on the TH the Subscribe Response has the following fields: SubscriptionId and MaxInterval In the following Steps 2, 3, 5-10, 13, and 15, the MaxInterval time reference in each step is the MaxInterval presented in the Subscribe Response of the subscription. |

| 7 | 10.6.5/8. 5.3 | MCORE. IDM.S.A ttribute _W.Dat aType_ Unsign edInteg er | Activate the subscription between the DUT and the TH for an attribute of data type "unsigned integer". Modify that attribute on the DUT. DUT should send the report data with the modified attribute value. Modify the attribute multiple times (3 times) before the MaxInterval time specified during the subscription activation. | Verify on the TH that the DUT sends the correct value of the attribute. |
| 8 | 10.6.5/8. 5.3 | MCORE. IDM.S.A ttribute _W.Dat aType_ SignedI nteger | Activate the subscription between the DUT and the TH for an attribute of data type "signed integer". Modify that attribute on the DUT. DUT should send the report data with the modified attribute value. Modify the attribute multiple times (3 times)before the MaxInterval time specified during the subscription activation. | Verify on the TH that the DUT sends the correct value of the attribute. |
| 9 | 10.6.5/8. 5.3 | MCORE. IDM.S.A ttribute _W.Dat aType_ Floatin gPoint | Activate the subscription between the DUT and the TH for an attribute of data type "floating point". Modify that attribute on the DUT. DUT should send the report data with the modified attribute value. Modify the attribute multiple times (3 times) before the MaxInterval time specified during the subscription activation. | Verify on the TH that the DUT sends the correct value of the attribute. |

| 11 | 10.6.5/8. 5.3 | | Activate the subscription between the DUT and the TH for any attribute. KeepSubscriptions flag should be set to False After the Maximum interval time is elapsed, TH should send another subscription request message with different parameters than before. KeepSubscriptions flag should be set to False Change the value of the attribute requested on the DUT. | Verify that the DUT sends the changed value of the attribute with the newest subscription id sent with the second request. |

| 15 | 10.6.5/8. 5.2.1 | TH sends a subscription request action for an attribute to the DUT with the KeepSubscriptions flag set to True. Activate the subscription between DUT and the TH. Initiate another subscription request action to the DUT for another attribute with the KeepSubscriptions flag set to False. Change both the attribute values on the DUT. | Verify that both the subscriptions are active and the TH receives notifications for both these attributes. Verify that the first subscription is terminated after the MaxInterval of the first subscription is reached. |

| 20 | 10.6.5/8. 5.3 | TH sends a subscription request to subscribe to all attributes from all clusters on an endpoint. AttributePath = [[Endpoint = EndpointID]]. Set the MinIntervalFloor to some value say "N"(seconds). Change all or few of the attributes on the DUT | Verify that the DUT sends reports for all the attributes that have changed after N seconds. |
| 21 | 10.6.5/8. 5.3 | TH sends a subscription request to subscribe to all attributes from a specific cluster on all endpoints. AttributePath = [[Cluster = ClusterID]]. Set the MinIntervalFloor to some value say "N"(seconds). Change all or few of the attributes on the DUT | Verify that the DUT sends reports for all the attributes that have changed after N seconds. |

## Notes/Testing Considerations

The Expected Outcome for the tests is verified by looking at the pretty printed TLV on the TH. Test Steps 17 19, 20 and 21 cannot be executed with V1.0 SDK

## TC-IDM-4.4 Persistent Subscription Test Cases. [DUT as Server]

## Purpose

This test case will verify persistent subscription on a server device.

## PICS

- MCORE.IDM.S
- MCORE.IDM.S.PersistentSubscription

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as the subscriber - Client |
| 2 | DUT | DUT as the Publisher - Server |

## Device Topology

## DUT and TH are on the same fabric

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

MaxInterval time will start after all DUT initialization is done (example: bootup, connect to Wi-Fi, etc.)

## TC-IDM-4.5 Subscription Wildcard Path Filter [DUT as Server] - PROVISIONAL

## Purpose

This test case verifies that the DUT properly applies Wildcard Path filters in a subscription request.

Verifies:

- Subscription request with each of the WildcardPathFlags set to 1 independently (1 filter path per SubscriptionRequest), with WildcardFilterConfigurationVersion set to current ConfigurationVersion (only requested filter values should be elided from priming report)
- Subscription request with ALL WildcardPathFlags set to 1, with WildcardFilterConfigurationVersion set to current ConfigurationVersion (all requested filtered values should be elided from the priming report)
- Subscription request with WildcardPathFlags set to 0, with WildcardFilterConfigurationVersion set to current ConfigurationVersion (all values should appear in the priming report)
- Subscription request with WildcardPathFlags elided, with WildcardFilterConfigurationVersion set to current ConfigurationVersion (all values should appear in the priming report)
- Subscription request with ALL WildcardPathFlags set to 1, with WildcardFilterConfigurationVersion set to a value 1 lower than the current ConfigurationVersion (all values should appear in the priming report)
- Subscription request with ALL WildcardPathFlags set to 1, with WildcardFilterConfigurationVersion elided (all values should appear in the priming report)
- Subscription request with both WildcardPathFlags and WildcardFilterConfigurationVersion elided (all values should appear in the priming report)

## · MCORE.IDM.S

## 11.4.5. Timed Request Action Test Cases

## TC-IDM-5.1 Timed Request Action from DUT to TH. [DUT as Client]

## Purpose

Verifying the Timed Request Action sent from the DUT is according to the specification for various scenarios.

## PICS

## · MCORE.IDM.C

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which is the recipient of the Timed Request message - Server |
| 2 | DUT | DUT as the device which sends the Timed Request Message - Client |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Test Setup

Test will need a reference implementation of the cluster of which the DUT is the client.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.8.2.1/1 0.6.8 | MCORE. IDM.C.I nvokeR equest | DUT sends the Timed Request to the TH and then sends an Invoke Request Message to the TH after receiving the status response message from the TH. The Timed Request Message should contain a timeout value in milliseconds. (Example - 200 milliseconds) | On the TH verify the received timed request message has the timeout value as sent by the DUT. Verify that the message is unicast. Verify that the DUT sends the Invoke Request Message to the TH before the specified timeout value. Verify that the Invoke Request has TimedRequest set to True. |
| 2 | 8.7.2.2/1 0.6.8 | MCORE. IDM.C. WriteR equest | DUT sends the Timed Request to the TH and then sends a WriteRequestMessage to the TH after receiving the status response message from the TH. The Timed Request Message should contain a timeout value in milliseconds. (Example - 200 milliseconds) | On the TH verify the received timed request message has the timeout value as sent by the DUT. Verify that the message is unicast. Verify that the DUT sends the WriteRequestMessage to the TH before the specified timeout value. Verify the WriteRequestMessage has the TimedRequest field set to TRUE. |

## Notes/Testing Considerations

The DUT should have a way of triggering the Timed Request Message for Testing. Test Step #3 might not be testable.

## TC-IDM-5.2 Status Response from DUT in response to a Timed Request Action from TH. [DUT as Server]

## Purpose

Verifying that the DUT sends a status response when a Timed Request Action is received. Verifies other error conditions as well.

## PICS

## · MCORE.IDM.S

| # | Device Name | Device Description |
| 1 | TH | Test harness as device which sends the Timed Request Message - Client |
| 2 | DUT | DUT as the device which receives the Timed Request Message - Server |

## Device Topology

TH and DUT will be commissioned and are on the same fabric.

## Test Setup

TH will act as the client.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | 8.7.2.2/1 0.6.8 | | TH sends a Timed Request Message(Timed Invoke Transaction) with the timeout value set. (Example - 200 milliseconds). Wait for the status response message to be received. Wait for 5 seconds(Timer has expired) and then send the Invoke Request Message to the DUT. | If the device being certified is Matter release 1.4 or later, Verify DUT responds w/ status TIMEOUT(0x94). If the device being certified is Matter release 1.3 or earlier, verify the DUT sends back a Status response with either status TIMEOUT(0x94) or status UNSUPPORTED_ACCESS(0x7e). |

| # | Ref | PICS | Test Step | Expected Outcome |
| 4 | 8.7.2.2/1 0.6.8 | | TH sends a Timed Request Message(Timed Write Transaction) with the timeout value set. (Example - 200 milliseconds). Wait for the status response message to be received. Wait for 5 seconds(Timer has expired) and then send the Write Request Message to the DUT. | If the device being certified is Matter release 1.4 or later, Verify DUT responds w/ status TIMEOUT(0x94). If the device being certified is Matter release 1.3 or earlier, verify the DUT sends back a Status response with either status TIMEOUT(0x94) or status UNSUPPORTED_ACCESS(0x7e). |

## Notes/Testing Considerations

## 11.4.6. Events Test Cases

## TC-IDM-6.1 Events Read Interaction from TH to DUT. [DUT as Server]

## Purpose

This test case will verify the report data messages for events sent from the DUT are according to specification.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as Event reader - Client |
| 2 | DUT | DUT as Event publisher - Server |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

DUT should be setup to generate events which the TH can read.

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.4.2.1/8 .9.3.2 | | TH sends Read Request Message to DUT with EventRequests set to a specific event from a specific cluster on a specific endpoint on a specific node that is, [Node = Specific, Endpoint = Specific, Cluster = Specific, Event = Specific]. | Verify TH receives Report Data Message with the data for specific event in Read Request Message. |
| 2 | 8.4.2.1/8 .9.3.2 | | TH sends Read Request Message to DUT with EventRequests set to all events from a specific cluster on a specific endpoint on a specific node that is, [Node = Specific, Endpoint = Specific, Cluster = Specific, Event = Wildcard]. | Verify TH receives Report Data Message with the data for events in Read Request Message. |
| 4 | 8.4.2.1/8 .9.3.2 | | TH sends Read Request Message to DUT with EventRequests set to a specific event from a specific cluster on all endpoints on a specific node that is, [Node = Specific, Endpoint = Wildcard, Cluster = Specific, Event = Specific]. | Verify TH receives Report Data Message with the data for specific event in Read Request Message. |

| # | Ref | PICS | Test Step | Expected Outcome |

* Test Steps 7 and 14 cannot be executed with V1.0 SDK '''

## TC-IDM-6.2 Events Subscribe Interaction from TH to DUT. [DUT as Server]

## Purpose

This test case will verify the report data messages for events sent from the DUT are according to specification.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as Event subscriber - Client |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.5.2.1/8 .9.3.2 | | TH sends Subscribe Request Message to DUT with EventRequests set to a specific event from a specific cluster on a specific endpoint on a specific node that is, [Node = Specific, Endpoint = Specific, Cluster = Specific, Event = Specific]. | Verify TH receives Report Data Message with SubscriptionId which uniquely identifies this subscription on the publisher and data for specific event in Subscribe Request Message. |
| 2 | 8.5.2.1/8 .9.3.2 | | TH sends Subscribe Request Message to DUT with EventRequests set to all events from a specific cluster on a specific endpoint on a specific node that is, [Node = Specific, Endpoint = Specific, Cluster = Specific, Event = Wildcard]. | Verify TH receives Report Data Message with SubscriptionId which uniquely identifies this subscription on the publisher and data for events in Subscribe Request Message. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | 8.5.2.1/8 .9.3.2 | | TH sends Subscribe Request Message to DUT with EventRequests set to all events from all clusters on a specific endpoint on a specific node that is, [Node = Specific, Endpoint = Specific, Cluster = Wildcard, Event = Wildcard]. | Verify TH receives Report Data Message with SubscriptionId which uniquely identifies this subscription on the publisher and data for events in Subscribe Request Message. |
| 4 | 8.5.2.1/8 .9.3.2 | | TH sends Subscribe Request Message to DUT with EventRequests set to a specific event from a specific cluster on all endpoints on a specific node that is, [Node = Specific, Endpoint = Wildcard, Cluster = Specific, Event = Specific]. | Verify TH receives Report Data Message with SubscriptionId which uniquely identifies this subscription on the publisher and data for specific event in Subscribe Request Message. |
| 5 | 8.5.2.1/8 .9.3.2 | | TH sends Subscribe Request Message to DUT with EventRequests set to all events from a specific cluster on all endpoints on a specific node that is, [Node = Specific, Endpoint = Wildcard, Cluster = Specific, Event = Wildcard]. | Verify TH receives Report Data Message with SubscriptionId which uniquely identifies this subscription on the publisher and data for events in Subscribe Request Message. |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

* Test Step #14 cannot be executed with V1.0 SDK. '''

## TC-IDM-6.3 Events Read Interaction from DUT to TH. [DUT as Client]

## Purpose

This test case will verify the report data messages for events sent from the DUT are according to specification.

- MCORE.IDM.C
- MCORE.IDM.C.ReadRequest
- MCORE.IDM.C.ReadEvent

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as Event reader |
| 2 | TH | Test harness as Event publisher |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.4.2.1/8 .9.3.2 | | DUT sends Read Request Message to the TH for a supported event. | Verify on the TH that the Read Request Message received has these fields EventRequests - list of request paths to cluster events. Should be a valid EventPathIB from the Valid Event Paths table and not target a group. EventFilters - list of minimum event numbers per specific node. (Optional) FabricFiltered which is of type bool. |

## Notes/Testing Considerations

## TC-IDM-6.4 Events Subscribe Interaction from DUT to TH. [DUT as Client]

## Purpose

This test case will verify the report data messages for events sent from the DUT are according to specification.

## PICS

- MCORE.IDM.C
- MCORE.IDM.C.SubscribeRequest

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as Event subscriber |
| 2 | TH | Test harness as Event publisher |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Steps 3,4,5 and 6 can be optional if they cannot be tested.

## TC-IDM-7.1 Multi Fabric Subscription Test Cases. [DUT as Server]

## Purpose

This test case will verify the report data messages for subscriptions requested from devices on different fabrics are handled correctly by the DUT.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | RD1 | Reference Device 1 as the commissioner and subscriber |
| 2 | RD1A | Reference Device 1A as the subscriber |
| 3 | RD2 | Reference Device 2 as the commissioner and subscriber |

| 4 | RD3 | Reference Device 3 as the commissioner and subscriber |
| 5 | RD4 | Reference Device 4 as the commissioner and subscriber |
| 6 | RD5 | Reference Device 5 as the commissioner and subscriber |

## Device Topology

RD1, RD2, RD3, RD4, RD5 should be on separate, distinct fabrics. RD1 and RD1A should be on the same fabric.

DUT should be commissioned onto all fabrics.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | 8.5.2.1/1 2.1 | | RD1, RD2, RD3, RD4, RD5 send 3 Subscribe Request Messages to DUT.(Total - 15 active subscriptions) Each subscribe request should contain 3 different paths. They can subscribe to different attributes and events. Once all subscriptions are active, change the value of all the attributes that have been subscribed or trigger an action on the DUT to generate an event. | Verify that all Subscription Requests succeed. Verify on each of these Reference Devices that the appropriate attribute value has been received. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 4b | 8.5.2.1/1 2.1 | | RD1, RD2, RD3, RD4, RD5 send 3 Subscribe request messages each with each of them having 3 different paths. Verify that the subscription request messages from RD1, RD2, RD3, RD4 and RD5 succeed. Once all the Subscription Requests are activated, send a Subscribe request messages having 3 different paths from RD1A to the DUT. | Verify that the Subscription from RD1A gets INVALID_ACTION and the previous subscriptions from RD2, RD3, RD4 and RD5 are not affected. |

## Notes/Testing Considerations

Test Step #4 cannot be executed with V1.0 SDK.

## TC-IDM-8.1 Fabric scoped Test Cases. [DUT as Server]

## Purpose

This test case will test if the DUT handles fabric scoped/sensitive data appropriately when it's part

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | RC1 | Reference Client 1 as client |
| 2 | RC2 | Reference Client 2 as client |
| 3 | DUT | Server as the DUT [DUT as Server] |

## Device Topology

RC1 and RC2 should be on separate, distinct fabrics. DUT should be commissioned onto both fabrics.

## Test Procedure

| # | Ref | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Test Step #6 and #7 cannot be executed with V1.0 SDK.

## TC-IDM-9.1 CONSTRAINT\_ERROR status response test cases [DUT as Server] - PROVISIONAL

## Purpose

This test case will verify that the server sends a status response with CONSTRAINT\_ERROR when a particular field is out of range.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## DUT and TH are on the same fabric

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This TC is removed for Matter 1.2 release. This test case will be modified for 1.3 Step 2 needs to be automated to be run. Please use this as an example attribute till the automated test is ready. Cluster: Basic Information, Attribute name - NodeLabel, type - String, Constraint max 32

## TC-IDM-10.1 Cluster requirements - Cluster ID and Global attribute conformance checks [DUT as Server]

## Purpose

Tests global attribute presence and AttributeList correctness for every cluster on every endpoint

## PICS

## · MCORE.IDM.S

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH performs a wildcard read of all attributes and endpoints. Confirms pre-conditions are met. | |
| 2 | | | | For every cluster on every endpoint verify that the cluster includes all the mandatory global attributes: • ClusterRevision • FeatureMap |

| 3 | For every cluster on every endpoint verify that the following global attributes do not contain duplicate values and every value in the list is in the required range: • AttributeList • AcceptedCommandList • GeneratedCommandList |
| 4 | For every cluster on every endpoint, verify that each attribute reported in the AttributeList exactly matches the set of received attributes from the wildcard read. In other words, if an attribute ID is present in the AttributeList, a report for that path must have been seen in the read of step 1, and if an attribute path exists in the read of step 1, its ID must be present in the AttributeList of the associated cluster within the hierarchy. |
| 5 | For every standard cluster on every endpoint, verify that none of the global attributes contain any additional values in their standard or scoped ranges that are not defined in the cluster specification. The global attributes to be checked and their standard and scoped ranges for the are as follows: • AttributeList: (0x0000_0000 - 0x0000_4FFF) and (0x0000_F000 - 0x0000_FFFE) • AcceptedCommandList: 0x0000_0000 - 0x0000_00FF • GeneratedCommandList: |

| 6 | For every cluster on every endpoint, verify that none of the global attributes contain values with prefixes outside the allowed standard or test_vendor MEI prefix range. The disallowed range of values for all global attributes is 0xFFF5_0000 - 0xFFFF_FFFF. The range 0xFFF1_0000 - 0xFFF4_FFFF is allowed for development purposes only. The set of global attributes to be checked is as follows: • AttributeList • AcceptedCommandList • GeneratedCommandList |
| 7 | For every cluster on every endpoint, verify that none of the global attributes contain MEI values outside of the allowed suffix range. The values to be checked and the allowed range of values is as follows: * AttributeList: (0xXXXX_0000 - 0xXXXX_4FFF) and (0xXXXX_F000 - 0xXXXX_FFFE) * AcceptedCommandList: 0xXXXX_0000 - 0xXXXX_00FF * GeneratedCommandList: 0xXXXX_0000 - 0xXXXX_00FF where XXXX denotes any prefix value. The prefix of each item should be masked before |

| | 10 | | For every cluster on every endpoint, verify that if the cluster ID is in the MEI prefix range, that the suffix is in the manufacturer suffix range (0xFC00 - 0xFFFE) |
| 12 | | TH performs a wildcard read of all events. | Verify that at least one event is returned. Note that all devices will have at least one event in the buffer from either the startup event, or events that later replaced the startup event in the buffer. |

## Notes/Testing Considerations

## TC-IDM-10.2 Cluster requirements - Conformance [DUT as Server]

## Purpose

Tests cluster conformance for features, attributes and commands across all endpoints.

## PICS

## · MCORE.IDM.S

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | For every server cluster on every endpoint, verify that the cluster is not provisional in the specification | No provisional clusters are present on the DUT |
| 2a | | | For every server cluster on every endpoint, verify that all features listed in the feature map are known features from the specification | No non-spec features are present on the DUT |
| 2c | | | For every server cluster on every endpoint, for each feature listed in the FeatureMap, ensure that the feature is allowed per the conformance as assessed in step 2b | No disallowed features are present in the feature map |
| 2d | | | For every server cluster on every endpoint, for each feature present in the spec, if the feature is required per the conformance in step 2b, ensure it is present | No required features missing from the DUT |
| 3a | | | For every server cluster on every endpoint, verify that all attributes in the standard range are known attributes from the specification | No non-spec standard attributes are present on the DUT |

| 3c | For every server cluster on every endpoint, for each attribute listed in the AttributeList, ensure that the attribute is allowed per the conformance as assessed in step 3b | No disallowed attributes are present in the AttributeList |
| 3d | For every server cluster on every endpoint, for each attribute present in the spec, if the attribute is required per the conformance in step 3b, ensure it is present | No required attributes missing from the DUT |
| 4a | For every server cluster on every endpoint, verify that all commands listed in the AcceptedCommands list in the standard range are known commands from the specification | No non-spec standard commands are present in the AcceptedCommands list |
| 4c | For every server cluster on every endpoint, for each command listed in the AcceptedCommands list, ensure that the command is allowed per the conformance as assessed in step 4b | No disallowed commands are present in the AcceptedCommands |
| 4d | For every server cluster on every endpoint, for each client ⇒ server command in the spec, if the command is required per the conformance in step 4b, ensure it is present | No required AcceptedCommands are missing from the DUT |
| 5a | For every server cluster on every endpoint, verify that all commands listed in the GeneratedCommands list in the standard range are known commands from the specification | No non-spec standard commands are present in the GeneratedCommands list |

| 5c | For every server cluster on every endpoint, for each command listed in the GeneratedCommands list, ensure that the command is allowed per the conformance as assessed in step 5b | No disallowed commands are present in the GeneratedCommands |
| 5d | For every server cluster on every endpoint, for each server ⇒ client command in the spec, if the command is required per the conformance in step 5b, ensure it is present | No required GeneratedCommands are missing from the DUT |

## TC-IDM-10.3 Cluster requirements - Revision [DUT as Server]

## Purpose

Tests the cluster revisions on the DUT are the most recent per the spec.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

## TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH performs a wildcard read of all attributes and endpoints | |
| 2 | | | For every server cluster on every endpoint, ensure that the ClusterRevision is the highest cluster revision listed in the spec | No clusters have ClusterRevisions that do not match the specification |

## TC-IDM-10.4 Cluster requirements - PICS [DUT as Server]

## Purpose

Tests the PICS for clusters, features, attributes, and commands on the DUT match exactly the PICS.

## PICS

## · MCORE.IDM.S

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## NOTE

This test should be run for each endpoint on the device, using the appropriate PICS file.

## Test Procedure

| # | Test Step | Expected Outcome |
| 2 | For every standard cluster: If the cluster is present on the endpoint, ensure the server-side PICS code for the cluster is present in the PICS file (e.g. OO.S for On/Off cluster). If the cluster is not present on the endpoint, ensure the cluster server PICS code is not present in the PICS file. | PICS exactly match for server clusters. |

| 3 | For every standard cluster, for every attribute in the cluster: If the cluster is present on the endpoint and the attribute ID is present in the AttributeList global attribute within the cluster, ensure the server-side PICS code for the attribute is present in the PICS file (e.g. OO.S.A000 for On/Off cluster's OnOff attribute). Otherwise, ensure the attribute PICS code is NOT present in the PICS file. | PICS exactly match for all attributes in all clusters. |
| 8 | If the device has a root node device type on this endpoint, ensure the MCORE.ROLE.COMMISSIONEE PICS code is set | PICS is set if root node is present |

| 9 | If the device has any onboarding payload (MCORE.DD.QR or MCORE.DD.NFC), it has the manual pairing code PICS set (MCORE.DD.MANUAL_PC) | Manual pairing code PICS is set if QR or NFC is set |
| 10 | If any of the above checks failed, fail the test | |

## TC-IDM-10.5 Device Type Requirements [DUT as Server]

## Purpose

Tests that the device conforms to the device type requirements on all endpoints

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Spec Reference

DL - Device library

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH performs a wildcard read of all attributes and endpoints | |
| Repeat the following steps for each endpoint on the device: | Repeat the following steps for each endpoint on the device: | Repeat the following steps for each endpoint on the device: |
| 2a | Create an empty set called allowed_clusters | |

| # | Test Step | Expected Outcome |
| 2b | For each standard device type listed in the Descriptor device_type_list: • ensure the device type is present in the spec • ensure all the mandatory server clusters IDs are present in the Descriptor cluster ServerList • ensure no disallowed clusters are present in the Descriptor cluster ServerList • append the set of allowed clusters for this device type to allowed_clusters | Device type is part of the spec, device contains all mandatory clusters and no disallowed clusters, all element requirements for clusters on the current endpoint are met. |
| 2c | If not PIXIT.allow_extra_clusters, ensure all the clusters present in the ServerList are in allowed_clusters | No extra clusters are present |

## Notes/Testing Considerations

This test only currently assesses the cluster and element conditions for current endpoint. It does not currently assess children device types or element requirements / conditions for children endpoints or the root node.

## TC-IDM-10.6 Device Type Revisions [DUT as Server]

## Purpose

Tests that the device type revisions match the spec requirements.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Spec Reference

DL - Device library

| # | Test Step | Expected Outcome |
| 1 | TH performs a wildcard read of all attributes and endpoints | |
| Repeat the following steps for each endpoint on the device: | Repeat the following steps for each endpoint on the device: | Repeat the following steps for each endpoint on the device: |
| 2 | For each standard device type listed in the Descriptor DeviceTypeList, ensure that the revision is the highest device type revision listed in the spec | No entries in the DeviceTypeList have revisions that do not match the specification |

## TC-IDM-11.1 Data types - attribute strings [DUT as Server] - data model

## Purpose

Tests that no string attributes on the node contain invalid characters.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH performs a wildcard read of all attributes and endpoints | |
| 2 | | | For every returned attribute, if the attribute type is string and the returned value is not Null or empty, ensure the returned value is a valid UTF-8-encoded string. It is not permitted to have partially encoded codepoints between the last legally-encoded codepoint and the end of the string. | All string-type attributes are valid UTF-8. |

## TC-IDM-12.1 Device attribute information [DUT as Server]

## Purpose

This test is used to create a json file of the wildcard attribute read for certification submission.

## PICS

## · MCORE.IDM.S

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | TestStep | Expected Outcome |
| 0 | TH performs a wildcard read of all attributes and endpoints on the device. Confirms pre-conditions are met. | |

## TC-IDM-13.1 Accidental defaults check [DUT as Server]

## Purpose

This test is used to ensure that common defaults were not accidentally left on the DUT. Device manufacturers who intentionally set the default values can use the given override flags to pass this test.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | TestStep | Expected Outcome |
| 1 | TH performs a wildcard read of all attributes | |
| 2 | If the pixit_allow_test_in_product_name flag is not set, check for "Test" in the product name | "Test" does not appear in the product name |
| 3 | If the pixit_allow_test_in_vendor_name flag is not set, check for "Test" in the vendor name | "Test" does not appear in the vendor name |
| 4 | If the pixit_allow_default_vendor_id flag is not set, check for test vendor IDs | Product does not use a test vendor ID |
| 5 | If the pixit_allow_default_calendar_format flag is not set, and the TimeFormatLocalization cluster is present and has the ActiveCalendarType attribute, check for the default calendar format | Calendar format is not the default |
| 6 | If the pixit_allow_unit_testing_cluster flag is not set, check for the presence of a unit testing cluster on any endpoint | Unit testing cluster does not appear on any endpoint |
| 7 | If the pixit_allow_fault_injection_cluster flag is not set, check for the presence of a fault injection cluster on any endpoint | Fault injection cluster does not appear on any endpoint |
| 8 | If the pixit_allow_sample_mei_cluster flag is not set, check for the presence of a sample mei cluster on any endpoint | Sample MEI cluster does not appear on any endpoint |

| 9 | If the pixit_allow_empty_fixed_label_list flag is not set, and the FixedLabel cluster is present on the device, check that the fixed label cluster list is not empty | List is not empty |
| 10 | If the pixit_allow_fixed_label_default_values flag is not set, and the FixedLabel cluster is present on the device, check that the fixed label cluster list does not contain any of the default labels (default values mentioned in the spec) | List does not contain default labels |
| 11 | Fail on any problems | |

## TC-IDM-14.1 Device-type-restricted clusters check [DUT as Server]

## Purpose

This test ensures particular or complex restrictions of certain clusters in some device types are properly enforced.

## This includes:

- Restrictions on clusters that are only allowed on the root node, to ensure they do not appear on non-root-node endpoints.
- Restrictions on some clusters in other device types, where there is no other test that could generically address

the verification of those constraints.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | TestStep | Expected Outcome |
| 0 | TH performs a wildcard read of attributes and endpoints on the device | |

| 1 | For each root-node-restricted cluster in the list, ensure the cluster does not appear on any endpoint that is not the root node. List of root-node-restricted clusters: • ACL • Time Synchronization • TLS Certificate Management • TLS Client Management | No root-node-restricted clusters appear on non-root endpoints |

| Ensure the complex device type composition and conformance rules related to closure device types are met: | No cluster violating the rules appear on any endpoint where the rule applies. |
| // Don't add closures to Window Covering in 1.5 * For any endpoint whose Descriptor cluster's DeviceTypeList has the Window Covering device type with revision 5 or lower, ensure that the ServerList does not contain either the Closure Dimension or Closure Control clusters; // Don't add window covering to Closures in 1.5 * For any endpoint whose Descriptor cluster's DeviceTypeList has the Closure device type with revision 1, ensure that the ServerList does not contain the Window Covering cluster; * For any endpoint whose Descriptor cluster's DeviceTypeList has the Closure Panel device type with revision 1, ensure that the ServerList does not contain the Window Covering cluster; // Don't mix Closure Control and Closure Dimension on same endpoint, as Closure Dimension belongs on child Closure Panel and vice-versa. * For any endpoint whose Descriptor cluster's DeviceTypeList has the Closure device type with any revision, ensure that the ServerList does not contain the Closure Dimension cluster; * For any endpoint whose Descriptor cluster's DeviceTypeList has the Closure Panel device type with any revision, ensure that the ServerList does not contain the Closure Control cluster. | |

| 3 | Ensure the Closure device type semantic tag constraints are followed on any Closure or Closure Panel endpoint: • For any endpoint whose Descriptor cluster's DeviceTypeList has the Closure device type, ensure that the TagList in that endpoint's Descriptor contains one and only one tag from the Closure namespace (0x44), and no tag from the Closure Panel namespace (0x45), in addition to any other tag from other legal namespaces. • For any endpoint whose Descriptor cluster's DeviceTypeList has the Closure Panel device type, ensure that the TagList in that endpoint's Descriptor contains one and only one tag from the Closure Panel namespace (0x45), and no tag from the Closure namespace (0x44), in addition to any other tag from other legal namespaces. | Semantic tags meeting the rules appear on the necessary endpoints. |

## Chapter 12. Administrator Commissioning Cluster Test Plan

## 12.1. PICS Definition

This section covers the Multiple Fabrics Test Plan related PICS items that are referenced in the following test cases.

## 12.1.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CADMIN.S | Does the Device implement the Admin Commissioning Cluster as a server? | O | |
| CADMIN.C | Does the Device implement the Admin Commissioning Cluster as a client? | O | |

## 12.1.2. Server

## Features

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CADMIN.S.F00(BC) | Does the Device support Basic Commissioning Method | CADMIN.S:O | |

## Commands received

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CADMIN.S.C00.Rsp(Ope nCommissioningWindo w) | Does the Device support Enhanced Commissioning Method (ECM)? | CADMIN.S:M | |
| CADMIN.S.C01.Rsp(Ope nBasicCommissioning Window) | Does the Device support Basic Commissioning Method (BCM)? | CADMIN.S.F00(BC) | |

| CADMIN.S.C02.Rsp(Rev okeCommissioning) | Does the Device support revoking commissioning window? | CADMIN.S:M |

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CADMIN.S.A0000(Wind owStatus) | Does the Device support WindowStatus attribute? | CADMIN.S:M | |
| CADMIN.S.A0001(Admi nFabricIndex) | Does the Device support AdminFabricIndex attribute? | CADMIN.S:M | |
| CADMIN.S.A0002(Admi nVendorId) | Does the Device support AdminVendorId attribute? | CADMIN.S:M | |

## 12.1.3. Client

## Manual controllable

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CADMIN.C.M.UserInterf aceDisplay | Does the Device support User Interface Display | CADMIN.C:O | |
| CADMIN.C.M.AudioInte rface | Does the Device support Audio Interface | CADMIN.C:O | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CADMIN.C.C00.Tx(Open CommissioningWindo w) | Does the Device support through Enhanced Commissioning Method (ECM) ? | CADMIN.C:O | |

| CADMIN.C.C01.Tx(Open BasicCommissioningWi ndow) | Does the Device support Basic Commissioning Method (BCM) ? | CADMIN.C:O |
| CADMIN.C.C02.Tx(Revo keCommissioning) | Does the Device support revoking commissioning window? | CADMIN.C:O |

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| CADMIN.C.A0000(Wind owStatus) | Does the DUT(client) have access privileges for the WindowStatus attribute implemented on the server? | CADMIN.C:O | |
| CADMIN.C.A0001(Admi nFabricIndex) | Does the DUT(client) have access privileges for the AdminFabricIndex attribute implemented on the server? | CADMIN.C:O | |
| CADMIN.C.A0002(Admi nVendorId) | Does the DUT(client) have access privileges for the AdminVendorId attribute implemented on the server? | CADMIN.C:O | |

## 12.2. PIXIT Definition

This section covers the Multiple Fabrics Test Plan related PIXIT items that are referenced in the following test cases.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PIXIT.CADMIN.CwDura tion | PIXIT of Duration (in seconds) for a commissioning window which is greater than 179 seconds and less than 901 seconds | M | |

## 12.3. Timing and Tolerance Considerations

## NOTE

This section summarizes timing tolerances and clock allowances relevant to test cases. The same information is also present in the shared cluster\_common.adoc front matter for consistency across test plans.

There are two main types of timing tolerances:

## 1. Action-at-End Tolerance:

- Actions-at-End tolerances apply to tests that check that an action occurs at the end of a timer (e.g., a device closes a valve after a set period, a failsafe timer expires, a commissioning window is closed).
- The Action-at-End tolerance permits the expected action to occur at the expected time +/- the tolerance
- The tolerance for these actions is 1% of the set timer time or 100ms, whichever is larger

## 2. Action-Over-Time Tolerance:

- Action-over-time tolerances apply to tests where the device changes occur continuously over a set period (for example, a light bulb ramping or changing color).
- Tests checking for value changes during the ongoing operation use a larger tolerance to account for both clock differences and algorithmic differences in applying the requested changes.
- Tests that use Action-Over-Time tolerances normally apply a tolerance of 15% of the expected change, calculated as follows:

For an action started at time T ₀ with a starting value V ₀ and an action-overtime change rate C (where C = Δ V ÷ Δ T), the expected change in value Δ V ₁ at time T ₁ is:

```
Δ V ₁ = C × (T ₁ T ₀ )
```

The allowed range of expected values for V ₁ at time T ₁ is:

```
V ₁ = V ₀ ± ( Δ V ₁ × tol)
```

where *tol* is the tolerance value and is normally 0.15.

It is important to differentiate between these two types of tolerances when writing or interpreting test cases. The default clock allowance applies to action-at-end scenarios, while action-over-time tolerances should be explicitly stated where used.

## 12.3.1. Clock allowances for commissioning test cases

For tests where an action happens at the end of a specified period (for example, failsafe expiry), a clock allowance is applied, such that the result of the action is expected to occur at the expected time +/- the clock allowance. These tests use a clock allowance of 1% of the set timer time or 100ms, whichever is larger. This allowance applies to commissioning window timeouts, failsafe timeouts, and other time-based validations.

## NOTE

When a commissioning test case specify timing requirements (e.g., "after 190 seconds" or "after PIXIT.CADMIN.CwDuration + 10 seconds"), the 1% with a minimum of 100ms clock allowance applies. This means that if a test case expects a commissioning window to be closed after a specific timeout, the actual timeout may vary by up to 1% of the expected time (with a minimum of 100ms) due to clock differences between devices and network effects. Testers should account for this allowance when verifying timeout behavior in commissioning window test cases.

## 12.4. Test Case List

| TC UUID | Test Case Name |
| TC-CADMIN-1.1 | Administrator Behavior using ECM [DUT - Commissioner] |
| TC-CADMIN-1.2 | Administrator Behavior using BCM [DUT - Commissioner] |
| TC-CADMIN-1.3 | Node Behavior using ECM [DUT - Commissionee] |
| TC-CADMIN-1.4 | Node Behavior using BCM [DUT - Commissionee] |
| TC-CADMIN-1.5 | Commissioning window handling timeout and revocation using ECM [DUT - Commissionee] |
| TC-CADMIN-1.7 | Commissioning window handling timeout and revocation using ECM [DUT - Commissioner] |
| TC-CADMIN-1.8 | Commissioning window handling timeout and revocation using BCM [DUT - Commissioner] |
| TC-CADMIN-1.9 | Device exit commissioning mode after 20 failed commission attempts [ECM] [DUT - Commissionee] |
| TC-CADMIN-1.10 | Revoke Commissioning Clears out PASE Session [DUT - Commissionee] |
| TC-CADMIN-1.11 | Open commissioning window on DUT using ECM then BCM [DUT - Commissionee] |
| TC-CADMIN-1.15 | Removing Fabrics from DUT and Fabric index enumeration using ECM [DUT - Commissionee] |
| TC-CADMIN-1.17 | Removing Fabrics from DUT and Fabric index enumeration using ECM [DUT - Commissioner] |

| TC-CADMIN-1.18 | Removing Fabrics from DUT and Fabric index enumeration using BCM [DUT - Commissioner] |
| TC-CADMIN-1.19 | max number of CommissionedFabrics and SupportedFabrics rollover using ECM [DUT - Commissionee] |
| TC-CADMIN-1.22 | Open commissioning window - durations max and max+ 1 [ECM] [DUT - Commissionee] |
| TC-CADMIN-1.25 | Subscription to the attributes - verify subscription response [ECM] [DUT - Commissionee] |

## 12.5. Test Cases

## 12.5.1. Multiple Fabrics Test Cases

## TC-CADMIN-1.1 Administrator Behavior using ECM [DUT - Commissioner]

## Purpose

This test case verifies Administrators involved in a Multiple Fabrics scenario are behaving properly by fulfilling:

1. The current Node Administrator SHALL allow another Administrator to be commissioned with that Node.
2. The new Commissioner MUST have their own Node Operational Certificate (NOC) issuing Root Certificate Authority (RCA).
3. Once commissioning is completed, the new Administrator has access to the Node and can perform all administrative tasks.
4. An Administrator SHALL support pairing with a device using the mandatory method described in Section 5.6.3, "Enhanced Commissioning Method (ECM)".
5. Verification when the Commissioning Timeout parameter of the OCW command is in the correct range (&gt;=3m and ⇐ 15m).

## PICS

- CADMIN.C
- CADMIN.C.C00.Tx(OpenCommissioningWindow)

## Required Devices

| Device Name | Device Description |

| 1 | TH_CE | Test harness as Commissionee |
| 2 | TH_CR1 | Test harness as Commissioner 1 |
| 3 | DUT_CR2 | DUT as Commissioner 2 |
| 4 | TH_CR3 | Test harness as Commissioner 3 |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Reset Devices to factory defaults | |

## Device Topology

An existing Fabric should exist, with a Commissioner (TH\_CR2) that will create a new, nonconflicting fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-CADMIN-1.2 Administrator Behavior using BCM [DUT - Commissioner]

## Purpose

This test case verifies Administrators involved in a Multiple Fabrics scenario are behaving properly by fulfilling:

1. The current Node Administrator SHALL allow another Administrator to be commissioned with that Node.
2. The new Commissioner MUST have their own Node Operational Certificate (NOC) issuing Root Certificate Authority (RCA).
3. Once commissioning is completed, the new Administrator has access to the Node and can perform all administrative tasks.
4. An Administrator MAY support pairing with a device using the optional method described in Section 5.6.2, "Basic Commissioning Method (BCM)".
5. Verification when the Commissioning Timeout parameter of the OCW command is in the correct range (&gt;=3m and ⇐ 15m).

## PICS

- CADMIN.C
- CADMIN.C.C01.Tx(OpenBasicCommissioningWindow)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CE | Test harness as Commissionee |
| 2 | TH_CR1 | Test harness as Commissioner 1 |
| 3 | DUT_CR2 | DUT as Commissioner 2 |
| 4 | TH_CR3 | Test harness as Commissioner 3 |

| # | Doc. Ref. | Condition | Notes |
| 1 | | Reset Devices to factory defaults | |

## Device Topology

An existing Fabric should exist, with a Commissioner (TH\_CR2) that will create a new, nonconflicting fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-CADMIN-1.3 Node Behavior using ECM [DUT - Commissionee]

## Purpose

This test case verifies Node behavior in a Multiple Fabrics scenario:

1. The Node SHALL host an "Administrator Commissioning Cluster" Section 11.18
2. The Cluster exposes a command which enables the entry into commissioning mode for a prescribed time, and which SHALL be invoked over a secure channel.
3. During this commissioning window, the Node SHALL maintain its existing configuration, such as its operational network connection and identities, and SHOULD allow normal interactions from other Nodes.
4. Verification when the Commissioning Timeout parameter of the OCW command is in the correct range (&gt;=3m and ⇐ 15m).

## Spec References

C.11.19 - Administrator commissioning cluster C.11.18 - Operational credentials cluster

## PICS

## · CADMIN.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CR2 | Test harness as Commissioner 2 on a different fabric |
| 3 | DUT_CE | DUT - Commissionee |

## Device Topology

An existing Fabric should exist, with a Commissioner (TH\_CR1) that will create a new, nonconflicting fabric.

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH_CR1 starts a commissioning process with DUT_CE | DUT_CE is commissioned by TH_CR1 on Fabric ID1 and is assigned a node ID1, under TH_CR1's root of trust. |
| 2 | TH_CR1 reads the BasicCommissioningInfo attribute from the General Commissioning cluster and saves the MaxCumulativeFailsafeSeconds field as max_window_duration . | |

| 3.b | DNS-SD records shows DUT_CE advertising | Verify that the DNS-SD advertisement shows CM=2 |
| 3.c | TH_CR1 writes and reads the Basic Information Cluster's NodeLabel mandatory attribute of DUT_CE | Verify DUT_CE responds to both write/read with a success |
| 4 | TH creates a controller (TH_CR2) on a new fabric and commissions DUT_CE using that controller. TH_CR2 should commission the device using a different NodeID than TH_CR1. | Commissioning is successful |
| 5 | TH_CR1 reads the Fabrics attribute from the Node Operational Credentials cluster using a fabric-filtered read | Verify that the RootPublicKey matches the root public key for TH_CR1 and the NodeID matches the node ID used when TH_CR1 commissioned the device. |
| 6 | TH_CR2 reads the Fabrics attribute from the Node Operational Credentials cluster using a fabric-filtered read | Verify that the RootPublicKey matches the root public key for TH_CR2 and the NodeID matches the node ID used when TH_CR2 commissioned the device. |
| 7 | TH_CR1 writes and reads the Basic Information Cluster's NodeLabel mandatory attribute of DUT_CE | Verify DUT_CE responds to both write/read with a success |
| 8 | TH_CR2 reads, writes and then reads the Basic Information Cluster's NodeLabel mandatory attribute of DUT_CE | Verify the initial read reflect the value written in the above step. Verify DUT_CE responds to both write/read with a success |
| 9 | TH_CR2 opens a commissioning window on DUT_CE for 180 seconds using ECM and monitors until the window closes to verify window timing | Verify that the window closed within the expected duration of 180 seconds + 1.8 seconds of clock skew |
| 10 | TH_CR2 opens a commissioning window on DUT_CE using ECM | DUT_CE opens its Commissioning window to allow a new commissioning |

| 11 | TH_CR1 starts a commissioning process with DUT_CE before the timeout from step 10 | Since DUT_CE was already commissioned by TH_CR1 in step 1, AddNOC fails with NOCResponse with StatusCode field set to FabricConflict (9) |
| 12 | TH_CR1 sends an RevokeCommissioning command to the DUT to cleanup step 11 | Verify DUT responds w/ status SUCCESS(0x00) |
| 13 | TH_CR2 reads the CurrentFabricIndex attribute from the Operational Credentials cluster and saves as th2_idx, TH_CR1 sends the RemoveFabric command to the DUT with the FabricIndex set to th2_idx | |

## Notes/Testing Considerations

## TC-CADMIN-1.4 Node Behavior using BCM [DUT - Commissionee]

## Purpose

This test case verifies Node behavior in a Multiple Fabrics scenario:

1. The Node SHALL host a Section 11.22, "Administrator Commissioning Cluster".
2. The Cluster exposes a command which enables the entry into commissioning mode for a prescribed time, and which SHALL be invoked over a secure channel.
3. During this commissioning window, the Node SHALL maintain its existing configuration, such as its operational network connection and identities, and SHOULD allow normal interactions from other Nodes.
4. Verification when the Commissioning Timeout parameter of the OCW command is in the correct range (&gt;=3m and ⇐ 15m).

Spec References

C.11.19 - Administrator commissioning cluster

C.11.18 - Operational credentials cluster

## PICS

## · CADMIN.S.F00

## Required Devices

| Device Name | Device Description |

| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CR2 | Test harness as Commissioner 2 on a different fabric |
| 3 | DUT_CE | DUT - Commissionee |

## Device Topology

An existing Fabric should exist, with a Commissioner (TH\_CR1) that will create a new, nonconflicting fabric.

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH_CR1 starts a commissioning process with DUT_CE | DUT_CE is commissioned by TH_CR1 on Fabric ID1 and is assigned a node ID1, under TH_CR1's root of trust. |
| 2 | TH_CR1 reads the BasicCommissioningInfo attribute from the General Commissioning cluster and saves the MaxCumulativeFailsafeSeconds field as max_window_duration . | |
| 3.b | DNS-SD records shows DUT_CE advertising | Verify that the DNS-SD advertisement shows CM=1 |
| 3.c | TH_CR1 writes and reads the Basic Information Cluster's NodeLabel mandatory attribute of DUT_CE | Verify DUT_CE responds to both write/read with a success |
| 4 | TH creates a controller (TH_CR2) on a new fabric and commissions DUT_CE using that controller. TH_CR2 should commission the device using a different NodeID than TH_CR1. | Commissioning is successful |

| 5 | TH_CR1 reads the Fabrics attribute from the Node Operational Credentials cluster using a fabric-filtered read | Verify that the RootPublicKey matches the root public key for TH_CR1 and the NodeID matches the node ID used when TH_CR1 commissioned the device. |
| 6 | TH_CR2 reads the Fabrics attribute from the Node Operational Credentials cluster using a fabric-filtered read | Verify that the RootPublicKey matches the root public key for TH_CR2 and the NodeID matches the node ID used when TH_CR2 commissioned the device. |
| 7 | TH_CR2 reads the CurrentFabricIndex attribute from the Operational Credentials cluster and saves as th2_idx, TH_CR1 sends the RemoveFabric command to the DUT with the FabricIndex set to th2_idx | TH_CR1 removes TH_CR2 fabric using th2_idx |

## Notes/Testing Considerations

## TC-CADMIN-1.5 Commissioning window handling timeout and revocation using ECM [DUT Commissionee]

## Purpose

This test case verifies the commissioning windows is open only during the expected time and can be revoked at any time.

## PICS

## · CADMIN.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | DUT_CE | DUT_CE - Commissionee |

## Preconditions

| Doc. Ref. | Condition | Notes |

| 1 | Reset Devices to factory defaults |

## Device Topology

An existing Fabric should exist, with a Commissioner (TH\_CR1) that will create a new, nonconflicting fabric.

## Specification References

## C.11.19: Administrator commissioning cluster

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | Commission DUT to TH_CR1 (can be skipped if done in a preceding test) | |
| 2 | TH_CR1 opens a commissioning window on DUT_CE using a commissioning timeout of 180 seconds using ECM | |
| 3 | TH_CR1 finds DUT_CE advertising as a commissionable node on DNS- SD | Verify that the DNS-SD advertisement TXT record shows CM=2 |
| 4 | TH_CR2 attempts to start a commissioning process with DUT_CE after 190 seconds | TH_CR2 should fail to commission the DUT since the window should be closed. This may be a failure to find the commissionable node or a failure to establish a PASE connection. |
| 5 | TH_CR1 opens a new commissioning window on DUT_CE using a commissioning timeout of 180 seconds using ECM | Verify DUT responds w/ status SUCCESS(0x00) |
| 6 | TH_CR1 revokes the commissioning window on DUT_CE using RevokeCommissioning command | Verify DUT responds w/ status SUCCESS(0x00) |

| 7 | TH_CR2 attempts to start a commissioning process with DUT_CE | TH_CR2 should fail to commission the DUT since the window should be closed. This may be a failure to find the commissionable node or a failure to establish a PASE connection. |
| 9 | TH_CR1 opens a new commissioning window on DUT_CE using a commissioning timeout of 180 seconds using ECM with the iterations field set to 999 | Verify DUT_CE fails to open Commissioning window with status code 3 (PakeParameterError) |
| 10 | TH_CR1 opens a new commissioning window on DUT_CE using a commissioning timeout of 180 seconds using ECM with the iterations field set to 100001 | Verify DUT_CE fails to open Commissioning window with status code 3 (PakeParameterError) |
| 11 | TH_CR1 opens a new commissioning window on DUT_CE using a commissioning timeout of 180 seconds using ECM with the salt set to "too_short" | Verify DUT_CE fails to open Commissioning window with status code 3 (PakeParameterError) |
| 12 | TH_CR1 opens a new commissioning window on DUT_CE using a commissioning timeout of 180 seconds using ECM with the salt set to "this pake salt very very very long" | Verify DUT_CE fails to open Commissioning window with status code 3 (PakeParameterError) |
| 13 | TH_CR1 opens a new commissioning window on DUT_CE using a commissioning timeout of PIXIT.CADMIN.CwDuration seconds using ECM | Verify DUT_CE opens its Commissioning window to allow a second commissioning |

| 14 | TH_CR1 opens another commissioning window on DUT_CE using a commissioning timeout of PIXIT.CADMIN.CwDuration seconds using ECM | Verify DUT_CE fails to open Commissioning window with status code 2 (Busy) |
| 15 | TH_CR2 starts a commissioning process with DUT_CE | Commissioning is successful |
| 16 | TH_CR1 tries to revoke the commissioning window on DUT_CE using RevokeCommissioning command | Verify DUT_CE fails to revoke giving status code 4 (WindowNotOpen) as there was no window open |
| 17 | TH_CR1 sends the RemoveFabric command to the DUT to remove TH_CR2 fabric | TH_CR1 removes TH_CR2 fabric |

## Notes/Testing Considerations

## TC-CADMIN-1.7 Commissioning window handling timeout and revocation using ECM [DUT Commissioner]

## Purpose

This test case verifies the commissioning windows is open only during the expected time and can be revoked at any time.

## PICS

- CADMIN.C
- CADMIN.C.C00.Tx(OpenCommissioningWindow)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CE | Test harness as Commissionee |
| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | DUT_CR1 | DUT - Commissioner 1 |
| 4 | TH_CR3 | Test harness as Commissioner 3 |

## Preconditions

| # | Doc. Ref. | Condition | Notes |

| 1 | Reset Devices to factory defaults |

## Device Topology

An existing Fabric should exist, with a Commissioner (TH\_CR2) that will create a new, nonconflicting fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-CADMIN-1.8 Commissioning window handling timeout and revocation using BCM [DUT Commissioner]

## Purpose

This test case verifies the commissioning windows is open only during the expected time and can be revoked at any time.

- CADMIN.C
- CADMIN.C.C01.Tx(OpenBasicCommissioningWindow)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CE | Test harness as Commissionee |
| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | DUT_CR1 | DUT - Commissioner 1 |
| 4 | TH_CR3 | Test harness as Commissioner 3 |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Reset Devices to factory defaults | |

## Device Topology

An existing Fabric should exist, with a Commissioner (TH\_CR2) that will create a new, nonconflicting fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-CADMIN-1.9 Device exit commissioning mode after 20 failed commission attempts [ECM] [DUT - Commissionee]

## Purpose

This test case verifies the DUT exits its commissioning window after the 20 failed commissioning attempts.

## PICS

## · CADMIN.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | DUT | DUT - Commissionee |

## Spec References

## C.13.3 - Exit commissioning mode after 20 failed attempts

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | Commission DUT to TH_CR1 (can be skipped if done in a preceding test) | |

| 2 | TH_CR1 reads the BasicCommissioningInfo attribute from the General Commissioning cluster on EP0 and saves the MaxCumulativeFailsafeSeconds as timeout | |
| 3 | TH_CR1 sends an OpenCommissioningWindow command to the DUT with the CommissioningTimeout set to timeout | Verify DUT responds w/ status SUCCESS(0x00) |
| 6 | TH_CR1 sends an OpenCommissioningWindow command to the DUT with the CommissioningTimeout set to timeout | Verify DUT responds w/ status SUCCESS(0x00) |
| 7 | TH_CR1 sends an RevokeCommissioning command to the DUT | Verify DUT responds w/ status SUCCESS(0x00) |

## TC-CADMIN-1.10 Revoke Commissioning Clears out PASE Session [DUT - Commissionee]

## Purpose

This test case verifies that the DUT clears out its PASE session when the RevokeCommissioning command is received.

## PICS

- CADMIN.S

| # | Doc. Ref. | Condition | Notes |
| 1 | | TH1 and DUT are commissioned | |
| 2 | | DUT's Matter Version is 1.5.1 or above | Verify that the SpecificationVersion attribute from Basic Information Cluster is equal to or greater than 1.5.1 |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH1 | Test harness as Commissioner 1 |
| 2 | TH2 | Test harness as Commissioner 2 |
| 3 | DUT | DUT - Commissionee |

## Spec References

## C.11.19.8.3 - Revoke Commissioning Command

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH1 sends an OpenCommissioningWindow command, to allow TH2 to establish a PASE session with the DUT | |
| 2 | TH2 establishes a PASE session with DUT | |
| 3 | Read VendorName from BasicInformation Cluster using TH2 over PASE, to ensure PASE session is established | Verify that the read is successful, and VendorName is present in the response |
| 4 | TH1 Sends RevokeCommissioning command (over CASE) to clear PASE session on DUT | |
| 5 | Ensure that the PASE Session got cleared, by attempting to read VendorName using TH2 (over PASE) | Verify that attempting to read VendorName attribute over PASE results in a timeout error. |

| 6 | recreate Second Controller; to establish a new PASE session and repeat test, but sending RevokeCommissioning over PASE this time | |
| 7 | TH1 sends an OpenCommissioningWindow command to DUT, to allow TH2 to establish a PASE session with the DUT | |
| 8 | TH2 establishes a PASE session with DUT | |
| 9 | TH2 Sends RevokeCommissioning command (Over PASE) to clear PASE session on DUT | |
| 10 | Ensure that the PASE Session got cleared, by attempting to read VendorName using TH2 (over PASE) | Verify that attempting to read VendorName attribute over PASE results in a timeout error |

## TC-CADMIN-1.11 Open commissioning window on DUT twice using ECM then BCM [DUT Commissionee]

## Purpose

This test case verifies DUT successfully rejects the OCW when it is already available for commissioning during PIXIT.CADMIN.CwDuration.

## PICS

## · CADMIN.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | DUT_CE | DUT - Commissionee |

## Spec References

## C.11.19.8 - Administrator commissioning commands

| # | Test Step | Expected Outcome |
| 1 | Commission DUT to TH_CR1 (can be skipped if done in a preceding test) | |
| 2 | TH_CR1 reads the BasicCommissioningInfo attribute from the General Commissioning cluster on EP0 and saves the MaxCumulativeFailsafeSeconds as timeout | |
| 3 | TH_CR1 sends an OpenCommissioningWindow command to the DUT with the CommissioningTimeout set to timeout | Verify DUT responds w/ status SUCCESS(0x00) |
| 4 | TH_CR2 fully commissions the DUT | Commissioning is successful |
| 5 | TH_CR1 sends an OpenCommissioningWindow command to the DUT with the CommissioningTimeout set to timeout | Verify DUT responds w/ status SUCCESS(0x00) |
| 6 | TH_CR1 sends an OpenCommissioningWindow command to the DUT with the CommissioningTimeout set to timeout | Verify DUT responds w/ status BUSY(0x9c) |
| 7 | TH_CR2 sends an OpenCommissioningWindow command to the DUT with the CommissioningTimeout set to timeout | Verify DUT responds w/ status BUSY(0x9c) |
| 8 | TH_CR1 sends an RevokeCommissioning command to the DUT | Verify DUT responds w/ status SUCCESS(0x00) |

| 9 | TH_CR1 reads the FeatureMap from the Administrator Commissioning Cluster. If the feature map includes the BC feature bit, repeat steps 5-8 using the OpenBasicCommissioningWind ow command | |
| 10 | TH_CR2 reads the CurrentFabricIndex attribute from the Node Operational Credentials cluster and saves as th2_idx | |
| 11 | TH_CR1 sends the RemoveFabric command to the DUT with the FabricIndex set to th2_idx | Verify DUT responds w/ status SUCCESS(0x00) |

## Notes/Testing Considerations

## TC-CADMIN-1.15 Removing Fabrics from DUT and Fabric index enumeration using ECM [DUT - Commissionee]

## Purpose

This test case verifies the removal of Fabrics.

## PICS

## · CADMIN.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CR2 | Test harness as Commissioner 2 on a different fabric than TH_CR1 and TH_CR3 |
| 3 | TH_CR3 | Test harness as Commissioner 3 on a different fabric than TH_CR1 and TH_CR2 |
| 4 | DUT_CE | DUT - Commissionee |

## Device Topology

## TH\_CR1 and DUT\_CE on the same Fabric

| # | Test Step | Expected Outcome |
| 1 | Commission DUT to TH_CR1 (can be skipped if done in a preceding test) | |
| 3 | TH_CR1 reads the Fabrics attribute from the Node Operational Credentials cluster using a non-fabric-filtered read. Save the number of fabrics in the list as initial_number_of_fabrics | |
| 4 | TH_CR1 send an OpenCommissioningWindow command to DUT_CE using a commissioning timeout of max_window_duration | Verify DUT responds w/ status SUCCESS(0x00) |
| 5 | TH_CR2 commissions DUT_CE | Commissioning is successful |
| 6 | TH_CR1 send an OpenCommissioningWindow command to DUT_CE using a commissioning timeout of max_window_duration | Verify DUT responds w/ status SUCCESS(0x00) |
| 7 | TH_CR3 commissions DUT_CE | Commissioning is successful |
| 8 | TH_CR2 reads the Fabrics attribute from the Node Operational Credentials cluster using a non-fabric-filtered read | Verify the list shows initial_number_of_fabrics + 2 fabrics |
| 10 | TH_CR2 reads the CurrentFabricIndex from the Node Operational Credentials cluster and saves as fabric_idx_cr2 | |
| 11 | TH_CR2 sends RemoveFabric with FabricIndex = fabric_idx_cr2 command to DUT_CE | Note that a response may NOT come to this command as the fabric being removed matches the sending fabric. Removal is confirmed in the following steps. |
| 12 | TH_CR2 reads the Basic Information Cluster's NodeLabel attribute of DUT_CE | Verify read/write commands fail as expected since the DUT_CE is no longer on the network |

| 14 | TH_CR1 send an OpenCommissioningWindow command to DUT_CE using a commissioning timeout of max_window_duration | Verify DUT responds w/ status SUCCESS(0x00) |
| 15 | TH_CR2 commissions DUT_CE | Commissioning is successful |
| 16 | TH_CR2 reads the Fabrics attribute from the Node Operational Credentials cluster using a non-fabric-filtered read | Verify the list shows initial_number_of_fabrics + 2 fabrics and fabric_idx_cr2 is not included, since a new fabric index should have been allocated. |
| 17 | TH_CR2 reads the CurrentFabricIndex from the Node Operational Credentials cluster and saves as fabric_idx_cr2_2 | |
| 18 | TH_CR3 reads the CurrentFabricIndex from the Node Operational Credentials cluster and saves as fabric_idx_cr3 | |
| 19 | TH_CR1 sends RemoveFabric with FabricIndex = fabric_idx_cr2_2 command to DUT_CE | Verify DUT_CE responses with NOCResponse with a StatusCode OK |
| 20 | TH_CR1 sends RemoveFabric with FabricIndex = fabric_idx_cr3 command to DUT_CE | Verify DUT_CE responses with NOCResponse with a StatusCode OK |

## TC-CADMIN-1.17 Removing Fabrics from DUT and Fabric index enumeration using ECM [DUT - Commissioner]

## Purpose

This test case verifies the removal of Fabrics.

## PICS

- CADMIN.C
- CADMIN.C.C00.Tx(OpenCommissioningWindow)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CE | Test harness as Commissionee |

| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | TH_CR3 | Test harness as Commissioner 3 |
| 4 | DUT_CR1 | DUT - Commissioner 1 |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Reset Devices to factory defaults | |

## Device Topology

## TH\_CE and DUT\_CR1 on the same Fabric

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-CADMIN-1.18 Removing Fabrics from DUT and Fabric index enumeration using BCM [DUT - Commissioner]

## Purpose

This test case verifies the removal of Fabrics.

## PICS

- CADMIN.C
- CADMIN.C.C01.Tx(OpenBasicCommissioningWindow)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CE | Test harness as Commissionee |

| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | TH_CR3 | Test harness as Commissioner 3 |
| 4 | DUT_CR1 | DUT - Commissioner 1 |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Reset Devices to factory defaults | |

## Device Topology

## TH\_CE and DUT\_CR1 on the same Fabric

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-CADMIN-1.19 max number of Commissioned Fabrics and SupportedFabrics rollover using ECM [DUT - Commissionee]

## Purpose

This test case verifies the max number of CommissionedFabrics based on SupportedFabrics. If the device already has the CommissionedFabrics attribute equal to the SupportedFabrics attribute, then the device's operational credentials table is considered full and the device SHALL process the error by responding with a StatusCode of TableFull as described in Section 11.17.7.7.2, "Handling Errors".

## PICS

- CADMIN.S

## Spec References

## C.11.19 - Administrator commissioning cluster C.11.18 - Operational credentials cluster

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CRn | Test harness as Commissioner n (multiple) |
| 3 | DUT_CE | DUT - Commissionee |

## Device Topology

## TH\_CR1 and DUT\_CE on the same Fabric

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | Commission DUT to TH_CR1 (can be skipped if done in a preceding test) | |
| 3 | TH_CR1 reads the Fabrics attribute from the Node Operational Credentials cluster using a non-fabric-filtered read. Save the number of fabrics in the list as initial_number_of_fabrics | |
| 4 | TH_CR1 reads the SupportedFabrics attribute from the Node Operational Credentials cluster. Save max_fabrics | Verify that max_fabrics is larger than initial_number_of_fabrics . If not, instruct the tester to remove one non-test-harness fabric and re-start the test. |
| 5 | Repeat the following steps (5a and 5b) max_fabrics - initial_number_of_fabrics times: | |
| 5a | TH_CR1 send an OpenCommissioningWindow command to DUT_CE using a commissioning timeout of max_window_duration | Verify DUT responds w/ status SUCCESS(0x00) |
| 5b | TH creates a controller on a new fabric and commissions DUT_CE using that controller | Commissioning is successful |

| 5c | The controller reads the CurrentFabricIndex from the Node Operational Credentials cluster. Save in list "fabric_indexes" | |
| 5d | Shutdown the created fabrics from test step 5b in order to not fill up the fabrics table on TH | |
| 7 | TH_CR1 send an OpenCommissioningWindow command to DUT_CE using a commissioning timeout of max_window_duration | Verify DUT responds w/ status SUCCESS(0x00) |
| 8 | TH creates a controller on a new fabric and commissions DUT_CE using that controller | Verify DUT_CE responds with NOCResponse with a StatusCode field value of TableFull(5) |
| 9 | TH_CR1 sends the RemoveFabric command to DUT_CE with FabricIndex set to iterate through "fabric_indexes" list | Verify DUT responds w/ status SUCCESS(0x00) |

## Notes/Testing Considerations

## TC-CADMIN-1.22 Open commissioning window - durations max max+1 and min-1 [ECM] [DUT - Commissionee]

## Purpose

This test case verifies when the Commissioning Timeout parameter of the OCW command is NOT set to less than the allowed maximum (15 minutes) therefore supporting 15 minutes, Also verifies when the Commissioning Timeout parameter of the OCW command is shorter to the minimum value (3m or 180s).

## PICS

- CADMIN.S

## Spec References

## C.11.19 - Administrator commissioning cluster

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner |
| 2 | DUT_CE | DUT - Commissionee |

## Device Topology

## TH\_CR1 and DUT\_CE on the same Fabric

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH_CR1 starts a commissioning process with DUT_CE | DUT_CE is commissioned by TH_CR1 |
| 2 | TH_CR1 opens a commissioning window on DUT_CE using ECM with a value of 900 seconds | DUT_CE returns SUCCESS |
| 3 | TH_CR1 sends an RevokeCommissioning command to the DUT | |
| 4 | TH_CR1 reads the window status to verify the DUT_CE window is closed | DUT_CE windows status shows the window is closed |
| 5 | TH_CR1 opens a commissioning window on DUT_CE using ECM with a value of 901 seconds | DUT_CE returns INVALID_COMMAND |
| 6 | TH_CR1 reads the window status to verify the DUT_CE window is closed | DUT_CE windows status shows the window is closed |
| 7 | TH_CR1 opens a commissioning window on DUT_CE using ECM with a value of 180 seconds | DUT_CE returns SUCCESS |
| 8 | TH_CR1 sends an RevokeCommissioning command to the DUT | |
| 9 | TH_CR1 opens a commissioning window on DUT_CE using ECM with a value of 179 seconds | DUT_CE returns INVALID_COMMAND |
| 10 | TH_CR1 reads the window status to verify the DUT_CE window is closed | DUT_CE windows status shows the window is closed |

## TC-CADMIN-1.25 Subscription to the attributes - verify subscription response [ECM] [DUT Commissionee]

## Purpose

This test case verifies response to the Subscription to attributes when commissioning window is opened or closed

## Spec References

C.11.19 - Administrator commissioning cluster

## PICS

## · CADMIN.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_CR1 | Test harness as Commissioner 1 |
| 2 | TH_CR2 | Test harness as Commissioner 2 |
| 3 | DUT_CE | DUT - Commissionee |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | Reset Devices to factory defaults | |

## Device Topology

TH\_CR1, TH\_CR2 and DUT\_CE on the same Fabric

## Test Procedure

| # | Ref | Test Step | Expected Outcome |

## Notes/Testing Considerations

## Chapter 13. Bridge Test Plan

## 13.1. PICS Definition

This section covers the bridge related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

## 13.1.1. DUT server

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.BRIDGE | Does the DUT implement a Bridge | Optional | |
| MCORE.BRIDGE.BatInfo | Does the DUT have information on battery level of (at least some of) of its bridged devices | MCORE.BRIDGE:Option al | |
| MCORE.BRIDGE.OtherC ontrol | Does the DUT have means to change the state of (at least some of) of its bridged devices, e.g. through a manufacturer-provided app | MCORE.BRIDGE:Option al | |
| MCORE.BRIDGE.AllowD eviceRename | Does the DUT have means to change the name of (at least some of) of its bridged devices, e.g. through a manufacturer-provided app | MCORE.BRIDGE:Option al | |

## 13.1.2. DUT client

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.BRIDGECLIENT | Does the DUT support a Bridge | O | |
| MCORE.DEVLIST.UseDe vices | Does the DUT support to maintain a list of connected devices | O | |

| MCORE.DEVLIST.UseDe viceName | Does the DUT support to maintain the names of connected devices | O |
| MCORE.DEVLIST.UseDe viceState | Does the DUT support to maintain the state of connected devices | O |
| MCORE.DEVLIST.UseBa tInfo | Does the DUT support maintaining information on battery level of connected devices | O |

## 13.2. Test Case List

| TC UUID | Test Case Name |
| TC-BR-1 | Basics of bridging (DUT server) |
| TC-BR-2 | Changing the set of bridged devices (DUT server) |
| TC-BR-3 | Changing name and state of a bridged device (DUT server) |
| TC-BR-4 | DUT client handling of bridges |
| TC-BR-5 | Conditions for Fabric Synchronization (DUT server) |

## 13.3. Test Cases

## 13.3.1. Bridge Test Cases

## TC-BR-1 Basics of bridging (DUT server)

## Purpose

This test case verifies the basic principles of bridging.

## PICS

## · MCORE.BRIDGE

## Precondition

| # | Doc. Ref. | Condition | Notes |

| DUT (bridge) has been commissioned to TH | 1 |
| Two or more bridged devices of a supported type connected via non- Matter network/protocol to DUT (bridge). If the bridge supports both actuator and sensor/switch devices, use at least one of each type | 2 |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as Administrator, Controller |
| 2 | DUT | DUT (bridge with some bridged devices) |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Manufacturer has provided bridge as DUT with some devices it can bridge, along with means to setup the bridge (e.g. add/remove/rename/group bridged devices).

## Test Procedure

| # Ref | PICS Test Step | Expected Outcome |
| 1: check exposed device types | 1: check exposed device types | 1: check exposed device types |

| 2: check present endpoints, and search bridged devices | 2: check present endpoints, and search bridged devices | 2: check present endpoints, and search bridged devices | 2: check present endpoints, and search bridged devices | 2: check present endpoints, and search bridged devices |

| 4: check battery information for bridged devices | 4: check battery information for bridged devices | 4: check battery information for bridged devices | 4: check battery information for bridged devices | 4: check battery information for bridged devices |
| 5: collect device types of bridged devices | 5: collect device types of bridged devices | 5: collect device types of bridged devices | 5: collect device types of bridged devices | 5: collect device types of bridged devices |
| 6: Set the state of a bridged device (actuator) | 6: Set the state of a bridged device (actuator) | 6: Set the state of a bridged device (actuator) | 6: Set the state of a bridged device (actuator) | 6: Set the state of a bridged device (actuator) |

| 7: Read the state of a bridged device (sensor/switch) | 7: Read the state of a bridged device (sensor/switch) | 7: Read the state of a bridged device (sensor/switch) | 7: Read the state of a bridged device (sensor/switch) | 7: Read the state of a bridged device (sensor/switch) |

## Notes/Testing Considerations

## TC-BR-2 Changing the set of bridged devices (DUT server)

## Purpose

This test case verifies the functionality of the bridge when bridged devices are being added or deleted.

## PICS

## · MCORE.BRIDGE

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT has been commissioned to TH | |
| 2 | | Two or more bridged devices of a supported type connected via non- Matter network/protocol to DUT (bridge) | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as Administrator, Controller |
| 2 | DUT | DUT (bridge with some bridged devices) |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Manufacturer has provided bridge as DUT with some devices it can bridge, along with means to setup the bridge (e.g. add/remove/rename/group bridged devices).

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1: preparation | 1: preparation | 1: preparation | 1: preparation | 1: preparation |

| 2: add a bridged device | 2: add a bridged device | 2: add a bridged device | 2: add a bridged device | 2: add a bridged device |

| 3: check newly added bridged device | 3: check newly added bridged device | 3: check newly added bridged device | 3: check newly added bridged device | 3: check newly added bridged device |
| 4: remove a bridged device | 4: remove a bridged device | 4: remove a bridged device | 4: remove a bridged device | 4: remove a bridged device |
| restart DUT to check if endpoint allocation does not get impacted by that | restart DUT to check if endpoint allocation does not get impacted by that | restart DUT to check if endpoint allocation does not get impacted by that | restart DUT to check if endpoint allocation does not get impacted by that | restart DUT to check if endpoint allocation does not get impacted by that |
| 4z | | MCORE. BRIDGE | restart the DUT | |

| 5b | | | Read the PartsList and DeviceTypeList attributes in the Descriptor cluster on endpoint 0 | • Verify that DeviceTypeList has not changed compared to step 1a • Verify that PartsList contains exactly one endpoint which previously (4b) was not present • Verify the new endpoint is higher than the previously used highest endpoint number, and different from the endpoint previously (in step 1) assigned to this bridged device • Verify that the endpoints for the other previously present bridged devices have not |
| 5c | | | Repeat step 5b for endpoint found in step 1b (the Aggregator EP) | similar as 5b (compare to results from 4c) |
| 5d | | | Read PartsList and DeviceTypeList attributes of the Descriptor cluster of all other endpoints listed in the PartsList attribute in the Descriptor cluster of endpoint 0 | Verify that the contents did not change (i.e. equal to result from step 1 for the original set of bridged devices resp. result from step 2 for the device added in step 2; for the device removed in step 4 and re-added in step 5, only verify that the DeviceTypeList attribute did not change, even though it is now at the new endpoint) |

## Notes/Testing Considerations

## TC-BR-3 Changing name and state of a bridged device (DUT server)

## Purpose

This test case verifies the functionality of the bridge when bridged devices are renamed or operated using non-Matter means.

## · MCORE.BRIDGE

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT has been commissioned to TH | |
| 2 | | Two or more bridged devices of a supported type connected via non- Matter network/protocol to DUT (bridge) | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as Administrator, Controller |
| 2 | DUT | DUT (bridge with some bridged devices) |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Manufacturer has provided bridge as DUT with some devices it can bridge, along with means to setup to bridge (e.g. add/remove/rename/group bridged devices).

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1: Rename a bridged device | 1: Rename a bridged device | 1: Rename a bridged device | 1: Rename a bridged device | |

| 1a | 9.13.3, 9.13.7 | MCORE. BRIDGE & MCORE. BRIDGE | Get the name of a bridged device: Read the NodeLabel attribute of the Bridged Device Basic Information cluster on the applicable endpoint | (Retrieved name will be used in 1c.) |
| 1b | 9.13.3, 9.13.7 | .AllowD eviceRe name | Using manufacturer provided means (i.e. NOT using Matter protocol), update the name of this bridged device | |
| 1c | 9.13.3, 9.13.7 | .AllowD eviceRe name | Read the NodeLabel attribute of the Bridged Device Basic Information cluster on the same endpoint as in 1a | Verify that the name has changed accordingly (i.e. matching what was entered in 1b and not equal to what was read in 1a) |
| 2: Change the state of a bridged device by other means | 2: Change the state of a bridged device by other means | 2: Change the state of a bridged device by other means | 2: Change the state of a bridged device by other means | 2: Change the state of a bridged device by other means |

## Notes/Testing Considerations

## TC-BR-4 DUT client handling of bridges (DUT client)

## Purpose

This test case verifies the basic principles of bridging - including the handling of DUT of composed devices, and changes in endpoints being exposed.

## PICS

## · MCORE.BRIDGECLIENT

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (client) has been not yet been commissioned to TH | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness simulating a bridge with some bridged devices; can use the bridge-app for this purpose |
| 2 | DUT | DUT (client and commissioner) |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH simulates a bridge with some bridged devices; can use the bridge-app for this purpose. bridge-app is provided with in the examples folder of the repo https://github.com/project-chip/ connectedhomeip.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1: verify DUT client gathers, uses and maintains information about endpoints | 1: verify DUT client gathers, uses and maintains information about endpoints | 1: verify DUT client gathers, uses and maintains information about endpoints | 1: verify DUT client gathers, uses and maintains information about endpoints | 1: verify DUT client gathers, uses and maintains information about endpoints |

| 1a | | • Start bridge-app on TH. • Commission TH to DUT. • Monitor traffic between DUT and TH. | Verify DUT reads relevant information from the various endpoints of TH: • DUT is expected to read DeviceTypeList and PartsList from all available endpoints • Default setup of bridge-app has endpoints 1..13: ◦ EP 1 = aggregator ◦ EP 3,10,11,12,13 = On/Off light (5 lights in total) ◦ EP 4,5 = Temperature Sensor ◦ EP 6..9 = composed ▪ EP 6 = top of composed device (battery powered device with two temperature sensors) ▪ EP 7,8 = Temperature Sensor ▪ EP 9 = Power Source (battery indication) |
| 1b | MCORE. DEVLIS T.UseDe vices | | • Verify DUT contains the (supported) devices from the above list |
| 1c | MCORE. DEVLIS T.UseDe viceNa me | | • Verify DUT has (during step 1a) read the NodeLabel attribute from the Bridged Device Basic Information cluster on various endpoints • Verify DUT contains the names for the (supported) devices from the above list |

| 1d | MCORE. DEVLIS T.UseDe viceStat e | | • Verify DUT has read or reads OnOff attribute from the On/Off cluster for the various endpoints containing an On/Off light • Verify DUT contains the state for the (supported) devices from the above list |
| 1e | MCORE. DEVLIS T.UseDe viceStat e | Use TH/ bridge-app to change the on/off state of one or more of the bridged On/Off lights (use key 'c' in the console to bridge-app ) | • Verify DUT has read or reads OnOff attribute from the On/Off cluster for the various endpoints containing an On/Off light (or receives updates because of a previously set up subscription) |
| 1f | MCORE. DEVLIS T.UseDe viceStat e | | • Verify DUT has read or reads MeasuredValue attribute from the Temperature Measurement cluster for the various endpoints containing a Temperature Sensor (or receives updates because of a previously set up subscription) • Verify DUT contains the state for the (supported) device from the above list |
| 1g | MCORE. DEVLIS T.UseDe viceStat e | Use TH/ bridge-app to change the simulated temperature level of the simulated temperature sensors (use key 't' in the console to bridge- app ) | • Verify DUT has read or reads MeasuredValue attribute from the Temperature Measurement cluster for the various endpoints containing a Temperature Sensor (or receives updates because of a previously set up subscription) • Verify DUT contains the |
| | | | updated state for the (supported) device from the above list |

| 1h | MCORE. DEVLIS T.UseBa tInfo | | • Verify DUT has read or reads BatChargeLevel attribute from the Power Source cluster from the relevant endpoint (or receives updates because of a previously set up subscription) • Verify DUT contains the state of the battery of the (supported) devices from the above list | |
| 2: verify DUT can control actuator devices | 2: verify DUT can control actuator devices | 2: verify DUT can control actuator devices | 2: verify DUT can control actuator devices | 2: verify DUT can control actuator devices |
| 2a | | Use the DUT to change the on/off state of one or more of the bridged On/Off lights | • Verify the DUT sends On command (On/Off cluster) • Verify that simulated light in TH changes state ◦ the change of light state (due to DUT command) is shown in log output of bridge-app | |
| 3: verify DUT can process changes in set of exposed devices, and changes in names | 3: verify DUT can process changes in set of exposed devices, and changes in names | 3: verify DUT can process changes in set of exposed devices, and changes in names | 3: verify DUT can process changes in set of exposed devices, and changes in names | 3: verify DUT can process changes in set of exposed devices, and changes in names |
| 3a | MCORE. DEVLIS T.UseDe viceNa me | Use TH/ bridge-app to rename a bridged light (use key 'b' in the console to bridge-app to rename Light 1 to Light 1b ) | • Verify DUT reads (or gets the update via a previously set up subscription) an updated version of the NodeLabel attribute in the Bridged Device Basic Information cluster of the bridged device that got renamed | |
| 3b | MCORE. DEVLIS T.UseDe viceNa me | | • Verify DUT contains the updated name for the renamed device | |

| 3c | | Use TH/ bridge-app to add a bridged light (use key '2' in the console to bridge-app to add Light 2 ) | • Verify DUT reads (or gets the update via a previously set up subscription) an updated version of the PartsList attribute in the Descriptor cluster on endpoint 0 and the endpoint of the Aggregator device type to be aware of the added device • Verify DUT reads PartsList and DeviceType attribute of the newly added endpoint |
| 3d | MCORE. DEVLIS T.UseDe vices | | • Verify DUT contains the added device in the list of devices |
| 3e | | Use TH/ bridge-app to remove a bridged light (use key '4' in the console to bridge-app to remove Light 1b ) | • Verify DUT reads (or gets the update via a previously set up subscription) an updated version of the PartsList attribute in the Descriptor cluster on endpoint 0 and the endpoint of the Aggregator device type to be aware of the removed device |
| 3f | MCORE. DEVLIS T.UseDe vices | | • Verify DUT no longer contains the removed device in the list of devices |

## Notes/Testing Considerations

## TC-BR-5 Conditions for Fabric Synchronization (DUT server)

## Purpose

This test case verifies the required conditions for the bridge device to have Fabric Synchronization capabilities.

## PICS

- MCORE.FS

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT has been commissioned to TH | |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test Harness as Administrator, Controller |
| 2 | DUT | DUT (bridge) |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Manufacturer has provided bridge as DUT with Fabric Synchronization feature.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1: Verify that the device has Commissioner Control Cluster | 1: Verify that the device has Commissioner Control Cluster | 1: Verify that the device has Commissioner Control Cluster | 1: Verify that the device has Commissioner Control Cluster | 1: Verify that the device has Commissioner Control Cluster |
| 1a | | MCORE. FS.Aggr egator | Locate Aggregator node in the same way as in TC-BR-1 | |
| 1b | | MCORE. FS.Com mission erContr ol | By inspecting the ServerList attribute of Aggregator, verify that the Commissioner Control Cluster is there | FAIL if no such endpoint was found |
| 2: Check FabricSynchronization bit | 2: Check FabricSynchronization bit | 2: Check FabricSynchronization bit | 2: Check FabricSynchronization bit | 2: Check FabricSynchronization bit |
| 2a | | MCORE. FS.Fabri cSynchr onizatio n | Read SupportedDeviceCategories attribute from Commissioner Control cluster on Aggregator node | Verify that the FabricSynchronization bit is set to 1 |

## Notes/Testing Considerations

- When validating SupportedDeviceCategories we check that FabricSynchronization is set to 1 because this is a test that only runs on Fabric Sync device (as per PICS).

## Chapter 14. Bulk Data Exchange Protocol Test Plan

## 14.1. PICS Definition

This section covers the Bulk Data Exchange Protocol related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.BDX.Sender | Does the DUT support the BDX Sender role? | Optional | |
| MCORE.BDX.Receiver | Does the DUT support the BDX Receiver role? | Optional | |
| MCORE.BDX.Synchrono usSender | Does the DUT support the BDX Sender role in Synchronous mode? | Optional | |
| MCORE.BDX.Synchrono usReceiver | Does the DUT support the BDX Receiver role in Synchronous mode? | Optional | |
| MCORE.BDX.Asynchron ousSender | Does the DUT support the BDX Sender role in Asynchronous mode? | Optional | |
| MCORE.BDX.Asynchron ousReceiver | Does the DUT support the BDX Receiver role in Asynchronous mode? | Optional | |
| MCORE.BDX.Driver | Does the DUT control the rate of the BDX transfer ? | Optional | |
| MCORE.BDX.Initiator | Is the DUT an Initiator of the BDX transfer? | Optional | |
| MCORE.BDX.Responder | Is the DUT a Responder of the BDX transfer? | Optional | |
| MCORE.BDX.BlockQuer yWithSkip | Does the DUT support sending the BlockQueryWithSkip message? | Optional | |

## 14.2. Test Case List

| TC UUID | Test Case Name |
| TC-BDX-1.1 | Sender Initiated BDX Transfer Session - PROVISIONAL |
| TC-BDX-1.2 | Receiver Initiated BDX Transfer Session |
| TC-BDX-1.3 | Response to Sender Initiated BDX Transfer Session - PROVISIONAL |
| TC-BDX-1.4 | Response to Receiver Initiated BDX Transfer Session |
| TC-BDX-1.5 | Response to Sender Initiated BDX Transfer Session - Negative scenario - PROVISIONAL |
| TC-BDX-1.6 | Response to Receiver Initiated BDX Transfer Session - Negative scenario - PROVISIONAL |
| TC-BDX-2.1 | Synchronous File Sending |
| TC-BDX-2.2 | Synchronous File Receiving |
| TC-BDX-2.3 | Restart Synchronous File Receiving - PROVISIONAL |
| TC-BDX-2.4 | Asynchronous File Sending - PROVISIONAL |
| TC-BDX-2.5 | Asynchronous File Receiving - PROVISIONAL |

## 14.3. Test Cases

## 14.3.1. Transfer Management Test Cases

## TC-BDX-1.1 Sender Initiated BDX Transfer Session - PROVISIONAL

## Purpose

This test case verifies that the SendInit message contains the necessary information to initiate the BDX transfer session.

## PICS

- MCORE.BDX.Sender
- MCORE.BDX.Initiator

## Required Devices

| Device Name | Device Description |

| 1 | TH | Test harness as BDX Responder and Receiver. |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be verified using TC-DIAGLOG-1.1 from the Diagnostic Logs cluster section. This test cannot be executed with V1.0 SDK.

## TC-BDX-1.2 Receiver Initiated BDX Transfer Session

## Purpose

This test case verifies that the ReceiveInit message contains the necessary information to initiate the BDX transfer session.

## PICS

- MCORE.BDX.Receiver
- MCORE.BDX.Initiator

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Responder and Sender. |
| 2 | DUT | DUT as BDX Initiator and Receiver. |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be verified using TC-SU-2.3 from the OTA Software Update section.

## TC-BDX-1.3 Response to Sender Initiated BDX Transfer Session - PROVISIONAL

## Purpose

This test case verifies that the SendAccept message contains the necessary information to initiate the BDX transfer session.

## PICS

- MCORE.BDX.Receiver
- MCORE.BDX.Responder

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Initiator and Sender. |
| 2 | DUT | DUT as BDX Responder and Receiver. |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be verified using TC-DIAGLOG-1.3 from the Diagnostic Logs cluster section. This test cannot be executed with V1.0 SDK.

## TC-BDX-1.4 Response to Receiver Initiated BDX Transfer Session

## Purpose

This test case verifies that the ReceiveAccept message contains the necessary information to initiate the BDX transfer session.

- MCORE.BDX.Sender
- MCORE.BDX.Responder

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Initiator and Receiver |
| 2 | DUT | DUT as BDX Responder and Sender |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be verified using TC-SU-3.3 from the OTA Software Update section.

## TC-BDX-1.5 Response to Sender Initiated BDX Transfer Session - Negative Scenario PROVISIONAL

## Purpose

This test case verifies that the DUT aborts the BDX transfer session with an appropriate error.

- MCORE.BDX.Receiver
- MCORE.BDX.Responder

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Initiator and Sender |
| 2 | DUT | DUT as BDX Responder and Receiver |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test cannot be executed with V1.0 SDK.

## TC-BDX-1.6 Response to Receiver Initiated BDX Transfer Session - Negative Scenario PROVISIONAL

## Purpose

This test case verifies that the DUT aborts the BDX transfer session with an appropriate error.

## PICS

- MCORE.BDX.Sender
- MCORE.BDX.Responder

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Initiator and Receiver |
| 2 | DUT | DUT as BDX Responder and Sender |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test cannot be executed with V1.0 SDK.

## 14.3.2. Data Transfer Test Cases

## TC-BDX-2.1 Synchronous File Sending

## Purpose

This test case verifies that the DUT can successfully send files in Synchronous mode.

- MCORE.BDX.SynchronousSender

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Receiver |
| 2 | DUT | DUT as BDX Sender |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

DUT can initiate a BDX transfer with a SendInit message to TH or TH can initiate a BDX transfer with a ReceiveInit message to DUT.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be verified using TC-SU-3.3 from the OTA Software Update section or TC-DIAGLOG-1.1 from the Diagnostic Logs cluster section.

## TC-BDX-2.2 Synchronous File Receiving

## Purpose

This test case verifies that the DUT can successfully receive files in Synchronous mode.

## PICS

- MCORE.BDX.SynchronousReceiver

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Sender |
| 2 | DUT | DUT as BDX Receiver |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH can initiate a BDX transfer with a SendInit message to TH or DUT can initiate a BDX transfer with a ReceiveInit message to DUT.

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be verified using TC-SU-2.3 from the OTA Software Update section or TC-DIAGLOG-1.3 from the Diagnostic Logs cluster section.

Test Step #4 cannot be executed with V1.0 SDK.

## TC-BDX-2.3 Restart Synchronous File Receiving - PROVISIONAL

## Purpose

This test case verifies that the DUT can successfully restart receiving files in Synchronous mode.

## PICS

## · MCORE.BDX.SynchronousReceiver

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Sender |
| 2 | DUT | DUT as BDX Receiver |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

DUT sends a ReceiveInit message to TH + TH sends a ReceiveAccept message back to DUT + TH sends a Block message to DUT + DUT sends a BlockAck message back to TH. After a while, TH stops sending Blocks which leads to idle timeout and abort transfer session.

## Test Procedure

| # | Ref | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be verified using TC-SU-2.3 from the OTA Software Update section. This test cannot be executed with V1.0 SDK.

## TC-BDX-2.4 Asynchronous File Sending - PROVISIONAL

## Purpose

This test case verifies that the DUT can successfully send files in Asynchronous mode.

## PICS

- MCORE.BDX.AsynchronousSender

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Receiver |
| 2 | DUT | DUT as BDX Sender |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be initiated from OTA Software Update section or Diagnostic Logs cluster section. This test can also be verified with TH sending a ReceiveInit message to the DUT. This test cannot be executed with V1.0 SDK.

## TC-BDX-2.5 Asynchronous File Receiving - PROVISIONAL

## Purpose

This test case verifies that the DUT can successfully receive files in Asynchronous mode.

- MCORE.BDX.AsynchronousReceiver

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as BDX Sender |
| 2 | DUT | DUT as BDX Receiver |

## Device Topology

TH and DUT are on the same fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

This test can be initiated from OTA Software Update section or Diagnostic Logs cluster section. This test can also be verified with TH sending a SendInit message to the DUT. This test cannot be executed with V1.0 SDK.

## Chapter 15. OTA Software Update Test Plan

## 15.1. PICS Definition

This section covers the Software Update Test Plan related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.OTA.Requestor | Does the DUT implement the OTA Requestor Device Type? | O | |
| MCORE.OTA.Provider | Does the DUT implement the OTA Provider Device Type? | O | |
| MCORE.OTA.HTTPS | Does the DUT support the HTTPS Protocol for OTA image download? | O | |
| MCORE.OTA.Requestor Consent | Does the DUT support obtaining user consent for OTA application by virtue of built-in user interface capabilities? | O | |
| MCORE.OTA.Resume | Does the DUT support resumption of a transfer previously aborted? | O | |
| MCORE.OTA.VendorSpe cific | Does the DUT support Vendor specific OTA implementation? | MCORE.ROLE.COMMISS IONEE & !MCORE.OTA.Requestor | |
| MCORE.ACL.Administra tor | Does the DUT have Administer privilege over the Access Control of another node? | O | |
| MCORE.OTA.Retry | Does the Requestor DUT support querying a different Provider in its OTA Provider List when it hits error conditions in invoking the QueryImage command? | O | |

| OTAP.S.M.DelayedActio nTime | Does the DUT support sending the DelayedActionTime field in QueryImageResponse Command? | O |
| OTAP.S.M.UserConsent Needed | Does the DUT support sending the UserConsentNeeded field in QueryImageResponse Command? | O |
| OTAR.C.M.AnnounceOT AProvider | Does the DUT support sending the AnnounceOTAProvider Command? | O |
| OTAR.C.M.NotifyUpdate Applied | Does the DUT support sending the NotifyUpdateApplied Command? | O |

## 15.2. Test Case List

| # | TC UUID | Test Case Name |
| 1 | TC-SU-1.1 | Invoke AnnounceOTAProvider from Admin(DUT) to OTA-R |
| 2 | TC-SU-2.1 | QueryImage Command from DUT to OTA-P |
| 3 | TC-SU-2.2 | Handling different QueryImageResponse scenarios on Requestor |
| 4 | TC-SU-2.3 | Transfer of Software Update Images between OTA-R(DUT) and OTA-P |
| 5 | TC-SU-2.4 | ApplyUpdateRequest command from DUT to OTA-P |
| 6 | TC-SU-2.5 | Handling different ApplyUpdateResponse scenarios on Requestor |
| 7 | TC-SU-2.6 | NotifyUpdateApplied Command from DUT to OTA-P |
| 8 | TC-SU-2.7 | Verifying Events on OTA-R(DUT) |

| 9 | TC-SU-2.8 | OTA functionality in Multi Fabric scenario |
| 10 | TC-SU-3.1 | QueryImageResponse from DUT to OTA-R |
| 11 | TC-SU-3.2 | Handling different QueryImageResponse scenarios on Provider |
| 12 | TC-SU-3.3 | Transfer of Software Update Images between OTA-R and OTA-P(DUT) |
| 13 | TC-SU-3.4 | Handling different ApplyUpdateResponse scenarios on Provider |
| 14 | TC-SU-4.1 | Verifying cluster attributes on OTA-R(DUT) |
| 15 | TC-SU-5.1 | Verifying vendor specific OTA implementation on DUT |

## 15.3. Test Cases

## 15.3.1. OTA Provider Discovery

## TC-SU-1.1 Invoke AnnounceOTAProvider from Admin(DUT) to OTA-R

## Purpose

This test case verifies that the DUT is able to invoke the AnnounceOTAProvider command on the OTA-R.

## PICS

- MCORE.ACL.Administrator

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness 1 as OTA-R device type. |
| 3 | TH2 | Test harness 2 as OTA-P device type. |

TH, TH2 and DUT are on the same fabric.

## Test Setup

OTA-R/TH and DUT are on the same fabric. OTA-P/TH2 is commissioned later as part of the test step.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Vendor needs to mention steps on how to trigger the AnnounceOTAProvider Command.

## 15.3.2. Querying the OTA Provider

## TC-SU-2.1 QueryImage Command from DUT to OTA-P

## Purpose

This test case verifies that the DUT is able to successfully send a QueryImage command to the OTA-P

## PICS

## · MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-P device type. |
| 3 | TH2 | Test harness 2 as Administrator. |

## Device Topology

TH, TH2 and DUT are on the same fabric.

## Test Setup

TH, TH2 and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

* Triggering OTA on the DUT is vendor specific. This is applicable for all devices which are triggering OTA.

## TC-SU-2.2 Handling Different QueryImageResponse Scenarios on Requestor

## Purpose

This test case verifies that the DUT behaves according to the spec on different scenarios of the QueryImageResponse Command from the OTA-P.

## PICS

- MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-P device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Test Step #5 cannot be executed with V1.0 SDK.

## 15.3.3. Transfer of Software Update Images

## TC-SU-2.3 Transfer of Software Update Images between DUT and TH/OTA-P

## Purpose

This test case verifies that the DUT behaves according to the spec when it is transferring images from the TH/OTA-P.

## PICS

- MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-P device type. |

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Requestor User Consent is specific to vendor implementation.

Test Step #3 cannot be executed with V1.0 SDK.

*

Test Step #5 cannot be executed with V1.0 SDK.

'''

## 15.3.4. Applying a Software Update

## TC-SU-2.4 ApplyUpdateRequest Command from DUT to OTA-P

## Purpose

This test case verifies that the DUT behaves according to the spec when it is applying the software update.

## PICS

- MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-P device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

* Vendor needs to provide instructions on how to trigger the DUT/OTA-R to send the ApplyUpdateRequest .

'''

## TC-SU-2.5 Handling Different ApplyUpdateResponse Scenarios on Requestor

## Purpose

This test case verifies that the DUT behaves according to the spec when it is applying the software update.

## · MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-P device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

DUT sends a QueryImage command to the TH/OTA-P. TH/OTA-P sends a QueryImageResponse back to DUT. QueryStatus is set to "UpdateAvailable". Set ImageURI to the location where the image is located. After the DUT transfers the image, the DUT should send ApplyUpdateRequest to the OTA-P.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Software version can be verified by querying the Basic Information cluster.

## TC-SU-2.6 NotifyUpdateApplied Command from DUT to OTA-P

## Purpose

This test case verifies that the DUT behaves according to the spec when it is applying the software update.

## PICS

## · MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-P device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

DUT sends a QueryImage command to the TH/OTA-P. TH/OTA-P sends a QueryImageResponse back to DUT. QueryStatus is set to "UpdateAvailable". Set ImageURI to the location where the image is located.After the DUT transfers the image, the DUT should send ApplyUpdateRequest to the OTA-P. OTA-P/TH sends the ApplyUpdateResponse Command to the DUT.

Action field is set to "Proceed"

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

Notes/Testing Considerations

## 15.3.5. Requestor Cluster Events

## TC-SU-2.7 Verifying Events on OTA-R(DUT)

## Purpose

This test case verifies that the DUT behaves according to the spec when events are generated.

## PICS

- MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | OTA-P device type |
| 3 | OTA-Subscriber | any device which has subscribed to the OTA events from the DUT. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

OTA-SUB should be setup such that it is subscribing to the OTA events from the DUT

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## 15.3.6. Multiple Fabrics

## TC-SU-2.8 OTA Functionality in Multi Fabric Scenario

## Purpose

This test case verifies that the DUT is able to successfully send a QueryImage command to the OTA-P in multi fabric scenario.

## PICS

## · MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH1 | Test harness 1 as OTA-P device type. |
| 3 | TH2 | Test harness 2 as OTA-P device type. |

## Device Topology

Commission TH1 and TH2 on different fabrics and DUT to both these fabrics.

## Test Setup

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric. DefaultOTAProviders Attribute is set by Administrators, either during Commissioning or at a later time, to set the Provider Location for the default OTA Provider Node to use for software updates on a given Fabric. There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

* Triggering OTA on the DUT is vendor specific. This is applicable for all devices which are triggering OTA.

## 15.3.7. Querying the OTA Provider

## TC-SU-3.1 QueryImageResponse from DUT to OTA-R

## Purpose

This test case verifies that the DUT behaves according to the spec when it receives a QueryImageRequest from the OTA-R.

## PICS

- MCORE.OTA.Provider

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-R device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

There is no ongoing OTA process, and reading the UpdateState Attribute of the OTA Requestor should return the value as Idle.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Test Step #1 - User Consent is obtained from the user and is specific to vendor implementation.

## TC-SU-3.2 Handling Different QueryImageResponse Scenarios on Provider

## Purpose

This test case verifies that the DUT behaves according to the spec in sending the correct QueryImageResponse to the OTA-R.

## PICS

## · MCORE.OTA.Provider

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-R device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric. DUT should be able to get user consent prior to QueryImageResponse when needed.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| | | the Verify the URI's scheme field is 'bdx' in lowercase characters. Verify the URI's authority field contains only the string representation of the Operational Node ID of the Node where to proceed with the download. Verify that the encoding of the Node ID in the host field uses an uppercase hexadecimal format, using exactly 16 characters to encode the network byte order value of the NodeID. Verify that the Operational Node ID in the host field matches with the NodeID of the OTA Provider responding with the QueryImageResponse . Verify that the the user section of the authority field is absent. Verify that the URI does not contain Query field. Fragment field. Verify that the path field has the absolute path to the software image. Verify that the path has only valid URI characters. Verify that the URI is 24 characters or longer. Verify the presence of prefix |

## Notes/Testing Considerations

Other than Test Case #2 all test cases assume that the software update image is available.

Test Step #2 - The DUT should not have any cached image already downloaded.

Verification of Test Case #3 can be done with Test Case #1.

Test Step #4 cannot be executed with V1.0 SDK.

## 15.3.8. Transfer of Software Update Images

## TC-SU-3.3 Transfer of Software Update Images between DUT and OTA-R

## Purpose

This test case verifies that the DUT behaves according to the spec when it is transferring images to the TH/OTA-R.

## PICS

- MCORE.OTA.Provider

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness as OTA-R device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric. DUT should be able to get user consent prior to QueryImageResponse when needed.

## Test Procedure

| Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Test Step #5 cannot be executed with V1.0 SDK.

## 15.3.9. Applying a Software Update

## TC-SU-3.4 Handling Different ApplyUpdateResponse Scenarios on Provider

## Purpose

This test case verifies that the DUT behaves according to the spec on when a software update should be applied by the OTA-R.

## PICS

- MCORE.OTA.Provider

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as OTA-P device type. |

| 2 | TH | Test harness as OTA-R device type. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

TH and DUT are on the same fabric.

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

DUT should be able to get user consent prior to QueryImageResponse when needed.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

Test Cases where the DUT needs to be forced to send a certain response might not be testable.

## 15.3.10. Requestor Cluster Attributes

## TC-SU-4.1 Verifying Cluster Attributes on OTA-R(DUT)

## Purpose

This test case verifies that the DUT behaves according to the spec with the Cluster attributes.

## PICS

## · MCORE.OTA.Requestor

## Required Devices

| # | Device Name | Device Description |
| 2 | TH | Test harness admin/controller used to perform read/write operations on Fabric 1 (default_controller). |

## Device Topology

TH2 (provider1\_fabric1) and TH4 (provider2\_fabric1) are on Fabric 1.

TH3 (provider1\_fabric2) is on Fabric 2. DUT is commissioned to both fabrics (Fabric 1 and Fabric 2). TH is the admin/controller for Fabric 1 (default controller). TH3 acts as the admin/controller for Fabric 2 (secondary controller created in test).

## Test Setup

Commissioner or Administrator should install necessary ACL entries at commissioning time or later to enable processing of QueryImage commands from OTA Requestors on their fabric.

## Test Procedure

| # | TestStep | Expected Outcome |
| 0 | Commissioning, already done | |

| 8 | TH sends a read request to read the UpdateState Attribute from the DUT. | Verify that the attribute value is set to one of the following values. Unknown, Idle, Querying, DelayedOnQuery, Downloading, Applying, DelayedOnApply, RollingBack, DelayedOnUserConsent. |

## Notes/Testing Considerations

## 15.3.11. Vendor specific OTA implementation

## TC-SU-5.1 Verifying vendor specific OTA implementation on DUT

## Purpose

This test case verifies that the DUT is able to successfully perform software update by vendor specific means if OTA Requestor cluster is not supported.

## PICS

- MCORE.OTA.VendorSpecific

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as Commissionee device. |
| 2 | TH | Test Harness as a Commissioner. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH, if not done so already.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Perform the OTA Update on DUT using vendor specific mechanism. | Verify that the DUT starts updating its software. Once the update is finished, verify the SoftwareVersion attribute from the Basic Information cluster on the DUT to match the version downloaded for the software update. |

## Notes/Testing Considerations

Vendor needs to provide a way to verify that the device is able to perform software update if OTA Requestor cluster is not supported.

## Chapter 16. Access Control Enforcement Test Plan

## 16.1. PICS Definition

This section covers the Access Control Enforcement Test Plan related PICS items that are referenced in the following test cases.

## 16.1.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ACL.S | Does the device implement the Access Control Cluster as a server? | O | |
| ACL.C | Does the device implement the Access Control Cluster as a client? | O | |
| APPDEVICE.S | Does the device implement an Application Device Type on any endpoint | O | |

## 16.1.2. Server

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ACL.S.A0000(ACL) | Does the DUT support the ACL attribute? | ACL.S :M | |

## 16.2. PIXIT Definition

This section covers the Access Control Enforcement Test Plan related PIXIT items that might be required in the following test cases.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |

| PIXIT.ACE.APPENDPOI NT | Endpoint that the device implements the Application Device Type on | APPDEVICE.S |
| PIXIT.ACE.APPDEVTYP EID | Application Device type ID that the DUT implements on PIXIT.ACE.APPENDPOI NT | APPDEVICE.S |
| PIXIT.ACE.APPCLUSTER | Server cluster implemented on PIXIT.ACE.APPENDPOI NT (must include at least one attribute) | APPDEVICE.S |
| PIXIT.ACE.APPATTRIBU TE | Attribute from PIXIT.ACE.APPCLUSTER to use for ACE tests | APPDEVICE.S |

## 16.3. Test Case List

| # | TC UUID | Test Case Name |
| 1 | TC-ACE-1.1 | Privileges [DUT-Commissionee] |
| 2 | TC-ACE-1.2 | Subscriptions [DUT-Commissionee] |
| 3 | TC-ACE-1.3 | Subjects [DUT-Commissionee] |
| 4 | TC-ACE-1.4 | Targets [DUT-Commissionee] |
| 5 | TC-ACE-1.5 | Multi-fabric [DUT-Commissionee] |
| 6 | TC-ACE-1.6 | Group auth mode [DUT-Commissionee] |
| 7 | TC-ACE-2.1 | Attribute read privilege enforcement - [DUT as Server] |
| 8 | TC-ACE-2.2 | Attribute write privilege enforcement - [DUT as Server] |
| 9 | TC-ACE-2.3 | Command privilege enforcement - [DUT as Server] |
| 10 | TC-ACE-2.4 | Attribute read subscription report - [DUT as Server] |

## 16.4. Test Cases

## 16.4.1. Cluster Attribute test cases

## TC-ACE-1.1 Privileges[DUT-Commissionee]

## Purpose

1. Verify that access control is correctly enforced for reading attributes.

2. Verify that access control is correctly enforced for writing attributes.
3. Verify that access control is correctly enforced for invoking commands.
4. Verify that access control is correctly enforced for reading events.
5. Verify that access control is correctly enforced when existing privileges are removed.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | | | N1 is the node ID of TH1 |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH | Commissioner - uses node ID N1 |

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH1 commissions DUT using admin node ID N1 | DUT is commissioned on TH1 fabric |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | | | TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing 1 elements, granting itself administer privileges on all of Endpoint 0: 1. struct ◦ Fabric Index: 1 ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: null, Endpoint: 0, DeviceType: null}] | Result is SUCCESS |
| 3 | | | TH reads the NOCs attribute from the Node Operational Credentials cluster using a fabric-scoped read (requires administer privilege) | DUT returns a list of NOCs containing 1 entry |
| 4 | | | TH writes the Location attribute in the Basic Information cluster with "XX" (requires administer privilege) | Result is SUCCESS |
| 5 | | | TH sends the UpdateFabricLabel command to the Node Operational Credentials cluster with the Label field set to "TestFabric" (requires administer privilege) | Result is SUCCESS |
| 6 | | | TH writes the NodeLabel attribute in the Basic Information cluster with the string "TestNode" (requires manage privilege) | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 7 | | | TH sends the TestEventTrigger command to the General Diagnostics cluster with the EnableKey set to 0 and the EventTrigger set to 0 (requires manage privilege). Note that this will cause an error to be returned because the EnableKey is invalid, but still indicates that the TH passed the ACL check. | Result is CONSTRAINT_ERROR |
| 8 | | | TH reads the VendorID attribute from the Basic Information cluster (requires view privilege) | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 9 | | | TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing 2 elements, giving itself administer privilege only on the Access Control cluster and manage privilege on everything else on EP0. 1. struct ◦ Fabric Index: 1 ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: 0x001F, Endpoint: 0}] 2. struct ◦ Fabric Index: 1 ◦ Privilege field: Manage (4) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: | Result is SUCCESS |
| 10 | | | TH reads the NOCs attribute from the Node Operational Credentials cluster using a fabric-filtered read (requires administer privilege) | Result is UNSUPPORTED_ACCESS (0x7e) |
| 11 | | | TH writes the Location attribute in the Basic Information cluster with "XX" (requires administer privilege) | Result is UNSUPPORTED_ACCESS (0x7e) |

| # | Ref | PICS | Test Step | Expected Outcome |
| 12 | | | TH sends the UpdateFabricLabel command to the operational credentials cluster with the Label field set to "TestFabric" (requires administer privilege) | Result is UNSUPPORTED_ACCESS (0x7e) |
| 13 | | | Repeat steps 6 to 8 to confirm that TH still has access associated with manage and view privileges | |
| 14 | | | TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing 2 elements, giving itself administer privilege only on the Access Control cluster and operate privilege on everything else on EP0. 1. struct ◦ Fabric Index: 1 ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: 0x001F, Endpoint: 0}] 2. struct ◦ Fabric Index: 1 ◦ Privilege field: Operate (3) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 15 | | | Repeat steps 10 to 12 to confirm that TH still does not have administer privileges | |
| 16 | | | TH writes the NodeLabel attribute in the Basic Information cluster with the string "TestNode" (requires manage privilege) | Result is UNSUPPORTED_ACCESS (0x7e) |
| 17 | | | TH sends the TestEventTrigger command to the General Diagnostics cluster with the EnableKey set to 0 and the EventTrigger set to 0. (requires manage privilege) | Result is UNSUPPORTED_ACCESS (0x7e) |
| 18 | | | Repeat step 8 to confirm that the TH still has view privileges | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 19 | | | TH1 writes the ACL attribute with a list of AccessControlEntryStruct entries containing 2 elements, giving itself administer privilege only on the Access Control cluster and view privilege on everything else on EP0. 1. struct ◦ Fabric Index: 1 ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: 0x001F, Endpoint: 0}] 2. struct ◦ Fabric Index: 1 ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Endpoint: 0}] | Result is SUCCESS |
| 20 | | | Repeat steps 10 to 12 to confirm that TH still does not have administer privileges | |
| 21 | | | Repeat steps 16 to 17 to confirm that TH still does not have manage privileges | |
| 22 | | | Repeat step 8 to confirm that the TH still has view privileges | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 23 | | | TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing a single element, granting Administer privilege on only the Access Control cluster and no other access. 1. struct ◦ Fabric Index: 1 ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: 0x001F, Endpoint: 0}] | Result is SUCCESS |
| 24 | | | Repeat steps 10 to 12 to confirm that TH still does not have administer privileges | |
| 25 | | | Repeat steps 16 to 17 to confirm that TH still does not have manage privileges | |
| 26 | | | TH reads the VendorID attribute from the Basic Information cluster (requires view privilege) | Result is UNSUPPORTED_ACCESS (0x7e) |
| 27 | | | TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing a single element, restoring full access to the node. . struct - Fabric Index: 1 - Privilege field: Administer (5) - AuthMode field: CASE (2) - Subjects field: [ N1 ] - Targets field: null | Result is SUCCESS |

## TC-ACE-1.2 Subscriptions[DUT-Commissionee]

## Purpose

1. Verify that access control is correctly enforced for new subscriptions.
2. Verify that access control is correctly enforced for existing subscriptions when privileges change.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | | | N1 is the node ID of TH1 |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner - uses node ID N1 |
| 3 | TH2 | Administrator (client) - uses node ID N2 , same fabric as N1 |

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH1 commissions DUT | DUT is commissioned on TH1 fabric |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 12 | | | Repeat steps 9 to 10, incrementing the Breadcrumb value from the last write, to verify that TH2 can still receive view- privilege attribute reports. | |
| 16 | | | Repeat steps 9 to 10, incrementing the Breadcrumb value from the last write, to verify that TH2 can still receive view- privilege attribute reports. | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 19 | | | Repeat steps 13 to 14 to ensure TH2 still does not have permissions to subscribe to administer- privilege attributes and events | |
| 20 | | | Repeat step 15 to ensure TH2 can still subscribe to view events | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 24 | | | Repeat steps 13 to 14 to ensure TH2 still does not have permissions to subscribe to administer- privilege attributes and events | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 25 | | | Repeat step 15 to ensure TH2 can still subscribe to view events | |
| 28 | | | Repeat steps 13 to 14 to ensure TH2 still does not have permissions to subscribe to administer- privilege attributes and events | |

## TC-ACE-1.3 Subjects[DUT-Commissionee]

## Purpose

1. Verify that access control is correctly enforced for wildcard subjects.
2. Verify that access control is correctly enforced for node ID subjects.
3. Verify that access control is correctly enforced for CAT subjects (including ID and version).

4. Verify that access control is correctly enforced for multiple subjects.

## PICS

- MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | | | TH0, TH1, TH2, TH3 are on the same fabric |
| 2 | | | N0 is the node ID of TH0 |
| 3 | | | N1 is the node ID of TH1 |
| 4 | | | N2 is the node ID of TH2 |
| 5 | | | N3 is the node ID of TH3 |
| 6 | | | DUT is commissioned by TH0 |
| 7 | | | CAT1v1 is a version 1 CAT |
| 8 | | | CAT1v2 is a version 2 CAT with the same ID as CAT1v1 |
| 9 | | | CAT1v3 is a version 3 CAT with the same ID as CAT1v2 |
| 10 | | | CAT2v1 is a version 1 CAT with a different ID from CAT1v1 |
| 11 | | | CAT2v2 is a version 2 CAT with the same ID as CAT2v1 |
| 12 | | | CAT2v3 is a version 3 CAT with the same ID as CAT2v2 |
| 13 | | | CAT1v1_subject is the ACL subject for CAT1v1 (0xFFFF_FFFD_0000_0000 &#124; CAT1v1 ) |
| 14 | | | CAT1v2_subject is the ACL subject for CAT1v2 (0xFFFF_FFFD_0000_0000 &#124; CAT1v2 ) |
| 15 | | | CAT1v3_subject is the ACL subject for CAT1v3 (0xFFFF_FFFD_0000_0000 &#124; CAT1v3 ) |
| 16 | | | CAT2v1_subject is the ACL subject for CAT2v1 (0xFFFF_FFFD_0000_0000 &#124; CAT2v1 ) |
| 17 | | | CAT2v2_subject is the ACL subject for CAT2v2 (0xFFFF_FFFD_0000_0000 &#124; CAT2v2 ) |

| # | Doc Ref | Condition | Notes |
| 18 | | | CAT2v3_subject is the ACL subject for CAT2v3 (0xFFFF_FFFD_0000_0000 &#124; CAT2v3 ) |
| 19 | | | TH1 has credentials for CAT1v3 |
| 20 | | | TH2 has credentials for CAT1v2 and CAT2v1 |
| 21 | | | TH3 has credentials for CAT1v1 and CAT2v2 |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |
| 3 | TH2 | Controller |
| 4 | TH3 | Controller |

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Precondition: TH0 commissions DUT using admin node ID N0 | DUT is commissioned on TH0 fabric |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 6 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome | |
| 10 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N2 ] | Result is SUCCESS | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 14 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N3 ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 18 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 , N2 ] | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 22 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 , N3 ] | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 26 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N2 , N3 ] | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 30 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 , N2 , N3 ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 34 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ CAT1v1_subject ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 38 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ CAT1v2_subject ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 42 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ CAT1v3_subject ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 46 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ CAT2v1_subject ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 50 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ CAT2v2_subject ] | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 54 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ CAT2v3_subject ] ◦ Targets field: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 58 | | | TH0 writes DUT Endpoint 0 AccessControl cluster ACL attribute to reset it back to the default State. Value is list of AccessControlEntryStruct containing 1 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N0 ] ◦ Targets field: null | Result is SUCCESS |

## TC-ACE-1.4 Targets[DUT-Commissionee]

## Purpose

1. Verify that access control is correctly enforced for wildcard targets.
2. Verify that access control is correctly enforced for cluster targets.
3. Verify that access control is correctly enforced for endpoint targets.
4. Verify that access control is correctly enforced for device type targets.
5. Verify that access control is correctly enforced for cluster plus endpoint targets.
6. Verify that access control is correctly enforced for cluster plus device type targets.
7. Verify that access control is correctly enforced for multiple targets.
8. Verify that access control is correctly enforced for wildcard reads, and returns correct status.

## PICS

- MCORE.ROLE.COMMISSIONEE
- APPDEVICE.S

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | | | N1 is the node ID of TH1 |
| 2 | | | AppClusterId is the cluster ID of PIXIT.ACE.APPCLUSTER |

| # | Doc Ref | Condition | Notes |
| 3 | | | AppAttributeId is the attribute ID of PIXIT.ACE.APPATTRIBUTE |
| 4 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH1 commissions DUT using admin node ID N1 . Confirms pre-conditions are met. | DUT is commissioned on TH1 fabric |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 6 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Cluster: Descriptor | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 10 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Cluster: PIXIT.ACE.APPCLUST | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 14 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Cluster: Descriptor (0x001d), Endpoint: PIXIT.ACE.APPENDPO | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome | |
| 18 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Cluster: PIXIT.ACE.APPCLUST ER ( AppClusterId ), Endpoint: PIXIT.ACE.APPENDPO | Result is SUCCESS | |

| # | Ref | PICS | Test Step | Expected Outcome | |
| 22 | | | PIXIT.ACE.APPENDPOINT TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Endpoint: PIXIT.ACE.APPENDPO | Result is SUCCESS | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 26 | | | PIXIT.ACE.APPENDPOINT TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{DeviceType: | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome | |
| 30 | | | PIXIT.ACE.APPENDPOINT TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{DeviceType: PIXIT.ACE.APPDEVTY | Result is SUCCESS | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 34 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Cluster: Descriptor (0x001d), DeviceType: PIXIT.ACE.APPDEVTY | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 38 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Cluster: PIXIT.ACE.APPCLUST ER ( AppClusterId ), DeviceType: PIXIT.ACE.APPDEVTY | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |
| 42 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute, value is list of AccessControlEntryStruct containing 2 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: AccessControl (0x001f), Endpoint: 0}] 2. struct ◦ Privilege field: View (1) ◦ AuthMode field: CASE (2) ◦ Subjects field: null ◦ Targets field: [{Cluster: Descriptor (0x001d), Endpoint: 0}, {Cluster: PIXIT.ACE.APPCLUST ER ( AppClusterId ), Endpoint: PIXIT.ACE.APPENDPO | Result is SUCCESS |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 48 | | | TH1 writes DUT Endpoint 0 AccessControl cluster ACL attribute to reset it back to the default State. Value is list of AccessControlEntryStruct containing 1 elements 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: null | Result is SUCCESS |

## TC-ACE-1.5 Multi-fabric[DUT-Commissionee]

## Purpose

1. Verify that access control is correctly enforced using only ACLs from appropriate fabric.

## PICS

- MCORE.ROLE.COMMISSIONEE
- APPDEVICE.S

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | | | N1 is the node ID of TH1 on fabric F1 |
| 2 | | | N2 is the node ID of TH2 on fabric F2 |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |
| 3 | TH2 | Commissioner |

## Test Setup

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH1 commissions DUT using admin node ID N1 | DUT is commissioned on TH1 fabric |
| 2 | | | TH1 opens the commissioning window on the DUT | |
| 3 | | | TH2 commissions DUT using admin node ID N2 | DUT is commissioned on TH2 fabric |
| 4 | | | TH2 reads its fabric index from the Operational Credentials cluster CurrentFabricIndex attribute | Read successful, save as th2FabricIndex |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## TC-ACE-1.6 Group auth mode[DUT-Commissionee]

## Purpose

1. Verify that access control is correctly enforced during group messaging using only ACLs with group auth mode.

## PICS

- MCORE.ROLE.COMMISSIONEE
- G.S

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | | | N1 is the node ID of TH1 |

| # | Doc Ref | Condition | Notes |
| 2 | | | PIXIT.G.ENDPOINT is an endpoint with a groups cluster |
| 3 | | | ep 1 is a Non-RootNode endpoint ID to add in a groupcast membership |

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH | Commissioner |

## Test Setup

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | CoreSpec- 11.2.5.1. | | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT using a key that is pre-installed on the TH. GroupKeySet fields are as follows: • GroupKeySetID: 0x01a3 • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: d0d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime0: 2220000 • EpochKey1: d1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 2220001 • EpochKey2: d2d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime2: 2220002 | Verify that the DUT sends SUCCESS response |

| # | Ref | PICS | Test Step | Expected Outcome |
| 1b | CoreSpec- 11.2.5.1. | | TH sends KeySetWrite command in the GroupKeyManagement cluster to DUT using a key that is pre-installed on the TH. GroupKeySet fields are as follows: • GroupKeySetID: 0x01a1 • GroupKeySecurityPolicy: TrustFirst (0) • EpochKey0: a0d1d2d3d4d5d6d7d8d9d adbdcdddedf • EpochStartTime0: 2220000 • EpochKey1: b1d1d2d3d4d5d6d7d8d9 dadbdcdddedf • EpochStartTime1: 2220001 • EpochKey2: c2d1d2d3d4d5d6d7d8d9d adbdcdddedf • EpochStartTime2: 2220002 | Verify that the DUT sends SUCCESS response |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | CoreSpec- 11.2.7.2 | | If the Groupcast cluster is enabled on the RootNode endpoint, skip this step. Otherwise, TH binds GroupIds 0x0101 and 0x0102 with GroupKeySetID 0x01a1 and GroupId 0x0103 with GroupKeySetID 0x01a3 in the GroupKeyMap attribute list on GroupKeyManagement cluster by writing the GroupKeyMap attribute with three entries as follows: • List item 1: ◦ GroupId: 0x0101 ◦ GroupKeySetId: 0x01a1 • List item 2: ◦ GroupId: 0x0102 ◦ GroupKeySetId: 0x01a1 • List item 3: ◦ GroupId: 0x0103 | Verify that the DUT sends SUCCESS response. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3b | | | If the Groupcast cluster is NOT enabled on the RootNode endpoint, skip to step 4. TH sends Groupcast JoinGroup command with GroupID field set to 0x0103, Endpoints field set to ep 1 and KeySetID field set to 0x01a3 to DUT. | DUT responds with SUCCESS |

| # | Ref | | Test Step | Expected Outcome |
| 4 | CoreSpec- 9.10.5.3 | PICS | TH writes The ACL attribute in the Access Control cluster to add Manage privileges for group 0x0103 and maintain the current administrative privileges for the TH on the Access Control cluster. It also writes an acl entry to grant admin privilege on the Groupcast cluster if it is enabled on the RootNode endpoint. The following access control list shall be used: • List item 1 (TH admin): ◦ Privilege: Administer (5) ◦ AuthMode: CASE (2) ◦ Subjects: [ N1 ] ◦ Targets: [{Cluster: AccessControl (0x001f), Endpoint: 0}] • List item 2 (group Manage access): ◦ Privilege: Manage (4) ◦ AuthMode: Group (3) ◦ Subjects: group 0x0103 ([0x0103]) ◦ Targets: If the Groupcast cluster is enabled on the RootNode endpoint: {Cluster: Select a cluster On DUT ep 1 with attributes that are modified by a cluster command. e.g OnOff cluster, Endpoint: ep 1 }. Otherwise: {Cluster: Groups (0x0004), | Verify that the DUT sends SUCCESS response. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 5 | AppSpec- 1.3.7.2 | | If the Groupcast cluster is enabled on the RootNode endpoint, skip to step 8. TH sends a AddGroup Command to the Groups cluster on Endpoint PIXIT.G.ENDPOINT over CASE with the GroupID field set to 0x0104 and the GroupName set to an empty string | DUT responds with UNSUPPORTED_ACCESS |
| 6 | AppSpec- 1.3.7.2 | | TH sends a AddGroup Command to the Groups cluster with the GroupID field set to 0x0101 and the GroupName set to an empty string. The command is sent as a group command using GroupID 0x0103 | |
| 7 | AppSpec- 1.3.7.2 | | TH sends a AddGroup Command to the Groups cluster with the GroupID field set to 0x0102 and the GroupName set to an empty string. The command is sent as a group command using GroupID 0x0101 | |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 15 | | | If the Groupcast cluster is NOT enabled on the RootNode endpoint, skip to step 21. TH sends a group command requiring the Operate privilege, using any command and field values, to any cluster on an endpoint that is a member of GroupID 0x0103. | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 21 | AppSpec- 1.3.7.2 | | If the Groupcast cluster is enabled on the RootNode endpoint, skip to step 27. TH sends a ViewGroup Command to the Groups cluster on Endpoint PIXIT.G.ENDPOINT over CASE with the GroupID set to 0x0101 to confirm that the AddGroup command from step 6 was successful | DUT responds with SUCCESS |
| 22 | AppSpec- 1.3.7.2 | | TH sends a ViewGroup Command to the Groups cluster on Endpoint PIXIT.G.ENDPOINT over CASE with the GroupID set to 0x0102 to confirm that the AddGroup command from step 7 was not successful | DUT responds with NOT_FOUND |
| 23 | AppSpec- 1.3.7.2 | | TH sends a AddGroup Command to the Groups cluster with the GroupID field set to 0x0105 and the GroupName set to an empty string. The command is sent as a group command using GroupID 0x0103 | |
| 24 | AppSpec- 1.3.7.2 | | TH sends a ViewGroup Command to the Groups cluster on Endpoint PIXIT.G.ENDPOINT over CASE with the GroupID set to 0x0105 to confirm that the AddGroup command from step 23 was not successful | DUT responds with NOT_FOUND |
| 25 | AppSpec- 1.3.7.5 | | TH sends the RemoveAllGroups Command to the Groups cluster on Endpoint PIXIT.G.ENDPOINT over CASE | DUT responds with SUCCESS |
| 26 | | | TH calls the GetGroupMembership command from the Groups cluster | Verify that the group list is empty. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 27 | | | If the Groupcast cluster is NOT enabled on the RootNode endpoint, skip this step. TH sends Groupcast LeaveGroup command with GroupID field set to 0 to DUT over CASE. | DUT responds with SUCCESS |
| 28 | CoreSpec- 11.2.7.2 | | TH resets the GroupKeyMap attribute list on GroupKeyManagement cluster by writing the GroupKeyMap attribute with an empty list | Verify that the DUT sends SUCCESS response. |
| 29 | CoreSpec- 11.2.8.4 | | TH resets the key set by sending the KeySetRemove command to the GroupKeyManagement cluster over CASE with the following fields: • GroupKeySetID: 0x01a3 | Verify that the DUT sends SUCCESS response. |
| 30 | CoreSpec- 11.2.8.4 | | TH resets the key set by sending the KeySetRemove command to the GroupKeyManagement cluster over CASE with the following fields: • GroupKeySetID: 0x01a1 | Verify that the DUT sends SUCCESS response. |

## TC-ACE-2.1 Attribute read privilege enforcement - [DUT as Server]

## Purpose

Tests that all attributes on the DUT require the appropriate access control privilege for reading.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_commissioner | client - original commissioner, has full admin access |
| 2 | TH_second_controller | client - same fabric as TH_commissioner, no ACL access at the start of the test. Node id is second_controller_nodeid |
| 3 | DUT | server |

## Test Procedure

| # | Ref | PIC S | Test Step | Expected Outcome |
| 2 | | | TH_commissioner reads the ACL attribute from the Access Control Cluster and saves it as default_acl | |
| 3 | | | Repeat steps 3a and 3b for each privilege level in the set of supported privilege levels (view, operate, manage, administer) using acl_privilege to denote the current privilege level under test: | |

| 3a | TH_commissioner appends an entry to default_acl to give limited permissions to TH_second_controller and writes the new list to the ACL attribute. The new entry is as follows: • struct ◦ privilege: acl_privilege ◦ authmode: CASE ◦ subjects: [ second_controller_nodeid ] ◦ targets: [] | |
| 3b | For each endpoint on the DUT, for each standard cluster on the endpoint, and for each standard and global attribute on the cluster, TH_second_controller reads the attribute | If acl_privilege is greater than or equal to the minimum required privilege for read as defined in the spec, verify that an attribute value is returned. Otherwise, verify that UNSUPPORTED_ACCESS is returned. |

## TC-ACE-2.2 Attribute write privilege enforcement - [DUT as Server]

## Purpose

Tests that all attributes on the DUT require the appropriate access control privilege for writing and that non-writeable attributes cannot be written.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_commissioner | client - original commissioner, has full admin access |

| 2 | TH_second_controller | client - same fabric as TH_commissioner, no ACL access at the start of the test. Node id is second_controller_nodeid |
| 3 | DUT | server |

## Test Procedure

| # | Ref | PIC S | Test Step | Expected Outcome |
| 2 | | | TH_commissioner reads the ACL attribute from the Access Control Cluster and saves it as default_acl | |
| 3 | | | TH_commissioner appends an entry to default_acl to give admin permissions to TH_second_controller and writes the new list to the ACL attribute. The new entry is as follows: • struct ◦ privilege: administer ◦ authmode: CASE ◦ subjects: [ second_controller_nodeid ] ◦ targets: [] | |
| 4 | | | TH_second_controller performs a wildcard read of the DUT to establish a viable set of attribute values for writing | |
| 5 | | | Repeat steps 5a and 5b for each privilege level in the set of supported privilege levels (view, operate, manage, administer) using acl_privilege to denote the current privilege level under test: | |

| 5a | TH_commissioner appends an entry to default_acl to give limited permissions to TH_second_controller and writes the new list to the ACL attribute. The new entry is as follows: • struct ◦ privilege: acl_privilege ◦ authmode: CASE ◦ subjects: [ second_controller_nodeid ] ◦ targets: [] | |
| 5b | For each endpoint on the DUT, for each standard cluster on the endpoint, and for each standard and global attribute on the cluster, TH_second_controller writes the attribute as follows: • If the attribute is the ACL and acl_privilege is administer, skip this step • If the attribute is a list, write an empty list • If the attribute is not a list, write back the value read during step 4. Save the returned value as write_response . If write_response is SUCCESS and the attribute is a list, write the attribute with the value read during step 4. | • If the attribute is NOT writeable per the spec, verify write_response is UNSUPPORTED_WRITE • If the attribute is OPTIONALLY writeable per the spec, write_response MAY be UNSUPPORTED_WRITE. Otherwise, treat as a writeable attribute. • If the attribute is writable per the spec and acl_privilege is greater than or equal to the minimum required privilege for write, verify write_response is NOT UNSUPPORTED_ACCESS. Other error codes are acceptable. • If the attribute is writeable per spec and acl_privilege is less the minimum required |

## TC-ACE-2.3 Command privilege enforcement - [DUT as Server]

## Purpose

Tests that all commands on the DUT require the appropriate access control privilege.

## PICS

- MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_commissioner | client - original commissioner, has full admin access |
| 2 | TH_second_controller | client - same fabric as TH_commissioner, no ACL access at the start of the test. Node id is second_controller_nodeid |
| 3 | DUT | server |

## Test Procedure

| # | TestStep | Expected Outcome |
| precondi tion | DUT is commissioned | |
| 1 | TH_commissioner performs a wildcard read | |
| 2 | TH_commissioner reads the ACL attribute | |
| 3 | Repeat steps 3a and 3b for each permission level acl_privilege | |
| 3a | TH_commissioner appends an entry to default_acl to give limited permissions to TH_second_controller and writes the new list to the ACL attribute. The new entry is as follows: • struct ◦ privilege: acl_privilege ◦ authmode: CASE ◦ subjects: [ second_controller_nodeid ] ◦ targets: [] | |

| 3b | For each standard command on each standard cluster on each endpoint, TH_second_controller checks the permission requirements for that command. If the permission required for the command is HIGHER than the permission level being tested, TH_second_controller sends the command to the DUT using default values. Regardless of the command contents, the DUT should return an access error since access must be checked before the command is processed. Receipt of an UNSUPPORTED_COMMAND error is a conformance failure. | DUT returns UNSUPPORTED_ACCESS error |

## TC-ACE-2.4 Attribute read subscription report - [DUT as Server]

## Purpose

Tests that all attributes on the DUT require the appropriate access control privilege for reading.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Pre-Conditions

| # | Doc Ref | Condition | Notes |
| 1 | 9.10 ACL Cluster | ARL Entries Cleared | If this device supports Managed Device feature (MNGD) of the ACL Cluster, then instructions must be provided by device maker for removing all access restrictions from DUT. This test case should be run after following these instructions to remove all restrictions. |

## Required Devices

| # | Device Name | Device Description |
| 1 | TH_commissioner | client - original commissioner, has full admin access |

| 2 | TH_second_controller | client - same fabric as TH_commissioner, no ACL access at the start of the test. Node ID is second_controller_nodeid |
| 3 | DUT | server |

## Test Procedure

| # | Ref | PIC S | Test Step | Expected Outcome |
| 2 | | | TH_commissioner reads the ACL attribute from the Access Control Cluster and saves it as default_acl | |
| 3 | | | Repeat steps 3a and 3b for each privilege level in the set of supported privilege levels (view, operate, manage, administer) using acl_privilege to denote the current privilege level under test: | |
| 3a | | | TH_commissioner appends an entry to default_acl to give limited permissions to TH_second_controller and writes the new list to the ACL attribute. The new entry is as follows: • struct ◦ privilege: acl_privilege | |
| 3b | | | TH_second_controller subscribes to all the attributes and verifies the subscription is established and priming report is received with appropriate permission errors | • Subscription is established and the priming report sent if the subscription is permitted. • If subscription is not permitted due to ACL privilege level being used the subscription fails with an appropriate permission-related error. |

## Chapter 17. ICD Management Cluster Test Plan

## 17.1. PICS Definition

This section covers the ICD Management Cluster Test Plan related PICS items that are referenced in the following test cases.

Support for an item is considered as "true" for conditional statements within the test case steps.

## 17.1.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S | Does the device implement the ICD Management Cluster as a server? | O | |
| ICDM.C | Does the device implement the ICD Management Cluster as a client? | O | |

## 17.1.2. Server

## Features

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S.F00(CIP) | Does the device support attributes and commands for the Check-In Protocol feature? | ICDM.S.F02(LITS), O | |
| ICDM.S.F01(UAT) | Does the device support the user active mode trigger feature? | ICDM.S.F02(LITS), O | |
| ICDM.S.F02(LITS) | Does the device support operating as a Long Idle Time ICD? | ICDM.S.F02(LITS) | |

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S.F03(DSLS) | Does the device support dynamic switching from Short Idle Time to Long Idle Time operating modes? | [ICDM.S.F02(LITS)] | |

1 : if the DUT supports LIT it SHALL also support LITS

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S.A0000(IdleMod eDuration) | Does the device implement the IdleModeDuration attribute? | ICDM.S:M | |
| ICDM.S.A0001(ActiveM odeDuration) | Does the device implement the ActiveModeDuration attribute? | ICDM.S:M | |
| ICDM.S.A0002(ActiveM odeThreshold) | Does the device implement the ActiveModeThreshold attribute? | ICDM.S:M | |
| ICDM.S.A0003(Registere dClients) | Does the device implement the RegisteredClients attribute? | ICDM.S.F00(CIP) | |
| ICDM.S.A0004(ICDCoun ter) | Does the device implement the ICDCounter attribute? | ICDM.S.F00(CIP) | |
| ICDM.S.A0005(ClientsSu pportedPerFabric) | Does the device implement the ClientsSupportedPerFab ric attribute? | ICDM.S.F00(CIP) | |
| ICDM.S.A0006(UserActi veModeTriggerHint) | Does the device implement the UserActiveModeTrigger Hint attribute? | ICDM.S.F01(UAT) | |

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S.A0007(UserActi veModeTriggerInstructi on) | Does the device implement the UserActiveModeTrigger Instruction attribute? | [ICDM.S.F01(UAT)] | |
| ICDM.S.A0008(Operatin gMode) | Does the device implement the OperatingMode attribute? | ICDM.S.F02(LITS) | |
| ICDM.S.A0009(Maximu mCheckInBackoff) | Does the device implement the MaximumCheckInBacko ff attribute? | ICDM.S.F00(CIP) | |

## Commands received

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S.C00.Rsp(Registe rClient) | Does the device implement receiving the RegisterClient command? | ICDM.S.F00(CIP) | |
| ICDM.S.C02.Rsp(Unregi sterClient) | Does the device implement receiving the UnregisterClient command? | ICDM.S.F00(CIP) | |
| ICDM.S.C03.Rsp(StayAct iveRequest) | Does the device implement receiving the StayActiveRequest command? | ICDM.S.F02(LITS), O | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.S.C01.Tx(Register ClientResponse) | Does the device implement sending the RegisterClientResponse command? | ICDM.S.F00(CIP) | |
| ICDM.S.C04.Tx(StayActi veResponse) | Does the device implement sending the StayActiveResponse command? | ICDM.S.F02(LITS), O | |

## 17.1.3. Client

## Features

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.C.F00(CIP) | Does the device support attributes and commands for the Check-In Protocol? | ICDM.C:O | |
| ICDM.C.F01(UAT) | Does the device support the user active mode trigger feature? | ICDM.C:O | |
| ICDM.C.F02(LITS) | Does the device support operating as a Long Idle Time ICD? | ICDM.C:O | |
| ICDM.C.F03(DSLS) | Does the device support dynamic switching from Short Idle Time to Long Idle Time operating modes? | ICDM.C:O | |

## Attributes

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.C.A0000(IdleMod eDuration) | Does the device implement the IdleModeDuration attribute? | ICDM.C:O | |
| ICDM.C.A0001(ActiveM odeDuration) | Does the device implement the ActiveModeDuration attribute? | ICDM.C:O | |
| ICDM.C.A0002(ActiveM odeThreshold) | Does the device implement the ActiveModeThreshold attribute? | ICDM.C:O | |
| ICDM.C.A0003(Register edClients) | Does the device implement the RegisteredClients attribute? | ICDM.C:O | |

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.C.A0004(ICDCoun ter) | Does the device implement the ICDCounter attribute? | ICDM.C:O | |
| ICDM.C.A0005(ClientsS upportedPerFabric) | Does the device implement the ClientsSupportedPerFab ric attribute? | ICDM.C:O | |
| ICDM.C.A0006(UserActi veModeTriggerHint) | Does the device implement the UserActiveModeTrigger Hint attribute? | ICDM.C:O | |
| ICDM.C.A0007(UserActi veModeTriggerInstructi on) | Does the device implement the UserActiveModeTrigger Instruction attribute? | ICDM.C:O | |
| ICDM.C.A0008(Operatin gMode) | Does the device implement the OperatingMode attribute? | ICDM.C:O | |
| ICDM.C.A0009(Maximu mCheckInBackoff) | Does the device implement the MaximumCheckInBacko ff attribute? | ICDM.C:O | |

## Commands received

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.C.C01.Rsp(Registe rClientResponse) | Does the device support receiving the RegisterClientResponse command? | ICDM.C:O | |
| ICDM.C.C04.Rsp(StayAct iveResponse) | Does the device implement receiving the StayActiveResponse command? | ICDM.C:O | |

## Commands generated

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDM.C.C00.Tx(Register Client) | Does the device support sending the RegisterClient command? | ICDM.C:O | |
| ICDM.C.C02.Tx(Unregist erClient) | Does the device implement sending the UnregisterClient command? | ICDM.C:O | |
| ICDM.C.C03.Tx(StayActi veRequest) | Does the device implement sending the StayActiveRequest command? | ICDM.C:O | |

## 17.2. PIXIT Definition

This section covers the ICD Management Cluster related PIXIT items that might be required in the following test cases.

Table 2.1: Defined Variables

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PIXIT.ICDM.TEST_EVEN T_TRIGGER_KEY | 128-bit test event trigger enable key | ICDM.S:M | Variable value is specific to each device manufacturer. |
| PIXIT.ICDM.TEST_EVEN T_TRIGGER | 64-bit device test event trigger key | ICDM.S:M | Variable value for triggered event is defined in table below. |

## 17.3. PIXIT Variable Values

This section covers the ICD Management Cluster Test Plan related PIXIT variable values that might be required in the following test cases.

Table 3.1: PIXIT.ICDM.TEST\_EVENT\_TRIGGER vs. Triggered Event

| PIXIT.ICDM.TEST_EVE NT_TRIGGER | Triggered Event | Conformance | Notes/Additional Constraints |
| 0x0046000000000001 | Adds the test event trigger ActiveMode requirement | ICDM.S:M | Triggering this event multiple times only adds a single requirement |

| 0x0046000000000002 | Removes the test event trigger ActiveMode requirement | ICDM.S:M | Triggering this event multiple times only removes a single requirement |

## Table 3.2: PIXIT Variable Values

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| {PIXIT.WAITTIME.REB OOT} | Integer indicating the wait time for the DUT to wait before continuing after a reboot | CIP:M | |

## 17.4. Test Case List

| TC UUID | Test Case Name |
| TC-ICDM-2.1 | Attributes with DUT as Server |
| TC-ICDM-3.1 | Register/Unregister Clients with DUT as Server |
| TC-ICDM-3.2 | Verify RegisterClient Command with DUT as Server |
| TC-ICDM-3.3 | Verify UnregisterClient Command with DUT as Server |
| TC-ICDM-3.4 | ICDCounter Persistence with DUT as Server |
| TC-ICDM-4.1 | Stay Active Request with DUT as Server |
| TC-ICDM-5.1 | Operating Mode with DUT as Server |
| TC-ICDM-5.2 | Operating Mode with DUT as Server - Multi-Fabrics |
| TC-ICDM-6.1 | Functionality with DUT as Client |

## Note:

If the DUT or TH is a LIT device,

- if test event trigger can be used to force the DUT to stay in active mode for the duration of test, user active mode trigger is not required;
- otherwise, prior to sending command to the DUT or TH, one can either wait for the DUT or TH to switch to active mode when the IdleModeDuration expires, or use the user active mode trigger to trigger the DUT or TH to switch to active mode.

## 17.5. Test Cases

## 17.5.1. Attribute test cases

## TC-ICDM-2.1 Attributes with DUT as Server

## Purpose

This test case verifies the non-global attributes of the ICD Management Cluster server.

## PICS

- ICDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | Commission DUT to TH (can be skipped if done in a preceding test). | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 5 | C.9. 17. 6.6 | ICDM.S. A0005(Cl ientsSup portedP erFabric ) | TH reads from the DUT the ClientsSupportedPerFabric attribute. | Verify that the DUT response contains an uint16. Value has to be between a range of 1 and up |
| 8 | C.9. 17. 6.7 | ICDM.S. A0006(U serActiv eModeT riggerHi nt) | TH reads from the DUT the UserActiveModeTriggerHint attribute. | Verify that the DUT response contains an bitmap32. - Multiple bits in the bitmap maybe set at the same time. - No more than one bit which has dependency on the UserActiveModeTriggerInstruction shall be set: bit 2, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16. |

| # | Ref | PICS | Test Step | Expected Outcome |
| 9 | C.9. 17. 6.8 | ICDM.S. A0007(U serActiv eModeT riggerIn structio n) | TH reads from the DUT the UserActiveModeTriggerInstruction attribute. | The value is encoded as a valid UTF-8 string with max length of 128 bytes. If UserActiveModeTriggerHint in step 8 is one of the following, DUT responses a value consists solely of an encoding of N as decimal unsigned integer using the ASCII digits 0-9, and without leading zeros. 5 - ActuateSensorSeconds 6 - ActuateSensorTimes 10 - ResetButtonSeconds 11 - ResetButtonTimes 13 - SetupButtonSeconds 15 - SetupButtonTimes If bit 2 in UserActiveModeTriggerHint in step 8 is set, UserActiveModeTriggerInstruction SHALL indicate a user instruction text string. If one of bit 7, 9, 14 in UserActiveModeTriggerHint in step 8 is set, UserActiveModeTriggerInstruction SHALL consist of exactly 6 hexadecimal digits using the ASCII characters 0-F and encoding the RGB color value as used in HTML |

## Notes/Testing Considerations

## 17.5.2. Functional test cases

## TC-ICDM-3.1 Register/Unregister Clients with DUT as Server

## Purpose

This test case verifies the limit of ClientsSupportedPerFabric with RegisterClient and UnregisterClient commands.

## PICS

- ICDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission DUT to TH (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH reads from the DUT the FeatureMap . If the CIP feature is not supported on the cluster, skip all remaining steps | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 6 | C.9. 17. 7.1 | | TH sends RegisterClient command. - CheckInNodeID: registering client's node ID - MonitoredSubject: MonitoredSubID - Key: shared secret between the client and the ICD - ClientType : Ephemeral(1) | Verify DUT responds w/ status SUCCESS(0x00). Verify that the DUT response contains the value of ICDCounter which should be equal or greater than the IcdCounter in Step 5. |
| 8 | C.9. 17. 7.1 | | If len(RegisteredClients) is less than ClientsSupportedPerFabric , TH repeats RegisterClient command with different CheckInNodeID(s) and the Permanent(0) ClientType until the number of entries in RegisteredClients equals ClientsSupportedPerFabric . | Verify DUT responds w/ status SUCCESS(0x00). Verify that the DUT response contains the value(s) of ICDCounter(s) which should be equal or greater than the IcdCounter in Step 5. |

| # | Ref | PICS | Test Step | Expected Outcome |

## Post-Conditions

| # | Post-Condition |
| 1 | TH reads from the DUT the RegisteredClients attribute. RegisteredClients is empty. |

## Notes/Testing Considerations

- CheckInNodeID: any random node ID
- MonitorSubID: any random subject ID
- Key: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef

## TC-ICDM-3.2 Verify RegisterClient Command with DUT as Server

## Purpose

This test case verifies the Verify RegisterClient command functionality/constraints of the ICD Management Cluster server.

- ICDM.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission TH to DUT (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 2c | | | Power cycle DUT | |
| 2d | | | TH waits for {PIXIT.WAITTIME.REBOOT} | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3a | C.9. 17. 7.1 | | TH sends RegisterClient command with same CheckInNodeID1 as in Step 2a and different MonitoredSubID2 and Key2 . - CheckInNodeID: CheckInNodeID1 - MonitoredSubject: MonitoredSubID2 - Key: Key2 | Verify DUT responds w/ status SUCCESS(0x00); + |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 8c | C.9. 17. 7.1 | | TH sends RegisterClient command with same CheckInNodeID5 as in Step 8a and different MonitoredSubID7 and Key7 , and an valid wrong VerificationKey7 - CheckInNodeID: CheckInNodeID5 - MonitoredSubject: MonitoredSubID7 - Key: Key7 - VerificationKey: VerificationKey7 | Verify DUT responds w/ status FAILURE(0x01). |
| 8d | C.9. 17. 7.1 | | TH sends RegisterClient command with same CheckInNodeID5 and VerificationKey5 as in Step 8a and different MonitoredSubID9 and Key9 - CheckInNodeID: CheckInNodeID5 - MonitoredSubject: MonitoredSubID9 - Key: Key9 - VerificationKey: VerificationKey5 | Verify DUT responds w/ status SUCCESS(0x00). |

## Post-Conditions

| # | Post-Condition |
| 1 | Re-enable TH admin access to ICD management cluster. TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing a single element, restoring full access to the node. . struct - Fabric Index: 1 - Privilege field: Administer (5) - AuthMode field: CASE (2) - Subjects field: [ N1 ] - Targets field: null 2 |

## Notes/Testing Considerations

- CheckInNodeID: any random node ID
- MonitorSubID: any random subject ID
- Key: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef
- VerificationKey: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef

## TC-ICDM-3.3 Verify UnregisterClient Command with DUT as Server

## Purpose

This test case verifies the Verify UnregisterClient command functionality/constraints of the ICD Management Cluster server.

## PICS

- ICDM.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission TH to DUT (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |
| 7 | | | Set the TH to Manage privilege for ICDM cluster. TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing 2 elements, giving itself administer privilege only on the Access Control cluster and manage privilege on everything else on EP0. • struct ◦ Fabric Index: 1 ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] ◦ Targets field: [{Cluster: 0x001F, Endpoint: 0}] • struct ◦ Fabric Index: 1 ◦ Privilege field: Manage (4) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] | Verify DUT responds w/ status SUCCESS(0x00). |
| 8a | C.9. 17. 7.1 | | TH sends RegisterClient command. - CheckInNodeID: CheckInNodeID8 - MonitoredSubject: MonitoredSubID8 - Key: Key8 + | Verify DUT responds w/ status SUCCESS(0x00). |
| 8b | C.9. 17. 7.3 | | TH sends UnregisterClient command with the CheckInNodeID8 from Step 8a and an invalid VerificationKey9 . - CheckInNodeID: CheckInNodeID8 - VerificationKey: VerificationKey9 | Verify DUT responds w/ status FAILURE(0x01). |
| 8c | C.9. 17. 7.3 | | TH sends UnregisterClient command with the CheckInNodeID8 from Step 8a and a valid wrong VerificationKey10 . - CheckInNodeID: CheckInNodeID8 - VerificationKey: VerificationKey10 | Verify DUT responds w/ status FAILURE(0x01). |

| # | Ref | PICS | Test Step | Expected Outcome |
| 8d | C.9. 17. 7.3 | | TH sends UnregisterClient command with the CheckInNodeID8 and VerificationKey8 from Step 8a. - CheckInNodeID: CheckInNodeID8 - VerificationKey: VerificationKey8 | Verify DUT responds w/ status SUCCESS(0x00). |

## Post-Conditions

| # | Post-Condition |
| 1 | Re-enable TH admin access to ICD management cluster. TH writes the ACL attribute with a list of AccessControlEntryStruct entries containing a single element, restoring full access to the node. 1. struct ◦ Fabric Index: 1 ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) ◦ Subjects field: [ N1 ] |

## Notes/Testing Considerations

- CheckInNodeID: any random node ID
- MonitorSubID: any random subject ID
- Key: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef
- VerificationKey: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef

## TC-ICDM-3.4 ICDCounter Persistence with DUT as Server

## Purpose

This test case verifies the Verify ICDCounter persistence after reboot of the ICD Management Cluster server.

## PICS

- ICDM.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission TH to DUT (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | Test Step | Expected Outcome |
| 2a | | Power cycle DUT | |
| 2b | | TH waits for {PIXIT.WAITTIME.REBOOT} | |
| 3 | C.9. 17. 6.5 | TH reads from the DUT the ICDCounter attribute. | Verify that the DUT response contains value of ICDCounter and stores in IcdCounter2 . IcdCounter2 is greater or equal to IcdCounter1 . ICDCounter attribute can roll over. If the attribute rolls over, it will be greater or equal to 0. |

## Notes/Testing Considerations

## TC-ICDM-4.1 Stay Active Request with DUT as Server

## Purpose

This test case verifies the Stay Active Request functionality of the ICD Management Cluster server.

## PICS

- ICDM.S
- ICDM.S.F02(LITS)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH and DUT are on the same fabric.

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission DUT to TH (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | C.9. 17. 7.4 | | TH sends StayActiveRequest command with StayActiveDuration greater than or equal 30000 milliseconds. | Verify DUT responds w/ status SUCCESS(0x00). Verify that the DUT response contains PromisedActiveDuration1 , which shall be greater than or equal to 30000 milliseconds. |

## Notes/Testing Considerations

## TC-ICDM-5.1 Operating Mode with DUT as Server

## Purpose

This test case verifies the LIT devices operating mode functionality with single fabric.

## PICS

- ICDM.S
- ICDM.S.F02(LITS)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission TH to DUT (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 3a | C.9. 17. 7.1 | | TH sends RegisterClient command. - CheckInNodeID: CheckInNodeID1 - MonitoredSubject: MonitoredSubID1 - Key: Key1 | Verify DUT responds w/ status SUCCESS(0x00); |

## Post-Conditions

| # | Post-Condition |
| 1 | TH reads from the DUT the RegisteredClients attribute. RegisteredClients is empty. |

## Notes/Testing Considerations

## TC-ICDM-5.2 Operating Mode with DUT as Server - Multi-Fabrics

## Purpose

This test case verifies the LIT devices operating mode functionality with multi-fabrics.

## PICS

- ICDM.S
- ICDM.S.F02(LITS)

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | DUT as Server |
| 2 | TH1 | TH1 as Client |
| 3 | TH2 | TH2 as Client |

## Pre-Conditions

| # | Pre-Condition |
| 1a | Commission DUT to TH1's Fabric with NodeId1 |
| 1b | Commission DUT to TH2's Fabric with NodeId2 |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | TH1 reads from the DUT the RegisteredClients attribute. RegisteredClients is empty. | |
| 1b | | | TH2 reads from the DUT the RegisteredClients attribute. RegisteredClients is empty. | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2 | C.9. 17. 7.1 | | TH1 sends RegisterClient command. - CheckInNodeID: CheckInNodeID1 - MonitoredSubject: MonitoredSubID1 - Key: Key1 | Verify DUT responds w/ status SUCCESS(0x00); Verify that the DUT response contains ICDCounter . |
| 4 | C.9. 17. 7.1 | | TH2 sends RegisterClient command. - CheckInNodeID: CheckInNodeID2 - MonitoredSubject: MonitoredSubID2 - Key: Key2 | Verify DUT responds w/ status SUCCESS(0x00); Verify that the DUT response contains ICDCounter . |

## Notes/Testing Considerations

## TC-ICDM-6.1 Functionality with DUT as Client

## Purpose

This test case verifies the register/unregister client functionality of the cluster client.

## · ICDM.C

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Server. |
| 2 | DUT | DUT as Client. |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission TH to DUT (can be skipped if done in a preceding test)

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | ICDM.C. C00.Tx( Registe rClient) | DUT issues an C_REGISTER_CLIENT command to the Test Harness. | If ICDM.C.C00.Tx(RegisterClient), Test Harness receives the C_REGISTER_CLIENT command from the DUT. Verify the command has following parameters: - ID 0 (CheckInNodeID): the type is a valid node-id . - ID 1 (MonitoredSubject): the type is a valid subject-id . - ID 2 (Key): the type is an octstr . - Optional ID 3 (VerificationKey): the type is an octstr . |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | | ICDM.C. C03.Tx( StayAct iveReq uest) | DUT issues an C_STAY_ACTIVE_REQUEST command to the Test Harness. | If ICDM.C.C03.Tx(StayActiveRequest), Test Harness receives the C_STAY_ACTIVE_REQUEST command from the DUT. Verify the command has following parameters: - ID 0 (StayActiveDuration): the type is a uint32 . |

## Notes/Testing Considerations

## Chapter 18. ICD Behavior Test Plan

## 18.1. PIXIT Definition

This section covers the ICD Behavior related PIXIT items that might be required in the following test cases.

Table 2.1: Defined Variables

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PIXIT.ICDB.TEST_EVEN T_TRIGGER_KEY | 128-bit test event trigger enable key | ICDB.S:M | Variable value is specific to each device manufacturer. |
| PIXIT.ICDB.TEST_EVEN T_TRIGGER | 64-bit device test event trigger key | ICDB.S:M | Variable value for triggered event is defined in table below. |

## 18.2. PIXIT Variable Values

This section covers the ICD Behavior Test Plan related PIXIT variable values that might be required in the following test cases.

Table 3.1: PIXIT.ICDB.TEST\_EVENT\_TRIGGER vs. Triggered Event

| PIXIT.ICDB.TEST_EVE NT_TRIGGER | Triggered Event | Conformance | Notes/Additional Constraints |
| 0x0046000000000001 | Adds the test event trigger ActiveMode requirement | ICDB.S:M | Triggering this event multiple times only adds a single requirement |
| 0x0046000000000002 | Removes the test event trigger ActiveMode requirement | ICDB.S:M | Triggering this event multiple times only removes a single requirement |
| 0x0046000000000003 | Invalidate ICD half counter values | ICDB.S:M | Triggering this event invalidate ICD half counter values 2^31. |

Table 3.2: PIXIT Variable Values

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| {PIXIT.WAITTIME.REB OOT} | Integer indicating the wait time for the DUT to wait before continuing after a reboot | CIP:M | |

## 18.3. PICS Definition

This section covers the ICD Behavior Cluster Test Plan related PICS items that are referenced in the following test cases.

Support for an item is considered as "true" for conditional statements within the test case steps.

## 18.3.1. Role

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| ICDB.S | Does the device implement the ICD Behavior as a server? | O | |
| ICDB.C | Does the device implement the ICD Behavior as a client? | O | |

## 18.4. Test Case List

| TC UUID | Test Case Name |
| TC-ICDB-1.1 | ICD Check-In Protocol - Register client - idle mode duration [DUT as Server] |
| TC-ICDB-1.2 | ICD Check-In Protocol - Register client - user active mode trigger [DUT as Server] |
| TC-ICDB-1.3 | ICD Check-In Protocol - Client response [DUT as Client] |
| TC-ICDB-2.1 | ICD State Machine - With client registration and no active subscription - Single Fabric [DUT as Server] |
| TC-ICDB-2.2 | ICD State Machine - With client registration and active subscription - Single Fabric [DUT as Server] |
| TC-ICDB-2.3 | ICD State Machine - With client registrations and no active subscription - Multiple Fabrics [DUT as Server] |
| TC-ICDB-2.4 | ICD State Machine - With client registrations and active subscriptions - Multiple Fabrics [DUT as Server] |
| TC-ICDB-2.5 | ICD State Machine - With 1 client registration with subscription and 1 unregistered client with subscription - Multiple Fabrics [DUT as Server] |

| TC-ICDB-3.1 | ICD Dynamic SIT/LIT - Verify OperatingMode transition between LIT and SIT when there is client registration with DUT as Server |
| TC-ICDB-3.2 | ICD Dynamic SIT/LIT - Verify OperatingMode does not transition between LIT and SIT when there is no client registration with DUT as Server |

## 18.5. Test Cases

## 18.5.1. ICD Check-In Protocol test cases

## TC-ICDB-1.1 ICD Check-In Protocol - Register client - idle mode duration [DUT as Server]

## Purpose

Test validates that an ICD will send Check-In messages when entering Active mode if no subscription is active.

This test validates device enters active mode after idle mode duration.

## PICS

- ICDB.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission DUT to TH (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | TH reads from the DUT the RegisteredClients attribute. | RegisteredClients is empty. If not empty, TH sends command UnregisterClient to clear all clients in RegisteredClients . |

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | | | Wait for DUT transition to Idle Mode | |
| 4 | | | Wait for 1 or more cycle of IdleModeDuration | DUT sends check-in message to the TH after each IdleModeDuration with Payload - Check-In Counter: greater than ICDCounter in Step 2. - Application Data: matches ActiveModeThreshold in Step 1. |

## Post-Conditions

- # Post-Condition
- 1 TH sends command UnregisterClient to clear all clients in RegisteredClients , if any.

## Notes/Testing Considerations

- CheckInNodeID: the NodeID of the TH.
- MonitoredSubID: the NodeID of the TH.
- Key: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef

## TC-ICDB-1.2 ICD Check-In Protocol - Register client - user active mode trigger [DUT as Server]

## Purpose

Test validates that an ICD will send Check-In messages when entering Active mode if no subscription is active.

This test validates device enters active mode when using the user active mode trigger.

## PICS

- ICDB.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |

| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission DUT to TH (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 3 | | | Wait for DUT transition to Idle Mode | |
| 4a | | | Use UserActiveModeTriggerHint / UserActiveModeTriggerInstruction to put device in active mode. Vendor specific interaction/action is required. | DUT sends check-in message to the TH with Payload - Check-In Counter: greater than ICDCounter in Step 2. - Application Data: matches ActiveModeThreshold in Step 1. |

## Post-Conditions

| # | Post-Condition |
| 1 | TH sends command UnregisterClient to clear all clients in RegisteredClients , if any. |

## Notes/Testing Considerations

- CheckInNodeID: any random node ID
- MonitoredSubID: any random subject ID
- Key: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef

## TC-ICDB-1.3 ICD Check-In Protocol - Client response [DUT as Client]

## Purpose

This test case verifies client response to valid/invalid check-in counter

## PICS

- ICDB.C

## Required Devices

| # | Device Name | Device Description |
| 1 | TH1 | TH as Server |
| 2 | TH2 | TH as Client; TH2 should a client able to send TestEventTrigger commands, eg. chip-tool. |
| 3 | DUT | DUT as Client |

## Device Topology

TH and DUT are on the same fabric.

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission TH1 to DUT (can be skipped if done in a preceding test) |
| 2 | Commission TH1 to TH2 (can be skipped if done in a preceding test) |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | DUT sends RegisterClient command. - CheckInNodeID: CheckInNodeID - MonitoredSubject: MonitoredSubID - Key: Key1 | Verify TH responds w/ status SUCCESS(0x00). Verify that the TH response contains ICDCounter1 . |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

- CheckInNodeID: any random node ID
- MonitoredSubID: any random subject ID
- Key: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef Test event trigger is required in Step 2.

## 18.5.2. ICD State Machine test cases

## TC-ICDB-2.1 ICD State Machine - With client registration and no active subscription - Single Fabric [DUT as Server]

## Purpose

Verify that after client registration, ICD state machine enters check-in state and periodically sends check-in message if there is no active subscription session presences.

## PICS

- ICDB.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Pre-Conditions

| # | Pre-Condition |
| 1 | DUT not commission to TH. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | Commission DUT to TH using NodeID and register ICD client during commissioning. | Verify DUT responds w/ status SUCCESS(0x00). Verify that the DUT response contains CheckInNodeID , MonitoredSubID , Key , and ICDCounter . |

## Notes/Testing Considerations

## TC-ICDB-2.2 ICD State Machine - With client registration and active subscription - Single Fabric [DUT as Server]

## Purpose

Verify that after client registration and subscription request, ICD state machine enters subscribed state, periodically sends subscription reports, and stop sending check-in message till subscription is torn down.

## PICS

- ICDB.S
- ICDM.S.F00(CIP)

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Pre-Conditions

| # | Pre-Condition |
| 1 | DUT not commission to TH. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

1. If DUT supports ICDM.S.F01(UAT) , transition from Idle Mode to Active Mode can be achieved by using a supported UserActiveModeTriggerHint .

## TC-ICDB-2.3 ICD State Machine - With both client registrations and no active subscription Multiple Fabrics [DUT as Server]

## Purpose

Verify that after multiple client registrations, ICD state machine enters check-in state for each client and periodically sends check-in message if there is no active subscription session presences on any fabrics.

## PICS

- ICDB.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |
| 3 | TH2 | Commissioner |

## Pre-Condition

| # | Pre-Condition |
| 1a | DUT not commission to TH1. |
| 1b | DUT not commission to TH2. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | Commission DUT to TH1 using NodeID1 and register ICD client during commissioning. | Verify DUT responds w/ status SUCCESS(0x00). Verify that the DUT response contains CheckInNodeID1 , MonitoredSubID1 , Key1 , and ICDCounter1 . |
| 1b | | | Commission DUT to TH2 using NodeID2 and register ICD client during commissioning. | Verify DUT responds w/ status SUCCESS(0x00). Verify that the DUT response contains CheckInNodeID2 , MonitoredSubID2 , Key2 , and ICDCounter2 . |

| 3 | | Wait for 1 or more IdleModeDuration | DUT sends periodic check-in message to TH1 and TH2 with updated ICDCounters . Both TH1 and TH2 receive the same ICDCounter : ICDCounter1 + Offset1 = ICDCounter2 + Offset2 . |

## Notes/Testing Considerations

## TC-ICDB-2.4 ICD State Machine - Multiple Fabrics [DUT as Server]

## Purpose

Verify that with multiple fabrics, as long as there is 1 or more client registration and 1 or more active subscriptions, ICD state machine enters subscribed state, periodically sends subscription reports, and stops sending check-in message.

ICD state machine would return to check-in state and resume periodic check-in message if there is no more active subscription on any fabrics.

## PICS

- ICDB.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |

| # | Device Name | Device Description |
| 2 | TH1 | Commissioner |
| 3 | TH2 | Commissioner |

## Pre-Condition

| # | Pre-Condition |
| 1a | DUT not commission to TH1. |
| 1b | DUT not commission to TH2. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 3a | | | DUT and TH1/TH2 activate the subscription and subscribe to all, with MinIntervalFloor and MaxIntervalCeiling . | Verify that the DUT response contains MaxInterval where MinIntervalFloor ≤ MaxInterval ≤ MAX(SUBSCRIPTION_MAX_INTERVAL _PUBLISHER_LIMIT, MaxIntervalCeiling) to both TH1 and TH2. |

| 5 | Deactivate subscriptions between DUT and TH2, and wait for 1 or more IdleModeDuration . | DUT sends periodic check-in message to both TH1 and TH2 with updated ICDCounter : ICDCounter1 + Offset1 = ICDCounter2 + Offset2 . DUT stops subscription reports to both TH1 and TH2. |

## Notes/Testing Considerations

## TC-ICDB-2.5 ICD State Machine - With 1 client registration with subscription and 1 unregistered client with subscription - Multiple Fabrics [DUT as Server]

## Purpose

This test case verifies the ICD server behaviour with 1 client registration with subscription and 1 unregistered client with subscription with multiple fabrics.

## PICS

- ICDB.S
- ICDM.S.F00(CIP)

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT | Commissionee |
| 2 | TH1 | Commissioner |
| 3 | TH2 | Commissioner |

## Pre-Condition

| # | Pre-Condition |
| 1a | DUT not commission to TH1. |
| 1b | DUT not commission to TH2. |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1a | | | Commission DUT to TH1 using NodeID1 and register ICD client during commissioning. | Verify DUT responds w/ status SUCCESS(0x00). Verify that the DUT response contains CheckInNodeID1 , MonitoredSubID1 , Key1 , and ICDCounter1 . |

| 3a | C.9. 17. 6.5 | DUT and TH1/TH2 activate the subscription and subscribe to ICDCounter , with MinIntervalFloor and MaxIntervalCeiling . | Verify that the DUT response contains MaxInterval1 and MaxInterval2 respectively, where MinIntervalFloor ≤ MaxInterval ≤ MAX(SUBSCRIPTION_MAX_INTERVAL _PUBLISHER_LIMIT, MaxIntervalCeiling) . |

## Notes/Testing Considerations

## 18.5.3. ICD Dynamic SIT/LIT test cases

## TC-ICDB-3.1 ICD Dynamic SIT/LIT - Verify OperatingMode transition between LIT and SIT when there is client registration with DUT as Server

## Purpose

This test case verifies the LIT ICD has the capacity to switch between LIT and SIT operating modes with vendor specific trigger when there is client registration present.

## PICS

- ICDB.S
- ICDM.S.F02(LITS)
- ICDM.S.F03(DSLS)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

| # | Pre-Condition |
| 1 | Commission DUT to TH (can be skipped if done in a preceding test). |

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | Test Step | Expected Outcome |

## Post-Conditions

| # | Post-Condition |
| 1 | TH sends command UnregisterClient to clear all clients in RegisteredClients , if any. |

## Notes/Testing Considerations

- CheckInNodeID: any random node ID
- MonitoredSubID: any random subject ID
- Key: a 16-byte octstr, eg, hex:1234567890abcdef1234567890abcdef

## TC-ICDB-3.2 ICD Dynamic SIT/LIT - Verify OperatingMode does not transition between LIT and SIT when there is no client registration with DUT as Server

## Purpose

This test case verifies the LIT ICD does not switch between LIT and SIT operating modes with vendor specific trigger when there is no client registration present.

## PICS

- ICDB.S
- ICDM.S.F02(LITS)
- ICDM.S.F03(DSLS)

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Pre-Conditions

| # | Pre-Condition |
| 1 | Commission DUT to TH (can be skipped if done in a preceding test). |

| # | Ref | PICS | Test Step | Expected Outcome |
| 2a | | | Apply vendor specific mechanism to transition DUT to from SIT operating mode to LIT operating mode. | |

## Notes/Testing Considerations

## Chapter 19. Fabric Synchronization Test Plan

## 19.1. PICS Definition

This section covers the Fabric Synchronization Test Plan related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

## 19.1.1. DUT server

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| MCORE.FS | Does the DUT implement Fabric Synchronization | Optional | |

## 19.2. Test Case List

| TC UUID | Test Case Name |
| TC-MCORE.FS-1.1 | FS Setup [DUT - Initial Commissionee] |
| TC-MCORE.FS-1.2 | FS Synchronization - No common devices [DUT - Commissioning End Device] |
| TC-MCORE.FS-1.3 | FS Synchronization - DUT Fabric Synchronization Administrator commissions device without UniqueID |
| TC-MCORE.FS-1.4 | FS Synchronization - DUT Fabric Synchronization Administrator syncs device from other FSA without UniqueID |
| TC-MCORE.FS-1.5 | FS Synchronization - DUT reflects bridged device's CADMIN attributes |

## 19.3. Test Cases

## 19.3.1. Fabric Synchronization test cases

## TC-MCORE.FS-1.1 FS Setup [DUT - Initial Commissionee]

## Purpose

This test validates the initial setup of Fabric Synchronization between two Fabric Synchronizing Administrators.

Verification of Cluster command responses and error conditions is handled in the Commissioner Control Cluster test plan.

## · MCORE.FS

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT_FSA | DUT - Fabric Synchronizing Administrator. (Administrator and Aggregator nodes.) |
| 2 | TH | Test Harness as Administrator, Controller |
| 3 | TH_SERVER | Test Harness Server application (lighting-app or all-cluster-app works) |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT_FSA is reset to factory defaults | |
| 2 | | DUT_FSA has been commissioned to TH | |

## Device Topology

Final Topology:

- DUT\_FSA has commissioned a Node presenting the Fabric Synchronization feature provided by TH\_FSA.
- TH\_FSA has commissioned a Node presenting the Fabric Synchronization feature provided by DUT\_FSA.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-MCORE.FS-1.2 FS Synchronization - No common devices [DUT - Commissioning End Device]

## Purpose

This test validates the common case of DUT\_FSA capable of enumerating newly added Matter device and shortly after having the newly added device be commissioned onto another fabric.

## PICS

- MCORE.FS

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT_FSA | DUT - Fabric Synchronizing Administrator. (Administrator and Aggregator nodes.) |
| 2 | TH | Test Harness as Administrator, Controller |
| 3 | TH_SERVER | Test Harness Server application (lighting-app or all-cluster-app works) |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT_FSA is reset to factory defaults | |
| 2 | | DUT_FSA has been commissioned to TH | |

Final Topology:

- DUT\_FSA has commissioned TH\_SERVER onto it's fabric.
- TH has commissioned TH\_SERVER onto TH's fabric.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH subscribes to PartsList attribute of the Descriptor cluster of DUT_FSA endpoint 0 (root endpoint) | TH saves the current PartsList result to be used in a later step |
| 2 | | | Follow manufacturer provided instructions to have DUT_FSA commission TH_SERVER | |
| 3 | | | TH waits up to 30 seconds for subscription report from the PartsList attribute of the Descriptor cluster made in step 1 | Verify that PartsList contains exactly one more endpoint which previously was not present in step 1 |

| | | | • VendorID |
| | | | • ProductName |
| | | | • ProductID |
| | | | • NodeLabel |
| | | | • HardwareVersion |
| | | | • SoftwareVersion |
| | | | • SoftwareVersionString |
| | | | • UniqueID |

## Notes/Testing Considerations

## TC-MCORE.FS-1.3 FS Synchronization - DUT Fabric Synchronization Administrator commissions device without UniqueID

## Purpose

This test validates that a Fabric Synchronizing Administrator generates a UniqueID for an End Device that do not provide a UniqueID.

## PICS

## · MCORE.FS

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT_FSA | DUT - Fabric Synchronizing Administrator. (Administrator and Aggregator nodes.) |
| 2 | TH | Test Harness as Administrator, Controller |
| 3 | TH_SERVER_NO_UID | Test Harness Server application which does not provide the UniqueID that will be commissioned onto DUT_FSA fabric during test. |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT_FSA is reset to factory defaults | |
| 2 | | DUT_FSA's aggregator is commissioned to TH fabric | |
| 3 | | TH_SERVER_NO_UID is not commissioned onto any fabric. | |

## Device Topology

Starting Topology:

- TH has commissioned DUT\_FSA's aggregator.

Final Topology:

- TH has commissioned a Node presenting the Fabric Synchronization feature provided by DUT\_FSA.
- DUT\_FSA's fabric contains TH\_SERVER\_NO\_UID.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-MCORE.FS-1.4 FS Synchronization - DUT Fabric Synchronization Administrator syncs device from other FSA without UniqueID

## Purpose

This test validates that a Fabric Synchronizing Administrator copies the UniqueID for Synchronized End Devices

from other Fabric Synchronizing Administrator if the Synchronized End Device does not provide the UniqueID.

## · MCORE.FS

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT_FSA | DUT - Fabric Synchronizing Administrator. (Administrator and Aggregator nodes.) |
| 2 | TH | Test Harness as Administrator, Controller |
| 3 | TH_FSA | Fabric Synchronizing Administrator running on TH. (Administrator and Aggregator nodes.) |
| 4 | TH_SERVER_NO_UID | Test Harness Server application which does not provide the UniqueID that will be synchronized from TH_FSA to DUT_FSA fabric during test. |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT_FSA is reset to factory defaults | |
| 3 | | DUT_FSA's aggregator is commissioned to TH fabric | |
| 4 | | DUT_FSA is configured to synchronize devices and expose devices to TH_FSA | |
| 6 | | Perform Setup as described in the steps of TC-MCORE.FS-1.1 | |

## Device Topology

Starting Topology:

- TH has commissioned DUT\_FSA's aggregator.
- TH has commissioned TH\_FSA's aggregator.

Final Topology:

- DUT\_FSA has commissioned a Node presenting the Fabric Synchronization feature provided by TH\_FSA.
- TH\_FSA has commissioned a Node presenting the Fabric Synchronization feature provided by DUT\_FSA.
- TH\_FSA's fabric contains TH\_SERVER\_NO\_UID.
- DUT\_FSA's fabric contains TH\_SERVER\_NO\_UID.
- TH's fabric contains TH\_SERVER\_NO\_UID.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 5 | | | Follow manufacturer provided instructions to enable DUT_FSA to synchronize TH_SERVER_NO_UID from TH_FSA onto DUT_FSA's fabric. TH to provide endpoint saved from step 2 in user prompt. | |

## Notes/Testing Considerations

## TC-MCORE.FS-1.5 FS Synchronization - DUT reflects bridged device's CADMIN attributes

## Purpose

This test validates that Fabric Synchronizing device properly reflects AdministratorCommissioning attributes of a bridged device.

## PICS

## · MCORE.FS

## Required Devices

| # | Device Name | Device Description |
| 1 | DUT_FSA | DUT - Fabric Synchronizing Administrator. (Administrator and Aggregator nodes.) |
| 2 | TH | Test Harness as Administrator, Controller |
| 3 | TH_SERVER | Test Harness Server application (lighting-app or all-cluster-app works) |

## Preconditions

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT_FSA is reset to factory defaults | |
| 2 | | DUT_FSA has been commissioned to TH | |

## Device Topology

## Final Topology:

- DUT\_FSA has commissioned TH\_SERVER onto it's fabric.
- TH has commissioned TH\_SERVER onto TH's fabric.

| # | Test Step | Expected Outcome |
| 1 | TH subscribes to PartsList attribute of the Descriptor cluster of DUT_FSA endpoint 0 (root endpoint) | TH saves the current PartsList result to be used in a later step |
| 2 | Follow manufacturer provided instructions to have DUT_FSA commission TH_SERVER | |
| 3 | TH waits up to 30 seconds for subscription report from the PartsList attribute of the Descriptor cluster made in step 1 | Verify that PartsList contains exactly one more endpoint which previously was not present in step 1 |
| 6 | TH subscribes to AdministratorCommissioning attributes on DUT_FSA for the newly added endpoint identified in step 3 | Validate subscription established successfully |
| 7 | TH directly opens the commissioning window of TH_SERVER using the Enhanced Commissioning Method (not using DUT_FSA) | |
| 8 | TH reads CurrentFabricIndex attributes on OperationalCredentials cluster from TH_SERVER directly (not using DUT_FSA) | Saves the results for validation in future step |
| 9 | TH reads AdministratorCommissioning attributes from TH_SERVER directly (not using DUT_FSA) | Saves the results for validation in future step, and validates the follow attributes • WindowStatus == |
| | | EnhancedWindowOpen |
| | | • AdminFabricIndex == CurrentFabricIndex (read in step 8) |

| 10 | TH waits up to 10 seconds for subscription report from the AdministratorCommissioning attribute (from step 6). For simplicity after receiving subscription, TH may do wildcard read on AdministratorCommissioning attribute. | Validate that the following attributes from bridged endpoint on DUT_FSA match what is reported from TH_SERVER from step 9: • WindowStatus • AdminFabricIndex • AdminVendorId |

## Notes/Testing Considerations

## Chapter 20. WebRTC Transport Test Plan

## 20.1. PICS Definition

This section covers the WebRTC Transport Test Plan related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| WEBRTCP.S | Does the DUT implement the WebRTC Transport Provider cluster? | M | |
| WEBRTCR.C | Does the DUT implement the WebRTC Transport Requester cluster? | O | |

## 20.2. Test Case List

| # | TC UUID | Test Case Name |
| 2 | TC-WEBRTC-1.2 | Validate that providing an existing WebRTC session ID with an SDP Offer successfully triggers the re-offer flow |
| 3 | TC-WEBRTC-1.3 | Validate Deferred Offer Flow for Battery-Powered Camera in Standby Mode |
| 4 | TC-WEBRTC-1.4 | Validate Non-Deferred Offer Flow for Battery-Powered Camera in Standby Mode |
| 5 | TC-WEBRTC-1.5 | Validate that the camera (DUT) can start a WebRTC session by issuing an ProvideOffer command - PROVISIONAL |
| 6 | TC-WEBRTC-1.6 | Validate Two-Way-Talk Full- Duplex support in camera(DUT)-Release 1.5.0 only |

| 7 | TC-WEBRTC-1.7 | Validate that setting an SDP Offer sequentially from multiple camera controllers successfully initiates multiple WebRTC sessions |
| 8 | TC-WEBRTC-1.8 | Validate that setting an SDP Offer simultaneously from multiple camera controllers successfully initiates multiple WebRTC sessions |
| 9 | TC_WEBRTC-1.9 | Validate Two-Way-Talk Full- Duplex support in camera(DUT)-Release 1.5.1 and later - PROVISIONAL |

## 20.3. Test Cases

## 20.3.1. WebRTC Transport test cases

## TC-WEBRTC-1.1 Validate that setting an SDP Offer successfully initiates a new WebRTC session

## Purpose

This test case verifies that the controller is able to initiate a new WebRTC session by issuing an SDP Offer without a session ID to the DUT.

## PICS

- WEBRTCR.C
- WEBRTCP.S

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH | |
| 2 | | Confirm no active WebRTC sessions exist in DUT | |

## Required Devices

| # | Device Name | Description |
| 2 | DUT | WebRTCProvider-enabled camera device as WEBRTCP. |

## Device Topology

- TH and DUT are on the same fabric.

## Test Setup

The manufacturer has supplied a Raspberry Pi 4 or later with a Raspberry Pi Camera Module 3 as the DUT, set in standby mode.

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH sends the ProvideOffer command with an SDP Offer and null WebRTCSessionID to the DUT. | DUT responds with ProvideOfferResponse containing allocated WebRTCSessionID. TH saves the WebRTCSessionID to be used in a later step |

## Notes/Testing Considerations

## TC-WEBRTC-1.2 Validate that providing an existing WebRTC session ID with an SDP Offer successfully triggers the re-offer flow

## Purpose

This test case verifies that the controller is able to use an existing WebRTC session ID with an SDP Offer successfully triggers the re-offer flow by updating the session's SDP details.

## PICS

- WEBRTCR.C
- WEBRTCP.S

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH | |
| 2 | | Confirm there is an active WebRTC sessions exist in DUT | |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness Controller as WEBRTCR. |
| 2 | DUT | WebRTCProvider-enabled device as WEBRTCP. |

## Device Topology

- TH and DUT are on the same fabric.

## Test Setup

The manufacturer has supplied a Raspberry Pi 4 or later with a Raspberry Pi Camera Module 3 as the DUT, set in standby mode.

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH Reads CurrentSessions attribute from WEBRTCP (DUT) | Verify the number of WebRTCSession in the list is 1 and the WebRTCSessionID of the WebRTCSession also exists in the CurrentSessions attribute of local WEBRTCR. TH saves the WebRTCSessionID to be used in a later step. |

## Notes/Testing Considerations

## TC-WEBRTC-1.3 Validate Deferred Offer Flow for Battery-Powered Camera in Standby Mode

## Purpose

This test case verify that the controller can start a WebRTC session by sending a SolicitOffer command to the DUT. The camera wakes up, responds with a new WebRTCSessionID, and sets the DeferredOffer flag to TRUE, indicating that it might take up to 30 seconds to send the final Offer while initializing its components.

## PICS

- WEBRTCR.C
- WEBRTCP.S

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH | |
| 2 | | Confirm no active WebRTC sessions exist in DUT | |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness Controller as WEBRTCR. |
| 2 | DUT | WebRTCProvider-enabled device as WEBRTCP. |

## Device Topology

- TH and DUT are on the same fabric.

## Test Setup

The manufacturer has supplied a Raspberry Pi 4 or later with a Raspberry Pi Camera Module 3 as the DUT, set in standby mode.

## Test Procedure

| # | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-WEBRTC-1.4 Validate Non-Deferred Offer Flow for Battery-Powered Camera in Standby Mode

## Purpose

Verify that the controller can initiate a WebRTC session by sending a SolicitOffer command to the DUT. The camera wakes up, returns a new WebRTCSessionID, and immediately sends the Offer (with the DeferredOffer flag set to FALSE), indicating no delay in session initialization.

## PICS

- WEBRTCR.C
- WEBRTCP.S

## Precondition

| # | Doc. Ref. | Condition | Notes |

| 1 | DUT (Camera) has been commissioned to TH |
| 2 | Confirm no active WebRTC sessions exist in DUT |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness Controller as WEBRTCR. |
| 2 | DUT | WebRTCProvider-enabled device as WEBRTCP. |

## Device Topology

- TH and DUT are on the same fabric.

## Test Setup

The manufacturer has supplied a Raspberry Pi 4 or later with a Raspberry Pi Camera Module 3 as the DUT, set in standby mode.

## Test Procedure

| # | Test Step | Expected Outcome |

## TC-WEBRTC-1.5 Validate that the camera (DUT) can start a WebRTC session by issuing an ProvideOffer command - PROVISIONAL

## Purpose

This test case verifies that the camera (DUT) can start a WebRTC session by sending a ProvideOffer command and receiving a Answer response from the Controller. This flow is used when the camera initiates the session, such as in outbound calls or intercom systems.

## PICS

- WEBRTCR.S
- WEBRTCP.C

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH | |
| 2 | | Confirm no active WebRTC sessions exist in DUT | |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness Controller as WEBRTCP. |
| 2 | DUT | WebRTCRequestor-enabled device as WEBRTCR. |

## Device Topology

- TH and DUT are on the same fabric.

## Test Setup

The manufacturer has supplied a Raspberry Pi 4 or later with a Raspberry Pi Camera Module 3 as the DUT, set in standby mode.

## Test Procedure

| # | Test Step | Expected Outcome |

| 1 | Follow manufacturer provided instructions to have DUT send the ProvideOffer command to the TH. | Verify the command has a non-empty offer SDP. TH sends ProvideOfferResponse containing allocated WebRTCSessionID. TH saves the WebRTCSessionID to be used in a later step. |

## Notes/Testing Considerations

Vendor needs to mention steps on how to trigger the ProvideOffer Command from DUT.

## TC-WEBRTC-1.6 Validate Two-Way-Talk Full-Duplex support in camera(DUT)- Release 1.5.0 only

## Purpose

This test case verifies that the camera (DUT) supports Full-Duplex Two-Way-Talk feature, where audio can be exchanged in both directions simultaneously. This feature is used in device types such as Video Doorbell, where camera will be able to playback the audio sent by the controller.

## PICS

- WEBRTCP.S
- WEBRTCR.C
- AVSM.S

## Precondition

| 0 | | DUT WebRTC Transport Provider cluster is at revision 1 | 1 |
| | DUT (Camera) has been commissioned to TH | | 2 |

| Confirm no active WebRTC sessions exist in DUT | 3 |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness Controller with microphone as WEBRTCR. |

## Device Topology

- TH and DUT are on the same fabric.

## Test Setup

The manufacturer has supplied a camera device as the DUT.

## Test Procedure

| # | Test Step | Expected Outcome |

## Notes/Testing Considerations

## TC-WEBRTC-1.7 Validate that setting an SDP Offer sequentially from multiple camera controllers successfully initiates multiple WebRTC sessions

## Purpose

This test case verifies that the DUT is able to create webrtc session for the SDP offer without a session id issued by multiple controllers. In this test, SDP offer issued from second controller is issued after the first controller has already created a webrtc session and ends session.

## PICS

- WEBRTCR.C
- WEBRTCP.S

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH1 | |
| 2 | | Confirm no active WebRTC sessions exist in DUT | |

## Required Devices

| # | Device Name | Description |
| 1 | TH1 | First Test Harness Controller as WEBRTCR. |
| 2 | DUT | WebRTCProvider-enabled camera device as WEBRTCP. |
| 3 | TH2 | Second Test Harness Controller as WEBRTCR. |

## Device Topology

- TH1 and DUT are on the same fabric. TH2 is on the different fabric from the DUT fabric.

## Test Setup

The manufacturer has supplied a Camera device as DUT, set in standby mode.

## Test Procedure

| # | Test Step | Expected Outcome |
| 4 | Either or both TH1 and DUT exchange ICE candidates if ICE candidates are not shared in the SDP Offer / Answer | |

## TC-WEBRTC-1.8 Validate that setting an SDP Offer simultaneously from multiple camera controllers successfully initiates multiple WebRTC sessions

## Purpose

This test case verifies that the DUT is able to create webrtc session for the SDP offer without a session id issued by multiple controllers. In this test, Second controller issues SDP offer before the first controller ends the session.

## PICS

- WEBRTCR.C
- WEBRTCP.S

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH1 | |
| 2 | | Confirm no active WebRTC sessions exist in DUT | |

## Required Devices

| # | Device Name | Description |
| 2 | DUT | WebRTCProvider-enabled camera device as WEBRTCP. |

## Device Topology

- TH1 and DUT are on the same fabric. TH2 is on the different fabric from the DUT fabric.

## Test Setup

The manufacturer has supplied a Camera device as DUT, set in standby mode.

## Test Procedure

| # | Test Step | Expected Outcome |

| 8 | Either or both TH1 and DUT exchange ICE candidates if ICE candidates are not shared in the SDP Offer / Answer | |
| 9 | Either or both TH2 and DUT exchange ICE candidates if ICE candidates are not shared in the SDP Offer / Answer | |

## Notes/Testing Considerations

## TC-WEBRTC-1.9 Validate Two-Way-Talk Full-Duplex support in camera(DUT)-Release 1.5.1 and later - PROVISIONAL

## Purpose

This test case verifies that the camera (DUT) supports Full-Duplex Two-Way-Talk feature, where audio can be exchanged in both directions simultaneously. This feature is used in device types such as Video Doorbell, where camera will be able to playback the audio sent by the controller.

## PICS

- WEBRTCP.S
- WEBRTCR.C
- AVSM.S

## Precondition

| 0 | | DUT WebRTC Transport Provider cluster is at revision 2 or higher | 1 |
| | DUT (Camera) has been commissioned to TH | | 2 |
| | Confirm no active WebRTC sessions exist in DUT | | 3 |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness Controller with microphone as WEBRTCR. |

## Device Topology

- TH and DUT are on the same fabric.

## Test Setup

The manufacturer has supplied a camera device as the DUT.

## Test Procedure

| # | Test Step | Expected Outcome |
| 1 | TH reads TwoWayTalkSupport Attribute from AVSM cluster from DUT | Verify DUT responds w/ status SUCCESS(0x00) and contains FullDuplex TwoWayTalkSupportTypeEnum value. |

## Notes/Testing Considerations

## Chapter 21. Push AV Stream Transport Test Plan

## 21.1. PICS Definition

This section covers the Push AV Stream Transport Integration Test Plan related PICS items that are referenced in the following test cases. Support for an item is considered as "true" for conditional statements within the test case steps.

| Variable | Description | Mandatory/Optional | Notes/Additional Constraints |
| PAVST.S | Does the device implement the Push AV Stream Transport cluster? | M | |

## 21.2. Test Case List

| TC UUID | Test Case Name |
| TC-PAVSTI-1.1 | Verify transmission when trigger type is Manual - PROVISIONAL |
| TC-PAVSTI-1.2 | Verify transmission with trigger type as Continuous and ensure privacy settings are checked if supported - PROVISIONAL |

## 21.3. Test Cases

## 21.3.1. Push AV Stream Transport Integration test cases

## TC-PAVSTI-1.1 Verify transmission when trigger type is Manual - PROVISIONAL

## Purpose

This test case verifies that the manually triggered video stream transmission is in CMAF format when CMAF is the container type.

Additionally, if supported, the privacy settings must be validated before initiating transmission.

## PICS

- PAVST.S

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH | |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness as Controller |
| 2 | DUT | PushAVStreamTransport- enabled device (e.g., Camera) |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH (can be skipped if done in a preceding test).

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH Reads CurrentConnections attribute from PushAV Stream Transport Cluster on DUT | Verify the number of PushAV Connections in the list is 0. If not 0, issue DeAllocatePushAVTransport with `ConnectionID to remove any connections. |

| 5 | | | TH sends the AllocatePushTransport command with valid parameters and TriggerType = Command and StreamUsage = Recording | DUT responds with AllocatePushTransportResponse containing the allocated ConnectionID , TransportOptions , and TransportStatus in the TransportConfigurationStruct . Store ConnectionID as aConnectionID . |
| 6 | | | TH establishes a subscription to all of the Events from the Cluster | |

| 19 | | | TH verifies that a PushTransportBegin Event was received | TH validates that connectionID = aConnectionID , triggerType = Command , and activationReason = UserInitiated |
| 20 | 11.7.1.2, Interfac e-2: DASH and HLS Ingest Naming | | TH shows the video prompt. The prompt must also list the uploaded content and list any non conforming extended paths. | The video playback must play while the DUT is uploading CMAF. All extended paths must conform to the Matter-defined format - session_<SessionNumber>/<Track Name>/segment_<SegmentNumbe r>.<SegmentExtension>. <SegmentExtension> must be any of the following: • segments - m4s • init segments - init • manifest - mpd / m3u8 |

| 22 | 11.7.1.2, Interfac e-2: DASH and HLS Ingest Naming | TH shows the video prompt. The prompt must also list the uploaded content and list any non conforming extended paths. | CMAF content must play successfully from uploaded files. DUT shall not upload any new files. All extended paths must conform to the Matter-defined format - session_<SessionNumber>/<Track Name>/segment_<SegmentNumbe r>.<SegmentExtension>. <SegmentExtension> must be any of the following: • segments - m4s • init segments - init • manifest - mpd / m3u8 |

## Notes/Testing Considerations

Manufacturer needs to provide instructions on how to turn On/Off HardPrivacyModeOn from DUT.

## TC-PAVSTI-1.2 Verify transmission with trigger type as Continuous and ensure privacy settings are checked if supported - PROVISIONAL

## Purpose

This test verifies that setting the TransportStatus to "Active" must initiate transmission, and setting it to "Inactive" must terminate transmission, when the trigger type is set to "Continuous". Additionally, if supported, the privacy settings must be validated before initiating transmission.

## PICS

- PAVST.S

## Precondition

| # | Doc. Ref. | Condition | Notes |
| 1 | | DUT (Camera) has been commissioned to TH | |

## Required Devices

| # | Device Name | Description |
| 1 | TH | Test Harness as Controller |

| 2 | DUT | PushAVStreamTransport- enabled device (e.g., Camera) |

## Device Topology

TH and DUT are on the same fabric.

## Test Setup

Commission DUT to TH (can be skipped if done in a preceding test).

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 5 | | | TH sends the AllocatePushTransport command with valid parameters and TriggerType = Continuous | DUT responds with AllocatePushTransportResponse containing the allocated ConnectionID , TransportOptions , and TransportStatus in the TransportConfigurationStruct . Store ConnectionID as aConnectionID . |

| 12 | 11.7.1.2, Interfac e-2: DASH and HLS Ingest Naming | | TH shows the video prompt. The prompt must also list the uploaded content and list any non conforming extended paths. | The video playback must play while the DUT is uploading CMAF. All extended paths must conform to the Matter-defined format - session_<SessionNumber>/<Track Name>/segment_<SegmentNumbe r>.<SegmentExtension>. <SegmentExtension> must be any of the following: • segments - m4s • init segments - init • manifest - mpd / m3u8 |

| 14 | 11.7.1.2, Interfac e-2: DASH and HLS Ingest Naming | TH shows the video prompt. The prompt must also list the uploaded content and list any non conforming extended paths. | CMAF content must play successfully from uploaded files. DUT shall not upload any new files. All extended paths must conform to the Matter-defined format - session_<SessionNumber>/<Track Name>/segment_<SegmentNumbe r>.<SegmentExtension>. <SegmentExtension> must be any of the following: • segments - m4s • init segments - init • manifest - mpd / m3u8 |

## Chapter 22. Minimal Resource Requirements Test Plan

## 22.1. Test Case List

| # | TC UUID | Test Case Name |
| 1 | TC-RR-1.1 | Minimal Resource Requirements for Matter Node |

## 22.2. Test Cases

## 22.2.1. Minimal Resource Requirements Test Cases

## TC-RR-1.1 Minimal Resource Requirements for Matter Node

## Purpose

This test case verifies that the device meets the minimal requirements for each resource type from the list of various resources required by a Matter Node implementation.

## PICS

## · MCORE.ROLE.COMMISSIONEE

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | Test harness as Client |
| 2 | DUT | DUT as Server |

## Device Topology

TH and DUT are on the same fabric.

Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1e | 11.1 7.6, 6.1.3 | | Repeat the process to commission DUT to 5 different fabrics. If, for a given fabric, it is not possible for all certificates in the chain to be of length 400 bytes, then at least 1 of the set must be larger or equal to 370 bytes and at least one of the set must be larger or equal to 350 bytes, and at least one must be exactly 400 bytes. All certificate chains have to be valid. VIDVerificationStatement field must be set for each. | Verify that the device can be commissione d to the minimum value of SupportedFab rics Attribute on the Node Operational Credentials Cluster which is 5. Record the number of fabrics commissione d as commissioned_ fabrics . |

| # | Ref | PICS | Test Step | Expected Outcome |

| Test Step | | Expected | Expected | Expected |
| Add 4 Access Control entries on DUT with a list of 4 Subjects and 3 Targets with the following parameters: 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) | Add 4 Access Control entries on DUT with a list of 4 Subjects and 3 Targets with the following parameters: 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) | Add 4 Access Control entries on DUT with a list of 4 Subjects and 3 Targets with the following parameters: 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) | Add 4 Access Control entries on DUT with a list of 4 Subjects and 3 Targets with the following parameters: 1. struct ◦ Privilege field: Administer (5) ◦ AuthMode field: CASE (2) | Outcome Verify that the Subjects have access control privilege on the Targets according to the ACL entries for each fabric and the device supports minimum constraints for each of EntriesPerFab ric Attribute, SubjectsPerAc cessControlEn try Attribute and TargetsPerAc cessControlEn try Attribute |
| ◦ Privilege field: Operate (3) ◦ AuthMode field: CASE (2) ◦ Subjects field: [0x3000_0000_0000_0001, 0x3000_0000_0000_0002, 0x3000_0000_0000_0003, | ◦ Privilege field: Operate (3) ◦ AuthMode field: CASE (2) ◦ Subjects field: [0x3000_0000_0000_0001, 0x3000_0000_0000_0002, 0x3000_0000_0000_0003, | ◦ Privilege field: Operate (3) ◦ AuthMode field: CASE (2) ◦ Subjects field: [0x3000_0000_0000_0001, 0x3000_0000_0000_0002, 0x3000_0000_0000_0003, | ◦ Privilege field: Operate (3) ◦ AuthMode field: CASE (2) ◦ Subjects field: [0x3000_0000_0000_0001, 0x3000_0000_0000_0002, 0x3000_0000_0000_0003, | |
| ◦ Subjects field: [0xFFFF_FFFD_0001_0001, 0x2000_0000_0000_0001, 0x2000_0000_0000_0002, | ◦ Subjects field: [0xFFFF_FFFD_0001_0001, 0x2000_0000_0000_0001, 0x2000_0000_0000_0002, | ◦ Subjects field: [0xFFFF_FFFD_0001_0001, 0x2000_0000_0000_0001, 0x2000_0000_0000_0002, | ◦ Subjects field: [0xFFFF_FFFD_0001_0001, 0x2000_0000_0000_0001, 0x2000_0000_0000_0002, | |
| 0x2000_0000_0000_0003] | 0x2000_0000_0000_0003] | 0x2000_0000_0000_0003] | 0x2000_0000_0000_0003] | |
| struct | struct | struct | struct | |
| ◦ Privilege field: Manage (4) | ◦ Privilege field: Manage (4) | ◦ Privilege field: Manage (4) | ◦ Privilege field: Manage (4) | |
| ◦ AuthMode field: CASE (2) | ◦ AuthMode field: CASE (2) | ◦ AuthMode field: CASE (2) | ◦ AuthMode field: CASE (2) | |
| | | AccessControl | AccessControl | AccessControl |
| ◦ Subjects 0x1000_0000_0000_0002, | field: | [0x1000_0000_0000_0001, 0x1000_0000_0000_0003, | | |
| 0x1000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC00, DeviceType: | 0x1000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC00, DeviceType: | 0x1000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC00, DeviceType: | 0x1000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC00, DeviceType: | |
| 0xFFF1_BC21}, {Cluster: 0xFFF1_FC02, DeviceType: 0xFFF1_BC22}] 3. struct | 0xFFF1_BC21}, {Cluster: 0xFFF1_FC02, DeviceType: 0xFFF1_BC22}] 3. struct | on the Access | on the Access | on the Access |
| | | Control | Control | Control |
| 0x3000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC40, DeviceType: 0xFFF1_BC20}, {Cluster: 0xFFF1_FC41, DeviceType: | 0x3000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC40, DeviceType: 0xFFF1_BC20}, {Cluster: 0xFFF1_FC41, DeviceType: | 0x3000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC40, DeviceType: 0xFFF1_BC20}, {Cluster: 0xFFF1_FC41, DeviceType: | 0x3000_0000_0000_0004] ◦ Targets field: [{Cluster: 0xFFF1_FC40, DeviceType: 0xFFF1_BC20}, {Cluster: 0xFFF1_FC41, DeviceType: | |
| 0xFFF1_BC21}, {Cluster: 0xFFF1_FC02, DeviceType: | 0xFFF1_BC21}, {Cluster: 0xFFF1_FC02, DeviceType: | 0xFFF1_BC21}, {Cluster: 0xFFF1_FC02, DeviceType: | 0xFFF1_BC21}, {Cluster: 0xFFF1_FC02, DeviceType: | |
| 0xFFF1_BC42}] | 0xFFF1_BC42}] | 0xFFF1_BC42}] | 0xFFF1_BC42}] | |
| struct | struct | struct | struct | |
| ◦ Privilege field: View (1) | ◦ Privilege field: View (1) | ◦ Privilege field: View (1) | ◦ Privilege field: View (1) | |
| ◦ AuthMode field: CASE (2) | ◦ AuthMode field: CASE (2) | ◦ AuthMode field: CASE (2) | ◦ AuthMode field: CASE (2) | |
| ◦ | | [0x4000_0000_0000_0001, | | |
| | | 0x4000_0000_0000_0003, | | |
| 0x4000_0000_0000_0004] Targets field: [{Cluster: 0xFFF1_BC20}, {Cluster: | field: | 0xFFF1_FC80, DeviceType: 0xFFF1_FC81, DeviceType: | | |
| Subjects 0x4000_0000_0000_0002, | | | | |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected | |

| # | Ref | PICS | Test Step | Expected Outcome |
| 11 | 2.11. 1.2, 11.2, 9.5.4 | | If Groupcast cluster is enabled on the RootNode endpoint, skip to step 16. Otherwise, TH counts all Groups cluster entries (cluster ID 0x0004) in every Descriptor's ServerList instance within every endpoint found in all 'PartsList' instances. TH records Groups cluster instances counted as counted_groups_clusters . | Verify the value of MaxGroupsPerF abric read from the Group Key Management Cluster is no less than the Group Limits requirements of 4 (groups) * counted_group s_clusters . |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

| # | Ref | PICS | Test Step | Expected Outcome |

## Notes/Testing Considerations

## Chapter 23. System Model Test Plan

## 23.1. Test Case List

| TC UUID | Test Case Name |
| TC-SM-1.1 | Device composition - Root Node [DUT as Server] |
| TC-SM-1.2 | Device composition - Topology [DUT as Server] |

## 23.2. Test Cases

## 23.2.1. Device composition tests

[TC-SM-1.1] Device composition - Root Node [DUT as Server]

Purpose

Tests root node requirements

## PICS

- MCORE.ROLE.COMMISSIONEE

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH performs a wildcard read of all attributes and endpoints | |
| 2 | C.2.10 | | | Verify that endpoint 0 exists in the returned data |

| 3 | C.2.10 | | Verify that the endpoint 0 descriptor cluster DeviceTypeList includes the Root Node device type id (0x0016) |
| 4 | {REF_S M_END POINT} | | For each of the non-root endpoints, verify that the descriptor cluster DeviceTypeList does NOT include the Root Node device type id (0x0016) |
| 6 | | | Verify that the SpecificationVersion attribute from Basic Information Cluster is Matter 1.6 or above. Otherwise, skip steps 7 and 8. |

## TC-SM-1.2 Device composition - Topology [DUT as Server]

## Purpose

Tests that the topology indicated by the descriptor cluster PartsList matches the requirements in {REF\_SM\_ENDPOINT}.

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH performs a wildcard read of all attributes on all endpoints | |
| 2 | | | | Verify the Descriptor cluster PartsList on endpoint 0 exactly lists all the other (non-0) endpoints on the DUT - i.e. the endpoints returned in step 1 (except EP 0) must be listed in the PartsList, and all endpoints listed in the PartsList must be amongst the endpoint(s) returned in step 1 |
| 3 | | | | For each endpoint on the DUT (including EP 0), verify the PartsList in the Descriptor cluster on that endpoint does not include itself |
| 4 | | | | Create two empty list variables flat and tree |

| 6 | For each endpoint e in the flat list: * for each endpoint id sub_id present in the in the PartsList of e , ensure that every id listed in the PartsList for endpoint sub_id appears in the PartsList of e |

## Chapter 24. Device Types Test Plan

## 24.1. Test Case List

| TC UUID | Test Case Name |
| TC-DT-1.1 | Base Device type [DUT as Server] |

## 24.2. Test Cases

## 24.2.1. Device composition tests

## TC-DT-1.1 Base Device Type [DUT as Server]

## Purpose

Tests that every device type conforms to the requirements of the base device type

## PICS

## · MCORE.IDM.S

## Required Devices

| # | Device Name | Device Description |
| 1 | TH | TH as Client. |
| 2 | DUT | DUT as Server. |

## Device Topology

TH can connect to DUT over PASE or CASE.

## Test Procedure

| # | Ref | PICS | Test Step | Expected Outcome |
| 1 | | | TH performs a wildcard read of all attributes and endpoints | |
| 2 | | | | Verify that each endpoint includes a Descriptor cluster |

## Chapter 25. Platform Certification Test List

## Document History

| Rev | Date | Author | Description |

## 25.1. Platform Certification Test Case Tagging

The following array lists all test cases belonging to a test plan featured in a platform certification. The tagging array is used to identify which tests are part of the platform certification and which tests are part of the product certification. This array shall be updated whenever a new test case is added to the test plans featured in the file platform certification test plans list.

## 25.2. Test Cases

| Test Plan Cluster Name | TestID | Description | Tagging |
| Device Discovery | TC-DD-1.1 | QR Code Onboarding Payload Verification [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-1.2 | Manual Pairing Code Payload Verification [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-1.3 | NFC Onboarding Payload Verification [DUT - Commissionee] | Platform |
| Device Discovery | TC-DD-1.4 | Concatenation - QR Code Onboarding Payload Verification [DUT - Commissionee] - PROVISIONAL | Provisio nal |
| Device Discovery | TC-DD-1.5 | NFC Rules of Advertisement and Onboarding [DUT - Commissionee] | Provisio nal |
| Device Discovery | TC-DD-1.6 | QR Code Format and Label [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-1.7 | Setup Code Format and Label [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-1.8 | QR Code Onboarding Payload Verification [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-1.9 | Manual Pairing Code Payload Verification [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-1.10 | NFC Onboarding Payload Verification [DUT - Commissioner] - PROVISIONAL | Provisio nal |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Device Discovery | TC-DD-1.11 | Concatenation - QR Code Onboarding Payload Verification [DUT - Commissioner] - PROVISIONAL | Provisio nal |
| Device Discovery | TC-DD-1.12 | Onboarding Payload Verification - Custom Flow = 0 [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-1.13 | Onboarding Payload Verification - Custom Flow = 1 [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-1.14 | Onboarding Payload Verification - Custom Flow = 2 [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-2.1 | Announcement by Device Verification [DUT - Commissionee] | Both |
| Device Discovery | TC-DD-2.2 | Discovery by Commissioner Verification [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.3 | User Directed Commissioning [DUT - Commissionee] | Platform |
| Device Discovery | TC-DD-3.4 | User Directed Commissioning [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.5 | Commissioning Flow - Concurrent [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.6 | Commissioning Flow - Non-concurrent [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.7 | Commissioning Flow - Concurrent - Negative Scenario [DUT - Commissioner] - PROVISIONAL | Provisio nal |
| Device Discovery | TC-DD-3.8 | Commissioning Flow - Non-concurrent - Negative Scenario [DUT - Commissioner] - PROVISIONAL | Provisio nal |
| Device Discovery | TC-DD-3.9 | Commissioning Flow - Custom Flow = 2 [DUT - Commissionee] | Product |
| Device Discovery | TC-DD-3.10 | Commissioning Flow - Custom Flow = 2 [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.11 | Commissioning Flow = 0 (Standard Flow) - QR Code [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.12 | Commissioning Flow = 1 (User-Intent Flow) - QR Code [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.13 | Commissioning Flow = 2 (Custom Flow) - QR Code [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.14 | Commissioning Flow - QR Code - Negative Scenario [DUT - Commissioner] | Product |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Device Discovery | TC-DD-3.15 | Commissioning Flow - Manual Pairing Code [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.16 | Commissioning Flow - 11-digit Manual Pairing Code - Negative Scenario [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.17 | Commissioning Flow - 21-digit Manual Pairing Code - Negative Scenario [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.18 | Commissioning Flow - Commissioning Multiple Devices [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.19 | Commissioning Flow - Commission, Unpair and Re-commission Device [DUT - Commissionee] | Platform |
| Device Discovery | TC-DD-3.20 | Commissioning Flow - Commission, Unpair and Re-commission Device [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.21 | Commissioning Flow - Commission Multiple- Endpoint Device [DUT - Commissioner] | Product |
| Device Discovery | TC-DD-3.22 | NFC-based Commissioning [DUT as Commissioner] | Product |
| Device Discovery | TC-DD-3.23 | NFC-based Commissioning - DUT with power [DUT as Commissionee] | Product |
| Device Discovery | TC-DD-3.24 | NFC-based Commissioning - DUT without power [DUT as Commissionee] | Product |
| Node Operational Credentials Cluster | TC-OPCREDS-3.1 | Attribute-NOCs,TrustedRootCertificates list validation [DUT-Server] | Platform |
| Node Operational Credentials Cluster | TC-OPCREDS-3.2 | Attribute-CurrentFabricIndex validation [DUT- Server] | Platform |
| Node Operational Credentials Cluster | TC-OPCREDS-3.3 | Attribute-NOCs,Commands[DUT-Client] | Product |
| Node Operational Credentials Cluster | TC-OPCREDS-3.4 | UpdateNOC-Error Condition [DUT-Server] | Platform |
| Node Operational Credentials Cluster | TC-OPCREDS-3.5 | NOC Check for UpdateNOC [DUT-Server] | Platform |
| Node Operational Credentials Cluster | TC-OPCREDS-3.6 | Last Fabric removal validation [DUT-Server] | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Node Operational Credentials Cluster | TC-OPCREDS-3.7 | Add Second Fabric over CASE [DUT-Server] | Platform |
| Node Operational Credentials Cluster | TC-OPCREDS-3.8 | VID Verification Attribute, Commands Error Conditions [DUT as Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-1.4 | Verification for Network Commissioning cluster dependencies [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.1 | [Wi-Fi] Verification for attributes check [DUT- Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.2 | [Thread] Verification for attributes check [DUT- Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.3 | [Ethernet] Verification for attributes check [DUT- Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.4 | [Wi-Fi] Verification for ScanNetworks command [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.5 | [Wi-Fi] FAILSAFE_REQUIRED message Validation [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.6 | [Thread] FAILSAFE_REQUIRED message Validation [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.9 | [Wi-Fi] Verification for RemoveNetwork Command [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.10 | [Thread] Verification for RemoveNetwork Command [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.11 | [Wi-Fi] Verification for ConnectNetwork Command [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.12 | [Thread] Verification for ConnectNetwork Command [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.13 | [Wi-Fi] Verification for ReorderNetwork command [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.14 | [Thread] Verification for ReorderNetwork command [DUT-Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.15 | [Wi-Fi] NetworkIDNotFound returned in LastNetworkingStatus field validation [DUT- Server] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.16 | [Thread] NetworkIDNotFound returned in LastNetworkingStatus field validation [DUT- Server] | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| NetworkCommissi oning Cluster | TC-CNET-4.20 | [Wi-Fi] Verification for commands check [DUT- Client] | Platform |
| NetworkCommissi oning Cluster | TC-CNET-4.21 | [Thread] Verification for commands check [DUT- Client] | Product |
| NetworkCommissi oning Cluster | TC-CNET-4.22 | [Thread] Verification for ScanNetworks command [DUT-Server] | Product |
| Secure Channel | TC-SC-1.1 | MRP Max Messaging Size Verification - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-1.2 | MRP Message Flows - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-1.3 | MRP Retransmissions - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-1.4 | MRP Message Counter and Duplicate Messaging Verification - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-2.1 | PASE Session Establishment - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-2.3 | PASE Error Handling [DUT_Responder/Commissionee] - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-2.4 | PASE Error Handling [DUT_Initiator/Commissioner] - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-3.1 | CASE Session Establishment - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-3.2 | CASE Session Resumption [DUT_Responder] - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-3.3 | CASE Session Resumption [DUT_Initiator] - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-3.4 | CASE Error Handling [DUT_Responder] - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-3.5 | CASE Error Handling [DUT_Initiator] - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-3.6 | CASE Resource validation | Platform |
| Secure Channel | TC-SC-4.1 | Commissionable Node Discovery [DUT as Commissionee] | Product |
| Secure Channel | TC-SC-4.2 | Discovery [DUT as Commissioner] | Product |
| Secure Channel | TC-SC-4.3 | Discovery [DUT as Commissionee] | Product |
| Secure Channel | TC-SC-4.4 | Discovery [DUT as Controller] | Product |
| Secure Channel | TC-SC-4.6 | Commissioner Discovery [DUT as Commissioner] | Product |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Secure Channel | TC-SC-4.7 | Commissioner Discovery [DUT as Commissionee] | Platform |
| Secure Channel | TC-SC-4.8 | Compressed Fabric ID remains the same for Nodes commissioned to the same fabric [DUT as Commissioner] | Product |
| Secure Channel | TC-SC-4.9 | Operational Discovery - RIO support [DUT as Commissionee] | Platform |
| Secure Channel | TC-SC-7.1 | Unique discriminators [DUT as Commissionee] | Product |
| Secure Channel | TC-SC-8.1 | Test TCP Connection Establishment with DUT. - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-8.2 | Test CASE Session allowing large payloads set up over TCP Connection with DUT. - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-8.3 | Test CASE Session becomes inactive after underlying TCP Connection with DUT is dropped. - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-8.4 | Test Back to back TCP Connection establishment, disconnection and re-establishment with DUT. - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-8.5 | Test InvokeCommandRequest and CommandResponse over a TCP-based CASE session established with DUT. - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-8.6 | Test a Large Payload interaction over a TCP- based CASE session with DUT via a wildcard Read operation. - PROVISIONAL | Provisio nal |
| Secure Channel | TC-SC-8.7 | Test that an IM operation(possible over MRP) can use an already existing TCP-based session with DUT. - PROVISIONAL | Provisio nal |
| Group Key Management Cluster | TC-GRPKEY-2.1 | Attributes {DUT-Server} | Platform |
| Group Key Management Cluster | TC-GRPKEY-2.2 | Primary functionality with DUT as Server | Platform |
| Group Key Management Cluster | TC-SC-5.1 | Adding member to a group - TH as Admin and DUT as Group Member | Platform |
| Group Key Management Cluster | TC-SC-5.2 | Receiving a group message - TH to DUT | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Group Key Management Cluster | TC-SC-5.3 | Sending a group message - TH to DUT | Product |
| Group Key Management Cluster | TC-GRPKEY-5.4 | Verification for KeySetReadResponse Command for CacheAndSync | Platform |
| Group Key Management Cluster | TC-SC-6.1 | Adding member to a group - DUT as Admin and TH as Group Member [DUT-Client] | Product |
| Device Attestation | TC-DA-1.1 | The NOC SHALL be wiped on Factory Reset [DUT-Commissionee] | Both |
| Device Attestation | TC-DA-1.2 | Device Attestation Request Validation [DUT- Commissionee] | Platform |
| Device Attestation | TC-DA-1.3 | Device Attestation Request Validation [DUT- Commissioner] | Product |
| Device Attestation | TC-DA-1.4 | Device Attestation Request Validation-Error Scenario [DUT-Commissioner] | Product |
| Device Attestation | TC-DA-1.5 | NOCSR Procedure Validation [DUT- Commissionee] | Platform |
| Device Attestation | TC-DA-1.6 | NOCSR Procedure Validation [DUT- Commissioner] | Product |
| Device Attestation | TC-DA-1.7 | Validate CertificateChainRequest [DUT- Commissionee] | Product |
| Device Attestation | TC-DA-1.8 | Device Attestation Request Validation-Success Scenario [DUT-Commissioner] | Product |
| Device Attestation | TC-DA-1.9 | Device Attestation Revocation [DUT- Commissioner] | Product |
| Interaction Data Model | TC-IDM-1.1 | Invoke Request Action from DUT to TH. [DUT as Client] | Product |
| Interaction Data Model | TC-IDM-1.2 | Invoke Response Action from DUT to TH. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-1.3 | Batched Commands Invoke Request Action from DUT to TH. [DUT as Client] | Product |
| Interaction Data Model | TC-IDM-1.4 | Batched Commands Invoke Response Action from DUT to TH. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-2.1 | Read Request Action from DUT to TH. [DUT as Client] | Product |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Interaction Data Model | TC-IDM-2.2 | Report Data Action from DUT to TH. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-2.3 | Read and Subscribe from DUT to TH with the maximum number of paths supported. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-3.1 | Write Request Message from DUT to TH. [DUT as Client] | Product |
| Interaction Data Model | TC-IDM-3.2 | Write Response Message from DUT to TH. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-4.1 | Subscription Request Action from DUT. [DUT as Client] | Product |
| Interaction Data Model | TC-IDM-4.2 | Subscription Response Action from DUT. [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-4.3 | Report Data Messages post Subscription Activation from DUT. [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-4.4 | Persistent Subscription Test Cases. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-4.5 | Subscription Wildcard Path Filter [DUT as Server] | Product |
| Interaction Data Model | TC-IDM-5.1 | Timed Request Action from DUT to TH. [DUT as Client] | Product |
| Interaction Data Model | TC-IDM-5.2 | Status Response from DUT in response to a Timed Request Action from TH. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-6.1 | Events Read Interaction from TH to DUT. [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-6.2 | Events Subscribe Interaction from TH to DUT. [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-6.3 | Events Read Interaction from DUT to TH. [DUT as Client] | Product |
| Interaction Data Model | TC-IDM-6.4 | Events Subscribe Interaction from DUT to TH. [DUT as Client] | Product |
| Interaction Data Model | TC-IDM-7.1 | Multi Fabric Subscription Test Cases. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-8.1 | Fabric scoped test cases. [DUT as Server] | Platform |
| Interaction Data Model | TC-IDM-9.1 | CONSTRAINT_ERROR status response test cases [DUT as Server] - PROVISIONAL | Provisio nal |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Interaction Data Model | TC-IDM-10.1 | Cluster requirements - Global attributes [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-10.2 | Cluster requirements - Conformance [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-10.3 | Cluster requirements - Revision [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-10.4 | Cluster requirements - PICS [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-10.5 | Device Type Requirements [DUT as Server] | Product |
| Interaction Data Model | TC-IDM-10.6 | Device Type Revisions [DUT as Server] | Product |
| Interaction Data Model | TC-IDM-11.1 | Data types - attribute strings [DUT as Server] | Both |
| Interaction Data Model | TC-IDM-12.1 | Device attribute information[DUT as Server] - data model | Product |
| Interaction Data Model | TC-IDM-13.1 | Accidental defaults check [DUT as Server] | Product |
| Interaction Data Model | TC-IDM-14.1 | Device-type-restricted clusters check [DUT as Server] | Product |
| Admin Commissioning Cluster | TC-CADMIN-1.1 | Administrator Behavior using ECM [DUT - Commissioner] | Product |
| Admin Commissioning Cluster | TC-CADMIN-1.2 | Administrator Behavior using BCM [DUT - Commissioner] | Product |
| Admin Commissioning Cluster | TC-CADMIN-1.3 | Node Behavior using ECM [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.4 | Node Behavior using BCM [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.5 | Commissioning window handling timeout and revocation using ECM [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.7 | Commissioning window handling timeout and revocation using ECM [DUT - Commissioner] | Product |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Admin Commissioning Cluster | TC-CADMIN-1.8 | Commissioning window handling timeout and revocation using BCM [DUT - Commissioner] | Product |
| Admin Commissioning Cluster | TC-CADMIN-1.9 | Device exit commissioning mode after 20 failed commission attempts [ECM] [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.10 | Revoke Commissioning Clears out PASE Session [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.11 | Open commissioning window on DUT using ECM then BCM [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.15 | Removing Fabrics from DUT and Fabric index enumeration using ECM [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.17 | Removing Fabrics from DUT and Fabric index enumeration using ECM [DUT - Commissioner] | Product |
| Admin Commissioning Cluster | TC-CADMIN-1.18 | Removing Fabrics from DUT and Fabric index enumeration using BCM [DUT - Commissioner] | Product |
| Admin Commissioning Cluster | TC-CADMIN-1.19 | max number of CommissionedFabrics and SupportedFabrics rollover using ECM [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.22 | Open commissioning window - durations max and max+ 1 [ECM] [DUT - Commissionee] | Platform |
| Admin Commissioning Cluster | TC-CADMIN-1.25 | Subscription to the attributes - verify subscription response [ECM] [DUT - Commissionee] | Platform |
| Bulk Data Exchange Protocol | TC-BDX-1.1 | Sender Initiated BDX Transfer Session - PROVISIONAL | Provisio nal |
| Bulk Data Exchange Protocol | TC-BDX-1.2 | Receiver Initiated BDX Transfer Session | Platform |
| Bulk Data Exchange Protocol | TC-BDX-1.3 | Response to Sender Initiated BDX Transfer Session - PROVISIONAL | Provisio nal |
| Bulk Data Exchange Protocol | TC-BDX-1.4 | Response to Receiver Initiated BDX Transfer Session | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Bulk Data Exchange Protocol | TC-BDX-1.5 | Response to Sender Initiated BDX Transfer Session - Negative scenario - PROVISIONAL | Provisio nal |
| Bulk Data Exchange Protocol | TC-BDX-1.6 | Response to Receiver Initiated BDX Transfer Session - Negative scenario - PROVISIONAL | Provisio nal |
| Bulk Data Exchange Protocol | TC-BDX-2.1 | Synchronous File Sending | Product |
| Bulk Data Exchange Protocol | TC-BDX-2.2 | Synchronous File Receiving | Platform |
| Bulk Data Exchange Protocol | TC-BDX-2.3 | Restart Synchronous File Receiving - PROVISIONAL | Provisio nal |
| Bulk Data Exchange Protocol | TC-BDX-2.4 | Asynchronous File Sending - PROVISIONAL | Provisio nal |
| Bulk Data Exchange Protocol | TC-BDX-2.5 | Asynchronous File Receiving - PROVISIONAL | Provisio nal |
| Software Update | TC-SU-1.1 | Invoke AnnounceOTAProvider from Admin(DUT) to OTA-R | Product |
| Software Update | TC-SU-2.1 | QueryImage Command from DUT to OTA-P | Both |
| Software Update | TC-SU-2.2 | Handling different QueryImageResponse scenarios on Requestor | Platform |
| Software Update | TC-SU-2.3 | Transfer of Software Update Images between OTA-R(DUT) and OTA-P | Both |
| Software Update | TC-SU-2.4 | ApplyUpdateRequest command from DUT to OTA-P | Both |
| Software Update | TC-SU-2.5 | Handling different ApplyUpdateResponse scenarios on Requestor | Platform |
| Software Update | TC-SU-2.6 | NotifyUpdateApplied Command from DUT to OTA-P | Platform |
| Software Update | TC-SU-2.7 | Verifying Events on OTA-R(DUT) | Platform |
| Software Update | TC-SU-2.8 | OTA functionality in Multi Fabric scenario | Both |
| Software Update | TC-SU-3.1 | QueryImageResponse from DUT to OTA-R | Product |
| Software Update | TC-SU-3.2 | Handling different QueryImageResponse scenarios on Provider | Product |
| Software Update | TC-SU-3.3 | Transfer of Software Update Images between OTA-R and OTA-P(DUT) | Product |
| Software Update | TC-SU-3.4 | Handling different ApplyUpdateResponse scenarios on Provider | Product |
| Software Update | TC-SU-4.1 | Verifying cluster attributes on OTA-R(DUT) | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Software Update | TC-SU-5.1 | Verifying vendor specific OTA implementation on DUT | Product |
| Access Control Cluster | TC-ACE-1.1 | Privileges [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACE-1.2 | Subscriptions [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACE-1.3 | Subjects [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACE-1.4 | Targets [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACE-1.5 | Multi-fabric [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACE-1.6 | Group auth mode [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACE-2.1 | Attribute read privilege enforcement - [DUT as Server] | Product |
| Access Control Cluster | TC-ACE-2.2 | Attribute write privilege enforcement - [DUT as Server] | Product |
| Access Control Cluster | TC-ACE-2.3 | Command privilege enforcement - [DUT as Server] | Product |
| Access Control Cluster | TC-ACE-2.4 | Attribute read subscription report - [DUT as Server] - PROVISIONAL | Provisio nal |
| ICD Management Cluster | TC-ICDM-2.1 | Attributes with DUT as Server | Platform |
| ICD Management Cluster | TC-ICDM-3.1 | Register/Unregister Clients with DUT as Server | Platform |
| ICD Management Cluster | TC-ICDM-3.2 | Verify RegisterClient Command with DUT as Server | Platform |
| ICD Management Cluster | TC-ICDM-3.3 | Verify UnregisterClient Command with DUT as Server | Platform |
| ICD Management Cluster | TC-ICDM-3.4 | ICDCounter Persistence with DUT as Server | Platform |
| ICD Management Cluster | TC-ICDM-4.1 | Stay Active Request with DUT as Server | Platform |
| ICD Management Cluster | TC-ICDM-5.1 | Operating Mode with DUT as Server | Platform |
| ICD Management Cluster | TC-ICDM-5.2 | Operating Mode with DUT as Server - Multi- Fabrics | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| ICD Management Cluster | TC-ICDM-6.1 | Functionality with DUT as Client | Product |
| ICD Behavior | TC-ICDB-1.1 | ICD Check-In Protocol - Register client - idle mode duration [DUT as Server] | Platform |
| ICD Behavior | TC-ICDB-1.2 | ICD Check-In Protocol - Register client - user active mode trigger [DUT as Server] | Product |
| ICD Behavior | TC-ICDB-1.3 | ICD Check-In Protocol - Client response [DUT as Client] | Platform |
| ICD Behavior | TC-ICDB-2.1 | ICD State Machine - With client registration and no active subscription - Single Fabric [DUT as Server] | Platform |
| ICD Behavior | TC-ICDB-2.2 | ICD State Machine - With client registration and active subscription - Single Fabric [DUT as Server] | Platform |
| ICD Behavior | TC-ICDB-2.3 | ICD State Machine - With client registrations and no active subscription - Multiple Fabrics [DUT as Server] | Platform |
| ICD Behavior | TC-ICDB-2.4 | ICD State Machine - With client registrations and active subscriptions - Multiple Fabrics [DUT as Server] | Platform |
| ICD Behavior | TC-ICDB-2.5 | ICD State Machine - With 1 client registration with subscription and 1 unregistered client with subscription - Multiple Fabrics [DUT as Server] | Platform |
| ICD Behavior | TC-ICDB-3.1 | ICD Dynamic SIT/LIT - Verify OperatingMode transition between LIT and SIT when there is client registration with DUT as Server | Product |
| ICD Behavior | TC-ICDB-3.2 | ICD Dynamic SIT/LIT - Verify OperatingMode does not transition between LIT and SIT when there is no client registration with DUT as Server | Product |
| Minimal Resource Requirements | TC-RR-1.1 | Minimal Resource Requirements for Matter Node | Both |
| Software Diagnostics Cluster | TC-DGSW-2.1 | Attributes [{DUT_Sever}] | Platform |
| Software Diagnostics Cluster | TC-DGSW-2.2 | Event Functionality [{DUT_Sever}] | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Software Diagnostics Cluster | TC-DGSW-2.3 | Command Received [{DUT_Sever}] | Platform |
| Software Diagnostics Cluster | TC-DGSW-3.2 | Commands Generated [DUT as Client] | Product |
| Ethernet Network Diagnostics Cluster | TC-DGETH-2.1 | Attributes [DUT as Server] | Platform |
| Ethernet Network Diagnostics Cluster | TC-DGETH-2.2 | Command Received [DUT as Server] | Platform |
| Ethernet Network Diagnostics Cluster | TC-DGETH-3.2 | Command Generated [DUT as Client] | Product |
| Thread Diagnostics Cluster | TC-DGTHREAD-2.1 | Attributes [DUT as Server] | Platform |
| Thread Diagnostics Cluster | TC-DGTHREAD-2.2 | Attributes-Tx [DUT as Server] | Platform |
| Thread Diagnostics Cluster | TC-DGTHREAD-2.3 | Attributes-Rx [DUT as Server] | Platform |
| Thread Diagnostics Cluster | TC-DGTHREAD-2.4 | ResetCounts Command [DUT as Server] | Platform |
| Thread Diagnostics Cluster | TC-DGTHREAD-2.5 | Events [DUT as Server] - PROVISIONAL | Provisio nal |
| Thread Diagnostics Cluster | TC-DGTHREAD-3.4 | ResetCounts Command [DUT as Client] | Product |
| Wi-Fi Network Diagnostics Cluster | TC-DGWIFI-2.1 | Attributes [DUT as Server] | Platform |
| Wi-Fi Network Diagnostics Cluster | TC-DGWIFI-2.2 | Event Functionality [DUT as Server] | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Wi-Fi Network Diagnostics Cluster | TC-DGWIFI-2.3 | Command Received [DUT as Server] | Platform |
| Wi-Fi Network Diagnostics Cluster | TC-DGWIFI-3.2 | Commands Generated [DUT as Client] | Product |
| Diagnostic Logs Cluster | DLOG-2.1 | Diagnostic Logs Cluster Commands Checks with BDX with DUT as Server | Platform |
| General Diagnostics Cluster | TC-DGGEN-2.1 | Attributes [DUT as Server] | Platform |
| General Diagnostics Cluster | TC-DGGEN-2.2 | Event Functionality [DUT as Server] | Platform |
| General Diagnostics Cluster | TC-DGGEN-2.3 | Command Received [DUT as Server] | Platform |
| General Diagnostics Cluster | TC-DGGEN-2.4 | TimeSnapshot Command Tests [DUT as Server] | Platform |
| General Diagnostics Cluster | TC-DGGEN-2.5 | DeviceLoadStatus Attribute Tests [DUT as Server] - PROVISIONAL | Product |
| General Diagnostics Cluster | TC-DGGEN-3.1 | Matter Specification 1.2 errata [DUT as Server] | Platform |
| General Diagnostics Cluster | TC-DGGEN-3.2 | DMTEST Feature Test [DUT as Server] | Platform |
| General Commissioning Cluster | TC-CGEN-2.1 | Breadcrumb, BasicCommissioningInfo, RegulatoryConfig, LocationCapability and SupportsConcurrentConnection attributes [DUT as Server] | Platform |
| General Commissioning Cluster | TC-CGEN-2.2 | ArmFailSafe command verification [DUT as Server] | Platform |
| General Commissioning Cluster | TC-CGEN-2.4 | Verification For CommissioningError on response message [DUT as Server] | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| General Commissioning Cluster | TC-CGEN-2.5 | Verification for SetTCAcknowledgements [DUT as Server] | Product |
| General Commissioning Cluster | TC-CGEN-2.6 | Verification for CommissioningComplete when no terms are accepted when required [DUT as Server] | Product |
| General Commissioning Cluster | TC-CGEN-2.7 | Verification for CommissioningComplete when SetTCAcknowledgements provides invalid terms [DUT as Server] | Product |
| General Commissioning Cluster | TC-CGEN-2.8 | Verification that TCAcknowledgements, TCAcceptedVersion, and TCAcknowledgementsRequired are reset after Factory Reset [DUT as Server] | Product |
| General Commissioning Cluster | TC-CGEN-2.9 | Verification that TCAcknowledgements is reset after all fabrics removed [DUT as Server] | Product |
| General Commissioning Cluster | TC-CGEN-2.10 | Verification that required terms can't be unset from TCAcknowledgements with SetTCAcknowledgements [DUT as Server] | Product |
| General Commissioning Cluster | TC-CGEN-2.11 | Verification that TCAcknowledgements and TCAcceptedVersion can be updated after being commissioned [DUT as Server] | Product |
| General Commissioning Cluster | TC-CGEN-2.12 | Commissioning Flow - Enhanced Setup Flow Terms and Conditions [DUT - Commissioner] - PROVISIONAL | Provisio nal |
| Localization Configuration Cluster | TC-LCFG-2.1 | Localization Configuration Cluster Attributes[DUT-Server] | Both |
| Time Format Localization Cluster | TC-LTIME-3.1 | Read and Write to Time Format Localization Cluster Attributes [DUT as Server] | Platform |
| Groups Cluster | TC-G-2.1 | Attributes [DUT-Server] | Platform |
| Groups Cluster | TC-G-2.2 | Commands - AddGroup, ViewGroup, RemoveGroup, RemoveAllGroups [DUT-Server] | Platform |
| Groups Cluster | TC-G-2.4 | Commands - AddGroup Command with same GroupID on Multiple Endpoint [DUT-Server] | Platform |
| Groups Cluster | TC-G-2.3 | Commands - GetGroupMembership, AddGroupIfIdentifying [DUT-Server] | Platform |
| Groups Cluster | TC-G-3.2 | Commands [DUT-Client] | Product |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Access Control Cluster | TC-ACL-2.1 | Simple attributes [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.2 | Cluster endpoint [DUT-Commissionee] | Product |
| Access Control Cluster | TC-ACL-2.3 | Extension attribute [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.4 | ACL attribute [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.5 | AccessControlExtensionChanged event [DUT- Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.6 | AccessControlEntryChanged event [DUT- Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.7 | Extension multi-fabric [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.8 | ACL multi-fabric [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.9 | Cluster access [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.10 | Persistence [DUT-Commissionee] | Platform |
| Access Control Cluster | TC-ACL-2.11 | Verification of Managed Device feature [DUT- Server] | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.1 | Attributes with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.2 | {C_SET_UTC_TIME} command with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.3 | SetTrustedTimeSource command with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.4 | SetTimeZone command with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.5 | {C_SET_DST_OFFSET} command with DUT as Server | Platform |

| Test Plan Cluster Name | TestID | Description | Tagging |
| Time Synchronization Cluster | TC-TIMESYNC-2.6 | {C_SET_DEFAULT_NTP} command with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.7 | {A_LOCAL_TIME} calculation for time zone with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.8 | {A_LOCAL_TIME} calculation for DST offset with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.9 | {A_LOCAL_TIME} calculation for time zone with DST offset with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.10 | {E_DST_TABLE_EMPTY} event generation with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.11 | {E_DST_STATUS} event generation with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.12 | {E_TIME_ZONE_STATUS} event generation with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-2.13 | {E_MISSING_TRUSTED_TIME_SOURCE} event generation with DUT as Server | Platform |
| Time Synchronization Cluster | TC-TIMESYNC-3.1 | Endpoint composition with DUT as Server | Product |
