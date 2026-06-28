## ALIRO Specification Test Plan Version 1.0
February 9, 2026


## 1 Introduction

## 1.1 Scope

This test plan covers the tests for Aliro 1.0.

## 1.2 Purpose

Describes tests to be performed for supported Aliro 1.0 features.

## 1.3 Provisional Status Notification

This section exists to inform of the results implications of the validation process on technical specification. As per Connectivity Standards Alliance Policies &amp; Procedures, the following items are marked as provisional based on the results of the Aliro Standard Validation Event resolution.

- [Optional] User Device test as in 7.13 Select Response with User Device Descriptor Tag
- [Optional] User Device test as in 7.40 BLE+UWB Flow with User Device Descriptor Tag
- [Optional] User Device test as in 7.50 BLE-Only Flow with Expedited Standard Phase
- [Optional] User Device test as in 7.51 BLE-Only Flow with User Device Descriptor Tag
- [Optional] User Device test as in 7.52 BLE-Only Flow with Failed L2CAP

## 2 References

[1] ALIRO Specification Version 0.9.0

## 3 Definitions

## 3.1 Acronyms

The acronyms are defined in Aliro 1.0 [1].

## 3.2 Glossary

| Access Credential | A set of information that contains all data necessary to perform the access transaction, this includes the Access Credential key pair and an optional Access Document. |
| Revocation Data Element | Standardized structure to define revocation information |

## 3.3 Conformance Levels

The key word meaning is defined in Aliro 1.0 [1].

## 4 Test Setup

## 4.1 Architecture

Figure 4-1 provides a detailed illustration of the Aliro Test Harness. This system is designed to execute test scripts that align with the test plan. Within this setup, the Aliro Actuator represents the implementation of the Aliro technical specifications.

The Test Harness is built around the Raspberry Pi development platform. It interfaces with various external platforms: UWB, BLE, and NFC. Specifically, it employs the NXP Murata SR150 UWB platform, which is connected via a USB interface using UCI-PnP. For NFC operations, the Test Harness utilizes the NXP PN7160 Reader/Card Emulation NFC platform, connected through an SPI or I2C interface, depending on the model of the NFC platform. The Bluetooth LE in the Murata board is used and not the the Raspberry Pi's built-in Bluetooth module for the performance purposes.

The Test Harness communicates wirelessly with the Device Under Test (DUT) using the Aliro Protocol.

Figure 4-1 Aliro Test Harness architecture

## 4.1.1 PICS

In this section the PICS parameter requirements for Reader and User Device are enumerated. 'M' implies mandatory feature, 'O' implies optional feature, 'C' implies conditional feature, and 'NA' implies feature Not Applicable for the purposes of tests. PICS parameter with a corresponding empty cell implies no test is defined.

Table 4-1 Expedited-Standard phase PICS parameters

| PICS Parameter | Re ad er | Us er De vi ce | Reader Test Identifier | User Device Test Identifier |
| Expedited- Standard Phase | M | M | NFC_RDR_STANDARD_NO_CER T, NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING, | NFC_UD_STANDARD_NO_CERT, NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, |

| PICS Parameter | Re ad er | Us er De vi ce | Reader Test Identifier | User Device Test Identifier |
| | | | NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING, NFC_RDR_NEG_SEL_RSP_NO_C OMMON_EXPEDITED_PROTOC OL_VERSION, NFC_RDR_NEG_AUTH0_EXTRA _TAG, NFC_RDR_NEG_AUTH0_WRON G_VALUE, NFC_RDR_NEG_AUTH1_WRON G_UD_SIGNATURE, NFC_RDR_NEG_AUTH1_EXTRA _TAG, NFC_RDR_NEG_AUTH1_WRON G_VALUES | NFC_UD_AUTH0_RESPONSE_CHAINING, NFC_UD_NEG_AUTH0_UNKNOWN_REA DER_ID, NFC_UD_NEG_AUTH0_UNSUPPORTED_ PROTOCOL_VERSION, NFC_UD_NEG_AUTH0_EXTRA_TAG, NFC_UD_NEG_AUTH0_WRONG_VALUE, NFC_UD_NEG_AUTH0_WRONG_P1P2, NFC_UD_NEG_AUTH0_CHAINING_NOT_ COMPLETED, NFC_UD_NEG_AUTH1_WRONG_READE R_SIGNATURE, NFC_UD_NEG_AUTH1_EXTRA_TAG, NFC_UD_NEG_AUTH1_WRONG_P1P2, NFC_UD_NEG_AUTH1_WRONG_VALUE |
| Reader signature generation and validation using reader_Pub K | M | M | NFC_RDR_STANDARD_NO_CER T | NFC_UD_STANDARD_NO_CERT, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| Reader signature generation and validation using intermediat e_reader_P ubK (from reader_Cer t) | M | M | NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| Device signature generation and validation | M | M | NFC_RDR_STANDARD_NO_CER T, NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING, | NFC_UD_STANDARD_NO_CERT, NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, |

| PICS Parameter | Re ad er | Us er De vi ce | Reader Test Identifier | User Device Test Identifier |
| | | | NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING | NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| Verificatio n of reader_Cer t with the CA public key | N A | M | NA | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING, NFC_UD_NEG_STANDARD_CERT_IN_LO AD_CERT_WITH_CHAINING_INCORREC T_SIGNATURE, NFC_UD_NEG_STANDARD_CERT_IN_LO |
| Verificatio n of reader_Cer t with the CA public key - reader_Cer t expiration time validation | N A | O | NA | |
| Lookup of the reader key through reader_gro up_identifi er | N A | M | NA | NFC_UD_STANDARD_NO_CERT, NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G |
| Lookup of reader CA public key through reader_gro | N A | M | NA | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING |

| PICS Parameter | Re ad er | Us er De vi ce | Reader Test Identifier | User Device Test Identifier |
| up_identifi er | | | | |
| Presentatio n and validation of reader_Cer t | M | M | NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| Presentatio n and validation of reader_Cer t in AUTH1 command | C | M | NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING | NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| Presentatio n and validation of reader_Cer t in LOAD_CE RT command | C | M | NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING |
| AUTH1 command command_ parameter | M | M | NFC_RDR_STANDARD_NO_CER T, NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING | NFC_UD_STANDARD_NO_CERT, NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| AUTH1 command | C | M | NFC_RDR_STANDARD_NO_CER T, | NFC_UD_STANDARD_NO_CERT, |

| PICS Parameter | Re ad er | Us er De vi ce | Reader Test Identifier | User Device Test Identifier |
| command_ parameter - key slot | | | NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| AUTH1 command command_ parameter - Access Credential Public Key | C | M | NFC_RDR_STANDARD_NO_CER T, NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_WITH_CHAINING , NFC_RDR_STANDARD_CERT_IN _LOAD_CERT_NO_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN _AUTH1_NO_CHAINING | NFC_UD_STANDARD_NO_CERT, NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAININ G, NFC_UD_STANDARD_CERT_IN_LOAD_C ERT_NO_CHAINING, NFC_UD_STANDARD_CERT_IN_AUTH1_ WITH_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |
| Subset of mailbox in AUTH1 command response | N A | M | NA | |

## Table 4-2 Expedited-Fast phase PICS parameters

| PICS Parameter | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifier |
| Expedite d-Fast Phase | O | O | NFC_RDR_F AST | NFC_UD_FAST, NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONS ECUTIVE_FAST |
| Cryptogr am generatio n and validatio n | M | M | NFC_RDR_F AST | NFC_UD_FAST, NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONS ECUTIVE_FAST |

Table 4-3 Expedited Phase PICS parameters

| PICS Parameter | Re ade r | Us er De vic e | Reader Test Identifier | User Device Test Identifier |
| Command chaining | M | M | NFC_RDR_STANDARD_CERT_IN_ LOAD_CERT_WITH_CHAINING, NFC_RDR_STANDARD_CERT_IN_ AUTH1_WITH_CHAINING | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_C HAINING, NFC_UD_STANDARD_CERT_IN_ AUTH1_WITH_CHAINING, NFC_UD_AUTH0_RESPONSE_CH AINING, NFC_UD_NEG_AUTH1_CHAININ G_NOT_COMPLTED, |
| Extended length | O | O | NFC_RDR_STANDARD_CERT_IN_ LOAD_CERT_NO_CHAINING, NFC_RDR_STANDARD_CERT_IN_ AUTH1_NO_CHAINING | NFC_UD_STANDARD_CERT_IN_ LOAD_CERT_NO_CHAINING, NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAININ G, NFC_UD_EXCHANGE_WITH_EX TENDED_LENGTH |
| User authentication policy enforcement | N A | M | NA | NFC_UD_STANDARD_NO_CERT |
| Support for credential_sign ed_timestamp in AUTH0/AUT H1 | N A | M | | |
| Support for revocation_sig ned_timestamp in AUTH0/AUT H1 | N A | M | | |
| Allow at least 16 reader_group_i dentifier per Access Credential | N A | M | NA | NFC_UD_STANDARD_SIXTEEN_ GROUPPIDENTIFIER_ONE_AC |

| PICS Parameter | Re ade r | Us er De vic e | Reader Test Identifier | User Device Test Identifier |
| User Device has a method to use all Access Credentials bound to the reader identifier | N A | M | NA | |
| EXCHANGE command | M | M | | NFC_UD_EXCHANGE_WITH_CH AINING, NFC_UD_NEG_EXCHANGE_WIT H_EXTRA_TAG, NFC_UD_NEG_EXCHANGE_WIT H_WRONG_LENGTH |
| EXCHANGE command - notify credential issuer in EXCHANGE | O | O | | |
| EXCHANGE command - notify bound application in EXCHANGE | O | O | | |
| EXCHANGE command - Update document in EXCHANGE | O | O | | |
| EXCHANGE command - Update document in EXCHANGE - providing and processing update_doc contents | N A | N A | NA | NA |
| Mailbox | O | M | NFC_RDR_EXCHANGE_MAILBOX | NFC_UD_EXCHANGE_SET_REQ UEST, |

| PICS Parameter | Re ade r | Us er De vic e | Reader Test Identifier | User Device Test Identifier |
| | | | | NFC_UD_NEG_EXCHANGE_MAI LBOX_OUT_OF_BOUNDS |
| Mailbox Read/Write by credential issuer | N A | N A | NA | NA |
| Read from Mailbox | O | M | | NFC_UD_EXCHANGE_READ_RE QUEST |
| Write to Mailbox | O | M | | NFC_UD_EXCHANGE_WRITE_R EQUEST |
| Reader Descriptor tag | O | N A | NFC_RDR_EXCHANGE_RDR_DES CRIPTOR_TAG, NFC_RDR_EXCHANGE_RDR_DES CRIPTOR_TAG, NFC_RDR_CONTROL_FLOW_RDR _DESCRIPTOR_TAG, BLEUWB_RDR_CONTROL_FLOW_ RDR_DESCRIPTOR_TAG | NA |
| User Device Descriptor Tag | N A | O | NA | NFC_UD_SELECT_RESPONSE_U D_DESCRIPTOR_TAG, BLEUWB_UD_UD_DESCRIPTOR _TAG, BLERKE_UD_UD_DESCRIPTOR_ TAG |

Table 4-4 Step-Up Phase PICS parameters

| PICS Paramete r | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifier |
| Step-Up phase | O | M | NFC_RDR_STEPUP_AD_KEY_ID, NFC_RDR_STEPUP_AD_ISSUER_CERT, NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID, NFC_RDR_STEPUP_AD_ACCESS_RULE, NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES, NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXT ENSION, NFC_RDR_STEPUP_AD_UNKNOWN_NON_CRITICAL_AC CESS_EXTENSION, NFC_RDR_NEG_STEPUP_AD_NO_ISSUER_CERT_NO_KE Y_ID, | NFC_UD_STEPU P_AD, NFC_UD_STEPU P_RD |

| PICS Paramete r | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifier |
| | | | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_INVALID_SI GNATURE, NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED, NFC_RDR_NEG_STEPUP_AD_INVALID_SIGNATURE_ISS UER_AUTH, NFC_RDR_NEG_STEPUP_AD_INVALID_HASH_ISSUER_A UTH, NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH, NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH, NFC_RDR_NEG_STEPUP_AD_ISSUER_CERTIFICATE_TI ME_MISMATCH, NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION, NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQ UIRED, NFC_RDR_NEG_STEPUP_AD_NO_DATA_ELEMENTS, NFC_RDR_NEG_STEPUP_AD_ISSUER_DOCTYPE_MISMA TCH, NFC_RDR_NEG_STEPUP_AD_DEVICE_KEY_INFO_MISM ATCH, NFC_RDR_NEG_STEPUP_AD_INVALID_ACCESS_DATA_ ELEMENT_VERSION, NFC_RDR_NEG_STEPUP_AD_NO_ACCESS_RULE_FOR_R EADER_ACTION, NFC_RDR_NEG_STEPUP_AD_NO_VALID_SCHEDULE_AL LOW_SCHEDULEID, NFC_RDR_NEG_STEPUP_AD_VALID_SCHEDULE_DENY_ SCHEDULEID, NFC_RDR_NEG_STEPUP_AD_SCHEDULE_TIME_VERIFY _REQUIRED, NFC_RDR_NEG_STEPUP_AD_SCHEDULE_IN_ACCESS_R ULE_AND_READER, NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RUL E, NFC_RDR_NEG_STEPUP_AD_UNKNOWN_CRITICAL_AC CESS_EXTENSION, NFC_RDR_STEPUP_RD, | |
| Step-Up phase - Access docume nt storage | O | M | NFC_RDR_STEPUP_AD_KEY_ID | NFC_UD_STEPU P_AD |

| PICS Paramete r | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifier |
| and retrieval | | | | |
| Step-Up phase - Revocat ion docume nt storage and retrieval | O | M | NFC_RDR_STEPUP_RD, NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERS ION | NFC_UD_STEPU P_RD |

Table 4-5 Access Document processing PICS parameters

| PICS Parameter | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifi er |
| Access documen t processin g | O | NA | NFC_RDR_STEPUP_AD_ISSUER_CERT, NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID, NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXTENSIO N, NFC_RDR_STEPUP_AD_UNKNOWN_NON_CRITICAL_ACCESS_ EXTENSION, NFC_RDR_NEG_STEPUP_AD_NO_ISSUER_CERT_NO_KEY_ID, NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_INVALID_SIGNAT URE, NFC_RDR_NEG_STEPUP_AD_INVALID_SIGNATURE_ISSUER_A UTH, NFC_RDR_NEG_STEPUP_AD_INVALID_HASH_ISSUER_AUTH, NFC_RDR_NEG_STEPUP_AD_ISSUER_CERTIFICATE_TIME_MIS MATCH, NFC_RDR_NEG_STEPUP_AD_NO_DATA_ELEMENTS, NFC_RDR_NEG_STEPUP_AD_ISSUER_DOCTYPE_MISMATCH, NFC_RDR_NEG_STEPUP_AD_DEVICE_KEY_INFO_MISMATCH, NFC_RDR_NEG_STEPUP_AD_INVALID_ACCESS_DATA_ELEME NT_VERSION, NFC_RDR_NEG_STEPUP_AD_NO_ACCESS_RULE_FOR_READE R_ACTION, NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE, NFC_RDR_NEG_STEPUP_AD_UNKNOWN_CRITICAL_ACCESS_ EXTENSION | NA |

| PICS Parameter | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifi er |
| Access documen t verificati on | M | NA | NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED, NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH, NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH, NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION, NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQUIRED | NA |
| Access documen t verificati on - Validity iteration | M | NA | NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION | NA |
| Access documen t verificati on - Validity time- based elements | O | NA | NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED, NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH, NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH, NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQUIRED , NFC_RDR_NEG_STEPUP_AD_SCHEDULE_TIME_VERIFY_REQU IRED | NA |
| Access data element verificati on | M | NA | NFC_RDR_STEPUP_AD_ACCESS_RULE, NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES | NA |
| Access data element verificati on - Access Rules | M | NA | NFC_RDR_STEPUP_AD_ACCESS_RULE | NA |
| Access data element verificati on - | O | NA | NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES, NFC_RDR_NEG_STEPUP_AD_NO_VALID_SCHEDULE_ALLOW_ SCHEDULEID, NFC_RDR_NEG_STEPUP_AD_VALID_SCHEDULE_DENY_SCHE DULEID, | NA |

