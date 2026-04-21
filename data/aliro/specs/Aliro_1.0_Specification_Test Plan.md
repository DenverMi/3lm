![](_page_0_Picture_0.jpeg)

# **ALIRO Specification Test Plan Version 1.0**

Document: 26-42803-001\_Aliro\_1.0\_specification\_test\_plan

February 9, 2026

Sponsored by: Connectivity Standard Alliance

Accepted by: This document has been accepted for release by the

Connectivity Standards Alliance Board of Directors

Abstract This test plan describes the tests to be performed for

supported Aliro 1.0 features.

Copyright 2026 Connectivity Standards Alliance, Inc.

508 Second Street, Suite 206 Davis, CA 95616 - USA

www.csa-iot.org

All rights reserved.

Permission is granted to members of the Connectivity Standards Alliance to reproduce this document for their own use or the use of other Connectivity Standards Alliance members only, provided this notice is included. All other rights reserved. Duplication for sale, or for commercial or for-profit use is strictly prohibited without the prior written consent of the Connectivity Standards Alliance.

This page is intentionally blank

### **Connectivity Standards Alliance – Copyright Notice, License and Disclaimer**

Copyright © Connectivity Standards Alliance (2026). All Rights Reserved. The information within this document is the property of the Connectivity Standards Alliance and its use and disclosure are restricted, except as expressly set forth herein.

Connectivity Standards Alliance hereby grants you a fully-paid, non-exclusive, nontransferable, worldwide, limited and revocable license (without the right to sublicense), under Connectivity Standards Alliance's applicable copyright rights, to view, download, save, reproduce and use the document solely for your own internal purposes and in accordance with the terms of the license set forth herein. This license does not authorize you to, and you expressly warrant that you shall not: (a) permit others (outside your organization) to use this document; (b) post or publish this document; (c) modify, adapt, translate, or otherwise change this document in any manner or create any derivative work based on this document; (d) remove or modify any notice or label on this document, including this Copyright Notice, License and Disclaimer. The Connectivity Standards Alliance does not grant you any license hereunder other than as expressly stated herein.

Elements of this document may be subject to third party intellectual property rights, including without limitation, patent, copyright or trademark rights, and any such third party may or may not be a member of the Connectivity Standards Alliance. Connectivity Standards Alliance members grant other Connectivity Standards Alliance members certain intellectual property rights as set forth in the Connectivity Standards Alliance IPR Policy. Connectivity Standards Alliance members do not grant you any rights under this license. The Connectivity Standards Alliance is not responsible for, and shall not be held responsible in any manner for, identifying or failing to identify any or all such third party intellectual property rights. Please visit www.csaiot.org for more information on how to become a member of the Connectivity Standards Alliance.

This document and the information contained herein are provided on an "AS IS" basis and the Connectivity Standards Alliance DISCLAIMS ALL WARRANTIES EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO (A) ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OF THIRD PARTIES (INCLUDING WITHOUT LIMITATION ANY INTELLECTUAL PROPERTY RIGHTS INCLUDING PATENT, COPYRIGHT OR TRADEMARK RIGHTS); OR (B) ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE OR NONINFRINGEMENT. IN NO EVENT WILL THE CONNECTIVITY STANDARDS ALLIANCE BE LIABLE FOR ANY LOSS OF PROFITS, LOSS OF BUSINESS, LOSS OF USE OF DATA, INTERRUPTION OF BUSINESS, OR FOR ANY OTHER DIRECT, INDIRECT, SPECIAL OR EXEMPLARY, INCIDENTIAL, PUNITIVE OR CONSEQUENTIAL DAMAGES OF ANY KIND, IN CONTRACT OR IN TORT, IN CONNECTION WITH THIS DOCUMENT OR THE INFORMATION CONTAINED HEREIN, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH LOSS OR DAMAGE.

All company, brand and product names in this document may be trademarks that are the sole property of their respective owners.

This Copyright Notice, License and Disclaimer must be included on all copies of this document.

![](_page_2_Picture_9.jpeg)

This page is intentionally blank

# **Revision history**

| Revision | Date        | Details     | Editor |
|----------|-------------|-------------|--------|
| 1.0      | Jan<br>2026 | release 1.0 |        |

![](_page_4_Picture_4.jpeg)

This page is intentionally blank

# **Table of Contents**

Aliro Specification Test Plan v1.0

| 1 | Introduction                                            | 26 |
|---|---------------------------------------------------------|----|
|   | 1.1 Scope                                               | 26 |
|   | 1.2 Purpose                                             | 26 |
|   | 1.3 Provisional Status Notification                     | 26 |
| 2 | References                                              | 27 |
| 3 | Definitions                                             | 28 |
|   | 3.1 Acronyms                                            | 28 |
|   | 3.2 Glossary                                            | 28 |
|   | 3.3 Conformance Levels                                  | 28 |
| 4 | Test Setup                                              | 29 |
|   | 4.1 Architecture                                        | 29 |
|   | 4.1.1 PICS                                              | 29 |
| 5 | User Device Under Test Routines                         | 45 |
|   | 5.1 SELECT Routine                                      | 45 |
|   | 5.2 AUTH0 Routine                                       | 45 |
|   | 5.3 AUTH1 with SW Equal to 9000h Routine                | 46 |
|   | 5.4 AUTH1 with SW Not Equal to 9000h Routine            | 46 |
|   | 5.5 EXCHANGE Indicating Transaction Success Routine     | 47 |
|   | 5.6 EXCHANGE Indicating Transaction Failure Routine     | 47 |
|   | 5.7 CONTROL FLOW Indicating Transaction Failure Routine | 48 |
|   | 5.8 BLE+UWB Aliro Access Protocol Routine               | 48 |
|   | 5.9 BLE+UWB Ranging Session Setup Routine               | 49 |
|   | 5.10 BLE-Only Aliro Access Protocol Routine             | 49 |
| 6 | Reader Under Test Routines                              | 51 |
|   | 6.1 SELECT Routine                                      | 51 |
|   | 6.2 AUTH0 Routine                                       | 51 |
|   | 6.3 AUTH1 Routine                                       | 51 |
|   | 6.4 EXCHANGE Indicating Transaction Success Routine     | 52 |
|   | 6.5 EXCHANGE Indicating Transaction Failure Routine     | 52 |
|   | 6.6 CONTROL FLOW Indicating Transaction Failure Routine | 52 |

![](_page_6_Picture_4.jpeg)

|   | 6.7<br>BLE+UWB Aliro Access Protocol Routine 53                                                                              |
|---|------------------------------------------------------------------------------------------------------------------------------|
|   | 6.8<br>BLE+UWB Ranging Session Setup Routine 53                                                                              |
|   | 6.9<br>BLE-Only Aliro Access Protocol Routine 54                                                                             |
| 7 | User Device Under Test Conformance Tests 55                                                                                  |
|   | 7.1<br>Expedited Standard Phase without Reader Certificate 55                                                                |
|   | 7.2<br>Expedited Standard Phase with Reader Certificate in LOAD_CERT with APDU<br>Chaining 55                                |
|   | 7.3<br>Expedited Standard Phase with Reader Cert in LOAD_CERT without APDU<br>Chaining 57                                    |
|   | 7.4<br>Expedited Standard Phase with Reader Cert in AUTH1 with APDU Chaining 58                                              |
|   | 7.5<br>Expedited Standard Phase with Reader Cert in AUTH1 without APDU Chaining<br>58                                        |
|   | 7.6<br>Expedited Fast Phase 59                                                                                               |
|   | 7.7<br>Expedited Standard Phase with Sixteen Reader Group Identifiers bound to Single<br>Access Credential 60                |
|   | 7.8<br>Expedited Standard Phase with Reader Certificate in LOAD_CERT with Chaining<br>and incorrect Reader Cert signature 61 |
|   | 7.9<br>Expedited Standard Phase with Reader Certificate in LOAD_CERT with Chaining<br>and incorrect Reader Cert format 62    |
|   | 7.10Step-Up Phase with Access Document 63                                                                                    |
|   | 7.11Step-Up Phase with Revocation Document 64                                                                                |
|   | 7.12Step-Up Phase with Access Document and Revocation Document 65                                                            |
|   | 7.13SELECT Response with User Device Descriptor Tag (provisional) 66                                                         |
|   | 7.14AUTH0 Response with Chaining 67                                                                                          |
|   | 7.15AUTH0 with Unknown Reader Identifier 68                                                                                  |
|   | 7.16AUTH0 with unsupported Protocol Version 69                                                                               |
|   | 7.17AUTH0 with Extra Unknown TLV 69                                                                                          |
|   | 7.18AUTH0 with Wrong Value 70                                                                                                |
|   | 7.19AUTH0 with Wrong P1 and P2 71                                                                                            |
|   | 7.20AUTH0 with Chaining Not Completed 71                                                                                     |
|   | 7.21AUTH0 with Different Cryptogram in Consecutive Expedited Fast Phase 72                                                   |
|   | 7.22AUTH1 with Wrong Reader Signature 73                                                                                     |
|   | 7.23AUTH1 with Extra Tag 74                                                                                                  |
|   | 7.24AUTH1 with Wrong P1 and P2 74                                                                                            |
|   | 7.25AUTH1 with Wrong Values 75                                                                                               |

|   | 7.26AUTH1 with Incomplete Chaining76                                                          |  |
|---|-----------------------------------------------------------------------------------------------|--|
|   | 7.27EXCHANGE with Mailbox Read Request77                                                      |  |
|   | 7.28EXCHANGE with Mailbox Write Request77                                                     |  |
|   | 7.29EXCHANGE with Set Request79                                                               |  |
|   | 7.30EXCHANGE with Chaining80                                                                  |  |
|   | 7.31EXCHANGE with Extended Length81                                                           |  |
|   | 7.32EXCHANGE with Extra Tag82                                                                 |  |
|   | 7.33EXCHANGE with Mailbox Out of Bounds82                                                     |  |
|   | 7.34EXCHANGE with Wrong Length83                                                              |  |
|   | 7.35BLE+UWB Flow with Expedited Standard Phase84                                              |  |
|   | 7.36BLE+UWB Flow with Expedited Fast Phase85                                                  |  |
|   | 7.37BLE+UWB Flow with Step-Up Phase87                                                         |  |
|   | 7.38BLE+UWB Flow with UWB Ranging Suspend89                                                   |  |
|   | 7.39BLE+UWB Flow with UWB Ranging Resume91                                                    |  |
|   | 7.40BLE+UWB Flow with User Device Descriptor Tag (provisional)92                              |  |
|   | 7.41BLE+UWB Flow with wrong advertisement format93                                            |  |
|   | 7.42BLE+UWB Flow with Failed L2CAP93                                                          |  |
|   | 7.43BLE+UWB Flow with timeout before AUTH094                                                  |  |
|   | 7.44BLE+UWB Flow with Timeout Extension94                                                     |  |
|   | 7.45BLE+UWB Flow with URSK Not Found96                                                        |  |
|   | 7.46BLE+UWB Flow with M1 Message Mismatch Parameter96                                         |  |
|   | 7.47BLE+UWB Flow with M3 Message Mismatch Parameter97                                         |  |
|   | 7.48BLE+UWB Flow with Suspend Request Mismatch Parameter98                                    |  |
|   | 7.49BLE+UWB Flow with Resume Request Mismatch Parameter99                                     |  |
|   | 7.50BLE-Only Flow with Expedited Standard Phase (provisional)100                              |  |
|   | 7.51BLE-Only Flow with User Device Descriptor Tag (provisional)100                            |  |
|   | 7.52BLE-Only Flow with Failed L2CAP (provisional)101                                          |  |
| 8 | Reader Under Test Conformance Tests102                                                        |  |
|   | 8.1<br>Expedited Standard Phase without Reader Certificate102                                 |  |
|   | 8.2<br>Expedited Standard Phase with Reader Certificate in LOAD_CERT with APDU<br>Chaining102 |  |
|   | 8.3<br>Expedited Standard Phase with Reader Cert in LOAD_CERT without APDU<br>Chaining103     |  |
|   | 8.4<br>Expedited Standard Phase with Reader Cert in AUTH1 with APDU Chaining 104              |  |

| 8.5<br>Expedited Standard Phase with Reader Cert in AUTH1 without Chaining 105                      |
|-----------------------------------------------------------------------------------------------------|
| 8.6<br>Expedited Fast Phase 106                                                                     |
| 8.7<br>Step-Up Phase with Minimal Access Document with Key Identifier 107                           |
| 8.8<br>Step-Up Phase with Minimal Access Document with Issuer Certificate 108                       |
| 8.9<br>Step-Up Phase with Minimal Access Document with both Issuer Certificate and<br>Key ID 108    |
| 8.10Step-Up Phase with Access Document with AccessRule 109                                          |
| 8.11Step-Up Phase with Access Document with AccessRule using Schedules 109                          |
| 8.12Step-Up Phase with Access Document with Unknown NonAccessExtension 110                          |
| 8.13Step-Up Phase with Access Document with Unknown Non-Critical<br>AccessExtension 110             |
| 8.14Step-Up Phase with Access Document with No Issuer Certificate or Key ID 110                     |
| 8.15Step-Up Phase with Access Document with Issuer Certificate with Invalid<br>Signature 111        |
| 8.16Step-Up Phase with Access Document with Expired Issuer Certificate 111                          |
| 8.17Step-Up Phase with Access Document with Invalid Signature in IssuerAuth 112                     |
| 8.18Step-Up Phase with Access Document with Invalid Hash in IssuerAuth 112                          |
| 8.19Step-Up Phase with Access Document with Expired IssuerAuth 112                                  |
| 8.20Step-Up Phase with Access Document with Early IssuerAuth 113                                    |
| 8.21Step-Up Phase with Access Document with Issuer Certificate Time Mismatch113                     |
| 8.22Step-Up Phase with Access Document with ValidityIteration 113                                   |
| 8.23Step-Up Phase with Access Document with TimeVerificationRequired 114                            |
| 8.24Step-Up Phase with Access Document with No Data Elements 115                                    |
| 8.25Step-Up Phase with Access Document with IssuerAuth docType Mismatch 115                         |
| 8.26Step-Up Phase with Access Document with docType Not Aliro-a 115                                 |
| 8.27Step-Up Phase with Access Document with DeviceKeyInfo Mismatch 116                              |
| 8.28Step-Up Phase with Access Document with Invalid Access Data Element Version<br>116              |
| 8.29Step-Up Phase with Access Document with No AccessRule for Intended Reader<br>Action 117         |
| 8.30Step-Up Phase with Access Document with No Valid Schedule in AccessRule<br>AllowScheduleIds 117 |
| 8.31Step-Up Phase with Access Document with Valid Schedule in AccessRule<br>DenyScheduleIds 117     |
| 8.32Step-Up Phase with Access Document with Schedule in AccessRule and<br>TimeVerifyRequired 118    |

| 8.33Step-Up Phase with Access Document with Schedule in AccessRule with No<br>Reader Support118 |  |
|-------------------------------------------------------------------------------------------------|--|
| 8.34Step-Up Phase with Access Document with Unknown ReaderRule119                               |  |
| 8.35Step-Up Phase with Access Document with Unknown Critical AccessExtension<br>119             |  |
| 8.36Step-Up Phase with Revocation Document120                                                   |  |
| 8.37Step-Up Phase with Revocation Document with Invalid Revocation Document                     |  |
| Version121                                                                                      |  |
| 8.38SELECT Response with No Common Expedited Protocol Version122                                |  |
| 8.39AUTH0 with Extra Unknown TLV123                                                             |  |
| 8.40AUTH0 with Wrong Value124                                                                   |  |
| 8.41AUTH1 with Wrong User Device Signature124                                                   |  |
| 8.42AUTH1 with Extra Tag125                                                                     |  |
| 8.43AUTH1 with Wrong Values126                                                                  |  |
| 8.44EXCHANGE with Reader Descriptor Tag126                                                      |  |
| 8.45Control Flow with Reader Descriptor Tag127                                                  |  |
| 8.46BLE+UWB Flow with Reader Descriptor Tag128                                                  |  |
| 8.47EXCHANGE with Mailbox Command128                                                            |  |
| 8.48BLE+UWB Flow with Expedited Standard Phase129                                               |  |
| 8.49BLE+UWB Flow with Expedited Fast Phase131                                                   |  |
| 8.50BLE+UWB Flow with Step-Up Phase132                                                          |  |
| 8.51BLE+UWB Flow with UWB Ranging Suspend134                                                    |  |
| 8.52BLE+UWB Flow with UWB Ranging Resume135                                                     |  |
| 8.53BLE+UWB Flow with Failed L2CAP136                                                           |  |
| 8.54BLE+UWB Flow with wrong SPSM137                                                             |  |
| 8.55BLE+UWB Flow with timeout before AUTH0138                                                   |  |
| 8.56BLE+UWB Flow with Timeout Extension139                                                      |  |
| 8.57BLE+UWB Flow with M2 Message Mismatch Parameter140                                          |  |
| 8.58BLE+UWB Flow with M4 Message Mismatch Parameter141                                          |  |
| 8.59BLE+UWB Flow with Suspend Request Mismatch Parameter142                                     |  |
| 8.60BLE+UWB Flow BLE Advertisement Format142                                                    |  |
| 8.61BLE-only Flow – RKE Unsecure143                                                             |  |
| 8.62BLE-only Flow – RKE Secure143                                                               |  |
| 8.63BLE-Only Flow with Disallowed Expedited Fast Phase144                                       |  |
| 8.64BLE-Only Flow with Failed L2CAP144                                                          |  |

![](_page_10_Picture_3.jpeg)

| 8.65BLE-Only Flow with wrong SPSM 145    |  |
|------------------------------------------|--|
| 8.66BLE-Only Flow with Step-Up Phase 146 |  |

# **List of Figures**

Figure 4-1 Aliro Test Harness architecture ........................................................................29

![](_page_12_Picture_4.jpeg)

This page is intentionally blank

# **List of Tables**

| Table 4-1 Expedited-Standard phase PICS parameters29                              |  |
|-----------------------------------------------------------------------------------|--|
| Table 4-2 Expedited-Fast phase PICS parameters33                                  |  |
| Table 4-3 Expedited Phase PICS parameters34                                       |  |
| Table 4-4 Step-Up Phase PICS parameters36                                         |  |
| Table 4-5 Access Document processing PICS parameters38                            |  |
| Table 4-6 Revocation document processing PICS parameters41                        |  |
| Table 4-7 NFC interface PICS parameters41                                         |  |
| Table 4-8 BLE interface PICS parameters41                                         |  |
| Table 4-9 BLE + UWB interface PICS parameters for Bluetooth LE + UWB Aliro Flow42 |  |
| Table 4-10 BLE interface PICS parameters for BLE-Only Flow44                      |  |
| Table 5-1 SELECT routine45                                                        |  |
| Table 5-2 AUTH0 routine45                                                         |  |
| Table 5-3 AUTH1 with SW = 9000h routine46                                         |  |
| Table 5-4 AUTH1 with SW != 9000h routine46                                        |  |
| Table 5-5 EXCHANGE indicating transaction success routine47                       |  |
| Table 5-6 EXCHANGE indicating transaction failure routine47                       |  |
| Table 5-7 CONTROL FLOW indicating transaction failure routine48                   |  |
| Table 5-8 BLE+UWB Aliro Access Protocol routine48                                 |  |
| Table 5-9 BLE+UWB ranging session setup routine49                                 |  |
| Table 5-10 BLE-only Aliro Access Protocol routine49                               |  |
| Table 6-1 SELECT routine51                                                        |  |
| Table 6-2 AUTH0 routine51                                                         |  |
| Table 6-3 AUTH1 routine51                                                         |  |
| Table 6-4 EXCHANGE indicating transaction success routine52                       |  |
| Table 6-5 EXCHANGE indicating transaction failure routine52                       |  |
| Table 6-6 CONTROL FLOW indicating transaction failure routine52                   |  |
| Table 6-7 BLE+UWB Aliro Access Protocol routine53                                 |  |
| Table 6-8 BLE+UWB ranging session setup routine53                                 |  |
| Table 6-9 BLE-only Aliro Access Protocol routine54                                |  |
| Table 7-1 NFC_UD_STANDARD_NO_CERT test identifiers55                              |  |
| Table 7-2 NFC_UD_STANDARD_NO_CERT test pre-conditions55                           |  |
| Table 7-3 NFC_UD_STANDARD_NO_CERT test steps55                                    |  |

| Table 7-4 NFC_UD_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING test<br>identifiers 56                              |
|---------------------------------------------------------------------------------------------------------------|
| Table 7-5 NFC_UD_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING test<br>pre-conditions 56                           |
| Table 7-6 NFC_UD_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING test<br>steps 56                                    |
| Table 7-7 NFC_UD_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING test<br>identifiers 57                                |
| Table 7-8 NFC_UD_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING test<br>steps 57                                      |
| Table 7-9 NFC_UD_STANDARD_CERT_IN_AUTH1_WITH_CHAINING test<br>identifiers 58                                  |
| Table 7-10 NFC_UD_STANDARD_CERT_IN_AUTH1_WITH_CHAINING test steps58                                           |
| Table 7-11 NFC_UD_STANDARD_CERT_IN_AUTH1_NO_CHAINING test identifiers<br>58                                   |
| Table 7-12 NFC_UD_STANDARD_CERT_IN_AUTH1_NO_CHAINING test steps 59                                            |
| Table 7-13 NFC_UD_FAST test identifiers 59                                                                    |
| Table 7-14 NFC_UD_FAST test steps 60                                                                          |
| Table 7-15 NFC_UD_STANDARD_SIXTEEN_GROUPPIDENTIFIER_ONE_AC test<br>identifiers 60                             |
| Table 7-16 NFC_UD_STANDARD_SIXTEEN_GROUPPIDENTIFIER_ONE_AC test<br>pre-conditions 61                          |
| Table 7-17 NFC_UD_STANDARD_SIXTEEN_GROUPPIDENTIFIER_ONE_AC test<br>steps 61                                   |
| Table 7-18<br>NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCO<br>RRECT_SIGNATURE test identifiers 61 |
| Table 7-19<br>NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCO<br>RRECT_SIGNATURE test steps 62       |
| Table 7-20<br>NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCO<br>RRECT_FORMAT test identifiers 62    |
| Table 7-21<br>NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCO<br>RRECT_FORMAT test steps 63          |
| Table 7-22 NFC_UD_STEPUP_AD test identifiers 63                                                               |
| Table 7-23 NFC_UD_STEPUP_AD test pre-conditions 63                                                            |
| Table 7-24 NFC_UD_STEPUP_AD test steps 63                                                                     |

| Table 7-25 NFC_UD_STEPUP_RD test identifiers64                                             |  |
|--------------------------------------------------------------------------------------------|--|
| Table 7-26 NFC_UD_STEPUP_RD test pre-conditions64                                          |  |
| Table 7-27 NFC_UD_STEPUP_RD test steps65                                                   |  |
| Table 7-28 NFC_UD_STEPUP_AD_RD test identifiers65                                          |  |
| Table 7-29 NFC_UD_STEPUP_AD_RD test pre-conditions65                                       |  |
| Table 7-30 NFC_UD_STEPUP_AD_RD test steps66                                                |  |
| Table 7-31 NFC_UD_SELECT_RESPONSE_UD_DESCRIPTOR_TAG test identifiers66                     |  |
| Table 7-32 NFC_UD_SELECT_RESPONSE_UD_DESCRIPTOR_TAG test steps66                           |  |
| Table 7-33 NFC_UD_AUTH0_RESPONSE_CHAINING test identifiers67                               |  |
| Table 7-34 NFC_UD_AUTH0_RESPONSE_CHAINING test steps67                                     |  |
| Table 7-35 NFC_UD_NEG_AUTH0_UNKNOWN_READER_ID test identifiers68                           |  |
| Table 7-36 NFC_UD_NEG_AUTH0_UNKNOWN_READER_ID test pre-conditions68                        |  |
| Table 7-37 NFC_UD_NEG_AUTH0_UNKNOWN_READER_ID test steps68                                 |  |
| Table 7-38 NFC_UD_NEG_AUTH0_UNSUPPORTED_PROTOCOL_VERSION test<br>identifiers69             |  |
| Table 7-39 NFC_UD_NEG_AUTH0_UNSUPPORTED_PROTOCOL_VERSION test<br>steps69                   |  |
| Table 7-40 NFC_UD_NEG_AUTH0_EXTRA_TAG test identifiers69                                   |  |
| Table 7-41 NFC_UD_NEG_AUTH0_EXTRA_TAG test steps70                                         |  |
| Table 7-42 NFC_UD_NEG_AUTH0_WRONG_VALUE test identifiers70                                 |  |
| Table 7-43 NFC_UD_NEG_AUTH0_WRONG_VALUE test steps70                                       |  |
| Table 7-44 NFC_UD_NEG_AUTH0_WRONG_P1P2 test identifiers71                                  |  |
| Table 7-45 NFC_UD_NEG_AUTH0_WRONG_P1P2 test steps71                                        |  |
| Table 7-46 NFC_UD_NEG_AUTH0_CHAINING_NOT_COMPLETED test identifiers71                      |  |
| Table 7-47 NFC_UD_NEG_AUTH0_CHAINING_NOT_COMPLETED test steps72                            |  |
| Table 7-50<br>NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONSECUTIVE_FAST<br>test identifiers72 |  |
| Table 7-51<br>NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONSECUTIVE_FAST<br>test steps72       |  |
| Table 7-48 NFC_UD_NEG_AUTH1_WRONG_READER_SIGNATURE test identifiers<br>73                  |  |
| Table 7-49 NFC_UD_NEG_AUTH1_WRONG_READER_SIGNATURE test steps73                            |  |
| Table 7-52 NFC_UD_NEG_AUTH1_EXTRA_TAG test identifiers74                                   |  |
| Table 7-53 NFC_UD_NEG_AUTH1_EXTRA_TAG test steps74                                         |  |

![](_page_16_Picture_3.jpeg)

| Table 7-55 NFC_UD_NEG_AUTH1_WRONG_P1P2 test steps 75<br>Table 7-56 NFC_UD_NEG_AUTH1_WRONG_VALUES test identifiers 75<br>Table 7-57 NFC_UD_NEG_AUTH1_WRONG_VALUES test steps 75<br>Table 7-58 NFC_UD_NEG_AUTH1_CHAINING_NOT_COMPLTED test identifiers. 76 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| Table 7-59 NFC_UD_NEG_AUTH1_CHAINING_NOT_COMPLTED test steps 76                                                                                                                                                                                          |
| Table 7-60 NFC_UD_EXCHANGE_READ_REQUEST test identifiers 77                                                                                                                                                                                              |
| Table 7-61 NFC_UD_EXCHANGE_READ_REQUEST test pre-conditions 77                                                                                                                                                                                           |
| Table 7-62 NFC_UD_EXCHANGE_READ_REQUEST test steps 77                                                                                                                                                                                                    |
| Table 7-63 NFC_UD_EXCHANGE_WRITE_REQUEST test identifiers 77                                                                                                                                                                                             |
| Table 7-64 NFC_UD_EXCHANGE_WRITE_REQUEST test steps 78                                                                                                                                                                                                   |
| Table 7-65 NFC_UD_EXCHANGE_SET_REQUEST test identifiers 79                                                                                                                                                                                               |
| Table 7-66 NFC_UD_EXCHANGE_SET_REQUEST test steps 79                                                                                                                                                                                                     |
| Table 7-67 NFC_UD_EXCHANGE_WITH_CHAINING test identifiers 80                                                                                                                                                                                             |
| Table 7-68 NFC_UD_EXCHANGE_WITH_CHAINING test steps 80                                                                                                                                                                                                   |
| Table 7-69 NFC_UD_EXCHANGE_WITH_EXTENDED_LENGTH test identifiers 81                                                                                                                                                                                      |
| Table 7-70 NFC_UD_EXCHANGE_WITH_EXTENDED_LENGTH test steps 81                                                                                                                                                                                            |
| Table 7-71 NFC_UD_NEG_EXCHANGE_WITH_EXTRA_TAG test identifiers 82                                                                                                                                                                                        |
| Table 7-72 NFC_UD_NEG_EXCHANGE_WITH_EXTRA_TAG test steps 82                                                                                                                                                                                              |
| Table 7-73 NFC_UD_NEG_EXCHANGE_MAILBOX_OUT_OF_BOUNDS test<br>identifiers 82                                                                                                                                                                              |
| Table 7-74 NFC_UD_NEG_EXCHANGE_MAILBOX_OUT_OF_BOUNDS test steps83                                                                                                                                                                                        |
| Table 7-75 NFC_UD_NEG_EXCHANGE_WITH_WRONG_LENGTH test identifiers 83                                                                                                                                                                                     |
| Table 7-76 NFC_UD_NEG_EXCHANGE_WITH_WRONG_LENGTH test steps 84                                                                                                                                                                                           |
| Table 7-79 BLEUWB_UD_EXPEDITED_STANDARD_PHASE test identifiers 84                                                                                                                                                                                        |
| Table 7-80 BLEUWB_UD_EXPEDITED_STANDARD_PHASE test pre-conditions 84                                                                                                                                                                                     |
| Table 7-81 BLEUWB_UD_EXPEDITED_STANDARD_PHASE test steps 85                                                                                                                                                                                              |
| Table 7-82 BLEUWB_UD_EXPEDITED_FAST_PHASE test identifiers 85                                                                                                                                                                                            |
| Table 7-83 BLEUWB_UD_EXPEDITED_FAST_PHASE test steps 86                                                                                                                                                                                                  |
| Table 7-84 BLEUWB_UD_STEPUP_PHASE test steps 87                                                                                                                                                                                                          |
| Table 7-85 BLEUWB_UD_STEPUP_PHASE test pre-conditions 87                                                                                                                                                                                                 |
| Table 7-86 BLEUWB_UD_STEPUP_PHASE test steps 88                                                                                                                                                                                                          |
| Table 7-87 BLEUWB_UD_RANGING_SUSPEND test identifiers 89                                                                                                                                                                                                 |
| Table 7-88 BLEUWB_UD_RANGING_SUSPEND test steps 90                                                                                                                                                                                                       |

| Table 7-89 BLEUWB_UD_RANGING_RESUME test identifiers91                            |  |
|-----------------------------------------------------------------------------------|--|
| Table 7-90 BLEUWB_UD_RANGING_RESUME test steps91                                  |  |
| Table 7-91 BLEUWB_UD_UD_DESCRIPTOR_TAG test steps92                               |  |
| Table 7-92 BLEUWB_UD_NEG_WRONG_ADV test identifiers93                             |  |
| Table 7-93 BLEUWB_UD_NEG_WRONG_ADV test steps93                                   |  |
| Table 7-94 BLEUWB_UD_NEG_FAILED_L2CAP test identifiers93                          |  |
| Table 7-95 BLEUWB_UD_NEG_FAILED_L2CAP test steps93                                |  |
| Table 7-96 BLEUWB_UD_NEG_TIMEOUT_BEFORE_AUTH0 test identifiers94                  |  |
| Table 7-97 BLEUWB_UD_NEG_TIMEOUT_BEFORE_AUTH0 test steps94                        |  |
| Table 7-98 BLEUWB_UD_TIMEOUT_EXTENSION test identifiers94                         |  |
| Table 7-99 BLEUWB_UD_TIMEOUT_EXTENSION test steps95                               |  |
| Table 7-100 BLEUWB_UD_NEG_URSK_NOT_FOUND test identifiers96                       |  |
| Table 7-101 BLEUWB_UD_NEG_URSK_NOT_FOUND test steps96                             |  |
| Table 7-102 BLEUWB_UD_NEG_M1_MISMATCH_PARAMETER test identifiers96                |  |
| Table 7-103 BLEUWB_UD_NEG_M1_MISMATCH_PARAMETER test steps96                      |  |
| Table 7-104 BLEUWB_UD_NEG_M3_MISMATCH_PARAMETER test identifiers97                |  |
| Table 7-105 BLEUWB_UD_NEG_M3_MISMATCH_PARAMETER test steps98                      |  |
| Table 7-106 BLEUWB_UD_NEG_SUSPEND_MISMATCH_PARAMETER test<br>identifiers98        |  |
| Table 7-107 BLEUWB_UD_NEG_SUSPEND_MISMATCH_PARAMETER test steps99                 |  |
| Table 7-108 BLEUWB_UD_NEG_RESUME_MISMATCH_PARAMETER test<br>identifiers99         |  |
| Table 7-109 BLEUWB_UD_NEG_RESUME_MISMATCH_PARAMETER test steps .99                |  |
| Table 7-110 BLERKE_UD_EXPEDITED_STANDARD_PHASE test identifiers100                |  |
| Table 7-111 BLERKE_UD_EXPEDITED_STANDARD_PHASE test steps100                      |  |
| Table 7-112 BLERKE_UD_UD_DESCRIPTOR_TAG test identifiers100                       |  |
| Table 7-113 BLERKE_UD_UD_DESCRIPTOR_TAG test steps101                             |  |
| Table 7-114 BLERKE_UD_NEG_FAILED_L2CAP test identifiers101                        |  |
| Table 8-1 NFC_RDR_STANDARD_NO_CERT test identifiers102                            |  |
| Table 8-2 NFC_RDR_STANDARD_NO_CERT test pre-conditions102                         |  |
| Table 8-3 NFC_RDR_STANDARD_NO_CERT test steps102                                  |  |
| Table 8-4 NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING test<br>identifiers102 |  |
| Table 8-5 NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING test                   |  |

![](_page_18_Picture_3.jpeg)

| Table 8-6 NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING test<br>steps 103                  |
|-----------------------------------------------------------------------------------------------|
| Table 8-7 NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING test<br>identifiers 103              |
| Table 8-8 NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING test<br>steps 104                    |
| Table 8-9 NFC_RDR_STANDARD_CERT_IN_AUTH1_WITH_CHAINING test<br>identifiers 104                |
| Table 8-10 NFC_RDR_STANDARD_CERT_IN_AUTH1_WITH_CHAINING test steps<br>105                     |
| Table 8-11 NFC_RDR_STANDARD_CERT_IN_AUTH1_NO_CHAINING test steps105                           |
| Table 8-12 NFC_RDR_STANDARD_CERT_IN_AUTH1_NO_CHAINING test steps106                           |
| Table 8-13 NFC_RDR_FAST test identifiers 106                                                  |
| Table 8-14 NFC_RDR_FAST test steps 106                                                        |
| Table 8-15 NFC_RDR_STEPUP_AD_KEY_ID test identifiers 107                                      |
| Table 8-16 NFC_RDR_STEPUP_AD_KEY_ID test pre-conditions 107                                   |
| Table 8-17 NFC_RDR_STEPUP_AD_KEY_ID test steps 107                                            |
| Table 8-18 NFC_RDR_STEPUP_AD_ISSUER_CERT test identifiers 108                                 |
| Table 8-19 NFC_RDR_STEPUP_AD_ISSUER_CERT test pre-conditions 108                              |
| Table 8-20 NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID test identifiers 108                          |
| Table 8-21 NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID test pre-conditions 109                       |
| Table 8-22 NFC_RDR_STEPUP_AD_ACCESS_RULE test identifiers 109                                 |
| Table 8-23 NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES test identifiers109                        |
| Table 8-24 NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXTENSION test<br>identifiers 110             |
| Table 8-25 NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXTENSION test<br>pre-conditions 110          |
| Table 8-26<br>NFC_RDR_STEPUP_AD_UNKNOWN_NON_CRITICAL_ACCESS_EXTENSION<br>test identifiers 110 |
| Table 8-27 NFC_RDR_NEG_STEPUP_AD_NO_ISSUER_CERT_NO_KEY_ID test<br>identifiers 110             |
| Table 8-28 NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_INVALID_SIGNATURE<br>test identifiers 111        |
| Table 8-29 NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_EXPIRED test identifiers<br>111                  |
| Table 8-30 NFC_RDR_NEG_STEPUP_AD_INVALID_SIGNATURE_ISSUER_AUTH<br>test identifiers 112        |