| PICS Parameter | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifi er |
| Schedule s | | | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_IN_ACCESS_RULE_A ND_READER | |
| Access data element verificati on - Access extensio n criticalit y | M | NA | | NA |
| Access data element verificati on - Access extensio n content | NA | NA | NA | NA |
| Access data element verificati on - Non access extensio n | NA | NA | NA | NA |
| Access data element verificati on - Reader rules | O | NA | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE | NA |
| Access data element verificati on - ID | NA | NA | NA | NA |

Table 4-6 Revocation document processing PICS parameters

| PICS Parameter | Reade r | User Devic e | Reader Test Identifier | User Device Test Identifie r |
| Revocatio n document processing | O | NA | NFC_RDR_STEPUP_RD, NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSI ON | NA |
| Revocatio n document verificatio n | M | NA | NFC_RDR_STEPUP_RD, NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSI ON | NA |
| Revocatio n element verificatio n | M | NA | NFC_RDR_STEPUP_RD, NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSI ON | NA |

Table 4-7 NFC interface PICS parameters

| PICS Parameter | Reader | User Device | Reader Test Identifier | User Device Test Identifier |
| NFC Interface | M | M | Table 4-1 | Table 4-1 |
| NFC - Step-Up AID SELECT | M | O | NFC_RDR_STEPUP_AD_KEY_ID | |
| Vendor-specific extensions in SELECT | NA | NA | NA | NA |

Table 4-8 BLE interface PICS parameters

| PICS Parameter | Reader | User Device | Reader Test Identifier | User Device Test Identifier |
| BLE Interface | O | O | Table 4-9, Table 4-10 | Table 4-9, Table 4-10 |

| PICS Parameter | Reader | User Device | Reader Test Identifier | User Device Test Identifier |
| BLE - send sensor triggered bit | O | O | | |
| Dynamic advertisement tag | M | O | BLEUWB_RDR_EXPEDITED_STANDARD_PHASE, BLEUWB_RDR_EXPEDITED_FAST_PHASE, BLEUWB_RDR_STEPUP_PHASE, BLEUWB_RDR_ADVERTISEMENT_FORMAT | |
| Pass Through | O | O | | |
| Unsolicited Reader status reporting | M | NA | BLEUWB_RDR_EXPEDITED_STANDARD_PHASE, BLEUWB_RDR_EXPEDITED_FAST_PHASE, BLEUWB_RDR_STEPUP_PHASE, BLERKE_RDR_UNSECURE, BLERKE_RDR_SECURE | NA |

Table 4-9 BLE + UWB interface PICS parameters for Bluetooth LE + UWB Aliro Flow

| PICS Parameter | Rea der | Use r Dev ice | Reader Test Identifier | User Device Test Identifier |
| Bluetooth LE + UWB Flow | O | O | BLEUWB_RDR_CONTROL_FLOW_R DR_DESCRIPTOR_TAG, BLEUWB_RDR_EXPEDITED_STAND ARD_PHASE, BLEUWB_RDR_EXPEDITED_FAST_P HASE, BLEUWB_RDR_STEPUP_PHASE, BLEUWB_RDR_RANGING_SUSPEND, BLEUWB_RDR_RANGING_RESUME, BLEUWB_RDR_NEG_FAILED_L2CAP , BLEUWB_RDR_NEG_FAILED_SPSM_ L2CAP, BLEUWB_RDR_NEG_TIMEOUT_BEF ORE_AUTH0, BLEUWB_RDR_TIMEOUT_EXTENSI ON, BLEUWB_RDR_NEG_M2_MISMATCH _PARAMETER, | BLEUWB_UD_EXPEDITED_STAND ARD_PHASE, BLEUWB_UD_EXPEDITED_FAST_P HASE, BLEUWB_UD_STEPUP_PHASE, BLEUWB_UD_RANGING_SUSPEND , BLEUWB_UD_RANGING_RESUME, BLEUWB_UD_UD_DESCRIPTOR_T AG, BLEUWB_UD_NEG_WRONG_ADV, BLEUWB_UD_NEG_FAILED_L2CAP , BLEUWB_UD_NEG_TIMEOUT_BEF ORE_AUTH0, BLEUWB_UD_TIMEOUT_EXTENSI ON, BLEUWB_UD_NEG_URSK_NOT_FO UND, |

| PICS Parameter | Rea der | Use r Dev ice | Reader Test Identifier | User Device Test Identifier |
| | | | BLEUWB_RDR_NEG_M4_MISMATCH _PARAMETER, BLEUWB_RDR_NEG_SUSPEND_MIS MATCH_PARAMETER, BLEUWB_RDR_ADVERTISEMENT_F ORMAT | BLEUWB_UD_NEG_M1_MISMATC H_PARAMETER, BLEUWB_UD_NEG_M3_MISMATC H_PARAMETER |
| UWB ranging | M | M | BLEUWB_RDR_EXPEDITED_STAND ARD_PHASE, BLEUWB_RDR_EXPEDITED_FAST_P HASE, BLEUWB_RDR_STEPUP_PHASE | BLEUWB_UD_EXPEDITED_STAND ARD_PHASE, BLEUWB_UD_EXPEDITED_FAST_P HASE, BLEUWB_UD_STEPUP_PHASE |
| UWB ranging suspend | M | M | BLEUWB_RDR_RANGING_SUSPEND, BLEUWB_RDR_NEG_SUSPEND_MIS MATCH_PARAMETER | BLEUWB_UD_RANGING_SUSPEND , BLEUWB_UD_NEG_SUSPEND_MIS MATCH_PARAMETER |
| UWB ranging resume | M | M | BLEUWB_RDR_RANGING_RESUME | BLEUWB_UD_RANGING_RESUME, BLEUWB_UD_NEG_RESUME_MIS MATCH_PARAMETER |
| One ranging round | M | M | BLEUWB_RDR_EXPEDITED_STAND ARD_PHASE, BLEUWB_RDR_EXPEDITED_FAST_P HASE, BLEUWB_RDR_STEPUP_PHASE | BLEUWB_UD_EXPEDITED_STAND ARD_PHASE, BLEUWB_UD_EXPEDITED_FAST_P HASE, BLEUWB_UD_STEPUP_PHASE |
| Two ranging rounds | O | M | BLEUWB_RDR_EXPEDITED_STAND ARD_PHASE, BLEUWB_RDR_EXPEDITED_FAST_P HASE, BLEUWB_RDR_STEPUP_PHASE | BLEUWB_UD_EXPEDITED_STAND ARD_PHASE, BLEUWB_UD_EXPEDITED_FAST_P HASE, BLEUWB_UD_STEPUP_PHASE |
| BLE UWB Time synchroni zation | O | M | BLEUWB_RDR_EXPEDITED_STAND ARD_PHASE, BLEUWB_RDR_EXPEDITED_FAST_P HASE, BLEUWB_RDR_STEPUP_PHASE | BLEUWB_UD_EXPEDITED_STAND ARD_PHASE, BLEUWB_UD_EXPEDITED_FAST_P HASE, BLEUWB_UD_STEPUP_PHASE |

Table 4-10 BLE interface PICS parameters for BLE-Only Flow

| PICS Paramet er | Read er | User Devi ce | Reader Test Identifier | User Device Test Identifier |
| BLE- Only Flow | O | O | BLERKE_RDR_UNSECURE, BLERKE_RDR_SECURE, BLERKE_RDR_NEG_FAST, BLERKE_RDR_NEG_FAILED_L2CA P, BLERKE_RDR_NEG_FAILED_SPSM _L2CAP, BLERKE_RDR_STEPUP_PHASE | BLERKE_UD_EXPEDITED_STANDAR D_PHASE, BLERKE_UD_UD_DESCRIPTOR_TAG, BLERKE_UD_NEG_FAILED_L2CAP |
| Explici t Reader selecti on | NA | M | NA | BLERKE_UD_EXPEDITED_STANDAR D_PHASE |

## 5 User Device Under Test Routines

This section describes routines used in User Device Under Test tests.

## 5.1 SELECT Routine

Table 5-1 SELECT routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send SELECT command | | |
| 2 | | send SELECT response | Verify the following: 1. order of TLVs matches the technical specification 2. All mandatory TLVs in technical specification are present 3. 0100h is present in the expedited_phase_supported_protocol_versions. 4. size of SELECT response is less than 256B 5. AID = A000000909ACCE5501, if Expedited Phase 6. AID = A000000909ACCE5502, if Step-Up Phase 7. Type = 0000h 8. Unknown TLVs are ignored, if present If all criteria are met, then CONTINUE else FAIL. |

## 5.2 AUTH0 Routine

Table 5-2 AUTH0 routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | | send AUTH0 response | Verify the following: 1. order of TLVs matches technical specification 2. All mandatory TLVs in technical specification are present 3. cryptogram is not present, if command_parameters = 0h 4. cryptogram is present, if command_parameters = 1h 5. auth0_response_vendor_extension, if present is less than 127B in size |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | | | 6. SW = 9000h 9. Success in establishing secure channel 10. Unknown TLVs are ignored, if present If all criteria are met, then CONTINUE else FAIL. |

## 5.3 AUTH1 with SW Equal to 9000h Routine

## Table 5-3 AUTH1 with SW = 9000h routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 5 | Send AUTH1 command 1. command_parameters = randomly selected between 00h, 01h | | |
| 6 | | send AUTH1 response | Verify the following: 1. order of TLVs matches technical specification. 2. All mandatory TLVs in technical specification are present. 3. key_slot is present, if command_parameters = 01h. 4. Access Credential long term public key is present, if command_parameters = 00h. 5. SW = 9000h. 6. User Device signature verification passes. 7. Unknown TLVs are ignored, if present If all criteria are met, then CONTINUE else FAIL. |

## 5.4 AUTH1 with SW Not Equal to 9000h Routine

Table 5-4 AUTH1 with SW != 9000h routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send AUTH1 command 1. command_parameters = randomly selected between 00h, 01h | | |
| 2 | | send AUTH1 response | Verify the following: 1. SW != 9000h. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | | | 2. Response data field is empty. If all criteria are met, then CONTINUE else FAIL. |

## 5.5 EXCHANGE Indicating Transaction Success Routine

## Table 5-5 EXCHANGE indicating transaction success routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | | send EXCHANGE response. | Verify the following: 1. response payload = 0x0002&#124;&#124;&#124;0x00&#124;&#124;0x00. 2. SW = 9000h. If all criteria are met, then PASS else FAIL. |

## 5.6 EXCHANGE Indicating Transaction Failure Routine

Table 5-6 EXCHANGE indicating transaction failure routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | | send EXCHANGE response. | Verify the following: 1. response payload = 0x0002&#124;&#124;0x00&#124;&#124;0x00. 2. SW = 9000h. If all criteria are met, then PASS else FAIL. |

## 5.7 CONTROL FLOW Indicating Transaction Failure Routine

## Table 5-7 CONTROL FLOW indicating transaction failure routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send CONTROL FLOW command. | | Verify the following: CONTROL FLOW command data field length does not exceed 255 bytes. CONTROL FLOW command is formatted according to the specification. If all criteria are met, then CONTINUE else FAIL. |

## 5.8 BLE+UWB Aliro Access Protocol Routine

Table 5-8 BLE+UWB Aliro Access Protocol routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send Bluetooth LE advertisement | | |
| 2 | | Establish L2CAP connection | |
| 3 | | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | Verify the following: Format of Initiate Access Protocol Message ID matches specification. If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 7 | | Send EXCHANGE response | |
| 8 | Send Reader Status Access Protocol Completed Message ID carrying Reader Information Attribute ID | | Verify the following: Ensure reader status is secured. Format of message matches technical specification. If all criteria are met, then CONTINUE else FAIL. |

## 5.9 BLE+UWB Ranging Session Setup Routine

Table 5-9 BLE+UWB ranging session setup routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send Ranging Session Setup M1 Message ID | | |
| 2 | | send Ranging Session Setup M2 Message ID | Verify the following: Format of this message matches the specification. If all criteria are met, then CONTINUE else FAIL. |
| 3 | Send Ranging Session Setup M3 Message ID | | |
| 4 | | send Ranging Session Setup M4 Message ID | Verify the following: Format of this message matches the specification. If all criteria are met, then CONTINUE else FAIL. |

## 5.10 BLE-Only Aliro Access Protocol Routine

Table 5-10 BLE-only Aliro Access Protocol routine

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send Bluetooth LE advertisement. | | |
| 3 | | User register intent to perform RKE action. | Verify the following: User selects the Reader and indicates the action. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | | | Note: how the user selects the Reader, and the associated action is implementation choice. If all criteria are met, then CONTINUE else FAIL. |

## 6 Reader Under Test Routines

This section describes routines used in Reader Under Test tests.

## 6.1 SELECT Routine

Table 6-1 SELECT routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send SELECT command | Verify the following: 1. AID = A000000909ACCE5501, if Expedited Phase 2. AID = A000000909ACCE5502, if Step-Up Phase If all criteria are met, then CONTINUE else FAIL. |
| 2 | send SELECT response | | |

## 6.2 AUTH0 Routine

Table 6-2 AUTH0 routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send AUTH0 command | Verify the following: 1. order of TLVs in AUTH0 command matches specification. 2. All mandatory TLVs in AUTH0 command are present 3. expedited_phase_protocol_version = 0100h 4. Unknown TLVs are ignored, if present If all criteria are met, then CONTINUE else FAIL. |
| 2 | Send AUTH0 response | | |

## 6.3 AUTH1 Routine

Table 6-3 AUTH1 routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send AUTH1 command | Verify the following: 1. order of TLVs in AUTH1 command matches specification. 2. All mandatory TLVs in AUTH1 command are present 3. Unknown TLVs are ignored, if present If all criteria are met, then CONTINUE else FAIL. |
| 2 | Send AUTH1 response | | |

## 6.4 EXCHANGE Indicating Transaction Success Routine

## Table 6-4 EXCHANGE indicating transaction success routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | send EXCHANGE command with tag 0x97 (Reader Status) | Verify the following: 1. order of TLVs in EXCHANGE command matches specification. 2. All mandatory TLVs in EXCHANGE command are present 3. 0x97h first byte is 0x01h. 4. Unknown TLVs are ignored, if present If all criteria are met, then CONTINUE else FAIL. |
| 2 | Send EXCHANGE response | | |

## 6.5 EXCHANGE Indicating Transaction Failure Routine

Table 6-5 EXCHANGE indicating transaction failure routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | send EXCHANGE command with tag 0x97 (Reader Status) | Verify the following: 0x97h first byte is 0x00h. If all criteria are met, then CONTINUE else FAIL. |
| 2 | Send EXCHANGE response | | |

## 6.6 CONTROL FLOW Indicating Transaction Failure Routine

Table 6-6 CONTROL FLOW indicating transaction failure routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send CONTROL FLOW command. | Verify the following: 1. command data field length does not exceed 255 bytes. 2. Format of CONTROL FLOW command matches the specification. If all criteria are met, then CONTINUE else FAIL. |

## 6.7 BLE+UWB Aliro Access Protocol Routine

## Table 6-7 BLE+UWB Aliro Access Protocol routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE + UWBAliro Flow Supported Bit is set to 1. Advertisement format matches the technical specification. If all criteria are met, then CONTINUE else FAIL. |
| 2 | Establish L2CAP connection | | |
| 3 | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | | |
| 9 | Send EXCHANGE response | | |

## 6.8 BLE+UWB Ranging Session Setup Routine

## Table 6-8 BLE+UWB ranging session setup routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Send Ranging Message ID carrying Initiate Ranging Session Attribute ID | | |
| 2 | | Send Ranging Session Setup M1 Message ID | Verify the following: Format of this message matches the specification. If all criteria are met, then CONTINUE else FAIL. |
| 3 | send Ranging Session Setup M2 Message ID | | |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 4 | | send Ranging Session Setup M3 Message ID | Verify the following: Format of this message matches the specification. If all criteria are met, then CONTINUE else FAIL. |
| 5 | send Ranging Session Setup M4 Message ID | | |

## 6.9 BLE-Only Aliro Access Protocol Routine

## Table 6-9 BLE-only Aliro Access Protocol routine

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE-Only Aliro Flow Supported Bit is set to 1. Advertisement format matches the technical specification. If all criteria are met, then CONTINUE else FAIL. |
| 2 | Establish L2CAP connection | | |
| 3 | Send Initiate Access Protocol RKE Message ID carrying AID = A000000909ACCE5501 | | |
| 5 | send AUTH0 response | | |
| 6 | | Send AUTH1 command | |
| 7 | Send AUTH1 response | | |
| 8 | | [Optional] Send EXCHANGE command | |

## 7 User Device Under Test Conformance Tests

## 7.1 Expedited Standard Phase without Reader Certificate

Table 7-1 NFC\_UD\_STANDARD\_NO\_CERT test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STANDARD_NO_CERT |
| PICS | Expedited-Standard PhaseAND User Authentication Policy Enforcement AND Reader signature generation and validation using reader_PubK AND Device signature generation and validation AND Lookup of the reader key through reader_group_identifier AND AUTH1 command parameter |
| Applicability | Mfor User Device |
| Interface | NFC |

Table 7-2 NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK, reader_group_identifier |
| TH (Reader) | Access Credential long term public key |

Table 7-3 NFC\_UD\_STANDARD\_NO\_CERT test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h. auth0_command_vendor_extension is present in AUTH0 command. | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h. auth0_command_vendor_extension is present in AUTH0 command. | If all criteria are met, then CONTINUE else FAIL. |

## 7.2 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with APDU Chaining

## Table 7-4 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAINING |
| PICS | Expedited-Standard Phase AND Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Presentation and validation of the reader_Cert in LOAD_CERT command Device signature generation and validation AND Verification of the reader_Cert with the CA Public Key AND Lookup of the reader CA Public Key through reader_group_identifier AND AUTH1 command parameter AND Command chaining |
| Applicability | Mfor User Device |
| Interface | NFC |

## Table 7-5 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | Reader System Issuer CA public key, reader_group_identifier |
| TH (Reader) | Access Credential long term public key, reader_Cert |

## Table 7-6 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Send LOAD_CERT command with fragmented reader_cert with chaining. | | |

## 7.3 Expedited Standard Phase with Reader Cert in LOAD\_CERT without APDU Chaining

Table 7-7 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING |
| PICS | Expedited-Standard Phase AND Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Presentation and validation of the reader_Cert in LOAD_CERT command Device signature generation and validation AND Verification of the reader_Cert with the CA Public Key AND Lookup of the reader CA Public Key through reader_group_identifier AND AUTH1 command parameter AND Extended length |
| Applicability | Mfor User Device, if it supports Extended length APDUs |
| Interface | NFC |

NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

Table 7-8 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test steps

| Step# | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Send LOAD_CERT command with reader_cert and no APDU chaining. | | |

## 7.4 Expedited Standard Phase with Reader Cert in AUTH1 with APDU Chaining

Table 7-9 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STANDARD_CERT_IN_AUTH1_WITH_CHAINING |
| PICS | Expedited-Standard Phase AND Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Presentation and validation of the reader_Cert in AUTH1 command Device signature generation and validation AND Verification of the reader_Cert with the CA Public Key AND Lookup of the reader CA Public Key through reader_group_identifier AND AUTH1 command parameter AND Command chaining |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

Table 7-10 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is present and fragmented with chaining | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is present and fragmented with chaining | If all criteria are met, then CONTINUE else FAIL |

## 7.5 Expedited Standard Phase with Reader Cert in AUTH1 without APDU Chaining

Table 7-11 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |

| PICS | Expedited-Standard Phase AND Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Presentation and validation of the reader_Cert in AUTH1 command Device signature generation and validation AND Verification of the reader_Cert with the CA Public Key AND Lookup of the reader CA Public Key through reader_group_identifier AND AUTH1 command parameter AND Extended length |
| Applicability | Mfor User Device, if it supports Extended length APDU |
| Interface | NFC |

NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

Table 7-12 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test steps

| Step# | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is present and without chaining over | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is present and without chaining over | If all criteria are met, then CONTINUE else FAIL. |

## 7.6 Expedited Fast Phase

Table 7-13 NFC\_UD\_FAST test identifiers

| Parameter | Value |
| Test ID | NFC_UD_FAST |
| PICS | Expedited-fast |
| Applicability | Mfor User Device that supports Expedited Fast Phase |
| Interface | NFC |

## NFC\_UD\_FAST test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-14 NFC\_UD\_FAST test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |

## 7.7 Expedited Standard Phase with Sixteen Reader Group Identifiers bound to Single Access Credential

Table 7-15 NFC\_UD\_STANDARD\_SIXTEEN\_GROUPPIDENTIFIER\_ONE\_AC test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STANDARD_SIXTEEN_GROUPPIDENTIFIER_ONE_AC |
| PICS | Allow at least 16 reader_group_identifier per Access Credential |
| Applicability | Mfor User Device |
| Interface | NFC |

Table 7-16 NFC\_UD\_STANDARD\_SIXTEEN\_GROUPPIDENTIFIER\_ONE\_AC test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK(i), reader_group_identifier(i), where i = 1, 2, 3, …16. |
| TH (Reader) | Access Credential long term public key |

Table 7-17 NFC\_UD\_STANDARD\_SIXTEEN\_GROUPPIDENTIFIER\_ONE\_AC test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |

## 7.8 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with Chaining and incorrect Reader Cert signature

Table 7-18 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_SIGNATURE test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCORRECT_SIGN ATURE |
| PICS | Verification of reader_Cert with the CA Public Key |
| Applicabilit y | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_SIGNATURE test preconditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

Table 7-19 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_SIGNATURE test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Send LOAD_CERT command with fragmented reader_cert with chaining | | |
| 4 | | Send LOAD_CERT response | Verify the following: 1. SW = 9000h. 2. Response data field is empty. If all criteria are met, then CONTINUE else FAIL. |

## 7.9 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with Chaining and incorrect Reader Cert format

Table 7-20 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_FORMAT test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCORRECT_FOR MAT |
| PICS | Verification of reader_Cert with the CA Public Key |
| Applicabilit y | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_FORMAT test preconditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

Table 7-21 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_FORMAT test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Send LOAD_CERT command with wrong value/length | | |
| 4 | | Send LOAD_CERT response | Verify the following: 1. SW != 9000h. 2. Response data field is empty. If all criteria are met, then CONTINUE else FAIL. |

## 7.10 Step-Up Phase with Access Document

## Table 7-22 NFC\_UD\_STEPUP\_AD test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STEPUP_AD |
| PICS | Step-Up PhaseAND Access Document storage and retrieval |
| Applicability | Mfor User Device |
| Interface | NFC |

Table 7-23 NFC\_UD\_STEPUP\_AD test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK, reader_group_identifier, Access Document |
| TH (Reader) | Access Credential long term public key, IssuerKey_PubK |

Table 7-24 NFC\_UD\_STEPUP\_AD test steps

| Steps | TH (Reader) | Verification at TH |
| 1 | Execute SELECT routine ( Table 5-1). Set AID = A000000909ACCE5501. | If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 6 | | Send Access Document in DeviceResponse inside ENVELOPE command response | Verify the following: Access Document is sent in ENVELOPE command response. If all criteria are met, then CONTINUE else FAIL. |

## 7.11 Step-Up Phase with Revocation Document

Table 7-25 NFC\_UD\_STEPUP\_RD test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STEPUP_RD |
| PICS | Step-Up Phase AND Revocation Document storage and retrieval |
| Applicability | Mfor User Device |
| Interface | NFC |

Table 7-26 NFC\_UD\_STEPUP\_RD test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK, reader_group_identifier, Revocation Document |
| TH (Reader) | Access Credential long term public key, IssuerKey_PubK |

Table 7-27 NFC\_UD\_STEPUP\_RD test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | | Send Revocation Document in DeviceResponse inside ENVELOPE command response | Verify the following: Revocation Document is sent in ENVELOPE command response. If all criteria are met, then CONTINUE else FAIL. |
| 7 | one or more GET RESPONSE command and GET RESPONSE command response can be exchanged. | one or more GET RESPONSE command and GET RESPONSE command response can be exchanged. | |

## 7.12 Step-Up Phase with Access Document and Revocation Document

Table 7-28 NFC\_UD\_STEPUP\_AD\_RD test identifiers

| Parameter | Value |
| Test ID | NFC_UD_STEPUP_AD_RD |
| PICS | Step-Up PhaseAND Revocation Document storage and retrieval AND Revocation Document storage and retrieval |
| Applicability | Mfor User Device |
| Interface | NFC |

Table 7-29 NFC\_UD\_STEPUP\_AD\_RD test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK, reader_group_identifier, Access Document, Revocation Document |
| TH (Reader) | Access Credential long term public key, IssuerKey_PubK |

Table 7-30 NFC\_UD\_STEPUP\_AD\_RD test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Request Access Document and Revocation Document in a single DeviceRequest inside ENVELOPE command. | | |
| 3 | | Send Access Document and Revocation Document in DeviceResponse inside ENVELOPE command response | Verify the following: Access Document and Revocation Document is sent in ENVELOPE command response If all criteria are met, then CONTINUE else FAIL. |

## 7.13 SELECT Response with User Device Descriptor Tag (provisional)

Table 7-31 NFC\_UD\_SELECT\_RESPONSE\_UD\_DESCRIPTOR\_TAG test identifiers

| Parameter | Value |
| Test ID | NFC_UD_SELECT_RESPONSE_UD_DESCRIPTOR_TAG |
| PICS | User Device Descriptor Tag |
| Applicability | Mfor User Device that supports sending User Device Descriptor Tag |
| Interface | NFC |

NFC\_UD\_SELECT\_RESPONSE\_UD\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-32 NFC\_UD\_SELECT\_RESPONSE\_UD\_DESCRIPTOR\_TAG test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute SELECT routine ( Table 5-1). Set AID = A000000909ACCE5501 | | Verify the following in addition to all verification in SELECT routine: 1. User Device Descriptor TLV structure is present in SELECT response. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | | | 2. User Device Descriptor TLV structure matches technical specification. If all criteria are met, then CONTINUE else FAIL. |

## 7.14 AUTH0 Response with Chaining

Table 7-33 NFC\_UD\_AUTH0\_RESPONSE\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_UD_AUTH0_RESPONSE_CHAINING |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_AUTH0\_RESPONSE\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-34 NFC\_UD\_AUTH0\_RESPONSE\_CHAINING test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | | [Optional] Send one or more GET RESPONSE | Verify AUTH0 response is chained. If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 5 | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is | If all criteria are met, then CONTINUE else FAIL. |
| 6 | Execute EXCHANGE indicating transaction success routine ( Table 5-5). | Execute EXCHANGE indicating transaction success routine ( Table 5-5). | If all criteria are met, then PASS else FAIL. |

## 7.15 AUTH0 with Unknown Reader Identifier

## Table 7-35 NFC\_UD\_NEG\_AUTH0\_UNKNOWN\_READER\_ID test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH0_UNKNOWN_READER_ID |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

## Table 7-36 NFC\_UD\_NEG\_AUTH0\_UNKNOWN\_READER\_ID test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK |
| TH (Reader) | Access Credential long term public key |

Table 7-37 NFC\_UD\_NEG\_AUTH0\_UNKNOWN\_READER\_ID test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h and reader_identifier to a random value | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h and reader_identifier to a random value | If all criteria are met, then CONTINUE else FAIL. |
| 3 | Execute AUTH1 with SW != 9000h routine ( Table 5-4). Reader_cert is not present in AUTH1 command. | Execute AUTH1 with SW != 9000h routine ( Table 5-4). Reader_cert is not present in AUTH1 command. | If all criteria are met, then CONTINUE else FAIL. |

## 7.16 AUTH0 with unsupported Protocol Version

Table 7-38 NFC\_UD\_NEG\_AUTH0\_UNSUPPORTED\_PROTOCOL\_VERSION test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH0_UNSUPPORTED_PROTOCOL_VERSION |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH0\_UNSUPPORTED\_PROTOCOL\_VERSION test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-39 NFC\_UD\_NEG\_AUTH0\_UNSUPPORTED\_PROTOCOL\_VERSION test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Send AUTH0 command with unsupported expedited_phase_protocol_version and command_parameters = 0h | | |
| 4 | | send AUTH0 response | Verify the following: 1. SW != 9000h. 2. Response data field is empty. If all criteria are met, then CONTINUE else FAIL. |

## 7.17 AUTH0 with Extra Unknown TLV

Table 7-40 NFC\_UD\_NEG\_AUTH0\_EXTRA\_TAG test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH0_EXTRA_TAG |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH0\_EXTRA\_TAG test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-41 NFC\_UD\_NEG\_AUTH0\_EXTRA\_TAG test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h and add extra unknown tag in TLV. Extra tag can be randomly injected at any location in the command payload. | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h and add extra unknown tag in TLV. Extra tag can be randomly injected at any location in the command payload. | If all criteria are met, then CONTINUE else FAIL. |

## 7.18 AUTH0 with Wrong Value

Table 7-42 NFC\_UD\_NEG\_AUTH0\_WRONG\_VALUE test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH0_WRONG_VALUE |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH0\_WRONG\_VALUE test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-43 NFC\_UD\_NEG\_AUTH0\_WRONG\_VALUE test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Send AUTH0 command with command_parameters = 0h and wrong value/length for tag. | | |
| 3 | | send AUTH0 response | Verify the following: 1. SW != 9000h. 2. Response data field is empty. If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Execute CONTROL FLOW indicating transaction failure routine (Table 5-7). | Execute CONTROL FLOW indicating transaction failure routine (Table 5-7). | If all criteria are met, then PASS else FAIL. |

## 7.19 AUTH0 with Wrong P1 and P2

Table 7-44 NFC\_UD\_NEG\_AUTH0\_WRONG\_P1P2 test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH0_WRONG_P1P2 |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH0\_WRONG\_P1P2 test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-45 NFC\_UD\_NEG\_AUTH0\_WRONG\_P1P2 test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Send AUTH0 command with command_parameters = 0h and wrong value of P1 and P2. | | |
| 3 | | send AUTH0 response | Verify the following: 1. SW != 9000h. 2. Response data field is empty. If all criteria are met, then CONTINUE else FAIL. |

## 7.20 AUTH0 with Chaining Not Completed

Table 7-46 NFC\_UD\_NEG\_AUTH0\_CHAINING\_NOT\_COMPLETED test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH0_CHAINING_NOT_COMPLETED |
| PICS | Expedited-Standard Phase |

Applicability M for User Device

NEG\_AUTH0\_CHAINING\_NOT\_COMPLETED test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-47 NFC\_UD\_NEG\_AUTH0\_CHAINING\_NOT\_COMPLETED test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Send AUTH0 command with command_parameters = 0h and with single auth0_command_vendor_extension with command chaining and skipping sending the last APDU in the chain. | | |
| 3 | | send AUTH0 response | |
| 4 | Execute AUTH1 with SW != 9000h routine ( Table 5-4) | Execute AUTH1 with SW != 9000h routine ( Table 5-4) | If all criteria are met, then CONTINUE else FAIL. |

## 7.21 AUTH0 with Different Cryptogram in Consecutive Expedited Fast Phase

Table 7-48 NFC\_UD\_NEG\_AUTH0\_DIFFERENT\_CRYPTOGRAM\_CONSECUTIVE\_FAST test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONSECUTIVE_FAST |
| PICS | Expedited-Fast Phase AND Cryptogram generation and validation |
| Applicability | Mfor User Device that support Expedited-Fast |
| Interface | NFC |

User Device and Reader do not have any information about each other as a pre-condition to this test.