| Table 8-31 NFC_RDR_NEG_STEPUP_AD_INVALID_HASH_ISSUER_AUTH test<br>identifiers112                |
|-------------------------------------------------------------------------------------------------|
| Table 8-32 NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH test identifiers<br>112                    |
| Table 8-33 NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH test identifiers113                          |
| Table 8-34<br>NFC_RDR_NEG_STEPUP_AD_ISSUER_CERTIFICATE_TIME_MISMATCH test<br>identifiers113     |
| Table 8-35 NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION test identifiers113                         |
| Table 8-36 NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION test steps114                               |
| Table 8-37 NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION test<br>iterations114                       |
| Table 8-38 NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQUIRED test<br>identifiers114              |
| Table 8-39 NFC_RDR_NEG_STEPUP_AD_NO_DATA_ELEMENTS test identifiers115                           |
| Table 8-40 NFC_RDR_NEG_STEPUP_AD_ISSUER_DOCTYPE_MISMATCH test<br>identifiers115                 |
| Table 8-41 NFC_RDR_NEG_STEPUP_AD_DEVICE_KEY_INFO_MISMATCH test<br>identifiers116                |
| Table 8-42<br>NFC_RDR_NEG_STEPUP_AD_INVALID_ACCESS_DATA_ELEMENT_VERSIO<br>N test identifiers116 |
| Table 8-43<br>NFC_RDR_NEG_STEPUP_AD_NO_ACCESS_RULE_FOR_READER_ACTION<br>test identifiers117     |
| Table 8-44<br>NFC_RDR_NEG_STEPUP_AD_NO_VALID_SCHEDULE_ALLOW_SCHEDULEI<br>D test identifiers117  |
| Table 8-45<br>NFC_RDR_NEG_STEPUP_AD_VALID_SCHEDULE_DENY_SCHEDULEID test<br>identifiers117       |
| Table 8-46 NFC_RDR_NEG_STEPUP_AD_SCHEDULE_TIME_VERIFY_REQUIRED<br>test identifiers118           |
| Table 8-47<br>NFC_RDR_NEG_STEPUP_AD_SCHEDULE_IN_ACCESS_RULE_AND_READE<br>R test identifiers118  |
| Table 8-48 NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE test<br>identifiers119                     |
| Table 8-49 NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE test pre<br>conditions119                  |

![](_page_20_Picture_3.jpeg)

| Table 8-50<br>NFC_RDR_NEG_STEPUP_AD_UNKNOWN_CRITICAL_ACCESS_EXTENSION                           |
|-------------------------------------------------------------------------------------------------|
| test identifiers 119                                                                            |
| Table 8-51 NFC_RDR_STEPUP_RD test identifiers 120                                               |
| Table 8-52 NFC_RDR_STEPUP_RD test pre-conditions 120                                            |
| Table 8-53 NFC_RDR_STEPUP_RD test steps 120                                                     |
| Table 8-54 NFC_RDR_STEPUP_RD test iterations 121                                                |
| Table 8-55 NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSION test<br>identifiers 121                |
| Table 8-56 NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSION test steps                             |
| 122                                                                                             |
| Table 8-57<br>NFC_RDR_NEG_SEL_RSP_NO_COMMON_EXPEDITED_PROTOCOL_VERSIO<br>N test identifiers 122 |
| Table 8-58<br>NFC_RDR_NEG_SEL_RSP_NO_COMMON_EXPEDITED_PROTOCOL_VERSIO<br>N test steps 123       |
| Table 8-59 NFC_RDR_NEG_AUTH0_EXTRA_TAG test identifiers 123                                     |
| Table 8-60 NFC_RDR_NEG_AUTH0_EXTRA_TAG test steps 124                                           |
| Table 8-61 NFC_RDR_NEG_AUTH0_WRONG_VALUE test identifiers 124                                   |
| Table 8-62 NFC_RDR_NEG_AUTH0_WRONG_VALUE test steps 124                                         |
| Table 8-63 NFC_RDR_NEG_AUTH1_WRONG_UD_SIGNATURE test identifiers 124                            |
| Table 8-64 NFC_RDR_NEG_AUTH1_WRONG_UD_SIGNATURE test steps 125                                  |
| Table 8-65 NFC_RDR_NEG_AUTH1_EXTRA_TAG test identifiers 125                                     |
| Table 8-66 NFC_RDR_NEG_AUTH1_EXTRA_TAG test steps 125                                           |
| Table 8-67 NFC_RDR_NEG_AUTH1_WRONG_VALUES test identifiers 126                                  |
| Table 8-68 NFC_RDR_NEG_AUTH1_WRONG_VALUES test steps 126                                        |
| Table 8-69 NFC_RDR_EXCHANGE_RDR_DESCRIPTOR_TAG test identifiers 126                             |
| Table 8-70 NFC_RDR_EXCHANGE_RDR_DESCRIPTOR_TAG test steps 126                                   |
| Table 8-71 NFC_RDR_CONTROL_FLOW_RDR_DESCRIPTOR_TAG test steps 127                               |
| Table 8-72 BLEUWB_RDR_CONTROL_FLOW_RDR_DESCRIPTOR_TAG test                                      |
| identifiers 128                                                                                 |
| Table 8-73 BLEUWB_RDR_CONTROL_FLOW_RDR_DESCRIPTOR_TAG test steps<br>128                         |
| Table 8-74 NFC_RDR_EXCHANGE_MAILBOX test identifiers 129                                        |
| Table 8-75 NFC_RDR_EXCHANGE_MAILBOX test pre-conditions 129                                     |
| Table 8-76 NFC_RDR_EXCHANGE_MAILBOX test steps 129                                              |

| Table 8-77 BLEUWB_RDR_EXPEDITED_STANDARD_PHASE test identifiers129           |  |
|------------------------------------------------------------------------------|--|
| Table 8-78 BLEUWB_RDR_EXPEDITED_STANDARD_PHASE test pre-conditions130        |  |
| Table 8-79 BLEUWB_RDR_EXPEDITED_STANDARD_PHASE test steps130                 |  |
| Table 8-80 BLEUWB_RDR_EXPEDITED_FAST_PHASE test identifiers131               |  |
| Table 8-81 BLEUWB_RDR_EXPEDITED_FAST_PHASE test steps131                     |  |
| Table 8-82 BLEUWB_RDR_STEPUP_PHASE test identifiers132                       |  |
| Table 8-83 BLEUWB_RDR_STEPUP_PHASE test pre-conditions133                    |  |
| Table 8-84 BLEUWB_RDR_STEPUP_PHASE test steps133                             |  |
| Table 8-85 BLEUWB_RDR_RANGING_SUSPEND test identifiers134                    |  |
| Table 8-86 BLEUWB_RDR_RANGING_SUSPEND test steps135                          |  |
| Table 8-87 BLEUWB_RDR_RANGING_RESUME test steps136                           |  |
| Table 8-88 BLEUWB_RDR_NEG_FAILED_L2CAP test identifiers136                   |  |
| Table 8-89 BLEUWB_RDR_NEG_FAILED_L2CAP test steps137                         |  |
| Table 8-90 BLEUWB_RDR_NEG_FAILED_SPSM_L2CAP test identifiers137              |  |
| Table 8-91 BLEUWB_RDR_NEG_FAILED_SPSM_L2CAP test steps137                    |  |
| Table 8-92 BLEUWB_RDR_NEG_TIMEOUT_BEFORE_AUTH0 test identifiers138           |  |
| Table 8-93 BLEUWB_RDR_NEG_TIMEOUT_BEFORE_AUTH0 test steps138                 |  |
| Table 8-94 BLEUWB_RDR_TIMEOUT_EXTENSION test identifiers139                  |  |
| Table 8-95 BLEUWB_RDR_TIMEOUT_EXTENSION test steps139                        |  |
| Table 8-96 BLEUWB_RDR_NEG_M2_MISMATCH_PARAMETER test identifiers .140        |  |
| Table 8-97 BLEUWB_RDR_NEG_M2_MISMATCH_PARAMETER test steps140                |  |
| Table 8-98 BLEUWB_RDR_NEG_M4_MISMATCH_PARAMETER test identifiers .141        |  |
| Table 8-99 BLEUWB_RDR_NEG_M4_MISMATCH_PARAMETER test steps141                |  |
| Table 8-100 BLEUWB_RDR_NEG_SUSPEND_MISMATCH_PARAMETER test<br>identifiers142 |  |
| Table 8-101 BLEUWB_RDR_NEG_SUSPEND_MISMATCH_PARAMETER test steps<br>142      |  |
| Table 8-102 BLEUWB_RDR_ADVERTISEMENT_FORMAT test identifiers142              |  |
| Table 8-103 BLEUWB_RDR_ADVERTISEMENT_FORMAT test steps142                    |  |
| Table 8-104 BLERKE_RDR_UNSECURE test identifiers143                          |  |
| Table 8-105 BLERKE_RDR_UNSECURE test steps143                                |  |
| Table 8-106 BLERKE_RDR_SECURE test identifiers143                            |  |
| Table 8-107 BLERKE_RDR_SECURE test steps144                                  |  |
| Table 8-108 BLERKE_RDR_NEG_FAST test identifiers144                          |  |

![](_page_22_Picture_3.jpeg)

| Table 8-109 BLERKE_RDR_NEG_FAST test steps 144                    |  |
|-------------------------------------------------------------------|--|
| Table 8-110 BLERKE_RDR_NEG_FAILED_L2CAP test identifiers 144      |  |
| Table 8-111 BLERKE_RDR_NEG_FAILED_L2CAP test steps 145            |  |
| Table 8-112 BLERKE_RDR_NEG_FAILED_SPSM_L2CAP test identifiers 145 |  |
| Table 8-113 BLERKE_RDR_NEG_FAILED_SPSM_L2CAP test steps 145       |  |
| Table 8-114 BLERKE_RDR_STEPUP_PHASE test identifiers 146          |  |
| Table 8-115 BLERKE_RDR_STEPUP_PHASE test steps 146                |  |

![](_page_24_Picture_2.jpeg)

# **1 Introduction**

### **1.1 Scope**

This test plan covers the tests for Aliro 1.0.

# **1.2 Purpose**

Describes tests to be performed for supported Aliro 1.0 features.

### **1.3 Provisional Status Notification**

This section exists to inform of the results implications of the validation process on technical specification. As per Connectivity Standards Alliance Policies & Procedures, the following items are marked as provisional based on the results of the Aliro Standard Validation Event resolution.

- [Optional] User Device test as in 7.13 Select Response with User Device Descriptor Tag
- [Optional] User Device test as in 7.40 BLE+UWB Flow with User Device Descriptor Tag
- [Optional] User Device test as in 7.50 BLE-Only Flow with Expedited Standard Phase
- [Optional] User Device test as in 7.51 BLE-Only Flow with User Device Descriptor Tag
- [Optional] User Device test as in 7.52 BLE-Only Flow with Failed L2CAP

![](_page_25_Picture_14.jpeg)

# **2 References**

[1] ALIRO Specification Version 0.9.0

![](_page_26_Picture_4.jpeg)

# **3 Definitions**

### **3.1 Acronyms**

The acronyms are defined in Aliro 1.0 [1].

**3.2 Glossary** 

Access Credential A set of information that contains all data necessary to

perform the access transaction, this includes the Access Credential key pair and an optional Access Document.

Access Data Element Standardized structure to define access information.

Access Document Issued by a Credential Issuer. Contains Access Data

Elements and the Access Credential public key.

Access ManagerA manager used to determine whether access should be

granted and actuate locking mechanisms. An Access

Manager may be embedded in the Reader.

Credential IssuerIssuer of the Access Credential.

Reader A reader device to read an Access Credential from a User

Device and optionally send Access Credential information to

an Access Manager.

Reader System Issuer Issuer of the Reader.

Revocation Data Element Standardized structure to define revocation information

Revocation Document Issued by the Credential Issuer. Contains revocation data

elements.

User DeviceA portable device containing one or more access credentials

E.g., card, fob, tag, key, mobile phone, smartwatch etc.

### **3.3 Conformance Levels**

The key word meaning is defined in Aliro 1.0 [1].

![](_page_27_Picture_26.jpeg)

# **4 Test Setup**

### **4.1 Architecture**

Figure 4-1 provides a detailed illustration of the Aliro Test Harness. This system is designed to execute test scripts that align with the test plan. Within this setup, the Aliro Actuator represents the implementation of the Aliro technical specifications.

The Test Harness is built around the Raspberry Pi development platform. It interfaces with various external platforms: UWB, BLE, and NFC. Specifically, it employs the NXP Murata SR150 UWB platform, which is connected via a USB interface using UCI-PnP. For NFC operations, the Test Harness utilizes the NXP PN7160 Reader/Card Emulation NFC platform, connected through an SPI or I2C interface, depending on the model of the NFC platform. The Bluetooth LE in the Murata board is used and not the the Raspberry Pi's built-in Bluetooth module for the performance purposes.

The Test Harness communicates wirelessly with the Device Under Test (DUT) using the Aliro Protocol.

![](_page_28_Figure_7.jpeg)

**Figure 4-1 Aliro Test Harness architecture** 

# **4.1.1 PICS**

In this section the PICS parameter requirements for Reader and User Device are enumerated. 'M' implies mandatory feature, 'O' implies optional feature, 'C' implies conditional feature, and 'NA' implies feature Not Applicable for the purposes of tests. PICS parameter with a corresponding empty cell implies no test is defined.

| PICS<br>Parameter              | Re<br>ad<br>er | Us<br>er<br>De<br>vi<br>ce | Reader Test Identifier                                                                                                                            | User Device Test Identifier                                                                                                                                                                    |
|--------------------------------|----------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Expedited<br>Standard<br>Phase | M              | M                          | NFC_RDR_STANDARD_NO_CER<br>T,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING, | NFC_UD_STANDARD_NO_CERT,<br>NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,<br>NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING, |

**Table 4-1 Expedited-Standard phase PICS parameters** 

![](_page_28_Picture_13.jpeg)

| PICS<br>Parameter                                                                                                             | Re<br>ad<br>er | Us<br>er<br>De<br>vi<br>ce | Reader Test Identifier                                                                                                                                                                                                                                                                                                                                                     | User Device Test Identifier                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------|----------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                               |                |                            | NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING,<br>NFC_RDR_NEG_SEL_RSP_NO_C<br>OMMON_EXPEDITED_PROTOC<br>OL_VERSION,<br>NFC_RDR_NEG_AUTH0_EXTRA<br>_TAG,<br>NFC_RDR_NEG_AUTH0_WRON<br>G_VALUE,<br>NFC_RDR_NEG_AUTH1_WRON<br>G_UD_SIGNATURE,<br>NFC_RDR_NEG_AUTH1_EXTRA<br>_TAG,<br>NFC_RDR_NEG_AUTH1_WRON<br>G_VALUES | NFC_UD_AUTH0_RESPONSE_CHAINING,<br>NFC_UD_NEG_AUTH0_UNKNOWN_REA<br>DER_ID,<br>NFC_UD_NEG_AUTH0_UNSUPPORTED_<br>PROTOCOL_VERSION,<br>NFC_UD_NEG_AUTH0_EXTRA_TAG,<br>NFC_UD_NEG_AUTH0_WRONG_VALUE,<br>NFC_UD_NEG_AUTH0_WRONG_P1P2,<br>NFC_UD_NEG_AUTH0_CHAINING_NOT_<br>COMPLETED,<br>NFC_UD_NEG_AUTH1_WRONG_READE<br>R_SIGNATURE,<br>NFC_UD_NEG_AUTH1_EXTRA_TAG,<br>NFC_UD_NEG_AUTH1_WRONG_P1P2,<br>NFC_UD_NEG_AUTH1_WRONG_VALUE<br>S |
| Reader<br>signature<br>generation<br>and<br>validation<br>using<br>reader_Pub<br>K                                            | M              | M                          | NFC_RDR_STANDARD_NO_CER<br>T                                                                                                                                                                                                                                                                                                                                               | NFC_UD_STANDARD_NO_CERT,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING                                                                                                                                                                                                                                                                                                                                                            |
| Reader<br>signature<br>generation<br>and<br>validation<br>using<br>intermediat<br>e_reader_P<br>ubK (from<br>reader_Cer<br>t) | M              | M                          | NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING                                                                                                                                                    | NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,<br>NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING                                                                                                                                                                                                                  |
| Device<br>signature<br>generation<br>and<br>validation                                                                        | M              | M                          | NFC_RDR_STANDARD_NO_CER<br>T,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING,                                                                                                                                                                                                                          | NFC_UD_STANDARD_NO_CERT,<br>NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,                                                                                                                                                                                                                                                                                           |

| PICS                                                                                                                         | Re       | Us                   | Reader Test Identifier                            | User Device Test Identifier                                                                                 |  |  |
|------------------------------------------------------------------------------------------------------------------------------|----------|----------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--|--|
| Parameter                                                                                                                    | ad<br>er | er<br>De<br>vi<br>ce |                                                   |                                                                                                             |  |  |
|                                                                                                                              |          |                      | NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING, | NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,                                                            |  |  |
|                                                                                                                              |          |                      | NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING    | NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING                                                               |  |  |
| Verificatio<br>n of                                                                                                          | N<br>A   | M                    | NA                                                | NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,                                                    |  |  |
| reader_Cer<br>t with the                                                                                                     |          |                      |                                                   | NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,                                                          |  |  |
| CA public<br>key                                                                                                             |          |                      |                                                   | NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,                                                            |  |  |
|                                                                                                                              |          |                      |                                                   | NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING,                                                              |  |  |
|                                                                                                                              |          |                      |                                                   | NFC_UD_NEG_STANDARD_CERT_IN_LO<br>AD_CERT_WITH_CHAINING_INCORREC<br>T_SIGNATURE,                            |  |  |
|                                                                                                                              |          |                      |                                                   | NFC_UD_NEG_STANDARD_CERT_IN_LO<br>AD_CERT_WITH_CHAINING_INCORREC<br>T_FORMAT                                |  |  |
| Verificatio<br>n of<br>reader_Cer<br>t with the<br>CA public<br>key –<br>reader_Cer<br>t<br>expiration<br>time<br>validation | N<br>A   | O                    | NA                                                |                                                                                                             |  |  |
| Lookup of<br>the reader<br>key<br>through<br>reader_gro<br>up_identifi<br>er                                                 | N<br>A   | M                    | NA                                                | NFC_UD_STANDARD_NO_CERT,<br>NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G                         |  |  |
| Lookup of<br>reader CA<br>public key<br>through<br>reader_gro                                                                | N<br>A   | M                    | NA                                                | NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING |  |  |

![](_page_30_Picture_3.jpeg)

| PICS<br>Parameter                                                                          | Re<br>ad<br>er | Us<br>er<br>De<br>vi<br>ce | Reader Test Identifier                                                                                                                                                                                                                                   | User Device Test Identifier                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------|----------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| up_identifi<br>er                                                                          |                |                            |                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                 |
| Presentatio<br>n and<br>validation<br>of<br>reader_Cer<br>t                                | M              | M                          | NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING                                  | NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,<br>NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING                             |
| Presentatio<br>n and<br>validation<br>of<br>reader_Cer<br>t in<br>AUTH1<br>command         | C              | M                          | NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING                                                                                                                                                      | NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING                                                                                                                                               |
| Presentatio<br>n and<br>validation<br>of<br>reader_Cer<br>t in<br>LOAD_CE<br>RT<br>command | C              | M                          | NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING                                                                                                                                          | NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING                                                                                                                                   |
| AUTH1<br>command<br>command_<br>parameter                                                  | M              | M                          | NFC_RDR_STANDARD_NO_CER<br>T,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING | NFC_UD_STANDARD_NO_CERT,<br>NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,<br>NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING |
| AUTH1<br>command                                                                           | C              | M                          | NFC_RDR_STANDARD_NO_CER<br>T,                                                                                                                                                                                                                            | NFC_UD_STANDARD_NO_CERT,                                                                                                                                                                                                                        |

| PICS<br>Parameter                                                                 | Re<br>ad<br>er | Us<br>er<br>De<br>vi<br>ce | Reader Test Identifier                                                                                                                                                                                                                                   | User Device Test Identifier                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------|----------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| command_<br>parameter<br>– key slot                                               |                |                            | NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING                                  | NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,<br>NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING                             |
| AUTH1<br>command<br>command_<br>parameter<br>– Access<br>Credential<br>Public Key | C              | M                          | NFC_RDR_STANDARD_NO_CER<br>T,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_WITH_CHAINING<br>,<br>NFC_RDR_STANDARD_CERT_IN<br>_LOAD_CERT_NO_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN<br>_AUTH1_NO_CHAINING | NFC_UD_STANDARD_NO_CERT,<br>NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_CHAININ<br>G,<br>NFC_UD_STANDARD_CERT_IN_LOAD_C<br>ERT_NO_CHAINING,<br>NFC_UD_STANDARD_CERT_IN_AUTH1_<br>WITH_CHAINING,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAINING |
| Subset of<br>mailbox in<br>AUTH1<br>command<br>response                           | N<br>A         | M                          | NA                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                 |

### **Table 4-2 Expedited-Fast phase PICS parameters**

| PICS<br>Parameter                                      | Read<br>er | User<br>Devi<br>ce | Reader Test<br>Identifier | User Device Test Identifier                                                |
|--------------------------------------------------------|------------|--------------------|---------------------------|----------------------------------------------------------------------------|
| Expedite<br>d-Fast<br>Phase                            | O          | O                  | NFC_RDR_F<br>AST          | NFC_UD_FAST,<br>NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONS<br>ECUTIVE_FAST |
| Cryptogr<br>am<br>generatio<br>n and<br>validatio<br>n | M          | M                  | NFC_RDR_F<br>AST          | NFC_UD_FAST,<br>NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONS<br>ECUTIVE_FAST |

![](_page_32_Picture_5.jpeg)

# **Table 4-3 Expedited Phase PICS parameters**

| PICS Parameter                                                                  | Re<br>ade<br>r | Us<br>er<br>De<br>vic<br>e | Reader Test Identifier                                                                                    | User Device Test Identifier                                                                                                                                                                        |  |  |
|---------------------------------------------------------------------------------|----------------|----------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| Command<br>chaining                                                             | M              | M                          | NFC_RDR_STANDARD_CERT_IN_<br>LOAD_CERT_WITH_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN_<br>AUTH1_WITH_CHAINING | NFC_UD_STANDARD_<br>CERT_IN_LOAD_CERT_WITH_C<br>HAINING,<br>NFC_UD_STANDARD_CERT_IN_<br>AUTH1_WITH_CHAINING,<br>NFC_UD_AUTH0_RESPONSE_CH<br>AINING,<br>NFC_UD_NEG_AUTH1_CHAININ<br>G_NOT_COMPLTED, |  |  |
| Extended<br>length                                                              | O              | O                          | NFC_RDR_STANDARD_CERT_IN_<br>LOAD_CERT_NO_CHAINING,<br>NFC_RDR_STANDARD_CERT_IN_<br>AUTH1_NO_CHAINING     | NFC_UD_STANDARD_CERT_IN_<br>LOAD_CERT_NO_CHAINING,<br>NFC_UD_STANDARD_<br>CERT_IN_AUTH1_NO_CHAININ<br>G,<br>NFC_UD_EXCHANGE_WITH_EX<br>TENDED_LENGTH                                               |  |  |
| User<br>authentication<br>policy<br>enforcement                                 | N<br>A         | M                          | NA                                                                                                        | NFC_UD_STANDARD_NO_CERT                                                                                                                                                                            |  |  |
| Support for<br>credential_sign<br>ed_timestamp<br>in<br>AUTH0/AUT<br>H1         | N<br>A         | M                          |                                                                                                           |                                                                                                                                                                                                    |  |  |
| Support for<br>revocation_sig<br>ned_timestamp<br>in<br>AUTH0/AUT<br>H1         | N<br>A         | M                          |                                                                                                           |                                                                                                                                                                                                    |  |  |
| Allow at least<br>16<br>reader_group_i<br>dentifier per<br>Access<br>Credential | N<br>A         | M                          | NA                                                                                                        | NFC_UD_STANDARD_SIXTEEN_<br>GROUPPIDENTIFIER_ONE_AC                                                                                                                                                |  |  |

| PICS Parameter                                                                                                        | Re<br>ade<br>r | Us<br>er<br>De<br>vic<br>e | Reader Test Identifier   | User Device Test Identifier                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------|----------------|----------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------|
| User Device<br>has a method to<br>use all Access<br>Credentials<br>bound to the<br>reader<br>identifier               | N<br>A         | M                          | NA                       |                                                                                                                            |
| EXCHANGE<br>command                                                                                                   | M              | M                          |                          | NFC_UD_EXCHANGE_WITH_CH<br>AINING,<br>NFC_UD_NEG_EXCHANGE_WIT<br>H_EXTRA_TAG,<br>NFC_UD_NEG_EXCHANGE_WIT<br>H_WRONG_LENGTH |
| EXCHANGE<br>command –<br>notify<br>credential<br>issuer in<br>EXCHANGE                                                | O              | O                          |                          |                                                                                                                            |
| EXCHANGE<br>command –<br>notify bound<br>application in<br>EXCHANGE                                                   | O              | O                          |                          |                                                                                                                            |
| EXCHANGE<br>command –<br>Update<br>document in<br>EXCHANGE                                                            | O              | O                          |                          |                                                                                                                            |
| EXCHANGE<br>command –<br>Update<br>document in<br>EXCHANGE –<br>providing and<br>processing<br>update_doc<br>contents | N<br>A         | N<br>A                     | NA                       | NA                                                                                                                         |
| Mailbox                                                                                                               | O              | M                          | NFC_RDR_EXCHANGE_MAILBOX | NFC_UD_EXCHANGE_SET_REQ<br>UEST,                                                                                           |

| PICS Parameter                                   | Re<br>ade<br>r | Us<br>er<br>De<br>vic<br>e | Reader Test Identifier                                                                                                                                                                 | User Device Test Identifier                                                                                          |
|--------------------------------------------------|----------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|                                                  |                |                            |                                                                                                                                                                                        | NFC_UD_NEG_EXCHANGE_MAI<br>LBOX_OUT_OF_BOUNDS                                                                        |
| Mailbox<br>Read/Write by<br>credential<br>issuer | N<br>A         | N<br>A                     | NA                                                                                                                                                                                     | NA                                                                                                                   |
| Read from<br>Mailbox                             | O              | M                          |                                                                                                                                                                                        | NFC_UD_EXCHANGE_READ_RE<br>QUEST                                                                                     |
| Write to<br>Mailbox                              | O              | M                          |                                                                                                                                                                                        | NFC_UD_EXCHANGE_WRITE_R<br>EQUEST                                                                                    |
| Reader<br>Descriptor tag                         | O              | N<br>A                     | NFC_RDR_EXCHANGE_RDR_DES<br>CRIPTOR_TAG,<br>NFC_RDR_EXCHANGE_RDR_DES<br>CRIPTOR_TAG,<br>NFC_RDR_CONTROL_FLOW_RDR<br>_DESCRIPTOR_TAG,<br>BLEUWB_RDR_CONTROL_FLOW_<br>RDR_DESCRIPTOR_TAG | NA                                                                                                                   |
| User Device<br>Descriptor Tag                    | N<br>A         | O                          | NA                                                                                                                                                                                     | NFC_UD_SELECT_RESPONSE_U<br>D_DESCRIPTOR_TAG,<br>BLEUWB_UD_UD_DESCRIPTOR<br>_TAG,<br>BLERKE_UD_UD_DESCRIPTOR_<br>TAG |

### **Table 4-4 Step-Up Phase PICS parameters**

| PICS<br>Paramete<br>r | Read<br>er | User<br>Devi<br>ce | Reader Test Identifier                                       | User Device Test<br>Identifier |
|-----------------------|------------|--------------------|--------------------------------------------------------------|--------------------------------|
| Step-Up               | O          | M                  | NFC_RDR_STEPUP_AD_KEY_ID,                                    | NFC_UD_STEPU                   |
| phase                 |            |                    | NFC_RDR_STEPUP_AD_ISSUER_CERT,                               | P_AD,                          |
|                       |            |                    | NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID,                        | NFC_UD_STEPU<br>P_RD           |
|                       |            |                    | NFC_RDR_STEPUP_AD_ACCESS_RULE,                               |                                |
|                       |            |                    | NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES,                     |                                |
|                       |            |                    | NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXT<br>ENSION,          |                                |
|                       |            |                    | NFC_RDR_STEPUP_AD_UNKNOWN_NON_CRITICAL_AC<br>CESS_EXTENSION, |                                |
|                       |            |                    | NFC_RDR_NEG_STEPUP_AD_NO_ISSUER_CERT_NO_KE<br>Y_ID,          |                                |

| PICS                                   | Read | User       | Reader Test Identifier                                         | User Device Test     |
|----------------------------------------|------|------------|----------------------------------------------------------------|----------------------|
| Paramete<br>r                          | er   | Devi<br>ce |                                                                | Identifier           |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_INVALID_SI<br>GNATURE,       |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED,                    |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_INVALID_SIGNATURE_ISS<br>UER_AUTH,       |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_INVALID_HASH_ISSUER_A<br>UTH,            |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH,                     |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH,                       |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERTIFICATE_TI<br>ME_MISMATCH,    |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION,                      |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQ<br>UIRED,          |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_NO_DATA_ELEMENTS,                        |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_ISSUER_DOCTYPE_MISMA<br>TCH,             |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_DEVICE_KEY_INFO_MISM<br>ATCH,            |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_INVALID_ACCESS_DATA_<br>ELEMENT_VERSION, |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_NO_ACCESS_RULE_FOR_R<br>EADER_ACTION,    |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_NO_VALID_SCHEDULE_AL<br>LOW_SCHEDULEID,  |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_VALID_SCHEDULE_DENY_<br>SCHEDULEID,      |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_TIME_VERIFY<br>_REQUIRED,       |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_IN_ACCESS_R<br>ULE_AND_READER,  |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RUL<br>E,                 |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_CRITICAL_AC<br>CESS_EXTENSION,   |                      |
|                                        |      |            | NFC_RDR_STEPUP_RD,                                             |                      |
|                                        |      |            | NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERS<br>ION              |                      |
| Step-Up<br>phase –<br>Access<br>docume | O    | M          | NFC_RDR_STEPUP_AD_KEY_ID                                       | NFC_UD_STEPU<br>P_AD |
| nt<br>storage                          |      |            |                                                                |                      |

![](_page_36_Picture_3.jpeg)

| PICS<br>Paramete<br>r                                                               | Read<br>er | User<br>Devi<br>ce | Reader Test Identifier                                                  | User Device Test<br>Identifier |
|-------------------------------------------------------------------------------------|------------|--------------------|-------------------------------------------------------------------------|--------------------------------|
| and<br>retrieval                                                                    |            |                    |                                                                         |                                |
| Step-Up<br>phase –<br>Revocat<br>ion<br>docume<br>nt<br>storage<br>and<br>retrieval | O          | M                  | NFC_RDR_STEPUP_RD,<br>NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERS<br>ION | NFC_UD_STEPU<br>P_RD           |

# **Table 4-5 Access Document processing PICS parameters**

| PICS<br>Parameter | Read<br>er | User<br>Devi<br>ce | Reader Test Identifier                                         | User<br>Device<br>Test<br>Identifi<br>er |
|-------------------|------------|--------------------|----------------------------------------------------------------|------------------------------------------|
| Access            | O          | NA                 | NFC_RDR_STEPUP_AD_ISSUER_CERT,                                 | NA                                       |
| documen           |            |                    | NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID,                          |                                          |
| t<br>processin    |            |                    | NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXTENSIO<br>N,            |                                          |
| g                 |            |                    | NFC_RDR_STEPUP_AD_UNKNOWN_NON_CRITICAL_ACCESS_<br>EXTENSION,   |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_NO_ISSUER_CERT_NO_KEY_ID,                |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_INVALID_SIGNAT<br>URE,       |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_INVALID_SIGNATURE_ISSUER_A<br>UTH,       |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_INVALID_HASH_ISSUER_AUTH,                |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERTIFICATE_TIME_MIS<br>MATCH,    |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_NO_DATA_ELEMENTS,                        |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_ISSUER_DOCTYPE_MISMATCH,                 |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_DEVICE_KEY_INFO_MISMATCH,                |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_INVALID_ACCESS_DATA_ELEME<br>NT_VERSION, |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_NO_ACCESS_RULE_FOR_READE<br>R_ACTION,    |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE,                     |                                          |
|                   |            |                    | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_CRITICAL_ACCESS_<br>EXTENSION    |                                          |

| PICS<br>Parameter                                                                     | Read<br>er | User<br>Devi<br>ce | Reader Test Identifier                                                                                                                                                                                                                                    | User<br>Device<br>Test<br>Identifi<br>er |
|---------------------------------------------------------------------------------------|------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| Access<br>documen<br>t<br>verificati<br>on                                            | M          | NA                 | NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED,<br>NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH,<br>NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH,<br>NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION,<br>NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQUIRED                    | NA                                       |
| Access<br>documen<br>t<br>verificati<br>on –<br>Validity<br>iteration                 | M          | NA                 | NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION                                                                                                                                                                                                                  | NA                                       |
| Access<br>documen<br>t<br>verificati<br>on –<br>Validity<br>time<br>based<br>elements | O          | NA                 | NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED,<br>NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH,<br>NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH,<br>NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQUIRED<br>,<br>NFC_RDR_NEG_STEPUP_AD_SCHEDULE_TIME_VERIFY_REQU<br>IRED | NA                                       |
| Access<br>data<br>element<br>verificati<br>on                                         | M          | NA                 | NFC_RDR_STEPUP_AD_ACCESS_RULE,<br>NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES                                                                                                                                                                                 | NA                                       |
| Access<br>data<br>element<br>verificati<br>on –<br>Access<br>Rules                    | M          | NA                 | NFC_RDR_STEPUP_AD_ACCESS_RULE                                                                                                                                                                                                                             | NA                                       |
| Access<br>data<br>element<br>verificati<br>on –                                       | O          | NA                 | NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES,<br>NFC_RDR_NEG_STEPUP_AD_NO_VALID_SCHEDULE_ALLOW_<br>SCHEDULEID,<br>NFC_RDR_NEG_STEPUP_AD_VALID_SCHEDULE_DENY_SCHE<br>DULEID,                                                                                    | NA                                       |

![](_page_38_Picture_3.jpeg)

| PICS<br>Parameter                                                                             | Read<br>er | User<br>Devi<br>ce | Reader Test Identifier                                       | User<br>Device<br>Test<br>Identifi<br>er |
|-----------------------------------------------------------------------------------------------|------------|--------------------|--------------------------------------------------------------|------------------------------------------|
| Schedule<br>s                                                                                 |            |                    | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_IN_ACCESS_RULE_A<br>ND_READER |                                          |
| Access<br>data<br>element<br>verificati<br>on –<br>Access<br>extensio<br>n<br>criticalit<br>y | M          | NA                 |                                                              | NA                                       |
| Access<br>data<br>element<br>verificati<br>on –<br>Access<br>extensio<br>n content            | NA         | NA                 | NA                                                           | NA                                       |
| Access<br>data<br>element<br>verificati<br>on – Non<br>access<br>extensio<br>n                | NA         | NA                 | NA                                                           | NA                                       |
| Access<br>data<br>element<br>verificati<br>on –<br>Reader<br>rules                            | O          | NA                 | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE                    | NA                                       |
| Access<br>data<br>element<br>verificati<br>on - ID                                            | NA         | NA                 | NA                                                           | NA                                       |

**Table 4-6 Revocation document processing PICS parameters** 

| PICS<br>Parameter                              | Reade<br>r | User<br>Devic<br>e | Reader Test Identifier                                                  | User<br>Device<br>Test<br>Identifie<br>r |
|------------------------------------------------|------------|--------------------|-------------------------------------------------------------------------|------------------------------------------|
| Revocatio<br>n<br>document<br>processing       | O          | NA                 | NFC_RDR_STEPUP_RD,<br>NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSI<br>ON | NA                                       |
| Revocatio<br>n<br>document<br>verificatio<br>n | M          | NA                 | NFC_RDR_STEPUP_RD,<br>NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSI<br>ON | NA                                       |
| Revocatio<br>n element<br>verificatio<br>n     | M          | NA                 | NFC_RDR_STEPUP_RD,<br>NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSI<br>ON | NA                                       |

### **Table 4-7 NFC interface PICS parameters**

| PICS Parameter                          | Reader | User<br>Device | Reader Test Identifier   | User<br>Device<br>Test<br>Identifier |
|-----------------------------------------|--------|----------------|--------------------------|--------------------------------------|
| NFC Interface                           | M      | M              | Table 4-1                | Table<br>4-1                         |
| NFC – Step-Up AID SELECT                | M      | O              | NFC_RDR_STEPUP_AD_KEY_ID |                                      |
| Vendor-specific extensions in<br>SELECT | NA     | NA             | NA                       | NA                                   |