Table 7-49 NFC\_UD\_NEG\_AUTH0\_DIFFERENT\_CRYPTOGRAM\_CONSECUTIVE\_FAST test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute SELECT routine ( Table 5-1). Set AID = A000000909ACCE5501. | Execute SELECT routine ( Table 5-1). Set AID = A000000909ACCE5501. | If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | | | Verify the following in AUTH0 command response: 1. Value of Tag 0x86h is different between step 2 and step 5 2. Value of Tag 0x9Dh is different between step 2 and step 5 If all criteria are met, then PASS else FAIL. |

## 7.22 AUTH1 with Wrong Reader Signature

Table 7-50 NFC\_UD\_NEG\_AUTH1\_WRONG\_READER\_SIGNATURE test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH1_WRONG_READER_SIGNATURE |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH1\_WRONG\_READER\_SIGNATURE test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-51 NFC\_UD\_NEG\_AUTH1\_WRONG\_READER\_SIGNATURE test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Execute AUTH1 with SW != 9000h routine ( Table 5-4) and send wrong reader signature in AUTH1 command. | Execute AUTH1 with SW != 9000h routine ( Table 5-4) and send wrong reader signature in AUTH1 command. | If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Execute CONTROL FLOW indicating transaction failure routine (Table 5-7). | Execute CONTROL FLOW indicating transaction failure routine (Table 5-7). | If all criteria are met, then PASS else FAIL. |

## 7.23 AUTH1 with Extra Tag

Table 7-52 NFC\_UD\_NEG\_AUTH1\_EXTRA\_TAG test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH1_EXTRA_TAG |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH1\_EXTRA\_TAG test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-53 NFC\_UD\_NEG\_AUTH1\_EXTRA\_TAG test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Add extra unknown tag in TLV. Extra tag can be randomly injected at any location in the command payload. | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Add extra unknown tag in TLV. Extra tag can be randomly injected at any location in the command payload. | If all criteria are met, then CONTINUE else FAIL. |

## 7.24 AUTH1 with Wrong P1 and P2

Table 7-54 NFC\_UD\_NEG\_AUTH1\_WRONG\_P1P2 test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH1_WRONG_P1P2 |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |

| Interface | NFC |

NFC\_UD\_NEG\_AUTH1\_WRONG\_P1P2 test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-55 NFC\_UD\_NEG\_AUTH1\_WRONG\_P1P2 test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Execute AUTH1 with SW != 9000h routine ( Table 5-4). Add wrong value of P1 and P2 in AUTH1 command. | Execute AUTH1 with SW != 9000h routine ( Table 5-4). Add wrong value of P1 and P2 in AUTH1 command. | If all criteria are met, then CONTINUE else FAIL. |

## 7.25 AUTH1 with Wrong Values

Table 7-56 NFC\_UD\_NEG\_AUTH1\_WRONG\_VALUES test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH1_WRONG_VALUES |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH1\_WRONG\_VALUES test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-57 NFC\_UD\_NEG\_AUTH1\_WRONG\_VALUES test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute SELECT routine ( Table 5-1). Set AID = A000000909ACCE5501. | Execute SELECT routine ( Table 5-1). Set AID = A000000909ACCE5501. | If all criteria are met, then CONTINUE else FAIL. |
| 2 | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h. | Execute AUTH0 routine ( Table 5-2). Set command_parameters = 0h. | If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Execute AUTH1 with SW != 9000h routine ( Table 5-4) with wrong value/length for tags in AUTH1 command. | Execute AUTH1 with SW != 9000h routine ( Table 5-4) with wrong value/length for tags in AUTH1 command. | If all criteria are met, then CONTINUE else FAIL. |

## 7.26 AUTH1 with Incomplete Chaining

Table 7-58 NFC\_UD\_NEG\_AUTH1\_CHAINING\_NOT\_COMPLTED test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_AUTH1_CHAINING_NOT_COMPLTED |
| PICS | Command Chaining |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_AUTH1\_CHAINING\_NOT\_COMPLTED test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

Table 7-59 NFC\_UD\_NEG\_AUTH1\_CHAINING\_NOT\_COMPLTED test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Send AUTH1 command with chaining and skipping sending the last APDU in the chain. | | |
| 4 | | send AUTH1 response | Abort at this step, if AUTH1 response not sent. Otherwise, proceed to next step. |
| 6 | | Select Response | Verify the following:SW ! = 9000h. If all criteria are met, then CONTINUE else FAIL. |

## 7.27 EXCHANGE with Mailbox Read Request

## Table 7-60 NFC\_UD\_EXCHANGE\_READ\_REQUEST test identifiers

| Parameter | Value |
| Test ID | NFC_UD_EXCHANGE_READ_REQUEST |
| PICS | Mailbox - Read |
| Applicability | Mfor User Device, if bit 4 in signaling_bitmap in AUTH1command response is set to 1 |
| Interface | NFC |

Table 7-61 NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK, reader_group_identifier, non-zero mailbox populated with random data |
| TH (Reader) | Access Credential long term public key |

Table 7-62 NFC\_UD\_EXCHANGE\_READ\_REQUEST test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send EXCHANGE command multiple times with multiple READ requests from mailbox | | |
| 5 | | Send Exchange command response | Verify the following: Read requests return random data in mailbox. B1 and B2 are both 00h. If all criteria are met, then CONTINUE else FAIL. |

## 7.28 EXCHANGE with Mailbox Write Request

Table 7-63 NFC\_UD\_EXCHANGE\_WRITE\_REQUEST test identifiers

| Parameter | Value |

| Test ID | NFC_UD_EXCHANGE_WRITE_REQUEST |
| PICS | Mailbox - Write |
| Applicability | Mfor User Device, if bit 5 in signaling_bitmap in AUTH1command response is set to 1 |
| Interface | NFC |

## NFC\_UD\_EXCHANGE\_WRITE\_REQUEST test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

Table 7-64 NFC\_UD\_EXCHANGE\_WRITE\_REQUEST test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send EXCHANGE command multiple times with multiple WRITE requests to mailbox (atomic session = TRUE). | | |
| 6 | Send EXCHANGE command with atomic session = FALSE and random requests | | |
| 7 | | Send EXCHANGE command response | Verify the following: If Read Request is present, non-updated data is returned. B1 and B2 are both 00h. If all criteria are met, then CONTINUE else FAIL. |
| 8 | Send EXCHANGE command to read data written to the mailbox | | |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | | | If all criteria are met, then CONTINUE else FAIL. |
| 10 | Execute EXCHANGE indicating transaction success routine ( Table 5-5). | Execute EXCHANGE indicating transaction success routine ( Table 5-5). | If all criteria are met, then PASS else FAIL. |

## 7.29 EXCHANGE with Set Request

Table 7-65 NFC\_UD\_EXCHANGE\_SET\_REQUEST test identifiers

| Parameter | Value |
| Test ID | NFC_UD_EXCHANGE_SET_REQUEST |
| PICS | Mailbox |
| Applicability | Mfor User Device, if bit 5 in signaling_bitmap in AUTH1command response is set to 1 |
| Interface | NFC |

NFC\_UD\_EXCHANGE\_SET\_REQUEST test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

Table 7-66 NFC\_UD\_EXCHANGE\_SET\_REQUEST test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send EXCHANGE command multiple times with multiple SET requests to mailbox (atomic session = TRUE). | | |
| 5 | | Send Exchange command response | Verify the following: Write requests do not fail. B1 and B2 are both 00h. If all criteria are met, then CONTINUE else FAIL. |
| 6 | Send EXCHANGE command with atomic session = FALSE and random requests | | |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 8 | Send EXCHANGE command to read data written to the mailbox | | |
| 9 | | Send EXCHANGE command response | Verify the following: Read request should return final data in the mailbox after closing of atomic session. B1 and B2 are both 00h. If all criteria are met, then CONTINUE else FAIL. |

## 7.30 EXCHANGE with Chaining

Table 7-67 NFC\_UD\_EXCHANGE\_WITH\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_UD_EXCHANGE_WITH_CHAINING |
| PICS | EXCHANGE command |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_EXCHANGE\_WITH\_CHAINING test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

Table 7-68 NFC\_UD\_EXCHANGE\_WITH\_CHAINING test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is not present in AUTH1 command. | Execute AUTH1 with SW = 9000h routine ( Table 5-3). Reader_cert is not present in AUTH1 command. | If all criteria are met, then CONTINUE else FAIL. |
| 7 | Send EXCHANGE command multiple times with chaining with Read/Write | | |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | requests and le!=0 (atomic session = TRUE) | | |
| 8 | | [Optional] Send Exchange command response | Send GET RESPONSE multiple times to retrieve complete response |

## 7.31 EXCHANGE with Extended Length

Table 7-69 NFC\_UD\_EXCHANGE\_WITH\_EXTENDED\_LENGTH test identifiers

| Parameter | Value |
| Test ID | NFC_UD_EXCHANGE_WITH_EXTENDED_LENGTH |
| PICS | EXCHANGE command AND Extended Length |
| Applicability | Mfor User Device that supports Extended Length |
| Interface | NFC |

NFC\_UD\_EXCHANGE\_WITH\_EXTENDED\_LENGTH test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

Table 7-70 NFC\_UD\_EXCHANGE\_WITH\_EXTENDED\_LENGTH test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send EXCHANGE command with extended length APDU and large Read request | | |
| 5 | | Send Exchange command response | Verify the following: Reading Mailbox should not fail. B1 and B2 are both 00h. If all criteria are met, then CONTINUE else FAIL. |

## 7.32 EXCHANGE with Extra Tag

Table 7-71 NFC\_UD\_NEG\_EXCHANGE\_WITH\_EXTRA\_TAG test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_EXCHANGE_WITH_EXTRA_TAG |
| PICS | EXCHANGE command |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_EXCHANGE\_WITH\_EXTRA\_TAG test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

Table 7-72 NFC\_UD\_NEG\_EXCHANGE\_WITH\_EXTRA\_TAG test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send EXCHANGE command with extra tag in encrypted payload | | |
| 5 | | Send Exchange command response | Verify the following: All requests should pass. B1 and B2 are both 00h. If all criteria are met, then CONTINUE else FAIL. |

## 7.33 EXCHANGE with Mailbox Out of Bounds

Table 7-73 NFC\_UD\_NEG\_EXCHANGE\_MAILBOX\_OUT\_OF\_BOUNDS test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_EXCHANGE_MAILBOX_OUT_OF_BOUNDS |
| PICS | Mailbox |
| Applicability | Mfor User Device |

Interface NFC

NFC\_UD\_NEG\_EXCHANGE\_MAILBOX\_OUT\_OF\_BOUNDS test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

Table 7-74 NFC\_UD\_NEG\_EXCHANGE\_MAILBOX\_OUT\_OF\_BOUNDS test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send EXCHANGE command with mailbox request with offset + length > mailbox size | | |
| 5 | | Send Exchange command response | Verify the following: Exchange command responseSW= 9000h and response payload has 0x0002&#124;&#124;B1&#124;&#124;B2, where B1 and B2 are implementation specific. If all criteria are met, then CONTINUE else FAIL. |

## 7.34 EXCHANGE with Wrong Length

Table 7-75 NFC\_UD\_NEG\_EXCHANGE\_WITH\_WRONG\_LENGTH test identifiers

| Parameter | Value |
| Test ID | NFC_UD_NEG_EXCHANGE_WITH_WRONG_LENGTH |
| PICS | EXCHANGE command |
| Applicability | Mfor User Device |
| Interface | NFC |

NFC\_UD\_NEG\_EXCHANGE\_WITH\_WRONG\_LENGTH test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

Table 7-76 NFC\_UD\_NEG\_EXCHANGE\_WITH\_WRONG\_LENGTH test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send EXCHANGE command with wrong length/value for tag | | |
| 5 | | Send Exchange command response | Verify the following: Exchange command responseSW= 9000h and response payload has 0x0002&#124;&#124;B1&#124;&#124;B2, where B1 and B2 are implementation specific. If all criteria are met, then CONTINUE else FAIL. |

## 7.35 BLE+UWB Flow with Expedited Standard Phase

Table 7-77 BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_EXPEDITED_STANDARD_PHASE |
| PICS | BLE + UWBFlow AND UWB ranging AND UWB Time Synchronization AND Expedited-Standard Phase |
| Applicability | Mfor User Device that supports BLE + UWBFlow |
| Interface | BLE |

Table 7-78 BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK, reader_group_identifier, GRK |
| TH (Reader) | Access Credential long term public key, GRK |
| NOTE 1: The TH (Reader) and the DUT (User Device) are in very close proximity (e.g., 1m and line-of- sight). NOTE 2: TH is in secured state as a pre-condition. | NOTE 1: The TH (Reader) and the DUT (User Device) are in very close proximity (e.g., 1m and line-of- sight). NOTE 2: TH is in secured state as a pre-condition. |

Table 7-79 BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |

## 7.36 BLE+UWB Flow with Expedited Fast Phase

Table 7-80 BLEUWB\_UD\_EXPEDITED\_FAST\_PHASE test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_EXPEDITED_FAST_PHASE |
| PICS | BLE +UWBFlow AND UWBranging AND UWBTime Synchronization AND Expedited-Fast Phase |
| Applicability | Mfor User Device that supports BLE + UWB Flow and Expedited-Fast phase |
| Interface | BLE |

## BLEUWB\_UD\_EXPEDITED\_FAST\_PHASE test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

## Table 7-81 BLEUWB\_UD\_EXPEDITED\_FAST\_PHASE test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | BLE teardown | BLE teardown | |
| 3 | Send Bluetooth LE advertisement | | |
| 4 | | Establish L2CAP connection | |
| 6 | Send AUTH0 command command_parameters = 1h authentication_policy = 01h (User Device) | | |
| 9 | | Send EXCHANGE response | |
| 10 | Send Reader Status Access Protocol Completed Message ID carrying Reader Information Attribute ID | | Verify the following: Ensure reader status is secured. Format of message matches technical specification. If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 15 | Reader Status Changed Message ID carrying State Attribute ID is sent. | | Verify the following: State Attribute ID has second byte [B7:B0] set to 0x01 or 0x02 or 0x81 or 0x82. If all criteria are met, then PASS else FAIL. |

## 7.37 BLE+UWB Flow with Step-Up Phase

## Table 7-82 BLEUWB\_UD\_STEPUP\_PHASE test steps

| Parameter | Value |
| Test ID | BLEUWB_UD_STEPUP_PHASE |
| PICS | BLE + UWB Flow AND UWBranging AND UWBTime Synchronization AND Step-Up Phase |
| Applicability | Mfor User Device that supports BLE + UWB Flow |
| Interface | BLE |

## Table 7-83 BLEUWB\_UD\_STEPUP\_PHASE test pre-conditions

| Provision onto | Remarks |
| DUT (User Device) | reader_PubK, reader_group_identifier, GRK, Access Document |
| TH (Reader) | Access Credential long term public key, GRK, IssuerKey_PubK |

NOTE 1: The TH (Reader) and the DUT (User Device) are in very close proximity (e.g., 1 m and line-ofsight).

NOTE 2: TH is in secured state as a pre-condition.

Table 7-84 BLEUWB\_UD\_STEPUP\_PHASE test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send Bluetooth LE advertisement | | |
| 2 | | Establish L2CAP connection | |
| 3 | | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | Verify the following: Format of Initiate Access Protocol Message ID matches specification. If all criteria are met, then CONTINUE else FAIL. |
| 4 | Send AUTH0 command command_parameters = 0h authentication_policy = 01h (User Device) | | |
| 6 | Send AUTH1 command and reader_cert is absent | | |
| 9 | | Send EXCHANGE response | |
| 10 | Request Access Document using DeviceRequest inside ENVELOPE command | | |
| 11 | | Send Access Document in DeviceResponse inside ENVELOPE command response | Verify the following: Access Document is sent in ENVELOPE command response. If all criteria are met, then CONTINUE else FAIL |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 12 | One or more GET RESPONSE command and GET RESPONSE command response can be | One or more GET RESPONSE command and GET RESPONSE command response can be | |
| 14 | | Send Time Sync Message ID | Verify the following: 1. Confirm Time Sync Message ID is received by TH 2. Format of message matches technical specification. If all criteria are met, then CONTINUE else FAIL. |

## 7.38 BLE+UWB Flow with UWB Ranging Suspend

Table 7-85 BLEUWB\_UD\_RANGING\_SUSPEND test identifiers Interface BLE