### **Table 4-8 BLE interface PICS parameters**

| PICS Parameter | Reader | User<br>Device | Reader Test Identifier | User<br>Device<br>Test<br>Identifier |
|----------------|--------|----------------|------------------------|--------------------------------------|
| BLE Interface  | O      | O              | Table 4-9, Table 4-10  | Table<br>4-9,<br>Table<br>4-10       |

![](_page_40_Picture_8.jpeg)

| PICS Parameter                            | Reader | User<br>Device | Reader Test Identifier                                                                                                                            | User<br>Device<br>Test<br>Identifier |
|-------------------------------------------|--------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| BLE – send<br>sensor triggered<br>bit     | O      | O              |                                                                                                                                                   |                                      |
| Dynamic<br>advertisement tag              | M      | O              | BLEUWB_RDR_EXPEDITED_STANDARD_PHASE,<br>BLEUWB_RDR_EXPEDITED_FAST_PHASE,<br>BLEUWB_RDR_STEPUP_PHASE,<br>BLEUWB_RDR_ADVERTISEMENT_FORMAT           |                                      |
| Pass Through                              | O      | O              |                                                                                                                                                   |                                      |
| Unsolicited<br>Reader status<br>reporting | M      | NA             | BLEUWB_RDR_EXPEDITED_STANDARD_PHASE,<br>BLEUWB_RDR_EXPEDITED_FAST_PHASE,<br>BLEUWB_RDR_STEPUP_PHASE,<br>BLERKE_RDR_UNSECURE,<br>BLERKE_RDR_SECURE | NA                                   |

**Table 4-9 BLE + UWB interface PICS parameters for Bluetooth LE + UWB Aliro Flow** 

| PICS<br>Parameter | Rea<br>der | Use<br>r<br>Dev<br>ice | Reader Test Identifier                                                         | User Device Test Identifier              |                                         |  |  |  |  |                             |
|-------------------|------------|------------------------|--------------------------------------------------------------------------------|------------------------------------------|-----------------------------------------|--|--|--|--|-----------------------------|
| Bluetooth<br>LE + | O          | O                      | BLEUWB_RDR_CONTROL_FLOW_R<br>DR_DESCRIPTOR_TAG,                                | BLEUWB_UD_EXPEDITED_STAND<br>ARD_PHASE,  |                                         |  |  |  |  |                             |
| UWB<br>Flow       |            |                        | BLEUWB_RDR_EXPEDITED_STAND<br>ARD_PHASE,                                       | BLEUWB_UD_EXPEDITED_FAST_P<br>HASE,      |                                         |  |  |  |  |                             |
|                   |            |                        | BLEUWB_RDR_EXPEDITED_FAST_P                                                    | BLEUWB_UD_STEPUP_PHASE,                  |                                         |  |  |  |  |                             |
|                   |            |                        | HASE,<br>BLEUWB_RDR_STEPUP_PHASE,                                              | BLEUWB_UD_RANGING_SUSPEND<br>,           |                                         |  |  |  |  |                             |
|                   |            |                        | BLEUWB_RDR_RANGING_SUSPEND,                                                    | BLEUWB_UD_RANGING_RESUME,                |                                         |  |  |  |  |                             |
|                   |            |                        | BLEUWB_RDR_RANGING_RESUME,                                                     | BLEUWB_UD_UD_DESCRIPTOR_T                |                                         |  |  |  |  |                             |
|                   |            |                        |                                                                                |                                          |                                         |  |  |  |  | BLEUWB_RDR_NEG_FAILED_L2CAP |
|                   |            |                        | ,                                                                              | BLEUWB_UD_NEG_WRONG_ADV,                 |                                         |  |  |  |  |                             |
|                   |            |                        | BLEUWB_RDR_NEG_FAILED_SPSM_<br>L2CAP,                                          | BLEUWB_UD_NEG_FAILED_L2CAP<br>,          |                                         |  |  |  |  |                             |
|                   |            |                        |                                                                                | BLEUWB_RDR_NEG_TIMEOUT_BEF<br>ORE_AUTH0, | BLEUWB_UD_NEG_TIMEOUT_BEF<br>ORE_AUTH0, |  |  |  |  |                             |
|                   |            |                        | BLEUWB_RDR_TIMEOUT_EXTENSI<br>ON,<br>BLEUWB_RDR_NEG_M2_MISMATCH<br>_PARAMETER, | BLEUWB_UD_TIMEOUT_EXTENSI<br>ON,         |                                         |  |  |  |  |                             |
|                   |            |                        |                                                                                | BLEUWB_UD_NEG_URSK_NOT_FO<br>UND,        |                                         |  |  |  |  |                             |

| PICS                | Rea | Use             | Reader Test Identifier                         | User Device Test Identifier                       |  |
|---------------------|-----|-----------------|------------------------------------------------|---------------------------------------------------|--|
| Parameter           | der | r<br>Dev<br>ice |                                                |                                                   |  |
|                     |     |                 | BLEUWB_RDR_NEG_M4_MISMATCH<br>_PARAMETER,      | BLEUWB_UD_NEG_M1_MISMATC<br>H_PARAMETER,          |  |
|                     |     |                 | BLEUWB_RDR_NEG_SUSPEND_MIS<br>MATCH_PARAMETER, | BLEUWB_UD_NEG_M3_MISMATC<br>H_PARAMETER           |  |
|                     |     |                 | BLEUWB_RDR_ADVERTISEMENT_F<br>ORMAT            |                                                   |  |
| UWB<br>ranging      | M   | M               | BLEUWB_RDR_EXPEDITED_STAND<br>ARD_PHASE,       | BLEUWB_UD_EXPEDITED_STAND<br>ARD_PHASE,           |  |
|                     |     |                 | BLEUWB_RDR_EXPEDITED_FAST_P<br>HASE,           | BLEUWB_UD_EXPEDITED_FAST_P<br>HASE,               |  |
|                     |     |                 | BLEUWB_RDR_STEPUP_PHASE                        | BLEUWB_UD_STEPUP_PHASE                            |  |
| UWB                 | M   | M               | BLEUWB_RDR_RANGING_SUSPEND,                    | BLEUWB_UD_RANGING_SUSPEND                         |  |
| ranging<br>suspend  |     |                 | BLEUWB_RDR_NEG_SUSPEND_MIS<br>MATCH_PARAMETER  | ,<br>BLEUWB_UD_NEG_SUSPEND_MIS<br>MATCH_PARAMETER |  |
| UWB                 | M   | M               | BLEUWB_RDR_RANGING_RESUME                      | BLEUWB_UD_RANGING_RESUME,                         |  |
| ranging<br>resume   |     |                 |                                                | BLEUWB_UD_NEG_RESUME_MIS<br>MATCH_PARAMETER       |  |
| One<br>ranging      | M   | M               | BLEUWB_RDR_EXPEDITED_STAND<br>ARD_PHASE,       | BLEUWB_UD_EXPEDITED_STAND<br>ARD_PHASE,           |  |
| round               |     |                 | BLEUWB_RDR_EXPEDITED_FAST_P<br>HASE,           | BLEUWB_UD_EXPEDITED_FAST_P<br>HASE,               |  |
|                     |     |                 | BLEUWB_RDR_STEPUP_PHASE                        | BLEUWB_UD_STEPUP_PHASE                            |  |
| Two<br>ranging      | O   | M               | BLEUWB_RDR_EXPEDITED_STAND<br>ARD_PHASE,       | BLEUWB_UD_EXPEDITED_STAND<br>ARD_PHASE,           |  |
| rounds              |     |                 | BLEUWB_RDR_EXPEDITED_FAST_P<br>HASE,           | BLEUWB_UD_EXPEDITED_FAST_P<br>HASE,               |  |
|                     |     |                 | BLEUWB_RDR_STEPUP_PHASE                        | BLEUWB_UD_STEPUP_PHASE                            |  |
| BLE                 | O   | M               | BLEUWB_RDR_EXPEDITED_STAND<br>ARD_PHASE,       | BLEUWB_UD_EXPEDITED_STAND<br>ARD_PHASE,           |  |
| UWB<br>Time         |     |                 | BLEUWB_RDR_EXPEDITED_FAST_P<br>HASE,           | BLEUWB_UD_EXPEDITED_FAST_P<br>HASE,               |  |
| synchroni<br>zation |     |                 | BLEUWB_RDR_STEPUP_PHASE                        | BLEUWB_UD_STEPUP_PHASE                            |  |
|                     |     |                 |                                                |                                                   |  |

![](_page_42_Picture_3.jpeg)

**Table 4-10 BLE interface PICS parameters for BLE-Only Flow** 

| PICS<br>Paramet<br>er                   | Read<br>er | User<br>Devi<br>ce | Reader Test Identifier                                                                                                                                                     | User Device Test Identifier                                                                           |
|-----------------------------------------|------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| BLE<br>Only<br>Flow                     | O          | O                  | BLERKE_RDR_UNSECURE,<br>BLERKE_RDR_SECURE,<br>BLERKE_RDR_NEG_FAST,<br>BLERKE_RDR_NEG_FAILED_L2CA<br>P,<br>BLERKE_RDR_NEG_FAILED_SPSM<br>_L2CAP,<br>BLERKE_RDR_STEPUP_PHASE | BLERKE_UD_EXPEDITED_STANDAR<br>D_PHASE,<br>BLERKE_UD_UD_DESCRIPTOR_TAG,<br>BLERKE_UD_NEG_FAILED_L2CAP |
| Explici<br>t<br>Reader<br>selecti<br>on | NA         | M                  | NA                                                                                                                                                                         | BLERKE_UD_EXPEDITED_STANDAR<br>D_PHASE                                                                |

# **5 User Device Under Test Routines**

This section describes routines used in User Device Under Test tests.

### **5.1 SELECT Routine**

**Table 5-1 SELECT routine** 

| Steps | TH (Reader)         | DUT<br>(User<br>Device)    | Verification at TH                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------|---------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send SELECT command |                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2     |                     | send<br>SELECT<br>response | Verify the following:<br>1.<br>order of TLVs matches the technical<br>specification<br>2.<br>All mandatory TLVs in technical specification<br>are present<br>0100h is present in the<br>3.<br>expedited_phase_supported_protocol_versions.<br>4.<br>size of SELECT response is less than 256B<br>AID = A000000909ACCE5501, if Expedited Phase<br>5.<br>6.<br>AID = A000000909ACCE5502, if Step-Up<br>Phase<br>Type = 0000h<br>7.<br>Unknown TLVs are ignored, if present<br>8.<br>If all criteria are met, then CONTINUE else FAIL. |

# **5.2 AUTH0 Routine**

**Table 5-2 AUTH0 routine** 

| Steps | TH (Reader)                                                                                                                                       | DUT<br>(User<br>Device)   | Verification at TH                                                                                                                                                                                                                                                                                                                                                      |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send AUTH0 command<br>1.<br>authentication_policy = select<br>randomly between 01h, 02h, 03h<br>2.<br>expedited_phase_protocol_version<br>= 0100h |                           | Verify the following:<br>1.<br>user authentication is performed by User<br>Device, if authentication_policy = 03h.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                              |
| 2     |                                                                                                                                                   | send<br>AUTH0<br>response | Verify the following:<br>1.<br>order of TLVs matches technical<br>specification<br>2.<br>All mandatory TLVs in technical<br>specification are present<br>3.<br>cryptogram is not present, if<br>command_parameters = 0h<br>4.<br>cryptogram is present, if<br>command_parameters = 1h<br>5.<br>auth0_response_vendor_extension, if<br>present is less than 127B in size |

![](_page_44_Picture_10.jpeg)

| Steps | TH (Reader) | DUT<br>(User<br>Device) | Verification at TH                                                                                              |
|-------|-------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|
|       |             |                         | SW = 9000h<br>6.<br>9.<br>Success in establishing secure channel<br>Unknown TLVs are ignored, if present<br>10. |
|       |             |                         | If all criteria are met, then CONTINUE else<br>FAIL.                                                            |

### **5.3 AUTH1 with SW Equal to 9000h Routine**

**Table 5-3 AUTH1 with SW = 9000h routine** 

| Steps | TH (Reader)                                                                            | DUT<br>(User<br>Device)   | Verification at TH                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------|----------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5     | Send AUTH1 command<br>command_parameters = randomly<br>1.<br>selected between 00h, 01h |                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 6     |                                                                                        | send<br>AUTH1<br>response | Verify the following:<br>1.<br>order of TLVs matches technical<br>specification.<br>2.<br>All mandatory TLVs in technical<br>specification are present.<br>key_slot is present, if<br>3.<br>command_parameters = 01h.<br>4.<br>Access Credential long term public key<br>is present, if command_parameters =<br>00h.<br>5.<br>SW = 9000h.<br>6.<br>User Device signature verification<br>passes.<br>Unknown TLVs are ignored, if present<br>7.<br>If all criteria are met, then CONTINUE else<br>FAIL. |

### **5.4 AUTH1 with SW Not Equal to 9000h Routine**

**Table 5-4 AUTH1 with SW != 9000h routine** 

| Steps | TH (Reader)                                                                            | DUT<br>(User<br>Device)   | Verification at TH                          |
|-------|----------------------------------------------------------------------------------------|---------------------------|---------------------------------------------|
| 1     | Send AUTH1 command<br>1.<br>command_parameters = randomly<br>selected between 00h, 01h |                           |                                             |
| 2     |                                                                                        | send<br>AUTH1<br>response | Verify the following:<br>1.<br>SW != 9000h. |

![](_page_45_Picture_9.jpeg)

| Steps | TH (Reader) | DUT<br>(User<br>Device) | Verification at TH                                                                          |
|-------|-------------|-------------------------|---------------------------------------------------------------------------------------------|
|       |             |                         | 2.<br>Response data field is empty.<br>If all criteria are met, then CONTINUE else<br>FAIL. |

### **5.5 EXCHANGE Indicating Transaction Success Routine**

**Table 5-5 EXCHANGE indicating transaction success routine** 

| Steps | TH (Reader)                                             | DUT (User<br>Device)          | Verification at TH                                                                                                                              |
|-------|---------------------------------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send EXCHANGE command with tag<br>0x97 (Reader Status). |                               | Verify the following:<br>1.<br>0x97h first byte is 0x01h.<br>If all criteria are met, then CONTINUE else<br>FAIL.                               |
| 2     |                                                         | send<br>EXCHANGE<br>response. | Verify the following:<br>1.<br>response payload =<br>0x0002   0x00  0x00.<br>2.<br>SW = 9000h.<br>If all criteria are met, then PASS else FAIL. |

# **5.6 EXCHANGE Indicating Transaction Failure Routine**

**Table 5-6 EXCHANGE indicating transaction failure routine** 

| Steps | TH (Reader)                                             | DUT (User<br>Device)          | Verification at TH                                                                                                                             |
|-------|---------------------------------------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send EXCHANGE command with tag<br>0x97 (Reader Status). |                               | Verify the following:<br>0x97h first byte is 0x00h.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                    |
| 2     |                                                         | send<br>EXCHANGE<br>response. | Verify the following:<br>1.<br>response payload =<br>0x0002  0x00  0x00.<br>SW = 9000h.<br>2.<br>If all criteria are met, then PASS else FAIL. |

![](_page_46_Picture_9.jpeg)

### **5.7 CONTROL FLOW Indicating Transaction Failure Routine**

**Table 5-7 CONTROL FLOW indicating transaction failure routine** 

| Steps | TH (Reader)                | DUT (User<br>Device)                 | Verification at TH                                                                                                                                                                                                            |
|-------|----------------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send CONTROL FLOW command. |                                      | Verify the following:<br>CONTROL FLOW command data field<br>length does not exceed 255 bytes.<br>CONTROL FLOW command is formatted<br>according to the specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     |                            | send<br>CONTROL<br>FLOW<br>response. | Verify the following:<br>1.<br>response data field is empty.<br>2.<br>SW = 9000h.<br>If all criteria are met, then PASS else FAIL.                                                                                            |

### **5.8 BLE+UWB Aliro Access Protocol Routine**

**Table 5-8 BLE+UWB Aliro Access Protocol routine** 

| Steps | TH (Reader)                                                                                         | DUT (User Device)                                                                   | Verification at TH                                                                                                                                                |
|-------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send Bluetooth LE advertisement                                                                     |                                                                                     |                                                                                                                                                                   |
| 2     |                                                                                                     | Establish L2CAP<br>connection                                                       |                                                                                                                                                                   |
| 3     |                                                                                                     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501 | Verify the following:<br>Format of Initiate<br>Access Protocol<br>Message ID matches<br>specification.<br>If all criteria are met,<br>then CONTINUE else<br>FAIL. |
| 4     | Execute AUTH0 routine. Set command_parameters = 0h and<br>authentication_policy = 01h (User Device) |                                                                                     | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                                                                           |
| 5     | Execute AUTH1 routine with SW = 9000h.<br>Reader_cert is not present in AUTH1 command.              |                                                                                     | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                                                                           |
| 6     | Send EXCHANGE command                                                                               |                                                                                     | Verify the following:<br>Tag 0x98 is present.<br>If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                          |

![](_page_47_Picture_8.jpeg)

| Steps | TH (Reader)                                                                                            | DUT (User Device)         | Verification at TH                                                                                                                                                                  |
|-------|--------------------------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 7     |                                                                                                        | Send EXCHANGE<br>response |                                                                                                                                                                                     |
| 8     | Send Reader Status Access Protocol Completed<br>Message ID carrying Reader Information<br>Attribute ID |                           | Verify the following:<br>Ensure reader status is<br>secured.<br>Format of message<br>matches technical<br>specification.<br>If all criteria are met,<br>then CONTINUE else<br>FAIL. |

# **5.9 BLE+UWB Ranging Session Setup Routine**

**Table 5-9 BLE+UWB ranging session setup routine** 

| Steps | TH (Reader)                              | DUT (User Device)                           | Verification at TH                                                                                                                          |
|-------|------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send Ranging Session Setup M1 Message ID |                                             |                                                                                                                                             |
| 2     |                                          | send Ranging Session<br>Setup M2 Message ID | Verify the following:<br>Format of this<br>message matches the<br>specification.<br>If all criteria are met,<br>then CONTINUE else<br>FAIL. |
| 3     | Send Ranging Session Setup M3 Message ID |                                             |                                                                                                                                             |
| 4     |                                          | send Ranging Session<br>Setup M4 Message ID | Verify the following:<br>Format of this<br>message matches the<br>specification.<br>If all criteria are met,<br>then CONTINUE else<br>FAIL. |

### **5.10 BLE-Only Aliro Access Protocol Routine**

**Table 5-10 BLE-only Aliro Access Protocol routine** 

| Steps | TH (Reader)                      | DUT (User Device)                              | Verification at TH                                                               |
|-------|----------------------------------|------------------------------------------------|----------------------------------------------------------------------------------|
| 1     | Send Bluetooth LE advertisement. |                                                |                                                                                  |
| 2     |                                  | Establish L2CAP<br>connection.                 |                                                                                  |
| 3     |                                  | User register intent to<br>perform RKE action. | Verify the following:<br>User selects the<br>Reader and indicates<br>the action. |

![](_page_48_Picture_9.jpeg)

| Steps | TH (Reader)                                                                                      | DUT (User Device)                            | Verification at TH                                                                                        |
|-------|--------------------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------|
|       |                                                                                                  |                                              | Note: how the user<br>selects the Reader,<br>and the associated<br>action is<br>implementation<br>choice. |
|       |                                                                                                  |                                              | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                   |
| 4     |                                                                                                  | Send Initiate Access<br>Protocol RKE Message | Verify the following:                                                                                     |
|       |                                                                                                  | ID carrying AID =<br>A000000909ACCE5501      | Format of Message ID<br>matches the technical<br>specification.                                           |
|       |                                                                                                  |                                              | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                   |
| 5     | Send AUTH0 command                                                                               |                                              | Verify the following:                                                                                     |
|       | command_parameters = 0h<br>authentication_policy = 01h (User Device) or 03h<br>(Force User Auth) |                                              | User Auth is<br>performed, if<br>authentication_policy<br>= 03h.                                          |
|       |                                                                                                  |                                              | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                   |
| 6     |                                                                                                  | Send AUTH0 response                          | Verify the following:                                                                                     |
|       |                                                                                                  |                                              | Format of this<br>message matches the<br>specification.                                                   |
|       |                                                                                                  |                                              | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                   |
| 7     | Send AUTH1 command and reader_cert is not<br>present.                                            |                                              |                                                                                                           |
|       |                                                                                                  | send AUTH1 response                          | Verify the following:                                                                                     |
|       |                                                                                                  |                                              | Format of this<br>message matches the<br>specification.                                                   |
|       |                                                                                                  |                                              | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                   |
| 8     | Send Reader Status Access Protocol Completed                                                     |                                              | Verify the following:                                                                                     |
|       | Message ID carrying Reader Information<br>Attribute ID                                           |                                              | Format of this<br>message matches the<br>specification.                                                   |
|       |                                                                                                  |                                              | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                                   |

# **6 Reader Under Test Routines**

This section describes routines used in Reader Under Test tests.

### **6.1 SELECT Routine**

**Table 6-1 SELECT routine** 

| Steps | TH (User Device)        | DUT (Reader)           | Verification at TH                                                                                                                                                                         |
|-------|-------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                         | Send SELECT<br>command | Verify the following:<br>AID = A000000909ACCE5501, if Expedited<br>1.<br>Phase<br>2.<br>AID = A000000909ACCE5502, if Step-Up<br>Phase<br>If all criteria are met, then CONTINUE else FAIL. |
| 2     | send SELECT<br>response |                        |                                                                                                                                                                                            |

# **6.2 AUTH0 Routine**

**Table 6-2 AUTH0 routine** 

| Steps | TH (User Device)       | DUT (Reader)          | Verification at TH                                                                                                                                                                                                                                                                                       |
|-------|------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                        | Send AUTH0<br>command | Verify the following:<br>1.<br>order of TLVs in AUTH0 command matches<br>specification.<br>2.<br>All mandatory TLVs in AUTH0 command are<br>present<br>3.<br>expedited_phase_protocol_version = 0100h<br>Unknown TLVs are ignored, if present<br>4.<br>If all criteria are met, then CONTINUE else FAIL. |
| 2     | Send AUTH0<br>response |                       |                                                                                                                                                                                                                                                                                                          |

### **6.3 AUTH1 Routine**

**Table 6-3 AUTH1 routine** 

| Steps | TH (User Device)       | DUT (Reader)          | Verification at TH                                                                                                                                                                                                                                     |
|-------|------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                        | Send AUTH1<br>command | Verify the following:<br>1.<br>order of TLVs in AUTH1 command matches<br>specification.<br>2.<br>All mandatory TLVs in AUTH1 command are<br>present<br>Unknown TLVs are ignored, if present<br>3.<br>If all criteria are met, then CONTINUE else FAIL. |
| 2     | Send AUTH1<br>response |                       |                                                                                                                                                                                                                                                        |

![](_page_50_Picture_13.jpeg)

### **6.4 EXCHANGE Indicating Transaction Success Routine**

**Table 6-4 EXCHANGE indicating transaction success routine** 

| Steps | TH (User Device)          | DUT (Reader)                                              | Verification at TH                                                                                                                                                                                                                                                                               |
|-------|---------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                           | send EXCHANGE<br>command with tag<br>0x97 (Reader Status) | Verify the following:<br>1.<br>order of TLVs in EXCHANGE command<br>matches specification.<br>2.<br>All mandatory TLVs in EXCHANGE command<br>are present<br>3.<br>0x97h first byte is 0x01h.<br>4.<br>Unknown TLVs are ignored, if present<br>If all criteria are met, then CONTINUE else FAIL. |
| 2     | Send EXCHANGE<br>response |                                                           |                                                                                                                                                                                                                                                                                                  |

### **6.5 EXCHANGE Indicating Transaction Failure Routine**

**Table 6-5 EXCHANGE indicating transaction failure routine** 

| Steps | TH (User Device)          | DUT (Reader)                                              | Verification at TH                                                                                       |
|-------|---------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1     |                           | send EXCHANGE<br>command with tag<br>0x97 (Reader Status) | Verify the following:<br>0x97h first byte is 0x00h.<br>If all criteria are met, then CONTINUE else FAIL. |
| 2     | Send EXCHANGE<br>response |                                                           |                                                                                                          |

### **6.6 CONTROL FLOW Indicating Transaction Failure Routine**

**Table 6-6 CONTROL FLOW indicating transaction failure routine** 

| Steps | TH (User Device)            | DUT<br>(Reader)                     | Verification at TH                                                                                                                                                                                                      |
|-------|-----------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                             | Send<br>CONTROL<br>FLOW<br>command. | Verify the following:<br>1.<br>command data field length does<br>not exceed 255 bytes.<br>2.<br>Format of CONTROL FLOW<br>command matches the<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | send CONTROL FLOW response. |                                     | Verify the following:<br>1.<br>response data field is empty.<br>SW = 9000h.<br>2.<br>If all criteria are met, then PASS else FAIL.                                                                                      |

![](_page_51_Picture_11.jpeg)

# **6.7 BLE+UWB Aliro Access Protocol Routine**

**Table 6-7 BLE+UWB Aliro Access Protocol routine** 

| Steps | TH (User Device)                                                                 | DUT (Reader)                                                                                                    | Verification at TH                                                                                                                                                                                  |
|-------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                                                                                  | Send Bluetooth LE<br>advertisement                                                                              | Verify the following:<br>BLE + UWB Aliro Flow Supported<br>Bit is set to 1.<br>Advertisement format matches the<br>technical specification.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Establish L2CAP connection                                                       |                                                                                                                 |                                                                                                                                                                                                     |
| 3     | Send Initiate Access Protocol<br>Message ID carrying AID =<br>A000000909ACCE5501 |                                                                                                                 |                                                                                                                                                                                                     |
| 4     | Execute AUTH0 routine                                                            |                                                                                                                 | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                |
| 5     | Execute AUTH1 routine                                                            |                                                                                                                 | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                |
| 8     |                                                                                  | Send EXCHANGE<br>command                                                                                        | Verify the following:<br>Tag 0x98 is present.<br>If all criteria are met, then<br>CONTINUE else FAIL.                                                                                               |
| 9     | Send EXCHANGE response                                                           |                                                                                                                 |                                                                                                                                                                                                     |
| 10    |                                                                                  | Send Reader Status<br>Access Protocol<br>Completed Message ID<br>carrying Reader<br>Information Attribute<br>ID | Verify the following:<br>reader status is secured.<br>If all criteria are met, then<br>CONTINUE else FAIL.                                                                                          |

### **6.8 BLE+UWB Ranging Session Setup Routine**

#### **Table 6-8 BLE+UWB ranging session setup routine**

| Steps | TH (User Device)                                                             | DUT (Reader)                                   | Verification at TH                                                                                                                    |
|-------|------------------------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send Ranging Message ID<br>carrying Initiate Ranging<br>Session Attribute ID |                                                |                                                                                                                                       |
| 2     |                                                                              | Send Ranging<br>Session Setup M1<br>Message ID | Verify the following:<br>Format of this message matches the<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 3     | send Ranging Session<br>Setup M2 Message ID                                  |                                                |                                                                                                                                       |

![](_page_52_Picture_8.jpeg)

| Steps | TH (User Device)                            | DUT (Reader)                                   | Verification at TH                                                                                                                    |
|-------|---------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 4     |                                             | send Ranging Session<br>Setup M3 Message<br>ID | Verify the following:<br>Format of this message matches the<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 5     | send Ranging Session<br>Setup M4 Message ID |                                                |                                                                                                                                       |

### **6.9 BLE-Only Aliro Access Protocol Routine**

**Table 6-9 BLE-only Aliro Access Protocol routine** 

| Steps | TH (User Device)                                                                        | DUT (Reader)                                                  | Verification at TH                                           |
|-------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| 1     |                                                                                         | Send Bluetooth LE<br>advertisement                            | Verify the following:                                        |
|       |                                                                                         |                                                               | BLE-Only Aliro Flow Supported Bit is set<br>to 1.            |
|       |                                                                                         |                                                               | Advertisement format matches the<br>technical specification. |
|       |                                                                                         |                                                               | If all criteria are met, then CONTINUE<br>else FAIL.         |
| 2     | Establish L2CAP<br>connection                                                           |                                                               |                                                              |
| 3     | Send Initiate Access<br>Protocol RKE Message<br>ID carrying AID =<br>A000000909ACCE5501 |                                                               |                                                              |
| 4     |                                                                                         | Send AUTH0 command                                            | Verify the following:                                        |
|       |                                                                                         |                                                               | command_parameters = 0h.                                     |
|       |                                                                                         |                                                               | If all criteria are met, then CONTINUE<br>else FAIL.         |
| 5     | send AUTH0 response                                                                     |                                                               |                                                              |
| 6     |                                                                                         | Send AUTH1 command                                            |                                                              |
| 7     | Send AUTH1 response                                                                     |                                                               |                                                              |
| 8     |                                                                                         | [Optional] Send<br>EXCHANGE command                           |                                                              |
| 9     | Send EXCHANGE<br>response                                                               |                                                               | Sent, if an EXCHANGE command is<br>received.                 |
| 10    |                                                                                         | Send Reader Status<br>Access Protocol<br>Completed Message ID | Verify the following:                                        |
|       |                                                                                         |                                                               | Format matches technical specification.                      |
|       | carrying Reader<br>Information Attribute ID                                             | If all criteria are met, then CONTINUE<br>else FAIL.          |                                                              |

# **7 User Device Under Test Conformance Tests**

# **7.1 Expedited Standard Phase without Reader Certificate**

**Table 7-1 NFC\_UD\_STANDARD\_NO\_CERT test identifiers** 

| Parameter     | Value                                                            |
|---------------|------------------------------------------------------------------|
| Test ID       | NFC_UD_STANDARD_NO_CERT                                          |
| PICS          | Expedited-Standard Phase AND                                     |
|               | User Authentication Policy Enforcement AND                       |
|               | Reader signature generation and validation using reader_PubK AND |
|               | Device signature generation and validation AND                   |
|               | Lookup of the reader key through reader_group_identifier AND     |
|               | AUTH1 command parameter                                          |
| Applicability | M for User Device                                                |
| Interface     | NFC                                                              |

#### **Table 7-2 NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions**

| Provision onto    | Remarks                                |
|-------------------|----------------------------------------|
| DUT (User Device) | reader_PubK, reader_group_identifier   |
| TH (Reader)       | Access Credential long term public key |

#### **Table 7-3 NFC\_UD\_STANDARD\_NO\_CERT test steps**

| Steps | TH (Reader)                                                                                                                          | DUT (User<br>Device) | Verification at TH                                   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                                                 |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.<br>auth0_command_vendor_extension is present in<br>AUTH0 command. |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 3     | Execute AUTH1 with SW = 9000h routine (Table<br>5-3).<br>Reader_cert is not present in AUTH1 command.                                |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 4     | Execute EXCHANGE indicating transaction<br>success routine (Table 5-5).                                                              |                      | If all criteria are met, then PASS else FAIL.        |

### **7.2 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with APDU Chaining**

![](_page_54_Picture_11.jpeg)

**Table 7-4 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test identifiers** 

| Parameter     | Value                                                                                               |  |
|---------------|-----------------------------------------------------------------------------------------------------|--|
| Test ID       | NFC_UD_STANDARD_ CERT_IN_LOAD_CERT_WITH_CHAINING                                                    |  |
| PICS          | Expedited-Standard Phase AND                                                                        |  |
|               | Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND |  |
|               | Presentation and validation of the reader_Cert in LOAD_CERT command                                 |  |
|               | Device signature generation and validation AND                                                      |  |
|               | Verification of the reader_Cert with the CA Public Key AND                                          |  |
|               | Lookup of the reader CA Public Key through reader_group_identifier AND                              |  |
|               | AUTH1 command parameter AND                                                                         |  |
|               | Command chaining                                                                                    |  |
| Applicability | M for User Device                                                                                   |  |
| Interface     | NFC                                                                                                 |  |

#### **Table 7-5 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions**

| Provision onto    | Remarks                                                     |
|-------------------|-------------------------------------------------------------|
| DUT (User Device) | Reader System Issuer CA public key, reader_group_identifier |
| TH (Reader)       | Access Credential long term public key, reader_Cert         |

#### **Table 7-6 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test steps**

| Steps | TH (Reader)                                                                                           | DUT (User<br>Device)           | Verification at TH                                                                                                                    |
|-------|-------------------------------------------------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID<br>= A000000909ACCE5501.                                  |                                | If all criteria are met, then CONTINUE else FAIL.                                                                                     |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                    |                                | If all criteria are met, then CONTINUE else FAIL.                                                                                     |
| 3     | Send LOAD_CERT command<br>with fragmented reader_cert<br>with chaining.                               |                                |                                                                                                                                       |
| 4     |                                                                                                       | Send<br>LOAD_CERT<br>response. | Verify the following:<br>1.<br>SW =9000h.<br>2.<br>Response data field is empty.<br>If all criteria are met, then CONTINUE else FAIL. |
| 5     | Execute AUTH1 with SW = 9000h routine<br>(Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                                | If all criteria are met, then CONTINUE else FAIL.                                                                                     |
| 6     | Execute EXCHANGE indicating transaction<br>success routine (Table 5-5).                               |                                | If all criteria are met, then PASS else FAIL.                                                                                         |

### **7.3 Expedited Standard Phase with Reader Cert in LOAD\_CERT without APDU Chaining**

**Table 7-7 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test identifiers** 

| Parameter     | Value                                                                                               |  |
|---------------|-----------------------------------------------------------------------------------------------------|--|
| Test ID       | NFC_UD_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING                                                       |  |
| PICS          | Expedited-Standard Phase AND                                                                        |  |
|               | Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND |  |
|               | Presentation and validation of the reader_Cert in LOAD_CERT command                                 |  |
|               | Device signature generation and validation AND                                                      |  |
|               | Verification of the reader_Cert with the CA Public Key AND                                          |  |
|               | Lookup of the reader CA Public Key through reader_group_identifier AND                              |  |
|               | AUTH1 command parameter AND                                                                         |  |
|               | Extended length                                                                                     |  |
| Applicability | M for User Device, if it supports Extended length APDUs                                             |  |
| Interface     | NFC                                                                                                 |  |

NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

**Table 7-8 NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test steps** 

| Step# | TH (Reader)                                                             | DUT (User<br>Device)           | Verification at TH                                                                                                                       |
|-------|-------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.    |                                | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                     |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h       |                                | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                     |
| 3     | Send LOAD_CERT command with<br>reader_cert and no APDU chaining.        |                                |                                                                                                                                          |
| 4     |                                                                         | Send<br>LOAD_CERT<br>response. | Verify the following:<br>1.<br>SW =9000h.<br>2.<br>Response data field is empty.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 5     | Execute AUTH1 with SW = 9000h routine (Table<br>5-3).                   |                                | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                     |
|       | Reader_cert is not present in AUTH1 command.                            |                                |                                                                                                                                          |
| 6     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5). |                                | If all criteria are met, then PASS else FAIL.                                                                                            |

![](_page_56_Picture_8.jpeg)

### **7.4 Expedited Standard Phase with Reader Cert in AUTH1 with APDU Chaining**

**Table 7-9 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test identifiers** 

| Parameter     | Value                                                                                               |  |
|---------------|-----------------------------------------------------------------------------------------------------|--|
| Test ID       | NFC_UD_STANDARD_CERT_IN_AUTH1_WITH_CHAINING                                                         |  |
| PICS          | Expedited-Standard Phase AND                                                                        |  |
|               | Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND |  |
|               | Presentation and validation of the reader_Cert in AUTH1 command                                     |  |
|               | Device signature generation and validation AND                                                      |  |
|               | Verification of the reader_Cert with the CA Public Key AND                                          |  |
|               | Lookup of the reader CA Public Key through reader_group_identifier AND                              |  |
|               | AUTH1 command parameter AND                                                                         |  |
|               | Command chaining                                                                                    |  |
| Applicability | M for User Device                                                                                   |  |
| Interface     | NFC                                                                                                 |  |

NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

**Table 7-10 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test steps** 

| Steps | TH (Reader)                                                                 | DUT (User<br>Device) | Verification at TH                                   |
|-------|-----------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.        |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.          |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 3     | Execute AUTH1 with SW = 9000h routine (Table<br>5-3).                       |                      | If all criteria are met, then CONTINUE else<br>FAIL  |
|       | Reader_cert is present and fragmented with chaining<br>over multiple APDUs. |                      |                                                      |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5).     |                      | If all criteria are met, then PASS else FAIL.        |

### **7.5 Expedited Standard Phase with Reader Cert in AUTH1 without APDU Chaining**

**Table 7-11 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test identifiers** 

| Parameter | Value                                      |
|-----------|--------------------------------------------|
| Test ID   | NFC_UD_STANDARD_ CERT_IN_AUTH1_NO_CHAINING |

![](_page_57_Picture_11.jpeg)

| PICS          | Expedited-Standard Phase AND                                                                        |  |
|---------------|-----------------------------------------------------------------------------------------------------|--|
|               | Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND |  |
|               | Presentation and validation of the reader_Cert in AUTH1 command                                     |  |
|               | Device signature generation and validation AND                                                      |  |
|               | Verification of the reader_Cert with the CA Public Key AND                                          |  |
|               | Lookup of the reader CA Public Key through reader_group_identifier AND                              |  |
|               | AUTH1 command parameter AND                                                                         |  |
|               | Extended length                                                                                     |  |
| Applicability | M for User Device, if it supports Extended length APDU                                              |  |
| Interface     | NFC                                                                                                 |  |

NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

**Table 7-12 NFC\_UD\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test steps** 

| Step# | TH (Reader)                                                                                                                  | DUT (User<br>Device) | Verification at TH                                   |
|-------|------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                                         |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                                           |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 3     | Execute AUTH1 with SW = 9000h routine (Table<br>5-3).<br>Reader_cert is present and without chaining over<br>multiple APDUs. |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5).                                                      |                      | If all criteria are met, then PASS else FAIL.        |

### **7.6 Expedited Fast Phase**

**Table 7-13 NFC\_UD\_FAST test identifiers** 

| Parameter     | Value                                                |
|---------------|------------------------------------------------------|
| Test ID       | NFC_UD_FAST                                          |
| PICS          | Expedited-fast                                       |
| Applicability | M for User Device that supports Expedited Fast Phase |
| Interface     | NFC                                                  |

![](_page_58_Picture_9.jpeg)

NFC\_UD\_FAST test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-14 NFC\_UD\_FAST test steps** 

| Steps | TH (Reader)                                                                                                                           | DUT (User<br>Device) | Verification at TH                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                                                  |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                           |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                                                    |                      | Note down reader_group_sub_identifier.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command.                                    |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                           |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5)                                                                |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                           |
| 5     | Wait for at least 3 seconds.                                                                                                          |                      |                                                                                                |
| 6     | Execute SELECT routine. Set AID =<br>A000000909ACCE5501.                                                                              |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                           |
| 7     | Execute AUTH0 routine. Set command_parameters =<br>1h.<br>Use reader_group_identifier and<br>reader_group_sub_identifier from step 2. |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                           |
| 8     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5).                                                               |                      | If all criteria are met, then PASS else<br>FAIL.                                               |

# **7.7 Expedited Standard Phase with Sixteen Reader Group Identifiers bound to Single Access Credential**

**Table 7-15 NFC\_UD\_STANDARD\_SIXTEEN\_GROUPPIDENTIFIER\_ONE\_AC test identifiers** 

| Parameter     | Value                                                           |
|---------------|-----------------------------------------------------------------|
| Test ID       | NFC_UD_STANDARD_SIXTEEN_GROUPPIDENTIFIER_ONE_AC                 |
| PICS          | Allow at least 16 reader_group_identifier per Access Credential |
| Applicability | M for User Device                                               |
| Interface     | NFC                                                             |

![](_page_59_Picture_8.jpeg)

**Table 7-16 NFC\_UD\_STANDARD\_SIXTEEN\_GROUPPIDENTIFIER\_ONE\_AC test pre-conditions** 

| Provision onto    | Remarks                                                             |
|-------------------|---------------------------------------------------------------------|
| DUT (User Device) | reader_PubK(i), reader_group_identifier(i), where i = 1, 2, 3, …16. |
| TH (Reader)       | Access Credential long term public key                              |

**Table 7-17 NFC\_UD\_STANDARD\_SIXTEEN\_GROUPPIDENTIFIER\_ONE\_AC test steps** 

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device) | Verification at TH                                                                                                                                                                             |
|-------|----------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                               |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                           |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                 |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                           |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                           |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5).                            |                      | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                           |
| 5     | Wait for at least 3 seconds.                                                                       |                      |                                                                                                                                                                                                |
| 6     | Repeat steps 1 through 5, for each of the<br>sixteen reader_group_identifier.                      |                      | Verify the following:<br>1.<br>All iterations PASS<br>2.<br>Same Access Credential long term<br>public key is used in each iteration<br>If all criteria above are met, then PASS<br>else FAIL. |

### **7.8 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with Chaining and incorrect Reader Cert signature**

**Table 7-18 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_SIGNATURE test identifiers** 

| Parameter         | Value                                                                       |  |
|-------------------|-----------------------------------------------------------------------------|--|
| Test ID           | NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCORRECT_SIGN<br>ATURE |  |
| PICS              | Verification of reader_Cert with the CA Public Key                          |  |
| Applicabilit<br>y | M for User Device                                                           |  |
| Interface         | NFC                                                                         |  |

![](_page_60_Picture_9.jpeg)

NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_SIGNATURE test preconditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

**Table 7-19 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_SIGNATURE test steps** 

| Steps | TH (Reader)                                                                                            | DUT (User<br>Device)          | Verification at TH                                                                                                                     |
|-------|--------------------------------------------------------------------------------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID<br>= A000000909ACCE5501.                                   |                               | If all criteria are met, then CONTINUE else FAIL.                                                                                      |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                     |                               | If all criteria are met, then CONTINUE else FAIL.                                                                                      |
| 3     | Send LOAD_CERT command<br>with fragmented reader_cert<br>with chaining                                 |                               |                                                                                                                                        |
| 4     |                                                                                                        | Send<br>LOAD_CERT<br>response | Verify the following:<br>1.<br>SW = 9000h.<br>2.<br>Response data field is empty.<br>If all criteria are met, then CONTINUE else FAIL. |
| 5     | Execute AUTH1 with SW != 9000h routine<br>(Table 5-4).<br>Reader_cert is not present in AUTH1 command. |                               | If all criteria are met, then CONTINUE else FAIL.                                                                                      |
| 6     | Execute CONTROL FLOW indicating<br>transaction failure routine (Table 5-7).                            |                               | If all criteria are met, then PASS else FAIL.                                                                                          |

# **7.9 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with Chaining and incorrect Reader Cert format**

**Table 7-20 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_FORMAT test identifiers** 

| Parameter         | Value                                                                    |  |
|-------------------|--------------------------------------------------------------------------|--|
| Test ID           | NFC_UD_NEG_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING_INCORRECT_FOR<br>MAT |  |
| PICS              | Verification of reader_Cert with the CA Public Key                       |  |
| Applicabilit<br>y | M for User Device                                                        |  |
| Interface         | NFC                                                                      |  |

NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_FORMAT test preconditions are identical to NFC\_UD\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 7-5.

![](_page_61_Picture_9.jpeg)

**Table 7-21 NFC\_UD\_NEG\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING\_INCORRECT\_FORMAT test steps** 

| Steps | TH (Reader)                                                                 | DUT (User<br>Device)          | Verification at TH                                                                                                                      |
|-------|-----------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID<br>= A000000909ACCE5501.        |                               | If all criteria are met, then CONTINUE else FAIL.                                                                                       |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.          |                               | If all criteria are met, then CONTINUE else FAIL.                                                                                       |
| 3     | Send LOAD_CERT command<br>with wrong value/length                           |                               |                                                                                                                                         |
| 4     |                                                                             | Send<br>LOAD_CERT<br>response | Verify the following:<br>1.<br>SW != 9000h.<br>2.<br>Response data field is empty.<br>If all criteria are met, then CONTINUE else FAIL. |
| 4     | Execute CONTROL FLOW indicating<br>transaction failure routine (Table 5-6). |                               | If all criteria are met, then PASS else FAIL.                                                                                           |

### **7.10 Step-Up Phase with Access Document**

#### **Table 7-22 NFC\_UD\_STEPUP\_AD test identifiers**

| Parameter     | Value                                 |  |
|---------------|---------------------------------------|--|
| Test ID       | NFC_UD_STEPUP_AD                      |  |
| PICS          | Step-Up Phase AND                     |  |
|               | Access Document storage and retrieval |  |
| Applicability | M for User Device                     |  |
| Interface     | NFC                                   |  |

#### **Table 7-23 NFC\_UD\_STEPUP\_AD test pre-conditions**

| Provision onto    | Remarks                                                |  |  |
|-------------------|--------------------------------------------------------|--|--|
| DUT (User Device) | reader_PubK, reader_group_identifier, Access Document  |  |  |
| TH (Reader)       | Access Credential long term public key, IssuerKey_PubK |  |  |

#### **Table 7-24 NFC\_UD\_STEPUP\_AD test steps**

| Steps | TH (Reader)                                                          | DUT (User<br>Device) | Verification at TH                                |
|-------|----------------------------------------------------------------------|----------------------|---------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set<br>AID = A000000909ACCE5501. |                      | If all criteria are met, then CONTINUE else FAIL. |

![](_page_62_Picture_11.jpeg)

| Steps | TH (Reader)                                                                                                                 | DUT (User<br>Device)                    | Verification at TH                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|----------------------------------------------------------|
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                                          |                                         | If all criteria are met, then CONTINUE else FAIL.        |
|       | auth0_command_vendor_extension is<br>present in AUTH0 command.                                                              |                                         |                                                          |
| 3     | Execute AUTH1 with SW = 9000h routine<br>(Table 5-3).                                                                       |                                         | If all criteria are met, then CONTINUE else FAIL.        |
|       | Reader_cert is not present in AUTH1<br>command.                                                                             |                                         |                                                          |
| 4     | If bit2 in signaling_bitmap in AUTH1<br>response is set to 1, then execute SELECT<br>routine. Set AID = A000000909ACCE5502. |                                         | If all criteria are met, then CONTINUE else FAIL.        |
| 5     | Request Access<br>Document using<br>DeviceRequest inside<br>ENVELOPE command.                                               |                                         |                                                          |
| 6     |                                                                                                                             | Send Access                             | Verify the following:                                    |
|       |                                                                                                                             | Document in<br>DeviceResponse<br>inside | Access Document is sent in ENVELOPE command<br>response. |
|       |                                                                                                                             | ENVELOPE<br>command<br>response         | If all criteria are met, then CONTINUE else FAIL.        |
| 7     | one or more GET RESPONSE command and<br>GET RESPONSE command response can be<br>exchanged.                                  |                                         |                                                          |
| 8     | Execute EXCHANGE indicating transaction<br>success routine (Table 5-5).                                                     |                                         | If all criteria are met, then PASS else FAIL.            |

### **7.11 Step-Up Phase with Revocation Document**

#### **Table 7-25 NFC\_UD\_STEPUP\_RD test identifiers**

| Parameter     | Value                                     |  |
|---------------|-------------------------------------------|--|
| Test ID       | NFC_UD_STEPUP_RD                          |  |
| PICS          | Step-Up Phase AND                         |  |
|               | Revocation Document storage and retrieval |  |
| Applicability | M for User Device                         |  |
| Interface     | NFC                                       |  |

### **Table 7-26 NFC\_UD\_STEPUP\_RD test pre-conditions**

| Provision onto    | Remarks                                                   |
|-------------------|-----------------------------------------------------------|
| DUT (User Device) | reader_PubK, reader_group_identifier, Revocation Document |
| TH (Reader)       | Access Credential long term public key, IssuerKey_PubK    |

![](_page_63_Picture_8.jpeg)

#### **Table 7-27 NFC\_UD\_STEPUP\_RD test steps**

| Steps | TH (Reader)                                                                                | DUT (User<br>Device)                                                                             | Verification at TH                                                                                                                         |
|-------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute test steps 1 through 4 in<br>NFC_UD_STEPUP_AD (Table 7-24)                         |                                                                                                  | If all criteria are met, then CONTINUE else FAIL.                                                                                          |
| 2     | Request Revocation<br>Document using<br>DeviceRequest inside<br>ENVELOPE command.          |                                                                                                  |                                                                                                                                            |
| 3     |                                                                                            | Send<br>Revocation<br>Document in<br>DeviceResponse<br>inside<br>ENVELOPE<br>command<br>response | Verify the following:<br>Revocation Document is sent in ENVELOPE<br>command response.<br>If all criteria are met, then CONTINUE else FAIL. |
| 7     | one or more GET RESPONSE command and<br>GET RESPONSE command response can be<br>exchanged. |                                                                                                  |                                                                                                                                            |
| 8     | Execute EXCHANGE indicating transaction<br>success routine (Table 5-5).                    |                                                                                                  | If all criteria are met, then PASS else FAIL.                                                                                              |

# **7.12 Step-Up Phase with Access Document and Revocation Document**

#### **Table 7-28 NFC\_UD\_STEPUP\_AD\_RD test identifiers**

| Parameter     | Value                                         |  |
|---------------|-----------------------------------------------|--|
| Test ID       | NFC_UD_STEPUP_AD_RD                           |  |
| PICS          | Step-Up Phase AND                             |  |
|               | Revocation Document storage and retrieval AND |  |
|               | Revocation Document storage and retrieval     |  |
| Applicability | M for User Device                             |  |
| Interface     | NFC                                           |  |

#### **Table 7-29 NFC\_UD\_STEPUP\_AD\_RD test pre-conditions**

| Provision onto    | Remarks                                                                    |  |
|-------------------|----------------------------------------------------------------------------|--|
| DUT (User Device) | reader_PubK, reader_group_identifier, Access Document, Revocation Document |  |
| TH (Reader)       | Access Credential long term public key, IssuerKey_PubK                     |  |

![](_page_64_Picture_9.jpeg)

**Table 7-30 NFC\_UD\_STEPUP\_AD\_RD test steps** 

| Steps | TH (Reader)                                                                                                       | DUT (User<br>Device)                                                                                                    | Verification at TH                                                                                                                                            |
|-------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute test steps 1 through 4 in<br>NFC_UD_STEPUP_AD (Table 7-24)                                                |                                                                                                                         | If all criteria are met, then CONTINUE else FAIL.                                                                                                             |
| 2     | Request Access<br>Document and<br>Revocation Document in<br>a single DeviceRequest<br>inside ENVELOPE<br>command. |                                                                                                                         |                                                                                                                                                               |
| 3     |                                                                                                                   | Send Access<br>Document and<br>Revocation<br>Document in<br>DeviceResponse<br>inside<br>ENVELOPE<br>command<br>response | Verify the following:<br>Access Document and Revocation Document is sent<br>in ENVELOPE command response<br>If all criteria are met, then CONTINUE else FAIL. |
| 7     | one or more GET RESPONSE command and<br>GET RESPONSE command response can be<br>exchanged.                        |                                                                                                                         |                                                                                                                                                               |
| 8     | Execute EXCHANGE indicating transaction<br>success routine (Table 5-5).                                           |                                                                                                                         | If all criteria are met, then PASS else FAIL.                                                                                                                 |

### **7.13 SELECT Response with User Device Descriptor Tag (provisional)**

**Table 7-31 NFC\_UD\_SELECT\_RESPONSE\_UD\_DESCRIPTOR\_TAG test identifiers** 

| Parameter     | Value                                                              |
|---------------|--------------------------------------------------------------------|
| Test ID       | NFC_UD_SELECT_RESPONSE_UD_DESCRIPTOR_TAG                           |
| PICS          | User Device Descriptor Tag                                         |
| Applicability | M for User Device that supports sending User Device Descriptor Tag |
| Interface     | NFC                                                                |

NFC\_UD\_SELECT\_RESPONSE\_UD\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-32 NFC\_UD\_SELECT\_RESPONSE\_UD\_DESCRIPTOR\_TAG test steps** 

| Steps | TH (Reader)                                                         | DUT (User<br>Device) | Verification at TH                                                           |
|-------|---------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1).<br>Set AID = A000000909ACCE5501 |                      | Verify the following in addition to all<br>verification in SELECT routine:   |
|       |                                                                     |                      | 1.<br>User Device Descriptor TLV structure is<br>present in SELECT response. |

![](_page_65_Picture_10.jpeg)

| Steps | TH (Reader)                                                                                           | DUT (User<br>Device) | Verification at TH                                                             |
|-------|-------------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------------------|
|       |                                                                                                       |                      | 2.<br>User Device Descriptor TLV structure<br>matches technical specification. |
|       |                                                                                                       |                      | If all criteria are met, then CONTINUE else<br>FAIL.                           |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                    |                      | If all criteria are met, then CONTINUE else<br>FAIL.                           |
| 3     | Execute AUTH1 with SW = 9000h routine (Table<br>5-3).<br>Reader_cert is not present in AUTH1 command. |                      | If all criteria are met, then CONTINUE else<br>FAIL.                           |
| 4     | Execute EXCHANGE indicating transaction success                                                       |                      | If all criteria are met, then PASS else FAIL.                                  |
|       | routine (Table 5-5).                                                                                  |                      |                                                                                |

# **7.14 AUTH0 Response with Chaining**

**Table 7-33 NFC\_UD\_AUTH0\_RESPONSE\_CHAINING test identifiers** 

| Parameter     | Value                          |
|---------------|--------------------------------|
| Test ID       | NFC_UD_AUTH0_RESPONSE_CHAINING |
| PICS          | Expedited-Standard Phase       |
| Applicability | M for User Device              |
| Interface     | NFC                            |

NFC\_UD\_AUTH0\_RESPONSE\_CHAINING test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-34 NFC\_UD\_AUTH0\_RESPONSE\_CHAINING test steps** 

| Steps | TH (Reader)                                                                                                                                                           | DUT (User<br>Device)                              | Verification at TH                                                                        |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                                                                                  |                                                   | If all criteria are met, then<br>CONTINUE else FAIL.                                      |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.<br>AUTH0 command with single or multiple<br>auth0_command_vendor_extension with chaining and le!=0 |                                                   | If all criteria are met, then<br>CONTINUE else FAIL.                                      |
| 3     | [Optional] Send one or more GET<br>RESPONSE command.                                                                                                                  |                                                   |                                                                                           |
| 4     |                                                                                                                                                                       | [Optional]<br>Send one or<br>more GET<br>RESPONSE | Verify AUTH0 response is chained.<br>If all criteria are met, then<br>CONTINUE else FAIL. |

![](_page_66_Picture_9.jpeg)

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device) | Verification at TH                                   |
|-------|----------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
|       |                                                                                                    | command<br>response. |                                                      |
| 5     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 6     | Execute EXCHANGE indicating transaction success routine<br>(Table 5-5).                            |                      | If all criteria are met, then PASS<br>else FAIL.     |

### **7.15 AUTH0 with Unknown Reader Identifier**

### **Table 7-35 NFC\_UD\_NEG\_AUTH0\_UNKNOWN\_READER\_ID test identifiers**

| Parameter     | Value                              |
|---------------|------------------------------------|
| Test ID       | NFC_UD_NEG_AUTH0_UNKNOWN_READER_ID |
| PICS          | Expedited-Standard Phase           |
| Applicability | M for User Device                  |
| Interface     | NFC                                |

#### **Table 7-36 NFC\_UD\_NEG\_AUTH0\_UNKNOWN\_READER\_ID test pre-conditions**

| Provision onto    | Remarks                                |
|-------------------|----------------------------------------|
| DUT (User Device) | reader_PubK                            |
| TH (Reader)       | Access Credential long term public key |

#### **Table 7-37 NFC\_UD\_NEG\_AUTH0\_UNKNOWN\_READER\_ID test steps**

| Steps | TH (Reader)                                                                                               | DUT (User<br>Device) | Verification at TH                                   |
|-------|-----------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                      |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set command_parameters<br>= 0h and reader_identifier to a random value |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 3     | Execute AUTH1 with SW != 9000h routine (Table 5-4).<br>Reader_cert is not present in AUTH1 command.       |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 4     | Execute CONTROL FLOW indicating transaction failure routine<br>(Table 5-7).                               |                      | If all criteria are met, then PASS<br>else FAIL.     |

![](_page_67_Picture_10.jpeg)

### **7.16 AUTH0 with unsupported Protocol Version**

**Table 7-38 NFC\_UD\_NEG\_AUTH0\_UNSUPPORTED\_PROTOCOL\_VERSION test identifiers** 

| Parameter     | Value                                         |
|---------------|-----------------------------------------------|
| Test ID       | NFC_UD_NEG_AUTH0_UNSUPPORTED_PROTOCOL_VERSION |
| PICS          | Expedited-Standard Phase                      |
| Applicability | M for User Device                             |
| Interface     | NFC                                           |

NFC\_UD\_NEG\_AUTH0\_UNSUPPORTED\_PROTOCOL\_VERSION test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-39 NFC\_UD\_NEG\_AUTH0\_UNSUPPORTED\_PROTOCOL\_VERSION test steps** 

| Steps | TH (Reader)                                                                                            | DUT (User<br>Device)   | Verification at TH                                                                                                                         |
|-------|--------------------------------------------------------------------------------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                   |                        | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                       |
| 3     | Send AUTH0 command with unsupported<br>expedited_phase_protocol_version and<br>command_parameters = 0h |                        |                                                                                                                                            |
| 4     |                                                                                                        | send AUTH0<br>response | Verify the following:<br>1.<br>SW != 9000h.<br>2.<br>Response data field is empty.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 5     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7).                            |                        | If all criteria are met, then PASS<br>else FAIL.                                                                                           |

### **7.17 AUTH0 with Extra Unknown TLV**

**Table 7-40 NFC\_UD\_NEG\_AUTH0\_EXTRA\_TAG test identifiers** 

| Parameter     | Value                      |
|---------------|----------------------------|
| Test ID       | NFC_UD_NEG_AUTH0_EXTRA_TAG |
| PICS          | Expedited-Standard Phase   |
| Applicability | M for User Device          |
| Interface     | NFC                        |

NFC\_UD\_NEG\_AUTH0\_EXTRA\_TAG test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

![](_page_68_Picture_12.jpeg)

**Table 7-41 NFC\_UD\_NEG\_AUTH0\_EXTRA\_TAG test steps** 

| Steps | TH (Reader)                                                                                                                                                                          | DUT (User<br>Device) | Verification at TH                                   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                                                                                                 |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h and add extra unknown tag in<br>TLV. Extra tag can be randomly injected at any location in the<br>command payload. |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command.                                                                                   |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 4     | Execute EXCHANGE indicating transaction success routine<br>(Table 5-5).                                                                                                              |                      | If all criteria are met, then PASS<br>else FAIL.     |

### **7.18 AUTH0 with Wrong Value**

**Table 7-42 NFC\_UD\_NEG\_AUTH0\_WRONG\_VALUE test identifiers** 

| Parameter     | Value                        |
|---------------|------------------------------|
| Test ID       | NFC_UD_NEG_AUTH0_WRONG_VALUE |
| PICS          | Expedited-Standard Phase     |
| Applicability | M for User Device            |
| Interface     | NFC                          |

NFC\_UD\_NEG\_AUTH0\_WRONG\_VALUE test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-43 NFC\_UD\_NEG\_AUTH0\_WRONG\_VALUE test steps** 

| Steps | TH (Reader)                                                                           | DUT (User<br>Device)      | Verification at TH                                                                                                                         |
|-------|---------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                  |                           | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                       |
| 2     | Send AUTH0 command with<br>command_parameters = 0h and wrong<br>value/length for tag. |                           |                                                                                                                                            |
| 3     |                                                                                       | send<br>AUTH0<br>response | Verify the following:<br>1.<br>SW != 9000h.<br>2.<br>Response data field is empty.<br>If all criteria are met, then<br>CONTINUE else FAIL. |

| Steps | TH (Reader)                                                                 | DUT (User<br>Device) | Verification at TH                               |
|-------|-----------------------------------------------------------------------------|----------------------|--------------------------------------------------|
| 4     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7). |                      | If all criteria are met, then PASS else<br>FAIL. |

# **7.19 AUTH0 with Wrong P1 and P2**

# **Table 7-44 NFC\_UD\_NEG\_AUTH0\_WRONG\_P1P2 test identifiers**

| Parameter     | Value                       |
|---------------|-----------------------------|
| Test ID       | NFC_UD_NEG_AUTH0_WRONG_P1P2 |
| PICS          | Expedited-Standard Phase    |
| Applicability | M for User Device           |
| Interface     | NFC                         |

NFC\_UD\_NEG\_AUTH0\_WRONG\_P1P2 test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-45 NFC\_UD\_NEG\_AUTH0\_WRONG\_P1P2 test steps** 

| Steps | TH (Reader)                                                                         | DUT (User<br>Device)      | Verification at TH                                                                                                                         |
|-------|-------------------------------------------------------------------------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                |                           | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                       |
| 2     | Send AUTH0 command with<br>command_parameters = 0h and wrong value of<br>P1 and P2. |                           |                                                                                                                                            |
| 3     |                                                                                     | send<br>AUTH0<br>response | Verify the following:<br>1.<br>SW != 9000h.<br>2.<br>Response data field is empty.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 4     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7).         |                           | If all criteria are met, then PASS<br>else FAIL.                                                                                           |

### **7.20 AUTH0 with Chaining Not Completed**

**Table 7-46 NFC\_UD\_NEG\_AUTH0\_CHAINING\_NOT\_COMPLETED test identifiers** 

| Parameter | Value                                   |  |
|-----------|-----------------------------------------|--|
| Test ID   | NFC_UD_NEG_AUTH0_CHAINING_NOT_COMPLETED |  |
| PICS      | Expedited-Standard Phase                |  |

![](_page_70_Picture_12.jpeg)

| Applicability |
|---------------|
|---------------|

NEG\_AUTH0\_CHAINING\_NOT\_COMPLETED test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-47 NFC\_UD\_NEG\_AUTH0\_CHAINING\_NOT\_COMPLETED test steps** 

| Steps | TH (Reader)                                                                                                                                                                       | DUT (User<br>Device)      | Verification at TH                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                                                                                              |                           | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Send AUTH0 command with<br>command_parameters = 0h and with single<br>auth0_command_vendor_extension with<br>command chaining and skipping sending the<br>last APDU in the chain. |                           |                                                      |
| 3     |                                                                                                                                                                                   | send<br>AUTH0<br>response |                                                      |
| 4     | Execute AUTH1 with SW != 9000h routine (Table 5-4)                                                                                                                                |                           | If all criteria are met, then<br>CONTINUE else FAIL. |
| 5     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7).                                                                                                       |                           | If all criteria are met, then PASS<br>else FAIL      |

# **7.21 AUTH0 with Different Cryptogram in Consecutive Expedited Fast Phase**

**Table 7-48 NFC\_UD\_NEG\_AUTH0\_DIFFERENT\_CRYPTOGRAM\_CONSECUTIVE\_FAST test identifiers** 

| Parameter     | Value                                                  |  |
|---------------|--------------------------------------------------------|--|
| Test ID       | NFC_UD_NEG_AUTH0_DIFFERENT_CRYPTOGRAM_CONSECUTIVE_FAST |  |
| PICS          | Expedited-Fast Phase AND                               |  |
|               | Cryptogram generation and validation                   |  |
| Applicability | M for User Device that support Expedited-Fast          |  |
| Interface     | NFC                                                    |  |

User Device and Reader do not have any information about each other as a pre-condition to this test.

**Table 7-49 NFC\_UD\_NEG\_AUTH0\_DIFFERENT\_CRYPTOGRAM\_CONSECUTIVE\_FAST test steps** 

| Steps | TH (Reader)                                                          | DUT (User<br>Device) | Verification at TH                                   |
|-------|----------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501. |                      | If all criteria are met, then CONTINUE else<br>FAIL. |

![](_page_71_Picture_12.jpeg)

| Steps | TH (Reader)                                                          | DUT (User<br>Device) | Verification at TH                                                                                                                       |
|-------|----------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 1h.   |                      | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                     |
| 3     | Wait at least 3 seconds.                                             |                      |                                                                                                                                          |
| 4     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501. |                      | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                     |
| 5     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 1h.   |                      | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                     |
|       |                                                                      |                      | Verify the following in AUTH0 command<br>response:                                                                                       |
|       |                                                                      |                      | 1.<br>Value of Tag 0x86h is different between<br>step 2 and step 5<br>2.<br>Value of Tag 0x9Dh is different between<br>step 2 and step 5 |
|       |                                                                      |                      | If all criteria are met, then PASS else FAIL.                                                                                            |

### **7.22 AUTH1 with Wrong Reader Signature**

**Table 7-50 NFC\_UD\_NEG\_AUTH1\_WRONG\_READER\_SIGNATURE test identifiers** 

| Parameter     | Value                                   |  |
|---------------|-----------------------------------------|--|
| Test ID       | NFC_UD_NEG_AUTH1_WRONG_READER_SIGNATURE |  |
| PICS          | Expedited-Standard Phase                |  |
| Applicability | M for User Device                       |  |
| Interface     | NFC                                     |  |

NFC\_UD\_NEG\_AUTH1\_WRONG\_READER\_SIGNATURE test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-51 NFC\_UD\_NEG\_AUTH1\_WRONG\_READER\_SIGNATURE test steps** 

| Steps | TH (Reader)                                                                                             | DUT (User<br>Device) | Verification at TH                                   |
|-------|---------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                    |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                      |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 3     | Execute AUTH1 with SW != 9000h routine (Table 5-4) and<br>send wrong reader signature in AUTH1 command. |                      | If all criteria are met, then<br>CONTINUE else FAIL. |

![](_page_72_Picture_9.jpeg)

| Steps | TH (Reader)                                                                 | DUT (User<br>Device) | Verification at TH                               |
|-------|-----------------------------------------------------------------------------|----------------------|--------------------------------------------------|
| 4     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7). |                      | If all criteria are met, then PASS<br>else FAIL. |

### **7.23 AUTH1 with Extra Tag**

#### **Table 7-52 NFC\_UD\_NEG\_AUTH1\_EXTRA\_TAG test identifiers**

| Parameter     | Value                      |
|---------------|----------------------------|
| Test ID       | NFC_UD_NEG_AUTH1_EXTRA_TAG |
| PICS          | Expedited-Standard Phase   |
| Applicability | M for User Device          |
| Interface     | NFC                        |

NFC\_UD\_NEG\_AUTH1\_EXTRA\_TAG test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-53 NFC\_UD\_NEG\_AUTH1\_EXTRA\_TAG test steps** 

| Steps | TH (Reader)                                                                                                                                                       | DUT (User<br>Device) | Verification at TH                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                                                                              |                      | If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                                                                                |                      | If all criteria are met, then CONTINUE<br>else FAIL. |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Add extra unknown tag in TLV. Extra tag can be randomly<br>injected at any location in the command payload. |                      | If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5).                                                                                           |                      | If all criteria are met, then PASS else<br>FAIL.     |

### **7.24 AUTH1 with Wrong P1 and P2**

**Table 7-54 NFC\_UD\_NEG\_AUTH1\_WRONG\_P1P2 test identifiers** 

| Parameter     | Value                       |
|---------------|-----------------------------|
| Test ID       | NFC_UD_NEG_AUTH1_WRONG_P1P2 |
| PICS          | Expedited-Standard Phase    |
| Applicability | M for User Device           |

![](_page_73_Picture_12.jpeg)

| Interface | NFC |
|-----------|-----|
|-----------|-----|

NFC\_UD\_NEG\_AUTH1\_WRONG\_P1P2 test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-55 NFC\_UD\_NEG\_AUTH1\_WRONG\_P1P2 test steps** 

| Steps | TH (Reader)                                                                                           | DUT (User<br>Device) | Verification at TH                                   |
|-------|-------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                  |                      | If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                    |                      | If all criteria are met, then CONTINUE<br>else FAIL. |
| 3     | Execute AUTH1 with SW != 9000h routine (Table 5-4).<br>Add wrong value of P1 and P2 in AUTH1 command. |                      | If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7).                           |                      | If all criteria are met, then PASS else<br>FAIL.     |

### **7.25 AUTH1 with Wrong Values**

**Table 7-56 NFC\_UD\_NEG\_AUTH1\_WRONG\_VALUES test identifiers** 

| Parameter     | Value                         |
|---------------|-------------------------------|
| Test ID       | NFC_UD_NEG_AUTH1_WRONG_VALUES |
| PICS          | Expedited-Standard Phase      |
| Applicability | M for User Device             |
| Interface     | NFC                           |

NFC\_UD\_NEG\_AUTH1\_WRONG\_VALUES test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-57 NFC\_UD\_NEG\_AUTH1\_WRONG\_VALUES test steps** 

| Steps | TH (Reader)                                                          | DUT (User<br>Device) | Verification at TH                                   |
|-------|----------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501. |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.   |                      | If all criteria are met, then<br>CONTINUE else FAIL. |

![](_page_74_Picture_12.jpeg)

| Steps | TH (Reader)                                                                                              | DUT (User<br>Device) | Verification at TH                                   |
|-------|----------------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 3     | Execute AUTH1 with SW != 9000h routine (Table 5-4)<br>with wrong value/length for tags in AUTH1 command. |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 4     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7).                              |                      | If all criteria are met, then PASS else<br>FAIL.     |

# **7.26 AUTH1 with Incomplete Chaining**

### **Table 7-58 NFC\_UD\_NEG\_AUTH1\_CHAINING\_NOT\_COMPLTED test identifiers**

| Parameter     | Value                                  |
|---------------|----------------------------------------|
| Test ID       | NFC_UD_NEG_AUTH1_CHAINING_NOT_COMPLTED |
| PICS          | Command Chaining                       |
| Applicability | M for User Device                      |
| Interface     | NFC                                    |

NFC\_UD\_NEG\_AUTH1\_CHAINING\_NOT\_COMPLTED test pre-conditions are identical to NFC\_UD\_STANDARD\_NO\_CERT test pre-conditions in Table 7-2.

**Table 7-59 NFC\_UD\_NEG\_AUTH1\_CHAINING\_NOT\_COMPLTED test steps** 

| Steps | TH (Reader)                                                                             | DUT (User<br>Device)   | Verification at TH                                                                     |
|-------|-----------------------------------------------------------------------------------------|------------------------|----------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                    |                        | If all criteria are met, then<br>CONTINUE else FAIL.                                   |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                      |                        | If all criteria are met, then<br>CONTINUE else FAIL.                                   |
| 3     | Send AUTH1 command with chaining and<br>skipping sending the last APDU in the<br>chain. |                        |                                                                                        |
| 4     |                                                                                         | send AUTH1<br>response | Abort at this step, if AUTH1 response<br>not sent. Otherwise, proceed to next<br>step. |
| 5     | Send Select with AID =<br>A000000909ACCE5502.                                           |                        |                                                                                        |
| 6     |                                                                                         | Select<br>Response     | Verify the following: SW ! = 9000h.                                                    |
|       |                                                                                         |                        | If all criteria are met, then<br>CONTINUE else FAIL.                                   |
| 7     | Execute CONTROL FLOW indicating transaction failure<br>routine (Table 5-7).             |                        | If all criteria are met, then PASS else<br>FAIL.                                       |

### **7.27 EXCHANGE with Mailbox Read Request**

### **Table 7-60 NFC\_UD\_EXCHANGE\_READ\_REQUEST test identifiers**

| Parameter     | Value                                                                                |
|---------------|--------------------------------------------------------------------------------------|
| Test ID       | NFC_UD_EXCHANGE_READ_REQUEST                                                         |
| PICS          | Mailbox - Read                                                                       |
| Applicability | M for User Device, if bit 4 in signaling_bitmap in AUTH1command response is set to 1 |
| Interface     | NFC                                                                                  |

#### **Table 7-61 NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions**

| Provision onto    | Remarks                                                                           |
|-------------------|-----------------------------------------------------------------------------------|
| DUT (User Device) | reader_PubK, reader_group_identifier, non-zero mailbox populated with random data |
| TH (Reader)       | Access Credential long term public key                                            |

#### **Table 7-62 NFC\_UD\_EXCHANGE\_READ\_REQUEST test steps**

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device)                    | Verification at TH                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                               |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                        |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                 |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                        |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                        |
| 4     | Send EXCHANGE command multiple<br>times with multiple READ requests from<br>mailbox                |                                         |                                                                                                                                                             |
| 5     |                                                                                                    | Send<br>Exchange<br>command<br>response | Verify the following:<br>Read requests return random data in<br>mailbox.<br>B1 and B2 are both 00h.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 6     | Execute EXCHANGE indicating transaction success routine<br>(Table 5-5).                            |                                         | If all criteria are met, then PASS else<br>FAIL.                                                                                                            |