| Parameter | Value |
| Test ID | BLEUWB_UD_RANGING_SUSPEND |
| PICS | BLE +UWBFlow AND UWBranging suspend |
| Applicability | Mfor User Device that supports BLE + UWB Flow |

BLEUWB\_UD\_RANGING\_SUSPEND test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78 with the exception: The TH (Reader) and the DUT (User Device) are in close proximity (e.g., 5 m and line-of-sight).

Table 7-86 BLEUWB\_UD\_RANGING\_SUSPEND test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 6 | Send Ranging Session Suspend Request with correct UWB Session Identifier | | |
| 7 | | Send Ranging Session Suspend Response | Verify the following 1. this message is sent. 2. format of Ranging Session Suspend Response matches technical specification. 3. No UWBpackets are received overUWB transport a short time (e.g., up to 3 seconds) after receiving Ranging Session Suspend Response. If all criteria are met, then PASS else FAIL. The status can either value 0 or 1. |

## 7.39 BLE+UWB Flow with UWB Ranging Resume

## Table 7-87 BLEUWB\_UD\_RANGING\_RESUME test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_RANGING_RESUME |
| PICS | BLE +UWBFlow AND UWBranging resume |
| Applicability | Mfor User Device that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_UD\_RANGING\_RESUME test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78 with the exception: The TH (Reader) and the DUT (User Device) are in close proximity (e.g., 5 m and line-of-sight)..

Table 7-88 BLEUWB\_UD\_RANGING\_RESUME test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 6 | Send Ranging Message ID carrying Ranging Session Suspended Attribute ID | | Verify the following: No UWB packets are received over UWB transport a short time (e.g., up to 3 seconds) after sending Ranging Message ID carrying Ranging Session Suspended Attribute ID. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 7 | 1 second after previous step, send Ranging Session Resume Request Message | | |
| 8 | | Send Ranging Session Resume Response or Ranging Message ID carrying Initiate Ranging Session Resume Later Attribute ID | Verify the following: 1. Ranging Session Resume Response or Ranging Message ID carrying Initiate Ranging Session Resume Later Attribute ID is sent. 2. Format of the message matches technical specification. If all criteria are met, then PASS else FAIL. |

## 7.40 BLE+UWB Flow with User Device Descriptor Tag (provisional)

| Parameter | Value |
| Test ID | BLEUWB_UD_UD_DESCRIPTOR_TAG |
| PICS | BLE + UWBFlow AND User Device Descriptor Tag |
| Applicability | Mfor User Device that supports BLE + UWBFlow and that supports sending User Device Descriptor Tag |
| Interface | BLE |

## BLEUWB\_UD\_UD\_DESCRIPTOR\_TAG test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-89 BLEUWB\_UD\_UD\_DESCRIPTOR\_TAG test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute BLE+UWB Aliro Access Protocol routine ( Table 5-8). | Execute BLE+UWB Aliro Access Protocol routine ( Table 5-8). | Verify the following in Initiate Access Protocol Message ID in addition to other verifications in BLE+UWB Aliro Access Protocol routine. 1. Proprietary Information Attribute ID is present. 2. The format of Proprietary Information ID matches the technical specification. 3. User Device Descriptor TLV structure is present in Proprietary Information Attribute ID. If all criteria are met, then PASS else FAIL. |

## 7.41 BLE+UWB Flow with wrong advertisement format

Table 7-90 BLEUWB\_UD\_NEG\_WRONG\_ADV test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_WRONG_ADV |
| PICS | BLE +UWBFlow |
| Applicability | Mfor User Device that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_UD\_NEG\_WRONG\_ADV test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-91 BLEUWB\_UD\_NEG\_WRONG\_ADV test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send Bluetooth LE advertisement with bits 6 and 7 in byte 7, each set to 0 for 30 seconds. | | |
| 2 | | No BLE connection initiated by the User Device. | Verify the following: DUT (User Device) does not establish BLE connection with the TH (Reader). If all criteria are met, then PASS else FAIL. |

## 7.42 BLE+UWB Flow with Failed L2CAP

Table 7-92 BLEUWB\_UD\_NEG\_FAILED\_L2CAP test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_FAILED_L2CAP |
| PICS | BLE +UWBFlow |
| Applicability | Mfor User Device that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_UD\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-93 BLEUWB\_UD\_NEG\_FAILED\_L2CAP test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | Reader sends wrong Supported Aliro BleUWB Protocol Version. | Establish L2CAP connection fails. | Verify the following: |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| | | | L2CAP establishment fails. If all criteria are met, then PASS else FAIL. |

## 7.43 BLE+UWB Flow with timeout before AUTH0

## Table 7-94 BLEUWB\_UD\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_TIMEOUT_BEFORE_AUTH0 |
| PICS | BLE + UWBFlow |
| Applicability | Mfor User Device that supports BLE + UWBFlow |
| Interface | BLE |

BLEUWB\_UD\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-95 BLEUWB\_UD\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Send Bluetooth LE advertisement. | | |
| 3 | | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501. | Verify the following: Format of Initiate Access Protocol Message ID matches specification. If all criteria are met, then CONTINUE else FAIL. |
| 4 | Do not send AUTH0 command. | | |

## 7.44 BLE+UWB Flow with Timeout Extension

Table 7-96 BLEUWB\_UD\_TIMEOUT\_EXTENSION test identifiers BLEUWB\_UD\_TIMEOUT\_EXTENSION test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

| Parameter | Value |

| Test ID | BLEUWB_UD_TIMEOUT_EXTENSION |
| PICS | BLE +UWBFlow |
| Applicability | Mfor User Device that supports BLE + UWB Flow |
| Interface | BLE |

Table 7-97 BLEUWB\_UD\_TIMEOUT\_EXTENSION test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 4 | Send Event Message ID carrying Busy Attribute ID at 1 second after receiving Initiate Access Protocol Message ID. | | |
| 8 | | Send EXCHANGE response | |
| 9 | Send Reader Status Access Protocol Completed Message ID carrying Reader Information Attribute ID | | Verify the following: Ensure reader status is secured or unsecured. Format of message matches technical specification. If all criteria are met, then PASS else FAIL. |

## 7.45 BLE+UWB Flow with URSK Not Found

Table 7-98 BLEUWB\_UD\_NEG\_URSK\_NOT\_FOUND test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_URSK_NOT_FOUND |
| PICS | BLE + UWBFlow |
| Applicability | Mfor User Device that supports BLE + UWBFlow |
| Interface | BLE |

BLEUWB\_UD\_NEG\_URSK\_NOT\_FOUND test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-99 BLEUWB\_UD\_NEG\_URSK\_NOT\_FOUND test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | | Send Event Message ID carrying General Error Attribute ID with URSK unavailable | Verify the following: Format of this message matches the specification. If all criteria are met, then PASS else FAIL. |
| 3 | BLE teardown | | |

## 7.46 BLE+UWB Flow with M1 Message Mismatch Parameter

Table 7-100 BLEUWB\_UD\_NEG\_M1\_MISMATCH\_PARAMETER test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_M1_MISMATCH_PARAMETER |
| PICS | BLE + UWBFlow |
| Applicability | Mfor User Device that supports BLE + UWBFlow |
| Interface | BLE |

BLEUWB\_UD\_NEG\_M1\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-101 BLEUWB\_UD\_NEG\_M1\_MISMATCH\_PARAMETER test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute BLE+UWB Aliro Access Protocol routine ( Table 5-8). | Execute BLE+UWB Aliro Access Protocol routine ( Table 5-8). | If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | | Send Time Sync Message ID | Verify the following: 1. Confirm Time Sync Message ID is received by TH 2. Format of message matches technical specification. If all criteria are met, then CONTINUE else FAIL. |
| 5 | Send Ranging Session Setup M1 Message ID without UWB Config ID | | |
| 7 | BLE teardown | | |

## 7.47 BLE+UWB Flow with M3 Message Mismatch Parameter

Table 7-102 BLEUWB\_UD\_NEG\_M3\_MISMATCH\_PARAMETER test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_M3_MISMATCH_PARAMETER |
| PICS | BLE +UWBFlow |
| Applicability | Mfor User Device that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_UD\_NEG\_M3\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-103 BLEUWB\_UD\_NEG\_M3\_MISMATCH\_PARAMETER test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 2 | | Send Time Sync Message ID | Verify the following: 1. Confirm Time Sync Message ID is received by TH 2. Format of message matches technical specification. If all criteria are met, then CONTINUE else FAIL. |
| 4 | Send Ranging Session Setup M1 Message ID | | |
| 5 | | Send Ranging Session Setup M2 Message ID | |
| 6 | Send Ranging Session Setup M3 Message ID without RAN Multiplier | | |
| 8 | BLE teardown | | |

## 7.48 BLE+UWB Flow with Suspend Request Mismatch Parameter

Table 7-104 BLEUWB\_UD\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test identifiers BLEUWB\_UD\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_SUSPEND_MISMATCH_PARAMETER |
| PICS | BLE + UWBFlow AND UWB Ranging Suspend |
| Applicability | Mfor User Device that supports BLE + UWBFlow |
| Interface | BLE |

Table 7-105 BLEUWB\_UD\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute BLEUWB_UD_RANGING_SUSPEND test steps ( Table 7-86). Send Ranging Session Suspend Request with an incorrect UWBSession Identifier | Send Event Message ID carrying General Error Attribute ID indicating Wrong Parameters | Verify the following: Format of Event Message ID. General Error Attribute ID indicates Wrong Parameters. If all criteria are met, then PASS else FAIL. |
| 2 | BLE teardown | | |

## 7.49 BLE+UWB Flow with Resume Request Mismatch Parameter

Table 7-106 BLEUWB\_UD\_NEG\_RESUME\_MISMATCH\_PARAMETER test identifiers

| Parameter | Value |
| Test ID | BLEUWB_UD_NEG_RESUME_MISMATCH_PARAMETER |
| PICS | BLE +UWBFlow AND UWBRanging Resume |
| Applicability | Mfor User Device that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_UD\_NEG\_RESUME\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-107 BLEUWB\_UD\_NEG\_RESUME\_MISMATCH\_PARAMETER test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute BLEUWB_UD_RANGING_RESUME test steps (Table 7-88). Send Ranging Session Resume Request with an incorrect UWB Session Identifier. | Send Event Message ID carrying General Error Attribute ID indicating Wrong Parameters. | Verify the following: Format of Event Message ID. General Error Attribute ID indicates Wrong Parameters. If all criteria are met, then PASS else FAIL. |
| 2 | BLE teardown | | |

## 7.50 BLE-Only Flow with Expedited Standard Phase (provisional)

Table 7-108 BLERKE\_UD\_EXPEDITED\_STANDARD\_PHASE test identifiers

| Parameter | Value |
| Test ID | BLERKE_UD_EXPEDITED_STANDARD_PHASE |
| PICS | BLE-Only Flow AND Explicit Reader Selection |
| Applicability | Mfor User Device that supports BLE-Only Flow |
| Interface | BLE |

BLERKE\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-109 BLERKE\_UD\_EXPEDITED\_STANDARD\_PHASE test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 3 | Send Reader Status Changed Message ID carrying State Attribute ID. | | Verify the following: Format of Reader Status Changed Message ID carrying State Attribute ID matches technical specification. If all criteria are met, then PASS else FAIL. |

## 7.51 BLE-Only Flow with User Device Descriptor Tag (provisional)

Table 7-110 BLERKE\_UD\_UD\_DESCRIPTOR\_TAG test identifiers

| Parameter | Value |
| Test ID | BLERKE_UD_UD_DESCRIPTOR_TAG |
| PICS | BLE-Only Flow |
| Applicability | Mfor User Device that supports BLE-Only Flow and that supports sending User Device Descriptor Tag |
| Interface | BLE |

BLERKE\_UD\_UD\_DESCRIPTOR\_TAG test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

Table 7-111 BLERKE\_UD\_UD\_DESCRIPTOR\_TAG test steps

| Steps | TH (Reader) | DUT (User Device) | Verification at TH |
| 1 | Execute BLE-Only Aliro Access Protocol routine ( Table 5-10). | Execute BLE-Only Aliro Access Protocol routine ( Table 5-10). | Verify the following in Initiate Access Protocol RKE Message ID, in addition to verifying BLE-Only Aliro Access Protocol routine: 1. Proprietary Information Attribute ID is present 2. The format of Proprietary Information ID is matching technical specification 3. User Device Descriptor TLV structure is present in Proprietary Information Attribute ID If all criteria are met, then PASS else FAIL. |

## 7.52 BLE-Only Flow with Failed L2CAP (provisional)

Table 7-112 BLERKE\_UD\_NEG\_FAILED\_L2CAP test identifiers

| Parameter | Value |
| Test ID | BLERKE_UD_NEG_FAILED_L2CAP |
| PICS | BLE-Only Flow |
| Applicability | Mfor User Device that supports BLE-Only Flow |
| Interface | BLE |

BLERKE\_UD\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

BLERKE\_UD\_NEG\_FAILED\_L2CAP test steps are identical to

BLEUWB\_UD\_NEG\_FAILED\_L2CAP test steps in Table 7-93.

## 8 Reader Under Test Conformance Tests

## 8.1 Expedited Standard Phase without Reader Certificate

Table 8-1 NFC\_RDR\_STANDARD\_NO\_CERT test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STANDARD_NO_CERT |
| PICS | Expedited-Standard Phase AND Reader signature generation and validation using reader_PubK AND Device signature generation and validation AND AUTH1 command parameter |
| Applicability | Mfor Reader |
| Interface | NFC |

Table 8-2 NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | Access Credential long term public key |
| TH (User Device) | reader_PubK, reader_group_identifier |

Table 8-3 NFC\_RDR\_STANDARD\_NO\_CERT test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501 | If all criteria are met, then CONTINUE else FAIL. |
| 4 | Execute EXCHANGE indicating transaction success routine ( Table 6-4). | Execute EXCHANGE indicating transaction success routine ( Table 6-4). | If all criteria are met, then PASS else FAIL. |

## 8.2 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with APDU Chaining

Table 8-4 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING |
| PICS | Expedited-Standard Phase AND |

| | Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Device signature generation and validation AND Presentation and validation of the reader_Cert in LOAD_CERT command AND Command chaining AND AUTH1 command parameter |
| Applicability | Mfor Reader |
| Interface | NFC |

Table 8-5 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | Access Credential long term public key |
| TH (User Device) | Reader System Issuer CA public key, reader_group_identifier |

Table 8-6 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | | Send LOAD_CERT command with fragmented reader_cert with chaining | Verify the following: reader_cert with chaining sent. If all criteria are met, then CONTINUE else FAIL. |
| 4 | Send LOAD_CERT Response | | |

## 8.3 Expedited Standard Phase with Reader Cert in LOAD\_CERT without APDU Chaining

Table 8-7 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING |
| PICS | Expedited-Standard Phase AND |

| | Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Device signature generation and validation AND Presentation and validation of the reader_Cert in LOAD_CERT command AND Extended length AND AUTH1 command parameter |
| Applicability | Mfor Reader, if it supports Extended length APDUs |
| Interface | NFC |

NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test pre-conditions are identical to NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

Table 8-8 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | | Send LOAD_CERT command with reader_cert and no chaining | Verify the following: Reader_cert sent without chaining. If all criteria are met, then CONTINUE else FAIL. |
| 4 | Send LOAD_CERT Response | | |

## 8.4 Expedited Standard Phase with Reader Cert in AUTH1 with APDU Chaining

Table 8-9 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STANDARD_CERT_IN_AUTH1_WITH_CHAINING |
| PICS | Expedited-Standard Phase AND Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Device signature generation and validation AND Presentation and validation of the reader_Cert in AUTH1 command AND Command chaining AND |

| | AUTH1 command parameter |
| Applicability | Mfor Reader |
| Interface | NFC |

NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test pre-conditions are identical to NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

Table 8-10 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | Execute AUTH1 routine ( Table 6-3). fragmented reader_cert with chaining over multiple APDUs. | Execute AUTH1 routine ( Table 6-3). fragmented reader_cert with chaining over multiple APDUs. | Verify AUTH1 routine criteria and the following: Reader_cert chaining. If all criteria are met, then CONTINUE else FAIL. |