### **7.28 EXCHANGE with Mailbox Write Request**

**Table 7-63 NFC\_UD\_EXCHANGE\_WRITE\_REQUEST test identifiers** 

| Parameter<br>Value |
|--------------------|
|--------------------|

![](_page_76_Picture_12.jpeg)

| Test ID       | NFC_UD_EXCHANGE_WRITE_REQUEST                                                        |  |
|---------------|--------------------------------------------------------------------------------------|--|
| PICS          | Mailbox - Write                                                                      |  |
| Applicability | M for User Device, if bit 5 in signaling_bitmap in AUTH1command response is set to 1 |  |
| Interface     | NFC                                                                                  |  |

NFC\_UD\_EXCHANGE\_WRITE\_REQUEST test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

**Table 7-64 NFC\_UD\_EXCHANGE\_WRITE\_REQUEST test steps** 

| Steps | TH (Reader)                                                                                                    | DUT (User<br>Device)                    | Verification at TH                                                                      |
|-------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                           |                                         | If all criteria are met, then CONTINUE else<br>FAIL.                                    |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                             |                                         | If all criteria are met, then CONTINUE else<br>FAIL.                                    |
| 3     | Execute AUTH1 with SW = 9000h routine (Table<br>5-3).                                                          |                                         | If all criteria are met, then CONTINUE else<br>FAIL.                                    |
|       | Reader_cert is not present in AUTH1 command.                                                                   |                                         |                                                                                         |
| 4     | Send EXCHANGE command<br>multiple times with multiple WRITE<br>requests to mailbox (atomic session =<br>TRUE). |                                         |                                                                                         |
| 5     |                                                                                                                | Send                                    | Verify the following:                                                                   |
|       |                                                                                                                | Exchange<br>command                     | Write requests do not fail.                                                             |
|       |                                                                                                                | response                                | B1 and B2 are both 00h.                                                                 |
|       |                                                                                                                |                                         | If all criteria are met, then CONTINUE else<br>FAIL.                                    |
| 6     | Send EXCHANGE command with<br>atomic session = FALSE and random<br>requests                                    |                                         |                                                                                         |
| 7     |                                                                                                                | Send<br>EXCHANGE<br>command<br>response | Verify the following:                                                                   |
|       |                                                                                                                |                                         | If Read Request is present, non-updated<br>data is returned.                            |
|       |                                                                                                                |                                         | B1 and B2 are both 00h.                                                                 |
|       |                                                                                                                |                                         | If all criteria are met, then CONTINUE else<br>FAIL.                                    |
| 8     | Send EXCHANGE command to read<br>data written to the mailbox                                                   |                                         |                                                                                         |
| 9     |                                                                                                                | Send                                    | Verify the following:                                                                   |
|       |                                                                                                                | EXCHANGE<br>command<br>response         | Read request should return final data in the<br>mailbox after closing of atomic session |
|       |                                                                                                                |                                         | B1 and B2 are both 00h.                                                                 |

| Steps | TH (Reader)                                                             | DUT (User<br>Device) | Verification at TH                                   |
|-------|-------------------------------------------------------------------------|----------------------|------------------------------------------------------|
|       |                                                                         |                      | If all criteria are met, then CONTINUE else<br>FAIL. |
| 10    | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5). |                      | If all criteria are met, then PASS else FAIL.        |

# **7.29 EXCHANGE with Set Request**

**Table 7-65 NFC\_UD\_EXCHANGE\_SET\_REQUEST test identifiers** 

| Parameter     | Value                                                                                |
|---------------|--------------------------------------------------------------------------------------|
| Test ID       | NFC_UD_EXCHANGE_SET_REQUEST                                                          |
| PICS          | Mailbox                                                                              |
| Applicability | M for User Device, if bit 5 in signaling_bitmap in AUTH1command response is set to 1 |
| Interface     | NFC                                                                                  |

NFC\_UD\_EXCHANGE\_SET\_REQUEST test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

**Table 7-66 NFC\_UD\_EXCHANGE\_SET\_REQUEST test steps** 

| Steps | TH (Reader)                                                                                               | DUT (User<br>Device)                    | Verification at TH                                                                                                                      |
|-------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                                      |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                    |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                        |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                    |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command.        |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                    |
| 4     | Send EXCHANGE command multiple<br>times with multiple SET requests to<br>mailbox (atomic session = TRUE). |                                         |                                                                                                                                         |
| 5     |                                                                                                           | Send<br>Exchange<br>command<br>response | Verify the following:<br>Write requests do not fail.<br>B1 and B2 are both 00h.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 6     | Send EXCHANGE command with atomic<br>session = FALSE and random requests                                  |                                         |                                                                                                                                         |
| 7     |                                                                                                           | Send<br>EXCHANGE<br>command<br>response | Verify the following:<br>If Read Request is present, non<br>updated data is returned.                                                   |

![](_page_78_Picture_9.jpeg)

| Steps | TH (Reader)                                                             | DUT (User<br>Device)            | Verification at TH                                                                          |
|-------|-------------------------------------------------------------------------|---------------------------------|---------------------------------------------------------------------------------------------|
|       |                                                                         |                                 | B1 and B2 are both 00h.                                                                     |
|       |                                                                         |                                 | If all criteria are met, then<br>CONTINUE else FAIL.                                        |
| 8     | Send EXCHANGE command to read data<br>written to the mailbox            |                                 |                                                                                             |
| 9     |                                                                         | Send                            | Verify the following:                                                                       |
|       |                                                                         | EXCHANGE<br>command<br>response | Read request should return final data<br>in the mailbox after closing of atomic<br>session. |
|       |                                                                         |                                 | B1 and B2 are both 00h.                                                                     |
|       |                                                                         |                                 | If all criteria are met, then<br>CONTINUE else FAIL.                                        |
| 10    | Execute EXCHANGE indicating transaction success routine<br>(Table 5-5). |                                 | If all criteria are met, then PASS else<br>FAIL.                                            |

# **7.30 EXCHANGE with Chaining**

**Table 7-67 NFC\_UD\_EXCHANGE\_WITH\_CHAINING test identifiers** 

| Parameter     | Value                         |
|---------------|-------------------------------|
| Test ID       | NFC_UD_EXCHANGE_WITH_CHAINING |
| PICS          | EXCHANGE command              |
| Applicability | M for User Device             |
| Interface     | NFC                           |

NFC\_UD\_EXCHANGE\_WITH\_CHAINING test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

**Table 7-68 NFC\_UD\_EXCHANGE\_WITH\_CHAINING test steps**

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device) | Verification at TH                                   |
|-------|----------------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                               |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                 |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                      | If all criteria are met, then<br>CONTINUE else FAIL. |
| 7     | Send EXCHANGE command multiple<br>times with chaining with Read/Write                              |                      |                                                      |

![](_page_79_Picture_9.jpeg)

| Steps | TH (Reader)                                                             | DUT (User<br>Device)                               | Verification at TH                                                |
|-------|-------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------|
|       | requests and le!=0 (atomic session =<br>TRUE)                           |                                                    |                                                                   |
| 8     |                                                                         | [Optional] Send<br>Exchange<br>command<br>response | Send GET RESPONSE multiple<br>times to retrieve complete response |
| 4     | Execute EXCHANGE indicating transaction success routine<br>(Table 5-5). |                                                    | If all criteria are met, then PASS else<br>FAIL.                  |

### **7.31 EXCHANGE with Extended Length**

**Table 7-69 NFC\_UD\_EXCHANGE\_WITH\_EXTENDED\_LENGTH test identifiers** 

| Parameter     | Value                                           |  |
|---------------|-------------------------------------------------|--|
| Test ID       | NFC_UD_EXCHANGE_WITH_EXTENDED_LENGTH            |  |
| PICS          | EXCHANGE command AND                            |  |
|               | Extended Length                                 |  |
| Applicability | M for User Device that supports Extended Length |  |
| Interface     | NFC                                             |  |

NFC\_UD\_EXCHANGE\_WITH\_EXTENDED\_LENGTH test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

**Table 7-70 NFC\_UD\_EXCHANGE\_WITH\_EXTENDED\_LENGTH test steps** 

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device)                    | Verification at TH                                                                                                                           |
|-------|----------------------------------------------------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                               |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                         |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                 |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                         |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                         |
| 4     | Send EXCHANGE command with<br>extended length APDU and large Read<br>request                       |                                         |                                                                                                                                              |
| 5     |                                                                                                    | Send<br>Exchange<br>command<br>response | Verify the following:<br>Reading Mailbox should not fail.<br>B1 and B2 are both 00h.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 6     | Execute EXCHANGE indicating transaction success routine<br>(Table 5-5).                            |                                         | If all criteria are met, then PASS else<br>FAIL.                                                                                             |

![](_page_80_Picture_9.jpeg)

# **7.32 EXCHANGE with Extra Tag**

**Table 7-71 NFC\_UD\_NEG\_EXCHANGE\_WITH\_EXTRA\_TAG test identifiers** 

| Parameter     | Value                              |
|---------------|------------------------------------|
| Test ID       | NFC_UD_NEG_EXCHANGE_WITH_EXTRA_TAG |
| PICS          | EXCHANGE command                   |
| Applicability | M for User Device                  |
| Interface     | NFC                                |

NFC\_UD\_NEG\_EXCHANGE\_WITH\_EXTRA\_TAG test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

**Table 7-72 NFC\_UD\_NEG\_EXCHANGE\_WITH\_EXTRA\_TAG test steps** 

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device)                    | Verification at TH                                                                                                                    |
|-------|----------------------------------------------------------------------------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                               |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                  |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                 |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                  |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                  |
| 4     | Send EXCHANGE command with extra<br>tag in encrypted payload                                       |                                         |                                                                                                                                       |
| 5     |                                                                                                    | Send<br>Exchange<br>command<br>response | Verify the following:<br>All requests should pass.<br>B1 and B2 are both 00h.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 6     | Execute EXCHANGE indicating transaction success<br>routine (Table 5-5).                            |                                         | If all criteria are met, then PASS else<br>FAIL.                                                                                      |

### **7.33 EXCHANGE with Mailbox Out of Bounds**

**Table 7-73 NFC\_UD\_NEG\_EXCHANGE\_MAILBOX\_OUT\_OF\_BOUNDS test identifiers** 

| Parameter     | Value                                     |
|---------------|-------------------------------------------|
| Test ID       | NFC_UD_NEG_EXCHANGE_MAILBOX_OUT_OF_BOUNDS |
| PICS          | Mailbox                                   |
| Applicability | M for User Device                         |

![](_page_81_Picture_11.jpeg)

| Interface | NFC |
|-----------|-----|
|           |     |

NFC\_UD\_NEG\_EXCHANGE\_MAILBOX\_OUT\_OF\_BOUNDS test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

**Table 7-74 NFC\_UD\_NEG\_EXCHANGE\_MAILBOX\_OUT\_OF\_BOUNDS test steps** 

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device)                    | Verification at TH                                                                                                                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1) Set AID =<br>A000000909ACCE5501.                                |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                                 |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                 |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                                 |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                                 |
| 4     | Send EXCHANGE command with<br>mailbox request with offset + length ><br>mailbox size               |                                         |                                                                                                                                                                                                                      |
| 5     |                                                                                                    | Send<br>Exchange<br>command<br>response | Verify the following:<br>Exchange command response SW =<br>9000h and response payload has<br>0x0002  B1  B2, where B1 and B2 are<br>implementation specific.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 6     | Execute CONTROL FLOW indicating transaction failure<br>(Table 5-7).                                |                                         | If all criteria are met, then PASS else<br>FAIL.                                                                                                                                                                     |

### **7.34 EXCHANGE with Wrong Length**

**Table 7-75 NFC\_UD\_NEG\_EXCHANGE\_WITH\_WRONG\_LENGTH test identifiers** 

| Parameter     | Value                                 |
|---------------|---------------------------------------|
| Test ID       | NFC_UD_NEG_EXCHANGE_WITH_WRONG_LENGTH |
| PICS          | EXCHANGE command                      |
| Applicability | M for User Device                     |
| Interface     | NFC                                   |

NFC\_UD\_NEG\_EXCHANGE\_WITH\_WRONG\_LENGTH test pre-conditions are identical to NFC\_UD\_EXCHANGE\_READ\_REQUEST test pre-conditions in Table 7-61.

![](_page_82_Picture_10.jpeg)

**Table 7-76 NFC\_UD\_NEG\_EXCHANGE\_WITH\_WRONG\_LENGTH test steps** 

| Steps | TH (Reader)                                                                                        | DUT (User<br>Device)                    | Verification at TH                                                                                                                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 5-1). Set AID =<br>A000000909ACCE5501.                               |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                                 |
| 2     | Execute AUTH0 routine (Table 5-2). Set<br>command_parameters = 0h.                                 |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                                 |
| 3     | Execute AUTH1 with SW = 9000h routine (Table 5-3).<br>Reader_cert is not present in AUTH1 command. |                                         | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                                                 |
| 4     | Send EXCHANGE command with wrong<br>length/value for tag                                           |                                         |                                                                                                                                                                                                                      |
| 5     |                                                                                                    | Send<br>Exchange<br>command<br>response | Verify the following:<br>Exchange command response SW =<br>9000h and response payload has<br>0x0002  B1  B2, where B1 and B2 are<br>implementation specific.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 6     | Execute CONTROL FLOW indicating transaction failure<br>(Table 5-7).                                |                                         | If all criteria are met, then PASS else<br>FAIL.                                                                                                                                                                     |

### **7.35 BLE+UWB Flow with Expedited Standard Phase**

**Table 7-77 BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test identifiers** 

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_EXPEDITED_STANDARD_PHASE             |  |
| PICS          | BLE + UWB Flow AND                             |  |
|               | UWB ranging AND                                |  |
|               | UWB Time Synchronization AND                   |  |
|               | Expedited-Standard Phase                       |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

**Table 7-78 BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions** 

| Provision onto                                                                                                  | Remarks                                     |  |  |  |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------|--|--|--|
| DUT (User Device)                                                                                               | reader_PubK, reader_group_identifier, GRK   |  |  |  |
| TH (Reader)                                                                                                     | Access Credential long term public key, GRK |  |  |  |
| NOTE 1: The TH (Reader) and the DUT (User Device) are in very close proximity (e.g., 1 m and line-of<br>sight). |                                             |  |  |  |
| NOTE 2: TH is in secured state as a pre-condition.                                                              |                                             |  |  |  |

![](_page_83_Picture_9.jpeg)

**Table 7-79 BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test steps** 

| Steps | TH (Reader)                                                                 | DUT (User<br>Device)                                                                            | Verification at TH                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol<br>routine (Table 5-8).               |                                                                                                 | If all criteria are met, then CONTINUE else FAIL.                                                                                                                                                    |
| 2     |                                                                             | Send Time<br>Sync<br>Message<br>ID.                                                             | Verify the following:<br>1.<br>Confirm Time Sync Message ID is received<br>by TH<br>2.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else FAIL. |
| 3     |                                                                             | Send<br>Ranging<br>Message<br>ID carrying<br>Initiate<br>Ranging<br>Session<br>Attribute<br>ID. | Verify the following:<br>Format of this message matches the specification.<br>If all criteria are met, then CONTINUE else FAIL.                                                                      |
| 4     | Execute BLE+UWB ranging session setup<br>routine (Table 5-9).               |                                                                                                 | If all criteria are met, then CONTINUE else FAIL.                                                                                                                                                    |
| 5     | Allow N (e.g., 3 seconds) for<br>UWB ranging to occur.                      |                                                                                                 | Verify the following:<br>UWB packets are exchanged over UWB transport.<br>If all criteria are met, then CONTINUE else FAIL.                                                                          |
| 6     | Reader Status Changed Message<br>ID carrying State Attribute ID is<br>sent. |                                                                                                 | Verify the following:<br>State Attribute ID has second byte [B7:B0] set to<br>0x01 or 0x02 or 0x81 or 0x82.<br>If all criteria are met, then PASS else FAIL.                                         |

### **7.36 BLE+UWB Flow with Expedited Fast Phase**

#### **Table 7-80 BLEUWB\_UD\_EXPEDITED\_FAST\_PHASE test identifiers**

| Parameter     | Value                                                                   |  |
|---------------|-------------------------------------------------------------------------|--|
| Test ID       | BLEUWB_UD_EXPEDITED_FAST_PHASE                                          |  |
| PICS          | BLE + UWB Flow AND                                                      |  |
|               | UWB ranging AND                                                         |  |
|               | UWB Time Synchronization AND                                            |  |
|               | Expedited-Fast Phase                                                    |  |
| Applicability | M for User Device that supports BLE + UWB Flow and Expedited-Fast phase |  |
| Interface     | BLE                                                                     |  |

![](_page_84_Picture_7.jpeg)

# BLEUWB\_UD\_EXPEDITED\_FAST\_PHASE test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

### **Table 7-81 BLEUWB\_UD\_EXPEDITED\_FAST\_PHASE test steps**

| Steps | TH (Reader)                                                                                                  | DUT (User Device)                                                                   | Verification at TH                                                                                                                                                         |
|-------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol routine<br>(Table 5-8).                                                |                                                                                     | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                       |
| 2     | BLE teardown                                                                                                 |                                                                                     |                                                                                                                                                                            |
| 3     | Send Bluetooth LE<br>advertisement                                                                           |                                                                                     |                                                                                                                                                                            |
| 4     |                                                                                                              | Establish L2CAP<br>connection                                                       |                                                                                                                                                                            |
| 5     |                                                                                                              | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501 | Verify the following:<br>Format of Initiate Access Protocol Message<br>ID matches specification.<br>If all criteria are met, then CONTINUE else<br>FAIL.                   |
| 6     | Send AUTH0 command<br>command_parameters =<br>1h<br>authentication_policy =<br>01h (User Device)             |                                                                                     |                                                                                                                                                                            |
| 7     |                                                                                                              | send AUTH0 response                                                                 | Verify the following:<br>Format of AUTH0 response matches<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                        |
| 8     | Send EXCHANGE<br>command                                                                                     |                                                                                     | Verify the following:<br>Tag 0x98 is present.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                                                      |
| 9     |                                                                                                              | Send EXCHANGE<br>response                                                           |                                                                                                                                                                            |
| 10    | Send Reader Status<br>Access Protocol<br>Completed Message ID<br>carrying Reader<br>Information Attribute ID |                                                                                     | Verify the following:<br>Ensure reader status is secured.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 11    |                                                                                                              | Send Time Sync<br>Message ID                                                        | Verify the following:<br>1.<br>Confirm Time Sync Message ID is<br>received by TH<br>2.<br>Format of message matches technical<br>specification.                            |

![](_page_85_Picture_5.jpeg)

| Steps | TH (Reader)                                                                 | DUT (User Device)                                                               | Verification at TH                                                                 |
|-------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
|       |                                                                             |                                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                               |
| 12    |                                                                             | Send Ranging Message<br>ID carrying Initiate<br>Ranging Session<br>Attribute ID | Verify the following:                                                              |
|       |                                                                             |                                                                                 | Format of this message matches the<br>specification.                               |
|       |                                                                             |                                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                               |
| 13    | Execute BLE+UWB ranging session setup routine<br>(Table 5-9).               |                                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                               |
| 14    | Allow N (e.g., 3 seconds)                                                   |                                                                                 | Verify the following:                                                              |
|       | for UWB ranging to<br>occur.                                                |                                                                                 | UWB packets are exchanged over UWB<br>transport.                                   |
|       |                                                                             |                                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                               |
| 15    | Reader Status Changed<br>Message ID carrying<br>State Attribute ID is sent. |                                                                                 | Verify the following:                                                              |
|       |                                                                             |                                                                                 | State Attribute ID has second byte [B7:B0]<br>set to 0x01 or 0x02 or 0x81 or 0x82. |
|       |                                                                             |                                                                                 | If all criteria are met, then PASS else FAIL.                                      |

### **7.37 BLE+UWB Flow with Step-Up Phase**

#### **Table 7-82 BLEUWB\_UD\_STEPUP\_PHASE test steps**

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_STEPUP_PHASE                         |  |
| PICS          | BLE + UWB Flow AND                             |  |
|               | UWB ranging AND                                |  |
|               | UWB Time Synchronization AND                   |  |
|               | Step-Up Phase                                  |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

#### **Table 7-83 BLEUWB\_UD\_STEPUP\_PHASE test pre-conditions**

| Provision onto                                                                                                  | Remarks                                                     |  |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--|
| DUT (User Device)                                                                                               | reader_PubK, reader_group_identifier, GRK, Access Document  |  |
| TH (Reader)                                                                                                     | Access Credential long term public key, GRK, IssuerKey_PubK |  |
| NOTE 1: The TH (Reader) and the DUT (User Device) are in very close proximity (e.g., 1 m and line-of<br>sight). |                                                             |  |
| NOTE 2: TH is in secured state as a pre-condition.                                                              |                                                             |  |

![](_page_86_Picture_8.jpeg)

#### **Table 7-84 BLEUWB\_UD\_STEPUP\_PHASE test steps**

| Steps | TH (Reader)                                                                                         | DUT (User Device)                                                                   | Verification at TH                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send Bluetooth LE<br>advertisement                                                                  |                                                                                     |                                                                                                                                                          |
| 2     |                                                                                                     | Establish L2CAP<br>connection                                                       |                                                                                                                                                          |
| 3     |                                                                                                     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501 | Verify the following:<br>Format of Initiate Access Protocol Message ID<br>matches specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 4     | Send AUTH0<br>command<br>command_parameters<br>= 0h<br>authentication_policy<br>= 01h (User Device) |                                                                                     |                                                                                                                                                          |
| 5     |                                                                                                     | send AUTH0 response                                                                 | Verify the following:                                                                                                                                    |
|       |                                                                                                     |                                                                                     | Format of AUTH0 response matches<br>specification.                                                                                                       |
|       |                                                                                                     |                                                                                     | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                     |
| 6     | Send AUTH1<br>command and<br>reader_cert is absent                                                  |                                                                                     |                                                                                                                                                          |
| 7     |                                                                                                     | send AUTH1 response                                                                 | Verify the following:                                                                                                                                    |
|       |                                                                                                     |                                                                                     | Format of AUTH1response matches<br>specification.                                                                                                        |
|       |                                                                                                     |                                                                                     | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                     |
| 8     | Send EXCHANGE                                                                                       |                                                                                     | Verify the following:                                                                                                                                    |
|       | command                                                                                             |                                                                                     | Tag 0x98 is present.                                                                                                                                     |
|       |                                                                                                     |                                                                                     | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                     |
| 9     |                                                                                                     | Send EXCHANGE<br>response                                                           |                                                                                                                                                          |
| 10    | Request Access<br>Document using<br>DeviceRequest inside<br>ENVELOPE<br>command                     |                                                                                     |                                                                                                                                                          |
| 11    |                                                                                                     | Send Access Document<br>in DeviceResponse<br>inside ENVELOPE<br>command response    | Verify the following:                                                                                                                                    |
|       |                                                                                                     |                                                                                     | Access Document is sent in ENVELOPE<br>command response.                                                                                                 |
|       |                                                                                                     |                                                                                     | If all criteria are met, then CONTINUE else<br>FAIL                                                                                                      |

| Steps | TH (Reader)                                                                                                     | DUT (User Device)                                                               | Verification at TH                                                                                                                                                                                      |
|-------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 12    | One or more GET RESPONSE command and<br>GET RESPONSE command response can be<br>exchanged.                      |                                                                                 |                                                                                                                                                                                                         |
| 13    | Send Reader Status<br>Access Protocol<br>Completed Message<br>ID carrying Reader<br>Information Attribute<br>ID |                                                                                 | Verify the following:<br>Ensure reader status is secured.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL.                              |
| 14    |                                                                                                                 | Send Time Sync<br>Message ID                                                    | Verify the following:<br>1.<br>Confirm Time Sync Message ID is<br>received by TH<br>2.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 15    |                                                                                                                 | Send Ranging Message<br>ID carrying Initiate<br>Ranging Session<br>Attribute ID | Verify the following:<br>Format of this message matches the<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                                                   |
| 16    | Execute BLE+UWB ranging session setup routine<br>(Table 5-9).                                                   |                                                                                 |                                                                                                                                                                                                         |
| 17    | Allow N (e.g., 3 seconds) for UWB ranging to<br>occur                                                           |                                                                                 | Verify the following:<br>UWB packets are exchanged over UWB<br>transport.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                                                       |
| 18    | Reader Status<br>Changed Message ID<br>carrying State<br>Attribute ID is sent                                   |                                                                                 | Verify the following:<br>State Attribute ID has second byte [B7:B0] set<br>to 0x01 or 0x02 or 0x81 or 0x82.<br>If all criteria are met, then PASS else FAIL.                                            |

### **7.38 BLE+UWB Flow with UWB Ranging Suspend**

#### **Table 7-85 BLEUWB\_UD\_RANGING\_SUSPEND test identifiers**

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_RANGING_SUSPEND                      |  |
| PICS          | BLE + UWB Flow AND<br>UWB ranging suspend      |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |

![](_page_88_Picture_6.jpeg)

| Interface | BLE |  |  |
|-----------|-----|--|--|
|           |     |  |  |

BLEUWB\_UD\_RANGING\_SUSPEND test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78 with the exception: The TH (Reader) and the DUT (User Device) are in close proximity (e.g., 5 m and line-of-sight).

**Table 7-86 BLEUWB\_UD\_RANGING\_SUSPEND test steps** 

| Steps | TH (Reader)                                                                    | DUT (User<br>Device)                                                               | Verification at TH                                                                                                                                                                                                                                                                                                                                   |
|-------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol<br>routine (Table 5-8).                  |                                                                                    | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                                                                                                                                 |
| 2     |                                                                                | Send Time Sync<br>Message ID                                                       | Verify the following:<br>1.<br>Confirm Time Sync Message ID is<br>received by TH<br>2.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                              |
| 3     |                                                                                | Send Ranging<br>Message ID<br>carrying Initiate<br>Ranging Session<br>Attribute ID | Verify the following:<br>Format of this message matches the<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                                                |
| 4     | Execute BLE+UWB ranging session setup routine<br>(Table 5-9).                  |                                                                                    | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                                                                                                                                 |
| 5     | Allow N (e.g., 3 seconds) for UWB ranging to<br>occur                          |                                                                                    | Verify the following:<br>UWB packets are exchanged over UWB<br>transport.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                                                    |
| 6     | Send Ranging Session<br>Suspend Request with correct<br>UWB Session Identifier |                                                                                    |                                                                                                                                                                                                                                                                                                                                                      |
| 7     |                                                                                | Send Ranging<br>Session Suspend<br>Response                                        | Verify the following<br>1.<br>this message is sent.<br>2.<br>format of Ranging Session Suspend<br>Response matches technical specification.<br>3.<br>No UWB packets are received over UWB<br>transport a short time (e.g., up to 3<br>seconds) after receiving Ranging Session<br>Suspend Response.<br>If all criteria are met, then PASS else FAIL. |
|       |                                                                                |                                                                                    | The status can either value 0 or 1.                                                                                                                                                                                                                                                                                                                  |

### **7.39 BLE+UWB Flow with UWB Ranging Resume**

**Table 7-87 BLEUWB\_UD\_RANGING\_RESUME test identifiers** 

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_RANGING_RESUME                       |  |
| PICS          | BLE + UWB Flow AND                             |  |
|               | UWB ranging resume                             |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

BLEUWB\_UD\_RANGING\_RESUME test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78 with the exception: The TH (Reader) and the DUT (User Device) are in close proximity (e.g., 5 m and line-of-sight)..

**Table 7-88 BLEUWB\_UD\_RANGING\_RESUME test steps** 

| Steps | TH (Reader)                                                                   | DUT (User<br>Device)                                                                     | Verification at TH                                                                                                                                                                                      |  |
|-------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 1     | Execute BLE+UWB Aliro Access Protocol<br>routine (Table 5-8).                 |                                                                                          | If all criteria are met, then CONTINUE else FAIL.                                                                                                                                                       |  |
| 2     |                                                                               | Send Time<br>Sync Message<br>ID                                                          | Verify the following:<br>1.<br>Confirm Time Sync Message ID is received by<br>TH<br>2.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else FAIL.    |  |
| 3     |                                                                               | Send Ranging<br>Message ID<br>carrying<br>Initiate<br>Ranging<br>Session<br>Attribute ID | Verify the following:<br>Format of this message matches the specification.<br>If all criteria are met, then CONTINUE else FAIL.                                                                         |  |
| 4     | Execute BLE+UWB ranging session setup<br>routine (Table 5-9).                 |                                                                                          | If all criteria are met, then CONTINUE else FAIL.                                                                                                                                                       |  |
| 5     | Allow N (e.g., 3 seconds) for UWB ranging<br>to occur                         |                                                                                          | Verify the following:<br>UWB packets are exchanged over UWB transport.<br>If all criteria are met, then CONTINUE else FAIL.                                                                             |  |
| 6     | Send Ranging Message ID<br>carrying Ranging Session<br>Suspended Attribute ID |                                                                                          | Verify the following:<br>No UWB packets are received over UWB transport a<br>short time (e.g., up to 3 seconds) after sending<br>Ranging Message ID carrying Ranging Session<br>Suspended Attribute ID. |  |

![](_page_90_Picture_8.jpeg)

| Steps | TH (Reader)                                                                     | DUT (User<br>Device)                                                                                                                                    | Verification at TH                                                                                                                                                                                                                                                                  |  |
|-------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 7     | 1 second after previous<br>step, send Ranging Session<br>Resume Request Message |                                                                                                                                                         |                                                                                                                                                                                                                                                                                     |  |
| 8     |                                                                                 | Send Ranging<br>Session<br>Resume<br>Response or<br>Ranging<br>Message ID<br>carrying<br>Initiate<br>Ranging<br>Session<br>Resume Later<br>Attribute ID | Verify the following:<br>1.<br>Ranging Session Resume Response or Ranging<br>Message ID carrying Initiate Ranging Session<br>Resume Later Attribute ID is sent.<br>2.<br>Format of the message matches technical<br>specification.<br>If all criteria are met, then PASS else FAIL. |  |

### **7.40 BLE+UWB Flow with User Device Descriptor Tag (provisional)**

| Parameter     | Value                                                                                                  |  |
|---------------|--------------------------------------------------------------------------------------------------------|--|
| Test ID       | BLEUWB_UD_UD_DESCRIPTOR_TAG                                                                            |  |
| PICS          | BLE + UWB Flow AND                                                                                     |  |
|               | User Device Descriptor Tag                                                                             |  |
| Applicability | M for User Device that supports BLE + UWB Flow and that supports sending User Device<br>Descriptor Tag |  |
| Interface     | BLE                                                                                                    |  |

BLEUWB\_UD\_UD\_DESCRIPTOR\_TAG test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-89 BLEUWB\_UD\_UD\_DESCRIPTOR\_TAG test steps** 

| Steps | TH (Reader)                                                   | DUT<br>(User<br>Device) | Verification at TH                                                                                                                                                                                                                                                                                                                                                                                                                                       |  |
|-------|---------------------------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 1     | Execute BLE+UWB Aliro Access Protocol<br>routine (Table 5-8). |                         | Verify the following in Initiate Access Protocol<br>Message ID in addition to other verifications in<br>BLE+UWB Aliro Access Protocol routine.<br>1.<br>Proprietary Information Attribute ID is present.<br>2.<br>The format of Proprietary Information ID matches<br>the technical specification.<br>3.<br>User Device Descriptor TLV structure is present in<br>Proprietary Information Attribute ID.<br>If all criteria are met, then PASS else FAIL. |  |

![](_page_91_Picture_8.jpeg)

### **7.41 BLE+UWB Flow with wrong advertisement format**

**Table 7-90 BLEUWB\_UD\_NEG\_WRONG\_ADV test identifiers**

| Parameter     | Value                                          |
|---------------|------------------------------------------------|
| Test ID       | BLEUWB_UD_NEG_WRONG_ADV                        |
| PICS          | BLE + UWB Flow                                 |
| Applicability | M for User Device that supports BLE + UWB Flow |
| Interface     | BLE                                            |

BLEUWB\_UD\_NEG\_WRONG\_ADV test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-91 BLEUWB\_UD\_NEG\_WRONG\_ADV test steps** 

| Steps | TH (Reader)                                                                                   | DUT (User Device)                                     | Verification at TH                                                                                                                                              |
|-------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send Bluetooth LE advertisement with bits 6 and<br>7 in byte 7, each set to 0 for 30 seconds. |                                                       |                                                                                                                                                                 |
| 2     |                                                                                               | No BLE connection<br>initiated by the User<br>Device. | Verify the following:<br>DUT (User Device)<br>does not establish<br>BLE connection with<br>the TH (Reader).<br>If all criteria are met,<br>then PASS else FAIL. |

### **7.42 BLE+UWB Flow with Failed L2CAP**

**Table 7-92 BLEUWB\_UD\_NEG\_FAILED\_L2CAP test identifiers** 

| Parameter                             | Value                                          |
|---------------------------------------|------------------------------------------------|
| Test ID<br>BLEUWB_UD_NEG_FAILED_L2CAP |                                                |
| PICS                                  | BLE + UWB Flow                                 |
| Applicability                         | M for User Device that supports BLE + UWB Flow |
| Interface                             | BLE                                            |

BLEUWB\_UD\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-93 BLEUWB\_UD\_NEG\_FAILED\_L2CAP test steps** 

| Steps                                 | TH (Reader)                                                     | DUT (User Device)                    | Verification at TH    |
|---------------------------------------|-----------------------------------------------------------------|--------------------------------------|-----------------------|
| 1<br>Send Bluetooth LE advertisement. |                                                                 |                                      |                       |
| 2                                     | Reader sends wrong Supported Aliro Ble UWB<br>Protocol Version. | Establish L2CAP<br>connection fails. | Verify the following: |

![](_page_92_Picture_14.jpeg)

| Steps | TH (Reader) | DUT (User Device) | Verification at TH                               |
|-------|-------------|-------------------|--------------------------------------------------|
|       |             |                   | L2CAP establishment<br>fails.                    |
|       |             |                   | If all criteria are met,<br>then PASS else FAIL. |

### **7.43 BLE+UWB Flow with timeout before AUTH0**

**Table 7-94 BLEUWB\_UD\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test identifiers** 

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_NEG_TIMEOUT_BEFORE_AUTH0             |  |
| PICS          | BLE + UWB Flow                                 |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

BLEUWB\_UD\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-95 BLEUWB\_UD\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test steps** 

| Steps | TH (Reader)                         | DUT (User Device)                                                                    | Verification at TH                                                                                                                                       |
|-------|-------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send Bluetooth LE<br>advertisement. |                                                                                      |                                                                                                                                                          |
| 2     |                                     | Establish L2CAP<br>connection.                                                       |                                                                                                                                                          |
| 3     |                                     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501. | Verify the following:<br>Format of Initiate Access Protocol<br>Message ID matches specification.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Do not send AUTH0<br>command.       |                                                                                      |                                                                                                                                                          |
| 5     |                                     | BLE teardown.                                                                        | Verify the following:                                                                                                                                    |
|       |                                     |                                                                                      | BLE teardown is initiated by the DUT<br>(User Device).                                                                                                   |
|       |                                     |                                                                                      | If all criteria are met, then PASS else<br>FAIL.                                                                                                         |

### **7.44 BLE+UWB Flow with Timeout Extension**

**Table 7-96 BLEUWB\_UD\_TIMEOUT\_EXTENSION test identifiers** 

| Parameter |
|-----------|
|-----------|

![](_page_93_Picture_12.jpeg)

| Test ID       | BLEUWB_UD_TIMEOUT_EXTENSION                    |  |
|---------------|------------------------------------------------|--|
| PICS          | BLE + UWB Flow                                 |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

BLEUWB\_UD\_TIMEOUT\_EXTENSION test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-97 BLEUWB\_UD\_TIMEOUT\_EXTENSION test steps** 

| Steps | TH (Reader)                                                                                                                                          | DUT (User Device)                                                                    | Verification at TH                                                                                                                                                                     |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Send Bluetooth LE advertisement.                                                                                                                     |                                                                                      |                                                                                                                                                                                        |
| 2     |                                                                                                                                                      | Establish L2CAP<br>connection.                                                       |                                                                                                                                                                                        |
| 3     |                                                                                                                                                      | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501. | Verify the following:<br>Format of Initiate Access Protocol<br>Message ID matches specification.<br>If all criteria are met, then CONTINUE<br>else FAIL.                               |
| 4     | Send Event Message ID carrying<br>Busy Attribute ID at 1 second after<br>receiving Initiate Access Protocol<br>Message ID.                           |                                                                                      |                                                                                                                                                                                        |
| 5     | 1 second of sending Event Busy Attribute ID, execute AUTH0<br>routine. Set command_parameters = 0h and<br>authentication_policy = 01h (User Device). |                                                                                      | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                   |
| 6     | Execute AUTH1 routine with SW = 9000h.<br>Reader_cert is not present in AUTH1 command.                                                               |                                                                                      | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                   |
| 7     | Send EXCHANGE command                                                                                                                                |                                                                                      | Verify the following:<br>Tag 0x98 is present.<br>If all criteria are met, then CONTINUE<br>else FAIL.                                                                                  |
| 8     |                                                                                                                                                      | Send EXCHANGE<br>response                                                            |                                                                                                                                                                                        |
| 9     | Send Reader Status Access<br>Protocol Completed Message ID<br>carrying Reader Information<br>Attribute ID                                            |                                                                                      | Verify the following:<br>Ensure reader status is secured or<br>unsecured.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then PASS else<br>FAIL. |

![](_page_94_Picture_6.jpeg)

### **7.45 BLE+UWB Flow with URSK Not Found**

**Table 7-98 BLEUWB\_UD\_NEG\_URSK\_NOT\_FOUND test identifiers** 

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_NEG_URSK_NOT_FOUND                   |  |
| PICS          | BLE + UWB Flow                                 |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

BLEUWB\_UD\_NEG\_URSK\_NOT\_FOUND test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-99 BLEUWB\_UD\_NEG\_URSK\_NOT\_FOUND test steps** 

| Steps | TH (Reader)                                                                                                                      | DUT (User Device)                                                                        | Verification at TH                                                                                                                |
|-------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol routine (Table<br>5-8).<br>When sending EXCHANGE command do not include Tag<br>0x98 in it. |                                                                                          | If all criteria are met, then CONTINUE<br>else FAIL.                                                                              |
| 2     |                                                                                                                                  | Send Event Message ID<br>carrying General Error<br>Attribute ID with URSK<br>unavailable | Verify the following:<br>Format of this message matches the<br>specification.<br>If all criteria are met, then PASS else<br>FAIL. |
| 3     | BLE teardown                                                                                                                     |                                                                                          |                                                                                                                                   |

### **7.46 BLE+UWB Flow with M1 Message Mismatch Parameter**

**Table 7-100 BLEUWB\_UD\_NEG\_M1\_MISMATCH\_PARAMETER test identifiers** 

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_NEG_M1_MISMATCH_PARAMETER            |  |
| PICS          | BLE + UWB Flow                                 |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

BLEUWB\_UD\_NEG\_M1\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-101 BLEUWB\_UD\_NEG\_M1\_MISMATCH\_PARAMETER test steps** 

| Steps | TH (Reader)                                                   | DUT<br>(User<br>Device) | Verification at TH                                |
|-------|---------------------------------------------------------------|-------------------------|---------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol<br>routine (Table 5-8). |                         | If all criteria are met, then CONTINUE else FAIL. |

![](_page_95_Picture_14.jpeg)

| Steps | TH (Reader)                                                          | DUT<br>(User<br>Device)                                                                                                | Verification at TH                                                                                                                                                                                   |
|-------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2     |                                                                      | Send Time<br>Sync<br>Message<br>ID                                                                                     | Verify the following:<br>1.<br>Confirm Time Sync Message ID is received<br>by TH<br>2.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else FAIL. |
| 3     |                                                                      | Send<br>Ranging<br>Message<br>ID<br>carrying<br>Initiate<br>Ranging<br>Session<br>Attribute<br>ID                      | Verify the following:<br>Format of this message matches the specification.<br>If all criteria are met, then CONTINUE else FAIL.                                                                      |
| 5     | Send Ranging Session Setup M1<br>Message ID without UWB Config<br>ID |                                                                                                                        |                                                                                                                                                                                                      |
| 6     |                                                                      | Send<br>Event<br>Message<br>ID<br>carrying<br>General<br>Error<br>Attribute<br>ID<br>indicating<br>Wrong<br>Parameters | Verify the following:<br>Format of Event Message ID.<br>General Error Attribute ID indicates Wrong<br>Parameters.<br>If all criteria are met, then PASS else FAIL.                                   |
| 7     | BLE teardown                                                         |                                                                                                                        |                                                                                                                                                                                                      |

### **7.47 BLE+UWB Flow with M3 Message Mismatch Parameter**

**Table 7-102 BLEUWB\_UD\_NEG\_M3\_MISMATCH\_PARAMETER test identifiers** 

| Parameter     | Value                                          |
|---------------|------------------------------------------------|
| Test ID       | BLEUWB_UD_NEG_M3_MISMATCH_PARAMETER            |
| PICS          | BLE + UWB Flow                                 |
| Applicability | M for User Device that supports BLE + UWB Flow |
| Interface     | BLE                                            |

BLEUWB\_UD\_NEG\_M3\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

![](_page_96_Picture_7.jpeg)

**Table 7-103 BLEUWB\_UD\_NEG\_M3\_MISMATCH\_PARAMETER test steps** 

| Steps | TH (Reader)                                                           | DUT (User<br>Device)                                                                                 | Verification at TH                                                                                                                                                                                      |
|-------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol routine<br>(Table 5-8).         |                                                                                                      | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                                    |
| 2     |                                                                       | Send Time Sync<br>Message ID                                                                         | Verify the following:<br>1.<br>Confirm Time Sync Message ID is<br>received by TH<br>2.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 3     |                                                                       | Send Ranging<br>Message ID<br>carrying Initiate<br>Ranging Session<br>Attribute ID                   | Verify the following:<br>Format of this message matches the<br>specification.<br>If all criteria are met, then CONTINUE<br>else FAIL.                                                                   |
| 4     | Send Ranging Session Setup M1<br>Message ID                           |                                                                                                      |                                                                                                                                                                                                         |
| 5     |                                                                       | Send Ranging<br>Session Setup M2<br>Message ID                                                       |                                                                                                                                                                                                         |
| 6     | Send Ranging Session Setup M3<br>Message ID without RAN<br>Multiplier |                                                                                                      |                                                                                                                                                                                                         |
| 7     |                                                                       | Send Event<br>Message ID<br>carrying General<br>Error Attribute ID<br>indicating Wrong<br>Parameters | Verify the following:<br>Format of Event Message ID.<br>General Error Attribute ID indicates<br>Wrong Parameters.<br>If all criteria are met, then PASS else<br>FAIL.                                   |
| 8     | BLE teardown                                                          |                                                                                                      |                                                                                                                                                                                                         |

### **7.48 BLE+UWB Flow with Suspend Request Mismatch Parameter**

**Table 7-104 BLEUWB\_UD\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test identifiers** 

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_NEG_SUSPEND_MISMATCH_PARAMETER       |  |
| PICS          | BLE + UWB Flow AND                             |  |
|               | UWB Ranging Suspend                            |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

![](_page_97_Picture_7.jpeg)

BLEUWB\_UD\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-105 BLEUWB\_UD\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test steps** 

| Steps | TH (Reader)                                                                                                                                             | DUT (User Device)                                                                                 | Verification at TH                                                                                                                                                    |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute<br>BLEUWB_UD_RANGING_SUSPEND<br>test steps (Table 7-86).<br>Send Ranging Session Suspend Request<br>with an incorrect UWB Session<br>Identifier | Send Event Message<br>ID carrying General<br>Error Attribute ID<br>indicating Wrong<br>Parameters | Verify the following:<br>Format of Event Message ID.<br>General Error Attribute ID<br>indicates Wrong Parameters.<br>If all criteria are met, then PASS<br>else FAIL. |
| 2     | BLE teardown                                                                                                                                            |                                                                                                   |                                                                                                                                                                       |

### **7.49 BLE+UWB Flow with Resume Request Mismatch Parameter**

**Table 7-106 BLEUWB\_UD\_NEG\_RESUME\_MISMATCH\_PARAMETER test identifiers** 

| Parameter     | Value                                          |  |
|---------------|------------------------------------------------|--|
| Test ID       | BLEUWB_UD_NEG_RESUME_MISMATCH_PARAMETER        |  |
| PICS          | BLE + UWB Flow AND<br>UWB Ranging Resume       |  |
| Applicability | M for User Device that supports BLE + UWB Flow |  |
| Interface     | BLE                                            |  |

BLEUWB\_UD\_NEG\_RESUME\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-107 BLEUWB\_UD\_NEG\_RESUME\_MISMATCH\_PARAMETER test steps** 

| Steps | TH (Reader)                                                                                                                                         | DUT (User Device)                                                                               | Verification at TH                                                                                                                                                    |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute<br>BLEUWB_UD_RANGING_RESUME<br>test steps (Table 7-88). Send Ranging<br>Session Resume Request with an<br>incorrect UWB Session Identifier. | Send Event Message ID<br>carrying General Error<br>Attribute ID indicating<br>Wrong Parameters. | Verify the following:<br>Format of Event Message ID.<br>General Error Attribute ID<br>indicates Wrong Parameters.<br>If all criteria are met, then<br>PASS else FAIL. |
| 2     | BLE teardown                                                                                                                                        |                                                                                                 |                                                                                                                                                                       |

![](_page_98_Picture_11.jpeg)

### **7.50 BLE-Only Flow with Expedited Standard Phase (provisional)**

**Table 7-108 BLERKE\_UD\_EXPEDITED\_STANDARD\_PHASE test identifiers** 

| Parameter     | Value                                         |  |
|---------------|-----------------------------------------------|--|
| Test ID       | BLERKE_UD_EXPEDITED_STANDARD_PHASE            |  |
| PICS          | BLE-Only Flow AND                             |  |
|               | Explicit Reader Selection                     |  |
| Applicability | M for User Device that supports BLE-Only Flow |  |
| Interface     | BLE                                           |  |

BLERKE\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

**Table 7-109 BLERKE\_UD\_EXPEDITED\_STANDARD\_PHASE test steps** 

| Steps | TH (Reader)                                                              | DUT (User Device)                                              | Verification at TH                                                                                                                                                                         |
|-------|--------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE-Only Aliro Access Protocol routine (Table<br>5-10).          |                                                                | If all criteria are met, then<br>CONTINUE else FAIL.                                                                                                                                       |
| 2     |                                                                          | Send RKE Request<br>Message ID carrying<br>Action Attribute ID | Verify the following:<br>Format of Message ID matches the<br>technical specification.<br>If all criteria are met, then<br>CONTINUE else FAIL.                                              |
| 3     | Send Reader Status Changed<br>Message ID carrying State<br>Attribute ID. |                                                                | Verify the following:<br>Format of Reader Status Changed<br>Message ID carrying State Attribute<br>ID matches technical specification.<br>If all criteria are met, then PASS else<br>FAIL. |

### **7.51 BLE-Only Flow with User Device Descriptor Tag (provisional)**

**Table 7-110 BLERKE\_UD\_UD\_DESCRIPTOR\_TAG test identifiers** 

| Parameter     | Value                                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------|
| Test ID       | BLERKE_UD_UD_DESCRIPTOR_TAG                                                                           |
| PICS          | BLE-Only Flow                                                                                         |
| Applicability | M for User Device that supports BLE-Only Flow and that supports sending User Device<br>Descriptor Tag |
| Interface     | BLE                                                                                                   |

BLERKE\_UD\_UD\_DESCRIPTOR\_TAG test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

![](_page_99_Picture_12.jpeg)

#### **Table 7-111 BLERKE\_UD\_UD\_DESCRIPTOR\_TAG test steps**

| Steps | TH (Reader)                                                     | DUT<br>(User<br>Device) | Verification at TH                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------|-----------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE-Only Aliro Access Protocol routine<br>(Table 5-10). |                         | Verify the following in Initiate Access<br>Protocol RKE Message ID, in addition to<br>verifying BLE-Only Aliro Access Protocol<br>routine:<br>1.<br>Proprietary Information Attribute ID is<br>present<br>2.<br>The format of Proprietary Information<br>ID is matching technical specification<br>3.<br>User Device Descriptor TLV structure<br>is present in Proprietary Information<br>Attribute ID<br>If all criteria are met, then PASS else FAIL. |

### **7.52 BLE-Only Flow with Failed L2CAP (provisional)**

**Table 7-112 BLERKE\_UD\_NEG\_FAILED\_L2CAP test identifiers** 

| Parameter     | Value                                         |
|---------------|-----------------------------------------------|
| Test ID       | BLERKE_UD_NEG_FAILED_L2CAP                    |
| PICS          | BLE-Only Flow                                 |
| Applicability | M for User Device that supports BLE-Only Flow |
| Interface     | BLE                                           |

BLERKE\_UD\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_UD\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 7-78.

BLERKE\_UD\_NEG\_FAILED\_L2CAP test steps are identical to BLEUWB\_UD\_NEG\_FAILED\_L2CAP test steps in Table 7-93.

![](_page_100_Picture_9.jpeg)

# **8 Reader Under Test Conformance Tests**

# **8.1 Expedited Standard Phase without Reader Certificate**

**Table 8-1 NFC\_RDR\_STANDARD\_NO\_CERT test identifiers**

| Parameter     | Value                                                            |  |
|---------------|------------------------------------------------------------------|--|
| Test ID       | NFC_RDR_STANDARD_NO_CERT                                         |  |
| PICS          | Expedited-Standard Phase AND                                     |  |
|               | Reader signature generation and validation using reader_PubK AND |  |
|               | Device signature generation and validation AND                   |  |
|               | AUTH1 command parameter                                          |  |
| Applicability | M for Reader                                                     |  |
| Interface     | NFC                                                              |  |

#### **Table 8-2 NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions**

| Provision onto   | Remarks                                |  |
|------------------|----------------------------------------|--|
| DUT (Reader)     | Access Credential long term public key |  |
| TH (User Device) | reader_PubK, reader_group_identifier   |  |

#### **Table 8-3 NFC\_RDR\_STANDARD\_NO\_CERT test steps**

| Steps | TH (User Device)                                                        | DUT (Reader) | Verification at TH                                   |
|-------|-------------------------------------------------------------------------|--------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501     |              | If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | Execute AUTH0 routine (Table 6-2).                                      |              | If all criteria are met, then CONTINUE<br>else FAIL. |
| 3     | Execute AUTH1 routine (Table 6-3).                                      |              | If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4). |              | If all criteria are met, then PASS else<br>FAIL.     |

### **8.2 Expedited Standard Phase with Reader Certificate in LOAD\_CERT with APDU Chaining**

#### **Table 8-4 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test identifiers**

| Parameter | Value                                            |
|-----------|--------------------------------------------------|
| Test ID   | NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_WITH_CHAINING |
| PICS      | Expedited-Standard Phase AND                     |

![](_page_101_Picture_13.jpeg)

|               | Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND |
|---------------|-----------------------------------------------------------------------------------------------------|
|               | Device signature generation and validation AND                                                      |
|               | Presentation and validation of the reader_Cert in LOAD_CERT command AND                             |
|               | Command chaining AND                                                                                |
|               | AUTH1 command parameter                                                                             |
| Applicability | M for Reader                                                                                        |
| Interface     | NFC                                                                                                 |

#### **Table 8-5 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions**

| Provision onto                                                                  | Remarks                                |  |
|---------------------------------------------------------------------------------|----------------------------------------|--|
| DUT (Reader)                                                                    | Access Credential long term public key |  |
| TH (User Device)<br>Reader System Issuer CA public key, reader_group_identifier |                                        |  |

### **Table 8-6 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test steps**

| Steps | TH (User Device)                                                        | DUT (Reader)                                                              | Verification at TH                                                                                               |
|-------|-------------------------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501     |                                                                           | If all criteria are met, then CONTINUE<br>else FAIL.                                                             |
| 2     | Execute AUTH0 routine (Table 6-2).                                      |                                                                           | If all criteria are met, then CONTINUE<br>else FAIL.                                                             |
| 3     |                                                                         | Send LOAD_CERT<br>command with<br>fragmented reader_cert<br>with chaining | Verify the following:<br>reader_cert with chaining sent.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Send LOAD_CERT<br>Response                                              |                                                                           |                                                                                                                  |
| 5     | Execute AUTH1 routine (Table 6-3).                                      |                                                                           | If all criteria are met, then CONTINUE<br>else FAIL.                                                             |
| 6     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4). |                                                                           | If all criteria are met, then PASS else<br>FAIL.                                                                 |

### **8.3 Expedited Standard Phase with Reader Cert in LOAD\_CERT without APDU Chaining**

**Table 8-7 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test identifiers** 

| Parameter | Value                                          |
|-----------|------------------------------------------------|
| Test ID   | NFC_RDR_STANDARD_CERT_IN_LOAD_CERT_NO_CHAINING |
| PICS      | Expedited-Standard Phase AND                   |

![](_page_102_Picture_10.jpeg)

| Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND |                                                                         |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
|                                                                                                     | Device signature generation and validation AND                          |
|                                                                                                     | Presentation and validation of the reader_Cert in LOAD_CERT command AND |
|                                                                                                     | Extended length AND                                                     |
|                                                                                                     | AUTH1 command parameter                                                 |
| Applicability                                                                                       | M for Reader, if it supports Extended length APDUs                      |
| Interface                                                                                           | NFC                                                                     |

NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test pre-conditions are identical to NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

**Table 8-8 NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_NO\_CHAINING test steps** 

| Steps | TH (User Device)                                                        | DUT (Reader)                                                     | Verification at TH                                                                                                  |
|-------|-------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501     |                                                                  | If all criteria are met, then CONTINUE<br>else FAIL.                                                                |
| 2     | Execute AUTH0 routine (Table 6-2).                                      |                                                                  | If all criteria are met, then CONTINUE<br>else FAIL.                                                                |
| 3     |                                                                         | Send LOAD_CERT<br>command with<br>reader_cert and no<br>chaining | Verify the following:<br>Reader_cert sent without chaining.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Send LOAD_CERT<br>Response                                              |                                                                  |                                                                                                                     |
| 5     | Execute AUTH1 routine (Table 6-3).                                      |                                                                  | If all criteria are met, then CONTINUE<br>else FAIL.                                                                |
| 6     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4). |                                                                  | If all criteria are met, then PASS else<br>FAIL.                                                                    |

### **8.4 Expedited Standard Phase with Reader Cert in AUTH1 with APDU Chaining**

**Table 8-9 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test identifiers** 

| Parameter | Value                                                                                               |  |
|-----------|-----------------------------------------------------------------------------------------------------|--|
| Test ID   | NFC_RDR_STANDARD_CERT_IN_AUTH1_WITH_CHAINING                                                        |  |
| PICS      | Expedited-Standard Phase AND                                                                        |  |
|           | Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND |  |
|           | Device signature generation and validation AND                                                      |  |
|           | Presentation and validation of the reader_Cert in AUTH1 command AND                                 |  |
|           | Command chaining AND                                                                                |  |

![](_page_103_Picture_9.jpeg)

|               | AUTH1 command parameter |
|---------------|-------------------------|
| Applicability | M for Reader            |
| Interface     | NFC                     |

NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test pre-conditions are identical to NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

**Table 8-10 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_WITH\_CHAINING test steps** 

| Steps | TH (User Device)                                                                                   | DUT (Reader) | Verification at TH                                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501                                |              | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                 |
| 2     | Execute AUTH0 routine (Table 6-2).                                                                 |              | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                 |
| 3     | Execute AUTH1 routine (Table 6-3).<br>fragmented reader_cert with chaining over multiple<br>APDUs. |              | Verify AUTH1 routine criteria and the<br>following:<br>Reader_cert chaining.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4).                            |              | If all criteria are met, then PASS else<br>FAIL.                                                                                     |

### **8.5 Expedited Standard Phase with Reader Cert in AUTH1 without Chaining**

**Table 8-11 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test steps** 

| Parameter     | Value                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------|
| Test ID       | NFC_RDR_STANDARD_CERT_IN_AUTH1_NO_CHAINING                                                             |
| PICS          | Expedited-Standard Phase AND                                                                           |
|               | Reader signature generation and validation using intermediate_reader_PubK (from<br>reader_Cert) AND    |
|               | Device signature generation and validation AND                                                         |
|               | Presentation and validation of the reader_Cert in AUTH1 command AND                                    |
|               | Extended length AND                                                                                    |
|               | AUTH1 command parameter                                                                                |
| Applicability | M for Reader, if it supports Extended length APDU and supports sending reader_Cert in<br>AUTH1 command |
| Interface     | NFC                                                                                                    |

NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test pre-conditions are identical to NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

![](_page_104_Picture_10.jpeg)

**Table 8-12 NFC\_RDR\_STANDARD\_CERT\_IN\_AUTH1\_NO\_CHAINING test steps** 

| Steps | TH (User Device)                                                                        | DUT (Reader) | Verification at TH                                                                                                                         |
|-------|-----------------------------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501                     |              | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                       |
| 2     | Execute AUTH0 routine (Table 6-2).                                                      |              | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                       |
| 3     | Execute AUTH1 routine (Table 6-3).<br>reader_cert with no chaining over multiple APDUs. |              | Verify AUTH1 routine criteria and the<br>following:<br>Reader_cert is not chained.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4).                 |              | If all criteria are met, then PASS else<br>FAIL.                                                                                           |

### **8.6 Expedited Fast Phase**

**Table 8-13 NFC\_RDR\_FAST test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_FAST                                    |
| PICS          | Expedited-fast AND                              |
|               | Cryptogram generation and validation            |
| Applicability | M for Reader that supports Expedited-Fast Phase |
| Interface     | NFC                                             |

NFC\_RDR\_FAST test pre-conditions are identical to

NFC\_RDR\_STANDARD\_CERT\_IN\_LOAD\_CERT\_WITH\_CHAINING test pre-conditions in Table 8-5.

**Table 8-14 NFC\_RDR\_FAST test steps** 

| Steps | TH (User Device)                                                                                       | DUT (Reader) | Verification at TH                                   |
|-------|--------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------|
| 1     | Execute NFC_RDR_STANDARD_NO_CERT test steps<br>(Table 8-3)                                             |              | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Wait for at least 3 seconds.                                                                           |              |                                                      |
| 3     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501                                    |              | If all criteria are met, then<br>CONTINUE else FAIL. |
| 4     | Execute AUTH0 routine (Table 6-2). Use reader_identifier<br>value from step 1. command_parameters = 1h |              | If all criteria are met, then<br>CONTINUE else FAIL. |

![](_page_105_Picture_11.jpeg)

| Steps | TH (User Device)                                                        | DUT (Reader) | Verification at TH                               |
|-------|-------------------------------------------------------------------------|--------------|--------------------------------------------------|
| 5     | Execute EXCHANGE indicating transaction success routine<br>(Table 6-4). |              | If all criteria are met, then PASS<br>else FAIL. |

# **8.7 Step-Up Phase with Minimal Access Document with Key Identifier**

#### **Table 8-15 NFC\_RDR\_STEPUP\_AD\_KEY\_ID test identifiers**

| Parameter     | Value                                    |
|---------------|------------------------------------------|
| Test ID       | NFC_RDR_STEPUP_AD_KEY_ID                 |
| PICS          | Step-Up Phase AND                        |
|               | Step-Up AID Select AND                   |
|               | Access document storage and retrieval    |
| Applicability | M for Reader that supports Step-Up Phase |
| Interface     | NFC                                      |

#### **Table 8-16 NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions**

| Provision onto   | Remarks                                               |
|------------------|-------------------------------------------------------|
| DUT (Reader)     | IssuerKey_PubK                                        |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document |

### **Table 8-17 NFC\_RDR\_STEPUP\_AD\_KEY\_ID test steps**

| Steps | TH (User Device)                                                    | DUT (Reader)                                                                                                                                  | Verification at TH                                   |
|-------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501 |                                                                                                                                               | If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | Execute AUTH0 routine (Table 6-2).                                  |                                                                                                                                               | If all criteria are met, then CONTINUE<br>else FAIL. |
| 3     | Execute AUTH1 routine (Table 6-3).                                  |                                                                                                                                               | If all criteria are met, then CONTINUE<br>else FAIL. |
| 4     |                                                                     | Send SELECT command<br>AID =<br>A000000909ACCE5502,<br>if Step-Up AID is<br>required is indicated in<br>signaling_bitmap in<br>AUTH1 response | If all criteria are met, then CONTINUE<br>else FAIL. |
| 5     | Send SELECT response                                                |                                                                                                                                               |                                                      |
| 6     |                                                                     | Request Access<br>Document using                                                                                                              | Verify the following:                                |

![](_page_106_Picture_10.jpeg)

| Steps | TH (User Device)                                                                                | DUT (Reader)                              | Verification at TH                                            |
|-------|-------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------------------------------------|
|       |                                                                                                 | DeviceRequest inside<br>ENVELOPE command. | Access Document is requested in<br>ENVELOPE command response. |
|       |                                                                                                 |                                           | If all criteria are met, then CONTINUE<br>else FAIL.          |
| 7     | Send appropriate Access<br>Document in<br>DeviceResponse inside<br>ENVELOPE command<br>response |                                           |                                                               |
| 8     | One or more GET RESPONSE command and GET<br>RESPONSE command response can be exchanged.         |                                           |                                                               |
| 9     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4).                         |                                           | If all criteria are met, then PASS else<br>FAIL.              |

### **8.8 Step-Up Phase with Minimal Access Document with Issuer Certificate**

**Table 8-18 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_STEPUP_AD_ISSUER_CERT                   |
| PICS          | Step-Up Phase AND<br>Access Document processing |
| Applicability | M for Reader that supports Step-Up Phase        |
| Interface     | NFC                                             |

#### **Table 8-19 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions**

| Provision onto   | Remarks                                                             |
|------------------|---------------------------------------------------------------------|
| DUT (Reader)     | Credential Issuer CA Certificate or Credential Issuer CA public key |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document               |

Repeat Table 8-17 with Access Document with Issuer Certificate.

### **8.9 Step-Up Phase with Minimal Access Document with both Issuer Certificate and Key ID**

**Table 8-20 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT\_KEY\_ID test identifiers** 

| Parameter | Value                                |
|-----------|--------------------------------------|
| Test ID   | NFC_RDR_STEPUP_AD_ISSUER_CERT_KEY_ID |
| PICS      | Step-Up Phase AND                    |
|           | Access Document processing           |

![](_page_107_Picture_12.jpeg)

| Applicability | M for Reader that supports Step-Up Phase |
|---------------|------------------------------------------|
| Interface     | NFC                                      |

**Table 8-21 NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT\_KEY\_ID test pre-conditions** 

| Provision onto   | Remarks                                                                             |
|------------------|-------------------------------------------------------------------------------------|
| DUT (Reader)     | IssuerKey_PubK, Credential Issuer CA Certificate or Credential Issuer CA public key |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document                               |

Repeat Table 8-17 with Access Document with Issuer Certificate and Key Identifier.

# **8.10 Step-Up Phase with Access Document with AccessRule**

**Table 8-22 NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_STEPUP_AD_ACCESS_RULE                   |
| PICS          | Step-Up Phase AND                               |
|               | Access Data element verification – Access Rules |
| Applicability | M for Reader that supports Step-Up Phase        |
| Interface     | NFC                                             |

NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with AccessRule.

### **8.11 Step-Up Phase with Access Document with AccessRule using Schedules**

**Table 8-23 NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE\_SCHEDULES test identifiers** 

| Parameter     | Value                                                                |
|---------------|----------------------------------------------------------------------|
| Test ID       | NFC_RDR_STEPUP_AD_ACCESS_RULE_SCHEDULES                              |
| PICS          | Step-Up Phase AND                                                    |
|               | Access Data element verification – Access Rules AND Schedules        |
| Applicability | M for Reader that supports Step-Up Phase and that supports schedules |
| Interface     | NFC                                                                  |

NFC\_RDR\_STEPUP\_AD\_ACCESS\_RULE\_SCHEDULES test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with AccessRule with schedules.

![](_page_108_Picture_16.jpeg)

### **8.12 Step-Up Phase with Access Document with Unknown NonAccessExtension**

**Table 8-24 NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_ACCESS\_EXTENSION test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_STEPUP_AD_UNKNOWN_NON_ACCESS_EXTENSION  |
| PICS          | Step-Up Phase AND<br>Access Document processing |
| Applicability | M for Reader that supports Step-Up Phase        |
| Interface     | NFC                                             |

#### **Table 8-25 NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_ACCESS\_EXTENSION test pre-conditions**

| Provision onto   | Remarks                                                                   |
|------------------|---------------------------------------------------------------------------|
| DUT (Reader)     | IssuerKey_PubK, does not parse Extensions from Vendor_RegisteredID 000001 |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document                     |

Repeat Table 8-17 with Access Document with unknown nonAccessExtension.

# **8.13 Step-Up Phase with Access Document with Unknown Non-Critical AccessExtension**

**Table 8-26 NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_CRITICAL\_ACCESS\_EXTENSION test identifiers** 

| Parameter     | Value                                                   |
|---------------|---------------------------------------------------------|
| Test ID       | NFC_RDR_STEPUP_AD_UNKNOWN_NON_CRITICAL_ACCESS_EXTENSION |
| PICS          | Step-Up Phase AND<br>Access Document processing         |
| Applicability | M for Reader that supports Step-Up Phase                |
| Interface     | NFC                                                     |

NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_CRITICAL\_ACCESS\_EXTENSION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_ UNKNOWN\_NON\_ACCESS\_EXTENSION test pre-conditions in Table 8-25.

Repeat Table 8-17 with Access Document with unknown non-critical AccessExtension.

### **8.14 Step-Up Phase with Access Document with No Issuer Certificate or Key ID**

**Table 8-27 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ISSUER\_CERT\_NO\_KEY\_ID test identifiers** 

| Parameter | Value                                          |
|-----------|------------------------------------------------|
| Test ID   | NFC_RDR_NEG_STEPUP_AD_NO_ISSUER_CERT_NO_KEY_ID |
| PICS      | Step-Up Phase AND                              |

![](_page_109_Picture_16.jpeg)

|               | Access Document processing               |
|---------------|------------------------------------------|
| Applicability | M for Reader that supports Step-Up Phase |
| Interface     | NFC                                      |

NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ISSUER\_CERT\_NO\_KEY\_ID test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with no issuer certificate and no key identifier. EXCHANGE command indicates transaction failure for test to pass.

### **8.15 Step-Up Phase with Access Document with Issuer Certificate with Invalid Signature**

**Table 8-28 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_INVALID\_SIGNATURE test identifiers** 

| Parameter     | Value                                               |
|---------------|-----------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERT_INVALID_SIGNATURE |
| PICS          | Step-Up Phase AND                                   |
|               | Access Document processing                          |
| Applicability | M for Reader that supports Step-Up Phase            |
| Interface     | NFC                                                 |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_INVALID\_SIGNATURE test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions in Table 8-19.

Repeat Table 8-17 with Access Document with issuer invalid signature. EXCHANGE command indicates transaction failure for test to pass.

### **8.16 Step-Up Phase with Access Document with Expired Issuer Certificate**

**Table 8-29 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_EXPIRED test identifiers** 

| Parameter     | Value                                                                            |
|---------------|----------------------------------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD _ISSUER_CERT_EXPIRED                                       |
| PICS          | Step-Up Phase AND<br>Access Document verification – Validate time-based elements |
| Applicability | M for Reader that supports time concept and Step-Up Phase                        |
| Interface     | NFC                                                                              |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERT\_EXPIRED test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions in Table 8-19.

Repeat Table 8-17 with Access Document with expired issuer certificate. EXCHANGE command indicates transaction failure for test to pass.

![](_page_110_Picture_15.jpeg)

### **8.17 Step-Up Phase with Access Document with Invalid Signature in IssuerAuth**

**Table 8-30 NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_SIGNATURE\_ISSUER\_AUTH test identifiers** 

| Parameter     | Value                                               |
|---------------|-----------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_INVALID_SIGNATURE_ISSUER_AUTH |
| PICS          | Step-Up Phase AND                                   |
|               | Access Document processing                          |
| Applicability | M for Reader that supports Step-Up Phase            |
| Interface     | NFC                                                 |

NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_SIGNATURE\_ISSUER\_AUTH test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with invalid signature in IssuerAuth. EXCHANGE command indicates transaction failure for test to pass.

### **8.18 Step-Up Phase with Access Document with Invalid Hash in IssuerAuth**

**Table 8-31 NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_HASH\_ISSUER\_AUTH test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_INVALID_HASH_ISSUER_AUTH  |
| PICS          | Step-Up Phase AND<br>Access Document processing |
| Applicability | M for Reader that supports Step-Up Phase        |
| Interface     | NFC                                             |

NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_HASH\_ISSUER\_AUTH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with invalid hash in IssuerAuth. EXCHANGE command indicates transaction failure for test to pass.

### **8.19 Step-Up Phase with Access Document with Expired IssuerAuth**

**Table 8-32 NFC\_RDR\_NEG\_STEPUP\_AD\_EXPIRED\_ISSUER\_AUTH test identifiers** 

| Parameter     | Value                                                       |
|---------------|-------------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_EXPIRED_ISSUER_AUTH                   |
| PICS          | Step-Up Phase AND                                           |
|               | Access Document verification – Validate time-based elements |
| Applicability | M for Reader that supports time concept and Step-Up Phase   |
| Interface     | NFC                                                         |

![](_page_111_Picture_15.jpeg)

NFC\_RDR\_NEG\_STEPUP\_AD\_EXPIRED\_ISSUER\_AUTH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with expired IssuerAuth. EXCHANGE command indicates transaction failure for test to pass.

# **8.20 Step-Up Phase with Access Document with Early IssuerAuth**

**Table 8-33 NFC\_RDR\_NEG\_STEPUP\_AD\_EARLY\_ISSUER\_AUTH test identifiers** 

| Parameter     | Value                                                                          |
|---------------|--------------------------------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_EARLY_ISSUER_AUTH                                        |
| PICS          | Step-Up Phase AND<br>Access Document processing – Validate time-based elements |
| Applicability | M for Reader that supports time concept and Step-Up Phase                      |
| Interface     | NFC                                                                            |

NFC\_RDR\_NEG\_STEPUP\_AD\_EARLY\_ISSUER\_AUTH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with early IssuerAuth. EXCHANGE command indicates transaction failure for test to pass.

### **8.21 Step-Up Phase with Access Document with Issuer Certificate Time Mismatch**

**Table 8-34 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERTIFICATE\_TIME\_MISMATCH test identifiers** 

| Parameter     | Value                                                  |
|---------------|--------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_ISSUER_CERTIFICATE_TIME_MISMATCH |
| PICS          | Step-Up Phase AND<br>Access Document processing        |
| Applicability | M for Reader that supports Step-Up Phase               |
| Interface     | NFC                                                    |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_CERTIFICATE\_TIME\_MISMATCH test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_ISSUER\_CERT test pre-conditions in Table 8-19.

Repeat Table 8-17 with Access Document with Issuer Certificate validity time does not match "signed" date. EXCHANGE command indicates transaction failure for test to pass.

### **8.22 Step-Up Phase with Access Document with ValidityIteration**

**Table 8-35 NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test identifiers** 

| Parameter | Value                                    |
|-----------|------------------------------------------|
| Test ID   | NFC_RDR_NEG_STEPUP_AD_VALIDITY_ITERATION |
| PICS      | Step-Up Phase AND                        |

![](_page_112_Picture_17.jpeg)

|               | Access Document verification – Validity Iteration |
|---------------|---------------------------------------------------|
| Applicability | M for Reader that supports Step-Up Phase          |
| Interface     | NFC                                               |

NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

**Table 8-36 NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test steps** 

| Step# | TH (User Device)                                              | DUT (Reader) | Verification at TH                                                                                                                                                     |
|-------|---------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps<br>(Table 8-17)   |              | Verify the following:<br>Tag 0x97 (Reader Status) value in<br>EXCHANGE command matches the<br>expected result.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | Repeat step 1 for each testable Access Document, in<br>order. |              | Verify<br>Criteria for all iterations is met.<br>If all criteria are met, then PASS else<br>FAIL.                                                                      |