## 8.5 Expedited Standard Phase with Reader Cert in AUTH1 without Chaining

Table 8-11 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test steps

| Parameter | Value |
| Test ID | NFC_RDR_STANDARD_CERT_IN_AUTH1_NO_CHAINING |
| PICS | Expedited-Standard Phase AND Reader signature generation and validation using intermediate_reader_PubK (from reader_Cert) AND Device signature generation and validation AND Presentation and validation of the reader_Cert in AUTH1 command AND Extended length AND AUTH1 command parameter |
| Applicability | Mfor Reader, if it supports Extended length APDU and supports sending reader_Cert in AUTH1 command |
| Interface | NFC |

NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test pre-conditions are identical to NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

Table 8-12 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | Execute AUTH1 routine ( Table 6-3). reader_cert with no chaining over multiple APDUs. | Execute AUTH1 routine ( Table 6-3). reader_cert with no chaining over multiple APDUs. | Verify AUTH1 routine criteria and the following: Reader_cert is not chained. If all criteria are met, then CONTINUE else FAIL. |

## 8.6 Expedited Fast Phase

Table 8-13 NFC\_RDR\_FAST test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_FAST |
| PICS | Expedited-fast AND Cryptogram generation and validation |
| Applicability | Mfor Reader that supports Expedited-Fast Phase |
| Interface | NFC |

NFC\_RDR\_FAST test pre-conditions are identical to

NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

Table 8-14 NFC\_RDR\_FAST test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute NFC_RDR_STANDARD_NO_CERT test steps (Table 8-3) | Execute NFC_RDR_STANDARD_NO_CERT test steps (Table 8-3) | If all criteria are met, then CONTINUE else FAIL. |
| 3 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501 | If all criteria are met, then CONTINUE else FAIL. |
| 4 | Execute AUTH0 routine ( Table 6-2). Use reader_identifier value from step 1. command_parameters = 1h | Execute AUTH0 routine ( Table 6-2). Use reader_identifier value from step 1. command_parameters = 1h | If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (User Device) DUT (Reader) | Verification at TH |
| 5 | Execute EXCHANGE indicating transaction success routine ( Table 6-4). | If all criteria are met, then PASS else FAIL. |

## 8.7 Step-Up Phase with Minimal Access Document with Key Identifier

Table 8-15 NFC\_RDR\_STEPUP\_AD\_KEY\_ID test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_AD_KEY_ID |
| PICS | Step-Up Phase AND Step-Up AID Select AND Access document storage and retrieval |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

Table 8-16 NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | IssuerKey_PubK |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document |

Table 8-17 NFC\_RDR\_STEPUP\_AD\_KEY\_ID test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501 | If all criteria are met, then CONTINUE else FAIL. |
| 4 | | Send SELECT command AID = A000000909ACCE5502, if Step-Up AID is required is indicated in signaling_bitmap in AUTH1 response | If all criteria are met, then CONTINUE else FAIL. |
| 5 | Send SELECT response | | |
| 6 | | Request Access Document using | Verify the following: |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 7 | Send appropriate Access Document in DeviceResponse inside ENVELOPE command response | | |
| 8 | One or more GET RESPONSE command and GET RESPONSE command response can be exchanged. | One or more GET RESPONSE command and GET RESPONSE command response can be exchanged. | |

## 8.8 Step-Up Phase with Minimal Access Document with Issuer Certificate

Table 8-18 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_AD_ISSUER_CERT |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

Table 8-19 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | Credential Issuer CA Certificate or Credential Issuer CA public key |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document |

Repeat Table 8-17 with Access Document with Issuer Certificate.

## 8.9 Step-Up Phase with Minimal Access Document with both Issuer Certificate and Key ID

Table 8-20 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT\_KEY\_ID test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID |
| PICS | Step-Up Phase AND Access Document processing |

| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

Table 8-21 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT\_KEY\_ID test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | IssuerKey_PubK, Credential Issuer CA Certificate or Credential Issuer CA public key |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document |

Repeat Table 8-17 with Access Document with Issuer Certificate and Key Identifier.

## 8.10 Step-Up Phase with Access Document with AccessRule

Table 8-22 NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_AD_ACCESS_RULE |
| PICS | Step-Up Phase AND Access Data element verification - Access Rules |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with AccessRule.

## 8.11 Step-Up Phase with Access Document with AccessRule using Schedules

Table 8-23 NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE\_SCHEDULES test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES |
| PICS | Step-Up PhaseAND Access Data element verification - Access Rules AND Schedules |
| Applicability | Mfor Reader that supports Step-Up Phase and that supports schedules |
| Interface | NFC |

NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE\_SCHEDULES test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with AccessRule with schedules.

## 8.12 Step-Up Phase with Access Document with Unknown NonAccessExtension

Table 8-24 NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_ACCESS\_EXTENSION test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXTENSION |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

Table 8-25 NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_ACCESS\_EXTENSION test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | IssuerKey_PubK, does not parse Extensions from Vendor_RegisteredID 000001 |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document |

Repeat Table 8-17 with Access Document with unknown nonAccessExtension.

## 8.13 Step-Up Phase with Access Document with Unknown Non-Critical AccessExtension

Table 8-26 NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_CRITICAL\_ACCESS\_EXTENSION test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_AD_UNKNOWN_NON_CRITICAL_ACCESS_EXTENSION |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_CRITICAL\_ACCESS\_EXTENSION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_

UNKNOWN\_NON\_ACCESS\_EXTENSION test pre-conditions in Table 8-25.

Repeat Table 8-17 with Access Document with unknown non-critical AccessExtension.

## 8.14 Step-Up Phase with Access Document with No Issuer Certificate or Key ID

Table 8-27 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ISSUER\_CERT\_NO\_KEY\_ID test identifiers NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ISSUER\_CERT\_NO\_KEY\_ID test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_NO_ISSUER_CERT_NO_KEY_ID |
| PICS | Step-Up Phase AND |

| | Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

Repeat Table 8-17 with Access Document with no issuer certificate and no key identifier. EXCHANGE command indicates transaction failure for test to pass.

## 8.15 Step-Up Phase with Access Document with Issuer Certificate with I nvalid Signature

Table 8-28 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_INVALID\_SIGNATURE test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_INVALID_SIGNATURE |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_INVALID\_SIGNATURE test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions in Table 8-19.

Repeat Table 8-17 with Access Document with issuer invalid signature. EXCHANGE command indicates transaction failure for test to pass.

## 8.16 Step-Up Phase with Access Document with Expired Issuer Certificate

Table 8-29 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_EXPIRED test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED |
| PICS | Step-Up PhaseAND Access Document verification - Validate time-based elements |
| Applicability | Mfor Reader that supports time concept and Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_EXPIRED test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions in Table 8-19.

Repeat Table 8-17 with Access Document with expired issuer certificate. EXCHANGE command indicates transaction failure for test to pass.

## 8.17 Step-Up Phase with Access Document with Invalid Signature in I ssuerAuth

Table 8-30 NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_SIGNATURE\_ISSUER\_AUTH test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_INVALID_SIGNATURE_ISSUER_AUTH |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_SIGNATURE\_ISSUER\_AUTH test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with invalid signature in IssuerAuth.

EXCHANGE command indicates transaction failure for test to pass.

## 8.18 Step-Up Phase with Access Document with Invalid Hash in I ssuerAuth

Table 8-31 NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_HASH\_ISSUER\_AUTH test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_INVALID_HASH_ISSUER_AUTH |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_HASH\_ISSUER\_AUTH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with invalid hash in IssuerAuth. EXCHANGE command indicates transaction failure for test to pass.

## 8.19 Step-Up Phase with Access Document with Expired IssuerAuth

Table 8-32 NFC\_RDR\_NEG\_STEPUP\_AD\_EXPIRED\_ISSUER\_AUTH test identifiers NFC\_RDR\_NEG\_STEPUP\_AD\_EXPIRED\_ISSUER\_AUTH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH |
| PICS | Step-Up Phase AND Access Document verification - Validate time-based elements |
| Applicability | Mfor Reader that supports time concept and Step-Up Phase |
| Interface | NFC |

Repeat Table 8-17 with Access Document with expired IssuerAuth. EXCHANGE command indicates transaction failure for test to pass.

## 8.20 Step-Up Phase with Access Document with Early IssuerAuth

Table 8-33 NFC\_RDR\_NEG\_STEPUP\_AD\_EARLY\_ISSUER\_AUTH test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH |
| PICS | Step-Up PhaseAND Access Document processing - Validate time-based elements |
| Applicability | Mfor Reader that supports time concept and Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_EARLY\_ISSUER\_AUTH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with early IssuerAuth. EXCHANGE command indicates transaction failure for test to pass.

## 8.21 Step-Up Phase with Access Document with Issuer Certificate Time Mismatch

Table 8-34 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERTIFICATE\_TIME\_MISMATCH test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERTIFICATE_TIME_MISMATCH |
| PICS | Step-Up PhaseAND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERTIFICATE\_TIME\_MISMATCH test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions in Table 8-19.

Repeat Table 8-17 with Access Document with Issuer Certificate validity time does not match 'signed' date. EXCHANGE command indicates transaction failure for test to pass.

## 8.22 Step-Up Phase with Access Document with ValidityIteration

Table 8-35 NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test identifiers NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION |
| PICS | Step-Up PhaseAND |

| | Access Document verification - Validity Iteration |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

Table 8-36 NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test steps

| Step# | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps (Table 8-17) | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps (Table 8-17) | Verify the following: Tag 0x97 (Reader Status) value in EXCHANGE command matches the expected result. If all criteria are met, then CONTINUE else FAIL. |

Table 8-37 NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test iterations

| Iteration | Access Credential | Access Document | Expected Result |
| 1 | Access Credential 1 | Minimal Document with Validity Iteration of 1 | Access Granted (0x97 first byte is 0x01h) |
| 2 | Access Credential 2 | Minimal Document with Validity Iteration of 9 | Access Granted (0x97 first byte is 0x01h) |
| 3 | Access Credential 1 | Minimal Document with Validity Iteration of 3 | Access Granted (0x97 first byte is 0x01h) |
| 4 | Access Credential 3 | Minimal Document with Validity Iteration of 1 | Access Denied (0x97 first byte is 0x00h) |

## 8.23 Step-Up Phase with Access Document with TimeVerificationRequired

Table 8-38 NFC\_RDR\_NEG\_STEPUP\_AD\_TIME\_VERIFICATION\_REQUIRED test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQUIRED |
| PICS | Step-Up Phase AND |
| Applicability | Mfor Reader that supports Step-Up Phase and does not support time concept |

| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_TIME\_VERIFICATION\_REQUIRED test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with Issuer Certificate with TimeVerificationRequired set and reader cannot determine time. EXCHANGE command indicates transaction failure for test to pass.

## 8.24 Step-Up Phase with Access Document with No Data Elements

Table 8-39 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_DATA\_ELEMENTS test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_NO_DATA_ELEMENTS |
| PICS | Step-Up PhaseAND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_DATA\_ELEMENTS test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with no data elements. EXCHANGE command indicates transaction failure for test to pass.

## 8.25 Step-Up Phase with Access Document with IssuerAuth docType Mismatch

Table 8-40 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_DOCTYPE\_MISMATCH test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_ISSUER_DOCTYPE_MISMATCH |
| PICS | Step-Up PhaseAND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_DOCTYPE\_MISMATCH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with IssuerAuth doctype does not match document docType. EXCHANGE command indicates transaction failure for test to pass.

## 8.26 Step-Up Phase with Access Document with docType Not Aliro-a

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_DOCTYPE_NOT_ALIROA |

| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_DOCTYPE\_NOT\_ALIROA test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with doctype not 'aliro-a'. EXCHANGE command indicates transaction failure for test to pass.

## 8.27 Step-Up Phase with Access Document with DeviceKeyInfo Mismatch

Table 8-41 NFC\_RDR\_NEG\_STEPUP\_AD\_DEVICE\_KEY\_INFO\_MISMATCH test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_DEVICE_KEY_INFO_MISMATCH |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_DEVICE\_KEY\_INFO\_MISMATCH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with deviceKeyInfo does not match Access Credential. EXCHANGE command indicates transaction failure for test to pass.

## 8.28 Step-Up Phase with Access Document with Invalid Access Data Element Version

Table 8-42 NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_ACCESS\_DATA\_ELEMENT\_VERSION test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_INVALID_ACCESS_DATA_ELEMENT_VERSION |
| PICS | Step-Up Phase AND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_ACCESS\_DATA\_ELEMENT\_VERSION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with invalid access data element version. EXCHANGE command indicates transaction failure for test to pass.

## 8.29 Step-Up Phase with Access Document with No AccessRule for I ntended Reader Action

Table 8-43 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ACCESS\_RULE\_FOR\_READER\_ACTION test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_NO_ACCESS_RULE_FOR_READER_ACTION |
| PICS | Step-Up PhaseAND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ACCESS\_RULE\_FOR\_READER\_ACTION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with no AccessRule for intended reader action. EXCHANGE command indicates transaction failure for test to pass.

## 8.30 Step-Up Phase with Access Document with No Valid Schedule in AccessRule AllowScheduleIds

Table 8-44 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_VALID\_SCHEDULE\_ALLOW\_SCHEDULEID test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_NO_VALID_SCHEDULE_ALLOW_SCHEDULEID |
| PICS | Step-Up PhaseAND Access Data Element verification - Schedules |
| Applicability | Mfor Reader that supports Step-Up Phase and that supports schedules |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_VALID\_SCHEDULE\_ALLOW\_SCHEDULEID test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with no valid schedule in AccessRule AllowScheduleIds. EXCHANGE command indicates transaction failure for test to pass.

## 8.31 Step-Up Phase with Access Document with Valid Schedule in AccessRule DenyScheduleIds

Table 8-45 NFC\_RDR\_NEG\_STEPUP\_AD\_VALID\_SCHEDULE\_DENY\_SCHEDULEID test identifiers NFC\_RDR\_NEG\_STEPUP\_AD\_VALID\_SCHEDULE\_DENY\_SCHEDULEID test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_VALID_SCHEDULE_DENY_SCHEDULEID |

| PICS | Step-Up Phase AND |
| Applicability | Mfor Reader that supports Step-Up Phase and that supports schedules |
| Interface | NFC |

Repeat Table 8-17 with Access Document with valid schedule in AccessRule DenyScheduleIds. EXCHANGE command indicates transaction failure for test to pass.

## 8.32 Step-Up Phase with Access Document with Schedule in AccessRule and TimeVerifyRequired

Table 8-46 NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_TIME\_VERIFY\_REQUIRED test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_TIME_VERIFY_REQUIRED |
| PICS | Step-Up Phase AND NOT Access Document verification - Time-based elements |
| Applicability | Mfor Reader that supports Step-Up Phase and that does not support time-based elements |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_TIME\_VERIFY\_REQUIRED test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with schedule in AccessRule and TimeVerifyRequired. EXCHANGE command indicates transaction failure for test to pass.

## 8.33 Step-Up Phase with Access Document with Schedule in AccessRule with No Reader Support

Table 8-47 NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_IN\_ACCESS\_RULE\_AND\_READER test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_IN_ACCESS_RULE_AND_READER |
| PICS | Step-Up Phase AND NOT Access Document verification - Schedules |
| Applicability | Mfor Reader that supports Step-Up Phase and that does not support schedules |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_IN\_ACCESS\_RULE\_AND\_READER test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with schedule in AccessRule and Reader. EXCHANGE command indicates transaction failure for test to pass.

## 8.34 Step-Up Phase with Access Document with Unknown ReaderRule

Table 8-48 NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_READER\_RULE test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE |
| PICS | Step-Up PhaseAND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up Phase |
| Interface | NFC |

Table 8-49 NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_READER\_RULE test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | IssuerKey_PubK, does not store a Reader Rule with ReaderRuleId 0xF118 |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document |

Repeat Table 8-17 with Access Document with unknown ReaderRule. EXCHANGE command indicates transaction failure for test to pass.

## 8.35 Step-Up Phase with Access Document with Unknown Critical AccessExtension

Table 8-50 NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_CRITICAL\_ACCESS\_EXTENSION test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_CRITICAL_ACCESS_EXTENSION |
| PICS | Step-Up PhaseAND Access Document processing |
| Applicability | Mfor Reader that supports Step-Up |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_CRITICAL\_ACCESS\_EXTENSION test pre-conditions are identical to

NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_ACCESS\_EXTENSION test preconditions in Table 8-25.

Repeat Table 8-17 with Access Document with unknown critical AccessExtension. EXCHANGE command indicates transaction failure for test to pass.

## 8.36 Step-Up Phase with Revocation Document

## Table 8-51 NFC\_RDR\_STEPUP\_RD test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_STEPUP_RD |
| PICS | Step-Up Phase AND Revocation document storage and retrieval AND Revocation document processing |
| Applicability | Mfor Reader that supports Revocation Documents |
| Interface | NFC |

## Table 8-52 NFC\_RDR\_STEPUP\_RD test pre-conditions

| Provision onto | Remarks |
| TH (User Device) | reader_PubK, reader_group_identifier, Revocation Documents |
| DUT (Reader) | Access Credential long term public keys, IssuerKey_PubK |

## Table 8-53 NFC\_RDR\_STEPUP\_RD test steps

| Step# | TH (User Device) | DUT (Reader) | Verification at TH |
| 5 | Send SELECT response | | |
| 7 | Send appropriate Revocation Document in DeviceResponse inside ENVELOPE command response | | |

| Step# | TH (User Device) | DUT (Reader) | Verification at TH |
| | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps (Table 8-17) with Access Credential 1 | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps (Table 8-17) with Access Credential 1 | Verify the following: Tag 0x97 matches expected result for Access Credential 1. If all criteria are met, then CONTINUE else FAIL. |
| 12 | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps (Table 8-17) with Access Credential 2 | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps (Table 8-17) with Access Credential 2 | Verify the following: Tag 0x97 matches expected result for Access Credential 2. If all criteria are met, then CONTINUE else FAIL. |

Table 8-54 NFC\_RDR\_STEPUP\_RD test iterations

| Iteration | Revocation Document | Access Credential 1 Result | Access Credential 2 Result |
| 1 | Overwrite containing Access Credential 1 Public Key | Access Rejected (0x97 first byte is 0x00h) | Access Accepted (0x97 first byte is 0x01h) |
| 2 | Update adding Access Credential 2 Public Key | Access Rejected | Access Rejected |
| 3 | Update removing Access Credential 1 Public Key | Access Accepted | Access Rejected |
| 4 | Update adding Access Credential 1 Public Key and removing Access Credential 1 Public Key and Access Credential 2 Public Key | Access Accepted | Access Accepted |
| 5 | Overwrite containing Access Credential 2 Public Key | Access Accepted | Access Rejected |
| 6 | Overwrite empty | Access Accepted | Access Accepted |

## 8.37 Step-Up Phase with Revocation Document with Invalid Revocation Document Version

Table 8-55 NFC\_RDR\_NEG\_STEPUP\_RD\_INVALID\_ELEMENT\_VERSION test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSION |
| PICS | Step-Up Phase AND |

| | Revocation document storage and retrieval AND Revocation document processing |
| Applicability | Mfor Reader that supports Revocation Documents |
| Interface | NFC |

NFC\_RDR\_NEG\_STEPUP\_RD\_INVALID\_ELEMENT\_VERSION test pre-conditions are identical to NFC\_RDR\_STEPUP\_RD test pre-conditions in Table 8-52 NFC\_RDR\_STEPUP\_RD test pre-conditions

Table 8-56 NFC\_RDR\_NEG\_STEPUP\_RD\_INVALID\_ELEMENT\_VERSION test steps

| Step# | TH (User Device) | DUT (Reader) | Verification at TH |

## 8.38 SELECT Response with No Common Expedited Protocol Version

Table 8-57 NFC\_RDR\_NEG\_SEL\_RSP\_NO\_COMMON\_EXPEDITED\_PROTOCOL\_VERSION test identifiers Interface NFC

| Parameter | Value |
| Test ID | NFC_RDR_NEG_SEL_RSP_NO_COMMON_EXPEDITED_PROTOCOL_VERSION |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor Reader |

NFC\_RDR\_NEG\_SEL\_RSP\_NO\_COMMON\_EXPEDITED\_PROTOCOL\_VERSION test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test preconditions in Table 8-2.

Table 8-58 NFC\_RDR\_NEG\_SEL\_RSP\_NO\_COMMON\_EXPEDITED\_PROTOCOL\_VERSION test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Send SELECT Response. Set the expedited_phase_supported_protocol_versions equal to 0x0A00 | | |
| 3 | | Send CONTROL FLOW command. | Verify the following: 1. CONTROL FLOW command data field length does not exceed 255 bytes. 2. S2_parameter in command data field is equal to 0x27. If all criteria are met, then CONTINUE else FAIL. |

## 8.39 AUTH0 with Extra Unknown TLV

Table 8-59 NFC\_RDR\_NEG\_AUTH0\_EXTRA\_TAG test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_AUTH0_EXTRA_TAG |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor Reader |
| Interface | NFC |

NFC\_RDR\_NEG\_AUTH0\_EXTRA\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-60 NFC\_RDR\_NEG\_AUTH0\_EXTRA\_TAG test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Execute AUTH0 routine ( Table 6-2). Extra tag can be randomly injected at any location in the AUTH0 response command payload. | Execute AUTH0 routine ( Table 6-2). Extra tag can be randomly injected at any location in the AUTH0 response command payload. | If all criteria are met, then CONTINUE else FAIL. |

## 8.40 AUTH0 with Wrong Value

Table 8-61 NFC\_RDR\_NEG\_AUTH0\_WRONG\_VALUE test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_AUTH0_WRONG_VALUE |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor Reader |
| Interface | NFC |

NFC\_RDR\_NEG\_AUTH0\_WRONG\_VALUE test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-62 NFC\_RDR\_NEG\_AUTH0\_WRONG\_VALUE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501. | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501. | If all criteria are met, then CONTINUE else FAIL. |
| 2 | Execute AUTH0 routine ( Table 6-2). wrong value/length of tag in the AUTH0 | Execute AUTH0 routine ( Table 6-2). wrong value/length of tag in the AUTH0 | If all criteria are met, then CONTINUE else FAIL. |
| 3 | Execute CONTROL FLOW indicating transaction failure routine (Table 6-6). | Execute CONTROL FLOW indicating transaction failure routine (Table 6-6). | If all criteria are met, then PASS else FAIL. |

## 8.41 AUTH1 with Wrong User Device Signature

Table 8-63 NFC\_RDR\_NEG\_AUTH1\_WRONG\_UD\_SIGNATURE test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_AUTH1_WRONG_UD_SIGNATURE |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor Reader |

| Interface | NFC |

NFC\_RDR\_NEG\_AUTH1\_WRONG\_UD\_SIGNATURE test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-64 NFC\_RDR\_NEG\_AUTH1\_WRONG\_UD\_SIGNATURE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | Execute AUTH1 routine ( Table 6-3). Send wrong User Device signature in AUTH1 | Execute AUTH1 routine ( Table 6-3). Send wrong User Device signature in AUTH1 | If all criteria are met, then CONTINUE else FAIL. |

## 8.42 AUTH1 with Extra Tag

Table 8-65 NFC\_RDR\_NEG\_AUTH1\_EXTRA\_TAG test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_AUTH1_EXTRA_TAG |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor Reader |
| Interface | NFC |

NFC\_RDR\_NEG\_AUTH1\_EXTRA\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-66 NFC\_RDR\_NEG\_AUTH1\_EXTRA\_TAG test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | Execute AUTH1 routine ( Table 6-3). Send extra unknown tag TLV in AUTH1 response. | Execute AUTH1 routine ( Table 6-3). Send extra unknown tag TLV in AUTH1 response. | If all criteria are met, then CONTINUE else FAIL. |

## 8.43 AUTH1 with Wrong Values

Table 8-67 NFC\_RDR\_NEG\_AUTH1\_WRONG\_VALUES test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_NEG_AUTH1_WRONG_VALUES |
| PICS | Expedited-Standard Phase |
| Applicability | Mfor Reader |
| Interface | NFC |

NFC\_RDR\_NEG\_AUTH1\_WRONG\_VALUES test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-68 NFC\_RDR\_NEG\_AUTH1\_WRONG\_VALUES test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | Execute AUTH1 routine ( Table 6-3). Send wrong value/length for tag in AUTH1 | Execute AUTH1 routine ( Table 6-3). Send wrong value/length for tag in AUTH1 | If all criteria are met, then CONTINUE else FAIL. |
| 4 | Execute EXCHANGE indicating transaction failure routine (Table 6-5). | Execute EXCHANGE indicating transaction failure routine (Table 6-5). | If all criteria are met, then PASS else FAIL. |

## 8.44 EXCHANGE with Reader Descriptor Tag

Table 8-69 NFC\_RDR\_EXCHANGE\_RDR\_DESCRIPTOR\_TAG test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_EXCHANGE_RDR_DESCRIPTOR_TAG |
| PICS | Reader Descriptor tag |
| Applicability | Mfor Reader that supports sending Reader Information to the User Device |
| Interface | NFC |

NFC\_RDR\_EXCHANGE\_RDR\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-70 NFC\_RDR\_EXCHANGE\_RDR\_DESCRIPTOR\_TAG test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501. | Execute SELECT routine ( Table 6-1). Set AID = A000000909ACCE5501. | If all criteria are met, then CONTINUE else FAIL. |
| 2 | Execute AUTH0 routine ( Table 6-2). command_parameters = 0h. | Execute AUTH0 routine ( Table 6-2). command_parameters = 0h. | If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 4 | Execute EXCHANGE indicating transaction success routine ( Table 6-4). | Execute EXCHANGE indicating transaction success routine ( Table 6-4). | Verify the following in addition to EXCHANGE routine: 1. order of TLVs in EXCHANGE command matches specification. 2. All mandatory TLVs in EXCHANGE command present 3. 0xAE with sub tag 0xB5 is present 4. Format of 0xB5 matches the technical specification 5. 0xAE length is less than 250 bytes If all criteria are met, then PASS else FAIL. |

## 8.45 Control Flow with Reader Descriptor Tag

| Parameter | Value |
| Test ID | NFC_RDR_CONTROL_FLOW_RDR_DESCRIPTOR_TAG |
| PICS | Reader Descriptor tag |
| Applicability | Mfor Reader that supports sending Reader Information to the User Device |
| Interface | NFC |

NFC\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-71 NFC\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute NFC_RDR_NEG_AUTH0_WRONG_VALUE test steps (Table 8-62). | Execute NFC_RDR_NEG_AUTH0_WRONG_VALUE test steps (Table 8-62). | Verify the following in addition to NFC_RDR_NEG_AUTH0_WRONG_VALUE test steps: 1. All mandatory TLVs in Control Flow command are present. 2. 0x63 is present. 3. Format of 0x63 matches the technical specification. 4. Control Flow command data field length is less than 255 bytes. If all criteria are met, then PASS else FAIL. |

## 8.46 BLE+UWB Flow with Reader Descriptor Tag

Table 8-72 BLEUWB\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_CONTROL_FLOW_RDR_DESCRIPTOR_TAG |
| PICS | BLE + UWBFlow AND Reader Descriptor tag |
| Applicability | Mfor Reader that supports sending Reader Information to the User Device |
| Interface | BLE |

BLEUWB\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

Table 8-73 BLEUWB\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Establish L2CAP connection | | |
| 3 | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | | |
| 5 | | send Event Message ID carrying General Error Attribute ID and Reader Information Attribute ID | Verify the following: 1. General Error Attribute ID and Reader Descriptor Attribute ID are present 2. Format of Attribute IDs matches the technical specification If all criteria are met, then PASS else FAIL. |
| 6 | BLE teardown | | |

## 8.47 EXCHANGE with Mailbox Command

This test assumes Reader Under Test can be made to send EXCHANGE with Mailbox commands.

Table 8-74 NFC\_RDR\_EXCHANGE\_MAILBOX test identifiers

| Parameter | Value |
| Test ID | NFC_RDR_EXCHANGE_MAILBOX |
| PICS | Mailbox |
| Applicability | Mfor Reader that supports Mailbox commands |
| Interface | NFC |

Table 8-75 NFC\_RDR\_EXCHANGE\_MAILBOX test pre-conditions

| Provision onto | Remarks |
| TH (User Device) | Reader_PubK, reader_group_identifier, non-zero mailbox populated with existing data |
| DUT (Reader) | Access Credential long term public key |

## Table 8-76 NFC\_RDR\_EXCHANGE\_MAILBOX test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 4 | | Send EXCHANGE command multiple times with multiple Mailbox commands to or from mailbox | Verify the following: Request format matches technical specification. Requests contain one or more Mailbox commands. If all criteria are met, then CONTINUE else FAIL. |
| 5 | Send EXCHANGE response | | |

## 8.48 BLE+UWB Flow with Expedited Standard Phase

Table 8-77 BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test identifiers

| Parameter | Value |

| Test ID | BLEUWB_RDR_EXPEDITED_STANDARD_PHASE |
| PICS | BLE + UWBFlow AND UWB ranging AND Dynamic Advertisement Tag AND Unsolicited reader status reporting AND Expedited-Standard Phase AND UWB Time Synchronization |
| Applicability | Mfor Reader that supports BLE + UWB Flow |
| Interface | BLE |

## Table 8-78 BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | Access Credential long term public key, GRK |
| TH (User Device) | reader_PubK, reader_group_identifier, GRK |
| NOTE 1: The TH (User Device) and the DUT (Reader) are in very close proximity (e.g.,1m and line-of- sight). NOTE 2: Reader is in secured state as a pre-condition. | NOTE 1: The TH (User Device) and the DUT (Reader) are in very close proximity (e.g.,1m and line-of- sight). NOTE 2: Reader is in secured state as a pre-condition. |

Table 8-79 BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Send Time Sync Message ID | | |
| 5 | | Send Reader Status Changed Message ID carrying State Attribute ID | Verify the following: State Attribute ID has second byte [B7:B0] set to 0x01 or 0x02 or 0x81 or 0x82. If all criteria are met, then PASS else FAIL. |

## 8.49 BLE+UWB Flow with Expedited Fast Phase

## Table 8-80 BLEUWB\_RDR\_EXPEDITED\_FAST\_PHASE test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_EXPEDITED_FAST_PHASE |
| PICS | BLE +UWBFlow AND UWBranging AND Dynamic Advertisement Tag AND Unsolicited reader status reporting AND Expedited-fast |
| Applicability | Mfor Reader that supports BLE + UWBFlow and Expedited-Fast Phase |
| Interface | BLE |

BLEUWB\_RDR\_EXPEDITED\_FAST\_PHASE test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-81 BLEUWB\_RDR\_EXPEDITED\_FAST\_PHASE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 3 | | Send Bluetooth LE advertisement | |
| 4 | Establish L2CAP connection | | |
| 5 | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | | |
| 6 | | Send AUTH0 command with command_parameters = 1h | |
| 7 | Send AUTH0 response | | |
| 8 | | Send EXCHANGE command with Tag 0x98 | Verify the following: Tag 0x98 is present. If all criteria are met, then CONTINUE else FAIL. |
| 9 | Send EXCHANGE Response | | |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 11 | Send Time Sync Message ID | | |
| 12 | Send Ranging Message ID carrying Initiate Ranging Session Attribute ID | | |
| 15 | | Reader Status Changed Message ID carrying State Attribute ID is sent | Verify the following: State Attribute ID has second byte [B7:B0] set to 0x01 or 0x02 or 0x81 or 0x82. If all criteria are met, then PASS else FAIL. |

## 8.50 BLE+UWB Flow with Step-Up Phase

Table 8-82 BLEUWB\_RDR\_STEPUP\_PHASE test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_STEPUP_PHASE |
| PICS | BLE + UWBFlow AND UWB ranging AND Dynamic Advertisement Tag AND Unsolicited reader status reporting AND Step-Up Phase |
| Applicability | Mfor Reader that supports BLE + UWB Flow and support Step-Up Phase |
| Interface | BLE |