#### **Table 8-37 NFC\_RDR\_NEG\_STEPUP\_AD\_VALIDITY\_ITERATION test iterations**

| Iteration | Access Credential   | Access Document                               | Expected Result                                 |
|-----------|---------------------|-----------------------------------------------|-------------------------------------------------|
| 1         | Access Credential 1 | Minimal Document with Validity Iteration of 1 | Access Granted<br>(0x97 first byte is<br>0x01h) |
| 2         | Access Credential 2 | Minimal Document with Validity Iteration of 9 | Access Granted<br>(0x97 first byte is<br>0x01h) |
| 3         | Access Credential 1 | Minimal Document with Validity Iteration of 3 | Access Granted<br>(0x97 first byte is<br>0x01h) |
| 4         | Access Credential 3 | Minimal Document with Validity Iteration of 1 | Access Denied (0x97<br>first byte is 0x00h)     |

### **8.23 Step-Up Phase with Access Document with TimeVerificationRequired**

#### **Table 8-38 NFC\_RDR\_NEG\_STEPUP\_AD\_TIME\_VERIFICATION\_REQUIRED test identifiers**

| Parameter     | Value                                                                      |
|---------------|----------------------------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_TIME_VERIFICATION_REQUIRED                           |
| PICS          | Step-Up Phase AND                                                          |
|               | Access Document verification – Validate time-based elements                |
| Applicability | M for Reader that supports Step-Up Phase and does not support time concept |

![](_page_113_Picture_11.jpeg)

| Interface | NFC |
|-----------|-----|
|           |     |

NFC\_RDR\_NEG\_STEPUP\_AD\_TIME\_VERIFICATION\_REQUIRED test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with Issuer Certificate with TimeVerificationRequired set and reader cannot determine time. EXCHANGE command indicates transaction failure for test to pass.

# **8.24 Step-Up Phase with Access Document with No Data Elements**

**Table 8-39 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_DATA\_ELEMENTS test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_NO_DATA_ELEMENTS          |
| PICS          | Step-Up Phase AND<br>Access Document processing |
| Applicability | M for Reader that supports Step-Up Phase        |
| Interface     | NFC                                             |

NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_DATA\_ELEMENTS test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with no data elements. EXCHANGE command indicates transaction failure for test to pass.

### **8.25 Step-Up Phase with Access Document with IssuerAuth docType Mismatch**

**Table 8-40 NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_DOCTYPE\_MISMATCH test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_ISSUER_DOCTYPE_MISMATCH   |
| PICS          | Step-Up Phase AND<br>Access Document processing |
| Applicability | M for Reader that supports Step-Up Phase        |
| Interface     | NFC                                             |

NFC\_RDR\_NEG\_STEPUP\_AD\_ISSUER\_DOCTYPE\_MISMATCH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with IssuerAuth doctype does not match document docType. EXCHANGE command indicates transaction failure for test to pass.

### **8.26 Step-Up Phase with Access Document with docType Not Aliro-a**

| Parameter | Value                                    |
|-----------|------------------------------------------|
| Test ID   | NFC_RDR_NEG_STEPUP_AD_DOCTYPE_NOT_ALIROA |

![](_page_114_Picture_17.jpeg)

| PICS          | Step-Up Phase AND                        |
|---------------|------------------------------------------|
|               | Access Document processing               |
| Applicability | M for Reader that supports Step-Up Phase |
| Interface     | NFC                                      |

NFC\_RDR\_NEG\_STEPUP\_AD\_DOCTYPE\_NOT\_ALIROA test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with doctype not "aliro-a". EXCHANGE command indicates transaction failure for test to pass.

# **8.27 Step-Up Phase with Access Document with DeviceKeyInfo Mismatch**

**Table 8-41 NFC\_RDR\_NEG\_STEPUP\_AD\_DEVICE\_KEY\_INFO\_MISMATCH test identifiers** 

| Parameter     | Value                                           |
|---------------|-------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_DEVICE_KEY_INFO_MISMATCH  |
| PICS          | Step-Up Phase AND<br>Access Document processing |
| Applicability | M for Reader that supports Step-Up Phase        |
| Interface     | NFC                                             |

NFC\_RDR\_NEG\_STEPUP\_AD\_DEVICE\_KEY\_INFO\_MISMATCH test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with deviceKeyInfo does not match Access Credential. EXCHANGE command indicates transaction failure for test to pass.

# **8.28 Step-Up Phase with Access Document with Invalid Access Data Element Version**

**Table 8-42 NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_ACCESS\_DATA\_ELEMENT\_VERSION test identifiers** 

| Parameter     | Value                                                     |
|---------------|-----------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_INVALID_ACCESS_DATA_ELEMENT_VERSION |
| PICS          | Step-Up Phase AND<br>Access Document processing           |
| Applicability | M for Reader that supports Step-Up Phase                  |
| Interface     | NFC                                                       |

NFC\_RDR\_NEG\_STEPUP\_AD\_INVALID\_ACCESS\_DATA\_ELEMENT\_VERSION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with invalid access data element version. EXCHANGE command indicates transaction failure for test to pass.

### **8.29 Step-Up Phase with Access Document with No AccessRule for Intended Reader Action**

**Table 8-43 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ACCESS\_RULE\_FOR\_READER\_ACTION test identifiers** 

| Parameter     | Value                                                  |
|---------------|--------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_NO_ACCESS_RULE_FOR_READER_ACTION |
| PICS          | Step-Up Phase AND                                      |
|               | Access Document processing                             |
| Applicability | M for Reader that supports Step-Up Phase               |
| Interface     | NFC                                                    |

NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_ACCESS\_RULE\_FOR\_READER\_ACTION test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with no AccessRule for intended reader action. EXCHANGE command indicates transaction failure for test to pass.

# **8.30 Step-Up Phase with Access Document with No Valid Schedule in AccessRule AllowScheduleIds**

**Table 8-44 NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_VALID\_SCHEDULE\_ALLOW\_SCHEDULEID test identifiers** 

| Parameter     | Value                                                                |
|---------------|----------------------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_NO_VALID_SCHEDULE_ALLOW_SCHEDULEID             |
| PICS          | Step-Up Phase AND<br>Access Data Element verification - Schedules    |
| Applicability | M for Reader that supports Step-Up Phase and that supports schedules |
| Interface     | NFC                                                                  |

NFC\_RDR\_NEG\_STEPUP\_AD\_NO\_VALID\_SCHEDULE\_ALLOW\_SCHEDULEID test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with no valid schedule in AccessRule AllowScheduleIds. EXCHANGE command indicates transaction failure for test to pass.

# **8.31 Step-Up Phase with Access Document with Valid Schedule in AccessRule DenyScheduleIds**

**Table 8-45 NFC\_RDR\_NEG\_STEPUP\_AD\_VALID\_SCHEDULE\_DENY\_SCHEDULEID test identifiers** 

| Parameter | Value                                                |
|-----------|------------------------------------------------------|
| Test ID   | NFC_RDR_NEG_STEPUP_AD_VALID_SCHEDULE_DENY_SCHEDULEID |

![](_page_116_Picture_16.jpeg)

| PICS          | Step-Up Phase AND                                                    |
|---------------|----------------------------------------------------------------------|
|               | Access Document processing - Schedules                               |
| Applicability | M for Reader that supports Step-Up Phase and that supports schedules |
| Interface     | NFC                                                                  |

NFC\_RDR\_NEG\_STEPUP\_AD\_VALID\_SCHEDULE\_DENY\_SCHEDULEID test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with valid schedule in AccessRule DenyScheduleIds. EXCHANGE command indicates transaction failure for test to pass.

### **8.32 Step-Up Phase with Access Document with Schedule in AccessRule and TimeVerifyRequired**

**Table 8-46 NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_TIME\_VERIFY\_REQUIRED test identifiers** 

| Parameter     | Value                                                                                     |
|---------------|-------------------------------------------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_TIME_VERIFY_REQUIRED                                       |
| PICS          | Step-Up Phase AND<br>NOT Access Document verification – Time-based elements               |
| Applicability | M for Reader that supports Step-Up Phase and that does not support time-based<br>elements |
| Interface     | NFC                                                                                       |

NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_TIME\_VERIFY\_REQUIRED test preconditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

Repeat Table 8-17 with Access Document with schedule in AccessRule and TimeVerifyRequired. EXCHANGE command indicates transaction failure for test to pass.

# **8.33 Step-Up Phase with Access Document with Schedule in AccessRule with No Reader Support**

**Table 8-47 NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_IN\_ACCESS\_RULE\_AND\_READER test identifiers** 

| Parameter     | Value                                                                        |
|---------------|------------------------------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_SCHEDULE_IN_ACCESS_RULE_AND_READER                     |
| PICS          | Step-Up Phase AND<br>NOT Access Document verification - Schedules            |
| Applicability | M for Reader that supports Step-Up Phase and that does not support schedules |
| Interface     | NFC                                                                          |

NFC\_RDR\_NEG\_STEPUP\_AD\_SCHEDULE\_IN\_ACCESS\_RULE\_AND\_READER test pre-conditions are identical to NFC\_RDR\_STEPUP\_AD\_KEY\_ID test pre-conditions in Table 8-16.

![](_page_117_Picture_14.jpeg)

Repeat Table 8-17 with Access Document with schedule in AccessRule and Reader. EXCHANGE command indicates transaction failure for test to pass.

### **8.34 Step-Up Phase with Access Document with Unknown ReaderRule**

**Table 8-48 NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_READER\_RULE test identifiers** 

| Parameter     | Value                                     |
|---------------|-------------------------------------------|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_READER_RULE |
| PICS          | Step-Up Phase AND                         |
|               | Access Document processing                |
| Applicability | M for Reader that supports Step-Up Phase  |
| Interface     | NFC                                       |

**Table 8-49 NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_READER\_RULE test pre-conditions** 

| Provision onto   | Remarks                                                               |  |
|------------------|-----------------------------------------------------------------------|--|
| DUT (Reader)     | IssuerKey_PubK, does not store a Reader Rule with ReaderRuleId 0xF118 |  |
| TH (User Device) | reader_PubK, reader_group_identifier, Access Document                 |  |

Repeat Table 8-17 with Access Document with unknown ReaderRule. EXCHANGE command indicates transaction failure for test to pass.

# **8.35 Step-Up Phase with Access Document with Unknown Critical AccessExtension**

**Table 8-50 NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_CRITICAL\_ACCESS\_EXTENSION test identifiers** 

| Parameter     | Value                                                   |  |
|---------------|---------------------------------------------------------|--|
| Test ID       | NFC_RDR_NEG_STEPUP_AD_UNKNOWN_CRITICAL_ACCESS_EXTENSION |  |
| PICS          | Step-Up Phase AND<br>Access Document processing         |  |
| Applicability | M for Reader that supports Step-Up                      |  |
| Interface     | NFC                                                     |  |

NFC\_RDR\_NEG\_STEPUP\_AD\_UNKNOWN\_CRITICAL\_ACCESS\_EXTENSION test pre-conditions are identical to

NFC\_RDR\_STEPUP\_AD\_UNKNOWN\_NON\_ACCESS\_EXTENSION test preconditions in Table 8-25.

Repeat Table 8-17 with Access Document with unknown critical AccessExtension. EXCHANGE command indicates transaction failure for test to pass.

![](_page_118_Picture_15.jpeg)

### **8.36 Step-Up Phase with Revocation Document**

### **Table 8-51 NFC\_RDR\_STEPUP\_RD test identifiers**

| Parameter     | Value                                           |  |
|---------------|-------------------------------------------------|--|
| Test ID       | NFC_RDR_STEPUP_RD                               |  |
| PICS          | Step-Up Phase AND                               |  |
|               | Revocation document storage and retrieval AND   |  |
|               | Revocation document processing                  |  |
| Applicability | M for Reader that supports Revocation Documents |  |
| Interface     | NFC                                             |  |

#### **Table 8-52 NFC\_RDR\_STEPUP\_RD test pre-conditions**

| Provision onto   | Remarks                                                    |  |
|------------------|------------------------------------------------------------|--|
| TH (User Device) | reader_PubK, reader_group_identifier, Revocation Documents |  |
| DUT (Reader)     | Access Credential long term public keys, IssuerKey_PubK    |  |

#### **Table 8-53 NFC\_RDR\_STEPUP\_RD test steps**

| Step# | TH (User Device)                                                                                    | DUT (Reader)                                                                                                                                  | Verification at TH                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501                                 |                                                                                                                                               | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 2     | Execute AUTH0 routine (Table 6-2).                                                                  |                                                                                                                                               | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 3     | Execute AUTH1 routine (Table 6-3).                                                                  |                                                                                                                                               | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 4     |                                                                                                     | Send SELECT command<br>AID =<br>A000000909ACCE5502,<br>if Step-Up AID is<br>required is indicated in<br>signaling_bitmap in<br>AUTH1 response | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 5     | Send SELECT response                                                                                |                                                                                                                                               |                                                                                                                                                    |
| 6     |                                                                                                     | Request Revocation<br>Document using<br>DeviceRequest inside<br>ENVELOPE command.                                                             | Verify the following:<br>Revocation Document is requested in<br>ENVELOPE command response.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 7     | Send appropriate<br>Revocation Document in<br>DeviceResponse inside<br>ENVELOPE command<br>response |                                                                                                                                               |                                                                                                                                                    |
| 8     | One or more GET RESPONSE command and GET<br>RESPONSE command response can be exchanged.             |                                                                                                                                               |                                                                                                                                                    |

| Step# | TH (User Device)                                                                     | DUT (Reader) | Verification at TH                                                                                                                            |
|-------|--------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 9     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4).              |              | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                          |
| 10    | Wait for at least 3 seconds.                                                         |              |                                                                                                                                               |
|       | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps                                          |              | Verify the following:                                                                                                                         |
|       | (Table 8-17) with Access Credential 1                                                |              | Tag 0x97 matches expected result for<br>Access Credential 1.                                                                                  |
|       |                                                                                      |              | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                          |
| 11    | Wait for at least 3 seconds.                                                         |              |                                                                                                                                               |
| 12    | Execute NFC_RDR_STEPUP_AD_KEY_ID test steps<br>(Table 8-17) with Access Credential 2 |              | Verify the following:<br>Tag 0x97 matches expected result for<br>Access Credential 2.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 13    | Steps 1-12 are repeated for each testable Revocation<br>Document, in order           |              | Verify the following:<br>Criteria for all iterations is met.<br>If all criteria are met, then PASS else<br>FAIL.                              |

#### **Table 8-54 NFC\_RDR\_STEPUP\_RD test iterations**

| Iteration | Revocation Document                                                                                                               | Access Credential 1<br>Result                    | Access Credential 2<br>Result                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| 1         | Overwrite containing Access Credential 1<br>Public Key                                                                            | Access Rejected<br>(0x97 first byte is<br>0x00h) | Access Accepted<br>(0x97 first byte is<br>0x01h) |
| 2         | Update adding Access Credential 2 Public Key                                                                                      | Access Rejected                                  | Access Rejected                                  |
| 3         | Update removing Access Credential 1 Public<br>Key                                                                                 | Access Accepted                                  | Access Rejected                                  |
| 4         | Update adding Access Credential 1 Public Key<br>and removing Access Credential 1 Public Key<br>and Access Credential 2 Public Key | Access Accepted                                  | Access Accepted                                  |
| 5         | Overwrite containing Access Credential 2<br>Public Key                                                                            | Access Accepted                                  | Access Rejected                                  |
| 6         | Overwrite empty                                                                                                                   | Access Accepted                                  | Access Accepted                                  |

# **8.37 Step-Up Phase with Revocation Document with Invalid Revocation Document Version**

**Table 8-55 NFC\_RDR\_NEG\_STEPUP\_RD\_INVALID\_ELEMENT\_VERSION test identifiers** 

| Parameter | Value                                         |
|-----------|-----------------------------------------------|
| Test ID   | NFC_RDR_NEG_STEPUP_RD_INVALID_ELEMENT_VERSION |
| PICS      | Step-Up Phase AND                             |

![](_page_120_Picture_8.jpeg)

|               | Revocation document storage and retrieval AND<br>Revocation document processing |
|---------------|---------------------------------------------------------------------------------|
| Applicability | M for Reader that supports Revocation Documents                                 |
| Interface     | NFC                                                                             |

NFC\_RDR\_NEG\_STEPUP\_RD\_INVALID\_ELEMENT\_VERSION test pre-conditions are identical to NFC\_RDR\_STEPUP\_RD test pre-conditions in Table 8-52 NFC\_RDR\_STEPUP\_RD test pre-conditions

**Table 8-56 NFC\_RDR\_NEG\_STEPUP\_RD\_INVALID\_ELEMENT\_VERSION test steps** 

| Step# | TH (User Device)                                                                        | DUT (Reader)                                                                                                                                   | Verification at TH                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501                     |                                                                                                                                                | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 2     | Execute AUTH0 routine (Table 6-2).                                                      |                                                                                                                                                | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 3     | Execute AUTH1 routine (Table 6-3).                                                      |                                                                                                                                                | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 4     |                                                                                         | Send SELECT command<br>AID =<br>A000000909ACCE5502,<br>if Step-Up AID is<br>required is indicated in<br>signaling_bitmap in<br>AUTH1 response. | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                               |
| 5     | Send SELECT response.                                                                   |                                                                                                                                                |                                                                                                                                                    |
| 6     |                                                                                         | Request Revocation<br>Document using<br>DeviceRequest inside<br>ENVELOPE command.                                                              | Verify the following:<br>Revocation Document is requested in<br>ENVELOPE command response.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 7     | Send ENVELOPE<br>command response.                                                      |                                                                                                                                                |                                                                                                                                                    |
| 8     | One or more GET RESPONSE command and GET<br>RESPONSE command response can be exchanged. |                                                                                                                                                |                                                                                                                                                    |
| 9     | Execute EXCHANGE indicating transaction failure<br>routine (Table 6-5).                 |                                                                                                                                                | If all criteria are met, then PASS else<br>FAIL.                                                                                                   |

### **8.38 SELECT Response with No Common Expedited Protocol Version**

**Table 8-57 NFC\_RDR\_NEG\_SEL\_RSP\_NO\_COMMON\_EXPEDITED\_PROTOCOL\_VERSION test identifiers** 

| Parameter     | Value                                                    |
|---------------|----------------------------------------------------------|
| Test ID       | NFC_RDR_NEG_SEL_RSP_NO_COMMON_EXPEDITED_PROTOCOL_VERSION |
| PICS          | Expedited-Standard Phase                                 |
| Applicability | M for Reader                                             |

![](_page_121_Picture_9.jpeg)

| Interface | NFC |  |
|-----------|-----|--|
|           |     |  |

NFC\_RDR\_NEG\_SEL\_RSP\_NO\_COMMON\_EXPEDITED\_PROTOCOL\_VERSION test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test preconditions in Table 8-2.

**Table 8-58 NFC\_RDR\_NEG\_SEL\_RSP\_NO\_COMMON\_EXPEDITED\_PROTOCOL\_VERSION test steps** 

| Steps | TH (User Device)                                                                                | DUT<br>(Reader)                     | Verification at TH                                                                                                                                                                                                              |
|-------|-------------------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                                                                                                 | Send<br>SELECT<br>command.          | Verify the following:<br>AID =<br>1.<br>A000000909ACCE5501<br>2.<br>Format of command<br>matches the specification.<br>If all criteria are met, then<br>CONTINUE else FAIL.                                                     |
| 2     | Send SELECT Response. Set the<br>expedited_phase_supported_protocol_versions<br>equal to 0x0A00 |                                     |                                                                                                                                                                                                                                 |
| 3     |                                                                                                 | Send<br>CONTROL<br>FLOW<br>command. | Verify the following:<br>1.<br>CONTROL FLOW<br>command data field length<br>does not exceed 255 bytes.<br>2.<br>S2_parameter in command<br>data field is equal to 0x27.<br>If all criteria are met, then<br>CONTINUE else FAIL. |
| 4     | send CONTROL FLOW response.                                                                     |                                     | If all criteria are met, then PASS else<br>FAIL.                                                                                                                                                                                |

### **8.39 AUTH0 with Extra Unknown TLV**

**Table 8-59 NFC\_RDR\_NEG\_AUTH0\_EXTRA\_TAG test identifiers** 

| Parameter     | Value                       |
|---------------|-----------------------------|
| Test ID       | NFC_RDR_NEG_AUTH0_EXTRA_TAG |
| PICS          | Expedited-Standard Phase    |
| Applicability | M for Reader                |
| Interface     | NFC                         |

NFC\_RDR\_NEG\_AUTH0\_EXTRA\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

![](_page_122_Picture_10.jpeg)

**Table 8-60 NFC\_RDR\_NEG\_AUTH0\_EXTRA\_TAG test steps** 

| Steps | TH (User Device)                                                                                                                   | DUT (Reader) | Verification at TH                                   |
|-------|------------------------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501.                                                               |              | If all criteria are met, then<br>CONTINUE else FAIL. |
| 2     | Execute AUTH0 routine (Table 6-2). Extra tag can be<br>randomly injected at any location in the AUTH0 response<br>command payload. |              | If all criteria are met, then<br>CONTINUE else FAIL. |
| 3     | Execute AUTH1 routine (Table 6-3).                                                                                                 |              | If all criteria are met, then<br>CONTINUE else FAIL. |
| 4     | Execute EXCHANGE indicating transaction success routine<br>(Table 6-4).                                                            |              | If all criteria are met, then PASS<br>else FAIL.     |

### **8.40 AUTH0 with Wrong Value**

**Table 8-61 NFC\_RDR\_NEG\_AUTH0\_WRONG\_VALUE test identifiers** 

| Parameter     | Value                         |
|---------------|-------------------------------|
| Test ID       | NFC_RDR_NEG_AUTH0_WRONG_VALUE |
| PICS          | Expedited-Standard Phase      |
| Applicability | M for Reader                  |
| Interface     | NFC                           |

NFC\_RDR\_NEG\_AUTH0\_WRONG\_VALUE test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

**Table 8-62 NFC\_RDR\_NEG\_AUTH0\_WRONG\_VALUE test steps**

| Steps | TH (User Device)                                                                                          | DUT (Reader) | Verification at TH                                |
|-------|-----------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501.                                      |              | If all criteria are met, then CONTINUE else FAIL. |
| 2     | Execute AUTH0 routine (Table 6-2).<br>wrong value/length of tag in the AUTH0<br>response command payload. |              | If all criteria are met, then CONTINUE else FAIL. |
| 3     | Execute CONTROL FLOW indicating<br>transaction failure routine (Table 6-6).                               |              | If all criteria are met, then PASS else FAIL.     |

### **8.41 AUTH1 with Wrong User Device Signature**

**Table 8-63 NFC\_RDR\_NEG\_AUTH1\_WRONG\_UD\_SIGNATURE test identifiers** 

| Parameter     | Value                                |
|---------------|--------------------------------------|
| Test ID       | NFC_RDR_NEG_AUTH1_WRONG_UD_SIGNATURE |
| PICS          | Expedited-Standard Phase             |
| Applicability | M for Reader                         |

![](_page_123_Picture_13.jpeg)

|  | Interface | NFC |  |  |  |  |
|--|-----------|-----|--|--|--|--|
|--|-----------|-----|--|--|--|--|

NFC\_RDR\_NEG\_AUTH1\_WRONG\_UD\_SIGNATURE test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

**Table 8-64 NFC\_RDR\_NEG\_AUTH1\_WRONG\_UD\_SIGNATURE test steps** 

| Steps | TH (User Device)                                                                             | DUT (Reader) | Verification at TH                                   |  |
|-------|----------------------------------------------------------------------------------------------|--------------|------------------------------------------------------|--|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501.                         |              | If all criteria are met, then CONTINUE else<br>FAIL. |  |
| 2     | Execute AUTH0 routine (Table 6-2).<br>command_parameters = 0h.                               |              | If all criteria are met, then CONTINUE else<br>FAIL. |  |
| 3     | Execute AUTH1 routine (Table 6-3).<br>Send wrong User Device signature in AUTH1<br>response. |              | If all criteria are met, then CONTINUE else<br>FAIL. |  |
| 4     | Execute EXCHANGE indicating transaction failure<br>routine (Table 6-5).                      |              | If all criteria are met, then PASS else FAIL.        |  |

### **8.42 AUTH1 with Extra Tag**

**Table 8-65 NFC\_RDR\_NEG\_AUTH1\_EXTRA\_TAG test identifiers** 

| Parameter     | Value                       |  |
|---------------|-----------------------------|--|
| Test ID       | NFC_RDR_NEG_AUTH1_EXTRA_TAG |  |
| PICS          | Expedited-Standard Phase    |  |
| Applicability | M for Reader                |  |
| Interface     | NFC                         |  |

NFC\_RDR\_NEG\_AUTH1\_EXTRA\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

**Table 8-66 NFC\_RDR\_NEG\_AUTH1\_EXTRA\_TAG test steps** 

| Steps | TH (User Device)                                                                    | DUT (Reader) | Verification at TH                                   |
|-------|-------------------------------------------------------------------------------------|--------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501.                |              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | Execute AUTH0 routine (Table 6-2).<br>command_parameters = 0h.                      |              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 3     | Execute AUTH1 routine (Table 6-3).<br>Send extra unknown tag TLV in AUTH1 response. |              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4).             |              | If all criteria are met, then PASS else FAIL.        |

![](_page_124_Picture_12.jpeg)

### **8.43 AUTH1 with Wrong Values**

### **Table 8-67 NFC\_RDR\_NEG\_AUTH1\_WRONG\_VALUES test identifiers**

| Parameter     | Value                          |  |
|---------------|--------------------------------|--|
| Test ID       | NFC_RDR_NEG_AUTH1_WRONG_VALUES |  |
| PICS          | Expedited-Standard Phase       |  |
| Applicability | M for Reader                   |  |
| Interface     | NFC                            |  |

NFC\_RDR\_NEG\_AUTH1\_WRONG\_VALUES test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

**Table 8-68 NFC\_RDR\_NEG\_AUTH1\_WRONG\_VALUES test steps** 

| Steps | TH (User Device)                                                                            | DUT (Reader) | Verification at TH                                   |
|-------|---------------------------------------------------------------------------------------------|--------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501.                        |              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | Execute AUTH0 routine (Table 6-2).<br>command_parameters = 0h.                              |              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 3     | Execute AUTH1 routine (Table 6-3).<br>Send wrong value/length for tag in AUTH1<br>response. |              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 4     | Execute EXCHANGE indicating transaction<br>failure routine (Table 6-5).                     |              | If all criteria are met, then PASS else FAIL.        |

### **8.44 EXCHANGE with Reader Descriptor Tag**

#### **Table 8-69 NFC\_RDR\_EXCHANGE\_RDR\_DESCRIPTOR\_TAG test identifiers**

| Parameter     | Value                                                                    |  |
|---------------|--------------------------------------------------------------------------|--|
| Test ID       | NFC_RDR_EXCHANGE_RDR_DESCRIPTOR_TAG                                      |  |
| PICS          | Reader Descriptor tag                                                    |  |
| Applicability | M for Reader that supports sending Reader Information to the User Device |  |
| Interface     | NFC                                                                      |  |

NFC\_RDR\_EXCHANGE\_RDR\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

**Table 8-70 NFC\_RDR\_EXCHANGE\_RDR\_DESCRIPTOR\_TAG test steps** 

| Steps | TH (User Device)                                                     | DUT (Reader) | Verification at TH                                   |
|-------|----------------------------------------------------------------------|--------------|------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). Set AID =<br>A000000909ACCE5501. |              | If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | Execute AUTH0 routine (Table 6-2).<br>command_parameters = 0h.       |              | If all criteria are met, then CONTINUE<br>else FAIL. |

![](_page_125_Picture_14.jpeg)

| Steps | TH (User Device)                                                                    | DUT (Reader) | Verification at TH                                                                                                                                                                                                                                                                                                                                                                                 |
|-------|-------------------------------------------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3     | Execute AUTH1 routine (Table 6-3).<br>Send extra unknown tag TLV in AUTH1 response. |              | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                                                                                                                                                                                                                               |
| 4     | Execute EXCHANGE indicating transaction success<br>routine (Table 6-4).             |              | Verify the following in addition to<br>EXCHANGE routine:<br>1.<br>order of TLVs in EXCHANGE<br>command matches specification.<br>2.<br>All mandatory TLVs in<br>EXCHANGE command present<br>3.<br>0xAE with sub tag 0xB5 is present<br>4.<br>Format of 0xB5 matches the<br>technical specification<br>5.<br>0xAE length is less than 250 bytes<br>If all criteria are met, then PASS else<br>FAIL. |

### **8.45 Control Flow with Reader Descriptor Tag**

| Parameter     | Value                                                                    |  |
|---------------|--------------------------------------------------------------------------|--|
| Test ID       | NFC_RDR_CONTROL_FLOW_RDR_DESCRIPTOR_TAG                                  |  |
| PICS          | Reader Descriptor tag                                                    |  |
| Applicability | M for Reader that supports sending Reader Information to the User Device |  |
| Interface     | NFC                                                                      |  |

NFC\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

**Table 8-71 NFC\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test steps** 

| Steps | TH (User Device)                                                     | DUT (Reader) | Verification at TH                                                                                                                                                                                                                                                                     |
|-------|----------------------------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute<br>NFC_RDR_NEG_AUTH0_WRONG_VALUE test<br>steps (Table 8-62). |              | Verify the following in addition to<br>NFC_RDR_NEG_AUTH0_WRONG_VALUE<br>test steps:                                                                                                                                                                                                    |
|       |                                                                      |              | 1.<br>All mandatory TLVs in Control Flow<br>command are present.<br>2.<br>0x63 is present.<br>3.<br>Format of 0x63 matches the technical<br>specification.<br>4.<br>Control Flow command data field length<br>is less than 255 bytes.<br>If all criteria are met, then PASS else FAIL. |

![](_page_126_Picture_8.jpeg)

### **8.46 BLE+UWB Flow with Reader Descriptor Tag**

**Table 8-72 BLEUWB\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test identifiers** 

| Parameter     | Value                                                                    |  |
|---------------|--------------------------------------------------------------------------|--|
| Test ID       | BLEUWB_RDR_CONTROL_FLOW_RDR_DESCRIPTOR_TAG                               |  |
| PICS          | BLE + UWB Flow AND                                                       |  |
|               | Reader Descriptor tag                                                    |  |
| Applicability | M for Reader that supports sending Reader Information to the User Device |  |
| Interface     | BLE                                                                      |  |

BLEUWB\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test pre-conditions are identical to NFC\_RDR\_STANDARD\_NO\_CERT test pre-conditions in Table 8-2.

**Table 8-73 BLEUWB\_RDR\_CONTROL\_FLOW\_RDR\_DESCRIPTOR\_TAG test steps** 

| Steps | TH (User Device)                                                                        | DUT (Reader)                                                                                           | Verification at TH                                                                                                                                                                                                                         |
|-------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                                                                                         | Send Bluetooth LE<br>advertisement                                                                     | Verify the following:<br>BLE + UWB Aliro Flow Supported Bit is<br>not set to 1.<br>If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                    |
| 2     | Establish L2CAP<br>connection                                                           |                                                                                                        |                                                                                                                                                                                                                                            |
| 3     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501     |                                                                                                        |                                                                                                                                                                                                                                            |
| 4     | Execute AUTH0 routine (Table 6-2). Send wrong<br>value/length of tag in AUTH0 response. |                                                                                                        | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                                                                       |
| 5     |                                                                                         | send Event Message ID<br>carrying General Error<br>Attribute ID and Reader<br>Information Attribute ID | Verify the following:<br>1.<br>General Error Attribute ID and<br>Reader Descriptor Attribute ID are<br>present<br>2.<br>Format of Attribute IDs matches the<br>technical specification<br>If all criteria are met, then PASS else<br>FAIL. |
| 6     | BLE teardown                                                                            |                                                                                                        |                                                                                                                                                                                                                                            |

# **8.47 EXCHANGE with Mailbox Command**

This test assumes Reader Under Test can be made to send EXCHANGE with Mailbox commands.

![](_page_127_Picture_10.jpeg)

#### **Table 8-74 NFC\_RDR\_EXCHANGE\_MAILBOX test identifiers**

| Parameter     | Value                                       |
|---------------|---------------------------------------------|
| Test ID       | NFC_RDR_EXCHANGE_MAILBOX                    |
| PICS          | Mailbox                                     |
| Applicability | M for Reader that supports Mailbox commands |
| Interface     | NFC                                         |

#### **Table 8-75 NFC\_RDR\_EXCHANGE\_MAILBOX test pre-conditions**

| Provision onto      | Remarks                                                                             |
|---------------------|-------------------------------------------------------------------------------------|
| TH (User<br>Device) | Reader_PubK, reader_group_identifier, non-zero mailbox populated with existing data |
| DUT (Reader)        | Access Credential long term public key                                              |

#### **Table 8-76 NFC\_RDR\_EXCHANGE\_MAILBOX test steps**

| Steps | TH (User Device)                                                                  | DUT (Reader)                                                                                       | Verification at TH                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute SELECT routine (Table 6-1). AID =<br>A000000909ACCE5501                   |                                                                                                    | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                     |
| 2     | Execute AUTH0 routine (Table 6-2). Set<br>command_parameters = 0h.                |                                                                                                    | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                     |
| 3     | Execute AUTH1 routine (Table 6-3). Reader_Cert<br>is not presented AUTH1 command. |                                                                                                    | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                     |
| 4     |                                                                                   | Send EXCHANGE<br>command multiple<br>times with multiple<br>Mailbox commands to<br>or from mailbox | Verify the following:<br>Request format matches technical<br>specification.<br>Requests contain one or more Mailbox<br>commands.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 5     | Send EXCHANGE<br>response                                                         |                                                                                                    |                                                                                                                                                                                          |
| 6     | Verify mailbox contents                                                           |                                                                                                    | Verify the following:<br>Mailbox content format matches the technical<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                          |

### **8.48 BLE+UWB Flow with Expedited Standard Phase**

**Table 8-77 BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test identifiers** 

| Parameter | Value |
|-----------|-------|
|           |       |

![](_page_128_Picture_11.jpeg)

| Test ID       | BLEUWB_RDR_EXPEDITED_STANDARD_PHASE       |  |
|---------------|-------------------------------------------|--|
| PICS          | BLE + UWB Flow AND                        |  |
|               | UWB ranging AND                           |  |
|               | Dynamic Advertisement Tag AND             |  |
|               | Unsolicited reader status reporting AND   |  |
|               | Expedited-Standard Phase AND              |  |
|               | UWB Time Synchronization                  |  |
| Applicability | M for Reader that supports BLE + UWB Flow |  |
| Interface     | BLE                                       |  |

#### **Table 8-78 BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions**

| Provision onto                                                                                                  | Remarks                                     |  |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------|--|
| DUT (Reader)                                                                                                    | Access Credential long term public key, GRK |  |
| TH (User Device)                                                                                                | reader_PubK, reader_group_identifier, GRK   |  |
| NOTE 1: The TH (User Device) and the DUT (Reader) are in very close proximity (e.g., 1 m and line-of<br>sight). |                                             |  |
| NOTE 2: Reader is in secured state as a pre-condition.                                                          |                                             |  |

#### **Table 8-79 BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test steps**

| Steps | TH (User Device)                                              | DUT (Reader)                                                               | Verification at TH                                                                                                                                           |
|-------|---------------------------------------------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol<br>routine (Table 6-7). |                                                                            | If all criteria are met, then CONTINUE else FAIL.                                                                                                            |
| 2     | Send Time Sync<br>Message ID                                  |                                                                            |                                                                                                                                                              |
| 3     | Execute BLE+UWB Ranging Session setup<br>routine (Table 6-8). |                                                                            | If all criteria are met, then CONTINUE else FAIL.                                                                                                            |
| 4     | Allow N (e.g., 3 seconds) for UWB ranging to<br>occur         |                                                                            | Verify the following:<br>UWB packets are exchanged over UWB transport.<br>If all criteria are met, then CONTINUE else FAIL.                                  |
| 5     |                                                               | Send Reader Status<br>Changed Message ID<br>carrying State<br>Attribute ID | Verify the following:<br>State Attribute ID has second byte [B7:B0] set to<br>0x01 or 0x02 or 0x81 or 0x82.<br>If all criteria are met, then PASS else FAIL. |

### **8.49 BLE+UWB Flow with Expedited Fast Phase**