## Table 8-83 BLEUWB\_RDR\_STEPUP\_PHASE test pre-conditions

| Provision onto | Remarks |
| DUT (Reader) | Access Credential long term public key, GRK, IssuerKey_PubK |
| TH (User Device) | reader_PubK, reader_group_identifier, GRK, Access Document |

NOTE 1: The TH (User Device) and the DUT (Reader) are in very close proximity (e.g., 1 m and line-ofsight).

NOTE 2: Reader is in secured state as a pre-condition.

## Table 8-84 BLEUWB\_RDR\_STEPUP\_PHASE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE + UWBAliro Flow Supported Bit is set to 1. If all criteria are met, then CONTINUE else FAIL. |
| 3 | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | | |
| 7 | Send EXCHANGE response | | |
| 8 | | Request Access Document using DeviceRequest inside ENVELOPE command | |
| 9 | Send Access Document in DeviceResponse inside ENVELOPE command response | | |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 10 | One or more GET RESPONSE command/response can be exchanged | One or more GET RESPONSE command/response can be exchanged | |
| 11 | | Send Reader Status Access Protocol Completed Message ID carrying Reader Information Attribute ID | Verify the following: Ensure reader status is secured. Format of message matches technical specification. If all criteria are met, then CONTINUE else FAIL. |
| 12 | Send Time Sync Message ID | | |
| 13 | Send Ranging Message ID carrying Initiate Ranging Session Attribute ID | | |
| 16 | | Reader Status Changed Message ID carrying State Attribute ID is sent | Verify the following: State Attribute ID has second byte [B7:B0] set to 0x01 or 0x02 or 0x81 or 0x82. If all criteria are met, then PASS else FAIL. |

## 8.51 BLE+UWB Flow with UWB Ranging Suspend

Table 8-85 BLEUWB\_RDR\_RANGING\_SUSPEND test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_RANGING_SUSPEND |
| PICS | BLE + UWBFlow AND UWB ranging suspend |
| Applicability | Mfor Reader that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_RDR\_RANGING\_SUSPEND test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78 with the exception: The TH (User Device) and the DUT (Reader) are in close proximity (e.g., 5 m and line-of-sight).

Table 8-86 BLEUWB\_RDR\_RANGING\_SUSPEND test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Send Time Sync Message ID | | |
| 3 | Send Ranging Message ID carrying Initiate Ranging Session Attribute ID | | |
| 6 | Send Ranging Session Suspend Request with correct UWB Session Identifier | | |
| 7 | | Send Ranging Session Suspend Response | Verify the following 1. this message is sent. 2. format of Ranging Session Suspend Response matches technical specification. If all criteria are met, then PASS else FAIL. The status can either value 0 or 1. |

## 8.52 BLE+UWB Flow with UWB Ranging Resume

| Parameter | Value |
| Test ID | BLEUWB_RDR_RANGING_RESUME |
| PICS | BLE +UWBFlow AND UWBranging resume |
| Applicability | Mfor Reader that supports BLE + UWBFlow |
| Interface | BLE |

BLEUWB\_RDR\_RANGING\_RESUME test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78 with the exception: The TH (User Device) and the DUT (Reader) are in close proximity (e.g., 5 m and line-of-sight).

## Table 8-87 BLEUWB\_RDR\_RANGING\_RESUME test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Send Time Sync Message ID | | |
| 3 | Send Ranging Message ID carrying Initiate Ranging Session Attribute ID | | |
| 6 | Send Ranging Message ID carrying Ranging Session Suspended Attribute ID | | |
| 7 | 1 second after previous step, send Ranging Message ID carrying Initiate Ranging Session Resume Attribute ID | | |
| 9 | Send Ranging Session Resume Response Message | | Verify the following: 1. Format of the message matches technical specification. 2. UWBranging is resumed. 3. UWBpackets are exchanged overUWB transport in short time (e.g., up to 3 seconds) after sending Ranging Session Resume Response Message. If all criteria are met, then PASS else FAIL. |

## 8.53 BLE+UWB Flow with Failed L2CAP

Table 8-88 BLEUWB\_RDR\_NEG\_FAILED\_L2CAP test identifiers

Parameter

Value

| Test ID | BLEUWB_RDR_NEG_FAILED_L2CAP |
| PICS | BLE +UWBFlow |
| Applicability | Mfor Reader that supports BLE + UWBFlow |
| Interface | BLE |

BLEUWB\_RDR\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-89 BLEUWB\_RDR\_NEG\_FAILED\_L2CAP test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE + UWB Aliro Flow Supported Bit is not set to 1. If all criteria are met, then CONTINUE else FAIL. |

## 8.54 BLE+UWB Flow with wrong SPSM

## Table 8-90 BLEUWB\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_NEG_FAILED_SPSM_L2CAP |
| PICS | BLE +UWBFlow |
| Applicability | Mfor Reader that supports BLE + UWBFlow |
| Interface | BLE |

BLEUWB\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-91 BLEUWB\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE + UWB Aliro Flow Supported Bit is not set to 1. If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| | | | If all criteria are met, then PASS else FAIL. |

## 8.55 BLE+UWB Flow with timeout before AUTH0

## Table 8-92 BLEUWB\_RDR\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_NEG_TIMEOUT_BEFORE_AUTH0 |
| PICS | BLE + UWBFlow |
| Applicability | Mfor Reader that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_RDR\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-93 BLEUWB\_RDR\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Establish L2CAP connection | | |
| 3 | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | | |
| 4 | | Send AUTH0 command | |
| 5 | Wait for at least 3 seconds before sending AUTH0 command response | | |
| 6 | | Send Event Message ID carrying General Error Attribute ID | Verify the following: Format of Event Message ID carrying General Error Attribute ID matches the technical specification. If all criteria are met, then CONTINUE else FAIL. |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| | | | If all criteria are met, then PASS else FAIL. |

## 8.56 BLE+UWB Flow with Timeout Extension

## Table 8-94 BLEUWB\_RDR\_TIMEOUT\_EXTENSION test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_TIMEOUT_EXTENSION |
| PICS | BLE + UWBFlow |
| Applicability | Mfor Reader that supports BLE + UWBFlow |
| Interface | BLE |

BLEUWB\_RDR\_TIMEOUT\_EXTENSION test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-95 BLEUWB\_RDR\_TIMEOUT\_EXTENSION test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE + UWB Aliro Flow Supported Bit is not set to 1. If all criteria are met, then CONTINUE else FAIL. |
| 2 | Establish L2CAP connection | | |
| 3 | Send Initiate Access Protocol Message ID carrying AID = A000000909ACCE5501 | | |
| 4 | | Send AUTH0 command | |
| 5 | Send Event carrying Busy Attribute ID at 1 s after receiving AUTH0 command | | |
| 6 | Send AUTH0 command response after 1 s after sending Event Busy Attribute ID | | |
| 7 | | Send AUTH1 command | |
| 8 | Send AUTH1 response | | |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 10 | Send EXCHANGE response | | |
| 11 | | Send Reader Status Access Protocol Completed Message ID carrying Reader Information Attribute ID | Verify the following: Format of message matches technical specification. If all criteria are met, then PASS else FAIL. |

## 8.57 BLE+UWB Flow with M2 Message Mismatch Parameter

Table 8-96 BLEUWB\_RDR\_NEG\_M2\_MISMATCH\_PARAMETER test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_NEG_M2_MISMATCH_PARAMETER |
| PICS | BLE + UWBFlow |
| Applicability | Mfor Reader that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_RDR\_NEG\_M2\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-97 BLEUWB\_RDR\_NEG\_M2\_MISMATCH\_PARAMETER test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Send Time Sync Message ID | | |
| 4 | Send Ranging Message ID carrying Initiate Ranging Session Attribute ID | | |
| 5 | | Send Ranging Session Setup M1 Message ID | |
| 6 | Send Ranging Session Setup M2 Message ID without UWB Config ID | | |
| 7 | | Send Event with General Error Attribute ID indicating Wrong Parameters | Verify the following: Format of Event Message ID. General Error Attribute ID indicates Wrong Parameters. |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| | | | If all criteria are met, then PASS else FAIL. |
| 8 | BLE teardown | | |

## 8.58 BLE+UWB Flow with M4 Message Mismatch Parameter

## Table 8-98 BLEUWB\_RDR\_NEG\_M4\_MISMATCH\_PARAMETER test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_NEG_M4_MISMATCH_PARAMETER |
| PICS | BLE + UWB Flow |
| Applicability | Mfor Reader that supports BLE+UWB Flow |
| Interface | BLE |

BLEUWB\_RDR\_NEG\_M4\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-99 BLEUWB\_RDR\_NEG\_M4\_MISMATCH\_PARAMETER test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Send Time Sync Message ID | | |
| 3 | Send Ranging Message ID carrying Initiate Ranging Session Attribute ID | | |
| 4 | | Send Ranging Session Setup M1 Message ID | |
| 5 | Send Ranging Session Setup M2 Message | | |
| 6 | | Send Ranging Session Setup M3 Message | |
| 7 | Send Ranging Session Setup M4 Message ID without UWBTime0 | | |
| 15 | | Send Ranging Message ID carrying Secure Ranging Over UWBRadio Failed Attribute ID or General Error | Verify the following: Format of this message matches the specification. If all criteria are met, then PASS else FAIL. |

## 8.59 BLE+UWB Flow with Suspend Request Mismatch Parameter

Table 8-100 BLEUWB\_RDR\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_NEG_SUSPEND_MISMATCH_PARAMETER |
| PICS | BLE + UWBFlow AND UWB Ranging Suspend |
| Applicability | Mfor Reader that supports BLE + UWB Flow |
| Interface | BLE |

BLEUWB\_RDR\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-101 BLEUWB\_RDR\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | Execute BLEUWB_RDR_RANGING_SUSPEND test steps ( Table 8-86). Send Ranging Session Suspend Request without UWBSession Identifier | Send Event Message ID carrying General Error Attribute ID indicating Wrong Parameters | Verify the following: Format of Event Message ID. General Error Attribute ID indicates Wrong Parameters. If all criteria are met, then PASS else FAIL. |

## 8.60 BLE+UWB Flow BLE Advertisement Format

Table 8-102 BLEUWB\_RDR\_ADVERTISEMENT\_FORMAT test identifiers

| Parameter | Value |
| Test ID | BLEUWB_RDR_ADVERTISEMENT_FORMAT |
| PICS | BLE + UWBFlow AND |
| Applicability | Mfor Reader that supports BLE + UWB Flow |
| Interface | BLE |

Table 8-103 BLEUWB\_RDR\_ADVERTISEMENT\_FORMAT test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: advertisement data matches technical specification. If all criteria are met, then PASS else FAIL. |

## 8.61 BLE-only Flow - RKE Unsecure

Table 8-104 BLERKE\_RDR\_UNSECURE test identifiers

| Parameter | Value |
| Test ID | BLERKE_RDR_UNSECURE |
| PICS | BLE-Only Flow AND Unsolicited reader status reporting |
| Applicability | Mfor Reader that supports BLE-Only Flow |
| Interface | BLE |

BLERKE\_RDR\_UNSECURE test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78. Reader is in secured state before running this test.

Table 8-105 BLERKE\_RDR\_UNSECURE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Send RKE Request Message ID with action=UNSECURE | | |
| 3 | | Send Reader Status Changed Message ID carrying State Attribute ID (Unsecured) | Verify the following: State Attribute ID has second byte [B7:B0] set to 0x01 or 0x02 or 0x81 or 0x82. If all criteria are met, then PASS else FAIL. |

## 8.62 BLE-only Flow - RKE Secure

Table 8-106 BLERKE\_RDR\_SECURE test identifiers

| Parameter | Value |
| Test ID | BLERKE_RDR_SECURE |
| PICS | BLE-Only Flow AND Unsolicited reader status reporting |
| Applicability | Mfor Reader that supports BLE-Only Flow |
| Interface | BLE |

BLERKE\_RDR\_SECURE test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78. Reader is in unsecured state before running this test.

## Table 8-107 BLERKE\_RDR\_SECURE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 11 | Send RKE Request Message ID with action=SECURE | | |
| 12 | | Send Reader Status Changed Message ID carrying State Attribute ID (Secured) | Verify the following: State Attribute ID has second byte [B7:B0] set to 0x00 or 0x02 or 0x80 or 0x82. If all criteria are met, then PASS else FAIL. |

## 8.63 BLE-Only Flow with Disallowed Expedited Fast Phase

Table 8-108 BLERKE\_RDR\_NEG\_FAST test identifiers

| Parameter | Value |
| Test ID | BLERKE_RDR_NEG_FAST |
| PICS | BLE-Only Flow |
| Applicability | Mfor Reader that supports BLE-Only Flow |
| Interface | BLE |

BLERKE\_RDR\_NEG\_FAST test pre-conditions are identical to

BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

## Table 8-109 BLERKE\_RDR\_NEG\_FAST test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 2 | Secure the Reader and BLE teardown | | |

## 8.64 BLE-Only Flow with Failed L2CAP

Table 8-110 BLERKE\_RDR\_NEG\_FAILED\_L2CAP test identifiers

Parameter

Value

| Test ID | BLERKE_RDR_NEG_FAILED_L2CAP |
| PICS | BLE-Only Flow |
| Applicability | Mfor Reader that supports BLE-Only Flow |
| Interface | BLE |

BLERKE\_RDR\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-111 BLERKE\_RDR\_NEG\_FAILED\_L2CAP test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE-Only Aliro Flow Supported Bit is not set to 1. If all criteria are met, then CONTINUE else FAIL. |

## 8.65 BLE-Only Flow with wrong SPSM

Table 8-112 BLERKE\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test identifiers

| Parameter | Value |
| Test ID | BLERKE_RDR_NEG_FAILED_SPSM_L2CAP |
| PICS | BLE-Only Flow |
| Applicability | Mfor Reader that supports BLE-Only Flow |
| Interface | BLE |

BLERKE\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

Table 8-113 BLERKE\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE-Only Aliro Flow Supported Bit is not set to 1. If all criteria are met, then CONTINUE else FAIL. |

## 8.66 BLE-Only Flow with Step-Up Phase

Table 8-114 BLERKE\_RDR\_STEPUP\_PHASE test identifiers

| Parameter | Value |
| Test ID | BLERKE_RDR_STEPUP_PHASE |
| PICS | BLE-Only Flow |
| Applicability | Mfor Reader that supports BLE-Only Flow AND supports Step-Up Phase |
| Interface | BLE |

BLERKE\_RDR\_STEPUP\_PHASE test pre-conditions are identical to BLEUWB\_RDR\_STEPUP\_PHASE test pre-conditions in Table 8-83.

Table 8-115 BLERKE\_RDR\_STEPUP\_PHASE test steps

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 1 | | Send Bluetooth LE advertisement | Verify the following: BLE-Only Aliro Flow Supported Bit is set to 1. Advertisement format matches the technical specification. If all criteria are met, then CONTINUE else FAIL. |
| 2 | Establish L2CAP connection | | |
| 3 | Send Initiate Access Protocol RKE Message ID carrying AID = A000000909ACCE5501 | | |
| 5 | Send AUTH0 response | | |
| 6 | | Send AUTH1 command | |
| 7 | Send AUTH1 response | | |
| 8 | | [Optional] Send EXCHANGE command | |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH |
| 10 | | Request Access Document using DeviceRequest inside ENVELOPE command | |
| 11 | Send Access Document in DeviceResponse inside ENVELOPE command response | | |
| 12 | One or more GET RESPONSE command/response can be exchanged | One or more GET RESPONSE command/response can be exchanged | |
| 13 | | Send Reader Status Access Protocol Completed Message ID carrying Reader Information Attribute ID | Verify the following: Ensure reader status is secured. Format of message matches technical specification. If all criteria are met, then CONTINUE else FAIL. |
| 14 | Send RKE Request Message ID with action=UNSECURE | | |
| 15 | | Reader Status Changed Message ID carrying State Attribute ID is sent | Verify the following: State Attribute ID has second byte [B7:B0] set to 0x01 or 0x02 or 0x81 or 0x82. If all criteria are met, then PASS else FAIL. |