**Table 8-80 BLEUWB\_RDR\_EXPEDITED\_FAST\_PHASE test identifiers** 

| Parameter     | Value                                                              |
|---------------|--------------------------------------------------------------------|
| Test ID       | BLEUWB_RDR_EXPEDITED_FAST_PHASE                                    |
| PICS          | BLE + UWB Flow AND                                                 |
|               | UWB ranging AND                                                    |
|               | Dynamic Advertisement Tag AND                                      |
|               | Unsolicited reader status reporting AND                            |
|               | Expedited-fast                                                     |
| Applicability | M for Reader that supports BLE + UWB Flow and Expedited-Fast Phase |
| Interface     | BLE                                                                |

BLEUWB\_RDR\_EXPEDITED\_FAST\_PHASE test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-81 BLEUWB\_RDR\_EXPEDITED\_FAST\_PHASE test steps** 

| Steps | TH (User Device)                                                                    | DUT (Reader)                                                  | Verification at TH                                                                                    |
|-------|-------------------------------------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol routine<br>(Table 6-7).                       |                                                               | If all criteria are met, then CONTINUE<br>else FAIL.                                                  |
| 2     | BLE teardown.                                                                       |                                                               |                                                                                                       |
| 3     |                                                                                     | Send Bluetooth LE<br>advertisement                            |                                                                                                       |
| 4     | Establish L2CAP<br>connection                                                       |                                                               |                                                                                                       |
| 5     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501 |                                                               |                                                                                                       |
| 6     |                                                                                     | Send AUTH0 command<br>with<br>command_parameters =<br>1h      |                                                                                                       |
| 7     | Send AUTH0 response                                                                 |                                                               |                                                                                                       |
| 8     |                                                                                     | Send EXCHANGE<br>command with Tag 0x98                        | Verify the following:<br>Tag 0x98 is present.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 9     | Send EXCHANGE<br>Response                                                           |                                                               |                                                                                                       |
| 10    |                                                                                     | Send Reader Status<br>Access Protocol<br>Completed Message ID | Verify the following:<br>Ensure reader status is secured.                                             |

![](_page_130_Picture_8.jpeg)

| Steps | TH (User Device)                                                             | DUT (Reader)                                                               | Verification at TH                                                                    |
|-------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
|       |                                                                              | carrying Reader<br>Information Attribute ID                                | Format of message matches technical<br>specification.                                 |
|       |                                                                              |                                                                            | If all criteria are met, then CONTINUE<br>else FAIL.                                  |
| 11    | Send Time Sync Message<br>ID                                                 |                                                                            |                                                                                       |
| 12    | Send Ranging Message ID<br>carrying Initiate Ranging<br>Session Attribute ID |                                                                            |                                                                                       |
| 13    | Execute BLE+UWB ranging session setup routine (Table<br>6-8).                |                                                                            | If all criteria are met, then CONTINUE<br>else FAIL.                                  |
| 14    | Allow N (e.g., 3 seconds)<br>for UWB ranging to occur                        |                                                                            | Verify the following:                                                                 |
|       |                                                                              |                                                                            | UWB packets are exchanged over UWB<br>transport.                                      |
|       |                                                                              |                                                                            | If all criteria are met, then CONTINUE<br>else FAIL.                                  |
| 15    |                                                                              | Reader Status Changed<br>Message ID carrying State<br>Attribute ID is sent | Verify the following:                                                                 |
|       |                                                                              |                                                                            | State Attribute ID has second byte<br>[B7:B0] set to 0x01 or 0x02 or 0x81 or<br>0x82. |
|       |                                                                              |                                                                            | If all criteria are met, then PASS else<br>FAIL.                                      |

# **8.50 BLE+UWB Flow with Step-Up Phase**

#### **Table 8-82 BLEUWB\_RDR\_STEPUP\_PHASE test identifiers**

| Parameter     | Value                                                               |
|---------------|---------------------------------------------------------------------|
| Test ID       | BLEUWB_RDR_STEPUP_PHASE                                             |
| PICS          | BLE + UWB Flow AND                                                  |
|               | UWB ranging AND                                                     |
|               | Dynamic Advertisement Tag AND                                       |
|               | Unsolicited reader status reporting AND                             |
|               | Step-Up Phase                                                       |
| Applicability | M for Reader that supports BLE + UWB Flow and support Step-Up Phase |
| Interface     | BLE                                                                 |

#### **Table 8-83 BLEUWB\_RDR\_STEPUP\_PHASE test pre-conditions**

| Provision onto                                                                                                  | Remarks                                                     |  |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--|
| DUT (Reader)                                                                                                    | Access Credential long term public key, GRK, IssuerKey_PubK |  |
| TH (User Device)                                                                                                | reader_PubK, reader_group_identifier, GRK, Access Document  |  |
| NOTE 1: The TH (User Device) and the DUT (Reader) are in very close proximity (e.g., 1 m and line-of<br>sight). |                                                             |  |
| NOTE 2: Reader is in secured state as a pre-condition.                                                          |                                                             |  |

#### **Table 8-84 BLEUWB\_RDR\_STEPUP\_PHASE test steps**

| Steps | TH (User Device)                                                                               | DUT (Reader)                                                                 | Verification at TH                                   |
|-------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------|
| 1     |                                                                                                | Send Bluetooth LE<br>advertisement                                           | Verify the following:                                |
|       |                                                                                                |                                                                              | BLE + UWB Aliro Flow Supported Bit is set<br>to 1.   |
|       |                                                                                                |                                                                              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | Establish L2CAP<br>connection.                                                                 |                                                                              |                                                      |
| 3     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501            |                                                                              |                                                      |
| 4     | Execute AUTH0 routine. command_parameters =<br>0h<br>authentication_policy = 01h (User Device) |                                                                              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 5     | Execute AUTH1 routine.                                                                         |                                                                              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 6     |                                                                                                | Send EXCHANGE                                                                | Verify the following:                                |
|       |                                                                                                | command                                                                      | Tag 0x98 is present.                                 |
|       |                                                                                                |                                                                              | If all criteria are met, then CONTINUE else<br>FAIL. |
| 7     | Send EXCHANGE<br>response                                                                      |                                                                              |                                                      |
| 8     |                                                                                                | Request Access<br>Document using<br>DeviceRequest inside<br>ENVELOPE command |                                                      |
| 9     | Send Access Document<br>in DeviceResponse<br>inside ENVELOPE<br>command response               |                                                                              |                                                      |

![](_page_132_Picture_6.jpeg)

| Steps | TH (User Device)                                                                | DUT (Reader)                                                                                                    | Verification at TH                                                                                                                                                         |
|-------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10    | One or more GET RESPONSE command/response<br>can be exchanged                   |                                                                                                                 |                                                                                                                                                                            |
| 11    |                                                                                 | Send Reader Status<br>Access Protocol<br>Completed Message ID<br>carrying Reader<br>Information Attribute<br>ID | Verify the following:<br>Ensure reader status is secured.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 12    | Send Time Sync<br>Message ID                                                    |                                                                                                                 |                                                                                                                                                                            |
| 13    | Send Ranging Message<br>ID carrying Initiate<br>Ranging Session<br>Attribute ID |                                                                                                                 |                                                                                                                                                                            |
| 14    | Execute BLE+UWB ranging session setup routine<br>(Table 6-8).                   |                                                                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                       |
| 15    | Allow N (e.g., 3 seconds) for UWB ranging to<br>occur                           |                                                                                                                 | Verify the following:<br>UWB packets are exchanged over UWB<br>transport.<br>If all criteria are met, then CONTINUE else<br>FAIL.                                          |
| 16    |                                                                                 | Reader Status Changed<br>Message ID carrying<br>State Attribute ID is<br>sent                                   | Verify the following:<br>State Attribute ID has second byte [B7:B0] set<br>to 0x01 or 0x02 or 0x81 or 0x82.<br>If all criteria are met, then PASS else FAIL.               |

### **8.51 BLE+UWB Flow with UWB Ranging Suspend**

#### **Table 8-85 BLEUWB\_RDR\_RANGING\_SUSPEND test identifiers**

| Parameter     | Value                                     |  |
|---------------|-------------------------------------------|--|
| Test ID       | BLEUWB_RDR_RANGING_SUSPEND                |  |
| PICS          | BLE + UWB Flow AND<br>UWB ranging suspend |  |
| Applicability | M for Reader that supports BLE + UWB Flow |  |
| Interface     | BLE                                       |  |

BLEUWB\_RDR\_RANGING\_SUSPEND test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78 with the exception: The TH (User Device) and the DUT (Reader) are in close proximity (e.g., 5 m and line-of-sight).

![](_page_133_Picture_7.jpeg)

#### **Table 8-86 BLEUWB\_RDR\_RANGING\_SUSPEND test steps**

| Steps | TH (User Device)                                                               | DUT (Reader)                             | Verification at TH                                                                                                                                                                                                                        |
|-------|--------------------------------------------------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol routine<br>(Table 6-7).                  |                                          | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                                                                      |
| 2     | Send Time Sync Message ID                                                      |                                          |                                                                                                                                                                                                                                           |
| 3     | Send Ranging Message ID<br>carrying Initiate Ranging<br>Session Attribute ID   |                                          |                                                                                                                                                                                                                                           |
| 4     | Execute BLE+UWB ranging session setup routine (Table<br>6-8).                  |                                          | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                                                                      |
| 5     | Allow N (e.g., 3 seconds) for UWB ranging to occur                             |                                          | Verify the following:                                                                                                                                                                                                                     |
|       |                                                                                |                                          | UWB packets are exchanged over UWB<br>transport.                                                                                                                                                                                          |
|       |                                                                                |                                          | If all criteria are met, then CONTINUE<br>else FAIL.                                                                                                                                                                                      |
| 6     | Send Ranging Session<br>Suspend Request with correct<br>UWB Session Identifier |                                          |                                                                                                                                                                                                                                           |
| 7     |                                                                                | Send Ranging Session<br>Suspend Response | Verify the following<br>1.<br>this message is sent.<br>2.<br>format of Ranging Session Suspend<br>Response matches technical<br>specification.<br>If all criteria are met, then PASS else<br>FAIL.<br>The status can either value 0 or 1. |

### **8.52 BLE+UWB Flow with UWB Ranging Resume**

| Parameter     | Value                                     |  |
|---------------|-------------------------------------------|--|
| Test ID       | BLEUWB_RDR_RANGING_RESUME                 |  |
| PICS          | BLE + UWB Flow AND                        |  |
|               | UWB ranging resume                        |  |
| Applicability | M for Reader that supports BLE + UWB Flow |  |
| Interface     | BLE                                       |  |

BLEUWB\_RDR\_RANGING\_RESUME test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78 with the exception: The TH (User Device) and the DUT (Reader) are in close proximity (e.g., 5 m and line-of-sight).

![](_page_134_Picture_7.jpeg)

#### **Table 8-87 BLEUWB\_RDR\_RANGING\_RESUME test steps**

| Steps | TH (User Device)                                                                                                           | DUT (Reader)                                      | Verification at TH                                                                                                                                                                                                                                                                                                                     |
|-------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol<br>routine (Table 6-7).                                                              |                                                   | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                                                                                                                   |
| 2     | Send Time Sync<br>Message ID                                                                                               |                                                   |                                                                                                                                                                                                                                                                                                                                        |
| 3     | Send Ranging<br>Message ID carrying<br>Initiate Ranging<br>Session Attribute ID                                            |                                                   |                                                                                                                                                                                                                                                                                                                                        |
| 4     | Execute BLE+UWB ranging session setup routine<br>(Table 6-8).                                                              |                                                   | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                                                                                                                   |
| 5     | Allow N (e.g., 3 seconds) for UWB ranging to<br>occur                                                                      |                                                   | Verify the following:                                                                                                                                                                                                                                                                                                                  |
|       |                                                                                                                            |                                                   | UWB packets are exchanged over UWB<br>transport.                                                                                                                                                                                                                                                                                       |
|       |                                                                                                                            |                                                   | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                                                                                                                                                                                                   |
| 6     | Send Ranging<br>Message ID carrying<br>Ranging Session<br>Suspended Attribute<br>ID                                        |                                                   |                                                                                                                                                                                                                                                                                                                                        |
| 7     | 1 second after<br>previous step, send<br>Ranging Message ID<br>carrying Initiate<br>Ranging Session<br>Resume Attribute ID |                                                   |                                                                                                                                                                                                                                                                                                                                        |
| 8     |                                                                                                                            | send Ranging Session<br>Resume Request<br>Message | NOTE: For this test, the User Device and<br>Reader are next close (e.g., 5 m and line-of<br>sight) to each other.                                                                                                                                                                                                                      |
| 9     | Send Ranging Session<br>Resume Response<br>Message                                                                         |                                                   | Verify the following:<br>1.<br>Format of the message matches technical<br>specification.<br>2.<br>UWB ranging is resumed.<br>3.<br>UWB packets are exchanged over UWB<br>transport in short time (e.g., up to 3<br>seconds) after sending Ranging Session<br>Resume Response Message.<br>If all criteria are met, then PASS else FAIL. |

### **8.53 BLE+UWB Flow with Failed L2CAP**

### **Table 8-88 BLEUWB\_RDR\_NEG\_FAILED\_L2CAP test identifiers**

| Parameter | Value |
|-----------|-------|
|           |       |
|           |       |

![](_page_135_Picture_7.jpeg)

| Test ID       | BLEUWB_RDR_NEG_FAILED_L2CAP               |
|---------------|-------------------------------------------|
| PICS          | BLE + UWB Flow                            |
| Applicability | M for Reader that supports BLE + UWB Flow |
| Interface     | BLE                                       |

BLEUWB\_RDR\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-89 BLEUWB\_RDR\_NEG\_FAILED\_L2CAP test steps** 

| Steps | TH (User Device)                                      | DUT (Reader)                        | Verification at TH                                                                                                                      |
|-------|-------------------------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                                                       | Send Bluetooth LE<br>advertisement  | Verify the following:<br>BLE + UWB Aliro Flow Supported Bit is<br>not set to 1.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | send wrong Selected Aliro<br>Ble UWB Protocol Version | Establish L2CAP<br>connection fails | Verify the following:<br>L2CAP establishment fails.<br>If all criteria are met, then PASS else FAIL.                                    |

# **8.54 BLE+UWB Flow with wrong SPSM**

**Table 8-90 BLEUWB\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test identifiers** 

| Parameter     | Value                                     |
|---------------|-------------------------------------------|
| Test ID       | BLEUWB_RDR_NEG_FAILED_SPSM_L2CAP          |
| PICS          | BLE + UWB Flow                            |
| Applicability | M for Reader that supports BLE + UWB Flow |
| Interface     | BLE                                       |

BLEUWB\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-91 BLEUWB\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test steps** 

| Steps | TH (User Device)      | DUT (Reader)                        | Verification at TH                                                                                                                      |
|-------|-----------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                       | Send Bluetooth LE<br>advertisement  | Verify the following:<br>BLE + UWB Aliro Flow Supported Bit<br>is not set to 1.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | send wrong SPSM value | Establish L2CAP<br>connection fails | Verify the following:<br>L2CAP establishment fails.                                                                                     |

![](_page_136_Picture_12.jpeg)

| Steps | TH (User Device) | DUT (Reader) | Verification at TH                               |
|-------|------------------|--------------|--------------------------------------------------|
|       |                  |              | If all criteria are met, then PASS else<br>FAIL. |

### **8.55 BLE+UWB Flow with timeout before AUTH0**

**Table 8-92 BLEUWB\_RDR\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test identifiers** 

| Parameter     | Value                                     |
|---------------|-------------------------------------------|
| Test ID       | BLEUWB_RDR_NEG_TIMEOUT_BEFORE_AUTH0       |
| PICS          | BLE + UWB Flow                            |
| Applicability | M for Reader that supports BLE + UWB Flow |
| Interface     | BLE                                       |

BLEUWB\_RDR\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-93 BLEUWB\_RDR\_NEG\_TIMEOUT\_BEFORE\_AUTH0 test steps** 

| Steps | TH (User Device)                                                                    | DUT (Reader)                                                    | Verification at TH                                                                                        |
|-------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1     |                                                                                     | Send Bluetooth LE<br>advertisement                              | Verify the following:                                                                                     |
|       |                                                                                     |                                                                 | BLE + UWB Aliro Flow Supported Bit is<br>not set to 1.                                                    |
|       |                                                                                     |                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                                                      |
| 2     | Establish L2CAP<br>connection                                                       |                                                                 |                                                                                                           |
| 3     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501 |                                                                 |                                                                                                           |
| 4     |                                                                                     | Send AUTH0 command                                              |                                                                                                           |
| 5     | Wait for at least 3<br>seconds before sending<br>AUTH0 command<br>response          |                                                                 |                                                                                                           |
| 6     |                                                                                     | Send Event Message ID<br>carrying General Error<br>Attribute ID | Verify the following:                                                                                     |
|       |                                                                                     |                                                                 | Format of Event Message ID carrying<br>General Error Attribute ID matches the<br>technical specification. |
|       |                                                                                     |                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                                                      |
| 7     |                                                                                     | BLE teardown                                                    | Verify the following:                                                                                     |
|       |                                                                                     |                                                                 | BLE teardown is initiated by the DUT<br>(Reader).                                                         |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH                            |
|-------|------------------|--------------|-----------------------------------------------|
|       |                  |              | If all criteria are met, then PASS else FAIL. |

# **8.56 BLE+UWB Flow with Timeout Extension**

### **Table 8-94 BLEUWB\_RDR\_TIMEOUT\_EXTENSION test identifiers**

| Parameter     | Value                                     |
|---------------|-------------------------------------------|
| Test ID       | BLEUWB_RDR_TIMEOUT_EXTENSION              |
| PICS          | BLE + UWB Flow                            |
| Applicability | M for Reader that supports BLE + UWB Flow |
| Interface     | BLE                                       |

BLEUWB\_RDR\_TIMEOUT\_EXTENSION test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

### **Table 8-95 BLEUWB\_RDR\_TIMEOUT\_EXTENSION test steps**

| Steps | TH (User Device)                                                                     | DUT (Reader)                       | Verification at TH                                     |
|-------|--------------------------------------------------------------------------------------|------------------------------------|--------------------------------------------------------|
| 1     |                                                                                      | Send Bluetooth LE<br>advertisement | Verify the following:                                  |
|       |                                                                                      |                                    | BLE + UWB Aliro Flow Supported Bit is<br>not set to 1. |
|       |                                                                                      |                                    | If all criteria are met, then CONTINUE else<br>FAIL.   |
| 2     | Establish L2CAP<br>connection                                                        |                                    |                                                        |
| 3     | Send Initiate Access<br>Protocol Message ID<br>carrying AID =<br>A000000909ACCE5501  |                                    |                                                        |
| 4     |                                                                                      | Send AUTH0<br>command              |                                                        |
| 5     | Send Event carrying Busy<br>Attribute ID at 1 s after<br>receiving AUTH0<br>command  |                                    |                                                        |
| 6     | Send AUTH0 command<br>response after 1 s after<br>sending Event Busy<br>Attribute ID |                                    |                                                        |
| 7     |                                                                                      | Send AUTH1<br>command              |                                                        |
| 8     | Send AUTH1 response                                                                  |                                    |                                                        |
| 9     |                                                                                      | Send EXCHANGE<br>with Tag 0x98     | Verify the following:<br>Tag 0x98 is present.          |

![](_page_138_Picture_9.jpeg)

| Steps | TH (User Device)          | DUT (Reader)                                                                                                    | Verification at TH                                                                                                              |
|-------|---------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
|       |                           |                                                                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                                                                            |
| 10    | Send EXCHANGE<br>response |                                                                                                                 |                                                                                                                                 |
| 11    |                           | Send Reader Status<br>Access Protocol<br>Completed Message<br>ID carrying Reader<br>Information Attribute<br>ID | Verify the following:<br>Format of message matches technical<br>specification.<br>If all criteria are met, then PASS else FAIL. |

### **8.57 BLE+UWB Flow with M2 Message Mismatch Parameter**

#### **Table 8-96 BLEUWB\_RDR\_NEG\_M2\_MISMATCH\_PARAMETER test identifiers**

| Parameter     | Value                                     |
|---------------|-------------------------------------------|
| Test ID       | BLEUWB_RDR_NEG_M2_MISMATCH_PARAMETER      |
| PICS          | BLE + UWB Flow                            |
| Applicability | M for Reader that supports BLE + UWB Flow |
| Interface     | BLE                                       |

BLEUWB\_RDR\_NEG\_M2\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-97 BLEUWB\_RDR\_NEG\_M2\_MISMATCH\_PARAMETER test steps** 

| Steps | TH (User Device)                                                             | DUT (Reader)                                                                    | Verification at TH                                                                                                |
|-------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol routine<br>(Table 6-7).                |                                                                                 | If all criteria are met, then CONTINUE<br>else FAIL.                                                              |
| 2     | Send Time Sync Message<br>ID                                                 |                                                                                 |                                                                                                                   |
| 4     | Send Ranging Message ID<br>carrying Initiate Ranging<br>Session Attribute ID |                                                                                 |                                                                                                                   |
| 5     |                                                                              | Send Ranging Session<br>Setup M1 Message ID                                     |                                                                                                                   |
| 6     | Send Ranging Session<br>Setup M2 Message ID<br>without UWB Config ID         |                                                                                 |                                                                                                                   |
| 7     |                                                                              | Send Event with General<br>Error Attribute ID<br>indicating Wrong<br>Parameters | Verify the following:<br>Format of Event Message ID.<br>General Error Attribute ID indicates<br>Wrong Parameters. |

| Steps | TH (User Device) | DUT (Reader) | Verification at TH                               |
|-------|------------------|--------------|--------------------------------------------------|
|       |                  |              | If all criteria are met, then PASS else<br>FAIL. |
| 8     | BLE teardown     |              |                                                  |

### **8.58 BLE+UWB Flow with M4 Message Mismatch Parameter**

#### **Table 8-98 BLEUWB\_RDR\_NEG\_M4\_MISMATCH\_PARAMETER test identifiers**

| Parameter     | Value                                     |
|---------------|-------------------------------------------|
| Test ID       | BLEUWB_RDR_NEG_M4_MISMATCH_PARAMETER      |
| PICS          | BLE + UWB Flow                            |
| Applicability | M for Reader that supports BLE + UWB Flow |
| Interface     | BLE                                       |

BLEUWB\_RDR\_NEG\_M4\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-99 BLEUWB\_RDR\_NEG\_M4\_MISMATCH\_PARAMETER test steps** 

| Steps | TH (User Device)                                                                | DUT (Reader)                                                                                                    | Verification at TH                                                                                                             |
|-------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE+UWB Aliro Access Protocol routine<br>(Table 6-7).                   |                                                                                                                 | If all criteria are met, then CONTINUE else<br>FAIL.                                                                           |
| 2     | Send Time Sync<br>Message ID                                                    |                                                                                                                 |                                                                                                                                |
| 3     | Send Ranging Message<br>ID carrying Initiate<br>Ranging Session<br>Attribute ID |                                                                                                                 |                                                                                                                                |
| 4     |                                                                                 | Send Ranging Session<br>Setup M1 Message ID                                                                     |                                                                                                                                |
| 5     | Send Ranging Session<br>Setup M2 Message                                        |                                                                                                                 |                                                                                                                                |
| 6     |                                                                                 | Send Ranging Session<br>Setup M3 Message                                                                        |                                                                                                                                |
| 7     | Send Ranging Session<br>Setup M4 Message ID<br>without UWB Time0                |                                                                                                                 |                                                                                                                                |
| 15    |                                                                                 | Send Ranging Message ID<br>carrying Secure Ranging<br>Over UWB Radio Failed<br>Attribute ID or General<br>Error | Verify the following:<br>Format of this message matches the<br>specification.<br>If all criteria are met, then PASS else FAIL. |

![](_page_140_Picture_9.jpeg)

### **8.59 BLE+UWB Flow with Suspend Request Mismatch Parameter**

**Table 8-100 BLEUWB\_RDR\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test identifiers** 

| Parameter     | Value                                     |  |
|---------------|-------------------------------------------|--|
| Test ID       | BLEUWB_RDR_NEG_SUSPEND_MISMATCH_PARAMETER |  |
| PICS          | BLE + UWB Flow AND                        |  |
|               | UWB Ranging Suspend                       |  |
| Applicability | M for Reader that supports BLE + UWB Flow |  |
| Interface     | BLE                                       |  |

BLEUWB\_RDR\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-101 BLEUWB\_RDR\_NEG\_SUSPEND\_MISMATCH\_PARAMETER test steps** 

| Steps | TH (User Device)                                                                                                                            | DUT (Reader)                                                                                         | Verification at TH                                                                                                                                                    |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute<br>BLEUWB_RDR_RANGING_SUSPEND<br>test steps (Table 8-86).<br>Send Ranging Session Suspend Request<br>without UWB Session Identifier | Send Event<br>Message ID<br>carrying General<br>Error Attribute ID<br>indicating Wrong<br>Parameters | Verify the following:<br>Format of Event Message ID.<br>General Error Attribute ID<br>indicates Wrong Parameters.<br>If all criteria are met, then PASS<br>else FAIL. |

### **8.60 BLE+UWB Flow BLE Advertisement Format**

#### **Table 8-102 BLEUWB\_RDR\_ADVERTISEMENT\_FORMAT test identifiers**

| Parameter     | Value                                     |  |
|---------------|-------------------------------------------|--|
| Test ID       | BLEUWB_RDR_ADVERTISEMENT_FORMAT           |  |
| PICS          | BLE + UWB Flow AND                        |  |
|               | Dynamic advertisement tag                 |  |
| Applicability | M for Reader that supports BLE + UWB Flow |  |
| Interface     | BLE                                       |  |

#### **Table 8-103 BLEUWB\_RDR\_ADVERTISEMENT\_FORMAT test steps**

| Steps | TH (User<br>Device) | DUT (Reader)                       | Verification at TH                                                                                                               |
|-------|---------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 1     |                     | Send Bluetooth LE<br>advertisement | Verify the following:<br>advertisement data matches technical<br>specification.<br>If all criteria are met, then PASS else FAIL. |

![](_page_141_Picture_13.jpeg)

### **8.61 BLE-only Flow – RKE Unsecure**

**Table 8-104 BLERKE\_RDR\_UNSECURE test identifiers** 

| Parameter     | Value                                    |  |
|---------------|------------------------------------------|--|
| Test ID       | BLERKE_RDR_UNSECURE                      |  |
| PICS          | BLE-Only Flow AND                        |  |
|               | Unsolicited reader status reporting      |  |
| Applicability | M for Reader that supports BLE-Only Flow |  |
| Interface     | BLE                                      |  |

BLERKE\_RDR\_UNSECURE test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78. Reader is in secured state before running this test.

**Table 8-105 BLERKE\_RDR\_UNSECURE test steps** 

| Steps | TH (User Device)                                               | DUT (Reader)                                                                              | Verification at TH                                                                                                                                           |
|-------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE-Only Aliro Access Protocol<br>routine (Table 6-9). |                                                                                           | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                         |
| 2     | Send RKE Request<br>Message ID with<br>action=UNSECURE         |                                                                                           |                                                                                                                                                              |
| 3     |                                                                | Send Reader Status<br>Changed Message<br>ID carrying State<br>Attribute ID<br>(Unsecured) | Verify the following:<br>State Attribute ID has second byte [B7:B0] set<br>to 0x01 or 0x02 or 0x81 or 0x82.<br>If all criteria are met, then PASS else FAIL. |

### **8.62 BLE-only Flow – RKE Secure**

**Table 8-106 BLERKE\_RDR\_SECURE test identifiers** 

| Parameter     | Value                                    |
|---------------|------------------------------------------|
| Test ID       | BLERKE_RDR_SECURE                        |
| PICS          | BLE-Only Flow AND                        |
|               | Unsolicited reader status reporting      |
| Applicability | M for Reader that supports BLE-Only Flow |
| Interface     | BLE                                      |

BLERKE\_RDR\_SECURE test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78. Reader is in unsecured state before running this test.

![](_page_142_Picture_12.jpeg)

#### **Table 8-107 BLERKE\_RDR\_SECURE test steps**

| Steps | TH (User Device)                                               | DUT (Reader)                                                                         | Verification at TH                                                                                                                                           |
|-------|----------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Execute BLE-Only Aliro Access Protocol routine<br>(Table 6-9). |                                                                                      | If all criteria are met, then CONTINUE else<br>FAIL.                                                                                                         |
| 11    | Send RKE Request<br>Message ID with<br>action=SECURE           |                                                                                      |                                                                                                                                                              |
| 12    |                                                                | Send Reader Status<br>Changed Message ID<br>carrying State Attribute<br>ID (Secured) | Verify the following:<br>State Attribute ID has second byte [B7:B0]<br>set to 0x00 or 0x02 or 0x80 or 0x82.<br>If all criteria are met, then PASS else FAIL. |

### **8.63 BLE-Only Flow with Disallowed Expedited Fast Phase**

### **Table 8-108 BLERKE\_RDR\_NEG\_FAST test identifiers**

| Parameter     | Value                                    |
|---------------|------------------------------------------|
| Test ID       | BLERKE_RDR_NEG_FAST                      |
| PICS          | BLE-Only Flow                            |
| Applicability | M for Reader that supports BLE-Only Flow |
| Interface     | BLE                                      |

BLERKE\_RDR\_NEG\_FAST test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

#### **Table 8-109 BLERKE\_RDR\_NEG\_FAST test steps**

| Steps | TH (User Device)                                                                                                                     | DUT (Reader) | Verification at TH                                                                                 |
|-------|--------------------------------------------------------------------------------------------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------|
| 1     | Execute BLERKE_RDR_UNSECURE test<br>steps (Table 8-105) without changing the test<br>pre-conditions for<br>BLERKE_RDR_NEG_FAST test. |              | If all criteria are met,<br>then CONTINUE else<br>FAIL.                                            |
| 2     | Secure the Reader and BLE teardown                                                                                                   |              |                                                                                                    |
| 3     | Repeat steps 1 and 2, ten times.                                                                                                     |              | Verify the following:<br>Each iteration passes.<br>If all criteria are met,<br>then PASS else FAIL |

### **8.64 BLE-Only Flow with Failed L2CAP**

#### **Table 8-110 BLERKE\_RDR\_NEG\_FAILED\_L2CAP test identifiers**

| Parameter | Value |
|-----------|-------|
|           |       |

![](_page_143_Picture_13.jpeg)

| Test ID       | BLERKE_RDR_NEG_FAILED_L2CAP              |
|---------------|------------------------------------------|
| PICS          | BLE-Only Flow                            |
| Applicability | M for Reader that supports BLE-Only Flow |
| Interface     | BLE                                      |

BLERKE\_RDR\_NEG\_FAILED\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-111 BLERKE\_RDR\_NEG\_FAILED\_L2CAP test steps**

| Steps | TH (User Device)                                         | DUT (Reader)                        | Verification at TH                                                                                                                     |
|-------|----------------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                                                          | Send Bluetooth LE<br>advertisement  | Verify the following:<br>BLE-Only Aliro Flow Supported Bit is not<br>set to 1.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 2     | send wrong Selected<br>Aliro Ble UWB<br>Protocol Version | Establish L2CAP<br>connection fails | Verify the following:<br>L2CAP setup fails.<br>If all criteria are met, then PASS else FAIL.                                           |

### **8.65 BLE-Only Flow with wrong SPSM**

**Table 8-112 BLERKE\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test identifiers** 

| Parameter     | Value                                    |
|---------------|------------------------------------------|
| Test ID       | BLERKE_RDR_NEG_FAILED_SPSM_L2CAP         |
| PICS          | BLE-Only Flow                            |
| Applicability | M for Reader that supports BLE-Only Flow |
| Interface     | BLE                                      |

BLERKE\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test pre-conditions are identical to BLEUWB\_RDR\_EXPEDITED\_STANDARD\_PHASE test pre-conditions in Table 8-78.

**Table 8-113 BLERKE\_RDR\_NEG\_FAILED\_SPSM\_L2CAP test steps** 

| Steps | TH (User Device)         | DUT (Reader)                        | Verification at TH                                                                                                                     |
|-------|--------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 1     |                          | Send Bluetooth LE<br>advertisement  | Verify the following:<br>BLE-Only Aliro Flow Supported Bit is not<br>set to 1.<br>If all criteria are met, then CONTINUE<br>else FAIL. |
| 2     | send wrong SPSM<br>value | Establish L2CAP<br>connection fails | Verify the following:<br>L2CAP setup fails.<br>If all criteria are met, then PASS else<br>FAIL.                                        |

![](_page_144_Picture_12.jpeg)

### **8.66 BLE-Only Flow with Step-Up Phase**

### **Table 8-114 BLERKE\_RDR\_STEPUP\_PHASE test identifiers**

| Parameter     | Value                                                                  |
|---------------|------------------------------------------------------------------------|
| Test ID       | BLERKE_RDR_STEPUP_PHASE                                                |
| PICS          | BLE-Only Flow                                                          |
| Applicability | M for Reader that supports BLE-Only Flow AND<br>supports Step-Up Phase |
| Interface     | BLE                                                                    |

BLERKE\_RDR\_STEPUP\_PHASE test pre-conditions are identical to BLEUWB\_RDR\_STEPUP\_PHASE test pre-conditions in Table 8-83.

**Table 8-115 BLERKE\_RDR\_STEPUP\_PHASE test steps** 

| Steps | TH (User Device)                                                                        | DUT (Reader)                        | Verification at TH                                           |
|-------|-----------------------------------------------------------------------------------------|-------------------------------------|--------------------------------------------------------------|
| 1     |                                                                                         | Send Bluetooth LE<br>advertisement  | Verify the following:                                        |
|       |                                                                                         |                                     | BLE-Only Aliro Flow Supported Bit is set to<br>1.            |
|       |                                                                                         |                                     | Advertisement format matches the technical<br>specification. |
|       |                                                                                         |                                     | If all criteria are met, then CONTINUE else<br>FAIL.         |
| 2     | Establish L2CAP<br>connection                                                           |                                     |                                                              |
| 3     | Send Initiate Access<br>Protocol RKE Message<br>ID carrying AID =<br>A000000909ACCE5501 |                                     |                                                              |
| 4     |                                                                                         | Send AUTH0<br>command               | Verify the following:                                        |
|       |                                                                                         |                                     | command_parameters = 0h.                                     |
|       |                                                                                         |                                     | authentication_policy != 02h                                 |
|       |                                                                                         |                                     | authentication_policy = 01h or 03h                           |
|       |                                                                                         |                                     | If all criteria are met, then CONTINUE else<br>FAIL.         |
| 5     | Send AUTH0 response                                                                     |                                     |                                                              |
| 6     |                                                                                         | Send AUTH1<br>command               |                                                              |
| 7     | Send AUTH1 response                                                                     |                                     |                                                              |
| 8     |                                                                                         | [Optional] Send<br>EXCHANGE command |                                                              |
| 9     | Send EXCHANGE<br>response                                                               |                                     | Sent, if an EXCHANGE command is received.                    |

| Steps | TH (User Device)                                                                 | DUT (Reader)                                                                                                    | Verification at TH                                                                                                                                                         |
|-------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10    |                                                                                  | Request Access<br>Document using<br>DeviceRequest inside<br>ENVELOPE command                                    |                                                                                                                                                                            |
| 11    | Send Access Document<br>in DeviceResponse<br>inside ENVELOPE<br>command response |                                                                                                                 |                                                                                                                                                                            |
| 12    | One or more GET RESPONSE command/response<br>can be exchanged                    |                                                                                                                 |                                                                                                                                                                            |
| 13    |                                                                                  | Send Reader Status<br>Access Protocol<br>Completed Message ID<br>carrying Reader<br>Information Attribute<br>ID | Verify the following:<br>Ensure reader status is secured.<br>Format of message matches technical<br>specification.<br>If all criteria are met, then CONTINUE else<br>FAIL. |
| 14    | Send RKE Request<br>Message ID with<br>action=UNSECURE                           |                                                                                                                 |                                                                                                                                                                            |
| 15    |                                                                                  | Reader Status Changed<br>Message ID carrying<br>State Attribute ID is<br>sent                                   | Verify the following:<br>State Attribute ID has second byte [B7:B0] set<br>to 0x01 or 0x02 or 0x81 or 0x82.<br>If all criteria are met, then PASS else FAIL.               |

![](_page_146_Picture_3.jpeg)